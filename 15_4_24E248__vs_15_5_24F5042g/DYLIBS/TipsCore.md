## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore`

```diff

 778.4.3.0.0
-  __TEXT.__text: 0x9b2b0
-  __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x80f4
-  __TEXT.__const: 0x1678
-  __TEXT.__cstring: 0x5663
-  __TEXT.__oslogstring: 0x1205
-  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__text: 0x9a2e8
+  __TEXT.__auth_stubs: 0x19b0
+  __TEXT.__objc_methlist: 0x80c4
+  __TEXT.__const: 0x1668
+  __TEXT.__cstring: 0x5543
+  __TEXT.__oslogstring: 0x11be
+  __TEXT.__gcc_except_tab: 0x101c
   __TEXT.__ustring: 0x118
-  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0xf30
   __TEXT.__swift5_typeref: 0xb40
   __TEXT.__swift5_reflstr: 0xbb2

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__unwind_info: 0x2d78
+  __TEXT.__unwind_info: 0x2d48
   __TEXT.__eh_frame: 0x1180
   __TEXT.__objc_classname: 0xda2
-  __TEXT.__objc_methname: 0xeca1
-  __TEXT.__objc_methtype: 0x184a
-  __TEXT.__objc_stubs: 0x9600
+  __TEXT.__objc_methname: 0xeb64
+  __TEXT.__objc_methtype: 0x181a
+  __TEXT.__objc_stubs: 0x94a0
   __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__const: 0x12e8
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3980
+  __DATA_CONST.__objc_selrefs: 0x3930
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH_CONST.__auth_got: 0xce8
   __AUTH_CONST.__auth_ptr: 0x4c8
-  __AUTH_CONST.__const: 0x36b0
-  __AUTH_CONST.__cfstring: 0x53c0
-  __AUTH_CONST.__objc_const: 0xd318
+  __AUTH_CONST.__const: 0x3650
+  __AUTH_CONST.__cfstring: 0x5380
+  __AUTH_CONST.__objc_const: 0xd2b8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3a20
   __AUTH.__data: 0x920
-  __DATA.__objc_ivar: 0x7a4
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x11a0
-  __DATA.__bss: 0x1d20
+  __DATA.__bss: 0x1cf0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/Versions/A/NetAppsUtilities
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4537
-  Symbols:   6992
-  CStrings:  4251
+  Functions: 4518
+  Symbols:   6941
+  CStrings:  4221
 
Symbols:
+ __132-[TPSURLSessionManager newURLSessionItemWithRequest:identifier:attributionIdentifier:requestType:networkDelegate:completionHandler:]_block_invoke.24
+ __81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.28
+ __81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.28.cold.1
- -[TPSURLSessionACAuthHandler setSsoAuthenticator:]
- -[TPSURLSessionACAuthHandler ssoAuthenticator]
- -[TPSURLSessionManager _mappedURLRequest:].cold.1
- -[TPSURLSessionManager setUrlRedirector:]
- -[TPSURLSessionManager urlRedirector]
- OBJC_IVAR_$_TPSURLSessionACAuthHandler._ssoAuthenticator
- OBJC_IVAR_$_TPSURLSessionManager._urlRedirector
- PingPongClientLibraryCore.frameworkLibrary
- _PingPongClientLibrary
- _PingPongClientLibraryCore
- __132-[TPSURLSessionManager newURLSessionItemWithRequest:identifier:attributionIdentifier:requestType:networkDelegate:completionHandler:]_block_invoke.25
- __60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke.28
- __60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke.28.cold.1
- __60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke.28.cold.2
- __81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.29.cold.1
- __81-[TPSURLSessionManager URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.30
- ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
- ___PingPongClientLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16l
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
- ___getPPCRedirectClass_block_invoke
- ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
- ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
- __getPPCExtensibleSSOAuthenticatorClass_block_invoke.cold.1
- __getPPCRedirectClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringPingPongClient
- _dlerror
- _dlsym
- _objc_getClass
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$allHTTPHeaderFields
- _objc_msgSend$authenticateWithCompletion:
- _objc_msgSend$customHeaderFields
- _objc_msgSend$mappedURL:
- _objc_msgSend$setEnvIdentifier:
- _objc_msgSend$setInteractivity:
- _objc_msgSend$setSsoAuthenticator:
- _objc_msgSend$setUrlRedirector:
- _objc_msgSend$ssoAuthenticator
- _objc_msgSend$urlRedirector
- getPPCExtensibleSSOAuthenticatorClass.softClass
- getPPCRedirectClass.softClass
- getkExtensibleSSOTokenKeySymbolLoc.ptr
- getkExtensibleSSOUsernameKeySymbolLoc.ptr
CStrings:
+ "\x125"
- "\x126"
- "/System/Library/PrivateFrameworks/PingPongClient.framework/Contents/MacOS/PingPongClient"
- "@\"PPCExtensibleSSOAuthenticator\""
- "@\"PPCRedirect\""
- "Mapped URL Request: %@"
- "PPCExtensibleSSOAuthenticator"
- "PPCRedirect"
- "PPCRedirect initialized."
- "PPCRedirect not found."
- "T@\"PPCExtensibleSSOAuthenticator\",&,N,V_ssoAuthenticator"
- "T@\"PPCRedirect\",&,N,V_urlRedirector"
- "Unable to find class %s"
- "X-AppleConnect-Token"
- "X-AppleConnect-User"
- "_ssoAuthenticator"
- "_urlRedirector"
- "addEntriesFromDictionary:"
- "allHTTPHeaderFields"
- "authenticateWithCompletion:"
- "kExtensibleSSOTokenKey"
- "kExtensibleSSOUsernameKey"
- "mappedURL:"
- "setEnvIdentifier:"
- "setInteractivity:"
- "setSsoAuthenticator:"
- "setUrlRedirector:"
- "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
- "ssoAuthenticator"
- "urlRedirector"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
