## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x6b9b8
-  __TEXT.__objc_methlist: 0x77a4
+7027.2.13.0.0
+  __TEXT.__text: 0x6bfb8
+  __TEXT.__objc_methlist: 0x77e4
   __TEXT.__const: 0x328
-  __TEXT.__oslogstring: 0x9bfe
-  __TEXT.__cstring: 0x217d
+  __TEXT.__oslogstring: 0x9d82
+  __TEXT.__cstring: 0x2183
   __TEXT.__constg_swiftt: 0x104
   __TEXT.__swift5_typeref: 0x1c1
   __TEXT.__swift5_reflstr: 0x28b

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x148
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__unwind_info: 0x26c0
+  __TEXT.__gcc_except_tab: 0x84c
+  __TEXT.__unwind_info: 0x26f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c58
+  __DATA_CONST.__const: 0x1c78
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3420
+  __DATA_CONST.__objc_selrefs: 0x3450
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__got: 0xad0
-  __AUTH_CONST.__const: 0xf60
+  __DATA_CONST.__got: 0xad8
+  __AUTH_CONST.__const: 0xf80
   __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0xe4a0
+  __AUTH_CONST.__objc_const: 0xe4f0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0xbf8
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH.__objc_data: 0x720
-  __DATA.__objc_ivar: 0x4b8
-  __DATA.__data: 0x2348
+  __DATA.__objc_ivar: 0x4c0
+  __DATA.__data: 0x2368
   __DATA_DIRTY.__objc_ivar: 0xb4
   __DATA_DIRTY.__objc_data: 0x2970
-  __DATA_DIRTY.__data: 0x2f8
+  __DATA_DIRTY.__data: 0x2d8
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2734
-  Symbols:   5078
-  CStrings:  1045
+  Functions: 2744
+  Symbols:   5096
+  CStrings:  1052
 
Symbols:
+ -[HDSPEnvironment _updateStateIfPrepared]
+ -[HDSPWatchReadyProvider _startObservingInitialSync]
+ -[HDSPWatchReadyProvider dealloc]
+ -[HDSPWatchReadyProvider hasCompletedInitialSync]
+ -[HDSPWatchReadyProvider initWithEnvironment:springboardMonitor:hasCompletedInitialSync:]
+ -[HDSPWatchReadyProvider initialSyncDidComplete]
+ -[HDSPWatchReadyProvider observingInitialSync]
+ GCC_except_table45
+ GCC_except_table60
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterRemoveEveryObserver
+ _NPSHasCompletedInitialSync
+ _OBJC_IVAR_$_HDSPEnvironment._prepared
+ _OBJC_IVAR_$_HDSPWatchReadyProvider._hasCompletedInitialSync
+ _OBJC_IVAR_$_HDSPWatchReadyProvider._observingInitialSync
+ ___26-[HDSPEnvironment prepare]_block_invoke
+ ___41-[HDSPEnvironment _updateStateIfPrepared]_block_invoke
+ ___46-[HDSPWatchReadyProvider initWithEnvironment:]_block_invoke
+ ___52-[HDSPWatchReadyProvider _startObservingInitialSync]_block_invoke
+ ___54-[HDSPWatchReadyProvider _finishWaitingForInitialSync]_block_invoke
+ ___block_descriptor_32_e5_B8?0l
+ __handleInitialSyncNotification
+ _kNPSInitialSyncCompletionDarwinNotification
- -[HDSPEnvironment updateState]
- -[HDSPWatchReadyProvider observingRestore]
- GCC_except_table44
- _OBJC_IVAR_$_HDSPWatchReadyProvider._observingRestore
- ___30-[HDSPEnvironment updateState]_block_invoke
CStrings:
+ "B8@?0"
+ "[%{public}@] NPS completed initial sync."
+ "[%{public}@] NPS hasn't completed initial sync."
+ "[%{public}@] NPS initial sync completed"
+ "[%{public}@] Waiting for CSLSApplicationStateRestoredNotification or NPS initial sync completion"
+ "[%{public}@] not ready after prepare; re-checking for a waiting client"
+ "[%{public}@] received NPS initial sync notification, but NPS hasn't completed initial sync"
+ "\xf0\xf0a"
- "\xf0\xf0Q"
```
