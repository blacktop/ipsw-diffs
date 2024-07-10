## PowerExperience

> `/System/Library/PrivateFrameworks/PowerExperience.framework/Versions/A/PowerExperience`

```diff

-41.0.0.0.0
-  __TEXT.__text: 0x2d2c
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1f4
-  __TEXT.__oslogstring: 0x2c2
-  __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x1c8
+43.0.0.0.0
+  __TEXT.__text: 0x3060
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_methlist: 0x2a0
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x220
+  __TEXT.__oslogstring: 0x313
+  __TEXT.__gcc_except_tab: 0x1c4
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0xe7
-  __TEXT.__objc_methname: 0x6e6
-  __TEXT.__objc_methtype: 0x299
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x50
+  __TEXT.__objc_methname: 0x7a8
+  __TEXT.__objc_methtype: 0x2af
+  __TEXT.__objc_stubs: 0x640
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xe0
-  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__const: 0x310
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x6c8
+  __AUTH_CONST.__objc_const: 0x728
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x240
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x44
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 104
-  Symbols:   323
-  CStrings:  29
+  Functions: 112
+  Symbols:   346
+  CStrings:  31
 
Symbols:
+ -[ContextualPowerModesClient connectionInterrupted]
+ -[ContextualPowerModesClient init].cold.3
+ -[ContextualPowerModesClient interestedModes]
+ -[ContextualPowerModesClient reRegister]
+ -[ContextualPowerModesClient setConnectionInterrupted:]
+ -[ContextualPowerModesClient setInterestedModes:]
+ GCC_except_table12
+ OBJC_IVAR_$_ContextualPowerModesClient._connectionInterrupted
+ OBJC_IVAR_$_ContextualPowerModesClient._interestedModes
+ __34-[ContextualPowerModesClient init]_block_invoke.32
+ __34-[ContextualPowerModesClient init]_block_invoke.32.cold.1
+ __34-[ContextualPowerModesClient init]_block_invoke.34
+ __40-[ContextualPowerModesClient reRegister]_block_invoke.cold.1
+ ___40-[ContextualPowerModesClient reRegister]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v12?0i8l
+ __block_literal_global.20
+ __dispatch_main_q
+ _notify_register_dispatch
+ _objc_msgSend$connectionInterrupted
+ _objc_msgSend$identifier
+ _objc_msgSend$interestedModes
+ _objc_msgSend$reRegister
+ _objc_msgSend$setConnectionInterrupted:
+ _objc_msgSend$setInterestedModes:
+ init.syncToken
- __34-[ContextualPowerModesClient init]_block_invoke.30
- __34-[ContextualPowerModesClient init]_block_invoke.30.cold.1
CStrings:
+ "com.apple.powerexperienced.restart"
+ "v12@?0i8"

```
