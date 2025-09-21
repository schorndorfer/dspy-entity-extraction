import pytest
from dspy_entity_extraction.cli import app, main
from dspy_entity_extraction import __version__


def test_cli_main_function_exists():
    """Test that CLI main function exists and is callable."""
    assert callable(main)


def test_cli_app_exists():
    """Test that CLI app exists."""
    assert app is not None
    assert hasattr(app, 'name')
    # cyclopts app.name is a tuple, so check if our name is in it
    assert "dspy-entity-extraction" in app.name


class TestCLICommands:
    """Test class for CLI command functionality."""

    def test_version_command_output(self, capsys):
        """Test that version command produces expected output."""
        try:
            # Import and call version function directly
            from dspy_entity_extraction.cli import version
            version()
            captured = capsys.readouterr()
            assert __version__ in captured.out
            assert "dspy-entity-extraction version" in captured.out
        except SystemExit:
            # Expected when running CLI commands
            pass

    def test_commands_are_functions(self):
        """Test that command functions exist and are callable."""
        from dspy_entity_extraction.cli import extract, train, evaluate, version

        assert callable(extract)
        assert callable(train)
        assert callable(evaluate)
        assert callable(version)