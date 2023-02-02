import numpy as np
import kachery_cloud as kcl
import figneuro.views as vv
from config import head_velocity_npy_uri
import matplotlib.pyplot as plt


def create_head_velocity_plot():
    head_velocity = kcl.load_npy(head_velocity_npy_uri)
    sampling_frequency = 30 # same as camera
    tg = vv.TimeseriesGraph()
    tg.add_line_series(
        name='head-velocity',
        t=(np.arange(0, len(head_velocity)) / sampling_frequency).astype(np.float32),
        y=head_velocity.astype(np.float32),
        color='black'
    )
    return tg

def main():
    head_velocity_plot = create_head_velocity_plot()
    url = head_velocity_plot.url(label="Head velocity")
    print(url)

if __name__ == '__main__':
    main()