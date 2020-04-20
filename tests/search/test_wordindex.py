
import unittest
from search.wordindex import WordIndex

class TestWordIndex(unittest.TestCase):
    
    def test_operations(self):
        wordindex = WordIndex('something')
        with self.assertRaises(KeyError):
            wordindex.process_repeating_doc(1, 20)

        wordindex.process_new_doc(1, 10)
        self.assertTrue(1 in wordindex.docs_by_wordcount[1])
        wordindex.process_repeating_doc(1, 20)
        self.assertDictEqual(wordindex.docs_by_wordcount[1], {})
        self.assertTrue(2 in wordindex.docs_by_wordcount)
        self.assertTrue(1 in wordindex.docs_by_wordcount[2])
        self.assertTrue(1 in wordindex.wordpos_indoc)

        maxrepeat = wordindex.get_word_max_repeatcount()
        self.assertTrue(maxrepeat, 2)

        docslist = wordindex.get_docs_list(2)
        self.assertTrue(1 in docslist)

        position =  wordindex.wordpos_indoc[1]
        self.assertListEqual([10, 20], position.get_positions())
        

    
        
