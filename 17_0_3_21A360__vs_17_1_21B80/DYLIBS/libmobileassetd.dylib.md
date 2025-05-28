## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-936.2.1.0.0
-  __TEXT.__text: 0x16a550
+936.42.1.0.0
+  __TEXT.__text: 0x177bcc
   __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0xbee8
+  __TEXT.__objc_methlist: 0xc148
   __TEXT.__const: 0xb50
-  __TEXT.__cstring: 0x39969
-  __TEXT.__gcc_except_tab: 0x1424
-  __TEXT.__oslogstring: 0x1d3f7
+  __TEXT.__cstring: 0x3ba3d
+  __TEXT.__oslogstring: 0x20f69
+  __TEXT.__gcc_except_tab: 0x1438
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__unwind_info: 0x22d4
   __TEXT.__eh_frame: 0x7c
-  __TEXT.__objc_classname: 0xb37
-  __TEXT.__objc_methname: 0x28c83
-  __TEXT.__objc_methtype: 0x27e1
-  __TEXT.__objc_stubs: 0x183e0
-  __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x20d8
+  __TEXT.__objc_classname: 0xb34
+  __TEXT.__objc_methname: 0x2b3dd
+  __TEXT.__objc_methtype: 0x28a9
+  __TEXT.__objc_stubs: 0x19480
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd870
-  __DATA_CONST.__objc_selrefs: 0x6a90
+  __DATA_CONST.__objc_const: 0xddb0
+  __DATA_CONST.__objc_selrefs: 0x6f40
   __DATA_CONST.__objc_arraydata: 0x810
-  __AUTH_CONST.__cfstring: 0x250e0
+  __AUTH_CONST.__cfstring: 0x26560
   __AUTH_CONST.__objc_const: 0x3000
-  __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__auth_ptr: 0x30
+  __AUTH_CONST.__const: 0xa20
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0xc8

   __AUTH.__objc_data: 0x780
   __DATA.__objc_classrefs: 0x6a0
   __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0xf08
+  __DATA.__objc_ivar: 0xf74
   __DATA.__data: 0xd30
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x1860

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
+  - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor
   - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimg4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4826
-  Symbols:   15549
-  CStrings:  11750
+  Functions: 4872
+  Symbols:   15817
+  CStrings:  12264
 
Symbols:
+ +[MADAutoAssetControlManager autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:]
+ +[MADAutoAssetControlManager autoAssetStagerSetJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:]
+ +[MADAutoAssetControlManager migrateMismatchedPersistedSetTargetVersion:forEntryID:withMismatchedState:]
+ +[MADAutoAssetControlManager migrateMismatchedPersistedStagedSetConfiguration:forEntryID:withMismatchedState:]
+ +[MADAutoAssetControlManager preferenceAsIfBackgroundOrUse:]
+ +[MADAutoAssetControlManager preferenceAsIfRampOrUse:]
+ +[MADAutoAssetControlManager preferenceAutoAssetLogSetCompare]
+ +[MADAutoAssetControlManager preferenceMaxStagerDeterminingSecs]
+ +[MADAutoAssetControlManager preferenceSessionIDBase]
+ +[MADAutoAssetControlManager restoreVersionFromOSVersion:]
+ +[MADAutoAssetControlManager restoreVersionFromOSVersion:].cold.1
+ +[MADAutoAssetControlManager stagerResumed:withSetLookupResults:]
+ +[MADAutoAssetControlManager stagerStartJobDownloadForStaging:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:]
+ +[MADAutoAssetControlManager stagerStartSetJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:]
+ +[MADAutoAssetDescriptor isMorePreferredAssetFormat:comparedTo:]
+ +[MADAutoAssetStager autoAssetStagerJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:]
+ +[MADAutoAssetStager autoAssetStagerJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:].cold.1
+ +[MADAutoAssetStager autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:]
+ +[MADAutoAssetStager autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:].cold.1
+ +[MADAutoAssetStager controlAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:]
+ +[MADAutoAssetStager controlAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:].cold.1
+ +[MADAutoAssetStager migrateMismatchedPersistedSetPromotionVersion:forEntryID:withMismatchedState:]
+ +[MADAutoSetLookupResult supportsSecureCoding]
+ +[MADAutoSetTarget supportsSecureCoding]
+ -[ControlManager getSAFRegistrationBundleID:]
+ -[ControlManager registerAssetsWithSpaceAttributes]
+ -[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]
+ -[MADAutoAssetConnectorObserver pathStatusDispatchQueue]
+ -[MADAutoAssetConnectorObserver pathToServerIsUp]
+ -[MADAutoAssetConnectorObserver setPathToServerIsUp:]
+ -[MADAutoAssetControlManager _eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager _eliminateAtomicTriggeredWhileLoading:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager _eliminateBegin:forAssetSelector:limitingToActivity:fromLocation:]
+ -[MADAutoAssetControlManager _limitSetAtomicEntries:fromSetDescriptor:requestedAutoAssetEntries:]
+ -[MADAutoAssetControlManager _logPersistedSetLookupResult:operation:forPersistedEntryID:withSetLookupResult:message:]
+ -[MADAutoAssetControlManager _logPersistedSetLookupResultRemoved:removedPersistedEntryID:removedSetLookupResult:message:]
+ -[MADAutoAssetControlManager _logPersistedSetLookupResultTableOfContents:]
+ -[MADAutoAssetControlManager _logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:]
+ -[MADAutoAssetControlManager _logPersistedSetTargetRemoved:removedPersistedEntryID:removedSetTarget:message:]
+ -[MADAutoAssetControlManager _logPersistedSetTargetTableOfContents:]
+ -[MADAutoAssetControlManager _messageAssetPolicyDownloadUserInitiated:forClientRequest:]
+ -[MADAutoAssetControlManager _scheduleAndCreateSetConfiguration:fromLocation:errorString:]
+ -[MADAutoAssetControlManager action_CancelActivityAck:error:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:]
+ -[MADAutoAssetControlManager bootedOBuildVersion]
+ -[MADAutoAssetControlManager bootedOSVersion]
+ -[MADAutoAssetControlManager doesSetDescriptor:coverAllForAutoAssetEntries:]
+ -[MADAutoAssetControlManager doesSetDescriptor:coverRequestedAutoAssetEntries:]
+ -[MADAutoAssetControlManager doesSetDescriptor:matchSetConfiguration:]
+ -[MADAutoAssetControlManager findAtomicEntryForAssetType:forAssetSpecifier:representedByLookupResult:]
+ -[MADAutoAssetControlManager firstAssetTypeForSetEntries:]
+ -[MADAutoAssetControlManager handleClientCancelActivityForSelectorRequest:]
+ -[MADAutoAssetControlManager handleStagingClientDetermineAllAvailableForUpdateRequest:]
+ -[MADAutoAssetControlManager initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:withClientAssetPolicy:]
+ -[MADAutoAssetControlManager isAnyAssetEntryOnFilesystemForSetDescriptor:]
+ -[MADAutoAssetControlManager jobControlInformationForSetConfiguration:]
+ -[MADAutoAssetControlManager loadPersistedSetLookupResults]
+ -[MADAutoAssetControlManager loadPersistedSetTargets]
+ -[MADAutoAssetControlManager locateDownloadedNewBySelectorLimitedToStaging:]
+ -[MADAutoAssetControlManager locateNewAllSetConfigurations]
+ -[MADAutoAssetControlManager locateNewAllSetTargets]
+ -[MADAutoAssetControlManager locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:]
+ -[MADAutoAssetControlManager locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:]
+ -[MADAutoAssetControlManager locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPrevoiuslyStagedFound:fromLocation:]
+ -[MADAutoAssetControlManager locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:]
+ -[MADAutoAssetControlManager locateSetLookupResultSatisfying:]
+ -[MADAutoAssetControlManager locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:]
+ -[MADAutoAssetControlManager newSetDescriptorLimitedToLockInformation:forSetConfiguration:]
+ -[MADAutoAssetControlManager newSetEntryIDForClientDomainName:forAssetSetIdentifier:forMinTargetOS:forMaxTargetOS:]
+ -[MADAutoAssetControlManager newSetTargetFromClientProvidedSetTarget:forClientDomainName:forSetIdentifier:]
+ -[MADAutoAssetControlManager persistedSetLookupResults]
+ -[MADAutoAssetControlManager persistedSetTargets]
+ -[MADAutoAssetControlManager preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:]
+ -[MADAutoAssetControlManager preferenceAsIfBackgroundSpecified]
+ -[MADAutoAssetControlManager preferenceAsIfBackground]
+ -[MADAutoAssetControlManager preferenceAsIfRampSpecified]
+ -[MADAutoAssetControlManager preferenceAsIfRamp]
+ -[MADAutoAssetControlManager preferenceAutoAssetLogSetCompare]
+ -[MADAutoAssetControlManager preferenceMaxStagerDeterminingSecs]
+ -[MADAutoAssetControlManager preferenceSessionIDBase]
+ -[MADAutoAssetControlManager removePreviouslyStagedSetDescriptors]
+ -[MADAutoAssetControlManager removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:]
+ -[MADAutoAssetControlManager setBootedOBuildVersion:]
+ -[MADAutoAssetControlManager setBootedOSVersion:]
+ -[MADAutoAssetControlManager setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:selectedConfig:]
+ -[MADAutoAssetControlManager setConfigurationSelectUsingInfoInstance:dueToMessageName:selectedConfig:]
+ -[MADAutoAssetControlManager setPersistedSetLookupResults:]
+ -[MADAutoAssetControlManager setPersistedSetTargets:]
+ -[MADAutoAssetControlManager setPreferenceAsIfBackground:]
+ -[MADAutoAssetControlManager setPreferenceAsIfBackgroundSpecified:]
+ -[MADAutoAssetControlManager setPreferenceAsIfRamp:]
+ -[MADAutoAssetControlManager setPreferenceAsIfRampSpecified:]
+ -[MADAutoAssetControlManager setPreferenceAutoAssetLogSetCompare:]
+ -[MADAutoAssetControlManager setPreferenceMaxStagerDeterminingSecs:]
+ -[MADAutoAssetControlManager setPreferenceSessionIDBase:]
+ -[MADAutoAssetControlManager setStagerFormedSetConfiguration:]
+ -[MADAutoAssetControlManager setTargetEntries:matchSetConfiguration:]
+ -[MADAutoAssetControlManager setTargetNewEntryIDForClientDomainName:forAssetSetIdentifier:forClientProvidedSetTarget:]
+ -[MADAutoAssetControlManager stagerFormedSetConfiguration]
+ -[MADAutoAssetControlManagerParam assetTargetRestoreVersion]
+ -[MADAutoAssetControlManagerParam assetTargetTrainName]
+ -[MADAutoAssetControlManagerParam baseForStagingDescriptors]
+ -[MADAutoAssetControlManagerParam initForStagerJobLookupResults:withBaseForStagingDescriptors:withDetermineError:]
+ -[MADAutoAssetControlManagerParam initForStagerJobStart:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:]
+ -[MADAutoAssetControlManagerParam initForStagerSetJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:].cold.1
+ -[MADAutoAssetControlManagerParam initWithPromoted:withSetLookupResults:]
+ -[MADAutoAssetControlManagerParam setAssetTargetRestoreVersion:]
+ -[MADAutoAssetControlManagerParam setAssetTargetTrainName:]
+ -[MADAutoAssetControlManagerParam setBaseForStagingDescriptors:]
+ -[MADAutoAssetControlManagerParam setConfiguration]
+ -[MADAutoAssetControlManagerParam setPolicy]
+ -[MADAutoAssetControlManagerParam setSetPolicy:]
+ -[MADAutoAssetControlManagerParam setStagedSetLookupResults:]
+ -[MADAutoAssetControlManagerParam stagedSetLookupResults]
+ -[MADAutoAssetDescriptor isRamped]
+ -[MADAutoAssetEliminate awaitingCancelActivityAck]
+ -[MADAutoAssetEliminate limitedToCancelActivity]
+ -[MADAutoAssetEliminate setAwaitingCancelActivityAck:]
+ -[MADAutoAssetEliminate setLimitedToCancelActivity:]
+ -[MADAutoAssetJob _newSelectorForCachedAssetCatalog:]
+ -[MADAutoAssetJob _newSelectorForCachedAssetCatalog:].cold.1
+ -[MADAutoAssetJob _setPolicyFromClientRequest:]
+ -[MADAutoAssetJob action_SetDoneDetermine:error:]
+ -[MADAutoAssetJob cachedAutoAssetCatalog]
+ -[MADAutoAssetJob determineWhetherNetworkConnectivityError:]
+ -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.1
+ -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.2
+ -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.3
+ -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:]
+ -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:].cold.1
+ -[MADAutoAssetJob initForInstance:withAutoAssetUUID:downloadingUserInitiated:]
+ -[MADAutoAssetJob initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:]
+ -[MADAutoAssetJob initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:]
+ -[MADAutoAssetJob installedOnFilesystemWithVersion:fromLocation:]
+ -[MADAutoAssetJob preferenceAsIfRampOrUse:]
+ -[MADAutoAssetJob replyToJobsWhenCatalogDownloaded:discoveredNewer:].cold.1
+ -[MADAutoAssetJob setCachedAutoAssetCatalog:]
+ -[MADAutoAssetJob setStagerAssetTargetRestoreVersion:]
+ -[MADAutoAssetJob setStagerAssetTargetTrainName:]
+ -[MADAutoAssetJob setStagerJobAutoAssetCatalog:]
+ -[MADAutoAssetJob setStagerSetPolicy:]
+ -[MADAutoAssetJob stagerAssetTargetRestoreVersion]
+ -[MADAutoAssetJob stagerAssetTargetTrainName]
+ -[MADAutoAssetJob stagerJobAutoAssetCatalog]
+ -[MADAutoAssetJob stagerSetPolicy]
+ -[MADAutoAssetJob startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:]
+ -[MADAutoAssetJobParam assetTargetRestoreVersion]
+ -[MADAutoAssetJobParam assetTargetTrainName]
+ -[MADAutoAssetJobParam initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:]
+ -[MADAutoAssetJobParam initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withAutoAssetDescriptor:withControlInformation:]
+ -[MADAutoAssetJobParam setAssetTargetRestoreVersion:]
+ -[MADAutoAssetJobParam setAssetTargetTrainName:]
+ -[MADAutoAssetStager _extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:]
+ -[MADAutoAssetStager _extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:withDownloadDecryptionKey:]
+ -[MADAutoAssetStager _extendLookupByAssetTypeWithDownloadedDescriptors:]
+ -[MADAutoAssetStager _extendLookupByAssetTypeWithSetConfigurations:]
+ -[MADAutoAssetStager _formCandidateSetLookupArray]
+ -[MADAutoAssetStager _isAssetSetEntry:blockedBySetTarget:]
+ -[MADAutoAssetStager _isDescriptorAssetTypeManagedAsSet:]
+ -[MADAutoAssetStager _isSetTargetWithinRange:asCandidate:]
+ -[MADAutoAssetStager _isSetTargetWithinRange:asCandidate:].cold.1
+ -[MADAutoAssetStager _logPersistedSetLookupResult:operation:forPersistedEntryID:withSetLookupResult:message:]
+ -[MADAutoAssetStager _logPersistedSetLookupResultRemoved:removedPersistedEntryID:removedSetLookupResult:message:]
+ -[MADAutoAssetStager _logPersistedSetLookupResultTableOfContents:]
+ -[MADAutoAssetStager _persistRebuildTrackingNewHandedOffDescriptors:]
+ -[MADAutoAssetStager _setConfigurationForAssetType:forAssetSpecifier:]
+ -[MADAutoAssetStager _setConfigurationHasEntriesWhenTargeting:]
+ -[MADAutoAssetStager _setTargetForAssetType:]
+ -[MADAutoAssetStager _setTargetForSetConfiguration:]
+ -[MADAutoAssetStager _setupAwaitingStagingAndBeginFirstDownload].cold.2
+ -[MADAutoAssetStager _stagingClientMessageStaging]
+ -[MADAutoAssetStager _trimConsideringToLatestDownloaded:]
+ -[MADAutoAssetStager action_AddToAvailableDecideAnyAvailable:error:]
+ -[MADAutoAssetStager action_ClientContinueRestartingMaxDetermining:error:]
+ -[MADAutoAssetStager action_FormCandidatesDecideDetermine:error:].cold.1
+ -[MADAutoAssetStager action_NextAwaitingBeginDownload:error:].cold.1
+ -[MADAutoAssetStager activeSetJobConfiguration]
+ -[MADAutoAssetStager assetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:preferringBestFormat:]
+ -[MADAutoAssetStager assetTargetRestoreVersion]
+ -[MADAutoAssetStager assetTargetTrainName]
+ -[MADAutoAssetStager baseForPatchingToSelector:]
+ -[MADAutoAssetStager baseForStagingDescriptors]
+ -[MADAutoAssetStager candidateSetConfigurations]
+ -[MADAutoAssetStager loadPersistedSetLookupResults]
+ -[MADAutoAssetStager lookupCacheUpdateWithDetermineResult:fromLocation:]
+ -[MADAutoAssetStager lookupCacheUpdateWithDetermineResult:fromLocation:].cold.1
+ -[MADAutoAssetStager newAssetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:]
+ -[MADAutoAssetStager newAssetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:].cold.1
+ -[MADAutoAssetStager newSetLookupResult:forSetCatalog:]
+ -[MADAutoAssetStager newSetLookupResultsForTargetOS]
+ -[MADAutoAssetStager persistedSetLookupResults]
+ -[MADAutoAssetStager scheduledJobs]
+ -[MADAutoAssetStager setActiveSetJobConfiguration:]
+ -[MADAutoAssetStager setAssetTargetRestoreVersion:]
+ -[MADAutoAssetStager setAssetTargetTrainName:]
+ -[MADAutoAssetStager setBaseForStagingDescriptors:]
+ -[MADAutoAssetStager setCandidateSetConfigurations:]
+ -[MADAutoAssetStager setConfigurations]
+ -[MADAutoAssetStager setLookupResultLoadedFromPersisted:persistedEntryID:]
+ -[MADAutoAssetStager setLookupResults]
+ -[MADAutoAssetStager setPersistedSetLookupResults:]
+ -[MADAutoAssetStager setScheduledJobs:]
+ -[MADAutoAssetStager setSetConfigurations:]
+ -[MADAutoAssetStager setSetLookupResults:]
+ -[MADAutoAssetStager setSetTargets:]
+ -[MADAutoAssetStager setTargets]
+ -[MADAutoAssetStager startMaxTimeSpentDeterminingTimer]
+ -[MADAutoAssetStager startMaxTimeSpentDeterminingTimer].cold.1
+ -[MADAutoAssetStagerParam autoAssetCatalog]
+ -[MADAutoAssetStagerParam baseForStagingDescriptors]
+ -[MADAutoAssetStagerParam downloadedDescriptor]
+ -[MADAutoAssetStagerParam initWithAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:]
+ -[MADAutoAssetStagerParam initWithAutoAssetCatalog:withBaseForStagingDescriptors:withOperationError:]
+ -[MADAutoAssetStagerParam initWithJobInformation:withDownloadedDescriptor:withOperationError:]
+ -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:]
+ -[MADAutoAssetStagerParam scheduledJobs]
+ -[MADAutoAssetStagerParam setBaseForStagingDescriptors:]
+ -[MADAutoAssetStagerParam setConfigurations]
+ -[MADAutoAssetStagerParam setTargets]
+ -[MADAutoSetConfiguration assetSetEntryForAssetType:forAssetSpecifier:]
+ -[MADAutoSetConfiguration firstEntryAssetType]
+ -[MADAutoSetConfiguration refererncesAssetType:]
+ -[MADAutoSetDescriptor downloadedEntryForAssetType:forAssetSpecifier:]
+ -[MADAutoSetDescriptor firstAssetType]
+ -[MADAutoSetDescriptor requestedAutoAssetEntries]
+ -[MADAutoSetDescriptor setRequestedAutoAssetEntries:]
+ -[MADAutoSetLookupResult .cxx_destruct]
+ -[MADAutoSetLookupResult assetType]
+ -[MADAutoSetLookupResult catalogCachedAssetSetID]
+ -[MADAutoSetLookupResult catalogDownloadedFromLive]
+ -[MADAutoSetLookupResult catalogLastTimeChecked]
+ -[MADAutoSetLookupResult catalogPostedDate]
+ -[MADAutoSetLookupResult description]
+ -[MADAutoSetLookupResult discoveredAtomicEntries]
+ -[MADAutoSetLookupResult encodeWithCoder:]
+ -[MADAutoSetLookupResult initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:]
+ -[MADAutoSetLookupResult initWithCoder:]
+ -[MADAutoSetLookupResult newSummaryWithoutEntryID]
+ -[MADAutoSetLookupResult setCatalogCachedAssetSetID:]
+ -[MADAutoSetLookupResult setCatalogDownloadedFromLive:]
+ -[MADAutoSetLookupResult setCatalogLastTimeChecked:]
+ -[MADAutoSetLookupResult setCatalogPostedDate:]
+ -[MADAutoSetLookupResult setDiscoveredAtomicEntries:]
+ -[MADAutoSetLookupResult summary]
+ -[MADAutoSetTarget .cxx_destruct]
+ -[MADAutoSetTarget assetSetEntryForAssetType:forAssetSpecifier:]
+ -[MADAutoSetTarget assetSetIdentifier]
+ -[MADAutoSetTarget autoAssetEntries]
+ -[MADAutoSetTarget clientDomainName]
+ -[MADAutoSetTarget copy]
+ -[MADAutoSetTarget description]
+ -[MADAutoSetTarget encodeWithCoder:]
+ -[MADAutoSetTarget includesEntryForAssetType:forAssetSpecifier:]
+ -[MADAutoSetTarget initForClientDomainName:forAssetSetIdentifier:fromMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:]
+ -[MADAutoSetTarget initWithCoder:]
+ -[MADAutoSetTarget isEqual:]
+ -[MADAutoSetTarget maxTargetOSVersion]
+ -[MADAutoSetTarget minTargetOSVersion]
+ -[MADAutoSetTarget newSummaryWithoutEntryID]
+ -[MADAutoSetTarget setAssetSetIdentifier:]
+ -[MADAutoSetTarget setAutoAssetEntries:]
+ -[MADAutoSetTarget setClientDomainName:]
+ -[MADAutoSetTarget setMaxTargetOSVersion:]
+ -[MADAutoSetTarget setMinTargetOSVersion:]
+ -[MADAutoSetTarget summary]
+ -[MANAutoAssetSetEntry initForAssetType:withAssetSpecifier:withAssetVersion:assetLockedInhibitsRemoval:]
+ -[MANAutoAssetSetEntry initForAssetType:withAssetSpecifier:withAssetVersion:usingDecryptionKey:assetLockedInhibitsRemoval:]
+ GCC_except_table120
+ GCC_except_table148
+ GCC_except_table156
+ GCC_except_table214
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table40
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table421
+ _NSURLIsDirectoryKey
+ _NSURLNameKey
+ _OBJC_CLASS_$_MADAutoSetLookupResult
+ _OBJC_CLASS_$_MADAutoSetTarget
+ _OBJC_IVAR_$_MADAutoAssetConnectorObserver._pathStatusDispatchQueue
+ _OBJC_IVAR_$_MADAutoAssetConnectorObserver._pathToServerIsUp
+ _OBJC_IVAR_$_MADAutoAssetControlManager._bootedOBuildVersion
+ _OBJC_IVAR_$_MADAutoAssetControlManager._bootedOSVersion
+ _OBJC_IVAR_$_MADAutoAssetControlManager._persistedSetLookupResults
+ _OBJC_IVAR_$_MADAutoAssetControlManager._persistedSetTargets
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAsIfBackground
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAsIfBackgroundSpecified
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAsIfRamp
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAsIfRampSpecified
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAutoAssetLogSetCompare
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceMaxStagerDeterminingSecs
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceSessionIDBase
+ _OBJC_IVAR_$_MADAutoAssetControlManager._stagerFormedSetConfiguration
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._assetTargetRestoreVersion
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._assetTargetTrainName
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._baseForStagingDescriptors
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._setConfiguration
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._setPolicy
+ _OBJC_IVAR_$_MADAutoAssetControlManagerParam._stagedSetLookupResults
+ _OBJC_IVAR_$_MADAutoAssetEliminate._awaitingCancelActivityAck
+ _OBJC_IVAR_$_MADAutoAssetEliminate._limitedToCancelActivity
+ _OBJC_IVAR_$_MADAutoAssetJob._cachedAutoAssetCatalog
+ _OBJC_IVAR_$_MADAutoAssetJob._stagerAssetTargetRestoreVersion
+ _OBJC_IVAR_$_MADAutoAssetJob._stagerAssetTargetTrainName
+ _OBJC_IVAR_$_MADAutoAssetJob._stagerJobAutoAssetCatalog
+ _OBJC_IVAR_$_MADAutoAssetJob._stagerSetPolicy
+ _OBJC_IVAR_$_MADAutoAssetJobParam._assetTargetRestoreVersion
+ _OBJC_IVAR_$_MADAutoAssetJobParam._assetTargetTrainName
+ _OBJC_IVAR_$_MADAutoAssetStager._activeSetJobConfiguration
+ _OBJC_IVAR_$_MADAutoAssetStager._assetTargetRestoreVersion
+ _OBJC_IVAR_$_MADAutoAssetStager._assetTargetTrainName
+ _OBJC_IVAR_$_MADAutoAssetStager._baseForStagingDescriptors
+ _OBJC_IVAR_$_MADAutoAssetStager._candidateSetConfigurations
+ _OBJC_IVAR_$_MADAutoAssetStager._persistedSetLookupResults
+ _OBJC_IVAR_$_MADAutoAssetStager._scheduledJobs
+ _OBJC_IVAR_$_MADAutoAssetStager._setConfigurations
+ _OBJC_IVAR_$_MADAutoAssetStager._setLookupResults
+ _OBJC_IVAR_$_MADAutoAssetStager._setTargets
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._autoAssetCatalog
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._baseForStagingDescriptors
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._downloadedDescriptor
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._scheduledJobs
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._setConfigurations
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._setTargets
+ _OBJC_IVAR_$_MADAutoSetDescriptor._requestedAutoAssetEntries
+ _OBJC_IVAR_$_MADAutoSetLookupResult._assetType
+ _OBJC_IVAR_$_MADAutoSetLookupResult._catalogCachedAssetSetID
+ _OBJC_IVAR_$_MADAutoSetLookupResult._catalogDownloadedFromLive
+ _OBJC_IVAR_$_MADAutoSetLookupResult._catalogLastTimeChecked
+ _OBJC_IVAR_$_MADAutoSetLookupResult._catalogPostedDate
+ _OBJC_IVAR_$_MADAutoSetLookupResult._discoveredAtomicEntries
+ _OBJC_IVAR_$_MADAutoSetTarget._assetSetIdentifier
+ _OBJC_IVAR_$_MADAutoSetTarget._autoAssetEntries
+ _OBJC_IVAR_$_MADAutoSetTarget._clientDomainName
+ _OBJC_IVAR_$_MADAutoSetTarget._maxTargetOSVersion
+ _OBJC_IVAR_$_MADAutoSetTarget._minTargetOSVersion
+ _OBJC_METACLASS_$_MADAutoSetLookupResult
+ _OBJC_METACLASS_$_MADAutoSetTarget
+ _OUTLINED_FUNCTION_9
+ __MAPreferencesSetStringValue
+ __OBJC_$_CLASS_METHODS_MADAutoSetLookupResult
+ __OBJC_$_CLASS_METHODS_MADAutoSetTarget
+ __OBJC_$_CLASS_PROP_LIST_MADAutoSetLookupResult
+ __OBJC_$_CLASS_PROP_LIST_MADAutoSetTarget
+ __OBJC_$_INSTANCE_METHODS_MADAutoSetLookupResult
+ __OBJC_$_INSTANCE_METHODS_MADAutoSetTarget
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoSetLookupResult
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoSetTarget
+ __OBJC_$_PROP_LIST_MADAutoSetLookupResult
+ __OBJC_$_PROP_LIST_MADAutoSetTarget
+ __OBJC_CLASS_PROTOCOLS_$_MADAutoSetLookupResult
+ __OBJC_CLASS_PROTOCOLS_$_MADAutoSetTarget
+ __OBJC_CLASS_RO_$_MADAutoSetLookupResult
+ __OBJC_CLASS_RO_$_MADAutoSetTarget
+ __OBJC_METACLASS_RO_$_MADAutoSetLookupResult
+ __OBJC_METACLASS_RO_$_MADAutoSetTarget
+ ___26-[MADAutoAssetStager init]_block_invoke_2
+ ___27-[MABrainUpdater schedule:]_block_invoke_3.345
+ ___27-[MABrainUpdater schedule:]_block_invoke_4
+ ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.690
+ ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.734
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.784
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.784.cold.1
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.791
+ ___55-[MADAutoAssetStager startMaxTimeSpentDeterminingTimer]_block_invoke
+ ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.796
+ ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.671
+ ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.691
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.773
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.791
+ ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1665
+ ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke_7
+ ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke_8
+ ___80-[MADAutoAssetConnectorObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ____MAPreferencesCopyValue_block_invoke
+ ____MAPreferencesCopyValue_block_invoke_2
+ ____MAPreferencesSetStringValue_block_invoke
+ ____MAPreferencesSync_block_invoke
+ ____preferencesDomainProtectionDispatchQueue_block_invoke
+ ___block_literal_global.1005
+ ___block_literal_global.1008
+ ___block_literal_global.1025
+ ___block_literal_global.1194
+ ___block_literal_global.1267
+ ___block_literal_global.1378
+ ___block_literal_global.1596
+ ___block_literal_global.1615
+ ___block_literal_global.1623
+ ___block_literal_global.1631
+ ___block_literal_global.1639
+ ___block_literal_global.1647
+ ___block_literal_global.1655
+ ___block_literal_global.1663
+ ___block_literal_global.1902
+ ___block_literal_global.1951
+ ___block_literal_global.2457
+ ___block_literal_global.3030
+ ___block_literal_global.347
+ ___block_literal_global.494
+ ___block_literal_global.515
+ ___block_literal_global.640
+ ___block_literal_global.652
+ ___block_literal_global.656
+ ___block_literal_global.659
+ ___block_literal_global.662
+ ___block_literal_global.670
+ ___block_literal_global.682
+ ___block_literal_global.683
+ ___block_literal_global.687
+ ___block_literal_global.688
+ ___block_literal_global.689
+ ___block_literal_global.693
+ ___block_literal_global.694
+ ___block_literal_global.699
+ ___block_literal_global.704
+ ___block_literal_global.726
+ ___block_literal_global.728
+ ___block_literal_global.736
+ ___block_literal_global.772
+ ___block_literal_global.793
+ ___block_literal_global.820
+ ___block_literal_global.825
+ ___block_literal_global.846
+ ___block_literal_global.856
+ ___block_literal_global.876
+ ___block_literal_global.951
+ ___block_literal_global.956
+ __preferencesDomainProtectionDispatchQueue
+ __preferencesDomainProtectionDispatchQueue.preferencesDomainQueue
+ __preferencesDomainProtectionDispatchQueue.preferencesDomainQueueOnce
+ __unnamed_array_storage.1856
+ __unnamed_array_storage.1942
+ __unnamed_array_storage.2203
+ __unnamed_array_storage.2204
+ __unnamed_array_storage.2209
+ __unnamed_array_storage.2210
+ __unnamed_array_storage.2295
+ __unnamed_array_storage.2296
+ __unnamed_array_storage.725
+ __unnamed_array_storage.726
+ __unnamed_array_storage.742
+ __unnamed_array_storage.945
+ __unnamed_array_storage.953
+ __unnamed_array_storage.968
+ _isDownloadResultSuggestingCheckClockAndCerts
+ _isDownloadResultSuggestingCheckNetwork
+ _isDownloadResultSuggestingCheckTimeoutConditions
+ _kCFBundleIdentifierKey
+ _kMobileAssetPreferencesAutoAssetAsIfBackground
+ _kMobileAssetPreferencesAutoAssetAsIfRamp
+ _kMobileAssetPreferencesAutoAssetLogSetCompare
+ _kMobileAssetPreferencesAutoAssetMaxStagerDeterminingSecs
+ _kMobileAssetPreferencesAutoAssetSessionIDBase
+ _objc_msgSend$_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$_eliminateAtomicTriggeredWhileLoading:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$_eliminateBegin:forAssetSelector:limitingToActivity:fromLocation:
+ _objc_msgSend$_extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:
+ _objc_msgSend$_extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:withDownloadDecryptionKey:
+ _objc_msgSend$_extendLookupByAssetTypeWithDownloadedDescriptors:
+ _objc_msgSend$_extendLookupByAssetTypeWithSetConfigurations:
+ _objc_msgSend$_formCandidateSetLookupArray
+ _objc_msgSend$_isAssetSetEntry:blockedBySetTarget:
+ _objc_msgSend$_isSetTargetWithinRange:asCandidate:
+ _objc_msgSend$_limitSetAtomicEntries:fromSetDescriptor:requestedAutoAssetEntries:
+ _objc_msgSend$_logPersistedSetLookupResult:operation:forPersistedEntryID:withSetLookupResult:message:
+ _objc_msgSend$_logPersistedSetLookupResultRemoved:removedPersistedEntryID:removedSetLookupResult:message:
+ _objc_msgSend$_logPersistedSetLookupResultTableOfContents:
+ _objc_msgSend$_logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:
+ _objc_msgSend$_logPersistedSetTargetRemoved:removedPersistedEntryID:removedSetTarget:message:
+ _objc_msgSend$_logPersistedSetTargetTableOfContents:
+ _objc_msgSend$_longSummary
+ _objc_msgSend$_messageAssetPolicyDownloadUserInitiated:forClientRequest:
+ _objc_msgSend$_newSelectorForCachedAssetCatalog:
+ _objc_msgSend$_persistRebuildTrackingNewHandedOffDescriptors:
+ _objc_msgSend$_scheduleAndCreateSetConfiguration:fromLocation:errorString:
+ _objc_msgSend$_setConfigurationForAssetType:forAssetSpecifier:
+ _objc_msgSend$_setPolicyFromClientRequest:
+ _objc_msgSend$_setTargetForAssetType:
+ _objc_msgSend$_setTargetForSetConfiguration:
+ _objc_msgSend$_stagingClientMessageStaging
+ _objc_msgSend$_trimConsideringToLatestDownloaded:
+ _objc_msgSend$action_AddToAvailableDecideAnyAvailable:error:
+ _objc_msgSend$action_CancelActivityAck:error:
+ _objc_msgSend$action_ClientContinueRestartingMaxDetermining:error:
+ _objc_msgSend$action_SetDoneDetermine:error:
+ _objc_msgSend$activeSetJobConfiguration
+ _objc_msgSend$allAvailableForStagingAttributes
+ _objc_msgSend$assetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:preferringBestFormat:
+ _objc_msgSend$assetSetEntryForAssetType:forAssetSpecifier:
+ _objc_msgSend$assetTargetRestoreVersion
+ _objc_msgSend$assetTargetTrainName
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:
+ _objc_msgSend$autoAssetStagerJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:
+ _objc_msgSend$autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:
+ _objc_msgSend$autoAssetStagerSetJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:
+ _objc_msgSend$awaitingCancelActivityAck
+ _objc_msgSend$baseForPatchingToSelector:
+ _objc_msgSend$baseForStagingDescriptors
+ _objc_msgSend$bootedOBuildVersion
+ _objc_msgSend$bootedOSVersion
+ _objc_msgSend$cachedAutoAssetCatalog
+ _objc_msgSend$candidateSetConfigurations
+ _objc_msgSend$controlAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:
+ _objc_msgSend$determineWhetherNetworkConnectivityError:
+ _objc_msgSend$doesSetDescriptor:alignWithSetConfiguration:
+ _objc_msgSend$doesSetDescriptor:coverAllForAutoAssetEntries:
+ _objc_msgSend$doesSetDescriptor:coverRequestedAutoAssetEntries:
+ _objc_msgSend$downloadedDescriptor
+ _objc_msgSend$downloadedEntryForAssetType:forAssetSpecifier:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$firstAssetType
+ _objc_msgSend$firstAssetTypeForSetEntries:
+ _objc_msgSend$firstEntryAssetType
+ _objc_msgSend$getSAFRegistrationBundleID:
+ _objc_msgSend$handleClientCancelActivityForSelectorRequest:
+ _objc_msgSend$handleStagingClientDetermineAllAvailableForUpdateRequest:
+ _objc_msgSend$includesEntryForAssetType:forAssetSpecifier:
+ _objc_msgSend$initForAssetType:withAssetSpecifier:withAssetVersion:usingDecryptionKey:assetLockedInhibitsRemoval:
+ _objc_msgSend$initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:
+ _objc_msgSend$initForClientDomainName:forAssetSetIdentifier:fromMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:
+ _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:
+ _objc_msgSend$initForInstance:withAutoAssetUUID:downloadingUserInitiated:
+ _objc_msgSend$initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:
+ _objc_msgSend$initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:
+ _objc_msgSend$initForStagerJobLookupResults:withBaseForStagingDescriptors:withDetermineError:
+ _objc_msgSend$initForStagerJobStart:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:
+ _objc_msgSend$initForStagerSetJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:
+ _objc_msgSend$initWithAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:
+ _objc_msgSend$initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:
+ _objc_msgSend$initWithAutoAssetCatalog:withBaseForStagingDescriptors:withOperationError:
+ _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithJobInformation:withDownloadedDescriptor:withOperationError:
+ _objc_msgSend$initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withAutoAssetDescriptor:withControlInformation:
+ _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:
+ _objc_msgSend$initWithPromoted:withSetLookupResults:
+ _objc_msgSend$initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:withClientAssetPolicy:
+ _objc_msgSend$installedOnFilesystemWithVersion:fromLocation:
+ _objc_msgSend$isAnyAssetEntryOnFilesystemForSetDescriptor:
+ _objc_msgSend$isMorePreferredAssetFormat:comparedTo:
+ _objc_msgSend$isRamped
+ _objc_msgSend$jobControlInformationForSetConfiguration:
+ _objc_msgSend$limitedToCancelActivity
+ _objc_msgSend$loadPersistedSetLookupResults
+ _objc_msgSend$loadPersistedSetTargets
+ _objc_msgSend$locateDownloadedNewBySelectorLimitedToStaging:
+ _objc_msgSend$locateNewAllSetConfigurations
+ _objc_msgSend$locateNewAllSetTargets
+ _objc_msgSend$locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:
+ _objc_msgSend$locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:
+ _objc_msgSend$locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPrevoiuslyStagedFound:fromLocation:
+ _objc_msgSend$locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:
+ _objc_msgSend$locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:
+ _objc_msgSend$lookupCacheUpdateWithDetermineResult:fromLocation:
+ _objc_msgSend$migrateMismatchedPersistedSetPromotionVersion:forEntryID:withMismatchedState:
+ _objc_msgSend$migrateMismatchedPersistedSetTargetVersion:forEntryID:withMismatchedState:
+ _objc_msgSend$migrateMismatchedPersistedStagedSetConfiguration:forEntryID:withMismatchedState:
+ _objc_msgSend$newAssetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:
+ _objc_msgSend$newSetEntryIDForClientDomainName:forAssetSetIdentifier:forMinTargetOS:forMaxTargetOS:
+ _objc_msgSend$newSetLookupResult:forSetCatalog:
+ _objc_msgSend$newSetLookupResultsForTargetOS
+ _objc_msgSend$newSetTargetFromClientProvidedSetTarget:forClientDomainName:forSetIdentifier:
+ _objc_msgSend$pathStatusDispatchQueue
+ _objc_msgSend$pathToServerIsUp
+ _objc_msgSend$persistedSetLookupResults
+ _objc_msgSend$persistedSetTargets
+ _objc_msgSend$preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:
+ _objc_msgSend$preferenceAsIfBackground
+ _objc_msgSend$preferenceAsIfBackgroundOrUse:
+ _objc_msgSend$preferenceAsIfBackgroundSpecified
+ _objc_msgSend$preferenceAsIfRamp
+ _objc_msgSend$preferenceAsIfRampOrUse:
+ _objc_msgSend$preferenceAsIfRampSpecified
+ _objc_msgSend$preferenceAutoAssetLogSetCompare
+ _objc_msgSend$preferenceMaxStagerDeterminingSecs
+ _objc_msgSend$preferenceSessionIDBase
+ _objc_msgSend$refererncesAssetType:
+ _objc_msgSend$removePreviouslyStagedSetDescriptors
+ _objc_msgSend$removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:
+ _objc_msgSend$requestedAutoAssetEntries
+ _objc_msgSend$restoreVersionFromOSVersion:
+ _objc_msgSend$scheduledJobs
+ _objc_msgSend$setActiveSetJobConfiguration:
+ _objc_msgSend$setAssetTargetRestoreVersion:
+ _objc_msgSend$setAssetTargetTrainName:
+ _objc_msgSend$setAwaitingCancelActivityAck:
+ _objc_msgSend$setCandidateSetConfigurations:
+ _objc_msgSend$setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:selectedConfig:
+ _objc_msgSend$setConfigurationSelectUsingInfoInstance:dueToMessageName:selectedConfig:
+ _objc_msgSend$setConfigurations
+ _objc_msgSend$setLimitedToCancelActivity:
+ _objc_msgSend$setLookupResultLoadedFromPersisted:persistedEntryID:
+ _objc_msgSend$setLookupResults
+ _objc_msgSend$setPathToServerIsUp:
+ _objc_msgSend$setPersistedSetLookupResults:
+ _objc_msgSend$setPersistedSetTargets:
+ _objc_msgSend$setRequestedAutoAssetEntries:
+ _objc_msgSend$setScheduledJobs:
+ _objc_msgSend$setSetConfigurations:
+ _objc_msgSend$setSetLookupResults:
+ _objc_msgSend$setSetTargets:
+ _objc_msgSend$setStagerAssetTargetRestoreVersion:
+ _objc_msgSend$setStagerAssetTargetTrainName:
+ _objc_msgSend$setStagerFormedSetConfiguration:
+ _objc_msgSend$setStagerJobAutoAssetCatalog:
+ _objc_msgSend$setTargetEntries:matchSetConfiguration:
+ _objc_msgSend$setTargetNewEntryIDForClientDomainName:forAssetSetIdentifier:forClientProvidedSetTarget:
+ _objc_msgSend$setTargets
+ _objc_msgSend$stagedSetLookupResults
+ _objc_msgSend$stagerAssetTargetRestoreVersion
+ _objc_msgSend$stagerAssetTargetTrainName
+ _objc_msgSend$stagerJobAutoAssetCatalog
+ _objc_msgSend$stagerResumed:withSetLookupResults:
+ _objc_msgSend$stagerStartJobDownloadForStaging:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:
+ _objc_msgSend$stagerStartSetJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:
+ _objc_msgSend$startMaxTimeSpentDeterminingTimer
+ _objc_msgSend$startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:
+ _objc_msgSend$updateSpaceAttributionForBundleID:assetPath:doRegistration:
- +[MADAutoAssetControlManager autoAssetStagerJobDetermineDone:withDetremineError:]
- +[MADAutoAssetControlManager autoAssetStagerJobDownloadDone:withDownloadError:]
- +[MADAutoAssetControlManager stagerResumed:]
- +[MADAutoAssetControlManager stagerStartJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:]
- +[MADAutoAssetControlManager stagerStartJobDownloadForStaging:withAssetTargetOSVersion:withAssetTargetBuildVersion:]
- +[MADAutoAssetStager autoAssetStagerJobDetermineDone:withDetermineError:]
- +[MADAutoAssetStager autoAssetStagerJobDetermineDone:withDetermineError:].cold.1
- +[MADAutoAssetStager autoAssetStagerJobDownloadDone:withDownloadError:]
- +[MADAutoAssetStager autoAssetStagerJobDownloadDone:withDownloadError:].cold.1
- +[MADAutoAssetStager controlAlreadyDownloadedDescriptors:]
- +[MADAutoAssetStager controlAlreadyDownloadedDescriptors:].cold.1
- +[MADAutoSetStager _getAutoAssetStagerStateTable]
- +[MADAutoSetStager autoAssetSetStagerJobDetermineDone:withDetermineError:]
- +[MADAutoSetStager autoAssetSetStagerJobDetermineDone:withDetermineError:].cold.1
- +[MADAutoSetStager autoAssetSetStagerJobDownloadDone:withDownloadError:]
- +[MADAutoSetStager autoAssetSetStagerJobDownloadDone:withDownloadError:].cold.1
- +[MADAutoSetStager autoAssetSetStagerJobDownloadProgress:withProgressError:]
- +[MADAutoSetStager autoAssetSetStagerJobDownloadProgress:withProgressError:].cold.1
- +[MADAutoSetStager autoAssetSetStagerJobFailedToStart:]
- +[MADAutoSetStager autoAssetSetStagerJobFailedToStart:].cold.1
- +[MADAutoSetStager autoAssetSetStager]
- +[MADAutoSetStager clientDetermineAllAvailable:]
- +[MADAutoSetStager clientDetermineAllAvailable:].cold.1
- +[MADAutoSetStager clientDownloadAll:]
- +[MADAutoSetStager clientPurgeAll:]
- +[MADAutoSetStager clientPurgeAll:].cold.1
- +[MADAutoSetStager controlAlreadyDownloadedDescriptors:]
- +[MADAutoSetStager controlAlreadyDownloadedDescriptors:].cold.1
- +[MADAutoSetStager controlConvertStagedToDownloaded:]
- +[MADAutoSetStager controlConvertStagedToDownloaded:].cold.1
- +[MADAutoSetStager controlCopyCurrentStagedDescriptors]
- +[MADAutoSetStager controlCopyCurrentStagedDescriptors].cold.1
- +[MADAutoSetStager controlEliminateSelector:]
- +[MADAutoSetStager controlEliminateSelector:].cold.1
- +[MADAutoSetStager controlForcePurge:]
- +[MADAutoSetStager controlForcePurge:].cold.1
- +[MADAutoSetStager extendSummaryWithDeterminedAssets:basedOnControl:]
- +[MADAutoSetStager extendSummaryWithDeterminedAssets:basedOnControl:].cold.1
- +[MADAutoSetStager extendSummaryWithStagedAssets:basedOnControl:]
- +[MADAutoSetStager extendSummaryWithStagedAssets:basedOnControl:].cold.1
- +[MADAutoSetStager extendSummaryWithStagingAssets:basedOnControl:]
- +[MADAutoSetStager extendSummaryWithStagingAssets:basedOnControl:].cold.1
- +[MADAutoSetStager garbageCollectEliminateSelector:]
- +[MADAutoSetStager migrateMismatchedPersistedStateVersion:forEntryID:withMismatchedState:]
- +[MADAutoSetStager resumeFromPersisted]
- +[MADAutoSetStagerParam supportsSecureCoding]
- -[MADAutoAssetControlManager _eliminateBegin:forAssetSelector:fromLocation:]
- -[MADAutoAssetControlManager _scheduleAndCreateSetConfiguration:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:]
- -[MADAutoAssetControlManager initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager preInstalledSetDescriptorForSetInstance:dueToMessageName:]
- -[MADAutoAssetControlManager setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:]
- -[MADAutoAssetControlManager setConfigurationSelectUsingInfoInstance:dueToMessageName:]
- -[MADAutoAssetControlManagerParam initForStagerJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withAssetTargetOSVersion:withAssetTargetBuildVersion:withStagedToDownloaded:withDownloadingDescriptor:withBaseForPatchDescriptor:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withAssetTargetOSVersion:withAssetTargetBuildVersion:withStagedToDownloaded:withDownloadingDescriptor:withBaseForPatchDescriptor:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:].cold.1
- -[MADAutoAssetControlManagerParam initWithPromoted:]
- -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:asStagerJob:]
- -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:asStagerJob:].cold.1
- -[MADAutoAssetJob initForInstance:withAutoAssetUUID:]
- -[MADAutoAssetJob initForSelector:withAutoAssetUUID:asStagerJob:]
- -[MADAutoAssetJob installedOnFilesystemWithVersion:]
- -[MADAutoAssetJob startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withControlInformation:]
- -[MADAutoAssetJobParam initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withControlInformation:]
- -[MADAutoAssetJobParam initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAutoAssetDescriptor:withControlInformation:]
- -[MADAutoAssetStager _persistRebuildTrackingForFollowupEvent:]
- -[MADAutoAssetStager action_AddToAvailableDecideMoreCandidates:error:].cold.1
- -[MADAutoAssetStagerParam initWithAlreadyDownloadedDescriptors:]
- -[MADAutoAssetStagerParam initWithJobInformation:withOperationError:]
- -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withJobInformation:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:]
- -[MADAutoSetStager .cxx_destruct]
- -[MADAutoSetStager _acceptStagingClientRequest:]
- -[MADAutoSetStager _acknowledgeEliminatedForCurrentJob]
- -[MADAutoSetStager _acknowlegdeAndClearAllEliminations]
- -[MADAutoSetStager _addDescriptor:withRepresentation:toSummary:]
- -[MADAutoSetStager _allEliminationSelectors]
- -[MADAutoSetStager _cancelCurrentJob]
- -[MADAutoSetStager _clearAllTrackingOfActiveOperations]
- -[MADAutoSetStager _clearBeforeDetermineAvailable]
- -[MADAutoSetStager _controlConvertStagedToDownloaded:]
- -[MADAutoSetStager _doesSelector:matchDescriptor:]
- -[MADAutoSetStager _doesSelectorMatchCurrentJob:]
- -[MADAutoSetStager _extendSummaryWithDeterminedAssets:basedOnControl:]
- -[MADAutoSetStager _extendSummaryWithStagedAssets:basedOnControl:]
- -[MADAutoSetStager _extendSummaryWithStagingAssets:basedOnControl:]
- -[MADAutoSetStager _isAssetTypeInvolvedInStaging:]
- -[MADAutoSetStager _logPersistedConfigLoad:lastStagingFromOSVersion:lastStagingFromBuildVersion:assetTargetOSVersion:assetTargetBuildVersion:candidateAssetCount:determinedAvailableAssetCount:activelyStagingAssetCount:awaitingStagingAssetCount:stagedAssetCount:stagedAssetTotalContentBytes:message:]
- -[MADAutoSetStager _logPersistedConfigSet:message:]
- -[MADAutoSetStager _logPersistedEntry:operation:persistingDescriptor:withRepresentation:message:]
- -[MADAutoSetStager _logPersistedRemovedEntry:removedDescriptor:message:]
- -[MADAutoSetStager _logPersistedTableOfContents:]
- -[MADAutoSetStager _maintainLatestCandidate:candidateDescriptor:]
- -[MADAutoSetStager _persistDescriptor:operation:persistingDescriptor:withRepresentation:message:]
- -[MADAutoSetStager _persistLastStagingFrom]
- -[MADAutoSetStager _persistRebuildTrackingForFollowupEvent:]
- -[MADAutoSetStager _persistRemoveAll:message:flushing:]
- -[MADAutoSetStager _removeAllStagedContent]
- -[MADAutoSetStager _removeDescriptorFromSuccessfullyStaged:message:]
- -[MADAutoSetStager _removeEliminatedFromCandidatesAndAvaliable]
- -[MADAutoSetStager _removeEliminatedFromStaged]
- -[MADAutoSetStager _removeStagedAssetFromFilesystem:forHistoryOperation:]
- -[MADAutoSetStager _replyHaveStagedContent]
- -[MADAutoSetStager _replyNothingStaged]
- -[MADAutoSetStager _replyToStagingClient:withErrorCode:withUnderlyingError:withDescription:]
- -[MADAutoSetStager _replyToStagingClientOperationSuccess]
- -[MADAutoSetStager _setupAwaitingStagingAndBeginFirstDownload]
- -[MADAutoSetStager _stagingClientMessageDesire]
- -[MADAutoSetStager _stagingClientMessageInstance]
- -[MADAutoSetStager _trackReloadedDescriptorAvailableForStaging:]
- -[MADAutoSetStager _updateDescriptor:withLatestJobStatus:]
- -[MADAutoSetStager _updateLatestSummary]
- -[MADAutoSetStager actionUnknownAction:error:]
- -[MADAutoSetStager action_AddToAvailableDecideMoreCandidates:error:]
- -[MADAutoSetStager action_AddToStagedDecideMoreAvailable:error:]
- -[MADAutoSetStager action_CancelActiveJob:error:]
- -[MADAutoSetStager action_ClientAccept:error:]
- -[MADAutoSetStager action_ClientAcceptCancelActiveJob:error:]
- -[MADAutoSetStager action_ClientAcceptNextAvailableBeginDownload:error:]
- -[MADAutoSetStager action_ClientAcceptRemoveAllReplyPurged:error:]
- -[MADAutoSetStager action_ClientContinueUsingLatestRequest:error:]
- -[MADAutoSetStager action_ClientHaveStagedContent:error:]
- -[MADAutoSetStager action_ClientInvalidStagingPhase:error:]
- -[MADAutoSetStager action_ClientNothingStaged:error:]
- -[MADAutoSetStager action_ClientRequestAlreadyDownloaded:error:]
- -[MADAutoSetStager action_ControlUnstagedDecideCancelJob:error:]
- -[MADAutoSetStager action_ControlUnstagedDecideRemoveAll:error:]
- -[MADAutoSetStager action_DecideMoreAvailable:error:]
- -[MADAutoSetStager action_DecideMoreCandidates:error:]
- -[MADAutoSetStager action_DoneAvailableDecideAnyStaged:error:]
- -[MADAutoSetStager action_DoneCandidatesDecideAnyAvailable:error:]
- -[MADAutoSetStager action_EliminateAvailableDecideEmpty:error:]
- -[MADAutoSetStager action_EliminateCancelActiveJob:error:]
- -[MADAutoSetStager action_EliminateDecideMatch:error:]
- -[MADAutoSetStager action_EliminateDeterminingDecideMatch:error:]
- -[MADAutoSetStager action_EliminateDone:error:]
- -[MADAutoSetStager action_EliminateDoneDecideMoreCandidates:error:]
- -[MADAutoSetStager action_EliminateDoneDecideMoreDownload:error:]
- -[MADAutoSetStager action_EliminateDoneStagedDecideEmpty:error:]
- -[MADAutoSetStager action_FormCandidatesDecideDetermine:error:]
- -[MADAutoSetStager action_LoadPersistedDecideResume:error:]
- -[MADAutoSetStager action_NextAwaitingBeginDownload:error:]
- -[MADAutoSetStager action_NextCandidateBeginDetermine:error:]
- -[MADAutoSetStager action_RemeberEliminateDone:error:]
- -[MADAutoSetStager action_RemoveAllReplyPurged:error:]
- -[MADAutoSetStager action_ReplyHaveAvailable:error:]
- -[MADAutoSetStager action_ReplyHaveStaged:error:]
- -[MADAutoSetStager action_ReplyNoCandidates:error:]
- -[MADAutoSetStager action_ReplyNothingStaged:error:]
- -[MADAutoSetStager action_ReportStagingProgressToClient:error:]
- -[MADAutoSetStager action_ResumingNextAvailableBeginDownload:error:]
- -[MADAutoSetStager activeJobDescriptor]
- -[MADAutoSetStager alreadyDownloadedDescriptors]
- -[MADAutoSetStager alwaysPromoteStagedAssets]
- -[MADAutoSetStager assetTargetBuildVersion]
- -[MADAutoSetStager assetTargetOSVersion]
- -[MADAutoSetStager autoStagerFSM]
- -[MADAutoSetStager availableForStaging]
- -[MADAutoSetStager awaitingStagingAttempt]
- -[MADAutoSetStager candidatesForStaging]
- -[MADAutoSetStager description]
- -[MADAutoSetStager determiningBySelector]
- -[MADAutoSetStager eliminationSelectorsAcknowledged]
- -[MADAutoSetStager eliminationSelectors]
- -[MADAutoSetStager init]
- -[MADAutoSetStager init].cold.1
- -[MADAutoSetStager latestSafeSummary]
- -[MADAutoSetStager logger]
- -[MADAutoSetStager overallStagedDownloadedSoFarBytes]
- -[MADAutoSetStager overallStagedTotalExpectedBytes]
- -[MADAutoSetStager performAction:onEvent:inState:withInfo:nextState:error:]
- -[MADAutoSetStager persistedState]
- -[MADAutoSetStager setActiveJobDescriptor:]
- -[MADAutoSetStager setAlreadyDownloadedDescriptors:]
- -[MADAutoSetStager setAlwaysPromoteStagedAssets:]
- -[MADAutoSetStager setAssetTargetBuildVersion:]
- -[MADAutoSetStager setAssetTargetOSVersion:]
- -[MADAutoSetStager setAutoStagerFSM:]
- -[MADAutoSetStager setAvailableForStaging:]
- -[MADAutoSetStager setAwaitingStagingAttempt:]
- -[MADAutoSetStager setCandidatesForStaging:]
- -[MADAutoSetStager setDeterminingBySelector:]
- -[MADAutoSetStager setEliminationSelectors:]
- -[MADAutoSetStager setEliminationSelectorsAcknowledged:]
- -[MADAutoSetStager setLatestSafeSummary:]
- -[MADAutoSetStager setOverallStagedDownloadedSoFarBytes:]
- -[MADAutoSetStager setOverallStagedTotalExpectedBytes:]
- -[MADAutoSetStager setStagingClientRequest:]
- -[MADAutoSetStager setStagingFromBuildVersion:]
- -[MADAutoSetStager setStagingFromOSVersion:]
- -[MADAutoSetStager setSuccessfullyStaged:]
- -[MADAutoSetStager stagingClientRequest]
- -[MADAutoSetStager stagingFromBuildVersion]
- -[MADAutoSetStager stagingFromOSVersion]
- -[MADAutoSetStager stateTable]
- -[MADAutoSetStager successfullyStaged]
- -[MADAutoSetStager summary]
- -[MADAutoSetStagerParam .cxx_destruct]
- -[MADAutoSetStagerParam _summary]
- -[MADAutoSetStagerParam alreadyDownloaded]
- -[MADAutoSetStagerParam assetSelector]
- -[MADAutoSetStagerParam assetType]
- -[MADAutoSetStagerParam description]
- -[MADAutoSetStagerParam encodeWithCoder:]
- -[MADAutoSetStagerParam initWithAlreadyDownloadedDescriptors:]
- -[MADAutoSetStagerParam initWithAssetSelector:]
- -[MADAutoSetStagerParam initWithAssetType:]
- -[MADAutoSetStagerParam initWithCoder:]
- -[MADAutoSetStagerParam initWithJobInformation:withOperationError:]
- -[MADAutoSetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withJobInformation:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:]
- -[MADAutoSetStagerParam initWithSafeSummary:]
- -[MADAutoSetStagerParam initWithStagingClientRequest:]
- -[MADAutoSetStagerParam jobInformation]
- -[MADAutoSetStagerParam operationError]
- -[MADAutoSetStagerParam paramSafeSummary]
- -[MADAutoSetStagerParam paramType]
- -[MADAutoSetStagerParam setParamSafeSummary:]
- -[MADAutoSetStagerParam setStagingClientRequest:]
- -[MADAutoSetStagerParam stagingClientRequest]
- -[MADAutoSetStagerParam summary]
- -[MADAutoSetStagerParam updateSafeSummary]
- GCC_except_table116
- GCC_except_table147
- GCC_except_table155
- GCC_except_table18
- GCC_except_table20
- GCC_except_table213
- GCC_except_table24
- GCC_except_table385
- GCC_except_table388
- GCC_except_table39
- GCC_except_table390
- _OBJC_CLASS_$_MADAutoSetStager
- _OBJC_CLASS_$_MADAutoSetStagerParam
- _OBJC_IVAR_$_MADAutoSetStager._activeJobDescriptor
- _OBJC_IVAR_$_MADAutoSetStager._alreadyDownloadedDescriptors
- _OBJC_IVAR_$_MADAutoSetStager._alwaysPromoteStagedAssets
- _OBJC_IVAR_$_MADAutoSetStager._assetTargetBuildVersion
- _OBJC_IVAR_$_MADAutoSetStager._assetTargetOSVersion
- _OBJC_IVAR_$_MADAutoSetStager._autoStagerFSM
- _OBJC_IVAR_$_MADAutoSetStager._availableForStaging
- _OBJC_IVAR_$_MADAutoSetStager._awaitingStagingAttempt
- _OBJC_IVAR_$_MADAutoSetStager._candidatesForStaging
- _OBJC_IVAR_$_MADAutoSetStager._determiningBySelector
- _OBJC_IVAR_$_MADAutoSetStager._eliminationSelectors
- _OBJC_IVAR_$_MADAutoSetStager._eliminationSelectorsAcknowledged
- _OBJC_IVAR_$_MADAutoSetStager._latestSafeSummary
- _OBJC_IVAR_$_MADAutoSetStager._logger
- _OBJC_IVAR_$_MADAutoSetStager._overallStagedDownloadedSoFarBytes
- _OBJC_IVAR_$_MADAutoSetStager._overallStagedTotalExpectedBytes
- _OBJC_IVAR_$_MADAutoSetStager._persistedState
- _OBJC_IVAR_$_MADAutoSetStager._stagingClientRequest
- _OBJC_IVAR_$_MADAutoSetStager._stagingFromBuildVersion
- _OBJC_IVAR_$_MADAutoSetStager._stagingFromOSVersion
- _OBJC_IVAR_$_MADAutoSetStager._stateTable
- _OBJC_IVAR_$_MADAutoSetStager._successfullyStaged
- _OBJC_IVAR_$_MADAutoSetStagerParam._alreadyDownloaded
- _OBJC_IVAR_$_MADAutoSetStagerParam._assetSelector
- _OBJC_IVAR_$_MADAutoSetStagerParam._assetType
- _OBJC_IVAR_$_MADAutoSetStagerParam._jobInformation
- _OBJC_IVAR_$_MADAutoSetStagerParam._operationError
- _OBJC_IVAR_$_MADAutoSetStagerParam._paramSafeSummary
- _OBJC_IVAR_$_MADAutoSetStagerParam._paramType
- _OBJC_IVAR_$_MADAutoSetStagerParam._stagingClientRequest
- _OBJC_METACLASS_$_MADAutoSetStager
- _OBJC_METACLASS_$_MADAutoSetStagerParam
- __OBJC_$_CLASS_METHODS_MADAutoSetStager
- __OBJC_$_CLASS_METHODS_MADAutoSetStagerParam
- __OBJC_$_CLASS_PROP_LIST_MADAutoSetStagerParam
- __OBJC_$_INSTANCE_METHODS_MADAutoSetStager
- __OBJC_$_INSTANCE_METHODS_MADAutoSetStagerParam
- __OBJC_$_INSTANCE_VARIABLES_MADAutoSetStager
- __OBJC_$_INSTANCE_VARIABLES_MADAutoSetStagerParam
- __OBJC_$_PROP_LIST_MADAutoSetStager
- __OBJC_$_PROP_LIST_MADAutoSetStagerParam
- __OBJC_CLASS_PROTOCOLS_$_MADAutoSetStagerParam
- __OBJC_CLASS_RO_$_MADAutoSetStager
- __OBJC_CLASS_RO_$_MADAutoSetStagerParam
- __OBJC_METACLASS_RO_$_MADAutoSetStager
- __OBJC_METACLASS_RO_$_MADAutoSetStagerParam
- ___24-[MADAutoSetStager init]_block_invoke
- ___27-[MABrainUpdater schedule:]_block_invoke_3.352
- ___38+[MADAutoSetStager autoAssetSetStager]_block_invoke
- ___39+[MADAutoSetStager resumeFromPersisted]_block_invoke
- ___39+[MADAutoSetStager resumeFromPersisted]_block_invoke.cold.1
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.681
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.725
- ___53+[MADAutoSetStager controlConvertStagedToDownloaded:]_block_invoke
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.775
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.775.cold.1
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.782
- ___55+[MADAutoSetStager controlCopyCurrentStagedDescriptors]_block_invoke
- ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.787
- ___59-[MADAutoSetStager action_LoadPersistedDecideResume:error:]_block_invoke
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.662
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.682
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.764
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.782
- ___65+[MADAutoSetStager extendSummaryWithStagedAssets:basedOnControl:]_block_invoke
- ___66+[MADAutoSetStager extendSummaryWithStagingAssets:basedOnControl:]_block_invoke
- ___68-[ControlManager handleGetAllowNonUserInitiated:message:clientName:]_block_invoke
- ___68-[ControlManager handleServerUrlOverride:message:client:clientName:]_block_invoke
- ___69+[MADAutoSetStager extendSummaryWithDeterminedAssets:basedOnControl:]_block_invoke
- ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1609
- ___80-[ControlManager setPreferenceKeyAsync:andValue:allowNilToClear:replyUsing:and:]_block_invoke
- ___block_descriptor_83_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1185
- ___block_literal_global.1258
- ___block_literal_global.1556
- ___block_literal_global.1567
- ___block_literal_global.1575
- ___block_literal_global.1583
- ___block_literal_global.1591
- ___block_literal_global.1599
- ___block_literal_global.1893
- ___block_literal_global.1942
- ___block_literal_global.2445
- ___block_literal_global.2824
- ___block_literal_global.489
- ___block_literal_global.510
- ___block_literal_global.631
- ___block_literal_global.634
- ___block_literal_global.647
- ___block_literal_global.650
- ___block_literal_global.653
- ___block_literal_global.661
- ___block_literal_global.673
- ___block_literal_global.674
- ___block_literal_global.678
- ___block_literal_global.679
- ___block_literal_global.680
- ___block_literal_global.684
- ___block_literal_global.685
- ___block_literal_global.690
- ___block_literal_global.695
- ___block_literal_global.717
- ___block_literal_global.719
- ___block_literal_global.727
- ___block_literal_global.763
- ___block_literal_global.780
- ___block_literal_global.784
- ___block_literal_global.832
- ___block_literal_global.837
- ___block_literal_global.847
- ___block_literal_global.948
- ___block_literal_global.953
- ___block_literal_global.958
- ___block_literal_global.960
- ___block_literal_global.965
- ___block_literal_global.977
- __unnamed_array_storage.1847
- __unnamed_array_storage.1933
- __unnamed_array_storage.2191
- __unnamed_array_storage.2192
- __unnamed_array_storage.2197
- __unnamed_array_storage.2198
- __unnamed_array_storage.2283
- __unnamed_array_storage.2284
- __unnamed_array_storage.716
- __unnamed_array_storage.717
- __unnamed_array_storage.733
- __unnamed_array_storage.942
- __unnamed_array_storage.950
- __unnamed_array_storage.965
- _autoAssetSetStager.__autoAssetSetStager
- _autoAssetSetStager.dispatchOnceAutoAssetSetStager
- _objc_msgSend$_eliminateBegin:forAssetSelector:fromLocation:
- _objc_msgSend$_persistRebuildTrackingForFollowupEvent:
- _objc_msgSend$_scheduleAndCreateSetConfiguration:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:
- _objc_msgSend$autoAssetSetStager
- _objc_msgSend$autoAssetStagerJobDetermineDone:withDetermineError:
- _objc_msgSend$autoAssetStagerJobDetermineDone:withDetremineError:
- _objc_msgSend$autoAssetStagerJobDownloadDone:withDownloadError:
- _objc_msgSend$controlAlreadyDownloadedDescriptors:
- _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:asStagerJob:
- _objc_msgSend$initForInstance:withAutoAssetUUID:
- _objc_msgSend$initForSelector:withAutoAssetUUID:asStagerJob:
- _objc_msgSend$initForStagerJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:
- _objc_msgSend$initWithAlreadyDownloadedDescriptors:
- _objc_msgSend$initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withControlInformation:
- _objc_msgSend$initWithJobInformation:withOperationError:
- _objc_msgSend$initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withAssetTargetOSVersion:withAssetTargetBuildVersion:withStagedToDownloaded:withDownloadingDescriptor:withBaseForPatchDescriptor:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAutoAssetDescriptor:withControlInformation:
- _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withJobInformation:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:
- _objc_msgSend$initWithPromoted:
- _objc_msgSend$initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:
- _objc_msgSend$installedOnFilesystemWithVersion:
- _objc_msgSend$isSetDescriptor:coveredBySetDescriptorStatus:
- _objc_msgSend$locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:
- _objc_msgSend$locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:
- _objc_msgSend$locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:
- _objc_msgSend$preInstalledSetDescriptorForSetInstance:dueToMessageName:
- _objc_msgSend$setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:
- _objc_msgSend$setConfigurationSelectUsingInfoInstance:dueToMessageName:
- _objc_msgSend$stagerResumed:
- _objc_msgSend$stagerStartJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:
- _objc_msgSend$stagerStartJobDownloadForStaging:withAssetTargetOSVersion:withAssetTargetBuildVersion:
- _objc_msgSend$startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withControlInformation:
CStrings:
+ "\x01\x1c"
+ "\n{chooseNewerSetDescriptor}  left:%{public}@"
+ "\n{chooseNewerSetDescriptor} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided left (right previously staged) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (left previously staged) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} ignoring (invalid restore version) | foundLeftEntry:%{public}@ | nextRightEntry:%{public}@"
+ "\n{chooseNewerSetDescriptor} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
+ "\n{chooseNewerSetDescriptor} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} right:%{public}@"
+ "\n{chooseNewerSetDescriptor} | leftIsNewer | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetDescriptor} | leftNotPresent | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetDescriptor} | leftRightSame | left:%@ | right:%@"
+ "\n{chooseNewerSetDescriptor} | leftRightSame | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetDescriptor} | rightIsNewer | left:%@ | right:%@"
+ "\n{chooseNewerSetDescriptor} | rightIsNewer | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetDescriptor} | rightNotPresent | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetStatus} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} ignoring (invalid restore version) | foundLeftEntry:%{public}@ | nextRightEntry:%{public}@"
+ "\n{chooseNewerSetStatus} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
+ "\n{chooseNewerSetStatus} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} left:%{public}@"
+ "\n{chooseNewerSetStatus} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetStatus} right:%{public}@"
+ "\n{chooseNewerSetStatus} | leftIsNewer | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetStatus} | leftNotPresent | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetStatus} | leftRightSame | left:%@ | right:%@"
+ "\n{chooseNewerSetStatus} | leftRightSame | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetStatus} | rightIsNewer | left:%{public}@ | right:%{public}@"
+ "\n{chooseNewerSetStatus} | rightNotPresent | left:%{public}@ | right:%{public}@"
+ "\x11\x1c"
+ "\x11\x1f\x0f\b"
+ "\x1f"
+ "\x1f\f&"
+ "%@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, however, download appears to be complete. Previous Total Downloaded: %lld, Total Expected: %lld"
+ "%@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, likely stalled."
+ "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} AssetCacheServices not present in this OS, download from: %@"
+ "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} Attempting to get cache server url"
+ "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} not allowed to use caching server, download from: %@"
+ "%@\n[DOWNLOAD_INFO] {updateDownloadData} In progress and totalWritten is less than previous total (%lld < %lld), nsurl is backtracking significantly for %@. task %@"
+ "%@,0"
+ "%@.0.0.0.0,0"
+ "%@:_routeClientReuest"
+ "%@:_scheduleAndCreateSetConfiguration"
+ "%@:_scheduledAndRouteClientRequest"
+ "%@:atomicInstanceRemove"
+ "%@:handleSetClientCheckAtomic"
+ "%@:handleSetClientLockAtomic"
+ "%@:newSetDescriptorIfOtherSatisfying"
+ "%@:persistSetDescriptorDownloadedJob"
+ "%@:preInstalledSetDescriptorForSetInstance"
+ "%@:trackSetDescriptor"
+ "%@_%@_%@_%@"
+ "%{public}@\n[AUTO-STAGER] AUTO-STAGING-PROGRESS | client not provided progress | client does not respond to executeGenericBlock | overallStatus:%{public}@"
+ "%{public}@\n[AUTO-STAGER] AUTO-STAGING-PROGRESS | early progress before totalExpectedBytes indicated (ignored) | currentStatus:%{public}@"
+ "%{public}@\n[AUTO-STAGER] AUTO-STAGING-PROGRESS | staging-client provided with progress | overallStatus:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_logPersistedTableOfContents} unable to load entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} end determine-if-available | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} reply to staging-client:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} failed to allocate availableDescriptor | %{public}@ | nextSetEntry:%{public}@ | promotionSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} failed to allocate availableDescriptor | nextSetEntry:%{public}@ | promotionSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} located already-downloaded descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} not pre-SU-staging descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} unable to load persisted set-lookup-result file | set-eventInfo:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {AddToAvailableDecideMoreCandidates} unable to locate asset metadata | nextSetEntry:%{public}@ | promotionSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {ClientContinueRestartingMaxDetermining} staging-client-request was received when already performing requested operation (stale earlier request has been replied to with failure)"
+ "%{public}@\n[AUTO-STAGER] {ClientContinueUsingLatestRequest} staging-client-request was received when already performing requested operation (stale earlier request has been replied to with failure)"
+ "%{public}@\n[AUTO-STAGER] {ClientInvalidStagingPhase} reply to staging-client:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided %ld downloaded descriptor%{public}@ - potential candidate%{public}@ for staging"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type + asset-specifier + asset-version being eliminated - not considering downloaded | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type + asset-specifier being eliminated - not considering downloaded | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type being eliminated - not considering downloaded | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} auto-control-manager provided no downloaded descriptors - no candidate(s) for staging"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} have downloaded auto-asset candidate(s) for staging"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} nil encountered on alreadyDownloaded array | eventInfo:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} nil encountered on consideringDescriptors array"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} no candidate descriptors for staging"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} should have candidates yet unable to form set-lookup array"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} %{public}@ | MA_MILESTONE | (no promotion) | setLookupResults:%ld"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} %{public}@ | MA_MILESTONE | handedOffAsPromoted:%ld | setLookupResults:%ld"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} available entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} candidate entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had been determing with candidates for potential staging found (resuming determining) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had been staging (resuming staging) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had determined available for staging (resuming determined) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have content staged from currently running OS (resumed to staged) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content now applicable to the currently running OS (migrating) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content when configured to always promote (and now running target OS) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content when configured to always promote (not running target OS) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} inconsistency in staged information (purging) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} mismatched entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no persisted entries (purging) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no persisted indication of any pre-software-update-staging status | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no staging was in progress / no candidates / no staged content (purging to start clean) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} persisted entry counts match staging summary counts"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} preserving successfully staged content"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staged content from different OS (purging) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staged entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staging entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staging summary differs from per-entry totals | stagingSummary:%{public}@ | entryTotals:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} unable to determine previous status for entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} unable to load entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} unknown representation(%ld) for entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {NextAwaitingBeginDownload} begin download-for-staging | activeJobDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {NextAwaitingBeginDownload} unable to form autoAssetCatalog | stagingDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {NextCandidateBeginDetermine} begin determine-if-available | stagerSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {ReplyHaveAvailable} have available content for staging | MA_MILESTONE"
+ "%{public}@\n[AUTO-STAGER] {ReplyHaveStaged} have staged content | MA_MILESTONE"
+ "%{public}@\n[AUTO-STAGER] {_controlConvertStagedToDownloaded} IMMEDIATE-PROMOTION | %{public}@ | MA_MILESTONE"
+ "%{public}@\n[AUTO-STAGER] {_controlConvertStagedToDownloaded} NO-IMMEDIATE-PROMOTION: not staged | selectorToBecomeDownloaded:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_doesSelector:matchDescriptor} match for asset-type + asset-specifier + asset-version of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_doesSelector:matchDescriptor} match for asset-type + asset-specifier of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_doesSelector:matchDescriptor} match for asset-type of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_doesSelector:matchDescriptor} not a match | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} nil asset-type for asset-descriptor | autoAssetDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} nil encountered on alreadyDownloadedDescriptors array"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} not staging auto-asset (does not support pre-SU-staging) | autoAssetDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} not staging auto-asset (from downloaded [set target removes]) | autoAssetDescriptor:%@ | setConfig(by-asset-type):%ld"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} stage auto-asset (from downloaded [no set target]) | autoAssetDescriptor:%@ | setConfig(by-asset-type):%ld"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} stage auto-asset (from downloaded [set target includes]) | autoAssetDescriptor:%@ | setConfig(by-asset-type):%ld"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} nil encountered on setTargets array"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} nil set-entry encountered on setTargets array | setTargets:\n%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithSetConfigurations} stage auto-asset (from target) | nextSetEntry:%@ | lookupAssets(by-asset-type):%ld"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] asset-selector already tracked as candidate | setConfiguration:%{public}@ | assetType:%{public}@ | assetSpecifier:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] extended set-configuration for staging | setConfiguration:%{public}@ | assetSetEntry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] new set-configuration for staging | setConfiguration:%{public}@ | assetSetEntry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] unable to create asset-set-entry | assetType:%{public}@ | assetSpecifier:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] unable to locate additional asset-set-entry | assetType:%{public}@ | assetSpecifier:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetType} [%{public}@] unable to locate asset-set-entry | assetType:%{public}@ | assetSpecifier:%{public}@ | clientDefinedSetConfiguration:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_formCandidateSetLookupArray} formed set-configurations (for determine lookups):%ld"
+ "%{public}@\n[AUTO-STAGER] {_formCandidateSetLookupArray} set-configuration (%ld of %ld):%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_formCandidateSetLookupArray} unable to load stager-set-configuration from by-asset-type dict (dropping from candidates) | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_isSetTargetWithinRange} set-target versions not comparable (ignoring) | setTarget:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} accepted as candidate | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} best candidate so far | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} examining preSoftwareUpdateAssetStaging descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} nil candidateDescriptor provided by caller"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} not considering (not preSoftwareUpdateAssetStaging) | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} not newer version | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_maintainLatestCandidate} versions not comparable (keeping already encountered) | descriptor:%{public}@, already:%@"
+ "%{public}@\n[AUTO-STAGER] {_persistRebuildTrackingNewHandedOffDescriptors} persistedDescriptor candidateForStaging ignored (candidates come from stager-set-configurations) | entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_persistRebuildTrackingNewHandedOffDescriptors} promoted descriptor count:%ld"
+ "%{public}@\n[AUTO-STAGER] {_persistRebuildTrackingNewHandedOffDescriptors} unable to determine previous status for entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_persistRebuildTrackingNewHandedOffDescriptors} unable to load persistedDescriptor from persisted-state for entry:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeEliminatedFromCandidatesAndAvaliable} beginning to eliminate allEliminationSelectors:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeEliminatedFromStaged} elimination-selector for asset-type + asset-specifier + asset-version being eliminated - removed from successfully-staged | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeEliminatedFromStaged} elimination-selector for asset-type + asset-specifier being eliminated - removed from successfully-staged | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeEliminatedFromStaged} elimination-selector for asset-type being eliminated - removed from successfully-staged | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeEliminatedFromStaged} nil stagedDescriptor encountered on successfullyStaged for stagedSelectorKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeStagedAssetFromFilesystem} failed to remove stagedDescriptor:%{public}@ | localContentURL:%{public}@ | error:%{public}@\n%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeStagedAssetFromFilesystem} not on filesystem for stagedDescriptor:%{public}@ | localContentURL:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeStagedAssetFromFilesystem} successfully removed stagedDescriptor:%{public}@ | localContentURL:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_replyToStagingClientOperationSuccess} reply to staging-client:operationSuccess"
+ "%{public}@\n[AUTO-STAGER] {_setConfigurationForAssetDescriptor} unable to locate set-target entry when set-target allows entry | assetType:%{public}@ | assetSpecifier:%{public}@ | setTarget:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_setupAwaitingStagingAndBeginFirstDownload} available #%ld awaiting staging for descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_setupAwaitingStagingAndBeginFirstDownload} cleared awaiting staging (unable to locate first descriptor when awaitingStagingAttempt count:%ld)"
+ "%{public}@\n[AUTO-STAGER] {_setupAwaitingStagingAndBeginFirstDownload} nil encountered on availableForStaging array"
+ "%{public}@\n[AUTO-STAGER] {_setupAwaitingStagingAndBeginFirstDownload} unable to form autoAssetCatalog | stagingDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_stagingClientMessageInstance} invalid assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_trackReloadedDescriptorAvailableForStaging} nil persistedDescriptor provided by caller"
+ "%{public}@\n[AUTO-STAGER] {_trackReloadedDescriptorAvailableForStaging} | ignoring additional persisted entry for descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_trimConsideringToLatestDownloaded} best candidate so far | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_trimConsideringToLatestDownloaded} not newer version | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_trimConsideringToLatestDownloaded} versions not comparable (keeping already encountered) | descriptor:%{public}@, already:%@"
+ "%{public}@\n[AUTO-STAGER] {assetMetadataFromAssetCatalog} Assets array in set-catalog lookup response missing asset-specifier | assetSpecifier:%{public}@ | autoAssetSetCatalog:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {assetMetadataFromAssetCatalog} key value is not an array | setCatalogKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {assetMetadataFromAssetCatalog} unable to determine key/value from set-catalog | setCatalogKey:%{public}@ | setCatalogValue:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {garbageCollectEliminateSelector} not staged | eliminateSelector:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {loadPersistedSetLookupResults} content on filesystem validated | entryID:%{public}@, adopted setLookupResult:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {loadPersistedSetLookupResults} no persisted set-lookup-results to be resumed"
+ "%{public}@\n[AUTO-STAGER] {loadPersistedSetLookupResults} unable to retrieve set-lookup-result | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} Assets array in set-catalog lookup response missing asset-specifier | assetSpecifier:%{public}@ | autoAssetSetCatalog:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} found no matching asset-specifier in set-catalog lookup response | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} key value is not an array | setCatalogKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} no Assets array in set-catalog lookup response | autoAssetSetCatalog:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} set-catalog lookup response for different asset-type | assetType:%{public}@ | catalogAssetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} set-catalog lookup response has no auto-assets for asset-type | assetType:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newAssetMetadataFromAssetCatalog} unable to determine key/value from set-catalog | setCatalogKey:%{public}@ | setCatalogValue:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newSetLookupResultsForTargetOS} unable to retrieve set-lookup-result | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {newSetLookupResult} ignoring empty entry | assetMetadata:%{public}@"
+ "%{public}@ | {%{public}@:installedOnFilesystemWithVersion} considering by-version count:%ld, looking for assetVersion:%{public}@, locatedDescriptor:%{public}@"
+ "%{public}@ | {%{public}@:replyToJobsWhenCatalogDownloaded} stager-job encountering presumed stale trigger to reply on catalog download"
+ "%{public}@ | {ReportCatalogDecideFound} postponing[RAMPED] autoAsset:%{public}@"
+ "%{public}@ | {StagerDownloadDecideFilesystem} found already downloaded (on filesystem) asset %{public}@"
+ "%{public}@ | {StagerDownloadDecideFilesystem} using cached lookup result for asset-selector | followupParam:%{public}@"
+ "%{public}@ | {checkFilesystemAndDecidePurgeOrLookup} will attempt lookup for stager-formed set-configuration"
+ "%{public}@ | {determineWhetherNetworkConnectivityError} job completed successfully"
+ "%{public}@ | {determineWhetherNetworkConnectivityError} no underlying | jobFinishedError:%{public}@"
+ "%{public}@ | {determineWhetherNetworkConnectivityError} non-networking failure | underlyingError:%{public}@"
+ "%{public}@ | {determineWhetherNetworkConnectivityError} potential network failure | underlyingError:%{public}@"
+ "%{public}@ | {newSessionID} created base portion for session ID (low-order digits from preferences) | basePortion:%{public}@"
+ "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} auto-control-manager known descriptor count:%ld | specifierSelector:%{public}@, versionSelector:%{public}@"
+ "%{public}@ | {reportSetCatalogDecideFound} mixture of Ramping indications - considering overall set as NOT ramped | nextAsset:%{public}@"
+ "%{public}@ | {reportSetCatalogDecideFound} postponing[RAMPED] setConfiguration:%{public}@"
+ "-[ControlManager getSAFRegistrationBundleID:]"
+ "-[ControlManager handleGetAllowNonUserInitiated:message:clientName:]"
+ "-[ControlManager registerAssetsWithSpaceAttributes]"
+ "-[MABrainUpdater schedule:]_block_invoke_4"
+ ".%@"
+ ".0"
+ "/\x0e\x1f\x11\"c"
+ "2.0.20"
+ "2.0.5"
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88@96B104B108@112"
+ "@128@0:8q16@24@32@40@48@56@64@72@80@88@96@104@112@120"
+ "@132@0:8q16@24@32@40@48@56B64@68@76@84@92@100@108@116@124"
+ "@304@0:8q16@24@32@40@48@?56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240B248B252@256@264@272@280@288@296"
+ "@56@0:8@16@24@32@40B48B52"
+ "@60@0:8@16@24B32@36@44@52"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "A set configuration different than the currently defined set configuration is provided"
+ "ADD_FEWEER_CONFIG_ENTRIES  "
+ "ALL_INSTANCES"
+ "AUTO-CONTROL(NextAwaitingBeginDownload)"
+ "AUTO-CONTROL-MANAGER | Initialized | bootedOSVersion:%{public}@ | bootedOBuildVersion:%{public}@"
+ "AUTO-CONTROL:{restoreVersionFromOSVersion} too many elements | osVersion:%{public}@"
+ "AUTO-STAGER-SET-LOOKUP-RESULTS"
+ "AUTO_ASSET_STAGER_AS_CLIENT"
+ "AUTO_ASSET_STAGER_SET"
+ "AddToAvailableDecideAnyAvailable"
+ "An empty configuration for a set is not allowed"
+ "AutoAssetAsIfBackground"
+ "AutoAssetAsIfRamp"
+ "AutoAssetLogSetCompare"
+ "AutoAssetMaxStagerDeterminingSecs"
+ "AutoAssetSessionIDBase"
+ "AutoSetJob(%@)[%@]"
+ "AutoSetLookupResults"
+ "AutoSetTargets"
+ "AutoStagerSetLookupResults"
+ "B20@0:8B16"
+ "CancelActivityAck"
+ "Channel ID is nil for identifier %@"
+ "ClientContinueRestartingMaxDetermining"
+ "D\x1f\x0f\x06\x16<'\x12"
+ "DESCRIPTOR"
+ "DawnB"
+ "DeterminingLast"
+ "EMPTY"
+ "Existing assets are registered with Space Attribution."
+ "Exiting mobileassetd for release testing..."
+ "FROM_STAGED"
+ "FROM_STAGED_FOR_ALL"
+ "Failed to modify asset configuration with the provided asset configuration"
+ "FormCandidatesDecideDetermine"
+ "KNOWN-SET-TARGETS"
+ "MA-AUTO(REPLY):CANCEL_ACTIVITY_FOR_SELECTOR"
+ "MA-AUTO-STAGE(REPLY):DETERMINE_ALL_AVAILABLE_FOR_UPDATE"
+ "MA-AUTO-STAGE:DETERMINE_ALL_AVAILABLE_FOR_UPDATE"
+ "MA-AUTO:CANCEL_ACTIVITY_FOR_SELECTOR"
+ "MADAutoSetLookupResult"
+ "MADAutoSetTarget"
+ "NWPathStatusInvalid"
+ "NWPathStatusSatisfiable"
+ "NWPathStatusUnsatisfied"
+ "PROMOTED"
+ "Ramp"
+ "SAFBundleIdentifier"
+ "SD_DISCOVERED[%@](domain:%@|setID:%@|atomic:%@)"
+ "SD_DOWNLOADED[%@](domain:%@|setID:%@|atomic:%@)"
+ "SD_GONE[%@](domain:%@|setID:%@|atomic:%@)"
+ "SD_INCOMPLETE[%@](domain:%@|setID:%@|atomic:%@)"
+ "SD_LOOKUP[%@](domain:%@|setID:%@)"
+ "SET-TARGET"
+ "SET_LOOKUP_RESULTS"
+ "SET_TARGETS"
+ "SLKUP"
+ "SSLUP"
+ "STAGED-SET-CONFIGURATIONS"
+ "STAGER_LOOKUP|autoAssetCatalog:%@|baseDescriptors:%ld|determineError[%@]"
+ "STAGER_PROMOTED|stagedToDownloaded:%ld|stagedSetLookupResults:%ld"
+ "STAGER_SET_START|setConfig[%@]|policy:%@|assetTarget[OSVersion:%@|BuildVersion:%@|TrainName:%@|RestoreVersion:%@]"
+ "STAGER_START|selector[%@]|patchingFrom:%@|catalog:%@|policy:%@|assetTargetOSVersion:%@|assetTargetBuildVersion:%@"
+ "STAGER_TARGET|[(assetTarget)OSVersion:%@|BuildVersion:%@|TrainName:%@|RestoreVersion:%@]|%@"
+ "STAGING_ALREADY_DOWNLOADED|alreadyDownloaded:%ld|setConfigurations:%ld|setTargets:%ld|scheduledJobs:%ld"
+ "STAGING_AUTO_ASSET_CATALOG|autoAssetCatalog:%@[%@]|baseForPatching:%ld"
+ "STAGING_JOB_INFORMATION|jobInformation:%@|downloadedDescriptor:%@[%@]"
+ "STARG"
+ "SetCatalogDoneDetermine"
+ "SetDoneDetermine"
+ "SpaceAttributionRegisterVersion"
+ "StagerSetJob(%@)[entries:%ld]"
+ "Starting built-in MobileAsset brain built Oct  5 2023 21:17:05"
+ "Starting downloaded MobileAsset brain (version: %@) built Oct  5 2023 21:17:05"
+ "T@\"MADAutoAssetDescriptor\",R,&,N,V_downloadedDescriptor"
+ "T@\"MADAutoAssetPersisted\",&,N,V_persistedSetLookupResults"
+ "T@\"MADAutoAssetPersisted\",&,N,V_persistedSetTargets"
+ "T@\"MADAutoSetConfiguration\",&,N,V_activeSetJobConfiguration"
+ "T@\"MADAutoSetConfiguration\",&,N,V_stagerFormedSetConfiguration"
+ "T@\"MANAutoAssetSetPolicy\",&,N,V_setPolicy"
+ "T@\"MANAutoAssetSetPolicy\",&,N,V_stagerSetPolicy"
+ "T@\"NSArray\",&,N,V_baseForStagingDescriptors"
+ "T@\"NSArray\",&,N,V_requestedAutoAssetEntries"
+ "T@\"NSArray\",&,N,V_scheduledJobs"
+ "T@\"NSArray\",&,N,V_setConfigurations"
+ "T@\"NSArray\",&,N,V_setTargets"
+ "T@\"NSArray\",&,N,V_stagedSetLookupResults"
+ "T@\"NSArray\",R,&,N,V_scheduledJobs"
+ "T@\"NSArray\",R,&,N,V_setConfigurations"
+ "T@\"NSArray\",R,&,N,V_setTargets"
+ "T@\"NSDictionary\",&,N,V_cachedAutoAssetCatalog"
+ "T@\"NSDictionary\",&,N,V_stagerJobAutoAssetCatalog"
+ "T@\"NSMutableArray\",&,N,V_baseForStagingDescriptors"
+ "T@\"NSMutableArray\",&,N,V_candidateSetConfigurations"
+ "T@\"NSMutableDictionary\",&,N,V_setLookupResults"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_pathStatusDispatchQueue"
+ "T@\"NSString\",&,N,V_assetTargetRestoreVersion"
+ "T@\"NSString\",&,N,V_assetTargetTrainName"
+ "T@\"NSString\",&,N,V_bootedOBuildVersion"
+ "T@\"NSString\",&,N,V_bootedOSVersion"
+ "T@\"NSString\",&,N,V_preferenceSessionIDBase"
+ "T@\"NSString\",&,N,V_stagerAssetTargetRestoreVersion"
+ "T@\"NSString\",&,N,V_stagerAssetTargetTrainName"
+ "TB,N,V_awaitingCancelActivityAck"
+ "TB,N,V_limitedToCancelActivity"
+ "TB,N,V_pathToServerIsUp"
+ "TB,N,V_preferenceAsIfBackground"
+ "TB,N,V_preferenceAsIfBackgroundSpecified"
+ "TB,N,V_preferenceAsIfRamp"
+ "TB,N,V_preferenceAsIfRampSpecified"
+ "TB,N,V_preferenceAutoAssetLogSetCompare"
+ "TimeoutDetermining"
+ "Tq,N,V_preferenceMaxStagerDeterminingSecs"
+ "[%@]AutoAssetStager"
+ "[%@|instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
+ "[%{public}@] {%{public}@e} | NOT removing nextSetAtomicInstance:%{public}@"
+ "[%{public}@] {%{public}@} NO_WAIT_NOT_PERISTED | successful lock | chosenDownloadedSetDescriptor:%{public}@"
+ "[%{public}@] {%{public}@} [CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
+ "[%{public}@] {%{public}@} new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
+ "[%{public}@] {%{public}@} unable to load persisted-set-atomic-instance file | nextRemoveSetInstance:%{public}@"
+ "[%{public}@] {%{public}@} | removing nextSetAtomicInstance:%{public}@"
+ "[%{public}@] {_reclaimDownloadedDescriptorsWhenJustDownloaded} encountered blank auto-asset-descriptor - removing | entryID:%{public}@"
+ "[%{public}@] {_reclaimDownloadedDescriptorsWhenJustDownloaded} encountered downloaded descriptor not on the filesystem - removing | entryID:%{public}@"
+ "[%{public}@] {_reclaimDownloadedDescriptorsWhenJustDownloaded} removing older downloaded descriptor | removingDescriptor:%{public}@, keepingDescriptor:%{public}@"
+ "[%{public}@] {_reclaimDownloadedDescriptorsWhenJustDownloaded} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@] {_reclaimDownloadedDescriptorsWhenJustDownloaded} unable to load auto-asset-descriptor | entryID:%{public}@"
+ "[%{public}@] {_removeAllContentForEliminateTracker} reviewed all downloadedDescriptorsBySelector(%ld) | removeDescriptors:%ld | notRemovedStillLocked:%ld | eliminateTracker:%{public}@, lockedEliminateSelectors:%ld"
+ "[%{public}@] {handleSetClientAssetSetForStagingRequest} unable to load persisted-set-target file | setTarget:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} preserving previously staged | setAtomicInstance:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance with no asset-entries on filesystem | entryID:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance without backing set-descriptor | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetConfigurations} no persisted set-targets to be resumed"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} no entryID"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor has no downloaded asset - dropped | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor validated | entryID:%{public}@, adoptedSetDescriptor[fromStaged]:%{public}@"
+ "[%{public}@] {loadPersistedSetLookupResults} content on filesystem validated | entryID:%{public}@, adopted setLookupResult:%{public}@"
+ "[%{public}@] {loadPersistedSetLookupResults} no persisted set-lookup-results to be resumed"
+ "[%{public}@] {loadPersistedSetLookupResults} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetLookupResults} unable to load set-lookup-result | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetTargets} content on filesystem validated | entryID:%{public}@, adopted setTarget:%{public}@"
+ "[%{public}@] {loadPersistedSetTargets} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetTargets} unable to load set-target | entryID:%{public}@"
+ "[%{public}@] {locateSetLookupResultSatisfying} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@] {locateSetLookupResultSatisfying} unable to load set-lookup-result | entryID:%{public}@"
+ "[%{public}@] {newSetLookupResultsForTargetOS} unable to load set-lookup-result | entryID:%{public}@"
+ "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@\n#_%{public}@:(%{public}@) [%{public}@] | [%{public}@] intervalSecs:%{public}@ | remaininSecs:%{public}@ | requiringRetry:%{public}@ | setPolicy:%{public}@\n#_%{public}@:%{public}@"
+ "[AUTO-STAGER] {startMaxTimeSpentDeterminingTimer} begin timed determine-all-available | maxTimeSpentDeterminingSecs:%ld"
+ "[AUTO-STAGER] {startMaxTimeSpentDeterminingTimer} maxTimeSpentDeterminingSecs DISABLED"
+ "[AUTO-STAGER] {startMaxTimeSpentDeterminingTimer} unable to create maxDeterminingTimer | maxTimeSpentDeterminingSecs:%ld"
+ "[CONNECTION-OBSERVER] {initForServerPath} NWPathEvaluator not available | pathToServer:%{public}@"
+ "[CONNECTION-OBSERVER] {initForServerPath} starting DOWN | pathStatus:%{public}@ | pathToServer:%{public}@"
+ "[CONNECTION-OBSERVER] {initForServerPath} starting UP | pathStatus:NWPathStatusSatisfied | pathToServer:%{public}@"
+ "[CONNECTION-OBSERVER] {observeValueForKeyPath} connection DOWN | pathStatus:NWPathStatusUnsatisfied | pathToServer:%{public}@"
+ "[CONNECTION-OBSERVER] {observeValueForKeyPath} connection UP | pathStatus:NWPathStatusSatisfied | pathToServer:%{public}@"
+ "[CONTROL_MANAGER_CACHEDELETE_QUEUE] {respondToCacheDelete} performing cache-delete triggered operation..."
+ "[MA_PREFS] Read preference from: %@ for: %@ value: `%@` (%@)"
+ "[MA_PREFS] {%@} [%@] Could not synchronize preferences for %@ - this may be a permissions error"
+ "[MA_PREFS] {%@} [%@] Synchronized preferences for %@"
+ "[MA_PREFS] {%@} [%@] nil preference key provided"
+ "[MA_PREFS] {%@} [%@] | Completed operation to update preference %@ %@ to nil (clear)"
+ "[MA_PREFS] {%@} [%@] | Completed operation to update preference %@ %@ to string '%@'"
+ "[MA_PREFS] {%@} [%@] | attemptsMade:%d | Unable to synchronize after setting preference %@ %@ to nil (clear)"
+ "[MA_PREFS] {%@} [%@] | attemptsMade:%d | Unable to synchronize after setting preference %@ %@ to string '%@'"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number (from string)"
+ "[MA_PREFS] {_MAPreferencesCopyNSArrayOfNumbersValue} invalid type for key:%@ | expecting array of numbers"
+ "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%@ | expecting string or number or boolean"
+ "[assetType:%@]%@"
+ "[cachedAssetSetID:%@|downloadedFromLive:%@|lastTimeChecked:%@|postedDate:%@|atomicEntries:%ld]"
+ "[clientRequest:%@|assetSelector:%@|awaitingSchedulerAck:%@|awaitingCancelActivityAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@|limitedToCancelActivity:%@]"
+ "[clientRequest:%@|clientDomain:%@|setIdentifier:%@|awaitingSchedulerAck:%@|awaitingCancelActivityAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@|limitedToCancelActivity:%@]"
+ "[fromOS:%@,fromBuild:%@,targetOS:%@,targetBuild:%@|targetTrain:%@|targetRestoreVersion:%@|clientRequest:%@|activeDescriptor:%@|candidates:%ld,determining:%ld,available:%ld|awaitingStaging:%ld|staged:%ld|elimination:%ld,eliminationAck:%ld]"
+ "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
+ "_ASSetAssetServerURLForAssetType"
+ "_MAPreferencesSetStringValue"
+ "_MAPreferencesSetStringValue_block_invoke"
+ "_MAPreferencesSync_block_invoke"
+ "_activeSetJobConfiguration"
+ "_assetTargetRestoreVersion"
+ "_assetTargetTrainName"
+ "_awaitingCancelActivityAck"
+ "_baseForStagingDescriptors"
+ "_bootedOBuildVersion"
+ "_bootedOSVersion"
+ "_cachedAutoAssetCatalog"
+ "_candidateSetConfigurations"
+ "_downloadedDescriptor"
+ "_eliminateAtomicTriggeredByClient"
+ "_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:"
+ "_eliminateAtomicTriggeredWhileLoading:forClientDomainName:forAssetSetIdentifier:"
+ "_eliminateBegin:forAssetSelector:limitingToActivity:fromLocation:"
+ "_extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:"
+ "_extendLookupByAssetType:fromSource:withAssetType:withAssetSpecifier:withDownloadDecryptionKey:"
+ "_extendLookupByAssetTypeWithDownloadedDescriptors:"
+ "_extendLookupByAssetTypeWithSetConfigurations:"
+ "_formCandidateSetLookupArray"
+ "_isAssetSetEntry:blockedBySetTarget:"
+ "_isDescriptorAssetTypeManagedAsSet:"
+ "_isSetTargetWithinRange:asCandidate:"
+ "_limitSetAtomicEntries:fromSetDescriptor:requestedAutoAssetEntries:"
+ "_limitedToCancelActivity"
+ "_logPersistedSetLookupResult:operation:forPersistedEntryID:withSetLookupResult:message:"
+ "_logPersistedSetLookupResultRemoved:removedPersistedEntryID:removedSetLookupResult:message:"
+ "_logPersistedSetLookupResultTableOfContents:"
+ "_logPersistedSetTarget:operation:forPersistedEntryID:withSetTarget:message:"
+ "_logPersistedSetTargetRemoved:removedPersistedEntryID:removedSetTarget:message:"
+ "_logPersistedSetTargetTableOfContents:"
+ "_messageAssetPolicyDownloadUserInitiated:forClientRequest:"
+ "_newSelectorForCachedAssetCatalog:"
+ "_pathStatusDispatchQueue"
+ "_pathToServerIsUp"
+ "_persistRebuildTrackingNewHandedOffDescriptors"
+ "_persistRebuildTrackingNewHandedOffDescriptors:"
+ "_persistedSetLookupResults"
+ "_persistedSetTargets"
+ "_preferenceAsIfBackground"
+ "_preferenceAsIfBackgroundSpecified"
+ "_preferenceAsIfRamp"
+ "_preferenceAsIfRampSpecified"
+ "_preferenceAutoAssetLogSetCompare"
+ "_preferenceMaxStagerDeterminingSecs"
+ "_preferenceSessionIDBase"
+ "_reclaimDownloadedDescriptorsWhenJustDownloaded"
+ "_requestedAutoAssetEntries"
+ "_scheduleAndCreateSetConfiguration:fromLocation:errorString:"
+ "_scheduledJobs"
+ "_setConfigurationForAssetType:forAssetSpecifier:"
+ "_setConfigurationHasEntriesWhenTargeting:"
+ "_setConfigurations"
+ "_setLookupResults"
+ "_setPolicyFromClientRequest:"
+ "_setTargetForAssetType:"
+ "_setTargetForSetConfiguration:"
+ "_setTargets"
+ "_stagedSetLookupResults"
+ "_stagerAssetTargetRestoreVersion"
+ "_stagerAssetTargetTrainName"
+ "_stagerFormedSetConfiguration"
+ "_stagerJobAutoAssetCatalog"
+ "_stagerSetPolicy"
+ "_stagingClientMessageStaging"
+ "_trimConsideringToLatestDownloaded:"
+ "action_AddToAvailableDecideAnyAvailable:error:"
+ "action_CancelActivityAck:error:"
+ "action_ClientContinueRestartingMaxDetermining:error:"
+ "action_SetDoneDetermine:error:"
+ "activeSetJobConfiguration"
+ "allAvailableForStagingAttributes"
+ "altered set-configuration auto-asset-entries to align with set-target | setConfiguration:%@ | setTarget:%@"
+ "asset-selector missing asset-specifier when required for cancel-activity request"
+ "assetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:preferringBestFormat:"
+ "assetSetEntryForAssetType:forAssetSpecifier:"
+ "assetTargetRestoreVersion"
+ "assetTargetTrainName"
+ "atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:"
+ "atomicInstanceRemovedSetJob"
+ "autoAssetStagerJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:"
+ "autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:"
+ "autoAssetStagerSetJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:"
+ "awaitingCancelActivityAck"
+ "baseForPatchingToSelector:"
+ "baseForStagingDescriptors"
+ "bootedBuildVersion"
+ "bootedOBuildVersion"
+ "bootedOSVersion"
+ "cachedAutoAssetCatalog"
+ "candidateSetConfigurations"
+ "checkAndInitiateDownloadForAssetType"
+ "client setting preference"
+ "clientDomain:%@|setIdentifier:%@|targetOSVersion:%@..%@|autoAssetEntries:%ld"
+ "com.apple.MobileAsset.AutoAssetStager.client"
+ "com.apple.MobileAsset.autoassetconnectorobserver.status"
+ "com.apple.MobileAsset.preferencesDomain"
+ "controlAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:"
+ "determineWhetherNetworkConnectivityError:"
+ "doesSetDescriptor:coverAllForAutoAssetEntries:"
+ "doesSetDescriptor:coverRequestedAutoAssetEntries:"
+ "doesSetDescriptor:matchSetConfiguration:"
+ "downloadedDescriptor"
+ "downloadedEntryForAssetType:forAssetSpecifier:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "findAtomicEntryForAssetType:forAssetSpecifier:representedByLookupResult:"
+ "firstAssetType"
+ "firstAssetTypeForSetEntries:"
+ "firstEntryAssetType"
+ "getSAFRegistrationBundleID:"
+ "handleClientCancelActivityForSelectorRequest"
+ "handleClientCancelActivityForSelectorRequest:"
+ "handleClientConnection"
+ "handleStagingClientDetermineAllAvailableForUpdateRequest:"
+ "have not detected first-unlock since MA daemon startup"
+ "includesEntryForAssetType:forAssetSpecifier:"
+ "initForAssetType:withAssetSpecifier:withAssetVersion:assetLockedInhibitsRemoval:"
+ "initForAssetType:withAssetSpecifier:withAssetVersion:usingDecryptionKey:assetLockedInhibitsRemoval:"
+ "initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:"
+ "initForClientDomainName:forAssetSetIdentifier:fromMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:"
+ "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:"
+ "initForInstance:withAutoAssetUUID:downloadingUserInitiated:"
+ "initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:"
+ "initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:"
+ "initForStagerJobLookupResults:withBaseForStagingDescriptors:withDetermineError:"
+ "initForStagerJobStart:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:"
+ "initForStagerSetJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:"
+ "initWithAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduldJobs:"
+ "initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:"
+ "initWithAutoAssetCatalog:withBaseForStagingDescriptors:withOperationError:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithContentsOfURL:error:"
+ "initWithJobInformation:withDownloadedDescriptor:withOperationError:"
+ "initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withAutoAssetDescriptor:withControlInformation:"
+ "initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:"
+ "initWithPromoted:withSetLookupResults:"
+ "initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:withClientAssetPolicy:"
+ "installedOnFilesystemWithVersion:fromLocation:"
+ "invalid set-eventInfo (no set-identifier to be altered) | set-eventInfo:%@"
+ "isAnyAssetEntryOnFilesystemForSetDescriptor:"
+ "isMorePreferredAssetFormat:comparedTo:"
+ "isRamped"
+ "jobControlInformationForSetConfiguration:"
+ "limitedToCancelActivity"
+ "loadPersistedSetDownloadedDescriptors(incomplete)"
+ "loadPersistedSetDownloadedDescriptors(missing)"
+ "loadPersistedSetDownloadedDescriptors(validated)"
+ "loadPersistedSetLookupResults"
+ "loadPersistedSetTargets"
+ "locateDownloadedNewBySelectorLimitedToStaging:"
+ "locateNewAllSetConfigurations"
+ "locateNewAllSetTargets"
+ "locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:"
+ "locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:"
+ "locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPrevoiuslyStagedFound:fromLocation:"
+ "locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:"
+ "locateSetLookupResultSatisfying"
+ "locateSetLookupResultSatisfying:"
+ "locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:"
+ "lockSetAlreadyCompletedToClient"
+ "logger:%@|policy:%@|server:%@|table:%@|FSM:%@|(persisted)activeJobs:%@,knownDescriptors:%@,setConfigurations:%@,setAtomicInstances:%@,activeSes:%@,downloadedSets:%@,setTargets:%@,setLookupConfigurations:%@,setLockUsageMap:%@"
+ "lookupBootedBuildVersion"
+ "lookupBootedOSVersion"
+ "lookupCacheUpdateWithDetermineResult:fromLocation:"
+ "migrateMismatchedPersistedSetPromotionVersion:forEntryID:withMismatchedState:"
+ "migrateMismatchedPersistedSetTargetVersion:forEntryID:withMismatchedState:"
+ "migrateMismatchedPersistedStagedSetConfiguration:forEntryID:withMismatchedState:"
+ "new set %@atomic-instance added | setAtomicInstance:%@"
+ "new set-lookup-result | setLookupResult:%@"
+ "new set-target"
+ "newAssetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:"
+ "newSetDescriptorLimitedToLockInformation:forSetConfiguration:"
+ "newSetEntryIDForClientDomainName:forAssetSetIdentifier:forMinTargetOS:forMaxTargetOS:"
+ "newSetLookupResult:forSetCatalog:"
+ "newSetLookupResultsForTargetOS"
+ "newSetTargetFromClientProvidedSetTarget:forClientDomainName:forSetIdentifier:"
+ "no auto-asset-instance provided in client cancel-activity request"
+ "no set-target entries provided in request | MISSING REQUIRED FIELD"
+ "pallasRequestV2"
+ "pathStatusDispatchQueue"
+ "pathToCatalogLookupServer"
+ "pathToServerIsUp"
+ "persistedSetLookupResults"
+ "persistedSetTargets"
+ "persisting server URL"
+ "preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:"
+ "preferenceAsIfBackground"
+ "preferenceAsIfBackgroundOrUse:"
+ "preferenceAsIfBackgroundSpecified"
+ "preferenceAsIfRamp"
+ "preferenceAsIfRampOrUse:"
+ "preferenceAsIfRampSpecified"
+ "preferenceAutoAssetLogSetCompare"
+ "preferenceMaxStagerDeterminingSecs"
+ "preferenceSessionIDBase"
+ "previous MA daemon execution was running from different OS version than booted OS version"
+ "previous MA daemon execution was running version prior to having support for set-lookup-results"
+ "previous MA daemon execution was running version prior to having support for set-targets"
+ "q40@0:8@16@24^@32"
+ "q48@0:8@16@24@32^@40"
+ "refererncesAssetType:"
+ "registerAssetsWithSpaceAttributes"
+ "removePreviouslyStagedSetDescriptors"
+ "removeSetTargetsForClientDomain:forSetIdentifier:fromLocation:"
+ "removed previously defined set-target | setTarget:%@"
+ "requestedAutoAssetEntries"
+ "restoreVersionFromOSVersion:"
+ "scheduledJobs"
+ "set-identifier (for given client-domain-name) is not currently defined"
+ "set-lookup-result describing Pallas atomicity | setLookupResult:%@"
+ "set-lookup-result validated"
+ "set-target validated"
+ "setActiveSetJobConfiguration:"
+ "setAssetTargetRestoreVersion:"
+ "setAssetTargetTrainName:"
+ "setAwaitingCancelActivityAck:"
+ "setBaseForStagingDescriptors:"
+ "setBootedOBuildVersion:"
+ "setBootedOSVersion:"
+ "setCachedAutoAssetCatalog:"
+ "setCandidateSetConfigurations:"
+ "setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:selectedConfig:"
+ "setConfigurationSelectUsingInfoInstance:dueToMessageName:selectedConfig:"
+ "setConfigurations"
+ "setInfoInstance is not provided in request | MISSING REQUIRED FIELD"
+ "setLimitedToCancelActivity:"
+ "setLookupResult"
+ "setLookupResultLoadedFromPersisted"
+ "setLookupResultLoadedFromPersisted:persistedEntryID:"
+ "setLookupResults"
+ "setPathToServerIsUp:"
+ "setPersistedSetLookupResults:"
+ "setPersistedSetTargets:"
+ "setPreferenceAsIfBackground:"
+ "setPreferenceAsIfBackgroundSpecified:"
+ "setPreferenceAsIfRamp:"
+ "setPreferenceAsIfRampSpecified:"
+ "setPreferenceAutoAssetLogSetCompare:"
+ "setPreferenceKeySync"
+ "setPreferenceMaxStagerDeterminingSecs:"
+ "setPreferenceSessionIDBase:"
+ "setRequestedAutoAssetEntries:"
+ "setScheduledJobs:"
+ "setSetConfigurations:"
+ "setSetLookupResults:"
+ "setSetTargets:"
+ "setStagedSetLookupResults:"
+ "setStagerAssetTargetRestoreVersion:"
+ "setStagerAssetTargetTrainName:"
+ "setStagerFormedSetConfiguration:"
+ "setStagerJobAutoAssetCatalog:"
+ "setStagerSetPolicy:"
+ "setTarget"
+ "setTargetEntries:matchSetConfiguration:"
+ "setTargetNewEntryIDForClientDomainName:forAssetSetIdentifier:forClientProvidedSetTarget:"
+ "setTargets"
+ "stagedSetLookupResults"
+ "stager has provided set-lookup-results for OS just booteed into - clearing now-stale entries"
+ "stager-job determine-if-available done yet no auto-asset-catalog"
+ "stagerAssetTargetRestoreVersion"
+ "stagerAssetTargetTrainName"
+ "stagerFormedSetConfiguration"
+ "stagerJobAutoAssetCatalog"
+ "stagerResumed:withSetLookupResults:"
+ "stagerStartJobDownloadForStaging:withStagerSetConfiguration:usingCachedAutoAssetCatalog:usingBaseForPatching:withAssetTargetOSVersion:withAssetTargetBuildVersion:"
+ "stagerStartSetJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:"
+ "staging-client-request [DETERMINE_ALL_AVAILABLE_FOR_UPDATE] without staging update-attributes | stagingClientRequest:%@"
+ "startMaxTimeSpentDeterminingTimer"
+ "startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:"
+ "starting stager-job to dowload for staging"
+ "successfully defined asset-set-for-staging"
+ "unable to locate set-lookup-results"
+ "updateSpaceAttributionForBundleID:assetPath:doRegistration:"
+ "{%@:_logPersistedSetConfigurationRemoved} %@ | no persistedEntryID to remove | %@ | removedSetTarget:%@"
+ "{%@:_logPersistedSetLookupResultRemoved} %@ | no persistedEntryID to remove | %@ | removedSetLookupResult:%@"
+ "{%@:_logPersistedSetLookupResult} %@:%@ | no persistedEntryID | %@ | setLookupResult:%@"
+ "{%@:_logPersistedSetTarget} %@:%@ | no persistedEntryID | %@ | setTarget:%@"
+ "{%@} nil setJobDescriptor"
+ "{%@} no nextAtomicEntry | nextSetEntry:%@ | satisfyingSetDescriptor:%@"
+ "{%@} no set-configuration found when have chosen set-descriptor"
+ "{%@} | invalid eventInfo (instance:MISSING) | eventInfo:%@"
+ "{%@} | invalid eventInfo |messageName:%@|message:%@|instance:%@"
+ "{%@} | invalid set-eventInfo (instance:MISSING) | set-eventInfo:%@"
+ "{%{public}@:_logPersistedSetLookupResultTableOfContents} | (%{public}@) %{public}@ | unable to load entry:%{public}@"
+ "{%{public}@:_logPersistedSetTargetTableOfContents} | (%{public}@) %{public}@ | unable to load entry:%{public}@"
+ "{%{public}@:removeSetTargetsForClientDomain} | no set-taget entry found for entry:%{public}@"
+ "{%{public}@:removeSetTargetsForClientDomain} | unable to determine previous set-target for entry:%{public}@"
+ "{%{public}@:removeSetTargetsForClientDomain} | unable to re-load set-target for entry:%{public}@"
+ "{AddToAvailableDecideMoreCandidates} active-set-job set-configuration without assetType | activeSetJobConfiguration:%@"
+ "{AddToAvailableDecideMoreCandidates} active-set-job without base for staging descriptors | activeSetJobConfiguration:%@"
+ "{AddToAvailableDecideMoreCandidates} active-set-job without catalog lookup results | activeSetJobConfiguration:%@"
+ "{AddToStagedDecideMoreAvailable} no downloaded descriptor provided"
+ "{CancelActivityAck} duplicate cancel-activity-ack indication for eliminateTracker:%@"
+ "{CancelActivityAck} not tracking eliminate for autoAssetSelector:%@"
+ "{ControlManager:getSAFRegistrationBundleID} Fail to read content from %@. Error: %@"
+ "{ControlManager:getSAFRegistrationBundleID} Unable to find bundle ID from '%@' key and asset type from %@ key in: %@"
+ "{ControlManager:getSAFRegistrationBundleID} Unable to parse Info.plist in %@ to dictionary"
+ "{ControlManager:registerAssetsWithSpaceAttributes} Registering downloaded and preInstalled mobile assets with space attribution framework."
+ "{NextCandidateBeginDetermine} no candidates available for staging (after considering downloaded auto-assets and set-identifiers)"
+ "{PromoteResumeScheduler} | set-lookup-results when had previous lookup-results"
+ "{ResumeJobs} | Preserved Persisted-State | ActiveJobs:%ld, KnownDescriptors:%ld | Locks:%ld, Scheduled:%ld, Staged:%ld | SetConfigurations:%ld, AtomicInstances:%ld, ActiveSetDescriptors:%ld, DownloadedSetDescriptors:%ld, SetTargets:%ld, SetLookupResults:%ld"
+ "{SetDoneDetermine} not a stager-job"
+ "{_acceptStagingClientRequest} staging-client-request [DETERMINE_ALL_AVAILABLE_FOR_UPDATE] without staging information | stagingClientRequest:%@"
+ "{_acceptStagingClientRequest} staging-client-request [DETERMINE_ALL_AVAILABLE_FOR_UPDATE] without staging update-attributes | stagingClientRequest:%@"
+ "{_newSelectorForCachedAssetCatalog} Selector could not be determined from set-catalog lookup response | autoAssetSetCatalog:%{public}@"
+ "{_newSelectorForCachedAssetCatalog} key value is not an array | setCatalogKey:%{public}@ | autoAssetSetCatalog:%{public}@"
+ "{_newSelectorForCachedAssetCatalog} unable to determine key/value from set-catalog | setCatalogKey:%{public}@ | setCatalogValue:%{public}@ | autoAssetSetCatalog:%{public}@"
+ "{_persistRebuildTrackingNewHandedOffDescriptors} unsupported asset representation(%d) - not adopting persisted descriptor:%@"
+ "{_persistRebuildTrackingNewHandedOffDescriptors} | should have asset(s) to be promoted yet none to hand off to auto-control-manager"
+ "{_setConfigurationHasEntriesWhenTargeting} no auto-asset-entries for set-configuration:%@"
+ "{_stagingClientMessageStaging} incomplete staging-client-request:%@"
+ "{atomicInstanceRemovedSetJob} MISSING atomicInstanceUUID | nextSetAtomicInstance:%@"
+ "{doesSetDescriptor:coverRequestedAutoAssetEntries:} unable to form foundSelectorKey | fullAssetSelector:%@"
+ "{handleSetClientAssetSetForStagingRequest} persisted-entry already exists when should have just been removed | setTarget:%@ | %@"
+ "{isSSONeededForURL} Adding %@ to set of domains needing SSO"
+ "{loadPersistedSetTargets} no set-configuration for set-target | setTarget:%@"
+ "{loadPersistedSetTargets} set-target versions not comparable (ignoring) | setTarget:%@"
+ "{loadPersistedSetTargets} | no set-taget entry found for entry:%{public}@"
+ "{loadPersistedSetTargets} | unable to determine previous status for entry:%{public}@"
+ "{locateNewAllSetConfigurations} | no set-configuration entry found for entry:%{public}@"
+ "{locateNewAllSetConfigurations} | unable to determine previous status for entry:%{public}@"
+ "{locateNewAllSetTargets} | no set-taget entry found for entry:%{public}@"
+ "{locateNewAllSetTargets} | unable to determine previous status for entry:%{public}@"
+ "{mostSpecificSelectorToReport} no selector reported | jobSummary:%@"
+ "{mostSpecificSelectorToReport} unable to create copy-of-selector (returning un-clean selector) | jobSummary:%@"
- "\x01\x16"
- "\x11\x1a"
- "\x11\x1f\x0f\x02"
- "\x1e"
- "\x1f\x02\""
- "\x1f\x02&"
- "%{public}@ | AUTO-STAGING-PROGRESS | client not provided progress | client does not respond to executeGenericBlock | overallStatus:%{public}@"
- "%{public}@ | AUTO-STAGING-PROGRESS | early progress before totalExpectedBytes indicated (ignored) | currentStatus:%{public}@"
- "%{public}@ | AUTO-STAGING-PROGRESS | staging-client provided with progress | overallStatus:%{public}@"
- "%{public}@ | {%{public}@} reply to staging-client:%{public}@"
- "%{public}@ | {AddToAvailableDecideMoreCandidates} activeJobDescriptor:%{public}@ | end determine-if-available"
- "%{public}@ | {AddToAvailableDecideMoreCandidates} failed to allocate availableDescriptor | %{public}@ | jobInformation:%{public}@"
- "%{public}@ | {AddToAvailableDecideMoreCandidates} failed to allocate availableDescriptor | jobInformation:%{public}@"
- "%{public}@ | {AddToAvailableDecideMoreCandidates} located already-downloaded descriptor:%{public}@"
- "%{public}@ | {ClientInvalidStagingPhase} reply to staging-client:%{public}@"
- "%{public}@ | {FormCandidatesDecideDetermine} auto-control-manager provided %ld downloaded descriptor%{public}@ - potential candidate%{public}@ for staging"
- "%{public}@ | {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type + asset-specifier + asset-version being eliminated - not considering downloaded | descriptor:%{public}@"
- "%{public}@ | {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type + asset-specifier being eliminated - not considering downloaded | descriptor:%{public}@"
- "%{public}@ | {FormCandidatesDecideDetermine} auto-control-manager provided downloaded descriptor for asset-type being eliminated - not considering downloaded | descriptor:%{public}@"
- "%{public}@ | {FormCandidatesDecideDetermine} auto-control-manager provided no downloaded descriptors - no candidate(s) for staging"
- "%{public}@ | {FormCandidatesDecideDetermine} nil encountered on alreadyDownloaded array | eventInfo:%{public}@"
- "%{public}@ | {FormCandidatesDecideDetermine} nil encountered on consideringDescriptors array"
- "%{public}@ | {FormCandidatesDecideDetermine} no candidates for staging"
- "%{public}@ | {NextAwaitingBeginDownload} activeJobDescriptor:%{public}@ | begin download-for-staging"
- "%{public}@ | {NextCandidateBeginDetermine} activeJobDescriptor:%{public}@ | begin determine-if-available"
- "%{public}@ | {ReplyHaveAvailable} have available content for staging | MA_MILESTONE"
- "%{public}@ | {ReplyHaveStaged} have staged content | MA_MILESTONE"
- "%{public}@ | {_doesSelector:matchDescriptor} match for asset-type + asset-specifier + asset-version of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
- "%{public}@ | {_doesSelector:matchDescriptor} match for asset-type + asset-specifier of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
- "%{public}@ | {_doesSelector:matchDescriptor} match for asset-type of active stager-job | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
- "%{public}@ | {_doesSelector:matchDescriptor} not a match | checkMatchSelector:%{public}@ | candidateDescriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} best candidate so far | descriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} considering preSoftwareUpdateAssetStaging descriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} examining preSoftwareUpdateAssetStaging descriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} nil candidateDescriptor provided by caller"
- "%{public}@ | {_maintainLatestCandidate} not considering (not preSoftwareUpdateAssetStaging) descriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} not newer version | descriptor:%{public}@"
- "%{public}@ | {_maintainLatestCandidate} versions not comparable (keeping already encountered) | descriptor:%{public}@, already:%@"
- "%{public}@ | {_removeEliminatedFromCandidatesAndAvaliable} beginning to eliminate allEliminationSelectors:%{public}@"
- "%{public}@ | {_removeEliminatedFromStaged} elimination-selector for asset-type + asset-specifier + asset-version being eliminated - removed from successfully-staged | descriptor:%{public}@"
- "%{public}@ | {_removeEliminatedFromStaged} elimination-selector for asset-type + asset-specifier being eliminated - removed from successfully-staged | descriptor:%{public}@"
- "%{public}@ | {_removeEliminatedFromStaged} elimination-selector for asset-type being eliminated - removed from successfully-staged | descriptor:%{public}@"
- "%{public}@ | {_removeEliminatedFromStaged} nil stagedDescriptor encountered on successfullyStaged for stagedSelectorKey:%{public}@"
- "%{public}@ | {_removeStagedAssetFromFilesystem} failed to remove stagedDescriptor:%{public}@ | localContentURL:%{public}@ | error:%{public}@\n%{public}@"
- "%{public}@ | {_removeStagedAssetFromFilesystem} not on filesystem for stagedDescriptor:%{public}@ | localContentURL:%{public}@"
- "%{public}@ | {_removeStagedAssetFromFilesystem} successfully removed stagedDescriptor:%{public}@ | localContentURL:%{public}@"
- "%{public}@ | {_replyToStagingClientOperationSuccess} reply to staging-client:operationSuccess"
- "%{public}@ | {_setupAwaitingStagingAndBeginFirstDownload} available #%ld awaiting staging for descriptor:%{public}@"
- "%{public}@ | {_setupAwaitingStagingAndBeginFirstDownload} cleared awaiting staging (unable to locate first descriptor when awaitingStagingAttempt count:%ld)"
- "%{public}@ | {_setupAwaitingStagingAndBeginFirstDownload} nil encountered on availableForStaging array"
- "%{public}@ | {_stagingClientMessageInstance} invalid assetType:%{public}@"
- "%{public}@ | {_trackReloadedDescriptorAvailableForStaging} nil persistedDescriptor provided by caller"
- "%{public}@ | {installedOnFilesystemWithVersion} considering by-version count:%ld, looking for version: %{public}@, found: %{public}@"
- "%{public}@ | {refreshOnFilesystemFromManagerPromotingIfStaged} auto-control-manager known descriptor count:%ld | specifiedSelector:%{public}@, versionSelector:%{public}@"
- "(%@) new set %@atomic-instance added | setAtomicInstance:%@"
- "+"
- "-[ControlManager handleGetAllowNonUserInitiated:message:clientName:]_block_invoke"
- "-[ControlManager handleServerUrlOverride:message:client:clientName:]_block_invoke"
- "/\r\x1c\x11\x12a"
- "2.0.18"
- "@100@0:8@16@24@32@40@48@56@64@72@80@88B96"
- "@116@0:8q16@24@32@40@48@56B64@68@76@84@92@100@108"
- "@256@0:8q16@24@32@40@48@?56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200B208B212@216@224@232@240@248"
- "@80@0:8q16@24@32@40@48@56@64@72"
- "Adding %@ to set of domains needing SSO"
- "AssetCacheServices not present in this OS, download from: %@"
- "Attempting to get cache server url"
- "AutoSetJob"
- "Channel ID is nil for identifer %@"
- "ClientFormCandidatesDecideDetermine"
- "Completed operation to update preference %@ %@ to nil (clear)"
- "Completed operation to update preference %@ %@ to string '%@'"
- "Could not synchronize prefs for %@ - this may be a permissions error"
- "D\x1f\x0f\x03\x16:'\x12"
- "Dawn"
- "Download has not progressed since last update, however, download appears to be complete. Previous Total Downloaded: %lld, Total Expected: %lld"
- "Download has not progressed since last update, likely stalled."
- "In progress and totalWritten is less than previous total (%lld < %lld), nsurl is backtracking significantly for %@. task %@"
- "MADAutoSetStager"
- "MADAutoSetStagerParam"
- "Read preference from: %@ for: %@ value: `%@` (%@)"
- "SD_DISCOVERED(domain:%@|setID:%@|atomic:%@)"
- "SD_DOWNLOADED(domain:%@|setID:%@|atomic:%@)"
- "SD_GONE(domain:%@|setID:%@|atomic:%@)"
- "SD_INCOMPLETE(domain:%@|setID:%@|atomic:%@)"
- "SD_LOOKUP(domain:%@|setID:%@)"
- "STAGER_PROMOTED|stagedToDownloaded:%ld"
- "STAGER_START|selector[%@]|assetTargetOSVersion:%@|assetTargetBuildVersion:%@"
- "STAGER_TARGET|assetTargetOSVersion:%@|assetTargetBuildVersion:%@|%@"
- "STAGING_ALREADY_DOWNLOADED|alreadyDownloaded:%lld"
- "STAGING_JOB_INFORMATION|jobInformation:%@[%@]"
- "Specified set configuration is different than currently defined set configuration"
- "StagerSetJob"
- "Starting built-in MobileAsset brain built Sep 15 2023 13:57:07"
- "Starting downloaded MobileAsset brain (version: %@) built Sep 15 2023 13:57:07"
- "T@\"MADAutoSetDescriptor\",&,N,V_activeJobDescriptor"
- "T@\"MADAutoSetJobInformation\",R,&,N,V_jobInformation"
- "UPDATED_SET_STATUS"
- "[%@|instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
- "[%{public}@] {%{public}@:_doesEliminateSelector} considering | eliminateSelector:%{public}@, assetType:%{public}@, assetSpecifier:%{public}@, assetVersion:%{public}@"
- "[%{public}@] {%{public}@:_doesEliminateSelector} eliminate-selector for asset-type + asset-specifier + asset-version match | eliminateSelector:%{public}@"
- "[%{public}@] {%{public}@:_doesEliminateSelector} eliminate-selector for asset-type + asset-specifier match | eliminateSelector:%{public}@"
- "[%{public}@] {%{public}@:_doesEliminateSelector} eliminate-selector for asset-type match | eliminateSelector:%{public}@"
- "[%{public}@] {%{public}@:_routeClientRequest} [CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceRemove} unable to load persisted-set-atomic-instance file | nextRemoveSetInstance:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceRemove} | NOT removing nextSetAtomicInstance:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceRemove} | removing nextSetAtomicInstance:%{public}@"
- "[%{public}@] {_removeAllContentForEliminateTracker} dropped from consideration for removal (still locked) | eliminateSelector:%{public}@, lockedSelector:%{public}@"
- "[%{public}@] {_removeAllContentForEliminateTracker} reviewing all downloadedDescriptorsBySelector(%ld) | eliminateTracker:%{public}@, lockedEliminateSelectors:%ld"
- "[%{public}@] {_removeAllContentForEliminateTracker} will eliminate | eliminateTracker:%{public}@, downloadedDescriptor:%{public}@"
- "[%{public}@] {_removeAllContentForEliminateTracker} will not eliminate | eliminateTracker:%{public}@, downloadedDescriptor:%{public}@"
- "[%{public}@] {chooseNewerSetDescriptor} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
- "[%{public}@] {chooseNewerSetDescriptor} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetDescriptor} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
- "[%{public}@] {chooseNewerSetStatus} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {chooseNewerSetStatus} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "[%{public}@] {handleSetClientLockAtomic} NO_WAIT_NOT_PERISTED | successful lock | chosenDownloadedSetDescriptor:%{public}@"
- "[%{public}@] {newSetDescriptorIfOtherSatisfying} new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
- "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@\n#_%{public}@:(%{public}@) [%{public}@] | [%{public}@] intervalSecs:%{public}@ | remaininSecs:%{public}@ | setPolicy:%{public}@\n#_%{public}@:%{public}@"
- "[CONTROL_MANAGER_ASSET_QUEUE] {respondToCacheDelete} performing cache-delete triggered operation..."
- "[clientRequest:%@|clientDomain:%@|setIdentifier:%@|awaitingSchedulerAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@]"
- "[fromOS:%@,fromBuild:%@,targetOS:%@,targetBuild:%@|clientRequest:%@|activeDescriptor:%@|candidates:%ld,determining:%ld,available:%ld|awaitingStaging:%ld|staged:%ld|elimination:%ld,eliminationAck:%ld]"
- "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
- "_MAPreferencesSync"
- "_eliminateBegin:forAssetSelector:fromLocation:"
- "_persistRebuildTrackingForFollowupEvent"
- "_persistRebuildTrackingForFollowupEvent:"
- "_scheduleAndCreateSetConfiguration"
- "_scheduleAndCreateSetConfiguration:"
- "atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:"
- "autoAssetSetStager"
- "autoAssetSetStagerJobDetermineDone:withDetermineError:"
- "autoAssetSetStagerJobDownloadDone:withDownloadError:"
- "autoAssetSetStagerJobDownloadProgress:withProgressError:"
- "autoAssetSetStagerJobFailedToStart:"
- "autoAssetStagerJobDetermineDone:withDetermineError:"
- "autoAssetStagerJobDetermineDone:withDetremineError:"
- "autoAssetStagerJobDownloadDone:withDownloadError:"
- "byID"
- "controlAlreadyDownloadedDescriptors:"
- "handleSetClientAssetSetForStagingRequest - not yet implemented"
- "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:asStagerJob:"
- "initForInstance:withAutoAssetUUID:"
- "initForSelector:withAutoAssetUUID:asStagerJob:"
- "initForStagerJobStart:withAssetTargetOSVersion:withAssetTargetBuildVersion:"
- "initWithAlreadyDownloadedDescriptors:"
- "initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withControlInformation:"
- "initWithJobInformation:withOperationError:"
- "initWithParamType:withSafeSummary:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withAssetTargetOSVersion:withAssetTargetBuildVersion:withStagedToDownloaded:withDownloadingDescriptor:withBaseForPatchDescriptor:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "initWithParamType:withSafeSummary:withClientRequest:withAutoAssetSelector:withAutoAssetJobID:withAutoAssetCatalog:whereCatalogFromLookupCache:withFinishedError:withDownloadProgress:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAutoAssetDescriptor:withControlInformation:"
- "initWithParamType:withSafeSummary:withStagingClientRequest:withJobInformation:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:"
- "initWithPromoted:"
- "initialStatusForJob:usingSelector:withJobUUID:downloadingDescriptor:baseForPatchDescriptor:"
- "installedOnFilesystemWithVersion:"
- "invalid set-eventInfo (no set-identifer to be altered) | set-eventInfo:%@"
- "locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:"
- "locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:"
- "locateSetStatusPreferringByInstance:elseByClientDomain:forAssetSetIdentifier:"
- "logger:%@|policy:%@|server:%@|table:%@|FSM:%@|(persisted)activeJobs:%@,knownDescriptors:%@,setConfigurations:%@,setAtomicInstances:%@,activeSes:%@,downloadedSets:%@,setLockUsageMap:%@"
- "not allowed to use caching server, download from: %@"
- "preInstalledSetDescriptorForSetInstance:dueToMessageName:"
- "setConfigurationNewSetConfiguration:forSetInfoInstance:dueToMessageName:"
- "setConfigurationSelectUsingInfoInstance:dueToMessageName:"
- "stagerResumed:"
- "stagerStartJobDetermineIfAvailable:withAssetTargetOSVersion:withAssetTargetBuildVersion:"
- "stagerStartJobDownloadForStaging:withAssetTargetOSVersion:withAssetTargetBuildVersion:"
- "staging-client-request missing:MANAutoAssetSetInfoDesire | staging-client-request:%@"
- "startStagerDetermineIfAvailable:withAssetTargetBuildVersion:withControlInformation:"
- "{%@:_scheduledAndRouteClientRequest} | invalid eventInfo (instance:MISSING) | eventInfo:%@"
- "{%@:_scheduledAndRouteClientRequest} | invalid eventInfo |messageName:%@|message:%@|instance:%@"
- "{%@:_scheduledAndRouteClientRequest} | invalid set-eventInfo (instance:MISSING) | set-eventInfo:%@"
- "{%@:newSetDescriptorIfOtherSatisfying} no nextAtomicEntry | nextSetEntry:%@ | satisfyingSetDescriptor:%@"
- "{%@:trackSetDescriptor} nil setJobDescriptor"
- "{ClientContinueUsingLatestRequest} %{public}@ | staging-client-request was received when already performing requested operation (stale earlier request has been replied to with failure)"
- "{LoadPersistedDecideResume} %{public}@ | %{public}@ | MA_MILESTONE"
- "{LoadPersistedDecideResume} %{public}@ | available entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | candidate entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | had been determing with candidates for potential staging found (resuming determining) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | had been staging (resuming staging) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | had determined available for staging (resuming determined) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | have content staged from currently running OS (resumed to staged) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | have previously staged content now applicable to the currently running OS (migrating) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | have previously staged content when configured to always promote | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | inconsistency in staged information (purging) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | mismatched entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | no persisted entries (purging) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | no persisted indication of any pre-software-update-staging status | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | no staging was in progress / no candidates / no staged content (purging to start clean) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | persisted entry counts match staging summary counts"
- "{LoadPersistedDecideResume} %{public}@ | preserving successfully staged content"
- "{LoadPersistedDecideResume} %{public}@ | staged content from different OS (purging) | %{public}@ | %{public}@"
- "{LoadPersistedDecideResume} %{public}@ | staged entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | staging entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | staging summary differs from per-entry totals | stagingSummary:%{public}@ | entryTotals:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | unable to determine previous status for entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | unable to load entry:%{public}@"
- "{LoadPersistedDecideResume} %{public}@ | unknown representation(%ld) for entry:%{public}@"
- "{NextCandidateBeginDetermine} no candidates available for staging"
- "{ResumeJobs} | Preserved Persisted-State | ActiveJobs:%ld, KnownDescriptors:%ld | Locks:%ld, Scheduled:%ld, Staged:%ld | Set Configurations:%ld, AtomicInstances:%ld, ActiveSetDescriptors:%ld, DownloadedSetDescriptors:%ld"
- "{_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number"
- "{_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number (from string)"
- "{_MAPreferencesCopyNSArrayOfNumbersValue} invalid type for key:%@ | expecting array of numbers"
- "{_MAPreferencesCopyNSStringValue} invalid type for key:%@ | expecting string or number or boolean"
- "{_controlConvertStagedToDownloaded} %{public}@ | IMMEDIATE-PROMOTION | %{public}@ | MA_MILESTONE"
- "{_controlConvertStagedToDownloaded} %{public}@ | NO-IMMEDIATE-PROMOTION: not staged | selectorToBecomeDownloaded:%{public}@"
- "{_persistRebuildTrackingForFollowupEvent} %{public}@ | promoted descriptor count:%ld"
- "{_persistRebuildTrackingForFollowupEvent} %{public}@ | unable to determine previous status for entry:%{public}@"
- "{_persistRebuildTrackingForFollowupEvent} %{public}@ | unable to load persistedDescriptor from persisted-state for entry:%{public}@"
- "{_persistRebuildTrackingForFollowupEvent} unsupported asset representation(%d) - not adopting persisted descriptor:%@"
- "{_persistRebuildTrackingForFollowupEvent} | should have asset(s) to be promoted yet none to hand off to auto-control-manager"
- "{_trackReloadedDescriptorAvailableForStaging} %{public}@ | ignoring additional persisted entry for descriptor:%{public}@"
- "{autoAssetSetStagerJobDetermineDone} failed to locate shared AutoAssetStager"
- "{autoAssetSetStagerJobDownloadProgress} failed to locate shared AutoAssetStager"
- "{autoAssetSetStagerJobFailedToStart} failed to locate shared AutoAssetStager"
- "{garbageCollectEliminateSelector} %{public}@ | not staged | eliminateSelector:%{public}@"
- "{mostSpecificSelectorToReport} no selector reported"
- "{mostSpecificSelectorToReport} unable to create copy-of-selector (returning un-clean selector)"

```
