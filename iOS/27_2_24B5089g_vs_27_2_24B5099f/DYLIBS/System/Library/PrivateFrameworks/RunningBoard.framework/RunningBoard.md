## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-1084.40.6.0.0
-  __TEXT.__text: 0x789d0
-  __TEXT.__objc_methlist: 0x640c
+1084.40.7.0.0
+  __TEXT.__text: 0x78bd0
+  __TEXT.__objc_methlist: 0x6414
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x7d46
-  __TEXT.__oslogstring: 0xba9e
+  __TEXT.__cstring: 0x7d83
+  __TEXT.__oslogstring: 0xbad9
   __TEXT.__gcc_except_tab: 0xbac
-  __TEXT.__unwind_info: 0x25a8
+  __TEXT.__unwind_info: 0x25b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x178
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f50
+  __DATA_CONST.__objc_selrefs: 0x2f60
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x770
   __DATA_CONST.__got: 0x7a0
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__cfstring: 0x6c80
   __AUTH_CONST.__objc_const: 0xdbb0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x488

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2826
+  Functions: 2827
   Symbols:   4895
-  CStrings:  1860
+  CStrings:  1863
 
Symbols:
+ -[RBSLaunchContext(RBLaunchChecks) _installationHoldActive:]
+ GCC_except_table38
+ GCC_except_table54
- GCC_except_table17
- GCC_except_table37
- GCC_except_table53
Functions:
~ __addRBProperties : 1172 -> 1228
~ _OUTLINED_FUNCTION_5 : 12 -> 16
~ _OUTLINED_FUNCTION_5 : 16 -> 20
~ _OUTLINED_FUNCTION_5 : 20 -> 28
~ _OUTLINED_FUNCTION_5 : 28 -> 32
- _OUTLINED_FUNCTION_5
~ -[RBSLaunchContext(RBLaunchChecks) _passesPreflightChecksWithError:] : 476 -> 592
+ -[RBSLaunchContext(RBLaunchChecks) _installationHoldActive:]
~ -[RBSLaunchContext(RBLaunchChecks) _preflightEligibility:].cold.2 : 84 -> 72
+ -[RBSLaunchContext(RBLaunchChecks) _installationHoldActive:].cold.1
~ ___70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.cold.1 : 88 -> 76
~ ___70-[RBProcessManager _enqueueGuaranteedRunningLaunchForIdentity:atTime:]_block_invoke.cold.2 : 84 -> 88
~ -[RBProcessManager _resolveProcessWithIdentifier:auditToken:properties:].cold.1 : 84 -> 88
CStrings:
+ "Launch prevented due to active installation hold"
+ "_BundlePath"
+ "unable to find extension record for %{public}@: %{public}@"
```
