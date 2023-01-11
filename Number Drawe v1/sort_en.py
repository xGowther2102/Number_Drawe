''' (ES) Recuerda tener todos los imports instalados''' ''' '''
''' (EN) Remember to have all imports installed'''

from progress.bar import Bar, ChargingBar
import os, time, random
import random
from colorama import init
from termcolor import colored
import time
init()
sorteo = list()
cant = 1

''' Puedes cambiar la descripcion en 'premio'/ You can change the description in 'premio' '''

print(colored('===============================================================================', 'green'))
premio = input(colored('||Prize name: ', 'yellow'))
print(colored('===============================================================================', 'green'))

''' Recuerda que "time.sleep()" es para retraso para la siguiente ejecución / Remember that "time.sleep()" is for delay for the next execution '''

espera = time.sleep(1)
while cant > 0:
    numero = random.randrange(1,250) #Rango de numeros ya sea 10 boletos o 100 / Number range either 10 tickets or 100
    if numero not in sorteo:
        sorteo.append(numero)
        cant-=1
        os.system('cls') #Para borrar todo de la pantalla / To clear everything from the screen

''' El 'colored' es para dar colores a los textos, ejemplo: colored("text","color") / 
The 'colored' is to give colors to the texts, example: colored("text","color")'''

print(colored('The winning number will be displayed in less than 2 minutes', 'cyan')) # Tiempo Aproximado, usted puede cambiar la descripcion / Approximate time, you can change the description
os.system('cls')
print(colored('===============================================================================', 'green'))
time.sleep(2)
#Barra de progreso 1 / Progress bar 1
bar1 = ChargingBar(colored('Looking for Winning Number:','yellow'), max=100)#Puedes cambiar la descripcion y color de la letra / You can change the description and color of the letter
for num in range(100):
    time.sleep(random.uniform(0, 0.20))#(*, 0.20) Es el tiempo que tardara en llenarse la barra, puedes modificarlo / (*, 0.20) It is the time it will take to fill the bar, you can modify it
    bar1.next()
bar1.finish()
print(colored('===============================================================================', 'green'))
time.sleep(2)
os.system('cls')
print(colored('===============================================================================', 'green'))
time.sleep(2)
#Barra de progreso 2 / Progress bar 2
bar2 = ChargingBar(colored('Finalizing:','yellow'), max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.10))
    bar2.next()
bar2.finish()
print(colored('===============================================================================', 'green'))
time.sleep(2)
os.system('cls')
print(colored('===============================================================================', 'green'))
time.sleep(2)
#Barra de progreso 3 / Progress bar 3
bar3 = ChargingBar(colored('Showing Winning Number:', 'yellow') , max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.05))
    bar3.next()
bar3.finish()
print(colored('===============================================================================', 'green'))
time.sleep(2)
os.system('cls')
print(colored('===============================================================================', 'green'))
time.sleep(2.5)
print('Number: ')
time.sleep(2.5)
print(colored('***', 'red'))
time.sleep(2.5)
#Muestra el numero ganador / show the winning number
print('Winning Number:', colored(sorteo,'red'))
time.sleep(2.5)
#Insertar Nombre del Ganador / insert the name of the winner
Ganador = input(colored('||Winners Name: ', 'yellow'))

time.sleep(2.5)

print('Prize: ', colored(premio, 'red')) #Muestra el premio / show the reward
time.sleep(2.5)
os.system('cls')
#Muestra Nombre, Numero y premio / displays name, number and award
print(colored('===============================================================================', 'green'))
print('||¡Congratulations ', colored(Ganador,'cyan'), '-')
print('with number:',  colored(sorteo,'cyan'), ". you have won a:", colored(premio, 'cyan'))
time.sleep(2)
#Agradecimientos a los que participaron, puedes modificarlo o eliminarlo / Thanking those who participated, you can modify or delete it
print(colored('===============================================================================', 'green'))
time.sleep(2)
print(colored('==============================================================================='
     "\n"'||                      ¡Thank you all for participating!                    ||'
      "\n"'===============================================================================', 'white', 'on_red'))
time.sleep(3)
#Proximo sorteo(solo es relleno, ya saben que hacer xD) / Next giveaway (it's just filler, you know what to do xD)
print(colored('===============================================================================', 'green'))
print(" ")
time.sleep(3)
print(colored("\n" ' :-) ', 'cyan'))
print(" ")
time.sleep(3)
print(colored('===============================================================================', 'green'))
time.sleep(10)
os.system('cls')


'''Recuerda no ser malo y recomendar este sorteador de python con tus amigos y conocidos...'''
'''Remember not to be mean and recommend this python sorter to your friends and acquaintances...'''

# 

#Creditos / Credits
import emoji
time.sleep(5)
print('Script- (ES) HECHO POR / (EN) MADE BY \U0001f60e= ') ,time.sleep(1.1),print(colored('E','green')), time.sleep(1.1),print(colored('d','blue')),time.sleep(1.1),print(colored('w','red')),
time.sleep(1.1),print(colored('i','white')),time.sleep(1.1),print(colored('n','yellow')),time.sleep(1.1),print(colored('H','cyan')),time.sleep(1.1),print(colored('P','magenta'))
time.sleep(1.5),print("\u2764\uFE0F")

print(colored('My github','blue'))

print(colored('https://github.com/xGowther2102/','green'))

time.sleep(15)
os.system('cls')