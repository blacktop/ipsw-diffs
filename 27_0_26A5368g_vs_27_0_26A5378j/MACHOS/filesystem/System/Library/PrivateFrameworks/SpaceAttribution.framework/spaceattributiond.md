## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-  __TEXT.__text: 0x44e70
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x7500
-  __TEXT.__objc_methlist: 0x30a0
+  __TEXT.__text: 0x42094
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0x72e0
+  __TEXT.__objc_methlist: 0x2f38
   __TEXT.__const: 0x228
-  __TEXT.__gcc_except_tab: 0x180c
-  __TEXT.__cstring: 0x3708
-  __TEXT.__oslogstring: 0x5315
-  __TEXT.__objc_classname: 0x2fe
-  __TEXT.__objc_methname: 0x8c53
-  __TEXT.__objc_methtype: 0x1227
-  __TEXT.__unwind_info: 0xf50
-  __DATA_CONST.__const: 0x1b68
-  __DATA_CONST.__cfstring: 0x3040
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__gcc_except_tab: 0x16c4
+  __TEXT.__cstring: 0x3457
+  __TEXT.__oslogstring: 0x523a
+  __TEXT.__objc_classname: 0x2e8
+  __TEXT.__objc_methname: 0x87d8
+  __TEXT.__objc_methtype: 0x1192
+  __TEXT.__unwind_info: 0xeb8
+  __DATA_CONST.__const: 0x1a48
+  __DATA_CONST.__cfstring: 0x2ce0
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_intobj: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0xa8
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x46b0
-  __DATA.__objc_selrefs: 0x2338
-  __DATA.__objc_ivar: 0x384
-  __DATA.__objc_data: 0xd70
+  __DATA.__objc_const: 0x4520
+  __DATA.__objc_selrefs: 0x2280
+  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_data: 0xd20
   __DATA.__data: 0x250
   __DATA.__bss: 0x210
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1545
-  Symbols:   192
-  CStrings:  3197
+  Functions: 1498
+  Symbols:   191
+  CStrings:  3094
 
Sections:
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__data : content changed
Symbols:
- _traverse_directory
CStrings:
- "%s: can't decode data with %@"
- "%s: can't read from disk with %@"
- "%s: unknown sorting criteria"
- "-[SACacheUsageTelemetry getSortedBundleIDs:by:]_block_invoke"
- "-[SACacheUsageTelemetry loadFromDisk]"
- "@32@0:8@16q24"
- "B24@?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16"
- "B56@0:8@16@24@32@40@48"
- "Cache usage telemetry Deferred"
- "CacheUsage.db"
- "FAILED to log %@ cache usage telemetry using AnalyticsSendEventLazy\n"
- "Q32@0:8@16@24"
- "SACacheUsageTelemetry"
- "T@\"NSDate\",&,V_lastRunDate"
- "T@\"NSMutableDictionary\",&,V_cacheUsageTelemetry"
- "T@\"NSMutableDictionary\",&,V_movingAveragesInfo"
- "T@\"NSNumber\",&,V_databaseVersion"
- "UpdateCacheAndTmpTelemetryEntries:appPathList:pathList:BGTask:"
- "_cacheUsageTelemetry"
- "_databaseVersion"
- "_lastRunDate"
- "_movingAveragesInfo"
- "addValueToTelemetryEntry:value:bundleIDs:"
- "app_usage"
- "app_usage_30d"
- "buildCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
- "cacheUsageTelemetry"
- "cache_age_weighted_size"
- "cache_age_weighted_size_30d"
- "cache_file_count_30d"
- "cache_purgeable_count"
- "cache_purgeable_size"
- "cache_size_30d"
- "calculateMovingAverageForKey:currentValueKey:numOfSamples:windowLength:appAverageInfo:bundleIDs:"
- "can't archive data with %@"
- "com.apple.massStorage.spaceAttribution.cacheUsage"
- "createAppCacheUsageInfoForBundleIDs:"
- "data_file_count_30"
- "data_size"
- "data_size_30d"
- "databaseVersion"
- "databaseVersionNumber"
- "dateWithTimeIntervalSince1970:"
- "disk_used"
- "getSortedBundleIDs:by:"
- "getValueForTelemetryEntry:bundleIDs:"
- "lastRunDate"
- "movingAveragesInfo"
- "removeNonExistingAppsFromDiskData"
- "sendCacheUsageTelemetry:telemetryManager:appPathList:pathList:BGTask:"
- "setCacheUsageTelemetry:"
- "setDatabaseVersion:"
- "setLastRunDate:"
- "setMovingAveragesInfo:"
- "setValueToTelemetryEntry:value:bundleIDs:"
- "time_since_last_used"
- "tmp_age_weighted_size"
- "tmp_age_weighted_size_30d"
- "tmp_file_count"
- "tmp_file_count_30d"
- "tmp_file_size"
- "tmp_file_size_30d"
- "tmp_purgeable_count"
- "tmp_purgeable_size"
- "traversePath:BGTask:reply:"
- "updateAppsSizesAndUsageTimeInTelemetry:telemetryManager:"
- "updateMovingAveragesInTelemetry"
- "updateTelemetryForBundleIDs:folderType:size:fileCount:purgeableFileCount:purgeableFileSize:ageWeightedSize:"
- "v48@0:8@16@24@32@40"
- "v48@?0Q8Q16Q24Q32Q40"
- "v56@0:8@16@24@32@40@48"
- "v64@0:8@16@24Q32Q40@48@56"
- "v72@0:8@16q24Q32Q40Q48Q56Q64"

```
