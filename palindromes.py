word = input("Enter your word").lower() #getting the word and making it lowercase

#checking length
length = len(word)

#creating intermediate list
intermediate_word = list(word)

for letter in word: #looping through word letters
  length -= 1 #length counter -1
  intermediate_word[length] = letter #substituting with current letter

new_word = "".join(intermediate_word) #concatenating list to the new word

print("%s backwards is %s" % (word, new_word))

if new_word == word: #Palyndrome checking
  print("It's a palyndrome!")
