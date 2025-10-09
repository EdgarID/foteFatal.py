
test=open("./Annotation/Apprenants polonophones du FLE_Licence 2 (annotated).tsv")
for line in test:
    for i in range (len(line)):
        if line[i]=="*":
            print("pos tagging:")
            print([line[i+2+j] for j in range(3)])
            print("error tagging:")
            print([line[i+6+j] for j in range(len(line)-i-8)])
    print(line)