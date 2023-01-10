# Raster plot test

It seems the spike trains only go up to 167 seconds, whereas I thought the duration was supposed to be 15 minutes.

https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://f1722bc23ad55be2a2c0af7189303536f360194d&label=Raster%20plot

Script for generating this:

```python
import numpy as np
from typing import List
import kachery_cloud as kcl
import figneuro.spike_sorting.views as ssv


spikes_npy_uri = 'sha1://96197669d7355a153683597a4f0fed376ecf785b?label=spikes.npy'

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