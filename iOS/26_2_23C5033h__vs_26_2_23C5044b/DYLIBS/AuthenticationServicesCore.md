## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-623.1.13.10.3
-  __TEXT.__text: 0xc7120
+623.1.14.10.6
+  __TEXT.__text: 0xc766c
   __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x39b4
+  __TEXT.__objc_methlist: 0x39dc
   __TEXT.__const: 0xca78
-  __TEXT.__cstring: 0x5992
-  __TEXT.__oslogstring: 0x4010
-  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__cstring: 0x59f2
+  __TEXT.__oslogstring: 0x4060
+  __TEXT.__gcc_except_tab: 0x324
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48
   __TEXT.__swift5_typeref: 0x23d3

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3468
+  __TEXT.__unwind_info: 0x3488
   __TEXT.__eh_frame: 0x44f8
   __TEXT.__objc_classname: 0x7aa
-  __TEXT.__objc_methname: 0xb35d
-  __TEXT.__objc_methtype: 0x2a7c
-  __TEXT.__objc_stubs: 0x46e0
+  __TEXT.__objc_methname: 0xb435
+  __TEXT.__objc_methtype: 0x2a95
+  __TEXT.__objc_stubs: 0x4720
   __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0xc80
+  __DATA_CONST.__const: 0xca8
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc8
+  __DATA_CONST.__objc_selrefs: 0x1de8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1310
-  __AUTH_CONST.__const: 0x6388
+  __AUTH_CONST.__const: 0x63a8
   __AUTH_CONST.__cfstring: 0x2040
   __AUTH_CONST.__objc_const: 0x7bf8
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9A8A51A-1BA8-39A9-B350-192DA8104925
-  Functions: 4911
-  Symbols:   5398
-  CStrings:  2879
+  UUID: D3F2B5AD-FE39-3690-831D-893B34732C06
+  Functions: 4920
+  Symbols:   5423
+  CStrings:  2886
 
Symbols:
+ -[ASCAgent getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]
+ -[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:]
+ -[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:].cold.1
+ -[ASCAgentProxy _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]
+ GCC_except_table33
+ GCC_except_table72
+ ___37-[ASCAgentProxy cancelCurrentRequest]_block_invoke.21
+ ___62-[ASCAgentProxy isDeviceConfiguredForPasskeysWithTestOptions:]_block_invoke.13
+ ___62-[ASCAgentProxy isDeviceConfiguredForPasskeysWithTestOptions:]_block_invoke.14
+ ___72-[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:]_block_invoke
+ ___72-[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:]_block_invoke.5
+ ___72-[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:]_block_invoke.5.cold.1
+ ___72-[ASCAgentProxy _remoteObjectProxyForSynchronousCalls:withErrorHandler:]_block_invoke.cold.1
+ ___74-[ASCAgentProxy openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.11
+ ___78-[ASCAgent getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke
+ ___78-[ASCAgent getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke.cold.1
+ ___78-[ASCAgentProxy browserPasskeysForRelyingParty:testOptions:completionHandler:]_block_invoke.12
+ ___78-[ASCAgentProxy performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.8
+ ___83-[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke
+ ___83-[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke.18
+ ___83-[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke_2
+ ___83-[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_literal_global.17
+ _objc_msgSend$_remoteObjectProxyForSynchronousCalls:withErrorHandler:
+ _objc_msgSend$getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- -[ASCAgent isDeviceConfiguredForPasskeysWithTestOptions:]
- -[ASCAgentProxy _remoteObjectProxyWithErrorHandler:].cold.1
- GCC_except_table64
- ___37-[ASCAgentProxy cancelCurrentRequest]_block_invoke.15
- ___52-[ASCAgentProxy _remoteObjectProxyWithErrorHandler:]_block_invoke
- ___52-[ASCAgentProxy _remoteObjectProxyWithErrorHandler:]_block_invoke.cold.1
- ___57-[ASCAgent isDeviceConfiguredForPasskeysWithTestOptions:]_block_invoke
- ___57-[ASCAgent isDeviceConfiguredForPasskeysWithTestOptions:]_block_invoke.cold.1
- ___62-[ASCAgentProxy isDeviceConfiguredForPasskeysWithTestOptions:]_block_invoke.12
- ___74-[ASCAgentProxy openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.10
- ___78-[ASCAgentProxy browserPasskeysForRelyingParty:testOptions:completionHandler:]_block_invoke.11
- ___78-[ASCAgentProxy performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.7
- ___block_literal_global.14
- _objc_msgSend$isDeviceConfiguredForPasskeysWithTestOptions:
CStrings:
+ "-[ASCAgentProxy getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:]_block_invoke"
+ "@28@0:8B16@?20"
+ "Synchronous remote proxy object error handler invoked with error: %{public}@"
+ "_remoteObjectProxyForSynchronousCalls:withErrorHandler:"
+ "_synchronousRemoteObjectProxyWithErrorHandler:"
+ "getIsDeviceConfiguredForPasskeysWithTestOptions:completionHandler:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v32@0:8@\"_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions\"16@?<v@?B>24"
- "B24@0:8@\"_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions\"16"

```
