import threading

from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip

mp_clips = []

def createTextClip(text):
    return TextClip(text, color="white", fontsize=24).set_duration(5.0)

def edit_project(project, ext="mp4"):
    for clip_name in project["imported_clips"]:
        desc = project["imported_clips"][clip_name]

        mp_clips.append(createTextClip(desc))
        mp_clips.append(VideoFileClip(clip_name))
    
    final_clip = concatenate_videoclips(mp_clips)

    print("Clips list: \n" + str(mp_clips))

    proj_name = project["file_name"].split(".")[0]
    output_name = proj_name + "." + ext

    final_clip.write_videofile(output_name)
    