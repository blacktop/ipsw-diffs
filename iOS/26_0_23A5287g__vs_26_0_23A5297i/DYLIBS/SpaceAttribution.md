## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-444.0.0.0.0
-  __TEXT.__text: 0xfc74
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x11e8
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0xe55
-  __TEXT.__gcc_except_tab: 0x6b0
-  __TEXT.__oslogstring: 0xb9b
-  __TEXT.__unwind_info: 0x540
-  __TEXT.__objc_classname: 0x165
-  __TEXT.__objc_methname: 0x29ba
-  __TEXT.__objc_methtype: 0x6e2
-  __TEXT.__objc_stubs: 0x1a40
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x400
-  __DATA_CONST.__objc_classlist: 0x98
+446.0.0.0.1
+  __TEXT.__text: 0x13814
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x13b8
+  __TEXT.__const: 0x160
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__cstring: 0x11b3
+  __TEXT.__oslogstring: 0x1222
+  __TEXT.__unwind_info: 0x628
+  __TEXT.__objc_classname: 0x16f
+  __TEXT.__objc_methname: 0x2fb8
+  __TEXT.__objc_methtype: 0x7ae
+  __TEXT.__objc_stubs: 0x1ee0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
+  __DATA_CONST.__objc_selrefs: 0xd30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0x1cb8
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x320
+  __DATA_CONST.__objc_arraydata: 0x138
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x1280
+  __AUTH_CONST.__objc_const: 0x1d48
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x180
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x20
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D3060DC-0E8B-37FE-8136-695D74B09DE7
-  Functions: 478
-  Symbols:   1608
-  CStrings:  987
+  UUID: 2FF4E196-E073-30CC-8C49-CBEC7BB7E01F
+  Functions: 565
+  Symbols:   1877
+  CStrings:  1142
 
Symbols:
+ +[SASupport buildVersion]
+ +[SASupport buildVersion].cold.1
+ +[SASupport calculateMovingSumFor:with:numOfSamples:windowLength:]
+ +[SASupport enableDirStatInfoForPath:orFD:withOptions:andGetInfo:]
+ +[SASupport enableDirStatsForPath:orFD:withOptions:]
+ +[SASupport enableDirStatsForPath:orFD:withOptions:].cold.1
+ +[SASupport getAllAppsUsageTime:]
+ +[SASupport getCloneDstreamIDForPath:]
+ +[SASupport getCloneDstreamIDForPath:].cold.1
+ +[SASupport getDirStatInfoForPath:orFD:withOptions:info:]
+ +[SASupport getDirStatInfoForPath:orFD:withOptions:info:].cold.1
+ +[SASupport getDirStatInfoForPath:orFD:withOptions:info:].cold.2
+ +[SASupport getDirStatKeyForOriginID:ofMount:]
+ +[SASupport getDirStatKeyForOriginID:ofMount:].cold.1
+ +[SASupport getDiskCapacity]
+ +[SASupport getDiskCapacity].cold.1
+ +[SASupport getDiskCapacity].cold.2
+ +[SASupport getDiskCapacity].cold.3
+ +[SASupport getDiskCapacity].cold.4
+ +[SASupport getDiskCapacity].cold.5
+ +[SASupport getDiskCapacity].cold.6
+ +[SASupport getDiskCapacity].cold.7
+ +[SASupport getDiskCapacity].cold.8
+ +[SASupport getDiskCapacity].cold.9
+ +[SASupport getDiskUsed]
+ +[SASupport getDiskUsed].cold.1
+ +[SASupport getDiskUsed].cold.2
+ +[SASupport getEnterpriseVolumesPaths]
+ +[SASupport getEnterpriseVolumesPaths].cold.1
+ +[SASupport getFSPurgeableDataOnVolumes:]
+ +[SASupport getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:]
+ +[SASupport getInodeForDirStatKey:volumePath:]
+ +[SASupport getInodeForDirStatKey:volumePath:].cold.1
+ +[SASupport getInodeIDForPath:]
+ +[SASupport getInodeIDForPath:].cold.1
+ +[SASupport getLSAppRecordForBundle:reply:]
+ +[SASupport getPathForDirStatKey:volumePath:]
+ +[SASupport getPathOfNodeID:FSid:]
+ +[SASupport getPathOfNodeID:FSid:].cold.1
+ +[SASupport getPathOfiNode:inVolume:]
+ +[SASupport getPathOfiNode:inVolume:].cold.1
+ +[SASupport getRelevantVolumes]
+ +[SASupport getRelevantVolumes].cold.1
+ +[SASupport getResolvedPath:]
+ +[SASupport getResolvedPathForFD:]
+ +[SASupport getResolvedPathForFD:].cold.1
+ +[SASupport getResolvedURL:]
+ +[SASupport getResolvedURL:].cold.1
+ +[SASupport getURLMountPoint:]
+ +[SASupport getURLMountPoint:].cold.1
+ +[SASupport getVolSizeFromAttrList:completionHandler:]
+ +[SASupport getVolSizeFromAttrList:completionHandler:].cold.1
+ +[SASupport getVolumesPaths]
+ +[SASupport getVolumesPaths].cold.1
+ +[SASupport getiCloudPlanSizeGB]
+ +[SASupport getiCloudPlanSizeGB].cold.1
+ +[SASupport isFileCloned:]
+ +[SASupport isFileCloned:].cold.1
+ +[SASupport isFilePurgeable:]
+ +[SASupport isFilePurgeable:].cold.1
+ +[SASupport isItemMountedOnSystemVolume:]
+ +[SASupport isItemMountedOnSystemVolume:].cold.1
+ +[SASupport isSDHierarchyEnabledForPath:orFD:]
+ +[SASupport isSDHierarchyEnabledForPath:orFD:].cold.1
+ +[SASupport shouldExcludeCacheSizeForBundle:]
+ +[SASupport shouldExcludeCacheSizeForBundle:].cold.1
+ +[SASupport targetDeviceIsHomePod]
+ +[SASupport targetDeviceIsHomePod].cold.1
+ +[SASupport targetDeviceIsIpad]
+ +[SASupport targetDeviceIsIpad].cold.1
+ +[SASupport targetDeviceIsWatch]
+ +[SASupport targetDeviceIsWatch].cold.1
+ +[SASupport volumeSupportsAttributionTags:]
+ +[SASupport volumeSupportsAttributionTags:].cold.1
+ +[SASupport volumeSupportsAttributionTags:].cold.2
+ +[SASupport volumeSupportsCloneGroups:]
+ +[SASupport volumeSupportsCloneGroups:].cold.1
+ +[SASupport volumeSupportsCloneMapping:]
+ +[SASupport volumeSupportsCloneMapping:].cold.1
+ +[SASupport volumeSupportsCloneMapping:].cold.2
+ GCC_except_table50
+ _BiomeLibrary
+ _MGCopyAnswer
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_ACAccount
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_BPSPublisher
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_SASupport
+ _OBJC_METACLASS_$_SASupport
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_SASupport
+ __OBJC_CLASS_RO_$_SASupport
+ __OBJC_METACLASS_RO_$_SASupport
+ ___25+[SASupport buildVersion]_block_invoke
+ ___28+[SASupport getVolumesPaths]_block_invoke
+ ___28+[SASupport getVolumesPaths]_block_invoke.cold.1
+ ___31+[SASupport getRelevantVolumes]_block_invoke
+ ___31+[SASupport getRelevantVolumes]_block_invoke.cold.1
+ ___31+[SASupport targetDeviceIsIpad]_block_invoke
+ ___32+[SASupport targetDeviceIsWatch]_block_invoke
+ ___33+[SASupport getAllAppsUsageTime:]_block_invoke
+ ___33+[SASupport getAllAppsUsageTime:]_block_invoke.154
+ ___34+[SASupport targetDeviceIsHomePod]_block_invoke
+ ___block_descriptor_32_e23_v16?0"BPSCompletion"8l
+ ___block_descriptor_56_e8_32s40r48r_e22_v16?0"BMStoreEvent"8lr40l8r48l8s32l8
+ ___block_literal_global.123
+ ___block_literal_global.142
+ ___block_literal_global.144
+ ___block_literal_global.153
+ ___block_literal_global.86
+ ___block_literal_global.94
+ _buildVersion.buildVersion
+ _buildVersion.onceToken
+ _ffsctl
+ _fgetattrlist
+ _free
+ _fsctl
+ _fsgetpath
+ _getEnterpriseVolumesPaths.enterpriseVolumesPaths
+ _getRelevantVolumes.onceToken
+ _getRelevantVolumes.relevantVolumes
+ _getVolumesPaths.onceToken
+ _getVolumesPaths.volumesPaths
+ _getmntinfo_r_np
+ _objc_msgSend$App
+ _objc_msgSend$InFocus
+ _objc_msgSend$aa_lastKnownQuota
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$defaultStore
+ _objc_msgSend$doubleValue
+ _objc_msgSend$enableDirStatsForPath:orFD:withOptions:
+ _objc_msgSend$error
+ _objc_msgSend$eventBody
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$getDirStatInfoForPath:orFD:withOptions:info:
+ _objc_msgSend$getDiskCapacity
+ _objc_msgSend$getDiskUsed
+ _objc_msgSend$getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:
+ _objc_msgSend$getInodeForDirStatKey:volumePath:
+ _objc_msgSend$getPathOfiNode:inVolume:
+ _objc_msgSend$getRelevantVolumes
+ _objc_msgSend$getResolvedURL:
+ _objc_msgSend$getVolumesPaths
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isSDHierarchyEnabledForPath:orFD:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$publisherWithOptions:
+ _objc_msgSend$sinkWithCompletion:receiveInput:
+ _objc_msgSend$starting
+ _objc_msgSend$state
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timestamp
+ _objc_msgSend$valueForKey:
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _stat
+ _strerror
+ _targetDeviceIsHomePod.isHomePod
+ _targetDeviceIsHomePod.onceToken
+ _targetDeviceIsIpad.isiPad
+ _targetDeviceIsIpad.onceToken
+ _targetDeviceIsWatch.isWatch
+ _targetDeviceIsWatch.onceToken
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.10
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.11
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.12
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.2
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.3
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.4
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.5
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.6
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.7
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.8
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.9
CStrings:
+ "%@: Failed to get FSPurgeable data of urgency (%llu) with error: %s"
+ "%s: Can't get volume size for %s (err %li)"
+ "%s: Failed to get path (%s) mount point with error %d (%s)"
+ "%s: Failed to resolve item fd (%d) with error %d (%s)"
+ "%s: Failed to resolve path (%s) with error %d (%s)"
+ "%s: Invalid VOL_CAP_FMT_CLONE_MAPPING flag for volume %@"
+ "%s: Invalid VOL_CAP_INT_ATTRIBUTION_TAG flag for volume %@"
+ "%s: No path neither FD was provided"
+ "%s: statfs failed for %@ with error %s"
+ "%s:%s:used:%llu:reserved:%llu:capacity:%llu"
+ "+[SASupport enableDirStatsForPath:orFD:withOptions:]"
+ "+[SASupport getDirStatInfoForPath:orFD:withOptions:info:]"
+ "+[SASupport getDiskCapacity]"
+ "+[SASupport getDiskUsed]"
+ "+[SASupport getResolvedPathForFD:]"
+ "+[SASupport getResolvedURL:]"
+ "+[SASupport getURLMountPoint:]"
+ "+[SASupport getVolSizeFromAttrList:completionHandler:]"
+ "+[SASupport isItemMountedOnSystemVolume:]"
+ "+[SASupport isSDHierarchyEnabledForPath:orFD:]"
+ "+[SASupport volumeSupportsAttributionTags:]"
+ "+[SASupport volumeSupportsCloneMapping:]"
+ "@20@0:8i16"
+ "@32@0:8Q16@24"
+ "@32@0:8Q16^{fsid=[2i]}24"
+ "APFSIOC_CLONEGROUP_ITERATE returned with unexpected error %s"
+ "APFSIOC_DIR_STATS_OP : DIR_STATS_OP_SET failed for fd %@ : %s"
+ "APFSIOC_DIR_STATS_OP: DIR_STATS_OP_GET failed for %@ : %s"
+ "APFSIOC_GET_VOLUME_ROLE returned with error: %s"
+ "APFS_PURGEABLE_HIGH_URGENCY"
+ "APFS_PURGEABLE_LOW_URGENCY"
+ "APFS_PURGEABLE_MED_URGENCY"
+ "APFS_PURGEABLE_SU_URGENCY"
+ "App"
+ "B24@0:8r*16"
+ "B28@0:8@16i24"
+ "DeviceName"
+ "Dir-stats for %@ does not have SD hierarchy"
+ "DirStatForOriginID: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
+ "Enabled APFSIOC_DIR_STATS_OP for %@"
+ "Failed to GET speculative download hierarchy info for %@ with error %d (%s)"
+ "Failed to get volume (%@) attribution tag capability"
+ "Failed to get volume (%@) clone mapping capability"
+ "Failed to stat path %@"
+ "Failed to stat volume %@ with error %d (%s)"
+ "HomePod"
+ "INodeForDirStatKey: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
+ "InFocus"
+ "NO_RESPECT_0_SIZE"
+ "No ACAccount classes implemented."
+ "Q32@0:8Q16*24"
+ "Q32@0:8Q16r*24"
+ "Q36@0:8@16Q24B32"
+ "Q48@0:8Q16Q24Q32Q40"
+ "RESPECT_0_SIZE"
+ "SASupport"
+ "Skipping excluded id %@"
+ "SupplementalBuildVersion"
+ "aa_lastKnownQuota"
+ "aa_primaryAppleAccount"
+ "buildVersion"
+ "calculateMovingSumFor:with:numOfSamples:windowLength:"
+ "com.apple.GameCenterUI"
+ "com.apple.InCallService"
+ "com.apple.MobileSMS"
+ "com.apple.PassbookUIService"
+ "com.apple.mobilemail"
+ "date"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "defaultStore"
+ "dir-stat for %@ (attributes 0x%llx) does not count clones and purgeables."
+ "dir-stat for %@ (flags 0x%llx) is not in saf mode."
+ "dir-stats for %@ is possibly inconsistent."
+ "doubleValue"
+ "enableDirStatInfoForPath:orFD:withOptions:andGetInfo:"
+ "enableDirStatsForPath:orFD:withOptions:"
+ "error"
+ "eventBody"
+ "fileURLWithPath:isDirectory:"
+ "fsctl APFSIOC_GET_CLONE_INFO failed with error: %s"
+ "fsctl APFSIOC_GET_PURGEABLE_FILE_FLAGS failed with error: %s"
+ "fsgetpath returned errno %d for nodeID %llu"
+ "getAllAppsUsageTime:"
+ "getCloneDstreamIDForPath:"
+ "getDirStatInfoForPath:orFD:withOptions:info:"
+ "getDirStatKeyForOriginID:ofMount:"
+ "getDiskCapacity"
+ "getDiskUsed"
+ "getEnterpriseVolumesPaths"
+ "getFSPurgeableDataOnVolumes:"
+ "getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:"
+ "getInodeForDirStatKey:volumePath:"
+ "getInodeIDForPath:"
+ "getLSAppRecordForBundle:reply:"
+ "getPathForDirStatKey:volumePath:"
+ "getPathOfNodeID:FSid:"
+ "getPathOfiNode:inVolume:"
+ "getRelevantVolumes"
+ "getResolvedPath:"
+ "getResolvedPathForFD:"
+ "getResolvedURL:"
+ "getURLMountPoint:"
+ "getVolSizeFromAttrList:completionHandler:"
+ "getVolumesPaths"
+ "getiCloudPlanSizeGB"
+ "i36@0:8@16i24q28"
+ "i44@0:8@16i24q28^{?=QQQQQ}36"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "intValue"
+ "isEqualToString:"
+ "isFileCloned:"
+ "isFilePurgeable:"
+ "isItemMountedOnSystemVolume:"
+ "isSDHierarchyEnabledForPath:orFD:"
+ "mtrAoWJ3gsq+I90ZnQ0vQw"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "publisherWithOptions:"
+ "shouldExcludeCacheSizeForBundle:"
+ "sinkWithCompletion:receiveInput:"
+ "starting"
+ "state"
+ "stringWithCString:encoding:"
+ "stringWithUTF8String:"
+ "subscribeToAppInFocusStreamBeginning completion: %ld %@"
+ "targetDeviceIsHomePod"
+ "targetDeviceIsIpad"
+ "targetDeviceIsWatch"
+ "timeIntervalSinceDate:"
+ "timestamp"
+ "unable to get mounts: %s (%d)\n"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v32@0:8r*16@?24"
+ "valueForKey:"
+ "volumeSupportsAttributionTags:"
+ "volumeSupportsCloneGroups:"
+ "volumeSupportsCloneMapping:"

```
