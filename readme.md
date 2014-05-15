The academic project

language: python

API : google customer search api for python 

Goal: 
+ to abstract meaning of user input and expend input
+ pass the input to google 
+ return the summary of search. Search execute by google  


Query area:
+ Health
  + 50 documents  
+ Global Warming
  + 49 documents 
+ NLP
  + 50 documents 

Query expansion method: 
+  using synonym of non STOP word in query to expand query
+  query classify to one of the three cartgories (NLP,Healt,Global Warming)
  + The classifier is per-calculated 

The algorithm for summary :
+ tf-idf
+ idf = log(total documents / 1+ number of document contain the word)
+ the documents for training idf got from websites(web crawling) and storage in training folder
+ tf = 0.5 + (0.5 *word frequency/ document words count)
+ tf-idf socre = tf * idf
+ if the word is in the query or expanded query, its score would be increase 5%
+ sentence wieght = sum of tf-idf score of all the word in the sentence / number of words in the sentence
+ the return summary is the two have the highest wieght sentence



The Project requirment: 

web application: a web page for submitting serch queries and display results. This page should be hosted on a server,
either local or on the web. It should have the functionality of submitting the search query to the service for getting
search results and annotating with snippets and getting results from this service. the web application can be 
implemented in any language.
Snippet generating service will consist of three parts:document retrieval service,document analysis service , 
and snippet delivery service. The document retrieval service will accept search query requests,make calls to Google or 
Bing API, retrieve line from the API, and retrieve the documents that these line point to. The document analysis service
will analyze there documents to generate snippets.


+ User query:
"the top 10 climate change effect"
+ Link:
http://www.discovery.com/tv-shows/curiosity/topics/worst-effects-global-warming.htm

Result from project:
+ Summary :
  Extreme weather can create extreme financial setbacks. Governments suffer the consequences of diminished tourism and industrial profits, soaring energy, food and water demands, disaster cleanup and border tensions.And ignoring ...


Result from Google:
+ Summary :
  In this article, we'll look at 10 of the worst effects of climate change, including some immediate effects observed and some hypothesized ...







