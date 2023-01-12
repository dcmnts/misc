from create_raster_plot import create_raster_plot
from create_audio_spectrogram import create_audio_spectrogram
import figneuro.views as vv


def main():
    V = create_composite_view()
    url = V.url(label='composite view')
    print(url)

def create_composite_view():
    V_rp = create_raster_plot()
    V_as = create_audio_spectrogram()
    view = vv.Box(
        direction='vertical',
        items=[
            vv.LayoutItem(
                V_rp
            ),
            vv.LayoutItem(
                V_as
            )
        ]
    )
    return view

if __name__ == '__main__':
    main()