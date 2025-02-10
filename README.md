# Movie reccomendor system

# Overview:
This is a website that suggests movies to users based on their likings. It is based on Machine Learning algorithms that personalize choices of the user.

# Features:

Content-Based Filtering: Recommends movies based on similarities in genres, actors, and other metadata.

Collaborative Filtering: Suggests movies based on user behavior and preferences.

User Interface: Simple and interactive UI for searching and receiving recommendations.

User Login and password encryption: Uses hashing techniques to further safeguard passwords

Database Integration: Uses a dataset of movies, ratings, and user preferences.


# Dataset:
 Dataset consists of Movies with information like cast,crew,genres.
 It also has ratings of users for movies of the database

# Technologies used:
 Programming Language: Python
 Libraries: Pandas, NumPy, Scikit-learn, nltk,Streamlit,bcrypt,pickle
 Database:Json file

# The Model:
 1.Cleaning the dataframe as per need,merging information of the film into a column called tags.
 
 2. Use of text vectorisation to find similar movies based on content and predicting top 5 flims related to the query.
  
 3. Creation of user matrix as per reviews provided by the viewer.
  
 4. Use of Kmeans algorithm to categorize users into groups based on their preferences and then suggest movies.
     

 # Frontend:
 Use of Streamlit library to host the website and create a password protection for the website.
 Using tdmb API token to fetch the poster of the movie

 # Result:
 Optimized K parameter for the model
 ![image](https://github.com/user-attachments/assets/fce8b560-fbce-4cff-9e50-541fb5aaf50f)

 

 ![image](https://github.com/user-attachments/assets/c65a0ab9-a7cf-4c58-813a-b1681c5114a7)
 ![image](https://github.com/user-attachments/assets/b47f5ee3-20af-4bcb-8982-90a9cfa609b9)
 ![image](https://github.com/user-attachments/assets/8d7b603d-b736-4487-8785-3d4bcd4dba8d)


 
 
 
# Mock run instrunctions:
The "login.py" auto downloads all pickle files required for the website.
To access one can either register or use existing users:
                id:2 and password:hi
                id:1 and password:n

Pickle file uploaded :"https://drive.google.com/file/d/1POu4NYaDFTrizqjfRIsIfUQ9klA6CmUk/view?usp=sharing"
