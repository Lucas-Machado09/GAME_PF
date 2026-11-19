# # import pygame
# # import random
# # import math

# # pygame.init()
# # pygame.mixer.init()

# # # ----- Gera tela principal

# # WIDTH = 500
# # HEIGHT = 400
# # window = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption('DinoEvolution!')

# # # CONFIGURAÇÕES DO JOGO

# # MAX_DINOS = 20          # máximo de dinos na tela ao mesmo tempo
# # NIVEL_MAXIMO = 20       # nível final: 19 + 19 = 20 -> vitória!
# # OVO_MIN, OVO_MAX = 7, 11        # a cada quantos segundos um dino solta um ovo
# # MEDIA_OVO = (OVO_MIN + OVO_MAX) / 2
# # VIDA_OVO = 12           # segundos que o ovo fica na tela antes de sumir
# # MAX_OVOS = 40           # máximo de ovos na tela
# # ENTREGA_BASE = 12       # segundos entre caixas no começo
# # ENTREGA_PASSO = 1       # quanto cada melhoria reduz (segundos)
# # ENTREGA_MIN = 4
# # ENT_MAX = 8             # nível máximo da melhoria de entrega
# # QUAL_MAX = 12           # nível máximo de dino que vem nas caixas
# # COOLDOWN_ROLETA = 40    # segundos entre giros da roleta
# # lista_de_dinossauro=[0]*20

# # #tela de fundo
# # tela_de_fundo = pygame.image.load("imagens/WhatsApp Image 2026-11-16 at 10.41.21.jpeg")
# # tela_de_fundo = pygame.transform.scale(tela_de_fundo, (WIDTH, HEIGHT))
# # #musica
# # pygame.mixer.music.load("sons\dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3")
# # pygame.mixer.music.set_volume(0.4)

# # # Quanto vale (em moedas) o ovo de um dino do nível n: dobra a cada nível
# # def valor_ovo(n):
# #     return 2 ** (n - 1)
# # # Preço de comprar um dino do nível n direto na loja
# # def preco_dino(n):
# #     return 5 * valor_ovo(n) + 10 * lista_de_dinossauro[n]

# # def compra_dino(n):
# #     lista_de_dinossauro[n] += 1

# # # Limites da área onde os dinos andam (o chão da floresta) 
# # X_MIN, X_MAX = 0, WIDTH
# # Y_MIN, Y_MAX = 490, 650

# # CONTORNO = (40, 40, 40)

# # # OS 20 NÍVEIS DE DINO

# # BASE = [
# #     ("baby",       (pygame.image.load("imagens\dino_01.jpeg")),  0.8),
# #     ("Velociraptor",  (pygame.image.load("imagens\dino_02.jpeg")), 0.9),
# #     ("Tricerátops",   (pygame.image.load("imagens\dino_03.jpeg")), 1.0),
# #     ("Estegossauro",  (pygame.image.load("imagens\dino_04.jpeg")),  1.1),
# #     ("Braquiossauro", (pygame.image.load("imagens\dino_05.jpeg")),  1.1),
# #     ("Espinossauro",  (pygame.image.load("imagens\dino_06.jpeg")),   1.2),
# #     ("T-Rex",         (pygame.image.load("imagens\dino_07.jpeg")), 1.3),
# #     ("baby épico",       (pygame.image.load("imagens\dino_08.jpeg")),  0.8),
# #     ("Velociraptor épico",  (pygame.image.load("imagens\dino_09.jpeg")), 0.9),
# #     ("Tricerátops épico",   (pygame.image.load("imagens\dino_10.jpeg")), 1.0),
# #     ("Estegossauro épico",  (pygame.image.load("imagens\dino_11.jpeg")),  1.1),
# #     ("Braquiossauro épico", (pygame.image.load("imagens\dino_12.jpeg")),  1.1),
# #     ("Espinossauro épico",  (pygame.image.load("imagens\dino_13.jpeg")),   1.2),
# #     ("T-Rex épico",         (pygame.image.load("imagens\dino_14.jpeg")), 1.3),
# #     ("baby gold",       (pygame.image.load("imagens\dino_15.jpeg")),  0.8),
# #     ("Velociraptor gold",  (pygame.image.load("imagens\dino_16.jpeg")), 0.9),
# #     ("Tricerátops gold",   (pygame.image.load("imagens\dino_17.jpeg")), 1.0),
# #     ("Estegossauro gold",  (pygame.image.load("imagens\dino_18.jpeg")),  1.1),
# #     ("Espinossauro gold", (pygame.image.load("imagens\dino_19.jpeg")),  1.1),
# #     ("T-Rex gold",  (pygame.image.load("imagens\dino_20.jpeg")),   1.2),
# # ]
# # def dinheiro(n):
# #     n = float(n)
# #     for qtd in ["", "k", "M", "B", "T"]:
# #         if abs(n) < 1000 or qtd == "T":
# #             if qtd == "":
# #                 return str(int(n))
# #             return f"{n:.1f}{qtd}" if n < 100 else f"{int(n)}{qtd}"
# #         n /= 1000

# # #=======
# # def montar_info():
# #     info = {}
# #     for n in range(1, NIVEL_MAXIMO + 1):
# #         nome, imagem, escala = BASE[n - 1]

# #         info[n] = {
# #             "nome": nome,
# #             "imagem": imagem,
# #             "escala": escala
# #         }

# #     return info
# # INFO = montar_info()
# # >>>>>>> d44136aa1d7d9bf5ca0b6285f6c4506d67b3db48
# """DinoEvolution — versao com mouse, baseada no inicio do grupo.
# Adaptacao com assistencia de ChatGPT/Codex; consulte o guia linha por linha.
# EXTRAS AUTORIZADOS: eventos/posicao de mouse e set_colorkey para o fundo preto.
# Demais comandos de Pygame: exemplos do handout do Insper.
# """
# import pygame
# import random
# from os import path

# # ==================== CONFIGURACOES ====================
# IMG_DIR = path.join(path.dirname(__file__), "imagens")

# SND_DIR = path.join(path.dirname(__file__), "sons")

# WIDTH = 800

# HEIGHT = 600

# FPS = 60

# MAX_DINOS = 20

# NIVEL_MAXIMO = 20

# OVO_MIN, OVO_MAX = 6, 8

# MEDIA_OVO = (OVO_MIN + OVO_MAX) / 2

# VIDA_OVO = 12

# MAX_OVOS = 40

# ENTREGA_BASE = 12

# ENTREGA_PASSO = 1

# ENTREGA_MIN = 4

# ENT_MAX = 8

# QUAL_MAX = 12

# COOLDOWN_ROLETA = 120

# X_MIN, X_MAX = 12, WIDTH - 12

# Y_MIN, Y_MAX = 310, HEIGHT - 60

# FUNDO = "WhatsApp Image 2026-11-16 at 10.41.21.jpeg"

# MUSICA = "dinosaur_extinction_old_classical_music_by_kris_klavenes_ending_soundtrack_05.02.2021.mp3"

# BASE = [
#     ("Baby", "dino_01.jpeg", 0.8),
#     ("Velociraptor", "dino_02.jpeg", 0.9),
#     ("Tricerátops", "dino_03.jpeg", 1.0),
#     ("Estegossauro", "dino_04.jpeg", 1.1),
#     ("Braquiossauro", "dino_05.jpeg", 1.1),
#     ("Espinossauro", "dino_06.jpeg", 1.2),
#     ("T-Rex", "dino_07.jpeg", 1.3),
#     ("baby épico", "dino_08.jpeg", 0.8),
#     ("Velociraptor épico", "dino_09.jpeg", 0.9),
#     ("Tricerátops épico", "dino_10.jpeg", 1.0),
#     ("Estegossauro épico", "dino_11.jpeg", 1.1),
#     ("Braquiossauro épico", "dino_12.jpeg", 1.1),
#     ("Espinossauro épico", "dino_13.jpeg", 1.2),
#     ("T-Rex épico", "dino_14.jpeg", 1.3),
#     ("baby gold", "dino_15.jpeg", 0.8),
#     ("Velociraptor gold", "dino_16.jpeg", 0.9),
#     ("Tricerátops gold", "dino_17.jpeg", 1.0),
#     ("Estegossauro gold", "dino_18.jpeg", 1.1),
#     ("Espinossauro gold", "dino_19.jpeg", 1.1),
#     ("T-Rex gold", "dino_20.jpeg", 1.2),
# ]

# PREMIOS = [("renda", 30), ("caixa", 0), ("renda", 60), ("caixa", 1),
#            ("renda", 15), ("caixa", 0), ("renda", 120), ("caixa", 2)]

# ROTULOS = ["+30s", "Caixa", "+60s", "Caixa +1", "+15s", "Caixa", "+2min", "Caixa +2"]

# PESOS = [30, 20, 20, 8, 30, 20, 4, 2]

# BRANCO = (245, 244, 231)

# ESCURO = (18, 29, 29)

# PAINEL = (27, 45, 43)

# VERDE = (92, 205, 145)

# DOURADO = (255, 207, 93)

# CINZA = (172, 192, 181)

# VERMELHO = (255, 140, 121)

# # ==================== FUNCOES AUXILIARES ====================
# def valor_ovo(n):
#     """Calcula o valor de um ovo: 1, 2, 4, 8... conforme o nivel do dino."""
#     return 2 ** (n - 1)

# def preco_dino(n, lista_de_dinossauro):
#     """Mantem o preco do grupo; o nivel 1 usa a posicao zero da lista."""
#     return 10 * valor_ovo(n) + 30 * lista_de_dinossauro[n - 1]

# def compra_dino(n, lista_de_dinossauro):
#     """Registra uma compra. A Partida so chama depois de conferir o saldo."""
#     lista_de_dinossauro[n - 1] += 1

# def dinheiro(n):
#     """Abrevia o dinheiro usando comparacoes, int, str e contas simples."""
#     if n >= 1000000000000:
#         return str(int(n / 1000000000000)) + "T"
#     elif n >= 1000000000:
#         return str(int(n / 1000000000)) + "B"
#     elif n >= 1000000:
#         return str(int(n / 1000000)) + "M"
#     elif n >= 1000:
#         return str(int(n / 1000)) + "k"
#     return str(int(n))

# def montar_info():
#     """Organiza os vinte niveis; carrega e dimensiona cada imagem uma vez."""
#     info = {}
#     for n in range(1, NIVEL_MAXIMO + 1):
#         nome, arquivo, escala = BASE[n - 1]
#         imagem = pygame.image.load(path.join(IMG_DIR, arquivo)).convert()
#         # EXTRA AUTORIZADO: remove o preto do JPEG antes de redimensionar.
#         imagem.set_colorkey((0, 0, 0))
#         tamanho = imagem.get_rect()
#         # right e bottom de um get_rect() novo correspondem ao tamanho.
#         # A proporcao original do JPEG e preservada.
#         largura = int(86 * escala)
#         altura = int(largura * tamanho.bottom / tamanho.right)
#         mini_altura = int(54 * tamanho.bottom / tamanho.right)
#         info[n] = {
#             "nome": nome,
#             "imagem": pygame.transform.scale(imagem, (largura, altura)),
#             "mini": pygame.transform.scale(imagem, (54, mini_altura)),
#             "escala": escala,
#         }
#         if n == NIVEL_MAXIMO:
#             altura_vitoria = int(270 * tamanho.bottom / tamanho.right)
#             info[n]["vitoria"] = pygame.transform.scale(imagem, (270, altura_vitoria))
#     return info

# def carregar_assets():
#     """Carrega imagens, fontes e sons; e chamado depois de criar a janela."""
#     assets = {}
#     fundo = pygame.image.load(path.join(IMG_DIR, FUNDO)).convert()
#     assets["fundo"] = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
#     assets["dinos"] = montar_info()
#     assets["titulo"] = pygame.font.SysFont(None, 62)
#     assets["grande"] = pygame.font.SysFont(None, 36)
#     assets["fonte"] = pygame.font.SysFont(None, 26)
#     assets["pequena"] = pygame.font.SysFont(None, 21)
#     assets["ovo"] = pygame.font.SysFont(None, 37)
#     for nome in ["coletar", "mesclar", "comprar", "vitoria"]:
#         assets[nome] = pygame.mixer.Sound(path.join(SND_DIR, nome + ".wav"))
#     pygame.mixer.music.load(path.join(SND_DIR, MUSICA))
#     pygame.mixer.music.set_volume(0.4)
#     return assets

# def objetos_do_grupo(grupo):
#     """Cria uma lista dos sprites para percorrer os objetos na ordem desejada."""
#     objetos = []
#     for objeto in grupo:
#         objetos.append(objeto)
#     return objetos

# # ==================== PERSONAGENS ====================
# class Dino(pygame.sprite.Sprite):
#     """Um dinossauro com nivel, movimento e contador para produzir ovos."""

#     def __init__(self, nivel, x, y, assets):
#         """Posiciona a imagem escolhida pelo nivel e prepara os contadores."""
#         pygame.sprite.Sprite.__init__(self)
#         self.nivel = nivel
#         self.image = assets["dinos"][nivel]["imagem"]
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.x = self.rect.x
#         self.y = self.rect.y
#         self.vx = 0
#         self.vy = 0
#         self.tempo_direcao = 0
#         self.tempo_ovo = random.randint(OVO_MIN, OVO_MAX) * 1000
#         self.preso = False
#         self.escolher_direcao()

#     def escolher_direcao(self):
#         """Usa apenas randint para sortear uma pausa ou uma nova velocidade."""
#         if random.randint(1, 10) <= 3:
#             self.vx, self.vy = 0, 0
#         else:
#             self.vx = random.randint(-43, 43) / 1000
#             self.vy = random.randint(-19, 19) / 1000
#         self.tempo_direcao = random.randint(1000, 3000)

#     def update(self, dt):
#         """Move o dino dentro do campo; dt e o tempo do quadro em milissegundos."""
#         self.tempo_ovo -= dt
#         if not self.preso:
#             self.tempo_direcao -= dt
#             if self.tempo_direcao <= 0:
#                 self.escolher_direcao()
#             self.x += self.vx * dt
#             self.y += self.vy * dt
#             self.rect.x = int(self.x)
#             self.rect.y = int(self.y)
#             if self.rect.left < X_MIN:
#                 self.rect.left = X_MIN
#                 self.x = self.rect.x
#                 self.vx = -self.vx
#             if self.rect.right > X_MAX:
#                 self.rect.right = X_MAX
#                 self.x = self.rect.x
#                 self.vx = -self.vx
#             if self.rect.top < Y_MIN:
#                 self.rect.top = Y_MIN
#                 self.y = self.rect.y
#                 self.vy = -self.vy
#             if self.rect.bottom > Y_MAX:
#                 self.rect.bottom = Y_MAX
#                 self.y = self.rect.y
#                 self.vy = -self.vy

# class Ovo(pygame.sprite.Sprite):
#     """Um ovo coletavel, com valor ligado ao nivel e vida de doze segundos."""

#     def __init__(self, x, y, nivel, assets):
#         """Cria a imagem-base do Sprite para obter sua area; o ovo visivel e desenhado com poligonos."""
#         pygame.sprite.Sprite.__init__(self)
#         self.image = assets["ovo"].render("O", True, (255, 240, 194))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.valor = valor_ovo(nivel)
#         self.vida = VIDA_OVO * 1000

#     def update(self, dt):
#         """Remove o ovo do grupo quando o seu tempo termina."""
#         self.vida -= dt
#         if self.vida <= 0:
#             self.kill()

# class Caixa(pygame.sprite.Sprite):
#     """Uma entrega que cai no campo e depois se transforma em um dinossauro."""

#     def __init__(self, nivel, x, y, assets):
#         """Guarda o destino da caixa e sua area; o desenho de madeira e feito na interface."""
#         pygame.sprite.Sprite.__init__(self)
#         self.image = assets["grande"].render("?", True, (255, 225, 144))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, -30)
#         self.y = -30
#         self.y_alvo = y
#         self.nivel = nivel
#         self.espera = 700
#         self.estado = "caindo"

#     def update(self, dt):
#         """Separa a animacao da queda e a espera de 0,7 segundo para abrir."""
#         if self.estado == "caindo":
#             self.y += 0.45 * dt
#             if self.y >= self.y_alvo:
#                 self.y = self.y_alvo
#                 self.estado = "parada"
#             self.rect.centery = int(self.y)
#         else:
#             self.espera -= dt

# # ==================== REGRAS DA PARTIDA ====================
# class Partida:
#     """Guarda moedas, sprites, compras, melhorias, sorteio e condicao de vitoria."""

#     def __init__(self, assets):
#         """Cria uma partida independente, com cem moedas e dois dinos baby."""
#         self.assets = assets
#         self.moedas = 100
#         self.dinos = pygame.sprite.Group()
#         self.ovos = pygame.sprite.Group()
#         self.caixas = pygame.sprite.Group()
#         self.compradas = [0] * NIVEL_MAXIMO
#         self.ent_lvl = 0
#         self.qual = 1
#         self.maior = 1
#         self.timer = 3000
#         self.tempo = 0
#         self.aviso = "Junte dois dinos iguais para evoluir!"
#         self.aviso_t = 4000
#         self.venceu = False
#         self.girando = False
#         self.tempo_giro = 0
#         self.proxima_troca = 0
#         self.roleta_cd = 0
#         self.cursor_roleta = 0
#         self.premio = 0
#         self.resultado = ""
#         self.aparecer_dino(1, 260, 340)
#         self.aparecer_dino(1, 510, 390)

#     def avisar(self, mensagem):
#         """Mostra uma mensagem curta sem parar o jogo."""
#         self.aviso = mensagem
#         self.aviso_t = 2800

#     def ocupados(self):
#         """Caixas reservam uma vaga para o dinossauro que vai nascer."""
#         return len(self.dinos) + len(self.caixas)

#     def tem_espaco(self):
#         """Evita ultrapassar vinte dinos e entregas somados."""
#         return self.ocupados() < MAX_DINOS

#     def renda(self):
#         """Estima o valor dos ovos por segundo somando os dinos atuais."""
#         total = 0
#         for dino in self.dinos:
#             total += valor_ovo(dino.nivel)
#         return total / MEDIA_OVO

#     def intervalo(self):
#         """Cada melhoria reduz um segundo, ate o intervalo minimo de quatro."""
#         segundos = ENTREGA_BASE - ENTREGA_PASSO * self.ent_lvl
#         if segundos < ENTREGA_MIN:
#             segundos = ENTREGA_MIN
#         return segundos

#     def limite_compra(self):
#         """Libera ate um nivel abaixo do maior obtido; comeca liberando quatro."""
#         limite = self.maior - 1
#         if limite < 4:
#             limite = 4
#         if limite >= NIVEL_MAXIMO:
#             limite = NIVEL_MAXIMO - 1
#         return limite

#     def custo_entrega(self):
#         """Retorna o preco do proximo nivel da melhoria de entrega."""
#         return int(120 * 3 ** self.ent_lvl)

#     def custo_qual(self):
#         """Retorna o preco para melhorar o nivel de dinos das caixas."""
#         return int(60 * 2.5 ** self.qual)

#     def aparecer_dino(self, nivel, x, y):
#         """Adiciona um dinossauro e atualiza o maior nivel ja obtido."""
#         dino = Dino(nivel, x, y, self.assets)
#         self.dinos.add(dino)
#         if nivel > self.maior:
#             self.maior = nivel
#         return dino

#     def posicao(self):
#         """Sorteia um centro com margem suficiente para as imagens do grupo."""
#         x = random.randint(X_MIN + 65, X_MAX - 65)
#         y = random.randint(Y_MIN + 45, Y_MAX - 45)
#         return x, y

#     def nova_caixa(self, nivel):
#         """Reserva uma vaga; devolve False quando o campo esta cheio."""
#         if not self.tem_espaco():
#             return False
#         x, y = self.posicao()
#         self.caixas.add(Caixa(nivel, x, y, self.assets))
#         return True

#     def comprar_dino(self, nivel):
#         """Confere desbloqueio, espaco e dinheiro antes de registrar a compra."""
#         if nivel < 1 or nivel >= NIVEL_MAXIMO:
#             self.avisar("O nivel 20 so pode ser criado por fusao.")
#             return False
#         if nivel > self.limite_compra():
#             self.avisar("Alcance o nivel " + str(nivel + 1) + " para liberar.")
#             return False
#         if not self.tem_espaco():
#             self.avisar("Campo cheio! Junte dois dinossauros.")
#             return False
#         custo = preco_dino(nivel, self.compradas)
#         if self.moedas < custo:
#             self.avisar("Faltam moedas para essa compra.")
#             return False
#         self.moedas -= custo
#         compra_dino(nivel, self.compradas)
#         x, y = self.posicao()
#         self.aparecer_dino(nivel, x, y)
#         self.assets["comprar"].play()
#         self.avisar("Dinossauro nivel " + str(nivel) + " comprado!")
#         return True

#     def comprar_melhoria(self, tipo):
#         """Aplica uma melhoria apenas se ainda houver nivel e saldo disponiveis."""
#         if tipo == "entrega":
#             if self.ent_lvl >= ENT_MAX:
#                 self.avisar("Entrega ja esta no nivel maximo.")
#                 return False
#             custo = self.custo_entrega()
#         else:
#             if self.qual >= QUAL_MAX:
#                 self.avisar("Qualidade ja esta no nivel maximo.")
#                 return False
#             custo = self.custo_qual()
#         if self.moedas < custo:
#             self.avisar("Faltam moedas para essa melhoria.")
#             return False
#         self.moedas -= custo
#         if tipo == "entrega":
#             self.ent_lvl += 1
#             # O contador atual tambem respeita o novo intervalo.
#             if self.timer > self.intervalo() * 1000:
#                 self.timer = self.intervalo() * 1000
#         else:
#             self.qual += 1
#         self.assets["comprar"].play()
#         self.avisar("Melhoria comprada!")
#         return True

#     def mesclar(self, primeiro, segundo):
#         """Dois dinos diferentes do mesmo nivel viram um do nivel seguinte."""
#         if primeiro == segundo or primeiro not in self.dinos or segundo not in self.dinos:
#             return False
#         if primeiro.nivel != segundo.nivel:
#             self.avisar("Escolha dois dinossauros do mesmo nivel.")
#             return False
#         if primeiro.nivel >= NIVEL_MAXIMO:
#             return False
#         nivel = primeiro.nivel + 1
#         x, y = segundo.rect.center
#         primeiro.kill()
#         segundo.kill()
#         self.aparecer_dino(nivel, x, y)
#         self.assets["mesclar"].play()
#         self.avisar("Nova evolucao: " + self.assets["dinos"][nivel]["nome"] + "!")
#         if nivel == NIVEL_MAXIMO:
#             self.venceu = True
#             self.assets["vitoria"].play()
#         return True

#     def coletar_ovo(self, ovo):
#         """Credita um ovo existente uma unica vez."""
#         if ovo not in self.ovos:
#             return False
#         self.moedas += ovo.valor
#         self.avisar("+" + dinheiro(ovo.valor) + " moedas")
#         ovo.kill()
#         self.assets["coletar"].play()
#         return True

#     def sortear_premio(self):
#         """Reproduz os pesos da roleta usando somente randint e um acumulador."""
#         total = 0
#         for peso in PESOS:
#             total += peso
#         sorteio = random.randint(1, total)
#         acumulado = 0
#         for i in range(len(PESOS)):
#             acumulado += PESOS[i]
#             if sorteio <= acumulado:
#                 return i

#     def girar(self):
#         """Inicia quatro segundos de animacao, se a roleta estiver liberada."""
#         if self.girando or self.roleta_cd > 0:
#             self.avisar("A roleta ainda esta em espera.")
#             return False
#         self.premio = self.sortear_premio()
#         self.girando = True
#         self.tempo_giro = 0
#         self.proxima_troca = 0
#         self.resultado = ""
#         return True

#     def dar_premio(self):
#         """Entrega moedas ou uma caixa; campo cheio converte a caixa em moedas."""
#         tipo, valor = PREMIOS[self.premio]
#         if tipo == "renda":
#             ganho = int(self.renda() * valor)
#             if ganho < 25:
#                 ganho = 25
#             self.moedas += ganho
#             self.resultado = "+" + dinheiro(ganho) + " moedas!"
#         else:
#             nivel = self.qual + valor
#             if nivel >= NIVEL_MAXIMO:
#                 nivel = NIVEL_MAXIMO - 1
#             if self.nova_caixa(nivel):
#                 self.resultado = "Caixa com dino nivel " + str(nivel) + "!"
#             else:
#                 ganho = preco_dino(nivel, self.compradas)
#                 self.moedas += ganho
#                 self.resultado = "Campo cheio: +" + dinheiro(ganho) + " moedas!"
#         self.assets["coletar"].play()

#     def atualizar_roleta(self, dt):
#         """Desacelera o destaque dos premios e libera o resultado ao final."""
#         if self.girando:
#             self.tempo_giro += dt
#             if self.tempo_giro >= self.proxima_troca:
#                 self.cursor_roleta += 1
#                 if self.cursor_roleta >= len(PREMIOS):
#                     self.cursor_roleta = 0
#                 self.proxima_troca = self.tempo_giro + 70 + int(280 * (self.tempo_giro / 4000) ** 2)
#             if self.tempo_giro >= 4000:
#                 self.girando = False
#                 self.cursor_roleta = self.premio
#                 self.roleta_cd = COOLDOWN_ROLETA * 1000
#                 self.dar_premio()
#         elif self.roleta_cd > 0:
#             self.roleta_cd -= dt
#             if self.roleta_cd < 0:
#                 self.roleta_cd = 0

#     def update(self, dt, mundo_ativo):
#         """Atualiza o sorteio sempre; menus pausam ovos, dinos e entregas."""
#         self.atualizar_roleta(dt)
#         if self.aviso_t > 0:
#             self.aviso_t -= dt
#         if mundo_ativo:
#             self.tempo += dt
#             for dino in self.dinos:
#                 dino.update(dt)
#             for ovo in objetos_do_grupo(self.ovos):
#                 ovo.update(dt)
#             for caixa in self.caixas:
#                 caixa.update(dt)
#             for dino in self.dinos:
#                 if dino.tempo_ovo <= 0:
#                     dino.tempo_ovo = random.randint(OVO_MIN, OVO_MAX) * 1000
#                     if len(self.ovos) < MAX_OVOS:
#                         x = dino.rect.centerx + random.randint(-14, 14)
#                         y = dino.rect.bottom + 6
#                         self.ovos.add(Ovo(x, y, dino.nivel, self.assets))
#             for caixa in objetos_do_grupo(self.caixas):
#                 if caixa.estado == "parada" and caixa.espera <= 0:
#                     x, y = caixa.rect.center
#                     nivel = caixa.nivel
#                     caixa.kill()
#                     self.aparecer_dino(nivel, x, y)
#             if self.tem_espaco():
#                 self.timer -= dt
#                 if self.timer <= 0:
#                     self.nova_caixa(self.qual)
#                     self.timer = self.intervalo() * 1000

# # Pontos de uma circunferencia para a roleta: evita sin/cos no jogo.
# CIRCULO = [
#     (0, -1000), (98, -995), (195, -981), (290, -957), (383, -924), (471, -882), (556, -831), (634, -773),
#     (707, -707), (773, -634), (831, -556), (882, -471), (924, -383), (957, -290), (981, -195), (995, -98),
#     (1000, 0), (995, 98), (981, 195), (957, 290), (924, 383), (882, 471), (831, 556), (773, 634),
#     (707, 707), (634, 773), (556, 831), (471, 882), (383, 924), (290, 957), (195, 981), (98, 995),
#     (0, 1000), (-98, 995), (-195, 981), (-290, 957), (-383, 924), (-471, 882), (-556, 831), (-634, 773),
#     (-707, 707), (-773, 634), (-831, 556), (-882, 471), (-924, 383), (-957, 290), (-981, 195), (-995, 98),
#     (-1000, 0), (-995, -98), (-981, -195), (-957, -290), (-924, -383), (-882, -471), (-831, -556), (-773, -634),
#     (-707, -707), (-634, -773), (-556, -831), (-471, -882), (-383, -924), (-290, -957), (-195, -981), (-98, -995),
# ]


# # ==================== DESENHOS DA CAIXA E DO OVO ====================

# def poligono_local(tela, cor, pontos, x, y, k=1.0):
#     """Transforma os pontos de um desenho em coordenadas da tela."""
#     vertices = []
#     for dx, dy in pontos:
#         vertices.append((int(x + dx * k), int(y + dy * k)))
#     pygame.draw.polygon(tela, cor, vertices)

# def retangulo(tela, cor, area):
#     """Desenha uma area retangular com quatro vertices."""
#     x, y, largura, altura = area
#     pontos = [(0, 0), (largura, 0), (largura, altura), (0, altura)]
#     poligono_local(tela, cor, pontos, x, y)

# def placa(tela, area, cor, borda=(70, 42, 22)):
#     """Placa com cantos chanfrados, borda, sombra e faces de relevo."""
#     x, y, largura, altura = area
#     contorno = [(8, 0), (largura - 8, 0), (largura, 8),
#                 (largura, altura - 8), (largura - 8, altura), (8, altura),
#                 (0, altura - 8), (0, 8)]
#     poligono_local(tela, (35, 24, 17), contorno, x + 4, y + 5)
#     poligono_local(tela, borda, contorno, x, y)
#     interior = [(9, 3), (largura - 9, 3), (largura - 3, 9),
#                 (largura - 3, altura - 9), (largura - 9, altura - 3),
#                 (9, altura - 3), (3, altura - 9), (3, 9)]
#     poligono_local(tela, cor, interior, x, y)
#     clara = []
#     escura = []
#     for canal in cor:
#         luz = canal + 27
#         sombra = canal - 24
#         if luz > 255:
#             luz = 255
#         if sombra < 0:
#             sombra = 0
#         clara.append(luz)
#         escura.append(sombra)
#     luz = (clara[0], clara[1], clara[2])
#     sombra = (escura[0], escura[1], escura[2])
#     poligono_local(tela, luz, [(9, 3), (largura - 9, 3), (largura - 5, 7), (7, 7)], x, y)
#     poligono_local(tela, luz, [(3, 10), (7, 7), (7, altura - 10), (3, altura - 12)], x, y)
#     poligono_local(tela, sombra, [(9, altura - 7), (largura - 7, altura - 7),
#                     (largura - 9, altura - 3), (9, altura - 3), (5, altura - 7)], x, y)
#     poligono_local(tela, sombra, [(largura - 7, 8), (largura - 3, 10),
#                     (largura - 3, altura - 10), (largura - 7, altura - 7)], x, y)

# def desenhar_ovo(tela, x, y, k=1.0):
#     """Ovo de 18 por 28, com manchas, brilho e sombra no chao."""
#     poligono_local(tela, (66, 43, 27), [(-13, 13), (-8, 10), (7, 10),
#                     (13, 13), (8, 16), (-8, 16)], x, y, k)
#     casca = [(0, -14), (4, -12), (7, -7), (9, 0), (9, 6), (6, 11),
#              (2, 14), (-3, 13), (-7, 10), (-9, 4), (-8, -3), (-5, -10)]
#     poligono_local(tela, (74, 48, 29), casca, x, y, k)
#     poligono_local(tela, (241, 212, 157), [(0, -12), (3, -10), (6, -5),
#                     (7, 1), (7, 6), (4, 10), (1, 12), (-3, 11),
#                     (-6, 8), (-7, 3), (-6, -3), (-3, -9)], x, y, k)
#     poligono_local(tela, (255, 241, 202), [(-1, -11), (2, -9), (4, -4),
#                     (5, 3), (3, 9), (-2, 10), (-5, 7), (-6, 2),
#                     (-5, -4), (-3, -9)], x, y, k)
#     poligono_local(tela, (207, 163, 104), [(7, 2), (7, 6), (4, 10),
#                     (1, 12), (-3, 11), (-5, 9), (1, 10), (5, 7)], x, y, k)
#     detalhes = [(-2, -3, 2, (179, 126, 72)), (3, 4, 2, (191, 139, 79)),
#                 (-3, 7, 1, (194, 146, 89)), (-3, -8, 2, (255, 252, 231)),
#                 (-4, -5, 1, (255, 252, 231))]
#     for dx, dy, raio, cor in detalhes:
#         pygame.draw.circle(tela, cor, (int(x + dx * k), int(y + dy * k)), int(raio * k))

# def desenhar_caixa(tela, x, y, k=1.0):
#     """Madeira em tres faces, com tabuas, pregos e seta de entrega."""
#     poligono_local(tela, (61, 40, 25), [(-28, 22), (-17, 17), (20, 17),
#                     (29, 23), (18, 28), (-18, 28)], x, y, k)
#     poligono_local(tela, (65, 39, 22), [(-23, -13), (-13, -23), (23, -23),
#                     (23, 13), (13, 23), (-23, 23)], x, y, k)
#     poligono_local(tela, (183, 119, 61), [(-21, -11), (13, -11),
#                     (13, 21), (-21, 21)], x, y, k)
#     poligono_local(tela, (227, 169, 94), [(-20, -14), (-12, -21),
#                     (19, -21), (12, -14)], x, y, k)
#     poligono_local(tela, (130, 78, 37), [(15, -12), (21, -19),
#                     (21, 12), (15, 19)], x, y, k)
#     for linha in [-1, 10]:
#         poligono_local(tela, (123, 75, 36), [(-20, linha), (13, linha),
#                         (13, linha + 2), (-20, linha + 2)], x, y, k)
#         poligono_local(tela, (215, 151, 79), [(-19, linha - 1), (12, linha - 1),
#                         (12, linha), (-19, linha)], x, y, k)
#     poligono_local(tela, (165, 98, 43), [(-20, 14), (-15, 20),
#                     (12, -7), (7, -10)], x, y, k)
#     poligono_local(tela, (220, 156, 79), [(-19, 14), (-17, 16),
#                     (9, -10), (7, -10)], x, y, k)
#     poligono_local(tela, (229, 165, 86), [(-21, -11), (-17, -11),
#                     (-17, 20), (-21, 20)], x, y, k)
#     poligono_local(tela, (220, 151, 73), [(-21, 17), (13, 17),
#                     (13, 21), (-21, 21)], x, y, k)
#     poligono_local(tela, (254, 227, 158), [(-5, -8), (4, 1), (-1, 1),
#                     (-1, 11), (-9, 11), (-9, 1), (-14, 1)], x, y, k)
#     for dx, dy in [(-19, -8), (10, -8), (-19, 19), (10, 19)]:
#         pygame.draw.circle(tela, (93, 60, 34),
#                            (int(x + dx * k), int(y + dy * k)), int(2 * k))
#         pygame.draw.circle(tela, (244, 198, 120),
#                            (int(x + (dx - 0.5) * k), int(y + (dy - 0.5) * k)), int(1 * k))

# def desenhar_moeda(tela, x, y, k=1.0):
#     """Moeda dourada com volume, reflexo e um D gravado no centro."""
#     poligono_local(tela, (66, 44, 25), [(-13, 10), (-7, 7), (8, 7),
#                     (14, 11), (7, 14), (-7, 14)], x, y, k)
#     aneis = [(1, 2, 12, (111, 63, 18)), (0, 0, 12, (160, 93, 23)),
#              (0, -1, 10, (255, 207, 74)), (0, -1, 8, (211, 143, 33)),
#              (-1, -2, 7, (255, 212, 79))]
#     for dx, dy, raio, cor in aneis:
#         pygame.draw.circle(tela, cor, (int(x + dx * k), int(y + dy * k)), int(raio * k))
#     poligono_local(tela, (162, 103, 24), [(-3, -7), (1, -7), (4, -4),
#                     (4, 1), (1, 4), (-3, 4)], x, y, k)
#     poligono_local(tela, (255, 217, 89), [(-1, -5), (1, -5), (2, -3),
#                     (2, 0), (1, 2), (-1, 2)], x, y, k)
#     pygame.draw.circle(tela, (255, 246, 181),
#                        (int(x - 4 * k), int(y - 6 * k)), int(2 * k))

# # ==================== MOUSE, MENUS E PARTIDA ====================

# def dentro(pos, area):
#     """Confere se o ponto do mouse esta dentro de uma area de quatro numeros."""
#     x, y = pos
#     ax, ay, largura, altura = area
#     return ax <= x <= ax + largura and ay <= y <= ay + altura


# def distancia_quadrada(x1, y1, x2, y2):
#     """Compara distancias sem math.hypot: elevar ao quadrado e suficiente."""
#     return (x1 - x2) ** 2 + (y1 - y2) ** 2


# def escrever(tela, assets, mensagem, x, y, fonte="fonte", cor=(255, 250, 227), centro=False):
#     """Desenha texto com sombra para continuar legivel sobre a floresta."""
#     imagem = assets[fonte].render(mensagem, True, cor)
#     cor_sombra = (46, 30, 20)
#     if cor[0] < 150 and cor[1] < 150:
#         cor_sombra = (255, 247, 216)
#     sombra = assets[fonte].render(mensagem, True, cor_sombra)
#     rect = imagem.get_rect()
#     rect.x, rect.y = int(x), int(y)
#     if centro:
#         rect.center = (int(x), int(y))
#     tela.blit(sombra, (rect.x + 1, rect.y + 2))
#     tela.blit(imagem, rect)


# def ordenar_dinos(grupo):
#     """Ordena os poucos dinos pelo pe usando comparacoes e troca de posicoes."""
#     lista = objetos_do_grupo(grupo)
#     for i in range(len(lista)):
#         for j in range(len(lista) - 1 - i):
#             if lista[j].rect.bottom > lista[j + 1].rect.bottom:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return lista


# def oval(tela, cor, x, y, rx, ry):
#     """Aproxima uma elipse com pontos fixos e draw.polygon, sem draw.ellipse."""
#     pontos = []
#     for i in range(0, 64, 4):
#         px, py = CIRCULO[i]
#         pontos.append((int(x + px * rx / 1000), int(y + py * ry / 1000)))
#     pygame.draw.polygon(tela, cor, pontos)


# def anel(tela, cor, x, y, rx, ry):
#     """Desenha um anel no chao com pequenos quadrilateros."""
#     for i in range(0, 64, 4):
#         ax, ay = CIRCULO[i]
#         bx, by = CIRCULO[(i + 4) % 64]
#         pontos = [
#             (int(x + ax * rx / 1000), int(y + ay * ry / 1000)),
#             (int(x + bx * rx / 1000), int(y + by * ry / 1000)),
#             (int(x + bx * (rx - 3) / 1000), int(y + by * (ry - 2) / 1000)),
#             (int(x + ax * (rx - 3) / 1000), int(y + ay * (ry - 2) / 1000)),
#         ]
#         pygame.draw.polygon(tela, cor, pontos)


# BTN_DINOS = (448, 10, 90, 35)
# BTN_MELHORIAS = (546, 10, 108, 35)
# BTN_ROLETA = (662, 10, 128, 35)
# BTN_AJUDA = (411, 13, 29, 29)
# BTN_FECHAR = (681, 85, 32, 32)
# BTN_JOGAR = (285, 371, 230, 62)
# BTN_COMO = (302, 453, 196, 37)
# BTN_NOVO = (266, 495, 268, 48)
# BTN_GIRAR = (286, 489, 228, 43)
# BTN_ANTERIOR = (94, 505, 100, 29)
# BTN_PROXIMO = (606, 505, 100, 29)


# class InterfaceMouse:
#     """Mantem o jeito do jogo antigo: clique nos ovos e arraste os dinossauros."""

#     def __init__(self, assets):
#         """Prepara a partida, as telas e as variaveis usadas no arrasto."""
#         self.assets = assets
#         self.partida = Partida(assets)
#         self.estado = "menu"
#         self.voltar_ajuda = "menu"
#         self.painel = ""
#         self.scroll = 0
#         self.mouse = (0, 0)
#         self.arrastado = 0
#         self.offset = (0, 0)
#         self.efeitos = []
#         self.confetes = []
#         self.passo_roda = 0
#         self.inicio_roda = 0
#         self.total_roda = 0
#         self.menu_dinos = []
#         for nivel in [1, 3, 5, 8, 12, 17]:
#             x = random.randint(90, WIDTH - 90)
#             y = random.randint(360, 490)
#             self.menu_dinos.append(Dino(nivel, x, y, assets))

#     def botao(self, tela, area, titulo, cor=(76, 155, 76), ativo=True, fonte="fonte"):
#         """Desenha um botao em relevo e clareia quando o mouse passa por cima."""
#         if not ativo:
#             cor = (142, 137, 115)
#         elif dentro(self.mouse, area):
#             nova_cor = []
#             for canal in cor:
#                 canal += 20
#                 if canal > 255:
#                     canal = 255
#                 nova_cor.append(canal)
#             cor = nova_cor
#         placa(tela, area, cor)
#         x, y, largura, altura = area
#         escrever(tela, self.assets, titulo, x + largura / 2, y + altura / 2 - 1, fonte, centro=True)

#     def iniciar(self):
#         """Uma nova Partida limpa moedas, compras, melhorias e os objetos antigos."""
#         self.partida = Partida(self.assets)
#         self.estado = "jogo"
#         self.painel = ""
#         self.scroll = 0
#         self.arrastado = 0
#         self.efeitos = []
#         self.confetes = []
#         self.passo_roda = 0

#     def area_compra(self, linha):
#         """Calcula a area clicavel do botao Comprar de uma linha visivel."""
#         return (569, 149 + linha * 57, 128, 34)

#     def mudar_scroll(self, passo):
#         """Limita a lista para sempre mostrar apenas seis das vinte linhas."""
#         self.scroll += passo
#         if self.scroll < 0:
#             self.scroll = 0
#         if self.scroll > NIVEL_MAXIMO - 6:
#             self.scroll = NIVEL_MAXIMO - 6

#     def alvo(self, dino):
#         """Encontra o dino igual mais proximo que esta embaixo do arrastado."""
#         melhor = 0
#         menor = 999999
#         for outro in self.partida.dinos:
#             if outro != dino and outro.nivel == dino.nivel and dino.nivel < NIVEL_MAXIMO:
#                 distancia = distancia_quadrada(dino.rect.centerx, dino.rect.centery,
#                                                outro.rect.centerx, outro.rect.centery)
#                 largura = dino.rect.right - dino.rect.left
#                 outra_largura = outro.rect.right - outro.rect.left
#                 alcance = int((largura + outra_largura) * 0.24) + 13
#                 if distancia < alcance ** 2 and distancia < menor:
#                     melhor = outro
#                     menor = distancia
#         return melhor

#     def limitar_dino(self, dino):
#         """Impede que o dino fique fora do campo depois que o jogador o solta."""
#         if dino.rect.left < X_MIN:
#             dino.rect.left = X_MIN
#         if dino.rect.right > X_MAX:
#             dino.rect.right = X_MAX
#         if dino.rect.top < Y_MIN:
#             dino.rect.top = Y_MIN
#         if dino.rect.bottom > Y_MAX:
#             dino.rect.bottom = Y_MAX
#         dino.x, dino.y = dino.rect.x, dino.rect.y

#     def soltar(self):
#         """Ao soltar, junta uma dupla valida ou deixa o dino no novo lugar."""
#         if self.arrastado != 0:
#             dino = self.arrastado
#             outro = self.alvo(dino)
#             if outro != 0:
#                 x, y = outro.rect.center
#                 if self.partida.mesclar(dino, outro):
#                     self.efeitos.append([x, y, 600])
#             else:
#                 self.limitar_dino(dino)
#             dino.preso = False
#             self.arrastado = 0

#     def pegar_no_campo(self, pos):
#         """Prioriza ovos e depois escolhe o dino desenhado por cima dos outros."""
#         ovos = objetos_do_grupo(self.partida.ovos)
#         indice = len(ovos) - 1
#         coletou = False
#         while indice >= 0 and not coletou:
#             ovo = ovos[indice]
#             if distancia_quadrada(pos[0], pos[1], ovo.rect.centerx, ovo.rect.centery) <= 23 ** 2:
#                 self.partida.coletar_ovo(ovo)
#                 coletou = True
#             indice -= 1
#         if not coletou:
#             dinos = ordenar_dinos(self.partida.dinos)
#             indice = len(dinos) - 1
#             while indice >= 0 and self.arrastado == 0:
#                 dino = dinos[indice]
#                 r = dino.rect
#                 area = (r.left, r.top, r.right - r.left, r.bottom - r.top)
#                 if dentro(pos, area):
#                     self.arrastado = dino
#                     dino.preso = True
#                     dino.vx, dino.vy = 0, 0
#                     self.offset = (pos[0] - r.centerx, pos[1] - r.centery)
#                 indice -= 1

#     def clique_painel(self, pos):
#         """Encaminha os cliques dos tres paineis para as regras da partida."""
#         p = self.partida
#         if dentro(pos, BTN_FECHAR):
#             self.painel = ""
#         elif self.painel == "dinos":
#             if dentro(pos, BTN_ANTERIOR):
#                 self.mudar_scroll(-6)
#             elif dentro(pos, BTN_PROXIMO):
#                 self.mudar_scroll(6)
#             else:
#                 for linha in range(6):
#                     if dentro(pos, self.area_compra(linha)):
#                         p.comprar_dino(self.scroll + linha + 1)
#         elif self.painel == "melhorias":
#             if dentro(pos, (541, 204, 156, 43)):
#                 p.comprar_melhoria("entrega")
#             elif dentro(pos, (541, 347, 156, 43)):
#                 p.comprar_melhoria("qualidade")
#         elif self.painel == "roleta" and dentro(pos, BTN_GIRAR):
#             if p.girar():
#                 self.inicio_roda = self.passo_roda
#                 destino = (-p.premio * 8 - 4) % 64
#                 self.total_roda = (destino - self.inicio_roda) % 64 + 64 * 5

#     def evento(self, evento):
#         """EXTRA AUTORIZADO: le clique, soltura e rodinha do mouse."""
#         if evento.type == pygame.MOUSEWHEEL:
#             if self.estado == "jogo" and self.painel == "dinos":
#                 self.mudar_scroll(-evento.y)
#         elif evento.type == pygame.MOUSEBUTTONUP:
#             if evento.button == 1:
#                 self.soltar()
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             if evento.button == 1:
#                 pos = evento.pos
#                 self.mouse = pos
#                 if self.estado == "menu":
#                     if dentro(pos, BTN_JOGAR):
#                         self.iniciar()
#                     elif dentro(pos, BTN_COMO):
#                         self.voltar_ajuda = "menu"
#                         self.estado = "ajuda"
#                 elif self.estado == "ajuda":
#                     if dentro(pos, BTN_FECHAR) or dentro(pos, (286, 485, 228, 43)):
#                         self.estado = self.voltar_ajuda
#                 elif self.estado == "vitoria":
#                     if dentro(pos, BTN_NOVO):
#                         self.iniciar()
#                 elif self.estado == "jogo":
#                     novo_painel = ""
#                     if dentro(pos, BTN_DINOS):
#                         novo_painel = "dinos"
#                     elif dentro(pos, BTN_MELHORIAS):
#                         novo_painel = "melhorias"
#                     elif dentro(pos, BTN_ROLETA):
#                         novo_painel = "roleta"
#                     if novo_painel != "":
#                         if self.painel == novo_painel:
#                             self.painel = ""
#                         else:
#                             self.painel = novo_painel
#                     elif dentro(pos, BTN_AJUDA):
#                         self.voltar_ajuda = "jogo"
#                         self.estado = "ajuda"
#                     elif self.painel != "":
#                         self.clique_painel(pos)
#                     elif pos[1] >= 90:
#                         self.pegar_no_campo(pos)

#     def update(self, dt):
#         """EXTRA AUTORIZADO: acompanha o cursor para hover e arrasto suave."""
#         self.mouse = pygame.mouse.get_pos()
#         if self.estado == "menu":
#             for dino in self.menu_dinos:
#                 dino.update(dt)
#         elif self.estado == "jogo":
#             estava_girando = self.partida.girando
#             if self.arrastado != 0:
#                 dino = self.arrastado
#                 dino.rect.center = (self.mouse[0] - self.offset[0], self.mouse[1] - self.offset[1])
#                 dino.x, dino.y = dino.rect.x, dino.rect.y
#             self.partida.update(dt, self.painel == "")
#             if estava_girando:
#                 progresso = self.partida.tempo_giro / 4000
#                 if progresso > 1:
#                     progresso = 1
#                 suavizado = 1 - (1 - progresso) ** 3
#                 self.passo_roda = int(self.inicio_roda + self.total_roda * suavizado) % 64
#             novos = []
#             for efeito in self.efeitos:
#                 efeito[2] -= dt
#                 if efeito[2] > 0:
#                     novos.append(efeito)
#             self.efeitos = novos
#             if self.partida.venceu:
#                 self.estado = "vitoria"
#                 self.painel = ""
#         elif self.estado == "vitoria":
#             if len(self.confetes) < 120:
#                 self.confetes.append([random.randint(8, WIDTH - 8), -8, random.randint(65, 170), random.randint(0, 3)])
#             novos = []
#             for confete in self.confetes:
#                 confete[1] += confete[2] * dt / 1000
#                 if confete[1] < HEIGHT:
#                     novos.append(confete)
#             self.confetes = novos

#     def desenhar_dino(self, tela, dino):
#         """Mostra a imagem do grupo sem o fundo preto e um selo com o nivel."""
#         r = dino.rect
#         oval(tela, (59, 43, 25), r.centerx, r.bottom - 2, 27, 7)
#         tela.blit(dino.image, r)
#         cor = (241, 215, 147)
#         if dino.nivel >= 15:
#             cor = (255, 207, 67)
#         elif dino.nivel >= 8:
#             cor = (174, 147, 238)
#         pygame.draw.circle(tela, (66, 42, 23), (r.centerx, r.bottom + 9), 11)
#         escrever(tela, self.assets, str(dino.nivel), r.centerx, r.bottom + 8, "pequena", cor, True)

#     def desenhar(self, tela):
#         """Escolhe a tela; na partida o cenario inteiro continua aparecendo."""
#         tela.blit(self.assets["fundo"], (0, 0))
#         if self.estado == "menu":
#             self.desenhar_menu(tela)
#         elif self.estado == "ajuda":
#             self.desenhar_ajuda(tela)
#         elif self.estado == "vitoria":
#             self.desenhar_vitoria(tela)
#         else:
#             self.desenhar_campo(tela)
#             self.desenhar_hud(tela)
#             if self.painel == "dinos":
#                 self.desenhar_loja(tela)
#             elif self.painel == "melhorias":
#                 self.desenhar_melhorias(tela)
#             elif self.painel == "roleta":
#                 self.desenhar_roleta(tela)
#             if self.partida.aviso_t > 0:
#                 y_aviso = 105
#                 if self.painel != "":
#                     y_aviso = 563
#                 escrever(tela, self.assets, self.partida.aviso, WIDTH / 2, y_aviso, "fonte", (255, 242, 168), True)

#     def desenhar_menu(self, tela):
#         """Reaproveita a composicao do antigo: titulo, objetivo e botao Jogar."""
#         for dino in self.menu_dinos:
#             self.desenhar_dino(tela, dino)
#         placa(tela, (82, 88, 636, 205), (95, 63, 34))
#         placa(tela, (91, 96, 618, 187), (45, 70, 43))
#         escrever(tela, self.assets, "DinoEvolution", 400, 145, "titulo", (255, 216, 86), True)
#         escrever(tela, self.assets, "Junte dinos iguais ate criar o Rei T-Rex!", 400, 207, "fonte", (255, 250, 224), True)
#         escrever(tela, self.assets, "Arraste para evoluir. Clique nos ovos para ganhar moedas.", 400, 244, "pequena", (255, 248, 215), True)
#         self.botao(tela, BTN_JOGAR, "JOGAR", (77, 165, 76), fonte="grande")
#         self.botao(tela, BTN_COMO, "Como jogar", (155, 107, 54))

#     def desenhar_campo(self, tela):
#         """Desenha o dino arrastado por ultimo e destaca o alvo da fusao."""
#         for dino in ordenar_dinos(self.partida.dinos):
#             if dino != self.arrastado:
#                 self.desenhar_dino(tela, dino)
#         for caixa in self.partida.caixas:
#             desenhar_caixa(tela, caixa.rect.centerx, caixa.rect.centery)
#         for ovo in self.partida.ovos:
#             if ovo.vida >= 3000 or int(ovo.vida / 200) % 2 == 0:
#                 desenhar_ovo(tela, ovo.rect.centerx, ovo.rect.centery)
#         for efeito in self.efeitos:
#             tamanho = 20 + int((600 - efeito[2]) / 20)
#             anel(tela, (255, 231, 122), efeito[0], efeito[1], tamanho, int(tamanho / 2))
#         if self.arrastado != 0:
#             alvo = self.alvo(self.arrastado)
#             if alvo != 0:
#                 anel(tela, (255, 232, 88), alvo.rect.centerx, alvo.rect.bottom - 1, 43, 13)
#             self.desenhar_dino(tela, self.arrastado)
#         retangulo(tela, (65, 46, 27), (0, HEIGHT - 23, WIDTH, 23))
#         escrever(tela, self.assets, "Arraste dinos iguais para juntar  |  Clique nos ovos  |  Use a loja e a roleta", 400, HEIGHT - 13, "pequena", centro=True)

#     def desenhar_hud(self, tela):
#         """Mantem os tres botoes do antigo e a barra da proxima entrega."""
#         p = self.partida
#         retangulo(tela, (87, 58, 30), (0, 0, WIDTH, 58))
#         retangulo(tela, (132, 91, 47), (0, 0, WIDTH, 4))
#         desenhar_moeda(tela, 22, 25, 0.8)
#         escrever(tela, self.assets, dinheiro(p.moedas), 43, 10, "grande")
#         escrever(tela, self.assets, dinheiro(p.renda()) + "/s em ovos", 45, 38, "pequena", (255, 221, 122))
#         escrever(tela, self.assets, "Dinos " + str(p.ocupados()) + "/20", 272, 9, "fonte")
#         escrever(tela, self.assets, "Melhor: Nv " + str(p.maior), 273, 35, "pequena", (198, 242, 154))
#         self.botao(tela, BTN_AJUDA, "?", (145, 100, 55), fonte="pequena")
#         self.botao(tela, BTN_DINOS, "Dinos", (76, 151, 76))
#         self.botao(tela, BTN_MELHORIAS, "Melhorias", (92, 126, 183), fonte="pequena")
#         titulo = "ROLETA!"
#         if p.girando:
#             titulo = "Girando..."
#         elif p.roleta_cd > 0:
#             titulo = "Roleta " + str(int((p.roleta_cd + 999) / 1000)) + "s"
#         self.botao(tela, BTN_ROLETA, titulo, (198, 126, 41), fonte="pequena")
#         retangulo(tela, (59, 42, 23), (0, 58, WIDTH, 8))
#         progresso = 1 - p.timer / (p.intervalo() * 1000)
#         if progresso < 0:
#             progresso = 0
#         if progresso > 1:
#             progresso = 1
#         retangulo(tela, (139, 205, 74), (0, 58, int(WIDTH * progresso), 8))
#         texto = "Proxima caixa (Nv " + str(p.qual) + ") em " + str(int((p.timer + 999) / 1000)) + "s"
#         if not p.tem_espaco():
#             texto = "Campo cheio! Junte dinos para abrir espaco."
#         if self.painel == "":
#             escrever(tela, self.assets, texto, 12, 73, "pequena")

#     def painel_base(self, tela, titulo, detalhe):
#         """Desenha um painel claro de madeira, como os menus do jogo antigo."""
#         placa(tela, (70, 72, 660, 480), (242, 224, 172))
#         retangulo(tela, (147, 99, 48), (83, 84, 634, 40))
#         escrever(tela, self.assets, titulo, 400, 104, "grande", (255, 239, 184), True)
#         self.botao(tela, BTN_FECHAR, "X", (191, 73, 49), fonte="pequena")
#         escrever(tela, self.assets, detalhe, 400, 135, "pequena", (93, 63, 32), True)

#     def desenhar_loja(self, tela):
#         """Lista dinos com suas proprias imagens e botoes de compra clicaveis."""
#         p = self.partida
#         self.painel_base(tela, "LOJA DE DINOS", "Use a rodinha do mouse ou as setas abaixo para ver os niveis.")
#         for linha in range(6):
#             nivel = self.scroll + linha + 1
#             y = 145 + linha * 57
#             retangulo(tela, (255, 244, 205), (88, y, 624, 51))
#             imagem = self.assets["dinos"][nivel]["mini"]
#             r = imagem.get_rect()
#             r.center = (127, y + 25)
#             tela.blit(imagem, r)
#             escrever(tela, self.assets, "Nv " + str(nivel) + "  " + self.assets["dinos"][nivel]["nome"], 171, y + 5, "pequena", (77, 48, 24))
#             escrever(tela, self.assets, "Ovo: " + dinheiro(valor_ovo(nivel)) + "  |  Comprados: " + str(p.compradas[nivel - 1]), 171, y + 27, "pequena", (117, 86, 44))
#             preco = preco_dino(nivel, p.compradas)
#             mensagem = dinheiro(preco)
#             ativo = nivel <= p.limite_compra() and p.moedas >= preco
#             if nivel == NIVEL_MAXIMO:
#                 mensagem = "So por fusao"
#                 ativo = False
#             elif nivel > p.limite_compra():
#                 mensagem = "Alcance " + str(nivel + 1)
#             self.botao(tela, self.area_compra(linha), mensagem, ativo=ativo, fonte="pequena")
#         self.botao(tela, BTN_ANTERIOR, "< Voltar", (158, 111, 59), self.scroll > 0, "pequena")
#         self.botao(tela, BTN_PROXIMO, "Proximo >", (158, 111, 59), self.scroll < 14, "pequena")
#         escrever(tela, self.assets, "Niveis " + str(self.scroll + 1) + " a " + str(self.scroll + 6) + " de 20", 400, 520, "pequena", (99, 68, 33), True)

#     def desenhar_melhorias(self, tela):
#         """Mostra os efeitos e precos antes de comprar uma melhoria."""
#         p = self.partida
#         self.painel_base(tela, "MELHORIAS", "Entregas mais rapidas e dinossauros melhores nas caixas.")
#         titulos = ["Entrega rapida", "Qualidade das caixas"]
#         textos = ["Uma caixa a cada " + str(p.intervalo()) + " segundos", "Caixas trazem dino nivel " + str(p.qual)]
#         custos = [p.custo_entrega(), p.custo_qual()]
#         niveis = [p.ent_lvl, p.qual - 1]
#         maximos = [ENT_MAX, QUAL_MAX - 1]
#         for i in range(2):
#             y = 173 + i * 143
#             placa(tela, (89, y, 622, 120), (255, 244, 206))
#             escrever(tela, self.assets, titulos[i], 110, y + 13, "grande", (87, 52, 24))
#             escrever(tela, self.assets, textos[i], 112, y + 53, "pequena", (121, 86, 43))
#             retangulo(tela, (140, 111, 65), (112, y + 89, 367, 12))
#             retangulo(tela, (111, 179, 77), (112, y + 89, int(367 * niveis[i] / maximos[i]), 12))
#             titulo = dinheiro(custos[i])
#             if niveis[i] == maximos[i]:
#                 titulo = "MAXIMO"
#             self.botao(tela, (541, y + 31, 156, 43), titulo, ativo=niveis[i] < maximos[i] and p.moedas >= custos[i])
#         escrever(tela, self.assets, "Cada melhoria vale para toda a partida.", 400, 493, "fonte", (110, 75, 33), True)

#     def desenhar_roleta(self, tela):
#         """Desenha uma roleta circular animada com pontos fixos, sem sin/cos."""
#         p = self.partida
#         self.painel_base(tela, "ROLETA DA EVOLUCAO", "Gire para ganhar moedas ou uma caixa especial.")
#         cx, cy, raio = 400, 299, 124
#         pygame.draw.circle(tela, (105, 64, 26), (cx + 3, cy + 6), raio + 10)
#         pygame.draw.circle(tela, (239, 182, 67), (cx, cy), raio + 8)
#         cores = [(207, 92, 65), (223, 175, 68), (101, 161, 87), (87, 135, 182),
#                  (203, 129, 68), (134, 112, 180), (95, 164, 152), (204, 104, 135)]
#         rotulos = ["+30s", "Caixa", "+60s", "Cx +1", "+15s", "Caixa", "+2min", "Cx +2"]
#         for i in range(8):
#             pontos = [(cx, cy)]
#             for j in range(9):
#                 px, py = CIRCULO[(i * 8 + j + self.passo_roda) % 64]
#                 pontos.append((int(cx + raio * px / 1000), int(cy + raio * py / 1000)))
#             pygame.draw.polygon(tela, cores[i], pontos)
#             px, py = CIRCULO[(i * 8 + 4 + self.passo_roda) % 64]
#             escrever(tela, self.assets, rotulos[i], cx + 82 * px / 1000, cy + 82 * py / 1000, "pequena", centro=True)
#         pygame.draw.circle(tela, (126, 79, 32), (cx, cy), 19)
#         desenhar_moeda(tela, cx, cy, 0.9)
#         pygame.draw.polygon(tela, (93, 49, 24), [(383, 161), (417, 161), (400, 192)])
#         pygame.draw.polygon(tela, (255, 215, 86), [(388, 164), (412, 164), (400, 185)])
#         mensagem = p.resultado
#         if mensagem == "":
#             mensagem = "+Ns = segundos da renda | Caixa = dino gratis"
#         escrever(tela, self.assets, mensagem, 400, 453, "fonte", (89, 59, 27), True)
#         titulo = "GIRAR!"
#         if p.girando:
#             titulo = "Girando..."
#         elif p.roleta_cd > 0:
#             titulo = "Volta em " + str(int((p.roleta_cd + 999) / 1000)) + "s"
#         self.botao(tela, BTN_GIRAR, titulo, (213, 129, 46), not p.girando and p.roleta_cd == 0)

#     def desenhar_ajuda(self, tela):
#         """Ensina os controles com mouse usando exemplos do ovo e da caixa."""
#         self.painel_base(tela, "COMO JOGAR", "Tudo funciona com o mouse, como na referencia original.")
#         linhas = ["Segure um dinossauro e arraste para outro do mesmo nivel.",
#                   "Solte em cima dele: os dois viram um dino mais evoluido.",
#                   "Clique nos ovos para ganhar moedas antes que desaparecam.",
#                   "Use Dinos para comprar. Use Melhorias para evoluir as entregas.",
#                   "Gire a roleta a cada 40 segundos para receber um premio.",
#                   "A loja e os paineis pausam o campo. Feche no X para continuar.",
#                   "Objetivo: juntar dois dinos nivel 19 e criar o Rei T-Rex!"]
#         for i in range(len(linhas)):
#             escrever(tela, self.assets, linhas[i], 105, 178 + i * 32, "pequena", (94, 61, 29))
#         desenhar_ovo(tela, 255, 438, 1.3)
#         desenhar_caixa(tela, 545, 434, 0.9)
#         self.botao(tela, (286, 485, 228, 43), "ENTENDI!", (76, 158, 78))

#     def desenhar_vitoria(self, tela):
#         """Apresenta o T-Rex final, tempo, confetes e o botao de reinicio."""
#         placa(tela, (100, 74, 600, 474), (240, 219, 157))
#         escrever(tela, self.assets, "VITORIA!", 400, 124, "titulo", (117, 68, 23), True)
#         escrever(tela, self.assets, "Voce criou o Rei T-Rex!", 400, 184, "grande", (91, 111, 49), True)
#         imagem = self.assets["dinos"][20]["vitoria"]
#         r = imagem.get_rect()
#         r.center = (400, 337)
#         tela.blit(imagem, r)
#         segundos = int(self.partida.tempo / 1000)
#         escrever(tela, self.assets, "Tempo: " + str(int(segundos / 60)) + " min " + str(segundos % 60) + " s", 400, 455, "fonte", (106, 73, 34), True)
#         self.botao(tela, BTN_NOVO, "Jogar de novo", (80, 157, 76), fonte="grande")
#         cores = [(255, 208, 70), (113, 202, 99), (246, 125, 91), (124, 184, 237)]
#         for confete in self.confetes:
#             retangulo(tela, cores[confete[3]], (int(confete[0]), int(confete[1]), 5, 8))


# def main():
#     """Executa inicializacao, eventos de mouse, atualizacao e desenho."""
#     pygame.init()
#     pygame.mixer.init()
#     window = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("DinoEvolution!")
#     relogio = pygame.time.Clock()
#     assets = carregar_assets()
#     interface = InterfaceMouse(assets)
#     pygame.mixer.music.play(loops=-1)
#     rodando = True
#     while rodando:
#         dt = relogio.tick(FPS)
#         if dt > 100:
#             dt = 100
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 rodando = False
#             else:
#                 interface.evento(evento)
#         if rodando:
#             interface.update(dt)
#             interface.desenhar(window)
#             pygame.display.update()
#     pygame.quit()


# main()
#"""main.py — Arquivo principal do DinoEvolution (sprites, logica da partida, interface e loop)."""
import pygame
import random
from config import *
from assets import *


# ==================== FUNCOES AUXILIARES DE LOGICA ====================
def valor_ovo(n):  # Calcula o valor em moedas de um ovo conforme o nivel do dino (1, 2, 4, 8...).
    return 2 ** (n - 1)


def preco_dino(n, lista_de_dinossauro):  # Calcula o preco atual de compra de um dinossauro na loja.
    return 10 * valor_ovo(n) + 30 * lista_de_dinossauro[n - 1]


def compra_dino(n, lista_de_dinossauro):  # Registra +1 na quantidade de dinossauros comprados daquele nivel.
    lista_de_dinossauro[n - 1] += 1

<<<<<<< HEAD
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

def dinheiro(n):
    n = float(n)
    for qtd in ["", "k", "M", "B", "T"]:
        if abs(n) < 1000 or qtd == "T":
            if qtd == "":
                return str(int(n))
            return f"{n:.1f}{qtd}" if n < 100 else f"{int(n)}{qtd}"
        n /= 1000

def montar_info():
    info = {}
    for n in range(1, NIVEL_MAXIMO + 1):
        nome, imagem, escala = BASE[n - 1]
=======

def dinheiro(n):  # Abrevia valores grandes de moedas usando sufixos k, M, B e T.
    if n >= 1000000000000:
        return str(int(n / 1000000000000)) + "T"
    elif n >= 1000000000:
        return str(int(n / 1000000000)) + "B"
    elif n >= 1000000:
        return str(int(n / 1000000)) + "M"
    elif n >= 1000:
        return str(int(n / 1000)) + "k"
    return str(int(n))
>>>>>>> 84a6067887d5f636722f58a839fa9fa6dfe9bd9b


<<<<<<< HEAD
    return info
INFO = montar_info()

=======
def itens_do_jogo(itens):  # Converte um grupo de sprites do Pygame em uma lista comum.
    lista = []
    for item in itens:
        lista.append(item)
    return lista


def dentro(pos, area):  # Verifica se o ponto (x, y) do mouse esta dentro do retangulo area.
    x, y = pos
    ax, ay, largura, altura = area
    if ax <= x <= ax + largura and ay <= y <= ay + altura:
        return True
    else:
        return False


def calcular_distancia(x1, y1, x2, y2):  # Calcula a distancia real em pixels entre dois pontos.
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def ordenar_dinos(itens):  # Ordena os dinos pela base (rect.bottom) para dar nocao de profundidade.
    lista = itens_do_jogo(itens)
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j].rect.bottom > lista[j + 1].rect.bottom:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# ==================== PERSONAGENS (SPRITES) ====================
class Dino(pygame.sprite.Sprite):
    """Um dinossauro com nivel, movimento e contador para produzir ovos."""

    def __init__(self, nivel, x, y, assets):  # Cria um dinossauro no campo com nivel, posicao e timers.
        pygame.sprite.Sprite.__init__(self)
        self.nivel = nivel
        self.image = assets["dinos"][nivel]["imagem"]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = self.rect.x
        self.y = self.rect.y
        self.vx = 0
        self.vy = 0
        self.tempo_direcao = 0
        self.tempo_ovo = random.randint(OVO_MIN, OVO_MAX) * 1000
        self.preso = False
        self.escolher_direcao()

    def escolher_direcao(self):  # Sorteia se o dinossauro fica parado ou anda em uma nova direcao.
        if random.randint(1, 10) <= 3:
            self.vx, self.vy = 0, 0
        else:
            self.vx = random.randint(-43, 43) / 1000
            self.vy = random.randint(-19, 19) / 1000
        self.tempo_direcao = random.randint(1000, 3000)

    def update(self, dt):  # Atualiza o contador de ovos e move o dino dentro dos limites do gramado.
        self.tempo_ovo -= dt
        if not self.preso:
            self.tempo_direcao -= dt
            if self.tempo_direcao <= 0:
                self.escolher_direcao()
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)
            if self.rect.left < X_MIN:
                self.rect.left = X_MIN
                self.x = self.rect.x
                self.vx = -self.vx
            if self.rect.right > X_MAX:
                self.rect.right = X_MAX
                self.x = self.rect.x
                self.vx = -self.vx
            if self.rect.top < Y_MIN:
                self.rect.top = Y_MIN
                self.y = self.rect.y
                self.vy = -self.vy
            if self.rect.bottom > Y_MAX:
                self.rect.bottom = Y_MAX
                self.y = self.rect.y
                self.vy = -self.vy


class Ovo(pygame.sprite.Sprite):
    """Um ovo coletavel, com valor ligado ao nivel e vida de doze segundos."""

    def __init__(self, x, y, nivel, assets):  # Cria um ovo na posicao (x, y) com valor proporcional ao nivel.
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["ovo"].render("O", True, (255, 240, 194))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.valor = valor_ovo(nivel)
        self.vida = VIDA_OVO * 1000

    def update(self, dt):  # Desconta o tempo de vida do ovo e remove-o se passar de 12 segundos.
        self.vida -= dt
        if self.vida <= 0:
            self.kill()


class Caixa(pygame.sprite.Sprite):
    """Uma entrega que cai no campo e depois se transforma em um dinossauro."""

    def __init__(self, nivel, x, y, assets):  # Cria uma caixa acima da tela que vai cair ate o ponto (x, y).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["grande"].render("?", True, (255, 225, 144))
        self.rect = self.image.get_rect()
        self.rect.center = (x, -30)
        self.y = -30
        self.y_alvo = y
        self.nivel = nivel
        self.espera = 700
        self.estado = "caindo"

    def update(self, dt):  # Anima a queda da caixa ate o chao e conta 0,7s antes de abrir.
        if self.estado == "caindo":
            self.y += 0.45 * dt
            if self.y >= self.y_alvo:
                self.y = self.y_alvo
                self.estado = "parada"
            self.rect.centery = int(self.y)
        else:
            self.espera -= dt


# ==================== REGRAS DA PARTIDA ====================
class Partida:
    """Guarda moedas, sprites, compras, melhorias, sorteio e condicao de vitoria."""

    def __init__(self, assets):  # Inicia uma partida nova com 100 moedas e dois dinos nivel 1.
        self.assets = assets
        self.moedas = 100
        self.dinos = pygame.sprite.Group()
        self.ovos = pygame.sprite.Group()
        self.caixas = pygame.sprite.Group()
        self.compradas = [0] * NIVEL_MAXIMO
        self.ent_lvl = 0
        self.qual = 1
        self.maior = 1
        self.timer = 3000
        self.tempo = 0
        self.aviso = "Junte dois dinos iguais para evoluir!"
        self.aviso_t = 4000
        self.venceu = False
        self.girando = False
        self.tempo_giro = 0
        self.proxima_troca = 0
        self.roleta_cd = 0
        self.cursor_roleta = 0
        self.premio = 0
        self.resultado = ""
        self.aparecer_dino(1, 260, 340)
        self.aparecer_dino(1, 510, 390)

    def avisar(self, mensagem):  # Mostra uma mensagem rapida na tela por 2,8 segundos.
        self.aviso = mensagem
        self.aviso_t = 2800

    def ocupados(self):  # Retorna a soma de dinossauros vivos e caixas fechadas no campo.
        return len(self.dinos) + len(self.caixas)

    def tem_espaco(self):  # Verifica se ainda cabe mais um dinossauro ou caixa no campo.
        return self.ocupados() < MAX_DINOS

    def renda(self):  # Calcula a media de moedas geradas por segundo pelos dinos atuais.
        total = 0
        for dino in self.dinos:
            total += valor_ovo(dino.nivel)
        return total / MEDIA_OVO

    def intervalo(self):  # Retorna o intervalo atual (em segundos) entre entregas automaticas.
        segundos = ENTREGA_BASE - ENTREGA_PASSO * self.ent_lvl
        if segundos < ENTREGA_MIN:
            segundos = ENTREGA_MIN
        return segundos

    def limite_compra(self):  # Calcula o nivel maximo desbloqueado para compra na loja.
        limite = self.maior - 1
        if limite < 4:
            limite = 4
        if limite >= NIVEL_MAXIMO:
            limite = NIVEL_MAXIMO - 1
        return limite

    def custo_entrega(self):  # Retorna o preco da proxima melhoria de velocidade de entrega.
        return int(120 * 3 ** self.ent_lvl)

    def custo_qual(self):  # Retorna o preco da proxima melhoria de qualidade das caixas.
        return int(60 * 2.5 ** self.qual)

    def aparecer_dino(self, nivel, x, y):  # Cria um dinossauro no campo e atualiza o maior nivel alcancado.
        dino = Dino(nivel, x, y, self.assets)
        self.dinos.add(dino)
        if nivel > self.maior:
            self.maior = nivel
        return dino

    def posicao(self):  # Sorteia uma coordenada (x, y) valida dentro do gramado.
        x = random.randint(X_MIN + 65, X_MAX - 65)
        y = random.randint(Y_MIN + 45, Y_MAX - 45)
        return x, y

    def nova_caixa(self, nivel):  # Faz cair uma nova caixa no campo se houver vaga disponivel.
        if not self.tem_espaco():
            return False
        x, y = self.posicao()
        self.caixas.add(Caixa(nivel, x, y, self.assets))
        return True

    def comprar_dino(self, nivel):  # Confere desbloqueio, espaco e moedas antes de comprar um dino.
        if nivel < 1 or nivel >= NIVEL_MAXIMO:
            self.avisar("O nivel 20 so pode ser criado por fusao.")
            return False
        if nivel > self.limite_compra():
            self.avisar("Alcance o nivel " + str(nivel + 1) + " para liberar.")
            return False
        if not self.tem_espaco():
            self.avisar("Campo cheio! Junte dois dinossauros.")
            return False
        custo = preco_dino(nivel, self.compradas)
        if self.moedas < custo:
            self.avisar("Faltam moedas para essa compra.")
            return False
        self.moedas -= custo
        compra_dino(nivel, self.compradas)
        x, y = self.posicao()
        self.aparecer_dino(nivel, x, y)
        self.assets["comprar"].play()
        self.avisar("Dinossauro nivel " + str(nivel) + " comprado!")
        return True

    def comprar_melhoria(self, tipo):  # Aplica uma melhoria de entrega ou qualidade das caixas.
        if tipo == "entrega":
            if self.ent_lvl >= ENT_MAX:
                self.avisar("Entrega ja esta no nivel maximo.")
                return False
            custo = self.custo_entrega()
        else:
            if self.qual >= QUAL_MAX:
                self.avisar("Qualidade ja esta no nivel maximo.")
                return False
            custo = self.custo_qual()
        if self.moedas < custo:
            self.avisar("Faltam moedas para essa melhoria.")
            return False
        self.moedas -= custo
        if tipo == "entrega":
            self.ent_lvl += 1
            if self.timer > self.intervalo() * 1000:
                self.timer = self.intervalo() * 1000
        else:
            self.qual += 1
        self.assets["comprar"].play()
        self.avisar("Melhoria comprada!")
        return True

    def mesclar(self, primeiro, segundo):  # Funde dois dinos iguais em um de nivel superior e verifica vitoria.
        if primeiro == segundo or primeiro not in self.dinos or segundo not in self.dinos:
            return False
        if primeiro.nivel != segundo.nivel:
            self.avisar("Escolha dois dinossauros do mesmo nivel.")
            return False
        if primeiro.nivel >= NIVEL_MAXIMO:
            return False
        nivel = primeiro.nivel + 1
        x, y = segundo.rect.center
        primeiro.kill()
        segundo.kill()
        self.aparecer_dino(nivel, x, y)
        self.assets["encaixe"].play()
        self.avisar("Nova evolucao: " + self.assets["dinos"][nivel]["nome"] + "!")
        if nivel == NIVEL_MAXIMO:
            self.venceu = True
            self.assets["vitoria"].play()
        return True

    def coletar_ovo(self, ovo):  # Adiciona o valor do ovo as moedas e remove o ovo da tela.
        if ovo not in self.ovos:
            return False
        self.moedas += ovo.valor
        self.avisar("+" + dinheiro(ovo.valor) + " moedas")
        ovo.kill()
        self.assets["coletar"].play()
        return True

    def sortear_premio(self):  # Sorteia um premio da roleta respeitando os pesos definidos em config.py.
        total = 0
        for peso in PESOS:
            total += peso
        sorteio = random.randint(1, total)
        acumulado = 0
        for i in range(len(PESOS)):
            acumulado += PESOS[i]
            if sorteio <= acumulado:
                return i

    def girar(self):  # Inicia a animacao de giro da roleta se nao estiver em recarga.
        if self.girando or self.roleta_cd > 0:
            self.avisar("A roleta ainda esta em espera.")
            return False
        self.premio = self.sortear_premio()
        self.girando = True
        self.tempo_giro = 0
        self.proxima_troca = 0
        self.resultado = ""
        return True

    def dar_premio(self):  # Entrega moedas ou uma caixa ao finalizar o giro da roleta.
        tipo, valor = PREMIOS[self.premio]
        if tipo == "renda":
            ganho = int(self.renda() * valor)
            if ganho < 25:
                ganho = 25
            self.moedas += ganho
            self.resultado = "+" + dinheiro(ganho) + " moedas!"
        else:
            nivel = self.qual + valor
            if nivel >= NIVEL_MAXIMO:
                nivel = NIVEL_MAXIMO - 1
            if self.nova_caixa(nivel):
                self.resultado = "Caixa com dino nivel " + str(nivel) + "!"
            else:
                ganho = preco_dino(nivel, self.compradas)
                self.moedas += ganho
                self.resultado = "Campo cheio: +" + dinheiro(ganho) + " moedas!"
        self.assets["coletar"].play()

    def atualizar_roleta(self, dt):  # Atualiza os 4 segundos de animacao do giro e o cooldown.
        if self.girando:
            self.tempo_giro += dt
            if self.tempo_giro >= self.proxima_troca:
                self.cursor_roleta += 1
                if self.cursor_roleta >= len(PREMIOS):
                    self.cursor_roleta = 0
                self.proxima_troca = self.tempo_giro + 70 + int(280 * (self.tempo_giro / 4000) ** 2)
            if self.tempo_giro >= 4000:
                self.girando = False
                self.cursor_roleta = self.premio
                self.roleta_cd = COOLDOWN_ROLETA * 1000
                self.dar_premio()
        elif self.roleta_cd > 0:
            self.roleta_cd -= dt
            if self.roleta_cd < 0:
                self.roleta_cd = 0

    def update(self, dt, mundo_ativo):  # Atualiza dinos, ovos, caixas e entregas quando nenhum painel esta aberto.
        self.atualizar_roleta(dt)
        if self.aviso_t > 0:
            self.aviso_t -= dt
        if mundo_ativo:
            self.tempo += dt
            for dino in self.dinos:
                dino.update(dt)
            for ovo in itens_do_jogo(self.ovos):
                ovo.update(dt)
            for caixa in self.caixas:
                caixa.update(dt)
            for dino in self.dinos:
                if dino.tempo_ovo <= 0:
                    dino.tempo_ovo = random.randint(OVO_MIN, OVO_MAX) * 1000
                    if len(self.ovos) < MAX_OVOS:
                        x = dino.rect.centerx + random.randint(-14, 14)
                        y = dino.rect.bottom + 6
                        self.ovos.add(Ovo(x, y, dino.nivel, self.assets))
            for caixa in itens_do_jogo(self.caixas):
                if caixa.estado == "parada" and caixa.espera <= 0:
                    x, y = caixa.rect.center
                    nivel = caixa.nivel
                    caixa.kill()
                    self.aparecer_dino(nivel, x, y)
            if self.tem_espaco():
                self.timer -= dt
                if self.timer <= 0:
                    self.nova_caixa(self.qual)
                    self.timer = self.intervalo() * 1000


# ==================== CONTROLE DE TELAS E MOUSE ====================
class InterfaceMouse:
    """Gerencia telas, cliques, arrasto de dinossauros e animacao do meteoro."""

    def __init__(self, assets):  # Inicializa estados de tela, variaveis de arrasto e do meteoro.
        self.assets = assets
        self.partida = Partida(assets)
        self.estado = "menu"
        self.voltar_ajuda = "menu"
        self.painel = ""
        self.scroll = 0
        self.mouse = (0, 0)
        self.arrastado = 0
        self.offset = (0, 0)
        self.efeitos = []
        self.confetes = []
        self.passo_roda = 0
        self.inicio_roda = 0
        self.total_roda = 0
        self.meteoro_x = 0
        self.meteoro_y = 0
        self.tempo_meteoro = 0
        self.menu_dinos = []
        for nivel in [1, 3, 5, 8, 12, 17]:
            x = random.randint(90, WIDTH - 90)
            y = random.randint(360, 490)
            self.menu_dinos.append(Dino(nivel, x, y, assets))

    def botao(self, tela, area, titulo, cor=(76, 155, 76), ativo=True, fonte="fonte"):  # Desenha um botao clicavel com efeito hover.
        if not ativo:
            cor = (142, 137, 115)
        elif dentro(self.mouse, area):
            nova_cor = []
            for canal in cor:
                canal += 20
                if canal > 255:
                    canal = 255
                nova_cor.append(canal)
            cor = nova_cor
        placa(tela, area, cor)
        x, y, largura, altura = area
        escrever(tela, self.assets, titulo, x + largura / 2, y + altura / 2 - 1, fonte, centro=True)

    def iniciar(self):  # Comeca uma nova partida zerando os estados anteriores.
        self.partida = Partida(self.assets)
        self.estado = "jogo"
        self.painel = ""
        self.scroll = 0
        self.arrastado = 0
        self.efeitos = []
        self.confetes = []
        self.passo_roda = 0
        self.tempo_meteoro = 0

    def area_compra(self, linha):  # Calcula a area clicavel do botao Comprar de uma linha da loja.
        return (569, 149 + linha * 57, 128, 34)

    def mudar_scroll(self, passo):  # Move a rolagem da loja entre os 20 niveis disponiveis.
        self.scroll += passo
        if self.scroll < 0:
            self.scroll = 0
        if self.scroll > NIVEL_MAXIMO - 6:
            self.scroll = NIVEL_MAXIMO - 6

    def alvo(self, dino):  # Encontra um dinossauro do mesmo nivel proximo ao que esta sendo arrastado.
        melhor = 0
        menor = 999999
        for outro in self.partida.dinos:
            if outro != dino and outro.nivel == dino.nivel and dino.nivel < NIVEL_MAXIMO:
                distancia = calcular_distancia(dino.rect.centerx, dino.rect.centery,
                                               outro.rect.centerx, outro.rect.centery)
                largura = dino.rect.right - dino.rect.left
                outra_largura = outro.rect.right - outro.rect.left
                alcance = int((largura + outra_largura) * 0.24) + 13
                if distancia < alcance and distancia < menor:
                    melhor = outro
                    menor = distancia
        return melhor

    def limitar_dino(self, dino):  # Mantem o dinossauro dentro dos limites do gramado ao soltar.
        if dino.rect.left < X_MIN:
            dino.rect.left = X_MIN
        if dino.rect.right > X_MAX:
            dino.rect.right = X_MAX
        if dino.rect.top < Y_MIN:
            dino.rect.top = Y_MIN
        if dino.rect.bottom > Y_MAX:
            dino.rect.bottom = Y_MAX
        dino.x, dino.y = dino.rect.x, dino.rect.y

    def soltar(self):  # Solta o dino arrastado e realiza a fusao se houver par valido embaixo.
        if self.arrastado != 0:
            dino = self.arrastado
            outro = self.alvo(dino)
            if outro != 0:
                x, y = outro.rect.center
                if self.partida.mesclar(dino, outro):
                    self.efeitos.append([x, y, 600])
            else:
                self.limitar_dino(dino)
            dino.preso = False
            self.arrastado = 0

    def pegar_no_campo(self, pos):  # Coleta um ovo clicado ou inicia o arrasto de um dinossauro.
        ovos = itens_do_jogo(self.partida.ovos)
        indice = len(ovos) - 1
        coletou = False
        while indice >= 0 and not coletou:
            ovo = ovos[indice]
            if calcular_distancia(pos[0], pos[1], ovo.rect.centerx, ovo.rect.centery) <= 23:
                self.partida.coletar_ovo(ovo)
                coletou = True
            indice -= 1
        if not coletou:
            dinos = ordenar_dinos(self.partida.dinos)
            indice = len(dinos) - 1
            while indice >= 0 and self.arrastado == 0:
                dino = dinos[indice]
                r = dino.rect
                area = (r.left, r.top, r.right - r.left, r.bottom - r.top)
                if dentro(pos, area):
                    self.arrastado = dino
                    dino.preso = True
                    dino.vx, dino.vy = 0, 0
                    self.offset = (pos[0] - r.centerx, pos[1] - r.centery)
                indice -= 1

    def clique_painel(self, pos):  # Processa cliques dentro dos paineis de Loja, Melhorias ou Roleta.
        p = self.partida
        if dentro(pos, BTN_FECHAR):
            self.painel = ""
        elif self.painel == "dinos":
            if dentro(pos, BTN_ANTERIOR):
                self.mudar_scroll(-6)
            elif dentro(pos, BTN_PROXIMO):
                self.mudar_scroll(6)
            else:
                for linha in range(6):
                    if dentro(pos, self.area_compra(linha)):
                        p.comprar_dino(self.scroll + linha + 1)
        elif self.painel == "melhorias":
            if dentro(pos, (541, 204, 156, 43)):
                p.comprar_melhoria("entrega")
            elif dentro(pos, (541, 347, 156, 43)):
                p.comprar_melhoria("qualidade")
        elif self.painel == "roleta" and dentro(pos, BTN_GIRAR):
            if p.girar():
                self.inicio_roda = self.passo_roda
                destino = (-p.premio * 8 - 4) % 64
                self.total_roda = (destino - self.inicio_roda) % 64 + 64 * 5

    def evento(self, evento):  # Trata cliques, soltura e rodinha do mouse conforme a tela ativa.
        if evento.type == pygame.MOUSEWHEEL:
            if self.estado == "jogo" and self.painel == "dinos":
                self.mudar_scroll(-evento.y)
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                self.soltar()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos = evento.pos
                self.mouse = pos
                if self.estado == "menu":
                    if dentro(pos, BTN_JOGAR):
                        self.iniciar()
                    elif dentro(pos, BTN_COMO):
                        self.voltar_ajuda = "menu"
                        self.estado = "ajuda"
                elif self.estado == "ajuda":
                    if dentro(pos, BTN_FECHAR) or dentro(pos, (286, 485, 228, 43)):
                        self.estado = self.voltar_ajuda
                elif self.estado == "vitoria":
                    if dentro(pos, BTN_NOVO):
                        self.iniciar()
                elif self.estado == "jogo":
                    novo_painel = ""
                    if dentro(pos, BTN_DINOS):
                        novo_painel = "dinos"
                    elif dentro(pos, BTN_MELHORIAS):
                        novo_painel = "melhorias"
                    elif dentro(pos, BTN_ROLETA):
                        novo_painel = "roleta"
                    if novo_painel != "":
                        if self.painel == novo_painel:
                            self.painel = ""
                        else:
                            self.painel = novo_painel
                    elif dentro(pos, BTN_AJUDA):
                        self.voltar_ajuda = "jogo"
                        self.estado = "ajuda"
                    elif self.painel != "":
                        self.clique_painel(pos)
                    elif pos[1] >= 90:
                        self.pegar_no_campo(pos)

    def update(self, dt):  # Atualiza a logica da tela atual, o arrasto e a queda do meteoro.
        self.mouse = pygame.mouse.get_pos()
        if self.estado == "menu":
            for dino in self.menu_dinos:
                dino.update(dt)
        elif self.estado == "jogo":
            estava_girando = self.partida.girando
            if self.arrastado != 0:
                dino = self.arrastado
                dino.rect.center = (self.mouse[0] - self.offset[0], self.mouse[1] - self.offset[1])
                dino.x, dino.y = dino.rect.x, dino.rect.y
            self.partida.update(dt, self.painel == "")
            if estava_girando:
                progresso = self.partida.tempo_giro / 4000
                if progresso > 1:
                    progresso = 1
                suavizado = 1 - (1 - progresso) ** 3
                self.passo_roda = int(self.inicio_roda + self.total_roda * suavizado) % 64
            novos = []
            for efeito in self.efeitos:
                efeito[2] -= dt
                if efeito[2] > 0:
                    novos.append(efeito)
            self.efeitos = novos
            if self.partida.venceu:
                self.estado = "meteoro"
                self.painel = ""
                self.arrastado = 0
                self.tempo_meteoro = 0
                self.meteoro_x = WIDTH + 140
                self.meteoro_y = -140
        elif self.estado == "meteoro":
            self.tempo_meteoro += dt
            self.meteoro_x -= 0.52 * dt
            self.meteoro_y += 0.36 * dt
            if self.tempo_meteoro >= 2100:
                self.estado = "vitoria"
        elif self.estado == "vitoria":
            if len(self.confetes) < 120:
                self.confetes.append([random.randint(8, WIDTH - 8), -8, random.randint(65, 170), random.randint(0, 3)])
            novos = []
            for confete in self.confetes:
                confete[1] += confete[2] * dt / 1000
                if confete[1] < HEIGHT:
                    novos.append(confete)
            self.confetes = novos

    def desenhar_dino(self, tela, dino):  # Desenha sombra, sprite do dinossauro e medalha com seu nivel.
        r = dino.rect
        oval(tela, (59, 43, 25), r.centerx, r.bottom - 2, 27, 7)
        tela.blit(dino.image, r)
        cor = (241, 215, 147)
        if dino.nivel >= 15:
            cor = (255, 207, 67)
        elif dino.nivel >= 8:
            cor = (174, 147, 238)
        pygame.draw.circle(tela, (66, 42, 23), (r.centerx, r.bottom + 9), 11)
        escrever(tela, self.assets, str(dino.nivel), r.centerx, r.bottom + 8, "pequena", cor, True)

    def desenhar(self, tela):  # Desenha a tela correspondente ao estado atual do jogo.
        tela.blit(self.assets["fundo"], (0, 0))
        if self.estado == "menu":
            self.desenhar_menu(tela)
        elif self.estado == "ajuda":
            self.desenhar_ajuda(tela)
        elif self.estado == "meteoro":
            self.desenhar_meteoro(tela)
        elif self.estado == "vitoria":
            self.desenhar_vitoria(tela)
        else:
            self.desenhar_campo(tela)
            self.desenhar_hud(tela)
            if self.painel == "dinos":
                self.desenhar_loja(tela)
            elif self.painel == "melhorias":
                self.desenhar_melhorias(tela)
            elif self.painel == "roleta":
                self.desenhar_roleta(tela)
            if self.partida.aviso_t > 0:
                y_aviso = 105
                if self.painel != "":
                    y_aviso = 563
                escrever(tela, self.assets, self.partida.aviso, WIDTH / 2, y_aviso, "fonte", (255, 242, 168), True)

    def desenhar_menu(self, tela):  # Desenha a tela inicial com dinos andando, titulo e botao JOGAR.
        for dino in self.menu_dinos:
            self.desenhar_dino(tela, dino)
        placa(tela, (82, 88, 636, 205), (95, 63, 34))
        placa(tela, (91, 96, 618, 187), (45, 70, 43))
        escrever(tela, self.assets, "DinoEvolution", 400, 145, "titulo", (255, 216, 86), True)
        escrever(tela, self.assets, "Junte dinos iguais ate criar o Rei T-Rex!", 400, 207, "fonte", (255, 250, 224), True)
        escrever(tela, self.assets, "Arraste para evoluir. Clique nos ovos para ganhar moedas.", 400, 244, "pequena", (255, 248, 215), True)
        self.botao(tela, BTN_JOGAR, "JOGAR", (77, 165, 76), fonte="grande")
        self.botao(tela, BTN_COMO, "Como jogar", (155, 107, 54))

    def desenhar_campo(self, tela):  # Desenha dinossauros, caixas, ovos e o anel de fusao no gramado.
        for dino in ordenar_dinos(self.partida.dinos):
            if dino != self.arrastado:
                self.desenhar_dino(tela, dino)
        for caixa in self.partida.caixas:
            desenhar_caixa(tela, caixa.rect.centerx, caixa.rect.centery)
        for ovo in self.partida.ovos:
            if ovo.vida >= 3000 or int(ovo.vida / 200) % 2 == 0:
                desenhar_ovo(tela, ovo.rect.centerx, ovo.rect.centery)
        for efeito in self.efeitos:
            tamanho = 20 + int((600 - efeito[2]) / 20)
            anel(tela, (255, 231, 122), efeito[0], efeito[1], tamanho, int(tamanho / 2))
        if self.arrastado != 0:
            alvo = self.alvo(self.arrastado)
            if alvo != 0:
                anel(tela, (255, 232, 88), alvo.rect.centerx, alvo.rect.bottom - 1, 43, 13)
            self.desenhar_dino(tela, self.arrastado)
        retangulo(tela, (65, 46, 27), (0, HEIGHT - 23, WIDTH, 23))
        escrever(tela, self.assets, "Arraste dinos iguais para juntar  |  Clique nos ovos  |  Use a loja e a roleta", 400, HEIGHT - 13, "pequena", centro=True)

    def desenhar_hud(self, tela):  # Desenha a barra superior com moedas, botoes e barra de proxima caixa.
        p = self.partida
        retangulo(tela, (87, 58, 30), (0, 0, WIDTH, 58))
        retangulo(tela, (132, 91, 47), (0, 0, WIDTH, 4))
        desenhar_moeda(tela, 22, 25, 0.8)
        escrever(tela, self.assets, dinheiro(p.moedas), 43, 10, "grande")
        escrever(tela, self.assets, dinheiro(p.renda()) + "/s em ovos", 45, 38, "pequena", (255, 221, 122))
        escrever(tela, self.assets, "Dinos " + str(p.ocupados()) + "/20", 272, 9, "fonte")
        escrever(tela, self.assets, "Melhor: Nv " + str(p.maior), 273, 35, "pequena", (198, 242, 154))
        self.botao(tela, BTN_AJUDA, "?", (145, 100, 55), fonte="pequena")
        self.botao(tela, BTN_DINOS, "Dinos", (76, 151, 76))
        self.botao(tela, BTN_MELHORIAS, "Melhorias", (92, 126, 183), fonte="pequena")
        titulo = "ROLETA!"
        if p.girando:
            titulo = "Girando..."
        elif p.roleta_cd > 0:
            titulo = "Roleta " + str(int((p.roleta_cd + 999) / 1000)) + "s"
        self.botao(tela, BTN_ROLETA, titulo, (198, 126, 41), fonte="pequena")
        retangulo(tela, (59, 42, 23), (0, 58, WIDTH, 8))
        progresso = 1 - p.timer / (p.intervalo() * 1000)
        if progresso < 0:
            progresso = 0
        if progresso > 1:
            progresso = 1
        retangulo(tela, (139, 205, 74), (0, 58, int(WIDTH * progresso), 8))
        texto = "Proxima caixa (Nv " + str(p.qual) + ") em " + str(int((p.timer + 999) / 1000)) + "s"
        if not p.tem_espaco():
            texto = "Campo cheio! Junte dinos para abrir espaco."
        if self.painel == "":
            escrever(tela, self.assets, texto, 12, 73, "pequena")

    def painel_base(self, tela, titulo, detalhe):  # Desenha a moldura padrao dos paineis internos.
        placa(tela, (70, 72, 660, 480), (242, 224, 172))
        retangulo(tela, (147, 99, 48), (83, 84, 634, 40))
        escrever(tela, self.assets, titulo, 400, 104, "grande", (255, 239, 184), True)
        self.botao(tela, BTN_FECHAR, "X", (191, 73, 49), fonte="pequena")
        escrever(tela, self.assets, detalhe, 400, 135, "pequena", (93, 63, 32), True)

    def desenhar_loja(self, tela):  # Desenha a janela de compra de dinossauros paginada.
        p = self.partida
        self.painel_base(tela, "LOJA DE DINOS", "Use a rodinha do mouse ou as setas abaixo para ver os niveis.")
        for linha in range(6):
            nivel = self.scroll + linha + 1
            y = 145 + linha * 57
            retangulo(tela, (255, 244, 205), (88, y, 624, 51))
            imagem = self.assets["dinos"][nivel]["mini"]
            r = imagem.get_rect()
            r.center = (127, y + 25)
            tela.blit(imagem, r)
            escrever(tela, self.assets, "Nv " + str(nivel) + "  " + self.assets["dinos"][nivel]["nome"], 171, y + 5, "pequena", (77, 48, 24))
            escrever(tela, self.assets, "Ovo: " + dinheiro(valor_ovo(nivel)) + "  |  Comprados: " + str(p.compradas[nivel - 1]), 171, y + 27, "pequena", (117, 86, 44))
            preco = preco_dino(nivel, p.compradas)
            mensagem = dinheiro(preco)
            ativo = nivel <= p.limite_compra() and p.moedas >= preco
            if nivel == NIVEL_MAXIMO:
                mensagem = "So por fusao"
                ativo = False
            elif nivel > p.limite_compra():
                mensagem = "Alcance " + str(nivel + 1)
            self.botao(tela, self.area_compra(linha), mensagem, ativo=ativo, fonte="pequena")
        self.botao(tela, BTN_ANTERIOR, "< Voltar", (158, 111, 59), self.scroll > 0, "pequena")
        self.botao(tela, BTN_PROXIMO, "Proximo >", (158, 111, 59), self.scroll < 14, "pequena")
        escrever(tela, self.assets, "Niveis " + str(self.scroll + 1) + " a " + str(self.scroll + 6) + " de 20", 400, 520, "pequena", (99, 68, 33), True)

    def desenhar_melhorias(self, tela):  # Desenha o painel de upgrades permanentes.
        p = self.partida
        self.painel_base(tela, "MELHORIAS", "Entregas mais rapidas e dinossauros melhores nas caixas.")
        titulos = ["Entrega rapida", "Qualidade das caixas"]
        textos = ["Uma caixa a cada " + str(p.intervalo()) + " segundos", "Caixas trazem dino nivel " + str(p.qual)]
        custos = [p.custo_entrega(), p.custo_qual()]
        niveis = [p.ent_lvl, p.qual - 1]
        maximos = [ENT_MAX, QUAL_MAX - 1]
        for i in range(2):
            y = 173 + i * 143
            placa(tela, (89, y, 622, 120), (255, 244, 206))
            escrever(tela, self.assets, titulos[i], 110, y + 13, "grande", (87, 52, 24))
            escrever(tela, self.assets, textos[i], 112, y + 53, "pequena", (121, 86, 43))
            retangulo(tela, (140, 111, 65), (112, y + 89, 367, 12))
            retangulo(tela, (111, 179, 77), (112, y + 89, int(367 * niveis[i] / maximos[i]), 12))
            titulo = dinheiro(custos[i])
            if niveis[i] == maximos[i]:
                titulo = "MAXIMO"
            self.botao(tela, (541, y + 31, 156, 43), titulo, ativo=niveis[i] < maximos[i] and p.moedas >= custos[i])
        escrever(tela, self.assets, "Cada melhoria vale para toda a partida.", 400, 493, "fonte", (110, 75, 33), True)

    def desenhar_roleta(self, tela):  # Desenha a roleta giratoria com as 8 fatias e o botao GIRAR.
        p = self.partida
        self.painel_base(tela, "ROLETA DA EVOLUCAO", "Gire para ganhar moedas ou uma caixa especial.")
        cx, cy, raio = 400, 299, 124
        pygame.draw.circle(tela, (105, 64, 26), (cx + 3, cy + 6), raio + 10)
        pygame.draw.circle(tela, (239, 182, 67), (cx, cy), raio + 8)
        cores = [(207, 92, 65), (223, 175, 68), (101, 161, 87), (87, 135, 182),
                 (203, 129, 68), (134, 112, 180), (95, 164, 152), (204, 104, 135)]
        for i in range(8):
            pontos = [(cx, cy)]
            for j in range(9):
                px, py = CIRCULO[(i * 8 + j + self.passo_roda) % 64]
                pontos.append((int(cx + raio * px / 1000), int(cy + raio * py / 1000)))
            pygame.draw.polygon(tela, cores[i], pontos)
            px, py = CIRCULO[(i * 8 + 4 + self.passo_roda) % 64]
            escrever(tela, self.assets, ROTULOS[i], cx + 82 * px / 1000, cy + 82 * py / 1000, "pequena", centro=True)
        pygame.draw.circle(tela, (126, 79, 32), (cx, cy), 19)
        desenhar_moeda(tela, cx, cy, 0.9)
        pygame.draw.polygon(tela, (93, 49, 24), [(383, 161), (417, 161), (400, 192)])
        pygame.draw.polygon(tela, (255, 215, 86), [(388, 164), (412, 164), (400, 185)])
        mensagem = p.resultado
        if mensagem == "":
            mensagem = "+Ns = segundos da renda | Caixa = dino gratis"
        escrever(tela, self.assets, mensagem, 400, 453, "fonte", (89, 59, 27), True)
        titulo = "GIRAR!"
        if p.girando:
            titulo = "Girando..."
        elif p.roleta_cd > 0:
            titulo = "Volta em " + str(int((p.roleta_cd + 999) / 1000)) + "s"
        self.botao(tela, BTN_GIRAR, titulo, (213, 129, 46), not p.girando and p.roleta_cd == 0)

    def desenhar_ajuda(self, tela):  # Desenha a tela de instrucoes de como jogar com o mouse.
        self.painel_base(tela, "COMO JOGAR", "Tudo funciona com o mouse, como na referencia original.")
        linhas = ["Segure um dinossauro e arraste para outro do mesmo nivel.",
                  "Solte em cima dele: os dois viram um dino mais evoluido.",
                  "Clique nos ovos para ganhar moedas antes que desaparecam.",
                  "Use Dinos para comprar. Use Melhorias para evoluir as entregas.",
                  "Gire a roleta a cada 2 minutos para receber um premio.",
                  "A loja e os paineis pausam o campo. Feche no X para continuar.",
                  "Objetivo: juntar dois dinos nivel 19 e criar o Rei T-Rex!"]
        for i in range(len(linhas)):
            escrever(tela, self.assets, linhas[i], 105, 178 + i * 32, "pequena", (94, 61, 29))
        desenhar_ovo(tela, 255, 438, 1.3)
        desenhar_caixa(tela, 545, 434, 0.9)
        self.botao(tela, (286, 485, 228, 43), "ENTENDI!", (76, 158, 78))

    def desenhar_meteoro(self, tela):  # Desenha o meteoro cruzando a tela e o clarao antes da vitoria.
        self.desenhar_campo(tela)
        img = self.assets["meteoro"]
        r = img.get_rect()
        r.center = (int(self.meteoro_x), int(self.meteoro_y))
        tela.blit(img, r)
        if self.tempo_meteoro >= 1750:
            retangulo(tela, (255, 248, 215), (0, 0, WIDTH, HEIGHT))

    def desenhar_vitoria(self, tela):  # Desenha a tela final com o Rei T-Rex, tempo, confetes e reinicio.
        placa(tela, (100, 74, 600, 474), (240, 219, 157))
        escrever(tela, self.assets, "VITORIA!", 400, 124, "titulo", (117, 68, 23), True)
        escrever(tela, self.assets, "Voce criou o Rei T-Rex!", 400, 184, "grande", (91, 111, 49), True)
        imagem = self.assets["dinos"][20]["vitoria"]
        r = imagem.get_rect()
        r.center = (400, 337)
        tela.blit(imagem, r)
        segundos = int(self.partida.tempo / 1000)
        escrever(tela, self.assets, "Tempo: " + str(int(segundos / 60)) + " min " + str(segundos % 60) + " s", 400, 455, "fonte", (106, 73, 34), True)
        self.botao(tela, BTN_NOVO, "Jogar de novo", (80, 157, 76), fonte="grande")
        cores = [(255, 208, 70), (113, 202, 99), (246, 125, 91), (124, 184, 237)]
        for confete in self.confetes:
            retangulo(tela, cores[confete[3]], (int(confete[0]), int(confete[1]), 5, 8))


# ==================== LOOP PRINCIPAL ====================
def main():  # Inicializa o Pygame, cria a janela e roda o loop principal do jogo.
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DinoEvolution!")
    relogio = pygame.time.Clock()
    assets = carregar_assets()
    interface = InterfaceMouse(assets)
    pygame.mixer.music.play(loops=-1)
    rodando = True
    while rodando:
        dt = relogio.tick(FPS)
        if dt > 100:
            dt = 100
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            else:
                interface.evento(evento)
        if rodando:
            interface.update(dt)
            interface.desenhar(window)
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
>>>>>>> 84a6067887d5f636722f58a839fa9fa6dfe9bd9b
