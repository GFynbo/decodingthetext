import indicoio
indicoio.config.api_key = '43f08f36ac7e0871c28d67f797a78aba'

# single example
indicoio.sentiment_hq("I love writing code!")

text = input("Enter text here: ")

# batch examp
happiness = indicoio.sentiment_hq([
    text
])

print(happiness)
