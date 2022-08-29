
from time import sleep
import pyautogui, webbrowser

numero = input ('numero ')
mensaje = input ('mensaje a enviar ')

webbrowser.open('https://web.whatsapp.com/send?phone='+numero)

sleep(15)

for i in range(30):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')