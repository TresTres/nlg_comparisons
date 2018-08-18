#abc_news_nlg.py


import pandas as pd #data proc
import markovify #markov chain gen

inp = pd.read_csv('./abcnews-date-text.csv')

text_model = markovify.NewlineText(inp.headline_text, state_size = 2) #pair wise chain building

for i in range(10):
    print(text_model.make_sentence())
