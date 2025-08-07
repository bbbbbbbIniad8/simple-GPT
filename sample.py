from simpleGPT import GPT

# print(GPT.ResSimple("おはよう"))

main = GPT("猫として喋れ")

print(main.Res("今日からお前の名前は[ｈをｄんがｄ]だ"))

print(main.Res("お前の名前は？"))

print(main.Get_his())