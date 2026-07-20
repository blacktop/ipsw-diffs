## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/Versions/A/LowPowerMode`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2043.0.13.0.2
-  __TEXT.__text: 0x3ea0
-  __TEXT.__objc_methlist: 0x7a8
+2043.0.31.0.0
+  __TEXT.__text: 0x3fb8
+  __TEXT.__objc_methlist: 0x7c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x343
-  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__cstring: 0x38f
+  __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__oslogstring: 0x52c
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__unwind_info: 0x200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x88
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0xb90
+  __AUTH_CONST.__const: 0x3d0
+  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__objc_const: 0xb98
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x60

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 179
-  Symbols:   457
-  CStrings:  73
+  Functions: 182
+  Symbols:   463
+  CStrings:  75
 
Symbols:
+ -[_PMLowPowerMode isCurrentPowerModeUserInitiated]
+ GCC_except_table16
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ _objc_msgSend$getPowerModeUserInitiatedWithReply:
CStrings:
+ "isCurrentPowerModeUserInitiated synchronous connection failed: %@\n"
+ "v12@?0B8"
```
