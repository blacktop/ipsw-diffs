## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.0.0.0.0
-  __TEXT.__text: 0x2e5458
+1837.0.19.0.1
+  __TEXT.__text: 0x2e626c
   __TEXT.__auth_stubs: 0x2be0
-  __TEXT.__objc_stubs: 0x22ba0
-  __TEXT.__objc_methlist: 0x1060c
+  __TEXT.__objc_stubs: 0x22c00
+  __TEXT.__objc_methlist: 0x10624
   __TEXT.__const: 0x7ba18
-  __TEXT.__cstring: 0x39c3b
-  __TEXT.__objc_methname: 0x3e77e
+  __TEXT.__cstring: 0x39deb
+  __TEXT.__objc_methname: 0x3e7c9
   __TEXT.__objc_classname: 0xe64
   __TEXT.__objc_methtype: 0x3f65
-  __TEXT.__oslogstring: 0x54037
-  __TEXT.__gcc_except_tab: 0xd248
+  __TEXT.__oslogstring: 0x54207
+  __TEXT.__gcc_except_tab: 0xd2b0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1332
   __TEXT.__constg_swiftt: 0x1788

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x5e88
+  __TEXT.__unwind_info: 0x5e90
   __TEXT.__eh_frame: 0x3464
   __DATA_CONST.__auth_got: 0x1600
   __DATA_CONST.__got: 0x740
   __DATA_CONST.__auth_ptr: 0xac0
   __DATA_CONST.__const: 0x8540
-  __DATA_CONST.__cfstring: 0x2c2e0
+  __DATA_CONST.__cfstring: 0x2c460
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a58
-  __DATA_CONST.__objc_arraydata: 0xc00
+  __DATA_CONST.__objc_selrefs: 0x9a70
+  __DATA_CONST.__objc_arraydata: 0xbd0
   __DATA_CONST.__objc_arrayobj: 0x2d0
-  __DATA_CONST.__objc_intobj: 0x5b8
+  __DATA_CONST.__objc_intobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA.__objc_const: 0x15478
   __DATA.__objc_protorefs: 0x18

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 22043F0B-9434-31BE-ACE0-9A10F67244D8
-  Functions: 9072
-  Symbols:   16609
-  CStrings:  23316
+  UUID: CE4ADBA4-91CF-3292-AB15-4CA9BF1EFA82
+  Functions: 9075
+  Symbols:   16616
+  CStrings:  23349
 
Symbols:
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withAddendumMessage:]
+ -[MADAutoAssetStager action_ReplyNoCandidatesRemoveAllReplyErased:error:]
+ _MABrainUtilitySupportsGracefulUngraft
+ _NSStreamDataWrittenToMemoryStreamKey
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1685
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1692
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1693
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2179
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2353
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2286
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2298
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2334
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1759
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1742
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1743
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2233
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2234
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1908
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1915
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1869
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1975
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1940
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1172
+ __block_literal_global.1118
+ __block_literal_global.1129
+ __block_literal_global.1134
+ __block_literal_global.1139
+ __block_literal_global.1163
+ __block_literal_global.1256
+ __block_literal_global.1381
+ __block_literal_global.1387
+ __block_literal_global.1392
+ __block_literal_global.1397
+ __block_literal_global.1402
+ __block_literal_global.1424
+ __block_literal_global.1584
+ __block_literal_global.1656
+ __block_literal_global.1708
+ __block_literal_global.1713
+ __block_literal_global.1718
+ __block_literal_global.1752
+ __block_literal_global.1776
+ __block_literal_global.1798
+ __block_literal_global.2089
+ __block_literal_global.2111
+ __block_literal_global.2352
+ __block_literal_global.2398
+ __block_literal_global.2400
+ __block_literal_global.2406
+ __block_literal_global.2808
+ _objc_msgSend$action_ReplyNoCandidatesRemoveAllReplyErased:error:
+ _objc_msgSend$outputStreamToMemory
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withAddendumMessage:
- _NSStringEncodingDetectionSuggestedEncodingsKey
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1675
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1682
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1683
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2175
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2349
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2282
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2294
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2330
- __37-[DownloadManager startDownloadTimer]_block_invoke.1753
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1732
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1733
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2229
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2230
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1902
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1903
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1863
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1965
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1930
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1192
- __block_literal_global.1115
- __block_literal_global.1126
- __block_literal_global.1131
- __block_literal_global.1136
- __block_literal_global.1160
- __block_literal_global.1253
- __block_literal_global.1378
- __block_literal_global.1384
- __block_literal_global.1389
- __block_literal_global.1394
- __block_literal_global.1399
- __block_literal_global.1421
- __block_literal_global.1578
- __block_literal_global.1650
- __block_literal_global.1711
- __block_literal_global.1716
- __block_literal_global.1724
- __block_literal_global.1755
- __block_literal_global.1779
- __block_literal_global.1792
- __block_literal_global.2080
- __block_literal_global.2102
- __block_literal_global.2342
- __block_literal_global.2394
- __block_literal_global.2396
- __block_literal_global.2412
- __block_literal_global.2802
- _objc_msgSend$stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:
CStrings:
+ "%@ | {newAssetDownloadOptions} set-job yet no nextSetSpecifierToDownload"
+ "%@:splitOutAvailableForStagingByGroup"
+ "%{public}@\n[%{public}@] {_addToStaged} to-be-staged asset-descriptor already downloaded"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} best candidate so far | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} nil selectorEntryID | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} not newer version | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} trimmed auto-asset-descriptors available-for-staging | previousCount:%ld | trimmedCOunt:%ld"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} versions not comparable (keeping already encountered) | nextAvailableDescriptor:%{public}@ | alreadyAvailableDescriptor:%@"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} cache miss | lookupResultsKey:%{public}@ cachingEnabled:%@"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} content on filesystem validated | entryID:%{public}@, adopted targetLookupResults:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} multiple entries | lookupResultsKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} no persisted set-lookup-results to be resumed"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} unable to retrieve set-lookup-result | entryID:%{public}@"
+ "2.5.2"
+ "AUTO-CONTROL:{autoSetJobAvailableAtomicInstanceForSetDescriptor}: Returning no for atomicInstanceAvailable since FSM is not initialized"
+ "ControlFinishResumeFromPersisted"
+ "ControlResumeFromPersisted"
+ "DetermineEliminating"
+ "DownloadDecideMoreAvailable"
+ "Failed to reclaim due to %@ | path: %@"
+ "JobDetermineAvailableFailure"
+ "JobDetermineAvailableSuccess"
+ "JobDownloadForStagingFailure"
+ "JobDownloadForStagingProgress"
+ "JobDownloadForStagingSuccess"
+ "MADStager:ReplyNoCandidatesRemoveAllReplyErased"
+ "Old asset content did not exist | path: %@"
+ "Overriding resource timeout for auto asset to max download timeout."
+ "Params being sent to the server are: %{public}@"
+ "PurgeEraseAcceptedRemoveAll"
+ "RECLAIMED_ASSET"
+ "ReplyNoCandidatesRemoveAllReplyErased"
+ "Starting built-in MobileAsset brain built Jul  1 2025 00:08:16"
+ "Starting downloaded MobileAsset brain (version: %@) built Jul  1 2025 00:08:16"
+ "Successfully reclaimed path: %@"
+ "TargetAvailableOptional"
+ "TargetAvailableRequired"
+ "TargetHaveOtherAvailable"
+ "TargetNoOtherAvailable"
+ "TargetNotAvailable"
+ "TimeoutValidActiveDetermine"
+ "TimerFiredDetermining"
+ "UNGRAFTDMG_NOFORCE"
+ "UnstagedFromControlCancelJob"
+ "UnstagedFromControlRemoveAll"
+ "[%{public}@] {getTargetLookupResultsForKey} entry too old | dateOfEntry:%{public}@"
+ "[%{public}@] {getTargetLookupResultsForKey} unable to determine recency | dateOfEntry:%{public}@"
+ "[%{public}@] {getTargetLookupResultsForKey} unable to load set-lookup-result | entryID:%{public}@"
+ "[DownloadManager-isBuddyRunning] SetupAssistant framework not available in this environment"
+ "action_ReplyNoCandidatesRemoveAllReplyErased:error:"
+ "com.apple.MobileAsset.DeviceRecoveryBrain"
+ "com.apple.MobileAsset.UAF."
+ "com.apple.MobileAssetError.Purge"
+ "getTargetLookupResultsForKey"
+ "outputStreamToMemory"
+ "propertyForKey:"
+ "recordOperation:toHistoryType:fromLayer:withAddendumMessage:"
+ "supports-graceful-ungraft"
+ "ungraft_param"
+ "{%@} empty trimmedArray (unable to trim availableForStaging)"
+ "{%@} unable to load auto-asset-descriptor from trimmedAvailableForStaging | trimmedSelectorKey:%@"
+ "{%{public}@} (%{public}@)\n[DOWNLOADED-TO-MANAGER] asset-version just immediate-promoted | downloadedAsset:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_doesSelector:matchDescriptor} not a match | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} accepted as candidate | descriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} examining preSoftwareUpdateAssetStaging descriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} not newer version | descriptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} cache miss | lookupResultsKey:%{public}@ cachingEnabled:%@"
- "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} content on filesystem validated | entryID:%{public}@, adopted targetLookupResults:%{public}@"
- "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} multiple entries | lookupResultsKey:%{public}@"
- "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} no persisted set-lookup-results to be resumed"
- "%{public}@\n[AUTO-STAGER] {loadPersistedTargetLookupResults} unable to retrieve set-lookup-result | entryID:%{public}@"
- "2.5.1"
- "AUTO-CONTROL:{autoSetJobAvailableAtomicInstanceForSetDescriptor}: Returning no for atomicInstanceAvailaible since FSM is not initialized"
- "ControlUnstagedCancelJob"
- "ControlUnstagedRemoveAll"
- "DetermineAvailableFailure"
- "DetermineAvailableSuccess"
- "DetermineHaveRequiredMore"
- "DetermineTimedOut"
- "DownloadForStagingFailure"
- "DownloadForStagingProgress"
- "DownloadForStagingSuccess"
- "DownloadMoreOptional"
- "EraseAcceptedRemoveAll"
- "FinishResumeFromPersisted"
- "GroupTargetAvailableOptional"
- "GroupTargetAvailableRequired"
- "GroupTargetNotAvailable"
- "HaveOtherTargetAvailable"
- "LastStagedJustPromoted"
- "NoOtherTargetAvailable"
- "ResumeFromPersisted"
- "Starting built-in MobileAsset brain built Jun 18 2025 00:13:06"
- "Starting downloaded MobileAsset brain (version: %@) built Jun 18 2025 00:13:06"
- "TimeoutDetermining"
- "[%{public}@] {loadPersistedTargetLookupResults} entry too old | dateOfEntry:%{public}@"
- "[%{public}@] {loadPersistedTargetLookupResults} unable to determine recency | dateOfEntry:%{public}@"
- "[%{public}@] {loadPersistedTargetLookupResults} unable to load set-lookup-result | entryID:%{public}@"
- "[DownloadManager-isBuddyRunning] SetupAssistant framework not availaible in this environment"
- "loadPersistedTargetLookupResults"
- "newAssetDownloadOptions for set-job yet no nextSetSpecifierToDownload | potentialUUID:%@|basePortion:%@"
- "stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:"
- "{AddToStagedDecideMoreAvailable} no downloaded descriptor provided"

```
