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
        
  # Design score.py:
    # This is a script to take Moodle data and Panopto data, and based on certain metrics, give them a score from 0-1
    # based on how well designed a module is. Essentially, if they are using Moodle and Panopto to it's fullest, they will score
    # higher.
    # It also scores each module on their engagement, 'Quality' and 'Level'. Quality is measuring when a student has actually
    # engaged with an activity (like posting on a forum). Level is just clicks on a module page, and views on a Panopto video.
    # It will then visualise design vs these engagement metrics to see their relationships.

  
