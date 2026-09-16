## CompanionHealthDaemon

> `/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon`

```diff

-2027.0.123.1.10
-  __TEXT.__text: 0x73b4
-  __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x4d1
-  __TEXT.__gcc_except_tab: 0x284
-  __TEXT.__oslogstring: 0xcba
-  __TEXT.__unwind_info: 0x2d8
+2027.1.35.0.0
+  __TEXT.__text: 0x7a44
+  __TEXT.__objc_methlist: 0x69c
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x510
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__oslogstring: 0xe3f
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x840
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x2a0
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x1bb0
+  __DATA_CONST.__got: 0x2b0
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1bd0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 144
-  Symbols:   654
-  CStrings:  109
+  Functions: 155
+  Symbols:   673
+  CStrings:  116
 
Symbols:
+ -[CHFitnessAppBadgeManager _handleBadgeRefreshTask:]
+ -[CHFitnessAppBadgeManager _launchFitnessAppWithCompletion:]
+ -[CHFitnessAppBadgeManager _scheduleFitnessAppLaunch]
+ GCC_except_table0
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_IVAR_$_CHFitnessAppBadgeManager._consecutiveLaunchFailureCount
+ ___32-[CHFitnessAppBadgeManager init]_block_invoke
+ ___52-[CHFitnessAppBadgeManager _handleBadgeRefreshTask:]_block_invoke
+ ___60-[CHFitnessAppBadgeManager _launchFitnessAppWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32w_e22_v16?0"BGSystemTask"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e37_v24?0"BSProcessHandle"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ _objc_msgSend$_handleBadgeRefreshTask:
+ _objc_msgSend$_launchFitnessAppWithCompletion:
+ _objc_msgSend$_scheduleFitnessAppLaunch
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$submitTaskRequest:error:
- -[CHFitnessAppBadgeManager _launchFitnessApp]
- ___45-[CHFitnessAppBadgeManager _launchFitnessApp]_block_invoke
- ___block_descriptor_32_e37_v24?0"BSProcessHandle"8"NSError"16l
- _objc_msgSend$_launchFitnessApp
CStrings:
+ "FitnessAppBadgeManager failed to register badge-refresh background task"
+ "FitnessAppBadgeManager failed to reschedule badge-refresh task after launch error: %@"
+ "FitnessAppBadgeManager failed to submit badge-refresh task request: %@"
+ "FitnessAppBadgeManager giving up on badge-refresh launch after %lu consecutive failures"
+ "FitnessAppBadgeManager scheduling deferred badge-refresh launch via DAS"
+ "com.apple.healthd.fitness-badge-refresh"
+ "v16@?0@\"BGSystemTask\"8"
```
