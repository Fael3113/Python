#Programinha para "floodar" frases para amigos (não faça isso com estranhos)

import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ["Para de mandar esses links", "Nao aguento mais"]

for i in range(50):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press("Enter")