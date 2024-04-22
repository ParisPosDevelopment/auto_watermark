import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

video_path = os.path.abspath("video")
image_path = os.path.relpath("watermark")

def apply_watermark(video_names, image_names):
	for video in video_names:
		for image in image_names:
			video_file = os.path.join(video_path, video)
			image_file = os.path.join(image_path, image)

			video_name = os.path.splitext(video)[0]
			image_name = os.path.splitext(image)[0]

			if video_name == image_name:
				video_clip = VideoFileClip(video_file)
				image_clip = ImageClip(image_file)

				image_clip = image_clip.set_duration(video_clip.duration)

				video_with_watermark = CompositeVideoClip([video_clip, image_clip.set_position(('right','top'))])

				video_with_watermark.write_videofile(f"{video_name}_render.mp4", codec='libx264')

video_names = os.listdir(video_path)
image_names = os.listdir(image_path)

apply_watermark(video_names, image_names)
