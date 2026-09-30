## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-375.0.0.0.0
-  __TEXT.__text: 0x14ab8
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x978
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x4148
+378.0.0.0.0
+  __TEXT.__text: 0x1502c
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x968
+  __TEXT.__const: 0x168
+  __TEXT.__cstring: 0x41f6
   __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__oslogstring: 0x271d
+  __TEXT.__oslogstring: 0x27fb
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x394f
-  __TEXT.__objc_methtype: 0x71c
-  __TEXT.__objc_stubs: 0x12a0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x1560
+  __TEXT.__objc_methname: 0x398f
+  __TEXT.__objc_methtype: 0x759
+  __TEXT.__objc_stubs: 0x1440
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x1628
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0x19a8
+  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x5700
+  __AUTH_CONST.__objc_const: 0x1948
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1e0
-  __DATA.__data: 0x1c8
+  __DATA.__objc_ivar: 0x1d8
+  __DATA.__data: 0x1c0
   __DATA.__common: 0x18
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D1A013C-9CED-31A3-87F7-EAB4B64A9FC3
-  Functions: 525
-  Symbols:   1920
-  CStrings:  2173
+  UUID: 2454BBE8-40DB-37FA-B700-9A1A3C62D4E2
+  Functions: 527
+  Symbols:   1945
+  CStrings:  2211
 
Symbols:
+ +[HTMonitorPidHangEvent _updateRunningBoardProcessMonitor]
+ +[HTMonitorPidHangEvent removePidFromProcessMonitoring:]
+ +[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]
+ GCC_except_table13
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table73
+ _OBJC_CLASS_$_NSMutableSet
+ ___58+[HTMonitorPidHangEvent _updateRunningBoardProcessMonitor]_block_invoke
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_2
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_2.cold.1
+ ___97-[HTPrefs setupPrefsWithQueue:profilePath:taskingDomainName:hangtracerDomain:setupInternalPrefs:]_block_invoke.105
+ ___HTConnectToHTMonitor_block_invoke.41
+ ___HTInitializeHangTracerMonitor_block_invoke.50
+ ___HTInitializeHangTracerMonitor_block_invoke.50.cold.1
+ ___HTInitializeHangTracerMonitor_block_invoke.50.cold.2
+ ___HTInitializeHangTracerMonitor_block_invoke.50.cold.3
+ ___HTInitializeHangTracerMonitor_block_invoke.53
+ ___StartMonitoringWatchdogDisablement_block_invoke.159
+ ___block_descriptor_32_e40_v16?0"<RBSProcessMonitorConfiguring>"8l
+ ___block_literal_global.12
+ ___block_literal_global.139
+ ___block_literal_global.147
+ ___block_literal_global.153
+ ___block_literal_global.16
+ ___block_literal_global.163
+ ___block_literal_global.168
+ ___block_literal_global.201
+ ___block_literal_global.44
+ ___block_literal_global.49
+ ___block_literal_global.55
+ ___checkForAssertionOverlap_block_invoke.10
+ ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.188
+ ___exp10
+ ___handleSettingChange_block_invoke.145
+ _addNewTaskStateToHangEvent
+ _iterateRecentStateInfo
+ _kHTEndTaskStateKey
+ _kHTIntervalsInTaskStateKey
+ _kHTPercentInTaskStateKey
+ _kHTSecondsSinceTaskStateTransitionBeforeHangKey
+ _kHTStartTaskStateKey
+ _kHTStateInfoDataKey
+ _kHTTaskStateBreakdownKey
+ _kHTTaskStateEnumKey
+ _kHTTaskStateNameKey
+ _kHTTimeInTaskStateKey
+ _monitor
+ _objc_msgSend$_updateRunningBoardProcessMonitor
+ _objc_msgSend$bundle
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$pid
+ _objc_msgSend$predicateMatchingIdentifiers:
+ _objc_msgSend$previousState
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removePidFromProcessMonitoring:
+ _objc_msgSend$set
+ _objc_msgSend$setServiceClass:
+ _objc_msgSend$setupRunningBoardProcessMonitorForPid:
+ _objc_msgSend$taskState
+ _objc_msgSend$updateConfiguration:
+ _processIdentifiers
+ _roundDoubleToDecimalPlace
+ _stringDescriptionOfCPURole
+ _stringDescriptionOfRBSTaskState
- -[HTPrefs initPropertyMemoryLoggingIntervalSec:]
- -[HTPrefs memoryLoggingEnabled]
- -[HTPrefs memoryLoggingIntervalSec]
- -[HTPrefs setMemoryLoggingIntervalSec:]
- GCC_except_table37
- GCC_except_table39
- GCC_except_table41
- GCC_except_table43
- GCC_except_table46
- GCC_except_table51
- GCC_except_table57
- GCC_except_table62
- GCC_except_table7
- GCC_except_table72
- _ADClientAddValueForScalarKey
- _ADClientPushValueForDistributionKey
- _ADClientSetValueForScalarKey
- _HTAggdAddValueForScalarKey
- _HTAggdPushValueForDistributionKey
- _HTAggdSetValueForScalarKey
- _HTSE_ADDAILY_DATE_CHANGED_NOTIFICATION
- _OBJC_IVAR_$_HTPrefs._memoryLoggingEnabled
- _OBJC_IVAR_$_HTPrefs._memoryLoggingIntervalSec
- _OUTLINED_FUNCTION_9
- ___97-[HTPrefs setupPrefsWithQueue:profilePath:taskingDomainName:hangtracerDomain:setupInternalPrefs:]_block_invoke.107
- ___HTConnectToHTMonitor_block_invoke.25
- ___HTInitializeHangTracerMonitor_block_invoke.32
- ___HTInitializeHangTracerMonitor_block_invoke.32.cold.1
- ___HTInitializeHangTracerMonitor_block_invoke.32.cold.2
- ___HTInitializeHangTracerMonitor_block_invoke.32.cold.3
- ___HTInitializeHangTracerMonitor_block_invoke.36
- ___StartMonitoringWatchdogDisablement_block_invoke.162
- ___block_literal_global.142
- ___block_literal_global.150
- ___block_literal_global.156
- ___block_literal_global.169
- ___block_literal_global.171
- ___block_literal_global.218
- ___block_literal_global.31
- ___block_literal_global.38
- ___checkForAssertionOverlap_block_invoke.16
- ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.203
- ___handleSettingChange_block_invoke.148
- _checkForHangWithUserMovedAwayAndRecentAssertions.cold.8
- _isAppBeingDebugged.cold.2
- _kHTPrefsMemoryLoggingEnabled
- _kHTPrefsMemoryLoggingIntervalSec
- _objc_msgSend$setMemoryLoggingIntervalSec:
CStrings:
+ "  Index %d: Timestamp = %llu, Role = %d\n"
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
+ "Hang detected below telemetry threshold: hang duration = %.2fms, telemetry treshold = %.2dms"
+ "One or more of required XPC Keys were not received by hangtracerd"
+ "PRIO_DARWIN_ROLE_DARWIN_BG"
+ "PRIO_DARWIN_ROLE_DEFAULT"
+ "PRIO_DARWIN_ROLE_NON_UI"
+ "PRIO_DARWIN_ROLE_TAL_LAUNCH"
+ "PRIO_DARWIN_ROLE_UI"
+ "PRIO_DARWIN_ROLE_UI_FOCAL"
+ "PRIO_DARWIN_ROLE_UI_NON_FOCAL"
+ "PRIO_DARWIN_ROLE_UNKNOWN"
+ "PRIO_DARWIN_ROLE_USER_INIT"
+ "RBSTaskStateNone"
+ "RBSTaskStateRunningScheduled"
+ "RBSTaskStateRunningSuspended"
+ "RBSTaskStateRunningUnknown"
+ "RBSTaskStateUnknown"
+ "Received RB Notification for state change of process '%s'. State changed from %d to %d"
+ "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
+ "There is no HTMonitorPidHangEvent for process with pid %d and bundleInfo %{public}@"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
+ "_updateRunningBoardProcessMonitor"
+ "bundle"
+ "endTaskState"
+ "identifierWithPid:"
+ "intervalsInTaskState"
+ "objectForKey:"
+ "percentInTaskState"
+ "predicateMatchingIdentifiers:"
+ "previousState"
+ "received XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
+ "received an unexpected XPC response from hangtracerd"
+ "removeObject:"
+ "removePidFromProcessMonitoring:"
+ "secondsSinceTaskStateTransitionBeforeHangStart"
+ "set"
+ "setServiceClass:"
+ "setupRunningBoardProcessMonitorForPid:"
+ "startTaskState"
+ "stateInfo"
+ "stateInfoData"
+ "taskState"
+ "taskStateBreakdown"
+ "taskStateEnum"
+ "taskStateName"
+ "timeInTaskState"
+ "updateConfiguration:"
+ "\xf0\xf0A!V!"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
- "Hang detected below aggd threshold: hang duration = %.2fms, aggd treshold = %.2dms"
- "HangTracerEnableMemoryLogging"
- "HangTracerMemoryLoggingInterval"
- "One or more of required XPC Keys were not recieved by hangtracerd"
- "Recieved XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
- "Recieved an unexpected XPC response from hangtracerd"
- "TB,R,V_memoryLoggingEnabled"
- "TI,V_memoryLoggingIntervalSec"
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
- "_memoryLoggingEnabled"
- "_memoryLoggingIntervalSec"
- "com.apple.aggregated.addaily.logging"
- "com.apple.hangtracer.HTResume.OverResumed"
- "com.apple.ht_always_on.%s.%s"
- "com.apple.ht_assertion_overlap.%s.%s"
- "com.apple.ht_assertion_stats.hang_overlap_ms"
- "com.apple.ht_assertion_stats.hang_overlap_percent"
- "com.apple.ht_debugger_attached.%s.%s"
- "com.apple.ht_extended_launch_overlap.%s.%s"
- "initPropertyMemoryLoggingIntervalSec:"
- "memoryLoggingEnabled"
- "memoryLoggingIntervalSec"
- "setMemoryLoggingIntervalSec:"
- "v20@0:8I16"
- "\xf0\xf0Q!V!"

```
