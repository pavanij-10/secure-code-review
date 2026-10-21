
from review import review_file
from report import generate_html_report


result = review_file("sample_vulnerable.py")

if not result["success"]:
    print("Review failed:", result["error"])
else:
    print("Review completed!")
    print("Findings:", len(result["findings"]))

    report_path = generate_html_report(result)

    print("HTML report saved to:", report_path)
