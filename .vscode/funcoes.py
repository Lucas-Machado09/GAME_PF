import pygame
import random
import math

pygame.init()
pygame.mixer.init()

WIDTH = 550
HEIGHT = 600

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DinoEvolution")
tela_de_fundo = pygame.image.load("imagens/WhatsApp Image 2026-11-16 at 10.41.21.jpeg")
tela_de_fundo = pygame.transform.scale(tela_de_fundo, (WIDTH, HEIGHT))
pygame.mixer.music.load("sons\dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3")
pygame.mixer.music.set_volume(0.4)
