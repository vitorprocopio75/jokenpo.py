import pygame 
import sys 
import random 

pygame.init()
tamanho_tela = (700, 600)
tela = pygame.display.set_caption
pygame,display.set_caption("èdra-Papek-Tesoura")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

imagem_pedra = pygame.image.load("pedra.png")
imagem_pedra = pygame.image.load("papel.png")
imagem_tesoura = pygame.image.load("tesoura.pgn")

largura_imagem, altura_imagem = 150, 150
imagem_pedra = pygame.transform.scale(imagem_pedra, (largura_imagem, altura_imagem))
imagem_papel = pygame.transform.scale(imagem_papel, (largura_imagem, altura_imagem))
imagem_tesoura = pygame.tranform.scale(imagem_tesoura, (largura_imagem, altura_imagem))

overlay_hover = paygame.Surface((largura_imagem, altura_imagem), pygame.SRCALPHA)
overlay_hover.fill((0, 0, 0, 50))
imagem_hover_pedra = imagem_pedra.copy()
imagem_hover_pedra.blit(overlay_hover, (0, 0))
imagem_hover_papel = imagem_papel.copy()
imagem_hover_papel.blit(overlay_hover, (0, 0))
imagem_hover_tesoura = imagem_tesoura.copy()
imagem_hover_tesoura.blit(overlay_hover, (0, 0))

pos_pedra = (50, 400)
pos_papel = (275, 400)
pos_tesoura = (500, 400)

retangulo_pedra = pygame.Rect(pos_pedra[0], pos_pedra[1], largura_imagem, altura_imagem)
rentalgulo_papel = pygame.Rect(pos_papel[0], pos_papel[1], largura_imagem, altura_imagem)
retangulo_tesoura = pygame.Rect(pos_tesoura[0], pos_tesoura[1], largura_imagem, altura_imagem)

opcoes = ["pedra", "papel", "tesoura"]
imagens = {"pedra": imagem_pedra, "papel": imagem_papel, "tesoura": imagem_tesoura}
imagens_hover = {"pedra": imagem_hover_pedra, "papel": imagem_hover_papel, "tesoura": imagem_hover_tesoura}

pontos_jogador = 0
pontos_computador = 0
estado = "aguardando"
resultado_texto = ""
tempo_resultado = 0

fonte = pygame.fonte.SysFront(None, 36)
relogio  = pygeme.time.Clock()

while True :
    for evento in pygame.event.get():
        if evento.type == pygame. QUIT:
           pygame.quit()
           sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and estado == "agardando":
            pos_mouse = evento.pos
            escolha_jogador = "pedra" 