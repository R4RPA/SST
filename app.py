import os
import Utilities.DB_Actions as SqlDb


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = root_dir + '/Database/example.db'
    conn = SqlDb.get_db_connection(db_path)
    software_list = SqlDb.get_unique_values(conn, 'software')
    print('software_list', software_list)
    software = software_list[0]
    print('Search Keywords for :', software)
    keyword_list = SqlDb.get_unique_values(conn, 'keyword', software)
    print('keyword_list', keyword_list)
    keyword = keyword_list[4]
    print('Search Tools for :', keyword)
    data_json = SqlDb.get_data(conn, software, keyword)
    conn.close()


if __name__ == '__main__':
    main()
