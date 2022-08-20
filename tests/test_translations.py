def test_translations():
    '''Checks if all translations have the same length as the main english translations.'''
    import yaml
    import os
    from solipsist.utils import resource_path

    with open(resource_path("translations/en.yml")) as f:
        en = yaml.safe_load(f)

    all_languages = os.listdir("translations/")
    for language in all_languages:
        with open(resource_path(f"translations/{language}")) as f:
            lang = yaml.safe_load(f)
            assert len(lang) == len(en)
