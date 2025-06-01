## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x83e74
-  __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0x1fd8
-  __TEXT.__cstring: 0x4789
+617.1.17.10.9
+  __TEXT.__text: 0x843dc
+  __TEXT.__auth_stubs: 0x1f10
+  __TEXT.__objc_methlist: 0x2018
+  __TEXT.__cstring: 0x47a9
   __TEXT.__ustring: 0x4bc
-  __TEXT.__oslogstring: 0x1916
+  __TEXT.__oslogstring: 0x1963
   __TEXT.__const: 0x4bc1
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__swift5_typeref: 0x13cd

   __TEXT.__swift5_capture: 0x1e8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x2474
+  __TEXT.__unwind_info: 0x2478
   __TEXT.__eh_frame: 0x2210
-  __TEXT.__objc_classname: 0x6a0
-  __TEXT.__objc_methname: 0x7bfc
-  __TEXT.__objc_methtype: 0x1c24
-  __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x738
+  __TEXT.__objc_classname: 0x6a2
+  __TEXT.__objc_methname: 0x7cd6
+  __TEXT.__objc_methtype: 0x1c6e
+  __TEXT.__objc_stubs: 0x36e0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x708
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5418
-  __DATA_CONST.__objc_selrefs: 0x1408
+  __DATA_CONST.__objc_const: 0x54b8
+  __DATA_CONST.__objc_selrefs: 0x1438
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x1948
+  __AUTH_CONST.__const: 0x19a8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__auth_got: 0xf98
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x378
+  __DATA.__objc_classrefs: 0x380
   __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x364
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x25c8
   __DATA.__bss: 0x9750
   __DATA.__common: 0x1e8
-  __DATA_DIRTY.__const: 0x2248
+  __DATA_DIRTY.__const: 0x21e8
   __DATA_DIRTY.__objc_const: 0xff8
   __DATA_DIRTY.__objc_data: 0x1518
   __DATA_DIRTY.__data: 0xba0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2AB2B661-6951-3B77-8272-FAEBCCC6BCAA
-  Functions: 3416
-  Symbols:   3875
-  CStrings:  2121
+  UUID: E677B92A-8826-36A0-94AD-9A3569C19DB3
+  Functions: 3423
+  Symbols:   3899
+  CStrings:  2138
 
Symbols:
+ -[ASCAgent _hasAnyCredentialsAvailableForRequestContext:]
+ -[ASCAgent _hasSignInOptionsForRequestContext:]
+ -[ASCAgent authorizationPresenter:didFinishWithCredential:error:]
+ -[ASCAuthorizationPresentationContext serviceType]
+ -[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:]
+ -[ASCAuthorizationTrafficController cancelAuthorizationForAppIdentifierIfNecessary:token:]
+ -[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:token:clearanceHandler:]
+ -[ASCPlatformPublicKeyCredentialLoginChoice compare:]
+ -[ASCPlatformPublicKeyCredentialRegistration isExternal]
+ -[ASCPlatformPublicKeyCredentialRegistration setIsExternal:]
+ -[ASCPlatformPublicKeyCredentialRegistration setRawClientDataJSON:]
+ GCC_except_table125
+ GCC_except_table128
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_ASCAgent._authorizationTrafficControllerToken
+ _OBJC_IVAR_$_ASCAuthorizationPresentationContext._serviceType
+ _OBJC_IVAR_$_ASCPlatformPublicKeyCredentialRegistration._isExternal
+ _WBSAuthenticationPolicyForPasswordManager
+ ___107-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:]_block_invoke
+ ___107-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:]_block_invoke.17
+ ___107-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:]_block_invoke.cold.1
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.100
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.97
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.288
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.291
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.313
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.154
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.154.cold.1
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.159
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.161
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.161.cold.1
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.170
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.174
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.87
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.87.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.90
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.90.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.94
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.94.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.55.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.56
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.60
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.63
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.64
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.64.cold.1
+ ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.224
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.68
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.73
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.73.cold.1
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.72
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.72.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.297.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.298
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.302
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.303
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.307
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.307.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.304
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.304.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.236
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.239
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.239.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.249
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.249.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.253
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.256.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.262
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.265
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.265.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.274
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.274.cold.1
+ ___90-[ASCAuthorizationTrafficController cancelAuthorizationForAppIdentifierIfNecessary:token:]_block_invoke
+ ___93-[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:token:clearanceHandler:]_block_invoke
+ ___93-[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:token:clearanceHandler:]_block_invoke_2
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.109
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.109.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.116
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.119
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.119.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.122
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.129
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0ls32l8s56l8r64l8s40l8s48l8r72l8
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.111
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.153
+ ___block_literal_global.156
+ ___block_literal_global.163
+ ___block_literal_global.176
+ ___block_literal_global.180
+ ___block_literal_global.207
+ ___block_literal_global.210
+ ___block_literal_global.227
+ ___block_literal_global.235
+ ___block_literal_global.238
+ ___block_literal_global.245
+ ___block_literal_global.255
+ ___block_literal_global.264
+ ___block_literal_global.267
+ ___block_literal_global.279
+ ___block_literal_global.282
+ ___block_literal_global.290
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.306
+ ___block_literal_global.311
+ ___block_literal_global.312
+ ___block_literal_global.315
+ ___block_literal_global.321
+ ___block_literal_global.527
+ ___block_literal_global.58
+ ___block_literal_global.62
+ ___block_literal_global.75
+ ___block_literal_global.89
+ ___block_literal_global.92
+ ___block_literal_global.96
+ _objc_msgSend$_hasAnyCredentialsAvailableForRequestContext:
+ _objc_msgSend$_hasSignInOptionsForRequestContext:
+ _objc_msgSend$authorizationPresenter:didFinishWithCredential:error:
+ _objc_msgSend$beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:
+ _objc_msgSend$cancelAuthorizationForAppIdentifierIfNecessary:token:
+ _objc_msgSend$computeClientDataIfNeededForAssertionOptions:
+ _objc_msgSend$credentialIdentity
+ _objc_msgSend$endAuthorizationForAppIdentifier:token:clearanceHandler:
+ _objc_msgSend$externalCredentialIdentity
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$rank
+ _objc_msgSend$rawClientDataJSON
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRawClientDataJSON:
- -[ASCAgent _hasAnyCredentialsAvailableForRequestTypes:]
- -[ASCAgent _hasSignInOptionsForRequestTypes:]
- -[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:withClearanceHandler:]
- -[ASCAuthorizationTrafficController cancelAuthorizationForAppIdentifierIfNecessary:]
- -[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:clearanceHandler:]
- GCC_except_table124
- GCC_except_table127
- ___101-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:withClearanceHandler:]_block_invoke
- ___101-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:withClearanceHandler:]_block_invoke.16
- ___101-[ASCAuthorizationTrafficController beginAuthorizationForApplicationIdentifier:withClearanceHandler:]_block_invoke.cold.1
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.96
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.99
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.279
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.282
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.307
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.153
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.153.cold.1
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.158
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.160
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.160.cold.1
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.169
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.173
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.85
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.85.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.89
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.89.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93.cold.1
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.54
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.54.cold.1
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.59
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.62
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.63
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.63.cold.1
- ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.218
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.67
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.72
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.72.cold.1
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.71
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.71.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.291
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.291.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.292
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.295
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.295.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.296
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.298
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.298.cold.1
- ___84-[ASCAuthorizationTrafficController cancelAuthorizationForAppIdentifierIfNecessary:]_block_invoke
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.227
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.230
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.233.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.237
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.237.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.247
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.250
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.250.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268.cold.1
- ___87-[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:clearanceHandler:]_block_invoke
- ___87-[ASCAuthorizationTrafficController endAuthorizationForAppIdentifier:clearanceHandler:]_block_invoke_2
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.108
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.108.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.115
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.118
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.118.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.121
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.128
- ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"<ASCCredentialProtocol>"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0ls32l8s48l8r56l8s40l8r64l8
- ___block_literal_global.101
- ___block_literal_global.104
- ___block_literal_global.106
- ___block_literal_global.110
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.162
- ___block_literal_global.175
- ___block_literal_global.179
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.232
- ___block_literal_global.239
- ___block_literal_global.249
- ___block_literal_global.252
- ___block_literal_global.261
- ___block_literal_global.273
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.305
- ___block_literal_global.309
- ___block_literal_global.313
- ___block_literal_global.516
- ___block_literal_global.57
- ___block_literal_global.61
- ___block_literal_global.74
- ___block_literal_global.88
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.98
- _objc_msgSend$_hasAnyCredentialsAvailableForRequestTypes:
- _objc_msgSend$_hasSignInOptionsForRequestTypes:
- _objc_msgSend$beginAuthorizationForApplicationIdentifier:withClearanceHandler:
- _objc_msgSend$cancelAuthorizationForAppIdentifierIfNecessary:
- _objc_msgSend$completeAssertionWithExternalPasskeyForUUID:usingCredential:
- _objc_msgSend$endAuthorizationForAppIdentifier:clearanceHandler:
- _objc_msgSend$requestOptions
CStrings:
+ "\x015\x1f"
+ "\x02\x15\x1d\x12"
+ "\x17"
+ "@\"NSMutableDictionary\""
+ "At least one of clientDataHash, challenge, or clientDataJSON must be non-nil"
+ "TQ,R,N,V_serviceType"
+ "_authorizationTrafficControllerToken"
+ "_hasAnyCredentialsAvailableForRequestContext:"
+ "_hasSignInOptionsForRequestContext:"
+ "_serviceType"
+ "apple.com"
+ "authorizationPresenter:didFinishWithCredential:error:"
+ "beginAuthorizationForApplicationIdentifier:token:withClearanceHandler:"
+ "cancelAuthorizationForAppIdentifierIfNecessary:token:"
+ "computeClientDataIfNeededForAssertionOptions:"
+ "endAuthorizationForAppIdentifier:token:clearanceHandler:"
+ "isEqualToSet:"
+ "objectForKeyedSubscript:"
+ "rank"
+ "serviceType"
+ "setObject:forKeyedSubscript:"
+ "v40@0:8@\"ASCAuthorizationPresenter\"16@\"<ASCCredentialProtocol>\"24@\"NSError\"32"
- "\x01\x15\x1d\x12"
- "\x01?\x05"
- "@\"NSMutableSet\""
- "B24@0:8Q16"
- "_hasAnyCredentialsAvailableForRequestTypes:"
- "_hasSignInOptionsForRequestTypes:"
- "beginAuthorizationForApplicationIdentifier:withClearanceHandler:"
- "cancelAuthorizationForAppIdentifierIfNecessary:"
- "completeAssertionWithExternalPasskeyForUUID:usingCredential:"
- "endAuthorizationForAppIdentifier:clearanceHandler:"

```
