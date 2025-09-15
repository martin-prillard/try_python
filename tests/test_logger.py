"""Tests for logger module."""

import pytest
from unittest.mock import patch, Mock
import sys

from todo_app.logger import logger, setup_logging


class TestLogger:
    """Test logger functionality."""

    def test_logger_initialization(self):
        """Test that logger is properly initialized."""
        assert logger is not None
        assert hasattr(logger, "info")
        assert hasattr(logger, "warning")
        assert hasattr(logger, "error")
        assert hasattr(logger, "debug")

    @patch("todo_app.logger.loguru.logger")
    def test_logger_methods(self, mock_logger):
        """Test logger methods."""
        # Test info logging
        logger.info("Test info message")
        mock_logger.info.assert_called_once_with("Test info message")

        # Test warning logging
        logger.warning("Test warning message")
        mock_logger.warning.assert_called_once_with("Test warning message")

        # Test error logging
        logger.error("Test error message")
        mock_logger.error.assert_called_once_with("Test error message")

        # Test debug logging
        logger.debug("Test debug message")
        mock_logger.debug.assert_called_once_with("Test debug message")

    @patch("todo_app.logger.loguru.logger")
    def test_logger_with_formatting(self, mock_logger):
        """Test logger with string formatting."""
        logger.info("User %s logged in", "john")
        mock_logger.info.assert_called_once_with("User %s logged in", "john")

        logger.warning("Failed attempt %d", 3)
        mock_logger.warning.assert_called_once_with("Failed attempt %d", 3)

    @patch("todo_app.logger.loguru.logger")
    def test_logger_exception_handling(self, mock_logger):
        """Test logger exception handling."""
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            logger.exception("An error occurred: %s", str(e))
            mock_logger.exception.assert_called_once_with(
                "An error occurred: %s", str(e)
            )

    @patch("todo_app.logger.loguru.logger")
    def test_setup_logging_function(self, mock_logger):
        """Test setup_logging function."""
        # Mock the logger configuration
        mock_logger.remove.return_value = None
        mock_logger.add.return_value = None

        # Call setup_logging
        setup_logging()

        # Verify logger was configured
        mock_logger.remove.assert_called_once()
        mock_logger.add.assert_called()

    @patch("todo_app.logger.loguru.logger")
    def test_logger_context_manager(self, mock_logger):
        """Test logger context manager functionality."""
        with logger.contextualize(user_id=123, request_id="abc"):
            logger.info("Contextual message")
            mock_logger.bind.assert_called_with(user_id=123, request_id="abc")

    def test_logger_is_singleton(self):
        """Test that logger is a singleton."""
        from todo_app.logger import logger as logger1
        from todo_app.logger import logger as logger2

        assert logger1 is logger2

    @patch("todo_app.logger.loguru.logger")
    def test_logger_performance(self, mock_logger):
        """Test logger performance with multiple calls."""
        # Test multiple log calls
        for i in range(10):
            logger.info("Message %d", i)

        assert mock_logger.info.call_count == 10

    @patch("todo_app.logger.loguru.logger")
    def test_logger_different_levels(self, mock_logger):
        """Test different log levels."""
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")

        mock_logger.debug.assert_called_once_with("Debug message")
        mock_logger.info.assert_called_once_with("Info message")
        mock_logger.warning.assert_called_once_with("Warning message")
        mock_logger.error.assert_called_once_with("Error message")
