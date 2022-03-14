from moviepy.editor import *
from mpmath import mp
import argparse


def main(args):
    pi_array = get_pi_array(args.digits)
    create_montage(pi_array)


def get_pi_array(digits: str) -> list:
    mp.dps = int(digits)  # numero de digitos
    return [i for i in str(mp.pi)]


def create_montage(pi_array: list) -> None:

    video_order = create_video_order(pi_array)

    final_clip = concatenate_videoclips(video_order, method='compose')
    final_clip.write_videofile('digits_of_pi.mp4', codec='libx264')


def create_video_order(pi_array: list) -> list:
    video_order = []
    for number in pi_array:
        video_order.append(VideoFileClip(
            str(number) + '.mp4').fx(vfx.speedx, 2))
    return video_order


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make pi montage')
    parser.add_argument(
        '--digits', type=str, help='how many digits you want in the montage', default='100')
    args = parser.parse_args()
    main(args)
