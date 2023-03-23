#pyinstaller --onefile --windowed --paths Lib\site-packages -i "icon.ico" app.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from sst_ui import Ui_MainWindow
import os
import Utilities.DB_Actions as SqlDb
from dotenv import load_dotenv
import getpass
import zipfile
import shutil
import pandas as pd

dotenv_path = os.path.join(os.path.dirname(__file__), 'Utilities', '.env')
load_dotenv(dotenv_path)

class UiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiWindow, self).__init__()
        """Initiate DB Connection"""
        self.search_dict = {'software': None, 'function': None, 'keyword': None, 'wildcard': None, 'ActiveRecordsOnly': True}
        self.conn = get_connection()
        
        """Initiate GUI Window"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        """Assign user name"""
        self.username = getpass.getuser()
        self.usertype = 'user'
        self.ui.search_include_deleted_items.hide()
        
        """Reset app to default and get data from DB"""
        self.reset_app()
        
        """Dynamic Dropdown Lists"""
        self.ui.search_software.currentIndexChanged.connect(self.software_dropdown_updated)
        self.ui.search_function.currentIndexChanged.connect(self.function_dropdown_updated)
        self.ui.search_keyword.currentIndexChanged.connect(self.keyword_dropdown_updated)
        
        """Filter data by drowpdowns or by search term"""
        self.ui.search_by_wildcard.clicked.connect(self.search_by_wildcard)
        self.ui.search_by_filter.clicked.connect(self.search_by_filter)
        self.ui.search_by_reset.clicked.connect(self.reset_app)    
        
        """Capture user click on table row and download corresponding tools and scripts from repo"""
        self.ui.search_scripts_table.itemClicked.connect(self.update_desc_path)
        self.ui.search_description.textChanged.connect(self.updated_in_description)
        self.ui.search_script_tool_path.textChanged.connect(self.updated_in_scriptpath)
        self.ui.search_script_help_path.textChanged.connect(self.updated_in_docpath)
        self.ui.search_script_tool_path_download.clicked.connect(self.download_script_path)
        self.ui.search_script_help_path_download.clicked.connect(self.download_doc_path)
        self.ui.search_add_new_version.clicked.connect(self.prefill_add_form)
        
        """Add tool info form functions"""
        self.ui.add_script_path_browse.clicked.connect(self.browse_script_path)
        self.ui.add_help_path_browse.clicked.connect(self.browse_doc_path)        
        self.ui.add_reset.clicked.connect(lambda: self.reset_add_form(True))
        self.ui.save_info.clicked.connect(self.save_tool_info)        
        
        """Bulk upload functions"""
        self.ui.bulk_template_download.clicked.connect(self.download_data_template)  
        self.ui.bulk_upload_file.clicked.connect(self.bulk_import_data)  
        
        
        """Admin authentication and actions"""
        self.ui.admin_enable_edit_authenticate.clicked.connect(self.authenticate_user)  
        self.ui.admin_update_passcode.clicked.connect(self.update_passcode)  
        self.ui.search_include_deleted_items.stateChanged.connect(self.update_status_filter)
        self.ui.search_delete_undelete_record.clicked.connect(self.delete_undelete_record)
        
        """Exit functions"""
        self.ui.add_exit.clicked.connect(self.close)
        self.ui.bulk_exit.clicked.connect(self.close)
        self.ui.admin_exit.clicked.connect(self.close)
    
        
    def authenticate_user(self):
        """Authenticate user by passcode and enable respective actions"""
        passcode = self.ui.admin_enable_edit_passcode.text()
        if passcode and len(passcode) > 0:
            passcode_dict = {'passcode': passcode}
            authlevel = SqlDb.validate_passcode(self.conn, passcode_dict)
            if authlevel == 'Invalid passcode':
                self.ui.admin_status.setText('Authentication Unsuccessful: Invalid passcode')
            elif authlevel != 'user':
                self.ui.admin_enable_edit_passcode.setText('')
                self.usertype = authlevel
                self.ui.search_include_deleted_items.show()
                #self.ui.search_delete_undelete_record.show()
                self.ui.admin_status.setText('Authentication Successful: ' + self.usertype)
                if authlevel == 'Super':
                    pass
                
    def update_passcode(self):
        """Authenticate user by passcode and update passcode for Admin user"""
        current_passcode = self.ui.admin_update_passcode_current.text()
        new_passcode = self.ui.admin_update_passcode_new.text()
        retype_passcode = self.ui.admin_update_passcode_retype.text()
        if new_passcode != retype_passcode:
            self.ui.admin_status.setText('New passcode not matching!')
        elif current_passcode == new_passcode:
            self.ui.admin_status.setText('Old and New passcode are same!')
        else:
            self.ui.admin_update_passcode_current.setText('')
            self.ui.admin_update_passcode_new.setText('')
            self.ui.admin_update_passcode_retype.setText('')
            passcode_dict = {"old_passcode": current_passcode, "new_passcode": new_passcode}
            result = SqlDb.update_passcode(self.conn, passcode_dict)
            self.ui.admin_status.setText(result)
            
            
    def download_data_template(self):
        """Create excel template for bulk upload"""
        dest_path = self.browse_folder()
        if dest_path and len(dest_path) > 0:
            filename = "import_template.xlsx"
            file_path = os.path.join(dest_path, filename)
            valid_columns = ['sn','team', 'title', 'description', 'software', 'keyword', 'function', 'owner', 'toolpath', 'documentpath']
            df = pd.DataFrame(columns=valid_columns)
            df.to_excel(file_path, index=False)
            self.ui.bulk_status.setText('Template saved in: ' + file_path)
    
    def bulk_import_data(self):
        """Import data from Excel file"""
        src_path = self.browse_file()
        if src_path and len(src_path) > 0 and src_path.endswith('.xlsx'):
            try:
                SqlDb.import_data(self.conn, src_path)
                """Get latest tools data"""
                self.reset_app()
                """for new tools add, copy source files to repo folder"""
                self.check_and_upload_files_to_repo_folder()
                self.update_result_table()
                self.ui.bulk_status.setText('Imported data from : ' + src_path)
            except Exception as e:
                self.ui.bulk_status.setText('ERROR: ' + str(e))
        elif src_path and len(src_path) > 0:
            self.ui.bulk_status.setText('Invalid file type. Download template file and try again. ' + src_path)
            
    
    def updated_in_description(self):
        """if desction is blank hide action bttons, else enable"""
        description = self.ui.search_description.toPlainText()
        if description and len(description) > 0:
            self.ui.search_add_new_version.show()
            if self.usertype != 'user':
                self.ui.search_delete_undelete_record.show()
        else:
            self.ui.search_add_new_version.hide()
            self.ui.search_delete_undelete_record.hide()
            
    def updated_in_scriptpath(self):
        """if scriptpath is blank hide action bttons, else enable"""
        scriptpath = self.ui.search_script_tool_path.toPlainText()
        if scriptpath and len(scriptpath) > 0:
            self.ui.search_script_tool_path_download.show()
        else:
            self.ui.search_script_tool_path_download.hide()

    def updated_in_docpath(self):
        """if docpath is blank hide action bttons, else enable"""
        docpath = self.ui.search_script_help_path.toPlainText()
        if docpath and len(docpath) > 0:
            self.ui.search_script_help_path_download.show()
        else:
            self.ui.search_script_help_path_download.hide()
            
            
    def search_by_wildcard(self):
        """Search tools DB where search term in any of the column values"""
        self.ui.search_tool_id.setText('')
        self.ui.search_tool_status.setText('')
        self.ui.search_tool_version.setText('')
        self.ui.search_description.setText('')
        self.ui.search_script_tool_path.setText('')
        self.ui.search_script_help_path.setText('')
        wc = self.ui.search_open_term.text()
        self.search_dict.update({'software': None, 'function': None, 'keyword': None, 'wildcard': wc})
        self.update_result_table()
    
    
    def search_by_filter(self):
        """Filter data based on dropdown selection"""
        self.ui.search_tool_id.setText('')
        self.ui.search_tool_status.setText('')
        self.ui.search_tool_version.setText('')
        self.ui.search_description.setText('')
        self.ui.search_script_tool_path.setText('')
        self.ui.search_script_help_path.setText('')
        sw = self.ui.search_software.currentText()
        fn = self.ui.search_function.currentText()
        kw = self.ui.search_keyword.currentText()
        self.search_dict.update({'software': sw, 'function': fn, 'keyword': kw, 'wildcard': None})
        self.update_result_table()
    
    def update_status_filter(self):
        """Confirmation to filter data based status Active / Deleted"""
        self.ui.search_tool_id.setText('')
        self.ui.search_tool_status.setText('')
        self.ui.search_tool_version.setText('')
        self.ui.search_description.setText('')
        self.ui.search_script_tool_path.setText('')
        self.ui.search_script_help_path.setText('')
        IncludeDeletedItems = self.ui.search_include_deleted_items.isChecked()
        if IncludeDeletedItems:
            self.search_dict.update({'ActiveRecordsOnly': False})
        else:
            self.search_dict.update({'ActiveRecordsOnly': True})
        self.reset_app()
        
    def browse_script_path(self):
        """Select folder or file to copy"""
        script_path = self.select_file_or_folder()
        repo_path = os.getenv('Repo_Path')
        repo_path = repo_path.replace('/', '\\')
        src_path = script_path.replace('/', '\\')
        if (src_path and len(src_path) > 0 and not src_path.startswith(repo_path) 
            and not repo_path.startswith(src_path) and os.path.exists(src_path)
            and src_path not in repo_path):
            self.ui.add_toolpath.setText(src_path)
        elif src_path and len(src_path) > 0:
            self.ui.add_status.setText('Invalid folder, can not select master folder of SST Repo')
    
    def browse_doc_path(self):
        """Select folder or file to copy"""
        doc_path = self.select_file_or_folder()

        repo_path = os.getenv('Repo_Path')
        repo_path = repo_path.replace('/', '\\')
        src_path = doc_path.replace('/', '\\')
        if (src_path and len(src_path) > 0 and not src_path.startswith(repo_path) 
            and not repo_path.startswith(src_path) and os.path.exists(src_path)
            and src_path not in repo_path):
            self.ui.add_documentpath.setText(src_path)
        elif src_path and len(src_path) > 0:
            self.ui.add_status.setText('Invalid folder, can not select master folder of SST Repo')
            
    def update_result_table(self):
        """Based on query results and user selections update data grid"""
        self.ui.search_status.setText('')
        filtered_data_df = self.query_results_df.copy()
        if len(filtered_data_df) ==0:
            return False
        """Search by wild card"""
        wc = self.search_dict['wildcard']
        if wc and len(str(wc)) > 0:
            filtered_data_df = filtered_data_df[filtered_data_df.applymap(lambda x: str(wc).upper() in str(x).upper()).any(axis=1)]
        else:
            """filter by dropdown selection"""
            sw = self.search_dict['software']
            fn = self.search_dict['function']
            kw = self.search_dict['keyword']
            if sw and len(str(sw)) > 0 and sw != 'All':
                filtered_data_df = filtered_data_df[filtered_data_df['Software'] == sw]
            if fn and len(str(fn)) > 0 and fn != 'All':
                filtered_data_df = filtered_data_df[filtered_data_df['Function'] == fn]
            if kw and len(str(kw)) > 0 and kw != 'All':
                filtered_data_df = filtered_data_df[filtered_data_df['Keyword'].str.contains(kw)]
        
        """Set column width for better grid view"""
        min_length = 20
        max_lengths = {col: max(min_length, self.query_results_df[col].astype(str).map(len).max()) for col in self.query_results_df.columns}
        for col, max_len in max_lengths.items():
            filtered_data_df[col] = filtered_data_df[col].astype(str).str.ljust(int(max_len))
        
        """populate filtered data in grid view"""
        table_columns = ['ID', 'Team', 'Title', 'Owner', 'Software', 'Function', 'Keyword','Status', 'Version']
        self.ui.search_scripts_table.clearContents()
        self.ui.search_scripts_table.setRowCount(0)
        self.ui.search_scripts_table.setRowCount(len(filtered_data_df))
        self.ui.search_scripts_table.setColumnCount(len(table_columns))
        filtered_data_df = filtered_data_df.reset_index(drop=True)
        for i, row_data in filtered_data_df.iterrows():
            for j, column_name in enumerate(table_columns):
                val = str(row_data[column_name])
                if column_name == 'ID':
                    tool_id = val
                    val = 'T' + str(val).strip().zfill(4)
                if column_name == 'Status':
                    status = val
                if column_name == 'Version':
                    version = val
                item = QtWidgets.QTableWidgetItem(val)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.search_scripts_table.setItem(i, j, item)
        self.ui.search_scripts_table.viewport().update()
        self.ui.search_scripts_table.resizeColumnsToContents()
        
        """If there is only 1 row, select it by default"""
        if self.ui.search_scripts_table.rowCount() == 1:
            self.ui.search_scripts_table.setCurrentCell(0, 0)
            self.ui.search_scripts_table.item(0, 0).setSelected(True)
            self.ui.search_scripts_table.cellClicked.emit(0, 0)
            self.ui.search_scripts_table.setFocus()
            self.ui.search_tool_id.setText(str(int(float(tool_id))))
            self.ui.search_tool_status.setText(status)
            self.ui.search_tool_version.setText(version)
            self.update_desc_path(single_row=True)


    def delete_undelete_record(self):
        """Give option to Delete and Undelete based on status = Active/Delete"""
        row_id = self.ui.search_tool_id.text()
        if row_id != '':
            row_id = int(row_id)
            row_status = self.ui.search_tool_status.text()
            if row_status == 'Active':
                SqlDb.delete_data(self.conn, row_id)
                msg = 'Deleted record successfully'
                self.ui.search_delete_undelete_record.setText('ACTIVATE RECORD')
                self.ui.search_tool_status.setText('Deleted')
            else:
                SqlDb.undelete_data(self.conn, row_id)
                msg = 'Activeted record successfully'
                self.ui.search_delete_undelete_record.setText('DELETE RECORD')
                self.ui.search_tool_status.setText('Active')
            self.ui.search_status.setText(msg)
            self.reset_app()
        
    def update_desc_path(self, item=None, single_row=False):
        """Based on user click on data grid, display description and paths below grid"""
        if single_row:
            row_id = int(self.ui.search_tool_id.text())
        else:
            row = item.row()
            row_id = int(self.ui.search_scripts_table.item(row, 0).text()[1:].lstrip('0'))
        selected_row = self.query_results_df[self.query_results_df['ID'].astype(str).str.upper() == str(row_id).upper()]
        description = selected_row['Description'].values[0]
        tool_path = selected_row['ToolPath'].values[0]
        doc_path = selected_row['DocumentPath'].values[0]
        version = selected_row['Version'].values[0]
        status = selected_row['Status'].values[0]
        if status == 'Active':
            self.ui.search_delete_undelete_record.setText('DELETE RECORD')
        else:
            self.ui.search_delete_undelete_record.setText('ACTIVATE RECORD')
        self.ui.search_tool_id.setText(str(row_id))
        self.ui.search_tool_status.setText(status)
        self.ui.search_tool_version.setText(str(int(float(version))))
        self.ui.search_description.setText(description)
        self.ui.search_script_tool_path.setText(tool_path)
        self.ui.search_script_help_path.setText(doc_path)
        
        
    def prefill_add_form(self):
        """Prefill the add/manage form with existing row values"""
        try:
            row_id = int(self.ui.search_tool_id.text())
            selected_row = self.query_results_df[self.query_results_df['ID'].astype(str).str.upper() == str(row_id).upper()]
            form_fields = ['Title', 'Team', 'Description', 'Software', 'Keyword', 'Function',
                        'Owner', 'ToolPath', 'DocumentPath', 'Version']
            for col in form_fields:
                widget = getattr(self.ui, 'add_'+col.lower())
                val = str(selected_row[col].values[0])
                if val not in ['', 'None'] and col != 'ToolPath' and col != 'DocumentPath':
                    widget.setText(val)
                else:
                    widget.setText('')
            self.ui.tabWidget.setCurrentIndex(1)
        except:
            pass
            
    def save_tool_info(self):
        """validate form fields and get data as dictionary"""
        data_dict = self.get_add_tool_data()
        if data_dict:
            """Insert the data into the database"""
            status = SqlDb.insert_data(self.conn, data_dict)
            self.ui.add_status.setText(status['message'])
            self.ui.search_status.setText(status['message'])
            print(status)
            if status['inserted']:
                self.reset_add_form(clear_status=False)
                self.reset_app()
                self.check_and_upload_files_to_repo_folder()
                self.update_result_table()
            
            
    def get_add_tool_data(self):
        """Create a dictionary with all form fields"""
        form_fields = ['Title', 'Team', 'Description', 'Software', 'Keyword', 'Function',
               'Owner', 'ToolPath', 'DocumentPath', 'Version']
        data_dict = {}
        for col in form_fields:
            widget = getattr(self.ui, 'add_'+col.lower())
            if widget is not None:
                if col == 'Description':
                    data_dict[col] = widget.toPlainText()
                else:
                    data_dict[col] = widget.text()
        data_dict['Status'] = 'Active'
        data_dict['Version'] = int(float(data_dict.get('Version', '0'))) + 1
        
        """validate mandatory field values"""
        blank_fields = ''
        for key, value in data_dict.items():
            if key != 'DocumentPath' and (not value or value == ''):
                blank_fields += key + ', '
        if len(blank_fields) == 0:
            """Data is complete - pass to insert into db"""
            self.ui.add_status.setText('')
            return data_dict
        else:
            """Notify user on blank fields"""
            err_message = 'Please fill : ' + blank_fields
            self.ui.add_status.setText(err_message)
            return {}
            

    def reset_add_form(self, clear_status=True):
        """Reset the add/manage form"""
        if clear_status:
            self.ui.add_status.setText('')
        form_fields = ['Title', 'Team', 'Description', 'Software', 'Keyword', 'Function',
                    'Owner', 'ToolPath', 'DocumentPath', 'Version']
        for col in form_fields:
            widget = getattr(self.ui, 'add_'+col.lower())
            
            if col == 'Version':
                widget.setText('0')
            else:
                widget.setText('')
                
                
    def download_script_path(self):
        '''download_script_path'''
        str_path = self.ui.search_script_tool_path.toPlainText()
        status = self.browse_and_save(str_path)
        self.ui.search_status.setText(status)
        
    def download_doc_path(self):
        '''download_doc_path'''
        str_path = self.ui.search_script_help_path.toPlainText()
        status = self.browse_and_save(str_path)
        self.ui.search_status.setText(status)
        
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
        return "Files saved successfully @ " + dest_path
    
    
    def check_and_upload_files_to_repo_folder(self):
        """Upload scripts to repor folder for new files uploaded by the user"""
        for i, row_data in self.query_results_df.iterrows():
            tool_id = 'T' + str(row_data['ID']).zfill(5)
            tool_path = str(row_data['ToolPath'])
            doc_path = str(row_data['DocumentPath'])
            created_by = str(row_data['Created_By'])
            created_on = pd.to_datetime(row_data['Created_On'])
            time_difference = pd.Timestamp.now() - created_on
            if created_by == self.username and time_difference < pd.Timedelta(hours=12):
                try:
                    save_in_path = self.save_files_in_repo(tool_path, tool_id, 'ToolPath')
                    if save_in_path and len(save_in_path) > 0:
                        self.query_results_df.at[i, 'ToolPath'] = save_in_path
                        
                    save_in_path = self.save_files_in_repo(doc_path, tool_id, 'DocumentPath')
                    if save_in_path and len(save_in_path) > 0:
                        self.query_results_df.at[i, 'DocumentPath'] = save_in_path
                        
                except Exception as e:
                    print('check_and_upload_files_to_repo_folder', str(e))
                    
    
    def save_files_in_repo(self, src_path, tool_id, field_name):
        """Create a folder by Tool ID and save files"""
        save_in_path = ''
        repo_path = os.getenv('Repo_Path')
        repo_path = repo_path.replace('/', '\\')
        src_path = src_path.replace('/', '\\')
        if (src_path and len(src_path) > 0 and not src_path.startswith(repo_path) 
            and not repo_path.startswith(src_path) and os.path.exists(src_path)
            and src_path not in repo_path):
            dest_path = os.path.join(os.path.join(repo_path, 'Scripts'), tool_id)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            if os.path.exists(dest_path):
                save_in_path = self._save_files_in_repo(src_path, dest_path, tool_id, field_name)

        return save_in_path
    
    def _save_files_in_repo(self, src_path, dest_path, tool_id, field_name):
        """_save_files_in_repo"""
        save_in_path = ''
        row_id = tool_id[1:].lstrip('0')
        if os.path.isfile(src_path):
            file_name = os.path.basename(src_path)
            file_dest_path = os.path.join(dest_path, f"{tool_id}_{file_name}")
            shutil.copy2(src_path, file_dest_path)
            save_in_path = file_dest_path
        elif os.path.isdir(src_path):
            folder_name = os.path.basename(src_path)
            zip_file_path = os.path.join(dest_path, f"{tool_id}_{folder_name}.zip")
            with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(src_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, src_path)
                        zf.write(file_path, arcname=os.path.join(folder_name, rel_path))
            save_in_path = zip_file_path
        data_dict = {field_name: save_in_path}

        SqlDb.update_data(self.conn, data_dict, row_id)
        return save_in_path
        
        
    def reset_app(self):
        """Clear all selections and get data from DB"""
        self.search_dict.update({'software': None, 'function': None, 'keyword': None, 'wildcard': None})
        self.query_results_df = get_data_df(self.conn, self.search_dict)
        self.update_result_table()
        
        self.ui.search_add_new_version.hide()
        self.ui.search_delete_undelete_record.hide()
        self.ui.search_script_tool_path_download.hide()
        self.ui.search_script_help_path_download.hide()
        self.ui.search_open_term.setText('')
        self.ui.UserName1.setText(self.username)
        self.ui.UserName2.setText(self.username)
        self.ui.UserName3.setText(self.username)
        self.ui.UserName4.setText(self.username)
        self.ui.search_open_term.setText('')
        self.sw_list = self.get_unique_list('Software')
        self.fn_list = self.get_unique_list('Function')
        self.kw_list = self.get_unique_list('Keyword')
        self.ui.search_software.clear()
        self.ui.search_software.addItems(self.sw_list)
        self.ui.search_function.clear()
        self.ui.search_function.addItems(self.fn_list)
        self.ui.search_keyword.clear()
        self.ui.search_keyword.addItems(self.kw_list)
        
        self.ui.tabWidget.setCurrentIndex(0)
        
        
    
    def browse_folder(self):
        """Browse for Folder """
        return QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', '')
    
    def browse_file(self):
        """Browse for File"""
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*);;Text Files (*.txt)')[0]

    def select_file_or_folder(self):
        """Browse for Folder or File"""
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        str_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File or Folder", "",
                                                             "All Files (*);;Directories", options=options)
        if not str_path:  # No file was selected
            str_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        return str_path


    def search_wild_card(self):
        """search_wild_card"""
        wild_card = self.ui.search_open_term.text()
        self.search_dict.update({'software': None, 'function': None, 'keyword': None, 'wildcard': wild_card})
        #self.update_result_table()
        
    def software_dropdown_updated(self):
        """software_dropdown_updated"""
        sw = self.ui.search_software.currentText()
        self.search_dict.update({'software': sw, 'function': None, 'keyword': None, 'wildcard': None})
        self.fn_list = self.get_unique_list('Function')
        self.ui.search_function.clear()
        self.ui.search_function.addItems(self.fn_list)
        #self.update_result_table()
        
    def function_dropdown_updated(self):
        """function_dropdown_updated"""
        sw = self.ui.search_software.currentText()
        fn = self.ui.search_function.currentText()
        self.search_dict.update({'software': sw, 'function': fn, 'keyword': None, 'wildcard': None})
        self.kw_list = self.get_unique_list('Keyword')
        self.ui.search_keyword.clear()
        self.ui.search_keyword.addItems(self.kw_list)
        #self.update_result_table()
        
    def keyword_dropdown_updated(self):
        """keyword_dropdown_updated"""
        sw = self.ui.search_software.currentText()
        fn = self.ui.search_function.currentText()
        kw = self.ui.search_keyword.currentText()
        self.search_dict.update({'software': sw, 'function': fn, 'keyword': kw, 'wildcard': None})
        #self.update_result_table()
    


    def get_filtered_data_df(self):
        """get_filtered_data_df"""
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
        return df_filtered
    
    def get_unique_list(self, field):
        """get_unique_list for dropdown lists"""
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
            
        """Get unique values for Software, Function and Keyword"""
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
    Repo_Path = os.getenv('Repo_Path')
    db_path = os.path.join(os.path.join(Repo_Path, 'Database'), 'SST.db')
    print('db_path', Repo_Path)
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

    
def create_app():
    """Initiate PyQT Application"""
    app = QtWidgets.QApplication(sys.argv)
    win = UiWindow()
    win.show()
    sys.exit(app.exec_())

def check_tool_setup():
    """Check if tool database exists else create the setup"""
    Repo_Path = os.getenv('Repo_Path')
    db_folder = os.path.join(Repo_Path, 'Database')
    repo_folder = os.path.join(Repo_Path, 'Scripts')
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
        """Connect to DB"""
        db_path = os.path.join(db_folder, 'SST.db')
        conn = SqlDb.get_db_connection(db_path)
        SqlDb.create_table(conn)
        SqlDb.create_db_auth_table(conn)
    if not os.path.exists(repo_folder):
        os.makedirs(repo_folder)
    
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
    #   Bulk Upload
    #   Admin/Passcode
    #   Integrate Backend - GUI
    

    # DONE GUI:
    #   Search View
    #   Add/Manage Entry
    #   Bulk Upload
    #   Admin
    
    # DONE GUI Intigration
    #   List Unique Values in Dropdowns
    #   Make Dropdowns dependent Software > Function > keyword
    #   Display all tools in grid by default
    #   Search & Filter grid based on dropdown selection
    #   Search & Filter grid based on search parameter
    #   Download Script / document to user slected folder
    #   Add New Tool
    #   Edit Existing Tool
    #   Edit and Save Existing tool as New Tool (Multiple Versions)
    #   Bulk uplad
    #   Passcode authenticate
    
    """Check if tool database exists else create the setup"""
    check_tool_setup()
    
    """Start the app"""
    create_app()
