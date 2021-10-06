def check(who, cards):
    global winner
    temp = cards[:]
    x = 0
    while x < 10:
        if temp[x] >= 3:
            winner = who
            return
        if x <= 7 and temp[x] >= 1 and temp[x+1] >= 1 and temp[x+2] >= 1:
            winner = who
            return
        x += 1


for tc in range(1, int(input())+1):
    a_num_cards = [0] * 10
    b_num_cards = [0] * 10
    winner = 0
    num_list = list(map(int, input().rstrip().split()))
    for i in range(12):
        if i & 1:
            b_num_cards[num_list[i]] += 1
            check(2, b_num_cards)

        else:
            a_num_cards[num_list[i]] += 1
            check(1, a_num_cards)

        if winner:
            break
    print('#{} {}'.format(tc, winner))
