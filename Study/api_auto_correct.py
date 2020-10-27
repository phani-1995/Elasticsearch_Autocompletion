from flask import Flask
from flask_restful import Resource, Api, reqparse
from elasticsearch import Elasticsearch


app = Flask(__name__)
api = Api(app)

index_name = 'emp11'
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

class autocorrect(Resource):
    def __init__(self):
        self.query1 = parser.parse_args().get("query1", None)
        self.baseQuery = {
            "_source": [],
            "size": 0,
            "min_score": 0.5,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "County.keyword": {
                                    "query": "{}".format(self.query1),
                                    "fuzziness": "2"
                                }
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "auto_correct": {
                    "terms": {
                        "field": "County.keyword",
                        "order": {
                            "_count": "desc"
                        },
                        "size": 20
                    }
                }
            }
        }
    def get(self):
        res = es.search(index=index_name, size=0, body=self.baseQuery)
        return res


parser = reqparse.RequestParser()
parser.add_argument("query1", type=str, required=True, help="query parameter is Required ")
api.add_resource(autocorrect, '/autocorrect')

if __name__ == '__main__':
    app.run(debug=True, port=4001)

