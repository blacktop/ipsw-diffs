## PreferencesUI

> `/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI`

```diff

-1250.3.17.0.0
-  __TEXT.__text: 0x43484
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x2a0c
-  __TEXT.__const: 0xe6
-  __TEXT.__gcc_except_tab: 0x1234
-  __TEXT.__oslogstring: 0x37e2
-  __TEXT.__cstring: 0x47e2
-  __TEXT.__dlopen_cstrs: 0x618
-  __TEXT.__constg_swiftt: 0x8c
-  __TEXT.__swift5_typeref: 0x28
-  __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1184
-  __TEXT.__objc_classname: 0x7fe
-  __TEXT.__objc_methname: 0xc642
-  __TEXT.__objc_methtype: 0x2335
-  __TEXT.__objc_stubs: 0x9aa0
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1440
+1250.5.10.0.0
+  __TEXT.__text: 0x48fd0
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x2d1c
+  __TEXT.__const: 0x106
+  __TEXT.__gcc_except_tab: 0x131c
+  __TEXT.__oslogstring: 0x4237
+  __TEXT.__cstring: 0x52a2
+  __TEXT.__dlopen_cstrs: 0x670
+  __TEXT.__constg_swiftt: 0xd0
+  __TEXT.__swift5_typeref: 0x5a
+  __TEXT.__swift5_fieldmd: 0x30
+  __TEXT.__swift5_capture: 0x34
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__unwind_info: 0x1420
+  __TEXT.__eh_frame: 0xf0
+  __TEXT.__objc_classname: 0x7ca
+  __TEXT.__objc_methname: 0xd046
+  __TEXT.__objc_methtype: 0x23a7
+  __TEXT.__objc_stubs: 0xa2a0
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__const: 0x1590
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x47b0
-  __DATA_CONST.__objc_selrefs: 0x2e70
+  __DATA_CONST.__objc_const: 0x4a40
+  __DATA_CONST.__objc_selrefs: 0x30a0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x588
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0xdf0
-  __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0x4660
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_const: 0xd18
+  __AUTH_CONST.__const: 0x628
+  __AUTH_CONST.__cfstring: 0x4d40
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH.__objc_data: 0x608
-  __AUTH.__data: 0xc0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x570
-  __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0xdf0
-  __DATA.__bss: 0x130
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH.__objc_data: 0x678
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x2ac
+  __DATA.__data: 0xe30
+  __DATA.__bss: 0x140
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0xf8

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount
   - /System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI
+  - /System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1415
-  Symbols:   5526
-  CStrings:  3300
+  Functions: 1550
+  Symbols:   5859
+  CStrings:  3518
 
Symbols:
+ +[PSUIPrefsListController isFaceTimeRestricted:]
+ -[PSUIDeviceTakeOverController getAuthenticationFallbackDescriptionForIdentifier:]
+ -[PSUIDeviceTakeOverController getInProgressDescriptionForIdentifier:]
+ -[PSUIDeviceTakeOverController getOperationDeepLinkForIdentifier:]
+ -[PSUIDeviceTakeOverController getOperationNameForIdentifier:]
+ -[PSUIDeviceTakeOverController getTitleForIdentifier:]
+ -[PSUIDeviceTakeOverController performPreliminaryPreEnableDTOChecksWithCompletion:]
+ -[PSUIDeviceTakeOverController proceedToEnableRatchetWithCompletion:]
+ -[PSUIDeviceTakeOverController proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:]
+ -[PSUIDeviceTakeOverSectionController .cxx_destruct]
+ -[PSUIDeviceTakeOverSectionController addSpecifiers:toExistingSpecifiers:atIndex:]
+ -[PSUIDeviceTakeOverSectionController disableDTO]
+ -[PSUIDeviceTakeOverSectionController dtoController]
+ -[PSUIDeviceTakeOverSectionController enableDTO]
+ -[PSUIDeviceTakeOverSectionController ensureAccountSecurityIsSufficientWithCompletion:]
+ -[PSUIDeviceTakeOverSectionController ensureAccountSecurityIsSufficientWithCompletion:].cold.1
+ -[PSUIDeviceTakeOverSectionController getSpecifiersForSecurityOptionsGroup:]
+ -[PSUIDeviceTakeOverSectionController getSpecifiersForToggleGroup:]
+ -[PSUIDeviceTakeOverSectionController getStatus]
+ -[PSUIDeviceTakeOverSectionController getValueForStrictMode]
+ -[PSUIDeviceTakeOverSectionController getValueForStrictMode].cold.1
+ -[PSUIDeviceTakeOverSectionController getValueForStrictMode].cold.2
+ -[PSUIDeviceTakeOverSectionController init]
+ -[PSUIDeviceTakeOverSectionController isFindMyEnabled]
+ -[PSUIDeviceTakeOverSectionController openLearnMoreLink]
+ -[PSUIDeviceTakeOverSectionController performPreEnableDTOChecksWithCompletion:]
+ -[PSUIDeviceTakeOverSectionController printSpecifiersDescription:]
+ -[PSUIDeviceTakeOverSectionController proceedToDisableDTO]
+ -[PSUIDeviceTakeOverSectionController proceedToDisableDTO].cold.1
+ -[PSUIDeviceTakeOverSectionController proceedToEnableDTO]
+ -[PSUIDeviceTakeOverSectionController reloadEntirePane]
+ -[PSUIDeviceTakeOverSectionController reloadSpecifiersPostStatusToggle]
+ -[PSUIDeviceTakeOverSectionController setDtoController:]
+ -[PSUIDeviceTakeOverSectionController setIsFindMyEnabled:]
+ -[PSUIDeviceTakeOverSectionController setUpFindMyEnablementStatus]
+ -[PSUIDeviceTakeOverSectionController setValueForStrictMode:]
+ -[PSUIDeviceTakeOverSectionController setValueForStrictMode:].cold.1
+ -[PSUIDeviceTakeOverSectionController shouldIgnoreSecurityOptionsGroupRowSelectionFor:]
+ -[PSUIDeviceTakeOverSectionController shouldIgnoreToggleGroupRowSelectionFor:]
+ -[PSUIDeviceTakeOverSectionController showAlertForFindMyIsDisabledWithCompletion:]
+ -[PSUIDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]
+ -[PSUIDeviceTakeOverSectionController specifiers]
+ -[PSUIDeviceTakeOverSectionController tableView:cellForRowAtIndexPath:]
+ -[PSUIDeviceTakeOverSectionController tableView:didSelectRowAtIndexPath:]
+ -[PSUIDeviceTakeOverSectionController tableView:willSelectRowAtIndexPath:]
+ -[PSUIDeviceTakeOverSectionController toggleStatusTo:]
+ -[PSUIDeviceTakeOverSectionController updateFooterForSecurityOptionsGroupSpecifier:]
+ -[PSUIDeviceTakeOverSectionController updateFooterForToggleGroupSpecifier:]
+ -[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]
+ -[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:].cold.1
+ -[PSUIDeviceTakeOverSplashPaneController .cxx_destruct]
+ -[PSUIDeviceTakeOverSplashPaneController addEnrollButtonWithTitle:andAction:]
+ -[PSUIDeviceTakeOverSplashPaneController addNotNowButtonWithTitle:andAction:]
+ -[PSUIDeviceTakeOverSplashPaneController controller]
+ -[PSUIDeviceTakeOverSplashPaneController createLinkButtonWithTitle:action:]
+ -[PSUIDeviceTakeOverSplashPaneController enrollHandler]
+ -[PSUIDeviceTakeOverSplashPaneController enrollTapped]
+ -[PSUIDeviceTakeOverSplashPaneController init]
+ -[PSUIDeviceTakeOverSplashPaneController notNowTapped]
+ -[PSUIDeviceTakeOverSplashPaneController setController:]
+ -[PSUIDeviceTakeOverSplashPaneController setEnrollHandler:]
+ -[PSUIDeviceTakeOverSplashPaneController setUpButtons]
+ -[PSUIDeviceTakeOverSplashPaneController setUpFirstBullet]
+ -[PSUIDeviceTakeOverSplashPaneController setUpSecondBullet]
+ -[PSUIDeviceTakeOverSplashPaneController setUpThirdBullet]
+ -[PSUIDeviceTakeOverSplashPaneController viewDidLoad]
+ -[PSUIPasscodeLockController didPerformStartupAction]
+ -[PSUIPasscodeLockController getSpecifierIDForAction:]
+ -[PSUIPasscodeLockController getSpecifierIDForAction:].cold.1
+ -[PSUIPasscodeLockController handleDTOStatusChanged]
+ -[PSUIPasscodeLockController handleStartupActionIfAny]
+ -[PSUIPasscodeLockController handleStartupActionIfAny].cold.1
+ -[PSUIPasscodeLockController handleStartupActionIfAny].cold.2
+ -[PSUIPasscodeLockController isInternetReachable]
+ -[PSUIPasscodeLockController isObservingDTOStatusChange]
+ -[PSUIPasscodeLockController pathMonitor]
+ -[PSUIPasscodeLockController registerObserverAndHandlerForDTOStatusChanges]
+ -[PSUIPasscodeLockController scrollAndHighlightSpecifierWithID:]
+ -[PSUIPasscodeLockController scrollToStolenDeviceProtection]
+ -[PSUIPasscodeLockController setDidPerformStartupAction:]
+ -[PSUIPasscodeLockController setIsInternetReachable:]
+ -[PSUIPasscodeLockController setIsObservingDTOStatusChange:]
+ -[PSUIPasscodeLockController setPathMonitor:]
+ -[PSUIPasscodeLockController setupInternetAvailabilityMonitoring]
+ -[PSUIPasscodeLockController shouldPerformStartupAction]
+ -[PSUIPasscodeLockController shouldPresentAppleIDAuthenticationForTogglingPasscode]
+ -[PSUIPasscodeLockController updateDTOSpecifierIfNeeded]
+ -[PSUIPasscodeLockController updatePasscodeChangesGroupFooterToSpecifier:mustRemove:]
+ -[PSUIPasscodeLockController viewDidAppear:]
+ -[PSUIPrefsListController _appInstallationSpecifier]
+ -[PSUIPrefsListController addStartupActionToPasscodePane:]
+ -[PSUIPrefsListController marketplaceOrTrustedDevelopersDidChange]
+ -[PSUIPrefsListController passcodePaneStartupAction]
+ -[PSUIPrefsListController setPasscodePaneStartupAction:]
+ -[PSUIPrefsListController set_appInstallationSpecifier:]
+ -[PSUIPrefsListController updateAppInstallationWithCompletion:]
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table161
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table177
+ GCC_except_table190
+ GCC_except_table21
+ GCC_except_table211
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table269
+ GCC_except_table28
+ GCC_except_table280
+ GCC_except_table284
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table36
+ GCC_except_table43
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table72
+ _CFBooleanGetValue
+ _CPCopySharedResourcesPreferencesDomainForDomain
+ _LADarwinNotificationRatchetStateDidChange
+ _LARatchetErrorDomain
+ _OBJC_CLASS_$_LAContext
+ _OBJC_CLASS_$_OBBoldTrayButton
+ _OBJC_CLASS_$_OBLinkTrayButton
+ _OBJC_CLASS_$_PSUIDeviceTakeOverSectionController
+ _OBJC_CLASS_$_PSUIDeviceTakeOverSplashPaneController
+ _OBJC_CLASS_$__TtC13PreferencesUI21AppDistributorWrapper
+ _OBJC_IVAR_$_PSUIDeviceTakeOverSectionController._dtoController
+ _OBJC_IVAR_$_PSUIDeviceTakeOverSectionController._isFindMyEnabled
+ _OBJC_IVAR_$_PSUIDeviceTakeOverSplashPaneController._controller
+ _OBJC_IVAR_$_PSUIDeviceTakeOverSplashPaneController._enrollHandler
+ _OBJC_IVAR_$_PSUIPasscodeLockController._didPerformStartupAction
+ _OBJC_IVAR_$_PSUIPasscodeLockController._isInternetReachable
+ _OBJC_IVAR_$_PSUIPasscodeLockController._isObservingDTOStatusChange
+ _OBJC_IVAR_$_PSUIPasscodeLockController._pathMonitor
+ _OBJC_IVAR_$_PSUIPrefsListController.__appInstallationSpecifier
+ _OBJC_IVAR_$_PSUIPrefsListController._passcodePaneStartupAction
+ _OBJC_METACLASS_$_PSUIDeviceTakeOverSectionController
+ _OBJC_METACLASS_$_PSUIDeviceTakeOverSplashPaneController
+ _OBJC_METACLASS_$__TtC13PreferencesUI21AppDistributorWrapper
+ _PSIsRadioGroupKey
+ _PSJoinedCDPCircleAccount
+ _PSRadioGroupCheckedSpecifierKey
+ __Block_copy
+ __Block_release
+ __DATA__TtC13PreferencesUI21AppDistributorWrapper
+ __METACLASS_DATA__TtC13PreferencesUI21AppDistributorWrapper
+ __OBJC_$_CLASS_METHODS__TtC13PreferencesUI21AppDistributorWrapper
+ __OBJC_$_INSTANCE_METHODS_PSUIDeviceTakeOverSectionController
+ __OBJC_$_INSTANCE_METHODS_PSUIDeviceTakeOverSplashPaneController
+ __OBJC_$_INSTANCE_METHODS__TtC13PreferencesUI21AppDistributorWrapper
+ __OBJC_$_INSTANCE_VARIABLES_PSUIDeviceTakeOverSectionController
+ __OBJC_$_INSTANCE_VARIABLES_PSUIDeviceTakeOverSplashPaneController
+ __OBJC_$_PROP_LIST_PSUIDeviceTakeOverSectionController
+ __OBJC_$_PROP_LIST_PSUIDeviceTakeOverSplashPaneController
+ __OBJC_CLASS_RO_$_PSUIDeviceTakeOverSectionController
+ __OBJC_CLASS_RO_$_PSUIDeviceTakeOverSplashPaneController
+ __OBJC_METACLASS_RO_$_PSUIDeviceTakeOverSectionController
+ __OBJC_METACLASS_RO_$_PSUIDeviceTakeOverSplashPaneController
+ ___108-[PSUIDeviceTakeOverController proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:]_block_invoke
+ ___108-[PSUIDeviceTakeOverController proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:]_block_invoke.cold.1
+ ___108-[PSUIDeviceTakeOverController proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:]_block_invoke.cold.2
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.159
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.162
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.166
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.166.cold.1
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.166.cold.2
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.168
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.168.cold.1
+ ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.164
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.121
+ ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.121.cold.1
+ ___46-[PSUIPrefsListController willEnterForeground]_block_invoke.993
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.270
+ ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.270.cold.1
+ ___47-[PSUIPasscodeLockController showKeychainAlert]_block_invoke.335
+ ___48-[PSUIDeviceTakeOverSectionController enableDTO]_block_invoke
+ ___48-[PSUIDeviceTakeOverSectionController enableDTO]_block_invoke.99
+ ___48-[PSUIDeviceTakeOverSectionController enableDTO]_block_invoke.99.cold.1
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.266
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.268
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.269
+ ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.269.cold.1
+ ___49-[PSUIDeviceTakeOverSectionController disableDTO]_block_invoke
+ ___49-[PSUIDeviceTakeOverSectionController disableDTO]_block_invoke.101
+ ___49-[PSUIDeviceTakeOverSectionController disableDTO]_block_invoke.101.cold.1
+ ___49-[PSUIPrefsListController refresh3rdPartyBundles]_block_invoke_2.568
+ ___52-[PSUIPasscodeLockController handleDTOStatusChanged]_block_invoke
+ ___52-[PSUIPasscodeLockController handleDTOStatusChanged]_block_invoke.cold.1
+ ___56-[PSUIDeviceTakeOverSectionController openLearnMoreLink]_block_invoke
+ ___56-[PSUIDeviceTakeOverSectionController openLearnMoreLink]_block_invoke.cold.1
+ ___56-[PSUIPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.532
+ ___56-[PSUIPasscodeLockController updateDTOSpecifierIfNeeded]_block_invoke
+ ___56-[PSUIPasscodeLockController updateDTOSpecifierIfNeeded]_block_invoke_2
+ ___56-[PSUIPasscodeLockController updateDTOSpecifierIfNeeded]_block_invoke_2.cold.1
+ ___56-[PSUIPrefsListController indexManifestsWithCompletion:]_block_invoke.1136
+ ___56-[PSUIPrefsListController testSpecifierCountAfterBlock:]_block_invoke.497
+ ___57-[PSUIDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke
+ ___57-[PSUIDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.96
+ ___57-[PSUIDeviceTakeOverSectionController proceedToEnableDTO]_block_invoke.96.cold.1
+ ___58-[PSUIDeviceTakeOverSectionController proceedToDisableDTO]_block_invoke
+ ___58-[PSUIDeviceTakeOverSectionController proceedToDisableDTO]_block_invoke_2
+ ___58-[PSUIDeviceTakeOverSectionController proceedToDisableDTO]_block_invoke_2.cold.1
+ ___58-[PSUIDeviceTakeOverSectionController proceedToDisableDTO]_block_invoke_2.cold.2
+ ___58-[PSUIPrefsListController vpnSpecifierGeneratorDidUpdate:]_block_invoke.1182
+ ___60-[PSUIDeviceTakeOverController enableRatchetWithCompletion:]_block_invoke.cold.2
+ ___61-[PSUIPrefsListController familySpecifierGeneratorDidUpdate:]_block_invoke.1179
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.160
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.161
+ ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke_2.162
+ ___63-[PSUIPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.221
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.487
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.488
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.489
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.490
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.491
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.492
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.493
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.494
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.495
+ ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.496
+ ___63-[PSUIPrefsListController updateAppInstallationWithCompletion:]_block_invoke
+ ___63-[PSUIPrefsListController updateAppInstallationWithCompletion:]_block_invoke_2
+ ___63-[PSUIPrefsListController updateAppInstallationWithCompletion:]_block_invoke_3
+ ___64-[PSUIPrefsListController updateHomeKitSpecifierWithCompletion:]_block_invoke.701
+ ___65-[PSUIPasscodeLockController setupInternetAvailabilityMonitoring]_block_invoke
+ ___66-[PSUIDeviceTakeOverSectionController setUpFindMyEnablementStatus]_block_invoke
+ ___66-[PSUIDeviceTakeOverSectionController setUpFindMyEnablementStatus]_block_invoke.cold.1
+ ___66-[PSUIDeviceTakeOverSectionController setUpFindMyEnablementStatus]_block_invoke.cold.2
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.162
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.162.cold.1
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.163
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.163.cold.1
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.164
+ ___67-[PSUIDeviceTakeOverSectionController userUpdatedSecurityOptionTo:]_block_invoke.164.cold.1
+ ___69-[PSUIDeviceTakeOverController proceedToEnableRatchetWithCompletion:]_block_invoke
+ ___69-[PSUIDeviceTakeOverController proceedToEnableRatchetWithCompletion:]_block_invoke.cold.1
+ ___77-[PSUIPrefsListController _insertOrRemovePaymentSpecifierAsNeededCompletion:]_block_invoke.983
+ ___79-[PSUIDeviceTakeOverSectionController performPreEnableDTOChecksWithCompletion:]_block_invoke
+ ___82-[PSUIDeviceTakeOverSectionController showAlertForFindMyIsDisabledWithCompletion:]_block_invoke
+ ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.251
+ ___83-[PSUIDeviceTakeOverController performPreliminaryPreEnableDTOChecksWithCompletion:]_block_invoke
+ ___83-[PSUIDeviceTakeOverController performPreliminaryPreEnableDTOChecksWithCompletion:]_block_invoke.cold.1
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.549
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.553
+ ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.560
+ ___87-[PSUIDeviceTakeOverSectionController ensureAccountSecurityIsSufficientWithCompletion:]_block_invoke
+ ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.545
+ ___94-[PSUIDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]_block_invoke
+ ___94-[PSUIDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]_block_invoke.146
+ ___94-[PSUIDeviceTakeOverSectionController showDTOAlertForFailureToToggleToState:withRatchetError:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
+ ___block_descriptor_41_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40w_e21_v20?0B8"NSString"12lw40l8s32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8w48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.223
+ ___block_literal_global.231
+ ___block_literal_global.272
+ ___block_literal_global.274
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.381
+ ___block_literal_global.399
+ ___block_literal_global.555
+ ___block_literal_global.562
+ ___block_literal_global.588
+ ___block_literal_global.591
+ ___block_literal_global.995
+ ___block_literal_global.997
+ ___chkstk_darwin
+ __unnamed_array_storage.1070
+ __unnamed_array_storage.1212
+ __unnamed_array_storage.1213
+ _calloc
+ _dtoStatusChangedNotification
+ _dtoStatusChangedNotification.cold.1
+ _nw_path_create_evaluator_for_endpoint
+ _nw_path_evaluator_copy_path
+ _nw_path_get_status
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _objc_allocWithZone
+ _objc_msgSend$_appInstallationSpecifier
+ _objc_msgSend$addBulletedListItemWithTitle:description:symbolName:
+ _objc_msgSend$addButton:
+ _objc_msgSend$addEnrollButtonWithTitle:andAction:
+ _objc_msgSend$addNotNowButtonWithTitle:andAction:
+ _objc_msgSend$addSpecifiers:toExistingSpecifiers:atIndex:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$applicationIsInstalled:
+ _objc_msgSend$boldButton
+ _objc_msgSend$buttonTray
+ _objc_msgSend$checkCanEnableFeatureWithCompletion:
+ _objc_msgSend$createLinkButtonWithTitle:action:
+ _objc_msgSend$didPerformStartupAction
+ _objc_msgSend$disableDTO
+ _objc_msgSend$domain
+ _objc_msgSend$enableDTO
+ _objc_msgSend$enrollHandler
+ _objc_msgSend$evaluatePolicy:options:reply:
+ _objc_msgSend$getAuthenticationFallbackDescriptionForIdentifier:
+ _objc_msgSend$getGroupSpecifierForSpecifier:
+ _objc_msgSend$getInProgressDescriptionForIdentifier:
+ _objc_msgSend$getOperationDeepLinkForIdentifier:
+ _objc_msgSend$getOperationNameForIdentifier:
+ _objc_msgSend$getSpecifierIDForAction:
+ _objc_msgSend$getSpecifiersForSecurityOptionsGroup:
+ _objc_msgSend$getSpecifiersForToggleGroup:
+ _objc_msgSend$getStatus
+ _objc_msgSend$getTitleForIdentifier:
+ _objc_msgSend$getValueForStrictMode
+ _objc_msgSend$handleDTOStatusChanged
+ _objc_msgSend$handleStartupActionIfAny
+ _objc_msgSend$headerView
+ _objc_msgSend$initWithTitle:detailText:icon:contentLayout:
+ _objc_msgSend$isEqualToSpecifier:
+ _objc_msgSend$isFaceTimeRestricted:
+ _objc_msgSend$isInternetReachable
+ _objc_msgSend$isObservingDTOStatusChange
+ _objc_msgSend$linkButton
+ _objc_msgSend$openLearnMoreLink
+ _objc_msgSend$passcodePaneStartupAction
+ _objc_msgSend$performPreliminaryPreEnableDTOChecksWithCompletion:
+ _objc_msgSend$printSpecifiersDescription:
+ _objc_msgSend$proceedToDisableDTO
+ _objc_msgSend$proceedToEnableDTO
+ _objc_msgSend$proceedToEnableRatchetWithCompletion:
+ _objc_msgSend$proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:
+ _objc_msgSend$registerObserverAndHandlerForDTOStatusChanges
+ _objc_msgSend$reloadEntirePane
+ _objc_msgSend$reloadSpecifiersPostStatusToggle
+ _objc_msgSend$scrollAndHighlightSpecifierWithID:
+ _objc_msgSend$setDidPerformStartupAction:
+ _objc_msgSend$setIsInternetReachable:
+ _objc_msgSend$setIsObservingDTOStatusChange:
+ _objc_msgSend$setPasscodePaneStartupAction:
+ _objc_msgSend$setSelectionStyle:
+ _objc_msgSend$setSubtitleText:
+ _objc_msgSend$setTitle:forState:
+ _objc_msgSend$setUpButtons
+ _objc_msgSend$setUpFirstBullet
+ _objc_msgSend$setUpSecondBullet
+ _objc_msgSend$setUpThirdBullet
+ _objc_msgSend$setValueForStrictMode:
+ _objc_msgSend$set_appInstallationSpecifier:
+ _objc_msgSend$setupInternetAvailabilityMonitoring
+ _objc_msgSend$shouldIgnoreSecurityOptionsGroupRowSelectionFor:
+ _objc_msgSend$shouldIgnoreToggleGroupRowSelectionFor:
+ _objc_msgSend$shouldPerformStartupAction
+ _objc_msgSend$shouldPresentAppleIDAuthenticationForTogglingPasscode
+ _objc_msgSend$shouldShowAppInstallationSettingsNotification
+ _objc_msgSend$shouldShowAppInstallationSettingsWithCompletionHandler:
+ _objc_msgSend$showDTOAlertForFailureToToggleToState:withRatchetError:
+ _objc_msgSend$updateAppInstallationWithCompletion:
+ _objc_msgSend$updateDTOSpecifierIfNeeded
+ _objc_msgSend$updateFooterForSecurityOptionsGroupSpecifier:
+ _objc_msgSend$updateFooterForToggleGroupSpecifier:
+ _objc_msgSend$updatePasscodeChangesGroupFooterToSpecifier:mustRemove:
+ _objc_msgSend$updateRestrictedSettings
+ _objc_msgSend$userUpdatedSecurityOptionTo:
+ _swift_deallocObject
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _symbolic IeghH_
+ _symbolic SbIeyBy_
+ _symbolic ScPSg
+ _symbolic _____ 13PreferencesUI21AppDistributorWrapperC
+ _symbolic _____XMo 13PreferencesUI21AppDistributorWrapperC
+ _symbolic ytIeghHr_
- +[PSUIRatchetedOperationGroupNameTransformer allowsReverseTransformation]
- +[PSUIRatchetedOperationGroupNameTransformer transformedValueClass]
- +[PSUIRatchetedOperationNameDetailedTransformer allowsReverseTransformation]
- +[PSUIRatchetedOperationNameDetailedTransformer transformedValueClass]
- +[PSUIRatchetedOperationNameTransformer allowsReverseTransformation]
- +[PSUIRatchetedOperationNameTransformer transformedValueClass]
- -[PSUIPasscodeLockController cdpCircleExists]
- -[PSUIPasscodeLockController cdpCircleExists].cold.1
- -[PSUIPasscodeLockController disableDTO:]
- -[PSUIPasscodeLockController enableDTO:]
- -[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:]
- -[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:].cold.1
- -[PSUIPasscodeLockController openDTOFooterHelpLink]
- -[PSUIPasscodeLockController performPreEnableDTOChecksWithCompletion:]
- -[PSUIPasscodeLockController setNameForDTOToggle:]
- -[PSUIPasscodeLockController setUpFindMyEnablementStatus]
- -[PSUIPasscodeLockController setValueForDTOStatusLabel]
- -[PSUIPasscodeLockController showAlertForFindMyIsDisabledWithCompletion:]
- -[PSUIPasscodeLockController showDTOAlertForFailureToToggleToState:]
- -[PSUIPasscodeLockController toggleDTO:]
- -[PSUIPasscodeLockController toggledDTOSuccessfully:]
- -[PSUIPasscodeLockController updateFooterForDTOGroupSpecifier:]
- -[PSUIRatchetedOperationGroupNameTransformer transformedValue:]
- -[PSUIRatchetedOperationNameDetailedTransformer transformedValue:]
- -[PSUIRatchetedOperationNameTransformer transformedValue:]
- GCC_except_table106
- GCC_except_table113
- GCC_except_table125
- GCC_except_table129
- GCC_except_table136
- GCC_except_table140
- GCC_except_table144
- GCC_except_table151
- GCC_except_table160
- GCC_except_table164
- GCC_except_table171
- GCC_except_table184
- GCC_except_table205
- GCC_except_table220
- GCC_except_table224
- GCC_except_table26
- GCC_except_table262
- GCC_except_table273
- GCC_except_table277
- GCC_except_table305
- GCC_except_table307
- GCC_except_table310
- GCC_except_table313
- GCC_except_table60
- GCC_except_table71
- GCC_except_table88
- _OBJC_CLASS_$_CDPStateController
- _OBJC_CLASS_$_NSValueTransformer
- _OBJC_CLASS_$_PSUIRatchetedOperationGroupNameTransformer
- _OBJC_CLASS_$_PSUIRatchetedOperationNameDetailedTransformer
- _OBJC_CLASS_$_PSUIRatchetedOperationNameTransformer
- _OBJC_METACLASS_$_NSValueTransformer
- _OBJC_METACLASS_$_PSUIRatchetedOperationGroupNameTransformer
- _OBJC_METACLASS_$_PSUIRatchetedOperationNameDetailedTransformer
- _OBJC_METACLASS_$_PSUIRatchetedOperationNameTransformer
- _OUTLINED_FUNCTION_6
- __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationGroupNameTransformer
- __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationNameDetailedTransformer
- __OBJC_$_CLASS_METHODS_PSUIRatchetedOperationNameTransformer
- __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationGroupNameTransformer
- __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationNameDetailedTransformer
- __OBJC_$_INSTANCE_METHODS_PSUIRatchetedOperationNameTransformer
- __OBJC_CLASS_RO_$_PSUIRatchetedOperationGroupNameTransformer
- __OBJC_CLASS_RO_$_PSUIRatchetedOperationNameDetailedTransformer
- __OBJC_CLASS_RO_$_PSUIRatchetedOperationNameTransformer
- __OBJC_METACLASS_RO_$_PSUIRatchetedOperationGroupNameTransformer
- __OBJC_METACLASS_RO_$_PSUIRatchetedOperationNameDetailedTransformer
- __OBJC_METACLASS_RO_$_PSUIRatchetedOperationNameTransformer
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.152
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.154
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.156
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.161.cold.1
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.161.cold.2
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.163
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke.163.cold.1
- ___132-[PSUIPasscodeLockController showLocalAuthenticationPasscodeChangeFlowFromPresentingController:title:passcodePrompt:withCompletion:]_block_invoke_2.159
- ___37-[PSUIPrefsListController specifiers]_block_invoke_5
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.282
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.282.cold.1
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.283
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.283.cold.1
- ___40-[PSUIPasscodeLockController enableDTO:]_block_invoke.284
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.293
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.293.cold.1
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.294
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.294.cold.1
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.295
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.295.cold.1
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.296
- ___41-[PSUIPasscodeLockController disableDTO:]_block_invoke.cold.1
- ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.116
- ___45-[PSUIPasscodeLockController togglePasscode:]_block_invoke.116.cold.1
- ___46-[PSUIPrefsListController willEnterForeground]_block_invoke.978
- ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.269
- ___47-[PSUIFingerprintController deleteFingerprint:]_block_invoke.269.cold.1
- ___47-[PSUIPasscodeLockController showKeychainAlert]_block_invoke.384
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.265
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke.267
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.268
- ___48-[PSUIFingerprintController replaceFingerprint:]_block_invoke_2.268.cold.1
- ___49-[PSUIPrefsListController refresh3rdPartyBundles]_block_invoke_2.558
- ___51-[PSUIPasscodeLockController openDTOFooterHelpLink]_block_invoke
- ___51-[PSUIPasscodeLockController openDTOFooterHelpLink]_block_invoke.cold.1
- ___56-[PSUIPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.548
- ___56-[PSUIPrefsListController indexManifestsWithCompletion:]_block_invoke.1118
- ___56-[PSUIPrefsListController testSpecifierCountAfterBlock:]_block_invoke.487
- ___57-[PSUIPasscodeLockController setUpFindMyEnablementStatus]_block_invoke
- ___57-[PSUIPasscodeLockController setUpFindMyEnablementStatus]_block_invoke.cold.1
- ___58-[PSUIPrefsListController vpnSpecifierGeneratorDidUpdate:]_block_invoke.1165
- ___61-[PSUIPrefsListController familySpecifierGeneratorDidUpdate:]_block_invoke.1162
- ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.157
- ___62-[PSUIBiometricController setSafariAutoFillEnabled:specifier:]_block_invoke.158
- ___63-[PSUIPasscodeLockController gracePeriodClearRecoveryPasscode:]_block_invoke.217
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.469
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.470
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.471
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.472
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.473
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.474
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.475
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.476
- ___63-[PSUIPrefsListController reloadAsyncSpecifiersWithCompletion:]_block_invoke.477
- ___64-[PSUIPrefsListController updateHomeKitSpecifierWithCompletion:]_block_invoke.684
- ___68-[PSUIPasscodeLockController showDTOAlertForFailureToToggleToState:]_block_invoke
- ___70-[PSUIPasscodeLockController performPreEnableDTOChecksWithCompletion:]_block_invoke
- ___73-[PSUIPasscodeLockController showAlertForFindMyIsDisabledWithCompletion:]_block_invoke
- ___77-[PSUIPrefsListController _insertOrRemovePaymentSpecifierAsNeededCompletion:]_block_invoke.968
- ___78-[PSUIPasscodeLockController ensureAccountSecurityIsSufficientWithCompletion:]_block_invoke
- ___82-[PSUIFingerprintController presentAlertSheetForFingerprintBindingToGovernmentID:]_block_invoke.250
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.565
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.569
- ___86-[PSUIPasscodeLockController presentAutoUnlockEnableFailureAlertWithDevice:withError:]_block_invoke.576
- ___88-[PSUIPasscodeLockController showAlertForPhoneAutoUnlockEnablementOfDevice:ofSpecifier:]_block_invoke.561
- ___block_descriptor_32_e28_B32?0"PSSpecifier"8Q16^B24l
- ___block_descriptor_42_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_literal_global.219
- ___block_literal_global.227
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.325
- ___block_literal_global.372
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.386
- ___block_literal_global.390
- ___block_literal_global.552
- ___block_literal_global.571
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.828
- ___block_literal_global.980
- ___block_literal_global.982
- __unnamed_array_storage.1055
- __unnamed_array_storage.1195
- __unnamed_array_storage.1196
- _malloc_type_calloc
- _objc_msgSend$cdpCircleExists
- _objc_msgSend$disableDTO:
- _objc_msgSend$enableDTO:
- _objc_msgSend$getDTOStatusForSpecifier:
- _objc_msgSend$isFeatureAvailable
- _objc_msgSend$isFeatureSupported
- _objc_msgSend$isManateeAvailable:
- _objc_msgSend$refreshCellForSpecifier:
- _objc_msgSend$setNameForDTOToggle:
- _objc_msgSend$setValueForDTOStatusLabel
- _objc_msgSend$showDTOAlertForFailureToToggleToState:
- _objc_msgSend$toggledDTOSuccessfully:
- _objc_msgSend$transformedValue:
- _objc_msgSend$updateFooterForDTOGroupSpecifier:
- _objc_msgSend$valueTransformerForName:
CStrings:
+ "\x12\x16"
+ "\x15\x14\x1f\x02\x18\x1f\x1f\x03"
+ " *** Unknown ***"
+ " -> Toggled [%@]"
+ " -> i. Familiar only"
+ " -> i. Familiar only [Checked]"
+ " -> ii. Always"
+ " -> ii. Always [Checked]"
+ "%@%lu"
+ "%s: updateAppInstallationWithCompletion finished"
+ "%{public}s: updateAppInstallationWithCompletion finished"
+ ".GlobalPreferences"
+ "@\"NSNumber\""
+ "@\"NSObject<OS_nw_path_monitor>\""
+ "@24@0:8Q16"
+ "@32@0:8@16:24"
+ "APP_INSTALLATION"
+ "CHANGE_PASSCODE"
+ "DTO Summary: "
+ "DTO: Available [Status: %@]: Adding specifiers"
+ "DTO: Could not open Learn More - No instance (self)"
+ "DTO: Downgrading security option to Familiar Locations"
+ "DTO: Failed preliminary checks - will be disabled"
+ "DTO: Failed to retrieve - defaulting to strict mode [0]"
+ "DTO: Failed to set - defaulting to existing strict mode"
+ "DTO: Failed to update changes as missing instance (self)"
+ "DTO: No value set currently - defaulting to strict mode [0]"
+ "DTO: Not downgrading security option to Familiar Locations only as we are Ratcheted"
+ "DTO: Passed preliminary checks"
+ "DTO: Performing preliminary checks - No instance (self)"
+ "DTO: Received notification: Changed arm/overall state"
+ "DTO: Received notification: Changed arm/overall state but have no observer"
+ "DTO: Refreshing Security Options UI"
+ "DTO: Reloading Status Label to updated status"
+ "DTO: Reloading the pane"
+ "DTO: Spash pane displayed"
+ "DTO: Spash pane: User tapped Enroll"
+ "DTO: Spash pane: User tapped Not Now"
+ "DTO: Start observing status changes"
+ "DTO: Stopped observing status changes"
+ "DTO: Strict Mode [%@]"
+ "DTO: Turn %@ Protection [Failed] - Alert [Dismissed - Learn More]"
+ "DTO: Turn Off Protection [%@]"
+ "DTO: Turn Off Protection [Failed] - was not on!"
+ "DTO: Turn On Protection [%@]"
+ "DTO: Unable downgrade security options - DTO is not ON"
+ "DTO: Unable downgrade security options - missing instance (self)"
+ "DTO: Unable to refresh Security Options UI - missing instance (self)"
+ "DTO: Unavailable: Skip adding specifiers"
+ "DTO: User clicked on support link."
+ "DTO: User downgraded security option to Familiar Locations only"
+ "DTO: User tapped on Toggle row, ignoring"
+ "DTO: User tapped on already currently check marked security option, ignoring"
+ "DTO: User toggled to state [%@]"
+ "DTO: User upgraded security option to Always"
+ "DTO: Will perform preliminary checks"
+ "DTO_ALERT_COULD_NOT_TOGGLE_LEARN_MORE_BUTTON"
+ "DTO_ALERT_FACE_ID_REQUIRED_TO_ENABLE"
+ "DTO_ALERT_TOUCH_ID_REQUIRED_TO_ENABLE"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_ADD_FINGERPRINT"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_DEFAULT"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_DELETE_FINGERPRINT"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_DISABLE_USING_FACE_ID_FOR_FEATURES"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_DISABLE_USING_TOUCH_ID_FOR_FEATURES"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_DOWNGRADE_SECURITY_FAMILIAR_ONLY"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_RESET_FACE_ID"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_SET_UP_FACE_ID"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_SET_UP_FACE_ID_WITH_GLASSES"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_SET_UP_FACE_ID_WITH_MASK"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_TURN_OFF_PASSCODE"
+ "DTO_AUTHENTICATION_FALLBACK_DESCRIPTION_TURN_OFF_STOLEN_DEVICE_PROTECTION"
+ "DTO_BEGIN_DESCRIPTION_DEFAULT"
+ "DTO_BEGIN_TITLE_CHANGE_FACE_ID"
+ "DTO_BEGIN_TITLE_CHANGE_PASSCODE"
+ "DTO_BEGIN_TITLE_CHANGE_STOLEN_DEVICE_PROTECTION"
+ "DTO_BEGIN_TITLE_CHANGE_TOUCH_ID"
+ "DTO_BEGIN_TITLE_DEFAULT"
+ "DTO_BEGIN_TITLE_ENROLL_FACE_ID"
+ "DTO_BEGIN_TITLE_ENROLL_TOUCH_ID"
+ "DTO_GROUP_DISABLED_REASON_FOOTER_DESCRIPTION_DEFAULT"
+ "DTO_GROUP_DISABLED_REASON_FOOTER_DESCRIPTION_FACE_ID"
+ "DTO_GROUP_DISABLED_REASON_FOOTER_DESCRIPTION_TOUCH_ID"
+ "DTO_GROUP_FOOTER_DESCRIPTION"
+ "DTO_IN_PROGRESS_DESCRIPTION_ADD_FINGERPRINT"
+ "DTO_IN_PROGRESS_DESCRIPTION_DEFAULT"
+ "DTO_IN_PROGRESS_DESCRIPTION_DELETE_FINGERPRINT"
+ "DTO_IN_PROGRESS_DESCRIPTION_DISABLE_USING_FACE_ID_FOR_FEATURES"
+ "DTO_IN_PROGRESS_DESCRIPTION_DISABLE_USING_TOUCH_ID_FOR_FEATURES"
+ "DTO_IN_PROGRESS_DESCRIPTION_DOWNGRADE_SECURITY_FAMILIAR_ONLY"
+ "DTO_IN_PROGRESS_DESCRIPTION_RESET_FACE_ID"
+ "DTO_IN_PROGRESS_DESCRIPTION_SET_UP_FACE_ID"
+ "DTO_IN_PROGRESS_DESCRIPTION_SET_UP_FACE_ID_WITH_GLASSES"
+ "DTO_IN_PROGRESS_DESCRIPTION_SET_UP_FACE_ID_WITH_MASK"
+ "DTO_IN_PROGRESS_DESCRIPTION_TURN_OFF_PASSCODE"
+ "DTO_IN_PROGRESS_DESCRIPTION_TURN_OFF_STOLEN_DEVICE_PROTECTION"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_FAMILIAR_LOCATIONS_ONLY"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION"
+ "DTO_SECURITY_DELAY_OPTION_AWAY_ALWAYS"
+ "DTO_SECURITY_DELAY_OPTION_AWAY_FAMILIAR_LOCATIONS_ONLY"
+ "DTO_SECURITY_OPTIONS_GROUP_ID"
+ "DTO_SECURITY_OPTION_ALWAYS_FAMILIAR_ID"
+ "DTO_SECURITY_OPTION_ALWAYS_ID"
+ "DTO_TOGGLE_GROUP_ID"
+ "DTO_TOGGLE_ID"
+ "DowngradeRatchetSecurityToFamiliarLocationsOnly"
+ "FaceTimeUninstall"
+ "Has a startup action"
+ "Has no startup action"
+ "IDS"
+ "Insufficient space allocated to copy string contents"
+ "Internet status: at startup [%@]"
+ "Internet status: changed to [%@]"
+ "LA.dto.strictModeEnabled"
+ "Lock with Location Waves"
+ "Off"
+ "On"
+ "PASSCODE_GROUP"
+ "PASSCODE_OFF_UNSUPPORTED_DESCRIPTION_WIFI"
+ "PSUIDeviceTakeOverSectionController"
+ "PSUIDeviceTakeOverSplashPaneController"
+ "Passcode Group: Passcode On/Off enablement status [%@] | appleIDConnection [%@] | MC [%@]"
+ "Passcode Group: Passcode not set"
+ "Passcode Pane loaded"
+ "Ratchet: %@ [isPhone: %@, FeatureEnabled: %@]"
+ "Ratchet: Biometric liveness confirmed already"
+ "Ratchet: Cannot perform Biometric Livenes check as we are missing instance (self)"
+ "Ratchet: Cannot proceed to enable Ratchet as we are missing instance (self)"
+ "Ratchet: Confirming Biometric liveness"
+ "Ratchet: Confirming Biometric liveness: Failed"
+ "Ratchet: Confirming Biometric liveness: Succeeded"
+ "Ratchet: Failed to enable - Initial check failed: Error: %@"
+ "Ratchet: Preliminary check failed: Error: %@ - %@"
+ "Ratchet: Preliminary check succeeded"
+ "STOLEN_DEVICE_PROTECTION_DELAY_ITEM_TITLE"
+ "STOLEN_DEVICE_PROTECTION_DETAIL"
+ "STOLEN_DEVICE_PROTECTION_FACE_ID_ITEM_TITLE"
+ "STOLEN_DEVICE_PROTECTION_LOCATION_ITEM_TITLE"
+ "STOLEN_DEVICE_PROTECTION_NOT_NOW_BUTTON"
+ "STOLEN_DEVICE_PROTECTION_SUBTITLE"
+ "STOLEN_DEVICE_PROTECTION_TITLE"
+ "STOLEN_DEVICE_PROTECTION_TOUCH_ID_ITEM_TITLE"
+ "STOLEN_DEVICE_PROTECTION_TURN_ON_BUTTON"
+ "Scrolling and highlighting: %@"
+ "Scrolling and highlighting: Stolen Device Protection"
+ "SpecifierIDForAction unknown  %lu"
+ "Startup action: cannot perform for specifierID %@"
+ "Startup action: cannot perform unknown %lu"
+ "StartupActionKey"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSNumber\",C,N,V_passcodePaneStartupAction"
+ "T@\"NSObject<OS_nw_path_monitor>\",&,N,V_pathMonitor"
+ "T@\"NSString\",?,R,C"
+ "T@\"PSSpecifier\",&,N,V__appInstallationSpecifier"
+ "T@?,C,N,V_enrollHandler"
+ "TB,N,V_didPerformStartupAction"
+ "TB,N,V_isInternetReachable"
+ "TB,N,V_isObservingDTOStatusChange"
+ "TOUCHID_SAFARI_AUTOFILL"
+ "Turn On Stolen Device Protection"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC13PreferencesUI21AppDistributorWrapper"
+ "__appInstallationSpecifier"
+ "_appInstallationSpecifier"
+ "_didPerformStartupAction"
+ "_enrollHandler"
+ "_isInternetReachable"
+ "_isObservingDTOStatusChange"
+ "_passcodePaneStartupAction"
+ "_pathMonitor"
+ "addBulletedListItemWithTitle:description:symbolName:"
+ "addButton:"
+ "addEnrollButtonWithTitle:andAction:"
+ "addNotNowButtonWithTitle:andAction:"
+ "addSpecifiers:toExistingSpecifiers:atIndex:"
+ "addStartupAction: %@"
+ "addStartupAction: Passcode Pane has a startup action to perform: %@"
+ "addStartupActionToPasscodePane:"
+ "addTarget:action:forControlEvents:"
+ "appendFormat:"
+ "applicationIsInstalled:"
+ "boldButton"
+ "buttonTray"
+ "checkCanEnableFeatureWithCompletion:"
+ "com.apple.facetime"
+ "configure: Passcode Pane has a startup action to perform: %@"
+ "createLinkButtonWithTitle:action:"
+ "didPerformStartupAction"
+ "disableDTO"
+ "domain"
+ "enableDTO"
+ "enrollHandler"
+ "enrollTapped"
+ "evaluatePolicy:options:reply:"
+ "faceid"
+ "getAuthenticationFallbackDescriptionForIdentifier:"
+ "getGroupSpecifierForSpecifier:"
+ "getInProgressDescriptionForIdentifier:"
+ "getOperationDeepLinkForIdentifier:"
+ "getOperationNameForIdentifier:"
+ "getSpecifierIDForAction:"
+ "getSpecifiersForSecurityOptionsGroup:"
+ "getSpecifiersForToggleGroup:"
+ "getStatus"
+ "getTitleForIdentifier:"
+ "getValueForStrictMode"
+ "handleDTOStatusChanged"
+ "handleStartupActionIfAny"
+ "headerView"
+ "initWithTitle:detailText:icon:contentLayout:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isEqualToSpecifier:"
+ "isFaceTimeRestricted:"
+ "isInternetReachable"
+ "isObservingDTOStatusChange"
+ "linkButton"
+ "location.fill"
+ "lock.badge.clock.fill"
+ "marketplaceOrTrustedDevelopersDidChange"
+ "notNowTapped"
+ "openLearnMoreLink"
+ "passcodePaneStartupAction"
+ "pathMonitor"
+ "performPreliminaryPreEnableDTOChecksWithCompletion:"
+ "prefs:root=PASSCODE&path="
+ "printSpecifiersDescription:"
+ "proceedToDisableDTO"
+ "proceedToEnableDTO"
+ "proceedToEnableRatchetWithCompletion:"
+ "proceedToPeformBiometricLivenessIfNeededWithResultDictionary:withCompletion:"
+ "registerObserverAndHandlerForDTOStatusChanges"
+ "reloadEntirePane"
+ "reloadSpecifiersPostStatusToggle"
+ "scrollAndHighlightSpecifierWithID:"
+ "scrollToStolenDeviceProtection"
+ "setDidPerformStartupAction:"
+ "setEnrollHandler:"
+ "setIsInternetReachable:"
+ "setIsObservingDTOStatusChange:"
+ "setPasscodePaneStartupAction:"
+ "setPathMonitor:"
+ "setSelectionStyle:"
+ "setSubtitleText:"
+ "setTitle:forState:"
+ "setUpButtons"
+ "setUpFirstBullet"
+ "setUpSecondBullet"
+ "setUpThirdBullet"
+ "setValueForStrictMode:"
+ "set_appInstallationSpecifier:"
+ "setupInternetAvailabilityMonitoring"
+ "shouldIgnoreSecurityOptionsGroupRowSelectionFor:"
+ "shouldIgnoreToggleGroupRowSelectionFor:"
+ "shouldPerformStartupAction"
+ "shouldPresentAppleIDAuthenticationForTogglingPasscode"
+ "shouldShowAppInstallationSettingsNotification"
+ "shouldShowAppInstallationSettingsWithCompletionHandler:"
+ "showAppInstallation"
+ "showDTOAlertForFailureToToggleToState:withRatchetError:"
+ "toggleStatusTo:"
+ "updateAppInstallationWithCompletion:"
+ "updateDTOSpecifierIfNeeded"
+ "updateFooterForSecurityOptionsGroupSpecifier:"
+ "updateFooterForToggleGroupSpecifier:"
+ "updatePasscodeChangesGroupFooterToSpecifier:mustRemove:"
+ "userUpdatedSecurityOptionTo:"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v20@?0B8@\"NSString\"12"
+ "v24@0:8@?<v@?B>16"
+ "v28@0:8B16Q20"
+ "v32@0:8@16:24"
+ "v40@0:8@16@24Q32"
+ "| Group 1: Toggle"
+ "| Group 2: Options (Strict Mode = %@)"
- "\x12\x15"
- "\x15\x14\x1f\x02\x18\x1e\x1f\x02"
- "Account security: CDP Circle: %@ Error: %@"
- "B32@?0@\"PSSpecifier\"8Q16^B24"
- "DTO: Turn Off Protection [Failed]"
- "DTO: Turn Off Protection [Success]"
- "DTO: Turn On Protection [Failed]"
- "DTO: Turn On Protection [Success]"
- "DTO: Unavailable"
- "DTO: User pressed Turn Off Protection"
- "DTO: User pressed Turn On Protection"
- "DTO_GROUP_FOOTER_DESCRIPTION_FACE_ID"
- "DTO_GROUP_FOOTER_DESCRIPTION_TOUCH_ID"
- "DTO_OPERATION_DESCRIPTION_ADD_FINGERPRINT"
- "DTO_OPERATION_DESCRIPTION_DEFAULT"
- "DTO_OPERATION_DESCRIPTION_DELETE_FINGERPRINT"
- "DTO_OPERATION_DESCRIPTION_DISABLE_USING_FACE_ID_FOR_FEATURES"
- "DTO_OPERATION_DESCRIPTION_DISABLE_USING_TOUCH_ID_FOR_FEATURES"
- "DTO_OPERATION_DESCRIPTION_RESET_FACE_ID"
- "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID"
- "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID_WITH_GLASSES"
- "DTO_OPERATION_DESCRIPTION_SET_UP_FACE_ID_WITH_MASK"
- "DTO_OPERATION_DESCRIPTION_TURN_OFF_PASSCODE"
- "DTO_OPERATION_DESCRIPTION_TURN_OFF_STOLEN_DEVICE_PROTECTION"
- "DTO_OPERATION_TITLE_NAME_CHANGE_FACE_ID"
- "DTO_OPERATION_TITLE_NAME_CHANGE_PASSCODE"
- "DTO_OPERATION_TITLE_NAME_CHANGE_STOLEN_DEVICE_PROTECTION"
- "DTO_OPERATION_TITLE_NAME_CHANGE_TOUCH_ID"
- "DTO_OPERATION_TITLE_NAME_DEFAULT"
- "DTO_OPERATION_TITLE_NAME_ENROLL_FACE_ID"
- "DTO_OPERATION_TITLE_NAME_ENROLL_TOUCH_ID"
- "DTO_SECURITY_DELAY_BEGIN_DESCRIPTION_DEFAULT"
- "DTO_SECURITY_DELAY_BEGIN_TITLE"
- "DTO_SECURITY_DELAY_IN_PROGRESS_DESCRIPTION"
- "DTO_SECURITY_FALLBACK_AUTHENTICATION_DESCRIPTION"
- "DTO_TOGGLE_BUTTON_DESCRIPTON_OFF"
- "DTO_TOGGLE_BUTTON_DESCRIPTON_ON"
- "DTO_TOGGLE_BUTTON_ID"
- "PSUIRatchetedOperationGroupNameTransformer"
- "PSUIRatchetedOperationNameDetailedTransformer"
- "PSUIRatchetedOperationNameTransformer"
- "Ratchet: Current status [%@]"
- "Ratchet: Proceeding to perform critical operation as gating is not required"
- "SettingsPasscodePane_"
- "_Ratchet_Identifier"
- "allowsReverseTransformation"
- "cdpCircleExists"
- "disableDTO:"
- "enableDTO:"
- "isFeatureAvailable"
- "isFeatureSupported"
- "isManateeAvailable:"
- "openDTOFooterHelpLink"
- "setNameForDTOToggle:"
- "setValueForDTOStatusLabel"
- "showDTOAlertForFailureToToggleToState:"
- "toggleDTO:"
- "toggledDTOSuccessfully:"
- "transformedValue:"
- "transformedValueClass"
- "updateFooterForDTOGroupSpecifier:"
- "valueTransformerForName:"

```
