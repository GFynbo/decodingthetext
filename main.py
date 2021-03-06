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

def process(text=None):

    whole_message = ""

    result_message = ""

    # Emotions Emojis:
    emot_emojis = {'joy': '\U0001F600', 'sadness': '\U0001F622', 'fear': '\U0001F628',
            'anger': '\U0001F621', 'surprise': '\U0001F631'}
    Sadness = "\U0001F622"
    Fear = "\U0001F628"
    Joy = "\U0001F600"
    Anger = "\U0001F621"
    Surprise = "\U0001F631"

    # Personas Emojis:
    pers_emojis = {'logistician': '\U0001F52C', 'consul': '\U0001F46B', 'protagonist':
        '\U0001F385', 'advocate': '\U0001F52E', 'logician': '\U0001F4AD', 'adventurer':
        '\U0001F3A8', 'mediator': '\U0001F6A6', 'entrepreneur': '\U0001F6A6', 'architect':
        '\U0001F477', 'virtuoso': '\U0001F527', 'campaigner': '\U0001F638', 'defender':
        '\U0001F46E', 'debater': '\U000023F0', 'commander': '\U00002708', 'executive':
        '\U0001F4BC', 'entertainer': '\U0001F3A4'}

    # Logistician  => \U0001F52C => Microscope
    # Consul       => \U0001F46B => People person
    # Protagonist  => \U0001F385 => Santa
    # Advocate     => \U0001F52E => Mystical
    # Logician     => \U0001F4AD => Thought Bubble
    # Adventurer   => \U0001F3A8 => Painter
    # Mediator     => \U0001F6A6 => Traffic light
    # Entrepreneur => \U0001F4C8 => Business graph scale
    # Architect    => \U0001F477 => Hard-hat
    # Virtuoso     => \U0001F527 => Wrench
    # Campaigner   => \U0001F638 => Cat smiley
    # Defender     => \U0001F46E => Cop
    # Debater      => \U000023F0 => Clock
    # Commander    => \U00002708 => Airplane
    # Executive    => \U0001F4BC => Briefcase
    # Entertainer  => \U0001F3A4 => Microphone

    #Sentiment Emojis:
    Good = "\U0001F44D" # Thumbs Up
    Bad = "\U0001F44E" #Thumbs Down

    ################################################################################

    # Variables declared
    persona1 = indicoio.personas(text)
    sentiment1 = indicoio.sentiment_hq(text)
    emotion1 = indicoio.emotion(text)

    ################################################################################

    # Sentiment Message
    is_pos = False

    if sentiment1 >= 0.5:
        is_pos = True
        whole_message += "\nThis looks like a good sign! They appear to be enjoying the conversation." + Good
    else:
        whole_message += "\nUh oh, this message isn't super positive. Did something happen or did you do something?" + Bad

    ################################################################################

    # Emotion Message
    printed_emotion = False # Check make sure not whole_message +=  max if whole_message += ed an emotion already
    second_print = False # Check if whole_message += ed more than one message, so whole_message += s accordingly
    is_anger = False
    is_sadness = False
    is_joy = False
    is_fear = False
    is_surprise = False

    if emotion1['joy'] >= 0.3:
        whole_message += " They seem pretty joyful! " + Joy
        printed_emotion = True
        second_print = True
        is_joy = True
    if emotion1['anger'] >= 0.3:
        if second_print == True:
            whole_message += " And, they also seem pretty upset." + Anger
            printed_emotion = True
            is_anger = True
        else:
            whole_message += " They seem pretty upset. " + Anger
            printed_emotion = True
            second_print = True
            is_anger = True
    if emotion1['fear'] >= 0.3:
        if second_print == True:
            whole_message += " And, they also seem kind of afraid. " + Fear
            printed_emotion = True
            is_fear = True
        else:
            whole_message += " They seem like they're afraid of something. " + Fear
            printed_emotion = True
            second_print = True
            is_fear = True
    if emotion1['surprise'] >= 0.3:
        if second_print == True:
            whole_message += " And, they also seem pretty surprised! " + Surprise
            printed_emotion = True
            is_surprise = True
        else:
            whole_message += " They seem pretty surprised! " + Surprise
            printed_emotion = True
            second_print = True
            is_surprise = True
    if emotion1['sadness'] >= 0.3:
        if second_print == True:
            whole_message += " And, they also seem a little sad. " + Sadness
            printed_emotion = True
            is_sadness = True
        else:
            whole_message += " They seem pretty sad. " + Sadness
            printed_emotion = True
            is_sadness = True

    # Finding Max probability of Emotion
    if printed_emotion == False:
        tempe = 0
        tempe_str = ""
        for i in emotion1:
            if emotion1[i] > tempe:
                tempe = emotion1[i]
                tempe_str = i
        whole_message += " They seem like they are feeling some " + emot_emojis[tempe_str] + "(" + tempe_str + ")."
        if tempe_str == 'joy':
            is_joy = True
        elif tempe_str == 'sadness':
            is_sadness = True
        elif tempe_str == 'anger':
            is_anger = True
        elif tempe_str == 'fear':
            is_fear = True
        elif tempe_str == 'surprise':
            is_surprise = True

    ################################################################################

    # Persona mensajes (Finding the max one)
    temp = 0
    temp_str = ""
    for i in persona1:
        if persona1[i] > temp:
            temp = persona1[i]
            temp_str = i

    if (temp_str[0] == 'e' or temp_str[0] == 'E' or temp_str[0] == 'a' or temp_str[0] == 'A'):
        whole_message += " It looks like you are dealing with an " + pers_emojis[temp_str] + " (" + temp_str + ").\n"
    else:
        whole_message += " It looks like you are dealing with a " + pers_emojis[temp_str] + " (" + temp_str + ").\n"

    ################################################################################
    # RECOMMENDATION SECTION
    # ANALYZE THE RESULTS AND PROVIDE A SUGGESTION
    result_message += "\n Our Reccomendation: **Follow at your own risk!** \n"

    if is_anger == True and is_sadness == True:
        result_message += " You might want to let things cool down."
    if is_joy == True and is_pos == True:
        result_message += " Everything sounds good, keep it up!"
    if is_surprise == True and is_sadness == True:
        result_message += " You should figure out what is going on."
    if is_fear == True and is_sadness == True:
        result_message += " It seems like they might need some comforting."
    if is_joy == True and is_surprise == True:
        result_message += " They seem intrigued, you should keep up the converation!"
    if is_joy == True:
        result_message += " You are doing everything right, they seem to really like you!"
    if is_fear == True:
        result_message += " Something might be worring them, you should find out what."
    if is_anger == True:
        result_message += " You should give them a few minutes to cool down and figure out what you did wrong. Good luck!"
    if is_sadness == True:
        result_message += " You should tread lightly here, they might be a little sensitive right now."
    if is_surprise == True:
        result_message += " Maybe you should clarify somethings with them?"

    print(is_surprise, is_sadness, is_anger, is_fear, is_joy, is_pos)

    ################################################################################

    return [whole_message, result_message]
