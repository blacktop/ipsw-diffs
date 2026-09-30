## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-553.125.5.0.0
-  __TEXT.__text: 0x23bfb4
-  __TEXT.__auth_stubs: 0x3ba0
+553.250.1.0.0
+  __TEXT.__text: 0x24ef5c
+  __TEXT.__auth_stubs: 0x3bc0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x244
-  __TEXT.__objc_methlist: 0xb0ec
-  __TEXT.__cstring: 0x9f99
-  __TEXT.__const: 0xbd3e
-  __TEXT.__gcc_except_tab: 0x167c
-  __TEXT.__oslogstring: 0xdd7c
+  __TEXT.__objc_methlist: 0xb484
+  __TEXT.__cstring: 0xa579
+  __TEXT.__const: 0xbede
+  __TEXT.__gcc_except_tab: 0x169c
+  __TEXT.__oslogstring: 0xe5ec
   __TEXT.__dlopen_cstrs: 0x526
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x48b0
-  __TEXT.__swift5_typeref: 0xd528
-  __TEXT.__swift5_reflstr: 0x2526
-  __TEXT.__swift5_fieldmd: 0x2344
-  __TEXT.__swift5_types: 0x440
-  __TEXT.__swift5_capture: 0x2604
+  __TEXT.__constg_swiftt: 0x4ba8
+  __TEXT.__swift5_typeref: 0xd64a
+  __TEXT.__swift5_reflstr: 0x2616
+  __TEXT.__swift5_fieldmd: 0x247c
+  __TEXT.__swift5_types: 0x454
+  __TEXT.__swift5_capture: 0x2a24
   __TEXT.__swift5_assocty: 0xc50
-  __TEXT.__swift5_proto: 0x5bc
+  __TEXT.__swift5_proto: 0x5c4
   __TEXT.__swift_as_entry: 0x108
   __TEXT.__swift_as_ret: 0xec
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5360
+  __TEXT.__unwind_info: 0x5650
   __TEXT.__eh_frame: 0x1518
-  __TEXT.__objc_classname: 0x21ef
-  __TEXT.__objc_methname: 0x1b23b
-  __TEXT.__objc_methtype: 0x5009
-  __TEXT.__objc_stubs: 0x138a0
-  __DATA_CONST.__got: 0x1c50
-  __DATA_CONST.__const: 0x3110
-  __DATA_CONST.__objc_classlist: 0x7c8
+  __TEXT.__objc_classname: 0x2210
+  __TEXT.__objc_methname: 0x1b7a9
+  __TEXT.__objc_methtype: 0x508e
+  __TEXT.__objc_stubs: 0x13ba0
+  __DATA_CONST.__got: 0x1c68
+  __DATA_CONST.__const: 0x3248
+  __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6738
+  __DATA_CONST.__objc_selrefs: 0x6858
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x468
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x1df0
-  __AUTH_CONST.__const: 0x91e8
-  __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0x3c428
+  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x1e00
+  __AUTH_CONST.__const: 0x9dc8
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0x3d388
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x6758
-  __AUTH.__data: 0x2890
-  __DATA.__objc_ivar: 0xbd8
-  __DATA.__data: 0x5510
-  __DATA.__bss: 0xbfd0
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH.__objc_data: 0x6c10
+  __AUTH.__data: 0x29b0
+  __DATA.__objc_ivar: 0xbe8
+  __DATA.__data: 0x5590
+  __DATA.__bss: 0xbfe0
   __DATA.__common: 0x4c8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D900662D-1B90-31FB-8957-427ECA7D265B
-  Functions: 11214
-  Symbols:   17254
-  CStrings:  7995
+  UUID: F9168B06-1E15-3367-8C08-52B6F0E09593
+  Functions: 11617
+  Symbols:   17530
+  CStrings:  8123
 
Symbols:
+ +[AAUIFeatureFlags isAgeAssuranceEnabled]
+ +[AAUIFeatureFlags isPrivacyRepromptEnabled]
+ +[AAUIFeatureFlags isPrivacyRepromptEnabled].cold.1
+ +[AAUIFeatureFlags isPrivacyRepromptEnabled].cold.2
+ -[AAUIConnectToFamilyFlowPresenter .cxx_destruct]
+ -[AAUIConnectToFamilyFlowPresenter authContext]
+ -[AAUIConnectToFamilyFlowPresenter dismissConnectToFamilyCFU]
+ -[AAUIConnectToFamilyFlowPresenter followupController]
+ -[AAUIConnectToFamilyFlowPresenter initWithViewController:]
+ -[AAUIConnectToFamilyFlowPresenter initWithViewController:].cold.1
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]
+ -[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:].cold.1
+ -[AAUIConnectToFamilyFlowPresenter presentingViewController]
+ -[AAUIConnectToFamilyFlowPresenter setAuthContext:]
+ -[AAUIConnectToFamilyFlowPresenter setFollowupController:]
+ -[AAUIConnectToFamilyFlowPresenter setPresentingViewController:]
+ -[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]
+ -[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:].cold.1
+ -[AAUIServiceSignInController _configureBasicAuthContext:forAccount:serviceType:viewController:]
+ -[AAUIServiceSignInController _configurePrimaryiCloudAuthContext:]
+ -[AAUIServiceSignInController _createAuthContextForExistingAccount:serviceType:viewController:]
+ -[AAUIServiceSignInController _performAuthenticationWithContext:completion:]
+ -[AAUIServiceSignInController signInViewController:didDetectPrivacyConsentVersion:]
+ -[AAUIServiceSignInController signInViewController:didDetectPrivacyConsentVersion:].cold.1
+ -[AAUIServiceSignInController signInViewController:didDetectPrivacyConsentVersion:].cold.2
+ -[AAUIServiceSignInController signInViewController:didDetectPrivacyConsentVersion:].cold.3
+ -[AAUIServiceSignInController signInViewController:didDetectPrivacyConsentVersion:].cold.4
+ -[AAUISignInViewController _cacheAuthenticationContext:]
+ -[AAUISignInViewController _configureBasicAuthenticationContext:]
+ -[AAUISignInViewController _configurePiggybackingForContext:]
+ -[AAUISignInViewController _configureProtoAccountForContext:]
+ -[AAUISignInViewController _createAuthenticationContext]
+ -[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]
+ -[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate].cold.1
+ -[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate].cold.2
+ -[AAUISignInViewController _transferPrivacyVersionToContext:]
+ -[AAUISignInViewController cachedAuthContext]
+ -[AAUISignInViewController setCachedAuthContext:]
+ GCC_except_table119
+ GCC_except_table46
+ GCC_except_table75
+ _AAUIConnectToFamilyFlowPresenterErrorDomain
+ _AppleMediaServicesUILibrary
+ _NSSelectorFromString
+ _OBJC_CLASS_$_AAUIConnectToFamilyFlowPresenter
+ _OBJC_CLASS_$_AAUIPrivacyConsentUIProvider
+ _OBJC_CLASS_$_AAUIPrivacyConsentViewController
+ _OBJC_CLASS_$_OBBundle
+ _OBJC_CLASS_$_OBPrivacyFlow
+ _OBJC_CLASS_$__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ _OBJC_IVAR_$_AAUIConnectToFamilyFlowPresenter._authContext
+ _OBJC_IVAR_$_AAUIConnectToFamilyFlowPresenter._followupController
+ _OBJC_IVAR_$_AAUIConnectToFamilyFlowPresenter._presentingViewController
+ _OBJC_IVAR_$_AAUISignInViewController._cachedAuthContext
+ _OBJC_METACLASS_$_AAUIConnectToFamilyFlowPresenter
+ _OBJC_METACLASS_$_AAUIPrivacyConsentUIProvider
+ _OBJC_METACLASS_$_AAUIPrivacyConsentViewController
+ _OBJC_METACLASS_$__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __CLASS_METHODS_AAUIPrivacyConsentUIProvider
+ __DATA_AAUIPrivacyConsentUIProvider
+ __DATA_AAUIPrivacyConsentViewController
+ __DATA__TtC14AppleAccountUI25AAUIDefaultConsentService
+ __DATA__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __INSTANCE_METHODS_AAUIPrivacyConsentUIProvider
+ __INSTANCE_METHODS_AAUIPrivacyConsentViewController
+ __INSTANCE_METHODS__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __IVARS_AAUIPrivacyConsentUIProvider
+ __IVARS_AAUIPrivacyConsentViewController
+ __IVARS__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __METACLASS_DATA_AAUIPrivacyConsentUIProvider
+ __METACLASS_DATA_AAUIPrivacyConsentViewController
+ __METACLASS_DATA__TtC14AppleAccountUI25AAUIDefaultConsentService
+ __METACLASS_DATA__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __OBJC_$_INSTANCE_METHODS_AAUIConnectToFamilyFlowPresenter
+ __OBJC_$_INSTANCE_VARIABLES_AAUIConnectToFamilyFlowPresenter
+ __OBJC_$_PROP_LIST_AAUIConnectToFamilyFlowPresenter
+ __OBJC_CLASS_RO_$_AAUIConnectToFamilyFlowPresenter
+ __OBJC_METACLASS_RO_$_AAUIConnectToFamilyFlowPresenter
+ __PROPERTIES_AAUIPrivacyConsentViewController
+ __PROPERTIES__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __PROTOCOLS__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel
+ __PROTOCOLS__TtC14AppleAccountUI27AAUIPrivacyConsentViewModel.11
+ ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.53
+ ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.54
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.41
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke.48
+ ___116-[AAUIPaymentVerificationHook _validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:]_block_invoke_2
+ ___61-[AAUIConnectToFamilyFlowPresenter dismissConnectToFamilyCFU]_block_invoke
+ ___61-[AAUIConnectToFamilyFlowPresenter dismissConnectToFamilyCFU]_block_invoke.cold.1
+ ___62-[AAUISignInViewController _attemptAuthenticationWithContext:]_block_invoke.231
+ ___73-[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]_block_invoke
+ ___73-[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]_block_invoke.cold.1
+ ___73-[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]_block_invoke.cold.2
+ ___73-[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]_block_invoke.cold.3
+ ___73-[AAUISignInViewController _detectPrivacyConsentVersionAndNotifyDelegate]_block_invoke.cold.4
+ ___76-[AAUIServiceSignInController _performAuthenticationWithContext:completion:]_block_invoke
+ ___76-[AAUIServiceSignInController _performAuthenticationWithContext:completion:]_block_invoke_2
+ ___77-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]_block_invoke
+ ___77-[AAUIConnectToFamilyFlowPresenter presentConnectToFamilyFlowWithCompletion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48bs_e58_v24?0"AMSUIRegulatoryAgeVerificationResult"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.180
+ ___block_literal_global.185
+ ___getAMSUIRegulatoryAgeVerificationTaskClass_block_invoke
+ ___getAMSUIRegulatoryAgeVerificationTaskClass_block_invoke.cold.1
+ _block_copy_helper.101
+ _block_copy_helper.11
+ _block_copy_helper.14
+ _block_copy_helper.172
+ _block_copy_helper.21
+ _block_copy_helper.28
+ _block_copy_helper.41
+ _block_descriptor.103
+ _block_descriptor.13
+ _block_descriptor.16
+ _block_descriptor.174
+ _block_descriptor.23
+ _block_descriptor.30
+ _block_descriptor.43
+ _block_destroy_helper.102
+ _block_destroy_helper.12
+ _block_destroy_helper.15
+ _block_destroy_helper.173
+ _block_destroy_helper.22
+ _block_destroy_helper.29
+ _block_destroy_helper.42
+ _getAMSUIRegulatoryAgeVerificationTaskClass
+ _getAMSUIRegulatoryAgeVerificationTaskClass.softClass
+ _objc_msgSend$_cacheAuthenticationContext:
+ _objc_msgSend$_configureBasicAuthContext:forAccount:serviceType:viewController:
+ _objc_msgSend$_configureBasicAuthenticationContext:
+ _objc_msgSend$_configurePiggybackingForContext:
+ _objc_msgSend$_configurePrimaryiCloudAuthContext:
+ _objc_msgSend$_configureProtoAccountForContext:
+ _objc_msgSend$_createAuthContextForExistingAccount:serviceType:viewController:
+ _objc_msgSend$_createAuthenticationContext
+ _objc_msgSend$_detectPrivacyConsentVersionAndNotifyDelegate
+ _objc_msgSend$_performAuthenticationWithContext:completion:
+ _objc_msgSend$_transferPrivacyVersionToContext:
+ _objc_msgSend$_validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:
+ _objc_msgSend$cachedAuthContext
+ _objc_msgSend$contentVersion
+ _objc_msgSend$createBagForSubProfile
+ _objc_msgSend$dismissConnectToFamilyCFU
+ _objc_msgSend$flowWithBundle:
+ _objc_msgSend$initWithAccountParameters:viewController:bag:
+ _objc_msgSend$perform
+ _objc_msgSend$privacyBundleVersion
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$setCachedAuthContext:
+ _objc_msgSend$setPrivacyBundleVersion:
+ _objc_msgSend$setTeenRequiredToConnectToFamily:
+ _objc_msgSend$signInViewController:didDetectPrivacyConsentVersion:
+ _swift_dynamicCastMetatype
+ _symbolic $s14AppleAccountUI26AAUIConsentServiceProtocolP
+ _symbolic $s14AppleAccountUI27AAUIPrivacyConsentProvidingP
+ _symbolic Sb______pSgIegyg_ s5ErrorP
+ _symbolic Sb______pSgytIegnnr_ s5ErrorP
+ _symbolic _____ 14AppleAccountUI25AAUIDefaultConsentServiceC
+ _symbolic _____ 14AppleAccountUI27AAUIPrivacyConsentViewModelC
+ _symbolic _____ 14AppleAccountUI28AAUIPrivacyConsentUIProviderC
+ _symbolic _____ 14AppleAccountUI32AAUIPrivacyConsentViewControllerC
+ _symbolic _____SgSo7NSErrorCSgIeyByy_ 14AppleAccountUI32AAUIPrivacyConsentViewControllerC
+ _symbolic _____SgXw 14AppleAccountUI32AAUIPrivacyConsentViewControllerC
+ _symbolic _____SgXwz_Xx 14AppleAccountUI32AAUIPrivacyConsentViewControllerC
+ _symbolic _____Sg______pSgIeggg_ 14AppleAccountUI32AAUIPrivacyConsentViewControllerC s5ErrorP
+ _symbolic _____So7NSErrorCSgIeyByy_ 10ObjectiveC8ObjCBoolV
+ _symbolic ______p 14AppleAccountUI26AAUIConsentServiceProtocolP
+ _symbolic ySb_______pSgtcSg s5ErrorP
- GCC_except_table32
- GCC_except_table42
- GCC_except_table52
- GCC_except_table63
- ___100-[AAUIServiceSignInController _authenticateExistingAccount:serviceType:inViewController:completion:]_block_invoke
- ___100-[AAUIServiceSignInController _authenticateExistingAccount:serviceType:inViewController:completion:]_block_invoke_2
- ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.41
- ___101-[AAUIPaymentVerificationHook _validatePaymentVerificationWithTokenFetchTask:objectModel:completion:]_block_invoke.49
- ___62-[AAUISignInViewController _attemptAuthenticationWithContext:]_block_invoke.228
- ___block_literal_global.177
- ___block_literal_global.182
- _objc_msgSend$_validatePaymentVerificationWithTokenFetchTask:objectModel:completion:
CStrings:
+ "@\"AAFollowUpController\""
+ "@\"AKAppleIDAuthenticationInAppContext\""
+ "AAPrivacyConsentManager"
+ "AAPrivacyConsentManager method not available, using fallback"
+ "AAPrivacyConsentManager not available, using fallback"
+ "AAPrivacyConsentManager response - shouldPresent: %{bool}d, error: %s"
+ "AAUIConnectToFamilyFlowPresenter"
+ "AAUIConnectToFamilyFlowPresenterErrorDomain"
+ "AMSUIRegulatoryAgeVerificationTask"
+ "AMSUIRegulatoryAgeVerificationTask retuned with token %@ error : %@"
+ "About Apple Account & Privacy"
+ "Accessibility label for the Apple Account symbol in privacy consent UI"
+ "AgeAssurance"
+ "Apple Account"
+ "Apple Account & Privacy has been updated to better explain how Apple collects, uses, and protects your personal information."
+ "AppleAccountUI.AAUIPrivacyConsentUIProvider"
+ "AppleAccountUI.AAUIPrivacyConsentViewController"
+ "AppleAccountUI/AAUIPrivacyConsentUIProvider.swift"
+ "AppleAccountUI/AAUIPrivacyConsentViewController.swift"
+ "AppleAccountUI/PrivacyReprompt is enabled on internal builds."
+ "AppleAccountUI/PrivacyReprompt=%d"
+ "Auth context does not support privacyBundleVersion property"
+ "AuthKit"
+ "AuthKit/isAgeAssuranceEnabled %d"
+ "Body text for Apple Account & Privacy About Text UI"
+ "Calling AAPrivacyConsentManager.shouldPresentConsentUI"
+ "Checking consent UI eligibility for account: %s"
+ "ConnectToFamilyFlowPresenter - Connect to family encountered an error: %{public}@"
+ "ConnectToFamilyFlowPresenter - Connect to family succeeded."
+ "ConnectToFamilyFlowPresenter - Dismissed connect to family CFU"
+ "ConnectToFamilyFlowPresenter - Dismissing connect to family CFU encountered an error: %{public}@"
+ "ConnectToFamilyFlowPresenter - init"
+ "ConnectToFamilyFlowPresenter - present."
+ "ConnectToFamilyFlowPresenter - presenting view controller is nil. Nothing to do."
+ "Consent UI should present: %s"
+ "Consent flow completed with success: %{bool}d"
+ "Consent flow error: %s"
+ "Created consent view controller"
+ "Creating consent view controller"
+ "Delegate does not respond to privacy consent version detection, skipping"
+ "Detected privacy consent version: %@"
+ "Error checking consent eligibility: %s"
+ "Exception occurred during privacy consent version detection: %@"
+ "Failed to get primary button"
+ "Failed to record consent acknowledgment: %s"
+ "No privacy bundle found for identifier: %@"
+ "No privacy flow found for bundle: %@"
+ "No privacy link identifiers configured, skipping privacy consent version detection"
+ "OK button for privacy consent UI"
+ "PRIVACY_CONSENT_BODY"
+ "PRIVACY_CONSENT_CONTINUE"
+ "PRIVACY_CONSENT_SYMBOL_ACCESSIBILITY_LABEL"
+ "PRIVACY_CONSENT_TITLE"
+ "Privacy consent UI configured"
+ "Privacy consent UI dismissed without Continue"
+ "Privacy consent UI loaded"
+ "Privacy consent version detected: %@"
+ "Privacy consent version setting FAILED - expected %@, got %@"
+ "Privacy consent version successfully set: %@"
+ "PrivacyReprompt"
+ "Successfully recorded consent acknowledgment"
+ "T@\"AAFollowUpController\",&,N,V_followupController"
+ "T@\"AKAppleIDAuthenticationInAppContext\",&,N,V_authContext"
+ "T@\"AKAppleIDAuthenticationInAppContext\",&,N,V_cachedAuthContext"
+ "T@?,N,C"
+ "Title for Apple Account & Privacy About Text UI"
+ "Unable to get auth context to set privacy bundle version"
+ "Unable to perform age verification!"
+ "Unknown error"
+ "User tapped Continue button"
+ "Using AMSUIRegulatoryAgeVerificationTask"
+ "_TtC14AppleAccountUI25AAUIDefaultConsentService"
+ "_TtC14AppleAccountUI27AAUIPrivacyConsentViewModel"
+ "_cacheAuthenticationContext:"
+ "_cachedAuthContext"
+ "_configureBasicAuthContext:forAccount:serviceType:viewController:"
+ "_configureBasicAuthenticationContext:"
+ "_configurePiggybackingForContext:"
+ "_configurePrimaryiCloudAuthContext:"
+ "_configureProtoAccountForContext:"
+ "_createAuthContextForExistingAccount:serviceType:viewController:"
+ "_createAuthenticationContext"
+ "_detectPrivacyConsentVersionAndNotifyDelegate"
+ "_performAuthenticationWithContext:completion:"
+ "_transferPrivacyVersionToContext:"
+ "_validatePaymentVerificationWithRegulatoryAgeVerificationTask:objectModel:completion:"
+ "apple.account"
+ "cachedAuthContext"
+ "com.apple.AAFollowUpIdentifier.connectToFamily"
+ "consentService"
+ "consentViewControllerForAccount:completion:"
+ "consentViewControllerIfNeeded:completion:"
+ "contentVersion"
+ "createBagForSubProfile"
+ "defaultProvider"
+ "dismissConnectToFamilyCFU"
+ "flowWithBundle:"
+ "hasCompleted"
+ "init(coder:) has not been implemented"
+ "initWithAccountParameters:viewController:bag:"
+ "initWithViewController:"
+ "isAgeAssuranceEnabled"
+ "isBeingDismissed"
+ "isPrivacyRepromptEnabled"
+ "perform"
+ "presentConnectToFamilyFlowWithCompletion:"
+ "privacyBundleIdentifier"
+ "privacyBundleVersion"
+ "recordConsentAcknowledgmentForAccount:completion:"
+ "resultWithCompletion:"
+ "setCachedAuthContext:"
+ "setPrivacyBundleVersion:"
+ "setPrivacyLinkForBundles:"
+ "setTeenRequiredToConnectToFamily:"
+ "shouldPresentConsentUIForAccount:completion:"
+ "signInViewController:didDetectPrivacyConsentVersion:"
+ "v24@?0@\"AMSUIRegulatoryAgeVerificationResult\"8@\"NSError\"16"
+ "v32@0:8@\"AAUISignInViewController\"16@\"NSString\"24"
+ "v48@0:8@16@24@32@40"

```
