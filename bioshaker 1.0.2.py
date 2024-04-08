import os
import math
import time
import datetime
import keyboard
from scipy.integrate import quad as integral
#1.2.0 ---> datos globlales, cuidado de masa, meses
os.system('cls' if os.name == 'nt' else 'clear')

A = .01 #m
f = 50*2 #Hz

T = 1/f #s
w = 2*math.pi*f #rad/s

bioshaker = 'bioshaker 1.1.0'

masa_max = 100 #kg

i = 0

gers = [60.9, 22.7, 17.5, 5.3, 11.6, 13.5, 61.0, 22.5, 12.2, 14.7, 14.7 ,10.5]
gersumrest = [-54, 495, 651, 679, 879, 487, -51, 499, 746, 496, 746, 596]
fxa = [1.3, 1.3, 1.6, 1.5, 1.7, 1.6, 2.1, 1.9, 2.4, 2.2]

def masa():

    global masa_max, bioshaker

    m = input('ingrese su masa en kg: ')
    print('')

    try:

        m = float(m)
        if(m>masa_max):

            os.system('cls' if os.name == 'nt' else 'clear')
            print('el ', bioshaker, ' no es capaz de soportar tanto peso')
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return(masa())
        
        return(m)
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(masa())

def edad():

    e = input('ingrese su edad en años: ')
    print('')

    try:

        e = float(e)
        return(e)
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(edad())

def af():

    global name

    a = input(f'en una escala del 1 al 5 donde el 1 es actividad física muy leve y 5 es excepcional, ¿dónde se encuentra, {name}? (unícamente ingrese el número): ')
    print('')

    try:

        a = int(a)

        if((a==1) or (a==2) or (a==3) or (a==4) or (a==5)):

            return(a)
        
        else:

            os.system('cls' if os.name == 'nt' else 'clear')
            print('por favor ingrese un número válido (1, 2, 3, 4 o 5)...')
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return(af())
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido (1, 2, 3, 4 o 5)...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(af())

def sexo():

    s = input('ingrese su sexo biológico ("femenino"/"masculino"): ')
    print('')

    if(s=='femenino') or (s=='masculino'):

        return(s)
        
    else:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un valor válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(sexo())

def tin():

    t = input(f'ingrese el tiempo de uso de {bioshaker} en segundos: ')
    print('')

    try:

        t = float(t)
        return(t)
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(tin())

def inideal(m):

    ideal = input('ingrese su peso "ideal" en kg: ')
    print('')

    try:

        ideal = float(ideal)
        if(ideal>m):
                        
            os.system('cls' if os.name == 'nt' else 'clear')
            print('su peso "ideal" debe ser menor a su masa actual')
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return(inideal(m))
    
        return(ideal)
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(inideal())

def calo():

    calorias = input('ingrese las calorías que desea quemar en cal: ')
    print('')

    try:

        calorias = float(calorias)
        return(calorias)
    
    except ValueError:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese un número válido...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(calo())
 
def iniciar():

    print('modos disponibles para el ', bioshaker, ':\n')

    print('default: calcula las calorías quemadas según su peso en un cierto periodo de tiempo')
    print('')
    print('peso ideal: calcula el tiempo a utilizar el ', bioshaker, ' para llegar a su peso "ideal" según su peso')
    print('')
    print('calorías: calcula el tiempo a utilizar el ', bioshaker, ' para llegar a quemar las calorías que desee según su peso')
    print('')
    print('temporizador: ingresa su peso cuando empece a usar el ', bioshaker, ' y cuando usted indique que ha terminado de usarlo se le informará de las calorías que ha quemado\n')
    print('')
    print('c: cancelar y cerrar\n')
    print('')

    mode = input('por favor escriba el modo a usar: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    modo(mode)

def modo(mode):

    global bioshaker

    if(mode=='default'):

        m = masa()
        t = tin()

        print('en ', t, ' segundos, usted quemará ', cal(t, m, 0), ' calorías\n')
        temp(t, m)

    elif(mode=='peso ideal'):

        m = masa()
        ideal = inideal(m)

        os.system('cls' if os.name == 'nt' else 'clear')
        get_time(cal((m - ideal)*3500, m, 1), 1, m)

    elif(mode=='calorías'):

        m = masa()
        calorias = calo()

        os.system('cls' if os.name == 'nt' else 'clear')
        get_time(cal(calorias, m, 1), 1, m)

    elif(mode=='temporizador'):

        print('cinco segundos antes de empezar')

        m = masa()

        time.sleep(5)
        i = time.time()

        input('envie cualquier carácter cuando termine su ejercicio...\n')
        print('')
        print('usted ha quemado ',cal(time.time()-i, m, 0), ' calorías')
        end()

    elif(mode=='c'):
        print('muchas gracias por usar el ', bioshaker, ', espero que regrese pronto :)')
        return

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('tiene que escribir el nombre del modo tal cual está indicado en la lista...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        iniciar()

def temp(t , m):

    global bioshaker

    f = input('¿desea iniciar su ejercicio con el tiempo indicado? (sí/no) \n')

    if(f=='sí'):

        i = time.time()
        s = t

        while((time.time()-i<t) and not (keyboard.is_pressed('n'))):
            
            contador(s)

        print('has gastado ', cal(time.time()-i, m, 0), ' calorías, que gran trabajo!!\n')
        
        end()

    elif(f=='no'):

        end()

    else:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('indique "sí" o "no" por favor...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        temp(t, m)

def x(t):

    return(A*math.sin(w*t))

def end():
    
    global bioshaker

    time.sleep(2)
    d = input('envia "sí" si deseas continuar con otros modos, envia "no" de lo contrario\n')
        
    if(d=='sí'):

        os.system('cls' if os.name == 'nt' else 'clear')

        iniciar()

    elif(d=='no'):

        print('muchas gracias por usar el ', bioshaker, ', espero que regrese pronto :)')

    else:
                
        os.system('cls' if os.name == 'nt' else 'clear')
        print('por favor ingrese "sí" o "no"...')
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return(end())

def v(t):

    return(w*A*math.cos(w*t))

def Ec(m):

    return((1/2)*m*((2*(integral(v, 0, T/4)[0]))**2))

def s(t, m):

    return((t*Ec(m))/(T/2))

def cal(t, m, i):

    global actividad

    if(i==1):
        if(t>(get_get(m))):
            print(f'gastar más de {round(get_get(m), 2)} calorías al día por actividad física puede ser perjudicial para tu salud!!\n')
        return(round(s(t, m)*(1/4.184)*50, 2))
    else:
        if(t>15000) and (actividad<=2):
            print(f'por tu actividad física, no es recomendable que pases {round(t/3600, 2)} horas haciendo ejercicio\n')
        if(t>21600) and (actividad==3 or actividad==4):
            print(f'por tu actividad física, no es recomendable que pases {round(t/3600, 2)} horas haciendo ejercicio\n')
        return(round(s(t, m)*(1/4.184)/50, 2))

def get_time(s, t, *arg):
    
    if(t==1):
        
        sec = datetime.timedelta(seconds=s)
        d = datetime.datetime(1,1,1) + sec
        print('(días:horas:minutos:segundos)')
        print('%d:%d:%d:%d\n' % (d.day-1, d.hour, d.minute, d.second))
        temp(s, *arg)
    
    else:

        sec = datetime.timedelta(seconds=s)
        d = datetime.datetime(1,1,1) + sec
        print('(días:horas:minutos:segundos)')
        print('%d:%d:%d:%d\n' % (d.day-1, d.hour, d.minute, d.second))

def contador(s):

    while(s>0 and not (keyboard.is_pressed('n'))):
        print('')
        print('rendirse no está mal, deje presionado "n" si quiere parar...\n')
        print('')
        print("tiempo restante: ")
        get_time(s, 0)
        time.sleep(1)
        s -= 1
        os.system('cls' if os.name == 'nt' else 'clear')

def get_get(m):

    global name, edad0, sexo0, actividad, gers, gersumrest, fxa

    if(sexo0=='masculino'):

        if((edad0>=3)):
            ger = (gers[0]*m)+gers[0]
        if((edad0>3) and (edad0<=10)):
            ger = (gers[1]*m)+gers[1]
        if((edad0>10) and (edad0<=18)):
            ger = (gers[2]*m)+gers[2] 
        if((edad0>18) and (edad0<=30)):
            ger = (gers[3]*m)+gers[3]
        if((edad0>30) and (edad0<=60)):
            ger = (gers[4]*m)+gers[4]
        if((edad0>60)):
            ger = (gers[5]*m)+gers[5]
        
        if(actividad==1):
            get = ger*fxa[0]
        if(actividad==2):
            get = ger*fxa[2]
        if(actividad==3):
            get = ger*fxa[4]
        if(actividad==4):
            get = ger*fxa[6]
        if(actividad==5):
            get = ger*fxa[8]

    elif(sexo0=='femenino'):

        if((edad0>=3)):
            ger = (gers[6]*m)+gers[6]
        if((edad0>3) and (edad0<=10)):
            ger = (gers[7]*m)+gers[7]
        if((edad0>10) and (edad0<=18)):
            ger = (gers[8]*m)+gers[8] 
        if((edad0>18) and (edad0<=30)):
            ger = (gers[9]*m)+gers[9]
        if((edad0>30) and (edad0<=60)):
            ger = (gers[10]*m)+gers[10]
        if((edad0>60)):
            ger = (gers[11]*m)+gers[11]

        if(actividad==1):
            get = ger*fxa[1]
        if(actividad==2):
            get = ger*fxa[3]
        if(actividad==3):
            get = ger*fxa[5]
        if(actividad==4):
            get = ger*fxa[7]
        if(actividad==5):
            get = ger*fxa[9]

    return(get-ger)

print('permitanos que le conozcamos mejor :)\n')
print('')
name = input('ingrese su nombre: ')
print('')
edad0 = edad()
sexo0 = sexo()
actividad = af()
os.system('cls' if os.name == 'nt' else 'clear')
if(sexo0=='masculino'):
    print('bienvenido ', name, ', usted está usando el ', bioshaker, '\n')
else:
    print('bienvenida ', name, ', usted está usando el ', bioshaker, '\n')

iniciar()