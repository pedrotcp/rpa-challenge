from .reuters import ReutersSource
from .googlenews import GoogleNewsSource


def get_news_source(source_name = "google_news"):

    if source_name == 'google_news':
        return GoogleNewsSource()
    if source_name == 'reuters':
        return ReutersSource()
    else:
        raise ValueError(f"News sorce not implemented: {source_name}.")
        #Add some logic to let user know which sources are available, via a report, or maybe e-mail
    