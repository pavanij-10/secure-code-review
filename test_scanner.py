from pathlib import Path
from scanner import scan_file

SAMPLE_FILE = Path(__file__).parent / "sample_vulnerable.py"


def test_scan_completes_successfully():
    result = scan_file(SAMPLE_FILE)
    assert result["success"] is True


def test_shell_execution_issue_is_detected():
    result = scan_file(SAMPLE_FILE)
    assert result["success"] is True
    assert any(
        "shell=True" in finding["issue_text"]
        for finding in result["findings"]
    )


def test_hardcoded_password_is_detected():
    result = scan_file(SAMPLE_FILE)
    assert result["success"] is True
    assert any(
        "hardcoded password" in finding["issue_text"].lower()
        for finding in result["findings"]
    )


def test_missing_file_is_rejected():
    result = scan_file("file_that_does_not_exist.py")
    assert result["success"] is False
