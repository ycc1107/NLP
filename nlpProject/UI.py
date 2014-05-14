from UserInput import UserInput 
import flask,flask.views
import os

app = flask.Flask(__name__)

app.secret_key = "cheng"


class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        test = UserInput()
        result = test.result(str(flask.request.form['expression']))
        #flask.Flash(result)
        return flask.render_template('index.html', list=result)


app.add_url_rule("/",view_func=View.as_view('main'),methods=['GET','POST'])

app.debug = True

app.run()

