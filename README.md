# CSV File Processing and Report Generation

This project is created to generate pdf files by uploading a csv dataset. Irrespective of the number of columns, the data will be uploaded in to a SQLite database table named 'data'. Then queries can be configurable in queries.sql file. Required query and the report configs are also configurable via config.xml file. In addition, report template is highly customizable via html & css templates.

## Setting up the environment

1. Clone the code base
2. Create a virtual environment and activate it

```
python -m venv env
source env/bin/activate

```

3. Install the required packages

```
pip install -r requirements.txt
```

## Usage

```
python main.py
    -f or --csv_file => Path to the CSV data file
    -d or --database => Path to the SQLite database file
    -r or --pdf => Name of the output PDF file (default=prefix with 'report_' + <date/time>)
    -c or --config => Path to the configuration XML file (default='configurations/config.xml')
    --db_only => Run only the database insertion
    --pdf_only => Run only the PDF generation
```

### Insert data to a datasource and generate a pdf report

`python main.py -f <csv_file_path>`

### Only to insert data in to a datasource

`python main.py -f <csv_file_path> --db_only`

#### Only to generate a pdf report from an existing datasource

`python main.py -d <datasource_path> --pdf_only`

> [!NOTE]  
> This is a GPT 3.5 [assisted project](https://chatgpt.com/share/bacddbb0-f84d-42f5-bb30-b7895d27239c) created to assess an optimal approach in processing csv files and report genration with html templates with python
