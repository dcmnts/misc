import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.spike_sorting.views as ssv
from config import spikes_npy_uri


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