
import json
from model.book import BookInfo
from search.memoryindex import MemoryIndex

def parse_and_build_memoryindex():
    """
    parse the document data.json and build the memory index
    """
    with open("data.json", "r") as fh:
        content = fh.read()
        data = json.loads(content)

    titles = data['titles']
    summaries = data['summaries']
    memoryindex = MemoryIndex(min_word_length=3)
    for index, title in enumerate(titles):
        summaryinfo = summaries[index]
        bookid = summaryinfo['id']
        summary = summaryinfo['summary']
        bookinfo = BookInfo(bookid, title, summary)
        memoryindex.index_words_inbook(bookinfo)

    return memoryindex