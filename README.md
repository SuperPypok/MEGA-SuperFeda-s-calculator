# MEGA SuperFeda's calculator
## About:
A calculator that automatically detects the system language and can add numbers up to infinity. For now, the calculator only supports Belarusian, Turkish, Russian and English.
## Code review:
In this line, in the `current_lang` variable I have saved which language your system uses.
```py
current_lang, encoding = locale.getdefaultlocale()
```
----
Comparison. If the `current_lang` variable contains the information "ru_RU", the calculator will be in Russian.
```py
if current_lang == "ru_RU":
```
----
If the information is correct, a `while` loop is started, which will run until the variable `aboba_lox` contains the word "нет (no)".
```py
while aboba_lox != "Да" or aboba_lox != "да":
# code
    if aboba_lox == "Нет" or aboba_lox == "нет":
        break
```
----
Here, the `aboba` variable I store the expression that the user enters. This expression can be as much as 8723 + 234 * 32 / 2.
```py
aboba = input("Введите выражение: ")
```
----
Here goes another check to see if the user has entered the combination `/ 0` (`// 0` or `% 0`) into the variable `aboba`. If it turns out that such information is contained in the variable, the console will print the text "На ноль делить нельзя! (You cannot divide by zero!)".
```py
if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
    print("На ноль делить нельзя!")
```
----
Python stores the result of an expression in the `result` variable.
```py
result = numexpr.evaluate(aboba)
```
----
Output the result.
```py
print(f"Результат: {result}")
```
----
This is where I ask the user whether to continue running the calculator or not. If "да (yes)", the code will resume, if "нет (no)", the loop will end along with the rest of the code.
```py
print("Продолжить?")
aboba_lox = input()
if aboba_lox == "Нет" or aboba_lox == "нет":
    break
```
----
##### I don't know English well, so I used a translator to translate this text.
