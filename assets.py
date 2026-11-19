#Assets:"""assets.py — Carregamento de imagens, fontes, sons e funcoes de desenho do DinoEvolution."""
import pygame
from os import path
from config import *


# ==================== CARREGAMENTO DE RECURSOS ====================
def montar_info():  # Carrega e redimensiona as imagens dos 20 niveis de dinossauros.
    dinos = {}
    for i in range(NIVEL_MAXIMO):
        nivel = i + 1
        nome, arquivo, escala = BASE[i]
        original = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
        original.set_colorkey((0, 0, 0))
        r = original.get_rect()

        largura = int(86 * escala)
        altura = int(r.height * largura / r.width)
        imagem = pygame.transform.scale(original, (largura, altura))
        imagem.set_colorkey((0, 0, 0))

        largura_mini = 54
        altura_mini = int(r.height * largura_mini / r.width)
        if altura_mini > 44:
            altura_mini = 44
            largura_mini = int(r.width * altura_mini / r.height)
        mini = pygame.transform.scale(original, (largura_mini, altura_mini))
        mini.set_colorkey((0, 0, 0))

        info = {"nome": nome, "imagem": imagem, "mini": mini}
        if nivel == NIVEL_MAXIMO:
            largura_vit = 270
            altura_vit = int(r.height * largura_vit / r.width)
            vitoria = pygame.transform.scale(original, (largura_vit, altura_vit))
            vitoria.set_colorkey((0, 0, 0))
            info["vitoria"] = vitoria

        dinos[nivel] = info
    return dinos


def carregar_assets():  # Carrega fundo, meteoro, dinossauros, fontes, efeitos sonoros e musica.
    assets = {}
    fundo = pygame.image.load(path.join(IMG_DIR, FUNDO)).convert()
    assets["fundo"] = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    assets["meteoro"] = pygame.image.load(path.join(IMG_DIR, METEORO)).convert_alpha()
    assets["dinos"] = montar_info()

    assets["titulo"] = pygame.font.SysFont("arial", 52, bold=True)
    assets["grande"] = pygame.font.SysFont("arial", 28, bold=True)
    assets["fonte"] = pygame.font.SysFont("arial", 20, bold=True)
    assets["pequena"] = pygame.font.SysFont("arial", 15, bold=True)
    assets["ovo"] = pygame.font.SysFont("arial", 22, bold=True)

    som = pygame.mixer.Sound(path.join(SND_DIR, SOM_ENCAIXE))
    for nome in ["coletar", "mesclar", "comprar", "vitoria", "encaixe"]:
        assets[nome] = som

    pygame.mixer.music.load(path.join(SND_DIR, MUSICA))
    pygame.mixer.music.set_volume(0.4)
    return assets


# ==================== FUNCOES DE DESENHO ====================
def poligono_local(tela, cor, pontos, x, y, k=1.0):  # Desenha um poligono deslocado para (x, y) com escala k.
    convertidos = []
    for px, py in pontos:
        convertidos.append((int(x + px * k), int(y + py * k)))
    pygame.draw.polygon(tela, cor, convertidos)


def retangulo(tela, cor, area):  # Desenha um retangulo preenchido a partir de (x, y, largura, altura).
    x, y, largura, altura = area
    pontos = [(0, 0), (largura, 0), (largura, altura), (0, altura)]
    poligono_local(tela, cor, pontos, x, y)


def placa(tela, area, cor, borda=(70, 42, 22)):  # Desenha um botao ou painel com sombra e borda 3D.
    x, y, largura, altura = area
    retangulo(tela, (42, 26, 14), (x + 3, y + 4, largura, altura))
    retangulo(tela, borda, (x, y, largura, altura))
    retangulo(tela, cor, (x + 3, y + 3, largura - 6, altura - 6))
    clara = []
    escura = []
    for canal in cor:
        c1 = canal + 27
        if c1 > 255:
            c1 = 255
        c2 = canal - 24
        if c2 < 0:
            c2 = 0
        clara.append(c1)
        escura.append(c2)
    retangulo(tela, clara, (x + 3, y + 3, largura - 6, 3))
    retangulo(tela, escura, (x + 3, y + altura - 6, largura - 6, 3))


def oval(tela, cor, cx, cy, rx, ry):  # Desenha uma elipse preenchida usando a tabela CIRCULO.
    pontos = []
    for px, py in CIRCULO:
        pontos.append((int(cx + rx * px / 1000), int(cy + ry * py / 1000)))
    pygame.draw.polygon(tela, cor, pontos)


def anel(tela, cor, cx, cy, rx, ry, grossura=3):  # Desenha o contorno de uma elipse usando CIRCULO.
    pontos = []
    for px, py in CIRCULO:
        pontos.append((int(cx + rx * px / 1000), int(cy + ry * py / 1000)))
    pygame.draw.lines(tela, cor, True, pontos, grossura)


def desenhar_ovo(tela, x, y, k=1.0):  # Desenha um ovo manchado com sombra na posicao (x, y).
    oval(tela, (59, 43, 25), x, y + int(13 * k), int(12 * k), int(4 * k))
    oval(tela, (250, 240, 206), x, y, int(11 * k), int(14 * k))
    anel(tela, (145, 114, 72), x, y, int(11 * k), int(14 * k), 2)
    oval(tela, (194, 152, 88), x - int(4 * k), y - int(3 * k), int(3 * k), int(4 * k))
    oval(tela, (194, 152, 88), x + int(4 * k), y + int(3 * k), int(2 * k), int(3 * k))


def desenhar_caixa(tela, x, y, k=1.0):  # Desenha uma caixa de madeira de entrega centralizada em (x, y).
    lado = int(42 * k)
    meio = int(lado / 2)
    oval(tela, (59, 43, 25), x, y + meio + 2, int(22 * k), int(6 * k))
    placa(tela, (x - meio, y - meio, lado, lado), (184, 128, 66), (92, 56, 26))
    poligono_local(tela, (132, 86, 40), [(-15, -12), (-11, -15), (15, 12), (11, 15)], x, y, k)
    poligono_local(tela, (132, 86, 40), [(11, -15), (15, -12), (-11, 15), (-15, 12)], x, y, k)


def desenhar_moeda(tela, x, y, k=1.0):  # Desenha uma moeda dourada na posicao (x, y).
    raio = int(14 * k)
    pygame.draw.circle(tela, (153, 102, 24), (int(x), int(y)), raio)
    pygame.draw.circle(tela, (255, 214, 68), (int(x), int(y)), int(raio * 0.82))
    retangulo(tela, (214, 153, 36), (int(x - 2 * k), int(y - 6 * k), max(2, int(4 * k)), max(4, int(12 * k))))


def escrever(tela, assets, texto, x, y, fonte="fonte", cor=(255, 250, 232), centro=False):  # Escreve texto com sombra na tela.
    f = assets[fonte]
    sombra = f.render(str(texto), True, (42, 26, 14))
    superficie = f.render(str(texto), True, cor)
    r = superficie.get_rect()
    if centro:
        r.center = (int(x), int(y))
    else:
        r.topleft = (int(x), int(y))
    tela.blit(sombra, (r.x + 2, r.y + 2))
    tela.blit(superficie, r)