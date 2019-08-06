from src.tools import dtloader
from src import settings


class APIEndpoint:
    API_DIRECTIVES = './directives/api_info.json'
    URL_KEY = 'api_url'
    VERSION_KEY = 'latest_version'
    RELEASE_KEY = 'latest_release'
    LANG_KEY = 'lang'
    ALL_CARDS_KEY = 'all_cards'
    COLLECTIBLE_CARDS_KEY = 'collectible_cards'

    def __init__(self, all_cards=False):
        self.api_url = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES, APIEndpoint.URL_KEY)
        self.lts_version = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES,
                                              APIEndpoint.VERSION_KEY)
        self.lts_release = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES,
                                              APIEndpoint.RELEASE_KEY)
        self.lang = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES, APIEndpoint.LANG_KEY)

        if all_cards:
            self.cards = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES,
                                            APIEndpoint.ALL_CARDS_KEY)
        else:
            self.cards = dtloader.read_json(settings.PROJECT_ROOT, APIEndpoint.API_DIRECTIVES,
                                            APIEndpoint.COLLECTIBLE_CARDS_KEY)

    @property
    def request_url(self):
        return '{api_url}{version}{release}{lang}{cards}'.format(api_url=self.api_url,
                                                                 version=self.lts_version,
                                                                 release=self.lts_release,
                                                                 lang=self.lang,
                                                                 cards=self.cards)
