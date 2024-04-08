import os
import math
import time
import datetime
import keyboard
from scipy.integrate import quad as integral

os.system('cls' if os.name == 'nt' else 'clear')

A = .01 #m
f = 50*2 #Hz

T = 1/f #s
w = 2*math.pi*f #rad/s

bioshaker = 'bioshaker'

masa_max = 100 #kg

i = 0

name = input('ingrese su nombre: ')
os.system('cls' if os.name == 'nt' else 'clear')
print('bienvenid@ ', name, ', usted está usando el ', bioshaker, ' 1.0.0\n')

def masa():

    global masa_max, bioshaker

    m = input('ingrese su masa en kg: ')
    print('')

    try:

        m = float(m)
        if(m>masa_max):

            os.system('cls' if os.name == 'nt' else 'clear')
            print('el ', bioshaker, ' 1.0.0 no es capaz de soportar tanto peso')
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

def tin():

    t = input('ingrese el tiempo de uso del bioshaker en segundos: ')
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

    calorias = input('ingrese las calorias que desea quemar en cal: ')
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

    print('modos disponibles para el ', bioshaker, ' 1.0.0:\n')

    print('default: calcula las calorías quemadas según su peso en un cierto periodo de tiempo')
    print('peso ideal: calcula el tiempo a utilizar el ', bioshaker, ' 1.0.0 para llegar a su peso "ideal" según su peso')
    print('calorías: calcula el tiempo a utilizar el ', bioshaker, ' 1.0.0 para llegar a quemar las calorías que desee según su peso')
    print('temporizador: ingresa su peso cuando empece a usar el ', bioshaker, ' 1.0.0 y cuando usted indique que ha terminado de usarlo se le informará de las calorías que ha quemado\n')

    mode = input('por favor escriba el modo a usar\n')
    print('')
    os.system('cls' if os.name == 'nt' else 'clear')
    modo(mode)

def modo(mode):

    if(mode=='default'):

        m = masa()
        t = tin()

        print('en ', t, ' segundos, usted quemará ', cal(t, m), ' calorias\n')
        temp(t, m)

    elif(mode=='peso ideal'):

        m = masa()
        ideal = inideal(m)

        os.system('cls' if os.name == 'nt' else 'clear')
        get_time(cal((m - ideal)*7700, m), m)

    elif(mode=='calorías'):

        m = masa()
        calorias = calo()

        os.system('cls' if os.name == 'nt' else 'clear')
        get_time(cal(calorias, m), m)

    elif(mode=='temporizador'):

        print('cinco segundos antes de empezar')

        m = masa()

        time.sleep(5)
        i = time.time()

        input('envie cualquier carácter cuando termine su ejercicio...\n')
        print('')
        print('usted ha quemado ',cal(time.time()-i, m), ' calorías')
        end()

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

        print('')
        print('rendirse no está mal, presione "n" si quiere parar...\n')

        i = time.time()

        while((time.time()-i<t) and not (keyboard.is_pressed('n'))):
            
            a = 1

        if(cal(time.time()-i, m)<0):

            calc = 0

        else:

            calc = cal(time.time()-i, m)

        print('has quemado ', calc, ' calorias, que gran trabajo!!\n')
        
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

        print('muchas gracias por usar l ', bioshaker, ' 1.0.0, espero que regrese pronto :)')

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
    
    return(s(t, m)*(1/4.184))

def get_time(s, m):
    
    sec = datetime.timedelta(seconds=s)
    d = datetime.datetime(1,1,1) + sec
    print('(días:horas:minutos:segundos)')
    print('%d:%d:%d:%d\n' % (d.day-1, d.hour, d.minute, d.second))
    temp(s, m)

iniciar()