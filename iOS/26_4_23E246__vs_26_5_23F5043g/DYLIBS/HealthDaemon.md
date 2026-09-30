## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.5.85.2.2
-  __TEXT.__text: 0x7e24e0
+6200.6.4.0.0
+  __TEXT.__text: 0x7e2f70
   __TEXT.__auth_stubs: 0x4b20
-  __TEXT.__objc_methlist: 0x441bc
+  __TEXT.__objc_methlist: 0x441d4
   __TEXT.__const: 0x1fd38
   __TEXT.__dlopen_cstrs: 0x15b
   __TEXT.__constg_swiftt: 0x1288

   __TEXT.__swift5_reflstr: 0x7eb
   __TEXT.__swift5_fieldmd: 0xac4
   __TEXT.__swift5_types: 0x10c
-  __TEXT.__cstring: 0x7cf15
+  __TEXT.__cstring: 0x7cefb
   __TEXT.__swift5_capture: 0x7b8
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_proto: 0x1ac
-  __TEXT.__oslogstring: 0x42d94
+  __TEXT.__oslogstring: 0x42d57
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__gcc_except_tab: 0x3a428
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1e878
+  __TEXT.__unwind_info: 0x1e868
   __TEXT.__eh_frame: 0x17f0
-  __TEXT.__objc_classname: 0xd106
-  __TEXT.__objc_methname: 0x90139
-  __TEXT.__objc_methtype: 0x1766a
-  __TEXT.__objc_stubs: 0x51140
+  __TEXT.__objc_classname: 0xd10e
+  __TEXT.__objc_methname: 0x90159
+  __TEXT.__objc_methtype: 0x17676
+  __TEXT.__objc_stubs: 0x51160
   __DATA_CONST.__got: 0x5660
   __DATA_CONST.__const: 0x1d548
   __DATA_CONST.__objc_classlist: 0x2a10
   __DATA_CONST.__objc_catlist: 0x4c8
   __DATA_CONST.__objc_protolist: 0x9e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a0b0
+  __DATA_CONST.__objc_selrefs: 0x1a0b8
   __DATA_CONST.__objc_protorefs: 0x200
   __DATA_CONST.__objc_superrefs: 0x1d80
-  __DATA_CONST.__objc_arraydata: 0x84a0
+  __DATA_CONST.__objc_arraydata: 0x84f8
   __AUTH_CONST.__auth_got: 0x25a8
-  __AUTH_CONST.__const: 0x10958
-  __AUTH_CONST.__cfstring: 0x3da80
+  __AUTH_CONST.__const: 0x10938
+  __AUTH_CONST.__cfstring: 0x3dc40
   __AUTH_CONST.__objc_const: 0x7e070
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x3e88
-  __AUTH_CONST.__objc_arrayobj: 0x1ed8
+  __AUTH_CONST.__objc_arrayobj: 0x1ef0
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH.__objc_data: 0xd588
   __AUTH.__data: 0x7b8
   __DATA.__objc_ivar: 0x446c
   __DATA.__data: 0x7fa8
-  __DATA.__bss: 0x2b50
+  __DATA.__bss: 0x2b58
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_ivar: 0xe20
   __DATA_DIRTY.__objc_data: 0xe3b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 96AEB735-4809-3BCE-BE23-CDF6A1A757BD
+  UUID: 2924F16A-9C4B-39F0-BBE6-BDE1673CDD89
   Functions: 35439
-  Symbols:   105472
-  CStrings:  44492
+  Symbols:   105473
+  CStrings:  44523
 
Symbols:
+ +[HDDatabaseTransaction(Logging) hk_processQueueNameForLogging:]
+ __OBJC_$_CLASS_METHODS_HDDatabaseTransaction(Logging)
+ ___83-[HDDatabaseTransaction logTransactionEndIfNecessary:transactionStartTime:context:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ _getAllowedStrings.strings
+ _objc_msgSend$hk_processQueueNameForLogging:
- ___59-[HDWorkoutLocationSmoother _showTTRAlertForTask:duration:]_block_invoke
- ___85-[HDWorkoutLocationSmoother _handleAlertResponse:selectedButton:task:duration:error:]_block_invoke
- ___block_descriptor_56_e8_32s40w_e43_v32?0"HDUserNotification"8q16"NSError"24lw40l8s32l8
- ___block_literal_global.510
CStrings:
+ "%{public}@: Observer timed out waiting (%0.1f) for %{public}@"
+ "%{public}@: observer %@ returned when not in progress and missed the analytics send."
+ "%{public}@:%@ observer unsuccessful (%ld)"
+ "3rd Party BundleId"
+ "@24@0:8r*16"
+ "Fitness"
+ "HealthBalanceWidgetExtension"
+ "Logging"
+ "Long database transaction %{public}@ duration: duration=%{public}@, wait=%{public}@, work=%{public}@, write=%{BOOL}d, protected=%{BOOL}d, priority=%{BOOL}d, cache=%ld, journal=%ld, queue=%{sensitive}s"
+ "Research"
+ "SleepWidgetExtension"
+ "activityawardsd"
+ "activitysharingd"
+ "apple"
+ "audioaccessoryd"
+ "com"
+ "com.apple.HealthKit.unnamed queue"
+ "com.apple.healthd-orchestration"
+ "com.apple.healthd.transactions"
+ "fitcored"
+ "healthappd"
+ "hk_processQueueNameForLogging:"
+ "sleepd"
+ "waitDuration"
+ "workDuration"
- "%{public}@: Route smoothing TTR alert: 'Tap-to-Radar' button pressed"
- "%{public}@: Smoothing TTR alert: 'Not Now' button pressed"
- "%{public}@: Timeout (%0.1f) waiting for %{public}@"
- "%{public}@: observer %@ returned when not in progress. It missed the send."
- "<Workout UUID=%@ \ntotalLocations=%tu \nTask Creation Date=%@ \nTask Start Date=%@ \nAttempts=%lu \nPrevious Attempts Error=%@ \nError=%@>"
- "Long database transaction %{public}@ duration: duration=%{public}@, wait=%{public}@, work=%{public}@, write=%{BOOL}d, protected=%{BOOL}d, priority=%{BOOL}d, cache=%ld, journal=%ld, queue=%{public}s"
- "Route Smoothing Issue Detected"
- "Route Smoothing took %f seconds to complete"
- "Route Smoothing took over %f seconds to complete"
- "TimeOut: %f seconds \nTaskDuration: %f seconds \n\nDevice: %@ \n\nTask:\n%@ \n\nWorkout: %@"

```
