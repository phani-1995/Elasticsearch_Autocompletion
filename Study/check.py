from elasticsearch import Elasticsearch

index_name = 'emp11'
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# query = {
#     "_source": [],
#     "size": 0,
#     "min_score": 0.5,
#     "query": {
#         "bool": {
#             "should": [
#                 {
#                     "match": {
#                         "County.keyword": {
#                             "query": "New yark",
#                             "fuzziness": "2"
#                         }
#                     }
#                 }
#             ]
#         }
#     },
#     "aggs": {
#         "auto_correct": {
#             "terms": {
#                 "field": "County.keyword",
#                 "order": {
#                     "_count": "desc"
#                 },
#                 "size":20
#             }
#         }
#     }
# }
query = {
  "query" : {
    "multi_match" : {
        "query" : "New Yark",
        "fields" : ["County"],
        "type" : "best_fields",
        "tie_breaker" : 0.8,
        "fuzziness": 2
    },
  }
}

print(es.search(index=index_name, body=query))


