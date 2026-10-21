
import os
from scanner import scan_file
from explainer import explain_finding


def review_file(file_path, original_filename=None):
    scan_result = scan_file(file_path)

    if not scan_result["success"]:
        return {
            "success": False,
            "error": scan_result["error"],
            "findings": []
        }

    reviewed_findings = []

    for finding in scan_result["findings"]:
        explanation = explain_finding(finding)

        reviewed_findings.append({
            "issue": finding.get("issue_text", ""),
            "severity": finding.get("issue_severity", "UNKNOWN"),
            "confidence": finding.get("issue_confidence", "UNKNOWN"),
            "file": original_filename or os.path.basename(
                finding.get("filename", file_path)
            ),
            "line": finding.get("line_number", 0),
            "test_id": finding.get("test_id", ""),
            "cwe": finding.get("issue_cwe"),
           "title": explanation["title"],
           "risk": explanation["risk"],
           "recommendation": explanation["recommendation"],
           "secure_example": explanation.get("secure_example", ""),
           "reference": explanation["reference"]
        })

    return {
        "success": True,
        "error": None,
        "findings": reviewed_findings
    }
