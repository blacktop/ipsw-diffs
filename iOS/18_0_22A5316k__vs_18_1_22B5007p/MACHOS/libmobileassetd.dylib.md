## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.0.0.0.8
-  __TEXT.__text: 0x259004
-  __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_stubs: 0x1f000
-  __TEXT.__objc_methlist: 0xea10
+1309.40.0.502.1
+  __TEXT.__text: 0x258284
+  __TEXT.__auth_stubs: 0x2380
+  __TEXT.__objc_stubs: 0x1efa0
+  __TEXT.__objc_methlist: 0xe9f8
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x35653
-  __TEXT.__cstring: 0x4b8dc
+  __TEXT.__objc_methname: 0x35604
+  __TEXT.__cstring: 0x4b86c
   __TEXT.__objc_classname: 0xd50
   __TEXT.__objc_methtype: 0x32ad
-  __TEXT.__oslogstring: 0x32589
-  __TEXT.__gcc_except_tab: 0x24c8
+  __TEXT.__oslogstring: 0x31d88
+  __TEXT.__gcc_except_tab: 0x2518
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4680
+  __TEXT.__unwind_info: 0x4668
   __TEXT.__eh_frame: 0x30c4
-  __DATA_CONST.__auth_got: 0x11c8
+  __DATA_CONST.__auth_got: 0x11d0
   __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6488
-  __DATA_CONST.__cfstring: 0x309e0
+  __DATA_CONST.__const: 0x6460
+  __DATA_CONST.__cfstring: 0x30940
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8860
+  __DATA_CONST.__objc_selrefs: 0x8850
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x918
   __DATA_CONST.__objc_arrayobj: 0x198

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8133
-  Symbols:   14531
-  CStrings:  15550
+  Functions: 8127
+  Symbols:   14523
+  CStrings:  15527
 
Symbols:
+ -[MADAutoAssetScheduler _startPushDelayTimer:]
+ GCC_except_table54
+ GCC_except_table88
+ ___46-[MADAutoAssetScheduler _startPushDelayTimer:]_block_invoke
+ __block_literal_global.1107
+ _dispatch_source_cancel
+ _objc_msgSend$_startPushDelayTimer:
- -[MADAutoAssetScheduler _performPushNotificationActivityOperations]
- -[MADAutoAssetScheduler _registerForAndStartPushActivity:]
- -[MADAutoAssetScheduler _startPushBackupTrigger]
- GCC_except_table94
- __58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.1067
- ___48-[MADAutoAssetScheduler _startPushBackupTrigger]_block_invoke
- ___48-[MADAutoAssetScheduler _startPushBackupTrigger]_block_invoke_2
- ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke
- ___67-[MADAutoAssetScheduler _performPushNotificationActivityOperations]_block_invoke
- ___block_descriptor_48_e8_32s_e17_v16?0"NSTimer"8ls32l8
- __block_literal_global.1116
- _objc_msgSend$_performPushNotificationActivityOperations
- _objc_msgSend$_registerForAndStartPushActivity:
- _objc_msgSend$_startPushBackupTrigger
- _objc_msgSend$setPushJobsXPCActivity:
CStrings:
+ "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} push delay timer DISABLED"
+ "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} push delay timer | ...pushing"
+ "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} push delay timer | pushing..."
+ "CrystalBSeed"
+ "Starting built-in MobileAsset brain built Jul 19 2024 18:02:56"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Jul 19 2024 18:02:56"
+ "_startPushDelayTimer:"
+ "com.apple.MobileAsset.handlePushNotificationReceived"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} 1-shot XPC activity | ...pushing"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} 1-shot XPC activity | pushing..."
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} ...xpc_activity_register"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity DISABLED with previous delayPeriod:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity activated with desired pushDelay:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity re-activated with overridden delayPeriod:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity re-activated with previously desired pushDelay:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity started with pushDelay:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity without criteria (and no pushDelay provided - push triggering DISABLED"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_registerForAndStartPushActivity} xpc_activity_register..."
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} backup push trigger DISABLED"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} backup push trigger not needed - push triggered by XPC activity"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} backup push trigger | ...pushing"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_startPushBackupTrigger} backup push trigger | pushing..."
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:resumeFromPersisted} registering auto-asset-scheduler.push-notifications XPC Activity for 1-shot started by earlier MobileAsset daemon instance | pushDelay:%!{(MISSING)public}@"
- "CrystalSeed"
- "Starting built-in MobileAsset brain built Jul 12 2024 11:53:29"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Jul 12 2024 11:53:29"
- "[XPC] {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity | ...XPC_ACTIVITY_STATE_CHECK_IN"
- "[XPC] {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity | ...XPC_ACTIVITY_STATE_RUN"
- "[XPC] {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity | XPC_ACTIVITY_STATE_CHECK_IN..."
- "[XPC] {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity | XPC_ACTIVITY_STATE_RUN..."
- "[XPC] {AUTO-SCHEDULER:_registerForAndStartPushActivity} 1-shot XPC activity | xpc_activity_state_t state:%!l(MISSING)d"
- "_registerForAndStartPushActivity"
- "_registerForAndStartPushActivity:"
- "_startPushBackupTrigger"
- "com.apple.mobileassetd.auto-asset-scheduler.push-notifications"
- "push-delay now in use"
- "push-delay of 0 (DISABLED)"
- "pushTriggerSecs"

```
