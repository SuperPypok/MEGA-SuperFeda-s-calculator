# MEGA SuperFeda's calculator 228

<details>
<summary>English translate</summary> 

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

</details>

<details>
<summary>Русский перевод</summary>
    
## About:
Калькулятор который может складывать числа до бесконечности, имеет защиту от идиотов которые хотят делить на ноль и который может сам определить язык системы и подстроиться под него.
## Code review:
В этой линии, в переменную `current_lang` я сохранил информацию о языке, который в данный момент используется ОС.
```py
current_lang, encoding = locale.getdefaultlocale()
```
----
Сравнение. Если данные в `current_lang` = "ru_RU", то калькулятор будет на русском языке.
```py
if current_lang == "ru_RU":
```
----
Если информация верна, запускается цикл "`while`", который будет выполняться до тех пор, пока переменная "`aboba_lox`" не будет содержать слово "нет".
```py
while aboba_lox != "Да" or aboba_lox != "да":
# code
    if aboba_lox == "Нет" or aboba_lox == "нет":
        break
```
----
Здесь в переменной "`aboba`" я храню выражение, которое вводит пользователь. Это выражение может быть таким: 8723 + 234 * 32 / 2 или любым другим.
```py
aboba = input("Введите выражение: ")
```
----
Здесь идет очередная проверка, не ввел ли пользователь в переменную "`aboba`" комбинацию "`/ 0`" (`// 0` или `% 0`). Если окажется, что такая информация содержится в переменной, то в консоль будет выведен текст "На ноль делить нельзя!".
```py
if "// 0" in aboba or "/ 0" in aboba or "% 0" in aboba:
    print("На ноль делить нельзя!")
```
----
Здесь Python сохранил результат выражения из переменной "`aboba`" в "`result`".
```py
result = numexpr.evaluate(aboba)
```
----
Вывод результата.
```py
print(f"Результат: {result}")
```
----
Здесь я спрашиваю пользователя, продолжать ли работу калькулятора или нет. Если "да", код возобновится, если "нет", то цикл завершится вместе с остальной частью кода.
```py
print("Продолжить?")
aboba_lox = input()
if aboba_lox == "Нет" or aboba_lox == "нет":
    break
```

</details>
