## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-2109.2.1.0.0
-  __TEXT.__text: 0x13388
-  __TEXT.__auth_stubs: 0x620
+2109.40.8.0.0
+  __TEXT.__text: 0x135ac
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x1264
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xa35
-  __TEXT.__oslogstring: 0x1fc5
-  __TEXT.__gcc_except_tab: 0x758
+  __TEXT.__cstring: 0xa7d
+  __TEXT.__oslogstring: 0x2013
+  __TEXT.__gcc_except_tab: 0x738
   __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x266
-  __TEXT.__objc_methname: 0x3d4c
+  __TEXT.__objc_methname: 0x3da3
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__objc_stubs: 0x25a0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__objc_stubs: 0x2620
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x698
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc18
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__cfstring: 0xf00
   __AUTH_CONST.__objc_const: 0x2860
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4EB7548C-297C-341E-8B02-48F369F24A23
-  Functions: 516
-  Symbols:   1871
-  CStrings:  1115
+  UUID: 5AC19116-A1DB-3958-B441-8A3F55E775F3
+  Functions: 517
+  Symbols:   1879
+  CStrings:  1128
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.126
+ ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.142
+ ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.140
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.cold.2
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke_2
+ ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke_2.cold.1
+ ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.143
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$integerValue
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$processInfo
+ _objc_msgSend$suspensionDelayMitigationsForActivity:
+ _objc_retain_x27
+ _objc_retain_x28
- GCC_except_table55
- ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.113
- ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.129
- ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.127
- ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.112
- ___63-[BGSystemTaskScheduler expireTaskWithRegistration:withReason:]_block_invoke.112.cold.1
- ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.130
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
CStrings:
+ "%@ was expired %lds ago, but hasn't responded yet"
+ "%@: Applying Suspension Delay Mitigations: Since version %@.%@, Threshold %@"
+ "Major"
+ "Minor"
+ "Threshold"
+ "integerValue"
+ "operatingSystemVersion"
+ "processInfo"
+ "suspensionDelayMitigationsForActivity:"
- "%@ was expired %ds ago, but hasn't responded yet"

```
