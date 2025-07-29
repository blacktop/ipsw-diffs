## MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

-0.0.0.0.0
-  __TEXT.__text: 0x5ac08
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0xdc00
-  __TEXT.__objc_methlist: 0x5f6c
-  __TEXT.__const: 0x5d0
-  __TEXT.__objc_methname: 0x111c6
-  __TEXT.__cstring: 0x17ad
-  __TEXT.__objc_classname: 0xed7
-  __TEXT.__objc_methtype: 0x3e3d
-  __TEXT.__oslogstring: 0x16b3
+146.9.4.11.0
+  __TEXT.__text: 0x5b028
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_stubs: 0xdde0
+  __TEXT.__objc_methlist: 0x602c
+  __TEXT.__const: 0x5c0
+  __TEXT.__objc_methname: 0x116bf
+  __TEXT.__cstring: 0x1797
+  __TEXT.__objc_classname: 0xef2
+  __TEXT.__objc_methtype: 0x3e8e
+  __TEXT.__oslogstring: 0x18c5
   __TEXT.__gcc_except_tab: 0x29c
   __TEXT.__dlopen_cstrs: 0xa1
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x1634
+  __TEXT.__unwind_info: 0x1644
   __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe78
-  __DATA_CONST.__cfstring: 0x22a0
+  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__cfstring: 0x2260
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x6f8
+  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x17808
-  __DATA.__objc_selrefs: 0x4018
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x6d8
-  __DATA.__objc_superrefs: 0x250
-  __DATA.__objc_ivar: 0x67c
+  __DATA.__objc_const: 0x179a8
+  __DATA.__objc_selrefs: 0x40c0
+  __DATA.__objc_ivar: 0x684
   __DATA.__objc_data: 0x19f0
-  __DATA.__data: 0x16a8
+  __DATA.__data: 0x1708
   __DATA.__bss: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40CD30C9-440C-3CED-9A31-724756D39E85
-  Functions: 2171
-  Symbols:   442
-  CStrings:  4224
+  UUID: 0784E289-FFE9-3B23-ACA2-9D97DDDE9AC8
+  Functions: 2193
+  Symbols:   444
+  CStrings:  4268
 
Symbols:
+ _OBJC_CLASS_$_DefaultDateProvider
+ _OBJC_CLASS_$_MTLegacyStopwatchMigrator
+ _OBJC_CLASS_$_MTStopwatch
+ _OBJC_CLASS_$_MTStopwatchManager
+ _OBJC_CLASS_$_MTStopwatchViewModel
- _NSRunLoopCommonModes
- _OBJC_CLASS_$_CADisplayLink
- _arc4random_uniform
CStrings:
+ "\x011\x11\x1f\x05"
+ "%{public}@ couldn't fetch stopwatch, have to create one"
+ "%{public}@ didAddLap"
+ "%{public}@ didLapLapTimer"
+ "%{public}@ didPauseLapTimer"
+ "%{public}@ didPauseStopwatch"
+ "%{public}@ didResetLapTimer"
+ "%{public}@ didResumeLapTimer"
+ "%{public}@ didStartLapTimer"
+ "%{public}@ endDisplayUpdates"
+ "%{public}@ error fetching stopwatches: %{public}@"
+ "%{public}@ initialized"
+ "%{public}@ migration completed without error"
+ "%{public}@ migration encountered error: %{public}@"
+ "%{public}@ migration not needed, proceeding to load stopwatch"
+ "%{public}@ setting up view model with stopwatch: %{public}@"
+ "%{public}@ sleep schedule model did change"
+ "%{public}@ startDisplayUpdates"
+ "%{public}@ stopwatch need migration"
+ "%{public}@ view model already exists, updating with stopwatch: %{public}@"
+ "%{public}@ view model does not exist, creating new one with stopwatch: %{public}@"
+ "@\"MTLegacyStopwatchMigrator\""
+ "@\"MTStopwatchManager\""
+ "@\"MTStopwatchViewModel\""
+ "StopwatchViewModelDelegate"
+ "T@\"MTLegacyStopwatchMigrator\",&,N,V_migrator"
+ "T@\"MTStopwatchManager\",&,N,V_stopwatchManager"
+ "T@\"MTStopwatchViewModel\",&,N,V_viewModel"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "TKRingtones-EncoreInfinitum"
+ "_migrator"
+ "_stopwatchManager"
+ "_viewModel"
+ "didAddLap:"
+ "didClearAllLaps"
+ "didLapLapTimer"
+ "didPauseLapTimer"
+ "didPauseStopwatch"
+ "didResetLapTimer"
+ "didResumeLapTimer"
+ "didStartLapTimer"
+ "didUpdateCurrentInterval:adjustedCurrentInterval:totalInterval:adjustedTotalInterval:isStopwatchRunning:"
+ "endDisplayUpdates"
+ "eraseLocalDefaults"
+ "getStopwatch"
+ "getStopwatches"
+ "handleEnterForeground"
+ "initWithDefaults:manager:"
+ "initWithStopwatch:manager:delegate:dateProvider:registerForNotifications:broadcastUpdates:"
+ "invalidateDisplayLink"
+ "lapLapTimerUI"
+ "laps"
+ "migrateLegacyStopwatch"
+ "migrator"
+ "needsMigration"
+ "pauseLapTimerUI"
+ "reloadSleepSection"
+ "reloadStopwatchesWithCompletion:"
+ "renderViewModel"
+ "resetLapTimerUI"
+ "resumeLapTimerUI"
+ "setMigrator:"
+ "setStopwatchManager:"
+ "setViewModel:"
+ "setupViewModelWithStopwatch:"
+ "shouldProcessUpdate"
+ "sleepScheduleModelDidChange"
+ "sleepStore:sleepScheduleModelDidChange:"
+ "startDisplayUpdates"
+ "stopwatchManager"
+ "updateStopwatch:"
+ "updateWithDisplayLink"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v52@0:8d16d24d32d40B48"
+ "viewModel"
- "\x021\x11\x1f\x02"
- "%{public}@ adding lap"
- "%{public}@ clearing all laps"
- "%{public}@ didLapStopwatchWithProvider"
- "%{public}@ didResetStopwatchWithProvider"
- "%{public}@ didStartStopwatchWithProvider"
- "%{public}@ didStopStopwatchWithProvider"
- "%{public}@ sleep schedule did change"
- "%{public}@ starting timer"
- "%{public}@ stopping timer"
- "@\"CADisplayLink\""
- "LAP_STOPWATCH_QUICK_ACTION_TITLE"
- "RESET_STOPWATCH_QUICK_ACTION_TITLE"
- "T@\"UIWindow\",&,N"
- "TKRingtones"
- "_addLap:"
- "_clearAllLaps"
- "_displayLink"
- "_startTimer"
- "_stopTimer"
- "_tick:"
- "_timeAdjustedFor30fpsDisplay:"
- "addToRunLoop:forMode:"
- "boolForKey:"
- "displayLinkWithTarget:selector:"
- "performActionForShortcutAction:withActionTitle:"
- "setBool:forKey:"
- "setFrameInterval:"
- "sleepScheduleDidChange"
- "timeIntervalSinceNow"

```
