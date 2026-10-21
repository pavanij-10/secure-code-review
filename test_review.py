
from review import review_file


def test_review_returns_explanations():
    result = review_file("sample_vulnerable.py")

    assert result["success"] is True
    assert len(result["findings"]) >= 1

    for finding in result["findings"]:
        assert "title" in finding
        assert "risk" in finding
        assert "recommendation" in finding


def test_review_rejects_missing_file():
    result = review_file("missing_sample.py")

    assert result["success"] is False
    assert result["findings"] == []
