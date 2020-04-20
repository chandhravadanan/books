
from .wordindex import WordIndex
from cache.book import BookCache

class MemoryIndex:
    """
    Each unique word stored in dictionary that points to relevant docs
    {
        'word1' : <WordIndexobject1>,
        'word2' : <WordIndexobject2>,
        ....
    }
    """

    def __init__(self, min_word_length=1, separators=False, ignorecase=True):
        """ 
        min word length used skip small words from indexing
        separators like .,)] can be omitted before indexing
        ignorecase used to skip case sense
        """
        self.word_indexed_data = {}
        self.include_separators = separators
        self.ignorecase = ignorecase
        self.min_word_length = min_word_length

    def index_word(self, bookid, word, pos):
        if word not in self.word_indexed_data:
            self.word_indexed_data[word] = WordIndex(word)

        wordindex = self.word_indexed_data[word]
        wordindex.push(bookid, pos)

    def check_and_omit_separator(self, word):
        if self.ignorecase:
            word = word.lower()

        if self.include_separators is True:
            return word

        lastch = word[len(word)-1]
        if lastch in ['.', ',', ')', ']', ':']:
            word = word[:-1]

        firstch = word[0]
        if firstch in ['(', '[']:
            word = word[1:]

        return word

    def index_words_inbook(self, bookinfo):
        bookid = bookinfo.get_bookid()
        sentence = bookinfo.get_actual_content()
        sentence = bookinfo.get_title() + ' ' + sentence
        words = sentence.split()
        cur_pos = 0
        for word in words:
            word = self.check_and_omit_separator(word)
            if len(word) < self.min_word_length:
                continue

            self.index_word(bookid, word, cur_pos)
            cur_pos += len(word)

        BookCache.cache_bookinfo(bookinfo)
    
    def get_matched_docs(self, word):
        matched_docs = set()
        word = self.check_and_omit_separator(word)
        if word in self.word_indexed_data:
            wordindex = self.word_indexed_data[word]
            max_repeated_count = wordindex.get_word_max_repeatcount()
            for index in range(max_repeated_count, 0, -1):
                matched_docs.update(wordindex.get_docs_list(index))

        return matched_docs

    def search(self, query, limit):
        """
        search query splitted by words and ordered by word length from high to low
        and try to find matched documents upto given limit
        """
        if limit<=0:
            return[]

        matched_docs = set()
        search_words = query.split()
        searchwords_bysize = sorted(search_words, key=len, reverse=True)
        for each in searchwords_bysize:
            matched_docs.update(self.get_matched_docs(each))
            if(len(matched_docs)> limit):
                break
        
        results = []
        for index, bookid in enumerate(matched_docs):
            if index>=limit:
                break
        
            bookinfo = BookCache.get_bookinfo_byid(bookid)
            summary = bookinfo.get_summary()
            results.append({'summary':summary, 'id':bookid})

        return results


