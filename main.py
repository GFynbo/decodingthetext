import indicoio
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/decode/")
def decode():
    return render_template('decode.html')

if __name__ == "__main__":
    app.run()

'''
def main():

    hello()

    indicoio.config.api_key = '43f08f36ac7e0871c28d67f797a78aba'

    # single example
    indicoio.sentiment_hq("I love writing code!")

    text = input("Enter text here: ")

    # batch examp
    happiness = indicoio.sentiment_hq([
        text
    ])

    print(happiness)
    ans = "Result: " + str(happiness)
    return ans
'''
