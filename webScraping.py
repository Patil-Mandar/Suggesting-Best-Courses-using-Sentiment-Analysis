from bs4 import BeautifulSoup
import urllib.request, json
import requests

def WebScraping(link,site):
    return {
        'title' : 'Flask Course',
        'instructor' : 'Mandar Patil',
        'duration' : '12 hr',
        'learner_count': '12421 total leaners',
        'description': 'Start Learning Flask from complete start. We cover all the main topics in best way possible compared to all the available plaform till the date',
        'comments' : ['Hello World','Great course']
    }


# def WebScraping(link,platform):
#     site = platform
#     c_url = link
#     comments = []
#     c = []
#     result = {}
#     if site == "Coursera":
#         result['platform']='Coursera'
#         if '?' in c_url:
#             c_url = c_url[:c_url.index("?")]
#         url = c_url
#         response = requests.get(url)
#         htmlcontent = response.content
#         soup = BeautifulSoup(htmlcontent, "html.parser")
#         c = soup.findAll('h1', {'class': 'banner-title banner-title-without--subtitle m-b-0'})
#         for i in c:
#             result["title"] = i.text
#         c = soup.findAll('div', {'class': '_16ni8zai m-b-0 m-t-1s'})
#         for i in c:
#             result["duration"] = i.text
#         c = soup.findAll('h3', {'class': 'instructor-name headline-3-text bold'})
#         for i in c:
#             result["instructor"] = i.text
#         c = soup.findAll('div', {'class': 'learners-count'})
#         for i in c:
#             result["learner_count"] = i.text
#         for k in range(1, 5):
#             url = c_url + "/reviews?page=" + str(k)
#             response = requests.get(url)
#             htmlcontent = response.content
#             soup = BeautifulSoup(htmlcontent, "html.parser")
#             container = soup.findAll('div', {'class': 'rc-CML font-lg show-soft-breaks cml-cui'})
#             for j in container:
#                 comments.append(j.text)
#         result["comments"] = comments
#         return result
    
#     if site == "Youtube":
#         result['platform']='Youtube'
#         #TODO get video id from url link
#         video_id = '6oxkWWfiVHs'
#         url = 'https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&videoId={}&key={}'.format(video_id,'AIzaSyDEgmEzXQ7GCRXqAa8ctgc6jA50vZJLhR4')
#         response = urllib.request.urlopen(url)
#         data = response.read()
#         data = json.loads(data)
#         for i in range(100):
#             comments.append(data['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'])
#         result["comments"] = comments
#         return result