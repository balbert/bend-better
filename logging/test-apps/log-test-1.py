
import logging

# Configure the logger to write to a file
logging.basicConfig(
    filename='logs/app.log', # Specify the log file name
    level=logging.INFO, # Set the logging level (e.g., INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s' # Define the log message format
    # format='%(asctime)s :: %(levelname)s :: %(message)s' # Define the log message format
)

# logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level=logging.INFO)
# logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', level=logging.DEBUG)

def addition(x, y):
    add = x + y
    return add

def subtract(x, y):
    sub = x - y
    return sub

def multiply(x, y):
    mul = x * y
    return mul

def divide(x, y):
    div = x / y
    return div

def exponent(x, y):
    exp = x ** y
    return exp

num1 = 20
num2 = 2

def main():
    # Get a logger instance (optional, basicConfig configures the root logger)
    logger = logging.getLogger(__name__)

    # Log messages
    logger.info('This is an informational message.')
    logger.debug('This is a debug message, which might not be shown if level is INFO or higher.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')

    add_result = addition(num1, num2)
    logging.info('Add: {} + {} = {}'.format(num1, num2, add_result))

    sub_result = subtract(num1, num2)
    logging.info('Sub: {} - {} = {}'.format(num1, num2, sub_result))

    mul_result = multiply(num1, num2)
    logging.info('Mul: {} * {} = {}'.format(num1, num2, mul_result))

    div_result = divide(num1, num2)
    logging.info('Div: {} / {} = {}'.format(num1, num2, div_result))

    exp_result = exponent(num1, num2)
    logging.info('Exp: {} ** {} = {}'.format(num1, num2, exp_result))

if __name__ == "__main__":
    main()
