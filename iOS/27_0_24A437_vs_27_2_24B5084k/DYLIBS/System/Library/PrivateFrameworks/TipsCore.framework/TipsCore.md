## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-866.0.0.0.0
-  __TEXT.__text: 0xaef14
-  __TEXT.__objc_methlist: 0x8bf0
+866.2.2.0.0
+  __TEXT.__text: 0xae42c
+  __TEXT.__objc_methlist: 0x8c08
   __TEXT.__const: 0x2b44
-  __TEXT.__cstring: 0x5103
-  __TEXT.__oslogstring: 0x1465
-  __TEXT.__gcc_except_tab: 0x1040
+  __TEXT.__cstring: 0x50a3
+  __TEXT.__oslogstring: 0x141e
+  __TEXT.__gcc_except_tab: 0xfdc
   __TEXT.__ustring: 0x118
-  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x18fc
   __TEXT.__swift5_typeref: 0x100a
   __TEXT.__swift5_reflstr: 0x12a2

   __TEXT.__swift_as_cont: 0x108
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4200
+  __TEXT.__unwind_info: 0x41c0
   __TEXT.__eh_frame: 0x1910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x23c0
+  __DATA_CONST.__const: 0x2350
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d90
+  __DATA_CONST.__objc_selrefs: 0x3d70
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x978
-  __AUTH_CONST.__const: 0x4050
-  __AUTH_CONST.__cfstring: 0x54a0
-  __AUTH_CONST.__objc_const: 0xe920
+  __AUTH_CONST.__const: 0x40b0
+  __AUTH_CONST.__cfstring: 0x55a0
+  __AUTH_CONST.__objc_const: 0xe8d0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x11e8
+  __AUTH_CONST.__auth_got: 0x11c8
   __AUTH.__objc_data: 0x710
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x7d4
+  __DATA.__objc_ivar: 0x7cc
   __DATA.__data: 0x12e0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x43f8
   __DATA_DIRTY.__data: 0x11c8
-  __DATA_DIRTY.__bss: 0x4a0
+  __DATA_DIRTY.__bss: 0x488
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
   - /System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5442
-  Symbols:   7185
-  CStrings:  1139
+  Functions: 5428
+  Symbols:   7160
+  CStrings:  1137
 
Symbols:
+ +[NSLocale(TPSCoreAdditions) tps_systemLanguages]
+ +[TPSCommonDefines isTVUI]
+ +[TPSContentURLController normalizeVirtualMachineModelIfNeeded:]
+ GCC_except_table75
+ GCC_except_table82
+ _TPSCommonDefinesCollectionNameHardware
+ _TPSCommonDefinesCollectionOverrideMajorVersion
+ _objc_msgSend$isMacUI
+ _objc_msgSend$isTVUI
+ _objc_msgSend$isVisionUI
+ _objc_msgSend$isWatchUI
+ _objc_msgSend$normalizeVirtualMachineModelIfNeeded:
+ _objc_msgSend$tps_systemLanguages
+ _objc_msgSend$userGuideLanguagesWithPreferredLanguages:systemLanguages:
+ _objc_msgSend$userGuideSystemLanguages
+ _swift_getObjCClassFromMetadata
- -[TPSURLSessionACAuthHandler setSsoAuthenticator:]
- -[TPSURLSessionACAuthHandler ssoAuthenticator]
- -[TPSURLSessionManager setUrlRedirector:]
- -[TPSURLSessionManager urlRedirector]
- GCC_except_table59
- GCC_except_table74
- _OBJC_IVAR_$_TPSURLSessionACAuthHandler._ssoAuthenticator
- _OBJC_IVAR_$_TPSURLSessionManager._urlRedirector
- _PingPongClientLibrary
- _PingPongClientLibraryCore
- _PingPongClientLibraryCore.frameworkLibrary
- ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
- ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke_2
- ___PingPongClientLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___getPPCExtensibleSSOAuthenticatorClass_block_invoke
- ___getPPCRedirectClass_block_invoke
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
CStrings:
+ "27"
+ "A2117"
+ "A2737"
+ "A3256"
+ "A3281"
+ "A3357"
+ "AppleTV"
+ "IsVirtualDevice"
+ "ec5be57655e13fa5afb54167ccf91580f8bd99dc"
+ "hardware"
- "Mapped URL Request: %@"
- "PPCExtensibleSSOAuthenticator"
- "PPCRedirect"
- "PPCRedirect initialized."
- "PPCRedirect not found."
- "Unable to find class %s"
- "X-AppleConnect-Token"
- "X-AppleConnect-User"
- "kExtensibleSSOTokenKey"
- "kExtensibleSSOUsernameKey"
- "softlink:o:path:/System/Library/PrivateFrameworks/PingPongClient.framework/PingPongClient"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
```
