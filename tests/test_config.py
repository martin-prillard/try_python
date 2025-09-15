"""Tests for configuration module."""

import os
from unittest.mock import patch

import pytest

from todo_app.config import Settings


class TestSettings:
    """Test Settings configuration."""

    def test_default_settings(self):
        """Test default configuration values."""
        settings = Settings()

        # Test default values
        assert settings.app_name == "Todo List API"
        assert settings.debug is False
        assert settings.host == "0.0.0.0"
        assert settings.port == 8000
        assert settings.log_level == "INFO"

    @patch.dict(
        os.environ,
        {
            "APP_NAME": "Test App",
            "DEBUG": "true",
            "HOST": "127.0.0.1",
            "PORT": "9000",
            "LOG_LEVEL": "DEBUG",
        },
    )
    def test_settings_from_environment(self):
        """Test settings loaded from environment variables."""
        settings = Settings()

        assert settings.app_name == "Test App"
        assert settings.debug is True
        assert settings.host == "127.0.0.1"
        assert settings.port == 9000
        assert settings.log_level == "DEBUG"

    @patch.dict(os.environ, {"DEBUG": "false"})
    def test_debug_false_from_env(self):
        """Test debug=False from environment."""
        settings = Settings()
        assert settings.debug is False

    @patch.dict(os.environ, {"DEBUG": "1"})
    def test_debug_true_from_env(self):
        """Test debug=True from environment."""
        settings = Settings()
        assert settings.debug is True

    @patch.dict(os.environ, {"PORT": "invalid"})
    def test_invalid_port_from_env(self):
        """Test invalid port from environment raises validation error."""
        with pytest.raises(ValueError):
            Settings()

    def test_settings_validation(self):
        """Test settings validation."""
        # Test valid port range
        with patch.dict(os.environ, {"PORT": "65535"}):
            settings = Settings()
            assert settings.port == 65535

        with patch.dict(os.environ, {"PORT": "1"}):
            settings = Settings()
            assert settings.port == 1

    def test_log_level_validation(self):
        """Test log level validation."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        for level in valid_levels:
            with patch.dict(os.environ, {"LOG_LEVEL": level}):
                settings = Settings()
                assert settings.log_level == level

    @patch.dict(os.environ, {"LOG_LEVEL": "INVALID"})
    def test_invalid_log_level(self):
        """Test invalid log level raises validation error."""
        with pytest.raises(ValueError):
            Settings()

    def test_settings_immutability(self):
        """Test that settings are immutable after creation."""
        settings = Settings()

        # These should not be settable
        with pytest.raises(AttributeError):
            settings.app_name = "New Name"

        with pytest.raises(AttributeError):
            settings.debug = True
