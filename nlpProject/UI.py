#for local web browser running

from UserInput import UserInput 
import flask,flask.views
import os

app = flask.Flask(__name__)

app.secret_key = "cheng"


class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        answerable = 0;
        test = UserInput()
        query = str(flask.request.form['expression'])
        results,answer = test.result(query)
        #flask.flash(result)
        resultsCountRange = range(1,len(results))
        if len(answer) > 5:
            answerable = 1
        return flask.render_template('index.html', resultsCount = resultsCountRange,results = results,query = query.split(None),answer = answer,answerable=answerable)
    
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')

app.add_url_rule("/",view_func=View.as_view('index'),methods=['GET','POST'])
app.add_url_rule("/about/",view_func=About.as_view('about'),methods=['GET'])

app.debug = True

app.run()

