import indicoio
from flask import Flask, render_template, url_for, request, flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required


app = Flask(__name__)

app.secret_key = 'do not try to guess this'

@app.route("/")
def home():
    return render_template('index.html')


class MyForm(Form):
    message = TextAreaField('Message', validators=[Required()])
    submit = SubmitField("Submit")

def process(message):
    # ENTER_TATIANA_CODE_HERE
    return ""

@app.route('/decode/', methods=('GET', 'POST'))
def decode():
    form = MyForm()
    if request.method == 'POST':
        return success(form.message.data)
    elif request.method == 'GET':
        return render_template('decode.html', form = form)
    return render_template('decode.html', form=form)

@app.route('/success/', methods=('GET', 'POST'))
def success(results=None):
    length = len(results)
    results = length
    return render_template('success.html', results=results)

if __name__ == "__main__":
    app.run()
