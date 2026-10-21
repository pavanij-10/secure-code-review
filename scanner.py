import json
import subprocess
import sys
from pathlib import Path

def scan_file(file_path):
    path = Path(file_path).resolve()

    if not path.is_file() or path.suffix != ".py":
        return {
            "success": False,
            "findings": [],
            "error": "Please provide an existing Python file."
        }

    try:
        result = subprocess.run(
            [sys.executable, "-m", "bandit", "-f", "json", str(path)],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode not in (0, 1):
            return {
                "success": False,
                "findings": [],
                "error": result.stderr.strip() or "The scan failed."
            }

        report = json.loads(result.stdout)

        return {
            "success": True,
            "findings": report.get("results", []),
            "metrics": report.get("metrics", {}),
            "error": None
        }

    except subprocess.TimeoutExpired:
        return {"success": False, "findings": [], "error": "Scan timed out."}
    except (json.JSONDecodeError, OSError) as error:
        return {"success": False, "findings": [], "error": str(error)}
