import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((450, 800))
clock = pygame.time.Clock()
score_sound = pygame.mixer.Sound("./sounds/score.mp3")
pygame.mixer.music.load("./sounds/bg.mp3")
pygame.mixer.music.play(-1)

sky_sur = pygame.image.load("./graphics/skyy.png")
font = pygame.font.Font("./fonts/FiraMonoNerdFont-Regular.otf", 50)

player_sur = pygame.image.load("./graphics/player/player.png").convert_alpha()
player_gravity = 0
player_rect = player_sur.get_rect(center = (60, 400))

score = 0
text_surface = font.render(f"Score: {score}", False, "White").convert_alpha()
text_rect = text_surface.get_rect(center = (225, 50))

stub1_sur = pygame.image.load("./graphics/stub1.png")
stub1_rect = stub1_sur.get_rect(topright = (425, 0))
stub2_sur = pygame.image.load("./graphics/stub2.png")
stub2_rect = stub2_sur.get_rect(bottomright = (425, 800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -10

    screen.blit(sky_sur, (0,0))
    screen.blit(text_surface, text_rect)
    screen.blit(stub1_sur, stub1_rect)
    screen.blit(stub2_sur, stub2_rect)

    stub1_rect.x -= 2
    stub2_rect.x -= 2

    if player_rect.colliderect(stub1_rect) or player_rect.colliderect(stub2_rect):
        pygame.quit()
        exit()
  
    if player_rect.top <= 0: player_rect.top = 0

    if player_rect.top >= 800: 
        pygame.quit()
        exit()

    if stub1_rect.x == 60:
        score_sound.play()
    if stub1_rect.right <= 0:
        stub1_rect.left = 410 
        stub2_rect.left = 410
        score+=1
        text_surface = font.render(f"Score: {score}", False, "White").convert_alpha()
    player_gravity += 0.5
    player_rect.y += player_gravity
    screen.blit(player_sur, player_rect)

    pygame.display.update()
    clock.tick(60)
