from stackoverflow.models.base_article import BaseArticle


class Comment(BaseArticle):
    def __init__(self, comment_text, created_by):
        super(Comment, self).__init__(comment_text, created_by)


class CommentV2(object):
    def __init__(self, comment_text, created_by):
        self.__base_article = BaseArticle(comment_text, created_by)

