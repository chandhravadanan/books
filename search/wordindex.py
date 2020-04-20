
from .positions import WordPositions

class WordIndex:
    """
    context maintained between specific word and relevant docs

    specific word positions in the document maintained 
    and this can be used for proximity search (Not done)
    {
        <doc-id1> : [10, 20, 30]
        <doc-id2> : [20, 55]
    }

    another map maintains words counts vs word positions 
    which documents contains most matching word can be obtained in O(1)
    {
        3 : { <doc-id1> : [10, 20, 30], ...}
        2 : { <doc-id2> : [20, 55], ...}
    }
    """
    def __init__(self, word):
        self.word = word
        self.wordpos_indoc = {}
        self.docs_by_wordcount = {}

    def process_repeating_doc(self, docid, pos):
        pos_list_obj = self.wordpos_indoc[docid]
        self.remove_docs_bycount_entry(docid, pos_list_obj)
        pos_list_obj.append(pos)
        self.add_docs_bycount_entry(docid, pos_list_obj)

    def process_new_doc(self, docid, pos):
        pos_list_obj = WordPositions(pos)
        self.wordpos_indoc[docid] = pos_list_obj
        self.add_docs_bycount_entry(docid, pos_list_obj)

    def remove_docs_bycount_entry(self, docid, pos_list_obj):
        count = pos_list_obj.word_count()
        docs_info = self.docs_by_wordcount[count]
        docs_info.pop(docid, None)

    def add_docs_bycount_entry(self, docid, pos_list_obj):
        count = pos_list_obj.word_count()
        if count not in self.docs_by_wordcount:
            self.docs_by_wordcount[count] = {}

        docs_info = self.docs_by_wordcount[count]
        docs_info[docid] =  pos_list_obj
        

    def push(self, docid, pos):
        if docid in self.wordpos_indoc:
            self.process_repeating_doc(docid, pos)
        else:
            self.process_new_doc(docid, pos)

    def get_word_max_repeatcount(self):
        return len(self.docs_by_wordcount)

    def get_docs_list(self, repeating_count):
        docs_info = self.docs_by_wordcount.get(repeating_count, {})
        return docs_info.keys()

