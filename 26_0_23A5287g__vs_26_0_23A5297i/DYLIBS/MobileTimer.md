## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2293.0.0.0.0
-  __TEXT.__text: 0xf74d4
+2295.0.0.0.0
+  __TEXT.__text: 0xf7868
   __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0xd570
+  __TEXT.__objc_methlist: 0xd590
   __TEXT.__const: 0x1220
-  __TEXT.__oslogstring: 0xf830
-  __TEXT.__cstring: 0x95a6
+  __TEXT.__oslogstring: 0xf8d0
+  __TEXT.__cstring: 0x95c6
   __TEXT.__gcc_except_tab: 0x1264
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x1a

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift_as_entry: 0x100
   __TEXT.__swift_as_ret: 0x104
-  __TEXT.__unwind_info: 0x41e8
+  __TEXT.__unwind_info: 0x41f8
   __TEXT.__eh_frame: 0x2ec0
   __TEXT.__objc_classname: 0x193b
-  __TEXT.__objc_methname: 0x17c29
-  __TEXT.__objc_methtype: 0x41e5
-  __TEXT.__objc_stubs: 0x11a20
+  __TEXT.__objc_methname: 0x17ca2
+  __TEXT.__objc_methtype: 0x41f6
+  __TEXT.__objc_stubs: 0x11a60
   __DATA_CONST.__got: 0xbd0
   __DATA_CONST.__const: 0x4108
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f68
+  __DATA_CONST.__objc_selrefs: 0x5f80
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xb08
   __AUTH_CONST.__const: 0x2cf0
-  __AUTH_CONST.__cfstring: 0x6fe0
-  __AUTH_CONST.__objc_const: 0x28e28
+  __AUTH_CONST.__cfstring: 0x7000
+  __AUTH_CONST.__objc_const: 0x28e38
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: ADC04DB1-304D-3191-9AC8-1B156976095D
-  Functions: 6249
-  Symbols:   17822
-  CStrings:  8255
+  UUID: 8E3E6D22-CCAA-38FD-8A8A-52926BF9C69F
+  Functions: 6254
+  Symbols:   17834
+  CStrings:  8264
 
Symbols:
+ +[MTUserNotificationCenter setCommonContent:alert:hasPairedWatchSupportingAlarmKit:]
+ -[MTAlarmStorage dataStoreReady]
+ -[MTPairedDeviceListener hasActivePairedDeviceSupportingAlarmKit]
+ -[MTTimerStorage dataStoreReady]
+ -[MTUserNotificationCenter hasPairedWatchSupportingAlarmKit]
+ __OBJC_$_PROP_LIST_MTAlarmStorage.731
+ __OBJC_$_PROP_LIST_MTTimerStorage.329
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.368
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.317
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.390
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.390.cold.1
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.299
+ ___65-[MTPairedDeviceListener hasActivePairedDeviceSupportingAlarmKit]_block_invoke
+ ___block_literal_global.298
+ ___block_literal_global.312
+ ___block_literal_global.321
+ ___block_literal_global.376
+ ___block_literal_global.396
+ ___block_literal_global.400
+ ___block_literal_global.477
+ _objc_msgSend$hasActivePairedDeviceSupportingAlarmKit
+ _objc_msgSend$hasPairedWatchSupportingAlarmKit
+ _objc_msgSend$setCommonContent:alert:hasPairedWatchSupportingAlarmKit:
- +[MTUserNotificationCenter setCommonContent:alert:]
- GCC_except_table75
- GCC_except_table77
- __OBJC_$_PROP_LIST_MTAlarmStorage.733
- __OBJC_$_PROP_LIST_MTTimerStorage.328
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.371
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.320
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.393
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.393.cold.1
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.302
- ___block_literal_global.301
- ___block_literal_global.315
- ___block_literal_global.324
- ___block_literal_global.379
- ___block_literal_global.399
- ___block_literal_global.403
- ___block_literal_global.480
- _objc_msgSend$setCommonContent:alert:
CStrings:
+ "%{public}@ has active paired watch with AlarmKit capability"
+ "%{public}@ paired watch version is too old for custom AlarmKit alert"
+ "%{public}@ restoreFromDataStore"
+ "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
+ "dataStoreReady"
+ "hasActivePairedDeviceSupportingAlarmKit"
+ "hasPairedWatchSupportingAlarmKit"
+ "setCommonContent:alert:hasPairedWatchSupportingAlarmKit:"
+ "v36@0:8@16@24B32"
- "setCommonContent:alert:"

```
