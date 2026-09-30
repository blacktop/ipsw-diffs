## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/Versions/A/SpaceAttribution`

```diff

-322.80.5.0.1
-  __TEXT.__text: 0x128b4
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x1088
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__cstring: 0xe0f
-  __TEXT.__oslogstring: 0xfab
-  __TEXT.__unwind_info: 0x5d0
-  __TEXT.__objc_classname: 0x170
-  __TEXT.__objc_methname: 0x2a37
-  __TEXT.__objc_methtype: 0x804
-  __TEXT.__objc_stubs: 0x1b20
-  __DATA_CONST.__got: 0x118
+322.100.57.0.0
+  __TEXT.__text: 0x1009c
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x1138
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0xd71
+  __TEXT.__gcc_except_tab: 0x62c
+  __TEXT.__oslogstring: 0x9b7
+  __TEXT.__unwind_info: 0x548
+  __TEXT.__objc_classname: 0x162
+  __TEXT.__objc_methname: 0x27ee
+  __TEXT.__objc_methtype: 0x6ce
+  __TEXT.__objc_stubs: 0x1980
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xad0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0xf20
-  __AUTH_CONST.__objc_const: 0x1ee0
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x110
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0x180
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
-  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/DiskImages2
-  - /System/Library/PrivateFrameworks/StorageKit.framework/Versions/A/StorageKit
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90E17ECB-FF92-3A10-AA2F-B912318BED8E
-  Functions: 523
-  Symbols:   1177
-  CStrings:  1003
+  UUID: B91AD110-F9D0-3467-90AC-25D9218CA7B7
+  Functions: 471
+  Symbols:   1075
+  CStrings:  937
 
Symbols:
+ +[SABGSystemTask newWithBGTask:]
+ +[SAInternalAPI adjustDenomAgeBy:reply:]
+ +[SAInternalAPI setForceSDAAbort:]
+ +[SAUtilities processArrayConcurrently:number:queue:group:block:]
+ +[SAUtilities processArrayConcurrently:number:queue:group:block:].cold.1
+ +[SAUtilities splitArray:into:].cold.3
+ -[SAAppSizerResults collectPathSizeInfo:info:]
+ -[SAAppSizerResults getPhySizeForAppSet:]
+ -[SAAppSizerResults rawDiskedUsed]
+ -[SAAppSizerResults rawSystemDataSize]
+ -[SAAppSizerResults setRawDiskedUsed:]
+ -[SAAppSizerResults setRawSystemDataSize:]
+ -[SAAppSizerResults setTotalCDAppsCacheSize:]
+ -[SAAppSizerResults setTotalCDPluginsSize:]
+ -[SAAppSizerResults setTotalPurgeableDataSize:]
+ -[SAAppSizerResults setTotalSAFAppsCacheSize:]
+ -[SAAppSizerResults setTotalSAFPluginsSize:]
+ -[SAAppSizerResults systemApp]
+ -[SAAppSizerResults systemDataApp]
+ -[SAAppSizerResults totalCDAppsCacheSize]
+ -[SAAppSizerResults totalCDPluginsSize]
+ -[SAAppSizerResults totalPurgeableDataSize]
+ -[SAAppSizerResults totalSAFAppsCacheSize]
+ -[SAAppSizerResults totalSAFPluginsSize]
+ -[SABGSystemTask .cxx_destruct]
+ -[SABGSystemTask deferTask]
+ -[SABGSystemTask initWithBGTask:]
+ -[SABGSystemTask setTask:]
+ -[SABGSystemTask shouldDefer]
+ -[SABGSystemTask task]
+ GCC_except_table106
+ GCC_except_table2
+ GCC_except_table34
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table69
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table92
+ OBJC_IVAR_$_SAAppSizerResults._rawDiskedUsed
+ OBJC_IVAR_$_SAAppSizerResults._rawSystemDataSize
+ OBJC_IVAR_$_SAAppSizerResults._systemApp
+ OBJC_IVAR_$_SAAppSizerResults._systemDataApp
+ OBJC_IVAR_$_SAAppSizerResults._totalCDAppsCacheSize
+ OBJC_IVAR_$_SAAppSizerResults._totalCDPluginsSize
+ OBJC_IVAR_$_SAAppSizerResults._totalPurgeableDataSize
+ OBJC_IVAR_$_SAAppSizerResults._totalSAFAppsCacheSize
+ OBJC_IVAR_$_SAAppSizerResults._totalSAFPluginsSize
+ OBJC_IVAR_$_SABGSystemTask._shouldDefer
+ OBJC_IVAR_$_SABGSystemTask._task
+ SALog.cold.1
+ _OBJC_CLASS_$_SABGSystemTask
+ _OBJC_METACLASS_$_SABGSystemTask
+ __38-[SADaemonXPC setInvalidationHandler:]_block_invoke.104
+ __38-[SADaemonXPC setInvalidationHandler:]_block_invoke.104.cold.1
+ __63+[SAInternalAPI setAppSizerFilteringOptionsToDefaultWithReply:]_block_invoke.56
+ __OBJC_$_CLASS_METHODS_SABGSystemTask
+ __OBJC_$_INSTANCE_METHODS_SABGSystemTask
+ __OBJC_$_INSTANCE_VARIABLES_SABGSystemTask
+ __OBJC_$_PROP_LIST_SABGSystemTask
+ __OBJC_CLASS_RO_$_SABGSystemTask
+ __OBJC_METACLASS_RO_$_SABGSystemTask
+ ___34+[SAInternalAPI setForceSDAAbort:]_block_invoke
+ ___34+[SAInternalAPI setForceSDAAbort:]_block_invoke_2
+ ___34+[SAInternalAPI setForceSDAAbort:]_block_invoke_3
+ ___40+[SAInternalAPI adjustDenomAgeBy:reply:]_block_invoke
+ ___40+[SAInternalAPI adjustDenomAgeBy:reply:]_block_invoke_2
+ ___40+[SAInternalAPI adjustDenomAgeBy:reply:]_block_invoke_3
+ ___65+[SAUtilities processArrayConcurrently:number:queue:group:block:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b
+ ___destroy_helper_block_e8_32s40s48s
+ __block_literal_global.106
+ _dispatch_async
+ _objc_msgSend$adjustDenomAgeBy:reply:
+ _objc_msgSend$initWithBGTask:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$rawDiskedUsed
+ _objc_msgSend$rawSystemDataSize
+ _objc_msgSend$setForceSDAAbort:
+ _objc_msgSend$splitArray:into:
+ _objc_msgSend$totalCDAppsCacheSize
+ _objc_msgSend$totalCDPluginsSize
+ _objc_msgSend$totalPurgeableDataSize
+ _objc_msgSend$totalSAFAppsCacheSize
+ _objc_msgSend$totalSAFPluginsSize
- +[SAActivity newWithActivity:andCompletionHandler:]
- +[SAInternalAPI computeSizeOfVolumeAtURL:options:completionHandler:]
- +[SASupport enableDirStatInfoForPath:withOptions:andGetInfo:]
- +[SASupport enableDirStatsForPath:withOptions:]
- +[SASupport enableDirStatsForPath:withOptions:].cold.1
- +[SASupport enableDirStatsForPath:withOptions:].cold.2
- +[SASupport getCloneDstreamIDForPath:]
- +[SASupport getCloneDstreamIDForPath:].cold.1
- +[SASupport getDirStatInfoForPath:withOptions:info:]
- +[SASupport getDirStatInfoForPath:withOptions:info:].cold.1
- +[SASupport getDirStatInfoForPath:withOptions:info:].cold.2
- +[SASupport getDirStatInfoForPath:withOptions:info:].cold.3
- +[SASupport getDirStatInfoForPath:withOptions:info:].cold.4
- +[SASupport getDirStatInfoForPath:withOptions:info:].cold.5
- +[SASupport getDirStatKeyForOriginID:ofMount:]
- +[SASupport getDirStatKeyForOriginID:ofMount:].cold.1
- +[SASupport getEnterpriseVolumesPaths]
- +[SASupport getEnterpriseVolumesPaths].cold.1
- +[SASupport getFSPurgeableDataOnVolumes:]
- +[SASupport getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:]
- +[SASupport getINodeForDirStatKey:ofMount:]
- +[SASupport getINodeForDirStatKey:ofMount:].cold.1
- +[SASupport getInodeIDForPath:]
- +[SASupport getInodeIDForPath:].cold.1
- +[SASupport getLSAppRecordForBundle:reply:]
- +[SASupport getPathOfNodeID:FSid:]
- +[SASupport getPathOfNodeID:FSid:].cold.1
- +[SASupport getPathOfiNode:inVolume:]
- +[SASupport getResolvedURL:]
- +[SASupport getResolvedURL:].cold.1
- +[SASupport getURLMountPoint:]
- +[SASupport getURLMountPoint:].cold.1
- +[SASupport getVolSizeFromAttrList:completionHandler:]
- +[SASupport getVolSizeFromAttrList:completionHandler:].cold.1
- +[SASupport getVolumesPaths]
- +[SASupport isFileCloned:]
- +[SASupport isFileCloned:].cold.1
- +[SASupport isFilePurgeable:]
- +[SASupport isFilePurgeable:].cold.1
- +[SASupport isItemMountedOnSystemVolume:]
- +[SASupport isItemMountedOnSystemVolume:].cold.1
- +[SASupport markTimeEndForPhase:]
- +[SASupport markTimeEndForPhase:].cold.1
- +[SASupport markTimeStartForPhase:]
- +[SASupport targetDeviceIsHomePod]
- +[SASupport targetDeviceIsIpad]
- +[SASupport targetDeviceIsWatch]
- +[SASupport volumeSupportsAttributionTags:]
- +[SASupport volumeSupportsAttributionTags:].cold.1
- +[SASupport volumeSupportsAttributionTags:].cold.2
- +[SASupport volumeSupportsCloneMapping:]
- +[SASupport volumeSupportsCloneMapping:].cold.1
- +[SASupport volumeSupportsCloneMapping:].cold.2
- -[SAActivity .cxx_destruct]
- -[SAActivity activity]
- -[SAActivity completionHandler]
- -[SAActivity deferActivity]
- -[SAActivity initWithActivity:completionHandler:]
- -[SAActivity setActivity:]
- -[SAActivity setActivityResult:]
- -[SAActivity setCompletionHandler:]
- -[SAActivity setDeferActivity:]
- -[SAActivity setShouldStop:]
- -[SAActivity shouldDefer]
- -[SAActivity shouldStop]
- -[SAAppSizerResults addSystemVolumeWithCapacity:used:withReplyBlock:]
- -[SAAppSizerResults addSystemVolumeWithCapacity:used:withReplyBlock:].cold.1
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.4
- -[SAAppSizerResults initDiskUsedAndCapacity].cold.5
- -[SAAppSizerResults setDiskUsed:andCapacity:]
- -[SATimeVal getTimeValAddr]
- -[SATimeVal setTimeVal:]
- -[SATimeVal timeVal]
- GCC_except_table25
- GCC_except_table26
- GCC_except_table35
- GCC_except_table38
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- GCC_except_table80
- GCC_except_table83
- GCC_except_table89
- GCC_except_table9
- OBJC_IVAR_$_SAActivity._activity
- OBJC_IVAR_$_SAActivity._completionHandler
- OBJC_IVAR_$_SAActivity._deferActivity
- OBJC_IVAR_$_SAActivity._shouldStop
- OBJC_IVAR_$_SATimeVal._timeVal
- _MGCopyAnswer
- _OBJC_CLASS_$_DIIOMedia
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_SAActivity
- _OBJC_CLASS_$_SASupport
- _OBJC_CLASS_$_SATimeVal
- _OBJC_CLASS_$_SKManager
- _OBJC_METACLASS_$_SAActivity
- _OBJC_METACLASS_$_SASupport
- _OBJC_METACLASS_$_SATimeVal
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __28+[SASupport getVolumesPaths]_block_invoke.cold.1
- __38-[SADaemonXPC setInvalidationHandler:]_block_invoke.103
- __38-[SADaemonXPC setInvalidationHandler:]_block_invoke.103.cold.1
- __63+[SAInternalAPI setAppSizerFilteringOptionsToDefaultWithReply:]_block_invoke.59
- __OBJC_$_CLASS_METHODS_SAActivity
- __OBJC_$_CLASS_METHODS_SASupport
- __OBJC_$_INSTANCE_METHODS_SAActivity
- __OBJC_$_INSTANCE_METHODS_SATimeVal
- __OBJC_$_INSTANCE_VARIABLES_SAActivity
- __OBJC_$_INSTANCE_VARIABLES_SATimeVal
- __OBJC_$_PROP_LIST_SAActivity
- __OBJC_$_PROP_LIST_SATimeVal
- __OBJC_CLASS_RO_$_SAActivity
- __OBJC_CLASS_RO_$_SASupport
- __OBJC_CLASS_RO_$_SATimeVal
- __OBJC_METACLASS_RO_$_SAActivity
- __OBJC_METACLASS_RO_$_SASupport
- __OBJC_METACLASS_RO_$_SATimeVal
- ___28+[SASupport getVolumesPaths]_block_invoke
- ___31+[SASupport targetDeviceIsIpad]_block_invoke
- ___32+[SASupport targetDeviceIsWatch]_block_invoke
- ___34+[SASupport targetDeviceIsHomePod]_block_invoke
- ___68+[SAInternalAPI computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke
- ___68+[SAInternalAPI computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke_2
- ___68+[SAInternalAPI computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke_3
- ___block_descriptor_48_e8_32bs40r_e38_v24?0"SAVolumeSizeInfo"8"NSError"16l
- __block_literal_global.105
- __block_literal_global.126
- __block_literal_global.87
- __block_literal_global.96
- _free
- _fsctl
- _fsgetpath
- _getmntinfo_r_np
- _gettimeofday
- _objc_copyStruct
- _objc_msgSend$container
- _objc_msgSend$copyPropertyWithClass:key:
- _objc_msgSend$designatedPhysicalStore
- _objc_msgSend$diskForPath:
- _objc_msgSend$diskIdentifier
- _objc_msgSend$enableDirStatsForPath:withOptions:
- _objc_msgSend$fileURLWithPath:isDirectory:
- _objc_msgSend$getDirStatInfoForPath:withOptions:info:
- _objc_msgSend$getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:
- _objc_msgSend$getTimeValAddr
- _objc_msgSend$getVolumesPaths
- _objc_msgSend$initWithActivity:completionHandler:
- _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
- _objc_msgSend$initWithDevName:error:
- _objc_msgSend$intValue
- _objc_msgSend$isEqualToString:
- _objc_msgSend$mountedOn
- _objc_msgSend$shouldDefer
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$syncSharedManager
- _objc_msgSend$timeVal
- _objc_msgSend$used
- _objc_msgSend$valueForKey:
- _objc_msgSend$wholeDiskForDisk:
- _objc_retainBlock
- _stat
- _strerror
- _timesDict
- getEnterpriseVolumesPaths.enterpriseVolumesPaths
- getVolumesPaths.onceToken
- getVolumesPaths.volumesPaths
- targetDeviceIsHomePod.isHomePod
- targetDeviceIsHomePod.onceToken
- targetDeviceIsIpad.isiPad
- targetDeviceIsIpad.onceToken
- targetDeviceIsWatch.isWatch
- targetDeviceIsWatch.onceToken
CStrings:
+ "%s: Volume %@, %@ %@"
+ "%s: supplied array in nil"
+ "@\"BGSystemTask\""
+ "@\"SAAppSize\""
+ "Failed to split array (count: %ld) to %d parts. Bailing out"
+ "RawDiskedUsed"
+ "RawSystemDataSize"
+ "SABGSystemTask"
+ "T@\"BGSystemTask\",&,V_task"
+ "T@\"SAAppSize\",R,V_systemApp"
+ "T@\"SAAppSize\",R,V_systemDataApp"
+ "TB,R,V_shouldDefer"
+ "TQ,V_rawDiskedUsed"
+ "TQ,V_totalCDAppsCacheSize"
+ "TQ,V_totalCDPluginsSize"
+ "TQ,V_totalPurgeableDataSize"
+ "TQ,V_totalSAFAppsCacheSize"
+ "TQ,V_totalSAFPluginsSize"
+ "TotalCDAppsCacheSize"
+ "TotalCDPluginsSize"
+ "TotalPurgeableDataSize"
+ "TotalSAFAppsCacheSize"
+ "TotalSAFPluginsSize"
+ "Tq,V_rawSystemDataSize"
+ "Unable to get %@, purgeable size is set to 0: %@"
+ "_rawDiskedUsed"
+ "_rawSystemDataSize"
+ "_shouldDefer"
+ "_systemApp"
+ "_systemDataApp"
+ "_task"
+ "_totalCDAppsCacheSize"
+ "_totalCDPluginsSize"
+ "_totalPurgeableDataSize"
+ "_totalSAFAppsCacheSize"
+ "_totalSAFPluginsSize"
+ "adjustDenomAgeBy:reply:"
+ "collectPathSizeInfo:info:"
+ "deferTask"
+ "getPhySizeForAppSet:"
+ "initWithBGTask:"
+ "newWithBGTask:"
+ "numberWithLongLong:"
+ "processArrayConcurrently:number:queue:group:block:"
+ "rawDiskedUsed"
+ "rawSystemDataSize"
+ "setForceSDAAbort:"
+ "setRawDiskedUsed:"
+ "setRawSystemDataSize:"
+ "setTask:"
+ "setTotalCDAppsCacheSize:"
+ "setTotalCDPluginsSize:"
+ "setTotalPurgeableDataSize:"
+ "setTotalSAFAppsCacheSize:"
+ "setTotalSAFPluginsSize:"
+ "systemApp"
+ "systemDataApp"
+ "task"
+ "totalCDAppsCacheSize"
+ "totalCDPluginsSize"
+ "totalPurgeableDataSize"
+ "totalSAFAppsCacheSize"
+ "totalSAFPluginsSize"
+ "v52@0:8@16i24@28@36@?44"
- "%@: Failed to get FSPurgeable data of urgency (%llu) with error: %s"
- "%s: Can't get volume size for %s (err %li)"
- "%s: Failed to get path (%s) mount point with error %d (%s)"
- "%s: Failed to resolve path (%s) with error %d (%s)"
- "%s: Invalid VOL_CAP_FMT_CLONE_MAPPING flag for volume %@"
- "%s: Invalid VOL_CAP_INT_ATTRIBUTION_TAG flag for volume %@"
- "%s: Volume %@, CACHE_DELETE_TOTAL_AVAILABLE %@"
- "%s: statfs failed for %@ with error %s"
- "%s:%s: Failed to find %@ in the registry: %@"
- "%s:%s: Failed to find size of disk0"
- "%s:%s:used:%llu:reserved:%llu:capacity:%llu"
- "'System' not found, creating"
- "+[SASupport getResolvedURL:]"
- "+[SASupport getURLMountPoint:]"
- "+[SASupport getVolSizeFromAttrList:completionHandler:]"
- "+[SASupport isItemMountedOnSystemVolume:]"
- "+[SASupport volumeSupportsAttributionTags:]"
- "+[SASupport volumeSupportsCloneMapping:]"
- "@\"NSBackgroundActivityScheduler\""
- "@32@0:8@16@?24"
- "@32@0:8Q16^{fsid=[2i]}24"
- "@32@0:8Q16^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}24"
- "APFSIOC_DIR_STATS_OP : DIR_STATS_OP_SET failed for %s : %s"
- "APFSIOC_DIR_STATS_OP: DIR_STATS_OP_GET failed for %@ : %s"
- "APFSIOC_GET_VOLUME_ROLE returned with error: %s"
- "APFS_PURGEABLE_HIGH_URGENCY"
- "APFS_PURGEABLE_LOW_URGENCY"
- "APFS_PURGEABLE_MED_URGENCY"
- "APFS_PURGEABLE_SU_URGENCY"
- "Adding for %@ - data size: %llu, fixed size: %llu"
- "B24@0:8r*16"
- "DeviceName"
- "DirStatForOriginID: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "END: App Sizer %@ (%lf)"
- "END: Unknown phase %@"
- "Enabled APFSIOC_DIR_STATS_OP for %s with flags 0x%llx"
- "Failed to get volume (%@) attribution tag capability"
- "Failed to get volume (%@) clone mapping capability"
- "Failed to stat path %@"
- "HomePod"
- "INodeForDirStatKey: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "K#"
- "NO_RESPECT_0_SIZE"
- "Q32@0:8Q16*24"
- "Q36@0:8@16Q24B32"
- "RESPECT_0_SIZE"
- "Root volume disk: %@"
- "SAActivity"
- "SASupport"
- "SATimeVal"
- "START: App Sizer %@"
- "Size"
- "T@\"NSBackgroundActivityScheduler\",&,V_activity"
- "T@?,C,V_completionHandler"
- "TB,V_deferActivity"
- "TB,V_shouldStop"
- "T{timeval=qi},V_timeVal"
- "Unable to get CACHE_DELETE_TOTAL_AVAILABLE, purgeable size is set to 0: %@"
- "^{timeval=qi}16@0:8"
- "_activity"
- "_completionHandler"
- "_deferActivity"
- "_shouldStop"
- "_timeVal"
- "activity"
- "addSystemVolumeWithCapacity:used:withReplyBlock:"
- "completionHandler"
- "container"
- "copyPropertyWithClass:key:"
- "deferActivity"
- "designatedPhysicalStore"
- "dir-stat for %@ (attributes 0x%llx) does not count clones and purgeables."
- "dir-stat for %@ (flags 0x%llx) is not in saf mode."
- "dir-stats for %@ does not have hierarchy on (0x%llx)."
- "dir-stats for %@ is possibly inconsistent."
- "diskForPath:"
- "diskIdentifier"
- "enableDirStatInfoForPath:withOptions:andGetInfo:"
- "enableDirStatsForPath:withOptions:"
- "fileURLWithPath:isDirectory:"
- "fsctl APFSIOC_GET_CLONE_INFO failed with error: %s"
- "fsctl APFSIOC_GET_PURGEABLE_FILE_FLAGS failed with error: %s"
- "fsgetpath returned errno %d for nodeID %llu"
- "getCloneDstreamIDForPath:"
- "getDirStatInfoForPath:withOptions:info:"
- "getDirStatKeyForOriginID:ofMount:"
- "getEnterpriseVolumesPaths"
- "getFSPurgeableDataOnVolumes:"
- "getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:"
- "getINodeForDirStatKey:ofMount:"
- "getInodeIDForPath:"
- "getLSAppRecordForBundle:reply:"
- "getPathOfNodeID:FSid:"
- "getPathOfiNode:inVolume:"
- "getResolvedURL:"
- "getTimeValAddr"
- "getURLMountPoint:"
- "getVolSizeFromAttrList:completionHandler:"
- "getVolumesPaths"
- "i32@0:8@16q24"
- "i40@0:8@16q24^{?=QQQQ}32"
- "initWithActivity:completionHandler:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithDevName:error:"
- "intValue"
- "isEqualToString:"
- "isFileCloned:"
- "isFilePurgeable:"
- "isItemMountedOnSystemVolume:"
- "markTimeEndForPhase:"
- "markTimeStartForPhase:"
- "mtrAoWJ3gsq+I90ZnQ0vQw"
- "newWithActivity:andCompletionHandler:"
- "runFullScan:"
- "setActivity:"
- "setActivityResult:"
- "setCompletionHandler:"
- "setDeferActivity:"
- "setDiskUsed:andCapacity:"
- "setShouldStop:"
- "setTimeVal:"
- "shouldStop"
- "stringWithCString:encoding:"
- "stringWithUTF8String:"
- "syncSharedManager"
- "targetDeviceIsHomePod"
- "targetDeviceIsIpad"
- "targetDeviceIsWatch"
- "timeVal"
- "unable to get mounts: %s (%d)\n"
- "v32@0:8Q16Q24"
- "v32@0:8r*16@?24"
- "v32@0:8{timeval=qi}16"
- "v40@0:8Q16Q24@?32"
- "valueForKey:"
- "volumeSupportsAttributionTags:"
- "volumeSupportsCloneMapping:"
- "wholeDiskForDisk:"
- "{timeval=\"tv_sec\"q\"tv_usec\"i}"
- "{timeval=qi}16@0:8"

```
