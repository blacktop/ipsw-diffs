## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

### Sections with Same Size but Changed Content

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
- `__AUTH_CONST.__const`
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
-  __TEXT.__text: 0xa8dcc
-  __TEXT.__auth_stubs: 0x1ed0
-  __TEXT.__objc_methlist: 0x8420
-  __TEXT.__const: 0x20b4
-  __TEXT.__cstring: 0x4a13
-  __TEXT.__oslogstring: 0x1222
-  __TEXT.__gcc_except_tab: 0xfd8
+  __TEXT.__text: 0xa9c94
+  __TEXT.__auth_stubs: 0x1f20
+  __TEXT.__objc_methlist: 0x8450
+  __TEXT.__const: 0x20c4
+  __TEXT.__cstring: 0x4ad3
+  __TEXT.__oslogstring: 0x1269
+  __TEXT.__gcc_except_tab: 0x103c
   __TEXT.__ustring: 0x118
+  __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x1380
   __TEXT.__swift5_typeref: 0xe2c
   __TEXT.__swift5_reflstr: 0xd42

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x33a0
+  __TEXT.__unwind_info: 0x33e0
   __TEXT.__eh_frame: 0x1568
   __TEXT.__objc_classname: 0x13d7
-  __TEXT.__objc_methname: 0xfce6
-  __TEXT.__objc_methtype: 0x1d35
-  __TEXT.__objc_stubs: 0xa260
+  __TEXT.__objc_methname: 0xfe16
+  __TEXT.__objc_methtype: 0x1d65
+  __TEXT.__objc_stubs: 0xa3c0
   __DATA_CONST.__got: 0x918
-  __DATA_CONST.__const: 0x2140
+  __DATA_CONST.__const: 0x21c0
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ac0
+  __DATA_CONST.__objc_selrefs: 0x3b10
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__auth_got: 0xfa0
   __AUTH_CONST.__const: 0x3240
-  __AUTH_CONST.__cfstring: 0x5320
-  __AUTH_CONST.__objc_const: 0xde68
+  __AUTH_CONST.__cfstring: 0x5360
+  __AUTH_CONST.__objc_const: 0xdec8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x15a0
   __AUTH.__data: 0xbb8
-  __DATA.__objc_ivar: 0x7b4
+  __DATA.__objc_ivar: 0x7bc
   __DATA.__data: 0x1080
-  __DATA.__bss: 0x1bb0
+  __DATA.__bss: 0x1bc0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2750
   __DATA_DIRTY.__data: 0x678
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
-  Functions: 4873
-  Symbols:   6868
-  CStrings:  4058
+  Functions: 4891
+  Symbols:   6907
+  CStrings:  4085
 
Symbols:
+ -[TPSURLSessionACAuthHandler setSsoAuthenticator:]
+ -[TPSURLSessionACAuthHandler ssoAuthenticator]
+ -[TPSURLSessionManager setUrlRedirector:]
+ -[TPSURLSessionManager urlRedirector]
+ _OBJC_IVAR_$_TPSURLSessionACAuthHandler._ssoAuthenticator
+ _OBJC_IVAR_$_TPSURLSessionManager._urlRedirector
+ _PingPongClientLibrary
+ _PingPongClientLibraryCore
+ _PingPongClientLibraryCore.frameworkLibrary
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke
+ ___60-[TPSURLSessionACAuthHandler _authenticateWithAppleConnect:]_block_invoke_2
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
