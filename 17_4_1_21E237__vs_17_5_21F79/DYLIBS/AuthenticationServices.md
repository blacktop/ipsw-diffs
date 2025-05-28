## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x55ea4
+618.2.12.10.9
+  __TEXT.__text: 0x56544
   __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x55b8
+  __TEXT.__objc_methlist: 0x55e8
   __TEXT.__const: 0x7a4
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x4d66
-  __TEXT.__oslogstring: 0x23f8
-  __TEXT.__ustring: 0x7712
+  __TEXT.__gcc_except_tab: 0x34c
+  __TEXT.__cstring: 0x4da6
+  __TEXT.__oslogstring: 0x2417
+  __TEXT.__ustring: 0x78e8
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__constg_swiftt: 0x1e4
   __TEXT.__swift5_typeref: 0x22e

   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1c40
+  __TEXT.__unwind_info: 0x1c58
   __TEXT.__eh_frame: 0x1e0
-  __TEXT.__objc_classname: 0x1d00
-  __TEXT.__objc_methname: 0x14775
-  __TEXT.__objc_methtype: 0x4349
-  __TEXT.__objc_stubs: 0xd7e0
+  __TEXT.__objc_classname: 0x1d03
+  __TEXT.__objc_methname: 0x148ed
+  __TEXT.__objc_methtype: 0x4360
+  __TEXT.__objc_stubs: 0xd8a0
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x15f0
+  __DATA_CONST.__const: 0x1648
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb210
-  __DATA_CONST.__objc_selrefs: 0x40b8
+  __DATA_CONST.__objc_const: 0xb2c0
+  __DATA_CONST.__objc_selrefs: 0x40e8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x848
   __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__objc_const: 0x30e0
-  __AUTH_CONST.__cfstring: 0x4520
-  __AUTH_CONST.__const: 0x1350
+  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__const: 0x1390
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH.__objc_data: 0x2440
+  __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x694
+  __DATA.__objc_ivar: 0x6a4
   __DATA.__data: 0x16c8
   __DATA.__bss: 0x6b0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2518
-  Symbols:   8786
-  CStrings:  4073
+  Functions: 2529
+  Symbols:   8820
+  CStrings:  4093
 
Symbols:
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialAssertion _initWithBaseCredential:userID:signature:rawAuthenticatorData:appID:]
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialAssertion appID]
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest appID]
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest setAppID:]
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialRegistration _initWithBaseCredential:rawAttestationObject:transports:]
+ -[ASAuthorizationSecurityKeyPublicKeyCredentialRegistration transports]
+ -[ASCredentialPickerPaneViewController _isOtherAccountsSection:]
+ -[ASCredentialRequestConfirmButtonSubPane disableBiometricView]
+ GCC_except_table92
+ _OBJC_IVAR_$_ASAuthorizationSecurityKeyPublicKeyCredentialAssertion._appID
+ _OBJC_IVAR_$_ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest._appID
+ _OBJC_IVAR_$_ASAuthorizationSecurityKeyPublicKeyCredentialRegistration._transports
+ _OBJC_IVAR_$_ASCredentialPickerPaneViewController._onlyHasOtherAccountsLoginChoices
+ ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke.343
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.311
+ ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.312
+ ___107-[ASCredentialPickerPaneViewController initWithPresentationContext:shouldExpandOtherLoginChoices:activity:]_block_invoke_3
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.319
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.319.cold.1
+ ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.321
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.105
+ ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.107
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.20
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.26.cold.1
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.27
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.29
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.34
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.37
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.21
+ ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.30
+ ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.391
+ ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.392
+ ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.395
+ ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.421
+ ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.111
+ ___63-[ASCredentialRequestConfirmButtonSubPane disableBiometricView]_block_invoke
+ ___63-[ASCredentialRequestConfirmButtonSubPane disableBiometricView]_block_invoke.cold.1
+ ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.103
+ ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.358
+ ___84-[ASAuthorizationSecurityKeyPublicKeyCredentialRegistration initWithCoreCredential:]_block_invoke
+ ___84-[ASAuthorizationSecurityKeyPublicKeyCredentialRegistration initWithCoreCredential:]_block_invoke.cold.1
+ ___block_descriptor_32_e28_"NSString"16?0"NSNumber"8l
+ ___block_descriptor_48_e8_32s40r_e86_"_WKPublicKeyCredentialRequestOptions"16?0"ASCPublicKeyCredentialAssertionOptions"8lr40l8s32l8
+ ___block_literal_global.101
+ ___block_literal_global.110
+ ___block_literal_global.113
+ ___block_literal_global.154
+ ___block_literal_global.163
+ ___block_literal_global.186
+ ___block_literal_global.218
+ ___block_literal_global.286
+ ___block_literal_global.300
+ ___block_literal_global.307
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.32
+ ___block_literal_global.328
+ ___block_literal_global.335
+ ___block_literal_global.342
+ ___block_literal_global.357
+ ___block_literal_global.36
+ ___block_literal_global.362
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.394
+ ___block_literal_global.41
+ ___block_literal_global.57
+ ___block_literal_global.88
+ ___block_literal_global.92
+ _objc_msgSend$_initWithBaseCredential:rawAttestationObject:transports:
+ _objc_msgSend$_initWithBaseCredential:userID:signature:rawAuthenticatorData:appID:
+ _objc_msgSend$_isOtherAccountsSection:
+ _objc_msgSend$appIDForSecurityKeys
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$disableBiometricView
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:
+ _objc_msgSend$setAppIDForSecurityKeys:
- -[ASAuthorizationSecurityKeyPublicKeyCredentialAssertion _initWithBaseCredential:userID:signature:rawAuthenticatorData:]
- -[ASAuthorizationSecurityKeyPublicKeyCredentialRegistration _initWithBaseCredential:rawAttestationObject:]
- -[ASCredentialRequestConfirmButtonSubPane _disableBiometricView]
- GCC_except_table90
- ___101-[ASCredentialPickerPaneViewController confirmButtonSubPaneDidFailBiometry:allowingPasscodeFallback:]_block_invoke.335
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke.303
- ___104-[ASCredentialPickerPaneViewController _performAuthorizationWithAuthenticatedContext:completionHandler:]_block_invoke_2.304
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.311
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.311.cold.1
- ___120-[ASCredentialPickerPaneViewController credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke.313
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.104
- ___134-[ASPublicKeyCredentialManager _createCredentialOfKind:withOptions:authenticatedLAContext:delegate:webFrameIdentifier:parentActivity:]_block_invoke.106
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.19
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.25
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.25.cold.1
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.28
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.33
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke.36
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.20
- ___151-[ASPublicKeyCredentialManager beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:]_block_invoke_2.29
- ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.368
- ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.375
- ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.387
- ___58-[ASCredentialPickerPaneViewController _dumpConfiguration]_block_invoke.410
- ___61-[ASCredentialPickerPaneViewController _useCABLEButtonTapped]_block_invoke.109
- ___64-[ASCredentialRequestConfirmButtonSubPane _disableBiometricView]_block_invoke
- ___64-[ASCredentialRequestConfirmButtonSubPane _disableBiometricView]_block_invoke.cold.1
- ___67-[ASCredentialPickerPaneViewController _useSecurityKeyButtonTapped]_block_invoke.101
- ___70-[ASCredentialPickerPaneViewController performPasswordAuthentication:]_block_invoke.350
- ___block_descriptor_40_e8_32s_e86_"_WKPublicKeyCredentialRequestOptions"16?0"ASCPublicKeyCredentialAssertionOptions"8ls32l8
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.104
- ___block_literal_global.111
- ___block_literal_global.146
- ___block_literal_global.155
- ___block_literal_global.178
- ___block_literal_global.210
- ___block_literal_global.285
- ___block_literal_global.299
- ___block_literal_global.302
- ___block_literal_global.306
- ___block_literal_global.320
- ___block_literal_global.327
- ___block_literal_global.334
- ___block_literal_global.349
- ___block_literal_global.35
- ___block_literal_global.354
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.367
- ___block_literal_global.386
- ___block_literal_global.54
- ___block_literal_global.83
- ___block_literal_global.87
- ___block_literal_global.91
- ___block_literal_global.97
- _objc_msgSend$_disableBiometricView
- _objc_msgSend$_initWithBaseCredential:rawAttestationObject:
- _objc_msgSend$_initWithBaseCredential:userID:signature:rawAuthenticatorData:
CStrings:
+ "\x01\x13"
+ "\x01\x15"
+ "@\"NSString\"16@?0@\"NSNumber\"8"
+ "@52@0:8@16@24@32@40B48"
+ "Other Accounts"
+ "T@\"NSArray\",R,N,V_transports"
+ "T@\"NSString\",C,N,V_appID"
+ "TB,R,N,V_appID"
+ "Unknown transport: %{public}ld"
+ "_appID"
+ "_initWithBaseCredential:rawAttestationObject:transports:"
+ "_initWithBaseCredential:userID:signature:rawAuthenticatorData:appID:"
+ "_isOtherAccountsSection:"
+ "_onlyHasOtherAccountsLoginChoices"
+ "appIDForSecurityKeys"
+ "decodeBoolForKey:"
+ "disableBiometricView"
+ "encodeBool:forKey:"
+ "hybrid"
+ "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:"
+ "internal"
+ "setAppIDForSecurityKeys:"
+ "smartcard"
- "\x01\x14"
- "_disableBiometricView"
- "_initWithBaseCredential:rawAttestationObject:"
- "_initWithBaseCredential:userID:signature:rawAuthenticatorData:"

```
