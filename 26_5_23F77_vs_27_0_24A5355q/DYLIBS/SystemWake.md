## SystemWake

> `/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake`

```diff

-732.1.1.0.0
-  __TEXT.__text: 0xc128
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x8ac
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x1318
-  __TEXT.__cstring: 0xae7
-  __TEXT.__oslogstring: 0x1622
-  __TEXT.__unwind_info: 0x580
-  __TEXT.__objc_classname: 0x2ab
-  __TEXT.__objc_methname: 0x14bf
-  __TEXT.__objc_methtype: 0x5e5
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x108
+821.0.0.0.0
+  __TEXT.__text: 0xb81c
+  __TEXT.__objc_methlist: 0x8b4
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x10a8
+  __TEXT.__cstring: 0xb39
+  __TEXT.__oslogstring: 0x18dc
+  __TEXT.__unwind_info: 0x588
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x1978
-  __DATA.__objc_ivar: 0x138
+  __AUTH_CONST.__cfstring: 0xae0
+  __AUTH_CONST.__objc_const: 0x19a8
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x58

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF1EC45F-AD1F-3502-96A1-41BDCFE07200
-  Functions: 172
-  Symbols:   920
-  CStrings:  583
+  UUID: 2CE439E3-6A3A-33BE-AF87-B2B1EA990F84
+  Functions: 173
+  Symbols:   923
+  CStrings:  266
 
Symbols:
+ -[SWSystemSleepMonitor _lock_setSleepStateAbortingSleepForSystemActivity]
+ -[SWSystemSleepMonitor areAssertionsIgnoredToForceSleep]
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table76
+ _OBJC_IVAR_$_SWSystemSleepMonitor._lock_assertionsIgnoredToForceSleep
+ __OBJC_$_PROP_LIST_SWSystemActivityAcquisitionDetails.197
+ ___57-[SWSystemSleepMonitor sleepRequestedWithNotificationID:]_block_invoke.57
+ ___57-[SWSystemSleepMonitor sleepRequestedWithNotificationID:]_block_invoke.60
+ ___58-[SWSystemSleepMonitor prepareForSleepWithNotificationID:]_block_invoke.64
+ ___58-[SWSystemSleepMonitor prepareForSleepWithNotificationID:]_block_invoke.65
+ ___76-[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:]_block_invoke.69
+ ___76-[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:]_block_invoke.77
+ ___block_literal_global.267
+ ___block_literal_global.80
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- -[SWSystemSleepMonitor _lock_setSleepSlateAbortingSleepForSystemActivity]
- GCC_except_table22
- GCC_except_table26
- GCC_except_table32
- GCC_except_table36
- GCC_except_table42
- GCC_except_table46
- GCC_except_table47
- GCC_except_table52
- GCC_except_table63
- GCC_except_table69
- GCC_except_table71
- GCC_except_table74
- __OBJC_$_PROP_LIST_SWSystemActivityAcquisitionDetails.198
- ___57-[SWSystemSleepMonitor sleepRequestedWithNotificationID:]_block_invoke.52
- ___57-[SWSystemSleepMonitor sleepRequestedWithNotificationID:]_block_invoke.55
- ___58-[SWSystemSleepMonitor prepareForSleepWithNotificationID:]_block_invoke.59
- ___58-[SWSystemSleepMonitor prepareForSleepWithNotificationID:]_block_invoke.60
- ___76-[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:]_block_invoke.64
- ___76-[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:]_block_invoke.72
- ___block_literal_global.259
- ___block_literal_global.75
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%p assertionsIgnoredToForceSleep->%{BOOL}u state:%{public}@->:%{public}@ elapsed:%.3lfs phase:%{public}@(%u) elapsedPhase:%.3lfs systemActivityAborting:%{public}@->%{public}@"
+ "%p ignored\u00a0request to update to state:%{public}@ forID:%ld elapsed:%.3lfs – currentState:%{public}@ elapsed:%.3lfs currentID:%ld systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p obsolete\u00a0request to update to state:%{public}@ forID:%ld elapsed:%.3lfs – currentState:%{public}@ elapsed:%.3lfs currentID:%ld systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p stale request to update to state:%{public}@ forID:%ld elapsed:%.3lfs – currentState:%{public}@ elapsed:%.3lfs currentID:%ld systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p state:%{public}@->%{public}@ elapsed:%.3lfs(%.3lfs) systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p systemActivity++=1 state:%{public}@ elapsed:%.3lfs phase:%{public}@(%u) elapsedPhase:%.3lfs systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p systemActivity--=0 state:%{public}@ elapsed:%.3lfs phase:%{public}@(%u) elapsedPhase:%.3lfs systemActivityAborting:%{public}@->%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld systemActivityAborting:%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld systemActivityAborting:%{public}@->%{public}@ assertionsIgnoredToForceSleep:%{BOOL}u"
+ "sleep was requested when setAssertionsIgnoredToForceSleep:YES"
- "#16@0:8"
- "%p (zero active system activities) state:%{public}@ elapsed:%.3lfs phase:%{public}@(%u) elapsedPhase:%.3lfs systemActivityAborting:%{public}@->%{public}@"
- "%p obsolete\u00a0request to update to state:%{public}@ forID:%ld elapsed:%.3lfs – currentState:%{public}@ elapsed:%.3lfs currentID:%ld systemActivityAborting:%{public}@"
- "%p stale request to update to state:%{public}@ forID:%ld elapsed:%.3lfs – currentState:%{public}@ elapsed:%.3lfs currentID:%ld systemActivityAborting:%{public}@"
- "%p state:%{public}@ elapsed:%.3lfs phase:%{public}@(%u) elapsedPhase:%.3lfs systemActivityAborting:%{public}@"
- "%p state:%{public}@->%{public}@ elapsed:%.3lfs(%.3lfs) systemActivityAborting:%{public}@"
- "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld"
- "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld systemActivityAborting:%{public}@"
- "%p systemPowerChanged:%{public}@(%u) previous:%{public}@(%u) elapsedPhase:%.3lfs state:%{public}@->%{public}@ elapsedState:%.3lfs notificationID:%ld systemActivityAborting:%{public}@->%{public}@"
- ".cxx_destruct"
- "@\"<BSInvalidatable>\""
- "@\"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>\""
- "@\"<SWSystemActivityProviding>\""
- "@\"<SWSystemSleepAssertionProviding>\""
- "@\"<SWSystemSleepMonitorProviding>\""
- "@\"BSAbsoluteMachTimer\""
- "@\"BSAbsoluteMachTimer\"24@0:8@\"NSString\"16"
- "@\"BSZeroingWeakReference\""
- "@\"NSDate\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SWActiveSystemActivityRegistry\""
- "@\"SWDeclareSystemActivityResult\"24@0:8@\"NSString\"16"
- "@\"SWPreventSystemSleepAssertion\"24@0:8@\"NSString\"16"
- "@\"SWScheduledSystemWake\""
- "@\"SWSystemActivityAssertion\"24@0:8@\"NSString\"16"
- "@\"SWSystemSleepMonitor\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8B16B20B24"
- "@28@0:8i16I20i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8Q16Q24Q32Q40"
- "@60@0:8@16@24B32@36@44@52"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BSCancellable"
- "BSInvalidatable"
- "BSTimerScheduleQuerying"
- "I"
- "I16@0:8"
- "NSObject"
- "Q"
- "Q16@0:8"
- "SWActiveSystemActivityRegistryObserving"
- "SWDeclareSystemActivityResult"
- "SWPreventSystemSleepAssertion"
- "SWScheduledSystemWake"
- "SWSystemActivityAcquisitionDetails"
- "SWSystemActivityAssertion"
- "SWSystemActivityAssertionConfiguring"
- "SWSystemActivityAssertionConfiguring_Internal"
- "SWSystemActivityProvider"
- "SWSystemActivityProviding"
- "SWSystemSleepAssertionProvider"
- "SWSystemSleepAssertionProviding"
- "SWSystemSleepMonitorAggregateState"
- "SWSystemSleepMonitorProvider"
- "SWSystemSleepMonitorProviding"
- "SWSystemSleepMonitorProvidingDelegate"
- "SWSystemSleepObserver"
- "SWWakingTimer"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"SWSystemSleepMonitorAggregateState\",R"
- "TB,R,GhasSleepBeenRequested"
- "TB,R,GisAwakeOrAbortingSleep"
- "TB,R,GisSleepImminent"
- "TB,R,N"
- "TB,R,N,GisActive"
- "TB,R,N,GisScheduled"
- "TB,R,N,V_afterFailingToRevertPendingSleep"
- "TB,R,N,V_afterPendingSleepWasAlreadyInitiated"
- "TB,R,N,V_afterSleepOfNonZeroDuration"
- "TI,R,N,V_assertionID"
- "TQ,R"
- "TQ,R,V_powerManagementPhase"
- "TQ,R,V_powerManagementPhaseTimestamp"
- "TQ,R,V_sleepMonitorState"
- "TQ,R,V_sleepMonitorStateTimestamp"
- "Td,R,N"
- "Ti,R,N,V_returnValue"
- "Ti,R,N,V_systemState"
- "Tq,R,N"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{IONotificationPort=}"
- "^{_NSZone=}16@0:8"
- "_acquireWaitsToAbortSleepImminent"
- "_acquireWaitsToAbortSleepRequested"
- "_activeSystemActivityRegistry"
- "_afterFailingToRevertPendingSleep"
- "_afterPendingSleepWasAlreadyInitiated"
- "_afterSleepOfNonZeroDuration"
- "_assertionID"
- "_identifier"
- "_initializing"
- "_invalidated"
- "_lock"
- "_lock_acquisitionHandler"
- "_lock_activeSystemActivities"
- "_lock_activeSystemActivitiesCount"
- "_lock_assertionID"
- "_lock_clientDidInvalidate"
- "_lock_didFailToRevertPendingSleep"
- "_lock_handler"
- "_lock_leeway"
- "_lock_messageID"
- "_lock_observers"
- "_lock_powerManagementNotificationID"
- "_lock_powerManagementPhase"
- "_lock_queue"
- "_lock_registered"
- "_lock_startKernelAPWakeTime"
- "_lock_state"
- "_lock_stateTimestamp"
- "_lock_systemActivitiesAreActive"
- "_lock_systemActivityAbortSleepPhase"
- "_lock_systemPowerConnection"
- "_lock_systemPowerNotifier"
- "_lock_systemPowerPort"
- "_lock_timeout"
- "_lock_timeoutTime"
- "_lock_timeoutTimer"
- "_lock_timer"
- "_lock_wakeDate"
- "_lock_wakeIdentifier"
- "_lock_wasSleepImminent"
- "_lock_weakDelegateWrapper"
- "_monitorProvider"
- "_powerManagementPhase"
- "_powerManagementPhaseTimestamp"
- "_preventSleepAssertion"
- "_provider"
- "_queue"
- "_queue_declareSystemActivity"
- "_returnValue"
- "_scheduledWake"
- "_sleepAssertionProvider"
- "_sleepMonitor"
- "_sleepMonitorState"
- "_sleepMonitorStateTimestamp"
- "_stateCaptureHandler"
- "_systemState"
- "acquirePreventSystemSleepAssertionWithIdentifier:"
- "acquireSystemActivityAssertionWithIdentifier:"
- "acquireWithTimeout:handler:"
- "active"
- "addObject:"
- "addObserver:"
- "aggregateState"
- "allObjects"
- "allowPowerChange:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCollection:withName:itemBlock:"
- "appendInt:withName:"
- "appendObject:withName:"
- "appendProem:block:"
- "appendString:withName:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUnsignedInt:withName:"
- "appendUnsignedInteger:withName:"
- "autorelease"
- "awakeOrAbortingSleep"
- "boolValue"
- "build"
- "builderWithObject:"
- "cancel"
- "cancelPowerChange:"
- "cancelWake"
- "class"
- "conformsToProtocol:"
- "context"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "createTimerWithIdentifier:"
- "d"
- "d16@0:8"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "declareSystemActivityWithName:"
- "description"
- "descriptionForTimestamp:"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "formatDateAsLongYMDHMSZPosixLocaleWithDate:"
- "formatDuration:"
- "getMachContinuousKernelWakeTime"
- "hasSleepBeenRequested"
- "hash"
- "hashTableWithOptions:"
- "i"
- "i16@0:8"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithAfterPendingSleepWasAlreadyInitiated:afterFailingToRevertPendingSleep:afterSleepOfNonZeroDuration:"
- "initWithIdentifier:"
- "initWithIdentifier:configurator:"
- "initWithIdentifier:forReason:invalidationBlock:"
- "initWithIdentifier:internalConfigurator:"
- "initWithIdentifier:queue:"
- "initWithIdentifier:queue:allowsInvalidation:monitorProvider:sleepAssertionProvider:activeSystemActivityRegistry:"
- "initWithIdentifier:sleepMonitor:sleepAssertionProvider:"
- "initWithReturnValue:assertionID:systemState:"
- "initWithSleepMonitorState:stateTimestamp:powerManagementPhase:phaseTimestamp:"
- "invalidate"
- "invalidateWithReason:"
- "isActive"
- "isAwakeOrAbortingSleep"
- "isComplete"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isScheduled"
- "isSleepImminent"
- "monitorUsingMainQueue"
- "numberWithDouble:"
- "numberWithInteger:"
- "object"
- "objectsAtIndexes:"
- "observersOfSelector:performObserverBlock:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "powerManagementPhase"
- "powerManagementPhaseTimestamp"
- "q"
- "q16@0:8"
- "referenceWithObject:"
- "registerActiveSystemActivity:"
- "registerForSystemPowerOnQueue:withDelegate:"
- "release"
- "releaseAssertionID:"
- "removeObject:"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scheduleForDate:leewayInterval:queue:handler:"
- "scheduleWake:leeway:"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "scheduled"
- "self"
- "sentinelWithQueue:signalCount:signalHandler:"
- "setAcquireWaitsToAbortSleepImminent:"
- "setAcquireWaitsToAbortSleepRequested:"
- "setSleepMonitor:"
- "setSleepSlate:powerManagementPhase:notificationID:"
- "setSystemActivityProvider:"
- "sharedHighPriorityQueue"
- "sharedInstance"
- "sharedProvider"
- "sharedRegistry"
- "signal"
- "signalWithContext:"
- "sleepMonitorState"
- "sleepMonitorStateTimestamp"
- "sleepRequested"
- "stringWithFormat:"
- "superclass"
- "systemActivityRegistryCountDidDecrementToZero:"
- "systemActivityRegistryCountDidIncrementToOne:"
- "systemPowerChanged:notificationID:"
- "systemSleepMonitor:prepareForSleepWithCompletion:"
- "systemSleepMonitor:sleepRequestedWithResult:"
- "systemSleepMonitorDidWakeFromSleep:"
- "systemSleepMonitorSleepRequestAborted:"
- "systemSleepMonitorWillWakeFromSleep:"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "unregisterInactiveSystemActivity:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"<SWSystemActivityProviding>\"16"
- "v24@0:8@\"SWActiveSystemActivityRegistry\"16"
- "v24@0:8@\"SWSystemSleepMonitor\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8I16^v20"
- "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@\"<SWSystemSleepMonitorProvidingDelegate>\"24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<@\"SWPreventSystemSleepAssertion\"@?B@\"NSString\">24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<v@?>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8d16@?24"
- "v32@0:8d16q24"
- "v48@0:8@16d24@32@?40"
- "v48@0:8d16d24@32@?40"
- "wakeTime"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
