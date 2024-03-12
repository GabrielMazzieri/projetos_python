from pytube import YouTube
import time
import os

def download_audio_batch(video_urls, output_path=".", interval=5):
    for url in video_urls:
        try:
            yt = YouTube(url)

            audio_stream = yt.streams.filter(only_audio=True).first()

            video_title = yt.title

            video_title = "".join(c if c.isalnum() or c in [' ', '.', '-'] else '_' for c in video_title)

            file_name = os.path.join(output_path, f"{video_title}.mp3")

            audio_stream.download(output_path)

            os.rename(os.path.join(output_path, audio_stream.default_filename), file_name)

            print(f"Download de áudio concluído para {video_title}")

            time.sleep(interval)
        except Exception as e:
            print(f"Ocorreu um erro ao processar {url}: {str(e)}")

lista_de_urls = [
    "https://www.youtube.com/watch?v=8nTCRatHvmo&ab_channel=JosetteFeres-Topic",
    "https://www.youtube.com/watch?v=fG7SWXXPlOo&ab_channel=ShauanBencks-Topic",
    "https://www.youtube.com/watch?v=zFiwYiQuxZE&ab_channel=IlhadaLua%26MariaCeciliaMalta-Topic",
    "https://www.youtube.com/watch?v=RjgABP-gMI8&ab_channel=PalavraCantadaOficial",
    "https://www.youtube.com/watch?v=n9m9TFZ9h2Q&ab_channel=JosetteFeres-Topic",
    "https://www.youtube.com/watch?v=jg90sNShR3Q&ab_channel=H%C3%A9lioZiskind-Topic",
    "https://www.youtube.com/watch?v=mnDc1MiEnTk&ab_channel=JPKids",
    "https://www.youtube.com/watch?v=oB5VnK5zqvU&ab_channel=MargarethDarezzo-Topic",
    "https://www.youtube.com/watch?v=8A60RyGY7OQ&ab_channel=KamaluESuaTurma",
    "https://www.youtube.com/watch?v=jqy_y7n5KRE&ab_channel=Somente1",
    "https://www.youtube.com/watch?v=15ySW8HrqKk&ab_channel=ElianeBen%C3%ADcio",
    "https://www.youtube.com/watch?v=j-Z9IJAgvxs&ab_channel=GabrielSaterOficial",
    "https://www.youtube.com/watch?v=v1Pv9cOy-2s&ab_channel=PalavraCantadaOficial",
    "https://www.youtube.com/watch?v=RHbnazDkHbc&ab_channel=ybmusic",
    "https://www.youtube.com/watch?v=CaTXgmHyMSk&ab_channel=PalavraCantadaOficial",
    "https://youtu.be/jHvtbqz7oIE?si=wHQvTljnl22kpk_s&t=17",
    "https://youtu.be/XGvNQpT6_bM?si=JEdtqAcDJ2jUZ5F8&t=17",
    "https://www.youtube.com/watch?v=HpM7dCySOro&ab_channel=FabianaGodoy-NinhoMusical",
    "https://www.youtube.com/watch?v=_Lx9c-eMwVw&ab_channel=OTubaraoMarteloVEVO",
    "https://www.youtube.com/watch?v=gsy3jRvuDXs&ab_channel=Bamboozinho%3Alivrosparaainf%C3%A2ncia",
    "https://youtu.be/c2xT4gxNqbM?si=0cxWCxK7wbSUGG8m&t=6",
    "https://youtu.be/hyW1EmTIUY8?si=_TH1Bzy-lo7SWZeO&t=9",
    "https://www.youtube.com/watch?v=TUSRt8OXJq0&ab_channel=PatatiPatat%C3%A1",
    "https://www.youtube.com/watch?v=DQ9iK7Nu8Nw&ab_channel=balaomagicoVEVO"
]

output_directory = "D:\musicas"
intervalo_entre_downloads = 10 

download_audio_batch(lista_de_urls, output_directory, intervalo_entre_downloads)