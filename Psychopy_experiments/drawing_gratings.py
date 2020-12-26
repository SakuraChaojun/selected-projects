from psychopy import visual,monitors
import psychopy.event

m = monitors.Monitor("default")

win = psychopy.visual.Window(
    monitor = m,
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[80, 80]
)

# basic:
grating.draw()
img = win.getMovieFrame() # get the output image

#----------------------------------
# Phase:

#grating_hpos = [-150, -50, 50, 150]
#grating_phase = [0.0, 0.16, 0.33, 0.5]

#for i in range(4):
#    grating.phase = grating_phase[i]
#    grating.pos = [grating_hpos[i], 0]
#    grating.draw()

#----------------------------------
# Frequency:

#grating.sf = 5.0/80.0

#----------------------------------
# Orientation:

#grating.ori = 90

#----------------------------------
# Contrast:
#contrast = [0.1, 0.2, 0.4, 0.8]
#grating_hpos = [-150, -50, 50, 150]

#for i in range(4):
#    grating.contrast = contrast[i]
#    grating.pos = [grating_hpos[i], 0]
#    grating.draw()

#----------------------------------

win.flip()

psychopy.event.waitKeys()

win.close()

img.show()
