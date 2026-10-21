
from explainer import explain_finding


def test_shell_injection_explanation():
    finding = {
        "test_id": "B602",
        "issue_text": "subprocess call with shell=True identified"
    }

    result = explain_finding(finding)

    assert result["title"] == "Potential shell command injection"
    assert "shell=False" in result["recommendation"]


def test_hardcoded_password_explanation():
    finding = {
        "test_id": "B105",
        "issue_text": "Possible hardcoded password"
    }

    result = explain_finding(finding)

    assert result["title"] == "Possible hardcoded password"
    assert "secret manager" in result["recommendation"]


def test_unknown_finding_gets_general_guidance():
    result = explain_finding({
        "test_id": "UNKNOWN",
        "issue_text": "Unknown issue"
    })

    assert result["title"] == "Potential security issue"



def test_partial_executable_path_explanation():
    result = explain_finding({
        "test_id": "B607",
        "issue_text": "Starting a process with a partial executable path"
    })

    assert result["title"] == "Review executable path"
    assert "trusted executable path" in result["recommendation"]


def test_subprocess_arguments_explanation():
    result = explain_finding({
        "test_id": "B603",
        "issue_text": "subprocess call - check for execution of untrusted input."
    })

    assert result["title"] == "Review subprocess arguments"
    assert "validate arguments" in result["recommendation"]
