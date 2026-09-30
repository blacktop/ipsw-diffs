## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.2.1.0.0
-  __TEXT.__text: 0x81c64
+1837.40.40.0.0
+  __TEXT.__text: 0x84a68
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x6294
-  __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x1037b
-  __TEXT.__oslogstring: 0xa457
-  __TEXT.__gcc_except_tab: 0x13a4
-  __TEXT.__unwind_info: 0x1b88
-  __TEXT.__objc_classname: 0x884
-  __TEXT.__objc_methname: 0x14d99
-  __TEXT.__objc_methtype: 0x1788
-  __TEXT.__objc_stubs: 0x8080
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x20a8
-  __DATA_CONST.__objc_classlist: 0x250
+  __TEXT.__objc_methlist: 0x68d4
+  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x11814
+  __TEXT.__oslogstring: 0xa612
+  __TEXT.__gcc_except_tab: 0x13bc
+  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__objc_classname: 0x8ad
+  __TEXT.__objc_methname: 0x16fc2
+  __TEXT.__objc_methtype: 0x1794
+  __TEXT.__objc_stubs: 0x8880
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3078
+  __DATA_CONST.__objc_selrefs: 0x3460
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__objc_arraydata: 0x300
+  __DATA_CONST.__objc_superrefs: 0x228
+  __DATA_CONST.__objc_arraydata: 0x2f8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0xda60
-  __AUTH_CONST.__objc_const: 0x97d0
+  __AUTH_CONST.__cfstring: 0xe4c0
+  __AUTH_CONST.__objc_const: 0xa3e0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x7e4
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0x358
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E4D78AA-EA09-3DD6-AAF9-07D3F59EAA1D
-  Functions: 2755
-  Symbols:   8323
-  CStrings:  6882
+  UUID: EC88E774-A42F-3848-BFA4-DD5B1493A428
+  Functions: 2891
+  Symbols:   8731
+  CStrings:  7302
 
Symbols:
+ +[MAAutoAssetControl stagerOverview:]
+ +[MAAutoAssetControlStagerInformation previousOTASituationName:]
+ +[MAAutoAssetControlStagerInformation supportsSecureCoding]
+ -[MAAutoAssetControl _failedControlStagerOverview:withErrorCode:withResponseError:description:isSynchronous:completion:]
+ -[MAAutoAssetControl _stagerOverview:limitedToAssetTypes:isSynchronous:completion:]
+ -[MAAutoAssetControl _successControlStagerOverview:withStagerInformation:isSynchronous:completion:]
+ -[MAAutoAssetControlStagerInformation .cxx_destruct]
+ -[MAAutoAssetControlStagerInformation activeTargetAvailableForStagingOptionalCount]
+ -[MAAutoAssetControlStagerInformation activeTargetAvailableForStagingRequiredCount]
+ -[MAAutoAssetControlStagerInformation activeTargetCandidateSetConfigurationsOptionalCount]
+ -[MAAutoAssetControlStagerInformation activeTargetCandidateSetConfigurationsRequiredCount]
+ -[MAAutoAssetControlStagerInformation activeTargetCandidatesForStagingOptionalCount]
+ -[MAAutoAssetControlStagerInformation activeTargetCandidatesForStagingRequiredCount]
+ -[MAAutoAssetControlStagerInformation activeTargetOTASituation]
+ -[MAAutoAssetControlStagerInformation alwaysPromoteStagedAssets]
+ -[MAAutoAssetControlStagerInformation assetTargetBuildVersion]
+ -[MAAutoAssetControlStagerInformation assetTargetOSVersion]
+ -[MAAutoAssetControlStagerInformation assetTargetRestoreVersion]
+ -[MAAutoAssetControlStagerInformation assetTargetTrainName]
+ -[MAAutoAssetControlStagerInformation availableForStagingCount]
+ -[MAAutoAssetControlStagerInformation awaitingStagingAttemptCount]
+ -[MAAutoAssetControlStagerInformation baseForStagingDescriptorsCount]
+ -[MAAutoAssetControlStagerInformation candidateSetConfigurationsCount]
+ -[MAAutoAssetControlStagerInformation candidatesForStagingCount]
+ -[MAAutoAssetControlStagerInformation currentStagedLastWrittenBytes]
+ -[MAAutoAssetControlStagerInformation currentStagedRemainingBytes]
+ -[MAAutoAssetControlStagerInformation description]
+ -[MAAutoAssetControlStagerInformation determiningBySelectorCount]
+ -[MAAutoAssetControlStagerInformation eliminationSelectorsAcknowledgedCount]
+ -[MAAutoAssetControlStagerInformation eliminationSelectorsCount]
+ -[MAAutoAssetControlStagerInformation eliminationSetConfigurationCurrentJob]
+ -[MAAutoAssetControlStagerInformation encodeWithCoder:]
+ -[MAAutoAssetControlStagerInformation initWithCoder:]
+ -[MAAutoAssetControlStagerInformation init]
+ -[MAAutoAssetControlStagerInformation loadPersistedPostponed]
+ -[MAAutoAssetControlStagerInformation optionalAssetSizeAllowed]
+ -[MAAutoAssetControlStagerInformation otherTargetAvailableForStagingOptionalCount]
+ -[MAAutoAssetControlStagerInformation otherTargetAvailableForStagingRequiredCount]
+ -[MAAutoAssetControlStagerInformation otherTargetCandidateSetConfigurationsOptionalCount]
+ -[MAAutoAssetControlStagerInformation otherTargetCandidateSetConfigurationsRequiredCount]
+ -[MAAutoAssetControlStagerInformation otherTargetCandidatesForStagingOptionalCount]
+ -[MAAutoAssetControlStagerInformation otherTargetCandidatesForStagingRequiredCount]
+ -[MAAutoAssetControlStagerInformation otherTargetName]
+ -[MAAutoAssetControlStagerInformation otherTargetOTASituation]
+ -[MAAutoAssetControlStagerInformation overallStagedDownloadedSoFarBytes]
+ -[MAAutoAssetControlStagerInformation overallStagedTotalExpectedBytes]
+ -[MAAutoAssetControlStagerInformation persistedAvailableForStagingByTargetCount]
+ -[MAAutoAssetControlStagerInformation persistedStateCount]
+ -[MAAutoAssetControlStagerInformation persistedTargetLookupResultsCount]
+ -[MAAutoAssetControlStagerInformation scheduledJobsCount]
+ -[MAAutoAssetControlStagerInformation setActiveTargetAvailableForStagingOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetAvailableForStagingRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetCandidateSetConfigurationsOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetCandidateSetConfigurationsRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetCandidatesForStagingOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetCandidatesForStagingRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setActiveTargetOTASituation:]
+ -[MAAutoAssetControlStagerInformation setAlwaysPromoteStagedAssets:]
+ -[MAAutoAssetControlStagerInformation setAssetTargetBuildVersion:]
+ -[MAAutoAssetControlStagerInformation setAssetTargetOSVersion:]
+ -[MAAutoAssetControlStagerInformation setAssetTargetRestoreVersion:]
+ -[MAAutoAssetControlStagerInformation setAssetTargetTrainName:]
+ -[MAAutoAssetControlStagerInformation setAvailableForStagingCount:]
+ -[MAAutoAssetControlStagerInformation setAwaitingStagingAttemptCount:]
+ -[MAAutoAssetControlStagerInformation setBaseForStagingDescriptorsCount:]
+ -[MAAutoAssetControlStagerInformation setCandidateSetConfigurationsCount:]
+ -[MAAutoAssetControlStagerInformation setCandidatesForStagingCount:]
+ -[MAAutoAssetControlStagerInformation setConfigurationsCount]
+ -[MAAutoAssetControlStagerInformation setCurrentStagedLastWrittenBytes:]
+ -[MAAutoAssetControlStagerInformation setCurrentStagedRemainingBytes:]
+ -[MAAutoAssetControlStagerInformation setDeterminingBySelectorCount:]
+ -[MAAutoAssetControlStagerInformation setEliminationSelectorsAcknowledgedCount:]
+ -[MAAutoAssetControlStagerInformation setEliminationSelectorsCount:]
+ -[MAAutoAssetControlStagerInformation setEliminationSetConfigurationCurrentJob:]
+ -[MAAutoAssetControlStagerInformation setLoadPersistedPostponed:]
+ -[MAAutoAssetControlStagerInformation setLookupResultsCount]
+ -[MAAutoAssetControlStagerInformation setOptionalAssetSizeAllowed:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetAvailableForStagingOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetAvailableForStagingRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetCandidateSetConfigurationsOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetCandidateSetConfigurationsRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetCandidatesForStagingOptionalCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetCandidatesForStagingRequiredCount:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetName:]
+ -[MAAutoAssetControlStagerInformation setOtherTargetOTASituation:]
+ -[MAAutoAssetControlStagerInformation setOverallStagedDownloadedSoFarBytes:]
+ -[MAAutoAssetControlStagerInformation setOverallStagedTotalExpectedBytes:]
+ -[MAAutoAssetControlStagerInformation setPersistedAvailableForStagingByTargetCount:]
+ -[MAAutoAssetControlStagerInformation setPersistedStateCount:]
+ -[MAAutoAssetControlStagerInformation setPersistedTargetLookupResultsCount:]
+ -[MAAutoAssetControlStagerInformation setScheduledJobsCount:]
+ -[MAAutoAssetControlStagerInformation setSetConfigurationsCount:]
+ -[MAAutoAssetControlStagerInformation setSetLookupResultsCount:]
+ -[MAAutoAssetControlStagerInformation setSetTargetsCount:]
+ -[MAAutoAssetControlStagerInformation setStagingClientDetermineRequestsCount:]
+ -[MAAutoAssetControlStagerInformation setStagingClientDownloadRequestActive:]
+ -[MAAutoAssetControlStagerInformation setStagingClientName:]
+ -[MAAutoAssetControlStagerInformation setStagingClientRequestActive:]
+ -[MAAutoAssetControlStagerInformation setStagingFromBuildVersion:]
+ -[MAAutoAssetControlStagerInformation setStagingFromOSVersion:]
+ -[MAAutoAssetControlStagerInformation setStartupActivelyStagingAssetCount:]
+ -[MAAutoAssetControlStagerInformation setStartupAssetTargetBuildVersion:]
+ -[MAAutoAssetControlStagerInformation setStartupAssetTargetOSVersion:]
+ -[MAAutoAssetControlStagerInformation setStartupAwaitingStagingAssetCount:]
+ -[MAAutoAssetControlStagerInformation setStartupCandidateAssetCount:]
+ -[MAAutoAssetControlStagerInformation setStartupDeterminedAvailableAssetCount:]
+ -[MAAutoAssetControlStagerInformation setStartupLastStagingFromBuildVersion:]
+ -[MAAutoAssetControlStagerInformation setStartupLastStagingFromOSVersion:]
+ -[MAAutoAssetControlStagerInformation setStartupPreviousOTASituation:]
+ -[MAAutoAssetControlStagerInformation setStartupStagedAssetCount:]
+ -[MAAutoAssetControlStagerInformation setStartupStagedAssetTotalContentBytes:]
+ -[MAAutoAssetControlStagerInformation setSuccessfullyStagedCount:]
+ -[MAAutoAssetControlStagerInformation setTargetsCount]
+ -[MAAutoAssetControlStagerInformation stagingClientDetermineRequestsCount]
+ -[MAAutoAssetControlStagerInformation stagingClientDownloadRequestActive]
+ -[MAAutoAssetControlStagerInformation stagingClientName]
+ -[MAAutoAssetControlStagerInformation stagingClientRequestActive]
+ -[MAAutoAssetControlStagerInformation stagingFromBuildVersion]
+ -[MAAutoAssetControlStagerInformation stagingFromOSVersion]
+ -[MAAutoAssetControlStagerInformation startupActivelyStagingAssetCount]
+ -[MAAutoAssetControlStagerInformation startupAssetTargetBuildVersion]
+ -[MAAutoAssetControlStagerInformation startupAssetTargetOSVersion]
+ -[MAAutoAssetControlStagerInformation startupAwaitingStagingAssetCount]
+ -[MAAutoAssetControlStagerInformation startupCandidateAssetCount]
+ -[MAAutoAssetControlStagerInformation startupDeterminedAvailableAssetCount]
+ -[MAAutoAssetControlStagerInformation startupLastStagingFromBuildVersion]
+ -[MAAutoAssetControlStagerInformation startupLastStagingFromOSVersion]
+ -[MAAutoAssetControlStagerInformation startupPreviousOTASituation]
+ -[MAAutoAssetControlStagerInformation startupStagedAssetCount]
+ -[MAAutoAssetControlStagerInformation startupStagedAssetTotalContentBytes]
+ -[MAAutoAssetControlStagerInformation successfullyStagedCount]
+ -[MAAutoAssetControlStagerInformation summary]
+ _OBJC_CLASS_$_MAAutoAssetControlStagerInformation
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetAvailableForStagingOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetAvailableForStagingRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetCandidateSetConfigurationsOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetCandidateSetConfigurationsRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetCandidatesForStagingOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetCandidatesForStagingRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._activeTargetOTASituation
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._alwaysPromoteStagedAssets
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._assetTargetBuildVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._assetTargetOSVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._assetTargetRestoreVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._assetTargetTrainName
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._availableForStagingCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._awaitingStagingAttemptCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._baseForStagingDescriptorsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._candidateSetConfigurationsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._candidatesForStagingCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._currentStagedLastWrittenBytes
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._currentStagedRemainingBytes
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._determiningBySelectorCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._eliminationSelectorsAcknowledgedCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._eliminationSelectorsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._eliminationSetConfigurationCurrentJob
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._loadPersistedPostponed
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._optionalAssetSizeAllowed
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetAvailableForStagingOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetAvailableForStagingRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetCandidateSetConfigurationsOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetCandidateSetConfigurationsRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetCandidatesForStagingOptionalCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetCandidatesForStagingRequiredCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetName
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._otherTargetOTASituation
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._overallStagedDownloadedSoFarBytes
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._overallStagedTotalExpectedBytes
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._persistedAvailableForStagingByTargetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._persistedStateCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._persistedTargetLookupResultsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._scheduledJobsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._setConfigurationsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._setLookupResultsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._setTargetsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingClientDetermineRequestsCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingClientDownloadRequestActive
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingClientName
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingClientRequestActive
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingFromBuildVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._stagingFromOSVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupActivelyStagingAssetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupAssetTargetBuildVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupAssetTargetOSVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupAwaitingStagingAssetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupCandidateAssetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupDeterminedAvailableAssetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupLastStagingFromBuildVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupLastStagingFromOSVersion
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupPreviousOTASituation
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupStagedAssetCount
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._startupStagedAssetTotalContentBytes
+ _OBJC_IVAR_$_MAAutoAssetControlStagerInformation._successfullyStagedCount
+ _OBJC_METACLASS_$_MAAutoAssetControlStagerInformation
+ __OBJC_$_CLASS_METHODS_MAAutoAssetControlStagerInformation
+ __OBJC_$_CLASS_PROP_LIST_MAAutoAssetControlStagerInformation
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetControlStagerInformation
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetControlStagerInformation
+ __OBJC_$_PROP_LIST_MAAutoAssetControlStagerInformation
+ __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetControlStagerInformation
+ __OBJC_CLASS_RO_$_MAAutoAssetControlStagerInformation
+ __OBJC_METACLASS_RO_$_MAAutoAssetControlStagerInformation
+ ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.947
+ ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.415
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.563
+ ___37+[MAAutoAssetControl stagerOverview:]_block_invoke
+ ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.917
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.602
+ ___83-[MAAutoAssetControl _stagerOverview:limitedToAssetTypes:isSynchronous:completion:]_block_invoke
+ ___83-[MAAutoAssetControl _stagerOverview:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_2
+ ___83-[MAAutoAssetControl _stagerOverview:limitedToAssetTypes:isSynchronous:completion:]_block_invoke_3
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.595
+ ___Block_byref_object_copy_.708
+ ___Block_byref_object_copy_.782
+ ___Block_byref_object_dispose_.709
+ ___Block_byref_object_dispose_.783
+ ___block_descriptor_48_e8_32r40r_e57_v24?0"MAAutoAssetControlStagerInformation"8"NSError"16lr32l8r40l8
+ ___block_literal_global.2793
+ ___block_literal_global.2795
+ ___block_literal_global.2797
+ ___block_literal_global.438
+ ___block_literal_global.469
+ ___block_literal_global.475
+ ___block_literal_global.477
+ ___block_literal_global.537
+ ___block_literal_global.654
+ ___block_literal_global.699
+ ___block_literal_global.705
+ ___block_literal_global.707
+ ___block_literal_global.800
+ ___block_literal_global.805
+ ___block_literal_global.807
+ ___block_literal_global.809
+ ___block_literal_global.987
+ ___block_literal_global.989
+ ___block_literal_global.994
+ _objc_msgSend$_failedControlStagerOverview:withErrorCode:withResponseError:description:isSynchronous:completion:
+ _objc_msgSend$_stagerOverview:limitedToAssetTypes:isSynchronous:completion:
+ _objc_msgSend$_successControlStagerOverview:withStagerInformation:isSynchronous:completion:
+ _objc_msgSend$activeTargetAvailableForStagingOptionalCount
+ _objc_msgSend$activeTargetAvailableForStagingRequiredCount
+ _objc_msgSend$activeTargetCandidateSetConfigurationsOptionalCount
+ _objc_msgSend$activeTargetCandidateSetConfigurationsRequiredCount
+ _objc_msgSend$activeTargetCandidatesForStagingOptionalCount
+ _objc_msgSend$activeTargetCandidatesForStagingRequiredCount
+ _objc_msgSend$activeTargetOTASituation
+ _objc_msgSend$alwaysPromoteStagedAssets
+ _objc_msgSend$assetTargetBuildVersion
+ _objc_msgSend$assetTargetOSVersion
+ _objc_msgSend$assetTargetRestoreVersion
+ _objc_msgSend$assetTargetTrainName
+ _objc_msgSend$availableForStagingCount
+ _objc_msgSend$awaitingStagingAttemptCount
+ _objc_msgSend$baseForStagingDescriptorsCount
+ _objc_msgSend$candidateSetConfigurationsCount
+ _objc_msgSend$candidatesForStagingCount
+ _objc_msgSend$currentStagedLastWrittenBytes
+ _objc_msgSend$currentStagedRemainingBytes
+ _objc_msgSend$determiningBySelectorCount
+ _objc_msgSend$eliminationSelectorsAcknowledgedCount
+ _objc_msgSend$eliminationSelectorsCount
+ _objc_msgSend$eliminationSetConfigurationCurrentJob
+ _objc_msgSend$loadPersistedPostponed
+ _objc_msgSend$optionalAssetSizeAllowed
+ _objc_msgSend$otherTargetAvailableForStagingOptionalCount
+ _objc_msgSend$otherTargetAvailableForStagingRequiredCount
+ _objc_msgSend$otherTargetCandidateSetConfigurationsOptionalCount
+ _objc_msgSend$otherTargetCandidateSetConfigurationsRequiredCount
+ _objc_msgSend$otherTargetCandidatesForStagingOptionalCount
+ _objc_msgSend$otherTargetCandidatesForStagingRequiredCount
+ _objc_msgSend$otherTargetName
+ _objc_msgSend$otherTargetOTASituation
+ _objc_msgSend$overallStagedDownloadedSoFarBytes
+ _objc_msgSend$overallStagedTotalExpectedBytes
+ _objc_msgSend$persistedAvailableForStagingByTargetCount
+ _objc_msgSend$persistedStateCount
+ _objc_msgSend$persistedTargetLookupResultsCount
+ _objc_msgSend$previousOTASituationName:
+ _objc_msgSend$scheduledJobsCount
+ _objc_msgSend$setConfigurationsCount
+ _objc_msgSend$setLookupResultsCount
+ _objc_msgSend$setTargetsCount
+ _objc_msgSend$stagingClientDetermineRequestsCount
+ _objc_msgSend$stagingClientDownloadRequestActive
+ _objc_msgSend$stagingClientName
+ _objc_msgSend$stagingClientRequestActive
+ _objc_msgSend$stagingFromBuildVersion
+ _objc_msgSend$stagingFromOSVersion
+ _objc_msgSend$startupActivelyStagingAssetCount
+ _objc_msgSend$startupAssetTargetBuildVersion
+ _objc_msgSend$startupAssetTargetOSVersion
+ _objc_msgSend$startupAwaitingStagingAssetCount
+ _objc_msgSend$startupCandidateAssetCount
+ _objc_msgSend$startupDeterminedAvailableAssetCount
+ _objc_msgSend$startupLastStagingFromBuildVersion
+ _objc_msgSend$startupLastStagingFromOSVersion
+ _objc_msgSend$startupPreviousOTASituation
+ _objc_msgSend$startupStagedAssetCount
+ _objc_msgSend$startupStagedAssetTotalContentBytes
+ _objc_msgSend$successfullyStagedCount
- ___101+[MAAutoAsset stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]_block_invoke.944
- ___119+[MAAutoAsset(SoftwareUpdateSuspendResume) _sendRequestIsSynchronous:fromOperation:messageName:requestInfo:completion:]_block_invoke.412
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.560
- ___65+[MAAutoAsset stageDetermineGroupsAvailableForUpdate:completion:]_block_invoke.914
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.599
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.592
- ___Block_byref_object_copy_.705
- ___Block_byref_object_copy_.779
- ___Block_byref_object_dispose_.706
- ___Block_byref_object_dispose_.780
- ___block_literal_global.2785
- ___block_literal_global.2787
- ___block_literal_global.2789
- ___block_literal_global.435
- ___block_literal_global.466
- ___block_literal_global.472
- ___block_literal_global.474
- ___block_literal_global.520
- ___block_literal_global.651
- ___block_literal_global.679
- ___block_literal_global.685
- ___block_literal_global.687
- ___block_literal_global.797
- ___block_literal_global.802
- ___block_literal_global.804
- ___block_literal_global.806
- ___block_literal_global.984
- ___block_literal_global.986
- ___block_literal_global.988
CStrings:
+ ">>>\nPERSISTED COUNTS:\n                            General: %llu\n                TargetLookupResults: %llu\n        AvailableForStagingByTarget: %llu\n\nSTARTUP:\n           LastStagingFromOSVersion: %@\n        LastStagingFromBuildVersion: %@\n               AssetTargetOSVersion: %@\n            AssetTargetBuildVersion: %@\n                CandidateAssetCount: %llu\n      DeterminedAvailableAssetCount: %llu\n          ActivelyStagingAssetCount: %llu\n          AwaitingStagingAssetCount: %llu\n                   StagedAssetCount: %llu\n       StagedAssetTotalContentBytes: %llu\n               PreviousOTASituation: %@\n               StagingFromOSVersion: %@\n            StagingFromBuildVersion: %@\n\nCONTROL:\n             LoadPersistedPostponed: %@\n          AlwaysPromoteStagedAssets: %@\n\nMOST-RECENT TARGET:\n               AssetTargetOSVersion: %@\n            AssetTargetBuildVersion: %@\n               AssetTargetTrainName: %@\n          AssetTargetRestoreVersion: %@\n           OptionalAssetSizeAllowed: %@\n           ActiveTargetOTASituation: %@\n      ActiveCandidatesRequiredCount: %llu\n      ActiveCandidatesOptionalCount: %llu\n      ActiveSetConfigsRequiredCount: %llu\n      ActiveSetConfigsOptionalCount: %llu\n       ActiveAvailableRequiredCount: %llu\n       ActiveAvaialbleOptionalCount: %llu\n\nOTHER TARGET:\n                    OtherTargetName: %@\n            OtherTargetOTASituation: %@\n       OtherCandidatesRequiredCount: %llu\n       OtherCandidatesOptionalCount: %llu\n       OtherSetConfigsRequiredCount: %llu\n       OtherSetConfigsOptionalCount: %llu\n        OtherAvailableRequiredCount: %llu\n        OtherAvaialbleOptionalCount: %llu\n\nSTAGING-CLIENT REQUESTS:\n                     DetermineCount: %llu\n                     DownloadActive: %@\n                             Active: %@\n                               Name: %@\n\nDETERMINE:\n             SetConfigurationsCount: %llu\n                    SetTargetsCount: %llu\n                 ScheduledJobsCount: %llu\n\nCANDIDATES:\n          CandidatesForStagingCount: %llu\n             SetConfigurationsCount: %llu\n              SetLookupResultsCount: %llu\n     BaseForStagingDescriptorsCount: %llu\n         DeterminingBySelectorCount: %llu\n\nAVAILABLE-OR-STAGED:\n           AvailableForStagingCount: %llu\n        AwaitingStagingAttemptCount: %llu\n            SuccessfullyStagedCount: %llu\n\nPROGRESS:\n    OverallStagedTotalExpectedBytes: %llu\n  OverallStagedDownloadedSoFarBytes: %llu\n      CurrentStagedLastWrittenBytes: %llu\n        CurrentStagedRemainingBytes: %llu\n\nELIMINATION:\n    SelectorsCount: %llu\n    SetConfigurationCurrentJob: %@\n    SelectorsAcknowledgedCount: %llu\n<<<]"
+ "@\"NSNumber\""
+ "CLIENT_ALTERED"
+ "CLIENT_SET_TARGET"
+ "CorruptedAtomicEntries"
+ "DETERMINED_AVAILABLE"
+ "DETERMINED_BLOCKED"
+ "DETERMINED_NO_NEWER"
+ "DETERMINED_PARTIAL"
+ "DETERMINED_PURGED"
+ "DOWNLOADED_BLOCKED"
+ "DOWNLOADED_EMPTIED"
+ "DOWNLOADED_NOTHING"
+ "Dwq\x81"
+ "MA-AUTO-CONTROL(REPLY):STAGER_OVERVIEW"
+ "MA-AUTO-CONTROL:STAGER_OVERVIEW"
+ "MA-auto-control{_failedControlStagerOverview} | %{public}@ | error:%{public}@"
+ "MA-auto-control{_failedControlStagerOverview} | %{public}@ | no client completion block | %{public}@"
+ "MA-auto-control{_successControlStagerOverview} | %{public}@ | no client completion block"
+ "MA-auto-control{_successControlStagerOverview} | %{public}@ | stagerInformation:%{public}@ | SUCCESS"
+ "MA-auto-control{stagerOverview} | no client completion block | %{public}@"
+ "MAAutoAssetControlStagerInformation"
+ "OTA_FROM_LEGACY"
+ "OTA_NEVER"
+ "STAGED_ALL_DESIRED"
+ "STAGED_PARTIAL"
+ "STARTUP{lastStagingFrom:%@(%@)|target:%@(%@)|determined:%llu|staged:%llu(%llu bytes)|situation:%@|from:%@(%@)}|MOST-RECENT{target:%@(%@)|situation:%@|(available)R:%llu,O:%llu}|OTHER{target:%@|situation:%@|(available)R:%llu,O:%llu}|staged:%llu"
+ "T@\"NSNumber\",&,N,V_optionalAssetSizeAllowed"
+ "T@\"NSString\",&,N,V_assetTargetBuildVersion"
+ "T@\"NSString\",&,N,V_assetTargetOSVersion"
+ "T@\"NSString\",&,N,V_assetTargetRestoreVersion"
+ "T@\"NSString\",&,N,V_assetTargetTrainName"
+ "T@\"NSString\",&,N,V_otherTargetName"
+ "T@\"NSString\",&,N,V_stagingClientName"
+ "T@\"NSString\",&,N,V_stagingFromBuildVersion"
+ "T@\"NSString\",&,N,V_stagingFromOSVersion"
+ "T@\"NSString\",&,N,V_startupAssetTargetBuildVersion"
+ "T@\"NSString\",&,N,V_startupAssetTargetOSVersion"
+ "T@\"NSString\",&,N,V_startupLastStagingFromBuildVersion"
+ "T@\"NSString\",&,N,V_startupLastStagingFromOSVersion"
+ "TB,N,V_alwaysPromoteStagedAssets"
+ "TB,N,V_eliminationSetConfigurationCurrentJob"
+ "TB,N,V_loadPersistedPostponed"
+ "TB,N,V_stagingClientDownloadRequestActive"
+ "TB,N,V_stagingClientRequestActive"
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
+ "TQ,N,V_startupActivelyStagingAssetCount"
+ "TQ,N,V_startupAwaitingStagingAssetCount"
+ "TQ,N,V_startupCandidateAssetCount"
+ "TQ,N,V_startupDeterminedAvailableAssetCount"
+ "TQ,N,V_startupStagedAssetCount"
+ "TQ,N,V_startupStagedAssetTotalContentBytes"
+ "TQ,N,V_successfullyStagedCount"
+ "TRIGGER_STAGER_JOB_FINISHED"
+ "Tq,N,V_activeTargetOTASituation"
+ "Tq,N,V_currentStagedLastWrittenBytes"
+ "Tq,N,V_currentStagedRemainingBytes"
+ "Tq,N,V_otherTargetOTASituation"
+ "Tq,N,V_overallStagedDownloadedSoFarBytes"
+ "Tq,N,V_overallStagedTotalExpectedBytes"
+ "Tq,N,V_startupPreviousOTASituation"
+ "_activeTargetAvailableForStagingOptionalCount"
+ "_activeTargetAvailableForStagingRequiredCount"
+ "_activeTargetCandidateSetConfigurationsOptionalCount"
+ "_activeTargetCandidateSetConfigurationsRequiredCount"
+ "_activeTargetCandidatesForStagingOptionalCount"
+ "_activeTargetCandidatesForStagingRequiredCount"
+ "_activeTargetOTASituation"
+ "_alwaysPromoteStagedAssets"
+ "_assetTargetBuildVersion"
+ "_assetTargetOSVersion"
+ "_assetTargetRestoreVersion"
+ "_assetTargetTrainName"
+ "_availableForStagingCount"
+ "_awaitingStagingAttemptCount"
+ "_baseForStagingDescriptorsCount"
+ "_candidateSetConfigurationsCount"
+ "_candidatesForStagingCount"
+ "_currentStagedLastWrittenBytes"
+ "_currentStagedRemainingBytes"
+ "_determiningBySelectorCount"
+ "_eliminationSelectorsAcknowledgedCount"
+ "_eliminationSelectorsCount"
+ "_eliminationSetConfigurationCurrentJob"
+ "_failedControlStagerOverview:withErrorCode:withResponseError:description:isSynchronous:completion:"
+ "_loadPersistedPostponed"
+ "_optionalAssetSizeAllowed"
+ "_otherTargetAvailableForStagingOptionalCount"
+ "_otherTargetAvailableForStagingRequiredCount"
+ "_otherTargetCandidateSetConfigurationsOptionalCount"
+ "_otherTargetCandidateSetConfigurationsRequiredCount"
+ "_otherTargetCandidatesForStagingOptionalCount"
+ "_otherTargetCandidatesForStagingRequiredCount"
+ "_otherTargetName"
+ "_otherTargetOTASituation"
+ "_overallStagedDownloadedSoFarBytes"
+ "_overallStagedTotalExpectedBytes"
+ "_persistedAvailableForStagingByTargetCount"
+ "_persistedStateCount"
+ "_persistedTargetLookupResultsCount"
+ "_scheduledJobsCount"
+ "_setConfigurationsCount"
+ "_setLookupResultsCount"
+ "_setTargetsCount"
+ "_stagerOverview:limitedToAssetTypes:isSynchronous:completion:"
+ "_stagingClientDetermineRequestsCount"
+ "_stagingClientDownloadRequestActive"
+ "_stagingClientName"
+ "_stagingClientRequestActive"
+ "_stagingFromBuildVersion"
+ "_stagingFromOSVersion"
+ "_startupActivelyStagingAssetCount"
+ "_startupAssetTargetBuildVersion"
+ "_startupAssetTargetOSVersion"
+ "_startupAwaitingStagingAssetCount"
+ "_startupCandidateAssetCount"
+ "_startupDeterminedAvailableAssetCount"
+ "_startupLastStagingFromBuildVersion"
+ "_startupLastStagingFromOSVersion"
+ "_startupPreviousOTASituation"
+ "_startupStagedAssetCount"
+ "_startupStagedAssetTotalContentBytes"
+ "_successControlStagerOverview:withStagerInformation:isSynchronous:completion:"
+ "_successfullyStagedCount"
+ "activeTargetAvailableForStagingOptionalCount"
+ "activeTargetAvailableForStagingRequiredCount"
+ "activeTargetCandidateSetConfigurationsOptionalCount"
+ "activeTargetCandidateSetConfigurationsRequiredCount"
+ "activeTargetCandidatesForStagingOptionalCount"
+ "activeTargetCandidatesForStagingRequiredCount"
+ "activeTargetOTASituation"
+ "alwaysPromoteStagedAssets"
+ "assetTargetBuildVersion"
+ "assetTargetOSVersion"
+ "assetTargetRestoreVersion"
+ "assetTargetTrainName"
+ "availableForStagingCount"
+ "awaitingStagingAttemptCount"
+ "baseForStagingDescriptorsCount"
+ "candidateSetConfigurationsCount"
+ "candidatesForStagingCount"
+ "currentStagedLastWrittenBytes"
+ "currentStagedRemainingBytes"
+ "determiningBySelectorCount"
+ "eliminationSelectorsAcknowledgedCount"
+ "eliminationSelectorsCount"
+ "eliminationSetConfigurationCurrentJob"
+ "loadPersistedPostponed"
+ "no stager-information provided by server"
+ "optionalAssetSizeAllowed"
+ "otherTargetAvailableForStagingOptionalCount"
+ "otherTargetAvailableForStagingRequiredCount"
+ "otherTargetCandidateSetConfigurationsOptionalCount"
+ "otherTargetCandidateSetConfigurationsRequiredCount"
+ "otherTargetCandidatesForStagingOptionalCount"
+ "otherTargetCandidatesForStagingRequiredCount"
+ "otherTargetName"
+ "otherTargetOTASituation"
+ "overallStagedDownloadedSoFarBytes"
+ "overallStagedTotalExpectedBytes"
+ "persistedAvailableForStagingByTargetCount"
+ "persistedStateCount"
+ "persistedTargetLookupResultsCount"
+ "previousOTASituationName:"
+ "scheduledJobsCount"
+ "setActiveTargetAvailableForStagingOptionalCount:"
+ "setActiveTargetAvailableForStagingRequiredCount:"
+ "setActiveTargetCandidateSetConfigurationsOptionalCount:"
+ "setActiveTargetCandidateSetConfigurationsRequiredCount:"
+ "setActiveTargetCandidatesForStagingOptionalCount:"
+ "setActiveTargetCandidatesForStagingRequiredCount:"
+ "setActiveTargetOTASituation:"
+ "setAlwaysPromoteStagedAssets:"
+ "setAssetTargetBuildVersion:"
+ "setAssetTargetOSVersion:"
+ "setAssetTargetRestoreVersion:"
+ "setAssetTargetTrainName:"
+ "setAvailableForStagingCount:"
+ "setAwaitingStagingAttemptCount:"
+ "setBaseForStagingDescriptorsCount:"
+ "setCandidateSetConfigurationsCount:"
+ "setCandidatesForStagingCount:"
+ "setConfigurationsCount"
+ "setCurrentStagedLastWrittenBytes:"
+ "setCurrentStagedRemainingBytes:"
+ "setDeterminingBySelectorCount:"
+ "setEliminationSelectorsAcknowledgedCount:"
+ "setEliminationSelectorsCount:"
+ "setEliminationSetConfigurationCurrentJob:"
+ "setLoadPersistedPostponed:"
+ "setLookupResultsCount"
+ "setOptionalAssetSizeAllowed:"
+ "setOtherTargetAvailableForStagingOptionalCount:"
+ "setOtherTargetAvailableForStagingRequiredCount:"
+ "setOtherTargetCandidateSetConfigurationsOptionalCount:"
+ "setOtherTargetCandidateSetConfigurationsRequiredCount:"
+ "setOtherTargetCandidatesForStagingOptionalCount:"
+ "setOtherTargetCandidatesForStagingRequiredCount:"
+ "setOtherTargetName:"
+ "setOtherTargetOTASituation:"
+ "setOverallStagedDownloadedSoFarBytes:"
+ "setOverallStagedTotalExpectedBytes:"
+ "setPersistedAvailableForStagingByTargetCount:"
+ "setPersistedStateCount:"
+ "setPersistedTargetLookupResultsCount:"
+ "setScheduledJobsCount:"
+ "setSetConfigurationsCount:"
+ "setSetLookupResultsCount:"
+ "setSetTargetsCount:"
+ "setStagingClientDetermineRequestsCount:"
+ "setStagingClientDownloadRequestActive:"
+ "setStagingClientName:"
+ "setStagingClientRequestActive:"
+ "setStagingFromBuildVersion:"
+ "setStagingFromOSVersion:"
+ "setStartupActivelyStagingAssetCount:"
+ "setStartupAssetTargetBuildVersion:"
+ "setStartupAssetTargetOSVersion:"
+ "setStartupAwaitingStagingAssetCount:"
+ "setStartupCandidateAssetCount:"
+ "setStartupDeterminedAvailableAssetCount:"
+ "setStartupLastStagingFromBuildVersion:"
+ "setStartupLastStagingFromOSVersion:"
+ "setStartupPreviousOTASituation:"
+ "setStartupStagedAssetCount:"
+ "setStartupStagedAssetTotalContentBytes:"
+ "setSuccessfullyStagedCount:"
+ "setTargetsCount"
+ "stagerInformation"
+ "stagerOverview"
+ "stagerOverview:"
+ "stagingClientDetermineRequestsCount"
+ "stagingClientDownloadRequestActive"
+ "stagingClientName"
+ "stagingClientRequestActive"
+ "stagingFromBuildVersion"
+ "stagingFromOSVersion"
+ "startupActivelyStagingAssetCount"
+ "startupAssetTargetBuildVersion"
+ "startupAssetTargetOSVersion"
+ "startupAwaitingStagingAssetCount"
+ "startupCandidateAssetCount"
+ "startupDeterminedAvailableAssetCount"
+ "startupLastStagingFromBuildVersion"
+ "startupLastStagingFromOSVersion"
+ "startupPreviousOTASituation"
+ "startupStagedAssetCount"
+ "startupStagedAssetTotalContentBytes"
+ "successfullyStagedCount"
+ "v24@?0@\"MAAutoAssetControlStagerInformation\"8@\"NSError\"16"

```
