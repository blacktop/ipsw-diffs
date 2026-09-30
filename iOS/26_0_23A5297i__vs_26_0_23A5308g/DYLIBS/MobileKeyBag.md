## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-674.0.2.0.0
-  __TEXT.__text: 0x1f498
+674.0.3.0.0
+  __TEXT.__text: 0x1f5b0
   __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__cstring: 0x9881
+  __TEXT.__cstring: 0x98f7
   __TEXT.__const: 0x506
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x658
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__unwind_info: 0x958
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x15d5
   __TEXT.__objc_methtype: 0xa31
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x888
+  __DATA_CONST.__const: 0x8a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0xa18
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x4fc0
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x4fe0
   __AUTH_CONST.__objc_const: 0x718
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x360
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 546D5D48-71B3-3B88-8113-E71726E9C75D
-  Functions: 692
-  Symbols:   2051
-  CStrings:  2078
+  UUID: 58166084-14AB-3CA1-A344-70F0A64DAC42
+  Functions: 695
+  Symbols:   2061
+  CStrings:  2083
 
Symbols:
+ ___is_device_in_device_recovery_environment_block_invoke
+ _is_device_in_device_recovery_environment
+ _is_device_in_device_recovery_environment.answer
+ _is_device_in_device_recovery_environment.cold.1
+ _is_device_in_device_recovery_environment.once
Functions:
~ _MKBGetDeviceLockStateInfo : 568 -> 588
+ _is_device_in_device_recovery_environment
+ ___is_device_in_device_recovery_environment_block_invoke
+ _is_device_in_device_recovery_environment.cold.1
CStrings:
+ "device-recovery"
+ "hw.osenvironment"
+ "is_device_in_device_recovery_environment_block_invoke"
+ "sysctl(hw.osenvironment) -> %d"

```
