## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0x1503c
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x968
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x41f6
+382.0.0.0.0
+  __TEXT.__text: 0x17250
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x974
+  __TEXT.__const: 0x160
+  __TEXT.__cstring: 0x41b0
+  __TEXT.__oslogstring: 0x2b44
   __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__oslogstring: 0x279d
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__unwind_info: 0x558
   __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x398f
-  __TEXT.__objc_methtype: 0x759
-  __TEXT.__objc_stubs: 0x1440
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x1650
+  __TEXT.__objc_methname: 0x3b6d
+  __TEXT.__objc_methtype: 0x765
+  __TEXT.__objc_stubs: 0x16c0
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x1688
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x588
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x5700
-  __AUTH_CONST.__objc_const: 0x1948
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x56c0
+  __AUTH_CONST.__objc_const: 0x1978
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1d8
-  __DATA.__data: 0x1c0
+  __DATA.__objc_ivar: 0x1dc
+  __DATA.__data: 0x208
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x18
-  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2166393-B7CA-36EF-9447-99B7969C7D41
-  Functions: 527
-  Symbols:   1950
-  CStrings:  2209
+  UUID: 07EE3275-4A43-374A-866C-F04C62C13920
+  Functions: 550
+  Symbols:   2039
+  CStrings:  2242
 
Symbols:
+ -[HTPrefs shouldCollectCPURoleInfo]
+ _CFAbsoluteTimeGetCurrent
+ _HTGetMachAbsoluteTimeFromNSDate
+ _NSStringFromRBSRole
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSNull
+ _OBJC_IVAR_$_HTPrefs._shouldCollectCPURoleInfo
+ ___63+[HTMonitorPidHangEvent setupRunningBoardProcessMonitorForPid:]_block_invoke_3.cold.2
+ ___HTConnectToHTMonitor_block_invoke.42
+ ___HTInitializeHangTracerMonitor_block_invoke.51
+ ___HTInitializeHangTracerMonitor_block_invoke.51.cold.1
+ ___HTInitializeHangTracerMonitor_block_invoke.51.cold.2
+ ___HTInitializeHangTracerMonitor_block_invoke.51.cold.3
+ ___HTInitializeHangTracerMonitor_block_invoke.55
+ ___block_descriptor_120_e19_"NSDictionary"8?0l
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_40_e8_32s_e11_q24?0816ls32l8
+ ___block_descriptor_48_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_80_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.4
+ ___block_literal_global.45
+ ___block_literal_global.50
+ ___block_literal_global.57
+ ___createStateInfoJSONBlobForHang_block_invoke
+ ___createStateInfoSortedArrayWithPtr_block_invoke
+ ___createStateInfoSortedArrayWithPtr_block_invoke.cold.1
+ ___stateInfoSortedArrayComparator_block_invoke
+ ___stateInfoSortedArrayComparator_block_invoke_2
+ ___stateInfoSortedArrayComparator_block_invoke_2.cold.1
+ ___stateInfoSortedArrayComparator_block_invoke_2.cold.2
+ __isValidStateInfoSortedArray
+ __isValidStateInfoSortedArray.cold.1
+ __isValidStateInfoSortedArray.cold.2
+ _addNewCPURoleToHangEvent
+ _calcluateDurationInCPURoleFromSortedArray
+ _calculateDurationInCPURoleFromStateInfoDict
+ _createStateInfoJSONBlobForHang
+ _createStateInfoJSONBlobForHang.cold.1
+ _createStateInfoSortedArrayWithPtr
+ _createStateInfoSortedArrayWithPtr.cold.1
+ _createStateInfoSortedArrayWithPtr.cold.2
+ _iterateRecentStateInfo.cold.1
+ _kHTCPURoleBreakdownKey
+ _kHTCPURoleEnumKey
+ _kHTCPURoleNameKey
+ _kHTCoreAnalyticsAssertionOtherCPURole
+ _kHTCoreAnalyticsAssertionUIFocal
+ _kHTCoreAnalyticsAssertionUINonFocal
+ _kHTCoreAnalyticsHTForegroundOtherCPURole
+ _kHTCoreAnalyticsHTForegroundUIFocal
+ _kHTCoreAnalyticsHTForegroundUINonFocal
+ _kHTCoreAnalyticsHangOtherCPURole
+ _kHTCoreAnalyticsHangUIFocal
+ _kHTCoreAnalyticsHangUINonFocal
+ _kHTEndCPURoleKey
+ _kHTIntervalsInCPURoleKey
+ _kHTPercentInCPURoleKey
+ _kHTPrefsShouldCollectCPURoleInfo
+ _kHTSecondsSinceCPURoleTransitionBeforeHangKey
+ _kHTStartCPURoleKey
+ _kHTTimeInCPURoleKey
+ _objc_msgSend$count
+ _objc_msgSend$cpuRole
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$floatValue
+ _objc_msgSend$identifier
+ _objc_msgSend$indexOfObject:inSortedRange:options:usingComparator:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$lastObject
+ _objc_msgSend$lastStateChangeTimestamp
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shouldCollectCPURoleInfo
+ _objc_msgSend$stringValue
+ _objc_msgSend$unsignedCharValue
+ _objc_retain_x26
+ _printCurrentTailspinConfig
+ _stateInfoSortedArrayComparator
+ _stateInfoSortedArrayComparator._comparator
+ _stateInfoSortedArrayComparator.cold.1
+ _stateInfoSortedArrayComparator.onceToken
- ___HTConnectToHTMonitor_block_invoke.41
- ___HTInitializeHangTracerMonitor_block_invoke.50
- ___HTInitializeHangTracerMonitor_block_invoke.50.cold.1
- ___HTInitializeHangTracerMonitor_block_invoke.50.cold.2
- ___HTInitializeHangTracerMonitor_block_invoke.50.cold.3
- ___HTInitializeHangTracerMonitor_block_invoke.53
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_72_e19_"NSDictionary"8?0l
- ___block_literal_global.44
- ___block_literal_global.49
- ___block_literal_global.55
- _addNewTaskStateToHangEvent
- _kHTEndTaskStateKey
- _kHTIntervalsInTaskStateKey
- _kHTPercentInTaskStateKey
- _kHTSecondsSinceTaskStateTransitionBeforeHangKey
- _kHTStartTaskStateKey
- _kHTTaskStateBreakdownKey
- _kHTTaskStateEnumKey
- _kHTTaskStateNameKey
- _kHTTimeInTaskStateKey
- _objc_msgSend$taskState
- _objc_retain_x9
- _stringDescriptionOfCPURole
- _stringDescriptionOfRBSTaskState
CStrings:
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16Q24"
+ "C"
+ "Compsed final stateInfo sorted Array: %{public}@"
+ "Failed to parse State info dictionary object from sorted array '%@', object is type of class '%@'"
+ "Failed to parse State info dictionary object of key '%@' from sorted array '%@', object is type of class '%@'"
+ "Index %d: Timestamp = %llu, Role = %@\n"
+ "Invalid object(s) of class '%@' and '%@' passed into StateInfo timestamp comparator."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary '%@' during sorting."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary during sorting."
+ "No states were present in the state info array before a hang occurred."
+ "No valid data in recentStateInfo for hang, not sending CPURole data."
+ "Object in state info array is not a dictionary. Is kind of class %@"
+ "Passed in nil stateInfoPtr, returning nil."
+ "RB Notification contained a nil bundle identifier, defaulting to event bundle id."
+ "Received RB Notification for CPU Role change of process(%d) '%{public}@'. Changed from %{public}@ to %{public}@ at %@"
+ "Recent state info:\n%{public}@"
+ "ShouldCollectCPURoleInfo"
+ "TB,R,V_shouldCollectCPURoleInfo"
+ "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ},R,V_shmem_region"
+ "The provided stateInfoArray '%@' only has state objects AFTER then end of the hang (%llu matu)."
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16@0:8"
+ "_shouldCollectCPURoleInfo"
+ "assertion_other_ms"
+ "assertion_ui_focal_ms"
+ "assertion_ui_nonfocal_ms"
+ "count"
+ "cpuRole"
+ "cpuRoleBreakdown"
+ "cpuRoleEnum"
+ "cpuRoleName"
+ "dictionary"
+ "dictionaryWithDictionary:"
+ "duration_other_ms"
+ "duration_ui_focal_ms"
+ "duration_ui_nonfocal_ms"
+ "endCPURole"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "floatValue"
+ "foreground_other_ms"
+ "foreground_ui_focal_ms"
+ "foreground_ui_nonfocal_ms"
+ "identifier"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "insertObject:atIndex:"
+ "intervalsInCPURole"
+ "isEqualToNumber:"
+ "lastObject"
+ "lastStateChangeTimestamp"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLong:"
+ "objectAtIndexedSubscript:"
+ "percentInCPURole"
+ "q24@?0@8@16"
+ "removeObjectAtIndex:"
+ "secondsSinceCPURoleTransitionBeforeHangStart"
+ "setValue:forKey:"
+ "shouldCollectCPURoleInfo"
+ "startCPURole"
+ "stringValue"
+ "timeInCPURole"
+ "timestamp"
+ "unsignedCharValue"
+ "v32@?0@8@16^B24"
- "  Index %d: Timestamp = %llu, Role = %d\n"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
- "PRIO_DARWIN_ROLE_DARWIN_BG"
- "PRIO_DARWIN_ROLE_DEFAULT"
- "PRIO_DARWIN_ROLE_NON_UI"
- "PRIO_DARWIN_ROLE_TAL_LAUNCH"
- "PRIO_DARWIN_ROLE_UI"
- "PRIO_DARWIN_ROLE_UI_FOCAL"
- "PRIO_DARWIN_ROLE_UI_NON_FOCAL"
- "PRIO_DARWIN_ROLE_UNKNOWN"
- "PRIO_DARWIN_ROLE_USER_INIT"
- "RBSTaskStateNone"
- "RBSTaskStateRunningScheduled"
- "RBSTaskStateRunningSuspended"
- "RBSTaskStateRunningUnknown"
- "RBSTaskStateUnknown"
- "Received RB Notification for state change of pid %d with bundleID '%{public}@'. State changed from %d to %d"
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
- "endTaskState"
- "intervalsInTaskState"
- "percentInTaskState"
- "secondsSinceTaskStateTransitionBeforeHangStart"
- "startTaskState"
- "taskState"
- "taskStateBreakdown"
- "taskStateEnum"
- "taskStateName"
- "timeInTaskState"

```
