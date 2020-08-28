import random

file = open("usa.txt","r")
words = []

#agrupar em 'words' todas as palavras inglesas com comprimento entre 5 e 8
for line in file:
    line = line.strip('\n')
    if len(line) > 4:
        words.append(line)

def picture(fails):
    if fails == 0:
        return """
                  ________  
                  |      |
                         |
                         |
                         |
                        _|_
                """
    elif fails == 1:
        return """
                  ________  
                  |      |
                  O      |
                         |
                         |
                        _|_
                """
    elif fails == 2:
        return """
                  ________  
                  |      |
                  O      |
                  |      |
                  |      |
                        _|_
                """
    elif fails == 3:
        return """
                  ________  
                  |      |
                  O      |
                 \|      |
                  |      |
                        _|_
                """
    elif fails == 4:
        return """
                  ________  
                  |      |
                  O      |
                 \|/     |
                  |      |
                        _|_
                """
    elif fails == 5:
        return """
                  ________  
                  |      |
                  O      |
                 \|/     |
                  |      |
                 /      _|_
                """
    elif fails == 6:
        return """
                  ________  
                  |      |
                  O      |
                 \|/     |
                  |      |
                 / \    _|_
                """


def hangman(words):

    secret = random.choice(words)   # escolha aleatória de uma palavra de 'words'
    blank = list('_' * len(secret)) # criar lista com n elementos '_', n = len(secret)
    dic = {}                        # dicionário para guardar caracteres da secret word e os respetivos indexes

    for i in range(0, len(secret)):
        if secret[i] not in dic:
            dic.setdefault(secret[i], [i])
        else:
            dic[secret[i]].append(i)

    fails = 0
    misses = []
    guesses = []           # listas com caracteres errados e certos
    print(picture(fails))
    print('Try to guess the secret word! If you fail 6 times, you will be hanged.')
    print('Word: ' + "".join(blank))

    while fails < 6:

        print('Character: ')
        char = input().lower()

        while ((len(char) != 1) or (not char.isalpha())):
            print('Character: ')
            char = input().lower()

        if (char in misses or char in guesses):   #se é repetido
            print('You tiped that character before, try again.')
        elif (char in dic):                       #se acertar
            guesses.append(char)
            for integer in dic[char]:
                blank[integer] = char
        elif (char not in dic):                   #se errar
            misses.append(char)
            fails += 1

        print('\nWord: ' + "".join(blank))
        print('Fails: ' + str(fails) + " | Misses: " + " / ".join(misses))
        print(picture(fails))

        if fails == 6:
            print('\nYou failed 6 times and you were hanged!')
            print('The correct word was ' + secret)

        if "".join(blank) == secret:
            print('Congratulations, you guessed the word!')
            break

def main():

    print('Welcome to the Hangman Game!')
    hangman(words)

main()
