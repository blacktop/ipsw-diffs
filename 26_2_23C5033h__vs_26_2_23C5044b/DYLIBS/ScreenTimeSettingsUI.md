## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.2.5.0.0
-  __TEXT.__text: 0x1236a0
-  __TEXT.__auth_stubs: 0x2ed0
-  __TEXT.__objc_methlist: 0xc054
-  __TEXT.__const: 0x3c94
-  __TEXT.__cstring: 0xe719
-  __TEXT.__oslogstring: 0x5763
-  __TEXT.__gcc_except_tab: 0x1184
+605.2.7.0.0
+  __TEXT.__text: 0x124140
+  __TEXT.__auth_stubs: 0x2ec0
+  __TEXT.__objc_methlist: 0xc0cc
+  __TEXT.__const: 0x3ca4
+  __TEXT.__cstring: 0xe769
+  __TEXT.__oslogstring: 0x5a53
+  __TEXT.__gcc_except_tab: 0x11fc
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x4394
   __TEXT.__constg_swiftt: 0x1504

   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0x90
-  __TEXT.__unwind_info: 0x3b30
+  __TEXT.__unwind_info: 0x3b58
   __TEXT.__eh_frame: 0x20a8
   __TEXT.__objc_classname: 0x1ddd
-  __TEXT.__objc_methname: 0x22088
-  __TEXT.__objc_methtype: 0x3a1b
-  __TEXT.__objc_stubs: 0x14fa0
-  __DATA_CONST.__got: 0x1408
-  __DATA_CONST.__const: 0x24c8
+  __TEXT.__objc_methname: 0x22397
+  __TEXT.__objc_methtype: 0x3a1e
+  __TEXT.__objc_stubs: 0x15140
+  __DATA_CONST.__got: 0x1418
+  __DATA_CONST.__const: 0x2518
   __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b30
+  __DATA_CONST.__objc_selrefs: 0x6ba8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x2d8
-  __AUTH_CONST.__auth_got: 0x1778
+  __AUTH_CONST.__auth_got: 0x1770
   __AUTH_CONST.__const: 0x31e8
-  __AUTH_CONST.__cfstring: 0xaec0
-  __AUTH_CONST.__objc_const: 0x25338
+  __AUTH_CONST.__cfstring: 0xaee0
+  __AUTH_CONST.__objc_const: 0x25768
   __AUTH_CONST.__objc_intobj: 0x840
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH.__objc_data: 0x4d88
   __AUTH.__data: 0xa30
-  __DATA.__objc_ivar: 0xcb4
+  __DATA.__objc_ivar: 0xcc0
   __DATA.__data: 0x2698
   __DATA.__bss: 0x1e18
   __DATA.__common: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B729078-44F2-3D85-9DBE-1D169A2172E8
-  Functions: 6130
-  Symbols:   16172
-  CStrings:  9168
+  UUID: F6C180C8-8F68-3CBC-8100-91AD00EEDEB7
+  Functions: 6146
+  Symbols:   16231
+  CStrings:  9196
 
Symbols:
+ +[STConnectToFamilyHelper connectToFamilySpecifierForUserDSID:regionAACID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:]
+ -[STCommunicationSafetyListController _authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:]
+ -[STCommunicationSafetyListController _authenticateWithPasscodeIfNeededForSpecifier:success:failure:]
+ -[STConnectToFamilyHelper connectToFamily].cold.1
+ -[STConnectToFamilyHelper connectToFamily].cold.2
+ -[STConnectToFamilyHelper initWithPresentingViewController:dsid:regionAACID:completion:]
+ -[STConnectToFamilyHelper regionAACID]
+ -[STConnectToFamilyHelper setRegionAACID:]
+ -[STContentPrivacyAllowedAppsDetailController _tryAuthenticatingThenIfNeededThenPerform:]
+ -[STContentPrivacyListController _authenticateIfNeededForRestrictionsEnabledSpecifier:completionBlock:]
+ -[STContentPrivacyListController parentAuthenticationPrompt]
+ -[STContentPrivacyListController setParentAuthenticationPrompt:]
+ -[STContentPrivacyListController showViewController:animated:]
+ -[STContentPrivacyViewModel isParentSignInRequiredForAllowedAppsChange]
+ -[STContentPrivacyViewModel isParentSignInRequiredForTopLevelRestrictionsChange]
+ -[STContentPrivacyViewModel setIsParentSignInRequiredForAllowedAppsChange:]
+ -[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]
+ GCC_except_table116
+ _OBJC_CLASS_$_AKAuthenticatableResource
+ _OBJC_CLASS_$_STRegulatoryManagerRevokeAccessData
+ _OBJC_IVAR_$_STConnectToFamilyHelper._regionAACID
+ _OBJC_IVAR_$_STContentPrivacyListController._parentAuthenticationPrompt
+ _OBJC_IVAR_$_STContentPrivacyViewModel._isParentSignInRequiredForAllowedAppsChange
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1014
+ __OBJC_CLASS_PROTOCOLS_$_STContentPrivacyListController
+ ___101-[STCommunicationSafetyListController _authenticateWithPasscodeIfNeededForSpecifier:success:failure:]_block_invoke
+ ___103-[STContentPrivacyListController _authenticateIfNeededForRestrictionsEnabledSpecifier:completionBlock:]_block_invoke
+ ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke
+ ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.823
+ ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.823.cold.1
+ ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:]_block_invoke.cold.1
+ ___115-[STCommunicationSafetyListController _authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:]_block_invoke
+ ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.316
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke_2
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.833
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.832
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.844
+ ___89-[STContentPrivacyAllowedAppsDetailController _tryAuthenticatingThenIfNeededThenPerform:]_block_invoke
+ ___89-[STContentPrivacyAllowedAppsDetailController _tryAuthenticatingThenIfNeededThenPerform:]_block_invoke_2
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e57_v24?0"STRegulatoryManagerRevokeAccessData"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_95_e8_32s40s48s56s64s72bs_e60_v28?0B8"STRegulatoryManagerRevokeAccessData"12"NSError"20ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1017
+ _objc_msgSend$_authenticateIfNeededForRestrictionsEnabledSpecifier:completionBlock:
+ _objc_msgSend$_authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:
+ _objc_msgSend$_authenticateWithPasscodeIfNeededForSpecifier:success:failure:
+ _objc_msgSend$_tryAuthenticatingThenIfNeededThenPerform:
+ _objc_msgSend$authenticatableResource
+ _objc_msgSend$connectToFamilySpecifierForUserDSID:regionAACID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:
+ _objc_msgSend$fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:
+ _objc_msgSend$initWithIsRevokeAccessModeEnabled:isParentSignInRequired:
+ _objc_msgSend$initWithPresentingViewController:dsid:regionAACID:completion:
+ _objc_msgSend$isParentSignInRequired
+ _objc_msgSend$isParentSignInRequiredForAllowedAppsChange
+ _objc_msgSend$isParentSignInRequiredForCommunicationSafetyForPersistenceController:error:
+ _objc_msgSend$isParentSignInRequiredForTopLevelRestrictionsChange
+ _objc_msgSend$isParentSignInRequiredForWebContentFilterForPersistenceController:error:
+ _objc_msgSend$isRevokeAccessModeEnabled
+ _objc_msgSend$regionAACID
+ _objc_msgSend$revokeAccessDataForAccountDSID:persistenceController:completionHandler:
+ _objc_msgSend$setAuthenticatableResource:
+ _objc_msgSend$setIsParentSignInRequiredForAllowedAppsChange:
+ _objc_msgSend$setValue:forKey:
- +[STConnectToFamilyHelper connectToFamilySpecifierForUserDSID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:]
- -[STCommunicationSafetyListController _authenticateIfNeededForSpecifier:success:failure:]
- -[STConnectToFamilyHelper initWithPresentingViewController:dsid:completion:]
- -[STContentPrivacyAllowedAppsDetailController _authenticateIfNeededThenPerform:]
- -[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:]
- GCC_except_table102
- GCC_except_table113
- GCC_except_table36
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1007
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:]_block_invoke
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:]_block_invoke.817
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:]_block_invoke.817.cold.1
- ___109-[STContentPrivacyViewModelCoordinator fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:]_block_invoke.cold.1
- ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.315
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.813
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.813.cold.1
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.814
- ___80-[STContentPrivacyAllowedAppsDetailController _authenticateIfNeededThenPerform:]_block_invoke
- ___80-[STContentPrivacyAllowedAppsDetailController _authenticateIfNeededThenPerform:]_block_invoke_2
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.826
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.825
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.837
- ___89-[STCommunicationSafetyListController _authenticateIfNeededForSpecifier:success:failure:]_block_invoke
- ___89-[STCommunicationSafetyListController _authenticateIfNeededForSpecifier:success:failure:]_block_invoke_2
- ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
- ___block_descriptor_57_e8_32s40bs48r_e30_v24?0"NSNumber"8"NSError"16lr48l8s40l8s32l8
- ___block_descriptor_95_e8_32s40s48s56s64s72bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1010
- _objc_msgSend$_authenticateIfNeededForSpecifier:success:failure:
- _objc_msgSend$connectToFamilySpecifierForUserDSID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:
- _objc_msgSend$fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:
- _objc_msgSend$initWithPresentingViewController:dsid:completion:
- _objc_msgSend$isCommunicationSafetyRegulatedForLocalUserAndReturnError:
- _objc_msgSend$isRevokeAccessModeEnabledForAccountDSID:completionHandler:
- _objc_msgSend$isWebContentFilterRegulatedForLocalUserAndReturnError:
- _objc_retain_x7
CStrings:
+ "@72@0:8@16@24@32@40@48@56@?64"
+ "Communication Safety forced to enabled: %{public}d for user %@"
+ "Error checking if web content filter is forced for user %@: %{public}@ ; assuming forced"
+ "Error determining if parent sign-in is required for web content filter for user %@: %{public}@ ; assuming required"
+ "Failed to determine if Communication Safety is forced for user %@: %{public}@ ; assuming forced"
+ "Failed to determine if parent sign-in is required for Communication Safety for user %@: %{public}@ ; assuming required"
+ "Failed to fetch revoke access data for account %@: %{public}@. Assuming not revoke access mode and parent sign-in not required."
+ "Fetched revoke access data for account %@: isRevokeAccessModeEnabled=%d, isParentSignInRequired=%d"
+ "Parent sign-in required for Communication Safety change: %{public}d for user %@"
+ "Parent sign-in required for Web Content Filter change: %{public}d for user %@"
+ "STConnectToFamilyHelper - customShieldAssetID property not available yet (waiting for rdar://162647923)"
+ "STConnectToFamilyHelper - no regionAACID"
+ "STConnectToFamilyHelper - setting customShieldAssetID to: %{public}@"
+ "T@\"NSString\",C,N,V_regionAACID"
+ "TB,N,V_isParentSignInRequiredForAllowedAppsChange"
+ "Web Content Filter forced to Limit Adult Websites: %{public}d for user %@"
+ "_authenticateIfNeededForRestrictionsEnabledSpecifier:completionBlock:"
+ "_authenticateWithParentSignInOrPasscodeIfNeededForSpecifier:success:failure:"
+ "_authenticateWithPasscodeIfNeededForSpecifier:success:failure:"
+ "_isParentSignInRequiredForAllowedAppsChange"
+ "_regionAACID"
+ "_tryAuthenticatingThenIfNeededThenPerform:"
+ "authenticatableResource"
+ "connectToFamilySpecifierForUserDSID:regionAACID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:"
+ "customShieldAssetID"
+ "fetchImageGenerationAndRevokeAccessDataForAccountDSID:withCompletion:"
+ "initWithIsRevokeAccessModeEnabled:isParentSignInRequired:"
+ "initWithPresentingViewController:dsid:regionAACID:completion:"
+ "isParentSignInRequired"
+ "isParentSignInRequiredForAllowedAppsChange"
+ "isParentSignInRequiredForCommunicationSafetyForPersistenceController:error:"
+ "isParentSignInRequiredForTopLevelRestrictionsChange"
+ "isParentSignInRequiredForWebContentFilterForPersistenceController:error:"
+ "isRevokeAccessModeEnabled"
+ "regionAACID"
+ "revokeAccessData: isRevokeAccessModeEnabled=%d, isParentSignInRequired=%d"
+ "revokeAccessDataForAccountDSID:persistenceController:completionHandler:"
+ "setAuthenticatableResource:"
+ "setCustomShieldAssetID:"
+ "setIsParentSignInRequiredForAllowedAppsChange:"
+ "setRegionAACID:"
+ "setValue:forKey:"
+ "v24@?0@\"STRegulatoryManagerRevokeAccessData\"8@\"NSError\"16"
+ "v28@?0B8@\"STRegulatoryManagerRevokeAccessData\"12@\"NSError\"20"
- "@64@0:8@16@24@32@40@48@?56"
- "Error checking if web content filter is forced: %{public}@ ; assuming forced"
- "Error checking if web content filter is regulated: %{public}@ ; assuming regulated"
- "Failed to check revoke access mode: %{public}@"
- "Failed to determine if Communication Safety is forced: %{public}@ ; assuming forced"
- "Failed to determine if Communication Safety is regulated: %{public}@ ; assuming regulated"
- "Failed to fetch image generation or revoke access values: %{public}@"
- "Fetched revokeAccessMode:%d"
- "_authenticateIfNeededForSpecifier:success:failure:"
- "connectToFamilySpecifierForUserDSID:presentingViewController:promptTitle:promptSubtitle:promptButtonTitle:completion:"
- "fetchImageGenerationAndRevokeAccessModeForAccountDSID:withCompletion:"
- "initWithPresentingViewController:dsid:completion:"
- "isCommunicationSafetyRegulatedForLocalUserAndReturnError:"
- "isRevokeAccessModeEnabledForAccountDSID:completionHandler:"
- "isWebContentFilterRegulatedForLocalUserAndReturnError:"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "v24@?0B8B12@\"NSError\"16"

```
