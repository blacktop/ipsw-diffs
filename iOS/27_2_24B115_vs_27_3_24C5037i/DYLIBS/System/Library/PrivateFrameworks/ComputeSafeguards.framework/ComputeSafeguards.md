## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-177.40.5.0.0
-  __TEXT.__text: 0x5a3e8
+177.60.2.0.0
+  __TEXT.__text: 0x5a4ac
   __TEXT.__objc_methlist: 0x466c
   __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x6155
-  __TEXT.__gcc_except_tab: 0x10c4
-  __TEXT.__oslogstring: 0xf3aa
-  __TEXT.__unwind_info: 0x18a0
+  __TEXT.__cstring: 0x615d
+  __TEXT.__gcc_except_tab: 0x10cc
+  __TEXT.__oslogstring: 0xf38d
+  __TEXT.__unwind_info: 0x18a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x2a40
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x21e0
+  __DATA_CONST.__objc_arraydata: 0x21f0
   __DATA_CONST.__got: 0x328
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x6360
+  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__cfstring: 0x6380
   __AUTH_CONST.__objc_const: 0x61e0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x550

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 2073
-  Symbols:   2702
-  CStrings:  1877
+  Functions: 2076
+  Symbols:   2705
+  CStrings:  1878
 
Symbols:
+ GCC_except_table71
+ ___userActiveDeferredDaemons_block_invoke
+ _userActiveDeferredDaemons
+ _userActiveDeferredDaemons.daemons
+ _userActiveDeferredDaemons.onceToken
- GCC_except_table56
- GCC_except_table58
Functions:
~ -[CSMitigationManager handleDetectionViolation:forCSProcess:coalitionID:coalitionName:pid:startTime:endTime:forcedMitigation:mitigationSuggestion:withMitigationDecisionType:withMitigationDecisionReason:withError:] : 6828 -> 6868
+ _userActiveDeferredDaemons
+ ___userActiveDeferredDaemons_block_invoke
~ _OUTLINED_FUNCTION_23 : 20 -> 12
~ _OUTLINED_FUNCTION_24 : 12 -> 20
+ _userActiveDeferredDaemons.cold.1
CStrings:
+ "assetsd"
+ "handleDetectionViolation: Deferred bgQoS (user active); will restore when user becomes idle for process:%@"
+ "handleDetectionViolation: Skipped fatal (user active); incremented fatal counter for process:%@"
+ "handleDetectionViolation: user active, deferring mitigation decision for %@ instead of skipping."
- "handleDetectionViolation: Deferred bgQoS for searchd (user active); will restore when user becomes idle for process:%@"
- "handleDetectionViolation: Skipped fatal for searchd (user active); incremented fatal counter for process:%@"
- "handleDetectionViolation: user active, deferring mitigation decision for searchd instead of skipping."
```
