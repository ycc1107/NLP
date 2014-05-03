The academic project

language: python

API : google customer search api for python 

Goal: 
+ to abstract meaning of user input and expend input
+ pass the input to google 
+ return the summary of search. Search execute by google  


Query area:
+ Health
  + 35 documents  
+ Global Warming
  + 40 documents 
+ NLP
  + 30 documents 

Query expansion method: 

The algorithm for summary :
+ tf-idf
+ idf = log(number documents / number of document contain the word)
+ the documents for training idf got from websites(web crawling) and storage in training folder
+ tf = the number of the word appear in document / the number of the words in document (the document is for summary)
+ tf-idf socre = tf * idf
+ sentence weigth = sum of tf-idf socre of all the word in the sentence / number of words in the sentence
+ the return summary is the two have the highest weigth sentence



The Project requirment: 

web application: a web page for submitting serch queries and display results. This page should be hosted on a server,
either local or on the web. It should have the functionality of submitting the search query to the service for getting
search results and annotating with snippets and getting results from this service. the web application can be 
implemented in any language.

Snippet generating service will consist of three parts:document retrieval service,document analysis service , 
and snippet delivery service. The document retrieval service will accept search query requests,make calls to Google or 
Bing API, retrieve line from the API, and retrieve the documents that these line point to. The document analysis service 
will analyze there documents to generate snippets.
