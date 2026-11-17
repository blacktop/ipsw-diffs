## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2333.3.4.0.0
-  __TEXT.__text: 0x12f1e4
-  __TEXT.__objc_methlist: 0xeb54
-  __TEXT.__const: 0x2200
-  __TEXT.__gcc_except_tab: 0x1248
-  __TEXT.__cstring: 0x9a42
-  __TEXT.__oslogstring: 0x13213
+2333.3.6.0.0
+  __TEXT.__text: 0x130ba8
+  __TEXT.__objc_methlist: 0xec6c
+  __TEXT.__const: 0x2210
+  __TEXT.__gcc_except_tab: 0x1244
+  __TEXT.__cstring: 0x9ab2
+  __TEXT.__oslogstring: 0x13293
   __TEXT.__dlopen_cstrs: 0x9dd
   __TEXT.__ustring: 0x2c
   __TEXT.__swift5_typeref: 0x114c

   __TEXT.__swift_as_cont: 0x4d0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6d50
+  __TEXT.__unwind_info: 0x6dc8
   __TEXT.__eh_frame: 0x50c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4a00
-  __DATA_CONST.__objc_classlist: 0x728
+  __DATA_CONST.__const: 0x4a08
+  __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68c0
+  __DATA_CONST.__objc_selrefs: 0x6908
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0xd20
   __AUTH_CONST.__const: 0x5ce8
-  __AUTH_CONST.__cfstring: 0x75e0
-  __AUTH_CONST.__objc_const: 0x2c518
+  __AUTH_CONST.__cfstring: 0x7640
+  __AUTH_CONST.__objc_const: 0x2c6d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xe70
-  __AUTH.__objc_data: 0x3898
+  __AUTH.__objc_data: 0x38e8
   __AUTH.__data: 0x7b0
-  __DATA.__objc_ivar: 0xa1c
+  __DATA.__objc_ivar: 0xa34
   __DATA.__data: 0x30b0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__bss: 0x240
+  - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7933
-  Symbols:   10002
-  CStrings:  2879
+  Functions: 7982
+  Symbols:   10061
+  CStrings:  2886
 
Symbols:
+ +[MTAppEntityDonor isAppIntentsSupportAvailable]
+ +[MTAppEntityDonor isLinwoodAvailable]
+ +[MTAppEntityDonor registerSpotlightClient:]
+ -[MTAppEntityDonor _queue_migrateIndexIfNeeded]
+ -[MTAppEntityDonor _queue_migrateIndex]
+ -[MTAppEntityDonor _queue_needsIndexMigration]
+ -[MTAppEntityDonor _queue_persistIndexVersion]
+ -[MTAppEntityDonor _queue_reindexAllItems]
+ -[MTAppEntityDonor initWithAlarmStorage:timerStorage:persistence:]
+ -[MTAppEntityDonor persistence]
+ -[MTAppEntityDonor serializerQueue]
+ -[MTAppEntityDonor serializer]
+ -[MTTimerService .cxx_destruct]
+ -[MTTimerService addTimer:withCompletion:]
+ -[MTTimerService dismissTimerWithIdentifier:withCompletion:]
+ -[MTTimerService getTimerDurationsWithCompletion:]
+ -[MTTimerService getTimersWithCompletion:]
+ -[MTTimerService initWithStorage:]
+ -[MTTimerService metrics]
+ -[MTTimerService removeTimer:withCompletion:]
+ -[MTTimerService serializer]
+ -[MTTimerService storage]
+ -[MTTimerService updateTimer:withCompletion:]
+ -[MTTimerService whenReady:]
+ GCC_except_table58
+ _OBJC_CLASS_$_MTTimerService
+ _OBJC_IVAR_$_MTAppEntityDonor._persistence
+ _OBJC_IVAR_$_MTAppEntityDonor._serializer
+ _OBJC_IVAR_$_MTAppEntityDonor._serializerQueue
+ _OBJC_IVAR_$_MTTimerService._metrics
+ _OBJC_IVAR_$_MTTimerService._serializer
+ _OBJC_IVAR_$_MTTimerService._storage
+ _OBJC_METACLASS_$_MTTimerService
+ __OBJC_$_CLASS_METHODS_MTAppEntityDonor
+ __OBJC_$_INSTANCE_METHODS_MTTimerService
+ __OBJC_$_INSTANCE_VARIABLES_MTTimerService
+ __OBJC_$_PROP_LIST_MTTimerService
+ __OBJC_CLASS_RO_$_MTTimerService
+ __OBJC_METACLASS_RO_$_MTTimerService
+ ___28-[MTTimerService whenReady:]_block_invoke
+ ___37-[MTAppEntityDonor handleSystemReady]_block_invoke
+ ___40-[MTAppEntityDonor source:didAddTimers:]_block_invoke
+ ___40-[MTAppEntityDonor source:didFireTimer:]_block_invoke
+ ___42-[MTTimerService addTimer:withCompletion:]_block_invoke
+ ___42-[MTTimerService getTimersWithCompletion:]_block_invoke
+ ___43-[MTAppEntityDonor source:didDismissTimer:]_block_invoke
+ ___43-[MTAppEntityDonor source:didRemoveAlarms:]_block_invoke
+ ___43-[MTAppEntityDonor source:didRemoveTimers:]_block_invoke
+ ___43-[MTAppEntityDonor source:didUpdateTimers:]_block_invoke
+ ___45-[MTTimerService removeTimer:withCompletion:]_block_invoke
+ ___45-[MTTimerService updateTimer:withCompletion:]_block_invoke
+ ___47-[MTAppEntityDonor _queue_migrateIndexIfNeeded]_block_invoke
+ ___47-[MTAppEntityDonor _queue_migrateIndexIfNeeded]_block_invoke_2
+ ___47-[MTAppEntityDonor _queue_migrateIndexIfNeeded]_block_invoke_3
+ ___50-[MTTimerService getTimerDurationsWithCompletion:]_block_invoke
+ ___52-[MTAppEntityDonor source:didFireAlarm:triggerType:]_block_invoke
+ ___57-[MTAppEntityDonor handleNotification:ofType:completion:]_block_invoke
+ ___57-[MTAppEntityDonor source:didDismissAlarm:dismissAction:]_block_invoke
+ ___60-[MTTimerService dismissTimerWithIdentifier:withCompletion:]_block_invoke
+ ___86-[MTAppEntityDonor reindexAllItemsForBundleID:protectionClass:acknowledgementHandler:]_block_invoke
+ _kMTAppEntityIndexVersion
+ _kMTAppEntityIndexVersionKey
- -[MTAppEntityDonor initWithAlarmStorage:timerStorage:]
- -[MTAppEntityDonor reindexAllItems]
- GCC_except_table2
CStrings:
+ "%{public}@ migrated index to version %f"
+ "%{public}@ migrating index to version %f"
+ "%{public}@ store not loaded, dropping index migration"
+ "MTAppEntityIndexVersion"
+ "MTTimerService.m"
+ "com.apple.MTAppEntityDonor.serial"
+ "com.apple.MTTimerService.access-queue"
```
