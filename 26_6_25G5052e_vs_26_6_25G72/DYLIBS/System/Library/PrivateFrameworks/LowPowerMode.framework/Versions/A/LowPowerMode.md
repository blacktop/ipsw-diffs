## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/Versions/A/LowPowerMode`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1846.160.2.0.0
-  __TEXT.__text: 0x43e4
+1846.160.4.0.0
+  __TEXT.__text: 0x4500
   __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x7a8
+  __TEXT.__objc_methlist: 0x7c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x339
-  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__cstring: 0x385
+  __TEXT.__gcc_except_tab: 0xa4
   __TEXT.__oslogstring: 0x52c
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x18d
-  __TEXT.__objc_methname: 0xf7b
-  __TEXT.__objc_methtype: 0x4c3
-  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methname: 0xfbf
+  __TEXT.__objc_methtype: 0x4d5
+  __TEXT.__objc_stubs: 0x8a0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0xb90
+  __AUTH_CONST.__const: 0x3d0
+  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__objc_const: 0xb98
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x3c0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 184
-  Symbols:   460
-  CStrings:  333
+  Functions: 187
+  Symbols:   466
+  CStrings:  338
 
Symbols:
+ -[_PMLowPowerMode isCurrentPowerModeUserInitiated]
+ GCC_except_table16
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ _objc_msgSend$getPowerModeUserInitiatedWithReply:
CStrings:
+ "getPowerModeUserInitiatedWithReply:"
+ "isCurrentPowerModeUserInitiated"
+ "isCurrentPowerModeUserInitiated synchronous connection failed: %@\n"
+ "v12@?0B8"
+ "v24@0:8@?<v@?B>16"
```
