import pyautogui as auto, os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from time import sleep



class Loader():
    def __init__(self):
        return
    
    def load_urls(self, file_path):
        f = open(file_path, 'r')
        lines =  []
        for line in f:
            line = line.strip()
            lines.append(line)
        print(lines)
        f.close()


        auto.press("winright")
        sleep(0.2)
        auto.write("cmd")
        sleep(0.2)
        auto.press('return')
        sleep(0.4)
        auto.write('firefox')
        sleep(0.2)
        auto.press('return')
        sleep(2)

        i = 1
        while i < int(lines[0]):
            print(lines[i])
            sleep(0.3)
            auto.click(x=950, y=100)
            sleep(0.2)
            auto.write(lines[i])
            sleep(2)
            auto.press('return')
            i+=1
    
    def glue_vids(self, v):
        vids = []
        for vid in v:
            clip = VideoFileClip(vid)
            vids.append(clip)
        f_clip = concatenate_videoclips(vids)
        # return f_clip
        f_clip.write_videofile('/home/a455c/proj/yt-creator/output')

    def write_clips(self, clip, path):
        clip.write_videofile(path)

    def remove_content(self, path):
        if os.path.exists(path):
            for f in os.path(path):
                os.remove(f.path)

