#    Author details for techsupport:
#        - Name: Joe Tan
#        - Email: joetkk@outlook.my
#        - Contact: 016-2010402
#        - Date: 2024-03-06
import logging
import datetime


def write_errorlog(self, message):
    # Create a logger
    logger = logging.getLogger('errorlog')
    logger.setLevel(logging.ERROR)

    # Create a file handler
    today = datetime.date.today().strftime("%Y%m%d")
    file_path = f"errorlog/{today}.txt"
    handler = logging.FileHandler(file_path)
    handler.setLevel(logging.ERROR)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Write the error message to the log file
    logger.error(message)
    return None