# Configuration Guide

<details>
<summary>Complete pylogger_slack.toml Reference</summary>

```toml
# General settings
disable_existing_loggers = false  # Whether to disable other loggers (true/false)
slack_webhook_url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"  # Slack webhook URL 
dev = true  # Set to false in production to send real Slack notifications
env = "development"  # Environment name (development, production, testing, etc.)
format_type = "json"  # Output format: "default" (plain text), "json", or "yaml"

# Formatter configuration
[formatters.default]
"()" = "logging.Formatter"  # Formatter class
format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"  # Log format
datefmt = "%Y-%m-%d %H:%M:%S"  # Date format
extra = { "app" = "my_app", "version" = "1.0" }  # Default fields added to all logs
exclude_fields = ["password", "token", "secret"]  # Fields to exclude from log output

# Optional: Additional formatter for more detailed logs
[formatters.detailed]
format = "%(asctime)s - [%(levelname)s] [%(name)s] [pid:%(process)d] - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
extra = { "environment" = "${ENV:development}", "app" = "my_app" }

# Console handler configuration
[handlers.console]
class = "logging.StreamHandler"  # Handler class
level = "INFO"  # Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
formatter = "default"  # Reference to formatter defined above
stream = "ext://sys.stdout"  # Output stream

# File handler configuration
[handlers.file]
class = "logging.FileHandler"
level = "DEBUG"
formatter = "detailed"
filename = "logs/app.log"  # File path for logs

# Root logger configuration
[root]
level = "DEBUG"  # Log level threshold for root logger
handlers = ["console", "file"]  # Handlers to use (defined above)

# Optional: Configure specific loggers
[loggers.sqlalchemy]
level = "WARNING"
handlers = ["console"]
propagate = false  # Don't propagate to parent loggers

[loggers.requests]
level = "WARNING"
handlers = ["console"]
propagate = false
```
</details>

This guide explains how to configure `pylogger_slack` to suit your specific needs.

## Configuration File Locations

`pylogger_slack` can be configured using a TOML configuration file. The package looks for configuration in two places (in order of precedence):

1. A file named `pylogger_slack.toml` in your project root
2. A `[tool.pylogger_slack]` section in your project's `pyproject.toml`

For example, if you prefer to keep all your configuration in `pyproject.toml`:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your-project-name"
version = "0.1.0"
# ... other project metadata ...

# pylogger_slack configuration
[tool.pylogger_slack]
version = 1
disable_existing_loggers = false
slack_webhook_url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"
dev = false
env = "production"
format_type = "json"

[tool.pylogger_slack.formatters.default]
"()" = "pylogger_slack.logger.LoggerFormatter"
format = "%(asctime)s [%(levelname)s] %(message)s"
datefmt = "%H:%M:%S"
extra = { "app" = "my_app", "version" = "1.0" }
exclude_fields = ["user_id", "secret"]

[tool.pylogger_slack.handlers.console]
class = "logging.StreamHandler"
level = "INFO"
formatter = "default"
stream = "ext://sys.stdout"

[tool.pylogger_slack.handlers.file]
class = "logging.FileHandler"
level = "WARNING"
formatter = "default"
filename = "app.log"

[tool.pylogger_slack.root]
level = "DEBUG"
handlers = ["console", "file"]
```

This approach allows you to keep all your project configuration in a single file, which many developers prefer for simplicity.

## General Configuration Options

### Development Mode

The `dev` option determines whether Slack notifications are actually sent or just printed to the console:

```toml
# Print to console instead of sending to Slack (useful during development)
dev = true

# Send actual Slack notifications (for production)
dev = false
```

### Environment Name

The `env` option specifies the environment name, which is included in logs and Slack notifications:

```toml
# For development environments
env = "development"

# For production systems
env = "production"

# For testing
env = "testing"
```

### Slack Webhook URL

The `slack_webhook_url` option specifies the webhook URL for sending Slack notifications:

```toml
# Use an explicit webhook URL
slack_webhook_url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

# Or leave it blank to disable Slack notifications
slack_webhook_url = null
```

You can also set this via the `SLACK_WEBHOOK` environment variable.

### Output Format

The `format_type` option determines how logs are formatted:

```toml
# Standard text logs
format_type = "default"

# JSON-formatted logs (good for structured logging)
format_type = "json"

# YAML-formatted logs
format_type = "yaml"
```

JSON and YAML formats include both the log message and any extra fields.

### Existing Loggers

Control whether existing Python loggers should be disabled:

```toml
# Keep existing loggers active (recommended)
disable_existing_loggers = false

# Disable existing loggers
disable_existing_loggers = true
```

## Formatters Configuration

Formatters control how log messages are formatted. You can define multiple formatters for different purposes:

```toml
[formatters.default]
format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
```

### Format String

The `format` option uses Python's standard logging format string syntax:

```toml
# Simple format
format = "%(levelname)s - %(message)s"

# More detailed format
format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

# With process ID and thread name
format = "[%(process)d] %(threadName)s - %(levelname)s - %(message)s"
```

Common format placeholders:
- `%(asctime)s` - Timestamp
- `%(name)s` - Logger name
- `%(levelname)s` - Log level (INFO, WARNING, etc.)
- `%(message)s` - The log message
- `%(filename)s` - Source filename
- `%(lineno)d` - Line number in source file
- `%(process)d` - Process ID

### Date Format

The `datefmt` option controls how timestamps are formatted:

```toml
# Full date and time
datefmt = "%Y-%m-%d %H:%M:%S"

# Shorter time only
datefmt = "%H:%M:%S"

# ISO format
datefmt = "%Y-%m-%dT%H:%M:%S%z"
```

### Default Extra Fields

The `extra` option lets you add default fields to all log records:

```toml
[formatters.default]
extra = { "app" = "my_app", "version" = "1.0", "env" = "production" }
```

These fields will be included in structured output formats (JSON, YAML).

### Excluding Sensitive Information

The `exclude_fields` option lets you prevent certain fields from appearing in logs:

```toml
[formatters.default]
exclude_fields = ["password", "credit_card", "auth_token"]
```

## Handlers Configuration

Handlers determine where logs are sent. You can configure multiple handlers to send logs to different destinations:

```toml
[handlers.console]
class = "logging.StreamHandler"
level = "INFO"
formatter = "default"
stream = "ext://sys.stdout"

[handlers.file]
class = "logging.FileHandler"
level = "DEBUG"
formatter = "detailed"
filename = "logs/app.log"
```

### Common Handler Types

- **StreamHandler**: Outputs to console (stdout/stderr)
- **FileHandler**: Writes to a file
- **RotatingFileHandler**: Writes to a file, with rotation based on size
- **TimedRotatingFileHandler**: Writes to a file, with rotation based on time

### Handler Levels

Each handler can have its own log level:

```toml
# Only show INFO and above
level = "INFO"

# Capture all logs including DEBUG
level = "DEBUG"

# Only important warnings and errors
level = "WARNING"
```

Available levels in order of severity: DEBUG, INFO, WARNING, ERROR, CRITICAL

## Root Logger Configuration

The root logger settings apply to all logging in your application:

```toml
[root]
level = "DEBUG"
handlers = ["console", "file"]
```

This configures the root logger to:
1. Capture all logs of DEBUG level and above
2. Send logs to both the console and file handlers

## Configuring Specific Loggers

You can configure individual loggers for different parts of your application:

```toml
[loggers.sqlalchemy]
level = "WARNING"
handlers = ["console"]
propagate = false

[loggers.requests]
level = "WARNING"
handlers = ["console"]
propagate = false
```

Setting `propagate = false` prevents messages from being passed to parent loggers.

## Using Environment Variables

You can include environment variables in your configuration using `${VAR}` or `${VAR:default}` syntax:

```toml
# Use LOG_LEVEL from environment, defaulting to "INFO"
[root]
level = "${LOG_LEVEL:INFO}"

# Use APP_NAME from environment with no default
[formatters.default]
extra = { "app" = "${APP_NAME}" }
```
