import logging

#configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler() ## input log
    ]
)

logger = logging.getLogger('ArthemeticApp') # call module

def add(a,g):
    result = a+g
    logger.debug(f'Adding {a}+{g},{result}')
    return result 
def sub(a,g):
    result = a-g
    logger.debug(f'subtracting {a}+{g},{result}')
    return result 
def mul(a,g):
    result = a*g
    logger.debug(f'Multyplying {a}+{g},{result}')
    return result 
def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,15)
sub(15,10)
mul(10,20)
divide(20,0)
