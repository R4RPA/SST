import sqlite3
import openpyxl
from datetime import datetime
import json
import os


def create_table(conn):
    _create_db_table(conn)


def import_data(conn, input_file):
    _import_data(conn, input_file)


def get_data(conn, software=None, keyword=None):
    return _get_data(conn, software, keyword)


def get_unique_values(conn, column, software_filter=None):
    unique_list = _get_unique_values(conn, column, software_filter)
    return unique_list


def get_db_connection(db_path):
    """connect to database (create a new one if it doesn't exist)"""
    return sqlite3.connect(db_path)


def _import_data(conn, input_file):
    valid_columns = ['team', 'title', 'description', 'software',
                     'keyword', 'function', 'owner', 'toolpath', 'documentpath']
    """Open input file"""
    workbook = openpyxl.load_workbook(input_file)
    worksheet = workbook.active

    """Get the header row and create a mapping of column names to indices"""
    header_row = list(worksheet.iter_rows(min_row=2, max_row=2, values_only=True))[0]
    column_mapping = {header_row[i].lower().strip(): i for i in range(len(header_row))}

    """Get the data rows and insert them into the database"""
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        print(row)
        columns = []
        values = []
        has_valid_columns = False
        for column_name in valid_columns:
            """If the column name is not in the input file, skip it"""
            if column_name not in column_mapping:
                continue
            column_index = column_mapping[column_name]
            value = row[column_index]
            """Comma separate Keyword by + ad / """
            if column_name.lower() == 'keyword' and (isinstance(value, str) and ('+' in value or '/' in value)):
                value = str(','.join(value.split('+')).replace('/', ',')).strip().replace(" ,", ",")
            columns.append(column_name)
            values.append(value)
            has_valid_columns = True

        """Skip the row if there are no valid columns"""
        if not has_valid_columns:
            continue

        """Add the Status as Active by default and set Created_On as Current Time"""
        values.append('Active')
        values.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        """Construct the INSERT INTO query"""
        columns = ','.join(columns)
        query = f"INSERT INTO ScriptInfo ({columns}, Status, Created_On) " \
                f"VALUES ({','.join(['?'] * (len(columns.split(',')) + 2))})"

        """Insert the row into the database"""
        conn.execute(query, values)

    """Commit the changes to the database"""
    conn.commit()


def _create_db_table(conn):
    """Create table if it doesn't already exist"""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ScriptInfo'")
    result = cursor.fetchone()
    if result is None:
        cursor.execute('''
            CREATE TABLE ScriptInfo (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Team TEXT,
                Title TEXT,
                Description TEXT,
                Software TEXT,
                Keyword TEXT,
                Function TEXT,
                Owner TEXT,
                ToolPath TEXT,
                Status TEXT,
                DocumentPath TEXT,
                Created_On DATETIME,
                Edited_On DATETIME,
                Deleted_On DATETIME
            );
        ''')
    conn.commit()


def _get_data(conn, software=None, keyword=None):
    """get column names"""
    cur = conn.cursor()
    cur.execute("PRAGMA table_info('ScriptInfo')")
    columns = cur.fetchall()
    column_names = [column[1] for column in columns]

    """get entries from db"""
    if not software and not keyword:
        query = "SELECT * FROM ScriptInfo"
    else:
        query = "SELECT * FROM ScriptInfo " \
                f"WHERE Status = 'Active' and software = '{software}' and keyword  LIKE '%' || '{keyword}' || '%'"
    print(query)
    cur.execute(query)

    """get all results and convert to JSON"""
    rows = cur.fetchall()
    results = []
    for row in rows:
        result = {}
        for i in range(len(column_names)):
            result[column_names[i]] = row[i]
        results.append(result)

    json_results = json.dumps(results, indent=2)
    print(json_results)
    return json_results


def _get_unique_values(conn, column, software_filter=None):
    """Get unique values for a given column and concatenate them with comma separation"""
    if software_filter:
        query = f"SELECT GROUP_CONCAT(DISTINCT {column}) FROM ScriptInfo " \
                f"WHERE Status = 'Active' and software = '{software_filter}'"
    else:
        query = f"SELECT GROUP_CONCAT(DISTINCT {column}) FROM ScriptInfo WHERE Status = 'Active'"
    result = conn.execute(query).fetchone()[0]
    if result:
        result = sorted(result.strip().replace(" ,", ",").replace(", ", ",").split(','))
    else:
        result = []
    return result


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    input_file = root_dir + "/Input/Tools_Summary.xlsx"
    db_path = root_dir + '/Database/example.db'
    conn = get_db_connection(db_path)
    # create_table(conn)
    # import_data(conn, input_file)
    data_json = get_data(conn)
    unique_list = get_unique_values(conn, 'software')
    print('unique_list', unique_list)


if __name__ == '__main__':
    main()
