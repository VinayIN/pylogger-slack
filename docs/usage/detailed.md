# Logging and Slack Notifications

This guide provides a quick overview of using the logging and Slack notification features in `pylogger_slack`.

## Logging

The `pylogger_slack` package provides enhanced logging with structured output formats (plain text, JSON, YAML).

### Example 1: Basic Logging

```python
from pylogger_slack import LOGGER

# Basic logging at different levels
LOGGER.info("Application started")
LOGGER.warning("Database connection slow")
LOGGER.error("Failed to process request", exc_info=True)

# Add structured data to your logs
LOGGER.info("User login", extra={
    "user_id": "user123",
    "ip_address": "192.168.1.1"
})
```

### Example 2: Custom Loggers and Structured Data

```python
import logging
from pylogger_slack.logger import LoggerInitializer

# Create a logger for your specific module
logger = logging.getLogger("my_app.users")
initializer = LoggerInitializer()
initializer(logger=logger)

# Standard logging
logger.info("Processing user request")

# Enhanced structured logging using extra parameter
logger.info("Database query completed", extra={
    "query_time_ms": 42.5,
    "rows_returned": 127,
    "cached": False
})
```

## Slack Notifications

`pylogger_slack` makes it easy to send notifications to your Slack workspace using webhooks.

### Example 1: Basic Notifications

```python
from pylogger_slack import SLACK

# Send a simple notification
SLACK.notify("Database backup completed successfully")

# Send a notification with extra fields
SLACK.notify(
    "User registration spike detected",
    extra_fields={
        "New users": "1,254",
        "Time period": "Last hour",
        "Server": "web-prod-02"
    }
)
```

### Example 2: Custom Notifications

```python
from pylogger_slack.slack import SlackNotification

# Create a custom notification sender with your webhook
notifier = SlackNotification(
    webhook="https://hooks.slack.com/services/XXX/YYY/ZZZ",
    dev=False  # Set to True during development to print instead of send
)

# Use custom blocks for rich formatting
custom_blocks = [
    {
        "type": "header",
        "text": {"type": "plain_text", "text": "🚨 Critical Alert", "emoji": True}
    },
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*Error Rate Exceeded*\nThe application is experiencing high error rates."}
    }
]

notifier.notify("Error rate alert", blocks=custom_blocks)
```
