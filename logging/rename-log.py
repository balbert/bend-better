import logging
import os
import shutil

# Create a logger and an initial FileHandler
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

initial_filename = 'app.log'
handler = logging.FileHandler(initial_filename)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("This is the first log message in the initial file.")

# Change the filename
new_filename = 'app_new.log'

# 1. Close the existing handler
handler.close()

# 1.5a Rename old file to new name
# try:
#     os.rename(initial_filename, new_filename)
# except FileNotFoundError:
#     print(f"Error: The file '{initial_filename}' was not found.")
# except PermissionError:
#     print(f"Error: Permission denied to rename '{initial_filename}'.")
# except OSError as e:
#     print(f"An unexpected error occurred: {e}")

# 1.5b Copy old file to new name
try:
    shutil.copy(initial_filename, new_filename)
except FileNotFoundError:
    print(f"Error: Source file '{initial_filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 2. Update the baseFilename attribute
# It's good practice to get the absolute path for consistency
handler.baseFilename = os.path.abspath(new_filename)

# 3. Re-open the handler (this implicitly happens when it's used again)
# Or, if you need to force it open immediately, you could re-add it to the logger
# (though updating baseFilename is usually sufficient for subsequent logging)
# For a clean re-initialization, you might remove and re-add:
logger.removeHandler(handler)
logger.addHandler(handler)

logger.info("This is a log message in the new file.")

# Verify the files
if os.path.exists(initial_filename):
    print(f"Content of {initial_filename}:")
    with open(initial_filename, 'r') as f:
        print(f.read())

if os.path.exists(new_filename):
    print(f"\nContent of {new_filename}:")
    with open(new_filename, 'r') as f:
        print(f.read())

# Clean up created log files
os.remove(initial_filename) if os.path.exists(initial_filename) else None
os.remove(new_filename) if os.path.exists(new_filename) else None


# import os

# # Define the old and new file names
# old_file_name = "original_file.txt"
# new_file_name = "renamed_file.txt"
#
# try:
#     # Rename the file
#     os.rename(old_file_name, new_file_name)
#     print(f"File '{old_file_name}' successfully renamed to '{new_file_name}'.")
# except FileNotFoundError:
#     print(f"Error: The file '{old_file_name}' was not found.")
# except PermissionError:
#     print(f"Error: Permission denied to rename '{old_file_name}'.")
# except OSError as e:
#     print(f"An unexpected error occurred: {e}")


# import shutil

# source_path = 'path/to/source_file.txt'
# destination_path = 'path/to/destination_file.txt'
#
# try:
#     shutil.copyfile(source_path, destination_path)
#     print(f"File '{source_path}' copied to '{destination_path}' successfully.")
# except FileNotFoundError:
#     print(f"Error: Source file '{source_path}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
#