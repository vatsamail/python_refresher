import logging
from report import msg

# create logger
logger = logging.getLogger("main.auxiliary")


class Auxiliary:
    def __init__(self):
        # self.logger = logging.getLogger("spam_application.auxiliary.Auxiliary")
        # self.logger.info("creating an instance of Auxiliary")
        msg(logger, "w", "warn at init")

    def do_something(self):
        msg(logger, "i", "before doing something")
        # self.logger.info("doing something")
        a = 1 + 1
        # self.logger.info("done doing something")
        msg(logger, "i", "after doing something:", a)


def some_function():
    msg(logger, "e", "erroring at the same some function")
    # module_logger.info('received a call to "some_function"')
