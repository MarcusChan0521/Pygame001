import pgzrun
import random


WIDTH = 700
HEIGHT = 700
TIMECOUNT = 30


alien = Actor('alien.png')
alien.pos = WIDTH / 2, HEIGHT / 2 

start_button = Actor('start.png')
start_button.pos = WIDTH / 2, HEIGHT / 2

over_button = Actor('game_over.png')
over_button.pos = WIDTH / 2, HEIGHT / 2 - 120

game_mode = 0       # 0: Game Ready; 1: Game Start; 2: Game Over
count = TIMECOUNT
score = 0


def set_alien_normal():
    alien.image = 'alien.png'


def set_alien_hurt():
    global score
    score += 1
    alien.image = 'alien_hurt.png'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.3)


def set_game_start():
    global game_mode
    global count
    global score

    game_mode = 1
    count = TIMECOUNT
    score = 0


def on_mouse_down(pos, button):
    if button == mouse.LEFT:

        if game_mode == 0:
            if start_button.collidepoint(pos):
                set_game_start()

        elif game_mode == 1:
            if alien.collidepoint(pos):
                set_alien_hurt()
                print("Eek")
            else:
                print("You missed me!")

        else:
            if start_button.collidepoint(pos):
               set_game_start()


def draw():
    screen.clear()

    screen.fill((83, 255, 73))

    if game_mode == 0:
        start_button.draw()
        screen.draw.text("Alien Run", (WIDTH / 2 - 110, HEIGHT / 2 - 150), color = "black", fontsize = 70)

    elif game_mode == 1:
        alien.draw()
        screen.draw.text(f"score: {score}",(7, 57), color = "orange", fontsize = 50)
        screen.draw.text(f"clock: {int(count)}", (7, 7), color = "black", fontsize = 50)
    
    else:
        over_button.draw()
        start_button.draw()
        screen.draw.text(f"score: {score}", (WIDTH / 2 - 60, HEIGHT / 2 - 60), color = "red", fontsize = 50)
    

def update():
    global count
    global game_mode
    
    if game_mode == 1:
        count -= (1 / 60)
        if count <= 0:
            game_mode = 2

        alien.left += random.randint(-20, 20)
        alien.bottom += random.randint(-20, 20)
        if alien.left > WIDTH or alien.right < 0 or alien.bottom < 0 or alien.top > HEIGHT:
            alien.pos = WIDTH / 2, HEIGHT / 2


pgzrun.go()