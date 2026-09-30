## AuthenticationServices

> `/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0xea128
-  __TEXT.__objc_methlist: 0x53f0
+625.2.4.1.0
+  __TEXT.__text: 0xeaa10
+  __TEXT.__objc_methlist: 0x5438
   __TEXT.__const: 0x12394
-  __TEXT.__gcc_except_tab: 0xf30
-  __TEXT.__cstring: 0x566b
-  __TEXT.__oslogstring: 0x237b
+  __TEXT.__gcc_except_tab: 0xf7c
+  __TEXT.__cstring: 0x56bb
+  __TEXT.__oslogstring: 0x239b
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__ustring: 0x3608
   __TEXT.__swift5_typeref: 0x298a

   __TEXT.__swift_as_ret: 0x228
   __TEXT.__swift_as_cont: 0x404
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x5850
+  __TEXT.__unwind_info: 0x5890
   __TEXT.__eh_frame: 0x5a54
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11d8
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a28
+  __DATA_CONST.__objc_selrefs: 0x2a70
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__got: 0xaf8
   __AUTH_CONST.__const: 0x81c0
   __AUTH_CONST.__cfstring: 0x2c60
-  __AUTH_CONST.__objc_const: 0xb990
+  __AUTH_CONST.__objc_const: 0xb9d0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1358
   __AUTH.__objc_data: 0x2668
   __AUTH.__data: 0x13c0
-  __DATA.__objc_ivar: 0x55c
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x2c80
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x808

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6489
-  Symbols:   5825
-  CStrings:  848
+  Functions: 6502
+  Symbols:   5851
+  CStrings:  852
 
Symbols:
+ -[ASPasskeyCredentialIdentity _initWithFoundationCredentialIdentity:]
+ -[_ASWebAuthenticationSessionRequestServer _completeRequest:withCallbackURL:error:]
+ -[_ASWebsiteNameProvider _updateFetchingSuspended:]
+ -[_ASWebsiteNameProvider resumeFetching]
+ -[_ASWebsiteNameProvider suspendFetching]
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ OBJC_IVAR_$__ASAgentCredentialExchangeListener._extensionManager
+ OBJC_IVAR_$__ASWebsiteNameFetchOperation._request
+ OBJC_IVAR_$__ASWebsiteNameProvider._fetchingSuspended
+ _OBJC_CLASS_$_NSThread
+ __105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke_2
+ __51-[_ASPasswordManagerIconController suspendFetching]_block_invoke
+ __71-[_ASWebsiteNameProvider fetchOperation:finishedWithResult:completion:]_block_invoke
+ __97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_3
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke_2
+ ___38-[_ASWebsiteNameFetchOperation cancel]_block_invoke
+ ___51-[_ASWebsiteNameProvider _updateFetchingSuspended:]_block_invoke
+ ___61-[_ASWebAuthenticationSessionRequestServer _dispatchRequest:]_block_invoke_2
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_3
+ ___block_descriptor_32_e54_"<ASCredentialIdentity>"16?0"SFCredentialIdentity"8l
+ ___block_descriptor_40_e8_32s_e23_B32?0"NSUUID"816^B24ls32l8
+ ___block_descriptor_41_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e34_"NSExtension"16?0"NSExtension"8ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_completeRequest:withCallbackURL:error:
+ _objc_msgSend$_initWithFoundationCredentialIdentity:
+ _objc_msgSend$_updateFetchingSuspended:
+ _objc_msgSend$activeRequestTokens
+ _objc_msgSend$allObjects
+ _objc_msgSend$initWithFoundationCredentialIdentity:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isSuspended
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$sf_extensionAppID
- GCC_except_table10
- GCC_except_table12
- GCC_except_table15
- GCC_except_table22
- GCC_except_table23
- GCC_except_table24
- GCC_except_table38
- GCC_except_table48
- GCC_except_table49
- GCC_except_table50
- GCC_except_table51
- GCC_except_table58
- GCC_except_table70
- GCC_except_table71
- GCC_except_table72
- OBJC_IVAR_$__ASPasswordManagerIconController._fetchingSuspended
- __97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2
- ___71-[_ASWebsiteNameProvider fetchOperation:finishedWithResult:completion:]_block_invoke_2
- ___block_descriptor_32_e34_"NSExtension"16?0"NSExtension"8l
- ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$removeAllObjects
CStrings:
+ "@\"<ASCredentialIdentity>\"16@?0@\"SFCredentialIdentity\"8"
+ "B"
+ "B32@?0@\"NSUUID\"8@16^B24"
+ "Ignoring credential identity with unexpected type: %ld"
+ "Not persisting cancelled fetch for %{sensitive}@"
+ "\xf1"
- "A"
- "Skipping touch icon fetch while suspended; domain=%{sensitive, mask.hash}@"
```
