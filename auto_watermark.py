import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

video_path = "/home/bianca/workspace/paris/video"
image_path = "/home/bianca/workspace/paris/watermark"

def apply_watermark(video_names, image_names):
    for video in video_names:
        for image in image_names:
            # Construct full paths to video and image
            video_file = os.path.join(video_path, video)
            image_file = os.path.join(image_path, image)

            # Remove extension to match video and image names
            video_name = os.path.splitext(video)[0]
            image_name = os.path.splitext(image)[0]

            if video_name == image_name:
                # Load video and image
                video_clip = VideoFileClip(video_file)
                image_clip = ImageClip(image_file)

                # Set duration of image clip to match video clip
                image_clip = image_clip.set_duration(video_clip.duration)

                # Composite video with image watermark
                video_with_watermark = CompositeVideoClip([video_clip, image_clip.set_position(('right','top'))])

                # Write the composite video with watermark
                video_with_watermark.write_videofile(f"{video_name}_render.mp4", codec='libx264')

# Get list of video and image files
video_names = os.listdir(video_path)
image_names = os.listdir(image_path)

# Call the function with lists of video and image names
apply_watermark(video_names, image_names)
