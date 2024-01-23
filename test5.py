from moviepy.editor import VideoFileClip, concatenate_videoclips


clip1 = VideoFileClip("/home/a455c/Downloads/sBScUQKjAI8xszq2.ts")
clip2 = VideoFileClip("/home/a455c/Downloads/dWT6e4sRPOsNnRAj.ts")
finalClip = concatenate_videoclips([clip1, clip2])
finalClip.write_videofile("final_clip.mp4")

