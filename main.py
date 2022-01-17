import os
import json


print("Intervalo entre as imagens (EM SEGUNDOS)")
tempo = {'tempo': input("> ")}
with open('config.json', 'w') as f:
    json.dump(tempo, f, indent=4)


print("""


*Script para para mudar wallpaper com artes de anime/hentai*



// 3 OPÇÕES DE DATABASE

1 - Neko (geralmente SFW, porém as vezes algo NSFW aparece) *ALTA QUALIDADE*
2 - Neko.Fun (99% NSFW, é o que eu recomendo) *QUALIDADE MEDIANA* 
3 - Akaneko (95% NSFW) *QUALIDADE GERALMENTE MERDA, AS VEZES TEM ALGO BOM*""")

escolha = int(input(": "))

print("Iniciado!")

if escolha == 1:
    stream = os.popen(r'python .\db\life.py')
    output = stream.read()
if escolha == 2:
    stream = os.popen(r'python .\db\fun.py')
    output = stream.read()
if escolha == 3:
    stream = os.popen(r'python .\db\aaneko.py')
    output = stream.read()


