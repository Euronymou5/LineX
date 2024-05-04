import json
import requests
import os
import time
import argparse
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument("-numero", type=str, required=True, help="Añadir numero de telefono")
args = parser.parse_args()

logo = f"""{Fore.BLUE}▄▀▀▀▀▄     ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄ 
█    █     █   █  █  █  █ █ █ ▐  ▄▀   ▐ █    █   █ 
▐    █     ▐   █  ▐  ▐  █  ▀█   █▄▄▄▄▄  ▐     ▀▄▀  
    █          █       █   █    █    ▌       ▄▀ █  
  ▄▀▄▄▄▄▄▄▀ ▄▀▀▀▀▀▄  ▄▀   █    ▄▀▄▄▄▄       █  ▄▀  
  █        █       █ █    ▐    █    ▐     ▄▀  ▄▀   
  ▐        ▐       ▐ ▐         ▐         █    ▐"""

with open('keys.json', 'r') as configuracion:
  configuracion_dat = json.load(configuracion)

def info():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

  numero = args.numero
  print(logo)
  print(f'{Fore.YELLOW}\n[~] Escaneando: {numero}...')
  time.sleep(2)

  payload = {}
  headers = {
    "apikey": configuracion_dat['key']
  }
  api = f"https://api.apilayer.com/number_verification/validate?number={numero}"
  try: 
    data = requests.request("GET", api, headers=headers, data = payload).json()
    if data['valid'] == False:
     print(f'{Fore.RED}\n[!] El numero no es valido!')
    else:
      print(f'{Fore.GREEN}\n[~] Numero: ', data['number'])
      print('[~] Codigo del pais: ', data['country_code'])
      print('[~] Nombre del pais: ', data['country_name'])
      print('[~] Ubicacion: ', data['location'])
      print('[~] Transportador: ', data['carrier'])
  except Exception as e:
        print(f'{Fore.RED}\n[!] Ocurrio un error: {e}')
        exit()

if __name__ == "__main__":
  info()
