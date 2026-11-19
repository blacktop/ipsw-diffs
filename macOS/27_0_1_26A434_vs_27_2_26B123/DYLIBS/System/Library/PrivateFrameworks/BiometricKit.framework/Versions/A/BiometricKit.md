## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/Versions/A/BiometricKit`

```diff

-577.0.0.0.0
-  __TEXT.__text: 0x2e3a8
-  __TEXT.__objc_methlist: 0x2a64
+578.40.7.0.0
+  __TEXT.__text: 0x2e8cc
+  __TEXT.__objc_methlist: 0x2a94
   __TEXT.__const: 0x138
-  __TEXT.__oslogstring: 0x3e87
-  __TEXT.__cstring: 0x1887
-  __TEXT.__gcc_except_tab: 0xae4
-  __TEXT.__unwind_info: 0xe70
+  __TEXT.__oslogstring: 0x3ee8
+  __TEXT.__cstring: 0x18b0
+  __TEXT.__gcc_except_tab: 0xb2c
+  __TEXT.__unwind_info: 0xe90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f8
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0xcf0
-  __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0x5220
+  __AUTH_CONST.__cfstring: 0x10e0
+  __AUTH_CONST.__objc_const: 0x5248
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2e8
+  __DATA.__objc_ivar: 0x2ec
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA.__bss: 0x28
+  __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xa0
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1232
-  Symbols:   2414
-  CStrings:  515
+  Functions: 1236
+  Symbols:   2425
+  CStrings:  519
 
Symbols:
+ -[BKDevice valueForDeviceProperty:error:]
+ -[BiometricKitXPCClient getDeviceProperties:]
+ GCC_except_table141
+ GCC_except_table187
+ GCC_except_table213
+ GCC_except_table258
+ GCC_except_table266
+ GCC_except_table298
+ GCC_except_table79
+ OBJC_IVAR_$_BKDevice._deviceProperties
+ _OSLogHandle
+ _OSLogTraceHandle
+ ___45-[BiometricKitXPCClient getDeviceProperties:]_block_invoke
+ ___45-[BiometricKitXPCClient getDeviceProperties:]_block_invoke_2
+ _objc_msgSend$getDeviceProperties:
+ _objc_msgSend$getDeviceProperties:replyBlock:
- GCC_except_table151
- GCC_except_table192
- GCC_except_table216
- GCC_except_table263
- GCC_except_table268
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.7~571, %s file: %s, line: %d\n\n"
+ "BKDPHasFaceIDInExclave"
+ "BKDPRequiresFaceIDLatencyMitigation"
+ "BKDevicePearl::valueForDeviceProperty: %lu (_cid:%lu)\n"
+ "BKDevicePearl::valueForDeviceProperty: -> %@, error:%@\n"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Framework'!\n"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Legacy'!\n"
+ "Framework"
+ "Framework-Legacy"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~3086, %s file: %s, line: %d\n\n"
- "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Internal'!\n"
- "Couldn't create OS Log for 'com.apple.BiometricKit.Framework-Internal-Legacy'!\n"
- "Framework-Internal"
- "Framework-Internal-Legacy"
```
