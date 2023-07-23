# Search Engine 

The Marvel Wikipedia Search Engine is a keyword-based search application that utilizes Elasticsearch to perform lightning-fast searches on a collection of over 8800 Wikipedia articles linked to Marvel. It employs the BM25 and TF-IDF models for ranking, ensuring that relevant material is prioritized and presented to users in under two seconds. The application is built with Flask, offering a user-friendly web interface for seamless access.

### Features

Utilizes Elasticsearch for efficient keyword-based search on a vast collection of Marvel-related Wikipedia articles.

Implements BM25 and TF-IDF ranking models to ensure accurate and relevant search results.

Performs extensive data preprocessing, including stop word removal, lemmatization, and stemming, to enhance search accuracy.

### How to Run the Project
To run the Marvel Wikipedia Search Engine locally on your machine, follow these steps:
1. Download [dataset](https://bitbucket.org/dalvimangesh000/ir-project/src/%27main%27/) **or** scrap data using Web_scrapping.ipynb
2. Ensure that you have Elasticsearch 7.x installed and running on your system. You can download Elasticsearch from the official website (https://www.elastic.co/downloads/elasticsearch) and follow the installation instructions.
3. For preprocessing data and creating index

        python final.py 
      
5. Running the Flask Web App
   
        python main.py
   
6. Once the server is running, open your web browser and navigate to http://localhost:5000 to access the Marvel Wikipedia Search Engine. You can enter your search queries and explore the prioritized search results.
