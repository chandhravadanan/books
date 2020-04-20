
import unittest
from search.memoryindex import MemoryIndex
from model.book import BookInfo

class TestMemoryIndex(unittest.TestCase):

    def test_check_and_omit_separator(self):
        memoryindex = MemoryIndex()
        expected = memoryindex.check_and_omit_separator('sample')
        self.assertEqual(expected, 'sample')
        expected = memoryindex.check_and_omit_separator('sample.')
        self.assertEqual(expected, 'sample')
        expected = memoryindex.check_and_omit_separator('sample,')
        self.assertEqual(expected, 'sample')
        expected = memoryindex.check_and_omit_separator('sample)')
        self.assertEqual(expected, 'sample')
        expected = memoryindex.check_and_omit_separator('(sample)')
        self.assertEqual(expected, 'sample')
        memoryindex = MemoryIndex(separators=True)
        expected = memoryindex.check_and_omit_separator('sample.')
        self.assertEqual(expected, 'sample.')

    def test_index_word(self):
        memoryindex = MemoryIndex()
        self.assertTrue(len(memoryindex.word_indexed_data)==0)
        memoryindex.index_word(1, 'something', 4)
        self.assertTrue('something' in memoryindex.word_indexed_data)
        wordindex = memoryindex.word_indexed_data['something']
        self.assertTrue(wordindex.word, 'something')

    def test_index_words_inbook(self):
        bookinfo = BookInfo(1, 'Django', 'Web framework')
        memoryindex = MemoryIndex()
        memoryindex.index_words_inbook(bookinfo)
        self.assertTrue('web' in memoryindex.word_indexed_data)
        self.assertTrue('framework' in memoryindex.word_indexed_data)
        memoryindex = MemoryIndex(min_word_length=4)
        memoryindex.index_words_inbook(bookinfo)
        self.assertTrue('web' not in memoryindex.word_indexed_data)
        self.assertTrue('framework' in memoryindex.word_indexed_data)

    def test_get_matched_docs(self):
        bookinfo = BookInfo(1, 'Django', 'Web framework')
        memoryindex = MemoryIndex()
        memoryindex.index_words_inbook(bookinfo)
        results = memoryindex.get_matched_docs('Web')
        self.assertSetEqual(results, {1})
        results = memoryindex.get_matched_docs('None')
        self.assertSetEqual(results, set())

    def test_search(self):
        bookinfo = BookInfo(1, 'Django', 'Web framework')
        memoryindex = MemoryIndex()
        memoryindex.index_words_inbook(bookinfo)
        self.assertListEqual(memoryindex.search('Web', 0), [])
        self.assertListEqual(memoryindex.search('None', 1), [])
        results = memoryindex.search('Web', 1)
        self.assertListEqual(results, [{'summary':'Web framework', 'id':1}])


