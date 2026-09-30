## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-180.0.0.0.0
-  __TEXT.__text: 0xf5c0
+180.0.1.0.0
+  __TEXT.__text: 0xf66c
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x157c
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x3b79
+  __TEXT.__cstring: 0x3b84
   __TEXT.__oslogstring: 0xcb
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__unwind_info: 0x368
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x455f
+  __TEXT.__objc_methname: 0x456a
   __TEXT.__objc_methtype: 0xd58
   __TEXT.__objc_stubs: 0x2bc0
   __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 72F28E15-D75E-347D-85DE-19ED570706FB
+  UUID: A2374EC0-6517-3EA4-AE70-4DBE9B2CC887
   Functions: 424
-  Symbols:   1743
+  Symbols:   1745
   CStrings:  1662
 
Symbols:
+ -[SUControllerManager _handleXPCEvent:connection:]
+ GCC_except_table16
+ ___50-[SUControllerManager _handleXPCEvent:connection:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_handleXPCEvent:connection:
- -[SUControllerManager _handleXPCEvent:]
- ___39-[SUControllerManager _handleXPCEvent:]_block_invoke
- ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
- _objc_msgSend$_handleXPCEvent:
Functions:
~ -[SUControllerManager _connectToServer] : 464 -> 432
~ ___39-[SUControllerManager _connectToServer]_block_invoke : 152 -> 156
~ -[SUControllerManager _serverConnection] : 164 -> 284
~ ___40-[SUControllerManager _serverConnection]_block_invoke : 8 -> 76
~ -[SUControllerManager _handleXPCEvent:] -> -[SUControllerManager _handleXPCEvent:connection:] : 180 -> 216
~ ___39-[SUControllerManager _handleXPCEvent:]_block_invoke -> ___50-[SUControllerManager _handleXPCEvent:connection:]_block_invoke : 808 -> 776
~ -[SUControllerManager _daemonLaunched] : 264 -> 272
CStrings:
+ "-[SUControllerManager _handleXPCEvent:connection:]_block_invoke"
+ "_handleXPCEvent:connection:"
- "-[SUControllerManager _handleXPCEvent:]_block_invoke"
- "_handleXPCEvent:"

```
