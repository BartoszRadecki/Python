import random
import sys

print("Ile chcesz prób?: ")
no_of_tries = input()
no_of_tries=int(no_of_tries)
lista_slow = ['BATERIA', 'WODOCIĄG', 'UJŚCIE', 'ARSYNA', 'JUBILEUSZ', 'SINICE', 'PARMEZAN', 'MAJDANIARZ', 'TWARZ', 'ODPOWIEDZIALNOŚĆ', 'KONTRAKT', 'KSZTAŁCENIE', 'HEGEMONIA', 'ZSZYWARKA', 'LEASING', 'NIEŻYWOŚĆ', 'BEZIMIENNOŚĆ', 'RÓJ', 'KRYSZTAŁEK', 'ZACHOWEK', 'KREM', 'ECHOLOKACJA', 'DRIAKIEW', 'TWÓR', 'KOŁNIERZ', 'MARYNARZ', 'HUMOR', 'INSTRUMENT', 'KREACJONIZM']

word = random.choice(lista_slow).lower()
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery: ", used_letters)
    print ()

for _ in word:
    user_word.append("_")


while True:
    letter = input("podaj literę: ")
    if letter in used_letters:
        print("Ta litera już została sprawdzona")
        show_state_of_game()
        continue
    used_letters.append(letter)
    if letter.isalpha() == False:
        print("Podano nieprawidłowy symbol")
        show_state_of_game()
        continue


    found_indexes = find_indexes(word,letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Koniec gry :(")
            print("Czy chcesz zagrać jeszcze raz? Tak = 1, Nie = 0")
            jeszcze_raz = input()
            if jeszcze_raz == 0:
                sys.exit(0)
            else:
                no_of_tries = 5
    else:
        for index in found_indexes:
            user_word[index] = letter


        if "".join(user_word) == word:
            print("Brawo, to jest to słowo! -- ", word)

            sys.exit(0)


    show_state_of_game()