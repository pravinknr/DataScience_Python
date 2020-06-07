# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:10:09 2020

@author: pravi
"""

# Import the Libraries
import pandas as pd

books = pd.read_csv("E:/Data Science/Assignment/Recommendation System/books.csv",header=0,encoding='ISO-8859-1',names=['unname','Users','book_title','book_author','publisher','ratings'])
books.head()
books.shape
books.columns

book1 = books.iloc[0:4000,1:]
book1.head()
# We will remove the Rows having Ratings as 0
book1 = book1[~(book1 == 0).any(axis=1)]
book1.head()

book1.book_title

book1.book_author

book1.publisher

from sklearn.feature_extraction.text import TfidfVectorizer

book1['book_author'].isnull().sum()
# we Dont have any Null Values in author column

# Creating a Tfidf Vectorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words="english")    #taking stop words from tfid vectorizer

tfidf_matrix = tfidf.fit_transform(book1.publisher)   #Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix.shape 

# Lets Find the Similarity Score
from sklearn.metrics.pairwise import linear_kernel
# Computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix,tfidf_matrix)

book1_index = pd.Series(book1.index,index=book1['book_title']).drop_duplicates()

book1_index['Clara Callan']

def get_book_recommendations(Name,topN):
    
   
    topN = 10
    # Getting the book index using its title 
    title_id = book1_index[Name]
    
    # Getting the pair wise similarity score for all the Books with that 
    # Book
    cosine_scores = list(enumerate(cosine_sim_matrix[title_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores,key=lambda x:x[1],reverse = True)
    
    # Get the scores of top 10 most similar Books 
    cosine_scores_10 = cosine_scores[0:topN+1]
    
    # Getting the Book index 
    book1_idx  =  [i[0] for i in cosine_scores_10]
    book1_scores =  [i[1] for i in cosine_scores_10]
    
    # Similar Books and scores
    book_similar_show = pd.DataFrame(columns=["name","Score"])
    book_similar_show["name"] = book1.loc[book1_idx,"book_title"]
    book_similar_show["Score"] = book1_scores
    book_similar_show.reset_index(inplace=True)  
    book_similar_show.drop(["index"],axis=1,inplace=True)
    print (book_similar_show)
    

get_book_recommendations("PLEADING GUILTY",topN=15) # The Recommendations is Based on the Publisher
# So we can Recommend the book "My Father, Dancing(Harvest Book) to the Users based on Publsher of Pleading Guilty

get_book_recommendations("Clara Callan",topN=15)
# we recommend Books Ralph S. Mouse and 3 more to the Users based on the Publisher of Clara Callan