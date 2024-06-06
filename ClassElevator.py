import pygame
import queue
import time

BLACK = (0, 0, 0)

window_width, window_heigh = 1024, 633
size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("elevator")

building_floor = 570
floor_heit = 51
f_heit_line = 57

img_elv = 'WhatsApp Image 2024-05-29 at 18.33.11.jpeg'
img2 = pygame.image.load(img_elv).convert()

class Elevator():
    def __init__(self, num):
        self.__current_floor = building_floor
        self.__till_available = 0
        self.__queue = queue.Queue()
        self.__num = num
        self.__t_end = 0
        self.__dst = self.__current_floor

    def black_button(self, num_floor):
        for i in range (num_floor + 1) :
            y = building_floor - i * floor_heit + 20
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (BLACK))
        screen.blit(number, (300, y))

    def black_button(self, num_floor):
        for i in range (num_floor + 1) :
            y = building_floor - i * floor_heit + 20
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (BLACK))
        screen.blit(number, (300, y))


    def update(self):
        t_start = time.perf_counter()
        if t_start - self.__t_end >= 2:
            if self.__queue.qsize() > 0:
                next_floor  = self.__queue.queue[0]
                dst = building_floor - next_floor * floor_heit 
                if dst != self.__current_floor:
                    diff = dst - self.__current_floor 
                    direction  = diff / abs(diff)
                    self.__current_floor += direction * 1
                    x = 395 + self.__num * f_heit_line
                    screen.blit(img2,(x, self.__current_floor))
                if dst == self.__current_floor:
                    self.__queue.get()
                    pygame.mixer.music.load("ding.mp3")
                    pygame.mixer.music.play()
                    self.black_button(next_floor)
                    self.__t_end = time.perf_counter()
           


    def get_current_floor(self):
        return self.__current_floor
    
    def get_dst(self):
        return self.__dst
    
    def set_dst(self, new_floor):
        self.__dst = new_floor
    
    def set_current_floor(self, new_y):
        self.__current_floor = new_y

    def set_num(self, num_elv):
        self.__num = num_elv

    def get_till_available(self):
        return self.__till_available
    
    def set_till_available(self, timer):
        self.__till_available = timer
    
    def put_queue(self, item):
        self.__queue.put(item)

   