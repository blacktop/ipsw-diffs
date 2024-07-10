## AuthenticationServices

> `/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-619.1.20.11.1
-  __TEXT.__text: 0x38e80
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x3a50
+619.1.18.11.1
+  __TEXT.__text: 0x38e68
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x3a6c
   __TEXT.__const: 0xd44
-  __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__cstring: 0x32c6
+  __TEXT.__gcc_except_tab: 0xbf8
+  __TEXT.__cstring: 0x32b6
   __TEXT.__oslogstring: 0x1044
   __TEXT.__dlopen_cstrs: 0x1a1
   __TEXT.__ustring: 0x1d96

   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1570
+  __TEXT.__unwind_info: 0x1588
   __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x125a
-  __TEXT.__objc_methname: 0xac8a
-  __TEXT.__objc_methtype: 0x1b6b
-  __TEXT.__objc_stubs: 0x5bc0
+  __TEXT.__objc_methname: 0xacd0
+  __TEXT.__objc_methtype: 0x1c8b
+  __TEXT.__objc_stubs: 0x5ba0
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0xfc8
+  __DATA_CONST.__const: 0xfa0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2068
+  __DATA_CONST.__objc_selrefs: 0x2078
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x150
-  __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH_CONST.__auth_ptr: 0x248
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__auth_ptr: 0x238
   __AUTH_CONST.__const: 0xce8
   __AUTH_CONST.__cfstring: 0x25e0
-  __AUTH_CONST.__objc_const: 0x9bf0
+  __AUTH_CONST.__objc_const: 0x9c50
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x1390
   __AUTH.__data: 0x558
-  __DATA.__objc_ivar: 0x500
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0x1018
   __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x870

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1863
-  Symbols:   4006
+  Functions: 1866
+  Symbols:   4014
   CStrings:  410
 
Symbols:
+ +[ASSettingsHelper requestCredentialProviderExtensionEnablementWithCompletionHandler:]
+ -[_ASWebsiteNameProvider .cxx_construct]
+ -[_ASWebsiteNameProvider disableSuddenTerminationForAccountStoreLoad]
+ -[_ASWebsiteNameProvider enableSuddenTerminationForAccountStoreLoad]
+ GCC_except_table50
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table65
+ GCC_except_table74
+ OBJC_IVAR_$__ASWebsiteNameProvider._suddenTerminationDisabler
+ __44-[ASAuthorizationController _failWithError:]_block_invoke.125
+ __56-[ASAuthorizationController _completeWithAuthorization:]_block_invoke.121
+ __ZN12SafariShared25SuddenTerminationDisabler23enableSuddenTerminationEv
+ __ZN12SafariShared25SuddenTerminationDisablerC1EP8NSString
+ __ZN12SafariShared25SuddenTerminationDisablerD2Ev
+ __ZNSt3__110unique_ptrIN12SafariShared25SuddenTerminationDisablerENS_14default_deleteIS2_EEE5resetB8sn180100EPS2_
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___86+[ASSettingsHelper requestCredentialProviderExtensionEnablementWithCompletionHandler:]_block_invoke
+ __block_literal_global.280
+ _objc_msgSend$requestCredentialProviderExtensionEnablementWithCompletionHandler:
- +[ASSettingsHelper requestToTurnOnCredentialProviderExtensionWithCompletionHandler:]
- +[_ASAccountManagerTipManager _checkEligibilityForImportPasswordsTipWithCompletionHandler:]
- GCC_except_table52
- GCC_except_table53
- GCC_except_table57
- __44-[ASAuthorizationController _failWithError:]_block_invoke.128
- __56-[ASAuthorizationController _completeWithAuthorization:]_block_invoke.124
- ___46+[_ASAccountManagerTipManager fetchTipToShow:]_block_invoke_2
- ___84+[ASSettingsHelper requestToTurnOnCredentialProviderExtensionWithCompletionHandler:]_block_invoke
- ___block_descriptor_48_e8_32bs_e8_v12?0B8ls32l8
- __block_literal_global.272
- _objc_msgSend$_checkEligibilityForImportPasswordsTipWithCompletionHandler:
- _objc_msgSend$requestToTurnOnCredentialProviderExtensionWithCompletionHandler:
CStrings:
+ "com.apple.AuthenticationServices.ASWebsiteNameProvider"
- "All Public Key Credential requests must specify a relyingPartyIdentifier."

```
