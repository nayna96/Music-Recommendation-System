# Music-Recommendation-System

The volume of data has been increasing in the past years. It is often difficult to sift through the variety and identify the things the users would like. Therefore, effective techniques are needed to handle the large amount of data generated daily and provide recommendation to the users. 

Recommendations help these services solve the problem of discovery by helping user navigate the maze of the catalogues to find what they are looking for but don’t know of. Recommendation systems take data such as what users bought, what users browsed, what users rated as input to the recommendation engine and give top picks for you as the desired output. Recommendation engine predicts the rating a user would give to a product, whether a user would buy a product and filters relevant products to the user. 

Collaborative filtering is a general term for any algorithm used by most recommendation engines. Collaborative filtering relies only on user behavior (history, ratings, similar users etc) and normally predicts users ratings for products they haven’t yet rated. Latent factor analysis is one of the algorithm to perform collaborative filtering. It identifies hidden factors that influence a user’s rating by a user-product rating matrix. It represents users by their ratings for different products. 

This paper is a framework for recommending music artist for a particular by using Alternating Least Squares (ALS) method of Sparks MLlib. Alternating least squares (ALS) is used to solve the equations in user-product rating matrix. 

Spark's MLlib has a built-in module for recommendation system that performs machine learning algorithms. It has built in functionality for applying ALS on any user-product-rating matrix. 

MLlib abstracts the programmer from the technical implementation details of ALS algorithm and running it across the cluster. Since Sparks RDDs are in-memory it can make multiple passes over the same data without doing disk writes.
