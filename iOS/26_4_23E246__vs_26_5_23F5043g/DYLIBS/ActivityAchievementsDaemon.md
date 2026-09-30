## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-2026.4.11.0.0
-  __TEXT.__text: 0x7efe0
+2026.5.1.0.0
+  __TEXT.__text: 0x7ed70
   __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_methlist: 0x60b4
+  __TEXT.__objc_methlist: 0x607c
   __TEXT.__const: 0x978
   __TEXT.__cstring: 0x61e1
   __TEXT.__gcc_except_tab: 0x2350
-  __TEXT.__oslogstring: 0x932d
+  __TEXT.__oslogstring: 0x92dd
   __TEXT.__swift5_typeref: 0x2f7
   __TEXT.__swift5_capture: 0x24
   __TEXT.__constg_swiftt: 0x180

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0x2450
+  __TEXT.__unwind_info: 0x2438
   __TEXT.__eh_frame: 0x3a8
   __TEXT.__objc_classname: 0xd0d
-  __TEXT.__objc_methname: 0x11d21
-  __TEXT.__objc_methtype: 0x2341
+  __TEXT.__objc_methname: 0x11d91
+  __TEXT.__objc_methtype: 0x2351
   __TEXT.__objc_stubs: 0xab00
   __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x2730

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37e0
+  __DATA_CONST.__objc_selrefs: 0x37e8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xc50
   __AUTH_CONST.__const: 0xc90
   __AUTH_CONST.__cfstring: 0x2cc0
-  __AUTH_CONST.__objc_const: 0x12028
+  __AUTH_CONST.__objc_const: 0x11fc8
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_ivar: 0x714
   __DATA.__data: 0x1088
   __DATA.__bss: 0xdf0
   __DATA_DIRTY.__objc_data: 0x1450

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 663670B3-BF65-3569-BDBE-4464FCC328EA
-  Functions: 2834
-  Symbols:   9357
-  CStrings:  4189
+  UUID: B8D06956-7468-32FC-BF73-834371C77430
+  Functions: 2828
+  Symbols:   9343
+  CStrings:  4190
 
Symbols:
+ -[ACHTinkerAwardingScheduler initWithHealthStore:assertionClient:systemTaskScheduler:dataStore:earnedInstanceStore:templateStore:awardingEngine:]
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.372
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.379
- -[ACHTinkerAwardingScheduler _cloudRestoreStatusDidChange:]
- -[ACHTinkerAwardingScheduler cloudSyncStatusProvider]
- -[ACHTinkerAwardingScheduler initWithHealthStore:assertionClient:cloudSyncStatusProvider:systemTaskScheduler:dataStore:earnedInstanceStore:templateStore:awardingEngine:]
- -[ACHTinkerAwardingScheduler setCloudSyncStatusProvider:]
- -[ACHTinkerAwardingScheduler setShouldRunImmediatelyOnCloudSyncCompletion:]
- -[ACHTinkerAwardingScheduler shouldRunImmediatelyOnCloudSyncCompletion]
- _OBJC_IVAR_$_ACHTinkerAwardingScheduler._cloudSyncStatusProvider
- _OBJC_IVAR_$_ACHTinkerAwardingScheduler._shouldRunImmediatelyOnCloudSyncCompletion
- ___59-[ACHTinkerAwardingScheduler _cloudRestoreStatusDidChange:]_block_invoke
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.374
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.381
CStrings:
+ "@72@0:8@16@24@32@40@48@56@64"
+ "initWithHealthStore:assertionClient:systemTaskScheduler:dataStore:earnedInstanceStore:templateStore:awardingEngine:"
- "[ACHTinkerAwardingScheduler] received cloud restore status change notification"

```
