# main.py
from pylogger_slack import LOGGER, SLACK, CONFIG
from pprint import pprint

if __name__ == "__main__":
    LOGGER.info("This is an info message.")
    LOGGER.info("This is a test with extra", extra={"tag": "v0.0.1", "ecs": "some_ecs_data"})
    LOGGER.error("This is an error message.")
    LOGGER.debug("This is a debug message.")
    SLACK.notify("This is a test message for Slack.")