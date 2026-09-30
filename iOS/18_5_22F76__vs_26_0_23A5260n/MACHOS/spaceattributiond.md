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
+428.0.0.0.1
+  __TEXT.__text: 0x3bd70
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x67c0
+  __TEXT.__objc_methlist: 0x2a88
+  __TEXT.__const: 0x1e8
+  __TEXT.__oslogstring: 0x4d53
+  __TEXT.__cstring: 0x2f00
+  __TEXT.__objc_classname: 0x2f0
+  __TEXT.__objc_methtype: 0x1035
+  __TEXT.__objc_methname: 0x7ace
+  __TEXT.__gcc_except_tab: 0x1638
+  __TEXT.__unwind_info: 0xd08
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__cfstring: 0x2520
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__objc_arraydata: 0x168
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3910
-  __DATA.__objc_selrefs: 0x1ca8
-  __DATA.__objc_ivar: 0x2c0
-  __DATA.__objc_data: 0xb40
-  __DATA.__data: 0x248
+  __DATA.__objc_const: 0x3ef0
+  __DATA.__objc_selrefs: 0x1f30
+  __DATA.__objc_ivar: 0x308
+  __DATA.__objc_data: 0xc80
+  __DATA.__data: 0x250
   __DATA.__bss: 0x1e8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MetricKit.framework/MetricKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
+  - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35F4748F-0D63-3632-BA71-5B03B4795122
-  Functions: 1198
-  Symbols:   212
-  CStrings:  2593
+  UUID: 1FADB037-45EC-364E-9862-4809EA3C9411
+  Functions: 1301
+  Symbols:   221
+  CStrings:  2761
 
Symbols:
+ _CacheDeleteGetReserveSpace
+ _CacheManagementEnumerateAssets
+ _OBJC_CLASS_$_MXDiskSpaceUsageMetric
+ _OBJC_CLASS_$_MXSourceManager
+ _OBJC_CLASS_$_MXSourceUtilities
+ _OBJC_CLASS_$_MXSpaceAttributionData
+ _OBJC_CLASS_$_NSMeasurement
+ _OBJC_CLASS_$_NSUnitInformationStorage
+ _SBSCopyDisplayIdentifiers
+ __os_log_fault_impl
- _NSLog
CStrings:
+ "\"A"
+ "%s : BGSystemTask object must be supplied with run mode SAAppSizerModeCheckDefer"
+ "%s: removing writer %@ of %@ from appPathList"
+ "+[SAMetricKit sendDataToMetricKit:telemetryManager:]"
+ "-[SAAppSizerScan initiatePathsScanWithRunMode:BGTask:scanOptions:replyBlock:]"
+ "-[SADUrlSizer scanURLs:withSizer:]"
+ "-[SATelemetryManager subtractValue:forAppInfoEntry:forBundleIDs:]"
+ "-[SAVolumesInfo addPurgeableTaggedClone:size:volumePath:]"
+ "-[SAVolumesInfo getBundleIDForTagHash:volumePath:]"
+ "-[SAVolumesInfo getDirCacheElementForDirKey:volumePath:climbUpDSHierarchy:cacheDiscoveredDirElement:]"
+ "-[SAVolumesInfo getPurgeableTaggedCloneSize:volumePath:]"
+ "-[SAVolumesInfo insertDirCacheElement:dirKey:volumePath:]"
+ "-[SAVolumesInfo insertDirKey:bundleIDs:purgeable:cache:volumePath:]"
+ "-[SAVolumesInfo insertTagHash:bundleID:volumePath:]"
+ "/var/db/spaceattribution/AppPathList.db"
+ "@\"SADirCacheElement\""
+ "@32@0:8Q16@24"
+ "@32@0:8Q16r*24"
+ "@40@0:8@16@24B32B36"
+ "@40@0:8Q16@24@32"
+ "@44@0:8@16i24I28i32i36B40"
+ "@48@0:8i16I20i24i28Q32Q40"
+ "@48@0:8q16q24q32Q40"
+ "@60@0:8Q16@24I32Q36Q44Q52"
+ "APFSDiskUsed"
+ "APFSIOC_CLONEGROUP_ITERATE failed with error %d (%s)"
+ "APFSIOC_DIR_STATS_OP for %llu returned errno %u (%s)"
+ "APFSIOC_SPEC_TELEM_OP returned error %d (%s)"
+ "App Sizer diskUsed:%llu diskCapacity:%llu SUR:%llu totalPurgeableDataSize:%llu"
+ "B16@?0@\"CacheManagementAsset\"8"
+ "B48@0:8Q16Q24@32^@40"
+ "C48@0:8Q16@24Q32^@40"
+ "CACHE_DELETE_REPORTABLE_RESERVE_SPACE_AMOUNT"
+ "CACHE_DELETE_RESERVE_SPACE_ENABLED"
+ "CACHE_DELETE_RESERVE_SPACE_FILESYSTEM_AMOUNT"
+ "Can't alloc buff"
+ "Can't find bundleIDs associated with path (%@)"
+ "Can't find name for hash %llu with error %d (%s)"
+ "Clone mapping is not supported"
+ "Done processing clone groups on volume %@"
+ "END: Software Update Reserve"
+ "Error: Duplicate attribute detected (attribute: %d)\n"
+ "Error: bundleIDs %@ cache size: %llu is greater than existing data size: %llu"
+ "Failed to iterate clone with DStream ID (%llu) with %@. Fallback to clone mapping"
+ "Failed to malloc %llu bytes with error %d (%s)"
+ "Failed to process clone groups on volume %@ with error %@"
+ "Failed to process clone groups with %@, fallback to clone mapping"
+ "Failed to stat volume %@ with error %d (%s)"
+ "I"
+ "I16@0:8"
+ "Neither clone mapping nor clone groups are supported!"
+ "No bundleIDs for path %@"
+ "Path %@ is already claimed by another bundles-IDs"
+ "Process clone groups on volume %@"
+ "Purgeable tags size for %@ is %llu"
+ "Q32@0:8Q16r*24"
+ "RESIDENCY_%u"
+ "Removing AppPath for %@ from app path list on disk"
+ "Removing shared path %@ for %@ from app path list on disk"
+ "Removing unique path %@ for %@ from app path list on disk"
+ "SAClone"
+ "SACloneGroupsAnalyzer"
+ "SADUrlSizer"
+ "SAMetricKit"
+ "START: Software Update Reserve"
+ "Sending diskSpaceUsageMetric for app: %@ binarySize: %@ binaryFileCount: %llu dataSize: %@ dataFileCount: %llu cacheFolderSize: %@ cloneSize: %@"
+ "Skipping the attribution of group %llu (number of clones: %llu)"
+ "Software Update Reserve Reportable Amount: %@"
+ "Software Update Reserve is not enabled."
+ "Some attributes are missing (0x%llX). inum: %llu group ID: %llu flags: %d physicalSize: %llu"
+ "Start: App Sizer account for cache size"
+ "State %ul for hash number %llu, inode %llu, bundleID %@"
+ "T@\"NSMutableDictionary\",&,V_appPathListOnDisk"
+ "T@\"NSMutableDictionary\",&,V_purgeableTaggedCloneSize"
+ "T@\"NSMutableDictionary\",&,V_tagsMap"
+ "T@\"NSMutableDictionary\",R,V_pathToBundleIDs"
+ "T@\"NSString\",&,V_bundleIDs"
+ "T@\"NSString\",R,V_bundleID"
+ "T@\"SADirCacheElement\",&,V_dirCacheElement"
+ "TB,R,V_isInsideCacheDir"
+ "TB,R,V_isInsidePurgeableCacheDir"
+ "TB,R,V_isInsidePurgeableDir"
+ "TB,R,V_isPurgeable"
+ "TB,R,V_isRegularPurgeable"
+ "TB,R,V_isSUPurgeable"
+ "TI,V_flags"
+ "TI,V_residency"
+ "TQ,V_attributionHash"
+ "TQ,V_dirStatID"
+ "TQ,V_inum"
+ "TQ,V_physicalSize"
+ "TQ,V_softwareUpdateReserve"
+ "There shouldn't be that many nested folders. (dirKey: %llu, chainedKey: %llu)"
+ "Tq,V_cacheFixUp"
+ "Tq,V_cloneFixUpSize"
+ "Unknown attribute %u"
+ "Validating the app path list on disk"
+ "_attributionHash"
+ "_bundleID"
+ "_bundleIDs"
+ "_cacheFixUp"
+ "_cloneFixUpSize"
+ "_dirCacheElement"
+ "_dirStatID"
+ "_flags"
+ "_inum"
+ "_isInsideCacheDir"
+ "_isInsidePurgeableCacheDir"
+ "_isInsidePurgeableDir"
+ "_isPurgeable"
+ "_isRegularPurgeable"
+ "_isSUPurgeable"
+ "_pathToBundleIDs"
+ "_purgeableTaggedCloneSize"
+ "_softwareUpdateReserve"
+ "_tagsMap"
+ "accountForAppsCacheSize"
+ "accountForPurgeableAssets"
+ "accountPurgeableTagsFor:purgeableTagsSize:"
+ "addAttributedCloneToBundleIDs:withCloneSize:withPurgeableSize:onCloneData:"
+ "addCachePurgeableClones:bundleIDs:onCloneData:"
+ "addClonePathOfCloneID:FSId:dataSize:purgeableSize:dirStatKey:attributionTag:bundleIDs:cloneData:"
+ "addPath:fixedPath:size:bundleIDs:"
+ "addPathOfClone:cloneData:"
+ "addPluginSize:bundleIDs:"
+ "addPurgeableTaggedClone:size:"
+ "addPurgeableTaggedClone:size:volumePath:"
+ "addSoftwareUpdateReserve"
+ "addTagSize:bundleIDs:"
+ "addToSystemDetails:key:"
+ "addValue:forAppInfoEntry:forBundleIDs:"
+ "appCacheSize"
+ "attributeCloneSizeForClone:volumesInfo:clonesData:appSizeBreakdownList:collectClonesPaths:"
+ "attributionHash"
+ "bundleIDs"
+ "bundleIDs %@ Total App Size (%llu) + dataSize (%llu) + fixedSize (%llu) is larger than usedDataVolumes (%llu)"
+ "bundleIDs %@ dataSize (%lld) overflowed"
+ "bundleIDs %@ dataSize (%llu) > dataVolumeSizeUsed (%llu)"
+ "bundleIDs %@ fixedSize (%llu) > dataVolumeSizeUsed (%llu)"
+ "bundleIDs %@ fixedSize overflowed (%lld), setting the size to zero"
+ "bytes"
+ "cacheFixUp"
+ "cacheIsPurgeable"
+ "cache_file_count"
+ "can't find saf dir for dir-key %llu"
+ "cloneFixUpSize"
+ "code"
+ "com.apple.fakeapp.SoftwareUpdateReserve"
+ "com.apple.managedassets"
+ "dirCacheElement"
+ "dirStatID"
+ "diskSpaceUsageMetrics"
+ "diskUsed: %llu totalVisibleAppSize: %llu softwareUpdateVolumeSize: %llusystemVolumeSize: %llu systemData: %lld"
+ "enumeratePurgeableAssets:block:"
+ "fixUpCloneSizeForClone:volumesInfo:clonesData:appSizeBreakdownList:revert:"
+ "flags"
+ "getAccessBundleIdForTag:onVolumeName:"
+ "getAppCacheSize"
+ "getAppPathForInternalDaemonContainer:identifier:block:"
+ "getAttributionSizeWithVolumesInfo:reply:"
+ "getBundleIDForTagHash:"
+ "getBundleIDForTagHash:volumePath:"
+ "getBundleIDsByPathForNodeID:forFsid:andPathList:"
+ "getBundleIDsForPath:"
+ "getBundleIDsForSuccessorPath:"
+ "getBundleIDsOfInode:withDirKey:andTag:inVolume:usingPathList:andVolumesInfo:volumePath:"
+ "getDirCacheElementForDirKey:volumePath:climbUpDSHierarchy:cacheDiscoveredDirElement:"
+ "getDirInfoByDirKey:volumesInfo:volumePath:"
+ "getFixUpSizeAndOwnerWithVolumesInfo:reply:"
+ "getInodeForDirStatKey:volumePath:"
+ "getOwnerWithVolumesInfo:"
+ "getPathForDirStatKey:volumePath:"
+ "getPurgeableTaggedCloneSize:"
+ "getPurgeableTaggedCloneSize:volumePath:"
+ "getValueForAppInfoEntry:forBundleIDs:"
+ "getVendorNameForBundleIDs:"
+ "getVendorValueforBundleIDs:"
+ "importDefaultListWithBGTask:volumesInfo:reply:"
+ "importFromLaunchServicesWithBGTask:volumesInfo:reply:"
+ "initPayloadDataWithMutipleAppVersions:withTimeStampBegin:withTimeStampEnd:withMetrics:"
+ "initWithBundleIDs:purgeable:cacheFolder:"
+ "initWithDoubleValue:unit:"
+ "initWithInum:volumePath:flags:dirStatID:attributionTag:physicalSize:"
+ "initWithOptions:"
+ "initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:"
+ "initiatePathsScanWithRunMode:BGTask:scanOptions:replyBlock:"
+ "insertDirCacheElement:dirKey:volumePath:"
+ "insertDirKey:bundleIDs:purgeable:cache:volumePath:"
+ "insertTagHash:bundleID:"
+ "insertTagHash:bundleID:volumePath:"
+ "internalFlags"
+ "inum"
+ "isFullClone"
+ "isInsideCacheDir"
+ "isInsidePurgeableCacheDir"
+ "isInsidePurgeableDir"
+ "isMetricKitClient:"
+ "isNodeID:oldestForDStreamID:path:"
+ "isNodeID:oldestForDStreamID:path:error:"
+ "isPurgeable"
+ "isRegularPurgeable"
+ "isSUPurgeable"
+ "iterateCloneGroupsOnVolume:volumesInfo:appSizeBreakdownList:collectClonesPaths:reply:"
+ "newWithBundleIDs:purgeable:cacheFolder:"
+ "newWithDataSize:cloneSize:purgeableSize:cacheFixUp:"
+ "newWithInum:volumePath:flags:dirStatID:attributionTag:physicalSize:"
+ "newWithOptions:"
+ "pathToBundleIDs"
+ "processCloneGroups:error:"
+ "processCloneGroupsOnVol:volumesInfo:appSizeBreakdownList:collectClonesPaths:reply:"
+ "processClones:"
+ "processClonesMap:error:"
+ "processPurgeableAttributionTags:"
+ "purgeabilityScoreAtUrgency:"
+ "purgeable asset: %@"
+ "purgeable assets size: %llu is greater than existing data size: %llu for bundleSet %@"
+ "purgeable size: %llu is greater than existing data size: %llu for bundleSet %@"
+ "purgeableTaggedCloneSize"
+ "removeBundleIDs:"
+ "resolvePathAndGetSize:forBundleIDs:reply:"
+ "runAppSizerWithRunMode:BGTask:scanOptions:error:"
+ "scanDataPathsWithRunMode:BGTask:scanOptions:"
+ "scanPathsWithRunMode:BGTask:scanOptions:reply:"
+ "sendDataToMetricKit:telemetryManager:"
+ "sendMetrics:forDate:andSourceID:"
+ "sendTelemetry:"
+ "setAPFSDiskUsed:"
+ "setAppPathListOnDisk:"
+ "setAppPathListPathOnDisk:reply:"
+ "setAppPathListPathOnDisktoDefaultWithReply:"
+ "setAttributionHash:"
+ "setBundleIDs:"
+ "setBundleIDs:vendorName:"
+ "setCacheFixUp:"
+ "setCloneFixUpSize:"
+ "setDirCacheElement:"
+ "setDirStatID:"
+ "setFlags:"
+ "setInternalFlags:"
+ "setInum:"
+ "setPurgeableTaggedCloneSize:"
+ "setSoftwareUpdateReserve:"
+ "setTagsMap:"
+ "setValue:forAppInfoEntry:forBundleIDs:"
+ "sharedManager"
+ "shouldValidateAppPathsOnDisk"
+ "softwareUpdateReserve"
+ "subtractValue:forAppInfoEntry:forBundleIDs:"
+ "tagsMap"
+ "total_cache_file_count"
+ "updateAppSizeBreakdownForClone:appSizeBreakdownList:dataSize:"
+ "updateAppSizeBreakdownList:FSId:dataSize:attributionTag:bundleIDs:appSizeBreakdownList:pathList:"
+ "updateAttributonTagInfoForBundle:purgeableTagSize:volumePath:"
+ "updateBundleIDs:appCacheSize:"
+ "updateBundleIDs:appCacheSize:CDPluginSize:"
+ "updateBundleIDs:attributionSize:attributionCloneSize:attributionTagCount:"
+ "updateBundleIDs:fixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
+ "updateBundleIDs:usedDirStat:fixedSize:dataSize:cloneSize:purgeableSize:fileCount:"
+ "updateBundleIDs:withAppSize:"
+ "updateBundleIDs:withDataSize:"
+ "updateBundleIDs:withPurgeableTagSize:"
+ "updateBundleIDs:withSUPurgeableSize:"
+ "updateCacheFileCount:forBundleIDs:"
+ "updateCacheSize:cacheIsPurgeable:bundleIDs:"
+ "updateCloneInfoWithBundleIDs:withItemSize:"
+ "updatePath:cloneSize:bundleIDs:"
+ "updateTagsWithCloneSize:bundleIDs:"
+ "v24@?0@\"NSString\"8@\"SAAppSize\"16"
+ "v24@?0@\"NSString\"8Q16"
+ "v28@0:8B16^@20"
+ "v28@?0@\"NSString\"8I16@\"SDADataBaseAveElement\"20"
+ "v32@0:8Q16@24"
+ "v32@0:8i16I20@?24"
+ "v32@?0@\"NSString\"8q16q24"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16Q24@32"
+ "v40@0:8@16i24I28@?32"
+ "v40@0:8Q16Q24@32"
+ "v40@?0@\"NSString\"8@\"NSNumber\"16Q24Q32"
+ "v48@?0@\"NSString\"8i16I20i24i28@\"SDAHistogramElement\"32^B40"
+ "v52@0:8@16@24@32B40@?44"
+ "v56@0:8i16I20i24i28Q32Q40Q48"
+ "v64@0:8@16i24@28I36Q40Q48Q56"
+ "v64@0:8@16i24i28i32I36Q40Q48Q56"
+ "validateAppPathsOnDisk"
- "%s : An Bg system task must be supplied with run mode SAAppSizerModeCheckDefer"
- "%s: removing writer %@ from appPathList"
- "-[SAAppSizerScan initiatePathsScanWithBlocksNum:withRunMode:withBGTask:scanOptions:withReplyBlock:]"
- "-[SATelemetryManager subtractValue:forAppInfoEntry:forBundleSet:]"
- "-[SAVolumeScanner scanURLs:withSizer:]"
- "-[SAVolumesInfo getDirCacheElementForDirKey:volumePath:]"
- "-[SAVolumesInfo insertDirStatID:bundlesSet:purgeable:cache:volumePath:]"
- "1"
- "@\"NSSet\""
- "@32@0:8Q16*24"
- "@32@0:8Q16^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}24"
- "@44@0:8@16i24i28i32i36B40"
- "@48@0:8i16i20i24i28Q32Q40"
- "APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "Adding path (%@) (%llu)"
- "App Sizer diskUsed:%llu diskCapacity:%llu totalPurgeableDataSize:%llu"
- "AppPathList.db"
- "Bundle set %@ dataSize (%lld) overflowed"
- "Bundles set %@ Total App Size (%llu) + dataSize (%llu) + fixedSize (%llu) is larger than usedDataVolumes (%llu)"
- "Bundles set %@ dataSize (%llu) > dataVolumeSizeUsed (%llu)"
- "Bundles set %@ fixedSize (%llu) > dataVolumeSizeUsed (%llu)"
- "Bundles set %@ fixedSize overflowed (%lld), setting the size to zero"
- "C52@0:8i16Q20@28Q36^@44"
- "Can't find bundles set associated with path (%@)"
- "Can't find name for hash %llu"
- "Error: Group %@ cache size: %llu is greater than existing data size: %llu"
- "Failed to get the dirStats ID for path %@ with error %s"
- "No appsSet for path %@"
- "Path %@ is already claimed by another bundles-set"
- "Q20@0:8B16"
- "RESIDENCY_1"
- "RESIDENCY_2"
- "RESIDENCY_3"
- "RESIDENCY_4"
- "Start: App Sizer account for group container cache size"
- "T@\"NSMutableArray\",R"
- "T@\"NSMutableDictionary\",&,V_tagMap"
- "T@\"NSMutableDictionary\",R,V_appPathListOnDisk"
- "T@\"NSMutableDictionary\",R,V_pathToBundlesSet"
- "T@\"NSSet\",&,V_bundlesSet"
- "TQ,R,V_lastKnownAppCacheSize"
- "Ti,V_residency"
- "_bundlesSet"
- "_lastKnownAppCacheSize"
- "_pathToBundlesSet"
- "_tagMap"
- "accountFoGroupContainersCacheSize"
- "addAttributedCloneToBundleSet:withCloneSize:withPurgeableSize:onCloneData:"
- "addClonePathOfCloneID:FSId:dataSize:purgeableSize:dirStatKey:attributionTag:bundleSet:cloneData:"
- "addPath:fixedPath:size:bundleId:"
- "addPaths:ToBundleSets:"
- "addPluginSize:bundleId:"
- "addTagSize:bundleId:"
- "addValue:forAppInfoEntry:forBundleSet:"
- "appList"
- "bundlesSet"
- "can't find saf dir for dir-key %llu file path %@"
- "com.apple.Preferences"
- "dirstat key %@ is not inside saf_dirstat hierarchy"
- "dirstat key %llu is not inside saf_dirstat hierarchy"
- "getAppCacheSize:"
- "getAppsSetForPath:"
- "getBundlesSetByPathForNodeID:forFsid:andPathList:"
- "getBundlesSetForPath:"
- "getBundlesSetOfInode:withDirKey:andTag:inVolume:usingPathList:andVolumesInfo:volumePath:"
- "getINodeForDirStatKey:ofMount:"
- "getValueForAppInfoEntry:forBundleSet:"
- "getVendorNameForBundleSet:"
- "getVendorValueforBundleSet:"
- "importDefaultListWithBGTask:reply:"
- "importFromLaunchServicesWithBGTask:reply:"
- "initWithBundleSet:purgeable:cacheFolder:"
- "initiatePathsScanWithBlocksNum:withRunMode:withBGTask:scanOptions:withReplyBlock:"
- "insertDirStatID:bundlesSet:purgeable:cache:volumePath:"
- "lastKnownAppCacheSize"
- "lookupAndCacheDirInfoByDirKey:volumePath:"
- "newWithBundleSet:purgeable:cacheFolder:"
- "newWithDataSize:cloneSize:purgeableSize:"
- "pathToBundlesSet"
- "processClonesMap:"
- "processPurgeableAttributionTags"
- "purgeable size: %llu (%llu + %llu) is greater than existing data size: %llu for bundleSet %@"
- "removeBundleSet:"
- "resolvePathAndGetSize:forBundleSet:reply:"
- "runAppSizerWithAsyncBlocksNum:withRunMode:withBGTask:withScanOptions:error:"
- "scanDataPathsWithRunMode:task:scanOptions:"
- "scanPathsWithRunMode:task:scanOptions:reply:"
- "sendTelemetry:appPathList:"
- "setAppSet:vendorName:"
- "setBundlesSet:"
- "setTagMap:"
- "setValue:forAppInfoEntry:forBundleSet:"
- "subtractValue:forAppInfoEntry:forBundleSet:"
- "systemDetails"
- "tagMap"
- "there shouldn't be that many nested folders. (dirKey: %llu, chainedKey: %llu)"
- "updateAppSet:appCacheSize:CDPluginSize:"
- "updateAppSet:attributionSize:attributionCloneSize:attributionTagCount:"
- "updateAppSet:fixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:"
- "updateAppSet:usedDirStat:fixedSize:dataSize:cloneSize:purgeableSize:fileCount:"
- "updateAppSet:withAppSize:"
- "updateAppSet:withPurgeableTagSize:"
- "updateAppSet:withSUPurgeableSize:"
- "updateAppSizeBreakdownList:FSId:dataSize:attributionTag:bundleSet:appSizeBreakdownList:pathList:"
- "updateBundleID:withDataSize:"
- "updateCloneInfoWithAppSet:withItemSize:"
- "updatePath:cacheSize:bundleId:"
- "updatePath:cloneSize:bundleId:"
- "updateTagsWithCloneSize:bundleId:"
- "url is %@"
- "v24@?0@\"NSSet\"8@\"SAAppSize\"16"
- "v24@?0@\"NSString\"8@\"NSNumber\"16"
- "v28@0:8B16@20"
- "v28@?0@\"NSString\"8i16@\"SDADataBaseAveElement\"20"
- "v32@0:8i16i20@?24"
- "v32@?0@\"NSString\"8Q16^B24"
- "v40@0:8@16i24i28@?32"
- "v48@?0@\"NSString\"8i16i20i24i28@\"SDAHistogramElement\"32^B40"
- "v52@0:8i16Q20@28Q36@?44"
- "v56@0:8i16i20i24i28Q32Q40Q48"
- "v64@0:8@16i24@28i36Q40Q48Q56"
- "v64@0:8@16i24i28i32i36Q40Q48Q56"

```
