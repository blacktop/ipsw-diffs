## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.0.19.0.1
-  __TEXT.__text: 0x2e626c
+1837.0.31.0.1
+  __TEXT.__text: 0x2e69ac
   __TEXT.__auth_stubs: 0x2be0
-  __TEXT.__objc_stubs: 0x22c00
-  __TEXT.__objc_methlist: 0x10624
-  __TEXT.__const: 0x7ba18
-  __TEXT.__cstring: 0x39deb
-  __TEXT.__objc_methname: 0x3e7c9
-  __TEXT.__objc_classname: 0xe64
-  __TEXT.__objc_methtype: 0x3f65
-  __TEXT.__oslogstring: 0x54207
-  __TEXT.__gcc_except_tab: 0xd2b0
+  __TEXT.__objc_stubs: 0x22cc0
+  __TEXT.__objc_methlist: 0x10654
+  __TEXT.__const: 0x7ba08
+  __TEXT.__cstring: 0x3a10b
+  __TEXT.__objc_methname: 0x3e881
+  __TEXT.__objc_classname: 0xe66
+  __TEXT.__objc_methtype: 0x3f68
+  __TEXT.__oslogstring: 0x53dc7
+  __TEXT.__gcc_except_tab: 0xd21c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1332
   __TEXT.__constg_swiftt: 0x1788

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x5e90
+  __TEXT.__unwind_info: 0x5e88
   __TEXT.__eh_frame: 0x3464
   __DATA_CONST.__auth_got: 0x1600
   __DATA_CONST.__got: 0x740
   __DATA_CONST.__auth_ptr: 0xac0
-  __DATA_CONST.__const: 0x8540
-  __DATA_CONST.__cfstring: 0x2c460
+  __DATA_CONST.__const: 0x8580
+  __DATA_CONST.__cfstring: 0x2c940
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a70
-  __DATA_CONST.__objc_arraydata: 0xbd0
+  __DATA_CONST.__objc_selrefs: 0x9a88
+  __DATA_CONST.__objc_arraydata: 0xbe8
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x15478
+  __DATA.__objc_const: 0x154d8
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x850
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13f0
+  __DATA.__objc_ivar: 0x13f8
   __DATA.__objc_data: 0x2b88
   __DATA.__data: 0x2ca8
   __DATA.__bss: 0x6668

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CE4ADBA4-91CF-3292-AB15-4CA9BF1EFA82
-  Functions: 9075
-  Symbols:   16616
-  CStrings:  23349
+  UUID: 81A06B36-B25B-398E-941E-564DA44F8972
+  Functions: 9079
+  Symbols:   16627
+  CStrings:  23430
 
Symbols:
+ +[MADAutoAssetSetHealthReport bucketedTimeSinceDate:]
+ -[ControlManager alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:logString:]
+ -[ControlManager garbageCollectionTypeToString:]
+ -[MADAutoAssetSetHealthReport configurationChangedDate]
+ -[MADAutoAssetSetHealthReport setConfigurationChangedDate:]
+ -[MADAutoSetConfiguration configurationChangedDate]
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._configurationChangedDate
+ OBJC_IVAR_$_MADAutoSetConfiguration._configurationChangedDate
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1745
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1752
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1753
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2182
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2356
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1164
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1165
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1173
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1174
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2289
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2301
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2337
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1762
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1802
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1803
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2236
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2237
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1911
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1912
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1918
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1872
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2035
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2000
+ ___block_descriptor_56_e8_32s40s_e8_v16?0q8ls32l8s40l8
+ __block_literal_global.1614
+ __block_literal_global.1659
+ __block_literal_global.2092
+ __block_literal_global.2114
+ __block_literal_global.2401
+ __block_literal_global.2403
+ __block_literal_global.2413
+ __block_literal_global.5013
+ _objc_msgSend$alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:logString:
+ _objc_msgSend$bucketedTimeSinceDate:
+ _objc_msgSend$configurationChangedDate
+ _objc_msgSend$garbageCollectionTypeToString:
+ _objc_msgSend$setConfigurationChangedDate:
+ _objc_msgSend$typeAssetJob:assetSelector:downloadResult:
+ _objc_msgSend$typeSetConfiguration:assetSet:configuredCount:requestedCount:fromPallasCount:clientDomainName:
- -[ControlManager alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:]
- -[MADAutoAssetJob handleClientRequest:withControlInformation:]
- GCC_except_table191
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1685
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1692
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1693
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2179
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2353
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1158
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1159
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1167
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1168
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2286
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2298
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2334
- __37-[DownloadManager startDownloadTimer]_block_invoke.1759
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1742
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1743
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2233
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2234
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1908
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1909
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1915
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1869
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1975
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1940
- ___block_descriptor_56_e8_32s40s_e8_v12?0B8ls32l8s40l8
- __block_literal_global.1611
- __block_literal_global.1656
- __block_literal_global.2089
- __block_literal_global.2111
- __block_literal_global.2352
- __block_literal_global.2398
- __block_literal_global.2400
- __block_literal_global.5016
- _objc_msgSend$alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:
CStrings:
+ " %{public}@ | RECLAIMABLE:%{public}@"
+ " %{public}@ | targetingPurgeBytes:%{public}@ | RECLAIMED:%{public}@"
+ " | %s"
+ " | Urgency:%d | %@ | retPolicy: %ld"
+ " | beforeSec:%f | afterSec:%f | reclaimable:%@"
+ " | immediately remove"
+ " | multiplier: %f"
+ " | never remove"
+ " | no multiplier"
+ " | not system+, immediately remove"
+ " | not system+, multipier: %f"
+ " | skipping due to policy of never collect"
+ " | system+, never remove"
+ " | threshold:%@ | gap:%@"
+ "%@ %@ Attempted to move to staging dir %@"
+ "%@ Download manager is nil aborting. Session %{public}@ task %{public}@"
+ "%@ Moving file in didFinishDownloadingToURL, extractor: %d. Session %{public}@ task %{public}@ type %{public}@ repository %{public}@"
+ "%@ Skipping the move as we do not have a task description. Session %{public}@"
+ "%@ Skipping the move due to extractor consuming bytes. Session %{public}@ task %{public}@"
+ "%@ Task completed with response %@ and error %@"
+ "%@ Task resumed at offset %lld bytes out of an expected %lld bytes. Session %{public}@ task %{public}@\n"
+ "%@ | setDescriptor:%@ | atomicInstanceFilename:%@ | latest:%@ | setDescriptorCurrentStatus:%@ | error:%@"
+ "%llu days"
+ "%{public}@ %{public}@ is defined, %{public}@ is %{public}@ on the list.  Reclaim stat will %{public}@ be maintained."
+ "%{public}@ %{public}@ is defined. Unable to get asset type from asset directory %{public}@."
+ "%{public}@ Not able to calculate time since null passed in for timeTaken"
+ "%{public}@ | Could not read asset attributes from assetDirectory(asset could be non-existent), skipping asset."
+ "%{public}@ | Result: asset content did not exist"
+ "%{public}@ | Result: failed to remove asset content - purgeResult:%{public}lld(%{public}@)"
+ "%{public}@ | Result: removed asset content"
+ "%{public}@ | Result: will not delete - reason: %@"
+ "%{public}@ | Result: will not delete - reason: never remove"
+ "%{public}@ | Result: will not delete - reason: recent client interest"
+ "%{public}@ | cache delete not performed | assetCount:%{public}ld | collectionTypeCount:%{public}ld"
+ "%{public}@ | setting client usage as it was not set"
+ "%{public}@ | unable to determine collection types | targetingPurgeBytes:%{public}@ | assetCount:%{public}ld | collectionTypeCount:%{public}ld"
+ "%{public}@: Bulk registering %lu assets with space attribution."
+ "%{public}@: Bulk unregistering %{public}lu assets with space attribution."
+ "%{public}@: Did not find any asset paths to bulk register with space attribution."
+ "%{public}@: Did not find any asset paths to bulk unregister with space attribution."
+ "%{public}@: Failed to bulk register assets with space attribution. Error: %{public}@"
+ "%{public}@: Failed to bulk unregister assets with space attribution. Error: %{public}@"
+ "%{public}@: Successfully bulk registered %{public}lu assets with space attribution."
+ "%{public}@: Successfully bulk unregistered %{public}lu assets with space attribution."
+ "0 days, %llu hours"
+ "14 days or more"
+ "????UNKNOWN GCType???"
+ "AssetGC %@"
+ "AutoJobCancellationTimerFired:"
+ "CD Check: Enough space.  Grand Total Required:%{public}llu, Required for request:%{public}llu, Avail FS:%{public}llu, Avail CD:%{public}llu"
+ "CD Check: NOT enough space.  Grand Total Required:%{public}llu, Required for request:%{public}llu, Avail FS:%{public}llu, Avail CD:%{public}llu"
+ "Cache delete purgeable check results: %{public}@"
+ "CannotSetEmptyAtomicInstance"
+ "ConfigChange"
+ "ConfigChangeBucket"
+ "EvictionTimerFired"
+ "FS Check: Enough free space.  Grand Total Required: %{public}llu, Required space for request: %{public}llu, Available Space: %{public}llu"
+ "FS Check: NOT enough free space.  Grand Total Required: %{public}llu, Required space for request: %{public}llu, Available Space: %{public}llu"
+ "FailedToStart"
+ "GCTypeLocked"
+ "GCTypeLockedNeverRemove"
+ "GCTypeMalformed"
+ "GCTypeNone"
+ "GCTypeOrphan"
+ "GCTypeStaged"
+ "GCTypeUnlockedReferenced"
+ "GCTypeUnlockedUnreferenced"
+ "Performing cache delete purgeable check for %{public}lld bytes free space with these options: %{public}@"
+ "SET_JOB_ASSET_DOWNLOAD_END  "
+ "SET_JOB_ASSET_DOWNLOAD_START"
+ "Starting built-in MobileAsset brain built Jul 14 2025 23:40:39"
+ "Starting downloaded MobileAsset brain (version: %@) built Jul 14 2025 23:40:39"
+ "StatusUnepxectedState"
+ "StatusUnexpectedNonce"
+ "StatusUnknownState"
+ "StatusWriteError"
+ "T@\"NSDate\",&,V_configurationChangedDate"
+ "T@\"NSDate\",R,&,N,V_configurationChangedDate"
+ "Unexpected"
+ "[MAKeyManagerDownloadSessionDelegate]: Challange handler running for session %@"
+ "[PURGE] cache delete purge results: %{public}@"
+ "[SPACE] Using FAKE available space set by the %{public}@ default. Free space available: %{public}llu"
+ "[SPACE] purged %{public}lld bytes"
+ "_configurationChangedDate"
+ "alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:logString:"
+ "bucketedTimeSinceDate:"
+ "com.apple.MobileAsset.DictionaryServices.dictionary3iOS"
+ "com.apple.MobileAsset.DictionaryServices.dictionary3macOS"
+ "com.apple.MobileAsset.Font8"
+ "configurationChangedDate"
+ "d88@0:8d16@24q32@40^B48^@56^q64q72@80"
+ "determine"
+ "duringStartup"
+ "garbageCollectionTypeToString:"
+ "reclaim"
+ "setConfigurationChangedDate:"
+ "unable to create directory for SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@ | errno:%i"
+ "unable to prepare for SHORT-TERM locking [MISSING-REQUIRED] | atomic-instance filenames (latest:%@,base:%@)"
+ "{[%@] performCacheDeleteForGroup} %@ | %s"
+ "{finishAllPartiallyPurgedAssets} %{public}@ | checking for purged assets at path:%{public}@"
+ "{handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | ...respondToCacheDelete | reclaimed:%{public}@"
+ "{handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | respondToCacheDelete..."
+ "{handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | ...respondToCacheDelete | reclaimable:%{public}@"
+ "{handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | respondToCacheDelete..."
+ "{performCacheDeleteCollection} %{public}@ | number of assets and GC types for those corresponding assets don't match | assetCount: %{public}ld | assetGCTypesCount: %{public}ld"
+ "{removeDownloadsNotRecentlyInFlight} could not determine content modification date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} could not determine creation date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} could not remove old in-flight download tracking file (not in-flight) | URL:%{public}@ | result:%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} dir:%{public}@ | referenceDateForRecent:%{public}@ | tasksInFlight:%{public}ld"
+ "{removeDownloadsNotRecentlyInFlight} error determining contents of directory:%{public}@ | error:%{public}@\n%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} failed to determine contents of directory:%{public}@ | error:%{public}@\n%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} removed old in-flight download tracking file (not in-flight) | URL:%{public}@"
+ "{removeDownloadsNotRecentlyInFlight} skipping %{public}@ since it was modified before %{public}@"
+ "{respondToCacheDelete} %{public}@... | targetingPurgeAmount:%{public}@ | urgency:%{public}d(%{public}@) | volume:%{public}@ | assetTypeDirs:%{public}ld | preciousInterval:%{public}@%{public}@, defaultInterval:%{public}@%{public}@%{public}@ | autoAssetStatus:%{public}@"
+ "{respondToCacheDelete} (determining space) for volume %@"
+ "{respondToCacheDelete} ...%{public}@ | targetingPurgeAmount:%{public}@ | urgency:%{public}d(%{public}@) | volume:%{public}@ | assetTypeDirs:%{public}ld | preciousInterval:%{public}@%{public}@, defaultInterval:%{public}@%{public}@%{public}@ | autoAssetStatus:%{public}@ | %{public}@ | MA_MILESTONE"
+ "{respondToCacheDelete} Initializing SAF arrays for register/unregister of assets after determine for volume %{public}@ at urgency %{public}d ..."
+ "{respondToCacheDelete} Using Cache Delete Results: %{public}@"
+ "{respondToCacheDelete} Volume: %{public}@ | Urgency: %{public}d | Operation: %{public}d | reportingLevel %{public}@"
+ "{respondToCacheDelete} performing cache-delete triggered operation for volume %{public}@ at urgency %{public}d ..."
+ "{respondToCacheDelete} skipping garbage collection (no asset-type directories, volume reported by cache delete might be invalid) | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@"
+ "{respondToCacheDelete} skipping garbage collection | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@ | current time is not valid | currentTimeInSeconds:%{public}f, numberOfSecondsInAYear:%{public}llu"
+ "{respondToCacheDelete} | %{public}@ default is specified.  Created set with values %{public}@"
- " %@ targetingPurgeBytes:%@ | directory:%@ | %@:%@"
- "%@ %@ is defined, %@ is %@on the list.  Reclaim stat will %@be maintained."
- "%@ %@ is defined. Unable to get asset type from asset directory %@."
- "%@ Not able to calculate time since null passed in for timeTaken"
- "%@ unable to determine collection types | targetingPurgeBytes:%@ | directory:%@ | assetCount:%ld | collectionTypeCount:%ld"
- "%@ | setDescriptor:%@ | atomicInstanceFilename:%@ | specific:%@ | latest:%@ | setDescriptorCurrentStatus:%@ | error:%@"
- "%@: Bulk registering %lu assets with space attribution."
- "%@: Bulk unregistering %lu assets with space attribution."
- "%@: Did not find any asset paths to bulk register with space attribution."
- "%@: Did not find any asset paths to bulk unregister with space attribution."
- "%@: Failed to bulk register assets with space attribution. Error: %{public}@"
- "%@: Failed to bulk unregister assets with space attribution. Error: %{public}@"
- "%@: Successfully bulk registered %lu assets with space attribution."
- "%@: Successfully bulk unregistered %lu assets with space attribution."
- "CD Check: Enough space.  Grand Total Required:%llu, Required for request:%llu, Avail FS:%llu, Avail CD:%llu"
- "CD Check: NOT enough space.  Grand Total Required:%llu, Required for request:%llu, Avail FS:%llu, Avail CD:%llu"
- "Cache delete purgeable check results: %@"
- "Download manager is nil aborting. Session %{public}@ task %{public}@"
- "Download resumed at offset %lld bytes out of an expected %lld bytes. Session %{public}@ task %{public}@\n"
- "FS Check: Enough free space.  Grand Total Required: %llu, Required space for request: %llu, Available Space: %llu"
- "FS Check: NOT enough free space.  Grand Total Required: %llu, Required space for request: %llu, Available Space: %llu"
- "MADJob:handleClientRequest"
- "Moving file in didFinishDownloadingToURL, extractor: %d. Session %{public}@ task %{public}@ type %{public}@ repository %{public}@"
- "Performing cache delete purgeable check for %lld bytes free space with these options: %@"
- "RECLAIMABLE"
- "RECLAIMED"
- "Skipping the move as we do not have a task description. Session %{public}@"
- "Skipping the move due to extractor consuming bytes. Session %{public}@ task %{public}@"
- "Starting built-in MobileAsset brain built Jul  1 2025 00:08:16"
- "Starting downloaded MobileAsset brain (version: %@) built Jul  1 2025 00:08:16"
- "[CONTROL_MANAGER_CACHEDELETE_QUEUE] {respondToCacheDelete} Initializing SAF arrays for register/unregister of assets after determine for volume %@ at urgency %d ..."
- "[CONTROL_MANAGER_CACHEDELETE_QUEUE] {respondToCacheDelete} performing cache-delete triggered operation for volume %@ at urgency %d ..."
- "[GARBAGE_COLLECTION] {[%@]performCacheDeleteForGroup} %@ |"
- "[GARBAGE_COLLECTION] {finishAllPartiallyPurgedAssets} %{public}@ | checking for purged assets at path:%{public}@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | ...respondToCacheDelete | reclaimed:%{public}@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | respondToCacheDelete..."
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | ...respondToCacheDelete | reclaimable:%{public}@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | respondToCacheDelete..."
- "[GARBAGE_COLLECTION] {performCacheDeleteCollection} %{public}@ | number of assets and GC types for those corresponding assets don't match | assetCount: %ld | assetGCTypesCount: %ld"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | asset:%@ | After alterSecondsBeforeCollection, number of seconds: %f"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | asset:%@ | Before alterSecondsBeforeCollection, number of seconds: %f"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | failed to remove old asset content | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@ | result:%lld(%{public}@)"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | old asset content did not exist | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | removed old asset content | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | setting client usage as it was not set | asset:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | skipping due to policy of never collect | asset:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (%{public}@) | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (never remove) | asset:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (recent client interest) | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} Could not read asset attributes from assetDirectory(asset could be non-existent): %{public}@, skipping asset."
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine content modification date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine creation date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not remove old in-flight download tracking file (not in-flight) | URL:%{public}@ | result:%{public}@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} dir:%{public}@ | referenceDateForRecent:%{public}@ | tasksInFlight:%ld"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} error determining contents of directory:%{public}@ | error:%{public}@\n%{public}@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} failed to determine contents of directory:%{public}@ | error:%{public}@\n%{public}@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} removed old in-flight download tracking file (not in-flight) | URL:%{public}@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} %@... | targetingPurgeAmount:%@ | urgency:%d(%@) | volume:%@ | assetTypeDirs:%ld | preciousInterval:%@%@, defaultInterval:%@%@%@ | autoAssetStatus:%@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} ...%@ | targetingPurgeAmount:%@ | urgency:%d(%@) | volume:%@ | assetTypeDirs:%ld | preciousInterval:%@%@, defaultInterval:%@%@%@ | autoAssetStatus:%@ | %@ | MA_MILESTONE"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} Using Cache Delete Results: %{public}@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} Volume: %{public}@ | Urgency: %d | Operation: %hhu | | reportingLevel %{public}@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} have assetTypeDirs:%ld"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection (no asset-type directories, volume reported by cache delete might be invalid) | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@ | current time is not valid | currentTimeInSeconds:%f, numberOfSecondsInAYear:%llu"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} | %@ default is specified.  Created set with values %@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} | Couldn't reclaim any of the asset in the directory | countAssets: %ld"
- "[MAKeyManagerDownloadSessionDelegate]: Challange handler running"
- "[PURGE] cache delete purge results: %@"
- "[SPACE] Using FAKE available space set by the %@ default. Free space available: %llu"
- "[SPACE] purged %lld bytes"
- "[WARNING] [GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} skipping %{public}@ since it was modified before %{public}@"
- "alterSecondsBeforeCollection:forAssetTypeDir:determinedDescriptorType:fromDescriptors:isAutoAsset:autoAssetDescriptor:assetFilesystemSize:retentionPolicy:"
- "client request with invalid command:%@"
- "d80@0:8d16@24q32@40^B48^@56^q64q72"
- "determining reclaimable space"
- "handleClientRequest:withControlInformation:"
- "reclaiming space"
- "respondToCacheDelete (determining space) for volume %@"
- "specific"
- "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@ | errno:%i"
- "unable to create directory for SHORT-TERM locking | shortTermDirectory:%@"
- "unable to prepare for SHORT-TERM locking [MISSING-REQUIRED] | atomic-instance filenames (specific:%@,latest:%@,base:%@)"
- "{validateShortTermLockURL} specific | clientDomainName:%{public}@ assetSetIdentifier:%{public}@ atomicInstanceUUID:%{public}@"

```
