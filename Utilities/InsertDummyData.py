import sqlite3

# connect to database
conn = sqlite3.connect('../Database/example.db')

# create a cursor to execute SQL commands
c = conn.cursor()

# insert first record
c.execute("INSERT INTO ScriptInfo (Department, Software, ScriptName, ShortDescription, Functionalities, Features, KeyWords, Owner, Created_On, Edited_On, Deleted_On, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
          ('Sales', 'CRM', 'Update Leads', 'Updates the leads table with new information', 'Update lead details', 'Add/Update/Delete leads', 'Leads, Update, Information', 'John Doe', '2022-01-01 12:00:00', '2022-01-02 10:00:00', None, 'Active'))

# insert second record
c.execute("INSERT INTO ScriptInfo (Department, Software, ScriptName, ShortDescription, Functionalities, Features, KeyWords, Owner, Created_On, Edited_On, Deleted_On, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
          ('Marketing', 'Email Campaigns', 'Send Newsletter', 'Sends a monthly newsletter to subscribers', 'Create and send newsletters', 'Manage subscribers, templates, campaigns', 'Email, Newsletter, Subscribers', 'Jane Smith', '2022-02-01 10:00:00', '2022-02-05 14:00:00', None, 'Active'))

# commit changes and close connection
conn.commit()
conn.close()
