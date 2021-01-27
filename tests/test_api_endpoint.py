from fastapi.testclient import TestClient

from ..bluestorm_app.main import app

client = TestClient(app)


def test_endpoint_status():
    response = client.get("/search/tylenol")
    assert response.status_code == 200


def test_endpoint_empty_list():
    response = client.get("/search/xxxyyy")
    assert response.status_code == 200


def test_endpoint_response():
    response = client.get("/search/pytest")

    medications = response.json()["medications"]

    medication_test = medications[0]

    assert response.status_code == 200
    assert medication_test["ingredients"][0]["name"] == "UREA, C-14"
    assert medication_test["dfs"][0]["method"] == "CAPSULE"
    assert medication_test["routes"][0]["method"] == "ORAL"
    assert medication_test["trade_names"][0]["name"] == "PYTEST"
    assert medication_test["applicants"][0]["name"] == "AVENT"
    assert medication_test["strengths"][0]["amount"] == "1uCi"
    assert medication_test["warning_messages"] == []