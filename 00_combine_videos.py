"""
Combines video files from subdirectories into a single video file.
"""

import os
from tqdm.auto import tqdm
from moviepy.editor import *


def combine_video_files(file_list: str, output_file_name: str):
    """
    file_list: a list of files to combine.
    output_file_name: the name of the combined video file.

    returns: final filename - combines all video files in file_list into a single video file.
    """

    clip_list = []
    # load all files in file_list
    for filename in tqdm(file_list, desc='Loading video files'):
        clip = VideoFileClip(filename)
        clip_list.append(clip)

    # combine all clips into a single clip
    combined_clip = concatenate_videoclips(clip_list)
    combined_clip.write_videofile(output_file_name)





def create_directory_vid(dir_in: str):
    """
    dir_in: the directory containing the video files to combine.

    returns: None - combines all video files in dir_in into a single video file.
    """

    # list all files in 
    files = os.listdir(dir_in)
    files.sort()

    # get the directory name
    dir_name = os.path.basename(dir_in)

    combined_file_name = dir_in + "/" + dir_name + '_combined.mp4'

    print(f'Running on {dir_in}...')
    print(f'Found files: {len(files)}')
    print(f'Output file name: {combined_file_name}')


    files = [os.path.join(dir_in, f) for f in files]
    # print(files)
    combine_video_files(files, combined_file_name)



if __name__ == '__main__':

    dir_name = '/home/tony/Videos/20240108/00'
    create_directory_vid(dir_name)
