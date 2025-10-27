from logger import logging
def add (a,b):
    logging.debug("The addition operation is taing place")
    return a+b

logging.debug("The addition function is calles")
add(10,15)