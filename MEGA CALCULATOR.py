import numexpr, locale

aboba_lox = "hgdf"
current_lang, encoding = locale.getdefaultlocale()

#print("Select language RU or EN")
#lang = input()
#lang = lang.upper()

if current_lang == "ru_RU":
    while aboba_lox != "Да" or aboba_lox != "да":
        aboba = input("Введите выражение: ")
        if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
            print("На ноль делить нельзя!")
        # elif "**" in aboba:
        #    print("Cимовл \"**\" нельзя использовать.")
        else:
            result = numexpr.evaluate(aboba)
            print(f"Результат: {result}")
            print("Продолжить?")
            aboba_lox = input()
            if aboba_lox == "Нет" or aboba_lox == "нет":
                break

elif current_lang == "be_BY":
    while aboba_lox != "Так" or aboba_lox != "так" or aboba_lox != "Да" or aboba_lox != "да":
        aboba = input("Увядзіце выраз: ")
        if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
            print("На нуль дзяліць нельга!")
        else:
            result = numexpr.evaluate(aboba)
            print(f"Вынік: {result}")
            print("Працягнуць?")
            aboba_lox = input()
            if aboba_lox == "Нет" or aboba_lox == "нет" or aboba_lox == "Не" or aboba_lox == "не":
                break

elif current_lang == "tr_TR":
    while aboba_lox != "Evet" or aboba_lox != "evet" or aboba_lox != "Yes" or aboba_lox != "yes":
        aboba = input("Bir ifade girin:")
        if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
            print("Sıfıra bölemezsiniz!")
        else:
            result = numexpr.evaluate(aboba)
            print(f"Sonuç: {result}")
            print("Devam etmek?")
            aboba_lox = input()
            if aboba_lox == "Hayır" or aboba_lox == "hayır" or aboba_lox == "No" or aboba_lox == "no":
                break

else:
    while aboba_lox != "Yes" or aboba_lox != "yes":
        aboba = input("Enter an expression: ")
        if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
            print("You cannot divide by zero!")
        else:
            result = numexpr.evaluate(aboba)
            print(f"Result: {result}")
            print("Continue?")
            aboba_lox = input()
            if aboba_lox == "No" or aboba_lox == "no":
                break