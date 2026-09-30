## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.80.19.0.0
-  __TEXT.__text: 0x301a88
-  __TEXT.__auth_stubs: 0x2cb0
-  __TEXT.__objc_stubs: 0x24540
-  __TEXT.__objc_methlist: 0x11364
-  __TEXT.__const: 0x7bd18
-  __TEXT.__objc_methname: 0x416db
-  __TEXT.__objc_classname: 0xf07
-  __TEXT.__objc_methtype: 0x41eb
-  __TEXT.__cstring: 0x3da7b
-  __TEXT.__oslogstring: 0x55f87
-  __TEXT.__gcc_except_tab: 0xd9a4
+1837.80.25.0.0
+  __TEXT.__text: 0x304a08
+  __TEXT.__auth_stubs: 0x2cd0
+  __TEXT.__objc_stubs: 0x247e0
+  __TEXT.__objc_methlist: 0x1148c
+  __TEXT.__const: 0x7bd38
+  __TEXT.__objc_methname: 0x422bb
+  __TEXT.__objc_classname: 0xf08
+  __TEXT.__objc_methtype: 0x4304
+  __TEXT.__cstring: 0x3e28b
+  __TEXT.__oslogstring: 0x563c7
+  __TEXT.__gcc_except_tab: 0xda08
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x14cc
+  __TEXT.__swift5_typeref: 0x14d2
   __TEXT.__constg_swiftt: 0x18a8
   __TEXT.__swift5_reflstr: 0x951
   __TEXT.__swift5_fieldmd: 0x13f8

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x60e8
+  __TEXT.__unwind_info: 0x6110
   __TEXT.__eh_frame: 0x346c
-  __DATA_CONST.__auth_got: 0x1668
-  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__auth_got: 0x1678
+  __DATA_CONST.__got: 0x8e8
   __DATA_CONST.__auth_ptr: 0xaf8
   __DATA_CONST.__const: 0x9c50
-  __DATA_CONST.__cfstring: 0x2f840
+  __DATA_CONST.__cfstring: 0x2fb20
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0c8
+  __DATA_CONST.__objc_selrefs: 0xa190
   __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x1278
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x16728
+  __DATA.__objc_const: 0x16870
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x890
+  __DATA.__objc_classrefs: 0x898
   __DATA.__objc_superrefs: 0x310
-  __DATA.__objc_ivar: 0x1534
+  __DATA.__objc_ivar: 0x154c
   __DATA.__objc_data: 0x2d18
-  __DATA.__data: 0x2cf0
+  __DATA.__data: 0x2d00
   __DATA.__bss: 0x66a8
   __DATA.__common: 0x98
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3810FD1B-BDA1-3F02-91F1-12BED5039A31
-  Functions: 9448
-  Symbols:   17336
-  CStrings:  24597
+  UUID: C9F97099-1FDB-31E5-BD48-96FE54A6D674
+  Functions: 9475
+  Symbols:   17389
+  CStrings:  24697
 
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
+ GCC_except_table323
+ GCC_except_table336
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table361
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table434
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table534
+ GCC_except_table596
+ GCC_except_table634
+ GCC_except_table636
+ GCC_except_table642
+ GCC_except_table644
+ GCC_except_table661
+ GCC_except_table691
+ GCC_except_table798
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table804
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagerFromOSBuild
+ OBJC_IVAR_$_MADAutoAssetJob._assetOriginType
+ OBJC_IVAR_$_MADAutoSetAtomicInstance._stagedFromOSBuild
+ OBJC_IVAR_$_MADAutoSetDescriptor._allEntriesFromFactoryPreinstalled
+ OBJC_IVAR_$_MANAutoAssetSetStatus._latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ OBJC_IVAR_$_MANAutoAssetSetStatus._latestDownloadedAtomicInstanceStagedFromOSBuild
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginEntry
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1610
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3487
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3488
+ __IVARS_MAAIRBDownloadResult
+ __block_literal_global.2548
+ __block_literal_global.4147
+ __block_literal_global.5217
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
- GCC_except_table321
- GCC_except_table330
- GCC_except_table337
- GCC_except_table338
- GCC_except_table351
- GCC_except_table352
- GCC_except_table359
- GCC_except_table363
- GCC_except_table364
- GCC_except_table371
- GCC_except_table372
- GCC_except_table375
- GCC_except_table376
- GCC_except_table380
- GCC_except_table432
- GCC_except_table438
- GCC_except_table439
- GCC_except_table530
- GCC_except_table594
- GCC_except_table631
- GCC_except_table633
- GCC_except_table639
- GCC_except_table641
- GCC_except_table658
- GCC_except_table687
- GCC_except_table794
- GCC_except_table795
- GCC_except_table796
- GCC_except_table797
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1609
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3484
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3485
- __block_literal_global.2544
- __block_literal_global.4144
- __block_literal_global.5214
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
+ "Starting built-in MobileAsset brain built Jan  4 2026 21:11:22"
+ "Starting downloaded MobileAsset brain (version: %@) built Jan  4 2026 21:11:22"
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
- "3.0.4"
- "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116@120"
- "@180@0:8@16@24@32@40@48@56@64@72B80@84@92@100@108@116B124@128q136q144B152@156@164@172"
- "@52@0:8@16@24@32B40@44"
- "@68@0:8@16@24@32B40@44@52@60"
- "@96@0:8@16@24@32@40@48@56@64q72@80@88"
- "Starting built-in MobileAsset brain built Dec  8 2025 20:19:29"
- "Starting downloaded MobileAsset brain (version: %@) built Dec  8 2025 20:19:29"
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
