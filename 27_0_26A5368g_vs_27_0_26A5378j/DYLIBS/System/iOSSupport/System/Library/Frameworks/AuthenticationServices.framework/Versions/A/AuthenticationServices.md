## AuthenticationServices

> `/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-  __TEXT.__text: 0xf3a74
-  __TEXT.__objc_methlist: 0x55c0
-  __TEXT.__const: 0x123b4
-  __TEXT.__gcc_except_tab: 0x1024
+  __TEXT.__text: 0xf2e60
+  __TEXT.__objc_methlist: 0x54a0
+  __TEXT.__const: 0x12394
+  __TEXT.__gcc_except_tab: 0xfec
   __TEXT.__cstring: 0x56db
-  __TEXT.__oslogstring: 0x236b
+  __TEXT.__oslogstring: 0x22fb
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__ustring: 0x3608
   __TEXT.__swift5_typeref: 0x297c

   __TEXT.__swift_as_ret: 0x228
   __TEXT.__swift_as_cont: 0x40c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x4a78
+  __TEXT.__unwind_info: 0x4a28
   __TEXT.__eh_frame: 0x5a7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__const: 0x1270
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x230
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b10
-  __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x2a90
+  __DATA_CONST.__objc_protorefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0xb20
-  __AUTH_CONST.__const: 0x8220
-  __AUTH_CONST.__cfstring: 0x2ca0
-  __AUTH_CONST.__objc_const: 0xbd68
+  __DATA_CONST.__got: 0xb10
+  __AUTH_CONST.__const: 0x81e0
+  __AUTH_CONST.__cfstring: 0x2cc0
+  __AUTH_CONST.__objc_const: 0xbbd0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x13b8
-  __AUTH.__objc_data: 0x28a8
-  __AUTH.__data: 0x1420
-  __DATA.__objc_ivar: 0x570
-  __DATA.__data: 0x2e20
-  __DATA.__bss: 0x10d80
+  __AUTH_CONST.__auth_got: 0x13a8
+  __AUTH.__objc_data: 0x2668
+  __AUTH.__data: 0x13f0
+  __DATA.__objc_ivar: 0x560
+  __DATA.__data: 0x2d60
+  __DATA.__bss: 0x10d60
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x6b8
-  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__objc_data: 0x8a8
+  __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6529
-  Symbols:   6506
+  Functions: 6501
+  Symbols:   6428
   CStrings:  1165
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ __86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2
+ ___86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2
+ _objc_msgSend$shouldCurrentProcessShowPasswordManagerServiceNames
- -[ASAuthorizationController _deviceLoginListenerProxy]
- -[ASAuthorizationController _isPasskeyAssertionRequestForDeviceLoginWithContext:]
- -[ASAuthorizationController isRequestingPasskeyAssertionForDeviceLogin]
- -[ASAuthorizationController setIsRequestingPasskeyAssertionForDeviceLogin:]
- -[_ASDeviceLoginPresentationProxy .cxx_destruct]
- -[_ASDeviceLoginPresentationProxy _reconnectIfNecessary]
- -[_ASDeviceLoginPresentationProxy _remoteObjectProxyWithErrorHandler:]
- -[_ASDeviceLoginPresentationProxy _setUpConnection:]
- -[_ASDeviceLoginPresentationProxy cancelCurrentRequest]
- -[_ASDeviceLoginPresentationProxy clientWillAuthenticate]
- -[_ASDeviceLoginPresentationProxy clientWillConnect]
- -[_ASDeviceLoginPresentationProxy delegate]
- -[_ASDeviceLoginPresentationProxy init]
- -[_ASDeviceLoginPresentationProxy presentWithQRCodeURL:serviceName:]
- -[_ASDeviceLoginPresentationProxy setDelegate:]
- -[_ASDeviceLoginPresentationProxy shouldDismiss]
- GCC_except_table45
- OBJC_IVAR_$_ASAuthorizationController._deviceLoginListenerProxy
- OBJC_IVAR_$_ASAuthorizationController._isRequestingPasskeyAssertionForDeviceLogin
- OBJC_IVAR_$__ASDeviceLoginPresentationProxy._connection
- OBJC_IVAR_$__ASDeviceLoginPresentationProxy._delegate
- _ASDeviceLoginPresentationClientInterface.interface
- _ASDeviceLoginPresentationClientInterface.onceToken
- _ASDeviceLoginPresentationDaemonInterface.interface
- _ASDeviceLoginPresentationDaemonInterface.onceToken
- _OBJC_CLASS_$_ASCDeviceLoginListenerProxy
- _OBJC_CLASS_$__ASDeviceLoginPresentationProxy
- _OBJC_METACLASS_$__ASDeviceLoginPresentationProxy
- __47-[_ASDeviceLoginPresentationProxy setDelegate:]_block_invoke
- __52-[_ASDeviceLoginPresentationProxy _setUpConnection:]_block_invoke
- __55-[_ASDeviceLoginPresentationProxy cancelCurrentRequest]_block_invoke
- __70-[_ASDeviceLoginPresentationProxy _remoteObjectProxyWithErrorHandler:]_block_invoke
- __86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke
- __OBJC_$_INSTANCE_METHODS__ASDeviceLoginPresentationProxy
- __OBJC_$_INSTANCE_VARIABLES__ASDeviceLoginPresentationProxy
- __OBJC_$_PROP_LIST__ASDeviceLoginPresentationProxy
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCDeviceLoginPresentationClientProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCDeviceLoginPresentationDaemonProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASCDeviceLoginPresentationClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASCDeviceLoginPresentationDaemonProtocol
- __OBJC_CLASS_PROTOCOLS_$__ASDeviceLoginPresentationProxy
- __OBJC_CLASS_RO_$__ASDeviceLoginPresentationProxy
- __OBJC_LABEL_PROTOCOL_$_ASCDeviceLoginPresentationClientProtocol
- __OBJC_LABEL_PROTOCOL_$_ASCDeviceLoginPresentationDaemonProtocol
- __OBJC_METACLASS_RO_$__ASDeviceLoginPresentationProxy
- __OBJC_PROTOCOL_$_ASCDeviceLoginPresentationClientProtocol
- __OBJC_PROTOCOL_$_ASCDeviceLoginPresentationDaemonProtocol
- __OBJC_PROTOCOL_REFERENCE_$_ASCDeviceLoginPresentationClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_ASCDeviceLoginPresentationDaemonProtocol
- ___47-[_ASDeviceLoginPresentationProxy setDelegate:]_block_invoke
- ___48-[_ASDeviceLoginPresentationProxy shouldDismiss]_block_invoke
- ___52-[_ASDeviceLoginPresentationProxy _setUpConnection:]_block_invoke
- ___52-[_ASDeviceLoginPresentationProxy clientWillConnect]_block_invoke
- ___55-[_ASDeviceLoginPresentationProxy cancelCurrentRequest]_block_invoke
- ___57-[_ASDeviceLoginPresentationProxy clientWillAuthenticate]_block_invoke
- ___68-[_ASDeviceLoginPresentationProxy presentWithQRCodeURL:serviceName:]_block_invoke
- ___70-[_ASDeviceLoginPresentationProxy _remoteObjectProxyWithErrorHandler:]_block_invoke
- ____ASDeviceLoginPresentationClientInterface_block_invoke
- ____ASDeviceLoginPresentationDaemonInterface_block_invoke
- ___block_descriptor_40_e17_v16?0"NSError"8l
- _getuid
- _objc_msgSend$_deviceLoginListenerProxy
- _objc_msgSend$_isPasskeyAssertionRequestForDeviceLoginWithContext:
- _objc_msgSend$_xpcConnection
- _objc_msgSend$absoluteString
- _objc_msgSend$didSetPresentationDelegate
- _objc_msgSend$dismissPasskeyDeviceLogin
- _objc_msgSend$initWithMessage:
- _objc_msgSend$passkeyHybridClientWillAuthenticate
- _objc_msgSend$passkeyHybridClientWillConnect
- _objc_msgSend$performPasskeyAssertionRequestForContext:withCompletionHandler:
- _objc_msgSend$presentPasskeyDeviceLoginWithQRCodeView:serviceName:
- _objc_msgSend$requestTypes
- _xpc_connection_set_non_launching
CStrings:
+ "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2"
+ "An export is currently in progress. Please try again in a few minutes."
+ "Export in progress"
+ "\x92"
- "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke"
- "Notifying %{mask.hash}@ to dismiss"
- "Notifying %{mask.hash}@ to present passkey assertion flow for %{public}@"
- "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.login.non-launching"
- "\xa2"

```
