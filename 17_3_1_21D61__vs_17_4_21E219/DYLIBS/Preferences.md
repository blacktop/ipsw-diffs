## Preferences

> `/System/Library/PrivateFrameworks/Preferences.framework/Preferences`

```diff

-5215.3.10.0.0
-  __TEXT.__text: 0xda08c
-  __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0xa938
+5215.5.10.0.0
+  __TEXT.__text: 0xdd70c
+  __TEXT.__auth_stubs: 0x1780
+  __TEXT.__objc_methlist: 0xaae8
   __TEXT.__const: 0x1fc
-  __TEXT.__gcc_except_tab: 0x1c58
-  __TEXT.__cstring: 0xdd04
+  __TEXT.__gcc_except_tab: 0x1dbc
+  __TEXT.__cstring: 0xe1c5
   __TEXT.__ustring: 0x22
-  __TEXT.__dlopen_cstrs: 0x1ece
-  __TEXT.__oslogstring: 0x339d
-  __TEXT.__unwind_info: 0x37a4
-  __TEXT.__objc_classname: 0x1d09
-  __TEXT.__objc_methname: 0x1e1e8
-  __TEXT.__objc_methtype: 0x44eb
-  __TEXT.__objc_stubs: 0x16bc0
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x39d8
-  __DATA_CONST.__objc_classlist: 0x6e8
+  __TEXT.__dlopen_cstrs: 0x2014
+  __TEXT.__oslogstring: 0x3564
+  __TEXT.__unwind_info: 0x38c8
+  __TEXT.__objc_classname: 0x1d4e
+  __TEXT.__objc_methname: 0x1e77c
+  __TEXT.__objc_methtype: 0x4534
+  __TEXT.__objc_stubs: 0x16f60
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__const: 0x3bc0
+  __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10900
-  __DATA_CONST.__objc_selrefs: 0x7088
-  __DATA_CONST.__objc_arraydata: 0x2c0
-  __AUTH_CONST.__cfstring: 0xcb80
-  __AUTH_CONST.__objc_const: 0x51e8
-  __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_const: 0x10b48
+  __DATA_CONST.__objc_selrefs: 0x71a8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x8f8
+  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_arraydata: 0x2d0
+  __AUTH_CONST.__cfstring: 0xcf00
+  __AUTH_CONST.__objc_const: 0x5278
+  __AUTH_CONST.__const: 0xc00
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0x3a20
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x8e8
-  __DATA.__objc_superrefs: 0x498
-  __DATA.__objc_ivar: 0xb9c
-  __DATA.__data: 0x19ea
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH.__objc_data: 0x3ac0
+  __DATA.__objc_ivar: 0xbc4
+  __DATA.__data: 0x1a1a
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xa90
+  __DATA.__bss: 0xab8
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: FB122D5B-9F56-3533-A225-E4409E311718
-  Functions: 4934
-  Symbols:   17277
-  CStrings:  9891
+  UUID: 1E877C8E-5302-37AC-98E6-901FF8ED1A4F
+  Functions: 5001
+  Symbols:   17508
+  CStrings:  10027
 
Symbols:
+ +[PSSystemPolicyManager isInstalledByThirdPartyMarketplace:]
+ -[DevicePINController deactivateKeypad]
+ -[DevicePINController setPinBlocked:]
+ -[PSBadgedTableCell contentAccessoryPadding]
+ -[PSBadgedTableCell minimumBadgeWidth]
+ -[PSBankConnectAnalyticsConsentCoordinator .cxx_destruct]
+ -[PSBankConnectAnalyticsConsentCoordinator dealloc]
+ -[PSBankConnectAnalyticsConsentCoordinator fetchStateWithCompletion:]
+ -[PSBankConnectAnalyticsConsentCoordinator init]
+ -[PSBankConnectAnalyticsConsentCoordinator privacyBundleIdentifier]
+ -[PSBankConnectAnalyticsConsentCoordinator registerForUpdatesWithHandler:]
+ -[PSBankConnectAnalyticsConsentCoordinator setAnalyticsConsent:completion:]
+ -[PSBankConnectAnalyticsConsentCoordinator setUpdateHandler:]
+ -[PSBankConnectAnalyticsConsentCoordinator shouldShare]
+ -[PSBankConnectAnalyticsConsentCoordinator showPreference]
+ -[PSBankConnectAnalyticsConsentCoordinator updateCachedPermission:]
+ -[PSBankConnectAnalyticsConsentCoordinator updateCachedVisibility:]
+ -[PSBankConnectAnalyticsConsentCoordinator updateHandler]
+ -[PSEditableTableCell defaultTextFieldIndentation]
+ -[PSEditableTableCell minTextFieldIndentation]
+ -[PSEditableTableCell textFieldHorizontalPadding]
+ -[PSSubtitleDisclosureTableCell contentAccessoryPadding]
+ -[PSSwitchTableCell spinnerStyle]
+ -[PSSystemPolicyForApp walletSpecifier]
+ -[PSThirdPartyApp initWithApplicationRecord:]
+ -[PSThirdPartyApp record]
+ -[PSWalletPolicyController .cxx_destruct]
+ -[PSWalletPolicyController initWithBundleIdentifier:]
+ -[PSWalletPolicyController specifier]
+ -[PSWalletPolicyController walletAuthorizationType]
+ -[ProblemReportingController bankConnectAnalyticsConsentCoordinator]
+ -[ProblemReportingController bankConnectDataSpecifiers]
+ -[ProblemReportingController setBankConnectAnalyticsConsentCoordinator:]
+ -[ProblemReportingController setShouldShareBankConnectData:specifier:]
+ -[ProblemReportingController setShouldShareHealthData:specifier:].cold.1
+ -[ProblemReportingController shouldShareBankConnectDataForSpecifier:]
+ -[ProblemReportingController showAboutBankConnectDataSheet]
+ GCC_except_table103
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table78
+ GCC_except_table86
+ GCC_except_table96
+ _FinanceKitLibraryCore.frameworkLibrary
+ _HealthAppServicesLibrary
+ _HealthAppServicesLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_PSBankConnectAnalyticsConsentCoordinator
+ _OBJC_CLASS_$_PSWalletPolicyController
+ _OBJC_IVAR_$_PSBankConnectAnalyticsConsentCoordinator._offlineLabConsentCoordinator
+ _OBJC_IVAR_$_PSBankConnectAnalyticsConsentCoordinator._shouldShare
+ _OBJC_IVAR_$_PSBankConnectAnalyticsConsentCoordinator._showPreference
+ _OBJC_IVAR_$_PSBankConnectAnalyticsConsentCoordinator._syncedKeychainNotifyToken
+ _OBJC_IVAR_$_PSBankConnectAnalyticsConsentCoordinator._updateHandler
+ _OBJC_IVAR_$_PSSystemPolicyForApp._walletPrivacyController
+ _OBJC_IVAR_$_PSThirdPartyApp._record
+ _OBJC_IVAR_$_PSWalletPolicyController._bundleIdentifier
+ _OBJC_IVAR_$_PSWalletPolicyController._privacyController
+ _OBJC_IVAR_$_ProblemReportingController._bankConnectAnalyticsConsentCoordinator
+ _OBJC_IVAR_$_ProblemReportingController._bankConnectDataSpecifiers
+ _OBJC_METACLASS_$_PSBankConnectAnalyticsConsentCoordinator
+ _OBJC_METACLASS_$_PSWalletPolicyController
+ _PSIsUserParcElisabethEligible
+ _PS_LocalizedStringForProblemReportingBankConnect
+ _SEServiceLibraryCore.frameworkLibrary
+ __OBJC_$_INSTANCE_METHODS_PSBankConnectAnalyticsConsentCoordinator
+ __OBJC_$_INSTANCE_METHODS_PSWalletPolicyController
+ __OBJC_$_INSTANCE_VARIABLES_PSBankConnectAnalyticsConsentCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_PSWalletPolicyController
+ __OBJC_$_PROP_LIST_PSBankConnectAnalyticsConsentCoordinator
+ __OBJC_CLASS_RO_$_PSBankConnectAnalyticsConsentCoordinator
+ __OBJC_CLASS_RO_$_PSWalletPolicyController
+ __OBJC_METACLASS_RO_$_PSBankConnectAnalyticsConsentCoordinator
+ __OBJC_METACLASS_RO_$_PSWalletPolicyController
+ __PSServiceIconTypeIDs
+ __ShouldShareBankConnectDataCacheKey
+ __ShowBankConnectPreferenceCacheKey
+ ___34-[DevicePINController pinEntered:]_block_invoke.184
+ ___41-[DevicePINController setPIN:completion:]_block_invoke.119
+ ___54-[PSRootController _delayedControllerReleaseAfterPop:]_block_invoke.188
+ ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke.393
+ ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke_2.398
+ ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke_4
+ ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke_5
+ ___55-[ProblemReportingController bankConnectDataSpecifiers]_block_invoke
+ ___62-[PSURLManager processURL:animated:fromSearch:withCompletion:]_block_invoke.138
+ ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.384
+ ___64+[PSSystemPolicyManager _cellularDataSettingsNeededForBundleID:]_block_invoke.41
+ ___65-[ProblemReportingController setShouldShareHealthData:specifier:]_block_invoke
+ ___69-[PSBankConnectAnalyticsConsentCoordinator fetchStateWithCompletion:]_block_invoke
+ ___69-[PSBankConnectAnalyticsConsentCoordinator fetchStateWithCompletion:]_block_invoke_2
+ ___70-[ProblemReportingController setShouldShareBankConnectData:specifier:]_block_invoke
+ ___70-[ProblemReportingController setShouldShareBankConnectData:specifier:]_block_invoke_2
+ ___70-[ProblemReportingController setShouldShareBankConnectData:specifier:]_block_invoke_3
+ ___70-[ProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.764
+ ___74-[PSBankConnectAnalyticsConsentCoordinator registerForUpdatesWithHandler:]_block_invoke
+ ___74-[PSBankConnectAnalyticsConsentCoordinator registerForUpdatesWithHandler:]_block_invoke_2
+ ___74-[PSBankConnectAnalyticsConsentCoordinator registerForUpdatesWithHandler:]_block_invoke_3
+ ___74-[PSBankConnectAnalyticsConsentCoordinator registerForUpdatesWithHandler:]_block_invoke_4
+ ___74-[ProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.850
+ ___75-[PSBankConnectAnalyticsConsentCoordinator setAnalyticsConsent:completion:]_block_invoke
+ ___75-[PSBankConnectAnalyticsConsentCoordinator setAnalyticsConsent:completion:]_block_invoke.cold.1
+ ___FinanceKitLibraryCore_block_invoke
+ ___HealthAppServicesLibraryCore_block_invoke
+ ___SEServiceLibraryCore_block_invoke
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32w_e11_v16?0B8B12lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e11_v16?0B8B12lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_50_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e50_v32?0"NSNumber"8^{__CFString=}16"PSSpecifier"24lw48l8s32l8s40l8
+ ___block_literal_global.10
+ ___block_literal_global.149
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.253
+ ___block_literal_global.40
+ ___block_literal_global.486
+ ___block_literal_global.502
+ ___block_literal_global.833
+ ___block_literal_global.866
+ ___getFKBankConnectOfflineLabConsentCoordinatorClass_block_invoke
+ ___getFKBankConnectOfflineLabConsentCoordinatorClass_block_invoke.cold.1
+ ___getFKPrivacySettingsControllerClass_block_invoke
+ ___getFKPrivacySettingsControllerClass_block_invoke.cold.1
+ ___getHealthAppAnalyticsAgreementImproveHealthAndAnalyticsSymbolLoc_block_invoke
+ ___getHealthAppAnalyticsAgreementImproveHealthRecordsSymbolLoc_block_invoke
+ ___getHealthAppAnalyticsStoreClass_block_invoke
+ ___getHealthAppAnalyticsStoreClass_block_invoke.cold.1
+ ___getSESSettingsEligiblityClass_block_invoke
+ ___getSESSettingsEligiblityClass_block_invoke.cold.1
+ _audit_stringFinanceKit
+ _audit_stringHealthAppServices
+ _audit_stringSEService
+ _getFKBankConnectOfflineLabConsentCoordinatorClass.softClass
+ _getFKPrivacySettingsControllerClass.softClass
+ _getHealthAppAnalyticsAgreementImproveHealthAndAnalyticsSymbolLoc.ptr
+ _getHealthAppAnalyticsAgreementImproveHealthRecordsSymbolLoc.ptr
+ _getHealthAppAnalyticsStoreClass
+ _getHealthAppAnalyticsStoreClass.softClass
+ _getSESSettingsEligiblityClass
+ _getSESSettingsEligiblityClass.softClass
+ _kTCCContactlessAccess
+ _kTCCPasskeysID
+ _kTCCSecureElementAccess
+ _kTCCServiceContactlessAccess
+ _kTCCServiceFinancialData
+ _kTCCServiceSecureElementAccess
+ _kTCCServiceWebBrowserPublicKeyCredential
+ _objc_msgSend$authorizationType
+ _objc_msgSend$bankConnectAnalyticsConsentCoordinator
+ _objc_msgSend$bankConnectDataSpecifiers
+ _objc_msgSend$contentAccessoryPadding
+ _objc_msgSend$defaultTextFieldIndentation
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$distributorIsFirstPartyApple
+ _objc_msgSend$fetchStateWithCompletion:
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$initWithApplicationRecord:
+ _objc_msgSend$isContactlessTCCServiceEligible
+ _objc_msgSend$isEligibleMailClient
+ _objc_msgSend$isEligibleWebBrowser
+ _objc_msgSend$isInstalledByThirdPartyMarketplace:
+ _objc_msgSend$isManagedAppDistributor
+ _objc_msgSend$isSecureElementTCCServiceEligible
+ _objc_msgSend$loadOfflineLabSharingPreferenceWithCompletion:
+ _objc_msgSend$minTextFieldIndentation
+ _objc_msgSend$minimumBadgeWidth
+ _objc_msgSend$offlineLabPrivacyBundleIdentifier
+ _objc_msgSend$privacyBundleIdentifier
+ _objc_msgSend$record
+ _objc_msgSend$registerForUpdatesWithHandler:
+ _objc_msgSend$saveOfflineLabSharingPermission:withCompletion:
+ _objc_msgSend$setPinBlocked:
+ _objc_msgSend$setShouldShareAppActivityWithAppDevelopers:specifier:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setUserDidAccept:currentAgreement:completion:
+ _objc_msgSend$shouldShare
+ _objc_msgSend$showPreference
+ _objc_msgSend$spinnerStyle
+ _objc_msgSend$textFieldHorizontalPadding
+ _objc_msgSend$updateCachedPermission:
+ _objc_msgSend$updateCachedVisibility:
+ _objc_msgSend$updateHandler
+ _objc_msgSend$walletSpecifier
+ _os_eligibility_get_domain_answer
- -[ProblemReportingController _handleUpdateForSpecifierID:value:error:]
- GCC_except_table100
- GCC_except_table115
- GCC_except_table134
- GCC_except_table135
- GCC_except_table136
- GCC_except_table66
- GCC_except_table76
- GCC_except_table97
- _OBJC_IVAR_$_PSThirdPartyApp._proxy
- ___34-[DevicePINController pinEntered:]_block_invoke.183
- ___41-[DevicePINController setPIN:completion:]_block_invoke.118
- ___54+[PSSystemPolicyManager _thirdPartyApplicationProxies]_block_invoke_2
- ___54-[PSRootController _delayedControllerReleaseAfterPop:]_block_invoke.187
- ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke.369
- ___54-[PSSystemPolicyForApp setPrivacyAccess:forSpecifier:]_block_invoke_2.374
- ___62-[PSURLManager processURL:animated:fromSearch:withCompletion:]_block_invoke.137
- ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.144
- ___64+[PSSystemPolicyManager _cellularDataSettingsNeededForBundleID:]_block_invoke.44
- ___70-[ProblemReportingController _handleUpdateForSpecifierID:value:error:]_block_invoke
- ___70-[ProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.520
- ___block_descriptor_40_e8_32s_e27_v24?0"LSBundleProxy"8^B16ls32l8
- ___block_descriptor_48_e8_32s40w_e50_v32?0"NSNumber"8^{__CFString=}16"PSSpecifier"24lw40l8s32l8
- ___block_literal_global.127
- ___block_literal_global.148
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.163
- ___block_literal_global.230
- ___block_literal_global.450
- ___block_literal_global.466
- ___block_literal_global.865
- _getkHKSettingsUserDefaultClinicalDataCollectionOptInKey
- _getkHKSettingsUserDefaultClinicalDataCollectionOptInKey.cold.1
- _objc_msgSend$_handleUpdateForSpecifierID:value:error:
- _objc_msgSend$_setDaemonPreferenceValue:forKey:completion:
- _objc_msgSend$enumerateBundlesOfType:block:
- _objc_msgSend$initWithApplicationProxy:
- _objc_msgSend$isMailClient
- _objc_msgSend$isWebBrowser
- _objc_msgSend$localizedNameForContext:
- _objc_msgSend$proxy
CStrings:
+ "\x05\x1f\x02"
+ "%s, Error when saving OfflineLab analytics consent, error: %@"
+ "%s: Saving OfflineLab analytics consent state."
+ "&&"
+ "-[PSBankConnectAnalyticsConsentCoordinator setAnalyticsConsent:completion:]"
+ "-[PSBankConnectAnalyticsConsentCoordinator setAnalyticsConsent:completion:]_block_invoke"
+ "@\"LSApplicationRecord\""
+ "@\"PSBankConnectAnalyticsConsentCoordinator\""
+ "@\"PSWalletPolicyController\""
+ "BANK_CONNECT_DATA_GROUP"
+ "CONTACTLESS_NFC"
+ "Cannot determine eligibility due to error: %d"
+ "FKBankConnectOfflineLabConsentCoordinator"
+ "FKPrivacySettingsController"
+ "Failed to update user agreement state: %@"
+ "HealthAppAnalyticsAgreementImproveHealthAndAnalytics"
+ "HealthAppAnalyticsAgreementImproveHealthRecords"
+ "HealthAppAnalyticsStore"
+ "Override with record compatability object %@"
+ "PASSKEYS"
+ "PRIVACY_OFFLINE_LAB_DATA_EXPLANATION"
+ "PRIVACY_OFFLINE_LAB_DATA_LINK"
+ "PRIVACY_OFFLINE_LAB_DATA_SHARE"
+ "PRIVACY_OFFLINE_LAB_SYNC_ALERT_DEFAULT_BUTTON"
+ "PRIVACY_OFFLINE_LAB_SYNC_ALERT_MESSAGE"
+ "PRIVACY_OFFLINE_LAB_SYNC_ALERT_TITLE"
+ "PROBLEM_REPORTING_EXPLANATION_ALT"
+ "PSBankConnectAnalyticsConsentCoordinator"
+ "PSWalletPolicyController"
+ "Privacy/WalletPrivacySettings"
+ "ProblemReporting-BankConnect"
+ "Reading AppList from LSEnumerator"
+ "SECURE_ELEMENT"
+ "SECURE_ELEMENT_PROMPT_DETAIL"
+ "SECURE_ELEMENT_PROMPT_TITLE"
+ "SESSettingsEligiblity"
+ "SHARE_BANKCONNECT_OFFLINELAB_DATA"
+ "Scroll target index path row %ld is out of bounds. Current number of row is %ld for section %ld."
+ "Scroll target index path section %ld is out of bounds. Current number of sections is %ld."
+ "T@\"LSApplicationProxy\",R,N"
+ "T@\"LSApplicationRecord\",R,N,V_record"
+ "T@\"NSArray\",R,V_bankConnectDataSpecifiers"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"PSBankConnectAnalyticsConsentCoordinator\",&,N,V_bankConnectAnalyticsConsentCoordinator"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@?,C,N,V_updateHandler"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,N,GisShowingSetupController"
+ "TB,R,N,V_shouldShare"
+ "TB,R,N,V_showPreference"
+ "TCC_ALERT_CANCEL"
+ "TCC_ALERT_TURN_OFF"
+ "Tq,?,N"
+ "Tq,?,N,V_autocapitalizationType"
+ "Tq,?,N,V_autocorrectionType"
+ "Tq,?,N,V_keyboardAppearance"
+ "Tq,?,N,V_keyboardType"
+ "Unable to determine eligibility "
+ "User is eligible"
+ "User is not eligible"
+ "WALLET"
+ "WALLET_NO_ACCOUNTS"
+ "WALLET_SELECTED_ACCOUNTS"
+ "WalletPrivacySettings.FinanceDataAuthorizationLevelController"
+ "_bankConnectAnalyticsConsentCoordinator"
+ "_bankConnectDataSpecifiers"
+ "_offlineLabConsentCoordinator"
+ "_privacyController"
+ "_record"
+ "_shouldShare"
+ "_showPreference"
+ "_syncedKeychainNotifyToken"
+ "_updateHandler"
+ "_walletPrivacyController"
+ "authorizationType"
+ "bankConnectAnalyticsConsentCoordinator"
+ "bankConnectDataSpecifiers"
+ "com.apple.graphic-icon.contactless-and-nfc"
+ "com.apple.graphic-icon.person-passkey"
+ "com.apple.security.keychainchanged"
+ "contentAccessoryPadding"
+ "deactivateKeypad"
+ "defaultTextFieldIndentation"
+ "distributorID"
+ "distributorInfo"
+ "distributorIsFirstPartyApple"
+ "fetchStateWithCompletion:"
+ "iTunesMetadata"
+ "initWithApplicationRecord:"
+ "isContactlessTCCServiceEligible"
+ "isEligibleMailClient"
+ "isEligibleWebBrowser"
+ "isInstalledByThirdPartyMarketplace:"
+ "isManagedAppDistributor"
+ "isSecureElementTCCServiceEligible"
+ "loadOfflineLabSharingPreferenceWithCompletion:"
+ "minTextFieldIndentation"
+ "minimumBadgeWidth"
+ "offlineLabPrivacyBundleIdentifier"
+ "privacyBundleIdentifier"
+ "record"
+ "registerForUpdatesWithHandler:"
+ "saveOfflineLabSharingPermission:withCompletion:"
+ "setBankConnectAnalyticsConsentCoordinator:"
+ "setPinBlocked:"
+ "setShouldShareBankConnectData:specifier:"
+ "setUpdateHandler:"
+ "setUserDidAccept:currentAgreement:completion:"
+ "shouldShare"
+ "shouldShareBankConnectData"
+ "shouldShareBankConnectDataForSpecifier:"
+ "showAboutBankConnectDataSheet"
+ "showBankConnectPreference"
+ "showPreference"
+ "softlink:r:path:/System/Library/Frameworks/FinanceKit.framework/FinanceKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SEService.framework/SEService"
+ "spinnerStyle"
+ "textFieldHorizontalPadding"
+ "updateCachedPermission:"
+ "updateCachedVisibility:"
+ "updateHandler"
+ "v16@?0B8B12"
+ "walletAuthorizationType"
+ "walletSpecifier"
+ "\x91"
- "\x05\x1f"
- "%&"
- "@\"LSApplicationProxy\""
- "Reading AppList from LSApplicationWorkspace"
- "T@\"LSApplicationProxy\",R,N,V_proxy"
- "T@\"NSString\",C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "TB,N,GisSecureTextEntry"
- "TB,N,GisShowingSetupController"
- "Tq,N"
- "Tq,N,V_autocapitalizationType"
- "Tq,N,V_autocorrectionType"
- "Tq,N,V_keyboardType"
- "_handleUpdateForSpecifierID:value:error:"
- "_proxy"
- "_setDaemonPreferenceValue:forKey:completion:"
- "enumerateBundlesOfType:block:"
- "isMailClient"
- "isWebBrowser"
- "localizedNameForContext:"
- "v24@?0@\"LSBundleProxy\"8^B16"

```
