import pygame
from pygame.locals import *
from gl import Renderer
from buffer import Buffer
from shaders import *
from model import Model

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

# Nuevos Shaders
rend.SetShaders(scan_vertex_shader, scan_fragment_shader)

faceModel = Model("models/model.obj")
faceModel.AddTexture("textures/model.bmp")
faceModel.translation.z = -5
faceModel.scale.x = 2
faceModel.scale.y = 2
faceModel.scale.z = 2
rend.scene.append(faceModel)

isRunnig = True

while isRunnig:
    deltaTime = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunnig = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunnig = False

            elif event.key == pygame.K_1:
                rend.FilledMode()

            elif event.key == pygame.K_2:
                rend.WireframeMode()

    if keys[K_LEFT]:
        faceModel.rotation.y -= 40 * deltaTime

    if keys[K_RIGHT]:
        faceModel.rotation.y += 40 * deltaTime

    # camera
    if keys[K_a]:
        rend.camera.position.x -= 1 * deltaTime  # 1m/s

    if keys[K_d]:
        rend.camera.position.x += 1 * deltaTime  # 1m/s

    if keys[K_w]:
        rend.camera.position.y += 1 * deltaTime  # 1m/s

    if keys[K_s]:
        rend.camera.position.y -= 1 * deltaTime  # 1m/s

    rend.time += deltaTime

    rend.Render()
    pygame.display.flip()

pygame.quit()
