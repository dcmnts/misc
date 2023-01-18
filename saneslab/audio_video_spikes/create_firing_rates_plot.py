import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.spike_sorting.views as ssv
import figneuro.views as vv
from distinctipy import distinctipy


firing_rates_npy_uri = 'sha1://2e89846342897a8b521cf58af13463a2452e9cd4?firing_rates.npy'

def create_firing_rates_plot():
    X = kcl.load_npy(firing_rates_npy_uri)
    sampling_rate_hz = 20

    TSG = vv.TimeseriesGraph()
    n = 10
    colors = distinctipy.get_colors(n)
    for j in range(10):
        x = X[j].astype(np.float32)
        t = (np.arange(0, len(x)) / sampling_rate_hz).astype(np.float32)
        TSG.add_line_series(
            name=f'Unit {j + 1}',
            t=t,
            y=x,
            color=distinctipy.get_hex(colors[j])
        )
    return TSG

    # spikes_path = kcl.load_file(spikes_npy_uri)
    # spikes = np.load(spikes_path, allow_pickle=True)

    # plots: List[ssv.RasterPlotItem] = []
    # for i, s in enumerate(spikes):
    #     item = ssv.RasterPlotItem(unit_id=(i + 1), spike_times_sec=s.astype(np.float32))
    #     plots.append(item)
    # raster_plot = ssv.RasterPlot(
    #     start_time_sec=0,
    #     end_time_sec=60 * 15,
    #     plots=plots
    # )
    # return raster_plot

def main():
    firing_rates_plot = create_firing_rates_plot()
    url = firing_rates_plot.url(label="Firing rates plot")
    print(url)

if __name__ == '__main__':
    main()