
#################################################################################################################
#                                                                                                               #
#   ███████████                                                ████                   █████                     #               
#  ▒█▒▒▒███▒▒▒█                                               ▒▒███                  ▒▒███                      #
#  ▒   ▒███  ▒      ██████     █████████████      ████████     ▒███      ██████      ███████       ██████       #
#      ▒███        ███▒▒███   ▒▒███▒▒███▒▒███    ▒▒███▒▒███    ▒███     ▒▒▒▒▒███    ▒▒▒███▒       ███▒▒███      #
#      ▒███       ▒███████     ▒███ ▒███ ▒███     ▒███ ▒███    ▒███      ███████      ▒███       ▒███████       #
#      ▒███       ▒███▒▒▒      ▒███ ▒███ ▒███     ▒███ ▒███    ▒███     ███▒▒███      ▒███ ███   ▒███▒▒▒        #
#      █████      ▒▒██████     █████▒███ █████    ▒███████     █████   ▒▒████████     ▒▒█████    ▒▒██████       #
#     ▒▒▒▒▒        ▒▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒     ▒███▒▒▒     ▒▒▒▒▒     ▒▒▒▒▒▒▒▒       ▒▒▒▒▒      ▒▒▒▒▒▒        #
#                                                 ▒███                                                          #
#                                                 █████                                                         #
#                                                ▒▒▒▒▒                                                          #
#                                                                                                               #
#################################################################################################################

import logging.config
import os
import shutil
import time
import random
import array as arr

# The name and path to the configuration file
LOGGING_CONFIG_FILE_NAME = "tkinter/example1/logging.ini"
LOGGING_LOGGER_NAME = "client"
LOGGING_FILE_HANDLER_NAME = "file"
LOGGING_FILE_NAME = "example1"

''' function main() '''
def main():
    say_quote()

''' functions say_quote() - print out a quote '''
def say_quote():

    citation = [
        "A person needs new experiences. It jars something deep inside, allowing them to grow.",
        "Without change something sleeps inside us, and seldom awakens. The sleeper must awaken."
    ]
    source = [
        "Duke Leto Atreides"
    ]

    quote = [citation, source]
    quote_list = [quote]

    citation = [
        "If you understand why:",
        "  pizza is round,",
        "  packed in a square box,",
        "  and eaten as a triangle",
        "then you will understand women."
    ]
    source = [
        "Wise Man"
    ]

    quote = [citation, source]
    quote_list.append(quote)

    quote = [
        "Understanding what a woman wants is very difficult",
        "it's like trying to figure out what color the letter 7 smells like.",
        "Unknown"
    ]

    quote = [citation, source]
    quote_list.append(quote)

    citation = [
        "Seven things men do to upset women",
        "----------------------------------",
        "  1. Lie",
        "  2. Be honest",
        "  3. Not talk",
        "  4. Talk too much",
        "  5. Not show emotions",
        "  6. Be too emotional",
        "  7. Breathe"
    ]
    source = [
        "Unknown"
    ]

    quote = [citation, source]
    quote_list.append(quote)

    citation = [
        "He's not the sharpest marble in the sea."
    ]
    source = [
        "Frank Herzig"
    ]

    quote = [citation, source]
    quote_list.append(quote)

    index = random.randint(0, len(quote) - 1)
    print()
    print('\n'.join([f"  {str(x)}" for x in quote_list[index][0]]))
    print()
    print('- ' + quote_list[index][1][0] + '\n')

''' function get_handler() - get a reference to the FileHandler object '''
def get_handler(name):
    for nm, lgr in logging.Logger.manager.loggerDict.items():
        if not isinstance(lgr, logging.PlaceHolder):
            for h in lgr.handlers:
                if isinstance(h, logging.FileHandler):
                    if h.name == name:
                        return h 


''' function move_logfile() - move/rename/copy existing logfile '''
def move_logfile(handler, old_name, new_name, rename=True):
    # Close the existing handler
    handler.close()

    # If the new file doesn't exists create it
    if not os.path.exists(new_name):
        # Rename/copy old file to new name
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
    handler.baseFilename = os.path.abspath(new_name)

    # Re-open the handler (this implicitly happens when it's used again)
    # If you need to force it open immediately, you could re-add it to
    # the logger (though updating baseFilename is usually sufficient
    # for subsequent logging)
    #logger.removeHandler(h)
    #logger.addHandler(h)

    # Clean up created log files
    os.remove(old_name) if os.path.exists(old_name) else None


''' function init_logging() - initial/instantiate '''
def init_logging(config_name, logger_name):
    # Configure the logger
    logging.config.fileConfig(os.path.normpath(config_name))

    # Open/Instantiate logfile
    logger = logging.getLogger(logger_name)

    # return the logger
    return logger


''' function log_start() - log application start time'''
def log_start_time(logger):
    time_stamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    logger.info(f"Python application started @ {time_stamp}")


''' function log_stop() - log application start time'''
def log_stop_time(logger):
    time_stamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    logger.info(f"Python application stopped @ {time_stamp}")


''' function rename_logfile() - rename/copy/move log file '''
def rename_logfile(handler_name, file_name, fine=False):
    # Get a reference to the FileHandler object
    handler = get_handler(handler_name)

    # Get current log file name
    old_name = handler.baseFilename

    # Split file name into path and name components
    dir_name = os.path.dirname(old_name)

    # Create a new log file name
    if fine:
        time_stamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    else:
        time_stamp = time.strftime("%Y-%m-%d")
    new_name = dir_name + '/' + file_name + '-' + time_stamp + '.log'

    # Rename the current log file
    move_logfile(handler, old_name, new_name)


'''
     ██████   ██████      █████████      █████    ██████   █████
    ▒▒██████ ██████      ███▒▒▒▒▒███    ▒▒███    ▒▒██████ ▒▒███ 
     ▒███▒█████▒███     ▒███    ▒███     ▒███     ▒███▒███ ▒███ 
     ▒███▒▒███ ▒███     ▒███████████     ▒███     ▒███▒▒███▒███ 
     ▒███ ▒▒▒  ▒███     ▒███▒▒▒▒▒███     ▒███     ▒███ ▒▒██████ 
     ▒███      ▒███     ▒███    ▒███     ▒███     ▒███  ▒▒█████ 
     █████     █████    █████   █████    █████    █████  ▒▒█████
    ▒▒▒▒▒     ▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒ 

'''                                                                                                                    
if __name__ == '__main__':

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Initialize and start logging
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    logger = init_logging(LOGGING_CONFIG_FILE_NAME, LOGGING_LOGGER_NAME)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Rename log file
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    rename_logfile(LOGGING_FILE_HANDLER_NAME, LOGGING_FILE_NAME)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Log time
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    log_start_time(logger)

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

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Log time
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    log_stop_time(logger)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Shut down logging
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    logging.shutdown()
