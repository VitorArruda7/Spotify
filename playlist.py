import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

musicas_json = {}

scope = os.getenv("scope")
username = os.getenv("username")
token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

#cria a playlist
playlist_name = input("Qual será o nome da Playlist?")
playlist_description = input("Qual será a descrição da Playlist?")
spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

#acha a playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist["items"][0]["id"]

lista_de_musicas = []
contador = 0
while contador < 100:
    primeira_musica = (musicas_json["data"][contador])              #pega os dados das musicas
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"]) #adiciona as musicas encontradas na lista para adicionar a playlist em seguida
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas)

while contador < 200:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[100:])

while contador < 300:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[200:])

while contador < 400:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[300:])

while contador < 500:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[400:])

while contador < 600:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[500:])

while contador < 648:
    primeira_musica = (musicas_json["data"][contador])
    nome_da_musica=(primeira_musica["title"])
    artista=(primeira_musica["artist"])
    dados_para_busca = ("{} {}".format(nome_da_musica, artista))
    contador += 1
    resultado = spotifyObject.search(q=dados_para_busca)
    lista_de_musicas.append(resultado["tracks"]["items"][0]["uri"])
    print(len(lista_de_musicas))
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=lista_de_musicas[600:])