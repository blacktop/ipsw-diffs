## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.100.54.502.2
-  __TEXT.__text: 0x2800fc
-  __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x215e0
-  __TEXT.__objc_methlist: 0xfeec
+1487.100.93.502.2
+  __TEXT.__text: 0x2709e4
+  __TEXT.__auth_stubs: 0x2440
+  __TEXT.__objc_stubs: 0x21f80
+  __TEXT.__objc_methlist: 0x10154
   __TEXT.__const: 0x48ae
-  __TEXT.__cstring: 0x36abc
-  __TEXT.__objc_methname: 0x3b316
-  __TEXT.__objc_classname: 0xd99
-  __TEXT.__objc_methtype: 0x3781
-  __TEXT.__oslogstring: 0x47ed5
-  __TEXT.__gcc_except_tab: 0x2ef0
+  __TEXT.__cstring: 0x3720c
+  __TEXT.__objc_methname: 0x3c91f
+  __TEXT.__objc_classname: 0xdd3
+  __TEXT.__objc_methtype: 0x3931
+  __TEXT.__oslogstring: 0x4b40c
+  __TEXT.__gcc_except_tab: 0x2f34
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093
   __TEXT.__constg_swiftt: 0x14fc

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4840
+  __TEXT.__unwind_info: 0x4878
   __TEXT.__eh_frame: 0x3284
-  __DATA_CONST.__auth_got: 0x11e0
-  __DATA_CONST.__got: 0x648
-  __DATA_CONST.__auth_ptr: 0xa10
-  __DATA_CONST.__const: 0x6738
-  __DATA_CONST.__cfstring: 0x2afe0
+  __DATA_CONST.__auth_got: 0x1230
+  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__auth_ptr: 0xa18
+  __DATA_CONST.__const: 0x67e8
+  __DATA_CONST.__cfstring: 0x2b380
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9430
-  __DATA_CONST.__objc_arraydata: 0xaf8
-  __DATA_CONST.__objc_arrayobj: 0x240
+  __DATA_CONST.__objc_selrefs: 0x96b8
+  __DATA_CONST.__objc_arraydata: 0xb20
+  __DATA_CONST.__objc_arrayobj: 0x258
   __DATA_CONST.__objc_intobj: 0x408
-  __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14a80
-  __DATA.__objc_classrefs: 0x800
+  __DATA_CONST.__objc_dictobj: 0x118
+  __DATA.__objc_const: 0x14d70
+  __DATA.__objc_classrefs: 0x7f8
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x1384
+  __DATA.__objc_ivar: 0x13bc
   __DATA.__objc_data: 0xd60
-  __DATA.__data: 0x25b0
+  __DATA.__data: 0x25a8
   __DATA.__bss: 0x51b0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1978
-  __DATA_DIRTY.__bss: 0x328
+  __DATA_DIRTY.__bss: 0x318
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8237
-  Symbols:   15096
-  CStrings:  16293
+  Functions: 8288
+  Symbols:   15258
+  CStrings:  16579
 
Symbols:
+ +[DownloadManager addNWActivityToDownloadInfo:andTask:andLabel:]
+ +[MADAutoAssetControlManager assetConfigJobFinished:withDownloadInfo:error:]
+ +[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:]
+ +[MADAutoAssetControlManager preferenceStagerDetermineLastRequiredTimesOut]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:failingWithError:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:]
+ +[MADAutoAssetHistory recordFailedOperation:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forAssetSetIdentifier:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:]
+ +[MADAutoAssetLocker forceGlobalUnlock:atomicInstancesHandle:]
+ +[MADAutoAssetLocker newSetClientNameForDomain:withAutoAssetClientName:forSetAtomicInstance:]
+ +[MADAutoAssetSecure readyToCommitPrePersonalized:forSetDescriptor:]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _currentState]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _nonceFileURL]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState _stateFileURL]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState clear]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState currentStatusWithStateHandle:]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState supportsSecureCoding]
+ +[MADAutoAssetSoftwareUpdateSuspendResumeState writeNewSuspendingStateWithNonce:setConfigurationsToEvict:]
+ -[DownloadInfo nwActivity]
+ -[DownloadInfo setNwActivity:]
+ -[DownloadManager indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:]
+ -[DownloadManager indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:]
+ -[MADAutoAssetControlManager _allPreInstalledDescriptor:forAssetType:]
+ -[MADAutoAssetControlManager _constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:]
+ -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:]
+ -[MADAutoAssetControlManager _errorUnlessSameVersionFound:changedReportedError:]
+ -[MADAutoAssetControlManager _persistedKnownDescriptorForFullAssetSelector:]
+ -[MADAutoAssetControlManager _persistedKnownDescriptorForPersistedEntryID:]
+ -[MADAutoAssetControlManager _removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:]
+ -[MADAutoAssetControlManager _removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager cancelActiveSetJob:activeSetJob:]
+ -[MADAutoAssetControlManager cancelingSetJobsByIdentifier]
+ -[MADAutoAssetControlManager completionCallbacksBySetJobKey]
+ -[MADAutoAssetControlManager doesSetJobDescriptor:representSameContentAs:]
+ -[MADAutoAssetControlManager evictedCallbacksByAtomicInstanceUUID]
+ -[MADAutoAssetControlManager forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:]
+ -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:]
+ -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:]
+ -[MADAutoAssetControlManager isNoWaitRequestInvolvingSecureAsset:]
+ -[MADAutoAssetControlManager locateCancelingSetJobForClientDomain:byIdentifier:]
+ -[MADAutoAssetControlManager newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:]
+ -[MADAutoAssetControlManager persistedKnownDescriptorForSetAtomicEntry:]
+ -[MADAutoAssetControlManager preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:]
+ -[MADAutoAssetControlManager preferenceStagerDetermineLastRequiredTimesOut]
+ -[MADAutoAssetControlManager setCancelingSetJobsByIdentifier:]
+ -[MADAutoAssetControlManager setCompletionCallbacksBySetJobKey:]
+ -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:]
+ -[MADAutoAssetControlManager setEvictedCallbacksByAtomicInstanceUUID:]
+ -[MADAutoAssetControlManager setPreferenceStagerDetermineLastRequiredTimesOut:]
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
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetDescriptor totalFilesystemSpace]
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
+ -[MADAutoAssetLocker _endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:]
+ -[MADAutoAssetLocker _lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:]
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
+ -[MADAutoAssetStager _replyHaveStagedContent:withEventInfo:]
+ -[MADAutoSetConfiguration availableForUseError]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoSetConfiguration newerVersionError]
+ -[MADAutoSetConfiguration setAvailableForUseError:]
+ -[MADAutoSetConfiguration setNewerVersionError:]
+ -[MobileAssetHealthReport getGreymatterStatus]
+ GCC_except_table144
+ GCC_except_table174
+ GCC_except_table255
+ GCC_except_table413
+ GCC_except_table593
+ GCC_except_table595
+ GCC_except_table601
+ GCC_except_table603
+ GCC_except_table617
+ GCC_except_table65
+ GCC_except_table749
+ MALOG_AUTOCONTROL_SUSPENDRESUME_MASK_block_invoke.onceToken
+ OBJC_IVAR_$_DownloadInfo._nwActivity
+ OBJC_IVAR_$_MADAutoAssetControlManager._cancelingSetJobsByIdentifier
+ OBJC_IVAR_$_MADAutoAssetControlManager._completionCallbacksBySetJobKey
+ OBJC_IVAR_$_MADAutoAssetControlManager._evictedCallbacksByAtomicInstanceUUID
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDetermineLastRequiredTimesOut
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._downloadOptions
+ OBJC_IVAR_$_MADAutoAssetJob._boostedToCellular
+ OBJC_IVAR_$_MADAutoAssetJob._boostedToExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToCellular
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._configuredToUserInitiated
+ OBJC_IVAR_$_MADAutoAssetJob._downloadingCellular
+ OBJC_IVAR_$_MADAutoAssetJob._downloadingExpensive
+ OBJC_IVAR_$_MADAutoAssetJob._queuedRequestsForNewJobOnceCanceled
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._build
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._nonce
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._setConfigurationsToEvict
+ OBJC_IVAR_$_MADAutoAssetSoftwareUpdateSuspendResumeState._status
+ OBJC_IVAR_$_MADAutoSetConfiguration._availableForUseError
+ OBJC_IVAR_$_MADAutoSetConfiguration._newerVersionError
+ _CC_SHA256
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFPropertyListCreateDeepCopy
+ _MAAutoAssetSuspendResumeForSoftwareUpdateStatusString
+ _MAConvertTicksToSeconds
+ _MAMeasurementHashAlgorithmSHA1
+ _MAMeasurementHashAlgorithmSHA256
+ _OBJC_CLASS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ _OBJC_METACLASS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_72
+ _SZExtractorHashTypeSHA256
+ _SecPolicyCreate3PMobileAsset
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1207
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1642
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2116
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1136
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1140
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1156
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1218
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1219
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1223
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2289
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1242
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1252
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1121
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1122
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1130
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1131
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2227
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2239
+ __22-[ControlManager init]_block_invoke.1182
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2270
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1702
+ __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1080
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1695
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1696
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1172
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1219
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2171
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2172
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1854
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1861
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1815
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1460
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1268
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1275
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1927
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1230
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1231
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1232
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1542
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1205
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1226
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1892
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1085
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1184
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1191
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1192
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2287
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1056
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1057
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1058
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2481
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2482
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1169
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1170
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1171
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1175
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1205
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1206
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1208
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3262
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3263
+ __MABufferToHexString
+ __MAHashDictionary
+ __MobileAssetVerifyThirdPartySigning
+ __OBJC_$_CLASS_METHODS_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_CLASS_PROP_LIST_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetControlManager(SoftwareUpdateSuspendResume)
+ __OBJC_$_INSTANCE_METHODS_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_INSTANCE_VARIABLES_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_$_PROP_LIST_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_CLASS_PROTOCOLS_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_CLASS_RO_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ __OBJC_METACLASS_RO_$_MADAutoAssetSoftwareUpdateSuspendResumeState
+ ___108+[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:]_block_invoke
+ ___150-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:]_block_invoke
+ ___173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke
+ ___178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke
+ ___401+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:]_block_invoke
+ ___413-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:]_block_invoke
+ ___62+[MADAutoAssetLocker forceGlobalUnlock:atomicInstancesHandle:]_block_invoke
+ ___83-[MADAutoAssetJob handleDownloadConfigJobFinished:withDownloadOptions:configError:]_block_invoke
+ ___97-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) handleSuspendForSoftwareUpdateRequest:]_block_invoke
+ ___block_descriptor_232_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16ls32l8s40l8r64l8s48l8r72l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ __block_literal_global.1042
+ __block_literal_global.1045
+ __block_literal_global.1057
+ __block_literal_global.1059
+ __block_literal_global.1069
+ __block_literal_global.1073
+ __block_literal_global.1081
+ __block_literal_global.1085
+ __block_literal_global.1088
+ __block_literal_global.1091
+ __block_literal_global.1101
+ __block_literal_global.1105
+ __block_literal_global.1106
+ __block_literal_global.1130
+ __block_literal_global.1159
+ __block_literal_global.1169
+ __block_literal_global.1170
+ __block_literal_global.1171
+ __block_literal_global.1204
+ __block_literal_global.1218
+ __block_literal_global.1228
+ __block_literal_global.1274
+ __block_literal_global.1276
+ __block_literal_global.1281
+ __block_literal_global.1283
+ __block_literal_global.1320
+ __block_literal_global.1343
+ __block_literal_global.1350
+ __block_literal_global.1355
+ __block_literal_global.1377
+ __block_literal_global.1459
+ __block_literal_global.1560
+ __block_literal_global.1599
+ __block_literal_global.1671
+ __block_literal_global.1691
+ __block_literal_global.1696
+ __block_literal_global.1701
+ __block_literal_global.1704
+ __block_literal_global.1735
+ __block_literal_global.1759
+ __block_literal_global.2030
+ __block_literal_global.2052
+ __block_literal_global.2206
+ __block_literal_global.2217
+ __block_literal_global.2222
+ __block_literal_global.2225
+ __block_literal_global.2233
+ __block_literal_global.2241
+ __block_literal_global.2249
+ __block_literal_global.2257
+ __block_literal_global.2265
+ __block_literal_global.2273
+ __block_literal_global.2316
+ __block_literal_global.2318
+ __block_literal_global.2344
+ __block_literal_global.2346
+ __block_literal_global.2383
+ __block_literal_global.3916
+ __block_literal_global.4876
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1087
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1083
+ __hashCFArray
+ __hashCFString
+ _applyCatalogTransforms
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _hashCFString.cold.1
+ _hashCFString.cold.2
+ _hashCFString.cold.3
+ _hashCFType.cold.1
+ _kMobileAssetPreferencesAutoAssetStagerDetermineLastRequiredTimesOut
+ _kMobileAssetPreferencesAutoAssetSuspendResumeEnabled
+ _kMobileAssetPreferencesAutoAssetSuspendResumeForSUSetsOverride
+ _mach_absolute_time
+ _nw_activity_activate
+ _nw_activity_complete_with_reason
+ _nw_activity_create
+ _objc_msgSend$_addCompletionCallbackForSetJobKey:completionCallback:
+ _objc_msgSend$_addEvictedCallbackForAtomicInstanceUUID:completionCallback:
+ _objc_msgSend$_allPreInstalledDescriptor:forAssetType:
+ _objc_msgSend$_constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:
+ _objc_msgSend$_currentState
+ _objc_msgSend$_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:
+ _objc_msgSend$_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:
+ _objc_msgSend$_errorUnlessSameVersionFound:changedReportedError:
+ _objc_msgSend$_handleEstimateEvictableBytesForSoftwareUpdateRequestWithBytesBySetIdentifier:
+ _objc_msgSend$_handleResumeFromSoftwareUpdateRequest
+ _objc_msgSend$_handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce:setConfigurationsToEvict:completionBlock:
+ _objc_msgSend$_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:
+ _objc_msgSend$_nonceFileURL
+ _objc_msgSend$_persistedKnownDescriptorForFullAssetSelector:
+ _objc_msgSend$_persistedKnownDescriptorForPersistedEntryID:
+ _objc_msgSend$_removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:
+ _objc_msgSend$_removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:
+ _objc_msgSend$_replyHaveStagedContent:withEventInfo:
+ _objc_msgSend$_softwareUpdateSuspendResumeEligibleSetEntryIDs
+ _objc_msgSend$_stateFileURL
+ _objc_msgSend$_updateDownloadOptions:
+ _objc_msgSend$_updateUserInitiatedFields
+ _objc_msgSend$action_BoostConfig:error:
+ _objc_msgSend$addNWActivityToDownloadInfo:andTask:andLabel:
+ _objc_msgSend$assetConfigJobFinished:withDownloadInfo:error:
+ _objc_msgSend$boostedToCellular
+ _objc_msgSend$boostedToExpensive
+ _objc_msgSend$byGroupAvailableForStagingAttributes
+ _objc_msgSend$cancelActiveSetJob:activeSetJob:
+ _objc_msgSend$cancelingSetJobsByIdentifier
+ _objc_msgSend$clear
+ _objc_msgSend$completionCallbacksBySetJobKey
+ _objc_msgSend$configuredToCellular
+ _objc_msgSend$configuredToExpensive
+ _objc_msgSend$configuredToUserInitiated
+ _objc_msgSend$currentStatusWithStateHandle:
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$dedupAtomicEntries:
+ _objc_msgSend$doesSetJobDescriptor:representSameContentAs:
+ _objc_msgSend$downloadingCellular
+ _objc_msgSend$downloadingExpensive
+ _objc_msgSend$evictedCallbacksByAtomicInstanceUUID
+ _objc_msgSend$forceGlobalUnlock:atomicInstancesHandle:
+ _objc_msgSend$forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:
+ _objc_msgSend$getGreymatterStatus
+ _objc_msgSend$handleDownloadConfigJobFinished:withDownloadOptions:configError:
+ _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:
+ _objc_msgSend$handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:
+ _objc_msgSend$handleSuspendResumeForSoftwareUpdateDaemonStartup
+ _objc_msgSend$indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:
+ _objc_msgSend$indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
+ _objc_msgSend$initForConfigFinishedJobID:andDownloadOptions:withError:
+ _objc_msgSend$initForSetAtomicInstanceUUID:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$initWithNonce:status:setConfigurationsToEvict:
+ _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$isNoWaitRequestInvolvingSecureAsset:
+ _objc_msgSend$isSuspendedForSoftwareUpdate:forAssetSetIdentifier:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$locateCancelingSetJobForClientDomain:byIdentifier:
+ _objc_msgSend$neededBytes
+ _objc_msgSend$newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:
+ _objc_msgSend$nonce
+ _objc_msgSend$notifyEvictedCallbacksForSetDescriptor:
+ _objc_msgSend$nwActivity
+ _objc_msgSend$objectIsEqual:to:
+ _objc_msgSend$permitThirdPartySigningForAssetType:outOrganizations:
+ _objc_msgSend$persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:
+ _objc_msgSend$persistedKnownDescriptorForSetAtomicEntry:
+ _objc_msgSend$preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:
+ _objc_msgSend$preferenceStagerDetermineLastRequiredTimesOut
+ _objc_msgSend$queuedRequestsForNewJobOnceCanceled
+ _objc_msgSend$readyToCommitPrePersonalized:forSetDescriptor:
+ _objc_msgSend$recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:
+ _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:
+ _objc_msgSend$refreshDownloadedToManager:
+ _objc_msgSend$refreshSetFoundToManager:fromLocation:
+ _objc_msgSend$reportSetCatalogDecideFound:fromLocation:
+ _objc_msgSend$setAtomicInstanceUUID
+ _objc_msgSend$setBoostedToCellular:
+ _objc_msgSend$setBoostedToExpensive:
+ _objc_msgSend$setCompletionCallbacksBySetJobKey:
+ _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:
+ _objc_msgSend$setConfigurationsToEvict
+ _objc_msgSend$setConfiguredToCellular:
+ _objc_msgSend$setConfiguredToExpensive:
+ _objc_msgSend$setConfiguredToUserInitiated:
+ _objc_msgSend$setEvictedCallbacksByAtomicInstanceUUID:
+ _objc_msgSend$setNwActivity:
+ _objc_msgSend$setQueuedRequestsForNewJobOnceCanceled:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$set_nw_activity:
+ _objc_msgSend$suspendedSetConfigurationsFromPreviousOS
+ _objc_msgSend$suspendedSetConfigurationsHasCurrentNonce
+ _objc_msgSend$totalFilesystemSpace
+ _objc_msgSend$triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:
+ _objc_msgSend$write
+ _objc_msgSend$writeNewSuspendingStateWithNonce:setConfigurationsToEvict:
+ _os_eligibility_get_domain_answer
- +[MADAutoAssetControlManager assetConfigJobFinished:error:]
- +[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:]
- +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:]
- +[MADAutoAssetLocker forceGlobalUnlock:]
- +[MADAutoSetLocker addClientLockReasons:basedOnControl:]
- +[MADAutoSetLocker additionalLockedByClient:forAssetSelector:forLockReason:withUsagePolicy:lockError:]
- +[MADAutoSetLocker autoAssetLocker]
- +[MADAutoSetLocker autoAssetLocker].cold.1
- +[MADAutoSetLocker continuedLockByClient:forAssetSelector:forLockReason:withUsagePolicy:continueError:]
- +[MADAutoSetLocker copyOfLocksBySelector]
- +[MADAutoSetLocker endedAllPreviousLocksByClient:forAssetSelector:forLockReason:endError:]
- +[MADAutoSetLocker endedLockByClient:forAssetSelector:forLockReason:endError:]
- +[MADAutoSetLocker endedPreviousLocksByClient:forAssetSelector:forLockReason:removingLockCount:endError:]
- +[MADAutoSetLocker forceGlobalUnlock:]
- +[MADAutoSetLocker lockedByClient:forAssetSetIdentifier:forAtomicInstance:forLockReason:withUsagePolicy:lockError:]
- +[MADAutoSetLocker lockedSelectorsForEliminate:]
- +[MADAutoSetLocker migrateMismatchedPersistedStateVersion:forEntryID:withMismatchedState:]
- +[MADAutoSetLocker newCurrentLockUsageForSelector:]
- +[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]
- -[DownloadManager applyTransforms:toAssets:]
- -[MADAutoAssetControlManager _decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:]
- -[MADAutoAssetControlManager _removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:]
- -[MADAutoAssetControlManager handleEstimateEvictableBytesForSoftwareUpdateRequest:]
- -[MADAutoAssetControlManager handleResumeFromSoftwareUpdateRequest:]
- -[MADAutoAssetControlManager handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:]
- -[MADAutoAssetControlManager handleSetClientEliminateAtomicRequest:forAutoJob:]
- -[MADAutoAssetControlManager handleStatusForSoftwareUpdateRequest:]
- -[MADAutoAssetControlManager handleSuspendForSoftwareUpdateRequest:]
- -[MADAutoAssetControlManager newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:]
- -[MADAutoAssetControlManager preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:]
- -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:]
- -[MADAutoAssetControlManager setSuspendResumeStatus:]
- -[MADAutoAssetControlManager suspendResumeStatus]
- -[MADAutoAssetControlManagerParam initForConfigFinishedJobID:withError:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:]
- -[MADAutoAssetJob action_BoostToUserInitiated:error:]
- -[MADAutoAssetJob action_NowUserInitiated:error:]
- -[MADAutoAssetJob action_ReportFailBoostSetDownloadNext:error:]
- -[MADAutoAssetJob action_ReportFailureUserInitiated:error:]
- -[MADAutoAssetJob action_UserInitiatedDownloadNewestFull:error:]
- -[MADAutoAssetJob action_UserInitiatedSetDownloadNext:error:]
- -[MADAutoAssetJob handleDownloadConfigJobFinished:configError:]
- -[MADAutoAssetJob refreshDownloadedToManager]
- -[MADAutoAssetJob refreshSetFoundToManager:]
- -[MADAutoAssetJob reportSetCatalogDecideFound:]
- -[MADAutoAssetLocker _endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:]
- -[MADAutoAssetLocker _lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:]
- -[MADAutoAssetLocker setAtomicInstanceForUUID:fromSetAtomicInstances:]
- -[MADAutoAssetStager _replyHaveStagedContent:]
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
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
- -[MADAutoSetLocker _persistRemoveAssetLock:removedAssetLock:message:]
- -[MADAutoSetLocker _refreshFilesystemMetadataLastInterest:]
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
- GCC_except_table172
- GCC_except_table253
- GCC_except_table409
- GCC_except_table592
- GCC_except_table594
- GCC_except_table597
- GCC_except_table599
- GCC_except_table613
- GCC_except_table740
- MALOG_AUTOJOB_MASK_block_invoke.onceToken
- OBJC_IVAR_$_MADAutoAssetControlManager._suspendResumeStatus
- OBJC_IVAR_$_MADAutoSetLocker._eliminateSelectors
- OBJC_IVAR_$_MADAutoSetLocker._lockerQueue
- OBJC_IVAR_$_MADAutoSetLocker._locksBySelector
- OBJC_IVAR_$_MADAutoSetLocker._logger
- OBJC_IVAR_$_MADAutoSetLocker._persistedState
- _CFStringCreateWithCString
- _OBJC_CLASS_$_MADAutoSetLocker
- _OBJC_METACLASS_$_MADAutoSetLocker
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_49
- _OUTLINED_FUNCTION_70
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1198
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1627
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2104
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1127
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1131
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1147
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1209
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1210
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1214
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2275
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1233
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1243
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2218
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2228
- __22-[ControlManager init]_block_invoke.1173
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2259
- __37-[DownloadManager startDownloadTimer]_block_invoke.1690
- __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1068
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1680
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1681
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1163
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1210
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2159
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2160
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1848
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1849
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1809
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1451
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1259
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1266
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1912
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1221
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1222
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1223
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1527
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1067
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1087
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1194
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1215
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1877
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1076
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1175
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1182
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1183
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2278
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1047
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1048
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1049
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2472
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2473
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1160
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1161
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1162
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1166
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1196
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1197
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1199
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3221
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3222
- __OBJC_$_CLASS_METHODS_MADAutoSetLocker
- __OBJC_$_INSTANCE_METHODS_MADAutoAssetControlManager
- __OBJC_$_INSTANCE_METHODS_MADAutoSetLocker
- __OBJC_$_INSTANCE_VARIABLES_MADAutoSetLocker
- __OBJC_$_PROP_LIST_MADAutoSetLocker
- __OBJC_CLASS_RO_$_MADAutoSetLocker
- __OBJC_METACLASS_RO_$_MADAutoSetLocker
- ___24-[MADAutoSetLocker init]_block_invoke
- ___24-[MADAutoSetLocker init]_block_invoke_2
- ___315+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:]_block_invoke
- ___325-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:]_block_invoke
- ___35+[MADAutoSetLocker autoAssetLocker]_block_invoke
- ___38+[MADAutoSetLocker forceGlobalUnlock:]_block_invoke
- ___40+[MADAutoAssetLocker forceGlobalUnlock:]_block_invoke
- ___41+[MADAutoSetLocker copyOfLocksBySelector]_block_invoke
- ___48+[MADAutoSetLocker lockedSelectorsForEliminate:]_block_invoke
- ___51+[MADAutoSetLocker newCurrentLockUsageForSelector:]_block_invoke
- ___63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke
- ___95+[MADAutoAssetControlManager persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:]_block_invoke
- ___block_descriptor_192_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_81_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- __block_literal_global.1033
- __block_literal_global.1036
- __block_literal_global.1048
- __block_literal_global.1050
- __block_literal_global.1051
- __block_literal_global.1063
- __block_literal_global.1064
- __block_literal_global.1066
- __block_literal_global.1070
- __block_literal_global.1076
- __block_literal_global.1079
- __block_literal_global.1087
- __block_literal_global.1089
- __block_literal_global.1092
- __block_literal_global.1097
- __block_literal_global.1121
- __block_literal_global.1150
- __block_literal_global.1160
- __block_literal_global.1161
- __block_literal_global.1162
- __block_literal_global.1193
- __block_literal_global.1209
- __block_literal_global.1217
- __block_literal_global.1253
- __block_literal_global.1255
- __block_literal_global.1260
- __block_literal_global.1262
- __block_literal_global.1311
- __block_literal_global.1334
- __block_literal_global.1341
- __block_literal_global.1346
- __block_literal_global.1368
- __block_literal_global.1450
- __block_literal_global.1548
- __block_literal_global.1587
- __block_literal_global.1662
- __block_literal_global.1682
- __block_literal_global.1687
- __block_literal_global.1692
- __block_literal_global.1695
- __block_literal_global.1725
- __block_literal_global.1749
- __block_literal_global.2018
- __block_literal_global.2040
- __block_literal_global.2197
- __block_literal_global.2204
- __block_literal_global.2208
- __block_literal_global.2216
- __block_literal_global.2224
- __block_literal_global.2232
- __block_literal_global.2240
- __block_literal_global.2248
- __block_literal_global.2256
- __block_literal_global.2264
- __block_literal_global.2302
- __block_literal_global.2303
- __block_literal_global.2330
- __block_literal_global.2332
- __block_literal_global.2374
- __block_literal_global.3863
- __block_literal_global.4852
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1078
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1074
- __hashCFArrayLegacy
- __hashCFArrayNoLegacy
- __hashCFDataOfLength
- __hashCFStringOfLength
- __hashToCFString
- _hashCFDataOfLength.cold.1
- _hashCFStringOfLength.cold.1
- _hashCFStringOfLength.cold.2
- _hashCFStringOfLength.cold.3
- _iPhoneCACert_crt_len
- _objc_msgSend$_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:
- _objc_msgSend$_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:
- _objc_msgSend$_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:
- _objc_msgSend$_removeAssetLock:lastClient:forSelector:message:
- _objc_msgSend$_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:
- _objc_msgSend$_replyHaveStagedContent:
- _objc_msgSend$action_BoostToUserInitiated:error:
- _objc_msgSend$action_NowUserInitiated:error:
- _objc_msgSend$action_ReportFailBoostSetDownloadNext:error:
- _objc_msgSend$action_ReportFailureUserInitiated:error:
- _objc_msgSend$action_UserInitiatedDownloadNewestFull:error:
- _objc_msgSend$action_UserInitiatedSetDownloadNext:error:
- _objc_msgSend$applyTransforms:toAssets:
- _objc_msgSend$assetConfigJobFinished:error:
- _objc_msgSend$forceGlobalUnlock:
- _objc_msgSend$handleDownloadConfigJobFinished:configError:
- _objc_msgSend$handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:
- _objc_msgSend$handleSetClientEliminateAtomicRequest:forAutoJob:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
- _objc_msgSend$initForConfigFinishedJobID:withError:
- _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$locksBySelector
- _objc_msgSend$newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:
- _objc_msgSend$persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:
- _objc_msgSend$preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:
- _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:
- _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:
- _objc_msgSend$refreshDownloadedToManager
- _objc_msgSend$refreshSetFoundToManager:
- _objc_msgSend$reportSetCatalogDecideFound:
- _objc_msgSend$setAtomicInstanceForUUID:fromSetAtomicInstances:
- _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:
- _objc_msgSend$setSuspendResumeStatus:
- _objc_msgSend$suspendResumeStatus
- _objc_msgSend$tryPersonalizeSuccess
- _objc_release_x11
- _swift_retain_n
CStrings:
+ "\x01\x12"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} received nil descriptor for entry requiring personalization | nextAtomicEntry:%{public}@"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} received nil set lookup result"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%{public}@} skipping set configuration atomic entry, does not involve personalization or does not require personalization | nextAtomicEntry:%{public}@"
+ "\n[SET-ELIMINATE]{handleSetClientEliminateAtomicRequest} failed client-request that had been waiting for cancel to complete when eliminated | dropEventInfo:%{public}@"
+ "\n{QueueClientRequestBefore1st} queueing singleton check|lock client-request (NOT involving secure content) until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequestBefore1st} queueing singleton check|lock client-request involving secure content until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequestBefore1st} responded to singleton check|lock client-request (NOT involving secure content) | clientRequest:%{public}@"
+ "\n{QueueClientRequest} queueing singleton check|lock client-request (NOT involving secure content) until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequest} queueing singleton check|lock client-request involving secure content until STARTUP_ACTIVATED | clientRequest:%{public}@"
+ "\n{QueueClientRequest} responded to singleton check|lock client-request (NOT involving secure content) | clientRequest:%{public}@"
+ "\x11\x1f\x0f\f"
+ "\x15q/\x03"
+ "\x18\x1a"
+ "%@ | eventInfo:%@"
+ "%@:cancelActiveSetJob"
+ "%@:decrementClientRequestCount"
+ "%@:forceGlobalUnlockFromLocation"
+ "%@:foundAndDownloaded"
+ "%@:foundAndDownloadedSet"
+ "%@:handleSetClientNeedForAtomicRequest"
+ "%@:persistSetJobDescriptor"
+ "%@:refreshDownloadedToManager"
+ "%@:refreshSetFoundToManager"
+ "%@:reportSetCatalogDecideFound"
+ "%@targetBuild:%@"
+ "%@|status:%ld(set:%ld)|jobs:%ld(set:%ld)(setCanceling:%ld)(UUID:%ld)|grants:%ld|configs:%ld|AI:%ld|downloaded:%ld|sched:%ld|timed:%ld|client:%ld"
+ "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)(setJobsCancelingByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
+ "%{%{public}@} (%{public}@)\n[SET-DOWNLOAD] set-download | SUCCESS | autoAssetSetDescriptor:%{public}@"
+ "%{public}@\n[AUTO-STAGER] {%{public}@:_startDetermineJobForNextCandidate} !!!!! SIMULATED TIMEOUT !!!!!"
+ "(%{public}@)\n[SET-DECIDE-FOUND] potential full selector: %{public}@:potentialDescriptor:%{public}@,onFS:%{public}@"
+ "(%{public}@) unable to initialize alreadyOnFilesystemSelector"
+ "/var/run"
+ "2.5.8"
+ "@\"NSObject<OS_nw_activity>\""
+ "@104@0:8@16@24q32@40@48@56@64q72@80@88@96"
+ "@188@0:8@16@24@32@40@48@56@64B72@76q84@92@100@108@116@124@132@140@148@156@164B172B176B180B184"
+ "@340@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272B280B284B288@292@300@308@316@324@332"
+ "@40@0:8@16q24@32"
+ "ADD_AI_FROM_SU_SUSPEND_0   "
+ "AIEligible"
+ "ANOMALY-LATEST-TO-VEND"
+ "Asset failed receipt sha1 check as measurements are not equal"
+ "Asset failed receipt sha256 check as measurements are not equal"
+ "Asset metadata is malformed. \"%@\" is present but is not of type NSData."
+ "Asset metadata lacks a valid measurement to perform streaming extraction"
+ "Asset-Type: (%@) has an overridden URL (%@) that will not be honored."
+ "Asset-Type: (%@) is a 3rd party asset, but contains no server URL."
+ "Audience"
+ "AutoAssetStagerDetermineLastRequiredTimesOut"
+ "AutoAssetSuspendResumeForSUEnabled"
+ "AutoAssetSuspendResumeForSUSetsOverride"
+ "AutoControl-SuspendResume"
+ "B100@0:8@16@24B32@36q44@52@60@68@76q84^@92"
+ "B40@0:8Q16@24@?32"
+ "B44@0:8@16@24B32@36"
+ "B48@0:8@16@24@32B40B44"
+ "B52@0:8@16@24@32q40B48"
+ "B68@0:8@16@24@32B40B44B48@52q60"
+ "BoostConfig"
+ "Cannot start download with nil DownloadInfo"
+ "Certificate is not valid for 3rd party asset map signing: %d"
+ "Configuring download for task:%{public}@ overriding Cellular"
+ "Configuring download for task:%{public}@ overriding Constrained"
+ "Configuring download for task:%{public}@ overriding Expensive"
+ "Configuring download for task:%{public}@ overriding:%{public}@"
+ "Count:%llu|"
+ "CrystalESeed"
+ "DEL_AI_DROP_CACHE_DELETE_LK"
+ "DEL_AI_DROP_CACHE_DELETE_UN"
+ "DEL_AI_DROP_ELIMINATE      "
+ "DEL_AI_DROP_FROM_SU_RESUME0"
+ "DEL_SD_DROP_CACHE_DELETE_LK"
+ "DEL_SD_DROP_CACHE_DELETE_UN"
+ "DEL_SD_DROP_ELIMINATE      "
+ "DownloadFull"
+ "DownloadPatch"
+ "Downloading"
+ "DownloadingAwaitGrant"
+ "DownloadingLookup"
+ "Error while attempting to config download"
+ "FROM_SU_SUSPEND"
+ "HealthReportDontSendOut"
+ "MADAutoAssetSoftwareUpdateSuspendResumeState"
+ "MeasurementSHA256"
+ "MobileAssetSuspendSystemOptionalForSoftwareUpdate.active"
+ "MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce"
+ "No \"%@\" key in asset map, falling back to legacy key \"%@\""
+ "No asset-type in asset map"
+ "OPTIONAL|"
+ "Patching"
+ "PatchingAwaitGrant"
+ "PatchingLookup"
+ "Q24@0:8^@16"
+ "REQUIRED|"
+ "SHA-1"
+ "SHA-256"
+ "SetDownloadFull"
+ "SetDownloadPatch"
+ "SetJobsByIdentifier:%ld(canceling:%ld) | SetStatusByInstance:%ld"
+ "SignatureRSA-SHA256"
+ "Skipping transformation (key: \"%@\" value: \"%@\"): Value cannot be base64 decoded."
+ "Skipping transformation, as asset isn't a dict"
+ "SoftwareUpdateSuspendResume"
+ "Starting built-in MobileAsset brain built Feb 25 2025 22:16:34"
+ "Starting downloaded MobileAsset brain (version: %@) built Feb 25 2025 22:16:34"
+ "SuspendResumeStatus - Issue encountered transitioning to running!"
+ "SuspendResumeStatus - already suspended!"
+ "SuspendResumeStatus - transition to suspended. | eventInfo=%@"
+ "T@\"MADownloadOptions\",R,&,N,V_downloadOptions"
+ "T@\"NSArray\",R,&,N,V_setConfigurationsToEvict"
+ "T@\"NSMutableArray\",&,N,V_queuedRequestsForNewJobOnceCanceled"
+ "T@\"NSMutableDictionary\",&,N,V_cancelingSetJobsByIdentifier"
+ "T@\"NSMutableDictionary\",&,N,V_completionCallbacksBySetJobKey"
+ "T@\"NSMutableDictionary\",&,N,V_evictedCallbacksByAtomicInstanceUUID"
+ "T@\"NSObject<OS_nw_activity>\",&,V_nwActivity"
+ "T@\"NSUUID\",R,&,N,V_nonce"
+ "TB,N,V_boostedToCellular"
+ "TB,N,V_boostedToExpensive"
+ "TB,N,V_configuredToCellular"
+ "TB,N,V_configuredToExpensive"
+ "TB,N,V_configuredToUserInitiated"
+ "TB,N,V_downloadingCellular"
+ "TB,N,V_downloadingExpensive"
+ "TB,N,V_preferenceStagerDetermineLastRequiredTimesOut"
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
+ "Tq,N,V_status"
+ "TryFullAwaitGrant"
+ "TryFullLookup"
+ "TryPatchAwaitGrant"
+ "[%{public}@] {%{public}@}\n[CLEARER-LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "[%{public}@] {%{public}@}\n[SET_CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
+ "[%{public}@] {%{public}@} unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
+ "[%{public}@] {ScheduleSetJobs} suspended for software update (so not scheduling set-job) | schedulerTriggered:%{public}@"
+ "[%{public}@] {addToCurrentJobs} Invariant violation, suspended sets should be handled before this point | selector:%{public}@ | autoJob:%{public}@ | JobUUID:%{public}@ | message:%{public}@ | downloadingDescriptor:%{public}@ | baseForPatchDescriptor:%{public}@"
+ "[%{public}@] {handleSetClientAlterEntriesRepresentingAtomicRequest}\n[ALTER] altered when canceling set-job | setInfoInstance:%{public}@"
+ "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)(fromPSUS:%@)|previousAI:%@(%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate OPTIONAL descriptor (filtered) | nextOptionalDescriptor:%{public}@"
+ "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duplicate REQUIRED descriptor (filtered) | nextRequiredDescriptor:%{public}@"
+ "[MobileAssetHealthReport]: %@ is set, not sending the event to Splunk"
+ "[MobileAssetHealthReport]: Failed to query greymatter eligibility; error: %s"
+ "[clientName:%@|setEntries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)|previousAI:%@(%ld)|(error)available:%@,newer:%@|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
+ "_Measurement-SHA256"
+ "_addCompletionCallbackForSetJobKey:completionCallback:"
+ "_addEvictedCallbackForAtomicInstanceUUID:completionCallback:"
+ "_allPreInstalledDescriptor:forAssetType:"
+ "_boostedToCellular"
+ "_boostedToExpensive"
+ "_cancelingSetJobsByIdentifier"
+ "_completionCallbacksBySetJobKey"
+ "_configuredToCellular"
+ "_configuredToExpensive"
+ "_configuredToUserInitiated"
+ "_constructSetInfoSameFoundFrom"
+ "_constructSetInfoSameFoundFrom:forSetConfiguration:fromSetStatus:"
+ "_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:allowRemovalWithoutNewerDescriptor:fromLocation:"
+ "_downloadingCellular"
+ "_downloadingExpensive"
+ "_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:"
+ "_errorUnlessSameVersionFound:changedReportedError:"
+ "_evictedCallbacksByAtomicInstanceUUID"
+ "_handleEstimateEvictableBytesForSoftwareUpdateRequest done | totalSystemFileSystemSpace:%llu"
+ "_handleEstimateEvictableBytesForSoftwareUpdateRequestWithBytesBySetIdentifier:"
+ "_handleResumeFromSoftwareUpdateRequest"
+ "_handleStatusForSoftwareUpdateRequest"
+ "_handleSuspendForSoftwareUpdateRequestWithNeededBytes:bytesBySetIdentifier:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce"
+ "_handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:"
+ "_handleSuspendForSoftwareUpdate_phaseSuspendedWithNonce:setConfigurationsToEvict:completionBlock:"
+ "_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSelector:forSetAtomicInstance:forLockReason:withDeltaLockCount:withUsagePolicy:withLocalContentURL:withAssetAttributes:"
+ "_nonce"
+ "_nonceFileURL"
+ "_nwActivity"
+ "_persistedKnownDescriptorForFullAssetSelector:"
+ "_persistedKnownDescriptorForPersistedEntryID:"
+ "_preferenceStagerDetermineLastRequiredTimesOut"
+ "_queuedRequestsForNewJobOnceCanceled"
+ "_removeDownloadedSetDescriptorWithNewerDownloadedFromLocation:setDescriptor:allowRemovalWithoutNewerDescriptor:"
+ "_removeIncompleteSetDescriptorFromLocation:incompleteSetDescriptor:historyOperationAI:historyOperationSD:"
+ "_replyHaveStagedContent:withEventInfo:"
+ "_setConfigurationsToEvict"
+ "_softwareUpdateSuspendResumeEligibleSetEntryIDs"
+ "_stateFileURL"
+ "_status"
+ "_updateDownloadOptions:"
+ "_updateUserInitiatedFields"
+ "action_BoostConfig:error:"
+ "addNWActivityToDownloadInfo:andTask:andLabel:"
+ "altered set-configuration converted same-version-found error(s) to SUCCESS | setConfiguration:%@ "
+ "assetConfigJobFinished:withDownloadInfo:error:"
+ "atomic-instance shared lock directory (incomplete set-descriptor atomic-instance)"
+ "attempting to commit pre personalized descriptors"
+ "attempting to heal from set job"
+ "availableBytes"
+ "boostedToCellular"
+ "boostedToExpensive"
+ "byGroupAvailableForStagingAttributes"
+ "cancelActiveSetJob:activeSetJob:"
+ "cancelingSetJobsByIdentifier"
+ "clear"
+ "client-request that had been waiting for set-job to be canceled when set was eliminated"
+ "com.apple.MobileAsset.MobileAssetSHA256Tests"
+ "completionCallbacksBySetJobKey"
+ "configuredToCellular"
+ "configuredToExpensive"
+ "configuredToUserInitiated"
+ "currentStatusWithStateHandle:"
+ "d\x1f\x0f\a\x16<+\x14"
+ "dataWithContentsOfURL:"
+ "dedupAtomicEntries:"
+ "doesSetJobDescriptor:representSameContentAs:"
+ "domain:%@"
+ "downloadingCellular"
+ "downloadingExpensive"
+ "durationSeconds"
+ "evictSetDescriptorIfAwaitingUnlocked"
+ "evictedCallbacksByAtomicInstanceUUID"
+ "forceGlobalUnlock:atomicInstancesHandle:"
+ "forceGlobalUnlockFromLocation:fullAssetSelector:historyOperationAI:historyOperationSD:"
+ "getGreymatterStatus"
+ "handleDownloadConfigJobFinished:withDownloadOptions:configError:"
+ "handleEstimateEvictableBytesForSoftwareUpdateRequest - not in state .Running, unable to estimate."
+ "handleResumeFromSoftwareUpdateRequest - already running"
+ "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:whenCancelingSetJob:alteringFromSetConfiguration:"
+ "handleSetClientEliminateAtomicRequest:whenCancelingSetJob:forAutoJob:"
+ "handleSuspendForSoftwareUpdateRequest - already suspended"
+ "handleSuspendForSoftwareUpdateRequest - bytes needed are unavailable"
+ "handleSuspendForSoftwareUpdateRequest - failed to transition to suspended"
+ "handleSuspendForSoftwareUpdateRequest | unexpectedly empty bytesBySetIdentifier!"
+ "handleSuspendForSoftwareUpdateRequest-spaceCheck"
+ "handleSuspendForSoftwareUpdateRequest-suspendComplete"
+ "handleSuspendResumeForSoftwareUpdateDaemonStartup"
+ "indicateAutoDownloadJobFinished:downloadInfo:performingAutoAssetJob:ofJobType:"
+ "indicateDownloadJobFinished:usingXPCConnection:withXPCMessage:"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:withAavailableForUseError:withNewerVersionError:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
+ "initForConfigFinishedJobID:andDownloadOptions:withError:"
+ "initForSetAtomicInstanceUUID:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "initWithNonce:status:setConfigurationsToEvict:"
+ "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "invalid set-configuration (no set-configuration found) | set-eventInfo:%@"
+ "isNoWaitRequestInvolvingSecureAsset"
+ "isNoWaitRequestInvolvingSecureAsset:"
+ "isSuspendedForSoftwareUpdate:forAssetSetIdentifier:"
+ "keysSortedByValueUsingComparator:"
+ "locateCancelingSetJobForClientDomain:byIdentifier:"
+ "neededBytes"
+ "newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:"
+ "notifyEvictedCallbacksForSetDescriptor"
+ "notifyEvictedCallbacksForSetDescriptor:"
+ "nwActivity"
+ "o\x0f\x03\x1f\b\x112Rh"
+ "objectIsEqual:to:"
+ "permitThirdPartySigningForAssetType:outOrganizations:"
+ "persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:fromLocation:"
+ "persistedKnownDescriptorForSelector"
+ "persistedKnownDescriptorForSetAtomicEntry:"
+ "pre-installed is available as newer-once-personalized"
+ "preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:forAssetType:"
+ "preferenceStagerDetermineLastRequiredTimesOut"
+ "q24@0:8^@16"
+ "q24@?0@8@16"
+ "queuedRequestsForNewJobOnceCanceled"
+ "readyToCommitPrePersonalized:forSetDescriptor:"
+ "recordFailedOperation:fromLayer:failingWithError:forTargetOSVersion:forTargetBuildVersion:"
+ "recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:"
+ "recordFailedOperation:fromLayer:forAssetID:withSelector:failingWithError:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:"
+ "recordFailedOperation:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:failingWithError:"
+ "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:failingWithError:"
+ "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:required:failingWithError:"
+ "recordOperation:toHistoryType:fromLayer:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forClientDomainName:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:forAssetID:withSelector:forTargetOSVersion:forTargetBuildVersion:withOptionalCount:withRequiredCount:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:forAssetSetIdentifier:withSelector:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:forTargetOSVersion:forTargetBuildVersion:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forAssetSetIdentifier:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:"
+ "recordOperation:toHistoryType:fromLayer:withSelector:forTargetOSVersion:forTargetBuildVersion:isRequired:"
+ "recordOperation:toHistoryType:fromLayer:withSelector:fromClient:fromClientDomain:forTargetOSVersion:forTargetBuildVersion:"
+ "refreshDownloadedToManager:"
+ "refreshSetFoundToManager:fromLocation:"
+ "reportSetCatalogDecideFound:fromLocation:"
+ "set-job completed successfully yet did not result in latest-to-vend (newer-once-personalized)"
+ "set-job completed successfully yet did not result in latest-to-vend nor in newer-once-personalized"
+ "set-job completed with error yet have latest-to-vend when availableForUseError | beforeAvailableForUseError:%@"
+ "setAtomicInstance:%@"
+ "setAtomicInstanceUUID"
+ "setBoostedToCellular:"
+ "setBoostedToExpensive:"
+ "setCancelingSetJobsByIdentifier:"
+ "setCompletionCallbacksBySetJobKey:"
+ "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:"
+ "setConfigurationsToEvict"
+ "setConfiguredToCellular:"
+ "setConfiguredToExpensive:"
+ "setConfiguredToUserInitiated:"
+ "setDownloadingCellular:"
+ "setDownloadingExpensive:"
+ "setEvictedCallbacksByAtomicInstanceUUID:"
+ "setNwActivity:"
+ "setPreferenceStagerDetermineLastRequiredTimesOut:"
+ "setQueuedRequestsForNewJobOnceCanceled:"
+ "setStatus:"
+ "set_nw_activity:"
+ "suspendResumeEnabled"
+ "suspended for software update"
+ "suspendedSetConfigurationsFromPreviousOS"
+ "suspendedSetConfigurationsHasCurrentNonce"
+ "targetOS:%@"
+ "time=%@ op=%@ %@ %@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ asset=%@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ set=%@ %@ %@%@%@ %@"
+ "time=%@ op=%@ %@ %@ set=%@ %@%@%@ %@"
+ "totalFileSystemBytes"
+ "totalFilesystemSpace"
+ "v208@0:8q16q24@32q40@48@56@64q72q80q88q96q104@112@120@128@136@144@152@160@168Q176Q184@192@200"
+ "v28@0:8B16@20"
+ "v36@0:8@16@24I32"
+ "v40@0:8q16q24q32"
+ "v44@0:8i16@20@28@36"
+ "v64@0:8q16q24q32@40@48@56"
+ "v68@0:8q16q24q32@40@48@56B64"
+ "v72@0:8q16q24@32@40@48@56@64"
+ "v72@0:8q16q24q32@40@48@56@64"
+ "v80@0:8q16q24q32@40@48@56@64@72"
+ "v92@0:8q16q24@32@40@48@56@64Q72Q80B88"
+ "v92@0:8q16q24q32@40@48@56@64Q72Q80B88"
+ "write"
+ "writeNewSuspendingStateWithNonce:setConfigurationsToEvict:"
+ "{%@:verifySetDescriptorIsLockable} zero atomic-instance entries | setJobDescriptor:%@"
+ "{%@} (%@)\n[DOWNLOADED-TO-MANAGER]  downloadedAsPatch yet no baseForPatch"
+ "{%@} canceling active set-job but unable to form set-job-key | currentSetJob:%@"
+ "{%@} canceling active set-job that is already in canceling table | currentSetJob:%@"
+ "{%@} canceling active set-job that is also already in canceling table | currentSetJob:%@"
+ "{%@} canceling active set-job that is not in routing table | currentSetJob:%@"
+ "{%@} set-job being removed that is not an activeSetJob and not a cancelingSetJob | autoSetJob:%@"
+ "{%@} set-job decrementing client request count when not an activeSetJob and not a cancelingSetJob | eventInfo:%@"
+ "{%@} unable to determine local repository path for nextDownloadedAtomicEntry:%@"
+ "{%@} | unable to create canceling-set-job queue | eventInfo:%@"
+ "{%{public}@ (%{public}@)\n[SET-FOUND] set-job just became set-configuration's latest-to-vend"
+ "{%{public}@}\n[BECAME-LATEST-TO-VEND] adopted set-descriptor as latest-to-vend | setDescriptor:%{public}@"
+ "{%{public}@}\n[FROM-TRACKED-LATEST-TO-VEND] same version found first-tracked as downloaded set-descriptor | setConfiguration:%{public}@"
+ "{%{public}@}\n[FROM-TRACKED-LATEST-TO-VEND] update to set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] [NO_CHANGE] atomic-instance entry requiring personalization | nextAtomicEntry:%{public}@ | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] [NO_CHANGE] no asset-versions are available to the client | setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] not setting latestAtomicInstanceToVend (requiresPersonalization) | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] same version found is always latestAtomicInstanceToVend | setConfiguration:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] set-descriptor matches latest-to-vend when vendingAtomicInstanceForConfiguredEntries=NO | setDescriptor:%{public}@"
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
+ "{%{public}@} Created valid set descriptor from preinstalled set, will adopt as latest to vend."
+ "{%{public}@} Found %lu preinstalled asset descriptor(s) matching assetType: %{public}@"
+ "{%{public}@} Personalization is required to adopt set descriptor."
+ "{%{public}@} Received need for atomic request where latest-to-vend has never been set. Attempting to set latest-to-vend via preinstalled assets."
+ "{%{public}@} processing zero-entries set | setConfiguration:%{public}@"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | unknown persistedStateOperation type | selector:%{public}@ persistedStateOperation:%{public}@"
+ "{AUTO-LOCKER:_refreshFilesystemMetadataLastInterest} asset-lock refresh skipped for set | asset-lock:%{public}@"
+ "{AUTO-LOCKER:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed end-lock(s) | client:%{public}@, selector:%{public}@, reason:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER:currentSetLockUsageEliminatingOtherThanSetAtomicInstances} failed lock | client:%{public}@, selector:%{public}@, reason:%{public}@, policy:%{public}@ | error:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:continuedSetLockByClient} | unable to continue auto-asset lock of the set | setSelector:%{public}@ | continueError:%{public}@"
+ "{AUTO-LOCKER[totalLocks:%ld]:eliminateAllPreviousSetLocksByClient} | unable to end auto-asset all-lock for the set | lockedSetDescriptor:%{public}@ | setSelector:%{public}@ | endedLocksAutoAssetError:%{public}@"
+ "{ScheduleSetJobs}\n[SET_CLIENT_REQUESTS_AWAITING_CANCEL] | scheduled job triggered for set-job that is being canceled - not scheduling | schedulerTriggered:%{public}@"
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
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for array member | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for key | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} found wrong type for value | expected:%@ found:%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} override not set | value:\n%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} override set | value:\n%@"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} unable to alloc NSMutableSet"
+ "{_softwareUpdateSuspendResumeEligibleSetEntryIDs} unexpected nil for setEntryID | clientDomainName:%@ assetSetIdentifier:%@"
+ "{clear} encountered error removing file | fileURL:%@ error:%@"
+ "{clear} unable to allow fileURLs"
+ "{clear} unable to resolve fileManager on clear"
+ "{clear} unable to resolve nonceFileURL"
+ "{clear} unable to resolve stateFileURL"
+ "{currentJobByUUID} unexpected resume of suspended set. | clientDomainName:%@ forAssetSetIdentifier:%@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | additional locked auto-asset for already tracked lock-reason+set-atomic-instance count mismatch - using largest count for set-lock-usage-map | alreadyTrackedCount:%ld | nextLockTracker:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | failed to alloc/init autoAssetSetAtomicInstanceSelector"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | ignoring reason not associated with an asset set | entry:%{public}@ | lockReasonKey:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | set-atomic-instance lock count higher than auto-asset lock count for instance, repairing. | nextLockTracker:%{public}@"
+ "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | set-atomic-instance lock count lower than auto-asset lock count for instance, repairing. | nextLockTracker:%{public}@"
+ "{handleDownloadConfigJobFinished} Failed to config download"
+ "{handleSuspendForSoftwareUpdateRequest} bytes needed unavailable | neededBytes:%llu availableBytes:%llu"
+ "{handleSuspendForSoftwareUpdateRequest} error transitioning to resume!"
+ "{isSuspendedForSoftwareUpdate} isSuspendedForSoftwareUpdate:forAssetSetIdentifier observing nil setEntryID | clientDomainName:%@ assetSetIdentifier:%@"
+ "{isSuspendedForSoftwareUpdate} isSuspendedForSoftwareUpdate:forAssetSetIdentifier observing nil softwareUpdateSuspendResumeEligibleSetEntryIDs"
+ "{isSuspendedForSoftwareUpdate} missing required parameter | clientDomainName:%@ assetSetIdentifier:%@"
+ "{locateCancelingSetJobForClientDomain} missing required | clientDomainName:%@ | assetSetIdentifier:%@"
+ "{notifyEvictedCallbacksForSetDescriptor} unable to remove downloaded set descriptor | setDescriptor:%@"
+ "{suspendedSetConfigurationsHasCurrentNonce} encountered reading suspendResumeNonce file | unarchiveError:%@"
+ "{suspendedSetConfigurationsHasCurrentNonce} unable to resolve nonceFileURL"
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
- "\x11\x1f\x0f\v"
- "\x15q/\x02"
- "\x18\x18"
- "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x"
- "%@|status:%ld(set:%ld)|jobs:%ld(set:%ld)(UUID:%ld)|grants:%ld|configs:%ld|AI:%ld|downloaded:%ld|sched:%ld|timed:%ld|client:%ld"
- "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
- "%{public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-PRE] pre-personalized secure auto-asset to be part of atomic-instance (already pre-personalized) | alreadyOnFilesystemSelector:%{public}@"
- "%{public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-TRY]{reportSetCatalogDecideFound}  secure auto-asset to be part of atomic-instance (requires personalization) | alreadyOnFilesystemSelector:%{public}@"
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
- "2.5.7"
- "@104@0:8@16@24q32@40@48@56@64@72@80@88@96"
- "@172@0:8@16@24@32@40@48@56@64B72@76q84@92@100@108@116@124@132@140@148B156B160B164B168"
- "@332@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264B272B276B280@284@292@300@308@316@324"
- "AUTO-SET-JOB(UserInitiatedSetDownloadNext)"
- "Asset failed receipt check as measurements are not equal"
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
- "B108@0:8@16@24B32@36q44@52@60@68@76@84q92^@100"
- "B44@0:8@16@24@32B40"
- "B64@0:8@16@24@32@40@48^@56"
- "BoostToUserInitiated"
- "CancelingAwaitingThree"
- "Configuring download for task:%{public}@ overriding Cellular:%{public}@ Expensive:%{public}@ Constrained:%{public}@"
- "CrystalSeedUpdate"
- "DownloadAutoFull"
- "DownloadAutoPatch"
- "DownloadUserFull"
- "DownloadUserPatch"
- "DownloadedBoostingHealing"
- "DownloadedGrantBoostHealing"
- "DownloadedLookupBoostHealing"
- "DownloadingAwaitGrantBoosting"
- "DownloadingBoosting"
- "DownloadingLookupBoosting"
- "FailedUserInitiated"
- "LATEST-TO-VEND"
- "MADAutoSetLocker"
- "NowUserInitiated"
- "PERSISTED_SET_DESCRIPTOR"
- "PatchingAwaitGrantBoosting"
- "PatchingBoosting"
- "PatchingLookupBoosting"
- "PersonalizingAwaitGrantBoost"
- "PersonalizingBoosting"
- "PersonalizingLookupBoosting"
- "ReportFailBoostSetDownloadNext"
- "ReportFailureUserInitiated"
- "SetDownloadAutoFull"
- "SetDownloadAutoPatch"
- "SetDownloadUserFull"
- "SetDownloadUserPatch"
- "SetJobsByIdentifier:%ld | SetStatusByInstance:%ld"
- "Skipping asset as it isn't a dict"
- "Starting built-in MobileAsset brain built Feb 17 2025 23:50:46"
- "Starting downloaded MobileAsset brain (version: %@) built Feb 17 2025 23:50:46"
- "SuspendResumeStatus - repair to running."
- "SuspendResumeStatus - transition to running."
- "SuspendResumeStatus - transition to suspended."
- "T\x1f\x0f\x06\x16<+\x14"
- "T@\"NSMutableDictionary\",&,N,V_locksBySelector"
- "Tq,N,V_suspendResumeStatus"
- "TryFullAwaitGrantBoosting"
- "TryFullBoosting"
- "TryFullLookupBoosting"
- "TryPatchAwaitGrantBoosting"
- "TryPatchBoosting"
- "TryPatchLookupBoosting"
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
- "Using server URL for 3rd party MobileAsset | assetType:%@ | defaultServerURL:%@"
- "[%{public}@] {%{public}@:_routeClientRequest} [SET_CLIENT_REQUESTS_AWAITING_SYNC] | job queued since device before first-unlock | eventInfo:%{public}@"
- "[%{public}@] {%{public}@:handleSetClientAlterEntriesRepresentingAtomicRequest} unable to load persisted-set-configuration file | set-eventInfo:%{public}@"
- "[%{public}@] {%{public}@}\n[LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "[%{public}@] {_routeClientRequest}\n[CANCEL-SET-JOB] active set-job being canceled - not considering as active job | set-eventInfo:%{public}@"
- "[(client)Domain:%@,Name:%@|(set)Identifier:%@,Entries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)(fromPSUS:%@)|previousAI:%@(%ld)|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
- "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duuplicate OPTIONAL descriptor (filtered) | nextOptionalDescriptor:%{public}@"
- "[FROM-AVAILABLE-FOR-STAGING] {%{public}@:formAvailableForStagingByCombiningRequiredAndOptional} duuplicate REQUIRED descriptor (filtered) | nextRequiredDescriptor:%{public}@"
- "[clientName:%@|setEntries:%ld|inFlightAI:%@(setID:%@)|oncePersonalized:%@|latestToVend:%@(setID:%@)|previousAI:%@(%ld)|everVended:%@|inhibitScheduling:%@|lookupRsp:%@|vendingForConfig:%@]"
- "_decideRemoveDescriptorWithNewerDownloaded:maintainingRemoveDescriptors:fromLocation:"
- "_endLocksByClient:forAssetClientName:forAllClientNames:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:removingLockCount:endError:"
- "_endLocksByClient:forAssetSelector:forLockReason:removingLockCount:endError:"
- "_lockAutoAssetByClient:forClientProcessName:withClientProcessID:forClientDomainName:forAssetSetIdentifier:forAssetSelector:forSetAtomicInstance:forLockReason:withUsagePolicy:withLocalContentURL:withAssetAttributes:"
- "_locksBySelector"
- "_persistAssetLock:operation:forAssetLock:message:"
- "_removeAssetLock"
- "_removeAssetLock:lastClient:forSelector:message:"
- "_removeDownloadedSetDescriptorWithNewerDownloaded:fromLocation:"
- "_removeSetDeterminedToBeIncomplete"
- "_replyHaveStagedContent:"
- "_suspendResumeStatus"
- "action_BoostToUserInitiated:error:"
- "action_NowUserInitiated:error:"
- "action_ReportFailBoostSetDownloadNext:error:"
- "action_ReportFailureUserInitiated:error:"
- "action_UserInitiatedDownloadNewestFull:error:"
- "action_UserInitiatedSetDownloadNext:error:"
- "additionalLockedByClient:forAssetSelector:forLockReason:withUsagePolicy:lockError:"
- "applyTransforms:toAssets:"
- "assetConfigJobFinished:error:"
- "forceGlobalUnlock:"
- "handleDownloadConfigJobFinished:configError:"
- "handleEstimateEvictableBytesForSoftwareUpdateRequest - not yet implemented"
- "handleResumeFromSoftwareUpdateRequest - not yet implemented"
- "handleSetClientAlterEntriesRepresentingAtomicRequest:forAutoJob:alteringFromSetConfiguration:"
- "handleSetClientEliminateAtomicRequest:forAutoJob:"
- "handleSetClientNeedForAtomicRequest"
- "handleStatusForSoftwareUpdateRequest - not yet implemented"
- "handleSuspendForSoftwareUpdateRequest - not yet implemented"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withDiscoveredInFlightAtomicInstance:withNewerAtomicInstanceOncePersonalized:withLatestAtomicInstanceToVend:withLatestAtomicInstanceToVendFromPreSUStaging:withPreviouslyVendedLockedAtomicInstance:withTicksUntilPreviousForceUnlocked:withMostRecentlyReceivedCachedAssetSetID:withMostRecentlyReceivedDownloadedFromLive:withMostRecentlyReceivedLastTimeChecked:withMostRecentlyReceivedPostedDate:withLatestToVendCachedAssetSetID:withLatestToVendDownloadedFromLive:withLatestToVendLastTimeChecked:withLatestToVendPostedDate:havingEverProvidedLatestToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
- "initForConfigFinishedJobID:withError:"
- "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "invalid set-eventInfo (no set-identifier to be altered) | set-eventInfo:%@"
- "lockedByClient:forAssetSetIdentifier:forAtomicInstance:forLockReason:withUsagePolicy:lockError:"
- "newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:"
- "no next specifier to download (at location UserInitiatedSetDownloadNext)"
- "o\x0f\x04\x1f\a\x11\x112Rd"
- "persistSetJobDescriptor"
- "persistSetJobDescriptor:withCurrentSetStatus:withFirstClientName:"
- "preInstalledSetDescriptor:forClientDomainName:forSetClientName:forAssetSetIdentifier:representingInstanceEntries:"
- "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:"
- "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:withSelectors:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:forPushChannelID:forPopulationType:failingWithError:"
- "refreshDownloadedToManager"
- "refreshSetFoundToManager"
- "refreshSetFoundToManager:"
- "reportSetCatalogDecideFound"
- "reportSetCatalogDecideFound:"
- "setAtomicInstanceForUUID:fromSetAtomicInstances:"
- "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:"
- "setLocksBySelector:"
- "setSuspendResumeStatus:"
- "suspendResumeStatus"
- "time=%@ op=%@ %@ domain=%@ set=%@ %@%@"
- "time=%@ op=%@ %@ domain=%@ set=%@ asset=%@ %@%@"
- "time=%@ op=%@ %@ domain=%@ set=%@ asset=%@%@"
- "time=%@ op=%@ %@ domain=%@ set=%@%@"
- "v168@0:8q16q24@32q40@48@56@64q72q80q88q96q104@112@120@128@136@144@152@160"
- "v52@0:8@16@24@32q40B48"
- "{%@:verifySetDescriptorIsLockable} no downloaded atomic-instance entries | setJobDescriptor:%@"
- "{%{publci}@}\n[LATEST-TO-VEND] just committed all pre-personalized secure | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] [NO_CHANGE] atomic-instance entry requiring personalization | nextAtomicEntry:%{public}@ | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] [NO_CHANGE] no asset-versions are available to the client | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] not setting latestAtomicInstanceToVend (requiresPersonalization) | setJobDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] same version found first-tracked as downloaded set-descriptor | setConfiguration:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] same version found is always latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] set-descriptor matches latest-to-vend when vendingAtomicInstanceForConfiguredEntries=NO | setDescriptor:%{public}@"
- "{%{public}@}\n[LATEST-TO-VEND] update to set-configuration latestAtomicInstanceToVend | setConfiguration:%{public}@"
- "{%{public}@}\n[SELF-HEAL] deduped setDescriptor:%{public}@"
- "{AUTO-LOCKER:%{public}@:_persistAssetLock} | unable to record lock (no persisted-state) for selector:%{public}@"
- "{AUTO-LOCKER:%{public}@:_persistRemoveAssetLock} | unable to remove lock tracker (no persisted-state) for selector:%{public}@"
- "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} | unable to create set-selector | clientDomainName:%{public}@ | assetSetIdentifier:%{public}@"
- "{UserInitiatedSetDownloadNext} invalid nextSetSpecifierToDownload value"
- "{currentSetLockUsageEliminatingOtherThanSetAtomicInstances} | additional locked auto-asset for already tracked lock-reason+set-atomic-instance count mismatch - using first count for set-lock-usage-map | alreadyTrackedCount:%ld | nextLockTracker:%{public}@"
- "{persistSetJobDescriptor}\n[SET-DESCRIPTOR][VEND] update to set-descriptor provided by set-job | justBecameLatestToVend:%{public}@ | setJobDescriptor:%{public}@"
- "{persistSetJobDescriptor} unable to determine local repository path for nextDownloadedAtomicEntry:%@"
- "{refreshDownloadedToManager} downloadedAsPatch yet no baseForPatch"
- "{reportSetCatalogDecideFound} unable to initialize alreadyOnFilesystemSelector"

```
