**1. Create a Python Package:**
   - keep the same project structure and add scripts where needed
   - dont create setup.py use the pyproject.toml way of developing the package

**2. check the already implemented the Logger:**
   - the code is in `logger.py`for logging and the configuration is in `_config.py`
   - Implement the logger class, which should extend Python's built-in `logging.Logger` class.
   - check if methods to configure the logger, set up handlers, and format log messages are proper or not.

**3. check the already implemented Slack Notification:**
   - the code is in `slack.py` for Slack integration.
   - Use the `slack-sdk` library to send notifications to Slack.
   - Implement a `notify` method that takes a message and sends it to Slack.

**4. Configuration File (pylogger_slack.toml):**
   - Create a TOML configuration file named `pylogger_slack.toml` with the structure shown in the provided syntax.
   ```
    disable_existing_loggers = false # Whether to disable other loggers (true/false)
    slack_webhook_url = "https://hooks.slack.com/services/T00" # Webhook
    dev = false   # False to send real Slack notifications

    # General settings
    env = "production"  # Environment name
    format_type = "json"  # Output type: "default" (plain), "json", "yaml"

    # Formatter configuration
    [formatters.default]    # Name can be changed (e.g., "custom")
    "()" = "pylogger_slack.logger.LoggerFormatter"  # Class to instantiate (optional, default provided)
    format = "%(asctime)s [%(levelname)s] %(message)s"  # Log format string
    datefmt = "%H:%M:%S"           # Date/time format (optional)
    extra = { "app" = "my_app", "version" = "1.0" }  # Default extra fields
    exclude_fields = ["user_id", "secret"]  # Fields to exclude from structured output

    # Additional formatter example
    [formatters.detailed]
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - tag:%(tag)s"
    extra = { "service" = "api" }
    exclude_fields = ["log.original"]

    # Handler configuration
    [handlers.console]
    class = "logging.StreamHandler"  # Handler class
    level = "INFO"                   # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    formatter = "default"            # Reference to a formatter name
    stream = "ext://sys.stdout"      # Output stream (ext://sys.stdout or ext://sys.stderr)

    [handlers.file]
    class = "logging.FileHandler"
    level = "WARNING"
    formatter = "detailed"
    filename = "app.log"             # File to log to

    # Root logger configuration
    [root]
    level = "DEBUG"                  # Root log level
    handlers = ["console", "file"]   # List of handler names
   ```
   - This file will be used to customize the logger's behavior.

**5. library outcomes**
  - default mode is python logging format
  - additional for json and yaml, when configured in the `pyproject_slack.toml`

**6. Configuration Customization:**
   - Users can customize the logger's behavior by creating a `pylogger_slack.toml` file in their project root directory.
   - The configuration file allows users to set log levels, handlers, formatters, and Slack integration details.

**6. Example Usage:**
   - create a sample (e.g., `example.py`) to demonstrate how to use the package.

**Example Usage:**
```python
# example.py
from pylogger_slack import LOGGER, SLACK

# Log messages
LOGGER.info("This is an info message.")
LOGGER.info("Tagged message", extra={"tag": "v1.0"})

# Send Slack notification
SLACK.notify("Something happened!")
```
**Example Output:**

With the default configuration:
```
2025-03-29 12:34:56 - __main__ - INFO - This is an info message.
2025-03-29 12:34:56 - __main__ - INFO - Tagged message
```

With a custom `pylogger_slack.toml` file:
```json
{"log": "INFO - This is an info message.", "extra": {"app": "my_app"}}
{"log": "INFO - Tagged message", "extra": {"app": "my_app", "tag": "v1.0"}}
```

**9. Documentation:**
   - Document your package using tools with MkDocs.
   - Install the library, create docstrings and configuration for mkdocs, and then create a workflow in `.github/workflow/` for it to generate and publish it with mkdocs.
   - To test locally, give me command in the `README.md`

**10. Testing:**
   - create test cases for the same using `pytest`library inside `tests/` folder

**11. Publishing to PyPI:**
   - publish the package through github workflows to pypi and mkdocs
   - use uv to do the publishing
