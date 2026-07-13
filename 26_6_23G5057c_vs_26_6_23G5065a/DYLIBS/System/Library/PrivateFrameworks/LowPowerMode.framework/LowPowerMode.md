## LowPowerMode

> `/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode`

```diff

-  __TEXT.__text: 0x5e34
+  __TEXT.__text: 0x5f4c
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x954
+  __TEXT.__objc_methlist: 0x96c
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__cstring: 0x3c5
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__cstring: 0x411
   __TEXT.__oslogstring: 0x677
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_classname: 0x1ab
-  __TEXT.__objc_methname: 0xedc
-  __TEXT.__objc_methtype: 0x3ab
-  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__objc_methname: 0xf20
+  __TEXT.__objc_methtype: 0x3bd
+  __TEXT.__objc_stubs: 0xaa0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x270
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0xc38
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0xc40
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 219
-  Symbols:   856
-  CStrings:  371
+  Functions: 222
+  Symbols:   866
+  CStrings:  377
 
Sections:
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[_PMLowPowerMode isCurrentPowerModeUserInitiated]
+ GCC_except_table12
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke
+ ___50-[_PMLowPowerMode isCurrentPowerModeUserInitiated]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ _objc_msgSend$getPowerModeUserInitiatedWithReply:
CStrings:
+ "getPowerModeUserInitiatedWithReply:"
+ "isCurrentPowerModeUserInitiated"
+ "isCurrentPowerModeUserInitiated synchronous connection failed: %@\n"
+ "v12@?0B8"
+ "v24@0:8@?<v@?B>16"

```
