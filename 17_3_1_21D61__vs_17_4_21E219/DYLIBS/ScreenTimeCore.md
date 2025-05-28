## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-503.2.1.0.0
-  __TEXT.__text: 0x69e50
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x56c0
+503.4.14.0.0
+  __TEXT.__text: 0x6dad0
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x5a80
   __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0x5a6a
-  __TEXT.__oslogstring: 0x57fe
-  __TEXT.__gcc_except_tab: 0x1174
-  __TEXT.__swift5_typeref: 0x162
-  __TEXT.__swift5_capture: 0x48
-  __TEXT.__swift5_fieldmd: 0xa0
+  __TEXT.__cstring: 0x6297
+  __TEXT.__oslogstring: 0x59bf
+  __TEXT.__gcc_except_tab: 0x11f8
+  __TEXT.__swift5_typeref: 0x13c
+  __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__constg_swiftt: 0x90
+  __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift5_reflstr: 0x88
-  __TEXT.__unwind_info: 0x1c40
-  __TEXT.__eh_frame: 0x3c8
-  __TEXT.__objc_classname: 0x1445
-  __TEXT.__objc_methname: 0x11b46
-  __TEXT.__objc_methtype: 0x1d3d
-  __TEXT.__objc_stubs: 0xaf00
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x15a8
-  __DATA_CONST.__objc_classlist: 0x4d0
+  __TEXT.__swift5_reflstr: 0xd2
+  __TEXT.__unwind_info: 0x1b98
+  __TEXT.__eh_frame: 0x280
+  __TEXT.__objc_classname: 0x155b
+  __TEXT.__objc_methname: 0x120b4
+  __TEXT.__objc_methtype: 0x1d54
+  __TEXT.__objc_stubs: 0xb3e0
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x1648
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9da0
-  __DATA_CONST.__objc_selrefs: 0x3938
-  __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0x3d90
+  __DATA_CONST.__objc_const: 0xa0f8
+  __DATA_CONST.__objc_selrefs: 0x3a98
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x6f0
+  __DATA_CONST.__objc_superrefs: 0x350
+  __DATA_CONST.__objc_arraydata: 0x260
+  __AUTH_CONST.__cfstring: 0x7100
+  __AUTH_CONST.__objc_const: 0x40f0
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x678
-  __AUTH.__objc_data: 0x1df8
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x6c8
-  __DATA.__objc_superrefs: 0x320
-  __DATA.__objc_ivar: 0x4cc
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0x2028
+  __DATA.__objc_ivar: 0x4f8
   __DATA.__data: 0xeb8
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x18

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2518
-  Symbols:   8698
-  CStrings:  4382
+  Functions: 2611
+  Symbols:   8966
+  CStrings:  4529
 
Symbols:
+ +[STAMSClient handleLoadMediaTaskForResult:error:withCompletionHandler:]
+ +[STAMSClient loadMediaForTask:withCompletionHandler:]
+ +[STAMSClient makeAMSMediaTaskForApps:isGlobal:]
+ +[STAMSClient makeGlobalQueryParamsFor:]
+ +[STAppAndWebsiteActivityEnabledUserNotificationContext supportsSecureCoding]
+ +[STBlueprint(Restrictions) disableRestrictionsBlueprintForUser:error:]
+ +[STBlueprint(Restrictions) disableRestrictionsBlueprintForUser:error:].cold.1
+ +[STBlueprint(Restrictions) disableRestrictionsBlueprintForUser:error:].cold.2
+ +[STBlueprint(Restrictions) disableRestrictionsBlueprintForUser:error:].cold.3
+ +[STBlueprint(Restrictions) disableRestrictionsBlueprintForUser:error:].cold.4
+ +[STCoreDevice fetchDeviceWithCoreDuetIdentifier:inContext:error:]
+ +[STCoreDevice fetchDeviceWithCoreDuetIdentifier:inContext:error:].cold.1
+ +[STDeviceActivityDataSourceInterface allLocallyUsedBundleIdentifiers]
+ +[STDeviceActivityDataSourceInterface downloadRemoteData]
+ +[STDeviceActivityDataSourceInterface lastUpdatedDateFor:]
+ +[STDeviceActivityDataSourceInterface refreshAndUploadLocalDataSinceDate:completionHandler:]
+ +[STDeviceActivityDataSourceInterface totalWeeklyUsageDuringDateInterval:userAltDSID:error:]
+ +[STInstalledApp bundleIdentifiersInstalledForAltDSID:inContext:error:]
+ +[STInstalledApp bundleIdentifiersInstalledForPredicate:inContext:error:]
+ +[STLocationServicesLockedUserNotificationContext supportsSecureCoding]
+ +[STLocationServicesUnlockedUserNotificationContext supportsSecureCoding]
+ +[STLog familyMessaging]
+ +[STLog v2Disable]
+ +[STShareMyLocationLockedUserNotificationContext supportsSecureCoding]
+ +[STShareMyLocationUnlockedUserNotificationContext supportsSecureCoding]
+ -[STAppAndWebsiteActivityEnabledUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STAppAndWebsiteActivityEnabledUserNotificationContext initWithCoder:]
+ -[STAppAndWebsiteActivityEnabledUserNotificationContext init]
+ -[STAppAndWebsiteActivityEnabledUserNotificationContext notificationBundleIdentifier]
+ -[STAppInfo adamID]
+ -[STAppInfo betaVersionIdentifier]
+ -[STAppInfo distributorID]
+ -[STAppInfo distributorIsThirdParty]
+ -[STAppInfo setAdamID:]
+ -[STAppInfo setBetaVersionIdentifier:]
+ -[STAppInfo setDistributorID:]
+ -[STAppInfo setDistributorIsThirdParty:]
+ -[STAppInfo setVersionIdentifier:]
+ -[STAppInfo versionIdentifier]
+ -[STAppInfoCache _handleAMSClientResponseForBundleIdentifiers:results:error:completionHandler:]
+ -[STAppInfoCache _handleAMSClientResponseForBundleIdentifiers:results:error:completionHandler:].cold.1
+ -[STAppMetadata .cxx_destruct]
+ -[STAppMetadata artworkURL]
+ -[STAppMetadata bundleIdentifier]
+ -[STAppMetadata copyWithZone:]
+ -[STAppMetadata displayName]
+ -[STAppMetadata initWithBundleIdentifier:displayName:artworkURL:vendorName:ratingLabel:software:]
+ -[STAppMetadata ratingLabel]
+ -[STAppMetadata setArtworkURL:]
+ -[STAppMetadata setBundleIdentifier:]
+ -[STAppMetadata setDisplayName:]
+ -[STAppMetadata setRatingLabel:]
+ -[STAppMetadata setSoftware:]
+ -[STAppMetadata setVendorName:]
+ -[STAppMetadata software]
+ -[STAppMetadata vendorName]
+ -[STLocationServicesLockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STLocationServicesLockedUserNotificationContext initWithCoder:]
+ -[STLocationServicesLockedUserNotificationContext init]
+ -[STLocationServicesLockedUserNotificationContext notificationBundleIdentifier]
+ -[STLocationServicesUnlockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STLocationServicesUnlockedUserNotificationContext initWithCoder:]
+ -[STLocationServicesUnlockedUserNotificationContext init]
+ -[STLocationServicesUnlockedUserNotificationContext notificationBundleIdentifier]
+ -[STShareMyLocationLockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STShareMyLocationLockedUserNotificationContext initWithCoder:]
+ -[STShareMyLocationLockedUserNotificationContext init]
+ -[STShareMyLocationLockedUserNotificationContext notificationBundleIdentifier]
+ -[STShareMyLocationUnlockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]
+ -[STShareMyLocationUnlockedUserNotificationContext initWithCoder:]
+ -[STShareMyLocationUnlockedUserNotificationContext init]
+ -[STShareMyLocationUnlockedUserNotificationContext notificationBundleIdentifier]
+ -[STWeeklyReportUserNotificationContext setDeltaScreenTimeUsage:totalUsage:]
+ -[STWeeklyReportUserNotificationContext setTotalUsage:]
+ -[STWeeklyReportUserNotificationContext totalUsage]
+ GCC_except_table58
+ GCC_except_table61
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMediaArtwork
+ _OBJC_CLASS_$_AMSMediaTask
+ _OBJC_CLASS_$_STAMSClient
+ _OBJC_CLASS_$_STAppAndWebsiteActivityEnabledUserNotificationContext
+ _OBJC_CLASS_$_STAppMetadata
+ _OBJC_CLASS_$_STLocationServicesLockedUserNotificationContext
+ _OBJC_CLASS_$_STLocationServicesUnlockedUserNotificationContext
+ _OBJC_CLASS_$_STShareMyLocationLockedUserNotificationContext
+ _OBJC_CLASS_$_STShareMyLocationUnlockedUserNotificationContext
+ _OBJC_IVAR_$_STAppInfo._adamID
+ _OBJC_IVAR_$_STAppInfo._betaVersionIdentifier
+ _OBJC_IVAR_$_STAppInfo._distributorID
+ _OBJC_IVAR_$_STAppInfo._distributorIsThirdParty
+ _OBJC_IVAR_$_STAppInfo._versionIdentifier
+ _OBJC_IVAR_$_STAppMetadata._artworkURL
+ _OBJC_IVAR_$_STAppMetadata._bundleIdentifier
+ _OBJC_IVAR_$_STAppMetadata._displayName
+ _OBJC_IVAR_$_STAppMetadata._ratingLabel
+ _OBJC_IVAR_$_STAppMetadata._software
+ _OBJC_IVAR_$_STAppMetadata._vendorName
+ _OBJC_IVAR_$_STWeeklyReportUserNotificationContext._totalUsage
+ _OBJC_METACLASS_$_STAMSClient
+ _OBJC_METACLASS_$_STAppAndWebsiteActivityEnabledUserNotificationContext
+ _OBJC_METACLASS_$_STAppMetadata
+ _OBJC_METACLASS_$_STLocationServicesLockedUserNotificationContext
+ _OBJC_METACLASS_$_STLocationServicesUnlockedUserNotificationContext
+ _OBJC_METACLASS_$_STShareMyLocationLockedUserNotificationContext
+ _OBJC_METACLASS_$_STShareMyLocationUnlockedUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STAMSClient
+ __OBJC_$_CLASS_METHODS_STAppAndWebsiteActivityEnabledUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STLocationServicesLockedUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STLocationServicesUnlockedUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STShareMyLocationLockedUserNotificationContext
+ __OBJC_$_CLASS_METHODS_STShareMyLocationUnlockedUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STAppAndWebsiteActivityEnabledUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STAppMetadata
+ __OBJC_$_INSTANCE_METHODS_STLocationServicesLockedUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STLocationServicesUnlockedUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STShareMyLocationLockedUserNotificationContext
+ __OBJC_$_INSTANCE_METHODS_STShareMyLocationUnlockedUserNotificationContext
+ __OBJC_$_INSTANCE_VARIABLES_STAppMetadata
+ __OBJC_$_PROP_LIST_STAppMetadata
+ __OBJC_CLASS_PROTOCOLS_$_STAppMetadata
+ __OBJC_CLASS_RO_$_STAMSClient
+ __OBJC_CLASS_RO_$_STAppAndWebsiteActivityEnabledUserNotificationContext
+ __OBJC_CLASS_RO_$_STAppMetadata
+ __OBJC_CLASS_RO_$_STLocationServicesLockedUserNotificationContext
+ __OBJC_CLASS_RO_$_STLocationServicesUnlockedUserNotificationContext
+ __OBJC_CLASS_RO_$_STShareMyLocationLockedUserNotificationContext
+ __OBJC_CLASS_RO_$_STShareMyLocationUnlockedUserNotificationContext
+ __OBJC_METACLASS_RO_$_STAMSClient
+ __OBJC_METACLASS_RO_$_STAppAndWebsiteActivityEnabledUserNotificationContext
+ __OBJC_METACLASS_RO_$_STAppMetadata
+ __OBJC_METACLASS_RO_$_STLocationServicesLockedUserNotificationContext
+ __OBJC_METACLASS_RO_$_STLocationServicesUnlockedUserNotificationContext
+ __OBJC_METACLASS_RO_$_STShareMyLocationLockedUserNotificationContext
+ __OBJC_METACLASS_RO_$_STShareMyLocationUnlockedUserNotificationContext
+ ___100-[STLocationServicesLockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___101-[STAppInfoCache _fetchAppStoreInfoAndNotifyWithBundleIdentifiers:timeoutInterval:completionHandler:]_block_invoke_2
+ ___101-[STAppInfoCache _fetchAppStoreInfoAndNotifyWithBundleIdentifiers:timeoutInterval:completionHandler:]_block_invoke_3
+ ___101-[STAppInfoCache _fetchAppStoreInfoAndNotifyWithBundleIdentifiers:timeoutInterval:completionHandler:]_block_invoke_4
+ ___101-[STAppInfoCache _fetchAppStoreInfoAndNotifyWithBundleIdentifiers:timeoutInterval:completionHandler:]_block_invoke_5
+ ___101-[STShareMyLocationUnlockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___102-[STLocationServicesUnlockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___106-[STAppAndWebsiteActivityEnabledUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___54+[STAMSClient loadMediaForTask:withCompletionHandler:]_block_invoke
+ ___54+[STAMSClient loadMediaForTask:withCompletionHandler:]_block_invoke_2
+ ___66-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke.216
+ ___95-[STAppInfoCache _handleAMSClientResponseForBundleIdentifiers:results:error:completionHandler:]_block_invoke
+ ___99-[STShareMyLocationLockedUserNotificationContext customizeNotificationContent:withCompletionBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v28?0"NSNumber"8B16"NSError"20ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e29_v24?0"NSError"8"NSArray"16ls32l8w56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.221
+ __swift_stdlib_bridgeErrorToNSError
+ __unnamed_array_storage.84
+ __unnamed_array_storage.85
+ __unnamed_array_storage.88
+ __unnamed_array_storage.89
+ _bzero
+ _objc_msgSend$URLWithSize:
+ _objc_msgSend$_handleAMSClientResponseForBundleIdentifiers:results:error:completionHandler:
+ _objc_msgSend$adamID
+ _objc_msgSend$addFinishBlock:
+ _objc_msgSend$allLocallyUsedBundleIdentifiers
+ _objc_msgSend$ams_activeiTunesAccount
+ _objc_msgSend$ams_sharedAccountStore
+ _objc_msgSend$artworkURL
+ _objc_msgSend$bag
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$betaVersionIdentifier
+ _objc_msgSend$bundleIdentifiersInstalledForPredicate:inContext:error:
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$distributorIsThirdParty
+ _objc_msgSend$downloadRemoteData
+ _objc_msgSend$handleLoadMediaTaskForResult:error:withCompletionHandler:
+ _objc_msgSend$initWithBundleIdentifier:displayName:artworkURL:vendorName:ratingLabel:software:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
+ _objc_msgSend$lastUpdatedDateFor:
+ _objc_msgSend$loadMediaForTask:withCompletionHandler:
+ _objc_msgSend$makeAMSMediaTaskForApps:isGlobal:
+ _objc_msgSend$makeGlobalQueryParamsFor:
+ _objc_msgSend$perform
+ _objc_msgSend$refreshAndUploadLocalDataSinceDate:completionHandler:
+ _objc_msgSend$responseDataItems
+ _objc_msgSend$setAccount:
+ _objc_msgSend$setAdamID:
+ _objc_msgSend$setAdditionalQueryParams:
+ _objc_msgSend$setBetaVersionIdentifier:
+ _objc_msgSend$setDistributorID:
+ _objc_msgSend$setDistributorIsThirdParty:
+ _objc_msgSend$setTotalUsage:
+ _objc_msgSend$setVersionIdentifier:
+ _objc_msgSend$software
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$totalWeeklyUsageDuringDateInterval:userAltDSID:error:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$valueWithCompletion:
+ _objc_msgSend$vendorName
+ _objc_msgSend$versionIdentifier
+ _objc_retain_x7
+ _swift_release_n
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectCSg
+ _symbolic _____Sg 14DeviceActivity0aB6FilterV7DevicesV
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____y_____G 14DeviceActivity01_aB7ResultsV AA01_aB4DataV0B7SegmentV
- +[STDeviceActivityDataSourceInterface weeklyNotificationPayloadUsingCoreDuetIdentifiers:userAltDSID:completionHandler:]
- -[STWeeklyReportUserNotificationContext setDeltaScreenTimeUsage:totalOrAverageUsage:isLegacyOS:]
- -[STWeeklyReportUserNotificationContext setTotalOrAverageUsage:]
- -[STWeeklyReportUserNotificationContext totalOrAverageUsage]
- GCC_except_table38
- GCC_except_table42
- _OBJC_IVAR_$_STWeeklyReportUserNotificationContext._totalOrAverageUsage
- ___66-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke.180
- ___block_literal_global.185
- __unnamed_array_storage.80
- __unnamed_array_storage.83
- __unnamed_array_storage.86
- __unnamed_array_storage.87
- _objc_msgSend$longValue
- _objc_msgSend$setTotalOrAverageUsage:
- _objc_msgSend$weeklyNotificationPayloadWithCoreDuetIdentifiers:userAltDSID:completionHandler:
- _swift_bridgeObjectRetain_n
- _swift_getObjCClassMetadata
- _symbolic SSSg
- _symbolic So8NSNumberCSgACSo7NSErrorCSgIeyByyy_
- _symbolic So8NSNumberCSgAC______pSgIegggg_ s5ErrorP
- _symbolic _____ 10Foundation12DateIntervalV
- _symbolic _____Sg 10Foundation8CalendarV
- _symbolic _____Sg 10Foundation8TimeZoneV
- _symbolic _____XDXMT 14ScreenTimeCore26STDeviceActivityDataSourceC
- _symbolic _____XMT 14ScreenTimeCore26STDeviceActivityDataSourceC
CStrings:
+ "\"\x11%"
+ "%llu"
+ "@64@0:8@16@24@32@40@48@56"
+ "AMSMediaTask requested for an empty array of STAppInfos. Returning nil"
+ "App lookup of %@ from media services failed: %{public}@"
+ "AppAndWebsiteActivityEnabledUserNotificationBody"
+ "AppAndWebsiteActivityEnabledUserNotificationTitle"
+ "AppInfo from unknown source or missing an adamID. Reverting to iTunes lookup. BundleIdentifier: %@"
+ "AppInfo not found for bundleIdentifier: %@"
+ "Disabling restrictions blueprint."
+ "Division by zero"
+ "Division results in an overflow"
+ "Error parsing response item: %@"
+ "Failed to fetch all locally used bundle identifiers: %{public}s"
+ "Failed to fetch last updated date frome data source: %{public}@"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "LocationServicesLockedUserNotificationBody"
+ "LocationServicesLockedUserNotificationTitle"
+ "LocationServicesUnlockedUserNotificationBody"
+ "LocationServicesUnlockedUserNotificationTitle"
+ "STAMSClient"
+ "STAppAndWebsiteActivityEnabledUserNotificationContext"
+ "STAppMetadata"
+ "STLocationServicesLockedUserNotificationContext"
+ "STLocationServicesUnlockedUserNotificationContext"
+ "STShareMyLocationLockedUserNotificationContext"
+ "STShareMyLocationUnlockedUserNotificationContext"
+ "ShareMyLocationLockedUserNotificationBody"
+ "ShareMyLocationLockedUserNotificationTitle"
+ "ShareMyLocationUnlockedUserNotificationBody"
+ "ShareMyLocationUnlockedUserNotificationTitle"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSArray\",N,R"
+ "T@\"NSNumber\",C,N,V_totalUsage"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_distributorID"
+ "T@\"NSString\",C,N,V_software"
+ "T@\"NSString\",C,N,V_vendorName"
+ "TB,N,V_distributorIsThirdParty"
+ "TQ,N,V_adamID"
+ "TQ,N,V_betaVersionIdentifier"
+ "TQ,N,V_versionIdentifier"
+ "URLWithSize:"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_adamID"
+ "_betaVersionIdentifier"
+ "_distributorID"
+ "_distributorIsThirdParty"
+ "_handleAMSClientResponseForBundleIdentifiers:results:error:completionHandler:"
+ "_software"
+ "_totalUsage"
+ "_vendorName"
+ "_versionIdentifier"
+ "adamID"
+ "addFinishBlock:"
+ "additionalVersions"
+ "allLocallyUsedBundleIdentifiers"
+ "ams_activeiTunesAccount"
+ "ams_app_metadata_api"
+ "ams_sharedAccountStore"
+ "appDistribution"
+ "app_and_website_activity_enabled"
+ "appsApple"
+ "artwork"
+ "attributes"
+ "bag"
+ "bagForProfile:profileVersion:"
+ "betaVersionIdentifier"
+ "bundleIdentifiersInstalledForAltDSID:inContext:error:"
+ "bundleIdentifiersInstalledForPredicate:inContext:error:"
+ "com.apple.ScreenTimeSettingsUI"
+ "contentRatingsBySystem"
+ "device identifier is not unique but it should be:\n%{public}@"
+ "disableRestrictionsBlueprintForUser:error:"
+ "distributorID"
+ "distributorInfo"
+ "distributorIsThirdParty"
+ "downloadRemoteData"
+ "enable-app-distribution-account-personalization"
+ "extend"
+ "failed to disable restrictions blueprint: %{public}@"
+ "familyMessaging"
+ "fetchDeviceWithCoreDuetIdentifier:inContext:error:"
+ "handleLoadMediaTaskForResult:error:withCompletionHandler:"
+ "initWithBundleIdentifier:displayName:artworkURL:vendorName:ratingLabel:software:"
+ "initWithDictionary:"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "invalid Collection: less than 'count' elements in collection"
+ "ios"
+ "lastUpdatedDateFor:"
+ "loadMediaForTask:withCompletionHandler:"
+ "location_services_locked"
+ "location_services_unlocked"
+ "macSoftware"
+ "macos"
+ "makeAMSMediaTaskForApps:isGlobal:"
+ "makeGlobalQueryParamsFor:"
+ "new_usage_swiftui"
+ "perform"
+ "platformAttributes"
+ "refreshAndUploadLocalDataSinceDate:completionHandler:"
+ "responseDataItems"
+ "seller"
+ "setAccount:"
+ "setAdamID:"
+ "setAdditionalQueryParams:"
+ "setBetaVersionIdentifier:"
+ "setDeltaScreenTimeUsage:totalUsage:"
+ "setDistributorID:"
+ "setDistributorIsThirdParty:"
+ "setSoftware:"
+ "setTotalUsage:"
+ "setVendorName:"
+ "setVersionIdentifier:"
+ "share_my_location_locked"
+ "share_my_location_unlocked"
+ "shortName"
+ "shortName,allowedDistributorIds"
+ "storeItemIdentifier"
+ "totalUsage"
+ "totalWeeklyUsageDuringDateInterval:userAltDSID:error:"
+ "transparency"
+ "unsignedLongValue"
+ "userDeviceState.user.altDSID"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
+ "v2Disable"
+ "v32@0:8d16@24"
+ "valueWithCompletion:"
+ "vendorName"
+ "versionIdentifier"
+ "version[apps:%llu]"
+ "with"
- "DeviceActivity data not available for requested device: %{public}s"
- "Failed to fetch activity segment with record name: %{public}s"
- "T@\"NSNumber\",C,N,V_totalOrAverageUsage"
- "_totalOrAverageUsage"
- "longValue"
- "setDeltaScreenTimeUsage:totalOrAverageUsage:isLegacyOS:"
- "setTotalOrAverageUsage:"
- "totalOrAverageUsage"
- "v36@0:8d16@24B32"
- "weeklyNotificationPayloadUsingCoreDuetIdentifiers:userAltDSID:completionHandler:"
- "weeklyNotificationPayloadWithCoreDuetIdentifiers:userAltDSID:completionHandler:"

```
