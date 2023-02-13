# 2/2/23
# https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://a9f52d9f0d7d89cba5ee194961fe41ea5ab9bd8d&label=camera

from typing import List
import numpy as np
import figneuro.misc.views as mv
import kachery_cloud as kcl
from config import camera_ogv_uri
import cv2


def main():
    V = create_annotated_video_view()
    url = V.url(label='annotated video')
    print(url)

def create_annotated_video_view():
    ogv_fname = kcl.load_file(camera_ogv_uri)

    vid = cv2.VideoCapture(ogv_fname)
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = vid.get(cv2.CAP_PROP_FPS)
    num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'height/width: {height}/{width}')
    print(f'fps: {fps}')
    print(f'num_frames: {num_frames}')

    annotation_frames: List[mv.AnnotationFrame] = []
    for j in range(num_frames):
        elements: List[mv.AnnotationElement] = []
        theta1 = j * 2 * np.pi / 100
        theta2 = j * 2 * np.pi / 60
        theta3 = j * 2 * np.pi / 40
        a = height
        x1 = (a / 2 + a / 3 * np.cos(theta1)).astype(np.float32)
        y1 = (a / 2 + a / 3 * np.sin(theta1)).astype(np.float32)
        x2 = (a / 2 + a / 5 * np.cos(theta2)).astype(np.float32)
        y2 = (a / 2 + a / 5 * np.sin(theta2)).astype(np.float32)
        x3 = (a / 2 + a / 7 * np.cos(theta3)).astype(np.float32)
        y3 = (a / 2 + a / 7 * np.sin(theta3)).astype(np.float32)
        elements.append(mv.NodeElement('0', x=x1, y=y1))
        elements.append(mv.NodeElement('1', x=x2, y=y2))
        elements.append(mv.NodeElement('2', x=x3, y=y3))
        elements.append(mv.EdgeElement('0-1', id1='0', id2='1'))
        elements.append(mv.EdgeElement('1-2', id1='1', id2='2'))
        F = mv.AnnotationFrame(elements=elements)
        annotation_frames.append(F)
    annotations_uri = mv.create_annotations_uri(annotation_frames)

    V = mv.AnnotatedVideo(
        video_uri=camera_ogv_uri,
        video_width=width,
        video_height=height,
        video_num_frames=num_frames,
        sampling_frequency=fps,
        annotations_uri=annotations_uri
    )
    return V

if __name__ == '__main__':
    main()