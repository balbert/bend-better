
import logging.config
import os

# https://docs.python.org/3/library/logging.html#logging.basicConfig

loggerConfigFileName = './fluidsynth/tutorials/1/logger.ini'

def main():
    # Create the logger
    # Admin_Client: The name of a logger defined in the config file
    my_logger = logging.getLogger('Admin_Client')

    # Log some messages
    msg='Bite Me'
    my_logger.debug(msg)
    my_logger.info(msg)
    my_logger.warning(msg)
    my_logger.error(msg)
    my_logger.critical(msg)

if __name__ == '__main__':
    # Configure the logger
    # loggerConfigFileName: The name and path of your configuration file
    logging.config.fileConfig(os.path.normpath(loggerConfigFileName))

    main()

    # Shut down the logger
    logging.shutdown()
    