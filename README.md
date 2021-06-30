# AutoCompletion using Flask, ElasticSearch

* Our goal is to design an AutoSuggestion and AutoCorrection system the same as Google search engine. 
For designing such system we are using tools like
  * ElasticSearch  for writing queries in backend 
  * Flask for generating an API 
  * AJAX and JQUERY for sending requests and getting data in the UI from backend
  
* Before Going to step1 we have stored the data in elastic search with the index name emp11.
**Step 1:**  First we need to write a query in backend using Elastic Search, for autosuggestion 
I used a prefix.
Using Flask I have generated an API for running the elasticsearch query in the backend.

**Step 2:** In the Frontend I have used Flask, Jquery and Ajax 
* In app1.py I have created a method inside the flask app in which i have given a url of the backend 
  along with a route for requesting data from the backend.
* Using Html first i have created a searchbox in the web UI for searching the data
  Using Jquery I wrote  a function and inside the function  there is a Ajax method in which 
  I have requested a method in app1.py using POST, Such that when the user types anything in the 
  searchbox in web UI then the Ajax will request the method in app1.py and fromapp1.py the POST request will send 
  to backend and it will collect the result and display the suggestion on the screen.


**Step 3:** In this step first we have to run the api.py for running backend query and afterthat 
run app1.py


**Output**
![Alt text](https://github.com/phani-1995/Elasticsearch_Autocompletion/blob/master/output/Screenshot%20from%202020-10-31%2016-09-53.png)
![Alt text](https://github.com/phani-1995/Elasticsearch_Autocompletion/blob/master/output/Screenshot%20from%202020-10-31%2016-09-53.png)


## References:
* https://blog.mimacom.com/autocomplete-elasticsearch-part1/
* https://www.elastic.co/guide/en/elasticsearch/reference








