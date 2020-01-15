#BASIC TRANSLATOR

#PANDA LANGUAGE
#rules = all vowels (a, e, i, o, u) become "g"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            #Making sure the upper case letters also get translated into upper case form.
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase to translate into Panda language: ")))