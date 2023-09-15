import pygame
import sys
import random

# กำหนดขนาดหน้าต่างเกม
WINDOW_SIZE = 400
GRID_SIZE = 20
GRID_WIDTH = WINDOW_SIZE // GRID_SIZE
GRID_HEIGHT = WINDOW_SIZE // GRID_SIZE

# กำหนดสี
BLACK = (0, 0, 0)
SLATEGRAY1 = (198, 226, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ROYALBLUE =(66, 105, 225)

# สร้างหน้าต่างเกม
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game")

# เริ่มต้นระบบการแสดงผลฟอนต์
pygame.font.init()

# กำหนดตำแหน่งและความยาวของงูเริ่มต้น
snake = [(5, 5)]
snake_direction = (1, 0)

# สร้างตำแหน่งเริ่มต้นของอาหาร
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# กำหนดคะแนน
score = 0

# ฟังก์ชันสำหรับแสดงคะแนน
def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    window.blit(text, (10, 10))

# กำหนดจำนวนชีวิต
lives = 3

# รับข้อมูลอินพุตจากผู้เล่น
def handle_input():
    global snake_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

# ตรวจสอบการชนกัน
def check_collision():
    global snake, food, score, lives
    head = snake[0]
    if head == food:
        snake.append((0, 0))  # เพิ่มความยาวของงู
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        lives -= 1
        if lives == 0:
            pygame.quit()
            sys.exit()
        else:
            # สร้างงูใหม่เมื่อชีวิตลดลง
            snake = [(5, 5)]
            snake_direction = (1, 0)

    if head in snake[1:]:
        lives -= 1
        if lives == 0:
            pygame.quit()
            sys.exit()
        else:
            # สร้างงูใหม่เมื่อชีวิตลดลง
            snake = [(5, 5)]
            snake_direction = (1, 0)

# วาดตัวอนุบาล
def draw():
    window.fill(SLATEGRAY1)
    for segment in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(window, ROYALBLUE, pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
        # แสดงคะแนน
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    window.blit(score_text, (270, 10))
    
    # แสดงจำนวนชีวิต
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    window.blit(lives_text, (10, 10))
    
    pygame.display.flip()

# เริ่มเกม
while True:
    handle_input()
    check_collision()
    
    # ย้ายงู
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    draw()
    
    # เปลี่ยนสีเมื่อได้ 100 คะแนน
    if score >= 100:
        BLUE = (0, 0, 255)  # เปลี่ยนสีงูเป็นสีน้ำเงิน
         
    pygame.time.delay(100)  # หน่วงเวลาเพื่อควบคุมความเร็วของเกม
