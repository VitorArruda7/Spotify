<div align="center">
<h1 align="center">

<br> Projeto Spotify
</h1>
<h3>◦ Ferramantas utilizadas.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Dotenv-purple" alt="Dotenv"/>
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=blue" alt="JSON" />
<img src="https://img.shields.io/badge/Spotipy-white" alt="Spotipy" />

</p>

---

## 📍 Projeto

A ideia do projeto é pegar uma playlist da Apple Music com 647 musicas em formato json, filtrar os dados necessários do json, usar a API do Spotify para criar uma playlist para o usuário da forma que desejar e depois adicionar todas as musicas da Apple Music para a playlist criada no Spotify.
---

## ⚙️ Caracteristicas

O código é capaz de coletar as informações necessárias de cada música presente na playlist, entrar na API do Spotify, criar uma playlist de acordo com o que o usuário quiser, buscar musicas para o usuário e adicionar músicas em uma playlist. O número de músicas pode ser facilmente alterado mudando alguns detalhes no código, onde a cada 100 musicas tem que se fazer um novo laço. O arquivo musicas.json é um exemplo curto de json que poderia ser utilizado para fazer esse processo, e o arquivo .env são dados sensíveis necessários do usuário, como seu username que pode ser encontrado na sua conta do Spotify e outros dados necessários pra API do Spotify.

---

### 📦 Instalação

1. Mude para o diretório do projeto

2. Instale os requisitos:
```
pip install python-dotenv
pip install spotipy
```
