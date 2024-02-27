import sys
import os
import ffmpeg

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("informe o caminho do diretório com os arquivos compactados: $ python3 run.py <caminho_do_diretorio> ")
        sys.exit()

    path = sys.argv[1]
        
    if path == "help" or path == "h" or path == "-h" or path == "--h" or path == "-help" or path == "--help:":
        print("informe o caminho do diretório com os arquivos compactados: $ python3 run.py <caminho_do_diretorio> ")
        sys.exit()

    if os.path.exists(path) == False:
        print("caminho do vídeo inválido ou inexistente. Se você estiver utilizando o Windows, utilize o caminho com barras (/) ou 2 invertidas (\\)")
        sys.exit()  

    # Caminho para o arquivo de saída (vídeo com marca d'água)
    output_file = './video_com_marca.mp4'

    # Texto da marca d'água
    texto_marca = 'D-27/02/2024'

    # Configuração da marca d'água (posição, tamanho, cor, fonte)
    marca_dagua = f"drawtext=text='{texto_marca}':x=10:y=10:fontsize=24:fontcolor=black"

    # Executa o comando FFmpeg para adicionar a marca d'água
    ffmpeg.input(path).output(output_file, vf=marca_dagua).run()

    print(f"Marca d'água adicionada ao vídeo: {output_file}")
