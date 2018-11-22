

###############################################################
# Standard imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plot
import librosa

import librosa.display

###############################################################
# Load an example with vocals.
y, smr = librosa.load('genevieve.wav', duration=120)


# And compute the spectrogram magnitude and phase
full_S, phase = librosa.magphase(librosa.stft(y))


###############################################################
# Plot a 5-second slice of the spectrum
index = slice(*librosa.time_to_frames([30, 35], sr=smr))
plot.figure(figsize=(12, 4))	
librosa.display.specshow(librosa.amplitude_to_db(full_S[:, index], ref=np.max),
                         y_axis='log', x_axis='time', sr=smr)
					 
plot.colorbar()
plot.tight_layout()


###############################################################
#The wavy lines above are due to the voice component.
#Our goal is to separate them from those who accompany them.
#instrumentation.


#We will compare the images using cosine similarity and aggregate similar images
#taking their median value (by frequency).

#To avoid being skewed by local continuity, we are compelling similar frameworks to
#separated by at least 2 seconds.

#This removes sparse / non-repetitive deviations from the average spectrum,
#and works well to eliminate the vocal elements.

filter_S = librosa.decompose.nn_filter(full_S,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=smr)))

'''The filter output must not be greater than the input
if we assume that the signals are additive. Taking the punctual minimium
with the input spectrum requires that.'''
filter_S = np.minimum(full_S, filter_S)


#################################################################
'''The output of the raw filter can be used as a mask,
but it sounds better if we use soft masking.

We can also use a margin to reduce the bleed between voices and instrumentation masks.
Note: Margins do not need to be equal for foreground and background separation
'''
#margin i and margin v
mi, mv = 2, 10
power = 2

v_mask = librosa.util.softmask(full_S - filter_S,
                               mv * filter_S,
                               power=power)


i_mask = librosa.util.softmask(filter_S,
                               mi * (full_S - filter_S),
                               power=power)


'''Once we have the masks, just multiply them with the input spectrum
separate the components'''

background_S = i_mask * full_S
foreground_S = v_mask * full_S


#######################################################################
'''Draw the same slice, but by separating its foreground and background

sphinx_gallery_thumbnail_number = 2'''

plot.figure(figsize=(12, 8))
plot.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(full_S[:, index], ref=np.max),
                         y_axis='log', sr=smr)
plot.title('Full spectrum')
plot.colorbar()

plot.subplot(3, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(background_S[:, index], ref=np.max),
                         y_axis='log', sr=smr)
plot.title('Background Audio')
plot.colorbar()
plot.subplot(3, 1, 3)
librosa.display.specshow(librosa.amplitude_to_db(foreground_S[:, index], ref=np.max),
                         y_axis='log', x_axis='time', sr=smr)
plot.title('Foreground Audio')
plot.colorbar()
plot.tight_layout()
plot.show()
