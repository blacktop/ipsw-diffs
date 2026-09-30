## HelpData

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData`

```diff

-243.0.0.0.0
-  __TEXT.__text: 0x1ccac
-  __TEXT.__objc_methlist: 0x202c
-  __TEXT.__cstring: 0x35fa
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__dlopen_cstrs: 0xb4
+243.2.1.0.0
+  __TEXT.__text: 0x1c9e4
+  __TEXT.__objc_methlist: 0x206c
+  __TEXT.__cstring: 0x35dc
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__oslogstring: 0x250
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__unwind_info: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x2d8
-  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__const: 0x690
   __AUTH_CONST.__cfstring: 0x35a0
   __AUTH_CONST.__objc_const: 0x46b0
   __AUTH_CONST.__objc_intobj: 0x18

   __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x480
   __DATA.__ddm_mapping: 0x5fa
-  __DATA.__ddm_config: 0x164c
+  __DATA.__ddm_config: 0x1686
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 762
-  Symbols:   2259
-  CStrings:  519
+  Functions: 741
+  Symbols:   2228
+  CStrings:  505
 
Symbols:
+ +[HPDHelpBook _generatedIndexRootForTesting]
+ +[HPDHelpBook _pathIsContainedInRoot:inRoot:]
+ -[DDMConfig _webContentProductNames]
+ -[DDMConfig isWebContentBookID:productName:]
+ -[DDMConfig setWebContentProductNames:]
+ -[DDMConfig webContentProductNames]
+ -[HPDHelpBook _cachedResourceContainmentRoot]
+ GCC_except_table50
+ OBJC_IVAR_$_DDMConfig._webContentProductNames
+ _DDMBookConfigKeyIsWebContent
+ _NSSearchPathForDirectoriesInDomains
+ _objc_msgSend$_cachedResourceContainmentRoot
+ _objc_msgSend$_webContentProductNames
+ _objc_msgSend$isWebContentBookID:productName:
+ _objc_msgSend$setWebContentProductNames:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$webContentProductNames
- -[DDMContext setUrlRedirector:]
- -[DDMContext urlRedirector]
- GCC_except_table43
- GCC_except_table7
- OBJC_IVAR_$_DDMContext._urlRedirector
- PingPongClientLibrary
- PingPongClientLibraryCore.frameworkLibrary
- _PingPongClientLibrary
- _PingPongClientLibraryCore
- __69-[HPDAuthChallengeHandler authenticateForHost:withCompletionHandler:]_block_invoke
- ___69-[HPDAuthChallengeHandler authenticateForHost:withCompletionHandler:]_block_invoke
- ___PingPongClientLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
- ___getPPCRedirectClass_block_invoke
- ___getkExtensibleOIDCTokenKeySymbolLoc_block_invoke
- ___getkExtensibleSSOTokenKeySymbolLoc_block_invoke
- ___getkExtensibleSSOUsernameKeySymbolLoc_block_invoke
- __getPPCExtensibleSSOAuthenticatorClass_block_invoke
- __getPPCRedirectClass_block_invoke
- __sl_dlopen
- _audit_stringPingPongClient
- _dlerror
- _dlsym
- _getkExtensibleOIDCTokenKeySymbolLoc
- _getkExtensibleSSOTokenKeySymbolLoc
- _getkExtensibleSSOUsernameKeySymbolLoc
- _objc_getClass
- _objc_msgSend$authenticateWithCompletion:
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$resultWithValues:error:
- _objc_msgSend$setAppIdentifier:
- _objc_msgSend$setEnvIdentifier:
- _objc_msgSend$setInteractivity:
- _objc_msgSend$setSsoAuthenticator:
- _objc_msgSend$setTargetHost:
- _objc_msgSend$setUrlRedirector:
- _objc_msgSend$ssoAuthenticator
- _objc_msgSend$syncQueue
- getPPCExtensibleSSOAuthenticatorClass.softClass
- getPPCRedirectClass.softClass
- getkExtensibleOIDCTokenKeySymbolLoc.ptr
- getkExtensibleSSOTokenKeySymbolLoc.ptr
- getkExtensibleSSOUsernameKeySymbolLoc.ptr
CStrings:
+ "%@/%@/%@"
+ "Rejecting ExactMatch.plist %@ for book at %@ - resolves outside the help book"
+ "Rejecting Suggestions.plist %@ for book at %@ - resolves outside the help book"
+ "Rejecting access page %@ for book at %@ - resolves outside the help book"
+ "Rejecting cached ExactMatch.plist %@ for book %@ - resolves outside its resource root"
+ "Rejecting cached Suggestions.plist %@ for book %@ - resolves outside its resource root"
+ "Rejecting cached access page %@ for book at %@ - resolves outside the help book"
+ "Rejecting potential access page %@ - resolves outside its help book directory %@"
+ "isWebContent"
- "%@ %@"
- "%s"
- "/System/Library/PrivateFrameworks/PingPongClient.framework/Contents/MacOS/PingPongClient"
- "0"
- "170617"
- "APPLECONNECT.APPLE.COM"
- "Authorization"
- "Bearer"
- "Class getPPCExtensibleSSOAuthenticatorClass(void)_block_invoke"
- "Class getPPCRedirectClass(void)_block_invoke"
- "NSString *getkExtensibleOIDCTokenKey(void)"
- "NSString *getkExtensibleSSOTokenKey(void)"
- "NSString *getkExtensibleSSOUsernameKey(void)"
- "PPCExtensibleSSOAuthenticator"
- "PPCRedirect"
- "PPClientSoftLink.h"
- "Unable to find class %s"
- "kExtensibleOIDCTokenKey"
- "kExtensibleSSOTokenKey"
- "kExtensibleSSOUsernameKey"
- "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "void *PingPongClientLibrary(void)"
```
