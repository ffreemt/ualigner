"""Define ualigner."""
# pylint: disable=invalid-name
import os
import logzero
from logzero import logger

try:
    loglevel = int(os.environ.get("loglevel"))
except:
    loglevel = 20
_ = """
if os.environ.get("loglevel").lower() in ["info"]:
    loglevel = 20
if os.environ.get("loglevel").lower() in ["debug"]:
    loglevel = 10
# """

logzero.loglevel(loglevel)  # change to 10 to turn on debug


def ualigner():
    """Define."""
    logger.info(" entry ")
    logger.debug(" entry ")


if __name__ == "__main__":
    ualigner()
