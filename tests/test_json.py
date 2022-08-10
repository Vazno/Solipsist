import json


def test_json():
    from utils import resource_path

    with open(resource_path("settings.json")) as f:
        test_j = json.load(f)

    assert (test_j["stats"]["CLICKS"] == 0) is True
    assert (test_j["stats"]["TIME_PLAYED"] == 0) is True
    assert (test_j["stats"]["BEST_RECORD"] == 0) is True
