## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-936.80.3.0.0
-  __TEXT.__text: 0x17a520
+1022.102.3.0.0
+  __TEXT.__text: 0x1912b0
   __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0xc260
-  __TEXT.__const: 0xb50
-  __TEXT.__cstring: 0x3c249
-  __TEXT.__oslogstring: 0x21389
-  __TEXT.__gcc_except_tab: 0x1440
+  __TEXT.__objc_methlist: 0xc8c0
+  __TEXT.__const: 0xc38
+  __TEXT.__cstring: 0x3eb25
+  __TEXT.__oslogstring: 0x258c1
+  __TEXT.__gcc_except_tab: 0x1424
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x22f8
+  __TEXT.__unwind_info: 0x2434
   __TEXT.__eh_frame: 0x7c
-  __TEXT.__objc_classname: 0xb34
-  __TEXT.__objc_methname: 0x2b843
-  __TEXT.__objc_methtype: 0x290e
-  __TEXT.__objc_stubs: 0x19700
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x2100
-  __DATA_CONST.__objc_classlist: 0x330
+  __TEXT.__objc_classname: 0xb5c
+  __TEXT.__objc_methname: 0x2d851
+  __TEXT.__objc_methtype: 0x2aab
+  __TEXT.__objc_stubs: 0x1a5a0
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x2138
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xde58
-  __DATA_CONST.__objc_selrefs: 0x6ff0
-  __DATA_CONST.__objc_arraydata: 0x810
-  __AUTH_CONST.__cfstring: 0x26960
-  __AUTH_CONST.__objc_const: 0x3048
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__objc_intobj: 0x330
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_const: 0xe270
+  __DATA_CONST.__objc_selrefs: 0x7438
+  __DATA_CONST.__objc_arraydata: 0x868
+  __AUTH_CONST.__cfstring: 0x28500
+  __AUTH_CONST.__objc_const: 0x3090
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__objc_intobj: 0x390
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x958
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_classrefs: 0x6a0
+  __AUTH.__objc_data: 0x7a8
+  __DATA.__objc_classrefs: 0x6b0
   __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0xf88
+  __DATA.__objc_ivar: 0xfd0
   __DATA.__data: 0xd30
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x1860
-  __DATA_DIRTY.__bss: 0x330
+  __DATA.__bss: 0x90
+  __DATA_DIRTY.__objc_data: 0x1888
+  __DATA_DIRTY.__bss: 0x338
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimg4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2686F731-46F5-32F0-A260-FA824E4BC76A
-  Functions: 4896
-  Symbols:   15893
-  CStrings:  17285
+  UUID: 2D9B1ACA-8DBA-3719-87AE-F6D29388D7B0
+  Functions: 5075
+  Symbols:   16407
+  CStrings:  18062
 
Symbols:
+ +[DownloadManager getPallasUrl:assetType:]
+ +[MADAutoAssetAuthorizationPolicy _accessibleAssetTypes:containsAssetType:]
+ +[MADAutoAssetAuthorizationPolicy _allowListedAutoAssetTypes]
+ +[MADAutoAssetAuthorizationPolicy authorizationAssetTypeFromMessage:alreadyOnStateQueue:]
+ +[MADAutoAssetAuthorizationPolicy isConnection:authorizedForMessage:]
+ +[MADAutoAssetAuthorizationPolicy isConnection:authorizedForMessage:].cold.1
+ +[MADAutoAssetAuthorizationPolicy isConnectionAuthorized:]
+ +[MADAutoAssetAuthorizationPolicy issueSandboxExtensionForAuditToken:path:]
+ +[MADAutoAssetControlManager assetTypeForClientDomainName:forSetIdentifier:alreadyOnStateQueue:]
+ +[MADAutoAssetControlManager buildDirectivesSummary]
+ +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withJobInformation:withFirstClientName:]
+ +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justPatched:withJobInformation:withFirstClientName:]
+ +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:withJobInformation:withFirstClientName:]
+ +[MADAutoAssetControlManager preferenceActivityAggressiveAssetType]
+ +[MADAutoAssetControlManager preferenceActivityAggressiveIntervalSecs]
+ +[MADAutoAssetControlManager preferenceActivityHeightenedAssetType]
+ +[MADAutoAssetControlManager preferenceActivityHeightenedIntervalSecs]
+ +[MADAutoAssetControlManager preferenceAutoAssetNoPersistedOverflowLimit]
+ +[MADAutoAssetControlManager preferenceScheduledAsIfNotInternal]
+ +[MADAutoAssetControlManager stagerEliminatedSetConfiguration:]
+ +[MADAutoAssetLocker eliminateSetEndAllLocks:forClientDomainName:forAssetSetIdentifier:]
+ +[MADAutoAssetLookupCache clearLookupResultsForSetConfiguration:]
+ +[MADAutoAssetLookupCache clearLookupResultsForSetConfiguration:].cold.1
+ +[MADAutoAssetScheduler assetTypesAtAggressiveFrequency]
+ +[MADAutoAssetScheduler assetTypesAtHeightenedFrequency]
+ +[MADAutoAssetScheduler persistedEntryIDForClientDomain:forAssetSetIdentifier:]
+ +[MADAutoAssetScheduler resumeFromPersisted:]
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:]
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.1
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.2
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.3
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.4
+ +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.5
+ +[MADAutoAssetStager controlEliminateSetConfiguration:]
+ +[MADAutoAssetStager controlEliminateSetConfiguration:].cold.1
+ +[MANAutoAssetSetStatus _shortTermLockFilenameNormalizedComponent:]
+ +[MANAutoAssetSetStatus shortTermLockDirectory:forAssetSetIdentifier:]
+ +[MANAutoAssetSetStatus shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:]
+ +[SecureMobileAssetBundle assetIsSecureMobileAsset:]
+ -[ControlManager handleCommandGetPallasURL:]
+ -[DownloadManager clientIdentifierWithName:]
+ -[MADAutoAssetClientRequest clientRequestAuditToken]
+ -[MADAutoAssetControlManager _autoAssetJobProgressNewValidatedCurrentStatus:requiringProgress:]
+ -[MADAutoAssetControlManager _autoAssetJobProgressNewValidatedCurrentStatus:requiringProgress:].cold.1
+ -[MADAutoAssetControlManager _eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:]
+ -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:fromLocation:]
+ -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:fromLocation:].cold.1
+ -[MADAutoAssetControlManager _removeSetDeterminedToBeIncomplete:]
+ -[MADAutoAssetControlManager _shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:]
+ -[MADAutoAssetControlManager _shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:].cold.1
+ -[MADAutoAssetControlManager _shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:].cold.2
+ -[MADAutoAssetControlManager _shortTermCreateSymbolicLink:symbolicLinkFilename:linkedToFilename:forSetDescriptor:usingFileManager:]
+ -[MADAutoAssetControlManager _shortTermPersistSetStatus:forSetDescriptor:persistingSetStatus:toFilename:]
+ -[MADAutoAssetControlManager _shortTermSharedLockClose:forSetDescriptor:atomicInstanceFileDescriptor:]
+ -[MADAutoAssetControlManager _shortTermSharedLockOpenExclusive:forSetDescriptor:atomicInstanceFilename:error:]
+ -[MADAutoAssetControlManager _shortTermSharedLockRemove:removingSharedLockFilename:usingFileManager:removingDescription:]
+ -[MADAutoAssetControlManager _updateSandboxExtensionForResponse:responseError:clientRequest:alreadyOnStateQueue:]
+ -[MADAutoAssetControlManager action_EliminateStagerSetDone:error:]
+ -[MADAutoAssetControlManager action_EliminateStagerSetDone:error:].cold.1
+ -[MADAutoAssetControlManager action_EliminateStagerSetDone:error:].cold.2
+ -[MADAutoAssetControlManager action_IssueClientReplySetJob:error:].cold.1
+ -[MADAutoAssetControlManager action_QueueClientRequest:error:].cold.1
+ -[MADAutoAssetControlManager action_QueueClientRequest:error:].cold.2
+ -[MADAutoAssetControlManager action_QueueClientRequestBefore1st:error:].cold.1
+ -[MADAutoAssetControlManager action_QueueClientRequestBefore1st:error:].cold.2
+ -[MADAutoAssetControlManager action_RouteClientRequest:error:].cold.1
+ -[MADAutoAssetControlManager action_RouteClientRequest:error:].cold.2
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:]
+ -[MADAutoAssetControlManager atomicInstanceOverflowRemove:]
+ -[MADAutoAssetControlManager atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:historyOperation:]
+ -[MADAutoAssetControlManager atomicInstanceRemovedSetJob:removingForReason:historyOperation:]
+ -[MADAutoAssetControlManager atomicInstanceTrimOverflowAfterPersisting:]
+ -[MADAutoAssetControlManager atomicInstanceTrimOverflowAfterPersisting:].cold.1
+ -[MADAutoAssetControlManager buildReportedSetStatus:forClientDomainName:forSetIdentifier:forAtomicInstance:withFoundSetDescriptor:withSubAtomicInstance:reportingLocalContentURLs:]
+ -[MADAutoAssetControlManager buildShortTermLockError:code:description:forSetDescriptor:underlyingError:]
+ -[MADAutoAssetControlManager descriptorsDroppedOnStartup]
+ -[MADAutoAssetControlManager doSetAtomicEntries:matchOtherAtomicEntries:]
+ -[MADAutoAssetControlManager doesSetDescriptor:referenceAssetDescriptor:]
+ -[MADAutoAssetControlManager finishSetEliminateIfAwaitingUnlocked:forClientDomain:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager handleClientEliminateAllForAssetTypeRequest:].cold.1
+ -[MADAutoAssetControlManager handleClientEliminateAllForSelectorRequest:].cold.1
+ -[MADAutoAssetControlManager handleClientEliminateAllForSelectorRequest:].cold.2
+ -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.1
+ -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.2
+ -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.3
+ -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:]
+ -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:].cold.1
+ -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.1
+ -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.2
+ -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.3
+ -[MADAutoAssetControlManager isAnyAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:]
+ -[MADAutoAssetControlManager isAutoAssetBeingEliminated:]
+ -[MADAutoAssetControlManager isConnection:authorizedForMessage:]
+ -[MADAutoAssetControlManager isConnectionAuthorized:]
+ -[MADAutoAssetControlManager isSetIdentifierBeingEliminated:forClientDomainName:ofSetIdentifier:]
+ -[MADAutoAssetControlManager isSetIdentifierCurrentlyLocked:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager isShortTermLockableSetDescriptor:]
+ -[MADAutoAssetControlManager latestShortTermLockableAtomicInstanceForClientDomain:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager loadPersistedAtomicInstancesSupportingShortTermLocking]
+ -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors]
+ -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.1
+ -[MADAutoAssetControlManager persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:]
+ -[MADAutoAssetControlManager preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:].cold.1
+ -[MADAutoAssetControlManager preferenceActivityAggressiveAssetType]
+ -[MADAutoAssetControlManager preferenceActivityAggressiveIntervalSecs]
+ -[MADAutoAssetControlManager preferenceActivityHeightenedAssetType]
+ -[MADAutoAssetControlManager preferenceActivityHeightenedIntervalSecs]
+ -[MADAutoAssetControlManager preferenceAutoAssetNoPersistedOverflowLimit]
+ -[MADAutoAssetControlManager preferenceScheduledAsIfNotInternal]
+ -[MADAutoAssetControlManager removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:historyOperation:]
+ -[MADAutoAssetControlManager removeSetDescriptorDownloaded:fromLocation:checkingByInstance:regardlessOfLatest:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager removeShortTermLockingOfSetDescriptor:endingAll:error:]
+ -[MADAutoAssetControlManager removeShortTermLockingOfSetDescriptor:endingAll:error:].cold.1
+ -[MADAutoAssetControlManager setConfigurationCopy:]
+ -[MADAutoAssetControlManager setConfigurationForClientDomain:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager setConfigurationNewEntryIDForClientDomain:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:]
+ -[MADAutoAssetControlManager setConfigurationRefreshToVendFromPromoted:]
+ -[MADAutoAssetControlManager setDescriptorAllEntriesDownloaded:forSetDescriptor:loggingEntryExists:]
+ -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:]
+ -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:].cold.1
+ -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:].cold.2
+ -[MADAutoAssetControlManager setDescriptorEliminateMatching:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager setDescriptorsDroppedOnStartup:]
+ -[MADAutoAssetControlManager setIdentifierEliminate:usingEliminateTracker:whenCurrentlyLocked:beginningToEliminate:removingContent:]
+ -[MADAutoAssetControlManager setJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:]
+ -[MADAutoAssetControlManager setLockUsageMapForAtomicInstance:clientLockUsageMap:lockReason:]
+ -[MADAutoAssetControlManager setPreferenceActivityAggressiveAssetType:]
+ -[MADAutoAssetControlManager setPreferenceActivityAggressiveIntervalSecs:]
+ -[MADAutoAssetControlManager setPreferenceActivityHeightenedAssetType:]
+ -[MADAutoAssetControlManager setPreferenceActivityHeightenedIntervalSecs:]
+ -[MADAutoAssetControlManager setPreferenceAutoAssetNoPersistedOverflowLimit:]
+ -[MADAutoAssetControlManager setPreferenceScheduledAsIfNotInternal:]
+ -[MADAutoAssetControlManager setShortTermLockedByAtomicInstance:]
+ -[MADAutoAssetControlManager setShortTermLockedLatestByIdentifier:]
+ -[MADAutoAssetControlManager shortTermLockSetDescriptor:forSetDescriptor:]
+ -[MADAutoAssetControlManager shortTermLockedByAtomicInstance]
+ -[MADAutoAssetControlManager shortTermLockedLatestByIdentifier]
+ -[MADAutoAssetControlManager shouldAdoptJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:]
+ -[MADAutoAssetControlManager trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:]
+ -[MADAutoAssetControlManager trackShortTermLockedSetDescriptor:]
+ -[MADAutoAssetControlManager updateAssociatedNoVersionStatus:currentStatus:forAssetSelector:]
+ -[MADAutoAssetControlManager updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:matchingAssetVersion:fromLocation:]
+ -[MADAutoAssetControlManager updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:matchingAssetVersion:fromLocation:].cold.1
+ -[MADAutoAssetControlManager updateAutoAssetStatusForChosenDownloadedDescriptor:matchingAssetVersion:fromLocation:]
+ -[MADAutoAssetControlManager updateCurrentAssetStatus:currentStatus:forAssetSelector:forActiveJobUUID:matchingAssetVersion:downloadingDescriptor:baseForPatchDescriptor:]
+ -[MADAutoAssetControlManager updateCurrentAssetStatus:currentStatus:forAssetSelector:forActiveJobUUID:matchingAssetVersion:downloadingDescriptor:baseForPatchDescriptor:].cold.1
+ -[MADAutoAssetControlManager verifySetDescriptorIsLockable:fromLocation:notLocakableError:]
+ -[MADAutoAssetControlManagerParam initForSetConfiguration:]
+ -[MADAutoAssetEliminate awaitingUnlocked]
+ -[MADAutoAssetEliminate initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:awaitingUnlocked:]
+ -[MADAutoAssetEliminate initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:awaitingUnlocked:].cold.1
+ -[MADAutoAssetEliminate setAwaitingUnlocked:]
+ -[MADAutoAssetJob beingCanceled]
+ -[MADAutoAssetJob errorCodeForNoNewerContentFound]
+ -[MADAutoAssetJob replyToJobsWhenOperationFoundSame:forCheckAtomic:withLookupError:]
+ -[MADAutoAssetJob setBeingCanceled:]
+ -[MADAutoAssetLocker _autoAssetLockPolicyFromSetPolicy:]
+ -[MADAutoAssetLocker _autoAssetLockPolicyFromSetPolicy:].cold.1
+ -[MADAutoAssetLocker _endAllSetLocks:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetLocker _isSetAssetLock:forClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetScheduler _aggressiveIntervalSecs]
+ -[MADAutoAssetScheduler _assetTypeForAssetSelector:]
+ -[MADAutoAssetScheduler _decideTriggerIntervalSecs:forAssetSelector:]
+ -[MADAutoAssetScheduler _heightenedIntervalSecs]
+ -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:]
+ -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:].cold.1
+ -[MADAutoAssetScheduler _setConfigurationForAssetSelector:]
+ -[MADAutoAssetScheduler _trackSetConfigurations:]
+ -[MADAutoAssetScheduler schedulerIntervalAggressiveAssetTypes]
+ -[MADAutoAssetScheduler schedulerIntervalHeightenedAssetTypes]
+ -[MADAutoAssetScheduler setConfigurations]
+ -[MADAutoAssetScheduler setSchedulerIntervalAggressiveAssetTypes:]
+ -[MADAutoAssetScheduler setSchedulerIntervalHeightenedAssetTypes:]
+ -[MADAutoAssetScheduler setSetConfigurations:]
+ -[MADAutoAssetStager action_RememberEliminateDone:error:]
+ -[MADAutoAssetStager action_RememberSetEliminateDone:error:]
+ -[MADAutoAssetStager action_SetEliminateAvailableDecideEmpty:error:]
+ -[MADAutoAssetStager action_SetEliminateDecideMatch:error:]
+ -[MADAutoAssetStager action_SetEliminateDeterminingDecideMatch:error:]
+ -[MADAutoAssetStager action_SetEliminateDone:error:]
+ -[MADAutoAssetStager action_SetEliminateDoneStagedDecideEmpty:error:]
+ -[MADAutoAssetStager eliminationSetConfigurationCurrentJob]
+ -[MADAutoAssetStager notifyControlManagerEliminateDone:forAssetSelector:]
+ -[MADAutoAssetStager notifyControlManagerEliminateDone:forSetConfiguration:]
+ -[MADAutoAssetStager setEliminationSetConfigurationCurrentJob:]
+ -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:]
+ -[MADAutoAssetStagerParam initWithSetConfiguration:]
+ -[MADAutoAssetStagerParam setIdentifierConfiguration]
+ -[MADAutoSetAtomicInstance lockedSupportingShortTermLocking]
+ -[MADAutoSetAtomicInstance setLockedSupportingShortTermLocking:]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:]
+ -[MADAutoSetConfiguration latestAtomicInstanceToVend]
+ -[MADAutoSetConfiguration managesAssetSelector:]
+ -[MADAutoSetConfiguration setLatestAtomicInstanceToVend:]
+ -[MADAutoSetDescriptor atomicInstanceDownloadedNotified]
+ -[MADAutoSetDescriptor setAtomicInstanceDownloadedNotified:]
+ -[MADAutoSetJobInformation assignedAutoAssetUUID]
+ -[MADAutoSetJobInformation setAssignedAutoAssetUUID:]
+ -[MANAutoAssetSetPolicy setSupportingShortTermLocks:]
+ -[MANAutoAssetSetPolicy supportingShortTermLocks]
+ -[SecureMobileAssetBundle .cxx_destruct]
+ -[SecureMobileAssetBundle accessPath]
+ -[SecureMobileAssetBundle assetBundlePath]
+ -[SecureMobileAssetBundle beginAccess:error:]
+ -[SecureMobileAssetBundle cryptexPath]
+ -[SecureMobileAssetBundle depersonalize:]
+ -[SecureMobileAssetBundle endAccess:error:]
+ -[SecureMobileAssetBundle graft:]
+ -[SecureMobileAssetBundle graftPath]
+ -[SecureMobileAssetBundle graftdmgType]
+ -[SecureMobileAssetBundle initWithPath:]
+ -[SecureMobileAssetBundle isAccessible]
+ -[SecureMobileAssetBundle isGloballySigned]
+ -[SecureMobileAssetBundle isGraftedPath:]
+ -[SecureMobileAssetBundle isGrafted]
+ -[SecureMobileAssetBundle isPersonalized]
+ -[SecureMobileAssetBundle isSecureMobileAsset]
+ -[SecureMobileAssetBundle personalize:error:]
+ -[SecureMobileAssetBundle rootHashPath]
+ -[SecureMobileAssetBundle secureAssetDataPath]
+ -[SecureMobileAssetBundle secureInfoPlist]
+ -[SecureMobileAssetBundle ticketPath]
+ -[SecureMobileAssetBundle trustCachePath]
+ -[SecureMobileAssetBundle ungraft:]
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table153
+ GCC_except_table215
+ GCC_except_table230
+ GCC_except_table318
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table458
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table66
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table90
+ _AMAuthInstallUpdaterCryptex1MobileAssetSetInfo
+ _MABrainUtilityAllowUnpersonalizedSecureAssets
+ _MABrainUtilityCopyBoardId
+ _MABrainUtilityCopyCertificateSecurityMode
+ _MABrainUtilityCopyChipId
+ _MABrainUtilityCopyEcid
+ _MABrainUtilityCopySecurityDomain
+ _MABrainUtilityCopySigningFuse
+ _OBJC_CLASS_$_MADAutoAssetAuthorizationPolicy
+ _OBJC_CLASS_$_SecureMobileAssetBundle
+ _OBJC_IVAR_$_MADAutoAssetClientRequest._clientRequestAuditToken
+ _OBJC_IVAR_$_MADAutoAssetControlManager._descriptorsDroppedOnStartup
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceActivityAggressiveAssetType
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceActivityAggressiveIntervalSecs
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceActivityHeightenedAssetType
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceActivityHeightenedIntervalSecs
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceAutoAssetNoPersistedOverflowLimit
+ _OBJC_IVAR_$_MADAutoAssetControlManager._preferenceScheduledAsIfNotInternal
+ _OBJC_IVAR_$_MADAutoAssetControlManager._shortTermLockedByAtomicInstance
+ _OBJC_IVAR_$_MADAutoAssetControlManager._shortTermLockedLatestByIdentifier
+ _OBJC_IVAR_$_MADAutoAssetEliminate._awaitingUnlocked
+ _OBJC_IVAR_$_MADAutoAssetJob._beingCanceled
+ _OBJC_IVAR_$_MADAutoAssetScheduler._schedulerIntervalAggressiveAssetTypes
+ _OBJC_IVAR_$_MADAutoAssetScheduler._schedulerIntervalHeightenedAssetTypes
+ _OBJC_IVAR_$_MADAutoAssetScheduler._setConfigurations
+ _OBJC_IVAR_$_MADAutoAssetStager._eliminationSetConfigurationCurrentJob
+ _OBJC_IVAR_$_MADAutoAssetStagerParam._setIdentifierConfiguration
+ _OBJC_IVAR_$_MADAutoSetAtomicInstance._lockedSupportingShortTermLocking
+ _OBJC_IVAR_$_MADAutoSetConfiguration._latestAtomicInstanceToVend
+ _OBJC_IVAR_$_MADAutoSetDescriptor._atomicInstanceDownloadedNotified
+ _OBJC_IVAR_$_MADAutoSetJobInformation._assignedAutoAssetUUID
+ _OBJC_IVAR_$_MANAutoAssetSetPolicy._supportingShortTermLocks
+ _OBJC_IVAR_$_SecureMobileAssetBundle._assetBundlePath
+ _OBJC_METACLASS_$_MADAutoAssetAuthorizationPolicy
+ _OBJC_METACLASS_$_SecureMobileAssetBundle
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_CLASS_METHODS_MADAutoAssetAuthorizationPolicy
+ __OBJC_$_CLASS_METHODS_SecureMobileAssetBundle
+ __OBJC_$_INSTANCE_METHODS_SecureMobileAssetBundle
+ __OBJC_$_INSTANCE_VARIABLES_SecureMobileAssetBundle
+ __OBJC_$_PROP_LIST_SecureMobileAssetBundle
+ __OBJC_CLASS_RO_$_MADAutoAssetAuthorizationPolicy
+ __OBJC_CLASS_RO_$_SecureMobileAssetBundle
+ __OBJC_METACLASS_RO_$_MADAutoAssetAuthorizationPolicy
+ __OBJC_METACLASS_RO_$_SecureMobileAssetBundle
+ ___110+[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:]_block_invoke
+ ___142+[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withJobInformation:withFirstClientName:]_block_invoke
+ ___27-[MABrainUpdater schedule:]_block_invoke_2.368
+ ___27-[MABrainUpdater schedule:]_block_invoke_3.369
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.749
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.796
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.cold.1
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.845
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.845.cold.1
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.852
+ ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.857
+ ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.695
+ ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.715
+ ___64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.250
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.797
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.815
+ ___65+[MADAutoAssetLookupCache clearLookupResultsForSetConfiguration:]_block_invoke
+ ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1691
+ ___96+[MADAutoAssetControlManager assetTypeForClientDomainName:forSetIdentifier:alreadyOnStateQueue:]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_literal_global.1050
+ ___block_literal_global.1053
+ ___block_literal_global.1070
+ ___block_literal_global.1202
+ ___block_literal_global.1213
+ ___block_literal_global.1290
+ ___block_literal_global.1426
+ ___block_literal_global.1622
+ ___block_literal_global.1633
+ ___block_literal_global.1641
+ ___block_literal_global.1649
+ ___block_literal_global.1657
+ ___block_literal_global.1665
+ ___block_literal_global.1673
+ ___block_literal_global.1681
+ ___block_literal_global.1689
+ ___block_literal_global.1949
+ ___block_literal_global.1998
+ ___block_literal_global.233
+ ___block_literal_global.236
+ ___block_literal_global.239
+ ___block_literal_global.2506
+ ___block_literal_global.290
+ ___block_literal_global.304
+ ___block_literal_global.3348
+ ___block_literal_global.371
+ ___block_literal_global.518
+ ___block_literal_global.539
+ ___block_literal_global.664
+ ___block_literal_global.667
+ ___block_literal_global.676
+ ___block_literal_global.680
+ ___block_literal_global.686
+ ___block_literal_global.706
+ ___block_literal_global.710
+ ___block_literal_global.715
+ ___block_literal_global.717
+ ___block_literal_global.720
+ ___block_literal_global.724
+ ___block_literal_global.725
+ ___block_literal_global.746
+ ___block_literal_global.748
+ ___block_literal_global.749
+ ___block_literal_global.750
+ ___block_literal_global.796
+ ___block_literal_global.817
+ ___block_literal_global.865
+ ___block_literal_global.870
+ ___block_literal_global.877
+ ___block_literal_global.888
+ ___block_literal_global.907
+ ___block_literal_global.972
+ ___block_literal_global.977
+ ___isExternalPreReleaseAssetType_block_invoke
+ __securemobileassetbundle_log
+ __unnamed_array_storage.1210
+ __unnamed_array_storage.1900
+ __unnamed_array_storage.1989
+ __unnamed_array_storage.2250
+ __unnamed_array_storage.2251
+ __unnamed_array_storage.2256
+ __unnamed_array_storage.2257
+ __unnamed_array_storage.233
+ __unnamed_array_storage.2342
+ __unnamed_array_storage.2343
+ __unnamed_array_storage.746
+ __unnamed_array_storage.747
+ __unnamed_array_storage.763
+ __unnamed_array_storage.966
+ __unnamed_array_storage.974
+ __unnamed_array_storage.989
+ _isExternalPreReleaseAssetType
+ _isExternalPreReleaseAssetType.assetTypes
+ _isExternalPreReleaseAssetType.once
+ _kAMAuthInstallBuildIdentityCryptex1GenericDmg
+ _kAMAuthInstallBuildIdentityCryptex1GenericIntegrityCatalog
+ _kAMAuthInstallBuildIdentityCryptex1GenericTrustCache
+ _kAMAuthInstallBuildIdentityCryptex1GenericVolume
+ _kMobileAssetPreferencesAutoAssetActivityAggressiveAssetType
+ _kMobileAssetPreferencesAutoAssetActivityAggressiveIntervalSecs
+ _kMobileAssetPreferencesAutoAssetActivityHeightenedAssetType
+ _kMobileAssetPreferencesAutoAssetActivityHeightenedIntervalSecs
+ _kMobileAssetPreferencesAutoAssetNoPersistedOverflowLimit
+ _kMobileAssetPreferencesAutoAssetScheduledAsIfNotInternal
+ _objc_msgSend$_accessibleAssetTypes:containsAssetType:
+ _objc_msgSend$_aggressiveIntervalSecs
+ _objc_msgSend$_allowListedAutoAssetTypes
+ _objc_msgSend$_assetTypeForAssetSelector:
+ _objc_msgSend$_autoAssetJobProgressNewValidatedCurrentStatus:requiringProgress:
+ _objc_msgSend$_autoAssetLockPolicyFromSetPolicy:
+ _objc_msgSend$_decideTriggerIntervalSecs:forAssetSelector:
+ _objc_msgSend$_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:
+ _objc_msgSend$_heightenedIntervalSecs
+ _objc_msgSend$_isSetAssetLock:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$_preInstalledMakeDescriptorAvailable:fromLocation:
+ _objc_msgSend$_removeSetDeterminedToBeIncomplete:
+ _objc_msgSend$_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:
+ _objc_msgSend$_setConfigurationForAssetSelector:
+ _objc_msgSend$_shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:
+ _objc_msgSend$_shortTermCreateSymbolicLink:symbolicLinkFilename:linkedToFilename:forSetDescriptor:usingFileManager:
+ _objc_msgSend$_shortTermLockFilenameNormalizedComponent:
+ _objc_msgSend$_shortTermPersistSetStatus:forSetDescriptor:persistingSetStatus:toFilename:
+ _objc_msgSend$_shortTermSharedLockClose:forSetDescriptor:atomicInstanceFileDescriptor:
+ _objc_msgSend$_shortTermSharedLockOpenExclusive:forSetDescriptor:atomicInstanceFilename:error:
+ _objc_msgSend$_shortTermSharedLockRemove:removingSharedLockFilename:usingFileManager:removingDescription:
+ _objc_msgSend$_trackSetConfigurations:
+ _objc_msgSend$_updateSandboxExtensionForResponse:responseError:clientRequest:alreadyOnStateQueue:
+ _objc_msgSend$action_EliminateStagerSetDone:error:
+ _objc_msgSend$action_RememberEliminateDone:error:
+ _objc_msgSend$action_RememberSetEliminateDone:error:
+ _objc_msgSend$action_SetEliminateAvailableDecideEmpty:error:
+ _objc_msgSend$action_SetEliminateDecideMatch:error:
+ _objc_msgSend$action_SetEliminateDeterminingDecideMatch:error:
+ _objc_msgSend$action_SetEliminateDone:error:
+ _objc_msgSend$action_SetEliminateDoneStagedDecideEmpty:error:
+ _objc_msgSend$assetBundlePath
+ _objc_msgSend$assetIsSecureMobileAsset:
+ _objc_msgSend$assetTypeForClientDomainName:forSetIdentifier:alreadyOnStateQueue:
+ _objc_msgSend$assetTypesAtAggressiveFrequency
+ _objc_msgSend$assetTypesAtHeightenedFrequency
+ _objc_msgSend$assignedAutoAssetUUID
+ _objc_msgSend$atomicInstanceDownloadedNotified
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:
+ _objc_msgSend$atomicInstanceOverflowRemove:
+ _objc_msgSend$atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:historyOperation:
+ _objc_msgSend$atomicInstanceRemovedSetJob:removingForReason:historyOperation:
+ _objc_msgSend$atomicInstanceTrimOverflowAfterPersisting:
+ _objc_msgSend$authorizationAssetTypeFromMessage:alreadyOnStateQueue:
+ _objc_msgSend$awaitingUnlocked
+ _objc_msgSend$beingCanceled
+ _objc_msgSend$buildDirectivesSummary
+ _objc_msgSend$buildReportedSetStatus:forClientDomainName:forSetIdentifier:forAtomicInstance:withFoundSetDescriptor:withSubAtomicInstance:reportingLocalContentURLs:
+ _objc_msgSend$buildShortTermLockError:code:description:forSetDescriptor:underlyingError:
+ _objc_msgSend$clearLookupResultsForSetConfiguration:
+ _objc_msgSend$clientConnectionAuditToken
+ _objc_msgSend$clientIDRaw
+ _objc_msgSend$clientIdentifierWithName:
+ _objc_msgSend$controlEliminateSetConfiguration:
+ _objc_msgSend$createSymbolicLinkAtPath:withDestinationPath:error:
+ _objc_msgSend$descriptorsDroppedOnStartup
+ _objc_msgSend$doSetAtomicEntries:matchOtherAtomicEntries:
+ _objc_msgSend$doesSetDescriptor:referenceAssetDescriptor:
+ _objc_msgSend$eliminateSetEndAllLocks:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$eliminationSetConfigurationCurrentJob
+ _objc_msgSend$errorCodeForNoNewerContentFound
+ _objc_msgSend$finishSetEliminateIfAwaitingUnlocked:forClientDomain:forAssetSetIdentifier:
+ _objc_msgSend$firstObject
+ _objc_msgSend$getPallasUrl:assetType:
+ _objc_msgSend$graft:
+ _objc_msgSend$handleCommandGetPallasURL:
+ _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:
+ _objc_msgSend$hasDirectoryPath
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:
+ _objc_msgSend$initForSetConfiguration:
+ _objc_msgSend$initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:awaitingUnlocked:
+ _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$initWithSetConfiguration:
+ _objc_msgSend$isAnyAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:
+ _objc_msgSend$isAutoAssetBeingEliminated:
+ _objc_msgSend$isConnection:authorizedForMessage:
+ _objc_msgSend$isConnectionAuthorized:
+ _objc_msgSend$isSetIdentifierBeingEliminated:forClientDomainName:ofSetIdentifier:
+ _objc_msgSend$isSetIdentifierCurrentlyLocked:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$isShortTermLockableSetDescriptor:
+ _objc_msgSend$issueSandboxExtensionForAuditToken:path:
+ _objc_msgSend$latestAtomicInstanceToVend
+ _objc_msgSend$latestShortTermLockableAtomicInstanceForClientDomain:forAssetSetIdentifier:
+ _objc_msgSend$loadPersistedAtomicInstancesSupportingShortTermLocking
+ _objc_msgSend$loadPersistedCrossCheckTrimSetDescriptors
+ _objc_msgSend$lockedSupportingShortTermLocking
+ _objc_msgSend$managesAssetSelector:
+ _objc_msgSend$messageType
+ _objc_msgSend$notifyControlManagerEliminateDone:forAssetSelector:
+ _objc_msgSend$notifyControlManagerEliminateDone:forSetConfiguration:
+ _objc_msgSend$persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withJobInformation:withFirstClientName:
+ _objc_msgSend$persistForJobSelector:persistingJobDescriptor:justPatched:withJobInformation:withFirstClientName:
+ _objc_msgSend$persistForJobSelector:persistingJobDescriptor:withJobInformation:withFirstClientName:
+ _objc_msgSend$persistSecureCodedObject:forKey:shouldPersist:
+ _objc_msgSend$persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:
+ _objc_msgSend$persistedEntryIDForClientDomain:forAssetSetIdentifier:
+ _objc_msgSend$preferenceActivityAggressiveAssetType
+ _objc_msgSend$preferenceActivityAggressiveIntervalSecs
+ _objc_msgSend$preferenceActivityHeightenedAssetType
+ _objc_msgSend$preferenceActivityHeightenedIntervalSecs
+ _objc_msgSend$preferenceAutoAssetNoPersistedOverflowLimit
+ _objc_msgSend$preferenceScheduledAsIfNotInternal
+ _objc_msgSend$removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:historyOperation:
+ _objc_msgSend$removeSetDescriptorDownloaded:fromLocation:checkingByInstance:regardlessOfLatest:historyOperationAI:historyOperationSD:
+ _objc_msgSend$removeShortTermLockingOfSetDescriptor:endingAll:error:
+ _objc_msgSend$replyToJobsWhenOperationFoundSame:forCheckAtomic:withLookupError:
+ _objc_msgSend$resumeFromPersisted:
+ _objc_msgSend$scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:
+ _objc_msgSend$schedulerIntervalAggressiveAssetTypes
+ _objc_msgSend$schedulerIntervalHeightenedAssetTypes
+ _objc_msgSend$secureAssetDataPath
+ _objc_msgSend$setAssignedAutoAssetUUID:
+ _objc_msgSend$setAtomicInstanceDownloadedNotified:
+ _objc_msgSend$setAwaitingUnlocked:
+ _objc_msgSend$setBeingCanceled:
+ _objc_msgSend$setConfigurationCopy:
+ _objc_msgSend$setConfigurationForClientDomain:forAssetSetIdentifier:
+ _objc_msgSend$setConfigurationNewEntryIDForClientDomain:forAssetSetIdentifier:
+ _objc_msgSend$setConfigurationPersist:fromLocation:
+ _objc_msgSend$setConfigurationRefreshToVendFromPromoted:
+ _objc_msgSend$setDescriptorAllEntriesDownloaded:forSetDescriptor:loggingEntryExists:
+ _objc_msgSend$setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:
+ _objc_msgSend$setDescriptorEliminateMatching:forClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$setDescriptorsDroppedOnStartup:
+ _objc_msgSend$setEliminationSetConfigurationCurrentJob:
+ _objc_msgSend$setIdentifierConfiguration
+ _objc_msgSend$setIdentifierEliminate:usingEliminateTracker:whenCurrentlyLocked:beginningToEliminate:removingContent:
+ _objc_msgSend$setJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:
+ _objc_msgSend$setLatestAtomicInstanceToVend:
+ _objc_msgSend$setLockUsageMapForAtomicInstance:clientLockUsageMap:lockReason:
+ _objc_msgSend$setLockedSupportingShortTermLocking:
+ _objc_msgSend$setSupportingShortTermLocks:
+ _objc_msgSend$set_sourceApplicationBundleIdentifierForMobileAsset:
+ _objc_msgSend$shortTermLockDirectory:forAssetSetIdentifier:
+ _objc_msgSend$shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:
+ _objc_msgSend$shortTermLockSetDescriptor:forSetDescriptor:
+ _objc_msgSend$shortTermLockedByAtomicInstance
+ _objc_msgSend$shortTermLockedLatestByIdentifier
+ _objc_msgSend$shouldAdoptJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:
+ _objc_msgSend$stagerEliminatedSetConfiguration:
+ _objc_msgSend$supportingShortTermLocks
+ _objc_msgSend$trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:
+ _objc_msgSend$trackShortTermLockedSetDescriptor:
+ _objc_msgSend$ungraft:
+ _objc_msgSend$updateAssociatedNoVersionStatus:currentStatus:forAssetSelector:
+ _objc_msgSend$updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:matchingAssetVersion:fromLocation:
+ _objc_msgSend$updateAutoAssetStatusForChosenDownloadedDescriptor:matchingAssetVersion:fromLocation:
+ _objc_msgSend$updateCurrentAssetStatus:currentStatus:forAssetSelector:forActiveJobUUID:matchingAssetVersion:downloadingDescriptor:baseForPatchDescriptor:
+ _objc_msgSend$verifySetDescriptorIsLockable:fromLocation:notLocakableError:
+ _objc_msgSend$version
+ _safeAtomicWriteToPath
- +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withFirstClientName:]
- +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justPatched:withFirstClientName:]
- +[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:withFirstClientName:]
- +[MADAutoAssetLocker endedAllPreviousSetLocksByClient:forSetDescriptor:forLockReason:endError:]
- +[MADAutoAssetScheduler resumeFromPersisted]
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.1
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.2
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.3
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.4
- +[MADAutoSetEliminate supportsSecureCoding]
- -[MADAutoAssetControlManager _autoAssetJobProgressNewValidatedCurrentStatus:]
- -[MADAutoAssetControlManager _eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:]
- -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:].cold.1
- -[MADAutoAssetControlManager action_ResumeScheduler:error:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:forSetInfoInstance:asSubAtomicFrom:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:]
- -[MADAutoAssetControlManager atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:]
- -[MADAutoAssetControlManager atomicInstanceRemovedSetJob:removingForReason:]
- -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:]
- -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:].cold.1
- -[MADAutoAssetControlManager isAnyAssetEntryOnFilesystemForSetDescriptor:]
- -[MADAutoAssetControlManager loadPersistedRecoverLost]
- -[MADAutoAssetControlManager persistSetDescriptorDownloadedJob:fromLocation:]
- -[MADAutoAssetControlManager removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:]
- -[MADAutoAssetControlManager removeSetDescriptorDownloaded:fromLocation:]
- -[MADAutoAssetControlManager setDescriptorAllEntriesDownloaded:]
- -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:]
- -[MADAutoAssetControlManager updateAssociatedStatus:forActiveJobUUID:withLatestJobStatus:]
- -[MADAutoAssetControlManager updateAssociatedStatus:forActiveJobUUID:withLatestJobStatus:].cold.1
- -[MADAutoAssetControlManager updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:fromLocation:]
- -[MADAutoAssetControlManager updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:fromLocation:].cold.1
- -[MADAutoAssetEliminate initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:]
- -[MADAutoAssetEliminate initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:].cold.1
- -[MADAutoAssetJob replyToJobsWhenLockFoundSame:]
- -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:]
- -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:].cold.1
- -[MADAutoAssetStager action_RemeberEliminateDone:error:]
- -[MADAutoAssetStagerParam initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:]
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:inhibitingImpliedScheduling:]
- -[MADAutoSetEliminate .cxx_destruct]
- -[MADAutoSetEliminate activeJobsByUUID]
- -[MADAutoSetEliminate assetSelector]
- -[MADAutoSetEliminate awaitingSchedulerAck]
- -[MADAutoSetEliminate awaitingStagerAck]
- -[MADAutoSetEliminate clientRequest]
- -[MADAutoSetEliminate description]
- -[MADAutoSetEliminate encodeWithCoder:]
- -[MADAutoSetEliminate initWithAssetSelector:]
- -[MADAutoSetEliminate initWithClientRequest:]
- -[MADAutoSetEliminate initWithClientRequest:withAssetSelector:]
- -[MADAutoSetEliminate initWithClientRequest:withAssetSelector:].cold.1
- -[MADAutoSetEliminate initWithCoder:]
- -[MADAutoSetEliminate setActiveJobsByUUID:]
- -[MADAutoSetEliminate setAwaitingSchedulerAck:]
- -[MADAutoSetEliminate setAwaitingStagerAck:]
- -[MADAutoSetEliminate summary]
- GCC_except_table124
- GCC_except_table131
- GCC_except_table150
- GCC_except_table214
- GCC_except_table227
- GCC_except_table40
- GCC_except_table418
- GCC_except_table42
- GCC_except_table421
- GCC_except_table423
- GCC_except_table52
- GCC_except_table56
- GCC_except_table65
- GCC_except_table67
- GCC_except_table81
- GCC_except_table83
- GCC_except_table84
- _OBJC_CLASS_$_MADAutoSetEliminate
- _OBJC_IVAR_$_MADAutoSetEliminate._activeJobsByUUID
- _OBJC_IVAR_$_MADAutoSetEliminate._assetSelector
- _OBJC_IVAR_$_MADAutoSetEliminate._awaitingSchedulerAck
- _OBJC_IVAR_$_MADAutoSetEliminate._awaitingStagerAck
- _OBJC_IVAR_$_MADAutoSetEliminate._clientRequest
- _OBJC_METACLASS_$_MADAutoSetEliminate
- __OBJC_$_CLASS_METHODS_MADAutoSetEliminate
- __OBJC_$_CLASS_PROP_LIST_MADAutoSetEliminate
- __OBJC_$_INSTANCE_METHODS_MADAutoSetEliminate
- __OBJC_$_INSTANCE_VARIABLES_MADAutoSetEliminate
- __OBJC_$_PROP_LIST_MADAutoSetEliminate
- __OBJC_CLASS_PROTOCOLS_$_MADAutoSetEliminate
- __OBJC_CLASS_RO_$_MADAutoSetEliminate
- __OBJC_METACLASS_RO_$_MADAutoSetEliminate
- ___123+[MADAutoAssetControlManager persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withFirstClientName:]_block_invoke
- ___27-[MABrainUpdater schedule:]_block_invoke_2.344
- ___27-[MABrainUpdater schedule:]_block_invoke_3.345
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.690
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.734
- ___44+[MADAutoAssetScheduler resumeFromPersisted]_block_invoke.cold.1
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.782
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.782.cold.1
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.789
- ___58-[MADAutoAssetScheduler _registerForAndStartPushActivity:]_block_invoke.794
- ___61+[MADAutoAssetControlManager installAutoAssetWithDescriptor:]_block_invoke
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.671
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.691
- ___64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.226
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.773
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.791
- ___69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.1662
- ___90+[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]_block_invoke
- ___95+[MADAutoAssetLocker endedAllPreviousSetLocksByClient:forSetDescriptor:forLockReason:endError:]_block_invoke
- ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_literal_global.1005
- ___block_literal_global.1008
- ___block_literal_global.1025
- ___block_literal_global.1194
- ___block_literal_global.1267
- ___block_literal_global.1378
- ___block_literal_global.1593
- ___block_literal_global.1604
- ___block_literal_global.1612
- ___block_literal_global.1620
- ___block_literal_global.1628
- ___block_literal_global.1636
- ___block_literal_global.1644
- ___block_literal_global.1652
- ___block_literal_global.1660
- ___block_literal_global.1914
- ___block_literal_global.1963
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.2469
- ___block_literal_global.266
- ___block_literal_global.280
- ___block_literal_global.3039
- ___block_literal_global.347
- ___block_literal_global.494
- ___block_literal_global.515
- ___block_literal_global.640
- ___block_literal_global.643
- ___block_literal_global.652
- ___block_literal_global.656
- ___block_literal_global.659
- ___block_literal_global.662
- ___block_literal_global.670
- ___block_literal_global.682
- ___block_literal_global.687
- ___block_literal_global.689
- ___block_literal_global.693
- ___block_literal_global.699
- ___block_literal_global.700
- ___block_literal_global.726
- ___block_literal_global.728
- ___block_literal_global.772
- ___block_literal_global.793
- ___block_literal_global.823
- ___block_literal_global.828
- ___block_literal_global.844
- ___block_literal_global.856
- ___block_literal_global.876
- ___block_literal_global.951
- ___block_literal_global.956
- __unnamed_array_storage.1868
- __unnamed_array_storage.1954
- __unnamed_array_storage.209
- __unnamed_array_storage.2215
- __unnamed_array_storage.2216
- __unnamed_array_storage.2221
- __unnamed_array_storage.2222
- __unnamed_array_storage.2307
- __unnamed_array_storage.2308
- __unnamed_array_storage.725
- __unnamed_array_storage.726
- __unnamed_array_storage.945
- __unnamed_array_storage.953
- __unnamed_array_storage.968
- _getPallasUrl
- _getRepositoryDownloadsPath
- _kCFBundleIdentifierKey
- _moveTargetPathToDirectory
- _objc_msgSend$_autoAssetJobProgressNewValidatedCurrentStatus:
- _objc_msgSend$_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:
- _objc_msgSend$_preInstalledMakeDescriptorAvailable:
- _objc_msgSend$_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:
- _objc_msgSend$action_RemeberEliminateDone:error:
- _objc_msgSend$action_ResumeScheduler:error:
- _objc_msgSend$atomicInstanceForSetDescriptor:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:forSetInfoInstance:asSubAtomicFrom:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:
- _objc_msgSend$atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:
- _objc_msgSend$atomicInstanceRemovedSetJob:removingForReason:
- _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:inhibitingImpliedScheduling:
- _objc_msgSend$initFromClientLockReasonKey:
- _objc_msgSend$initWithClientRequest:withAssetSelector:
- _objc_msgSend$initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:
- _objc_msgSend$initWithContentsOfURL:error:
- _objc_msgSend$initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:
- _objc_msgSend$isAnyAssetEntryOnFilesystemForSetDescriptor:
- _objc_msgSend$loadPersistedRecoverLost
- _objc_msgSend$maintainingActiveJobStatus
- _objc_msgSend$persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withFirstClientName:
- _objc_msgSend$persistForJobSelector:persistingJobDescriptor:justPatched:withFirstClientName:
- _objc_msgSend$persistForJobSelector:persistingJobDescriptor:withFirstClientName:
- _objc_msgSend$persistSetDescriptorDownloadedJob:fromLocation:
- _objc_msgSend$removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:
- _objc_msgSend$removeSetDescriptorDownloaded:fromLocation:
- _objc_msgSend$replyToJobsWhenLockFoundSame:
- _objc_msgSend$scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:
- _objc_msgSend$setDescriptorAllEntriesDownloaded:
- _objc_msgSend$setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:
- _objc_msgSend$setJobInstanceKeyFromSetStatus:forLatestDownloaded:
- _objc_msgSend$trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:
- _objc_msgSend$updateAssociatedStatus:forActiveJobUUID:withLatestJobStatus:
- _objc_msgSend$updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:fromLocation:
- _objc_release_x10
CStrings:
+ "\x01\x1d"
+ "\n[ELIMINATE(STAGER)]{%{public}@} notifying auto-control-manager asset-selector eliminate done | assetSelector:%{public}@"
+ "\n[ELIMINATE] {_eliminateCompleteIfAllDone} [SUCCESS] done with asset-selector elimination | eliminateTracker:%{public}@ | MA_MILESTONE"
+ "\n[ELIMINATE] {_eliminateCompleteIfAllDone} checking whether done with elimination | eliminateTracker:%{public}@"
+ "\n[ELIMINATE] {_eliminateCompleteIfAllDone} no persisted descriptor entry yet entry already exists | eliminateTracker:%{public}@"
+ "\n[ELIMINATE] {_eliminateCompleteIfAllDone} not yet complete | eliminateTracker:%{public}@"
+ "\n[ELIMINATE]{%{public}@:removeCurrentJob} no active job withVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
+ "\n[ELIMINATE]{%{public}@:removeCurrentJob} no active job withoutVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
+ "\n[ELIMINATE]{QueueClientRequestBefore1st} [EliminationInProgress] in-progress elimination blocking new request | clientRequest:%{public}@"
+ "\n[ELIMINATE]{QueueClientRequest} [EliminationInProgress] in-progress elimination blocking new request | clientRequest:%{public}@"
+ "\n[ELIMINATE]{RouteClientRequest} [EliminationInProgress] in-progress elimination blocking new request | clientRequest:%{public}@"
+ "\n[ELIMINATE]{ScheduleJobs} [IGNORED] auto-asset being eliminated - scheduler trigger ignored | selector:%{public}@"
+ "\n[ELIMINATE]{StagerJobStartDownload} [EliminationInProgress] stager-job for auto-asset being eliminated | selector:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminateAllForAssetTypeRequest} no auto-asset-instance provided in client eliminate request | eventInfo:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminateAllForSelectorRequest} asset-selector missing asset-specifier when required for eliminate request | eventInfo:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminateAllForSelectorRequest} no auto-asset-instance provided in client eliminate request | eventInfo:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminatePromotedNeverLockedForSelectorRequest} [MissingParameter] asset-selector missing asset-specifier when required for eliminate request | eventInfo:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminatePromotedNeverLockedForSelectorRequest} [MissingParameter] asset-selector with asset-version not supported for eliminate request | eventInfo:%{public}@"
+ "\n[ELIMINATE]{handleClientEliminatePromotedNeverLockedForSelectorRequest} [MissingParameter] no auto-asset-instance provided in client eliminate request | eventInfo:%{public}@"
+ "\n[SET-CONFIGURATION]{%{public}@:setConfigurationCopy} unable to copy set-configuration | nextSetConfiguration:%{public}@"
+ "\n[SET-CONFIGURATION]{%{public}@:setConfigurationCopy} unable to load set-configuration | setConfigurationKey:%{public}@"
+ "\n[SET-ELIMINATE(STAGER)]{%{public}@} notifying auto-control-manager set-identifier eliminate done | setConfiguration:%{public}@"
+ "\n[SET-ELIMINATE] {_eliminateCompleteIfAllDone} [SUCCESS] done with set-identifier elimination | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:removeCurrentSetJob} no active job for clientDomainName:%{public}@ | setJobIdentifier:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} NOT eliminating | nextSetConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} eliminating | nextSetConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} unable to load persisted-set-configuration file | nextRemoveSetConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [BusyPerformingOperation] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [ResourceUnavailable] unable to allocate eliminate operation tracking entry"
+ "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [SUCCESS] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setIdentifierEliminate} AWAIT-UNLOCKED elimination operations in progress | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setIdentifierEliminate} [BEGIN] elimination operations in progress | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setIdentifierEliminate} [REMOVE-CONTENT] elimination operations in progress | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setIdentifierEliminate} [REMOVE-CONTENT] no elimination operations in progress | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:setIdentifierEliminate} eliminateTracker:%{public}@ | currentlyLocked:%{public}@ | beginEliminate:%{public}@ | removeContent:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:} no entryID | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} matched set-descriptor | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} unable to load persisted entry | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} unable to load set-descriptor | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
+ "\n[SET-ELIMINATE]{EliminateStagerSetDone} [InvalidInstance] not tracking eliminate for setConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{EliminateStagerSetDone} [TooManyEntries] duplicate stager indication for eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{IssueClientReplySetJob} [EliminationInProgress] set-identifier is being eliminated | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{QueueClientRequestBefore1st} [EliminationInProgress] in-progress elimination blocking new set-request | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{QueueClientRequest} [EliminationInProgress] in-progress elimination blocking new set-request | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{RouteClientRequest} [EliminationInProgress] in-progress elimination blocking new set-request | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{ScheduleSetJobs} [IGNORED] set-identifier being eliminated - scheduler trigger ignored | schedulerTriggered:%{public}@"
+ "\n[SET-ELIMINATE]{handleSetClientEliminateAtomicRequest} [MissingParameter] instance missing asset-set-identifier when required for eliminate request | eventInfo:%{public}@"
+ "\n[SET-ELIMINATE]{handleSetClientEliminateAtomicRequest} [MissingParameter] instance missing client-domain-name when required for eliminate request | eventInfo:%{public}@"
+ "\n[SET-ELIMINATE]{handleSetClientEliminateAtomicRequest} [MissingParameter] no instance provided in client eliminate request | eventInfo:%{public}@"
+ "\n[STARTUP-STATE] [AUTO-ASSET-VERSION:%{public}@] | build environment:%{public}@"
+ "\n[STARTUP-STATE] [PERSISTED] %{public}@\n[STARTUP-STATE] [CURRENT] %{public}@\n[STARTUP-STATE] [KNOWN] %{public}@\n[STARTUP-STATE] [DOWNLOADED] %{public}@\n[STARTUP-STATE] [ACTIVE] %{public}@"
+ "\n{chooseNewerSetDescriptor} decided left (fewer assets) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided left (newer all present no extra) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (fewer assets) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} decided right (newer all present no extra) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
+ "\n{chooseNewerSetDescriptor} setConfiguration:%{public}@"
+ "\x14\x11Q\x14"
+ "\x1f\f'"
+ "!"
+ "%@ found Pallas URL %@ for asset type %@"
+ "%@ requested Pallas URL for asset type %@"
+ "%@ requested when chosen downloaded descriptor not lockable"
+ "%@ requested when device is before first-unlock"
+ "%@ requested when specific atomic-instance not already downloaded"
+ "%@ requested when unable to load set-configuration"
+ "%@ requested when unable to locate already downloaded content"
+ "%@ | setDescriptor:%@ | atomicInstanceFilename:%@ | specific:%@ | latest:%@ | setDescriptorCurrentStatus:%@ | error:%@"
+ "%@/%@/%@/%@"
+ "%@/%@/%@/%@/%@_%@.%@"
+ "%@:_removeSetDeterminedToBeIncomplete"
+ "%@:_shortTermChangeAtomicInstance"
+ "%@:_shortTermCreateSymbolicLink"
+ "%@:_shortTermPersistSetStatus"
+ "%@:_shortTermSharedLockOpenExclusive"
+ "%@:removeCurrentSetJob"
+ "%@:setDescriptorEliminateMatching"
+ "%@:setJobFoundAllContent"
+ "%@:shortTermLockSetDescriptor"
+ "%@:shouldAdoptJobFoundAllContent"
+ "%@:verifySetDescriptorIsLockable"
+ "%s: Atomic write to path failed and failed to remove temp path(%@): %@"
+ "%s: Failed to write item to path %@"
+ "%{public}@ | {AUTO-SCHEDULER:_decideTriggerIntervalSecs} aggressive | assetSelector:%{public}@ | scheduledJobAssetType:%{public}@ | determinedIntervalSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:_decideTriggerIntervalSecs} default | assetSelector:%{public}@ | scheduledJobAssetType:%{public}@ | determinedIntervalSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:_decideTriggerIntervalSecs} heightened | assetSelector:%{public}@ | scheduledJobAssetType:%{public}@ | determinedIntervalSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:_decideTriggerIntervalSecs} internal image | assetSelector:%{public}@ | scheduledJobAssetType:%{public}@ | determinedIntervalSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:_decideTriggerIntervalSecs} preference-based | assetSelector:%{public}@ | scheduledJobAssetType:%{public}@ | determinedIntervalSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:_performActivityOperations} scheduler triggered push-job when no job awaiting push trigger | currentlyAwaiting:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_setConfigurationForAssetSelector} unable to access entry in self.setConfigurations | nextSetConfigurationKey:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_setConfigurationForAssetSelector} unable to access entry key in self.setConfigurations"
+ "%{public}@ | {AUTO-SCHEDULER:_trackSetConfigurations} unable to access entry in allDefinedSetConfigurations"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} removed not-configured entry:%{public}@ | assetSelector:%@"
+ "(NO_TARGETS_DEFINED)"
+ "+[DownloadManager getPallasUrl:assetType:]"
+ "-[SecureMobileAssetBundle depersonalize:]"
+ "-[SecureMobileAssetBundle graft:]"
+ "-[SecureMobileAssetBundle personalize:error:]"
+ "-[SecureMobileAssetBundle ungraft:]"
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "0206c249-b301-46e0-9d6a-23ce9c5d875d"
+ "2.1.6"
+ ":;,/\\?~%*|\"<>[](){}"
+ "?\x0f\x1f\x03\x11\"BC"
+ "@\"NSSet\""
+ "@136@0:8q16@24@32@40@48@56@64@72@80@88@96@104@112@120@128"
+ "@48@0:8@16q24@32@40"
+ "@56@0:8@16q24@32@40@48"
+ "@56@0:8{?=[8I]}16@48"
+ "@60@0:8@16@24@32@40@48B56"
+ "@68@0:8@16@24@32@40@48@56B64"
+ "@80@0:8@16q24@32@40@48@56@64@72"
+ "ADD_AI_FROM_PRE_INSTALLED  "
+ "ADD_AI_FROM_SATISFYING     "
+ "ADD_AI_FROM_STAGED_DESCR   "
+ "ADD_AI_PROMOTED_STARTUP    "
+ "ADD_AI_RECOVER_LOST        "
+ "ADD_AI_ROUTING_NEW_SET_JOB "
+ "ADD_AI_SCHEDULER_TRIGGERED "
+ "ADD_AI_SUB_ATOMIC_0_ENTRIES"
+ "ADD_AI_SUB_ATOMIC_W_ENTRIES"
+ "ADD_SD_DOWNLOADED_OR_SAME  "
+ "ADD_SD_FROM_ALREADY_DWNLDED"
+ "ADD_SD_FROM_OTHR_SATISFYING"
+ "ADD_SD_FROM_STAGED_DESCR   "
+ "ADD_SD_PRE_INSTALLED       "
+ "ADD_SD_PROMOTED_STARTUP    "
+ "ADD_SD_ROUTING_NEW_SET_JOB "
+ "AMAuthInstallUpdaterCryptex1MobileAssetSetInfo"
+ "ATOMIC_INSTANCE_ELIMINATED"
+ "ATOMIC_INSTANCE_FIRST_LOCKED"
+ "ActiveJobs:%ld | KnownDescriptors:%ld | Locks:%ld | Scheduled:%ld | Staged:%ld | SetConfigurations:%ld | AtomicInstances:%ld | ActiveSetDescriptors:%ld | DownloadedSetDescriptors:%ld | SetTargets:%ld | SetLookupResults:%ld"
+ "AutoAssetActivityAggressiveAssetType"
+ "AutoAssetActivityAggressiveIntervalSecs"
+ "AutoAssetActivityHeightenedAssetType"
+ "AutoAssetActivityHeightenedIntervalSecs"
+ "AutoAssetNoPersistedOverflowLimit"
+ "AutoAssetScheduledAsIfNotInternal"
+ "B24@0:8@\"NSXPCConnection\"16"
+ "B32@0:8@\"NSXPCConnection\"16@\"SUCoreConnectMessage\"24"
+ "B32@0:8q16^@24"
+ "Completed end of all atomic-locks of auto-asset-set for MA_END_ATOMIC_LOCKS_ALL_INSTANCES request"
+ "ControlEliminateSetIdentifier"
+ "DEL_AI_CROSS_CHECK_TRIM    "
+ "DEL_AI_DISCOVERED_NOT_DWNLD"
+ "DEL_AI_DROP_CROSS_CHK_TRIM "
+ "DEL_AI_DROP_CRSS_CHK_DESCRS"
+ "DEL_AI_DROP_FAIL_ALLOC     "
+ "DEL_AI_DROP_INCOMPLETE     "
+ "DEL_AI_DROP_LOAD_PERSISTED "
+ "DEL_AI_DROP_LOAD_SET_DESCRS"
+ "DEL_AI_DROP_OVERFLOW_TRIM_D"
+ "DEL_AI_DROP_UNLOCKED_OTHER "
+ "DEL_AI_ELIMINATE_LOAD_PERSD"
+ "DEL_AI_ELIMINATE_MATCH_SID "
+ "DEL_AI_ELIMINATE_RMV_CONTNT"
+ "DEL_AI_FAILED_ALLOCATION   "
+ "DEL_AI_NO_CONTENT_FILESYSTM"
+ "DEL_AI_OVERFLOW_TRIM       "
+ "DEL_AI_RMV_CURRENT_SET_JOB "
+ "DEL_AI_RMV_CURR_SET_JOB_2ND"
+ "DEL_AI_RMV_PREVIOUS_STAGED "
+ "DEL_SD_DROP_CRSS_CHK_DESCRS"
+ "DEL_SD_DROP_INCOMPLETE     "
+ "DEL_SD_DROP_LOAD_SET_DESCRS"
+ "DEL_SD_DROP_NO_LATEST_AI   "
+ "DEL_SD_DROP_OVERFLOW_TRIM_D"
+ "DEL_SD_DROP_UNLOCKED_OTHER "
+ "DEL_SD_ELIMINATE_DROP_MATCH"
+ "DEL_SD_ELIMINATE_LOAD_PERSD"
+ "DEL_SD_ELIMINATE_MATCH_SID "
+ "DEL_SD_ELIMINATE_RMV_CONTNT"
+ "DEL_SD_NO_CONTENT_FILESYSTM"
+ "DEL_SD_RMV_PREVIOUS_STAGED "
+ "DawnE"
+ "ELIMINATING_ALL_CLIENTS"
+ "EliminateStagerSetDone"
+ "FINAL"
+ "Failed to mark bundle(%@) as current brain."
+ "Failed to remove personalized bundle for %@: %@"
+ "Failed to ungraft secure asset data for %@: %@"
+ "Failed to write stagingName final path component(%@) to proposed path(%@)"
+ "INITIAL(again)"
+ "INITIAL(first)"
+ "Internal Build with External Pre Release"
+ "Invalid data passed to %s"
+ "Invalid path passed to %s"
+ "MAAutoAssetControl-all-asset-specifiers"
+ "MAAutoAssetControl-all-asset-types"
+ "MABrainUtilityCopyBoardId"
+ "MABrainUtilityCopyCertificateSecurityMode"
+ "MABrainUtilityCopyChipId"
+ "MABrainUtilityCopyEcid"
+ "MABrainUtilityCopySecurityDomain"
+ "MABrainUtilityCopySigningFuse"
+ "MADAutoAssetAuthorizationPolicy"
+ "MA_GET_PALLAS_URL"
+ "Personalized bundle cannot be removed while grafted"
+ "Proceeding on Tatsu authorization failure because unpersonalized secure assets are allowed: %@"
+ "RememberEliminateDone"
+ "RememberSetEliminateDone"
+ "SET_CONFIGURATION|setConfiguration:%@"
+ "SHORT-TERM"
+ "SHORT-TERM behavior change | supportingShortTermLocking:%@ | setAtomicInstance:%@"
+ "STARTUP_ACTIVATED"
+ "STA_STARTUP_ACTIVATED      "
+ "Secure MobileAsset"
+ "SecureAssetData"
+ "SecureMobileAsset did not contain a personalized entry for %@"
+ "SecureMobileAsset.dmg"
+ "SecureMobileAsset.integritycatalog"
+ "SecureMobileAsset.root_hash"
+ "SecureMobileAsset.trustcache"
+ "SecureMobileAssetAllowUnpersonalized"
+ "SecureMobileAssetBundle"
+ "SecureMobileAssetCryptex1Ticket.der"
+ "SecureMobileAssetErrorDomain"
+ "SetConfigurationsByIdentifier:%ld | SetAtomicInstancesByInstance:%ld"
+ "SetDescriptorsByIdentifier:%ld | SetDescriptorsByInstance:%ld"
+ "SetDescriptorsByInstance:%ld"
+ "SetEliminateAvailableDecideEmpty"
+ "SetEliminateDecideMatch"
+ "SetEliminateDeterminingDecideMatch"
+ "SetEliminateDone"
+ "SetEliminateDoneStagedDecideEmpty"
+ "SetJobsByIdentifier:%ld | SetStatusByInstance:%ld"
+ "StagerEliminatedConfiguration"
+ "Starting built-in MobileAsset brain built Feb 23 2024 00:22:18"
+ "Starting downloaded MobileAsset brain (version: %@) built Feb 23 2024 00:22:18"
+ "Successfully removed personalized bundle for %@"
+ "Successfully ungrafted secure asset data for %@"
+ "T@\"MADAutoSetConfiguration\",&,N,V_eliminationSetConfigurationCurrentJob"
+ "T@\"MADAutoSetConfiguration\",R,&,N,V_setIdentifierConfiguration"
+ "T@\"NSMutableArray\",&,N,V_descriptorsDroppedOnStartup"
+ "T@\"NSMutableDictionary\",&,N,V_setConfigurations"
+ "T@\"NSMutableDictionary\",&,N,V_shortTermLockedByAtomicInstance"
+ "T@\"NSMutableDictionary\",&,N,V_shortTermLockedLatestByIdentifier"
+ "T@\"NSSet\",&,N,V_schedulerIntervalAggressiveAssetTypes"
+ "T@\"NSSet\",&,N,V_schedulerIntervalHeightenedAssetTypes"
+ "T@\"NSString\",&,N,V_assignedAutoAssetUUID"
+ "T@\"NSString\",&,N,V_latestAtomicInstanceToVend"
+ "T@\"NSString\",&,N,V_preferenceActivityAggressiveAssetType"
+ "T@\"NSString\",&,N,V_preferenceActivityHeightenedAssetType"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_atomicInstanceDownloadedNotified"
+ "TB,N,V_awaitingUnlocked"
+ "TB,N,V_beingCanceled"
+ "TB,N,V_lockedSupportingShortTermLocking"
+ "TB,N,V_preferenceAutoAssetNoPersistedOverflowLimit"
+ "TB,N,V_preferenceScheduledAsIfNotInternal"
+ "TB,N,V_supportingShortTermLocks"
+ "Tq,N,V_preferenceActivityAggressiveIntervalSecs"
+ "Tq,N,V_preferenceActivityHeightenedIntervalSecs"
+ "T{?=[8I]},R,N,V_clientRequestAuditToken"
+ "UPDATE"
+ "WARNING: Using relaxed cryptex validation!!! (SecureMobileAssetAllowUnpersonalized=1)"
+ "WARNING: Using software coprocessor parameters override:\n%@"
+ "[%@|instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@(notified:%@)|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
+ "[%{public}@]\n[ASSET_STATUS][%{public}@] | statusKey:%{public}@ | currentStatus:%{public}@ | jobUUID:%{public}@ | downloading:%{public}@ | baseForPatch:%{public}@"
+ "[%{public}@]\n[ASSET_STATUS][ASSOCIATED] | statusKey:%{public}@ | currentStatus:%{public}@ "
+ "[%{public}@]\n[ASSET_STATUS][PROMOTED] | currentStatus:%{public}@ | jobUUID:N"
+ "[%{public}@]\n[ASSET_STATUS][REMOVED] | eliminateSelectorKey:%{public}@"
+ "[%{public}@]\n[ASSET_STATUS][REMOVED] | statusKey:%{public}@ | jobUUID:N"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} [WARNING] over threshold for atomic-instances by set-identifier (trimming) | setAtomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} atomic-instance without backing set-descriptor | removedOverflowAtomicInstance:%{public}@"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} over threshold for atomic-instances by set-identifier (unable to reduce) | setAtomicInstance:%{public}@"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} unable to allocate required resources"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} unable to determine persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} unable to determine previous status | entryID:%{public}@"
+ "[%{public}@]\n[OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} unable to load set-atomic-instance | entryID:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@e} (%{public}@) NOT removing by UUID | setAtomicInstanceUUID:%{public}@ | nextSetAtomicInstance:%{public}@"
+ "[%{public}@]\n[REMOVAL] {%{public}@} (%{public}@) removing by UUID | setAtomicInstanceUUID:%{public}@ | nextSetAtomicInstance:%{public}@"
+ "[%{public}@] {%{public}@:atomicInstanceNewSetAtomicInstance} not persisting sub-atomic-instance of 0 entries | setAtomicInstance:%{public}@"
+ "[%{public}@] {%{public}@:handleSetClientAlterEntriesRepresentingAtomicRequest} unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
+ "[%{public}@] {%{public}@:removeSetDescriptorDownloaded} unable to load persisted-set-descriptor file | downloadedSetDescriptor:%{public}@"
+ "[%{public}@] {%{public}@:setConfigurationPersist} unable to load persisted-set-configuration file | setConfiguration:%{public}@"
+ "[%{public}@] {%{public}@:trackSetDescriptor}\n[VEND] update to set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "[%{public}@] {%{public}@}\n[VEND] new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
+ "[%{public}@] {%{public}@} persist of set-descriptor that has previously issued atomic-instance downloaded notification | setJobDescriptor:%{public}@"
+ "[%{public}@] {_routeClientRequest}\n[CANCEL-SET-JOB] active set-job being canceled - not considering as active job | set-eventInfo:%{public}@"
+ "[%{public}@] {_updateSandboxExtensionForResponse} MADAutoAssetAuthorizationPolicy failed set sandbox extension for response message | assetType=%{public}@, path=%{public}@, responseMessage:%{public}@, clientRequest:%{public}@"
+ "[%{public}@] {_updateSandboxExtensionForResponse} MADAutoAssetAuthorizationPolicy not applicable for this message | responseMessage:%{public}@, responseError:%{public}@, clientRequest:%{public}@"
+ "[%{public}@] {_updateSandboxExtensionForResponse} MADAutoAssetAuthorizationPolicy not applicable on this base build (no clientConnectionAuditToken) | responseMessage:%{public}@, responseError:%{public}@, clientRequest:%{public}@"
+ "[%{public}@] {_updateSandboxExtensionForResponse} MADAutoAssetAuthorizationPolicy not available on this base build | responseMessage:%{public}@, responseError:%{public}@, clientRequest:%{public}@"
+ "[%{public}@] {_updateSandboxExtensionForResponse} MADAutoAssetAuthorizationPolicy successfully set sandbox extension for response message | assetType=%{public}@, path=%{public}@, responseMessage:%{public}@, clientRequest:%{public}@"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest}\n[ALTER] altered without change to auto-asset-entries | setInfoInstance:%{public}@"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest}\n[CANCEL-SET-JOB][ALTER] already canceling set-job | set-eventInfo:%{public}@"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest}\n[CANCEL-SET-JOB][ALTER] canceling active set-job | set-eventInfo:%{public}@"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest} [ALTER] unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} [WARNING] over threshold for atomic-instances by set-identifier (trimming) | setAtomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} atomic-instance without backing set-descriptor | removedOverflowAtomicInstance:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} over threshold for atomic-instances by set-identifier (unable to reduce) | setAtomicInstance:%{public}@"
+ "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} unable to determine persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
+ "[%{public}@] {loadPersistedDescriptors} encountered auto-asset-descriptor with metadata=nil | entryID:%{public}@"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} incomplete set-descriptor currently locked - dropped | setDescriptor:%{public}@"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} incomplete set-descriptor not currently locked - dropped | setDescriptor:%{public}@"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} just unlocked selectors:%ld"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} no selectors just unlocked"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} set-descriptor without latestDownloadedAtomicInstance - dropped | setDescriptor:%{public}@"
+ "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor has no downloaded asset - dropped | setDescriptor:%{public}@"
+ "[%{public}@] {locateSetDescriptorDownloadedPreferringByAtomicInstance}\n[VEND] new set-descriptor generated from staged set-descriptor | setConfiguration:%{public}@, fromStagedSetDescriptor:%{public}@"
+ "[%{public}@] {newSetDescriptorFromAlreadyDownloaded}\n[VEND] new set-descriptor from already downloaded | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
+ "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@\n#_%{public}@:(%{public}@) [%{public}@] | [%{public}@] intervalSecs:%{public}@ | remainingSecs:%{public}@ | requiringRetry:%{public}@ | setPolicy:%{public}@\n#_%{public}@:%{public}@"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|latestToVend:%@|inhibitScheduling:%@]"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[ALTER] incomplete set-eventInfo | set-eventInfo:%@"
+ "[ALTER] invalid set-eventInfo (instance:MISSING) | set-eventInfo:%@"
+ "[ALTER] invalid set-eventInfo (no set-identifier to be altered) | set-eventInfo:%@"
+ "[ALTER] no valid asset-entries to alter to | set-eventInfo:%@"
+ "[ALTER] unable to allocate set-configuration | set-eventInfo:%@"
+ "[ALTER] unable to load persisted-set-configuration file | set-eventInfo:%@"
+ "[AUTO-PRE-INSTALLED] {%{public}@:_preInstalledMakeDescriptorAvailable} attempted to migrate asset but not on filesystem | descriptor:%{public}@"
+ "[AUTO-PRE-INSTALLED] {%{public}@:_preInstalledMakeDescriptorAvailable} content on filesystem validated for migration | descriptor:%{public}@"
+ "[AUTO-PRE-INSTALLED] {%{public}@} found some asset-specifiers as pre-installed - returning found subset | setInstance:%{public}@"
+ "[AUTO-PRE-INSTALLED] {%{public}@} unable to allocate set-descriptor | setInstance:%{public}@"
+ "[AUTO-SHORT-TERM][EXCLUSIVE]{%{public}@:_shortTermSharedLockClose} ERROR(%d) | errno:%d | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][EXCLUSIVE]{%{public}@:_shortTermSharedLockClose} SUCCESS(%d) | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][EXCLUSIVE]{%{public}@} ERROR(%d) | atomicInstanceFilename:%{public}@ | returnedError:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][EXCLUSIVE]{%{public}@} SUCCESS(%d) | atomicInstanceFilename:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][FILE]{%{public}@} created SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][FILE]{_shortTermPersistSetStatus} created SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@ | setStatus:%{public}@ "
+ "[AUTO-SHORT-TERM][INSTANCE]{removeShortTermLockingOfSetDescriptor} from clientLockUsageMap, currently held standard locks:%d | latestShortTermLockableAtomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][INSTANCE]{removeShortTermLockingOfSetDescriptor} no longer supporting SHORT-TERM locking | atomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][INSTANCE]{removeShortTermLockingOfSetDescriptor} unable to end SHORT-TERM locking (considering as no shared locks) | nextAtomicInstance:%{public}@ | setDescriptor:%{public}@ | underlyingError:%{public}@"
+ "[AUTO-SHORT-TERM][INSTANCE]{removeShortTermLockingOfSetDescriptor} unable to end SHORT-TERM locking (shared lock held) | nextAtomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][INSTANCE]{trackShortTermLockedSetDescriptor} now supporting SHORT-TERM locking | atomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][LATEST]{removeShortTermLockingOfSetDescriptor} latest removed when older supporting SHORT-TERM locking | atomicInstance:%{public}@ | otherSetDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][LATEST]{removeShortTermLockingOfSetDescriptor} no longer supporting SHORT-TERM locking | shortTermLockedKey:%{public}@ | otherSetDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][LATEST]{removeShortTermLockingOfSetDescriptor} removed latest | shortTermLatestLockedKey:%{public}@"
+ "[AUTO-SHORT-TERM][LATEST]{trackShortTermLockedSetDescriptor} latest supporting SHORT-TERM locking | atomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SUPPORT]{%{public}@} ERROR preparing for SHORT-TERM locking | error:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SUPPORT]{%{public}@} SUCCESS preparing for SHORT-TERM locking | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SUPPORT]{removeShortTermLockingOfSetDescriptor} ERROR removing SHORT-TERM locking | error:%{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SUPPORT]{removeShortTermLockingOfSetDescriptor} SUCCESS removing SHORT-TERM locking | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SYMLINK]{%{public}@:_shortTermCreateSymbolicLink} created SHORT-TERM locking symlink | %{public}@ >=> %{public}@ | setDescriptor:%{public}@"
+ "[AUTO-SHORT-TERM][SYMLINK]{_shortTermCreateSymbolicLink} unable to remove symlink (normal if no symlink yet created) | symbolicLinkFilename:%{public}@ | error:%{public}@"
+ "[AUTO-SHORT-TERM]{%{public}@:_shortTermSharedLockRemove} WARNING unable to remove %{public}@ | sharedLockFilename:%{public}@ | removeError:%{public}@"
+ "[AUTO-SHORT-TERM]{%{public}@:_shortTermSharedLockRemove} attempted to remove %{public}@ [did not exist] | sharedLockFilename:%{public}@"
+ "[AUTO-SHORT-TERM]{%{public}@:_shortTermSharedLockRemove} removed %{public}@ | sharedLockFilename:%{public}@"
+ "[AUTO-SHORT-TERM]{%{public}@} WARNING unable to load atomic-instance persisted-state entry | atomicInstance:%{public}@"
+ "[AUTO-SHORT-TERM]{%{public}@} no atomic-instance provided"
+ "[SMA] %s"
+ "[clientName:%@|SubAtomic:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[clientName:%@|setEntries:%ld|latestToVend:%@|inhibitScheduling:%@]"
+ "[clientRequest:%@|clientDomain:%@|setIdentifier:%@|awaitingUnlocked:%@|awaitingSchedulerAck:%@|awaitingCancelActivityAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@|limitedToCancelActivity:%@]"
+ "[initialSelector:%@|fullSelector:%@|clientInstance:%@|clientDesire:%@|foundContent:%@|currentStatus:%@]"
+ "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@(notified:%@)|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
+ "[overall]instance:%@,selector:%@,UUID:%@,logger:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@"
+ "_accessibleAssetTypes:containsAssetType:"
+ "_aggressiveIntervalSecs"
+ "_allowListedAutoAssetTypes"
+ "_assetBundlePath"
+ "_assetTypeForAssetSelector:"
+ "_assignedAutoAssetUUID"
+ "_atomicInstanceDownloadedNotified"
+ "_autoAssetJobProgressNewValidatedCurrentStatus:requiringProgress:"
+ "_autoAssetLockPolicyFromSetPolicy:"
+ "_awaitingUnlocked"
+ "_beingCanceled"
+ "_clientRequestAuditToken"
+ "_decideTriggerIntervalSecs:forAssetSelector:"
+ "_descriptorsDroppedOnStartup"
+ "_eliminateAtomicTriggeredByClient(awaitUnlocked:%@)"
+ "_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:"
+ "_eliminateAtomicTriggeredWhileLoading"
+ "_eliminationSetConfigurationCurrentJob"
+ "_endAllSetLocks:forClientDomainName:forAssetSetIdentifier:"
+ "_heightenedIntervalSecs"
+ "_isSetAssetLock:forClientDomainName:forAssetSetIdentifier:"
+ "_latestAtomicInstanceToVend"
+ "_lockedSupportingShortTermLocking"
+ "_preInstalledMakeDescriptorAvailable:fromLocation:"
+ "_preferenceActivityAggressiveAssetType"
+ "_preferenceActivityAggressiveIntervalSecs"
+ "_preferenceActivityHeightenedAssetType"
+ "_preferenceActivityHeightenedIntervalSecs"
+ "_preferenceAutoAssetNoPersistedOverflowLimit"
+ "_preferenceScheduledAsIfNotInternal"
+ "_removeSetDeterminedToBeIncomplete:"
+ "_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:"
+ "_schedulerIntervalAggressiveAssetTypes"
+ "_schedulerIntervalHeightenedAssetTypes"
+ "_securemobileassetbundle_log"
+ "_setConfigurationForAssetSelector:"
+ "_setIdentifierConfiguration"
+ "_shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:"
+ "_shortTermCreateSymbolicLink:symbolicLinkFilename:linkedToFilename:forSetDescriptor:usingFileManager:"
+ "_shortTermLockFilenameNormalizedComponent:"
+ "_shortTermLockedByAtomicInstance"
+ "_shortTermLockedLatestByIdentifier"
+ "_shortTermPersistSetStatus:forSetDescriptor:persistingSetStatus:toFilename:"
+ "_shortTermSharedLockClose:forSetDescriptor:atomicInstanceFileDescriptor:"
+ "_shortTermSharedLockOpenExclusive:forSetDescriptor:atomicInstanceFilename:error:"
+ "_shortTermSharedLockRemove:removingSharedLockFilename:usingFileManager:removingDescription:"
+ "_supportingShortTermLocks"
+ "_trackSetConfigurations:"
+ "_updateSandboxExtensionForResponse:responseError:clientRequest:alreadyOnStateQueue:"
+ "accessPath"
+ "action_EliminateStagerSetDone:error:"
+ "action_RememberEliminateDone:error:"
+ "action_RememberSetEliminateDone:error:"
+ "action_SetEliminateAvailableDecideEmpty:error:"
+ "action_SetEliminateDecideMatch:error:"
+ "action_SetEliminateDeterminingDecideMatch:error:"
+ "action_SetEliminateDone:error:"
+ "action_SetEliminateDoneStagedDecideEmpty:error:"
+ "assetBundlePath"
+ "assetIsSecureMobileAsset:"
+ "assetTypeForClientDomainName:forSetIdentifier:alreadyOnStateQueue:"
+ "assetTypesAtAggressiveFrequency"
+ "assetTypesAtHeightenedFrequency"
+ "assignedAutoAssetUUID"
+ "atomic-instance shared lock atomic-instance (eliminated set-identifier)"
+ "atomic-instance shared lock directory (eliminated set-identifier)"
+ "atomic-instance shared lock directory (no more SHORT-TERM locking support for the set-identifier)"
+ "atomic-instance shared lock file (just removed from supporting SHORT-TERM locking)"
+ "atomic-instance shared lock file (no other atomic-instance supporting SHORT-TERM locking)"
+ "atomic-instance shared lock file removed (eliminated set-identifier)"
+ "atomic-instance shared lock removed (eliminated set-identifier)"
+ "atomic-instance symlink file (to re-attempt symlink on standard-unlock of newest)"
+ "atomicInstanceDownloadedNotified"
+ "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:"
+ "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:"
+ "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:"
+ "atomicInstanceOverflowRemove:"
+ "atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:historyOperation:"
+ "atomicInstanceRemovedSetJob:removingForReason:historyOperation:"
+ "atomicInstanceTrimOverflowAfterPersisting"
+ "atomicInstanceTrimOverflowAfterPersisting:"
+ "atomic_instance"
+ "authorizationAssetTypeFromMessage:alreadyOnStateQueue:"
+ "awaitingUnlocked"
+ "beginAccess:error:"
+ "beingCanceled"
+ "buildDirectivesSummary"
+ "buildReportedSetStatus:forClientDomainName:forSetIdentifier:forAtomicInstance:withFoundSetDescriptor:withSubAtomicInstance:reportingLocalContentURLs:"
+ "buildShortTermLockError:code:description:forSetDescriptor:underlyingError:"
+ "checkAtomic (NO_WAIT) requested specific atomic-instance not valid for given set-identifier"
+ "checkAtomic (NO_WAIT) requested when no already downloaded asset-version available"
+ "checkAtomic (NO_WAIT) requested when no latest atomic-instance to vend (and failed to locate set-descriptor satisfying [or build from pre-SU-staged]) (and not pre-installed)"
+ "checkAtomic (NO_WAIT) unable to load set-configuration"
+ "clearLookupResultsForSetConfiguration:"
+ "clientConnectionAuditToken"
+ "clientIDRaw"
+ "clientIdentifierWithName:"
+ "clientRequestAuditToken"
+ "com.apple.MobileAsset.LinguisticDataAuto"
+ "com.apple.MobileAsset.MAAutoAsset"
+ "com.apple.MobileAsset.OSEligibility"
+ "com.apple.MobileAsset.Trial.Siri."
+ "com.apple.MobileAsset.UAF.Siri."
+ "com.apple.MobileAsset.UAF.Siri.DialogAssets"
+ "com.apple.MobileAsset.UAF.Siri.FindMyConfigurationFiles"
+ "com.apple.MobileAsset.UAF.Siri.PlatformAssets"
+ "com.apple.MobileAsset.UAF.Siri.SiriResponseFramework"
+ "com.apple.MobileAsset.UAF.Siri.TextToSpeech"
+ "com.apple.MobileAsset.UAF.Siri.Understanding"
+ "com.apple.MobileAsset.UAF.Siri.UnderstandingASRHammer"
+ "com.apple.MobileAsset.UAF.Siri.UnderstandingNLOverrides"
+ "com.apple.MobileAsset.UAF.sage.IFPlannerOverrides"
+ "com.apple.mobileassetd.client.%@"
+ "com.asset.MobileAsset."
+ "com.asset.MobileAsset.*"
+ "controlEliminateSetConfiguration:"
+ "createSymbolicLinkAtPath:withDestinationPath:error:"
+ "depersonalize:"
+ "descriptorsDroppedOnStartup"
+ "doSetAtomicEntries:matchOtherAtomicEntries:"
+ "doesSetDescriptor:referenceAssetDescriptor:"
+ "downloaded set-descriptor no longer referencing content on the filesystem (newer exists)"
+ "dropping to avoid overflow"
+ "eliminate-atomic when already eliminating (and not changing from soft to hard eliminate) | eliminateSelector:%@"
+ "eliminateSetEndAllLocks:forClientDomainName:forAssetSetIdentifier:"
+ "eliminationSetConfigurationCurrentJob"
+ "endAccess:error:"
+ "errorCodeForNoNewerContentFound"
+ "failed to end SHORT-TERM locking of set-descriptor"
+ "failed to end all locks due to SHORT-TERM locks"
+ "failed to end standard-lock due to SHORT-TERM locks"
+ "finishSetEliminateIfAwaitingUnlocked:forClientDomain:forAssetSetIdentifier:"
+ "firstObject"
+ "found auto-asset without localContentURL and/or assetAttributes in response message"
+ "getPallasUrl:assetType:"
+ "handleCommandGetPallasURL:"
+ "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:"
+ "handleSetClientLockAtomic"
+ "hard-eliminate completed (pending soft-eliminate should also have completed)"
+ "hasDirectoryPath"
+ "i40@0:8@16@24@32"
+ "incomplete set-descriptor atomic-instance"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:"
+ "initForSetConfiguration:"
+ "initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:awaitingUnlocked:"
+ "initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withSetIdentifierConfiguration:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:"
+ "initWithSet:"
+ "initWithSetConfiguration:"
+ "insufficient memory to perform removal"
+ "isAccessible"
+ "isAnyAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:"
+ "isAutoAssetBeingEliminated:"
+ "isConnection:authorizedForMessage:"
+ "isConnectionAuthorized:"
+ "isSecureMobileAsset"
+ "isSetIdentifierBeingEliminated:forClientDomainName:ofSetIdentifier:"
+ "isSetIdentifierCurrentlyLocked:forClientDomainName:forAssetSetIdentifier:"
+ "isShortTermLockableSetDescriptor:"
+ "issueSandboxExtensionForAuditToken:path:"
+ "latest"
+ "latestAtomicInstanceToVend"
+ "latestShortTermLockableAtomicInstanceForClientDomain:forAssetSetIdentifier:"
+ "loadPersistedAtomicInstancesSupportingShortTermLocking"
+ "loadPersistedCrossCheckTrimSetDescriptors"
+ "lock found descriptor MISSING required element(s) | chosenDownloadedDescriptor:%@"
+ "lockAtomic[NO_WAIT][SUPPORTING-SHORT-TERM]"
+ "lockAtomic[NO_WAIT_NOT_PERSISTED][SUPPORTING-SHORT-TERM]"
+ "lockAtomic[SUPPORTING-SHORT-TERM]"
+ "lockedSupportingShortTermLocking"
+ "locker"
+ "lockerType"
+ "managesAssetSelector:"
+ "messageType"
+ "notifyControlManagerEliminateDone:forAssetSelector:"
+ "notifyControlManagerEliminateDone:forSetConfiguration:"
+ "notifyLockerAsIndicatedBySetJob"
+ "persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withJobInformation:withFirstClientName:"
+ "persistForJobSelector:persistingJobDescriptor:justPatched:withJobInformation:withFirstClientName:"
+ "persistForJobSelector:persistingJobDescriptor:withJobInformation:withFirstClientName:"
+ "persistSecureCodedObject:forKey:shouldPersist:"
+ "persistSetDescriptorDownloadedJob:fromLocation:issuingDownloadedNotification:"
+ "persistedEntryIDForClientDomain:forAssetSetIdentifier:"
+ "personalize:error:"
+ "preferenceActivityAggressiveAssetType"
+ "preferenceActivityAggressiveIntervalSecs"
+ "preferenceActivityHeightenedAssetType"
+ "preferenceActivityHeightenedIntervalSecs"
+ "preferenceAutoAssetNoPersistedOverflowLimit"
+ "preferenceScheduledAsIfNotInternal"
+ "removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:historyOperation:"
+ "removeSetDescriptorDownloaded:fromLocation:checkingByInstance:regardlessOfLatest:historyOperationAI:historyOperationSD:"
+ "removeShortTermLockingOfSetDescriptor"
+ "removeShortTermLockingOfSetDescriptor:endingAll:error:"
+ "removed set-atomic-instance | removalReason:%@"
+ "removing previously persisted downloaded-set-descriptor that has been eliminated"
+ "removing previously persisted downloaded-set-descriptor that no longer had backing latest downloaded atomic-instance"
+ "replyToJobsWhenOperationFoundSame:forCheckAtomic:withLookupError:"
+ "resumeFromPersisted(NOT-CONFIGURED)"
+ "resumeFromPersisted:"
+ "resumeJobsWhenBeforeFirstUnlock(new jobDescriptor)"
+ "resumeJobsWhenBeforeFirstUnlock(nowDownloadedDescriptor)"
+ "safeAtomicWriteToPath"
+ "sandboxExtensionPathKey"
+ "scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:"
+ "schedulerIntervalAggressiveAssetTypes"
+ "schedulerIntervalHeightenedAssetTypes"
+ "scpParametersOverride"
+ "secureAssetDataPath"
+ "secureInfoPlist"
+ "set-descriptor not lockable"
+ "set-identifier is being eliminated"
+ "setAssignedAutoAssetUUID:"
+ "setAtomicInstanceDownloadedNotified:"
+ "setAwaitingUnlocked:"
+ "setBeingCanceled:"
+ "setConfigurationCopy:"
+ "setConfigurationForClientDomain:forAssetSetIdentifier:"
+ "setConfigurationNewEntryIDForClientDomain:forAssetSetIdentifier:"
+ "setConfigurationPersist:fromLocation:"
+ "setConfigurationRefreshToVendFromPromoted"
+ "setConfigurationRefreshToVendFromPromoted:"
+ "setDescriptorAllEntriesDownloaded:forSetDescriptor:loggingEntryExists:"
+ "setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:"
+ "setDescriptorEliminateMatching"
+ "setDescriptorEliminateMatching:forClientDomainName:forAssetSetIdentifier:"
+ "setDescriptorsDroppedOnStartup:"
+ "setEliminationSetConfigurationCurrentJob:"
+ "setIdentifierConfiguration"
+ "setIdentifierEliminate"
+ "setIdentifierEliminate:usingEliminateTracker:whenCurrentlyLocked:beginningToEliminate:removingContent:"
+ "setJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:"
+ "setLatestAtomicInstanceToVend:"
+ "setLockUsageMapForAtomicInstance:clientLockUsageMap:lockReason:"
+ "setLockedSupportingShortTermLocking:"
+ "setPreferenceActivityAggressiveAssetType:"
+ "setPreferenceActivityAggressiveIntervalSecs:"
+ "setPreferenceActivityHeightenedAssetType:"
+ "setPreferenceActivityHeightenedIntervalSecs:"
+ "setPreferenceAutoAssetNoPersistedOverflowLimit:"
+ "setPreferenceScheduledAsIfNotInternal:"
+ "setSchedulerIntervalAggressiveAssetTypes:"
+ "setSchedulerIntervalHeightenedAssetTypes:"
+ "setShortTermLockedByAtomicInstance:"
+ "setShortTermLockedLatestByIdentifier:"
+ "setSupportingShortTermLocks:"
+ "set_sourceApplicationBundleIdentifierForMobileAsset:"
+ "sharedLockSetStatus"
+ "shared_locks"
+ "shortTermLockDirectory:forAssetSetIdentifier:"
+ "shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:"
+ "shortTermLockSetDescriptor:forSetDescriptor:"
+ "shortTermLockedByAtomicInstance"
+ "shortTermLockedLatestByIdentifier"
+ "shouldAdoptJobFoundAllContent:forJobAtomicInstance:withCurrentSetStatus:"
+ "specific"
+ "stager-job for auto-asset being eliminated"
+ "stagerEliminatedSetConfiguration:"
+ "supportingShortTermLocks"
+ "trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:"
+ "trackShortTermLockedSetDescriptor"
+ "trackShortTermLockedSetDescriptor:"
+ "unable to allocate set-descriptor"
+ "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@"
+ "unable to create directory for SHORT-TERM locking | shortTermDirectory:%@"
+ "unable to create persisted-state for shared lock file | atomicInstanceFilename:%@ | firstLockedSetStatus:%@"
+ "unable to create shimmed set-status to write to shared lock file | atomicInstanceFilename:%@ | firstLockedSetStatus:%@"
+ "unable to create symbolic link for SHORT-TERM locking latest | %@ >=> %@"
+ "unable to load persisted-state for shared lock file | atomicInstanceFilename:%@ | firstLockedSetStatus:%@"
+ "unable to prepare for SHORT-TERM locking [MISSING-REQUIRED] | atomic-instance filenames (specific:%@,latest:%@,base:%@) | currentStatus:%@"
+ "updateAssociatedNoVersionStatus:currentStatus:forAssetSelector:"
+ "updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:matchingAssetVersion:fromLocation:"
+ "updateAutoAssetStatusForChosenDownloadedDescriptor:matchingAssetVersion:fromLocation:"
+ "updateCurrentAssetStatus:currentStatus:forAssetSelector:forActiveJobUUID:matchingAssetVersion:downloadingDescriptor:baseForPatchDescriptor:"
+ "v44@0:8@16@24@32B40"
+ "v44@0:8@16@24B32B36B40"
+ "v48@0:8@16B24B28@32q40"
+ "v56@0:8@16@24B32B36@40@48"
+ "v56@0:8@16@24B32B36q40q48"
+ "v64@0:8@16q24q32B40B44@48B56B60"
+ "v84@0:8@16@24B32@36@44B52B56B60B64q68@76"
+ "verifySetDescriptorIsLockable:fromLocation:notLocakableError:"
+ "version"
+ "{%@:_preInstalledMakeDescriptorAvailable} already migrated | availableToMigrate:%@, alreadyAvailable:%@"
+ "{%@:finishSetEliminateIfAwaitingUnlocked} set-identifier being eliminated yet no eliminateTracker | clientDomainName:%@ | assetSetIdentifier:%@ | %@"
+ "{%@:verifySetDescriptorIsLockable} MISSING required | setJobDescriptor:%@ | downloadedDescriptor:%@"
+ "{%@:verifySetDescriptorIsLockable} no downloaded atomic-instance entries | setJobDescriptor:%@"
+ "{%@:verifySetDescriptorIsLockable} no downloaded descriptor | setJobDescriptor:%@ | nextDownloadedAtomicEntry:%@"
+ "{%@:verifySetDescriptorIsLockable} not MAAutoAsset | setJobDescriptor:%@ | downloadedDescriptor:%@"
+ "{%@:verifySetDescriptorIsLockable} not on filesystem | setJobDescriptor:%@ | downloadedDescriptor:%@"
+ "{%@} no setConfiguration | setJobDescriptor:%@"
+ "{%@} set-job current-set-status did not include active atomic-instance | jobAtomicInstance:%@ | currentSetStatus:%@"
+ "{%@} set-job current-set-status does not include latestDowloadedEntries | downloadedAtomicInstance:%@ | latestDowloadedEntries:%ld | setJobDescriptor:%@ | currentSetStatus:%@"
+ "{%@} set-job current-set-status does not include latestDowloadedEntries | jobAtomicInstance:%@ | currentSetStatus:%@"
+ "{%@} set-job current-set-status has no set-configuration | jobAtomicInstance:%@ | currentSetStatus:%@"
+ "{%@} unable to determine set-descriptor for atomic-instance that should be currently symlinked | atomic-instance:%@"
+ "{%@} unable to obtain exclusive lock | errno:%d | atomicInstanceFilename:%@"
+ "{%{public}@} [CHECK-SET-DESCRIPTOR] checking set-descriptor | setDescriptor:%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing from filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry missing localContentURL | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@"
+ "{%{public}@} [DROP-SET-DESCRIPTOR] set-descriptor with downloaded entry that is not a directory | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} [KEEP-SET-DESCRIPTOR] set-descriptor with downloaded entry on filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} no entryID"
+ "{%{public}@} unable to load persisted entry | entryID:%{public}@"
+ "{%{public}@} unable to load set-descriptor | entryID:%{public}@"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"
+ "{AUTO-LOCKER:_autoAssetLockPolicyFromSetPolicy} | unable to allocate lockUsagePolicy | lockSetUsagePolicy:%{public}@"
+ "{AUTO-LOCKER:_endAllSetLocks} | unable to end auto-asset all-locks for set-identifier | orphanedLock:%{public}@ |  endedLocksAutoAssetError:%{public}@"
+ "{AUTO-LOOKUP-CACHE[CLIENT]:clearLookupResultsForSetConfiguration} | clearing auto-asset-lookup-cache | set-configuration:%{public}@"
+ "{AUTO-LOOKUP-CACHE[CLIENT]:clearLookupResultsForSetConfiguration} | removed stale auto-asset-lookup-cache entry | lookupCacheKey:%{public}@ | set-configuration:%{public}@"
+ "{AUTO-LOOKUP-CACHE[CLIENT]:clearLookupResultsForSetConfiguration} | unable to locate auto-asset-lookup-cache | set-configuration:%{public}@"
+ "{AUTO-SCHEDULER:init} AGGRESSIVE trigger frequency | schedulerIntervalAggressiveAssetTypes:\n%{public}@"
+ "{AUTO-SCHEDULER:init} HEIGHTENED trigger frequency | schedulerIntervalHeightenedAssetTypes:\n%{public}@"
+ "{AUTO-SCHEDULER:scheduleSetDomainName} no scheduling change | nil set-configuration provided"
+ "{EliminateStagerSetDone} duplicate stager indication for eliminateTracker:%@"
+ "{EliminateStagerSetDone} not tracking eliminate for setConfiguration:%@"
+ "{MADAutoAssetAuthorizationPolicy}(%{public}@) Client does not have requested asset type: %@ (found: %@)"
+ "{MADAutoAssetAuthorizationPolicy}(%{public}@) Request had no asset type listed for message: %{public}@"
+ "{MADAutoAssetAuthorizationPolicy}(authorizationAssetTypeFromMessage) Found asset type: %{public}@, for message: %{public}@"
+ "{MADAutoAssetAuthorizationPolicy}(authorizationAssetTypeFromMessage) Found multiple asset types: %{public}@, for message: %{public}@"
+ "{MADAutoAssetAuthorizationPolicy}(issueSandboxExtensionForAuditToken) Failed to set sandbox extension for audit token path: %{public}@"
+ "{MADAutoAssetAuthorizationPolicy}(issueSandboxExtensionForAuditToken) Set sandbox extension for audit token at path: %{public}@"
+ "{MADAutoAssetControlManager-updateCurrentAssetStatus} WARNING: wrong class provided as jobStatus"
+ "{_eliminateBegin} called for set eliminateTracker:%@"
+ "{controlEliminateSetConfiguration} failed to locate shared AutoAssetStager"
+ "{handleSetClientEndAtomicLocksForClientRequest} Ending all locks in all atomic and sub-atomic instances for domain: %{public}@, setID: %{public}@"
+ "{handleSetClientEndAtomicLocksForClientRequest} No lock is held when requesting to end all locks in all atomic and sub-atomic instances for domain: %{public}@, setID: %{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor with no latestDownloadedAtomicInstance | setDescriptor:%{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without atomic-instance | setDescriptor:%{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load persisted entry | entryID:%{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load set-descriptor | entryID:%{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [KEEP-SET-DESCRIPTOR] set-descriptor with atomic-instance | setDescriptor:%{public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} no entryID"
+ "{persistSetJobDescriptor}\n[SET-DESCRIPTOR][VEND] update to set-descriptor provided by set-job | setJobDescriptor:%{public}@"
+ "{replyToJobsWhenOperationFoundSame} no associated descriptor on filesystem (should always be there at this point)"
+ "{replyToJobsWhenOperationFoundSame} not valid for a stager-job"
+ "{updateLastFetchedDate} failed to update lastFetchedDate in xml | targetLocation:%@"
+ "|BUILDING_DAEMON"
+ "|TARGET_OS_IPHONE"
+ "|TARGET_OS_MAC"
+ "|lockInhibitsRemoval:%@|supportingShortTermLocks:%@|allowCheckDownload(OnBattery:%@,WhenBatteryLow:%@,WhenCPUHigh:%@,OverExpensive:%@,OverCellular:%@)|blockCheckDownload:%@|"
- "\x01\x1c"
- "\n{chooseNewerSetDescriptor} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\x14\x11Q\x11"
- "\x1f\f&"
- "%{public}@ | {AUTO-SCHEDULER:_performActivityOperations} scheduler triggered push-job when ho jos awaiting push trigger | currentlyAwaiting:%{public}@"
- "-[ControlManager getSAFRegistrationBundleID:]"
- "/\x0f\x1f\x11\"c"
- "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/downloadDir"
- "2.0.20"
- "@128@0:8q16@24@32@40@48@56@64@72@80@88@96@104@112@120"
- "AUTO-LOCKER:endedAllPreviousSetLocksByClient"
- "DawnD"
- "Failed to remove temporary files with error: %@"
- "Failed to update lastFetchedDate in xml"
- "MADAutoSetEliminate"
- "RECOVERED"
- "RemeberEliminateDone"
- "ResumeScheduler"
- "SAFBundleIdentifier"
- "Starting built-in MobileAsset brain built Dec 20 2023 18:39:24"
- "Starting downloaded MobileAsset brain (version: %@) built Dec 20 2023 18:39:24"
- "Unable to move current mabrain, returned %d errno: %d"
- "Unable to move proposed mabrain, returned %d errno: %d"
- "[%@|instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
- "[%{public}@]\n[REMOVAL] {%{public}@e} (%{public}@) NOT removing by UUID | nextSetAtomicInstance:%{public}@"
- "[%{public}@]\n[REMOVAL] {%{public}@} (%{public}@) removing by UUID | nextSetAtomicInstance:%{public}@"
- "[%{public}@] ASSOCIATED_STATUS | currentStatus:%{public}@"
- "[%{public}@] FINAL_STATUS | currentStatus:%{public}@"
- "[%{public}@] INITIAL_STATUS(%{public}@) | currentStatus:%{public}@ | jobUUID:%{public}@ | downloading:%{public}@ | baseForPatch:%{public}@"
- "[%{public}@] no auto-asset-job associated with selector (or job UUID) for auto-asset-stager related (status dropped) selector:%{public}@ | currentStatus:%{public}@"
- "[%{public}@] not yet maintaining active job status (status dropped) selector:%{public}@ | currentStatus:%{public}@"
- "[%{public}@] {%{public}@:handleSetClientAlterEntriesRepresentingAtomicRequest} unable to load persisted-set-configuration file | set-eventInfo::%{public}@"
- "[%{public}@] {%{public}@:removeSetDescriptorDownloadedByClientDomain} unable to load persisted-set-descriptor file | downloadedSetDescriptor:%{public}@"
- "[%{public}@] {%{public}@:setConfigurationEliminate} unable to load persisted-set-configuration file | nextRemoveSetConfiguration:%{public}@"
- "[%{public}@] {%{public}@:setConfigurationEliminate} | NOT eliminating nextSetConfiguration:%{public}@"
- "[%{public}@] {%{public}@:setConfigurationEliminate} | eliminating nextSetConfiguration:%{public}@"
- "[%{public}@] {%{public}@:setConfigurationNewSetConfiguration} unable to load persisted-set-configuration file | setConfiguration:%{public}@"
- "[%{public}@] {%{public}@:setDescriptorEliminate} all elimination operations in progress | eliminateTracker:%{public}@"
- "[%{public}@] {%{public}@} new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
- "[%{public}@] {_eliminateCompleteIfAllDone} checking whether done with elimination | eliminateTracker:%{public}@"
- "[%{public}@] {_eliminateCompleteIfAllDone} done with set-elimination | eliminateTracker:%{public}@"
- "[%{public}@] {_eliminateCompleteIfAllDone} eliminate complete | eliminateTracker:%{public}@ | MA_MILESTONE"
- "[%{public}@] {_eliminateCompleteIfAllDone} no persisted descriptor entry yet entry already exists | eliminateTracker:%{public}@"
- "[%{public}@] {_eliminateCompleteIfAllDone} not yet complete | eliminateTracker:%{public}@"
- "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest} unable to load persisted-set-configuration file | set-eventInfo::%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrimAtomicInstances} over threshold for atomic-instances by set-identifier | setAtomicInstance:%{public}@"
- "[%{public}@] {loadPersistedRecoverLost} successfully recovered lost atomic-instance | setDescriptor:%{public}@ | setAtomicInstance:%{public}@"
- "[%{public}@] {loadPersistedRecoverLost} unable to recover lost atomic-instance | setDescriptor:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} WARNING: some content on filesystem missing (still tracking locks) | entryID:%{public}@, adoptedSetDescriptor[locked,onFilesystemIncomplete]:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} content on filesystem incomplete (still tracking locks) | entryID:%{public}@, adoptedSetDescriptor[locked,onFilesystemIncomplete]:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} incomplete set-descriptor not currently locked - dropped | entryID:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} set-descriptor without latestDownloadedAtomicInstance - dropped | entryID:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor has no downloaded asset - dropped | entryID:%{public}@"
- "[%{public}@] {newSetDescriptorFromAlreadyDownloaded} new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
- "[%{public}@] {removeCurrentJob} no active job withVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
- "[%{public}@] {removeCurrentJob} no active job withoutVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
- "[%{public}@] {removeCurrentSetJob} no active job for clientDomainName:%{public}@ | setJobIdentifier:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
- "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@\n#_%{public}@:(%{public}@) [%{public}@] | [%{public}@] intervalSecs:%{public}@ | remaininSecs:%{public}@ | requiringRetry:%{public}@ | setPolicy:%{public}@\n#_%{public}@:%{public}@"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inhibitScheduling:%@]"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[AUTO-PRE-INSTALLED] {_preInstalledMakeDescriptorAvailable} attempted to migrate asset but not on filesystem | descriptor:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledMakeDescriptorAvailable} content on filesystem validated for migration | descriptor:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledSetAtomicEntriesFromInstanceEntries} unable to load auto-asset-descriptor | nextInstanceEntry:%{public}@"
- "[clientName:%@|SubAtomic:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[clientName:%@|setEntries:%ld|inhibitScheduling:%@]"
- "[clientRequest:%@|assetSelector:%@|awaitingSchedulerAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@]"
- "[clientRequest:%@|clientDomain:%@|setIdentifier:%@|awaitingSchedulerAck:%@|awaitingCancelActivityAck:%@|awaitingStagerAck:%@|activeJobsByUUID:%@|limitedToCancelActivity:%@]"
- "[initialSelector:%@|fullSelector:%@|clientInstance:%@|clientDesire:%@|foundContent:%@]"
- "[instance latestDownloaded:%@(entries:%ld), discovered:%@(entries:%ld), requested(entries:%ld), fullyDownloaded:%@|onFilesystem:%@(incomplete:%@), neverBeenLocked:%@, userInitiated:%@, stagedPrior:%@|catalog cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@|downloaded cachedAssetSetID:%@, downloadedFromLive:%@, lastTimeChecked:%@, postedDate:%@]"
- "[overall]instance:%@,selector:%@,UUID:%@,logger:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@"
- "_autoAssetJobProgressNewValidatedCurrentStatus:"
- "_eliminateAtomicTriggeredByClient:forClientDomainName:forAssetSetIdentifier:"
- "_mabrain_copy_certificate_security_mode"
- "_mabrainbundle_copy_board_id"
- "_mabrainbundle_copy_chip_id"
- "_mabrainbundle_copy_ecid"
- "_mabrainbundle_copy_security_domain"
- "_mabrainbundle_copy_signing_fuse"
- "_preInstalledMakeDescriptorAvailable:"
- "_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:"
- "action_RemeberEliminateDone:error:"
- "action_ResumeScheduler:error:"
- "again"
- "atomicInstanceNewSetAtomicInstance:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:"
- "atomicInstanceNewSetAtomicInstance:forSetInfoInstance:asSubAtomicFrom:"
- "atomicInstanceNewSetAtomicInstance:recoveringForSetDescriptor:usingAsSetClient:"
- "atomicInstanceRemove:setAtomicInstanceUUID:removingForReason:"
- "atomicInstanceRemovedSetJob:removingForReason:"
- "checkAtomic (NO_WAIT) requested when specific atomic-instance not already downloaded (and not pre-installed)"
- "com.apple.MobileAsset.RegulatoryCertification"
- "dropping stale entries"
- "endedAllPreviousSetLocksByClient:forSetDescriptor:forLockReason:endError:"
- "first"
- "getPallasUrl"
- "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:"
- "incomplete set-eventInfo | set-eventInfo:%@"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:inhibitingImpliedScheduling:"
- "initFromClientLockReasonKey:"
- "initWithClientRequest:withAssetSelector:"
- "initWithClientRequest:withAssetSelector:forClientDomain:forSetIdentifier:"
- "initWithContentsOfURL:error:"
- "initWithParamType:withSafeSummary:withStagingClientRequest:withBaseForStagingDescriptors:withJobInformation:withAutoAssetCatalog:withOperationError:withAssetType:withAssetSelector:withAlreadyDownloaded:withSetConfigurations:withSetTargets:withScheduldJobs:withDownloadedDescriptor:"
- "isAnyAssetEntryOnFilesystemForSetDescriptor:"
- "loadPersistedRecoverLost"
- "loadPersistedSetDownloadedDescriptors(incomplete)"
- "loadPersistedSetDownloadedDescriptors(missing)"
- "lock (NO_WAIT) requested when specific atomic-instance not already downloaded (and not pre-installed)"
- "lockAtomic[NO_WAIT_NOT_PERSISTED]"
- "no valid asset-entries to alter to | set-eventInfo:%@"
- "persistForJobSelector:persistingJobDescriptor:justDownloaded:justPatched:withFirstClientName:"
- "persistForJobSelector:persistingJobDescriptor:justPatched:withFirstClientName:"
- "persistForJobSelector:persistingJobDescriptor:withFirstClientName:"
- "persistSetDescriptorDownloadedJob:fromLocation:"
- "removeCurrentSetJob:schedulerInvolved:potentialNetworkFailure:fromLocation:"
- "removeSetDescriptorDownloaded:fromLocation:"
- "removed set-atomic-instance"
- "replyToJobsWhenLockFoundSame:"
- "scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:"
- "setDescriptorAllEntriesDownloaded:"
- "setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:"
- "trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:"
- "updateAssociatedStatus:forActiveJobUUID:withLatestJobStatus:"
- "updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:fromLocation:"
- "v48@0:8@16@24B32B36@40"
- "v60@0:8@16q24q32B40B44@48B56"
- "v68@0:8@16@24B32@36B44B48q52@60"
- "{%@} no set-configuration found when have chosen set-descriptor"
- "{AUTO-LOCKER:endedAllPreviousSetLocksByClient} failed end-set-lock(s) | client:%{public}@, lockedSetDescriptor:%{public}@, reason:%{public}@ | error:%{public}@"
- "{AUTO-LOCKER:endedAllPreviousSetLocksByClient} successful end-set-lock(s) | client:%{public}@, lockedSetDescriptor:%{public}@, reason:%{public}@"
- "{AUTO-LOCKER:endedAllPreviousSetLocksByClient} | unable to end auto-asset all-locks of the set | setAtomicEntry:%{public}@ | endedLocksAutoAssetError:%{public}@"
- "{ControlManager:getSAFRegistrationBundleID} Fail to read content from %@. Error: %@"
- "{ControlManager:getSAFRegistrationBundleID} Unable to find bundle ID from '%@' key and asset type from %@ key in: %@"
- "{ControlManager:getSAFRegistrationBundleID} Unable to parse Info.plist in %@ to dictionary"
- "{MADAutoAssetControlManager-updateAssociatedStatus} WARNING: wrong class provided as jobStatus"
- "{ResumeJobs} | Preserved Persisted-State | ActiveJobs:%ld, KnownDescriptors:%ld | Locks:%ld, Scheduled:%ld, Staged:%ld | SetConfigurations:%ld, AtomicInstances:%ld, ActiveSetDescriptors:%ld, DownloadedSetDescriptors:%ld, SetTargets:%ld, SetLookupResults:%ld"
- "{_preInstalledMakeDescriptorAvailable} already migrated | availableToMigrate:%@, alreadyAvailable:%@"
- "{replyToJobsWhenLockFoundSame} no associated descriptor on filesystem (should always be there at this point)"
- "{replyToJobsWhenLockFoundSame} not valid for a stager-job"
- "{updateAssociatedStatus} unable to locate autoJob for autoAssetSelector:%@, autoAssetJobUUID:%@ | partial status:%@"
- "{updateLastFetchedDate} failed to update lastFetchedDate in xml | tempLocation:%@ targetLocation:%@"
- "{writeDictionaryToFile} failed to move XML | tempLocation:%@ targetLocation:%@"

```
