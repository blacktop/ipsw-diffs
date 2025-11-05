## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/Versions/A/AuthenticationServicesCore`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0xab4e4
-  __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_methlist: 0x2778
-  __TEXT.__const: 0x7720
-  __TEXT.__cstring: 0x4172
-  __TEXT.__oslogstring: 0x2cdd
-  __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__ustring: 0x4ba
+621.1.15.11.10
+  __TEXT.__text: 0xacd94
+  __TEXT.__auth_stubs: 0x1e30
+  __TEXT.__objc_methlist: 0x31a0
+  __TEXT.__const: 0x7bc0
+  __TEXT.__cstring: 0x3f92
+  __TEXT.__oslogstring: 0x2b9d
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__ustring: 0x48e
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x1aab
-  __TEXT.__constg_swiftt: 0x1994
-  __TEXT.__swift5_reflstr: 0xe41
-  __TEXT.__swift5_fieldmd: 0x1a6c
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_assocty: 0x348
-  __TEXT.__swift5_proto: 0x7d8
-  __TEXT.__swift5_types: 0x220
-  __TEXT.__swift5_capture: 0x340
+  __TEXT.__swift5_typeref: 0x1b87
+  __TEXT.__constg_swiftt: 0x1b60
+  __TEXT.__swift5_reflstr: 0xf31
+  __TEXT.__swift5_fieldmd: 0x1b8c
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_assocty: 0x360
+  __TEXT.__swift5_proto: 0x820
+  __TEXT.__swift5_types: 0x23c
+  __TEXT.__swift5_capture: 0x350
   __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2f18
-  __TEXT.__eh_frame: 0x3348
-  __TEXT.__objc_classname: 0x7be
-  __TEXT.__objc_methname: 0x99fe
-  __TEXT.__objc_methtype: 0x2324
-  __TEXT.__objc_stubs: 0x4160
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x390
+  __TEXT.__unwind_info: 0x2d50
+  __TEXT.__eh_frame: 0x3518
+  __TEXT.__objc_classname: 0x788
+  __TEXT.__objc_methname: 0x9b3a
+  __TEXT.__objc_methtype: 0x23f5
+  __TEXT.__objc_stubs: 0x4180
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x1a8
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1790
+  __DATA_CONST.__objc_selrefs: 0x19b0
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __AUTH_CONST.__auth_got: 0xf18
-  __AUTH_CONST.__const: 0x5988
-  __AUTH_CONST.__cfstring: 0x1c80
-  __AUTH_CONST.__objc_const: 0x7760
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__const: 0x5b60
+  __AUTH_CONST.__cfstring: 0x1c60
+  __AUTH_CONST.__objc_const: 0x6740
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x1b90
-  __AUTH.__data: 0xe80
-  __DATA.__objc_ivar: 0x3c4
-  __DATA.__data: 0x2350
-  __DATA.__bss: 0xf950
+  __AUTH.__objc_data: 0x1c98
+  __AUTH.__data: 0xed0
+  __DATA.__objc_ivar: 0x3ac
+  __DATA.__data: 0x2430
+  __DATA.__bss: 0x10240
   __DATA.__common: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
+  - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FF44AD56-8C9F-3345-A001-C32AF73F65DC
-  Functions: 4266
-  Symbols:   3711
-  CStrings:  2408
+  UUID: 202E1E2F-5DD9-33F0-A10A-62E27F6299DF
+  Functions: 4229
+  Symbols:   3733
+  CStrings:  2393
 
Symbols:
+ +[ASCAgentInterface xpcInterface].cold.1
+ +[ASCAuthorizationPresenterHostInterface xpcInterface].cold.1
+ +[ASCAuthorizationTrafficController sharedInstance].cold.1
+ +[ASCViewServiceInterface xpcInterface].cold.1
+ +[ASCWebKitSPISupport getArePasskeysDisallowedForRelyingParty:withCompletionHandler:].cold.1
+ +[ASCWebKitSPISupport getCanCurrentProcessAccessPasskeysForRelyingParty:withCompletionHandler:].cold.1
+ +[ASFeatureManager sharedManager].cold.1
+ +[_ASDevice deviceClass].cold.1
+ -[ASAgentAutoFillListener didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:]
+ -[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:]
+ -[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:].cold.1
+ -[ASAuthorizationRemoteViewController cancelExportFlow]
+ -[ASCAgent _configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:testOptions:completionHandler:]
+ -[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]
+ -[ASCAgent requestNewPINWithMinLength:completionHandler:]
+ -[ASCAgent requestToTurnOnCredentialProviderExtensionWithCompletionHandler:].cold.1
+ -[ASCAuthorizationPresentationContext testOptions]
+ -[ASCAuthorizationPresenter presentNewPINEntryInterfaceWithMinLength:]
+ -[ASCAuthorizationRemotePresenter cancelExportFlow]
+ -[ASCCredentialRequestContext requestRequiresRelyingParty]
+ -[ASCCredentialRequestContext setTestOptions:]
+ -[ASCCredentialRequestContext testOptions]
+ -[ASPublicKeyCredentialOperationTestDelegate requestNewPINWithMinLength:completionHandler:]
+ -[NSString(AuthenticationServiceCoreExtras) isValidRPIDForHost:]
+ -[NSString(AuthenticationServiceCoreExtras) isValidRPIDForOrigin:]
+ GCC_except_table110
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table42
+ GCC_except_table81
+ OBJC_IVAR_$_ASCAgent._conditionalRegistrationRequesterProxy
+ OBJC_IVAR_$_ASCAuthorizationPresentationContext._testOptions
+ OBJC_IVAR_$_ASCCredentialRequestContext._testOptions
+ WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent.cold.1
+ WBS_LOG_CHANNEL_PREFIXAuthorization.cold.1
+ _OBJC_CLASS_$__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ _OBJC_CLASS_$__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ _OBJC_METACLASS_$__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ _OBJC_METACLASS_$__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ _PROTOCOLS__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions.12
+ _PROTOCOLS__TtC26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputs.40
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.117
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.121
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.173
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.173.cold.1
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.175
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.179
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke.179.cold.1
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke_2.118
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke_2.118.cold.1
+ __124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke_2.cold.1
+ __32-[ASCAgent cancelCurrentRequest]_block_invoke.238
+ __32-[ASCAgent cancelCurrentRequest]_block_invoke.241
+ __47-[ASCAgent listener:shouldAcceptNewConnection:]_block_invoke.297
+ __52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.452
+ __52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.455
+ __55-[ASAuthorizationRemoteViewController cancelExportFlow]_block_invoke.cold.1
+ __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.475
+ __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.481
+ __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.481.cold.1
+ __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.483
+ __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.486
+ __64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.379
+ __64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.382
+ __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.304
+ __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.304.cold.1
+ __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.307
+ __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.307.cold.1
+ __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.312
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.229
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.229.cold.1
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.230
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.230.cold.1
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.233
+ __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.233.cold.1
+ __85-[ASAuthorizationRemoteViewController beginExportFlowWithData:withCompletionHandler:]_block_invoke.23
+ __85-[ASAuthorizationRemoteViewController presentSheetForNearbyDevice:completionHandler:]_block_invoke.30
+ __87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.463
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.387.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.393
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.399
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.405
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.405.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.413
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.413.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.419
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.419.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.423
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.426
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.426.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.427
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.427.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.433
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.436
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.436.cold.1
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.442
+ __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.442.cold.1
+ __90-[ASAuthorizationRemoteViewController beginAuthorizationOnEndpoint:withCompletionHandler:]_block_invoke.20
+ __90-[ASAuthorizationRemoteViewController beginAuthorizationOnEndpoint:withCompletionHandler:]_block_invoke.21
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.250
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.250.cold.1
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.257
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.260
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.260.cold.1
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.263
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.268
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.270
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.273
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.273.cold.1
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.274
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.283
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.286
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.271
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.271.cold.1
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.280
+ __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.272
+ __CFHostIsDomainTopLevel
+ __CLASS_METHODS__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __CLASS_PROPERTIES__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __DATA__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ __DATA__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __INSTANCE_METHODS__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ __INSTANCE_METHODS__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __IVARS__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ __IVARS__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __METACLASS_DATA__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ __METACLASS_DATA__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_AuthenticationServiceCoreExtras
+ __OBJC_$_CATEGORY_NSString_$_AuthenticationServiceCoreExtras
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSConditionalRegistrationRequester
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSConditionalRegistrationRequester
+ __OBJC_$_PROTOCOL_REFS_WBSConditionalRegistrationRequester
+ __OBJC_LABEL_PROTOCOL_$_WBSConditionalRegistrationRequester
+ __OBJC_PROTOCOL_$_WBSConditionalRegistrationRequester
+ __OBJC_PROTOCOL_REFERENCE_$_WBSConditionalRegistrationRequester
+ __PROPERTIES__TtC26AuthenticationServicesCore22ASCPasswordSignInEvent
+ __PROPERTIES__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ __PROTOCOLS__TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions
+ ___124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke
+ ___124-[ASCAgent _requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:]_block_invoke_2
+ ___55-[ASAuthorizationRemoteViewController cancelExportFlow]_block_invoke
+ ___block_descriptor_40_e8_32bs_e64_v24?0"ASCPlatformPublicKeyCredentialRegistration"8"NSError"16l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e66_v16?0"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e21_v16?0"NSExtension"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy33_8
+ ___swift_memcpy56_8
+ __block_literal_global.129
+ __block_literal_global.134
+ __block_literal_global.136
+ __block_literal_global.181
+ __block_literal_global.232
+ __block_literal_global.235
+ __block_literal_global.237
+ __block_literal_global.240
+ __block_literal_global.243
+ __block_literal_global.246
+ __block_literal_global.252
+ __block_literal_global.259
+ __block_literal_global.262
+ __block_literal_global.276
+ __block_literal_global.282
+ __block_literal_global.285
+ __block_literal_global.288
+ __block_literal_global.29
+ __block_literal_global.295
+ __block_literal_global.306
+ __block_literal_global.309
+ __block_literal_global.330
+ __block_literal_global.343
+ __block_literal_global.364
+ __block_literal_global.381
+ __block_literal_global.386
+ __block_literal_global.395
+ __block_literal_global.398
+ __block_literal_global.401
+ __block_literal_global.415
+ __block_literal_global.429
+ __block_literal_global.435
+ __block_literal_global.438
+ __block_literal_global.449
+ __block_literal_global.451
+ __block_literal_global.454
+ __block_literal_global.457
+ __block_literal_global.462
+ __block_literal_global.465
+ __block_literal_global.467
+ __block_literal_global.471
+ __block_literal_global.477
+ __block_literal_global.485
+ __block_literal_global.488
+ __block_literal_global.492
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOSHAASQ
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO14FailCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO14FailCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO17SuccessCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO17SuccessCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultOSHAASQ
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOSHAASQ
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _keypath_getTm
+ _keypath_setTm
+ _noCredentialsErrorString
+ _objc_msgSend$_configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:testOptions:completionHandler:
+ _objc_msgSend$_requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:
+ _objc_msgSend$beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:testOptions:
+ _objc_msgSend$beginCreatingNewSecurityKeyCredentialIfAvailableWithOptions:delegate:webFrameIdentifier:parentActivity:testOptions:
+ _objc_msgSend$cancelExportFlow
+ _objc_msgSend$createNewPlatformCredentialWithOptions:authenticatedContext:delegate:webFrameIdentifier:parentActivity:isConditionalRegistration:testOptions:
+ _objc_msgSend$didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:
+ _objc_msgSend$didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:
+ _objc_msgSend$externalProviderListenerEndpoint
+ _objc_msgSend$isUserAllowedToTogglePasswordAutoFillEnabledState
+ _objc_msgSend$isValidRPIDForHost:
+ _objc_msgSend$isValidRPIDForOrigin:
+ _objc_msgSend$presentNewPINEntryInterfaceWithMinLength:
+ _objc_msgSend$providerBundleIdentifier
+ _objc_msgSend$requestAutomaticPasskeyUpgradeWithLoginChoice:completionHandler:
+ _objc_msgSend$requestRequiresRelyingParty
+ _objc_msgSend$signInEventForRecentlyFilledCredentialWithUsername:forAppWithBundleIdentifier:completionHandler:
+ _objc_msgSend$signInEventForRecentlyFilledCredentialWithUsername:forRelyingPartyIdentifier:inAppWithBundleIdentifier:completionHandler:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$testOptions
+ _symbolic So21NSXPCListenerEndpointCSg
+ _symbolic _____ 26AuthenticationServicesCore22ASCPasswordSignInEventC
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO14FailCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO17SuccessCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____ 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____ So14LABiometryTypeV
+ _symbolic _____Sg 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalA6ResultO
+ _symbolic _____Sg So14LABiometryTypeV
+ _symbolic _____SgIeyBy_ 26AuthenticationServicesCore22ASCPasswordSignInEventC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO14FailCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO17SuccessCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO14FailCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC05LocalD6ResultO17SuccessCodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AuthenticationServicesCore31ASCCredentialRequestTestOptionsC10CodingKeys33_E99877A236D9CD0AC4407F7B99BBD097LLO
+ descriptionForErrorCode.cold.1
+ objectdestroy.24Tm
- -[ASAgentAutoFillListener didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:]
- -[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:]
- -[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:].cold.1
- -[ASCAgent _configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:completionHandler:]
- -[ASCAgent _isRPIDValid:forOrigin:]
- -[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]
- -[ASCAgent test_isRPIDValid:forOrigin:]
- -[ASCAgentCredentialExchangeListener .cxx_destruct]
- -[ASCAgentCredentialExchangeListener _atLeastOneAppAvailableForImportForConnection:]
- -[ASCAgentCredentialExchangeListener _atLeastOneAppAvailableForImportForConnection:].cold.1
- -[ASCAgentCredentialExchangeListener exportCredentials:completionHandler:]
- -[ASCAgentCredentialExchangeListener exportCredentials:completionHandler:].cold.1
- -[ASCAgentCredentialExchangeListener exportCredentials:completionHandler:].cold.2
- -[ASCAgentCredentialExchangeListener exportCredentials:completionHandler:].cold.3
- -[ASCAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:]
- -[ASCAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:].cold.1
- -[ASCAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:].cold.2
- -[ASCAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:].cold.3
- -[ASCAgentCredentialExchangeListener init]
- -[ASCAgentCredentialExchangeListener listener:shouldAcceptNewConnection:]
- -[ASCAgentCredentialExchangeListener listener:shouldAcceptNewConnection:].cold.1
- -[ASCAgentCredentialExchangeListener setTokenForImport:]
- -[ASCAgentCredentialExchangeListener setTokenForImport:].cold.1
- -[ASCAgentCredentialExchangeListenerProxy .cxx_destruct]
- -[ASCAgentCredentialExchangeListenerProxy _reconnectIfNecessary]
- -[ASCAgentCredentialExchangeListenerProxy _remoteObjectProxyWithErrorHandler:]
- -[ASCAgentCredentialExchangeListenerProxy _remoteObjectProxyWithErrorHandler:].cold.1
- -[ASCAgentCredentialExchangeListenerProxy _setUpConnection:]
- -[ASCAgentCredentialExchangeListenerProxy exportCredentials:completionHandler:]
- -[ASCAgentCredentialExchangeListenerProxy importCredentialsWithToken:completionHandler:]
- -[ASCAgentCredentialExchangeListenerProxy init]
- -[ASCAgentCredentialExchangeListenerProxy setTokenForImport:]
- ASCAgentCredentialExchangeListenerInterface.interface
- ASCAgentCredentialExchangeListenerInterface.onceToken
- GCC_except_table1
- GCC_except_table105
- GCC_except_table14
- GCC_except_table156
- GCC_except_table77
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._connection
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._exportedCredentialData
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._importerBundleID
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._importerToken
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._internalLock
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._listener
- OBJC_IVAR_$_ASCAgentCredentialExchangeListener._presenter
- OBJC_IVAR_$_ASCAgentCredentialExchangeListenerProxy._activity
- OBJC_IVAR_$_ASCAgentCredentialExchangeListenerProxy._connection
- _ASCAgentCredentialExchangeListenerInterface
- _ASCAgentCredentialExchangeServiceName
- _OBJC_CLASS_$_ASCAgentCredentialExchangeListener
- _OBJC_CLASS_$_ASCAgentCredentialExchangeListenerProxy
- _OBJC_CLASS_$_NSTimer
- _OBJC_METACLASS_$_ASCAgentCredentialExchangeListener
- _OBJC_METACLASS_$_ASCAgentCredentialExchangeListenerProxy
- _PROTOCOLS__TtC26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputs.39
- _SFCredentialProviderDeveloperEntitlement
- _SFCredentialProviderSystemEntitlement
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke.117
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke.121
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke.125
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke.125.cold.1
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke_2.118
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke_2.118.cold.1
- __107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke_2.cold.1
- __32-[ASCAgent cancelCurrentRequest]_block_invoke.183
- __32-[ASCAgent cancelCurrentRequest]_block_invoke.186
- __47-[ASCAgent listener:shouldAcceptNewConnection:]_block_invoke.256
- __52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.406
- __52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.409
- __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.429
- __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.435
- __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.435.cold.1
- __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.437
- __56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.440
- __60-[ASCAgentCredentialExchangeListenerProxy _setUpConnection:]_block_invoke.cold.1
- __61-[ASCAgentCredentialExchangeListenerProxy setTokenForImport:]_block_invoke_2.cold.1
- __64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.334
- __64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.337
- __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.261
- __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.261.cold.1
- __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.264
- __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.264.cold.1
- __69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.269
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.174
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.174.cold.1
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.175
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.175.cold.1
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.178
- __72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.178.cold.1
- __78-[ASCAgentCredentialExchangeListenerProxy _remoteObjectProxyWithErrorHandler:]_block_invoke.cold.1
- __79-[ASCAgentCredentialExchangeListenerProxy exportCredentials:completionHandler:]_block_invoke_2.cold.1
- __85-[ASAuthorizationRemoteViewController beginExportFlowWithData:withCompletionHandler:]_block_invoke.21
- __85-[ASAuthorizationRemoteViewController presentSheetForNearbyDevice:completionHandler:]_block_invoke.26
- __87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.417
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.342
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.342.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.348
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.351
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.354
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.360
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.360.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.364
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.364.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.368
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.368.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.374
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.374.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.378
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.381
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.381.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.390
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.390.cold.1
- __87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.396.cold.1
- __88-[ASCAgentCredentialExchangeListenerProxy importCredentialsWithToken:completionHandler:]_block_invoke_2.cold.1
- __90-[ASAuthorizationRemoteViewController beginAuthorizationOnEndpoint:withCompletionHandler:]_block_invoke.18
- __90-[ASAuthorizationRemoteViewController beginAuthorizationOnEndpoint:withCompletionHandler:]_block_invoke.19
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.195
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.195.cold.1
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.202
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.205
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.205.cold.1
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.208
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.213
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.216
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.219
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.219.cold.1
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.220
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.229
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.217
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.217.cold.1
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.226
- __96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.218
- __OBJC_$_INSTANCE_METHODS_ASCAgentCredentialExchangeListener
- __OBJC_$_INSTANCE_METHODS_ASCAgentCredentialExchangeListenerProxy
- __OBJC_$_INSTANCE_VARIABLES_ASCAgentCredentialExchangeListener
- __OBJC_$_INSTANCE_VARIABLES_ASCAgentCredentialExchangeListenerProxy
- __OBJC_$_PROP_LIST_ASCAgentCredentialExchangeListener
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCAgentCredentialExchangeListenerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASCAgentCredentialExchangeListenerInterface
- __OBJC_CLASS_PROTOCOLS_$_ASCAgentCredentialExchangeListener
- __OBJC_CLASS_PROTOCOLS_$_ASCAgentCredentialExchangeListenerProxy
- __OBJC_CLASS_RO_$_ASCAgentCredentialExchangeListener
- __OBJC_CLASS_RO_$_ASCAgentCredentialExchangeListenerProxy
- __OBJC_LABEL_PROTOCOL_$_ASCAgentCredentialExchangeListenerInterface
- __OBJC_METACLASS_RO_$_ASCAgentCredentialExchangeListener
- __OBJC_METACLASS_RO_$_ASCAgentCredentialExchangeListenerProxy
- __OBJC_PROTOCOL_$_ASCAgentCredentialExchangeListenerInterface
- __OBJC_PROTOCOL_REFERENCE_$_ASCAgentCredentialExchangeListenerInterface
- ___107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke
- ___107-[ASCAgent _requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:]_block_invoke_2
- ___60-[ASCAgentCredentialExchangeListenerProxy _setUpConnection:]_block_invoke
- ___61-[ASCAgentCredentialExchangeListenerProxy setTokenForImport:]_block_invoke
- ___61-[ASCAgentCredentialExchangeListenerProxy setTokenForImport:]_block_invoke_2
- ___73-[ASCAgentCredentialExchangeListener listener:shouldAcceptNewConnection:]_block_invoke
- ___74-[ASCAgentCredentialExchangeListener exportCredentials:completionHandler:]_block_invoke
- ___78-[ASCAgentCredentialExchangeListenerProxy _remoteObjectProxyWithErrorHandler:]_block_invoke
- ___79-[ASCAgentCredentialExchangeListenerProxy exportCredentials:completionHandler:]_block_invoke
- ___79-[ASCAgentCredentialExchangeListenerProxy exportCredentials:completionHandler:]_block_invoke_2
- ___88-[ASCAgentCredentialExchangeListenerProxy importCredentialsWithToken:completionHandler:]_block_invoke
- ___88-[ASCAgentCredentialExchangeListenerProxy importCredentialsWithToken:completionHandler:]_block_invoke_2
- ___ASCAgentCredentialExchangeListenerInterface_block_invoke
- ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e18_v16?0"NSString"8l
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e21_v16?0"NSExtension"8l
- ___copy_helper_block_e8_32s40s48s56s64b72r
- __block_literal_global.121
- __block_literal_global.126
- __block_literal_global.128
- __block_literal_global.133
- __block_literal_global.177
- __block_literal_global.180
- __block_literal_global.182
- __block_literal_global.185
- __block_literal_global.188
- __block_literal_global.191
- __block_literal_global.197
- __block_literal_global.204
- __block_literal_global.207
- __block_literal_global.222
- __block_literal_global.228
- __block_literal_global.231
- __block_literal_global.25
- __block_literal_global.254
- __block_literal_global.263
- __block_literal_global.266
- __block_literal_global.273
- __block_literal_global.286
- __block_literal_global.298
- __block_literal_global.319
- __block_literal_global.336
- __block_literal_global.341
- __block_literal_global.344
- __block_literal_global.350
- __block_literal_global.353
- __block_literal_global.356
- __block_literal_global.380
- __block_literal_global.383
- __block_literal_global.392
- __block_literal_global.400
- __block_literal_global.403
- __block_literal_global.405
- __block_literal_global.408
- __block_literal_global.411
- __block_literal_global.416
- __block_literal_global.419
- __block_literal_global.421
- __block_literal_global.431
- __block_literal_global.439
- __block_literal_global.442
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AuthenticationServicesCore
- _associated conformance 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLOSHAASQ
- _associated conformance 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLOs0F3KeyAAs23CustomStringConvertible
- _associated conformance 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLOs0F3KeyAAs28CustomDebugStringConvertible
- _objc_msgSend$_atLeastOneAppAvailableForImportForConnection:
- _objc_msgSend$_configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:completionHandler:
- _objc_msgSend$_isRPIDValid:forOrigin:
- _objc_msgSend$_requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:
- _objc_msgSend$atLeastOneAvailableExtensionSupportsCredentialExchange:
- _objc_msgSend$beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:
- _objc_msgSend$beginCreatingNewSecurityKeyCredentialIfAvailableWithOptions:delegate:webFrameIdentifier:parentActivity:
- _objc_msgSend$createNewPlatformCredentialWithOptions:authenticatedContext:delegate:webFrameIdentifier:parentActivity:isConditionalRegistration:
- _objc_msgSend$didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:
- _objc_msgSend$didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:
- _objc_msgSend$exportCredentials:completionHandler:
- _objc_msgSend$importCredentialsWithToken:completionHandler:
- _objc_msgSend$providerForRecentlyFilledCredentialWithUsername:forAppWithBundleIdentifier:completionHandler:
- _objc_msgSend$providerForRecentlyFilledCredentialWithUsername:forRelyingPartyIdentifier:inAppWithBundleIdentifier:completionHandler:
- _objc_msgSend$safari_domainFromHost
- _objc_msgSend$safari_effectiveTopLevelDomainForHost
- _objc_msgSend$safari_highLevelDomainFromHost
- _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
- _objc_msgSend$setTokenForImport:
- _symbolic So8NSStringCSgIeyBy_
- _symbolic _____ 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLO
- _symbolic _____Sg 26AuthenticationServicesCore41ASCTAPAuthenticatorMakeCredentialResponseV
- _symbolic _____y_____G s22KeyedDecodingContainerV 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 26AuthenticationServicesCore20ASCTAPCredentialDataV10CodingKeys33_629875BA8F16EF0226BC3CEBF7561DC0LLO
- objectdestroy.18Tm
CStrings:
+ "-[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:]"
+ "."
+ "@\"<WBSConditionalRegistrationRequester>\""
+ "@\"_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions\""
+ "Attempted to make a request of type %lx without setting relying party."
+ "AuthenticationServiceCoreExtras"
+ "AuthenticationServicesCore.ASCPasswordSignInEvent"
+ "AuthenticationServicesCore/ASCCredentialRequestTestOptions.swift"
+ "Lost connection to automatic passkey upgrade requester: %{public}@"
+ "No available credentials and not using preferImmediatelyAvailableCredentials, show error message sheet"
+ "Password AutoFill is restricted by a management profile"
+ "Pin entered was too long. Please choose a shorter one."
+ "Pin entered was too short. Please choose a longer one."
+ "T@\"NSArray\",C,N"
+ "T@\"NSData\",C,N"
+ "T@\"NSNumber\",C,N"
+ "T@\"NSString\",C,N"
+ "T@\"NSXPCListenerEndpoint\",N,R,VexternalProviderListenerEndpoint"
+ "T@\"_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions\",&,N,V_testOptions"
+ "T@\"_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions\",R,C,N,V_testOptions"
+ "WBSConditionalRegistrationRequester"
+ "_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent"
+ "_TtC26AuthenticationServicesCore31ASCCredentialRequestTestOptions"
+ "_conditionalRegistrationRequesterProxy"
+ "_configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:testOptions:completionHandler:"
+ "_requestConditionalRegistrationOnProvider:listenerEndpoint:presentationContext:requestContext:completionHandler:"
+ "_testOptions"
+ "beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:testOptions:"
+ "beginCreatingNewSecurityKeyCredentialIfAvailableWithOptions:delegate:webFrameIdentifier:parentActivity:testOptions:"
+ "cancelExportFlow"
+ "createNewPlatformCredentialWithOptions:authenticatedContext:delegate:webFrameIdentifier:parentActivity:isConditionalRegistration:testOptions:"
+ "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:"
+ "didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:"
+ "didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:"
+ "didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:"
+ "externalProviderListenerEndpoint"
+ "hasPasscode"
+ "inputWasAlreadyHashedForHybrid"
+ "isUserAllowedToTogglePasswordAutoFillEnabledState"
+ "isValidRPIDForHost:"
+ "isValidRPIDForOrigin:"
+ "localAuthenticationResult"
+ "presentNewPINEntryInterfaceWithMinLength:"
+ "requestAutomaticPasskeyUpgradeWithLoginChoice:completionHandler:"
+ "requestNewPINWithMinLength:completionHandler:"
+ "requestRequiresRelyingParty"
+ "setTestOptions:"
+ "shouldAutoFillFromICloudKeychain"
+ "signInEventForRecentlyFilledCredentialWithUsername:forAppWithBundleIdentifier:completionHandler:"
+ "signInEventForRecentlyFilledCredentialWithUsername:forRelyingPartyIdentifier:inAppWithBundleIdentifier:completionHandler:"
+ "stringByAppendingString:"
+ "testOptions"
+ "v16@?0@\"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent\"8"
+ "v24@?0@\"ASCPlatformPublicKeyCredentialRegistration\"8@\"NSError\"16"
+ "v32@0:8@\"ASCPlatformPublicKeyCredentialLoginChoice\"16@?<v@?@\"ASCPlatformPublicKeyCredentialRegistration\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent\">40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSXPCListenerEndpoint\"48"
+ "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40@\"NSXPCListenerEndpoint\"48"
+ "v56@0:8@16@24q32@40@?48"
- "-[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:]"
- "@\"ASCAuthorizationPresenter\""
- "ASCAgentCredentialExchangeListener"
- "ASCAgentCredentialExchangeListenerInterface"
- "ASCAgentCredentialExchangeListenerProxy"
- "Can't construct Array with count < 0"
- "Connection to AuthenticationServicesAgent closed"
- "Credential Exchange listener"
- "Developer mode must be enabled for this API. You can do this with the command `defaults write com.apple.AuthenticationServices.Developer CredentialExchangeEnabled -bool YES`"
- "Division by zero"
- "Division results in an overflow"
- "Export not available because passcode and/or biometrics are not enabled"
- "Exported credential data not found"
- "Exported credential data not found."
- "Exported data was not consumed for five minutes, deleting"
- "Insufficient space allocated to copy string contents"
- "Invalid importer token"
- "Negative value is not representable"
- "No apps available for import"
- "Not enough bits to represent the passed value"
- "Rejecting connection from unentitled process"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "The import request came from a client that did not match the one selected by the user for import."
- "Token for importer must only be set by the view service"
- "Unable to get exporting app's bundle ID"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_atLeastOneAppAvailableForImportForConnection:"
- "_configurePublicKeyCredentialsWithAssertionOptions:forProcessWithApplicationIdentifier:requestStyle:completionHandler:"
- "_exportedCredentialData"
- "_importerBundleID"
- "_importerToken"
- "_isRPIDValid:forOrigin:"
- "_presenter"
- "_requestConditionalRegistrationOnProvider:presentationContext:requestContext:completionHandler:"
- "atLeastOneAvailableExtensionSupportsCredentialExchange:"
- "beginAssertionsWithOptions:forProcessWithApplicationIdentifier:delegate:requestStyle:webFrameIdentifier:parentActivity:"
- "beginCreatingNewSecurityKeyCredentialIfAvailableWithOptions:delegate:webFrameIdentifier:parentActivity:"
- "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange"
- "com.apple.Passwords"
- "createNewPlatformCredentialWithOptions:authenticatedContext:delegate:webFrameIdentifier:parentActivity:isConditionalRegistration:"
- "credentialPublicKey"
- "didFillCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:"
- "didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:"
- "didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:"
- "didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:"
- "exportCredentials:completionHandler:"
- "importCredentialsWithToken:completionHandler:"
- "invalid Collection: less than 'count' elements in collection"
- "providerForRecentlyFilledCredentialWithUsername:forAppWithBundleIdentifier:completionHandler:"
- "providerForRecentlyFilledCredentialWithUsername:forRelyingPartyIdentifier:inAppWithBundleIdentifier:completionHandler:"
- "safari_domainFromHost"
- "safari_effectiveTopLevelDomainForHost"
- "safari_highLevelDomainFromHost"
- "safari_isHostOrSubdomainOfHost:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "setTokenForImport:"
- "test_isRPIDValid:forOrigin:"
- "v16@?0@\"NSString\"8"
- "v16@?0@\"NSTimer\"8"
- "v24@0:8@\"NSUUID\"16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\">32"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40"

```
