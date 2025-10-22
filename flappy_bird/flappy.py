import pygame
import sys
import random

# ---------- Ayarlar ----------
WIDTH, HEIGHT = 400, 600
FPS = 60

BIRD_RADIUS = 16
GRAVITY = 0.45
FLAP_STRENGTH = -9.5

PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_FREQ_MS = 1500  # yeni boru üretme aralığı (ms)
PIPE_SPEED = 3.5

FLOOR_HEIGHT = 90

# Renkler
WHITE = (255, 255, 255)
SKY = (135, 206, 235)
BIRD_COLOR = (255, 215, 0)
PIPE_COLOR = (34, 139, 34)
FLOOR_COLOR = (222, 184, 135)
TEXT_COLOR = (20, 20, 20)

# ---------- Pygame başlat ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)
pygame.display.set_caption("Flappy Bird - Pygame")

# Oyun durumları
def reset_game():
    bird_x = 80
    bird_y = HEIGHT // 2
    bird_vel = 0.0
    pipes = []  # her pipe: dict {'x':..., 'top':..., 'bottom':...}
    score = 0
    passed_pipes = set()
    game_over = False
    return bird_x, bird_y, bird_vel, pipes, score, passed_pipes, game_over

bird_x, bird_y, bird_vel, pipes, score, passed_pipes, game_over = reset_game()

# Zamanlayıcı: boru üretimi
SPAWNPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNPIPE, PIPE_FREQ_MS)

# Yer (zemin) için kaydırma efekti
floor_x = 0

def create_pipe():
    gap_y_center = random.randint(120, HEIGHT - FLOOR_HEIGHT - 120)
    top = gap_y_center - PIPE_GAP // 2
    bottom = gap_y_center + PIPE_GAP // 2
    return {'x': WIDTH, 'top': top, 'bottom': bottom}

def draw_bird(x, y):
    pygame.draw.circle(screen, BIRD_COLOR, (int(x), int(y)), BIRD_RADIUS)
    # göz
    eye_x = int(x + BIRD_RADIUS * 0.3)
    eye_y = int(y - BIRD_RADIUS * 0.3)
    pygame.draw.circle(screen, (0,0,0), (eye_x, eye_y), 3)

def draw_pipe(pipe):
    x = int(pipe['x'])
    # üst boru
    pygame.draw.rect(screen, PIPE_COLOR, pygame.Rect(x, 0, PIPE_WIDTH, pipe['top']))
    # alt boru
    pygame.draw.rect(screen, PIPE_COLOR, pygame.Rect(x, pipe['bottom'], PIPE_WIDTH, HEIGHT - pipe['bottom'] - FLOOR_HEIGHT))

def bird_rect(x, y):
    return pygame.Rect(int(x - BIRD_RADIUS), int(y - BIRD_RADIUS), BIRD_RADIUS*2, BIRD_RADIUS*2)

def pipe_rects(pipe):
    x = int(pipe['x'])
    top_rect = pygame.Rect(x, 0, PIPE_WIDTH, pipe['top'])
    bottom_rect = pygame.Rect(x, pipe['bottom'], PIPE_WIDTH, HEIGHT - pipe['bottom'] - FLOOR_HEIGHT)
    return top_rect, bottom_rect

def draw_text_centered(text, y, font_obj, color=TEXT_COLOR):
    surf = font_obj.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

# Ana döngü
running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # saniye cinsinden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    bird_x, bird_y, bird_vel, pipes, score, passed_pipes, game_over = reset_game()
                else:
                    bird_vel = FLAP_STRENGTH
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                bird_vel = FLAP_STRENGTH

        if event.type == SPAWNPIPE and not game_over:
            pipes.append(create_pipe())

    if not game_over:
        # fizik
        bird_vel += GRAVITY
        bird_y += bird_vel

        # boruları hareket ettir
        for p in pipes:
            p['x'] -= PIPE_SPEED

        # boruları sil (ekran dışına çıkan)
        pipes = [p for p in pipes if p['x'] + PIPE_WIDTH > -50]

        # çarpışma kontrolü
        brect = bird_rect(bird_x, bird_y)
        # zemin veya tavana çarpma
        if bird_y + BIRD_RADIUS >= HEIGHT - FLOOR_HEIGHT:
            game_over = True
        if bird_y - BIRD_RADIUS <= 0:
            bird_y = BIRD_RADIUS
            bird_vel = 0

        # borularla çarpışma
        for p in pipes:
            top_r, bot_r = pipe_rects(p)
            if brect.colliderect(top_r) or brect.colliderect(bot_r):
                game_over = True

        # skor: borunun merkezini geçince
        for i, p in enumerate(pipes):
            center_x = p['x'] + PIPE_WIDTH/2
            if center_x < bird_x and i not in passed_pipes:
                score += 1
                passed_pipes.add(i)

        # floor kaydırma
        floor_x -= PIPE_SPEED
        if floor_x <= -WIDTH:
            floor_x = 0

    # ----- çizim -----
    screen.fill(SKY)

    # boruları çiz
    for p in pipes:
        draw_pipe(p)

    # zemin (iki parça kaydırarak sonsuzmuş gibi göster)
    pygame.draw.rect(screen, FLOOR_COLOR, pygame.Rect(0 + floor_x, HEIGHT - FLOOR_HEIGHT, WIDTH, FLOOR_HEIGHT))
    pygame.draw.rect(screen, FLOOR_COLOR, pygame.Rect(WIDTH + floor_x, HEIGHT - FLOOR_HEIGHT, WIDTH, FLOOR_HEIGHT))

    # kuşu çiz
    draw_bird(bird_x, bird_y)

    # skor
    draw_text_centered(str(score), 40, font)

    if game_over:
        draw_text_centered("OYUN BİTTİ", HEIGHT//2 - 30, font)
        draw_text_centered("Tekrar başlatmak için Space", HEIGHT//2 + 10, small_font)
        draw_text_centered("Boşluk: zıpla / Fare tıkla: zıpla", HEIGHT - FLOOR_HEIGHT - 30, small_font)

    pygame.display.flip()

pygame.quit()
sys.exit()