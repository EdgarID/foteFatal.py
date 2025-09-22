import os, os.path
import typeError as err
import output as out

input=os.listdir("./input")

if len(input)==0:
    print ("input file is empty.")
for name in input:
    print (name+":")
    err.test("./input/"+name)
    iden=err.identification("./input/"+name)
    print(iden)
    print(out.response(iden))
