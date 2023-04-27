import sys
import subprocess

def baixar_video(url):
    try:
        output = subprocess.check_output(['yt-dlp', '--no-check-certificate', '-f', 'mp4', url], stderr=subprocess.STDOUT)
        return f"Vídeo baixado com sucesso: {output}"
    except subprocess.CalledProcessError as e:
        return f"Erro ao baixar vídeo: {e.output}"
    except Exception as e:
        return f"Erro ao baixar vídeo: {e}"

if __name__ == "__main__":
    url = sys.argv[1]
    print(baixar_video(url))
