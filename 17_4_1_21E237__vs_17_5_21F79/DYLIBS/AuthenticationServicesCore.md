## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x8b74c
+618.2.12.10.9
+  __TEXT.__text: 0x8bed4
   __TEXT.__auth_stubs: 0x2030
-  __TEXT.__objc_methlist: 0x21a4
+  __TEXT.__objc_methlist: 0x21ec
   __TEXT.__const: 0x4cb8
-  __TEXT.__cstring: 0x4eb2
-  __TEXT.__oslogstring: 0x1a85
+  __TEXT.__cstring: 0x4ed2
+  __TEXT.__oslogstring: 0x1a98
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__ustring: 0x45c
   __TEXT.__constg_swiftt: 0x120c
   __TEXT.__swift5_typeref: 0x1488
   __TEXT.__swift5_reflstr: 0xd84
-  __TEXT.__swift5_fieldmd: 0x12d4
+  __TEXT.__swift5_fieldmd: 0x12ec
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x2d0
   __TEXT.__swift5_proto: 0x4d8

   __TEXT.__swift5_capture: 0x27c
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2a78
+  __TEXT.__unwind_info: 0x2a8c
   __TEXT.__eh_frame: 0x25f0
   __TEXT.__objc_classname: 0x709
-  __TEXT.__objc_methname: 0x84d2
-  __TEXT.__objc_methtype: 0x1ff7
-  __TEXT.__objc_stubs: 0x3880
+  __TEXT.__objc_methname: 0x86c4
+  __TEXT.__objc_methtype: 0x201d
+  __TEXT.__objc_stubs: 0x38e0
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x748
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5b98
-  __DATA_CONST.__objc_selrefs: 0x14d0
+  __DATA_CONST.__objc_const: 0x5c18
+  __DATA_CONST.__objc_selrefs: 0x1500
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_classrefs: 0x3b0
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__const: 0x1c68
+  __AUTH_CONST.__const: 0x1c48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0xa0
   __AUTH_CONST.__auth_got: 0x1028
   __AUTH.__objc_data: 0x158
   __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x374
+  __DATA.__objc_ivar: 0x380
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x26d8
+  __DATA.__data: 0x26b8
   __DATA.__bss: 0x9850
   __DATA.__common: 0x1e8
-  __DATA_DIRTY.__const: 0x2158
+  __DATA_DIRTY.__const: 0x2198
   __DATA_DIRTY.__objc_const: 0xff8
   __DATA_DIRTY.__objc_data: 0x1520
-  __DATA_DIRTY.__data: 0xb88
+  __DATA_DIRTY.__data: 0xb98
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3575
-  Symbols:   4060
-  CStrings:  2044
+  Functions: 3583
+  Symbols:   4083
+  CStrings:  2057
 
Symbols:
+ -[ASCAgent test_addCredentialProviderExtensionLoginChoiceWithName:extensionBundleID:containingAppBundleID:]
+ -[ASCAgent test_clearCredentialProviderExtensionLoginChoices]
+ -[ASCPublicKeyCredentialAssertionOptions _initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:appIDForSecurityKeys:]
+ -[ASCPublicKeyCredentialAssertionOptions appIDForSecurityKeys]
+ -[ASCPublicKeyCredentialAssertionOptions setAppIDForSecurityKeys:]
+ -[ASCSecurityKeyPublicKeyCredentialAssertion appID]
+ -[ASCSecurityKeyPublicKeyCredentialAssertion initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:]
+ -[ASCSecurityKeyPublicKeyCredentialAssertion setAppID:]
+ GCC_except_table131
+ GCC_except_table134
+ _OBJC_IVAR_$_ASCAgent._test_credentialProviderExtensionLoginChoices
+ _OBJC_IVAR_$_ASCPublicKeyCredentialAssertionOptions._appIDForSecurityKeys
+ _OBJC_IVAR_$_ASCSecurityKeyPublicKeyCredentialAssertion._appID
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.105
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.108
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.297
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.300
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.303
+ ___55-[ASCAgent _allAvailableLoginChoicesForRequestContext:]_block_invoke
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.325
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.102
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.102.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.95
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.95.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.98
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.98.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.56.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.57
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.61
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.64
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.65
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.65.cold.1
+ ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.236
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.69
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.77
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.77.cold.1
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.70
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.309
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.309.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.310
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.313.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.314
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.315
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.319
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.319.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.316
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.316.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.242
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.242.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.248
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.251
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.251.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.255
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.255.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.261
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.261.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.265
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.274
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.277
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.277.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.286
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.286.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.117
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.117.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.124
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.127
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.127.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.130
+ ___block_literal_global.100
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.113
+ ___block_literal_global.119
+ ___block_literal_global.126
+ ___block_literal_global.129
+ ___block_literal_global.199
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.241
+ ___block_literal_global.244
+ ___block_literal_global.250
+ ___block_literal_global.257
+ ___block_literal_global.267
+ ___block_literal_global.270
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.291
+ ___block_literal_global.296
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.307
+ ___block_literal_global.312
+ ___block_literal_global.318
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.333
+ ___block_literal_global.547
+ ___block_literal_global.59
+ ___block_literal_global.63
+ ___block_literal_global.75
+ ___block_literal_global.79
+ ___block_literal_global.97
+ ___swift_memcpy178_8
+ ___swift_memcpy42_8
+ ___swift_memcpy90_8
+ _objc_msgSend$_initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:appIDForSecurityKeys:
+ _objc_msgSend$appIDForSecurityKeys
+ _objc_msgSend$initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:
+ _objc_msgSend$removeAllObjects
- -[ASCPublicKeyCredentialAssertionOptions _initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:]
- -[ASCSecurityKeyPublicKeyCredentialAssertion initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:]
- GCC_except_table130
- GCC_except_table133
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.104
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.107
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.295
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.298
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.301
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.323
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.101
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.101.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.97
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.97.cold.1
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.55
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.55.cold.1
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.60
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.63
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.64
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.64.cold.1
- ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.234
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.68
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.76
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.76.cold.1
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.69
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.307
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.307.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.308
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.311
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.311.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.312
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.317
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.317.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.314
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.314.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.240
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.240.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.246
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.249
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.249.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.253
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.253.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.263
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.266
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.266.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.272
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.275
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.275.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.284
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.284.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.116
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.116.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.123
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.126
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.126.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.129
- ___block_literal_global.103
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.118
- ___block_literal_global.125
- ___block_literal_global.128
- ___block_literal_global.216
- ___block_literal_global.219
- ___block_literal_global.237
- ___block_literal_global.242
- ___block_literal_global.248
- ___block_literal_global.255
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.274
- ___block_literal_global.277
- ___block_literal_global.289
- ___block_literal_global.292
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.303
- ___block_literal_global.310
- ___block_literal_global.316
- ___block_literal_global.321
- ___block_literal_global.325
- ___block_literal_global.331
- ___block_literal_global.541
- ___block_literal_global.58
- ___block_literal_global.62
- ___block_literal_global.74
- ___block_literal_global.78
- ___block_literal_global.96
- ___block_literal_global.99
- ___swift_memcpy177_8
- ___swift_memcpy89_8
- _objc_msgSend$_initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:
CStrings:
+ "\x02\x15\x1d\x13"
+ "\tRP: %{private, mask.hash}@\n\tuv: %{public}@\n\tallowedCredentialsCount: %{public}lu\n\ttransports: %{public}@\n\tappID: %{public}@\n"
+ "+"
+ "@84@0:8@16@24@32@40@48@56@64@72B80"
+ "@84@0:8Q16@24@32@40@48@56@64B72@76"
+ "T@\"NSString\",C,N,V_appIDForSecurityKeys"
+ "TB,N,V_appID"
+ "_appIDForSecurityKeys"
+ "_initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:appIDForSecurityKeys:"
+ "_test_credentialProviderExtensionLoginChoices"
+ "appIDForSecurityKeys"
+ "appid"
+ "initWithRelyingPartyIdentifier:authenticatorData:signature:userHandle:rawClientDataJSON:credentialID:extensionOutputsCBOR:attachment:appID:"
+ "removeAllObjects"
+ "setAppIDForSecurityKeys:"
+ "test_addCredentialProviderExtensionLoginChoiceWithName:extensionBundleID:containingAppBundleID:"
+ "test_clearCredentialProviderExtensionLoginChoices"
- "\x02\x15\x1d\x12"
- "\tRP: %{private, mask.hash}@\n\tuv: %{public}@\n\tallowedCredentialsCount: %{public}lu\n\ttransports: %{public}@\n"
- "*"
- "@76@0:8Q16@24@32@40@48@56@64B72"
- "_initWithKind:relyingPartyIdentifier:challenge:clientDataHash:clientDataJSON:userVerificationPreference:allowedCredentials:shouldHideHybrid:"

```
