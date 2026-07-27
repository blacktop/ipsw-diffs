## HelpData

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 239.5.1.0.0
-  __TEXT.__text: 0x1e058
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x2014
-  __TEXT.__cstring: 0x3368
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x33c
+  __TEXT.__text: 0x1f348
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x202c
+  __TEXT.__cstring: 0x35d0
+  __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__oslogstring: 0x250
-  __TEXT.__unwind_info: 0x730
-  __TEXT.__objc_classname: 0x32a
-  __TEXT.__objc_methname: 0x5693
-  __TEXT.__objc_methtype: 0xc0e
-  __TEXT.__objc_stubs: 0x4a40
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__objc_classname: 0x32b
+  __TEXT.__objc_methname: 0x576d
+  __TEXT.__objc_methtype: 0xc1d
+  __TEXT.__objc_stubs: 0x4b80
   __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1780
+  __DATA_CONST.__objc_selrefs: 0x17b8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0x690
-  __AUTH_CONST.__cfstring: 0x34a0
-  __AUTH_CONST.__objc_const: 0x4680
+  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__cfstring: 0x35c0
+  __AUTH_CONST.__objc_const: 0x46b0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x708
-  __DATA.__objc_ivar: 0x298
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x480
   __DATA.__ddm_mapping: 0x5fa
   __DATA.__ddm_config: 0x164c
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x2a8
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 736
-  Symbols:   2214
-  CStrings:  1690
+  Functions: 763
+  Symbols:   2264
+  CStrings:  1723
 
Symbols:
+ -[DDMContext setUrlRedirector:]
+ -[DDMContext urlRedirector]
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table7
+ OBJC_IVAR_$_DDMContext._urlRedirector
+ PingPongClientLibrary
+ PingPongClientLibraryCore.frameworkLibrary
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ __61-[HPDAuthChallengeHandler authenticateWithCompletionHandler:]_block_invoke
+ ___61-[HPDAuthChallengeHandler authenticateWithCompletionHandler:]_block_invoke
+ ___PingPongClientLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r
+ ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ ___getPPCRedirectClass_block_invoke
+ ___getkExtensibleOIDCTokenKeySymbolLoc_block_invoke
+ ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
+ ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
+ __getPPCExtensibleSSOAuthenticatorClass_block_invoke
+ __getPPCRedirectClass_block_invoke
+ __sl_dlopen
+ _audit_stringPingPongClient
+ _dlerror
+ _dlsym
+ _getkExtensibleOIDCTokenKeySymbolLoc
+ _getkExtensibleSSOTokenKeySymbolLoc
+ _getkExtensibleSSOUsernameKeySymbolLoc
+ _objc_autorelease
+ _objc_getClass
+ _objc_msgSend$authenticateWithCompletion:
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$resultWithValues:error:
+ _objc_msgSend$setAppIdentifier:
+ _objc_msgSend$setEnvIdentifier:
+ _objc_msgSend$setInteractivity:
+ _objc_msgSend$setSsoAuthenticator:
+ _objc_msgSend$setUrlRedirector:
+ _objc_msgSend$ssoAuthenticator
+ _objc_msgSend$syncQueue
+ getPPCExtensibleSSOAuthenticatorClass.softClass
+ getPPCRedirectClass.softClass
+ getkExtensibleOIDCTokenKeySymbolLoc.ptr
+ getkExtensibleSSOTokenKeySymbolLoc.ptr
+ getkExtensibleSSOUsernameKeySymbolLoc.ptr
CStrings:
+ "%@ %@"
+ "%s"
+ "/System/Library/PrivateFrameworks/PingPongClient.framework/Contents/MacOS/PingPongClient"
+ "0"
+ "170617"
+ "@\"PPCRedirect\""
+ "APPLECONNECT.APPLE.COM"
+ "Authorization"
+ "Bearer"
+ "Class getPPCExtensibleSSOAuthenticatorClass(void)_block_invoke"
+ "Class getPPCRedirectClass(void)_block_invoke"
+ "NSString *getkExtensibleOIDCTokenKey(void)"
+ "NSString *getkExtensibleSSOTokenKey(void)"
+ "NSString *getkExtensibleSSOUsernameKey(void)"
+ "PPCExtensibleSSOAuthenticator"
+ "PPCRedirect"
+ "PPClientSoftLink.h"
+ "T@\"PPCRedirect\",&,N,V_urlRedirector"
+ "Unable to find class %s"
+ "_urlRedirector"
+ "authenticateWithCompletion:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "kExtensibleOIDCTokenKey"
+ "kExtensibleSSOTokenKey"
+ "kExtensibleSSOUsernameKey"
+ "setAppIdentifier:"
+ "setEnvIdentifier:"
+ "setInteractivity:"
+ "setUrlRedirector:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
+ "urlRedirector"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "void *PingPongClientLibrary(void)"
```
