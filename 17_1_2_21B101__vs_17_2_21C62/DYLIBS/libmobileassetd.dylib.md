## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-936.42.1.0.0
-  __TEXT.__text: 0x177bcc
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0xc148
-  __TEXT.__const: 0xb50
-  __TEXT.__cstring: 0x3ba3d
-  __TEXT.__oslogstring: 0x20f69
-  __TEXT.__gcc_except_tab: 0x1438
+936.60.10.0.0
+  __TEXT.__text: 0x17a2dc
+  __TEXT.__auth_stubs: 0x1290
+  __TEXT.__objc_methlist: 0xc230
+  __TEXT.__const: 0xb60
+  __TEXT.__cstring: 0x3c095
+  __TEXT.__oslogstring: 0x21389
+  __TEXT.__gcc_except_tab: 0x1440
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x22d4
+  __TEXT.__unwind_info: 0x22f8
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_classname: 0xb34
-  __TEXT.__objc_methname: 0x2b3dd
-  __TEXT.__objc_methtype: 0x28a9
-  __TEXT.__objc_stubs: 0x19480
+  __TEXT.__objc_methname: 0x2b71f
+  __TEXT.__objc_methtype: 0x290e
+  __TEXT.__objc_stubs: 0x19680
   __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x20f8
+  __DATA_CONST.__const: 0x2100
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xddb0
-  __DATA_CONST.__objc_selrefs: 0x6f40
+  __DATA_CONST.__objc_const: 0xddf8
+  __DATA_CONST.__objc_selrefs: 0x6fd0
   __DATA_CONST.__objc_arraydata: 0x810
-  __AUTH_CONST.__cfstring: 0x26560
-  __AUTH_CONST.__objc_const: 0x3000
-  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x26860
+  __AUTH_CONST.__objc_const: 0x3048
+  __AUTH_CONST.__const: 0xa00
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__auth_got: 0x958
   __AUTH.__objc_data: 0x780
   __DATA.__objc_classrefs: 0x6a0
   __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0xf74
+  __DATA.__objc_ivar: 0xf80
   __DATA.__data: 0xd30
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimg4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 729375A4-D568-3566-B882-00456572ADF3
-  Functions: 4872
-  Symbols:   15817
-  CStrings:  17171
+  UUID: 65D72530-E339-3DC0-805B-DBF5DC87CE05
+  Functions: 4892
+  Symbols:   15879
+  CStrings:  17260
 
Symbols:
+ +[MADAutoAssetControlManager schedulerResumed:]
+ +[PallasResponseVerifier CopyDataFromEncodedBase64:range:]
+ +[PallasResponseVerifier base64DecodeString:toBuffer:length:]
+ +[PallasResponseVerifier verifyReceipt:withSignature:]
+ -[DownloadManager forceDaemonBusy]
+ -[DownloadManager setForceDaemonBusy:]
+ -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:]
+ -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:].cold.1
+ -[MADAutoAssetControlManager _removeDownloadedDescriptorsWithNewerDownloaded:]
+ -[MADAutoAssetControlManager _removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:]
+ -[MADAutoAssetControlManager _routeClientRequest:alreadyScheduledSelector:fromLocation:]
+ -[MADAutoAssetControlManager alreadyScheduledSelectors]
+ -[MADAutoAssetControlManager atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:]
+ -[MADAutoAssetControlManager atomicInstanceRemovedSetJob:removingForReason:]
+ -[MADAutoAssetControlManager handleClientPotentialJob:alreadyScheduledSelector:forAutoJob:fromLocation:]
+ -[MADAutoAssetControlManager isDescriptorManagedAsSet:]
+ -[MADAutoAssetControlManager scheduledJobsResumed:]
+ -[MADAutoAssetControlManager setAlreadyScheduledSelectors:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:].cold.1
+ -[MADAutoAssetControlManagerParam initWithScheduledJobs:]
+ -[MADAutoAssetControlManagerParam scheduledJobs]
+ -[MADAutoAssetControlManagerParam setScheduledJobs:]
+ -[MADAutoAssetJob adoptCachedLookupResult:]
+ -[MADAutoAssetJob buildPotentialDescriptors:fromLookupResults:buildingPatchDescriptors:andFullDescriptors:]
+ -[MADAutoAssetJob foundAndDownloadedSet:]
+ -[MADAutoAssetJob isSetFoundAlreadyOnFilesystem:justPromotedAnyDescriptor:]
+ -[MADAutoAssetJob newFoundSetDescriptorsFromCachedLookup:]
+ -[MADAutoAssetScheduler _snapshotOfJobsBySelector]
+ GCC_except_table124
+ GCC_except_table131
+ GCC_except_table150
+ GCC_except_table225
+ GCC_except_table418
+ GCC_except_table42
+ GCC_except_table423
+ GCC_except_table81
+ GCC_except_table84
+ _OBJC_IVAR_$_DownloadManager._forceDaemonBusy
+ _OBJC_IVAR_$_MADAutoAssetControlManager._alreadyScheduledSelectors
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._scheduledJobs
+ __OBJC_$_CLASS_METHODS_PallasResponseVerifier
+ ___23-[DownloadManager init]_block_invoke
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.782
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.782.cold.1
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.789
+ ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.794
+ ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1662
+ ___block_literal_global.1593
+ ___block_literal_global.1604
+ ___block_literal_global.1612
+ ___block_literal_global.1620
+ ___block_literal_global.1628
+ ___block_literal_global.1636
+ ___block_literal_global.1644
+ ___block_literal_global.1652
+ ___block_literal_global.1660
+ ___block_literal_global.1914
+ ___block_literal_global.1963
+ ___block_literal_global.2469
+ ___block_literal_global.3039
+ ___block_literal_global.823
+ ___block_literal_global.828
+ ___block_literal_global.844
+ ___memcpy_chk
+ __unnamed_array_storage.1868
+ __unnamed_array_storage.1954
+ __unnamed_array_storage.2215
+ __unnamed_array_storage.2216
+ __unnamed_array_storage.2221
+ __unnamed_array_storage.2222
+ __unnamed_array_storage.2307
+ __unnamed_array_storage.2308
+ _getRepositoryDownloadsPath
+ _kMobileAssetPreferencesMABrainForceStartupBusy
+ _moveTargetPathToDirectory
+ _moveTargetURLToDirectory
+ _objc_msgSend$CopyDataFromEncodedBase64:range:
+ _objc_msgSend$_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:
+ _objc_msgSend$_removeDownloadedDescriptorsWithNewerDownloaded:
+ _objc_msgSend$_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:
+ _objc_msgSend$_routeClientRequest:alreadyScheduledSelector:fromLocation:
+ _objc_msgSend$_snapshotOfJobsBySelector
+ _objc_msgSend$adoptCachedLookupResult:
+ _objc_msgSend$alreadyScheduledSelectors
+ _objc_msgSend$atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:
+ _objc_msgSend$atomicInstanceRemovedSetJob:removingForReason:
+ _objc_msgSend$base64DecodeString:toBuffer:length:
+ _objc_msgSend$buildPotentialDescriptors:fromLookupResults:buildingPatchDescriptors:andFullDescriptors:
+ _objc_msgSend$data
+ _objc_msgSend$foundAndDownloadedSet:
+ _objc_msgSend$handleClientPotentialJob:alreadyScheduledSelector:forAutoJob:fromLocation:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$initWithScheduledJobs:
+ _objc_msgSend$isDescriptorManagedAsSet:
+ _objc_msgSend$isSetFoundAlreadyOnFilesystem:justPromotedAnyDescriptor:
+ _objc_msgSend$newFoundSetDescriptorsFromCachedLookup:
+ _objc_msgSend$scheduledJobsResumed:
+ _objc_msgSend$schedulerResumed:
+ _objc_msgSend$setAlreadyScheduledSelectors:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$verifyReceipt:withSignature:
+ _rename
- +[MADAutoAssetControlManager schedulerResumed]
- -[MADAutoAssetControlManager _removeDownloadedDescriptorsWithNewerDownloaded]
- -[MADAutoAssetControlManager _routeClientRequest:fromLocation:]
- -[MADAutoAssetControlManager atomicInstanceRemove:setAtomicInstanceUUID:]
- -[MADAutoAssetControlManager atomicInstanceRemovedSetJob:]
- -[MADAutoAssetControlManager handleClientPotentialJob:forAutoJob:fromLocation:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:].cold.1
- -[MADAutoAssetJob foundAndDownloadedSet:forJobParam:]
- -[MADAutoAssetJob isSetFoundAlreadyOnFilesystem]
- GCC_except_table123
- GCC_except_table130
- GCC_except_table149
- GCC_except_table222
- GCC_except_table41
- GCC_except_table416
- GCC_except_table419
- GCC_except_table6
- GCC_except_table82
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.784
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.784.cold.1
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.791
- ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.796
- ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1665
- ___block_literal_global.1596
- ___block_literal_global.1607
- ___block_literal_global.1615
- ___block_literal_global.1623
- ___block_literal_global.1631
- ___block_literal_global.1639
- ___block_literal_global.1647
- ___block_literal_global.1655
- ___block_literal_global.1663
- ___block_literal_global.1902
- ___block_literal_global.1951
- ___block_literal_global.2457
- ___block_literal_global.3030
- ___block_literal_global.736
- ___block_literal_global.820
- ___block_literal_global.825
- ___block_literal_global.846
- __unnamed_array_storage.1856
- __unnamed_array_storage.1942
- __unnamed_array_storage.2203
- __unnamed_array_storage.2204
- __unnamed_array_storage.2209
- __unnamed_array_storage.2210
- __unnamed_array_storage.2295
- __unnamed_array_storage.2296
- _b64_decode
- _base64Decode
- _base64UrlDecode
- _objc_msgSend$_removeDownloadedDescriptorsWithNewerDownloaded
- _objc_msgSend$_routeClientRequest:fromLocation:
- _objc_msgSend$atomicInstanceRemove:setAtomicInstanceUUID:
- _objc_msgSend$atomicInstanceRemovedSetJob:
- _objc_msgSend$foundAndDownloadedSet:forJobParam:
- _objc_msgSend$handleClientPotentialJob:forAutoJob:fromLocation:
- _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
- _objc_msgSend$initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$isSetFoundAlreadyOnFilesystem
- _objc_msgSend$schedulerResumed
- _verifyReceipt
CStrings:
+ "\x11\x1f\x0f\t"
+ "%@:_removeDownloadedSetDescriptorWithNewerDownloaded"
+ "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld(set:%ld)|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
+ "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld(set:%ld)|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
+ "%{public}@ {%{public}@:isSetFoundAlreadyOnFilesystem} latest version on fliesystem | assetVersion:%{public}@, for assetSpecifier:%{public}@,"
+ "%{public}@ | {%{public}@} filtering out asset (additional full of less-preferred format) | filtered:%{public}@"
+ "%{public}@ | {%{public}@} filtering out asset (additional patch of less-preferred format) | filtered:%{public}@"
+ "%{public}@ | {%{public}@} filtering out asset (empty entry) | metadata:%{public}@"
+ "%{public}@ | {%{public}@} filtering out asset (specifier not requested) | response specifier:%{public}@ | filtered:%{public}@"
+ "%{public}@ | {%{public}@} full provided | considering:%{public}@"
+ "%{public}@ | {%{public}@} mixture of Ramping indications - considering overall set as NOT ramped | nextAsset:%{public}@"
+ "%{public}@ | {%{public}@} more preferred full provided | now considering:%{public}@"
+ "%{public}@ | {%{public}@} more preferred patch provided | now considering:%{public}@"
+ "%{public}@ | {%{public}@} no assets provided (and no latest-installed atomic-instance)"
+ "%{public}@ | {%{public}@} patch provided | considering:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_snapshotOfJobsBySelector} unable to load scheduledJob entry"
+ "+[MABrainBundle stageProposed:error:]"
+ "+[PallasResponseVerifier CopyDataFromEncodedBase64:range:]"
+ "+[PallasResponseVerifier verifyReceipt:withSignature:]"
+ "-[DownloadManager init]_block_invoke"
+ "-[MABrainBundle stageCurrent:]"
+ "/\x0f\x1f\x11\"c"
+ "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/downloadDir"
+ "@312@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248B256B260@264@272@280@288@296@304"
+ "@40@0:8@16{_NSRange=QQ}24"
+ "B32@0:8@16^B24"
+ "B44@0:8@16B24@28@36"
+ "CopyDataFromEncodedBase64:range:"
+ "DawnC"
+ "Failed to remove temporary files with error: %@"
+ "Forcing MA Brain to be busy during startup for %@ seconds"
+ "MA Brain force busy timer fired - allowing downloads now (%ld)"
+ "MA Brain not busy, but going into artificial delayed sync mode"
+ "MABrainForceStartupBusy"
+ "Pallas JWS parsing did not yield 3 elements, elements: %lu bytes: %s"
+ "SCHEDULED_JOBS|scheduledJobs:%ld"
+ "Starting built-in MobileAsset brain built Nov 12 2023 07:43:21"
+ "Starting downloaded MobileAsset brain (version: %@) built Nov 12 2023 07:43:21"
+ "T@\"NSMutableDictionary\",&,N,V_alreadyScheduledSelectors"
+ "TB,N,V_forceDaemonBusy"
+ "Unable to move current mabrain, returned %d errno: %d"
+ "Unable to move proposed mabrain, returned %d errno: %d"
+ "[%{public}@]\n[REMOVAL] (%{public}@) {%{public}@} unable to load persisted-set-atomic-instance file | nextRemoveSetInstance:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@e} (%{public}@) NOT removing by UUID | nextSetAtomicInstance:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} (%{public}@) removing by UUID | nextSetAtomicInstance:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} encountered blank auto-asset-descriptor - removing | downloadedAssetDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} encountered downloaded descriptor not on the filesystem - ignored | downloadedAssetDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} nil downloadedAssetDescriptor"
+ "[%{public}@]\n[REMOVAL] {%{public}@} not considering for removal since currently locked | keepingDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} not considering for removal since found by lookup with asset-version | keepingDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} not considering for removal since no newer on filesystem | keepingDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} removing older downloaded descriptor | removingDescriptor:%{public}@, keepingDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} removing | removeDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeAllUnlockedForOtherAtomicInstances} %{public}@ | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeAllUnlockedForOtherAtomicInstances} cannot remove - currently locked | nextSetDescriptor:%{public}@ | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeAllUnlockedForOtherAtomicInstances} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeAllUnlockedForOtherAtomicInstances} unable to load set-descriptor | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} no persisted known-descriptors"
+ "[%{public}@]\n[REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} removing | removeDescriptor:%{public}@"
+ "[%{public}@]\n[REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} atomic-instance without backing set-descriptor | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance with no asset-entries on filesystem | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance without backing set-descriptor | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} unable to load set-atomic-instance | entryID:%{public}@"
+ "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [PREVIOUSLY_QUEUED] | [schedule and] route client-request that had been awaiting first-unlock | jobParam:%{public}@"
+ "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [PREVIOUSLY_QUEUED] | [schedule and] route client-request | jobParam:%{public}@"
+ "[%{public}@] {%{public}@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} [PREVIOUSLY_QUEUED] | [schedule and] route client-request | jobParam:%{public}@"
+ "_alreadyScheduledSelectors"
+ "_decideRemoveDescriptorWithNewerDownloaded"
+ "_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:"
+ "_forceDaemonBusy"
+ "_removeDownloadedDescriptorsWithNewerDownloaded:"
+ "_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:"
+ "_routeClientRequest:alreadyScheduledSelector:fromLocation:"
+ "_snapshotOfJobsBySelector"
+ "adoptCachedLookupResult:"
+ "alreadyScheduledSelectors"
+ "atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:"
+ "atomicInstanceRemovedSetJob:removingForReason:"
+ "base64DecodeString:toBuffer:length:"
+ "buildPotentialDescriptors:fromLookupResults:buildingPatchDescriptors:andFullDescriptors:"
+ "dropping stale entries"
+ "failure where atomic-instance never reached downloaded stage"
+ "forceDaemonBusy"
+ "foundAndDownloadedSet:"
+ "handleClientPotentialJob:alreadyScheduledSelector:forAutoJob:fromLocation:"
+ "initWithLength:"
+ "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "initWithScheduledJobs:"
+ "isDescriptorManagedAsSet:"
+ "isSetFoundAlreadyOnFilesystem:justPromotedAnyDescriptor:"
+ "moveTargetURLToDirectory"
+ "newFoundSetDescriptorsFromCachedLookup"
+ "newFoundSetDescriptorsFromCachedLookup:"
+ "older set-descriptor found - dropped setDescriptor:%@"
+ "promoteAnyPreviouslyStagedNowDownloaded"
+ "scheduledJobsResumed:"
+ "schedulerResumed:"
+ "setAlreadyScheduledSelectors:"
+ "setForceDaemonBusy:"
+ "unable to create new set-descriptor"
+ "unsignedLongValue"
+ "v36@0:8@16B24@28"
+ "v40@0:8r*16*24^Q32"
+ "verifyReceipt:withSignature:"
+ "{%@} auto-asset metadata considered invalid | %@"
+ "{CopyDataFromEncodedBase64} Invalid range"
+ "{CopyDataFromEncodedBase64} decode error, decoded data size is 0"
+ "{CopyDataFromEncodedBase64} decode error, decoded data size is not 3"
+ "{CopyDataFromEncodedBase64} range is 0"
+ "{CopyDataFromEncodedBase64} range larger than data length"
+ "{updateLastFetchedDate} failed to update lastFetchedDate in xml | tempLocation:%@ targetLocation:%@"
+ "{writeDictionaryToFile} Failed to write dictionary to file, asset type was not well formed: %@"
+ "{writeDictionaryToFile} failed to move XML | tempLocation:%@ targetLocation:%@"
- "\x11\x1f\x0f\b"
- "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld(set:%ld)|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
- "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld(set:%ld)|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
- "%{public}@ | {reportSetCatalogDecideFound} filtering out asset (additional full of less-preferred format) | filtered:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} filtering out asset (additional patch of less-preferred format) | filtered:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} filtering out asset (empty entry) | metadata:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} filtering out asset (specifier not requested) | response specifier:%{public}@ | filtered:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} full provided | considering:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} mixture of Ramping indications - considering overall set as NOT ramped | nextAsset:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} more preferred full provided | now considering:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} more preferred patch provided | now considering:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} no assets provided (and no latest-installed atomic-instance)"
- "%{public}@ | {reportSetCatalogDecideFound} patch provided | considering:%{public}@"
- "/\x0e\x1f\x11\"c"
- "=="
- "@304@0:8q16@24@32@40@48@?56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240B248B252@256@264@272@280@288@296"
- "DawnB"
- "Pallas JWS parsing did not yield 3 elements"
- "Starting built-in MobileAsset brain built Oct  5 2023 21:17:05"
- "Starting downloaded MobileAsset brain (version: %@) built Oct  5 2023 21:17:05"
- "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [CLIENT_REQUESTS_AWAITING_SYNC] | [scheduled and] routed client-request that had been awaiting first-unlock | jobParam:%{public}@"
- "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [CLIENT_REQUESTS_AWAITING_SYNC] | [scheduled and] routed client-request | jobParam:%{public}@"
- "[%{public}@] {%{public}@e} | NOT removing nextSetAtomicInstance:%{public}@"
- "[%{public}@] {%{public}@} unable to load persisted-set-atomic-instance file | nextRemoveSetInstance:%{public}@"
- "[%{public}@] {%{public}@} | removing nextSetAtomicInstance:%{public}@"
- "[%{public}@] {_removeAllUnlockedForOtherAtomicInstances} older set-descriptor found - dropped | entryID:%{public}@"
- "[%{public}@] {_removeAllUnlockedForOtherAtomicInstances} unable to determine previous status | entryID:%{public}@"
- "[%{public}@] {_removeAllUnlockedForOtherAtomicInstances} unable to load set-descriptor | entryID:%{public}@"
- "[%{public}@] {_removeDownloadedDescriptorsWithNewerDownloaded} encountered blank auto-asset-descriptor - removing | entryID:%{public}@"
- "[%{public}@] {_removeDownloadedDescriptorsWithNewerDownloaded} encountered downloaded descriptor not on the filesystem - removing | entryID:%{public}@"
- "[%{public}@] {_removeDownloadedDescriptorsWithNewerDownloaded} removing older downloaded descriptor | removingDescriptor:%{public}@, keepingDescriptor:%{public}@"
- "[%{public}@] {_removeDownloadedDescriptorsWithNewerDownloaded} unable to determine previous status | entryID:%{public}@"
- "[%{public}@] {_removeDownloadedDescriptorsWithNewerDownloaded} unable to load auto-asset-descriptor | entryID:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} atomic-instance without backing set-descriptor | entryID:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance with no asset-entries on filesystem | entryID:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance without backing set-descriptor | entryID:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} unable to determine previous status | entryID:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} unable to load set-atomic-instance | entryID:%{public}@"
- "_routeClientRequest:fromLocation:"
- "atomicInstanceRemove:setAtomicInstanceUUID:"
- "atomicInstanceRemovedSetJob:"
- "foundAndDownloadedSet:forJobParam:"
- "handleClientPotentialJob:forAutoJob:fromLocation:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "isSetFoundAlreadyOnFilesystem"
- "moveTargetToDirectory"
- "schedulerResumed"
- "verifyReceipt"
- "{reportSetCatalogDecideFound} auto-asset metadata considered invalid | %@"

```
