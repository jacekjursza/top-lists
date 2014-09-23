
list = {
    'imdb_higest_scifi_tv_series': {
        'entity': 'tv_series',
        'description': 'Highest Rated Sci-Fi TV Series With At Least 1,000 Votes',
        'url': 'http://www.imdb.com/search/title?genres=sci_fi&num_votes=1000,&sort=user_rating&desc&'
               'start=%(start)s&title_type=tv_series',
        'xpath': '//*[@id="main"]/table/tr[*]/td[3]/a',
        'per_page': 50,
        'sub_pages': 7
    }
}