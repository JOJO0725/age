ask = input('你有開車的經驗嗎? (yes or no)')
if ask == 'yes':
    when = input('你幾歲開始開車?')
    when = int(when)
    if when < 18:
        print('你這樣還太小,開車是違法的!!!')
    elif when >= 18 and when < 75:
        print('你是個守法的好公民!!!')
    else:
        print('你年紀太大了需要找人載,比較安全!!')
elif ask == 'yes':
    qus = input('你滿18歲了嗎?(yes or no)')
    if qus == 'yes':
        print('你可以考慮考一張駕照!')
    else:
        print('等你成年再來考駕照吧!')         
else:
    print('請輸入 yes 或 no')
    raise SystemExit
    