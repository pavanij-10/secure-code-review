
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from io import BytesIO

from flask import Flask, request, render_template, send_file, session
from review import review_file
from report import generate_html_report

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024
app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "local-development-key-change-before-deployment"
)
@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        findings=[],
        error="File is too large. Maximum upload size is 1 MB."
    ), 413

@app.route("/", methods=["GET", "POST"])
def index():
    findings = []
    error = None

    if request.method == "POST":
        uploaded_file = request.files.get("code_file")

        if not uploaded_file or not uploaded_file.filename:
            error = "Please select a Python file."

        elif Path(uploaded_file.filename).suffix.lower() != ".py":
            error = "Only .py files are supported."

        else:
            original_filename = Path(uploaded_file.filename).name

            with TemporaryDirectory() as temp_dir:
                file_path = Path(temp_dir) / "uploaded_code.py"
                uploaded_file.save(file_path)

                result = review_file(
                    file_path,
                    original_filename=original_filename
                )

                if not result["success"]:
                    error = result["error"]

                else:
                    findings = result["findings"]
                    report_file = Path(temp_dir) / "security_report.html"

                    generate_html_report(result, report_file)

                    session["report_html"] = report_file.read_text(
                        encoding="utf-8"
                    )

    return render_template(
        "index.html",
        findings=findings,
        error=error
    )


@app.route("/download-report")
def download_report():
    report_html = session.get("report_html")

    if not report_html:
        return "Please scan a file first.", 400

    return send_file(
        BytesIO(report_html.encode("utf-8")),
        mimetype="text/html",
        as_attachment=True,
        download_name="security_report.html"
    )


if __name__ == "__main__":
    app.run(debug=True)

 