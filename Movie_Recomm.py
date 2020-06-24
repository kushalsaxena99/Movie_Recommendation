import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import*
root = Tk()
root.geometry("1366x768+0+0")
root.title("Blood group")
root.resizable(0, 0)
df = pd.read_csv("movie_dataset.csv")


def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:", row)	



def S():
    frame2 = Frame(root, width=1366, height=900)
    frame2.place(x=0, y=0)
    Label(frame2, width="1366", height="768").place(x=0, y=100)
    Entry(frame2,width=100).pack(side=TOP,padx=100,pady=50)
    
    b1=Button(frame2, text='SEARCH',command=lambda: PrintFrame(frame2, root))
    b1.place( relx = 0.5, rely = 0.15, anchor = CENTER)
    frame2.pack(fill=BOTH, expand=YES)
    frame2.mainloop()

def PrintFrame(frame2,root):
    label = Label(frame2, text=str(hello(frame2,root)))
    label.pack()
    
l=[]

def hello(frame2,root):
    #print df.columns
    ##Step 2: Select Features
    features = ['keywords','cast','genres','director']
    ##Step 3: Create a column in DF which combines all selected features
    for feature in features:
        df[feature] = df[feature].fillna('')
    df["combined_features"] = df.apply(combine_features,axis=1)
    
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])

    ##Step 5: Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix) 
    movie_user_likes ="Avatar"
    ## Step 6: Get index of this movie from its title
    movie_index = get_index_from_title(movie_user_likes)

    similar_movies =  list(enumerate(cosine_sim[movie_index]))

    ## Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

    ## Step 8: Print titles of first 50 movies
    i=0
    for element in sorted_similar_movies:
        #label= Label(frame2, text=get_title_from_index(element[0]).pack()
        l.append(get_title_from_index(element[0]))
        i=i+1
        if i>5:
            break
    return l
S()
