import logging
import auxiliary_module
from report import logInit, msg


logger = logging.getLogger("spam_application")


def main():
    logInit(logger, "spam.log", True)
    msg(logger, "d", "only a debug message")
    msg(logger, "e", "on command line too")
    msg(logger, "w", "we ignore the warning")
    msg(logger, "i", "good info, only for the file")
    a = auxiliary_module.Auxiliary()
    auxiliary_module.some_function()
    msg(logger, "i", "after some function")
    a.do_something()


if __name__ == "__main__":
    main()
