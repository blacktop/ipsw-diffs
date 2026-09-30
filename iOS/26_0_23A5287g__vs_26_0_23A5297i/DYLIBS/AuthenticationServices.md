## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-622.1.18.10.3
-  __TEXT.__text: 0xe0ae4
-  __TEXT.__auth_stubs: 0x22c0
-  __TEXT.__objc_methlist: 0x756c
-  __TEXT.__const: 0xde44
-  __TEXT.__gcc_except_tab: 0x13d8
-  __TEXT.__cstring: 0x9646
-  __TEXT.__oslogstring: 0x2f97
+622.1.19.10.4
+  __TEXT.__text: 0xe9454
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_methlist: 0x758c
+  __TEXT.__const: 0xec64
+  __TEXT.__gcc_except_tab: 0x13f4
+  __TEXT.__cstring: 0xb3a6
+  __TEXT.__oslogstring: 0x2ee7
   __TEXT.__dlopen_cstrs: 0x308
-  __TEXT.__ustring: 0x6ee0
-  __TEXT.__constg_swiftt: 0x1460
-  __TEXT.__swift5_typeref: 0x1c78
-  __TEXT.__swift5_reflstr: 0x1243
-  __TEXT.__swift5_fieldmd: 0x202c
-  __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__swift5_proto: 0x64c
-  __TEXT.__swift5_types: 0x208
+  __TEXT.__ustring: 0x6d1c
+  __TEXT.__constg_swiftt: 0x14d8
+  __TEXT.__swift5_typeref: 0x1de0
+  __TEXT.__swift5_reflstr: 0x1333
+  __TEXT.__swift5_fieldmd: 0x218c
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_assocty: 0x5e8
+  __TEXT.__swift5_proto: 0x69c
+  __TEXT.__swift5_types: 0x218
   __TEXT.__swift5_capture: 0x5b0
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf8
-  __TEXT.__swift5_mpenum: 0x88
+  __TEXT.__swift5_mpenum: 0x90
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x3fa8
-  __TEXT.__eh_frame: 0x3018
-  __TEXT.__objc_classname: 0x1f9d
-  __TEXT.__objc_methname: 0x1608b
-  __TEXT.__objc_methtype: 0x4097
-  __TEXT.__objc_stubs: 0xd340
+  __TEXT.__unwind_info: 0x4118
+  __TEXT.__eh_frame: 0x31b0
+  __TEXT.__objc_classname: 0x1f9f
+  __TEXT.__objc_methname: 0x16235
+  __TEXT.__objc_methtype: 0x40e7
+  __TEXT.__objc_stubs: 0xd200
   __DATA_CONST.__got: 0xe40
-  __DATA_CONST.__const: 0x1ac8
+  __DATA_CONST.__const: 0x1aa8
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48b8
+  __DATA_CONST.__objc_selrefs: 0x48e8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x1178
-  __AUTH_CONST.__const: 0x5c38
-  __AUTH_CONST.__cfstring: 0x44c0
-  __AUTH_CONST.__objc_const: 0xe5a8
+  __AUTH_CONST.__auth_got: 0x11a8
+  __AUTH_CONST.__const: 0x5ee0
+  __AUTH_CONST.__cfstring: 0x4560
+  __AUTH_CONST.__objc_const: 0xe618
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x3440
-  __AUTH.__data: 0xea0
-  __DATA.__objc_ivar: 0x6d4
-  __DATA.__data: 0x29e0
-  __DATA.__bss: 0xba90
+  __AUTH.__data: 0xe90
+  __DATA.__objc_ivar: 0x6e0
+  __DATA.__data: 0x2ac8
+  __DATA.__bss: 0xc490
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A72FEA61-627B-342D-965F-61098CA162AE
-  Functions: 5786
-  Symbols:   10524
-  CStrings:  5265
+  UUID: B7F1A2D0-DA37-3C30-81BF-CF9A192ED7E9
+  Functions: 5916
+  Symbols:   10548
+  CStrings:  5369
 
Symbols:
+ +[ASCredentialRequestSecurityKeyStringUtilities _basicAssertionMessageTextWithServiceName:serviceType:]
+ +[ASCredentialRequestSecurityKeyStringUtilities _multipleAllowedSecurityKeysMessageTextWithServiceName:serviceType:]
+ +[ASCredentialRequestSecurityKeyStringUtilities _registerSecurityKeyMessageTextWithServiceName:serviceType:]
+ +[ASCredentialRequestSecurityKeyStringUtilities messageWithMode:serviceName:serviceType:]
+ -[ASCredentialRequestCABLEAuthenticatingViewController initWithServiceName:serviceType:isRegistrationRequest:]
+ -[ASCredentialRequestCABLEClientViewController _subtitleText]
+ -[ASCredentialRequestCABLEClientViewController initWithMode:serviceName:serviceType:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:]
+ -[ASCredentialRequestCABLEClientViewController initWithMode:serviceName:serviceType:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:]
+ -[ASCredentialRequestConfirmButtonSubPane _authorizeAccountViaDelegationWithPasswordButtonSelected:]
+ -[ASCredentialRequestConfirmButtonSubPane setAuthorizationCapabilityEnabled:forLoginChoice:]
+ -[ASCredentialRequestConfirmButtonSubPane showContinueWithPasswordButtonWithTitle:]
+ -[ASCredentialRequestPaneViewController _cancelButtonSelected:]
+ -[ASCredentialRequestPaneViewController cancelBarButtonItem]
+ -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:serviceType:overrideTitle:overrideSubtitle:]
+ -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:serviceType:presentingError:]
+ -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:serviceType:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:]
+ -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:serviceType:reinsertSecurityKey:]
+ -[_ASAgentPeriodicMaintenanceActivity initRegisteringActivityHandler:]
+ -[_ASPasswordManagerIconController bundleIDForDomain:completionHandler:]
+ -[_ASPasswordManagerIconController fetchAppIconForDomain:responseHandler:]
+ -[_ASPasswordManagerIconController initWithAllowNetworkFetchingBlock:]
+ -[_ASPasswordManagerIconController initWithAllowNetworkFetchingBlock:].cold.1
+ -[_ASPasswordManagerIconController initWithMetadataManager:allowNetworkFetchingBlock:]
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table60
+ _CGFloatNearlyEqualToFloat
+ _OBJC_IVAR_$_ASCredentialRequestCABLEClientViewController._serviceType
+ _OBJC_IVAR_$_ASCredentialRequestConfirmButtonSubPane._lastAuthenticationViewVisibility
+ _OBJC_IVAR_$__ASPasswordManagerIconController._allowNetworkFetchingBlock
+ ___40-[_ASPasswordManagerIconController init]_block_invoke
+ ___68-[_ASPasswordManagerIconController prepareForApplicationTermination]_block_invoke.31
+ ___72-[_ASPasswordManagerIconController bundleIDForDomain:completionHandler:]_block_invoke
+ ___72-[_ASPasswordManagerIconController bundleIDForDomain:completionHandler:]_block_invoke_2
+ ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke.7
+ ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_2.9
+ ___74-[_ASPasswordManagerIconController fetchAppIconForDomain:responseHandler:]_block_invoke
+ ___74-[_ASPasswordManagerIconController fetchAppIconForDomain:responseHandler:]_block_invoke_2
+ ___74-[_ASPasswordManagerIconController fetchAppIconForDomain:responseHandler:]_block_invoke_2.cold.1
+ ___74-[_ASPasswordManagerIconController fetchAppIconForDomain:responseHandler:]_block_invoke_2.cold.2
+ ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.47
+ ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.47.cold.1
+ ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.51
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.91
+ ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.94
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.36
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.37
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.38
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.38.cold.1
+ ___block_descriptor_32_e5_B8?0l
+ ___block_literal_global.19
+ ___block_literal_global.298
+ ___block_literal_global.46
+ ___block_literal_global.49
+ ___block_literal_global.78
+ ___block_literal_global.93
+ ___swift_get_extra_inhabitant_index.88Tm
+ ___swift_memcpy392_8
+ ___swift_memcpy42_8
+ ___swift_memcpy57_8
+ ___swift_memcpy72_8
+ ___swift_store_extra_inhabitant_index.89Tm
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysOSHAASQ
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysOs0G3KeyAAs0E17StringConvertible
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysOs0G3KeyAAs0E22DebugStringConvertible
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO12CustomFieldsVSHAASQ
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLOSHAASQ
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 22AuthenticationServices22ASImportableCredentialO13ItemReferenceVSHAASQ
+ _associated conformance 22AuthenticationServices24ASAuthorizationUIContextV8IconTypeO10BiometricsOs12CaseIterableAA8AllCasessAHP_Sl
+ _associated conformance So46ASCAuthorizationPresentationContextServiceTypeVSHSCSQ
+ _objc_msgSend$_basicAssertionMessageTextWithServiceName:serviceType:
+ _objc_msgSend$_multipleAllowedSecurityKeysMessageTextWithServiceName:serviceType:
+ _objc_msgSend$_registerSecurityKeyMessageTextWithServiceName:serviceType:
+ _objc_msgSend$_setSectionContentInset:
+ _objc_msgSend$fetchAppIconForDomain:responseHandler:
+ _objc_msgSend$initWithAllowNetworkFetchingBlock:
+ _objc_msgSend$initWithMetadataManager:allowNetworkFetchingBlock:
+ _objc_msgSend$initWithMode:serviceName:serviceType:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:
+ _objc_msgSend$initWithPreferredIcon:mode:serviceName:serviceType:overrideTitle:overrideSubtitle:
+ _objc_msgSend$initWithPreferredIcon:mode:serviceName:serviceType:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:
+ _objc_msgSend$initWithServiceName:serviceType:isRegistrationRequest:
+ _objc_msgSend$isNetworkFetchingForPasswordsEnabled
+ _objc_msgSend$messageWithMode:serviceName:serviceType:
+ _objc_msgSend$safari_boolForKey:defaultValue:
+ _objc_msgSend$serviceType
+ _objc_retain_x28
+ _swift_release_n
+ _symbolic SS11serviceName______0A4TypeSS4siteSSSg019proxiedOriginDeviceB0t So46ASCAuthorizationPresentationContextServiceTypeV
+ _symbolic Say_____G 22AuthenticationServices24ASAuthorizationUIContextV8IconTypeO10BiometricsO
+ _symbolic Say_____G 22AuthenticationServices25ASImportableEditableFieldV
+ _symbolic Sb16selectedFromList_t
+ _symbolic _____ 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV
+ _symbolic _____ 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysO
+ _symbolic _____ 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV
+ _symbolic _____ 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLO
+ _symbolic _____ So46ASCAuthorizationPresentationContextServiceTypeV
+ _symbolic _____17passkeyParameters_SS12providerNameSb10isExternalt 22AuthenticationServices24ASAuthorizationUIContextV24PasskeyMessageParametersV
+ _symbolic _____17passkeyParameters_SSSg12providerNamet 22AuthenticationServices24ASAuthorizationUIContextV24PasskeyMessageParametersV
+ _symbolic _____7service_SS12providerName_____8biometryt 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV
+ _symbolic _____7service_SS16originDeviceNameSSSg08providerD0t 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
+ _symbolic _____7service_SS8usernameSSSg12creationDateAD12providerNamet 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
+ _symbolic _____7service______8biometryt 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV
+ _symbolic _____7service_t 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
+ _symbolic _____Sg_ABt So55ASPasswordAuthenticationPaneViewControllerConfigurationC0B8ServicesE13ContentFields33_4AD42645A6C55D1DE304DC57F60A33AALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV10CodingKeys33_CA4A76CC3A0F7944655FAD38FECCC931LLO
+ _type_layout_string 22AuthenticationServices22ASImportableCredentialO10CreditCardV
+ _type_layout_string 22AuthenticationServices22ASImportableCredentialO12CustomFieldsV
+ _type_layout_string 22AuthenticationServices22ASImportableCredentialO13ItemReferenceV
- +[ASCredentialRequestIconGenerator _providerIconForPasswordLoginChoice:]
- +[ASCredentialRequestIconGenerator iconForPasswordLoginChoice:presentationContext:]
- +[ASCredentialRequestIconGenerator iconForPublicKeyCredentialLoginChoiceWithPresentationContext:]
- +[ASCredentialRequestSecurityKeyStringUtilities _basicAssertionMessageTextWithServiceName:]
- +[ASCredentialRequestSecurityKeyStringUtilities _multipleAllowedSecurityKeysMessageTextWithServiceName:]
- +[ASCredentialRequestSecurityKeyStringUtilities _registerSecurityKeyMessageTextWithServiceName:]
- +[ASCredentialRequestSecurityKeyStringUtilities messageWithMode:serviceName:]
- -[ASCredentialRequestCABLEAuthenticatingViewController initWithServiceName:isRegistrationRequest:]
- -[ASCredentialRequestCABLEClientViewController initWithMode:serviceName:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:]
- -[ASCredentialRequestCABLEClientViewController initWithMode:serviceName:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:]
- -[ASCredentialRequestConfirmButtonSubPane _authorizeAppleAccountWithPasswordButtonSelected:]
- -[ASCredentialRequestConfirmButtonSubPane _passwordAuthenticationButtonTitle]
- -[ASCredentialRequestConfirmButtonSubPane _switchToAppleAccountPassword]
- -[ASCredentialRequestConfirmButtonSubPane setAuthorizationCapabilityEnabled:]
- -[ASCredentialRequestConfirmButtonSubPane showContinueWithPasswordButton]
- -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:overrideTitle:overrideSubtitle:]
- -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:presentingError:]
- -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:]
- -[ASCredentialRequestSecurityKeyViewController initWithPreferredIcon:mode:serviceName:reinsertSecurityKey:]
- -[_ASAgentPeriodicMaintenanceActivity init]
- -[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]
- -[_ASPasswordManagerIconController initWithMetadataManager:]
- -[_ASPasswordManagerIconController init].cold.1
- GCC_except_table47
- GCC_except_table48
- GCC_except_table50
- GCC_except_table58
- ___48-[ASCredentialRequestButtonContinue _commonInit]_block_invoke
- ___52-[ASCredentialRequestPaneViewController viewDidLoad]_block_invoke
- ___68-[_ASPasswordManagerIconController prepareForApplicationTermination]_block_invoke.28
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke.5
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_2.7
- ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.53
- ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.53.cold.1
- ___75-[ASCredentialRequestCABLEClientViewController _useSecurityKeyButtonTapped]_block_invoke.57
- ___75-[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]_block_invoke
- ___75-[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]_block_invoke_2
- ___75-[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]_block_invoke_2.cold.1
- ___75-[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]_block_invoke_2.cold.2
- ___75-[_ASPasswordManagerIconController _fetchAppIconForDomain:responseHandler:]_block_invoke_2.cold.3
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.89
- ___78-[ASCredentialRequestConfirmButtonSubPane authenticationResult:error:context:]_block_invoke.92
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.33
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.34
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.35
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.35.cold.1
- ___block_descriptor_40_e8_32s_e24_v16?0"NSMutableArray"8ls32l8
- ___block_literal_global.297
- ___block_literal_global.50
- ___block_literal_global.52
- ___block_literal_global.55
- ___block_literal_global.60
- ___block_literal_global.76
- ___block_literal_global.91
- ___swift_get_extra_inhabitant_index.87Tm
- ___swift_memcpy41_8
- ___swift_store_extra_inhabitant_index.88Tm
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_AuthenticationServices
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_AuthenticationServices
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_AuthenticationServices
- _associated conformance So17ASLoginChoiceKindVSHSCSQ
- _objc_msgSend$_basicAssertionMessageTextWithServiceName:
- _objc_msgSend$_fetchAppIconForDomain:responseHandler:
- _objc_msgSend$_iconForPasswordProviderBundleIdentifier:
- _objc_msgSend$_multipleAllowedSecurityKeysMessageTextWithServiceName:
- _objc_msgSend$_passwordAuthenticationButtonTitle
- _objc_msgSend$_providerIconForPasswordLoginChoice:
- _objc_msgSend$_registerSecurityKeyMessageTextWithServiceName:
- _objc_msgSend$_switchToAppleAccountPassword
- _objc_msgSend$appIdentifier
- _objc_msgSend$constraintLessThanOrEqualToSystemSpacingBelowAnchor:multiplier:
- _objc_msgSend$contentOffset
- _objc_msgSend$doubleValue
- _objc_msgSend$iconForData:scale:size:
- _objc_msgSend$initWithMetadataManager:
- _objc_msgSend$initWithMode:serviceName:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:
- _objc_msgSend$initWithPreferredIcon:mode:serviceName:overrideTitle:overrideSubtitle:
- _objc_msgSend$initWithPreferredIcon:mode:serviceName:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:
- _objc_msgSend$initWithServiceName:isRegistrationRequest:
- _objc_msgSend$isExternal
- _objc_msgSend$isSolariumEnabled
- _objc_msgSend$messageWithMode:serviceName:
- _objc_msgSend$providerBundleIdentifier
- _objc_msgSend$proxiedIconData
- _objc_msgSend$proxiedIconScale
- _objc_msgSend$systemPasswordIcon
- _symbolic SS11serviceName_SS4siteSSSg019proxiedOriginDeviceB0t
- _symbolic _____ So17ASLoginChoiceKindV
- _symbolic _____17passkeyParameters_SS12providerNamet 22AuthenticationServices24ASAuthorizationUIContextV24PasskeyMessageParametersV
- _symbolic _____7service_SS8usernameSSSg12creationDatet 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO
- _symbolic _____7service______8biometrySb19showSaveInPasswordst 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV
- _symbolic _____y_____G s11_SetStorageC So17ASLoginChoiceKindV
- _symbolic _____yyXlG s23_ContiguousArrayStorageC
CStrings:
+ "\tAutoFill from Passwords: %{public}s"
+ "@32@0:8@16Q24"
+ "@36@0:8@16Q24B32"
+ "@36@0:8B16@20@28"
+ "@40@0:8q16@24Q32"
+ "@48@0:8@16@24Q32@40"
+ "@52@0:8q16q24@32Q40B48"
+ "@56@0:8@16@24@32Q40@48"
+ "@56@0:8q16q24@32Q40q48"
+ "@64@0:8@16d24@32@40Q48@56"
+ "@64@0:8q16q24@32Q40@48@56"
+ "@72@0:8q16@24Q32@40q48@56@64"
+ "@80@0:8q16@24Q32@40q48@56@64@72"
+ "@88@0:8q16q24@32Q40q48@56@64@72@80"
+ "Add a credential?"
+ "An account will be created for “%@” with a passkey saved in “%@”."
+ "An account will be created for “%@” with a passkey saved in “%@”. (app)"
+ "An account will be created for “%@” with a passkey saved in “%@”. (website)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID."
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID. (website)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID."
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID. (website)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID."
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID. (website)"
+ "An account will be created for “%@” with a passkey. (app)"
+ "An account will be created for “%@” with a passkey. (website)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID."
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID. (website)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID."
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID. (website)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID."
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID. (app)"
+ "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID. (website)"
+ "B8@?0"
+ "Choose an account to sign in to your “%@” account."
+ "Choose an account to sign in to “%@” on “%@”. (app)"
+ "Choose an account to sign in to “%@” on “%@”. (website)"
+ "Choose how youʼd like to add a passkey for “%@”."
+ "Choose how youʼd like to add a passkey for “%@”. (app)"
+ "Choose how youʼd like to add a passkey for “%@”. (website)"
+ "Choose how you‘d like to add a credential for “%@”."
+ "Choose how you’d like to sign in to your “%@” account."
+ "Do you want to sign in to “%@” on “%@” with your saved password saved in “%@”? (app)"
+ "Do you want to sign in to “%@” on “%@” with your saved password saved in “%@”? (website)"
+ "Do you want to sign in to “%@” with your saved password for “%@” saved in “%@”? (app)"
+ "Do you want to sign in to “%@” with your saved password for “%@” saved in “%@”? (website)"
+ "Enter your user name and password to sign in to “%@” on “%@”. (app)"
+ "Enter your user name and password to sign in to “%@” on “%@”. (website)"
+ "Enter your user name and password to sign in to “%@”. (app)"
+ "Enter your user name and password to sign in to “%@”. (website)"
+ "Passwords (app name)"
+ "Scan QR Code (CABLE title)"
+ "ShouldAttemptPasskeyAvailabilityManagerFetchingInAuthenticationServicesAgent"
+ "Sign Up (Button)"
+ "Sign in to “%@” from “%@” on the other device with your shared passkey for “%@”? (app)"
+ "Sign in to “%@” from “%@” on the other device with your shared passkey for “%@”? (website)"
+ "Sign in to “%@” on the other device with your passkey for “%@” saved in “%@”?"
+ "Sign in to “%@” on the other device with your passkey for “%@” saved in “%@”? (app)"
+ "Sign in to “%@” on the other device with your passkey for “%@” saved in “%@”? (website)"
+ "Sign in to “%@” on the other device with your passkey for “%@”? (app)"
+ "Sign in to “%@” on the other device with your passkey for “%@”? (website)"
+ "Sign in to “%@” on the other device with your saved account? (app)"
+ "Sign in to “%@” on the other device with your saved account? (website)"
+ "Sign in to “%@” on the other device with your shared passkey for “%@” saved in “Passwords”?"
+ "Sign in to “%@” on the other device with your shared passkey for “%@” saved in “Passwords”? (app)"
+ "Sign in to “%@” on the other device with your shared passkey for “%@” saved in “Passwords”? (website)"
+ "Sign in to “%@” on the other device with your shared passkey for “%@”? (app)"
+ "Sign in to “%@” on the other device with your shared passkey for “%@”? (website)"
+ "Sign in to “%@” on “%@” with your passkey for “%@”? (app)"
+ "Sign in to “%@” on “%@” with your passkey for “%@”? (website)"
+ "Sign in to “%@” on “%@” with your password from “%@”? (app)"
+ "Sign in to “%@” on “%@” with your password from “%@”? (website)"
+ "Sign in to “%@” on “%@” with your password saved in “%@”?"
+ "Sign in to “%@” on “%@” with your shared passkey for “%@”? (app)"
+ "Sign in to “%@” on “%@” with your shared passkey for “%@”? (website)"
+ "Sign in to “%@” with your passkey for “%@” saved in “%@”?"
+ "Sign in to “%@” with your passkey for “%@” saved in “%@”? (app)"
+ "Sign in to “%@” with your passkey for “%@” saved in “%@”? (website)"
+ "Sign in to “%@” with your passkey for “%@”? (app)"
+ "Sign in to “%@” with your passkey for “%@”? (website)"
+ "Sign in to “%@” with your password for “%@” saved in “%@”?"
+ "Sign in to “%@” with your saved account? (app)"
+ "Sign in to “%@” with your saved account? (website)"
+ "Sign in to “%@” with your shared passkey for “%@” saved in “Passwords”?"
+ "Sign in to “%@” with your shared passkey for “%@” saved in “Passwords”? (app)"
+ "Sign in to “%@” with your shared passkey for “%@” saved in “Passwords”? (website)"
+ "Sign in to “%@” with your shared passkey for “%@”? (app)"
+ "Sign in to “%@” with your shared passkey for “%@”? (website)"
+ "Sign in with Apple (button accessibility)"
+ "T@\"UIBarButtonItem\",R,N"
+ "The other device will be signed in to “%@” on “%@” with your saved passkey for “%@”. (app)"
+ "The other device will be signed in to “%@” on “%@” with your saved passkey for “%@”. (website)"
+ "Use Selected Passkey"
+ "Use Selected Password"
+ "_allowNetworkFetchingBlock"
+ "_authorizeAccountViaDelegationWithPasswordButtonSelected:"
+ "_basicAssertionMessageTextWithServiceName:serviceType:"
+ "_cancelButtonSelected:"
+ "_lastAuthenticationViewVisibility"
+ "_multipleAllowedSecurityKeysMessageTextWithServiceName:serviceType:"
+ "_registerSecurityKeyMessageTextWithServiceName:serviceType:"
+ "_serviceType"
+ "_setSectionContentInset:"
+ "bundleIDForDomain:completionHandler:"
+ "cancelBarButtonItem"
+ "custom-fields"
+ "externalCredentialIdentity"
+ "fetchAppIconForDomain:responseHandler:"
+ "fields"
+ "initRegisteringActivityHandler:"
+ "initWithAllowNetworkFetchingBlock:"
+ "initWithFirst:second:"
+ "initWithIsSupported:first:second:"
+ "initWithManualPasswordEntryForCredentialProviderWithApplicationBundleID:site:serviceName:serviceType:proxiedOriginDeviceName:"
+ "initWithManualPasswordEntryForCredentialProviderWithProxiedIconData:proxiedIconScale:site:serviceName:serviceType:proxiedOriginDeviceName:"
+ "initWithManualPasswordEntryForPasswordManagerWithSite:serviceName:serviceType:proxiedOriginDeviceName:"
+ "initWithMetadataManager:allowNetworkFetchingBlock:"
+ "initWithMode:serviceName:serviceType:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:"
+ "initWithMode:serviceName:serviceType:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:"
+ "initWithPreferredIcon:mode:serviceName:serviceType:overrideTitle:overrideSubtitle:"
+ "initWithPreferredIcon:mode:serviceName:serviceType:presentingError:"
+ "initWithPreferredIcon:mode:serviceName:serviceType:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:"
+ "initWithPreferredIcon:mode:serviceName:serviceType:reinsertSecurityKey:"
+ "initWithServiceName:serviceType:isRegistrationRequest:"
+ "isNetworkFetchingForPasswordsEnabled"
+ "item-reference"
+ "localizedCredentialProviderName"
+ "localizedDisplayName"
+ "messageWithMode:serviceName:serviceType:"
+ "numberOfAutoFillProvidersEnabled"
+ "passkeyParameters providerName isExternal "
+ "safari_boolForKey:defaultValue:"
+ "service biometry "
+ "service providerName biometry "
+ "setAuthorizationCapabilityEnabled:forLoginChoice:"
+ "showContinueWithPasswordButtonWithTitle:"
+ "v28@0:8B16Q20"
+ "v40@0:8q16B24B28@32"
+ "year-month"
+ "\xe1"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen."
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. (app)"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. (website)"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”."
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”. (app)"
+ "“%@” supports passkeys, a stronger alternative to passwords that cannot be leaked or stolen. Your passkey will be saved in “%@”. (website)"
+ "\xf0!"
- "\tiCloud Keychain AutoFill: %{public}s"
- "@44@0:8q16q24@32B40"
- "@48@0:8q16q24@32q40"
- "@56@0:8@16d24@32@40@48"
- "@56@0:8q16q24@32@40@48"
- "@64@0:8q16@24@32q40@48@56"
- "@72@0:8q16@24@32q40@48@56@64"
- "@80@0:8q16q24@32q40@48@56@64@72"
- "A passkey for “%@” will be saved and available on devices where “%@” is installed."
- "A passkey for “%@” will be saved in Passwords and available on all your devices."
- "An account will be created for “%@” with a passkey saved in Passwords."
- "An account will be created for “%@” with a passkey saved in Passwords. You can sign into this account with Face\u00a0ID."
- "An account will be created for “%@” with a passkey saved in Passwords. You can sign into this account with Optic\u00a0ID."
- "An account will be created for “%@” with a passkey saved in Passwords. You can sign into this account with Touch\u00a0ID."
- "App does not exist for domain; domain=%{sensitive, mask.hash}@"
- "Application identifier for retrieving icon did not match expected format; domain=%{sensitive, mask.hash}@"
- "Choose an account to sign in to “%@”."
- "Choose how you’d like to sign in to “%@”."
- "Choose where to save a passkey for “%@”."
- "Create a passkey?"
- "Sign up with a passkey?"
- "_authorizeAppleAccountWithPasswordButtonSelected:"
- "_basicAssertionMessageTextWithServiceName:"
- "_fetchAppIconForDomain:responseHandler:"
- "_multipleAllowedSecurityKeysMessageTextWithServiceName:"
- "_passwordAuthenticationButtonTitle"
- "_providerIconForPasswordLoginChoice:"
- "_registerSecurityKeyMessageTextWithServiceName:"
- "_switchToAppleAccountPassword"
- "constraintLessThanOrEqualToSystemSpacingBelowAnchor:multiplier:"
- "contentOffset"
- "iconForPasswordLoginChoice:presentationContext:"
- "iconForPublicKeyCredentialLoginChoiceWithPresentationContext:"
- "initWithManualPasswordEntryForCredentialProviderWithApplicationBundleID:site:serviceName:proxiedOriginDeviceName:"
- "initWithManualPasswordEntryForCredentialProviderWithProxiedIconData:proxiedIconScale:site:serviceName:proxiedOriginDeviceName:"
- "initWithManualPasswordEntryForPasswordManagerWithSite:serviceName:proxiedOriginDeviceName:"
- "initWithMetadataManager:"
- "initWithMode:serviceName:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:"
- "initWithMode:serviceName:destinationSiteForCrossSiteAssertion:cableAuthenticatorRequirement:loginChoice:securityKeyLoginChoice:activity:"
- "initWithPreferredIcon:mode:serviceName:overrideTitle:overrideSubtitle:"
- "initWithPreferredIcon:mode:serviceName:presentingError:"
- "initWithPreferredIcon:mode:serviceName:presentingError:overrideTitle:overrideSubtitle:overrideNoCredentialsErrorTitle:overrideNoCredentialsErrorMessage:"
- "initWithPreferredIcon:mode:serviceName:reinsertSecurityKey:"
- "initWithServiceName:isRegistrationRequest:"
- "isSolariumEnabled"
- "messageWithMode:serviceName:"
- "service biometry showSaveInPasswords "
- "setAuthorizationCapabilityEnabled:"
- "showContinueWithPasswordButton"
- "v16@?0@\"NSMutableArray\"8"
- "v36@0:8B16B20B24@28"
- "\xd1"

```
