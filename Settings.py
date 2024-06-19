import pygame

pygame.init()

WHITE = (245, 245, 245)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (220, 220, 220)

window_width = 1024
window_heigh =  633
size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("elevator")
screen.fill(WHITE)
pygame.display.flip()



img_bld = 'various/WhatsApp Image 2024-05-30 at 09.15.01.jpeg'
img1 = pygame.image.load(img_bld).convert()

img_elv = 'various/WhatsApp Image 2024-05-29 at 18.33.11.jpeg'
img2 = pygame.image.load(img_elv).convert()

img_screen = 'various/WhatsApp Image 2024-05-30 at 09.59.45.jpg'
img3 = pygame.image.load(img_screen).convert()


clock = pygame.time.Clock()
REFRESH_RATE = 87

zero_line = 620
building_floor = 570
Building_floor_screen = 590
floor_heit = 51
f_heit_line = 57
button_pos = 300
show_timer_pos = 340
show_circle_pos = 350
left_building = 20
right_building = 280
location_left_elevator = 395
right_position_black_line = 386
LEFT = 1
left_side = 290
right_side = 320
down = 10
up = 31
time_for_one_floor = 0.5
delay_time = 2

