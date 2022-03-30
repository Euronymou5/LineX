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
  key = "d7afce278cd44bdd33d25552bf9adb57"
  key1 = "a186ca602e0b2fce38730fbef1a8070b"
  key3 = "2c4547f4a4097632350d259f086e43a0"
  key4 = "8edc91f238d8f220bf3a2dc42214c397"
  key5 = "0d4e34fd0c7aa33ed22b73f0e1c345ad"
  print('[~] Ejemplo: 14158586273')
  numero = input('[~] Ingresa el numero de telefono: ')
  api = f"http://apilayer.net/api/validate?access_key={key}&number={numero}"
  try: 
    data = requests.get(api).json()
    if data['valid'] == False:
     print('\n[!] El numero no es valido!')
    else:
      print('\n[~] Numero: ', data['number'])
      print('[~] Codigo del pais: ', data['country_code'])
      print('[~] Nombre del pais: ', data['country_name'])
      print('[~] Ubicacion: ', data['location'])
      print('[~] Transportador: ', data['carrier'])
  except KeyError:
    try:
      api1 = f"http://apilayer.net/api/validate?access_key={key1}&number={numero}"
      data1 = requests.get(api1).json()
      if data1['valid'] == False:
       print('\n[!] El numero no es valido!')
      else:
        print('\n[~] Numero: ', data1['number'])
        print('[~] Codigo del pais: ', data1['country_code'])
        print('[~] Nombre del pais: ', data1['country_name'])
        print('[~] Ubicacion: ', data1['location'])
        print('[~] Transportador: ', data1['carrier'])
    except KeyError:
      try:
       api3 = f"http://apilayer.net/api/validate?access_key={key3}&number={numero}"
       data3 = requests.get(api3).json()
       if data3['valid'] == False:
        print('\n[!] El numero no es valido!')
       else:
         print('\n[~] Numero: ', data3['number'])
         print('[~] Codigo del pais: ', data3['country_code'])
         print('[~] Nombre del pais: ', data3['country_name'])
         print('[~] Ubicacion: ', data3['location'])
         print('[~] Transportador: ', data3['carrier'])
      except KeyError:
        try:
           api4 = f"http://apilayer.net/api/validate?access_key={key4}&number={numero}"
           data4 = requests.get(api4).json()
           if data4['valid'] == False:
             print('\n[!] El numero no es valido!')
           else:
             print('\n[~] Numero: ', data4['number'])
             print('[~] Codigo del pais: ', data4['country_code'])
             print('[~] Nombre del pais: ', data4['country_name'])
             print('[~] Ubicacion: ', data4['location'])
             print('[~] Transportador: ', data4['carrier'])
        except KeyError:
          try:
           api5 = f"http://apilayer.net/api/validate?access_key={key5}&number={numero}"
           data5 = requests.get(api5).json()
           if data5['valid'] == False:
             print('\n[!] El numero no es valido!')
           else:
             print('\n[~] Numero: ', data5['number'])
             print('[~] Codigo del pais: ', data5['country_code'])
             print('[~] Nombre del pais: ', data5['country_name'])
             print('[~] Ubicacion: ', data5['location'])
             print('[~] Transportador: ', data5['carrier'])
          except KeyError:
            print('\n[!] APIs agotadas debes esperar a que sean actualizadas')
      
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
