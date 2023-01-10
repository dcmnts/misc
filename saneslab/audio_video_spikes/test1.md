# Raster plot test

Here's a raster plot

https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://4edcfa971e3804bae7a383d512ae4f12a37ce039&label=Raster%20plot
<!--
height: 400
-->

Script for generating this:

```python
import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.spike_sorting.views as ssv


spikes_npy_uri = 'sha1://d0357a63035753a4520b990170e0c59c8ef417f5?label=spikes.npy'

def main():
    spikes_path = kcl.load_file(spikes_npy_uri)
    spikes = np.load(spikes_path, allow_pickle=True)

    plots: List[ssv.RasterPlotItem] = []
    for i, s in enumerate(spikes):
        item = ssv.RasterPlotItem(unit_id=(i + 1), spike_times_sec=s.astype(np.float32))
        plots.append(item)
        print(np.max(s))
    raster_plot = ssv.RasterPlot(
        start_time_sec=0,
        end_time_sec=60 * 15,
        plots=plots
    )
    url = raster_plot.url(label="Raster plot")
    print(url)

if __name__ == '__main__':
    main()
```