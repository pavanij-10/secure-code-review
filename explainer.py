
def explain_finding(finding):
    issue = finding.get("issue_text", "")
    test_id = finding.get("test_id", "")

    if test_id == "B602":
        return {
            "title": "Potential shell command injection",
            "risk": (
                "Using shell=True with untrusted input can allow "
                "unexpected commands to execute. Review whether "
                "user-controlled data reaches this command."
            ),
            "recommendation": (
                "Prefer subprocess.run with a list of arguments "
                "and shell=False. Validate inputs where appropriate "
                "and avoid passing untrusted data to a shell."
            ),
            "secure_example": (
                "subprocess.run(['echo', user_input], "
                "check=True, shell=False)"
            ),
            "reference": "https://cwe.mitre.org/data/definitions/78.html"
        }

    if test_id == "B105":
        return {
            "title": "Possible hardcoded password",
            "risk": (
                "A password embedded in source code may be exposed "
                "through repositories, backups, or shared files. "
                "Verify whether the detected string is a real secret."
            ),
            "recommendation": (
                "Remove hardcoded secrets. Load secrets from "
                "environment variables or a suitable secret manager. "
                "If a real password was exposed, rotate it."
            ),
            "secure_example": (
                "import os\n"
                "password = os.environ.get('APP_PASSWORD')\n"
                "if not password:\n"
                "    raise RuntimeError('APP_PASSWORD is not configured')"
            ),
            "reference": "https://cwe.mitre.org/data/definitions/259.html"
        }

    if test_id == "B404":
        return {
            "title": "Informational: subprocess module imported",
            "risk": (
                "Importing subprocess alone is not a vulnerability. "
                "This finding is informational; inspect command "
                "execution separately for unsafe usage."
            ),
            "recommendation": (
                "Review subprocess calls for unsafe shell execution "
                "and untrusted input. Do not treat this import alone "
                "as a confirmed security vulnerability."
            ),
            "secure_example": (
                "No change is required for the import alone. "
                "Review how subprocess functions are used."
            ),
            "reference": "https://docs.python.org/3/library/subprocess.html"
        }

    if test_id == "B607":
        return {
            "title": "Review executable path",
            "risk": (
                "Using a partial executable name may cause a different "
                "program to be selected, depending on the environment."
            ),
            "recommendation": (
                "Where practical, configure a trusted executable path "
                "and review the environment used to launch the process."
            ),
            "secure_example": (
                "subprocess.run(\n"
                "    [trusted_executable_path, message],\n"
                "    check=True,\n"
                "    shell=False\n"
                ")"
            ),
            "reference": (
                "https://bandit.readthedocs.io/en/latest/"
                "plugins/b607_start_process_with_partial_path.html"
            )
        }

    if test_id == "B603":
        return {
            "title": "Review subprocess arguments",
            "risk": (
                "Using shell=False reduces shell-injection risk, but "
                "arguments can still affect the executable's behavior."
            ),
            "recommendation": (
                "Use a trusted executable, validate arguments, and "
                "review whether untrusted input can influence the "
                "command's behavior."
            ),
            "secure_example": (
                "subprocess.run(\n"
                "    [trusted_executable_path, validated_argument],\n"
                "    check=True,\n"
                "    shell=False\n"
                ")"
            ),
            "reference": (
                "https://bandit.readthedocs.io/en/latest/"
                "plugins/b603_subprocess_without_shell_equals_true.html"
            )
        }

    return {
        "title": "Potential security issue",
        "risk": issue or "The scanner reported a potential issue.",
        "recommendation": (
            "Review the affected code, verify the risk, and test "
            "an appropriate fix before marking this finding resolved."
        ),
        "secure_example": (
            "No generic fix is available. Review the affected code "
            "and choose a fix appropriate to the issue."
        ),
        "reference": ""
    }
