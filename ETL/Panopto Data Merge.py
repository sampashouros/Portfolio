import os
import pandas as pd

def main():
    existing_data_file_folder_usage = "\\\\DOTNET2019\\MoodleExports\\Master Files\\Panopto Master - Folder.csv"
    existing_data_file_session_usage = "\\\\DOTNET2019\\MoodleExports\\Master Files\\Panopto Master - Session.csv"
    existing_data_file_user_usage = "\\\\DOTNET2019\\MoodleExports\\Master Files\\Panopto Master - User.csv"
    output_directory = "\\\\DOTNET2019\\MoodleExports\Panopto Report Downloads"
    processed_files_file = "\\\\DOTNET2019\\MoodleExports\\Master Files\\processed_files.txt"
    error_folder = "\\\\DOTNET2019\\MoodleExports\\Errors"

    try:
        # Read the existing data set CSV files into DataFrames
        existing_data_session = pd.read_csv(existing_data_file_session_usage) if os.path.exists(existing_data_file_session_usage) else pd.DataFrame()
        existing_data_folder = pd.read_csv(existing_data_file_folder_usage) if os.path.exists(existing_data_file_folder_usage) else pd.DataFrame()
        existing_data_user = pd.read_csv(existing_data_file_user_usage) if os.path.exists(existing_data_file_user_usage) else pd.DataFrame()

        # Load the list of already processed files
        processed_files = []
        if os.path.exists(processed_files_file):
            with open(processed_files_file, "r") as file:
                processed_files = [line.strip() for line in file]

        # Iterate over the new CSV files
        for filename in os.listdir(output_directory):
            if filename.endswith(".csv") and filename not in processed_files:
                file_path = os.path.join(output_directory, filename)
                if os.path.getsize(file_path) == 0:
                    continue  # Skip empty files

                if filename.startswith("SessionUsage"):
                    try:
                        new_data = pd.read_csv(file_path)
                        if not new_data.empty:
                            existing_data_session = pd.concat([existing_data_session, new_data], ignore_index=True)
                        # Process sessions usage report
                    except pd.errors.EmptyDataError:
                        print(f"Empty file: {file_path}")

                elif filename.startswith("FolderUsage"):
                    try:
                        new_data = pd.read_csv(file_path)
                        if not new_data.empty:
                            existing_data_folder = pd.concat([existing_data_folder, new_data], ignore_index=True)
                        # Process folder usage report
                    except pd.errors.EmptyDataError:
                        print(f"Empty file: {file_path}")
                elif filename.startswith("SystemViews"):
                    try:
                        new_data = pd.read_csv(file_path)
                        if not new_data.empty:
                            existing_data_user = pd.concat([existing_data_user, new_data], ignore_index=True)
                        # Process user usage report
                    except pd.errors.EmptyDataError:
                        print(f"Empty file: {file_path}")

                processed_files.append(filename)

        # Save the merged data set to the CSV files if non-empty data is available
        if not existing_data_session.empty:
            existing_data_session.to_csv(existing_data_file_session_usage, index=False)

        if not existing_data_folder.empty:
            existing_data_folder.to_csv(existing_data_file_folder_usage, index=False)

        if not existing_data_user.empty:
            existing_data_user.to_csv(existing_data_file_user_usage, index=False)

        # Write the updated list of processed files to a file
        with open(processed_files_file, "w") as file:
            for filename in processed_files:
                file.write(filename + "\n")

        # Delete the used files
        for filename in os.listdir(output_directory):
            file_path = os.path.join(output_directory, filename)
            if os.path.getsize(file_path) == 0 or filename in processed_files:
                try:
                    os.remove(file_path)
                    print(f"Successfully removed {file_path}")
                except FileNotFoundError:
                    print(f"File {file_path} not found")

    except Exception as ex:
        error_file = os.path.join(error_folder, f"Error_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(error_file, "w") as file:
            file.write(f"Error occurred at {pd.Timestamp.now()}:\n{str(ex)}\n")
        print(f"An error occurred. Error details have been saved to {error_file}")


if __name__ == '__main__':
    main()
