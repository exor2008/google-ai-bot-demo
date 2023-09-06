import logging
import os

from dotenv import load_dotenv

load_dotenv()


logger = logging.getLogger("AIbot logger")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
