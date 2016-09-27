#Program to check if user entry is palindrome

print "This program checks if your entry is a palindrome."
print "\n\n"
print "-" * 10

word = raw_input("Please enter your word:  ")
#reverse = word[::-1]

if word == word[::-1]:
    print "Your word %s is definately palindromic!" % word
else:
    print "Your word %s is definately not palindromic!" % word
