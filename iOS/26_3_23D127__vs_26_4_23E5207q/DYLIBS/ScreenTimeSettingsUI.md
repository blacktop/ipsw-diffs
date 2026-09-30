## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.3.1.0.0
-  __TEXT.__text: 0x124160
-  __TEXT.__auth_stubs: 0x2ec0
-  __TEXT.__objc_methlist: 0xc0cc
-  __TEXT.__const: 0x3cb4
-  __TEXT.__cstring: 0xe769
-  __TEXT.__oslogstring: 0x5a53
-  __TEXT.__gcc_except_tab: 0x11fc
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x4394
-  __TEXT.__constg_swiftt: 0x1504
-  __TEXT.__swift5_reflstr: 0xa10
-  __TEXT.__swift5_fieldmd: 0xbe4
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0x2d8
-  __TEXT.__swift5_capture: 0xcac
-  __TEXT.__swift5_proto: 0xec
+605.4.13.0.0
+  __TEXT.__text: 0x132d6c
+  __TEXT.__auth_stubs: 0x2ed0
+  __TEXT.__objc_methlist: 0xc464
+  __TEXT.__const: 0x3da4
+  __TEXT.__cstring: 0xd055
+  __TEXT.__oslogstring: 0x5953
+  __TEXT.__gcc_except_tab: 0x1234
+  __TEXT.__dlopen_cstrs: 0x10a
+  __TEXT.__swift5_typeref: 0x44ea
+  __TEXT.__constg_swiftt: 0x1538
+  __TEXT.__swift5_reflstr: 0xaf0
+  __TEXT.__swift5_fieldmd: 0xc3c
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_assocty: 0x308
+  __TEXT.__swift5_capture: 0xcb8
+  __TEXT.__swift5_proto: 0xe8
   __TEXT.__swift5_types: 0x104
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift_as_entry: 0x9c
-  __TEXT.__swift_as_ret: 0x90
-  __TEXT.__unwind_info: 0x3b58
-  __TEXT.__eh_frame: 0x20a8
-  __TEXT.__objc_classname: 0x1ddd
-  __TEXT.__objc_methname: 0x22397
-  __TEXT.__objc_methtype: 0x3a1e
-  __TEXT.__objc_stubs: 0x15140
-  __DATA_CONST.__got: 0x1418
-  __DATA_CONST.__const: 0x2518
-  __DATA_CONST.__objc_classlist: 0x758
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__unwind_info: 0x3ff0
+  __TEXT.__eh_frame: 0x20c0
+  __TEXT.__objc_classname: 0x2854
+  __TEXT.__objc_methname: 0x235ad
+  __TEXT.__objc_methtype: 0x4223
+  __TEXT.__objc_stubs: 0x16360
+  __DATA_CONST.__got: 0x1430
+  __DATA_CONST.__const: 0x2640
+  __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ba8
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_arraydata: 0x2d8
-  __AUTH_CONST.__auth_got: 0x1770
-  __AUTH_CONST.__const: 0x31e8
-  __AUTH_CONST.__cfstring: 0xaee0
-  __AUTH_CONST.__objc_const: 0x25768
-  __AUTH_CONST.__objc_intobj: 0x840
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x6d40
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x608
+  __DATA_CONST.__objc_arraydata: 0x2e0
+  __AUTH_CONST.__auth_got: 0x1778
+  __AUTH_CONST.__const: 0x3220
+  __AUTH_CONST.__cfstring: 0xaf80
+  __AUTH_CONST.__objc_const: 0x25da0
+  __AUTH_CONST.__objc_intobj: 0x8d0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x4d88
-  __AUTH.__data: 0xa30
-  __DATA.__objc_ivar: 0xcc0
-  __DATA.__data: 0x2698
-  __DATA.__bss: 0x1e18
-  __DATA.__common: 0xa0
+  __AUTH.__objc_data: 0x5170
+  __AUTH.__data: 0x9a8
+  __DATA.__objc_ivar: 0xcf4
+  __DATA.__data: 0x27d0
+  __DATA.__bss: 0x1e40
+  __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x9b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32D2B078-C2E2-35B8-B38E-66A06FE8D4DD
-  Functions: 6146
-  Symbols:   16231
-  CStrings:  9196
+  UUID: 501BE9B5-3370-38DE-BB37-8805365C0A5D
+  Functions: 6231
+  Symbols:   16692
+  CStrings:  9254
 
Symbols:
+ +[STAuthenticationCoordinator(Factory) createWithPresentingListViewController:]
+ +[STUILog regulatoryRestrictions]
+ -[STAdultVerificationPrompt .cxx_destruct]
+ -[STAdultVerificationPrompt _callCompletionWithOverrideIfSetForSuccess:error:]
+ -[STAdultVerificationPrompt ageAssuranceDidFinishWithResult:viewControllersToRemove:error:]
+ -[STAdultVerificationPrompt ageAssuranceDidFinishWithResult:viewControllersToRemove:error:].cold.1
+ -[STAdultVerificationPrompt authenticateWithContext:completion:]
+ -[STAdultVerificationPrompt completion]
+ -[STAdultVerificationPrompt presentingViewController]
+ -[STAdultVerificationPrompt setCompletion:]
+ -[STAdultVerificationPrompt setPresentingViewController:]
+ -[STAuthenticationContext .cxx_destruct]
+ -[STAuthenticationContext dsid]
+ -[STAuthenticationContext guardianSignInReason]
+ -[STAuthenticationContext initWithDSID:guardianSignInReason:regulatoryRegion:presentingController:]
+ -[STAuthenticationContext presentingController]
+ -[STAuthenticationContext regulatoryRegion]
+ -[STAuthenticationContext setDsid:]
+ -[STAuthenticationContext setGuardianSignInReason:]
+ -[STAuthenticationContext setPresentingController:]
+ -[STAuthenticationContext setRegulatoryRegion:]
+ -[STAuthenticationCoordinator .cxx_destruct]
+ -[STAuthenticationCoordinator _authenticateWithContext:prompts:promptIndex:completion:]
+ -[STAuthenticationCoordinator _authenticateWithContext:prompts:promptIndex:completion:].cold.1
+ -[STAuthenticationCoordinator authenticateWithContext:promptTypes:completion:]
+ -[STAuthenticationCoordinator authenticateWithContext:promptTypes:completion:].cold.1
+ -[STAuthenticationCoordinator initWithPromptByType:]
+ -[STAuthenticationCoordinator promptByType]
+ -[STAuthenticationCoordinator setPromptByType:]
+ -[STAuthenticationPINPrompt .cxx_destruct]
+ -[STAuthenticationPINPrompt authenticateWithContext:completion:]
+ -[STAuthenticationPINPrompt initWithListController:]
+ -[STAuthenticationPINPrompt listController]
+ -[STAuthenticationPINPrompt setListController:]
+ -[STAuthenticationParentSignInPrompt .cxx_destruct]
+ -[STAuthenticationParentSignInPrompt authenticateWithContext:completion:]
+ -[STAuthenticationParentSignInPrompt parentAuthenticationPrompt]
+ -[STAuthenticationParentSignInPrompt setParentAuthenticationPrompt:]
+ -[STCommunicationSafetyListController _authenticationContext]
+ -[STCommunicationSafetyListController _createAdditionalFooterIfNeeded]
+ -[STCommunicationSafetyListController _guardianSignInReason]
+ -[STCommunicationSafetyListController _isEditable]
+ -[STCommunicationSafetyListController authenticationCoordinator]
+ -[STCommunicationSafetyListController setAuthenticationCoordinator:]
+ -[STCommunicationSafetyViewModel regulatoryCommSafetyPolicy]
+ -[STCommunicationSafetyViewModel setRegulatoryCommSafetyPolicy:]
+ -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:]
+ -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:modelUpdatedHandler:]
+ -[STCommunicationSafetyViewModelCoordinator regulatoryUIPolicyProviderDidUpdate:]
+ -[STCommunicationSafetyViewModelCoordinator regulatoryUIPolicyProvider]
+ -[STConnectToFamilyHelper handlePromptAction]
+ -[STConnectToFamilyHelper handlePromptAction].cold.1
+ -[STConnectToFamilyHelper handlePromptAction].cold.2
+ -[STConnectToFamilyPrompt authenticateWithContext:completion:]
+ -[STConnectToFamilyPrompt authenticateWithContext:completion:].cold.1
+ -[STContentPrivacyAllowedAppsDetailController authenticationCoordinator]
+ -[STContentPrivacyAllowedAppsDetailController setAuthenticationCoordinator:]
+ -[STContentPrivacyListController _guardianSignInReason]
+ -[STContentPrivacyListController authenticationCoordinator]
+ -[STContentPrivacyListController setAuthenticationCoordinator:]
+ -[STContentPrivacyViewModel allowedAppsShowsFullList]
+ -[STContentPrivacyViewModel allowedAppsValueChangePrompts]
+ -[STContentPrivacyViewModel appsRatingEditable]
+ -[STContentPrivacyViewModel appsRatingForcedToDoNotAllow]
+ -[STContentPrivacyViewModel regulatoryWebContentFilterPolicy]
+ -[STContentPrivacyViewModel setAllowedAppsShowsFullList:]
+ -[STContentPrivacyViewModel setAllowedAppsValueChangePrompts:]
+ -[STContentPrivacyViewModel setAppsRatingEditable:]
+ -[STContentPrivacyViewModel setAppsRatingForcedToDoNotAllow:]
+ -[STContentPrivacyViewModel setRegulatoryWebContentFilterPolicy:]
+ -[STContentPrivacyViewModel setTopLevelRestrictionsValueChangePrompts:]
+ -[STContentPrivacyViewModel topLevelRestrictionsValueChangePrompts]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]
+ -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:]
+ -[STContentPrivacyViewModelCoordinator regulatoryUIPolicyProviderDidUpdate:]
+ -[STContentPrivacyViewModelCoordinator regulatoryUIPolicyProvider]
+ -[STRestrictingApplicationsGroupSpecifierProvider _isEligibleOrApprovedForDataAccess:]
+ -[STRestrictingApplicationsGroupSpecifierProvider _isEligibleOrApprovedForDataAccess:].cold.1
+ -[STRestrictingApplicationsGroupSpecifierProvider _isEligibleOrApprovedForDataAccess:].cold.2
+ -[STRestrictingApplicationsGroupSpecifierProvider _isEligibleOrApprovedForDataAccess:].cold.3
+ -[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]
+ -[STRestrictingApplicationsGroupSpecifierProvider _updateDataAccessLevelForSpecifier:usingRecord:]
+ -[STRestrictingApplicationsGroupSpecifierProvider eligibilityChangedNotificationToken]
+ -[STRestrictingApplicationsGroupSpecifierProvider setEligibilityChangedNotificationToken:]
+ -[STRootViewModelCoordinator _regulatoryContext]
+ -[STRootViewModelCoordinator regulatoryUIPolicyProvider]
+ -[STRootViewModelCoordinator setRegulatoryUIPolicyProvider:]
+ -[STRootViewModelCoordinator startRefreshRegulatoryPolicy]
+ -[STScreenTimeUsageGroupSpecifierProvider reloadSummaryGraph]
+ -[STWebFilterDetailController _createAdditionalFooterIfNeeded]
+ -[STWebFilterDetailController _guardianSignInReason]
+ -[STWebFilterDetailController _isEditable]
+ -[STWebFilterDetailController authenticationCoordinator]
+ -[STWebFilterDetailController setAuthenticationCoordinator:]
+ GCC_except_table113
+ GCC_except_table195
+ GCC_except_table20
+ GCC_except_table204
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table36
+ _AppleIDSetupLibraryCore.frameworkLibrary
+ _AppleIDSetupUILibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_STAdultVerificationPrompt
+ _OBJC_CLASS_$_STAuthenticationContext
+ _OBJC_CLASS_$_STAuthenticationCoordinator
+ _OBJC_CLASS_$_STAuthenticationPINPrompt
+ _OBJC_CLASS_$_STAuthenticationParentSignInPrompt
+ _OBJC_CLASS_$_STBannerCell
+ _OBJC_CLASS_$_STConnectToFamilyPrompt
+ _OBJC_CLASS_$_STRegulatoryPolicy
+ _OBJC_CLASS_$_STRegulatoryUIPolicyProvider
+ _OBJC_CLASS_$__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ _OBJC_CLASS_$__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ _OBJC_IVAR_$_STAdultVerificationPrompt._completion
+ _OBJC_IVAR_$_STAdultVerificationPrompt._presentingViewController
+ _OBJC_IVAR_$_STAuthenticationContext._dsid
+ _OBJC_IVAR_$_STAuthenticationContext._guardianSignInReason
+ _OBJC_IVAR_$_STAuthenticationContext._presentingController
+ _OBJC_IVAR_$_STAuthenticationContext._regulatoryRegion
+ _OBJC_IVAR_$_STAuthenticationCoordinator._promptByType
+ _OBJC_IVAR_$_STAuthenticationPINPrompt._listController
+ _OBJC_IVAR_$_STAuthenticationParentSignInPrompt._parentAuthenticationPrompt
+ _OBJC_IVAR_$_STCommunicationSafetyListController._authenticationCoordinator
+ _OBJC_IVAR_$_STCommunicationSafetyViewModel._regulatoryCommSafetyPolicy
+ _OBJC_IVAR_$_STCommunicationSafetyViewModelCoordinator._regulatoryUIPolicyProvider
+ _OBJC_IVAR_$_STContentPrivacyAllowedAppsDetailController._authenticationCoordinator
+ _OBJC_IVAR_$_STContentPrivacyListController._authenticationCoordinator
+ _OBJC_IVAR_$_STContentPrivacyViewModel._allowedAppsShowsFullList
+ _OBJC_IVAR_$_STContentPrivacyViewModel._allowedAppsValueChangePrompts
+ _OBJC_IVAR_$_STContentPrivacyViewModel._appsRatingEditable
+ _OBJC_IVAR_$_STContentPrivacyViewModel._appsRatingForcedToDoNotAllow
+ _OBJC_IVAR_$_STContentPrivacyViewModel._regulatoryWebContentFilterPolicy
+ _OBJC_IVAR_$_STContentPrivacyViewModel._topLevelRestrictionsValueChangePrompts
+ _OBJC_IVAR_$_STContentPrivacyViewModelCoordinator._regulatoryUIPolicyProvider
+ _OBJC_IVAR_$_STRestrictingApplicationsGroupSpecifierProvider._eligibilityChangedNotificationToken
+ _OBJC_IVAR_$_STRootViewModelCoordinator._regulatoryUIPolicyProvider
+ _OBJC_IVAR_$_STWebFilterDetailController._authenticationCoordinator
+ _OBJC_METACLASS_$_STAdultVerificationPrompt
+ _OBJC_METACLASS_$_STAuthenticationContext
+ _OBJC_METACLASS_$_STAuthenticationCoordinator
+ _OBJC_METACLASS_$_STAuthenticationPINPrompt
+ _OBJC_METACLASS_$_STAuthenticationParentSignInPrompt
+ _OBJC_METACLASS_$_STBannerCell
+ _OBJC_METACLASS_$_STConnectToFamilyPrompt
+ _OBJC_METACLASS_$_STRegulatoryUIPolicyProvider
+ _OBJC_METACLASS_$__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ _OBJC_METACLASS_$__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _STRegionRatingsDontAllowValue
+ _STSystemRatingsAppsRatingPayloadKey
+ _STSystemRatingsConfigurationName
+ __CLASS_METHODS_STBannerCell
+ __DATA_STBannerCell
+ __DATA_STRegulatoryUIPolicyProvider
+ __DATA__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ __DATA__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ __INSTANCE_METHODS_STBannerCell
+ __INSTANCE_METHODS_STRegulatoryUIPolicyProvider
+ __INSTANCE_METHODS__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ __INSTANCE_METHODS__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ __IVARS_STRegulatoryUIPolicyProvider
+ __IVARS__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ __IVARS__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ __METACLASS_DATA_STBannerCell
+ __METACLASS_DATA_STRegulatoryUIPolicyProvider
+ __METACLASS_DATA__TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader
+ __METACLASS_DATA__TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext
+ __OBJC_$_CLASS_METHODS_STAuthenticationCoordinator(Factory)
+ __OBJC_$_INSTANCE_METHODS_STAdultVerificationPrompt
+ __OBJC_$_INSTANCE_METHODS_STAuthenticationContext
+ __OBJC_$_INSTANCE_METHODS_STAuthenticationCoordinator
+ __OBJC_$_INSTANCE_METHODS_STAuthenticationPINPrompt
+ __OBJC_$_INSTANCE_METHODS_STAuthenticationParentSignInPrompt
+ __OBJC_$_INSTANCE_METHODS_STConnectToFamilyPrompt
+ __OBJC_$_INSTANCE_VARIABLES_STAdultVerificationPrompt
+ __OBJC_$_INSTANCE_VARIABLES_STAuthenticationContext
+ __OBJC_$_INSTANCE_VARIABLES_STAuthenticationCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_STAuthenticationPINPrompt
+ __OBJC_$_INSTANCE_VARIABLES_STAuthenticationParentSignInPrompt
+ __OBJC_$_PROP_LIST_STAdultVerificationPrompt
+ __OBJC_$_PROP_LIST_STAuthenticationContext
+ __OBJC_$_PROP_LIST_STAuthenticationCoordinator
+ __OBJC_$_PROP_LIST_STAuthenticationPINPrompt
+ __OBJC_$_PROP_LIST_STAuthenticationParentSignInPrompt
+ __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.193
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1023
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AISAgeAssuranceFlowPresenterDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STAuthenticationPrompt
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STBannerActionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STRegulatoryUIPolicyObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STRegulatoryUIPolicyProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AISAgeAssuranceFlowPresenterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STAuthenticationPrompt
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STBannerActionHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STRegulatoryUIPolicyObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STRegulatoryUIPolicyProviding
+ __OBJC_$_PROTOCOL_REFS_AISAgeAssuranceFlowPresenterDelegate
+ __OBJC_$_PROTOCOL_REFS_STBannerActionHandler
+ __OBJC_$_PROTOCOL_REFS_STRegulatoryUIPolicyObserving
+ __OBJC_$_PROTOCOL_REFS_STRegulatoryUIPolicyProviding
+ __OBJC_CLASS_PROTOCOLS_$_STAdultVerificationPrompt
+ __OBJC_CLASS_PROTOCOLS_$_STAuthenticationPINPrompt
+ __OBJC_CLASS_PROTOCOLS_$_STAuthenticationParentSignInPrompt
+ __OBJC_CLASS_PROTOCOLS_$_STConnectToFamilyPrompt
+ __OBJC_CLASS_RO_$_STAdultVerificationPrompt
+ __OBJC_CLASS_RO_$_STAuthenticationContext
+ __OBJC_CLASS_RO_$_STAuthenticationCoordinator
+ __OBJC_CLASS_RO_$_STAuthenticationPINPrompt
+ __OBJC_CLASS_RO_$_STAuthenticationParentSignInPrompt
+ __OBJC_CLASS_RO_$_STConnectToFamilyPrompt
+ __OBJC_LABEL_PROTOCOL_$_AISAgeAssuranceFlowPresenterDelegate
+ __OBJC_LABEL_PROTOCOL_$_STAuthenticationPrompt
+ __OBJC_LABEL_PROTOCOL_$_STBannerActionHandler
+ __OBJC_LABEL_PROTOCOL_$_STRegulatoryUIPolicyObserving
+ __OBJC_LABEL_PROTOCOL_$_STRegulatoryUIPolicyProviding
+ __OBJC_METACLASS_RO_$_STAdultVerificationPrompt
+ __OBJC_METACLASS_RO_$_STAuthenticationContext
+ __OBJC_METACLASS_RO_$_STAuthenticationCoordinator
+ __OBJC_METACLASS_RO_$_STAuthenticationPINPrompt
+ __OBJC_METACLASS_RO_$_STAuthenticationParentSignInPrompt
+ __OBJC_METACLASS_RO_$_STConnectToFamilyPrompt
+ __OBJC_PROTOCOL_$_AISAgeAssuranceFlowPresenterDelegate
+ __OBJC_PROTOCOL_$_STAuthenticationPrompt
+ __OBJC_PROTOCOL_$_STBannerActionHandler
+ __OBJC_PROTOCOL_$_STRegulatoryUIPolicyObserving
+ __OBJC_PROTOCOL_$_STRegulatoryUIPolicyProviding
+ __PROPERTIES_STRegulatoryUIPolicyProvider
+ __PROTOCOLS_STRegulatoryUIPolicyProvider
+ __PROTOCOLS_STRegulatoryUIPolicyProvider.2
+ ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.71
+ ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.72
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke
+ ___137-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:]_block_invoke.cold.1
+ ___143-[STCommunicationSafetyViewModelCoordinator saveCommunicationSafetyReceivingRestricted:communicationSafetySendingRestricted:completionHandler:]_block_invoke.74
+ ___198-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:]_block_invoke
+ ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.427
+ ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.427.cold.1
+ ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.503
+ ___45-[STConnectToFamilyHelper handlePromptAction]_block_invoke
+ ___45-[STConnectToFamilyHelper handlePromptAction]_block_invoke.cold.1
+ ___55-[STRestrictingApplicationsGroupSpecifierProvider init]_block_invoke_3
+ ___58-[STRootViewModelCoordinator startRefreshRegulatoryPolicy]_block_invoke
+ ___59-[STCommunicationSafetyViewModelCoordinator _loadViewModel]_block_invoke.68
+ ___62-[STConnectToFamilyPrompt authenticateWithContext:completion:]_block_invoke
+ ___62-[STConnectToFamilyPrompt authenticateWithContext:completion:]_block_invoke.cold.1
+ ___64-[STAdultVerificationPrompt authenticateWithContext:completion:]_block_invoke
+ ___64-[STAdultVerificationPrompt authenticateWithContext:completion:]_block_invoke.20
+ ___64-[STAdultVerificationPrompt authenticateWithContext:completion:]_block_invoke_2
+ ___64-[STAdultVerificationPrompt authenticateWithContext:completion:]_block_invoke_2.cold.1
+ ___69-[STRootViewModelCoordinator loadRegionRatingsWithCompletionHandler:]_block_invoke.460
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.832
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.832.cold.1
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.833
+ ___76-[STContentPrivacyViewModelCoordinator regulatoryUIPolicyProviderDidUpdate:]_block_invoke
+ ___78-[STAuthenticationCoordinator authenticateWithContext:promptTypes:completion:]_block_invoke
+ ___78-[STAuthenticationCoordinator authenticateWithContext:promptTypes:completion:]_block_invoke_2
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.434
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.434.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.441
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.441.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.442
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.442.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.445
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.445.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.450
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.450.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.451
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.451.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.454
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.454.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.455
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.841
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.840
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.852
+ ___87-[STAuthenticationCoordinator _authenticateWithContext:prompts:promptIndex:completion:]_block_invoke
+ ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.433
+ ___91-[STAdultVerificationPrompt ageAssuranceDidFinishWithResult:viewControllersToRemove:error:]_block_invoke
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.40
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.40.cold.1
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.42
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.42.cold.1
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke.cold.1
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2.41
+ ___93-[STRestrictingApplicationsGroupSpecifierProvider _performFamilyControlsChange:forSpecifier:]_block_invoke_2.43
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.431
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.431.cold.1
+ ___AppleIDSetupLibraryCore_block_invoke
+ ___AppleIDSetupUILibraryCore_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
+ ___block_descriptor_40_e8_32s_e28_v16?0"STRegulatoryPolicy"8ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_41_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8ls32l8w40l8
+ ___block_descriptor_48_e8_32bs40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e26_v16?0"UIViewController"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1026
+ ___block_literal_global.447
+ ___block_literal_global.453
+ ___block_literal_global.727
+ ___block_literal_global.857
+ ___getAISAgeAssuranceContextClass_block_invoke
+ ___getAISAgeAssuranceContextClass_block_invoke.cold.1
+ ___getAISAgeAssuranceContextClass_block_invoke.cold.2
+ ___getAISAgeAssuranceFlowPresenterClass_block_invoke
+ ___getAISAgeAssuranceFlowPresenterClass_block_invoke.cold.1
+ ___getAISAgeAssuranceFlowPresenterClass_block_invoke.cold.2
+ _associated conformance 20ScreenTimeSettingsUI16STBannerCellViewV05SwiftD00G0AA4BodyAdEP_AdE
+ _associated conformance 20ScreenTimeSettingsUI23STRegulatoryAccountTypeOSHAASQ
+ _audit_stringAppleIDSetup
+ _audit_stringAppleIDSetupUI
+ _block_copy_helper.102
+ _block_copy_helper.106
+ _block_copy_helper.120
+ _block_copy_helper.124
+ _block_copy_helper.28
+ _block_copy_helper.35
+ _block_copy_helper.62
+ _block_copy_helper.76
+ _block_copy_helper.79
+ _block_copy_helper.85
+ _block_copy_helper.93
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.104
+ _block_descriptor.108
+ _block_descriptor.122
+ _block_descriptor.126
+ _block_descriptor.30
+ _block_descriptor.37
+ _block_descriptor.64
+ _block_descriptor.78
+ _block_descriptor.81
+ _block_descriptor.87
+ _block_descriptor.95
+ _block_destroy_helper.100
+ _block_destroy_helper.103
+ _block_destroy_helper.107
+ _block_destroy_helper.121
+ _block_destroy_helper.125
+ _block_destroy_helper.29
+ _block_destroy_helper.36
+ _block_destroy_helper.63
+ _block_destroy_helper.77
+ _block_destroy_helper.80
+ _block_destroy_helper.86
+ _block_destroy_helper.94
+ _flat unique So21STBannerActionHandler_p
+ _flat unique So29STRegulatoryUIPolicyObserving_p
+ _getAISAgeAssuranceContextClass.softClass
+ _getAISAgeAssuranceFlowPresenterClass.softClass
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOQr.4
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.2
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOqd0__AaBHC.5
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.3
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4FormVyAA9TupleViewVyAA7SectionVyAA4TextVACyAA0G0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQOyAA0L0VyAKSiSgAA7ForEachVySnySiGSiAmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAK_SiQo_GG_AA04MenulK0VQo_AA32_EnvironmentKeyTransformModifierVySbGGAKSgG_AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQOyAIyAkTySay018ScreenTimeSettingsB012ExceptionAppVGSSA10_014STAppExceptionG0VGAKG_AA05PlainyK0VQo_SgAIyAkTySayA10_17AboveAgeRatingAppVGSSA10_021STPendingAppExceptionG0VGAA05EmptyG0VGSgtGGA4_GAaLHPA33_AaLHPyHC_A4_AA0gV0HPyHCHC.66
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6HStackVyAA9TupleViewVyACyACyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAA12_FrameLayoutVGAA016_ForegroundStyleL0VyAA09TintShapeQ0VGG_ACyAA6VStackVyAGyAA4TextV_ACyA1_AKyAA0U9AlignmentOGGtGGAA05_FlexnO0VGACyACyApUyAA03AnysQ0VGGARGtGGAA08_PaddingO0VGAA011_BackgroundL0VyAA06StrokesG0VyAA16RoundedRectangleVA12_AA05EmptyG0VGGGAA0G0HPA20_AAA32_HPA17_AAA32_HPyHC_A19_AA0gL0HPyHCHC_A30_AAA33_HPyHCHC.48
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA12ProgressViewVyAA05EmptyF0VAGGAA0F0PAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA08ModifiedD0VyAjAE20listHasStackBehaviorQryFQOyARyAjAE06scrollD10BackgroundyQrAA10VisibilityOFQOyAA4FormVyAA05TupleF0Vy018ScreenTimeSettingsB00D21RestrictionAgeSectionV_A_0dZ7SectionVyAGA_0dZ4CellVySiA_7AppIconVyAA03AnyF0VGAA5ColorVGAGGA3_yAgZyA13__A5_ySiA_17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLVAA14LinearGradientVGA20_A5_ySbA10_A12_GtGAGGA3_yAgZyA5_ySbAA14GeometryReaderVyARyARyARyAA5ImageVAA12_FrameLayoutVGA29_GAA11_ClipEffectVyAA9RectangleVGGGA12_G_A5_ySbA17_A19_GA5_ySbA25_yA31_GA19_GtGAGGA3_yAgZyA5_ySbA17_A12_G_A45_A45_SgtGAGGA3_yAGA45_AA4TextVGA3_yAGA50_AGGtGG_Qo_AA16_FixedSizeLayoutVG_Qo_A_0Z10ResetAlertVG_Qo_GAaIHPAhaIHPyHC_qd__AaIHD2_A63_HOHC.134
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA14GeometryReaderVyAA08ModifiedD0VyAGyAGyAA5ImageVAA12_FrameLayoutVGAKGAA11_ClipEffectVyAA9RectangleVGGGAIGAA4ViewHPAtaVHPyHC_AiaVHPyHCHC.13
+ _get_witness_table 7SwiftUI4ViewRzlqd__AaBHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA6VStackVyAA19_ConditionalContentVy018ScreenTimeSettingsB012AppIconImage33_F7421E97E89C76E374C87DDE77856B66LLVxGG_Qo_HO.9
+ _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA0E0PAAE12onTapGesture5count7performQrSi_yyctFQOy018ScreenTimeSettingsB09PickerRow33_02F314FBF7653240FBB92EA68B618E57LLV_Qo__AOtGGAaFHPyHC.41
+ _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAA6HStackVyAEyAGyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGGAA06_FrameL0VG_ACyAEyAA4TextV_AGyAzPyAA0S9AlignmentOGGtGGAA6SpacerVtGGAA08_PaddingL0VGA10_G_AGyAA7DividerVA10_GAGyAGyAGyAGyAGyAA6ButtonVyAZGATGAPyAA4FontVSgGGAA05_FlexrL0VGA10_GA10_GtGGAA0E0HPyHC.9
+ _objc_msgSend$DeviceIdentifierByChildDSID
+ _objc_msgSend$DeviceIdentifierLocalUser
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_authenticateWithContext:prompts:promptIndex:completion:
+ _objc_msgSend$_authenticationContext
+ _objc_msgSend$_callCompletionWithOverrideIfSetForSuccess:error:
+ _objc_msgSend$_createAdditionalFooterIfNeeded
+ _objc_msgSend$_guardianSignInReason
+ _objc_msgSend$_isEditable
+ _objc_msgSend$_isEligibleOrApprovedForDataAccess:
+ _objc_msgSend$_performFamilyControlsChange:forSpecifier:
+ _objc_msgSend$_regulatoryContext
+ _objc_msgSend$_updateDataAccessLevelForSpecifier:usingRecord:
+ _objc_msgSend$activate
+ _objc_msgSend$adamID
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$age
+ _objc_msgSend$allowedApps
+ _objc_msgSend$allowedAppsShowsFullList
+ _objc_msgSend$allowedAppsValueChangePrompts
+ _objc_msgSend$animateToStateName:completionHandler:
+ _objc_msgSend$appInfoForBundleIdentifier:adamId:distributorId:
+ _objc_msgSend$applicationState
+ _objc_msgSend$appsAboveAgeRating
+ _objc_msgSend$appsRatingEditable
+ _objc_msgSend$appsRatingForcedToDoNotAllow
+ _objc_msgSend$authenticateWithContext:promptTypes:completion:
+ _objc_msgSend$authenticationCoordinator
+ _objc_msgSend$availablePresets
+ _objc_msgSend$bannerCellWithIdentifier:title:subtitle:buttonTitle:actionHandler:
+ _objc_msgSend$beginAgeAssuranceWithContext:completion:
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$client
+ _objc_msgSend$commSafety
+ _objc_msgSend$computedProperties
+ _objc_msgSend$configuration
+ _objc_msgSend$connectToFamilyBanner
+ _objc_msgSend$connectToFamilyBannerDescription
+ _objc_msgSend$connectionError
+ _objc_msgSend$createWithPresentingListViewController:
+ _objc_msgSend$currentPolicy
+ _objc_msgSend$defaultValueForRestrictionIdentifier:
+ _objc_msgSend$deleteAppException:completion:
+ _objc_msgSend$deleteExceptionFor:completionHandler:
+ _objc_msgSend$dependencies
+ _objc_msgSend$disableActions
+ _objc_msgSend$distributorID
+ _objc_msgSend$downtimeFromIntroductionViewModel:
+ _objc_msgSend$editable
+ _objc_msgSend$enablementState
+ _objc_msgSend$entitlements
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$exceptionConnection
+ _objc_msgSend$exceptionsListChangedHandler
+ _objc_msgSend$fallbackPolicyWithContext:
+ _objc_msgSend$fetchAllAppExceptionsForRequesterDSID:completionHandler:
+ _objc_msgSend$fetchAppExceptionsWithCompletion:
+ _objc_msgSend$fetchCachedPresetsWithCompletion:
+ _objc_msgSend$fetchPresetsWithCompletion:
+ _objc_msgSend$footerInfo
+ _objc_msgSend$forcedToEnabled
+ _objc_msgSend$forcedToLimitAdultWebsites
+ _objc_msgSend$fullName
+ _objc_msgSend$guardianSignInReason
+ _objc_msgSend$handlePromptAction
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$imageForBundleIdentifier:completionHandler:
+ _objc_msgSend$initWithAgeAssuranceContext:
+ _objc_msgSend$initWithChildAge:
+ _objc_msgSend$initWithChildAge:storeFront:version:
+ _objc_msgSend$initWithChildName:forceParentalControls:continueHandler:endHandler:
+ _objc_msgSend$initWithChildName:limitType:continueHandler:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDSID:guardianSignInReason:regulatoryRegion:presentingController:
+ _objc_msgSend$initWithDsid:childAge:isInitialSetup:restrictionsToPresetMappingViewModel:restrictionsDefaultValueProvider:agePresetsAnalytics:
+ _objc_msgSend$initWithFamilyMember:
+ _objc_msgSend$initWithFamilyMember:storeFront:version:
+ _objc_msgSend$initWithFlowType:verificationType:
+ _objc_msgSend$initWithInitialPolicy:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithIntroductionModel:childName:askForRecoveryAppleID:altDSID:isChildOrNotSignedIntoiCloud:continueHandler:
+ _objc_msgSend$initWithIntroductionModel:childName:continueHandler:
+ _objc_msgSend$initWithIsLocalDevice:
+ _objc_msgSend$initWithIsLocalUser:userDSID:accountType:isInFamily:isManaged:hasScreenTimePasscode:
+ _objc_msgSend$initWithManagedUserDSID:isLocalDevice:
+ _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:
+ _objc_msgSend$initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:
+ _objc_msgSend$initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:modelUpdatedHandler:
+ _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:
+ _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:
+ _objc_msgSend$initWithPromptByType:
+ _objc_msgSend$initWithSessionId:
+ _objc_msgSend$initWithSessionId:isInitialSetup:
+ _objc_msgSend$initWithSessionId:lowerBoundAgeRange:upperBoundAgeRange:
+ _objc_msgSend$initWithSessionId:recommendedPresetId:fieldName:recommendedValue:selectedValue:
+ _objc_msgSend$initWithSessionId:selectionType:lowerBoundAgeRange:upperBoundAgeRange:
+ _objc_msgSend$initWithTitle:detailText:icon:contentLayout:
+ _objc_msgSend$initWithTitle:detailText:symbolName:contentLayout:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isInstalledFromDistributorOrWeb
+ _objc_msgSend$limitType
+ _objc_msgSend$loadPolicyWithContext:completion:
+ _objc_msgSend$loadPresetMatchingCurrentRestrictionsWithCompletionHandler:
+ _objc_msgSend$localizedMessage
+ _objc_msgSend$localizedName
+ _objc_msgSend$maxAge
+ _objc_msgSend$members
+ _objc_msgSend$minAge
+ _objc_msgSend$nextObject
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$observers
+ _objc_msgSend$openURL:configuration:error:
+ _objc_msgSend$packageRootLayer
+ _objc_msgSend$packageWithContentsOfURL:type:options:error:
+ _objc_msgSend$policy
+ _objc_msgSend$presentFromViewController:signInReason:completion:
+ _objc_msgSend$presentingController
+ _objc_msgSend$presetValueForKey:
+ _objc_msgSend$presetValueForKey:userValueProvider:
+ _objc_msgSend$promptByType
+ _objc_msgSend$ratingValue
+ _objc_msgSend$regulatoryCommSafetyPolicy
+ _objc_msgSend$regulatoryRegionAACID
+ _objc_msgSend$regulatoryRestrictions
+ _objc_msgSend$regulatoryUIPolicyProvider
+ _objc_msgSend$regulatoryUIPolicyProviderDidUpdate:
+ _objc_msgSend$regulatoryWebContentFilterPolicy
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$requestDataAccessAuthorizationForRecordIdentifier:completionHandler:
+ _objc_msgSend$restrictionReason
+ _objc_msgSend$rootLayer
+ _objc_msgSend$secondarySystemBackgroundColor
+ _objc_msgSend$sendChooseAgeButtonTappedAnalyticsEvent
+ _objc_msgSend$sendEnabledRestrictionsEventWithSelectionType:lowerBound:upperBound:
+ _objc_msgSend$sendPresetsValueChangedAnalyticsEventWithRecommendedPresetId:fieldName:recomendedValue:selectedValue:
+ _objc_msgSend$sendPresetsViewedAnalyticsEventWithIsInitialSetup:
+ _objc_msgSend$sendResetAgePresetSelectedAnalyticsEvent
+ _objc_msgSend$sendSelectedAgeRangeAnalyticsEventWithLowerBound:upperBound:
+ _objc_msgSend$sendSkippedAnalyticsEvent
+ _objc_msgSend$setAllowedAppsShowsFullList:
+ _objc_msgSend$setAllowedAppsValueChangePrompts:
+ _objc_msgSend$setAppsRatingEditable:
+ _objc_msgSend$setAppsRatingForcedToDoNotAllow:
+ _objc_msgSend$setBackButtonTitle:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setCompletion:
+ _objc_msgSend$setConnectionError:
+ _objc_msgSend$setContentsGravity:
+ _objc_msgSend$setCustomShieldAssetID:
+ _objc_msgSend$setDisableActions:
+ _objc_msgSend$setExceptionsListChangedHandler:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setFillMode:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$setParentAuthenticationPrompt:
+ _objc_msgSend$setPolicy:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setRasterizationScale:
+ _objc_msgSend$setRegulatoryCommSafetyPolicy:
+ _objc_msgSend$setRegulatoryWebContentFilterPolicy:
+ _objc_msgSend$setTopLevelRestrictionsValueChangePrompts:
+ _objc_msgSend$showMessage
+ _objc_msgSend$showsFullList
+ _objc_msgSend$sourceWithIdentifier:
+ _objc_msgSend$st_getUserAgeRange:forAccountWithAltDSID:error:
+ _objc_msgSend$startRefreshRegulatoryPolicy
+ _objc_msgSend$startRequestWithCompletionHandler:
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$storefront
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$synchronousExceptionServiceWithErrorHandler:
+ _objc_msgSend$topLevelRestrictionsValueChangePrompts
+ _objc_msgSend$updateIntroductionViewModel:withDowntime:
+ _objc_msgSend$updatePolicy:
+ _objc_msgSend$updatedRestrictions:withImageGenerationRestriction:
+ _objc_msgSend$updatedRestrictions:withValueByAgePresetKey:
+ _objc_msgSend$valueChangePrompts
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSend$webContentFilter
+ _objectdestroy.33Tm
+ _objectdestroy.7Tm
+ _swift_bridgeObjectRelease_n
+ _symbolic So12STBannerCellCm
+ _symbolic So18STRegulatoryPolicyCIegg_
+ _symbolic So18STRegulatoryPolicyCIeyBy_
+ _symbolic So18STRegulatoryPolicyC___________tc 15ScreenTimeSwift23RegulatoryConfigurationV AA0D7ContextV
+ _symbolic So18STRegulatoryPolicyC_____c 15ScreenTimeSwift17RegulatoryContextV
+ _symbolic _____ 15ScreenTimeSwift16RegulationLoaderV
+ _symbolic _____ 15ScreenTimeSwift21RegulatoryAccountTypeO
+ _symbolic _____ 20ScreenTimeSettingsUI16STBannerCellViewV
+ _symbolic _____ 20ScreenTimeSettingsUI23STRegulatoryAccountTypeO
+ _symbolic _____ 20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoaderC
+ _symbolic _____ 20ScreenTimeSettingsUI27STRegulatoryUIPolicyContextC
+ _symbolic __________IegHnr_ 15ScreenTimeSwift23RegulationLoaderOptionsV AA23RegulatoryConfigurationV
+ _symbolic __________YaKc 15ScreenTimeSwift23RegulatoryConfigurationV AA23RegulationLoaderOptionsV
+ _symbolic ______p So21STBannerActionHandlerP
+ _symbolic ______p So29STRegulatoryUIPolicyObservingP
+ _symbolic _____yAAyAAyAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____G_____yAIGG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA13_OffsetEffectV AA14_PaddingLayoutV AA011_BackgroundlI0V AA05_ClipO0V AA6CircleV
+ _symbolic _____yAAyAAyAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____yAIGG_____y_____GGALG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA14_PaddingLayoutV AA011_BackgroundlI0V AA11_ClipEffectV AA6CircleV
+ _symbolic _____yAAyAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____G_____yAIGG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA13_OffsetEffectV AA14_PaddingLayoutV AA011_BackgroundlI0V
+ _symbolic _____yAAyAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____yAIGG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA14_PaddingLayoutV AA011_BackgroundlI0V AA11_ClipEffectV AA6CircleV
+ _symbolic _____yAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____G 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA13_OffsetEffectV AA14_PaddingLayoutV
+ _symbolic _____yAAyAAyAAy__________y_____SgGG_____y_____GG_____G_____yAIGG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA14_PaddingLayoutV AA011_BackgroundlI0V
+ _symbolic _____yAAyAAy__________GACG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV
+ _symbolic _____yAAyAAy__________G_____y_____SgGG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameH0V
+ _symbolic _____yAAyAAy__________y_____SgGG_____y_____GG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV AA14_PaddingLayoutV
+ _symbolic _____yAAy__________GACG 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV
+ _symbolic _____yAAy__________ySiSgGGACy_____SgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA5ColorV
+ _symbolic _____yAAy__________y_____SgGG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV
+ _symbolic _____yAAy_____y_____yAAyAAyAAy__________G_____y_____SgGG_____G______yACy______AAyAoGy_____GGtGG_____tGG_____GAXG 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameK0V AA6VStackV AA4TextV AA0S9AlignmentO AA6SpacerV AA08_PaddingK0V
+ _symbolic _____yAAy_____y_____yAAyAAyAAy__________G_____y_____SgGG_____G______yACy______AAyAoGy_____GGtGG_____tGG_____GAXG_AAy_____AXGAAyAAyAAyAAyAAy_____yAOGAJGAGy_____SgGG_____GAXGAXGt 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameK0V AA6VStackV AA4TextV AA0S9AlignmentO AA6SpacerV AA08_PaddingK0V AA7DividerV AA6ButtonV AA4FontV AA05_FlexqK0V
+ _symbolic _____y__________G 7SwiftUI22UIHostingConfigurationV 018ScreenTimeSettingsB016STBannerCellViewV AA05EmptyJ0V
+ _symbolic _____y___________y_____yADy_____yACyADyADyADy__________G_____y_____SgGG_____G______yACy______ADyAqIy_____GGtGG_____tGG_____GAZG_ADy_____AZGADyADyADyADyADy_____yAQGALGAIy_____SgGG_____GAZGAZGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA15ModifiedContentV AA6HStackV AA5ImageV AA012_AspectRatioG0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameG0V AA0F0V AA4TextV AA0U9AlignmentO AA6SpacerV AA08_PaddingG0V AA7DividerV AA6ButtonV AA4FontV AA05_FlextG0V
+ _symbolic _____y__________y_____y_____yABSiSg_____ySnySiGSi_____yAB_SiQo_GG______Qo______ySbGGABSgG 7SwiftUI7SectionV AA4TextV AA15ModifiedContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerI0Rd__lFQO AA0J0V AA7ForEachV AiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenujI0V AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y__________y_____y_____yABSiSg_____ySnySiGSi_____yAB_SiQo_GG______Qo______ySbGGABSgG______yAAyAbFySay_____GSS_____GABG______Qo_SgAAyAbFySay_____GSS_____G_____GSgt 7SwiftUI7SectionV AA4TextV AA15ModifiedContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerI0Rd__lFQO AA0J0V AA7ForEachV AiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenujI0V AA32_EnvironmentKeyTransformModifierV AiAE06buttonI0yQrqd__AA015PrimitiveButtonI0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV AX014STAppExceptionG0V AA05PlainwI0V AX17AboveAgeRatingAppV AX021STPendingAppExceptionG0V AA05EmptyG0V
+ _symbolic _____y_____yAByABy__________G_____y_____SgGG_____G______yAAy______AByAnFy_____GGtGG_____tG 7SwiftUI9TupleViewV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameJ0V AA6VStackV AA4TextV AA0R9AlignmentO AA6SpacerV
+ _symbolic _____y_____y_____ACG_____y_____y_____yAEy_____y_____y_____y___________yAC_____ySi_____y_____G_____GACGAIyAcGyAO_AJySi__________GAsJySbAmNGtGACGAIyAcGyAJySb_____yAEyAEyAEy__________GAYG_____y_____GGGANG_AJySbAqRGAJySbAWyA_GARGtGACGAIyAcGyAJySbAqNG_A11_A11_SgtGACGAIyACA11______GAIyACA15_ACGtGG_Qo______G_Qo______G_Qo_G 7SwiftUI19_ConditionalContentV AA12ProgressViewV AA05EmptyF0V AA0F0PAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V AiAE20listHasStackBehaviorQryFQO AiAE06scrollD10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleF0V 018ScreenTimeSettingsB00D21RestrictionAgeSectionV AZ0dZ7SectionV AZ0dZ4CellV AZ7AppIconV AA03AnyF0V AA5ColorV AZ17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV AZ0Z10ResetAlertV
+ _symbolic _____y_____y_____ACG_____y_____y_____yAEy_____y_____y_____y___________yAC_____ySi_____y_____G_____GACGAIyAcGyAO_AJySi__________GAsJySbAmNGtGACGAIyAcGyAJySb_____yAEyAEyAEy__________GAYG_____y_____GGGANG_AJySbAqRGAJySbAWyA_GARGtGACGAIyAcGyAJySbAqNG_A11_A11_SgtGACGAIyACA11______GAIyACA15_ACGtGG_Qo______G_Qo______G_Qo__G 7SwiftUI19_ConditionalContentV7StorageO AA12ProgressViewV AA05EmptyG0V AA0G0PAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V AkAE20listHasStackBehaviorQryFQO AkAE06scrollD10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleG0V 018ScreenTimeSettingsB00D21RestrictionAgeSectionV A0_0D18RestrictionSectionV A0_0D15RestrictionCellV A0_7AppIconV AA03AnyG0V AA5ColorV A0_17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV A0_21RestrictionResetAlertV
+ _symbolic _____y_____y______ACtGG 7SwiftUI6VStackV AA9TupleViewV AA4TextV
+ _symbolic _____y_____y__________y_____y_____yACSiSg_____ySnySiGSi_____yAC_SiQo_GG______Qo______ySbGGACSgG______yAByAcGySay_____GSS_____GACG______Qo_SgAByAcGySay_____GSS_____G_____GSgtG 7SwiftUI9TupleViewV AA7SectionV AA4TextV AA15ModifiedContentV AA0D0PAAE11pickerStyleyQrqd__AA06PickerJ0Rd__lFQO AA0K0V AA7ForEachV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenukJ0V AA32_EnvironmentKeyTransformModifierV AkAE06buttonJ0yQrqd__AA015PrimitiveButtonJ0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV AZ014STAppExceptionD0V AA05PlainxJ0V AZ17AboveAgeRatingAppV AZ021STPendingAppExceptionD0V AA05EmptyD0V
+ _symbolic _____y_____y_____yAAyAAyAAy__________G_____y_____SgGG_____G______yACy______AAyAoGy_____GGtGG_____tGG_____G 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameK0V AA6VStackV AA4TextV AA0S9AlignmentO AA6SpacerV AA08_PaddingK0V
+ _symbolic _____y_____y_____yAAy_____y_____y_____y___________y__________ySi_____y_____G_____GAFGAEyAfCyAL_AGySi__________GApGySbAjKGtGAFGAEyAfCyAGySb_____yAAyAAyAAy__________GAVG_____y_____GGGAKG_AGySbAnOGAGySbATyAXGAOGtGAFGAEyAfCyAGySbAnKG_A8_A8_SgtGAFGAEyAFA8______GAEyAFA12_AFGtGG_Qo______G_Qo______G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AcAE20listHasStackBehaviorQryFQO AcAE06scrollJ10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleC0V 018ScreenTimeSettingsB00J21RestrictionAgeSectionV AT0jwY0V AA05EmptyC0V AT0jW4CellV AT7AppIconV AA03AnyC0V AA5ColorV AT17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV AT0W10ResetAlertV
+ _symbolic _____y_____y_____yACyACy__________G_____y_____SgGG_____G______yABy______ACyAoGy_____GGtGG_____tGG 7SwiftUI6HStackV AA9TupleViewV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameK0V AA6VStackV AA4TextV AA0S9AlignmentO AA6SpacerV
+ _symbolic _____y_____y_____yACy_____yAByACyACyACy__________G_____y_____SgGG_____G_AAyABy______ACyAoHy_____GGtGG_____tGG_____GAXG_ACy_____AXGACyACyACyACyACy_____yAOGAKGAHy_____SgGG_____GAXGAXGtGG 7SwiftUI6VStackV AA9TupleViewV AA15ModifiedContentV AA6HStackV AA5ImageV AA18_AspectRatioLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA06_FrameL0V AA4TextV AA0S9AlignmentO AA6SpacerV AA08_PaddingL0V AA7DividerV AA6ButtonV AA4FontV AA05_FlexrL0V
+ _symbolic _____y_____y_____y__________y_____y_____yADSiSg_____ySnySiGSi_____yAD_SiQo_GG______Qo______ySbGGADSgG______yACyAdHySay_____GSS_____GADG______Qo_SgACyAdHySay_____GSS_____G_____GSgtGG 7SwiftUI4FormV AA9TupleViewV AA7SectionV AA4TextV AA15ModifiedContentV AA0E0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQO AA0L0V AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenulK0V AA32_EnvironmentKeyTransformModifierV AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV A0_014STAppExceptionE0V AA05PlainyK0V A0_17AboveAgeRatingAppV A0_021STPendingAppExceptionE0V AA05EmptyE0V
+ _symbolic _____y_____y_____y_____xGG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA6VStackV AA19_ConditionalContentV 018ScreenTimeSettingsB012AppIconImage33_F7421E97E89C76E374C87DDE77856B66LLV
+ _symbolic _____y_____y_____y_____y_____AAy_____y_____yAESiSg_____ySnySiGSi_____yAE_SiQo_GG______Qo______ySbGGAESgG______yADyAeHySay_____GSS_____GAEG______Qo_SgADyAeHySay_____GSS_____G_____GSgtGGAPG 7SwiftUI15ModifiedContentV AA4FormV AA9TupleViewV AA7SectionV AA4TextV AA0G0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQO AA0L0V AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenulK0V AA32_EnvironmentKeyTransformModifierV AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV A0_014STAppExceptionG0V AA05PlainyK0V A0_17AboveAgeRatingAppV A0_021STPendingAppExceptionG0V AA05EmptyG0V
+ _type_layout_string 20ScreenTimeSettingsUI16STBannerCellViewV
- -[STCommunicationSafetyListController _authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:]
- -[STCommunicationSafetyListController _authenticateWithPasscodeIfNeededForSpecifier:success:failure:]
- -[STCommunicationSafetyListController parentAuthenticationPrompt]
- -[STCommunicationSafetyListController setParentAuthenticationPrompt:]
- -[STCommunicationSafetyListController showViewController:animated:]
- -[STCommunicationSafetyViewModel isParentSignInRequiredForCommunicationSafetyChange]
- -[STCommunicationSafetyViewModel setIsParentSignInRequiredForCommunicationSafetyChange:]
- -[STCommunicationSafetyViewModel setShouldForceCommunicationSafetyEnabled:]
- -[STCommunicationSafetyViewModel shouldForceCommunicationSafetyEnabled]
- -[STCommunicationSafetyViewModelCoordinator _isParentSignInRequiredForCommunicationSafetyChange]
- -[STCommunicationSafetyViewModelCoordinator _isParentSignInRequiredForCommunicationSafetyChange].cold.1
- -[STCommunicationSafetyViewModelCoordinator _regulatoryRegion]
- -[STCommunicationSafetyViewModelCoordinator _regulatoryRegion].cold.1
- -[STCommunicationSafetyViewModelCoordinator _shouldForceCommunicationSafetyEnabled]
- -[STCommunicationSafetyViewModelCoordinator _shouldForceCommunicationSafetyEnabled].cold.1
- -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:]
- -[STCommunicationSafetyViewModelCoordinator initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:]
- -[STCommunicationSafetyViewModelCoordinator updateRegulatoryValues:]
- -[STConnectToFamilyHelper connectToFamily]
- -[STConnectToFamilyHelper connectToFamily].cold.1
- -[STConnectToFamilyHelper connectToFamily].cold.2
- -[STContentPrivacyAllowedAppsDetailController parentAuthenticationPrompt]
- -[STContentPrivacyAllowedAppsDetailController setParentAuthenticationPrompt:]
- -[STContentPrivacyAllowedAppsDetailController showViewController:animated:]
- -[STContentPrivacyListController parentAuthenticationPrompt]
- -[STContentPrivacyListController setParentAuthenticationPrompt:]
- -[STContentPrivacyListController showViewController:animated:]
- -[STContentPrivacyViewModel isParentSignInRequiredForAllowedAppsChange]
- -[STContentPrivacyViewModel isParentSignInRequiredForTopLevelRestrictionsChange]
- -[STContentPrivacyViewModel isParentSignInRequiredForWebContentFilterChange]
- -[STContentPrivacyViewModel isWebContentFilterForcedToLimitAdultWebsites]
- -[STContentPrivacyViewModel regulatoryRevokeAccessMode]
- -[STContentPrivacyViewModel setIsParentSignInRequiredForAllowedAppsChange:]
- -[STContentPrivacyViewModel setIsParentSignInRequiredForWebContentFilterChange:]
- -[STContentPrivacyViewModel setIsWebContentFilterForcedToLimitAdultWebsites:]
- -[STContentPrivacyViewModel setRegulatoryRevokeAccessMode:]
- -[STContentPrivacyViewModelCoordinator _isParentSignInRequiredForWebContentFilterChange]
- -[STContentPrivacyViewModelCoordinator _isParentSignInRequiredForWebContentFilterChange].cold.1
- -[STContentPrivacyViewModelCoordinator _isWebContentFilterForced]
- -[STContentPrivacyViewModelCoordinator _isWebContentFilterForced].cold.1
- -[STContentPrivacyViewModelCoordinator _regulatoryRegion]
- -[STContentPrivacyViewModelCoordinator _regulatoryRegion].cold.1
- -[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]
- -[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]
- -[STContentPrivacyViewModelCoordinator regulatoryManager]
- -[STContentPrivacyViewModelCoordinator updateRegulatoryValues:]
- -[STWebFilterDetailController parentAuthenticationPrompt]
- -[STWebFilterDetailController setParentAuthenticationPrompt:]
- -[STWebFilterDetailController showViewController:animated:]
- GCC_except_table116
- GCC_except_table192
- GCC_except_table201
- GCC_except_table39
- _OBJC_CLASS_$_STRegulatoryManager
- _OBJC_CLASS_$_STRegulatoryManagerRevokeAccessData
- _OBJC_CLASS_$__TtC20ScreenTimeSettingsUI21STConnectToFamilyCell
- _OBJC_IVAR_$_STCommunicationSafetyListController._parentAuthenticationPrompt
- _OBJC_IVAR_$_STCommunicationSafetyViewModel._isParentSignInRequiredForCommunicationSafetyChange
- _OBJC_IVAR_$_STCommunicationSafetyViewModel._shouldForceCommunicationSafetyEnabled
- _OBJC_IVAR_$_STContentPrivacyAllowedAppsDetailController._parentAuthenticationPrompt
- _OBJC_IVAR_$_STContentPrivacyListController._parentAuthenticationPrompt
- _OBJC_IVAR_$_STContentPrivacyViewModel._isParentSignInRequiredForAllowedAppsChange
- _OBJC_IVAR_$_STContentPrivacyViewModel._isParentSignInRequiredForWebContentFilterChange
- _OBJC_IVAR_$_STContentPrivacyViewModel._isWebContentFilterForcedToLimitAdultWebsites
- _OBJC_IVAR_$_STContentPrivacyViewModel._regulatoryRevokeAccessMode
- _OBJC_IVAR_$_STContentPrivacyViewModelCoordinator._regulatoryManager
- _OBJC_IVAR_$_STWebFilterDetailController._parentAuthenticationPrompt
- _OBJC_METACLASS_$__TtC20ScreenTimeSettingsUI21STConnectToFamilyCell
- __DATA__TtC20ScreenTimeSettingsUI21STConnectToFamilyCell
- __INSTANCE_METHODS__TtC20ScreenTimeSettingsUI21STConnectToFamilyCell
- __METACLASS_DATA__TtC20ScreenTimeSettingsUI21STConnectToFamilyCell
- __OBJC_$_PROP_LIST_STCommunicationSafetyViewModelCoordinator.194
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1014
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AISViewControllerPresentationHandlerProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_STConnectToFamily
- __OBJC_$_PROTOCOL_METHOD_TYPES_AISViewControllerPresentationHandlerProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_STConnectToFamily
- __OBJC_$_PROTOCOL_REFS_AISViewControllerPresentationHandlerProtocol
- __OBJC_$_PROTOCOL_REFS_STConnectToFamily
- __OBJC_$_PROTOCOL_REFS_STParentAuthenticationPromptPresenting
- __OBJC_CLASS_PROTOCOLS_$_STCommunicationSafetyListController
- __OBJC_CLASS_PROTOCOLS_$_STContentPrivacyListController
- __OBJC_CLASS_PROTOCOLS_$_STWebFilterDetailController
- __OBJC_LABEL_PROTOCOL_$_AISViewControllerPresentationHandlerProtocol
- __OBJC_LABEL_PROTOCOL_$_STConnectToFamily
- __OBJC_LABEL_PROTOCOL_$_STParentAuthenticationPromptPresenting
- __OBJC_PROTOCOL_$_AISViewControllerPresentationHandlerProtocol
- __OBJC_PROTOCOL_$_STConnectToFamily
- __OBJC_PROTOCOL_$_STParentAuthenticationPromptPresenting
- ___101-[STCommunicationSafetyListController _authenticateWithPasscodeIfNeededForSpecifier:success:failure:]_block_invoke
- ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.75
- ___101-[STCommunicationSafetyViewModelCoordinator persistCommunicationSafetySettingsWithCompletionHandler:]_block_invoke.76
- ___103-[STContentPrivacyListController _authenticateIfNeededForRestrictionsEnabledSpecifier:completionBlock:]_block_invoke
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.823
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.823.cold.1
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.cold.1
- ___110-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]_block_invoke
- ___110-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:]_block_invoke.cold.1
- ___115-[STCommunicationSafetyListController _authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:]_block_invoke
- ___143-[STCommunicationSafetyViewModelCoordinator saveCommunicationSafetyReceivingRestricted:communicationSafetySendingRestricted:completionHandler:]_block_invoke.78
- ___189-[STContentPrivacyViewModelCoordinator initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:]_block_invoke
- ___42-[STConnectToFamilyHelper connectToFamily]_block_invoke
- ___42-[STConnectToFamilyHelper connectToFamily]_block_invoke.cold.1
- ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.425
- ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.425.cold.1
- ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.497
- ___59-[STCommunicationSafetyViewModelCoordinator _loadViewModel]_block_invoke.72
- ___63-[STContentPrivacyViewModelCoordinator updateRegulatoryValues:]_block_invoke
- ___63-[STContentPrivacyViewModelCoordinator updateRegulatoryValues:]_block_invoke_2
- ___64-[STWebFilterDetailController _authenticateIfNeededThenPerform:]_block_invoke_2
- ___68-[STCommunicationSafetyViewModelCoordinator updateRegulatoryValues:]_block_invoke
- ___68-[STCommunicationSafetyViewModelCoordinator updateRegulatoryValues:]_block_invoke_2
- ___69-[STCommunicationSafetyListController _setEnableAnalytics:specifier:]_block_invoke_2
- ___69-[STRootViewModelCoordinator loadRegionRatingsWithCompletionHandler:]_block_invoke.458
- ___70-[STWebFilterDetailController _createConnectToFamilySpecifierIfNeeded]_block_invoke_2
- ___70-[STWebFilterDetailController _createConnectToFamilySpecifierIfNeeded]_block_invoke_3
- ___74-[STCommunicationSafetyListController _setCheckForUnsafePhotos:specifier:]_block_invoke_2
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke_2
- ___78-[STCommunicationSafetyListController _createConnectToFamilySpecifierIfNeeded]_block_invoke_2
- ___78-[STCommunicationSafetyListController _createConnectToFamilySpecifierIfNeeded]_block_invoke_3
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.432
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.432.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.439
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.439.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.440
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.440.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.443
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.443.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.446
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.446.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.449
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.449.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.452
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.452.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.453
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.833
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.832
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.844
- ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.431
- ___89-[STContentPrivacyAllowedAppsDetailController _tryAuthenticatingThenIfNeededThenPerform:]_block_invoke_2
- ___89-[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke.29
- ___89-[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke.29.cold.1
- ___89-[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke.cold.1
- ___89-[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke_2
- ___89-[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:]_block_invoke_2.30
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.429
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.429.cold.1
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
- ___block_descriptor_48_e8_32bs40bs_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e57_v24?0"STRegulatoryManagerRevokeAccessData"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_62_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_95_e8_32s40s48s56s64s72bs_e60_v28?0B8"STRegulatoryManagerRevokeAccessData"12"NSError"20ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1017
- ___block_literal_global.445
- ___block_literal_global.451
- ___block_literal_global.713
- ___swift_memcpy0_1
- _associated conformance 15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE0deF7UIErrorOSHADSQ
- _block_copy_helper.107
- _block_copy_helper.121
- _block_copy_helper.129
- _block_copy_helper.135
- _block_copy_helper.139
- _block_copy_helper.39
- _block_copy_helper.46
- _block_copy_helper.81
- _block_copy_helper.84
- _block_copy_helper.90
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.109
- _block_descriptor.123
- _block_descriptor.131
- _block_descriptor.137
- _block_descriptor.141
- _block_descriptor.41
- _block_descriptor.48
- _block_descriptor.83
- _block_descriptor.86
- _block_descriptor.92
- _block_destroy_helper.108
- _block_destroy_helper.122
- _block_destroy_helper.130
- _block_destroy_helper.136
- _block_destroy_helper.140
- _block_destroy_helper.40
- _block_destroy_helper.47
- _block_destroy_helper.82
- _block_destroy_helper.85
- _block_destroy_helper.91
- _block_destroy_helper.99
- _dispatch_get_global_queue
- _flat unique So17STConnectToFamily_p
- _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOQr.10
- _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOQr.8
- _get_underlying_witness 7SwiftUI4ViewPAAEAcAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOqd0__AaBHC.11
- _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.9
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4FormVyAA9TupleViewVyAA7SectionVyAA4TextVACyAA0G0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQOyAA0L0VyAKSiSgAA7ForEachVySnySiGSiAmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQOyAK_SiQo_GG_AA04MenulK0VQo_AA32_EnvironmentKeyTransformModifierVySbGGAA05EmptyG0VG_AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQOyAIyAkTySay018ScreenTimeSettingsB012ExceptionAppVGSSA11_014STAppExceptionG0VGAKG_AA05PlainzK0VQo_SgAIyAkTySayA11_17AboveAgeRatingAppVGSSA11_021STPendingAppExceptionG0VGA7_GSgtGGA4_GAaLHPA32_AaLHPyHC_A4_AA0gV0HPyHCHC.66
- _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6HStackVyAA9TupleViewVyACyACyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAA12_FrameLayoutVGAA016_ForegroundStyleL0VyAA09TintShapeQ0VGG_ACyAA6VStackVyAGyAA4TextV_ACyA1_AKyAA0U9AlignmentOGGtGGAA05_FlexnO0VGACyACyApUyAA03AnysQ0VGGARGtGGAA08_PaddingO0VGAA011_BackgroundL0VyAA06StrokesG0VyAA16RoundedRectangleVA12_AA05EmptyG0VGGGAA0G0HPA20_AAA32_HPA17_AAA32_HPyHC_A19_AA0gL0HPyHCHC_A30_AAA33_HPyHCHC.53
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA12ProgressViewVyAA05EmptyF0VAGGAA0F0PAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOyAA08ModifiedD0VyAjAE20listHasStackBehaviorQryFQOyASyAjAE06scrollD10BackgroundyQrAA10VisibilityOFQOyAA4FormVyAA05TupleF0Vy018ScreenTimeSettingsB00D21RestrictionAgeSectionV_A0_0D18RestrictionSectionVyAGA0_0D15RestrictionCellVySiA0_7AppIconVyAA03AnyF0VGAA5ColorVGAGGA4_yAGA_yA14__A6_ySiA0_17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLVAA14LinearGradientVGA21_A6_ySbA11_A13_GtGAGGA4_yAGA_yA6_ySbAA14GeometryReaderVyASyASyASyAA5ImageVAA12_FrameLayoutVGA30_GAA11_ClipEffectVyAA9RectangleVGGGA13_G_A6_ySbA18_A20_GA6_ySbA26_yA32_GA20_GtGAGGA4_yAGA_yA6_ySbA18_A13_G_A46_A46_SgtGAGGA4_yAGA46_AA4TextVGA4_yAGA51_AGGtGG_Qo_AA16_FixedSizeLayoutVG_Qo_A0_21RestrictionResetAlertVG_Qo_GAaIHPAhaIHPyHC_qd__AaIHD2_A64_HOHC.134
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA14GeometryReaderVyAA08ModifiedD0VyAGyAGyAA5ImageVAA12_FrameLayoutVGAKGAA11_ClipEffectVyAA9RectangleVGGGAIGAA4ViewHPAtaVHPyHC_AiaVHPyHCHC.12
- _get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyAA6VStackVyAA012_ConditionalE0Vy018ScreenTimeSettingsB012AppIconImage33_F7421E97E89C76E374C87DDE77856B66LLVxGGAA13_TaskModifierVGAaBHPAnaBHPyHC_ApA0cW0HPyHCHC.8
- _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA0E0PAAE12onTapGesture5count7performQrSi_yyctFQOy018ScreenTimeSettingsB09PickerRow33_02F314FBF7653240FBB92EA68B618E57LLV_Qo__AOtGGAaFHPyHC.46
- _objc_msgSend$_authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:
- _objc_msgSend$_authenticateWithPasscodeIfNeededForSpecifier:success:failure:
- _objc_msgSend$_isParentSignInRequiredForCommunicationSafetyChange
- _objc_msgSend$_isParentSignInRequiredForWebContentFilterChange
- _objc_msgSend$_isWebContentFilterForced
- _objc_msgSend$create
- _objc_msgSend$fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:
- _objc_msgSend$initWithIsRevokeAccessModeEnabled:isParentSignInRequired:
- _objc_msgSend$initWithManagedUserDSID:
- _objc_msgSend$initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
- _objc_msgSend$initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:
- _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:
- _objc_msgSend$initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:
- _objc_msgSend$isCommunicationSafetyForcedToEnabledForPersistenceController:error:
- _objc_msgSend$isParentSignInRequired
- _objc_msgSend$isParentSignInRequiredForAllowedAppsChange
- _objc_msgSend$isParentSignInRequiredForCommunicationSafetyChange
- _objc_msgSend$isParentSignInRequiredForCommunicationSafetyForPersistenceController:error:
- _objc_msgSend$isParentSignInRequiredForTopLevelRestrictionsChange
- _objc_msgSend$isParentSignInRequiredForWebContentFilterChange
- _objc_msgSend$isParentSignInRequiredForWebContentFilterForPersistenceController:error:
- _objc_msgSend$isRevokeAccessModeEnabled
- _objc_msgSend$isWebContentFilterForcedToLimitAdultWebsites
- _objc_msgSend$isWebContentFilterForcedToLimitAdultWebsitesForPersistenceController:error:
- _objc_msgSend$presentFromViewController:completion:
- _objc_msgSend$regionAndReturnError:
- _objc_msgSend$regulatoryManager
- _objc_msgSend$regulatoryRevokeAccessMode
- _objc_msgSend$revokeAccessDataForAccountDSID:persistenceController:completionHandler:
- _objc_msgSend$setIsParentSignInRequiredForAllowedAppsChange:
- _objc_msgSend$setIsParentSignInRequiredForCommunicationSafetyChange:
- _objc_msgSend$setIsParentSignInRequiredForWebContentFilterChange:
- _objc_msgSend$setIsWebContentFilterForcedToLimitAdultWebsites:
- _objc_msgSend$setRegulatoryRevokeAccessMode:
- _objc_msgSend$setShouldForceCommunicationSafetyEnabled:
- _objc_msgSend$shouldForceCommunicationSafetyEnabled
- _objc_msgSend$updateRegulatoryValues:
- _objc_retain_x4
- _objc_retain_x6
- _objectdestroy.2Tm
- _objectdestroy.37Tm
- _swift_getExistentialTypeMetadata
- _symbolic $s15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE0F5StoreP
- _symbolic _____ 15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE016InternalToPublicF5StoreV
- _symbolic _____ 15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE0F0V
- _symbolic _____ 15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE0deF7UIErrorO
- _symbolic _____ 20ScreenTimeSettingsUI21STConnectToFamilyCellC
- _symbolic _____Iegn_ 15ScreenTimeSwift21STExpressIntroductionO0aB10SettingsUIE0F0V
- _symbolic ______p 15ScreenTimeSwift21STExpressIntroductionO15STSettingsStoreP
- _symbolic ______p So17STConnectToFamilyP
- _symbolic _____yAAyAAyAAyAAy__________y_____SgGGACy_____SgGG_____G_____yADGG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleI0V AA11_ClipEffectV AA6CircleV
- _symbolic _____yAAy_____yAAy_____y_____y_____y___________y__________ySi_____y_____G_____GAFGAEyAfCyAL_AGySi__________GApGySbAjKGtGAFGAEyAfCyAGySb_____yAAyAAyAAy__________GAVG_____y_____GGGAKG_AGySbAnOGAGySbATyAXGAOGtGAFGAEyAfCyAGySbAnKG_A8_A8_SgtGAFGAEyAFA8______GAEyAFA12_AFGtGG_Qo______G_Qo______G_____G 7SwiftUI15ModifiedContentV AA4ViewPAAE20listHasStackBehaviorQryFQO AeAE06scrollD10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleE0V 018ScreenTimeSettingsB00D21RestrictionAgeSectionV AN0drT0V AA05EmptyE0V AN0dR4CellV AN7AppIconV AA03AnyE0V AA5ColorV AN17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV AN0R10ResetAlertV AA13_TaskModifierV
- _symbolic _____yAAy_____y_____yAAyAAyAAyAAyAAy__________y_____SgGGAEy_____SgGG_____G_____yAFGG_____y_____GG______yACy______AAyAxEy_____GGtGG_____tGG_____GA5_G 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleL0V AA11_ClipEffectV AA6CircleV AA6VStackV AA4TextV AA0W9AlignmentO AA6SpacerV AA08_PaddingP0V
- _symbolic _____yAAy_____y_____yAAyAAyAAyAAyAAy__________y_____SgGGAEy_____SgGG_____G_____yAFGG_____y_____GG______yACy______AAyAxEy_____GGtGG_____tGG_____GA5_G_AAy_____A5_GAAyAAyAAyAAyAAy_____yAXGAHGALG_____GA5_GA5_Gt 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleL0V AA11_ClipEffectV AA6CircleV AA6VStackV AA4TextV AA0W9AlignmentO AA6SpacerV AA08_PaddingP0V AA7DividerV AA6ButtonV AA05_FlexoP0V
- _symbolic _____y_______________G 7SwiftUI15StrokeShapeViewV AA16RoundedRectangleV AA03AnyD5StyleV AA05EmptyE0V
- _symbolic _____y___________y_____yADy_____yACyADyADyADyADyADy__________y_____SgGGAGy_____SgGG_____G_____yAHGG_____y_____GG______yACy______ADyAzGy_____GGtGG_____tGG_____GA7_G_ADy_____A7_GADyADyADyADyADy_____yAZGAJGANG_____GA7_GA7_GtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA15ModifiedContentV AA6HStackV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA06_FrameG0V AA016_BackgroundStyleP0V AA11_ClipEffectV AA6CircleV AA0F0V AA4TextV AA0Y9AlignmentO AA6SpacerV AA08_PaddingG0V AA7DividerV AA6ButtonV AA05_FlexsG0V
- _symbolic _____y__________y_____y_____yABSiSg_____ySnySiGSi_____yAB_SiQo_GG______Qo______ySbGG_____G 7SwiftUI7SectionV AA4TextV AA15ModifiedContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerI0Rd__lFQO AA0J0V AA7ForEachV AiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenujI0V AA32_EnvironmentKeyTransformModifierV AA05EmptyG0V
- _symbolic _____y__________y_____y_____yABSiSg_____ySnySiGSi_____yAB_SiQo_GG______Qo______ySbGG_____G______yAAyAbFySay_____GSS_____GABG______Qo_SgAAyAbFySay_____GSS_____GAPGSgt 7SwiftUI7SectionV AA4TextV AA15ModifiedContentV AA4ViewPAAE11pickerStyleyQrqd__AA06PickerI0Rd__lFQO AA0J0V AA7ForEachV AiAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenujI0V AA32_EnvironmentKeyTransformModifierV AA05EmptyG0V AiAE06buttonI0yQrqd__AA015PrimitiveButtonI0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV AZ014STAppExceptionG0V AA05PlainxI0V AZ17AboveAgeRatingAppV AZ021STPendingAppExceptionG0V
- _symbolic _____y_____yAByAByAByABy__________y_____SgGGADy_____SgGG_____G_____yAEGG_____y_____GG______yAAy______AByAwDy_____GGtGG_____tG 7SwiftUI9TupleViewV AA15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleK0V AA11_ClipEffectV AA6CircleV AA6VStackV AA4TextV AA0V9AlignmentO AA6SpacerV
- _symbolic _____y_____y_____ACG_____y_____y_____yAEy_____y_____y_____y___________yAC_____ySi_____y_____G_____GACGAIyAcGyAO_AJySi__________GAsJySbAmNGtGACGAIyAcGyAJySb_____yAEyAEyAEy__________GAYG_____y_____GGGANG_AJySbAqRGAJySbAWyA_GARGtGACGAIyAcGyAJySbAqNG_A11_A11_SgtGACGAIyACA11______GAIyACA15_ACGtGG_Qo______G_Qo______G_Qo_G 7SwiftUI19_ConditionalContentV AA12ProgressViewV AA05EmptyF0V AA0F0PAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V AiAE20listHasStackBehaviorQryFQO AiAE06scrollD10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleF0V 018ScreenTimeSettingsB00D21RestrictionAgeSectionV A_0D18RestrictionSectionV A_0D15RestrictionCellV A_7AppIconV AA03AnyF0V AA5ColorV A_17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV A_21RestrictionResetAlertV
- _symbolic _____y_____y_____ACG_____y_____y_____yAEy_____y_____y_____y___________yAC_____ySi_____y_____G_____GACGAIyAcGyAO_AJySi__________GAsJySbAmNGtGACGAIyAcGyAJySb_____yAEyAEyAEy__________GAYG_____y_____GGGANG_AJySbAqRGAJySbAWyA_GARGtGACGAIyAcGyAJySbAqNG_A11_A11_SgtGACGAIyACA11______GAIyACA15_ACGtGG_Qo______G_Qo______G_Qo__G 7SwiftUI19_ConditionalContentV7StorageO AA12ProgressViewV AA05EmptyG0V AA0G0PAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQO AA08ModifiedD0V AkAE20listHasStackBehaviorQryFQO AkAE06scrollD10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleG0V 018ScreenTimeSettingsB00D21RestrictionAgeSectionV A1_0D18RestrictionSectionV A1_0D15RestrictionCellV A1_7AppIconV AA03AnyG0V AA5ColorV A1_17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV A1_21RestrictionResetAlertV
- _symbolic _____y_____y__________y_____y_____yACSiSg_____ySnySiGSi_____yAC_SiQo_GG______Qo______ySbGG_____G______yAByAcGySay_____GSS_____GACG______Qo_SgAByAcGySay_____GSS_____GAQGSgtG 7SwiftUI9TupleViewV AA7SectionV AA4TextV AA15ModifiedContentV AA0D0PAAE11pickerStyleyQrqd__AA06PickerJ0Rd__lFQO AA0K0V AA7ForEachV AkAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenukJ0V AA32_EnvironmentKeyTransformModifierV AA05EmptyD0V AkAE06buttonJ0yQrqd__AA015PrimitiveButtonJ0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV A0_014STAppExceptionD0V AA05PlainyJ0V A0_17AboveAgeRatingAppV A0_021STPendingAppExceptionD0V
- _symbolic _____y_____y_____yAAy_____y_____y_____y___________y__________ySi_____y_____G_____GAFGAEyAfCyAL_AGySi__________GApGySbAjKGtGAFGAEyAfCyAGySb_____yAAyAAyAAy__________GAVG_____y_____GGGAKG_AGySbAnOGAGySbATyAXGAOGtGAFGAEyAfCyAGySbAnKG_A8_A8_SgtGAFGAEyAFA8______GAEyAFA12_AFGtGG_Qo______G_Qo______G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AcAE20listHasStackBehaviorQryFQO AcAE06scrollK10BackgroundyQrAA10VisibilityOFQO AA4FormV AA05TupleC0V 018ScreenTimeSettingsB00K21RestrictionAgeSectionV AU0kxZ0V AA05EmptyC0V AU0kX4CellV AU7AppIconV AA03AnyC0V AA5ColorV AU17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV AA14LinearGradientV AA14GeometryReaderV AA5ImageV AA12_FrameLayoutV AA11_ClipEffectV AA9RectangleV AA4TextV AA16_FixedSizeLayoutV AU0X10ResetAlertV
- _symbolic _____y_____y_____yACy_____yAByACyACyACyACyACy__________y_____SgGGAFy_____SgGG_____G_____yAGGG_____y_____GG_AAyABy______ACyAxFy_____GGtGG_____tGG_____GA5_G_ACy_____A5_GACyACyACyACyACy_____yAXGAIGAMG_____GA5_GA5_GtGG 7SwiftUI6VStackV AA9TupleViewV AA15ModifiedContentV AA6HStackV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleM0V AA11_ClipEffectV AA6CircleV AA4TextV AA0W9AlignmentO AA6SpacerV AA08_PaddingQ0V AA7DividerV AA6ButtonV AA05_FlexpQ0V
- _symbolic _____y_____y_____y__________y_____y_____yADSiSg_____ySnySiGSi_____yAD_SiQo_GG______Qo______ySbGG_____G______yACyAdHySay_____GSS_____GADG______Qo_SgACyAdHySay_____GSS_____GARGSgtGG 7SwiftUI4FormV AA9TupleViewV AA7SectionV AA4TextV AA15ModifiedContentV AA0E0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQO AA0L0V AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenulK0V AA32_EnvironmentKeyTransformModifierV AA05EmptyE0V AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV A2_014STAppExceptionE0V AA05PlainzK0V A2_17AboveAgeRatingAppV A2_021STPendingAppExceptionE0V
- _symbolic _____y_____y_____y_____xGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA012_ConditionalD0V 018ScreenTimeSettingsB012AppIconImage33_F7421E97E89C76E374C87DDE77856B66LLV AA13_TaskModifierV
- _symbolic _____y_____y_____y_____yADy_____yACyADyADyADyADyADy__________y_____SgGGAGy_____SgGG_____G_____yAHGG_____y_____GG_AByACy______ADyAyGy_____GGtGG_____tGG_____GA6_G_ADy_____A6_GADyADyADyADyADy_____yAYGAJGANG_____GA6_GA6_GtGG_____G 7SwiftUI22UIHostingConfigurationV AA6VStackV AA9TupleViewV AA15ModifiedContentV AA6HStackV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4FontV AA12_FrameLayoutV AA016_BackgroundStyleO0V AA11_ClipEffectV AA6CircleV AA4TextV AA0Y9AlignmentO AA6SpacerV AA08_PaddingS0V AA7DividerV AA6ButtonV AA05_FlexrS0V AA05EmptyG0V
- _symbolic _____y_____y_____y_____y_____AAy_____y_____yAESiSg_____ySnySiGSi_____yAE_SiQo_GG______Qo______ySbGG_____G______yADyAeHySay_____GSS_____GAEG______Qo_SgADyAeHySay_____GSS_____GARGSgtGGAPG 7SwiftUI15ModifiedContentV AA4FormV AA9TupleViewV AA7SectionV AA4TextV AA0G0PAAE11pickerStyleyQrqd__AA06PickerK0Rd__lFQO AA0L0V AA7ForEachV AmAE3tag_15includeOptionalQrqd___SbtSHRd__lFQO AA04MenulK0V AA32_EnvironmentKeyTransformModifierV AA05EmptyG0V AmAE06buttonK0yQrqd__AA015PrimitiveButtonK0Rd__lFQO 018ScreenTimeSettingsB012ExceptionAppV A2_014STAppExceptionG0V AA05PlainzK0V A2_17AboveAgeRatingAppV A2_021STPendingAppExceptionG0V
CStrings:
+ "@\"<STRegulatoryUIPolicyProviding>\""
+ "@\"STAuthenticationCoordinator\""
+ "@\"STRegulatoryCommSafetyPolicy\""
+ "@\"STRegulatoryPolicy\""
+ "@\"STRegulatoryPolicy\"16@0:8"
+ "@\"STRegulatoryUIPolicyProvider\""
+ "@\"STRegulatoryWebContentFilterPolicy\""
+ "@44@0:8@16@24B32@36"
+ "@52@0:8@16@24B32@36@?44"
+ "@60@0:8@16@24@32B40@44@?52"
+ "@64@0:8@16@24q32@40@48@56"
+ "@68@0:8@16@24@32@40B48@52@?60"
+ "AISAgeAssuranceContext"
+ "AISAgeAssuranceFlowPresenter"
+ "AISAgeAssuranceFlowPresenterDelegate"
+ "Age Rating footer explaining why rating is not editable"
+ "Age assurance flow did not provide a view controller"
+ "AgeRatingDisabledFooterText"
+ "Allowed Apps shows full list:%d"
+ "Apps rating is forced to Don't Allow"
+ "At least one of expected parameters missing:\nTitle:%@\nSubtitle:%@\nButtonTitle:%@\nActionHandler:%@"
+ "Class getAISAgeAssuranceContextClass(void)_block_invoke"
+ "Class getAISAgeAssuranceFlowPresenterClass(void)_block_invoke"
+ "CommunicationSafetyEnabledGuardianVerificationReason"
+ "ContentPrivacyViewModelCoordinator loaded view model for regulatory policy update"
+ "Could not get a bundle record for %{public}@"
+ "Could not get a bundle record for %{public}@ with error %{public}@"
+ "EligibleForDataAccess"
+ "Factory"
+ "Failure checking data access eligibility: %{public}d"
+ "Regulatory_AdultVerificationRequiredFooterText"
+ "Regulatory_ConnectToFamilyBannerButtonTitle"
+ "Regulatory_ConnectToFamilySubtitle"
+ "Request for data access authorization failed: %{public}@"
+ "STAccessListDataAccessSubtitle"
+ "STAdultVerificationPrompt"
+ "STAdultVerificationPrompt - age assurance completed with error:%@"
+ "STAdultVerificationPrompt - age assurance completed with result:%@"
+ "STAdultVerificationPrompt - beginAgeAssurance completed with no view controller"
+ "STAdultVerificationPrompt - dismissed presented age assurance controller"
+ "STAdultVerificationPrompt - found result override: %@"
+ "STAdultVerificationPrompt - presenting adult verification viewController"
+ "STAdultVerificationPrompt - starting adult verification flow"
+ "STAdultVerificationPrompt - verify adult flow presented"
+ "STAdultVerificationPrompt.m"
+ "STAuthenticationContext"
+ "STAuthenticationCoordinator"
+ "STAuthenticationCoordinator - Invalid index:%{public}@"
+ "STAuthenticationCoordinator - Prompt type not found:%{public}@"
+ "STAuthenticationCoordinator - prompt index:%{public}@ promptsCount:%{public}@"
+ "STAuthenticationPINPrompt"
+ "STAuthenticationParentSignInPrompt"
+ "STAuthenticationPrompt"
+ "STBannerActionHandler"
+ "STBannerCell"
+ "STBannerCellSpecifier"
+ "STCommunicationSafetyListControllerRegulatoryObservationContext"
+ "STConnectToFamilyPrompt"
+ "STRegulatoryUIPolicyObserving"
+ "STRegulatoryUIPolicyProvider"
+ "STRegulatoryUIPolicyProviding"
+ "STRootViewModelCoordinator finished loading regulatory policy: %{public}@"
+ "STVerifyAdultActionHandlerResultForceSuccess"
+ "STVerifyAdultPromptError"
+ "ScreenTimeSettingsUI.STRegulatoryUIPolicyContext"
+ "ScreenTimeSettingsUI/AppIcon.swift"
+ "ScreenTimeSettingsUI_Private.STRegulatoryUIPolicyProvider"
+ "T@\"<STRegulatoryUIPolicyProviding>\",R,N,V_regulatoryUIPolicyProvider"
+ "T@\"NSArray\",C,N,V_allowedAppsValueChangePrompts"
+ "T@\"NSArray\",C,N,V_topLevelRestrictionsValueChangePrompts"
+ "T@\"NSDictionary\",C,V_promptByType"
+ "T@\"NSString\",C,N,V_guardianSignInReason"
+ "T@\"PSListController\",&,N,V_presentingController"
+ "T@\"PSListController\",W,N,V_listController"
+ "T@\"STAuthenticationCoordinator\",&,N,V_authenticationCoordinator"
+ "T@\"STRegulatoryCommSafetyPolicy\",&,N,V_regulatoryCommSafetyPolicy"
+ "T@\"STRegulatoryPolicy\",N,&,Vpolicy"
+ "T@\"STRegulatoryUIPolicyProvider\",&,N,V_regulatoryUIPolicyProvider"
+ "T@\"STRegulatoryWebContentFilterPolicy\",&,N,V_regulatoryWebContentFilterPolicy"
+ "T@,N,&,Vobservers"
+ "TB,N,V_allowedAppsShowsFullList"
+ "TB,N,V_appsRatingEditable"
+ "TB,N,V_appsRatingForcedToDoNotAllow"
+ "TB,N,VisLocalDevice"
+ "Ti,V_eligibilityChangedNotificationToken"
+ "WebContentAutoFilterLimitedGuardianVerificationReason"
+ "WebFilterViewModelChangeContext"
+ "_TtC20ScreenTimeSettingsUI26STRegulatoryUIPolicyLoader"
+ "_TtC20ScreenTimeSettingsUI27STRegulatoryUIPolicyContext"
+ "_allowedAppsShowsFullList"
+ "_allowedAppsValueChangePrompts"
+ "_appsRatingEditable"
+ "_appsRatingForcedToDoNotAllow"
+ "_authenticateWithContext:prompts:promptIndex:completion:"
+ "_authenticationContext"
+ "_authenticationCoordinator"
+ "_callCompletionWithOverrideIfSetForSuccess:error:"
+ "_createAdditionalFooterIfNeeded"
+ "_eligibilityChangedNotificationToken"
+ "_guardianSignInReason"
+ "_isEligibleOrApprovedForDataAccess:"
+ "_performFamilyControlsChange:forSpecifier:"
+ "_presentingController"
+ "_promptByType"
+ "_regulatoryCommSafetyPolicy"
+ "_regulatoryContext"
+ "_regulatoryUIPolicyProvider"
+ "_regulatoryWebContentFilterPolicy"
+ "_topLevelRestrictionsValueChangePrompts"
+ "_updateDataAccessLevelForSpecifier:usingRecord:"
+ "accountType"
+ "addObserver:"
+ "ageAssuranceDidFinishWithResult:viewControllersToRemove:error:"
+ "allowedApps"
+ "allowedAppsShowsFullList"
+ "allowedAppsShowsFullList is off but access revoked. Adding row for:%@"
+ "allowedAppsValueChangePrompts"
+ "appsRatingForcedToDoNotAllow"
+ "authenticateWithContext:promptTypes:completion:"
+ "authenticationCoordinator"
+ "banner-action-handler"
+ "banner-button-title"
+ "bannerCellWithIdentifier:title:subtitle:buttonTitle:actionHandler:"
+ "beginAgeAssuranceWithContext:completion:"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "com.apple.developer.family-controls-data"
+ "com.apple.os-eligibility-domain.change.radium"
+ "commSafety"
+ "communicationSafetyCoordinator.viewModel.regulatoryCommSafetyPolicy"
+ "configurationLoader"
+ "connectToFamilyBanner"
+ "connectToFamilyBannerDescription"
+ "createWithPresentingListViewController:"
+ "currentPolicy"
+ "editable"
+ "eligibilityChangedNotificationToken"
+ "entitlements"
+ "fallbackPolicyCalculator"
+ "fallbackPolicyWithContext:"
+ "figure.child.shield.fill"
+ "footerInfo"
+ "forcedToEnabled"
+ "forcedToLimitAdultWebsites"
+ "guardianSignInReason"
+ "handlePromptAction"
+ "hasScreenTimePasscode"
+ "initWithAgeAssuranceContext:"
+ "initWithDSID:guardianSignInReason:regulatoryRegion:presentingController:"
+ "initWithFlowType:verificationType:"
+ "initWithInitialPolicy:"
+ "initWithIsLocalUser:userDSID:accountType:isInFamily:isManaged:hasScreenTimePasscode:"
+ "initWithListController:"
+ "initWithManagedUserDSID:isLocalDevice:"
+ "initWithPersistenceController:organizationSettingsRestrictionUtility:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:"
+ "initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:"
+ "initWithPersistenceController:userDSID:currentAccountIsProto:regulatoryUIPolicyProvider:modelUpdatedHandler:"
+ "initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:"
+ "initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:"
+ "initWithPromptByType:"
+ "isInFamily"
+ "loadPolicyWithContext:completion:"
+ "localizedMessage"
+ "objectForKey:ofClass:"
+ "observers"
+ "policy"
+ "policyCalculator"
+ "presentFromViewController:signInReason:completion:"
+ "presentingController"
+ "promptByType"
+ "rating.apps"
+ "ratingSectionFooterText"
+ "regulatoryCommSafetyPolicy"
+ "regulatoryRegionAACID"
+ "regulatoryRestrictions"
+ "regulatoryUIPolicyProvider"
+ "regulatoryUIPolicyProviderDidUpdate:"
+ "regulatoryWebContentFilterPolicy"
+ "reloadSummaryGraph"
+ "requestDataAccessAuthorizationForRecordIdentifier:completionHandler:"
+ "setAllowedAppsShowsFullList:"
+ "setAllowedAppsValueChangePrompts:"
+ "setAppsRatingEditable:"
+ "setAppsRatingForcedToDoNotAllow:"
+ "setAuthenticationCoordinator:"
+ "setEligibilityChangedNotificationToken:"
+ "setGuardianSignInReason:"
+ "setListController:"
+ "setObservers:"
+ "setPolicy:"
+ "setPresentingController:"
+ "setPromptByType:"
+ "setRegulatoryCommSafetyPolicy:"
+ "setRegulatoryUIPolicyProvider:"
+ "setRegulatoryWebContentFilterPolicy:"
+ "setTopLevelRestrictionsValueChangePrompts:"
+ "showMessage"
+ "showsFullList"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI"
+ "st_getUserAgeRange:forAccountWithAltDSID:error:"
+ "startRefreshRegulatoryPolicy"
+ "topLevelRestrictionsValueChangePrompts"
+ "updatePolicy:"
+ "v16@?0@\"STRegulatoryPolicy\"8"
+ "v16@?0@\"UIViewController\"8"
+ "v24@0:8@\"<STRegulatoryUIPolicyObserving>\"16"
+ "v24@0:8@\"<STRegulatoryUIPolicyProviding>\"16"
+ "v32@0:8@\"STAuthenticationContext\"16@?<v@?B>24"
+ "v40@0:8@\"AISAgeAssuranceResult\"16@\"NSArray\"24@\"NSError\"32"
+ "v48@0:8@16@24Q32@?40"
+ "valueChangePrompts"
+ "viewModel.regulatoryWebContentFilterPolicy"
+ "void *AppleIDSetupLibrary(void)"
+ "void *AppleIDSetupUILibrary(void)"
+ "weakObjectsHashTable"
+ "webContentFilter"
- "@\"<STRegulatoryManagerProtocol>\""
- "@44@0:8@16@24B32@?36"
- "@68@0:8@16@24@32@40@48B56@?60"
- "AISViewControllerPresentationHandlerProtocol"
- "At least one of expected parameters missing:\nTitle:%@\nSubtitle:%@\nButtonTitle:%@\nConnectToFamilyHelper:%@"
- "Communication Safety forced to enabled: %{public}d for user %@"
- "CommunicationSafetyEnabledConnectToFamilyButtonTitle"
- "CommunicationSafetyEnabledConnectToFamilySubtitle"
- "CommunicationSafetyEnabledConnectToFamilySubtitle_%@"
- "Error checking if web content filter is forced for user %@: %{public}@ ; assuming forced"
- "Error determining if parent sign-in is required for web content filter for user %@: %{public}@ ; assuming required"
- "Failed to determine if Communication Safety is forced for user %@: %{public}@ ; assuming forced"
- "Failed to determine if parent sign-in is required for Communication Safety for user %@: %{public}@ ; assuming required"
- "Failed to determine regulatory region. Error: %{public}@"
- "Failed to fetch revoke access data for account %@: %{public}@. Assuming not revoke access mode and parent sign-in not required."
- "Fetched revoke access data for account %@: isRevokeAccessModeEnabled=%d, isParentSignInRequired=%d"
- "Loaded for user %{private}s settings: %{private}s"
- "Loading for user %{private}s with defaults %{public}s"
- "Parent sign-in required for Communication Safety change: %{public}d for user %@"
- "Parent sign-in required for Web Content Filter change: %{public}d for user %@"
- "Revoke access mode status:%d"
- "STConnectToFamily"
- "STConnectToFamilyCell"
- "STParentAuthenticationPromptPresenting"
- "Saved for user %{private}s defaults %{public}s"
- "Saved for user %{private}s settings %{private}s"
- "Saving for user %{private}s defaults %{public}s"
- "Saving for user %{private}s settings %{private}s"
- "ScreenTimeSettingsUI.STConnectToFamilyCell"
- "T@\"<STRegulatoryManagerProtocol>\",R,N,V_regulatoryManager"
- "TB,N,V_isParentSignInRequiredForAllowedAppsChange"
- "TB,N,V_isParentSignInRequiredForCommunicationSafetyChange"
- "TB,N,V_isParentSignInRequiredForWebContentFilterChange"
- "TB,N,V_isWebContentFilterForcedToLimitAdultWebsites"
- "TB,N,V_regulatoryRevokeAccessMode"
- "TB,N,V_shouldForceCommunicationSafetyEnabled"
- "Web Content Filter forced to Limit Adult Websites: %{public}d for user %@"
- "WebContentFilterEnabledConnectToFamilySubtitle"
- "WebContentFilterEnabledConnectToFamilySubtitle_%@"
- "WebContentFilterEnabledConnectToFamilyToFamilyButtonTitle"
- "_TtC20ScreenTimeSettingsUI21STConnectToFamilyCell"
- "_authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:"
- "_authenticateWithPasscodeIfNeededForSpecifier:success:failure:"
- "_isParentSignInRequiredForAllowedAppsChange"
- "_isParentSignInRequiredForCommunicationSafetyChange"
- "_isParentSignInRequiredForWebContentFilterChange"
- "_isWebContentFilterForced"
- "_isWebContentFilterForcedToLimitAdultWebsites"
- "_regulatoryManager"
- "_regulatoryRevokeAccessMode"
- "connectToFamily"
- "create"
- "expressIntroductionUISettingsStore"
- "fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:"
- "initWithIsRevokeAccessModeEnabled:isParentSignInRequired:"
- "initWithManagedUserDSID:"
- "initWithPersistenceController:organizationSettingsRestrictionUtility:regulatoryManager:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"
- "initWithPersistenceController:userDSID:currentAccountIsProto:modelUpdatedHandler:"
- "initWithPersistenceController:userDSID:userName:currentAccountIsProto:"
- "initWithPersistenceController:userDSID:userName:currentAccountIsProto:loadCompletionHandler:"
- "isCommunicationSafetyForcedToEnabledForPersistenceController:error:"
- "isParentSignInRequired"
- "isParentSignInRequiredForAllowedAppsChange"
- "isParentSignInRequiredForCommunicationSafetyChange"
- "isParentSignInRequiredForCommunicationSafetyForPersistenceController:error:"
- "isParentSignInRequiredForTopLevelRestrictionsChange"
- "isParentSignInRequiredForWebContentFilterChange"
- "isParentSignInRequiredForWebContentFilterForPersistenceController:error:"
- "isRevokeAccessModeEnabled"
- "isWebContentFilterForcedToLimitAdultWebsites"
- "isWebContentFilterForcedToLimitAdultWebsitesForPersistenceController:error:"
- "presentFromViewController:completion:"
- "prompt-button-title"
- "prompt-subtitle"
- "prompt-title"
- "regionAndReturnError:"
- "regulatoryManager"
- "regulatoryRevokeAccessMode"
- "revokeAccessData: isRevokeAccessModeEnabled=%d, isParentSignInRequired=%d"
- "revokeAccessDataForAccountDSID:persistenceController:completionHandler:"
- "revokeAccessMode is off but access revoked. Adding row for:%@"
- "setIsParentSignInRequiredForAllowedAppsChange:"
- "setIsParentSignInRequiredForCommunicationSafetyChange:"
- "setIsParentSignInRequiredForWebContentFilterChange:"
- "setIsWebContentFilterForcedToLimitAdultWebsites:"
- "setRegulatoryRevokeAccessMode:"
- "setShouldForceCommunicationSafetyEnabled:"
- "shouldForceCommunicationSafetyEnabled"
- "showViewController:animated:"
- "updateRegulatoryValues:"
- "v24@?0@\"STRegulatoryManagerRevokeAccessData\"8@\"NSError\"16"
- "v28@?0B8@\"STRegulatoryManagerRevokeAccessData\"12@\"NSError\"20"
- "v40@0:8@16@?24@?32"

```
