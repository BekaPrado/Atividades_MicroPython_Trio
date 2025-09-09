from machine import Pin, time_pulse_us
import time

trig = Pin(25, Pin.OUT)
echo = Pin(27, Pin.IN)
led = Pin(26, Pin.OUT)

def medir():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)


    
    duracao = time_pulse_us(echo, 1, 30000)
    return (duracao / 2) * 0.0343

contagem = 0

while True:
    distancia = medir()
    print("Distância:", distancia, "cm")

    if distancia <= 10:
        contagem += 1
        print("Movimento detectado! Contagem:", contagem)
        time.sleep(1)
    else:
        print("Nenhum movimento.")

    if contagem >= 10:
        print("LIMITE DE MOVIMENTOS! LED ACESO.")
        led.value(1)
        time.sleep(5)
        led.value(0)
        contagem = 0

    time.sleep(3)
