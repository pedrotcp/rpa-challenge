from .reuters import ReutersSource
from .googlenews import GoogleNewsSource


def get_news_source(payload,headless):

    source = payload.get('news_source',None)

    if source == 'google_news' or source is None:
        return GoogleNewsSource(payload,headless=headless)
    if source == 'reuters':
        return ReutersSource(payload,headless=headless)
    else:
        raise ValueError(f"News suorce not implemented: {source}.")
        #Improvement: It would be nice to let user know which sources are available, via a report, or maybe e-mail
    