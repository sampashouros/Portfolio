import mysql.connector
import pandas as pd

# Create connection to MySQL server
auth = mysql.connector.connect(user='sam.pashouros',
                               password='aQuie8tai6ep3cui$&',
                               host='smuc-reporting.bloom.ulcc.ac.uk',
                               database='moodle')

# Function to execute the query and return the DF
def execute_query_and_get_dataframe(query):
    cursor = auth.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    cursor.close()
    return pd.DataFrame(rows, columns=column_names)

# Execute the first query
# This query gets all the students from the Student Training Module
file = open("user query.txt")
query=file.read()
df1=execute_query_and_get_dataframe(query)
file.close()

# Execute the second query
# This query gets all of the student results for each SCORM/quiz
file = open("\\\\DOTNET2019\\MoodleExports\\Scripts\\Queries\\activitiy query.txt")
query=file.read()
df2=execute_query_and_get_dataframe(query)
file.close()
auth.close()

# Merge data from queries
df3 = pd.merge(df1, df2, on="email", how="left")
 
# Transformations - fill any missing data (missing data means student hasn't attempted)
df3.fillna("Not attempted", inplace=True)
df3['group_name'] = df3['group_name'].replace('Not attempted', 'No group')

# Adds data to file
file_path = 'User Scorm Data.csv'
df3.to_csv(file_path, index=False)
