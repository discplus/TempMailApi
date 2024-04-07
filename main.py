import requests
import json
from colorama import init, Fore
import random
import string
import time
import os

init()

print(Fore.CYAN + "Программа разработана discplus.")
print("Ссылка на GitHub: https://github.com/discplus")
print("Ссылка на файл: https://github.com/discplus/TempMailApi")
for x in range(5):
    print()




while True:

  def create_email():
    url = 'https://api.mail.tm/accounts'
    headers = {'accept': 'application/ld+json', 'Content-Type': 'application/json'}

    with open('baza.txt', 'a') as f:
      for _ in range(8):

        email_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

        email_name += ''.join(random.choice(string.digits) for _ in range(2))
        email_name += '@awgarstone.com'

        password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))

        data = {
                'address': email_name,
                'password': password
               }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
          f.write(f'{data["address"]} | {data["password"]}\n')


          f.flush()
          os.fsync(f.fileno())
          print("Почтовый ящик успешно создался!")
        else:
          print('Произошла ошибка при создании почтового ящика.')

        time.sleep(1/8)  

  create_email()
