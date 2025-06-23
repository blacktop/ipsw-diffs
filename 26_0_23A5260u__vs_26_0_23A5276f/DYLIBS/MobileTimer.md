## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2286.0.0.0.0
-  __TEXT.__text: 0xf4904
+2289.0.0.0.0
+  __TEXT.__text: 0xf4b60
   __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0xd510
-  __TEXT.__const: 0x11c0
-  __TEXT.__oslogstring: 0xf5f0
-  __TEXT.__cstring: 0x9406
+  __TEXT.__objc_methlist: 0xd520
+  __TEXT.__const: 0x11d0
+  __TEXT.__oslogstring: 0xf640
+  __TEXT.__cstring: 0x9426
   __TEXT.__gcc_except_tab: 0x1264
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x1a

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift_as_entry: 0x100
   __TEXT.__swift_as_ret: 0x104
-  __TEXT.__unwind_info: 0x4180
+  __TEXT.__unwind_info: 0x4170
   __TEXT.__eh_frame: 0x2ec0
   __TEXT.__objc_classname: 0x193b
-  __TEXT.__objc_methname: 0x17aec
+  __TEXT.__objc_methname: 0x17b1a
   __TEXT.__objc_methtype: 0x41e5
-  __TEXT.__objc_stubs: 0x11920
+  __TEXT.__objc_stubs: 0x11960
   __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x4118
+  __DATA_CONST.__const: 0x4108
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f18
+  __DATA_CONST.__objc_selrefs: 0x5f30
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xac0
   __AUTH_CONST.__const: 0x2c60
-  __AUTH_CONST.__cfstring: 0x6f40
+  __AUTH_CONST.__cfstring: 0x6f80
   __AUTH_CONST.__objc_const: 0x28de0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
-  - /System/Library/PrivateFrameworks/AlarmKitCore.framework/AlarmKitCore
   - /System/Library/PrivateFrameworks/AlarmKitFoundation.framework/AlarmKitFoundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BAFAA01A-6A54-3BDF-8B2E-3BFCEAE37B94
-  Functions: 6220
-  Symbols:   17786
-  CStrings:  8215
+  UUID: 20061DF9-8417-3F55-8461-BC7F23C82EC1
+  Functions: 6222
+  Symbols:   17787
+  CStrings:  8223
 
Symbols:
+ +[MTSleepUtilities alarmFromSleepOccurrence:scheduleEnabled:keepOffUntilDate:].cold.1
+ -[MTAlarm(MTScheduling) isRunningUnitTest]
+ _MTAlarmKitStopButtonLabel
+ __OBJC_$_PROP_LIST_MTAlarmStorage.723
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.371
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.320
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.383
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.383.cold.1
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.302
+ ___block_literal_global.301
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.379
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.470
+ _kMTAlarmMaxSnoozeDuration
+ _objc_msgSend$environment
+ _objc_msgSend$stopButtonLabel
+ _unitTestKey
- __OBJC_$_PROP_LIST_MTAlarmStorage.720
- ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.368
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.317
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.380
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.380.cold.1
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.299
- ___block_literal_global.298
- ___block_literal_global.312
- ___block_literal_global.321
- ___block_literal_global.376
- ___block_literal_global.386
- ___block_literal_global.390
- ___block_literal_global.467
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MobileTimer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MobileTimer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MobileTimer
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MobileTimer
CStrings:
+ "  \n \tlastModifiedDate: "
+ "%{public}@ Received invalid snooze duration from Sleep: %{public}f@. Defaulting to 9mins."
+ "ATP"
+ "MTAlarmKitStopButtonLabel"
+ "environment"
+ "isRunningUnitTest"
+ "stopButtonLabel"
- "   \n \tlastModifiedDate: "

```
