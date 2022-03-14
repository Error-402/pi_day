from moviepy.editor import *
from mpmath import mp


def main():
    pi_array = get_pi_array()
    create_montage(pi_array)


def get_pi_array() -> list:
    mp.dps = 100  # numero de digitos
    return [i for i in str(mp.pi)]


def create_montage(pi_array: list) -> None:

    video_order = create_video_order(pi_array)

    final_clip = concatenate_videoclips(video_order, method='compose')
    final_clip.write_videofile('digits_of_pi.mp4', codec='libx264')


def create_video_order(pi_array) -> list:
    video_order = []
    for number in pi_array:
        video_order.append(VideoFileClip(
            str(number) + '.mp4').fx(vfx.speedx, 2))
    return video_order


if __name__ == '__main__':
    main()
