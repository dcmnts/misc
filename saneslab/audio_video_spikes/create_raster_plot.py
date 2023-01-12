import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.spike_sorting.views as ssv


video_timestamps_npy_uri = 'sha1://df13b1efdc8ba07a1c1e64c3710cc5bbc5ef6394?label=video_timestamps_s.npy'
spikes_npy_uri = 'sha1://d0357a63035753a4520b990170e0c59c8ef417f5?label=spikes.npy'
camera_avi_uri = 'sha1://6fe810f0e96288f362a29ed3844ff3623f43588b?label=2022_08_26_16_25_27_533291_cam_b.avi'
mic_wav_uri = 'sha1://3aeecc0796895f06909a2116a6fd22f99cd7751b?label=mic_2022_08_26_16_25_27_533291_combined.wav'

def create_raster_plot():
    spikes_path = kcl.load_file(spikes_npy_uri)
    spikes = np.load(spikes_path, allow_pickle=True)

    plots: List[ssv.RasterPlotItem] = []
    for i, s in enumerate(spikes):
        item = ssv.RasterPlotItem(unit_id=(i + 1), spike_times_sec=s.astype(np.float32))
        plots.append(item)
    raster_plot = ssv.RasterPlot(
        start_time_sec=0,
        end_time_sec=60 * 15,
        plots=plots
    )
    return raster_plot

def main():
    raster_plot = create_raster_plot()
    url = raster_plot.url(label="Raster plot")
    print(url)

if __name__ == '__main__':
    main()