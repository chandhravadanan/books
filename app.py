
from flask import Flask, request, Response
from parser import parse_and_build_memoryindex
from cache.book import BookCache
import json

app = Flask(__name__)
memory_index = parse_and_build_memoryindex()

@app.route("/search", methods=["GET"])
def search_books():
    """
    comma separted queries splitted and performed search using memory index
    """
    queries = request.args.get('queries', default = '', type = str)
    limit = request.args.get('limit', default = 3 , type = int)
    
    results = []
    for eachquery in queries.split(','):
        matches = memory_index.search(eachquery, limit)
        for eachbook in matches:
            bookid = eachbook['id']
            eachbook['query'] = eachquery
            eachbook['author'] = BookCache.get_authorname_bybookid(bookid)
        
        results.append(matches)

    return Response(json.dumps(results),  mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=8888)