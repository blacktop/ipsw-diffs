## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2330.0.0.0.0
-  __TEXT.__text: 0x1360e0
-  __TEXT.__objc_methlist: 0xea84
+2333.0.0.0.0
+  __TEXT.__text: 0x137d28
+  __TEXT.__objc_methlist: 0xeb44
   __TEXT.__const: 0x21d0
-  __TEXT.__gcc_except_tab: 0x1228
-  __TEXT.__cstring: 0x99d2
-  __TEXT.__oslogstring: 0x12d93
+  __TEXT.__gcc_except_tab: 0x1248
+  __TEXT.__cstring: 0x99f2
+  __TEXT.__oslogstring: 0x13213
   __TEXT.__dlopen_cstrs: 0x9dd
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x114c
-  __TEXT.__swift5_reflstr: 0x4ad
+  __TEXT.__swift5_reflstr: 0x4cd
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__constg_swiftt: 0x9f8
-  __TEXT.__swift5_fieldmd: 0x5cc
+  __TEXT.__swift5_fieldmd: 0x5d8
   __TEXT.__swift5_proto: 0xc4
   __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_capture: 0x1d20

   __TEXT.__swift_as_cont: 0x4d0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x59a8
+  __TEXT.__unwind_info: 0x5a10
   __TEXT.__eh_frame: 0x50c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4988
+  __DATA_CONST.__const: 0x4a00
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6830
+  __DATA_CONST.__objc_selrefs: 0x68b8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0xd20
-  __AUTH_CONST.__const: 0x5c68
+  __AUTH_CONST.__const: 0x5cc8
   __AUTH_CONST.__cfstring: 0x7540
-  __AUTH_CONST.__objc_const: 0x2c510
+  __AUTH_CONST.__objc_const: 0x2c518
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7894
-  Symbols:   12496
-  CStrings:  2853
+  Functions: 7930
+  Symbols:   12543
+  CStrings:  2872
 
Symbols:
+ -[MTAgent holidayAwareAlarmsEnabled]
+ -[MTAlarmStorage upcomingDateForHolidayAwareAlarm:]
+ -[MTAppEntityDonor donateHolidayAlarmsToIndex:]
+ -[MTAppEntityDonor partitionAlarms:completion:]
+ -[MTCalendarDataStorage upcomingDateForHolidayAlarm:]
+ -[MTTimerManager(Testing) test_currentTimer]
+ -[MTTimerManager(Testing) test_nextTimer]
+ -[MTTimerManager(Testing) test_pauseCurrentTimer]
+ -[MTTimerManager(Testing) test_resumeCurrentTimer]
+ -[MTTimerManager(Testing) test_startCurrentTimerWithDuration:]
+ -[MTTimerManager(Testing) test_stopCurrentTimer]
+ -[MTTimerManager(Testing) test_timerSyncWithIdentifier:]
+ -[MTTimerManager(Testing) test_timerWithIdentifier:]
+ -[MTTimerManager(Testing) test_timers]
+ -[MTTimerManager(Testing) test_updateCurrentTimerWithState:]
+ -[MTTimerServer test_getTimersWithCompletion:]
+ -[MTTimerStorage coreDataReady]
+ -[MTTimerStorage test_getTimersWithCompletion:]
+ GCC_except_table39
+ GCC_except_table75
+ __OBJC_$_INSTANCE_METHODS_MTTimerManager(IntentsSupport|Testing|MTTimerManagerProviding)
+ __OBJC_CLASS_PROTOCOLS_$_MTTimerManager(IntentsSupport|Testing|MTTimerManagerProviding)
+ ___38-[MTTimerManager(Testing) test_timers]_block_invoke
+ ___38-[MTTimerManager(Testing) test_timers]_block_invoke_2
+ ___38-[MTTimerManager(Testing) test_timers]_block_invoke_3
+ ___40-[MTAppEntityDonor source:didAddAlarms:]_block_invoke
+ ___41-[MTTimerManager(Testing) test_nextTimer]_block_invoke
+ ___41-[MTTimerManager(Testing) test_nextTimer]_block_invoke_2
+ ___41-[MTTimerManager(Testing) test_nextTimer]_block_invoke_3
+ ___43-[MTAppEntityDonor source:didUpdateAlarms:]_block_invoke
+ ___44-[MTTimerManager(Testing) test_currentTimer]_block_invoke
+ ___47-[MTAppEntityDonor partitionAlarms:completion:]_block_invoke
+ ___47-[MTTimerStorage test_getTimersWithCompletion:]_block_invoke
+ ___47-[MTTimerStorage test_getTimersWithCompletion:]_block_invoke_2
+ ___47-[MTTimerStorage test_getTimersWithCompletion:]_block_invoke_3
+ ___52-[MTTimerManager(Testing) test_timerWithIdentifier:]_block_invoke
+ ___52-[MTTimerManager(Testing) test_timerWithIdentifier:]_block_invoke_2
+ ___54-[MTAlarmIntentDonor source:didFireAlarm:triggerType:]_block_invoke
+ ___56-[MTTimerManager(Testing) test_timerSyncWithIdentifier:]_block_invoke
+ ___56-[MTTimerManager(Testing) test_timerSyncWithIdentifier:]_block_invoke_2
+ ___60-[MTTimerManager(Testing) test_updateCurrentTimerWithState:]_block_invoke
+ ___62-[MTTimerManager(Testing) test_startCurrentTimerWithDuration:]_block_invoke
+ ___block_descriptor_40_e8_32s_e25_v16?0"<MTTimerServer>"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSArray"16ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
+ _objc_msgSend$coreDataReady
+ _objc_msgSend$donateHolidayAlarmsToIndex:
+ _objc_msgSend$holidayAwareAlarmsEnabled
+ _objc_msgSend$partitionAlarms:completion:
+ _objc_msgSend$test_currentTimer
+ _objc_msgSend$test_getTimersWithCompletion:
+ _objc_msgSend$test_timers
+ _objc_msgSend$test_updateCurrentTimerWithState:
+ _objc_msgSend$upcomingDateForHolidayAlarm:
+ _objc_msgSend$upcomingDateForHolidayAwareAlarm:
+ _objc_msgSend$updateAlarmInIndex:upcomingDate:
- -[MTTimerStorage _createDefaultTimerIfNeededWithCompletion:]
- -[MTTimerStorage shouldUseCoreData]
- GCC_except_table42
- __OBJC_$_INSTANCE_METHODS_MTTimerManager(IntentsSupport|MTTimerManagerProviding)
- __OBJC_CLASS_PROTOCOLS_$_MTTimerManager(IntentsSupport|MTTimerManagerProviding)
- ___42-[MTTimerStorage getTimersWithCompletion:]_block_invoke_2
- ___60-[MTTimerStorage _createDefaultTimerIfNeededWithCompletion:]_block_invoke
- ___60-[MTTimerStorage _createDefaultTimerIfNeededWithCompletion:]_block_invoke_2
- _objc_msgSend$_createDefaultTimerIfNeededWithCompletion:
CStrings:
+ "%{public}@ Holiday alarm fired - re-donating intent: %{public}@"
+ "%{public}@ associatesEntities=NO, dropping didAddAlarms"
+ "%{public}@ associatesEntities=NO, dropping didAddTimers"
+ "%{public}@ associatesEntities=NO, dropping didDismissAlarm"
+ "%{public}@ associatesEntities=NO, dropping didDismissTimer"
+ "%{public}@ associatesEntities=NO, dropping didFireAlarm"
+ "%{public}@ associatesEntities=NO, dropping didFireTimer"
+ "%{public}@ associatesEntities=NO, dropping didRemoveAlarms"
+ "%{public}@ associatesEntities=NO, dropping didRemoveTimers"
+ "%{public}@ associatesEntities=NO, dropping didUpdateAlarms"
+ "%{public}@ associatesEntities=NO, dropping didUpdateTimers"
+ "%{public}@ associatesEntities=NO, dropping handleSystemReady"
+ "%{public}@ associatesEntities=NO, dropping reindexAllItems"
+ "%{public}@ associatesEntities=NO, dropping updateStopwatch"
+ "%{public}@ core data not ready, returning error to client: %{public}@"
+ "Earliest trigger date %{public}@ is past the last makeup day %{public}@, using current date instead"
+ "Error re-donating holiday alarm on fire: %{public}@"
+ "not initializing calendar data storage; holiday-aware alarms unsupported or disabled on this platform"
+ "repeatSchedule == %lld OR repeatSchedule == %lld"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
- "enabled == YES AND (repeatSchedule == %lld OR repeatSchedule == %lld)"
```
