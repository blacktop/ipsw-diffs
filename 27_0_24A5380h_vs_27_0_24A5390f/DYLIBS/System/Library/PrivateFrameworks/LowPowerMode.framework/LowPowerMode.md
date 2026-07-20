## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2043.0.13.502.1
-  __TEXT.__text: 0x5714
-  __TEXT.__objc_methlist: 0x954
+2043.0.31.0.0
+  __TEXT.__text: 0x5828
+  __TEXT.__objc_methlist: 0x96c
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__cstring: 0x3cd
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__cstring: 0x419
   __TEXT.__oslogstring: 0x677
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x80
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0xc38
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0xc40
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x420

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 214
-  Symbols:   524
-  CStrings:  89
+  Functions: 217
+  Symbols:   530
+  CStrings:  91
 
Symbols:
+ -[_PMLowPowerMode isCurrentPowerModeUserInitiated]
+ GCC_except_table12
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ _objc_msgSend$getPowerModeUserInitiatedWithReply:
CStrings:
+ "isCurrentPowerModeUserInitiated synchronous connection failed: %@\n"
+ "v12@?0B8"
```
