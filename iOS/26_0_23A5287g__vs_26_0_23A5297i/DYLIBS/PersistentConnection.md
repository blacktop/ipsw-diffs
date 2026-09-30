## PersistentConnection

> `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`

```diff

 557.100.1.0.0
-  __TEXT.__text: 0x23b1c
+  __TEXT.__text: 0x234a4
   __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x1fa8
   __TEXT.__const: 0x250
   __TEXT.__gcc_except_tab: 0xf10
-  __TEXT.__cstring: 0x1b8e
-  __TEXT.__oslogstring: 0x4b89
+  __TEXT.__cstring: 0x1aa0
+  __TEXT.__oslogstring: 0x4823
   __TEXT.__unwind_info: 0xc10
   __TEXT.__objc_classname: 0x321
   __TEXT.__objc_methname: 0x49fe

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5052317-AD7B-34DB-96CD-55737F42DA05
-  Functions: 769
-  Symbols:   3005
-  CStrings:  1690
+  UUID: 80634EDB-EE51-3ED8-B1E7-E09F6A60F2D5
+  Functions: 799
+  Symbols:   3065
+  CStrings:  1680
 
Symbols:
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __NSDate_alloc_initWithTimeIntervalSinceNow.cold.1
+ _countOfGrowthActions.cold.1
+ _currentKeepAliveInterval.cold.1
+ _growthStage.cold.1
+ _isServerOriginatedKeepAlive.cold.1
+ _lastSuccessfulKeepAliveInterval.cold.1
+ _minimumIntervalFallbackEnabled.cold.1
+ _minimumIntervalFallbackStateTimeout.cold.1
+ _previousAction.cold.1
+ _serverStatsExpectedKeepAliveInterval.cold.1
+ _serverStatsMaxKeepAliveInterval.cold.1
+ _serverStatsMinKeepAliveInterval.cold.1
+ _setIsServerOriginatedKeepAlive.cold.1
+ _setMinimumIntervalFallbackStateTimeout.cold.1
+ _setServerStatsExpectedKeepAliveInterval.cold.1
+ _setServerStatsMaxKeepAliveInterval.cold.1
+ _setServerStatsMinKeepAliveInterval.cold.1
+ _setUsingServerStatsAggressively.cold.1
+ _usingServerStatsAggressively.cold.1
CStrings:
+ "%s:   - forcing RefinedShrink (%lld <= %g)"
+ "%s: Initialized with keepAliveInterval %g inInitialGrowth %s"
+ "%s: Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
+ "%s: Shrinking %g by %g"
+ "%s: Unexpected _leaveMinimumIntervalFallbackStateDate %llu in MinimumIntervalFallbackState, changing to %llu"
+ "%s: _leaveMinimumIntervalFallbackStateDate is nil. Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
+ "%s: adjustGrowthAlgorithmMode. {lastMode: %s, currentMode: %s}"
+ "%s: after previous MinimumIntervalFallbackState ends, extend leaveMinimumIntervalFallbackStateDate to %llu"
+ "%s: leaveMinimumFallbackStateDate passed, acting"
+ "%s: leaving the initial growth stage for refined growth"
+ "%s: leaving the steady state and trying to grow again"
+ "%s: minimumIntervalFallbackEnabled changed to %s"
+ "%s: moved into Steady State - %g - %g <= %g"
+ "%s: no signal avoidance {interval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g}"
+ "%s: override interval %g"
+ "%s: override max interval %g"
+ "%s: override min interval %g"
+ "%s: received action %s while in stage %s"
+ "%s: resetAlgorithmToInterval: %g state: %s"
+ "%s: set the steady state expiration date to %llu"
+ "%s: setCurrentKeepAlive with interval %g varianceMode %u allowRoundup %s"
+ "%s: setting current interval to %g seconds"
+ "%s: setting lastSuccessfulKeepAliveInterval to %g seconds"
+ "%s: signalAvoidanceRange contained, increasing %s, end %g"
+ "%s: surpassed where the previous initial growth stopped at %g; reverting to initial growth."
+ "%s: triggered signaling avoidance {interval: %g, adjustedInterval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g, roundUpRatio: %g}"
+ "%s: useIntervalIfImprovement %g   lastKeepAliveInterval: %g  currentKeepAliveInterval: %g"
+ "%s: using a steady state timeout of %g for current interval %g"
+ "%s: using double the current interval for the steady state timer interval since we are significantly below the high watermark of %g seconds"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s:   - forcing RefinedShrink (%lld <= %g)"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Initialized with keepAliveInterval %g inInitialGrowth %s"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Shrinking %g by %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Unexpected _leaveMinimumIntervalFallbackStateDate %llu in MinimumIntervalFallbackState, changing to %llu"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: _leaveMinimumIntervalFallbackStateDate is nil. Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: adjustGrowthAlgorithmMode. {lastMode: %s, currentMode: %s}"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: after previous MinimumIntervalFallbackState ends, extend leaveMinimumIntervalFallbackStateDate to %llu"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaveMinimumFallbackStateDate passed, acting"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaving the initial growth stage for refined growth"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaving the steady state and trying to grow again"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: minimumIntervalFallbackEnabled changed to %s"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: moved into Steady State - %g - %g <= %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: no signal avoidance {interval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g}"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override interval %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override max interval %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override min interval %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: received action %s while in stage %s"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: resetAlgorithmToInterval: %g state: %s"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: set the steady state expiration date to %llu"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setCurrentKeepAlive with interval %g varianceMode %u allowRoundup %s"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setting current interval to %g seconds"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setting lastSuccessfulKeepAliveInterval to %g seconds"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: signalAvoidanceRange contained, increasing %s, end %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: surpassed where the previous initial growth stopped at %g; reverting to initial growth."
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: triggered signaling avoidance {interval: %g, adjustedInterval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g, roundUpRatio: %g}"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: useIntervalIfImprovement %g   lastKeepAliveInterval: %g  currentKeepAliveInterval: %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: using a steady state timeout of %g for current interval %g"
- "[%15s:%-4d| %-30s] PCMSGA(%p) %s: using double the current interval for the steady state timer interval since we are significantly below the high watermark of %g seconds"
- "_processInitialGrowthAction"
- "_processRefinedGrowthAction"
- "_processRefinedShrinkAction"
- "_resetAlgorithmToInterval"
- "_setCurrentKeepAliveInterval"
- "initWith"
- "processNextAction"
- "useIntervalIfImprovement"

```
