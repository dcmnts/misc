# Saneslab widgets test

## Raster plot

https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://4edcfa971e3804bae7a383d512ae4f12a37ce039&label=Raster%20plot
<!--
height: 400
-->

See create_raster_plot.py

## Audio spectrogram

The loading delay is due to the time it takes to decompress that spectrogram, plus the time it takes to send the very large decompressed array to the child view.

https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://8c043b845568d0cfc327045174bf409bef250866&label=audio%20spectrogram
<!--
height: 400
-->

See create_audio_spectrogram.py

## Composite view

There is a delay in loading the audio spectrogram (see above). Once the spectrogram loads, the time range is set to the first 120 seconds. If you zoom out too far, the GUI slows down.

I think we can store the spectrogram in a better representation - then things will be much faster.

https://figurl.org/f?v=gs://figurl/figneuro-1&d=sha1://8205fcf0d147461cc3931cb1fde54c48e6b7f80b&label=composite%20view
<!--
height: 700
-->

See create_composite_view.py