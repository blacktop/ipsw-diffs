## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-17.2.1.0.0
-  __TEXT.__text: 0x31060
-  __TEXT.__auth_stubs: 0xc20
+17.4.6.0.0
+  __TEXT.__text: 0x43290
+  __TEXT.__auth_stubs: 0x1530
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x206c
-  __TEXT.__const: 0x514
-  __TEXT.__gcc_except_tab: 0xb44
-  __TEXT.__cstring: 0x31cf
-  __TEXT.__oslogstring: 0x48b4
+  __TEXT.__objc_methlist: 0x2324
+  __TEXT.__const: 0x1014
+  __TEXT.__gcc_except_tab: 0xb3c
+  __TEXT.__cstring: 0x3773
+  __TEXT.__oslogstring: 0x535d
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
-  __TEXT.__constg_swiftt: 0xe0
-  __TEXT.__swift5_typeref: 0x136
-  __TEXT.__swift5_fieldmd: 0x58
-  __TEXT.__swift5_capture: 0x28
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x23
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xc70
-  __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0x7189
-  __TEXT.__objc_methtype: 0xd73
-  __TEXT.__objc_stubs: 0x6080
-  __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x10d0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__swift5_typeref: 0x714
+  __TEXT.__swift5_capture: 0x1ac
+  __TEXT.__constg_swiftt: 0x438
+  __TEXT.__swift5_reflstr: 0x361
+  __TEXT.__swift5_fieldmd: 0x2ac
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__unwind_info: 0x1280
+  __TEXT.__eh_frame: 0x828
+  __TEXT.__objc_classname: 0x6ed
+  __TEXT.__objc_methname: 0x76a0
+  __TEXT.__objc_methtype: 0x1086
+  __TEXT.__objc_stubs: 0x6340
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__const: 0x10f8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dd8
+  __DATA_CONST.__objc_selrefs: 0x1f00
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x2c80
-  __AUTH_CONST.__objc_const: 0x1fa8
+  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH_CONST.__const: 0xbf0
+  __AUTH_CONST.__cfstring: 0x2d20
+  __AUTH_CONST.__objc_const: 0x2430
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x740
-  __AUTH.__data: 0xc0
+  __AUTH.__objc_data: 0xbd0
+  __AUTH.__data: 0x388
   __DATA.__objc_ivar: 0xf4
-  __DATA.__data: 0x674
-  __DATA.__bss: 0x778
+  __DATA.__data: 0xa54
+  __DATA.__bss: 0x1128
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings
   - /System/Library/PrivateFrameworks/Home.framework/Home

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CD6207DE-9069-3664-BCE1-A87631BC6EBB
-  Functions: 1058
-  Symbols:   3748
-  CStrings:  2417
+  UUID: 7E8ED878-9A44-3C97-9DD3-9F42F65DCE99
+  Functions: 1441
+  Symbols:   4092
+  CStrings:  2579
 
Symbols:
+ -[PABSTouchIDPasscodeController enrollmentControllerDidDismiss].cold.1
+ -[PABSTouchIDPasscodeController viewDidAppear:].cold.1
+ -[PSListController(PasscodeExtraction) extractPasscodeObjectFromSpecifier:]
+ -[PSListController(PasscodeExtraction) extractPasscodeObjectFromSpecifier:].cold.1
+ -[PSListController(PasscodeExtraction) extractPasscodeObjectFromSpecifier:].cold.2
+ -[PSListController(PasscodeExtraction) extractPasscodeObject]
+ -[PSListController(PasscodeExtraction) extractPasscodeStringFromContext:error:]
+ -[PSListController(PasscodeExtraction) extractPasscodeStringFromContext:error:].cold.1
+ -[PSListController(PasscodeExtraction) extractPasscodeStringFromContext:error:].cold.2
+ -[PSListController(PasscodeExtraction) extractPasscodeStringFromContext:error:].cold.3
+ -[PSListController(PasscodeExtraction) extractPasscodeStringWithError:]
+ -[PSListController(PasscodeExtraction) extractPasscodeStringWithError:].cold.1
+ -[PSListController(PasscodeExtraction) extractPasscodeStringWithError:].cold.2
+ -[PSListController(PasscodeExtraction) updatePasscodeObject:]
+ -[PSListController(PasscodeExtraction) updatePasscodeObjectFromString:]
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table134
+ GCC_except_table154
+ GCC_except_table36
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table71
+ GCC_except_table80
+ GCC_except_table96
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_pearlIDCapability
+ _MobileGestalt_get_touchIDCapability
+ _OBJC_CLASS_$_LAPasscodeVerificationService
+ _OBJC_CLASS_$_LAPasscodeVerificationServiceOptions
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_PSListControllerCellHighlightingSelectionInvocationRelay
+ _OBJC_CLASS_$__TtC29PasscodeAndBiometricsSettings11BundleToken
+ _OBJC_CLASS_$__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ _OBJC_CLASS_$__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ _OBJC_CLASS_$__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ _OBJC_CLASS_$__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ _OBJC_METACLASS_$__TtC29PasscodeAndBiometricsSettings11BundleToken
+ _OBJC_METACLASS_$__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ _OBJC_METACLASS_$__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ _OBJC_METACLASS_$__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ _OBJC_METACLASS_$__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_9
+ _PSListControllerCellHighlightingSelectionInvocationRelayKey
+ __CLASS_METHODS__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ __CLASS_METHODS__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ __CLASS_PROPERTIES__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ __DATA__TtC29PasscodeAndBiometricsSettings11BundleToken
+ __DATA__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ __DATA__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ __DATA__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ __DATA__TtC29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModel
+ __DATA__TtC29PasscodeAndBiometricsSettings38PABSPasscodeVerificationStateViewModel
+ __DATA__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ __INSTANCE_METHODS__TtC29PasscodeAndBiometricsSettings11BundleToken
+ __INSTANCE_METHODS__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ __INSTANCE_METHODS__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ __INSTANCE_METHODS__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ __INSTANCE_METHODS__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ __IVARS__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ __IVARS__TtC29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModel
+ __IVARS__TtC29PasscodeAndBiometricsSettings38PABSPasscodeVerificationStateViewModel
+ __IVARS__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings11BundleToken
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings13PABSConstants
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModel
+ __METACLASS_DATA__TtC29PasscodeAndBiometricsSettings38PABSPasscodeVerificationStateViewModel
+ __METACLASS_DATA__TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder
+ __OBJC_$_CATEGORY_PSListController_$_PasscodeExtraction
+ __OBJC_$_INSTANCE_METHODS_PSListController(PasscodeExtraction|Utility)
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_PSController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PSController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PSController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PSStateRestoration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PSController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PSStateRestoration
+ __OBJC_$_PROTOCOL_REFS_PSController
+ __OBJC_$_PROTOCOL_REFS_PSStateRestoration
+ __OBJC_LABEL_PROTOCOL_$_PSController
+ __OBJC_LABEL_PROTOCOL_$_PSStateRestoration
+ __OBJC_PROTOCOL_$_PSController
+ __OBJC_PROTOCOL_$_PSStateRestoration
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.590
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.592
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.594
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.595
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.599
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.599.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.601
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.601.cold.1
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.597
+ ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.584
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.554
+ ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.554.cold.1
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.315
+ ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.315.cold.1
+ ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.760
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.114
+ ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.114.cold.1
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.310
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.312
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.313
+ ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.313.cold.1
+ ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.175
+ ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.730
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.908
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.908.cold.1
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.909
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.204
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.205
+ ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.206
+ ___62-[PABSPearlAttentionGroupController setPearlUnlock:specifier:]_block_invoke.70
+ ___62-[PABSPearlAttentionGroupController setPearlUnlock:specifier:]_block_invoke.75
+ ___62-[PABSPearlAttentionGroupController setPearlUnlock:specifier:]_block_invoke.cold.1
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.654
+ ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.658
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke.88
+ ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_2.89
+ ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.886
+ ___71-[PABSBiometricController proceedTouchIDForStockholmEnabled:specifier:]_block_invoke.cold.1
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.267
+ ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.267.cold.1
+ ___79-[PSListController(PasscodeExtraction) extractPasscodeStringFromContext:error:]_block_invoke
+ ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.292
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.967
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.967.cold.1
+ ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.968
+ ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.972
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.951
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.955
+ ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.962
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.976
+ ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.977
+ ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.947
+ ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.125
+ ___95-[PABSFaceIDEnrollmentCoordinator preloadAndCreateEnrollmentControllerWithPasscode:completion:]_block_invoke_2.cold.1
+ ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSString"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_tmp.181
+ ___block_literal_global.183
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.604
+ ___block_literal_global.660
+ ___block_literal_global.666
+ ___block_literal_global.756
+ ___block_literal_global.758
+ ___block_literal_global.762
+ ___block_literal_global.957
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy16_8
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_0Tm
+ ___swift_project_value_buffer
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 29PasscodeAndBiometricsSettings0A18VerificationStatusOSHAASQ
+ _associated conformance 29PasscodeAndBiometricsSettings12PABSRootViewV7SwiftUI0F0AA4BodyAdEP_AdE
+ _associated conformance 29PasscodeAndBiometricsSettings13BiometricTypeOSHAASQ
+ _associated conformance 29PasscodeAndBiometricsSettings13BiometricTypeOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 29PasscodeAndBiometricsSettings14PABSLockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV7SwiftUI0F0AA4BodyAeFP_AeF
+ _associated conformance 29PasscodeAndBiometricsSettings15PABSFeatureFlagOSHAASQ
+ _associated conformance 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV7SwiftUI0F0AA4BodyAeFP_AeF
+ _associated conformance 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV7SwiftUI06UIViewG13RepresentableAaD0F0
+ _associated conformance 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV7SwiftUI0F0AA4BodyAdEP_AdE
+ _block_copy_helper.63
+ _block_descriptor.65
+ _block_destroy_helper.64
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyACyACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGAA022_EnvironmentKeyWritingM0VyAA4FontVSgGGAA017_AppearanceActionM0VG_So16UIViewControllerCSgQo_AYGAaDHPqd0__AaDHD3_A2_HO_AyA0eM0HPyHCHC.59
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA5GroupVyAA012_ConditionalD0Vy19PreferencesExtended0G14ControllerViewVAA4TextVGGAA25_AppearanceActionModifierVGAPGAA0J0HPAqaSHPAnaSHPAmaSHPAjaSHPyHC_AlaSHPyHCHC_HC_ApA0jN0HPyHCHC_ApaTHPyHCHC.58
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAA5GroupVyAA012_ConditionalI0Vy29PasscodeAndBiometricsSettings012PABSUnlockedC033_3802A58DA4E1D8E56B33C7255C8E20F1LLVAM010PABSLockedC0AOLLVGGAA19_BackgroundModifierVyAHyAM07HostingC17ControllerCaptureVAA12_FrameLayoutVGGG_SbQo_HO.12
+ _malloc_size
+ _memmove
+ _objc_autorelease
+ _objc_msgSend$canOpenURL:
+ _objc_msgSend$colorWithAlphaComponent:
+ _objc_msgSend$enableForType:withIDSDeviceID:passcodeRef:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$extractAndDecodePasscodeFrom:completionHandler:
+ _objc_msgSend$extractPasscodeObject
+ _objc_msgSend$extractPasscodeObjectFrom:
+ _objc_msgSend$extractPasscodeObjectFromSpecifier:
+ _objc_msgSend$extractPasscodeStringFromContext:error:
+ _objc_msgSend$extractPasscodeStringWithError:
+ _objc_msgSend$graceValue:
+ _objc_msgSend$init
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$labelColor
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$primeWithExternalizedAuthContext:
+ _objc_msgSend$setBoolValue:forSetting:credentialSet:
+ _objc_msgSend$setCredential:type:
+ _objc_msgSend$setDismissUIAfterCompletion:
+ _objc_msgSend$setFingerprintUnlockAllowed:credentialSet:completionBlock:
+ _objc_msgSend$setTitleView:
+ _objc_msgSend$setValue:forSetting:credentialSet:
+ _objc_msgSend$specifierIdentifierToScrollAndHighlight
+ _objc_msgSend$specifierIdentifierToScrollAndSelect
+ _objc_msgSend$target
+ _objc_msgSend$updatePasscodeObject:
+ _objc_msgSend$updatePasscodeObject:passcodePaneSpecifier:
+ _objc_msgSend$updatePasscodeObjectFromString:
+ _objc_msgSend$updatePasscodeObjectWithString:passcodePaneSpecifier:
+ _objectdestroy.23Tm
+ _objectdestroyTm
+ _swift_allocError
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deletedAsyncMethodErrorTu
+ _swift_dynamicCast
+ _swift_dynamicCastMetatype
+ _swift_dynamicCastTypeToObjCProtocolConditional
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getAtKeyPath
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getKeyPath
+ _swift_getOpaqueTypeConformance2
+ _swift_getSingletonMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
+ _symbolic $s7SwiftUI29UIViewControllerRepresentableP
+ _symbolic $s7SwiftUI4ViewP
+ _symbolic $ss12CaseIterableP
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic Ig_
+ _symbolic SSSg
+ _symbolic SSSg______pSgIeghgg_ s5ErrorP
+ _symbolic Say_____G 29PasscodeAndBiometricsSettings13BiometricTypeO
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Sb
+ _symbolic Sb12userCanceled_t
+ _symbolic ScA_pSg
+ _symbolic ScCySo9LAContextC______pG s5ErrorP
+ _symbolic ScCy_____Sg______pG 10Foundation4DataV s5ErrorP
+ _symbolic ScPSg
+ _symbolic So11PSSpecifierC
+ _symbolic So16UIViewControllerC
+ _symbolic So16UIViewControllerCSg
+ _symbolic So16UIViewControllerCSgXw
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringCSgIeyBy_
+ _symbolic So8NSStringCSgSo7NSErrorCSgIeyBhyy_
+ _symbolic So9LAContextC
+ _symbolic So9LAContextCSg
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 29PasscodeAndBiometricsSettings0A18VerificationStatusO
+ _symbolic _____ 29PasscodeAndBiometricsSettings0A19AuthenticationErrorO
+ _symbolic _____ 29PasscodeAndBiometricsSettings11BundleTokenC
+ _symbolic _____ 29PasscodeAndBiometricsSettings12PABSRootViewV
+ _symbolic _____ 29PasscodeAndBiometricsSettings13BiometricTypeO
+ _symbolic _____ 29PasscodeAndBiometricsSettings13PABSConstantsC
+ _symbolic _____ 29PasscodeAndBiometricsSettings14PABSLockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV
+ _symbolic _____ 29PasscodeAndBiometricsSettings15PABSFeatureFlagO
+ _symbolic _____ 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV
+ _symbolic _____ 29PasscodeAndBiometricsSettings19FeatureFlagsManagerC
+ _symbolic _____ 29PasscodeAndBiometricsSettings19PABSPasscodeManagerC
+ _symbolic _____ 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV
+ _symbolic _____ 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV04HostfG6FinderC
+ _symbolic _____ 29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModelC
+ _symbolic _____ 29PasscodeAndBiometricsSettings38PABSPasscodeVerificationStateViewModelC
+ _symbolic _____ 7SwiftUI17EnvironmentValuesV
+ _symbolic _____ 8Settings0A15NavigationProxyV
+ _symbolic _____ s5NeverO
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 7SwiftUI4FontV
+ _symbolic _____Sg 7SwiftUI4FontV6DesignO
+ _symbolic _____Sg So20NSNotificationCenterC10FoundationE16ObservationTokenV
+ _symbolic _____SgXw 29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModelC
+ _symbolic ______p s19_HasContiguousBytesP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s19_HasContiguousBytesP
+ _symbolic _____yAAyAAy__________y_____GG_____y_____SgGG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA022_EnvironmentKeyWritingH0V AA4FontV AA017_AppearanceActionH0V
+ _symbolic _____yAAy__________y_____GG_____y_____SgGG 7SwiftUI15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA022_EnvironmentKeyWritingH0V AA4FontV
+ _symbolic _____yAAy_____y_____y__________GG_____GAHG 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V 19PreferencesExtended0G14ControllerViewV AA4TextV AA25_AppearanceActionModifierV
+ _symbolic _____ySbG 7SwiftUI5StateV
+ _symbolic _____ySo16UIViewControllerCSgG 7SwiftUI5StateV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 8Settings0D15NavigationProxyV
+ _symbolic _____y_____G 7SwiftUI24_ForegroundStyleModifierV AA5ColorV
+ _symbolic _____y_____G 7SwiftUI5StateV 29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModelC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____SgG 7SwiftUI30_EnvironmentKeyWritingModifierV AA4FontV
+ _symbolic _____y______G 7SwiftUI11EnvironmentV7ContentO 8Settings0E15NavigationProxyV
+ _symbolic _____y______G So20NSNotificationCenterC10FoundationE21BaseMessageIdentifierV So13UIApplicationC5UIKitE018DidEnterBackgroundE0V
+ _symbolic _____y______G So20NSNotificationCenterC10FoundationE21BaseMessageIdentifierV So13UIApplicationC5UIKitE019WillEnterForegroundE0V
+ _symbolic _____y__________G 7SwiftUI19_ConditionalContentV 19PreferencesExtended0E14ControllerViewV AA4TextV
+ _symbolic _____y__________G 7SwiftUI19_ConditionalContentV 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV AD010PABSLockedJ0AFLLV
+ _symbolic _____y___________G 7SwiftUI19_ConditionalContentV7StorageO 19PreferencesExtended0F14ControllerViewV AA4TextV
+ _symbolic _____y__________y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV
+ _symbolic _____y_____yAAyAAyAAy__________y_____GG_____y_____SgGG_____G_So16UIViewControllerCSgQo_ALG 7SwiftUI15ModifiedContentV AA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA022_EnvironmentKeyWritingM0V AA4FontV AA017_AppearanceActionM0V
+ _symbolic _____y_____y__________GG 7SwiftUI19_BackgroundModifierV AA15ModifiedContentV 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV AA12_FrameLayoutV
+ _symbolic _____y_____y__________GG 7SwiftUI5GroupV AA19_ConditionalContentV 19PreferencesExtended0F14ControllerViewV AA4TextV
+ _symbolic _____y_____y__________GG 7SwiftUI5GroupV AA19_ConditionalContentV 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV AF010PABSLockedK0AHLLV
+ _symbolic _____y_____y_____y__________GG_____G 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V 19PreferencesExtended0G14ControllerViewV AA4TextV AA25_AppearanceActionModifierV
+ _symbolic _____y_____y_____y__________GG_____yAAy__________GGG 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV AH010PABSLockedL0AJLLV AA19_BackgroundModifierV AH07HostingL17ControllerCaptureV AA12_FrameLayoutV
+ _symbolic _____y_____y_____y_____y__________GG_____yAAy__________GGG_SbQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQO AA15ModifiedContentV AA5GroupV AA012_ConditionalI0V 29PasscodeAndBiometricsSettings012PABSUnlockedC033_3802A58DA4E1D8E56B33C7255C8E20F1LLV AM010PABSLockedC0AOLLV AA19_BackgroundModifierV AM07HostingC17ControllerCaptureV AA12_FrameLayoutV
+ _symbolic x
+ _symbolic ySo16UIViewControllerCc
+ _symbolic ypSg
+ _symbolic yt
+ _symbolic ytIeAgHr_
+ _type_layout_string 29PasscodeAndBiometricsSettings14PABSLockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV
+ _type_layout_string 29PasscodeAndBiometricsSettings16PABSUnlockedView33_3802A58DA4E1D8E56B33C7255C8E20F1LLV
+ _type_layout_string 29PasscodeAndBiometricsSettings28HostingViewControllerCaptureV
- -[PABSBiometricController authorizationToken]
- -[PABSBiometricController authorizationToken].cold.1
- -[PABSBiometricController authorizationToken].cold.2
- -[PABSBiometricController proceedTouchIDForStockholmEnabled:specifier:].cold.1
- -[PABSBiometricController proceedTouchIDForStockholmEnabled:specifier:].cold.2
- -[PABSPasscodeLockController _shouldUseLocalAuthenticationBasedPasscodeFlowForPINSheetRequest:]
- -[PABSPasscodeLockController enableAutoUnlockForDevice:ofSpecifier:].cold.2
- -[PABSPasscodeLockController enableVisionUnlockForDevice:ofSpecifier:].cold.1
- -[PABSPasscodeLockController enableVisionUnlockForDevice:ofSpecifier:].cold.2
- -[PABSPasscodeLockController setGraceValue:specifier:].cold.1
- -[PABSPasscodeLockController setGraceValue:specifier:].cold.2
- -[PABSPasscodeLockController shouldUseLocalAuthenticationBasedPasscodeFlowForChangePasscodeRequests]
- -[PABSPasscodeLockController shouldUseLocalAuthenticationBasedPasscodeFlowForRemovePasscodeRequests]
- -[PABSPearlPasscodeController event:params:reply:].cold.2
- -[PABSPearlPasscodeController proceedToEnrollGlassesForExistingAppearance:].cold.1
- -[PABSPearlPasscodeController proceedToEnrollGlassesForExistingAppearance:].cold.2
- -[PABSPearlPasscodeController proceedToEnrollPeriocularForExistingAppearance:].cold.1
- -[PABSPearlPasscodeController proceedToEnrollPeriocularForExistingAppearance:].cold.2
- -[PABSPearlPasscodeController proceedToEnrollWithSpecifier:].cold.1
- -[PABSPearlPasscodeController proceedToEnrollWithSpecifier:].cold.2
- -[PABSPearlPasscodeController pushPasscodePane]
- -[PABSPearlPasscodeController specifiers].cold.1
- -[PABSPearlPasscodeController specifiers].cold.2
- -[PABSTouchIDPasscodeController event:params:reply:].cold.2
- GCC_except_table124
- GCC_except_table126
- GCC_except_table128
- GCC_except_table137
- GCC_except_table157
- GCC_except_table39
- GCC_except_table44
- GCC_except_table46
- GCC_except_table72
- GCC_except_table83
- GCC_except_table90
- GCC_except_table97
- _OBJC_CLASS_$_BFFPasscodeViewController
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_67
- _OUTLINED_FUNCTION_68
- __OBJC_$_CATEGORY_INSTANCE_METHODS_PSListController_$_Utility
- __OBJC_$_CATEGORY_PSListController_$_Utility
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.544
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.546
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.548
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.549
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.553
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.553.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.555
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.555.cold.1
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.551
- ___132-[PABSPasscodeLockController showLocalAuthenticationPasscodeRemoveFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.538
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506
- ___45-[PABSPasscodeLockController togglePasscode:]_block_invoke.506.cold.1
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.314
- ___47-[PABSFingerprintController deleteFingerprint:]_block_invoke.314.cold.1
- ___47-[PABSPasscodeLockController showKeychainAlert]_block_invoke.713
- ___47-[PABSPearlPasscodeController pushPasscodePane]_block_invoke
- ___47-[PABSPearlPasscodeController pushPasscodePane]_block_invoke_2
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.113
- ___47-[PABSTouchIDPasscodeController addEnrollment:]_block_invoke.113.cold.1
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.309
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke.311
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.312
- ___48-[PABSFingerprintController replaceFingerprint:]_block_invoke_2.312.cold.1
- ___52-[PABSBiometricController useBiometricForSpecifiers]_block_invoke.174
- ___55-[PABSPasscodeLockController setWipeEnabled:specifier:]_block_invoke.683
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864.cold.1
- ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.865
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.201
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.202
- ___62-[PABSBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.203
- ___62-[PABSPearlAttentionGroupController setPearlUnlock:specifier:]_block_invoke.74
- ___62-[PABSPearlAttentionGroupController setPearlUnlock:specifier:]_block_invoke_2
- ___63-[PABSBiometricController setBiometricUnlockEnabled:specifier:]_block_invoke.cold.1
- ___63-[PABSBiometricController setBiometricUnlockEnabled:specifier:]_block_invoke.cold.2
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.607
- ___63-[PABSPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.611
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke.87
- ___67-[PABSBiometricController setTouchIDForPurchasesEnabled:specifier:]_block_invoke_2.88
- ___69-[PABSPasscodeLockController setEnabledInLockScreenForUSB:specifier:]_block_invoke.842
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.279
- ___72-[PABSPearlPasscodeController deleteFaceIDIdentitiesCheckWithSpecifier:]_block_invoke.279.cold.1
- ___82-[PABSFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.291
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.923.cold.1
- ___84-[PABSPasscodeLockController updatePendingVisionUnlockDeviceForSession:forceReload:]_block_invoke.924
- ___85-[PABSPasscodeLockController showAlertForVisionUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.928
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.907
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.911
- ___86-[PABSPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.918
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.932
- ___88-[PABSPasscodeLockController presentVisionUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.933
- ___88-[PABSPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.903
- ___93-[PABSBiometricController presentConfirmationAndProceedTouchIDForStockholmEnabled:specifier:]_block_invoke.124
- ___block_descriptor_tmp.170
- ___block_literal_global.172
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.316
- ___block_literal_global.318
- ___block_literal_global.558
- ___block_literal_global.613
- ___block_literal_global.619
- ___block_literal_global.709
- ___block_literal_global.711
- ___block_literal_global.715
- ___block_literal_global.913
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_shouldUseLocalAuthenticationBasedPasscodeFlowForPINSheetRequest:
- _objc_msgSend$authorizationToken
- _objc_msgSend$setBarStyle:
- _objc_msgSend$setPasscodeCreationDelegate:
- _objc_msgSend$setShadowImage:
- _objc_msgSend$shouldUseLocalAuthenticationBasedPasscodeFlowForChangePasscodeRequests
- _objc_msgSend$shouldUseLocalAuthenticationBasedPasscodeFlowForRemovePasscodeRequests
- _objc_msgSend$systemBackgroundColor
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ " + specifierIdentifierToScrollAndSelect: "
+ "%@: Proceeding to enroll Face ID"
+ "@\"NSBundle\"16@0:8"
+ "@\"PSRootController\"16@0:8"
+ "@\"PSSpecifier\"16@0:8"
+ "@\"UIViewController<PSController>\"16@0:8"
+ "@24@0:8@\"PSSpecifier\"16"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "B20@0:8I16"
+ "B40@0:8@\"NSString\"16@\"NSDictionary\"24^B32"
+ "B40@0:8@16@24^B32"
+ "B48@0:8@\"NSString\"16@\"NSDictionary\"24^B32@?<v@?>40"
+ "B48@0:8@16@24^B32@?40"
+ "Error: Unable to load"
+ "Extracted passcode is invalid or empty"
+ "Failed to extract passcode from authentication context"
+ "Failed to start identity matching: %i"
+ "Fatal error"
+ "HostViewControllerFinder: Capturing root view controller from window"
+ "HostViewControllerFinder: No window root view controller found, using parent directly"
+ "HostViewControllerFinder: Parent view controller changed"
+ "HostViewControllerFinder: Parent view controller removed"
+ "LAContext is nil"
+ "LAUIDelegate [LAEventParamActive]: Failed to extract passcode - %@"
+ "LockedView: Appearing"
+ "LockedView: Disapearing"
+ "Navigation title for Face\u00a0ID & Passcode settings"
+ "Navigation title for Passcode settings"
+ "Navigation title for Touch\u00a0ID & Passcode settings"
+ "No passcode object in specifier"
+ "No root view controller available to present passcode challenge"
+ "PABSPasscodeContextKey"
+ "PABSPasscodeManager: Failed to extract passcode - Error: %@"
+ "PABSPasscodeManager: Failed to extract passcode from context - Error: %@"
+ "PABSPasscodeManager: No passcode context in specifier"
+ "PABSPasscodeManager: No passcode in specifier"
+ "PABSPasscodeManager: Starting passcode extraction from LAContext"
+ "PABSPasscodeManager: Successfully extracted passcode"
+ "PABSPasscodeManager: Successfully extracted passcode from context"
+ "PABSPasscodeManager: Successfully retrieved passcode from specifier"
+ "PSController"
+ "PSStateRestoration"
+ "Passcode Group: Passcode On/Off enablement status [%@] | needsAppleIDAuthWhichNeedsInternet [%@] | isMC [%@] | sdpIsON [%@] | isEnrolledInBiometrics [%@] | parentSpecifier [%@] | canExtractPasscode [%@]"
+ "Passcode authentication failed"
+ "Passcode authentication was cancelled by the user"
+ "Passcode challenge: dismissed after succeeding"
+ "Passcode challenge: presenting sheet now"
+ "Passcode extraction returned nil"
+ "Passcode unevaluated"
+ "Passcode unverified"
+ "Passcode validation: failed with error: '%@'"
+ "Passcode validation: succeeded"
+ "Passcode validation: succeeded, storing the context"
+ "Passcode verification In Progress"
+ "Passcode verification failed"
+ "Passcode verification not needed as we have no passcode set"
+ "Passcode verified"
+ "PasscodeAndBiometricsSettings.HostViewControllerFinder"
+ "PasscodeAndBiometricsSettings/PABSPasscodeVerificationViewModel.swift"
+ "PasscodeAndBiometricsSettings/PABSRootView.swift"
+ "PasscodeContextAdoption"
+ "PasscodeExtraction"
+ "PasscodePaneSpecifier:\n  - identifier: %s\n  - relay: %s\n  - passcode: %s"
+ "PasscodeVerificationStateViewModel: init"
+ "PasscodeVerificationViewModel: deinit"
+ "PasscodeVerificationViewModel: init"
+ "Pearl unlock: Failed to extract passcode - %@"
+ "Pearl unlock: applying settings"
+ "PearlEnrollController: priming with no passcode"
+ "Perform identity matching"
+ "Popping from root view back to the main view"
+ "Proceeding to Add Glasses flow "
+ "Proceeding to Use Mask with Face ID flow"
+ "Received event: LAUIDelegate [LAEventParamActive]"
+ "Refreshing passcode verification status"
+ "SessionID for enabling Vision Pro autounlock device: %@"
+ "Settings.app has been backgrounded!"
+ "Settings.app has been foregrounded!"
+ "T@\"NSString\",N,R"
+ "Touch ID: authContext = nil - No passcode object"
+ "Touch ID: enrollment controller appeared"
+ "Touch ID: enrollment controller dismissed"
+ "Unexpected passcode object type: %@"
+ "UnlockedView: Disapearing"
+ "UnlockedView: Loaded"
+ "_$observationRegistrar"
+ "_TtC29PasscodeAndBiometricsSettings11BundleToken"
+ "_TtC29PasscodeAndBiometricsSettings13PABSConstants"
+ "_TtC29PasscodeAndBiometricsSettings19FeatureFlagsManager"
+ "_TtC29PasscodeAndBiometricsSettings19PABSPasscodeManager"
+ "_TtC29PasscodeAndBiometricsSettings33PABSPasscodeVerificationViewModel"
+ "_TtC29PasscodeAndBiometricsSettings38PABSPasscodeVerificationStateViewModel"
+ "_TtCV29PasscodeAndBiometricsSettings28HostingViewControllerCapture24HostViewControllerFinder"
+ "_createCheckedThrowingContinuation(_:)"
+ "_mustPopToSettingsMainView"
+ "_passcodeVerificationStatus"
+ "com.apple.pabs.passcodemanager"
+ "com.apple.pabs.passcodemanager.specifier"
+ "createLAContext: Creating LAContext with passcode credential"
+ "createLAContext: Failed to create a LAContext with the given passcode"
+ "createLAContext: Failed to encode passcode as UTF-8 data"
+ "createLAContext: Successfully created LAContext with passcode credential"
+ "didLock"
+ "didWake"
+ "enableAutoUnlockForDevice: Failed to extract passcode - %@"
+ "enableForType:withIDSDeviceID:passcodeRef:"
+ "errorWithDomain:code:userInfo:"
+ "extractAndDecodePasscodeFrom:completionHandler:"
+ "extractPasscodeObject"
+ "extractPasscodeObject: Successfully retrieved passcode object from specifier"
+ "extractPasscodeObject: passcode object is nil"
+ "extractPasscodeObject: passcode object is unexpected type: %@"
+ "extractPasscodeObjectFrom:"
+ "extractPasscodeObjectFromSpecifier:"
+ "extractPasscodeStringFrom:completionHandler:"
+ "extractPasscodeStringFromContext: Failed to extract passcode - Error: %@"
+ "extractPasscodeStringFromContext: LAContext is nil"
+ "extractPasscodeStringFromContext: Passcode extraction returned nil without error"
+ "extractPasscodeStringFromContext: Starting passcode extraction from LAContext (blocking)"
+ "extractPasscodeStringFromContext: Successfully extracted passcode"
+ "extractPasscodeStringFromContext:error:"
+ "extractPasscodeStringWithError:"
+ "extractPasscodeStringWithError: Failed to extract passcode - %@"
+ "extractPasscodeStringWithError: No passcode object"
+ "extractPasscodeStringWithError: Unexpected passcodeObject type: %@"
+ "extractPasscodeStringWithError: Using passcode string directly"
+ "faceIDAndPasscode"
+ "formatSearchEntries:parent:"
+ "handleURL:"
+ "handleURL:withCompletion:"
+ "highlightSpecifierWithID:"
+ "init(coder:) has not been implemented"
+ "init(nibName:bundle:)"
+ "isFeatureEnabled:"
+ "localizedDescription"
+ "mustPopToSettingsMainView changed from [%{bool}d] -> [%{bool}d]"
+ "none"
+ "onCapture"
+ "passcodeContextKey"
+ "passcodePaneSpecifier"
+ "passcodeVerificationStatus changed from [%s] -> [%s]"
+ "prepareHandlingURLForSpecifierID:resourceDictionary:animatePush:"
+ "prepareHandlingURLForSpecifierID:resourceDictionary:animatePush:withCompletion:"
+ "previousParent"
+ "primeWithExternalizedAuthContext:"
+ "pushController:"
+ "pushController:animate:"
+ "rootController"
+ "searchBundle"
+ "setBiometricUnlockEnabled: completion invoked"
+ "setBoolValue:forSetting:credentialSet:"
+ "setCredential:type:"
+ "setDismissUIAfterCompletion:"
+ "setFingerprintUnlockAllowed:credentialSet:completionBlock:"
+ "setParentController:"
+ "setRootController:"
+ "setStockholmCompletion: invoked"
+ "setValue:forSetting:credentialSet:"
+ "showController:"
+ "showController:animate:"
+ "specifierIdentifierToScrollAndHighlight"
+ "specifierIdentifierToScrollAndHighlight: "
+ "specifierIdentifierToScrollAndSelect"
+ "specifierQueue"
+ "state"
+ "statusBarWillAnimateByHeight:"
+ "touchIDAndPasscode"
+ "updatePasscodeObject:"
+ "updatePasscodeObject: Removed passcode object for key: %s"
+ "updatePasscodeObject: Successfully set passcode object for key: %s"
+ "updatePasscodeObject: Successfully updated passcode object on specifier"
+ "updatePasscodeObject:passcodePaneSpecifier:"
+ "updatePasscodeObjectFromString:"
+ "updatePasscodeObjectWithString:passcodePaneSpecifier:"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"PSRootController\"16"
+ "v24@0:8@\"PSSpecifier\"16"
+ "v24@0:8@\"UIViewController\"16"
+ "v24@0:8@\"UIViewController<PSController>\"16"
+ "v24@?0@\"LAContext\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v28@0:8@\"UIViewController\"16B24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "v32@0:8@\"NSMutableArray\"16@\"PSSearchEntry\"24"
+ "v32@0:8@\"PSSpecifier\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@16@\"PSSpecifier\"24"
+ "validateSpecifier:"
+ "wasAppBackgroundedObserver"
+ "wasAppForegroundedObserver"
+ "willBecomeActive"
+ "willResignActive"
+ "willUnlock"
- "%@: Showing spinner, proceeding to startWithPasscode"
- "Failed to start matching: %i"
- "FlyingScotsman"
- "LAUIDelegate event: No passcode"
- "LAUIDelegate event: No specifier"
- "Maglev"
- "Passcode Group: Passcode On/Off enablement status [%@] | needsAppleIDAuthWhichNeedsInternet [%@] | isMC [%@] | sdpIsON [%@] | isEnrolledInBiometrics [%@] | parentSpecifier [%@] | retrievedCreds [%@]"
- "Pearl specifiers setup: No passcode"
- "Pearl specifiers setup: No specifier"
- "SeesionID for enabling Vision Pro autounlock device: %@"
- "SpringBoard"
- "Touch ID: authContext = nil - No passcode"
- "_shouldUseLocalAuthenticationBasedPasscodeFlowForPINSheetRequest:"
- "authorizationToken"
- "authorizationToken: No passcode"
- "authorizationToken: No specifier"
- "enableAutoUnlockForDevice: No passcode"
- "enableAutoUnlockForDevice: No specifier"
- "enableVisionUnlockForDevice: No passcode"
- "enableVisionUnlockForDevice: No specifier"
- "proceedToEnrollGlassesForExistingAppearance: No passcode"
- "proceedToEnrollGlassesForExistingAppearance: No specifier"
- "proceedToEnrollPeriocularForExistingAppearance: No passcode"
- "proceedToEnrollPeriocularForExistingAppearance: No specifier"
- "proceedToEnrollWithSpecifier: No passcode"
- "proceedToEnrollWithSpecifier: No specifier"
- "proceedTouchIDForStockholmEnabled: No passcode"
- "proceedTouchIDForStockholmEnabled: No specifier"
- "setBarStyle:"
- "setBiometricUnlockEnabled: No passcode"
- "setBiometricUnlockEnabled: No specifier"
- "setGraceValue: No passcode"
- "setGraceValue: No specifier"
- "setPasscodeCreationDelegate:"
- "setShadowImage:"
- "shouldUseLocalAuthenticationBasedPasscodeFlowForChangePasscodeRequests"
- "shouldUseLocalAuthenticationBasedPasscodeFlowForRemovePasscodeRequests"
- "systemBackgroundColor"

```
