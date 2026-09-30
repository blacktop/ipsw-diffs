## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

 198.0.0.0.0
-  __TEXT.__text: 0x28ad4
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x3434
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xc70
-  __TEXT.__cstring: 0x18e8
+  __TEXT.__text: 0x27ab0
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x3404
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0xc04
+  __TEXT.__cstring: 0x184f
   __TEXT.__oslogstring: 0x329
-  __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0xa60
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methname: 0x9849
-  __TEXT.__objc_methtype: 0x1da9
-  __TEXT.__objc_stubs: 0x7400
+  __TEXT.__objc_methname: 0x9749
+  __TEXT.__objc_methtype: 0x1d79
+  __TEXT.__objc_stubs: 0x72c0
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0xed0
+  __DATA_CONST.__const: 0xe38
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2570
+  __DATA_CONST.__objc_selrefs: 0x2530
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x2bc0
-  __AUTH_CONST.__objc_const: 0x4fd8
+  __AUTH_CONST.__objc_const: 0x4f78
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x410
+  __DATA.__objc_ivar: 0x408
   __DATA.__data: 0x858
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFEA4622-8732-30D4-A8FC-FDB0E93C64EA
-  Functions: 1104
-  Symbols:   4272
-  CStrings:  2703
+  UUID: FF436D4A-5C57-36DA-AAE3-603A565D35B3
+  Functions: 1083
+  Symbols:   4195
+  CStrings:  2681
 
Symbols:
+ ___98-[HLPURLSessionManager newURLSessionItemWithRequest:identifier:networkDelegate:completionHandler:]_block_invoke.22
- -[HLPURLSessionACAuthHandler setSsoAuthenticator:]
- -[HLPURLSessionACAuthHandler ssoAuthenticator]
- -[HLPURLSessionManager setUrlRedirector:]
- -[HLPURLSessionManager urlRedirector]
- _OBJC_IVAR_$_HLPURLSessionACAuthHandler._ssoAuthenticator
- _OBJC_IVAR_$_HLPURLSessionManager._urlRedirector
- _PingPongClientLibrary
- _PingPongClientLibraryCore
- _PingPongClientLibraryCore.frameworkLibrary
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2.cold.1
- ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2.cold.2
- ___98-[HLPURLSessionManager newURLSessionItemWithRequest:identifier:networkDelegate:completionHandler:]_block_invoke.24
- ___PingPongClientLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke.cold.1
- ___getPPCRedirectClass_block_invoke
- ___getPPCRedirectClass_block_invoke.cold.1
- ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
- ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringPingPongClient
- _dlerror
- _dlsym
- _getPPCExtensibleSSOAuthenticatorClass.softClass
- _getPPCRedirectClass.softClass
- _getkExtensibleSSOTokenKeySymbolLoc.ptr
- _getkExtensibleSSOUsernameKeySymbolLoc.ptr
- _objc_getClass
- _objc_msgSend$customHeaderFields
- _objc_msgSend$hostMappings
- _objc_msgSend$mappedURL:
- _objc_msgSend$setEnvIdentifier:
- _objc_msgSend$setInteractivity:
- _objc_msgSend$setSsoAuthenticator:
- _objc_msgSend$setUrlRedirector:
- _objc_msgSend$ssoAuthenticator
- _objc_msgSend$syncQueue
- _objc_msgSend$urlRedirector
CStrings:
- "%s"
- "@\"PPCExtensibleSSOAuthenticator\""
- "@\"PPCRedirect\""
- "PPCExtensibleSSOAuthenticator"
- "PPCRedirect"
- "T@\"PPCExtensibleSSOAuthenticator\",&,N,V_ssoAuthenticator"
- "T@\"PPCRedirect\",&,N,V_urlRedirector"
- "Unable to find class %s"
- "_ssoAuthenticator"
- "_urlRedirector"
- "hostMappings"
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
