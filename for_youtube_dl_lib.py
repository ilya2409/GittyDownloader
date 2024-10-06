import yt_dlp
import os

dir_path = './download_videos'
current_file_path = os.path.abspath(__file__)

def download_youtube_video(url, output_path=dir_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Выбирает лучшее видео и лучший аудио формат
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'retries': 40,  # Количество попыток повторного соединения
        'fragment_retries': 40,  # Количество попыток повторного соединения для фрагментов
        'retry_sleep_functions': {
            'sleep': lambda x: 2 ** x,  # Экспоненциальное увеличение времени ожидания
        },
        'ignoreerrors': True,  # Пропускать недоступные видео
        # 'playlist_items': '16-56',  # Загружать видео с 2 по 10
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Пример использования
# video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# Замените на URL вашего видео 

command = "exit"

if __name__ == "__main__":
    # os.system("color 2")
    
    print(
        "\n",
        f"# Вставьте ссылку на youtube видео",
        "\n",
        f"# Для завершения работы программы напишите - {command}",
        "\n",
    )
    
    while True:
        video_url = input("Your video url: ")
            
        if video_url == command:
            break
        else:
            download_youtube_video(video_url)
        
        print('\n', end="")
