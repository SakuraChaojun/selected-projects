#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 08, 2020, at 01:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\36552\\Desktop\\assignment4\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
weclomeText = visual.TextStim(win=win, name='weclomeText',
    text='Welcome to our experiment\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_welcome = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyback = visual.Rect(
    win=win, name='polyback',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trail"
trailClock = core.Clock()
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textstudy = visual.TextStim(win=win, name='textstudy',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyback = visual.Rect(
    win=win, name='polyback',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "waithere"
waithereClock = core.Clock()
textWait = visual.TextStim(win=win, name='textWait',
    text='Please wait \n\nready press space',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_respexit = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyback = visual.Rect(
    win=win, name='polyback',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyback = visual.Rect(
    win=win, name='polyback',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
textEnd = visual.TextStim(win=win, name='textEnd',
    text='Thanks for participating ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_welcome.keys = []
key_welcome.rt = []
_key_welcome_allKeys = []
# keep track of which components have finished
instructionComponents = [weclomeText, key_welcome]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *weclomeText* updates
    if weclomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        weclomeText.frameNStart = frameN  # exact frame index
        weclomeText.tStart = t  # local t and not account for scr refresh
        weclomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(weclomeText, 'tStartRefresh')  # time at next scr refresh
        weclomeText.setAutoDraw(True)
    
    # *key_welcome* updates
    waitOnFlip = False
    if key_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_welcome.frameNStart = frameN  # exact frame index
        key_welcome.tStart = t  # local t and not account for scr refresh
        key_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
        key_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_welcome.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_welcome_allKeys.extend(theseKeys)
        if len(_key_welcome_allKeys):
            key_welcome.keys = _key_welcome_allKeys[-1].name  # just the last key pressed
            key_welcome.rt = _key_welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('weclomeText.started', weclomeText.tStartRefresh)
thisExp.addData('weclomeText.stopped', weclomeText.tStopRefresh)
# check responses
if key_welcome.keys in ['', [], None]:  # No response was made
    key_welcome.keys = None
thisExp.addData('key_welcome.keys',key_welcome.keys)
if key_welcome.keys != None:  # we had a response
    thisExp.addData('key_welcome.rt', key_welcome.rt)
thisExp.addData('key_welcome.started', key_welcome.tStartRefresh)
thisExp.addData('key_welcome.stopped', key_welcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [polyback, textBlank500]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polyback* updates
    if polyback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polyback.frameNStart = frameN  # exact frame index
        polyback.tStart = t  # local t and not account for scr refresh
        polyback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polyback, 'tStartRefresh')  # time at next scr refresh
        polyback.setAutoDraw(True)
    if polyback.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polyback.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            polyback.tStop = t  # not accounting for scr refresh
            polyback.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polyback, 'tStopRefresh')  # time at next scr refresh
            polyback.setAutoDraw(False)
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polyback.started', polyback.tStartRefresh)
thisExp.addData('polyback.stopped', polyback.tStopRefresh)
thisExp.addData('textBlank500.started', textBlank500.tStartRefresh)
thisExp.addData('textBlank500.stopped', textBlank500.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialsStudy = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word.xlsx', selection='0:3'),
    seed=None, name='trialsStudy')
thisExp.addLoop(trialsStudy)  # add the loop to the experiment
thisTrialsStudy = trialsStudy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
if thisTrialsStudy != None:
    for paramName in thisTrialsStudy:
        exec('{} = thisTrialsStudy[paramName]'.format(paramName))

for thisTrialsStudy in trialsStudy:
    currentLoop = trialsStudy
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
    if thisTrialsStudy != None:
        for paramName in thisTrialsStudy:
            exec('{} = thisTrialsStudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trail"-------
    continueRoutine = True
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    textstudy.setText(word)
    # keep track of which components have finished
    trailComponents = [polygon_3, textstudy]
    for thisComponent in trailComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trailClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trail"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trailClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trailClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # *textstudy* updates
        if textstudy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textstudy.frameNStart = frameN  # exact frame index
            textstudy.tStart = t  # local t and not account for scr refresh
            textstudy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textstudy, 'tStartRefresh')  # time at next scr refresh
            textstudy.setAutoDraw(True)
        if textstudy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textstudy.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                textstudy.tStop = t  # not accounting for scr refresh
                textstudy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textstudy, 'tStopRefresh')  # time at next scr refresh
                textstudy.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trailComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trail"-------
    for thisComponent in trailComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('polygon_3.started', polygon_3.tStartRefresh)
    trialsStudy.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    trialsStudy.addData('textstudy.started', textstudy.tStartRefresh)
    trialsStudy.addData('textstudy.stopped', textstudy.tStopRefresh)
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [polyback, textBlank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polyback* updates
        if polyback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polyback.frameNStart = frameN  # exact frame index
            polyback.tStart = t  # local t and not account for scr refresh
            polyback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polyback, 'tStartRefresh')  # time at next scr refresh
            polyback.setAutoDraw(True)
        if polyback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polyback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polyback.tStop = t  # not accounting for scr refresh
                polyback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polyback, 'tStopRefresh')  # time at next scr refresh
                polyback.setAutoDraw(False)
        
        # *textBlank500* updates
        if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500.frameNStart = frameN  # exact frame index
            textBlank500.tStart = t  # local t and not account for scr refresh
            textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(True)
        if textBlank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500.tStop = t  # not accounting for scr refresh
                textBlank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
                textBlank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('polyback.started', polyback.tStartRefresh)
    trialsStudy.addData('polyback.stopped', polyback.tStopRefresh)
    trialsStudy.addData('textBlank500.started', textBlank500.tStartRefresh)
    trialsStudy.addData('textBlank500.stopped', textBlank500.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsStudy'


# ------Prepare to start Routine "waithere"-------
continueRoutine = True
# update component parameters for each repeat
key_respexit.keys = []
key_respexit.rt = []
_key_respexit_allKeys = []
# keep track of which components have finished
waithereComponents = [textWait, key_respexit]
for thisComponent in waithereComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waithereClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "waithere"-------
while continueRoutine:
    # get current time
    t = waithereClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waithereClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWait* updates
    if textWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWait.frameNStart = frameN  # exact frame index
        textWait.tStart = t  # local t and not account for scr refresh
        textWait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWait, 'tStartRefresh')  # time at next scr refresh
        textWait.setAutoDraw(True)
    
    # *key_respexit* updates
    waitOnFlip = False
    if key_respexit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_respexit.frameNStart = frameN  # exact frame index
        key_respexit.tStart = t  # local t and not account for scr refresh
        key_respexit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_respexit, 'tStartRefresh')  # time at next scr refresh
        key_respexit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_respexit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_respexit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_respexit.status == STARTED and not waitOnFlip:
        theseKeys = key_respexit.getKeys(keyList=['space'], waitRelease=False)
        _key_respexit_allKeys.extend(theseKeys)
        if len(_key_respexit_allKeys):
            key_respexit.keys = _key_respexit_allKeys[-1].name  # just the last key pressed
            key_respexit.rt = _key_respexit_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waithereComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "waithere"-------
for thisComponent in waithereComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWait.started', textWait.tStartRefresh)
thisExp.addData('textWait.stopped', textWait.tStopRefresh)
# check responses
if key_respexit.keys in ['', [], None]:  # No response was made
    key_respexit.keys = None
thisExp.addData('key_respexit.keys',key_respexit.keys)
if key_respexit.keys != None:  # we had a response
    thisExp.addData('key_respexit.rt', key_respexit.rt)
thisExp.addData('key_respexit.started', key_respexit.tStartRefresh)
thisExp.addData('key_respexit.stopped', key_respexit.tStopRefresh)
thisExp.nextEntry()
# the Routine "waithere" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [polyback, textBlank500]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polyback* updates
    if polyback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polyback.frameNStart = frameN  # exact frame index
        polyback.tStart = t  # local t and not account for scr refresh
        polyback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polyback, 'tStartRefresh')  # time at next scr refresh
        polyback.setAutoDraw(True)
    if polyback.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polyback.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            polyback.tStop = t  # not accounting for scr refresh
            polyback.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polyback, 'tStopRefresh')  # time at next scr refresh
            polyback.setAutoDraw(False)
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polyback.started', polyback.tStartRefresh)
thisExp.addData('polyback.stopped', polyback.tStopRefresh)
thisExp.addData('textBlank500.started', textBlank500.tStartRefresh)
thisExp.addData('textBlank500.stopped', textBlank500.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [polyback, textBlank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polyback* updates
        if polyback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polyback.frameNStart = frameN  # exact frame index
            polyback.tStart = t  # local t and not account for scr refresh
            polyback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polyback, 'tStartRefresh')  # time at next scr refresh
            polyback.setAutoDraw(True)
        if polyback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polyback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polyback.tStop = t  # not accounting for scr refresh
                polyback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polyback, 'tStopRefresh')  # time at next scr refresh
                polyback.setAutoDraw(False)
        
        # *textBlank500* updates
        if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500.frameNStart = frameN  # exact frame index
            textBlank500.tStart = t  # local t and not account for scr refresh
            textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(True)
        if textBlank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500.tStop = t  # not accounting for scr refresh
                textBlank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
                textBlank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polyback.started', polyback.tStartRefresh)
    trials.addData('polyback.stopped', polyback.tStopRefresh)
    trials.addData('textBlank500.started', textBlank500.tStartRefresh)
    trials.addData('textBlank500.stopped', textBlank500.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [textEnd]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.tStart = t  # local t and not account for scr refresh
        textEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
        textEnd.setAutoDraw(True)
    if textEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEnd.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            textEnd.tStop = t  # not accounting for scr refresh
            textEnd.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEnd, 'tStopRefresh')  # time at next scr refresh
            textEnd.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEnd.started', textEnd.tStartRefresh)
thisExp.addData('textEnd.stopped', textEnd.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
