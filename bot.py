#-*- coding: utf-8 -*-
import telebot
import authPyDrive as att
from pydrive.drive import GoogleDrive
import os
import time
import tempfile

gauth=att.auth()

bot = telebot.TeleBot( "")

@bot.message_handler(commands=['start', 'help'])
def send_start(msg):
	bot.send_message(msg.chat.id , "Bem Vindo !")


@bot.message_handler(content_types=['photo'])
def photo(message):
	print('Recebendo Foto')
	fileID = message.photo[-1].file_id
	file_info = bot.get_file(fileID)
	downloaded_file = bot.download_file(file_info.file_path)

	f = tempfile.NamedTemporaryFile(mode='wb', delete=False)
	f.write(downloaded_file)
	file_name = f.name
	drive = GoogleDrive(gauth)
	file1 = drive.CreateFile({'title': '{}'.format(file_info.file_path)})
	file1.SetContentFile(f.name)
	file1.Upload()
	f.close()



@bot.message_handler(content_types=['video'])
def photo(message):
	print('Recebendo Video')
	file_info = bot.get_file(message.video.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	f = tempfile.NamedTemporaryFile(mode='wb', delete=False)
	f.write(downloaded_file)
	file_name = f.name
	drive = GoogleDrive(gauth)
	file1 = drive.CreateFile({'title': '{}'.format(file_info.file_path)})
	file1.SetContentFile(f.name)
	file1.Upload()
	f.close()


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
	print('Recebendo Documento')
	file_info = bot.get_file(message.document.file_id)
	print(message.document)
	downloaded_file = bot.download_file(file_info.file_path)
	src=message.document.file_name

	f = tempfile.NamedTemporaryFile(mode='wb', delete=False)
	f.write(downloaded_file)
	file_name = f.name
	drive = GoogleDrive(gauth)
	file1 = drive.CreateFile({'title': '{}'.format(src)})
	file1.SetContentFile(f.name)
	file1.Upload()
	f.close()

print("Bot Funcionando !")
bot.polling()