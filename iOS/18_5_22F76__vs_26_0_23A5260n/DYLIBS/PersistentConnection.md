## PersistentConnection

> `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`

```diff

-547.100.21.0.0
-  __TEXT.__text: 0x1dcf4
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x1d58
-  __TEXT.__const: 0x1e0
+556.100.1.0.0
+  __TEXT.__text: 0x23988
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x1fa8
+  __TEXT.__const: 0x250
   __TEXT.__gcc_except_tab: 0xe60
-  __TEXT.__cstring: 0x168f
-  __TEXT.__oslogstring: 0x3d32
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__objc_classname: 0x2fb
-  __TEXT.__objc_methname: 0x47f5
-  __TEXT.__objc_methtype: 0xc5a
-  __TEXT.__objc_stubs: 0x3180
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__cstring: 0x1b8e
+  __TEXT.__oslogstring: 0x4b5f
+  __TEXT.__unwind_info: 0xb90
+  __TEXT.__objc_classname: 0x321
+  __TEXT.__objc_methname: 0x49ec
+  __TEXT.__objc_methtype: 0x1071
+  __TEXT.__objc_stubs: 0x3200
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x6a0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1040
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x630
+  __DATA_CONST.__objc_selrefs: 0x1098
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x660
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0x1640
-  __AUTH_CONST.__objc_const: 0x6470
-  __DATA.__objc_ivar: 0x358
-  __DATA.__data: 0x468
+  __AUTH_CONST.__objc_const: 0x6e88
+  __AUTH.__data: 0xf8
+  __DATA.__objc_ivar: 0x360
+  __DATA.__data: 0x4c8
   __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB8ADE7C-7C26-331F-A444-28FB0D9A7D6F
-  Functions: 683
-  Symbols:   2762
-  CStrings:  1570
+  UUID: A8EAFC94-5241-3ED1-B8FA-1DC0151E13E5
+  Functions: 769
+  Symbols:   2999
+  CStrings:  1689
 
Symbols:
+ +[PCConnectionManager stringForAddressFamily:]
+ +[PCInterfaceMonitor isPathUltraConstrained:]
+ +[PCInterfaceUsabilityMonitor isPathUltraConstrained:]
+ +[PCSharedMultiStageGrowthAlgorithm _loadDefaultValue:forKey:]
+ +[PCSharedMultiStageGrowthAlgorithm _loadDefaults]
+ -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]
+ -[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:].cold.1
+ -[PCConnectionManager currentCacheDictonary]
+ -[PCConnectionManager resetKeepAliveStateMachineIfNecessary]
+ -[PCConnectionManager saveKeepAliveInterval:isInitialGrowth:]
+ -[PCSharedMultiStageGrowthAlgorithm .cxx_destruct]
+ -[PCSharedMultiStageGrowthAlgorithm _resetAlgorithmToInterval:stage:]
+ -[PCSharedMultiStageGrowthAlgorithm _stringForAction:]
+ -[PCSharedMultiStageGrowthAlgorithm _stringForMode:]
+ -[PCSharedMultiStageGrowthAlgorithm _stringForStage:]
+ -[PCSharedMultiStageGrowthAlgorithm cacheInfo]
+ -[PCSharedMultiStageGrowthAlgorithm countOfGrowthActions]
+ -[PCSharedMultiStageGrowthAlgorithm currentKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm description]
+ -[PCSharedMultiStageGrowthAlgorithm growthStage]
+ -[PCSharedMultiStageGrowthAlgorithm growthState]
+ -[PCSharedMultiStageGrowthAlgorithm initWithCacheInfo:loggingIdentifier:algorithmName:]
+ -[PCSharedMultiStageGrowthAlgorithm isServerOriginatedKeepAlive]
+ -[PCSharedMultiStageGrowthAlgorithm lastSuccessfulKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm logObject]
+ -[PCSharedMultiStageGrowthAlgorithm maximumKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm minimumIntervalFallbackEnabled]
+ -[PCSharedMultiStageGrowthAlgorithm minimumIntervalFallbackStateTimeout]
+ -[PCSharedMultiStageGrowthAlgorithm minimumKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm previousAction]
+ -[PCSharedMultiStageGrowthAlgorithm processNextAction:]
+ -[PCSharedMultiStageGrowthAlgorithm serverStatsExpectedKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm serverStatsMaxKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm serverStatsMinKeepAliveInterval]
+ -[PCSharedMultiStageGrowthAlgorithm setIsServerOriginatedKeepAlive:]
+ -[PCSharedMultiStageGrowthAlgorithm setLastSuccessfulKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setMaximumKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setMinimumIntervalFallbackEnabled:]
+ -[PCSharedMultiStageGrowthAlgorithm setMinimumIntervalFallbackStateTimeout:]
+ -[PCSharedMultiStageGrowthAlgorithm setMinimumKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setServerStatsExpectedKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setServerStatsMaxKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setServerStatsMinKeepAliveInterval:]
+ -[PCSharedMultiStageGrowthAlgorithm setSignalAvoidanceRange:]
+ -[PCSharedMultiStageGrowthAlgorithm setUnderlyingAlgorithm:]
+ -[PCSharedMultiStageGrowthAlgorithm setUsingServerStatsAggressively:]
+ -[PCSharedMultiStageGrowthAlgorithm signalAvoidanceRange]
+ -[PCSharedMultiStageGrowthAlgorithm underlyingAlgorithm]
+ -[PCSharedMultiStageGrowthAlgorithm useIntervalIfImprovement:]
+ -[PCSharedMultiStageGrowthAlgorithm usingServerStatsAggressively]
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table68
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table97
+ _NO
+ _OBJC_CLASS_$_CTDataConnectionAgentData
+ _OBJC_CLASS_$_PCSharedMultiStageGrowthAlgorithm
+ _OBJC_IVAR_$_PCSharedMultiStageGrowthAlgorithm._logObject
+ _OBJC_IVAR_$_PCSharedMultiStageGrowthAlgorithm._underlyingAlgorithm
+ _OBJC_METACLASS_$_PCSharedMultiStageGrowthAlgorithm
+ _PCMSGA__resetAlgorithmToInterval
+ _PCMSGA_countOfGrowthActions
+ _PCMSGA_currentKeepAliveInterval
+ _PCMSGA_globals
+ _PCMSGA_growthStage
+ _PCMSGA_initWith
+ _PCMSGA_isServerOriginatedKeepAlive
+ _PCMSGA_lastSuccessfulKeepAliveInterval
+ _PCMSGA_maximumKeepAliveInterval
+ _PCMSGA_minimumIntervalFallbackEnabled
+ _PCMSGA_minimumIntervalFallbackStateTimeout
+ _PCMSGA_minimumKeepAliveInterval
+ _PCMSGA_previousAction
+ _PCMSGA_processNextAction
+ _PCMSGA_serverStatsExpectedKeepAliveInterval
+ _PCMSGA_serverStatsMaxKeepAliveInterval
+ _PCMSGA_serverStatsMinKeepAliveInterval
+ _PCMSGA_setIsServerOriginatedKeepAlive
+ _PCMSGA_setLastSuccessfulKeepAliveInterval
+ _PCMSGA_setMaximumKeepAliveInterval
+ _PCMSGA_setMinimumIntervalFallbackEnabled
+ _PCMSGA_setMinimumIntervalFallbackStateTimeout
+ _PCMSGA_setMinimumKeepAliveInterval
+ _PCMSGA_setServerStatsExpectedKeepAliveInterval
+ _PCMSGA_setServerStatsMaxKeepAliveInterval
+ _PCMSGA_setServerStatsMinKeepAliveInterval
+ _PCMSGA_setSignalAvoidanceRange
+ _PCMSGA_setUsingServerStatsAggressively
+ _PCMSGA_signalAvoidanceRange
+ _PCMSGA_useIntervalIfImprovement
+ _PCMSGA_usingServerStatsAggressively
+ _YES
+ __NSDate_alloc_initWithTimeIntervalSinceNow
+ __NSDate_timeIntervalSinceNow
+ __OBJC_$_CLASS_METHODS_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_$_INSTANCE_METHODS_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_$_INSTANCE_VARIABLES_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_$_PROP_LIST_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_CLASS_PROTOCOLS_$_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_CLASS_RO_$_PCSharedMultiStageGrowthAlgorithm
+ __OBJC_METACLASS_RO_$_PCSharedMultiStageGrowthAlgorithm
+ ___50+[PCSharedMultiStageGrowthAlgorithm _loadDefaults]_block_invoke
+ ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke
+ ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke_2
+ ___58-[PCConnectionManager _saveWWANKeepAliveIntervalWithInfo:]_block_invoke_2.cold.1
+ ___assert_rtn
+ ___block_literal_global.176
+ __fallbackToLastSuccessfulKeepAliveInterval
+ __resetAlgorithmToInterval
+ __saveWWANKeepAliveIntervalWithInfo:.pred
+ __saveWWANKeepAliveIntervalWithInfo:.queue
+ __setCurrentKeepAliveInterval
+ __steadyStateTimeout
+ __stringForStage
+ _countOfGrowthActions
+ _currentKeepAliveInterval
+ _free
+ _growthStage
+ _initWith
+ _isServerOriginatedKeepAlive
+ _lastSuccessfulKeepAliveInterval
+ _malloc_type_malloc
+ _maximumKeepAliveInterval
+ _memcpy
+ _minimumIntervalFallbackEnabled
+ _minimumIntervalFallbackStateTimeout
+ _minimumKeepAliveInterval
+ _nil
+ _objc_msgSend$_saveWWANKeepAliveIntervalWithInfo:
+ _objc_msgSend$dataPlanTier
+ _objc_msgSend$initAgentDataFromInternetPath:
+ _objc_msgSend$isPathUltraConstrained:
+ _objc_msgSend$stringForAddressFamily:
+ _previousAction
+ _processNextAction
+ _serverStatsExpectedKeepAliveInterval
+ _serverStatsMaxKeepAliveInterval
+ _serverStatsMinKeepAliveInterval
+ _setIsServerOriginatedKeepAlive
+ _setLastSuccessfulKeepAliveInterval
+ _setMaximumKeepAliveInterval
+ _setMaximumKeepAliveInterval.cold.1
+ _setMinimumIntervalFallbackEnabled
+ _setMinimumIntervalFallbackStateTimeout
+ _setMinimumKeepAliveInterval
+ _setServerStatsExpectedKeepAliveInterval
+ _setServerStatsMaxKeepAliveInterval
+ _setServerStatsMinKeepAliveInterval
+ _setSignalAvoidanceRange
+ _setUsingServerStatsAggressively
+ _signalAvoidanceRange
+ _strlen
+ _time
+ _useIntervalIfImprovement
+ _usingServerStatsAggressively
- -[PCConnectionManager _saveWWANKeepAliveInterval].cold.1
- -[PCConnectionManager _stringForAddressFamily:]
- GCC_except_table36
- GCC_except_table56
- GCC_except_table59
- GCC_except_table60
- GCC_except_table64
- GCC_except_table75
- GCC_except_table76
- GCC_except_table83
- GCC_except_table84
- GCC_except_table94
- ___49-[PCConnectionManager _saveWWANKeepAliveInterval]_block_invoke
- ___49-[PCConnectionManager _saveWWANKeepAliveInterval]_block_invoke_2
- ___49-[PCConnectionManager _saveWWANKeepAliveInterval]_block_invoke_2.cold.1
- ___block_literal_global.169
- __saveWWANKeepAliveInterval.pred
- __saveWWANKeepAliveInterval.queue
- _objc_msgSend$_stringForAddressFamily:
CStrings:
+ " %g+%llu => %llu"
+ "%s(%p) returns  %d"
+ "%s(%p) returns  %g"
+ "%s(%p) returns %d"
+ "%s(%p) returns %llu"
+ "%s(%p) returns {%g,%g}"
+ "%s(%p, %d)"
+ "%s(%p, %g)"
+ "%s(%p, {%g,%g})"
+ "%s():%d | %s(%g) malloc %p"
+ "%s():%d | %s(%p) %llu - %llu = %llu"
+ "%{public}@ InterfaceUsabilityMonitor [%{public}@]: Interface constraint changed. Old constraint: %ld; New constraint: %ld;"
+ "%{public}@ InterfaceUsabilityMonitor: Plan tier %d, path is ultra constrained %{BOOL}d, isUltraConstrained %{BOOL}d"
+ "/Library/Caches/com.apple.xbs/Sources/AOP_MicroAPSD/src/libuaps/pc-msgrowth.c"
+ "PCSharedMultiStageGrowthAlgorithm"
+ "T@\"NSObject<OS_os_log>\",R,N,V_logObject"
+ "TB,D,N"
+ "TQ,R,D,N"
+ "Td,D,N"
+ "Td,R,D,N"
+ "Ti,R,D,N"
+ "T{_PCMSGA=dBddddddBBdQ{_PCMSGA_PCTimeRange=dd}iiddddd^q^q(?={?=Q[128c]}{?=Q[0c]})@ii},N,V_underlyingAlgorithm"
+ "T{_PCTimeRange=dd},D,N"
+ "UseSharedUAPSLibrary"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s:   - forcing RefinedShrink (%lld <= %g)"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s(%d) [%d]"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s(%g) [%g]"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s() %d"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s() %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s() %llu"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s() {%g,%g}"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: %s({%g,%g}) [{%g,%g}]"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Initialized with keepAliveInterval %g inInitialGrowth %s"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Shrinking %g by %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: Unexpected _leaveMinimumIntervalFallbackStateDate %llu in MinimumIntervalFallbackState, changing to %llu"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: _leaveMinimumIntervalFallbackStateDate is nil. Leave minimumIntervalFallbackState. Changing maximum keep alive interval back to %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: adjustGrowthAlgorithmMode. {lastMode: %s, currentMode: %s}"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: after previous MinimumIntervalFallbackState ends, extend leaveMinimumIntervalFallbackStateDate to %llu"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaveMinimumFallbackStateDate passed, acting"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaving the initial growth stage for refined growth"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: leaving the steady state and trying to grow again"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: minimumIntervalFallbackEnabled changed to %s"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: moved into Steady State - %g - %g <= %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: no signal avoidance {interval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g}"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override interval %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override max interval %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: override min interval %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: received action %s while in stage %s"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: resetAlgorithmToInterval: %g state: %s"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: set the steady state expiration date to %llu"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setCurrentKeepAlive with interval %g varianceMode %u allowRoundup %s"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setting current interval to %g seconds"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: setting lastSuccessfulKeepAliveInterval to %g seconds"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: signalAvoidanceRange contained, increasing %s, end %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: surpassed where the previous initial growth stopped at %g; reverting to initial growth."
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: triggered signaling avoidance {interval: %g, adjustedInterval: %g, _signalAvoidanceRange.start: %g, _signalAvoidanceRange.duration: %g, roundUpRatio: %g}"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: useIntervalIfImprovement %g   lastKeepAliveInterval: %g  currentKeepAliveInterval: %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: using a steady state timeout of %g for current interval %g"
+ "[%15s:%-4d| %-30s] PCMSGA(%p) %s: using double the current interval for the steady state timer interval since we are significantly below the high watermark of %g seconds"
+ "_NSDate_alloc_initWithTimeIntervalSinceNow"
+ "_NSDate_timeIntervalSinceNow"
+ "_processInitialGrowthAction"
+ "_processMinimumIntervalFallbackStateAction"
+ "_processRefinedGrowthAction"
+ "_processRefinedShrinkAction"
+ "_processSteadyStateAction"
+ "_resetAlgorithmToInterval"
+ "_saveWWANKeepAliveIntervalWithInfo:"
+ "_setCurrentKeepAliveInterval"
+ "_underlyingAlgorithm"
+ "currentCacheDictonary"
+ "dataPlanTier"
+ "growthState"
+ "initAgentDataFromInternetPath:"
+ "initWith"
+ "interval > 0"
+ "isPathUltraConstrained:"
+ "logObject"
+ "pc-msgrowth.c"
+ "processNextAction"
+ "resetKeepAliveStateMachineIfNecessary"
+ "saveKeepAliveInterval:isInitialGrowth:"
+ "setIsServerOriginatedKeepAlive"
+ "setLastSuccessfulKeepAliveInterval"
+ "setMaximumKeepAliveInterval"
+ "setMinimumIntervalFallbackEnabled"
+ "setMinimumIntervalFallbackStateTimeout"
+ "setMinimumKeepAliveInterval"
+ "setServerStatsExpectedKeepAliveInterval"
+ "setServerStatsMaxKeepAliveInterval"
+ "setServerStatsMinKeepAliveInterval"
+ "setSignalAvoidanceRange"
+ "setUnderlyingAlgorithm:"
+ "setUsingServerStatsAggressively"
+ "stringForAddressFamily:"
+ "underlyingAlgorithm"
+ "useIntervalIfImprovement"
+ "v336@0:8{_PCMSGA=dBddddddBBdQ{_PCMSGA_PCTimeRange=dd}iiddddd^q^q(?={?=Q[128c]}{?=Q[0c]})@ii}16"
+ "{_PCMSGA=\"currentKeepAliveInterval\"d\"isServerOriginatedKeepAlive\"B\"minimumKeepAliveInterval\"d\"maximumKeepAliveInterval\"d\"serverStatsExpectedKeepAliveInterval\"d\"serverStatsMinKeepAliveInterval\"d\"serverStatsMaxKeepAliveInterval\"d\"lastSuccessfulKeepAliveInterval\"d\"minimumIntervalFallbackEnabled\"B\"usingServerStatsAggressively\"B\"minimumIntervalFallbackStateTimeout\"d\"countOfGrowthActions\"Q\"signalAvoidanceRange\"{_PCMSGA_PCTimeRange=\"start\"d\"duration\"d}\"growthStage\"i\"previousAction\"i\"previousMaximumKeepAliveInterval\"d\"lastKeepAliveInterval\"d\"highWatermark\"d\"initialGrowthStageHighWatermark\"d\"initialGrowthStageLastAttempt\"d\"leaveSteadyStateDate\"^q\"leaveMinimumIntervalFallbackStateDate\"^q\"algorithmName\"(?=\"\"{?=\"len\"Q\"payload\"[128c]}\"nsstring\"{?=\"len\"Q\"payload\"[0c]})\"logObject\"@\"NSObject<OS_os_log>\"\"lastKeepAliveAlgorithmMode\"i\"currentKeepAliveAlgorithmMode\"i}"
+ "{_PCMSGA=dBddddddBBdQ{_PCMSGA_PCTimeRange=dd}iiddddd^q^q(?={?=Q[128c]}{?=Q[0c]})@ii}16@0:8"
+ "\xf0\xf0\x91"
- "_stringForAddressFamily:"

```
