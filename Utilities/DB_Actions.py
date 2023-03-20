import sqlite3
import openpyxl
from datetime import datetime
import json
import os
import pandas as pd

def create_table(conn):
    """connect to database"""
    _create_db_table(conn)


def create_db_auth_table(conn):
    """Create Auth table with base passcodes"""
    _create_db_auth_table(conn)
    _delete_existing_rows(conn)
    _create_base_auth_entries(conn)

def update_passcode(conn, passcode_dict):
    return _update_passcode(conn, passcode_dict)

def validate_passcode(conn, passcode_dict):
    return _validate_passcode(conn, passcode_dict)

def import_data(conn, input_file):
    """Insert data into DB from Excel file"""
    _import_data(conn, input_file)


def insert_data(conn, data_dict):
    """Insert new row into ScriptInfo table"""
    _insert_data(conn, data_dict)


def update_data(conn, data, _id):
    """Update row in ScriptInfo table"""
    _update_data(conn, data, _id)


def delete_data(conn, _id):
    """Delete row from ScriptInfo table"""
    _delete_data(conn, _id)


def get_data(conn, search_dict=None, export_as='json'):
    """Get data from DB"""
    return _get_data(conn, search_dict, export_as)


def get_unique_values(conn, column, search_dict=None):
    """Get list of values from selected column"""
    unique_list = _get_unique_values(conn, column, search_dict)
    return unique_list


def get_db_connection(db_path):
    """connect to database (create a new one if it doesn't exist)"""
    return sqlite3.connect(db_path)


def _import_data(conn, input_file):
    """Insert data into DB from Excel file"""
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


def _create_db_auth_table(conn):
    """Create table if it doesn't already exist"""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Auth'")
    result = cursor.fetchone()
    if result is None:
        cursor.execute('''
            CREATE TABLE Auth (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Passcode TEXT,
                AuthLevel TEXT
            );
        ''')
    conn.commit()

    
def _delete_existing_rows(conn):
    """Delete existing rows in Auth table if they exist"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Auth;")
    conn.commit()

def _create_base_auth_entries(conn):
    """Create a dictionary with two entries, and insert them into the Auth table"""
    auth_dict = {"passcode": 'Super#123', "authlevel": "Super"}, {"passcode": 'Admin@123', "authlevel": "Admin"}
    cursor = conn.cursor()
    for auth in auth_dict:
        cursor.execute("INSERT INTO Auth (Passcode, AuthLevel) VALUES (?, ?);", (auth['passcode'], auth['authlevel']))
    conn.commit()


def _update_passcode(conn, passcode_dict):
    """Update passcode in Auth table if old and new passcodes are valid"""
    old_passcode = passcode_dict['old_passcode']
    new_passcode = passcode_dict['new_passcode']
    cursor = conn.cursor()
    # Check if old and new passcodes are not the same as the passcode with authlevel 'Super'
    cursor.execute("SELECT Passcode FROM Auth WHERE AuthLevel = 'Super';")
    result = cursor.fetchone()
    if result is None:
        return "No passcode with authlevel 'Super' found in Auth table"
    super_passcode = result[0]
    if old_passcode == new_passcode or old_passcode == super_passcode or new_passcode == super_passcode:
        return "Invalid old and/or new passcode"
    # Replace passcode as new_passcode where passcode = old_passcode in Auth table
    cursor.execute("UPDATE Auth SET Passcode = ? WHERE Passcode = ?;", (new_passcode, old_passcode))
    conn.commit()
    return "Passcode updated successfully"


def _validate_passcode(conn, passcode_dict):
    """Validate passcode and get authlevel from Auth table"""
    passcode = passcode_dict['passcode']
    cursor = conn.cursor()
    # Check if passcode exists in Auth table
    cursor.execute("SELECT AuthLevel FROM Auth WHERE Passcode = ?;", (passcode,))
    result = cursor.fetchone()
    if result is None:
        return "Invalid passcode"
    authlevel = result[0]
    return authlevel

def _check_for_duplicate(conn, data_dict1, _id=None):
    """Check if data already exists in ScriptInfo table"""
    if _id:
        data_dict1.update({'ID': _id})
    cursor = conn.cursor()
    placeholders = ' AND '.join([f"{key} = ?" for key in data_dict1.keys()])
    sql = f'''SELECT * FROM ScriptInfo WHERE {placeholders}'''
    values = tuple(data_dict1.values())
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result is not None:
        print("Data already exists in ScriptInfo table")
        return True
    else:
        return False


def _insert_data(conn, data_dict):
    """Check if data already exists in ScriptInfo table"""
    data_exists_in_ScriptInfo = _check_for_duplicate(conn, data_dict)
    if not data_exists_in_ScriptInfo:
        """Insert new row into ScriptInfo table"""
        cursor = conn.cursor()
        data_dict.update({'Created_On': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        placeholders = ', '.join(['?' for _ in range(len(data_dict))])
        columns = ', '.join(data_dict.keys())
        values = tuple(data_dict.values())
        sql = f"INSERT INTO ScriptInfo ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, values)
        conn.commit()


def _update_data(conn, data_dict, _id):
    """Check if data already exists in ScriptInfo table"""
    data_exists_in_ScriptInfo = _check_for_duplicate(conn, data_dict, _id)
    if not data_exists_in_ScriptInfo:
        """Update row in ScriptInfo table"""
        cursor = conn.cursor()
        data_dict.update({'Edited_On': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        placeholders = ', '.join([f"{key} = ?" for key in data_dict])
        values = tuple(data_dict.values())
        sql = f"UPDATE ScriptInfo SET {placeholders} WHERE ID = ?"
        cursor.execute(sql, (*values, _id))
        conn.commit()


def _delete_data(conn, _id):
    """Check if data already exists in ScriptInfo table"""
    data_dict = {'Status': 'Deleted'}
    data_deleted_in_ScriptInfo = _check_for_duplicate(conn, data_dict, _id)
    if not data_deleted_in_ScriptInfo:
        """Delete row from ScriptInfo table"""
        cursor = conn.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE ScriptInfo SET Status='Deleted', Deleted_On='{}' WHERE ID={}".format(current_time, _id))
        conn.commit()


def _get_data(conn, search_dict=None, export_as='json'):
    """get column names"""
    cur = conn.cursor()
    cur.execute("PRAGMA table_info('ScriptInfo')")
    columns = cur.fetchall()
    column_names = [column[1] for column in columns if column]

    """get entries from db"""
    if search_dict:
        
        sw_filter = search_dict['software'] if 'software' in search_dict else None
        fn_filter = search_dict['function'] if 'function' in search_dict else None
        kw_filter = search_dict['keyword'] if 'keyword' in search_dict else None
        wildcard = search_dict['wildcard'] if 'wildcard' in search_dict else None
        
        query = "SELECT * FROM ScriptInfo WHERE Status not null "
        if wildcard and len(wildcard) > 0:
            wild_query = f"{' OR '.join([f'{col} LIKE ?' for col in column_names])}"
            query += ' and ' + wild_query
            params = ['%' + wildcard + '%' for i in range(len(column_names))]
            cur.execute(query, params)
        else:
            if sw_filter and len(sw_filter) > 0 and sw_filter != 'All':
                query += f"and software = '{search_dict['software']}'"
            if fn_filter and len(fn_filter) > 0 and fn_filter != 'All':
                query += f"and function = '{search_dict['function']}'"
            if kw_filter and len(kw_filter) > 0 and kw_filter != 'All':
                query += f"and keyword like '%{search_dict['keyword']}%'"
            cur.execute(query)
    else:
        query = "SELECT * FROM ScriptInfo"
        cur.execute(query)

    """get data from db"""
    rows = cur.fetchall()
    
    if export_as=='json':
        """get all results and convert to JSON"""
        results = []
        for row in rows:
            result = {}
            for i in range(len(column_names)):
                result[column_names[i]] = row[i]
            results.append(result)
    elif export_as=='df':
        """get all results and convert to dataframe"""
        results = pd.DataFrame(rows, columns=column_names)
    else:
        results = rows
    return results


def _get_unique_values(conn, column, search_dict=None):
    """Get unique values for a given column and concatenate them with comma separation"""
    if search_dict:
        query = f"SELECT GROUP_CONCAT(DISTINCT {column}) FROM ScriptInfo " \
                "WHERE Status = 'Active' "
        if 'software' in search_dict and search_dict['software'] != 'All':
            query += f"and software = '{search_dict['software']}'"
        if 'function' in search_dict and search_dict['function'] != 'All':
            query += f"and function = '{search_dict['function']}'"
        if 'keyword' in search_dict and search_dict['keyword'] != 'All':
            query += f"and keyword like '%{search_dict['keyword']}%'"
        
    else:
        query = f"SELECT GROUP_CONCAT(DISTINCT {column}) FROM ScriptInfo WHERE Status = 'Active'"
    db_result = conn.execute(query).fetchone()[0]
    if db_result:
        result_set = set(db_result.strip().replace(" ,", ",").replace(", ", ",").split(','))
        result_sorted = sorted(list(result_set))
        
        result = ['All']
        for item in result_sorted:
            result.append(item)
        
    else:
        result = []
    return result


def main1():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    input_file = root_dir + "/Input/Tools_Summary.xlsx"
    db_path = root_dir + '/Database/SST.db'
    conn = get_db_connection(db_path)
    # create_table(conn)
    # import_data(conn, input_file)
    data_json = get_data(conn)
    unique_list = get_unique_values(conn, 'software')

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    
    db_path = root_dir + '/Database/SST.db'
    conn = get_db_connection(db_path)
    
    passcode_dict = {'passcode': 'Admin@123'}
    authlevel = validate_passcode(conn, passcode_dict)
    print(authlevel)
    passcode_dict = {'passcode': 'Super#123'}
    authlevel = validate_passcode(conn, passcode_dict)
    print(authlevel)
    
    
    passcode_dict = {"old_passcode": 'Super#123', "new_passcode": 'Super#1123'}
    result = update_passcode(conn, passcode_dict)
    print(result)
    
    #data_json = get_data(conn)
    #unique_list = get_unique_values(conn, 'software')


if __name__ == '__main__':
    main()
