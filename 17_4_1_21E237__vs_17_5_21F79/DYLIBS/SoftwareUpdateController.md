## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-146.0.0.0.1
-  __TEXT.__text: 0xcea8
+148.120.1.0.1
+  __TEXT.__text: 0xcf20
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x10f4
+  __TEXT.__objc_methlist: 0x1104
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x302a
+  __TEXT.__cstring: 0x3098
   __TEXT.__oslogstring: 0x17
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x310
+  __TEXT.__unwind_info: 0x318
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x3c3a
+  __TEXT.__objc_methname: 0x3c4c
   __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_stubs: 0x1f60
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x23a8
-  __DATA_CONST.__objc_selrefs: 0xb50
+  __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_classrefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__cfstring: 0x2240
+  __AUTH_CONST.__cfstring: 0x2260
   __AUTH_CONST.__objc_const: 0x5e8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05A6D599-F037-3042-8513-EA2F2DAC3DEE
-  Functions: 390
-  Symbols:   1538
-  CStrings:  1397
+  UUID: 63B482C8-4688-3286-B5A3-6FEBCD5597A5
+  Functions: 391
+  Symbols:   1541
+  CStrings:  1400
 
Symbols:
+ -[SUControllerManager _connectToServer]
+ GCC_except_table14
+ ___39-[SUControllerManager _connectToServer]_block_invoke
+ _objc_msgSend$_connectToServer
- GCC_except_table15
- ___40-[SUControllerManager _serverConnection]_block_invoke_2
CStrings:
+ "-[SUControllerManager _connectToServer]"
+ "-[SUControllerManager _connectToServer]_block_invoke"
+ "SUCManager[CONNECTING] resumed server connection, sending add client message for client name %s, connection: %@"
+ "_connectToServer"
+ "sucontrollerd is launched - initial launch after boot"
+ "sucontrollerd is relaunched.  Connecting %s to get deletegate callback again."
- "-[SUControllerManager _serverConnection]_block_invoke"
- "-[SUControllerManager _serverConnection]_block_invoke_2"
- "SUCManager[CONNECTING] resumed server connection, sending add client message for client %@"
- "sucontrollerd is launched"

```
