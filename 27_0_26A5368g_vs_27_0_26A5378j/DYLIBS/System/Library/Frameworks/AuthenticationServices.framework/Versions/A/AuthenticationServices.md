## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-  __TEXT.__text: 0x1194f4
-  __TEXT.__objc_methlist: 0x80b4
-  __TEXT.__const: 0x12804
+  __TEXT.__text: 0x118c00
+  __TEXT.__objc_methlist: 0x8014
+  __TEXT.__const: 0x127f4
   __TEXT.__cstring: 0xb198
   __TEXT.__ustring: 0x65ac
-  __TEXT.__oslogstring: 0x33e8
-  __TEXT.__gcc_except_tab: 0x1284
+  __TEXT.__oslogstring: 0x3378
+  __TEXT.__gcc_except_tab: 0x124c
   __TEXT.__dlopen_cstrs: 0x25e
   __TEXT.__swift5_typeref: 0x2ae0
   __TEXT.__constg_swiftt: 0x1ee4

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_capture: 0xc14
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__unwind_info: 0x5288
+  __TEXT.__unwind_info: 0x5250
   __TEXT.__eh_frame: 0x5638
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x890
-  __DATA_CONST.__objc_classlist: 0x540
+  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x2c8
+  __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c38
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x350
+  __DATA_CONST.__objc_selrefs: 0x4c08
+  __DATA_CONST.__objc_protorefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __DATA_CONST.__got: 0xee0
-  __AUTH_CONST.__const: 0x9ec0
-  __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0xfc40
+  __DATA_CONST.__got: 0xed8
+  __AUTH_CONST.__const: 0x9e80
+  __AUTH_CONST.__cfstring: 0x4900
+  __AUTH_CONST.__objc_const: 0xfb08
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x13a0
-  __AUTH.__objc_data: 0x32f0
-  __AUTH.__data: 0x1410
-  __DATA.__objc_ivar: 0x7a0
-  __DATA.__data: 0x34d0
-  __DATA.__bss: 0x10c40
+  __AUTH_CONST.__auth_got: 0x1398
+  __AUTH.__objc_data: 0x30b0
+  __AUTH.__data: 0x13f0
+  __DATA.__objc_ivar: 0x798
+  __DATA.__data: 0x3410
+  __DATA.__bss: 0x10c20
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__data: 0xa0
+  __DATA_DIRTY.__objc_data: 0xa60
+  __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7504
-  Symbols:   9101
-  CStrings:  1828
+  Functions: 7489
+  Symbols:   9043
+  CStrings:  1826
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[ASAuthorizationServiceViewController _credentialRequiresDismissalFromViewService:]
+ -[ASAuthorizationServiceViewController _dismissOnMainQueue]
+ -[ASAuthorizationServiceViewController authorizationViewController:deliverCredentialToClient:error:]
+ -[ASAuthorizationServiceViewController authorizationViewControllerDismiss:]
+ -[ASAuthorizationServiceViewController awaitSheetDismissalWithHandler:]
+ -[ASAuthorizationServiceViewController dismiss]
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table41
+ GCC_except_table47
+ OBJC_IVAR_$_ASAuthorizationServiceViewController._dismissalHandler
+ OBJC_IVAR_$_ASCredentialRequestConfirmButtonSubPane._selectedLoginChoice
+ __59-[ASAuthorizationServiceViewController _dismissOnMainQueue]_block_invoke
+ __86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2
+ ___47-[ASAuthorizationServiceViewController dismiss]_block_invoke
+ ___59-[ASAuthorizationServiceViewController _dismissOnMainQueue]_block_invoke
+ ___71-[ASAuthorizationServiceViewController awaitSheetDismissalWithHandler:]_block_invoke
+ ___75-[ASAuthorizationServiceViewController authorizationViewControllerDismiss:]_block_invoke
+ ___86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2
+ _objc_msgSend$_credentialRequiresDismissalFromViewService:
+ _objc_msgSend$_dismissOnMainQueue
+ _objc_msgSend$dismiss
+ _objc_msgSend$passkeyHeaderWithTitle:subtitle:
+ _objc_msgSend$setFastAnimations:
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
- GCC_except_table32
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
- _objc_msgSend$_deviceLoginListenerProxy
- _objc_msgSend$_isPasskeyAssertionRequestForDeviceLoginWithContext:
- _objc_msgSend$_xpcConnection
- _objc_msgSend$didSetPresentationDelegate
- _objc_msgSend$dismissPasskeyDeviceLogin
- _objc_msgSend$passkeyHybridClientWillAuthenticate
- _objc_msgSend$passkeyHybridClientWillConnect
- _objc_msgSend$performPasskeyAssertionRequestForContext:withCompletionHandler:
- _objc_msgSend$presentPasskeyDeviceLoginWithQRCodeView:serviceName:
- _xpc_connection_set_non_launching
CStrings:
+ "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2"
+ "An export is currently in progress. Please try again in a few minutes."
+ "Export in progress"
+ "\xa2"
+ "\xd1"
- "\f"
- "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke"
- "Notifying %{mask.hash}@ to dismiss"
- "Notifying %{mask.hash}@ to present passkey assertion flow for %{public}@"
- "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.login.non-launching"
- "\xb2"
- "\xc1"
- "\xf1"

```
