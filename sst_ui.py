<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>987</width>
    <height>638</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>ScriptSearchTool</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>981</width>
      <height>591</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="tab">
     <attribute name="title">
      <string>SEARCH</string>
     </attribute>
     <widget class="QLabel" name="label_51">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>15</y>
        <width>331</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>12</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>SEARCH / FILTER CRITERIA</string>
      </property>
     </widget>
     <widget class="Line" name="line">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>130</y>
        <width>941</width>
        <height>21</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="label_48">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>99</y>
        <width>90</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;SOFTWARE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QComboBox" name="search_software">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>94</y>
        <width>170</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
     </widget>
     <widget class="QComboBox" name="search_function">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>94</y>
        <width>170</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_49">
      <property name="geometry">
       <rect>
        <x>310</x>
        <y>99</y>
        <width>90</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;FUNCTION&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QComboBox" name="search_keyword">
      <property name="geometry">
       <rect>
        <x>670</x>
        <y>94</y>
        <width>170</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_50">
      <property name="geometry">
       <rect>
        <x>580</x>
        <y>99</y>
        <width>90</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;KEYWORD&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QTableWidget" name="search_scripts_table">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>200</y>
        <width>951</width>
        <height>181</height>
       </rect>
      </property>
      <property name="mouseTracking">
       <bool>true</bool>
      </property>
      <property name="autoFillBackground">
       <bool>false</bool>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Sunken</enum>
      </property>
      <property name="lineWidth">
       <number>1</number>
      </property>
      <property name="midLineWidth">
       <number>0</number>
      </property>
      <property name="autoScrollMargin">
       <number>16</number>
      </property>
      <property name="editTriggers">
       <set>QAbstractItemView::DoubleClicked</set>
      </property>
      <property name="dragDropOverwriteMode">
       <bool>false</bool>
      </property>
      <property name="alternatingRowColors">
       <bool>true</bool>
      </property>
      <property name="selectionMode">
       <enum>QAbstractItemView::SingleSelection</enum>
      </property>
      <property name="selectionBehavior">
       <enum>QAbstractItemView::SelectRows</enum>
      </property>
      <property name="gridStyle">
       <enum>Qt::SolidLine</enum>
      </property>
      <property name="sortingEnabled">
       <bool>true</bool>
      </property>
      <property name="rowCount">
       <number>14</number>
      </property>
      <attribute name="horizontalHeaderCascadingSectionResizes">
       <bool>true</bool>
      </attribute>
      <attribute name="horizontalHeaderDefaultSectionSize">
       <number>101</number>
      </attribute>
      <attribute name="verticalHeaderCascadingSectionResizes">
       <bool>false</bool>
      </attribute>
      <attribute name="verticalHeaderShowSortIndicator" stdset="0">
       <bool>false</bool>
      </attribute>
      <attribute name="verticalHeaderStretchLastSection">
       <bool>false</bool>
      </attribute>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <row/>
      <column>
       <property name="text">
        <string>ID</string>
       </property>
       <property name="font">
        <font>
         <pointsize>9</pointsize>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>TEAM</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>TITLE</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>OWNER</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>SOFTWARE</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>FUNCTION</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>KEYWORD</string>
       </property>
       <property name="font">
        <font>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>STATUS</string>
       </property>
       <property name="font">
        <font>
         <family>MS Shell Dlg 2</family>
         <pointsize>8</pointsize>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
      <column>
       <property name="text">
        <string>VERSION</string>
       </property>
       <property name="font">
        <font>
         <family>MS Shell Dlg 2</family>
         <pointsize>8</pointsize>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
      </column>
     </widget>
     <widget class="QTextBrowser" name="search_description">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>430</y>
        <width>451</width>
        <height>101</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="mouseTracking">
       <bool>false</bool>
      </property>
      <property name="documentTitle">
       <string/>
      </property>
     </widget>
     <widget class="QLabel" name="label_52">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>395</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:9pt; font-weight:600;&quot;&gt;DESCRIPTION&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QTextBrowser" name="search_script_tool_path">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>480</x>
        <y>440</y>
        <width>370</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="mouseTracking">
       <bool>false</bool>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="documentTitle">
       <string/>
      </property>
      <property name="lineWrapMode">
       <enum>QTextEdit::NoWrap</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="search_script_tool_path_download">
      <property name="geometry">
       <rect>
        <x>857</x>
        <y>440</y>
        <width>103</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>DOWNLOAD</string>
      </property>
     </widget>
     <widget class="QTextBrowser" name="search_script_help_path">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>480</x>
        <y>500</y>
        <width>370</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
       </font>
      </property>
      <property name="mouseTracking">
       <bool>false</bool>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="documentTitle">
       <string/>
      </property>
      <property name="lineWrapMode">
       <enum>QTextEdit::NoWrap</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="search_script_help_path_download">
      <property name="geometry">
       <rect>
        <x>857</x>
        <y>500</y>
        <width>103</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>DOWNLOAD</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_53">
      <property name="geometry">
       <rect>
        <x>480</x>
        <y>416</y>
        <width>161</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:9pt; font-weight:600;&quot;&gt;SCRIPT/TOOL FILE&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_54">
      <property name="geometry">
       <rect>
        <x>480</x>
        <y>476</y>
        <width>131</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:9pt; font-weight:600;&quot;&gt;HELP/DOCUMENT&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_102">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>160</y>
        <width>381</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>12</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>LIST OF SCRIPTS / TOOLS</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label2_4">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>0</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Welcome&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="UserName1">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>20</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;username&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="Line" name="line_2">
      <property name="geometry">
       <rect>
        <x>840</x>
        <y>10</y>
        <width>20</width>
        <height>51</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="search_add_new_version">
      <property name="geometry">
       <rect>
        <x>809</x>
        <y>390</y>
        <width>151</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>ADD NEW VERSION</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_80">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>55</y>
        <width>101</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;SEARCH TERM&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="Line" name="line_35">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>50</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLineEdit" name="search_open_term">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>50</y>
        <width>251</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QCheckBox" name="search_include_deleted_items">
      <property name="geometry">
       <rect>
        <x>760</x>
        <y>160</y>
        <width>201</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <pointsize>10</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>INCLUDE DELETED RECORDS</string>
      </property>
     </widget>
     <widget class="QPushButton" name="search_delete_undelete_record">
      <property name="geometry">
       <rect>
        <x>630</x>
        <y>390</y>
        <width>151</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>DELETE RECORD</string>
      </property>
     </widget>
     <widget class="QLabel" name="search_tool_id">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>380</y>
        <width>101</width>
        <height>16</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>1</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="search_tool_version">
      <property name="geometry">
       <rect>
        <x>110</x>
        <y>380</y>
        <width>101</width>
        <height>16</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>1</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="search_tool_status">
      <property name="geometry">
       <rect>
        <x>210</x>
        <y>380</y>
        <width>101</width>
        <height>16</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>1</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="search_status">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>540</y>
        <width>951</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QPushButton" name="search_by_wildcard">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>50</y>
        <width>171</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>SEARCH</string>
      </property>
     </widget>
     <widget class="QPushButton" name="search_by_filter">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>94</y>
        <width>111</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>SEARCH</string>
      </property>
     </widget>
     <widget class="QPushButton" name="search_by_reset">
      <property name="geometry">
       <rect>
        <x>670</x>
        <y>50</y>
        <width>171</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>RESET</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_2">
     <attribute name="title">
      <string>ADD/MANAGE</string>
     </attribute>
     <widget class="QLabel" name="add_header_lable">
      <property name="geometry">
       <rect>
        <x>12</x>
        <y>20</y>
        <width>381</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>ADD SCRIPT / TOOL INFO</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_56">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>115</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;TEAM&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_team">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>110</y>
        <width>280</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_57">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>164</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;SOFTWARE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_software">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>160</y>
        <width>280</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_function">
      <property name="geometry">
       <rect>
        <x>550</x>
        <y>160</y>
        <width>280</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_58">
      <property name="geometry">
       <rect>
        <x>440</x>
        <y>164</y>
        <width>81</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;FUNCTION&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_keyword">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>210</y>
        <width>691</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_59">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>213</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;KEYWORD&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_owner">
      <property name="geometry">
       <rect>
        <x>550</x>
        <y>110</y>
        <width>280</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_60">
      <property name="geometry">
       <rect>
        <x>440</x>
        <y>115</y>
        <width>81</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;OWNER&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_title">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>60</y>
        <width>691</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_61">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>64</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;TITLE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_62">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>263</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;DESCRIPTION&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_toolpath">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>410</y>
        <width>511</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_63">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>413</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;SCRIPT FILE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="add_script_path_browse">
      <property name="geometry">
       <rect>
        <x>660</x>
        <y>410</y>
        <width>171</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>BROWSE FILE / FOLDER</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_64">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>463</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;HELP FILE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="add_help_path_browse">
      <property name="geometry">
       <rect>
        <x>660</x>
        <y>460</y>
        <width>171</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>BROWSE FILE / FOLDER</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="add_documentpath">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>460</y>
        <width>511</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="QPushButton" name="add_reset">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>510</y>
        <width>151</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>RESET</string>
      </property>
     </widget>
     <widget class="QPushButton" name="save_info">
      <property name="geometry">
       <rect>
        <x>320</x>
        <y>510</y>
        <width>221</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>ADD TOOL TO DB</string>
      </property>
     </widget>
     <widget class="QPushButton" name="add_exit">
      <property name="geometry">
       <rect>
        <x>570</x>
        <y>510</y>
        <width>151</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>EXIT</string>
      </property>
     </widget>
     <widget class="Line" name="line_4">
      <property name="geometry">
       <rect>
        <x>840</x>
        <y>10</y>
        <width>20</width>
        <height>531</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_5">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>180</y>
        <width>101</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="Line" name="line_6">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>380</y>
        <width>101</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="add_status">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>410</y>
        <width>112</width>
        <height>121</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#5b5b5b;&quot;&gt;.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="UserName2">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>20</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;username&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label2_3">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>0</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Welcome&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="Line" name="line_36">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>50</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="edit_tool_id">
      <property name="geometry">
       <rect>
        <x>740</x>
        <y>10</y>
        <width>101</width>
        <height>16</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>1</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_version">
      <property name="geometry">
       <rect>
        <x>740</x>
        <y>30</y>
        <width>101</width>
        <height>16</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>1</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>0</string>
      </property>
     </widget>
     <widget class="QTextEdit" name="add_description">
      <property name="geometry">
       <rect>
        <x>140</x>
        <y>260</y>
        <width>691</width>
        <height>131</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
       </font>
      </property>
     </widget>
     <widget class="QLabel" name="label_65">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>60</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_66">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>110</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_67">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>160</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_68">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>210</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_69">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>260</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_70">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>410</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_72">
      <property name="geometry">
       <rect>
        <x>530</x>
        <y>110</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_73">
      <property name="geometry">
       <rect>
        <x>530</x>
        <y>160</y>
        <width>21</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_71">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>510</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:8pt; font-weight:400; color:#ff0000;&quot;&gt;*&lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:400;&quot;&gt; Mandatory fields&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_3">
     <attribute name="title">
      <string>BULK ADD</string>
     </attribute>
     <widget class="QPushButton" name="bulk_template_download">
      <property name="geometry">
       <rect>
        <x>210</x>
        <y>70</y>
        <width>160</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>DOWNLOAD</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label_2">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>230</y>
        <width>112</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;UPLOAD FILE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label_3">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>70</y>
        <width>181</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;DOWNLOAD TEMPLATE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_101">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>150</y>
        <width>381</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>BULK ADD</string>
      </property>
     </widget>
     <widget class="QPushButton" name="bulk_upload_file">
      <property name="geometry">
       <rect>
        <x>210</x>
        <y>230</y>
        <width>160</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>UPLOAD DATA</string>
      </property>
     </widget>
     <widget class="QPushButton" name="bulk_exit">
      <property name="geometry">
       <rect>
        <x>690</x>
        <y>230</y>
        <width>160</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>EXIT</string>
      </property>
     </widget>
     <widget class="Line" name="line_7">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>120</y>
        <width>931</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="label_103">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>20</y>
        <width>381</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>UPLOAD FORMAT</string>
      </property>
     </widget>
     <widget class="Line" name="line_8">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>350</y>
        <width>931</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label2_6">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>0</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Welcome&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="UserName3">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>20</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;username&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="Line" name="line_3">
      <property name="geometry">
       <rect>
        <x>840</x>
        <y>10</y>
        <width>20</width>
        <height>51</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_37">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>50</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="bulk_status">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>370</y>
        <width>691</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#5b5b5b;&quot;&gt;.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_10">
     <attribute name="title">
      <string>ADMIN</string>
     </attribute>
     <widget class="QLabel" name="add_enable_edit_label2">
      <property name="geometry">
       <rect>
        <x>139</x>
        <y>320</y>
        <width>151</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;UPDATE PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="admin_update_passcode_retype">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>380</y>
        <width>200</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData</set>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Password</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="admin_enable_edit_authenticate">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>160</y>
        <width>118</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>AUTHENTICATE</string>
      </property>
     </widget>
     <widget class="QLabel" name="admin_update_passcode_label3">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>360</y>
        <width>118</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>8</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;RETYPE PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="admin_enable_edit_passcode">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>120</y>
        <width>201</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData</set>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Password</enum>
      </property>
     </widget>
     <widget class="QLabel" name="admin_enable_edit_label">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>100</y>
        <width>71</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>8</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="admin_update_passcode">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>420</y>
        <width>118</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>UPDATE</string>
      </property>
     </widget>
     <widget class="QLabel" name="admin_update_passcode_label2">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>300</y>
        <width>118</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>8</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;NEW PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="admin_update_passcode_new">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>320</y>
        <width>200</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Normal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="label_104">
      <property name="geometry">
       <rect>
        <x>290</x>
        <y>30</y>
        <width>211</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>ADMIN OPTIONS</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label_4">
      <property name="geometry">
       <rect>
        <x>139</x>
        <y>130</y>
        <width>231</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;ENABLE EDIT EXISTING TOOLS&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="Line" name="line_9">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>210</y>
        <width>531</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLineEdit" name="admin_update_passcode_current">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>260</y>
        <width>200</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData</set>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Password</enum>
      </property>
     </widget>
     <widget class="QLabel" name="admin_update_passcode_label1">
      <property name="geometry">
       <rect>
        <x>410</x>
        <y>240</y>
        <width>131</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>8</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;CURRENT PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="Line" name="line_10">
      <property name="geometry">
       <rect>
        <x>370</x>
        <y>100</y>
        <width>20</width>
        <height>91</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_11">
      <property name="geometry">
       <rect>
        <x>370</x>
        <y>240</y>
        <width>20</width>
        <height>211</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_12">
      <property name="geometry">
       <rect>
        <x>680</x>
        <y>80</y>
        <width>20</width>
        <height>441</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_13">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>80</y>
        <width>20</width>
        <height>441</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_14">
      <property name="geometry">
       <rect>
        <x>109</x>
        <y>470</y>
        <width>581</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="Line" name="line_15">
      <property name="geometry">
       <rect>
        <x>109</x>
        <y>70</y>
        <width>581</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="Line" name="line_16">
      <property name="geometry">
       <rect>
        <x>110</x>
        <y>510</y>
        <width>581</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="admin_status">
      <property name="geometry">
       <rect>
        <x>120</x>
        <y>490</y>
        <width>551</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>8</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;status...&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label2_8">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>0</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Welcome&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="UserName4">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>20</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;username&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="Line" name="line_17">
      <property name="geometry">
       <rect>
        <x>840</x>
        <y>10</y>
        <width>20</width>
        <height>51</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_38">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>50</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="admin_exit">
      <property name="geometry">
       <rect>
        <x>760</x>
        <y>480</y>
        <width>160</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>EXIT</string>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab_8">
     <attribute name="title">
      <string>DB LOCATION</string>
     </attribute>
     <widget class="QPushButton" name="admin_setup_create_repo">
      <property name="geometry">
       <rect>
        <x>180</x>
        <y>220</y>
        <width>151</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>CREATE DB SETUP</string>
      </property>
     </widget>
     <widget class="Line" name="line_46">
      <property name="geometry">
       <rect>
        <x>850</x>
        <y>50</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLabel" name="admin_setup_passcode_label2">
      <property name="geometry">
       <rect>
        <x>780</x>
        <y>140</y>
        <width>141</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;PASSCODE&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="connect_to_db">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>360</x>
        <y>220</y>
        <width>111</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="layoutDirection">
       <enum>Qt::LeftToRight</enum>
      </property>
      <property name="text">
       <string>CONNECT</string>
      </property>
     </widget>
     <widget class="QLabel" name="add_header_lable_4">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>30</y>
        <width>551</width>
        <height>21</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>15</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>SELECT DB LOCATION TO START APPLICATION</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="admin_setup_passcode">
      <property name="geometry">
       <rect>
        <x>780</x>
        <y>170</y>
        <width>161</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData</set>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Password</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="db_exit">
      <property name="geometry">
       <rect>
        <x>490</x>
        <y>220</y>
        <width>101</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>EXIT</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_109">
      <property name="geometry">
       <rect>
        <x>30</x>
        <y>143</y>
        <width>121</width>
        <height>20</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;DB LOCATION&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="db_location_path_browse">
      <property name="geometry">
       <rect>
        <x>610</x>
        <y>140</y>
        <width>111</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>BROWSE</string>
      </property>
     </widget>
     <widget class="QLabel" name="admin_setup_passcode_label1">
      <property name="geometry">
       <rect>
        <x>780</x>
        <y>90</y>
        <width>191</width>
        <height>41</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>12</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>AUTHENTICATE TO CREATE NEW REPO</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="UserName5">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>20</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:400;&quot;&gt;username&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="add_enable_edit_label2_12">
      <property name="geometry">
       <rect>
        <x>860</x>
        <y>0</y>
        <width>101</width>
        <height>31</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="inputMethodHints">
       <set>Qt::ImhNone</set>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;Welcome&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="Line" name="line_47">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>310</y>
        <width>961</width>
        <height>21</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
     <widget class="QLineEdit" name="db_location_path">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>180</x>
        <y>140</y>
        <width>411</width>
        <height>30</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>10</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
     </widget>
     <widget class="Line" name="line_48">
      <property name="geometry">
       <rect>
        <x>840</x>
        <y>10</y>
        <width>20</width>
        <height>51</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="Line" name="line_18">
      <property name="geometry">
       <rect>
        <x>740</x>
        <y>100</y>
        <width>20</width>
        <height>201</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="admin_setup_passcode_authenticate">
      <property name="geometry">
       <rect>
        <x>780</x>
        <y>220</y>
        <width>161</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>AUTHENTICATE</string>
      </property>
     </widget>
     <widget class="QLabel" name="db_status">
      <property name="geometry">
       <rect>
        <x>60</x>
        <y>330</y>
        <width>841</width>
        <height>61</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Verdana</family>
        <pointsize>9</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#5b5b5b;&quot;&gt;.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QPushButton" name="show_db_auth_fields">
      <property name="geometry">
       <rect>
        <x>940</x>
        <y>60</y>
        <width>31</width>
        <height>30</height>
       </rect>
      </property>
      <property name="palette">
       <palette>
        <active>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </active>
        <inactive>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>127</red>
            <green>212</green>
            <blue>127</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </inactive>
        <disabled>
         <colorrole role="WindowText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Button">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Light">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>255</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Midlight">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>212</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Dark">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Mid">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>113</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Text">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="BrightText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>255</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ButtonText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>85</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Base">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Window">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="Shadow">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="AlternateBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>170</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipBase">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>255</red>
            <green>255</green>
            <blue>220</blue>
           </color>
          </brush>
         </colorrole>
         <colorrole role="ToolTipText">
          <brush brushstyle="SolidPattern">
           <color alpha="255">
            <red>0</red>
            <green>0</green>
            <blue>0</blue>
           </color>
          </brush>
         </colorrole>
        </disabled>
       </palette>
      </property>
      <property name="font">
       <font>
        <family>MS Outlook</family>
        <pointsize>12</pointsize>
        <weight>50</weight>
        <bold>false</bold>
       </font>
      </property>
      <property name="text">
       <string>B</string>
      </property>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>987</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
