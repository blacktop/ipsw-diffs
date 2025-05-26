## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-503.4.14.0.0
-  __TEXT.__text: 0xebd4c
-  __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_methlist: 0x9a14
-  __TEXT.__const: 0x1734
-  __TEXT.__cstring: 0xbcf4
-  __TEXT.__oslogstring: 0x35a5
-  __TEXT.__gcc_except_tab: 0xb20
+503.5.12.3.0
+  __TEXT.__text: 0xf0318
+  __TEXT.__auth_stubs: 0x2250
+  __TEXT.__objc_methlist: 0x9b94
+  __TEXT.__const: 0x1764
+  __TEXT.__cstring: 0xc184
+  __TEXT.__oslogstring: 0x3b58
+  __TEXT.__gcc_except_tab: 0xb18
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1cd4
-  __TEXT.__swift5_reflstr: 0x4e9
+  __TEXT.__swift5_reflstr: 0x4f9
   __TEXT.__swift5_assocty: 0x1e8
-  __TEXT.__constg_swiftt: 0xac8
-  __TEXT.__swift5_fieldmd: 0x63c
+  __TEXT.__constg_swiftt: 0xad4
+  __TEXT.__swift5_fieldmd: 0x648
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_capture: 0x4a8
-  __TEXT.__unwind_info: 0x3378
-  __TEXT.__eh_frame: 0x1528
+  __TEXT.__swift5_capture: 0x4b8
+  __TEXT.__unwind_info: 0x34b0
+  __TEXT.__eh_frame: 0x1600
   __TEXT.__objc_classname: 0x1a71
-  __TEXT.__objc_methname: 0x1f165
+  __TEXT.__objc_methname: 0x1f2e7
   __TEXT.__objc_methtype: 0x36c5
-  __TEXT.__objc_stubs: 0x13ca0
-  __DATA_CONST.__got: 0x850
-  __DATA_CONST.__const: 0x2080
+  __TEXT.__objc_stubs: 0x13d80
+  __DATA_CONST.__got: 0x860
+  __DATA_CONST.__const: 0x20a0
   __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d9e0
-  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_const: 0x1db30
+  __DATA_CONST.__objc_selrefs: 0x5ef0
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_classrefs: 0xc68
+  __DATA_CONST.__objc_classrefs: 0xc88
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__objc_const: 0x4100
-  __AUTH_CONST.__cfstring: 0x9de0
+  __AUTH_CONST.__cfstring: 0xa120
   __AUTH_CONST.__objc_intobj: 0x858
-  __AUTH_CONST.__const: 0x1f30
+  __AUTH_CONST.__const: 0x1fc8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__auth_got: 0x1128
-  __AUTH.__objc_data: 0x3bc8
+  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH.__objc_data: 0x3bd8
   __AUTH.__data: 0x3f0
-  __DATA.__objc_ivar: 0xbc0
+  __DATA.__objc_ivar: 0xbc8
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x1bd0
+  __DATA.__data: 0x1bf0
   __DATA.__bss: 0xfd0
-  __DATA.__common: 0xb8
+  __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x9b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4886
-  Symbols:   14085
-  CStrings:  7012
+  Functions: 4946
+  Symbols:   14180
+  CStrings:  7074
 
Symbols:
+ -[STAllowLocationRestrictionsController devicePINController:didAcceptChangedPIN:]
+ -[STAllowLocationRestrictionsController devicePINController:didAcceptSetPIN:]
+ -[STAllowLocationRestrictionsController devicePINControllerDidDismissPINPane:]
+ -[STAllowLocationRestrictionsController didAcceptEnteredPIN:]
+ -[STAllowLocationRestrictionsController didAcceptRemovePIN]
+ -[STAllowLocationRestrictionsController didCancelEnteringPIN]
+ -[STAllowLocationRestrictionsController validatePIN:forPINController:]
+ -[STAllowPhotoRestrictionsController devicePINController:didAcceptChangedPIN:]
+ -[STAllowPhotoRestrictionsController devicePINController:didAcceptSetPIN:]
+ -[STAllowPhotoRestrictionsController devicePINControllerDidDismissPINPane:]
+ -[STAllowPhotoRestrictionsController didAcceptEnteredPIN:]
+ -[STAllowPhotoRestrictionsController didAcceptRemovePIN]
+ -[STAllowPhotoRestrictionsController didCancelEnteringPIN]
+ -[STAllowPhotoRestrictionsController validatePIN:forPINController:]
+ -[STAllowTCCRestrictionsController devicePINController:didAcceptChangedPIN:]
+ -[STAllowTCCRestrictionsController devicePINController:didAcceptSetPIN:]
+ -[STAllowTCCRestrictionsController devicePINControllerDidDismissPINPane:]
+ -[STAllowTCCRestrictionsController didAcceptEnteredPIN:]
+ -[STAllowTCCRestrictionsController didAcceptRemovePIN]
+ -[STAllowTCCRestrictionsController didCancelEnteringPIN]
+ -[STAllowTCCRestrictionsController validatePIN:forPINController:]
+ -[STContentPrivacyViewModel hasPasscode]
+ -[STContentPrivacyViewModel setHasPasscode:]
+ -[STPINListItemsController loadView]
+ -[STRestrictionsGroupSpecifierProvider informativeTextGroupSpecifier]
+ -[STRestrictionsGroupSpecifierProvider setInformativeTextGroupSpecifier:]
+ -[STRootViewModelCoordinator _validateDeviceIdentifier]
+ -[STRootViewModelCoordinator setDeviceIdentifier:]
+ -[STUsageDetailListController _isCloudSyncEnabledDidChangeFrom:to:]
+ -[STUsageDetailsViewModelCoordinator _downloadRemoteDeviceActivityDataAndRefreshLegacyUsageDataWithCompletionHandler:]
+ -[STUsageDetailsViewModelCoordinator _refreshLegacyUsageDataWithCompletionHandler:]
+ -[STUsageDetailsViewModelCoordinator initForLocalDeviceWithPersistenceController:selectedUsageReportType:usageContext:]
+ -[STUsageDetailsViewModelCoordinator initForLocalDeviceWithPersistenceController:selectedUsageReportType:usageContext:].cold.1
+ -[STUsageDetailsViewModelCoordinator initForLocalDeviceWithPersistenceController:selectedUsageReportType:usageContext:].cold.2
+ GCC_except_table169
+ GCC_except_table178
+ GCC_except_table34
+ GCC_except_table51
+ GCC_except_table89
+ GCC_except_table92
+ _OBJC_CLASS_$_STLocationServicesLockedUserNotificationContext
+ _OBJC_CLASS_$_STLocationServicesUnlockedUserNotificationContext
+ _OBJC_CLASS_$_STManagementState
+ _OBJC_CLASS_$_STUsage
+ _OBJC_IVAR_$_STContentPrivacyViewModel._hasPasscode
+ _OBJC_IVAR_$_STRestrictionsGroupSpecifierProvider._informativeTextGroupSpecifier
+ _PSControllerTitleKey
+ _STDisabledRadioGroupIDKey
+ __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.929
+ __OBJC_$_PROP_LIST_STUsageDetailsViewModelCoordinator.458
+ ___119-[STUsageDetailsViewModelCoordinator initForLocalDeviceWithPersistenceController:selectedUsageReportType:usageContext:]_block_invoke
+ ___208-[STUsageDetailsViewModelCoordinator _loadAllHistoricalDeviceActivityForUserWithAltDSID:deviceActivityIdentifier:selectedItemDisplayName:selectedDay:selectedWeek:hadUsageData:referenceDate:completionHandler:]_block_invoke.269
+ ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.439
+ ___55-[STRootViewModelCoordinator _validateDeviceIdentifier]_block_invoke
+ ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.269
+ ___67-[STUsageDetailListController _isCloudSyncEnabledDidChangeFrom:to:]_block_invoke
+ ___67-[STUsageDetailListController _isCloudSyncEnabledDidChangeFrom:to:]_block_invoke.cold.1
+ ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.246
+ ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.254
+ ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.258
+ ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.cold.5
+ ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.768
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.391
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.391.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.392
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.392.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.397
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.397.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.400
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.400.cold.1
+ ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.401
+ ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.775
+ ___83-[STUsageDetailsViewModelCoordinator _refreshLegacyUsageDataWithCompletionHandler:]_block_invoke
+ ___83-[STUsageDetailsViewModelCoordinator _refreshLegacyUsageDataWithCompletionHandler:]_block_invoke.cold.1
+ ___83-[STUsageDetailsViewModelCoordinator _refreshLegacyUsageDataWithCompletionHandler:]_block_invoke.cold.2
+ ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.774
+ ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.789
+ ___85-[STUsageReport initWithReportType:startDate:lastUpdatedDate:firstPickup:usageItems:]_block_invoke.28
+ ___85-[STUsageReport initWithReportType:startDate:lastUpdatedDate:firstPickup:usageItems:]_block_invoke.40
+ ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.383
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.379
+ ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.379.cold.1
+ ___block_descriptor_32_e27_B32?0"STUIDevice"8Q16^B24l
+ ___block_descriptor_32_e58_B32?0"_TtC20ScreenTimeSettingsUI13DeviceDetails"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e27_B32?0"STUIDevice"8Q16^B24ls32l8
+ ___block_descriptor_85_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s56l8r64l8s48l8
+ ___block_literal_global.249
+ ___block_literal_global.257
+ ___block_literal_global.399
+ ___block_literal_global.645
+ ___block_literal_global.932
+ ___createDevices_block_invoke
+ __unnamed_array_storage.197
+ __unnamed_array_storage.279
+ __unnamed_array_storage.288
+ _objc_msgSend$_downloadRemoteDeviceActivityDataAndRefreshLegacyUsageDataWithCompletionHandler:
+ _objc_msgSend$_isCloudSyncEnabledDidChangeFrom:to:
+ _objc_msgSend$_refreshLegacyUsageDataWithCompletionHandler:
+ _objc_msgSend$_validateDeviceIdentifier
+ _objc_msgSend$fetchRequestMatchingUser:device:
+ _objc_msgSend$postNotificationForContext:
+ _objc_msgSend$setDeviceIdentifier:
+ _objc_msgSend$setHasPasscode:
+ _objc_msgSend$userNotifications
- -[STCommunicationLimitsScreenTimeDetailListController tableView:cellForRowAtIndexPath:]
- -[STUsageDetailsViewModelCoordinator _didFinishRefreshingWithError:completionHandler:]
- GCC_except_table10
- GCC_except_table167
- GCC_except_table176
- GCC_except_table49
- __OBJC_$_PROP_LIST_STContentPrivacyViewModelCoordinator.893
- __OBJC_$_PROP_LIST_STUsageDetailsViewModelCoordinator.454
- ___208-[STUsageDetailsViewModelCoordinator _loadAllHistoricalDeviceActivityForUserWithAltDSID:deviceActivityIdentifier:selectedItemDisplayName:selectedDay:selectedWeek:hadUsageData:referenceDate:completionHandler:]_block_invoke.268
- ___44-[STRootViewModelCoordinator saveViewModel:]_block_invoke.432
- ___55-[PSListController(PIN) st_showPINSheetWithCompletion:]_block_invoke
- ___67-[STContentPrivacyListController setRestrictionsEnabled:specifier:]_block_invoke.246
- ___70-[STUsageDetailsViewModelCoordinator _refreshUsageDataWithCompletion:]_block_invoke.179
- ___70-[STUsageDetailsViewModelCoordinator _refreshUsageDataWithCompletion:]_block_invoke_2
- ___70-[STUsageDetailsViewModelCoordinator _refreshUsageDataWithCompletion:]_block_invoke_3
- ___70-[STUsageDetailsViewModelCoordinator _refreshUsageDataWithCompletion:]_block_invoke_3.cold.1
- ___70-[STUsageDetailsViewModelCoordinator _refreshUsageDataWithCompletion:]_block_invoke_3.cold.2
- ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.256
- ___73-[STUsageDetailsViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.259
- ___75-[STContentPrivacyViewModelCoordinator loadViewModelWithCompletionHandler:]_block_invoke.734
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.377
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.377.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.385
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.385.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.386
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.386.cold.1
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.387
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.390
- ___79-[STRootViewModelCoordinator applyIntroductionViewModel:withCompletionHandler:]_block_invoke.390.cold.1
- ___82-[STContentPrivacyViewModelCoordinator saveCommunicationLimits:completionHandler:]_block_invoke.741
- ___84-[STContentPrivacyViewModelCoordinator saveContentPrivacyEnabled:completionHandler:]_block_invoke.740
- ___84-[STContentPrivacyViewModelCoordinator saveValuesForRestrictions:completionHandler:]_block_invoke.755
- ___85-[STUsageReport initWithReportType:startDate:lastUpdatedDate:firstPickup:usageItems:]_block_invoke.30
- ___85-[STUsageReport initWithReportType:startDate:lastUpdatedDate:firstPickup:usageItems:]_block_invoke.42
- ___86-[STUsageDetailsViewModelCoordinator _didFinishRefreshingWithError:completionHandler:]_block_invoke
- ___88-[STRootViewModelCoordinator enableManagementWithPIN:recoveryAltDSID:completionHandler:]_block_invoke.376
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.372
- ___97-[STRootViewModelCoordinator _setPIN:recoveryAltDSID:shouldSetRecoveryAppleID:completionHandler:]_block_invoke.372.cold.1
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_84_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_90_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s56l8r64l8s48l8
- ___block_literal_global.392
- ___block_literal_global.636
- ___block_literal_global.896
- ___block_literal_global.9
- __unnamed_array_storage.191
- __unnamed_array_storage.256
- __unnamed_array_storage.265
- _objc_msgSend$_didFinishRefreshingWithError:completionHandler:
- _objc_msgSend$hasDeviceActivityData
CStrings:
+ "%K == YES"
+ "1"
+ "@56@0:8@16@24@32s40B44@48"
+ "AADC_AccountChangesSpecifierName"
+ "AADC_AllowChangesLabel"
+ "AADC_AllowedAppsAndFeaturesSpecifierHeader"
+ "AADC_AllowedAppsAndFeaturesSpecifierName"
+ "AADC_AllowedWebsitesSpecifierName"
+ "AADC_BackgroundAppActivitiesSpecifierName"
+ "AADC_BackgroundAppActivitiesSpecifierTitle"
+ "AADC_CellularChangesSpecifierName"
+ "AADC_CommunicationLimitsDetailText"
+ "AADC_ContentPrivacyDetailText"
+ "AADC_ContentRestrictionsSpecifierName"
+ "AADC_DrivingFocusSpecifierTitle"
+ "AADC_IntroWelcomeDetail"
+ "AADC_IntroWelcomeDetailChild"
+ "AADC_IntroWelcomeDetailGenericChild"
+ "AADC_OnlyAllowLabel"
+ "AADC_PasscodeAndFaceIDSpecifierName"
+ "AADC_ScreenTimeGroupSpecifierFooterText"
+ "AADC_TVProviderSpecifierTitle"
+ "AADC_WirelessChangesSpecifierName"
+ "B32@?0@\"STUIDevice\"8Q16^B24"
+ "B32@?0@\"_TtC20ScreenTimeSettingsUI13DeviceDetails\"8Q16^B24"
+ "Device Activity Device Found:  %{public}@ %{public}@ %{public}@"
+ "Device Activity Device added: %{public}@, %{public}@"
+ "Downloading remote device activity data."
+ "Error isCloudSyncEnabledDidChangeFrom: %@"
+ "Failed to create usage request: %{public}@"
+ "Failed to refresh local device ativity data: %{public}@"
+ "Failed to save usage request: %{public}@"
+ "Finding devices for user: %{public}@"
+ "Finished refreshing legacy usage data"
+ "InstallingMarketplacesSpecifierName"
+ "InstallingWebMarketplacesSpecifierName"
+ "IntroPresetsTurnOffRestrictionsAlertButton"
+ "IntroPresetsTurnOffRestrictionsAlertCancelButton"
+ "IntroPresetsTurnOffRestrictionsAlertChildMessage"
+ "IntroPresetsTurnOffRestrictionsAlertGenericChildMessage"
+ "IntroPresetsTurnOffRestrictionsAlertTitle"
+ "MarketplaceKit"
+ "Refreshing legacy usage data."
+ "Refreshing local device activity data."
+ "Rendering usage with Device Activity Data for user: %{public}@ device: %{public}@"
+ "Rendering usage with Legacy Screen Time Data for user: %{public}@ device: %{public}@"
+ "STDisabledRadioGroupIDKey"
+ "STUI:: STHistoricalUsageViewController _selectedWeekUsageReportDidChange setViewControllers, isInitialLoad : %d"
+ "STUI:: STHistoricalUsageViewController selectedCoreDuetIdentifier change %{public}@ %{public}@"
+ "STUsageDetailsViewModel: selectedWeek out of range, will reset for device: %{public}@, week usage report count: %lu, selectedWeek: %lus"
+ "Screen Time Device Found: coreDuetIdentifier: %{public}@ %{public}@ %{public}@"
+ "Screen Time Device added: %{public}@, %{public}@"
+ "Skipping legacy usage data refresh because a refresh is already in-progress."
+ "Successfully saved legacy usage request."
+ "T@\"NSString\",C,V_deviceIdentifier"
+ "TB,N,V_hasPasscode"
+ "WebInstallation"
+ "_downloadRemoteDeviceActivityDataAndRefreshLegacyUsageDataWithCompletionHandler:"
+ "_hasPasscode"
+ "_isCloudSyncEnabledDidChangeFrom:to:"
+ "_refreshLegacyUsageDataWithCompletionHandler:"
+ "_validateDeviceIdentifier"
+ "_validateDeviceIdentifier: deviceIdentifier %{public}@ not found. Switching to %{public}@"
+ "allowWebDistributionAppInstallation"
+ "application.store.allowWebDistributionAppInstallation"
+ "application.store.allowWebMarketplaceAppInstallation"
+ "fetchLastUpdatedDate Request failed for user %{public}@ and device %{public}@: %{public}@"
+ "fetchLastUpdatedDate no usage for user %{public}@ and device %{public}@: %{public}@"
+ "fetchRequestMatchingUser:device:"
+ "initForLocalDeviceWithPersistenceController Failed to fetch local device: %{public}@. Will default to All Devices"
+ "initForLocalDeviceWithPersistenceController Local Device Found:  %{public}@ %{public}@ %{public}@"
+ "initForLocalDeviceWithPersistenceController failed to fetch device details from DeviceActivity: %{public}@"
+ "initForLocalDeviceWithPersistenceController:selectedUsageReportType:usageContext:"
+ "initWithCoreDuetIdentifier:identifier:name:platform:isLocalDevice:lastUpdatedDate:"
+ "loadViewModel no localDevice found! Setting to first device found %@"
+ "postNotificationForContext:"
+ "setDeviceIdentifier:"
+ "setHasPasscode:"
+ "userNotifications"
+ "viewModel.selectedCoreDuetIdentifier"
- "@48@0:8@16@24@32s40B44"
- "Error creating usage request: %{public}@"
- "Error saving usage request: %{public}@"
- "Failed to refresh local Device Activity data: %{public}@"
- "InstallingMarketPlacesSpecifierName"
- "Missing coreDuetIdentifier for device activity device: %{public}@"
- "Missing coreDuetIdentifier for legacy usage device: %{public}@"
- "Rendering usage with Device Activity Data."
- "Rendering usage with Legacy Screen Time Data."
- "STUsageDetailsViewModel.m"
- "Saved updated usage request"
- "Saving updated usage request"
- "T@\"NSString\",R,C,V_deviceIdentifier"
- "Usage update changed"
- "_didFinishRefreshingWithError:completionHandler:"
- "application.store.allowMarketplaceAppInstallation"
- "initWithCoreDuetIdentifier:identifier:name:platform:isLocalDevice:"
- "stillLoading || NSLocationInRange(selectedWeek, NSMakeRange(STCurrentWeek, weekUsageReports.count))"

```
