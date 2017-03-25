import indicoio
from flask import Flask, render_template, url_for, request, flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

app = Flask(__name__)

indicoio.config.api_key = '43f08f36ac7e0871c28d67f797a78aba'
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
        return success(form.message.data, form.message.data)
    elif request.method == 'GET':
        return render_template('decode.html', form = form)
    return render_template('decode.html', form=form)

@app.route('/success/', methods=('GET', 'POST'))
def success(results=None, message=None):
    results = process(results)
    return render_template('success.html', results=results, message=message)

if __name__ == "__main__":
    app.run()


################################################################################
# Indico Examples:
#
# Emotion: emotion(data, [api_key], [cloud], [top_n], [threshold])
#       Outputs: Probability of the 5 emotions (anger, fear, joy, sadness, surprise)
#
# Persona: personas(data, [api_key], [cloud], [top_n], [threshold])
#       Outputs: Probability of the 16 Myers Briggs personas (logistician, consul,
#               protagonist, advocate, logician, adventurer, mediator, entrepreneur,
#               architect, virtuoso, campaigner, defender, debater, commander,
#               executive, entertainer)
#
# Sentiment HQ: sentiment_hq(data, [api_key], [cloud], [language])
#       Outputs: number between 0 and 1. This number is a probability representing
#        the likelihood that the analyzed text is positive or negative
#
################################################################################
# Emoji Unicode List:

def process(text=None):

    whole_message = ""

    emot_emojis = {'joy': '\U0001F600', 'sadness': '\U0001F622', 'fear': '\U0001F628', 'anger': '\U0001F621', 'surprise': '\U0001F631'}

    # Emotions
    Sad = "\U0001F622"
    Fear = "\U0001F628"
    Happy = "\U0001F600"
    Angry = "\U0001F621"
    Surprise = "\U0001F631"

    # Personas
    # Logistician = "\U0001F #
    # Consul = "\U0001F  #
    # Protagonist = "\U0001F
    Advocate = "\U0001F575" #investigator
    # Logician = "\U0001F
    Adventurer = "\U0001F3C4" #surfing
    Mediator = "\U00002696"  #judge
    # Entrepreneur = "\U0001F
    Architect = "\U0001F477"  #hardhat
    #Virtuoso = "\U0001F" #graduate
    # Campaigner = "\U0001F
    Defender = "\U0001F46E" #cop
    # Debater = "\U0001F #teacher
    # Commander = "\U0001F
    Executive = "\U0001F4BC"  #suit
    Entertainer = "\U0001F3A4" #singer

    whole_message += "Entertainer" + Entertainer
    whole_message += "Executive" + Executive
    whole_message += "Defender" + Defender
    whole_message += "Architect" + Architect
    whole_message += "Mediator" + Mediator
    whole_message += "Adventurer" + Adventurer
    whole_message += "Advocate" + Advocate

    ################################################################################

    # Variables
    persona1 = indicoio.personas(text)
    sentiment1 = indicoio.sentiment_hq(text)
    emotion1 = indicoio.emotion(text)

    ################################################################################

    # Sentiment Message
    if sentiment1 >= 0.5:
        whole_message += "\nThis looks like a good sign! They appear to be enjoying the conversation."
    else:
        whole_message += "\nUh oh, this message isn't super positive. Did something happen or did you do something?"

    ################################################################################

    # Emotion Message
    printed_em = False # check make sure not whole_message +=  max if whole_message += ed an emotion already
    second_pr = False # check if whole_message += ed more than one message, so whole_message += s accordingly


    if emotion1['joy'] >= 0.3:
        whole_message += " They seem pretty happy! " + Happy
        printed_em = True
        second_pr = True
    if emotion1['anger'] >= 0.3:
        if second_pr == True:
            whole_message += " And, they also seem pretty upset." + Angry
            printed_em = True
        else:
            whole_message += " They seem pretty upset. " + Angry
            printed_em = True
            second_pr = True
    if emotion1['fear'] >= 0.3:
        if second_pr == True:
            whole_message += " And, they also seem kind of afraid. " + Fear
            printed_em = True
        else:
            whole_message += " They seem like they're afraid of something. " + Fear
            printed_em = True
            second_pr = True
    if emotion1['surprise'] >= 0.3:
        if second_pr == True:
            whole_message += " And, they also seem pretty surprised! " + Surprise
            printed_em = True
        else:
            whole_message += " They seem pretty surprised! " + Surprise
            printed_em = True
            second_pr = True
    if emotion1['sadness'] >= 0.3:
        if second_pr == True:
            whole_message += " And, they also seem a little sad. " + Sad
            printed_em = True
        else:
            whole_message += " They seem pretty sad. " + Sad
            printed_em = True

    # Finding Max probability of Emotion
    if printed_em ==  False:
        tempe = 0
        tempe_str = ""
        for i in emotion1:
            if emotion1[i] > tempe:
                tempe = emotion1[i]
                tempe_str = i
        whole_message += " They seem like they are feeling some " + emot_emojis[tempe_str] + "(" + tempe_str + ")."

    ################################################################################

    # Persona mensajes
    # Finding Max probability of Persona
    temp = 0
    temp_str = ""
    for i in persona1:
        if persona1[i] > temp:
            temp = persona1[i]
            temp_str = i

    if (temp_str[0] == 'e' or temp_str[0] == 'E' or temp_str[0] == 'a' or temp_str[0] == 'A'):
        whole_message += " It looks like you are dealing with an " + temp_str + ".\n"
    else:
        whole_message += " It looks like you are dealing with a " + temp_str + ".\n"

    ################################################################################
    # RECOMMENDATION SECTION
    # ANALYZE THE RESULTS AND PROVIDE A SUGGESTION


    ################################################################################

    return whole_message
