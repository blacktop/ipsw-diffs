## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`

```diff

-577.0.0.0.0
-  __TEXT.__text: 0x3b8e8
-  __TEXT.__objc_methlist: 0x2cf4
+578.40.6.0.0
+  __TEXT.__text: 0x3bf04
+  __TEXT.__objc_methlist: 0x2d24
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x2818
-  __TEXT.__oslogstring: 0x4f8a
-  __TEXT.__gcc_except_tab: 0xb58
-  __TEXT.__unwind_info: 0x1630
+  __TEXT.__cstring: 0x2841
+  __TEXT.__oslogstring: 0x4fea
+  __TEXT.__gcc_except_tab: 0xba0
+  __TEXT.__unwind_info: 0x1658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1768
+  __DATA_CONST.__objc_selrefs: 0x1780
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x248
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x17c0
-  __AUTH_CONST.__objc_const: 0x5258
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0x5280
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x3d0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2ec
+  __DATA.__objc_ivar: 0x2f0
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1548
-  Symbols:   2534
-  CStrings:  741
+  Functions: 1555
+  Symbols:   2545
+  CStrings:  745
 
Symbols:
+ -[BKDevice valueForDeviceProperty:error:]
+ -[BiometricKitXPCClient getDeviceProperties:]
+ GCC_except_table126
+ GCC_except_table172
+ GCC_except_table196
+ GCC_except_table241
+ GCC_except_table249
+ GCC_except_table281
+ GCC_except_table72
+ _OBJC_IVAR_$_BKDevice._deviceProperties
+ _OSLogHandle
+ _OSLogTraceHandle
+ ___45-[BiometricKitXPCClient getDeviceProperties:]_block_invoke
+ ___45-[BiometricKitXPCClient getDeviceProperties:]_block_invoke_2
+ _objc_msgSend$getDeviceProperties:
+ _objc_msgSend$getDeviceProperties:replyBlock:
- GCC_except_table136
- GCC_except_table175
- GCC_except_table199
- GCC_except_table246
- GCC_except_table251
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.6~29, %s file: %s, line: %d\n\n"
+ "BKDPHasFaceIDInExclave"
+ "BKDPRequiresFaceIDLatencyMitigation"
+ "BKDevicePearl::valueForDeviceProperty: %lu (_cid:%lu)\n"
+ "BKDevicePearl::valueForDeviceProperty: -> %@, error:%@\n"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Framework'!\n"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Legacy'!\n"
+ "Framework"
+ "Framework-Legacy"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~3088, %s file: %s, line: %d\n\n"
- "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Internal'!\n"
- "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Internal-Legacy'!\n"
- "Framework-Internal"
- "Framework-Internal-Legacy"
```
