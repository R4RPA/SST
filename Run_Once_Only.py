import os
import Utilities.DB_Actions as SqlDb


def _check_database_folder():
    if not os.path.exists('Database'):
        os.makedirs('Database')


def main():
    """To be executed only on First Time Run - for tool setup"""
    _check_database_folder()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = root_dir + "/Input/Tools_Summary.xlsx"
    db_path = root_dir + '/Database/SST.db'

    """Connect to DB"""
    conn = SqlDb.get_db_connection(db_path)
    """Create Scritps Table"""
    SqlDb.create_table(conn)
    """Insert Data"""
    SqlDb.import_data(conn, input_file)
    
    
    """Create Authentication Table with base passcodes"""
    SqlDb.create_db_auth_table(conn)
    
    """Check user auth level"""
    passcode_dict = {'passcode': 'Admin@123'}
    authlevel = SqlDb.validate_passcode(conn, passcode_dict)
    print('authlevel', authlevel)
    passcode_dict = {'passcode': 'Super#123'}
    authlevel = SqlDb.validate_passcode(conn, passcode_dict)
    print('authlevel', authlevel)
    
    """Update Existing passcode"""
    passcode_dict = {"old_passcode": 'Admin@123', "new_passcode": '12345'}
    result = SqlDb.update_passcode(conn, passcode_dict)
    print('Passcode update', result)
    
    passcode_dict = {"old_passcode": 'Super#123', "new_passcode": '12345'}
    result = SqlDb.update_passcode(conn, passcode_dict)
    print('Passcode update', result)
    
    
    conn.close()


if __name__ == '__main__':
    main()
