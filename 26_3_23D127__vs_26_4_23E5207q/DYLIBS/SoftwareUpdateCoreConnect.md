## SoftwareUpdateCoreConnect

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-2422.80.9.0.2
-  __TEXT.__text: 0xb0a8
-  __TEXT.__auth_stubs: 0x4c0
+2422.100.179.0.3
+  __TEXT.__text: 0xb68c
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0x9c8
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x36c
+  __TEXT.__gcc_except_tab: 0x340
   __TEXT.__cstring: 0xb6b
-  __TEXT.__oslogstring: 0x1e56
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__oslogstring: 0x1de0
+  __TEXT.__unwind_info: 0x348
   __TEXT.__objc_classname: 0x1ac
   __TEXT.__objc_methname: 0x1b8b
   __TEXT.__objc_methtype: 0x5b3
   __TEXT.__objc_stubs: 0x12a0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_const: 0x12d8

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 307D1FE9-061D-36DB-B731-A3926B2D9D36
-  Functions: 259
-  Symbols:   1006
-  CStrings:  612
+  UUID: B4BE7FCA-1412-3B8A-BE2D-9A1E0F3065FD
+  Functions: 263
+  Symbols:   1013
+  CStrings:  611
 
Symbols:
+ GCC_except_table23
+ GCC_except_table50
+ GCC_except_table51
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke.126
+ ___86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke.120
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ _objc_copyWeak
- -[SUCoreConnectClient _droppedConnection:].cold.1
- GCC_except_table25
- GCC_except_table53
- GCC_except_table54
- ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke.128
- ___86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke.122
- ___Block_byref_object_copy_.120
- ___Block_byref_object_dispose_.121
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x9
CStrings:
- "[ConnectionDropped] Client connection dropped to XPC server, found no retained client object available during cleanup"

```
