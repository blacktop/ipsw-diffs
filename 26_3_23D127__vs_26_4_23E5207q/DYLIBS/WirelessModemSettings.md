## WirelessModemSettings

> `/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings`

```diff

-805.10.0.0.0
-  __TEXT.__text: 0xfaac
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0xa24
+810.7.0.0.0
+  __TEXT.__text: 0x1245c
+  __TEXT.__auth_stubs: 0xc10
+  __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0x1c2
-  __TEXT.__cstring: 0x10ef
-  __TEXT.__oslogstring: 0x676
-  __TEXT.__gcc_except_tab: 0x178
+  __TEXT.__cstring: 0x148f
+  __TEXT.__oslogstring: 0x9d6
+  __TEXT.__gcc_except_tab: 0x1cc
   __TEXT.__swift5_typeref: 0xdc
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_reflstr: 0x14

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x4c8
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x14f
-  __TEXT.__objc_methname: 0x2154
-  __TEXT.__objc_methtype: 0x627
-  __TEXT.__objc_stubs: 0x2020
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__objc_classname: 0x22f
+  __TEXT.__objc_methname: 0x2a16
+  __TEXT.__objc_methtype: 0xafe
+  __TEXT.__objc_stubs: 0x26e0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae0
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0xd30
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x198
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x12f8
+  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__const: 0x218
+  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__objc_const: 0x1900
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x2d0
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xec
-  __DATA.__data: 0x188
-  __DATA.__bss: 0x120
+  __DATA.__objc_ivar: 0x10c
+  __DATA.__data: 0x248
+  __DATA.__bss: 0x150
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
+  - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D838D76-D42C-3E4F-B27D-B8222ED5D8DC
-  Functions: 304
-  Symbols:   1285
-  CStrings:  894
+  UUID: E37A28D3-7BEF-384C-B5AE-95D97F7F2E8A
+  Functions: 382
+  Symbols:   1560
+  CStrings:  1063
 
Symbols:
+ +[WMSPersonalHotspotDataUsageCache sharedInstance]
+ +[WMSPersonalHotspotDataUsageCache sharedInstance].cold.1
+ -[WMSPersonalHotspotDataUsageCache .cxx_destruct]
+ -[WMSPersonalHotspotDataUsageCache _clearCache]
+ -[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]
+ -[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage].cold.1
+ -[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage].cold.2
+ -[WMSPersonalHotspotDataUsageCache _handleUsageOrInfoChanged]
+ -[WMSPersonalHotspotDataUsageCache _handleUsageOrInfoChanged].cold.1
+ -[WMSPersonalHotspotDataUsageCache _refreshCacheIfNeeded]
+ -[WMSPersonalHotspotDataUsageCache _usageForBundleID:inPeriod:]
+ -[WMSPersonalHotspotDataUsageCache cacheNeedsRefresh]
+ -[WMSPersonalHotspotDataUsageCache cachedDeviceDataUsage]
+ -[WMSPersonalHotspotDataUsageCache ctClient]
+ -[WMSPersonalHotspotDataUsageCache dataRatesChanged]
+ -[WMSPersonalHotspotDataUsageCache dataRatesChanged].cold.1
+ -[WMSPersonalHotspotDataUsageCache fetchDataUsageWithCompletion:]
+ -[WMSPersonalHotspotDataUsageCache initPrivate]
+ -[WMSPersonalHotspotDataUsageCache initWithCoreTelephonyClient:]
+ -[WMSPersonalHotspotDataUsageCache init]
+ -[WMSPersonalHotspotDataUsageCache queue]
+ -[WMSPersonalHotspotDataUsageCache refreshCompletionHandler]
+ -[WMSPersonalHotspotDataUsageCache refreshDataUsageUINotification]
+ -[WMSPersonalHotspotDataUsageCache refreshDataUsageUINotification].cold.1
+ -[WMSPersonalHotspotDataUsageCache refreshInProgress]
+ -[WMSPersonalHotspotDataUsageCache setCacheNeedsRefresh:]
+ -[WMSPersonalHotspotDataUsageCache setCachedDeviceDataUsage:]
+ -[WMSPersonalHotspotDataUsageCache setCtClient:]
+ -[WMSPersonalHotspotDataUsageCache setQueue:]
+ -[WMSPersonalHotspotDataUsageCache setRefreshCompletionHandler:]
+ -[WMSPersonalHotspotDataUsageCache setRefreshInProgress:]
+ -[WMSPersonalHotspotDataUsageCache totalHotspotClientUsageForPeriod:]
+ -[WirelessModemController _dataUsageCacheRefreshedHandler:]
+ -[WirelessModemController _dataUsageCacheRefreshedHandler:].cold.1
+ -[WirelessModemController _fetchAndDisplayDataUsage]
+ -[WirelessModemController fetchPersonalHotspotDataUsageSpecifierWithTotalDataUsage:]
+ -[WirelessModemController fetchPersonalHotspotDataUsageSpecifierWithTotalDataUsage:].cold.1
+ -[WirelessModemController updateDataUsageSection]
+ -[WirelessModemController updateDataUsageSection].cold.1
+ -[WirelessModemController updateDataUsageSection].cold.2
+ -[WirelessModemController updateDataUsageSection].cold.3
+ -[WirelessModemController updateDataUsageSection].cold.4
+ -[WirelessModemController updateDataUsageSection].cold.5
+ -[WirelessModemController updateDataUsageSection].cold.6
+ GCC_except_table5
+ GCC_except_table59
+ GCC_except_table7
+ GCC_except_table93
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_WMSPersonalHotspotDataUsageCache
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._cacheNeedsRefresh
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._cachedDeviceDataUsage
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._ctClient
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._queue
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._refreshCompletionHandler
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._refreshInProgress
+ _OBJC_IVAR_$_WirelessModemController._hotspotDataUsageGroupSpec
+ _OBJC_IVAR_$_WirelessModemController._hotspotDataUsageSpecifiers
+ _OBJC_METACLASS_$_WMSPersonalHotspotDataUsageCache
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _PHocalizedStringWithFormat
+ _PSBundlePathForPreferenceBundle
+ _SFRuntimeAbsoluteFilePathForPath
+ __OBJC_$_CLASS_METHODS_WMSPersonalHotspotDataUsageCache
+ __OBJC_$_INSTANCE_METHODS_WMSPersonalHotspotDataUsageCache
+ __OBJC_$_INSTANCE_VARIABLES_WMSPersonalHotspotDataUsageCache
+ __OBJC_$_PROP_LIST_WMSPersonalHotspotDataUsageCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientAppDataUsageDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientRegistrationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientAppDataUsageDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientRegistrationDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientAppDataUsageDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientRegistrationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WMSPersonalHotspotDataUsageCache
+ __OBJC_CLASS_RO_$_WMSPersonalHotspotDataUsageCache
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientAppDataUsageDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientRegistrationDelegate
+ __OBJC_METACLASS_RO_$_WMSPersonalHotspotDataUsageCache
+ __OBJC_PROTOCOL_$_CoreTelephonyClientAppDataUsageDelegate
+ __OBJC_PROTOCOL_$_CoreTelephonyClientRegistrationDelegate
+ ___50+[WMSPersonalHotspotDataUsageCache sharedInstance]_block_invoke
+ ___52-[WirelessModemController _fetchAndDisplayDataUsage]_block_invoke
+ ___52-[WirelessModemController _fetchAndDisplayDataUsage]_block_invoke.cold.1
+ ___52-[WirelessModemController _fetchAndDisplayDataUsage]_block_invoke.cold.2
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.14
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.16
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.16.cold.1
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.cold.1
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.cold.2
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.cold.3
+ ___66-[WMSPersonalHotspotDataUsageCache refreshDataUsageUINotification]_block_invoke
+ ___block_descriptor_40_e8_32w_e39_v24?0"CTDeviceDataUsage"8"NSError"16lw32l8
+ ___block_literal_global.18
+ ___block_literal_global.20
+ ___logger_block_invoke
+ ___usageSizeString_block_invoke
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _kWMSPersonalHotspotDataUsageCacheRefreshedNotification
+ _logger
+ _logger.cold.1
+ _logger.logger
+ _logger.onceToken
+ _objc_autorelease
+ _objc_exception_throw
+ _objc_msgSend$_clearCache
+ _objc_msgSend$_fetchAndDisplayDataUsage
+ _objc_msgSend$_fetchDeviceDataUsage
+ _objc_msgSend$_handleUsageOrInfoChanged
+ _objc_msgSend$_refreshCacheIfNeeded
+ _objc_msgSend$_usageForBundleID:inPeriod:
+ _objc_msgSend$appDataUsageForPeriod:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$bundleId
+ _objc_msgSend$cacheNeedsRefresh
+ _objc_msgSend$cachedDeviceDataUsage
+ _objc_msgSend$cellularHome
+ _objc_msgSend$cellularRoaming
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$dataUsageForLastPeriods:completion:
+ _objc_msgSend$fetchDataUsageWithCompletion:
+ _objc_msgSend$fetchPersonalHotspotDataUsageSpecifierWithTotalDataUsage:
+ _objc_msgSend$hiddenAppDataUsageForPeriod:
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithCoreTelephonyClient:
+ _objc_msgSend$initWithName:reason:userInfo:
+ _objc_msgSend$initWithParentListController:properties:
+ _objc_msgSend$initWithPath:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithValidatedFormat:validFormatSpecifiers:locale:arguments:error:
+ _objc_msgSend$insertContiguousSpecifiers:atIndex:animated:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$native
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$principalClass
+ _objc_msgSend$proxied
+ _objc_msgSend$proxiedOnlyAppDataUsageForPeriod:
+ _objc_msgSend$refreshCompletionHandler
+ _objc_msgSend$refreshDataUsageUINotification
+ _objc_msgSend$refreshInProgress
+ _objc_msgSend$setAdaptive:
+ _objc_msgSend$setCacheNeedsRefresh:
+ _objc_msgSend$setCachedDeviceDataUsage:
+ _objc_msgSend$setCountStyle:
+ _objc_msgSend$setRefreshCompletionHandler:
+ _objc_msgSend$setRefreshInProgress:
+ _objc_msgSend$setZeroPadsFractionDigits:
+ _objc_msgSend$specifiersWithSpecifier:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringFromByteCount:
+ _objc_msgSend$systemServiceDataUsageForPeriod:
+ _objc_msgSend$totalHotspotClientUsageForPeriod:
+ _objc_msgSend$traitCollection
+ _objc_msgSend$uninstalledAppDataUsageForPeriod:
+ _objc_msgSend$updateDataUsageSection
+ _objc_msgSend$used
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_setProperty_nonatomic_copy
+ _objc_sync_enter
+ _objc_sync_exit
+ _sharedInstance.cacheInstance
+ _sharedInstance.onceToken
+ _usageSizeString
+ _usageSizeString.byteCountFormatter
+ _usageSizeString.cold.1
+ _usageSizeString.onceToken
+ _zeroPaddedMACAddress
- GCC_except_table88
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "%s: Clearing cache due to usage change"
+ "%s: Current period usage: %lu bytes, Previous period: %lu bytes"
+ "%s: Data rates changed"
+ "%s: Data usage cache refreshed, updating UI"
+ "%s: Data usage fetch completed"
+ "%s: Data usage specifiers already present, reloading"
+ "%s: Fetch failed with error: %{public}@"
+ "%s: Fetch succeeded with %lu app usage entries for period 0"
+ "%s: Initiating data usage fetch from CoreTelephony"
+ "%s: Inserted %lu data usage specifiers at index %ld"
+ "%s: Inserting data usage specifiers"
+ "%s: No usage data available (totalUsage = 0)"
+ "%s: Posting %@ notification"
+ "%s: Received notification to refresh data usage UI"
+ "%s: Refresh already in progress, skipping"
+ "%s: Removing data usage specifiers"
+ "%s: Total usage for current period: %lu bytes"
+ "%s: Warning - no completion handler set for fetch"
+ "-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]"
+ "-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke"
+ "-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke_2"
+ "-[WMSPersonalHotspotDataUsageCache _handleUsageOrInfoChanged]"
+ "-[WMSPersonalHotspotDataUsageCache dataRatesChanged]"
+ "-[WMSPersonalHotspotDataUsageCache refreshDataUsageUINotification]"
+ "-[WirelessModemController _dataUsageCacheRefreshedHandler:]"
+ "-[WirelessModemController _fetchAndDisplayDataUsage]_block_invoke"
+ "-[WirelessModemController updateDataUsageSection]"
+ "/Library/Caches/com.apple.xbs/43BB4EEF-655F-496B-A3F6-0CDF2CDEBCB2/TemporaryDirectory.3CRUcT/Sources/WirelessModemSettings/Source/WMSSettingsNavigation.swift"
+ "/Library/Caches/com.apple.xbs/43BB4EEF-655F-496B-A3F6-0CDF2CDEBCB2/TemporaryDirectory.3CRUcT/Sources/WirelessModemSettings/Source/WirelessModemSettings.swift"
+ "0"
+ ":"
+ "@\"CTDeviceDataUsage\""
+ "@\"CoreTelephonyClient\""
+ "@24@0:8Q16"
+ "@32@0:8@16Q24"
+ "@?"
+ "@?16@0:8"
+ "CoreTelephonyClientAppDataUsageDelegate"
+ "CoreTelephonyClientRegistrationDelegate"
+ "Failed to load Wireless Modem Settings aka Personal Hotspot bundle controller"
+ "PHDataUsage"
+ "PersonalHotspotBundleController"
+ "PersonalHotspotDataUsage"
+ "Q24@0:8Q16"
+ "T@\"CTDeviceDataUsage\",&,N,V_cachedDeviceDataUsage"
+ "T@\"CoreTelephonyClient\",&,N,V_ctClient"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@?,C,N,V_refreshCompletionHandler"
+ "TB,N,V_cacheNeedsRefresh"
+ "TB,N,V_refreshInProgress"
+ "Unsupported initializer"
+ "Use sharedInstance instead"
+ "WMSPersonalHotspotDataUsageCache"
+ "WMSPersonalHotspotDataUsageCacheRefreshedNotification"
+ "_"
+ "_cacheNeedsRefresh"
+ "_cachedDeviceDataUsage"
+ "_clearCache"
+ "_ctClient"
+ "_dataUsageCacheRefreshedHandler:"
+ "_fetchAndDisplayDataUsage"
+ "_fetchDeviceDataUsage"
+ "_handleUsageOrInfoChanged"
+ "_hotspotDataUsageGroupSpec"
+ "_hotspotDataUsageSpecifiers"
+ "_queue"
+ "_refreshCacheIfNeeded"
+ "_refreshCompletionHandler"
+ "_refreshInProgress"
+ "_usageForBundleID:inPeriod:"
+ "appDataUsageForPeriod:"
+ "arrayWithCapacity:"
+ "arrayWithObject:"
+ "bundleId"
+ "cacheNeedsRefresh"
+ "cachedDeviceDataUsage"
+ "cellChanged:cell:"
+ "cellMonitorUpdate:info:"
+ "cellularHome"
+ "cellularRoaming"
+ "com.apple.cellularSettings"
+ "com.apple.datausage.personalhotspot"
+ "com.apple.wirelessmodemsettings.dataUsageQueue"
+ "componentsJoinedByString:"
+ "ctClient"
+ "customerServiceProfileChanged:visible:"
+ "dataRatesChanged"
+ "dataUsageForLastPeriods:completion:"
+ "displayStatusChanged:status:"
+ "encryptionStatusChanged:info:"
+ "enhancedDataLinkQualityChanged:metric:"
+ "enhancedVoiceLinkQualityChanged:metric:"
+ "fetchDataUsageWithCompletion:"
+ "fetchPersonalHotspotDataUsageSpecifierWithTotalDataUsage:"
+ "hiddenAppDataUsageForPeriod:"
+ "imsRegistrationChanged:info:"
+ "initPrivate"
+ "initWithCoreTelephonyClient:"
+ "initWithName:reason:userInfo:"
+ "initWithParentListController:properties:"
+ "initWithQueue:"
+ "initWithValidatedFormat:validFormatSpecifiers:locale:arguments:error:"
+ "insertContiguousSpecifiers:atIndex:animated:"
+ "native"
+ "networkListAvailable:list:"
+ "networkReselectionNeeded:"
+ "networkSelected:success:mode:"
+ "nrDisableStatusChanged:status:"
+ "operatorNameChanged:name:"
+ "plmnChanged:plmn:"
+ "postNotificationName:object:"
+ "principalClass"
+ "proxied"
+ "proxiedOnlyAppDataUsageForPeriod:"
+ "queue"
+ "ratSelectionChanged:selection:"
+ "refreshCompletionHandler"
+ "refreshDataUsageUINotification"
+ "refreshInProgress"
+ "rejectCauseCodeChanged:causeCode:"
+ "setAdaptive:"
+ "setCacheNeedsRefresh:"
+ "setCachedDeviceDataUsage:"
+ "setCountStyle:"
+ "setCtClient:"
+ "setQueue:"
+ "setRefreshCompletionHandler:"
+ "setRefreshInProgress:"
+ "setZeroPadsFractionDigits:"
+ "signalStrengthChanged:info:"
+ "stringByAppendingString:"
+ "stringByTrimmingCharactersInSet:"
+ "stringFromByteCount:"
+ "systemServiceDataUsageForPeriod:"
+ "totalHotspotClientUsageForPeriod:"
+ "uninstalledAppDataUsageForPeriod:"
+ "updateDataUsageSection"
+ "used"
+ "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
+ "v24@0:8@?16"
+ "v24@?0@\"CTDeviceDataUsage\"8@\"NSError\"16"
+ "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTEncryptionStatusInfo\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTNRStatus\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTPlmnInfo\"24"
+ "v32@0:8@\"CTServiceDescriptor\"16@\"CTRatSelection\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTCellInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedDataLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTIMSRegistrationTransportInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTNetworkList\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTRegistrationDisplayStatus\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSignalStrengthInfo\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTVoiceLinkQualityMetric\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSDictionary\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
+ "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
+ "v36@0:8@\"CTXPCServiceSubscriptionContext\"16B24@\"NSString\"28"
+ "v36@0:8@16B24@28"
+ "voiceLinkQualityChanged:metric:"
+ "whitespaceCharacterSet"
- "/Library/Caches/com.apple.xbs/Sources/WirelessModemSettings/Source/WMSSettingsNavigation.swift"
- "/Library/Caches/com.apple.xbs/Sources/WirelessModemSettings/Source/WirelessModemSettings.swift"

```
