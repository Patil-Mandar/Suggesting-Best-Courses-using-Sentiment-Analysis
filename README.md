# Suggesting-Best-Courses-using-Sentiment-Analysis

 ## Model files link
 <pre>
 https://www.mediafire.com/file/1xyj8geqfhwqurj/model.pkl/file
 https://www.mediafire.com/file/c5qcusvf96ckg14/vector.pkl/file
 download these both the files and place it in the root directory

</pre>
**-> We aimed to analyze courses on the basis of their comments and not just the stars the get.**

**-> You just have to enter the URL of the course you want to analyze.**

**-> By web scraping, we get the comments on that course and send it to our ML model (Count vectorizer followed by Random Forest).**

**-> The model classifies each comment into positive, negative and neutral.**

**-> After applying some maths, we display a rating of that course purely on the basis of the comments it has.**

**-> The model is trained on https://www.kaggle.com/datasets/imuhammad/course-reviews-on-coursera**

**Here is performance of the model -**

<img width="350" alt="Screenshot 2022-05-01 130053" src="https://user-images.githubusercontent.com/76464970/166136606-f5783a32-0e55-49ec-a039-1099fbc10e52.png">

**Working -**

![ISA](https://user-images.githubusercontent.com/76464970/166136619-cd8c02de-2ed2-49e2-a048-d9ad5c28f659.gif)
 
