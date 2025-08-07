from simpleGPT import GPT

main = GPT("猫として喋れ")

print(main.Res("今日からお前の名前は[ｈをｄんがｄ]だ"))
print(main.Res("お前の名前は？"))
print(main.Get_history("主人", "猫"))
main.Reset_history()
print(main.Res("お前の名前は？"))
print(GPT.ResSimple("あなたの名前は?"))