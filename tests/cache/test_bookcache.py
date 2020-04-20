
import unittest
from model.book import BookInfo
from cache.book import BookCache

class TestBookCache(unittest.TestCase):

    def test_get_bookinfo_byid(self):
        bookinfo = BookCache.get_bookinfo_byid(1)
        self.assertEqual(bookinfo, None)
        bookinfo = BookInfo(1, 'Flask', 'Web framework')
        BookCache.cache_bookinfo(bookinfo)
        expected = BookCache.get_bookinfo_byid(1)
        self.assertEqual(expected, bookinfo)

    def test_get_authorname_bybookid(self):
        authorname = BookCache.get_authorname_bybookid(0)
        self.assertEqual(authorname, None)
        bookinfo = BookInfo(0, 'Flask', 'Web framework')
        bookinfo.set_authorname('random')
        BookCache.cache_bookinfo(bookinfo)
        expected = BookCache.get_authorname_bybookid(0)
        self.assertEqual(expected, 'random')

    def test_clear_bookinfo_byid(self):
        BookCache.clear_bookinfo_byid(3)
        bookinfo = BookInfo(3, 'Flask', 'Web framework')
        BookCache.cache_bookinfo(bookinfo)
        expected = BookCache.get_bookinfo_byid(3)
        self.assertEqual(expected, bookinfo)
        BookCache.clear_bookinfo_byid(3)
        bookinfo = BookCache.get_bookinfo_byid(3)
        self.assertEqual(bookinfo, None)

    