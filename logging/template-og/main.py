
import logging.config
import os
import shutil
import time

# The name and path to the configuration file
loggerConfigFileName = "tkinter/template/logging.ini"


''' function main() '''
def main():
    quote = """
    A person needs new experiences. It jars something deep inside, allowing them to grow.
    Without change something sleeps inside us, and seldom awakens. The sleeper must awaken.”
    ― Duke Leto Atreides
    """
    print(quote)


''' get a reference to the FIleHandler object '''
def get_FileHandler(name):
    for nm, lgr in logging.Logger.manager.loggerDict.items():
        if not isinstance(lgr, logging.PlaceHolder):
            for hndlr in lgr.handlers:
                if isinstance(hndlr, logging.FileHandler):
                    if hndlr.name == name:
                        return hndlr 


''' rename/copy existing logfile '''
def rename_logfile(h, old, new, rename=True):
    # Close the existing handler
    h.close()

    # Rename/copy old file to new name
    if rename:
        try:
            os.rename(old, new)
        except FileNotFoundError:
            print(f"Error: The file '{old}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied to rename '{old}'.")
        except OSError as e:
            print(f"An unexpected error occurred: {e}")
    else: # copy
        try:
            shutil.copy(old, new)
        except FileNotFoundError:
            print(f"Error: Source file '{old}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Update the baseFilename attribute
    # It's good practice to get the absolute path for consistency
    h.baseFilename = os.path.abspath(new)

    # Re-open the handler (this implicitly happens when it's used again)
    # If you need to force it open immediately, you could re-add it to
    # the logger (though updating baseFilename is usually sufficient
    # for subsequent logging)
    logger.removeHandler(h)
    logger.addHandler(h)

    # Clean up created log files
    # os.remove(old_name) if os.path.exists(old_name) else None


if __name__ == '__main__':

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Initialize logging
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Configure the logger
    logging.config.fileConfig(os.path.normpath(loggerConfigFileName))

    # Open/Instantiate logfile
    logger = logging.getLogger('Admin_Client')

    # Log initial message (current log file)
    logger.info(f"Python application started @ {time.strftime("%Y-%m-%d_%H:%M:%S")}")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Rename/Copy/Move log file
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Get a reference to the FileHandler object
    handler = get_FileHandler("fileHandler")

    # Get current log file name
    old_name = handler.baseFilename

    # Split file name into path and name components
    directory, filename = os.path.split(old_name)

    # Create a new log file name
    new_name = directory + '/my-app_' + time.strftime("%Y-%m-%d_%H:%M:%S") + '.log'

    # Rename the current log file
    rename_logfile(handler, old_name, new_name)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Sends some messages to the new log file
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # logger = logging.getLogger('Admin_Client')

    # Create an important message
    msg='There can be only one!'

    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    logger.critical(msg)

    # Let's do this...
    main()

    # Shut down the logger
    logging.shutdown()
