word = "kajak"
print("Is palidrom: ", word == word[::-1])

sentence ="Kobyła ma mały bok"
sentence = sentence.replace(" ","")
print(sentence)
sentence = sentence.lower()
print(sentence)
print("Is palidrom: ", sentence == sentence[::-1])

sentence =input("Give me a sentence?  ")
sentence = sentence.replace(" ","")
print(sentence)
sentence = sentence.lower()
print(sentence)
print("Is palidrom: ", sentence == sentence[::-1])