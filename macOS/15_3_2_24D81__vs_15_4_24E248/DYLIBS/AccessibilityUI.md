## AccessibilityUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUI.framework/Versions/A/AccessibilityUI`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x4d5c
+3148.15.11.1.0
+  __TEXT.__text: 0x4d48
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x32c
+  __TEXT.__objc_methlist: 0x484
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x2d0
   __TEXT.__oslogstring: 0x812

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x410
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0x888
+  __AUTH_CONST.__objc_const: 0x610
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120

   - /System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/Versions/A/AccessibilityUIShared
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 72B99666-E66B-3274-820B-28904813EDFF
+  UUID: EBC0E3A4-78BB-3509-A49B-896830CC2069
   Functions: 128
   Symbols:   440
   CStrings:  310
Symbols:
+ +[AXUIClientConnection sharedClientConnection].cold.1
+ GCC_except_table67
- GCC_except_table66
- _OUTLINED_FUNCTION_10
Functions:
~ +[AXUIClientConnection sharedClientConnection] : 84 -> 68
~ -[AXUIClientConnection serviceConnection] : 264 -> 260
~ -[AXUIClientConnection setServiceConnection:] : 152 -> 148
~ -[AXUIClientConnection _initializeServiceConnection] : 568 -> 564
~ ___52-[AXUIClientConnection _initializeServiceConnection]_block_invoke : 532 -> 516
~ __52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.292 : 284 -> 288
~ -[AXUIClientConnection _processXPCReply:context:] : 1996 -> 1992
~ -[AXUIClientConnection cleanUp] : 368 -> 372
~ _OUTLINED_FUNCTION_0 : 32 -> 16
~ _OUTLINED_FUNCTION_1 : 32 -> 16
~ _OUTLINED_FUNCTION_2 : 32 -> 12
~ _OUTLINED_FUNCTION_4 : 16 -> 24
~ _OUTLINED_FUNCTION_5 : 28 -> 24
~ _OUTLINED_FUNCTION_6 : 24 -> 28
~ _OUTLINED_FUNCTION_7 : 24 -> 20
~ _OUTLINED_FUNCTION_8 : 20 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 20
~ _OUTLINED_FUNCTION_10 -> -[AXUIClient messageSender:processCustomDataFromXPCReply:].cold.1 : 20 -> 176
~ -[AXUIClient messageSender:willSendXPCMessage:context:].cold.2 -> +[AXUIClientConnection sharedClientConnection].cold.1 : 176 -> 20
~ -[AXUIClientConnection _initializeServiceConnection].cold.1 : 108 -> 104
~ __52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.cold.1 : 160 -> 172
~ __52-[AXUIClientConnection _initializeServiceConnection]_block_invoke_2.296.cold.1 : 160 -> 172
~ __52-[AXUIClientConnection _initializeServiceConnection]_block_invoke.297.cold.1 : 140 -> 152
~ -[AXUIClientConnection performLaunchAngelTask:].cold.1 : 152 -> 172
~ __47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.1 : 180 -> 196
~ __47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.2 : 180 -> 280
~ __47-[AXUIClientConnection performLaunchAngelTask:]_block_invoke.cold.3 : 280 -> 188
~ __42-[AXUIClientConnection tearDownConnection]_block_invoke.cold.1 : 188 -> 196
~ -[AXUIClientConnection _processXPCReply:context:].cold.1 : 156 -> 104
~ -[AXUIClientConnection _processXPCReply:context:].cold.2 : 124 -> 176
~ -[AXUIClientConnection _processXPCReply:context:].cold.3 : 176 -> 124
~ -[AXUIClientConnection _processXPCReply:context:].cold.4 : 108 -> 156
~ __31-[AXUIClientConnection cleanUp]_block_invoke.cold.1 : 156 -> 144

```
