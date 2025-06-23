## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 38.0.0.0.0
-  __TEXT.__text: 0x12f78
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_stubs: 0x1760
-  __TEXT.__objc_methlist: 0xc34
+  __TEXT.__text: 0x13908
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x73ed
+  __TEXT.__cstring: 0x74e9
   __TEXT.__oslogstring: 0x34d
-  __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x1701
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__objc_methname: 0x17dc
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x789
-  __TEXT.__unwind_info: 0x518
-  __DATA_CONST.__auth_got: 0x748
+  __TEXT.__unwind_info: 0x560
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x36a0
+  __DATA_CONST.__cfstring: 0x36c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x12b0
-  __DATA.__objc_selrefs: 0x708
-  __DATA.__objc_ivar: 0xd4
+  __DATA.__objc_const: 0x1340
+  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x5e8
   __DATA.__bss: 0xc8

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBFCC9F3-32CB-3581-90CE-996AC4F31082
-  Functions: 478
-  Symbols:   291
-  CStrings:  1793
+  UUID: 2D896BD1-EE90-354E-BA23-01A64CF2DF2C
+  Functions: 497
+  Symbols:   294
+  CStrings:  1814
 
Symbols:
+ ___assert_rtn
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "CHECKPOINT_INTERNAL_ERROR(%s): unable to create step ID number for tolerated failure lookup\n"
+ "CheckpointEngineErrorDomain"
+ "TB,V_isCanceled"
+ "T^v,N,V_awaitDescription"
+ "T^v,N,V_stepDescription"
+ "_awaitDescription"
+ "_isCanceled"
+ "_stepDescription"
+ "awaitDescription"
+ "cancel"
+ "checkpoint_chassis_set_global_async_error"
+ "checkpoint_engine_set_async_error"
+ "checkpoint_tolerated_get_failed_entry"
+ "chip-epoch"
+ "failingStep"
+ "isCanceled"
+ "ramrod_checkpoint.c"
+ "setAwaitDescription:"
+ "setIsCanceled:"
+ "setStepDescription:"
+ "stepDescription"
- "certificate-security-mode"

```
