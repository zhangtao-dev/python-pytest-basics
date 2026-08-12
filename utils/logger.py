# utils/logger.py
import logging

def setup_logger(name=__name__, log_level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger