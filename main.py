from flask import Flask, render_template, request
from randomw import *
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation=None
    res=None
    words=None
    if request.method=='POST' and 'count' in request.form:
        view=yaTranslation()
        #assigning None for no request
        words=view.getrandom(request.form['count'])
        translation=view.gettranslate(words)
        return render_template('form.html', org=words.split(), res=translation)
    else:
        return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
