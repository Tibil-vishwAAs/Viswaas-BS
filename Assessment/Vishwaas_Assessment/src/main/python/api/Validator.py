import json
import time
import datetime
import logging
# Create a logger
logger = logging.getLogger('Assessment-logger')
# Create a file handler to write logs to a file
handler = logging.FileHandler('/home/amith/Desktop/Vishwass/Runner/vishwaas-final-poc-1/vishwaas/src/main/python/api/assessment.log', mode='a')
# Set the logging level to INFO
logger.setLevel(logging.INFO)
# Create a formatter to format the log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the formatter for the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


def validate(self,data):
    logger.info("Parsing the validation json specification file")
    with open('config.json') as config_file:
        config_data = json.load(config_file)

    Version = config_data['Column']['ver']

    assert data.status_code == 200
    print(f"Response code: {data.status_code}")
    logger.info("Validating the API version ")
    response_version = data['ver']
    if response_version in Version:
        # print('Response version matches the config version:', response_version)
        logger.info(f"version:{response_version} validation is successful and match NBFC-AA ecosystem version")
    else:
        print('Response version does not match the config version')
        logger.info(f"version:{response_version} validation is unsuccessful, not match NBFC-AA ecosystem version")

    assert data.ok == True, 'Response is not displayed as "OK"'
    print('Response is displayed as "OK"')
    return "ok"
