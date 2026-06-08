## MobileObliteration

> `/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration`

```diff

-371.120.3.0.0
-  __TEXT.__text: 0xaec
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__cstring: 0x453
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0x205
-  __TEXT.__unwind_info: 0x78
-  __TEXT.__objc_methname: 0x46
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x140
+395.0.0.0.0
+  __TEXT.__text: 0xd18
+  __TEXT.__objc_methlist: 0x16c
+  __TEXT.__cstring: 0x442
+  __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0x14
+  __TEXT.__oslogstring: 0x18e
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__objc_const: 0x1c0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x4
+  __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB46E6FD-7E71-3518-A366-6C92890AD42D
-  Functions: 20
-  Symbols:   139
-  CStrings:  97
+  UUID: 5D3F2CA7-555F-3770-91FC-A6C9C00948D3
+  Functions: 24
+  Symbols:   204
+  CStrings:  89
 
Symbols:
+ +[MOXPCClient sharedInstance]
+ -[MOXPCClient .cxx_destruct]
+ -[MOXPCClient _createMOServerConnection]
+ -[MOXPCClient _init]
+ -[MOXPCClient mobileObliterate:]
+ GCC_except_table4
+ _OBJC_CLASS_$_MOXPCClient
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_IVAR_$_MOXPCClient._connection
+ _OBJC_METACLASS_$_MOXPCClient
+ _OBJC_METACLASS_$_NSObject
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_MOXPCClient
+ __OBJC_$_INSTANCE_METHODS_MOXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_MOXPCClient
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOXPCProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MOXPCProtocol
+ __OBJC_CLASS_RO_$_MOXPCClient
+ __OBJC_LABEL_PROTOCOL_$_MOXPCProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_MOXPCClient
+ __OBJC_PROTOCOL_$_MOXPCProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_MOXPCProtocol
+ __Unwind_Resume
+ ___29+[MOXPCClient sharedInstance]_block_invoke
+ ___32-[MOXPCClient mobileObliterate:]_block_invoke
+ ___32-[MOXPCClient mobileObliterate:]_block_invoke.48
+ ___32-[MOXPCClient mobileObliterate:]_block_invoke.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___objc_personality_v0
+ __objc_empty_cache
+ _dispatch_once
+ _kObliterationSanitizeStorageKey
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_createMOServerConnection
+ _objc_msgSend$_init
+ _objc_msgSend$domain
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$mobileObliterate:
+ _objc_msgSend$obliterateWithOptions:reply:
+ _objc_msgSend$resume
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_storeStrong
+ _sharedInstance.onceToken
+ _sharedInstance.service
- _MOBILE_OBLITERATION_REMOTE_SERVICE_NAME
- _MOXPCTransportClose
- _MOXPCTransportOpen
- _MOXPCTransportReceiveMessage
- _MOXPCTransportResume
- _MOXPCTransportSendMessage
- _Mobile_Obliterate.cold.2
- _Mobile_Obliterate.cold.3
- _Mobile_Obliterate.cold.4
- _Mobile_Obliterate.cold.5
- _Mobile_Obliterate.cold.6
- _Mobile_Obliterate.cold.7
- _OUTLINED_FUNCTION_2
- _kObliterationTypeSafeWipe
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "ObliterationSanitizeStorage"
+ "XPC Connection Error Handler called - error: %s (code: %ld, domain: %s)\n"
+ "v16@?0@\"NSError\"8"
- "Could not create transport connection"
- "Could not receive response from server"
- "Could not send request through transport"
- "Error from server"
- "ObliterationTypeSafeWipe"
- "Status missing from response"
- "Unrecognized return status"
- "code"
- "com.apple.xpc.remote.mobile_obliteration"
- "errorWithDomain:code:userInfo:"
- "objectForKeyedSubscript:"
- "userInfo"

```
