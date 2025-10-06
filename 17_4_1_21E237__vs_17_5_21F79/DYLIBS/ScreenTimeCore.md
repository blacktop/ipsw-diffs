## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-503.4.14.0.0
-  __TEXT.__text: 0x6dad0
+503.5.12.3.0
+  __TEXT.__text: 0x6f7f0
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x5a80
+  __TEXT.__objc_methlist: 0x5ac0
   __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0x6297
-  __TEXT.__oslogstring: 0x59bf
-  __TEXT.__gcc_except_tab: 0x11f8
+  __TEXT.__cstring: 0x6457
+  __TEXT.__oslogstring: 0x63e6
+  __TEXT.__gcc_except_tab: 0x12a0
   __TEXT.__swift5_typeref: 0x13c
   __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__constg_swiftt: 0x90

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0xd2
-  __TEXT.__unwind_info: 0x1b98
+  __TEXT.__unwind_info: 0x1b90
   __TEXT.__eh_frame: 0x280
   __TEXT.__objc_classname: 0x155b
-  __TEXT.__objc_methname: 0x120b4
-  __TEXT.__objc_methtype: 0x1d54
-  __TEXT.__objc_stubs: 0xb3e0
+  __TEXT.__objc_methname: 0x12178
+  __TEXT.__objc_methtype: 0x1d7a
+  __TEXT.__objc_stubs: 0xb4e0
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0x1648
   __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa0f8
-  __DATA_CONST.__objc_selrefs: 0x3a98
+  __DATA_CONST.__objc_const: 0xa128
+  __DATA_CONST.__objc_selrefs: 0x3ad8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_classrefs: 0x6f0
+  __DATA_CONST.__objc_classrefs: 0x6f8
   __DATA_CONST.__objc_superrefs: 0x350
-  __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__cfstring: 0x7100
+  __DATA_CONST.__objc_arraydata: 0x250
+  __AUTH_CONST.__cfstring: 0x7220
   __AUTH_CONST.__objc_const: 0x40f0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0x2028
   __DATA.__objc_ivar: 0x4f8

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
+  - /System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1DEE41B2-7CB6-3A94-954E-ED17CEF300F2
-  Functions: 2611
-  Symbols:   8966
-  CStrings:  5433
+  UUID: 882CF138-22F4-3DBF-A574-4219ED619EDC
+  Functions: 2638
+  Symbols:   9031
+  CStrings:  5499
 
Symbols:
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:]
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.1
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.2
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.3
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.4
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.5
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.6
+ +[STAMSClient _handleLoadMediaTaskForResult:error:withCompletionHandler:].cold.7
+ +[STAMSClient _makeGlobalQueryParamsFor:]
+ +[STCoreDevice fetchRequestForDevicesMissingUsage]
+ +[STCoreDevice fetchRequestForNonLocalDevices]
+ +[STUnique addHistoryToken:toMetadataForStore:error:]
+ +[STUnique historyTokenFromStore:]
+ +[STUnique historyTokenFromStore:].cold.1
+ +[STUserDeviceState _getCoreDuetIdentifier]
+ +[STUserDeviceState _getCoreDuetIdentifier].cold.1
+ -[STAppInfoCache _appInfoForBundleIdentifier:].cold.1
+ -[STAppInfoCache _appInfoForBundleIdentifier:].cold.2
+ -[STCoreUser systemFullUserName]
+ -[STFamilyOrganizationSettings updateWithDictionaryRepresentation:].cold.7
+ -[STHistoryAnalyzer deltasForStore:inManagedObjectContext:sinceToken:ignoreAuthor:finalToken:error:].cold.5
+ -[STInstalledApp description]
+ -[STInstalledApp updateWithDictionaryRepresentation:].cold.1
+ -[STManagementState postNotificationForContext:]
+ -[STUnique addHistoryToken:toMetadataForStore:error:]
+ -[STUnique historyTokenFromStore:]
+ -[STUserDeviceState dictionaryRepresentation].cold.1
+ -[STUserDeviceState dictionaryRepresentation].cold.2
+ _OBJC_CLASS_$_USUsageReporter
+ ___104+[STBlueprint(UsageLimit) displayNameForUsageLimitWithCategoryIdentifiers:bundleIdentifiers:webDomains:]_block_invoke.63
+ ___54+[STAMSClient loadMediaForTask:withCompletionHandler:]_block_invoke.32
+ ___66-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke.cold.2
+ ___block_descriptor_56_e8_32r40r48r_e31_B32?0"STInstalledApp"8Q16^B24lr32l8r40l8r48l8
+ ___block_literal_global.222
+ _objc_msgSend$_getCoreDuetIdentifier
+ _objc_msgSend$_handleLoadMediaTaskForResult:error:withCompletionHandler:
+ _objc_msgSend$_makeGlobalQueryParamsFor:
+ _objc_msgSend$addHistoryToken:toMetadataForStore:error:
+ _objc_msgSend$getLocalDeviceIdentifierAndReturnError:
+ _objc_msgSend$historyTokenFromStore:
+ _objc_msgSend$localURL
+ _objc_msgSend$personNameComponentsFromString:
+ _objc_msgSend$postNotificationForContext:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$setLastUpdatedDate:
+ _objc_msgSend$systemFullUserName
- +[STAMSClient handleLoadMediaTaskForResult:error:withCompletionHandler:]
- +[STAMSClient makeGlobalQueryParamsFor:]
- +[STCoreDevice fetchRequestForOrphanedDevices]
- -[STBlueprint updateWithDictionaryRepresentation:].cold.12
- -[STUnique addHistoryToken:forAuthor:toMetadataForStore:error:]
- -[STUnique historyTokenForAuthor:fromStore:]
- GCC_except_table25
- ___104+[STBlueprint(UsageLimit) displayNameForUsageLimitWithCategoryIdentifiers:bundleIdentifiers:webDomains:]_block_invoke_3
- ___54+[STAMSClient loadMediaForTask:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_48_e8_32r40r_e31_B32?0"STInstalledApp"8Q16^B24lr32l8r40l8
- ___block_literal_global.221
- _objc_msgSend$addHistoryToken:forAuthor:toMetadataForStore:error:
- _objc_msgSend$handleLoadMediaTaskForResult:error:withCompletionHandler:
- _objc_msgSend$historyTokenForAuthor:fromStore:
- _objc_msgSend$makeGlobalQueryParamsFor:
CStrings:
+ "(%K == NULL)"
+ "+[STBlueprint(UsageLimit) displayNameForUsageLimitWithCategoryIdentifiers:bundleIdentifiers:webDomains:]"
+ "-[STAppInfoCache _appInfoForBundleIdentifier:]"
+ "-[STAppInfoCache _fetchSyncedInstalledAppInfoForBundleIdentifier:]_block_invoke"
+ "-[STUserDeviceState dictionaryRepresentation] called when device = nil : %{public}@"
+ "-[STUserDeviceState dictionaryRepresentation] called when device.identifier = nil : %{public}@"
+ "<%p ID: %@ Name: %@ Developer: %@, AdamID: %llu>"
+ "AADC_ScreenTimeEnabledUserNotificationBody"
+ "AADC_ScreenTimeEnabledUserNotificationTitle"
+ "AMSMediaTask created with type: AMSMediaTaskTypeApp"
+ "AMSMediaTask created with type: AMSMediaTaskTypeAppDistribution"
+ "Adding account info to media task"
+ "Adding app with bundleID %{public}@ to App Store list"
+ "Adding app with bundleID %{public}@ to global list"
+ "Blueprint version clocks concurrent. Most recent modification wins"
+ "Concurrent"
+ "Did not find app %@ in AMS Response; setting AppInfo to placeholder"
+ "Did not find app %@ in iTunes Response; setting AppInfo to placeholder"
+ "Display name and bundleId missing for appInfo: %{public}@ in function: %s:%d"
+ "Display name missing for appInfo: %{public}@ in function: %s:%d. using bundleId instead"
+ "Display name missing for installedApplication: %{public}@ in function: %s:%d"
+ "DisplayNameUnknown"
+ "Found valid STUserDeviceState: %{public}@"
+ "Local blueprint is more recently modified. We will ignore the received blueprint. Local = %@, Incoming = %@"
+ "Local modification date = %@, Incoming modification date = %@"
+ "Local settings is more recently modified. We will ignore the received settings. Local = %@, Incoming = %@"
+ "Nil appInfo: %{public}@ in function: %s:%d"
+ "Only the inboud blueprint has a modification date. We will overwrite the local blueprint."
+ "Only the local blueprint has a modification date. We will ignore the received blueprint."
+ "Received blueprint is more recently modified. We will overwrite the local blueprint. Local = %@, Incoming = %@"
+ "Received settings is more recently modified. We will overwrite the local settings. Local = %@, Incoming = %@"
+ "STAppInfoCache is vending result with no displayName: %{public}@ in function: %s:%d"
+ "STAppMetadata (global) parsing error - artworkURL is nil"
+ "STAppMetadata (global) parsing error - bundleIdentifier is nil"
+ "STAppMetadata (global) parsing error - platformAttributes is nil"
+ "STAppMetadata (global) parsing error - responseItem[attributes] is nil"
+ "STAppMetadata (global) parsing success for app name: %{public}@"
+ "STAppMetadata parsing error - bundleIdentifier OR artworkURL are nil"
+ "STAppMetadata parsing error - platformAttributes is nil"
+ "STAppMetadata parsing error - responseItem[attributes] is nil"
+ "STAppMetadata parsing success for app name: %{public}@"
+ "STUserDeviceState failed to fetch coreduetIdentifier %{public}@"
+ "STUserDeviceState setting coreduetIdentifier %{public}@"
+ "Settings version clocks concurrent. Most recent modification wins"
+ "Skipping STUserDeviceState with device = nil : %{public}@"
+ "Skipping STUserDeviceState with device.identifier = nil : %{public}@"
+ "_getCoreDuetIdentifier"
+ "_handleLoadMediaTaskForResult:error:withCompletionHandler:"
+ "_makeGlobalQueryParamsFor:"
+ "addHistoryToken:toMetadataForStore:error:"
+ "additionalPlatforms"
+ "appletvos"
+ "fetchHistoryAfterToken failed: %@"
+ "fetchRequestForDevicesMissingUsage"
+ "fetchRequestForNonLocalDevices"
+ "getLocalDeviceIdentifierAndReturnError:"
+ "historyTokenFromStore:"
+ "iphone,ipad,mac,appletv,watch,web"
+ "osx"
+ "personNameComponentsFromString:"
+ "postNotificationForContext:"
+ "remoteObjectProxy"
+ "setLastUpdatedDate:"
+ "systemFullUserName"
+ "v24@0:8@\"STUserNotificationContext\"16"
+ "versionAttributes"
+ "xros"
- "<%p ID: %@ Name: %@ Developer: %@>"
- "Failed to find the app %@"
- "Local Lose"
- "Local Win"
- "addHistoryToken:forAuthor:toMetadataForStore:error:"
- "fetchRequestForOrphanedDevices"
- "handleLoadMediaTaskForResult:error:withCompletionHandler:"
- "historyTokenForAuthor:fromStore:"
- "macSoftware"
- "macos"
- "makeGlobalQueryParamsFor:"

```
