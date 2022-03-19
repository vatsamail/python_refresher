import logging
from datetime import datetime


def msg(logger, log_type, *args):
    message = " ".join([str(i) for i in args])
    if log_type == "f":
        logger.critical(message)
        exit()
    elif log_type == "w":
        logger.warning(message)
    elif log_type == "e":
        logger.error(message)
    elif log_type == "d":
        logger.debug(message)
    elif log_type == "i":
        logger.info(message)
    elif log_type == "s":
        now = datetime.now()
        info = "# This Stage : " + message + " at " + str(now)
        message = info + " " + message
        print(
            "\n#----------------------------------------------------\n"
            + info
            + "\n#----------------------------------------------------\n"
        )
        logger.info(message)
    else:
        msg(logger, "f", "Cannot understand the logging type:", log_type)


def logInit(logger, file_name, debug=False):
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(file_name, "w")
    if debug:
        fh.setLevel(logging.DEBUG)
    else:
        fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    file_formatter = logging.Formatter(
        fmt="TOOL %(asctime)s,%(name)s,%(module)s,%(funcName)s,%(levelname)s:: %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S %p",
    )
    screen_formatter = logging.Formatter(
        fmt="TOOL %(asctime)s,%(name)s,%(levelname)s:: %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S %p",
    )
    fh.setFormatter(file_formatter)
    ch.setFormatter(screen_formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
