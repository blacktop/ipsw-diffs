## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0x3b9cc
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x4550
+152.0.0.0.0
+  __TEXT.__text: 0x3bfa0
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x45d0
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x3acb
+  __TEXT.__cstring: 0x3b58
   __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__oslogstring: 0xb8c
-  __TEXT.__unwind_info: 0x7f0
-  __TEXT.__objc_classname: 0x3b1
-  __TEXT.__objc_methname: 0xdc2d
-  __TEXT.__objc_methtype: 0x1967
-  __TEXT.__objc_stubs: 0x8480
+  __TEXT.__oslogstring: 0xb97
+  __TEXT.__unwind_info: 0x820
+  __TEXT.__objc_classname: 0x3d4
+  __TEXT.__objc_methname: 0xdd8b
+  __TEXT.__objc_methtype: 0x1a23
+  __TEXT.__objc_stubs: 0x85c0
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x998
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0xa08
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb850
-  __DATA_CONST.__objc_selrefs: 0x3248
+  __DATA_CONST.__objc_const: 0xb960
+  __DATA_CONST.__objc_selrefs: 0x32a8
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__objc_const: 0x1100
-  __AUTH_CONST.__cfstring: 0x5d60
+  __AUTH_CONST.__objc_const: 0x11d8
+  __AUTH_CONST.__cfstring: 0x5de0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x230
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x73c
-  __DATA.__data: 0x5a0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_protorefs: 0x10
+  __DATA.__objc_classrefs: 0x250
+  __DATA.__objc_superrefs: 0x80
+  __DATA.__objc_ivar: 0x744
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x780
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1548
-  Symbols:   5477
-  CStrings:  3610
+  Functions: 1563
+  Symbols:   5550
+  CStrings:  3641
 
Symbols:
+ +[SDLogger client]
+ +[SDLogger daemon]
+ +[SpeedDClient sharedInstance]
+ -[SpeedDClient .cxx_destruct]
+ -[SpeedDClient getPrivilegedFileHandleForPacketCapture:]
+ -[SpeedDClient getPrivilegedFileHandleForPath:completionHandler:]
+ -[SpeedDClient init]
+ -[SpeedDClient testServiceWithArguments:completionHandler:]
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_SDLogger
+ _OBJC_CLASS_$_SpeedDClient
+ _OBJC_IVAR_$_SpeedDClient.connection
+ _OBJC_IVAR_$_SpeedDClient.server
+ _OBJC_METACLASS_$_SDLogger
+ _OBJC_METACLASS_$_SpeedDClient
+ __OBJC_$_CLASS_METHODS_SDLogger
+ __OBJC_$_CLASS_METHODS_SpeedDClient
+ __OBJC_$_INSTANCE_METHODS_SpeedDClient
+ __OBJC_$_INSTANCE_VARIABLES_SpeedDClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDServices
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SDServices
+ __OBJC_CLASS_PROTOCOLS_$_SpeedDClient
+ __OBJC_CLASS_RO_$_SDLogger
+ __OBJC_CLASS_RO_$_SpeedDClient
+ __OBJC_LABEL_PROTOCOL_$_SDServices
+ __OBJC_METACLASS_RO_$_SDLogger
+ __OBJC_METACLASS_RO_$_SpeedDClient
+ __OBJC_PROTOCOL_$_SDServices
+ __OBJC_PROTOCOL_REFERENCE_$_SDServices
+ ___20-[SpeedDClient init]_block_invoke
+ ___20-[SpeedDClient init]_block_invoke_2
+ ___20-[SpeedDClient init]_block_invoke_3
+ ___30+[SpeedDClient sharedInstance]_block_invoke
+ ___56-[SpeedDClient getPrivilegedFileHandleForPacketCapture:]_block_invoke
+ ___59-[SpeedDClient testServiceWithArguments:completionHandler:]_block_invoke
+ ___65-[SpeedDClient getPrivilegedFileHandleForPath:completionHandler:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e21_v24?0q8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSFileHandle"8"NSError"16ls32l8
+ ___block_literal_global.12
+ ___block_literal_global.17
+ ___block_literal_global.23
+ _dispatch_once
+ _objc_msgSend$getPrivilegedFileHandleForPacketCapture:
+ _objc_msgSend$getPrivilegedFileHandleForPath:completionHandler:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$testServiceWithArguments:completionHandler:
+ _objc_release_x1
+ _sharedInstance
+ _sharedInstance.onceToken
CStrings:
+ "\x02"
+ "%@: %@ %@\n"
+ "@\"<SDServices>\""
+ "@\"NSXPCConnection\""
+ "Error on remote object proxy"
+ "Interrupted"
+ "Invalidated"
+ "SDLogger"
+ "SDServices"
+ "SpeedDClient"
+ "com.apple.speedd"
+ "daemon"
+ "getPrivilegedFileHandleForPacketCapture:"
+ "getPrivilegedFileHandleForPath:completionHandler:"
+ "initWithMachServiceName:options:"
+ "interfaceWithProtocol:"
+ "localizedFailureReason"
+ "remoteObjectProxyWithErrorHandler:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "sharedInstance"
+ "testServiceWithArguments:completionHandler:"
+ "v24@0:8@?<v@?@\"NSFileHandle\"@\"NSError\">16"
+ "v24@?0@\"NSFileHandle\"8@\"NSError\"16"
+ "v24@?0q8@\"NSString\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?q@\"NSString\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSFileHandle\"@\"NSError\">24"
+ "v32@0:8@16@?24"

```
