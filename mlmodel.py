import pickle
import math
def Ratings(comments):
    print("Comments Vishal ",comments)
    vectorizer = pickle.load(open('./vector.pkl','rb'))
    matrix = vectorizer.transform(comments)
    model = pickle.load(open('./model.pkl','rb'))
    list_of_ratings = model.predict(matrix)
    count = {
    '1':0,
    '0':0,
    '-1':0
    }
    # list_of_ratings = [1,-1,1,1,0]
    for i in list_of_ratings:
        count[str(i)]+= 1

    print(count)
    rating =  (count['-1']*0 + count['0']*1 + count['1']*2)*5/(len(list_of_ratings)*2)
    return round(rating,2)