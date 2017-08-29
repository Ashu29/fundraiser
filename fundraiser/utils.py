import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['fundraiser/settings'])[0]
    except ImportError:
        default_django_settings_module = "fundraiser.settings.settings"
    else:
        default_django_settings_module = "fundraiser.settings.local"
        file_.close()
    return default_django_settings_module
