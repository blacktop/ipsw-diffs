## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-620.1.11.10.8
-  __TEXT.__text: 0xb6964
-  __TEXT.__auth_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x2638
+620.1.14.10.4
+  __TEXT.__text: 0xb8580
+  __TEXT.__auth_stubs: 0x2210
+  __TEXT.__objc_methlist: 0x2708
   __TEXT.__const: 0x7990
-  __TEXT.__cstring: 0x41e2
-  __TEXT.__oslogstring: 0x3830
-  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__cstring: 0x43a2
+  __TEXT.__oslogstring: 0x3a40
+  __TEXT.__gcc_except_tab: 0x2ec
   __TEXT.__ustring: 0x590
   __TEXT.__dlopen_cstrs: 0x48
   __TEXT.__swift5_typeref: 0x1ca5

   __TEXT.__swift5_capture: 0x408
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3070
+  __TEXT.__unwind_info: 0x30f0
   __TEXT.__eh_frame: 0x36e0
-  __TEXT.__objc_classname: 0x712
-  __TEXT.__objc_methname: 0x9b60
-  __TEXT.__objc_methtype: 0x251d
-  __TEXT.__objc_stubs: 0x4000
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__const: 0x968
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__objc_classname: 0x78d
+  __TEXT.__objc_methname: 0x9d31
+  __TEXT.__objc_methtype: 0x25f6
+  __TEXT.__objc_stubs: 0x40e0
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1798
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0x17d8
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1120
-  __AUTH_CONST.__auth_ptr: 0x6b8
-  __AUTH_CONST.__const: 0x5620
-  __AUTH_CONST.__cfstring: 0x1d60
-  __AUTH_CONST.__objc_const: 0x7880
+  __AUTH_CONST.__auth_got: 0x1118
+  __AUTH_CONST.__auth_ptr: 0x6c0
+  __AUTH_CONST.__const: 0x5640
+  __AUTH_CONST.__cfstring: 0x1e40
+  __AUTH_CONST.__objc_const: 0x7bf8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x3c8
-  __DATA.__data: 0x24f0
-  __DATA.__bss: 0xfbd0
-  __DATA.__common: 0x200
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x3f0
+  __DATA.__data: 0x22d0
+  __DATA.__bss: 0xed60
+  __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0x1cb8
-  __DATA_DIRTY.__data: 0xf40
-  __DATA_DIRTY.__bss: 0xa0
-  __DATA_DIRTY.__common: 0x28
+  __DATA_DIRTY.__data: 0x1240
+  __DATA_DIRTY.__bss: 0xf20
+  __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4348
-  Symbols:   1521
-  CStrings:  2306
+  Functions: 4386
+  Symbols:   1577
+  CStrings:  2344
 
Symbols:
+ _ASCAgentCredentialExchangeListenerInterface
+ _ASCAgentCredentialExchangeServiceName
+ _ASCAuthorizationCredentialExchangeDataKey
+ _ASCAuthorizationCredentialExchangeExporterBundleIDKey
+ _OBJC_CLASS_$_ASCAgentCredentialExchangeListener
+ _OBJC_CLASS_$_ASCAgentCredentialExchangeListenerProxy
+ _OBJC_METACLASS_$_ASCAgentCredentialExchangeListener
+ _OBJC_METACLASS_$_ASCAgentCredentialExchangeListenerProxy
+ _SFCredentialProviderDeveloperEntitlement
+ _SFCredentialProviderSystemEntitlement
CStrings:
+ "\x01\x15"
+ "\b\x11"
+ "@\"ASCAuthorizationPresenter\""
+ "ASCAgentCredentialExchangeListener"
+ "ASCAgentCredentialExchangeListenerInterface"
+ "ASCAgentCredentialExchangeListenerProxy"
+ "ASCAuthorizationCredentialExchangeData"
+ "ASCAuthorizationCredentialExchangeExporterBundleID"
+ "Connection to AuthenticationServicesAgent closed"
+ "Credential Exchange listener"
+ "Developer mode must be enabled for this API. You can find the toggle for this in Settings > Developer in the Authentication Services Testing section."
+ "Export not available because passcode and/or biometrics are not enabled"
+ "Exported credential data not found"
+ "Exported credential data not found."
+ "Invalid importer token"
+ "No apps available for import"
+ "Rejecting connection from unentitled process"
+ "The import request came from a client that did not match the one selected by the user for import."
+ "Token for importer must only be set by the view service"
+ "Unable to get exporting app's bundle ID"
+ "_atLeastOneAppAvailableForImportForConnection:"
+ "_exportedCredentialData"
+ "_importerBundleID"
+ "_importerToken"
+ "_presentExportFlowResultHandler"
+ "_presenter"
+ "atLeastOneAvailableExtensionSupportsCredentialExchange:"
+ "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange"
+ "exportCredentials:windowSceneIdentifier:completionHandler:"
+ "importCredentialsWithToken:completionHandler:"
+ "isCredentialExchangeEnabled"
+ "presentExportFlowWithData:forProcess:windowSceneIdentifier:completionHandler:"
+ "safari_isHostOrSubdomainOfHost:"
+ "setTokenForImport:"
+ "v24@0:8@\"NSUUID\"16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"BSProcessHandle\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "\xa1"
- "\b"
- "conditionalMediation"
- "\x91"

```
