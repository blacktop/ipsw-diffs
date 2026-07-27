## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

 822.6.3.0.0
-  __TEXT.__text: 0xaf930
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0x8498
+  __TEXT.__text: 0xb08b8
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_methlist: 0x84c8
   __TEXT.__const: 0x20c4
-  __TEXT.__cstring: 0x4a83
-  __TEXT.__oslogstring: 0x1222
-  __TEXT.__gcc_except_tab: 0xff0
+  __TEXT.__cstring: 0x4ba3
+  __TEXT.__oslogstring: 0x1269
+  __TEXT.__gcc_except_tab: 0x1054
   __TEXT.__ustring: 0x118
+  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x1380
   __TEXT.__swift5_typeref: 0xe2c
   __TEXT.__swift5_reflstr: 0xd42

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x3430
+  __TEXT.__unwind_info: 0x3470
   __TEXT.__eh_frame: 0x1540
   __TEXT.__objc_classname: 0x13d7
-  __TEXT.__objc_methname: 0xfef6
-  __TEXT.__objc_methtype: 0x1d35
-  __TEXT.__objc_stubs: 0xa260
+  __TEXT.__objc_methname: 0x10056
+  __TEXT.__objc_methtype: 0x1d65
+  __TEXT.__objc_stubs: 0xa3c0
   __DATA_CONST.__got: 0x918
-  __DATA_CONST.__const: 0x1400
+  __DATA_CONST.__const: 0x1430
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b18
+  __DATA_CONST.__objc_selrefs: 0x3b68
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0xea8
-  __AUTH_CONST.__const: 0x4140
-  __AUTH_CONST.__cfstring: 0x5400
-  __AUTH_CONST.__objc_const: 0xdf58
+  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH_CONST.__const: 0x41a0
+  __AUTH_CONST.__cfstring: 0x5440
+  __AUTH_CONST.__objc_const: 0xdfb8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x16c0
   __AUTH.__data: 0xa88
-  __DATA.__objc_ivar: 0x7c8
+  __DATA.__objc_ivar: 0x7d0
   __DATA.__data: 0x10b0
-  __DATA.__bss: 0x1c60
+  __DATA.__bss: 0x1c80
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2630
   __DATA_DIRTY.__data: 0x7a8
-  __DATA_DIRTY.__bss: 0x490
+  __DATA_DIRTY.__bss: 0x4a0
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/Versions/A/NetAppsUtilities
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/Versions/A/PegasusAPI
   - /System/Library/PrivateFrameworks/PegasusKit.framework/Versions/A/PegasusKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4936
-  Symbols:   6937
-  CStrings:  4087
+  Functions: 4954
+  Symbols:   6978
+  CStrings:  4115
 
Symbols:
+ -[TPSURLSessionACAuthHandler setSsoAuthenticator:]
+ -[TPSURLSessionACAuthHandler ssoAuthenticator]
+ -[TPSURLSessionManager setUrlRedirector:]
+ -[TPSURLSessionManager urlRedirector]
+ OBJC_IVAR_$_TPSURLSessionACAuthHandler._ssoAuthenticator
+ OBJC_IVAR_$_TPSURLSessionManager._urlRedirector
+ PingPongClientLibraryCore.frameworkLibrary
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ __60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
+ ___PingPongClientLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16l
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
+ getPPCExtensibleSSOAuthenticatorClass.softClass
+ getPPCRedirectClass.softClass
+ getkExtensibleSSOTokenKeySymbolLoc.ptr
+ getkExtensibleSSOUsernameKeySymbolLoc.ptr
CStrings:
+ "/System/Library/PrivateFrameworks/PingPongClient.framework/Contents/MacOS/PingPongClient"
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
