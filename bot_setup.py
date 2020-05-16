# Временное решение
# TODO: Реализовать более удобное хранение токена (в переменных окружения, например)
import json
import requests

# Функция проверки токена бота
def check(token):
	try:
		url = f"https://api.telegram.org/bot{token}/getMe"
		req = requests.get(url)
		response = req.json()

		if response['ok'] == False:
			print(f"Не удалось авторизировать бота; Ошибка: {response['description']}")
			return False
		else:
			print(f"Бот авторизирован; Имя бота: {response['result']['first_name']}")
			return True

	except Exception as ex:
		print(f"Не удалось выполнить запрос на авторизацию бота; Ошибка: {str(ex)}")
		return False

# -------------------------------------------------
token = input("Введите токен: ")
token = str(token)


# Проверка токена
result = check(token)
if not result:
	while True:
		q = input("Токен не прошёл проверку. Вы хотите продолжить? (Y/n)")
		if str(q).lower() == 'n':
			exit
		elif str(q).lower() == 'y':
			break


data = {
	'API_TOKEN': token
}

json_str = json.dumps(data)
try:
	f = open('config.json', 'w')
	f.write(json_str)
	f.close()
	print("Токен успешно сохранён!")
except Exception as ex:
	print(f'Не удалось записать токен в файл; Ошибка: {str(ex)}')