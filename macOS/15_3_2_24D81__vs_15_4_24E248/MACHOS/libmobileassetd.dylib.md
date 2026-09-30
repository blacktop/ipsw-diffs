## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1329.80.16.0.0
-  __TEXT.__text: 0x2a334c
-  __TEXT.__auth_stubs: 0x2260
-  __TEXT.__objc_stubs: 0x1fec0
-  __TEXT.__objc_methlist: 0xf2e0
-  __TEXT.__const: 0x491e
-  __TEXT.__objc_methname: 0x37e5e
-  __TEXT.__cstring: 0x4bc66
-  __TEXT.__objc_classname: 0xdb0
-  __TEXT.__objc_methtype: 0x363d
-  __TEXT.__oslogstring: 0x31d5d
-  __TEXT.__gcc_except_tab: 0x24c8
-  __TEXT.__swift5_typeref: 0x10c4
-  __TEXT.__constg_swiftt: 0x1530
-  __TEXT.__swift5_fieldmd: 0x1014
-  __TEXT.__swift5_reflstr: 0x801
+1487.101.2.0.0
+  __TEXT.__text: 0x2b06c4
+  __TEXT.__auth_stubs: 0x2330
+  __TEXT.__objc_stubs: 0x22260
+  __TEXT.__objc_methlist: 0x103e4
+  __TEXT.__const: 0x485e
+  __TEXT.__cstring: 0x37236
+  __TEXT.__objc_methname: 0x3d4a6
+  __TEXT.__objc_classname: 0xe0d
+  __TEXT.__objc_methtype: 0x39fb
+  __TEXT.__oslogstring: 0x4a4e3
+  __TEXT.__gcc_except_tab: 0x2e04
+  __TEXT.__swift5_typeref: 0x1093
+  __TEXT.__constg_swiftt: 0x14fc
+  __TEXT.__swift5_fieldmd: 0xfec
+  __TEXT.__swift5_reflstr: 0x7e1
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x5e0
-  __TEXT.__swift5_proto: 0x324
-  __TEXT.__swift5_types: 0x19c
+  __TEXT.__swift5_proto: 0x300
+  __TEXT.__swift5_types: 0x198
   __TEXT.__swift5_protos: 0x60
+  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x48b8
-  __TEXT.__eh_frame: 0x312c
-  __DATA_CONST.__auth_got: 0x1140
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__auth_ptr: 0x900
-  __DATA_CONST.__const: 0x67b8
-  __DATA_CONST.__cfstring: 0x31620
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __TEXT.__unwind_info: 0x47d8
+  __TEXT.__eh_frame: 0x332c
+  __DATA_CONST.__auth_got: 0x11a8
+  __DATA_CONST.__got: 0x670
+  __DATA_CONST.__auth_ptr: 0x968
+  __DATA_CONST.__const: 0x6908
+  __DATA_CONST.__cfstring: 0x2b300
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ce0
-  __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0xa68
-  __DATA_CONST.__objc_arrayobj: 0x228
-  __DATA_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_const: 0x14998
-  __DATA.__objc_classrefs: 0x788
+  __DATA_CONST.__objc_selrefs: 0x97b8
+  __DATA_CONST.__objc_intobj: 0x558
+  __DATA_CONST.__objc_arraydata: 0xb50
+  __DATA_CONST.__objc_arrayobj: 0x270
+  __DATA_CONST.__objc_dictobj: 0xf0
+  __DATA.__objc_const: 0x15120
+  __DATA.__objc_classrefs: 0x7d0
   __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x12c4
-  __DATA.__objc_data: 0x2728
-  __DATA.__data: 0x260a
+  __DATA.__objc_ivar: 0x13f0
+  __DATA.__objc_data: 0x2778
+  __DATA.__data: 0x25aa
   __DATA.__s_async_hook: 0x190
   __DATA.__swift56_hooks: 0xb0
-  __DATA.__bss: 0x5728
-  __DATA.__common: 0xb0
+  __DATA.__bss: 0x54f8
+  __DATA.__common: 0x90
   - /System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 02C492AD-81C1-3676-9DA8-C0E583791D33
-  Functions: 8466
-  Symbols:   15083
-  CStrings:  22156
+  UUID: B23199DB-974A-3456-B808-BF229391D18D
+  Functions: 8431
+  Symbols:   15418
+  CStrings:  22078
 
Symbols:
+ +[ASAssetMetadataUpdatePolicy policy].cold.1
+ +[DownloadManager addNWActivityToDownloadInfo:andTask:andLabel:]
+ +[MABrainRestartManager sharedInstance].cold.1
+ +[MABrainUpdater sharedInstance].cold.1
+ +[MADActivityManager sharedActivityManager].cold.1
+ +[MADAnalyticsManager getAnalyticsManager].cold.1
+ +[MADAutoAssetConnector autoAssetConnector].cold.1
+ +[MADAutoAssetControlManager assetConfigJobFinished:withDownloadInfo:error:]
+ +[MADAutoAssetControlManager autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:withCatalogLookupResponse:]
+ +[MADAutoAssetControlManager autoControlManager].cold.1
+ +[MADAutoAssetControlManager autoSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:]
+ +[MADAutoAssetControlManager autoSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:]
+ +[MADAutoAssetControlManager daemonProcessStartupBegun]
+ +[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:]
+ +[MADAutoAssetControlManager postSetNotificationName:forClientDomainName:forAssetSetIdentifier:forAtomicInstanceUUID:fromModule:fromLocation:]
+ +[MADAutoAssetControlManager preferencePerformanceLoggingEnabled]
+ +[MADAutoAssetControlManager preferenceStagerDetermineLastRequiredTimesOut]
+ +[MADAutoAssetControlManager schedulerTickOccurred]
+ +[MADAutoAssetControlManager stagerResumed:withSetLookupResults:requiringLoadPriorToUse:]
+ +[MADAutoAssetControlManager stagerSetPolicy].cold.1
+ +[MADAutoAssetDescriptor typeAndSpecifierKeyForAssetType:andAssetSpecifier:]
+ +[MADAutoAssetHistory autoAssetHistory].cold.1
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:failingWithError:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:failingWithError:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:withSelectors:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forSelectors:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forAssetSetIdentifier:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withSelector:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistoryTracker summaryOfAssetSelectors:]
+ +[MADAutoAssetLocker autoAssetLocker].cold.1
+ +[MADAutoAssetLocker copyOfLockCountsBySelector]
+ +[MADAutoAssetLocker forceGlobalUnlock:atomicInstancesHandle:]
+ +[MADAutoAssetLocker newSetClientNameForDomain:withAutoAssetClientName:forSetAtomicInstance:]
+ +[MADAutoAssetLookupCache autoAssetLookupCache].cold.1
+ +[MADAutoAssetScheduler autoAssetScheduler].cold.1
+ +[MADAutoAssetSecure autoAssetSecure].cold.1
+ +[MADAutoAssetSecure readyToCommitPrePersonalized:forSetDescriptor:]
+ +[MADAutoAssetSetHealthReport errorSummaryForSplunk:]
+ +[MADAutoAssetSetHealthReport formattedDate:]
+ +[MADAutoAssetSetHealthReport formattedDate:].cold.1
+ +[MADAutoAssetSetHealthReport shortUUID:]
+ +[MADAutoAssetSetHealthReport trimmedSetIdentifier:]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _currentState]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _nonceFileURL]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _stateFileURL]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState clear]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState currentStatusWithStateHandle:]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState supportsSecureCoding]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState writeNewSuspendingStateWithNonce:setConfigurationsToEvict:]
+ +[MADAutoAssetStager autoAssetStager].cold.1
+ +[MADAutoAssetStager finishSuspendedResumeFromPersisted]
+ +[MADCacheDeleteManager sharedManager].cold.1
+ +[MADPowerLogManager sharedManager].cold.1
+ +[MAPushNotificationServiceDaemon sharedInstance].cold.1
+ +[MAStringUtilities convertFromString:usingBase:toI64:].cold.1
+ +[MobileAssetHealthReport bucketedDays:]
+ +[MobileAssetHealthReport sharedInstance].cold.1
+ +[SecureMobileAssetBundle clearGraftList:]
+ +[SecureMobileAssetBundle copyGraftList:]
+ +[SecureMobileAssetBundle getGraftListLock]
+ +[SecureMobileAssetBundle getGraftListLock].cold.1
+ +[SecureMobileAssetBundle personalizationQueue].cold.1
+ +[SecureMobileAssetMountManager sharedInstance].cold.1
+ -[ASAssetMetadataUpdatePolicy trainName].cold.1
+ -[DownloadInfo nwActivity]
+ -[DownloadInfo setNwActivity:]
+ -[DownloadManager MACopyDawToken:].cold.1
+ -[DownloadManager _getKeysNotLoggedForAutoResponse].cold.1
+ -[DownloadManager _getKeysNotLoggedForV2Response].cold.1
+ -[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]
+ -[DownloadManager decryptContentEncryptedAssetAtPathIfRequired:].cold.1
+ -[DownloadManager downloadNeedsSSO:taskDescriptor:url:].cold.1
+ -[DownloadManager handleDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:notifyingAutoAssetLayer:]
+ -[DownloadManager indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:]
+ -[DownloadManager indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:]
+ -[DownloadManager sendMobileAssetHealthReport:commonFields:sessionId:]
+ -[DownloadManager taskFinishedUpdateState:with:extraInfo:fromLocation:]
+ -[DownloadManager taskFinishedUpdateState:with:fromLocation:]
+ -[DownloadManager trackDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:]
+ -[MABAACertManager copyCurrentBootManifestHash].cold.1
+ -[MABrainBundle personalize:options:error:].cold.1
+ -[MADAnalyticsManager recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:withReason:]
+ -[MADAutoAssetControlManager _acceptPersonalizationFromPSUSToBecomeLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:]
+ -[MADAutoAssetControlManager _acceptPersonalizationToAttempt:forAtomicEntry:]
+ -[MADAutoAssetControlManager _acceptPersonalizationToAttempt:forSetDescriptor:withCandidates:extendingToBePersonalized:]
+ -[MADAutoAssetControlManager _acceptPersonalizationToAttempt:forSetLookupResult:withCandidates:extendingToBePersonalized:]
+ -[MADAutoAssetControlManager _acceptPersonalizationToProvideLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:]
+ -[MADAutoAssetControlManager _acceptPersonalizationToProvidePreinstalled:forSetConfiguration:withCandidates:extendingToBePersonalized:]
+ -[MADAutoAssetControlManager _allPreInstalledDescriptor:forAssetType:]
+ -[MADAutoAssetControlManager _clearAtomicInstanceFromAllSetConfigurations:fromLocation:]
+ -[MADAutoAssetControlManager _clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:]
+ -[MADAutoAssetControlManager _constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:]
+ -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:]
+ -[MADAutoAssetControlManager _errorUnlessSameVersionFound:changedReportedError:]
+ -[MADAutoAssetControlManager _filesystemCachedInfo:forPath:]
+ -[MADAutoAssetControlManager _forceSetUngraftAndEliminateAllSetLocks:forSetDescriptor:]
+ -[MADAutoAssetControlManager _handleClientAlterLockOperationForDescriptor:forEventInfo:error:]
+ -[MADAutoAssetControlManager _persistedKnownDescriptorForFullAssetSelector:]
+ -[MADAutoAssetControlManager _persistedKnownDescriptorForPersistedEntryID:]
+ -[MADAutoAssetControlManager _preinstalledTrackBySelector:]
+ -[MADAutoAssetControlManager _removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:]
+ -[MADAutoAssetControlManager _removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager _schedulerTickOccurred]
+ -[MADAutoAssetControlManager _shortTermForceForget:forSetDescriptor:]
+ -[MADAutoAssetControlManager _startupActivationProcessIdentifier]
+ -[MADAutoAssetControlManager _trackPerformanceStartupBegin]
+ -[MADAutoAssetControlManager action_DecrementTickDriven:error:]
+ -[MADAutoAssetControlManager action_SchedulerJobDownloaded:error:]
+ -[MADAutoAssetControlManager action_SchedulerJobFoundSame:error:]
+ -[MADAutoAssetControlManager addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:fromLocation:]
+ -[MADAutoAssetControlManager assetPersonalizatonAttemptCompletePostEvent:withControlParam:]
+ -[MADAutoAssetControlManager atomicInstanceDropOncePersonalized:forSetConfiguration:]
+ -[MADAutoAssetControlManager atomicInstanceForceUnlock:forgettingAtomicInstance:]
+ -[MADAutoAssetControlManager atomicInstanceFromPSUSLookupResultOncePersonalized:forSetConfiguration:]
+ -[MADAutoAssetControlManager atomicInstanceIsCurrentlyLocked:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:]
+ -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:]
+ -[MADAutoAssetControlManager atomicInstanceUpdateUsageStatus:toNewStatus:forAtomicInstance:]
+ -[MADAutoAssetControlManager bootedOSBuildVersion]
+ -[MADAutoAssetControlManager cancelActiveSetJob:activeSetJob:]
+ -[MADAutoAssetControlManager cancelingSetJobsByIdentifier]
+ -[MADAutoAssetControlManager completionCallbacksBySetJobKey]
+ -[MADAutoAssetControlManager considerDownloadedWithPSUSLookupResultsForLatestToVend]
+ -[MADAutoAssetControlManager decrementClientRequestCount:forEventInfo:]
+ -[MADAutoAssetControlManager doesSetDescriptor:referenceSetConfiguration:]
+ -[MADAutoAssetControlManager doesSetDescriptor:satisfySetConfiguration:allowingMoreDownloaded:]
+ -[MADAutoAssetControlManager doesSetDescriptorReferenceAllPreInstalledContent:]
+ -[MADAutoAssetControlManager doesSetDescriptorWithoutVersion:referenceAssetDescriptor:]
+ -[MADAutoAssetControlManager doesSetJobDescriptor:representSameContentAs:]
+ -[MADAutoAssetControlManager ensureStagerFullyResumed]
+ -[MADAutoAssetControlManager evictedCallbacksByAtomicInstanceUUID]
+ -[MADAutoAssetControlManager filesystemDoesDirectoryExist:atPath:isDirectory:]
+ -[MADAutoAssetControlManager filesystemDoesFileExist:atPath:]
+ -[MADAutoAssetControlManager filesystemFileExistAtPathCache]
+ -[MADAutoAssetControlManager filesystemStartupLookupCount]
+ -[MADAutoAssetControlManager firstSchedulerCrosscheckTrimAtomicInstances]
+ -[MADAutoAssetControlManager firstSchedulerCrosscheckTrimSetDescriptors]
+ -[MADAutoAssetControlManager firstSchedulerCrosscheckTrim]
+ -[MADAutoAssetControlManager forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:]
+ -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:]
+ -[MADAutoAssetControlManager isAnyAssetFromSetFromNewOSPromoted:]
+ -[MADAutoAssetControlManager isAtomicInstanceForCurrentSetJob:]
+ -[MADAutoAssetControlManager isAtomicInstanceLatestToVendForSet:]
+ -[MADAutoAssetControlManager isEveryAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:]
+ -[MADAutoAssetControlManager isNoWaitRequestInvolvingSecureAsset:]
+ -[MADAutoAssetControlManager loadPersistedCrosscheckStaleForceUnlock]
+ -[MADAutoAssetControlManager locateCancelingSetJobForClientDomain:byIdentifier:]
+ -[MADAutoAssetControlManager locateSetDescriptor:forAtomicInstanceUUID:requireExists:]
+ -[MADAutoAssetControlManager locateSetDescriptorForStagingDescriptor:]
+ -[MADAutoAssetControlManager locateStagedSetDescriptorFor:]
+ -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MADAutoAssetControlManager newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:]
+ -[MADAutoAssetControlManager persistedKnownDescriptorForSetAtomicEntry:]
+ -[MADAutoAssetControlManager preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:]
+ -[MADAutoAssetControlManager preferencePerformanceLoggingEnabled]
+ -[MADAutoAssetControlManager preferenceStagerDetermineLastRequiredTimesOut]
+ -[MADAutoAssetControlManager preinstalledAssetDescriptorsBySelector]
+ -[MADAutoAssetControlManager removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:performingHardEliminate:error:]
+ -[MADAutoAssetControlManager schedulerTickPerformedCrossCheck]
+ -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:fromPreSUStaging:]
+ -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:fromPreSUStaging:completion:]
+ -[MADAutoAssetControlManager setBootedOSBuildVersion:]
+ -[MADAutoAssetControlManager setCancelingSetJobsByIdentifier:]
+ -[MADAutoAssetControlManager setCompletionCallbacksBySetJobKey:]
+ -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:]
+ -[MADAutoAssetControlManager setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:]
+ -[MADAutoAssetControlManager setConfigurationAssetSetIDLatestToVend:fromSetDescriptor:forSetConfiguration:buildingPersistReason:]
+ -[MADAutoAssetControlManager setConfigurationAssetSetIDMostRecentlyReceived:fromSetDescriptor:forSetConfiguration:buildingPersistReason:]
+ -[MADAutoAssetControlManager setConfigurationForDescriptorIfManagedAsSet:]
+ -[MADAutoAssetControlManager setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:]
+ -[MADAutoAssetControlManager setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:]
+ -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:forReason:dueToAlter:forHistoryOperation:]
+ -[MADAutoAssetControlManager setConfigurationPreviouslyVendedLockedAtomicInstances:]
+ -[MADAutoAssetControlManager setConfigurationRemovedAtomicInstance:fromLocation:]
+ -[MADAutoAssetControlManager setConfigurationTickForPreviouslyVended]
+ -[MADAutoAssetControlManager setConfigurationTrackAsPreviouslyVended:forSetConfiguration:addingAtomicInstance:]
+ -[MADAutoAssetControlManager setConfigurationTrackLatestToVend:forSetConfiguration:becomingLatestToVend:historyOperation:fromPreSUStaging:]
+ -[MADAutoAssetControlManager setDescriptorAllDiscoveredEntriesDownloaded:forSetDescriptor:loggingEntryExists:]
+ -[MADAutoAssetControlManager setDescriptorWalkKeys]
+ -[MADAutoAssetControlManager setDescriptorWalkLocate:forKey:]
+ -[MADAutoAssetControlManager setEvictedCallbacksByAtomicInstanceUUID:]
+ -[MADAutoAssetControlManager setFilesystemFileExistAtPathCache:]
+ -[MADAutoAssetControlManager setFilesystemStartupLookupCount:]
+ -[MADAutoAssetControlManager setJobIndicationOfPotentialLatestToVend:forEventInfo:issuingClientReply:]
+ -[MADAutoAssetControlManager setLockUsageMapLockCount]
+ -[MADAutoAssetControlManager setPreferencePerformanceLoggingEnabled:]
+ -[MADAutoAssetControlManager setPreferenceStagerDetermineLastRequiredTimesOut:]
+ -[MADAutoAssetControlManager setPreinstalledAssetDescriptorsBySelector:]
+ -[MADAutoAssetControlManager setSchedulerTickPerformedCrossCheck:]
+ -[MADAutoAssetControlManager setStagedAssetToSetDescriptorCache:]
+ -[MADAutoAssetControlManager setStagedIsNewOSPromotedCache:]
+ -[MADAutoAssetControlManager setStagedSetLookupResults:]
+ -[MADAutoAssetControlManager setStagedToDownloaded:]
+ -[MADAutoAssetControlManager setStagerResumePostponed:]
+ -[MADAutoAssetControlManager setStartupTimeBeginSeconds:]
+ -[MADAutoAssetControlManager setStartupTimeDurationSeconds:]
+ -[MADAutoAssetControlManager shortTermLockFilesHealthCheck]
+ -[MADAutoAssetControlManager shortTermLockSetDescriptor:forSetDescriptor:forSpecificAtomicInstance:]
+ -[MADAutoAssetControlManager stagedAssetToSetDescriptorCache]
+ -[MADAutoAssetControlManager stagedIsNewOSPromotedCache]
+ -[MADAutoAssetControlManager stagedSetLookupResults]
+ -[MADAutoAssetControlManager stagedToDownloaded]
+ -[MADAutoAssetControlManager stagerResumePostponed]
+ -[MADAutoAssetControlManager startupActivationCompleted:]
+ -[MADAutoAssetControlManager startupActivationIsFirstExecutionSinceBoot:]
+ -[MADAutoAssetControlManager startupActivationResourceSummary]
+ -[MADAutoAssetControlManager startupTimeBeginSeconds]
+ -[MADAutoAssetControlManager startupTimeDurationSeconds]
+ -[MADAutoAssetControlManager trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:isPromoted:]
+ -[MADAutoAssetControlManager trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:]
+ -[MADAutoAssetControlManager trackPerformanceIteration:ofContainer:]
+ -[MADAutoAssetControlManager trackPerformancePhaseBegin:]
+ -[MADAutoAssetControlManager trackPerformancePhaseEnd:]
+ -[MADAutoAssetControlManager trackPerformanceStartupEnd:]
+ -[MADAutoAssetControlManager trackPerformanceStartupStep:beginningStep:]
+ -[MADAutoAssetControlManager trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:fromPreSUStaging:]
+ -[MADAutoAssetControlManager trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:]
+ -[MADAutoAssetControlManager validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:]
+ -[MADAutoAssetControlManager wouldSetDescriptorForStagedPlusPrePersonalizedVendAtomicInstance:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _addCompletionCallbackForSetJobKey:completionCallback:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _addEvictedCallbackForAtomicInstanceUUID:completionCallback:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleEstimateEvictableBytesForSoftwareUpdateRequestWithBytesBySetIdentifier:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleResumeFromSoftwareUpdateRequest]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce:setConfigurationsToEvict:completionBlock:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _softwareUpdateSuspendResumeEligibleSetEntryIDs]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleEstimateEvictableBytesForSoftwareUpdateRequest:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleResumeFromSoftwareUpdateRequest:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleStatusForSoftwareUpdateRequest:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleSuspendForSoftwareUpdateRequest:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleSuspendResumeForSoftwareUpdateDaemonStartup]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) isSuspendedForSoftwareUpdate:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) notifyEvictedCallbacksForSetDescriptor:]
+ -[MADAutoAssetControlManagerParam downloadOptions]
+ -[MADAutoAssetControlManagerParam initForConfigFinishedJobID:andDownloadOptions:withError:]
+ -[MADAutoAssetControlManagerParam initForSetConfiguration:withSetDescriptor:withCatalogLookupResponse:]
+ -[MADAutoAssetControlManagerParam initForSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:]
+ -[MADAutoAssetControlManagerParam initForSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetControlManagerParam initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:]
+ -[MADAutoAssetControlManagerParam requiringLoadPriorToUse]
+ -[MADAutoAssetDescriptor existsOnFilesystem]
+ -[MADAutoAssetDescriptor localContentURLOfAssetDescriptor]
+ -[MADAutoAssetDescriptor totalFilesystemSpace]
+ -[MADAutoAssetDescriptor typeAndSpecifierKey]
+ -[MADAutoAssetHistory trackerPushNotification]
+ -[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:]
+ -[MADAutoAssetJob _updateDownloadOptions:]
+ -[MADAutoAssetJob _updateUserInitiatedFields]
+ -[MADAutoAssetJob action_BoostConfig:error:]
+ -[MADAutoAssetJob boostedToCellular]
+ -[MADAutoAssetJob boostedToExpensive]
+ -[MADAutoAssetJob configuredToCellular]
+ -[MADAutoAssetJob configuredToExpensive]
+ -[MADAutoAssetJob configuredToUserInitiated]
+ -[MADAutoAssetJob dedupAtomicEntries:]
+ -[MADAutoAssetJob downloadingCellular]
+ -[MADAutoAssetJob downloadingExpensive]
+ -[MADAutoAssetJob handleDownloadConfigJobFinished:withDownloadOptions:configError:]
+ -[MADAutoAssetJob manager]
+ -[MADAutoAssetJob queuedRequestsForNewJobOnceCanceled]
+ -[MADAutoAssetJob refreshDownloadedToManager:]
+ -[MADAutoAssetJob refreshSetFoundToManager:fromLocation:]
+ -[MADAutoAssetJob reportSetCatalogDecideFound:fromLocation:]
+ -[MADAutoAssetJob setBoostedToCellular:]
+ -[MADAutoAssetJob setBoostedToExpensive:]
+ -[MADAutoAssetJob setConfiguredToCellular:]
+ -[MADAutoAssetJob setConfiguredToExpensive:]
+ -[MADAutoAssetJob setConfiguredToUserInitiated:]
+ -[MADAutoAssetJob setDownloadingCellular:]
+ -[MADAutoAssetJob setDownloadingExpensive:]
+ -[MADAutoAssetJob setQueuedRequestsForNewJobOnceCanceled:]
+ -[MADAutoAssetJob setTryPersonalizePromoted:]
+ -[MADAutoAssetJob tryPersonalizePromoted]
+ -[MADAutoAssetLocker _endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:]
+ -[MADAutoAssetLocker _lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:]
+ -[MADAutoAssetLocker _persistAssetLock:operation:forAssetLock:withDeltaLockCount:message:]
+ -[MADAutoAssetLocker _removeAssetLock:removingAssetLock:lastClient:forSelector:message:]
+ -[MADAutoAssetLocker addToLockCountsBySelector:addingAssetLock:]
+ -[MADAutoAssetLocker lockCountsBySelector]
+ -[MADAutoAssetLocker lockCountsTotal]
+ -[MADAutoAssetLocker setLockCountsBySelector:]
+ -[MADAutoAssetLocker setLockCountsTotal:]
+ -[MADAutoAssetLocker trackPerformanceIteration:ofContainer:]
+ -[MADAutoAssetLocker trackPerformanceIteration:ofContainer:forSelector:]
+ -[MADAutoAssetPersisted decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:allowingNilObject:]
+ -[MADAutoAssetPersisted decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:withEncodeClasses:allowingNilObject:]
+ -[MADAutoAssetScheduler defaultSchedulerSetPolicy].cold.1
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
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState .cxx_destruct]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState build]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState encodeWithCoder:]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState initWithCoder:]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState initWithNonce:status:setConfigurationsToEvict:]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState nonce]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState setConfigurationsToEvict]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState setStatus:]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState status]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState suspendedSetConfigurationsFromPreviousOS]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState suspendedSetConfigurationsHasCurrentNonce]
+ -[MADAutoAssetSoftwareUpdateSuspendResumeState write]
+ -[MADAutoAssetStager _acceptStagingClientRequest:fromLocation:adoptingSpecifiedTarget:]
+ -[MADAutoAssetStager _limitCachePersistResultByGroupToCount:fromLocation:]
+ -[MADAutoAssetStager _logPersistedConfigLoad:message:]
+ -[MADAutoAssetStager _replyHaveStagedContent:withEventInfo:]
+ -[MADAutoAssetStager _setConfigurationAdjustedFrom:basedOnSetTarget:]
+ -[MADAutoAssetStager action_LoadDecideNewOSPromote:error:]
+ -[MADAutoAssetStager analyticsManager]
+ -[MADAutoAssetStager formAvailableForStagingByCombiningRequiredAndOptional:]
+ -[MADAutoAssetStager loadPersistedPostponed]
+ -[MADAutoAssetStager newSetConfigurationForAssetSetIdentifier:withAutoAssetEntries:]
+ -[MADAutoAssetStager newSetConfigurationForClientDomainName:forAssetSetIdentifier:withAutoAssetEntries:]
+ -[MADAutoAssetStager optionalAssetSizeAllowed]
+ -[MADAutoAssetStager setAnalyticsManager:]
+ -[MADAutoAssetStager setLoadPersistedPostponed:]
+ -[MADAutoAssetStager setOptionalAssetSizeAllowed:]
+ -[MADAutoAssetStager setStartupActivelyStagingAssetCount:]
+ -[MADAutoAssetStager setStartupAssetTargetBuildVersion:]
+ -[MADAutoAssetStager setStartupAssetTargetOSVersion:]
+ -[MADAutoAssetStager setStartupAwaitingStagingAssetCount:]
+ -[MADAutoAssetStager setStartupCandidateAssetCount:]
+ -[MADAutoAssetStager setStartupDeterminedAvailableAssetCount:]
+ -[MADAutoAssetStager setStartupLastStagingFromBuildVersion:]
+ -[MADAutoAssetStager setStartupLastStagingFromOSVersion:]
+ -[MADAutoAssetStager setStartupModeByGroups:]
+ -[MADAutoAssetStager setStartupStagedAssetCount:]
+ -[MADAutoAssetStager setStartupStagedAssetTotalContentBytes:]
+ -[MADAutoAssetStager splitOutAvailableForStagingByGroup:forGroupDetermine:]
+ -[MADAutoAssetStager startupActivelyStagingAssetCount]
+ -[MADAutoAssetStager startupAssetTargetBuildVersion]
+ -[MADAutoAssetStager startupAssetTargetOSVersion]
+ -[MADAutoAssetStager startupAwaitingStagingAssetCount]
+ -[MADAutoAssetStager startupCandidateAssetCount]
+ -[MADAutoAssetStager startupDeterminedAvailableAssetCount]
+ -[MADAutoAssetStager startupLastStagingFromBuildVersion]
+ -[MADAutoAssetStager startupLastStagingFromOSVersion]
+ -[MADAutoAssetStager startupModeByGroups]
+ -[MADAutoAssetStager startupStagedAssetCount]
+ -[MADAutoAssetStager startupStagedAssetTotalContentBytes]
+ -[MADAutoSetAtomicInstance creationReason]
+ -[MADAutoSetAtomicInstance initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:]
+ -[MADAutoSetAtomicInstance setUsageStatus:]
+ -[MADAutoSetAtomicInstance usageStatus]
+ -[MADAutoSetConfiguration availableForUseError]
+ -[MADAutoSetConfiguration discoveredInFlightAtomicInstance]
+ -[MADAutoSetConfiguration everProvidedLatestToVend]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoSetConfiguration latestAtomicInstanceToVendFromPreSUStaging]
+ -[MADAutoSetConfiguration latestToVendCachedAssetSetID]
+ -[MADAutoSetConfiguration latestToVendDownloadedFromLive]
+ -[MADAutoSetConfiguration latestToVendLastTimeChecked]
+ -[MADAutoSetConfiguration latestToVendPostedDate]
+ -[MADAutoSetConfiguration mostRecentlyReceivedCachedAssetSetID]
+ -[MADAutoSetConfiguration mostRecentlyReceivedDownloadedFromLive]
+ -[MADAutoSetConfiguration mostRecentlyReceivedLastTimeChecked]
+ -[MADAutoSetConfiguration mostRecentlyReceivedPostedDate]
+ -[MADAutoSetConfiguration newerAtomicInstanceOncePersonalized]
+ -[MADAutoSetConfiguration newerVersionError]
+ -[MADAutoSetConfiguration previouslyVendedLockedAtomicInstances]
+ -[MADAutoSetConfiguration previouslyVendedLockedSummary]
+ -[MADAutoSetConfiguration setAvailableForUseError:]
+ -[MADAutoSetConfiguration setDiscoveredInFlightAtomicInstance:]
+ -[MADAutoSetConfiguration setEverProvidedLatestToVend:]
+ -[MADAutoSetConfiguration setLatestAtomicInstanceToVendFromPreSUStaging:]
+ -[MADAutoSetConfiguration setLatestToVendCachedAssetSetID:]
+ -[MADAutoSetConfiguration setLatestToVendDownloadedFromLive:]
+ -[MADAutoSetConfiguration setLatestToVendLastTimeChecked:]
+ -[MADAutoSetConfiguration setLatestToVendPostedDate:]
+ -[MADAutoSetConfiguration setMostRecentlyReceivedCachedAssetSetID:]
+ -[MADAutoSetConfiguration setMostRecentlyReceivedDownloadedFromLive:]
+ -[MADAutoSetConfiguration setMostRecentlyReceivedLastTimeChecked:]
+ -[MADAutoSetConfiguration setMostRecentlyReceivedPostedDate:]
+ -[MADAutoSetConfiguration setNewerAtomicInstanceOncePersonalized:]
+ -[MADAutoSetConfiguration setNewerVersionError:]
+ -[MADAutoSetConfiguration setPreviouslyVendedLockedAtomicInstances:]
+ -[MADAutoSetConfiguration setTicksUntilPreviousForceUnlocked:]
+ -[MADAutoSetConfiguration ticksUntilPreviousForceUnlocked]
+ -[MADAutoSetTarget includesEntryForAssetType:]
+ -[MANAutoAssetControlStatisticsByCommand estimateEvictableBytesForSoftwareUpdate]
+ -[MANAutoAssetControlStatisticsByCommand resumeFromSoftwareUpdate]
+ -[MANAutoAssetControlStatisticsByCommand setEstimateEvictableBytesForSoftwareUpdate:]
+ -[MANAutoAssetControlStatisticsByCommand setResumeFromSoftwareUpdate:]
+ -[MANAutoAssetControlStatisticsByCommand setSuspendForSoftwareUpdate:]
+ -[MANAutoAssetControlStatisticsByCommand setSuspendResumeStatusForSoftwareUpdate:]
+ -[MANAutoAssetControlStatisticsByCommand suspendForSoftwareUpdate]
+ -[MANAutoAssetControlStatisticsByCommand suspendResumeStatusForSoftwareUpdate]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MANAutoAssetSetStatus latestDownloadedAtomicInstanceFromPreSUStaging]
+ -[MANAutoAssetSetStatus previouslyVendedLockedAtomicInstance]
+ -[MANAutoAssetSetStatus setLatestDownloadedAtomicInstanceFromPreSUStaging:]
+ -[MAPushChannel populationTypeString]
+ -[MAPushServiceConnection _recordFailedOperation:forReason:]
+ -[MAPushServiceConnection _recordOperation:]
+ -[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]
+ -[MobileAssetHealthReport _submitReportToSplunk:commonFields:sessionId:]
+ -[MobileAssetHealthReport getGreymatterStatus]
+ -[MobileAssetHealthReport getHealthReports]
+ -[MobileAssetHealthReport getSystemInformation].cold.1
+ -[SecureMobileAssetBundle _personalize:error:].cold.1
+ -[SecureMobileAssetBundle isMappableToExclaves:]
+ -[SecureMobileAssetBundle recordAssetGraftStateForEarlyBootTask:]
+ -[SoftwareUpdateSSO initWithOptions:].cold.1
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table148
+ GCC_except_table161
+ GCC_except_table172
+ GCC_except_table212
+ GCC_except_table24
+ GCC_except_table33
+ GCC_except_table40
+ GCC_except_table441
+ GCC_except_table47
+ GCC_except_table631
+ GCC_except_table635
+ GCC_except_table641
+ GCC_except_table643
+ GCC_except_table657
+ GCC_except_table67
+ GCC_except_table789
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table97
+ MABrainUtilityDeviceSupportsExclaves.answer
+ MABrainUtilityDeviceSupportsExclaves.cold.1
+ MABrainUtilityDeviceSupportsExclaves.onceToken
+ MAInternalServerTrustCredential.cold.1
+ MALOG_AUTOCONTROL_SUSPENDRESUME_MASK_block_invoke.onceToken
+ OBJC_IVAR_$_DownloadInfo._nwActivity
+ OBJC_IVAR_$_MADAutoAssetControlManager._bootedOSBuildVersion
+ OBJC_IVAR_$_MADAutoAssetControlManager._cancelingSetJobsByIdentifier
+ OBJC_IVAR_$_MADAutoAssetControlManager._completionCallbacksBySetJobKey
+ OBJC_IVAR_$_MADAutoAssetControlManager._evictedCallbacksByAtomicInstanceUUID
+ OBJC_IVAR_$_MADAutoAssetControlManager._filesystemFileExistAtPathCache
+ OBJC_IVAR_$_MADAutoAssetControlManager._filesystemStartupLookupCount
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferencePerformanceLoggingEnabled
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDetermineLastRequiredTimesOut
+ OBJC_IVAR_$_MADAutoAssetControlManager._preinstalledAssetDescriptorsBySelector
+ OBJC_IVAR_$_MADAutoAssetControlManager._schedulerTickPerformedCrossCheck
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagedAssetToSetDescriptorCache
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagedIsNewOSPromotedCache
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagedSetLookupResults
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagedToDownloaded
+ OBJC_IVAR_$_MADAutoAssetControlManager._stagerResumePostponed
+ OBJC_IVAR_$_MADAutoAssetControlManager._startupTimeBeginSeconds
+ OBJC_IVAR_$_MADAutoAssetControlManager._startupTimeDurationSeconds
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._downloadOptions
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._requiringLoadPriorToUse
+ OBJC_IVAR_$_MADAutoAssetHistory._trackerPushNotification
+ OBJC_IVAR_$_MADAutoAssetJob._boostedToCellular
+ OBJC_IVAR_$_MADAutoAssetJob._boostedToExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToCellular
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToUserInitiated
+ OBJC_IVAR_$_MADAutoAssetJob._downloadingCellular
+ OBJC_IVAR_$_MADAutoAssetJob._downloadingExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._manager
+ OBJC_IVAR_$_MADAutoAssetJob._queuedRequestsForNewJobOnceCanceled
+ OBJC_IVAR_$_MADAutoAssetJob._tryPersonalizePromoted
+ OBJC_IVAR_$_MADAutoAssetLocker._lockCountsBySelector
+ OBJC_IVAR_$_MADAutoAssetLocker._lockCountsTotal
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._LastCheckedDate
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._availableForUseError
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._lastestToVendIsLocked
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._lastestToVendMatchesSetConfig
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._latestDiscoveredAssetSetUUID
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._latestToVendAssetSetUUID
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._newerVersionError
+ OBJC_IVAR_$_MADAutoAssetSetHealthReport._setIdentifier
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._build
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._nonce
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._setConfigurationsToEvict
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._status
+ OBJC_IVAR_$_MADAutoAssetStager._analyticsManager
+ OBJC_IVAR_$_MADAutoAssetStager._loadPersistedPostponed
+ OBJC_IVAR_$_MADAutoAssetStager._optionalAssetSizeAllowed
+ OBJC_IVAR_$_MADAutoAssetStager._startupActivelyStagingAssetCount
+ OBJC_IVAR_$_MADAutoAssetStager._startupAssetTargetBuildVersion
+ OBJC_IVAR_$_MADAutoAssetStager._startupAssetTargetOSVersion
+ OBJC_IVAR_$_MADAutoAssetStager._startupAwaitingStagingAssetCount
+ OBJC_IVAR_$_MADAutoAssetStager._startupCandidateAssetCount
+ OBJC_IVAR_$_MADAutoAssetStager._startupDeterminedAvailableAssetCount
+ OBJC_IVAR_$_MADAutoAssetStager._startupLastStagingFromBuildVersion
+ OBJC_IVAR_$_MADAutoAssetStager._startupLastStagingFromOSVersion
+ OBJC_IVAR_$_MADAutoAssetStager._startupModeByGroups
+ OBJC_IVAR_$_MADAutoAssetStager._startupStagedAssetCount
+ OBJC_IVAR_$_MADAutoAssetStager._startupStagedAssetTotalContentBytes
+ OBJC_IVAR_$_MADAutoSetAtomicInstance._creationReason
+ OBJC_IVAR_$_MADAutoSetAtomicInstance._usageStatus
+ OBJC_IVAR_$_MADAutoSetConfiguration._availableForUseError
+ OBJC_IVAR_$_MADAutoSetConfiguration._discoveredInFlightAtomicInstance
+ OBJC_IVAR_$_MADAutoSetConfiguration._everProvidedLatestToVend
+ OBJC_IVAR_$_MADAutoSetConfiguration._latestAtomicInstanceToVendFromPreSUStaging
+ OBJC_IVAR_$_MADAutoSetConfiguration._latestToVendCachedAssetSetID
+ OBJC_IVAR_$_MADAutoSetConfiguration._latestToVendDownloadedFromLive
+ OBJC_IVAR_$_MADAutoSetConfiguration._latestToVendLastTimeChecked
+ OBJC_IVAR_$_MADAutoSetConfiguration._latestToVendPostedDate
+ OBJC_IVAR_$_MADAutoSetConfiguration._mostRecentlyReceivedCachedAssetSetID
+ OBJC_IVAR_$_MADAutoSetConfiguration._mostRecentlyReceivedDownloadedFromLive
+ OBJC_IVAR_$_MADAutoSetConfiguration._mostRecentlyReceivedLastTimeChecked
+ OBJC_IVAR_$_MADAutoSetConfiguration._mostRecentlyReceivedPostedDate
+ OBJC_IVAR_$_MADAutoSetConfiguration._newerAtomicInstanceOncePersonalized
+ OBJC_IVAR_$_MADAutoSetConfiguration._newerVersionError
+ OBJC_IVAR_$_MADAutoSetConfiguration._previouslyVendedLockedAtomicInstances
+ OBJC_IVAR_$_MADAutoSetConfiguration._ticksUntilPreviousForceUnlocked
+ OBJC_IVAR_$_MANAutoAssetControlStatisticsByCommand._estimateEvictableBytesForSoftwareUpdate
+ OBJC_IVAR_$_MANAutoAssetControlStatisticsByCommand._resumeFromSoftwareUpdate
+ OBJC_IVAR_$_MANAutoAssetControlStatisticsByCommand._suspendForSoftwareUpdate
+ OBJC_IVAR_$_MANAutoAssetControlStatisticsByCommand._suspendResumeStatusForSoftwareUpdate
+ OBJC_IVAR_$_MANAutoAssetSetStatus._latestDownloadedAtomicInstanceFromPreSUStaging
+ OBJC_IVAR_$_MANAutoAssetSetStatus._previouslyVendedLockedAtomicInstance
+ _CC_SHA256
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFPropertyListCreateDeepCopy
+ _MAAutoAssetSuspendResumeForSoftwareUpdateStatusString
+ _MABrainUtilityDeviceSupportsExclaves
+ _MAClientLog.clientLoggers
+ _MAClientLog.cold.1
+ _MAClientLog.onceToken
+ _MAConvertTicksToSeconds
+ _MADLog.cold.1
+ _MADLog.daemonLoggers
+ _MADLog.onceToken
+ _MAMeasurementHashAlgorithmSHA1
+ _MAMeasurementHashAlgorithmSHA256
+ _MAPreferencesIsInternalAllowed.cold.1
+ _MAPreferencesIsVerboseLoggingEnabled.cold.1
+ _MGIsQuestionValid
+ _MobileAssetGetWorkQueue.cold.1
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ _OBJC_CLASS_$_MADAutoAssetSetHealthReport
+ _OBJC_CLASS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ _OBJC_CLASS_$_MAThirdPartyCompatibility
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$__NSURLSessionBackgroundTaskOverrides
+ _OBJC_METACLASS_$_MADAutoAssetSetHealthReport
+ _OBJC_METACLASS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_72
+ _SZExtractorHashTypeSHA256
+ _SecPolicyCreate3PMobileAsset
+ _ZN5swift14VoucherManager9swapToJobEPNS_3JobE.cold.1
+ _ZN5swift18restoreTaskVoucherEPNS_9AsyncTaskE.cold.1
+ _ZN5swift19_swift_tsan_acquireEPv.cold.1
+ _ZN5swift19_swift_tsan_releaseEPv.cold.1
+ _ZN5swift31swift_task_escalateBackdeploy56EPNS_9AsyncTaskENS_11JobPriorityE.cold.1
+ _ZN5swift45swift_task_exitThreadLocalContextBackdeploy56EPc.cold.1
+ _ZN5swift46swift_task_enterThreadLocalContextBackdeploy56EPc.cold.1
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1207
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1605
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2089
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1136
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1140
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1156
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1228
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1229
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1233
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1234
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2266
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1255
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1265
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1121
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1122
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1130
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1131
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2198
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2210
+ __22-[ControlManager init]_block_invoke.1119
+ __24-[MABrainUpdater start:]_block_invoke.380
+ __24-[MABrainUpdater start:]_block_invoke.385
+ __24-[MABrainUpdater start:]_block_invoke.389
+ __27-[MABrainUpdater schedule:]_block_invoke.398
+ __27-[MABrainUpdater schedule:]_block_invoke.443
+ __27-[MABrainUpdater schedule:]_block_invoke.444
+ __27-[MABrainUpdater schedule:]_block_invoke.450
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2247
+ __36-[MABrainUpdater update:completion:]_block_invoke.516
+ __36-[MABrainUpdater update:completion:]_block_invoke.517
+ __36-[MABrainUpdater update:completion:]_block_invoke.524
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1702
+ __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1077
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1672
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1675
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1148
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1195
+ __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.433
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2139
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2140
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1862
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1863
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1869
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.498
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.499
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.501
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1821
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1413
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1250
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1257
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1915
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1241
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1242
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1243
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1499
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.367
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.385
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.391
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.393
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1207
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1228
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1877
+ __66-[MADAutoAssetStager _extendSummaryWithAvailableForStagingAssets:]_block_invoke.1727
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1070
+ __67-[ControlManager handleQueryRequest:clientName:connection:message:]_block_invoke.1348
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1184
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1193
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1194
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2308
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1056
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1057
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1058
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2509
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2510
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1169
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1170
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1171
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1211
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1212
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1216
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3294
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3295
+ __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.393
+ __MABufferToHexString
+ __MAClientLog
+ __MADLog
+ __MAHashDictionary
+ __MAPreferencesCopyNSDictionaryValue
+ __MobileAssetVerifyThirdPartySigning
+ __OBJC_$_CLASS_METHODS_MADAutoAssetSetHealthReport
+ __OBJC_$_CLASS_METHODS_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_CLASS_PROP_LIST_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetControlManager(SoftwareUpdateSuspendResume)
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetSetHealthReport
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoAssetSetHealthReport
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_PROP_LIST_MADAutoAssetSetHealthReport
+ __OBJC_$_PROP_LIST_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_CLASS_PROTOCOLS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_CLASS_RO_$_MADAutoAssetSetHealthReport
+ __OBJC_CLASS_RO_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_METACLASS_RO_$_MADAutoAssetSetHealthReport
+ __OBJC_METACLASS_RO_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ ___108+[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:]_block_invoke
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke
+ ___138-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:fromPreSUStaging:]_block_invoke
+ ___138-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:fromPreSUStaging:]_block_invoke_2
+ ___138-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:fromPreSUStaging:completion:]_block_invoke
+ ___138-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:fromPreSUStaging:completion:]_block_invoke_2
+ ___142+[MADAutoAssetControlManager postSetNotificationName:forClientDomainName:forAssetSetIdentifier:forAtomicInstanceUUID:fromModule:fromLocation:]_block_invoke
+ ___150-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:]_block_invoke
+ ___173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke
+ ___178-[DownloadManager handleDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:notifyingAutoAssetLayer:]_block_invoke
+ ___178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke
+ ___401+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:]_block_invoke
+ ___413-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:]_block_invoke
+ ___43+[SecureMobileAssetBundle getGraftListLock]_block_invoke
+ ___45+[MADAutoAssetSetHealthReport formattedDate:]_block_invoke
+ ___48+[MADAutoAssetLocker copyOfLockCountsBySelector]_block_invoke
+ ___58-[MADAutoAssetStager action_LoadDecideNewOSPromote:error:]_block_invoke
+ ___62+[MADAutoAssetLocker forceGlobalUnlock:atomicInstancesHandle:]_block_invoke
+ ___71-[DownloadManager taskFinishedUpdateState:with:extraInfo:fromLocation:]_block_invoke
+ ___74-[MADAutoAssetStager _limitCachePersistResultByGroupToCount:fromLocation:]_block_invoke
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke
+ ___83-[MADAutoAssetJob handleDownloadConfigJobFinished:withDownloadOptions:configError:]_block_invoke
+ ___97-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleSuspendForSoftwareUpdateRequest:]_block_invoke
+ ___MABrainUtilityDeviceSupportsExclaves_block_invoke
+ ___MAPreferencesIsVerboseLoggingEnabled_block_invoke.cold.1
+ ____MAClientLog_block_invoke
+ ____MADLog_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0l
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
+ ___block_descriptor_232_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s_e5_v8?0l
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e27_q24?0"NSDate"8"NSDate"16l
+ ___block_descriptor_49_e8_32s40s_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s_e8_v12?0B8l
+ ___block_descriptor_65_e8_32s40r48r56r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24l
+ ___block_descriptor_65_e8_32s40s48s56s_e17_v16?0"NSError"8l
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0l
+ ___block_descriptor_74_e8_32s40s48s56bs64r_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16l
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e42_v24?0"MADAutoSetDescriptor"8"NSError"16l
+ ___block_descriptor_98_e8_32s40s48s56s64s72s80s88bs_e42_v24?0"MADAutoSetDescriptor"8"NSError"16l
+ ___copy_helper_block_e8_32s40r48r56r
+ ___copy_helper_block_e8_32s40s48s56b64r
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s
+ ___destroy_helper_block_e8_32s40r48r56r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s
+ ___swift_memcpy8_8
+ __block_literal_global.1042
+ __block_literal_global.1045
+ __block_literal_global.1055
+ __block_literal_global.1057
+ __block_literal_global.1059
+ __block_literal_global.1060
+ __block_literal_global.1062
+ __block_literal_global.1065
+ __block_literal_global.1075
+ __block_literal_global.1081
+ __block_literal_global.1085
+ __block_literal_global.1091
+ __block_literal_global.1096
+ __block_literal_global.1101
+ __block_literal_global.1105
+ __block_literal_global.1106
+ __block_literal_global.1121
+ __block_literal_global.1130
+ __block_literal_global.1145
+ __block_literal_global.1147
+ __block_literal_global.1206
+ __block_literal_global.1218
+ __block_literal_global.1230
+ __block_literal_global.1268
+ __block_literal_global.1310
+ __block_literal_global.1316
+ __block_literal_global.1318
+ __block_literal_global.1345
+ __block_literal_global.1350
+ __block_literal_global.1372
+ __block_literal_global.1424
+ __block_literal_global.1560
+ __block_literal_global.1599
+ __block_literal_global.1607
+ __block_literal_global.1691
+ __block_literal_global.1696
+ __block_literal_global.1701
+ __block_literal_global.1704
+ __block_literal_global.1738
+ __block_literal_global.1762
+ __block_literal_global.2186
+ __block_literal_global.2195
+ __block_literal_global.2227
+ __block_literal_global.2238
+ __block_literal_global.2246
+ __block_literal_global.2254
+ __block_literal_global.2262
+ __block_literal_global.2270
+ __block_literal_global.2278
+ __block_literal_global.2286
+ __block_literal_global.2294
+ __block_literal_global.2308
+ __block_literal_global.2322
+ __block_literal_global.2324
+ __block_literal_global.2386
+ __block_literal_global.383
+ __block_literal_global.391
+ __block_literal_global.3954
+ __block_literal_global.446
+ __block_literal_global.4978
+ __block_literal_global.526
+ __block_literal_global.533
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1095
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1091
+ __hashCFArray
+ __hashCFString
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ _applyCatalogTransforms
+ _cc_disable_dit
+ _ccn_gcd_approximate
+ _ccn_gcd_update_ws
+ _dateAfterTimeTravel
+ _deepMergeDictionaries
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _fsgetpath
+ _getDaemonAsyncConnectionQueue.cold.1
+ _getDaemonAsyncHandlerQueue.cold.1
+ _getpid
+ _hashCFString.cold.1
+ _hashCFString.cold.2
+ _hashCFString.cold.3
+ _hashCFType.cold.1
+ _isAssetTypeAllowlisted.cold.1
+ _kMobileAssetPreferencesAutoAssetPerformanceLoggingEnabled
+ _kMobileAssetPreferencesAutoAssetStagerDetermineLastRequiredTimesOut
+ _kMobileAssetPreferencesAutoAssetSuspendResumeEnabled
+ _kMobileAssetPreferencesAutoAssetSuspendResumeForSUSetsOverride
+ _kMobileAssetPreferencesForceBatteryAllowedDownload
+ _kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA256
+ _mach_absolute_time
+ _nw_activity_activate
+ _nw_activity_complete_with_reason
+ _nw_activity_create
+ _objc_msgSend$LastCheckedDate
+ _objc_msgSend$_acceptPersonalizationFromPSUSToBecomeLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:
+ _objc_msgSend$_acceptPersonalizationToAttempt:forAtomicEntry:
+ _objc_msgSend$_acceptPersonalizationToAttempt:forSetDescriptor:withCandidates:extendingToBePersonalized:
+ _objc_msgSend$_acceptPersonalizationToAttempt:forSetLookupResult:withCandidates:extendingToBePersonalized:
+ _objc_msgSend$_acceptPersonalizationToProvideLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:
+ _objc_msgSend$_acceptPersonalizationToProvidePreinstalled:forSetConfiguration:withCandidates:extendingToBePersonalized:
+ _objc_msgSend$_acceptStagingClientRequest:fromLocation:adoptingSpecifiedTarget:
+ _objc_msgSend$_addCompletionCallbackForSetJobKey:completionCallback:
+ _objc_msgSend$_addEvictedCallbackForAtomicInstanceUUID:completionCallback:
+ _objc_msgSend$_allPreInstalledDescriptor:forAssetType:
+ _objc_msgSend$_applyBackgroundTaskOverrides:
+ _objc_msgSend$_clearAtomicInstanceFromAllSetConfigurations:fromLocation:
+ _objc_msgSend$_clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:
+ _objc_msgSend$_constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:
+ _objc_msgSend$_currentState
+ _objc_msgSend$_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:
+ _objc_msgSend$_effectiveConfiguration
+ _objc_msgSend$_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:
+ _objc_msgSend$_errorUnlessSameVersionFound:changedReportedError:
+ _objc_msgSend$_filesystemCachedInfo:forPath:
+ _objc_msgSend$_forceSetUngraftAndEliminateAllSetLocks:forSetDescriptor:
+ _objc_msgSend$_handleClientAlterLockOperationForDescriptor:forEventInfo:error:
+ _objc_msgSend$_handleEstimateEvictableBytesForSoftwareUpdateRequestWithBytesBySetIdentifier:
+ _objc_msgSend$_handleResumeFromSoftwareUpdateRequest
+ _objc_msgSend$_handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_limitCachePersistResultByGroupToCount:fromLocation:
+ _objc_msgSend$_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:
+ _objc_msgSend$_logPersistedConfigLoad:message:
+ _objc_msgSend$_nonceFileURL
+ _objc_msgSend$_persistAssetLock:operation:forAssetLock:withDeltaLockCount:message:
+ _objc_msgSend$_persistedKnownDescriptorForFullAssetSelector:
+ _objc_msgSend$_persistedKnownDescriptorForPersistedEntryID:
+ _objc_msgSend$_preinstalledTrackBySelector:
+ _objc_msgSend$_recordFailedOperation:forReason:
+ _objc_msgSend$_recordOperation:
+ _objc_msgSend$_removeAssetLock:removingAssetLock:lastClient:forSelector:message:
+ _objc_msgSend$_removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:
+ _objc_msgSend$_removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:
+ _objc_msgSend$_replyHaveStagedContent:withEventInfo:
+ _objc_msgSend$_schedulerTickOccurred
+ _objc_msgSend$_setConfigurationAdjustedFrom:basedOnSetTarget:
+ _objc_msgSend$_shortTermForceForget:forSetDescriptor:
+ _objc_msgSend$_softwareUpdateSuspendResumeEligibleSetEntryIDs
+ _objc_msgSend$_startupActivationProcessIdentifier
+ _objc_msgSend$_stateFileURL
+ _objc_msgSend$_submitReportToCoreAnalytics:commonFields:sessionId:
+ _objc_msgSend$_submitReportToSplunk:commonFields:sessionId:
+ _objc_msgSend$_trackPerformanceStartupBegin
+ _objc_msgSend$_updateDownloadOptions:
+ _objc_msgSend$_updateUserInitiatedFields
+ _objc_msgSend$action_BoostConfig:error:
+ _objc_msgSend$action_DecrementTickDriven:error:
+ _objc_msgSend$action_LoadDecideNewOSPromote:error:
+ _objc_msgSend$action_SchedulerJobDownloaded:error:
+ _objc_msgSend$action_SchedulerJobFoundSame:error:
+ _objc_msgSend$addNWActivityToDownloadInfo:andTask:andLabel:
+ _objc_msgSend$addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:fromLocation:
+ _objc_msgSend$addToLockCountsBySelector:addingAssetLock:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$assetConfigJobFinished:withDownloadInfo:error:
+ _objc_msgSend$assetPersonalizatonAttemptCompletePostEvent:withControlParam:
+ _objc_msgSend$atomicInstanceDropOncePersonalized:forSetConfiguration:
+ _objc_msgSend$atomicInstanceForSetDescriptor:
+ _objc_msgSend$atomicInstanceForceUnlock:forgettingAtomicInstance:
+ _objc_msgSend$atomicInstanceFromPSUSLookupResultOncePersonalized:forSetConfiguration:
+ _objc_msgSend$atomicInstanceIsCurrentlyLocked:
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:
+ _objc_msgSend$atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:
+ _objc_msgSend$atomicInstanceUpdateUsageStatus:toNewStatus:forAtomicInstance:
+ _objc_msgSend$autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:withCatalogLookupResponse:
+ _objc_msgSend$autoSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:
+ _objc_msgSend$autoSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:
+ _objc_msgSend$boostedToCellular
+ _objc_msgSend$boostedToExpensive
+ _objc_msgSend$bootedOSBuildVersion
+ _objc_msgSend$bucketedDays:
+ _objc_msgSend$byGroupAvailableForStagingAttributes
+ _objc_msgSend$cancelActiveSetJob:activeSetJob:
+ _objc_msgSend$cancelingSetJobsByIdentifier
+ _objc_msgSend$clear
+ _objc_msgSend$completionCallbacksBySetJobKey
+ _objc_msgSend$configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:
+ _objc_msgSend$configuredToCellular
+ _objc_msgSend$configuredToExpensive
+ _objc_msgSend$configuredToUserInitiated
+ _objc_msgSend$considerDownloadedWithPSUSLookupResultsForLatestToVend
+ _objc_msgSend$copyGraftList:
+ _objc_msgSend$copyOfLockCountsBySelector
+ _objc_msgSend$creationReason
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentStatusWithStateHandle:
+ _objc_msgSend$daemonProcessStartupBegun
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:allowingNilObject:
+ _objc_msgSend$decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:withEncodeClasses:allowingNilObject:
+ _objc_msgSend$decrementClientRequestCount:forEventInfo:
+ _objc_msgSend$dedupAtomicEntries:
+ _objc_msgSend$defaultThirdPartyServerURLForAssetType:
+ _objc_msgSend$discoveredInFlightAtomicInstance
+ _objc_msgSend$doesSetConfiguration:coverAssetDescriptor:
+ _objc_msgSend$doesSetDescriptor:satisfySetConfiguration:allowingMoreDownloaded:
+ _objc_msgSend$doesSetDescriptorReferenceAllPreInstalledContent:
+ _objc_msgSend$doesSetDescriptorWithoutVersion:referenceAssetDescriptor:
+ _objc_msgSend$doesSetJobDescriptor:representSameContentAs:
+ _objc_msgSend$downloadingCellular
+ _objc_msgSend$downloadingExpensive
+ _objc_msgSend$ensureStagerFullyResumed
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$errorSummaryForSplunk:
+ _objc_msgSend$estimateEvictableBytesForSoftwareUpdate
+ _objc_msgSend$eventPayloadForCoreAnalytics
+ _objc_msgSend$eventPayloadForSplunk
+ _objc_msgSend$everProvidedLatestToVend
+ _objc_msgSend$evictedCallbacksByAtomicInstanceUUID
+ _objc_msgSend$existsOnFilesystem
+ _objc_msgSend$filesystemDoesDirectoryExist:atPath:isDirectory:
+ _objc_msgSend$filesystemDoesFileExist:atPath:
+ _objc_msgSend$filesystemFileExistAtPathCache
+ _objc_msgSend$filesystemStartupLookupCount
+ _objc_msgSend$finishSuspendedResumeFromPersisted
+ _objc_msgSend$firstSchedulerCrosscheckTrim
+ _objc_msgSend$firstSchedulerCrosscheckTrimAtomicInstances
+ _objc_msgSend$firstSchedulerCrosscheckTrimSetDescriptors
+ _objc_msgSend$forceGlobalUnlock:atomicInstancesHandle:
+ _objc_msgSend$forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:
+ _objc_msgSend$formAvailableForStagingByCombiningRequiredAndOptional:
+ _objc_msgSend$formattedDate:
+ _objc_msgSend$getGraftListLock
+ _objc_msgSend$getGreymatterStatus
+ _objc_msgSend$getHealthReports
+ _objc_msgSend$handleDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:notifyingAutoAssetLayer:
+ _objc_msgSend$handleDownloadConfigJobFinished:withDownloadOptions:configError:
+ _objc_msgSend$handleEstimateEvictableBytesForSoftwareUpdateRequest:
+ _objc_msgSend$handleResumeFromSoftwareUpdateRequest:
+ _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:
+ _objc_msgSend$handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:
+ _objc_msgSend$handleStatusForSoftwareUpdateRequest:
+ _objc_msgSend$handleSuspendForSoftwareUpdateRequest:
+ _objc_msgSend$handleSuspendResumeForSoftwareUpdateDaemonStartup
+ _objc_msgSend$includesEntryForAssetType:
+ _objc_msgSend$indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:
+ _objc_msgSend$indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
+ _objc_msgSend$initForConfigFinishedJobID:andDownloadOptions:withError:
+ _objc_msgSend$initForSetAtomicInstanceUUID:
+ _objc_msgSend$initForSetConfiguration:withSetDescriptor:withCatalogLookupResponse:
+ _objc_msgSend$initForSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:
+ _objc_msgSend$initForSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$initWithEstimatedEvictableBytes:
+ _objc_msgSend$initWithNonce:status:setConfigurationsToEvict:
+ _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$isAnyAssetFromSetFromNewOSPromoted:
+ _objc_msgSend$isAtomicInstanceForCurrentSetJob:
+ _objc_msgSend$isAtomicInstanceLatestToVendForSet:
+ _objc_msgSend$isEveryAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:
+ _objc_msgSend$isMappableToExclaves:
+ _objc_msgSend$isNoWaitRequestInvolvingSecureAsset:
+ _objc_msgSend$isSuspendedForSoftwareUpdate:forAssetSetIdentifier:
+ _objc_msgSend$isThirdPartyAssetType:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$lastestToVendIsLocked
+ _objc_msgSend$lastestToVendMatchesSetConfig
+ _objc_msgSend$latestAtomicInstanceToVendFromPreSUStaging
+ _objc_msgSend$latestDiscoveredAssetSetUUID
+ _objc_msgSend$latestDownloadedAtomicInstanceFromPreSUStaging
+ _objc_msgSend$latestToVendAssetSetUUID
+ _objc_msgSend$latestToVendCachedAssetSetID
+ _objc_msgSend$latestToVendDownloadedFromLive
+ _objc_msgSend$latestToVendLastTimeChecked
+ _objc_msgSend$latestToVendPostedDate
+ _objc_msgSend$loadPersistedCrosscheckStaleForceUnlock
+ _objc_msgSend$loadPersistedPostponed
+ _objc_msgSend$localContentURLOfAssetDescriptor
+ _objc_msgSend$locateCancelingSetJobForClientDomain:byIdentifier:
+ _objc_msgSend$locateSetDescriptor:forAtomicInstanceUUID:requireExists:
+ _objc_msgSend$locateSetDescriptorForStagingDescriptor:
+ _objc_msgSend$locateSetLookupResultSatisfying:
+ _objc_msgSend$locateStagedSetDescriptorFor:
+ _objc_msgSend$lockCountsBySelector
+ _objc_msgSend$lockCountsTotal
+ _objc_msgSend$manager
+ _objc_msgSend$mostRecentlyReceivedCachedAssetSetID
+ _objc_msgSend$mostRecentlyReceivedDownloadedFromLive
+ _objc_msgSend$mostRecentlyReceivedLastTimeChecked
+ _objc_msgSend$mostRecentlyReceivedPostedDate
+ _objc_msgSend$neededBytes
+ _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:
+ _objc_msgSend$newSetConfigurationForAssetSetIdentifier:withAutoAssetEntries:
+ _objc_msgSend$newSetConfigurationForClientDomainName:forAssetSetIdentifier:withAutoAssetEntries:
+ _objc_msgSend$newerAtomicInstanceOncePersonalized
+ _objc_msgSend$nonce
+ _objc_msgSend$notifyEvictedCallbacksForSetDescriptor:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$nwActivity
+ _objc_msgSend$objectIsEqual:to:
+ _objc_msgSend$optionalAssetSizeAllowed
+ _objc_msgSend$permitThirdPartySigningForAssetType:outOrganizations:
+ _objc_msgSend$persistDate:forKey:
+ _objc_msgSend$persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:
+ _objc_msgSend$persistedKnownDescriptorForSetAtomicEntry:
+ _objc_msgSend$populationTypeString
+ _objc_msgSend$postSetNotificationName:forClientDomainName:forAssetSetIdentifier:forAtomicInstanceUUID:fromModule:fromLocation:
+ _objc_msgSend$preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:
+ _objc_msgSend$preferencePerformanceLoggingEnabled
+ _objc_msgSend$preferenceStagerDetermineLastRequiredTimesOut
+ _objc_msgSend$preinstalledAssetDescriptorsBySelector
+ _objc_msgSend$previouslyVendedLockedAtomicInstances
+ _objc_msgSend$previouslyVendedLockedSummary
+ _objc_msgSend$queuedRequestsForNewJobOnceCanceled
+ _objc_msgSend$readyToCommitPrePersonalized:forSetDescriptor:
+ _objc_msgSend$recordAssetGraftStateForEarlyBootTask:
+ _objc_msgSend$recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:
+ _objc_msgSend$recordFailedOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:
+ _objc_msgSend$recordFailedOperation:fromLayer:withSelectors:failingWithError:
+ _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:
+ _objc_msgSend$recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:withReason:
+ _objc_msgSend$recordOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forSelectors:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withSelector:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$refreshDownloadedToManager:
+ _objc_msgSend$refreshSetFoundToManager:fromLocation:
+ _objc_msgSend$removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:performingHardEliminate:error:
+ _objc_msgSend$reportSetCatalogDecideFound:fromLocation:
+ _objc_msgSend$requiringLoadPriorToUse
+ _objc_msgSend$resumeFromSoftwareUpdate
+ _objc_msgSend$schedulerTickOccurred
+ _objc_msgSend$schedulerTickPerformedCrossCheck
+ _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:fromPreSUStaging:
+ _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:fromPreSUStaging:completion:
+ _objc_msgSend$sendMobileAssetHealthReport:commonFields:sessionId:
+ _objc_msgSend$setAllowsConstrainedNetworkAccess:
+ _objc_msgSend$setAllowsExpensiveNetworkAccess:
+ _objc_msgSend$setAtomicInstanceUUID
+ _objc_msgSend$setBoostedToCellular:
+ _objc_msgSend$setBoostedToExpensive:
+ _objc_msgSend$setCompletionCallbacksBySetJobKey:
+ _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:
+ _objc_msgSend$setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:
+ _objc_msgSend$setConfigurationAssetSetIDLatestToVend:fromSetDescriptor:forSetConfiguration:buildingPersistReason:
+ _objc_msgSend$setConfigurationAssetSetIDMostRecentlyReceived:fromSetDescriptor:forSetConfiguration:buildingPersistReason:
+ _objc_msgSend$setConfigurationForDescriptorIfManagedAsSet:
+ _objc_msgSend$setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:
+ _objc_msgSend$setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:
+ _objc_msgSend$setConfigurationPersist:fromLocation:forReason:dueToAlter:forHistoryOperation:
+ _objc_msgSend$setConfigurationPreviouslyVendedLockedAtomicInstances:
+ _objc_msgSend$setConfigurationRemovedAtomicInstance:fromLocation:
+ _objc_msgSend$setConfigurationTickForPreviouslyVended
+ _objc_msgSend$setConfigurationTrackLatestToVend:forSetConfiguration:becomingLatestToVend:historyOperation:fromPreSUStaging:
+ _objc_msgSend$setConfigurationsToEvict
+ _objc_msgSend$setConfiguredToCellular:
+ _objc_msgSend$setConfiguredToExpensive:
+ _objc_msgSend$setConfiguredToUserInitiated:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setDescriptorWalkKeys
+ _objc_msgSend$setDescriptorWalkLocate:forKey:
+ _objc_msgSend$setDiscoveredInFlightAtomicInstance:
+ _objc_msgSend$setEstimateEvictableBytesForSoftwareUpdate:
+ _objc_msgSend$setEverProvidedLatestToVend:
+ _objc_msgSend$setEvictedCallbacksByAtomicInstanceUUID:
+ _objc_msgSend$setFilesystemFileExistAtPathCache:
+ _objc_msgSend$setFilesystemStartupLookupCount:
+ _objc_msgSend$setIdentifier
+ _objc_msgSend$setJobIndicationOfPotentialLatestToVend:forEventInfo:issuingClientReply:
+ _objc_msgSend$setLastCheckedDate:
+ _objc_msgSend$setLastestToVendIsLocked:
+ _objc_msgSend$setLastestToVendMatchesSetConfig:
+ _objc_msgSend$setLatestAtomicInstanceToVendFromPreSUStaging:
+ _objc_msgSend$setLatestDiscoveredAssetSetUUID:
+ _objc_msgSend$setLatestToVendAssetSetUUID:
+ _objc_msgSend$setLatestToVendCachedAssetSetID:
+ _objc_msgSend$setLatestToVendDownloadedFromLive:
+ _objc_msgSend$setLatestToVendLastTimeChecked:
+ _objc_msgSend$setLatestToVendPostedDate:
+ _objc_msgSend$setLoadPersistedPostponed:
+ _objc_msgSend$setLockCountsBySelector:
+ _objc_msgSend$setLockCountsTotal:
+ _objc_msgSend$setLockUsageMapLockCount
+ _objc_msgSend$setMostRecentlyReceivedCachedAssetSetID:
+ _objc_msgSend$setMostRecentlyReceivedDownloadedFromLive:
+ _objc_msgSend$setMostRecentlyReceivedLastTimeChecked:
+ _objc_msgSend$setMostRecentlyReceivedPostedDate:
+ _objc_msgSend$setNewerAtomicInstanceOncePersonalized:
+ _objc_msgSend$setNwActivity:
+ _objc_msgSend$setOptionalAssetSizeAllowed:
+ _objc_msgSend$setPreviouslyVendedLockedAtomicInstances:
+ _objc_msgSend$setQueuedRequestsForNewJobOnceCanceled:
+ _objc_msgSend$setResumeFromSoftwareUpdate:
+ _objc_msgSend$setSchedulerTickPerformedCrossCheck:
+ _objc_msgSend$setSetIdentifier:
+ _objc_msgSend$setStagedAssetToSetDescriptorCache:
+ _objc_msgSend$setStagedIsNewOSPromotedCache:
+ _objc_msgSend$setStagedSetLookupResults:
+ _objc_msgSend$setStagedToDownloaded:
+ _objc_msgSend$setStagerResumePostponed:
+ _objc_msgSend$setStartupActivelyStagingAssetCount:
+ _objc_msgSend$setStartupAssetTargetBuildVersion:
+ _objc_msgSend$setStartupAssetTargetOSVersion:
+ _objc_msgSend$setStartupAwaitingStagingAssetCount:
+ _objc_msgSend$setStartupCandidateAssetCount:
+ _objc_msgSend$setStartupDeterminedAvailableAssetCount:
+ _objc_msgSend$setStartupLastStagingFromBuildVersion:
+ _objc_msgSend$setStartupLastStagingFromOSVersion:
+ _objc_msgSend$setStartupModeByGroups:
+ _objc_msgSend$setStartupStagedAssetCount:
+ _objc_msgSend$setStartupStagedAssetTotalContentBytes:
+ _objc_msgSend$setStartupTimeDurationSeconds:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setSuspendForSoftwareUpdate:
+ _objc_msgSend$setSuspendResumeStatusForSoftwareUpdate:
+ _objc_msgSend$setTicksUntilPreviousForceUnlocked:
+ _objc_msgSend$setTryPersonalizePromoted:
+ _objc_msgSend$setUsageStatus:
+ _objc_msgSend$set_nw_activity:
+ _objc_msgSend$set_shouldSkipPreferredClientCertificateLookup:
+ _objc_msgSend$shortTermLockFilesHealthCheck
+ _objc_msgSend$shortTermLockSetDescriptor:forSetDescriptor:forSpecificAtomicInstance:
+ _objc_msgSend$shortUUID:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$splitOutAvailableForStagingByGroup:forGroupDetermine:
+ _objc_msgSend$stagedAssetToSetDescriptorCache
+ _objc_msgSend$stagedIsNewOSPromotedCache
+ _objc_msgSend$stagerResumePostponed
+ _objc_msgSend$stagerResumed:withSetLookupResults:requiringLoadPriorToUse:
+ _objc_msgSend$startupActivationCompleted:
+ _objc_msgSend$startupActivationIsFirstExecutionSinceBoot:
+ _objc_msgSend$startupActivationResourceSummary
+ _objc_msgSend$startupActivelyStagingAssetCount
+ _objc_msgSend$startupAssetTargetBuildVersion
+ _objc_msgSend$startupAssetTargetOSVersion
+ _objc_msgSend$startupAwaitingStagingAssetCount
+ _objc_msgSend$startupCandidateAssetCount
+ _objc_msgSend$startupDeterminedAvailableAssetCount
+ _objc_msgSend$startupLastStagingFromBuildVersion
+ _objc_msgSend$startupLastStagingFromOSVersion
+ _objc_msgSend$startupModeByGroups
+ _objc_msgSend$startupStagedAssetCount
+ _objc_msgSend$startupStagedAssetTotalContentBytes
+ _objc_msgSend$startupTimeBeginSeconds
+ _objc_msgSend$startupTimeDurationSeconds
+ _objc_msgSend$summaryOfAssetSelectors:
+ _objc_msgSend$suspendForSoftwareUpdate
+ _objc_msgSend$suspendResumeStatusForSoftwareUpdate
+ _objc_msgSend$suspendedSetConfigurationsFromPreviousOS
+ _objc_msgSend$suspendedSetConfigurationsHasCurrentNonce
+ _objc_msgSend$taskFinishedUpdateState:with:extraInfo:fromLocation:
+ _objc_msgSend$taskFinishedUpdateState:with:fromLocation:
+ _objc_msgSend$ticksUntilPreviousForceUnlocked
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$totalFilesystemSpace
+ _objc_msgSend$trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:isPromoted:
+ _objc_msgSend$trackDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:
+ _objc_msgSend$trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:
+ _objc_msgSend$trackPerformanceIteration:ofContainer:
+ _objc_msgSend$trackPerformanceIteration:ofContainer:forSelector:
+ _objc_msgSend$trackPerformancePhaseBegin:
+ _objc_msgSend$trackPerformancePhaseEnd:
+ _objc_msgSend$trackPerformanceStartupEnd:
+ _objc_msgSend$trackPerformanceStartupStep:beginningStep:
+ _objc_msgSend$trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:fromPreSUStaging:
+ _objc_msgSend$trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:
+ _objc_msgSend$trackerPushNotification
+ _objc_msgSend$trimmedSetIdentifier:
+ _objc_msgSend$tryPersonalizePromoted
+ _objc_msgSend$typeAndSpecifierKey
+ _objc_msgSend$typeAndSpecifierKeyForAssetType:andAssetSpecifier:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$uploadTaskWithRequest:fromData:
+ _objc_msgSend$usageStatus
+ _objc_msgSend$validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:
+ _objc_msgSend$wouldSetDescriptorForStagedPlusPrePersonalizedVendAtomicInstance:
+ _objc_msgSend$write
+ _objc_msgSend$writeNewSuspendingStateWithNonce:setConfigurationsToEvict:
+ _os_eligibility_get_domain_answer
+ _preferencesDomainProtectionDispatchQueue.cold.1
+ _swift_getTupleTypeMetadata2
+ _symbolic _____ 16CryptoKit_Static19CorecryptoCurveTypeV
+ _symbolic _____ SS5IndexV
+ _unregisterMappedExclavePath
+ assetIdDisallowedCharacterSet.cold.1
+ assetTypeDisallowedCharacterSet.cold.1
+ atfork_child.cold.1
+ atfork_parent.cold.1
+ atfork_prepare.cold.1
+ cc_log_default.cold.1
+ ccrng_getentropy_generate.cold.1
+ downloadManagerDecodeClasses.cold.1
+ epochToDate.cold.1
+ extractorDecodeClasses.cold.1
+ filesystemMetadataLastRefreshDate.cold.1
+ filesystemProtectionQueue.cold.1
+ formattedDate:.formatter
+ formattedDate:.onceToken
+ generate.cold.1
+ getControlManager.cold.1
+ getDownloadManager.cold.1
+ getGraftListLock.lock
+ getGraftListLock.onceToken
+ getSoftwareUpdateTypes.cold.1
+ getSupportedAnalyticsEventFields.cold.1
+ get_aks_client_connection.cold.1
+ get_time_nsec.cold.1
+ init.cold.1
+ init.cold.2
+ isExternalPreReleaseAssetType.cold.1
+ isExternalPreReleaseAssetType.isVM
+ isSSONeededForURL.cold.1
+ isXMLAssetType.cold.1
+ loadDecodeClasses.cold.1
+ preservedIdsDecodeClasses.cold.1
+ purposeDisallowedCharacterSet.cold.1
+ purposeIgnoredCharacterSet.cold.1
+ queryDecodeClasses.cold.1
+ supportedAssetFormatsArray.cold.1
+ tokenFileDisallowedCharacterSet.cold.1
+ urlSupportsAuthenticatedPallas.cold.1
+ usingCentralizedCachedelete.cold.1
- +[MADAutoAssetAuthorizationPolicy isConnection:authorizedForMessage:].cold.1
- +[MADAutoAssetConnector alteredMonitoringMarkers:withTriggeredNoRetry:withTriggeredRequiringRetry:].cold.1
- +[MADAutoAssetConnector observedNetworkPathToServerDown:].cold.1
- +[MADAutoAssetConnector observedNetworkPathToServerUp:].cold.1
- +[MADAutoAssetConnector resumeMonitoringMarkers:withMarkersRequiringRetry:].cold.1
- +[MADAutoAssetConnector scheduledMarkerFinished:withPotentialNetworkFailure:].cold.1
- +[MADAutoAssetConnector simulateNetworkPathDown:].cold.1
- +[MADAutoAssetConnector simulateNetworkPathUp:].cold.1
- +[MADAutoAssetControlManager assetConfigJobFinished:error:]
- +[MADAutoAssetControlManager autoAssetJobIssueReply:forAutoAssetSelector:withAutoAssetUUID:fromAutoAssetJob:withOriginalSelector:withJobInformation:withResponseError:].cold.1
- +[MADAutoAssetControlManager autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:]
- +[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:]
- +[MADAutoAssetControlManager postSetNotificationName:forAssetSetIdentifier:fromModule:fromLocation:]
- +[MADAutoAssetControlManager restoreVersionFromOSVersion:].cold.1
- +[MADAutoAssetControlManager stagerResumed:withSetLookupResults:]
- +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
- +[MADAutoAssetHistoryTracker nameForHistoryType:].cold.1
- +[MADAutoAssetLocker addClientLockReasons:basedOnControl:].cold.1
- +[MADAutoAssetLocker copyOfLocksBySelector].cold.1
- +[MADAutoAssetLocker copyOfSetLocksByDescriptor]
- +[MADAutoAssetLocker currentSetLockUsageEliminatingOtherThanSetAtomicInstances:].cold.1
- +[MADAutoAssetLocker eliminateAllPreviousSetLocksByClient:forSetDescriptor:].cold.1
- +[MADAutoAssetLocker eliminateAllPreviousSetLocksNoLongerTracked:].cold.1
- +[MADAutoAssetLocker eliminateAllPreviousSetLocksNoLongerTracked:].cold.2
- +[MADAutoAssetLocker endedAllPreviousLocksByClientProcessName:withClientProcessID:forAssetSelector:endError:]
- +[MADAutoAssetLocker forceGlobalUnlock:]
- +[MADAutoAssetLocker forceGlobalUnlock:].cold.1
- +[MADAutoAssetLocker lockedSelectorsForEliminate:].cold.1
- +[MADAutoAssetLocker newCurrentLockUsageForSelector:].cold.1
- +[MADAutoAssetLocker newCurrentSetLockUsageForDescriptor:].cold.1
- +[MADAutoAssetLocker persistedLocksCount].cold.1
- +[MADAutoAssetLookupCache cachedLookupResultForSetConfiguration:forStaging:].cold.1
- +[MADAutoAssetLookupCache clearLookupResultsForSetConfiguration:].cold.1
- +[MADAutoAssetLookupCache recordLookupResult:forSetConfiguration:forStaging:].cold.1
- +[MADAutoAssetScheduler addScheduledJobs:basedOnControl:].cold.1
- +[MADAutoAssetScheduler controlEliminateSelector:].cold.1
- +[MADAutoAssetScheduler controlEliminateSelector:].cold.2
- +[MADAutoAssetScheduler controlEliminateSetDomainName:forAssetSetIdentifier:indicatingWhenEliminated:].cold.1
- +[MADAutoAssetScheduler controlEliminateSetDomainName:forAssetSetIdentifier:indicatingWhenEliminated:].cold.2
- +[MADAutoAssetScheduler forceGlobalForget:].cold.1
- +[MADAutoAssetScheduler jobFinishedForSelector:withPotentialNetworkFailure:].cold.1
- +[MADAutoAssetScheduler jobFinishedForSetDomainName:forAssetSetIdentifier:withPotentialNetworkFailure:].cold.1
- +[MADAutoAssetScheduler jobFinishedForSetDomainName:forAssetSetIdentifier:withPotentialNetworkFailure:].cold.2
- +[MADAutoAssetScheduler jobsAwaitingTrigger].cold.1
- +[MADAutoAssetScheduler newSetPolicyForDomainName:forAssetSetIdentifier:].cold.1
- +[MADAutoAssetScheduler persistedScheduledCount].cold.1
- +[MADAutoAssetScheduler schedulePushNotifications:].cold.1
- +[MADAutoAssetScheduler schedulePushNotifications:].cold.2
- +[MADAutoAssetScheduler scheduleSelector:triggeringAtIntervalSecs:].cold.1
- +[MADAutoAssetScheduler scheduleSelector:triggeringAtIntervalSecs:].cold.2
- +[MADAutoAssetScheduler scheduleSelector:triggeringAtIntervalSecs:].cold.3
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.1
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.2
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.3
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.4
- +[MADAutoAssetScheduler scheduleSetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:forSetConfiguration:].cold.5
- +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.1
- +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.2
- +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.3
- +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.4
- +[MADAutoAssetSecure depersonalizeIfSecure:forDescriptor:].cold.1
- +[MADAutoAssetSecure depersonalizeIfSecure:forDescriptor:].cold.2
- +[MADAutoAssetSecure getGraftPath:forDescriptor:].cold.1
- +[MADAutoAssetSecure graftSecureAsset:secureAssetBundle:forAssetID:withSelector:error:].cold.1
- +[MADAutoAssetSecure graftSecureAsset:secureAssetBundle:forAssetID:withSelector:error:].cold.2
- +[MADAutoAssetSecure isGraftedOrMounted:forDescriptor:].cold.1
- +[MADAutoAssetSecure isGraftedOrMounted:forDescriptor:].cold.2
- +[MADAutoAssetSecure isPersonalizationOrGraftingRequired:forDescriptor:].cold.1
- +[MADAutoAssetSecure isPersonalizationOrGraftingRequired:forDescriptor:].cold.2
- +[MADAutoAssetSecure isPersonalizationOrGraftingRequired:forSetDescriptor:].cold.1
- +[MADAutoAssetSecure isPersonalizationRequired:forDescriptor:].cold.1
- +[MADAutoAssetSecure isPersonalizationRequired:forDescriptor:].cold.2
- +[MADAutoAssetSecure isPersonalizationRequired:forSetDescriptor:].cold.1
- +[MADAutoAssetSecure isPrePersonalized:forDescriptor:].cold.1
- +[MADAutoAssetSecure isPrePersonalized:forDescriptor:].cold.2
- +[MADAutoAssetSecure isSecureAsset:forDescriptor:].cold.1
- +[MADAutoAssetSecure isSecureAsset:forDescriptor:].cold.2
- +[MADAutoAssetSecure latestDownloadedAtomicInstanceEntries:forSetDescriptor:].cold.1
- +[MADAutoAssetSecure orphanedProcessLifeLocks:]
- +[MADAutoAssetSecure removeAllPersisted].cold.1
- +[MADAutoAssetSecure secureBundleForAssetType:assetId:].cold.1
- +[MADAutoAssetSecure ungraftIfNotAccessible:].cold.1
- +[MADAutoAssetSecure ungraftIfNotAccessible:].cold.2
- +[MADAutoAssetStager autoAssetStagerJobDetermineDone:withBaseForStagingDescriptors:withDetermineError:].cold.1
- +[MADAutoAssetStager autoAssetStagerJobDownloadDone:withDownloadedDescriptor:withDownloadError:].cold.1
- +[MADAutoAssetStager autoAssetStagerJobDownloadProgress:withProgressError:].cold.1
- +[MADAutoAssetStager autoAssetStagerJobFailedToStart:].cold.1
- +[MADAutoAssetStager clientCancelOperation:].cold.1
- +[MADAutoAssetStager clientDetermineAllAvailable:].cold.1
- +[MADAutoAssetStager clientDetermineGroupsAvailable:].cold.1
- +[MADAutoAssetStager clientDownloadAll:].cold.1
- +[MADAutoAssetStager clientDownloadAll:].cold.2
- +[MADAutoAssetStager clientDownloadAll:].cold.3
- +[MADAutoAssetStager clientDownloadGroups:].cold.1
- +[MADAutoAssetStager clientDownloadGroups:].cold.2
- +[MADAutoAssetStager clientDownloadGroups:].cold.3
- +[MADAutoAssetStager clientEraseAll:].cold.1
- +[MADAutoAssetStager clientPurgeAll:].cold.1
- +[MADAutoAssetStager controlAlreadyDownloadedDescriptors:withSetConfigurations:withSetTargets:withScheduledJobs:].cold.1
- +[MADAutoAssetStager controlConvertStagedToDownloaded:].cold.1
- +[MADAutoAssetStager controlCopyCurrentStagedDescriptors].cold.1
- +[MADAutoAssetStager controlEliminateSelector:].cold.1
- +[MADAutoAssetStager controlEliminateSetConfiguration:].cold.1
- +[MADAutoAssetStager controlForcePurge:].cold.1
- +[MADAutoAssetStager controlStatisticsClientRepliesSuccess:clientRepliesFailure:totalStaged:totalUnstaged:clearingAfter:].cold.1
- +[MADAutoAssetStager extendSummaryWithAvailableForStagingAssets:].cold.1
- +[MADAutoAssetStager extendSummaryWithDeterminedAssets:basedOnControl:].cold.1
- +[MADAutoAssetStager extendSummaryWithStagedAssets:basedOnControl:].cold.1
- +[MADAutoAssetStager extendSummaryWithStagingAssets:basedOnControl:].cold.1
- +[MADAutoAssetStager garbageCollectEliminateSelector:].cold.1
- +[MADAutoAssetStager persistedStagedCount].cold.1
- +[MADAutoSetLocker addClientLockReasons:basedOnControl:]
- +[MADAutoSetLocker additionalLockedByClient:forAssetSelector:forLockReason:withUsagePolicy:lockError:]
- +[MADAutoSetLocker autoAssetLocker]
- +[MADAutoSetLocker continuedLockByClient:forAssetSelector:forLockReason:withUsagePolicy:continueError:]
- +[MADAutoSetLocker copyOfLocksBySelector]
- +[MADAutoSetLocker copyOfLocksBySelector].cold.1
- +[MADAutoSetLocker endedAllPreviousLocksByClient:forAssetSelector:forLockReason:endError:]
- +[MADAutoSetLocker endedLockByClient:forAssetSelector:forLockReason:endError:]
- +[MADAutoSetLocker endedPreviousLocksByClient:forAssetSelector:forLockReason:removingLockCount:endError:]
- +[MADAutoSetLocker forceGlobalUnlock:]
- +[MADAutoSetLocker forceGlobalUnlock:].cold.1
- +[MADAutoSetLocker lockedByClient:forAssetSetIdentifier:forAtomicInstance:forLockReason:withUsagePolicy:lockError:]
- +[MADAutoSetLocker lockedSelectorsForEliminate:]
- +[MADAutoSetLocker lockedSelectorsForEliminate:].cold.1
- +[MADAutoSetLocker migrateMismatchedPersistedStateVersion:forEntryID:withMismatchedState:]
- +[MADAutoSetLocker newCurrentLockUsageForSelector:]
- +[MADAutoSetLocker newCurrentLockUsageForSelector:].cold.1
- +[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]
- +[MADPowerLogManager _retrieveSpecificIdentifier:andCategory:].cold.1
- +[MADPowerLogManager _retrieveSpecificIdentifier:andCategory:].cold.2
- +[MANAutoAssetStatus newCurrentLockUsageSummary:].cold.1
- +[MASAutoAssetStatus newShimmedToFramework:].cold.1
- -[DownloadManager applyTransforms:toAssets:]
- -[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadConfig:forAutoAssetName:]
- -[DownloadManager taskFinishedUpdateState:with:]
- -[DownloadManager taskFinishedUpdateState:with:extraInfo:]
- -[MABAACertManager copyBase64EncodedCertificateChain:referenceKey:].cold.1
- -[MABAACertManager copyDeviceIdentityOptionsForCertAndRequestType:skipNetworkRequest:invalidateExistingCert:].cold.1
- -[MABAACertManager copyDeviceIdentityOptionsForCertAndRequestType:skipNetworkRequest:invalidateExistingCert:].cold.2
- -[MABAACertManager copyDeviceIdentityOptionsForCertAndRequestType:skipNetworkRequest:invalidateExistingCert:].cold.3
- -[MABAACertManager copyPreviouslyCreatedCertsIfPresent:].cold.1
- -[MABAACertManager copyPreviouslyCreatedCertsIfPresent:].cold.2
- -[MABAACertManager copyPreviouslyCreatedCertsIfPresent:].cold.3
- -[MABAACertManager issueAndCopyCerts:].cold.1
- -[MABAACertManager issueAndCopyCertsInternal:].cold.1
- -[MABAACertManager issueAndCopyCertsInternal:].cold.2
- -[MADAnalyticsManager recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:]
- -[MADAutoAssetConnector _addObserverForMarker:].cold.1
- -[MADAutoAssetConnector _followupInUseServerStatus:].cold.1
- -[MADAutoAssetConnector _removeObserverForMarker:].cold.1
- -[MADAutoAssetConnector init].cold.1
- -[MADAutoAssetControlManager _autoAssetJobProgressNewValidatedCurrentStatus:requiringProgress:].cold.1
- -[MADAutoAssetControlManager _clearAtomicInstanceFromLatestToVend:fromLocation:]
- -[MADAutoAssetControlManager _clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:]
- -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:]
- -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:].cold.1
- -[MADAutoAssetControlManager _doesSetDescriptorRequirePersonalization:forSetDescriptor:].cold.1
- -[MADAutoAssetControlManager _eliminateCompleteIfAllDone:].cold.1
- -[MADAutoAssetControlManager _haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager _haveReceivedLookupResponseForSetDescriptor:]
- -[MADAutoAssetControlManager _initializeAutoControl].cold.1
- -[MADAutoAssetControlManager _initializeAutoControl].cold.2
- -[MADAutoAssetControlManager _initializeConnectionServer].cold.1
- -[MADAutoAssetControlManager _initializeServerConnectionPolicy].cold.1
- -[MADAutoAssetControlManager _isSetDescriptorAvailableToClient:forSetDescriptor:].cold.1
- -[MADAutoAssetControlManager _logPersistedSetLookupResultTableOfContents:]
- -[MADAutoAssetControlManager _newAtomicEntryIDsOtherThanDescriptor:]
- -[MADAutoAssetControlManager _preInstalledAtomicInstanceDescriptors]
- -[MADAutoAssetControlManager _preInstalledMakeDescriptorAvailable:fromLocation:].cold.1
- -[MADAutoAssetControlManager _preInstalledRelocateAutoAssets].cold.1
- -[MADAutoAssetControlManager _preInstalledSetAtomicEntriesFromInstanceEntries:].cold.1
- -[MADAutoAssetControlManager _preInstalledSetAtomicEntriesFromInstanceEntries:].cold.2
- -[MADAutoAssetControlManager _promotePreviouslyStagedNowDownloaded:forHistoryOperation:].cold.1
- -[MADAutoAssetControlManager _removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:]
- -[MADAutoAssetControlManager _requestDownloadManagerSync].cold.1
- -[MADAutoAssetControlManager _shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:].cold.1
- -[MADAutoAssetControlManager _shortTermChangeAtomicInstance:forAtomicInstance:toShortTermSupported:].cold.2
- -[MADAutoAssetControlManager _vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager _vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:]
- -[MADAutoAssetControlManager action_DecideNeedGraft:error:].cold.1
- -[MADAutoAssetControlManager action_DecideNeedPersonalize:error:].cold.1
- -[MADAutoAssetControlManager action_EliminateStagerSetDone:error:].cold.1
- -[MADAutoAssetControlManager action_EliminateStagerSetDone:error:].cold.2
- -[MADAutoAssetControlManager action_IssueClientReplySetJob:error:].cold.1
- -[MADAutoAssetControlManager action_IssueClientReplySetJob:error:].cold.2
- -[MADAutoAssetControlManager action_IssueClientReplySetJob:error:].cold.3
- -[MADAutoAssetControlManager action_LogStatistics:error:]
- -[MADAutoAssetControlManager action_ObtainLookupGrant:error:].cold.1
- -[MADAutoAssetControlManager action_ObtainLookupGrant:error:].cold.2
- -[MADAutoAssetControlManager action_PersonalizeSuccessDecideMore:error:].cold.1
- -[MADAutoAssetControlManager action_ProvidePersistedForJob:error:].cold.1
- -[MADAutoAssetControlManager action_ProvidePersistedForJob:error:].cold.2
- -[MADAutoAssetControlManager action_ProvidePersistedForJob:error:].cold.3
- -[MADAutoAssetControlManager action_QueueClientRequest:error:].cold.1
- -[MADAutoAssetControlManager action_QueueClientRequest:error:].cold.2
- -[MADAutoAssetControlManager action_QueueClientRequestBefore1st:error:].cold.1
- -[MADAutoAssetControlManager action_QueueClientRequestBefore1st:error:].cold.2
- -[MADAutoAssetControlManager action_QueueDownloadManager:error:].cold.1
- -[MADAutoAssetControlManager action_ReleaseLookupGrant:error:].cold.1
- -[MADAutoAssetControlManager action_ReleaseLookupGrant:error:].cold.2
- -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.1
- -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.2
- -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.3
- -[MADAutoAssetControlManager action_RouteClientRequest:error:].cold.1
- -[MADAutoAssetControlManager action_RouteClientRequest:error:].cold.2
- -[MADAutoAssetControlManager action_SetJobLookupResponseRcvd:error:].cold.1
- -[MADAutoAssetControlManager action_StartUnlockPollingTimer:error:].cold.1
- -[MADAutoAssetControlManager addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:]
- -[MADAutoAssetControlManager alreadyHaveSetDescriptorMatching:].cold.1
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:]
- -[MADAutoAssetControlManager atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:]
- -[MADAutoAssetControlManager atomicInstanceTrimOverflowAfterPersisting:].cold.1
- -[MADAutoAssetControlManager bootedOBuildVersion]
- -[MADAutoAssetControlManager buildFoundResponseMessage:forClientRequest:withFoundDescriptor:withInstance:withDesire:fromLocation:error:].cold.1
- -[MADAutoAssetControlManager buildFoundResponseMessage:forClientRequest:withFoundDescriptor:withInstance:withDesire:fromLocation:error:].cold.2
- -[MADAutoAssetControlManager chooseNewerSetDescriptor:considering:]
- -[MADAutoAssetControlManager chooseNewerSetStatus:comparingTo:]
- -[MADAutoAssetControlManager clientRequestMessageDesire:].cold.1
- -[MADAutoAssetControlManager clientRequestMessageInstance:].cold.1
- -[MADAutoAssetControlManager clientRequestMessageInstance:].cold.2
- -[MADAutoAssetControlManager clientRequestMessageSetDesire:].cold.1
- -[MADAutoAssetControlManager clientRequestMessageSetEnd:].cold.1
- -[MADAutoAssetControlManager clientRequestMessageSetPolicy:].cold.1
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend]
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.1
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.2
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.3
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.4
- -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.5
- -[MADAutoAssetControlManager decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:]
- -[MADAutoAssetControlManager doesSetDescriptor:satisfyAllAutoAssetEntries:]
- -[MADAutoAssetControlManager downloadedSetDescriptorsByInstance]
- -[MADAutoAssetControlManager handleClientAlterLockOperation:forAutoJob:].cold.1
- -[MADAutoAssetControlManager handleClientEliminateAllForAssetTypeRequest:].cold.1
- -[MADAutoAssetControlManager handleClientEliminateAllForSelectorRequest:].cold.1
- -[MADAutoAssetControlManager handleClientEliminateAllForSelectorRequest:].cold.2
- -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.1
- -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.2
- -[MADAutoAssetControlManager handleClientEliminatePromotedNeverLockedForSelectorRequest:].cold.3
- -[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:].cold.1
- -[MADAutoAssetControlManager handleMessage:proxyObject:reply:].cold.1
- -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:]
- -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:].cold.1
- -[MADAutoAssetControlManager handleSetClientCheckAtomic:forAutoJob:instance:desire:fromLocation:].cold.1
- -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:]
- -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.1
- -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.2
- -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:].cold.3
- -[MADAutoAssetControlManager handleSetClientLockAtomic:forAutoJob:instance:desire:fromLocation:].cold.1
- -[MADAutoAssetControlManager isDescriptorManagedAsSet:]
- -[MADAutoAssetControlManager issueResponseToFailedAutoAssetLockRequest:forEventInfo:withResponseError:forAttemptedDescriptor:].cold.1
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimAtomicInstances]
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors]
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.1
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.2
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.3
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.4
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrimSetDescriptors].cold.5
- -[MADAutoAssetControlManager loadPersistedCrossCheckTrim]
- -[MADAutoAssetControlManager loadPersistedSetDownloadedDescriptors].cold.1
- -[MADAutoAssetControlManager loadPersistedSetLookupResults]
- -[MADAutoAssetControlManager locateDownloadedByFullSelector:].cold.1
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedByAtomicInstanceUUID:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedLatest:forAssetSetIdentifier:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPreviouslyStagedFound:fromLocation:]
- -[MADAutoAssetControlManager locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:]
- -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
- -[MADAutoAssetControlManager notifyLockerAsIndicatedByJob:].cold.1
- -[MADAutoAssetControlManager notifyLockerAsIndicatedBySetJob:withSetInstance:withSetDesire:forSetDescriptor:withClientReplyCompletion:].cold.1
- -[MADAutoAssetControlManager notifyLockerJustLockedDescriptor:forClientInstance:withClientDesire:respondingToClientRequest:withClientCompletion:].cold.1
- -[MADAutoAssetControlManager preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:]
- -[MADAutoAssetControlManager preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:]
- -[MADAutoAssetControlManager removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:error:]
- -[MADAutoAssetControlManager secureCheckProcessLifeLocks:]
- -[MADAutoAssetControlManager secureForceUngraft:forDescriptorBeingRemoved:].cold.1
- -[MADAutoAssetControlManager secureForceUngraftAll:forSetDescriptorBeingRemoved:]
- -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]
- -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]
- -[MADAutoAssetControlManager setBootedOBuildVersion:]
- -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:]
- -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:]
- -[MADAutoAssetControlManager setConfigurationReferencesDescriptor:].cold.1
- -[MADAutoAssetControlManager setConfigurationVendingDescriptor:managedAsSet:].cold.1
- -[MADAutoAssetControlManager setDescriptorAddedPreInstalled:].cold.1
- -[MADAutoAssetControlManager setDescriptorDownloadedLoadedFromPersisted:persistedEntryID:]
- -[MADAutoAssetControlManager setDescriptorDownloadedLoadedFromPersisted:persistedEntryID:].cold.1
- -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:].cold.1
- -[MADAutoAssetControlManager setDescriptorEliminate:triggeredByClient:forClientDomainName:forAssetSetIdentifier:awaitingUnlocked:].cold.2
- -[MADAutoAssetControlManager setDownloadedSetDescriptorsByInstance:]
- -[MADAutoAssetControlManager setJobInstanceKeyForSetInstance:].cold.1
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetDescriptor:forLatestDownloaded:].cold.1
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetDescriptor:forLatestDownloaded:].cold.2
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetDescriptor:forLatestDownloaded:].cold.3
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetStatus:forLatestDownloaded:].cold.1
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetStatus:forLatestDownloaded:].cold.2
- -[MADAutoAssetControlManager setJobInstanceKeyFromSetStatus:forLatestDownloaded:].cold.3
- -[MADAutoAssetControlManager shortTermLockSetDescriptor:forSetDescriptor:]
- -[MADAutoAssetControlManager trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:]
- -[MADAutoAssetControlManager trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:]
- -[MADAutoAssetControlManager trackShortTermLockedSetDescriptor:]
- -[MADAutoAssetControlManager updateAutoAssetStatus:forActiveJobUUID:withLatestJobStatus:matchingAssetVersion:fromLocation:].cold.1
- -[MADAutoAssetControlManager updateCurrentAssetStatus:currentStatus:forAssetSelector:forActiveJobUUID:matchingAssetVersion:downloadingDescriptor:baseForPatchDescriptor:].cold.1
- -[MADAutoAssetControlManagerParam initForConfigFinishedJobID:withError:]
- -[MADAutoAssetControlManagerParam initForSetConfiguration:withSetDescriptor:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:].cold.1
- -[MADAutoAssetControlManagerParam initWithPromoted:withSetLookupResults:]
- -[MADAutoAssetHistory _trackerForHistoryType:].cold.1
- -[MADAutoAssetHistoryTracker loadPersistedState].cold.1
- -[MADAutoAssetHistoryTracker makeSureHistoryDirectoryExists].cold.1
- -[MADAutoAssetHistoryTracker recordFormattedHistoryEntry:toBucketFilename:settingCurrentBucketBytes:].cold.1
- -[MADAutoAssetHistoryTracker recordFormattedHistoryEntry:toBucketFilename:settingCurrentBucketBytes:].cold.2
- -[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
- -[MADAutoAssetJob _autoAssetJobFinished:forJobFinishedReason:failingWithError:].cold.1
- -[MADAutoAssetJob _commitPrePersonalized:error:].cold.1
- -[MADAutoAssetJob _newSelectorForCachedAssetCatalog:].cold.1
- -[MADAutoAssetJob action_BoostToUserInitiated:error:]
- -[MADAutoAssetJob action_DecideStartupDownloading:error:].cold.1
- -[MADAutoAssetJob action_DecideStartupDownloading:error:].cold.2
- -[MADAutoAssetJob action_NowUserInitiated:error:]
- -[MADAutoAssetJob action_ReportFailBoostSetDownloadNext:error:]
- -[MADAutoAssetJob action_ReportFailBoostSetDownloadNext:error:].cold.1
- -[MADAutoAssetJob action_ReportFailureUserInitiated:error:]
- -[MADAutoAssetJob action_ReportFailureUserInitiated:error:].cold.1
- -[MADAutoAssetJob action_UserInitiatedDownloadNewestFull:error:]
- -[MADAutoAssetJob action_UserInitiatedSetDownloadNext:error:]
- -[MADAutoAssetJob autoAssetSetAssetType].cold.1
- -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.1
- -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.2
- -[MADAutoAssetJob determineWhetherNetworkConnectivityError:].cold.3
- -[MADAutoAssetJob handleDownloadConfigJobFinished:configError:]
- -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:].cold.1
- -[MADAutoAssetJob isFoundAlreadyOnFilesystem:].cold.1
- -[MADAutoAssetJob newCurrentStatusForDescriptor:].cold.1
- -[MADAutoAssetJob refreshDownloadedToManager]
- -[MADAutoAssetJob refreshDownloadedToManager].cold.1
- -[MADAutoAssetJob refreshDownloadedToManager].cold.2
- -[MADAutoAssetJob refreshDownloadedToManager].cold.3
- -[MADAutoAssetJob refreshSetFoundToManager:]
- -[MADAutoAssetJob replyToJobsWhenCatalogDownloaded:discoveredNewer:].cold.1
- -[MADAutoAssetJob reportJustDownloadedAssetOfSet:].cold.1
- -[MADAutoAssetJob reportSetCatalogDecideFound:]
- -[MADAutoAssetJob simulateEnd:].cold.1
- -[MADAutoAssetJob simulateEnd:].cold.2
- -[MADAutoAssetJob simulateEnd:].cold.3
- -[MADAutoAssetJob simulateEnd:].cold.4
- -[MADAutoAssetJob simulateSet:].cold.1
- -[MADAutoAssetJob simulateSet:].cold.2
- -[MADAutoAssetLocker _autoAssetLockPolicyFromSetPolicy:].cold.1
- -[MADAutoAssetLocker _endLocksByClient:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:]
- -[MADAutoAssetLocker _lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:]
- -[MADAutoAssetLocker _persistAssetLock:operation:forAssetLock:message:]
- -[MADAutoAssetLocker _persistAssetLock:operation:forAssetLock:message:].cold.1
- -[MADAutoAssetLocker _persistRemoveAssetLock:removedAssetLock:message:].cold.1
- -[MADAutoAssetLocker _refreshFilesystemMetadataLastInterest:].cold.1
- -[MADAutoAssetLocker _refreshFilesystemMetadataLastInterest:].cold.2
- -[MADAutoAssetLocker _refreshFilesystemMetadataLastInterest:].cold.3
- -[MADAutoAssetLocker _removeAssetLock:lastClient:forSelector:message:]
- -[MADAutoAssetLocker locateLockBySelector:].cold.1
- -[MADAutoAssetLocker locateLockBySelector:].cold.2
- -[MADAutoAssetLocker locateLocksCurrentLocksCount]
- -[MADAutoAssetLocker setAtomicInstanceForUUID:fromSetAtomicInstances:]
- -[MADAutoAssetPersisted persistedEntry:fromLocation:].cold.1
- -[MADAutoAssetPersisted removePersistedEntry:fromLocation:].cold.1
- -[MADAutoAssetScheduler _eliminateSpecificSelector:].cold.1
- -[MADAutoAssetScheduler _performPushNotificationOperations].cold.1
- -[MADAutoAssetScheduler _performTickerOperations:].cold.1
- -[MADAutoAssetScheduler _performTickerOperations:].cold.2
- -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:].cold.1
- -[MADAutoAssetScheduler _setConfigurationForAssetSelector:].cold.1
- -[MADAutoAssetScheduler _snapshotOfJobsBySelector].cold.1
- -[MADAutoAssetScheduler _trackSetConfigurations:].cold.1
- -[MADAutoAssetSecure init].cold.1
- -[MADAutoAssetStager _acceptStagingClientRequest:fromLocation:]
- -[MADAutoAssetStager _addDescriptor:withRepresentation:toSummary:withStageGroupType:withTargetOS:].cold.1
- -[MADAutoAssetStager _adjustPallasResponseBasedOnPreferences:].cold.1
- -[MADAutoAssetStager _extendLookupByAssetTypeWithDownloadedDescriptors:].cold.1
- -[MADAutoAssetStager _extendLookupByAssetTypeWithSetConfigurations:].cold.1
- -[MADAutoAssetStager _isSetTargetWithinRange:asCandidate:].cold.1
- -[MADAutoAssetStager _logPersistedConfigLoad:lastStagingFromOSVersion:lastStagingFromBuildVersion:assetTargetOSVersion:assetTargetBuildVersion:usingModeByGroups:candidateAssetCount:determinedAvailableAssetCount:activelyStagingAssetCount:awaitingStagingAssetCount:stagedAssetCount:stagedAssetTotalContentBytes:message:]
- -[MADAutoAssetStager _replyHaveStagedContent:]
- -[MADAutoAssetStager _replyWithAlreadyDetermined:forEventInfo:orFollowupDetermineStart:].cold.1
- -[MADAutoAssetStager _setupAwaitingStagingAndBeginFirstDownload].cold.1
- -[MADAutoAssetStager _updateDescriptor:withLatestJobStatus:].cold.1
- -[MADAutoAssetStager _updateLookupResultsJustStagedByGroupMode:].cold.1
- -[MADAutoAssetStager action_ClientAcceptAllDetermine:error:].cold.1
- -[MADAutoAssetStager action_ClientCheckLatchGroupsDetermine:error:].cold.1
- -[MADAutoAssetStager action_FormCandidatesDecideDetermine:error:].cold.1
- -[MADAutoAssetStager action_FormCandidatesDecideDetermine:error:].cold.2
- -[MADAutoAssetStager action_ReportStagingProgressToClient:error:].cold.1
- -[MADAutoAssetStager init].cold.1
- -[MADAutoAssetStager newAssetMetadataFromAssetCatalog:forAssetype:forAssetSpecifier:].cold.1
- -[MADAutoAssetStager splitOutAvailableForStagingByGroup:]
- -[MADAutoAssetStager startMaxTimeSpentDeterminingTimer].cold.1
- -[MADAutoSetAtomicInstance initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:]
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
- -[MADAutoSetLocker .cxx_destruct]
- -[MADAutoSetLocker _anyCurrentLocksForEliminate:]
- -[MADAutoSetLocker _assetIDOfLock:]
- -[MADAutoSetLocker _currentLockCountOfLock:]
- -[MADAutoSetLocker _endLockDecideUnlocked:]
- -[MADAutoSetLocker _endLocksByClient:forAssetSelector:forLockReason:removingLockCount:endError:]
- -[MADAutoSetLocker _logPersistedEntry:operation:persistingAssetLock:forSelector:message:]
- -[MADAutoSetLocker _logPersistedRemovedEntry:removedAssetLock:forSelector:message:]
- -[MADAutoSetLocker _logPersistedTableOfContents:]
- -[MADAutoSetLocker _mergeAddedLock:intoExistingLock:]
- -[MADAutoSetLocker _mergeContinuedLock:intoExistingLock:]
- -[MADAutoSetLocker _newAssetLockSummaryWithoutSelectorOrAttributes:]
- -[MADAutoSetLocker _persistAssetLock:operation:forAssetLock:message:]
- -[MADAutoSetLocker _persistAssetLock:operation:forAssetLock:message:].cold.1
- -[MADAutoSetLocker _persistRemoveAssetLock:removedAssetLock:message:]
- -[MADAutoSetLocker _persistRemoveAssetLock:removedAssetLock:message:].cold.1
- -[MADAutoSetLocker _refreshFilesystemMetadataLastInterest:]
- -[MADAutoSetLocker _refreshFilesystemMetadataLastInterest:].cold.1
- -[MADAutoSetLocker _refreshFilesystemMetadataLastInterest:].cold.2
- -[MADAutoSetLocker _refreshFilesystemMetadataLastInterest:].cold.3
- -[MADAutoSetLocker _removeAssetLock:lastClient:forSelector:message:]
- -[MADAutoSetLocker description]
- -[MADAutoSetLocker eliminateSelectors]
- -[MADAutoSetLocker init]
- -[MADAutoSetLocker lockerQueue]
- -[MADAutoSetLocker locksBySelector]
- -[MADAutoSetLocker logger]
- -[MADAutoSetLocker persistedState]
- -[MADAutoSetLocker setEliminateSelectors:]
- -[MADAutoSetLocker setLocksBySelector:]
- -[MADAutoSetLocker summary]
- -[MADCacheDeleteManager actionUnknownAction:error:].cold.1
- -[MANAutoAssetSummary initWithAssetSelector:withAssetRepresentation:withAssetWasPatched:withAssetIsStaged:withJobStatus:withScheduledIntervalSecs:withScheduledRemainingSecs:withPushDelaySecs:withActiveClientCount:withActiveMonitorCount:withMaximumClientCount:withTotalClientCount:].cold.1
- -[MobileAssetHealthReport _collectAndSubmitReport].cold.1
- -[MobileAssetHealthReport getHealthReport]
- -[MobileAssetHealthReport initWithInterval:leeway:].cold.1
- -[MobileAssetHealthReport logger]
- -[MobileAssetKeyManager copyDawTokenFromOverrides].cold.1
- -[MobileAssetKeyManager copyDawTokenFromOverrides].cold.2
- -[MobileAssetKeyManager copyDawTokenInternal:useAppleConnect:error:].cold.1
- -[MobileAssetKeyManager copyDawTokenInternal:useAppleConnect:error:].cold.2
- -[MobileAssetKeyManager copyPersonalizationSSOTokenInternal:error:].cold.1
- -[MobileAssetKeyManager copyPersonalizationSSOTokenInternal:error:].cold.2
- -[MobileAssetKeyManager createGetDecryptionKeyRequestForKnox:authData:keyFetchBaseURLString:apTicket:assetAttributes:error:].cold.1
- -[MobileAssetKeyManager createGetDecryptionKeyRequestForKnox:authData:keyFetchBaseURLString:apTicket:assetAttributes:error:].cold.2
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.2
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.3
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.4
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.5
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.6
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.7
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.8
- -[MobileAssetKeyManager decryptFileAtURL:iv:tag:cryptor:].cold.9
- -[MobileAssetKeyManager getDecryptionKey:downloadOptions:apTicket:skipKnoxLookup:disableUI:error:].cold.1
- -[MobileAssetKeyManager getDecryptionKeyFromAssetMetadataOrDownloadOptionsInternal:downloadOptions:error:].cold.1
- -[MobileAssetKeyManager getDecryptionKeyFromKnoxUsingAssetAttributesInternal:downloadOptions:apTicket:disableUI:error:].cold.1
- -[MobileAssetKeyManager getDecryptionKeyFromKnoxUsingAssetAttributesInternal:downloadOptions:apTicket:disableUI:error:].cold.2
- -[MobileAssetKeyManager getDecryptionKeyFromKnoxUsingAssetAttributesInternal:downloadOptions:apTicket:disableUI:error:].cold.3
- -[MobileAssetKeyManager getDecryptionKeyFromKnoxUsingAssetAttributesInternal:downloadOptions:apTicket:disableUI:error:].cold.4
- -[MobileAssetKeyManager isWellFormedTokenFileName:].cold.2
- -[MobileAssetKeyManager isWellFormedTokenFileName:].cold.3
- -[MobileAssetKeyManager isWellFormedTokenFileName:].cold.4
- -[MobileAssetKeyManager isWellFormedTokenFileName:].cold.5
- GCC_except_table107
- GCC_except_table155
- GCC_except_table166
- GCC_except_table204
- GCC_except_table22
- GCC_except_table26
- GCC_except_table403
- GCC_except_table45
- GCC_except_table570
- GCC_except_table574
- GCC_except_table577
- GCC_except_table579
- GCC_except_table59
- GCC_except_table593
- GCC_except_table72
- GCC_except_table725
- GCC_except_table73
- GCC_except_table74
- GCC_except_table86
- GCC_except_table90
- GCC_except_table93
- GCC_except_table95
- MACancelDownloadErrorDomain_block_invoke.onceToken
- OBJC_IVAR_$_MADAutoAssetControlManager._bootedOBuildVersion
- OBJC_IVAR_$_MADAutoAssetControlManager._downloadedSetDescriptorsByInstance
- OBJC_IVAR_$_MADAutoSetLocker._eliminateSelectors
- OBJC_IVAR_$_MADAutoSetLocker._lockerQueue
- OBJC_IVAR_$_MADAutoSetLocker._locksBySelector
- OBJC_IVAR_$_MADAutoSetLocker._logger
- OBJC_IVAR_$_MADAutoSetLocker._persistedState
- OBJC_IVAR_$_MobileAssetHealthReport._logger
- SoftwareUpdateSSOlogDebug.infoDebug
- SoftwareUpdateSSOlogDebug.logDebugOnce
- SoftwareUpdateSSOlogError.infoError
- SoftwareUpdateSSOlogError.logErrorOnce
- SoftwareUpdateSSOlogInfo.infoLog
- SoftwareUpdateSSOlogInfo.logInfoOnce
- _CFStringCreateWithCString
- _CacheDeleteCopyAvailableSpaceForVolume
- _MobileAssetFault.cold.1
- _MobileAssetLog.cold.1
- _MobileAssetLog.cold.2
- _NSLog
- _OBJC_CLASS_$_MADAutoSetLocker
- _OBJC_METACLASS_$_MADAutoSetLocker
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _SoftwareUpdateSSOlogDebug
- _SoftwareUpdateSSOlogError
- _SoftwareUpdateSSOlogInfo
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1114
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.1
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.2
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.3
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.4
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.5
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.cold.6
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1043
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1047
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1063
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1135
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1136
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1140
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1143
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1162
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1162.cold.1
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1172
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2818
- __22-[ControlManager init]_block_invoke.1137
- __24-[MABrainUpdater start:]_block_invoke_2.349
- __27-[MABrainUpdater schedule:]_block_invoke.364
- __27-[MABrainUpdater schedule:]_block_invoke.422
- __27-[MABrainUpdater schedule:]_block_invoke.437
- __27-[MABrainUpdater schedule:]_block_invoke_2.421
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2915
- __41+[MADAutoAssetStager resumeFromPersisted]_block_invoke.cold.1
- __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.988
- __44-[ControlManager handleClientConnection:on:]_block_invoke.2454
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1049
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1096
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.cold.1
- __45-[MobileAssetKeyManager copyDawTokenFileName]_block_invoke.cold.1
- __45-[MobileAssetKeyManager copyDawTokenFileName]_block_invoke.cold.2
- __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.360
- __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.cold.1
- __47-[MABAACertManager issueAndCopySelfSignedCert:]_block_invoke.cold.1
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1988
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke_2.1992
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.527
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.532
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke_2.536
- __51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke.cold.1
- __51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke.cold.2
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1151
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1151.cold.1
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1158
- __56-[MABAACertManager copyPreviouslyCreatedCertsIfPresent:]_block_invoke.cold.1
- __56-[MABAACertManager copyPreviouslyCreatedCertsIfPresent:]_block_invoke.cold.2
- __57+[MADAutoAssetScheduler addScheduledJobs:basedOnControl:]_block_invoke.cold.1
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2942
- __58+[MADAutoAssetLocker addClientLockReasons:basedOnControl:]_block_invoke.cold.1
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1150
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1151
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1152
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1003
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.983
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.cold.1
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.295
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.333
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.335
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1109
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1127
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.cold.1
- __66-[MADAutoAssetStager _extendSummaryWithAvailableForStagingAssets:]_block_invoke.1615
- __67-[ControlManager handleQueryRequest:clientName:connection:message:]_block_invoke.1519
- __68+[MADAutoAssetLookupCache cachedLookupResultForSelector:forStaging:]_block_invoke.cold.1
- __68+[MADAutoAssetLookupCache cachedLookupResultForSelector:forStaging:]_block_invoke.cold.2
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1091
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1100
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1101
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.cold.1
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2118
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.987
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2315
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2316
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2316.cold.1
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1076
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1077
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1078
- __76+[MADAutoAssetLookupCache cachedLookupResultForSetConfiguration:forStaging:]_block_invoke.cold.1
- __76+[MADAutoAssetLookupCache cachedLookupResultForSetConfiguration:forStaging:]_block_invoke.cold.2
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.1
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.2
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.3
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.4
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.5
- __81-[MobileAssetKeyManager decryptContentEncryptedAssetAtURL:assetAttributes:error:]_block_invoke.cold.6
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1118
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1119
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1119.cold.1
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1123
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1123.cold.1
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2894
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2895
- __98+[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]_block_invoke.cold.1
- __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.345
- __MobileAssetFault
- __MobileAssetLog
- __OBJC_$_CLASS_METHODS_MADAutoSetLocker
- __OBJC_$_INSTANCE_METHODS_MADAutoAssetControlManager
- __OBJC_$_INSTANCE_METHODS_MADAutoSetLocker
- __OBJC_$_INSTANCE_VARIABLES_MADAutoSetLocker
- __OBJC_$_PROP_LIST_MADAutoSetLocker
- __OBJC_CLASS_RO_$_MADAutoSetLocker
- __OBJC_METACLASS_RO_$_MADAutoSetLocker
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke_2
- ___109+[MADAutoAssetLocker endedAllPreviousLocksByClientProcessName:withClientProcessID:forAssetSelector:endError:]_block_invoke
- ___110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke_2
- ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]_block_invoke
- ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]_block_invoke_2
- ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]_block_invoke
- ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]_block_invoke_2
- ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke_2
- ___152-[DownloadManager sendDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:]_block_invoke
- ___184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke_2
- ___24-[MABrainUpdater start:]_block_invoke_2
- ___24-[MABrainUpdater start:]_block_invoke_3
- ___24-[MADAutoSetLocker init]_block_invoke
- ___24-[MADAutoSetLocker init]_block_invoke_2
- ___266+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
- ___276-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
- ___35+[MADAutoSetLocker autoAssetLocker]_block_invoke
- ___36-[MABrainUpdater update:completion:]_block_invoke_3
- ___36-[MABrainUpdater update:completion:]_block_invoke_4
- ___36-[MABrainUpdater update:completion:]_block_invoke_5
- ___37-[DownloadManager startDownloadTimer]_block_invoke_2
- ___38+[MADAutoSetLocker forceGlobalUnlock:]_block_invoke
- ___40+[MADAutoAssetLocker forceGlobalUnlock:]_block_invoke
- ___41+[MADAutoSetLocker copyOfLocksBySelector]_block_invoke
- ___44-[ControlManager handleClientConnection:on:]_block_invoke_2
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke_2
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke_3
- ___48+[MADAutoSetLocker lockedSelectorsForEliminate:]_block_invoke
- ___51+[MADAutoSetLocker newCurrentLockUsageForSelector:]_block_invoke
- ___51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke_3
- ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke_2
- ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke_2
- ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke
- ___54-[MADAutoAssetControlManager _getHealthReportForSets:]_block_invoke_2
- ___58-[DownloadManager taskFinishedUpdateState:with:extraInfo:]_block_invoke
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke_2
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke
- ___64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_3
- ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke_2
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke_2
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke_2
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke_3
- ___95+[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:]_block_invoke
- ___SoftwareUpdateSSOlogDebug_block_invoke
- ___SoftwareUpdateSSOlogError_block_invoke
- ___SoftwareUpdateSSOlogInfo_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16l
- ___block_descriptor_73_e8_32s40s48r56r64r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24l
- ___block_descriptor_82_e8_32s40s48s56s64bs72r_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e42_v24?0"MADAutoSetDescriptor"8"NSError"16l
- ___block_descriptor_89_e8_32s40s48s56s64bs72r_e5_v8?0l
- ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e42_v24?0"MADAutoSetDescriptor"8"NSError"16l
- ___handleCacheDeletePurgeCallbackForVolume_block_invoke_2
- ___handleCacheDeletePurgeableCallbackForVolume_block_invoke_2
- ___logDebug_block_invoke
- ___logError_block_invoke
- ___logFault_block_invoke
- ___logInfo_block_invoke
- ___unnamed_2
- __block_literal_global.1003
- __block_literal_global.1005
- __block_literal_global.1006
- __block_literal_global.1008
- __block_literal_global.1012
- __block_literal_global.1013
- __block_literal_global.1037
- __block_literal_global.1046
- __block_literal_global.1048
- __block_literal_global.1108
- __block_literal_global.1129
- __block_literal_global.1139
- __block_literal_global.1174
- __block_literal_global.1202
- __block_literal_global.1211
- __block_literal_global.1283
- __block_literal_global.1285
- __block_literal_global.1302
- __block_literal_global.1304
- __block_literal_global.1309
- __block_literal_global.1461
- __block_literal_global.1496
- __block_literal_global.1579
- __block_literal_global.1584
- __block_literal_global.1589
- __block_literal_global.1592
- __block_literal_global.1626
- __block_literal_global.1687
- __block_literal_global.2043
- __block_literal_global.2054
- __block_literal_global.2062
- __block_literal_global.2070
- __block_literal_global.2078
- __block_literal_global.2086
- __block_literal_global.2094
- __block_literal_global.2102
- __block_literal_global.2110
- __block_literal_global.2776
- __block_literal_global.278
- __block_literal_global.2794
- __block_literal_global.281
- __block_literal_global.284
- __block_literal_global.3111
- __block_literal_global.3181
- __block_literal_global.3183
- __block_literal_global.335
- __block_literal_global.3371
- __block_literal_global.3482
- __block_literal_global.351
- __block_literal_global.4
- __block_literal_global.4216
- __block_literal_global.424
- __block_literal_global.570
- __block_literal_global.595
- __block_literal_global.7
- __block_literal_global.949
- __block_literal_global.952
- __block_literal_global.962
- __block_literal_global.964
- __block_literal_global.966
- __block_literal_global.969
- __block_literal_global.972
- __block_literal_global.982
- __block_literal_global.992
- __block_literal_global.995
- __block_literal_global.998
- __hashCFArrayLegacy
- __hashCFArrayNoLegacy
- __hashCFDataOfLength
- __hashCFStringOfLength
- __hashToCFString
- __os_log_debug_impl
- __os_log_error_impl
- _associated conformance 16CryptoKit_Static4ASN1O0D3AnyVSHAASQ
- _associated conformance 16CryptoKit_Static4ASN1O26RFC5480AlgorithmIdentifierVSHAASQ
- _cczp_inv_update_ws
- _gExclusivelyNSLog
- _gForceNSLog
- _gForceStdOut
- _hashCFDataOfLength.cold.1
- _hashCFStringOfLength.cold.1
- _hashCFStringOfLength.cold.2
- _hashCFStringOfLength.cold.3
- _iPhoneCACert_crt_len
- _logDebug
- _logError
- _logFault
- _logInfo
- _objc_msgSend$_acceptStagingClientRequest:fromLocation:
- _objc_msgSend$_clearAtomicInstanceFromLatestToVend:fromLocation:
- _objc_msgSend$_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:
- _objc_msgSend$_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:
- _objc_msgSend$_endLocksByClient:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:
- _objc_msgSend$_haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:
- _objc_msgSend$_haveReceivedLookupResponseForSetDescriptor:
- _objc_msgSend$_limitSetAtomicEntries:fromSetDescriptor:requestedAutoAssetEntries:
- _objc_msgSend$_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:
- _objc_msgSend$_logPersistedConfigLoad:lastStagingFromOSVersion:lastStagingFromBuildVersion:assetTargetOSVersion:assetTargetBuildVersion:usingModeByGroups:candidateAssetCount:determinedAvailableAssetCount:activelyStagingAssetCount:awaitingStagingAssetCount:stagedAssetCount:stagedAssetTotalContentBytes:message:
- _objc_msgSend$_logPersistedSetLookupResultTableOfContents:
- _objc_msgSend$_newAtomicEntryIDsOtherThanDescriptor:
- _objc_msgSend$_persistAssetLock:operation:forAssetLock:message:
- _objc_msgSend$_removeAssetLock:lastClient:forSelector:message:
- _objc_msgSend$_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:
- _objc_msgSend$_replyHaveStagedContent:
- _objc_msgSend$_vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:
- _objc_msgSend$_vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:
- _objc_msgSend$action_BoostToUserInitiated:error:
- _objc_msgSend$action_LogStatistics:error:
- _objc_msgSend$action_NowUserInitiated:error:
- _objc_msgSend$action_ReportFailBoostSetDownloadNext:error:
- _objc_msgSend$action_ReportFailureUserInitiated:error:
- _objc_msgSend$action_UserInitiatedDownloadNewestFull:error:
- _objc_msgSend$action_UserInitiatedSetDownloadNext:error:
- _objc_msgSend$addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:
- _objc_msgSend$alreadyHaveSetDescriptorMatching:
- _objc_msgSend$applyTransforms:toAssets:
- _objc_msgSend$assetConfigJobFinished:error:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:
- _objc_msgSend$atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:
- _objc_msgSend$atomicInstanceUUIDFromCurrentStatus:
- _objc_msgSend$autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:
- _objc_msgSend$bootedOBuildVersion
- _objc_msgSend$chooseNewerSetDescriptor:considering:
- _objc_msgSend$chooseNewerSetStatus:comparingTo:
- _objc_msgSend$configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadConfig:forAutoAssetName:
- _objc_msgSend$considerSetDescriptorsForLatestToVend
- _objc_msgSend$decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:
- _objc_msgSend$doesSetDescriptor:coverAllForAtomicInstanceEntries:
- _objc_msgSend$doesSetDescriptor:coverAllForAutoAssetEntries:
- _objc_msgSend$doesSetDescriptor:satisfyAllAutoAssetEntries:
- _objc_msgSend$downloadedSetDescriptorsByInstance
- _objc_msgSend$endedAllPreviousLocksByClientProcessName:withClientProcessID:forAssetSelector:endError:
- _objc_msgSend$fileHandleWithStandardOutput
- _objc_msgSend$findAtomicEntryForAssetType:forAssetSpecifier:representedByStatus:
- _objc_msgSend$findSetEntryForAssetType:forAssetSpecifier:representedByConfiguration:
- _objc_msgSend$firstDaemonStartupSinceDeviceBoot
- _objc_msgSend$forceGlobalUnlock:
- _objc_msgSend$getHealthReport
- _objc_msgSend$handleDownloadConfigJobFinished:configError:
- _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:
- _objc_msgSend$handleSetClientEliminateAtomicRequest:forAutoJob:
- _objc_msgSend$includesEntryForAssetType:forAssetSpecifier:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
- _objc_msgSend$initForConfigFinishedJobID:withError:
- _objc_msgSend$initForSetConfiguration:withSetDescriptor:
- _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$initWithPromoted:withSetLookupResults:
- _objc_msgSend$isAnyAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:
- _objc_msgSend$isDescriptorManagedAsSet:
- _objc_msgSend$loadPersistedCrossCheckTrim
- _objc_msgSend$loadPersistedCrossCheckTrimAtomicInstances
- _objc_msgSend$loadPersistedCrossCheckTrimSetDescriptors
- _objc_msgSend$locateLocksCurrentLocksCount
- _objc_msgSend$locateSetDescriptorDownloadedByAtomicInstanceUUID:
- _objc_msgSend$locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:
- _objc_msgSend$locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:
- _objc_msgSend$locateSetDescriptorDownloadedLatest:forAssetSetIdentifier:
- _objc_msgSend$locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPreviouslyStagedFound:fromLocation:
- _objc_msgSend$locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:
- _objc_msgSend$locksBySelector
- _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
- _objc_msgSend$newSetDescriptorIfOtherSatisfying:forSetInfoInstance:
- _objc_msgSend$orphanedProcessLifeLocks:
- _objc_msgSend$persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:
- _objc_msgSend$persistedStagedCount
- _objc_msgSend$postSetNotificationName:forAssetSetIdentifier:fromModule:fromLocation:
- _objc_msgSend$preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:
- _objc_msgSend$preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:
- _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
- _objc_msgSend$recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:
- _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
- _objc_msgSend$refreshDownloadedToManager
- _objc_msgSend$refreshSetFoundToManager:
- _objc_msgSend$removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:error:
- _objc_msgSend$reportSetCatalogDecideFound:
- _objc_msgSend$secureCheckProcessLifeLocks:
- _objc_msgSend$secureForceUngraftAll:forSetDescriptorBeingRemoved:
- _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:
- _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:
- _objc_msgSend$setAtomicInstanceForUUID:fromSetAtomicInstances:
- _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:
- _objc_msgSend$setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:
- _objc_msgSend$setConfigurationPotentialLatestToVend:forSetDescriptor:forSetConfiguration:
- _objc_msgSend$setConfigurationVendingDescriptor:managedAsSet:
- _objc_msgSend$setDescriptorDownloadedLoadedFromPersisted:persistedEntryID:
- _objc_msgSend$sharedLogger
- _objc_msgSend$shortTermLockSetDescriptor:forSetDescriptor:
- _objc_msgSend$splitOutAvailableForStagingByGroup:
- _objc_msgSend$stagerResumed:withSetLookupResults:
- _objc_msgSend$taskFinishedUpdateState:with:
- _objc_msgSend$taskFinishedUpdateState:with:extraInfo:
- _objc_msgSend$trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:
- _objc_msgSend$trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:
- _objc_msgSend$trackShortTermLockedSetDescriptor:
- _objc_msgSend$tryPersonalizeSuccess
- _objc_msgSend$verifySetLookupResultPreferringDownloaded:
- _objc_msgSend$writeData:
- _swift_retain_n
- _symbolic _____ 16CryptoKit_Static4ASN1O0D3AnyV
- _symbolic _____ 16CryptoKit_Static4ASN1O26RFC5480AlgorithmIdentifierV
- _symbolic _____Sg 16CryptoKit_Static4ASN1O0D3AnyV
- _symbolic _____Sg 16CryptoKit_Static4ASN1O0D4NodeV
- _symbolic _____Sg 16CryptoKit_Static4ASN1O0D9BitStringV
- _symbolic _____Sg 16CryptoKit_Static4ASN1O26RFC5480AlgorithmIdentifierV
- cc_log_default.initp
- cc_log_default.log
- logDebug.infoDebug
- logDebug.logDebugOnce
- logError.infoError
- logError.logErrorOnce
- logFault.infoFault
- logFault.logFaultOnce
- logInfo.infoLog
- logInfo.logInfoOnce
CStrings:
+ "\n>>> [AUTO-STAGER] >>>\n    stagingFrom: [%@] OSVersion:%@ | BuildVersion:%@\n   activeTarget: %@\n  stagingClient: Determines:%ld | DownloadRequest:%@ | Name:%@\n         active: Config:%@ | Job:%@\n  nowDownloaded: %ld\n            set: Configs:%ld | Targets:%ld\n      scheduled: Jobs:%ld\ncandidateAssets: RequiredByTarget:%ld | OptionalByTarget:%ld | Available:%ld\n  candidateSets: RequiredByTarget:%ld | OptionalByTarget:%ld | Configurations:%ld\n  lookupResults: GroupNames:%@ | [GROUP]SetLookups:%@ | [ALL]SetLookups:%ld\n     baseAssets: ForStaging:%ld\n    determining: BySelector:%ld\navailableAssets: RequiredByTarget:%ld | OptionalByTarget:%ld | Available:%ld\n  stagingCounts: awaiting:%ld | staged:%ld\n        control: loadPostponed:%@ | alwaysPromote:%@\n  overallStaged: TotalExpectedBytes:%lld | DownloadedSoFarBytes:%lld\n    elimination: %@\n    stagingMode: Chosen:%@ | UsingGroups:%@ | OnceRequired:%@\n<<<]"
+ "\n[ATOMIC-INSTANCE] {%{public}@:atomicInstanceNewSetAtomicInstance} created | setAtomicInstance:%{public}@"
+ "\n[ATOMIC-INSTANCE] {%{public}@:atomicInstanceNewSetAtomicInstance} not persisting sub-atomic-instance of 0 entries | setAtomicInstance:%{public}@"
+ "\n[ATOMIC-INSTANCE] {%{public}@:atomicInstanceNewSetAtomicInstance} unable to load persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
+ "\n[ATOMIC-INSTANCE] {%{public}@} removed | nextRemoveSetInstance:%{public}@"
+ "\n[ATOMIC-INSTANCE] {%{public}@} unable to update atomic-instance usage-status - failed to load persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
+ "\n[ATOMIC-INSTANCE] {%{public}@} updated usage-status | setAtomicInstance:%{public}@"
+ "\n[AUTO-SECURE]LATEST-DOWNLOADED] {%{public}@} Failed to graft SecureMobileAssetBundle | isSecureMobileAsset:%{public}@ | isAccessible:%{public}@ | setDescriptor:%{public}@ | nextAtomicEntry:%{public}@ | error:%{public}@"
+ "\n[AUTO-SECURE][AUTO-GRAFT][STARTUP] {DecideNeedPersonalize} will graft|mount (once startup personalization completes) | downloadedDescriptor:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} candidate unavailable for attempting personalization | nextSelectorKey:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} received nil descriptor for entry requiring personalization | nextAtomicEntry:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} received nil set lookup result"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} skipping set configuration atomic entry, does not involve personalization or does not require personalization | nextAtomicEntry:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [PRE-INSTALLED] asset-versions not comparable | left(downloadedDescriptor):%{public}@ | right(preinstalledDescriptor):%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [PRE-INSTALLED] multiple for same specifier | left(downloadedDescriptor):%{public}@ | right(preinstalledDescriptor):%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [set] no startup personalization to be performed | nextSetConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [set] personalizing to provide latest-to-vend | nextSetConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [set] personalizing to provide newer set atomic-instance | nextSetConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [set] personalizing to provide pre-installed | nextSetConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [singleton] asset-versions not comparable | left(nextAssetDescriptor):%{public}@ | right(latestAssetDesctiptor):%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [singleton] better candidate for selector | nextAssetDescriptor:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} [singleton] first candidate for selector | nextAssetDescriptor:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} candidate for personalization [managed as set] | downloadedDescriptor:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} candidate for personalization [singleton] | downloadedDescriptor:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} altered set-configuration previouslyVendedLockedAtomicInstance | setConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} unable to self-heal, clearing previously vended locked | setConfiguration:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | personalization required after startup secure-healing (previously vended locked) | downloadedSelector:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | personalized-not-grafted|mounted (previously vended locked) | downloadedSelector:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | unable to load set-configuration | setConfigurationKey:%{public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | unable to re-graft during startup secure-healing (previously vended locked) | downloadedSelector:%{public}@"
+ "\n[CONSIDER-ELIMINATE] {%{public}@} unable to access asset-descriptor | entryID:%{public}@"
+ "\n[CONSIDER-REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} atomic-instance for currently active set-job (keeping) | entryID:%{public}@"
+ "\n[CONSIDER-REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} not subject to verflow trim - atomic-instance for currently active set-job (keeping) | setAtomicInstance:%{public}@"
+ "\n[CONSIDER-REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} over threshold for atomic-instances by set-identifier (unable to reduce) | setAtomicInstance:%{public}@"
+ "\n[CONSIDER-REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} unable to determine persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
+ "\n[CONSIDER-REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} unable to determine previous status | entryID:%{public}@"
+ "\n[ELIMINATE] {%{public}@} ungrafted|unmounted | downloadedDescriptor:%{public}@"
+ "\n[ELIMINATE] {%{public}@} ungraft|unmount failure | downloadedDescriptor:%{public}@ | ungraftError:%{public}@"
+ "\n[KNOWN-SET-DESCRIPTORS]{%{public}@} no entryID | atomicInstanceUUID:%{public}@"
+ "\n[KNOWN-SET-DESCRIPTORS]{%{public}@} unable to load persisted entry | atomicInstanceUUID:%{public}@"
+ "\n[REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} [WARNING] over threshold for atomic-instances by set-identifier (trimming) | setAtomicInstance:%{public}@ | setDescriptor:%{public}@"
+ "\n[REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} atomic-instance not tracked by set-configuration | entryID:%{public}@"
+ "\n[REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} atomic-instance without backing set-descriptor | entryID:%{public}@"
+ "\n[REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} atomic-instance without backing set-descriptor | removedOverflowAtomicInstance:%{public}@"
+ "\n[REMOVAL] {firstSchedulerCrosscheckTrimAtomicInstances} unable to load set-atomic-instance | entryID:%{public}@ | setAtomicInstance:%{public}@ | fullSetIdentifier:%{public}@"
+ "\n[SECURE][AUTO-PERSONALIZATION-COMMIT][STARTUP] {%{public}@} | commit pre-personalized asset-selectors ERROR | error:%{public}@ | prePersonalizedSelectors:%ld"
+ "\n[SECURE][AUTO-PERSONALIZATION-COMMIT][STARTUP] {%{public}@} | commit pre-personalized asset-selectors SUCCESS | prePersonalizedSelectors:%ld"
+ "\n[SET-CONFIGURATION]{%{public}@} unable to copy set-configuration | nextSetConfiguration:%{public}@"
+ "\n[SET-CONFIGURATION]{%{public}@} unable to load set-configuration | setConfigurationKey:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@:} eliminating | nextSetConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} [BusyPerformingOperation] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} [EliminationInProgress] set-identifier is being eliminated | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} [ResourceUnavailable] unable to allocate eliminate operation tracking entry"
+ "\n[SET-ELIMINATE]{%{public}@} [SUCCESS] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} [SecureOperationInProgress] set-identifier already performing a secure-operation | clientRequest:%{public}@"
+ "\n[SET-ELIMINATE]{%{public}@} unable to load persisted-set-configuration file | nextRemoveSetConfiguration:%{public}@"
+ "\n[SET-ELIMINATE]{handleSetClientEliminateAtomicRequest} failed client-request that had been waiting for cancel to complete when eliminated | dropEventInfo:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping atomic-instance without set-descriptor | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping locked atomic-instance (not latest-to-vend) (not previously-latest-still-locked) | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping locked atomic-instance without set-configuration | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping unlocked atomic-instance (not latest-to-vend) | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} dropping unlocked atomic-instance without set-configuration | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} preserving atomic-instance (newer-once-personalized) | setAtomicInstance:%{public}@"
+ "\n[STARTUP-CROSSCHECK] {loadPersistedCrosscheckStaleForceUnlock} preserving locked atomic-instance (previously-vended-locked) | setAtomicInstance:%{public}@"
+ "\n[STARTUP-STATE] [FILESYSTEM-CACHE] %{public}@"
+ "\n[STARTUP-STATE] [PERSISTED] %{public}@\n[STARTUP-STATE] [CURRENT] %{public}@\n[STARTUP-STATE] [KNOWN] %{public}@\n[STARTUP-STATE] [ACTIVE] %{public}@"
+ "\n{QueueClientRequestBefore1st} queueing singleton check|lock client-request (NOT involving secure content) until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequestBefore1st} queueing singleton check|lock client-request involving secure content until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequestBefore1st} responded to singleton check|lock client-request (NOT involving secure content) | clientRequest:%{public}@"
+ "\n{QueueClientRequest} queueing singleton check|lock client-request (NOT involving secure content) until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequest} queueing singleton check|lock client-request involving secure content until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequest} responded to singleton check|lock client-request (NOT involving secure content) | clientRequest:%{public}@"
+ "                      clientDomainName:        %@\n                    assetSetIdentifier:        %@\n                configuredAssetEntries:        %@\n             atomicInstancesDownloaded:        %@\n               catalogCachedAssetSetID:        %@\n             catalogDownloadedFromLive:        %@\n                catalogLastTimeChecked:        %@\n                     catalogPostedDate:        %@\n         newerAtomicInstanceDiscovered:        %@\n          newerDiscoveredAtomicEntries:        %@\n              latestDownloadedInstance:        %@\nlatestDownloadedAtomicInstanceFromPreSUStaging:%@\n        latestDowloadedInstanceEntries:        %@\n     downloadedCatalogCachedAssetSetID:        %@\n   downloadedCatalogDownloadedFromLive:        %@\n      downloadedCatalogLastTimeChecked:        %@\n           downloadedCatalogPostedDate:        %@\n                  currentNotifications:        %@\n                     currentNeedPolicy:        %@\n                currentSchedulerPolicy:        %@\n                   currentStagerPolicy:        %@\n            haveReceivedLookupResponse:        %@\n vendingAtomicInstanceForConfigEntries:        %@\n                 downloadUserInitiated:        %@\n                      downloadProgress:        \n%@\n                downloadedNetworkBytes:        %ld\n             downloadedFilesystemBytes:        %ld\n                      currentLockUsage:        \n%@\n                   selectorsForStaging:        %@\n                  availableForUseError:        %@\n                     newerVersionError:        %@\n"
+ " atomicInstanceUUID:%@ | setConfiguration:%@"
+ " clientDomainName:%@ | assetSetIdentifier:%@"
+ "%"
+ "%-27s %27s %-32lld\n"
+ "%@\n[AUTO-STAGER] {%@:_limitCachePersistResultToCount} unexpected error looking up entry by date %@"
+ "%@ (after secure operation attempt)"
+ "%@ (no secure operation required [SUCCESS])"
+ "%@ (no secure operation required [reply-on-error])"
+ "%@ (secure operation already in progress)"
+ "%@ latestToVend"
+ "%@ set-configuration - %@ | setConfiguration:%@"
+ "%@ | eventInfo:%@"
+ "%@,set everProvidedLatestToVend"
+ "%@:_acceptPersonalizationFromPSUSToBecomeLatestToVend"
+ "%@:_acceptPersonalizationToAttempt(forSetDescriptor)"
+ "%@:_acceptPersonalizationToAttempt(forSetLookupResult)"
+ "%@:_acceptPersonalizationToProvideLatestToVend"
+ "%@:_acceptPersonalizationToProvidePreinstalled"
+ "%@:_clearAtomicInstanceFromAllSetConfigurations"
+ "%@:_clearAtomicInstanceFromSetConfiguration"
+ "%@:_eliminateBegin"
+ "%@:_endAllSetLocks"
+ "%@:_endLocksByClient"
+ "%@:_forceSetUngraftAndEliminateAllSetLocks"
+ "%@:_forgetAtomicLostToVend"
+ "%@:_isDownloadedDescriptorPartOfLatestToVend"
+ "%@:_isDownloadedSetDescriptorLatestToVend"
+ "%@:_latestDownloadedDescriptor"
+ "%@:_logPersistedSetTargetTableOfContents"
+ "%@:_logPersistedTableOfContents"
+ "%@:_removeAssetLock"
+ "%@:_replyNoCandidates"
+ "%@:adoptTargetFromUpdateAttributes"
+ "%@:assetPersonalizatonAttemptCompletePostEvent"
+ "%@:atomicInstanceForceUnlock"
+ "%@:atomicInstanceNextCreationIndex"
+ "%@:cancelActiveSetJob"
+ "%@:clearDownloadedFromSetStatus"
+ "%@:clientRequestsAwaitingDispatchAll"
+ "%@:clientRequestsAwaitingSyncToAwaitingFirstUnlock"
+ "%@:decrementClientRequestCount"
+ "%@:forceGlobalUnlockFromLocation"
+ "%@:foundAndDownloaded"
+ "%@:foundAndDownloadedSet"
+ "%@:handleSetClientNeedForAtomicRequest"
+ "%@:isAnyAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:"
+ "%@:isEveryAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:"
+ "%@:isSetDescriptorCurrentlyLocked"
+ "%@:isSetIdentifierCurrentlyLocked"
+ "%@:locateSetDescriptor"
+ "%@:locateSetStatusPreferringByInstance"
+ "%@:persistSetJobDescriptor"
+ "%@:refreshDownloadedToManager"
+ "%@:refreshSetFoundToManager"
+ "%@:removeActiveJobForFullSelector"
+ "%@:removeClientRequest"
+ "%@:removeSetDescriptorDownloaded"
+ "%@:removeSetTargetsForClientDomain"
+ "%@:reportSetCatalogDecideFound"
+ "%@:setConfigurationAllPreviouslyVendedForceUnlock"
+ "%@:setConfigurationEliminate"
+ "%@:setConfigurationForgetIfTrackedAsPreviouslyVended"
+ "%@:setConfigurationIsTrackedAsPreviouslyVended"
+ "%@:setConfigurationRemovedAtomicInstance"
+ "%@:setConfigurationTrackAsPreviouslyVended"
+ "%@:setConfigurationTrackLatestToVend"
+ "%@:setDescriptorAllDiscoveredEntriesDownloaded"
+ "%@:setDescriptorAllEntriesDownloaded"
+ "%@:setDescriptorEliminate"
+ "%@:setJobIndicationOfPotentialLatestToVend"
+ "%@=%@"
+ "%@_"
+ "%@targetBuild:%@"
+ "%@|status:%ld(set:%ld)|jobs:%ld(set:%ld)(setCanceling:%ld)(UUID:%ld)|grants:%ld|configs:%ld|AI:%ld|downloaded:%ld|sched:%ld|timed:%ld|client:%ld"
+ "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)(setJobsCancelingByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
+ "%{%{public}@} (%{public}@)\n[SET-DOWNLOAD] set-download | SUCCESS | autoAssetSetDescriptor:%{public}@"
+ "%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] message:%{public}@%{public}@"
+ "%{public}@\n[%{public}@] {%{public}@} already replied to staging-client"
+ "%{public}@\n[%{public}@] {%{public}@} end determine-if-available | assetType:%{public}@ | totalDeterminedAvailableForTarget:%ld"
+ "%{public}@\n[%{public}@] {FormCandidatesDecideDetermine} [IGNORED(by-set-target)] candidateDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_limitCachePersistResultToCount} pruning outdated entry with key %{public}@ and date %{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_limitCachePersistResultToCount} removing entry missing date with key %{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_limitCachePersistResultToCount} removing entry with unexpected collision on date %{public}@ with key %{public}@, "
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_limitCachePersistResultToCount} restricting count to %llu"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_limitCachePersistResultToCount} unable to load key %{public}@, "
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_startDetermineJobForNextCandidate} !!!!! SIMULATED TIMEOUT !!!!!"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@OPTIONAL] | including OPTIONAL | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@OPTIONAL] | not including OPTIONAL | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@REQUIRED] | including REQUIRED | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@REQUIRED] | not including REQUIRED | nextAvailableDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} have previously staged content now applicable to the currently running OS (migrating) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} have previously staged content when configured to always promote (and now running target OS) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} have previously staged content when configured to always promote (not running target OS) | %{public}@ | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadDecideNewOSPromote} no persisted indication of any pre-software-update-staging status | %{public}@"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no persisted entries (purging)"
+ "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staging summary differs from per-entry totals | entryTotals:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} not extending with pre-existing base auto-asset asset-version (client-provided set-target) | autoAssetDescriptor:%{public}@"
+ "%{public}@\n[DOWNLOAD_INFO] {determineDownloadUrl} AssetCacheServices not present in this OS, download from: %{public}@"
+ "%{public}@\n[DOWNLOAD_INFO] {determineDownloadUrl} Attempting to get cache server url"
+ "%{public}@\n[DOWNLOAD_INFO] {determineDownloadUrl} not allowed to use caching server, download from: %{public}@"
+ "%{public}@\n[DOWNLOAD_INFO] {updateDownloadData} In progress and totalWritten is less than previous total (%lld < %lld), nsurl is backtracking significantly for %{public}@. task %{public}@"
+ "%{public}@\n[STARTUP-COMPLETED] Failed post-write existence check after writing STARTUP_ACTIVATED cookie file [%{public}@] | stashError:%@"
+ "%{public}@\n[STARTUP-COMPLETED] Failed to write STARTUP_ACTIVATED cookie file [%{public}@] | stashError:%@"
+ "%{public}@\n[STARTUP-COMPLETED] STARTUP_ACTIVATED cookie file exists [%{public}@]"
+ "%{public}@\n[STARTUP-COMPLETED] Successfully wrote STARTUP_ACTIVATED cookie file"
+ "%{public}@\n[STARTUP-COMPLETED] Writing STARTUP_ACTIVATED cookie file [%{public}@]"
+ "%{public}@\n{%{public}@} forming available-for-staging (to then be split into REQUIred and OPTIONAL"
+ "%{public}@\n{%{public}@} staging doesn't involve optional assets"
+ "%{public}@ %{public}@ %{public}@"
+ "%{public}@ %{public}@ %{public}@..."
+ "%{public}@ %{public}@ ...%{public}@(%{public}@)"
+ "%{public}@ %{public}@ OWNER %{public}@=>%{public}@ | %{public}@"
+ "%{public}@ %{public}@ [%{public}@] %d(%{public}@) | %{public}@"
+ "%{public}@ %{public}@ {%{public}@} %{public}@"
+ "%{public}@ ----CausedBy---> %{public}@"
+ "%{public}@ Attempting to set tokenPath, but cannot convert argument to string"
+ "%{public}@ Completed operation to update preference %{public}@ to nil (clear)"
+ "%{public}@ Completed operation to update preference %{public}@ to string '%{public}@'"
+ "%{public}@ Completed operation to update preferences with values %{public}@"
+ "%{public}@ Could not read PMV from: %{public}@ error: file does not exist"
+ "%{public}@ Could not read PMV from: %{public}@ error: no path for %{public}@"
+ "%{public}@ Setting Pallas audience to '%{public}@' for asset type '%{public}@'"
+ "%{public}@ Setting Pallas audience to (null) for asset type '%{public}@'"
+ "%{public}@ Setting Pallas enabled to %{public}@ for asset type %{public}@"
+ "%{public}@ Setting pallas V2 url to %0x for asset type '%{public}@' failed as the url cannot convert to string"
+ "%{public}@ Setting pallas V2 url to '%{public}@' for asset type '%{public}@'"
+ "%{public}@ Setting pallas V2 url to nil failed for asset type '%{public}@' as it must be cleared explicitly by the framework"
+ "%{public}@ Setting pallas audience to %0x... cannot convert to string."
+ "%{public}@ Setting pallas url to nil for asset type '%{public}@'"
+ "%{public}@ Token file name is not well formed and cannot be set"
+ "%{public}@ Update client usage failed due to nil asset type"
+ "%{public}@ asset %{public}@ %{public}@ has been used in past 24 hours '%{public}@': %f"
+ "%{public}@ asset %{public}@ %{public}@ unable to update client usage '%{public}@'"
+ "%{public}@ assets folder successfully deleted"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preference %{public}@ to nil (clear)"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preference %{public}@ to string '%{public}@'"
+ "%{public}@ attempts:%d | Unable to synchronize after setting preferences with values %{public}@"
+ "%{public}@ cancel being applied: %{public}@ for %{public}@ with purpose: %{public}@"
+ "%{public}@ cancel result for %{public}@ %{public}@ is: %ld (%{public}@ %{public}@)"
+ "%{public}@ canceling task: %{public}@ (asset)"
+ "%{public}@ canceling task: %{public}@ (catalog)"
+ "%{public}@ canceling task: %{public}@ (other)"
+ "%{public}@ canceling task: %{public}@ (pmv)"
+ "%{public}@ cannot purgeCatalogs before first unlock"
+ "%{public}@ cannot purgeCatalogs with invalid purpose"
+ "%{public}@ client Usage type: %{public}@ id:%{public}@, parent path: '%{public}@' AssetData exists"
+ "%{public}@ client Usage type: %{public}@ id:%{public}@, parent path: '%{public}@' unable to get AssetData subdirectory"
+ "%{public}@ client Usage type: %{public}@ id:%{public}@, path: '%{public}@' original: %f new: %f result: %ld"
+ "%{public}@ could not load PMV JSON: %{public}@ error: %{public}@"
+ "%{public}@ could not load PMV JSON: %{public}@ error: PMV file contents were not JSON dictionary"
+ "%{public}@ could not load PMV JSON: %{public}@ error: nil after deserialization"
+ "%{public}@ could not load PMV file: %{public}@"
+ "%{public}@ could not purge catalog of type %{public}@ from %{public}@"
+ "%{public}@ could not purge catalog of type %{public}@ from %{public}@ (doesn't exist, treating as success)"
+ "%{public}@ could not purge catalog of type %{public}@ from nil (path composition faillure)"
+ "%{public}@ finished purge catalogs for %{public}@ with purpose: %{public}@"
+ "%{public}@ found Pallas URL %{public}@ for asset type %{public}@"
+ "%{public}@ found Pallas asset audience %{public}@ for asset type %{public}@"
+ "%{public}@ found Pallas enabled %{public}@ for asset type %{public}@"
+ "%{public}@ gave invalid preserved ID %{public}@ for %{public}@"
+ "%{public}@ gave invalid preserved IDs array for %{public}@"
+ "%{public}@ gave invalid preserved IDs dict"
+ "%{public}@ gave invalid preserved IDs key"
+ "%{public}@ is attempting to cancel %{public}@ %{public}@ (%{public}@)"
+ "%{public}@ issued PMV download command %{public}@"
+ "%{public}@ issued PMV query command for %{public}@"
+ "%{public}@ issued clean v1 for %{public}@"
+ "%{public}@ issued download asset command: %{public}@, %{public}@, %{public}@, %{public}@ to local url '%{public}@'"
+ "%{public}@ issued load command for %{public}@"
+ "%{public}@ issued load of: %{public}@ ID %{public}@ allowing for differences %{public}@"
+ "%{public}@ issued load of: %{public}@ ID %{public}@ allowing for differences %{public}@ causing ID error MAQueryParamsEncodeFailure %{public}@"
+ "%{public}@ issued load of: %{public}@ ID %{public}@ allowing for differences %{public}@ causing ID error MAQueryParamsEncodeFailure because the allowed differences could not be instantiated"
+ "%{public}@ issued load of: %{public}@ ID %{public}@ allowing for differences %{public}@ causing ID error MAQueryParamsEncodeFailure due to having nil for allowedDifferences"
+ "%{public}@ issued load of: %{public}@ ID %{public}@ causing ID error MAQueryParamsEncodeFailure %{public}@"
+ "%{public}@ issued load of: %{public}@ ID '%{public}@' causing ID error MAQueryParamsEncodeFailure due to the ID not having the correct type"
+ "%{public}@ issued meta data download command"
+ "%{public}@ issued query command for %{public}@"
+ "%{public}@ issued query for installed asset ids for %{public}@"
+ "%{public}@ issued space check"
+ "%{public}@ makeDataVaultAtUrl %{public}@ status: %lld"
+ "%{public}@ nil preference key provided"
+ "%{public}@ proceeding before cancel happens. Cannot get in-flight downloads state: %ld for %{public}@ with purpose: %{public}@"
+ "%{public}@ provided asset type %{public}@ when %{public}@ was required"
+ "%{public}@ purgeCatalogs: the asset types are: %{public}@ with purpose: %{public}@"
+ "%{public}@ queried for: %{public}@ with returnType of: %lld (%{public}@) - %{public}@"
+ "%{public}@ queried for: %{public}@ with returnType of: %lld with Purpose: %{public}@"
+ "%{public}@ request asset audience for asset type %{public}@"
+ "%{public}@ requested Pallas URL for asset type %{public}@"
+ "%{public}@ requested if Pallas is enabled for asset type %{public}@"
+ "%{public}@ unable to categorize query results for: %{public}@"
+ "%{public}@ unable to completely purge all catalogs for %{public}@ with purpose: %{public}@"
+ "%{public}@ unable to load catalog for: %{public}@"
+ "%{public}@ unable to load repository for: %{public}@"
+ "%{public}@ user for AppleConnect token for key retrieval due to override on downloadOptions"
+ "%{public}@ | Daemon not ready for download"
+ "%{public}@ | FINISH | %{public}@ | %d"
+ "%{public}@ | FINISH | %{public}@ | %d(%{public}@)"
+ "%{public}@ | FINISH | %{public}@ | SUCCESS"
+ "%{public}@ | FINISH | %{public}@ | UNABLE TO REPLY"
+ "%{public}@ | START"
+ "%{public}@ | unable to decode entry (specifying encode classes) - dropped | %{public}@[key:%{public}@]"
+ "%{public}@ | unable to decode entry - dropped | %{public}@[key:%{public}@]"
+ "%{public}@ | {%{public}@} | %{public}@: | no entry ID for fullAssetSelector:%{public}@ | assetLock:%{public}@"
+ "%{public}@ | {SetDownloadNext} Attempting to download %{public}@ update for %{public}@"
+ "%{public}s: Analytics event recording is %{public}s"
+ "%{public}s: Atomic write to path failed and failed to remove temp path(%{public}@): %{public}@"
+ "%{public}s: Failed to read boot-args"
+ "%{public}s: Failed to write item to path %{public}@"
+ "%{public}s: Field is invalid"
+ "%{public}s: Unable to get event submission override(unable to get options entry from the device tree)"
+ "%{public}s: Unable to get event submission overrides(Could not get master port[%d])"
+ "(%{public}@)\n[SET-DECIDE-FOUND] potential full selector: %{public}@:potentialDescriptor:%{public}@,onFS:%{public}@"
+ "(%{public}@) unable to initialize alreadyOnFilesystemSelector"
+ "(OS:%@[%@],pid:%ld)"
+ ",cleared discovered-in-flight"
+ ",cleared newer-once-personalized"
+ ",fixed vending-configured-entries"
+ ",new previouslyVendedLocked"
+ ",refreshed most-recently-received"
+ ",set have-received-lookup-response"
+ ",set vending-configured-entries"
+ ",updated asset-set-ID (latest-to-vend)"
+ ",updated asset-set-ID (most-recenty-received)"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
+ "/System/Volumes/Update/Controller/MobileAsset/"
+ "/var/run"
+ "0x%llx"
+ "2.4.3"
+ "2.5.9"
+ ">>>\n                       interestInContent: %lld\n                           checkForNewer: %lld\n                    determineIfAvailable: %lld\n                           currentStatus: %lld\n                             lockContent: %lld\n                        mapLockedContent: %lld\n                       continueLockUsage: %lld\n                            endLockUsage: %lld\n                        endPreviousLocks: %lld\n                     endAllPreviousLocks: %lld\n                 eliminateAllForSelector: %lld\n                eliminateAllForAssetType: %lld\n eliminatePromotedNeverLockedForSelector: %lld\n              stageDetermineAllAvailable: %lld\n                        stageDownloadAll: %lld\n                           stagePurgeAll: %lld\n                           stageEraseAll: %lld\n estimateEvictableBytesForSoftwareUpdate: %lld\n                suspendForSoftwareUpdate: %lld\n                resumeFromSoftwareUpdate: %lld\n    suspendResumeStatusForSoftwareUpdate: %lld\n<<<]"
+ ">>>\nCategory                    Statistic                   Value\n=========================== =========================== ================================\n%@autoJobs                     totalAutoAssetJobsStarted: %lld\nautoJobs                         totalAutoJobsFinished: %lld\nstagerJobs             totalStagerDetermineJobsStarted: %lld\nstagerJobs            totalStagerDetermineJobsFinished: %lld\nstagerJobs              totalStagerDownloadJobsStarted: %lld\nstagerJobs             totalStagerDownloadJobsFinished: %lld\nresumedInFlightJobs           totalResumedInFlightJobs: %lld\nscheduledJobs              totalSchedulerTriggeredJobs: %lld\nfailuresToStartJobs           totalFailuresToStartJobs: %lld\n\npreviously           previouslyDownloadedPatchedAssets: %lld\npreviously            previouslyDownloadedPatchedBytes: %lld\npreviously              previouslyDownloadedFullAssets: %lld\npreviously               previouslyDownloadedFullBytes: %lld\n\ndownloaded                totalDownloadedPatchedAssets: %lld\ndownloaded                 totalDownloadedPatchedBytes: %lld\ndownloaded                   totalDownloadedFullAssets: %lld\ndownloaded                    totalDownloadedFullBytes: %lld\n\nstaged                        totalStagedPatchedAssets: %lld\nstaged                         totalStagedPatchedBytes: %lld\nstaged                           totalStagedFullAssets: %lld\nstaged                            totalStagedFullBytes: %lld\n\nunstaged                    totalUnstagedPatchedAssets: %lld\nunstaged                     totalUnstagedPatchedBytes: %lld\nunstaged                       totalUnstagedFullAssets: %lld\nunstaged                        totalUnstagedFullBytes: %lld\n\npromoted                    totalPromotedPatchedAssets: %lld\npromoted                     totalPromotedPatchedBytes: %lld\npromoted                       totalPromotedFullAssets: %lld\npromoted                        totalPromotedFullBytes: %lld\n\nremoved                      totalRemovedPatchedAssets: %lld\nremoved                       totalRemovedPatchedBytes: %lld\nremoved                         totalRemovedFullAssets: %lld\nremoved                          totalRemovedFullBytes: %lld\n\nfinishedJobs        finishedJobSchedulerNetworkFailure: %lld\nfinishedJobs     finishedJobSchedulerNotNetworkRelated: %lld\nfinishedJobs           finishedJobClientNetworkFailure: %lld\nfinishedJobs        finishedJobClientNotNetworkRelated: %lld\n\ngarbageColection                             performed: %@\ngarbageColection                          reclaimSpace: %@\ngarbageColection                   totalReclaimedSpace: %@\ngarbageColection                 reclaimedV2AssetCount: %ld\ngarbageColection                 reclaimedV2AssetSpace: %@\ngarbageColection                reclaimedUnlockedCount: %ld\ngarbageColection                reclaimedUnlockedSpace: %@\ngarbageColection       reclaimedLockedOverridableCount: %ld\ngarbageColection       reclaimedLockedOverridableSpace: %@\ngarbageColection       reclaimedLockedNeverRemoveCount: %ld\ngarbageColection       reclaimedLockedNeverRemoveSpace: %@\ngarbageColection                  reclaimedStagedCount: %ld\ngarbageColection                  reclaimedStagedSpace: %@\ngarbageColection         reclaimedMetadataBlockedCount: %ld\ngarbageColection         reclaimedMetadataBlockedSpace: %@\n<<<]"
+ "@\"NSObject<OS_nw_activity>\""
+ "@104@0:8@16@24q32@40@48@56@64q72@80@88@96"
+ "@180@0:8@16@24@32@40@48@56@64@72B80@84@92@100@108@116B124@128q136q144B152@156@164@172"
+ "@188@0:8@16@24@32@40@48@56@64B72@76q84@92@100@108@116@124@132@140@148@156@164B172B176B180B184"
+ "@248@0:8@16@24@32@40@48@56@64@72@80@88@96B104@108@116@124@132@140@148@156@164@172B180B184B188@192q200q208@216@224@232@240"
+ "@252@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188B192@196q204q212@220@228@236@244"
+ "@256@0:8@16@24@32@40@48@56@64@72@80@88@96B104@108@116@124@132@140@148@156@164@172@180B188B192B196@200q208q216@224@232@240@248"
+ "@340@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272B280B284B288@292@300@308@316@324@332"
+ "@40@0:8@16q24@32"
+ "@56@0:8@16@24@32B40B44q48"
+ "@60@0:8@16@24@32@40#48B56"
+ "@68@0:8@16@24@32@40#48@56B64"
+ "@88@0:8@16@24q32@40@48@56@64@72@80"
+ "@96@0:8@16@24@32@40@48@56@64q72@80@88"
+ "AAError"
+ "ADD_AI_FROM_SU_SUSPEND_0   "
+ "AIEligible"
+ "ANOMALY-LATEST-TO-VEND"
+ "ATOMIC_INSTANCE_FORCE_UNLOCKED"
+ "ATOMIC_INSTANCE_UNLOCK_DESIRED"
+ "AUTO-CONTROL-MANAGER [AutoAssetVersion:%{public}@] | Initialized | bootedOSVersion:%{public}@ | bootedOSBuildVersion:%{public}@"
+ "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager | ...init"
+ "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager | init..."
+ "ActiveJobs:%ld | KnownDescriptors:%ld | Locks:%ld | Scheduled:%ld | SetConfigurations:%ld | AtomicInstances:%ld | ActiveSetDescriptors:%ld | DownloadedSetDescriptors:%ld | SetTargets:%ld | SetLookupResults:%ld"
+ "Activity"
+ "Adding client: %{public}@"
+ "Adding synthetic job: %{public}@"
+ "Allow listed for Exclaves: %@:%@ fstag=%u"
+ "Already subscribed to channel %{public}@"
+ "Analytics"
+ "Analytics clearing on launch%{public}@"
+ "Analytics submitting on launch%{public}@"
+ "Asset %{public}@ %{public}@ despite appearing to be a type + assetId match for the requested asset load, did not match allowed diff %{public}@ because its diff was %{public}@"
+ "Asset at path %{public}@ does not support content encryption. Nothing to do"
+ "Asset dir: %{public}@ exists and is not directory, deleting"
+ "Asset failed receipt check with error %ld: %{public}@"
+ "Asset failed receipt sha1 check as measurements are not equal"
+ "Asset failed receipt sha256 check as measurements are not equal"
+ "Asset metadata is malformed. \"%@\" is present but is not of type NSData."
+ "Asset metadata lacks a valid measurement to perform streaming extraction"
+ "Asset requires features: %{public}@"
+ "Asset that could not determine an asset ID from Info.plist: %{public}@ in %{public}@"
+ "Asset that is being installed has different asset ID when looking at its Info.plist: %{public}@ in %{public}@ generates ID %{public}@ when looking at its Info.plist."
+ "Asset that is installed has different asset ID when looking at its Info.plist: %{public}@ in %{public}@ generates ID %{public}@ when looking at its Info.plist."
+ "Asset type+sepcifier is unsupported in Exclaves"
+ "Asset-Type: (%@) has an overridden URL (%@) that will not be honored."
+ "Asset-Type: (%@) is a 3rd party asset, but contains no server URL."
+ "Attempt to extract DAW token from response"
+ "Attempting decryption of content encrypted asset at path %{public}@"
+ "Attempting overriding GC for: %{public}@"
+ "Attempting to set tokenPath to %{public}@"
+ "Audience"
+ "Auto"
+ "AutoAssetPerformanceLoggingEnabled"
+ "AutoAssetStagerDetermineLastRequiredTimesOut"
+ "AutoAssetSuspendResumeForSUEnabled"
+ "AutoAssetSuspendResumeForSUSetsOverride"
+ "AutoControl"
+ "AutoControl-SuspendResume"
+ "AutoControlManagerActingAsClient"
+ "AutoHistory"
+ "AutoJob"
+ "AutoLocker"
+ "AutoScheduler"
+ "AutoSet"
+ "AutoStager"
+ "AvailErr"
+ "B100@0:8@16@24B32@36q44@52@60@68@76q84^@92"
+ "B24@0:8^I16"
+ "B40@0:8@16@24^B32"
+ "B40@0:8Q16@24@?32"
+ "B44@0:8@16@24B32@36"
+ "B48@0:8@16@24@32B40B44"
+ "B48@0:8@16@24B32B36^@40"
+ "B52@0:8@16@24@32q40B48"
+ "B56@0:8@16@24@32q40@48"
+ "B68@0:8@16@24@32B40B44B48@52q60"
+ "B88@0:8@16@24B32@36@44B52B56B60B64q68@76B84"
+ "Background updates %{public}s allowed"
+ "BoostConfig"
+ "Brain"
+ "CLIENT_RECIEVE_NOTIFICATION"
+ "CacheDelete"
+ "Can't extract NSError at nil key from dictionary: %{public}@"
+ "Can't grant allowlist entitlement for %lld (%{public}@)"
+ "Cancel for: %{public}@ of %{public}@ catalog failed due to purpose that is not well formed"
+ "Cancel for: %{public}@ of %{public}@ id: %{public}@ failed due to asset ID that is not well formed"
+ "Cancel for: %{public}@ of %{public}@ id: %{public}@ failed due to nil asset ID"
+ "Cancel for: %{public}@ of %{public}@ id: %{public}@ failed due to purpose that is not well formed"
+ "Cancelling stale background session: %{public}@"
+ "Cannot map an unpersonalized asset to Exclaves"
+ "Cannot persist PMV as there is no target location for copying %{public}@ to %{public}@ for %{public}@"
+ "Cannot persist xml as there is no target location for copying %{public}@ to %{public}@ for %{public}@"
+ "Cannot start download with nil DownloadInfo"
+ "Cannot write xml for %{public}@ as control manager is nil"
+ "Catalog download for: %{public}@ got: %ld assets"
+ "Catalog fileLocation: %{public}@"
+ "Certificate is not valid for 3rd party asset map signing: %d"
+ "Channel Population ID: %{public}@"
+ "Channel subscriptions failed with reasons: %{public}@"
+ "Check splunk for %{public}@ status code: %ld"
+ "Cleaning up source: %{public}@"
+ "Client didn't send'update client usage with a reply context, but requested an asset path? (%lld %{public}@: %{public}s = %{public}s)"
+ "Client process does not have '%{public}@' entitlement"
+ "Client process entitlements are not in the correct format (expected an array of strings)"
+ "Config for client: %{public}@ and descriptor: %{public}@ failed as task could not be found"
+ "Configuring download for task:%{public}@ overriding Cellular"
+ "Configuring download for task:%{public}@ overriding Constrained"
+ "Configuring download for task:%{public}@ overriding Expensive"
+ "Configuring download for task:%{public}@ overriding:%{public}@"
+ "Conflicting registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "Content encryption method %{public}@ is unsupported for asset at path %{public}@"
+ "Copied %{public}@ to %{public}@"
+ "Could not clean up malformed asset: %{public}@"
+ "Could not convert date string %{public}@"
+ "Could not create asset type from: %{public}@. task %{public}@"
+ "Could not create reply for getInstalledAssetIds: %{public}@"
+ "Could not create target directory: %{public}@"
+ "Could not create target folder: %{public}@,   %{public}@"
+ "Could not determine Exclave mapped path registration state"
+ "Could not ensure directory %{public}@ %{public}@error %d"
+ "Could not get asset list out of catalog for %{public}@"
+ "Could not load catalog for %{public}@"
+ "Could not make protected directory %{public}@: %{public}s (%d)"
+ "Could not make temporary directory %{public}@ error %d"
+ "Could not move Splunk file: %{public}@ to: %{public}@ error: %{public}@"
+ "Could not parse the taskDescriptor of: %{public}@. task %{public}@"
+ "Could not remove Splunk file: %{public}@, error: %{public}@"
+ "Could not subscribe to channel"
+ "Could not subscribe to channel %{public}@"
+ "Could not unsubscribe from channel"
+ "Could not unsubscribe from channel %{public}@"
+ "Could not verify signature using public key: %{public}@"
+ "Couldn't get registered channels: %{public}@"
+ "Couldn't purge asset: %{public}@ does not exist"
+ "Couldn't purge asset: %{public}@ when first moving to: %{public}@ due to error: %{public}@"
+ "Couldn't purge asset: %{public}@ when removing due to error: %{public}@"
+ "Couldn't remove previous purging asset: %{public}@ due to error: %{public}@"
+ "Count:%llu|"
+ "Created the following MAAutoAssetPushNotifications: %{public}@"
+ "Created the following push MAAutoAssetUpdatePolicy: %{public}@"
+ "Creating asset download task for: %{public}@, %{public}@"
+ "Creating live asset download task for: %{public}@"
+ "CryptoKit_Static/SubjectPublicKeyInfo.swift"
+ "DAEMON_RECIEVE_NOTIFICATION"
+ "DAW token was %{public}s"
+ "DEL_AI_CROSSCHECK_TRIM     "
+ "DEL_AI_DROP_CACHE_DELETE_LK"
+ "DEL_AI_DROP_CACHE_DELETE_UN"
+ "DEL_AI_DROP_CROSSCHECK_TRIM"
+ "DEL_AI_DROP_CROSSCHK_DESCRS"
+ "DEL_AI_DROP_ELIMINATE      "
+ "DEL_AI_DROP_FORCE_UNLOCKED "
+ "DEL_AI_DROP_FROM_SU_RESUME0"
+ "DEL_AI_DROP_MISSING_SETDESC"
+ "DEL_AI_DROP_MULTIPLE_STALE "
+ "DEL_AI_DROP_ONCE_PERSONALZD"
+ "DEL_AI_DROP_PSUS_ALTERED   "
+ "DEL_AI_DROP_PSUS_PALLAS_RSP"
+ "DEL_AI_DROP_UNLK_NOT_LATEST"
+ "DEL_AI_DROP_UNREFERENCED   "
+ "DEL_SD_DROP_CACHE_DELETE_LK"
+ "DEL_SD_DROP_CACHE_DELETE_UN"
+ "DEL_SD_DROP_CROSSCHK_DESCRS"
+ "DEL_SD_DROP_ELIMINATE      "
+ "DEL_SD_DROP_FORCE_UNLOCKED "
+ "DEL_SD_DROP_MULTIPLE_STALE "
+ "DEL_SD_DROP_ONCE_PERSONALZD"
+ "DEL_SD_DROP_PSUS_ALTERED   "
+ "DEL_SD_DROP_PSUS_PALLAS_RSP"
+ "DEL_SD_DROP_UNLK_NOT_LATEST"
+ "DEL_SD_DROP_UNREFERENCED   "
+ "DecrementTickDriven"
+ "Deletion of %{public}@ failed due to: %{public}@"
+ "DirectoryExists"
+ "Discovered task: %{public}@ new info: %{public}@"
+ "DoesNotExist"
+ "Download"
+ "Download already started for task:%{public}@ overriding Cellular:%{public}@ Expensive:%{public}@ Constrained:%{public}@"
+ "Download already started for: %{public}@"
+ "Download already started for: %{public}@ and %{public}@. task %{public}@ %{public}@ %{public}@"
+ "Download failed for: %{public}@, could not remove temp file before starting"
+ "Download failed however we are going to retry at original url: %{public}@"
+ "Download manager is nil aborting. Session %{public}@ task %{public}@"
+ "Download manager notified of finished task: %{public}@ from location: %{public}@"
+ "Download process complete for: %{public}@, with %ld. task %{public}@"
+ "Download resumed at offset %lld bytes out of an expected %lld bytes. Session %{public}@ task %{public}@\n"
+ "DownloadAuthorizationHeader already set in options for task (%{public}@)"
+ "DownloadFull"
+ "DownloadPatch"
+ "Downloading"
+ "Downloading in foreground: %{public}@, removing timeout. (forced inProc: %d)"
+ "DownloadingAwaitGrant"
+ "DownloadingLookup"
+ "ENTRY_DECREASED"
+ "ENTRY_INCREASED"
+ "ERROR(before first-unlock)|"
+ "ERROR(failed to schedule)|"
+ "ERROR(no downloaded atomic-instance [later])|"
+ "ERROR(no downloaded atomic-instance)|"
+ "ERROR(no set-configuration)|"
+ "ERROR(not lockable)|"
+ "ERROR(specific atomic-instance not downloaded)|"
+ "ERROR(unable to lock)|"
+ "ERROR: Invalid string passed to %{public}s"
+ "E_DEC"
+ "E_INC"
+ "Entitlement"
+ "Entitlement %{public}@ not satisfied for connection remote object interface: %{public}@, exported interface: %{public}@"
+ "Entitlement '%{public}@' is not a boolean"
+ "Entitlement '%{public}@' is not an array"
+ "Entitlement '%{public}@' is not an boolean value"
+ "Error code is: %ld descriptor:%{public}@ with %{public}@ . task %{public}@"
+ "Error in getting JSON from the headerJson of Pallas response: %{public}@"
+ "Error while attempting to config download"
+ "Event %{public}@ with uuid %{public}@ does not exist"
+ "Event payload data \"%{public}@\" is unsupported type \"%{public}@\". Supported Types: NSString, NSNumber, NSData, NSDate"
+ "ExclaveCapability"
+ "Expected query dictionary for %{public}@"
+ "FORGOTTEN"
+ "FROM_CLIENT_IN_FLIGHT"
+ "FROM_OTHER_DESCRIPTOR"
+ "FROM_PREINSTALLED"
+ "FROM_STAGED_PROMOTED_LOOKUP"
+ "FROM_SU_SUSPEND"
+ "FSIOC_EXCLAVE_FS_GET_BASE_DIRS"
+ "FSIOC_EXCLAVE_FS_UNREGISTER"
+ "Failed MAPallasFailedRetryNew and had no url on pallas for %{public}@ client: %{public}@"
+ "Failed MAPallasFailedRetryNew but asset type does not support XML fallback. Would have attempted with: %{public}@ after failing on pallas for %{public}@ client: %{public}@"
+ "Failed MAPallasFailedRetryNew but client used liveServerCatalogOnly to disable XML fallback. Would have attempted with: %{public}@ after failing on pallas for %{public}@ client: %{public}@"
+ "Failed MAPallasFailedRetrySame but asset type does not support XML fallback. Would have attempted retry with: %{public}@ after failing on pallas for %{public}@ client: %{public}@ with failure: %ld %{public}@"
+ "Failed MAPallasFailedRetrySame but client used liveServerCatalogOnly to disable XML fallback. Would have attempted retry with: %{public}@ after failing on pallas for %{public}@ client: %{public}@ with failure: %ld %{public}@"
+ "Failed to acquire required SSO token for task(%{public}@)"
+ "Failed to copy %{public}@ to %{public}@ (missing current/target path)"
+ "Failed to copy %{public}@ to %{public}@, error is: %{public}@"
+ "Failed to delete contentmanifest plist: %{public}@"
+ "Failed to expire task with error: %{public}@"
+ "Failed to find or update brain with new features: %{public}@"
+ "Failed to get key: %{public}s"
+ "Failed to get key: %{public}s due to not beinng present"
+ "Failed to move %{public}@ to %{public}@, error is: %{public}@"
+ "Failed to move asset: %{public}@ in migration"
+ "Failed to read contents of event file: %{public}@ (%{public}@)"
+ "Failed to read directory path: %{public}s"
+ "Failed to remove %{public}@, error is: %{public}@"
+ "Failed to remove event file %{public}@: %{public}@"
+ "Failed to remove event file after event submission %{public}@: %{public}@"
+ "Failed to submit task with error: %{public}@"
+ "Failed to subscribe to some channels: %{public}@"
+ "Failed with no retry on pallas for %{public}@ client: %{public}@"
+ "FailureReason"
+ "Falling back to XML. Retry with: %{public}@ after failure on pallas for %{public}@ client: %{public}@ with failure: %ld %{public}@"
+ "Falling back to XML: %{public}@ after failure before pallas response for %{public}@ client: %{public}@"
+ "FileExists"
+ "FinishResumeFromPersisted"
+ "For asset-type: %{public}@ Assets array nil in xml"
+ "For asset-type: %{public}@ Could not get assets from xml"
+ "For asset-type: %{public}@ asset(s) skipped due to nil assetId during query"
+ "For asset-type: %{public}@ query was skipped due to special __Empty keyword"
+ "ForceBatteryAllowedDownload"
+ "Forcing requiresPowerPluggedIn to false"
+ "Forcing system asset's build ID to: `%{public}@`"
+ "Forcing system asset's system image ID to: `%{public}@`"
+ "Found %{public}@ preference override. Was not well formed, will ignore '%{public}@' (%{public}@)."
+ "Found %{public}@ preference override. Will force build '%{public}@'."
+ "Found %{public}@ preference override. Will force result %ld."
+ "Found a lost task download information not in correct format with info: %{public}@ with task descriptor: %{public}@"
+ "Found download information but the NSURLSessionDownload task is nil, for task descriptor: %{public}@"
+ "Found download information from a task descriptor not in correct format with task descriptor: %{public}@"
+ "Found purpose directories to purge: %{public}@"
+ "Full URL is %{public}@"
+ "GlowE"
+ "Going pallas route for %{public}@ client: %{public}@"
+ "Got a malformed asset when reading %{public}@, cleaning up"
+ "Got a malformed asset when reading %{public}@, cleaning up. plist: %{public}@, infoPlistPath: %{public}@, assetDataPath: %{public}@"
+ "Got an error trying to determine if brain has features required by asset: %{public}@"
+ "Got nil assets for getInstalledAssetIds: %{public}@"
+ "HIT"
+ "Had no fallback XML url to retry with: (nil) after failure on pallas for %{public}@ client: %{public}@ with failure: %ld %{public}@"
+ "Hash duplicate found at index %i (%li duplicates found) with entry %@"
+ "HealthReportDontSendOut"
+ "Ignoring preference; key %{public}@ has unexpected class: %{public}@ value: '%{public}@'"
+ "In configDownload for client: %{public}@"
+ "Info plist does not exist under location %{public}@: %{public}@"
+ "Invalid data passed to %{public}s"
+ "Invalid event data for :%{public}@ (%{public}@)"
+ "Invalid file type found for even at path: %{public}@ [%{public}@] (skipping)"
+ "Invalid interactivity level was passed in: %@"
+ "Invalid options passed to %{public}s"
+ "Invalid path passed to %{public}s"
+ "Invalid range request: incomplete %{public}@ %{public}@"
+ "Invalid range request: negative start %{public}@ %{public}@"
+ "Invalid range request: zero length %{public}@ %{public}@"
+ "Invalid transform, skipping: %{public}@"
+ "Invalid url passed to %{public}s"
+ "KNOWN-ATOMIC-INSTANCES"
+ "KNOWN-SET-DESCRIPTORS"
+ "Keeping task: %{public}@ info: %{public}@"
+ "KeyManager"
+ "Knox lookup for decryption key %{public}@"
+ "LATEST_TO_VEND"
+ "LastCheckedDate"
+ "LoadDecideNewOSPromote"
+ "Lost task: %{public}@ info: %{public}@"
+ "MA"
+ "MA Notifying: %{public}@"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):EVICTABLE_BYTES"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):RESUME"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):STATUS"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):SUSPEND"
+ "MA-AUTO-SUSPEND-RESUME-SU:EVICTABLE_BYTES"
+ "MA-AUTO-SUSPEND-RESUME-SU:RESUME"
+ "MA-AUTO-SUSPEND-RESUME-SU:STATUS"
+ "MA-AUTO-SUSPEND-RESUME-SU:SUSPEND"
+ "MA-PROCESS-IDENTIFIER"
+ "MA-RESOURCE-SUMMARY"
+ "MADAutoAssetSetHealthReport"
+ "MADAutoAssetSoftwareUpdateSuspendResumeState"
+ "MADownloadFailed: Pallas result unknown! %ld on pallas for %{public}@ client: %{public}@"
+ "MAHR-%@"
+ "MAPushPopulationTypeCustomer"
+ "MAPushPopulationTypeDeveloperSeeding"
+ "MAPushPopulationTypeInternalLivability"
+ "MAPushPopulationTypeManagedSeeding"
+ "MAPushPopulationTypePublicSeeding"
+ "MAPushPopulationTypeUnknown"
+ "MISS"
+ "Making: %{public}@ into a datavault"
+ "Matching registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "MeasurementSHA256"
+ "Migrating assets for %{public}@ and %{public}@"
+ "MobileAssetSuspendSystemOptionalForSoftwareUpdate.active"
+ "MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce"
+ "Moved %{public}@ to %{public}@"
+ "Moved asset: %{public}@ in migration"
+ "Moving asset to target directory: %{public}@"
+ "Moving file in didFinishDownloadingToURL, extractor: %d. Session %{public}@ task %{public}@ type %{public}@ repository %{public}@"
+ "NIL"
+ "New subscription denied since we reached the channel limit"
+ "No \"%@\" key in asset map, falling back to legacy key \"%@\""
+ "No asset-type in asset map"
+ "No need to clean, %{public}@ does not exist"
+ "No need to convertpath: %{public}s is already a datavault"
+ "No options specified for download config, skipping configDownload for: %{public}@"
+ "No options specified for download config, wrong class, skipping configDownload for: %{public}@"
+ "Not adding %{public}@ to analytics payload due to invalid type"
+ "Not adding %{public}@ to analytics payload due to unallowed name"
+ "Not allow listed for Exclaves: %@:%@"
+ "Not recording event for : %{public}@"
+ "OPTIONAL|"
+ "OptionalAssetSizeAllowed"
+ "Over riding url with url from pallas: %{public}@, %{public}@"
+ "Override of asset audience due to build variable: %{public}@"
+ "PMV download is being forced as client asked. Downloading %{public}@ for %{public}@ client: %{public}@"
+ "PMV file contents were not JSON dictionary: %{public}@ from %{public}@"
+ "PREVIOUS_VEND_LOCKED"
+ "PROMOTED-NEEDS-PERSONALIZATION"
+ "PSUS_NEEDS_PERSONALIZATION"
+ "PUSH_NOTIF  "
+ "Pallas JWS parsing did not yield 3 elements, elements: %lu bytes: %{public}s"
+ "Pallas Server url is: %{public}@"
+ "Pallas call succeeded on pallas for %{public}@ client: %{public}@"
+ "Pallas request creation, array element dictionary entry key:%{public}@ holds value that is not an NSString or NSNumber | skipped"
+ "Pallas request creation, invalid value for key: %{public}@"
+ "Pallas request creation, nil value skipping key: %{public}@"
+ "Pallas request creation, unknown value '%{public}@' skipped for key: %{public}@"
+ "Pallas response contains nonce mismatch, original %{public}@, skipping: %{public}@"
+ "Pallas response nonce: %{public}@. Details for asset #%ld [of %ld] is: %{public}@"
+ "Pallas response nonce: %{public}@. Total asset count: %ld. The response body is: %{public}@"
+ "PallasOverrides"
+ "Params being sent to the server are: %{public}@"
+ "Patching"
+ "PatchingAwaitGrant"
+ "PatchingLookup"
+ "Path %{public}@ is not on volume %{public}@"
+ "Path %{public}@ is on volume %{public}@"
+ "Path to asset dir: %{public}@"
+ "PowerLog"
+ "Prior catalog could not be loaded (may not have been downloaded yet) for %{public}@ so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog did not have a URL string for %{public}@ (was %{public}@) so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog did not have a string for %{public}@ (was %{public}@) so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog did not have have a dictionary for %{public}@ and it did not have %{public}@ so it looks like a corrupt catalog. We will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog had %{public}@ and did not indicate %{public}@ ... yet also did not have %{public}@ which makes it unclear if it came from XML. We will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog had %{public}@ and said it was not %{public}@ ... yet also did not have %{public}@ which makes it unclear if it came from XML. We will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog had %{public}@ which matches the URL, we will attempt to use a Last-Modified when downloading %{public}@"
+ "Prior catalog had %{public}@, so we will not use Last-Modified when downloading %{public}@"
+ "Prior catalog had a base %{public}@ URL that matches: %{public}@ so we will use a Last-Modified when downloading %{public}@"
+ "Prior catalog had a different %{public}@ URL: %{public}@ so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog had a different base %{public}@ URL: %{public}@ so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog had a non-number for %{public}@/%{public}@ and it did not have %{public}@ so it looks like a corrupt Pallas catalog. We will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog has no %{public}@ or %{public}@ or %{public}@ or %{public}@, so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog has no or invalid %{public}@ (was %{public}@), so we will not use a Last-Modified when downloading %{public}@"
+ "Prior catalog was from Pallas: %{public}@/%{public}@. We will not use a Last-Modified when downloading %{public}@"
+ "PushNotification"
+ "Q24@0:8^@16"
+ "REMOVE_EVENT: Event %{public}@ does not exist. Nothing to do"
+ "REMOVE_EVENT: Successfully removed event %{public}@ from queue"
+ "REMOVE_EVENTS_WITH_NAME: Removing %{public}@"
+ "REQUIRED|"
+ "RESOURCE_USAGE_NONE"
+ "Range string is: %{public}@"
+ "Received %d and nil url returned by Pallas server using: %{public}@"
+ "Received %d from pallas but url is invalid: %{public}@ using: %{public}@"
+ "Received channel id %{public}@ with length %tu > %tu"
+ "Received notification with payload: %{public}@"
+ "Recording event for: %{public}@"
+ "Removing client: %{public}@"
+ "ResumeNewOSPromote"
+ "ResumePostponeNoPromote"
+ "ResumedPostponedLoad"
+ "SCHEDULED_IN_FLIGHT"
+ "SCHEDULED_SET_JOBS         "
+ "SCHEDULED_SINGLETON_JOBS   "
+ "SET_CLIENT_REPLY|setJobInfo:%@|domain:%@|identifier:%@|jobID[%@]|responseError[%@]|clientReply[%@]"
+ "SET_CONFIGURATION|setConfiguration:%@|autoAssetCatalog:%@"
+ "SET_CONFIGURATION|setConfiguration:%@|setDescriptor:%@|autoAssetCatalog:%@"
+ "SET_CONFIG_FIX_VEND_CONFIG "
+ "SET_CONFIG_LATEST_VEND_SAME"
+ "SET_CONFIG_MOST_RCNT_RCVD  "
+ "SET_CONFIG_MOST_RCNT_RCVD_S"
+ "SET_CONFIG_PSUS_LKUP_ASSOC "
+ "SET_CONFIG_PSUS_LKUP_CLEARD"
+ "SET_CONFIG_SAME_VEND_CONFIG"
+ "SET_EVENT: Adding CoreAnalytics event to submission queue: %{public}@"
+ "SET_SCHEDULER_DOWNLOADED|setJobInfo:%@|domain:%@|identifier:%@|jobID[%@]|responseError[%@]|autoAssetCatalog:%@"
+ "SET_SCHEDULER_FOUND_SAME|setJobInfo:%@|domain:%@|identifier:%@|jobID[%@]|responseError[%@]|autoAssetCatalog:%@"
+ "SHA-1"
+ "SHA-256"
+ "SPLUNK Failed due to writing data to file:%{public}@ isBatch: %d with: %{public}@"
+ "SSO"
+ "SSO token does not need to be collected for this task (%{public}@)"
+ "SSO token needs to be collected for this task (%{public}@)"
+ "STAGER_PROMOTED|requiringLoad:%@|stagedToDownloaded:%ld|stagedSetLookupResults:%ld"
+ "STARTUP-CROSSCHECK"
+ "STARTUP-PRE-INSTALLED"
+ "SUBMIT: Found event %{public}@. Sending"
+ "SUBMIT: No event found matching %{public}@. Skipping"
+ "SUBMIT_EVENTS_WITH_NAME: Submitting %{public}@"
+ "SUBSCRIBE_CHANNEL          "
+ "SUB_ATOMIC_0_ENTRIES"
+ "SUB_ATOMIC_WITH_ENTRIES"
+ "Saving event %{public}@:%{public}@ to %{public}@"
+ "SchedulerJobDownloaded"
+ "SchedulerJobFoundSame"
+ "SchedulerTickOccurred"
+ "SecureMA"
+ "Sending base url: %{public}@"
+ "Sending download result %ld (%{public}@) for %{public}@"
+ "Sending download result %ld (%{public}@) for assetType: %{public}@ XML download did not have a catalog URL. This could be for a type where liveServerCatalogOnly was set to disable XML fallback, or a lookup error for the build of SystemApps. Would have attempted the fallback URL after skipping on pallas for %{public}@ client: %{public}@"
+ "Sending splunk event:\n%{public}@"
+ "Sending splunk event:%{public}@"
+ "Sending splunk event; session id: %{public}@"
+ "Server connection handler received unknown type: %{public}@"
+ "Server didn't return Last-Modified header on statusCode %lld for %{public}@ download. task %{public}@ downloaded from %{public}@"
+ "Session %{public}@ Task completed but task was nil"
+ "SetDownloadFull"
+ "SetDownloadPatch"
+ "SetID"
+ "SetJobSchedulerDownloaded"
+ "SetJobSchedulerFoundSame"
+ "SetJobsByIdentifier:%ld(canceling:%ld) | SetStatusByInstance:%ld"
+ "Setting ifModified header to: %{public}@"
+ "Setting the time out on: %{public}@ to: %ld due to caching server"
+ "Setting the time out on: %{public}@ to: %ld due to nil options"
+ "Setting the time out on: %{public}@ to: %ld due to options"
+ "Setting the time out on: %{public}@ to: %ld due to options specifying to use default"
+ "Setting train name on DownloadManger to %{public}@"
+ "SignatureRSA-SHA256"
+ "Skipping asset download for %{public}@ due to preferences, giving result %ld (%{public}@)"
+ "Skipping asset: %{public}@ as it already exists"
+ "Skipping catalog download for %{public}@ due to preferences, giving result %ld (%{public}@)"
+ "Skipping due to no downloadInfo. CFNetwork error: %{public}@"
+ "Skipping file: %{public}@ as allData was nil"
+ "Skipping file: %{public}@ as events was nil"
+ "Skipping file: %{public}@ as we could not delete it"
+ "Skipping operation to update preference %{public}@ %{public}@ to nil (clear) as nil is not allowed"
+ "Skipping pallas route for %{public}@ client: %{public}@"
+ "Skipping splunk for %{public}@"
+ "Skipping the move as we do not have a task description. Session %{public}@"
+ "Skipping the move due to extractor consuming bytes. Session %{public}@ task %{public}@"
+ "Skipping transformation (key: \"%@\" value: \"%@\"): Value cannot be base64 decoded."
+ "Skipping transformation, as asset isn't a dict"
+ "Skipping: %{public}@ not making it a datavault"
+ "Skipping: %{public}@ not making it a datavault as assetType is nil in descriptor"
+ "SoftwareUpdateSuspendResume"
+ "Space check result: Not enough space to download and unarchive asset: need %llu and %llu available. error: %{public}@"
+ "Splunk report result for %{public}@: %d, code:%ld error: %{public}@"
+ "Starting built-in MobileAsset brain built Mar 15 2025 18:00:27"
+ "Starting downloaded MobileAsset brain (version: %@) built Mar 15 2025 18:00:27"
+ "Submit called for event but reportingLevel does not allow sending. Skipping event: %{public}@"
+ "Submit called for events but reportingLevel does not allow sending. Skipping event name: %{public}@"
+ "Submitted event %{public}@\n"
+ "Subscribing to channel %{public}@"
+ "Subscribing to channel: %{public}@"
+ "Subscribing to platform channel %{public}@"
+ "Succeeded with not modified on pallas for %{public}@ client: %{public}@"
+ "Successfully decrypted ContentEncrypted asset. Deleting ContentProtection plist at location %{public}@"
+ "Successfully purged asset from: %{public}@"
+ "Successfully registered Exclave mapped path [fstag=%d] %@:%@: %s"
+ "Successfully removed event file %{public}@"
+ "Successfully removed item %{public}@"
+ "Successfully retrieved response from authenticator"
+ "Supplied purpose for download config is not well formed, skipping configDownload for: %{public}@"
+ "SuspendResumeStatus - Issue encountered transitioning to running!"
+ "SuspendResumeStatus - already suspended!"
+ "SuspendResumeStatus - transition to suspended. | eventInfo=%@"
+ "T@\"MADAnalyticsManager\",&,N,V_analyticsManager"
+ "T@\"MADAnalyticsManager\",R,N,V_manager"
+ "T@\"MADAutoAssetHistoryTracker\",R,&,N,V_trackerPushNotification"
+ "T@\"MADownloadOptions\",R,&,N,V_downloadOptions"
+ "T@\"NSArray\",R,&,N,V_setConfigurationsToEvict"
+ "T@\"NSCache\",&,N,V_stagedAssetToSetDescriptorCache"
+ "T@\"NSCache\",&,N,V_stagedIsNewOSPromotedCache"
+ "T@\"NSDate\",&,N,V_latestToVendLastTimeChecked"
+ "T@\"NSDate\",&,N,V_latestToVendPostedDate"
+ "T@\"NSDate\",&,N,V_mostRecentlyReceivedLastTimeChecked"
+ "T@\"NSDate\",&,N,V_mostRecentlyReceivedPostedDate"
+ "T@\"NSDate\",&,V_LastCheckedDate"
+ "T@\"NSError\",&,V_availableForUseError"
+ "T@\"NSError\",&,V_newerVersionError"
+ "T@\"NSMutableArray\",&,N,V_previouslyVendedLockedAtomicInstances"
+ "T@\"NSMutableArray\",&,N,V_queuedRequestsForNewJobOnceCanceled"
+ "T@\"NSMutableDictionary\",&,N,V_cancelingSetJobsByIdentifier"
+ "T@\"NSMutableDictionary\",&,N,V_completionCallbacksBySetJobKey"
+ "T@\"NSMutableDictionary\",&,N,V_evictedCallbacksByAtomicInstanceUUID"
+ "T@\"NSMutableDictionary\",&,N,V_filesystemFileExistAtPathCache"
+ "T@\"NSMutableDictionary\",&,N,V_lockCountsBySelector"
+ "T@\"NSMutableDictionary\",&,N,V_preinstalledAssetDescriptorsBySelector"
+ "T@\"NSMutableSet\",&,N,V_tryPersonalizePromoted"
+ "T@\"NSNumber\",&,N,V_optionalAssetSizeAllowed"
+ "T@\"NSObject<OS_nw_activity>\",&,V_nwActivity"
+ "T@\"NSString\",&,N,V_bootedOSBuildVersion"
+ "T@\"NSString\",&,N,V_discoveredInFlightAtomicInstance"
+ "T@\"NSString\",&,N,V_latestToVendCachedAssetSetID"
+ "T@\"NSString\",&,N,V_mostRecentlyReceivedCachedAssetSetID"
+ "T@\"NSString\",&,N,V_newerAtomicInstanceOncePersonalized"
+ "T@\"NSString\",&,N,V_startupAssetTargetBuildVersion"
+ "T@\"NSString\",&,N,V_startupAssetTargetOSVersion"
+ "T@\"NSString\",&,N,V_startupLastStagingFromBuildVersion"
+ "T@\"NSString\",&,N,V_startupLastStagingFromOSVersion"
+ "T@\"NSString\",&,N,V_usageStatus"
+ "T@\"NSString\",&,V_latestDiscoveredAssetSetUUID"
+ "T@\"NSString\",&,V_latestToVendAssetSetUUID"
+ "T@\"NSString\",&,V_setIdentifier"
+ "T@\"NSString\",R,&,N,V_creationReason"
+ "T@\"NSString\",R,&,N,V_previouslyVendedLockedAtomicInstance"
+ "T@\"NSURL\",&,N,V_latestToVendDownloadedFromLive"
+ "T@\"NSURL\",&,N,V_mostRecentlyReceivedDownloadedFromLive"
+ "T@\"NSUUID\",R,&,N,V_nonce"
+ "TB,N,V_boostedToCellular"
+ "TB,N,V_boostedToExpensive"
+ "TB,N,V_configuredToCellular"
+ "TB,N,V_configuredToExpensive"
+ "TB,N,V_configuredToUserInitiated"
+ "TB,N,V_downloadingCellular"
+ "TB,N,V_downloadingExpensive"
+ "TB,N,V_everProvidedLatestToVend"
+ "TB,N,V_latestAtomicInstanceToVendFromPreSUStaging"
+ "TB,N,V_latestDownloadedAtomicInstanceFromPreSUStaging"
+ "TB,N,V_loadPersistedPostponed"
+ "TB,N,V_preferencePerformanceLoggingEnabled"
+ "TB,N,V_preferenceStagerDetermineLastRequiredTimesOut"
+ "TB,N,V_schedulerTickPerformedCrossCheck"
+ "TB,N,V_stagerResumePostponed"
+ "TB,N,V_startupModeByGroups"
+ "TB,R,N,V_requiringLoadPriorToUse"
+ "TB,V_lastestToVendIsLocked"
+ "TB,V_lastestToVendMatchesSetConfig"
+ "TQ,N,V_startupActivelyStagingAssetCount"
+ "TQ,N,V_startupAwaitingStagingAssetCount"
+ "TQ,N,V_startupCandidateAssetCount"
+ "TQ,N,V_startupDeterminedAvailableAssetCount"
+ "TQ,N,V_startupStagedAssetCount"
+ "TQ,N,V_startupStagedAssetTotalContentBytes"
+ "Task descriptor is nil, skipping. task %{public}@"
+ "Task info is nil, skipping. task %{public}@"
+ "Task was updated but was nil, should never happen! Session %{public}@"
+ "Td,N,V_startupTimeBeginSeconds"
+ "Td,N,V_startupTimeDurationSeconds"
+ "The PMV posting date is: %{public}@ from %{public}@"
+ "The PMV staging path is: %{public}@ from %{public}@"
+ "The asset download options for %{public}@ PMV were not a valid class, failing"
+ "The asset download options for %{public}@ and %{public}@ were not a valid class, failing"
+ "The asset download options for %{public}@ catalog were not a valid class, failing: %{public}@"
+ "The attempt to create data vault failed, path: %{public}s , mode: %o, errno: %lli"
+ "The attempt to create data vault succeeded, path: %{public}s"
+ "The attempt to make data vault failed, path: %{public}s, errno: %lli"
+ "The attempt to make data vault succeeded, path: %{public}s"
+ "The background download url is: %{public}@ and %{public}@. task %{public}@ options %{public}@"
+ "The base url is empty in the request, using default: %{public}@"
+ "The downloads in flight are: %{public}@"
+ "The event with uuid of: %{public}@ exists already, keeping one with higher error count"
+ "The in process download url is: %{public}@ and %{public}@. task %{public}@ options %{public}@"
+ "The live asset server posting date is: %{public}@"
+ "The pallas URL doesn't contain /assets, so we cannot substitute /pmv. Falling back to static PMV: %{public}@"
+ "The pallas response %{public}@ header is: %{public}@"
+ "The pallas response was { RequestNonce: %{public}@ ResponseNonce: %{public}@ code: %ld"
+ "The purpose for PMV is: '%{public}@' which is not well formed, and type is: %{public}@"
+ "The purpose for XML is: '%{public}@' which is not well formed, and type is: %{public}@, bailing"
+ "The purpose for pallas v2 is: '%{public}@' which is not well formed, and type is: %{public}@"
+ "The staging path is: %{public}@ from %{public}@ target %{public}@"
+ "The task descriptor for pallas v2 is: %{public}@ and type is: %{public}@"
+ "The task descriptor is: %{public}@, %ld"
+ "The xml posting date is: %{public}@ for %{public}@ from %{public}@"
+ "There was a Pallas networking failure: %{public}@ error: %{public}@"
+ "There was a Pallas networking failure: %{public}@ error: %{public}@ for the request with nonce: %{public}@"
+ "There was a Pallas networking failure: %{public}@ statusCode: %ld"
+ "Third Party: Could not create MobileAsset 3P certificate policy"
+ "Third Party: Could not create secure trust object: %ld"
+ "Third Party: Could not evaluate trust: %@"
+ "Third Party: Could not extract public key from trust object"
+ "Third Party: Failed to allocate array"
+ "Third Party: Not organizations were provided for 3P signing verification"
+ "Third Party: Obtaining public key from certificate"
+ "Third Party: Successfully extracted public key from trust object"
+ "Third Party: Trust evaluation was performed on an OS that does not support SecPolicyCreate3PMobileAsset()."
+ "Third Party: Trust evaluation was performed on an OS that is not supported."
+ "Time Travel Date has invalid format where it should be of format YYYY-MM-DD"
+ "Tq,N,V_estimateEvictableBytesForSoftwareUpdate"
+ "Tq,N,V_filesystemStartupLookupCount"
+ "Tq,N,V_lockCountsTotal"
+ "Tq,N,V_resumeFromSoftwareUpdate"
+ "Tq,N,V_status"
+ "Tq,N,V_suspendForSoftwareUpdate"
+ "Tq,N,V_suspendResumeStatusForSoftwareUpdate"
+ "Tq,N,V_ticksUntilPreviousForceUnlocked"
+ "Triggering push notification with payload: %{public}@"
+ "Trust result is failure. Unable to verify certificates are trusted. Error: %{public}@"
+ "TryFullAwaitGrant"
+ "TryFullLookup"
+ "TryPatchAwaitGrant"
+ "Trying to create a PMV download job while background sync is ongoing, bailing, %{public}@"
+ "Trying to create a catalog download job while background sync is ongoing, bailing, %{public}@"
+ "Trying to create a download job with nil task descriptor, bailing, %{public}@"
+ "Trying to create a download job without a well formed purpose, bailing, %{public}@"
+ "Trying to create an asset download job while background sync is ongoing, bailing, %{public}@"
+ "UNSUBSCRIBE_CHANNEL        "
+ "UNTRACKED"
+ "URL %{public}@ requires SSO"
+ "UTC"
+ "Unable to create auto asset descriptor from asset with reason: %{public}@ | Assuming V2 Asset."
+ "Unable to create directory '%{public}@': %{public}@"
+ "Unable to create folder for graft list"
+ "Unable to find/reconstruct stashed event for event %{public}@ with uuid %{public}@"
+ "Unable to initialize keyed unarchiver, error: %{public}@"
+ "Unable to load grafted asset list"
+ "Unable to locate directory: %{public}@"
+ "Unable to look up client's entitlement: %{public}@"
+ "Unable to move directory from %{public}@ to %{public}@ with error: %{public}@ | Errno: %{public}s"
+ "Unable to obtain decryption key: error: %{public}@"
+ "Unable to read event at %{public}@ for submission..Removing and moving on"
+ "Unable to read number of events written for assetType: %{public}@"
+ "Unable to register asset path with fstag"
+ "Unable to remove event %{public}@ : %{public}@ : %{public}@"
+ "Unable to remove event file %{public}@: %{public}@"
+ "Unable to remove item %{public}@: %{public}@"
+ "Unable to save MAD analytics event(%{public}@)"
+ "Unable to set attributes for directory '%{public}@': %{public}@"
+ "Unable to unregister existing asset path for fstag"
+ "Unexpected xpc object %{public}@"
+ "Unknown Command: %lld (%{public}@) from client: %{public}@"
+ "Unknown Command: %lld (%{public}@), using default command behavior of not allowing allowlist without asset type"
+ "Unknown asset format:%{public}@"
+ "Unsubscribing from all channels: %{public}@"
+ "Unsubscribing from channel %{public}@"
+ "Usage is: %{public}@, Override is: %f"
+ "Using Knox url from asset: %{public}@"
+ "Using asset audience '%{public}@' via selection '%{public}@' for asset type '%{public}@'"
+ "Using auth pallas session for %{public}@"
+ "Using base url from default: %{public}@"
+ "Using base url from request: %{public}@"
+ "Using default interactivity level(0)"
+ "Using internal server trust for %{public}@"
+ "Using legacy pallas session for %{public}@"
+ "Using train name(%{public}s) from download manager"
+ "Using train name(%{public}s) from legacy method"
+ "V2"
+ "V2Control"
+ "Value for entitlement %{public}@ is false"
+ "VendingConfig"
+ "VendingLatest"
+ "We have already retried this task, skipping: %{public}@"
+ "We have no info about this task, cannot reply: %{public}@  The downloads in flight are: %{public}@"
+ "We have no info about this task, cannot retry: %{public}@"
+ "XML catalog failed as client asked for liveServerCatalogOnly to disable fallback. Would have attempted %{public}@ after skipping on pallas for %{public}@ client: %{public}@"
+ "XPC data error: %{public}@ is %zu bytes, but we failed to decode"
+ "XPC error connecting for didReceivePushNotificationWithInfo: %{public}@"
+ "Y(%ld)[%@"
+ "[%{public}@]\n[CONSIDER-OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} atomic-instance for currently active set-job (keeping) | setAtomicInstance:%{public}@"
+ "[%{public}@]\n[CONSIDER-OVERFLOW-TRIM] {atomicInstanceTrimOverflowAfterPersisting} atomic-instance is latest-to-vend to set (keeping) | setAtomicInstance:%{public}@"
+ "[%{public}@]\n[CONSIDER-REMOVAL] {%{public}@} no persisted set-descriptors when removing other than setJobDescriptor:%{public}@"
+ "[%{public}@] Connection interrupted"
+ "[%{public}@] Connection invalid"
+ "[%{public}@] Received unknown event:%lld"
+ "[%{public}@] Termination imminent"
+ "[%{public}@] {%{public}@:removeSetDescriptorDownloaded} unable to load persisted-set-descriptor file | toBeRemovedSeteDescriptor:%{public}@"
+ "[%{public}@] {%{public}@}\n[CLEARER-LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "[%{public}@] {%{public}@}\n[SET_CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
+ "[%{public}@] {%{public}@} [CLIENT_REQUESTS_AWAITING_SYNC] | moved client-request to awaiting first-unlock | jobParam:%{public}@"
+ "[%{public}@] {%{public}@} [CLIENT_REQUESTS_AWAITING_SYNC] | scheduling all queued client requests"
+ "[%{public}@] {%{public}@} [PREVIOUSLY_QUEUED] | [schedule and] route client-request that had been awaiting first-unlock | jobParam:%{public}@"
+ "[%{public}@] {%{public}@} [PREVIOUSLY_QUEUED] | [schedule and] route client-request | jobParam:%{public}@"
+ "[%{public}@] {%{public}@} ignoring (invalid restore version) | descriptor:%{public}@"
+ "[%{public}@] {%{public}@} matched on downloaded | descriptor:%{public}@"
+ "[%{public}@] {%{public}@} no match on downloaded descriptor | assetType:%{public}@, assetSpecifier:%{public}@"
+ "[%{public}@] {%{public}@} unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
+ "[%{public}@] {ScheduleSetJobs} suspended for software update (so not scheduling set-job) | schedulerTriggered:%{public}@"
+ "[%{public}@] {addToCurrentJobs} Invariant violation, suspended sets should be handled before this point | selector:%{public}@ | autoJob:%{public}@ | JobUUID:%{public}@ | message:%{public}@ | downloadingDescriptor:%{public}@ | baseForPatchDescriptor:%{public}@"
+ "[%{public}@] {firstSchedulerCrosscheckTrim} just unlocked selectors:%ld"
+ "[%{public}@] {firstSchedulerCrosscheckTrim} no selectors just unlocked"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest}\n[ALTER] altered when canceling set-job | setInfoInstance:%{public}@"
+ "[%{public}@] {jobDescriptorOnFilesystemValidated} asset file does not exist | jobDescriptor:%{public}@ | localURLForDescriptor:%{public}@"
+ "[%{public}@] {loadPersistedTargetLookupResults} entry too old | dateOfEntry:%{public}@"
+ "[%{public}@] {loadPersistedTargetLookupResults} unable to determine recency | dateOfEntry:%{public}@"
+ "[%{public}@] {setLockUsageMapEndedLockForSetDescriptor} set-descriptor not in lock-usage-map | setDescriptor:%{public}@"
+ "[%{public}@][%{public}@][%{public}@]\n#_%{public}@:%{public}@ {%{public}@} %{public}@ [totalLocks:%ld]\n#_%{public}@:(%{public}@) [%{public}@] | %{public}@\n#_%{public}@:%{public}@"
+ "[%{public}s:%d] [%{public}s] Failed to allocate AEAExtractor/STRemoteExtractor"
+ "[%{public}s:%d] [%{public}s] invalid decryption key length: %lu (should be 32 or 97 bytes)"
+ "[%{public}s] Attempting to fetch current inflight downloads"
+ "[%{public}s] Downloading: %{public}@"
+ "[%{public}s] No background session present for fetching inflight downloads"
+ "[%{public}s] Size of _downloadTasksInFlight: %ld"
+ "[%{public}s] Sync with NSURLSession is complete and found %lu tasks"
+ "[%{public}s] Sync with NSURLSession is not possible; in-process downloads found %lu tasks"
+ "[%{public}s] We should not have nil DownloadInfo for a task descriptor for taskDescriptor:%{public}@, skipping."
+ "[%{public}s] We should not have nil NSUrlSessionTask for a valid DownloadInfo for taskDescriptor:%{public}@, skipping."
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)(fromPSUS:%@)|previousAI:%@(ticks:%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[ANALYTICS] {recordEventWithName} Automatically submitting event due to reportingLevel being immediate. eventName: %{public}@"
+ "[ANALYTICS] {recordEventWithName} Could not extract Event from payload:%{public}@ and eventName:%{public}@"
+ "[AUTO-ASSET] [LOCAL-CONTENT-URL] {_handleClientAlterLockOperation} failure to perform alter lock operation - %{public}@"
+ "[AUTO-PERFORMANCE] {AUTO-LOCKER:%{public}@:trackPerformanceIteration} | containerName:%{public}@"
+ "[AUTO-PERFORMANCE] {AUTO-LOCKER:%{public}@:trackPerformanceIteration} | containerName:%{public}@ | assetSelector:%{public}@"
+ "[AUTO-PERFORMANCE] {AUTO-SET-CONTROL:trackPerformanceStartupBegin} | STARTUP_BEGIN"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] [FILESYSTEM-CACHE] {%{public}@:trackPerformanceFilesystemExistCheck} [%{public}@] | cachedInfo:%{public}@ | filePath:%{public}@"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] {AUTO-SET-CONTROL:%{public}@:trackPerformanceIteration} | containerName:%{public}@"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] {AUTO-SET-CONTROL:%{public}@:trackPerformancePhaseBegin} | PHASE_BEGIN"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] {AUTO-SET-CONTROL:%{public}@:trackPerformancePhaseEnd} | PHASE_END"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] {AUTO-SET-CONTROL:%{public}@:trackPerformanceStartupEnd} | STARTUP_END"
+ "[AUTO-PERFORMANCE][ELAPSED:%ldsecs] {AUTO-SET-CONTROL:%{public}@:trackPerformanceStartupStep} | startupStepName:%{public}@"
+ "[AUTO-PRE-INSTALLED] {_preInstalledMigrateAssets} no descriptors failed migration"
+ "[AUTO-PRE-INSTALLED] {_preInstalledSetAtomicEntriesFromInstanceEntries} found some of desired instance-entries (valid when providing pre-installed)\ninstanceEntries:\n%{public}@\npreInstalledAtomicEntries:\n%{public}@"
+ "[AUTO-SHORT-TERM][FILE]{%{public}@} attempted to persist SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@ | setStatus:%{public}@ "
+ "[AUTO-SHORT-TERM]{%{public}@} no atomic-instance tracked | atomicInstance:%{public}@"
+ "[AUTO-STAGER] {%{public}@} [%{public}@OPTIONAL] | dropping descriptor due to space constraint:%llu descriptorBytes:%llu nextAvailableDescriptor:%{public}@"
+ "[AuthenticatedPallas]: Invalid url passed to %{public}s"
+ "[AuthenticatedPallas]: Pallas server(%{public}@) does *NOT* require authentication"
+ "[AuthenticatedPallas]: Pallas server(%{public}@) requires authentication"
+ "[AuthenticatedPallas]: URL %{public}@ supports authenticated pallas"
+ "[AuthenticatedPallas]: {urlSupportsAuthenticatedPallas} Adding %{public}@ to set of domains supporting authenticated pallas"
+ "[CoreAnalytics] SUBMIT: Calling SendEventLazy for %{public}@"
+ "[CoreAnalytics] SUBMIT: NO -- Unable to invoke CoreAnalytics on this OS for event %{public}@"
+ "[CoreAnalytics] SUBMIT: YES -- Submitting CoreAnalytics event: %{public}@"
+ "[CoreAnalytics]: SUBMIT_ALL_EVENT: Sending event %{public}@"
+ "[DeepMergeDictionaries]: Invalid source/target dictionaries passed"
+ "[DeepMergeDictionaries]: No object exists in source dict for key %{public}@"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate OPTIONAL descriptor (filtered) | nextOptionalDescriptor:%{public}@"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate REQUIRED descriptor (filtered) | nextRequiredDescriptor:%{public}@"
+ "[GARBAGE_COLLECTION] {finishAllPartiallyPurgedAssets} %{public}@ | checking for purged assets at path:%{public}@"
+ "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | ...respondToCacheDelete | reclaimed:%{public}@"
+ "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%{public}@), volume:%{public}@, targeting:%{public}@ | respondToCacheDelete..."
+ "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | ...respondToCacheDelete | reclaimable:%{public}@"
+ "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%{public}@), volume:%{public}@ | respondToCacheDelete..."
+ "[GARBAGE_COLLECTION] {performCacheDeleteCollection} %{public}@ | number of assets and GC types for those corresponding assets don't match | assetCount: %ld | assetGCTypesCount: %ld"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | failed to remove old asset content | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@ | result:%lld(%{public}@)"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | old asset content did not exist | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | removed old asset content | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | setting client usage as it was not set | asset:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | skipping due to policy of never collect | asset:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (%{public}@) | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (never remove) | asset:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %{public}@ | will not delete (recent client interest) | asset:%{public}@ | gapDuration:%{public}@, removalThreshold:%{public}@"
+ "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} Could not read asset attributes from assetDirectory(asset could be non-existent): %{public}@, skipping asset."
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine content modification date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine creation date, continuing anyway | URL:%{public}@ | error:%{public}@\n%{public}@"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not remove old in-flight download tracking file (not in-flight) | URL:%{public}@ | result:%{public}@"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} dir:%{public}@ | referenceDateForRecent:%{public}@ | tasksInFlight:%ld"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} error determining contents of directory:%{public}@ | error:%{public}@\n%{public}@"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} failed to determine contents of directory:%{public}@ | error:%{public}@\n%{public}@"
+ "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} removed old in-flight download tracking file (not in-flight) | URL:%{public}@"
+ "[GARBAGE_COLLECTION] {respondToCacheDelete} Using Cache Delete Results: %{public}@"
+ "[GARBAGE_COLLECTION] {respondToCacheDelete} Volume: %{public}@ | Urgency: %d | Operation: %hhu | | reportingLevel %{public}@"
+ "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection (no asset-type directories, volume reported by cache delete might be invalid) | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@"
+ "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection | targetingPurgeAmount:%{public}@ | urgency:%d(%{public}@) | volume:%{public}@ | current time is not valid | currentTimeInSeconds:%f, numberOfSecondsInAYear:%llu"
+ "[GROUP][fromOS:%@,fromBuild:%@,targetOS:%@,targetBuild:%@|targetTrain:%@|targetRestoreVersion:%@|determineRequests:%ld|downloadRequest:%@(chosen:%@,usingGroups:%@,OnceRequired:%@)|activeDescriptor:%@|candidates:(R:%ld,O:%ld,a:%ld),determining:%ld,optionalSizeAllowed:%lld,available:(R:%ld,O:%ld,a:%ld)|awaitingStaging:%ld|staged:%ld|elimination:%ld,eliminationAck:%ld]"
+ "[MA_PREFS] Read preference from: %{public}@ for: %{public}@ value: `%{public}@` (%{public}@)"
+ "[MA_PREFS] {%{public}@} [%{public}@] Could not synchronize preferences for %{public}@ - this may be a permissions error"
+ "[MA_PREFS] {%{public}@} [%{public}@] Synchronized preferences for %{public}@"
+ "[MA_PREFS] {%{public}@} [%{public}@] nil preference key provided"
+ "[MA_PREFS] {%{public}@} [%{public}@] | Completed operation to update preference %{public}@ %{public}@ to data"
+ "[MA_PREFS] {%{public}@} [%{public}@] | Completed operation to update preference %{public}@ %{public}@ to nil (clear)"
+ "[MA_PREFS] {%{public}@} [%{public}@] | attemptsMade:%d | Unable to synchronize after setting preference %{public}@ %{public}@ to data"
+ "[MA_PREFS] {%{public}@} [%{public}@] | attemptsMade:%d | Unable to synchronize after setting preference %{public}@ %{public}@ to nil (clear)"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a number"
+ "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%{public}@ | value:%{public}@ | index:%d | not a number (from string)"
+ "[MA_PREFS] {_MAPreferencesCopyNSArrayOfNumbersValue} invalid type for key:%{public}@ | expecting array of numbers"
+ "[MA_PREFS] {_MAPreferencesCopyNSDataValue} invalid type for key:%{public}@ | expecting data"
+ "[MA_PREFS] {_MAPreferencesCopyNSDictionaryValue} invalid type for key:%{public}@ | expecting dictionary"
+ "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%{public}@ | expecting string or number or boolean"
+ "[MORE_CLIENT_REQUESTS] {%{public}@:removeCurrentSetJob} set-job indicated removal but has more to do | clientRequestCount(autoJobByUUID:%ld,autoJobByIdentifier:%ld) | eventInfo:%{public}@"
+ "[MobileAssetHealthReport] Submitting to CoreAnalytics:\nID: %{public}@\nReports: %{public}@\n"
+ "[MobileAssetHealthReport] Submitting to Splunk:\nID: %{public}@\nReports: %{public}@\nCommonFields: %{public}@"
+ "[MobileAssetHealthReport]: %@ is set, not sending out the event"
+ "[MobileAssetHealthReport]: CoreAnalytics is not available"
+ "[MobileAssetHealthReport]: Failed to query greymatter eligibility; error: %s"
+ "[MobileAssetHealthReport]: Submitting CoreAnalytics MAHR: %{public}@"
+ "[PALLAS OVERRIDES]: Failed to merge serverParams with PallasOverrides"
+ "[PALLAS OVERRIDES]: Merged serverParams { %{public}@ }"
+ "[PALLAS OVERRIDES]: Merging current serverParams(%{public}@) with PallasOverrides(%{public}@)"
+ "[PALLAS OVERRIDES]: Parsing value set in asset specific default(%{public}@) for PallasOverrides(%{public}@)"
+ "[PALLAS OVERRIDES]: Parsing value set in global default(%{public}@) for PallasOverrides(%{public}@)"
+ "[STARTUP][DURATION:%ldsecs](assets:%ld,configs:%ld,atomic:%ld[locks:%ld],sdesc:%ld,targets:%ld,lookups:%ld,jobs:[single:%ld,set:%ld])"
+ "[SU_PREFS] Background download allowed: %{public}@  automaticCheckEnabled: %{public}@ dataInstall: %{public}@"
+ "[SU_PREFS] Background updates are %{public}@"
+ "[SU_PREFS] Read preference from: %{public}@ for key: %{public}@ with no match and using default value: %{public}@"
+ "[SU_PREFS] Read preference from: %{public}@ for key: %{public}@ with value: %{public}@"
+ "[SecureMAHelper]: Creating new graft list for tracking grafted assets"
+ "[SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
+ "[SecureMAHelper]: Failed to delete graft list file at %@ : %@"
+ "[SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
+ "[SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
+ "[SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
+ "[SecureMAHelper]: Graft list does not exist at %@"
+ "[SecureMAHelper]: Successfully created folder(%@) for grafted list file"
+ "[SecureMAHelper]: Successfully recorded graft entry for asset of type %@"
+ "[WARNING] Asset requires new features - need to look for a new brain that supports these features: %{public}@"
+ "[WARNING] Channel ID is nil for identifier %{public}@"
+ "[WARNING] No population type ID for device!"
+ "[WARNING] Unexpected byte string length"
+ "[WARNING] [GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} skipping %{public}@ since it was modified before %{public}@"
+ "[asset-type:%@]("
+ "[clientName:%@|SubAtomic:%@|(creation)[%@(%@)]Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
+ "[clientName:%@|setEntries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)|previousAI:%@(ticks:%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "[interestInContent:%lld,checkForNewer:%lld,determineIfAvailable:%lld,currentStatus:%lld,lockContent:%lld,mapLockedContent:%lld,continueLockUsage:%lld,endLockUsage:%lld,endPreviousLocks:%lld,endAllPreviousLocks:%lld|eliminateAllForSelector:%lld|eliminateAllForAssetType:%lld|eliminatePromotedNeverLockedForSelector:%lld|stageDetermineAllAvailable:%lld,stageDownloadAll:%lld,stagePurgeAll:%lld,stageEraseAll:%lld,estimateEvictableBytesForSoftwareUpdate:%lld,suspendForSoftwareUpdate:%lld,resumeFromSoftwareUpdate:%lld,suspendResumeStatusForSoftwareUpdate:%lld]"
+ "[type:%@]"
+ "_LastCheckedDate"
+ "_Measurement-SHA256"
+ "_acceptPersonalizationFromPSUSToBecomeLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:"
+ "_acceptPersonalizationToAttempt:forAtomicEntry:"
+ "_acceptPersonalizationToAttempt:forSetDescriptor:withCandidates:extendingToBePersonalized:"
+ "_acceptPersonalizationToAttempt:forSetLookupResult:withCandidates:extendingToBePersonalized:"
+ "_acceptPersonalizationToProvideLatestToVend:forSetConfiguration:withCandidates:extendingToBePersonalized:"
+ "_acceptPersonalizationToProvidePreinstalled:forSetConfiguration:withCandidates:extendingToBePersonalized:"
+ "_acceptStagingClientRequest:fromLocation:adoptingSpecifiedTarget:"
+ "_addCompletionCallbackForSetJobKey:completionCallback:"
+ "_addEvictedCallbackForAtomicInstanceUUID:completionCallback:"
+ "_allPreInstalledDescriptor:forAssetType:"
+ "_anyCurrentLocksForEliminate"
+ "_applyBackgroundTaskOverrides:"
+ "_boostedToCellular"
+ "_boostedToExpensive"
+ "_bootedOSBuildVersion"
+ "_cancelingSetJobsByIdentifier"
+ "_clearAtomicInstanceFromAllSetConfigurations:fromLocation:"
+ "_clearAtomicInstanceFromSetConfiguration:forSetDesriptor:forSetAtomicInstance:fromLocation:"
+ "_completionCallbacksBySetJobKey"
+ "_configuredToCellular"
+ "_configuredToExpensive"
+ "_configuredToUserInitiated"
+ "_constructSetInfoSameFoundFrom"
+ "_constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:"
+ "_creationReason"
+ "_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:"
+ "_discoveredInFlightAtomicInstance"
+ "_downloadingCellular"
+ "_downloadingExpensive"
+ "_effectiveConfiguration"
+ "_endAllSetLocksByClient"
+ "_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:"
+ "_errorUnlessSameVersionFound:changedReportedError:"
+ "_estimateEvictableBytesForSoftwareUpdate"
+ "_everProvidedLatestToVend"
+ "_evictedCallbacksByAtomicInstanceUUID"
+ "_filesystemCachedInfo:forPath:"
+ "_filesystemFileExistAtPathCache"
+ "_filesystemStartupLookupCount"
+ "_forceSetUngraftAndEliminateAllSetLocks:forSetDescriptor:"
+ "_getHealthReportForSets"
+ "_handleClientAlterLockOperation"
+ "_handleClientAlterLockOperation(END_ALL_PREVIOUS_LOCKS)"
+ "_handleClientAlterLockOperation(END_LOCK_USAGE)"
+ "_handleClientAlterLockOperation(END_PREVIOUS_LOCKS)"
+ "_handleClientAlterLockOperationForDescriptor:forEventInfo:error:"
+ "_handleEstimateEvictableBytesForSoftwareUpdateRequest done | totalSystemFileSystemSpace:%llu"
+ "_handleEstimateEvictableBytesForSoftwareUpdateRequestWithBytesBySetIdentifier:"
+ "_handleResumeFromSoftwareUpdateRequest"
+ "_handleStatusForSoftwareUpdateRequest"
+ "_handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce"
+ "_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce:setConfigurationsToEvict:completionBlock:"
+ "_lastestToVendIsLocked"
+ "_lastestToVendMatchesSetConfig"
+ "_latestAtomicInstanceToVendFromPreSUStaging"
+ "_latestDiscoveredAssetSetUUID"
+ "_latestDownloadedAtomicInstanceFromPreSUStaging"
+ "_latestToVendAssetSetUUID"
+ "_latestToVendCachedAssetSetID"
+ "_latestToVendDownloadedFromLive"
+ "_latestToVendLastTimeChecked"
+ "_latestToVendPostedDate"
+ "_limitCachePersistResultByGroupToCount:fromLocation:"
+ "_loadPersistedPostponed"
+ "_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:"
+ "_lockCountsBySelector"
+ "_lockCountsTotal"
+ "_logPersistedConfigLoad:message:"
+ "_manager"
+ "_mostRecentlyReceivedCachedAssetSetID"
+ "_mostRecentlyReceivedDownloadedFromLive"
+ "_mostRecentlyReceivedLastTimeChecked"
+ "_mostRecentlyReceivedPostedDate"
+ "_newAtomicInstancesDownloadedForSetIdentifier"
+ "_newerAtomicInstanceOncePersonalized"
+ "_nonce"
+ "_nonceFileURL"
+ "_nwActivity"
+ "_optionalAssetSizeAllowed"
+ "_persistAssetLock:operation:forAssetLock:withDeltaLockCount:message:"
+ "_persistedKnownDescriptorForFullAssetSelector:"
+ "_persistedKnownDescriptorForPersistedEntryID:"
+ "_preInstalledSetAtomicEntriesFromInstanceEntries"
+ "_preferencePerformanceLoggingEnabled"
+ "_preferenceStagerDetermineLastRequiredTimesOut"
+ "_preinstalledAssetDescriptorsBySelector"
+ "_preinstalledTrackBySelector:"
+ "_previouslyVendedLockedAtomicInstance"
+ "_previouslyVendedLockedAtomicInstances"
+ "_queuedRequestsForNewJobOnceCanceled"
+ "_recordFailedOperation:forReason:"
+ "_recordOperation:"
+ "_removeAssetLock:removingAssetLock:lastClient:forSelector:message:"
+ "_removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:"
+ "_removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:"
+ "_replyHaveStagedContent:withEventInfo:"
+ "_requiringLoadPriorToUse"
+ "_resumeFromSoftwareUpdate"
+ "_schedulerTickOccurred"
+ "_schedulerTickPerformedCrossCheck"
+ "_setConfigurationAdjustedFrom:basedOnSetTarget:"
+ "_setConfigurationsToEvict"
+ "_setIdentifier"
+ "_shortTermForceForget:forSetDescriptor:"
+ "_softwareUpdateSuspendResumeEligibleSetEntryIDs"
+ "_stagedAssetToSetDescriptorCache"
+ "_stagedIsNewOSPromotedCache"
+ "_stagerResumePostponed"
+ "_startupActivationProcessIdentifier"
+ "_startupActivelyStagingAssetCount"
+ "_startupAssetTargetBuildVersion"
+ "_startupAssetTargetOSVersion"
+ "_startupAwaitingStagingAssetCount"
+ "_startupCandidateAssetCount"
+ "_startupDeterminedAvailableAssetCount"
+ "_startupLastStagingFromBuildVersion"
+ "_startupLastStagingFromOSVersion"
+ "_startupModeByGroups"
+ "_startupStagedAssetCount"
+ "_startupStagedAssetTotalContentBytes"
+ "_startupTimeBeginSeconds"
+ "_startupTimeDurationSeconds"
+ "_stateFileURL"
+ "_status"
+ "_submitReportToCoreAnalytics:commonFields:sessionId:"
+ "_submitReportToSplunk:commonFields:sessionId:"
+ "_suspendForSoftwareUpdate"
+ "_suspendResumeStatusForSoftwareUpdate"
+ "_ticksUntilPreviousForceUnlocked"
+ "_trackPerformanceStartupBegin"
+ "_trackerPushNotification"
+ "_tryPersonalizePromoted"
+ "_updateDownloadOptions:"
+ "_updateUserInitiatedFields"
+ "_usageStatus"
+ "action_BoostConfig:error:"
+ "action_DecrementTickDriven:error:"
+ "action_LoadDecideNewOSPromote:error:"
+ "action_ResumeJobs"
+ "action_ScheduleSetJobs"
+ "action_SchedulerJobDownloaded:error:"
+ "action_SchedulerJobFoundSame:error:"
+ "addActiveJobs"
+ "addClientLockReasons"
+ "addNWActivityToDownloadInfo:andTask:andLabel:"
+ "addSuccessfullyDownloadedJobs"
+ "addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:fromLocation:"
+ "addToLockCountsBySelector:addingAssetLock:"
+ "adding event %{public}@"
+ "alloc_count"
+ "altered autoAssetEntries"
+ "altered previouslyVendedLocked (not accessible on startup)"
+ "altered set-configuration converted same-version-found error(s) to SUCCESS | setConfiguration:%@ "
+ "arrayByAddingObject:"
+ "assessDownloadCompletion"
+ "asset locked|"
+ "asset set id for %{public}@ from server is: %{public}@"
+ "assetConfigJobFinished:withDownloadInfo:error:"
+ "assetPersonalizatonAttemptCompletePostEvent:withControlParam:"
+ "assetType: %{public}@"
+ "assetType: %{public}@ asset: %{public}@"
+ "assetType: %{public}@ client: %{public}@, command: %lld (%{public}@)"
+ "assetTypes: %{public}@ client: %{public}@, command: %lld (%{public}@)"
+ "atomic-instance shared lock directory (incomplete set-descriptor atomic-instance)"
+ "atomic-instance without associated set-descriptor"
+ "atomicInstanceDropOncePersonalized:forSetConfiguration:"
+ "atomicInstanceForceUnlock:forgettingAtomicInstance:"
+ "atomicInstanceFromPSUSLookupResultOncePersonalized"
+ "atomicInstanceFromPSUSLookupResultOncePersonalized:forSetConfiguration:"
+ "atomicInstanceIsCurrentlyLocked"
+ "atomicInstanceIsCurrentlyLocked:"
+ "atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:"
+ "atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:"
+ "atomicInstanceNewSetAtomicInstance:forCreationReason:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:"
+ "atomicInstanceUpdateUsageStatus:toNewStatus:forAtomicInstance:"
+ "attempting to commit pre personalized descriptors"
+ "attempting to heal from set job"
+ "auto-asset-descriptor (for provided full-asset-selector) is not currently downloaded"
+ "autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:withCatalogLookupResponse:"
+ "autoSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:"
+ "autoSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:"
+ "availableBytes"
+ "awaiting secure|"
+ "backgroundDownloadsPossible: 1 %{public}@"
+ "base_dir"
+ "boostedToCellular"
+ "boostedToExpensive"
+ "bootedOSBuildVersion"
+ "bucketedDays:"
+ "byGroupAvailableForStagingAttributes"
+ "cancelActiveSetJob:activeSetJob:"
+ "cancelingSetJobsByIdentifier"
+ "cannot accept ended locks by process name since no locks found to be ended"
+ "cannot accept ended locks when no existing lock for auto-specific-asset (ending for all reasons) | fullAssetSelector:%@"
+ "cannot accept ended locks when no existing lock for auto-specific-asset | clientProcessName:%@ | fullAssetSelector:%@"
+ "cannot accept ended locks when no existing lock for auto-specific-asset | endLockReason:%@ | fullAssetSelector:%@"
+ "checkAtomic (NO_WAIT) requested when no latest atomic-instance to vend and no newer-once-personalized"
+ "checkForNewer:"
+ "clear"
+ "clearGraftList:"
+ "cleared"
+ "cleared UUID[%@] (removed across all atomic-instances)"
+ "cleared previoulsy-vended (dropAtomicInstance)"
+ "cleared previoulsy-vended (forceUnlockAtomicInstance)"
+ "cleared previoulsy-vended (nextForgetPreviouslyVendedAtomicInstance)"
+ "cleared stale references from set-configuration"
+ "client %{public}@ requested data migration. No DataMigrator work was needed."
+ "client %{public}@ requested data vault for %{public}@"
+ "client %{public}@ requested data vault for %{public}@, it failed with status: %ld"
+ "client %{public}@ requested data vault for %{public}@, it succeeded"
+ "client-request that had been waiting for set-job to be canceled when set was eliminated"
+ "client: %{public}@ requested reporting %{public}@"
+ "clientRequestsAwaitingDispatchAll"
+ "com.apple.MobileAsset.MobileAssetSHA256Tests"
+ "com.apple.MobileAsset.TKModelMessages"
+ "com.apple.MobileAsset.UAF.Photos.MagicCleanup"
+ "com.apple.MobileAsset.UAF.TKModelMessages"
+ "com.apple.MobileAsset.VideoEffect"
+ "com.apple.mobileassetd.AutoAssetSet.DailyHealthReport"
+ "completionCallbacksBySetJobKey"
+ "configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:"
+ "configuredToCellular"
+ "configuredToExpensive"
+ "configuredToUserInitiated"
+ "considerDownloadedWithPSUSLookupResultsForLatestToVend"
+ "continueLockUsage:"
+ "copyGraftList:"
+ "copyOfLockCountsBySelector"
+ "could not load PMV JSON after download: %{public}@ from %{public}@"
+ "could not load PMV JSON after download: %{public}@ from %{public}@ error %{public}@"
+ "could not load PMV file after download: %{public}@ from %{public}@"
+ "could not load xml file after download: %{public}@ from %{public}@.  Error: %{public}@"
+ "created from setInfoInstance"
+ "creationReason"
+ "currentCalendar"
+ "currentJobByUUID"
+ "currentStatus:"
+ "currentStatusWithStateHandle:"
+ "customer"
+ "daemonProcessStartupBegun"
+ "dataWithContentsOfURL:"
+ "dateByAddingComponents:toDate:options:"
+ "decodeFromLocation"
+ "decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:allowingNilObject:"
+ "decodeFromLocation:ofEntryName:fromPersistedEntry:decodingObjectForKey:ofClass:withEncodeClasses:allowingNilObject:"
+ "decrementClientRequestCount:forEventInfo:"
+ "decremented ticksUntilPreviousForceUnlocked"
+ "dedupAtomicEntries:"
+ "defaultThirdPartyServerURLForAssetType:"
+ "determineIfAvailable:"
+ "dirs(MA_PATH_TO_INSTALL_WITH_OS)"
+ "discoveredInFlightAtomicInstance"
+ "discretionary:%@, timeout:%@ | assetId:%@ | decrypt:%@ | source:%@ | cellular:%@ | expensive:%@ | constrained:%@"
+ "doesSetDescriptor:referenceSetConfiguration:"
+ "doesSetDescriptor:satisfySetConfiguration:allowingMoreDownloaded:"
+ "doesSetDescriptorReferenceAllPreInstalledContent"
+ "doesSetDescriptorReferenceAllPreInstalledContent:"
+ "doesSetDescriptorWithoutVersion:referenceAssetDescriptor:"
+ "doesSetJobDescriptor:representSameContentAs:"
+ "domain:%@"
+ "download of the auto-asset content could not begin (download postponed [scheduled])"
+ "downloadManagerInFlightTasks-cancel"
+ "downloadingCellular"
+ "downloadingExpensive"
+ "dropping set-configuration newer-once-personalized"
+ "dropping set-configuration older newer-once-personalized"
+ "dumpClientUsage for client: %{public}@"
+ "durationSeconds"
+ "endAllPreviousLocks:"
+ "endLockUsage:"
+ "endPreviousLocks:"
+ "ensureStagerFullyResumed"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "errorSummaryForSplunk:"
+ "estEvictableBytesForSU:"
+ "estimateEvictableBytesForSoftwareUpdate"
+ "eventPayloadForCoreAnalytics"
+ "eventPayloadForSplunk"
+ "everProvidedLatestToVend"
+ "evictSetDescriptorIfAwaitingUnlocked"
+ "evictedCallbacksByAtomicInstanceUUID"
+ "existsOnFilesystem"
+ "failed entitlement check for: %lld %{public}@"
+ "failed entitlement check for: %{public}@ with %d for command: %lld (%{public}@)"
+ "failed entitlement check for: %{public}@ with MalformedAssetType for command: %lld (%{public}@)"
+ "failed entitlement check for: nil asset type for command: %lld (%{public}@)"
+ "failed entitlement check for: one %lld %{public}@"
+ "filesystemDoesDirectoryExist:atPath:isDirectory:"
+ "filesystemDoesFileExist:atPath:"
+ "filesystemFileExistAtPathCache"
+ "filesystemFileExistAtPathCache:%ld | filesystemStartupLookupCount:%ld"
+ "filesystemStartupLookupCount"
+ "finishSuspendedResumeFromPersisted"
+ "firstSchedulerCrosscheckTrim"
+ "firstSchedulerCrosscheckTrimAtomicInstances"
+ "firstSchedulerCrosscheckTrimSetDescriptors"
+ "flushPersistedStateCacheAndSetCachingBehaviour:NO"
+ "forceGlobalUnlock"
+ "forceGlobalUnlock:atomicInstancesHandle:"
+ "forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:"
+ "formAvailableForStagingByCombiningRequiredAndOptional:"
+ "formattedDate:"
+ "found atomic instance but not considered locked"
+ "from=%@"
+ "fsgetpath()"
+ "fsid"
+ "fstag"
+ "full replacement"
+ "getGraftListLock"
+ "getGreymatterStatus"
+ "getHealthReports"
+ "getInstalledAssetIds result is %ld for:%{public}@"
+ "getObjectFromMessage: could not decode object for key: %{public}s error: %{public}@"
+ "graft"
+ "graftList.plist"
+ "handleDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:notifyingAutoAssetLayer:"
+ "handleDownloadConfigJobFinished:withDownloadOptions:configError:"
+ "handleEstimateEvictableBytesForSoftwareUpdateRequest"
+ "handleEstimateEvictableBytesForSoftwareUpdateRequest - not in state .Running, unable to estimate."
+ "handleEstimateEvictableBytesForSoftwareUpdateRequest:"
+ "handleResumeFromSoftwareUpdateRequest"
+ "handleResumeFromSoftwareUpdateRequest - already running"
+ "handleResumeFromSoftwareUpdateRequest:"
+ "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:"
+ "handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:"
+ "handleStatusForSoftwareUpdateRequest"
+ "handleStatusForSoftwareUpdateRequest:"
+ "handleSuccessfulDownload"
+ "handleSuspendForSoftwareUpdateRequest"
+ "handleSuspendForSoftwareUpdateRequest - already suspended"
+ "handleSuspendForSoftwareUpdateRequest - bytes needed are unavailable"
+ "handleSuspendForSoftwareUpdateRequest - failed to transition to suspended"
+ "handleSuspendForSoftwareUpdateRequest - missing request info"
+ "handleSuspendForSoftwareUpdateRequest | unexpectedly empty bytesBySetIdentifier!"
+ "handleSuspendForSoftwareUpdateRequest-spaceCheck"
+ "handleSuspendForSoftwareUpdateRequest-suspendComplete"
+ "handleSuspendForSoftwareUpdateRequest:"
+ "handleSuspendResumeForSoftwareUpdateDaemonStartup"
+ "have-received-lookup-response,vending-for-configured"
+ "includesEntryForAssetType:"
+ "incremental"
+ "indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:"
+ "indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:forCreationReason:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstances:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
+ "initForConfigFinishedJobID:andDownloadOptions:withError:"
+ "initForSetAtomicInstanceUUID:"
+ "initForSetConfiguration:withSetDescriptor:withCatalogLookupResponse:"
+ "initForSetJobSchedulerNoClientDownloaded:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:"
+ "initForSetJobSchedulerNoClientFoundSame:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "initWithEstimatedEvictableBytes:"
+ "initWithNonce:status:setConfigurationsToEvict:"
+ "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "initWithPromoted:withSetLookupResults:withRequiringLoadPriorToUse:"
+ "initWithStatus:"
+ "inode"
+ "interestInContent:"
+ "internal"
+ "invalid set-configuration (no set-configuration found) | set-eventInfo:%@"
+ "isAnyAssetFromSetFromNewOSPromoted"
+ "isAnyAssetFromSetFromNewOSPromoted:"
+ "isAtomicInstanceForCurrentSetJob:"
+ "isAtomicInstanceLatestToVendForSet:"
+ "isEveryAssetEntryOnFilesystemForSetDescriptor:forSetDescriptor:"
+ "isMappableToExclaves:"
+ "isNoWaitRequestInvolvingSecureAsset"
+ "isNoWaitRequestInvolvingSecureAsset:"
+ "isSuspendedForSoftwareUpdate:forAssetSetIdentifier:"
+ "isThirdPartyAssetType:"
+ "just cleared newer-once-personalized and unable to create from-staged set-descriptor"
+ "kMA_A_ScheduleJobs"
+ "kern.hv_vmm_present"
+ "keysSortedByValueUsingComparator:"
+ "lastestToVendIsLocked"
+ "lastestToVendMatchesSetConfig"
+ "latestAtomicInstanceToVendFromPreSUStaging"
+ "latestAtomicInstanceToVendFromPreSUStagingKey"
+ "latestDiscoveredAssetSetUUID"
+ "latestDownloadedAtomicInstanceFromPreSUStaging"
+ "latestToVendAssetSetUUID"
+ "latestToVendCachedAssetSetID"
+ "latestToVendDownloadedFromLive"
+ "latestToVendLastTimeChecked"
+ "latestToVendPostedDate"
+ "loadDescriptorsForJobSelector"
+ "loadPersistedCrosscheckStaleForceUnlock"
+ "loadPersistedPostponed"
+ "loaded configuration to determine whether new OS promotion is to occur"
+ "localContentURLOfAssetDescriptor"
+ "locateCancelingSetJobForClientDomain:byIdentifier:"
+ "locateDownloadedNewBySelectorLimitedToStaging"
+ "locateDownloadedNewBySelectorLimitedToStaging:YES"
+ "locateSetDescriptor:forAtomicInstanceUUID:requireExists:"
+ "locateSetDescriptorForSelector"
+ "locateSetDescriptorForStagingDescriptor:"
+ "locateSetStatusForDomainName"
+ "locateStagedSetDescriptorFor"
+ "locateStagedSetDescriptorFor:"
+ "lockContent:"
+ "lockCountsBySelector"
+ "lockCountsTotal"
+ "lockedSelectorsForEliminate"
+ "lookup-response"
+ "manager"
+ "may be stale - routing to set-job|"
+ "message (%{public}@) called without userInfo"
+ "modified"
+ "mostRecentlyReceivedCachedAssetSetID"
+ "mostRecentlyReceivedDownloadedFromLive"
+ "mostRecentlyReceivedLastTimeChecked"
+ "mostRecentlyReceivedPostedDate"
+ "moveAssetIntoRepo"
+ "neededBytes"
+ "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:"
+ "newCurrentLockUsageForSelector"
+ "newSetConfigurationForAssetSetIdentifier:withAutoAssetEntries:"
+ "newSetConfigurationForClientDomainName:forAssetSetIdentifier:withAutoAssetEntries:"
+ "newSetInfoLimitedToCheckInformation"
+ "newerAtomicInstanceOncePersonalized"
+ "newestDownloadedForSetDescriptor"
+ "no auto-asset-descriptors currently downloaded"
+ "no global entitlement found, command %lld (%{public}@) allows asset-type specific entitlement."
+ "no global entitlement found, command %lld (%{public}@) requires asset-type specific entitlement for type not on allowlist. status: %d"
+ "no grafting required|"
+ "notifyEvictedCallbacksForSetDescriptor"
+ "notifyEvictedCallbacksForSetDescriptor:"
+ "now have"
+ "now latest-to-vend|"
+ "numberWithUnsignedInt:"
+ "nwActivity"
+ "objectIsEqual:to:"
+ "optionalAssetSizeAllowed"
+ "overrideGCValue for: %{public}@ cannot proceed with purpose that isn't well formed"
+ "overrideGCValue for: %{public}@ could not determine path to asset, skipping"
+ "overrideGCValue for: %{public}@ failed due to asset id not being well formed"
+ "overrideGCValue for: %{public}@ failed due to nil asset id"
+ "overrideGCValue for: %{public}@ path:%{public}@, days:%lld"
+ "passed entitlement check for: one %lld %{public}@"
+ "permitThirdPartySigningForAssetType:outOrganizations:"
+ "persistDate:forKey:"
+ "persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:"
+ "persisted entry ID was nil"
+ "persistedKnownDescriptorForSelector"
+ "persistedKnownDescriptorForSetAtomicEntry:"
+ "persistedSetLookupResults-removeAllPersistedEntries"
+ "populationTypeString"
+ "postSetNotificationName:forClientDomainName:forAssetSetIdentifier:forAtomicInstanceUUID:fromModule:fromLocation:"
+ "pre-installed is available as newer-once-personalized"
+ "pre-installed set as newer-once-personalized"
+ "preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:"
+ "preferencePerformanceLoggingEnabled"
+ "preferenceStagerDetermineLastRequiredTimesOut"
+ "preinstalledAssetDescriptorsBySelector"
+ "previously active job that was canceled has completed all tracked operations (grant released) - cancel complete"
+ "previouslyVendedLockedAtomicInstance"
+ "previouslyVendedLockedAtomicInstances"
+ "previouslyVendedLockedSummary"
+ "promoteAnyPreviouslyStagedNowDownloaded"
+ "promotedFromStagedToDownloaded"
+ "purging all asset types in list: %{public}@"
+ "q24@0:8^@16"
+ "q24@?0@\"NSDate\"8@\"NSDate\"16"
+ "q24@?0@8@16"
+ "queryNSUrlSessiondAndUpdateState complete, _downloadStateQueue resumed _downloadTasksInFlight: %{public}@"
+ "queuedRequestsForNewJobOnceCanceled"
+ "readyToCommitPrePersonalized:forSetDescriptor:"
+ "received MA_DUMP_CODE_COVERAGE [deprecated] from client %{public}@"
+ "received command from client %{public}@ that should be handled by MA XPC layer: %lld (%{public}@)"
+ "recordAssetGraftStateForEarlyBootTask:"
+ "recordFailedOperation:fromLayer:failingWithError:forTargetOSVersion:forTargetBuildVersion:"
+ "recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:"
+ "recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:"
+ "recordFailedOperation:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:failingWithError:"
+ "recordFailedOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:"
+ "recordFailedOperation:fromLayer:withSelectors:failingWithError:"
+ "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:"
+ "recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:withReason:"
+ "recordOperation:fromLayer:forPushChannelID:forPopulationType:failingWithError:"
+ "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:"
+ "recordOperation:toHistoryType:fromLayer:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:forSelectors:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forAssetSetIdentifier:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:withSelector:"
+ "recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:"
+ "refreshDownloadedToManager:"
+ "refreshSetFoundToManager:fromLocation:"
+ "registerCatalogDownloadJob"
+ "removeAllObsoletedV1Assets Checking: %{public}@ for V1 Assets"
+ "removeAllObsoletedV1Assets Skipping: %{public}@ not removing its V1 assets"
+ "removeAllObsoletedV1Assets Skipping: %{public}@ not removing its V1 assets as assetType is nil in descriptor"
+ "removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:performingHardEliminate:error:"
+ "removed previously downloaded set-descriptor | toBeRemovedSeteDescriptor:%@"
+ "removing any set-lookup-results just reported by pre-SU-staging new-OS promotion"
+ "removing any set-lookup-results stored when earlier pre-SU-staging new-OS promotion"
+ "replaced what had been"
+ "reportSetCatalogDecideFound:fromLocation:"
+ "reporting download attempt %{public}@"
+ "requiringLoadPriorToUse"
+ "resumeFromSU:"
+ "resumeFromSoftwareUpdate"
+ "resumeJobsWhenBeforeFirstUnlock:NO"
+ "retryTask"
+ "returnXml Encoding error: %{public}@"
+ "routing to set-job|"
+ "s:\n"
+ "schedulerTickOccurred"
+ "schedulerTickPerformedCrossCheck"
+ "secure operations pending"
+ "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:fromPreSUStaging:"
+ "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:fromPreSUStaging:completion:"
+ "selector=%@"
+ "selectors=%@"
+ "sendMobileAssetHealthReport:commonFields:sessionId:"
+ "set"
+ "set discoveredInFlight"
+ "set everProvidedLatestToVend"
+ "set haveReceivedLookupResponse"
+ "set-configuration has been eliminated"
+ "set-job completed successfully yet did not result in latest-to-vend (newer-once-personalized)"
+ "set-job completed successfully yet did not result in latest-to-vend nor in newer-once-personalized"
+ "set-job completed with error yet have latest-to-vend when availableForUseError | beforeAvailableForUseError:%@"
+ "set-job indicating same-version-found when set-configuration required fix to vendingAtomicInstanceForConfiguredEntries | eventInfo:%@"
+ "setAllowsConstrainedNetworkAccess:"
+ "setAllowsExpensiveNetworkAccess:"
+ "setAnalyticsManager:"
+ "setAtomicInstance:%@"
+ "setAtomicInstanceUUID"
+ "setBoostedToCellular:"
+ "setBoostedToExpensive:"
+ "setBootedOSBuildVersion:"
+ "setCancelingSetJobsByIdentifier:"
+ "setCompletionCallbacksBySetJobKey:"
+ "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:"
+ "setConfigurationAllPreviouslyVendedForceUnlock:forSetConfiguration:"
+ "setConfigurationAssetSetIDLatestToVend:fromSetDescriptor:forSetConfiguration:buildingPersistReason:"
+ "setConfigurationAssetSetIDMostRecentlyReceived:fromSetDescriptor:forSetConfiguration:buildingPersistReason:"
+ "setConfigurationForDescriptorIfManagedAsSet"
+ "setConfigurationForDescriptorIfManagedAsSet:"
+ "setConfigurationForgetIfTrackedAsPreviouslyVended:forSetConfiguration:removingAtomicInstance:"
+ "setConfigurationIsTrackedAsPreviouslyVended:forSetConfiguration:forAtomicInstanceUUID:"
+ "setConfigurationPersist:fromLocation:forReason:dueToAlter:forHistoryOperation:"
+ "setConfigurationPreviouslyVendedLockedAtomicInstances:"
+ "setConfigurationReferencesDescriptor"
+ "setConfigurationRemovedAtomicInstance:fromLocation:"
+ "setConfigurationTickForPreviouslyVended"
+ "setConfigurationTrackAsPreviouslyVended:forSetConfiguration:addingAtomicInstance:"
+ "setConfigurationTrackLatestToVend:forSetConfiguration:becomingLatestToVend:historyOperation:fromPreSUStaging:"
+ "setConfigurationVendingDescriptor"
+ "setConfigurationsToEvict"
+ "setConfiguredToCellular:"
+ "setConfiguredToExpensive:"
+ "setConfiguredToUserInitiated:"
+ "setDay:"
+ "setDescriptorAllDiscoveredEntriesDownloaded:forSetDescriptor:loggingEntryExists:"
+ "setDescriptorWalkKeys"
+ "setDescriptorWalkLocate:forKey:"
+ "setDiscoveredInFlightAtomicInstance:"
+ "setDownloadingCellular:"
+ "setDownloadingExpensive:"
+ "setEstimateEvictableBytesForSoftwareUpdate:"
+ "setEverProvidedLatestToVend:"
+ "setEvictedCallbacksByAtomicInstanceUUID:"
+ "setFilesystemFileExistAtPathCache:"
+ "setFilesystemStartupLookupCount:"
+ "setIdentifier"
+ "setJobIndicationOfPotentialLatestToVend:forEventInfo:issuingClientReply:"
+ "setLastCheckedDate:"
+ "setLastestToVendIsLocked:"
+ "setLastestToVendMatchesSetConfig:"
+ "setLatestAtomicInstanceToVendFromPreSUStaging:"
+ "setLatestDiscoveredAssetSetUUID:"
+ "setLatestDownloadedAtomicInstanceFromPreSUStaging:"
+ "setLatestToVendAssetSetUUID:"
+ "setLatestToVendCachedAssetSetID:"
+ "setLatestToVendDownloadedFromLive:"
+ "setLatestToVendLastTimeChecked:"
+ "setLatestToVendPostedDate:"
+ "setLoadPersistedPostponed:"
+ "setLockCountsBySelector:"
+ "setLockCountsTotal:"
+ "setLockUsageMapLockCount"
+ "setMostRecentlyReceivedCachedAssetSetID:"
+ "setMostRecentlyReceivedDownloadedFromLive:"
+ "setMostRecentlyReceivedLastTimeChecked:"
+ "setMostRecentlyReceivedPostedDate:"
+ "setNewerAtomicInstanceOncePersonalized:"
+ "setNwActivity:"
+ "setOptionalAssetSizeAllowed:"
+ "setPreferencePerformanceLoggingEnabled:"
+ "setPreferenceStagerDetermineLastRequiredTimesOut:"
+ "setPreinstalledAssetDescriptorsBySelector:"
+ "setPreviouslyVendedLockedAtomicInstances:"
+ "setQueuedRequestsForNewJobOnceCanceled:"
+ "setResumeFromSoftwareUpdate:"
+ "setSchedulerTickPerformedCrossCheck:"
+ "setSetIdentifier:"
+ "setStagedAssetToSetDescriptorCache:"
+ "setStagedIsNewOSPromotedCache:"
+ "setStagerResumePostponed:"
+ "setStartupActivelyStagingAssetCount:"
+ "setStartupAssetTargetBuildVersion:"
+ "setStartupAssetTargetOSVersion:"
+ "setStartupAwaitingStagingAssetCount:"
+ "setStartupCandidateAssetCount:"
+ "setStartupDeterminedAvailableAssetCount:"
+ "setStartupLastStagingFromBuildVersion:"
+ "setStartupLastStagingFromOSVersion:"
+ "setStartupModeByGroups:"
+ "setStartupStagedAssetCount:"
+ "setStartupStagedAssetTotalContentBytes:"
+ "setStartupTimeBeginSeconds:"
+ "setStartupTimeDurationSeconds:"
+ "setStatus:"
+ "setSuspendForSoftwareUpdate:"
+ "setSuspendResumeStatusForSoftwareUpdate:"
+ "setTicksUntilPreviousForceUnlocked:"
+ "setTryPersonalizePromoted:"
+ "setUsageStatus:"
+ "set_nw_activity:"
+ "set_shouldSkipPreferredClientCertificateLookup:"
+ "short-term lock file exists for an atomic instance that does not exist"
+ "shortTermLockFilesHealthCheck"
+ "shortTermLockSetDescriptor:forSetDescriptor:forSpecificAtomicInstance:"
+ "shortUUID:"
+ "sortedArrayUsingComparator:"
+ "specifier"
+ "splitOutAvailableForStagingByGroup:forGroupDetermine:"
+ "stageDetermineAllAvailable:"
+ "stageDownloadAll:"
+ "stageEraseAll:"
+ "stagePurgeAll:"
+ "stagedAssetToSetDescriptorCache"
+ "stagedIsNewOSPromotedCache"
+ "stagedToDownloadedFromStager"
+ "stagerResumePostponed"
+ "stagerResumed:withSetLookupResults:requiringLoadPriorToUse:"
+ "startDownloadAndUpdateState"
+ "startupActivationCompleted"
+ "startupActivationCompleted:"
+ "startupActivationIsFirstExecutionSinceBoot:"
+ "startupActivationResourceSummary"
+ "startupActivelyStagingAssetCount"
+ "startupAssetTargetBuildVersion"
+ "startupAssetTargetOSVersion"
+ "startupAwaitingStagingAssetCount"
+ "startupCandidateAssetCount"
+ "startupDeterminedAvailableAssetCount"
+ "startupLastStagingFromBuildVersion"
+ "startupLastStagingFromOSVersion"
+ "startupModeByGroups"
+ "startupStagedAssetCount"
+ "startupStagedAssetTotalContentBytes"
+ "startupTimeBeginSeconds"
+ "startupTimeDurationSeconds"
+ "statfs failed for %{public}s : %lld (%{public}s)"
+ "summaryOfAssetSelectors:"
+ "supporting SHORT-TERM|"
+ "suspendForSU:"
+ "suspendForSoftwareUpdate"
+ "suspendResumeEnabled"
+ "suspendResumeForSU"
+ "suspendResumeStatusForSU:"
+ "suspendResumeStatusForSoftwareUpdate"
+ "suspended for software update"
+ "suspendedSetConfigurationsFromPreviousOS"
+ "suspendedSetConfigurationsHasCurrentNonce"
+ "targetLookupResultsByGroupDate"
+ "targetOS:%@"
+ "task: %{public}@ completed with no response. task %{public}@"
+ "taskFinishedUpdateState:with:extraInfo:fromLocation:"
+ "taskFinishedUpdateState:with:fromLocation:"
+ "the default/fallback url is not valid when the asset type is nil: '%{public}@'"
+ "the server url is not valid: '%{public}@'"
+ "ticksUntilPreviousForceUnlocked"
+ "ticksUntilPreviousForceUnlocked FIRED - force-unlocked"
+ "time=%@ op=%@ %@ %@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ %@%@"
+ "time=%@ op=%@ %@ %@ %@%@%@"
+ "time=%@ op=%@ %@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@ %@%@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@%@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ domain=%@ %@%@"
+ "time=%@ op=%@ %@ %@ domain=%@%@"
+ "time=%@ op=%@ %@ %@ id-%@ set=%@ domain=%@ %@%@"
+ "time=%@ op=%@ %@ %@ id-%@ set=%@ domain=%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ domain=%@ %@%@"
+ "time=%@ op=%@ %@ %@ id=%@ domain=%@ %@%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ domain=%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ domain=%@%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@ %@%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@ domain=%@ %@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@ domain=%@ %@%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@ domain=%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@ domain=%@%@%@"
+ "time=%@ op=%@ %@ %@ id=%@ set=%@%@%@"
+ "time=%@ op=%@ %@ %@ set=%@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ set=%@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@%@"
+ "time=%@ op=%@ %@ %@%@%@"
+ "time=%@ op=%@ %@ asset=%@ %@%@"
+ "time=%@ op=%@ %@ asset=%@%@"
+ "time=%@ op=%@ %@ count=%004ld %@%@"
+ "time=%@ op=%@ %@ count=%004ld asset=%@ %@%@"
+ "time=%@ op=%@ %@ count=%004ld asset=%@%@"
+ "time=%@ op=%@ %@ count=%004ld%@"
+ "time=%@ op=%@ %@ name=%@ %@%@"
+ "time=%@ op=%@ %@ name=%@%@"
+ "time=%@ op=%@ %@%@"
+ "time=%@ op=%@ selector=%@\n"
+ "time=%@ op=%@ selector=%@ pushChannelID:%@ populationType:%@\n"
+ "timeZoneWithAbbreviation:"
+ "totalFileSystemBytes"
+ "totalFilesystemSpace"
+ "trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:isPromoted:"
+ "trackDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:"
+ "trackPerformanceFilesystemExistCheck:atPath:withFilesystemInfo:justUpdatedCache:"
+ "trackPerformanceIteration:ofContainer:"
+ "trackPerformanceIteration:ofContainer:forSelector:"
+ "trackPerformancePhaseBegin:"
+ "trackPerformancePhaseEnd:"
+ "trackPerformanceStartupEnd:"
+ "trackPerformanceStartupStep:beginningStep:"
+ "trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:fromPreSUStaging:"
+ "trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:"
+ "trackerPushNotification"
+ "trimmedSetIdentifier:"
+ "tryPersonalizePromoted"
+ "typeAndSpecifierKey"
+ "typeAndSpecifierKeyForAssetType:andAssetSpecifier:"
+ "unable to continue lock | descriptor:%@"
+ "unable to create NSURL from path: %{public}@"
+ "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@ | errno:%i"
+ "unable to end all previous locks | descriptor:%@"
+ "unable to end lock | descriptor:%@"
+ "unable to end previous locks | descriptor:%@"
+ "unable to make latest-to-vend since not fully personalized so tracked as newer-once-personalized"
+ "unable to service finished set-job [set-job with no assigned UUID and no eventInfo.autoAssetUUID]"
+ "ungraft"
+ "unknown auto-asset command request received (%@)"
+ "unknown auto-asset lock manipulation command request received | descriptor:%@"
+ "unsignedIntegerValue"
+ "updateLastFetchedDate"
+ "uploadTaskWithRequest:fromData:"
+ "usageStatus"
+ "using latestToVend|"
+ "using newer-once-personalized|"
+ "using pre-installed|"
+ "v208@0:8q16q24@32q40@48@56@64q72q80q88q96q104@112@120@128@136@144@152@160@168Q176Q184@192@200"
+ "v28@0:8B16@20"
+ "v28@0:8I16@20"
+ "v36@0:8@16@24I32"
+ "v40@0:8q16q24q32"
+ "v44@0:8@16@24q32B40"
+ "v44@0:8i16@20@28@36"
+ "v48@0:8q16q24@32@40"
+ "v52@0:8@16@24@32B40q44"
+ "v56@0:8@16@24@32B40B44@?48"
+ "v64@0:8@16B24@28B36B40q44@52B60"
+ "v64@0:8q16q24q32@40@48@56"
+ "v68@0:8q16q24q32@40@48@56B64"
+ "v72@0:8q16q24@32@40@48@56@64"
+ "v72@0:8q16q24q32@40@48@56@64"
+ "v80@0:8q16q24q32@40@48@56@64@72"
+ "v92@0:8q16@24@32@40@48@56@64@72@80B88"
+ "v92@0:8q16q24@32@40@48@56@64Q72Q80B88"
+ "v92@0:8q16q24q32@40@48@56@64Q72Q80B88"
+ "validateShortTermLockURL:normalizedClientDomainNameURL:normalizedAssetSetIdentifierURL:fileManager:"
+ "verifySetDescriptorIsLockable"
+ "wouldSetDescriptorForStagedPlusPrePersonalizedVendAtomicInstance"
+ "wouldSetDescriptorForStagedPlusPrePersonalizedVendAtomicInstance:"
+ "write"
+ "writeDictionaryToFile"
+ "writeJsonDictionaryToFile %{public}@ could not move json from: %{public}@ to: %{public}@ error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ could not move old file: %{public}@ to: %{public}@ error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ could not remove file: %{public}@ (after initial error moving it to: %{public}@) with removal error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ could not remove file: %{public}@ error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ could not remove prior archive file: %{public}@ (will continue) error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ could not remove prior temp file: %{public}@ (will fall back to directly writing) error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ failed to create json stream: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ failed to write json to: %{public}@ error: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ moved existing file: %{public}@ to: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ notifying download manager move complete"
+ "writeJsonDictionaryToFile %{public}@ removed existing file: %{public}@"
+ "writeJsonDictionaryToFile %{public}@ removed existing file: %{public}@ (after initial error moving it to: %{public}@)"
+ "writeJsonDictionaryToFile %{public}@ succeeded"
+ "writeNewSuspendingStateWithNonce:setConfigurationsToEvict:"
+ "xml file contents were not a dictionary: %{public}@ from %{public}@"
+ "xml file failed signature check: %{public}@ from %{public}@"
+ "yyyy-MM-dd HH:mm:ss Z"
+ "{%@:newAssetSetStatus} no set-configuration | clientDomainName:%@ | assetSetIdentifier:%@"
+ "{%@:verifySetDescriptorIsLockable} zero atomic-instance entries | setJobDescriptor:%@"
+ "{%@} (%@)\n[DOWNLOADED-TO-MANAGER]  downloadedAsPatch yet no baseForPatch"
+ "{%@} An entry in latest-to-vend for set %@, %@, has latestDownloadedAtomicInstanceEntries that contain nil value. Entry: %@"
+ "{%@} atomic-instance entry no longer on the filesystem | atomicEntry:%@ | assetDescriptor:%@"
+ "{%@} atomic-instance entry no longer on the filesystem | nextAtomicEntry:%@ | setDescriptor:%@"
+ "{%@} canceling active set-job but unable to form set-job-key | currentSetJob:%@"
+ "{%@} canceling active set-job that is already in canceling table | currentSetJob:%@"
+ "{%@} canceling active set-job that is also already in canceling table | currentSetJob:%@"
+ "{%@} canceling active set-job that is not in routing table | currentSetJob:%@"
+ "{%@} corrupted known-set-atomic-instances container - unable to load key | setDescriptorWalkKey:%@"
+ "{%@} intending to reply to staging-client with indication of no candidates available for staging (pending staging-client-request with no reply-completion)"
+ "{%@} nil atomic-instance entry"
+ "{%@} no jobPersistedState | persistedEntryID:%@"
+ "{%@} no progress status"
+ "{%@} no setAtomicInstance | setJobDescriptor:%@"
+ "{%@} pre-installed set-descriptor without atomic-instance | preInstalledSetDescriptor:%@"
+ "{%@} pre-personalized selector managed as set with latest-to-vend yet unable to locate being-vended set-descriptor | prePersonalizedSelector:%@ | managingSetConfiguration:%@"
+ "{%@} pre-personalized selector yet no downloaded asset descriptor | prePersonalizedSelector:%@"
+ "{%@} previouslyVendedLockedAtomicInstances count of 0 yet present | setConfiguration:%@"
+ "{%@} second component type check - unknown componentType:%@"
+ "{%@} set-atomic-instance without atomicInstanceUUID | hadBeenLatestAtomicInstance:%@"
+ "{%@} set-atomic-instance without set-descriptor | setAtomicInstance:%@"
+ "{%@} set-configuration newer-once-personalized matches not-fully-personalized set-descriptor to become newer-once-personalized | setConfiguration:%@ | setDescriptor:%@"
+ "{%@} set-configuration newer-once-personalized matches set-descriptor to become latest-to-vend | setConfiguration:%@ | setDescriptor:%@"
+ "{%@} set-job being removed that is not an activeSetJob and not a cancelingSetJob | autoSetJob:%@"
+ "{%@} set-job decrementing client request count when not an activeSetJob and not a cancelingSetJob | eventInfo:%@"
+ "{%@} set-job with no assigned UUID and no eventInfo.autoAssetUUID | eventInfo:%@"
+ "{%@} setConfigurationTrackAsPreviouslyVended nil atomic-instance-UUID | setConfiguration:%@"
+ "{%@} ticksUntilPreviousForceUnlocked at 0 yet no previouslyVendedLockedAtomicInstances | setConfiguration:%@"
+ "{%@} unable to decode persisted auto-asset-descriptor entryID:%@"
+ "{%@} unable to determine local repository path for nextDownloadedAtomicEntry:%@"
+ "{%@} unable to locate asset-descriptor for atomic-instance entry | atomicEntry:%@"
+ "{%@} unable to locate asset-descriptor for atomic-instance entry | nextAtomicEntry:%@ | setDescriptor:%@"
+ "{%@} unable to locate atomic-instance UUID | atomicInstanceUUID:%@"
+ "{%@} unknown componentType:%@"
+ "{%@} | nil jobParam on clientRequestsAwaitingSync"
+ "{%@} | no persistedEntryID for fullSelector:%@"
+ "{%@} | no persistedEntryID for noVersionSelector:%@"
+ "{%@} | unable to create canceling-set-job queue | eventInfo:%@"
+ "{%@}%@%@"
+ "{%{public}@ (%{public}@)\n[SET-FOUND] set-job just became set-configuration's latest-to-vend"
+ "{%{public}@:setPolicyValidate} setInstance:%{public}@\n[SET-POLICY](%{public}@) accepted | setPolicy:%{public}@"
+ "{%{public}@:setPolicyValidate} setInstance:%{public}@\n[SET-POLICY](%{public}@) cannot accept set-policy | errorCode:%ld(%{public}@) | setPolicy:%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] additional latest-to-vend moved to previously-vended-still-locked | hadBeenLatestAtomicInstance:%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] all previously vended force-unlocked | dropped atomic-instance%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] all previously vended force-unlocked | previouslyVendedSetDescriptor:%{public}@"
+ "{%{public}@}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] first latest-to-vend moved to previously-vended-still-locked | hadBeenLatestAtomicInstance:%{public}@"
+ "{%{public}@}\n[BECAME-LATEST-TO-VEND] adopted set-descriptor as latest-to-vend | setDescriptor:%{public}@"
+ "{%{public}@}\n[FROM-TRACKED-LATEST-TO-VEND] same version found first-tracked as downloaded set-descriptor | setConfiguration:%{public}@"
+ "{%{public}@}\n[FROM-TRACKED-LATEST-TO-VEND] update to set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "{%{public}@}\n[LATEST-TO-VEND] %{public}@ latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] [NO_CHANGE] atomic-instance entry requiring personalization | nextAtomicEntry:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] [NO_CHANGE] no asset-versions are available to the client | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] not setting latestAtomicInstanceToVend (requiresPersonalization) | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] same version found already tracked as latest-to-vend | setConfiguration:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] same version found is always latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-descriptor matches latest-to-vend when vendingAtomicInstanceForConfiguredEntries=NO | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job found same content already latest-to-vend | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job matches latest-to-vend | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job with no assigned UUID - using event information | eventInfo:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job with no set-job descriptor yet jobAtomicInstance is already downloaded set-descriptor | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job with set-job descriptor that is already a downloaded set-descriptor | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-job with set-job descriptor that is different from already downloaded set-descriptor (using already downloaded) | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] unable to allocate basis for response message | clientRequest:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND][SELF-HEAL] deduped setDescriptor:%{public}@"
+ "{%{public}@}\n[SECURE-COMMITTED-LATEST-TO-VEND] just committed all pre-personalized secure | setDescriptor:%{public}@"
+ "{%{public}@}\n[SET-DESCRIPTOR][VEND] update to set-descriptor provided by set-job | justBecameLatestToVend:%{public}@ | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] %{public}@ | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] cleared set-configuration error tracking | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] failed set-job and no latest-to-vend | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] failed set-job but have latest-to-vend | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] successful set-job and have latest-to-vend | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET_CLIENT_REQUESTS_AWAITING_CANCEL] triggering client-request that had been waiting for set-job canceled | nextHadBeenQueued:%{public}@"
+ "{%{public}@}\n[SET_CLIENT_REQUESTS_AWAITING_CANCEL] | job queued since set-job is being canceled | queued-count:%ld | eventInfo:%{public}@"
+ "{%{public}@}\n[SET_CLIENT_REQUESTS_AWAITING_CANCEL] | last client-request has completed for set-job that is being canceled - still awaiting job finished | cancelingSetJob:%{public}@"
+ "{%{public}@} (%{public}@)\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-PRE] pre-personalized secure auto-asset to be part of atomic-instance (already pre-personalized) | alreadyOnFilesystemSelector:%{public}@"
+ "{%{public}@} (%{public}@)\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-TRY] secure auto-asset to be part of atomic-instance (requires personalization) | alreadyOnFilesystemSelector:%{public}@"
+ "{%{public}@} (%{public}@)\n[DOWNLOADED-TO-MANAGER] no result-found for just-downloaded asset\nJOB-SUMMARY:%{public}@"
+ "{%{public}@} (%{public}@)\n[DOWNLOADED-TO-MANAGER] no result-set-found for just-downloaded auto-asset of auto-asset-set\nJOB-SUMMARY:%{public}@"
+ "{%{public}@} (%{public}@)\n[DOWNLOADED-TO-MANAGER] set-job just became set-configuration's latest-to-vend"
+ "{%{public}@} (%{public}@)\n[DOWNLOADED-TO-MANAGER] unable to create asset-descriptor for just-downloaded asset | invalid:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] considering potential descriptors | potentialDescriptorCount:%{public}lu,alreadyOnFilesystem:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] no valid entries in Pallas response"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] postponing[RAMPED] setConfiguration:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] some in Pallas response already on filesystem (an no newer available) - treat as catalog finding same"
+ "{%{public}@} (%{public}@)\n[SET-DECIDE-FOUND] | filtering out asset from group to be downloaded (same as already on filesystem) | filtered potentialDescriptor:%{public}@"
+ "{%{public}@} (%{public}@)\n[SET-DOWNLOAD] no latest-downloaded-atomic-entries so reporting discovered:\n%{public}@"
+ "{%{public}@} CHECK-NO-WAIT-FLOW[%{public}@] set-configuration:%{public}@"
+ "{%{public}@} Created valid set descriptor from preinstalled set, will adopt as latest to vend."
+ "{%{public}@} Found %lu preinstalled asset descriptor(s) matching assetType: %{public}@"
+ "{%{public}@} LOCK-FLOW[%{public}@] set-configuration:%{public}@"
+ "{%{public}@} Personalization is required to adopt set descriptor."
+ "{%{public}@} Received need for atomic request where latest-to-vend has never been set. Attempting to set latest-to-vend via preinstalled assets."
+ "{%{public}@} [GROUP-MODE] preserved tracking of all previously determined targets | alsoPerformPurgeAll:%{public}@ removeDetermined:%{public}@"
+ "{%{public}@} [GROUP-MODE] removed tracking of all previously determined targets | alsoPerformPurgeAll:%{public}@ removeDetermined:%{public}@"
+ "{%{public}@} [INCOMPLETE-SET-DESCRIPTOR] set-descriptor with downloaded entry missing from filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} [INCOMPLETE-SET-DESCRIPTOR] set-descriptor with downloaded entry missing localContentURL | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@"
+ "{%{public}@} [INCOMPLETE-SET-DESCRIPTOR] set-descriptor with downloaded entry that is not a directory | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} determining atomic-instance to use for checkAtomic (NO_WAIT) | setConfiguration:%{public}@"
+ "{%{public}@} determining atomic-instance to use | setConfiguration:%{public}@"
+ "{%{public}@} downloaded (on filesystem) asset-descriptor | descriptor:%{public}@"
+ "{%{public}@} no downloaded asset-descriptor | assetType:%{public}@, assetSpecifier:%{public}@, assetVersion:%{public}@"
+ "{%{public}@} processing zero-entries set | setConfiguration:%{public}@"
+ "{%{public}@} purged all previously staged content | alsoPerformPurgeAll:%{public}@ removeDetermined:%{public}@"
+ "{%{public}@} set-descriptor discovered by PSUS lookup is currently downloaded [and if secure: is personalized] | nextSetConfiguration:%{public}@ | downloadedAssetDescriptor:%{public}@"
+ "{%{public}@} set-descriptor with downloaded entry on filesystem | entry:%ld-of-%ld | nextDownloadedEntry:%{public}@ | localContentURL:%{public}@"
+ "{%{public}@} tracked as downloaded yet not on filesystem | descriptor:%{public}@"
+ "{%{public}@} | no set-taget entry found for entry:%{public}@"
+ "{%{public}@} | unable to determine previous set-target for entry:%{public}@"
+ "{%{public}@} | unable to re-load set-target for entry:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | decreasing lock count for selector not represented in lockCountsBySelector | selector:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | decreasing lock count for selector with fewer locks tracked (ignored) | lockCountToDecrease:%ld | deltaLockCount:%ld | selector:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | decreasing lock count to 0 - should be a remove operation (ignored) | lockCountToDecrease:%ld | deltaLockCount:%ld | selector:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | increasing lock count for selector not represented in lockCountsBySelector | selector:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | unknown persistedStateOperation type | selector:%{public}@ persistedStateOperation:%{public}@"
+ "{AUTO-LOCKER:%{public}@} failed end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER:_refreshFilesystemMetadataLastInterest} asset-lock refresh skipped for set | asset-lock:%{public}@"
+ "{AUTO-LOCKER:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed lock | client:%{public}@, selector:%{public}@, reason:%{public}@, policy:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER:persistedLocksCount} | unable to determine current auto-asset lock count (no auto-asset-locker)"
+ "{AUTO-LOCKER[totalLocks:%ld]:%{public}@:_persistAssetLock} | unable to record delta-to-locks (no persisted-state) for selector:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:%{public}@:_persistRemoveAssetLock} | no entry ID for selector (ignored) | selector:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:%{public}@:_persistRemoveAssetLock} | removing asset-lock that is not represented in lockCountsBySelector | selector:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:%{public}@:_persistRemoveAssetLock} | unable to remove lock tracker (no persisted-state) for selector:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:%{public}@} successful end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@, ended locks:%ld"
+ "{AUTO-LOCKER[totalLocks:%ld]:_endAllSetLocksNoLongerTracked} | unable to end auto-asset all-locks not tracked in sets | untrackedLock:%{public}@ |  endedLocksAutoAssetError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:_isUntrackedSetAssetLock} | untracked set-asset-lock | assetLock:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:continuedSetLockByClient} | unable to continue auto-asset lock of the set | setAtomicEntry:%{public}@ | continueError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:continuedSetLockByClient} | unable to continue auto-asset lock of the set | setSelector:%{public}@ | continueError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed to drop stale lock | dropFromAssetLock:%{public}@, dropLockTracker:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:eliminateAllPreviousSetLocksByClient} | unable to end auto-asset all-lock for the set | lockedSetDescriptor:%{public}@ | nextEntry:%{public}@ | endedLocksAutoAssetError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:eliminateAllPreviousSetLocksByClient} | unable to end auto-asset all-lock for the set | lockedSetDescriptor:%{public}@ | setSelector:%{public}@ | endedLocksAutoAssetError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:endedPreviousSetLocksByClient} | unable to end auto-asset lock-count of the set | setAtomicEntry:%{public}@ | endedLocksAutoAssetError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:lockedSetByClient} | unable to end auto-asset lock after failure to lock entire set | setAtomicEntry:%{public}@ | endLockError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:{%{public}@} | unable to end auto-asset all-locks for set-identifier | orphanedLock:%{public}@ |  endedLocksAutoAssetError:%{public}@"
+ "{AUTO-STAGER:finishSuspendedResumeFromPersisted} | no auto-asset-stager"
+ "{LoadPersistedDecideResume} beyond delivery of new-OS promotion content yet have content to be promoted"
+ "{RemoveFinishedJob} job has FINISHED | eventInfo:%{public}@"
+ "{ScheduleJobsBefore1st}\n[AUTO-CONTROL-SCHEDULER-TRIGGER] no operations performed since device is before first-unlock"
+ "{ScheduleJobs}\n[AUTO-CONTROL-SCHEDULER-TRIGGER] no singleton jobs started"
+ "{ScheduleJobs}\n[AUTO-CONTROL-SCHEDULER-TRIGGER] singleton job(s) started | singletonScheduledJobsTriggered:%ld"
+ "{ScheduleSetJobs}\n[AUTO-CONTROL-SCHEDULER-TRIGGER] no set jobs started"
+ "{ScheduleSetJobs}\n[AUTO-CONTROL-SCHEDULER-TRIGGER] set job(s) started | setScheduledJobsTriggered:%ld"
+ "{ScheduleSetJobs}\n[SET_CLIENT_REQUESTS_AWAITING_CANCEL] | scheduled job triggered for set-job that is being canceled - not scheduling | schedulerTriggered:%{public}@"
+ "{SetJobLookupResponseRcvd} auto-asset-catalog provided by set-job MISSING MA_CACHED_ASSET_ID_KEY"
+ "{_allPreinstalledDescriptor} returned %llu descriptor(s) for type:%{public}@"
+ "{_currentState} encountered reading suspendResumeState file | unarchiveError:%@"
+ "{_currentState} unable to resolve stateFileURL"
+ "{_handleEstimateEvictableBytesForSoftwareUpdateRequest} done calculating latest atomic instance to vend size | setIdentifier:%@ setFileSystemBytes:%llu"
+ "{_handleEstimateEvictableBytesForSoftwareUpdateRequest} has no latest instance to vend | setIdentifier:%@"
+ "{_handleEstimateEvictableBytesForSoftwareUpdateRequest} missing download descriptor | setIdentifier:%@ setAtomicEntry:%@"
+ "{_handleEstimateEvictableBytesForSoftwareUpdateRequest} no known set configuration | setIdentifier:%@"
+ "{_handleResumeFromSoftwareUpdateRequest} already running, nothing to do."
+ "{_handleResumeFromSoftwareUpdateRequest} expected a state file but none was returned | currentStatus:%@"
+ "{_handleResumeFromSoftwareUpdateRequest} failed to clear resuming file."
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} failed to alloc/init NSMutableArray!"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} failed to alloc/init NSUUID!"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} failed to resolve sorted bytesBySetIdentifier"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} failed to write suspend file, resumed"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} failed to write suspend file, resuming..."
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} found sufficient bytes to evict!"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} missing required parameter | bytesBySetIdentifier:%@ completionBlock:%@"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} missing set configuration | setIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} unable to evict expected bytes, resumed"
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} unable to evict expected bytes, resuming..."
+ "{_handleSuspendForSoftwareUpdateRequestWithNeededBytes} unexpected status!"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} already unlocked! | setIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} evicting  | assetSetIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} eviction cancellation timer fired"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} evictions finished"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} failed setup empty atomic instances, failing suspend."
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} failed to mark latest to vend | setIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} found latestAtomicInstanceToVend, evicted! | clientDomainName:%@ assetSetIdentifier:%@ latestAtomicInstanceToVend:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} found latestAtomicInstanceToVend, scheduling eviction. | clientDomainName:%@ assetSetIdentifier:%@ latestAtomicInstanceToVend:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} missing asset type | assetSetIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} missing latestAtomicInstanceToVend | assetSetIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} setConfiguration missing clientDomainName or assetSetIdentifier| clientDomainName:%@ assetSetIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} unable to locate set descriptor | latestAtomicInstanceToVend:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce} unable to remove downloaded set descriptor | setDescriptor:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} auto-job cancellation timer fired"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} auto-job cancellation timer scheduled"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} auto-job canellations finished"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} found active auto-asset-job, cancelling. | clientDomainName:%@ setJobIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} found active auto-asset-job, finished cancellation. | clientDomainName:%@ setJobIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} missing required parameter | clientDomainName:%@ setJobIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce} unable to compute setJobKey | clientDomainName:%@ setJobIdentifier:%@"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce} failed to write suspend file, resumed"
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce} failed to write suspend file, resuming..."
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce} nonce has changed, do not attempt to update."
+ "{_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce} unexpected state, must be suspending."
+ "{_initializeAutoControl}%@ successfully initialized AutoControlManager FSM (device is before first-unlock) | MA_MILESTONE"
+ "{_initializeAutoControl}%@ successfully initialized AutoControlManager FSM (device is not before first-unlock) | MA_MILESTONE"
+ "{_logResponseBody} ANOLMALY:_parseForAssetDetailsToLog returned nil for detailsToLog for the following asset meta data: %{public}@"
+ "{_preinstalledTrackBySelector} not a pre-installed asset-descriptor | downloadedDescriptor:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for array member | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for key | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for value | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} override not set | value:\n%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} override set | value:\n%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} unable to alloc NSMutableSet"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} unexpected nil for setEntryID | clientDomainName:%@ assetSetIdentifier:%@"
+ "{addLiveServerRequest} Additional AnalyticsInfo for task : %{public}@"
+ "{adoptTargetFromUpdateAttributes}"
+ "{assembleTaskDescriptorWithPurposeAndAutoAssetJobID} invalid autoAssetJobID(ignored):%{public}@"
+ "{atomic instance for short-term lock validation} %{public}@ | clientDomainName:%@ assetSetIdentifier:%@ atomicInstanceUUID:%@"
+ "{atomic instance for short-term lock validation} error extracting atomic instance from path, missing prefix | shortTermLockURL:%@"
+ "{atomic instance for short-term lock validation} found atomic instance but not considered to support short-term locks | clientDomainName:%@ assetSetIdentifier:%@ atomicInstanceUUID:%@"
+ "{atomic instance for short-term lock validation} found atomic instance for short-term lock file | clientDomainName:%@ assetSetIdentifier:%@ atomicInstanceUUID:%@"
+ "{atomic instance for short-term lock validation} latest | clientDomainName:%@ assetSetIdentifier:%@ atomicInstanceUUID:%@"
+ "{atomic instance for short-term lock validation} specific | clientDomainName:%@ assetSetIdentifier:%@ atomicInstanceUUID:%@"
+ "{atomic instance for short-term lock validation} unexpected error extracting atomic instance from path, missing suffix | shortTermLockURL:%@"
+ "{atomic instance for short-term lock validation} unexpected error extracting atomic instance from path, prefix A | shortTermLockURL:%@"
+ "{atomic instance for short-term lock validation} unexpected error extracting atomic instance from path, prefix B | shortTermLockURL:%@"
+ "{atomic instance for short-term lock validation} unexpected error extracting atomic instance from path, suffix A | shortTermLockURL:%@"
+ "{atomic instance for short-term lock validation} unexpected error extracting atomic instance from path, suffix B | shortTermLockURL:%@"
+ "{atomicInstanceDropOncePersonalized} (atomic-instance without set-descriptor)"
+ "{cancelAssetDownloadJob} cancel of overallJobInfo in downloadTasksInFlight | autoAssetJobID:%{public}@, assetType:%{public}@, purpose:%{public}@, assetId:%{public}@, autoAssetName:%{public}@ | taskDescriptor:%{public}@ | result:%ld(%{public}@)"
+ "{cancelAssetDownloadJob} unable to assemble taskDescriptor | autoAssetJobID:%{public}@, assetType:%{public}@, purpose:%{public}@, assetId:%{public}@, autoAssetName:%{public}@ | result:%ld(%{public}@)"
+ "{cancelAssetDownloadJob} unable to locate overallJobInfo in downloadTasksInFlight | autoAssetJobID:%{public}@, assetType:%{public}@, purpose:%{public}@, assetId:%{public}@, autoAssetName:%{public}@ | taskDescriptor:%{public}@ | result:%ld(%{public}@)"
+ "{cancelAssetDownloadTask} cancel of overallJobInfo in downloadTasksInFlight | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask} unable to locate overallJobInfo in downloadTasksInFlight | taskDescriptor:%{public}@"
+ "{categoryForCommand} unknown command:%{public}@"
+ "{checkSplunkStatus} Unable to create base-level event requirements - not sending event | assetType:%{public}@, sessionId:%{public}@, events:%{public}@, uuid:%{public}@"
+ "{clear} encountered error removing file | fileURL:%@ error:%@"
+ "{clear} unable to allow fileURLs"
+ "{clear} unable to resolve fileManager on clear"
+ "{clear} unable to resolve nonceFileURL"
+ "{clear} unable to resolve stateFileURL"
+ "{considerDownloadedWithPSUSLookupResultsForLatestToVend} pre-installed set-descriptor without atomic-instance | preInstalledSetDescriptor:%@"
+ "{currentJobByUUID} unexpected resume of suspended set. | clientDomainName:%@ forAssetSetIdentifier:%@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | additional locked auto-asset for already tracked lock-reason+set-atomic-instance count mismatch - using largest count for set-lock-usage-map | alreadyTrackedCount:%ld | nextLockTracker:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | failed to alloc/init autoAssetSetAtomicInstanceSelector"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | ignoring reason not associated with an asset set | entry:%{public}@ | lockReasonKey:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | set-atomic-instance lock count higher than auto-asset lock count for instance, repairing. | nextLockTracker:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | set-atomic-instance lock count lower than auto-asset lock count for instance, repairing. | nextLockTracker:%{public}@"
+ "{doesSetDescriptor:doesSetDescriptorReferenceAllPreInstalledContent:} downloaded set-descriptor missing asset-descriptor | setDescriptor:%@ | nextDownloadedEntry:%@"
+ "{finishPartiallyPurgedAssets} successful purged cleanup | path:%{public}@ | depth:%d"
+ "{finishPartiallyPurgedAssets} unable to finish purged cleanup | path:%{public}@ | depth:%d | error:%{public}@\n%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor referencing content not on the filesystem | setDescriptor:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor with no latestDownloadedAtomicInstance | setDescriptor:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without atomic-instance | setDescriptor:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without set-configuration | setDescriptor:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load persisted entry | entryID:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load set-descriptor | entryID:%{public}@"
+ "{firstSchedulerCrosscheckTrimSetDescriptors} no entryID"
+ "{handleClientAlterLockOperation} unable to load persistedKnownDescriptors entry | entryID:%{public}@"
+ "{handleClientAlterLockOperation} unable to secure-decode persistedKnownDescriptors entry | entryID:%{public}@"
+ "{handleDownloadConfigJobFinished} Failed to config download"
+ "{handleSuspendForSoftwareUpdateRequest} bytes needed unavailable | neededBytes:%llu availableBytes:%llu"
+ "{handleSuspendForSoftwareUpdateRequest} error transitioning to resume!"
+ "{indicateDownloadJobFinished} unknown job-type(%{public}@) for autoAssetJobID:%{public}@"
+ "{isSSONeededForURL} Adding %{public}@ to set of domains needing SSO"
+ "{isSuspendedForSoftwareUpdate} isSuspendedForSoftwareUpdate:forAssetSetIdentifier observing nil setEntryID | clientDomainName:%@ assetSetIdentifier:%@"
+ "{isSuspendedForSoftwareUpdate} isSuspendedForSoftwareUpdate:forAssetSetIdentifier observing nil softwareUpdateSuspendResumeEligibleSetEntryIDs"
+ "{isSuspendedForSoftwareUpdate} missing required parameter | clientDomainName:%@ assetSetIdentifier:%@"
+ "{loadPersistedCrosscheckStaleForceUnlock} unable to access knownSetAtomicInstancesByInstance | atomicInstanceKey:%@"
+ "{loadPersistedCrosscheckStaleForceUnlock} unable to access knownSetConfigurationsByIdentifier | setConfigurationKey:%@"
+ "{locateCancelingSetJobForClientDomain} missing required | clientDomainName:%@ | assetSetIdentifier:%@"
+ "{newTrackingCommandForEvent} missing required parameters - event:%{public}@, client:%{public}@"
+ "{newTrackingCommandForEvent} unable to allocate command tracker for client:%{public}@ command:%{public}@"
+ "{newTrackingCommandForEvent} unable to allocate command type tracker for remote client:%{public}@ command:%{public}@"
+ "{newTrackingCommandForEvent} unable to associate reply with request from client:%{public}@ command:%{public}@"
+ "{newTrackingCommandForEvent} unable to create XPC reply for un-trackable event from client for command:%{public}@"
+ "{newTrackingCommandForEvent} unable to determine client process identifier(s) for command:%{public}@"
+ "{newTrackingCommandForEvent} unable to track remote client request for command:%{public}@"
+ "{notifyEvictedCallbacksForSetDescriptor} unable to remove downloaded set descriptor | setDescriptor:%@"
+ "{persistedCommand} unknown category:%llu for command:%{public}@"
+ "{purgeAllAssetsInDirectory} %{public}@ requested purge (failed) | assetDirectory:%{public}@ | result:%lld(%{public}@)"
+ "{purgeAllAssetsInDirectory} %{public}@ requested purge (skipped purge [MAPurgeAssetDidntExist]) | assetDirectory:%{public}@"
+ "{purgeAllAssetsInDirectory} %{public}@ requested purge (skipped purge of asset to be preserved) | assetDirectory:%{public}@ | assetID:%{public}@"
+ "{purgeAllAssetsInDirectory} %{public}@ requested purge (successfully purged) | assetDirectory:%{public}@"
+ "{purgeAllAssetsInDirectory} %{public}@ requested purge of %lld assets | assetTypeDirectory:%{public}@"
+ "{purgeAllAssetsOfType} %{public}@ attempted to create asset-type directory to purge but failed | assetType:%{public}@"
+ "{purgeAllAssetsOfType} %{public}@ attempted to purge on invalid asset-type"
+ "{purgeAllAssetsOfType} %{public}@ specified asset-type that could not be normalized"
+ "{purgeAllAssetsOfType} %{public}@ specified asset-type where could not determine pre-installed asset path | assetType:%{public}@"
+ "{purgeAllAssetsOfType} %{public}@ specified invalid purpose:%{public}@ | assetType:%{public}@"
+ "{purgeAllAssetsOfType} %{public}@ specified unsupported path:%{public}@ | assetType:%{public}@"
+ "{purgeAllAssetsOfType} %{public}@ specified unsupported purpose:%{public}@ | assetType:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all for purpose that does not support purge-all | purpose:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all for purpose that is not well formed"
+ "{purgeAll} %{public}@ requested purge-all has finished successfully | asset-types:%ld\n%{public}@"
+ "{purgeAll} %{public}@ requested purge-all that cannot occur before first unlock | assetType:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all where unable to completely purge all assets | asset-types:%ld\n%{public}@"
+ "{purgeAll} %{public}@ requested purge-all with an asset-type that is not well formed | assetType:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all with preserved asset ID that is not well formed | assetType:%{public}@ | assetID:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all with preserved asset type is not well formed | assetType:%{public}@"
+ "{purgeAll} %{public}@ requested purge-all | asset-types:%ld\n%{public}@"
+ "{removeAssetDir} canceling download due to purge | cancelTaskDescriptor:%{public}@ | clientName:%{public}@"
+ "{removeAssetDir} failed to purge (purpose or asset ID not well formed) path:%{public}@ | assetType:%{public}@ | assetID:%{public}@ | purpose:%{public}@ | clientName:%{public}@ | result:%lld(%{public}@)"
+ "{removeAssetDir} failed to purge path:%{public}@ | assetType:%{public}@ | assetID:%{public}@ | clientName:%{public}@ | result:%lld(%{public}@)"
+ "{removeAssetDir} failed to purge secondary path:%{public}@ | assetType:%{public}@ | assetID:%{public}@ | clientName:%{public}@ | result:%lld(%{public}@)"
+ "{removeAssetDir} successfully purged path:%{public}@ | assetType:%{public}@ | assetID:%{public}@ | clientName:%{public}@"
+ "{removeAssetDir} successfully purged secondary path:%{public}@ | assetType:%{public}@ | assetID:%{public}@ | clientName:%{public}@"
+ "{resumeFromPersistedWithDownloadedSelectors} | called a second time when should only be called once"
+ "{sendDownloadResult} [SUCCESS] ANOMALY | jobID != autoAssetJobID:%{public}@ | assetType:%{public}@, purpose:%{public}@, jobID:%{public}@ | downloadInfo:%{public}@"
+ "{sendDownloadResult} catalog download success yet incomplete information | [session] assetType:%{public}@, purpose:%{public}@, jobID:%{public}@ | autoAssetJobID:%{public}@ | downloadInfo:%{public}@"
+ "{setConfigurationPreviouslyVendedLockedAtomicInstances} set-configuration previouslyVendedLockedAtomicInstances references orphan atomic-instance | nextPreviouslyVendedStillLockedUUID:%@ | setConfiguration:%@"
+ "{setConfigurationPreviouslyVendedLockedAtomicInstances} set-configuration with invalid previouslyVendedLockedAtomicInstances | setConfiguration:%@"
+ "{setConfigurationTickForPreviouslyVended}\n[AUTO-CONTROL-PREVIOUSLY-VENDED-LOCKED] decremented countdown to force-unlocked | nextSetConfiguration:%{public}@"
+ "{setLockUsageMapEndedLockForSetDescriptor} no set-locks in set-lock-usage-map for set-descriptor | setDescriptor:%{public}@ | setLockUsageMap:\n%{public}@"
+ "{setPreviousBatchedFailureEvent} Missing required paarameter - not considering re-sending previous failure indication | previousEvent:%{public}@, sendEvents:%{public}@"
+ "{suspendedSetConfigurationsHasCurrentNonce} encountered reading suspendResumeNonce file | unarchiveError:%@"
+ "{suspendedSetConfigurationsHasCurrentNonce} unable to resolve nonceFileURL"
+ "{topLevelActivityForCommand} unknown command:%{public}@"
+ "{updateLastFetchedDate} failed to update lastFetchedDate in xml | targetLocation:%{public}@"
+ "{writeDictionaryToFile} Failed to write dictionary to file, asset type was not well formed: %{public}@"
+ "{writeDictionaryToFile} could not remove file | targetLocation:%{public}@ | error:%{public}@\n%{public}@"
+ "{writeDictionaryToFile} could not remove prior archive file (will continue) | archivePath:%{public}@ | error:%{public}@\n%{public}@"
+ "{writeDictionaryToFile} failed to write XML | targetLocation:%{public}@"
+ "{writeDictionaryToFile} moved existing file | targetLocation:%{public}@ to archivePath:%{public}@"
+ "{writeDictionaryToFile} removed existing file | targetLocation:%{public}@"
+ "{writeDictionaryToFile} succeeded | taskDescriptor:%{public}@"
+ "{writeNewSuspendingStateWithNonce} encountered error serializing nonce | error:%@"
+ "{writeNewSuspendingStateWithNonce} encountered error writing file | fileURL:%@ error:%@"
+ "{writeNewSuspendingStateWithNonce} missing required parameter | nonce:%@ setConfigurationsToEvict:%@"
+ "{writeNewSuspendingStateWithNonce} unable to alloc/init suspendResumeState | nonce:%@ setConfigurationsToEvict:%@"
+ "{writeNewSuspendingStateWithNonce} unable to resolve nonceFileURL"
+ "{write} attempting to write suspendResumeState but nonce is not current"
+ "{write} encountered error serializing suspendResumeState | error:%@"
+ "{write} encountered error writing suspendResumeState | stateFileURL:%@ writeError:%@"
+ "{write} unable to resolve stateFileURL"
+ "{write} writing suspendResumeState | status:%@"
+ "{{public}@} (%{public}@)\n[SET-DECIDE-FOUND] set-catalog lookup summary: %{public}@:catalogCount:%{public}lu,patchDescriptorCount:%{public}lu,fullDescriptorCount:%{public}lu"
- "\n>>> [AUTO-STAGER] >>>\n    stagingFrom: [%@] OSVersion:%@ | BuildVersion:%@\n   activeTarget: %@\n  stagingClient: Determines:%ld | DownloadRequest:%@ | Name:%@\n         active: Config:%@ | Job:%@\n  nowDownloaded: %ld\n            set: Configs:%ld | Targets:%ld\n      scheduled: Jobs:%ld\ncandidateAssets: RequiredByTarget:%ld | OptionalByTarget:%ld | Available:%ld\n  candidateSets: RequiredByTarget:%ld | OptionalByTarget:%ld | Configurations:%ld\n  lookupResults: GroupNames:%@ | [GROUP]SetLookups:%@ | [ALL]SetLookups:%ld\n     baseAssets: ForStaging:%ld\n    determining: BySelector:%ld\navailableAssets: RequiredByTarget:%ld | OptionalByTarget:%ld | Available:%ld\n  stagingCounts: awaiting:%ld | staged:%ld\n       internal: alwaysPromote:%@\n  overallStaged: TotalExpectedBytes:%lld | DownloadedSoFarBytes:%lld\n    elimination: %@\n    stagingMode: Chosen:%@ | UsingGroups:%@ | OnceRequired:%@\n<<<]"
- "\n[AUTO-MANAGER-SECURE]{%{public}@} ERROR | ending all PROCESS-LIFE locks for asset-selector | nextOrphanedLifeLock%{public}@ | nextOrphanedSelector:%{public}@ | error:%{public}@"
- "\n[AUTO-MANAGER-SECURE]{%{public}@} SUCCESS | ended all PROCESS-LIFE locks for asset-selector | nextOrphanedLifeLock%{public}@ | nextOrphanedSelector:%{public}@"
- "\n[AUTO-SECURE]LATEST-DOWNLOADED] {%{public}@} Failed to graft SecureMobileAssetBundle | isSecureMobileAsset:%{public}@ | isAccessible:%{public}@ | setDescriptor:%{public}@ | nextAtomicEntry:%{public}@ | error: %{public}@"
- "\n[AUTO-SECURE][AUTO-GRAFT][STARTUP] {DecideNeedPersonalize} will graft|mount (part of latest-to-vend) | downloadedDescriptor:%{public}@"
- "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} secure not part of latest-to-vend yet managed as set (not considering for secure-healing) | personalizationRequired:%{public}@ | graftedOrMounted:%{public}@ | downloadedDescriptor:%{public}@"
- "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {DecideNeedPersonalize} will personalize (part of latest-to-vend) | downloadedDescriptor:%{public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | post secure startup self-healing - validating all latest-to-vend | persistedEntryIDs Count:%llu"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | unable to load persisted-state entry | entryID:%{public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%{public}@} | unable to load set-configuration | persistedEntry:%{public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-COMMIT][STARTUP] {PersonalizeSuccessDecideMore} | commit pre-personalized asset-selectors ERROR | error:%{public}@ | prePersonalizedSelectors:%ld"
- "\n[SECURE][AUTO-PERSONALIZATION-COMMIT][STARTUP] {PersonalizeSuccessDecideMore} | commit pre-personalized asset-selectors SUCCESS | prePersonalizedSelectors:%ld"
- "\n[SET-CONFIGURATION]{%{public}@:setConfigurationCopy} unable to copy set-configuration | nextSetConfiguration:%{public}@"
- "\n[SET-CONFIGURATION]{%{public}@:setConfigurationCopy} unable to load set-configuration | setConfigurationKey:%{public}@"
- "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} NOT eliminating | nextSetConfiguration:%{public}@"
- "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} eliminating | nextSetConfiguration:%{public}@"
- "\n[SET-ELIMINATE]{%{public}@:setConfigurationEliminate} unable to load persisted-set-configuration file | nextRemoveSetConfiguration:%{public}@"
- "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [BusyPerformingOperation] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
- "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [ResourceUnavailable] unable to allocate eliminate operation tracking entry"
- "\n[SET-ELIMINATE]{%{public}@:setDescriptorEliminate} [SUCCESS] hard-eliminate (pending soft-eliminate should also have completed) | eliminateTracker:%{public}@"
- "\n[SET-ELIMINATE]{IssueClientReplySetJob} [EliminationInProgress] set-identifier is being eliminated | clientRequest:%{public}@"
- "\n[SET-ELIMINATE]{IssueClientReplySetJob} [SecureOperationInProgress] set-identifier already performing a secure-operation | clientRequest:%{public}@"
- "\n[STARTUP-STATE] [PERSISTED] %{public}@\n[STARTUP-STATE] [CURRENT] %{public}@\n[STARTUP-STATE] [KNOWN] %{public}@\n[STARTUP-STATE] [DOWNLOADED] %{public}@\n[STARTUP-STATE] [ACTIVE] %{public}@"
- "\n{chooseNewerSetDescriptor}  left:%{public}@"
- "\n{chooseNewerSetDescriptor} decided left (fewer assets) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided left (right previously staged) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided right (fewer assets) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided right (left previously staged) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetDescriptor} ignoring (invalid restore version) | foundLeftEntry:%{public}@ | nextRightEntry:%{public}@"
- "\n{chooseNewerSetDescriptor} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
- "\n{chooseNewerSetDescriptor} right:%{public}@"
- "\n{chooseNewerSetDescriptor} setConfiguration:%{public}@"
- "\n{chooseNewerSetDescriptor} | leftIsNewer | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetDescriptor} | leftNotPresent | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetDescriptor} | leftRightSame | left:%@ | right:%@"
- "\n{chooseNewerSetDescriptor} | leftRightSame | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetDescriptor} | rightIsNewer | left:%@ | right:%@"
- "\n{chooseNewerSetDescriptor} | rightIsNewer | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetDescriptor} | rightNotPresent | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetStatus} decided left (mixed results) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided left (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided left (right not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided left (right not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided right (left not configured) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided right (left not present) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} decided right (more newer) | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} ignoring (invalid restore version) | foundLeftEntry:%{public}@ | nextRightEntry:%{public}@"
- "\n{chooseNewerSetStatus} ignoring (invalid restore version) | nextLeftEntry:%{public}@ | foundRightEntry:%{public}@"
- "\n{chooseNewerSetStatus} left chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} right chosen | (left)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, (right)NotPresent:%ld,NotConfigured:%ld,IsNewer:%ld, same:%ld"
- "\n{chooseNewerSetStatus} | leftIsNewer | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetStatus} | leftNotPresent | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetStatus} | leftRightSame | left:%@ | right:%@"
- "\n{chooseNewerSetStatus} | leftRightSame | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetStatus} | rightIsNewer | left:%{public}@ | right:%{public}@"
- "\n{chooseNewerSetStatus} | rightNotPresent | left:%{public}@ | right:%{public}@"
- "                      clientDomainName: %@\n                    assetSetIdentifier: %@\n                configuredAssetEntries: %@\n             atomicInstancesDownloaded: %@\n               catalogCachedAssetSetID: %@\n             catalogDownloadedFromLive: %@\n                catalogLastTimeChecked: %@\n                     catalogPostedDate: %@\n         newerAtomicInstanceDiscovered: %@\n          newerDiscoveredAtomicEntries: %@\n              latestDownloadedInstance: %@\n        latestDowloadedInstanceEntries: %@\n     downloadedCatalogCachedAssetSetID: %@\n   downloadedCatalogDownloadedFromLive: %@\n      downloadedCatalogLastTimeChecked: %@\n           downloadedCatalogPostedDate: %@\n                  currentNotifications: %@\n                     currentNeedPolicy: %@\n                currentSchedulerPolicy: %@\n                   currentStagerPolicy: %@\n            haveReceivedLookupResponse: %@\n vendingAtomicInstanceForConfigEntries: %@\n                 downloadUserInitiated: %@\n                      downloadProgress:\n%@\n                downloadedNetworkBytes: %ld\n             downloadedFilesystemBytes: %ld\n                      currentLockUsage:\n%@\n                   selectorsForStaging: %@\n                  availableForUseError: %@\n                     newerVersionError: %@\n"
- " assetSetIdentifier:%@"
- "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
- "%@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, however, download appears to be complete. Previous Total Downloaded: %lld, Total Expected: %lld"
- "%@\n[DOWNLOAD_INFO] {addNewRateDataPoint} Download has not progressed since last update, likely stalled."
- "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} AssetCacheServices not present in this OS, download from: %@"
- "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} Attempting to get cache server url"
- "%@\n[DOWNLOAD_INFO] {determineDownloadUrl} not allowed to use caching server, download from: %@"
- "%@\n[DOWNLOAD_INFO] {updateDownloadData} In progress and totalWritten is less than previous total (%lld < %lld), nsurl is backtracking significantly for %@. task %@"
- "%@ %@ %@"
- "%@ %@ %@..."
- "%@ %@ ...%@(%@)"
- "%@ %@ OWNER %@=>%@ | %@"
- "%@ %@ [%@] %d(%@) | %@"
- "%@ %@ {%@} %@"
- "%@ ----CausedBy---> %@"
- "%@ Attempting to set tokenPath, but cannot convert argument to string"
- "%@ Completed operation to update preference %@ to nil (clear)"
- "%@ Completed operation to update preference %@ to string '%@'"
- "%@ Completed operation to update preferences with values %@"
- "%@ Could not read PMV from: %@ error: file does not exist"
- "%@ Could not read PMV from: %@ error: no path for %@"
- "%@ Setting Pallas audience to '%@' for asset type '%@'"
- "%@ Setting Pallas audience to (null) for asset type '%@'"
- "%@ Setting Pallas enabled to %@ for asset type %@"
- "%@ Setting pallas V2 url to %0x for asset type '%@' failed as the url cannot convert to string"
- "%@ Setting pallas V2 url to '%@' for asset type '%@'"
- "%@ Setting pallas V2 url to nil failed for asset type '%@' as it must be cleared explicitly by the framework"
- "%@ Setting pallas audience to %0x... cannot convert to string."
- "%@ Setting pallas url to nil for asset type '%@'"
- "%@ Token file name is not well formed and cannot be set"
- "%@ Update client usage failed due to nil asset type"
- "%@ asset %@ %@ has been used in past 24 hours '%@': %f"
- "%@ asset %@ %@ unable to update client usage '%@'"
- "%@ assets folder successfully deleted"
- "%@ attempts:%d | Unable to synchronize after setting preference %@ to nil (clear)"
- "%@ attempts:%d | Unable to synchronize after setting preference %@ to string '%@'"
- "%@ attempts:%d | Unable to synchronize after setting preferences with values %@"
- "%@ cancel being applied: %@ for %@ with purpose: %@"
- "%@ cancel result for %@ %@ is: %ld (%@ %@)"
- "%@ canceling task: %@ (asset)"
- "%@ canceling task: %@ (catalog)"
- "%@ canceling task: %@ (other)"
- "%@ canceling task: %@ (pmv)"
- "%@ cannot purgeCatalogs before first unlock"
- "%@ cannot purgeCatalogs with invalid purpose"
- "%@ client Usage type: %@ id:%@, parent path: '%@' AssetData exists"
- "%@ client Usage type: %@ id:%@, parent path: '%@' unable to get AssetData subdirectory"
- "%@ client Usage type: %@ id:%@, path: '%@' original: %f new: %f result: %ld"
- "%@ could not load PMV JSON: %@ error: %@"
- "%@ could not load PMV JSON: %@ error: PMV file contents were not JSON dictionary"
- "%@ could not load PMV JSON: %@ error: nil after deserialization"
- "%@ could not load PMV file: %@"
- "%@ could not purge catalog of type %@ from %@"
- "%@ could not purge catalog of type %@ from %@ (doesn't exist, treating as success)"
- "%@ could not purge catalog of type %@ from nil (path composition faillure)"
- "%@ finished purge catalogs for %@ with purpose: %@"
- "%@ found Pallas URL %@ for asset type %@"
- "%@ found Pallas asset audience %@ for asset type %@"
- "%@ found Pallas enabled %@ for asset type %@"
- "%@ gave invalid preserved ID %@ for %@"
- "%@ gave invalid preserved IDs array for %@"
- "%@ gave invalid preserved IDs dict"
- "%@ gave invalid preserved IDs key"
- "%@ is attempting to cancel %@ %@ (%@)"
- "%@ issued PMV download command %@"
- "%@ issued PMV query command for %@"
- "%@ issued clean v1 for %@"
- "%@ issued download asset command: %@, %@, %@, %@ to local url '%@'"
- "%@ issued load command for %@"
- "%@ issued load of: %@ ID %@ allowing for differences %@"
- "%@ issued load of: %@ ID %@ allowing for differences %@ causing ID error MAQueryParamsEncodeFailure %@"
- "%@ issued load of: %@ ID %@ allowing for differences %@ causing ID error MAQueryParamsEncodeFailure because the allowed differences could not be instantiated"
- "%@ issued load of: %@ ID %@ allowing for differences %@ causing ID error MAQueryParamsEncodeFailure due to having nil for allowedDifferences"
- "%@ issued load of: %@ ID %@ causing ID error MAQueryParamsEncodeFailure %@"
- "%@ issued load of: %@ ID '%@' causing ID error MAQueryParamsEncodeFailure due to the ID not having the correct type"
- "%@ issued meta data download command"
- "%@ issued query command for %@"
- "%@ issued query for installed asset ids for %@"
- "%@ issued space check"
- "%@ makeDataVaultAtUrl %@ status: %lld"
- "%@ nil preference key provided"
- "%@ proceeding before cancel happens. Cannot get in-flight downloads state: %ld for %@ with purpose: %@"
- "%@ provided asset type %@ when %@ was required"
- "%@ purgeCatalogs: the asset types are: %@ with purpose: %@"
- "%@ queried for: %@ with returnType of: %lld (%@) - %@"
- "%@ queried for: %@ with returnType of: %lld with Purpose: %@"
- "%@ request asset audience for asset type %@"
- "%@ requested Pallas URL for asset type %@"
- "%@ requested if Pallas is enabled for asset type %@"
- "%@ set-configuration persisted | setConfiguration:%@"
- "%@ unable to categorize query results for: %@"
- "%@ unable to completely purge all catalogs for %@ with purpose: %@"
- "%@ unable to load catalog for: %@"
- "%@ unable to load repository for: %@"
- "%@ user for AppleConnect token for key retrieval due to override on downloadOptions"
- "%@ | Daemon not ready for download"
- "%@ | FINISH | %@ | %d"
- "%@ | FINISH | %@ | %d(%@)"
- "%@ | FINISH | %@ | SUCCESS"
- "%@ | FINISH | %@ | UNABLE TO REPLY"
- "%@ | START"
- "%@:preInstalledSetDescriptorForSetInstance"
- "%@:secureCheckProcessLifeLocks"
- "%@|status:%ld(set:%ld)|jobs:%ld(set:%ld)(UUID:%ld)|grants:%ld|configs:%ld|AI:%ld|FS:%ld(set:%ld)|sched:%ld|timed:%ld|client:%ld"
- "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld(set:%ld)|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
- "%s: Analytics event recording is %s"
- "%s: Atomic write to path failed and failed to remove temp path(%@): %@"
- "%s: Failed to read boot-args"
- "%s: Failed to write item to path %@"
- "%s: Field is invalid"
- "%s: Unable to get event submission override(unable to get options entry from the device tree)"
- "%s: Unable to get event submission overrides(Could not get master port[%d])"
- "%{public}@\n[%{public}@] {%{public}@} end determine-if-available | assetType:%{public}@"
- "%{public}@\n[%{public}@] {%{publid}@} [STAGING-CLIENT-REQUEST(DETERMINE)] message:%{public}@%{public}@"
- "%{public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-PRE] pre-personalized secure auto-asset to be part of atomic-instance (already pre-personalized) | alreadyOnFilesystemSelector:%{public}@"
- "%{public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-TRY]{reportSetCatalogDecideFound}  secure auto-asset to be part of atomic-instance (requires personalization) | alreadyOnFilesystemSelector:%{public}@"
- "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@OPTIONAL] | nextAvailableDescirptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {%{public}@} [%{public}@REQUIRED] | nextAvailableDescirptor:%{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had been determining from candidates but no determine attempt had found any content to be staged (resuming determining) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had been staging (resuming staging) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} had determined available for staging (resuming determined) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have content staged from currently running OS (resumed to staged) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content now applicable to the currently running OS (migrating) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content when configured to always promote (and now running target OS) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} have previously staged content when configured to always promote (not running target OS) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} inconsistency in staged information (purging) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no persisted entries (purging) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no persisted indication of any pre-software-update-staging status | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} no staging was in progress / no candidates / no staged content (purging to start clean) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staged content from different OS (purging) | %{public}@ | %{public}@"
- "%{public}@\n[AUTO-STAGER] {LoadPersistedDecideResume} staging summary differs from per-entry totals | stagingSummary:%{public}@ | entryTotals:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_controlConvertStagedToDownloaded} NO-IMMEDIATE-PROMOTION: not staged | selectorToBecomeDownloaded:%{public}@"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} not staging auto-asset (from downloaded [set target removes]) | autoAssetDescriptor:%@ | setConfig(by-asset-type):%ld"
- "%{public}@\n[AUTO-STAGER] {_extendLookupByAssetTypeWithDownloadedDescriptors} stage auto-asset (from downloaded [set target includes]) | autoAssetDescriptor:%@ | setConfig(by-asset-type):%ld"
- "%{public}@ | unable to boost set-job to user-initiated | error:%{public}@\nJOB-SUMMARY:%{public}@"
- "%{public}@ | unable to boost to user-initiated | error:%{public}@\nJOB-SUMMARY:%{public}@"
- "%{public}@ | {%{public}@} no latest-downloaded-atomic-entries so reporting discovered:\n%{public}@"
- "%{public}@ | {%{public}@} set-download | SUCCESS | autoAssetSetDescriptor:%{public}@"
- "%{public}@ | {_anyCurrentLocksForEliminate} considering current lock | assetLock:%{public}@ | eliminateSelector:%{public}@"
- "%{public}@ | {_removeAssetLock} | %{public}@: | no entry ID for fullAssetSelector:%{public}@ | assetLock:%{public}@"
- "%{public}@ | {copyOfLocksBySelector} assetLock on locksBySelector with nil fullAssetSelector | selectorName:%{public}@ | assetLock:%{public}@"
- "%{public}@ | {lockedSelectorsForEliminate} considering current lock | assetLock:%{public}@ | eliminateSelector:%{public}@"
- "%{public}@ | {refreshDownloadedToManager} no result-found for just-downloaded asset\nJOB-SUMMARY:%{public}@"
- "%{public}@ | {refreshDownloadedToManager} no result-set-found for just-downloaded auto-asset of auto-asset-set\nJOB-SUMMARY:%{public}@"
- "%{public}@ | {refreshDownloadedToManager} set-job just became set-configuration's latest-to-vend"
- "%{public}@ | {refreshDownloadedToManager} unable to create asset-descriptor for just-downloaded asset | invalid:%{public}@"
- "%{public}@ | {refreshSetFoundToManager} set-job just became set-configuration's latest-to-vend"
- "%{public}@ | {reportSetCatalogDecideFound} filtering out asset from group to be downloaded (same as already on filesystem) | filtered potentialDescriptor:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} no valid entries in Pallas response"
- "%{public}@ | {reportSetCatalogDecideFound} postponing[RAMPED] setConfiguration:%{public}@"
- "%{public}@ | {reportSetCatalogDecideFound} some in Pallas response already on filesystem (an no newer available) - treat as catalog finding same"
- "%{public}@:catalogCount:%{public}lu,patchDescriptorCount:%{public}lu,fullDescriptorCount:%{public}lu"
- "%{public}@:potentialDescriptor:%{public}@,onFS:%{public}@"
- "%{public}@:potentialDescriptorCount:%{public}lu,alreadyOnFilesystem:%{public}@"
- "%{public}s: %{public}@"
- "+[DownloadManager _extractCheckedNSErrorFromDict:withKey:]"
- "+[DownloadManager getPallasUrl:assetType:]"
- "+[DownloadManager isDeviceBeforeFirstUnlock]"
- "+[MABrainBundle garbageCollect]"
- "+[MABrainBundle garbageCollect]_block_invoke"
- "+[MABrainBundle stageProposed:error:]"
- "+[MADActivityManager failureOfActivity:withResult:ofResultName:forReason:]"
- "+[MADActivityManager newTrackingCommandForEvent:forClient:]"
- "+[MADActivityManager newTrackingCommandForEvent:forClient:]_block_invoke"
- "+[MADActivityManager noticeForActivity:reason:]"
- "+[MADActivityManager progressForActivity:calledPrimitive:withBoolResult:]"
- "+[MADActivityManager progressForActivity:calledPrimitive:withErrorResult:]"
- "+[MADActivityManager progressForActivity:calledPrimitive:withSuccessResult:]"
- "+[MADActivityManager progressForActivity:callingPrimitive:]"
- "+[MADActivityManager transferOwnership:toOwner:reason:]"
- "+[MADActivityManager unknownXPCError:forClient:]_block_invoke"
- "+[MADActivityManager unknownXPCType:forClient:]_block_invoke"
- "+[MADActivityManager warningForActivity:fromMethod:leaderNote:warning:]"
- "+[MADActivityTracker categoryForCommand:]"
- "+[MADActivityTracker persistedCommand:]"
- "+[MADActivityTracker topLevelActivityForCommand:]"
- "+[MAStringUtilities writeToByte:fromHexByteString:]"
- "+[PallasResponseVerifier CopyDataFromEncodedBase64:range:]"
- "+[PallasResponseVerifier verifyReceipt:withSignature:]"
- "+[SecureMobileAssetBundle commitStagedManifestsForSelectors:darwinOnly:error:]"
- "+[SecureMobileAssetBundle fsTag:forAssetType:specifier:]"
- "+[SecureMobileAssetBundle getSigningServerURL:]"
- "-[ASAssetMetadataUpdatePolicy _stringPreferenceValueForKey:]"
- "-[ASAssetMetadataUpdatePolicy serverURLForAssetType:]"
- "-[ASAssetMetadataUpdatePolicy trainName]_block_invoke"
- "-[ControlManager _performRootlessRestrictedRepairWithRepository:repairFileDescriptor:]"
- "-[ControlManager _repairRepositoriesIfNecessary]"
- "-[ControlManager applyDataVaults]"
- "-[ControlManager cancelDownload:using:for:assetType:purpose:withExtension:]"
- "-[ControlManager cancelDownload:using:for:assetType:purpose:withExtension:]_block_invoke_2"
- "-[ControlManager checkAndInitiateDownloadForAssetType:message:forClientName:usingConnection:requiringClientExtractor:]"
- "-[ControlManager checkEntitlementAndRespondIfErrorForConnection:usingMessage:forAssetType:withCommand:]"
- "-[ControlManager checkEntitlementAndRespondIfErrorForConnection:usingMessage:forAssetTypes:withCommand:]"
- "-[ControlManager decodeXpcObject:ofClass:dataKey:lengthKey:decodeClasses:error:]"
- "-[ControlManager determineAssets:clientName:connection:downloadingTasks:message:resultTypes:queryArray:isForSpecificAsset:specificAssetId:specificAllowedDifferences:]"
- "-[ControlManager determineBestMatchFor:absoluteId:allowedDifferences:fromResults:isExact:candidates:bestMatch:differencesFound:missedTypeAndAssetIdMatch:]"
- "-[ControlManager determinePmv:clientName:connection:message:queryDict:]"
- "-[ControlManager dictionaryWithArrayOfStringValues:forXpcKey:andLengthKey:clientName:]"
- "-[ControlManager dumpClientUsage:using:and:clientName:]_block_invoke"
- "-[ControlManager getCatalogLastModifiedDate:ifFromXmlUrl:withPurpose:]"
- "-[ControlManager getNotEntitledResultForCommand:]"
- "-[ControlManager getProductMarketingVersions:and:clientName:assetType:]"
- "-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke"
- "-[ControlManager handleCacheDeleteMigration:]"
- "-[ControlManager handleClientConnection:on:]_block_invoke"
- "-[ControlManager handleClientConnection:on:]_block_invoke_2"
- "-[ControlManager handleDataMigrator:message:clientName:]"
- "-[ControlManager handleEnsureDataVault:message:client:clientName:]"
- "-[ControlManager handleGetAllowNonUserInitiated:message:clientName:]"
- "-[ControlManager handleGetServerUrl:message:client:clientName:]"
- "-[ControlManager handleInstallAsset:forType:]"
- "-[ControlManager handleLoadRequest:clientName:connection:message:]"
- "-[ControlManager handleLoadRequest:clientName:connection:message:]_block_invoke"
- "-[ControlManager handleMigrateAssetsRequest:using:and:]_block_invoke"
- "-[ControlManager handlePmvRequest:clientName:connection:message:]"
- "-[ControlManager handlePmvRequest:clientName:connection:message:]_block_invoke"
- "-[ControlManager handleQueryRequest:clientName:connection:message:]"
- "-[ControlManager handleReportingRequest:message:clientName:]_block_invoke"
- "-[ControlManager handleSecureMABundleCommand:message:clientName:]"
- "-[ControlManager handleServerUrlOverride:message:client:clientName:]"
- "-[ControlManager handleUpdateClientUsage:using:and:clientName:]_block_invoke"
- "-[ControlManager handleUpdateMABrain:message:clientName:]"
- "-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke"
- "-[ControlManager init]_block_invoke"
- "-[ControlManager isAllowlistedForCommand:]"
- "-[ControlManager isAssetTypeOptionalForCommand:]"
- "-[ControlManager isAssetTypeRequiredForCommand:]"
- "-[ControlManager isCommandAllowedForAllClientsWithoutAssetType:]"
- "-[ControlManager isCommandRequiringForcedSoftwareUpdateType:]"
- "-[ControlManager isEntitledForCommand:forConnection:forAssetType:]"
- "-[ControlManager loadCatalog:catalogAssets:assetIds:postedDate:lastFetchDate:catalogInfo:withPurpose:]"
- "-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]"
- "-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke"
- "-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke_2"
- "-[ControlManager newCatalogLoad:withPurpose:]"
- "-[ControlManager overrideGCValue:using:and:clientName:]_block_invoke"
- "-[ControlManager performCacheDeleteCollection:forCollectionType:withGarbageCollectionTypes:cacheDeleteResults:]"
- "-[ControlManager performCacheDeleteForGroup:forAssetTypeDir:timeTaken:cacheDeleteResults:]"
- "-[ControlManager performGarbageCollectionOfType:forAssetTypeDir:fromDescriptors:cacheDeleteResults:]"
- "-[ControlManager purgeAll:and:assetTypesList:clientName:]"
- "-[ControlManager purgeAll:and:assetTypesList:clientName:]_block_invoke_2"
- "-[ControlManager purgeAllAssetsInDirectory:clientName:exceptForAssetIds:]"
- "-[ControlManager purgeAllAssetsOfType:forPurpose:clientName:exceptForAssetIds:]"
- "-[ControlManager purgeCatalogOfType:clientName:withPurpose:]"
- "-[ControlManager purgeCatalogOfType:clientName:withPurpose:]_block_invoke"
- "-[ControlManager purgeCatalogs:and:assetTypesList:clientName:]"
- "-[ControlManager purgeCatalogs:and:assetTypesList:clientName:]_block_invoke_2"
- "-[ControlManager registerForCacheDeleteMigration]"
- "-[ControlManager removeAllObsoletedV1Assets]"
- "-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke"
- "-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke_2"
- "-[ControlManager removeDownloadsNotRecentlyInFlight:]"
- "-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke"
- "-[ControlManager sendQueryResults:assetType:purpose:catalogInfo:returnTypes:postedDate:lastFetchedDate:result:isFiltered:requireSpecificAsset:connection:message:clientName:]"
- "-[ControlManager setPreferenceKeySync:andValue:allowNilToClear:]"
- "-[ControlManager setServerConnectionHandler:with:and:]_block_invoke"
- "-[ControlManager updateLastFetchedDate:assetType:withPurpose:with:]_block_invoke"
- "-[ControlManager writeDictionaryToFile:to:with:]_block_invoke"
- "-[ControlManager writeJsonDictionaryToFile:to:with:]_block_invoke"
- "-[DownloadInfo addNewRateDataPoint:]"
- "-[DownloadInfo determineDownloadUrl:callback:]"
- "-[DownloadInfo updateDownloadData:]"
- "-[DownloadManager MACopyDawToken:]"
- "-[DownloadManager _logResponseBody:nonce:extraServerOptions:]"
- "-[DownloadManager addInFailedJobs:finalEvents:]"
- "-[DownloadManager addLiveServerRequest:forAssetType:withPurpose:audience:pallasUrl:using:with:clientName:autoAssetJobID:task:options:]"
- "-[DownloadManager applyTransforms:toAssets:]"
- "-[DownloadManager applyTransformsAndCheckReceipts:transformations:assetType:assets:receiptResults:]"
- "-[DownloadManager assessDownloadCompletion:originalUrl:taskDescription:taskId:error:moveFile:extractorExists:]_block_invoke"
- "-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]"
- "-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke"
- "-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke"
- "-[DownloadManager cancelAssetDownloadTask:]_block_invoke"
- "-[DownloadManager checkAssetDownloadIsSkipped:connection:with:autoAssetJob:]"
- "-[DownloadManager checkCatalogDownloadIsSkipped:connection:with:autoAssetJob:]"
- "-[DownloadManager checkDownloadIsSyncing:using:with:autoAssetJob:]"
- "-[DownloadManager checkPmvDownloadIsSkipped:connection:with:]"
- "-[DownloadManager checkSplunkStatus:failureReason:productVersion:sessionId:nonce:url:statusCode:assetAudience:version:receiptResults:baseUrl:discretionary:deviceCheck:]_block_invoke"
- "-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke"
- "-[DownloadManager configDownload:clientName:using:with:]"
- "-[DownloadManager decryptContentEncryptedAssetAtPathIfRequired:]"
- "-[DownloadManager getCurrentInflightDownloads:]_block_invoke_2"
- "-[DownloadManager getCurrentInflightDownloads:]_block_invoke_3"
- "-[DownloadManager getPallasEnabledForAssetType:]"
- "-[DownloadManager handleSplunkReportFinished:result:]"
- "-[DownloadManager handleSplunkReportFinished:result:]_block_invoke"
- "-[DownloadManager handleSuccessfulDownload:task:taskId:shouldMove:extractorExists:postedDate:notModified:]"
- "-[DownloadManager indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:performingAutoAssetJob:ofJobType:]"
- "-[DownloadManager init]"
- "-[DownloadManager init]_block_invoke"
- "-[DownloadManager initializeSessionsAsync]_block_invoke"
- "-[DownloadManager massagePmvAndPersist:from:to:postedDate:]"
- "-[DownloadManager massageXmlAndPersist:catalogInfo:descriptor:assets:transformations:to:postedDate:receiptResults:assetSetId:pallasUrl:considerCaching:]"
- "-[DownloadManager massageXmlAndPersist:from:to:with:postedDate:considerCaching:]"
- "-[DownloadManager newAssetAudience:assetType:]"
- "-[DownloadManager pallasRequestRequiresAuthentication:serverParams:]"
- "-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]"
- "-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke"
- "-[DownloadManager processAssetDownload:with:and:shouldMove:extractorExists:]"
- "-[DownloadManager queryNSUrlSessiondAndUpdateState]"
- "-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke"
- "-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke_2"
- "-[DownloadManager registerAssetDownloadJob:forAssetType:withPurpose:clientName:usingDownloadOptions:forAssetId:withCatalogMetadata:withSpaceCheckedUUID:]"
- "-[DownloadManager registerAssetDownloadJob:forThis:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:connection:message:clientName:notify:withCatalogMetadata:withSpaceCheckedUUID:]"
- "-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]"
- "-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke"
- "-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]"
- "-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke"
- "-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke_2"
- "-[DownloadManager registerPmvDownloadJob:using:with:clientName:]"
- "-[DownloadManager registerPmvDownloadJob:using:with:clientName:]_block_invoke"
- "-[DownloadManager registerXmlDownloadJob:using:with:clientName:]"
- "-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke"
- "-[DownloadManager retryTask:retryUrl:modified:clientName:]_block_invoke"
- "-[DownloadManager sendDownloadCannotStartResult:assetType:connection:requestMessage:clientName:autoAssetJobID:ofJobType:underlyingError:additionalData:]"
- "-[DownloadManager sendDownloadResult:with:extraInfo:]"
- "-[DownloadManager sendEvents:sessionId:]"
- "-[DownloadManager sendNotification:suffix:]"
- "-[DownloadManager setPreviousBatchedFailureEvent:inSendEventsByUUID:]"
- "-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]"
- "-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke"
- "-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke_2"
- "-[DownloadManager startDownloadTask:downloadSize:for:startingAt:withLength:extractWith:options:modified:session:isCachingServer:]"
- "-[DownloadManager startDownloadTimer]_block_invoke"
- "-[DownloadManager stopTimerIfNoDownloadsInProgress]"
- "-[DownloadManager syncSplunkTasks]"
- "-[DownloadManager syncSplunkTasks]_block_invoke_2"
- "-[DownloadManager taskFinishedUpdateState:with:extraInfo:]"
- "-[DownloadManager taskFinishedUpdateState:with:extraInfo:]_block_invoke"
- "-[DownloadManager triggerVPN]_block_invoke"
- "-[DownloadManager updateEstimateInfo:]_block_invoke"
- "-[DownloadManager updateStateAndNotifyIfRequired]"
- "-[DownloaderSessionDelegate URLSession:didReceiveChallenge:completionHandler:]"
- "-[DownloaderSessionDelegate URLSession:downloadTask:didFinishDownloadingToURL:]"
- "-[DownloaderSessionDelegate URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]"
- "-[DownloaderSessionDelegate URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]"
- "-[DownloaderSessionDelegate URLSession:task:didCompleteWithError:]"
- "-[MABrainBundle graft:]"
- "-[MABrainBundle graftdmgType]"
- "-[MABrainBundle personalize:options:error:]"
- "-[MABrainBundle stageCurrent:]"
- "-[MABrainBundle ungraft:]"
- "-[MABrainDownloader download:options:completion:]"
- "-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2"
- "-[MABrainUpdater commit]_block_invoke"
- "-[MABrainUpdater hasAppleConnect]"
- "-[MABrainUpdater install:asset:options:completion:]"
- "-[MABrainUpdater install:asset:options:completion:]_block_invoke"
- "-[MABrainUpdater purge:completion:]_block_invoke"
- "-[MABrainUpdater schedule:]"
- "-[MABrainUpdater schedule:]_block_invoke"
- "-[MABrainUpdater schedule:]_block_invoke_2"
- "-[MABrainUpdater start:]_block_invoke"
- "-[MABrainUpdater start:]_block_invoke_2"
- "-[MABrainUpdater start:]_block_invoke_3"
- "-[MABrainUpdater update:completion:]_block_invoke"
- "-[MABrainUpdater update:completion:]_block_invoke_2"
- "-[MABrainUpdater update:completion:]_block_invoke_4"
- "-[MABrainUpdater update:completion:]_block_invoke_5"
- "-[MABrainUpdater writePlist:path:error:]"
- "-[MADActivityManager _finishClientCommandActivity:withResult:ofResultName:ableToReply:]"
- "-[MADActivityManager _startClientCommandActivity:]"
- "-[MADAnalyticsEvent setEventPayloadEntry:value:]"
- "-[MADAnalyticsEventSubmitter _queue_registerSendEvent:]"
- "-[MADAnalyticsEventSubmitter _queue_registerSendEvent:]_block_invoke"
- "-[MADAnalyticsEventSubmitter _queue_removeAllEvents]"
- "-[MADAnalyticsEventSubmitter _queue_removeEvent:]"
- "-[MADAnalyticsEventSubmitter _queue_removeEventsWithName:]"
- "-[MADAnalyticsEventSubmitter _queue_setEvent:]"
- "-[MADAnalyticsEventSubmitter _queue_submitAllEvents]"
- "-[MADAnalyticsEventSubmitter _queue_submitEvent:]"
- "-[MADAnalyticsEventSubmitter _queue_submitEventsWithName:]"
- "-[MADAnalyticsEventSubmitter removeEvent:]_block_invoke"
- "-[MADAnalyticsEventSubmitter removeEventsWithName:]_block_invoke"
- "-[MADAnalyticsEventSubmitter setEvent:]_block_invoke"
- "-[MADAnalyticsEventSubmitter submitEvent:]_block_invoke"
- "-[MADAnalyticsEventSubmitter submitEventsWithName:]_block_invoke"
- "-[MADAnalyticsManager analyticsPreferences]_block_invoke"
- "-[MADAnalyticsManager copyEventFromPath:]"
- "-[MADAnalyticsManager initWithPath:]"
- "-[MADAnalyticsManager init]"
- "-[MADAnalyticsManager recordDownloadAttemptForAssetType:clientName:baseUrl:relativePath:purpose:result:analyticsFileType:isAutoDownload:isPallas:pallasAssetAudience:isUserPriority:bytesWritten:bytesTransferredEst:brainVersion:withTaskMetrics:withOptions:additionalData:]"
- "-[MADAnalyticsManager recordEventWithName:assetType:payload:]"
- "-[MADAnalyticsManager removeAllEvents]_block_invoke"
- "-[MADAnalyticsManager removeEvent:]_block_invoke"
- "-[MADAnalyticsManager removeEventsWithName:]_block_invoke"
- "-[MADAnalyticsManager saveEventToDisk:]_block_invoke"
- "-[MADAnalyticsManager shouldRecordEventForAssetType:]"
- "-[MADAnalyticsManager submitAllEvents]_block_invoke"
- "-[MADAnalyticsManager submitEvent:]_block_invoke"
- "-[MADAnalyticsManager submitEventsWithName:]_block_invoke"
- "-[MAPushChannel channelIDForPopulationType]"
- "-[MAPushChannel initWithIdentifier:]"
- "-[MAPushChannel initWithPopulationType:]"
- "-[MAPushNotificationClient didReceivePushNotificationWithInfo:]_block_invoke"
- "-[MAPushNotificationServiceDaemon addSyntheticJobWithType:assetSpecifier:matchingAssetVersion:triggerInterval:]"
- "-[MAPushNotificationServiceDaemon channelSubscriptionsFailedWithReasons:]"
- "-[MAPushNotificationServiceDaemon didReceivePushNotification:]"
- "-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]"
- "-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke"
- "-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke_2"
- "-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke_3"
- "-[MAPushNotificationServiceDaemon subscribeToChannelForCurrentPlatform]"
- "-[MAPushNotificationServiceDaemon subscribeToChannelWithIdentifier:]"
- "-[MAPushNotificationServiceDaemon triggerPushNotificationWithPayload:]"
- "-[MAPushNotificationServiceDaemon unsubscribeFromAllChannels]"
- "-[MAPushNotificationServiceDaemon unsubscribeToChannelWithIdentifier:]"
- "-[MAPushServiceConnection _APSConnectionEnvironment]"
- "-[MAPushServiceConnection _publicChannelForPushChannel:]"
- "-[MAPushServiceConnection _subscribeToChannel:]"
- "-[MAPushServiceConnection _unsubscribeFromChannel:]"
- "-[MAPushServiceConnection connection:channelSubscriptionsFailedWithFailures:]"
- "-[MAPushServiceConnection connection:didReceiveIncomingMessage:]"
- "-[MAPushServiceConnection initWithDelegate:]"
- "-[MAPushServiceConnection subscribedChannels]"
- "-[NSDictionary(MABrainFeatures) areRequirementsMetByBrain:error:]"
- "-[NSDictionary(MABrainFeatures) areRequirementsMetByBrainFeatures:missingRequirements:error:]"
- "-[NSDictionary(MABrainFeatures) areRequirementsMetByBrain]"
- "-[PallasResponseVerifier verifyCerts:error:]"
- "-[PallasResponseVerifier verifyCerts:error:]_block_invoke"
- "-[SecureMobileAssetBundle _generateNonceProposalForHandle:digest:nonce:error:]"
- "-[SecureMobileAssetBundle _manifestDataFromFullyFormedTicket:]"
- "-[SecureMobileAssetBundle _personalize:error:]"
- "-[SecureMobileAssetBundle _personalizedBundleTicketData]"
- "-[SecureMobileAssetBundle _shouldForcePersonalizationFailure]"
- "-[SecureMobileAssetBundle _storeManifest:stage:error:]"
- "-[SecureMobileAssetBundle attach:error:]"
- "-[SecureMobileAssetBundle beginAccess_nowait:error:]"
- "-[SecureMobileAssetBundle depersonalize:]"
- "-[SecureMobileAssetBundle endAccess_nowait:error:]"
- "-[SecureMobileAssetBundle graft:]"
- "-[SecureMobileAssetBundle graftOrMount:]"
- "-[SecureMobileAssetBundle mount:]"
- "-[SecureMobileAssetBundle personalize:completionQueue:completion:]"
- "-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke"
- "-[SecureMobileAssetBundle stagedPersonalizedManifestPath]"
- "-[SecureMobileAssetBundle ticketPath]"
- "-[SecureMobileAssetBundle ungraft:]"
- "-[SecureMobileAssetBundle unmount:]"
- "-[SecureMobileAssetMountManager _shouldDissentUnmount:]"
- "-[SecureMobileAssetMountManager registerDissenterForVolume:]"
- "-[SecureMobileAssetMountManager registerDissenterForVolume:]_block_invoke"
- "-[SecureMobileAssetMountManager unregisterDissenterForVolume:]"
- "-[SplunkSessionDelegate URLSession:task:didCompleteWithError:]"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
- "2.1.13"
- "2.4.1"
- ">>>\n                       interestInContent: %lld\n                           checkForNewer: %lld\n                    determineIfAvailable: %lld\n                           currentStatus: %lld\n                             lockContent: %lld\n                        mapLockedContent: %lld\n                       continueLockUsage: %lld\n                            endLockUsage: %lld\n                        endPreviousLocks: %lld\n                     endAllPreviousLocks: %lld\n                 eliminateAllForSelector: %lld\n                eliminateAllForAssetType: %lld\n eliminatePromotedNeverLockedForSelector: %lld\n              stageDetermineAllAvailable: %lld\n                        stageDownloadAll: %lld\n                           stagePurgeAll: %lld\n                           stageEraseAll: %lld\n<<<]"
- ">>>\nCategory                    Statistic                   Value\n=========================== =========================== ================================\ntotalClientRequests                  interestInContent: %lld\ntotalClientRequests                      checkForNewer: %lld\ntotalClientRequests               determineIfAvailable: %lld\ntotalClientRequests                      currentStatus: %lld\ntotalClientRequests                        lockContent: %lld\ntotalClientRequests                  continueLockUsage: %lld\ntotalClientRequests                       endLockUsage: %lld\ntotalClientRequests                   endPreviousLocks: %lld\ntotalClientRequests                endAllPreviousLocks: %lld\ntotalClientRequests         stageDetermineAllAvailable: %lld\ntotalClientRequests                   stageDownloadAll: %lld\ntotalClientRequests                      stagePurgeAll: %lld\ntotalClientRequests                      stageEraseAll: %lld\n\ntotalClientRepliesSuccess            interestInContent: %lld\ntotalClientRepliesSuccess                checkForNewer: %lld\ntotalClientRepliesSuccess         determineIfAvailable: %lld\ntotalClientRepliesSuccess                currentStatus: %lld\ntotalClientRepliesSuccess                  lockContent: %lld\ntotalClientRepliesSuccess            continueLockUsage: %lld\ntotalClientRepliesSuccess                 endLockUsage: %lld\ntotalClientRepliesSuccess             endPreviousLocks: %lld\ntotalClientRepliesSuccess          endAllPreviousLocks: %lld\ntotalClientRepliesSuccess   stageDetermineAllAvailable: %lld\ntotalClientRepliesSuccess             stageDownloadAll: %lld\ntotalClientRepliesSuccess                stagePurgeAll: %lld\ntotalClientRepliesSuccess                stageEraseAll: %lld\n\ntotalClientRepliesFailure            interestInContent: %lld\ntotalClientRepliesFailure                checkForNewer: %lld\ntotalClientRepliesFailure         determineIfAvailable: %lld\ntotalClientRepliesFailure                currentStatus: %lld\ntotalClientRepliesFailure                  lockContent: %lld\ntotalClientRepliesFailure            continueLockUsage: %lld\ntotalClientRepliesFailure                 endLockUsage: %lld\ntotalClientRepliesFailure             endPreviousLocks: %lld\ntotalClientRepliesFailure          endAllPreviousLocks: %lld\ntotalClientRepliesFailure   stageDetermineAllAvailable: %lld\ntotalClientRepliesFailure             stageDownloadAll: %lld\ntotalClientRepliesFailure                stagePurgeAll: %lld\ntotalClientRepliesFailure                stageEraseAll: %lld\n\ntotalQueuedClientRequests            interestInContent: %lld\ntotalQueuedClientRequests                checkForNewer: %lld\ntotalQueuedClientRequests         determineIfAvailable: %lld\ntotalQueuedClientRequests                currentStatus: %lld\ntotalQueuedClientRequests                  lockContent: %lld\ntotalQueuedClientRequests            continueLockUsage: %lld\ntotalQueuedClientRequests                 endLockUsage: %lld\ntotalQueuedClientRequests             endPreviousLocks: %lld\ntotalQueuedClientRequests          endAllPreviousLocks: %lld\ntotalQueuedClientRequests   stageDetermineAllAvailable: %lld\ntotalQueuedClientRequests             stageDownloadAll: %lld\ntotalQueuedClientRequests                stagePurgeAll: %lld\ntotalQueuedClientRequests                stageEraseAll: %lld\n\ntotalDequeuedClientRequests          interestInContent: %lld\ntotalDequeuedClientRequests              checkForNewer: %lld\ntotalDequeuedClientRequests       determineIfAvailable: %lld\ntotalDequeuedClientRequests              currentStatus: %lld\ntotalDequeuedClientRequests                lockContent: %lld\ntotalDequeuedClientRequests          continueLockUsage: %lld\ntotalDequeuedClientRequests               endLockUsage: %lld\ntotalDequeuedClientRequests           endPreviousLocks: %lld\ntotalDequeuedClientRequests        endAllPreviousLocks: %lld\ntotalDequeuedClientRequests stageDetermineAllAvailable: %lld\ntotalDequeuedClientRequests           stageDownloadAll: %lld\ntotalDequeuedClientRequests              stagePurgeAll: %lld\ntotalDequeuedClientRequests              stageEraseAll: %lld\n\nautoJobs                     totalAutoAssetJobsStarted: %lld\nautoJobs                         totalAutoJobsFinished: %lld\nstagerJobs             totalStagerDetermineJobsStarted: %lld\nstagerJobs            totalStagerDetermineJobsFinished: %lld\nstagerJobs              totalStagerDownloadJobsStarted: %lld\nstagerJobs             totalStagerDownloadJobsFinished: %lld\nresumedInFlightJobs           totalResumedInFlightJobs: %lld\nscheduledJobs              totalSchedulerTriggeredJobs: %lld\nfailuresToStartJobs           totalFailuresToStartJobs: %lld\n\npreviously           previouslyDownloadedPatchedAssets: %lld\npreviously            previouslyDownloadedPatchedBytes: %lld\npreviously              previouslyDownloadedFullAssets: %lld\npreviously               previouslyDownloadedFullBytes: %lld\n\ndownloaded                totalDownloadedPatchedAssets: %lld\ndownloaded                 totalDownloadedPatchedBytes: %lld\ndownloaded                   totalDownloadedFullAssets: %lld\ndownloaded                    totalDownloadedFullBytes: %lld\n\nstaged                        totalStagedPatchedAssets: %lld\nstaged                         totalStagedPatchedBytes: %lld\nstaged                           totalStagedFullAssets: %lld\nstaged                            totalStagedFullBytes: %lld\n\nunstaged                    totalUnstagedPatchedAssets: %lld\nunstaged                     totalUnstagedPatchedBytes: %lld\nunstaged                       totalUnstagedFullAssets: %lld\nunstaged                        totalUnstagedFullBytes: %lld\n\npromoted                    totalPromotedPatchedAssets: %lld\npromoted                     totalPromotedPatchedBytes: %lld\npromoted                       totalPromotedFullAssets: %lld\npromoted                        totalPromotedFullBytes: %lld\n\nremoved                      totalRemovedPatchedAssets: %lld\nremoved                       totalRemovedPatchedBytes: %lld\nremoved                         totalRemovedFullAssets: %lld\nremoved                          totalRemovedFullBytes: %lld\n\nfinishedJobs        finishedJobSchedulerNetworkFailure: %lld\nfinishedJobs     finishedJobSchedulerNotNetworkRelated: %lld\nfinishedJobs           finishedJobClientNetworkFailure: %lld\nfinishedJobs        finishedJobClientNotNetworkRelated: %lld\n\ngarbageColection                             performed: %@\ngarbageColection                          reclaimSpace: %@\ngarbageColection                   totalReclaimedSpace: %@\ngarbageColection                 reclaimedV2AssetCount: %ld\ngarbageColection                 reclaimedV2AssetSpace: %@\ngarbageColection                reclaimedUnlockedCount: %ld\ngarbageColection                reclaimedUnlockedSpace: %@\ngarbageColection       reclaimedLockedOverridableCount: %ld\ngarbageColection       reclaimedLockedOverridableSpace: %@\ngarbageColection       reclaimedLockedNeverRemoveCount: %ld\ngarbageColection       reclaimedLockedNeverRemoveSpace: %@\ngarbageColection                  reclaimedStagedCount: %ld\ngarbageColection                  reclaimedStagedSpace: %@\ngarbageColection         reclaimedMetadataBlockedCount: %ld\ngarbageColection         reclaimedMetadataBlockedSpace: %@\n<<<]"
- "@104@0:8@16@24q32@40@48@56@64@72@80@88@96"
- "@248@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188B192@196q204q212B220@224@232@240"
- "@328@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264B272B276@280@288@296@304@312@320"
- "@48@0:8@16@24@32B40B44"
- "@48@0:8@16q24@32@40"
- "@56@0:8@16@24@32@40B48B52"
- "@68@0:8@16@24@32@40@48B56B60B64"
- "@72@0:8@16@24@32@40@48B56B60@64"
- "@80@0:8@16q24@32@40@48@56@64@72"
- "@88@0:8@16@24@32@40@48@56q64@72@80"
- "ASDateForHTTPDateString"
- "AUTO-CONTROL-MANAGER [AutoAssetVersion:%{public}@] | Initialized | bootedOSVersion:%{public}@ | bootedOBuildVersion:%{public}@"
- "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager [AutoAssetVersion:%{public}@] | ...init"
- "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager [AutoAssetVersion:%{public}@] | init..."
- "AUTO-JOB:CONFIG_DOWNLOAD"
- "AUTO-LOCKER:endLocksByClient"
- "AUTO-LOCKER:endedAllPreviousLocksByClientProcessName"
- "AUTO-SET-JOB(UserInitiatedSetDownloadNext)"
- "ActiveJobs:%ld | KnownDescriptors:%ld | Locks:%ld | Scheduled:%ld | Staged:%ld | SetConfigurations:%ld | AtomicInstances:%ld | ActiveSetDescriptors:%ld | DownloadedSetDescriptors:%ld | SetTargets:%ld | SetLookupResults:%ld"
- "Adding client: %@"
- "Adding synthetic job: %@"
- "Already subscribed to channel %@"
- "Analytics clearing on launch%@"
- "Analytics submitting on launch%@"
- "Asset %@ %@ despite appearing to be a type + assetId match for the requested asset load, did not match allowed diff %@ because its diff was %@"
- "Asset at path %@ does not support content encryption. Nothing to do"
- "Asset dir: %@ exists and is not directory, deleting"
- "Asset failed receipt check as measurements are not equal"
- "Asset failed receipt check with error %ld: %@"
- "Asset passed receipt validation"
- "Asset requires features: %@"
- "Asset requires new features - need to look for a new brain that supports these features: %@"
- "Asset that could not determine an asset ID from Info.plist: %@ in %@"
- "Asset that is being installed has different asset ID when looking at its Info.plist: %@ in %@ generates ID %@ when looking at its Info.plist."
- "Asset that is installed has different asset ID when looking at its Info.plist: %@ in %@ generates ID %@ when looking at its Info.plist."
- "Attempt to extract DAW token from response\n"
- "Attempting decryption of content encrypted asset at path %@"
- "Attempting overriding GC for: %@"
- "Attempting to set tokenPath to %@"
- "AutoDownloading"
- "AutoDownloadingAwaitGrant"
- "AutoDownloadingLookup"
- "AutoPatching"
- "AutoPatchingAwaitGrant"
- "AutoPatchingLookup"
- "AutoPersonalizing"
- "AutoPersonalizingAwaitGrant"
- "AutoPersonalizingLookup"
- "AutoTryFullAwaitGrant"
- "AutoTryFullLookup"
- "AutoTryPatchAwaitGrant"
- "AwaitGrantBoosting"
- "AwaitingBoosting"
- "AwaitingLookupBoosting"
- "B100@0:8@16B24@28q36@44@52@60@68@76q84^@92"
- "B44@0:8@16@24B32^@36"
- "B48@0:8@16q24@32^@40"
- "B64@0:8@16@24@32@40@48^@56"
- "B84@0:8@16@24B32@36@44B52B56B60B64q68@76"
- "Background updates %s allowed"
- "BoostToUserInitiated"
- "Can't extract NSError at nil key from dictionary: %@"
- "Can't grant allowlist entitlement for %lld (%@)"
- "Cancel for: %@ of %@ catalog failed due to purpose that is not well formed"
- "Cancel for: %@ of %@ id: %@ failed due to asset ID that is not well formed"
- "Cancel for: %@ of %@ id: %@ failed due to nil asset ID"
- "Cancel for: %@ of %@ id: %@ failed due to purpose that is not well formed"
- "CancelingAwaitingThree"
- "Cancelling stale background session: %@"
- "Cannot persist PMV as there is no target location for copying %@ to %@ for %@"
- "Cannot persist xml as there is no target location for copying %@ to %@ for %@"
- "Cannot write xml for %@ as control manager is nil"
- "Catalog download for: %@ got: %ld assets"
- "Catalog fileLocation: %@"
- "Channel ID is nil for identifier %@"
- "Channel Population ID: %@"
- "Channel subscriptions failed with reasons: %@"
- "Check splunk for %@ status code: %ld"
- "Cleaning up source: %@"
- "Client didn't send'update client usage with a reply context, but requested an asset path? (%lld %@: %s = %s)"
- "Config for client: %@ and descriptor: %@ failed as task could not be found"
- "Content encryption method %@ is unsupported for asset at path %@"
- "Copied %@ to %@"
- "Could not clean up malformed asset: %@"
- "Could not convert date string %@"
- "Could not create asset type from: %@. task %@"
- "Could not create reply for getInstalledAssetIds: %@"
- "Could not create target directory: %@"
- "Could not create target folder: %@,   %@"
- "Could not ensure directory %@ %@error %d"
- "Could not get asset list out of catalog for %@"
- "Could not load catalog for %@"
- "Could not make protected directory %@: %s (%d)"
- "Could not make temporary directory %@ error %d"
- "Could not move Splunk file: %@ to: %@ error: %@"
- "Could not parse the taskDescriptor of: %@. task %@"
- "Could not remove Splunk file: %@"
- "Could not subscribe to channel %@"
- "Could not unsubscribe from channel %@"
- "Could not verify signature using public key: %@"
- "Couldn't get registered channels: %@"
- "Couldn't purge asset: %@ does not exist"
- "Couldn't purge asset: %@ when first moving to: %@ due to error: %@"
- "Couldn't purge asset: %@ when removing due to error: %@"
- "Couldn't remove previous purging asset: %@ due to error: %@"
- "Created the following MAAutoAssetPushNotifications: %@"
- "Created the following push MAAutoAssetUpdatePolicy: %@"
- "Creating asset download task for: %@, %@"
- "Creating live asset download task for: %@"
- "DAW token was %s"
- "DEL_AI_CROSS_CHECK_TRIM    "
- "DEL_AI_DROP_CROSS_CHK_TRIM "
- "DEL_AI_DROP_CRSS_CHK_DESCRS"
- "DEL_SD_DROP_CRSS_CHK_DESCRS"
- "Debug"
- "Deletion of %@ failed due to: %@"
- "Discovered task: %@ new info: %@"
- "Download already started for: %@"
- "Download already started for: %@ and %@. task %@ %@ %@"
- "Download failed for: %@, could not remove temp file before starting"
- "Download failed however we are going to retry at original url: %@"
- "Download manager is nil aborting. Session %@ task %@"
- "Download manager notified of finished task: %@"
- "Download process complete for: %@, with %ld. task %@"
- "Download resumed at offset %lld bytes out of an expected %lld bytes. Session %@ task %@\n"
- "DownloadAuthorizationHeader already set in options for task (%@)"
- "DownloadAutoFull"
- "DownloadAutoPatch"
- "DownloadUserFull"
- "DownloadUserPatch"
- "DownloadedBoostingHealing"
- "DownloadedGrantBoostHealing"
- "DownloadedLookupBoostHealing"
- "Downloading in foreground: %@, removing timeout. (forced inProc: %d)"
- "DownloadingAwaitGrantBoosting"
- "DownloadingBoosting"
- "DownloadingLookupBoosting"
- "ELIMINATING_ALL_CLIENTS"
- "ERROR: Invalid string passed to %s"
- "Entitlement %@ not satisfied for connection remote object interface: %@, exported interface: %@"
- "Entitlement '%@' is not a boolean"
- "Entitlement '%@' is not an array"
- "Entitlement '%@' is not an boolean value"
- "EntryID: %@. latestDownloadedAtomicInstance is nil"
- "Error code is: %ld descriptor:%@ with %@ . task %@"
- "Error in getting JSON from the headerJson of Pallas response: %@"
- "Event %@ with uuid %@ does not exist"
- "Event payload data \"%@\" is unsupported type \"%@\". Supported Types: NSString, NSNumber, NSData, NSDate"
- "Expected query dictionary for %@"
- "FROM_STAGED"
- "Failed MAPallasFailedRetryNew and had no url on pallas for %@ client: %@"
- "Failed MAPallasFailedRetryNew but asset type does not support XML fallback. Would have attempted with: %@ after failing on pallas for %@ client: %@"
- "Failed MAPallasFailedRetryNew but client used liveServerCatalogOnly to disable XML fallback. Would have attempted with: %@ after failing on pallas for %@ client: %@"
- "Failed MAPallasFailedRetrySame but asset type does not support XML fallback. Would have attempted retry with: %@ after failing on pallas for %@ client: %@ with failure: %ld %@"
- "Failed MAPallasFailedRetrySame but client used liveServerCatalogOnly to disable XML fallback. Would have attempted retry with: %@ after failing on pallas for %@ client: %@ with failure: %ld %@"
- "Failed to acquire required SSO token for task(%@)"
- "Failed to copy %@ to %@ (missing current/target path)"
- "Failed to copy %@ to %@, error is: %@"
- "Failed to delete contentmanifest plist: %@"
- "Failed to expire task with error: %@"
- "Failed to find or update brain with new features: %@"
- "Failed to get key: %s"
- "Failed to get key: %s due to not beinng present"
- "Failed to move %@ to %@, error is: %@"
- "Failed to move asset: %@ in migration"
- "Failed to read contents of event file: %@ (%@)"
- "Failed to read directory path: %s"
- "Failed to remove %@, error is: %@"
- "Failed to remove event file %@: %@"
- "Failed to remove event file after event submission %@: %@"
- "Failed to submit task with error: %@"
- "Failed to subscribe to some channels: %@"
- "Failed with no retry on pallas for %@ client: %@"
- "FailedUserInitiated"
- "Falling back to XML. Retry with: %@ after failure on pallas for %@ client: %@ with failure: %ld %@"
- "Falling back to XML: %@ after failure before pallas response for %@ client: %@"
- "Fault"
- "For asset-type: %@ Assets array nil in xml"
- "For asset-type: %@ Could not get assets from xml"
- "For asset-type: %@ asset(s) skipped due to nil assetId during query"
- "For asset-type: %@ query was skipped due to special __Empty keyword"
- "Forcing system asset's build ID to: `%@`"
- "Forcing system asset's system image ID to: `%@`"
- "Found %@ preference override. Was not well formed, will ignore '%@' (%@)."
- "Found %@ preference override. Will force build '%@'."
- "Found %@ preference override. Will force result %ld."
- "Found a lost task download information not in correct format with info: %@ with task descriptor: %@"
- "Found download information but the NSURLSessionDownload task is nil, for task descriptor: %@"
- "Found download information from a task descriptor not in correct format with task descriptor: %@"
- "Found purpose directories to purge: %@"
- "Full URL is %@"
- "GlowD"
- "Going pallas route for %@ client: %@"
- "Got a malformed asset when reading %@, cleaning up"
- "Got a malformed asset when reading %@, cleaning up. plist: %@, infoPlistPath: %@, assetDataPath: %@"
- "Got an error trying to determine if brain has features required by asset: %@"
- "Got nil assets for getInstalledAssetIds: %@"
- "Had no fallback XML url to retry with: (nil) after failure on pallas for %@ client: %@ with failure: %ld %@"
- "Ignoring preference; key %@ has unexpected class: %@ value: '%@'"
- "In configDownload for client: %@"
- "Info plist does not exist under location %@: %@"
- "Invalid data passed to %s"
- "Invalid event data for :%@ (%@)"
- "Invalid file type found for even at path: %@ [%@] (skipping)"
- "Invalid interactivity level was passed in: %@\n"
- "Invalid options passed to %s"
- "Invalid path passed to %s"
- "Invalid range request: incomplete %@ %@"
- "Invalid range request: negative start %@ %@"
- "Invalid range request: zero length %@ %@"
- "Invalid transform, skipping: %@"
- "Invalid url passed to %s"
- "Knox lookup for decryption key %@"
- "LATEST-TO-VEND"
- "LogStatistics"
- "Lost task: %@ info: %@"
- "MA Notifying: %@"
- "MAAutoAssetControl-all-asset-specifiers"
- "MAAutoAssetControl-all-asset-types"
- "MABrainLoadFeaturesOverrides"
- "MABrainUtilityBootSessionUUID"
- "MABrainUtilityCancelDeviceUnlockAction"
- "MABrainUtilityCopyBoardId"
- "MABrainUtilityCopyCertificateSecurityMode"
- "MABrainUtilityCopyChipId"
- "MABrainUtilityCopyEcid"
- "MABrainUtilityCopySecurityDomain"
- "MABrainUtilityCopySigningFuse"
- "MABrainUtilityScheduleDeviceUnlockAction"
- "MABrainUtilityScheduleDeviceUnlockAction_block_invoke"
- "MABrainUtilityWalkDirectory"
- "MABrainUtilityWriteDictionary"
- "MADAutoSetLocker"
- "MADownloadFailed: Pallas result unknown! %ld on pallas for %@ client: %@"
- "MAPreferencesBackgroundUpdatesAllowed"
- "MAPreferencesBackgroundUpdatesAllowedForAssetType"
- "Making: %@ into a datavault"
- "Migrated"
- "Migrating assets for %@ and %@"
- "MobileAsset Simulated %{public}s: %{public}@"
- "Moved %@ to %@"
- "Moved asset: %@ in migration"
- "Moving asset to target directory: %@"
- "Moving file in didFinishDownloadingToURL, extractor: %d. Session %@ task %@ type %@ repository %@"
- "No need to clean, %@ does not exist"
- "No need to convertpath: %s is already a datavault"
- "No options specified for download config, skipping configDownload for: %@"
- "No options specified for download config, wrong class, skipping configDownload for: %@"
- "No population type ID for device!"
- "Not adding %@ to analytics payload due to invalid type"
- "Not adding %@ to analytics payload due to unallowed name"
- "Not recording event for : %@"
- "Notice"
- "NowUserInitiated"
- "Over riding url with url from pallas: %@, %@"
- "Override of asset audience due to build variable: %@"
- "PERSISTED_SET_DESCRIPTOR"
- "PMV download is being forced as client asked. Downloading %@ for %@ client: %@"
- "PMV file contents were not JSON dictionary: %@ from %@"
- "PROMOTED"
- "Pallas JWS parsing did not yield 3 elements, elements: %lu bytes: %s"
- "Pallas Server url is: %@"
- "Pallas call succeeded on pallas for %@ client: %@"
- "Pallas request creation, array element dictionary entry key:%@ holds value that is not an NSString or NSNumber | skipped"
- "Pallas request creation, invalid value for key: %@"
- "Pallas request creation, nil value skipping key: %@"
- "Pallas request creation, unknown value '%@' skipped for key: %@"
- "Pallas response contains nonce mismatch, original %@, skipping: %@"
- "Pallas response nonce: %@. Details for asset #%ld [of %ld] is: %@"
- "Pallas response nonce: %@. Total asset count: %ld. The response body is: %@"
- "Params being sent to the server are: %@"
- "PatchingAwaitGrantBoosting"
- "PatchingBoosting"
- "PatchingLookupBoosting"
- "Path %@ is not on volume %@"
- "Path %@ is on volume %@"
- "Path to asset dir: %@"
- "PersonalizingAwaitGrantBoost"
- "PersonalizingBoosting"
- "PersonalizingLookupBoosting"
- "Prior catalog could not be loaded (may not have been downloaded yet) for %@ so we will not use a Last-Modified when downloading %@"
- "Prior catalog did not have a URL string for %@ (was %@) so we will not use a Last-Modified when downloading %@"
- "Prior catalog did not have a string for %@ (was %@) so we will not use a Last-Modified when downloading %@"
- "Prior catalog did not have have a dictionary for %@ and it did not have %@ so it looks like a corrupt catalog. We will not use a Last-Modified when downloading %@"
- "Prior catalog had %@ and did not indicate %@ ... yet also did not have %@ which makes it unclear if it came from XML. We will not use a Last-Modified when downloading %@"
- "Prior catalog had %@ and said it was not %@ ... yet also did not have %@ which makes it unclear if it came from XML. We will not use a Last-Modified when downloading %@"
- "Prior catalog had %@ which matches the URL, we will attempt to use a Last-Modified when downloading %@"
- "Prior catalog had %@, so we will not use Last-Modified when downloading %@"
- "Prior catalog had a base %@ URL that matches: %@ so we will use a Last-Modified when downloading %@"
- "Prior catalog had a different %@ URL: %@ so we will not use a Last-Modified when downloading %@"
- "Prior catalog had a different base %@ URL: %@ so we will not use a Last-Modified when downloading %@"
- "Prior catalog had a non-number for %@/%@ and it did not have %@ so it looks like a corrupt Pallas catalog. We will not use a Last-Modified when downloading %@"
- "Prior catalog has no %@ or %@ or %@ or %@, so we will not use a Last-Modified when downloading %@"
- "Prior catalog has no or invalid %@ (was %@), so we will not use a Last-Modified when downloading %@"
- "Prior catalog was from Pallas: %@/%@. We will not use a Last-Modified when downloading %@"
- "REMOVE_EVENT: Event %@ does not exist. Nothing to do"
- "REMOVE_EVENT: Successfully removed event %@ from queue"
- "REMOVE_EVENTS_WITH_NAME: Removing %@"
- "Range string is: %@"
- "Received %d and nil url returned by Pallas server using: %@"
- "Received %d from pallas but url is invalid: %@ using: %@"
- "Received channel id %@ with length %tu > %tu"
- "Received notification with payload: %@"
- "Recording event for: %@"
- "Removing client: %@"
- "ReportFailBoostSetDownloadNext"
- "ReportFailureUserInitiated"
- "SET_CLIENT_REPLY|setJobInfo:%@|domain:%@|identifier:%@|jobID[%@]|clientRequest[%@]|clientReply[%@]"
- "SET_CONFIGURATION|setConfiguration:%@|setDescriptor:%@"
- "SET_EVENT: Adding CoreAnalytics event to submission queue: %@"
- "SPLUNK Failed due to writing data to file:%@ isBatch: %d with: %@"
- "SSO token does not need to be collected for this task (%@)"
- "SSO token needs to be collected for this task (%@)"
- "STAGER_PROMOTED|stagedToDownloaded:%ld|stagedSetLookupResults:%ld"
- "SUBMIT: Found event %@. Sending"
- "SUBMIT: No event found matching %@. Skipping"
- "SUBMIT_EVENTS_WITH_NAME: Submitting %@"
- "Saving event %@:%@ to %@"
- "Sending base url: %@"
- "Sending download result %ld (%@) for %@"
- "Sending download result %ld (%@) for assetType: %@ XML download did not have a catalog URL. This could be for a type where liveServerCatalogOnly was set to disable XML fallback, or a lookup error for the build of SystemApps. Would have attempted the fallback URL after skipping on pallas for %@ client: %@"
- "Sending splunk event:%@"
- "Server connection handler received unknown type: %@"
- "Server didn't return Last-Modified header on statusCode %lld for %@ download. task %@ downloaded from %@"
- "Session %@ Task completed but task was nil"
- "SetDescriptorsByInstance:%ld"
- "SetDownloadAutoFull"
- "SetDownloadAutoPatch"
- "SetDownloadUserFull"
- "SetDownloadUserPatch"
- "SetJobsByIdentifier:%ld | SetStatusByInstance:%ld"
- "Setting ifModified header to: %@"
- "Setting the time out on: %@ to: %ld due to caching server"
- "Setting the time out on: %@ to: %ld due to nil options"
- "Setting the time out on: %@ to: %ld due to options"
- "Setting the time out on: %@ to: %ld due to options specifying to use default"
- "Setting train name on DownloadManger to %@"
- "Skipping asset as it isn't a dict"
- "Skipping asset download for %@ due to preferences, giving result %ld (%@)"
- "Skipping asset: %@ as it already exists"
- "Skipping catalog download for %@ due to preferences, giving result %ld (%@)"
- "Skipping due to no downloadInfo. CFNetwork error: %@"
- "Skipping file: %@ as allData was nil"
- "Skipping file: %@ as events was nil"
- "Skipping file: %@ as we could not delete it"
- "Skipping operation to update preference %@ %@ to nil (clear) as nil is not allowed"
- "Skipping pallas route for %@ client: %@"
- "Skipping splunk for %@"
- "Skipping the move as we do not have a task description. Session %@"
- "Skipping the move due to extractor consuming bytes. Session %@ task %@"
- "Skipping: %@ not making it a datavault"
- "Skipping: %@ not making it a datavault as assetType is nil in descriptor"
- "Space check result: Not enough space to download and unarchive asset: need %llu and %llu available. error: %@"
- "Splunk report result for %@: %d, code:%ld error: %@"
- "Starting built-in MobileAsset brain built Dec 19 2024 22:16:24"
- "Starting downloaded MobileAsset brain (version: %@) built Dec 19 2024 22:16:24"
- "Submit called for event but reportingLevel does not allow sending. Skipping event: %@"
- "Submit called for events but reportingLevel does not allow sending. Skipping event name: %@"
- "Submitted event %@\n"
- "Subscribing to channel %@"
- "Subscribing to channel: %@"
- "Subscribing to platform channel %@"
- "Succeeded with not modified on pallas for %@ client: %@"
- "Successfully decrypted ContentEncrypted asset. Deleting ContentProtection plist at location %@"
- "Successfully purged asset from: %@"
- "Successfully removed event file %@"
- "Successfully retrieved response from authenticator\n"
- "Supplied purpose for download config is not well formed, skipping configDownload for: %@"
- "T@\"NSMutableDictionary\",&,N,V_downloadedSetDescriptorsByInstance"
- "T@\"NSMutableDictionary\",&,N,V_locksBySelector"
- "T@\"NSString\",&,N,V_bootedOBuildVersion"
- "Task descriptor is nil, skipping. task %@"
- "Task info is nil, skipping. task %@"
- "Task was updated but was nil, should never happen! Session %@"
- "The PMV posting date is: %@ from %@"
- "The PMV staging path is: %@ from %@"
- "The asset download options for %@ PMV were not a valid class, failing"
- "The asset download options for %@ and %@ were not a valid class, failing"
- "The asset download options for %@ catalog were not a valid class, failing: %@"
- "The attempt to create data vault failed, path: %s , mode: %o, errno: %lli"
- "The attempt to create data vault succeeded, path: %s"
- "The attempt to make data vault failed, path: %s, errno: %lli"
- "The attempt to make data vault succeeded, path: %s"
- "The background download url is: %@ and %@. task %@ options %@"
- "The base url is empty in the request, using default: %@"
- "The downloads in flight are: %@"
- "The event with uuid of: %@ exists already, keeping one with higher error count"
- "The in process download url is: %@ and %@. task %@ options %@"
- "The live asset server posting date is: %@"
- "The pallas URL doesn't contain /assets, so we cannot substitute /pmv. Falling back to static PMV: %@"
- "The pallas response %@ header is: %@"
- "The pallas response was { RequestNonce: %@ ResponseNonce: %@ code: %ld"
- "The purpose for PMV is: '%@' which is not well formed, and type is: %@"
- "The purpose for XML is: '%@' which is not well formed, and type is: %@, bailing"
- "The purpose for pallas v2 is: '%@' which is not well formed, and type is: %@"
- "The staging path is: %@ from %@ target %@"
- "The task descriptor for pallas v2 is: %@ and type is: %@"
- "The task descriptor is: %@, %ld"
- "The xml posting date is: %@ for %@ from %@"
- "There was a Pallas networking failure: %@ error: %@"
- "There was a Pallas networking failure: %@ error: %@ for the request with nonce: %@"
- "There was a Pallas networking failure: %@ statusCode: %ld"
- "TimeTravelDate '%@' is not in the correct YYYY-MM-DD format, ignoring"
- "TimeTravelDateDiff '%@' is not in the correct format (should just be numbers at max 365 and only numbers)"
- "Triggering push notification with payload: %@"
- "Trust result is failure. Unable to verify certificates are trusted. Error: %@"
- "TryFullAwaitGrantBoosting"
- "TryFullBoosting"
- "TryFullLookupBoosting"
- "TryPatchAwaitGrantBoosting"
- "TryPatchBoosting"
- "TryPatchLookupBoosting"
- "Trying to create a PMV download job while background sync is ongoing, bailing, %@"
- "Trying to create a catalog download job while background sync is ongoing, bailing, %@"
- "Trying to create a download job with nil task descriptor, bailing, %@"
- "Trying to create a download job without a well formed purpose, bailing, %@"
- "Trying to create an asset download job while background sync is ongoing, bailing, %@"
- "URL %@ requires SSO"
- "Unable to allocate log message"
- "Unable to create auto asset descriptor from asset with reason: %@ | Assuming V2 Asset."
- "Unable to create directory '%@': %@"
- "Unable to find/reconstruct stashed event for event %@ with uuid %@"
- "Unable to initialize keyed unarchiver, error: %@"
- "Unable to locate directory: %@"
- "Unable to look up client's entitlement: %@"
- "Unable to move directory from %@ to %@ with error: %@ | Errno: %s"
- "Unable to obtain decryption key: error: %@"
- "Unable to read event at %@ for submission..Removing and moving on"
- "Unable to read number of events written for assetType: %@"
- "Unable to remove event %@ : %@ : %@"
- "Unable to remove event file %@: %@"
- "Unable to remove item %@: %@"
- "Unable to save MAD analytics event(%@)"
- "Unable to set attributes for directory '%@': %@"
- "Unexpected byte string length"
- "Unexpected xpc object %@"
- "Unknown Command: %lld (%@) from client: %@"
- "Unknown Command: %lld (%@), using default command behavior of not allowing allowlist without asset type"
- "Unknown Command: %lld (not allowing the type to bypass entitlement)"
- "Unknown asset format:%@"
- "Unsubscribing from all channels: %@"
- "Unsubscribing from channel %@"
- "Usage is: %@, Override is: %f"
- "UserDownloading"
- "UserDownloadingAwaitGrant"
- "UserDownloadingLookup"
- "UserInitiatedDownloadNewestFull"
- "UserInitiatedSetDownloadNext"
- "UserPatching"
- "UserPatchingAwaitGrant"
- "UserPatchingLookup"
- "UserTryFullAwaitGrant"
- "UserTryFullLookup"
- "UserTryPatchAwaitGrant"
- "Using Knox url from asset: %@"
- "Using asset audience '%@' via selection '%@' for asset type '%@'"
- "Using auth pallas session for %@"
- "Using base url from default: %@"
- "Using base url from request: %@"
- "Using default interactivity level(0)\n"
- "Using internal server trust for %@"
- "Using legacy pallas session for %@"
- "Using train name(%s) from download manager"
- "Using train name(%s) from legacy method"
- "Value for entitlement %@ is false"
- "We have already retried this task, skipping: %@"
- "We have no info about this task, cannot reply: %@  The downloads in flight are: %@"
- "We have no info about this task, cannot retry: %@"
- "XML catalog failed as client asked for liveServerCatalogOnly to disable fallback. Would have attempted %@ after skipping on pallas for %@ client: %@"
- "XPC data error: %@ is %zu bytes, but we failed to decode"
- "XPC error connecting for didReceivePushNotificationWithInfo: %@"
- "[%@] Connection interrupted"
- "[%@] Connection invalid"
- "[%@] Received unknown event:%lld"
- "[%@] Termination imminent"
- "[%s:%d] [%s] Failed to allocate AEAExtractor/STRemoteExtractor"
- "[%s] Attempting to fetch current inflight downloads"
- "[%s] Downloading: %@"
- "[%s] No background session present for fetching inflight downloads"
- "[%s] Size of _downloadTasksInFlight: %ld"
- "[%s] Sync with NSURLSession is complete and found %lu tasks"
- "[%s] Sync with NSURLSession is not possible; in-process downloads found %lu tasks"
- "[%s] We should not have nil DownloadInfo for a task descriptor for taskDescriptor:%@, skipping."
- "[%s] We should not have nil NSUrlSessionTask for a valid DownloadInfo for taskDescriptor:%@, skipping."
- "[%{public}@]\n[CONSIDER-REMOVAL] {%{public}@} no persisted set-descriptors when should have at least setJobDescriptor:%{public}@"
- "[%{public}@]\n[CONSIDER-REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} over threshold for atomic-instances by set-identifier (unable to reduce) | setAtomicInstance:%{public}@"
- "[%{public}@]\n[CONSIDER-REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} unable to determine persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
- "[%{public}@]\n[CONSIDER-REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} unable to determine previous status | entryID:%{public}@"
- "[%{public}@]\n[DEVICE-BOOT] {ResumeJobs} no persisted known-descriptors"
- "[%{public}@]\n[DEVICE-BOOT] {ResumeJobs} unable to determine known descriptor status | entryID:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} [WARNING] over threshold for atomic-instances by set-identifier (trimming) | setAtomicInstance:%{public}@ | setDescriptor:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} atomic-instance without backing set-descriptor | entryID:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} atomic-instance without backing set-descriptor | removedOverflowAtomicInstance:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance with no asset-entries on filesystem | entryID:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} staged-now-downloaded atomic-instance without backing set-descriptor | entryID:%{public}@"
- "[%{public}@]\n[REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} unable to load set-atomic-instance | entryID:%{public}@"
- "[%{public}@] {%{public}@:_latestDownloadedDescriptor} ignoring (invalid restore version) | descriptor:%{public}@"
- "[%{public}@] {%{public}@:_latestDownloadedDescriptor} matched on downloaded | descriptor:%{public}@"
- "[%{public}@] {%{public}@:_latestDownloadedDescriptor} no match on downloaded descriptor | assetType:%{public}@, assetSpecifier:%{public}@"
- "[%{public}@] {%{public}@:_latestDownloadedDescriptor} no match on downloaded descriptor | assetType:%{public}@, assetSpecifier:%{public}@, assetVersion:%{public}@"
- "[%{public}@] {%{public}@:_routeClientRequest} [SET_CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceNewSetAtomicInstance}\n[PSUS] not trimming based on overflow | setAtomicInstance:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceNewSetAtomicInstance} not persisting sub-atomic-instance of 0 entries | setAtomicInstance:%{public}@"
- "[%{public}@] {%{public}@:atomicInstanceNewSetAtomicInstance} unable to load persisted-set-atomic-instance file | setAtomicInstance:%{public}@"
- "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [CLIENT_REQUESTS_AWAITING_SYNC] | scheduling all queued client requests"
- "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [PREVIOUSLY_QUEUED] | [schedule and] route client-request that had been awaiting first-unlock | jobParam:%{public}@"
- "[%{public}@] {%{public}@:clientRequestsAwaitingDispatchAll} [PREVIOUSLY_QUEUED] | [schedule and] route client-request | jobParam:%{public}@"
- "[%{public}@] {%{public}@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} [CLIENT_REQUESTS_AWAITING_SYNC] | moved client-request to awaiting first-unlock | jobParam:%{public}@"
- "[%{public}@] {%{public}@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} [PREVIOUSLY_QUEUED] | [schedule and] route client-request | jobParam:%{public}@"
- "[%{public}@] {%{public}@:handleSetClientAlterEntriesRepresentingAtomicRequest} unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
- "[%{public}@] {%{public}@:removeSetDescriptorDownloaded} no latest downloaded atomic-instance | setDescriptor:%{public}@"
- "[%{public}@] {%{public}@:removeSetDescriptorDownloaded} unable to load persisted-set-descriptor file | downloadedSetDescriptor:%{public}@"
- "[%{public}@] {%{public}@}\n[LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "[%{public}@] {_routeClientRequest}\n[CANCEL-SET-JOB] active set-job being canceled - not considering as active job | set-eventInfo:%{public}@"
- "[%{public}@] {jobDescriptorOnFilesystemValidated} asset file does not exist | jobDescriptor:%{public}@, localURLForDescriptor:%{public}@"
- "[%{public}@] {loadPersistedCrossCheckTrim} just unlocked selectors:%ld"
- "[%{public}@] {loadPersistedCrossCheckTrim} no selectors just unlocked"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor has no downloaded asset - dropped | setDescriptor:%{public}@"
- "[%{public}@] {loadPersistedSetDownloadedDescriptors} staged-now-promoted set-descriptor validated | entryID:%{public}@, adoptedSetDescriptor[fromStaged]:%{public}@"
- "[%{public}@] {loadPersistedSetLookupResults} no persisted set-lookup-results to be resumed"
- "[%{public}@] {loadPersistedSetLookupResults} unable to determine previous status | entryID:%{public}@"
- "[%{public}@] {locateSetDescriptorDownloadedPreferringByAtomicInstance}\n[VEND] new set-descriptor generated from staged set-descriptor | setConfiguration:%{public}@, fromStagedSetDescriptor:%{public}@"
- "[%{public}@] {locateSetDescriptorDownloadedPreferringByAtomicInstance} located descriptor not fully downloaded | locatedDownloadedSetDescriptor:%{public}@"
- "[%{public}@] {locateSetLookupResultSatisfying} unable to determine previous status | entryID:%{public}@"
- "[%{public}@] {locateSetLookupResultSatisfying} unable to load set-lookup-result | entryID:%{public}@"
- "[%{public}@] {setDescriptorDownloadedLoadedFromPersisted} downloaded-by-instance set-descriptor already known | setDescriptor:%{public}@"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|latestToVend:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,UUID:%@,Sub:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[ANALYTICS] {recordEventWithName} Automatically submitting event due to reportingLevel being immediate. eventName: %@"
- "[ANALYTICS] {recordEventWithName} Could not extract Event from payload:%@ and eventName:%@"
- "[AUTO-ASSET] [LOCAL-CONTENT-URL] {handleClientAlterLockOperation} failure to perform alter lock operation - %{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledAtomicInstanceDescriptors} encountered blank auto-asset-descriptor - removing | entryID:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledAtomicInstanceDescriptors} unable to determine previous status | entryID:%{public}@"
- "[AUTO-PRE-INSTALLED] {_preInstalledAtomicInstanceDescriptors} unable to load auto-asset-descriptor | entryID:%{public}@"
- "[AUTO-SHORT-TERM][FILE]{_shortTermPersistSetStatus} created SHORT-TERM atomic-instance file | filename:%{public}@ | setDescriptor:%{public}@ | setStatus:%{public}@ "
- "[AUTO-SHORT-TERM][LATEST]{%{public}@} latest removed when older supporting SHORT-TERM locking | atomicInstance:%{public}@ | otherSetDescriptor:%{public}@"
- "[AuthenticatedPallas]: Invalid url passed to %s"
- "[AuthenticatedPallas]: Pallas server(%@) does *NOT* require authentication"
- "[AuthenticatedPallas]: Pallas server(%@) requires authentication"
- "[AuthenticatedPallas]: URL %@ supports authenticated pallas"
- "[AuthenticatedPallas]: {urlSupportsAuthenticatedPallas} Adding %@ to set of domains supporting authenticated pallas"
- "[CoreAnalytics] SUBMIT: Calling SendEventLazy for %@"
- "[CoreAnalytics] SUBMIT: NO -- Unable to invoke CoreAnalytics on this OS for event %@"
- "[CoreAnalytics] SUBMIT: YES -- Submitting CoreAnalytics event: %@"
- "[CoreAnalytics]: SUBMIT_ALL_EVENT: Sending event %@"
- "[GARBAGE_COLLECTION] {finishAllPartiallyPurgedAssets} %@ | checking for purged assets at path:%@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%@), volume:%@, targeting:%@ | ...respondToCacheDelete | reclaimed:%@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeCallbackForVolume} reclaiming space | urgency:%d(%@), volume:%@, targeting:%@ | respondToCacheDelete..."
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%@), volume:%@ | ...respondToCacheDelete | reclaimable:%@"
- "[GARBAGE_COLLECTION] {handleCacheDeletePurgeableCallbackForVolume} determining reclaimable space | urgency:%d(%@), volume:%@ | respondToCacheDelete..."
- "[GARBAGE_COLLECTION] {performCacheDeleteCollection} %@ | number of assets and GC types for those corresponding assets don't match | assetCount: %ld | assetGCTypesCount: %ld"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | failed to remove old asset content | asset:%@ | gapDuration:%@, removalThreshold:%@ | result:%lld(%@)"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | old asset content did not exist | asset:%@ | gapDuration:%@, removalThreshold:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | removed old asset content | asset:%@ | gapDuration:%@, removalThreshold:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | setting client usage as it was not set | asset:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | skipping due to policy of never collect | asset:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | will not delete (%@) | asset:%@ | gapDuration:%@, removalThreshold:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | will not delete (never remove) | asset:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} %@ | will not delete (recent client interest) | asset:%@ | gapDuration:%@, removalThreshold:%@"
- "[GARBAGE_COLLECTION] {performGarbageCollectionOfType} Could not read asset attributes from assetDirectory(asset could be non-existent): %@, skipping asset."
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine content modification date, continuing anyway | URL:%@ | error:%@\n%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not determine creation date, continuing anyway | URL:%@ | error:%@\n%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} could not remove old in-flight download tracking file (not in-flight) | URL:%@ | result:%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} dir:%@ | referenceDateForRecent:%@ | tasksInFlight:%ld"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} error determining contents of directory:%@ | error:%@\n%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} failed to determine contents of directory:%@ | error:%@\n%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} removed old in-flight download tracking file (not in-flight) | URL:%@"
- "[GARBAGE_COLLECTION] {removeDownloadsNotRecentlyInFlight} skipping %@ since it was modified before %@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} Using Cache Delete Results: %@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} Volume: %@ | Urgency: %d | Operation: %hhu | | reportingLevel %@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection (no asset-type directories, volume reported by cache delete might be invalid) | targetingPurgeAmount:%@ | urgency:%d(%@) | volume:%@"
- "[GARBAGE_COLLECTION] {respondToCacheDelete} skipping garbage collection | targetingPurgeAmount:%@ | urgency:%d(%@) | volume:%@ | current time is not valid | currentTimeInSeconds:%f, numberOfSecondsInAYear:%llu"
- "[GROUP][fromOS:%@,fromBuild:%@,targetOS:%@,targetBuild:%@|targetTrain:%@|targetRestoreVersion:%@|determineRequests:%ld|downloadRequest:%@(chosen:%@,usingGroups:%@,OnceRequired:%@)|activeDescriptor:%@|candidates:(R:%ld,O:%ld,a:%ld),determining:%ld,available:(R:%ld,O:%ld,a:%ld)|awaitingStaging:%ld|staged:%ld|elimination:%ld,eliminationAck:%ld]"
- "[MAB] %s"
- "[MA_PREFS] Read preference from: %@ for: %@ value: `%@` (%@)"
- "[MA_PREFS] {%@} [%@] Could not synchronize preferences for %@ - this may be a permissions error"
- "[MA_PREFS] {%@} [%@] Synchronized preferences for %@"
- "[MA_PREFS] {%@} [%@] nil preference key provided"
- "[MA_PREFS] {%@} [%@] | Completed operation to update preference %@ %@ to data"
- "[MA_PREFS] {%@} [%@] | Completed operation to update preference %@ %@ to nil (clear)"
- "[MA_PREFS] {%@} [%@] | attemptsMade:%d | Unable to synchronize after setting preference %@ %@ to data"
- "[MA_PREFS] {%@} [%@] | attemptsMade:%d | Unable to synchronize after setting preference %@ %@ to nil (clear)"
- "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number"
- "[MA_PREFS] {_MAPreferencesCopyArrayOfNumbers} invalid entry for key:%@ | value:%@ | index:%d | not a number (from string)"
- "[MA_PREFS] {_MAPreferencesCopyNSArrayOfNumbersValue} invalid type for key:%@ | expecting array of numbers"
- "[MA_PREFS] {_MAPreferencesCopyNSDataValue} invalid type for key:%@ | expecting data"
- "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%@ | expecting string or number or boolean"
- "[MORE_CLIENT_REQUESTS] {%{public}@:removeCurrentSetJob} set-job indicated removal but has more to do | eventInfo:%{public}@"
- "[MobileAssetHealthReport]: Submitting health report %{public}@"
- "[SMA] %s"
- "[SPACE] checked space on %@.  Free space available: %llu"
- "[SU_PREFS] Background download allowed: %@  automaticCheckEnabled: %@ dataInstall: %@"
- "[SU_PREFS] Background updates are %@"
- "[SU_PREFS] Read preference from: %@ for key: %@ with no match and using default value: %@"
- "[SU_PREFS] Read preference from: %@ for key: %@ with value: %@"
- "[clientName:%@|SubAtomic:%@|(creation)Date:%@,Index:%ld|entries:%ld|setJob:%@|(status)newerAvailable:%@,allDownloaded:%@|shortTerm:%@|(awiating)NewerFound:%@,Altered:%@]"
- "[clientName:%@|setEntries:%ld|latestToVend:%@|inhibitScheduling:%@|lookupRsp:%@|vendingforConfig:%@]"
- "[interestInContent:%lld,checkForNewer:%lld,determineIfAvailable:%lld,currentStatus:%lld,lockContent:%lld,mapLockedContent:%lld,continueLockUsage:%lld,endLockUsage:%lld,endPreviousLocks:%lld,endAllPreviousLocks:%lld|eliminateAllForSelector:%lld|eliminateAllForAssetType:%lld|eliminatePromotedNeverLockedForSelector:%lld|stageDetermineAllAvailable:%lld,stageDownloadAll:%lld,stagePurgeAll:%lld,stageEraseAll:%lld]"
- "^\\d{3}$"
- "_MAPreferencesCopyArrayOfNumbers"
- "_MAPreferencesCopyNSArrayOfNumbersValue"
- "_MAPreferencesCopyNSDataValue"
- "_MAPreferencesCopyNSStringValue"
- "_MAPreferencesCopyValue"
- "_MAPreferencesSetDataValue"
- "_MAPreferencesSetDataValue_block_invoke"
- "_MAPreferencesSetKeyForValue"
- "_MAPreferencesSetStringValue"
- "_MAPreferencesSetStringValue_block_invoke"
- "_MAPreferencesSetValues"
- "_MAPreferencesSetValues_block_invoke"
- "_MobileAssetCheckConnectionEntitlementWithName"
- "_MobileAssetCreateDirectoryWorldWriteable"
- "_MobileAssetDecryptAndVerifySignature"
- "_MobileAssetVerifyAssetMapSignature"
- "_MobileAssetVerifyDevelopmentSigning"
- "_MobileAssetVerifyStrongSigning"
- "_SUBoolPreferenceValue_block_invoke"
- "_acceptStagingClientRequest:fromLocation:"
- "_bootedOBuildVersion"
- "_checkBooleanEntitlement"
- "_clearAtomicInstanceFromLatestToVend:fromLocation:"
- "_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:"
- "_copy_value_from_IONode"
- "_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:"
- "_downloadedSetDescriptorsByInstance"
- "_eliminateAtomicTriggeredWhileLoading"
- "_endLocksByClient"
- "_endLocksByClient:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:"
- "_endLocksByClient:forAssetSelector:forLockReason:removingLockCount:endError:"
- "_hashCFArrayLegacy"
- "_hashCFDataOfLength"
- "_hashCFStringOfLength"
- "_haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:"
- "_haveReceivedLookupResponseForSetDescriptor:"
- "_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:"
- "_locksBySelector"
- "_logPersistedConfigLoad:lastStagingFromOSVersion:lastStagingFromBuildVersion:assetTargetOSVersion:assetTargetBuildVersion:usingModeByGroups:candidateAssetCount:determinedAvailableAssetCount:activelyStagingAssetCount:awaitingStagingAssetCount:stagedAssetCount:stagedAssetTotalContentBytes:message:"
- "_logPersistedSetLookupResultTableOfContents:"
- "_mabrainbundle_log"
- "_newAtomicEntryIDsOtherThanDescriptor:"
- "_persistAssetLock:operation:forAssetLock:message:"
- "_preInstalledAtomicInstanceDescriptors"
- "_removeAssetLock"
- "_removeAssetLock:lastClient:forSelector:message:"
- "_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:"
- "_replyHaveStagedContent:"
- "_replyNoCandidates"
- "_securemobileassetbundle_log"
- "_targetPath"
- "_vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:"
- "_vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:"
- "action_BoostToUserInitiated:error:"
- "action_LogStatistics:error:"
- "action_NowUserInitiated:error:"
- "action_ReportFailBoostSetDownloadNext:error:"
- "action_ReportFailureUserInitiated:error:"
- "action_UserInitiatedDownloadNewestFull:error:"
- "action_UserInitiatedSetDownloadNext:error:"
- "addAdditionalParams"
- "addToCurrentJobs:usingSelector:withJobUUID:triggeredByClientMessage:downloadingDescriptor:baseForPatchDescriptor:usingSetDescriptor:"
- "adding event %@"
- "additionalLockedByClient:forAssetSelector:forLockReason:withUsagePolicy:lockError:"
- "applyTransforms:toAssets:"
- "assembleTaskDescriptorWithPurposeAndAutoAssetJobID"
- "asset set id for %@ from server is: %@"
- "assetConfigJobFinished:error:"
- "assetExistsAndIsValidWithPurpose"
- "assetType: %@"
- "assetType: %@ asset: %@"
- "assetType: %@ client: %@, command: %lld (%@)"
- "assetTypes: %@ client: %@, command: %lld (%@)"
- "atomic-instance shared lock atomic-instance (eliminated set-identifier)"
- "atomic-instance symlink file (to re-attempt symlink on standard-unlock of newest)"
- "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:recoveringAtomicInstanceUUID:asSubAtomicFrom:"
- "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:forSetInfoInstance:asSubAtomicFrom:"
- "atomicInstanceNewSetAtomicInstance:recordingHistoryOperation:recoveringForSetDescriptor:usingAsSetClient:"
- "autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:"
- "backgroundDownloadsPossible: 1 %@"
- "backgroundDownloadsPossibleWithInfo"
- "bootedOBuildVersion"
- "calculateTimeout"
- "cannot accept ended locks when no existing lock for auto-specific-asset"
- "check filesystem for available space failed (unable to determine volume name from path=%@)"
- "check for available space failed (error reported by cache delete for path=%@)"
- "check for available space failed (unable to determine available space through cache delete for path=%@)"
- "checkAtomic (NO_WAIT) requested when no latest atomic-instance to vend (and failed to locate set-descriptor satisfying [or build from pre-SU-staged]) (and not pre-installed)"
- "checkConnectionAccessToAssetType"
- "checkSpaceForDownload"
- "chooseNewerSetDescriptor:considering:"
- "chooseNewerSetStatus:comparingTo:"
- "cleanV1Assets"
- "client %@ requested data migration. No DataMigrator work was needed."
- "client %@ requested data vault for %@"
- "client %@ requested data vault for %@, it failed with status: %ld"
- "client %@ requested data vault for %@, it succeeded"
- "client: %@ requested reporting %@"
- "com.apple.SoftwareUpdateSSO"
- "configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadConfig:forAutoAssetName:"
- "considerSetDescriptorsForLatestToVend"
- "copyOfSetLocksByDescriptor"
- "copySsoToken"
- "copySsoToken_block_invoke"
- "copyTargetToDirectory"
- "could not load PMV JSON after download: %@ from %@"
- "could not load PMV JSON after download: %@ from %@ error %@"
- "could not load PMV file after download: %@ from %@"
- "could not load xml file after download: %@ from %@.  Error: %@"
- "createExtension"
- "dataFillInstalledWithPurpose"
- "decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:"
- "discretionary:%@, timeout:%@ | assetId:%@ | decrypt:%@, source:%@"
- "doesSetDescriptor:satisfyAllAutoAssetEntries:"
- "download of the auto-asset content could begin (download postponed [scheduled])"
- "downloaded set-descriptor no longer referencing content on the filesystem (newer exists)"
- "downloadedSetDescriptorsByInstance"
- "dumpClientUsage for client: %@"
- "eject"
- "endedAllPreviousLocksByClientProcessName:withClientProcessID:forAssetSelector:endError:"
- "ensureAndIncrementNumberAtKey"
- "ensureAssetDirectory"
- "ensureDirectory"
- "failed end of lock of auto-specific-asset"
- "failed entitlement check for: %@ with %d for command: %lld (%@)"
- "failed entitlement check for: %@ with MalformedAssetType for command: %lld (%@)"
- "failed entitlement check for: %lld %@"
- "failed entitlement check for: nil asset type for command: %lld (%@)"
- "failed entitlement check for: one %lld %@"
- "failed lock continuation of auto-specific-asset"
- "failed to end all locks of auto-specific-asset (for client-specified criteria)"
- "failed to end previous locks of auto-specific-asset (for client-specified criteria)"
- "failure to perform alter lock operation"
- "fileHandleWithStandardOutput"
- "finishAllPartiallyPurgedAssets"
- "finishPartiallyPurgedAssets"
- "forceGlobalUnlock:"
- "getAssetsFromXml"
- "getAutoLocalUrlFromTypeAndIdGivenDefaultRepoWithPurpose"
- "getAutoLocalUrlFromTypeGivenDefaultRepoWithPurpose"
- "getHealthReport"
- "getInstalledAssetIds result is %ld for:%@"
- "getLocalUrlFromTypeAndIdGivenDefaultRepoWithPurpose"
- "getObjectFromMessage: could not decode object for key: %s error: %@"
- "getObjectFromMessageLogIfDesired"
- "getPathToAssetWithPurpose"
- "getPmvUrl"
- "getRepositoryDownloadsUrl"
- "getStandardUrl"
- "handleCacheDeletePurgeCallbackForVolume"
- "handleCacheDeletePurgeCallbackForVolume_block_invoke"
- "handleCacheDeletePurgeableCallbackForVolume"
- "handleCacheDeletePurgeableCallbackForVolume_block_invoke"
- "handleClientAlterLockOperation(END_ALL_PREVIOUS_LOCKS)"
- "handleClientAlterLockOperation(END_LOCK_USAGE)"
- "handleClientAlterLockOperation(END_PREVIOUS_LOCKS)"
- "handleDownloadConfigJobFinished:configError:"
- "handleGetInstalledAssetIds"
- "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:"
- "handleSetClientEliminateAtomicRequest:forAutoJob:"
- "handleSetClientNeedForAtomicRequest"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAtomicInstanceUUID:asSubAtomicFrom:originallyCreatedOnDate:withCreationIndex:representingInstanceEntries:inUseBySetJob:"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
- "initForConfigFinishedJobID:withError:"
- "initForSetConfiguration:withSetDescriptor:"
- "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "initWithPromoted:withSetLookupResults:"
- "invalid set-eventInfo (no set-identifier to be altered) | set-eventInfo:%@"
- "isDescriptorManagedAsSet:"
- "isForcedBuildPreferenceSetForAssetType"
- "isForcedResultPreferenceSetForAssetType"
- "isPathOnVolume"
- "isSSONeededForURL_block_invoke"
- "isWellFormedTokenFileName"
- "loadPersistedCrossCheckTrim"
- "loadPersistedCrossCheckTrimAtomicInstances"
- "loadPersistedCrossCheckTrimSetDescriptors"
- "loadPersistedSetDescriptorAsLatestToVend"
- "loaded configuration to determine whether any stager operation had been in progress"
- "locateLocksCurrentLocksCount"
- "locateSetDescriptorDownloadedByAtomicInstanceUUID:"
- "locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:consideringPreviouslyStaged:"
- "locateSetDescriptorDownloadedByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:consideringPreviouslyStaged:"
- "locateSetDescriptorDownloadedLatest:forAssetSetIdentifier:"
- "locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:forSetConfiguration:requestedAutoAssetEntries:performingNoWait:creatingIfPreviouslyStagedFound:fromLocation:"
- "locateSetDescriptorDownloadedPreferringByAtomicInstance:elseByClientDomain:forAssetSetIdentifier:fromLocation:"
- "lockedByClient:forAssetSetIdentifier:forAtomicInstance:forLockReason:withUsagePolicy:lockError:"
- "locks not ended (missing required) | clientProcessName:%@, selector:%@"
- "locks not ended (selector missing asset-version) | clientProcessName:%@, selector:%@"
- "lookupBootedBuildVersion"
- "lookupBootedOSVersion"
- "makeDataVaultAtUrl"
- "message (%@) called without userInfo"
- "mobileassetd_main"
- "mountPointForPath"
- "moveTargetURLToDirectory"
- "new set-lookup-result | setLookupResult:%@"
- "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
- "no global entitlement found, command %lld (%@) allows asset-type specific entitlement."
- "no global entitlement found, command %lld (%@) requires asset-type specific entitlement for type not on allowlist. status: %d"
- "no next specifier to download (at location UserInitiatedSetDownloadNext)"
- "orphanedProcessLifeLocks:"
- "overrideGCValue for: %@ cannot proceed with purpose that isn't well formed"
- "overrideGCValue for: %@ could not determine path to asset, skipping"
- "overrideGCValue for: %@ failed due to asset id not being well formed"
- "overrideGCValue for: %@ failed due to nil asset id"
- "overrideGCValue for: %@ path:%@, days:%lld"
- "passed entitlement check for: one %lld %@"
- "persistSetJobDescriptor"
- "persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:"
- "postSetNotificationName:forAssetSetIdentifier:fromModule:fromLocation:"
- "preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:"
- "preInstalledSetDescriptorForSetInstance:dueToMessageName:fromLocation:"
- "previous MA daemon execution was running version prior to having support for set-lookup-results"
- "purging all asset types in list: %@"
- "queryNSUrlSessiondAndUpdateState complete, _downloadStateQueue resumed _downloadTasksInFlight: %@"
- "received MA_DUMP_CODE_COVERAGE [deprecated] from client %@"
- "received command from client %@ that should be handled by MA XPC layer: %lld (%@)"
- "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
- "recordMobileAssetPromotionAttempt:assetType:assetVersion:osPromotion:successfullyPromoted:"
- "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
- "refreshDownloadedToManager"
- "refreshSetFoundToManager"
- "refreshSetFoundToManager:"
- "removeAllObsoletedV1Assets Checking: %@ for V1 Assets"
- "removeAllObsoletedV1Assets Skipping: %@ not removing its V1 assets"
- "removeAllObsoletedV1Assets Skipping: %@ not removing its V1 assets as assetType is nil in descriptor"
- "removeDownloadsNotRecentlyInFlight"
- "removeItem"
- "removeSetDescriptorDownloaded"
- "removeShortTermLockingOfSetDescriptor:forSetDescriptor:endingAll:error:"
- "removed previously downloaded set-descriptor | setDescriptor:%@"
- "renameWithExtThenRemove"
- "reportSetCatalogDecideFound"
- "reportSetCatalogDecideFound:"
- "reporting download attempt %@"
- "request DownloadManager configuration change to discretionary | downloadAssetDescriptor:%@"
- "resumeJobs"
- "returnXml Encoding error: %@"
- "secureCheckProcessLifeLocks"
- "secureCheckProcessLifeLocks:"
- "secureForceUngraftAll:forSetDescriptorBeingRemoved:"
- "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:"
- "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:"
- "set-configuration is nil while trying to update LATEST-TO-VEND to existing atomic-instance:\n %@\nAll known setConfigurations are: %@"
- "set-job indicating issue-reply when no tracked client-requests | eventInfo:%@"
- "setAtomicInstanceForUUID:fromSetAtomicInstances:"
- "setBootedOBuildVersion:"
- "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:"
- "setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:"
- "setDescriptorDownloadedLoadedFromPersisted"
- "setDescriptorDownloadedLoadedFromPersisted:persistedEntryID:"
- "setDownloadedSetDescriptorsByInstance:"
- "setLocksBySelector:"
- "setValue"
- "setupMemoryPressureMonitor"
- "setupMemoryPressureMonitor_block_invoke"
- "sharedLogger"
- "shortTermLockSetDescriptor:forSetDescriptor:"
- "sloadPersistedCrossCheckTrim"
- "splitOutAvailableForStagingByGroup:"
- "stager has provided set-lookup-results for OS just booteed into - clearing now-stale entries"
- "stagerResumed:withSetLookupResults:"
- "statfs failed for %s : %lld (%s)"
- "successful end of all previous locks of auto-specific-asset (yet still other lock[s])"
- "successful end of lock of auto-specific-asset (last lock ended)"
- "successful end of lock of auto-specific-asset (still other lock[s])"
- "successful end of previous locks of auto-specific-asset (last lock ended)"
- "successful end of previous locks of auto-specific-asset (still other lock[s])"
- "successful lock continuation of auto-specific-asset (that was previously locked)"
- "supportedAssetFormatsArray_block_invoke"
- "syncPreferences"
- "task: %@ completed with no response. task %@"
- "taskFinishedUpdateState:with:"
- "taskFinishedUpdateState:with:extraInfo:"
- "the default/fallback url is not valid when the asset type is nil: '%@'"
- "the server url is not valid: '%@'"
- "time=%@ op=%@ %@=%@ %@ asset=%@ selector=%@%@%@"
- "time=%@ op=%@ %@=%@ %@ asset=%@%@%@"
- "time=%@ op=%@ %@=%@ %@ domain=%@%@"
- "time=%@ op=%@ %@=%@ %@ id-%@ set=%@ domain=%@%@"
- "time=%@ op=%@ %@=%@ %@ id=%@ domain=%@%@"
- "time=%@ op=%@ %@=%@ %@ id=%@ domain=%@%@%@"
- "time=%@ op=%@ %@=%@ %@ id=%@ set=%@ domain=%@%@"
- "time=%@ op=%@ %@=%@ %@ id=%@ set=%@ domain=%@%@%@"
- "time=%@ op=%@ %@=%@ %@ id=%@ set=%@%@%@"
- "time=%@ op=%@ %@=%@ %@%@"
- "time=%@ op=%@ %@=%@ %@%@%@"
- "time=%@ op=%@ %@=%@ asset=%@ selector=%@%@"
- "time=%@ op=%@ %@=%@ asset=%@%@"
- "time=%@ op=%@ %@=%@ count=%004ld asset=%@ selector=%@%@"
- "time=%@ op=%@ %@=%@ count=%004ld asset=%@%@"
- "time=%@ op=%@ %@=%@ count=%004ld%@"
- "time=%@ op=%@ %@=%@ domain=%@ set=%@ asset=%@ selector=%@%@"
- "time=%@ op=%@ %@=%@ domain=%@ set=%@ asset=%@%@"
- "time=%@ op=%@ %@=%@ domain=%@ set=%@ selector=%@%@"
- "time=%@ op=%@ %@=%@ domain=%@ set=%@%@"
- "time=%@ op=%@ %@=%@%@"
- "trackDescriptor:persisting:fromLocation:changedWhileTerminated:changedNeverBeenLocked:historyOperation:firstClientName:"
- "trackSetDescriptor:fromLocation:forLatestDownloaded:forSpecificAtomicInstance:withCurrentSetStatus:changedWhileTerminated:changedNeverBeenLocked:notifyingIfJustDownloaded:latestToVend:historyOperation:firstClientName:"
- "trackShortTermLockedSetDescriptor:"
- "unable to create NSURL from path: %@"
- "unable to create SHORT-TERM lock atomic-instance file | filename:%@ | setDescriptor:%@"
- "unknown auto-asset command request received"
- "unknown auto-asset lock manipulation command request received"
- "updateClientUsageDate"
- "updateGCOverride"
- "urlSupportsAuthenticatedPallas_block_invoke"
- "userInitiated|"
- "v116@0:8@16@24@32@40@48B56Q60Q68Q76Q84Q92Q100@108"
- "v144@0:8q16q24@32q40@48@56q64q72q80q88q96@104@112@120@128@136"
- "v44@0:8@16@24B32q36"
- "v52@0:8@16@24@32B40@?44"
- "v60@0:8@16B24@28B36B40q44@52"
- "writeData:"
- "writeJsonDictionaryToFile %@ could not move json from: %@ to: %@ error: %@"
- "writeJsonDictionaryToFile %@ could not move old file: %@ to: %@ error: %@"
- "writeJsonDictionaryToFile %@ could not remove file: %@ (after initial error moving it to: %@) with removal error: %@"
- "writeJsonDictionaryToFile %@ could not remove file: %@ error: %@"
- "writeJsonDictionaryToFile %@ could not remove prior archive file: %@ (will continue) error: %@"
- "writeJsonDictionaryToFile %@ could not remove prior temp file: %@ (will fall back to directly writing) error: %@"
- "writeJsonDictionaryToFile %@ failed to create json stream: %@"
- "writeJsonDictionaryToFile %@ failed to write json to: %@ error: %@"
- "writeJsonDictionaryToFile %@ moved existing file: %@ to: %@"
- "writeJsonDictionaryToFile %@ notifying download manager move complete"
- "writeJsonDictionaryToFile %@ removed existing file: %@"
- "writeJsonDictionaryToFile %@ removed existing file: %@ (after initial error moving it to: %@)"
- "writeJsonDictionaryToFile %@ succeeded"
- "xml file contents were not a dictionary: %@ from %@"
- "xml file failed signature check: %@ from %@"
- "{%@:_logPersistedTableOfContents} second component type check - unknown componentType:%@"
- "{%@:_logPersistedTableOfContents} third component type check - unknown componentType:%@"
- "{%@:_logPersistedTableOfContents} unknown componentType:%@"
- "{%@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} | invalid eventInfo (instance:MISSING) | eventInfo:%@"
- "{%@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} | invalid set-eventInfo (instance:MISSING) | set-eventInfo:%@"
- "{%@:clientRequestsAwaitingSyncToAwaitingFirstUnlock} | nil jobParam on clientRequestsAwaitingSync"
- "{%@:removeActiveJobForFullSelector} | no persistedEntryID for fullSelector:%@"
- "{%@:removeActiveJobForFullSelector} | no persistedEntryID for noVersionSelector:%@"
- "{%@:updateAutoAssetStatus} no jobPersistedState | persistedEntryID:%@"
- "{%@:updateAutoAssetStatus} no progress status"
- "{%@:verifySetDescriptorIsLockable} no downloaded atomic-instance entries | setJobDescriptor:%@"
- "{%@} atomic-instance entry no longer on the filesystem | nextAtomicEntry:%@| setDescriptor:%@"
- "{%@} unable to locate asset-descriptor for atomic-instance entry | nextAtomicEntry:%@| setDescriptor:%@"
- "{%{publci}@}\n[LATEST-TO-VEND] just committed all pre-personalized secure | setDescriptor:%{public}@"
- "{%{public}@:_logPersistedSetLookupResultTableOfContents} | (%{public}@) %{public}@ | unable to load entry:%{public}@"
- "{%{public}@:removeSetTargetsForClientDomain} | no set-taget entry found for entry:%{public}@"
- "{%{public}@:removeSetTargetsForClientDomain} | unable to determine previous set-target for entry:%{public}@"
- "{%{public}@:removeSetTargetsForClientDomain} | unable to re-load set-target for entry:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] [NO_CHANGE] atomic-instance entry requiring personalization | nextAtomicEntry:%{public}@ | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] [NO_CHANGE] no asset-versions are available to the client | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] cleared set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] not setting latestAtomicInstanceToVend (requiresPersonalization) | setJobDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] replaced what had been latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] update to set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{%{public}@}\n[SELF-HEAL] deduped setDescriptor:%{public}@"
- "{%{public}@} check-atomic found newer and latest - newer does not satisfy current set-configuration | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} check-atomic found newer and latest - newer not from PSUS (vending latest) | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} check-atomic found newer(PSUS) and latest - unable to create from PSUS (vending latest) | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} check-atomic found newer(PSUS) and latest - vending new from PSUS | chosenDownloadedSetDescriptor:%{public}@"
- "{%{public}@} lock-atomic found newer (not awaiting any secure operation) | chosenDownloadedSetDescriptor:%{public}@"
- "{%{public}@} lock-atomic found newer and latest - newer does not satisfy current set-configuration | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} lock-atomic found newer and latest - newer not from PSUS (vending latest) | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} lock-atomic found newer(PSUS) and latest - unable to create from PSUS (vending latest) | newerDownloadedSetDescriptor:%{public}@"
- "{%{public}@} lock-atomic found newer(PSUS) and latest - vending new from PSUS | chosenDownloadedSetDescriptor:%{public}@"
- "{%{public}@}Determining atomic-instance to use for (NO_WAIT). setConfig:%{public}@"
- "{AUTO-LOCKER:%{public}@:_persistAssetLock} | unable to record lock (no persisted-state) for selector:%{public}@"
- "{AUTO-LOCKER:%{public}@:_persistRemoveAssetLock} | unable to remove lock tracker (no persisted-state) for selector:%{public}@"
- "{AUTO-LOCKER:_endAllSetLocksNoLongerTracked} | unable to end auto-asset all-locks not tracked in sets | untrackedLock:%{public}@ |  endedLocksAutoAssetError:%{public}@"
- "{AUTO-LOCKER:_endAllSetLocks} | unable to end auto-asset all-locks for set-identifier | orphanedLock:%{public}@ |  endedLocksAutoAssetError:%{public}@"
- "{AUTO-LOCKER:_endLocksByClient} failed end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@ | error:%{public}@"
- "{AUTO-LOCKER:_endLocksByClient} successful end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@, ended locks:%ld"
- "{AUTO-LOCKER:_isUntrackedSetAssetLock} | untracked set-asset-lock | assetLock:%{public}@"
- "{AUTO-LOCKER:continuedSetLockByClient} | unable to continue auto-asset lock of the set | setAtomicEntry:%{public}@ | continueError:%{public}@"
- "{AUTO-LOCKER:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed to drop stale lock | dropFromAssetLock:%{public}@, dropLockTracker:%{public}@ | error:%{public}@"
- "{AUTO-LOCKER:eliminateAllPreviousSetLocksByClient} | unable to end auto-asset all-lock for the set | lockedSetDescriptor:%{public}@ | nextEntry:%{public}@ | endedLocksAutoAssetError:%{public}@"
- "{AUTO-LOCKER:endedAllPreviousLocksByClientProcessName} failed end-all-locks | clientProcessName:%{public}@, selector:%{public}@ | error:%{public}@"
- "{AUTO-LOCKER:endedAllPreviousLocksByClientProcessName} successful end-all-locks | clientProcessName:%{public}@, selector:%{public}@"
- "{AUTO-LOCKER:endedPreviousSetLocksByClient} | unable to end auto-asset lock-count of the set | setAtomicEntry:%{public}@ | endedLocksAutoAssetError:%{public}@"
- "{AUTO-LOCKER:lockedSetByClient} | unable to end auto-asset lock after failure to lock entire set | setAtomicEntry:%{public}@ | endLockError:%{public}@"
- "{AUTO-LOCKER:persistedLocksCount} | unable to determine current locks from persisted-state (no auto-asset-locker)"
- "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} | unable to create set-selector | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] same version found already tracked as latest-to-vend | setConfiguration:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job found same content already latest-to-vend | setJobDescriptor:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job matches latest-to-vend | setJobDescriptor:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no assigned UUID - using event information | eventInfo:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no assigned UUID, no event UUID - using current set status | currentSetStatus:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no set-job descriptor yet jobAtomicInstance is already downloaded set-descriptor | setDescriptor:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job with set-job descriptor that is already a downloaded set-descriptor | setDescriptor:%{public}@"
- "{IssueClientReplySetJob}\n[JOB-UUID] set-job with set-job descriptor that is different from already downloaded set-descriptor (using already downloaded) | setJobDescriptor:%{public}@"
- "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found first-tracked as downloaded set-descriptor | setConfiguration:%{public}@"
- "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found is always latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{IssueClientReplySetJob} set-configuration before sending reply: %{public}@"
- "{IssueClientReplySetJob} unable to allocate basis for response message | clientRequest:%{public}@"
- "{ReplyNoCandidates} intending to reply to staging-client with indication of no candidates available for staging (no pending staging-client-request)"
- "{ReplyNoCandidates} intending to reply to staging-client with indication of no candidates available for staging (pending staging-client-request with no reply-completion)"
- "{ResumeJobs} | Failed post-write existence check after writing STARTUP_ACTIVATED cookie file [%{public}@] | stashError:%@"
- "{ResumeJobs} | Failed to write STARTUP_ACTIVATED cookie file [%{public}@] | stashError:%@"
- "{ResumeJobs} | Set LockUsageMap | knownSetAtomicInstancesByInstance:%{public}@"
- "{ResumeJobs} | Set LockUsageMap | no knownSetAtomicInstancesByInstance"
- "{ResumeJobs} | Successfully wrote STARTUP_ACTIVATED cookie file"
- "{ResumeJobs} | Writing STARTUP_ACTIVATED cookie file [%{public}@]"
- "{SetJobLookupResponseRcvd} set-job did not provide its assigned set-descriptor"
- "{UserInitiatedSetDownloadNext} invalid nextSetSpecifierToDownload value"
- "{_initializeAutoControl} successfully initialized AutoControlManager FSM (device is before first-unlock) | MA_MILESTONE"
- "{_initializeAutoControl} successfully initialized AutoControlManager FSM (device is not before first-unlock) | MA_MILESTONE"
- "{_logResponseBody} ANOLMALY:_parseForAssetDetailsToLog returned nil for detailsToLog for the following asset meta data: %@"
- "{addLiveServerRequest} Additional AnalyticsInfo for task : %@"
- "{alreadyHaveSetDescriptorMatching} skipping set-descriptor because it's staged. Descriptor: %{public}@"
- "{assembleTaskDescriptorWithPurposeAndAutoAssetJobID} invalid autoAssetJobID(ignored):%@"
- "{cancelAssetDownloadJob} cancel of overallJobInfo in downloadTasksInFlight | autoAssetJobID:%@, assetType:%@, purpose:%@, assetId:%@, autoAssetName:%@ | taskDescriptor:%@ | result:%ld(%@)"
- "{cancelAssetDownloadJob} unable to assemble taskDescriptor | autoAssetJobID:%@, assetType:%@, purpose:%@, assetId:%@, autoAssetName:%@ | result:%ld(%@)"
- "{cancelAssetDownloadJob} unable to locate overallJobInfo in downloadTasksInFlight | autoAssetJobID:%@, assetType:%@, purpose:%@, assetId:%@, autoAssetName:%@ | taskDescriptor:%@ | result:%ld(%@)"
- "{cancelAssetDownloadTask} cancel of overallJobInfo in downloadTasksInFlight | taskDescriptor:%@"
- "{cancelAssetDownloadTask} unable to locate overallJobInfo in downloadTasksInFlight | taskDescriptor:%@"
- "{categoryForCommand} unknown command:%@"
- "{checkSplunkStatus} Unable to create base-level event requirements - not sending event | assetType:%@, sessionId:%@, events:%@, uuid:%@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] pre-SU-staging set-descriptor | setDescriptor:%{public}@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor with no latestDownloadedAtomicInstance | setDescriptor:%{public}@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor without atomic-instance | setDescriptor:%{public}@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor without set-configuration | setDescriptor:%{public}@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] unable to load persisted entry | entryID:%{public}@"
- "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] unable to load set-descriptor | entryID:%{public}@"
- "{considerSetDescriptorsForLatestToVend} no entryID"
- "{considerSetDescriptorsForLatestToVend} set-descriptor being vended does not cover current set-configuration (not first MA daemon exeution) | beingVendedSetDescriptor:%{public}@ | setConfiguration:%{public}@"
- "{considerSetDescriptorsForLatestToVend} set-descriptor being vended does not cover current set-configuration - triggering scheduler job | beingVendedSetDescriptor:%{public}@ | setConfiguration:%{public}@"
- "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | additional locked auto-asset for already tracked lock-reason+set-atomic-instance count mismatch - using first count for set-lock-usage-map | alreadyTrackedCount:%ld | nextLockTracker:%{public}@"
- "{doesSetDescriptor:satisfyAllAutoAssetEntries:} unable to form foundSelectorKey | fullAssetSelector:%@"
- "{finishPartiallyPurgedAssets} successful purged cleanup | path:%@ | depth:%d"
- "{finishPartiallyPurgedAssets} unable to finish purged cleanup | path:%@ | depth:%d | error:%@\n%@"
- "{indicateDownloadJobFinished} unknown job-type(%@) for autoAssetJobID:%@"
- "{isSSONeededForURL} Adding %@ to set of domains needing SSO"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor with no latestDownloadedAtomicInstance | setDescriptor:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without atomic-instance | setDescriptor:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor without set-configuration | setDescriptor:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load persisted entry | entryID:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] unable to load set-descriptor | entryID:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} [KEEP-SET-DESCRIPTOR] set-descriptor from pre-SU-staging | setDescriptor:%{public}@"
- "{loadPersistedCrossCheckTrimSetDescriptors} no entryID"
- "{loadPersistedSetDescriptorAsLatestToVend} adopted when no pre-existing latest-to-vend | adoptedSetDescriptor:%{public}@"
- "{loadPersistedSetDescriptorAsLatestToVend} considering covering | mostRecentSetDescriptor:%{public}@ | setConfiguration:%{public}@"
- "{loadPersistedSetDescriptorAsLatestToVend} considering satisfying | mostRecentSetDescriptor:%{public}@ | setConfiguration:%{public}@"
- "{loadPersistedSetDescriptorAsLatestToVend} no latest-to-vend | setConfiguration:%{public}@"
- "{loadPersistedSetDescriptorAsLatestToVend} preserved latest-to-vend | setConfiguration:%{public}@"
- "{loadPersistedSetDescriptorAsLatestToVend} replaced latest-to-vend | adoptedSetDescriptor:%{public}@"
- "{newTrackingCommandForEvent} missing required parameters - event:%@, client:%@"
- "{newTrackingCommandForEvent} unable to allocate command tracker for client:%@ command:%@"
- "{newTrackingCommandForEvent} unable to allocate command type tracker for remote client:%@ command:%@"
- "{newTrackingCommandForEvent} unable to associate reply with request from client:%@ command:%@"
- "{newTrackingCommandForEvent} unable to create XPC reply for un-trackable event from client for command:%@"
- "{newTrackingCommandForEvent} unable to determine client process identifier(s) for command:%@"
- "{newTrackingCommandForEvent} unable to track remote client request for command:%@"
- "{notifyLockerAsIndicatedBySetJob}"
- "{persistSetJobDescriptor}\n[SET-DESCRIPTOR][VEND] update to set-descriptor provided by set-job | setJobDescriptor:%{public}@"
- "{persistSetJobDescriptor} unable to determine local repository path for nextDownloadedAtomicEntry:%@"
- "{persistSetJobDescriptor}: found existing-atomic instance representing assets in job descriptor: %{public}@"
- "{persistSetJobDescriptor}: no existing atomic-instance representing assets in this set descriptor"
- "{persistSetJobDescriptor}: set already has existing atomic-instance as LATEST-TO-VEND. Set-configuration: %@"
- "{persistedCommand} unknown category:%llu for command:%@"
- "{purgeAllAssetsInDirectory} %@ requested purge (failed) | assetDirectory:%@ | result:%lld(%@)"
- "{purgeAllAssetsInDirectory} %@ requested purge (skipped purge [MAPurgeAssetDidntExist]) | assetDirectory:%@"
- "{purgeAllAssetsInDirectory} %@ requested purge (skipped purge of asset to be preserved) | assetDirectory:%@ | assetID:%@"
- "{purgeAllAssetsInDirectory} %@ requested purge (successfully purged) | assetDirectory:%@"
- "{purgeAllAssetsInDirectory} %@ requested purge of %lld assets | assetTypeDirectory:%@"
- "{purgeAllAssetsOfType} %@ attempted to create asset-type directory to purge but failed | assetType:%@"
- "{purgeAllAssetsOfType} %@ attempted to purge on invalid asset-type"
- "{purgeAllAssetsOfType} %@ specified asset-type that could not be normalized"
- "{purgeAllAssetsOfType} %@ specified asset-type where could not determine pre-installed asset path | assetType:%@"
- "{purgeAllAssetsOfType} %@ specified invalid purpose:%@ | assetType:%@"
- "{purgeAllAssetsOfType} %@ specified unsupported path:%@ | assetType:%@"
- "{purgeAllAssetsOfType} %@ specified unsupported purpose:%@ | assetType:%@"
- "{purgeAll} %@ requested purge-all for purpose that does not support purge-all | purpose:%@"
- "{purgeAll} %@ requested purge-all for purpose that is not well formed"
- "{purgeAll} %@ requested purge-all has finished successfully | asset-types:%ld\n%@"
- "{purgeAll} %@ requested purge-all that cannot occur before first unlock | assetType:%@"
- "{purgeAll} %@ requested purge-all where unable to completely purge all assets | asset-types:%ld\n%@"
- "{purgeAll} %@ requested purge-all with an asset-type that is not well formed | assetType:%@"
- "{purgeAll} %@ requested purge-all with preserved asset ID that is not well formed | assetType:%@ | assetID:%@"
- "{purgeAll} %@ requested purge-all with preserved asset type is not well formed | assetType:%@"
- "{purgeAll} %@ requested purge-all | asset-types:%ld\n%@"
- "{refreshDownloadedToManager} downloadedAsPatch yet no baseForPatch"
- "{removeAssetDir} canceling download due to purge | cancelTaskDescriptor:%@ | clientName:%@"
- "{removeAssetDir} failed to purge (purpose or asset ID not well formed) path:%@ | assetType:%@ | assetID:%@ | purpose:%@ | clientName:%@ | result:%lld(%@)"
- "{removeAssetDir} failed to purge path:%@ | assetType:%@ | assetID:%@ | clientName:%@ | result:%lld(%@)"
- "{removeAssetDir} failed to purge secondary path:%@ | assetType:%@ | assetID:%@ | clientName:%@ | result:%lld(%@)"
- "{removeAssetDir} successfully purged path:%@ | assetType:%@ | assetID:%@ | clientName:%@"
- "{removeAssetDir} successfully purged secondary path:%@ | assetType:%@ | assetID:%@ | clientName:%@"
- "{reportSetCatalogDecideFound} unable to initialize alreadyOnFilesystemSelector"
- "{sendDownloadResult} [SUCCESS] ANOMALY | jobID != autoAssetJobID:%@ | assetType:%@, purpose:%@, jobID:%@ | downloadInfo:%@"
- "{sendDownloadResult} catalog download success yet incomplete information | [session] assetType:%@, purpose:%@, jobID:%@ | autoAssetJobID:%@ | downloadInfo:%@"
- "{setDescriptorDownloadedLoadedFromPersisted} already no latestDownloadedAtomicInstance | setDescriptor:%@"
- "{setLockUsageMapEndedLockForSetDescriptor} just ended locks when no setIdentifierByLockReason in lock-usage-map | justEndedReason:%@ | justEndedLockCount:%ld | setDescriptor:%@ "
- "{setPreviousBatchedFailureEvent} Missing required paarameter - not considering re-sending previous failure indication | previousEvent:%@, sendEvents:%@"
- "{topLevelActivityForCommand} unknown command:%@"
- "{updateLastFetchedDate} failed to update lastFetchedDate in xml | targetLocation:%@"
- "{writeDictionaryToFile} Failed to write dictionary to file, asset type was not well formed: %@"
- "{writeDictionaryToFile} could not remove file | targetLocation:%@ | error:%@\n%@"
- "{writeDictionaryToFile} could not remove prior archive file (will continue) | archivePath:%@ | error:%@\n%@"
- "{writeDictionaryToFile} failed to write XML | targetLocation:%@"
- "{writeDictionaryToFile} moved existing file | targetLocation:%@ to archivePath:%@"
- "{writeDictionaryToFile} removed existing file | targetLocation:%@"
- "{writeDictionaryToFile} succeeded | taskDescriptor:%@"

```
