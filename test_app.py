
import io
import app as app_module


def test_home_page_loads():
    app_module.app.config["TESTING"] = True
    client = app_module.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Secure Code Review Assistant" in response.data


def test_rejects_non_python_file():
    app_module.app.config["TESTING"] = True
    client = app_module.app.test_client()

    response = client.post(
        "/",
        data={
            "code_file": (io.BytesIO(b"hello"), "notes.txt")
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Only .py files are supported." in response.data


def test_missing_file_is_handled():
    app_module.app.config["TESTING"] = True
    client = app_module.app.test_client()

    response = client.post(
        "/",
        data={},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Please select a Python file." in response.data


def test_report_download_without_scan():
    app_module.app.config["TESTING"] = True
    client = app_module.app.test_client()

    response = client.get("/download-report")

    assert response.status_code == 400
    assert b"Please scan a file first." in response.data

    
def test_successful_upload_and_report_download():
    app_module.app.config["TESTING"] = True
    client = app_module.app.test_client()

    response = client.post(
        "/",
        data={
            "code_file": (
                io.BytesIO(
                    b"import subprocess\n"
                    b"subprocess.call('echo hello', shell=True)\n"
                    b"password = 'admin123'\n"
),
"test_sample.py"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Download HTML Report" in response.data
    download_response = client.get("/download-report")

    assert download_response.status_code == 200
    assert b"test_sample.py" in download_response.data

