## SettingsCellular

> `/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular`

```diff

-659.1.0.0.0
-  __TEXT.__text: 0xa4ec
-  __TEXT.__auth_stubs: 0x520
+678.0.0.0.0
+  __TEXT.__text: 0xaf94
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_methlist: 0xdbc
   __TEXT.__const: 0xa8
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__cstring: 0x73a
   __TEXT.__oslogstring: 0x95c
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_classname: 0x27c
   __TEXT.__objc_methname: 0x2757
   __TEXT.__objc_methtype: 0x8f5

   __DATA_CONST.__objc_selrefs: 0xb68
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x640
   __AUTH_CONST.__objc_const: 0x13b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B49F74DB-7CAC-3319-8616-63BAF349B6C2
+  UUID: F718681D-18DA-37ED-B621-A2E90C65D242
   Functions: 237
-  Symbols:   1091
+  Symbols:   1088
   CStrings:  733
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x26
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[PSCellularManagementCache sharedInstance] : 84 -> 100
~ -[PSCellularManagementCache initPrivate] : 256 -> 268
~ -[PSCellularManagementCache init] : 168 -> 172
~ -[PSCellularManagementCache clearCache] : 120 -> 124
~ -[PSCellularManagementCache willEnterForeground] : 116 -> 120
~ -[PSCellularManagementCache managedConfigurationSettingsDidChange] : 116 -> 120
~ -[PSCellularManagementCache managedConfigurationProfileListDidChange] : 116 -> 120
~ -[PSCellularManagementCache isGlobalDataModificationRestricted] : 80 -> 84
~ -[PSCellularManagementCache mdmName] : 152 -> 172
~ -[PSCellularManagementCache managedAppBundleIDs] : 84 -> 92
~ -[PSCellularManagementCache managedCellDataAppBundleIDs] : 412 -> 432
~ -[PSCellularManagementCache hasManagedCellularData] : 60 -> 64
~ -[PSCellularManagementCache isManaged:] : 260 -> 268
~ -[PSAppDataUsagePolicyListController specifiers] : 516 -> 560
~ -[PSAppDataUsagePolicyListController _adjustTitle] : 128 -> 132
~ +[PSDataUsageStatisticsCache sharedInstance] : 84 -> 100
~ -[PSDataUsageStatisticsCache initPrivate] : 128 -> 132
~ -[PSDataUsageStatisticsCache initWithCoreTelephonyClient:] : 192 -> 196
~ -[PSDataUsageStatisticsCache init] : 132 -> 136
~ -[PSDataUsageStatisticsCache dealloc] : 100 -> 104
~ -[PSDataUsageStatisticsCache willEnterForeground] : 116 -> 120
~ -[PSDataUsageStatisticsCache _clearCache] : 200 -> 204
~ -[PSDataUsageStatisticsCache fetchDeviceDataUsage] : 368 -> 380
~ ___50-[PSDataUsageStatisticsCache fetchDeviceDataUsage]_block_invoke : 652 -> 676
~ -[PSDataUsageStatisticsCache fetchHotspotClientsUsage] : 348 -> 360
~ -[PSDataUsageStatisticsCache bundleIDsForAppType:] : 768 -> 836
~ -[PSDataUsageStatisticsCache displayNamesForBundleIDs:appType:] : 900 -> 964
~ -[PSDataUsageStatisticsCache totalWatchOnlyAppUsageForPeriod:] : 96 -> 104
~ -[PSDataUsageStatisticsCache totalSystemServicesUsageForPeriod:] : 96 -> 104
~ -[PSDataUsageStatisticsCache totalUninstalledAppUsageForPeriod:] : 96 -> 104
~ -[PSDataUsageStatisticsCache hotspotClientIDsForPeriod:] : 840 -> 888
~ -[PSDataUsageStatisticsCache displayNameForHotspotClientID:] : 720 -> 760
~ -[PSDataUsageStatisticsCache totalHotspotClientUsageForPeriod:] : 228 -> 248
~ -[PSDataUsageStatisticsCache usageForHotspotClientID:inPeriod:] : 892 -> 936
~ -[PSDataUsageStatisticsCache totalHiddenAppUsageForPeriod:] : 96 -> 104
~ -[PSDataUsageStatisticsCache usageForBundleID:inPeriod:] : 1368 -> 1452
~ -[PSDataUsageStatisticsCache wifiAssistUsageForPeriod:] : 96 -> 104
~ -[PSDataUsageStatisticsCache totalCellularUsageForPeriod:] : 220 -> 244
~ -[PSDataUsageStatisticsCache totalRoamingUsageForPeriod:] : 156 -> 172
~ -[PSDataUsageStatisticsCache totalSatelliteUsageForPeriod:] : 156 -> 172
~ -[PSDataUsageStatisticsCache fetchWorkspaceInfo] : 360 -> 368
~ -[PSDataUsageStatisticsCache billingCycleSupported] : 160 -> 172
~ -[PSDataUsageStatisticsCache useCalendarMonthBillingCycle] : 220 -> 240
~ -[PSDataUsageStatisticsCache billingCycleEndDate] : 164 -> 176
~ -[PSDataUsageStatisticsCache previousBillingCycleEndDate] : 164 -> 176
~ -[PSDataUsageStatisticsCache _handleUsageOrInfoChanged] : 284 -> 296
~ -[PSDataUsageStatisticsCache refreshDataUsageUINotification] : 196 -> 200
~ -[PSDataUsageStatisticsCache dataRatesChanged] : 116 -> 120
~ -[PSDataUsageStatisticsCache setClient:] : 12 -> 64
~ +[PSSimStatusCache sharedInstance] : 84 -> 100
~ -[PSSimStatusCache initPrivate] : 128 -> 132
~ -[PSSimStatusCache initWithCoreTelephonyClient:] : 256 -> 260
~ -[PSSimStatusCache clearSubscriptionInfoAndSimStatusCache] : 148 -> 152
~ -[PSSimStatusCache clearSubscriptionContextCache] : 148 -> 152
~ -[PSSimStatusCache clearSimHardwareInfoCache] : 136 -> 140
~ -[PSSimStatusCache willEnterForeground] : 164 -> 168
~ -[PSSimStatusCache fetchSubscriptionContextsHasCacheLock:] : 420 -> 428
~ -[PSSimStatusCache fetchActiveDataSubscriptionContextIfNeeded] : 516 -> 532
~ -[PSSimStatusCache fetchDefaultVoiceSubscriptionContextIfNeeded] : 516 -> 532
~ -[PSSimStatusCache subscriptionContextsHasCacheLock:] : 156 -> 168
~ -[PSSimStatusCache subscriptionsInUse] : 144 -> 156
~ -[PSSimStatusCache subscriptionInfoDidChange] : 120 -> 124
~ -[PSSimStatusCache defaultVoiceSubscriptionContext] : 88 -> 92
~ -[PSSimStatusCache activeDataSubscriptionContext] : 88 -> 92
~ -[PSSimStatusCache isSlotActiveDataSlot:] : 100 -> 104
~ -[PSSimStatusCache fetchSimStatusHasCacheLock:] : 696 -> 712
~ -[PSSimStatusCache simStatus:] : 188 -> 200
~ -[PSSimStatusCache fetchSimHardwareInfoHasCacheLock:] : 736 -> 756
~ -[PSSimStatusCache simHardwareInfo:] : 204 -> 216
~ -[PSSimStatusCache isDualSimCapable] : 64 -> 68
~ -[PSSimStatusCache updateIsAnySimPresent] : 620 -> 644
~ -[PSSimStatusCache simStatusDidChange:status:] : 456 -> 468
~ -[PSSimStatusCache preferredDataSimChanged:] : 116 -> 120
~ -[PSSimStatusCache currentDataSimChanged:] : 116 -> 120
~ -[PSSimStatusCache setCoreTelephonyClient:] : 12 -> 64
~ -[PSBillingPeriodSelectorSpecifier refreshSelectorWithStatisticsCache:] : 852 -> 848
~ -[PSBillingPeriodSelectorSpecifier setBillingPeriod:specifier:] : 316 -> 328
~ -[PSAppDataUsagePolicySwitchSpecifier initWithBundleID:displayName:statisticsCache:] : 180 -> 176
~ -[PSAppDataUsagePolicySwitchSpecifier usagePolicy] : 352 -> 376
~ -[PSAppDataUsagePolicySwitchSpecifier setUsagePolicy:] : 424 -> 448
~ ___54-[PSAppDataUsagePolicySwitchSpecifier setUsagePolicy:]_block_invoke : 204 -> 212
~ +[PSAppCellularUsageSpecifier _specifierWithDisplayName:appName:bundleID:shouldShowUsage:icon:statisticsCache:usageType:] : 348 -> 340
~ +[PSAppCellularUsageSpecifier appSpecifierWithBundleID:name:statisticsCache:usageType:] : 164 -> 168
~ +[PSAppCellularUsageSpecifier setIconForSpecifier:bundleID:] : 368 -> 388
~ +[PSAppCellularUsageSpecifier systemPolicySpecifierForAppName:bundleID:icon:] : 352 -> 368
~ -[PSAppCellularUsageSpecifier dataUsage] : 328 -> 360
~ -[PSAppCellularUsageSpecifier dataUsageString] : 480 -> 520
~ -[PSAppCellularUsageSpecifier usagePolicy] : 56 -> 60
~ -[PSAppCellularUsageSpecifier setUsagePolicy:] : 60 -> 64
~ -[PSAppCellularUsageSpecifier isRestricted] : 168 -> 184
~ -[PSAppCellularUsageSpecifier setBundleID:] : 20 -> 80
~ -[PSAppCellularUsageSpecifier setStatisticsCache:] : 20 -> 80
~ +[PSWatchOnlyAppCellularUsageSpecifier setIconForSpecifier:bundleID:] : 548 -> 552
~ ___69+[PSWatchOnlyAppCellularUsageSpecifier setIconForSpecifier:bundleID:]_block_invoke : 168 -> 188
~ +[PSWatchOnlyAppCellularUsageSpecifier getGenericRoundIcon] : 84 -> 100
~ ___59+[PSWatchOnlyAppCellularUsageSpecifier getGenericRoundIcon]_block_invoke : 532 -> 544
~ -[PSMultilineTitleTableCell initWithStyle:reuseIdentifier:] : 1640 -> 1920
~ -[PSMultilineTitleTableCell layoutSubviews] : 628 -> 700
~ -[PSMultilineTitleTableCell setValueTrailingCon:] : 20 -> 80
~ -[PSMultilineTitleTableCell setTitleLeadingCon:] : 20 -> 80
~ -[PSDataUsageSpecifier initWithAppType:bundleID:name:statisticsCache:usageType:] : 536 -> 540
~ -[PSDataUsageSpecifier dataUsage] : 388 -> 416
~ -[PSDataUsageSpecifier dataUsageString] : 448 -> 480
~ -[PSDataUsageSpecifier setStatisticsCache:] : 20 -> 80
~ -[PSDataUsageSpecifier setBundleID:] : 20 -> 80
~ -[PSAppDataUsagePolicyTernaryControlSpecifier initWithBundleID:displayName:appName:statisticsCache:] : 328 -> 316
~ -[PSAppDataUsagePolicyTernaryControlSpecifier finishInitializing:] : 1412 -> 1556
~ -[PSAppDataUsagePolicyTernaryControlSpecifier cellularUsagePolicy] : 380 -> 404
~ -[PSAppDataUsagePolicyTernaryControlSpecifier setCellularUsagePolicy:] : 308 -> 328
~ ___70-[PSAppDataUsagePolicyTernaryControlSpecifier setCellularUsagePolicy:]_block_invoke : 92 -> 96
~ -[PSAppDataUsagePolicyTernaryControlSpecifier setDisplayName:] : 20 -> 80
~ -[PSAppDataUsagePolicyTernaryControlSpecifier setAppName:] : 20 -> 80
~ +[SettingsCellularSharedUtils sharedCTClientWorkloop] : 84 -> 100
~ +[SettingsCellularSharedUtils createCTClientSerialQueue:] : 184 -> 196
~ +[SettingsCellularSharedUtils logSpecifiers:origin:] : 524 -> 532
~ +[PSAppDataUsagePolicyCache sharedInstance] : 84 -> 100
~ -[PSAppDataUsagePolicyCache initPrivate] : 716 -> 736
~ -[PSAppDataUsagePolicyCache clearCache] : 116 -> 120
~ -[PSAppDataUsagePolicyCache handlePolicyChangedNotification] : 380 -> 396
~ -[PSAppDataUsagePolicyCache willEnterForeground] : 116 -> 120
~ -[PSAppDataUsagePolicyCache managedConfigurationSettingsDidChange] : 116 -> 120
~ -[PSAppDataUsagePolicyCache managedConfigurationProfileListDidChange] : 116 -> 120
~ -[PSAppDataUsagePolicyCache init] : 168 -> 172
~ ___48-[PSAppDataUsagePolicyCache addPoliciesToCache:]_block_invoke : 180 -> 188
~ -[PSAppDataUsagePolicyCache fetchUsagePoliciesFor:] : 428 -> 432
~ -[PSAppDataUsagePolicyCache fetchUsagePolicyFor:] : 476 -> 488
~ -[PSAppDataUsagePolicyCache policiesFor:] : 352 -> 368
~ -[PSAppDataUsagePolicyCache setPolicies:completion:] : 456 -> 464
~ ___52-[PSAppDataUsagePolicyCache setPolicies:completion:]_block_invoke : 480 -> 504
~ -[PSAppDataUsagePolicyCache setPolicyCache:] : 12 -> 64
~ -[PSAppDataUsagePolicyCache setCtClient:] : 12 -> 64

```
