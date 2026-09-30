## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.100.93.502.2
-  __TEXT.__text: 0x2709e4
+1487.100.105.502.1
+  __TEXT.__text: 0x2742f8
   __TEXT.__auth_stubs: 0x2440
-  __TEXT.__objc_stubs: 0x21f80
-  __TEXT.__objc_methlist: 0x10154
+  __TEXT.__objc_stubs: 0x22440
+  __TEXT.__objc_methlist: 0x10354
   __TEXT.__const: 0x48ae
-  __TEXT.__cstring: 0x3720c
-  __TEXT.__objc_methname: 0x3c91f
-  __TEXT.__objc_classname: 0xdd3
-  __TEXT.__objc_methtype: 0x3931
-  __TEXT.__oslogstring: 0x4b40c
+  __TEXT.__cstring: 0x376fc
+  __TEXT.__objc_methname: 0x3d4bf
+  __TEXT.__objc_classname: 0xdf0
+  __TEXT.__objc_methtype: 0x39d1
+  __TEXT.__oslogstring: 0x4b5af
   __TEXT.__gcc_except_tab: 0x2f34
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4878
+  __TEXT.__unwind_info: 0x48a8
   __TEXT.__eh_frame: 0x3284
   __DATA_CONST.__auth_got: 0x1230
   __DATA_CONST.__got: 0x680
-  __DATA_CONST.__auth_ptr: 0xa18
-  __DATA_CONST.__const: 0x67e8
-  __DATA_CONST.__cfstring: 0x2b380
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__auth_ptr: 0xa20
+  __DATA_CONST.__const: 0x6808
+  __DATA_CONST.__cfstring: 0x2b740
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x96b8
-  __DATA_CONST.__objc_arraydata: 0xb20
-  __DATA_CONST.__objc_arrayobj: 0x258
-  __DATA_CONST.__objc_intobj: 0x408
+  __DATA_CONST.__objc_selrefs: 0x97f8
+  __DATA_CONST.__objc_arraydata: 0xb98
+  __DATA_CONST.__objc_arrayobj: 0x270
+  __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x14d70
-  __DATA.__objc_classrefs: 0x7f8
+  __DATA.__objc_const: 0x14ff0
+  __DATA.__objc_classrefs: 0x800
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13bc
-  __DATA.__objc_data: 0xd60
+  __DATA.__objc_ivar: 0x13e4
+  __DATA.__objc_data: 0xdb0
   __DATA.__data: 0x25a8
-  __DATA.__bss: 0x51b0
+  __DATA.__bss: 0x51c0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__bss: 0x318

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8288
-  Symbols:   15258
-  CStrings:  16579
+  Functions: 8332
+  Symbols:   15360
+  CStrings:  16679
 
Symbols:
+ +[MADAutoAssetSetHealthReport errorSummaryForSplunk:]
+ +[MADAutoAssetSetHealthReport formattedDate:]
+ +[MADAutoAssetSetHealthReport formattedDate:].cold.1
+ +[MADAutoAssetSetHealthReport shortUUID:]
+ +[MADAutoAssetSetHealthReport trimmedSetIdentifier:]
+ +[MobileAssetHealthReport bucketedDays:]
+ -[DownloadManager sendMobileAssetHealthReport:commonFields:sessionId:]
+ -[MADAutoAssetControlManager _clearAtomicInstanceFromAllSetConfigurations:fromLocation:]
+ -[MADAutoAssetControlManager _clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:]
+ -[MADAutoAssetControlManager _filesystemCachedInfo:forPath:]
+ -[MADAutoAssetControlManager filesystemDoesDirectoryExist:atPath:isDirectory:]
+ -[MADAutoAssetControlManager filesystemDoesFileExist:atPath:]
+ -[MADAutoAssetControlManager filesystemFileExistAtPathCache]
+ -[MADAutoAssetControlManager filesystemStartupLookupCount]
+ -[MADAutoAssetControlManager setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:]
+ -[MADAutoAssetControlManager setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:]
+ -[MADAutoAssetControlManager setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:]
+ -[MADAutoAssetControlManager setConfigurationPreviouslyVendedLockedAtomicInstances:]
+ -[MADAutoAssetControlManager setConfigurationRemovedAtomicInstance:fromLocation:]
+ -[MADAutoAssetControlManager setConfigurationTrackAsPreviouslyVended:forSetConfiguration:addingAtomicInstance:]
+ -[MADAutoAssetControlManager setFilesystemFileExistAtPathCache:]
+ -[MADAutoAssetControlManager setFilesystemStartupLookupCount:]
+ -[MADAutoAssetControlManager trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:]
+ -[MADAutoAssetSetHealthReport .cxx_destruct]
+ -[MADAutoAssetSetHealthReport LastCheckedDate]
+ -[MADAutoAssetSetHealthReport availableForUseError]
+ -[MADAutoAssetSetHealthReport eventPayloadForCoreAnalytics]
+ -[MADAutoAssetSetHealthReport eventPayloadForSplunk]
+ -[MADAutoAssetSetHealthReport lastestToVendIsLocked]
+ -[MADAutoAssetSetHealthReport lastestToVendMatchesSetConfig]
+ -[MADAutoAssetSetHealthReport latestDiscoveredAssetSetUUID]
+ -[MADAutoAssetSetHealthReport latestToVendAssetSetUUID]
+ -[MADAutoAssetSetHealthReport newerVersionError]
+ -[MADAutoAssetSetHealthReport setAvailableForUseError:]
+ -[MADAutoAssetSetHealthReport setIdentifier]
+ -[MADAutoAssetSetHealthReport setLastCheckedDate:]
+ -[MADAutoAssetSetHealthReport setLastestToVendIsLocked:]
+ -[MADAutoAssetSetHealthReport setLastestToVendMatchesSetConfig:]
+ -[MADAutoAssetSetHealthReport setLatestDiscoveredAssetSetUUID:]
+ -[MADAutoAssetSetHealthReport setLatestToVendAssetSetUUID:]
+ -[MADAutoAssetSetHealthReport setNewerVersionError:]
+ -[MADAutoAssetSetHealthReport setSetIdentifier:]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoSetConfiguration previouslyVendedLockedAtomicInstances]
+ -[MADAutoSetConfiguration previouslyVendedLockedSummary]
+ -[MADAutoSetConfiguration setPreviouslyVendedLockedAtomicInstances:]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]
+ -[MobileAssetHealthReport _submitReportToSplunk:commonFields:sessionId:]
+ -[MobileAssetHealthReport getHealthReports]
+ GCC_except_table135
+ GCC_except_table142
+ GCC_except_table175
+ GCC_except_table256
+ GCC_except_table414
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table626
+ GCC_except_table758
+ GCC_except_table95
+ OBJC_IVAR_$_MADAutoAssetControlManager._filesystemFileExistAtPathCache
+ OBJC_IVAR_$_MADAutoAssetControlManager._filesystemStartupLookupCount
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._LastCheckedDate
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._availableForUseError
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._lastestToVendIsLocked
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._lastestToVendMatchesSetConfig
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._latestDiscoveredAssetSetUUID
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._latestToVendAssetSetUUID
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._newerVersionError
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._setIdentifier
+ OBJC_IVAR_$_MADAutoSetConfiguration._previouslyVendedLockedAtomicInstances
+ _OBJC_CLASS_$_MADAutoAssetSetHealthReport
+ _OBJC_METACLASS_$_MADAutoAssetSetHealthReport
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2119
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2292
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2230
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2242
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2273
+ __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1077
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2174
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2175
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1857
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1858
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1864
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1818
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2308
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2505
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2506
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3286
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3287
+ __OBJC_$_CLASS_METHODS_MADAutoAssetSetHealthReport
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetSetHealthReport
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoAssetSetHealthReport
+ __OBJC_$_PROP_LIST_MADAutoAssetSetHealthReport
+ __OBJC_CLASS_RO_$_MADAutoAssetSetHealthReport
+ __OBJC_METACLASS_RO_$_MADAutoAssetSetHealthReport
+ ___45+[MADAutoAssetSetHealthReport formattedDate:]_block_invoke
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke
+ __block_literal_global.1079
+ __block_literal_global.2033
+ __block_literal_global.2055
+ __block_literal_global.2216
+ __block_literal_global.2227
+ __block_literal_global.2238
+ __block_literal_global.2246
+ __block_literal_global.2254
+ __block_literal_global.2262
+ __block_literal_global.2270
+ __block_literal_global.2278
+ __block_literal_global.2286
+ __block_literal_global.2294
+ __block_literal_global.2319
+ __block_literal_global.2347
+ __block_literal_global.2349
+ __block_literal_global.3940
+ __block_literal_global.4954
+ _objc_msgSend$LastCheckedDate
+ _objc_msgSend$_clearAtomicInstanceFromAllSetConfigurations:fromLocation:
+ _objc_msgSend$_clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:
+ _objc_msgSend$_filesystemCachedInfo:forPath:
+ _objc_msgSend$_submitReportToCoreAnalytics:commonFields:sessionId:
+ _objc_msgSend$_submitReportToSplunk:commonFields:sessionId:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$bucketedDays:
+ _objc_msgSend$errorSummaryForSplunk:
+ _objc_msgSend$eventPayloadForCoreAnalytics
+ _objc_msgSend$eventPayloadForSplunk
+ _objc_msgSend$filesystemDoesDirectoryExist:atPath:isDirectory:
+ _objc_msgSend$filesystemDoesFileExist:atPath:
+ _objc_msgSend$filesystemFileExistAtPathCache
+ _objc_msgSend$filesystemStartupLookupCount
+ _objc_msgSend$formattedDate:
+ _objc_msgSend$getHealthReports
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$lastestToVendIsLocked
+ _objc_msgSend$lastestToVendMatchesSetConfig
+ _objc_msgSend$latestDiscoveredAssetSetUUID
+ _objc_msgSend$latestToVendAssetSetUUID
+ _objc_msgSend$previouslyVendedLockedAtomicInstances
+ _objc_msgSend$previouslyVendedLockedSummary
+ _objc_msgSend$sendMobileAssetHealthReport:commonFields:sessionId:
+ _objc_msgSend$setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:
+ _objc_msgSend$setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:
+ _objc_msgSend$setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:
+ _objc_msgSend$setConfigurationPreviouslyVendedLockedAtomicInstances:
+ _objc_msgSend$setConfigurationRemovedAtomicInstance:fromLocation:
+ _objc_msgSend$setFilesystemFileExistAtPathCache:
+ _objc_msgSend$setFilesystemStartupLookupCount:
+ _objc_msgSend$setIdentifier
+ _objc_msgSend$setLastCheckedDate:
+ _objc_msgSend$setLastestToVendIsLocked:
+ _objc_msgSend$setLastestToVendMatchesSetConfig:
+ _objc_msgSend$setLatestDiscoveredAssetSetUUID:
+ _objc_msgSend$setLatestToVendAssetSetUUID:
+ _objc_msgSend$setPreviouslyVendedLockedAtomicInstances:
+ _objc_msgSend$setSetIdentifier:
+ _objc_msgSend$shortUUID:
+ _objc_msgSend$trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:
+ _objc_msgSend$trimmedSetIdentifier:
+ _objc_msgSend$uploadTaskWithRequest:fromData:
+ formattedDate:.formatter
+ formattedDate:.onceToken
- -[MADAutoAssetControlManager _clearAtomicInstanceFromLatestToVend:fromLocation:]
- -[MADAutoAssetControlManager _clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:]
- -[MADAutoAssetControlManager setConfigurationRemovedAtomicInstance:]
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
- -[MADAutoSetConfiguration previouslyVendedLockedAtomicInstance]
- -[MADAutoSetConfiguration setPreviouslyVendedLockedAtomicInstance:]
- -[MobileAssetHealthReport getHealthReport]
- GCC_except_table134
- GCC_except_table141
- GCC_except_table174
- GCC_except_table255
- GCC_except_table413
- GCC_except_table43
- GCC_except_table593
- GCC_except_table595
- GCC_except_table601
- GCC_except_table603
- GCC_except_table617
- GCC_except_table749
- GCC_except_table93
- OBJC_IVAR_$_MADAutoSetConfiguration._previouslyVendedLockedAtomicInstance
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2116
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2289
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2227
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2239
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2270
- __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1080
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2171
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2172
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1854
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1855
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1861
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1815
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2287
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2481
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2482
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3262
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3263
- ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke
- ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke_2
- __block_literal_global.1082
- __block_literal_global.2030
- __block_literal_global.2052
- __block_literal_global.2206
- __block_literal_global.2213
- __block_literal_global.2217
- __block_literal_global.2222
- __block_literal_global.2233
- __block_literal_global.2241
- __block_literal_global.2249
- __block_literal_global.2257
- __block_literal_global.2265
- __block_literal_global.2273
- __block_literal_global.2316
- __block_literal_global.2344
- __block_literal_global.2346
- __block_literal_global.3916
- __block_literal_global.4876
- _objc_msgSend$_clearAtomicInstanceFromLatestToVend:fromLocation:
- _objc_msgSend$_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:
- _objc_msgSend$getHealthReport
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
- _objc_msgSend$previouslyVendedLockedAtomicInstance
- _objc_msgSend$setConfigurationRemovedAtomicInstance:
- _objc_msgSend$setPreviouslyVendedLockedAtomicInstance:
CStrings:
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} altered set-configuration previouslyVendedLockedAtomicInstance | setConfiguration:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping locked atomic-instance (not latest-to-vend) (not previously-latest-still-locked) | setAtomicInstance:%{public}@"
+ "\n[STARTUP-STATE] [FILESYSTEM-CACHE] %{public}@"
+ "                      clientDomainName:        %@\n                    assetSetIdentifier:        %@\n                configuredAssetEntries:        %@\n             atomicInstancesDownloaded:        %@\n               catalogCachedAssetSetID:        %@\n             catalogDownloadedFromLive:        %@\n                catalogLastTimeChecked:        %@\n                     catalogPostedDate:        %@\n         newerAtomicInstanceDiscovered:        %@\n          newerDiscoveredAtomicEntries:        %@\n              latestDownloadedInstance:        %@\nlatestDownloadedAtomicInstanceFromPreSUStaging:%@\n        latestDowloadedInstanceEntries:        %@\n     downloadedCatalogCachedAssetSetID:        %@\n   downloadedCatalogDownloadedFromLive:        %@\n      downloadedCatalogLastTimeChecked:        %@\n           downloadedCatalogPostedDate:        %@\n                  currentNotifications:        %@\n                     currentNeedPolicy:        %@\n                currentSchedulerPolicy:        %@\n                   currentStagerPolicy:        %@\n            haveReceivedLookupResponse:        %@\n vendingAtomicInstanceForConfigEntries:        %@\n                 downloadUserInitiated:        %@\n                      downloadProgress:        \n%@\n                downloadedNetworkBytes:        %ld\n             downloadedFilesystemBytes:        %ld\n                      currentLockUsage:        \n%@\n                   selectorsForStaging:        %@\n                  availableForUseError:        %@\n                     newerVersionError:        %@\n"
+ "%@:_clearAtomicInstanceFromAllSetConfigurations"
+ "%@:_clearAtomicInstanceFromSetConfiguration"
+ "%@:setConfigurationAllPreviouslyVendedForceUnlock"
+ "%@:setConfigurationForgetIfTrackedAsPreviouslyVended"
+ "%@:setConfigurationIsTrackedAsPreviouslyVended"
+ "%@:setConfigurationRemovedAtomicInstance"
+ "%@:setConfigurationTrackAsPreviouslyVended"
+ "%@:setDescriptorAllDiscoveredEntriesDownloaded"
+ "%@:setDescriptorAllEntriesDownloaded"
+ "2.5.9"
+ "@248@0:8@16@24@32@40@48@56@64@72@80@88@96B104@108@116@124@132@140@148@156@164@172B180B184B188@192q200q208@216@224@232@240"
+ "AvailErr"
+ "B40@0:8@16@24^B32"
+ "Could not remove Splunk file: %{public}@, error: %{public}@"
+ "DirectoryExists"
+ "DoesNotExist"
+ "FileExists"
+ "HIT"
+ "LastCheckedDate"
+ "MA"
+ "MADAutoAssetSetHealthReport"
+ "MAHR-%@"
+ "MISS"
+ "Sending splunk event:\n%{public}@"
+ "Sending splunk event; session id: %{public}@"
+ "SetID"
+ "Starting built-in MobileAsset brain built Mar  3 2025 21:57:08"
+ "Starting downloaded MobileAsset brain (version: %@) built Mar  3 2025 21:57:08"
+ "T@\"NSDate\",&,V_LastCheckedDate"
+ "T@\"NSError\",&,V_availableForUseError"
+ "T@\"NSError\",&,V_newerVersionError"
+ "T@\"NSMutableArray\",&,N,V_previouslyVendedLockedAtomicInstances"
+ "T@\"NSMutableDictionary\",&,N,V_filesystemFileExistAtPathCache"
+ "T@\"NSString\",&,V_latestDiscoveredAssetSetUUID"
+ "T@\"NSString\",&,V_latestToVendAssetSetUUID"
+ "T@\"NSString\",&,V_setIdentifier"
+ "TB,V_lastestToVendIsLocked"
+ "TB,V_lastestToVendMatchesSetConfig"
+ "Tq,N,V_filesystemStartupLookupCount"
+ "VendingConfig"
+ "VendingLatest"
+ "Y(%ld)[%@"
+ "[%{public}@] {jobDescriptorOnFilesystemValidated} asset file does not exist | jobDescriptor:%{public}@ | localURLForDescriptor:%{public}@"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)(fromPSUS:%@)|previousAI:%@(ticks:%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] [FILESYSTEM-CACHE] {%{public}@:trackPerformanceFilesystemExistCheck} [%{public}@] | cachedInfo:%{public}@ | filePath:%{public}@"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} no descriptors failed migration"
+ "[MobileAssetHealthReport] Submitting to CoreAnalytics:\nID: %{public}@\nReports: %{public}@\n"
+ "[MobileAssetHealthReport] Submitting to Splunk:\nID: %{public}@\nReports: %{public}@\nCommonFields: %{public}@"
+ "[MobileAssetHealthReport]: %@ is set, not sending out the event"
+ "[MobileAssetHealthReport]: CoreAnalytics is not available"
+ "[MobileAssetHealthReport]: Submitting CoreAnalytics MAHR: %{public}@"
+ "[clientName:%@|setEntries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)|previousAI:%@(ticks:%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[%ld])|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@]"
+ "_LastCheckedDate"
+ "_clearAtomicInstanceFromAllSetConfigurations:fromLocation:"
+ "_clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:"
+ "_filesystemCachedInfo:forPath:"
+ "_filesystemFileExistAtPathCache"
+ "_filesystemStartupLookupCount"
+ "_lastestToVendIsLocked"
+ "_lastestToVendMatchesSetConfig"
+ "_latestDiscoveredAssetSetUUID"
+ "_latestToVendAssetSetUUID"
+ "_previouslyVendedLockedAtomicInstances"
+ "_setIdentifier"
+ "_submitReportToCoreAnalytics:commonFields:sessionId:"
+ "_submitReportToSplunk:commonFields:sessionId:"
+ "altered previouslyVendedLocked (not accessible on startup)"
+ "arrayByAddingObject:"
+ "bucketedDays:"
+ "cleared previoulsy-vended (dropAtomicInstance)"
+ "cleared previoulsy-vended (forceUnlockAtomicInstance)"
+ "cleared previoulsy-vended (nextForgetPreviouslyVendedAtomicInstance)"
+ "com.apple.mobileassetd.AutoAssetSet.DailyHealthReport"
+ "errorSummaryForSplunk:"
+ "eventPayloadForCoreAnalytics"
+ "eventPayloadForSplunk"
+ "filesystemDoesDirectoryExist:atPath:isDirectory:"
+ "filesystemDoesFileExist:atPath:"
+ "filesystemFileExistAtPathCache"
+ "filesystemFileExistAtPathCache:%ld | filesystemStartupLookupCount:%ld"
+ "filesystemStartupLookupCount"
+ "formattedDate:"
+ "getHealthReports"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "lastestToVendIsLocked"
+ "lastestToVendMatchesSetConfig"
+ "latestDiscoveredAssetSetUUID"
+ "latestToVendAssetSetUUID"
+ "o\x0f\x03\x11\x1f\b\x112Rh"
+ "previouslyVendedLockedAtomicInstances"
+ "previouslyVendedLockedSummary"
+ "s:\n"
+ "sendMobileAssetHealthReport:commonFields:sessionId:"
+ "setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:"
+ "setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:"
+ "setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:"
+ "setConfigurationPreviouslyVendedLockedAtomicInstances:"
+ "setConfigurationRemovedAtomicInstance:fromLocation:"
+ "setConfigurationTrackAsPreviouslyVended:forSetConfiguration:addingAtomicInstance:"
+ "setFilesystemFileExistAtPathCache:"
+ "setFilesystemStartupLookupCount:"
+ "setIdentifier"
+ "setLastCheckedDate:"
+ "setLastestToVendIsLocked:"
+ "setLastestToVendMatchesSetConfig:"
+ "setLatestDiscoveredAssetSetUUID:"
+ "setLatestToVendAssetSetUUID:"
+ "setPreviouslyVendedLockedAtomicInstances:"
+ "setSetIdentifier:"
+ "shortUUID:"
+ "trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:"
+ "trimmedSetIdentifier:"
+ "uploadTaskWithRequest:fromData:"
+ "v44@0:8@16@24q32B40"
+ "{%@} previouslyVendedLockedAtomicInstances count of 0 yet present | setConfiguration:%@"
+ "{%@} set-atomic-instance without atomicInstanceUUID | hadBeenLatestAtomicInstance:%@"
+ "{%@} setConfigurationTrackAsPreviouslyVended nil atomic-instance-UUID | setConfiguration:%@"
+ "{%@} ticksUntilPreviousForceUnlocked at 0 yet no previouslyVendedLockedAtomicInstances | setConfiguration:%@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] additional latest-to-vend moved to previously-vended-still-locked | hadBeenLatestAtomicInstance:%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] all previously vended force-unlocked | dropped atomic-instance%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] all previously vended force-unlocked | previouslyVendedSetDescriptor:%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] first latest-to-vend moved to previously-vended-still-locked | hadBeenLatestAtomicInstance:%{public}@"
+ "{setConfigurationPreviouslyVendedLockedAtomicInstances} set-configuration previouslyVendedLockedAtomicInstances references orphan atomic-instance | nextPreviouslyVendedStillLockedUUID:%@ | setConfiguration:%@"
+ "{setConfigurationPreviouslyVendedLockedAtomicInstances} set-configuration with invalid previouslyVendedLockedAtomicInstances | setConfiguration:%@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} clearing set-configuration previouslyVendedLockedAtomicInstance | setConfiguration:%{public}@"
- "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping locked atomic-instance (not latest-to-vend) | setAtomicInstance:%{public}@"
- "                      clientDomainName:        %@\n                    assetSetIdentifier:        %@\n                configuredAssetEntries:        %@\n             atomicInstancesDownloaded:        %@\n               catalogCachedAssetSetID:        %@\n             catalogDownloadedFromLive:        %@\n                catalogLastTimeChecked:        %@\n                     catalogPostedDate:        %@\n         newerAtomicInstanceDiscovered:        %@\n          newerDiscoveredAtomicEntries:        %@\n              latestDownloadedInstance:        %@\nlatestDownloadedAtomicInstanceFromPreSUStaging:%@\n        latestDowloadedInstanceEntries:        %@\n        previouslyVendedLockedInstance:        %@\n     downloadedCatalogCachedAssetSetID:        %@\n   downloadedCatalogDownloadedFromLive:        %@\n      downloadedCatalogLastTimeChecked:        %@\n           downloadedCatalogPostedDate:        %@\n                  currentNotifications:        %@\n                     currentNeedPolicy:        %@\n                currentSchedulerPolicy:        %@\n                   currentStagerPolicy:        %@\n            haveReceivedLookupResponse:        %@\n vendingAtomicInstanceForConfigEntries:        %@\n                 downloadUserInitiated:        %@\n                      downloadProgress:        \n%@\n                downloadedNetworkBytes:        %ld\n             downloadedFilesystemBytes:        %ld\n                      currentLockUsage:        \n%@\n                   selectorsForStaging:        %@\n                  availableForUseError:        %@\n                     newerVersionError:        %@\n"
- "%@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, however, download appears to be complete. Previous Total Downloaded: %lld, Total Expected: %lld"
- "%{public}@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, likely stalled."
- ",force-unlocked previouslyVendedLocked"
- "2.5.8"
- "Could not remove Splunk file: %{public}@"
- "Migrated"
- "Starting built-in MobileAsset brain built Feb 25 2025 22:16:34"
- "Starting downloaded MobileAsset brain (version: %@) built Feb 25 2025 22:16:34"
- "T@\"NSString\",&,N,V_previouslyVendedLockedAtomicInstance"
- "[%{public}@] {jobDescriptorOnFilesystemValidated} asset file does not exist | jobDescriptor:%{public}@, localURLForDescriptor:%{public}@"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)(fromPSUS:%@)|previousAI:%@(%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
- "[MobileAssetHealthReport]: %@ is set, not sending the event to Splunk"
- "[MobileAssetHealthReport]: Submitting health report %{public}@"
- "[clientName:%@|setEntries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)|previousAI:%@(%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
- "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[%ld])(previous:%@)|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@]"
- "_clearAtomicInstanceFromLatestToVend:fromLocation:"
- "_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:"
- "cleared previouslyVendedLocked (not accessible on startup)"
- "getHealthReport"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
- "o\x0f\x03\x1f\b\x112Rh"
- "setConfigurationRemovedAtomicInstance"
- "setConfigurationRemovedAtomicInstance:"
- "setPreviouslyVendedLockedAtomicInstance:"
- "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] new latest-to-vend when had previously-vended-still-locked so forcing unlock of older | hadBeenPreviousLockedAtomicInstance:%{public}@"
- "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] new latest-to-vend when older latest-to-vend is locked - beginning countdown to force-unlocked | hadBeenLatestAtomicInstance:%{public}@"
- "{setConfigurationTickForPreviouslyVended}"
- "{setConfigurationTickForPreviouslyVended}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] countdown time complete - force-unlocked | previouslyVendedSetDescriptor:%{public}@"
- "{setConfigurationTickForPreviouslyVended} ticksUntilPreviousForceUnlocked at 0 yet no previouslyVendedLockedAtomicInstance nextSetConfiguration:%@"

```
