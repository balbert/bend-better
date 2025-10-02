
import logging.config
import os
import shutil
import time

# The name and path to the configuration file
loggerConfigFileName = "tkinter/logging.ini"

""" function main """
def main():
    quote = """
    A person needs new experiences. It jars something deep inside, allowing them to grow.
    Without change something sleeps inside us, and seldom awakens. The sleeper must awaken.”
    ― Duke Leto Atreides
    """
    print(quote)

""" get the FileHandler from the loaded logger """
def get_FileHandler(name):
    for nm, lgr in logging.Logger.manager.loggerDict.items():
        if not isinstance(lgr, logging.PlaceHolder):
            for hndlr in lgr.handlers:
                if isinstance(hndlr, logging.FileHandler):
                    if hndlr.name == name:
                        return hndlr 

""" change the basename of the current handler """
def rename_logfile(hndlr, old_name, new_name, rename=True):
    # 1. Close the existing handler
    hndlr.close()

    # 2. Rename/Copy old file to new name
    if rename:
        try:
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print(f"Error: The file '{old_name}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied to rename '{old_name}'.")
        except OSError as e:
            print(f"An unexpected error occurred: {e}")
    else: # copy
        try:
            shutil.copy(old_name, new_name)
        except FileNotFoundError:
            print(f"Error: Source file '{old_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # 3. Update the baseFilename attribute
    #    It's good practice to get the absolute path for consistency
    hndlr.baseFilename = os.path.abspath(new_name)

    # 4. Re-open the handler (this implicitly happens when it's used again)
    #    If you need to force it open immediately, you could re-add it to
    #    the logger (though updating baseFilename is usually sufficient
    #    for subsequent logging)
    logger.removeHandler(handler)
    logger.addHandler(handler)

    # Clean up created log files
    # os.remove(old_name) if os.path.exists(old_name) else None

#     ██████   ██████      █████████      █████    ██████   █████
#    ░░██████ ██████      ███░░░░░███    ░░███    ░░██████ ░░███ 
#     ░███░█████░███     ░███    ░███     ░███     ░███░███ ░███ 
#     ░███░░███ ░███     ░███████████     ░███     ░███░░███░███ 
#     ░███ ░░░  ░███     ░███░░░░░███     ░███     ░███ ░░██████ 
#     ░███      ░███     ░███    ░███     ░███     ░███  ░░█████ 
#     █████     █████    █████   █████    █████    █████  ░░█████
#    ░░░░░     ░░░░░    ░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░ 

if __name__ == '__main__':

    #---------------------------------------------------------------------------
    # Initialize logging
    #---------------------------------------------------------------------------

    # Configure the logger
    logging.config.fileConfig(os.path.normpath(loggerConfigFileName))

    # Get a logger instance
    logger = logging.getLogger('Admin_Client')

    # Log an initial message
    msg = "App started @ " + time.strftime("%Y-%m-%d_%H:%M:%S")
    logger.info(msg)

    #---------------------------------------------------------------------------
    # Rename the logfile
    #---------------------------------------------------------------------------

    # Get the current name of the log file from the file handler
    handler = get_FileHandler("fileHandler")
    old_name = handler.baseFilename

    # Split the current name into path and filename components
    directory, filename = os.path.split(old_name)

    # Create a new log file name
    new_name = directory + '/my-app_' + time.strftime("%Y-%m-%d_%H:%M:%S") + '.log'

    # Rename the log file to the new name
    rename_logfile(handler, old_name, new_name)

    #---------------------------------------------------------------------------
    # Log test messages
    #---------------------------------------------------------------------------

    # Prepare a message for logging
    msg = 'There can be only one!'

    # Log messages to file and console
    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    logger.critical(msg)

    # Run the program
    main()

    # Shut down the logger
    logging.shutdown()
