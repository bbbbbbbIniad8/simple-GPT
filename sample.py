from simpleGPT import GPT


def sample1():
    news = GPT.res_simple("この世の終わりみたいな冗談みたいな架空のニュースを300字以内で解説しろ")

    print(f"[最新のニュース]\n\n{news}\n\n\n\n")

    woman = GPT("あなたはニュースの女のコメンテーターである。")
    dog = GPT("あなたはニュースの犬のコメンテーターである。犬なので犬語で喋れ。")

    question = f"以下のニュースに対してコメントしろ。\n\n{news}"
    print(f"[コメンテーター1のコメント]\n{woman.res(question)}\n\n\n")
    print(f"[コメンテーター2のコメント]\n{dog.res(question)}\n\n\n")

def sample2():
    cat = GPT("猫として喋れ(200字以内で)")
    while True:
        print(cat.res("挨拶しろ", save=False) + "\n\n\n")
        for i in range(3):
            you_say = input("あなた発言を入力してください\n:")
            print("\n\n\n" + cat.res(you_say) + "\n\n\n")

        print("会話は終了しました。会話ログをtxtファイルで出力しますか?[y/n]")
        if input(":") == "y":
            with open("log.txt", mode = "w", encoding="utf-8") as f:
                f.write(cat.get_history(AI_name="猫"))
        
        print("もう一度最初から会話をやり直しますか?")
        if input(":") == "y":
            cat.reset_history()
            print("\n\n\n")
            continue
        else:
            break
        

sample2()