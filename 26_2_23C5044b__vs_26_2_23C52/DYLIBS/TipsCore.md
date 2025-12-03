## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

 822.2.8.0.0
-  __TEXT.__text: 0xa1af0
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0x8390
-  __TEXT.__const: 0x20d4
-  __TEXT.__cstring: 0x6107
-  __TEXT.__oslogstring: 0x1222
-  __TEXT.__gcc_except_tab: 0xfe4
+  __TEXT.__text: 0xa2990
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0x83c0
+  __TEXT.__const: 0x20e4
+  __TEXT.__cstring: 0x61a7
+  __TEXT.__oslogstring: 0x1269
+  __TEXT.__gcc_except_tab: 0x1048
   __TEXT.__ustring: 0x118
+  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x1378
   __TEXT.__swift5_typeref: 0xe02
   __TEXT.__swift5_reflstr: 0xd22

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x44
-  __TEXT.__unwind_info: 0x2fc8
+  __TEXT.__unwind_info: 0x2ff8
   __TEXT.__eh_frame: 0x16d8
   __TEXT.__objc_classname: 0xded
-  __TEXT.__objc_methname: 0xef85
-  __TEXT.__objc_methtype: 0x18f5
-  __TEXT.__objc_stubs: 0x9820
+  __TEXT.__objc_methname: 0xf0c2
+  __TEXT.__objc_methtype: 0x1925
+  __TEXT.__objc_stubs: 0x9980
   __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x20c0
+  __DATA_CONST.__const: 0x2140
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a60
+  __DATA_CONST.__objc_selrefs: 0x3ab0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__auth_got: 0xfb0
   __AUTH_CONST.__const: 0x3138
-  __AUTH_CONST.__cfstring: 0x52e0
-  __AUTH_CONST.__objc_const: 0xdda8
+  __AUTH_CONST.__cfstring: 0x5320
+  __AUTH_CONST.__objc_const: 0xde08
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1550
   __AUTH.__data: 0xba8
-  __DATA.__objc_ivar: 0x7b4
+  __DATA.__objc_ivar: 0x7bc
   __DATA.__data: 0x10d0
-  __DATA.__bss: 0x1bb0
+  __DATA.__bss: 0x1bc0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2748
   __DATA_DIRTY.__data: 0x648
-  __DATA_DIRTY.__bss: 0x548
+  __DATA_DIRTY.__bss: 0x560
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
   - /System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC08B594-205E-332E-90CB-1774DFA9E3C6
-  Functions: 4838
-  Symbols:   9911
-  CStrings:  4988
+  UUID: 907BD8F8-634E-3672-B877-12DD1230E9D6
+  Functions: 4857
+  Symbols:   9982
+  CStrings:  5018
 
Symbols:
+ -[TPSURLSessionACAuthHandler setSsoAuthenticator:]
+ -[TPSURLSessionACAuthHandler ssoAuthenticator]
+ -[TPSURLSessionManager _mappedURLRequest:].cold.1
+ -[TPSURLSessionManager setUrlRedirector:]
+ -[TPSURLSessionManager urlRedirector]
+ _OBJC_IVAR_$_TPSURLSessionACAuthHandler._ssoAuthenticator
+ _OBJC_IVAR_$_TPSURLSessionManager._urlRedirector
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ _PingPongClientLibraryCore.frameworkLibrary
+ ___132-[TPSURLSessionManager newURLSessionItemWithRequest:identifier:attributionIdentifier:requestType:networkDelegate:completionHandler:]_block_invoke.25
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke_2
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke_2.cold.1
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke_2.cold.2
+ ___81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.29.cold.1
+ ___81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.30
+ ___PingPongClientLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke.cold.1
+ ___getPPCRedirectClass_block_invoke
+ ___getPPCRedirectClass_block_invoke.cold.1
+ ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
+ ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringPingPongClient
+ _dlerror
+ _dlsym
+ _getPPCExtensibleSSOAuthenticatorClass.softClass
+ _getPPCRedirectClass.softClass
+ _getkExtensibleSSOTokenKeySymbolLoc.ptr
+ _getkExtensibleSSOUsernameKeySymbolLoc.ptr
+ _objc_getClass
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$allHTTPHeaderFields
+ _objc_msgSend$authenticateWithCompletion:
+ _objc_msgSend$customHeaderFields
+ _objc_msgSend$mappedURL:
+ _objc_msgSend$setEnvIdentifier:
+ _objc_msgSend$setInteractivity:
+ _objc_msgSend$setSsoAuthenticator:
+ _objc_msgSend$setUrlRedirector:
+ _objc_msgSend$ssoAuthenticator
+ _objc_msgSend$urlRedirector
- ___132-[TPSURLSessionManager newURLSessionItemWithRequest:identifier:attributionIdentifier:requestType:networkDelegate:completionHandler:]_block_invoke.24
- ___81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.28
- ___81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.28.cold.1
CStrings:
+ "@\"PPCExtensibleSSOAuthenticator\""
+ "@\"PPCRedirect\""
+ "Mapped URL Request: %@"
+ "PPCExtensibleSSOAuthenticator"
+ "PPCRedirect"
+ "PPCRedirect initialized."
+ "PPCRedirect not found."
+ "T@\"PPCExtensibleSSOAuthenticator\",&,N,V_ssoAuthenticator"
+ "T@\"PPCRedirect\",&,N,V_urlRedirector"
+ "Unable to find class %s"
+ "X-AppleConnect-Token"
+ "X-AppleConnect-User"
+ "_ssoAuthenticator"
+ "_urlRedirector"
+ "addEntriesFromDictionary:"
+ "allHTTPHeaderFields"
+ "authenticateWithCompletion:"
+ "kExtensibleSSOTokenKey"
+ "kExtensibleSSOUsernameKey"
+ "mappedURL:"
+ "setEnvIdentifier:"
+ "setInteractivity:"
+ "setSsoAuthenticator:"
+ "setUrlRedirector:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
+ "ssoAuthenticator"
+ "urlRedirector"

```
