## CarouselPreferenceServices

> `/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices`

```diff

-1114.2.10.0.0
-  __TEXT.__text: 0x2954c
-  __TEXT.__auth_stubs: 0x710
+1114.4.41.0.0
+  __TEXT.__text: 0x2ad14
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x31e0
   __TEXT.__const: 0x358
   __TEXT.__dlopen_cstrs: 0x6a

   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x2bd3
-  __TEXT.__gcc_except_tab: 0x790
+  __TEXT.__gcc_except_tab: 0x77c
+  __TEXT.__cstring: 0x2b79
   __TEXT.__oslogstring: 0x1938
-  __TEXT.__unwind_info: 0xd28
-  __TEXT.__objc_classname: 0xc5d
+  __TEXT.__unwind_info: 0xe28
+  __TEXT.__objc_classname: 0xcb7
   __TEXT.__objc_methname: 0x64da
   __TEXT.__objc_methtype: 0x158f
   __TEXT.__objc_stubs: 0x4b40

   __DATA_CONST.__objc_selrefs: 0x17c0
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x5f0
   __AUTH_CONST.__cfstring: 0x3260
   __AUTH_CONST.__objc_const: 0x6e40

   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x3a4
   __DATA.__data: 0xcc8
-  __DATA.__bss: 0x2d8
+  __DATA.__bss: 0x2c8
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6DFD07FE-E66F-3EE5-B520-40627E4D6DE2
+  UUID: 4D7C9EC8-F901-38EA-BFC0-6D5FC20F47F1
   Functions: 1150
-  Symbols:   4365
+  Symbols:   4361
   CStrings:  2391
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
Functions:
~ sub_230d34fb8 -> sub_2347cdfb8 : 24 -> 20
~ sub_230d35028 -> sub_2347ce024 : 24 -> 20
~ sub_230d3519c -> sub_2347ce194 : 12 -> 8
~ -[CSLPRFAppBacklightPrivacySettings hash] : 176 -> 180
~ -[CSLPRFAppBacklightPrivacySettings isEqual:] : 584 -> 572
~ -[CSLPRFAppBacklightPrivacySettings description] : 232 -> 240
~ -[CSLPRFAppBacklightPrivacySettings serialize] : 328 -> 344
~ _CSLPRFEqualAppBacklightPrivacySettingsValues : 364 -> 360
~ -[CSLPRFAppBacklightPrivacyResolvedSettings initWithSettings:globalSettings:] : 152 -> 144
~ -[CSLPRFAppBacklightPrivacySettings updateSettingsWithBlock:] : 380 -> 388
~ -[CSLPRFAppBacklightPrivacySettings initForApplication:isGlobalDefault:withSerialization:delegate:] : 492 -> 480
~ +[CSLPRFAppBacklightPrivacySettings sharedSettingsModel] : 84 -> 100
~ ___56+[CSLPRFAppBacklightPrivacySettings sharedSettingsModel]_block_invoke : 140 -> 144
~ +[CSLPRFAppBacklightPrivacySettings categoryForApplication:] : 184 -> 188
~ ___60+[CSLPRFAppBacklightPrivacySettings categoryForApplication:]_block_invoke : 204 -> 212
~ +[CSLPRFAppBacklightPrivacySettings globalSettingsWithSerialization:delegate:] : 188 -> 192
~ +[CSLPRFAppBacklightPrivacySettings settingsForApplication:withSerialization:delegate:] : 136 -> 128
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForLiveActivities:withIgnoredSpecifier:] : 340 -> 344
~ ___113-[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForLiveActivities:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) privacyDuringAlwaysOnForLiveActivitiesWithIgnoredSpecifier:] : 268 -> 280
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForNotification:withIgnoredSpecifier:] : 340 -> 344
~ ___111-[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForNotification:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) privacyDuringAlwaysOnForNotificationWithIgnoredSpecifier:] : 268 -> 280
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForApp:withIgnoredSpecifier:] : 340 -> 344
~ ___102-[CSLPRFAppBacklightPrivacySettings(PSSpecifier) setPrivacyDuringAlwaysOnForApp:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFAppBacklightPrivacySettings(PSSpecifier) privacyDuringAlwaysOnForAppWithIgnoredSpecifier:] : 268 -> 280
~ -[LSApplicationProxy(CarouselPreferenceServices) cslprf_safeCorrespondingApplicationRecord] : 328 -> 336
~ -[CSLPRFLocalApplicationLibrary applicationInstallsDidStart:] : 160 -> 164
~ ___61-[CSLPRFLocalApplicationLibrary applicationInstallsDidStart:]_block_invoke : 332 -> 356
~ -[CSLPRFLocalApplicationLibrary _applicationsUninstalledWithRecords:] : 668 -> 676
~ -[CSLPRFLocalApplicationLibrary _isVisibleApplicationForRecord:] : 184 -> 192
~ -[CSLPRFLocalApplicationLibrary applicationsDidUninstall:] : 100 -> 104
~ -[CSLPRFLocalApplicationLibrary applicationsDidInstall:] : 1200 -> 1236
~ -[CSLPRFLocalApplicationLibrary _stopObserving] : 140 -> 144
~ -[CSLPRFLocalApplicationLibrary addObserver:] : 228 -> 236
~ -[CSLPRFLocalApplicationLibrary allApplicationsWithCompletion:] : 116 -> 112
~ -[CSLPRFLocalApplicationLibrary allApplicationsDictionary] : 520 -> 532
~ ___58-[CSLPRFLocalApplicationLibrary allApplicationsDictionary]_block_invoke : 272 -> 284
~ -[CSLPRFLocalApplicationLibrary allApplications] : 76 -> 84
~ -[CSLPRFLocalApplicationLibrary applicationWithBundleIdentifier:completion:] : 124 -> 128
~ -[CSLPRFLocalApplicationLibrary applicationWithBundleIdentifier:] : 428 -> 436
~ -[CSLPRFLocalApplicationLibrary init] : 132 -> 136
~ +[CSLPRFDeviceUtilities screenImageNameWithPrefix:] : 272 -> 284
~ +[CSLPRFDeviceUtilities isHermes] : 96 -> 104
~ +[CSLPRFDeviceUtilities isTinker:] : 124 -> 128
~ +[CSLPRFDeviceUtilities seriesForProductType:] : 444 -> 452
~ +[CSLPRFDeviceUtilities bridgeController] : 168 -> 172
~ +[CSLPRFDeviceUtilities activePairedWatchUsesSolarium] : 64 -> 68
~ +[CSLPRFDeviceUtilities activePairedWatchSupportsControls] : 64 -> 68
~ +[CSLPRFDeviceUtilities activePairedWatchSupportsMoonstoneActions] : 64 -> 68
~ +[CSLPRFDeviceUtilities activePairedWatchSupportsLiveActivities] : 64 -> 68
~ +[CSLPRFDeviceUtilities activeWatch] : 112 -> 124
~ -[CSLPRFStingQuickSwitchSettings setQuickSwitchActionAvailability:] : 320 -> 328
~ -[CSLPRFStingQuickSwitchSettings setQuickSwitchEnabled:] : 288 -> 300
~ -[CSLPRFStingQuickSwitchSettings isQuickSwitchEnabled] : 68 -> 72
~ -[CSLPRFStingQuickSwitchSettings _toSettingValue] : 228 -> 236
~ -[CSLPRFStingQuickSwitchSettings fromSetting:] : 528 -> 548
~ -[CSLPRFStingQuickSwitchSettings didUpdate] : 256 -> 260
~ -[CSLPRFStingQuickSwitchSettings setValue:] : 160 -> 168
~ -[CSLPRFAppViewChoiceButton init] : 300 -> 320
~ -[CSLPRFStingQuickSwitchModel quickSwitchItemDidChange:] : 564 -> 584
~ -[CSLPRFStingQuickSwitchModel availableQuickSwitchActions] : 380 -> 384
~ -[CSLPRFStingQuickSwitchModel setQuickSwitchEnabled:] : 180 -> 184
~ -[CSLPRFStingQuickSwitchModel isQuickSwitchEnabled] : 88 -> 92
~ -[CSLPRFStingQuickSwitchModel lock_restoreFromSettings] : 800 -> 832
~ -[CSLPRFStingQuickSwitchModel restoreFromSettings] : 104 -> 108
~ -[CSLPRFStingQuickSwitchModel initWithDelegate:settingsModel:settings:] : 340 -> 344
~ -[CSLPRFStingQuickSwitchModel initWithDelegate:] : 280 -> 284
~ +[CSLPRFSharedWorkloop serialQueueWithQOSClass:label:] : 132 -> 140
~ +[CSLPRFSharedWorkloop dispatchWithQOSClass:block:] : 108 -> 112
~ +[CSLPRFSharedWorkloop workloop] : 84 -> 100
~ -[CSLPRFObservationHelper notifyObserversWithBlock:] : 304 -> 308
~ +[CSLPRFAppViewImageCache getImageForLauncherMode:] : 420 -> 432
~ _CSLPRFCachedAppViewImageURL : 624 -> 656
~ +[CSLPRFAppViewImageCache storeImage:forLauncherMode:] : 124 -> 132
~ +[CSLPRFAppSwitcherEditing logAppSwitcherEditingAction:fromSource:] : 272 -> 268
~ -[CSLPRFDepthAutoLaunchSettings description] : 292 -> 312
~ _NSStringFromCSLPRFDepthAutoLaunchBehavior : 144 -> 152
~ _NSStringFromCSLPRFDepthAutoLaunchThreshold : 156 -> 164
~ -[CSLPRFDepthAutoLaunchSettings hash] : 204 -> 212
~ -[CSLPRFDepthAutoLaunchSettings isEqual:] : 612 -> 604
~ -[CSLPRFMutableDepthAutoLaunchSettings setThreshold:] : 128 -> 132
~ -[CSLPRFMutableDepthAutoLaunchSettings setAutoLaunchBehavior:] : 128 -> 132
~ -[CSLPRFDepthAutoLaunchSettings copyWithZone:] : 4 -> 40
~ -[CSLPRFDepthAutoLaunchSettings initWithSettings:] : 152 -> 156
~ -[CSLPRFIconCache _writeMMappedImage:withName:] : 328 -> 320
~ ___47-[CSLPRFIconCache _writeMMappedImage:withName:]_block_invoke : 112 -> 120
~ ___47-[CSLPRFIconCache _writeMMappedImage:withName:]_block_invoke_2 : 96 -> 100
~ -[CSLPRFIconCache _loadMMappedImageWithName:] : 96 -> 104
~ -[CSLPRFIconCache _pathForIconName:] : 136 -> 144
~ -[CSLPRFIconCache _path] : 84 -> 100
~ ___24-[CSLPRFIconCache _path]_block_invoke : 140 -> 152
~ -[CSLPRFIconCache iconForName:fallBackToPersistentStoreIfNecessary:] : 128 -> 132
~ +[CSLPRFIconCache sharedIconCache] : 84 -> 100
~ _CSLActionTypeToSettingsActionType : 304 -> 284
~ _CSLIdentifierToLinkActionType : 124 -> 128
~ ___CSLIdentifierToLinkActionType_block_invoke : 236 -> 256
~ _CSLPRFStingAccessibilityActionTypeName : 112 -> 116
~ _getAXTripleClickHelpersClass : 224 -> 220
~ _CSLPRFIdentifierToStingAccessibilityActionType : 124 -> 128
~ ___CSLPRFIdentifierToStingAccessibilityActionType_block_invoke : 216 -> 220
~ _CSLPRFPerformAccessibilityActionForIdentifier : 188 -> 192
~ -[CSLPRFAppConduitApplicationLibrary applicationsUpdated:onDeviceWithPairingID:] : 504 -> 508
~ -[CSLPRFAppConduitApplicationLibrary applicationsInstalled:onDeviceWithPairingID:] : 504 -> 508
~ ___50-[CSLPRFAppConduitApplicationLibrary addObserver:]_block_invoke : 108 -> 112
~ ___70-[CSLPRFAppConduitApplicationLibrary _loadApplicationsWithCompletion:]_block_invoke : 208 -> 224
~ ___70-[CSLPRFAppConduitApplicationLibrary _loadApplicationsWithCompletion:]_block_invoke_3 : 684 -> 704
~ ___70-[CSLPRFAppConduitApplicationLibrary _loadApplicationsWithCompletion:]_block_invoke_2 : 92 -> 96
~ -[CSLPRFAppConduitApplicationLibrary applicationWithBundleIdentifier:completion:] : 196 -> 184
~ ___81-[CSLPRFAppConduitApplicationLibrary applicationWithBundleIdentifier:completion:]_block_invoke : 100 -> 104
~ -[CSLPRFAppConduitApplicationLibrary allApplications] : 76 -> 84
~ -[CSLPRFAppConduitApplicationLibrary applicationWithBundleIdentifier:] : 116 -> 120
~ -[CSLPRFAppConduitApplicationLibrary dealloc] : 104 -> 108
~ -[CSLPRFAppConduitApplicationLibrary initWithPairedWatch:] : 144 -> 136
~ -[CSLPRFCompositeApplicationLibrary applicationLibrary:didRemoveApplications:] : 2072 -> 2132
~ -[CSLPRFCompositeApplicationLibrary _applicationsByCounterpartFromApplications:] : 200 -> 204
~ -[CSLPRFCompositeApplicationLibrary _applicationOrCounterpartsForApplication:inApplications:orApplicationsByCounterpart:] : 604 -> 624
~ ___80-[CSLPRFCompositeApplicationLibrary _applicationsByCounterpartFromApplications:]_block_invoke : 268 -> 276
~ ___84-[CSLPRFCompositeApplicationLibrary _applicationLibrary:didAddOrUpdateApplications:]_block_invoke : 308 -> 316
~ -[CSLPRFCompositeApplicationLibrary _application:isUniqueAndNotCounterpartInApplications:orApplicationsByCounterpart:] : 88 -> 92
~ -[CSLPRFCompositeApplicationLibrary addObserver:] : 216 -> 228
~ -[CSLPRFCompositeApplicationLibrary _loadApplications] : 576 -> 568
~ ___54-[CSLPRFCompositeApplicationLibrary _loadApplications]_block_invoke : 120 -> 116
~ ___54-[CSLPRFCompositeApplicationLibrary _loadApplications]_block_invoke_2 : 852 -> 844
~ ___95-[CSLPRFCompositeApplicationLibrary _notifyObserversOfChangesWithApplications:oldApplications:]_block_invoke : 148 -> 152
~ -[CSLPRFCompositeApplicationLibrary allApplicationsWithCompletion:] : 116 -> 112
~ -[CSLPRFCompositeApplicationLibrary allApplicationsDictionary] : 72 -> 76
~ -[CSLPRFCompositeApplicationLibrary allApplications] : 76 -> 84
~ -[CSLPRFCompositeApplicationLibrary applicationWithBundleIdentifier:completion:] : 124 -> 128
~ -[CSLPRFCompositeApplicationLibrary applicationWithBundleIdentifier:] : 108 -> 116
~ -[CSLPRFCompositeApplicationLibrary initWithPrimaryLibrary:secondaryLibrary:] : 256 -> 260
~ -[CSLPRFDepthAutoLaunchAppSettingKincaidImpl setEnabledSetting:] : 12 -> 64
~ -[CSLPRFDepthAutoLaunchAppSettingKincaidImpl setChangeSourceSetting:] : 12 -> 64
~ -[CSLPRFDepthAutoLaunchAppSettingKincaidImpl setBundleIDSetting:] : 12 -> 64
~ -[CSLPRFDepthAutoLaunchAppSettingKincaidImpl twoWaySyncSettingDidUpdate:] : 108 -> 116
~ ___60-[CSLPRFDepthAutoLaunchAppSettingKincaidImpl applySettings:]_block_invoke : 592 -> 644
~ -[CSLPRFDepthAutoLaunchAppSettingKincaidImpl settings] : 280 -> 276
~ ___54-[CSLPRFDepthAutoLaunchAppSettingKincaidImpl settings]_block_invoke : 240 -> 264
~ +[CSLPRFAppSwitcherDefaultApplications defaultApplicationList] : 328 -> 336
~ -[CSLPRFConcurrentObserverStore setObservers:] : 12 -> 64
~ ___61-[CSLPRFConcurrentObserverStore enumerateObserversWithBlock:]_block_invoke : 92 -> 96
~ ___105-[CSLPRFConcurrentObserverStore performSelectorOnMainThreadWithRespondingObservers:object:waitUntilDone:]_block_invoke : 96 -> 104
~ ___48-[CSLPRFConcurrentObserverStore removeObserver:]_block_invoke : 176 -> 180
~ -[CSLPRFConcurrentObserverStore initWithServiceName:] : 108 -> 112
~ -[CSLPRFDepthAutoLaunchSettingsMigrator needsMigration] : 164 -> 172
~ -[CSLPRFDepthAutoLaunchSettingsMigrator migrateIfNeeded] : 156 -> 160
~ -[ACXRemoteApplication(CarouselPreferenceServices) cslprf_displayName] : 284 -> 312
~ -[CSLPRFIconFetcher _completeLoadForBundleID:image:error:] : 348 -> 344
~ -[CSLPRFIconFetcher _insertTask:forBundleID:] : 168 -> 172
~ -[CSLPRFIconFetcher hasPendingRequestsForBundleID:] : 64 -> 68
~ -[CSLPRFIconFetcher _loadNanoIconForBundleIdentifier:] : 388 -> 400
~ ___54-[CSLPRFIconFetcher _loadNanoIconForBundleIdentifier:]_block_invoke : 308 -> 312
~ -[CSLPRFIconFetcher _loadIconForBundleIdentifier:isPhoneApp:] : 336 -> 344
~ ___61-[CSLPRFIconFetcher _loadIconForBundleIdentifier:isPhoneApp:]_block_invoke : 176 -> 184
~ ___61-[CSLPRFIconFetcher _loadIconForBundleIdentifier:isPhoneApp:]_block_invoke_2 : 196 -> 204
~ -[CSLPRFIconFetcher iconFetchTaskForBundleIdentifier:isPhoneApp:completion:] : 384 -> 388
~ -[CSLPRFIconFetchTask invalidate] : 116 -> 120
~ -[CSLPRFIconFetcher genericIcon] : 204 -> 216
~ -[CSLPRFIconFetcher initWithIconCache:] : 140 -> 132
~ -[CSLPRFIconFetcher init] : 76 -> 80
~ -[CSLPRFStingSettingsModelControlItem setDefaultConfigurationIntent:] : 12 -> 64
~ -[CSLPRFStingSettingsModelControlItem setTitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelControlItem setIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelControlItem description] : 172 -> 180
~ -[CSLPRFStingSettingsModelControlItem isEqual:] : 480 -> 476
~ ___47-[CSLPRFStingSettingsModelControlItem isEqual:]_block_invoke_3 : 80 -> 88
~ -[CSLPRFStingSettingsModelControlItem hash] : 128 -> 132
~ -[CSLPRFStingSettingsModelControlItem initWithCoder:] : 188 -> 200
~ -[CSLPRFStingSettingsModelControlItem encodeWithCoder:] : 128 -> 136
~ -[CSLPRFNanoAppRegistryApplicationSource allApplicationsWithCompletion:] : 156 -> 164
~ ___72-[CSLPRFNanoAppRegistryApplicationSource allApplicationsWithCompletion:]_block_invoke : 188 -> 196
~ ___72-[CSLPRFNanoAppRegistryApplicationSource allApplicationsWithCompletion:]_block_invoke_2 : 776 -> 860
~ -[CSLPRFApp setRemoteApplicationRecord:] : 12 -> 64
~ -[CSLPRFApp hash] : 228 -> 232
~ -[CSLPRFApp isEqual:] : 968 -> 940
~ -[CSLPRFApp description] : 296 -> 304
~ -[CSLPRFApp supportsSmartStack] : 660 -> 684
~ ___31-[CSLPRFApp supportsSmartStack]_block_invoke : 164 -> 172
~ -[CSLPRFApp unionedBackgroundModes] : 244 -> 264
~ -[CSLPRFApp compare:] : 188 -> 204
~ -[CSLPRFApp initWithBundleIdentifier:localizedName:sdkVersion:supportsAlwaysOnDisplay:defaultsToPrivateAlwaysOnDisplayTreatment:applicationRecord:remoteApplicationRecord:bbSectionInfo:] : 804 -> 824
~ +[CSLPRFApp appWithBBSectionInfo:] : 492 -> 520
~ +[CSLPRFApp appWithApplicationRecord:] : 220 -> 232
~ +[CSLPRFApp appWithACXRemoteApplication:] : 220 -> 232
~ +[CSLPRFApp appWithBundleID:name:sdkVersion:supportsAlwaysOnDisplay:defaultsToPrivateAlwaysOnDisplayTreatment:] : 172 -> 164
~ -[CSLPRFStingConfigurationHistoryData setActionsDictionary:] : 12 -> 64
~ -[CSLPRFStingConfigurationHistoryData setVersion:] : 12 -> 64
~ -[CSLPRFStingConfigurationHistoryData description] : 148 -> 156
~ -[CSLPRFStingConfigurationHistoryData isEqual:] : 364 -> 360
~ -[CSLPRFStingConfigurationHistoryData hash] : 456 -> 460
~ -[CSLPRFStingConfigurationHistoryData initWithCoder:] : 156 -> 164
~ -[CSLPRFStingConfigurationHistoryData encodeWithCoder:] : 108 -> 116
~ +[CSLPRFStingConfigurationHistoryData fromExportData:] : 660 -> 684
~ -[CSLPRFStingSettingsModelData setStartWorkoutsDictionary:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setAccessibilityShortcutsArray:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setControlsDictionary:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setShortcutsDictionary:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setSecondaryActionsDictionary:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setActionsDictionary:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData setVersion:] : 12 -> 64
~ -[CSLPRFStingSettingsModelData description] : 308 -> 316
~ -[CSLPRFStingSettingsModelData isEqual:] : 872 -> 848
~ -[CSLPRFStingSettingsModelData hash] : 1076 -> 1080
~ -[CSLPRFStingSettingsModelData initWithCoder:] : 316 -> 344
~ -[CSLPRFStingSettingsModelData encodeWithCoder:] : 208 -> 216
~ +[CSLPRFStingSettingsModelData fromExportData:] : 824 -> 856
~ -[CSLPRFStingConfigurationHistoryItem setActionType:] : 12 -> 64
~ -[CSLPRFStingConfigurationHistoryItem setIdentifier:] : 12 -> 64
~ -[CSLPRFStingConfigurationHistoryItem setBundleID:] : 12 -> 64
~ -[CSLPRFStingConfigurationHistoryItem description] : 272 -> 280
~ -[CSLPRFStingConfigurationHistoryItem isEqual:] : 472 -> 464
~ -[CSLPRFStingConfigurationHistoryItem hash] : 128 -> 132
~ -[CSLPRFStingConfigurationHistoryItem initWithCoder:] : 188 -> 200
~ -[CSLPRFStingConfigurationHistoryItem encodeWithCoder:] : 128 -> 136
~ -[CSLPRFStingConfigurationHistoryItem initWithBundleID:actionType:identifier:] : 188 -> 184
~ -[CSLPRFAppCell blankIcon] : 112 -> 120
~ -[CSLPRFAppTableCellHelper getLazyIcon] : 528 -> 556
~ ___39-[CSLPRFAppTableCellHelper getLazyIcon]_block_invoke : 252 -> 256
~ -[CSLPRFAppTableCellHelper blankIcon] : 244 -> 268
~ -[CSLPRFAppSwitchCell blankIcon] : 112 -> 120
~ -[PSSpecifier(App) app] : 128 -> 144
~ -[CSLPRFReturnToAppSettings description] : 216 -> 224
~ -[CSLPRFReturnToAppSettings isEqual:] : 560 -> 548
~ -[CSLPRFReturnToAppSettings hash] : 144 -> 148
~ -[CSLPRFReturnToAppSettings toDictionary] : 268 -> 284
~ -[CSLPRFReturnToAppSettings setReturnToAppTimeout:] : 304 -> 312
~ -[CSLPRFReturnToAppSettings initWithDictionary:] : 272 -> 284
~ +[CSLPRFWatchApplicationLibrary libraryForWatchApplications] : 352 -> 376
~ -[CSLPRFTwoWaySyncSetting setValue:] : 224 -> 240
~ -[CSLPRFTwoWaySyncSetting safeValueOfType:] : 168 -> 192
~ -[CSLPRFTwoWaySyncSetting value] : 132 -> 156
~ -[CSLPRFTwoWaySyncSetting syncManager] : 84 -> 92
~ -[CSLPRFTwoWaySyncSetting domainAccessor] : 96 -> 104
~ -[CSLPRFTwoWaySyncSetting dealloc] : 140 -> 144
~ -[CSLPRFTwoWaySyncSetting migrate:withMapping:] : 256 -> 276
~ -[CSLPRFTwoWaySyncSetting observeValueForKeyPath:ofObject:change:context:] : 124 -> 128
~ -[CSLPRFTwoWaySyncSetting didUpdate] : 80 -> 84
~ -[CSLPRFTwoWaySyncSetting description] : 240 -> 260
~ -[CSLPRFTwoWaySyncSetting initWithKey:defaultValue:notification:] : 640 -> 652
~ ___65-[CSLPRFTwoWaySyncSetting initWithKey:defaultValue:notification:]_block_invoke : 204 -> 208
~ ___60-[CSLPRFLauncherViewModeSetting twoWaySyncSettingDidUpdate:]_block_invoke : 68 -> 72
~ -[CSLPRFLauncherViewModeSetting setLauncherViewMode:reason:] : 600 -> 636
~ -[CSLPRFLauncherViewModeSetting launcherViewModeReason] : 60 -> 64
~ -[CSLPRFLauncherViewModeSetting launcherViewMode] : 320 -> 328
~ -[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl twoWaySyncSettingDidUpdate:] : 88 -> 92
~ -[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl _updateWithDictionary:] : 192 -> 200
~ -[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl applySettings:] : 192 -> 204
~ -[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl init] : 184 -> 188
~ +[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl settingsForDictionary:] : 584 -> 536
~ +[CSLPRFDepthAutoLaunchAppSettingLighthouseImpl dictionaryForSettings:] : 328 -> 348
~ -[CSLPRFPerApplicationSettingsPSSpecifierFactory updateSpecifier:withSettings:] : 116 -> 120
~ -[CSLPRFPerApplicationSettingsPSSpecifierFactory specifierForSettings:set:get:] : 420 -> 444
~ -[CSLPRFStingSettingsModel setSettingsData:] : 12 -> 64
~ -[CSLPRFStingSettingsModel setActionIdentifierToSupportedBundleIDsMap:] : 12 -> 64
~ -[CSLPRFStingSettingsModel setDefaultActionTypeItems:] : 12 -> 64
~ -[CSLPRFStingSettingsModel twoWaySyncSettingDidUpdate:] : 116 -> 120
~ -[CSLPRFStingSettingsModel _lock_rebuildModels] : 128 -> 140
~ -[CSLPRFStingSettingsModel rebuildModel] : 160 -> 164
~ -[CSLPRFStingSettingsModel _lock_isLinkActionSupportedForIdentifier:] : 188 -> 208
~ -[CSLPRFStingSettingsModel _modelItemWithActionType:] : 232 -> 240
~ -[CSLPRFStingSettingsModel _buildActionIdentifierToSupportedBundleIDsMap:] : 308 -> 312
~ ___74-[CSLPRFStingSettingsModel _buildActionIdentifierToSupportedBundleIDsMap:]_block_invoke : 536 -> 560
~ -[CSLPRFStingSettingsModel _buildDefaultActionTypeItems] : 700 -> 752
~ -[CSLPRFStingSettingsModel quickActionItems] : 504 -> 508
~ ___44-[CSLPRFStingSettingsModel quickActionItems]_block_invoke : 328 -> 336
~ ___40-[CSLPRFStingSettingsModel controlItems]_block_invoke : 184 -> 192
~ ___40-[CSLPRFStingSettingsModel controlItems]_block_invoke_2 : 152 -> 148
~ ___41-[CSLPRFStingSettingsModel shortcutItems]_block_invoke : 184 -> 192
~ ___41-[CSLPRFStingSettingsModel shortcutItems]_block_invoke_2 : 152 -> 148
~ -[CSLPRFStingSettingsModel startWorkoutsListForBundleID:] : 356 -> 352
~ ___57-[CSLPRFStingSettingsModel startWorkoutsListForBundleID:]_block_invoke : 176 -> 188
~ -[CSLPRFStingSettingsModel defaultQuickActionItems] : 328 -> 324
~ ___51-[CSLPRFStingSettingsModel defaultQuickActionItems]_block_invoke : 112 -> 116
~ -[CSLPRFStingSettingsModel bundleIDsForActionType:] : 392 -> 380
~ ___51-[CSLPRFStingSettingsModel bundleIDsForActionType:]_block_invoke : 140 -> 148
~ -[CSLPRFStingSettingsModel init] : 148 -> 152
~ +[CSLPRFStingSettingsModel alternateActionNameForActionType:] : 464 -> 496
~ +[CSLPRFStingSettingsModel actionNameForActionType:] : 676 -> 732
~ +[CSLPRFStingSettingsModel sfSymbolAssetNameForActionType:] : 192 -> 200
~ _cslprf_app_library_log : 84 -> 100
~ _cslprf_app_switcher_log : 84 -> 100
~ _cslprf_dock_log : 84 -> 100
~ _cslprf_sessions_log : 84 -> 100
~ _cslprf_settings_log : 84 -> 100
~ _cslprf_sting_log : 84 -> 100
~ _cslprf_sting_settings_log : 84 -> 100
~ _cslprf_systemstate_log : 84 -> 100
~ _cslprf_backlight_log : 84 -> 100
~ _cslprf_diagnostics_log : 84 -> 100
~ _cslprf_fluidui_log : 84 -> 100
~ _cslprf_icon_log : 84 -> 100
~ _cslprf_icon_field_log : 84 -> 100
~ _cslprf_startup_log : 84 -> 100
~ _cslprf_ui_log : 84 -> 100
~ -[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:] : 352 -> 356
~ ___79-[CSLPRFAppViewImageProvider retrieveImageForLauncherViewMode:size:completion:]_block_invoke : 440 -> 428
~ +[CSLPRFApplicationLibrary _withClassLock_libraryForLocation:] : 600 -> 624
~ +[CSLPRFApplicationLibrary libraryForLocation:] : 444 -> 456
~ +[CSLPRFApplicationLibrary sharedLibraryForLocation:] : 464 -> 472
~ -[CSLPRFStingSettingsModelWorkoutItem setWorkoutIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelWorkoutItem setSubtitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelWorkoutItem setTitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelWorkoutItem description] : 164 -> 172
~ -[CSLPRFStingSettingsModelWorkoutItem isEqual:] : 464 -> 456
~ -[CSLPRFStingSettingsModelWorkoutItem hash] : 128 -> 132
~ -[CSLPRFStingSettingsModelWorkoutItem initWithCoder:] : 188 -> 200
~ -[CSLPRFStingSettingsModelWorkoutItem encodeWithCoder:] : 128 -> 136
~ -[CSLPRFLegacyWatchApplicationLibrary applicationsUpdated:onDeviceWithPairingID:] : 492 -> 496
~ -[CSLPRFLegacyWatchApplicationLibrary applicationsInstalled:onDeviceWithPairingID:] : 492 -> 496
~ -[CSLPRFLegacyWatchApplicationLibrary nanoRegistrySource:updatedWithAllApplications:] : 1356 -> 1392
~ ___85-[CSLPRFLegacyWatchApplicationLibrary nanoRegistrySource:updatedWithAllApplications:]_block_invoke_2 : 72 -> 76
~ ___85-[CSLPRFLegacyWatchApplicationLibrary nanoRegistrySource:updatedWithAllApplications:]_block_invoke_4 : 72 -> 76
~ ___85-[CSLPRFLegacyWatchApplicationLibrary nanoRegistrySource:updatedWithAllApplications:]_block_invoke_6 : 112 -> 116
~ ___51-[CSLPRFLegacyWatchApplicationLibrary addObserver:]_block_invoke : 108 -> 112
~ ___71-[CSLPRFLegacyWatchApplicationLibrary _loadApplicationsWithCompletion:]_block_invoke : 432 -> 428
~ ___108-[CSLPRFLegacyWatchApplicationLibrary _withFirstPartyApplications:loadAppConduitApplicationsWithCompletion:]_block_invoke : 680 -> 696
~ ___108-[CSLPRFLegacyWatchApplicationLibrary _withFirstPartyApplications:loadAppConduitApplicationsWithCompletion:]_block_invoke_2 : 536 -> 552
~ ___108-[CSLPRFLegacyWatchApplicationLibrary _withFirstPartyApplications:loadAppConduitApplicationsWithCompletion:]_block_invoke.16 : 92 -> 96
~ -[CSLPRFLegacyWatchApplicationLibrary applicationWithBundleIdentifier:completion:] : 196 -> 184
~ ___82-[CSLPRFLegacyWatchApplicationLibrary applicationWithBundleIdentifier:completion:]_block_invoke : 100 -> 104
~ -[CSLPRFLegacyWatchApplicationLibrary allApplications] : 76 -> 84
~ -[CSLPRFLegacyWatchApplicationLibrary applicationWithBundleIdentifier:] : 116 -> 120
~ -[CSLPRFLegacyWatchApplicationLibrary dealloc] : 116 -> 120
~ -[CSLPRFLegacyWatchApplicationLibrary initWithPairedWatch:] : 180 -> 172
~ -[CSLPRFStingSettingsModelAccessibilityItem setTitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelAccessibilityItem setIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelAccessibilityItem description] : 140 -> 148
~ -[CSLPRFStingSettingsModelAccessibilityItem isEqual:] : 364 -> 360
~ -[CSLPRFStingSettingsModelAccessibilityItem hash] : 108 -> 112
~ -[CSLPRFStingSettingsModelAccessibilityItem initWithCoder:] : 156 -> 164
~ -[CSLPRFStingSettingsModelAccessibilityItem initWithActionType:] : 260 -> 276
~ -[CSLPRFStingSettingsModelAccessibilityItem encodeWithCoder:] : 108 -> 116
~ +[CSLPRFStingSettingsModelAccessibilityItem defaultItems] : 168 -> 176
~ ___57+[CSLPRFStingSettingsModelAccessibilityItem defaultItems]_block_invoke : 112 -> 120
~ -[CSLPRFStingSettingsItem description] : 200 -> 208
~ -[CSLPRFStingSettingsItem subtitle] : 260 -> 268
~ -[CSLPRFStingSettingsItem initWithIdentifier:title:actionType:assetName:] : 224 -> 208
~ -[CSLPRFStingSettingsModelAction setTitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelAction setStartActionIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelAction setActionIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelAction description] : 188 -> 196
~ -[CSLPRFStingSettingsModelAction isEqual:] : 464 -> 456
~ -[CSLPRFStingSettingsModelAction hash] : 128 -> 132
~ -[CSLPRFStingSettingsModelAction initWithCoder:] : 188 -> 200
~ -[CSLPRFStingSettingsModelAction encodeWithCoder:] : 128 -> 136
~ -[CSLPRFPerApplicationSettingsModel didUpdateSettings:] : 640 -> 656
~ -[CSLPRFPerApplicationSettingsModel _globalSettingsForCustomizedSettings:] : 156 -> 168
~ -[CSLPRFPerApplicationSettingsModel twoWaySyncSettingDidUpdate:] : 1148 -> 1200
~ -[CSLPRFPerApplicationSettingsModel settingsObjectForBundleId:customizedSettings:existingSettings:] : 212 -> 224
~ -[CSLPRFPerApplicationSettingsModel applicationLibrary:didRemoveApplications:] : 372 -> 368
~ -[CSLPRFPerApplicationSettingsModel _processAddedOrUpdatedApplications:] : 1136 -> 1184
~ ___72-[CSLPRFPerApplicationSettingsModel _processAddedOrUpdatedApplications:]_block_invoke : 160 -> 176
~ -[CSLPRFPerApplicationSettingsModel bundleIdentifiersWithSettings] : 84 -> 88
~ -[CSLPRFPerApplicationSettingsModel settingsForBundleIdentifier:] : 120 -> 124
~ -[CSLPRFPerApplicationSettingsModel globalSettings] : 396 -> 404
~ -[CSLPRFPerApplicationSettingsModel settingsForApplication:] : 204 -> 220
~ -[CSLPRFPerApplicationSettingsModel _lock_customizedSettingsForBundleIdentifier:] : 208 -> 216
~ -[CSLPRFPerApplicationSettingsModel resolvedSettingsForBundleIdentifier:] : 124 -> 136
~ -[CSLPRFPerApplicationSettingsModel resolvedSettingsForApplication:] : 124 -> 136
~ -[CSLPRFPerApplicationSettingsModel allApplicationSettings] : 84 -> 88
~ -[CSLPRFPerApplicationSettingsModel initWithApplicationLibrary:perApplicationSettingsClass:] : 356 -> 372
~ -[CSLPRFPairing isTinker] : 60 -> 64
~ -[CSLPRFPairing _didPair] : 260 -> 268
~ __CSLPairingIsTinker : 112 -> 124
~ -[CSLPRFPairing init] : 252 -> 260
~ +[CSLPRFPairing shared] : 160 -> 176
~ _CSLPairingIsTinker : 64 -> 68
~ -[CSLPRFDepthAutoLaunchAppSetting autoLaunchSettingCoordinator:didUpdateSettings:] : 80 -> 84
~ -[CSLPRFDepthAutoLaunchAppSetting updateSettingsWithBlock:] : 172 -> 180
~ -[CSLPRFDepthAutoLaunchAppSetting settings] : 96 -> 104
~ -[CSLPRFDepthAutoLaunchAppSetting initWithVersion:] : 260 -> 264
~ +[CSLPRFDepthAutoLaunchAppSetting preferredVersion] : 184 -> 196
~ -[CSLPRFStingConfigurationHistorySetting write:] : 228 -> 240
~ -[CSLPRFStingConfigurationHistorySetting read] : 92 -> 100
~ -[CSLPRFStingConfigurationHistorySetting init] : 284 -> 292
~ _CSLSAllowReturnToAppUntilCrownPress : 316 -> 320
~ ___CSLSAllowReturnToAppUntilCrownPress_block_invoke : 128 -> 136
~ -[CSLAppSwitcherFavoritesSetting setDelegate:] : 112 -> 116
~ -[CSLAppSwitcherFavoritesSetting setMaximumFavorites:] : 92 -> 96
~ ___50-[CSLAppSwitcherFavoritesSetting maximumFavorites]_block_invoke : 96 -> 100
~ -[CSLAppSwitcherFavoritesSetting favorites] : 256 -> 252
~ ___43-[CSLAppSwitcherFavoritesSetting favorites]_block_invoke : 176 -> 188
~ -[CSLAppSwitcherFavoritesSetting twoWaySyncSettingDidUpdate:] : 104 -> 108
~ -[CSLAppSwitcherFavoritesSetting init] : 232 -> 236
~ -[CSLPRFStingConfigurationHistory _historyItemForActionType:] : 1160 -> 1180
~ -[CSLPRFStingConfigurationHistory _itemForActionType:withBundleID:] : 460 -> 480
~ -[CSLPRFStingConfigurationHistory itemForWorkoutWithBundleID:] : 568 -> 592
~ -[CSLPRFStingConfigurationHistory itemForActionType:] : 4692 -> 4848
~ ___53-[CSLPRFStingConfigurationHistory itemForActionType:]_block_invoke : 60 -> 80
~ ___53-[CSLPRFStingConfigurationHistory itemForActionType:]_block_invoke.8 : 60 -> 80
~ -[CSLPRFStingConfigurationHistory addHistoryItem:] : 1424 -> 1460
~ -[CSLPRFStingConfigurationHistory isValidHistoryItem:] : 540 -> 560
~ -[CSLPRFStingConfigurationHistory initWithSetting:model:] : 152 -> 144
~ -[CSLPRFBulletinBoardApplicationLibrary addObserver:] : 116 -> 120
~ -[CSLPRFBulletinBoardApplicationLibrary allApplicationsWithCompletion:] : 116 -> 112
~ -[CSLPRFBulletinBoardApplicationLibrary allApplicationsDictionary] : 72 -> 76
~ -[CSLPRFBulletinBoardApplicationLibrary _loadApplications] : 840 -> 856
~ ___58-[CSLPRFBulletinBoardApplicationLibrary _loadApplications]_block_invoke : 852 -> 844
~ ___99-[CSLPRFBulletinBoardApplicationLibrary _notifyObserversOfChangesWithApplications:oldApplications:]_block_invoke : 148 -> 152
~ -[CSLPRFBulletinBoardApplicationLibrary allApplications] : 76 -> 84
~ -[CSLPRFBulletinBoardApplicationLibrary applicationWithBundleIdentifier:completion:] : 124 -> 128
~ -[CSLPRFBulletinBoardApplicationLibrary applicationWithBundleIdentifier:] : 156 -> 160
~ -[CSLPRFWatchChoiceView setSelected:] : 144 -> 152
~ -[CSLPRFWatchChoiceView _addWatchScreenImageIfNecessary:] : 1040 -> 1088
~ -[CSLPRFWatchChoiceView _createWatchViewForChoice:] : 312 -> 332
~ -[CSLPRFWatchChoiceView _updateWatchViewPreferredWidth] : 168 -> 176
~ -[CSLPRFStingSystemSettings twoWaySyncSettingDidUpdate:] : 216 -> 220
~ -[CSLPRFStingSystemSettings write:] : 88 -> 92
~ -[CSLPRFStingSystemSettings read] : 92 -> 100
~ -[CSLPRFStingSettingsModelShortcutItem setTitle:] : 12 -> 64
~ -[CSLPRFStingSettingsModelShortcutItem setIdentifier:] : 12 -> 64
~ -[CSLPRFStingSettingsModelShortcutItem description] : 140 -> 148
~ -[CSLPRFStingSettingsModelShortcutItem isEqual:] : 364 -> 360
~ -[CSLPRFStingSettingsModelShortcutItem hash] : 108 -> 112
~ -[CSLPRFStingSettingsModelShortcutItem initWithCoder:] : 156 -> 164
~ -[CSLPRFStingSettingsModelShortcutItem encodeWithCoder:] : 108 -> 116
~ -[CSLPRFAppIconCellHelper didCompleteLoadForIdentifier:] : 380 -> 392
~ -[CSLPRFAppIconCellHelper loadIconForSpecifier:iconIdentifier:] : 516 -> 536
~ ___63-[CSLPRFAppIconCellHelper loadIconForSpecifier:iconIdentifier:]_block_invoke : 228 -> 232
~ -[CSLPRFAppIconCellHelper fetchLazyIconForSpecifier:] : 304 -> 332
~ -[CSLPRFAppIconCellHelper init] : 104 -> 108
~ -[CSLPRFWatchChoice setImageProvider:] : 12 -> 64
~ -[CSLPRFWatchChoice setScreenImage:] : 12 -> 64
~ -[CSLPRFWatchChoice initWithChoice:] : 224 -> 232
~ +[CSLPRFWatchChoice watchChoices] : 192 -> 204
~ ___49-[CSLPRFAppViewChoiceView _updateSelectedChoice:]_block_invoke : 264 -> 268
~ -[CSLPRFAppViewChoiceView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:] : 148 -> 152
~ -[CSLPRFDefaultAppDataProvider loadAppsWithCompletion:completionQueue:] : 220 -> 208
~ ___71-[CSLPRFDefaultAppDataProvider loadAppsWithCompletion:completionQueue:]_block_invoke : 176 -> 172
~ ___71-[CSLPRFDefaultAppDataProvider loadAppsWithCompletion:completionQueue:]_block_invoke_2 : 148 -> 156
~ -[CSLPRFDefaultAppDataProvider init] : 120 -> 124
~ -[CSLPRFStingConfiguration description] : 392 -> 404
~ -[CSLPRFStingConfiguration _lock_settingsDictionary] : 116 -> 124
~ -[CSLPRFStingConfiguration reset] : 264 -> 268
~ ___33-[CSLPRFStingConfiguration reset]_block_invoke : 96 -> 100
~ ___38-[CSLPRFStingConfiguration setSource:]_block_invoke : 312 -> 324
~ ___34-[CSLPRFStingConfiguration source]_block_invoke : 148 -> 156
~ ___49-[CSLPRFStingConfiguration setWorkoutIdentifier:]_block_invoke : 284 -> 292
~ -[CSLPRFStingConfiguration controlConfigurationIntent] : 256 -> 252
~ ___54-[CSLPRFStingConfiguration controlConfigurationIntent]_block_invoke : 256 -> 272
~ -[CSLPRFStingConfiguration workoutIdentifier] : 256 -> 252
~ ___45-[CSLPRFStingConfiguration workoutIdentifier]_block_invoke : 148 -> 160
~ -[CSLPRFStingConfiguration _locked_setConfigurationForBundleID:actionType:identifier:intent:source:] : 800 -> 808
~ ___100-[CSLPRFStingConfiguration _locked_setConfigurationForBundleID:actionType:identifier:intent:source:]_block_invoke : 88 -> 96
~ -[CSLPRFStingConfiguration setControlConfigurationForBundleID:identifier:intent:source:] : 240 -> 224
~ -[CSLPRFStingConfiguration setConfigurationForBundleID:actionType:identifier:source:] : 212 -> 204
~ -[CSLPRFStingConfiguration setExpectedConfigurationForAction:source:] : 168 -> 180
~ ___40-[CSLPRFStingConfiguration setBundleID:]_block_invoke : 88 -> 96
~ ___40-[CSLPRFStingConfiguration setBundleID:]_block_invoke_2 : 284 -> 292
~ -[CSLPRFStingConfiguration bundleID] : 328 -> 332
~ ___36-[CSLPRFStingConfiguration bundleID]_block_invoke : 148 -> 160
~ ___42-[CSLPRFStingConfiguration setActionType:]_block_invoke : 332 -> 336
~ ___38-[CSLPRFStingConfiguration actionType]_block_invoke : 148 -> 156
~ -[CSLPRFStingConfiguration depthAutoLaunchAppSettingDidUpdate:] : 204 -> 192
~ ___63-[CSLPRFStingConfiguration depthAutoLaunchAppSettingDidUpdate:]_block_invoke : 244 -> 252
~ -[CSLPRFStingConfiguration twoWaySyncSettingDidUpdate:] : 204 -> 192
~ ___55-[CSLPRFStingConfiguration twoWaySyncSettingDidUpdate:]_block_invoke : 244 -> 252
~ -[CSLPRFStingConfiguration initWithDelegate:] : 380 -> 384
~ -[CSLPRFAppViewChoiceCell retrieveImageForLauncherViewMode:size:completion:] : 336 -> 332
~ ___76-[CSLPRFAppViewChoiceCell retrieveImageForLauncherViewMode:size:completion:]_block_invoke : 300 -> 308
~ -[CSLPRFAppViewChoiceCell bundleID] : 76 -> 84
~ -[CSLPRFAppViewChoiceCell localize:] : 340 -> 360
~ -[CSLPRFAppViewChoiceCell layoutSubviews] : 180 -> 188
~ -[CSLPRFAppViewChoiceCell initWithStyle:reuseIdentifier:] : 912 -> 980
~ ___57-[CSLPRFAppViewChoiceCell initWithStyle:reuseIdentifier:]_block_invoke : 148 -> 160
~ _CSLAlertServiceIsApplePay : 88 -> 92
~ _CSLAlertServiceOverControlCenter : 80 -> 84
~ -[CSLPRFReturnToAppSettingsModel setSettings:forBundleID:] : 316 -> 300
~ ___58-[CSLPRFReturnToAppSettingsModel setSettings:forBundleID:]_block_invoke_2 : 96 -> 104
~ -[CSLPRFReturnToAppSettingsModel settingsForBundleID:] : 296 -> 292
~ ___54-[CSLPRFReturnToAppSettingsModel settingsForBundleID:]_block_invoke : 80 -> 84
~ -[CSLPRFReturnToAppSettingsModel saveAppSettings] : 320 -> 324
~ ___49-[CSLPRFReturnToAppSettingsModel saveAppSettings]_block_invoke : 88 -> 92
~ ___51-[CSLPRFReturnToAppSettingsModel reloadAppSettings]_block_invoke : 212 -> 220
~ ___51-[CSLPRFReturnToAppSettingsModel reloadAppSettings]_block_invoke_2 : 144 -> 140
~ -[CSLPRFReturnToAppSettingsModel init] : 220 -> 224
~ +[CSLPRFReturnToAppSettingsModel returnToAppSettingsToDictionary:] : 212 -> 220
~ ___66+[CSLPRFReturnToAppSettingsModel returnToAppSettingsToDictionary:]_block_invoke : 116 -> 120
~ -[CSLPRFLiveActivitiesAppSettingsCustomization settingsForBundleIdentifier:fromAllSettings:handled:] : 1020 -> 1048
~ -[CSLPRFLiveActivitiesAppSettings setApplication:] : 12 -> 64
~ -[CSLPRFLiveActivitiesAppSettings hash] : 204 -> 208
~ -[CSLPRFLiveActivitiesAppSettings isEqual:] : 700 -> 684
~ -[CSLPRFLiveActivitiesAppSettings description] : 268 -> 276
~ -[CSLPRFLiveActivitiesAppSettings serialize] : 348 -> 368
~ _CSLPRFEqualLiveActivitiesAppSettingsValues : 432 -> 428
~ -[CSLPRFLiveActivitiesAppResolvedSettings autoLaunchBehaviorForApp] : 880 -> 932
~ -[CSLPRFLiveActivitiesAppResolvedSettings allowLiveActivitiesForApp] : 220 -> 212
~ -[CSLPRFLiveActivitiesAppResolvedSettings initWithSettings:globalSettings:] : 152 -> 144
~ -[CSLPRFLiveActivitiesAppSettings autoLaunchBehaviorForApp] : 568 -> 604
~ -[CSLPRFLiveActivitiesAppSettings allowLiveActivitiesForApp] : 480 -> 508
~ -[CSLPRFLiveActivitiesAppSettings globalAutoLaunchLiveActivities] : 276 -> 288
~ -[CSLPRFLiveActivitiesAppSettings globalAllowLiveActivities] : 676 -> 736
~ -[CSLPRFLiveActivitiesAppSettings setDefaultAutoLaunchBehaviorWithBackgroundModes:] : 304 -> 312
~ -[CSLPRFLiveActivitiesAppSettings initForApplication:isGlobalDefault:withSerialization:delegate:] : 652 -> 672
~ ___55+[CSLPRFLiveActivitiesAppSettings _stateDataWithHints:]_block_invoke_2 : 424 -> 432
~ +[CSLPRFLiveActivitiesAppSettings migrateLegacySettings:] : 444 -> 464
~ +[CSLPRFLiveActivitiesAppSettings sharedSettingsModel] : 160 -> 176
~ ___54+[CSLPRFLiveActivitiesAppSettings sharedSettingsModel]_block_invoke : 408 -> 428
~ ___54+[CSLPRFLiveActivitiesAppSettings sharedSettingsModel]_block_invoke_2 : 76 -> 84
~ +[CSLPRFLiveActivitiesAppSettings categoryForApplication:] : 768 -> 800
~ +[CSLPRFLiveActivitiesAppSettings globalSettingsWithSerialization:delegate:] : 188 -> 192
~ +[CSLPRFLiveActivitiesAppSettings settingsForApplication:withSerialization:delegate:] : 136 -> 128
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setAutoLaunchBehaviorForApp:withIgnoredSpecifier:] : 320 -> 328
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) autoLaunchBehaviorForAppWithIgnoredSpecifier:] : 228 -> 236
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setAllowLiveActivitiesForApp:withIgnoredSpecifier:] : 340 -> 344
~ ___98-[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setAllowLiveActivitiesForApp:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) allowLiveActivitiesForAppWithIgnoredSpecifier:] : 268 -> 280
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setGlobalAutoLaunchLiveActivities:withIgnoredSpecifier:] : 340 -> 344
~ ___103-[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setGlobalAutoLaunchLiveActivities:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) globalAutoLaunchLiveActivitiesWithIgnoredSpecifier:] : 268 -> 280
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setGlobalAllowLiveActivities:withIgnoredSpecifier:] : 340 -> 344
~ ___98-[CSLPRFLiveActivitiesAppSettings(PSSpecifier) setGlobalAllowLiveActivities:withIgnoredSpecifier:]_block_invoke : 88 -> 92
~ -[CSLPRFLiveActivitiesAppSettings(PSSpecifier) globalAllowLiveActivitiesWithIgnoredSpecifier:] : 268 -> 280
~ -[NSDictionary(CarouselPreferenceServices) cslprf_boolForKey:withDefaultValue:] : 88 -> 92
~ -[CSLAppSwitcherModeSetting setDelegate:] : 92 -> 96
~ -[CSLAppSwitcherModeSetting setMode:] : 92 -> 96
~ ___33-[CSLAppSwitcherModeSetting mode]_block_invoke : 100 -> 104
~ -[CSLAppSwitcherModeSetting twoWaySyncSettingDidUpdate:] : 92 -> 96
~ -[CSLAppSwitcherModeSetting init] : 208 -> 212
~ -[CSLPRFStingQuickSwitchItem description] : 216 -> 220
~ -[CSLPRFStingQuickSwitchItem isEqual:] : 424 -> 408
~ -[CSLPRFStingQuickSwitchItem hash] : 108 -> 112
~ -[CSLPRFStingQuickSwitchItem copyWithZone:] : 132 -> 140
~ -[CSLPRFStingQuickSwitchItem initWithDelegate:settingsItem:availability:] : 188 -> 192
CStrings:
+ "622B6312-332F-481C-B7DE-7E80973B07BF"
- "622B6312-95FA-4F09-9148-69E286A9C31F"

```
