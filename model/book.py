
from constants import SUMMARY_PREFIX

class BookInfo:
    """ model object for book """

    def __init__(self, bookid, title, summary):
        self.bookid = bookid
        self.title = title
        self.summary = summary
        self.author = None

    def get_bookid(self):
        return self.bookid

    def get_title(self):
        return self.title

    def get_summary(self):
        return self.summary

    def get_authorname(self):
        return self.author

    def set_authorname(self, name):
        self.author = name

    def get_actual_content(self):
        """ summary prefix omitted for word index"""
        actual = self.summary.split(SUMMARY_PREFIX, 1)
        if len(actual)>1:
            return actual[1]

        return actual[0]