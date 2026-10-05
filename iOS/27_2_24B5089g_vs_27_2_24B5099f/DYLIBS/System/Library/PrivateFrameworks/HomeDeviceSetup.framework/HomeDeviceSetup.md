## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-405.10.29.0.0
-  __TEXT.__text: 0x70abc
-  __TEXT.__objc_methlist: 0x3474
-  __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x1a864
+405.10.34.1.1
+  __TEXT.__text: 0x71258
+  __TEXT.__objc_methlist: 0x3494
+  __TEXT.__const: 0x488
+  __TEXT.__cstring: 0x1aac4
   __TEXT.__oslogstring: 0x81d
-  __TEXT.__gcc_except_tab: 0x294
+  __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xd3
   __TEXT.__swift5_reflstr: 0x8b

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x2568
+  __TEXT.__unwind_info: 0x25a8
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1960
+  __DATA_CONST.__const: 0x19d8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dc0
+  __DATA_CONST.__objc_selrefs: 0x2e10
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x230
-  __DATA_CONST.__got: 0x410
-  __AUTH_CONST.__const: 0xc18
-  __AUTH_CONST.__cfstring: 0x5580
+  __DATA_CONST.__got: 0x418
+  __AUTH_CONST.__const: 0xc58
+  __AUTH_CONST.__cfstring: 0x5600
   __AUTH_CONST.__objc_const: 0x78a8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3069
-  Symbols:   3336
-  CStrings:  3113
+  Functions: 3080
+  Symbols:   3348
+  CStrings:  3127
 
Symbols:
+ -[HDSSetupService _applySetupTimeIfClockImplausible:]
+ -[HDSSetupSession _shouldTransferLoggingProfile]
+ GCC_except_table379
+ GCC_except_table429
+ _OBJC_CLASS_$_NSDateFormatter
+ __HDSBuildDateFloor.sFloor
+ __HDSBuildDateFloor.sOnce
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_6
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_7
+ ____HDSBuildDateFloor_block_invoke
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- GCC_except_table426
CStrings:
+ "  "
+ "-[HDSSetupService _applySetupTimeIfClockImplausible:]"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_4"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_7"
+ "<BUILD_TIMESTAMP>"
+ "Clock %@ predates build, applying setup time %@ (%@)\n"
+ "Ignoring setup time %@, predates build floor %@\n"
+ "Logging Profile install failed, logging will stay disabled\n"
+ "Logging Profile unreadable at %@, logging will stay disabled\n"
+ "Logging profile transfer timed out"
+ "MMM d yyyy"
+ "No build date floor, not applying setup time %@\n"
+ "_startSysDropLoggingProfileRequest timed out after %g s\n"
+ "_startSysDropLoggingProfileRequest timeout fired but transfer state is %d, ignoring\n"
+ "en_US_POSIX"
- "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_5"
```
