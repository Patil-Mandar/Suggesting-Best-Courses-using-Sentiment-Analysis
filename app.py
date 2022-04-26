from flask import Flask, render_template, request
from webScraping import WebScraping

app = Flask(__name__)

CourseInfo = {
    'totalCourses': 0,
    'courses': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analysis',methods=['GET','POST'])
def analysis():
    if request.method == 'GET':
        return render_template('analysisForm.html')
    
    if request.method == 'POST':
        link = request.form.get('link')
        site = request.form.get('platform')
        CourseInfo['totalCourses'] = 1
        CourseInfo['courses'].clear() 
        CourseInfo['courses'].append(WebScraping(link,site))
        # CourseInfo['courses'][0]['rating'] = model(CourseInfo.comments)
        CourseInfo['courses'][0]['rating'] = 4.5
        return render_template('analysisReport.html',CourseInfo=CourseInfo)

@app.route('/multipleAnalysis',methods=['GET','POST'])
def multipleAnalysis():
    if request.method == 'POST':
        if request.form.get('platform'):
            link = request.form.get('link')
            site = request.form.get('platform')
            CourseInfo['totalCourses'] += 1
            CourseInfo['courses'].append(WebScraping(link,site))
            # CourseInfo['courses'][-1]['rating'] = model(CourseInfo.comments)
            CourseInfo['courses'][-1]['rating'] = 4.5
        return render_template('multipleAnalysisReport.html',CourseInfo=CourseInfo)
    
