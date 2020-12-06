#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.8),
    on Sat Dec  5 23:45:15 2020
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
psychopyVersion = '2020.2.8'
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
    originPath='/Users/sakuramac/Desktop/Projects/Psychology_Aug_2020/untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "Testtrailcont"
TesttrailcontClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textTesttrait = visual.TextStim(win=win, name='textTesttrait',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_conf = keyboard.Keyboard()
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(2, 0.5)[0], height=(2, 0.5)[1],
    ori=0, pos=(0, -0.5),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textconfscale = visual.TextStim(win=win, name='textconfscale',
    text='1...2...3...4...5...6\nNEW.............OLD',
    font='Arial',
    pos=(0, -0.35), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Testblank"
TestblankClock = core.Clock()
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "TesttrailRFN"
TesttrailRFNClock = core.Clock()
polyBack = visual.Rect(
    win=win, name='polyBack',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textTestwordRFN = visual.TextStim(win=win, name='textTestwordRFN',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_TestRfn = keyboard.Keyboard()
textRFNscale = visual.TextStim(win=win, name='textRFNscale',
    text='(F)amiliar\n(N)either',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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
    trialList=data.importConditions('selection.xlsx', selection='0:6'),
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
    routineTimer.add(1.500000)
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
            if tThisFlipGlobal > polygon_3.tStartRefresh + 1.5-frameTolerance:
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
            if tThisFlipGlobal > textstudy.tStartRefresh + 1.5-frameTolerance:
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
    trialList=data.importConditions('selection.xlsx', selection='0:12'),
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
    
    # ------Prepare to start Routine "Testtrailcont"-------
    continueRoutine = True
    # update component parameters for each repeat
    textTesttrait.setText(word)
    key_conf.keys = []
    key_conf.rt = []
    _key_conf_allKeys = []
    # keep track of which components have finished
    TesttrailcontComponents = [polygon, textTesttrait, key_conf, polygon_5, textconfscale]
    for thisComponent in TesttrailcontComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TesttrailcontClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Testtrailcont"-------
    while continueRoutine:
        # get current time
        t = TesttrailcontClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TesttrailcontClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        # *textTesttrait* updates
        if textTesttrait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textTesttrait.frameNStart = frameN  # exact frame index
            textTesttrait.tStart = t  # local t and not account for scr refresh
            textTesttrait.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textTesttrait, 'tStartRefresh')  # time at next scr refresh
            textTesttrait.setAutoDraw(True)
        
        # *key_conf* updates
        waitOnFlip = False
        if key_conf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_conf.frameNStart = frameN  # exact frame index
            key_conf.tStart = t  # local t and not account for scr refresh
            key_conf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_conf, 'tStartRefresh')  # time at next scr refresh
            key_conf.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_conf.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_conf.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_conf.status == STARTED and not waitOnFlip:
            theseKeys = key_conf.getKeys(keyList=['1', '2', '3', '4', '5', '6'], waitRelease=False)
            _key_conf_allKeys.extend(theseKeys)
            if len(_key_conf_allKeys):
                key_conf.keys = _key_conf_allKeys[-1].name  # just the last key pressed
                key_conf.rt = _key_conf_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        
        # *textconfscale* updates
        if textconfscale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textconfscale.frameNStart = frameN  # exact frame index
            textconfscale.tStart = t  # local t and not account for scr refresh
            textconfscale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textconfscale, 'tStartRefresh')  # time at next scr refresh
            textconfscale.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TesttrailcontComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Testtrailcont"-------
    for thisComponent in TesttrailcontComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    trials.addData('textTesttrait.started', textTesttrait.tStartRefresh)
    trials.addData('textTesttrait.stopped', textTesttrait.tStopRefresh)
    # check responses
    if key_conf.keys in ['', [], None]:  # No response was made
        key_conf.keys = None
    trials.addData('key_conf.keys',key_conf.keys)
    if key_conf.keys != None:  # we had a response
        trials.addData('key_conf.rt', key_conf.rt)
    trials.addData('key_conf.started', key_conf.tStartRefresh)
    trials.addData('key_conf.stopped', key_conf.tStopRefresh)
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    trials.addData('textconfscale.started', textconfscale.tStartRefresh)
    trials.addData('textconfscale.stopped', textconfscale.tStopRefresh)
    # the Routine "Testtrailcont" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Testblank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    text.setText(word)
    # keep track of which components have finished
    TestblankComponents = [polygon_4, text]
    for thisComponent in TestblankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestblankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Testblank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TestblankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestblankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestblankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Testblank"-------
    for thisComponent in TestblankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "TesttrailRFN"-------
    continueRoutine = True
    # update component parameters for each repeat
    textTestwordRFN.setText(word)
    key_TestRfn.keys = []
    key_TestRfn.rt = []
    _key_TestRfn_allKeys = []
    # keep track of which components have finished
    TesttrailRFNComponents = [polyBack, textTestwordRFN, key_TestRfn, textRFNscale]
    for thisComponent in TesttrailRFNComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TesttrailRFNClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TesttrailRFN"-------
    while continueRoutine:
        # get current time
        t = TesttrailRFNClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TesttrailRFNClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polyBack* updates
        if polyBack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polyBack.frameNStart = frameN  # exact frame index
            polyBack.tStart = t  # local t and not account for scr refresh
            polyBack.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polyBack, 'tStartRefresh')  # time at next scr refresh
            polyBack.setAutoDraw(True)
        
        # *textTestwordRFN* updates
        if textTestwordRFN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textTestwordRFN.frameNStart = frameN  # exact frame index
            textTestwordRFN.tStart = t  # local t and not account for scr refresh
            textTestwordRFN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textTestwordRFN, 'tStartRefresh')  # time at next scr refresh
            textTestwordRFN.setAutoDraw(True)
        
        # *key_TestRfn* updates
        waitOnFlip = False
        if key_TestRfn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_TestRfn.frameNStart = frameN  # exact frame index
            key_TestRfn.tStart = t  # local t and not account for scr refresh
            key_TestRfn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_TestRfn, 'tStartRefresh')  # time at next scr refresh
            key_TestRfn.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_TestRfn.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_TestRfn.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_TestRfn.status == STARTED and not waitOnFlip:
            theseKeys = key_TestRfn.getKeys(keyList=['f', 'n'], waitRelease=False)
            _key_TestRfn_allKeys.extend(theseKeys)
            if len(_key_TestRfn_allKeys):
                key_TestRfn.keys = _key_TestRfn_allKeys[-1].name  # just the last key pressed
                key_TestRfn.rt = _key_TestRfn_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *textRFNscale* updates
        if textRFNscale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textRFNscale.frameNStart = frameN  # exact frame index
            textRFNscale.tStart = t  # local t and not account for scr refresh
            textRFNscale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textRFNscale, 'tStartRefresh')  # time at next scr refresh
            textRFNscale.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TesttrailRFNComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TesttrailRFN"-------
    for thisComponent in TesttrailRFNComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polyBack.started', polyBack.tStartRefresh)
    trials.addData('polyBack.stopped', polyBack.tStopRefresh)
    trials.addData('textTestwordRFN.started', textTestwordRFN.tStartRefresh)
    trials.addData('textTestwordRFN.stopped', textTestwordRFN.tStopRefresh)
    # check responses
    if key_TestRfn.keys in ['', [], None]:  # No response was made
        key_TestRfn.keys = None
    trials.addData('key_TestRfn.keys',key_TestRfn.keys)
    if key_TestRfn.keys != None:  # we had a response
        trials.addData('key_TestRfn.rt', key_TestRfn.rt)
    trials.addData('key_TestRfn.started', key_TestRfn.tStartRefresh)
    trials.addData('key_TestRfn.stopped', key_TestRfn.tStopRefresh)
    trials.addData('textRFNscale.started', textRFNscale.tStartRefresh)
    trials.addData('textRFNscale.stopped', textRFNscale.tStopRefresh)
    # the Routine "TesttrailRFN" was not non-slip safe, so reset the non-slip timer
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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
