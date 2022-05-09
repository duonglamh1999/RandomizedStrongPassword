import random

def pass_word_generate(site):
    #Pass in site, return random password as string
    #Strong password(12 chars): site's+ 1upper+3 numbers+1 special char
    char_special= "!%$#@*()_-+]/?.,"
    char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    pw=site[:7] +''.join(str(s) for s in random.sample(range(0,10),3))

    random_index= random.randint(0,len(pw)-2)
    random_elements = str(random.choice(char_special))+str(random.choice(char))
    pw= pw[:random_index]+ random_elements +pw[random_index:]

    for i in range (len(pw),12):
         pw+= random.choice(char)
    return print( pw)

pass_word_generate('Amazon')



