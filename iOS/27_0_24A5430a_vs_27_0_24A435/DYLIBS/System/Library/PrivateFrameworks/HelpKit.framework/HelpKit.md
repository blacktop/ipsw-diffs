## HelpKit

> `/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`

```diff

 208.0.0.0.0
-  __TEXT.__text: 0x2c244
-  __TEXT.__objc_methlist: 0x383c
+  __TEXT.__text: 0x2d2a0
+  __TEXT.__objc_methlist: 0x386c
   __TEXT.__const: 0x308
-  __TEXT.__gcc_except_tab: 0xb00
-  __TEXT.__cstring: 0x1d1f
+  __TEXT.__gcc_except_tab: 0xb6c
+  __TEXT.__cstring: 0x1dbf
   __TEXT.__oslogstring: 0x336
+  __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x206
   __TEXT.__constg_swiftt: 0x118

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0xbb8
+  __TEXT.__unwind_info: 0xbf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__const: 0xfb0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2788
+  __DATA_CONST.__objc_selrefs: 0x27c8
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__got: 0x570
   __AUTH_CONST.__const: 0x438
   __AUTH_CONST.__cfstring: 0x2e40
-  __AUTH_CONST.__objc_const: 0x5658
+  __AUTH_CONST.__objc_const: 0x56b8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x550
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0xef8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x43c
+  __DATA.__objc_ivar: 0x444
   __DATA.__data: 0x960
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1262
-  Symbols:   3337
-  CStrings:  468
+  Functions: 1283
+  Symbols:   3375
+  CStrings:  476
 
Symbols:
+ -[HLPURLSessionACAuthHandler setSsoAuthenticator:]
+ -[HLPURLSessionACAuthHandler ssoAuthenticator]
+ -[HLPURLSessionManager setUrlRedirector:]
+ -[HLPURLSessionManager urlRedirector]
+ _OBJC_IVAR_$_HLPURLSessionACAuthHandler._ssoAuthenticator
+ _OBJC_IVAR_$_HLPURLSessionManager._urlRedirector
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ _PingPongClientLibraryCore.frameworkLibrary
+ ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke
+ ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2
+ ___PingPongClientLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ ___getPPCRedirectClass_block_invoke
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
+ _objc_msgSend$customHeaderFields
+ _objc_msgSend$hostMappings
+ _objc_msgSend$mappedURL:
+ _objc_msgSend$setEnvIdentifier:
+ _objc_msgSend$setInteractivity:
+ _objc_msgSend$setSsoAuthenticator:
+ _objc_msgSend$setUrlRedirector:
+ _objc_msgSend$ssoAuthenticator
+ _objc_msgSend$syncQueue
+ _objc_msgSend$urlRedirector
CStrings:
+ "%s"
+ "PPCExtensibleSSOAuthenticator"
+ "PPCRedirect"
+ "Unable to find class %s"
+ "kExtensibleSSOTokenKey"
+ "kExtensibleSSOUsernameKey"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
```
