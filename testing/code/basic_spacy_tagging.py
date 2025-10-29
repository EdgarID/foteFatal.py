import spacy

nlp=spacy.load('fr_core_news_md')

text = "Le petit garcon mange une pomme rouge."

doc=nlp(text)

for word in doc:
    gender=word.morph.get("Gender")
    print(f"the word is: {word.text}")
    print(f"the lemma is: {word.lemma_}")
    print(f"the POS tag is: {word.pos_}")
    print(f"the features are: {word.morph}")
    print(f"the gender is: {gender if gender else None}")
    print('-'*30)
