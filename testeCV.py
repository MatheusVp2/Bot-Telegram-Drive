#-*- coding: utf-8 -*-
import numpy as np
import cv2
import telebot

def foto(nome, valor):
    # Cria uma imagem nova (tamanho 400x200 e 3 canais RGB)
    largura = 400
    altura = 200
    imagem = np.zeros((altura, largura, 3), dtype=np.uint8)

    # Preenche o fundo de amarelo
    cv2.rectangle(imagem, (0, 0), (largura, altura), (0, 255, 255), -1)

    # Desenha uma borda azul
    cv2.rectangle(imagem, (0, 0), (largura-5, altura-5), (255, 0, 0), 5)

    # Desenha o texto com a variavel em preto, no centro
    texto = '{} = {}'.format(nome, valor)

    fonte = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    escala = 2
    grossura = 3

    # Pega o tamanho (altura e largura) do texto em pixels
    tamanho, _ = cv2.getTextSize(texto, fonte, escala, grossura)

    # Desenha o texto no centro
    cv2.putText(imagem, texto, (int(largura / 2 - tamanho[0] / 2), int(altura / 2 + tamanho[1] / 2)), fonte, escala, (0, 0, 0), grossura)

    cv2.imwrite('imagem.jpg', imagem)

    # Exibe a imagem
    #cv2.imshow("Imagem", imagem)
    #cv2.waitKey(0)

bot = telebot.TeleBot( "713139444:AAFbFc2lDX5ZTI8ocCBM-1Blfc1Dfpfyxs0" )

foto('Matheus', 20)

photo = open('imagem.jpg', 'rb')
bot.send_photo(484393281, photo)


print('Bot Funcionando!')
bot.polling()