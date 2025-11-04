def my_function():
  # Оголошую функцію без заздалегідь заданих аргументів
  print("Enter the first number")
  # виводимо повідомлення на екран
  num1 = float(input())
  # запитуємо введення першого числа та перетворюємо його у десяткове
  print("Enter the second number")
  num2 = int(input())
  # запитуємо введення другого числа та перетворюємо його у ціле
  print (f"Result of addition: {num1 + num2}")
  # Використовуємо f-string для виводу суми чисел з текстом. Мені не дуже подобається, бо я про неї забуваю
  print ("Result of multiplication: ", num1 * num2)
  # Використовую кому для виводу декілької аргументів через прінт.
  print("Result of division: ", round(num1 / num2, 3))
  # Округлюю значення після ділення і залишаю 3 знаки після коми.

my_function()
# Викликаю функцію.