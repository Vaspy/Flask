from flask import Flask, render_template, request
from randomw import randomtorus
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation=None
    res=None
    if request.method=='POST' and 'count' in request.form:
        #assigning None for no request
        translation=randomtorus(request.form['count'])
    return render_template('form.html', res=translation)

if __name__ == '__main__':
    app.run(debug=True)
