# Portfolio
  # Panopto Data Merge.py
      Overview
        This Python script is designed to manage and process Panopto usage data in CSV format. 
        It reads new CSV files from a specified directory, merges them with existing data, and updates the existing CSV files. 
        This tool helps keep track of usage statistics and ensures that data files are organized and up to date.
        The script was created to simplify the management of Panopto usage data.
        
      Features
        Merges new CSV files with existing data.
        Handles different types of usage reports (Session Usage, Folder Usage, System Views).
        Keeps a record of processed files to avoid duplicates.
        Handles empty CSV files gracefully.
        Provides error handling and logging for troubleshooting.
        
      Prerequisites
        Before using this script, make sure you have the following:
        Python (version 3.6 or higher)
        Required Python libraries (Pandas)
        
      Usage
        Clone or download this repository to your local machine.
        Set the constants at the beginning of the script to specify the file paths and directories relevant to your environment.
      
      Configuration
        You can customize the behavior of the script by modifying the constants at the beginning of the script:
        
        EXISTING_DATA_FILE_FOLDER_USAGE: File path to the existing Folder Usage data.
        EXISTING_DATA_FILE_SESSION_USAGE: File path to the existing Session Usage data.
        EXISTING_DATA_FILE_USER_USAGE: File path to the existing System Views data.
        OUTPUT_DIRECTORY: Directory where new CSV files are generated.
        PROCESSED_FILES_FILE: File to keep track of processed files.
        ERROR_FOLDER: Directory where error logs are stored.
        Data Backup
        Before running the script on important data, it is recommended to create backups or archives of existing data files. 
        This ensures that you can revert to previous data in case of unexpected issues.
      
      Error Handling
        In case of errors during script execution, error details are logged in the ERROR_FOLDER directory. Review these logs to diagnose and resolve any issues.
  # SCORM Data processing
      Overview
        This Python script connects to a MySQL database, executes SQL queries to extract data, performs data transformation tasks, and saves the results to a CSV file. 
        It is designed to automate the process of gathering and processing data from a Moodle database hosted on a MySQL server.
        The data is then put into Power BI to track the usage of these SCORM and quizzes
        
      Features
        Connects to a MySQL database.
        Executes SQL queries to extract specific data.
        Merges data from different queries based on a common column.
        Performs data transformations and handling of missing values.
        Saves the final dataset to a CSV file.
        
      Prerequisites
        Before using this script, ensure you have the following - 
        Python (version 3.6 or higher)
        Required Python libraries (mysql.connector, pandas)
        
      Usage
        Clone or download this repository to your local machine.
        Modify the script to set your MySQL database credentials and query files

      Configuration
        You can customize the script by modifying the following sections:
        MySQL database connection details.
        File paths for SQL query files.
        Data transformations based on your specific requirements.
        The path to save the final CSV file.

      SQL queries
        Query 1: Activity query:
            The main objectives of this script are as follows:
              Identify whether a user has "Completed" or "Attempted" specific course components, such as 'Bystander Intervention' and 'Student Induction.'
              Categorize quiz grades for different sections of the course as "Pass," "Fail," or "Not attempted."
              Group users by their email addresses to consolidate data for analysis.
        Query 2: User query
            The main objectives of this script are as follows:
              Gather the name, email and group names of all students on a course on Moodle that holds all of the SCORM and quiz files that are required, thg

      Data Format
        Ensure that your SQL query files and the resulting data match the expected format. 
        The script assumes specific column names and data types. Adjust the script and queries accordingly to match your data.
        
      CSV Output
        The final dataset is saved to a CSV file in the specified directory. You can customize the file path and format according to your preferences.
      
  # Design score and Engagement.py:
    Overview
      The "Design Score Calculation" script is a Python program designed to calculate a design score based on various factors related to user interactions and engagement with a 
      Moodle-based learning management system. This score can be used to assess the design quality of a module. 
    
    Features
      Calculates a design score based on a combination of user engagement factors.
      Normalizes input data to ensure consistent scoring.
      Provides insights into the design quality of Moodle courses and modules.
      Supports data input from CSV files.
      
    Prerequisites
      Before using this script, ensure you have the following:
    
      Python (version 3.6 or higher)
      Required Python libraries (Pandas, NumPy, Statsmodels, Matplotlib)
      
     Usage
      Clone or download this repository to your local machine.
      
      Place your data files (CSV format) in the same directory as the script or specify the file paths in the script.
      The script will process the data, calculate design scores, and generate visualisation plots.
      
      Configuration
        You can customize the script by modifying certain parameters in the code:
      
        Data file paths: Update the paths to your data files.
        Scoring formula: Adjust the formula or weights used for design score calculation.
        Plot settings: Modify plot titles, axis labels, and save formats.
        Data Format
        Ensure that your data files follow the expected format. The script assumes specific column names and data types. 
        Refer to the provided sample data or adjust the script to match your data format.
      
      Visualisation
      The script generates visualisation plots to help you understand the relationships between design scores and user engagement factors. 
      You can save these plots in various formats for further analysis or presentation.

  
