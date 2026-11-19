#— Constantes, caminhos de pastas, botoes e tabelas do DinoEvolution."""
import math
from os import path

# ==================== CAMINHOS DAS PASTAS ====================
IMG_DIR = path.join(path.dirname(__file__), "imagens")
SND_DIR = path.join(path.dirname(__file__), "sons")

# ==================== TELA E REGRAS DO JOGO ====================
WIDTH = 800
HEIGHT = 600
FPS = 60

NIVEL_MAXIMO = 20
MAX_DINOS = 20
OVO_MIN, OVO_MAX = 4, 8
MEDIA_OVO = (OVO_MIN + OVO_MAX) / 2
VIDA_OVO = 12
MAX_OVOS = 40
ENTREGA_BASE = 12
ENTREGA_PASSO = 1
ENTREGA_MIN = 4
ENT_MAX = 8
QUAL_MAX = 12
COOLDOWN_ROLETA = 120

# ==================== LIMITES DO GRAMADO ====================
X_MIN, X_MAX = 12, WIDTH - 12
Y_MIN, Y_MAX = 310, HEIGHT - 60

# ==================== ARQUIVOS DE IMAGEM E SOM ====================
FUNDO = "WhatsApp Image 2026-11-16 at 10.41.21.jpeg"
MUSICA = "dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3"
METEORO = "Meteoro.png"
SOM_ENCAIXE = "encaixe.wav"

# ==================== ROLETA E PONTOS DO CIRCULO ====================
PREMIOS = [("renda", 30), ("caixa", 0), ("renda", 60), ("caixa", 1),
           ("renda", 15), ("caixa", 0), ("renda", 120), ("caixa", 2)]
ROTULOS = ["+30s", "Caixa", "+60s", "Caixa +1", "+15s", "Caixa", "+2min", "Caixa +2"]
PESOS = [30, 20, 20, 8, 30, 20, 4, 2]

CIRCULO = []
for i in range(64):
    angulo = 2 * math.pi * i / 64
    CIRCULO.append((int(math.cos(angulo) * 1000), int(math.sin(angulo) * 1000)))

# ==================== COORDENADAS DOS BOTOES (x, y, largura, altura) ====================
BTN_JOGAR = (275, 325, 250, 56)
BTN_COMO = (305, 396, 190, 42)
BTN_AJUDA = (430, 11, 34, 36)
BTN_DINOS = (472, 11, 88, 36)
BTN_MELHORIAS = (568, 11, 104, 36)
BTN_ROLETA = (680, 11, 108, 36)
BTN_FECHAR = (677, 89, 32, 30)
BTN_ANTERIOR = (95, 505, 115, 32)
BTN_PROXIMO = (590, 505, 115, 32)
BTN_GIRAR = (310, 485, 180, 44)
BTN_NOVO = (280, 485, 240, 46)

# ==================== LISTA DOS 20 DINOSSAUROS ====================
BASE = [
    ("Baby", "dino_01.jpeg", 0.80),
    ("Velociraptor", "dino_02.jpeg", 0.85),
    ("Dilofossauro", "dino_03.jpeg", 0.88),
    ("Paquicefalossauro", "dino_04.jpeg", 0.90),
    ("Parassaurolofo", "dino_05.jpeg", 0.93),
    ("Estegossauro", "dino_06.jpeg", 0.96),
    ("Anquilossauro", "dino_07.jpeg", 0.98),
    ("Triceratops", "dino_08.jpeg", 1.00),
    ("Carnotauro", "dino_09.jpeg", 1.03),
    ("Alossauro", "dino_10.jpeg", 1.05),
    ("Barionix", "dino_11.jpeg", 1.08),
    ("Pteranodonte", "dino_12.jpeg", 1.10),
    ("Quetzalcoatlus", "dino_13.jpeg", 1.13),
    ("Plesiossauro", "dino_14.jpeg", 1.15),
    ("Mosassauro", "dino_15.jpeg", 1.18),
    ("Diplodoco", "dino_16.jpeg", 1.20),
    ("Braquiossauro", "dino_17.jpeg", 1.23),
    ("Espinossauro", "dino_18.jpeg", 1.26),
    ("Giganotossauro", "dino_19.jpeg", 1.30),
    ("Rei T-Rex", "dino_20.jpeg", 1.35),
]