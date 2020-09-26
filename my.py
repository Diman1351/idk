import random
import time

wordlist = ("кошка","абзац","берега")

def get_word():
    word = random.choice(wordlist)
    return word

def welcome_message(n):
    print(f"Угадай слово из {n} букв")
    gaps = []
    for i in range(n):
        gaps.append("_")
    gaps = " ".join(gaps)
    print(gaps)

def get_letter(word):
    letter = input()
    found = []
    last = -1
    while True:
        index = word.find(letter, last+1)
        if index == -1:
            break
        found.append(index)
        last = index
    return found
            


def main():
    word = get_word()
    welcome_message(len(word))
    print(get_letter(word))

main()