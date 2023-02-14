# 2/14/23
# https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://7ea4170fca6904aaf40ae12a20735df934b9bf2a&label=composite%20view

from create_raster_plot import create_raster_plot
from create_firing_rates_plot import create_firing_rates_plot
from create_audio_spectrogram import create_audio_spectrogram
from create_annotated_video_view import create_annotated_video_view
from create_head_velocity_plot import create_head_velocity_plot
import figneuro.views as vv


def main():
    V = create_composite_view()
    url = V.url(label='composite view')
    print(url)

def create_composite_view():
    V_camera = create_annotated_video_view()
    # V_empty = vv.Empty()
    V_raster = create_raster_plot()
    V_firing_rate = create_firing_rates_plot()
    V_audio = create_audio_spectrogram()
    V_head_velocity = create_head_velocity_plot()
    view_right = vv.Box(
        direction='vertical',
        items=[
            vv.LayoutItem(
                V_audio
            ),
            vv.LayoutItem(
                V_raster
            ),
            vv.LayoutItem(
                V_firing_rate
            )
        ]
    )
    view_left = vv.Box(
        direction='vertical',
        items=[
            vv.LayoutItem(
                V_camera,
                stretch=2
            ),
            vv.LayoutItem(
                V_head_velocity,
                stretch=1
            )
        ]
    )
    view = vv.Splitter(
        direction='horizontal',
        item1=vv.LayoutItem(view_left, stretch=1),
        item2=vv.LayoutItem(view_right, stretch=2),
    )
    return view

if __name__ == '__main__':
    main()