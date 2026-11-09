import pytest
from unittest.mock import mock_open, patch
from file_handler import read_lines

class TestFileHandler:
    """Test suite for file system operations using unittest.mock."""

    def test_read_lines_success(self):
        mock_content = "First line\nSecond line\n"
        
        with patch("builtins.open", mock_open(read_data=mock_content)) as mocked_file:
            result = read_lines("sample.txt")
            
            assert result == ["First line\n", "Second line\n"]
            mocked_file.assert_called_once_with("sample.txt", "r", encoding="utf-8")

    def test_read_lines_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with pytest.raises(FileNotFoundError):
                read_lines("non_existent.txt")

    def test_read_lines_invalid_path_type(self):
        with pytest.raises(TypeError) as exc_info:
            read_lines(12345)
        
        assert str(exc_info.value) == "File path must be a string."