def lineUpdate(sentence, updatedSentence, lineNo=""):
    with open("F:\\PYTHON-NOTES\\practice\\read.txt", "r") as fp:
        if lineNo == "":
            content = fp.read()
            updated = content.replace(sentence, updatedSentence)
            with open("F:\\PYTHON-NOTES\\practice\\read.txt", "w") as fp:
                fp.write(updated)
        else:
            content = fp.readlines()
            line = content[int(lineNo)]
            updated = line.replace(sentence, updatedSentence)
            content[int(lineNo)] =  updated
            final ="".join(content)
            with open("F:\\PYTHON-NOTES\\practice\\read.txt", "w") as fp:
                fp.write(final)

sentence = input("Enter Sentence To Replace : ")
updatedSentence = input("Enter Updated Sentence : ")
lineNo = input("Enter Line Number(optional) : ")
if len(lineNo)==0 and len(sentence)==0:
    print("Please Enter Valid Input !!!")
else:
    print("inside else")
    lineUpdate(sentence, updatedSentence, lineNo)
