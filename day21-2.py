import pygame
import datetime
import time

def set_alram(set_time):
    print(f"The alram time is {set_time}")
    alram=True
    file_music="C:/Users/Dell/Desktop/Python/iphone_alarm.mp3"
    while alram:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time==set_time:
            print("Lets goooo")
            pygame.mixer.init()
            pygame.mixer.music.load(file_music)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            alram=False
        time.sleep(1)  
        

if __name__=="__main__":
    set_time=input("Set the alram(HH:MM:SS):  ")
    set_alram(set_time)