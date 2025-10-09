import os, os.path
import stanza
#import pandas as pd

stanza.download('fr')

import typeError as err
import output as out



input=os.listdir("./input")


print ("test opening file")
test=open("./Annotation/Apprenants polonophones du FLE_Licence 2 (annotated).tsv")
print(test.read())

if len(input)==0:
    print ("input file is empty.")
for name in input:
    print (name+":")
    err.test("./input/"+name)
    iden=err.identification("./input/"+name)
    print(iden)
    print(out.response(iden))
