import logging.config
import os
import shutil
import time

# The name and path to the configuration file
LOGGING_CONFIG_FILENAME = "logging/logging.ini"

''' function main() '''
def main():
    quote = """
    A person needs new experiences. It jars something deep inside, allowing them to grow.
    Without change something sleeps inside us, and seldom awakens. The sleeper must awaken.”
    ― Duke Leto Atreides
    """
    print(quote)


''' function listLoggers1() '''
def listLoggers1():
    rootlogger = logging.getLogger()
    print(rootlogger)
    for h in rootlogger.handlers:
        print('     %s' % h)

    for nm, lgr in logging.Logger.manager.loggerDict.items():
        print('+ [%-20s] %s ' % (nm, lgr))
        if not isinstance(lgr, logging.PlaceHolder):
            for h in lgr.handlers:
                print('     %s' % h)


''' function listLoggers2() '''
def listLoggers2():
    logger = logging.getLogger()
    print(f"logger -> name: {logger.name}, logger: {logger}")
    for hndlr in logger.handlers:
        print(f"handler -> name: {hndlr.get_name()}, handler: {hndlr}")
    print()

    for nm, lgr in logging.Logger.manager.loggerDict.items():
        print(f"logger -> name: {nm}, logger: {lgr}")
        if not isinstance(lgr, logging.PlaceHolder):
            for hndl in lgr.handlers:
                print(f"handler -> name: {hndl.get_name()}, handler: {hndl}")
                print()

                #print(hndl.__dict__)
                #print()

                print(f"Enumerate dictionary for handler -> {hndl.get_name()}")
                for i, key in enumerate(hndl.__dict__):
                    print(f"  index: {i}, {key} :: {hndl.__dict__[key]}")
                print()


''' function get_FileHandler() '''
def get_FileHandler(name):
    for nm, lgr in logging.Logger.manager.loggerDict.items():
        print(f"logger: {lgr}")
        if not isinstance(lgr, logging.PlaceHolder):
            print(f"logger name: {lgr.name}")
            for hndlr in lgr.handlers:
                if isinstance(hndlr, logging.FileHandler):
                    print(f"handler name: {hndlr.name}")
                    if hndlr.name == name:
                        return hndlr 


''' function renameLogFile() '''
def renameLogFile(hndlr, old_name, new_name, rename=True):
    # Close the existing handler
    hndlr.close()

    # Rename/Copy old file to new name
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

    # Update the baseFilename attribute
    # It's good practice to get the absolute path for consistency
    hndlr.baseFilename = os.path.abspath(new_name)

    # Re-open the handler (this implicitly happens when it's used again)

    # If you need to force it open immediately, you could re-add it to
    # the logger. Though updating "baseFilename" is usually sufficient
    # for subsequent logging

    # For a clean re-initialization, you might remove and re-add:
    logger.removeHandler(handler)
    logger.addHandler(handler)

    # Clean up old log file
    os.remove(old_name) if os.path.exists(old_name) else None

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    # Configure the logger
    logging.config.fileConfig(os.path.normpath(LOGGING_CONFIG_FILENAME))

    logger = logging.getLogger('Admin_Client')
    logger.info("This is the first log message in the initial file.")

    listLoggers2()

    handler = get_FileHandler("fileHandler")

    # /mnt/c/IAS_Projects/Work/Python/music/logs/dummy_2025-09-26_18:29:46.log
    old_name = handler.baseFilename
    directory, filename = os.path.split(old_name)
    print(f"Directory: {directory}, Filename: {filename}")

    # /mnt/c/IAS_Projects/Work/Python/music/logs/my-app_
    #new_name = directory + '/my-app_' + time.strftime("%Y-%m-%d") + '.log'
    new_name = directory + '/my-app_' + time.strftime("%Y-%m-%d_%H:%M:%S") + '.log'

    renameLogFile(handler, old_name, new_name)

    # Admin_Client: The name of a logger defined in the config file
    # Create the logger if necessary
    logger = logging.getLogger('Admin_Client')

    msg = 'There can be only one!'

    print()
    logger.debug(msg)
    logger.info(msg)
    logger.warning(msg)
    logger.error(msg)
    logger.critical(msg)
    print()

    # Shut down the logger
    logging.shutdown()

