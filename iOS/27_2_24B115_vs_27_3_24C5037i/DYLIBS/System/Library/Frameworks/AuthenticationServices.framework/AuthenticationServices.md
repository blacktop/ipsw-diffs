## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-625.2.8.10.6
-  __TEXT.__text: 0x138d90
-  __TEXT.__objc_methlist: 0x809c
-  __TEXT.__cstring: 0xb5a8
-  __TEXT.__const: 0x13ef4
-  __TEXT.__gcc_except_tab: 0x1220
-  __TEXT.__oslogstring: 0x357b
+626.1.12.10.3
+  __TEXT.__text: 0x142354
+  __TEXT.__objc_methlist: 0x82d0
+  __TEXT.__cstring: 0xb708
+  __TEXT.__const: 0x14484
+  __TEXT.__gcc_except_tab: 0x13a4
+  __TEXT.__oslogstring: 0x393b
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d36
-  __TEXT.__swift5_typeref: 0x324e
-  __TEXT.__constg_swiftt: 0x22b4
-  __TEXT.__swift5_reflstr: 0x1d5c
-  __TEXT.__swift5_fieldmd: 0x2f10
-  __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_assocty: 0x7c0
-  __TEXT.__swift5_proto: 0x9bc
-  __TEXT.__swift5_types: 0x354
+  __TEXT.__swift5_typeref: 0x3662
+  __TEXT.__swift5_fieldmd: 0x3064
+  __TEXT.__constg_swiftt: 0x23e8
+  __TEXT.__swift5_reflstr: 0x1edc
+  __TEXT.__swift5_builtin: 0x26c
+  __TEXT.__swift5_assocty: 0x838
+  __TEXT.__swift5_proto: 0x9ec
+  __TEXT.__swift5_types: 0x370
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_capture: 0xde8
-  __TEXT.__swift_as_entry: 0x248
-  __TEXT.__swift_as_ret: 0x2d4
-  __TEXT.__swift_as_cont: 0x508
+  __TEXT.__swift5_capture: 0xed8
+  __TEXT.__swift_as_entry: 0x278
+  __TEXT.__swift_as_ret: 0x320
+  __TEXT.__swift_as_cont: 0x58c
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__unwind_info: 0x7088
-  __TEXT.__eh_frame: 0x6e3c
+  __TEXT.__unwind_info: 0x7478
+  __TEXT.__eh_frame: 0x7740
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a40
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x2c8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d00
-  __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x4ee0
+  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1090
-  __AUTH_CONST.__const: 0x9a98
-  __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x10190
+  __DATA_CONST.__got: 0x1118
+  __AUTH_CONST.__const: 0xa010
+  __AUTH_CONST.__cfstring: 0x4620
+  __AUTH_CONST.__objc_const: 0x106a0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x1680
-  __AUTH.__objc_data: 0x39d8
-  __AUTH.__data: 0x18d0
-  __DATA.__objc_ivar: 0x708
-  __DATA.__data: 0x38d0
+  __AUTH_CONST.__auth_got: 0x1720
+  __AUTH.__objc_data: 0x39e0
+  __AUTH.__data: 0x1aa8
+  __DATA.__objc_ivar: 0x724
+  __DATA.__data: 0x3b48
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x560
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8194
-  Symbols:   6529
-  CStrings:  1355
+  Functions: 8443
+  Symbols:   6663
+  CStrings:  1377
 
Symbols:
+ +[ASViewServiceInterfaceUtilities floatingSheetWidth]
+ +[_ASPasswordManagerDeleteAlertConfiguration _canUseSingleItemConfigurationWithAccountsSelectionInfo:]
+ +[_ASPasswordManagerDeleteAlertConfiguration _namesOfWiFiNetworks:]
+ +[_ASPasswordManagerDeleteAlertConfiguration _shouldUseWLANTerminologyInsteadOfWiFi]
+ +[_ASPasswordManagerDeleteAlertConfiguration _titleStringForAlertToDeleteMixedItemsIsPermanentlyDeleting:]
+ +[_ASPasswordManagerDeleteAlertConfiguration _wiFiOnlySubtitleStringWithAccountsSelectionInfo:]
+ +[_ASPasswordManagerDeleteAlertConfiguration _wiFiSubtitleStringWithAccountsSelectionInfo:]
+ +[_ASPasswordManagerDeleteAlertConfiguration configurationForDeletingSavedAccounts:wiFiNetworks:]
+ -[ASCredentialRequestCABLEConnectingViewController contentContributesToPaneHeight]
+ -[ASCredentialRequestConfirmButtonSubPane _biometricsViewActiveAppearanceDidChange]
+ -[ASCredentialRequestConfirmButtonSubPane setUpButtonWithTitle:]
+ -[ASCredentialRequestPaneViewController contentContributesToPaneHeight]
+ -[ASCredentialRequestPaneViewController shouldEmbedPaneContentInScrollView]
+ -[ASPasskeyCredentialRequest initWithCredentialIdentity:requestType:clientDataHash:userVerificationPreference:supportedAlgorithms:]
+ -[_ASAgentCredentialExchangeListener _connection:ownsOperation:]
+ -[_ASAgentCredentialExchangeListener _performWithLockIfOperationIsCurrent:block:]
+ -[_ASAgentCredentialExchangeListener _terminateOperationIfCurrent:]
+ -[_ASAgentCredentialExchangeListener beginSceneHostingForApplicationIdentifier:fromEndpoint:flow:]
+ -[_ASAgentCredentialExchangeListener requestExportForCredentialProvider:completionHandler:]
+ -[_ASAgentCredentialExchangeListener sceneHostedUIDidSelectImporterApplicationIdentifier:completionHandler:]
+ -[_ASAgentCredentialExchangeListenerProxy requestExportForCredentialProvider:completionHandler:]
+ -[_ASAgentCredentialExchangeOperation endpointPresenter]
+ -[_ASAgentCredentialExchangeOperation setEndpointPresenter:]
+ -[_ASAgentCredentialExchangeOperation setViewServiceListener:]
+ -[_ASAgentCredentialExchangeOperation viewServiceListener]
+ -[_ASConditionalRegistrationRequester init]
+ -[_ASPasswordManagerAccountsSelectionInfo .cxx_destruct]
+ -[_ASPasswordManagerAccountsSelectionInfo accounts]
+ -[_ASPasswordManagerAccountsSelectionInfo hasWiFiNetworks]
+ -[_ASPasswordManagerAccountsSelectionInfo initWithSavedAccounts:wiFiNetworks:]
+ -[_ASPasswordManagerAccountsSelectionInfo managedWiFiNetworks]
+ -[_ASPasswordManagerAccountsSelectionInfo wiFiNetworksToForget]
+ -[_ASPasswordManagerDeleteAlertConfiguration hasIrreversibleConsequences]
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table56
+ GCC_except_table66
+ GCC_except_table77
+ _ASInterfaceForVerificationCodesDeliverySetupDaemonProtocol
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_ASCCredentialServiceIdentifier
+ _OBJC_CLASS_$_ASCEndpointAuthorizationPresenter
+ _OBJC_CLASS_$_ASCVerificationCodesDeliverySetupAccount
+ _OBJC_CLASS_$_UILayoutGuide
+ _OBJC_CLASS_$_UITraitActiveAppearance
+ _OBJC_CLASS_$_WBSWiFiNetworkLocalizedStrings
+ _OBJC_IVAR_$__ASAgentCredentialExchangeOperation._endpointPresenter
+ _OBJC_IVAR_$__ASAgentCredentialExchangeOperation._viewServiceListener
+ _OBJC_IVAR_$__ASConditionalRegistrationRequester._queue
+ _OBJC_IVAR_$__ASPasswordManagerAccountsSelectionInfo._accounts
+ _OBJC_IVAR_$__ASPasswordManagerAccountsSelectionInfo._managedWiFiNetworks
+ _OBJC_IVAR_$__ASPasswordManagerAccountsSelectionInfo._wiFiNetworksToForget
+ _OBJC_IVAR_$__ASPasswordManagerDeleteAlertConfiguration._isForgettingWiFiNetworks
+ __DATA__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E37VerificationCodesDeliverySetupSession
+ __DATA__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E45VerificationCodesDeliverySetupSessionsManager
+ __IVARS__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E37VerificationCodesDeliverySetupSession
+ __IVARS__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E45VerificationCodesDeliverySetupSessionsManager
+ __METACLASS_DATA__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E37VerificationCodesDeliverySetupSession
+ __METACLASS_DATA__TtC22AuthenticationServicesP33_5715F930C8FEF8ACFAE0CBB4BA5B403E45VerificationCodesDeliverySetupSessionsManager
+ __OBJC_$_INSTANCE_METHODS_ASAgentVerificationCodesService(AuthenticationServices|AuthenticationServices1|AuthenticationServices2)
+ __OBJC_$_INSTANCE_METHODS_ASAuthorizationController(SwiftImplementation|AuthenticationServices)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCSceneHostingDaemonProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASCSceneHostingDaemonProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __OBJC_$_PROTOCOL_REFS_ASCCredentialProtocol
+ __OBJC_$_PROTOCOL_REFS_ASCSceneHostingDaemonProtocol
+ __OBJC_$_PROTOCOL_REFS__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __OBJC_CLASS_PROTOCOLS_$_ASAgentVerificationCodesService(AuthenticationServices|AuthenticationServices1|AuthenticationServices2)
+ __OBJC_LABEL_PROTOCOL_$_ASCCredentialProtocol
+ __OBJC_LABEL_PROTOCOL_$_ASCSceneHostingDaemonProtocol
+ __OBJC_LABEL_PROTOCOL_$__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __OBJC_PROTOCOL_$_ASCCredentialProtocol
+ __OBJC_PROTOCOL_$_ASCSceneHostingDaemonProtocol
+ __OBJC_PROTOCOL_$__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __OBJC_PROTOCOL_REFERENCE_$_ASCSceneHostingDaemonProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __PROTOCOL_INSTANCE_METHODS__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __PROTOCOL_PROTOCOLS__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ __PROTOCOL__TtP22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocol_
+ ___103-[_ASConditionalRegistrationRequester requestAutomaticPasskeyUpgradeWithLoginChoice:completionHandler:]_block_invoke
+ ___119-[_ASConditionalRegistrationRequester credentialAuthenticationViewController:didFinishWithCredential:error:completion:]_block_invoke
+ ___138-[_ASConditionalRegistrationRequester credentialAuthenticationViewController:didFinishWithPasskeyRegistrationCredential:error:completion:]_block_invoke
+ ___64-[ASCredentialRequestConfirmButtonSubPane setUpButtonWithTitle:]_block_invoke
+ ___67-[_ASAgentCredentialExchangeListener _terminateOperationIfCurrent:]_block_invoke
+ ___70+[_ASWebsiteNameProvider fetchWebsiteNameForDomain:completionHandler:]_block_invoke_2
+ ___73-[_ASAgentCredentialExchangeListener listener:shouldAcceptNewConnection:]_block_invoke
+ ___73-[_ASAgentCredentialExchangeListener listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___76-[_ASAgentCredentialExchangeListener _setUpImporterConnection:forOperation:]_block_invoke_2
+ ___83-[_ASAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:]_block_invoke
+ ___86-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_3
+ ___96-[_ASAgentCredentialExchangeListenerProxy requestExportForCredentialProvider:completionHandler:]_block_invoke
+ ___96-[_ASAgentCredentialExchangeListenerProxy requestExportForCredentialProvider:completionHandler:]_block_invoke_2
+ ___97+[_ASPasswordManagerDeleteAlertConfiguration configurationForDeletingSavedAccounts:wiFiNetworks:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSTimer"8lw40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0ls32l8s48l8s40l8r56l8r64l8
+ ___block_descriptor_72_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___swift_closure_destructor.110Tm
+ ___swift_closure_destructor.16Tm
+ ___swift_closure_destructor.213Tm
+ ___swift_closure_destructor.28Tm
+ ___swift_closure_destructor.84Tm
+ _associated conformance 22AuthenticationServices35ASDeliveredVerificationCodesManagerC11SetUpReasonOSHAASQ
+ _associated conformance 22AuthenticationServices35ASDeliveredVerificationCodesManagerC21AccountRecordForSetUpV13ContactMethodOSHAASQ
+ _flat unique So21ASCCredentialProtocol_p
+ _keypath_setTm
+ _swift_release_x9
+ _swift_retain_x25
+ _symbolic $s22AuthenticationServices46ASVerificationCodesDeliverySetupDaemonProtocolP
+ _symbolic SaySo40ASCVerificationCodesDeliverySetupAccountCG
+ _symbolic ScCySo21NSXPCListenerEndpointCSg_Sbt______pG s5ErrorP
+ _symbolic SccySSSg_____G s5NeverO
+ _symbolic SccySb______pG s5ErrorP
+ _symbolic SccySo21NSXPCListenerEndpointC______pG s5ErrorP
+ _symbolic SccySo22WBSPasswordSignInEventCSg_____G s5NeverO
+ _symbolic SccySo26WBSPasswordGenerationEventCSg_____G s5NeverO
+ _symbolic So13ASCAgentProxyC
+ _symbolic So13NSXPCListenerC
+ _symbolic So15NSXPCConnectionCSgXw
+ _symbolic So21NSXPCListenerEndpointCSgSb______pSgIeghgyg_ s5ErrorP
+ _symbolic So21NSXPCListenerEndpointCSg_Sbt
+ _symbolic So21NSXPCListenerEndpointCSg_____So7NSErrorCSgIeyBhyyy_ 10ObjectiveC8ObjCBoolV
+ _symbolic So25ASAuthorizationControllerC
+ _symbolic So27ASCCredentialRequestContextC
+ _symbolic So30ASCCredentialServiceIdentifierC
+ _symbolic So31ASAgentVerificationCodesServiceCSgXw
+ _symbolic So31ASAgentVerificationCodesServiceCSgXwz_Xx
+ _symbolic So33ASCEndpointAuthorizationPresenterCSg
+ _symbolic So40ASCVerificationCodesDeliverySetupAccountC
+ _symbolic So40ASCVerificationCodesDeliverySetupAccountCm
+ _symbolic So7NSArrayCm
+ _symbolic So8UIWindowC
+ _symbolic _____ 22AuthenticationServices35ASDeliveredVerificationCodesManagerC11SetUpReasonO
+ _symbolic _____ 22AuthenticationServices35ASDeliveredVerificationCodesManagerC21AccountRecordForSetUpV
+ _symbolic _____ 22AuthenticationServices35ASDeliveredVerificationCodesManagerC21AccountRecordForSetUpV13ContactMethodO
+ _symbolic _____ 22AuthenticationServices37VerificationCodesDeliverySetupSession33_5715F930C8FEF8ACFAE0CBB4BA5B403ELLC
+ _symbolic _____ 22AuthenticationServices45VerificationCodesDeliverySetupSessionsManager33_5715F930C8FEF8ACFAE0CBB4BA5B403ELLC
+ _symbolic _____ So20ASPasswordCredentialC22AuthenticationServicesE10SaveActionV
+ _symbolic _____ So39ASCVerificationCodesDeliverySetupReasonV
+ _symbolic ______pSgSo7NSErrorCSgIeyByy_Sg So21ASCCredentialProtocolP
+ _symbolic _____ySay_____GG 2os21OSAllocatedUnfairLockV 22AuthenticationServices37VerificationCodesDeliverySetupSession33_5715F930C8FEF8ACFAE0CBB4BA5B403ELLC
+ _symbolic _____ySay_____G_____G s13ManagedBufferCsRi__rlE 22AuthenticationServices37VerificationCodesDeliverySetupSession33_5715F930C8FEF8ACFAE0CBB4BA5B403ELLC So16os_unfair_lock_sV
+ _symbolic _____ySo13NSXPCListenerCG 10SafariCore7WBSLazyC
+ _symbolic _____y_____G 10Foundation17KeyPathComparatorV 22AuthenticationServices26ASPasswordSavingModalStateO
+ _symbolic _____y_____G 10SafariCore7WBSLazyC 022AuthenticationServicesB021ASCHideMyEmailManagerC
+ _symbolic _____y_____G s11_SetStorageC s11AnyHashableV
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _type_layout_string 22AuthenticationServices35ASDeliveredVerificationCodesManagerC21AccountRecordForSetUpV
+ _type_layout_string 22AuthenticationServices35ASDeliveredVerificationCodesManagerC21AccountRecordForSetUpV13ContactMethodO
+ _type_layout_string So20ASPasswordCredentialC22AuthenticationServicesE10SaveActionV
- GCC_except_table24
- GCC_except_table35
- GCC_except_table46
- GCC_except_table52
- GCC_except_table65
- GCC_except_table74
- __CLASS_METHODS_ASPasswordSavingManager
- __CLASS_PROPERTIES_ASAuthorizationPublicKeyCredentialPRFRegistrationInput
- __OBJC_$_INSTANCE_METHODS_ASAgentVerificationCodesService(AuthenticationServices)
- __OBJC_$_INSTANCE_METHODS_ASAuthorizationController(SwiftImplementation)
- __OBJC_CLASS_PROTOCOLS_$_ASAgentVerificationCodesService(AuthenticationServices)
- ___80-[ASCredentialRequestConfirmButtonSubPane setUpButtonInPaneContext:buttonTitle:]_block_invoke
- ___84+[_ASPasswordManagerDeleteAlertConfiguration configurationForDeletingSavedAccounts:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSTimer"8ls32l8s40l8
- ___swift_closure_destructor.25Tm
- ___swift_closure_destructor.75Tm
- ___swift_closure_destructor.94Tm
- _swift_deletedAsyncMethodErrorTu
- _symbolic SccySSSg_A2At_____G s5NeverO
- _symbolic SccySSSg_AAt_____G s5NeverO
- _symbolic So5NSURLCSg
- _symbolic _____ 10ObjectiveC8ObjCBoolV
- _symbolic ______pSg 22AuthenticationServices27ASApplicationRecordResolverP
- _symbolic ______pSg 26AuthenticationServicesCore29ASCredentialProvidersProviderP
CStrings:
+ "\n\n"
+ "\v"
+ "%{public}s: Unexpectedly found no registration handler"
+ "-[_ASAgentCredentialExchangeListener beginSceneHostingForApplicationIdentifier:fromEndpoint:flow:]"
+ "-[_ASAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:]_block_invoke"
+ "-[_ASAgentCredentialExchangeListener requestExportForCredentialProvider:completionHandler:]"
+ "-[_ASAgentCredentialExchangeListener sceneHostedUIDidSelectImporterApplicationIdentifier:completionHandler:]"
+ "-[_ASConditionalRegistrationRequester credentialAuthenticationViewController:didFinishWithCredential:error:completion:]"
+ "-[_ASConditionalRegistrationRequester credentialAuthenticationViewController:didFinishWithPasskeyRegistrationCredential:error:completion:]"
+ "AuthenticationServices/ASAuthorizationPublicKeyCredentialPRFExtension.swift"
+ "AuthenticationServices/ASGeneratePasswordsRequest.swift"
+ "AuthenticationServices/ASGeneratedPassword.swift"
+ "AuthenticationServices/ASPasswordAuthenticationPaneViewControllerConfiguration.swift"
+ "AuthenticationServices/ASPasswordSavingManager.swift"
+ "AuthenticationServices/ASPasswordSavingManagerRequest.swift"
+ "AuthenticationServices/ASPasswordSavingModalState.swift"
+ "AuthenticationServices/ASPasswordSavingProvidersState.swift"
+ "AuthenticationServices/ASSavePasswordRequest.swift"
+ "AuthenticationServices/_ASAgentAutomaticSecurityUpgradeListener.swift"
+ "Connection arrived on a verification codes delivery setup endpoint with no presentation behind it"
+ "Could not look up the requesting app."
+ "Delete Items"
+ "Discarding a verification codes delivery setup presentation whose client went away"
+ "Forget"
+ "Hosted scene reported the answer. shouldProceed=%{bool,public}d"
+ "No accounts need verification codes delivery setup"
+ "No host window provided."
+ "No presentation anchor provided."
+ "Passkeys are digital keys saved to your iCloud Keychain. They are backed up and sync across all of your Apple devices. You can use a passkey to sign in to apps and websites on iPhone, iPad, Mac, Apple TV, Vision\u00a0Pro, and web browsers on other platforms.\n\nPasskeys keep your accounts more secure than passwords do. They use powerful cryptography, which makes every passkey strong. Unlike passwords, malicious websites cannot trick you into giving away your passkeys.\n\nYou sign in to apps and websites with passkeys differently than you do with passwords. When prompted to sign in with a passkey, you use Face\u00a0ID, Touch\u00a0ID, Optic\u00a0ID, or your device passcode. Your biometric information and device passcode are never sent to the service you’re signing in to."
+ "Rejected an unentitled connection to the verification codes delivery setup endpoint"
+ "Rejecting %{public}s from a connection that does not own the current operation."
+ "S"
+ "Scene-hosting handshake arrived for an unexpected flow"
+ "Scene-hosting handshake arrived with no presentation in progress"
+ "There is no verification codes delivery setup in progress."
+ "Unable to extract bundle ID from app ID: %{public}@, error: %{public}@"
+ "View service disconnected from a verification codes delivery setup presentation"
+ "View service reported the answer. shouldProceed=%{bool,public}d"
+ "com.apple.AuthenticationServices._ASConditionalRegistrationRequester"
+ "presentAccountsToSetUp(_:reason:anchor:)"
+ "wapi"
- "\t"
- "-[_ASAgentCredentialExchangeListener _setUpExporterConnection:forOperation:]_block_invoke"
- "-[_ASAgentCredentialExchangeListener continueExportWithCredentials:completionHandler:]_block_invoke_2"
- "-[_ASAgentCredentialExchangeListener importCredentialsWithToken:completionHandler:]"
- "AuthenticationServices.ASGeneratePasswordsRequest"
- "AuthenticationServices.ASGeneratedPassword"
- "AuthenticationServices.ASSavePasswordRequest"
- "AuthenticationServices.__ASAuthorizationPublicKeyCredentialPRFAssertionInput"
- "AuthenticationServices.__ASAuthorizationPublicKeyCredentialPRFAssertionInputValues"
- "AuthenticationServices.__ASAuthorizationPublicKeyCredentialPRFAssertionOutput"
- "AuthenticationServices.__ASAuthorizationPublicKeyCredentialPRFRegistrationInput"
- "AuthenticationServices.__ASAuthorizationPublicKeyCredentialPRFRegistrationOutput"
- "AuthenticationServices_Private.ASPasswordAuthenticationPaneViewControllerConfiguration"
- "AuthenticationServices_Private.ASPasswordSavingManager"
- "AuthenticationServices_Private.RequestObject"
- "AuthenticationServices_Private._ASAgentAutomaticSecurityUpgradeListener"
- "AuthenticationServices_Private.__ASPasswordSavingModalState"
- "AuthenticationServices_Private.__ASPasswordSavingProvidersState"
- "Passkeys are digital keys saved to your iCloud Keychain. They are backed up and sync across all of your Apple devices. You can use a passkey to sign in to apps and websites on iPhone, iPad, Mac, Apple TV, Vision\u00a0Pro, and web browsers on other platforms.\n\nPasskeys keep your accounts more secure than passwords do. They use powerful cryptography, which makes every passkey strong. Unlike passwords, malicious websites cannot trick you into giving away your passkeys.\n\nYou sign in to apps and websites with passkeys differently than you do with passwords. When prompted to sign in with a passkey, you use Face ID, Touch ID, Optic\u00a0ID, or your device passcode. Your biometric information and device passcode are never sent to the service you’re signing in to."
```
