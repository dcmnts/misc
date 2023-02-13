# https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://1a27dad4d2206c5eb3dc8a6cdfaf1ee0fc7115e3&label=Firing%20rates%20plot

import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.saneslab.views as slv
from config import spikes_npy_uri


def create_firing_rates_plot():
    spikes_path = kcl.load_file(spikes_npy_uri)
    spikes = np.load(spikes_path, allow_pickle=True)

    plots: List[slv.FiringRatesPlotItem] = []
    end_time_sec = 0
    for i, s in enumerate(spikes):
        item = slv.FiringRatesPlotItem(unit_id=(i + 1), spike_times_sec=s.astype(np.float32))
        end_time_sec = np.float32(np.maximum(end_time_sec, np.max(s)))
        plots.append(item)
    firing_rates_plot = slv.FiringRatesPlot(
        start_time_sec=0,
        end_time_sec=end_time_sec,
        plots=plots,
        hide_toolbar=True
    )
    return firing_rates_plot

def main():
    firing_rates_plot = create_firing_rates_plot()
    url = firing_rates_plot.url(label="Firing rates plot")
    print(url)

if __name__ == '__main__':
    main()