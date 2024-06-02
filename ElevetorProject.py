import pygame
import queue
import numpy
import sys

pygame.init()

WHITE = (245, 245, 245)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
# GREY = 


window_width, window_heigh = 1024, 633
size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("elevator")
screen.fill(WHITE)
pygame.display.flip()

img_bld = 'WhatsApp Image 2024-05-30 at 09.15.01.jpeg'
img1 = pygame.image.load(img_bld).convert()
# screen.blit(img1,(20, 613))
pygame.display.flip()

img_elv = 'WhatsApp Image 2024-05-29 at 18.33.11.jpeg'
img2 = pygame.image.load(img_elv).convert()


img_screen = 'WhatsApp Image 2024-05-30 at 09.59.45.jpg'
img3 = pygame.image.load(img_screen).convert()
# screen.blit(img3,(200, 100))
pygame.display.flip()


clock = pygame.time.Clock()
REFRESH_RATE = 60

building_floor = 570
floor_heit = 51
f_heit_line = 58


class Elevator():
    def __init__(self, num):
        self.__current_floor = building_floor
        self.__till_available = 0
        self.__queue = queue.Queue()
        self.__num = num

    def get_current_floor(self):
        return self.__current_floor
    
    def set_current_floor(self, new_y):
        self.__current_floor = new_y

    def get_till_available(self):
        return self.__till_available
    
    def put_queue(self, item):
        self.__queue.put(item)
       

    
class Floor():
    def __init__(self, num):
        self.__floor_num = num
        # pygame.mouse
        # pygame.timer

        
class Building:
    def __init__(self, floors: int, elevators: int):
        self.__floors = []
        for i in range(floors):
            self.__floors.append(Floor(i))
        self.__elevators = []
        for i in range(elevators):
            self.__elevators.append(Elevator(i))
        self.roof = 0
        
    
    def get_elevators(self):
        return self.__elevators

    def constract_the_building(self):
        for i in range (len(self.__floors)):
            y = building_floor - i * floor_heit
            screen.blit(img1, (20, y))
            screen.blit(img3,(280, y))
            pygame.draw.line(screen, (BLACK), [20, y], [386, y], 7)
            font = pygame.font.Font (None, 25)
            number = font.render(f"{i}", True, (BLACK))
            screen.blit(number, (300, y + 20))
        self.roof = y #the roof of the building
        for i in range (len(self.__elevators)):
            x = 395 + i * f_heit_line
            screen.blit(img2, (x, 570))


    def button(self): #identifies the booked floor
        LEFT = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            current_x, current_y = pygame.mouse.get_pos()
            if 290 < current_x < 320 and self.roof < current_y < 620 and 10 < (620 - current_y) % floor_heit < 31: 
                num_floor = (620 - current_y) // floor_heit
                green_button(num_floor)
                self.move_elv(num_floor)
                timer = a1.get_neareste_elevator(num_floor)
                print(timer)

    def move_elv(self, num_floor):
        for i in range (len(self.__elevators)):
            elevator = a1.get_elevators()[i]
            x = 395 + i * 58
            y = elevator.get_current_floor()
            screen.blit(img2,(x, y))
            pygame.display.flip()
            new_y = building_floor - (num_floor * floor_heit)
            while y != new_y:
            # pygame.time.delay(8)
                if new_y < y:
                    y -= 1
                else:
                    y += 1
            # img2.fill(WHITE)
                screen.blit(img2,(x, y))
                pygame.display.flip()
            elevator.set_current_floor(y)
        

    def get_neareste_elevator(self, num_floor):
        data_elevator = [] * len(self.__elevators)
        for i in range (len(self.__elevators)):
            elevator = a1.get_elevators()[i]
            new_floor = (620 - elevator.get_current_floor()) // floor_heit
            timer = elevator.get_till_available() + ((abs(new_floor - num_floor)) * 0.5)
            if elevator.get_till_available() != 0:
                timer += 2
            data_elevator.append(timer)
        elevator = a1.get_elevators()[data_elevator.index(min(data_elevator))]
        elevator.put_queue(min(data_elevator))
        # print((data_elevator.index(min(data_elevator))))
        return(min(data_elevator))
    



    
def black_button(num_floor):
    for i in range (num_floor + 1) :
        y = building_floor - i * floor_heit
    font = pygame.font.Font (None, 25)
    number = font.render(f"{i}", True, (BLACK))
    pygame.time.delay(3000)
    screen.blit(number, (300, y + 20))
   
    
    # elevator.set_current_foor(y)

def green_button(num_floor): #painting the button green
    for i in range (num_floor + 1) :
        y = building_floor - i * floor_heit
    font = pygame.font.Font (None, 25)
    number = font.render(f"{i}", True, (GREEN))
    screen.blit(number, (300, y + 20))
    pygame.display.flip()
    # black_button(num_floor)




          
    

a1 = Building(11, 8)            
a1.constract_the_building()                   
 
        

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        else:
            a1.button()
        print(pygame.mouse.get_pos())   
  
    # pygame.display.update()
    pygame.display.flip()
    clock.tick(REFRESH_RATE) 


    # def move_elv(self, num_floor):
    #     elevator = a1.get_elevators()[0]
    #     x = 395
    #     y = elevator.get_current_floor()
    #     screen.blit(img2,(x, y))
    #     pygame.display.flip()
    #     new_y = building_floor - (num_floor * floor_heit)
    #     while y != new_y:
    #         # pygame.time.delay(8)
    #         if new_y < y:
    #             y -= 1
    #         else:
    #             y += 1
    #         # img2.fill(WHITE)
    #         screen.blit(img2,(x, y))
    #         pygame.display.flip()
    #     elevator.set_current_floor(y)





 


