import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QHBoxLayout, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle('Data Analysis Projects')
        self.setGeometry(100, 100, 800, 600)

        self.data = data

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(len(self.data[0]))

        self.load_table_data()

        self.softwareCombo = QComboBox()
        self.softwareCombo.addItems(self.get_unique_values('Software'))

        self.functionCombo = QComboBox()
        self.functionCombo.addItems(self.get_unique_values('Function'))

        self.keywordCombo = QComboBox()
        self.keywordCombo.addItems(self.get_unique_values('Keyword'))

        self.softwareCombo.currentIndexChanged.connect(self.filter_data)
        self.functionCombo.currentIndexChanged.connect(self.filter_data)
        self.keywordCombo.currentIndexChanged.connect(self.filter_data)

        filterLayout = QHBoxLayout()
        filterLayout.addWidget(QLabel('Filter by Software:'))
        filterLayout.addWidget(self.softwareCombo)
        filterLayout.addWidget(QLabel('Filter by Function:'))
        filterLayout.addWidget(self.functionCombo)
        filterLayout.addWidget(QLabel('Filter by Keyword:'))
        filterLayout.addWidget(self.keywordCombo)

        filterWidget = QWidget()
        filterWidget.setLayout(filterLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tableWidget)
        mainLayout.addWidget(filterWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)

    def load_table_data(self):
        headers = ['ID', 'Team', 'Title', 'Description', 'Software', 'Keyword', 'Function', 'Owner', 'ToolPath', 'Status', 'DocumentPath', 'Created_On', 'Edited_On', 'Deleted_On']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for i, row in enumerate(self.data):
            for j, val in enumerate(row.values()):
                item = QTableWidgetItem(str(val))
                self.tableWidget.setItem(i, j, item)

    def get_unique_values(self, field):
        values = []
        for row in self.data:
            value = row[field]
            if value not in values:
                values.append(value)
        return values

    def filter_data(self):
        software = self.softwareCombo.currentText()
        function = self.functionCombo.currentText()
        keyword = self.keywordCombo.currentText()

        for i, row in enumerate(self.data):
            if (software == '' or row['Software'] == software) and (function == '' or row['Function'] == function) and (keyword == '' or row['Keyword'] == keyword):
                self.tableWidget.setRowHidden(i, False)
            else:
                self.tableWidget.setRowHidden(i, True)


if __name__ == '__main__':
    data = [
  {
    "ID": 14,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights and find trends",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Deleted",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:13:40",
    "Edited_On": "2023-03-08 22:40:41",
    "Deleted_On": "2023-03-08 22:54:35"
  },
  {
    "ID": 15,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Active",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:14:32",
    "Edited_On": 'null',
    "Deleted_On": 'null'
  },
  {
    "ID": 16,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Active",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:14:43",
    "Edited_On": 'null',
    "Deleted_On": 'null'
  },
  {
    "ID": 17,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Active",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:15:10",
    "Edited_On": 'null',
    "Deleted_On": 'null'
  },
  {
    "ID": 18,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Active",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:15:55",
    "Edited_On": 'null',
    "Deleted_On": 'null'
  },
  {
    "ID": 19,
    "Team": "Data Science",
    "Title": "Exploratory Data Analysis",
    "Description": "Analyzing data to gain insights",
    "Software": "Python",
    "Keyword": "EDA, Python, Analysis, Data",
    "Function": "data analysis",
    "Owner": "Sai",
    "ToolPath": "C:/data_analysis.py",
    "Status": "Active",
    "DocumentPath": "C:/eda_report.pdf",
    "Created_On": "2023-03-08 22:16:19",
    "Edited_On": 'null',
    "Deleted_On": 'null'
  }
]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Connect the filter button to the filter function
    ui.filter_button.clicked.connect(ui.filter_data)

    MainWindow.show()
    sys.exit(app.exec_())

