import json
import requests
import os
import time

logo = """\033[34m ▄▀▀▀▀▄     ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄ 
█    █     █   █  █  █  █ █ █ ▐  ▄▀   ▐ █    █   █ 
▐    █     ▐   █  ▐  ▐  █  ▀█   █▄▄▄▄▄  ▐     ▀▄▀  
    █          █       █   █    █    ▌       ▄▀ █  
  ▄▀▄▄▄▄▄▄▀ ▄▀▀▀▀▀▄  ▄▀   █    ▄▀▄▄▄▄       █  ▄▀  
  █        █       █ █    ▐    █    ▐     ▄▀  ▄▀   
  ▐        ▐       ▐ ▐         ▐         █    ▐   """

def info():
  os.system("clear")
  print(logo)
  key = "d0f8d48fb6cccba08753c1ed51fffae5"
  print('[~] Ejemplo: 14158586273')
  numero = input('[~] Ingresa el numero de telefono: ')
  api = f"http://apilayer.net/api/validate?access_key={key}&number={numero}"
  data = requests.get(api).json()
  print('\n[~] Numero: ', data['number'])
  print('[~] Codigo del pais: ', data['country_code'])
  print('[~] Nombre del pais: ', data['country_name'])
  print('[~] Ubicacion: ', data['location'])
  print('[~] Transportador: ', data['carrier'])
  

def menu():
  os.system("clear")
  print(logo)
  print('\n[1] Buscar informacion de un numero')
  print('[99] Salir')
  T = int(input('\n>> '))
  if T == 1:
    info()
  elif T == 99:
    exit()
  else:
    print('Error.')
    time.sleep(1)
    menu()

menu()
