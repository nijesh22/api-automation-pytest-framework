import logging
import inspect
import sys
import os

class Logger:
    @staticmethod
    def get_logger(log_level=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        if not logger.handlers:
            os.makedirs("logs", exist_ok=True)

            # File handler
            file_handler = logging.FileHandler("logs/automation.log", mode='a', encoding='utf-8')
            file_formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(name)s : %(message)s',
                datefmt='%I:%M:%S %p %d-%m-%Y'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%I:%M:%S %p %d-%m-%Y'
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

        return logger
