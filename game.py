import pygame
from random import randrange

class Sett():
    def __init__(self):
        pygame.init()
        self.Res = 800
        self.Size = 50
        self.x, self.y = randrange(0, self.Res, self.Size), randrange(0, self.Res, self.Size)
        self.apple = randrange(0, self.Res, self.Size), randrange(0, self.Res, self.Size)
        self.length = 1
        self.snake = [(self.x, self.y)]
        self.dirx, self.diry = 0, self.Size
        self.fps = 10
        self.bg_color = (0.0, 0.0, 1.0)  
        self.snake_color = pygame.Color('yellow')  
        self.Control = {'W': True, 'S': True, 'A': True, 'D': True}
        self.Font_Score = pygame.font.Font(None, 36)
        self.Font_End = pygame.font.Font(None, 110)
        self.score = 0
        self.New_Score = 10
        self.game_over = False

    def restart_game(self):
        self.x, self.y = randrange(0, self.Res, self.Size), randrange(0, self.Res, self.Size)
        self.apple = randrange(0, self.Res, self.Size), randrange(0, self.Res, self.Size)
        self.length = 1
        self.snake = [(self.x, self.y)]
        self.dirx, self.diry = 0, self.Size
        self.score = 0
        self.game_over = False

s_settings = Sett()
sc = pygame.display.set_mode([s_settings.Res, s_settings.Res])
pygame.display.set_caption("bagdan game")
Clock = pygame.time.Clock()

def draw_game_over():
    render_end = s_settings.Font_End.render('ВИ ПРОГРАЛИ', True, (255, 0, 0))
    sc.blit(render_end, (s_settings.Res // 2 - 239, s_settings.Res // 3))
    render_retry = s_settings.Font_Score.render('Натисніть R, щоб спробувати ще раз', True, (255, 255, 255))
    sc.blit(render_retry, (s_settings.Res // 2 - 220, s_settings.Res // 2))

def handle_game_over_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                s_settings.restart_game()

running = True
while running:
    sc.fill(s_settings.bg_color)
    render_score = s_settings.Font_Score.render(f'SCORE: {s_settings.score}', True, (255, 0, 0))
    sc.blit(render_score, (10, 10))

    if not s_settings.game_over:
        [pygame.draw.rect(sc, s_settings.snake_color, (i, j, s_settings.Size - 1, s_settings.Size - 1)) for i, j in s_settings.snake]
        pygame.draw.rect(sc, pygame.Color('blue'), (*s_settings.apple, s_settings.Size, s_settings.Size))
    else:
        draw_game_over()

    pygame.display.flip()
    Clock.tick(s_settings.fps)

    if not s_settings.game_over:
        newX = s_settings.snake[-1][0] + s_settings.dirx
        newY = s_settings.snake[-1][1] + s_settings.diry
        s_settings.snake.append((newX, newY))
        s_settings.snake = s_settings.snake[-s_settings.length:]

        if s_settings.snake[-1] == s_settings.apple:
            s_settings.apple = randrange(0, s_settings.Res, s_settings.Size), randrange(0, s_settings.Res, s_settings.Size)
            s_settings.length += 1
            s_settings.score += s_settings.New_Score

        if newX < 0 or newX >= s_settings.Res or newY < 0 or newY >= s_settings.Res:
            s_settings.game_over = True

        if len(s_settings.snake) != len(set(s_settings.snake)):
            s_settings.game_over = True

    if s_settings.game_over:
        handle_game_over_events()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and s_settings.Control['W'] and s_settings.diry != s_settings.Size:
                s_settings.dirx, s_settings.diry = 0, -s_settings.Size
                s_settings.Control = {'W': True, 'S': False, 'A': True, 'D': True}
            if event.key == pygame.K_s and s_settings.Control['S'] and s_settings.diry != -s_settings.Size:
                s_settings.dirx, s_settings.diry = 0, s_settings.Size
                s_settings.Control = {'W': False, 'S': True, 'A': True, 'D': True}
            if event.key == pygame.K_a and s_settings.Control['A'] and s_settings.dirx != s_settings.Size:
                s_settings.dirx, s_settings.diry = -s_settings.Size, 0
                s_settings.Control = {'W': True, 'S': True, 'A': True, 'D': False}
            if event.key == pygame.K_d and s_settings.Control['D'] and s_settings.dirx != -s_settings.Size:
                s_settings.dirx, s_settings.diry = s_settings.Size, 0
                s_settings.Control = {'W': True, 'S': True, 'A': False, 'D': True}