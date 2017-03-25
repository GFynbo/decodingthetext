import indicoio
indicoio.config.api_key = '43f08f36ac7e0871c28d67f797a78aba'

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

#User interface input
text = input("Enter the text message here: ")

#Variables
persona1 = indicoio.personas(text)
sentiment1 = indicoio.sentiment_hq(text)
emotion1 = indicoio.emotion(text)

#Sentiment Message
if sentiment1 >= 0.5:
    print("\nThis looks like a good sign!")
else:
    print("Uh oh")

#Emotion Message
if emotion1['joy'] >= 0.5:
    print("They seem pretty joyful!")
if emotion1['anger'] >= 0.5:
    print("They seem pretty angry...")
if emotion1['fear'] >= 0.5:
    print("They seem pretty fearful.")
if emotion1['surprise'] >= 0.5:
    print("They seem pretty surprised!")
if emotion1['sadness'] >= 0.5:
    print("They seem pretty sad...")

#Finding Max probability of Emotion
tempe = 0
tempe_str = ""
for i in emotion1:
    if emotion1[i] > tempe:
        tempe = emotion1[i]
        tempe_str = i

print("They seem like they are feeling some",tempe_str, ".")


#Persona message
if persona1['logistician'] >= 0.5:
    print("Looks like you are dealing with a logistician\n")
elif persona1['consul'] >= 0.5:
    print("Looks like you are dealing with a consul\n")
elif persona1['protagonist'] >= 0.5:
    print("Looks like you are dealing with a protagonist\n")
elif persona1['advocate'] >= 0.5:
    print("Looks like you are dealing with a advocate\n")
elif persona1['logician'] >= 0.5:
    print("Looks like you are dealing with a logician\n")
elif persona1['adventurer'] >= 0.5:
    print("Looks like you are dealing with a adventurer\n")
elif persona1['mediator'] >= 0.5:
    print("Looks like you are dealing with a mediator\n")
elif persona1['entrepreneur'] >= 0.5:
    print("Looks like you are dealing with a entrepreneur\n")
elif persona1['architect'] >= 0.5:
    print("Looks like you are dealing with a architect\n")
elif persona1['virtuoso'] >= 0.5:
    print("Looks like you are dealing with a virtuoso\n")
elif persona1['campaigner'] >= 0.5:
    print("Looks like you are dealing with a campaigner\n")
elif persona1['defender'] >= 0.5:
    print("Looks like you are dealing with a defender\n")
elif persona1['debater'] >= 0.5:
    print("Looks like you are dealing with a debater\n")
elif persona1['commander'] >= 0.5:
    print("Looks like you are dealing with a commander\n")
elif persona1['executive'] >= 0.5:
    print("Looks like you are dealing with a executive\n")
elif persona1['entertainer'] >= 0.5:
    print("Looks like you are dealing with a entertainer\n")

#Finding Max probability of Persona
temp = 0
temp_str = ""
for i in persona1:
    if persona1[i] > temp:
        temp = persona1[i]
        temp_str = i

print("Looks like you are dealing with a(n)",temp_str, ".\n")

# print('Emotion right now:', emotion1)
# print('Sentiment right now:', sentiment1)
# print('Persona right now:', persona1)
