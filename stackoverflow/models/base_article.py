import datetime


class BaseArticle(object):
    def __init__(self, created_by, article_text):
        self.__created_by = created_by
        self.__article_text = article_text
        self.__votes = 0
        self.__created_time = datetime.datetime.now()
