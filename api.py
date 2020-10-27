from flask import Flask
from flask_restful import Resource, Api, reqparse
from elasticsearch import Elasticsearch


app = Flask(__name__)
api = Api(app)

index_name = 'emp11'
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

class employee(Resource):
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        self.baseQuery = {
            "_source": [],
            "size": 0,
            "min_score": 0.5,
            "query": {
                "bool": {
                    "should": [
                        {
                            "prefix": {
                                "County.keyword": {
                                    "value":"{}".format(self.query)
                                }
                            }
                        },
                        {
                            "fuzzy": {
                                "County.keyword": {
                                    "value":"{}*".format(self.query),
                                    "fuzziness": "2"
                                }
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "auto_complete": {
                    "terms": {
                        "field": "County.keyword",
                        "order": {
                            "_count": "desc"
                        },
                        "size": 25
                    }
                }
            }
        }

    def get(self):
        res = es.search(index=index_name, size=0, body=self.baseQuery)
        return res


parser = reqparse.RequestParser()
parser.add_argument("query", type=str, required=True, help="query parameter is Required ")
api.add_resource(employee, '/autocomplete')

if __name__ == '__main__':
    app.run(debug=True, port=4000)

