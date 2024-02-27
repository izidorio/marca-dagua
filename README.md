[baixar ffmgpeg.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

descompactar o arquivo ffmpeg.7z na raiz do diretório C: ou D: e adicionar a pasta bin `D:\ffmpeg\bin` do ffmpeg no path das variável de ambiente do windows
```bash
pressione simultaneamente ”Windows + R” e digite ”sysdm.cpl”.

```

exemplo de uso do ffmpeg para adicionar marca d'água em um video
```bash
ffmpeg -i video.mp4 -vf "drawtext=text='Exemplo':fontsize=24:fontcolor=black:x=10:y=100:font=Arial" -codec:a copy output_video.mp4

```

com Python

instalar o ffmpeg-python

```bash
pip install ffmpeg-python
```

executar o arquivo marca-dagua.py

```bash
python marca-dagua.py D:/www/marca-dagua/video.mp4
```

```python

