#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Nov 27 10:53:43 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'PVT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
subject_directory = os.path.abspath(os.path.join(_thisDir, "../")) + os.sep + f'results/sub-{expInfo["participant"]}/ses-{expInfo["session"]}/'
if not os.path.exists(subject_directory):
    os.makedirs(subject_directory)
    
filename = f'sub-{expInfo["participant"]}_ses-{expInfo["session"]}_task-pvt'
output_path = f'{subject_directory}{filename}'
print(f'OUTPUT PATH: {output_path}')
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/u1984094/Documents/submarine/psychomotor_vigilance_task/PVT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=output_path)
# save a log file for detail verbose info
logFile = logging.LogFile(output_path + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsText = visual.TextStim(win=win, name='InstructionsText',
    text='Welcome!\n\n\nIn this task, you are to press the SPACEBAR as quick as possible after a red counter appears\non screen.\n\n\nStart the task by pressing the  SPACEBAR.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstrucKey = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
# All the durations are in seconds
# Random ISI between 2 and 10. 
minISI = 2
maxISI = 10

# Task duration (10 mins, 600 seconds).
length_of_task = 600

# Feedback duration 
feed = 0.5

# A timer
timing = core.Clock()

# Loading the beep sound
warning_beep = sound.Sound('beep.wav')

ISI_text = visual.TextStim(win=win, name='ISI_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
dontrespond = keyboard.Keyboard()

# Initialize components for Routine "Target"
TargetClock = core.Clock()
Targetstim = visual.TextStim(win=win, name='Targetstim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Response = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Feedback_text = visual.TextStim(win=win, name='Feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End_task"
End_taskClock = core.Clock()

# Initialize components for Routine "The_end"
The_endClock = core.Clock()
Goodbye = visual.TextStim(win=win, name='Goodbye',
    text='Thanks you for your participation\n\nPress the SPACE key to end the task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GoodbyeEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
InstrucKey.keys = []
InstrucKey.rt = []
_InstrucKey_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, InstrucKey]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText* updates
    if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText.frameNStart = frameN  # exact frame index
        InstructionsText.tStart = t  # local t and not account for scr refresh
        InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
        InstructionsText.setAutoDraw(True)
    
    # *InstrucKey* updates
    waitOnFlip = False
    if InstrucKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrucKey.frameNStart = frameN  # exact frame index
        InstrucKey.tStart = t  # local t and not account for scr refresh
        InstrucKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrucKey, 'tStartRefresh')  # time at next scr refresh
        InstrucKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstrucKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstrucKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstrucKey.status == STARTED and not waitOnFlip:
        theseKeys = InstrucKey.getKeys(keyList=['space'], waitRelease=False)
        _InstrucKey_allKeys.extend(theseKeys)
        if len(_InstrucKey_allKeys):
            InstrucKey.keys = _InstrucKey_allKeys[-1].name  # just the last key pressed
            InstrucKey.rt = _InstrucKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsText.started', InstructionsText.tStartRefresh)
thisExp.addData('InstructionsText.stopped', InstructionsText.tStopRefresh)
# check responses
if InstrucKey.keys in ['', [], None]:  # No response was made
    InstrucKey.keys = None
thisExp.addData('InstrucKey.keys',InstrucKey.keys)
if InstrucKey.keys != None:  # we had a response
    thisExp.addData('InstrucKey.rt', InstrucKey.rt)
thisExp.addData('InstrucKey.started', InstrucKey.tStartRefresh)
thisExp.addData('InstrucKey.stopped', InstrucKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PVT_Trials = data.TrialHandler(nReps=120.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='PVT_Trials')
thisExp.addLoop(PVT_Trials)  # add the loop to the experiment
thisPVT_Trial = PVT_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPVT_Trial.rgb)
if thisPVT_Trial != None:
    for paramName in thisPVT_Trial:
        exec('{} = thisPVT_Trial[paramName]'.format(paramName))

for thisPVT_Trial in PVT_Trials:
    currentLoop = PVT_Trials
    # abbreviate parameter names if possible (e.g. rgb = thisPVT_Trial.rgb)
    if thisPVT_Trial != None:
        for paramName in thisPVT_Trial:
            exec('{} = thisPVT_Trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # ISI is then set each routine
    randISI = random() * (maxISI - minISI) + minISI
    
    # If it is the first trial
    if PVT_Trials.thisN == 0:
        overall_timer = core.Clock()
        realISI = 0
        
    if PVT_Trials.thisN > 0:
        # We count the duration of the feedback as part of the ISI
        realISI = feed
    
    # A message when participant miss
    message = 'You did not hit the button!'
    
    # Adding the ISI so it is saved in the datafile
    thisExp.addData('ISI', randISI)
    dontrespond.keys = []
    dontrespond.rt = []
    _dontrespond_allKeys = []
    # keep track of which components have finished
    ISIComponents = [ISI_text, dontrespond]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys = dontrespond.getKeys(keyList=['space'], waitRelease=False)
        keys = [key.name for key in keys]
        
        # Append True to list if a key is pressed, clear list if not
        if "space" in keys:
             message = "Too soon!"
             continueRoutine = False
            
        
        # *ISI_text* updates
        if ISI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_text.frameNStart = frameN  # exact frame index
            ISI_text.tStart = t  # local t and not account for scr refresh
            ISI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_text, 'tStartRefresh')  # time at next scr refresh
            ISI_text.setAutoDraw(True)
        if ISI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_text.tStartRefresh + randISI-realISI-frameTolerance:
                # keep track of stop time/frame for later
                ISI_text.tStop = t  # not accounting for scr refresh
                ISI_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISI_text, 'tStopRefresh')  # time at next scr refresh
                ISI_text.setAutoDraw(False)
        
        # *dontrespond* updates
        waitOnFlip = False
        if dontrespond.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dontrespond.frameNStart = frameN  # exact frame index
            dontrespond.tStart = t  # local t and not account for scr refresh
            dontrespond.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dontrespond, 'tStartRefresh')  # time at next scr refresh
            dontrespond.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(dontrespond.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(dontrespond.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if dontrespond.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dontrespond.tStartRefresh + randISI-1-frameTolerance:
                # keep track of stop time/frame for later
                dontrespond.tStop = t  # not accounting for scr refresh
                dontrespond.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dontrespond, 'tStopRefresh')  # time at next scr refresh
                dontrespond.status = FINISHED
        if dontrespond.status == STARTED and not waitOnFlip:
            theseKeys = dontrespond.getKeys(keyList=['space'], waitRelease=False)
            _dontrespond_allKeys.extend(theseKeys)
            if len(_dontrespond_allKeys):
                dontrespond.keys = _dontrespond_allKeys[-1].name  # just the last key pressed
                dontrespond.rt = _dontrespond_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PVT_Trials.addData('ISI_text.started', ISI_text.tStartRefresh)
    PVT_Trials.addData('ISI_text.stopped', ISI_text.tStopRefresh)
    # check responses
    if dontrespond.keys in ['', [], None]:  # No response was made
        dontrespond.keys = None
    PVT_Trials.addData('dontrespond.keys',dontrespond.keys)
    if dontrespond.keys != None:  # we had a response
        PVT_Trials.addData('dontrespond.rt', dontrespond.rt)
    PVT_Trials.addData('dontrespond.started', dontrespond.tStartRefresh)
    PVT_Trials.addData('dontrespond.stopped', dontrespond.tStopRefresh)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Target"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    # Reset the timer
    timing.reset()
    
    # Check for response
    if message == 'Too soon!':
        # Adding 0 to Accuracy and missing to RTms
        thisExp.addData('Accuracy', 0)
        thisExp.addData('RTms', np.NAN)
        # End the Routine to continue next trial
        continueRoutine = False
    
    Response.keys = []
    Response.rt = []
    _Response_allKeys = []
    # keep track of which components have finished
    TargetComponents = [Targetstim, Response]
    for thisComponent in TargetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TargetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Target"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TargetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TargetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # counter in seconds
        time = int(round(timing.getTime(), 3) * 1000)
        
        
        
        # *Targetstim* updates
        if Targetstim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Targetstim.frameNStart = frameN  # exact frame index
            Targetstim.tStart = t  # local t and not account for scr refresh
            Targetstim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Targetstim, 'tStartRefresh')  # time at next scr refresh
            Targetstim.setAutoDraw(True)
        if Targetstim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Targetstim.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Targetstim.tStop = t  # not accounting for scr refresh
                Targetstim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Targetstim, 'tStopRefresh')  # time at next scr refresh
                Targetstim.setAutoDraw(False)
        if Targetstim.status == STARTED:  # only update if drawing
            Targetstim.setText(time, log=False)
        
        # *Response* updates
        waitOnFlip = False
        if Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Response.frameNStart = frameN  # exact frame index
            Response.tStart = t  # local t and not account for scr refresh
            Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Response.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Response.tStop = t  # not accounting for scr refresh
                Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Response, 'tStopRefresh')  # time at next scr refresh
                Response.status = FINISHED
        if Response.status == STARTED and not waitOnFlip:
            theseKeys = Response.getKeys(keyList=['space'], waitRelease=False)
            _Response_allKeys.extend(theseKeys)
            if len(_Response_allKeys):
                Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                Response.rt = _Response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TargetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Target"-------
    for thisComponent in TargetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if type(Response.rt) is float:
        message = str(round(Response.rt * 1000))
        thisExp.addData('Accuracy', 1)
        thisExp.addData('RTms', Response.rt * 1000)
        
    # PsychoPy is not running the trial for more than 29.991...
    if timing.getTime() >= 29.99:
            message = 'No response!'
            warning_beep.play()
            Response.rt = timing.getTime()
            thisExp.addData('RTms', np.NAN)
            thisExp.addData('Accuracy', 0)
            continueRoutine = False
    PVT_Trials.addData('Targetstim.started', Targetstim.tStartRefresh)
    PVT_Trials.addData('Targetstim.stopped', Targetstim.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
    PVT_Trials.addData('Response.keys',Response.keys)
    if Response.keys != None:  # we had a response
        PVT_Trials.addData('Response.rt', Response.rt)
    PVT_Trials.addData('Response.started', Response.tStartRefresh)
    PVT_Trials.addData('Response.stopped', Response.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Feedback_text.setText(message)
    # keep track of which components have finished
    FeedbackComponents = [Feedback_text]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback_text* updates
        if Feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Feedback_text.frameNStart = frameN  # exact frame index
            Feedback_text.tStart = t  # local t and not account for scr refresh
            Feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_text, 'tStartRefresh')  # time at next scr refresh
            Feedback_text.setAutoDraw(True)
        if Feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_text.tStartRefresh + feed-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_text.tStop = t  # not accounting for scr refresh
                Feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_text, 'tStopRefresh')  # time at next scr refresh
                Feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PVT_Trials.addData('Feedback_text.started', Feedback_text.tStartRefresh)
    PVT_Trials.addData('Feedback_text.stopped', Feedback_text.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "End_task"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    End_taskComponents = []
    for thisComponent in End_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_task"-------
    while continueRoutine:
        # get current time
        t = End_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_task"-------
    for thisComponent in End_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Get the time in the task
    time_in_task = overall_timer.getTime()
    
    # If time_in_task corresponds to the duration we set previously we end te task
    if time_in_task >= length_of_task:
        continueRoutine = False
        PVT_Trials.finished = True
    
    # the Routine "End_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 120.0 repeats of 'PVT_Trials'


# ------Prepare to start Routine "The_end"-------
continueRoutine = True
# update component parameters for each repeat
GoodbyeEnd.keys = []
GoodbyeEnd.rt = []
_GoodbyeEnd_allKeys = []
# keep track of which components have finished
The_endComponents = [Goodbye, GoodbyeEnd]
for thisComponent in The_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
The_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "The_end"-------
while continueRoutine:
    # get current time
    t = The_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=The_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Goodbye* updates
    if Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Goodbye.frameNStart = frameN  # exact frame index
        Goodbye.tStart = t  # local t and not account for scr refresh
        Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Goodbye, 'tStartRefresh')  # time at next scr refresh
        Goodbye.setAutoDraw(True)
    
    # *GoodbyeEnd* updates
    waitOnFlip = False
    if GoodbyeEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GoodbyeEnd.frameNStart = frameN  # exact frame index
        GoodbyeEnd.tStart = t  # local t and not account for scr refresh
        GoodbyeEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GoodbyeEnd, 'tStartRefresh')  # time at next scr refresh
        GoodbyeEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(GoodbyeEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(GoodbyeEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if GoodbyeEnd.status == STARTED and not waitOnFlip:
        theseKeys = GoodbyeEnd.getKeys(keyList=['space'], waitRelease=False)
        _GoodbyeEnd_allKeys.extend(theseKeys)
        if len(_GoodbyeEnd_allKeys):
            GoodbyeEnd.keys = _GoodbyeEnd_allKeys[-1].name  # just the last key pressed
            GoodbyeEnd.rt = _GoodbyeEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in The_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "The_end"-------
for thisComponent in The_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Goodbye.started', Goodbye.tStartRefresh)
thisExp.addData('Goodbye.stopped', Goodbye.tStopRefresh)
# check responses
if GoodbyeEnd.keys in ['', [], None]:  # No response was made
    GoodbyeEnd.keys = None
thisExp.addData('GoodbyeEnd.keys',GoodbyeEnd.keys)
if GoodbyeEnd.keys != None:  # we had a response
    thisExp.addData('GoodbyeEnd.rt', GoodbyeEnd.rt)
thisExp.addData('GoodbyeEnd.started', GoodbyeEnd.tStartRefresh)
thisExp.addData('GoodbyeEnd.stopped', GoodbyeEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "The_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(output_path+'.tsv', delim='\t')
thisExp.saveAsPickle(output_path)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
