## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2303.2.1.0.0
-  __TEXT.__text: 0x10c02c
+2303.2.2.0.0
+  __TEXT.__text: 0x10c2c0
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xd92c
+  __TEXT.__objc_methlist: 0xd95c
   __TEXT.__const: 0x1730
-  __TEXT.__oslogstring: 0x11023
-  __TEXT.__cstring: 0x9816
+  __TEXT.__oslogstring: 0x110b3
+  __TEXT.__cstring: 0x9836
   __TEXT.__gcc_except_tab: 0x14a8
   __TEXT.__dlopen_cstrs: 0x837
   __TEXT.__ustring: 0x1a

   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift_as_entry: 0x120
   __TEXT.__swift_as_ret: 0x124
-  __TEXT.__unwind_info: 0x46b8
+  __TEXT.__unwind_info: 0x46d0
   __TEXT.__eh_frame: 0x32d8
-  __TEXT.__objc_classname: 0x1955
-  __TEXT.__objc_methname: 0x180f9
+  __TEXT.__objc_classname: 0x195a
+  __TEXT.__objc_methname: 0x1812f
   __TEXT.__objc_methtype: 0x42ac
-  __TEXT.__objc_stubs: 0x11e20
+  __TEXT.__objc_stubs: 0x11e40
   __DATA_CONST.__got: 0xc78
-  __DATA_CONST.__const: 0x42c8
+  __DATA_CONST.__const: 0x4318
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60d8
+  __DATA_CONST.__objc_selrefs: 0x60e8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xca0
   __AUTH_CONST.__const: 0x3ce8
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x29028
+  __AUTH_CONST.__objc_const: 0x29090
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2f38
   __AUTH.__data: 0x4b8
-  __DATA.__objc_ivar: 0x968
+  __DATA.__objc_ivar: 0x96c
   __DATA.__data: 0x2ba8
   __DATA.__common: 0x68
   __DATA.__bss: 0x13a0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 09ACAE60-1F6C-34D5-8031-8DC125104189
-  Functions: 6719
-  Symbols:   18449
-  CStrings:  8428
+  UUID: BE20C531-4E54-3E51-9384-54C84710D72A
+  Functions: 6723
+  Symbols:   18463
+  CStrings:  8434
 
Symbols:
+ -[MTActivityCoordinator registerAnalyticsDelegate:]
+ -[MTActivityCoordinator reportingDelegate]
+ -[MTActivityCoordinator setReportingDelegate:]
+ _OBJC_IVAR_$_MTActivityCoordinator._reportingDelegate
+ __OBJC_$_PROP_LIST_MTAlarmStorage.768
+ ___43-[MTActivityCoordinator endAlertingSession]_block_invoke.62
+ ___43-[MTActivityCoordinator endAlertingSession]_block_invoke_2.61
+ ___43-[MTAlarmStorage updateSleepAlarms:source:]_block_invoke.410
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.382
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.329
+ ___45-[MTActivityCoordinator _dismissAlarmWithId:]_block_invoke.63
+ ___45-[MTActivityCoordinator _dismissTimerWithId:]_block_invoke.66
+ ___48-[MTActivityCoordinator source:didRemoveAlarms:]_block_invoke.50
+ ___48-[MTActivityCoordinator source:didRemoveAlarms:]_block_invoke.50.cold.1
+ ___49-[MTActivityCoordinator didRestoreAlarmSessions:]_block_invoke.56
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.406
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.406.cold.1
+ ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.388
+ ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.47
+ ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.47.cold.1
+ ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.48
+ ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke_3.cold.1
+ ___63-[MTActivityCoordinator source:didUpdateAlarms:previousAlarms:]_block_invoke.51
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.311
+ ___block_descriptor_48_e8_32s40s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.310
+ ___block_literal_global.333
+ ___block_literal_global.392
+ ___block_literal_global.413
+ ___block_literal_global.417
+ ___block_literal_global.494
+ ___block_literal_global.58
+ ___block_literal_global.65
+ _objc_msgSend$processDismissedAlarm:
- __OBJC_$_PROP_LIST_MTAlarmStorage.759
- ___43-[MTActivityCoordinator endAlertingSession]_block_invoke.58
- ___43-[MTActivityCoordinator endAlertingSession]_block_invoke_2.59
- ___43-[MTAlarmStorage updateSleepAlarms:source:]_block_invoke.401
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.364
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.320
- ___45-[MTActivityCoordinator _dismissAlarmWithId:]_block_invoke.61
- ___45-[MTActivityCoordinator _dismissTimerWithId:]_block_invoke.64
- ___48-[MTActivityCoordinator source:didRemoveAlarms:]_block_invoke.48
- ___48-[MTActivityCoordinator source:didRemoveAlarms:]_block_invoke.48.cold.1
- ___49-[MTActivityCoordinator didRestoreAlarmSessions:]_block_invoke.54
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.397.cold.1
- ___55-[MTAlarmStorage loadAlarmsFromCoreDataWithCompletion:]_block_invoke.379
- ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.45
- ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.45.cold.1
- ___57-[MTActivityCoordinator source:didFireAlarm:triggerType:]_block_invoke.46
- ___63-[MTActivityCoordinator source:didUpdateAlarms:previousAlarms:]_block_invoke.49
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.302
- ___block_literal_global.301
- ___block_literal_global.315
- ___block_literal_global.383
- ___block_literal_global.404
- ___block_literal_global.408
- ___block_literal_global.485
- ___block_literal_global.53
- ___block_literal_global.56
- ___block_literal_global.63
- ___block_literal_global.66
CStrings:
+ "%{public}@ didDismissAlarm:%{public}@"
+ "%{public}@ error alerting alarm activity in didFireAlarm: %{public}@. Did not return activity id"
+ "applicationsDidUpdateMetadata:"
+ "processDismissedAlarm:"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "\x81"

```
