# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import math

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DinoEvolution!')

# ----- Inicia assets
# ------------------------------------------------------------
# CONFIGURAÇÕES DO JOGO (dá pra mexer nos números pra mudar a dificuldade)
# ------------------------------------------------------------
MAX_DINOS = 20          # máximo de dinos na tela ao mesmo tempo
NIVEL_MAXIMO = 20       # nível final: 19 + 19 = 20 -> vitória!
OVO_MIN, OVO_MAX = 7, 11        # a cada quantos segundos um dino solta um ovo
MEDIA_OVO = (OVO_MIN + OVO_MAX) / 2
VIDA_OVO = 12           # segundos que o ovo fica na tela antes de sumir
MAX_OVOS = 40           # máximo de ovos na tela
ENTREGA_BASE = 12       # segundos entre caixas no começo
ENTREGA_PASSO = 1       # quanto cada melhoria reduz (segundos)
ENTREGA_MIN = 4
ENT_MAX = 8             # nível máximo da melhoria de entrega
QUAL_MAX = 12           # nível máximo de dino que vem nas caixas
COOLDOWN_ROLETA = 40    # segundos entre giros da roleta
lista_de_dinossauro=[0]*20

#tela de fundo
tela_de_fundo = pygame.image.load("imagens/WhatsApp Image 2026-11-16 at 10.41.21.jpeg")
tela_de_fundo = pygame.transform.scale(tela_de_fundo, (WIDTH, HEIGHT))
#musica
pygame.mixer.music.load("sons\dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3")
pygame.mixer.music.set_volume(0.4)

# Quanto vale (em moedas) o ovo de um dino do nível n: dobra a cada nível
def valor_ovo(n):
    return 2 ** (n - 1)
# Preço de comprar um dino do nível n direto na loja
def preco_dino(n):
    return 5 * valor_ovo(n) + 10 * lista_de_dinossauro[n]

def compra_dino(n):
    lista_de_dinossauro[n] += 1

# Limites da área onde os dinos andam (o chão da floresta) 
X_MIN, X_MAX = 50, WIDTH - 50
Y_MIN, Y_MAX = 355, HEIGHT - 50

CONTORNO = (40, 40, 40)