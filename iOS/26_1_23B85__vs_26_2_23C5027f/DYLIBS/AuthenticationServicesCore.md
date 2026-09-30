## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-622.2.11.10.8
-  __TEXT.__text: 0xc0224
-  __TEXT.__auth_stubs: 0x2580
-  __TEXT.__objc_methlist: 0x37c4
-  __TEXT.__const: 0xc548
-  __TEXT.__cstring: 0x55b2
-  __TEXT.__oslogstring: 0x3fd0
+623.1.12.10.4
+  __TEXT.__text: 0xc6fc0
+  __TEXT.__auth_stubs: 0x2600
+  __TEXT.__objc_methlist: 0x396c
+  __TEXT.__const: 0xca78
+  __TEXT.__cstring: 0x5992
+  __TEXT.__oslogstring: 0x3fc0
   __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__swift5_typeref: 0x21ff
-  __TEXT.__constg_swiftt: 0x23d0
-  __TEXT.__swift5_reflstr: 0x1651
-  __TEXT.__swift5_fieldmd: 0x2188
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0x92c
-  __TEXT.__swift5_types: 0x29c
-  __TEXT.__swift5_capture: 0x478
-  __TEXT.__swift_as_entry: 0x70
-  __TEXT.__swift_as_ret: 0x60
-  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_typeref: 0x23d3
+  __TEXT.__constg_swiftt: 0x25ac
+  __TEXT.__swift5_reflstr: 0x1751
+  __TEXT.__swift5_fieldmd: 0x22f4
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_assocty: 0x438
+  __TEXT.__swift5_proto: 0x96c
+  __TEXT.__swift5_types: 0x2b4
+  __TEXT.__swift5_capture: 0x53c
+  __TEXT.__swift_as_entry: 0x80
+  __TEXT.__swift_as_ret: 0x68
+  __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3248
-  __TEXT.__eh_frame: 0x4260
-  __TEXT.__objc_classname: 0x7a9
-  __TEXT.__objc_methname: 0xac35
-  __TEXT.__objc_methtype: 0x284a
-  __TEXT.__objc_stubs: 0x4520
-  __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __TEXT.__unwind_info: 0x3460
+  __TEXT.__eh_frame: 0x44f8
+  __TEXT.__objc_classname: 0x7aa
+  __TEXT.__objc_methname: 0xb31a
+  __TEXT.__objc_methtype: 0x2a60
+  __TEXT.__objc_stubs: 0x46c0
+  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__const: 0xc80
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d00
+  __DATA_CONST.__objc_selrefs: 0x1db8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH_CONST.__const: 0x61d8
-  __AUTH_CONST.__cfstring: 0x1fc0
-  __AUTH_CONST.__objc_const: 0x7810
+  __AUTH_CONST.__auth_got: 0x1310
+  __AUTH_CONST.__const: 0x6388
+  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__objc_const: 0x7bb8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xbb8
-  __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x40c
-  __DATA.__data: 0x2870
-  __DATA.__bss: 0x11050
+  __AUTH.__objc_data: 0xd08
+  __AUTH.__data: 0x480
+  __DATA.__objc_ivar: 0x418
+  __DATA.__data: 0x2990
+  __DATA.__bss: 0x116c0
   __DATA.__common: 0x1c8
-  __DATA_DIRTY.__objc_data: 0x1bf0
-  __DATA_DIRTY.__data: 0x1078
-  __DATA_DIRTY.__bss: 0x1320
+  __DATA_DIRTY.__objc_data: 0x1c38
+  __DATA_DIRTY.__data: 0x1088
+  __DATA_DIRTY.__bss: 0x1300
   __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 51ADABED-C98A-3209-94B0-424F9A8B63B7
-  Functions: 4733
-  Symbols:   5325
-  CStrings:  2810
+  UUID: 3FC4CC4B-6C6B-34D0-B669-9C2AEAF95291
+  Functions: 4906
+  Symbols:   5387
+  CStrings:  2875
 
Symbols:
+ -[ASAgentAutoFillListener credentialProviderInformationForAutoFillOfUsername:password:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:]
+ -[ASAgentAutoFillListener credentialProviderInformationForGenerationOfStrongPassword:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:]
+ -[ASAgentAutoFillListener didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:listenerEndpoint:]
+ -[ASAgentAutoFillListener didGenerateStrongPassword:passwordKind:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:]
+ -[ASCAuthorizationPresenter userDidSelectImportingDestinationWithApplicationIdentifier:]
+ -[ASCAuthorizationPresenter userDidSelectImportingDestinationWithApplicationIdentifier:].cold.1
+ -[ASCPasswordCredential externalProviderExtensionBundleIdentifier]
+ -[ASCPasswordCredential initWithUser:password:serviceIdentifierType:serviceIdentifier:site:creationDate:externalProviderBundleIdentifier:externalProviderExtensionBundleIdentifier:]
+ -[ASCPasswordCredential serviceIdentifierType]
+ -[ASCPasswordCredential serviceIdentifier]
+ -[ASFeatureManager passwordManagerResourcesProjectImportCommitURL]
+ -[ASFeatureManager passwordManagerResourcesProjectImportCommit]
+ -[ASFeatureManager passwordManagerResourcesProjectURL]
+ GCC_except_table13
+ _OBJC_CLASS_$_ASCCredentialProvider
+ _OBJC_CLASS_$__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ _OBJC_IVAR_$_ASCPasswordCredential._externalProviderExtensionBundleIdentifier
+ _OBJC_IVAR_$_ASCPasswordCredential._serviceIdentifier
+ _OBJC_IVAR_$_ASCPasswordCredential._serviceIdentifierType
+ _OBJC_METACLASS_$_ASCCredentialProvider
+ _OBJC_METACLASS_$__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ _WBSOSLogAuthenticationServicesAgent
+ _WBSOSLogAuthorization
+ _WBSOSLogServiceLifecycle
+ __DATA_ASCCredentialProvider
+ __DATA__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ __DATA__TtCE26AuthenticationServicesCoreCSo21ASCCredentialProviderP33_201E360AC0331836C3310F408B4E094F3Box
+ __INSTANCE_METHODS__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ __IVARS_ASCCredentialProvider
+ __IVARS__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ __IVARS__TtCE26AuthenticationServicesCoreCSo21ASCCredentialProviderP33_201E360AC0331836C3310F408B4E094F3Box
+ __METACLASS_DATA_ASCCredentialProvider
+ __METACLASS_DATA__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ __METACLASS_DATA__TtCE26AuthenticationServicesCoreCSo21ASCCredentialProviderP33_201E360AC0331836C3310F408B4E094F3Box
+ __OBJC_$_INSTANCE_METHODS_ASCCredentialProvider(AuthenticationServicesCore)
+ __PROPERTIES__TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent
+ __PROTOCOLS__TtC26AuthenticationServicesCore38ASCPasskeyAccountRegistrationUserState.27
+ __PROTOCOLS__TtC26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputs.58
+ ___176-[ASAgentAutoFillListener credentialProviderInformationForGenerationOfStrongPassword:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:]_block_invoke
+ ___177-[ASAgentAutoFillListener credentialProviderInformationForAutoFillOfUsername:password:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:]_block_invoke
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.422
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.461
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.466
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.466.cold.1
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.468
+ ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.350
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.443
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.443.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.444
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.447.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.448
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.449
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.453
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.453.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.450
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.450.cold.1
+ ___87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.432
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.357
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.357.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.363
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.375
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.375.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.379
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.379.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.383
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.383.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.389
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.389.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.393
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.396.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.397
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.397.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.403
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.406.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.412
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.412.cold.1
+ ___block_descriptor_40_e8_32bs_e66_v16?0"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent"8ls32l8
+ ___block_descriptor_40_e8_32bs_e70_v16?0"_TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent"8ls32l8
+ ___block_literal_global.313
+ ___block_literal_global.331
+ ___block_literal_global.352
+ ___block_literal_global.356
+ ___block_literal_global.365
+ ___block_literal_global.385
+ ___block_literal_global.395
+ ___block_literal_global.399
+ ___block_literal_global.405
+ ___block_literal_global.416
+ ___block_literal_global.421
+ ___block_literal_global.431
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.452
+ ___block_literal_global.457
+ ___block_literal_global.463
+ ___block_literal_global.470
+ ___block_literal_global.474
+ ___block_literal_global.696
+ ___swift_mutable_project_boxed_opaque_existential_1
+ _associated conformance 26AuthenticationServicesCore19ASCPrivacySensitiveVyxGSHAASHRzlSQ
+ _associated conformance 26AuthenticationServicesCore21ASCCredentialProviderOSHAASQ
+ _associated conformance 26AuthenticationServicesCore21ASCCredentialProviderOs12IdentifiableAA2IDsADP_SH
+ _block_copy_helper.3
+ _block_descriptor.5
+ _block_destroy_helper.4
+ _get_enum_tag_for_layout_string 26AuthenticationServicesCore21ASCCredentialProviderO
+ _keypath_get.14Tm
+ _keypath_get.6Tm
+ _objc_msgSend$absoluteString
+ _objc_msgSend$didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:listenerEndpoint:
+ _objc_msgSend$didGenerateStrongPassword:passwordKind:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:
+ _objc_msgSend$didUseCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:listenerEndpoint:
+ _objc_msgSend$didUsePasswordForUserName:appID:
+ _objc_msgSend$externalProviderExtensionBundleIdentifier
+ _objc_msgSend$generationEventForStrongPassword:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:
+ _objc_msgSend$importCommit
+ _objc_msgSend$initWithUser:password:serviceIdentifierType:serviceIdentifier:site:creationDate:externalProviderBundleIdentifier:externalProviderExtensionBundleIdentifier:
+ _objc_msgSend$passwordKind
+ _objc_msgSend$passwordManagerResourcesProjectImportCommit
+ _objc_msgSend$passwordManagerResourcesProjectURL
+ _objc_msgSend$providerApplicationBundleIdentifier
+ _objc_msgSend$providerExtensionBundleIdentifier
+ _objc_msgSend$safari_isAppleAccountPasskeyRPID
+ _objc_msgSend$serviceIdentifierType
+ _objc_msgSend$signInEventForAutoFillOfUsername:password:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:
+ _objectdestroy.4Tm
+ _objectdestroy.53Tm
+ _swift_getDynamicType
+ _swift_makeBoxUnique
+ _symbolic $s26AuthenticationServicesCore13ExpiringEvent33_AB7DB26FF9E60E2BE86A540BB3FCF93ALLP
+ _symbolic $s26AuthenticationServicesCore43ASCPrivacySensitiveDebugDescriptionProviderP
+ _symbolic $ss12IdentifiableP
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SDySSSay_____GG 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC010GenerationG0V
+ _symbolic Say_____GSg 26AuthenticationServicesCore21ASCCredentialProviderO
+ _symbolic So11NSExtensionC8provider_SS21containingAppBundleIDSS11displayNamet
+ _symbolic So21ASCCredentialProviderC
+ _symbolic _____ 26AuthenticationServicesCore19ASCPrivacySensitiveV
+ _symbolic _____ 26AuthenticationServicesCore21ASCCredentialProviderO
+ _symbolic _____ 26AuthenticationServicesCore26ASCPasswordGenerationEventC
+ _symbolic _____ 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC010GenerationG0V
+ _symbolic _____ So21ASCCredentialProviderC26AuthenticationServicesCoreE3Box33_201E360AC0331836C3310F408B4E094FLLC
+ _symbolic _____ So34WBSCredentialServiceIdentifierTypeV
+ _symbolic _____Sg 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC010GenerationG0V
+ _symbolic _____Sg 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC0efG0V
+ _symbolic _____SgIeyBy_ 26AuthenticationServicesCore26ASCPasswordGenerationEventC
+ _symbolic ______p 26AuthenticationServicesCore43ASCPrivacySensitiveDebugDescriptionProviderP
+ _symbolic ______pSg 26AuthenticationServicesCore43ASCPrivacySensitiveDebugDescriptionProviderP
+ _symbolic _____ySSG 26AuthenticationServicesCore19ASCPrivacySensitiveV
+ _symbolic _____ySSSay_____GG s18_DictionaryStorageC 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC010GenerationI0V
+ _symbolic _____ySSSgG 26AuthenticationServicesCore19ASCPrivacySensitiveV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 26AuthenticationServicesCore21ASCCredentialProviderO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 26AuthenticationServicesCore30ASPasswordSignInEventCollectorC010GenerationJ0V
+ _type_layout_string 26AuthenticationServicesCore21ASCCredentialProviderO
- -[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:].cold.1
- -[ASCAuthorizationPresenter userSelectedImportingDestinationWithBundleIdentfier:]
- -[ASCAuthorizationPresenter userSelectedImportingDestinationWithBundleIdentfier:].cold.1
- -[ASCPasswordCredential initWithUser:password:site:creationDate:externalProviderBundleIdentifier:]
- GCC_except_table10
- _WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent
- _WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent.cold.1
- _WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent.log
- _WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent.onceToken
- _WBS_LOG_CHANNEL_PREFIXAuthorization
- _WBS_LOG_CHANNEL_PREFIXAuthorization.cold.1
- _WBS_LOG_CHANNEL_PREFIXAuthorization.log
- _WBS_LOG_CHANNEL_PREFIXAuthorization.onceToken
- _WBS_LOG_CHANNEL_PREFIXServiceLifecycle
- _WBS_LOG_CHANNEL_PREFIXServiceLifecycle.cold.1
- _WBS_LOG_CHANNEL_PREFIXServiceLifecycle.log
- _WBS_LOG_CHANNEL_PREFIXServiceLifecycle.onceToken
- __PROTOCOLS__TtC26AuthenticationServicesCore38ASCPasskeyAccountRegistrationUserState.26
- __PROTOCOLS__TtC26AuthenticationServicesCore49ASCPublicKeyCredentialRegistrationExtensionInputs.59
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.431
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.464
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.469
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.469.cold.1
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.471
- ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.356
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.450
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.450.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.451
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.452
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.456
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.456.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.453
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.453.cold.1
- ___87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.435
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.360
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.360.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.372
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.378
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.378.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.382
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.382.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.386
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.386.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.392
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.392.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.399
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.399.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.400
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.400.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.415
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.415.cold.1
- ___WBS_LOG_CHANNEL_PREFIXAuthenticationServicesAgent_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXAuthorization_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXServiceLifecycle_block_invoke
- ___block_literal_global.10
- ___block_literal_global.316
- ___block_literal_global.337
- ___block_literal_global.355
- ___block_literal_global.362
- ___block_literal_global.374
- ___block_literal_global.388
- ___block_literal_global.398
- ___block_literal_global.4
- ___block_literal_global.402
- ___block_literal_global.411
- ___block_literal_global.422
- ___block_literal_global.430
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.449
- ___block_literal_global.455
- ___block_literal_global.460
- ___block_literal_global.466
- ___block_literal_global.473
- ___block_literal_global.477
- ___block_literal_global.699
- _block_copy_helper.4
- _block_descriptor.6
- _block_destroy_helper.5
- _keypath_get.13Tm
- _keypath_get.7Tm
- _objc_msgSend$didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:
- _objc_msgSend$didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:
- _objc_msgSend$initWithUser:password:site:creationDate:externalProviderBundleIdentifier:
- _objc_msgSend$providerBundleIdentifier
- _os_log_create
- _symbolic SaySSSgGSg
- _symbolic So11NSExtensionCSg
- _symbolic _____ySSSgG s23_ContiguousArrayStorageC
CStrings:
+ "$__lazy_storage_$_sortedCredentialProviders"
+ ".thirdParty(extensionBundleID: "
+ "@80@0:8@16@24q32@40@48@56@64@72"
+ "AuthenticationServicesCore.ASCCredentialProviderObject"
+ "AuthenticationServicesCore.ASCPasswordGenerationEvent"
+ "T@\"NSExtension\",N,R"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_externalProviderExtensionBundleIdentifier"
+ "T@\"NSString\",R,N,V_serviceIdentifier"
+ "Tq,R,N,V_serviceIdentifierType"
+ "_TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent"
+ "_TtCE26AuthenticationServicesCoreCSo21ASCCredentialProviderP33_201E360AC0331836C3310F408B4E094F3Box"
+ "_externalProviderExtensionBundleIdentifier"
+ "_serviceIdentifier"
+ "_serviceIdentifierType"
+ "_value"
+ "absoluteString"
+ "applicationBundleID"
+ "bundleIdentifierToGenerationEvents"
+ "commits"
+ "credentialProviderInformationForAutoFillOfUsername:password:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:"
+ "credentialProviderInformationForGenerationOfStrongPassword:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:"
+ "didFillCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:listenerEndpoint:"
+ "didGenerateStrongPassword:passwordKind:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:"
+ "didUseCredentialForUsername:password:serviceIdentifierType:serviceIdentifier:providerApplicationBundleIdentifier:providerExtensionBundleIdentifier:hostApplicationBundleIdentifier:listenerEndpoint:"
+ "didUsePasswordForUserName:appID:"
+ "extensionBundleID"
+ "externalExtension"
+ "externalExtensionBundleID"
+ "externalProviderExtensionBundleIdentifier"
+ "generationEventForStrongPassword:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:"
+ "https://github.com/apple/password-manager-resources"
+ "importCommit"
+ "initForExternalProviderWithExtension:applicationBundleID:displayName:"
+ "initForPasswordsApp"
+ "initWithUser:password:serviceIdentifierType:serviceIdentifier:site:creationDate:externalProviderBundleIdentifier:externalProviderExtensionBundleIdentifier:"
+ "passwordKind"
+ "passwordManagerResourcesProjectImportCommit"
+ "passwordManagerResourcesProjectImportCommitURL"
+ "passwordManagerResourcesProjectURL"
+ "providerApplicationBundleIdentifier"
+ "providerExtensionBundleIdentifier"
+ "safari_isAppleAccountPasskeyRPID"
+ "serviceIdentifierType"
+ "signInEventForAutoFillOfUsername:password:serviceIdentifierType:serviceIdentifier:hostApplicationBundleIdentifier:completionHandler:"
+ "userDidSelectImportingDestinationWithApplicationIdentifier:"
+ "v16@?0@\"_TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent\"8"
+ "v56@0:8@\"NSString\"16q24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSString\"@\"NSString\"@\"NSString\">48"
+ "v56@0:8@\"NSString\"16q24@\"NSString\"32@\"NSString\"40@?<v@?@\"_TtC26AuthenticationServicesCore26ASCPasswordGenerationEvent\">48"
+ "v56@0:8@16q24@32@40@?48"
+ "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSString\"@\"NSString\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"NSString\"48@?<v@?@\"_TtC26AuthenticationServicesCore22ASCPasswordSignInEvent\">56"
+ "v64@0:8@16@24q32@40@48@?56"
+ "v72@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64"
+ "v72@0:8@16@24q32@40@48@56@64"
+ "v80@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSXPCListenerEndpoint\"72"
+ "v80@0:8@16@24q32@40@48@56@64@72"
- "$__lazy_storage_$_sortedCredentialProviderIdentifiers"
- "-[ASAgentAutoFillListener didFillCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:]"
- "Nil URL passed to %s"
- "ServiceLifecycle"
- "apple.com"
- "didUseCredentialForUsername:forHost:fromProviderWithBundleIdentifier:inAppWithBundleIdentifier:listenerEndpoint:"
- "didUseCredentialForUsername:forURL:fromProviderWithBundleIdentifier:inBrowserWithBundleIdentifier:listenerEndpoint:"
- "initWithUser:password:site:creationDate:externalProviderBundleIdentifier:"
- "userSelectedImportingDestinationWithBundleIdentfier:"

```
