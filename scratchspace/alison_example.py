from typing import List
import pandas as pd
import xarray as xr
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sortingview.views as vv
from visualization_1D_view import create_1D_decode_view

position_info_fname = 'position_info_df.csv'
linear_position_info_fname = 'linear_position_info_df.csv'
marks_fname = 'marks_xarray.nc'
results_fname = 'results_xarray.nc'

unit_spike_times_fname = 'unit_spike_times.npy'

posterior_type='acausal_posterior'
position_name='linear_position'
speed_name='head_speed'

def main():
    position_info = pd.read_csv(position_info_fname)
    linear_position_info = pd.read_csv(linear_position_info_fname)
    print(position_info.columns)
    print(linear_position_info.columns)

    marks = xr.load_dataset(marks_fname)
    results = xr.load_dataset(results_fname)

    ref_time_sec = position_info['time'][0]
    end_time_sec = np.max(position_info['time'])

    #####################################################################################################
    print('Creating 1D decode view')
    view_1d_decode = create_1D_decode_view(
        ref_time_sec=ref_time_sec,
        posterior=results[posterior_type].sum("state"),
        linear_position=linear_position_info[position_name],
    )

    # #####################################################################################################
    # print('Creating probability view')
    # view_probability = vv.TimeseriesGraph()
    # COLOR_CYCLE = [
    #     "#1f77b4",
    #     "#ff7f0e",
    #     "#2ca02c",
    #     "#d62728",
    #     "#9467bd",
    #     "#8c564b",
    #     "#e377c2",
    #     "#7f7f7f",
    #     "#bcbd22",
    #     "#17becf",
    # ]
    # for state, color in zip(results.state.values, COLOR_CYCLE):
    #     view_probability.add_line_series(
    #         name=state,
    #         t=np.asarray(results['time'] - ref_time_sec).astype(np.float32),
    #         y=np.asarray(
    #             results[posterior_type].sel(state=state).sum("position"),
    #             dtype=np.float32,
    #         ),
    #         color=color,
    #         width=1,
    #     )

    #####################################################################################################
    print('Creating speed view')
    view_speed = vv.TimeseriesGraph().add_line_series(
        name="Speed [cm/s]",
        t=np.asarray(position_info['time'] - ref_time_sec).astype(np.float32),
        y=np.asarray(position_info[speed_name], dtype=np.float32),
        color="black",
        width=1,
    )

    #####################################################################################################
    print('Creating raster plot')
    unit_spike_times = np.load(unit_spike_times_fname, allow_pickle=True)
    plot_items: List[vv.RasterPlotItem] = []
    for i in range(len(unit_spike_times)):
        spike_times_sec = unit_spike_times[i] - ref_time_sec
        if len(spike_times_sec) > 0:
            # for unit_id in sorting.get_unit_ids():
            #     spike_times_sec = np.array(sorting.get_unit_spike_train(segment_index=0, unit_id=unit_id)) / sorting.get_sampling_frequency()
            plot_items.append(
                vv.RasterPlotItem(
                    unit_id=f'{i}',
                    spike_times_sec=spike_times_sec.astype(np.float32)
                )
            )
    view_raster_plot = vv.RasterPlot(
        start_time_sec=0,
        end_time_sec=end_time_sec - ref_time_sec,
        plots=plot_items
    )
    view_units_table = vv.UnitsTable(columns=[], rows=[vv.UnitsTableRow(unit_id=f'{i}', values={}) for i in range(len(unit_spike_times)) if len(unit_spike_times) > 0])

    #####################################################################################################
    print('Creating place fields view')
    unit_firing_rates_over_linear_position_bins = np.load('unit_firing_rates_over_linear_position_bins.npy', allow_pickle=True)
    linear_position_bins_cm = np.load('linear_position_bins_cm.npy', allow_pickle=True)
    image_items = []
    for i in range(len(unit_firing_rates_over_linear_position_bins)):
        y = unit_firing_rates_over_linear_position_bins[i]
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig.set_size_inches(5, 3)
        ax.plot(linear_position_bins_cm, y)
        image_items.append(vv.UnitImagesItem(
            unit_id=f'{i}',
            figure=fig,
            dpi=100
        ))
        plt.close(fig)
    view_place_fields = vv.UnitImages(items=image_items, item_width=500, item_height=300)


    #####################################################################################################
    print('Creating timeseries view')
    v_timeseries = vv.Box(
        direction='vertical',
        items=[
            vv.LayoutItem(view_1d_decode, stretch=1, title='Decode', collapsible=True),
            # vv.LayoutItem(view_probability, stretch=1, title='Probability of state', collapsible=True),
            vv.LayoutItem(view_speed, stretch=1, title='Speed', collapsible=True),
            vv.LayoutItem(view_raster_plot, stretch=1, title='Raster', collapsible=True)
        ],
        show_titles=True
    )

    v_right_window = vv.Box(
        direction='horizontal',
        items=[
            vv.LayoutItem(view_units_table, max_size=180),
            vv.LayoutItem(view_place_fields)
        ]
    )

    v_splitter = vv.Splitter(
        direction='horizontal',
        item1=vv.LayoutItem(v_timeseries, stretch=2),
        item2=vv.LayoutItem(v_right_window, stretch=1)
    )

    view = v_splitter
    
    #####################################################################################################
    print('Creating figURL')
    url = view.url(label='alison example')
    print(url)


if __name__ == '__main__':
    main()