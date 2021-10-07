for tc in range(1, int(input())+1):
    days = input()
    y = days[:4]
    m = days[4:6]
    d = days[6:]
    check = False
    if int(m) < 1 or int(m) > 12:
        check = True
    if m == '02' and int(d) > 28:
        check = True
    if int(d) < 1 :
        check = True
    if m in ('01', '03', '05', '07', '08', '10', '12') and int(d) > 31:
        check = True
    if m in ('04', '06', '09', '11') and int(d) > 30:
        check = True
    if check:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, '/'.join([y, m, d])))