import pytest
from main import main


def test_main_function_exists():
    """Test that main function exists and is callable."""
    assert callable(main)


def test_main_runs_without_error():
    """Test that main function runs without raising an exception."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")


class TestMainModule:
    """Test class for main module functionality."""

    def test_main_output(self, capsys):
        """Test that main function produces expected output."""
        main()
        captured = capsys.readouterr()
        assert "Hello from dspy-entity-extraction!" in captured.out

    def test_main_no_errors(self, capsys):
        """Test that main function doesn't produce any errors."""
        main()
        captured = capsys.readouterr()
        assert captured.err == ""