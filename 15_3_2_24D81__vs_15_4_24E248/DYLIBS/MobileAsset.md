## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset`

```diff

-1329.80.16.0.0
-  __TEXT.__text: 0x8e45c
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x5c28
-  __TEXT.__const: 0x238
-  __TEXT.__gcc_except_tab: 0x8c8
-  __TEXT.__cstring: 0x1527e
-  __TEXT.__oslogstring: 0x6e37
-  __TEXT.__unwind_info: 0x1af8
-  __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x6b1
-  __TEXT.__objc_methname: 0x12e10
-  __TEXT.__objc_methtype: 0x1479
-  __TEXT.__objc_stubs: 0x7a60
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xc30
-  __DATA_CONST.__objc_classlist: 0x210
+1487.101.2.0.0
+  __TEXT.__text: 0x8fd14
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x63cc
+  __TEXT.__const: 0x288
+  __TEXT.__gcc_except_tab: 0xbe4
+  __TEXT.__cstring: 0x1056c
+  __TEXT.__oslogstring: 0xa050
+  __TEXT.__unwind_info: 0x1b88
+  __TEXT.__objc_classname: 0x889
+  __TEXT.__objc_methname: 0x14fa5
+  __TEXT.__objc_methtype: 0x1768
+  __TEXT.__objc_stubs: 0x8180
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__objc_classlist: 0x250
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d48
+  __DATA_CONST.__objc_selrefs: 0x30a8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0xf3c0
-  __AUTH_CONST.__objc_const: 0x94d8
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_arraydata: 0x2f0
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__const: 0x1cd0
+  __AUTH_CONST.__cfstring: 0xd940
+  __AUTH_CONST.__objc_const: 0x98f0
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x7cc
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0x7fc
   __DATA.__data: 0x368
-  __DATA.__bss: 0x328
+  __DATA.__bss: 0x320
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/Versions/A/SoftwareUpdateCoreConnect
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/StreamingZip.framework/Versions/A/StreamingZip
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8784DD87-2DD1-3C7F-8CC5-F543D5EF65F6
-  Functions: 2963
-  Symbols:   5681
-  CStrings:  6957
+  UUID: 0C54DBDF-2D17-342C-8325-A43C13FCCA86
+  Functions: 2839
+  Symbols:   5697
+  CStrings:  6826
 
Symbols:
+ +[MAAutoAsset _privateStateQueue]
+ +[MAAutoAsset _privateStateQueue].cold.1
+ +[MAAutoAsset defaultDispatchQueue].cold.1
+ +[MAAutoAsset frameworkInstanceSetLogDomain].cold.1
+ +[MAAutoAsset frameworkInstanceUUID].cold.1
+ +[MAAutoAsset logMAAutoAssetVersion].cold.1
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) _estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) _resumeFromSoftwareUpdateIsSynchronous:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) estimateEvictableBytesForSoftwareUpdateSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) estimateEvictableBytesForSoftwareUpdateWithCompletion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) resumeFromSoftwareUpdateSyncWithReturnResumeErrorPtr:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) resumeFromSoftwareUpdateWithCompletion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) suspendForSoftwareUpdateSyncWithNeededBytes:returnSuspendErrorPtr:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) suspendForSoftwareUpdateWithNeededBytes:completion:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) suspendResumeStatusForSoftwareUpdateSyncWithReturnStatusErrorPtr:]
+ +[MAAutoAsset(SoftwareUpdateSuspendResume) suspendResumeStatusForSoftwareUpdateWithCompletion:]
+ +[MAAutoAssetAuthorizationPolicy _existingSandboxExtensions].cold.1
+ +[MAAutoAssetControl _privateStateQueue]
+ +[MAAutoAssetControl _privateStateQueue].cold.1
+ +[MAAutoAssetControl autoAssetControl].cold.1
+ +[MAAutoAssetControl defaultDispatchQueue].cold.1
+ +[MAAutoAssetControl frameworkInstanceSetLogDomain].cold.1
+ +[MAAutoAssetControl frameworkInstanceUUID].cold.1
+ +[MAAutoAssetMonitor defaultDispatchQueue].cold.1
+ +[MAAutoAssetPushNotificationHistory sharedInstance].cold.1
+ +[MAAutoAssetSet _privateStateQueue]
+ +[MAAutoAssetSet _privateStateQueue].cold.1
+ +[MAAutoAssetSet defaultDispatchQueue].cold.1
+ +[MAAutoAssetSet frameworkInstanceSetLogDomain].cold.1
+ +[MAAutoAssetSet frameworkInstanceUUID].cold.1
+ +[MAAutoAssetSetControl _privateStateQueue]
+ +[MAAutoAssetSetControl _privateStateQueue].cold.1
+ +[MAAutoAssetSetControl autoAssetSetControl].cold.1
+ +[MAAutoAssetSetControl defaultDispatchQueue].cold.1
+ +[MAAutoAssetSetControl frameworkInstanceSetLogDomain].cold.1
+ +[MAAutoAssetSetControl frameworkInstanceUUID].cold.1
+ +[MAAutoAssetSetRapidLock lockRecords]
+ +[MAAutoAssetSetRapidLock lockRecords].cold.1
+ +[MAAutoAssetSetRapidLock supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateInfo newServerMessageClasses:]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateInfo supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo supportsSecureCoding]
+ +[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo supportsSecureCoding]
+ +[MAPushNotificationController sharedInstance].cold.1
+ +[MASecureMobileAssetTypes sharedInstance].cold.1
+ +[MAThirdPartyCompatibility _thirdPartyAssetTypeStorage]
+ +[MAThirdPartyCompatibility compatibilityVersionForAssetType:]
+ +[MAThirdPartyCompatibility defaultThirdPartyServerURLForAssetType:]
+ +[MAThirdPartyCompatibility isThirdPartyAssetType:]
+ +[MAThirdPartyCompatibility permitThirdPartySigningForAssetType:outOrganizations:]
+ +[MAThirdPartyCompatibility(Certificates) __addTrustedSigningCertificateAuthority:]
+ +[MAThirdPartyCompatibility(Certificates) addTrustedSigningCertificateAuthority:]
+ +[MAThirdPartyCompatibility(Certificates) clearAllTrustedSigningCertificateAuthorities]
+ -[MAAsset getBaseAssetRepositoryPath]
+ -[MAAutoAsset _cancelActivityForSelectorIsSynchronous:completion:]
+ -[MAAutoAsset _checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:]
+ -[MAAutoAsset _continueLockUsage:withUsagePolicy:isSynchronous:completion:]
+ -[MAAutoAsset _currentStatusIsSynchronous:completion:]
+ -[MAAutoAsset _determineIfAvailable:withTimeout:isSynchronous:completion:]
+ -[MAAutoAsset _eliminateAllForAssetTypeIsSynchronous:completion:]
+ -[MAAutoAsset _eliminateAllForSelectorIsSynchronous:completion:]
+ -[MAAutoAsset _eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:]
+ -[MAAutoAsset _endAllPreviousLocksOfReason:isSynchronous:completion:]
+ -[MAAutoAsset _endLockUsage:isSynchronous:completion:]
+ -[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:]
+ -[MAAutoAsset _failedCancelActivity:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedCheckForNewer:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedContinueLockUsage:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedCurrentStatus:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedDetermineIfAvailable:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedEliminate:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedEndLockUsage:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedInterestInContent:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedLockContent:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedMapLockedContent:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageCancelOperation:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageDownloadAll:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageDownloadGroups:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStageEraseAll:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _failedStagePurgeAll:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAsset _interestInContent:withInterestPolicy:isSynchronous:completion:]
+ -[MAAutoAsset _lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:]
+ -[MAAutoAsset _mapLockedContent:isSynchronous:completion:]
+ -[MAAutoAsset _stageCancelOperationIsSynchronous:completion:]
+ -[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]
+ -[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]
+ -[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:]
+ -[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]
+ -[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:]
+ -[MAAutoAsset _stageEraseAllIsSynchronous:completion:]
+ -[MAAutoAsset _stagePurgeAllIsSynchronous:completion:]
+ -[MAAutoAsset _successCancelActivityIsSynchronous:completion:]
+ -[MAAutoAsset _successCheckForNewer:isSynchronous:completion:]
+ -[MAAutoAsset _successContinueLockUsage:isSynchronous:completion:]
+ -[MAAutoAsset _successCurrentStatus:isSynchronous:completion:]
+ -[MAAutoAsset _successDetermineIfAvailable:isSynchronous:completion:]
+ -[MAAutoAsset _successEliminateIsSynchronous:completion:]
+ -[MAAutoAsset _successEndLockUsage:isSynchronous:completion:]
+ -[MAAutoAsset _successInterestInContent:isSynchronous:completion:]
+ -[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:]
+ -[MAAutoAsset _successMapLockedContent:dueToDesire:isSynchronous:completion:]
+ -[MAAutoAsset _successStageCancelOperationIsSynchronous:completion:]
+ -[MAAutoAsset _successStageDetermineAllAvailable:isSynchronous:completion:]
+ -[MAAutoAsset _successStageDetermineGroupsAvailableForUpdate:isSynchronous:completion:]
+ -[MAAutoAsset _successStageDownloadAll:isSynchronous:completion:]
+ -[MAAutoAsset _successStageDownloadGroups:isSynchronous:completion:]
+ -[MAAutoAsset _successStageEraseAllIsSynchronous:completion:]
+ -[MAAutoAsset _successStagePurgeAllIsSynchronous:completion:]
+ -[MAAutoAsset infoInstance]
+ -[MAAutoAsset lockedInfoInstance]
+ -[MAAutoAsset maAutoAssetSharedConnectionClient]
+ -[MAAutoAsset setupConnectionState]
+ -[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _availableForStagingAssetSummaryIsSynchronous:completion:]
+ -[MAAutoAssetControl _controlStatistics:isSynchronous:completion:]
+ -[MAAutoAssetControl _failedControl:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _failedControlLockSummary:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _failedControlStatistics:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _failedControlSummary:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _forceGlobalAbandon:isSynchronous:completion:]
+ -[MAAutoAssetControl _forceGlobalForget:isSynchronous:completion:]
+ -[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:isSynchronous:completion:]
+ -[MAAutoAssetControl _forceGlobalUnlock:isSynchronous:completion:]
+ -[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:]
+ -[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:]
+ -[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:]
+ -[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _successControl:isSynchronous:completion:]
+ -[MAAutoAssetControl _successControlLockSummary:withLockSummaryEntries:isSynchronous:completion:]
+ -[MAAutoAssetControl _successControlStatistics:withControlStatistics:isSynchronous:completion:]
+ -[MAAutoAssetControl _successControlSummary:withJobSummaryEntries:isSynchronous:completion:]
+ -[MAAutoAssetControl _successSimulateCacheDeleteOperation:withReclaimableSpace:isSynchronous:completion:]
+ -[MAAutoAssetControlStatisticsByCommand estimateEvictableBytesForSoftwareUpdate]
+ -[MAAutoAssetControlStatisticsByCommand resumeFromSoftwareUpdate]
+ -[MAAutoAssetControlStatisticsByCommand setEstimateEvictableBytesForSoftwareUpdate:]
+ -[MAAutoAssetControlStatisticsByCommand setResumeFromSoftwareUpdate:]
+ -[MAAutoAssetControlStatisticsByCommand setSuspendForSoftwareUpdate:]
+ -[MAAutoAssetControlStatisticsByCommand setSuspendResumeStatusForSoftwareUpdate:]
+ -[MAAutoAssetControlStatisticsByCommand suspendForSoftwareUpdate]
+ -[MAAutoAssetControlStatisticsByCommand suspendResumeStatusForSoftwareUpdate]
+ -[MAAutoAssetSelector _initForAssetType:withAssetSpecifier:matchingAssetVersion:usingDecryptionKey:setAtomicInstanceUUID:]
+ -[MAAutoAssetSelector initForSetAtomicInstanceUUID:]
+ -[MAAutoAssetSelector setAtomicInstanceUUID]
+ -[MAAutoAssetSelector setSetAtomicInstanceUUID:]
+ -[MAAutoAssetSet _alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:]
+ -[MAAutoAssetSet _assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:]
+ -[MAAutoAssetSet _checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]
+ -[MAAutoAssetSet _continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:]
+ -[MAAutoAssetSet _currentSetStatusIsSynchronous:completion:]
+ -[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:isSynchronous:completion:]
+ -[MAAutoAssetSet _endAtomicLock:ofAtomicInstance:isSynchronous:completion:]
+ -[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedFormSubAtomicInstance:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSet _formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:]
+ -[MAAutoAssetSet _lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]
+ -[MAAutoAssetSet _lockAtomicSync:forAtomicInstance:performContentValidation:error:]
+ -[MAAutoAssetSet _mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:]
+ -[MAAutoAssetSet _needForAtomic:withNeedPolicy:isSynchronous:completion:]
+ -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:].cold.1
+ -[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]
+ -[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]
+ -[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:performContentValidation:isSynchronous:completion:]
+ -[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]
+ -[MAAutoAssetSet _successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:isSynchronous:completion:]
+ -[MAAutoAssetSet _successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:isSynchronous:completion:]
+ -[MAAutoAssetSet _successFormSubAtomicInstance:formedSubAtomicInstance:isSynchronous:completion:]
+ -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:]
+ -[MAAutoAssetSet _successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:isSynchronous:completion:]
+ -[MAAutoAssetSet _successOperation:forAssetSetIdentifier:isSynchronous:completion:]
+ -[MAAutoAssetSet initUsingClientDomain:forClientName:forAssetSetIdentifier:asShortTermLocker:comprisedOfEntries:usingDesiredPolicyCategory:completingFromQueue:error:].cold.1
+ -[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _autoAssetInstanceInfo:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _failedControl:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _failedControlInstanceInfo:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _failedControlLockSummary:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _failedControlOverview:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _failedControlSummary:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _successControl:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _successControlInstanceInfo:withInstanceInfo:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _successControlLockSummary:withLockSummaryEntries:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _successControlOverview:withOverviewEntries:isSynchronous:completion:]
+ -[MAAutoAssetSetControl _successControlSummary:withJobSummaryEntries:isSynchronous:completion:]
+ -[MAAutoAssetSetRapidLock .cxx_destruct]
+ -[MAAutoAssetSetRapidLock acquireShortTermLockSync]
+ -[MAAutoAssetSetRapidLock assetSetAtomicInstance]
+ -[MAAutoAssetSetRapidLock assetSetIdentifier]
+ -[MAAutoAssetSetRapidLock checkLockFileValidity]
+ -[MAAutoAssetSetRapidLock clientDomainName]
+ -[MAAutoAssetSetRapidLock encodeWithCoder:]
+ -[MAAutoAssetSetRapidLock endShortTermLockSync]
+ -[MAAutoAssetSetRapidLock init:assetSetIdentifier:assetSetAtomicInstance:]
+ -[MAAutoAssetSetRapidLock initWithCoder:]
+ -[MAAutoAssetSetRapidLock setAssetSetAtomicInstance:]
+ -[MAAutoAssetSetRapidLock setAssetSetIdentifier:]
+ -[MAAutoAssetSetRapidLock setClientDomainName:]
+ -[MAAutoAssetSetRapidLock setShortTermLockFileName:]
+ -[MAAutoAssetSetRapidLock shortTermLockFileName]
+ -[MAAutoAssetSetRapidLock summary]
+ -[MAAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MAAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MAAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MAAutoAssetSetStatus latestDownloadedAtomicInstanceFromPreSUStaging]
+ -[MAAutoAssetSetStatus previouslyVendedLockedAtomicInstance]
+ -[MAAutoAssetSetStatus setLatestDownloadedAtomicInstanceFromPreSUStaging:]
+ -[MAAutoAssetSetStatus setPreviouslyVendedLockedAtomicInstance:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo estimatedEvictableBytes]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo initWithEstimatedEvictableBytes:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo summary]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateInfo summary]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo init]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo summary]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo init]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo summary]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo initWithStatus:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo status]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo summary]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo description]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo encodeWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo initWitNeededBytes:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo initWithCoder:]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo neededBytes]
+ -[MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo summary]
+ -[SUCoreConnectClient(MAAutoSyncHelpers) connectClientSendServerMessage:proxyObject:replyQueue:isSynchronous:withReply:]
+ GCC_except_table0
+ GCC_except_table104
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table169
+ GCC_except_table17
+ GCC_except_table194
+ GCC_except_table214
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table237
+ GCC_except_table24
+ GCC_except_table248
+ GCC_except_table259
+ GCC_except_table27
+ GCC_except_table273
+ GCC_except_table284
+ GCC_except_table29
+ GCC_except_table295
+ GCC_except_table31
+ GCC_except_table312
+ GCC_except_table326
+ GCC_except_table339
+ GCC_except_table350
+ GCC_except_table361
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table88
+ GCC_except_table93
+ GCC_except_table94
+ MAConvertTicksToSeconds.ticksPerSecond
+ OBJC_IVAR_$_MAAutoAssetControlStatisticsByCommand._estimateEvictableBytesForSoftwareUpdate
+ OBJC_IVAR_$_MAAutoAssetControlStatisticsByCommand._resumeFromSoftwareUpdate
+ OBJC_IVAR_$_MAAutoAssetControlStatisticsByCommand._suspendForSoftwareUpdate
+ OBJC_IVAR_$_MAAutoAssetControlStatisticsByCommand._suspendResumeStatusForSoftwareUpdate
+ OBJC_IVAR_$_MAAutoAssetSelector._setAtomicInstanceUUID
+ OBJC_IVAR_$_MAAutoAssetSetRapidLock._assetSetAtomicInstance
+ OBJC_IVAR_$_MAAutoAssetSetRapidLock._assetSetIdentifier
+ OBJC_IVAR_$_MAAutoAssetSetRapidLock._clientDomainName
+ OBJC_IVAR_$_MAAutoAssetSetRapidLock._shortTermLockFileName
+ OBJC_IVAR_$_MAAutoAssetSetStatus._latestDownloadedAtomicInstanceFromPreSUStaging
+ OBJC_IVAR_$_MAAutoAssetSetStatus._previouslyVendedLockedAtomicInstance
+ OBJC_IVAR_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo._estimatedEvictableBytes
+ OBJC_IVAR_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo._status
+ OBJC_IVAR_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo._neededBytes
+ _CC_SHA256
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFPreferencesCopyAppValue
+ _MAAutoAssetSuspendResumeForSoftwareUpdateStatusString
+ _MAClientLog.clientLoggers
+ _MAClientLog.cold.1
+ _MAClientLog.onceToken
+ _MAConvertTicksToSeconds
+ _MAMeasurementHashAlgorithmSHA1
+ _OBJC_CLASS_$_MAAutoAssetSetRapidLock
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ _OBJC_CLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ _OBJC_CLASS_$_MAThirdPartyCompatibility
+ _OBJC_CLASS_$_NSPipe
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSTask
+ _OBJC_CLASS_$_SUCoreDevice
+ _OBJC_METACLASS_$_MAAutoAssetSetRapidLock
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ _OBJC_METACLASS_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ _OBJC_METACLASS_$_MAThirdPartyCompatibility
+ __101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.985
+ __113-[MAAutoAssetSet _alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:]_block_invoke.421
+ __113-[MAAutoAssetSet _alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:]_block_invoke.443
+ __119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.412
+ __120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.571
+ __121-[MAAutoAssetSet checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:completion:]_block_invoke.459
+ __121-[MAAutoAssetSet checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:completion:]_block_invoke_2.460
+ __133+[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke.699
+ __136-[MAAutoAssetSet _checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke.484
+ __26-[MAAsset cancelDownload:]_block_invoke.1097
+ __26-[MAAsset purgeWithError:]_block_invoke.1092
+ __36+[MAAutoAsset stageCancelOperation:]_block_invoke.1013
+ __42-[MAXpcManager setClientConnectionHandler]_block_invoke.1058
+ __42-[MAXpcManager setClientConnectionHandler]_block_invoke.1059
+ __50-[MAPushNotificationController _serviceConnection]_block_invoke.78
+ __60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.1081
+ __60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke.cold.1
+ __61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke.1004
+ __62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke.976
+ __64+[MAAutoAsset determineIfAvailable:forAssetSelector:completion:]_block_invoke.829
+ __64-[MASecureManifestStorage _storeManifest:infoPlist:stage:error:]_block_invoke.1037
+ __65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.943
+ __65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.947
+ __66-[MAAutoAssetControl _controlStatistics:isSynchronous:completion:]_block_invoke.390
+ __69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.610
+ __78-[MAAutoAsset _interestInContent:withInterestPolicy:isSynchronous:completion:]_block_invoke.441
+ __80+[MAAutoAsset interestInContent:forAssetSelector:withInterestPolicy:completion:]_block_invoke.817
+ __84-[MAAutoAsset lockContent:withUsagePolicy:withTimeout:reportingProgress:completion:]_block_invoke.518
+ __84-[MAAutoAsset lockContent:withUsagePolicy:withTimeout:reportingProgress:completion:]_block_invoke_2.519
+ __84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.603
+ __93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke.402
+ __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1050
+ __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1051
+ __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1053
+ __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.1055
+ __99-[MAAutoAsset _lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke.514
+ __99-[MAAutoAssetSet _mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:]_block_invoke.509
+ __Block_byref_object_copy_.1223
+ __Block_byref_object_copy_.729
+ __Block_byref_object_copy_.800
+ __Block_byref_object_dispose_.1224
+ __Block_byref_object_dispose_.730
+ __Block_byref_object_dispose_.801
+ __MABufferToHexString
+ __MAClientLog
+ __MAPreferencesCopyValue
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SUCoreConnectClient_$_MAAutoSyncHelpers
+ __OBJC_$_CATEGORY_SUCoreConnectClient_$_MAAutoSyncHelpers
+ __OBJC_$_CLASS_METHODS_MAAutoAsset(SoftwareUpdateSuspendResume)
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSetRapidLock
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_$_CLASS_METHODS_MAThirdPartyCompatibility(Certificates)
+ __OBJC_$_CLASS_PROP_LIST_MAAutoAssetSetRapidLock
+ __OBJC_$_CLASS_PROP_LIST_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSetRapidLock
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSetRapidLock
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_$_PROP_LIST_MAAutoAssetSetRapidLock
+ __OBJC_$_PROP_LIST_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_$_PROP_LIST_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_$_PROP_LIST_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetSetRapidLock
+ __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSetRapidLock
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_CLASS_RO_$_MAThirdPartyCompatibility
+ __OBJC_METACLASS_RO_$_MAAutoAssetSetRapidLock
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo
+ __OBJC_METACLASS_RO_$_MAThirdPartyCompatibility
+ ___100+[MAAutoAsset endPreviousLocksOfReason:forClientName:forAssetSelector:removingLockCount:completion:]_block_invoke_3
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke_3
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke_4
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke_5
+ ___102+[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:]_block_invoke_3
+ ___103-[MAAutoAssetSet lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:]_block_invoke_3
+ ___103-[MAAutoAssetSet lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:]_block_invoke_4
+ ___106+[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:]_block_invoke
+ ___106+[MAAutoAsset(SoftwareUpdateSuspendResume) _suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:]_block_invoke
+ ___107-[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:performContentValidation:isSynchronous:completion:]_block_invoke
+ ___108-[MAAutoAssetSet _formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:]_block_invoke
+ ___108-[MAAutoAssetSet _formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:]_block_invoke_2
+ ___108-[MAAutoAssetSet _formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:]_block_invoke_3
+ ___108-[MAAutoAssetSet _formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:]_block_invoke_4
+ ___109+[MAAutoAsset(SoftwareUpdateSuspendResume) _estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:]_block_invoke
+ ___109+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendResumeStatusForSoftwareUpdateSyncWithReturnStatusErrorPtr:]_block_invoke
+ ___110+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendForSoftwareUpdateSyncWithNeededBytes:returnSuspendErrorPtr:]_block_invoke
+ ___111-[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:]_block_invoke
+ ___111-[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:]_block_invoke_2
+ ___111-[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:]_block_invoke_3
+ ___113-[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:]_block_invoke
+ ___113-[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:]_block_invoke_2
+ ___113-[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:]_block_invoke_3
+ ___113-[MAAutoAssetSet _alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:]_block_invoke
+ ___113-[MAAutoAssetSet _alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:]_block_invoke_2
+ ___116-[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:]_block_invoke
+ ___116-[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_2
+ ___116-[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_3
+ ___118-[MAAutoAssetSet _lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke
+ ___118-[MAAutoAssetSet _lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_2
+ ___118-[MAAutoAssetSet _lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_3
+ ___118-[MAAutoAssetSet _lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_4
+ ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke
+ ___119-[MAAutoAsset lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:reportingProgress:]_block_invoke_3
+ ___120+[MAAutoAsset stageDownloadGroupsSync:awaitingAllGroups:withStagingTimeout:byGroupAssetsStaged:error:reportingProgress:]_block_invoke
+ ___120+[MAAutoAsset stageDownloadGroupsSync:awaitingAllGroups:withStagingTimeout:byGroupAssetsStaged:error:reportingProgress:]_block_invoke_2
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke
+ ___120-[SUCoreConnectClient(MAAutoSyncHelpers) connectClientSendServerMessage:proxyObject:replyQueue:isSynchronous:withReply:]_block_invoke
+ ___120-[SUCoreConnectClient(MAAutoSyncHelpers) connectClientSendServerMessage:proxyObject:replyQueue:isSynchronous:withReply:]_block_invoke_2
+ ___122-[MAAutoAssetSet lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:reportingProgress:]_block_invoke_3
+ ___133+[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke_2
+ ___136-[MAAutoAssetSet _checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke
+ ___136-[MAAutoAssetSet _checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_2
+ ___136-[MAAutoAssetSet _checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_3
+ ___144-[MAAutoAssetSet checkAtomicSync:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:discoveredAtomicEntries:error:reportingProgress:]_block_invoke_3
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke_2
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke_3
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke_4
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke_5
+ ___148-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:]_block_invoke_6
+ ___152+[MAAutoAsset(SoftwareUpdateSuspendResume) estimateEvictableBytesForSoftwareUpdateSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:]_block_invoke
+ ___29+[MAAutoAsset stageEraseAll:]_block_invoke_3
+ ___29+[MAAutoAsset stagePurgeAll:]_block_invoke_3
+ ___33+[MAAutoAsset _privateStateQueue]_block_invoke
+ ___35-[MAAutoAsset setupConnectionState]_block_invoke
+ ___36+[MAAutoAsset stageCancelOperation:]_block_invoke_2
+ ___36+[MAAutoAssetSet _privateStateQueue]_block_invoke
+ ___38+[MAAutoAssetSetRapidLock lockRecords]_block_invoke
+ ___40+[MAAutoAssetControl _privateStateQueue]_block_invoke
+ ___43+[MAAutoAssetSetControl _privateStateQueue]_block_invoke
+ ___50+[MAAutoAsset eliminateAllForSelector:completion:]_block_invoke_3
+ ___51+[MAAutoAsset eliminateAllForAssetType:completion:]_block_invoke_3
+ ___52+[MAAutoAsset cancelActivityForSelector:completion:]_block_invoke_3
+ ___54-[MAAutoAsset _currentStatusIsSynchronous:completion:]_block_invoke
+ ___54-[MAAutoAsset _currentStatusIsSynchronous:completion:]_block_invoke_2
+ ___54-[MAAutoAsset _currentStatusIsSynchronous:completion:]_block_invoke_3
+ ___54-[MAAutoAsset _endLockUsage:isSynchronous:completion:]_block_invoke
+ ___54-[MAAutoAsset _endLockUsage:isSynchronous:completion:]_block_invoke_2
+ ___54-[MAAutoAsset _endLockUsage:isSynchronous:completion:]_block_invoke_3
+ ___54-[MAAutoAsset _stageEraseAllIsSynchronous:completion:]_block_invoke
+ ___54-[MAAutoAsset _stageEraseAllIsSynchronous:completion:]_block_invoke_2
+ ___54-[MAAutoAsset _stageEraseAllIsSynchronous:completion:]_block_invoke_3
+ ___54-[MAAutoAsset _stagePurgeAllIsSynchronous:completion:]_block_invoke
+ ___54-[MAAutoAsset _stagePurgeAllIsSynchronous:completion:]_block_invoke_2
+ ___54-[MAAutoAsset _stagePurgeAllIsSynchronous:completion:]_block_invoke_3
+ ___58-[MAAutoAsset _mapLockedContent:isSynchronous:completion:]_block_invoke
+ ___58-[MAAutoAsset _mapLockedContent:isSynchronous:completion:]_block_invoke_2
+ ___58-[MAAutoAsset _mapLockedContent:isSynchronous:completion:]_block_invoke_3
+ ___58-[MAAutoAssetSet lockAtomic:forAtomicInstance:completion:]_block_invoke
+ ___58-[MAAutoAssetSet lockAtomic:forAtomicInstance:completion:]_block_invoke_2
+ ___60-[MAAutoAssetSet _currentSetStatusIsSynchronous:completion:]_block_invoke
+ ___60-[MAAutoAssetSet _currentSetStatusIsSynchronous:completion:]_block_invoke_2
+ ___60-[MAAutoAssetSet _currentSetStatusIsSynchronous:completion:]_block_invoke_3
+ ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_2
+ ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_3
+ ___61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke_4
+ ___61-[MAAutoAsset _stageCancelOperationIsSynchronous:completion:]_block_invoke
+ ___61-[MAAutoAsset _stageCancelOperationIsSynchronous:completion:]_block_invoke_2
+ ___61-[MAAutoAsset _stageCancelOperationIsSynchronous:completion:]_block_invoke_3
+ ___62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke_2
+ ___64+[MAAutoAsset determineIfAvailable:forAssetSelector:completion:]_block_invoke_2
+ ___64-[MAAutoAsset _eliminateAllForSelectorIsSynchronous:completion:]_block_invoke
+ ___64-[MAAutoAsset _eliminateAllForSelectorIsSynchronous:completion:]_block_invoke_2
+ ___64-[MAAutoAsset _eliminateAllForSelectorIsSynchronous:completion:]_block_invoke_3
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke_2
+ ___65-[MAAutoAsset _eliminateAllForAssetTypeIsSynchronous:completion:]_block_invoke
+ ___65-[MAAutoAsset _eliminateAllForAssetTypeIsSynchronous:completion:]_block_invoke_2
+ ___65-[MAAutoAsset _eliminateAllForAssetTypeIsSynchronous:completion:]_block_invoke_3
+ ___66+[MAAutoAsset eliminatePromotedNeverLockedForSelector:completion:]_block_invoke_3
+ ___66-[MAAutoAsset _cancelActivityForSelectorIsSynchronous:completion:]_block_invoke
+ ___66-[MAAutoAsset _cancelActivityForSelectorIsSynchronous:completion:]_block_invoke_2
+ ___66-[MAAutoAsset _cancelActivityForSelectorIsSynchronous:completion:]_block_invoke_3
+ ___66-[MAAutoAssetControl _controlStatistics:isSynchronous:completion:]_block_invoke
+ ___66-[MAAutoAssetControl _controlStatistics:isSynchronous:completion:]_block_invoke_2
+ ___66-[MAAutoAssetControl _forceGlobalForget:isSynchronous:completion:]_block_invoke
+ ___66-[MAAutoAssetControl _forceGlobalForget:isSynchronous:completion:]_block_invoke_2
+ ___66-[MAAutoAssetControl _forceGlobalForget:isSynchronous:completion:]_block_invoke_3
+ ___66-[MAAutoAssetControl _forceGlobalUnlock:isSynchronous:completion:]_block_invoke
+ ___66-[MAAutoAssetControl _forceGlobalUnlock:isSynchronous:completion:]_block_invoke_2
+ ___66-[MAAutoAssetControl _forceGlobalUnlock:isSynchronous:completion:]_block_invoke_3
+ ___67-[MAAutoAssetControl _forceGlobalAbandon:isSynchronous:completion:]_block_invoke
+ ___67-[MAAutoAssetControl _forceGlobalAbandon:isSynchronous:completion:]_block_invoke_2
+ ___67-[MAAutoAssetControl _forceGlobalAbandon:isSynchronous:completion:]_block_invoke_3
+ ___69-[MAAutoAsset _endAllPreviousLocksOfReason:isSynchronous:completion:]_block_invoke
+ ___69-[MAAutoAsset _endAllPreviousLocksOfReason:isSynchronous:completion:]_block_invoke_2
+ ___69-[MAAutoAsset _endAllPreviousLocksOfReason:isSynchronous:completion:]_block_invoke_3
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke
+ ___70+[MAAutoAsset endAllPreviousLocksOfSelector:forClientName:completion:]_block_invoke_3
+ ___73-[MAAutoAssetSet _needForAtomic:withNeedPolicy:isSynchronous:completion:]_block_invoke
+ ___73-[MAAutoAssetSet _needForAtomic:withNeedPolicy:isSynchronous:completion:]_block_invoke_2
+ ___73-[MAAutoAssetSet _needForAtomic:withNeedPolicy:isSynchronous:completion:]_block_invoke_3
+ ___73-[MAAutoAssetSet _needForAtomic:withNeedPolicy:isSynchronous:completion:]_block_invoke_4
+ ___73-[MAAutoAssetSetControl _autoAssetInstanceInfo:isSynchronous:completion:]_block_invoke
+ ___73-[MAAutoAssetSetControl _autoAssetInstanceInfo:isSynchronous:completion:]_block_invoke_2
+ ___73-[MAAutoAssetSetControl _autoAssetInstanceInfo:isSynchronous:completion:]_block_invoke_3
+ ___74-[MAAutoAsset _determineIfAvailable:withTimeout:isSynchronous:completion:]_block_invoke
+ ___74-[MAAutoAsset _determineIfAvailable:withTimeout:isSynchronous:completion:]_block_invoke_2
+ ___74-[MAAutoAsset _determineIfAvailable:withTimeout:isSynchronous:completion:]_block_invoke_3
+ ___75+[MAAutoAsset stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke_3
+ ___75-[MAAutoAsset _continueLockUsage:withUsagePolicy:isSynchronous:completion:]_block_invoke
+ ___75-[MAAutoAsset _continueLockUsage:withUsagePolicy:isSynchronous:completion:]_block_invoke_2
+ ___75-[MAAutoAsset _continueLockUsage:withUsagePolicy:isSynchronous:completion:]_block_invoke_3
+ ___75-[MAAutoAssetSet _endAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke
+ ___75-[MAAutoAssetSet _endAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke_2
+ ___75-[MAAutoAssetSet _endAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke_3
+ ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke
+ ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke_2
+ ___76-[MAAutoAsset _stageDownloadAll:reportingProgress:isSynchronous:completion:]_block_invoke_3
+ ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke
+ ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke_2
+ ___77-[MAAutoAsset _stageDetermineAllAvailableForUpdate:isSynchronous:completion:]_block_invoke_3
+ ___77-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:isSynchronous:completion:]_block_invoke
+ ___77-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:isSynchronous:completion:]_block_invoke_2
+ ___77-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:isSynchronous:completion:]_block_invoke_3
+ ___78-[MAAutoAsset _interestInContent:withInterestPolicy:isSynchronous:completion:]_block_invoke
+ ___78-[MAAutoAsset _interestInContent:withInterestPolicy:isSynchronous:completion:]_block_invoke_2
+ ___79-[MAAutoAssetControl _availableForStagingAssetSummaryIsSynchronous:completion:]_block_invoke
+ ___79-[MAAutoAssetControl _availableForStagingAssetSummaryIsSynchronous:completion:]_block_invoke_2
+ ___79-[MAAutoAssetControl _availableForStagingAssetSummaryIsSynchronous:completion:]_block_invoke_3
+ ___79-[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:isSynchronous:completion:]_block_invoke
+ ___79-[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:isSynchronous:completion:]_block_invoke_2
+ ___79-[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:isSynchronous:completion:]_block_invoke_3
+ ___80+[MAAutoAsset interestInContent:forAssetSelector:withInterestPolicy:completion:]_block_invoke_2
+ ___80-[MAAutoAsset _eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:]_block_invoke
+ ___80-[MAAutoAsset _eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:]_block_invoke_2
+ ___80-[MAAutoAsset _eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:]_block_invoke_3
+ ___80-[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:]_block_invoke
+ ___80-[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:]_block_invoke_2
+ ___80-[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:]_block_invoke_3
+ ___83+[MAAutoAsset(SoftwareUpdateSuspendResume) resumeFromSoftwareUpdateWithCompletion:]_block_invoke
+ ___83+[MAAutoAsset(SoftwareUpdateSuspendResume) resumeFromSoftwareUpdateWithCompletion:]_block_invoke_2
+ ___83-[MAAutoAsset _checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:]_block_invoke
+ ___83-[MAAutoAsset _checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:]_block_invoke_2
+ ___83-[MAAutoAsset _checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:]_block_invoke_3
+ ___83-[MAAutoAssetSet _lockAtomicSync:forAtomicInstance:performContentValidation:error:]_block_invoke
+ ___83-[MAAutoAssetSet lockAtomic:forAtomicInstance:performContentValidation:completion:]_block_invoke
+ ___83-[MAAutoAssetSet lockAtomic:forAtomicInstance:performContentValidation:completion:]_block_invoke_2
+ ___84-[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:]_block_invoke
+ ___84-[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:]_block_invoke_2
+ ___84-[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:]_block_invoke_3
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke
+ ___85+[MAAutoAsset endAllPreviousLocksOfReason:forClientName:forAssetSelector:completion:]_block_invoke_3
+ ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke
+ ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke_2
+ ___85+[MAAutoAsset stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke_3
+ ___85-[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___85-[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___85-[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___86-[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___86-[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___86-[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___86-[MAAutoAssetSet _assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:]_block_invoke
+ ___86-[MAAutoAssetSet _assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:]_block_invoke_2
+ ___86-[MAAutoAssetSet _assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:]_block_invoke_3
+ ___86-[MAAutoAssetSet _assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:]_block_invoke_4
+ ___87-[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___87-[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___87-[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___87-[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___87-[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___87-[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___88-[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___88-[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___88-[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke
+ ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke_2
+ ___90-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:]_block_invoke_3
+ ___93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___93-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___94+[MAAutoAsset(SoftwareUpdateSuspendResume) _resumeFromSoftwareUpdateIsSynchronous:completion:]_block_invoke
+ ___94-[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___94-[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___94-[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
+ ___95+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendForSoftwareUpdateWithNeededBytes:completion:]_block_invoke
+ ___95+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendForSoftwareUpdateWithNeededBytes:completion:]_block_invoke_2
+ ___95+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendResumeStatusForSoftwareUpdateWithCompletion:]_block_invoke
+ ___95+[MAAutoAsset(SoftwareUpdateSuspendResume) suspendResumeStatusForSoftwareUpdateWithCompletion:]_block_invoke_2
+ ___95-[MAAutoAssetSet _continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:]_block_invoke
+ ___95-[MAAutoAssetSet _continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:]_block_invoke_2
+ ___95-[MAAutoAssetSet _continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:]_block_invoke_3
+ ___95-[MAAutoAssetSet _continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:]_block_invoke_4
+ ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___95-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
+ ___97+[MAAutoAsset(SoftwareUpdateSuspendResume) resumeFromSoftwareUpdateSyncWithReturnResumeErrorPtr:]_block_invoke
+ ___97-[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:]_block_invoke
+ ___97-[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:]_block_invoke_2
+ ___97-[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:]_block_invoke_3
+ ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___97-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
+ ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___97-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
+ ___98+[MAAutoAsset(SoftwareUpdateSuspendResume) estimateEvictableBytesForSoftwareUpdateWithCompletion:]_block_invoke
+ ___98+[MAAutoAsset(SoftwareUpdateSuspendResume) estimateEvictableBytesForSoftwareUpdateWithCompletion:]_block_invoke_2
+ ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke
+ ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_2
+ ___98-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:]_block_invoke_3
+ ___99-[MAAutoAsset _lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke
+ ___99-[MAAutoAsset _lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:]_block_invoke_2
+ ___99-[MAAutoAssetSet _mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:]_block_invoke
+ ___99-[MAAutoAssetSet _mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:]_block_invoke_2
+ ___MAensureExtension_block_invoke.1230
+ ___MAsendDownloadAsset_block_invoke.1127
+ ___MAsendPMVCancelDownload_block_invoke.1147
+ ___MAsendPMVCancelDownload_block_invoke.1153
+ ___MAsendPMVDownload_block_invoke.1133
+ ____MAClientLog_block_invoke
+ ____MAPreferencesCopyValue_block_invoke
+ ____preferencesDomainProtectionDispatchQueue_block_invoke
+ ___block_descriptor_40_e8_32bs_e39_v24?0"MAAutoAssetStatus"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e75_v24?0"MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
+ ___block_descriptor_48_e8_32bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32bs_e20_v24?0q8"NSError"16l
+ ___block_descriptor_48_e8_32bs_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32r40r_e20_v24?0q8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e39_v24?0"MAAutoAssetStatus"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e50_v24?0"MAAutoAssetControlStatistics"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e54_v24?0"MAAutoAssetSetInstanceDescriptor"8"NSError"16l
+ ___block_descriptor_48_e8_32r40r_e54_v32?0"NSString"8"MAAutoAssetSelector"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"MAAutoAssetStatus"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e42_v32?0"NSString"8"NSArray"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e54_v32?0"NSString"8"MAAutoAssetSelector"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e58_v32?0"MAAutoAssetSelector"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e61_v36?0"MAAutoAssetSelector"8B16"NSDictionary"20"NSError"28l
+ ___block_descriptor_48_e8_32s40bs_e75_v24?0"MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36l
+ ___block_descriptor_49_e8_32s40bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_50_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0l
+ ___block_descriptor_56_e8_32r40r48r_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_56_e8_32r40r48r_e23_v32?0Q8q16"NSError"24l
+ ___block_descriptor_56_e8_32r40r48r_e37_v32?0"NSDictionary"8Q16"NSError"24l
+ ___block_descriptor_56_e8_32r40r48r_e42_v32?0"NSString"8"NSArray"16"NSError"24l
+ ___block_descriptor_56_e8_32r40r48r_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_56_e8_32r40r48r_e58_v32?0"MAAutoAssetSelector"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_56_e8_32r40r48r_e61_v36?0"MAAutoAssetSelector"8B16"NSDictionary"20"NSError"28l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_58_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_61_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32r40r48r56r_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36l
+ ___block_descriptor_64_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_65_e8_32s40bs48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_65_e8_32s40bs48r56r_e5_v8?0l
+ ___block_descriptor_65_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_65_e8_32s40s48s56bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_69_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48bs_e17_v16?0"NSError"8l
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e17_v16?0"NSError"8l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_74_e8_32s40s48bs56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_81_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8l
+ ___block_descriptor_82_e8_32s40s48s56bs64r72r_e5_v8?0l
+ ___block_descriptor_90_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8l
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32r40r
+ ___copy_helper_block_e8_32s40b48r56r
+ ___copy_helper_block_e8_32s40s48s56b64r72r
+ ___destroy_helper_block_e8_32r40r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r
+ ___maConnectionClient
+ __block_literal_global.1041
+ __block_literal_global.1043
+ __block_literal_global.1046
+ __block_literal_global.1049
+ __block_literal_global.1050
+ __block_literal_global.1085
+ __block_literal_global.1091
+ __block_literal_global.1101
+ __block_literal_global.1106
+ __block_literal_global.1130
+ __block_literal_global.1326
+ __block_literal_global.1343
+ __block_literal_global.2699
+ __block_literal_global.2701
+ __block_literal_global.2703
+ __block_literal_global.2705
+ __block_literal_global.481
+ __block_literal_global.524
+ __block_literal_global.528
+ __block_literal_global.534
+ __block_literal_global.536
+ __block_literal_global.665
+ __block_literal_global.711
+ __block_literal_global.717
+ __block_literal_global.719
+ __block_literal_global.77
+ __block_literal_global.81
+ __block_literal_global.819
+ __block_literal_global.824
+ __block_literal_global.826
+ __block_literal_global.828
+ __block_literal_global.83
+ __hashCFArray
+ __hashCFString
+ __os_activity_create
+ __os_activity_current
+ __preferencesDomainProtectionDispatchQueue
+ _dispatch_assert_queue_not$V2
+ _getClientCallbackQueue.cold.1
+ _getClientInternalStateQueue.cold.1
+ _getCommsManager.cold.1
+ _getSandboxExtensions.cold.1
+ _getV1DecodeClasses.cold.1
+ _hashCFString.cold.1
+ _hashCFString.cold.2
+ _hashCFString.cold.3
+ _hashCFType.cold.1
+ _kMobileAssetPreferencesThirdPartyStagingPathComponent
+ _mach_absolute_time
+ _mach_timebase_info
+ _malloc_type_malloc
+ _objc_msgSend$__addTrustedSigningCertificateAuthority:
+ _objc_msgSend$_activeJobSummary:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:
+ _objc_msgSend$_assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:
+ _objc_msgSend$_autoAssetInstanceInfo:isSynchronous:completion:
+ _objc_msgSend$_autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_availableForStagingAssetSummaryIsSynchronous:completion:
+ _objc_msgSend$_cancelActivityForSelectorIsSynchronous:completion:
+ _objc_msgSend$_checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:
+ _objc_msgSend$_checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:
+ _objc_msgSend$_continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:
+ _objc_msgSend$_continueLockUsage:withUsagePolicy:isSynchronous:completion:
+ _objc_msgSend$_controlStatistics:isSynchronous:completion:
+ _objc_msgSend$_currentSetStatusIsSynchronous:completion:
+ _objc_msgSend$_currentStatusIsSynchronous:completion:
+ _objc_msgSend$_determineIfAvailable:withTimeout:isSynchronous:completion:
+ _objc_msgSend$_eliminateAllForAssetTypeIsSynchronous:completion:
+ _objc_msgSend$_eliminateAllForSelectorIsSynchronous:completion:
+ _objc_msgSend$_eliminateAtomic:awaitingUnlocked:isSynchronous:completion:
+ _objc_msgSend$_eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:
+ _objc_msgSend$_endAllPreviousLocksOfReason:isSynchronous:completion:
+ _objc_msgSend$_endAtomicLock:ofAtomicInstance:isSynchronous:completion:
+ _objc_msgSend$_endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:
+ _objc_msgSend$_endLockUsage:isSynchronous:completion:
+ _objc_msgSend$_endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:
+ _objc_msgSend$_estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:
+ _objc_msgSend$_failedCancelActivity:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedCheckForNewer:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedContinueLockUsage:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControl:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControlInstanceInfo:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControlLockSummary:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControlOverview:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControlStatistics:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedControlSummary:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedCurrentStatus:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedDetermineIfAvailable:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedEliminate:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedEndLockUsage:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedFormSubAtomicInstance:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedInterestInContent:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedLockContent:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedMapLockedContent:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageCancelOperation:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageDownloadAll:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageDownloadGroups:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStageEraseAll:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_failedStagePurgeAll:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_forceGlobalAbandon:isSynchronous:completion:
+ _objc_msgSend$_forceGlobalForget:isSynchronous:completion:
+ _objc_msgSend$_forceGlobalPurge:forcingUnlock:isSynchronous:completion:
+ _objc_msgSend$_forceGlobalUnlock:isSynchronous:completion:
+ _objc_msgSend$_formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:
+ _objc_msgSend$_initForAssetType:withAssetSpecifier:matchingAssetVersion:usingDecryptionKey:setAtomicInstanceUUID:
+ _objc_msgSend$_interestInContent:withInterestPolicy:isSynchronous:completion:
+ _objc_msgSend$_knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:
+ _objc_msgSend$_lockAtomicSync:forAtomicInstance:performContentValidation:error:
+ _objc_msgSend$_lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:
+ _objc_msgSend$_lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:
+ _objc_msgSend$_mapLockedContent:isSynchronous:completion:
+ _objc_msgSend$_needForAtomic:withNeedPolicy:isSynchronous:completion:
+ _objc_msgSend$_privateStateQueue
+ _objc_msgSend$_resumeFromSoftwareUpdateIsSynchronous:completion:
+ _objc_msgSend$_scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:
+ _objc_msgSend$_shortTermCurrentSetStatusIsSynchronous:completion:
+ _objc_msgSend$_shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:
+ _objc_msgSend$_shortTermLockAtomic:forAtomicInstance:performContentValidation:isSynchronous:completion:
+ _objc_msgSend$_shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:
+ _objc_msgSend$_simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:
+ _objc_msgSend$_simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:
+ _objc_msgSend$_simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:
+ _objc_msgSend$_stageCancelOperationIsSynchronous:completion:
+ _objc_msgSend$_stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:
+ _objc_msgSend$_stageDetermineAllAvailableForUpdate:isSynchronous:completion:
+ _objc_msgSend$_stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:
+ _objc_msgSend$_stageDownloadAll:reportingProgress:isSynchronous:completion:
+ _objc_msgSend$_stageDownloadAllStatusProgress:stageProgressError:progressBlock:
+ _objc_msgSend$_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:
+ _objc_msgSend$_stageEraseAllIsSynchronous:completion:
+ _objc_msgSend$_stagePurgeAllIsSynchronous:completion:
+ _objc_msgSend$_stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:
+ _objc_msgSend$_stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_successCancelActivityIsSynchronous:completion:
+ _objc_msgSend$_successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:isSynchronous:completion:
+ _objc_msgSend$_successCheckForNewer:isSynchronous:completion:
+ _objc_msgSend$_successContinueLockUsage:isSynchronous:completion:
+ _objc_msgSend$_successControl:isSynchronous:completion:
+ _objc_msgSend$_successControlInstanceInfo:withInstanceInfo:isSynchronous:completion:
+ _objc_msgSend$_successControlLockSummary:withLockSummaryEntries:isSynchronous:completion:
+ _objc_msgSend$_successControlOverview:withOverviewEntries:isSynchronous:completion:
+ _objc_msgSend$_successControlStatistics:withControlStatistics:isSynchronous:completion:
+ _objc_msgSend$_successControlSummary:withJobSummaryEntries:isSynchronous:completion:
+ _objc_msgSend$_successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:isSynchronous:completion:
+ _objc_msgSend$_successCurrentStatus:isSynchronous:completion:
+ _objc_msgSend$_successDetermineIfAvailable:isSynchronous:completion:
+ _objc_msgSend$_successEliminateIsSynchronous:completion:
+ _objc_msgSend$_successEndLockUsage:isSynchronous:completion:
+ _objc_msgSend$_successFormSubAtomicInstance:formedSubAtomicInstance:isSynchronous:completion:
+ _objc_msgSend$_successInterestInContent:isSynchronous:completion:
+ _objc_msgSend$_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:
+ _objc_msgSend$_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:
+ _objc_msgSend$_successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:isSynchronous:completion:
+ _objc_msgSend$_successMapLockedContent:dueToDesire:isSynchronous:completion:
+ _objc_msgSend$_successOperation:forAssetSetIdentifier:isSynchronous:completion:
+ _objc_msgSend$_successSimulateCacheDeleteOperation:withReclaimableSpace:isSynchronous:completion:
+ _objc_msgSend$_successStageCancelOperationIsSynchronous:completion:
+ _objc_msgSend$_successStageDetermineAllAvailable:isSynchronous:completion:
+ _objc_msgSend$_successStageDetermineGroupsAvailableForUpdate:isSynchronous:completion:
+ _objc_msgSend$_successStageDownloadAll:isSynchronous:completion:
+ _objc_msgSend$_successStageDownloadGroups:isSynchronous:completion:
+ _objc_msgSend$_successStageEraseAllIsSynchronous:completion:
+ _objc_msgSend$_successStagePurgeAllIsSynchronous:completion:
+ _objc_msgSend$_suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:
+ _objc_msgSend$_suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:
+ _objc_msgSend$_thirdPartyAssetTypeStorage
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$checkLockFileValidity
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$compatibilityVersionForAssetType:
+ _objc_msgSend$connectClientSendServerMessage:proxyObject:replyQueue:isSynchronous:withReply:
+ _objc_msgSend$connectClientSendSynchronousServerMessage:proxyObject:errorPtr:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$estimateEvictableBytesForSoftwareUpdate
+ _objc_msgSend$estimatedEvictableBytes
+ _objc_msgSend$fileHandleForReading
+ _objc_msgSend$fileHandleForWriting
+ _objc_msgSend$fileHandleWithNullDevice
+ _objc_msgSend$infoInstance
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initWitNeededBytes:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$isBootedOSSecureInternal
+ _objc_msgSend$latestDownloadedAtomicInstanceFromPreSUStaging
+ _objc_msgSend$launchAndReturnError:
+ _objc_msgSend$lockRecords
+ _objc_msgSend$lockedInfoInstance
+ _objc_msgSend$maAutoAssetSharedConnectionClient
+ _objc_msgSend$neededBytes
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$pipe
+ _objc_msgSend$precomposedStringWithCanonicalMapping
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$readDataToEndOfFile
+ _objc_msgSend$resumeFromSoftwareUpdate
+ _objc_msgSend$setArguments:
+ _objc_msgSend$setAtomicInstanceUUID
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setEstimateEvictableBytesForSoftwareUpdate:
+ _objc_msgSend$setExecutableURL:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setResumeFromSoftwareUpdate:
+ _objc_msgSend$setStandardInput:
+ _objc_msgSend$setStandardOutput:
+ _objc_msgSend$setSuspendForSoftwareUpdate:
+ _objc_msgSend$setSuspendResumeStatusForSoftwareUpdate:
+ _objc_msgSend$setupConnectionState
+ _objc_msgSend$sharedDevice
+ _objc_msgSend$shortTermLockFileName
+ _objc_msgSend$status
+ _objc_msgSend$suspendForSoftwareUpdate
+ _objc_msgSend$suspendResumeStatusForSoftwareUpdate
+ _objc_msgSend$terminate
+ _objc_msgSend$terminationStatus
+ _objc_msgSend$waitUntilExit
+ _objc_msgSend$writeData:error:
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_activity_scope_enter
+ _os_activity_scope_leave
+ _os_variant_has_internal_content
+ _preferencesDomainProtectionDispatchQueue.cold.1
+ _preferencesDomainProtectionDispatchQueue.preferencesDomainQueue
+ _preferencesDomainProtectionDispatchQueue.preferencesDomainQueueOnce
+ _privateStateQueue.frameworkQueue
+ _privateStateQueue.frameworkQueueOnce
+ _privateStateQueue.setFrameworkQueue
+ _privateStateQueue.setFrameworkQueueOnce
+ assetIdDisallowedCharacterSet.cold.1
+ assetTypeDisallowedCharacterSet.cold.1
+ attributesInDownloadContent.cold.1
+ attributesInDownloadPolicy.cold.1
+ attributesInDownloadUrl.cold.1
+ attributesInPallasDynamicAssetId.cold.1
+ getRetryXpcDelayQueue.cold.1
+ lockRecords.lockRecords
+ lockRecords.onceToken
+ logMAAutoAssetVersion.__maAutoAssetLogVersionDispatchOnce
+ plistDecodeClasses.cold.1
+ purposeDisallowedCharacterSet.cold.1
+ purposeIgnoredCharacterSet.cold.1
+ queryDecodeClasses.cold.1
+ setupConnectionState.__maAutoAssetSharedDispatchOnce
+ setupConnectionState.error
+ suAssetTypes.cold.1
+ usingCentralizedCachedelete.cold.1
- +[MAAutoAsset cancelActivityForSelector:completion:].cold.1
- +[MAAutoAsset determineIfAvailable:forAssetSelector:completion:].cold.1
- +[MAAutoAsset eliminateAllForAssetType:completion:].cold.1
- +[MAAutoAsset eliminateAllForSelector:completion:].cold.1
- +[MAAutoAsset eliminatePromotedNeverLockedForSelector:completion:].cold.1
- +[MAAutoAsset endAllPreviousLocksOfReason:forClientName:forAssetSelector:completion:].cold.1
- +[MAAutoAsset endAllPreviousLocksOfSelector:forClientName:completion:].cold.1
- +[MAAutoAsset endPreviousLocksOfReason:forClientName:forAssetSelector:removingLockCount:completion:].cold.1
- +[MAAutoAsset frameworkDispatchQueue]
- +[MAAutoAsset interestInContent:forAssetSelector:withInterestPolicy:completion:].cold.1
- +[MAAutoAsset stageCancelOperation:].cold.1
- +[MAAutoAsset stageDetermineAllAvailable:forTargetBuildVersion:completion:].cold.1
- +[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:].cold.1
- +[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:].cold.1
- +[MAAutoAsset stageDetermineGroupsAvailableForUpdateSync:totalExpectedBytes:error:].cold.1
- +[MAAutoAsset stageDownloadAll:reportingProgress:completion:].cold.1
- +[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:].cold.1
- +[MAAutoAsset stageDownloadGroupsSync:awaitingAllGroups:withStagingTimeout:byGroupAssetsStaged:error:reportingProgress:].cold.1
- +[MAAutoAsset stageEraseAll:].cold.1
- +[MAAutoAsset stagePurgeAll:].cold.1
- +[MAAutoAsset waitOnSemaphore:withDaemonTriggeredTimeout:]
- +[MAAutoAssetAuthorizationPolicy consumeSandboxExtension:forPath:].cold.1
- +[MAAutoAssetAuthorizationPolicy consumeSandboxExtension:forPath:].cold.2
- +[MAAutoAssetControl frameworkDispatchQueue]
- +[MAAutoAssetControl waitOnSemaphore:withTimeout:]
- +[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:].cold.1
- +[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:].cold.1
- +[MAAutoAssetSet frameworkDispatchQueue]
- +[MAAutoAssetSet waitOnSemaphore:withDaemonTriggeredTimeout:]
- +[MAAutoAssetSetControl frameworkDispatchQueue]
- +[MAAutoAssetSetControl waitOnSemaphore:withTimeout:]
- -[MAAsset startDownloadWithExtractor:completion:]
- -[MAAsset startDownloadWithExtractor:options:completion:]
- -[MAAsset startDownloadWithExtractor:options:completionWithError:]
- -[MAAutoAsset _cancelActivityForSelector:]
- -[MAAutoAsset _cancelActivityForSelector:].cold.1
- -[MAAutoAsset _eliminateAllForAssetType:]
- -[MAAutoAsset _eliminateAllForAssetType:].cold.1
- -[MAAutoAsset _eliminateAllForSelector:]
- -[MAAutoAsset _eliminateAllForSelector:].cold.1
- -[MAAutoAsset _eliminatePromotedNeverLockedForSelector:]
- -[MAAutoAsset _eliminatePromotedNeverLockedForSelector:].cold.1
- -[MAAutoAsset _endAllPreviousLocksOfReason:completion:]
- -[MAAutoAsset _endAllPreviousLocksOfReason:completion:].cold.1
- -[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:completion:]
- -[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:completion:].cold.1
- -[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]
- -[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedCheckForNewer:withResponseError:description:completion:]
- -[MAAutoAsset _failedCheckForNewer:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedContinueLockUsage:withResponseError:description:completion:]
- -[MAAutoAsset _failedContinueLockUsage:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedCurrentStatus:withResponseError:description:completion:]
- -[MAAutoAsset _failedCurrentStatus:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedDetermineIfAvailable:withResponseError:description:completion:]
- -[MAAutoAsset _failedDetermineIfAvailable:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedEliminate:withResponseError:description:completion:]
- -[MAAutoAsset _failedEliminate:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedEndLockUsage:withResponseError:description:completion:]
- -[MAAutoAsset _failedEndLockUsage:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedInterestInContent:withResponseError:description:completion:]
- -[MAAutoAsset _failedInterestInContent:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedLockContent:withResponseError:description:completion:]
- -[MAAutoAsset _failedLockContent:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedMapLockedContent:withResponseError:description:completion:]
- -[MAAutoAsset _failedMapLockedContent:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageCancelOperation:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageCancelOperation:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageDownloadAll:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageDownloadAll:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageDownloadGroups:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageDownloadGroups:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStageEraseAll:withResponseError:description:completion:]
- -[MAAutoAsset _failedStageEraseAll:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _failedStagePurgeAll:withResponseError:description:completion:]
- -[MAAutoAsset _failedStagePurgeAll:withResponseError:description:completion:].cold.1
- -[MAAutoAsset _stageCancelOperation:]
- -[MAAutoAsset _stageCancelOperation:].cold.1
- -[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:completion:]
- -[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:completion:].cold.1
- -[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]
- -[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:].cold.1
- -[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:completion:]
- -[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:completion:].cold.1
- -[MAAutoAsset _stageDownloadAll:reportingProgress:completion:]
- -[MAAutoAsset _stageDownloadAll:reportingProgress:completion:].cold.1
- -[MAAutoAsset _stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]
- -[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]
- -[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:].cold.1
- -[MAAutoAsset _stageEraseAll:]
- -[MAAutoAsset _stageEraseAll:].cold.1
- -[MAAutoAsset _stagePurgeAll:]
- -[MAAutoAsset _stagePurgeAll:].cold.1
- -[MAAutoAsset _successCancelActivity:]
- -[MAAutoAsset _successCheckForNewer:completion:]
- -[MAAutoAsset _successCheckForNewer:completion:].cold.1
- -[MAAutoAsset _successContinueLockUsage:completion:]
- -[MAAutoAsset _successContinueLockUsage:completion:].cold.1
- -[MAAutoAsset _successCurrentStatus:completion:]
- -[MAAutoAsset _successCurrentStatus:completion:].cold.1
- -[MAAutoAsset _successDetermineIfAvailable:completion:]
- -[MAAutoAsset _successDetermineIfAvailable:completion:].cold.1
- -[MAAutoAsset _successEliminate:]
- -[MAAutoAsset _successEndLockUsage:completion:]
- -[MAAutoAsset _successInterestInContent:completion:]
- -[MAAutoAsset _successInterestInContent:completion:].cold.1
- -[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]
- -[MAAutoAsset _successMapLockedContent:dueToDesire:completion:]
- -[MAAutoAsset _successStageCancelOperation:]
- -[MAAutoAsset _successStageCancelOperation:].cold.1
- -[MAAutoAsset _successStageDetermineAllAvailable:completion:]
- -[MAAutoAsset _successStageDetermineAllAvailable:completion:].cold.1
- -[MAAutoAsset _successStageDetermineGroupsAvailableForUpdate:completion:]
- -[MAAutoAsset _successStageDetermineGroupsAvailableForUpdate:completion:].cold.1
- -[MAAutoAsset _successStageDownloadAll:completion:]
- -[MAAutoAsset _successStageDownloadAll:completion:].cold.1
- -[MAAutoAsset _successStageDownloadGroups:completion:]
- -[MAAutoAsset _successStageDownloadGroups:completion:].cold.1
- -[MAAutoAsset _successStageEraseAll:]
- -[MAAutoAsset _successStageEraseAll:].cold.1
- -[MAAutoAsset _successStagePurgeAll:]
- -[MAAutoAsset _successStagePurgeAll:].cold.1
- -[MAAutoAsset checkForNewer:withUsagePolicy:withTimeout:completion:].cold.1
- -[MAAutoAsset continueLockUsage:withUsagePolicy:completion:].cold.1
- -[MAAutoAsset currentStatus:].cold.1
- -[MAAutoAsset determineIfAvailable:withTimeout:completion:].cold.1
- -[MAAutoAsset endLockUsage:completion:].cold.1
- -[MAAutoAsset interestInContent:withInterestPolicy:completion:].cold.1
- -[MAAutoAsset lockContent:withUsagePolicy:withTimeout:reportingProgress:completion:].cold.1
- -[MAAutoAsset mapLockedContent:completion:].cold.1
- -[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:completion:]
- -[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:completion:].cold.1
- -[MAAutoAssetControl _availableForStagingAssetSummary:]
- -[MAAutoAssetControl _availableForStagingAssetSummary:].cold.1
- -[MAAutoAssetControl _controlStatistics:completion:]
- -[MAAutoAssetControl _controlStatistics:completion:].cold.1
- -[MAAutoAssetControl _failedControl:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetControl _failedControl:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetControl _failedControlStatistics:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetControl _failedControlStatistics:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetControl _failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetControl _failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetControl _forceGlobalAbandon:completion:]
- -[MAAutoAssetControl _forceGlobalAbandon:completion:].cold.1
- -[MAAutoAssetControl _forceGlobalForget:completion:]
- -[MAAutoAssetControl _forceGlobalForget:completion:].cold.1
- -[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:completion:]
- -[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:completion:].cold.1
- -[MAAutoAssetControl _forceGlobalUnlock:completion:]
- -[MAAutoAssetControl _forceGlobalUnlock:completion:].cold.1
- -[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:completion:]
- -[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:completion:].cold.1
- -[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:completion:]
- -[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:completion:].cold.1
- -[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:completion:]
- -[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:completion:].cold.1
- -[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:]
- -[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:].cold.1
- -[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:]
- -[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:].cold.1
- -[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:completion:]
- -[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:completion:].cold.1
- -[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:completion:]
- -[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:completion:].cold.1
- -[MAAutoAssetControl _successControl:completion:]
- -[MAAutoAssetControl _successControl:completion:].cold.1
- -[MAAutoAssetControl _successControlLockSummary:withLockSummaryEntries:completion:]
- -[MAAutoAssetControl _successControlLockSummary:withLockSummaryEntries:completion:].cold.1
- -[MAAutoAssetControl _successControlStatistics:withControlStatistics:completion:]
- -[MAAutoAssetControl _successControlStatistics:withControlStatistics:completion:].cold.1
- -[MAAutoAssetControl _successControlSummary:withJobSummaryEntries:completion:]
- -[MAAutoAssetControl _successControlSummary:withJobSummaryEntries:completion:].cold.1
- -[MAAutoAssetControl _successSimulateCacheDeleteOperation:withReclaimableSpace:completion:]
- -[MAAutoAssetControl _successSimulateCacheDeleteOperation:withReclaimableSpace:completion:].cold.1
- -[MAAutoAssetControl completionDispatchQueue]
- -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.1
- -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.2
- -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.3
- -[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]
- -[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:].cold.1
- -[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]
- -[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:].cold.1
- -[MAAutoAssetSet _failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSet _failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSet _failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSet _lockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:]
- -[MAAutoAssetSet _lockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:].cold.1
- -[MAAutoAssetSet _shortTermCurrentSetStatus:]
- -[MAAutoAssetSet _shortTermCurrentSetStatusSync:]
- -[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:completion:]
- -[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]
- -[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:completion:]
- -[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:performContentValidation:completion:]
- -[MAAutoAssetSet _shortTermLockAtomicSync:forAtomicInstance:error:]
- -[MAAutoAssetSet _shortTermLockAtomicSync:forAtomicInstance:performContentValidation:error:]
- -[MAAutoAssetSet _shortTermLockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:]
- -[MAAutoAssetSet _successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:completion:]
- -[MAAutoAssetSet _successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:completion:].cold.1
- -[MAAutoAssetSet _successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:completion:]
- -[MAAutoAssetSet _successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:completion:].cold.1
- -[MAAutoAssetSet _successFormSubAtomicInstance:formedSubAtomicInstance:completion:]
- -[MAAutoAssetSet _successFormSubAtomicInstance:formedSubAtomicInstance:completion:].cold.1
- -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:]
- -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:].cold.1
- -[MAAutoAssetSet _successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:completion:]
- -[MAAutoAssetSet _successOperation:forAssetSetIdentifier:completion:]
- -[MAAutoAssetSet _successOperation:forAssetSetIdentifier:completion:].cold.1
- -[MAAutoAssetSet alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:completion:].cold.1
- -[MAAutoAssetSet assetSetForStaging:asEntriesWhenTargeting:completion:].cold.1
- -[MAAutoAssetSet checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:completion:].cold.1
- -[MAAutoAssetSet continueAtomicLock:ofAtomicInstance:withNeedPolicy:completion:].cold.1
- -[MAAutoAssetSet currentSetStatus:].cold.1
- -[MAAutoAssetSet endAtomicLock:ofAtomicInstance:completion:].cold.1
- -[MAAutoAssetSet formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:completion:].cold.1
- -[MAAutoAssetSet lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:].cold.1
- -[MAAutoAssetSet lockAtomicSyncWithContentValidationOption:forAtomicInstance:performContentValidation:error:]
- -[MAAutoAssetSet mapLockedAtomicEntry:forAtomicInstance:mappingSelector:completion:].cold.1
- -[MAAutoAssetSet needForAtomic:withNeedPolicy:completion:].cold.1
- -[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _autoAssetInstanceInfo:completion:]
- -[MAAutoAssetSetControl _autoAssetInstanceInfo:completion:].cold.1
- -[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _failedControl:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSetControl _failedControl:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSetControl _failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSetControl _failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSetControl _failedControlOverview:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSetControl _failedControlOverview:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]
- -[MAAutoAssetSetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:].cold.1
- -[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:completion:]
- -[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:completion:].cold.1
- -[MAAutoAssetSetControl _successControl:completion:]
- -[MAAutoAssetSetControl _successControl:completion:].cold.1
- -[MAAutoAssetSetControl _successControlInstanceInfo:withInstanceInfo:completion:]
- -[MAAutoAssetSetControl _successControlInstanceInfo:withInstanceInfo:completion:].cold.1
- -[MAAutoAssetSetControl _successControlLockSummary:withLockSummaryEntries:completion:]
- -[MAAutoAssetSetControl _successControlLockSummary:withLockSummaryEntries:completion:].cold.1
- -[MAAutoAssetSetControl _successControlOverview:withOverviewEntries:completion:]
- -[MAAutoAssetSetControl _successControlOverview:withOverviewEntries:completion:].cold.1
- -[MAAutoAssetSetControl _successControlSummary:withJobSummaryEntries:completion:]
- -[MAAutoAssetSetControl _successControlSummary:withJobSummaryEntries:completion:].cold.1
- -[MAAutoAssetSetControl completionDispatchQueue]
- -[MAAutoAssetSetShortTermLockInMemoryRecord isCurrentlyValid].cold.1
- -[MAAutoAssetSetShortTermLockInMemoryRecord isCurrentlyValid].cold.2
- -[MAAutoAssetSummary getStringsForSummaryProps:isPersonalized:isPrePersonalized:isGrafted:graftPoint:stageGroup:targetOS:].cold.1
- -[MAAutoAssetSummary setAssetSelector:]
- GCC_except_table102
- GCC_except_table108
- GCC_except_table109
- GCC_except_table113
- GCC_except_table117
- GCC_except_table125
- GCC_except_table132
- GCC_except_table145
- GCC_except_table190
- GCC_except_table20
- GCC_except_table203
- GCC_except_table211
- GCC_except_table223
- GCC_except_table242
- GCC_except_table260
- GCC_except_table271
- GCC_except_table282
- GCC_except_table293
- GCC_except_table30
- GCC_except_table305
- GCC_except_table318
- GCC_except_table33
- GCC_except_table331
- GCC_except_table344
- GCC_except_table356
- GCC_except_table369
- GCC_except_table380
- GCC_except_table39
- GCC_except_table391
- GCC_except_table44
- GCC_except_table46
- GCC_except_table52
- GCC_except_table54
- GCC_except_table60
- GCC_except_table63
- GCC_except_table73
- GCC_except_table78
- GCC_except_table79
- GCC_except_table85
- GCC_except_table86
- GCC_except_table92
- GCC_except_table95
- GCC_except_table99
- OBJC_IVAR_$_MAAutoAssetControl._completionDispatchQueue
- OBJC_IVAR_$_MAAutoAssetSetControl._completionDispatchQueue
- _CFStringCreateWithCString
- _MobileAssetFault.cold.1
- _MobileAssetForceNSLog
- _MobileAssetLog.cold.1
- _MobileAssetLog.cold.2
- _NSLog
- _OBJC_CLASS_$_SUCoreLog
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.966
- __101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.cold.1
- __102-[MAAutoAsset _failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:]_block_invoke.cold.1
- __102-[MAAutoAssetControl _failedControlStatistics:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __102-[MAAutoAssetSet _failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __102-[MAAutoAssetSetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __103-[MAAutoAssetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __103-[MAAutoAssetSetControl _failedControlOverview:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __106-[MAAutoAssetSetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __107-[MAAutoAssetSetControl _failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __112-[MAAutoAssetSet _failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __113-[MAAutoAssetControl _failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __113-[MAAutoAssetSet _failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __114-[MAAutoAssetSet _failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __119-[MAAutoAsset lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:reportingProgress:]_block_invoke.457
- __119-[MAAutoAssetSet _failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __122-[MAAutoAssetSet lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:reportingProgress:]_block_invoke.422
- __123-[MAAutoAssetSet _failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __133+[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke.667
- __144-[MAAutoAssetSet checkAtomicSync:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:discoveredAtomicEntries:error:reportingProgress:]_block_invoke.407
- __26-[MAAsset cancelDownload:]_block_invoke.1096
- __26-[MAAsset purgeWithError:]_block_invoke.1070
- __33-[MAAutoAsset _successEliminate:]_block_invoke.709
- __33-[MAAutoAsset _successEliminate:]_block_invoke.cold.1
- __33-[MAAutoAsset currentStatusSync:]_block_invoke.441
- __36+[MAAutoAsset stageCancelOperation:]_block_invoke.999
- __38-[MAAutoAsset _successCancelActivity:]_block_invoke.702
- __38-[MAAutoAsset _successCancelActivity:]_block_invoke.cold.1
- __39-[MAAutoAssetSet currentSetStatusSync:]_block_invoke.528
- __40+[MAAutoAssetControl forceGlobalUnlock:]_block_invoke.434
- __40-[MAAutoAsset _stageCancelOperationSync]_block_invoke.1005
- __42-[MAXpcManager setClientConnectionHandler]_block_invoke_2.1013
- __46+[MAAutoAssetControl controlStatistics:error:]_block_invoke.292
- __47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.698
- __47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.cold.1
- __47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.cold.2
- __50-[MAAutoAsset connectToServerFrameworkCompletion:]_block_invoke.cold.1
- __51-[MAAutoAsset _newProxyObjectForLockProgressBlock:]_block_invoke.cold.1
- __51-[MAAutoAsset _newProxyObjectForLockProgressBlock:]_block_invoke.cold.2
- __51-[MAAutoAsset _newProxyObjectForLockProgressBlock:]_block_invoke.cold.3
- __52-[MAAutoAsset _newProxyObjectForStageProgressBlock:]_block_invoke.cold.1
- __52-[MAAutoAsset _newProxyObjectForStageProgressBlock:]_block_invoke.cold.2
- __52-[MAAutoAsset _newProxyObjectForStageProgressBlock:]_block_invoke.cold.3
- __53-[MAAutoAssetSet _newProxyObjectForSetProgressBlock:]_block_invoke.cold.1
- __53-[MAAutoAssetSet _newProxyObjectForSetProgressBlock:]_block_invoke.cold.2
- __53-[MAAutoAssetSet _newProxyObjectForSetProgressBlock:]_block_invoke.cold.3
- __53-[MAAutoAssetSet connectToServerFrameworkCompletion:]_block_invoke.cold.1
- __54+[MAAutoAssetControl availableForStagingAssetSummary:]_block_invoke.337
- __54+[MAAutoAssetSetControl assetSetDescriptorInfo:error:]_block_invoke.428
- __56-[MAAutoAsset interestInContentSync:withInterestPolicy:]_block_invoke.376
- __60-[MAAutoAssetSet endAtomicLock:ofAtomicInstance:completion:]_block_invoke.490
- __61+[MAAutoAsset stageDownloadAll:reportingProgress:completion:]_block_invoke.986
- __62+[MAAutoAsset stageDetermineAllAvailableForUpdate:completion:]_block_invoke.950
- __63-[MAAutoAsset _endPreviousLocksOfReasonSync:removingLockCount:]_block_invoke.785
- __63-[MAAutoAsset _successMapLockedContent:dueToDesire:completion:]_block_invoke.692
- __63-[MAAutoAsset _successMapLockedContent:dueToDesire:completion:]_block_invoke.cold.1
- __63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.1
- __63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.2
- __63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.3
- __63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.4
- __64+[MAAutoAsset determineIfAvailable:forAssetSelector:completion:]_block_invoke.772
- __64-[MAAutoAssetSet assetSetForStagingSync:asEntriesWhenTargeting:]_block_invoke.509
- __64-[MASecureManifestStorage _storeManifest:infoPlist:stage:error:]_block_invoke.944
- __65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.915
- __65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.919
- __65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.cold.1
- __73-[MAAutoAsset _failedEliminate:withResponseError:description:completion:]_block_invoke.cold.1
- __75-[MAAutoAsset _failedLockContent:withResponseError:description:completion:]_block_invoke.cold.1
- __76+[MAAutoAssetSetControl knownAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke.295
- __76-[MAAutoAsset _failedEndLockUsage:withResponseError:description:completion:]_block_invoke.cold.1
- __77-[MAAutoAsset _failedCheckForNewer:withResponseError:description:completion:]_block_invoke.cold.1
- __77-[MAAutoAsset _failedCurrentStatus:withResponseError:description:completion:]_block_invoke.cold.1
- __77-[MAAutoAsset _failedStageEraseAll:withResponseError:description:completion:]_block_invoke.cold.1
- __77-[MAAutoAsset _failedStagePurgeAll:withResponseError:description:completion:]_block_invoke.cold.1
- __78-[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]_block_invoke.cold.1
- __79-[MAAutoAsset determineIfAvailableSync:withTimeout:discoveredAttributes:error:]_block_invoke.416
- __80+[MAAutoAsset interestInContent:forAssetSelector:withInterestPolicy:completion:]_block_invoke.760
- __80-[MAAutoAsset _failedMapLockedContent:withResponseError:description:completion:]_block_invoke.cold.1
- __80-[MAAutoAsset _failedStageDownloadAll:withResponseError:description:completion:]_block_invoke.cold.1
- __81-[MAAutoAsset _failedContinueLockUsage:withResponseError:description:completion:]_block_invoke.cold.1
- __81-[MAAutoAsset _failedInterestInContent:withResponseError:description:completion:]_block_invoke.cold.1
- __81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke.956
- __83-[MAAutoAsset _failedStageDownloadGroups:withResponseError:description:completion:]_block_invoke.cold.1
- __84-[MAAutoAsset _failedDetermineIfAvailable:withResponseError:description:completion:]_block_invoke.cold.1
- __84-[MAAutoAsset _failedStageCancelOperation:withResponseError:description:completion:]_block_invoke.cold.1
- __84-[MAAutoAsset _stageDetermineGroupsAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke.940
- __85+[MAAutoAssetControl simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:]_block_invoke.488
- __86-[MAAutoAsset _stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke.993
- __88-[MAAutoAsset checkForNewerSync:withUsagePolicy:withTimeout:discoveredAttributes:error:]_block_invoke.402
- __90-[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:completion:]_block_invoke.cold.1
- __91-[MAAutoAssetSet alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:withNeedPolicy:]_block_invoke.371
- __92-[MAAutoAssetControl _failedControl:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __92-[MAAutoAssetSet mapLockedAtomicEntrySync:forAtomicInstance:mappingSelector:mappedSelector:]_block_invoke.445
- __95-[MAAutoAssetSetControl _failedControl:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke.992
- __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke_2.1001
- __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke_2.990
- __95-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke_2.993
- __96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke.688
- __96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke.cold.1
- __99-[MAAutoAssetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]_block_invoke.cold.1
- __Block_byref_object_copy_.1268
- __Block_byref_object_copy_.658
- __Block_byref_object_copy_.778
- __Block_byref_object_dispose_.1269
- __Block_byref_object_dispose_.659
- __Block_byref_object_dispose_.779
- __MobileAssetFault
- __MobileAssetLog
- __OBJC_$_CLASS_METHODS_MAAutoAsset
- ___102-[MAAutoAsset _failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:]_block_invoke
- ___102-[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke
- ___102-[MAAutoAsset _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke_2
- ___102-[MAAutoAssetControl _failedControlStatistics:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___102-[MAAutoAssetSet _failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___102-[MAAutoAssetSetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___103-[MAAutoAssetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___103-[MAAutoAssetSetControl _failedControlOverview:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___105-[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:]_block_invoke
- ___105-[MAAutoAssetControl _simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:]_block_invoke_2
- ___106-[MAAutoAssetSetControl _failedControlLockSummary:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___107-[MAAutoAssetSetControl _failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___111-[MAAutoAssetSet _lockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:]_block_invoke
- ___112-[MAAutoAssetSet _failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___113-[MAAutoAssetControl _failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___113-[MAAutoAssetSet _failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___114-[MAAutoAssetSet _failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___119-[MAAutoAssetSet _failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___119-[MAAutoAssetSet _successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:completion:]_block_invoke
- ___120-[MAAutoAssetSet _shortTermLockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:]_block_invoke
- ___121-[MAAutoAsset _stageDownloadGroupsSync:awaitingAllGroups:withStagingTimeout:byGroupAssetsStaged:error:reportingProgress:]_block_invoke_3
- ___123-[MAAutoAssetSet _failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___127-[MAAutoAssetSet _endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:]_block_invoke_2
- ___127-[MAAutoAssetSet _endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:]_block_invoke_3
- ___134-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke
- ___134-[MAAutoAssetSet _endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke_2
- ___149-[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke
- ___30-[MAAutoAsset _stageEraseAll:]_block_invoke
- ___30-[MAAutoAsset _stageEraseAll:]_block_invoke_2
- ___30-[MAAutoAsset _stagePurgeAll:]_block_invoke
- ___30-[MAAutoAsset _stagePurgeAll:]_block_invoke_2
- ___32-[MAAutoAsset endLockUsageSync:]_block_invoke_2
- ___32-[MAAutoAsset endLockUsageSync:]_block_invoke_3
- ___33-[MAAutoAsset _stageEraseAllSync]_block_invoke_2
- ___33-[MAAutoAsset _stageEraseAllSync]_block_invoke_3
- ___33-[MAAutoAsset _stagePurgeAllSync]_block_invoke_2
- ___33-[MAAutoAsset _stagePurgeAllSync]_block_invoke_3
- ___33-[MAAutoAsset _successEliminate:]_block_invoke
- ___33-[MAAutoAsset currentStatusSync:]_block_invoke_2
- ___37+[MAAutoAsset frameworkDispatchQueue]_block_invoke
- ___37-[MAAutoAsset _stageCancelOperation:]_block_invoke
- ___37-[MAAutoAsset _stageCancelOperation:]_block_invoke_2
- ___37-[MAAutoAsset _successStageEraseAll:]_block_invoke
- ___37-[MAAutoAsset _successStagePurgeAll:]_block_invoke
- ___38-[MAAutoAsset _successCancelActivity:]_block_invoke
- ___40+[MAAutoAssetControl forceGlobalForget:]_block_invoke_2
- ___40+[MAAutoAssetControl forceGlobalForget:]_block_invoke_3
- ___40+[MAAutoAssetControl forceGlobalUnlock:]_block_invoke_2
- ___40+[MAAutoAssetSet frameworkDispatchQueue]_block_invoke
- ___40-[MAAutoAsset _eliminateAllForSelector:]_block_invoke
- ___40-[MAAutoAsset _eliminateAllForSelector:]_block_invoke_2
- ___40-[MAAutoAsset _stageCancelOperationSync]_block_invoke_2
- ___41+[MAAutoAssetControl forceGlobalAbandon:]_block_invoke_2
- ___41+[MAAutoAssetControl forceGlobalAbandon:]_block_invoke_3
- ___41-[MAAutoAsset _eliminateAllForAssetType:]_block_invoke
- ___41-[MAAutoAsset _eliminateAllForAssetType:]_block_invoke_2
- ___42-[MAAutoAsset _cancelActivityForSelector:]_block_invoke
- ___42-[MAAutoAsset _cancelActivityForSelector:]_block_invoke_2
- ___42-[MAAutoAsset mapLockedContentSync:error:]_block_invoke_2
- ___42-[MAAutoAsset mapLockedContentSync:error:]_block_invoke_3
- ___42-[MAXpcManager setClientConnectionHandler]_block_invoke_2
- ___43-[MAAutoAsset _eliminateAllForSelectorSync]_block_invoke_2
- ___43-[MAAutoAsset _eliminateAllForSelectorSync]_block_invoke_3
- ___44+[MAAutoAssetControl frameworkDispatchQueue]_block_invoke
- ___44-[MAAutoAsset _eliminateAllForAssetTypeSync]_block_invoke_2
- ___44-[MAAutoAsset _eliminateAllForAssetTypeSync]_block_invoke_3
- ___44-[MAAutoAsset _successStageCancelOperation:]_block_invoke
- ___45-[MAAutoAsset _cancelActivityForSelectorSync]_block_invoke_2
- ___45-[MAAutoAsset _cancelActivityForSelectorSync]_block_invoke_3
- ___45-[MAAutoAssetSet _shortTermCurrentSetStatus:]_block_invoke
- ___46+[MAAutoAssetControl controlStatistics:error:]_block_invoke_2
- ___47+[MAAutoAssetSetControl frameworkDispatchQueue]_block_invoke
- ___47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke
- ___48-[MAAutoAsset _endAllPreviousLocksOfReasonSync:]_block_invoke_2
- ___48-[MAAutoAsset _endAllPreviousLocksOfReasonSync:]_block_invoke_3
- ___48-[MAAutoAsset _successCheckForNewer:completion:]_block_invoke
- ___48-[MAAutoAsset _successCurrentStatus:completion:]_block_invoke
- ___49-[MAAutoAssetControl _successControl:completion:]_block_invoke
- ___49-[MAAutoAssetSet _shortTermCurrentSetStatusSync:]_block_invoke
- ___50-[MAAutoAsset connectToServerFrameworkCompletion:]_block_invoke
- ___50-[MAPushNotificationController _serviceConnection]_block_invoke_2
- ___51-[MAAutoAsset _successStageDownloadAll:completion:]_block_invoke
- ___51-[MAAutoAssetSet needForAtomicSync:withNeedPolicy:]_block_invoke_2
- ___51-[MAAutoAssetSet needForAtomicSync:withNeedPolicy:]_block_invoke_3
- ___52-[MAAutoAsset _successContinueLockUsage:completion:]_block_invoke
- ___52-[MAAutoAsset _successInterestInContent:completion:]_block_invoke
- ___52-[MAAutoAssetControl _controlStatistics:completion:]_block_invoke
- ___52-[MAAutoAssetControl _controlStatistics:completion:]_block_invoke_2
- ___52-[MAAutoAssetControl _forceGlobalForget:completion:]_block_invoke
- ___52-[MAAutoAssetControl _forceGlobalForget:completion:]_block_invoke_2
- ___52-[MAAutoAssetControl _forceGlobalUnlock:completion:]_block_invoke
- ___52-[MAAutoAssetControl _forceGlobalUnlock:completion:]_block_invoke_2
- ___52-[MAAutoAssetSetControl _successControl:completion:]_block_invoke
- ___53+[MAAutoAssetControl forceGlobalPurge:forcingUnlock:]_block_invoke_2
- ___53+[MAAutoAssetControl forceGlobalPurge:forcingUnlock:]_block_invoke_3
- ___53-[MAAutoAsset continueLockUsageSync:withUsagePolicy:]_block_invoke_2
- ___53-[MAAutoAsset continueLockUsageSync:withUsagePolicy:]_block_invoke_3
- ___53-[MAAutoAssetControl _forceGlobalAbandon:completion:]_block_invoke
- ___53-[MAAutoAssetControl _forceGlobalAbandon:completion:]_block_invoke_2
- ___53-[MAAutoAssetSet endAtomicLockSync:ofAtomicInstance:]_block_invoke_3
- ___54+[MAAutoAssetControl availableForStagingAssetSummary:]_block_invoke_2
- ___54+[MAAutoAssetSetControl assetSetDescriptorInfo:error:]_block_invoke_2
- ___54-[MAAutoAsset _successStageDownloadGroups:completion:]_block_invoke
- ___55-[MAAutoAsset _endAllPreviousLocksOfReason:completion:]_block_invoke
- ___55-[MAAutoAsset _endAllPreviousLocksOfReason:completion:]_block_invoke_2
- ___55-[MAAutoAsset _successDetermineIfAvailable:completion:]_block_invoke
- ___55-[MAAutoAssetControl _availableForStagingAssetSummary:]_block_invoke
- ___55-[MAAutoAssetControl _availableForStagingAssetSummary:]_block_invoke_2
- ___56-[MAAutoAsset _eliminatePromotedNeverLockedForSelector:]_block_invoke
- ___56-[MAAutoAsset _eliminatePromotedNeverLockedForSelector:]_block_invoke_2
- ___56-[MAAutoAsset interestInContentSync:withInterestPolicy:]_block_invoke_2
- ___56-[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]_block_invoke_2
- ___56-[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]_block_invoke_3
- ___57-[MAAsset startDownloadWithExtractor:options:completion:]_block_invoke
- ___59-[MAAutoAsset _eliminatePromotedNeverLockedForSelectorSync]_block_invoke_2
- ___59-[MAAutoAsset _eliminatePromotedNeverLockedForSelectorSync]_block_invoke_3
- ___59-[MAAutoAssetSetControl _autoAssetInstanceInfo:completion:]_block_invoke
- ___59-[MAAutoAssetSetControl _autoAssetInstanceInfo:completion:]_block_invoke_2
- ___60+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke_3
- ___61-[MAAutoAsset _successStageDetermineAllAvailable:completion:]_block_invoke
- ___62-[MAAutoAsset _stageDownloadAll:reportingProgress:completion:]_block_invoke
- ___62-[MAAutoAsset _stageDownloadAll:reportingProgress:completion:]_block_invoke_2
- ___63-[MAAutoAsset _endPreviousLocksOfReasonSync:removingLockCount:]_block_invoke_2
- ___63-[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]_block_invoke
- ___63-[MAAutoAsset _stageDetermineAllAvailableForUpdate:completion:]_block_invoke_2
- ___63-[MAAutoAsset _successMapLockedContent:dueToDesire:completion:]_block_invoke
- ___63-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]_block_invoke
- ___63-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]_block_invoke_2
- ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke
- ___64-[MAAutoAssetSet assetSetForStagingSync:asEntriesWhenTargeting:]_block_invoke_2
- ___65+[MAAutoAssetControl activeJobSummary:limitedToAssetTypes:error:]_block_invoke_2
- ___65+[MAAutoAssetControl activeJobSummary:limitedToAssetTypes:error:]_block_invoke_3
- ___65-[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:completion:]_block_invoke
- ___65-[MAAutoAssetControl _forceGlobalPurge:forcingUnlock:completion:]_block_invoke_2
- ___66+[MAAutoAssetControl knownAssetSummary:limitedToAssetTypes:error:]_block_invoke_2
- ___66+[MAAutoAssetControl knownAssetSummary:limitedToAssetTypes:error:]_block_invoke_3
- ___66-[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke
- ___66-[MAAutoAsset _stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke_2
- ___67+[MAAutoAssetControl lockedAssetSummary:limitedToAssetTypes:error:]_block_invoke_2
- ___67+[MAAutoAssetControl lockedAssetSummary:limitedToAssetTypes:error:]_block_invoke_3
- ___67+[MAAutoAssetControl stagedAssetSummary:limitedToAssetTypes:error:]_block_invoke_2
- ___67+[MAAutoAssetControl stagedAssetSummary:limitedToAssetTypes:error:]_block_invoke_3
- ___68+[MAAutoAssetControl scheduledJobSummary:limitedToAssetTypes:error:]_block_invoke_2
- ___68+[MAAutoAssetControl scheduledJobSummary:limitedToAssetTypes:error:]_block_invoke_3
- ___69-[MAAutoAssetSet _successOperation:forAssetSetIdentifier:completion:]_block_invoke
- ___70-[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:completion:]_block_invoke
- ___70-[MAAutoAsset _endPreviousLocksOfReason:removingLockCount:completion:]_block_invoke_2
- ___70-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:completion:]_block_invoke
- ___71+[MAAutoAssetControl simulateSetJobOperation:withEndEvent:forSelector:]_block_invoke_2
- ___71+[MAAutoAssetControl simulateSetJobOperation:withEndEvent:forSelector:]_block_invoke_3
- ___71-[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:completion:]_block_invoke
- ___71-[MAAutoAssetControl _activeJobSummary:limitedToAssetTypes:completion:]_block_invoke_2
- ___72-[MAAutoAsset _lockContentStatusProgress:lockForUseError:progressBlock:]_block_invoke
- ___72-[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:completion:]_block_invoke
- ___72-[MAAutoAssetControl _knownAssetSummary:limitedToAssetTypes:completion:]_block_invoke_2
- ___73+[MAAutoAssetSetControl assetSetsOverview:limitedToSetIdentifiers:error:]_block_invoke_2
- ___73+[MAAutoAssetSetControl assetSetsOverview:limitedToSetIdentifiers:error:]_block_invoke_3
- ___73-[MAAutoAsset _failedEliminate:withResponseError:description:completion:]_block_invoke
- ___73-[MAAutoAsset _successStageDetermineGroupsAvailableForUpdate:completion:]_block_invoke
- ___73-[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:completion:]_block_invoke
- ___73-[MAAutoAssetControl _lockedAssetSummary:limitedToAssetTypes:completion:]_block_invoke_2
- ___73-[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:completion:]_block_invoke
- ___73-[MAAutoAssetControl _stagedAssetSummary:limitedToAssetTypes:completion:]_block_invoke_2
- ___73-[MAAutoAssetSet continueAtomicLockSync:ofAtomicInstance:withNeedPolicy:]_block_invoke_2
- ___73-[MAAutoAssetSet continueAtomicLockSync:ofAtomicInstance:withNeedPolicy:]_block_invoke_3
- ___74-[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:completion:]_block_invoke
- ___74-[MAAutoAssetControl _scheduledJobSummary:limitedToAssetTypes:completion:]_block_invoke_2
- ___74-[MAAutoAssetSet _lockAtomicStatusProgress:lockAtomicError:progressBlock:]_block_invoke
- ___75+[MAAutoAssetSetControl activeSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke_2
- ___75+[MAAutoAssetSetControl activeSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke_3
- ___75-[MAAutoAsset _failedLockContent:withResponseError:description:completion:]_block_invoke
- ___76+[MAAutoAssetSetControl knownAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke_2
- ___76-[MAAutoAsset _failedEndLockUsage:withResponseError:description:completion:]_block_invoke
- ___76-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke
- ___76-[MAAutoAsset _stageDetermineAllAvailable:forTargetBuildVersion:completion:]_block_invoke_2
- ___77+[MAAutoAssetSetControl lockedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke_2
- ___77+[MAAutoAssetSetControl lockedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke_3
- ___77+[MAAutoAssetSetControl stagedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke_2
- ___77+[MAAutoAssetSetControl stagedAssetSetSummary:limitedToSetIdentifiers:error:]_block_invoke_3
- ___77-[MAAutoAsset _failedCheckForNewer:withResponseError:description:completion:]_block_invoke
- ___77-[MAAutoAsset _failedCurrentStatus:withResponseError:description:completion:]_block_invoke
- ___77-[MAAutoAsset _failedStageEraseAll:withResponseError:description:completion:]_block_invoke
- ___77-[MAAutoAsset _failedStagePurgeAll:withResponseError:description:completion:]_block_invoke
- ___78+[MAAutoAssetSetControl scheduledSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke_2
- ___78+[MAAutoAssetSetControl scheduledSetJobSummary:limitedToSetIdentifiers:error:]_block_invoke_3
- ___78-[MAAutoAsset _failedCancelActivity:withResponseError:description:completion:]_block_invoke
- ___78-[MAAutoAssetControl _successControlSummary:withJobSummaryEntries:completion:]_block_invoke
- ___79-[MAAutoAsset determineIfAvailableSync:withTimeout:discoveredAttributes:error:]_block_invoke_2
- ___79-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:completion:]_block_invoke
- ___79-[MAAutoAssetSetControl _knownAssetSummary:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___80-[MAAutoAsset _failedMapLockedContent:withResponseError:description:completion:]_block_invoke
- ___80-[MAAutoAsset _failedStageDownloadAll:withResponseError:description:completion:]_block_invoke
- ___80-[MAAutoAsset _stageDownloadAllStatusProgress:stageProgressError:progressBlock:]_block_invoke
- ___80-[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:completion:]_block_invoke
- ___80-[MAAutoAssetSetControl _autoAssetsOverview:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___80-[MAAutoAssetSetControl _successControlOverview:withOverviewEntries:completion:]_block_invoke
- ___81-[MAAutoAsset _failedContinueLockUsage:withResponseError:description:completion:]_block_invoke
- ___81-[MAAutoAsset _failedInterestInContent:withResponseError:description:completion:]_block_invoke
- ___81-[MAAutoAsset _stageDetermineAllAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke_2
- ___81-[MAAutoAssetControl _successControlStatistics:withControlStatistics:completion:]_block_invoke
- ___81-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:completion:]_block_invoke
- ___81-[MAAutoAssetSetControl _activeSetJobSummary:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___81-[MAAutoAssetSetControl _successControlInstanceInfo:withInstanceInfo:completion:]_block_invoke
- ___81-[MAAutoAssetSetControl _successControlSummary:withJobSummaryEntries:completion:]_block_invoke
- ___83-[MAAutoAsset _failedStageDownloadGroups:withResponseError:description:completion:]_block_invoke
- ___83-[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:completion:]_block_invoke
- ___83-[MAAutoAssetControl _simulateSetJobOperation:withEndEvent:forSelector:completion:]_block_invoke_2
- ___83-[MAAutoAssetControl _successControlLockSummary:withLockSummaryEntries:completion:]_block_invoke
- ___83-[MAAutoAssetSet _successFormSubAtomicInstance:formedSubAtomicInstance:completion:]_block_invoke
- ___83-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:completion:]_block_invoke
- ___83-[MAAutoAssetSetControl _lockedAssetSetSummary:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___83-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:completion:]_block_invoke
- ___83-[MAAutoAssetSetControl _stagedAssetSetSummary:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___84-[MAAutoAsset _failedDetermineIfAvailable:withResponseError:description:completion:]_block_invoke
- ___84-[MAAutoAsset _failedStageCancelOperation:withResponseError:description:completion:]_block_invoke
- ___84-[MAAutoAsset _stageDetermineGroupsAvailableForUpdateSync:totalExpectedBytes:error:]_block_invoke_2
- ___84-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:completion:]_block_invoke
- ___84-[MAAutoAssetSetControl _scheduledSetJobSummary:limitedToSetIdentifiers:completion:]_block_invoke_2
- ___85+[MAAutoAssetControl simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:]_block_invoke_2
- ___86-[MAAutoAsset _stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke
- ___86-[MAAutoAsset _stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:]_block_invoke_2
- ___86-[MAAutoAssetSetControl _successControlLockSummary:withLockSummaryEntries:completion:]_block_invoke
- ___88-[MAAutoAsset checkForNewerSync:withUsagePolicy:withTimeout:discoveredAttributes:error:]_block_invoke_2
- ___90-[MAAutoAsset _failedStageDetermineAllAvailable:withResponseError:description:completion:]_block_invoke
- ___91-[MAAutoAssetControl _successSimulateCacheDeleteOperation:withReclaimableSpace:completion:]_block_invoke
- ___91-[MAAutoAssetSet alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:withNeedPolicy:]_block_invoke_2
- ___92-[MAAutoAssetControl _failedControl:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___92-[MAAutoAssetSet _shortTermLockAtomicSync:forAtomicInstance:performContentValidation:error:]_block_invoke
- ___92-[MAAutoAssetSet formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:]_block_invoke_2
- ___92-[MAAutoAssetSet formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:]_block_invoke_3
- ___92-[MAAutoAssetSet mapLockedAtomicEntrySync:forAtomicInstance:mappingSelector:mappedSelector:]_block_invoke_2
- ___93+[MAAutoAssetControl simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:]_block_invoke_2
- ___93+[MAAutoAssetControl simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:]_block_invoke_3
- ___94-[MAAutoAsset _stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:]_block_invoke_2
- ___94-[MAAutoAsset _stageDetermineAllAvailableSync:forTargetBuildVersion:totalExpectedBytes:error:]_block_invoke_3
- ___94-[MAAutoAssetSet _successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:completion:]_block_invoke
- ___95-[MAAutoAssetSet _successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:completion:]_block_invoke
- ___95-[MAAutoAssetSetControl _failedControl:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke
- ___97-[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:]_block_invoke
- ___97-[MAAutoAssetControl _simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:]_block_invoke_2
- ___99-[MAAutoAssetControl _failedControlSummary:withErrorCode:withResponseError:description:completion:]_block_invoke
- ___MAensureExtension_block_invoke.1287
- ___MAsendPMVCancelDownload_block_invoke.1177
- ____MAsendDownloadAsset_block_invoke_2
- ____MAsendPMVCancelDownload_block_invoke_2
- ____MAsendPMVDownload_block_invoke_3
- ___block_descriptor_104_e8_32s40s48r56r64r72r80r_e5_v8?0l
- ___block_descriptor_104_e8_32s40s48s56r64r72r80r88r_e5_v8?0l
- ___block_descriptor_104_e8_32s40s48s56s64r72r80r88r96r_e5_v8?0l
- ___block_descriptor_113_e8_32s40s48s56s64r72r80r88r96r104r_e5_v8?0l
- ___block_descriptor_120_e8_32s40s48s56s64s72r80r88r96r104r112r_e5_v8?0l
- ___block_descriptor_129_e8_32s40s48s56s64s72r80r88r96r104r112r120r_e5_v8?0l
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32r40r48r_e5_v8?0l
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
- ___block_descriptor_60_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0l
- ___block_descriptor_64_e8_32s40bs48bs_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40r48r56r_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40r48r56r_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_64_e8_32s40r48r56r_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
- ___block_descriptor_68_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32r40r48r56r64r_e5_v8?0l
- ___block_descriptor_72_e8_32s40r48r56r64r_e20_v24?0q8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e39_v24?0"MAAutoAssetStatus"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e41_v24?0"MAAutoAssetSelector"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e50_v24?0"MAAutoAssetControlStatistics"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e54_v24?0"MAAutoAssetSetInstanceDescriptor"8"NSError"16l
- ___block_descriptor_72_e8_32s40r48r56r64r_e54_v32?0"NSString"8"MAAutoAssetSelector"16"NSError"24l
- ___block_descriptor_72_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8l
- ___block_descriptor_73_e8_32s40s48bs56bs_e17_v16?0"NSError"8l
- ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0l
- ___block_descriptor_80_e8_32r40r48r56r64r72r_e5_v8?0l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e23_v32?0Q8q16"NSError"24l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e37_v32?0"NSDictionary"8Q16"NSError"24l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e42_v32?0"NSString"8"NSArray"16"NSError"24l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e58_v32?0"MAAutoAssetSelector"8"NSDictionary"16"NSError"24l
- ___block_descriptor_80_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8l
- ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_88_e8_32r40r48r56r64r72r80r_e5_v8?0l
- ___block_descriptor_88_e8_32s40r48r56r64r72r80r_e61_v36?0"MAAutoAssetSelector"8B16"NSDictionary"20"NSError"28l
- ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16l
- ___block_descriptor_88_e8_32s40s48r56r64r72r_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8l
- ___block_descriptor_96_e8_32s40r48r56r64r72r80r88r_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36l
- ___block_descriptor_96_e8_32s40s48r56r64r72r80r88r_e42_v32?0"NSString"8"NSArray"16"NSError"24l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
- ___copy_helper_block_e8_32r40r48r56r64r
- ___copy_helper_block_e8_32r40r48r56r64r72r
- ___copy_helper_block_e8_32r40r48r56r64r72r80r
- ___copy_helper_block_e8_32s40r48r
- ___copy_helper_block_e8_32s40r48r56r
- ___copy_helper_block_e8_32s40r48r56r64r
- ___copy_helper_block_e8_32s40r48r56r64r72r
- ___copy_helper_block_e8_32s40r48r56r64r72r80r
- ___copy_helper_block_e8_32s40r48r56r64r72r80r88r
- ___copy_helper_block_e8_32s40s48r56r64r
- ___copy_helper_block_e8_32s40s48r56r64r72r
- ___copy_helper_block_e8_32s40s48r56r64r72r80r
- ___copy_helper_block_e8_32s40s48r56r64r72r80r88r
- ___copy_helper_block_e8_32s40s48s56r64r
- ___copy_helper_block_e8_32s40s48s56r64r72r80r
- ___copy_helper_block_e8_32s40s48s56r64r72r80r88r
- ___copy_helper_block_e8_32s40s48s56s64r72r80r88r96r
- ___copy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r
- ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r
- ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r120r
- ___destroy_helper_block_e8_32r40r48r56r64r
- ___destroy_helper_block_e8_32r40r48r56r64r72r
- ___destroy_helper_block_e8_32r40r48r56r64r72r80r
- ___destroy_helper_block_e8_32s40r48r56r
- ___destroy_helper_block_e8_32s40r48r56r64r
- ___destroy_helper_block_e8_32s40r48r56r64r72r
- ___destroy_helper_block_e8_32s40r48r56r64r72r80r
- ___destroy_helper_block_e8_32s40r48r56r64r72r80r88r
- ___destroy_helper_block_e8_32s40s48r56r64r
- ___destroy_helper_block_e8_32s40s48r56r64r72r
- ___destroy_helper_block_e8_32s40s48r56r64r72r80r
- ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r
- ___destroy_helper_block_e8_32s40s48s56r64r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r96r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r120r
- ___logDebug_block_invoke
- ___logError_block_invoke
- ___logFault_block_invoke
- ___logInfo_block_invoke
- ___maAutoAssetLogVersionDispatchOnce
- ___maAutoAssetSetSharedConnectionClient
- ___maAutoAssetSharedConnectionClient
- ___maAutoAssetSharedDispatchOnce
- __block_literal_global.1008
- __block_literal_global.1013
- __block_literal_global.1035
- __block_literal_global.1037
- __block_literal_global.1042
- __block_literal_global.1141
- __block_literal_global.1302
- __block_literal_global.1413
- __block_literal_global.17
- __block_literal_global.22
- __block_literal_global.2719
- __block_literal_global.2721
- __block_literal_global.2723
- __block_literal_global.2725
- __block_literal_global.278
- __block_literal_global.281
- __block_literal_global.284
- __block_literal_global.451
- __block_literal_global.504
- __block_literal_global.510
- __block_literal_global.512
- __block_literal_global.532
- __block_literal_global.633
- __block_literal_global.725
- __block_literal_global.731
- __block_literal_global.733
- __block_literal_global.8
- __block_literal_global.807
- __block_literal_global.812
- __block_literal_global.814
- __block_literal_global.816
- __block_literal_global.946
- __block_literal_global.957
- __block_literal_global.992
- __block_literal_global.998
- __hashCFArrayLegacy
- __hashCFArrayNoLegacy
- __hashCFDataOfLength
- __hashCFStringOfLength
- __hashToCFString
- __os_log_debug_impl
- __os_log_error_impl
- __os_log_fault_impl
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _gExclusivelyNSLog
- _gForceNSLog
- _gForceStdOut
- _hashCFDataOfLength.cold.1
- _hashCFStringOfLength.cold.1
- _hashCFStringOfLength.cold.2
- _hashCFStringOfLength.cold.3
- _logDebug
- _logError
- _logFault
- _logInfo
- _objc_msgSend$_activeJobSummary:limitedToAssetTypes:completion:
- _objc_msgSend$_activeSetJobSummary:limitedToSetIdentifiers:completion:
- _objc_msgSend$_autoAssetInstanceInfo:completion:
- _objc_msgSend$_autoAssetsOverview:limitedToSetIdentifiers:completion:
- _objc_msgSend$_availableForStagingAssetSummary:
- _objc_msgSend$_cancelActivityForSelector:
- _objc_msgSend$_controlStatistics:completion:
- _objc_msgSend$_eliminateAllForAssetType:
- _objc_msgSend$_eliminateAllForSelector:
- _objc_msgSend$_eliminateAtomic:awaitingUnlocked:completion:
- _objc_msgSend$_eliminatePromotedNeverLockedForSelector:
- _objc_msgSend$_endAllPreviousLocksOfReason:completion:
- _objc_msgSend$_endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:
- _objc_msgSend$_endPreviousLocksOfReason:removingLockCount:completion:
- _objc_msgSend$_failedCancelActivity:withResponseError:description:completion:
- _objc_msgSend$_failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedCheckForNewer:withResponseError:description:completion:
- _objc_msgSend$_failedContinueLockUsage:withResponseError:description:completion:
- _objc_msgSend$_failedControl:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedControlLockSummary:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedControlOverview:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedControlStatistics:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedControlSummary:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedCurrentStatus:withResponseError:description:completion:
- _objc_msgSend$_failedDetermineIfAvailable:withResponseError:description:completion:
- _objc_msgSend$_failedEliminate:withResponseError:description:completion:
- _objc_msgSend$_failedEndLockUsage:withResponseError:description:completion:
- _objc_msgSend$_failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedInterestInContent:withResponseError:description:completion:
- _objc_msgSend$_failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedLockContent:withResponseError:description:completion:
- _objc_msgSend$_failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedMapLockedContent:withResponseError:description:completion:
- _objc_msgSend$_failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:
- _objc_msgSend$_failedStageCancelOperation:withResponseError:description:completion:
- _objc_msgSend$_failedStageDetermineAllAvailable:withResponseError:description:completion:
- _objc_msgSend$_failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:
- _objc_msgSend$_failedStageDownloadAll:withResponseError:description:completion:
- _objc_msgSend$_failedStageDownloadGroups:withResponseError:description:completion:
- _objc_msgSend$_failedStageEraseAll:withResponseError:description:completion:
- _objc_msgSend$_failedStagePurgeAll:withResponseError:description:completion:
- _objc_msgSend$_forceGlobalAbandon:completion:
- _objc_msgSend$_forceGlobalForget:completion:
- _objc_msgSend$_forceGlobalPurge:forcingUnlock:completion:
- _objc_msgSend$_forceGlobalUnlock:completion:
- _objc_msgSend$_knownAssetSummary:limitedToAssetTypes:completion:
- _objc_msgSend$_knownAssetSummary:limitedToSetIdentifiers:completion:
- _objc_msgSend$_lockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:
- _objc_msgSend$_lockedAssetSetSummary:limitedToSetIdentifiers:completion:
- _objc_msgSend$_lockedAssetSummary:limitedToAssetTypes:completion:
- _objc_msgSend$_scheduledJobSummary:limitedToAssetTypes:completion:
- _objc_msgSend$_scheduledSetJobSummary:limitedToSetIdentifiers:completion:
- _objc_msgSend$_shortTermCurrentSetStatus:
- _objc_msgSend$_shortTermCurrentSetStatusSync:
- _objc_msgSend$_shortTermEndAtomicLockSync:ofAtomicInstance:
- _objc_msgSend$_shortTermLockAtomic:forAtomicInstance:performContentValidation:completion:
- _objc_msgSend$_shortTermLockAtomicSync:forAtomicInstance:performContentValidation:error:
- _objc_msgSend$_shortTermLockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:
- _objc_msgSend$_simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:
- _objc_msgSend$_simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:
- _objc_msgSend$_simulateSetJobOperation:withEndEvent:forSelector:completion:
- _objc_msgSend$_stageCancelOperation:
- _objc_msgSend$_stageDetermineAllAvailable:forTargetBuildVersion:completion:
- _objc_msgSend$_stageDetermineAllAvailableForUpdate:completion:
- _objc_msgSend$_stageDetermineGroupsAvailableForUpdate:completion:
- _objc_msgSend$_stageDownloadAll:reportingProgress:completion:
- _objc_msgSend$_stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:
- _objc_msgSend$_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:
- _objc_msgSend$_stageEraseAll:
- _objc_msgSend$_stagePurgeAll:
- _objc_msgSend$_stagedAssetSetSummary:limitedToSetIdentifiers:completion:
- _objc_msgSend$_stagedAssetSummary:limitedToAssetTypes:completion:
- _objc_msgSend$_successCancelActivity:
- _objc_msgSend$_successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:completion:
- _objc_msgSend$_successCheckForNewer:completion:
- _objc_msgSend$_successContinueLockUsage:completion:
- _objc_msgSend$_successControl:completion:
- _objc_msgSend$_successControlInstanceInfo:withInstanceInfo:completion:
- _objc_msgSend$_successControlLockSummary:withLockSummaryEntries:completion:
- _objc_msgSend$_successControlOverview:withOverviewEntries:completion:
- _objc_msgSend$_successControlStatistics:withControlStatistics:completion:
- _objc_msgSend$_successControlSummary:withJobSummaryEntries:completion:
- _objc_msgSend$_successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:completion:
- _objc_msgSend$_successCurrentStatus:completion:
- _objc_msgSend$_successDetermineIfAvailable:completion:
- _objc_msgSend$_successEliminate:
- _objc_msgSend$_successEndLockUsage:completion:
- _objc_msgSend$_successFormSubAtomicInstance:formedSubAtomicInstance:completion:
- _objc_msgSend$_successInterestInContent:completion:
- _objc_msgSend$_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:
- _objc_msgSend$_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:
- _objc_msgSend$_successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:completion:
- _objc_msgSend$_successMapLockedContent:dueToDesire:completion:
- _objc_msgSend$_successOperation:forAssetSetIdentifier:completion:
- _objc_msgSend$_successSimulateCacheDeleteOperation:withReclaimableSpace:completion:
- _objc_msgSend$_successStageCancelOperation:
- _objc_msgSend$_successStageDetermineAllAvailable:completion:
- _objc_msgSend$_successStageDetermineGroupsAvailableForUpdate:completion:
- _objc_msgSend$_successStageDownloadAll:completion:
- _objc_msgSend$_successStageDownloadGroups:completion:
- _objc_msgSend$_successStageEraseAll:
- _objc_msgSend$_successStagePurgeAll:
- _objc_msgSend$assetSetForStaging:asEntriesWhenTargeting:completion:
- _objc_msgSend$currentSetStatus:
- _objc_msgSend$currentStatus:
- _objc_msgSend$dataUsingEncoding:
- _objc_msgSend$determineIfAvailable:withTimeout:completion:
- _objc_msgSend$endAtomicLock:ofAtomicInstance:completion:
- _objc_msgSend$endLockUsage:completion:
- _objc_msgSend$fileHandleWithStandardOutput
- _objc_msgSend$formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:completion:
- _objc_msgSend$frameworkDispatchQueue
- _objc_msgSend$hashToString:
- _objc_msgSend$lockAtomicSyncWithContentValidationOption:forAtomicInstance:performContentValidation:error:
- _objc_msgSend$mapLockedAtomicEntry:forAtomicInstance:mappingSelector:completion:
- _objc_msgSend$mapLockedContent:completion:
- _objc_msgSend$oslog
- _objc_msgSend$sharedLogger
- _objc_msgSend$startDownloadWithExtractor:options:completion:
- _objc_msgSend$startDownloadWithExtractor:options:completionWithError:
- _objc_msgSend$waitOnSemaphore:withDaemonTriggeredTimeout:
- _objc_msgSend$waitOnSemaphore:withTimeout:
- _objc_msgSend$writeData:
- frameworkDispatchQueue.frameworkQueue
- frameworkDispatchQueue.frameworkQueueOnce
- frameworkDispatchQueue.setFrameworkQueue
- frameworkDispatchQueue.setFrameworkQueueOnce
- logDebug.infoDebug
- logDebug.logDebugOnce
- logError.infoError
- logError.logErrorOnce
- logFault.infoFault
- logFault.logFaultOnce
- logInfo.infoLog
- logInfo.logInfoOnce
CStrings:
+ "                                clientDomainName: %@\n                              assetSetIdentifier: %@\n                          configuredAssetEntries: %@\n                       atomicInstancesDownloaded: %@\n                         catalogCachedAssetSetID: %@\n                       catalogDownloadedFromLive: %@\n                          catalogLastTimeChecked: %@\n                               catalogPostedDate: %@\n                   newerAtomicInstanceDiscovered: %@\n                    newerDiscoveredAtomicEntries: %@\n                        latestDownloadedInstance: %@\n                  latestDowloadedInstanceEntries: %@\n  latestDownloadedAtomicInstanceFromPreSUStaging: %@\n               downloadedCatalogCachedAssetSetID: %@\n             downloadedCatalogDownloadedFromLive: %@\n                downloadedCatalogLastTimeChecked: %@\n                     downloadedCatalogPostedDate: %@\n                            currentNotifications: %@\n                               currentNeedPolicy: %@\n                                 schedulerPolicy: %@\n                                    stagerPolicy: %@\n                      haveReceivedLookupResponse: %@\n           vendingAtomicInstanceForConfigEntries: %@\n                           downloadUserInitiated: %@\n                                downloadProgress: %@\n                          downloadedNetworkBytes: %ld\n                       downloadedFilesystemBytes: %ld\n                                currentLockUsage: %@\n                             selectorsForStaging: %@\n                            availableForUseError: %@\n                               newerVersionError: %@\n"
+ "%-27s %27s %-32lld\n"
+ "%@_SET_ATOMIC_INSTANCE"
+ "%@|estimatedEvictableBytes:%llu"
+ "%@|neededBytes:%llu"
+ "%@|request"
+ "%@|response"
+ "%@|status:%@"
+ "%{public}@ Received XPC error for message sent to mobileassetd"
+ "%{public}@ Received XPC error for message sent to mobileassetd: unexpected xpc type for reply"
+ "%{public}@ doesn't exist, create it"
+ "%{public}@ mobileassetd connection interrupted - retrying sync message: %{public}@"
+ "%{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
+ "%{public}s: Invalid options"
+ "%{public}s: Unable to extract plist object for key %{public}@ from dict"
+ "-_"
+ "/bin/cat"
+ "/usr/bin/tee"
+ "/usr/local/bin/dvdo"
+ "/var/protected/trustd/private/ConstrainedTestAnchors.plist"
+ "1.2.840.113635.100.1.122"
+ ">>>\n                       interestInContent: %lld\n                           checkForNewer: %lld\n                    determineIfAvailable: %lld\n                           currentStatus: %lld\n                             lockContent: %lld\n                        mapLockedContent: %lld\n                       continueLockUsage: %lld\n                            endLockUsage: %lld\n                        endPreviousLocks: %lld\n                     endAllPreviousLocks: %lld\n                 eliminateAllForSelector: %lld\n                eliminateAllForAssetType: %lld\n eliminatePromotedNeverLockedForSelector: %lld\n              stageDetermineAllAvailable: %lld\n                        stageDownloadAll: %lld\n                           stagePurgeAll: %lld\n                           stageEraseAll: %lld\n estimateEvictableBytesForSoftwareUpdate: %lld\n                suspendForSoftwareUpdate: %lld\n                resumeFromSoftwareUpdate: %lld\n    suspendResumeStatusForSoftwareUpdate: %lld\n<<<]"
+ ">>>\nCategory                    Statistic                   Value\n=========================== =========================== ================================\n%@autoJobs                     totalAutoAssetJobsStarted: %lld\nautoJobs                         totalAutoJobsFinished: %lld\nstagerJobs             totalStagerDetermineJobsStarted: %lld\nstagerJobs            totalStagerDetermineJobsFinished: %lld\nstagerJobs              totalStagerDownloadJobsStarted: %lld\nstagerJobs             totalStagerDownloadJobsFinished: %lld\nresumedInFlightJobs           totalResumedInFlightJobs: %lld\nscheduledJobs              totalSchedulerTriggeredJobs: %lld\nfailuresToStartJobs           totalFailuresToStartJobs: %lld\n\npreviously           previouslyDownloadedPatchedAssets: %lld\npreviously            previouslyDownloadedPatchedBytes: %lld\npreviously              previouslyDownloadedFullAssets: %lld\npreviously               previouslyDownloadedFullBytes: %lld\n\ndownloaded                totalDownloadedPatchedAssets: %lld\ndownloaded                 totalDownloadedPatchedBytes: %lld\ndownloaded                   totalDownloadedFullAssets: %lld\ndownloaded                    totalDownloadedFullBytes: %lld\n\nstaged                        totalStagedPatchedAssets: %lld\nstaged                         totalStagedPatchedBytes: %lld\nstaged                           totalStagedFullAssets: %lld\nstaged                            totalStagedFullBytes: %lld\n\nunstaged                    totalUnstagedPatchedAssets: %lld\nunstaged                     totalUnstagedPatchedBytes: %lld\nunstaged                       totalUnstagedFullAssets: %lld\nunstaged                        totalUnstagedFullBytes: %lld\n\npromoted                    totalPromotedPatchedAssets: %lld\npromoted                     totalPromotedPatchedBytes: %lld\npromoted                       totalPromotedFullAssets: %lld\npromoted                        totalPromotedFullBytes: %lld\n\nremoved                      totalRemovedPatchedAssets: %lld\nremoved                       totalRemovedPatchedBytes: %lld\nremoved                         totalRemovedFullAssets: %lld\nremoved                          totalRemovedFullBytes: %lld\n\nfinishedJobs        finishedJobSchedulerNetworkFailure: %lld\nfinishedJobs     finishedJobSchedulerNotNetworkRelated: %lld\nfinishedJobs           finishedJobClientNetworkFailure: %lld\nfinishedJobs        finishedJobClientNotNetworkRelated: %lld\n\ngarbageColection                             performed: %@\ngarbageColection                          reclaimSpace: %@\ngarbageColection                   totalReclaimedSpace: %@\ngarbageColection                 reclaimedV2AssetCount: %ld\ngarbageColection                 reclaimedV2AssetSpace: %@\ngarbageColection                reclaimedUnlockedCount: %ld\ngarbageColection                reclaimedUnlockedSpace: %@\ngarbageColection       reclaimedLockedOverridableCount: %ld\ngarbageColection       reclaimedLockedOverridableSpace: %@\ngarbageColection       reclaimedLockedNeverRemoveCount: %ld\ngarbageColection       reclaimedLockedNeverRemoveSpace: %@\ngarbageColection                  reclaimedStagedCount: %ld\ngarbageColection                  reclaimedStagedSpace: %@\ngarbageColection         reclaimedMetadataBlockedCount: %ld\ngarbageColection         reclaimedMetadataBlockedSpace: %@\n<<<]"
+ "@248@0:8@16@24@32@40@48@56@64@72@80@88@96B104@108@116@124@132@140@148@156@164@172B180B184B188@192q200q208@216@224@232@240"
+ "@252@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188B192@196q204q212@220@228@236@244"
+ "@256@0:8@16@24@32@40@48@56@64@72@80@88@96B104@108@116@124@132@140@148@156@164@172@180B188B192B196@200q208q216@224@232@240@248"
+ "@56@0:8@16@24@32@40@48"
+ "Asked to end lock when no prior lock exists for %@"
+ "Asset load result for %{public}@: %ld (%{public}@)"
+ "Asset load result for %{public}@: %ld (MAQueryHasAllowedDifferences). Found match %{public}@ within allowed differences %{public}@ (actual differences were %{public}@)"
+ "Asset load result for %{public}@: %ld (MAQuerySuccessful). Found %{public}@."
+ "Atomic instance not set on object"
+ "Auto"
+ "AutoSet"
+ "AutoStager"
+ "B32@0:8Q16^@24"
+ "B32@0:8^Q16^@24"
+ "Bad asset meta data, cannot download: %{public}@ %{public}@ %{public}@ %{public}@"
+ "Bad options for asset type: %{public}@ not sending message"
+ "BlockedSuspendedForSoftwareUpdate"
+ "Brain"
+ "Cannot download %{public}@ %{public}@ unless the download is user-initiated (non-discretionary) as the user has turned off background system file updates (check first if nonUserInitiatedDownloadsAllowed)."
+ "Cannot set Pallas URL to a class that is not NSURL (was given an %{public}@), returning MAOperationInvalid."
+ "Certificates"
+ "Client received notification with info %{public}@"
+ "ClientDomain:%@ | SetIdentifier:%@ | AtomicInstance:%@ | LockFile:%@ "
+ "CompatibilityVersionKey"
+ "Config download sync check failure server side: %lld (%{public}@)"
+ "Confirmed data vault for %{public}@"
+ "Could not connect to service %{public}@"
+ "Could not determine state for %{public}@ asset %{public}@; leaving state the same %ld (%{public}@)."
+ "Could not get asset attributes: %{public}@"
+ "Could not get attribute '%{public}@': %{public}@"
+ "Could not get space available for downloading as downloading an ASAsset is deprecated, use MAAsset: %{public}@"
+ "Could not send garbage collection behavior message: %{public}@"
+ "Could not set server URL in daemon: %lld %{public}@ for url: %{public}@"
+ "Created pushnotificationhistory.plist with result %{public}@"
+ "Creating client/daemon connection: %{public}@"
+ "Daemon not ready - retrying download in %d seconds [%{public}@, %{public}@]"
+ "Deprecated ASAsset API is no longer supported"
+ "Deprecated use asutil -nslog instead"
+ "Discarding params as they could not be encoded: %{public}@"
+ "ERROR: Invalid string passed to %{public}s"
+ "Error creating directory: %{public}@"
+ "Error loading history: %{public}@"
+ "Error making connection to mobileassetd: %{public}@"
+ "Error on the cancel download asset reply for %{public}@, response: %ld (%{public}@)"
+ "Error on the download asset reply for %{public}@, response: %ld (%{public}@)"
+ "Error on the download asset reply for %{public}@, response: %ld (%{public}@) due to no xpc message"
+ "Error on the download meta data reply for %{public}@, response: %ld (%{public}@)"
+ "Error on the download meta data reply for %{public}@, response: %ld (%{public}@) due to not having an xpc message"
+ "Error on the purge asset reply for %{public}@, response: %ld (%{public}@) due to XPC_TYPE_ERROR"
+ "Error on the retry download meta data reply for %{public}@, response: %ld (%{public}@)"
+ "Error on the retry download meta data reply for %{public}@, response: %ld (%{public}@) due to not having an xpc message"
+ "Error writing notifications to history: %{public}@"
+ "Error: %{public}@"
+ "Failed to get key: %{public}s"
+ "Failed to get key: %{public}s due to not beinng present"
+ "Failed to open lock file for %@ | Error: %s"
+ "Getting trusted anchors failed with status: %d"
+ "Got the cancel PMV reply, response: %ld (%{public}@)"
+ "Got the cancel catalog reply for %{public}@, response: %ld"
+ "Got the cancel download asset reply for %{public}@, response: %ld (%{public}@)"
+ "Got the config download reply for %{public}@, response: %ld (%{public}@)"
+ "Got the download asset reply for %{public}@, response: %ld (%{public}@)"
+ "Got the download meta data reply for %{public}@, response: %ld (%{public}@)"
+ "Got the purge asset reply for %{public}@, response: %ld (%{public}@)"
+ "Got the query meta data reply for: %{public}@, response: %ld"
+ "Got the retry download meta data reply for %{public}@, response: %ld (%{public}@)"
+ "Hash duplicate found at index %i (%li duplicates found) with entry %@"
+ "KeyManager"
+ "Launching dvdo to set trusted anchors failed with status: %d"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):EVICTABLE_BYTES"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):RESUME"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):STATUS"
+ "MA-AUTO-SUSPEND-RESUME-SU(REPLY):SUSPEND"
+ "MA-AUTO-SUSPEND-RESUME-SU:EVICTABLE_BYTES"
+ "MA-AUTO-SUSPEND-RESUME-SU:RESUME"
+ "MA-AUTO-SUSPEND-RESUME-SU:STATUS"
+ "MA-AUTO-SUSPEND-RESUME-SU:SUSPEND"
+ "MA-auto(%@) | SUCCESS | %@"
+ "MA-auto(%@)| error:%{public}@"
+ "MA-auto(suspend-resume-su-estimateEvictableBytes)"
+ "MA-auto(suspend-resume-su-suspendWithNeededBytes)"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK][RAPID-LOCK]{acquireShortTermLockSync}: %{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK][RAPID-LOCK]{endShortTermLockSync}: %{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockForAtomicInstance}\n[SHORT_FILE_CLOSE][%d] (%{public}@) | lockReason:%{public}@ | WARNING | first lock tracked, but already have tracked file descriptor (%d) | atomicInstanceFilename:%{public}@"
+ "MAAutoAssetSetRapidLock"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateEstimateEvictableBytesResponseInfo"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateInfo"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateRequestInfo"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateStatusResponseInfo"
+ "MAAutoAssetSuspendResumeForSoftwareUpdateSuspendWithNeededBytesRequestInfo"
+ "MAAutoSyncHelpers"
+ "MAThirdPartyCompatibility"
+ "MAThirdPartyCompatibility: Override (%@) provided, with illegal characters."
+ "Manifest"
+ "MobileAsset %{public}@ sendOperationSync %lld (%{public}@) given a non-NSString assetType"
+ "MobileAsset %{public}@ sendOperationSync %lld (%{public}@) given a non-NSString pathToAsset"
+ "MobileAsset Install Asset failed with error: %{public}@"
+ "No file descriptor in entry for lock %@"
+ "Old state: %ld (%{public}@) --> new state: %lld (%{public}@)"
+ "OrganizationsKey"
+ "Preserved ID is not a string: %{public}@ %{public}@"
+ "Preserved IDs value is not an array for: %{public}@"
+ "PushNotification"
+ "Querying with purpose: %{public}@"
+ "Requested to clear trusted 3P CA Data"
+ "Requested to set trusted 3P CA Data"
+ "Result from overrideGarbageCollectionThreshold: %ld (%{public}@)"
+ "Result from purge sync: %ld (%{public}@)"
+ "Result from space check: %ld (%{public}@)"
+ "Result of setDawTokenPath is %lld (%{public}@)"
+ "Result of setDawTokenValue is %lld (%{public}@)"
+ "Result of setPreferences is %lld (%{public}@)"
+ "Resuming"
+ "Retrying download [%{public}@, %{public}@]"
+ "Running"
+ "SHA-1"
+ "SHA-256"
+ "SSO"
+ "SecureMA"
+ "SetJobActive"
+ "SetJobNewerOncePersonalized"
+ "SetJobNoLatestToVend"
+ "SetNotYetServiced"
+ "Shared lock file no longer exists for lock %@"
+ "SoftwareUpdateSuspendResume"
+ "State refresh failure server side: %ld (%{public}@)"
+ "Successful cancel v1 download: %lld %{public}@"
+ "Successfully wrote out trusted anchors, trustd will be bounced."
+ "Suspended"
+ "Suspending"
+ "T@\"MAAutoAssetInfoInstance\",R,&,N"
+ "T@\"MAAutoAssetProgress\",&,V_downloadProgress"
+ "T@\"MAAutoAssetSetProgress\",&,V_downloadProgress"
+ "T@\"NSString\",&,N,V_assetSetAtomicInstance"
+ "T@\"NSString\",&,N,V_previouslyVendedLockedAtomicInstance"
+ "T@\"NSString\",&,N,V_setAtomicInstanceUUID"
+ "T@\"NSString\",&,N,V_shortTermLockFileName"
+ "T@\"SUCoreConnectClient\",R,&,N"
+ "TB,N,V_latestDownloadedAtomicInstanceFromPreSUStaging"
+ "TQ,R,N,V_estimatedEvictableBytes"
+ "TQ,R,N,V_neededBytes"
+ "The asset is installed at: %{public}@"
+ "The download options are %{public}@"
+ "ThirdPartyStagingPathComponent"
+ "This operation may only performed on Apple Internal."
+ "Tq,N,V_estimateEvictableBytesForSoftwareUpdate"
+ "Tq,N,V_resumeFromSoftwareUpdate"
+ "Tq,N,V_suspendForSoftwareUpdate"
+ "Tq,N,V_suspendResumeStatusForSoftwareUpdate"
+ "Tq,R,N,V_status"
+ "Unable to determine ref count for lock %@"
+ "Unable to initialize keyed unarchiver, error: %{public}@"
+ "Unable to launch dvdo to get trusted anchors. %@"
+ "Unable to launch dvdo to set trusted anchors. %@"
+ "Unable to parse existing trusted anchors to property list, will replace: %@"
+ "Unable to to write trusted anchors because pipe failed to close. %@"
+ "Unable to to write trusted anchors to pipe. %@"
+ "Unable to turn trusted anchors into Data. %@"
+ "Unexpected"
+ "Unknown MACancelDownloadResult: %ld (%{public}@)"
+ "V2"
+ "Will retry download meta data for %{public}@, after %ld seconds"
+ "[%{public}s] Failed to query PMV with error: %{public}@"
+ "[%{public}s] Setting include includeSupervised: %{public}@"
+ "[%{public}s] Setting notExpiredBeforeString: %{public}@"
+ "[%{public}s] Setting platformExactMatch: %{public}@"
+ "[%{public}s] Setting postedBeforeString: %{public}@"
+ "[%{public}s] Setting supportedDevicePrefix: %{public}@"
+ "[%{public}s] Setting versionPrefix: %{public}@"
+ "[AUTO-SHORT-TERM][FRAMEWORK][RAPID-LOCK]{acquireShortTermLockSync}"
+ "[AUTO-SHORT-TERM][FRAMEWORK][RAPID-LOCK]{endShortTermLockSync}"
+ "[MAAutoAssetSetShortTermLockInMemoryRecord]: Unable to determine modification date for lock file tracked by %{public}@"
+ "[WARNING] Could not cancel v1 download: %lld %{public}@"
+ "[WARNING] Could not pause asset download: %{public}@"
+ "[WARNING] Could not purge asset: %{public}@"
+ "[WARNING] Could not resume asset download: %{public}@"
+ "[WARNING] Service connection invalidated"
+ "[interestInContent:%lld,checkForNewer:%lld,determineIfAvailable:%lld,currentStatus:%lld,lockContent:%lld,mapLockedContent:%lld,continueLockUsage:%lld,endLockUsage:%lld,endPreviousLocks:%lld,endAllPreviousLocks:%lld|eliminateAllForSelector:%lld|eliminateAllForAssetType:%lld|eliminatePromotedNeverLockedForSelector:%lld|stageDetermineAllAvailable:%lld,stageDownloadAll:%lld,stagePurgeAll:%lld,stageEraseAll:%lld,estimateEvictableBytesForSoftwareUpdate:%lld,suspendForSoftwareUpdate:%lld,resumeFromSoftwareUpdate:%lld,suspendResumeStatusForSoftwareUpdate:%lld]"
+ "_Measurement-SHA256"
+ "_MeasurementAlgorithm"
+ "__addTrustedSigningCertificateAuthority:"
+ "_activeJobSummary:limitedToAssetTypes:isSynchronous:completion:"
+ "_activeSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_alterEntriesRepresentingAtomic:toBeComprisedOfEntries:withNeedPolicy:isSynchronous:completion:"
+ "_assetSetForStaging:asEntriesWhenTargeting:isSynchronous:completion:"
+ "_autoAssetInstanceInfo:isSynchronous:completion:"
+ "_autoAssetsOverview:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_availableForStagingAssetSummaryIsSynchronous:completion:"
+ "_cancelActivityForSelectorIsSynchronous:completion:"
+ "_checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:"
+ "_checkForNewer:withUsagePolicy:withTimeout:isSynchronous:completion:"
+ "_continueAtomicLock:ofAtomicInstance:withNeedPolicy:isSynchronous:completion:"
+ "_continueLockUsage:withUsagePolicy:isSynchronous:completion:"
+ "_controlStatistics:isSynchronous:completion:"
+ "_currentSetStatusIsSynchronous:completion:"
+ "_currentStatusIsSynchronous:completion:"
+ "_determineIfAvailable:withTimeout:isSynchronous:completion:"
+ "_eliminateAllForAssetTypeIsSynchronous:completion:"
+ "_eliminateAllForSelectorIsSynchronous:completion:"
+ "_eliminateAtomic:awaitingUnlocked:isSynchronous:completion:"
+ "_eliminatePromotedNeverLockedForSelectorIsSynchronous:completion:"
+ "_endAllPreviousLocksOfReason:isSynchronous:completion:"
+ "_endAtomicLock:ofAtomicInstance:isSynchronous:completion:"
+ "_endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:isSynchronous:completion:"
+ "_endLockUsage:isSynchronous:completion:"
+ "_endPreviousLocksOfReason:removingLockCount:isSynchronous:completion:"
+ "_estimateEvictableBytesForSoftwareUpdate"
+ "_estimateEvictableBytesForSoftwareUpdateIsSynchronous:completion:"
+ "_estimatedEvictableBytes"
+ "_failedCancelActivity:withResponseError:description:isSynchronous:completion:"
+ "_failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedCheckForNewer:withResponseError:description:isSynchronous:completion:"
+ "_failedContinueLockUsage:withResponseError:description:isSynchronous:completion:"
+ "_failedControl:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedControlInstanceInfo:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedControlLockSummary:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedControlOverview:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedControlStatistics:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedControlSummary:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedCurrentStatus:withResponseError:description:isSynchronous:completion:"
+ "_failedDetermineIfAvailable:withResponseError:description:isSynchronous:completion:"
+ "_failedEliminate:withResponseError:description:isSynchronous:completion:"
+ "_failedEndLockUsage:withResponseError:description:isSynchronous:completion:"
+ "_failedFormSubAtomicInstance:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedInterestInContent:withResponseError:description:isSynchronous:completion:"
+ "_failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedLockContent:withResponseError:description:isSynchronous:completion:"
+ "_failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedMapLockedContent:withResponseError:description:isSynchronous:completion:"
+ "_failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_failedStageCancelOperation:withResponseError:description:isSynchronous:completion:"
+ "_failedStageDetermineAllAvailable:withResponseError:description:isSynchronous:completion:"
+ "_failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:isSynchronous:completion:"
+ "_failedStageDownloadAll:withResponseError:description:isSynchronous:completion:"
+ "_failedStageDownloadGroups:withResponseError:description:isSynchronous:completion:"
+ "_failedStageEraseAll:withResponseError:description:isSynchronous:completion:"
+ "_failedStagePurgeAll:withResponseError:description:isSynchronous:completion:"
+ "_forceGlobalAbandon:isSynchronous:completion:"
+ "_forceGlobalForget:isSynchronous:completion:"
+ "_forceGlobalPurge:forcingUnlock:isSynchronous:completion:"
+ "_forceGlobalUnlock:isSynchronous:completion:"
+ "_formSubAtomicInstance:fromAtomicInstance:toBeComprisedOfEntries:isSynchronous:completion:"
+ "_initForAssetType:withAssetSpecifier:matchingAssetVersion:usingDecryptionKey:setAtomicInstanceUUID:"
+ "_interestInContent:withInterestPolicy:isSynchronous:completion:"
+ "_knownAssetSummary:limitedToAssetTypes:isSynchronous:completion:"
+ "_knownAssetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_latestDownloadedAtomicInstanceFromPreSUStaging"
+ "_lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:isSynchronous:completion:"
+ "_lockAtomicSync:forAtomicInstance:performContentValidation:error:"
+ "_lockContent:withUsagePolicy:withTimeout:reportingProgress:isSynchronous:completion:"
+ "_lockedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_lockedAssetSummary:limitedToAssetTypes:isSynchronous:completion:"
+ "_mapLockedAtomicEntry:forAtomicInstance:mappingSelector:isSynchronous:completion:"
+ "_mapLockedContent:isSynchronous:completion:"
+ "_needForAtomic:withNeedPolicy:isSynchronous:completion:"
+ "_neededBytes"
+ "_previouslyVendedLockedAtomicInstance"
+ "_privateStateQueue"
+ "_resumeFromSoftwareUpdate"
+ "_resumeFromSoftwareUpdateIsSynchronous:completion:"
+ "_scheduledJobSummary:limitedToAssetTypes:isSynchronous:completion:"
+ "_scheduledSetJobSummary:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:"
+ "_setAtomicInstanceUUID"
+ "_shortTermCurrentSetStatusIsSynchronous:completion:"
+ "_shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:"
+ "_shortTermLockAtomic:forAtomicInstance:performContentValidation:isSynchronous:completion:"
+ "_shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:"
+ "_shortTermLockFileName"
+ "_simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:isSynchronous:completion:"
+ "_simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:isSynchronous:completion:"
+ "_simulateSetJobOperation:withEndEvent:forSelector:isSynchronous:completion:"
+ "_stageCancelOperationIsSynchronous:completion:"
+ "_stageDetermineAllAvailable:forTargetBuildVersion:isSynchronous:completion:"
+ "_stageDetermineAllAvailableForUpdate:isSynchronous:completion:"
+ "_stageDetermineGroupsAvailableForUpdate:isSynchronous:completion:"
+ "_stageDownloadAll:reportingProgress:isSynchronous:completion:"
+ "_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:isSynchronous:completion:"
+ "_stageEraseAllIsSynchronous:completion:"
+ "_stagePurgeAllIsSynchronous:completion:"
+ "_stagedAssetSetSummary:limitedToSetIdentifiers:isSynchronous:completion:"
+ "_stagedAssetSummary:limitedToAssetTypes:isSynchronous:completion:"
+ "_status"
+ "_successCancelActivityIsSynchronous:completion:"
+ "_successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:isSynchronous:completion:"
+ "_successCheckForNewer:isSynchronous:completion:"
+ "_successContinueLockUsage:isSynchronous:completion:"
+ "_successControl:isSynchronous:completion:"
+ "_successControlInstanceInfo:withInstanceInfo:isSynchronous:completion:"
+ "_successControlLockSummary:withLockSummaryEntries:isSynchronous:completion:"
+ "_successControlOverview:withOverviewEntries:isSynchronous:completion:"
+ "_successControlStatistics:withControlStatistics:isSynchronous:completion:"
+ "_successControlSummary:withJobSummaryEntries:isSynchronous:completion:"
+ "_successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:isSynchronous:completion:"
+ "_successCurrentStatus:isSynchronous:completion:"
+ "_successDetermineIfAvailable:isSynchronous:completion:"
+ "_successEliminateIsSynchronous:completion:"
+ "_successEndLockUsage:isSynchronous:completion:"
+ "_successFormSubAtomicInstance:formedSubAtomicInstance:isSynchronous:completion:"
+ "_successInterestInContent:isSynchronous:completion:"
+ "_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:"
+ "_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:isSynchronous:completion:"
+ "_successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:isSynchronous:completion:"
+ "_successMapLockedContent:dueToDesire:isSynchronous:completion:"
+ "_successOperation:forAssetSetIdentifier:isSynchronous:completion:"
+ "_successSimulateCacheDeleteOperation:withReclaimableSpace:isSynchronous:completion:"
+ "_successStageCancelOperationIsSynchronous:completion:"
+ "_successStageDetermineAllAvailable:isSynchronous:completion:"
+ "_successStageDetermineGroupsAvailableForUpdate:isSynchronous:completion:"
+ "_successStageDownloadAll:isSynchronous:completion:"
+ "_successStageDownloadGroups:isSynchronous:completion:"
+ "_successStageEraseAllIsSynchronous:completion:"
+ "_successStagePurgeAllIsSynchronous:completion:"
+ "_suspendForSoftwareUpdate"
+ "_suspendForSoftwareUpdateIsSynchronous:neededBytes:completion:"
+ "_suspendResumeStatusForSoftwareUpdate"
+ "_suspendResumeStatusForSoftwareUpdateIsSynchronous:completion:"
+ "_thirdPartyAssetTypeStorage"
+ "acquireShortTermLockSync"
+ "addCharactersInString:"
+ "addTrustedSigningCertificateAuthority:"
+ "alphanumericCharacterSet"
+ "arrayWithObjects:"
+ "assetId: %{public}@ State: %ld attributes: %{public}@ purpose: %{public}@"
+ "auto(suspend-resume-su-status)"
+ "base64EncodedStringWithOptions:"
+ "checkForNewer:"
+ "checkLockFileValidity"
+ "clearAllTrustedSigningCertificateAuthorities"
+ "closeAndReturnError:"
+ "com.apple.MobileAsset"
+ "com.apple.MobileAsset.preferencesDomain"
+ "compatibilityVersionForAssetType:"
+ "connectClientSendServerMessage:proxyObject:replyQueue:isSynchronous:withReply:"
+ "connectClientSendSynchronousServerMessage:proxyObject:errorPtr:"
+ "connection cleared: %{public}@"
+ "continueLockUsage:"
+ "could not encode query params: %{public}@"
+ "createErrorFromMessage: Successfully created error: %{public}@"
+ "createErrorFromMessage: unarchiver cannot be created: %{public}@"
+ "dataWithPropertyList:format:options:error:"
+ "defaultThirdPartyServerURLForAssetType:"
+ "determineIfAvailable:"
+ "endAllPreviousLocks:"
+ "endLockUsage:"
+ "endPreviousLocks:"
+ "endShortTermLockSync"
+ "estEvictableBytesForSU:"
+ "estimateEvictableBytesForSoftwareUpdate"
+ "estimateEvictableBytesForSoftwareUpdateSyncWithReturnEvictableBytesPtr:returnEstimateEvictableBytesErrorPtr:"
+ "estimateEvictableBytesForSoftwareUpdateWithCompletion:"
+ "estimatedEvictableBytes"
+ "failed to alloc/init clientID"
+ "failed to alloc/init message"
+ "failed to alloc/init messageInfo"
+ "failed to alloc/init requestInfo"
+ "failed to derive info"
+ "fileHandleForReading"
+ "fileHandleForWriting"
+ "fileHandleWithNullDevice"
+ "getBaseAssetRepositoryPath"
+ "getLocalPath asset %{public}@ %{public}@ local path is '%{public}@'%{public}@%{public}@"
+ "getLocalPath asset %{public}@ %{public}@%{public}@%{public}@"
+ "getObjectFromMessage: could not decode object for key: %{public}s error: %{public}@"
+ "https://mesu.apple.com/3p/%@/assets/%@/%@/"
+ "https://mesu.apple.com/3p/assets/%@/%@/"
+ "https://mesu.apple.com/3p/staging/assets/%@/%@/"
+ "infoInstance"
+ "init:assetSetIdentifier:assetSetAtomicInstance:"
+ "initForSetAtomicInstanceUUID:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withPreviouslyVendedLockedAtomicInstance:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initWitNeededBytes:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "initWithEstimatedEvictableBytes:"
+ "initWithStatus:"
+ "interestInContent:"
+ "isBootedOSSecureInternal"
+ "isThirdPartyAssetType:"
+ "latestDownloadedAtomicInstanceFromPreSUStaging"
+ "launchAndReturnError:"
+ "load data is null skipping: %{public}@"
+ "load key is invalid skipping: %{public}@"
+ "load object is not a %{public}@: %{public}@"
+ "load object is null skipping: %{public}@"
+ "load rawData is null skipping: %{public}@"
+ "lockContent:"
+ "lockRecords"
+ "lockedInfoInstance"
+ "ma-auto-sync-helper/xpc-async"
+ "ma-auto-sync-helper/xpc-sync"
+ "ma-auto-sync-helper/xpc-sync total=%.3f (xpc=%.3f, queue=%.3f, reply=%.3f)"
+ "maAutoAssetSharedConnectionClient"
+ "macos"
+ "missing connect client"
+ "missing request info"
+ "missing response"
+ "missing response.message"
+ "neededBytes"
+ "newServerMessageClasses:"
+ "numberWithInt:"
+ "permitThirdPartySigningForAssetType:outOrganizations:"
+ "pipe"
+ "precomposedStringWithCanonicalMapping"
+ "previouslyVendedLockedAtomicInstance"
+ "propertyListWithData:options:format:error:"
+ "q24@0:8^@16"
+ "rapidLockAssetSetAtomicInstance"
+ "rapidLockAssetSetAtomicShortTermLockFileName"
+ "rapidLockAssetSetIdentifier"
+ "rapidLockClientDomainName"
+ "readDataToEndOfFile"
+ "resumeFromSU:"
+ "resumeFromSoftwareUpdate"
+ "resumeFromSoftwareUpdateSyncWithReturnResumeErrorPtr:"
+ "resumeFromSoftwareUpdateWithCompletion:"
+ "setArguments:"
+ "setAssetSetAtomicInstance:"
+ "setAtomicInstanceUUID"
+ "setAtomicInstanceUUID:%@"
+ "setByAddingObject:"
+ "setEstimateEvictableBytesForSoftwareUpdate:"
+ "setExecutableURL:"
+ "setLatestDownloadedAtomicInstanceFromPreSUStaging:"
+ "setObject:atIndexedSubscript:"
+ "setPreviouslyVendedLockedAtomicInstance:"
+ "setResumeFromSoftwareUpdate:"
+ "setSetAtomicInstanceUUID:"
+ "setShortTermLockFileName:"
+ "setStandardInput:"
+ "setStandardOutput:"
+ "setSuspendForSoftwareUpdate:"
+ "setSuspendResumeStatusForSoftwareUpdate:"
+ "setupConnectionState"
+ "sharedDevice"
+ "shortTermLockFileName"
+ "stageDetermineAllAvailable:"
+ "stageDownloadAll:"
+ "status"
+ "suspendForSU:"
+ "suspendForSoftwareUpdate"
+ "suspendForSoftwareUpdateSyncWithNeededBytes:returnSuspendErrorPtr:"
+ "suspendForSoftwareUpdateWithNeededBytes:completion:"
+ "suspendResumeForSU"
+ "suspendResumeForSoftwareUpdate"
+ "suspendResumeStatusForSU:"
+ "suspendResumeStatusForSoftwareUpdate"
+ "suspendResumeStatusForSoftwareUpdateSyncWithReturnStatusErrorPtr:"
+ "suspendResumeStatusForSoftwareUpdateWithCompletion:"
+ "suspendWithNeededBytes"
+ "terminate"
+ "terminationStatus"
+ "unable to find responseInfo"
+ "unexpected responseMessage"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"MAAutoAssetSuspendResumeForSoftwareUpdateResponseInfo\"8@\"NSError\"16"
+ "v28@?0B8Q12@\"NSError\"20"
+ "v32@0:8B16B20@?24"
+ "v32@0:8Q16@?24"
+ "v36@0:8B16Q20@?28"
+ "v40@0:8@16B24B28@?32"
+ "v40@0:8B16@20B28@?32"
+ "v44@0:8@16q24B32@?36"
+ "v44@0:8q16@?24B32@?36"
+ "v48@0:8@16@24B32B36@?40"
+ "v48@0:8@16i24^@28B36@?40"
+ "v48@0:8@16i24q28B36@?40"
+ "v52@0:8@16@24q32B40@?44"
+ "v52@0:8B16@20@28@36@?44"
+ "v52@0:8q16@24@32B40@?44"
+ "v52@0:8q16q24@32B40@?44"
+ "v56@0:8@16B24q28@?36B44@?48"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v60@0:8@16@24q32@?40B48@?52"
+ "v60@0:8@16q24@32@40B48@?52"
+ "v68@0:8@16@24@32q40@?48B56@?60"
+ "v68@0:8@16@24q32@40@48B56@?60"
+ "v72@0:8@16@24B32@36q44@?52B60@?64"
+ "v76@0:8@16@24@32@40@48@56B64@?68"
+ "v76@0:8@16@24@32@40@48q56B64@?68"
+ "waitUntilExit"
+ "writeData:error:"
+ "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) unable to consume sandbox extension with errno %{public}s (%d) for path %{public}@"
+ "{_MAsendSetPreferences} Encoding error: %{public}@"
+ "{assembleTaskDescriptorWithPurposeAndAutoAssetJobID} invalid autoAssetJobID(ignored):%{public}@"
- "                      clientDomainName: %@\n                    assetSetIdentifier: %@\n                configuredAssetEntries: %@\n             atomicInstancesDownloaded: %@\n               catalogCachedAssetSetID: %@\n             catalogDownloadedFromLive: %@\n                catalogLastTimeChecked: %@\n                     catalogPostedDate: %@\n         newerAtomicInstanceDiscovered: %@\n          newerDiscoveredAtomicEntries: %@\n              latestDownloadedInstance: %@\n        latestDowloadedInstanceEntries: %@\n     downloadedCatalogCachedAssetSetID: %@\n   downloadedCatalogDownloadedFromLive: %@\n      downloadedCatalogLastTimeChecked: %@\n           downloadedCatalogPostedDate: %@\n                  currentNotifications: %@\n                     currentNeedPolicy: %@\n                       schedulerPolicy: %@\n                          stagerPolicy: %@\n            haveReceivedLookupResponse: %@\n vendingAtomicInstanceForConfigEntries: %@\n                 downloadUserInitiated: %@\n                      downloadProgress:\n%@\n                downloadedNetworkBytes: %ld\n             downloadedFilesystemBytes: %ld\n                      currentLockUsage: %@\n                   selectorsForStaging: %@\n                  availableForUseError: %@\n                     newerVersionError: %@\n"
- "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
- "%@ Received XPC error for message sent to mobileassetd"
- "%@ Received XPC error for message sent to mobileassetd: unexpected xpc type for reply"
- "%@ doesn't exist, create it"
- "%@ mobileassetd connection interrupted - retrying sync message: %@"
- "%s: Extracted object for key %@ is invalid/not a dictionary"
- "%s: Invalid options"
- "%s: Unable to extract plist object for key %@ from dict"
- "%{public}s: %{public}@"
- "+[MAAsset cancelCatalogDownload:withPurpose:then:]_block_invoke"
- "+[MAAsset getLoadResultFromMessage:]"
- "+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke"
- "+[MAAsset startCatalogDownload:options:completionWithError:]_block_invoke_3"
- "-[ASAsset _downloadWithOptions:shouldFireCallback:]"
- "-[ASAsset _downloadWithOptions:shouldFireCallback:]_block_invoke"
- "-[ASAsset _getLocalAttribute:]"
- "-[ASAsset adjustDownloadOptions:completion:]"
- "-[ASAsset cancelDownload:]"
- "-[ASAsset cancelDownload:]_block_invoke_2"
- "-[ASAsset cancelDownloadAndReturnError:]"
- "-[ASAsset garbageCollectionBehavior]"
- "-[ASAsset installDate]"
- "-[ASAsset pauseDownload:]"
- "-[ASAsset pauseDownloadAndReturnError:]"
- "-[ASAsset purge:]"
- "-[ASAsset purgeAndReturnError:]"
- "-[ASAsset requiredDiskSpaceIsAvailableForDownloadOptions:requiredBytes:error:]"
- "-[ASAsset resumeDownload:]"
- "-[ASAsset resumeDownloadAndReturnError:]"
- "-[ASAsset setGarbageCollectionBehavior:]"
- "-[ASAsset(ASAssetInternal) fullAttributes]"
- "-[MAAsset cancelDownload:]"
- "-[MAAsset cancelDownload:]_block_invoke"
- "-[MAAsset commonAssetDownload:options:then:]"
- "-[MAAsset commonAssetDownload:options:then:]_block_invoke"
- "-[MAAsset configDownload:completion:]_block_invoke"
- "-[MAAsset logAsset]"
- "-[MAAsset purgeWithError:]_block_invoke"
- "-[MAAssetQuery addKeyValueArray:with:]"
- "-[MAAssetQuery getResultsFromMessage:]"
- "-[MAAssetQuery queryMetaDataSync]"
- "-[MAAutoAssetPushNotificationHistory _loadHistoryWithError:]"
- "-[MAAutoAssetPushNotificationHistory addNotificationsToHistory:withError:]"
- "-[MAAutoAssetPushNotificationHistory init]"
- "-[MADownloadConfig logConfig]"
- "-[MADownloadOptions initWithCoder:]"
- "-[MADownloadOptions initWithPlist:]"
- "-[MADownloadOptions logOptions]"
- "-[MAPushNotificationController _serviceConnection]"
- "-[MAPushNotificationController _serviceConnection]_block_invoke"
- "-[MAPushNotificationController _serviceConnection]_block_invoke_2"
- "-[MAPushNotificationController asyncProxy]_block_invoke"
- "-[MAPushNotificationController didReceivePushNotificationWithInfo:]"
- "-[MAPushNotificationController synchronousProxy]_block_invoke"
- "-[MASecureManifestStorage _serviceConnectionWithError:]"
- "-[MASecureMobileAssetTypes _loadTypes]"
- "-[MAXpcManager clearConnection:]"
- "-[MAXpcManager ensureConnection]"
- "-[MAXpcManager notifyClientsOfProgress:]_block_invoke"
- "-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke"
- "-[MAXpcManager sendAsync:clientHandler:taskDescriptor:withRetry:retryInitialReconnectionCount:]_block_invoke_2"
- "-[MAXpcManager sendSync:gettingResponseCode:codeForXpcError:loggingName:]"
- "-[MAXpcManager sendSync:gettingResponseCode:codeForXpcError:loggingName:]_block_invoke"
- "-[MAXpcManager setClientConnectionHandler]_block_invoke"
- "-[MAXpcManager setClientConnectionHandler]_block_invoke_2"
- ">>>\n                       interestInContent: %lld\n                           checkForNewer: %lld\n                    determineIfAvailable: %lld\n                           currentStatus: %lld\n                             lockContent: %lld\n                        mapLockedContent: %lld\n                       continueLockUsage: %lld\n                            endLockUsage: %lld\n                        endPreviousLocks: %lld\n                     endAllPreviousLocks: %lld\n                 eliminateAllForSelector: %lld\n                eliminateAllForAssetType: %lld\n eliminatePromotedNeverLockedForSelector: %lld\n              stageDetermineAllAvailable: %lld\n                        stageDownloadAll: %lld\n                           stagePurgeAll: %lld\n                           stageEraseAll: %lld\n<<<]"
- ">>>\nCategory                    Statistic                   Value\n=========================== =========================== ================================\ntotalClientRequests                  interestInContent: %lld\ntotalClientRequests                      checkForNewer: %lld\ntotalClientRequests               determineIfAvailable: %lld\ntotalClientRequests                      currentStatus: %lld\ntotalClientRequests                        lockContent: %lld\ntotalClientRequests                  continueLockUsage: %lld\ntotalClientRequests                       endLockUsage: %lld\ntotalClientRequests                   endPreviousLocks: %lld\ntotalClientRequests                endAllPreviousLocks: %lld\ntotalClientRequests         stageDetermineAllAvailable: %lld\ntotalClientRequests                   stageDownloadAll: %lld\ntotalClientRequests                      stagePurgeAll: %lld\ntotalClientRequests                      stageEraseAll: %lld\n\ntotalClientRepliesSuccess            interestInContent: %lld\ntotalClientRepliesSuccess                checkForNewer: %lld\ntotalClientRepliesSuccess         determineIfAvailable: %lld\ntotalClientRepliesSuccess                currentStatus: %lld\ntotalClientRepliesSuccess                  lockContent: %lld\ntotalClientRepliesSuccess            continueLockUsage: %lld\ntotalClientRepliesSuccess                 endLockUsage: %lld\ntotalClientRepliesSuccess             endPreviousLocks: %lld\ntotalClientRepliesSuccess          endAllPreviousLocks: %lld\ntotalClientRepliesSuccess   stageDetermineAllAvailable: %lld\ntotalClientRepliesSuccess             stageDownloadAll: %lld\ntotalClientRepliesSuccess                stagePurgeAll: %lld\n\ntotalClientRepliesFailure            interestInContent: %lld\ntotalClientRepliesFailure                checkForNewer: %lld\ntotalClientRepliesFailure         determineIfAvailable: %lld\ntotalClientRepliesFailure                currentStatus: %lld\ntotalClientRepliesFailure                  lockContent: %lld\ntotalClientRepliesFailure            continueLockUsage: %lld\ntotalClientRepliesFailure                 endLockUsage: %lld\ntotalClientRepliesFailure             endPreviousLocks: %lld\ntotalClientRepliesFailure          endAllPreviousLocks: %lld\ntotalClientRepliesFailure   stageDetermineAllAvailable: %lld\ntotalClientRepliesFailure             stageDownloadAll: %lld\ntotalClientRepliesFailure                stagePurgeAll: %lld\n\ntotalQueuedClientRequests            interestInContent: %lld\ntotalQueuedClientRequests                checkForNewer: %lld\ntotalQueuedClientRequests         determineIfAvailable: %lld\ntotalQueuedClientRequests                currentStatus: %lld\ntotalQueuedClientRequests                  lockContent: %lld\ntotalQueuedClientRequests            continueLockUsage: %lld\ntotalQueuedClientRequests                 endLockUsage: %lld\ntotalQueuedClientRequests             endPreviousLocks: %lld\ntotalQueuedClientRequests          endAllPreviousLocks: %lld\ntotalQueuedClientRequests   stageDetermineAllAvailable: %lld\ntotalQueuedClientRequests             stageDownloadAll: %lld\ntotalQueuedClientRequests                stagePurgeAll: %lld\n\ntotalDequeuedClientRequests          interestInContent: %lld\ntotalDequeuedClientRequests              checkForNewer: %lld\ntotalDequeuedClientRequests       determineIfAvailable: %lld\ntotalDequeuedClientRequests              currentStatus: %lld\ntotalDequeuedClientRequests                lockContent: %lld\ntotalDequeuedClientRequests          continueLockUsage: %lld\ntotalDequeuedClientRequests               endLockUsage: %lld\ntotalDequeuedClientRequests           endPreviousLocks: %lld\ntotalDequeuedClientRequests        endAllPreviousLocks: %lld\ntotalDequeuedClientRequests stageDetermineAllAvailable: %lld\ntotalDequeuedClientRequests           stageDownloadAll: %lld\ntotalDequeuedClientRequests              stagePurgeAll: %lld\n\nautoJobs                     totalAutoAssetJobsStarted: %lld\nautoJobs                         totalAutoJobsFinished: %lld\nstagerJobs             totalStagerDetermineJobsStarted: %lld\nstagerJobs            totalStagerDetermineJobsFinished: %lld\nstagerJobs              totalStagerDownloadJobsStarted: %lld\nstagerJobs             totalStagerDownloadJobsFinished: %lld\nresumedInFlightJobs           totalResumedInFlightJobs: %lld\nscheduledJobs              totalSchedulerTriggeredJobs: %lld\nfailuresToStartJobs           totalFailuresToStartJobs: %lld\n\npreviously           previouslyDownloadedPatchedAssets: %lld\npreviously            previouslyDownloadedPatchedBytes: %lld\npreviously              previouslyDownloadedFullAssets: %lld\npreviously               previouslyDownloadedFullBytes: %lld\n\ndownloaded                totalDownloadedPatchedAssets: %lld\ndownloaded                 totalDownloadedPatchedBytes: %lld\ndownloaded                   totalDownloadedFullAssets: %lld\ndownloaded                    totalDownloadedFullBytes: %lld\n\nstaged                        totalStagedPatchedAssets: %lld\nstaged                         totalStagedPatchedBytes: %lld\nstaged                           totalStagedFullAssets: %lld\nstaged                            totalStagedFullBytes: %lld\n\nunstaged                    totalUnstagedPatchedAssets: %lld\nunstaged                     totalUnstagedPatchedBytes: %lld\nunstaged                       totalUnstagedFullAssets: %lld\nunstaged                        totalUnstagedFullBytes: %lld\n\npromoted                    totalPromotedPatchedAssets: %lld\npromoted                     totalPromotedPatchedBytes: %lld\npromoted                       totalPromotedFullAssets: %lld\npromoted                        totalPromotedFullBytes: %lld\n\nremoved                      totalRemovedPatchedAssets: %lld\nremoved                       totalRemovedPatchedBytes: %lld\nremoved                         totalRemovedFullAssets: %lld\nremoved                          totalRemovedFullBytes: %lld\n\nfinishedJobs        finishedJobSchedulerNetworkFailure: %lld\nfinishedJobs     finishedJobSchedulerNotNetworkRelated: %lld\nfinishedJobs           finishedJobClientNetworkFailure: %lld\nfinishedJobs        finishedJobClientNotNetworkRelated: %lld\n\ngarbageColection                             performed: %@\ngarbageColection                          reclaimSpace: %@\ngarbageColection                   totalReclaimedSpace: %@\ngarbageColection                 reclaimedV2AssetCount: %ld\ngarbageColection                 reclaimedV2AssetSpace: %@\ngarbageColection                reclaimedUnlockedCount: %ld\ngarbageColection                reclaimedUnlockedSpace: %@\ngarbageColection       reclaimedLockedOverridableCount: %ld\ngarbageColection       reclaimedLockedOverridableSpace: %@\ngarbageColection       reclaimedLockedNeverRemoveCount: %ld\ngarbageColection       reclaimedLockedNeverRemoveSpace: %@\ngarbageColection                  reclaimedStagedCount: %ld\ngarbageColection                  reclaimedStagedSpace: %@\ngarbageColection         reclaimedMetadataBlockedCount: %ld\ngarbageColection         reclaimedMetadataBlockedSpace: %@\n<<<]"
- "ASEnsureDataVault"
- "ASSetAssetServerURLForAssetType"
- "ASSetDefaultAssetServerURLForAssetType"
- "Asset load result for %@: %ld (%@)"
- "Asset load result for %@: %ld (MAQueryHasAllowedDifferences). Found match %@ within allowed differences %@ (actual differences were %@)"
- "Asset load result for %@: %ld (MAQuerySuccessful). Found %@."
- "Bad asset meta data, cannot download: %@ %@ %@ %@"
- "Bad options for asset type: %@ not sending message"
- "Cannot download %@ %@ unless the download is user-initiated (non-discretionary) as the user has turned off background system file updates (check first if nonUserInitiatedDownloadsAllowed)."
- "Cannot set Pallas URL to a class that is not NSURL (was given an %@), returning MAOperationInvalid."
- "Client received notification with info %@"
- "Config download sync check failure server side: %lld (%@)"
- "Confirmed data vault for %@"
- "Could not cancel v1 download: %lld %@"
- "Could not connect to service %@"
- "Could not determine state for %@ asset %@; leaving state the same %ld (%@)."
- "Could not get asset attributes: %@"
- "Could not get attribute '%@': %@"
- "Could not get space available for downloading as downloading an ASAsset is deprecated, use MAAsset: %@"
- "Could not pause asset download: %@"
- "Could not purge asset: %@"
- "Could not resume asset download: %@"
- "Could not send garbage collection behavior message: %@"
- "Could not set server URL in daemon: %lld %@ for url: %@"
- "Created pushnotificationhistory.plist with result %@"
- "Creating client/daemon connection: %@"
- "Daemon not ready - retrying download in %d seconds [%@, %@]"
- "Debug"
- "Deprecated ASAsset API is no longer supported: %s"
- "Discarding params as they could not be encoded: %@"
- "ERROR: Invalid string passed to %s"
- "Error creating directory: %@"
- "Error loading history: %@"
- "Error making connection to mobileassetd: %@"
- "Error on the cancel download asset reply for %@, response: %ld (%@)"
- "Error on the download asset reply for %@, response: %ld (%@)"
- "Error on the download asset reply for %@, response: %ld (%@) due to no xpc message"
- "Error on the download meta data reply for %@, response: %ld (%@)"
- "Error on the download meta data reply for %@, response: %ld (%@) due to not having an xpc message"
- "Error on the purge asset reply for %@, response: %ld (%@) due to XPC_TYPE_ERROR"
- "Error on the retry download meta data reply for %@, response: %ld (%@)"
- "Error on the retry download meta data reply for %@, response: %ld (%@) due to not having an xpc message"
- "Error writing notifications to history: %@"
- "Error: %@"
- "Failed to get key: %s"
- "Failed to get key: %s due to not beinng present"
- "Fault"
- "Got the cancel PMV reply, response: %ld (%@)"
- "Got the cancel catalog reply for %@, response: %ld"
- "Got the cancel download asset reply for %@, response: %ld (%@)"
- "Got the config download reply for %@, response: %ld (%@)"
- "Got the download asset reply for %@, response: %ld (%@)"
- "Got the download meta data reply for %@, response: %ld (%@)"
- "Got the purge asset reply for %@, response: %ld (%@)"
- "Got the query meta data reply for: %@, response: %ld"
- "Got the retry download meta data reply for %@, response: %ld (%@)"
- "MAPurgeAllWithPurposeExceptGivenIds_block_invoke"
- "MAPurgeCatalogsWithPurpose_block_invoke"
- "MobileAsset %@ sendOperationSync %lld (%@) given a non-NSString assetType"
- "MobileAsset %@ sendOperationSync %lld (%@) given a non-NSString pathToAsset"
- "MobileAsset Install Asset failed with error: %@"
- "MobileAsset Simulated %{public}s: %{public}@"
- "MobileAssetQueryCreate"
- "MobileAssetQueryCreateArrayOfKnownAssets"
- "MobileAssetQueryGetMatchingAsset"
- "MobileAssetQueryRefreshAssetsAgainstLocalCache"
- "MobileAssetQueryRefreshKnownAssets"
- "Notice"
- "Old state: %ld (%@) --> new state: %lld (%@)"
- "Preserved ID is not a string: %@ %@"
- "Preserved IDs value is not an array for: %@"
- "Querying with purpose: %@"
- "Result from overrideGarbageCollectionThreshold: %ld (%@)"
- "Result from purge sync: %ld (%@)"
- "Result from space check: %ld (%@)"
- "Result of setDawTokenPath is %lld (%@)"
- "Result of setDawTokenValue is %lld (%@)"
- "Result of setPreferences is %lld (%@)"
- "Retrying download [%@, %@]"
- "Service connection invalidated"
- "State refresh failure server side: %ld (%@)"
- "Successful cancel v1 download: %lld %@"
- "T@\"MAAutoAssetProgress\",&,N,V_downloadProgress"
- "T@\"MAAutoAssetSetProgress\",&,N,V_downloadProgress"
- "The asset is installed at: %@"
- "The download options are %@"
- "Unable to allocate log message"
- "Unable to initialize keyed unarchiver, error: %@"
- "Unknown MACancelDownloadResult: %ld (%@)"
- "Will retry download meta data for %@, after %ld seconds"
- "[%s] Failed to query PMV with error: %@"
- "[%s] Setting include includeSupervised: %@"
- "[%s] Setting notExpiredBeforeString: %@"
- "[%s] Setting platformExactMatch: %@"
- "[%s] Setting postedBeforeString: %@"
- "[%s] Setting supportedDevicePrefix: %@"
- "[%s] Setting versionPrefix: %@"
- "[MAAutoAssetSetShortTermLockInMemoryRecord]: Unable to determine modification date for lock file tracked by %@"
- "[interestInContent:%lld,checkForNewer:%lld,determineIfAvailable:%lld,currentStatus:%lld,lockContent:%lld,mapLockedContent:%lld,continueLockUsage:%lld,endLockUsage:%lld,endPreviousLocks:%lld,endAllPreviousLocks:%lld|eliminateAllForSelector:%lld|eliminateAllForAssetType:%lld|eliminatePromotedNeverLockedForSelector:%lld|stageDetermineAllAvailable:%lld,stageDownloadAll:%lld,stagePurgeAll:%lld,stageEraseAll:%lld]"
- "_LengthOfDataRange"
- "_MASetDawTokenPath"
- "_MASetDawTokenValue"
- "_MAclientSendEnsureDataVault"
- "_MAclientSendGetServerUrl"
- "_MAensureExtension"
- "_MAsendDownloadAsset"
- "_MAsendDownloadAsset_block_invoke"
- "_MAsendDownloadAsset_block_invoke_2"
- "_MAsendDownloadMetaData"
- "_MAsendGetPallasAudience"
- "_MAsendGetPallasUrlForType"
- "_MAsendInstallAsset"
- "_MAsendPMVCancelDownload_block_invoke"
- "_MAsendPMVDownload"
- "_MAsendPMVDownload_block_invoke"
- "_MAsendQueryMetaData"
- "_MAsendSetPallasUrlForType"
- "_MAsendSetPreferences"
- "_MeasurementAlgorithmn"
- "_activeJobSummary:limitedToAssetTypes:completion:"
- "_activeSetJobSummary:limitedToSetIdentifiers:completion:"
- "_autoAssetInstanceInfo:completion:"
- "_autoAssetsOverview:limitedToSetIdentifiers:completion:"
- "_availableForStagingAssetSummary:"
- "_cancelActivityForSelector:"
- "_controlStatistics:completion:"
- "_eliminateAllForAssetType:"
- "_eliminateAllForSelector:"
- "_eliminateAtomic:awaitingUnlocked:completion:"
- "_eliminatePromotedNeverLockedForSelector:"
- "_endAllPreviousLocksOfReason:completion:"
- "_endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:"
- "_endPreviousLocksOfReason:removingLockCount:completion:"
- "_failedCancelActivity:withResponseError:description:completion:"
- "_failedCheckAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:"
- "_failedCheckForNewer:withResponseError:description:completion:"
- "_failedContinueLockUsage:withResponseError:description:completion:"
- "_failedControl:withErrorCode:withResponseError:description:completion:"
- "_failedControlInstanceInfo:withErrorCode:withResponseError:description:completion:"
- "_failedControlLockSummary:withErrorCode:withResponseError:description:completion:"
- "_failedControlOverview:withErrorCode:withResponseError:description:completion:"
- "_failedControlStatistics:withErrorCode:withResponseError:description:completion:"
- "_failedControlSummary:withErrorCode:withResponseError:description:completion:"
- "_failedCurrentSetStatus:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:"
- "_failedCurrentStatus:withResponseError:description:completion:"
- "_failedDetermineIfAvailable:withResponseError:description:completion:"
- "_failedEliminate:withResponseError:description:completion:"
- "_failedEndLockUsage:withResponseError:description:completion:"
- "_failedFormSubAtomicInstance:withErrorCode:withResponseError:description:completion:"
- "_failedInterestInContent:withResponseError:description:completion:"
- "_failedLockAtomic:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:"
- "_failedLockContent:withResponseError:description:completion:"
- "_failedMapLockedAtomicEntry:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:"
- "_failedMapLockedContent:withResponseError:description:completion:"
- "_failedOperation:forAssetSetIdentifier:withErrorCode:withResponseError:description:completion:"
- "_failedSimulateCacheDeleteOperation:withErrorCode:withResponseError:description:completion:"
- "_failedStageCancelOperation:withResponseError:description:completion:"
- "_failedStageDetermineAllAvailable:withResponseError:description:completion:"
- "_failedStageDetermineGroupsAvailableForUpdate:withResponseError:description:completion:"
- "_failedStageDownloadAll:withResponseError:description:completion:"
- "_failedStageDownloadGroups:withResponseError:description:completion:"
- "_failedStageEraseAll:withResponseError:description:completion:"
- "_failedStagePurgeAll:withResponseError:description:completion:"
- "_forceGlobalAbandon:completion:"
- "_forceGlobalForget:completion:"
- "_forceGlobalPurge:forcingUnlock:completion:"
- "_forceGlobalUnlock:completion:"
- "_getCommsManager"
- "_hashCFArrayLegacy"
- "_hashCFDataOfLength"
- "_hashCFStringOfLength"
- "_knownAssetSummary:limitedToAssetTypes:completion:"
- "_knownAssetSummary:limitedToSetIdentifiers:completion:"
- "_lockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:"
- "_lockedAssetSetSummary:limitedToSetIdentifiers:completion:"
- "_lockedAssetSummary:limitedToAssetTypes:completion:"
- "_scheduledJobSummary:limitedToAssetTypes:completion:"
- "_scheduledSetJobSummary:limitedToSetIdentifiers:completion:"
- "_shortTermCurrentSetStatus:"
- "_shortTermCurrentSetStatusSync:"
- "_shortTermEndAtomicLock:ofAtomicInstance:completion:"
- "_shortTermEndAtomicLockSync:ofAtomicInstance:"
- "_shortTermLockAtomic:forAtomicInstance:completion:"
- "_shortTermLockAtomic:forAtomicInstance:performContentValidation:completion:"
- "_shortTermLockAtomicSync:forAtomicInstance:error:"
- "_shortTermLockAtomicSync:forAtomicInstance:performContentValidation:error:"
- "_shortTermLockAtomicWithContentValidationOption:forAtomicInstance:performContentValidation:completion:"
- "_simulateCacheDeleteDetermineReclaimableSpace:withUrgency:error:completion:"
- "_simulateCacheDeleteReclaimSpace:withUrgency:targetingPurgeAmount:error:completion:"
- "_simulateSetJobOperation:withEndEvent:forSelector:completion:"
- "_stageCancelOperation:"
- "_stageDetermineAllAvailable:forTargetBuildVersion:completion:"
- "_stageDetermineAllAvailableForUpdate:completion:"
- "_stageDetermineGroupsAvailableForUpdate:completion:"
- "_stageDownloadAll:reportingProgress:completion:"
- "_stageDownloadAllSync:assetsSuccessfullyStaged:error:reportingProgress:"
- "_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:"
- "_stageEraseAll:"
- "_stagePurgeAll:"
- "_stagedAssetSetSummary:limitedToSetIdentifiers:completion:"
- "_stagedAssetSummary:limitedToAssetTypes:completion:"
- "_successCancelActivity:"
- "_successCheckAtomic:forAssetSetIdentifier:newerInstanceDiscovered:discoveredAtomicEntries:completion:"
- "_successCheckForNewer:completion:"
- "_successContinueLockUsage:completion:"
- "_successControl:completion:"
- "_successControlInstanceInfo:withInstanceInfo:completion:"
- "_successControlLockSummary:withLockSummaryEntries:completion:"
- "_successControlOverview:withOverviewEntries:completion:"
- "_successControlStatistics:withControlStatistics:completion:"
- "_successControlSummary:withJobSummaryEntries:completion:"
- "_successCurrentSetStatus:forAssetSetIdentifier:withAssetSetStatus:completion:"
- "_successCurrentStatus:completion:"
- "_successDetermineIfAvailable:completion:"
- "_successEliminate:"
- "_successEndLockUsage:completion:"
- "_successFormSubAtomicInstance:formedSubAtomicInstance:completion:"
- "_successInterestInContent:completion:"
- "_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:"
- "_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:"
- "_successMapLockedAtomicEntry:forAtomicInstance:forMappedSelector:completion:"
- "_successMapLockedContent:dueToDesire:completion:"
- "_successOperation:forAssetSetIdentifier:completion:"
- "_successSimulateCacheDeleteOperation:withReclaimableSpace:completion:"
- "_successStageCancelOperation:"
- "_successStageDetermineAllAvailable:completion:"
- "_successStageDetermineGroupsAvailableForUpdate:completion:"
- "_successStageDownloadAll:completion:"
- "_successStageDownloadGroups:completion:"
- "_successStageEraseAll:"
- "_successStagePurgeAll:"
- "addObjectToMessage"
- "assembleTaskDescriptorWithPurposeAndAutoAssetJobID"
- "assetId: %@ State: %ld attributes: %@ purpose: %@"
- "auto(cancelActivityForSelectorSync)"
- "auto(checkForNewerSync)"
- "auto(contniueLockUsageSync)"
- "auto(currentStatusSync)"
- "auto(determineIfAvailableSync)"
- "auto(eliminateAllForAssetTypeSync)"
- "auto(eliminateAllForSelectorSync)"
- "auto(eliminatePromotedNeverLockedForSelectorSync)"
- "auto(endAllPreviousLocksOfReasonSync)"
- "auto(endLockUsageSync)"
- "auto(endPreviousLocksOfReasonSync)"
- "auto(interestInContentSync)"
- "auto(lockContentSync)"
- "auto(mapLockedContentSync)"
- "auto(stageDetermineAllAvailableForUpdate)"
- "auto-control(activeJobSummary)"
- "auto-control(activeSetJobSummary)"
- "auto-control(assetSetInstanceInfo)"
- "auto-control(assetSetsOverview)"
- "auto-control(availableForStagingAssetSummary)"
- "auto-control(controlStatistics)"
- "auto-control(forceGlobalAbandon)"
- "auto-control(forceGlobalForget)"
- "auto-control(forceGlobalPurge)"
- "auto-control(forceGlobalUnlock)"
- "auto-control(knownAssetSummary)"
- "auto-control(lockedAssetSetSummary)"
- "auto-control(lockedAssetSummary)"
- "auto-control(scheduledJobSummary)"
- "auto-control(scheduledSetJobSummary)"
- "auto-control(simulateCacheDeleteDetermineReclaimableSpace)"
- "auto-control(simulateCacheDeleteReclaimSpace)"
- "auto-control(simulateSetJobOperation)"
- "auto-control(stagedAssetSetSummary)"
- "auto-control(stagedAssetSummary)"
- "auto-set(alterEntriesRepresentingAtomicSync)"
- "auto-set(assetSetForStagingSync)"
- "auto-set(checkAtomicSync)"
- "auto-set(continueAtomicLockSync)"
- "auto-set(currentSetStatusSync)"
- "auto-set(eliminateAtomicSync)"
- "auto-set(endAtomicLockSync)"
- "auto-set(endAtomicLocks)"
- "auto-set(formSubAtomicInstanceSync)"
- "auto-set(mapLockedAtomicEntrySync)"
- "auto-set(needForAtomicSync)"
- "connection cleared: %@"
- "could not encode query params: %@"
- "createErrorFromMessage"
- "createErrorFromMessage: Successfully created error: %@"
- "createErrorFromMessage: unarchiver cannot be created: %@"
- "dataUsingEncoding:"
- "fileHandleWithStandardOutput"
- "frameworkDispatchQueue"
- "getLoadClassFromMessage"
- "getLocalPath asset %@ %@ local path is '%@'%@%@"
- "getLocalPath asset %@ %@%@%@"
- "getLocalUrlFromTypeAndIdGivenDefaultRepoWithPurpose"
- "getObjectFromMessage: could not decode object for key: %s error: %@"
- "getObjectFromMessageLogIfDesired"
- "isCancelDownloadResultFailure"
- "isValidObjectForAssetTypesArray"
- "isValidObjectForPreservedIdsDict"
- "load data is null skipping: %@"
- "load key is invalid skipping: %@"
- "load object is not a %@: %@"
- "load object is null skipping: %@"
- "load rawData is null skipping: %@"
- "lockAtomicSyncWithContentValidationOption:forAtomicInstance:performContentValidation:error:"
- "normalizedAssetType"
- "oslog"
- "q32@0:8@16q24"
- "sendOperationSync"
- "sharedLogger"
- "startDownloadWithExtractor:completion:"
- "startDownloadWithExtractor:options:completion:"
- "startDownloadWithExtractor:options:completionWithError:"
- "timeout (at framework layer) while waiting for active-job-summary to complete"
- "timeout (at framework layer) while waiting for active-set-job-summary to complete"
- "timeout (at framework layer) while waiting for alter-entries-representing-atomic to complete"
- "timeout (at framework layer) while waiting for asset-set-for-staging to complete"
- "timeout (at framework layer) while waiting for asset-set-instance-info to complete"
- "timeout (at framework layer) while waiting for asset-sets-overview to complete"
- "timeout (at framework layer) while waiting for cancel-activity to complete"
- "timeout (at framework layer) while waiting for check-atomic to complete"
- "timeout (at framework layer) while waiting for check-for-newer to complete"
- "timeout (at framework layer) while waiting for continue-atomic-lock to complete"
- "timeout (at framework layer) while waiting for continue-lock-usage to complete"
- "timeout (at framework layer) while waiting for control-statistics to complete"
- "timeout (at framework layer) while waiting for current-set-status to complete"
- "timeout (at framework layer) while waiting for current-status to complete"
- "timeout (at framework layer) while waiting for determine-if-available to complete"
- "timeout (at framework layer) while waiting for eliminate-atomic to complete"
- "timeout (at framework layer) while waiting for elimination to complete"
- "timeout (at framework layer) while waiting for end-all-previous-locks to complete"
- "timeout (at framework layer) while waiting for end-atomic-lock to complete"
- "timeout (at framework layer) while waiting for end-atomic-locks to complete"
- "timeout (at framework layer) while waiting for end-lock-usage to complete"
- "timeout (at framework layer) while waiting for end-previous-locks to complete"
- "timeout (at framework layer) while waiting for force-global-abandon to complete"
- "timeout (at framework layer) while waiting for force-global-forget to complete"
- "timeout (at framework layer) while waiting for force-global-purge to complete"
- "timeout (at framework layer) while waiting for force-global-unlock to complete"
- "timeout (at framework layer) while waiting for form-sub-atomic-instance to complete"
- "timeout (at framework layer) while waiting for interest-in-content to complete"
- "timeout (at framework layer) while waiting for known-asset-summary to complete"
- "timeout (at framework layer) while waiting for lock-atomic to complete"
- "timeout (at framework layer) while waiting for lock-content to complete"
- "timeout (at framework layer) while waiting for locked-asset-summary to complete"
- "timeout (at framework layer) while waiting for map-locked-atomic-entry to complete"
- "timeout (at framework layer) while waiting for map-locked-content to complete"
- "timeout (at framework layer) while waiting for need-for-atomic to complete"
- "timeout (at framework layer) while waiting for scheduled-job-summary to complete"
- "timeout (at framework layer) while waiting for simulate-job-operation to complete"
- "timeout (at framework layer) while waiting for simulated-cache-delete-operation to complete"
- "timeout (at framework layer) while waiting for stage-cancel-operation to complete"
- "timeout (at framework layer) while waiting for stage-determine-all-available to complete"
- "timeout (at framework layer) while waiting for stage-determine-groups-available-for-update to complete"
- "timeout (at framework layer) while waiting for stage-download-all to complete"
- "timeout (at framework layer) while waiting for stage-download-groups to complete"
- "timeout (at framework layer) while waiting for stage-erase-all to complete"
- "timeout (at framework layer) while waiting for stage-purge-all to complete"
- "timeout (at framework layer) while waiting for staged-asset-set-summary to complete"
- "timeout (at framework layer) while waiting for staged-asset-summary to complete"
- "v32@0:8@?16@?24"
- "v36@0:8B16@20@?28"
- "v40@0:8@?16@24@?32"
- "v44@0:8@16i24^@28@?36"
- "v48@0:8q16@24@32@?40"
- "v48@0:8q16q24@32@?40"
- "v52@0:8@16i24q28^@36@?44"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16q24@32@40@?48"
- "v64@0:8@16@24q32@40@48@?56"
- "v72@0:8@16@24@32@40@48@56@?64"
- "waitOnSemaphore:withDaemonTriggeredTimeout:"
- "waitOnSemaphore:withTimeout:"
- "writeData:"
- "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) unable to consume sandbox extension with errno %s (%d) for path %{public}@"
- "{_MAsendSetPreferences} Encoding error: %@"
- "{assembleTaskDescriptorWithPurposeAndAutoAssetJobID} invalid autoAssetJobID(ignored):%@"

```
