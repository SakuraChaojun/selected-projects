/***************** 
 * Untitled Test *
 *****************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'untitled';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsStudyLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsStudyLoopBegin, trialsStudyLoopScheduler);
flowScheduler.add(trialsStudyLoopScheduler);
flowScheduler.add(trialsStudyLoopEnd);
flowScheduler.add(waithereRoutineBegin());
flowScheduler.add(waithereRoutineEachFrame());
flowScheduler.add(waithereRoutineEnd());
flowScheduler.add(Blank500RoutineBegin());
flowScheduler.add(Blank500RoutineEachFrame());
flowScheduler.add(Blank500RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionClock;
var weclomeText;
var key_welcome;
var Blank500Clock;
var polyback;
var textBlank500;
var trailClock;
var polygon_3;
var textstudy;
var waithereClock;
var textWait;
var key_respexit;
var TesttrailcontClock;
var polygon;
var textTesttrait;
var key_conf;
var textconfscale;
var EndClock;
var textEnd;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  weclomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'weclomeText',
    text: 'Welcome to our experiment\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_welcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  polyback = new visual.Rect ({
    win: psychoJS.window, name: 'polyback', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textBlank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank500',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trail"
  trailClock = new util.Clock();
  polygon_3 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_3', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textstudy = new visual.TextStim({
    win: psychoJS.window,
    name: 'textstudy',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  polyback = new visual.Rect ({
    win: psychoJS.window, name: 'polyback', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textBlank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank500',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "waithere"
  waithereClock = new util.Clock();
  textWait = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWait',
    text: 'Please wait \n\nready press space',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_respexit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  polyback = new visual.Rect ({
    win: psychoJS.window, name: 'polyback', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textBlank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank500',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Testtrailcont"
  TesttrailcontClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textTesttrait = new visual.TextStim({
    win: psychoJS.window,
    name: 'textTesttrait',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_conf = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  textconfscale = new visual.TextStim({
    win: psychoJS.window,
    name: 'textconfscale',
    text: '1...2...3...4...5...6\nNEW.............OLD',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Blank500"
  Blank500Clock = new util.Clock();
  polyback = new visual.Rect ({
    win: psychoJS.window, name: 'polyback', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  textBlank500 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank500',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thanks for participating ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_welcome_allKeys;
var instructionComponents;
function instructionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instruction'-------
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_welcome.keys = undefined;
    key_welcome.rt = undefined;
    _key_welcome_allKeys = [];
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(weclomeText);
    instructionComponents.push(key_welcome);
    
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instructionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instruction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *weclomeText* updates
    if (t >= 0.0 && weclomeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      weclomeText.tStart = t;  // (not accounting for frame time here)
      weclomeText.frameNStart = frameN;  // exact frame index
      
      weclomeText.setAutoDraw(true);
    }

    
    // *key_welcome* updates
    if (t >= 0.0 && key_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_welcome.tStart = t;  // (not accounting for frame time here)
      key_welcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_welcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_welcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_welcome.clearEvents(); });
    }

    if (key_welcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_welcome.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_welcome_allKeys = _key_welcome_allKeys.concat(theseKeys);
      if (_key_welcome_allKeys.length > 0) {
        key_welcome.keys = _key_welcome_allKeys[_key_welcome_allKeys.length - 1].name;  // just the last key pressed
        key_welcome.rt = _key_welcome_allKeys[_key_welcome_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instruction'-------
    instructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_welcome.keys', key_welcome.keys);
    if (typeof key_welcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_welcome.rt', key_welcome.rt);
        routineTimer.reset();
        }
    
    key_welcome.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Blank500Components;
function Blank500RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Blank500'-------
    t = 0;
    Blank500Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Blank500Components = [];
    Blank500Components.push(polyback);
    Blank500Components.push(textBlank500);
    
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function Blank500RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Blank500'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polyback* updates
    if (t >= 0.0 && polyback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polyback.tStart = t;  // (not accounting for frame time here)
      polyback.frameNStart = frameN;  // exact frame index
      
      polyback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polyback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polyback.setAutoDraw(false);
    }
    
    // *textBlank500* updates
    if (t >= 0.0 && textBlank500.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlank500.tStart = t;  // (not accounting for frame time here)
      textBlank500.frameNStart = frameN;  // exact frame index
      
      textBlank500.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textBlank500.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textBlank500.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Blank500Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Blank500RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Blank500'-------
    Blank500Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trialsStudy;
var currentLoop;
function trialsStudyLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsStudy = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'word.xlsx', '0:3'),
    seed: undefined, name: 'trialsStudy'
  });
  psychoJS.experiment.addLoop(trialsStudy); // add the loop to the experiment
  currentLoop = trialsStudy;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialsStudy.forEach(function() {
    const snapshot = trialsStudy.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trailRoutineBegin(snapshot));
    thisScheduler.add(trailRoutineEachFrame(snapshot));
    thisScheduler.add(trailRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsStudyLoopEnd() {
  psychoJS.experiment.removeLoop(trialsStudy);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'word.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(TesttrailcontRoutineBegin(snapshot));
    thisScheduler.add(TesttrailcontRoutineEachFrame(snapshot));
    thisScheduler.add(TesttrailcontRoutineEnd(snapshot));
    thisScheduler.add(Blank500RoutineBegin(snapshot));
    thisScheduler.add(Blank500RoutineEachFrame(snapshot));
    thisScheduler.add(Blank500RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trailComponents;
function trailRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trail'-------
    t = 0;
    trailClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.100000);
    // update component parameters for each repeat
    textstudy.setText(word);
    // keep track of which components have finished
    trailComponents = [];
    trailComponents.push(polygon_3);
    trailComponents.push(textstudy);
    
    trailComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trailRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trail'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trailClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_3* updates
    if (t >= 0.0 && polygon_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_3.tStart = t;  // (not accounting for frame time here)
      polygon_3.frameNStart = frameN;  // exact frame index
      
      polygon_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_3.setAutoDraw(false);
    }
    
    // *textstudy* updates
    if (t >= 0.0 && textstudy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textstudy.tStart = t;  // (not accounting for frame time here)
      textstudy.frameNStart = frameN;  // exact frame index
      
      textstudy.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textstudy.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textstudy.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trailComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trailRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trail'-------
    trailComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_respexit_allKeys;
var waithereComponents;
function waithereRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'waithere'-------
    t = 0;
    waithereClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_respexit.keys = undefined;
    key_respexit.rt = undefined;
    _key_respexit_allKeys = [];
    // keep track of which components have finished
    waithereComponents = [];
    waithereComponents.push(textWait);
    waithereComponents.push(key_respexit);
    
    waithereComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function waithereRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'waithere'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = waithereClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWait* updates
    if (t >= 0.0 && textWait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWait.tStart = t;  // (not accounting for frame time here)
      textWait.frameNStart = frameN;  // exact frame index
      
      textWait.setAutoDraw(true);
    }

    
    // *key_respexit* updates
    if (t >= 0.0 && key_respexit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respexit.tStart = t;  // (not accounting for frame time here)
      key_respexit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respexit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respexit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respexit.clearEvents(); });
    }

    if (key_respexit.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respexit.getKeys({keyList: ['space'], waitRelease: false});
      _key_respexit_allKeys = _key_respexit_allKeys.concat(theseKeys);
      if (_key_respexit_allKeys.length > 0) {
        key_respexit.keys = _key_respexit_allKeys[_key_respexit_allKeys.length - 1].name;  // just the last key pressed
        key_respexit.rt = _key_respexit_allKeys[_key_respexit_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    waithereComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function waithereRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'waithere'-------
    waithereComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_respexit.keys', key_respexit.keys);
    if (typeof key_respexit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respexit.rt', key_respexit.rt);
        routineTimer.reset();
        }
    
    key_respexit.stop();
    // the Routine "waithere" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_conf_allKeys;
var TesttrailcontComponents;
function TesttrailcontRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Testtrailcont'-------
    t = 0;
    TesttrailcontClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    textTesttrait.setText(word);
    key_conf.keys = undefined;
    key_conf.rt = undefined;
    _key_conf_allKeys = [];
    // keep track of which components have finished
    TesttrailcontComponents = [];
    TesttrailcontComponents.push(polygon);
    TesttrailcontComponents.push(textTesttrait);
    TesttrailcontComponents.push(key_conf);
    TesttrailcontComponents.push(textconfscale);
    
    TesttrailcontComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function TesttrailcontRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Testtrailcont'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TesttrailcontClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    
    // *textTesttrait* updates
    if (t >= 0.0 && textTesttrait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textTesttrait.tStart = t;  // (not accounting for frame time here)
      textTesttrait.frameNStart = frameN;  // exact frame index
      
      textTesttrait.setAutoDraw(true);
    }

    
    // *key_conf* updates
    if (t >= 0.0 && key_conf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_conf.tStart = t;  // (not accounting for frame time here)
      key_conf.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_conf.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_conf.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_conf.clearEvents(); });
    }

    if (key_conf.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_conf.getKeys({keyList: ['1', '2', '3', '4', '5', '6'], waitRelease: false});
      _key_conf_allKeys = _key_conf_allKeys.concat(theseKeys);
      if (_key_conf_allKeys.length > 0) {
        key_conf.keys = _key_conf_allKeys[_key_conf_allKeys.length - 1].name;  // just the last key pressed
        key_conf.rt = _key_conf_allKeys[_key_conf_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *textconfscale* updates
    if (t >= 0.0 && textconfscale.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textconfscale.tStart = t;  // (not accounting for frame time here)
      textconfscale.frameNStart = frameN;  // exact frame index
      
      textconfscale.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TesttrailcontComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TesttrailcontRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Testtrailcont'-------
    TesttrailcontComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_conf.keys', key_conf.keys);
    if (typeof key_conf.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_conf.rt', key_conf.rt);
        routineTimer.reset();
        }
    
    key_conf.stop();
    // the Routine "Testtrailcont" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndComponents;
function EndRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(textEnd);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function EndRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textEnd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textEnd.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
