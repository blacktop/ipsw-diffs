## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0x10eb60
-  __TEXT.__objc_methlist: 0x7f1c
+625.2.4.1.0
+  __TEXT.__text: 0x10f4a4
+  __TEXT.__objc_methlist: 0x7f64
   __TEXT.__const: 0x12784
-  __TEXT.__cstring: 0xb128
+  __TEXT.__cstring: 0xb168
   __TEXT.__ustring: 0x65ac
-  __TEXT.__oslogstring: 0x3378
-  __TEXT.__gcc_except_tab: 0x1158
+  __TEXT.__oslogstring: 0x33e8
+  __TEXT.__gcc_except_tab: 0x11a4
   __TEXT.__dlopen_cstrs: 0x25e
   __TEXT.__swift5_typeref: 0x2ab0
   __TEXT.__constg_swiftt: 0x1eb4

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_capture: 0xb54
   __TEXT.__swift5_mpenum: 0x90
-  __TEXT.__unwind_info: 0x6360
+  __TEXT.__unwind_info: 0x6390
   __TEXT.__eh_frame: 0x5570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b90
+  __DATA_CONST.__objc_selrefs: 0x4bc8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __DATA_CONST.__got: 0xea8
-  __AUTH_CONST.__const: 0x9cc0
+  __DATA_CONST.__got: 0xeb0
+  __AUTH_CONST.__const: 0x9d20
   __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0xf8b8
+  __AUTH_CONST.__objc_const: 0xf918
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1358
   __AUTH.__objc_data: 0x30b0
   __AUTH.__data: 0x13c0
-  __DATA.__objc_ivar: 0x790
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x3368
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x9c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7457
-  Symbols:   8330
-  CStrings:  1348
+  Functions: 7469
+  Symbols:   8356
+  CStrings:  1351
 
Symbols:
+ -[ASPasskeyCredentialIdentity _initWithFoundationCredentialIdentity:]
+ -[_ASWebAuthenticationSessionRequestServer _completeRequest:withCallbackURL:error:]
+ -[_ASWebsiteNameProvider _updateFetchingSuspended:]
+ -[_ASWebsiteNameProvider resumeFetching]
+ -[_ASWebsiteNameProvider suspendFetching]
+ GCC_except_table15
+ GCC_except_table40
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table94
+ OBJC_IVAR_$__ASAgentCredentialExchangeListener._extensionManager
+ OBJC_IVAR_$__ASWebsiteNameFetchOperation._request
+ OBJC_IVAR_$__ASWebsiteNameProvider._fetchingSuspended
+ _OBJC_CLASS_$_NSThread
+ __105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke_2
+ __71-[_ASWebsiteNameProvider fetchOperation:finishedWithResult:completion:]_block_invoke
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke_2
+ ___38-[_ASWebsiteNameFetchOperation cancel]_block_invoke
+ ___51-[_ASWebsiteNameProvider _updateFetchingSuspended:]_block_invoke
+ ___61-[_ASWebAuthenticationSessionRequestServer _dispatchRequest:]_block_invoke_2
+ ___block_descriptor_32_e54_"<ASCredentialIdentity>"16?0"SFCredentialIdentity"8l
+ ___block_descriptor_41_ea8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e34_"NSExtension"16?0"NSExtension"8l
+ _objc_msgSend$_completeRequest:withCallbackURL:error:
+ _objc_msgSend$_initWithFoundationCredentialIdentity:
+ _objc_msgSend$_updateFetchingSuspended:
+ _objc_msgSend$allObjects
+ _objc_msgSend$initWithFoundationCredentialIdentity:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$sf_extensionAppID
- GCC_except_table27
- GCC_except_table36
- GCC_except_table53
- GCC_except_table61
- GCC_except_table63
- GCC_except_table64
- GCC_except_table72
- GCC_except_table73
- GCC_except_table74
- GCC_except_table80
- GCC_except_table88
- GCC_except_table89
- GCC_except_table90
- ___71-[_ASWebsiteNameProvider fetchOperation:finishedWithResult:completion:]_block_invoke_2
- ___block_descriptor_32_e34_"NSExtension"16?0"NSExtension"8l
CStrings:
+ "@\"<ASCredentialIdentity>\"16@?0@\"SFCredentialIdentity\"8"
+ "B"
+ "Ignoring credential identity with unexpected type: %ld"
+ "Not persisting cancelled fetch for %{sensitive}@"
- "A"
```
