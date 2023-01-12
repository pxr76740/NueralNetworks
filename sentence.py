sentence=str(input("please enter the sentence "))
old="python"
withnew="pythons"
print("sentence is :",sentence)
def replacepythonwithpythons(sentence,old,withnew):
    return sentence.replace(old,withnew)
print(replacepythonwithpythons(sentence,old,withnew))
