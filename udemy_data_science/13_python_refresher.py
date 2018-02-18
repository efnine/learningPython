# write a function that retrieves the domain from an email address
def getDomainFromEmail(email_address):
    domain = email_address.split("@")[1]
    website = ('wwww.' + domain)
    return website

print(getDomainFromEmail('daniel.e.nieto@gmail.com'))   


# create a basic funciton that return True if the word 'dog' is
# contained in the inout string
user_input = "Is there a dog in there?"
print('dog' in user_input.lower())


# count how many times dog is in a sentence
sentence= "this dog runs faster than any other dog among all dogs"
word_count = 0
for word in sentence.split():
    if word == 'dog':
        word_count += 1
    else:
        pass

print(word_count)

# use lambda expression to filter out words that do not
# start with the letter 's'
seq = ['soup','pancakes','cookies','salad']       
filter_list = []

for i in range(len(seq)):
    if seq[i][0] == 's':
        filter_list.append(seq[i]) 
    else:
        pass
print(filter_list)

print(list(filter(lambda word: word[0]=='s',seq)))

