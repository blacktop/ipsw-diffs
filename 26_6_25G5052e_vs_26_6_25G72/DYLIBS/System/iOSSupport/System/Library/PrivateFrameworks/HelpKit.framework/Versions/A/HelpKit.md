## HelpKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/HelpKit.framework/Versions/A/HelpKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 198.4.1.0.0
-  __TEXT.__text: 0x29fec
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x33ec
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0xac4
-  __TEXT.__cstring: 0x17f8
+  __TEXT.__text: 0x2b0d4
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x341c
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0xb30
+  __TEXT.__cstring: 0x1891
   __TEXT.__oslogstring: 0x329
+  __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__ustring: 0x60
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__objc_classname: 0x5ab
-  __TEXT.__objc_methname: 0x9655
-  __TEXT.__objc_methtype: 0x1d79
-  __TEXT.__objc_stubs: 0x7200
+  __TEXT.__objc_methname: 0x9755
+  __TEXT.__objc_methtype: 0x1da9
+  __TEXT.__objc_stubs: 0x7340
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0xed0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24f0
+  __DATA_CONST.__objc_selrefs: 0x2530
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x2b00
-  __AUTH_CONST.__objc_const: 0x4ec8
+  __AUTH_CONST.__objc_const: 0x4f28
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x3f4
+  __DATA.__objc_ivar: 0x3fc
   __DATA.__data: 0x858
-  __DATA.__bss: 0x170
+  __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1083
-  Symbols:   3023
-  CStrings:  2288
+  Functions: 1104
+  Symbols:   3064
+  CStrings:  2310
 
Symbols:
+ -[HLPURLSessionACAuthHandler setSsoAuthenticator:]
+ -[HLPURLSessionACAuthHandler ssoAuthenticator]
+ -[HLPURLSessionManager setUrlRedirector:]
+ -[HLPURLSessionManager urlRedirector]
+ OBJC_IVAR_$_HLPURLSessionACAuthHandler._ssoAuthenticator
+ OBJC_IVAR_$_HLPURLSessionManager._urlRedirector
+ PingPongClientLibraryCore.frameworkLibrary
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ __57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2
+ ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke
+ ___57-[HLPURLSessionACAuthHandler authenticateWithCompletion:]_block_invoke_2
+ ___PingPongClientLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ ___getPPCRedirectClass_block_invoke
+ ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
+ ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
+ __getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ __getPPCRedirectClass_block_invoke
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringPingPongClient
+ _dlerror
+ _dlsym
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
+ getPPCExtensibleSSOAuthenticatorClass.softClass
+ getPPCRedirectClass.softClass
+ getkExtensibleSSOTokenKeySymbolLoc.ptr
+ getkExtensibleSSOUsernameKeySymbolLoc.ptr
CStrings:
+ "%s"
+ "@\"PPCExtensibleSSOAuthenticator\""
+ "@\"PPCRedirect\""
+ "PPCExtensibleSSOAuthenticator"
+ "PPCRedirect"
+ "T@\"PPCExtensibleSSOAuthenticator\",&,N,V_ssoAuthenticator"
+ "T@\"PPCRedirect\",&,N,V_urlRedirector"
+ "Unable to find class %s"
+ "_ssoAuthenticator"
+ "_urlRedirector"
+ "hostMappings"
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
```
