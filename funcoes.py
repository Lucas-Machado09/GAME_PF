
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