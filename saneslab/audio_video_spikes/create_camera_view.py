# 2/2/23
# https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://a9f52d9f0d7d89cba5ee194961fe41ea5ab9bd8d&label=camera

import figneuro.saneslab.views as sl
import kachery_cloud as kcl
from config import camera_ogv_uri
import cv2


def main():
    V = create_camera_view()
    url = V.url(label='camera')
    print(url)

def create_camera_view():
    ogv_fname = kcl.load_file(camera_ogv_uri)

    vid = cv2.VideoCapture(ogv_fname)
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = vid.get(cv2.CAP_PROP_FPS)
    num_frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f'height/width: {height}/{width}')
    print(f'fps: {fps}')
    print(f'num_frames: {num_frames}')

    V = sl.Camera(
        video_uri=camera_ogv_uri,
        video_width=width,
        video_height=height,
        video_num_frames=num_frames,
        sampling_frequency=fps
    )
    return V

if __name__ == '__main__':
    main()