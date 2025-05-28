## iOSScreenSharing

> `/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing`

```diff

-85.1.0.0.0
-  __TEXT.__text: 0xad0
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x98
+105.3.0.0.0
+  __TEXT.__text: 0x11a8
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x2a7
-  __TEXT.__oslogstring: 0x2d
-  __TEXT.__unwind_info: 0x7c
-  __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0x44e
-  __TEXT.__objc_methtype: 0x14d
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x48
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0x1af
+  __TEXT.__oslogstring: 0x1d6
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_classname: 0x66
+  __TEXT.__objc_methname: 0x52d
+  __TEXT.__objc_methtype: 0x15f
+  __TEXT.__objc_stubs: 0x480
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4d0
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_const: 0x540
+  __DATA_CONST.__objc_selrefs: 0x188
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x168
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x120
+  __DATA.__objc_ivar: 0xc
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18
-  Symbols:   153
-  CStrings:  116
+  Functions: 24
+  Symbols:   194
+  CStrings:  138
 
Symbols:
+ -[ViewServiceHelper connections]
+ -[ViewServiceHelper listener:shouldAcceptNewConnection:].cold.1
+ -[ViewServiceHelper sendSessionInfoToClient]
+ -[ViewServiceHelper sendSessionInfoToClient].cold.1
+ -[ViewServiceHelper setConnections:]
+ GCC_except_table6
+ _CFStringCreateWithCString
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_IVAR_$_ViewServiceHelper._connections
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ViewServiceBackChannelProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ViewServiceBackChannelProtocol
+ __OBJC_$_PROTOCOL_REFS_ViewServiceBackChannelProtocol
+ __OBJC_LABEL_PROTOCOL_$_ViewServiceBackChannelProtocol
+ __OBJC_PROTOCOL_$_ViewServiceBackChannelProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ViewServiceBackChannelProtocol
+ __Unwind_Resume
+ ___44-[ViewServiceHelper sendSessionInfoToClient]_block_invoke
+ ___block_literal_global.102
+ ___block_literal_global.105
+ ___objc_personality_v0
+ __dispatch_main_q
+ __os_log_error_impl
+ _kCFAllocatorDefault
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$connections
+ _objc_msgSend$lastObject
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$setConnections:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setUserInfo:
+ _objc_opt_new
+ _objc_release_x26
+ _objc_retain_x21
+ _objc_sync_enter
+ _objc_sync_exit
- ___block_literal_global.100
- ___block_literal_global.103
CStrings:
+ "\x12"
+ "@\"NSMutableArray\""
+ "NSXPCConnection"
+ "Sending session info to client"
+ "T@\"NSMutableArray\",&,V_connections"
+ "T@\"NSString\",?,R,C"
+ "Unable to get entitlement %@ for client task. Error: %@"
+ "ViewServiceBackChannelProtocol"
+ "_connections"
+ "addObject:"
+ "adding connection"
+ "arrayWithCapacity:"
+ "bundleIdentifier"
+ "connections"
+ "isAppleSupportRequest"
+ "lastObject"
+ "objectForKey:"
+ "pidNotification not supported"
+ "remoteObjectProxy"
+ "sendSessionInfoToClient"
+ "setConnections:"
+ "setObject:forKey:"
+ "setUserInfo:"
+ "start listener:shouldAcceptNewConnection:"
+ "viewServerHelper delegate does not support sessionState message"
- "\x11"
- "Unable to get entitlement (com.apple.springboard.activateawayviewplugins) for client task. Error: %@"
- "does not respond 2"

```
