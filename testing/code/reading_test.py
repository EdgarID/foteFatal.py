import os, os.path

import ToyVersion as tv
import typeError as err
import output as out



input=os.listdir("./input")


print ("test opening file")
test=open("./Annotation/Apprenants polonophones du FLE_Licence 2 (annotated).tsv")

if len(input)==0:
    print ("input file is empty.")
for name in input:
    print (name+":")
    """file=open("dictionary/POS/verb.csv")
    for line in file:
        split=line.split()
        print(split)"""
    
    #print(tv.token("./input/"+name))
    print(tv.POS(tv.token("./input/"+name)))
    
    #err.test("./input/"+name)
    #iden=err.identification("./input/"+name)
    #print(iden)
    #print(out.response(iden))
