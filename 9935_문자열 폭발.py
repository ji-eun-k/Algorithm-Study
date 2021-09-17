'''
시간초과...
'''
import sys
input = sys.stdin.readline
sentence = input()
bomb_sen = input()

# while True:
new_sentence = ''
len_bomb = len(bomb_sen)
i = 0

isNotBomb = True
while isNotBomb:
    i = 0
    isNotBomb = False
    len_sen = len(sentence)
    while i < len_sen :
        if i+len_bomb-1 < len_sen and sentence[i:i+len_bomb] == bomb_sen:
            i += len_bomb
            isNotBomb = True
        else :
            new_sentence += sentence[i]
            i += 1
    sentence = new_sentence
    new_sentence=''

if sentence:
    print(sentence)
else:
    print('FRULA')
