## spinandd

> `/usr/libexec/spinandd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0x10b14
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x42c
-  __TEXT.__const: 0x5e0
-  __TEXT.__objc_methname: 0xcb6
-  __TEXT.__cstring: 0x40c3
+149.40.3.0.0
+  __TEXT.__text: 0x11f54
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x464
+  __TEXT.__const: 0x640
+  __TEXT.__objc_methname: 0xd71
+  __TEXT.__cstring: 0x4448
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methtype: 0x3b3
-  __TEXT.__oslogstring: 0xcbe
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__cfstring: 0x400
+  __TEXT.__objc_methtype: 0x3cf
+  __TEXT.__oslogstring: 0xd80
+  __TEXT.__unwind_info: 0x580
+  __TEXT.__eh_frame: 0x58
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__cfstring: 0x520
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x4d0
-  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1c8
+  __DATA.__data: 0x1d0
   __DATA.__common: 0x270
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 445
-  Symbols:   126
-  CStrings:  740
+  Functions: 503
+  Symbols:   129
+  CStrings:  785
 
Symbols:
+ _NSClassFromString
+ __Block_object_assign
+ _dlopen
CStrings:
+ "%s:%d:%s(): Block Lock register 0x%x\n"
+ "%s:%d:%s(): Device identified as Micron MT29F1G01ABBFD\n"
+ "%s:%d:%s(): Expected Block Lock to be 0x%x, found 0x%x"
+ "%s:%d:%s(): Expected Configuration to be 0x%x, found 0x%x"
+ "%s:%d:%s(): Status register 0x%x\n"
+ "%s:%d:%s(): Unexpected ECC status 0x%x"
+ "/System/Library/Frameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "149.40.3~85"
+ "BGST unavailable; skipping task registration for %{public}s"
+ "BGSystemTaskScheduler"
+ "CheckForMicronMT29F1G01ABBFD"
+ "DMIG"
+ "Micron_Configure_On_Boot"
+ "Micron_Disable_ECC"
+ "Micron_Disable_OTP"
+ "Micron_Enable_ECC"
+ "Micron_Enable_OTP"
+ "Micron_Number_Bit_Flips"
+ "Micron_Pack"
+ "Micron_Print_Registers"
+ "Micron_Protect"
+ "Micron_Status_Register_Read"
+ "Micron_Unpack"
+ "Micron_Unprotect"
+ "SPINAND: injecting debug fault - crash"
+ "SPINAND: injecting debug fault - error %d"
+ "SPINAND: injecting debug fault - hang for %llu sec"
+ "SPINANDConsumeDebugFault:timeoutSec:"
+ "SPINANDDebugFault"
+ "SPINANDDebugFaultErrorCode"
+ "SPINANDDebugFaultMode"
+ "SPINANDDebugFaultTimeoutSec"
+ "SPINANDFormat: on-flash region version differs from this build; not reformatting"
+ "SPINANDHasInternalContent"
+ "SPINANDInjectDebugCrash"
+ "SPINANDJrnlMajorMismatchSeen"
+ "SPINANDNewerJrnlMinorSeen"
+ "SPINANDUtilVersionMismatchSeen"
+ "_injectDebugFaultIfArmed:"
+ "crash"
+ "error"
+ "hang"
+ "integerForKey:"
+ "micron.c"
+ "q24@0:8^i16"
+ "q32@0:8^i16^Q24"
+ "removeObjectForKey:"
+ "spinandd: debug fault injection (crash)"
- "142~2167"
- "SPINANDFormat: on-flash Jrnl has newer minor than this build; not reformatting"
- "SPINANDMajorMismatchSeen"
- "SPINANDNewerMinorSeen"
```
