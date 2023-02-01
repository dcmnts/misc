# 2/1/23
# https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://ed2f4b792b3028c984af121c9a78f65c73fb6846&label=composite%20view

from create_raster_plot import create_raster_plot
from create_firing_rates_plot import create_firing_rates_plot
from create_audio_spectrogram import create_audio_spectrogram
from create_camera_view import create_camera_view
import figneuro.views as vv


def main():
    V = create_composite_view()
    url = V.url(label='composite view')
    print(url)

def create_composite_view():
    V_camera = create_camera_view()
    V_empty = vv.Empty()
    V_raster = create_raster_plot()
    V_firing_rate = create_firing_rates_plot()
    V_audio = create_audio_spectrogram()
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
                V_empty,
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