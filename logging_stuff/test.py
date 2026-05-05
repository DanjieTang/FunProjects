import logging
from logging import basicConfig

basicConfig(level=logging.DEBUG, filename="log.log", filemode="w")

logging.debug("debug lmao")
logging.info("info lmao")
logging.warning("warning lmao")
logging.error("error lmao")
logging.critical("critical lmao")