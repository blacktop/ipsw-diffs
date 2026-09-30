## SensingPredictServices

> `/System/Library/PrivateFrameworks/SensingPredictServices.framework/Versions/A/SensingPredictServices`

```diff

 10.10.0.0.0
-  __TEXT.__text: 0x1798
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__text: 0x1900
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_methlist: 0x270
   __TEXT.__cstring: 0x4b4
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xf0
   __TEXT.__objc_classname: 0x62
   __TEXT.__objc_methname: 0x5ad
   __TEXT.__objc_methtype: 0x17b

   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x5c0
+  __AUTH_CONST.__objc_const: 0x4f8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1f0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C2A9CAC-DA37-3210-9B5F-8AD3B47AE95E
-  Functions: 52
-  Symbols:   186
+  UUID: 904C8862-D44E-31B8-BC79-30ACEE7B3E72
+  Functions: 70
+  Symbols:   205
   CStrings:  171
 
Symbols:
+ -[SPContextMonitor _activate:].cold.1
+ -[SPContextMonitor _ensureXPCStarted].cold.1
+ -[SPContextMonitor _interrupted].cold.1
+ -[SPContextMonitor _invalidated].cold.1
+ -[SPContextMonitor _invalidated].cold.2
+ -[SPContextMonitor _reportError:].cold.1
+ -[SPContextMonitor contextMonitorContextChanged:].cold.1
+ -[SPContextMonitor contextSignalUpdated:fusedState:].cold.1
+ -[SPContextMonitor init].cold.1
+ -[SPContextMonitor isSystemContext].cold.1
+ SPXPCGetNextClientID.cold.1
+ _OUTLINED_FUNCTION_0
+ __30-[SPContextMonitor _activate:]_block_invoke.14.cold.1
+ __30-[SPContextMonitor _activate:]_block_invoke.14.cold.2
+ __30-[SPContextMonitor _activate:]_block_invoke.cold.1
+ __30-[SPContextMonitor _activate:]_block_invoke.cold.2
+ __30-[SPContextMonitor invalidate]_block_invoke.cold.1
+ __43-[SPContextMonitor activateWithCompletion:]_block_invoke.cold.1
+ _objc_retainAutoreleaseReturnValue
Functions:
~ -[SPContext descriptionWithLevel:] : 252 -> 248
~ _SPXPCGetNextClientID : 80 -> 64
~ -[SPContextMonitor init] : 172 -> 156
~ -[SPContextMonitor setContextChangeFlags:] : 172 -> 176
~ -[SPContextMonitor description] : 80 -> 76
~ ___43-[SPContextMonitor activateWithCompletion:]_block_invoke : 292 -> 256
~ -[SPContextMonitor _activate:] : 624 -> 600
~ ___30-[SPContextMonitor _activate:]_block_invoke : 252 -> 192
~ __30-[SPContextMonitor _activate:]_block_invoke.14 : 392 -> 336
~ -[SPContextMonitor _ensureXPCStarted] : 636 -> 616
~ -[SPContextMonitor _interrupted] : 236 -> 208
~ ___30-[SPContextMonitor invalidate]_block_invoke : 320 -> 280
~ -[SPContextMonitor contextMonitorContextChanged:] : 196 -> 156
~ -[SPContextMonitor contextSignalUpdated:fusedState:] : 212 -> 172
~ -[SPContextMonitor _invalidated] : 432 -> 376
~ -[SPContextMonitor isSystemContext] : 68 -> 56
~ -[SPContextMonitor _reportError:] : 220 -> 184

```
