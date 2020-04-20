

import unittest
from model.book import BookInfo

class TestBookInfo(unittest.TestCase):

    def test_get_actual_content(self):
        expected = 'programming language'
        bookinfo = BookInfo(1, 'Python', expected)
        self.assertEqual(bookinfo.get_actual_content(), expected)
        summary = 'The Book in Three Sentences: programming language'
        bookinfo = BookInfo(1, 'Python', summary)
        self.assertEqual(bookinfo.get_actual_content(), ' '+expected)