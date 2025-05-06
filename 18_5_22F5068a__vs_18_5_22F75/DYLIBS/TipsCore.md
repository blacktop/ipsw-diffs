## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

 778.5.1.0.0
-  __TEXT.__text: 0x917d0
-  __TEXT.__auth_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x804c
+  __TEXT.__text: 0x9264c
+  __TEXT.__auth_stubs: 0x1bd0
+  __TEXT.__objc_methlist: 0x807c
   __TEXT.__const: 0x1818
-  __TEXT.__cstring: 0x54f3
-  __TEXT.__oslogstring: 0x120e
-  __TEXT.__gcc_except_tab: 0x1028
+  __TEXT.__cstring: 0x55a3
+  __TEXT.__oslogstring: 0x1255
+  __TEXT.__gcc_except_tab: 0x108c
   __TEXT.__ustring: 0x118
-  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__dlopen_cstrs: 0x10c
   __TEXT.__constg_swiftt: 0xf30
   __TEXT.__swift5_typeref: 0xb40
   __TEXT.__swift5_reflstr: 0xbb2

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__unwind_info: 0x2d00
+  __TEXT.__unwind_info: 0x2d50
   __TEXT.__eh_frame: 0x11a8
   __TEXT.__objc_classname: 0xda4
-  __TEXT.__objc_methname: 0xe9dc
-  __TEXT.__objc_methtype: 0x181a
-  __TEXT.__objc_stubs: 0x9520
+  __TEXT.__objc_methname: 0xeb19
+  __TEXT.__objc_methtype: 0x184a
+  __TEXT.__objc_stubs: 0x9680
   __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x1fc0
+  __DATA_CONST.__const: 0x2018
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38f0
+  __DATA_CONST.__objc_selrefs: 0x3940
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__const: 0x27e0
-  __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0xd1c8
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0xd228
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x1360
   __AUTH.__data: 0x540
-  __DATA.__objc_ivar: 0x788
+  __DATA.__objc_ivar: 0x790
   __DATA.__data: 0xf18
-  __DATA.__bss: 0x17b0
+  __DATA.__bss: 0x17c0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x26c0
   __DATA_DIRTY.__data: 0x708
-  __DATA_DIRTY.__bss: 0x560
+  __DATA_DIRTY.__bss: 0x578
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4441
-  Symbols:   9611
-  CStrings:  4200
+  Functions: 4459
+  Symbols:   9677
+  CStrings:  4228
 
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
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke.cold.1
+ ___getPPCRedirectClass_block_invoke
+ ___getPPCRedirectClass_block_invoke.cold.1
+ ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
+ ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
+ _audit_stringPingPongClient
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
+ "\x126"
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
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "\x125"

```
