import pdfkit
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import time
import sqlite3
from modules.query_loader import load_query

def generate_pdf_report(db_path, output_pdf, config_dict):
    start_time = time.time()
    print("Starting PDF report generation...")

    query_file_path = config_dict['sql_file_path']
    query_name = config_dict['query_name']
    query_limit = config_dict['query_limit']
    query = load_query(query_file_path, query_name, query_limit)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()

    env = Environment(loader=FileSystemLoader('template/html'))
    template = env.get_template('report.html')

    html_out = template.render(columns=columns, data=data, now=datetime.now())

    # Create a temporary directory within the project directory
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp_dir = os.path.join(project_dir, 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    # Generate the HTML file name based on the PDF file name
    report_name = os.path.splitext(os.path.basename(output_pdf))[0]
    temp_html_path = os.path.join(temp_dir, f'{report_name}.html')

    with open(temp_html_path, 'w') as f:
        f.write(html_out)

    path_to_wkhtmltopdf = config_dict['pdfkit_path']
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    options = config_dict['pdf_options']

    css_path = os.path.join(os.path.dirname(__file__), '../template/css/style.css')

    try:
        pdfkit.from_string(html_out, output_pdf, options=options, configuration=pdfkit_config, css=css_path)
        # Delete the temporary HTML file if PDF generation is successful
        if config_dict.get('delete_temp_html', 'true').lower() != 'false':
            os.remove(temp_html_path)
    except OSError as e:
        print("OS error:", e)
    except Exception as e:
        print("Error generating PDF:", e)
        print(f"The HTML file is retained at {temp_html_path} for debugging.")

    end_time = time.time()
    print(f"PDF report generation completed in {end_time - start_time:.2f} seconds.")