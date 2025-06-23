## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-428.0.0.0.1
-  __TEXT.__text: 0x3bd70
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_stubs: 0x67c0
-  __TEXT.__objc_methlist: 0x2a88
+437.0.0.0.0
+  __TEXT.__text: 0x3f200
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x6c40
+  __TEXT.__objc_methlist: 0x2c18
   __TEXT.__const: 0x1e8
-  __TEXT.__oslogstring: 0x4d53
-  __TEXT.__cstring: 0x2f00
-  __TEXT.__objc_classname: 0x2f0
-  __TEXT.__objc_methtype: 0x1035
-  __TEXT.__objc_methname: 0x7ace
-  __TEXT.__gcc_except_tab: 0x1638
-  __TEXT.__unwind_info: 0xd08
-  __DATA_CONST.__auth_got: 0x4a8
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x1378
-  __DATA_CONST.__cfstring: 0x2520
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__oslogstring: 0x4ec6
+  __TEXT.__cstring: 0x3241
+  __TEXT.__objc_classname: 0x308
+  __TEXT.__objc_methtype: 0x10ca
+  __TEXT.__objc_methname: 0x8093
+  __TEXT.__gcc_except_tab: 0x17d8
+  __TEXT.__unwind_info: 0xdb8
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x14d0
+  __DATA_CONST.__cfstring: 0x28a0
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0x588
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3ef0
-  __DATA.__objc_selrefs: 0x1f30
-  __DATA.__objc_ivar: 0x308
-  __DATA.__objc_data: 0xc80
+  __DATA.__objc_const: 0x4080
+  __DATA.__objc_selrefs: 0x2080
+  __DATA.__objc_ivar: 0x31c
+  __DATA.__objc_data: 0xcd0
   __DATA.__data: 0x250
   __DATA.__bss: 0x1e8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FADB037-45EC-364E-9862-4809EA3C9411
-  Functions: 1301
-  Symbols:   221
-  CStrings:  2761
+  UUID: E156B02D-C644-3F1B-A3B1-502AB3143A9B
+  Functions: 1350
+  Symbols:   225
+  CStrings:  2891
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BPSPublisher
+ _traverse_directory
CStrings:
+ "%s: can't decode data with %@"
+ "%s: can't read from disk with %@"
+ "%s: incorrect binary path type for bundle ID %@"
+ "%s: incorrect binaryPaths type for bundleID %@"
+ "%s: incorrect sharedPaths type for bundleID %@"
+ "%s: unknown sorting criteria"
+ "-[SACacheUsageTelemetry getSortedBundleIDs:by:]_block_invoke"
+ "-[SACacheUsageTelemetry loadFromDisk]"
+ "-[SAVolumeScanner sendCacheUsageTelemetryWithBGTask:]"
+ "@32@0:8@16q24"
+ "App"
+ "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16"
+ "B56@0:8@16@24@32@40@48"
+ "Cache usage telemetry Deferred"
+ "CacheUsage.db"
+ "FAILED to log %@ cache usage telemetry using AnalyticsSendEventLazy\n"
+ "InFocus"
+ "Q32@0:8@16@24"
+ "SACacheUsageTelemetry"
+ "T@\"NSDate\",&,V_lastRunDate"
+ "T@\"NSMutableDictionary\",&,V_cacheUsageTelemetry"
+ "T@\"NSMutableDictionary\",&,V_movingAveragesInfo"
+ "T@\"NSMutableSet\",&,VbinaryPaths"
+ "T@\"NSNumber\",&,V_databaseVersion"
+ "UpdateCacheAndTmpTelemetryEntries:appPathList:pathList:BGTask:"
+ "_cacheUsageTelemetry"
+ "_databaseVersion"
+ "_lastRunDate"
+ "_movingAveragesInfo"
+ "addValueToTelemetryEntry:value:bundleIDs:"
+ "app_usage"
+ "app_usage_30d"
+ "binaryURLs"
+ "buildCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
+ "cacheUsageTelemetry"
+ "cache_age_weighted_size"
+ "cache_age_weighted_size_30d"
+ "cache_file_count_30d"
+ "cache_purgeable_count"
+ "cache_purgeable_size"
+ "cache_size_30d"
+ "calculateMovingAverageForKey:currentValueKey:numOfSamples:windowLength:appAverageInfo:bundleIDs:"
+ "can't archive data with %@"
+ "com.apple.massStorage.spaceAttribution.cacheUsage"
+ "createAppCacheUsageInfoForBundleIDs:"
+ "data_file_count_30"
+ "data_size"
+ "data_size_30d"
+ "databaseVersion"
+ "databaseVersionNumber"
+ "dateWithTimeIntervalSince1970:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "disk_used"
+ "doubleValue"
+ "error"
+ "eventBody"
+ "getAllAppsUsageTime:"
+ "getSortedBundleIDs:by:"
+ "getValueForTelemetryEntry:bundleIDs:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "isDataURL"
+ "lastRunDate"
+ "movingAveragesInfo"
+ "numberWithDouble:"
+ "publisherWithOptions:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "removeBinaryPath:"
+ "removeBinaryPaths:"
+ "removeNonExistingAppsFromDiskData"
+ "sendCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
+ "sendCacheUsageTelemetryWithBGTask:"
+ "setCacheUsageTelemetry:"
+ "setDatabaseVersion:"
+ "setLastRunDate:"
+ "setMovingAveragesInfo:"
+ "setValueToTelemetryEntry:value:bundleIDs:"
+ "sinkWithCompletion:receiveInput:"
+ "starting"
+ "subscribeToAppInFocusStreamBeginning completion: %ld %@"
+ "time_since_last_used"
+ "timestamp"
+ "tmp_age_weighted_size"
+ "tmp_age_weighted_size_30d"
+ "tmp_file_count"
+ "tmp_file_count_30d"
+ "tmp_file_size"
+ "tmp_file_size_30d"
+ "tmp_purgeable_count"
+ "tmp_purgeable_size"
+ "traversePath:BGTask:reply:"
+ "updateAppsSizesAndUsageTimeInTelemetry:telemetryManager:"
+ "updateMovingAveragesInTelemetry"
+ "updateTelemetryForBundleIDs:folderType:size:fileCount:purgeableFileCount:purgeableFileSize:ageWeightedSize:"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v48@0:8@16@24@32@40"
+ "v48@?0Q8Q16Q24Q32Q40"
+ "v56@0:8@16@24@32@40@48"
+ "v64@0:8@16@24Q32Q40@48@56"
+ "v72@0:8@16q24Q32Q40Q48Q56Q64"
+ "vendorName"
- "%s: incorrect sharedURLs type for bundleID %@"
- "T@\"NSMutableSet\",&,V_binaryPaths"
- "_binaryPaths"

```
