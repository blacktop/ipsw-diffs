## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.80.19.0.0
-  __TEXT.__text: 0x343900
-  __TEXT.__auth_stubs: 0x2b80
-  __TEXT.__objc_stubs: 0x24420
-  __TEXT.__objc_methlist: 0x11414
-  __TEXT.__const: 0x7bce8
-  __TEXT.__objc_methname: 0x417dc
-  __TEXT.__objc_classname: 0xf25
-  __TEXT.__objc_methtype: 0x4238
-  __TEXT.__cstring: 0x3dca3
-  __TEXT.__oslogstring: 0x54a37
-  __TEXT.__gcc_except_tab: 0xd7f0
-  __TEXT.__swift5_typeref: 0x14cc
+1837.80.25.0.0
+  __TEXT.__text: 0x346c80
+  __TEXT.__auth_stubs: 0x2ba0
+  __TEXT.__objc_stubs: 0x246c0
+  __TEXT.__objc_methlist: 0x1153c
+  __TEXT.__const: 0x7bd08
+  __TEXT.__objc_methname: 0x423bc
+  __TEXT.__objc_classname: 0xf26
+  __TEXT.__objc_methtype: 0x4351
+  __TEXT.__cstring: 0x3e4a3
+  __TEXT.__oslogstring: 0x54e77
+  __TEXT.__gcc_except_tab: 0xd854
+  __TEXT.__swift5_typeref: 0x14d2
   __TEXT.__constg_swiftt: 0x18a8
   __TEXT.__swift5_reflstr: 0x951
   __TEXT.__swift5_fieldmd: 0x13f8

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x6250
+  __TEXT.__unwind_info: 0x6278
   __TEXT.__eh_frame: 0x3514
-  __DATA_CONST.__auth_got: 0x15d0
-  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__auth_got: 0x15e0
+  __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__auth_ptr: 0xa28
   __DATA_CONST.__const: 0x9de8
-  __DATA_CONST.__cfstring: 0x2f720
+  __DATA_CONST.__cfstring: 0x2fa00
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0c8
+  __DATA_CONST.__objc_selrefs: 0xa190
   __DATA_CONST.__objc_intobj: 0x1260
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x16858
+  __DATA.__objc_const: 0x169a0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x858
+  __DATA.__objc_classrefs: 0x860
   __DATA.__objc_superrefs: 0x318
-  __DATA.__objc_ivar: 0x1540
+  __DATA.__objc_ivar: 0x1558
   __DATA.__objc_data: 0x2d68
-  __DATA.__data: 0x2cf2
+  __DATA.__data: 0x2d02
   __DATA.__s_async_hook: 0x190
   __DATA.__swift56_hooks: 0xb0
   __DATA.__bss: 0x66e0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E3ABC19D-E2AD-34E0-8E54-E826CDFFBC9F
-  Functions: 9567
-  Symbols:   17423
-  CStrings:  24539
+  UUID: 844B7BD5-EE3A-34BD-891C-0D3388258C46
+  Functions: 9594
+  Symbols:   17476
+  CStrings:  24639
 
Symbols:
+ +[MADAutoAssetControlManager setExtendedAttributesForAssetOriginStory:forAssetDescriptor:withAssetOriginType:currentlyAvailableToClient:]
+ -[ASAssetMetadataUpdatePolicy usesAppleInternalServerForAssetType:]
+ -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:fromLocation:withAssetOriginType:]
+ -[MADAutoAssetControlManager _trackActiveDescriptor:withAssetOriginType:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:]
+ -[MADAutoAssetControlManager isLatestAtomicInstanceFromFactoryPreinstalled:]
+ -[MADAutoAssetControlManager latestAtomicInstanceStagedFromOSBuild:]
+ -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MADAutoAssetControlManager setExtendedAttributesForNewOSPromoted:forPromotedDescriptor:]
+ -[MADAutoAssetControlManager setStagerFromOSBuild:]
+ -[MADAutoAssetControlManager stagerFromOSBuild]
+ -[MADAutoAssetJob _getBiomeDownloadResult]
+ -[MADAutoAssetJob action_SaveOriginStoryAssetDownloaded:error:]
+ -[MADAutoAssetJob action_SaveOriginStoryJobFailedCanceled:error:]
+ -[MADAutoAssetJob assetOriginType]
+ -[MADAutoAssetJob initForDescriptor:withAssetOriginType:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:]
+ -[MADAutoAssetJob initForInstance:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:]
+ -[MADAutoAssetJob initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:]
+ -[MADAutoAssetJob initForSetConfiguration:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:]
+ -[MADAutoAssetJob initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob setAssetOriginType:]
+ -[MADAutoAssetStager _emitAirEventForDetermineRequest:requiredAssetsCount:optionalAssetsCount:error:fromCache:]
+ -[MADAutoSetAtomicInstance initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:stagedFromOSBuild:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:]
+ -[MADAutoSetAtomicInstance setStagedFromOSBuild:]
+ -[MADAutoSetAtomicInstance stagedFromOSBuild]
+ -[MADAutoSetDescriptor allEntriesFromFactoryPreinstalled]
+ -[MADAutoSetDescriptor setAllEntriesFromFactoryPreinstalled:]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MANAutoAssetSetStatus latestDownloadedAtomicInstanceFromFactoryPreinstalled]
+ -[MANAutoAssetSetStatus latestDownloadedAtomicInstanceStagedFromOSBuild]
+ -[MANAutoAssetSetStatus setLatestDownloadedAtomicInstanceFromFactoryPreinstalled:]
+ -[MANAutoAssetSetStatus setLatestDownloadedAtomicInstanceStagedFromOSBuild:]
+ GCC_except_table345
+ GCC_except_table358
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table464
+ GCC_except_table478
+ GCC_except_table479
+ GCC_except_table566
+ GCC_except_table628
+ GCC_except_table666
+ GCC_except_table670
+ GCC_except_table676
+ GCC_except_table678
+ GCC_except_table695
+ GCC_except_table725
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table835
+ GCC_except_table838
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagerFromOSBuild
+ OBJC_IVAR_$_MADAutoAssetJob._assetOriginType
+ OBJC_IVAR_$_MADAutoSetAtomicInstance._stagedFromOSBuild
+ OBJC_IVAR_$_MADAutoSetDescriptor._allEntriesFromFactoryPreinstalled
+ OBJC_IVAR_$_MANAutoAssetSetStatus._latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ OBJC_IVAR_$_MANAutoAssetSetStatus._latestDownloadedAtomicInstanceStagedFromOSBuild
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginEntry
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1566
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3498
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3499
+ __IVARS_MAAIRBDownloadResult
+ __block_literal_global.2559
+ __block_literal_global.4164
+ __block_literal_global.5238
+ _objc_msgSend$_emitAirEventForDetermineRequest:requiredAssetsCount:optionalAssetsCount:error:fromCache:
+ _objc_msgSend$_getBiomeDownloadResult
+ _objc_msgSend$_preInstalledMakeDescriptorAvailable:fromLocation:withAssetOriginType:
+ _objc_msgSend$_trackActiveDescriptor:withAssetOriginType:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:
+ _objc_msgSend$action_SaveOriginStoryAssetDownloaded:error:
+ _objc_msgSend$action_SaveOriginStoryJobFailedCanceled:error:
+ _objc_msgSend$allEntriesFromFactoryPreinstalled
+ _objc_msgSend$assetOriginType
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:stagedFromOSBuild:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:
+ _objc_msgSend$initForDescriptor:withAssetOriginType:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:
+ _objc_msgSend$initForInstance:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:
+ _objc_msgSend$initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:
+ _objc_msgSend$initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:
+ _objc_msgSend$initForSetConfiguration:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:
+ _objc_msgSend$initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initWithCellularRequest:cellularResponse:constrainedNetworkRequest:constrainedNetworkResponse:expensiveNetworkRequest:expensiveNetworkResponse:isMAAutoAsset:isDiscretionary:isUserPriority:result:bytesDownloaded:isPSUS:
+ _objc_msgSend$isLatestAtomicInstanceFromFactoryPreinstalled:
+ _objc_msgSend$latestAtomicInstanceStagedFromOSBuild:
+ _objc_msgSend$latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ _objc_msgSend$latestDownloadedAtomicInstanceStagedFromOSBuild
+ _objc_msgSend$nameOfOriginType:
+ _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$safeLLForKey:
+ _objc_msgSend$setAllEntriesFromFactoryPreinstalled:
+ _objc_msgSend$setExtendedAttributesForAssetOriginStory:forAssetDescriptor:withAssetOriginType:currentlyAvailableToClient:
+ _objc_msgSend$setExtendedAttributesForNewOSPromoted:forPromotedDescriptor:
+ _objc_msgSend$setStagerFromOSBuild:
+ _objc_msgSend$stagedFromOSBuild
+ _objc_msgSend$stagerFromOSBuild
+ _objc_msgSend$typePSUSDetermine:assetSet:assetType:requiredAssetCount:optionalAssetCount:clientDomain:targetOSVersion:lookupAssetAudience:isResponseFromCache:
+ _objc_msgSend$usesAppleInternalServerForAssetType:
+ _symbolic ypSg
- -[ASAssetMetadataUpdatePolicy isAppleInternalOverrideSetForAssetType:appleInternalPtr:]
- -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:fromLocation:]
- -[MADAutoAssetControlManager _trackActiveDescriptor:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:]
- -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
- -[MADAutoAssetJob initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:]
- -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:]
- -[MADAutoAssetJob initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:]
- -[MADAutoAssetJob initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:]
- -[MADAutoAssetJob initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:]
- -[MADAutoAssetJob initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:]
- -[MADAutoAssetJob initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
- -[MADAutoAssetJob initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
- -[MADAutoSetAtomicInstance initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:]
- GCC_except_table343
- GCC_except_table352
- GCC_except_table359
- GCC_except_table360
- GCC_except_table373
- GCC_except_table374
- GCC_except_table381
- GCC_except_table385
- GCC_except_table386
- GCC_except_table397
- GCC_except_table398
- GCC_except_table403
- GCC_except_table404
- GCC_except_table408
- GCC_except_table462
- GCC_except_table470
- GCC_except_table471
- GCC_except_table562
- GCC_except_table626
- GCC_except_table663
- GCC_except_table667
- GCC_except_table673
- GCC_except_table675
- GCC_except_table692
- GCC_except_table721
- GCC_except_table828
- GCC_except_table829
- GCC_except_table830
- GCC_except_table831
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1565
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3495
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3496
- __block_literal_global.2555
- __block_literal_global.4161
- __block_literal_global.5235
- _objc_msgSend$_preInstalledMakeDescriptorAvailable:fromLocation:
- _objc_msgSend$_trackActiveDescriptor:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:
- _objc_msgSend$initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:
- _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:
- _objc_msgSend$initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:
- _objc_msgSend$initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:
- _objc_msgSend$initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:
- _objc_msgSend$initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:
- _objc_msgSend$initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
- _objc_msgSend$initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
- _objc_msgSend$isAppleInternalOverrideSetForAssetType:appleInternalPtr:
- _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
CStrings:
+ "                                       clientDomainName: %@\n                                     assetSetIdentifier: %@\n                                 configuredAssetEntries: %@\n                              atomicInstancesDownloaded: %@\n                                catalogCachedAssetSetID: %@\n                              catalogDownloadedFromLive: %@\n                                 catalogLastTimeChecked: %@\n                                      catalogPostedDate: %@\n                          newerAtomicInstanceDiscovered: %@\n                           newerDiscoveredAtomicEntries: %@\n                               latestDownloadedInstance: %@\n         latestDownloadedAtomicInstanceFromPreSUStaging: %@\n  latestDownloadedAtomicInstanceFromFactoryPreinstalled: %@\n        latestDownloadedAtomicInstanceStagedFromOSBuild: %@\n                         latestDowloadedInstanceEntries: %@\n                      downloadedCatalogCachedAssetSetID: %@\n                    downloadedCatalogDownloadedFromLive: %@\n                       downloadedCatalogLastTimeChecked: %@\n                            downloadedCatalogPostedDate: %@\n                                   currentNotifications: %@\n                                      currentNeedPolicy: %@\n                                 currentSchedulerPolicy: %@\n                                    currentStagerPolicy: %@\n                             haveReceivedLookupResponse: %@\n                  vendingAtomicInstanceForConfigEntries: %@\n                                  downloadUserInitiated: %@\n                                       downloadProgress: \n%@\n                                 downloadedNetworkBytes: %ld\n                              downloadedFilesystemBytes: %ld\n                                       currentLockUsage: \n%@\n                                    selectorsForStaging: %@\n                                   availableForUseError: %@\n                                      newerVersionError: %@\n"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/4~CE70ugB-UTICH93HyMPCGKBaqYRFARhzf9LRi3s/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/4~CGHyugCImHJZGboNljmV8RnZc1Xhl6E7ft22ahs/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
+ "3.0.5"
+ "@104@0:8@16@24@32@40@48@56@64@72q80@88@96"
+ "@136@0:8@16@24@32@40q48@56@64@72@80@88@96@104@112B120B124@128"
+ "@192@0:8@16@24@32@40@48@56@64@72B80B84@88@96@104@112@120@128B136@140q148q156B164@168@176@184"
+ "@260@0:8@16@24@32@40@48@56@64@72@80@88@96B104B108@112@120@128@136@144@152@160@168@176@184B192B196B200@204q212q220@228@236@244@252"
+ "@48@0:8@16q24@32@40"
+ "@52@0:8@16q24@32@40B48"
+ "@60@0:8@16q24@32@40B48@52"
+ "@72@0:8@16q24@32@40@48@56@64"
+ "@72@0:8B16B20B24B28B32B36B40B44B48@52q60B68"
+ "@76@0:8@16@24@32I40I44@48@56@64B72"
+ "@76@0:8@16q24@32@40B48@52@60@68"
+ "ASSET-ORIGIN-STORY"
+ "MADJob:SaveOriginStoryAssetDownloaded"
+ "MADJob:SaveOriginStoryJobFailedCanceled"
+ "PSUS_DETERMINE_END         "
+ "PSUS_DETERMINE_START       "
+ "SaveOriginStoryAssetDownloaded"
+ "SaveOriginStoryJobFailedCanceled"
+ "Starting built-in MobileAsset brain built Jan  5 2026 21:01:29"
+ "Starting downloaded MobileAsset brain (version: %@) built Jan  5 2026 21:01:29"
+ "T@\"NSString\",&,N,V_latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "T@\"NSString\",&,N,V_stagedFromOSBuild"
+ "T@\"NSString\",&,N,V_stagerFromOSBuild"
+ "TB,N,V_allEntriesFromFactoryPreinstalled"
+ "TB,N,V_latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "Tq,N,V_assetOriginType"
+ "[%@ | instance latestDownloaded:%@(entries:%ld)%@, discovered:%@(entries:%ld)%@, requestedEntries:%ld, fullyDownloaded:%@(notified:%@) | onFilesystem:%@(incomplete:%@), neverBeenLocked:%@ | secureOperation(inProgress:%@), (elimintating:%@) | userInitiated:%@, stagedPrior:%@, allPreinstalled:%@]"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@,StagedFrom:%@|(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[ASSET_AVAILABLE_OS_BUILD] failed to set asset-available-os-build (xattr) | errno:%d\n"
+ "[ASSET_AVAILABLE_OS_BUILD] failed to set asset-available-os-build | errno:%d\n"
+ "[ASSET_AVAILABLE_OS_BUILD] successfully set asset-available-os-build (xattr) | currentOSBuild:%@\n"
+ "[ASSET_AVAILABLE_OS_BUILD] successfully set asset-available-os-build | currentOSBuild:%@\n"
+ "[ASSET_DOWNLOADED_OS_BUILD] failed to set asset-downloaded-os-build | errno:%d\n"
+ "[ASSET_DOWNLOADED_OS_BUILD] successfully set asset-downloaded-os-build | currentOSBuild:%@\n"
+ "[ASSET_ORIGIN_TYPE] failed to set asset-origin-type | errno:%d\n"
+ "[ASSET_ORIGIN_TYPE] successfully set asset-origin-type | assetOriginType:%@\n"
+ "[clientName:%@|SubAtomic:%@|StagedFrom:%@|(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requestedEntries:%ld, fullyDownloaded:%@(notified:%@) | onFilesystem:%@(incomplete:%@), neverBeenLocked:%@ | secureOperation(inProgress:%@), (elimintating:%@) | userInitiated:%@, stagedPrior:%@, allPreinstalled:%@ | catalog(cachedAssetSetID:%@), (downloadedFromLive:%@), (lastTimeChecked:%@), (postedDate:%@) | downloaded(cachedAssetSetID:%@), (downloadedFromLive:%@), (lastTimeChecked:%@), (postedDate:%@)]"
+ "__ObjC.MAAIRBDownloadResult"
+ "_allEntriesFromFactoryPreinstalled"
+ "_assetOriginType"
+ "_emitAirEventForDetermineRequest:requiredAssetsCount:optionalAssetsCount:error:fromCache:"
+ "_getBiomeDownloadResult"
+ "_latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "_latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "_preInstalledMakeDescriptorAvailable:fromLocation:withAssetOriginType:"
+ "_stagedFromOSBuild"
+ "_stagerFromOSBuild"
+ "_trackActiveDescriptor:withAssetOriginType:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:"
+ "action_SaveOriginStoryAssetDownloaded:error:"
+ "action_SaveOriginStoryJobFailedCanceled:error:"
+ "allEntriesFromFactoryPreinstalled"
+ "assetOriginType"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetAvailableOSBuild"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetDownloadedOSBuild"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetOriginType"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:stagedFromOSBuild:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:"
+ "initForDescriptor:withAssetOriginType:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:"
+ "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:"
+ "initForInstance:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:"
+ "initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:"
+ "initForSelector:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:"
+ "initForSetConfiguration:withAssetOriginType:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:"
+ "initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
+ "initForSetInstance:withAssetOriginType:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initWithCellularRequest:cellularResponse:constrainedNetworkRequest:constrainedNetworkResponse:expensiveNetworkRequest:expensiveNetworkResponse:isMAAutoAsset:isDiscretionary:isUserPriority:result:bytesDownloaded:isPSUS:"
+ "isLatestAtomicInstanceFromFactoryPreinstalled"
+ "isLatestAtomicInstanceFromFactoryPreinstalled:"
+ "latestAtomicInstanceStagedFromOSBuild:"
+ "latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "latestDownloadedAtomicInstanceFromPreInstalled"
+ "latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "nameOfOriginType:"
+ "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "safeLLForKey:"
+ "setAllEntriesFromFactoryPreinstalled:"
+ "setAssetOriginType:"
+ "setExtendedAttributesForAssetOriginStory:forAssetDescriptor:withAssetOriginType:currentlyAvailableToClient:"
+ "setExtendedAttributesForNewOSPromoted:forPromotedDescriptor:"
+ "setLatestDownloadedAtomicInstanceFromFactoryPreinstalled:"
+ "setLatestDownloadedAtomicInstanceStagedFromOSBuild:"
+ "setStagedFromOSBuild:"
+ "setStagerFromOSBuild:"
+ "stagedFromOSBuild"
+ "stagerFromOSBuild"
+ "typePSUSDetermine:assetSet:assetType:requiredAssetCount:optionalAssetCount:clientDomain:targetOSVersion:lookupAssetAudience:isResponseFromCache:"
+ "usesAppleInternalServerForAssetType:"
+ "v40@0:8B16I20I24@28B36"
+ "v88@0:8@16q24@32@40@48@56@64@72@80"
+ "{%@:newAtomicInstanceAndSetDescriptor} unable to allocate already-downloaded-atomic-entry | alreadyDownloadedDescriptor:%@"
+ "{%@:setExtendedAttributesForNewOSPromoted} base repository location does not exist (xattr) | assetDescriptor:%@ | localContentURL:%@"
+ "{%@:setExtendedAttributesForNewOSPromoted} base repository location is not a directory (xattr) | assetDescriptor:%@ | localContentURL:%@"
+ "{%{public}@:setExtendedAttributesForAssetOriginStory} base repository location does not exist | assetDescriptor:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@:setExtendedAttributesForAssetOriginStory} base repository location is not a directory | assetDescriptor:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@:setExtendedAttributesForAssetOriginStory} extended attributes successfully recorded | assetDescriptor:%{public}@ | localContentURL:%{public}@ | xattrFlow:\n%{public}@"
+ "{%{public}@:setExtendedAttributesForAssetOriginStory} failed to set extended attributes | assetDescriptor:%{public}@ | localContentURL:%{public}@ | xattrFlow:\n%{public}@"
+ "{%{public}@:setExtendedAttributesForNewOSPromoted} extended attributes successfully recorded (xattr) | assetDescriptor:%{public}@ | localContentURL:%{public}@ | xattrFlow:\n%{public}@"
+ "{%{public}@:setExtendedAttributesForNewOSPromoted} failed to set extended attributes (xattr) | assetDescriptor:%{public}@ | localContentURL:%{public}@ | xattrFlow:\n%{public}@"
- "                      clientDomainName:        %@\n                    assetSetIdentifier:        %@\n                configuredAssetEntries:        %@\n             atomicInstancesDownloaded:        %@\n               catalogCachedAssetSetID:        %@\n             catalogDownloadedFromLive:        %@\n                catalogLastTimeChecked:        %@\n                     catalogPostedDate:        %@\n         newerAtomicInstanceDiscovered:        %@\n          newerDiscoveredAtomicEntries:        %@\n              latestDownloadedInstance:        %@\nlatestDownloadedAtomicInstanceFromPreSUStaging:%@\n        latestDowloadedInstanceEntries:        %@\n     downloadedCatalogCachedAssetSetID:        %@\n   downloadedCatalogDownloadedFromLive:        %@\n      downloadedCatalogLastTimeChecked:        %@\n           downloadedCatalogPostedDate:        %@\n                  currentNotifications:        %@\n                     currentNeedPolicy:        %@\n                currentSchedulerPolicy:        %@\n                   currentStagerPolicy:        %@\n            haveReceivedLookupResponse:        %@\n vendingAtomicInstanceForConfigEntries:        %@\n                 downloadUserInitiated:        %@\n                      downloadProgress:        \n%@\n                downloadedNetworkBytes:        %ld\n             downloadedFilesystemBytes:        %ld\n                      currentLockUsage:        \n%@\n                   selectorsForStaging:        %@\n                  availableForUseError:        %@\n                     newerVersionError:        %@\n"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/4~CDyKugD-t2AqCtVN1mfAcSMu1x3VmcjXa-C5O7o/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/4~CDzeugBYVhKBwLaY5MyygQ-cER_aE35wvK8jTk0/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
- "3.0.4"
- "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116@120"
- "@180@0:8@16@24@32@40@48@56@64@72B80@84@92@100@108@116B124@128q136q144B152@156@164@172"
- "@52@0:8@16@24@32B40@44"
- "@68@0:8@16@24@32B40@44@52@60"
- "@96@0:8@16@24@32@40@48@56@64q72@80@88"
- "Starting built-in MobileAsset brain built Dec  5 2025 05:43:54"
- "Starting downloaded MobileAsset brain (version: %@) built Dec  5 2025 05:43:54"
- "[%@ | instance latestDownloaded:%@(entries:%ld)%@, discovered:%@(entries:%ld)%@, requestedEntries:%ld, fullyDownloaded:%@(notified:%@) | onFilesystem:%@(incomplete:%@), neverBeenLocked:%@ | secureOperation(inProgress:%@), (elimintating:%@) | userInitiated:%@, stagedPrior:%@]"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[clientName:%@|SubAtomic:%@|(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requestedEntries:%ld, fullyDownloaded:%@(notified:%@) | onFilesystem:%@(incomplete:%@), neverBeenLocked:%@ | secureOperation(inProgress:%@), (elimintating:%@) | userInitiated:%@, stagedPrior:%@ | catalog(cachedAssetSetID:%@), (downloadedFromLive:%@), (lastTimeChecked:%@), (postedDate:%@) | downloaded(cachedAssetSetID:%@), (downloadedFromLive:%@), (lastTimeChecked:%@), (postedDate:%@)]"
- "_preInstalledMakeDescriptorAvailable:fromLocation:"
- "_trackActiveDescriptor:operation:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:message:"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:"
- "initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:"
- "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:"
- "initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:"
- "initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:"
- "initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:"
- "initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:"
- "initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
- "initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
- "isAppleInternalOverrideSetForAssetType:appleInternalPtr:"
- "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
- "{%@:newAtomicInstanceAndSetDescriptorFromStaged} unable to allocate already-downloaded-atomic-entry | alreadyDownloadedDescriptor:%@"

```
