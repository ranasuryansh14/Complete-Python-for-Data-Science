from logger import logging
def add(a,b):

    logging.debug("The Addition Operation is Processing")

    return a+b

logging.debug("Addition Function is Called")
add(12,34)