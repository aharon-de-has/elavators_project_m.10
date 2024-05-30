import pygame
import queue
import numpy
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


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
# screen.blit(img2,(20, 100))
pygame.display.flip()

img_screen = 'WhatsApp Image 2024-05-30 at 09.59.45.jpg'
img3 = pygame.image.load(img_screen).convert()
# screen.blit(img3,(200, 100))
pygame.display.flip()


clock = pygame.time.Clock()
REFRESH_RATE = 60






floors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elevators = [0, 0, 0, 0]
for i in range (len(floors)):
    y = 570 - i * 51
    screen.blit(img1, (20, y))
    screen.blit(img3,(280, y))
    pygame.draw.line(screen, (BLACK), [20, y], [386, y], 7)
    font = pygame.font.Font (None, 25)
    number = font.render(f"{i}", True, (BLACK))
    screen.blit(number, (300, y+20))
roof = y #the roof of the building
for i in range (len(elevators)):
    x = 395 + i * 58
    screen.blit(img2, (x, 570))




class Elevator():
    def __init__(self):
        self.__current_floor = 0
        self.__till_available = 0
        self.__queue = queue.Queue()

    def move_elevator():
        pygame

    
class Floor():
    def __init__(self, num):
        self.__floor_num = num
        pygame.mouse
        pygame.timer

        
class Building:
    def __init__(self, floors: int, elevators: int):
        self.__floors = []
        for i in range(floors):
            self.__floors.append(Floor(i))
        self.__elevators = []
        for i in range(elevators):
            self.__elevators.append(Elevator(i))
        # self.__request = queue.Queue()



    

    def get_neareste_elevator(self, num_floor):
        data_elevator = [] * len(self.__elevators)
        for elevator in self.__elevators:
            timer = self.__till_available[elevator] + ((abs(self.current_floor[elevator] - self.__floor_num)) * 0.5)
            if self.__till_available != 0:
                timer += 2
            data_elevator[elevator] = timer
        self.__queue.put(data_elevator.index(min(data_elevator))) #need to be precise
        print(min(data_elevator))
        return min(data_elevator)

    
    # def control(self, floor_num): 
    #     self.__request.put(floor_num)
    #     neareste = get_neareste_elevator(__request) #need to be precise
  
def button(): #identifies wich floor the elevator was ordered to
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        current_x, current_y = pygame.mouse.get_pos()
        if 280 < current_x < 380 and roof < current_y < 620: 
            num_floor = (620 - current_y) // 51
            print(num_floor)
            # Building().get_neareste_elevator(num_floor)
    

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        else:
            button()
        # print(pygame.mouse.get_pos())   
  
    pygame.display.update()
    # pygame.display.flip()
    # clock.tick(REFRESH_RATE) 





 


