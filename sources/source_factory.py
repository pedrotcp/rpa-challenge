from .latimes import LosAngelesTimesSource
from .googlenews import GoogleNewsSource


def get_news_source(payload,headless):

    source = payload.get('news_source',None)

    if source == 'la_times' or source is None:
        return LosAngelesTimesSource(payload,headless=headless)
    if source == 'google_news' :
        # return GoogleNewsSource(payload,headless=headless)
        raise ValueError(f"News source not fully implemented.")
    else:
        raise ValueError(f"News suorce not implemented: {source}.")
    