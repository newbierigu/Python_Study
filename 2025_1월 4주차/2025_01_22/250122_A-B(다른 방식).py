def minus():
    print("'★ ★' 해당 양식으로 뺄 숫자를 입력해 주세요.")

    inp = input()
    splited_inp = inp.split()

    x = int(splited_inp[0])
    y = int(splited_inp[1])


    if x > 9:
        print("한 자리 숫자만 가능합니다.")
        minus()
        return

    if y > 9:
        print("한 자리 숫자만 가능합니다.")
        minus()
        return

    print(x - y)

minus()