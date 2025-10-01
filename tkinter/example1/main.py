
#################################################################################################################
#                                                                                                               #
#   ██████████                                                                ████                       ████   #
#  ▒▒███▒▒▒▒▒█                                                               ▒▒███                      ▒▒███   #
#   ▒███  █ ▒     █████ █████     ██████      █████████████      ████████     ▒███      ██████           ▒███   #
#   ▒██████      ▒▒███ ▒▒███     ▒▒▒▒▒███    ▒▒███▒▒███▒▒███    ▒▒███▒▒███    ▒███     ███▒▒███          ▒███   #
#   ▒███▒▒█       ▒▒▒█████▒       ███████     ▒███ ▒███ ▒███     ▒███ ▒███    ▒███    ▒███████           ▒███   #
#   ▒███ ▒   █     ███▒▒▒███     ███▒▒███     ▒███ ▒███ ▒███     ▒███ ▒███    ▒███    ▒███▒▒▒            ▒███   #
#   ██████████    █████ █████   ▒▒████████    █████▒███ █████    ▒███████     █████   ▒▒██████           █████  #
#  ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒▒     ▒▒▒▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒     ▒███▒▒▒     ▒▒▒▒▒     ▒▒▒▒▒▒           ▒▒▒▒▒   #
#                                                                ▒███                                           #
#                                                                █████                                          #
#                                                               ▒▒▒▒▒                                           #
#                                                                                                               #
#################################################################################################################

# https://www.geeksforgeeks.org/python/create-first-gui-application-using-python-tkinter/

import logging.config
import os
import shutil
import time
import random

import tkinter as tk

LOGGING_CONFIG_FILE_NAME = "tkinter/example1/logging.ini"
LOGGING_LOGGER_NAME = "client"
LOGGING_FILE_HANDLER_NAME = "file"
LOGGING_FILE_NAME = "example1"

''' function clicked() - display text when button is clicked '''
def clicked1(label):
    """
    This function will be called when the button is clicked.
    """
    #print("Here I am")
    label.configure(text = "I just got clicked")

''' function test1() '''
def test1():
    # Create root window
    root = tk.Tk()

    # Root window title and dimension
    root.title("Welcome to GeekForGeeks")
    # Set geometry (width x height)
    root.geometry('350x200')

    # All widgets will be here

    # Adding a label to the root window
    lbl = tk.Label(root, text = "Are you a Geek?")
    lbl.grid()

    # Button widget with red color text inside
    btn = tk.Button(root, text = "Click me", fg = "red", command = lambda: clicked1(lbl))

    # Set Button grid
    btn.grid(column = 1, row = 0)
    
    # Execute Tkinter
    root.mainloop()

''' function clicked() - display user text when button is clicked '''
def clicked2(txt, lbl):
    """
    This function will be called when the button is clicked.
    """
    res = "You wrote: " + txt.get()
    lbl.configure(text = res)

''' function test2() '''
def test2():
    # Create root window
    root = tk.Tk()

    # Root window title and dimension
    root.title("Welcome to GeekForGeeks")
    # Set geometry(width x height)
    root.geometry('400x200')

    # Adding a label to the root window
    lbl1 = tk.Label(
        root, 
        padx=10, pady=10, 
        text="Are you a Geek?"
        )
    
    lbl1.grid(
        column=0, row=0, 
        padx=10, pady=10
        )

    # Adding Entry Field
    txt1 = tk.Entry(
        root, 
        width=10
        )
    
    txt1.grid(
        column=1, row=0, 
        padx=10, pady=10
        )

    # Button widget with red color text inside
    btn1 = tk.Button(
        root,
        padx=10, pady=10,
        width=10,
        text="Click me",
        fg="red",
        command = lambda: clicked2(txt1, lbl2)
        )

    btn1.grid(
        column=2, row=0, 
        padx=10, pady=10
        )

    # Adding a label to the root window
    lbl2 = tk.Label(
        root, 
        padx=10, pady=10, 
        text="your entry here"
        )
    
    lbl2.grid(
        column=0, row=1, columnspan=3, 
        padx=10, pady=10
        )

    # Execute Tkinter
    root.mainloop()


''' function main() '''
def main():
    say_quote()

    #test1()
    test2()

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

    # If the new file doesn't exist create it
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
    handler.baseFilename = os.path.abspath(new_name)

    # Clean up old log file
    os.remove(old_name) if os.path.exists(old_name) else None


''' function init_logging() - initial/instantiate '''
def init_logging(config_name, logger_name, level=logging.INFO):
    # Configure the logger
    logging.config.fileConfig(os.path.normpath(config_name))

    # Open/Instantiate logfile
    logger = logging.getLogger(logger_name)

    # Set the logging level
    logger.setLevel(level)

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

    logger = init_logging(LOGGING_CONFIG_FILE_NAME, LOGGING_LOGGER_NAME, logging.DEBUG)

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

    # Create an important message
    msg = 'There can be only one!'

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

