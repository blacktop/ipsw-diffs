## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-322.120.5.0.0
-  __TEXT.__text: 0x37938
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x5e80
-  __TEXT.__objc_methlist: 0x2680
-  __TEXT.__objc_methname: 0x6dfc
-  __TEXT.__objc_classname: 0x2b7
-  __TEXT.__objc_methtype: 0xfaa
-  __TEXT.__const: 0x1c8
-  __TEXT.__gcc_except_tab: 0x15e8
-  __TEXT.__cstring: 0x2c8d
-  __TEXT.__oslogstring: 0x47cb
-  __TEXT.__unwind_info: 0xc10
-  __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x1260
-  __DATA_CONST.__cfstring: 0x24a0
-  __DATA_CONST.__objc_classlist: 0x120
+322.140.4.0.0
+  __TEXT.__text: 0x3ac6c
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x62e0
+  __TEXT.__objc_methlist: 0x2820
+  __TEXT.__objc_methname: 0x73f8
+  __TEXT.__objc_classname: 0x2cf
+  __TEXT.__objc_methtype: 0x1068
+  __TEXT.__const: 0x1b8
+  __TEXT.__gcc_except_tab: 0x180c
+  __TEXT.__cstring: 0x2fe1
+  __TEXT.__oslogstring: 0x48dd
+  __TEXT.__unwind_info: 0xcd0
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x1408
+  __DATA_CONST.__cfstring: 0x2800
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3910
-  __DATA.__objc_selrefs: 0x1ca8
-  __DATA.__objc_ivar: 0x2c0
-  __DATA.__objc_data: 0xb40
+  __DATA.__objc_const: 0x3aa0
+  __DATA.__objc_selrefs: 0x1df8
+  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_data: 0xb90
   __DATA.__data: 0x248
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
-  UUID: 35F4748F-0D63-3632-BA71-5B03B4795122
-  Functions: 1198
-  Symbols:   212
-  CStrings:  2593
+  UUID: 713FA6DC-1970-3EEA-A460-F2B64C62CA88
+  Functions: 1248
+  Symbols:   216
+  CStrings:  2725
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BPSPublisher
+ _traverse_directory
CStrings:
+ "%s: can't decode data with %@"
+ "%s: can't read from disk with %@"
+ "%s: unkown sorting criteria"
+ "-[SACacheUsageTelemetry getSortedBundleIDs:by:]_block_invoke"
+ "-[SACacheUsageTelemetry loadFromDisk]"
+ "-[SAVolumeScanner sendCacheUsageTelemetryWithBGTask:]"
+ "@32@0:8@16q24"
+ "@44@0:8@16i24I28i32i36B40"
+ "@48@0:8i16I20i24i28Q32Q40"
+ "App"
+ "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16"
+ "B56@0:8@16@24@32@40@48"
+ "Cache usage telemetry Deferred"
+ "CacheUsage.db"
+ "FAILED to log %@ cache usage telemetry using AnalyticsSendEventLazy\n"
+ "I"
+ "I16@0:8"
+ "InFocus"
+ "Q32@0:8@16@24"
+ "RESIDENCY_%u"
+ "SACacheUsageTelemetry"
+ "T@\"NSDate\",&,V_lastRunDate"
+ "T@\"NSMutableDictionary\",&,V_cacheUsageTelemetry"
+ "T@\"NSMutableDictionary\",&,V_movingAveragesInfo"
+ "T@\"NSNumber\",&,V_databaseVersion"
+ "TI,V_residency"
+ "TQ,V_lastKnownAppCacheSize"
+ "_cacheUsageTelemetry"
+ "_databaseVersion"
+ "_lastRunDate"
+ "_movingAveragesInfo"
+ "addValueToTelemetryEntry:value:bundleIDs:"
+ "app_usage"
+ "app_usage_30d"
+ "buildCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
+ "cacheUsageTelemetry"
+ "cache_age_weighted_size"
+ "cache_age_weighted_size_30d"
+ "cache_file_count"
+ "cache_file_count_30d"
+ "cache_purgeable_count"
+ "cache_purgeable_size"
+ "cache_size_30d"
+ "calculateMovingAverageForKey:currentValueKey:numOfSamples:windowLength:appAverageInfo:bundleIDs:"
+ "can't archive data with %@"
+ "com.apple.massStorage.spaceAttribution.cacheUsage"
+ "createAppCacheUsageInfoForBundleIDs:"
+ "data_file_count30d"
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
+ "getAppCacheSizeAndFileCount:"
+ "getSortedBundleIDs:by:"
+ "getValueForTelemetryEntry:bundleIDs:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "lastRunDate"
+ "movingAveragesInfo"
+ "numberWithDouble:"
+ "publisherWithOptions:"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "removeNonExistingAppsFromDiskData"
+ "sendCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
+ "sendCacheUsageTelemetryWithBGTask:"
+ "setCacheUsageTelemetry:"
+ "setDatabaseVersion:"
+ "setLastKnownAppCacheSize:"
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
+ "total_cache_file_count"
+ "traversePath:BGTask:reply:"
+ "updateAppsSizesAndUsageTimeInTelemetry:telemetryManager:"
+ "updateCacheAndTmpTelemetryEntries:appPathList:pathList:BGTask:"
+ "updateCacheFileCount:forBundleSet:"
+ "updateMovingAveragesInTelemetry"
+ "updateTelemetryForBundleIDs:folderType:size:fileCount:purgeableFileCount:purgeableFileSize:ageWeightedSize:"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v24@?0Q8Q16"
+ "v28@?0@\"NSString\"8I16@\"SDADataBaseAveElement\"20"
+ "v32@0:8Q16@24"
+ "v32@0:8i16I20@?24"
+ "v40@0:8@16Q24@32"
+ "v40@0:8@16i24I28@?32"
+ "v48@0:8@16@24@32@40"
+ "v48@?0@\"NSString\"8i16I20i24i28@\"SDAHistogramElement\"32^B40"
+ "v48@?0Q8Q16Q24Q32Q40"
+ "v56@0:8@16@24@32@40@48"
+ "v56@0:8i16I20i24i28Q32Q40Q48"
+ "v64@0:8@16@24Q32Q40@48@56"
+ "v64@0:8@16i24@28I36Q40Q48Q56"
+ "v64@0:8@16i24i28i32I36Q40Q48Q56"
+ "v72@0:8@16q24Q32Q40Q48Q56Q64"
+ "vendorName"
- "@44@0:8@16i24i28i32i36B40"
- "@48@0:8i16i20i24i28Q32Q40"
- "RESIDENCY_1"
- "RESIDENCY_2"
- "RESIDENCY_3"
- "RESIDENCY_4"
- "TQ,R,V_lastKnownAppCacheSize"
- "Ti,V_residency"
- "v28@?0@\"NSString\"8i16@\"SDADataBaseAveElement\"20"
- "v32@0:8i16i20@?24"
- "v40@0:8@16i24i28@?32"
- "v48@?0@\"NSString\"8i16i20i24i28@\"SDAHistogramElement\"32^B40"
- "v56@0:8i16i20i24i28Q32Q40Q48"
- "v64@0:8@16i24@28i36Q40Q48Q56"
- "v64@0:8@16i24i28i32i36Q40Q48Q56"

```
