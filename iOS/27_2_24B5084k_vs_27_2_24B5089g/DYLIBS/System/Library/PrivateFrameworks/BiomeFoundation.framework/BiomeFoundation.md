## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-255.0.2.0.0
-  __TEXT.__text: 0x33ae0
-  __TEXT.__objc_methlist: 0x2a74
+256.0.1.0.0
+  __TEXT.__text: 0x33be0
+  __TEXT.__objc_methlist: 0x2aa4
   __TEXT.__const: 0x23a
   __TEXT.__cstring: 0x50dd
-  __TEXT.__oslogstring: 0x33c2
-  __TEXT.__gcc_except_tab: 0xdf4
+  __TEXT.__oslogstring: 0x341f
+  __TEXT.__gcc_except_tab: 0xdfc
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__unwind_info: 0x12c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d0
+  __DATA_CONST.__objc_selrefs: 0x18f8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1348

   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_got: 0x710
   __AUTH.__objc_data: 0x520
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x294

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1232
-  Symbols:   2803
+  Functions: 1236
+  Symbols:   2809
   CStrings:  1062
 
Symbols:
+ +[BMXPCConnectionFactory connectionToAccessServerInDomain:user:useCase:options:callerConnection:]
+ -[BMAccessClient _newConnectionForDomain:callerConnection:]
+ -[BMAccessClient _requestAccessToResource:mode:callerConnection:error:]
+ -[BMAccessClient _synchronousRemoteObjectProxyForDomain:callerConnection:errorHandler:]
+ -[BMAccessClient requestAccessToResource:mode:callerConnection:error:]
+ -[BMXPCConnectionFactory _newConnectionWithCallerConnection:]
+ -[BMXPCConnectionFactory _newConnectionWrapperWithCallerConnection:]
+ -[BMXPCConnectionFactory _proxyConnectionThroughCaller:]
+ -[BMXPCConnectionFactory initWithServiceType:domain:user:useCase:options:]
+ GCC_except_table14
+ GCC_except_table24
+ ___56-[BMXPCConnectionFactory _proxyConnectionThroughCaller:]_block_invoke
+ ___68-[BMXPCConnectionFactory _newConnectionWrapperWithCallerConnection:]_block_invoke
+ ___68-[BMXPCConnectionFactory _newConnectionWrapperWithCallerConnection:]_block_invoke_2
+ ___71-[BMAccessClient _requestAccessToResource:mode:callerConnection:error:]_block_invoke
+ ___87-[BMAccessClient _synchronousRemoteObjectProxyForDomain:callerConnection:errorHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e29_"BMXPCConnectionWrapper"8?0ls32l8s40l8
+ _objc_msgSend$_newConnectionForDomain:callerConnection:
+ _objc_msgSend$_newConnectionWithCallerConnection:
+ _objc_msgSend$_newConnectionWrapperWithCallerConnection:
+ _objc_msgSend$_proxyConnectionThroughCaller:
+ _objc_msgSend$_requestAccessToResource:mode:callerConnection:error:
+ _objc_msgSend$_synchronousRemoteObjectProxyForDomain:callerConnection:errorHandler:
+ _objc_msgSend$connectionToAccessServerInDomain:user:useCase:options:callerConnection:
+ _objc_msgSend$initWithServiceType:domain:user:useCase:options:
+ _objc_retain_x6
- -[BMAccessClient _newConnectionForDomain:]
- -[BMXPCConnectionFactory _newConnection]
- -[BMXPCConnectionFactory _requestConnectionFromCaller]
- -[BMXPCConnectionFactory initWithType:domain:user:useCase:options:]
- -[BMXPCConnectionFactory makeConnectionWrapper]
- GCC_except_table11
- GCC_except_table18
- GCC_except_table25
- GCC_except_table42
- ___47-[BMXPCConnectionFactory makeConnectionWrapper]_block_invoke
- ___47-[BMXPCConnectionFactory makeConnectionWrapper]_block_invoke_2
- ___53-[BMAccessClient requestAccessToResource:mode:error:]_block_invoke
- ___54-[BMXPCConnectionFactory _requestConnectionFromCaller]_block_invoke
- ___70-[BMAccessClient _synchronousRemoteObjectProxyForDomain:errorHandler:]_block_invoke
- ___block_descriptor_40_e8_32s_e29_"BMXPCConnectionWrapper"8?0ls32l8
- _objc_msgSend$_newConnectionForDomain:
- _objc_msgSend$_requestConnectionFromCaller
- _objc_msgSend$connectionToAccessServerInDomain:user:useCase:options:
- _objc_msgSend$initWithType:domain:user:useCase:options:
- _objc_msgSend$makeConnectionWrapper
CStrings:
+ "Unable to determine caller connection for on-behalf-of proxy: no explicit callerConnection was supplied and NSXPCConnection.currentConnection is nil"
- "Unable to determine current connection in write service"
```
