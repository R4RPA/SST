import os
import Utilities.DB_Actions as SqlDb


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = root_dir + "/Input/Tools_Summary.xlsx"
    db_path = root_dir + '/Database/example.db'

    conn = SqlDb.get_db_connection(db_path)
    SqlDb.create_table(conn)
    SqlDb.import_data(conn, input_file)
    conn.close()


if __name__ == '__main__':
    main()
