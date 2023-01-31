import cv2
import kachery_cloud as kcl
from config import camera_ogv_uri

ogv_fname = kcl.load_file(camera_ogv_uri)

vid = cv2.VideoCapture(ogv_fname)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = vid.get(cv2.CAP_PROP_FPS)
print(f'height/width: {height}/{width}')
print(f'fps: {fps}')