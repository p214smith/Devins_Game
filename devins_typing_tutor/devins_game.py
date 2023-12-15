import pygame, sys
from pygame.locals import *
import pygame_menu
from pygame_menu import themes
import random

pygame.init()

selected_level = 1
selected_difficulty = 1
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
display = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF = pygame.display.set_mode(((1000,800)))
DISPLAYSURF.fill(BLUE)
pygame.display.set_caption("Devin's Typing Teacher")
font = pygame_menu.font.FONT_8BIT
font1 = pygame.font.Font('freesansbold.ttf',32)
dev_pic = pygame.image.load('devins_picture.jpg')

myTheme = themes.Theme(widget_font = font,background_color = GREEN, title_background_color = RED,widget_font_color = WHITE, widget_font_size = 36, title_bar_style = 
                       pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE, title_font = font, title_font_color = WHITE,title_font_size = 42)
myTheme2 = themes.Theme(widget_font = pygame_menu.font.FONT_FRANCHISE,background_color = BLUE, title_background_color = GREEN,widget_font_color = WHITE, widget_font_size = 24, title_bar_style = 
                       pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE, title_font = font, title_font_color = WHITE,title_font_size = 42)
myTheme3 = themes.Theme(widget_font = pygame_menu.font.FONT_FRANCHISE,background_color = RED, title_background_color = GREEN,widget_font_color = WHITE, widget_font_size = 24, title_bar_style = 
                       pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE, title_font = font, title_font_color = WHITE,title_font_size = 42)

mainMenu = pygame_menu.Menu("Devins Typing Game",SCREEN_WIDTH,SCREEN_HEIGHT,theme= myTheme)
mainMenu.add.image('devins_picture.jpg')
def set_level(value, level):
    selected_level = value
    print(level)
    print(selected_level)
    return selected_level
 
def start_the_game():
    mainMenu._open(loading)
    pygame.time.set_timer(update_loading, 30)
    
def start_level(update_loading):
    progress = loading.get_widget("1")
    progress.set_value(progress.get_value() + 1)
    if progress.get_value() == 100:
        pygame.time.set_timer(update_loading, 0)
        progress.set_value(0)
        loading.disable()
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        diff = diff_sel.get_value()
        diff1 = diff[0]
        diff2 = diff1[1]
        print(diff2)
        lev = lev_sel.get_value()
        lev1 = lev[0]
        lev2 = lev1[1]
        print(lev2)
        level_selector(lev2,diff2)
    
        
        
    
    
def level_menu():
    mainMenu._open(levelMenu)
    
def difficulty_menu():
    mainMenu._open(difficultyMenu)
    
def set_difficulty(value, difficulty):
    sel = value
    print(difficulty)
    print(value)
    return sel

mainMenu.add.button('Play', start_the_game)
mainMenu.add.button('Levels', level_menu)
mainMenu.add.button('Difficulty',difficulty_menu)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)
pygame.mixer.music.load("game_music.wav")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

 
levelMenu = pygame_menu.Menu('Select a Level', SCREEN_WIDTH, SCREEN_HEIGHT, theme= myTheme2)
levelMenu.add.image('devin_parrot.jpg')
lev_sel =levelMenu.add.selector('Level :', [('Home Row Left Hand', 1), ('Home Row Right Hand', 2),('Top Row Left Hand',3),('Top Row Right Hand',4),('Bottom Row Left Hand',5),('Bottom Row Right Hand',6)], onchange= set_level)

difficultyMenu = pygame_menu.Menu('Select Difficulty', SCREEN_WIDTH, SCREEN_HEIGHT, theme= myTheme2)
difficultyMenu.add.image('devin_swim.jpg',270)
diff_sel = difficultyMenu.add.selector('Difficulty :', [('Easy', 5), ('Medium', 3),('Hard',1)],  onchange=set_difficulty)
diff = diff_sel.get_value()


loading = pygame_menu.Menu('Loading the Game', SCREEN_WIDTH, SCREEN_HEIGHT, theme= myTheme3)
loading.add.image('devin_keyboard.jpg')
loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 500)
update_loading = pygame.USEREVENT + 0

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
def left_hand_home_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_a, 2 : K_s, 3 : K_d , 4 : K_f}
    pic_dic = {1 : "letter_a.png",2: "letter_s.png",3 : "letter_d.png", 4 : "letter_f.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(BLUE)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_1.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_1.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,4)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()

            
            
        
def right_hand_home_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_j, 2 : K_k, 3 : K_l , 4 : K_SEMICOLON}
    pic_dic = {1 : "letter_j.png",2: "letter_k.png",3 : "letter_l.png", 4 : "semicolon.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(RED)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_2.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_2.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,4)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()
    
def left_hand_top_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_q, 2 : K_w, 3 : K_e , 4 : K_r}
    pic_dic = {1 : "letter_q.png",2: "letter_w.png",3 : "letter_e.png", 4 : "letter_r.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(RED)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_3.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_3.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,4)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()

def right_hand_top_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_u, 2 : K_i, 3 : K_o , 4 : K_p}
    pic_dic = {1 : "letter_u.png",2: "letter_i.png",3 : "letter_o.png", 4 : "letter_p.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(RED)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_4.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_4.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,4)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()

def left_hand_bottom_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_z, 2 : K_x, 3 : K_c, 4 : K_v, 5 : K_b}
    pic_dic = {1 : "letter_z.png",2: "letter_x.png",3 : "letter_c.png", 4 : "letter_v.png", 5 : "letter_b.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(BLUE)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_5.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_5.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,5)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()

def right_hand_bottom_row(difficulty):
    diff = difficulty
    attempts = 10
    number_right = 0
    number_wrong = 0
    keys_dic = { 1 : K_t, 2 : K_y, 3 : K_g, 4 : K_h, 5 : K_n, 6 : K_m}
    pic_dic = {1 : "letter_t.png",2: "letter_y.png",3 : "letter_g.png", 4 : "letter_h.png", 5 : "letter_n.png", 6 : "letter_m.png"}
    itr = 0
    loading._close
    mainMenu.disable()
    display.fill(GREEN)
    DISPLAYSURF.blit(display, (0,0))
    counter = 11
    imp = pygame.image.load('keyboard_image_6.png').convert()
    DISPLAYSURF.blit(imp,(200,100))
    pygame.display.update()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('level_6.wav'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    counter = difficulty
    while itr < attempts:
        print(itr)
        display.fill(BLUE)
        DISPLAYSURF.blit(display,(0,0))
        rand = random.randint(1,6)
        print(rand)
        text = font1.render('Press The Letter ',True,GREEN,RED)
        textRect = text.get_rect()
        textRect.center = (1000/2,800/5)
        DISPLAYSURF.blit(text,textRect)
        imp = pygame.image.load(pic_dic[rand]).convert()
        DISPLAYSURF.blit(imp,(400,300))
        pygame.display.update()
        counter = diff
        message = 0
        while counter > 0 :
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == keys_dic[rand]:
                        number_right +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('GREAT JOB!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                        
                    else:
                        number_wrong +=1
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 2
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        message = 1
                    

                if event.type == USEREVENT:
                    counter -= 1
                    if message == 0 and counter == 0:
                        display.fill(BLUE)
                        DISPLAYSURF.blit(display,(0,0))
                        text = font1.render('NICE TRY!',True,GREEN,RED)
                        textRect = text.get_rect()
                        textRect.center = (1000/2,800/5)
                        DISPLAYSURF.blit(text,textRect)
                        pygame.display.update()
                        counter = 3
                        while counter > 0:
                            for event in pygame.event.get():
                                if event.type == USEREVENT:
                                    counter -= 1
                        number_wrong +=1    
        itr += 1
    display.fill(BLUE)
    DISPLAYSURF.blit(display,(0,0))
    str1 = "You got a score of " + str(number_right) + " out of 10"
    text = font1.render(str1,True,GREEN,RED)
    textRect = text.get_rect()
    textRect.center = (1000/2,800/5)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()
    if number_right > 8:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('good_job.wav'))
    else :
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('try_again.wav'))
    counter = 5
    while counter > 0:
        for event in pygame.event.get():
            if event.type == USEREVENT:
                counter -= 1
    mainMenu.enable()        
    display.fill(BLUE)
    DISPLAYSURF.fill(BLUE)
    mainMenu.reset(1)
    mainMenu.draw(DISPLAYSURF)
    pygame.display.update()

    
def level_selector(level_number, difficulty):
    if level_number == 1:
        left_hand_home_row(difficulty)
    elif level_number == 2:
        right_hand_home_row(difficulty)
    elif level_number == 3:
        left_hand_top_row(difficulty)
    elif level_number == 4:
        right_hand_top_row(difficulty)
    elif level_number == 5:
        left_hand_bottom_row(difficulty)
    elif level_number == 6:
        right_hand_bottom_row(difficulty)
 
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            start_level(update_loading)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if mainMenu.is_enabled():
            mainMenu.update(events)
            mainMenu.draw(DISPLAYSURF)
            pygame.display.update()

    