#pyinstaller --onefile --windowed --paths Lib\site-packages -i "icon.ico" app.py

import sys
from PyQt5 import QtWidgets
from sst_ui import Ui_MainWindow
import json
import os
from datetime import datetime
import Utilities.DB_Actions as SqlDb



class UiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiWindow, self).__init__()
        """Initiate GUI Window"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.reset_app()
        
        self.ui.admin_enable_edit_authenticate.clicked.connect(self.show_enable_edit)
        
    def reset_app(self):
        self.ui.edit_tool_id_label.hide()
        self.ui.edit_tool_id.hide()
    
    def show_enable_edit(self):
        self.ui.edit_tool_id_label.show()
        self.ui.edit_tool_id.show()
        

def main():
    """Initiate base path"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = root_dir + '/Database/SST.db'

    """Connect to DB"""
    conn = SqlDb.get_db_connection(db_path)

    """Get unique list of Softwares"""
    software_list = SqlDb.get_unique_values(conn, 'software')
    function_list = SqlDb.get_unique_values(conn, 'function')
    keyword_list = SqlDb.get_unique_values(conn, 'keyword')

    """Get unique list of Functions & Keywords for given Software"""
    software = 'Python' or software_list[0]
    search_dict = {'software': software}
    function_list = SqlDb.get_unique_values(conn, 'function', search_dict)
    keyword_list = SqlDb.get_unique_values(conn, 'keyword', search_dict)

    """Get unique list of Keywords for given Software and Function"""
    function = function_list[0]
    search_dict = {'software': software, 'function': function}
    keyword_list = SqlDb.get_unique_values(conn, 'keyword', search_dict)

    """Get list of Tools for given Software, Function & Keyword"""
    keyword = keyword_list[0]
    search_dict = {'software': software, 'function': function, 'keyword': keyword}
    data_json = SqlDb.get_data(conn, search_dict)
    print(json.dumps(data_json, indent=2))

    """Insert new record into ScriptInfo table"""
    SqlDb.insert_data(conn, insert_data_dict)

    """Update existing record in ScriptInfo table"""
    SqlDb.update_data(conn, update_data_dict, data_json[0]['ID'])

    """Check if data is updated in ScriptInfo table"""
    data_json = SqlDb.get_data(conn, search_dict)
    print(json.dumps(data_json, indent=2))

    """Delete row from ScriptInfo table"""
    SqlDb.delete_data(conn, data_json[0]['ID'])

    """Check if status is updated as deleted in ScriptInfo table"""
    data_json = SqlDb.get_data(conn, search_dict)
    print(json.dumps(data_json, indent=2))

    """Disconnect from DB"""
    conn.close()
    
def create_app():
    """Initiate PyQT Application"""
    app = QtWidgets.QApplication(sys.argv)
    win = UiWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # Software Search Tool
    # DONE Backend:
    #   Create SQLLite Database
    #   Insert base data
    #   Get unique values for selected column
    #   Get data - all
    #   Search data - for given Software and Keyword
    #   Create/Add new tool
    #   Edit Tool
    #   Delete Tool
    #   DB Schema/Model
    # TODO Backend:
    #   Bulk Upload
    #   Admin/Passcode
    #   Integrate backend to UI
    

    # DONE GUI:
    #   Search View
    #   Add Entry
    #   Edit Entry
    
    insert_data_dict = {
        'Team': 'Data Science',
        'Title': 'Exploratory Data Analysis',
        'Description': 'Analyzing data to gain insights',
        'Software': 'Python',
        'Keyword': 'EDA, Python, Analysis, Data',
        'Function': 'data analysis',
        'Owner': 'Sai',
        'ToolPath': 'C:/data_analysis.py',
        'Status': 'Active',
        'DocumentPath': 'C:/eda_report.pdf'
    }

    update_data_dict = {
        'Team': 'Data Science',
        'Title': 'Exploratory Data Analysis',
        'Description': 'Analyzing data to gain insights and find trends'
    }

    main()
    create_app()
