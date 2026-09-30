## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Versions/A/MobileTimer`

```diff

-2330.0.0.0.0
-  __TEXT.__text: 0x101628
-  __TEXT.__objc_methlist: 0xae54
+2333.0.0.0.0
+  __TEXT.__text: 0x1032d0
+  __TEXT.__objc_methlist: 0xaf34
   __TEXT.__const: 0x1f40
-  __TEXT.__gcc_except_tab: 0xb44
-  __TEXT.__cstring: 0x7da2
-  __TEXT.__oslogstring: 0xc393
+  __TEXT.__gcc_except_tab: 0xb64
+  __TEXT.__cstring: 0x7dc2
+  __TEXT.__oslogstring: 0xc7b3
   __TEXT.__dlopen_cstrs: 0x415
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x1070
-  __TEXT.__swift5_reflstr: 0x4ad
+  __TEXT.__swift5_reflstr: 0x4cd
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__constg_swiftt: 0x9b8
-  __TEXT.__swift5_fieldmd: 0x5cc
+  __TEXT.__swift5_fieldmd: 0x5d8
   __TEXT.__swift5_proto: 0xc4
   __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_capture: 0x19f4

   __TEXT.__swift_as_cont: 0x3e8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x47c0
+  __TEXT.__unwind_info: 0x4818
   __TEXT.__eh_frame: 0x4310
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19a0
+  __DATA_CONST.__const: 0x19c0
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5110
+  __DATA_CONST.__objc_selrefs: 0x51a8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0xa38
-  __AUTH_CONST.__const: 0x7b88
+  __AUTH_CONST.__const: 0x7c78
   __AUTH_CONST.__cfstring: 0x6120
-  __AUTH_CONST.__objc_const: 0x1e938
+  __AUTH_CONST.__objc_const: 0x1e940
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6300
-  Symbols:   9720
-  CStrings:  2084
+  Functions: 6338
+  Symbols:   9772
+  CStrings:  2102
 
Symbols:
+ -[MTAgent holidayAwareAlarmsEnabled]
+ -[MTAlarm isCalendarOverride]
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
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table15
+ GCC_except_table43
+ GCC_except_table51
+ GCC_except_table86
+ __38-[MTTimerManager(Testing) test_timers]_block_invoke
+ __42-[MTTimerStorage getTimersWithCompletion:]_block_invoke
+ __54-[MTAlarmIntentDonor source:didFireAlarm:triggerType:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_MTTimerManager(IntentsSupport|Testing|MTTimerManagerProviding)
+ __OBJC_CLASS_PROTOCOLS_$_MTTimerManager(IntentsSupport|Testing|MTTimerManagerProviding)
+ ___38-[MTTimerManager(Testing) test_timers]_block_invoke
+ ___38-[MTTimerManager(Testing) test_timers]_block_invoke_2
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
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e25_v16?0"<MTTimerServer>"8l
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSArray"16l
+ ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16l
+ _objc_msgSend$coreDataReady
+ _objc_msgSend$donateHolidayAlarmsToIndex:
+ _objc_msgSend$holidayAwareAlarmsEnabled
+ _objc_msgSend$partitionAlarms:completion:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$test_currentTimer
+ _objc_msgSend$test_getTimersWithCompletion:
+ _objc_msgSend$test_timers
+ _objc_msgSend$test_updateCurrentTimerWithState:
+ _objc_msgSend$upcomingDateForHolidayAlarm:
+ _objc_msgSend$upcomingDateForHolidayAwareAlarm:
+ _objc_msgSend$updateAlarmInIndex:upcomingDate:
- -[MTTimerStorage _createDefaultTimerIfNeededWithCompletion:]
- -[MTTimerStorage shouldUseCoreData]
- GCC_except_table108
- GCC_except_table112
- GCC_except_table49
- GCC_except_table62
- __42-[MTTimerStorage getTimersWithCompletion:]_block_invoke_2
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
+ "Error re-donating holiday alarm on fire: %{public}@"
+ "not initializing calendar data storage; holiday-aware alarms unsupported or disabled on this platform"
+ "repeatSchedule == %lld OR repeatSchedule == %lld"
+ "v24@?0@\"NSArray\"8@\"NSArray\"16"
- "enabled == YES AND (repeatSchedule == %lld OR repeatSchedule == %lld)"
```
