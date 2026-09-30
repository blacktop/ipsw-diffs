## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2300.100.0.0.0
-  __TEXT.__text: 0x105e78
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0xd74c
+2303.1.2.0.0
+  __TEXT.__text: 0x106894
+  __TEXT.__auth_stubs: 0x1800
+  __TEXT.__objc_methlist: 0xd744
   __TEXT.__const: 0x1310
   __TEXT.__oslogstring: 0x10f73
-  __TEXT.__cstring: 0x9866
-  __TEXT.__gcc_except_tab: 0x12b4
+  __TEXT.__cstring: 0x9656
+  __TEXT.__gcc_except_tab: 0x147c
   __TEXT.__dlopen_cstrs: 0x837
   __TEXT.__ustring: 0x1a
   __TEXT.__swift5_typeref: 0x86a

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift_as_entry: 0x104
   __TEXT.__swift_as_ret: 0x108
-  __TEXT.__unwind_info: 0x4868
-  __TEXT.__eh_frame: 0x30c0
-  __TEXT.__objc_classname: 0x1976
-  __TEXT.__objc_methname: 0x17e66
+  __TEXT.__unwind_info: 0x4910
+  __TEXT.__eh_frame: 0x3150
+  __TEXT.__objc_classname: 0x1955
+  __TEXT.__objc_methname: 0x17e37
   __TEXT.__objc_methtype: 0x4248
-  __TEXT.__objc_stubs: 0x11cc0
+  __TEXT.__objc_stubs: 0x11c80
   __DATA_CONST.__got: 0xc58
-  __DATA_CONST.__const: 0x41f0
-  __DATA_CONST.__objc_classlist: 0x690
+  __DATA_CONST.__const: 0x4240
+  __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6030
+  __DATA_CONST.__objc_selrefs: 0x6028
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH_CONST.__const: 0x39b8
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x29190
+  __AUTH_CONST.__objc_const: 0x28d60
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2df0
+  __AUTH.__objc_data: 0x2da0
   __AUTH.__data: 0x3c8
-  __DATA.__objc_ivar: 0x954
+  __DATA.__objc_ivar: 0x95c
   __DATA.__data: 0x2b28
   __DATA.__common: 0x68
   __DATA.__bss: 0x1190

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1D5F7017-8DA7-3EF1-9E3F-AFF41B794573
-  Functions: 6554
-  Symbols:   18248
-  CStrings:  8390
+  UUID: 5C6E64A2-15F7-3A94-A200-40E60CCC0AA8
+  Functions: 6578
+  Symbols:   18288
+  CStrings:  8382
 
Symbols:
+ -[MTAlarmStorage _withLock:]
+ -[MTAlarmStorage lock]
+ -[MTAlarmStorage setLock:]
+ -[MTTimerStorage _withLock:]
+ -[MTTimerStorage lock]
+ -[MTTimerStorage setLock:]
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table153
+ GCC_except_table169
+ GCC_except_table17
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table63
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table87
+ _OBJC_IVAR_$_MTAlarmStorage._lock
+ _OBJC_IVAR_$_MTTimerStorage._lock
+ __OBJC_$_PROP_LIST_MTAlarmStorage.759
+ __OBJC_$_PROP_LIST_MTTimerStorage.351
+ ___24-[MTAlarmStorage alarms]_block_invoke_2
+ ___24-[MTTimerStorage timers]_block_invoke_2
+ ___28-[MTAlarmStorage sleepAlarm]_block_invoke_2
+ ___34-[MTAlarmStorage _queue_allAlarms]_block_invoke
+ ___35-[MTAlarmStorage _queue_sortAlarms]_block_invoke
+ ___35-[MTTimerStorage _queue_sortTimers]_block_invoke_2
+ ___38-[MTAlarmStorage _queue_persistAlarms]_block_invoke
+ ___38-[MTTimerStorage _queue_persistTimers]_block_invoke
+ ___39-[MTAlarmStorage _queue_allSleepAlarms]_block_invoke
+ ___40-[MTAlarmStorage _queue_sortSleepAlarms]_block_invoke
+ ___43-[MTAlarmStorage updateSleepAlarms:source:]_block_invoke.401
+ ___43-[MTTimerStorage _queue_removeStaleTimers:]_block_invoke
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.364
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.373
+ ___44-[MTTimerStorage _loadTimersWithCompletion:]_block_invoke.28
+ ___46-[MTAlarmStorage _removeAlarmDataIfNecessary:]_block_invoke_2
+ ___50-[MTAlarmStorage _queue_removeAllAlarmsForSource:]_block_invoke
+ ___50-[MTTimerStorage _queue_removeAllTimersForSource:]_block_invoke
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397.cold.1
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke_2
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke_2.cold.1
+ ___52-[MTAlarmStorage _queuePersistAlarm:replacingAlarm:]_block_invoke
+ ___52-[MTAlarmStorage updateSleepAlarmsWithBlock:source:]_block_invoke_3
+ ___52-[MTAlarmStorage updateSleepAlarmsWithBlock:source:]_block_invoke_4
+ ___52-[MTTimerStorage _queuePersistTimer:replacingTimer:]_block_invoke
+ ___54-[MTTimerStorage _queue_timerMatchingTimerIdentifier:]_block_invoke_2
+ ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.379
+ ___56-[MTTimerStorage _queue_addTimer:withCompletion:source:]_block_invoke
+ ___60-[MTTimerStorage _createDefaultTimerIfNeededWithCompletion:]_block_invoke_2
+ ___60-[MTTimerStorage _queue_setAllTimers:source:persist:notify:]_block_invoke
+ ___61-[MTAlarmStorage _queue_updateSleepAlarmsFromExistingAlarms:]_block_invoke_3
+ ___81-[MTAlarmStorage _queue_setAllAlarms:sleepAlarms:source:persist:notify:override:]_block_invoke_4
+ ___block_descriptor_48_e8_32s40r_e26_"MTAlarm"16?0"MTAlarm"8lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_literal_global.383
+ ___block_literal_global.404
+ ___block_literal_global.408
+ ___block_literal_global.485
- -[MTCreateSingleTimerIntentHandler _createTimerWithIntent:dryRun:completion:]
- -[MTCreateSingleTimerIntentHandler _responseToCreateTimerIntent:withCreatedTimer:error:dryRun:]
- -[MTCreateSingleTimerIntentHandler confirmCreateTimer:completion:]
- -[MTCreateSingleTimerIntentHandler handleCreateTimer:completion:]
- -[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]
- -[MTCreateSingleTimerIntentHandler resolveLabelForCreateTimer:withCompletion:]
- GCC_except_table42
- GCC_except_table56
- _OBJC_CLASS_$_MTCreateSingleTimerIntentHandler
- _OBJC_METACLASS_$_MTCreateSingleTimerIntentHandler
- __OBJC_$_INSTANCE_METHODS_MTCreateSingleTimerIntentHandler
- __OBJC_$_PROP_LIST_MTAlarmStorage.748
- __OBJC_$_PROP_LIST_MTCreateSingleTimerIntentHandler
- __OBJC_$_PROP_LIST_MTTimerStorage.342
- __OBJC_CLASS_PROTOCOLS_$_MTCreateSingleTimerIntentHandler
- __OBJC_CLASS_RO_$_MTCreateSingleTimerIntentHandler
- __OBJC_METACLASS_RO_$_MTCreateSingleTimerIntentHandler
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.372
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.396
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.396.cold.1
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.cold.1
- ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.378
- ___77-[MTCreateSingleTimerIntentHandler _createTimerWithIntent:dryRun:completion:]_block_invoke
- ___77-[MTCreateSingleTimerIntentHandler _createTimerWithIntent:dryRun:completion:]_block_invoke_2
- ___77-[MTCreateSingleTimerIntentHandler _createTimerWithIntent:dryRun:completion:]_block_invoke_3
- ___77-[MTCreateSingleTimerIntentHandler _createTimerWithIntent:dryRun:completion:]_block_invoke_4
- ___81-[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]_block_invoke
- ___81-[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]_block_invoke.2
- ___81-[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]_block_invoke.2.cold.1
- ___block_descriptor_48_e8_32s40s_e26_"MTAlarm"16?0"MTAlarm"8ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSArray"8ls48l8s32l8s40l8
- ___block_literal_global.382
- ___block_literal_global.402
- ___block_literal_global.406
- ___block_literal_global.483
- _objc_msgSend$confirmationRequiredWithTimeIntervalToConfirm:
- _objc_msgSend$isRunningUnitTest
- _swift_task_isCurrentExecutor
- _swift_task_reportUnexpectedExecutor
CStrings:
+ "*"
- "-[MTCreateSingleTimerIntentHandler _responseToCreateTimerIntent:withCreatedTimer:error:dryRun:]"
- "-[MTCreateSingleTimerIntentHandler confirmCreateTimer:completion:]"
- "-[MTCreateSingleTimerIntentHandler handleCreateTimer:completion:]"
- "-[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]"
- "-[MTCreateSingleTimerIntentHandler resolveDurationForCreateTimer:withCompletion:]_block_invoke"
- "-[MTCreateSingleTimerIntentHandler resolveLabelForCreateTimer:withCompletion:]"
- "MTCreateSingleTimerIntentHandler"
- "MobileTimer/MTCDDataStore.swift"
- "confirmationRequiredWithTimeIntervalToConfirm:"

```
