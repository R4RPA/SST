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
    """Create Table"""
    SqlDb.create_table(conn)
    """Insert Data"""
    SqlDb.import_data(conn, input_file)
    conn.close()


if __name__ == '__main__':
    main()
