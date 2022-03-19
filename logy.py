import logging
from logme import LogInit

extra_data = {
   'user': "Vatsa Prahallada",
    'contact': "vatsamail@gmail.com",
} # part of custom logging

def myFunc():
    logging.debug("This is a debug at myFunction", extra=extra_data)

def main():
    fmtstr = "%(asctime)s: %(lineno)d: %(levelname)s: %(levelno)d: %(funcName)s: %(module)s: %(contact)s %(message)s" # part of custom logging
    datestr = "%Y-%m-%d %I:%M:%S %p" # part of custom logging
    logging.basicConfig(
                        level=logging.DEBUG,
                        filename="logging_output.log",
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr,

    ) # one time effect only
    # filemode default is append
    
    logging.debug("This is a debug message", extra=extra_data) # not default
    logging.info("This is an info message", extra=extra_data) # not default
    logging.warning("This is a warning message", extra=extra_data)
    logging.error("This is an error message", extra=extra_data)
    logging.critical("This is a critical/fatal message", extra=extra_data)
    logging.info("Here is a formatted logging function printing: {}".format("ALOHA!", 10), extra=extra_data)
    myFunc()

if __name__ == '__main__':
    main()