import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# Extensões suportadas para vídeo e imagem
video_extensions = ['.mp4','.avi', '.mkv', '.mov', '.proxy']
image_extensions = ['.jpg', '.jpeg', '.png']

def create_directories(video_path, image_path, render_path):
	try:
		for path in [video_path, image_path, render_path]:
			if not os.path.exists(path):
				os.makedirs(path)
		return True
	except OSError as e:
		print(f"Erro ao criar os diretórios: {str(e)}")

def extension_validation(video, image):
	try:
		# Verifica se as extensões dos arquivos de vídeo e imagem são suportadas.
		video_extension = os.path.splitext(video)[1].lower()
		image_extension = os.path.splitext(image)[1].lower()
		if video_extension not in video_extensions:
			print(f"O formato do vídeo {video} não é suportado.")
			return False
		
		if image_extension not in image_extensions:
			print(f"O formato da imagem {image} não é suportado.")
			return False
		return True
	except OSError as e:
		print(f"Erro ao validar as extensões: {str(e)}")

def apply_watermark(video_path, image_path, render_path):
		# Listando os arquivos nos diretórios de vídeo e imagem
		video_names = os.listdir(video_path)
		image_names = os.listdir(image_path)

		# Aplica uma marca d'água em vídeos com imagens correspondentes.
		for video in video_names:
			for image in image_names:
				if extension_validation(video, image):
					video_file = os.path.join(video_path, video)
					image_file = os.path.join(image_path, image)
					video_name = os.path.splitext(video)[0]
					image_name = os.path.splitext(image)[0]
					try:
						if video_name == image_name:
							video_clip = VideoFileClip(video_file)
							image_clip = ImageClip(image_file)
							image_clip = image_clip.set_duration(video_clip.duration)
							video_with_watermark = CompositeVideoClip([video_clip, image_clip.set_position(('right','top'))])
							render_path = os.path.join(render_path, f"{video_name}_rendered.mp4")
							video_with_watermark.write_videofile(render_path, codec='libx264', fps=30, threads=12)
					except Exception as e:
						print(f"Erro ao processar video {video_name}: {str(e)}")					

def main():
	# Definindo os caminhos para os diretórios de vídeo e imagem
	video_path = os.path.abspath("video")
	image_path = os.path.abspath("watermark")
	render_path = os.path.abspath("render")

	create_directories(video_path, image_path, render_path)
	apply_watermark(video_path, image_path, render_path)

if __name__ == "__main__":
    main()