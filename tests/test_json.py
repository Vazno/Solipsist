import json


def test_stats():
    from solipsist.utils import resource_path

    with open(resource_path("settings.json")) as f:
        test_j = json.load(f)

    assert (test_j["stats"]["CLICKS"] == 0) is True
    assert (test_j["stats"]["TIME_PLAYED"] == 0) is True
    assert (test_j["stats"]["BEST_RECORD"] == 0) is True

def test_themes():
    from solipsist.utils import resource_path
    with open(resource_path("settings.json")) as f:
        test_j = json.load(f)
    max_theme_num = test_j["graphic"]["max_theme"]+1 # Non programmic indexing
    assert len(test_j["graphic"]["FONT_COLOR"]) == max_theme_num
    assert len(test_j["graphic"]["PLAYER_COLOR"]) == max_theme_num
    assert len(test_j["graphic"]["BACKGROUND"]) == max_theme_num
    assert len(test_j["graphic"]["OBSTACLE_COLOR"]) == max_theme_num
    assert len(test_j["graphic"]["InputBox"]["COLOR_ACTIVE"]) == max_theme_num
    assert len(test_j["graphic"]["InputBox"]["COLOR_INACTIVE"]) == max_theme_num

def test_music():
    from solipsist.utils import resource_path
    with open(resource_path("settings.json")) as f:
        test_j = json.load(f)
    assert test_j["music"]["VOLUME"] <= 1
    assert test_j["music"]["EFFECT_VOLUME"] <= 1