## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-448.80.4.0.0
-  __TEXT.__text: 0x13814
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x13b8
+458.100.14.0.0
+  __TEXT.__text: 0x14780
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x14b0
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x6dc
-  __TEXT.__cstring: 0x11b3
-  __TEXT.__oslogstring: 0x1222
-  __TEXT.__unwind_info: 0x628
-  __TEXT.__objc_classname: 0x16f
-  __TEXT.__objc_methname: 0x2fb8
+  __TEXT.__cstring: 0x1359
+  __TEXT.__oslogstring: 0x13e1
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__objc_classname: 0x199
+  __TEXT.__objc_methname: 0x3231
   __TEXT.__objc_methtype: 0x7ae
-  __TEXT.__objc_stubs: 0x1ee0
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x448
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__objc_stubs: 0x2120
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd30
+  __DATA_CONST.__objc_selrefs: 0xe08
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0x1d48
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x1ec8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x138
+  __AUTH.__objc_data: 0x3e8
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E108B64-1BC5-31D7-8F16-8852E322D782
-  Functions: 565
-  Symbols:   1877
-  CStrings:  1142
+  UUID: A55BC00B-0150-33B6-B4C4-5EAAB7BC8CBE
+  Functions: 602
+  Symbols:   2015
+  CStrings:  1216
 
Symbols:
+ +[SAAppSize sizeWithDataSize:purgeableSize:]
+ +[SAAppSize sizeWithFixedSize:andDataSize:]
+ +[SAAppSize sizeWithFixedSize:dataSize:]
+ +[SAAppSizerCacheManager cacheAppSizes:]
+ +[SAAppSizerCacheManager cacheAppSizes:].cold.1
+ +[SAAppSizerCacheManager cacheAppSizes:].cold.2
+ +[SAAppSizerCacheManager cacheAppSizes:].cold.3
+ +[SAAppSizerCacheManager cacheFilePath]
+ +[SAAppSizerCacheManager getCacheDict]
+ +[SAAppSizerCacheManager getCacheDict].cold.1
+ +[SAAppSizerCacheManager getCacheDict].cold.2
+ +[SAAppSizerCacheManager getCacheDict].cold.3
+ +[SAAppSizerCacheManager getLastCachedAppSizes:maxAge:reply:]
+ +[SAPerfPowerMetrics getStorageConsumptionMetrics:maxAge:reply:]
+ -[SAAppSize addAppSize:]
+ -[SAAppSize setStagedSize:]
+ -[SAAppSize stagedSize]
+ -[SAAppSize withAppCacheSize:]
+ -[SAAppSize withCacheDeletePluginSize:]
+ -[SAAppSize withCloneFixUpSize:]
+ -[SAAppSize withCloneSize:]
+ -[SAAppSize withDataSize:]
+ -[SAAppSize withFixedSize:]
+ -[SAAppSize withPhysicalSize:]
+ -[SAAppSize withPurgeableSize:]
+ -[SAAppSizerResults addToSoftwareUpdateDetails:key:]
+ -[SAAppSizerResults setSoftwareUpdateDetails:]
+ -[SAAppSizerResults softwareUpdateDetails]
+ -[SAAppSizerResults updateBundleIDs:fixedSize:stagedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table112
+ GCC_except_table49
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table97
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_SAAppSizerCacheManager
+ _OBJC_CLASS_$_SAPerfPowerMetrics
+ _OBJC_IVAR_$_SAAppSize._stagedSize
+ _OBJC_IVAR_$_SAAppSizerResults._softwareUpdateDetails
+ _OBJC_METACLASS_$_SAAppSizerCacheManager
+ _OBJC_METACLASS_$_SAPerfPowerMetrics
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_CLASS_METHODS_SAAppSizerCacheManager
+ __OBJC_$_CLASS_METHODS_SAPerfPowerMetrics
+ __OBJC_CLASS_RO_$_SAAppSizerCacheManager
+ __OBJC_CLASS_RO_$_SAPerfPowerMetrics
+ __OBJC_METACLASS_RO_$_SAAppSizerCacheManager
+ __OBJC_METACLASS_RO_$_SAPerfPowerMetrics
+ ___33+[SASupport getAllAppsUsageTime:]_block_invoke.148
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.115
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.115.cold.1
+ ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.186
+ ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.186.cold.1
+ ___64+[SAPerfPowerMetrics getStorageConsumptionMetrics:maxAge:reply:]_block_invoke
+ ___64+[SAPerfPowerMetrics getStorageConsumptionMetrics:maxAge:reply:]_block_invoke.137
+ ___64+[SAPerfPowerMetrics getStorageConsumptionMetrics:maxAge:reply:]_block_invoke.cold.1
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.71
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.71.cold.1
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.72
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e36_v32?0"NSString"8"SAAppSize"16^B24ls32l8
+ ___block_literal_global.117
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.147
+ ___block_literal_global.80
+ ___block_literal_global.88
+ _objc_msgSend$addAppSize:
+ _objc_msgSend$appsDataInternal
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$cacheFilePath
+ _objc_msgSend$cacheIsPurgeable
+ _objc_msgSend$copy
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionary
+ _objc_msgSend$getCacheDict
+ _objc_msgSend$getLastCachedAppSizes:maxAge:reply:
+ _objc_msgSend$isAppUserVisibleForBundleID:
+ _objc_msgSend$longValue
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$setStagedSize:
+ _objc_msgSend$sizeWithFixedSize:dataSize:
+ _objc_msgSend$softwareUpdateDetails
+ _objc_msgSend$stagedSize
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x28
- +[SAAppSize newWithFixedSize:andDataSize:]
- +[SAAppSize newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
- -[SAAppSize initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
- -[SAAppSizerResults updateBundleIDs:fixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
- GCC_except_table50
- GCC_except_table75
- GCC_except_table77
- GCC_except_table78
- GCC_except_table79
- GCC_except_table80
- GCC_except_table93
- ___33+[SASupport getAllAppsUsageTime:]_block_invoke.154
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.112
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.112.cold.1
- ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.180
- ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.180.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.68
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.68.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.69
- ___block_literal_global.114
- ___block_literal_global.123
- ___block_literal_global.142
- ___block_literal_global.144
- ___block_literal_global.153
- ___block_literal_global.86
- ___block_literal_global.94
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$appPathList
- _objc_msgSend$initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:
- _objc_msgSend$isUserVisible
- _objc_msgSend$newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "%s: cache is not in the limit fileAge: %f minAge: %f maxAge: %f"
+ "%s: can't create folder at %@"
+ "%s: failed to write AppSizer cache data to disk with error %@"
+ "%s: successfully cached %lu app sizes"
+ "+[SAAppSizerCacheManager cacheAppSizes:]"
+ "+[SAAppSizerCacheManager getLastCachedAppSizes:maxAge:reply:]"
+ "/var/db/spaceattribution"
+ "/var/db/spaceattribution/AppSizerCache.db"
+ "<%@ fixedSize = %llu, stagedSize = %llu, dataSize = %llu, cloneSize = %llu, purgeableSize = %llu>"
+ "@24@0:8q16"
+ "AppSizer results or appData cannot be nil"
+ "Can't archive AppSizer cache dictionary with %@"
+ "Can't decode AppSizer cache data with %@"
+ "Can't read AppSizer cache data with %@"
+ "Corrupted cache data"
+ "Error getting cached app sizes: %@"
+ "No cached app sizes found"
+ "SAAppSizerCacheManager"
+ "SAPerfPowerMetrics"
+ "Saved AppSizer cache version and current version mismatch"
+ "Successfully processed %lu apps"
+ "T@\"NSDictionary\",&,V_softwareUpdateDetails"
+ "TQ,V_stagedSize"
+ "Unknown"
+ "_softwareUpdateDetails"
+ "_stagedSize"
+ "a"
+ "addAppSize:"
+ "addToSoftwareUpdateDetails:key:"
+ "appSizesDictionary"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "cacheAppSizes:"
+ "cacheFilePath"
+ "cacheSize"
+ "cacheTimestamp"
+ "cacheVersion"
+ "com.apple.fakeapp.SoftwareUpdatePSUS"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithContentsOfFile:options:error:"
+ "dictionary"
+ "getCacheDict"
+ "getLastCachedAppSizes:maxAge:reply:"
+ "getStorageConsumptionMetrics:maxAge:reply:"
+ "isAppUserVisibleForBundleID:"
+ "longValue"
+ "numberWithLong:"
+ "setSoftwareUpdateDetails:"
+ "setStagedSize:"
+ "sizeWithDataSize:purgeableSize:"
+ "sizeWithFixedSize:andDataSize:"
+ "sizeWithFixedSize:dataSize:"
+ "softwareUpdateDetails"
+ "stagedSize"
+ "timeIntervalSince1970"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "updateBundleIDs:fixedSize:stagedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
+ "v40@0:8d16d24@?32"
+ "v96@0:8@16Q24Q32Q40Q48Q56Q64Q72Q80Q88"
+ "withAppCacheSize:"
+ "withCacheDeletePluginSize:"
+ "withCloneFixUpSize:"
+ "withCloneSize:"
+ "withDataSize:"
+ "withFixedSize:"
+ "withPhysicalSize:"
+ "withPurgeableSize:"
+ "writeToFile:options:error:"
- "<%@ fixedSize = %llu, dataSize = %llu, cloneSize = %llu, purgeableSize = %llu>"
- "@80@0:8Q16Q24Q32Q40q48Q56Q64Q72"
- "appPathList"
- "initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
- "isUserVisible"
- "newWithFixedSize:andDataSize:"
- "newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
- "updateBundleIDs:fixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
- "v88@0:8@16Q24Q32Q40Q48Q56Q64Q72Q80"

```
