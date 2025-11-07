import spacy

nlp=spacy.load('fr_core_news_md')

def check_sentence_capitalization(paragraph):
    capitalization_err_count=0
    doc= nlp(paragraph)
    results=[]

    for sent in doc.sents:
        sentence=sent.text.strip()
        if not sentence:
            continue
        fLetter=None
        for char in sentence:
            if char.isalpha():
                fLetter=char
                break
        if fLetter is None:
            continue  
        if not fLetter.isupper():
            capitalization_err_count+=1
            stat="should start with uppercase"
        else:
            stat="correct cap..."
        results.append({
            "sentence":sentence,
            "status":stat
        })
    return results,capitalization_err_count
     

paragraph = "bonjour tout le monde. Comment ça va? ça va bien ! bonjour"
results,counter = check_sentence_capitalization(paragraph)
for r in results:
 print(f"Sentence: '{r['sentence']}' : {r['status']}")

print(f"the number of caitalization errors is {counter}")