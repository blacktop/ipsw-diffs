## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0x1385f0
-  __TEXT.__objc_methlist: 0x8064
-  __TEXT.__cstring: 0xb558
+625.2.4.1.0
+  __TEXT.__text: 0x138dbc
+  __TEXT.__objc_methlist: 0x809c
+  __TEXT.__cstring: 0xb5a8
   __TEXT.__const: 0x13ef4
-  __TEXT.__gcc_except_tab: 0x11d4
-  __TEXT.__oslogstring: 0x356b
+  __TEXT.__gcc_except_tab: 0x1220
+  __TEXT.__oslogstring: 0x357b
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d36
   __TEXT.__swift5_typeref: 0x324e

   __TEXT.__swift_as_ret: 0x2d4
   __TEXT.__swift_as_cont: 0x508
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__unwind_info: 0x7050
+  __TEXT.__unwind_info: 0x7088
   __TEXT.__eh_frame: 0x6e14
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19c8
+  __DATA_CONST.__const: 0x1a40
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4cb8
+  __DATA_CONST.__objc_selrefs: 0x4d00
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1090
+  __DATA_CONST.__got: 0x1098
   __AUTH_CONST.__const: 0x9a98
   __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x10150
+  __AUTH_CONST.__objc_const: 0x10190
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x1680
   __AUTH.__objc_data: 0x3a28
   __AUTH.__data: 0x18c0
-  __DATA.__objc_ivar: 0x700
+  __DATA.__objc_ivar: 0x708
   __DATA.__data: 0x38a0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x510

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8182
-  Symbols:   8450
-  CStrings:  1352
+  Functions: 8193
+  Symbols:   8475
+  CStrings:  1355
 
Symbols:
+ -[ASPasskeyCredentialIdentity _initWithFoundationCredentialIdentity:]
+ -[_ASWebsiteNameProvider _updateFetchingSuspended:]
+ -[_ASWebsiteNameProvider resumeFetching]
+ -[_ASWebsiteNameProvider suspendFetching]
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table33
+ GCC_except_table46
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$__ASAgentCredentialExchangeListener._extensionManager
+ _OBJC_IVAR_$__ASWebsiteNameFetchOperation._request
+ _OBJC_IVAR_$__ASWebsiteNameProvider._fetchingSuspended
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke
+ ___105-[ASCredentialIdentityStore getCredentialIdentitiesForService:credentialIdentityTypes:completionHandler:]_block_invoke_2
+ ___38-[_ASWebsiteNameFetchOperation cancel]_block_invoke
+ ___51-[_ASWebsiteNameProvider _updateFetchingSuspended:]_block_invoke
+ ___block_descriptor_32_e54_"<ASCredentialIdentity>"16?0"SFCredentialIdentity"8l
+ ___block_descriptor_40_e8_32s_e23_B32?0"NSUUID"816^B24ls32l8
+ ___block_descriptor_41_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e34_"NSExtension"16?0"NSExtension"8ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
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
- GCC_except_table15
- GCC_except_table22
- GCC_except_table23
- GCC_except_table48
- GCC_except_table49
- GCC_except_table50
- GCC_except_table51
- GCC_except_table56
- GCC_except_table66
- GCC_except_table70
- GCC_except_table71
- GCC_except_table72
- _OBJC_IVAR_$__ASPasswordManagerIconController._fetchingSuspended
- ___71-[_ASWebsiteNameProvider fetchOperation:finishedWithResult:completion:]_block_invoke_2
- ___block_descriptor_32_e34_"NSExtension"16?0"NSExtension"8l
- ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
CStrings:
+ "@\"<ASCredentialIdentity>\"16@?0@\"SFCredentialIdentity\"8"
+ "B32@?0@\"NSUUID\"8@16^B24"
+ "Ignoring credential identity with unexpected type: %ld"
+ "Not persisting cancelled fetch for %{sensitive}@"
+ "\xf0!"
- "Skipping touch icon fetch while suspended; domain=%{sensitive, mask.hash}@"
- "\xf01"
```
