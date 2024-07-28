import xml.etree.ElementTree as ET

def load_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()

    def get_text_or_default(element, default=None):
        return element.text if element is not None else default

    config_dict = {
        'batch_size': int(get_text_or_default(root.find('batchSize'), 1000)),
        'default_db': get_text_or_default(root.find('defaultDB'), 'default.db'),
        'default_pdf_prefix': get_text_or_default(root.find('defaultPDFPrefix'), 'report_'),
        'reports_directory': get_text_or_default(root.find('reportsDirectory'), 'reports'),
        'delete_temp_html': get_text_or_default(root.find('deleteTempHtml'), 'true'),
        'pdfkit_path': get_text_or_default(root.find('pdfkitPath'), '/usr/local/bin/wkhtmltopdf'),
        'pdf_options': {},
        'sql_file_path': get_text_or_default(root.find('sqlFilePath'), 'queries.sql'),
        'query_name': get_text_or_default(root.find('queryName'), 'default_query'),
        'query_limit': int(get_text_or_default(root.find('queryLimit'), 100))
    }

    for option in root.find('pdfOptions'):
        config_dict['pdf_options'][option.get('name')] = option.text

    return config_dict