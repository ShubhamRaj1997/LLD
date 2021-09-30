import datetime

from stackoverflow.models.base_article import BaseArticle


class Answer(BaseArticle):
    def __init__(self, answer_text, created_by):
        super(Answer, self).__init__(created_by, answer_text)
        self.__accepted = False
        self.__vote = 0
        self.__creation_time = datetime.datetime.now()
        self.__comments = []


class AnswerV2():
    def __init__(self, answer_text, created_by):
        self.__base_article = BaseArticle(created_by, answer_text)
        self.__accepted = False
        self.__vote = 0
        self.__creation_time = datetime.datetime.now()
        self.__comments = []

# observer that we have common entities between answer, Question and comments
# all of these have created_time, created_by, votes
# so we can make use of composition
# I have used inheritence first then we can check same with  composition (check v2)
