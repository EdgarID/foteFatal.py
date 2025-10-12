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
