ppl_invited = ["albert einstein","john lennon","JFK","feynman"]
print("Oh no, " + ppl_invited.pop().title() + " Can't make it!")
new_invitee = "claude shannon"
ppl_invited.append(new_invitee)

print("\nThat's ok, we can invite " + new_invitee.title())
print("\nOur new invite list looks like this: ")
print(ppl_invited)

print("\nWait!, I found a bigger dinner table! Lets invite more people.")
new_invitees = ["martin luther king","ghandi"]
ppl_invited.extend(new_invitees) # the extend method appends lists
print("We can invite " + str(new_invitees))
print("Our new list of guests looks like this:")
print(ppl_invited)

print("\nOh no!, the table won't arrive in time! Only two people can come now")
print("Sorry " + str(ppl_invited.pop()) + " we ran out fo room")
print("Sorry " + str(ppl_invited.pop()) + " we ran out fo room")
print("Sorry " + str(ppl_invited.pop()) + " we ran out fo room")
print("Sorry " + str(ppl_invited.pop()) + " we ran out fo room")
#del ppl_invited [2:]
print("Te people that will come will be: " + str(ppl_invited))
