## CoreCDPUI

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

-359.4.6.0.0
-  __TEXT.__text: 0x44bd4
-  __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_methlist: 0x2bd4
-  __TEXT.__const: 0x1244
-  __TEXT.__cstring: 0x3e18
-  __TEXT.__oslogstring: 0x26de
-  __TEXT.__gcc_except_tab: 0x9b4
+359.13.0.0.0
+  __TEXT.__text: 0x4499c
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_methlist: 0x2c0c
+  __TEXT.__const: 0x1304
+  __TEXT.__cstring: 0x3fa8
+  __TEXT.__oslogstring: 0x259b
+  __TEXT.__gcc_except_tab: 0x824
   __TEXT.__dlopen_cstrs: 0x230
-  __TEXT.__constg_swiftt: 0x820
-  __TEXT.__swift5_typeref: 0x37a8
+  __TEXT.__constg_swiftt: 0x864
+  __TEXT.__swift5_typeref: 0x3820
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x510
-  __TEXT.__swift5_fieldmd: 0x46c
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_reflstr: 0x530
+  __TEXT.__swift5_fieldmd: 0x488
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_capture: 0x190
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x134c
+  __TEXT.__unwind_info: 0x1340
   __TEXT.__objc_classname: 0xbce
-  __TEXT.__objc_methname: 0xa53b
-  __TEXT.__objc_methtype: 0x28b9
-  __TEXT.__objc_stubs: 0x7aa0
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x10c0
+  __TEXT.__objc_methname: 0xa717
+  __TEXT.__objc_methtype: 0x2901
+  __TEXT.__objc_stubs: 0x79c0
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe2e8
-  __DATA_CONST.__objc_selrefs: 0x2410
-  __AUTH_CONST.__cfstring: 0x2580
+  __DATA_CONST.__objc_const: 0xe318
+  __DATA_CONST.__objc_selrefs: 0x2400
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x4f0
+  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_catlist2: 0x8
+  __AUTH_CONST.__cfstring: 0x2420
   __AUTH_CONST.__objc_const: 0x1390
-  __AUTH_CONST.__const: 0x11b0
-  __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__auth_got: 0x9e8
+  __AUTH_CONST.__const: 0x12b0
+  __AUTH_CONST.__auth_ptr: 0x68
+  __AUTH_CONST.__auth_got: 0xa88
   __AUTH.__objc_data: 0x1a50
-  __AUTH.__data: 0x5b0
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x4f8
-  __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x34c
-  __DATA.__data: 0x1428
+  __AUTH.__data: 0x5a0
+  __DATA.__objc_ivar: 0x350
+  __DATA.__data: 0x1808
   __DATA.__objc_stublist: 0x8
-  __DATA.__objc_catlist2: 0x8
-  __DATA.__bss: 0xb50
-  __DATA.__common: 0x38
+  __DATA.__bss: 0xa60
+  __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1815
-  Symbols:   5455
+  Functions: 1840
+  Symbols:   5425
   CStrings:  2683
 
Symbols:
+ -[CDPQuotaStorageAppListRequest initWithAccount:isWalrusEnabled:]
+ -[CDPRecoveryKeyEntryViewController handleRecoveryKeyEscapeDuringDataRecoveryFlow:].cold.1
+ -[CDPRecoveryKeyEntryViewController handleRecoveryKeyEscapeDuringDataRecoveryFlow:].cold.2
+ -[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:]
+ -[CDPUIAccountRecoveryController _presentRemoteSecretControllerWithNewestDevice:]
+ -[CDPUICodeEntryPane preferredContentSize]
+ -[CDPUIController _beginCustodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:]
+ -[CDPUIController _custodianAskHelpViewControllerWithSupportedEscapeOfferMask:]
+ -[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]
+ -[CDPUIController _custodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:]
+ -[CDPUIController _custodianResetProtectedDataEscapeOfferWithSupportedEscapeOffers:]
+ -[CDPUIController _deviceLimitOfferCustodianForDevice:supportedEscapeOfferMask:]
+ -[CDPUIController _deviceLimitOfferDeviceSelectionForDevice:]
+ -[CDPUIController _deviceLimitOfferRecoveryKeyForDevice:supportedEscapeOfferMask:]
+ -[CDPUIController _deviceLimitOfferSkipForDevice:]
+ -[CDPUIController _disableUserInteractionAndStartSpinner]
+ -[CDPUIController _enableUserInteractionAndStopSpinner]
+ -[CDPUIController _enterCustodianCodeEscapeOfferWithCustodianController:supportedEscapeOfferMask:]
+ -[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:]
+ -[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:presentationBlock:]
+ -[CDPUIController _handleDepletedRemainingAttemptsForDevice:mask:]
+ -[CDPUIController _instructionsControllerForPlatform:controller:supportedEscapeOfferMask:]
+ -[CDPUIController _recoveryKeyEscapeOfferWithSupportedEscapeOfferMask:]
+ -[CDPUIController _recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:]
+ -[CDPUIController _recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:presentationBlock:]
+ -[CDPUIController _recoveryKeyResetProtectedDataEscapeOfferWithSupportedEscapeOffers:]
+ -[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]
+ -[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:].cold.1
+ -[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:].cold.2
+ -[CDPUIController _tryAgainLaterEscapeOption]
+ -[CDPUIController custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:]
+ -[CDPUIController presentDeviceSelection:]
+ -[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:]
+ GCC_except_table102
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table15
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table164
+ GCC_except_table168
+ GCC_except_table180
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table96
+ _AKTrueValue
+ _OBJC_IVAR_$_CDPQuotaStorageAppListRequest._isWalrusEnabled
+ ___102-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:]_block_invoke
+ ___102-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:]_block_invoke.333
+ ___102-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:]_block_invoke.340
+ ___102-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:]_block_invoke_2
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.504
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.509
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.509.cold.1
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.513
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.513.cold.1
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.520
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.520.cold.1
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.524
+ ___112-[CDPUIController _skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:]_block_invoke.cold.1
+ ___117-[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:presentationBlock:]_block_invoke
+ ___45-[CDPUIController _tryAgainLaterEscapeOption]_block_invoke
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.542
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.542.cold.1
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.542.cold.2
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.542.cold.3
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.542.cold.4
+ ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.544
+ ___59-[CDPUIController _enterSecretLaterEscapeOptionWithSecret:]_block_invoke.423
+ ___59-[CDPUIController _iCloudDeleteConfirmationViewController:]_block_invoke.561
+ ___61-[CDPRecoveryKeyEntryViewController handleForgotRecoveryKey:]_block_invoke.102
+ ___61-[CDPRecoveryKeyEntryViewController handleForgotRecoveryKey:]_block_invoke.102.cold.1
+ ___61-[CDPUIController _deviceLimitOfferDeviceSelectionForDevice:]_block_invoke
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.170
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.172
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.174
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.173
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.173.cold.1
+ ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.183
+ ___68-[CDPUIController keychainSyncController:didFinishWithResult:error:]_block_invoke.501
+ ___68-[CDPUIController keychainSyncController:didFinishWithResult:error:]_block_invoke.503
+ ___71-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:]_block_invoke
+ ___71-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:]_block_invoke_2
+ ___71-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:]_block_invoke_3
+ ___71-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:]_block_invoke_4
+ ___72-[CDPUIController _recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:]_block_invoke
+ ___73-[CDPUIController _showTryAgainLaterConfirmationAlertWithViewController:]_block_invoke.482
+ ___74-[CDPRemoteSecretEntryViewController _handleSecretValidationWithPasscode:]_block_invoke.33.cold.4
+ ___76-[CDPRecoveryKeyEntryViewController skipRecoveryKeyDuringPasswordResetFlow:]_block_invoke.86
+ ___76-[CDPRecoveryKeyEntryViewController skipRecoveryKeyDuringPasswordResetFlow:]_block_invoke.86.cold.1
+ ___78-[CDPUIController _custodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:]_block_invoke
+ ___83-[CDPRecoveryKeyEntryViewController _handleRecoveryKeyValidationWithSuccess:error:]_block_invoke.120
+ ___83-[CDPUIController _beginCustodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:]_block_invoke
+ ___90-[CDPUIController _instructionsControllerForPlatform:controller:supportedEscapeOfferMask:]_block_invoke
+ ___90-[CDPUIController _recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:presentationBlock:]_block_invoke
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.394
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.394.cold.1
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.395
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.395.cold.1
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.396
+ ___92-[CDPUIController _custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:]_block_invoke.cold.1
+ ___94-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:]_block_invoke
+ ___94-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:]_block_invoke_2
+ ___94-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:]_block_invoke_3
+ ___99-[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e21_v24?0"NSString"8Q16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e8_v16?0Q8lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e42_v32?0"<NSCopying>"8"NSArray"16?<v?>24lr56l8s32l8s48l8s40l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0lr64l8s32l8s40l8s56l8s48l8r72l8
+ ___block_literal_global.332
+ ___block_literal_global.532
+ ___block_literal_global.546
+ ___swift_memcpy25_8
+ _associated conformance 9CoreCDPUI19DisclosureIndicatorV7SwiftUI4ViewAA4BodyAdEP_AdE
+ _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA4TextV_AA6SpacerVAA15ModifiedContentVyAA6ButtonVyAEyAGSg_AKyAA08ProgressE0VyAA05EmptyE0VARGAA14_PaddingLayoutVGSg9CoreCDPUI19DisclosureIndicatorVtGGAA010_FixedSizeN0VGtGGAA0E0HPyHC.15
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE13symbolVariantyQrAA14SymbolVariantsVFQOyAA15ModifiedContentVyAHyAHyAHyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAJ5ScaleOGGALyAA4FontVSgGGAA016_ForegroundStyleN0VyAA017HierarchicalShapeR0VGGAA14_PaddingLayoutVG_Qo_HO.6
+ _objc_msgSend$_accountRecoveryEscapeOfferForDevice:
+ _objc_msgSend$_beginCustodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:
+ _objc_msgSend$_custodianAskHelpViewControllerWithSupportedEscapeOfferMask:
+ _objc_msgSend$_custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:
+ _objc_msgSend$_custodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:
+ _objc_msgSend$_custodianResetProtectedDataEscapeOfferWithSupportedEscapeOffers:
+ _objc_msgSend$_deviceLimitOfferCustodianForDevice:supportedEscapeOfferMask:
+ _objc_msgSend$_deviceLimitOfferDeviceSelectionForDevice:
+ _objc_msgSend$_deviceLimitOfferRecoveryKeyForDevice:supportedEscapeOfferMask:
+ _objc_msgSend$_deviceLimitOfferSkipForDevice:
+ _objc_msgSend$_enterCustodianCodeEscapeOfferWithCustodianController:supportedEscapeOfferMask:
+ _objc_msgSend$_enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:
+ _objc_msgSend$_enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:presentationBlock:
+ _objc_msgSend$_handleDepletedRemainingAttemptsForDevice:mask:
+ _objc_msgSend$_instructionsControllerForPlatform:controller:supportedEscapeOfferMask:
+ _objc_msgSend$_recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:
+ _objc_msgSend$_recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:presentationBlock:
+ _objc_msgSend$_recoveryKeyResetProtectedDataEscapeOfferWithSupportedEscapeOffers:
+ _objc_msgSend$_skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:
+ _objc_msgSend$_supportsCustodianRecovery
+ _objc_msgSend$_tryAgainLaterEscapeOption
+ _objc_msgSend$custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:
+ _objc_msgSend$initWithAccount:isWalrusEnabled:
+ _objc_msgSend$presentDeviceSelection:
+ _objc_msgSend$recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:
+ _swift_getAtKeyPath
+ _swift_initStaticObject
+ _symbolic _____ 7SwiftUI5ImageV5ScaleO
+ _symbolic _____ 9CoreCDPUI19DisclosureIndicatorV
+ _symbolic _____Sg 7SwiftUI4FontV6DesignO
+ _symbolic _____Sg______y_____y_____AEG_____GSg_____t 7SwiftUI4TextV AA15ModifiedContentV AA12ProgressViewV AA05EmptyG0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV
+ _symbolic ________________y_____y_____yAASg_ACy_____y_____AHG_____GSg_____tGG_____Gt 7SwiftUI4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA9TupleViewV AA08ProgressI0V AA05EmptyI0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV AA010_FixedSizeM0V
+ _symbolic _____yAAyAAyAAy__________y_____GGACy_____SgGG_____y_____GG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AE5ScaleO AA4FontV AA016_ForegroundStyleI0V AA017HierarchicalShapeM0V AA14_PaddingLayoutV
+ _symbolic _____yAAyAAy__________y_____GGACy_____SgGG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AE5ScaleO AA4FontV AA016_ForegroundStyleI0V AA017HierarchicalShapeM0V
+ _symbolic _____yAAy__________y_____GGACy_____SgGG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AE5ScaleO AA4FontV
+ _symbolic _____ySbG 7SwiftUI11EnvironmentV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 12CoreGraphics7CGFloatV
+ _symbolic _____y_____G 7SwiftUI24_ForegroundStyleModifierV AA017HierarchicalShapeD0V
+ _symbolic _____y_____G 7SwiftUI30_EnvironmentKeyWritingModifierV AA5ImageV5ScaleO
+ _symbolic _____y_____Sg______y_____y_____AFG_____GSg_____tG 7SwiftUI9TupleViewV AA4TextV AA15ModifiedContentV AA08ProgressD0V AA05EmptyD0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV
+ _symbolic _____y___________y________________y_____yACyADSg_AFy_____y_____AJG_____GSg_____tGG_____GtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA08ProgressD0V AA05EmptyD0V AA08_PaddingG0V 9CoreCDPUI19DisclosureIndicatorV AA010_FixedSizeG0V
+ _symbolic _____y__________y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AE5ScaleO
+ _symbolic _____y_____yAAyAAyAAy__________y_____GGACy_____SgGG_____y_____GG_____G_Qo_ 7SwiftUI4ViewPAAE13symbolVariantyQrAA14SymbolVariantsVFQO AA15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AJ5ScaleO AA4FontV AA016_ForegroundStyleN0V AA017HierarchicalShapeR0V AA14_PaddingLayoutV
+ _symbolic _____y_____y_____Sg______y_____y_____AGG_____GSg_____tGG 7SwiftUI6ButtonV AA9TupleViewV AA4TextV AA15ModifiedContentV AA08ProgressE0V AA05EmptyE0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV
+ _symbolic _____y_____y________________y_____yAByACSg_AEy_____y_____AIG_____GSg_____tGG_____GtGG 7SwiftUI6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA08ProgressE0V AA05EmptyE0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV AA010_FixedSizeN0V
+ _symbolic _____y_____y_____y_____Sg_AAy_____y_____AGG_____GSg_____tGG_____G 7SwiftUI15ModifiedContentV AA6ButtonV AA9TupleViewV AA4TextV AA08ProgressG0V AA05EmptyG0V AA14_PaddingLayoutV 9CoreCDPUI19DisclosureIndicatorV AA010_FixedSizeL0V
- -[CDPQuotaStorageAppListRequest initWithAccount:]
- -[CDPRecoveryKeyEntryViewController _resetEncryptedDataEscapeOptionForAlert:]
- -[CDPRecoveryKeyEntryViewController _tryAgainLaterEscapeOptionForAlert:]
- -[CDPRecoveryKeyEntryViewModel isFooterButtonForOtherRecoveryOptions]
- -[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:cdpContext:]
- -[CDPUIAccountRecoveryController _presentRemoteSecretControllerWithNewestDevice:cdpContext:]
- -[CDPUIController _custodianAskHelpViewController]
- -[CDPUIController _custodianCodeEntryViewControllerWithController:]
- -[CDPUIController _custodianRecoveryEscapeOption]
- -[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]
- -[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:].cold.1
- -[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:].cold.2
- -[CDPUIController _deviceLimitOfferForDevice:]
- -[CDPUIController _enterCustodianCodeEscapeOfferWithCustodianController:]
- -[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:]
- -[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:presentationBlock:]
- -[CDPUIController _escapeOfferForCustodianFlowWithMask:]
- -[CDPUIController _instructionsControllerForPlatform:controller:]
- -[CDPUIController _recoveryKeyEscapeOffer]
- -[CDPUIController _recoveryKeyEscapeOptionWithPresentationBlock:]
- -[CDPUIController _recoveryKeyEscapeOption]
- -[CDPUIController _resetAccountDataEscapeOption]
- -[CDPUIController _walrusBeginCustodianRecoveryEscapeOption]
- -[CDPUIController _walrusEscapeOfferForDevice:withMask:]
- -[CDPUIController _walrusEscapeOffersForgotAllWithMask:presenter:devices:]
- -[CDPUIController custodianOSSelectionViewControllerWithCustodianController:]
- -[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]
- GCC_except_table100
- GCC_except_table101
- GCC_except_table103
- GCC_except_table107
- GCC_except_table109
- GCC_except_table112
- GCC_except_table117
- GCC_except_table119
- GCC_except_table124
- GCC_except_table135
- GCC_except_table137
- GCC_except_table139
- GCC_except_table148
- GCC_except_table153
- GCC_except_table160
- GCC_except_table165
- GCC_except_table178
- GCC_except_table184
- GCC_except_table188
- GCC_except_table19
- GCC_except_table22
- GCC_except_table86
- GCC_except_table92
- GCC_except_table97
- _OBJC_CLASS_$_LSApplicationWorkspace
- __CDPUIBeneficiaryWelcomeTableRowHeight
- ___43-[CDPUIController _recoveryKeyEscapeOption]_block_invoke
- ___46-[CDPUIController _deviceLimitOfferForDevice:]_block_invoke
- ___46-[CDPUIController _deviceLimitOfferForDevice:]_block_invoke_2
- ___46-[CDPUIController _deviceLimitOfferForDevice:]_block_invoke_3
- ___48-[CDPUIController _resetAccountDataEscapeOption]_block_invoke
- ___48-[CDPUIController _resetAccountDataEscapeOption]_block_invoke.300
- ___48-[CDPUIController _resetAccountDataEscapeOption]_block_invoke.315
- ___48-[CDPUIController _resetAccountDataEscapeOption]_block_invoke.321
- ___48-[CDPUIController _resetAccountDataEscapeOption]_block_invoke.321.cold.1
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.575
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.575.cold.1
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.575.cold.2
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.575.cold.3
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.575.cold.4
- ___48-[CDPUIController _showQuotaStorageAppListView:]_block_invoke.577
- ___49-[CDPUIController _custodianRecoveryEscapeOption]_block_invoke
- ___56-[CDPUIController _escapeOfferForCustodianFlowWithMask:]_block_invoke
- ___56-[CDPUIController _escapeOfferForCustodianFlowWithMask:]_block_invoke_2
- ___56-[CDPUIController _walrusEscapeOfferForDevice:withMask:]_block_invoke
- ___57-[CDPUIController _escapeOfferForSingleApprovalWithMask:]_block_invoke
- ___57-[CDPUIController _escapeOfferForSingleApprovalWithMask:]_block_invoke_2
- ___59-[CDPUIController _enterSecretLaterEscapeOptionWithSecret:]_block_invoke.473
- ___59-[CDPUIController _iCloudDeleteConfirmationViewController:]_block_invoke.590
- ___60-[CDPUIController _walrusBeginCustodianRecoveryEscapeOption]_block_invoke
- ___61-[CDPRecoveryKeyEntryViewController handleForgotRecoveryKey:]_block_invoke.124
- ___61-[CDPRecoveryKeyEntryViewController handleForgotRecoveryKey:]_block_invoke.124.cold.1
- ___65-[CDPUIController _instructionsControllerForPlatform:controller:]_block_invoke
- ___65-[CDPUIController _recoveryKeyEscapeOptionWithPresentationBlock:]_block_invoke
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.168
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.171
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.173
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.172
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.172.cold.1
- ___65-[CDPUIController cdpContext:promptForLocalSecretWithCompletion:]_block_invoke_2.182
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.439
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.439.cold.1
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.440
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.440.cold.1
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.441
- ___67-[CDPUIController _custodianCodeEntryViewControllerWithController:]_block_invoke.cold.1
- ___68-[CDPUIController keychainSyncController:didFinishWithResult:error:]_block_invoke.538
- ___68-[CDPUIController keychainSyncController:didFinishWithResult:error:]_block_invoke.540
- ___69-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]_block_invoke
- ___69-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]_block_invoke_2
- ___69-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]_block_invoke_3
- ___69-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]_block_invoke_4
- ___69-[CDPUIController recoveryKeyEntryControllerForCircleJoinWithCancel:]_block_invoke_5
- ___72-[CDPRecoveryKeyEntryViewController _tryAgainLaterEscapeOptionForAlert:]_block_invoke
- ___72-[CDPRecoveryKeyEntryViewController _tryAgainLaterEscapeOptionForAlert:]_block_invoke.88
- ___72-[CDPRecoveryKeyEntryViewController _tryAgainLaterEscapeOptionForAlert:]_block_invoke.88.cold.1
- ___72-[CDPRecoveryKeyEntryViewController _tryAgainLaterEscapeOptionForAlert:]_block_invoke.cold.1
- ___72-[CDPUIController remoteSecretEntry:depletedRemainingAttemptsForDevice:]_block_invoke
- ___73-[CDPUIController _showTryAgainLaterConfirmationAlertWithViewController:]_block_invoke.522
- ___74-[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:]_block_invoke
- ___74-[CDPUIController _walrusEscapeOffersForgotAllWithMask:presenter:devices:]_block_invoke
- ___76-[CDPRecoveryKeyEntryViewController skipRecoveryKeyDuringPasswordResetFlow:]_block_invoke.108
- ___76-[CDPRecoveryKeyEntryViewController skipRecoveryKeyDuringPasswordResetFlow:]_block_invoke.108.cold.1
- ___77-[CDPRecoveryKeyEntryViewController _resetEncryptedDataEscapeOptionForAlert:]_block_invoke
- ___77-[CDPRecoveryKeyEntryViewController _resetEncryptedDataEscapeOptionForAlert:]_block_invoke.95
- ___77-[CDPRecoveryKeyEntryViewController _resetEncryptedDataEscapeOptionForAlert:]_block_invoke.95.cold.1
- ___77-[CDPRecoveryKeyEntryViewController _resetEncryptedDataEscapeOptionForAlert:]_block_invoke.cold.1
- ___77-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:]_block_invoke
- ___77-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:]_block_invoke.364
- ___77-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:]_block_invoke.371
- ___77-[CDPUIController custodianOSSelectionViewControllerWithCustodianController:]_block_invoke_2
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.541
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.546
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.546.cold.1
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.550
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.550.cold.1
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.557
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.557.cold.1
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.561
- ___81-[CDPUIController _deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:]_block_invoke.cold.1
- ___82-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:cdpContext:]_block_invoke
- ___82-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:cdpContext:]_block_invoke_2
- ___82-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:cdpContext:]_block_invoke_3
- ___82-[CDPUIAccountRecoveryController _accountRecoveryEscapeOfferForDevice:cdpContext:]_block_invoke_4
- ___83-[CDPRecoveryKeyEntryViewController _handleRecoveryKeyValidationWithSuccess:error:]_block_invoke.142
- ___83-[CDPRecoveryKeyEntryViewController handleRecoveryKeyEscapeDuringDataRecoveryFlow:]_block_invoke
- ___92-[CDPUIController _enterCustodianCodeEscapeOptionWithCustodianController:presentationBlock:]_block_invoke
- ___block_descriptor_40_e8_32bs_e21_v24?0"NSString"8Q16ls32l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e36_v24?0"CDPLocalSecret"8"NSError"16ls32l8s40l8w48l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8s32l8w48l8
- ___block_descriptor_64_e8_32s40bs48r56r_e42_v32?0"<NSCopying>"8"NSArray"16?<v?>24lr48l8s40l8s32l8r56l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8s48l8s40l8r64l8
- ___block_literal_global.363
- ___block_literal_global.565
- ___block_literal_global.579
- _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA4TextV_AA6SpacerVAA15ModifiedContentVyAA6ButtonVyAEyAGSg_AKyAA08ProgressE0VyAA05EmptyE0VARGAA14_PaddingLayoutVGSgAKyAKyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGA_yAA5ColorVSgGGtGGAA010_FixedSizeN0VGtGGAA0E0HPyHC.17
- _iconSize
- _keypath_set.32Tm
- _objc_msgSend$_accountRecoveryEscapeOfferForDevice:cdpContext:
- _objc_msgSend$_custodianAskHelpViewController
- _objc_msgSend$_custodianCodeEntryViewControllerWithController:
- _objc_msgSend$_custodianRecoveryEscapeOption
- _objc_msgSend$_deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:
- _objc_msgSend$_deviceLimitOfferForDevice:
- _objc_msgSend$_enterCustodianCodeEscapeOfferWithCustodianController:
- _objc_msgSend$_enterCustodianCodeEscapeOptionWithCustodianController:
- _objc_msgSend$_enterCustodianCodeEscapeOptionWithCustodianController:presentationBlock:
- _objc_msgSend$_escapeOfferForCustodianFlowWithMask:
- _objc_msgSend$_instructionsControllerForPlatform:controller:
- _objc_msgSend$_recoveryKeyEscapeOffer
- _objc_msgSend$_recoveryKeyEscapeOption
- _objc_msgSend$_recoveryKeyEscapeOptionWithPresentationBlock:
- _objc_msgSend$_resetAccountDataEscapeOption
- _objc_msgSend$_resetEncryptedDataEscapeOptionForAlert:
- _objc_msgSend$_showTryAgainLaterConfirmationAlertWithViewController:
- _objc_msgSend$_tryAgainLaterEscapeOptionForAlert:
- _objc_msgSend$_walrusBeginCustodianRecoveryEscapeOption
- _objc_msgSend$_walrusEscapeOfferForDevice:withMask:
- _objc_msgSend$_walrusEscapeOffersForgotAllWithMask:presenter:devices:
- _objc_msgSend$custodianOSSelectionViewControllerWithCustodianController:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$dismissAndResetAccountCDPState:localSecret:
- _objc_msgSend$dismissOfferAnimated:completion:
- _objc_msgSend$initWithAccount:
- _objc_msgSend$isFooterButtonForOtherRecoveryOptions
- _objc_msgSend$isSOSCFUFlow
- _objc_msgSend$openURL:withOptions:
- _objc_msgSend$recoveryKeyEntryControllerForCircleJoinWithCancel:
- _objc_msgSend$setProgressLabel:
- _objc_msgSend$setProgressTitle:
- _swift_bridgeObjectRetain_n
- _symbolic _____Sg______y_____y_____AEG_____GSgACyACy__________y_____SgGGAKy_____SgGGt 7SwiftUI4TextV AA15ModifiedContentV AA12ProgressViewV AA05EmptyG0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic ________________y_____y_____yAASg_ACy_____y_____AHG_____GSgACyACy__________y_____SgGGANy_____SgGGtGG_____Gt 7SwiftUI4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA9TupleViewV AA08ProgressI0V AA05EmptyI0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AA010_FixedSizeM0V
- _symbolic _____y_____Sg______y_____y_____AFG_____GSgADyADy__________y_____SgGGALy_____SgGGtG 7SwiftUI9TupleViewV AA4TextV AA15ModifiedContentV AA08ProgressD0V AA05EmptyD0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y___________y________________y_____yACyADSg_AFy_____y_____AJG_____GSgAFyAFy__________y_____SgGGAPy_____SgGGtGG_____GtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA08ProgressD0V AA05EmptyD0V AA08_PaddingG0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AA010_FixedSizeG0V
- _symbolic _____y_____y_____Sg______y_____y_____AGG_____GSgAEyAEy__________y_____SgGGAMy_____SgGGtGG 7SwiftUI6ButtonV AA9TupleViewV AA4TextV AA15ModifiedContentV AA08ProgressE0V AA05EmptyE0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____y________________y_____yAByACSg_AEy_____y_____AIG_____GSgAEyAEy__________y_____SgGGAOy_____SgGGtGG_____GtGG 7SwiftUI6HStackV AA9TupleViewV AA4TextV AA6SpacerV AA15ModifiedContentV AA6ButtonV AA08ProgressE0V AA05EmptyE0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AA010_FixedSizeN0V
- _symbolic _____y_____y_____y_____Sg_AAy_____y_____AGG_____GSgAAyAAy__________y_____SgGGAMy_____SgGGtGG_____G 7SwiftUI15ModifiedContentV AA6ButtonV AA9TupleViewV AA4TextV AA08ProgressG0V AA05EmptyG0V AA14_PaddingLayoutV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AA010_FixedSizeL0V
CStrings:
+ "\"Delegate is nil when trying to presentDeviceSelection\""
+ "\"Device limit reached, but other devices are available, show device selection screen\""
+ "\"cdpContextType = %ld\""
+ "\"iOS: Sending error %ld because user doesnt have their RK and has custodian recovery available.\""
+ "@28@0:8@16B24"
+ "@28@0:8B16Q20"
+ "@32@0:8Q16@?24"
+ "@40@0:8@16Q24@?32"
+ "@40@0:8Q16@24Q32"
+ "@48@0:8@16@24@32Q40"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "DATA_RECOVERY_CUSTODIAN_SKIP_MESSAGE"
+ "DATA_RECOVERY_CUSTODIAN_SKIP_TITLE"
+ "DATA_RECOVERY_DEVICE_SELECTION_SKIP_MESSAGE"
+ "DATA_RECOVERY_DEVICE_SELECTION_SKIP_TITLE"
+ "DATA_RECOVERY_ESCAPE_OPTION_SKIP"
+ "DATA_RECOVERY_RECOVERY_KEY_SKIP_MESSAGE"
+ "DATA_RECOVERY_RECOVERY_KEY_SKIP_TITLE"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "REMOTE_SECRET_RECOVERY_HARD_LIMIT_CHOOSE_DEVICE"
+ "REMOTE_SECRET_RECOVERY_HARD_LIMIT_LAST_DEVICE_CUSTODIAN"
+ "REMOTE_SECRET_RECOVERY_HARD_LIMIT_LAST_DEVICE_RECOVERY_KEY"
+ "REMOTE_SECRET_RECOVERY_HARD_LIMIT_LAST_DEVICE_RESET"
+ "REMOTE_SECRET_RECOVERY_HARD_LIMIT_LAST_DEVICE_SKIP"
+ "REMOTE_SECRET_RECOVERY_LIMIT_CHOOSE_ANOTHER_DEVICE"
+ "REMOTE_SECRET_RECOVERY_LIMIT_TRY_AGAIN_LATER"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "Tq,?,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_accountRecoveryEscapeOfferForDevice:"
+ "_beginCustodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:"
+ "_custodianAskHelpViewControllerWithSupportedEscapeOfferMask:"
+ "_custodianCodeEntryViewControllerWithController:supportedEscapeOfferMask:"
+ "_custodianRecoveryEscapeOptionWithSupportedEscapeOfferMask:"
+ "_custodianResetProtectedDataEscapeOfferWithSupportedEscapeOffers:"
+ "_deviceLimitOfferCustodianForDevice:supportedEscapeOfferMask:"
+ "_deviceLimitOfferDeviceSelectionForDevice:"
+ "_deviceLimitOfferRecoveryKeyForDevice:supportedEscapeOfferMask:"
+ "_deviceLimitOfferSkipForDevice:"
+ "_enterCustodianCodeEscapeOfferWithCustodianController:supportedEscapeOfferMask:"
+ "_enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:"
+ "_enterCustodianCodeEscapeOptionWithCustodianController:supportedEscapeOfferMask:presentationBlock:"
+ "_handleDepletedRemainingAttemptsForDevice:mask:"
+ "_instructionsControllerForPlatform:controller:supportedEscapeOfferMask:"
+ "_recoveryKeyEscapeOfferWithSupportedEscapeOfferMask:"
+ "_recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:"
+ "_recoveryKeyEscapeOptionWithSupportedEscapeOfferMask:presentationBlock:"
+ "_recoveryKeyResetProtectedDataEscapeOfferWithSupportedEscapeOffers:"
+ "_skipOrDeleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:supportedEscapeOfferMask:"
+ "_supportsCustodianRecovery"
+ "_tryAgainLaterEscapeOption"
+ "cdpuicontroller"
+ "custodianOSSelectionViewControllerWithCustodianController:supportedEscapeOfferMask:"
+ "initWithAccount:isWalrusEnabled:"
+ "invalid Collection: less than 'count' elements in collection"
+ "presentDeviceSelection:"
+ "recoveryKeyEntryControllerForCircleJoinWithCancel:supportedEscapeOfferMask:"
+ "x-apple-storageapplist-nadp"
- "\"Context is footer button for other recovery options\""
- "\"Device limit reached, but recovery key is available, show escape options\""
- "\"Hard limit reached\""
- "\"User elected to learn more\""
- "\"User elected to reset CDP flow, prompting to confirm\""
- "\"Walrus enabled = %d, mode = %d\""
- "\"Walrus enabled account, has neither RK nor RC.\""
- "\"delete icloud escape offer = %@\""
- "\"iOS: Sending error %ld because user chose to RPD.\""
- "\"iOS: User chose to reset encrypted data.\""
- "\"iOS: User chose to try RK later.\""
- "\"iOS: User in data recovery flow says that they dont have their RK. Presenting the skip recovery alert.\""
- "@20@0:8B16"
- "@32@0:8@16@?24"
- "IOS_RESET_CONFIRMATION_DIALOGUE_BUTTON_LEARN_MORE_URL"
- "REMOTE_SECRET_ENTRY_DEVICE_LIMIT"
- "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_MESSAGE_ANOTHER_DEVICE_RESET"
- "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_MESSAGE_ANOTHER_DEVICE_RK"
- "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_MESSAGE_RK"
- "REMOTE_SECRET_ENTRY_FORGOT_CODE_DIALOG_RESET"
- "RESET_CONFIRMATION_DIALOGUE_BUTTON_LEARN_MORE"
- "RESET_CONFIRMATION_DIALOG_BUTTON_RESET"
- "RESET_CONFIRMATION_DIALOG_MESSAGE"
- "RESET_CONFIRMATION_DIALOG_TITLE"
- "RK_ALERT_ACTION_RESET_DATA"
- "RK_ALERT_BODY_RESET_DATA"
- "SINGLE_ICSC_RESETTING_PROGRESS_LABEL"
- "SINGLE_ICSC_RESETTING_TITLE"
- "SKIP_RK_ALERT_ACTION_TRY_AGAIN_LATER"
- "SKIP_RK_ALERT_BODY_JOIN_LATER"
- "T@\"NSString\",C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "TB,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "WALRUS_ALERT_BUTTON_TITLE_ASK_SOMEONE_ELSE"
- "WALRUS_ALERT_BUTTON_TITLE_TRY_AGAIN_LATER"
- "WALRUS_ALERT_MESSAGE_CANT_GET_RECOVERY_CODE"
- "WALRUS_ALERT_MESSAGE_DONT_ASK_FOR_HELP"
- "WALRUS_ALERT_MESSAGE_HAVING_TROUBLE"
- "WALRUS_ALERT_MESSAGE_NO_RECOVERY_KEY"
- "WALRUS_ALERT_TITLE_CANT_GET_RECOVERY_CODE"
- "WALRUS_ALERT_TITLE_HAVING_TROUBLE"
- "WALRUS_ALERT_TITLE_NO_RECOVERY_KEY"
- "WALRUS_BUTTON_TITLE_CANT_REACH_RECOVERY_CONTACT"
- "WALRUS_BUTTON_TITLE_NO_RECOVERY_KEY"
- "_accountRecoveryEscapeOfferForDevice:cdpContext:"
- "_custodianAskHelpViewController"
- "_custodianCodeEntryViewControllerWithController:"
- "_deleteiCloudDataEscapeOfferWithTitle:message:skipButtonTitle:"
- "_deviceLimitOfferForDevice:"
- "_enterCustodianCodeEscapeOfferWithCustodianController:"
- "_enterCustodianCodeEscapeOptionWithCustodianController:"
- "_enterCustodianCodeEscapeOptionWithCustodianController:presentationBlock:"
- "_escapeOfferForCustodianFlowWithMask:"
- "_instructionsControllerForPlatform:controller:"
- "_presentRemoteSecretControllerWithNewestDevice:cdpContext:"
- "_recoveryKeyEscapeOffer"
- "_recoveryKeyEscapeOption"
- "_recoveryKeyEscapeOptionWithPresentationBlock:"
- "_resetAccountDataEscapeOption"
- "_resetEncryptedDataEscapeOptionForAlert:"
- "_tryAgainLaterEscapeOptionForAlert:"
- "_walrusBeginCustodianRecoveryEscapeOption"
- "_walrusEscapeOfferForDevice:withMask:"
- "_walrusEscapeOffersForgotAllWithMask:presenter:devices:"
- "custodianOSSelectionViewControllerWithCustodianController:"
- "defaultWorkspace"
- "initWithAccount:"
- "isFooterButtonForOtherRecoveryOptions"
- "isSOSCFUFlow"
- "openURL:withOptions:"
- "recoveryKeyEntryControllerForCircleJoinWithCancel:"

```
