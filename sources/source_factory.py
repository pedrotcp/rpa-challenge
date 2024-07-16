from .latimes import LosAngelesTimesSource
from .googlenews import GoogleNewsSource


def get_news_source(payload,headless):

    source = payload.get('news_source',None)

    if source == 'google_news' or source is None:
        return GoogleNewsSource(payload,headless=headless)
    if source == 'la_times':
        return LosAngelesTimesSource(payload,headless=headless)
    else:
        raise ValueError(f"News suorce not implemented: {source}.")
    