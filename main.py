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
        print('Элементы: ', words[0], translation[0])
        print('Типы: ', type(words), type(translation))
        return render_template('form.html', words=words, translation=translation, n=range(len(words)))
    else:
        return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
