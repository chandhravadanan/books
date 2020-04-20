
import requests
from constants import AUTHOR_API_URL

class BookCache:
    """ 
        This will maintain id vs bookinfo in memory
        fetch authour name through api and update the book info when needed
    """
    bookinfo_byid = {}

    @staticmethod
    def get_bookinfo_byid(bookid):
        return BookCache.bookinfo_byid.get(bookid, None)

    @staticmethod
    def clear_bookinfo_byid(bookid):
        BookCache.bookinfo_byid.pop(bookid, None)

    @staticmethod
    def cache_bookinfo(bookinfo):
        bookid = bookinfo.get_bookid()
        BookCache.bookinfo_byid[bookid] = bookinfo

    @staticmethod
    def get_authorname_byapi(bookid):
        response = requests.post(AUTHOR_API_URL, json={'book_id': bookid})
        content = response.json()
        if 'author' in content:
            return content['author']

        return None

    @staticmethod
    def get_authorname_bybookid(bookid):
        bookinfo = BookCache.get_bookinfo_byid(bookid)
        if bookinfo is None:
            return None

        authorname = bookinfo.get_authorname()
        if authorname is not None:
            return authorname

        name = BookCache.get_authorname_byapi(bookid)
        bookinfo.set_authorname(name)
        return name