import datetime

from stackoverflow.models.base_article import BaseArticle


class Question(BaseArticle):
    def __init__(self, title: str, description: str, created_by: str):
        super(Question, self).__init__(title, created_by)
        self.description = description
        self.__creation_time = datetime.datetime.now()
        self.__comments = []
        self.__answers = []
        self.__tags = []
        self.__bounty = None

    @property
    def answers(self):
        return self.__answers

    def add_answer(self, answer):
        self.answers.append(answer)

    def remove_answer(self, answer):
        self.answers.remove(answer)

    @property
    def comments(self):
        return self.__comments

    def add_comments(self, comment):
        self.comments.append(comment)

    def remove_comment(self, comment):
        self.comments.remove(comment)

    @property
    def tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    # other functions,
    #

    # similarly for tags, comments you can add


class QuestionV2(object):
    def __init__(self, title: str, description: str, created_by: str):
        self.__base_article = BaseArticle(created_by, title)
        self.description = description
        self.__creation_time = datetime.datetime.now()
        self.__comments = []
        self.__answers = []
        self.__tags = []
        self.__bounty = None

    @property
    def answers(self):
        return self.__answers

    def add_answer(self, answer):
        self.answers.append(answer)

    def remove_answer(self, answer):
        self.answers.remove(answer)

    @property
    def comments(self):
        return self.__comments

    def add_comments(self, comment):
        self.comments.append(comment)

    def remove_comment(self, comment):
        self.comments.remove(comment)

    @property
    def tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    # other functions,
    #

    # similarly for tags, comments you can add
