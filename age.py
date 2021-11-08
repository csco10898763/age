driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
    print('\n只能輸入,有 or 沒有 !')
    raise SystemExit

age = input('\n請問你的年齡：')
age = int(age)
if driving == '有':
    if age >= 18:
        print('\n你通過測驗 !!!')
    else:
        print('\n奇怪,你怎麼會開過車 !')

elif driving == '沒有':
    if age >= 18: 
        print('\n你可以考駕照了啊,怎麼還不去考 !')
    else:
        print('\n很好,再過幾年就可以考駕照了 !')
