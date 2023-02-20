#必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート
import sys                          #sysモジュールをインポート

#ポート番号の定義
Servo_pin = 18                      #変数"Servo_pin"に18を格納
Servo_pin1 = 23

#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Servo_pin, GPIO.OUT)     #GPIO18を出力モードに設定
GPIO.setup(Servo_pin1, GPIO.OUT)

#PWMの設定
#サーボモータSG90の周波数は50[Hz]
Servo = GPIO.PWM(Servo_pin, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo1 = GPIO.PWM(Servo_pin1, 50)

Servo.start(0)                      #Servo.start(デューティ比[0-100%])
Servo1.start(0)

#角度からデューティ比を求める関数
def servo_angle(Servo_t, angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo_t.ChangeDutyCycle(duty)     #デューティ比を変更

#while文で無限ループ
#サーボモータの角度をデューティ比で制御
#Servo.ChangeDutyCycle(デューティ比[0-100%])
while True:
    try:
        servo_angle(Servo,90)
        servo_angle(Servo1,-90)
        time.sleep(3)
        servo_angle(Servo, -90)
        servo_angle(Servo1, 90)
        time.sleep(3)
    except KeyboardInterrupt:          #Ctrl+Cキーが押された
        Servo.stop()                   #サーボモータをストップ
        Servo1.stop()
        GPIO.cleanup()                 #GPIOをクリーンアップ
        sys.exit()                     #プログラムを終了
