## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-177.0.0.0.1
-  __TEXT.__text: 0xf4b8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x1564
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x3add
+180.0.0.0.0
+  __TEXT.__text: 0xf5c0
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x157c
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x3b79
   __TEXT.__oslogstring: 0xcb
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x44db
+  __TEXT.__objc_methname: 0x455f
   __TEXT.__objc_methtype: 0xd58
-  __TEXT.__objc_stubs: 0x2b80
-  __DATA_CONST.__got: 0x228
+  __TEXT.__objc_stubs: 0x2bc0
+  __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x3b8
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_selrefs: 0xf28
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2c40
-  __AUTH_CONST.__objc_const: 0x2568
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__objc_const: 0x2598
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x348
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C130A1D-34DC-35F0-BB4B-627B8396F943
-  Functions: 422
-  Symbols:   1734
-  CStrings:  1653
+  UUID: 72F28E15-D75E-347D-85DE-19ED570706FB
+  Functions: 424
+  Symbols:   1743
+  CStrings:  1662
 
Symbols:
+ -[SUControllerManager needToAddClientForXPCMessages]
+ -[SUControllerManager setNeedToAddClientForXPCMessages:]
+ _OBJC_IVAR_$_SUControllerManager._needToAddClientForXPCMessages
+ __xpc_error_connection_invalid
+ _objc_msgSend$needToAddClientForXPCMessages
+ _objc_msgSend$setNeedToAddClientForXPCMessages:
+ _xpc_connection_copy_invalidation_reason
CStrings:
+ "-[SUControllerManager _addClient]"
+ "Received XPC_ERROR_CONNECTION_INTERRUPTED. sucontrollerd disconnected"
+ "Received XPC_ERROR_CONNECTION_INVALID. sucontrollerd disconnected.  Invalidation reason: %s"
+ "SUCManager[CONNECTING] resumed server connection: %@"
+ "Sending add client message for client name %@"
+ "TB,N,V_needToAddClientForXPCMessages"
+ "_needToAddClientForXPCMessages"
+ "needToAddClientForXPCMessages"
+ "setNeedToAddClientForXPCMessages:"
- "SUCManager[CONNECTING] resumed server connection, sending add client message for client name %s, connection: %@"
- "sucontrollerd disconnected"

```
