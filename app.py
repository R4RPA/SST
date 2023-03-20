#pyinstaller --onefile --windowed --paths Lib\site-packages -i "icon.ico" app.py

import sys
from PyQt5 import QtWidgets
from sst_ui import Ui_MainWindow
import json
import os
from datetime import datetime
import Utilities.DB_Actions as SqlDb
from dotenv import load_dotenv
import getpass
import zipfile
import shutil

dotenv_path = os.path.join(os.path.dirname(__file__), 'Utilities', '.env')
load_dotenv(dotenv_path)

class UiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiWindow, self).__init__()
        """Initiate DB Connection"""
        self.search_dict = {'software': None, 'function': None, 'keyword': None, 'wildcard': None}
        self.conn = get_connection()
        self.query_results_df = get_data_df(self.conn, None)
        self.max_lengths = {col: self.query_results_df[col].astype(str).map(len).max() for col in self.query_results_df.columns}
        self.sw_list = self.get_unique_list('Software')
        self.fn_list = self.get_unique_list('Function')
        self.kw_list = self.get_unique_list('Keyword')
        
        """Initiate GUI Window"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = getpass.getuser()
        self.reset_app()
        self.ui.search_open_term.textChanged.connect(self.search_wild_card)
        self.ui.admin_enable_edit_authenticate.clicked.connect(self.show_enable_edit)
        self.ui.search_software.currentIndexChanged.connect(self.software_dropdown_updated)
        self.ui.search_function.currentIndexChanged.connect(self.function_dropdown_updated)
        self.ui.search_keyword.currentIndexChanged.connect(self.keyword_dropdown_updated)
        self.ui.search_scripts_table.itemClicked.connect(self.update_desc_path)
    
        
        self.ui.search_script_tool_path_download.clicked.connect(self.download_script_path)
        self.ui.search_script_help_path_download.clicked.connect(self.download_doc_path)
        
        self.ui.save_info.clicked.connect(self.save_tool_info)
        
    
    def save_tool_info(self):
        add_header_lable = self.ui.add_header_lable.text()
        edit_tool_id = self.ui.edit_tool_id.text()
        add_title = self.ui.add_title.text()
        add_team = self.ui.add_team.text()
        add_owner = self.ui.add_owner.text()
        add_software = self.ui.add_software.text()
        add_function = self.ui.add_function.text()
        add_keyword = self.ui.add_keyword.text()
        add_description = self.ui.add_description.text()
        add_script_path = self.ui.add_script_path.text()
        add_help_path = self.ui.add_help_path.text()
        
        data_dict = {}
        
        
        data_dict = {"Team": add_team, 
                     "Title": add_title, 
                     "Description": add_description, 
                     "Software": add_software, 
                     "Keyword": add_keyword, 
                     "Function": add_function, 
                     "Owner": add_owner, 
                     "ToolPath": add_script_path, 
                     "Status": "Active", 
                     "DocumentPath": add_help_path}
    
    def download_script_path(self):
        print('download_script_path')
        str_path = self.ui.search_script_tool_path.toPlainText()
        print('str_path', str_path)
        status = self.browse_and_save(str_path)
        self.ui.statusbar.showMessage(status)
    
    def download_doc_path(self):
        str_path = self.ui.search_script_help_path.toPlainText()
        status = self.browse_and_save(str_path)
        self.ui.statusbar.showMessage(status)
        
    def browse_and_save(self, str_path):
        """Browse and save files/folders to a destination folder"""
        if not os.path.exists(str_path):
            return "Invalid path"
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dest_path = dialog.getExistingDirectory(None, "Select Folder to Save", os.path.expanduser("~"))
        if not dest_path:
            return "No destination folder selected"
        if os.path.isfile(str_path):
            file_name = os.path.basename(str_path)
            file_dest_path = os.path.join(dest_path, file_name)
            shutil.copy2(str_path, file_dest_path)
        elif os.path.isdir(str_path):
            folder_name = os.path.basename(str_path)
            zip_file_path = os.path.join(dest_path, f"{folder_name}.zip")
            with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(str_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, str_path)
                        zf.write(file_path, arcname=os.path.join(folder_name, rel_path))
        return "Files/folders saved successfully"
    
    
    def update_desc_path(self, item):
        row = item.row()
        description = self.query_results_df.loc[row, 'Description']
        tool_path = self.query_results_df.loc[row, 'ToolPath']
        doc_path = self.query_results_df.loc[row, 'DocumentPath']
        self.ui.search_description.setText(description)
        self.ui.search_script_tool_path.setText(tool_path)
        self.ui.search_script_help_path.setText(doc_path)
        
        
    def reset_app(self):
        self.ui.edit_tool_id_label.hide()
        self.ui.edit_tool_id.hide()
        self.ui.UserName1.setText(self.username)
        self.ui.UserName2.setText(self.username)
        self.ui.UserName3.setText(self.username)
        self.ui.UserName4.setText(self.username)
        self.ui.search_open_term.setText('')
        self.ui.search_software.addItems(self.sw_list)
        self.ui.search_function.addItems(self.fn_list)
        self.ui.search_keyword.addItems(self.kw_list)
        self.update_result_table()
        
        
        
    def show_enable_edit(self):
        self.ui.edit_tool_id_label.show()
        self.ui.edit_tool_id.show()
        
    def select_file_or_folder(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File or Folder", "", "All Files (*);;Folders", options=options)
        if file_path:
            self.label.setText(file_path)
    def search_wild_card(self):
        wild_card = self.ui.search_open_term.text()
        self.search_dict = {'software': None, 'function': None, 'keyword': None, 'wildcard': wild_card}
        self.update_result_table()
        
    def software_dropdown_updated(self):
        sw = self.ui.search_software.currentText()
        self.search_dict = {'software': sw, 'function': None, 'keyword': None, 'wildcard': None}
        self.fn_list = self.get_unique_list('Function')
        self.ui.search_function.clear()
        self.ui.search_function.addItems(self.fn_list)
        self.update_result_table()
        
    def function_dropdown_updated(self):
        sw = self.ui.search_software.currentText()
        fn = self.ui.search_function.currentText()
        self.search_dict = {'software': sw, 'function': fn, 'keyword': None, 'wildcard': None}
        self.kw_list = self.get_unique_list('Keyword')
        self.ui.search_keyword.clear()
        self.ui.search_keyword.addItems(self.kw_list)
        self.update_result_table()
        
    def keyword_dropdown_updated(self):
        sw = self.ui.search_software.currentText()
        fn = self.ui.search_function.currentText()
        kw = self.ui.search_keyword.currentText()
        self.search_dict = {'software': sw, 'function': fn, 'keyword': kw, 'wildcard': None}
        self.update_result_table()
    
    def update_result_table(self):
        filtered_data_df = get_data_df(self.conn, self.search_dict)
        
        # Add blank spaces to make all values in each column the same length
        for col, max_len in self.max_lengths.items():
            filtered_data_df[col] = filtered_data_df[col].astype(str).str.ljust(max_len)

        #print(len(filtered_data_df))
        #filtered_data_df = self.get_filtered_data_df()
        #print(len(filtered_data_df))
        #print(len(filtered_data_df))
        table_columns = ['ID', 'Team', 'Title', 'Owner', 'Software', 'Function', 'Keyword']
        # Set the number of rows and columns in the table widget
        self.ui.search_scripts_table.setRowCount(len(filtered_data_df))
        self.ui.search_scripts_table.setColumnCount(len(table_columns))
        # Iterate over the rows and columns of the DataFrame
        for i, row_data in filtered_data_df.iterrows():
            #print(list(row_data))
            for j, column_name in enumerate(table_columns):
                # Create a QTableWidgetItem object and set the text
                item = QtWidgets.QTableWidgetItem(str(row_data[column_name]))
                # Set the item in the corresponding cell of the table widget
                self.ui.search_scripts_table.setItem(i, j, item)
        # Force a repaint of the table widget
        self.ui.search_scripts_table.viewport().update()
        # Resize columns to fit contents
        self.ui.search_scripts_table.resizeColumnsToContents()


    def get_filtered_data_df(self):
        # Extract the three columns of interest from the dataframe
        print('get_filtered_data_df', self.search_dict)
        df_filtered = self.query_results_df
        sw_filter = self.search_dict['software']
        fn_filter = self.search_dict['function']
        kw_filter = self.search_dict['keyword']
        if sw_filter and len(sw_filter) > 0 and sw_filter != 'All':
            df_filtered = df_filtered[df_filtered['Software'].str.upper() == sw_filter.upper()]
        if fn_filter and len(fn_filter) > 0 and fn_filter != 'All':
            df_filtered = df_filtered[df_filtered['Function'].str.upper() == fn_filter.upper()]
        if kw_filter and len(kw_filter) > 0 and kw_filter != 'All':
            df_filtered = df_filtered[df_filtered['Keyword'].str.contains(kw_filter, case=False)]

        #print(df_filtered)
        return df_filtered
    
    def get_unique_list(self, field):
        # Extract the three columns of interest from the dataframe
        df_filtered = self.query_results_df[['Software', 'Function', 'Keyword']]
        
        sw_filter = self.search_dict['software']
        fn_filter = self.search_dict['function']
        kw_filter = self.search_dict['keyword']
        if sw_filter and len(sw_filter) > 0 and sw_filter != 'All':
            df_filtered = df_filtered[df_filtered['Software'] == sw_filter]
        if fn_filter and len(fn_filter) > 0 and fn_filter != 'All':
            df_filtered = df_filtered[df_filtered['Function'] == fn_filter]
        if kw_filter and len(kw_filter) > 0 and kw_filter != 'All':
            df_filtered = df_filtered[df_filtered['Keyword'].str.contains(kw_filter)]
            
        # Get unique values for Software, Function and Keyword
        if field in ['Software', 'Function']:
            unique_list = df_filtered[field].unique()
        elif field == 'Keyword':
            unique_keyword = set()
            for keywords in df_filtered['Keyword']:
                for keyword in keywords.split(','):
                    unique_keyword.add(keyword.strip())
            unique_list = sorted(list(unique_keyword))
        filter_list = ['All']
        for item in unique_list:
            filter_list.append(item)
        return filter_list
            

def get_connection():
    """Connect to DB"""
    db_path = os.getenv('DB_Path')
    conn = SqlDb.get_db_connection(db_path)
    return conn

def get_data_df(conn, search_dict):
    return SqlDb.get_data(conn=conn, search_dict=search_dict, export_as='df')
    
def get_data_json(conn, search_dict):
    return SqlDb.get_data(conn=conn, search_dict=search_dict, export_as='json')


def get_data_raw(conn, search_dict):
    return SqlDb.get_data(conn=conn, search_dict=search_dict, export_as=None)


def get_unique_list(conn, field, search_dict=None):
    return SqlDb.get_unique_values(conn, field, search_dict)


def main():
    """Connect to DB"""
    conn = get_connection()
    """Get unique list of Softwares"""
    software_list = SqlDb.get_unique_values(conn, 'software')
    function_list = SqlDb.get_unique_values(conn, 'function')
    keyword_list = SqlDb.get_unique_values(conn, 'keyword')

    """Get unique list of Functions & Keywords for given Software"""
    software = 'Python' or software_list[0]
    search_dict = {'software': software}
    function_list = SqlDb.get_unique_values(conn, 'function', search_dict)
    keyword_list = SqlDb.get_unique_values(conn, 'keyword', search_dict)
    
    data_json = get_data_json(conn=conn, search_dict=search_dict)

    """Get unique list of Keywords for given Software and Function"""
    function = function_list[0]
    search_dict = {'software': software, 'function': function}
    keyword_list = SqlDb.get_unique_values(conn, 'keyword', search_dict)

    """Get list of Tools for given Software, Function & Keyword"""
    keyword = keyword_list[0]
    search_dict = {'software': software, 'function': function, 'keyword': keyword}
    data_json = get_data_json(conn=conn, search_dict=search_dict)
    #print(1, json.dumps(data_json, indent=2))

    """Insert new record into ScriptInfo table"""
    SqlDb.insert_data(conn, insert_data_dict)

    """Update existing record in ScriptInfo table"""
    SqlDb.update_data(conn, update_data_dict, data_json[0]['ID'])

    """Check if data is updated in ScriptInfo table"""
    data_json = get_data_json(conn=conn, search_dict=search_dict)
    #print(2, json.dumps(data_json, indent=2))

    """Delete row from ScriptInfo table"""
    SqlDb.delete_data(conn, data_json[0]['ID'])

    """Check if status is updated as deleted in ScriptInfo table"""
    data_json = get_data_json(conn=conn, search_dict=search_dict)
    #print(3, json.dumps(data_json, indent=2))

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
    #   Capture current user name
    # TODO Backend:
    #   Bulk Upload
    #   Admin/Passcode
    #   Integrate Backend - GUI
    

    # DONE GUI:
    #   Search View
    #   Add/Manage Entry
    #   Bulk Upload
    #   Admin
    # TODO Backend:
    #   GUI Finetune
    
    # DONE GUI Intigration
    #   List Unique Values in Dropdowns
    #   Make Dropdowns dependent Software > Function > keyword
    #   Display all tools in grid by default
    #   Search & Filter grid based on dropdown selection
    #   Search & Filter grid based on search parameter
    #   Download Script / document to user slected folder
    # TOD GUI Intigration
    #   Add New Tool
    #   Edit Existing Tool
    #   Edit and Save Existing tool as New Tool (Multiple Versions)
    #   Bulk uplad
    #   Passcode authenticate
    
    
    
    insert_data_dict = {
        'Team': 'Data Science',
        'Title': 'Exploratory Data A Analysis',
        'Description': 'B Analyzing data to gain insights',
        'Software': 'Python',
        'Keyword': 'KIKD, Python, Analysis, Data',
        'Function': 'Analysis',
        'Owner': 'Sai',
        'ToolPath': r'C:\MySpace\Projects\learning\sst\Scripts',
        'Status': 'Active',
        'DocumentPath': r'C:\MySpace\Projects\learning\sst\Scripts\untitled0.py'
    }

    update_data_dict = {
        'Team': 'Data Science',
        'Title': 'Exploratory Data Analysis',
        'Description': 'Analyzing data to gain insights and find trends'
    }

    main()
    create_app()
