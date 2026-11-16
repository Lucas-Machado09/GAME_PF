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

# CONFIGURAÇÕES DO JOGO

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
X_MIN, X_MAX = 0, WIDTH
Y_MIN, Y_MAX = 490, 650

CONTORNO = (40, 40, 40)
# ------------------------------------------------------------
# OS 20 NÍVEIS DE DINO
# ------------------------------------------------------------
BASE = [
    ("baby",       (pygame.image.load("imagens\dino_01.jpeg")),  0.8),
    ("Velociraptor",  (pygame.image.load("imagens\dino_02.jpeg")), 0.9),
    ("Tricerátops",   (pygame.image.load("imagens\dino_03.jpeg")), 1.0),
    ("Estegossauro",  (pygame.image.load("imagens\dino_04.jpeg")),  1.1),
    ("Braquiossauro", (pygame.image.load("imagens\dino_05.jpeg")),  1.1),
    ("Espinossauro",  (pygame.image.load("imagens\dino_06.jpeg")),   1.2),
    ("T-Rex",         (pygame.image.load("imagens\dino_07.jpeg")), 1.3),
    ("baby épico",       (pygame.image.load("imagens\dino_08.jpeg")),  0.8),
    ("Velociraptor épico",  (pygame.image.load("imagens\dino_09.jpeg")), 0.9),
    ("Tricerátops épico",   (pygame.image.load("imagens\dino_10.jpeg")), 1.0),
    ("Estegossauro épico",  (pygame.image.load("imagens\dino_11.jpeg")),  1.1),
    ("Braquiossauro épico", (pygame.image.load("imagens\dino_12.jpeg")),  1.1),
    ("Espinossauro épico",  (pygame.image.load("imagens\dino_13.jpeg")),   1.2),
    ("T-Rex épico",         (pygame.image.load("imagens\dino_14.jpeg")), 1.3),
    ("baby gold",       (pygame.image.load("imagens\dino_15.jpeg")),  0.8),
    ("Velociraptor gold",  (pygame.image.load("imagens\dino_16.jpeg")), 0.9),
    ("Tricerátops gold",   (pygame.image.load("imagens\dino_17.jpeg")), 1.0),
    ("Estegossauro gold",  (pygame.image.load("imagens\dino_18.jpeg")),  1.1),
    ("Espinossauro gold", (pygame.image.load("imagens\dino_19.jpeg")),  1.1),
    ("T-Rex gold",  (pygame.image.load("imagens\dino_20.jpeg")),   1.2),
]
def montar_info():
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, imagem, escala = BASE[n - 1]

        info[n] = {
            "nome": nome,
            "imagem": imagem,
            "escala": escala
        }

    return info
INFO = montar_info()
