## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1837.2.1.0.0
-  __TEXT.__text: 0x2eafc0
+1837.40.40.0.0
+  __TEXT.__text: 0x2fb140
   __TEXT.__auth_stubs: 0x2be0
-  __TEXT.__objc_stubs: 0x22e60
-  __TEXT.__objc_methlist: 0x106ec
+  __TEXT.__objc_stubs: 0x23de0
+  __TEXT.__objc_methlist: 0x10fe4
   __TEXT.__const: 0x7ba88
-  __TEXT.__cstring: 0x3aaab
-  __TEXT.__objc_methname: 0x3eac8
-  __TEXT.__objc_classname: 0xe66
-  __TEXT.__objc_methtype: 0x403e
-  __TEXT.__oslogstring: 0x54347
-  __TEXT.__gcc_except_tab: 0xd23c
+  __TEXT.__objc_methname: 0x40a50
+  __TEXT.__objc_classname: 0xeb5
+  __TEXT.__objc_methtype: 0x4082
+  __TEXT.__cstring: 0x3cb8b
+  __TEXT.__oslogstring: 0x56d87
+  __TEXT.__gcc_except_tab: 0xd760
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x14cc
   __TEXT.__constg_swiftt: 0x18a8

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x5ee8
+  __TEXT.__unwind_info: 0x5fe8
   __TEXT.__eh_frame: 0x346c
   __DATA_CONST.__auth_got: 0x1600
   __DATA_CONST.__got: 0x748
   __DATA_CONST.__auth_ptr: 0xac8
-  __DATA_CONST.__const: 0x9b08
-  __DATA_CONST.__cfstring: 0x2d600
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__const: 0x9b38
+  __DATA_CONST.__cfstring: 0x2ea80
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9af0
-  __DATA_CONST.__objc_arraydata: 0xba0
+  __DATA_CONST.__objc_selrefs: 0x9ec0
+  __DATA_CONST.__objc_arraydata: 0xbe8
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x1020
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x154f8
+  __DATA.__objc_const: 0x16348
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x858
-  __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13fc
-  __DATA.__objc_data: 0x2b88
+  __DATA.__objc_classrefs: 0x870
+  __DATA.__objc_superrefs: 0x2f8
+  __DATA.__objc_ivar: 0x1510
+  __DATA.__objc_data: 0x2c28
   __DATA.__data: 0x2cf0
   __DATA.__bss: 0x6668
   __DATA.__common: 0x98

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 055DDD02-CEAF-384F-9D2C-DE8FCCD826E5
-  Functions: 9160
-  Symbols:   16698
-  CStrings:  23666
+  UUID: 80918C31-F5A5-3C2B-81E9-3106AA83B9D1
+  Functions: 9357
+  Symbols:   17117
+  CStrings:  24291
 
Symbols:
+ +[MADAutoAssetControlManager previousOTASituation]
+ +[MADAutoAssetControlManager stagerResumed:withSetLookupResults:performingNewOSPromotion:requiringLoadPriorToUse:]
+ +[MADAutoAssetStager clientDownloadGroups:withAlreadyDownloadedDescriptors:]
+ +[MADAutoAssetStager collectOverviewInformation]
+ +[MADAutoAssetStager controlAlteredSetConfiguration:]
+ +[MADAutoAssetStager controlSetTargetsSpecified:]
+ +[MADAutoAssetStager previousOTASituation]
+ +[MANAutoAssetControlStagerInformation previousOTASituationName:]
+ +[MANAutoAssetControlStagerInformation supportsSecureCoding]
+ +[MASAutoAssetControlStagerInformation newServerMessageClasses:]
+ +[MASAutoAssetControlStagerInformation newShimmedFromFramework:]
+ +[MASAutoAssetControlStagerInformation newShimmedFromFrameworkMessage:forKey:]
+ +[MASAutoAssetControlStagerInformation newShimmedToFramework:]
+ -[ASAssetMetadataUpdatePolicy getSystemAppURL:assetType:]
+ -[MADAutoAssetConnector _adoptAlteredMarkers:fromLocation:]
+ -[MADAutoAssetConnector currentAttemptBeginningMarkers]
+ -[MADAutoAssetConnector setCurrentAttemptBeginningMarkers:]
+ -[MADAutoAssetControlManager _alreadyDownloadedDescriptorsArray:limitingToSupportingStaging:]
+ -[MADAutoAssetControlManager _stagedNewOSPromoteAdoptSetTargets]
+ -[MADAutoAssetControlManager atomicInstanceForceUnlock:forgettingAtomicInstance:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager firstSchedulerShortTermLockContentChecks:]
+ -[MADAutoAssetControlManager handleControlClientStagerOverviewRequest:forAutoJob:]
+ -[MADAutoAssetControlManager isLocalContentValidForSetAtomicEntry:fromLocation:]
+ -[MADAutoAssetControlManager modifySetConfiguration:toEntriesFromSetTarget:]
+ -[MADAutoAssetControlManager setTargetEntries:match:]
+ -[MADAutoAssetControlManager setTargetPersistedMatchesClientSpecified:]
+ -[MADAutoAssetControlManager verifySetDescriptorIsLockable:fromLocation:notLocakableError:corruptedAtomicEntries:]
+ -[MADAutoAssetControlManagerParam clientVoucher]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withNewOSPromotion:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetControlManagerParam initWithPromoted:withSetLookupResults:withNewOSPromotion:withRequiringLoadPriorToUse:]
+ -[MADAutoAssetControlManagerParam newOSPromotion]
+ -[MADAutoAssetControlManagerParam setClientVoucher:]
+ -[MADAutoAssetJob startStagerDownloadForStaging:withAssetTargetBuildVersion:usingCachedAutoAssetCatalog:withControlInformation:]
+ -[MADAutoAssetJobParam initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:usingCachedAutoAssetCatalog:withControlInformation:]
+ -[MADAutoAssetStager _availableForStagingRemove:forTargetTrainName:withRestoreVersion:]
+ -[MADAutoAssetStager _candidatesRemove:forTargetTrainName:withRestoreVersion:]
+ -[MADAutoAssetStager _collectOverviewInformation]
+ -[MADAutoAssetStager _extendLookupByAssetTypeWithDownloadedDescriptors:limitingToSetTargets:]
+ -[MADAutoAssetStager _extendLookupByAssetTypeWithSetConfigurations:limitingToSetTargets:]
+ -[MADAutoAssetStager _logPersistedActiveTargetLookupResults:]
+ -[MADAutoAssetStager _logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:withTargetOTASituation:message:]
+ -[MADAutoAssetStager _lookupCacheRemoveResult:forTargetTrainName:withRestoreVersion:]
+ -[MADAutoAssetStager _persistAllTargetLookupResultsOTASituation:fromLocation:]
+ -[MADAutoAssetStager _persistEraseLookupResults:forTargetTrainName:forTargetRestoreVersion:]
+ -[MADAutoAssetStager _persistErasePreviousOTASituation:]
+ -[MADAutoAssetStager _persistLastStagingFrom:]
+ -[MADAutoAssetStager _persistPreviousOTASituationIfTargetMatchesCurrentOS:settingStartupSituation:]
+ -[MADAutoAssetStager _persistStoredTargetWithOTASituation:]
+ -[MADAutoAssetStager _persistTargetOTASituation:fromLocation:]
+ -[MADAutoAssetStager _persistTargetOTASituationForFollowup:fromLocation:]
+ -[MADAutoAssetStager _recordOperationForStagedAttributes:required:]
+ -[MADAutoAssetStager _removeAllStagedContent:]
+ -[MADAutoAssetStager _stagedAllDesiredForCurrentTarget]
+ -[MADAutoAssetStager action_AlteredDecideSameSetConfiguration:error:]
+ -[MADAutoAssetStager action_AlteredInvalAllAvailable:error:]
+ -[MADAutoAssetStager action_AlteredInvalAllAvailableCancelActiveJob:error:]
+ -[MADAutoAssetStager action_ClientAcceptEraseCancelActiveJob:error:]
+ -[MADAutoAssetStager action_ReplyNoCandidatesEraseAll:error:]
+ -[MADAutoAssetStager action_ReplyNothingStagedEraseAll:error:]
+ -[MADAutoAssetStager action_SetTargetDecideSameTarget:error:]
+ -[MADAutoAssetStager action_SetTargetInvalAllAvailable:error:]
+ -[MADAutoAssetStager action_SetTargetInvalAllAvailableCancelActiveJob:error:]
+ -[MADAutoAssetStager action_UpdateStagedSituation:error:]
+ -[MADAutoAssetStager dedupAvailableForStaging:dedupingAssetDescriptors:removingAlreadyDownloaded:ofContainerName:]
+ -[MADAutoAssetStager isAnyAvailableForStagingByGroup:withAlreadyDownloadedDescriptors:targetHadBeenDetermined:]
+ -[MADAutoAssetStager loadPersistedPreviousOTASituation]
+ -[MADAutoAssetStager loadPersistedTargetLookupResults:]
+ -[MADAutoAssetStager loadedPersistedTargetLookupResults]
+ -[MADAutoAssetStager setLoadPersistedPreviousOTASituation:]
+ -[MADAutoAssetStager setLoadedPersistedTargetLookupResults:]
+ -[MADAutoAssetStager setStartupAssetTargetRestoreVersion:]
+ -[MADAutoAssetStager setStartupAssetTargetTrainName:]
+ -[MADAutoAssetStager setStartupPreviousOTASituation:]
+ -[MADAutoAssetStager setStartupStagedNoContent:]
+ -[MADAutoAssetStager setStoredTargetWithOTASituation:]
+ -[MADAutoAssetStager startupAssetTargetRestoreVersion]
+ -[MADAutoAssetStager startupAssetTargetTrainName]
+ -[MADAutoAssetStager startupPreviousOTASituation]
+ -[MADAutoAssetStager startupStagedNoContent]
+ -[MADAutoAssetStager storedTargetWithOTASituation]
+ -[MADAutoAssetStager targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:withTargetOTASituation:]
+ -[MADAutoAssetStagerParam entriesWhenTargeting]
+ -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withEntriesWhenTargeting:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:]
+ -[MADAutoAssetStagerParam initWithSetTargets:]
+ -[MADAutoAssetStagerParam initWithStagingClientRequest:withAlreadyDownloadedDescriptors:]
+ -[MADAutoSetTarget firstEntryAssetType]
+ -[MADAutoSetTarget fullName]
+ -[MANAutoAssetControlStagerInformation .cxx_destruct]
+ -[MANAutoAssetControlStagerInformation activeTargetAvailableForStagingOptionalCount]
+ -[MANAutoAssetControlStagerInformation activeTargetAvailableForStagingRequiredCount]
+ -[MANAutoAssetControlStagerInformation activeTargetCandidateSetConfigurationsOptionalCount]
+ -[MANAutoAssetControlStagerInformation activeTargetCandidateSetConfigurationsRequiredCount]
+ -[MANAutoAssetControlStagerInformation activeTargetCandidatesForStagingOptionalCount]
+ -[MANAutoAssetControlStagerInformation activeTargetCandidatesForStagingRequiredCount]
+ -[MANAutoAssetControlStagerInformation activeTargetOTASituation]
+ -[MANAutoAssetControlStagerInformation alwaysPromoteStagedAssets]
+ -[MANAutoAssetControlStagerInformation assetTargetBuildVersion]
+ -[MANAutoAssetControlStagerInformation assetTargetOSVersion]
+ -[MANAutoAssetControlStagerInformation assetTargetRestoreVersion]
+ -[MANAutoAssetControlStagerInformation assetTargetTrainName]
+ -[MANAutoAssetControlStagerInformation availableForStagingCount]
+ -[MANAutoAssetControlStagerInformation awaitingStagingAttemptCount]
+ -[MANAutoAssetControlStagerInformation baseForStagingDescriptorsCount]
+ -[MANAutoAssetControlStagerInformation candidateSetConfigurationsCount]
+ -[MANAutoAssetControlStagerInformation candidatesForStagingCount]
+ -[MANAutoAssetControlStagerInformation currentStagedLastWrittenBytes]
+ -[MANAutoAssetControlStagerInformation currentStagedRemainingBytes]
+ -[MANAutoAssetControlStagerInformation description]
+ -[MANAutoAssetControlStagerInformation determiningBySelectorCount]
+ -[MANAutoAssetControlStagerInformation eliminationSelectorsAcknowledgedCount]
+ -[MANAutoAssetControlStagerInformation eliminationSelectorsCount]
+ -[MANAutoAssetControlStagerInformation eliminationSetConfigurationCurrentJob]
+ -[MANAutoAssetControlStagerInformation encodeWithCoder:]
+ -[MANAutoAssetControlStagerInformation initWithCoder:]
+ -[MANAutoAssetControlStagerInformation init]
+ -[MANAutoAssetControlStagerInformation loadPersistedPostponed]
+ -[MANAutoAssetControlStagerInformation optionalAssetSizeAllowed]
+ -[MANAutoAssetControlStagerInformation otherTargetAvailableForStagingOptionalCount]
+ -[MANAutoAssetControlStagerInformation otherTargetAvailableForStagingRequiredCount]
+ -[MANAutoAssetControlStagerInformation otherTargetCandidateSetConfigurationsOptionalCount]
+ -[MANAutoAssetControlStagerInformation otherTargetCandidateSetConfigurationsRequiredCount]
+ -[MANAutoAssetControlStagerInformation otherTargetCandidatesForStagingOptionalCount]
+ -[MANAutoAssetControlStagerInformation otherTargetCandidatesForStagingRequiredCount]
+ -[MANAutoAssetControlStagerInformation otherTargetName]
+ -[MANAutoAssetControlStagerInformation otherTargetOTASituation]
+ -[MANAutoAssetControlStagerInformation overallStagedDownloadedSoFarBytes]
+ -[MANAutoAssetControlStagerInformation overallStagedTotalExpectedBytes]
+ -[MANAutoAssetControlStagerInformation persistedAvailableForStagingByTargetCount]
+ -[MANAutoAssetControlStagerInformation persistedStateCount]
+ -[MANAutoAssetControlStagerInformation persistedTargetLookupResultsCount]
+ -[MANAutoAssetControlStagerInformation scheduledJobsCount]
+ -[MANAutoAssetControlStagerInformation setActiveTargetAvailableForStagingOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetAvailableForStagingRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetCandidateSetConfigurationsOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetCandidateSetConfigurationsRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetCandidatesForStagingOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetCandidatesForStagingRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setActiveTargetOTASituation:]
+ -[MANAutoAssetControlStagerInformation setAlwaysPromoteStagedAssets:]
+ -[MANAutoAssetControlStagerInformation setAssetTargetBuildVersion:]
+ -[MANAutoAssetControlStagerInformation setAssetTargetOSVersion:]
+ -[MANAutoAssetControlStagerInformation setAssetTargetRestoreVersion:]
+ -[MANAutoAssetControlStagerInformation setAssetTargetTrainName:]
+ -[MANAutoAssetControlStagerInformation setAvailableForStagingCount:]
+ -[MANAutoAssetControlStagerInformation setAwaitingStagingAttemptCount:]
+ -[MANAutoAssetControlStagerInformation setBaseForStagingDescriptorsCount:]
+ -[MANAutoAssetControlStagerInformation setCandidateSetConfigurationsCount:]
+ -[MANAutoAssetControlStagerInformation setCandidatesForStagingCount:]
+ -[MANAutoAssetControlStagerInformation setConfigurationsCount]
+ -[MANAutoAssetControlStagerInformation setCurrentStagedLastWrittenBytes:]
+ -[MANAutoAssetControlStagerInformation setCurrentStagedRemainingBytes:]
+ -[MANAutoAssetControlStagerInformation setDeterminingBySelectorCount:]
+ -[MANAutoAssetControlStagerInformation setEliminationSelectorsAcknowledgedCount:]
+ -[MANAutoAssetControlStagerInformation setEliminationSelectorsCount:]
+ -[MANAutoAssetControlStagerInformation setEliminationSetConfigurationCurrentJob:]
+ -[MANAutoAssetControlStagerInformation setLoadPersistedPostponed:]
+ -[MANAutoAssetControlStagerInformation setLookupResultsCount]
+ -[MANAutoAssetControlStagerInformation setOptionalAssetSizeAllowed:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetAvailableForStagingOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetAvailableForStagingRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetCandidateSetConfigurationsOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetCandidateSetConfigurationsRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetCandidatesForStagingOptionalCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetCandidatesForStagingRequiredCount:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetName:]
+ -[MANAutoAssetControlStagerInformation setOtherTargetOTASituation:]
+ -[MANAutoAssetControlStagerInformation setOverallStagedDownloadedSoFarBytes:]
+ -[MANAutoAssetControlStagerInformation setOverallStagedTotalExpectedBytes:]
+ -[MANAutoAssetControlStagerInformation setPersistedAvailableForStagingByTargetCount:]
+ -[MANAutoAssetControlStagerInformation setPersistedStateCount:]
+ -[MANAutoAssetControlStagerInformation setPersistedTargetLookupResultsCount:]
+ -[MANAutoAssetControlStagerInformation setScheduledJobsCount:]
+ -[MANAutoAssetControlStagerInformation setSetConfigurationsCount:]
+ -[MANAutoAssetControlStagerInformation setSetLookupResultsCount:]
+ -[MANAutoAssetControlStagerInformation setSetTargetsCount:]
+ -[MANAutoAssetControlStagerInformation setStagingClientDetermineRequestsCount:]
+ -[MANAutoAssetControlStagerInformation setStagingClientDownloadRequestActive:]
+ -[MANAutoAssetControlStagerInformation setStagingClientName:]
+ -[MANAutoAssetControlStagerInformation setStagingClientRequestActive:]
+ -[MANAutoAssetControlStagerInformation setStagingFromBuildVersion:]
+ -[MANAutoAssetControlStagerInformation setStagingFromOSVersion:]
+ -[MANAutoAssetControlStagerInformation setStartupActivelyStagingAssetCount:]
+ -[MANAutoAssetControlStagerInformation setStartupAssetTargetBuildVersion:]
+ -[MANAutoAssetControlStagerInformation setStartupAssetTargetOSVersion:]
+ -[MANAutoAssetControlStagerInformation setStartupAwaitingStagingAssetCount:]
+ -[MANAutoAssetControlStagerInformation setStartupCandidateAssetCount:]
+ -[MANAutoAssetControlStagerInformation setStartupDeterminedAvailableAssetCount:]
+ -[MANAutoAssetControlStagerInformation setStartupLastStagingFromBuildVersion:]
+ -[MANAutoAssetControlStagerInformation setStartupLastStagingFromOSVersion:]
+ -[MANAutoAssetControlStagerInformation setStartupPreviousOTASituation:]
+ -[MANAutoAssetControlStagerInformation setStartupStagedAssetCount:]
+ -[MANAutoAssetControlStagerInformation setStartupStagedAssetTotalContentBytes:]
+ -[MANAutoAssetControlStagerInformation setSuccessfullyStagedCount:]
+ -[MANAutoAssetControlStagerInformation setTargetsCount]
+ -[MANAutoAssetControlStagerInformation stagingClientDetermineRequestsCount]
+ -[MANAutoAssetControlStagerInformation stagingClientDownloadRequestActive]
+ -[MANAutoAssetControlStagerInformation stagingClientName]
+ -[MANAutoAssetControlStagerInformation stagingClientRequestActive]
+ -[MANAutoAssetControlStagerInformation stagingFromBuildVersion]
+ -[MANAutoAssetControlStagerInformation stagingFromOSVersion]
+ -[MANAutoAssetControlStagerInformation startupActivelyStagingAssetCount]
+ -[MANAutoAssetControlStagerInformation startupAssetTargetBuildVersion]
+ -[MANAutoAssetControlStagerInformation startupAssetTargetOSVersion]
+ -[MANAutoAssetControlStagerInformation startupAwaitingStagingAssetCount]
+ -[MANAutoAssetControlStagerInformation startupCandidateAssetCount]
+ -[MANAutoAssetControlStagerInformation startupDeterminedAvailableAssetCount]
+ -[MANAutoAssetControlStagerInformation startupLastStagingFromBuildVersion]
+ -[MANAutoAssetControlStagerInformation startupLastStagingFromOSVersion]
+ -[MANAutoAssetControlStagerInformation startupPreviousOTASituation]
+ -[MANAutoAssetControlStagerInformation startupStagedAssetCount]
+ -[MANAutoAssetControlStagerInformation startupStagedAssetTotalContentBytes]
+ -[MANAutoAssetControlStagerInformation successfullyStagedCount]
+ -[MANAutoAssetControlStagerInformation summary]
+ -[MobileAssetHealthReport getPreviousOTAStatus]
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table175
+ GCC_except_table193
+ GCC_except_table198
+ GCC_except_table204
+ GCC_except_table317
+ GCC_except_table330
+ GCC_except_table342
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table354
+ GCC_except_table359
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table366
+ GCC_except_table370
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table427
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table589
+ GCC_except_table626
+ GCC_except_table628
+ GCC_except_table634
+ GCC_except_table636
+ GCC_except_table651
+ GCC_except_table680
+ GCC_except_table786
+ GCC_except_table787
+ GCC_except_table788
+ GCC_except_table789
+ GCC_except_table792
+ OBJC_IVAR_$_MADAutoAssetConnector._currentAttemptBeginningMarkers
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._clientVoucher
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._newOSPromotion
+ OBJC_IVAR_$_MADAutoAssetStager._loadPersistedPreviousOTASituation
+ OBJC_IVAR_$_MADAutoAssetStager._loadedPersistedTargetLookupResults
+ OBJC_IVAR_$_MADAutoAssetStager._startupAssetTargetRestoreVersion
+ OBJC_IVAR_$_MADAutoAssetStager._startupAssetTargetTrainName
+ OBJC_IVAR_$_MADAutoAssetStager._startupPreviousOTASituation
+ OBJC_IVAR_$_MADAutoAssetStager._startupStagedNoContent
+ OBJC_IVAR_$_MADAutoAssetStager._storedTargetWithOTASituation
+ OBJC_IVAR_$_MADAutoAssetStagerParam._entriesWhenTargeting
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetAvailableForStagingOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetAvailableForStagingRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetCandidateSetConfigurationsOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetCandidateSetConfigurationsRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetCandidatesForStagingOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetCandidatesForStagingRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._activeTargetOTASituation
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._alwaysPromoteStagedAssets
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._assetTargetBuildVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._assetTargetOSVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._assetTargetRestoreVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._assetTargetTrainName
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._availableForStagingCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._awaitingStagingAttemptCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._baseForStagingDescriptorsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._candidateSetConfigurationsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._candidatesForStagingCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._currentStagedLastWrittenBytes
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._currentStagedRemainingBytes
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._determiningBySelectorCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._eliminationSelectorsAcknowledgedCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._eliminationSelectorsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._eliminationSetConfigurationCurrentJob
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._loadPersistedPostponed
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._optionalAssetSizeAllowed
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetAvailableForStagingOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetAvailableForStagingRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetCandidateSetConfigurationsOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetCandidateSetConfigurationsRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetCandidatesForStagingOptionalCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetCandidatesForStagingRequiredCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetName
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._otherTargetOTASituation
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._overallStagedDownloadedSoFarBytes
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._overallStagedTotalExpectedBytes
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._persistedAvailableForStagingByTargetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._persistedStateCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._persistedTargetLookupResultsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._scheduledJobsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._setConfigurationsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._setLookupResultsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._setTargetsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingClientDetermineRequestsCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingClientDownloadRequestActive
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingClientName
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingClientRequestActive
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingFromBuildVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._stagingFromOSVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupActivelyStagingAssetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupAssetTargetBuildVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupAssetTargetOSVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupAwaitingStagingAssetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupCandidateAssetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupDeterminedAvailableAssetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupLastStagingFromBuildVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupLastStagingFromOSVersion
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupPreviousOTASituation
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupStagedAssetCount
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._startupStagedAssetTotalContentBytes
+ OBJC_IVAR_$_MANAutoAssetControlStagerInformation._successfullyStagedCount
+ _OBJC_CLASS_$_MAAutoAssetControlStagerInformation
+ _OBJC_CLASS_$_MANAutoAssetControlStagerInformation
+ _OBJC_CLASS_$_MASAutoAssetControlStagerInformation
+ _OBJC_METACLASS_$_MANAutoAssetControlStagerInformation
+ _OBJC_METACLASS_$_MASAutoAssetControlStagerInformation
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2206
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2380
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2313
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2325
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2361
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1783
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1219
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1266
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2260
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2261
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1932
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1933
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1939
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1893
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1318
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.382
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.400
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.406
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2378
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2577
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2578
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1197
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3448
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3449
+ __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.407
+ __OBJC_$_CLASS_METHODS_MANAutoAssetControlStagerInformation
+ __OBJC_$_CLASS_METHODS_MASAutoAssetControlStagerInformation
+ __OBJC_$_CLASS_PROP_LIST_MANAutoAssetControlStagerInformation
+ __OBJC_$_INSTANCE_METHODS_MANAutoAssetControlStagerInformation
+ __OBJC_$_INSTANCE_VARIABLES_MANAutoAssetControlStagerInformation
+ __OBJC_$_PROP_LIST_MANAutoAssetControlStagerInformation
+ __OBJC_CLASS_PROTOCOLS_$_MANAutoAssetControlStagerInformation
+ __OBJC_CLASS_RO_$_MANAutoAssetControlStagerInformation
+ __OBJC_CLASS_RO_$_MASAutoAssetControlStagerInformation
+ __OBJC_METACLASS_RO_$_MANAutoAssetControlStagerInformation
+ __OBJC_METACLASS_RO_$_MASAutoAssetControlStagerInformation
+ ___42+[MADAutoAssetStager previousOTASituation]_block_invoke
+ ___48+[MADAutoAssetStager collectOverviewInformation]_block_invoke
+ ___50+[MADAutoAssetControlManager previousOTASituation]_block_invoke
+ ___58-[MADAutoAssetControlManager firstSchedulerCrosscheckTrim]_block_invoke_4
+ ___72-[MADAutoAssetStager _extendSummaryWithDeterminedAssets:basedOnControl:]_block_invoke
+ ___72-[MADAutoAssetStager _extendSummaryWithDeterminedAssets:basedOnControl:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r80l8r88l8
+ __block_literal_global.1216
+ __block_literal_global.1218
+ __block_literal_global.1421
+ __block_literal_global.1426
+ __block_literal_global.1448
+ __block_literal_global.1635
+ __block_literal_global.1680
+ __block_literal_global.1786
+ __block_literal_global.1791
+ __block_literal_global.1796
+ __block_literal_global.1799
+ __block_literal_global.1835
+ __block_literal_global.1861
+ __block_literal_global.2113
+ __block_literal_global.2135
+ __block_literal_global.2297
+ __block_literal_global.2308
+ __block_literal_global.2316
+ __block_literal_global.2324
+ __block_literal_global.2332
+ __block_literal_global.2340
+ __block_literal_global.2348
+ __block_literal_global.2356
+ __block_literal_global.2364
+ __block_literal_global.2425
+ __block_literal_global.2526
+ __block_literal_global.2836
+ __block_literal_global.2839
+ __block_literal_global.4090
+ __block_literal_global.417
+ __block_literal_global.5133
+ _isSystemAppType
+ _markPathPurgeable
+ _objc_msgSend$_adoptAlteredMarkers:fromLocation:
+ _objc_msgSend$_alreadyDownloadedDescriptorsArray:limitingToSupportingStaging:
+ _objc_msgSend$_availableForStagingRemove:forTargetTrainName:withRestoreVersion:
+ _objc_msgSend$_candidatesRemove:forTargetTrainName:withRestoreVersion:
+ _objc_msgSend$_collectOverviewInformation
+ _objc_msgSend$_extendLookupByAssetTypeWithDownloadedDescriptors:limitingToSetTargets:
+ _objc_msgSend$_extendLookupByAssetTypeWithSetConfigurations:limitingToSetTargets:
+ _objc_msgSend$_logPersistedActiveTargetLookupResults:
+ _objc_msgSend$_logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:withTargetOTASituation:message:
+ _objc_msgSend$_lookupCacheRemoveResult:forTargetTrainName:withRestoreVersion:
+ _objc_msgSend$_persistAllTargetLookupResultsOTASituation:fromLocation:
+ _objc_msgSend$_persistEraseLookupResults:forTargetTrainName:forTargetRestoreVersion:
+ _objc_msgSend$_persistErasePreviousOTASituation:
+ _objc_msgSend$_persistLastStagingFrom:
+ _objc_msgSend$_persistPreviousOTASituationIfTargetMatchesCurrentOS:settingStartupSituation:
+ _objc_msgSend$_persistStoredTargetWithOTASituation:
+ _objc_msgSend$_persistTargetOTASituation:fromLocation:
+ _objc_msgSend$_persistTargetOTASituationForFollowup:fromLocation:
+ _objc_msgSend$_recordOperationForStagedAttributes:required:
+ _objc_msgSend$_removeAllStagedContent:
+ _objc_msgSend$_stagedAllDesiredForCurrentTarget
+ _objc_msgSend$_stagedNewOSPromoteAdoptSetTargets
+ _objc_msgSend$action_AlteredDecideSameSetConfiguration:error:
+ _objc_msgSend$action_AlteredInvalAllAvailable:error:
+ _objc_msgSend$action_AlteredInvalAllAvailableCancelActiveJob:error:
+ _objc_msgSend$action_ClientAcceptEraseCancelActiveJob:error:
+ _objc_msgSend$action_ReplyNoCandidatesEraseAll:error:
+ _objc_msgSend$action_ReplyNothingStagedEraseAll:error:
+ _objc_msgSend$action_SetTargetDecideSameTarget:error:
+ _objc_msgSend$action_SetTargetInvalAllAvailable:error:
+ _objc_msgSend$action_SetTargetInvalAllAvailableCancelActiveJob:error:
+ _objc_msgSend$action_UpdateStagedSituation:error:
+ _objc_msgSend$activeTargetAvailableForStagingOptionalCount
+ _objc_msgSend$activeTargetAvailableForStagingRequiredCount
+ _objc_msgSend$activeTargetCandidateSetConfigurationsOptionalCount
+ _objc_msgSend$activeTargetCandidateSetConfigurationsRequiredCount
+ _objc_msgSend$activeTargetCandidatesForStagingOptionalCount
+ _objc_msgSend$activeTargetCandidatesForStagingRequiredCount
+ _objc_msgSend$activeTargetOTASituation
+ _objc_msgSend$atomicInstanceForceUnlock:forgettingAtomicInstance:historyOperationAI:historyOperationSD:
+ _objc_msgSend$availableForStagingCount
+ _objc_msgSend$awaitingStagingAttemptCount
+ _objc_msgSend$baseForStagingDescriptorsCount
+ _objc_msgSend$candidateSetConfigurationsCount
+ _objc_msgSend$candidatesForStagingCount
+ _objc_msgSend$clientDownloadGroups:withAlreadyDownloadedDescriptors:
+ _objc_msgSend$clientVoucher
+ _objc_msgSend$collectOverviewInformation
+ _objc_msgSend$controlAlteredSetConfiguration:
+ _objc_msgSend$controlSetTargetsSpecified:
+ _objc_msgSend$currentAttemptBeginningMarkers
+ _objc_msgSend$dedupAvailableForStaging:dedupingAssetDescriptors:removingAlreadyDownloaded:ofContainerName:
+ _objc_msgSend$determiningBySelectorCount
+ _objc_msgSend$eliminationSelectorsAcknowledgedCount
+ _objc_msgSend$eliminationSelectorsCount
+ _objc_msgSend$firstSchedulerShortTermLockContentChecks:
+ _objc_msgSend$fullName
+ _objc_msgSend$getPreviousOTAStatus
+ _objc_msgSend$getSystemAppURL:assetType:
+ _objc_msgSend$handleControlClientStagerOverviewRequest:forAutoJob:
+ _objc_msgSend$initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:usingCachedAutoAssetCatalog:withControlInformation:
+ _objc_msgSend$initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withNewOSPromotion:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withEntriesWhenTargeting:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:
+ _objc_msgSend$initWithPromoted:withSetLookupResults:withNewOSPromotion:withRequiringLoadPriorToUse:
+ _objc_msgSend$initWithSetTargets:
+ _objc_msgSend$initWithStagingClientRequest:withAlreadyDownloadedDescriptors:
+ _objc_msgSend$isAnyAvailableForStagingByGroup:withAlreadyDownloadedDescriptors:targetHadBeenDetermined:
+ _objc_msgSend$isLocalContentValidForSetAtomicEntry:fromLocation:
+ _objc_msgSend$loadPersistedPreviousOTASituation
+ _objc_msgSend$loadPersistedTargetLookupResults:
+ _objc_msgSend$loadedPersistedTargetLookupResults
+ _objc_msgSend$modifySetConfiguration:toEntriesFromSetTarget:
+ _objc_msgSend$newOSPromotion
+ _objc_msgSend$otherTargetAvailableForStagingOptionalCount
+ _objc_msgSend$otherTargetAvailableForStagingRequiredCount
+ _objc_msgSend$otherTargetCandidateSetConfigurationsOptionalCount
+ _objc_msgSend$otherTargetCandidateSetConfigurationsRequiredCount
+ _objc_msgSend$otherTargetCandidatesForStagingOptionalCount
+ _objc_msgSend$otherTargetCandidatesForStagingRequiredCount
+ _objc_msgSend$otherTargetName
+ _objc_msgSend$otherTargetOTASituation
+ _objc_msgSend$persistedAvailableForStagingByTargetCount
+ _objc_msgSend$persistedStateCount
+ _objc_msgSend$persistedTargetLookupResultsCount
+ _objc_msgSend$previousOTASituation
+ _objc_msgSend$previousOTASituationName:
+ _objc_msgSend$scheduledJobsCount
+ _objc_msgSend$setActiveTargetAvailableForStagingOptionalCount:
+ _objc_msgSend$setActiveTargetAvailableForStagingRequiredCount:
+ _objc_msgSend$setActiveTargetCandidateSetConfigurationsOptionalCount:
+ _objc_msgSend$setActiveTargetCandidateSetConfigurationsRequiredCount:
+ _objc_msgSend$setActiveTargetCandidatesForStagingOptionalCount:
+ _objc_msgSend$setActiveTargetCandidatesForStagingRequiredCount:
+ _objc_msgSend$setActiveTargetOTASituation:
+ _objc_msgSend$setAlwaysPromoteStagedAssets:
+ _objc_msgSend$setAvailableForStagingCount:
+ _objc_msgSend$setAwaitingStagingAttemptCount:
+ _objc_msgSend$setBaseForStagingDescriptorsCount:
+ _objc_msgSend$setCandidateSetConfigurationsCount:
+ _objc_msgSend$setCandidatesForStagingCount:
+ _objc_msgSend$setConfigurationsCount
+ _objc_msgSend$setCurrentAttemptBeginningMarkers:
+ _objc_msgSend$setDeterminingBySelectorCount:
+ _objc_msgSend$setEliminationSelectorsAcknowledgedCount:
+ _objc_msgSend$setEliminationSelectorsCount:
+ _objc_msgSend$setLoadPersistedPreviousOTASituation:
+ _objc_msgSend$setLoadedPersistedTargetLookupResults:
+ _objc_msgSend$setLookupResultsByAssetSelector:
+ _objc_msgSend$setLookupResultsBySetConfiguration:
+ _objc_msgSend$setLookupResultsCount
+ _objc_msgSend$setOtherTargetAvailableForStagingOptionalCount:
+ _objc_msgSend$setOtherTargetAvailableForStagingRequiredCount:
+ _objc_msgSend$setOtherTargetCandidateSetConfigurationsOptionalCount:
+ _objc_msgSend$setOtherTargetCandidateSetConfigurationsRequiredCount:
+ _objc_msgSend$setOtherTargetCandidatesForStagingOptionalCount:
+ _objc_msgSend$setOtherTargetCandidatesForStagingRequiredCount:
+ _objc_msgSend$setOtherTargetName:
+ _objc_msgSend$setOtherTargetOTASituation:
+ _objc_msgSend$setPersistedAvailableForStagingByTargetCount:
+ _objc_msgSend$setPersistedStateCount:
+ _objc_msgSend$setPersistedTargetLookupResultsCount:
+ _objc_msgSend$setScheduledJobsCount:
+ _objc_msgSend$setSetConfigurationsCount:
+ _objc_msgSend$setSetLookupResultsCount:
+ _objc_msgSend$setSetTargetsCount:
+ _objc_msgSend$setStagingClientDetermineRequestsCount:
+ _objc_msgSend$setStagingClientDownloadRequestActive:
+ _objc_msgSend$setStagingClientRequestActive:
+ _objc_msgSend$setStartupAssetTargetRestoreVersion:
+ _objc_msgSend$setStartupAssetTargetTrainName:
+ _objc_msgSend$setStartupPreviousOTASituation:
+ _objc_msgSend$setStartupStagedNoContent:
+ _objc_msgSend$setStoredTargetWithOTASituation:
+ _objc_msgSend$setSuccessfullyStagedCount:
+ _objc_msgSend$setTargetEntries:match:
+ _objc_msgSend$setTargetPersistedMatchesClientSpecified:
+ _objc_msgSend$setTargetsCount
+ _objc_msgSend$stagerResumed:withSetLookupResults:performingNewOSPromotion:requiringLoadPriorToUse:
+ _objc_msgSend$stagingClientDetermineRequestsCount
+ _objc_msgSend$stagingClientDownloadRequestActive
+ _objc_msgSend$stagingClientRequestActive
+ _objc_msgSend$startStagerDownloadForStaging:withAssetTargetBuildVersion:usingCachedAutoAssetCatalog:withControlInformation:
+ _objc_msgSend$startupAssetTargetRestoreVersion
+ _objc_msgSend$startupAssetTargetTrainName
+ _objc_msgSend$startupPreviousOTASituation
+ _objc_msgSend$startupStagedNoContent
+ _objc_msgSend$storedTargetWithOTASituation
+ _objc_msgSend$successfullyStagedCount
+ _objc_msgSend$targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:withTargetOTASituation:
+ _objc_msgSend$verifySetDescriptorIsLockable:fromLocation:notLocakableError:corruptedAtomicEntries:
+ _renameWithExtThenRemoveExposeError
- +[MADAutoAssetControlManager stagerResumed:withSetLookupResults:requiringLoadPriorToUse:]
- +[MADAutoAssetStager clientDownloadGroups:]
- -[ASAssetMetadataUpdatePolicy getSystemAppURL:]
- -[MADAutoAssetConnector _adoptAlteredMarkers:]
- -[MADAutoAssetControlManager verifySetDescriptorIsLockable:fromLocation:notLocakableError:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetControlManagerParam initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:]
- -[MADAutoAssetJob startStagerDownloadForStaging:withAssetTargetBuildVersion:withControlInformation:]
- -[MADAutoAssetJobParam initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:]
- -[MADAutoAssetLookupCache lookupResultsByAssetSelectorForStaging]
- -[MADAutoAssetLookupCache lookupResultsBySetConfigurationForStaging]
- -[MADAutoAssetLookupCache setLookupResultsByAssetSelectorForStaging:]
- -[MADAutoAssetLookupCache setLookupResultsBySetConfigurationForStaging:]
- -[MADAutoAssetStager _extendLookupByAssetTypeWithDownloadedDescriptors:]
- -[MADAutoAssetStager _extendLookupByAssetTypeWithSetConfigurations:]
- -[MADAutoAssetStager _logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:message:]
- -[MADAutoAssetStager _persistLastStagingFrom]
- -[MADAutoAssetStager _removeAllStagedContent]
- -[MADAutoAssetStager action_ClientDecideGroupTargetAvailablePurge:error:]
- -[MADAutoAssetStager action_DecideEmptyHaveAvailable:error:]
- -[MADAutoAssetStager action_ReplyNoCandidatesRemoveAllReplyErased:error:]
- -[MADAutoAssetStager dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:]
- -[MADAutoAssetStager isAnyAvailableForStagingByGroup:]
- -[MADAutoAssetStager targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:]
- -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:]
- GCC_except_table179
- GCC_except_table202
- GCC_except_table315
- GCC_except_table324
- GCC_except_table331
- GCC_except_table332
- GCC_except_table345
- GCC_except_table351
- GCC_except_table355
- GCC_except_table356
- GCC_except_table357
- GCC_except_table363
- GCC_except_table364
- GCC_except_table368
- GCC_except_table369
- GCC_except_table373
- GCC_except_table423
- GCC_except_table429
- GCC_except_table430
- GCC_except_table431
- GCC_except_table432
- GCC_except_table518
- GCC_except_table520
- GCC_except_table580
- GCC_except_table615
- GCC_except_table617
- GCC_except_table623
- GCC_except_table625
- GCC_except_table639
- GCC_except_table668
- GCC_except_table774
- GCC_except_table775
- GCC_except_table776
- GCC_except_table777
- GCC_except_table780
- OBJC_IVAR_$_MADAutoAssetLookupCache._lookupResultsByAssetSelectorForStaging
- OBJC_IVAR_$_MADAutoAssetLookupCache._lookupResultsBySetConfigurationForStaging
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2203
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2377
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2310
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2322
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2358
- __37-[DownloadManager startDownloadTimer]_block_invoke.1780
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1195
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1242
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2257
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2258
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1929
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1930
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1936
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1890
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1294
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.379
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.397
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.403
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2371
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2570
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2571
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1190
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3438
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3439
- __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.404
- ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80r88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r80l8r88l8
- __block_literal_global.1192
- __block_literal_global.1194
- __block_literal_global.1344
- __block_literal_global.1415
- __block_literal_global.1420
- __block_literal_global.1442
- __block_literal_global.1632
- __block_literal_global.1677
- __block_literal_global.1729
- __block_literal_global.1734
- __block_literal_global.1739
- __block_literal_global.1742
- __block_literal_global.1773
- __block_literal_global.1797
- __block_literal_global.2110
- __block_literal_global.2132
- __block_literal_global.2290
- __block_literal_global.2301
- __block_literal_global.2309
- __block_literal_global.2317
- __block_literal_global.2325
- __block_literal_global.2333
- __block_literal_global.2341
- __block_literal_global.2349
- __block_literal_global.2357
- __block_literal_global.2422
- __block_literal_global.2424
- __block_literal_global.2830
- __block_literal_global.2833
- __block_literal_global.4068
- __block_literal_global.414
- __block_literal_global.5111
- _objc_msgSend$_adoptAlteredMarkers:
- _objc_msgSend$_extendLookupByAssetTypeWithDownloadedDescriptors:
- _objc_msgSend$_extendLookupByAssetTypeWithSetConfigurations:
- _objc_msgSend$_logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:message:
- _objc_msgSend$_persistLastStagingFrom
- _objc_msgSend$_removeAllStagedContent
- _objc_msgSend$_setTargetForAssetType:
- _objc_msgSend$action_ClientDecideGroupTargetAvailablePurge:error:
- _objc_msgSend$action_DecideEmptyHaveAvailable:error:
- _objc_msgSend$action_ReplyNoCandidatesRemoveAllReplyErased:error:
- _objc_msgSend$clientDownloadGroups:
- _objc_msgSend$dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:
- _objc_msgSend$getSystemAppURL:
- _objc_msgSend$initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:
- _objc_msgSend$initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:
- _objc_msgSend$initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:
- _objc_msgSend$isAnyAvailableForStagingByGroup:
- _objc_msgSend$lookupResultsByAssetSelectorForStaging
- _objc_msgSend$lookupResultsBySetConfigurationForStaging
- _objc_msgSend$persistDate:forKey:
- _objc_msgSend$purgeAlreadyStagedNotApplicableForRequiredByTarget:andNotApplicableForOptionalByTarget:
- _objc_msgSend$stagerResumed:withSetLookupResults:requiringLoadPriorToUse:
- _objc_msgSend$startStagerDownloadForStaging:withAssetTargetBuildVersion:withControlInformation:
- _objc_msgSend$targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:
- _objc_msgSend$verifySetDescriptorIsLockable:fromLocation:notLocakableError:
CStrings:
+ "\n#_%{public}@:%{public}@ (%ld of %ld) [%{public}@] | situation:%{public}@ | %{public}@"
+ "%@ | auto-asset catalog for wrong assetType | catalog:%@, expecting:%@"
+ "%@ | auto-asset catalog without required fields | catalogAssetType:%@, catalogAssets:%@"
+ "%@ | successful catalog download yet no assets in catalog | have installed asset-version:%@ | REVOKED"
+ "%@ | {ReportCatalogDecideFound} auto-asset metadata considered invalid | %@"
+ "%@ | {ReportCatalogDecideFound} auto-asset patch and full entries for different versions | patch:%@, full:%@"
+ "%@ | {ReportCatalogDecideFound} expecting catalog provided by auto-asset-stager yet no catalog provided"
+ "%@ | {ReportCatalogDecideFound} set-job without set-configuration"
+ "%@ | {ReportCatalogDecideFound} successful catalog download yet no available patch or full asset found"
+ "%@ | {ReportCatalogDecideFound} successful catalog download yet no catalog provided"
+ "%@:_adoptAlteredMarkers"
+ "%@:_persistLastStagingFrom"
+ "%@:_removeAllStagedContent"
+ "%@:firstSchedulerShortTermLockContentChecks"
+ "%@:isLocalContentValidForSetAtomicEntry"
+ "%@:modifySetConfiguration"
+ "%@^%@"
+ "%@^%@^%@..%@"
+ "%@|domainName:%@|setIdentifier:%@"
+ "%@|selector:%@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] PSUS-DETERMINE results not considered valid | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] have target-lookup-results | message:%{public}@%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] have target-lookup-results | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] nil target-lookup-results-key | assetTargetTrainName:@%{public}@ | assetTargetRestoreVersion:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] no target-lookup-results even though already determined | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] re-running PSUS-DETERMINE | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] target-lookup-results beyond PSUS-DETERMINE phase | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] unable to load persisted set-lookup-result file | assetTargetTrainName:@%{public}@ | assetTargetRestoreVersion:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] unknown target-OTA-situation (re-running PSUS-DETERMINE) | targetLookupResultsKey:@%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} unable to load persisted set-lookup-result file | targetLookupResultsKey:@%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_availableForStagingRemove} removed target-OS entry | entryID:%{public}@ | availableForStaging:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_availableForStagingRemove} unable to load persisted-entry | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_lookupCacheRemoveResult} removed target-OS | entryID:%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_lookupCacheRemoveResult} unable to load persisted-entry | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} adopted previous-OTA-situation from target (just completed OTA) | targetOSVersion:%{public}@ | targetBuild:%{public}@ | startupPreviousOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} adopted previous-OTA-situation from target (now running OS where staging had been attempted from) | targetOSVersion:%{public}@ | targetBuild:%{public}@ | startupPreviousOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} change to target-OTA-situation | entryID:%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} change to target-OTA-situation | targetLookupResultsKey:%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} erased previous-OTA-situation | hadBeenPreviousOTASituation:%{public}@ | startupPreviousOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} first time persisted target-lookup-results included target-OTA-situation"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} persisted target-OTA-situation | targetLookupResultsKey:%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} unable to load entry from persistedTargetLookupResults | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} unable to load persistedTargetLookupResults from persistedEntry | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} unable to retrieve set-lookup-result | entryID:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {ClientPurgeDecideStagingClient} purging of all pre-SU-staging tracking / content | requestingPurgeProcessName:%{public}@ | stagingClientName:%{public}@ | eventInfo:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} client-defined set-target for asset-type - not staging based on alread-downloaded | descriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {FormCandidatesDecideDetermine} set-target indicating nothing to be staged and no set-configuration | nextSetTarget:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} first execution of MA daemon tracking previous-OTA-situation | startupPreviousOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} maintaining previous-OTA-situation | startupPreviousOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} not running new-OS | fromOS:%{public}@(%{public}@) | targetOS:%{public}@(%{public}@)"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} final resume complete | followupEvent:%{public}@ | stagerResumeFlow:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_collectOverviewInformation} unable to load entry from persistedTargetLookupResults (most recent target-OS) | targetLookupResultsKey:%{public}@, "
+ "%{public}@\n[AUTO-STAGER] {_collectOverviewInformation} unable to load entry from persistedTargetLookupResults (other target-OS) | otherTargetLookupResultsKey:%{public}@, "
+ "%{public}@\n[AUTO-STAGER] {_formCandidateSetLookupArray} set-target indicating nothing to be staged | nextSetTarget:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeDescriptorFromSuccessfullyStaged} target-OTA-situation now indicates empty | targetLookupResultsKey:%{public}@ | targetOTASituation:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeDescriptorFromSuccessfullyStaged} unable to load persisted set-lookup-result file | targetLookupResultsKey:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_removeStagedAssetFromFilesystem} asset directory does not exist - stagedDescriptor:%{public}@ | localContentURL:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} content on filesystem validated (adopted) | entryID:%{public}@ | targetOTASituation:%{public}@ | targetLookupResults:%{public}@"
+ "%{public}@\n{%{public}@} forming available-for-staging (to then be split into REQUIRED and OPTIONAL"
+ "%{public}@\n{%{public}@} unable to load persisted available-for-staging file | targetLookupResultsKey:%{public}@"
+ "%{public}@ {SetDoneDetermine} | SIMULATE_OPERATION(%lld) | call to stagerJobDetermineDone postponed"
+ "%{public}@ {SetDoneDetermine} | SIMULATE_OPERATION(%{public}@) | call to stagerJobDetermineDone postponed"
+ "%{public}@ {simulateEnd} | SIMULATE_END(%{public}@) | immediate operation so no end (ignored)\nJOB-SUMMARY:%{public}@"
+ "%{public}@ {simulateSet} | SIMULATE_IMMEDIATE | simulateOperation:%{public}@, simulateEnd:%{public}@"
+ "%{public}@ {simulateSet} | unable trigger immediate simulator operation(%{public}@) [- ]not yet triggered] | simulateOperation:%{public}@, simulateEnd:%{public}@\nJOB-SUMMARY:%{public}@"
+ "%{public}@ | {%{public}@} newer version found that is ramped (and have older atomic-instance) - discarding newer set-descriptor | autoAssetSetDescriptor:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationOperations} 1-shot triggered push-job | currentlyAwaiting:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationOperations} 1-shot triggered selectors | NoRetry:%ld RequiringRetry:%ld | MA_MILESTONE"
+ "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationOperations} nil currentlyAwaiting encountered on jobsAwaitingTrigger"
+ "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationOperations} nil currentlyAwaiting.assetSelector encountered on jobsAwaitingTrigger | assetSelector:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_schedulePushNotifications} scheduled-job now push-job | pushSelectorKey:%{public}@ | pushPolicy:%{public}@ | delay(%{public}@..%{public}@), jitter(%{public}@..%{public}@) | finalDelaySecs:%{public}@"
+ "-%@"
+ "2.5.3"
+ "3.0.4"
+ ">>>\nPERSISTED COUNTS:\n                            General: %llu\n                TargetLookupResults: %llu\n        AvailableForStagingByTarget: %llu\n\nSTARTUP:\n           LastStagingFromOSVersion: %@\n        LastStagingFromBuildVersion: %@\n               AssetTargetOSVersion: %@\n            AssetTargetBuildVersion: %@\n                CandidateAssetCount: %llu\n      DeterminedAvailableAssetCount: %llu\n          ActivelyStagingAssetCount: %llu\n          AwaitingStagingAssetCount: %llu\n                   StagedAssetCount: %llu\n       StagedAssetTotalContentBytes: %llu\n               PreviousOTASituation: %@\n               StagingFromOSVersion: %@\n            StagingFromBuildVersion: %@\n\nCONTROL:\n             LoadPersistedPostponed: %@\n          AlwaysPromoteStagedAssets: %@\n\nMOST-RECENT TARGET:\n               AssetTargetOSVersion: %@\n            AssetTargetBuildVersion: %@\n               AssetTargetTrainName: %@\n          AssetTargetRestoreVersion: %@\n           OptionalAssetSizeAllowed: %@\n           ActiveTargetOTASituation: %@\n      ActiveCandidatesRequiredCount: %llu\n      ActiveCandidatesOptionalCount: %llu\n      ActiveSetConfigsRequiredCount: %llu\n      ActiveSetConfigsOptionalCount: %llu\n       ActiveAvailableRequiredCount: %llu\n       ActiveAvaialbleOptionalCount: %llu\n\nOTHER TARGET:\n                    OtherTargetName: %@\n            OtherTargetOTASituation: %@\n       OtherCandidatesRequiredCount: %llu\n       OtherCandidatesOptionalCount: %llu\n       OtherSetConfigsRequiredCount: %llu\n       OtherSetConfigsOptionalCount: %llu\n        OtherAvailableRequiredCount: %llu\n        OtherAvaialbleOptionalCount: %llu\n\nSTAGING-CLIENT REQUESTS:\n                     DetermineCount: %llu\n                     DownloadActive: %@\n                             Active: %@\n                               Name: %@\n\nDETERMINE:\n             SetConfigurationsCount: %llu\n                    SetTargetsCount: %llu\n                 ScheduledJobsCount: %llu\n\nCANDIDATES:\n          CandidatesForStagingCount: %llu\n             SetConfigurationsCount: %llu\n              SetLookupResultsCount: %llu\n     BaseForStagingDescriptorsCount: %llu\n         DeterminingBySelectorCount: %llu\n\nAVAILABLE-OR-STAGED:\n           AvailableForStagingCount: %llu\n        AwaitingStagingAttemptCount: %llu\n            SuccessfullyStagedCount: %llu\n\nPROGRESS:\n    OverallStagedTotalExpectedBytes: %llu\n  OverallStagedDownloadedSoFarBytes: %llu\n      CurrentStagedLastWrittenBytes: %llu\n        CurrentStagedRemainingBytes: %llu\n\nELIMINATION:\n                     SelectorsCount: %llu\n         SetConfigurationCurrentJob: %@\n         SelectorsAcknowledgedCount: %llu\n<<<]"
+ "@\"NSObject<OS_voucher>\""
+ "@152@0:8q16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144"
+ "@352@0:8q16@24@32@40@48@56@64@?72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256B264@268@276@284B292B296B300@304@312@320@328@336@344"
+ "ANOMALY(content to be promoted)|"
+ "AlteredDecideSameSetConfiguration"
+ "AlteredInvalAllAvailable"
+ "AlteredInvalAllAvailableCancelActiveJob"
+ "Appending additional extention: %@"
+ "AutoStagerSituation"
+ "B48@0:8@16@24^@32^@40"
+ "C32@0:8@16@24"
+ "CLIENT_ALTERED"
+ "CLIENT_SET_TARGET"
+ "CancelingIgnoreDetermine"
+ "ClientAcceptEraseCancelActiveJob"
+ "ClientAlteredForgetDetermine"
+ "ClientSetTargetsForgetDetermine"
+ "ControlAlteredSetConfiguration"
+ "ControlSetTargetsSpecified"
+ "DEL_AI_DROP_CORRUPTED_ASSET "
+ "DEL_ASSET_CORRUPTED        "
+ "DEL_SD_DROP_CORRUPTED_ASSET"
+ "DETERMINED_AVAILABLE"
+ "DETERMINED_BLOCKED"
+ "DETERMINED_NO_NEWER"
+ "DETERMINED_PARTIAL"
+ "DETERMINED_PURGED"
+ "DOWNLOADED_BLOCKED"
+ "DOWNLOADED_EMPTIED"
+ "DOWNLOADED_NOTHING"
+ "Dwq\x81"
+ "Failed to mark path %@ as purgeable, errno:%d"
+ "LuckBSeed"
+ "MA-AUTO-CONTROL(REPLY):STAGER_OVERVIEW"
+ "MA-AUTO-CONTROL:STAGER_OVERVIEW"
+ "MADAutoControl:handleControlClientStagerOverviewRequest"
+ "MADStager:AlteredDecideSameSetConfiguration"
+ "MADStager:AlteredInvalAllAvailable"
+ "MADStager:AlteredInvalAllAvailableCancelActiveJob"
+ "MADStager:ClientAcceptEraseCancelActiveJob"
+ "MADStager:ReplyNoCandidatesEraseAll"
+ "MADStager:ReplyNothingStagedEraseAll"
+ "MADStager:SetTargetDecideSameTarget"
+ "MADStager:SetTargetInvalAllAvailable"
+ "MADStager:SetTargetInvalAllAvailableCancelActiveJob"
+ "MADStager:UpdateStagedSituation"
+ "MANAutoAssetControlStagerInformation"
+ "MASAutoAssetControlStagerInformation"
+ "OTA_FROM_LEGACY"
+ "OTA_NEVER"
+ "PrevOTA"
+ "ReplyNoCandidatesEraseAll"
+ "ReplyNothingStagedEraseAll"
+ "STAGED_ALL_DESIRED"
+ "STAGED_PARTIAL"
+ "STAGER_PROMOTED|requiringLoad:%@|stagedToDownloaded:%ld|stagedSetLookupResults:%ld|newOSPromotion:%@"
+ "STAGING_ALREADY_DOWNLOADED|alreadyDownloaded:%ld|setConfigurations:%ld|entriesWhenTargeting:%ld|setTargets:%ld|scheduledJobs:%ld"
+ "STAGING_AUTO_ASSET_CATALOG|autoAssetCatalog:%@[%@]|baseForStaging:%ld"
+ "STAGING_CLIENT_DOWNLOAD_REQUEST|stagingClientRequest:%@|baseForStaging:%ld"
+ "STAGING_SET_TARGETS|entriesWhenTargeting:%ld"
+ "STARTUP{lastStagingFrom:%@(%@)|target:%@(%@)|determined:%llu|staged:%llu(%llu bytes)|situation:%@|from:%@(%@)}|MOST-RECENT{target:%@(%@)|situation:%@|(available)R:%llu,O:%llu}|OTHER{target:%@|situation:%@|(available)R:%llu,O:%llu}|staged:%llu"
+ "SetTargetDecideSameTarget"
+ "SetTargetInvalAllAvailable"
+ "SetTargetInvalAllAvailableCancelActiveJob"
+ "Starting built-in MobileAsset brain built Sep 16 2025 23:13:33"
+ "Starting downloaded MobileAsset brain (version: %@) built Sep 16 2025 23:13:33"
+ "T@\"NSArray\",&,N,V_currentAttemptBeginningMarkers"
+ "T@\"NSObject<OS_voucher>\",&,N,V_clientVoucher"
+ "T@\"NSString\",&,N,V_otherTargetName"
+ "T@\"NSString\",&,N,V_startupAssetTargetRestoreVersion"
+ "T@\"NSString\",&,N,V_startupAssetTargetTrainName"
+ "TB,N,V_eliminationSetConfigurationCurrentJob"
+ "TB,N,V_loadPersistedPreviousOTASituation"
+ "TB,N,V_loadedPersistedTargetLookupResults"
+ "TB,N,V_stagingClientDownloadRequestActive"
+ "TB,N,V_stagingClientRequestActive"
+ "TB,N,V_startupStagedNoContent"
+ "TB,N,V_storedTargetWithOTASituation"
+ "TB,R,N,V_newOSPromotion"
+ "TQ,N,V_activeTargetAvailableForStagingOptionalCount"
+ "TQ,N,V_activeTargetAvailableForStagingRequiredCount"
+ "TQ,N,V_activeTargetCandidateSetConfigurationsOptionalCount"
+ "TQ,N,V_activeTargetCandidateSetConfigurationsRequiredCount"
+ "TQ,N,V_activeTargetCandidatesForStagingOptionalCount"
+ "TQ,N,V_activeTargetCandidatesForStagingRequiredCount"
+ "TQ,N,V_availableForStagingCount"
+ "TQ,N,V_awaitingStagingAttemptCount"
+ "TQ,N,V_baseForStagingDescriptorsCount"
+ "TQ,N,V_candidateSetConfigurationsCount"
+ "TQ,N,V_candidatesForStagingCount"
+ "TQ,N,V_determiningBySelectorCount"
+ "TQ,N,V_eliminationSelectorsAcknowledgedCount"
+ "TQ,N,V_eliminationSelectorsCount"
+ "TQ,N,V_otherTargetAvailableForStagingOptionalCount"
+ "TQ,N,V_otherTargetAvailableForStagingRequiredCount"
+ "TQ,N,V_otherTargetCandidateSetConfigurationsOptionalCount"
+ "TQ,N,V_otherTargetCandidateSetConfigurationsRequiredCount"
+ "TQ,N,V_otherTargetCandidatesForStagingOptionalCount"
+ "TQ,N,V_otherTargetCandidatesForStagingRequiredCount"
+ "TQ,N,V_persistedAvailableForStagingByTargetCount"
+ "TQ,N,V_persistedStateCount"
+ "TQ,N,V_persistedTargetLookupResultsCount"
+ "TQ,N,V_scheduledJobsCount"
+ "TQ,N,V_setConfigurationsCount"
+ "TQ,N,V_setLookupResultsCount"
+ "TQ,N,V_setTargetsCount"
+ "TQ,N,V_stagingClientDetermineRequestsCount"
+ "TQ,N,V_successfullyStagedCount"
+ "TRIGGER_STAGER_JOB_FINISHED"
+ "TargetWasEmptied"
+ "Tq,N,V_activeTargetOTASituation"
+ "Tq,N,V_otherTargetOTASituation"
+ "Tq,N,V_startupPreviousOTASituation"
+ "UpdateStagedSituation"
+ "[%{public}@] {%{public}@}\n[CLEARER-LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | hadBeenLatestIsLocked:%{public}@ | setConfiguration:%{public}@"
+ "[%{public}@] {CLOUDCHANNELS:handlePushNotifications} push-notification resulted in 0 push jobs"
+ "[%{public}@] {CLOUDCHANNELS:handlePushNotifications} scheduling push jobs | pushNotificationsBySelector:%ld"
+ "[%{public}@] {handleControlClientSimulateSetJobOperation} SIMULATE | routing to job | autoJobByIdentifier:%{public}@ | marker:%{public}@ | simulateOperation:%{public}@, simulateEnd:%{public}@"
+ "[%{public}@] {handleControlClientSimulateSetJobOperation} SIMULATE | routing to job | autoJobBySelector:%{public}@ | marker:%{public}@ | simulateOperation:%{public}@, simulateEnd:%{public}@"
+ "[%{public}@] {handleControlClientSimulateSetJobOperation} SIMULATE | routing to stager-job | stagerCurrentJob:%{public}@ | marker:%{public}@ | simulateOperation:%{public}@, simulateEnd:%{public}@"
+ "[%{public}@] {handleSetClientAssetSetForStagingRequest}\n[SET-TARGETS] client-specified set-target matches already-persisted | setInfoInstance:%{public}@"
+ "[%{public}@] {jobControlInformationForSetJobKey} SIMULATE | found control information | setConfiguration:%{public}@ | associatedControlInfo:%{public}@"
+ "[%{public}@] {loadPersistedSetConfigurations} all set-targets removed | reason:%{public}@ | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[%{public}@] {loadPersistedSetConfigurations} no persisted set-targets to be resumed | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[%{public}@] {loadPersistedSetConfigurations} set-targets preserved | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[%{public}@] {loadPersistedSetTargets} keeping set-targets (and not adjusting set-configurations) since last-OS version matches current OS version | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@\n#_%{public}@:(%{public}@) [%{public}@] | %{public}@ situation:%{public}@\n#_%{public}@:%{public}@"
+ "[MobileAssetHealthReport]: Submitted health reports | UUID:%{public}@\nMAHR reports:\n%{public}@\nMAHR commonFields:\n%{public}@"
+ "[MobileAssetHealthReport]: nil previous-OTA-situation-name | previousOTASituation:%ld"
+ "_activeTargetAvailableForStagingOptionalCount"
+ "_activeTargetAvailableForStagingRequiredCount"
+ "_activeTargetCandidateSetConfigurationsOptionalCount"
+ "_activeTargetCandidateSetConfigurationsRequiredCount"
+ "_activeTargetCandidatesForStagingOptionalCount"
+ "_activeTargetCandidatesForStagingRequiredCount"
+ "_activeTargetOTASituation"
+ "_adoptAlteredMarkers:fromLocation:"
+ "_alreadyDownloadedDescriptorsArray:limitingToSupportingStaging:"
+ "_availableForStagingCount"
+ "_availableForStagingRemove:forTargetTrainName:withRestoreVersion:"
+ "_awaitingStagingAttemptCount"
+ "_baseForStagingDescriptorsCount"
+ "_candidateSetConfigurationsCount"
+ "_candidatesForStagingCount"
+ "_candidatesRemove:forTargetTrainName:withRestoreVersion:"
+ "_clientVoucher"
+ "_collectOverviewInformation"
+ "_currentAttemptBeginningMarkers"
+ "_determiningBySelectorCount"
+ "_eliminationSelectorsAcknowledgedCount"
+ "_eliminationSelectorsCount"
+ "_extendLookupByAssetTypeWithDownloadedDescriptors:limitingToSetTargets:"
+ "_extendLookupByAssetTypeWithSetConfigurations:limitingToSetTargets:"
+ "_loadPersistedPreviousOTASituation"
+ "_loadedPersistedTargetLookupResults"
+ "_logPersistedActiveTargetLookupResults:"
+ "_logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:withTargetOTASituation:message:"
+ "_lookupCacheRemoveResult:forTargetTrainName:withRestoreVersion:"
+ "_newOSPromotion"
+ "_otherTargetAvailableForStagingOptionalCount"
+ "_otherTargetAvailableForStagingRequiredCount"
+ "_otherTargetCandidateSetConfigurationsOptionalCount"
+ "_otherTargetCandidateSetConfigurationsRequiredCount"
+ "_otherTargetCandidatesForStagingOptionalCount"
+ "_otherTargetCandidatesForStagingRequiredCount"
+ "_otherTargetName"
+ "_otherTargetOTASituation"
+ "_persistAllTargetLookupResultsOTASituation:fromLocation:"
+ "_persistEraseLookupResults:forTargetTrainName:forTargetRestoreVersion:"
+ "_persistErasePreviousOTASituation:"
+ "_persistLastStagingFrom:"
+ "_persistPreviousOTASituationIfTargetMatchesCurrentOS:settingStartupSituation:"
+ "_persistStoredTargetWithOTASituation:"
+ "_persistTargetOTASituation:fromLocation:"
+ "_persistTargetOTASituationForFollowup:fromLocation:"
+ "_persistedAvailableForStagingByTargetCount"
+ "_persistedStateCount"
+ "_persistedTargetLookupResultsCount"
+ "_recordOperationForStagedAttributes:required:"
+ "_removeAllStagedContent:"
+ "_scheduledJobsCount"
+ "_setConfigurationsCount"
+ "_setLookupResultsCount"
+ "_setTargetsCount"
+ "_stagedAllDesiredForCurrentTarget"
+ "_stagedNewOSPromoteAdoptSetTargets"
+ "_stagingClientDetermineRequestsCount"
+ "_stagingClientDownloadRequestActive"
+ "_stagingClientRequestActive"
+ "_startupAssetTargetRestoreVersion"
+ "_startupAssetTargetTrainName"
+ "_startupPreviousOTASituation"
+ "_startupStagedNoContent"
+ "_storedTargetWithOTASituation"
+ "_successfullyStagedCount"
+ "action_AlteredDecideSameSetConfiguration:error:"
+ "action_AlteredInvalAllAvailable:error:"
+ "action_AlteredInvalAllAvailableCancelActiveJob:error:"
+ "action_ClientAcceptEraseCancelActiveJob:error:"
+ "action_ReplyNoCandidatesEraseAll:error:"
+ "action_ReplyNothingStagedEraseAll:error:"
+ "action_SetTargetDecideSameTarget:error:"
+ "action_SetTargetInvalAllAvailable:error:"
+ "action_SetTargetInvalAllAvailableCancelActiveJob:error:"
+ "action_UpdateStagedSituation:error:"
+ "activeTargetAvailableForStagingOptionalCount"
+ "activeTargetAvailableForStagingRequiredCount"
+ "activeTargetCandidateSetConfigurationsOptionalCount"
+ "activeTargetCandidateSetConfigurationsRequiredCount"
+ "activeTargetCandidatesForStagingOptionalCount"
+ "activeTargetCandidatesForStagingRequiredCount"
+ "activeTargetOTASituation"
+ "addNoRetryCurrent:%@|"
+ "addObserver:%@|"
+ "addRetryCurrent:%@|"
+ "adopted startup target|"
+ "assetType:%@"
+ "atomicInstanceForceUnlock:forgettingAtomicInstance:historyOperationAI:historyOperationSD:"
+ "auto-asset-stager has indicated new-OS-promotion - all set-targets were from previous OS viewpoint so no longer applicable"
+ "availableForStagingCount"
+ "awaitingStagingAttemptCount"
+ "baseForStagingDescriptorsCount"
+ "candidateSetConfigurationsCount"
+ "candidates:%llu,determinedAvailable:%llu,activelyStaging:%llu,awaitingStaging:%llu | [stagedAssets]count:%llu,totalContentBytes:%llu,noContent:%@"
+ "candidatesForStagingCount"
+ "clientDownloadGroups:withAlreadyDownloadedDescriptors:"
+ "clientVoucher"
+ "collectOverviewInformation"
+ "com.apple.MobileAsset.UAF.FM.CodeLM"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Search.ODLA"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.VoiceAssistant"
+ "controlAlteredSetConfiguration:"
+ "controlSetTargetsSpecified:"
+ "corrupted assets found | "
+ "currentAttemptBeginningMarkers"
+ "dedupAvailableForStaging:dedupingAssetDescriptors:removingAlreadyDownloaded:ofContainerName:"
+ "determiningBySelectorCount"
+ "downloadedDescriptorsBySelector"
+ "eliminationSelectorsAcknowledgedCount"
+ "eliminationSelectorsCount"
+ "final available-for-staging | targetLookupResultsKey:%@ | availableForStaging:%@"
+ "firstSchedulerShortTermLockContentChecks:"
+ "fullName"
+ "getPreviousOTAStatus"
+ "getSystemAppURL:assetType:"
+ "handleControlClientStagerOverviewRequest"
+ "handleControlClientStagerOverviewRequest:forAutoJob:"
+ "handleStagingClientDownloadGroupsRequest"
+ "have currentAttemptRemainingMarkers yet nil currentAttemptBeginningMarkers"
+ "have staged content (alwaysPromoteStagedAssets)|"
+ "have staged content (nowRunningTargetOS)|"
+ "have staged content (purging)|"
+ "have staged content (running last-staging-from-OS)|"
+ "have target-lookup-results (running last-staging-from-OS)|"
+ "initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:usingCachedAutoAssetCatalog:withControlInformation:"
+ "initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withNewOSPromotion:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withEntriesWhenTargeting:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:"
+ "initWithPromoted:withSetLookupResults:withNewOSPromotion:withRequiringLoadPriorToUse:"
+ "initWithSetTargets:"
+ "initWithStagingClientRequest:withAlreadyDownloadedDescriptors:"
+ "invalid persisted counts|"
+ "isAnyAvailableForStagingByGroup:withAlreadyDownloadedDescriptors:targetHadBeenDetermined:"
+ "isLocalContentValidForSetAtomicEntry:fromLocation:"
+ "lastStagingFrom:%@(%@),assetTarget:%@(%@)[%@(%@)]"
+ "lastStagingFrom[OSVersion:%@,BuildVersion:%@] | assetTarget[OSVersion:%@,BuildVersion:%@,TrainName:%@,RestoreVersion:%@]"
+ "lastStagingFrom[OSVersion:%@,BuildVersion:%@] | assetTarget[OSVersion:%@,BuildVersion:%@,TrainName:%@,RestoreVersion:%@] | previousOTASituation:%@"
+ "loadPersistedPreviousOTASituation"
+ "loadPersistedTargetLookupResults:"
+ "loadedPersistedTargetLookupResults"
+ "markerRetry:%@|"
+ "markersNoRetry("
+ "markersRequiringRetry("
+ "modifySetConfiguration:toEntriesFromSetTarget:"
+ "monitorMarkers("
+ "newOSPromoted"
+ "newOSPromotion"
+ "no persisted entries (purging)|"
+ "no staged content (purging)|"
+ "nowRunningTargetOS|"
+ "otherTargetAvailableForStagingOptionalCount"
+ "otherTargetAvailableForStagingRequiredCount"
+ "otherTargetCandidateSetConfigurationsOptionalCount"
+ "otherTargetCandidateSetConfigurationsRequiredCount"
+ "otherTargetCandidatesForStagingOptionalCount"
+ "otherTargetCandidatesForStagingRequiredCount"
+ "otherTargetName"
+ "otherTargetOTASituation"
+ "persistedAvailableForStagingByTargetCount"
+ "persistedStateCount"
+ "persistedTargetLookupResultsCount"
+ "previousOTASituation"
+ "previousOTASituationName:"
+ "purgeAlreadyStagedNotApplicableForRequiredByTarget"
+ "purged (previousOTASituationAdopted:%@)|"
+ "removeObserver:%@|"
+ "removed all (new-OS-promoteed)|"
+ "removed all persisted-state (everything has been new-OS-promoted)"
+ "removed persisted-state (once fully resumed) | nowRunningTargetOS:%@ | previousOTASituationAdopted:%@"
+ "scheduledJobsCount"
+ "setActiveTargetAvailableForStagingOptionalCount:"
+ "setActiveTargetAvailableForStagingRequiredCount:"
+ "setActiveTargetCandidateSetConfigurationsOptionalCount:"
+ "setActiveTargetCandidateSetConfigurationsRequiredCount:"
+ "setActiveTargetCandidatesForStagingOptionalCount:"
+ "setActiveTargetCandidatesForStagingRequiredCount:"
+ "setActiveTargetOTASituation:"
+ "setAvailableForStagingCount:"
+ "setAwaitingStagingAttemptCount:"
+ "setBaseForStagingDescriptorsCount:"
+ "setCandidateSetConfigurationsCount:"
+ "setCandidatesForStagingCount:"
+ "setClientVoucher:"
+ "setConfigurationsCount"
+ "setCurrentAttemptBeginningMarkers:"
+ "setDeterminingBySelectorCount:"
+ "setEliminationSelectorsAcknowledgedCount:"
+ "setEliminationSelectorsCount:"
+ "setIdentifier:%@ | latestDiscoveredAssetSetUUID:%@ | latestToVendAssetSetUUID:%@ | LastCheckedDate:%@ | lastestToVendIsLocked:%@ | lastestToVendMatchesSetConfig:%@ | availableForUseError:%@ | newerVersionError:%@ | latestInstanceFromPreSUStaging:%@"
+ "setLoadPersistedPreviousOTASituation:"
+ "setLoadedPersistedTargetLookupResults:"
+ "setLookupResultsCount"
+ "setOtherTargetAvailableForStagingOptionalCount:"
+ "setOtherTargetAvailableForStagingRequiredCount:"
+ "setOtherTargetCandidateSetConfigurationsOptionalCount:"
+ "setOtherTargetCandidateSetConfigurationsRequiredCount:"
+ "setOtherTargetCandidatesForStagingOptionalCount:"
+ "setOtherTargetCandidatesForStagingRequiredCount:"
+ "setOtherTargetName:"
+ "setOtherTargetOTASituation:"
+ "setPersistedAvailableForStagingByTargetCount:"
+ "setPersistedStateCount:"
+ "setPersistedTargetLookupResultsCount:"
+ "setRetry|"
+ "setScheduledJobsCount:"
+ "setSetConfigurationsCount:"
+ "setSetLookupResultsCount:"
+ "setSetTargetsCount:"
+ "setStagingClientDetermineRequestsCount:"
+ "setStagingClientDownloadRequestActive:"
+ "setStagingClientRequestActive:"
+ "setStartupAssetTargetRestoreVersion:"
+ "setStartupAssetTargetTrainName:"
+ "setStartupPreviousOTASituation:"
+ "setStartupStagedNoContent:"
+ "setStoredTargetWithOTASituation:"
+ "setSuccessfullyStagedCount:"
+ "setTargetEntries:match:"
+ "setTargetPersistedMatchesClientSpecified"
+ "setTargetPersistedMatchesClientSpecified:"
+ "setTargetsCount"
+ "setTrigNoRetry|"
+ "setTrigRetry|"
+ "simulateSet"
+ "stagedNoContent"
+ "stagerInformation"
+ "stagerResumed:withSetLookupResults:performingNewOSPromotion:requiringLoadPriorToUse:"
+ "stagingClientDetermineRequestsCount"
+ "stagingClientDownloadRequestActive"
+ "stagingClientRequestActive"
+ "startStagerDownloadForStaging:withAssetTargetBuildVersion:usingCachedAutoAssetCatalog:withControlInformation:"
+ "startupAssetTargetRestoreVersion"
+ "startupAssetTargetTrainName"
+ "startupPreviousOTASituation"
+ "startupStagedNoContent"
+ "storedTargetWithOTASituation"
+ "successfullyStagedCount"
+ "target-lookup-results describing Pallas atomicity | targetOTASituation:%@ | trainTargetLookupResults:%@"
+ "targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:withTargetOTASituation:"
+ "targetLookupResultsOTASituation"
+ "targetMode:%@ | candidate:%llu | determinedAvailable:%llu | activelyStaging:%llu | awaitingStaging:%llu | staged:%llu(totalContentBytes:%llu)(noContent:%@)"
+ "targetMode:%@ | candidate:%llu | determinedAvailable:%llu | activelyStaging:%llu | awaitingStaging:%llu | staged:%llu(totalContentBytes:%llu,noContent:%@)"
+ "trigNoRetry:%@|"
+ "trigRetry:%@|"
+ "trimRetry:%@|"
+ "trimTrigNoRetry:%@|"
+ "trimTrigRetry:%@|"
+ "valid persisted counts (handedOffAsPromoted:%ld)|"
+ "valid persisted counts (non-exact match) (handedOffAsPromoted:%ld)|"
+ "verifySetDescriptorIsLockable:fromLocation:notLocakableError:corruptedAtomicEntries:"
+ "{%@:_persistTargetOTASituationForFollowup} unsupported followup event | followupEvent:%@"
+ "{%@:verifySetDescriptorIsLockable} Set is not lockable because corrupted asset as well as other not lockable reason is found. Asset corruption error will be returned. The other error is: %@"
+ "{%@:verifySetDescriptorIsLockable} corrupted assets: "
+ "{%@} altered set-configuration auto-asset-entries to align with set-target | setConfiguration:%@ | setTarget:%@"
+ "{%@} auto-asset-scheduled provided markersNoRetry entry not being monitored | marker:%@"
+ "{%@} auto-asset-scheduled provided markersRequiringRetry entry not being monitored | marker:%@"
+ "{%@} no set-configuration for set-target | setTarget:%@"
+ "{%@} set-target versions not comparable (ignoring) | setTarget:%@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] available-for-staging asset-descriptor dropped | availableDescriptor:%{public}@ | nextAlreadyDownloadedDescriptor:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] sole available-for-staging asset-descriptor dropped | availableDescriptor:%{public}@ | nextAlreadyDownloadedDescriptor:%{public}@"
+ "{%{public}@} Removing corrupted asset %{public}@"
+ "{%{public}@} adoptMarkersFlow:%{public}@"
+ "{%{public}@} | no set-target entry found for entry:%{public}@"
+ "{%{public}@} | set-target entry matches set-configuration | setTarget:%{public}@ | setConfiguration:%{public}@"
+ "{%{public}@} | set-target out-of-range | setTarget:%{public}@ | setConfiguration:%{public}@"
+ "{%{public}@} | unable to load persisted-set-configuration file | set-target:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:cachedLookupResultForSetConfiguration} | auto-asset-lookup-cache not in use for PSUS | set-configuration:%{public}@ | setAssetType:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSelector:} | auto-asset-lookup-cache not in use for PSUS | selector:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSelector:} | updated auto-asset-lookup-cache | selector:%{public}@ | assetAudience:%{public}@ | bySelectorKey:%{public}@"
+ "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSetConfiguration:} | auto-asset-lookup-cache not in use for PSUS | set-configuration:%{public}@"
+ "{AUTO-LOOKUP-CACHE[BOTH]:clearLookupResultsForSetConfiguration} | clearing auto-asset-lookup-cache | set-configuration:%{public}@"
+ "{AUTO-LOOKUP-CACHE[BOTH]:clearLookupResultsForSetConfiguration} | unable to locate auto-asset-lookup-cache | set-configuration:%{public}@"
+ "{AUTO-LOOKUP-CACHE[STAGING]:clearLookupResultsForSetConfiguration} | removed stale auto-asset-lookup-cache entry | lookupCacheKey:%{public}@ | asset-type:%{public}@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce} current nonce now nil, do not attempt to update."
+ "{collectOverviewInformation} failed to locate shared AutoAssetStager"
+ "{controlAlteredSetConfiguration} failed to locate shared AutoAssetStager"
+ "{controlSetTargetsSpecified} failed to locate shared AutoAssetStager"
+ "{didReceivePushNotification} [PUSH-NOTIFICATION] HANDLER | autoAssetPushNotifications:%{public}@"
+ "{didReceivePushNotification} [PUSH-NOTIFICATION] RECEIVED"
+ "{handleControlClientStagerOverviewRequest} stagerInformation:%{public}@"
+ "{loadPersistedSetTargets} | no set-target entry found for entry:%{public}@"
+ "{locateNewAllSetTargets} | no set-target entry found for entry:%{public}@"
+ "{previousOTASituation} failed to locate shared AutoAssetStager"
+ "{setTargetPersistedMatchesClientSpecified} | nil entry provided by client - treating as same set-target to preserve persisted | setInfoInstance:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | unable to decode persisted set-target | entryID:%{public}@"
+ "{setTargetPersistedMatchesClientSpecified} | unable to load persisted set-target | entryID:%{public}@"
- "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] message:%{public}@%{public}@"
- "%{public}@\n[%{public}@] {%{public}@} beginning BY-GROUP-MODE request when had been operating in ALL-MODE"
- "%{public}@\n[AUTO-STAGER] {ClientPurgeDecideStagingClient} purging of all pre-SU-staging tracking / content | requestingPurgeProcessName:%{public}@ | stagingClientName:%{public}@"
- "%{public}@\n[AUTO-STAGER] {getTargetLookupResultsForKey} content on filesystem validated | entryID:%{public}@, adopted targetLookupResults:%{public}@"
- "%{public}@\n{%{public}@} forming available-for-staging (to then be split into REQUIred and OPTIONAL"
- "%{public}@ | {%{public}@} newer version found that is ramped (and have older atomic-instance) - discrarding newer set-descriptor | autoAssetSetDescriptor:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} 1-shot triggered push-job | currentlyAwaiting:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} 1-shot triggered selectors | NoRetry:%ld RequiringRetry:%ld | MA_MILESTONE"
- "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} nil currentlyAwaiting encountered on jobsAwaitingTrigger"
- "%{public}@ | {AUTO-SCHEDULER:_performPushNotificationActivityOperations} nil currentlyAwaiting.assetSelector encountered on jobsAwaitingTrigger | assetSelector:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_schedulePushNotifications} scheduled-job now push-job | pushSelectorKey:%{public}@ | pushPolicy:%{public}@ | delay(%{public}@..%{public}@), jitter(%{public}@..%{public}@)"
- "%{public}@ | {StagerDownloadDecideFilesystem} using cached lookup result for asset-selector | followupParam:%{public}@"
- "2.5.2"
- "3.0.3"
- "@144@0:8q16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136"
- "@348@0:8q16@24@32@40@48@56@64@?72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280B288B292B296@300@308@316@324@332@340"
- "ClientDecideGroupTargetAvailablePurge"
- "Created the following MAAutoAssetPushNotifications: %{public}@"
- "DecideEmptyHaveAvailable"
- "Luck"
- "MADStager:ClientDecideGroupTargetAvailablePurge"
- "MADStager:DecideEmptyHaveAvailable"
- "MADStager:ReplyNoCandidatesRemoveAllReplyErased"
- "ReplyNoCandidatesRemoveAllReplyErased"
- "STAGER_PROMOTED|requiringLoad:%@|stagedToDownloaded:%ld|stagedSetLookupResults:%ld"
- "STAGING_ALREADY_DOWNLOADED|alreadyDownloaded:%ld|setConfigurations:%ld|setTargets:%ld|scheduledJobs:%ld"
- "STAGING_AUTO_ASSET_CATALOG|autoAssetCatalog:%@[%@]|baseForPatching:%ld"
- "Starting built-in MobileAsset brain built Aug 20 2025 20:19:08"
- "Starting downloaded MobileAsset brain (version: %@) built Aug 20 2025 20:19:08"
- "T@\"NSMutableDictionary\",&,N,V_lookupResultsByAssetSelectorForStaging"
- "T@\"NSMutableDictionary\",&,N,V_lookupResultsBySetConfigurationForStaging"
- "[%{public}@] {%{public}@}\n[CLEARER-LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "[%{public}@] {handleControlClientSimulateSetJobOperation} SIMULATE | setting job simulate operation | assetSelector:%{public}@ | simulateOperation:%{public}@, simulateEnd:%{public}@"
- "[%{public}@] {loadPersistedSetConfigurations} no persisted set-targets to be resumed"
- "_adoptAlteredMarkers"
- "_adoptAlteredMarkers:"
- "_extendLookupByAssetTypeWithDownloadedDescriptors:"
- "_extendLookupByAssetTypeWithSetConfigurations:"
- "_logPersistedTargetLookupResults:operation:forPersistedEntryID:withTargetLookupResults:message:"
- "_lookupResultsByAssetSelectorForStaging"
- "_lookupResultsBySetConfigurationForStaging"
- "_performPushNotificationActivityOperations"
- "_persistLastStagingFrom"
- "_removeAllStagedContent"
- "action_ClientDecideGroupTargetAvailablePurge:error:"
- "action_DecideEmptyHaveAvailable:error:"
- "action_ReplyNoCandidatesRemoveAllReplyErased:error:"
- "after resuming from persisted-state"
- "altered set-configuration auto-asset-entries to align with set-target | setConfiguration:%@ | setTarget:%@"
- "auto-asset patch and full entries for different versions | patch:%@, full:%@"
- "candidates:%llu,determinedAvailable:%llu,activelyStaging:%llu,awaitingStaging:%llu | [stagedAssets]count:%llu,totalContentBytes:%llu"
- "clientDownloadGroups:"
- "dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:"
- "getSystemAppURL:"
- "initWithAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withControlInformation:"
- "initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withTimerUUID:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduledJobs:withDownloadedDescriptor:"
- "initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:"
- "isAnyAvailableForStagingByGroup:"
- "lastStagingFrom:%@(%@),assetTarget:%@(%@)"
- "lastStagingFrom[OSVersion:%@,BuildVersion:%@] | assetTarget[OSVersion:%@,BuildVersion:%@]"
- "locateDownloadedNewBySelectorLimitedToStaging:YES"
- "lookupResultsByAssetSelectorForStaging"
- "lookupResultsBySetConfigurationForStaging"
- "persistDate:forKey:"
- "removed all persisted-state (nothing available)"
- "setIdentifier:%@ | latestDiscoveredAssetSetUUID:%@ | latestToVendAssetSetUUID:%@ | LastCheckedDate:%@ | lastestToVendIsLocked:%@ | lastestToVendMatchesSetConfig:%@ | availableForUseError:%@ | newerVersionError:%@ | latestInstanceFromPreSUStaging: %@"
- "setLookupResultsByAssetSelectorForStaging:"
- "setLookupResultsBySetConfigurationForStaging:"
- "stagerResumed:withSetLookupResults:requiringLoadPriorToUse:"
- "startStagerDownloadForStaging:withAssetTargetBuildVersion:withControlInformation:"
- "successful catalog download yet no assets in catalog | have installed asset-version:%@ | REVOKED"
- "successful catalog download yet no available patch or full asset found"
- "target-lookup-results describing Pallas atomicity | trainTargetLookupResults:%@"
- "targetLookupResultsLoadedFromPersisted:targetLookupResultsKey:persistedEntryID:"
- "targetMode:%@ | candidate:%llu | determinedAvailable:%llu | activelyStaging:%llu | awaitingStaging:%llu | staged:%llu(totalContentBytes:%llu)"
- "verifySetDescriptorIsLockable:fromLocation:notLocakableError:"
- "{%{public}@} | no set-taget entry found for entry:%{public}@"
- "{A:%@} auto-asset metadata considered invalid | %@"
- "{AUTO-LOOKUP-CACHE[%{public}@]:recordLookupResult:forSelector:} | updated auto-asset-lookup-cache | selector:%{public}@ | assetAudience:%{public}@"
- "{AUTO-LOOKUP-CACHE[CLIENT]:clearLookupResultsForSetConfiguration} | clearing auto-asset-lookup-cache | set-configuration:%{public}@"
- "{AUTO-LOOKUP-CACHE[CLIENT]:clearLookupResultsForSetConfiguration} | unable to locate auto-asset-lookup-cache | set-configuration:%{public}@"
- "{ClientDecideGroupTargetAvailablePurge} no REQUIRED and no OPTIONAL descriptors available for staging"
- "{ClientDecideGroupTargetAvailablePurge} no download client request when no REQUIRED but have OPTIONAL to stage"
- "{_adoptAlteredMarkers} auto-asset-scheduled provided markersNoRetry entry not being monitored | marker:%@"
- "{_adoptAlteredMarkers} auto-asset-scheduled provided markersRequiringRetry entry not being monitored | marker:%@"
- "{_removeDescriptorFromFilesystem} unable to determine local filesystem URL from localContentURL:%@"
- "{loadPersistedSetTargets} no set-configuration for set-target | setTarget:%@"
- "{loadPersistedSetTargets} set-target versions not comparable (ignoring) | setTarget:%@"
- "{loadPersistedSetTargets} | no set-taget entry found for entry:%{public}@"
- "{locateNewAllSetTargets} | no set-taget entry found for entry:%{public}@"

```
