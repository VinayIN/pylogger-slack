# PyLogger-Slack

A Python logging utility with Slack notification support, built for flexibility and ease of use.

`pylogger_slack` provides a customizable logger with structured output options (plain text, JSON, YAML) and integrates with Slack for notifications. It's designed to work out of the box with sensible defaults while allowing deep customization via a TOML configuration file. 

Key features are:

- **Structured Logging**: Output logs in plain text, JSON, or YAML format
- **Slack Integration**: Easy-to-use Slack notifications
- **Customizable Configuration**: TOML-based configuration with sensible defaults
- **Environment Variable Support**: Use env vars in your configuration

[![Buy me coffee](https://img.shields.io/badge/Buy%20me%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/i_binay)

## Installation

Install `pylogger_slack` via pip:

```bash
pip install pylogger_slack
```

## Quick Example

```python
from pylogger_slack import LOGGER, SLACK

# Basic logging
LOGGER.info("This is an info message")
LOGGER.warning("This is a warning")

# Logging with extra data
LOGGER.info("User action", extra={"user_id": "123", "action": "login"})

# Send a Slack notification
SLACK.notify("System alert: Database connection restored")
```
