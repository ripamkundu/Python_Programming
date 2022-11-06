#Count the Number of Each Vowel

vowels = 'aeiou'
vowel = 'AEIOU'

string = "Count the Number of Each Vowel Small latter"
string1 = "Count the Number of Each Vowel Capital latter"
string = string.casefold()
string1 = string1.casefold()
count = {}.fromkeys(vowels,0)
count1 = {}.fromkeys(vowel,0)

for char in string:
 if char in count:
  count[char] = count[char] + 1 
print(count)

for char in string1:
  for char in count1:
   count1[char] = count1[char] + 1
print(count1)