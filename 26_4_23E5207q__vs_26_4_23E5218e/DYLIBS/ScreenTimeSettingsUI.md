## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-605.4.13.0.0
-  __TEXT.__text: 0x132d6c
+605.4.16.0.0
+  __TEXT.__text: 0x133fb4
   __TEXT.__auth_stubs: 0x2ed0
-  __TEXT.__objc_methlist: 0xc464
-  __TEXT.__const: 0x3da4
-  __TEXT.__cstring: 0xd055
-  __TEXT.__oslogstring: 0x5953
-  __TEXT.__gcc_except_tab: 0x1234
+  __TEXT.__objc_methlist: 0xc4ac
+  __TEXT.__const: 0x3de4
+  __TEXT.__cstring: 0xd145
+  __TEXT.__oslogstring: 0x5d03
+  __TEXT.__gcc_except_tab: 0x126c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0x44ea
   __TEXT.__constg_swiftt: 0x1538

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x88
-  __TEXT.__unwind_info: 0x3ff0
+  __TEXT.__unwind_info: 0x4028
   __TEXT.__eh_frame: 0x20c0
   __TEXT.__objc_classname: 0x2854
-  __TEXT.__objc_methname: 0x235ad
-  __TEXT.__objc_methtype: 0x4223
-  __TEXT.__objc_stubs: 0x16360
-  __DATA_CONST.__got: 0x1430
-  __DATA_CONST.__const: 0x2640
+  __TEXT.__objc_methname: 0x238bd
+  __TEXT.__objc_methtype: 0x42c3
+  __TEXT.__objc_stubs: 0x164c0
+  __DATA_CONST.__got: 0x1420
+  __DATA_CONST.__const: 0x2660
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d40
+  __DATA_CONST.__objc_selrefs: 0x6da8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x1778
-  __AUTH_CONST.__const: 0x3220
-  __AUTH_CONST.__cfstring: 0xaf80
-  __AUTH_CONST.__objc_const: 0x25da0
+  __AUTH_CONST.__const: 0x3240
+  __AUTH_CONST.__cfstring: 0xb060
+  __AUTH_CONST.__objc_const: 0x25de0
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH.__objc_data: 0x5170
   __AUTH.__data: 0x9a8
-  __DATA.__objc_ivar: 0xcf4
-  __DATA.__data: 0x27d0
+  __DATA.__objc_ivar: 0xcf8
+  __DATA.__data: 0x27c0
   __DATA.__bss: 0x1e40
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x9b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 501BE9B5-3370-38DE-BB37-8805365C0A5D
-  Functions: 6231
-  Symbols:   16692
-  CStrings:  9254
+  UUID: ACB26EE7-5D52-306D-8D78-4773AACAE26F
+  Functions: 6241
+  Symbols:   16727
+  CStrings:  9295
 
Symbols:
+ +[STRootViewModel keyPathsForValuesAffectingIsThirdPartyReplacingAppAndWebsiteActivity]
+ +[STRootViewModelCoordinator regulatoryAccountTypeForUser:authKitGetUserAgeRange:]
+ -[STAppAndWebsiteActivityOnboardingController _createAppAndWebsiteActivityControllerReplacingThirdParty:]
+ -[STAppAndWebsiteActivityOnboardingController presentOverViewController:replacingThirdParty:completionBlock:]
+ -[STContentPrivacyListController getRestrictionsEnabled:].cold.1
+ -[STContentPrivacyViewModel regulatoryAllowedAppsPolicy]
+ -[STContentPrivacyViewModel regulatoryContentRestrictionsPolicy]
+ -[STContentPrivacyViewModel setRegulatoryAllowedAppsPolicy:]
+ -[STContentPrivacyViewModel setRegulatoryContentRestrictionsPolicy:]
+ -[STIntroAppAndWebsiteActivityViewController initWithIntroductionModel:childName:isReplacingThirdParty:continueHandler:]
+ -[STIntroAppAndWebsiteActivityViewController isReplacingThirdParty]
+ -[STIntroductionController initWithDSID:childAge:childName:isReplacingThirdParty:updateExistingSettings:restrictionsDataSource:]
+ -[STIntroductionController isReplacingThirdParty]
+ -[STIntroductionController setIsReplacingThirdParty:]
+ -[STRestrictingApplicationsGroupSpecifierProvider getAuthorizationRecordWithIdentifier:fromRecords:]
+ -[STRestrictingApplicationsGroupSpecifierProvider setFamilyControlsEnabled:forSpecifier:].cold.1
+ -[STRootViewModel isThirdPartyReplacingAppAndWebsiteActivity]
+ -[STRootViewModelCoordinator _regulatoryAccountType]
+ -[STUIUser isThirdPartyReplacingAppAndWebsiteActivity]
+ -[STUIUser setIsThirdPartyReplacingAppAndWebsiteActivity:]
+ GCC_except_table109
+ GCC_except_table202
+ GCC_except_table211
+ _OBJC_IVAR_$_STContentPrivacyViewModel._regulatoryAllowedAppsPolicy
+ _OBJC_IVAR_$_STContentPrivacyViewModel._regulatoryContentRestrictionsPolicy
+ _OBJC_IVAR_$_STIntroAppAndWebsiteActivityViewController._isReplacingThirdParty
+ _OBJC_IVAR_$_STIntroductionController._isReplacingThirdParty
+ _OBJC_IVAR_$_STUIUser._isThirdPartyReplacingAppAndWebsiteActivity
+ _STBlueprintConfigurationTypeSystemWebContentFilterBasic
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1011
+ ___109-[STAppAndWebsiteActivityOnboardingController presentOverViewController:replacingThirdParty:completionBlock:]_block_invoke
+ ___128-[STIntroductionController initWithDSID:childAge:childName:isReplacingThirdParty:updateExistingSettings:restrictionsDataSource:]_block_invoke
+ ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.436
+ ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.436.cold.1
+ ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.515
+ ___52-[STRootViewModelCoordinator _regulatoryAccountType]_block_invoke
+ ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.319
+ ___69-[STRootViewModelCoordinator loadRegionRatingsWithCompletionHandler:]_block_invoke.469
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.820.cold.1
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.821
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.cold.5
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.443
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.443.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.457
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.457.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.459
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.459.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.460
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.460.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.463
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.463.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.464
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.829
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.828
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.840
+ ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.442
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.440
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.440.cold.1
+ ___block_descriptor_125_e8_32s40s48s56s64s72s80s88s96s104bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_134_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
+ ___block_descriptor_32_e26_B32?0^Q8"NSString"16^24l
+ ___block_descriptor_64_e8_32s40s48bs56w_e8_v12?0B8lw56l8s32l8s40l8s48l8
+ ___block_literal_global.1014
+ ___block_literal_global.456
+ ___block_literal_global.462
+ ___block_literal_global.477
+ ___block_literal_global.742
+ ___block_literal_global.845
+ _block_copy_helper.49
+ _block_descriptor.51
+ _block_destroy_helper.50
+ _objc_msgSend$_createAppAndWebsiteActivityControllerReplacingThirdParty:
+ _objc_msgSend$_regulatoryAccountType
+ _objc_msgSend$appsRatingFooterInfo
+ _objc_msgSend$attemptWebContentFilterRecovery
+ _objc_msgSend$cemConfiguration
+ _objc_msgSend$composeContentViewControllerWithAppExceptionsController:alertPresentingController:specifier:forManagedUser:areRestrictionsEditable:appsRatingEditable:appsRatingFooterText:runAfterPinAuthentication:
+ _objc_msgSend$contentRestrictions
+ _objc_msgSend$getAuthorizationRecordWithIdentifier:fromRecords:
+ _objc_msgSend$initWithDSID:childAge:childName:isReplacingThirdParty:updateExistingSettings:restrictionsDataSource:
+ _objc_msgSend$initWithIntroductionModel:childName:isReplacingThirdParty:continueHandler:
+ _objc_msgSend$isReplacingThirdParty
+ _objc_msgSend$isThirdPartyReplacingAppAndWebsiteActivity
+ _objc_msgSend$logWebContentFilterDiagnostics:
+ _objc_msgSend$makeIntroductionAppAndWebsiteActivityViewControllerWithIntroductionModel:childName:isReplacingThirdParty:continueHandler:
+ _objc_msgSend$presentOverViewController:replacingThirdParty:completionBlock:
+ _objc_msgSend$regulatoryAccountTypeForUser:authKitGetUserAgeRange:
+ _objc_msgSend$regulatoryAllowedAppsPolicy
+ _objc_msgSend$regulatoryContentRestrictionsPolicy
+ _objc_msgSend$setIsThirdPartyReplacingAppAndWebsiteActivity:
+ _objc_msgSend$setRegulatoryAllowedAppsPolicy:
+ _objc_msgSend$setRegulatoryContentRestrictionsPolicy:
+ _objc_msgSend$topLevelRestrictionsForcedToEnabled
- -[STAppAndWebsiteActivityOnboardingController _createAppAndWebsiteActivityController]
- -[STAppAndWebsiteActivityOnboardingController presentOverViewController:completionBlock:]
- -[STContentPrivacyViewModel allowedAppsShowsFullList]
- -[STContentPrivacyViewModel allowedAppsValueChangePrompts]
- -[STContentPrivacyViewModel appsRatingEditable]
- -[STContentPrivacyViewModel appsRatingForcedToDoNotAllow]
- -[STContentPrivacyViewModel setAllowedAppsShowsFullList:]
- -[STContentPrivacyViewModel setAllowedAppsValueChangePrompts:]
- -[STContentPrivacyViewModel setAppsRatingEditable:]
- -[STContentPrivacyViewModel setAppsRatingForcedToDoNotAllow:]
- -[STIntroAppAndWebsiteActivityViewController initWithIntroductionModel:childName:continueHandler:]
- -[STIntroductionController initWithDSID:childAge:childName:updateExistingSettings:restrictionsDataSource:]
- GCC_except_table113
- GCC_except_table195
- GCC_except_table204
- _OBJC_CLASS_$_CEMConfigurationBase
- _OBJC_IVAR_$_STContentPrivacyViewModel._allowedAppsShowsFullList
- _OBJC_IVAR_$_STContentPrivacyViewModel._allowedAppsValueChangePrompts
- _OBJC_IVAR_$_STContentPrivacyViewModel._appsRatingEditable
- _OBJC_IVAR_$_STContentPrivacyViewModel._appsRatingForcedToDoNotAllow
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.1023
- ___106-[STIntroductionController initWithDSID:childAge:childName:updateExistingSettings:restrictionsDataSource:]_block_invoke
- ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.427
- ___42-[STRootViewModelCoordinator validatePIN:]_block_invoke.427.cold.1
- ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.503
- ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.316
- ___69-[STRootViewModelCoordinator loadRegionRatingsWithCompletionHandler:]_block_invoke.460
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.832
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.832.cold.1
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.833
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.434
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.434.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.441
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.441.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.442
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.442.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.445
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.445.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.448
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.448.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.455
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.841
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.840
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.852
- ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.433
- ___89-[STAppAndWebsiteActivityOnboardingController presentOverViewController:completionBlock:]_block_invoke
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.431
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.431.cold.1
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s56l8s48l8
- ___block_literal_global.1026
- ___block_literal_global.447
- ___block_literal_global.453
- ___block_literal_global.727
- ___block_literal_global.857
- _block_copy_helper.61
- _block_descriptor.63
- _block_destroy_helper.62
- _objc_msgSend$_createAppAndWebsiteActivityController
- _objc_msgSend$allowedAppsShowsFullList
- _objc_msgSend$allowedAppsValueChangePrompts
- _objc_msgSend$composeContentViewControllerWithAppExceptionsController:alertPresentingController:specifier:forManagedUser:areRestrictionsEditable:appsRatingEditable:runAfterPinAuthentication:
- _objc_msgSend$initWithDSID:childAge:childName:updateExistingSettings:restrictionsDataSource:
- _objc_msgSend$makeIntroductionAppAndWebsiteActivityViewControllerWithIntroductionModel:childName:continueHandler:
- _objc_msgSend$presentOverViewController:completionBlock:
- _objc_msgSend$setAllowedAppsShowsFullList:
- _objc_msgSend$setAllowedAppsValueChangePrompts:
- _objc_msgSend$setAppsRatingEditable:
- _objc_msgSend$setAppsRatingForcedToDoNotAllow:
CStrings:
+ "-[STContentPrivacyListController getRestrictionsEnabled:]: restrictionsEnabled == false but topLevelRestrictionsForcedToEnabled == true. Returning true."
+ "@\"STRegulatoryAllowedAppsPolicy\""
+ "@\"STRegulatoryContentPrivacyRestrictionsPolicy\""
+ "@44@0:8@16@24B32@?36"
+ "@56@0:8@16@24@32B40B44@48"
+ "@68@0:8@16@24@32B40B44B48@52@?60"
+ "AppAndWebsiteActivityEDULimitedAccessDetail"
+ "AppAndWebsiteActivityEDULimitedAccessTitle"
+ "Attempting recovery for corrupted web content filter configuration"
+ "B32@?0^Q8@\"NSString\"16^@24"
+ "Error deserializing configuration type %{public}@ from DB, skipping (user can still modify settings)"
+ "IntroAppAndWebsiteActivityLimitedAccessDetail"
+ "IntroAppAndWebsiteActivityLimitedAccessTitle"
+ "KVOContextRegulatoryContentRestrictionsPolicy"
+ "No record found for specifier"
+ "Regulatory_GuardianVerificationReason"
+ "STRootViewModelCoordinator AuthKit failed to get user age range: error=%{public}@, isRemoteUser=%{public}d, attempting fallback to STUserType"
+ "STRootViewModelCoordinator determined regulatory account type from AuthKit: ageRange=%{public}ld, accountType=%{public}ld, isRemoteUser=%{public}d"
+ "STRootViewModelCoordinator determined regulatory account type from STUserType fallback: userType=%{public}ld, accountType=%{public}ld"
+ "STRootViewModelCoordinator no altDSID, keeping account type as unknown"
+ "STRootViewModelCoordinator user not in family, keeping account type as unknown: userType=%{public}ld"
+ "T@\"STRegulatoryAllowedAppsPolicy\",&,N,V_regulatoryAllowedAppsPolicy"
+ "T@\"STRegulatoryContentPrivacyRestrictionsPolicy\",&,N,V_regulatoryContentRestrictionsPolicy"
+ "TB,N,V_isReplacingThirdParty"
+ "TB,N,V_isThirdPartyReplacingAppAndWebsiteActivity"
+ "TB,R,V_isReplacingThirdParty"
+ "Web content filter recovery succeeded"
+ "_createAppAndWebsiteActivityControllerReplacingThirdParty:"
+ "_isReplacingThirdParty"
+ "_isThirdPartyReplacingAppAndWebsiteActivity"
+ "_regulatoryAccountType"
+ "_regulatoryAllowedAppsPolicy"
+ "_regulatoryContentRestrictionsPolicy"
+ "appsRatingFooterInfo"
+ "attemptWebContentFilterRecovery"
+ "cemConfiguration"
+ "com.apple.developer.family-controls.app-and-website-usage"
+ "composeContentViewControllerWithAppExceptionsController:alertPresentingController:specifier:forManagedUser:areRestrictionsEditable:appsRatingEditable:appsRatingFooterText:runAfterPinAuthentication:"
+ "contentPrivacyCoordinator.viewModel.regulatoryContentRestrictionsPolicy"
+ "getAuthorizationRecordWithIdentifier:fromRecords:"
+ "hand.raised.fill"
+ "initWithDSID:childAge:childName:isReplacingThirdParty:updateExistingSettings:restrictionsDataSource:"
+ "initWithIntroductionModel:childName:isReplacingThirdParty:continueHandler:"
+ "isReplacingThirdParty"
+ "isThirdPartyReplacingAppAndWebsiteActivity"
+ "keyPathsForValuesAffectingIsThirdPartyReplacingAppAndWebsiteActivity"
+ "logWebContentFilterDiagnostics:"
+ "makeIntroductionAppAndWebsiteActivityViewControllerWithIntroductionModel:childName:isReplacingThirdParty:continueHandler:"
+ "me.isThirdPartyReplacingAppAndWebsiteActivity"
+ "presentOverViewController:replacingThirdParty:completionBlock:"
+ "q32@0:8@16@?24"
+ "regulatoryAccountTypeForUser:authKitGetUserAgeRange:"
+ "regulatoryAllowedAppsPolicy"
+ "regulatoryContentRestrictionsPolicy"
+ "setIsReplacingThirdParty:"
+ "setIsThirdPartyReplacingAppAndWebsiteActivity:"
+ "setRegulatoryAllowedAppsPolicy:"
+ "setRegulatoryContentRestrictionsPolicy:"
+ "topLevelRestrictionsForcedToEnabled"
- "@60@0:8@16@24@32B40B44B48@?52"
- "Age Rating footer explaining why rating is not editable"
- "CommunicationSafetyEnabledGuardianVerificationReason"
- "Error deserializing configuration from DB: %{public}@"
- "T@\"NSArray\",C,N,V_allowedAppsValueChangePrompts"
- "TB,N,V_allowedAppsShowsFullList"
- "TB,N,V_appsRatingEditable"
- "TB,N,V_appsRatingForcedToDoNotAllow"
- "WebContentAutoFilterLimitedGuardianVerificationReason"
- "_allowedAppsShowsFullList"
- "_allowedAppsValueChangePrompts"
- "_appsRatingEditable"
- "_appsRatingForcedToDoNotAllow"
- "_createAppAndWebsiteActivityController"
- "allowedAppsShowsFullList"
- "allowedAppsValueChangePrompts"
- "com.apple.developer.family-controls-data"
- "composeContentViewControllerWithAppExceptionsController:alertPresentingController:specifier:forManagedUser:areRestrictionsEditable:appsRatingEditable:runAfterPinAuthentication:"
- "initWithDSID:childAge:childName:updateExistingSettings:restrictionsDataSource:"
- "makeIntroductionAppAndWebsiteActivityViewControllerWithIntroductionModel:childName:continueHandler:"
- "presentOverViewController:completionBlock:"
- "rating.apps"
- "setAllowedAppsShowsFullList:"
- "setAllowedAppsValueChangePrompts:"
- "setAppsRatingEditable:"
- "setAppsRatingForcedToDoNotAllow:"

```
