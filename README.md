# LineX

### ¿Qué es LineX?

• R= LineX es una herramienta para obtener datos de un numero de teléfono utilizando la API de Numverify

• Con soporte para 232 Países

## Configuracion
Antes de utilizarlo, es necesario configurar algunas la clave api de [Numverify](https://numverify.com).

Una vez obtenida nuestra clave API, es necesario colocar cada una en orden en el archivo  `keys.json`  de la siguiente forma:

```json
{
   "key": "ReemplazarPorApikeyNumverify"
}
```

## Instalación y uso
Clonamos el repositorio
```
git clone https://github.com/Euronymou5/LineX.git
```
Instalamos dependencias
```
pip install -r requirements.txt
```
Iniciamos la herramienta
```
python3 linex.py -numero <numero>
```
Ejemplo
```
python3 linex.py -numero +14158586273
```

## Actualización
**v2.0**

 1. Se optimizaron unas partes del código.
    
 2.  Se agrego el modulo 'argparser' para utilizar argumentos en el
        script y evitar demasiadas lineas de codigo para agregar el numero
        de teléfono y evitar un menú innecesario.

### Nota

Esta será probablemente la última actualización que recibirá Linex. Si deseas utilizar una versión más actualizada, te recomiendo utilizar mi nuevo proyecto: [Dark-Hydro](https://github.com/Euronymou5/Dark-Hydro).

## Testeado en:

![android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)

![debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)

![windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


## 🌐 Contacto 🌐
[![discord](https://img.shields.io/badge/Discord-euronymou5-a?style=plastic&logo=discord&logoColor=white&labelColor=black&color=7289DA)](https://discord.com/users/452720652500205579)

![email](https://img.shields.io/badge/ProtonMail-mr.euron%40proton.me-a?style=plastic&logo=protonmail&logoColor=white&labelColor=black&color=8B89CC)

[![Twitter](https://img.shields.io/badge/Twitter-@Euronymou51-a?style=plastic&logo=twitter&logoColor=white&labelColor=black&color=1DA1F2)](https://twitter.com/Euronymou51)
