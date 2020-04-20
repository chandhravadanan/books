

Install the dependency using requirements.txt

> pip install -r requirements.txt


Note : Flask and Requests packages are the only dependencies.

Run unittest

> python -m unittest -v

Run application

> python app.py

Memory Index API:

> from search.memoryindex import MemoryIndex
> 
> from model.book import BookInfo
> 
>   
> 
> memoryindex = MemoryIndex(min_word_length=3)
> 
> bookinfo = BookInfo(bookid, title, summary)
> 
> memoryindex.index_words_inbook(bookinfo)
> 
> // each every unique word is indexed to find relevant books
> 
>   
> 
> matches = memoryindex.search('is your problems', 3)
> 
>   
> 
> // matches format [ { 'summary' : book-summary, 'id' : book-id},
> ... ]

  

API to search books using queries

> /search?queries=<csv>&limit=<int>
> 
>   
> 
> eg.
> 
> /search?queries=problems,your&limit=1
