# pig latin

text =       """Darkness at the break of noon 
          Shadows even the silver spoon 
          The handmade blade, the child's balloon 
          Eclipses both the sun and moon"""

VOWELS ='aeiou'
CONSONANTS = 'qwrtypsdfghjklzxcvbnm'

text = text.split()
pig_latin = ''

for word in text:
    if word[0].lower() in VOWELS:
        pig_latin += word + " way "
    elif word[0].lower() in CONSONANTS and word[1].lower() in CONSONANTS:
        pig_latin += word[2:] + " " + word[:2] + "ay "  
    else:
        pig_latin += word[1:] + " " + word[0] + "ay "

print(pig_latin)                 

