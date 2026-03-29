import pygame
import numpy as np
import random

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

G = 0.1

class Body:
    def __init__(self, x, y, vx, vy, mass, color):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)
        self.mass = mass
        self.color = color
        self.history = []

    def update(self, bodies):
        force = np.array([0.0, 0.0])
        for other in bodies:
            if other is self:
                continue

            diff = other.pos - self.pos
            distance = np.linalg.norm(diff)

            if distance > 1:
                # Loi de la gravitation universelle
                f = G * self.mass * other.mass / distance**2
                force += f * diff / distance

        acceleration = force / self.mass
        self.vel += acceleration
        self.pos += self.vel

        self.history.append(self.pos.copy())
        if len(self.history) > 200:
            self.history.pop(0)

    def draw(self, screen):
        # Dessin du corps principal
        pygame.draw.circle(screen, self.color, self.pos.astype(int), 5)
        # Dessin de la traînée
        for point in self.history:
             pygame.draw.circle(screen, self.color, point.astype(int), 1)

# Configuration initiale
bodies = [
    Body(500, 500, 0, 0, 5000, (255, 255, 0)), # soleil central
    Body(500, 300, 1.5, 0, 1, (0, 255, 0))     # planète de départ
]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Ajout d'une planète au clic
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            sun = bodies[0] 
            
            # calculer la distance (d) entre le clic et le soleil
            dx = mx - sun.pos[0]
            dy = my - sun.pos[1]
            distance = np.sqrt(dx**2 + dy**2)
            
            if distance > 10: 
                # calcul de la vitesse requise
                v_mag = np.sqrt((G * sun.mass) / distance)
                
                # calculer le vecteur vitesse perpendiculaire au rayon
                vx = -dy / distance * v_mag
                vy = dx / distance * v_mag
                
                new_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                bodies.append(Body(mx, my, vx, vy, 1, new_color))

    for body in bodies:
        body.update(bodies)
        body.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
