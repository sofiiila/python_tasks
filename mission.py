import time
import random
from datetime import datetime

def endless_cycle():
    variable = 0
    while True:  # бесконечный цикл
        variable += 1  # измените вычисление в соответствии с вашими потребностями
        print('Current variable value:', variable)
        print(abs(calc_min_angle(*parse_time(get_current_time()))))
        angle = abs(calc_min_angle(*parse_time(get_current_time())))
        print(angle)
        if angle > 90:
            for _ in range(5):
                print('Ку-ка-реку', end=' ')
        elif 150 < angle < 180:
            for _ in range(10):
                print("хрю-хрю", end=" ")
        else:
            print("пук" * 3)

        time.sleep(variable_value(value_massive=range(1, 4)))  # пауза на случайное время в интервале от 1 до 3 секунд

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    
def parse_time(current_time: str):
    _, minutes, seconds = current_time.split(":")
    return (int(minutes), int(seconds))



def calc_min_angle(minutes, seconds):
    angle = (minutes - seconds) * 6 
    if angle < 180:
        return angle
    else:
        return 360 - angle


def variable_value(value_massive: list[int]) -> int:
    return random.choice(value_massive) 

def main() -> None:
    endless_cycle()

if __name__ == "__main__":
    main()