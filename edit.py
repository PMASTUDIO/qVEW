import threading

from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip

mp_clips = []

def edit_project(project, ext="mp4"):
    for clip_name in project["imported_clips"]:
        desc = project["imported_clips"][clip_name]

        mp_clips.append(TextClip(desc, color="white", fontsize=32).set_duration(5.0))
        resized_clip = VideoFileClip(clip_name).resize(width=1920)
        with_transition = resized_clip.crossfadein(2.0)
        mp_clips.append(with_transition)
    
    final_clip = concatenate_videoclips(mp_clips, method="compose")

    proj_name = project["file_name"].split(".")[0]
    output_name = proj_name + "." + ext

    print("Tring to render " + str(len(mp_clips)) + " clips (including text).\nFinal name will be " + output_name)

    final_clip.write_videofile(output_name)
    