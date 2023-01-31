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
    V_c = create_camera_view()
    V_rp = create_raster_plot()
    V_fr = create_firing_rates_plot()
    V_as = create_audio_spectrogram()
    view_right = vv.Box(
        direction='vertical',
        items=[
            vv.LayoutItem(
                V_as
            ),
            vv.LayoutItem(
                V_fr
            ),
            vv.LayoutItem(
                V_rp
            )
        ]
    )
    view = vv.Box(
        direction='horizontal',
        items=[
            vv.LayoutItem(V_c, stretch=1),
            vv.LayoutItem(view_right, stretch=2)
        ]
    )
    return view

if __name__ == '__main__':
    main()