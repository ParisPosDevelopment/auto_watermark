import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Definindo os caminhos para os diretórios de vídeo e imagem
video_path = os.path.abspath("video")
image_path = os.path.abspath("watermark")

# Extensões suportadas para vídeo e imagem
video_extensions = ['.avi', '.mkv']
image_extensions = ['.jpg', '.png']

def extension_validation(video, image):
    """Verifica se as extensões dos arquivos de vídeo e imagem são suportadas."""
    video_extension = os.path.splitext(video)[1].lower()
    image_extension = os.path.splitext(image)[1].lower()
    if video_extension in video_extensions and image_extension in image_extensions:
        return True
    else:
        print(f"O formato do vídeo {video} ou da imagem {image} não é suportado.")
        return False

            
def apply_watermark(video_names, image_names):
    """Aplica uma marca d'água em vídeos com imagens correspondentes."""
    for video in video_names:
        for image in image_names:
            if extension_validation(video, image):
                video_file = os.path.join(video_path, video)
                image_file = os.path.join(image_path, image)
                video_name = os.path.splitext(video)[0]
                image_name = os.path.splitext(image)[0]

                if video_name == image_name:
                    video_clip = VideoFileClip(video_file)
                    image_clip = ImageClip(image_file)
                    image_clip = image_clip.set_duration(video_clip.duration)
                    video_with_watermark = CompositeVideoClip([video_clip, image_clip.set_position(('right','top'))])
                    render_path = os.path.abspath("render")
                    render_path = os.path.join(render_path, f"{video_name}_rendered.mp4")
                    video_with_watermark.write_videofile(render_path, codec='libx264')

# Listando os arquivos nos diretórios de vídeo e imagem
video_names = os.listdir(video_path)
image_names = os.listdir(image_path)

# Aplicando a marca d'água nos vídeos
apply_watermark(video_names, image_names)
