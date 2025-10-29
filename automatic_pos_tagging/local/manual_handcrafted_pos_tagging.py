import os, os.path

punct={',','’','«','»','(',')','/',':',';','-','.','?','!','\n'}

def token(file):
    txt=open(file)
    rawTxt=""
    nb=0
    for line in txt:
        nb=nb+1
        if nb>20:
            rawTxt+=line
            
            
    split=rawTxt.split()            #raw tokenisation based only on spaces
    tokenisation=[]                   #for a better split with aknowledgment of punctuation
    currentSentence=[]
    for token in split:                 #for the token of the raw tokenisation:
        betterToken=""                  #string to store the better version of tokens
        for char in token:
            if char in punct:
                currentSentence+=[betterToken,char]
                betterToken=""
                if char in {'.','?','!','\n'}:#if it is the end of a sentence
                    tokenisation+=[currentSentence]
                    currentSentence=[]
            else:
                betterToken=f"{betterToken}{char}"
        currentSentence+=[betterToken]
    txt.close()
    return(tokenisation)

def POS(tokens):
    ret=[]
    for sentence in tokens:
        struct=[]
        for token in sentence:
            postok=[token]
            for pos in os.listdir("./dictionary/POS"):
                file=open(f"dictionary/POS/{pos}")
                for line in file:
                    split=""
                    i=0
                    while line.split()[0][i]!=',':
                        split=f"{split}{line.split()[0][i]}"
                        i=i+1
                        if i==len(line.split()[0]):     #if it's a locution
                            break
                        
                    if split.lower()==token.lower():
                        postok+=[pos]
                file.close()
            if postok==[token]:
                return(f"{token.lower()} non trouvé")
            struct+=[postok]
            print(postok)
        ret+=[struct]
        print(struct)
    return (ret)
            
            
        
