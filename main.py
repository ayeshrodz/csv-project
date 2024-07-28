import argparse
import os
import time
from datetime import datetime
from modules.config_loader import load_config
from modules.db_handler import insert_csv_to_db
from modules.pdf_generator import generate_pdf_report

def main():
    parser = argparse.ArgumentParser(description='Process CSV files and generate PDF reports.')
    parser.add_argument('-c', '--config', type=str, default='configurations/config.xml', help='Path to the configuration XML file')
    parser.add_argument('-f', '--csv_file', type=str, help='Path to the CSV file')
    parser.add_argument('-d', '--database', type=str, help='Path to the SQLite database file')
    parser.add_argument('-r', '--pdf', type=str, help='Path to the output PDF file')
    parser.add_argument('--db_only', action='store_true', help='Run only the database insertion')
    parser.add_argument('--pdf_only', action='store_true', help='Run only the PDF generation')

    args = parser.parse_args()

    # Check if both db_only and pdf_only are provided
    if args.db_only and args.pdf_only:
        raise ValueError('Both --db_only and --pdf_only cannot be run at the same time.')

    if args.pdf_only and not args.database:
        raise ValueError('Database path must be provided for PDF generation.')
    
    config = load_config(args.config)

    if not args.database:
            args.database = config['default_db']

    # Create the reports directory if it doesn't exist
    reports_dir = config['reports_directory']
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    if not args.pdf:
        args.pdf = os.path.join(reports_dir, config['default_pdf_prefix'] + datetime.now().strftime('%Y%m%d%H%M%S') + '.pdf')
    else:
        args.pdf = os.path.join(reports_dir, os.path.basename(args.pdf) + datetime.now().strftime('%Y%m%d%H%M%S') + '.pdf')

    # if not args.pdf:
    #     args.pdf = config['default_pdf_prefix'] + datetime.now().strftime('%Y%m%d%H%M%S') + '.pdf'

    if not args.pdf_only:
        insert_csv_to_db(args.csv_file, args.database, config)

    if not args.db_only:
        generate_pdf_report(args.database, args.pdf, config)

if __name__ == "__main__":
    main()
