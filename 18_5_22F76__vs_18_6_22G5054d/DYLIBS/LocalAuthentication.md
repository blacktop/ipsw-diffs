## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x36430
+1656.140.3.0.0
+  __TEXT.__text: 0x36474
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x37b8
   __TEXT.__const: 0x2d4
   __TEXT.__gcc_except_tab: 0xfe8
   __TEXT.__cstring: 0x19a0
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2748
+  __TEXT.__oslogstring: 0x2779
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__unwind_info: 0x12d0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa2f
-  __TEXT.__objc_methname: 0x6f47
-  __TEXT.__objc_methtype: 0x1d33
-  __TEXT.__objc_stubs: 0x49c0
-  __DATA_CONST.__got: 0x508
+  __TEXT.__objc_classname: 0xa4c
+  __TEXT.__objc_methname: 0x6ecf
+  __TEXT.__objc_methtype: 0x1d3b
+  __TEXT.__objc_stubs: 0x4960
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd8
+  __DATA_CONST.__objc_selrefs: 0x1bc0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x88f8
+  __AUTH_CONST.__objc_const: 0x8988
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x550
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0xbe8
   __DATA.__bss: 0x420

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6C6FB48F-FD21-3FED-9D3F-5BF57844260B
-  Functions: 1468
-  Symbols:   5270
-  CStrings:  2264
+  UUID: 67E76038-F122-3C92-B8FC-897156A7FA23
+  Functions: 1470
+  Symbols:   5273
+  CStrings:  2263
 
Symbols:
+ -[LAEnvironmentServiceXPCClient _bootstrapServiceType:completion:]
+ -[LAEnvironmentServiceXPCClient _createConnectionToDaemon]
+ -[LAEnvironmentServiceXPCClient _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]
+ -[LAEnvironmentServiceXPCClient synchronousProxyToEnvironmentServiceWithCompletion:]
+ _OBJC_CLASS_$_LACXPCInterface
+ _OBJC_CLASS_$_LAEnvironmentServiceXPCClient
+ _OBJC_IVAR_$_LAEnvironment._xpcClient
+ _OBJC_METACLASS_$_LAEnvironmentServiceXPCClient
+ __OBJC_$_INSTANCE_METHODS_LAEnvironmentServiceXPCClient
+ __OBJC_CLASS_RO_$_LAEnvironmentServiceXPCClient
+ __OBJC_METACLASS_RO_$_LAEnvironmentServiceXPCClient
+ ___29-[LAEnvironment _updateState]_block_invoke.cold.1
+ ___66-[LAEnvironmentServiceXPCClient _bootstrapServiceType:completion:]_block_invoke
+ ___84-[LAEnvironmentServiceXPCClient synchronousProxyToEnvironmentServiceWithCompletion:]_block_invoke
+ ___94-[LAEnvironmentServiceXPCClient _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16lr32l8r40l8
+ _objc_msgSend$interfaceForXPCProtocol:
+ _objc_msgSend$synchronousProxyToEnvironmentServiceWithCompletion:
- -[LAEnvironment _bootstrapServiceType:completion:]
- -[LAEnvironment _createConnectionToDaemon]
- -[LAEnvironment _environmentServiceEndpointWithCompletion:]
- -[LAEnvironment _synchronousProxyToEnvironmentServiceWithCompletion:]
- -[LAEnvironment _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]
- GCC_except_table27
- _OBJC_CLASS_$_LACEnvironmentMechanismBiometry
- _OBJC_CLASS_$_LACEnvironmentMechanismCompanion
- _OBJC_CLASS_$_LACEnvironmentMechanismUserPassword
- _OBJC_CLASS_$_LACEnvironmentState
- _OBJC_IVAR_$_LAEnvironment._environmentServiceEndpoint
- ___50-[LAEnvironment _bootstrapServiceType:completion:]_block_invoke
- ___69-[LAEnvironment _synchronousProxyToEnvironmentServiceWithCompletion:]_block_invoke
- ___78-[LAEnvironment _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]_block_invoke
- ___block_descriptor_48_e8_32bs40w_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16ls32l8w40l8
- _objc_msgSend$_environmentServiceEndpointWithCompletion:
- _objc_msgSend$_synchronousProxyToEnvironmentServiceWithCompletion:
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setWithObjects:
CStrings:
+ "@\"LAEnvironmentServiceXPCClient\""
+ "Failed to obtain environment endpoint %{public}@"
+ "LAEnvironmentServiceXPCClient"
+ "_xpcClient"
+ "interfaceForXPCProtocol:"
+ "synchronousProxyToEnvironmentServiceWithCompletion:"
- "@\"NSXPCListenerEndpoint\""
- "_environmentServiceEndpoint"
- "_environmentServiceEndpointWithCompletion:"
- "_synchronousProxyToEnvironmentServiceWithCompletion:"
- "remoteObjectInterface"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setWithObjects:"

```
