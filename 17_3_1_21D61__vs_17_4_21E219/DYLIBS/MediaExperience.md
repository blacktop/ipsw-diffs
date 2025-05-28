## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-135.2.0.0.0
-  __TEXT.__text: 0x190b0c
-  __TEXT.__auth_stubs: 0x1db0
-  __TEXT.__objc_methlist: 0x374c
-  __TEXT.__cstring: 0x23fce
-  __TEXT.__const: 0x1938
-  __TEXT.__gcc_except_tab: 0x169c
-  __TEXT.__oslogstring: 0x2b63b
+140.21.1.1.0
+  __TEXT.__text: 0x19a994
+  __TEXT.__auth_stubs: 0x1e20
+  __TEXT.__objc_methlist: 0x39cc
+  __TEXT.__cstring: 0x24b0f
+  __TEXT.__const: 0x1968
+  __TEXT.__gcc_except_tab: 0x17e4
+  __TEXT.__oslogstring: 0x2ccff
   __TEXT.__dlopen_cstrs: 0x503
-  __TEXT.__unwind_info: 0x38e4
-  __TEXT.__objc_classname: 0x388
-  __TEXT.__objc_methname: 0xf470
-  __TEXT.__objc_methtype: 0x18d6
-  __TEXT.__objc_stubs: 0x95c0
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x5bc8
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__unwind_info: 0x3a18
+  __TEXT.__objc_classname: 0x3ce
+  __TEXT.__objc_methname: 0xfb88
+  __TEXT.__objc_methtype: 0x1903
+  __TEXT.__objc_stubs: 0x9b80
+  __DATA_CONST.__got: 0x808
+  __DATA_CONST.__const: 0x5d20
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5a70
-  __DATA_CONST.__objc_selrefs: 0x2870
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x15120
-  __AUTH_CONST.__const: 0x32c8
-  __AUTH_CONST.__objc_const: 0xca0
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_const: 0x5ce8
+  __DATA_CONST.__objc_selrefs: 0x2a00
+  __DATA_CONST.__objc_classrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__cfstring: 0x154e0
+  __AUTH_CONST.__const: 0x33c8
+  __AUTH_CONST.__objc_const: 0xdc0
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x490
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x210
-  __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x5fc
-  __DATA.__data: 0x1fe0
-  __DATA.__common: 0xd0
-  __DATA.__bss: 0x858
+  __DATA.__objc_ivar: 0x62c
+  __DATA.__data: 0x20a0
+  __DATA.__common: 0xb0
+  __DATA.__bss: 0x818
   __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4804
-  Symbols:   15538
-  CStrings:  8611
+  Functions: 4888
+  Symbols:   15853
+  CStrings:  8811
 
Symbols:
+ +[MXAdditiveRoutingManager sharedInstance]
+ +[MXMediaEndowmentManager sharedInstance]
+ +[MXSession(InternalUse) getSetPropertiesOrder]
+ -[AVSystemController grantMediaEndowmentWithEnvironmentID:endowmentPayload:]
+ -[AVSystemController revokeMediaEndowmentWithEnvironmentID:]
+ -[MXAdditiveRoutingManager copyActiveSessionsInfo]
+ -[MXAdditiveRoutingManager copyActiveVoiceOverSessionPlayingToOnDemandVAD]
+ -[MXAdditiveRoutingManager copyAndUpdateSessionInformation:]
+ -[MXAdditiveRoutingManager copyDetailedRouteDescription:]
+ -[MXAdditiveRoutingManager copySessionWithAudioSessionID:]
+ -[MXAdditiveRoutingManager dealloc]
+ -[MXAdditiveRoutingManager detailedRoutesDescription]
+ -[MXAdditiveRoutingManager init]
+ -[MXAdditiveRoutingManager mostRecentActiveSessions]
+ -[MXAdditiveRoutingManager sendActiveSessionsInfoToVA]
+ -[MXAdditiveRoutingManager setDetailedRoutesDescription:]
+ -[MXAdditiveRoutingManager setMostRecentActiveSessions:]
+ -[MXAdditiveRoutingManager setVadIDToName:]
+ -[MXAdditiveRoutingManager setVadNameToID:]
+ -[MXAdditiveRoutingManager updateDetailedRouteDescription:]
+ -[MXAdditiveRoutingManager vadIDToName]
+ -[MXAdditiveRoutingManager vadNameToID]
+ -[MXCoreSession constantOutputVolumeLeveldB]
+ -[MXCoreSession preferredRouteControlFeatures]
+ -[MXCoreSession prefersEchoCancelledInput]
+ -[MXCoreSession setConstantOutputVolumeLeveldB:]
+ -[MXCoreSession setPreferredRouteControlFeatures:]
+ -[MXCoreSession setPrefersEchoCancelledInput:]
+ -[MXCoreSession subscribeToNotifications:]
+ -[MXCoreSession willRouteToOnDemandVADOnActivation]
+ -[MXCoreSessionBase additiveRoutingInfo]
+ -[MXCoreSessionBase applicationState]
+ -[MXCoreSessionBase audioBehaviour]
+ -[MXCoreSessionBase audioDestinationPriority]
+ -[MXCoreSessionBase isRoutedToOnDemandVAD]
+ -[MXCoreSessionBase setApplicationState:]
+ -[MXCoreSessionBase setAudioBehaviour:]
+ -[MXCoreSessionBase setAudioDestinationPriority:]
+ -[MXCoreSessionBase updateAudioBehaviourFromVARouteConfig:]
+ -[MXMediaEndowmentManager dealloc]
+ -[MXMediaEndowmentManager dumpDebugInfo]
+ -[MXMediaEndowmentManager getRecordingAttributions:]
+ -[MXMediaEndowmentManager grantMediaEndowment:environmentID:endowmentPayload:]
+ -[MXMediaEndowmentManager handleEndowmentTreeUpdate]
+ -[MXMediaEndowmentManager init]
+ -[MXMediaEndowmentManager iterateEndowmentTree:rootPID:environment:endowmentLinks:]
+ -[MXMediaEndowmentManager loadMediaEndowments]
+ -[MXMediaEndowmentManager processStateUpdateHandler:process:update:]
+ -[MXMediaEndowmentManager refreshAssertions]
+ -[MXMediaEndowmentManager refreshDomainAssertions:currentlyActivePIDs:]
+ -[MXMediaEndowmentManager refreshEndowmentTrees]
+ -[MXMediaEndowmentManager revokeMediaEndowment:environmentID:]
+ -[MXMediaEndowmentManager storeMediaEndowments]
+ -[MXSession(InterfaceImpl) _beginInterruptionWithSecTask:andFlags:]
+ -[MXSession(InterfaceImpl) _endInterruptionWithSecTask:andStatus:]
+ -[MXSessionManager copyActiveSessionsInfoForAdditiveRouting]
+ -[MXSessionManager copySessionWithAudioSessionID:]
+ -[MXSessionManager(Utilities) canSessionsCoexistDueToIndependentRecording:victim:]
+ -[MXSessionManager(Utilities) interruptAllSessionsAndSystemSounds:]
+ -[MXSessionManager(Utilities) isAirPlaySession:]
+ -[MXSessionManager(Utilities) isSessionUsingBuiltInMic:]
+ -[MXSessionManager(Utilities) isSiriSessionActiveAndRoutedToSiriOutputVAD]
+ -[MXSessionManager(Utilities) sessionUtilizesIndependentRecordingOnly:]
+ -[MXSystemController auditToken]
+ -[MXSystemController bundleID]
+ -[MXSystemController grantMediaEndowmentWithEnvironmentID:endowmentPayload:]
+ -[MXSystemController revokeMediaEndowmentWithEnvironmentID:]
+ -[MXSystemController setAuditToken:]
+ -[MXSystemController setBundleID:]
+ GCC_except_table104
+ GCC_except_table112
+ GCC_except_table121
+ GCC_except_table32
+ GCC_except_table55
+ GCC_except_table73
+ GCC_except_table99
+ _CMSMDevicestate_ItsANonUIBuild
+ _CMSMNotificationUtility_PostSessionRouteControlFeaturesDidChange
+ _CMSMUtility_GetStringForRouteControlFeatures
+ _CMSMVAUtility_WillSessionWithDescriptionRouteToOnDemandVADOnActivation
+ _CMSM_IDSServer_StartAutomaticOwnershipTransferToPhoneTimer
+ _CMSUtility_IsNonIDSClientActiveOnDestination
+ _CMSUtility_IsSomeOtherNonIDSClientActiveWithNonDefaultVADConfiguration
+ _CMSUtility_SetIsRecording.onceToken
+ _CMSessionMgrCopyDisplayIdentifierToSession
+ _FigRouteDiscoveryManagerCopyCachedAudioSessionRouteInformation
+ _FigRouteDiscoveryManagerRunBlockWhileEndpointManagerInfoLockIsLocked
+ _FigRoutingMangerCreateBluetoothEndpointManager.cold.1
+ _HandleDispatchBlockException
+ _MX_FeatureFlags_IsStartupSequenceChangeEnabled
+ _MX_FeatureFlags_IsStartupSequenceChangeEnabled.isStartupSequenceChangeEnabled
+ _MX_FeatureFlags_IsStartupSequenceChangeEnabled.onceToken
+ _NSClassFromString
+ _NSSelectorFromString
+ _OBJC_CLASS_$_MXAdditiveRoutingManager
+ _OBJC_CLASS_$_MXMediaEndowmentManager
+ _OBJC_CLASS_$_MXSessionManagerBase
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_RBSEndowmentGrant
+ _OBJC_CLASS_$_RBSEndowmentTree
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_MXAdditiveRoutingManager._detailedRoutesDescription
+ _OBJC_IVAR_$_MXAdditiveRoutingManager._mostRecentActiveSessions
+ _OBJC_IVAR_$_MXAdditiveRoutingManager._vadIDToName
+ _OBJC_IVAR_$_MXAdditiveRoutingManager._vadNameToID
+ _OBJC_IVAR_$_MXCoreSession._constantOutputVolumeLeveldB
+ _OBJC_IVAR_$_MXCoreSession._preferredRouteControlFeatures
+ _OBJC_IVAR_$_MXCoreSession._prefersEchoCancelledInput
+ _OBJC_IVAR_$_MXCoreSessionBase._applicationState
+ _OBJC_IVAR_$_MXCoreSessionBase._audioBehaviour
+ _OBJC_IVAR_$_MXCoreSessionBase._audioDestinationPriority
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mEndowmentPayloads
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mEndowmentTrees
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mEndowments
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mMediaPlaybackAssertions
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mProcessMonitor
+ _OBJC_IVAR_$_MXMediaEndowmentManager.mSerialQueue
+ _OBJC_IVAR_$_MXSystemController._auditToken
+ _OBJC_IVAR_$_MXSystemController._bundleID
+ _OBJC_METACLASS_$_MXAdditiveRoutingManager
+ _OBJC_METACLASS_$_MXMediaEndowmentManager
+ _OBJC_METACLASS_$_MXSessionManagerBase
+ _SecTaskCopySigningIdentifier
+ __OBJC_$_CLASS_METHODS_MXAdditiveRoutingManager
+ __OBJC_$_CLASS_METHODS_MXMediaEndowmentManager
+ __OBJC_$_INSTANCE_METHODS_MXAdditiveRoutingManager
+ __OBJC_$_INSTANCE_METHODS_MXMediaEndowmentManager
+ __OBJC_$_INSTANCE_VARIABLES_MXAdditiveRoutingManager
+ __OBJC_$_INSTANCE_VARIABLES_MXMediaEndowmentManager
+ __OBJC_$_PROP_LIST_MXAdditiveRoutingManager
+ __OBJC_CLASS_RO_$_MXAdditiveRoutingManager
+ __OBJC_CLASS_RO_$_MXMediaEndowmentManager
+ __OBJC_CLASS_RO_$_MXSessionManagerBase
+ __OBJC_METACLASS_RO_$_MXAdditiveRoutingManager
+ __OBJC_METACLASS_RO_$_MXMediaEndowmentManager
+ __OBJC_METACLASS_RO_$_MXSessionManagerBase
+ __ZNKSt3__16vectorI11VARouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI12CMSRouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI11VARouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI12CMSRouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___31-[MXMediaEndowmentManager init]_block_invoke
+ ___31-[MXMediaEndowmentManager init]_block_invoke_2
+ ___40-[MXMediaEndowmentManager dumpDebugInfo]_block_invoke
+ ___41+[MXMediaEndowmentManager sharedInstance]_block_invoke
+ ___42+[MXAdditiveRoutingManager sharedInstance]_block_invoke
+ ___44-[MXMediaEndowmentManager refreshAssertions]_block_invoke
+ ___48-[MXMediaEndowmentManager refreshEndowmentTrees]_block_invoke
+ ___52-[MXMediaEndowmentManager getRecordingAttributions:]_block_invoke
+ ___62-[MXMediaEndowmentManager revokeMediaEndowment:environmentID:]_block_invoke
+ ___78-[MXMediaEndowmentManager grantMediaEndowment:environmentID:endowmentPayload:]_block_invoke
+ ___CMSMNotificationUtility_PostSessionRouteControlFeaturesDidChange_block_invoke
+ ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.412
+ ___CMSM_IDSServer_StartAutomaticOwnershipTransferToPhoneTimer_block_invoke
+ ___CMSUtility_SetIsRecording_block_invoke
+ ___CMSessionMgrCopyDisplayIdentifierToSession_block_invoke
+ ___FigRouteDiscovererCopyUserSelectionAvailable_block_invoke
+ ___FigRouteDiscoveryManagerCopyRoutePresentForType_block_invoke
+ ___FigRouteDiscoveryManagerLowerBTDiscoveryModeFromDetailed_block_invoke.12
+ ___FigRouteDiscoveryManagerLowerBTDiscoveryModeFromDetailed_block_invoke_2
+ ___MXCoreSessionSetProperty_block_invoke.114
+ ___MXCoreSessionSetProperty_block_invoke.117
+ ___MX_FeatureFlags_IsStartupSequenceChangeEnabled_block_invoke
+ ___MX_SystemStatus_PublishRecordingClientsInfo_block_invoke.20
+ ___block_descriptor_52_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_60_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_60_e8_32o40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_76_e8_32o40o48o56o64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_84_e5_v8?0l
+ ___block_literal_global.107
+ ___block_literal_global.109
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.118
+ ___block_literal_global.119
+ ___block_literal_global.135
+ ___block_literal_global.165
+ ___block_literal_global.193
+ ___block_literal_global.212
+ ___block_literal_global.219
+ ___block_literal_global.255
+ ___block_literal_global.262
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.32
+ ___block_literal_global.411
+ ___block_literal_global.420
+ ___block_literal_global.422
+ ___block_literal_global.50
+ ___block_literal_global.60
+ ___block_literal_global.64
+ ___block_literal_global.68
+ ___block_literal_global.85
+ ___block_literal_global.99
+ ___cmsSetIsPlaying_block_invoke_2
+ ___cmsmInitializeCMSessionManager_block_invoke.25
+ ___cmsmScreenIsBlankedChangedCallback_block_invoke.260
+ ___cmsmSkipPlayingSystemSound_block_invoke
+ ___cmsm_IDSServer_ProcessRemoteInterruptionStartMessage_block_invoke.128
+ ___discoveryManager_appendAvailableEndpoints_block_invoke
+ ___discoveryManager_iOSAppendAvailableEndpoints_block_invoke
+ ___discoveryManager_registerEndpointManager_block_invoke
+ ___discoveryManager_updateDiscoveryModeForType_block_invoke_2
+ ___getOwnershipCondition_block_invoke
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ ___mx_runningBoardServices_initializeMonitoring_block_invoke.26
+ ___mx_runningBoardServices_initializeMonitoring_block_invoke.36
+ _abort_with_reason
+ _cmsmSkipPlayingSystemSound.onceToken
+ _cmsmSkipPlayingSystemSound.unskippableSystemSounds
+ _gApplicationStateCache
+ _gApplicationStateCacheLock
+ _gVAEM.23
+ _getOwnershipCondition.onceToken
+ _getOwnershipCondition.sOwnershipCondition
+ _kAVSystemControllerMediaEndowmentPayload_RecordingWebsite
+ _kCMSessionPowerLogAudioPlaybackOperation_DataUpdate
+ _kFigSystemControllerXPCMsgParam_EndowmentPayload
+ _kFigSystemControllerXPCMsgParam_EnvironmentID
+ _kMXSessionAudioMode_EchoCancellationVoice
+ _kMXSessionNotificationKey_RouteControlFeaturesDidChange_HasEchoCancelledInput
+ _kMXSessionNotificationKey_RouteControlFeaturesDidChange_RouteControlFeatures
+ _kMXSessionNotification_RouteControlFeaturesDidChange
+ _kMXSessionProperty_AvailableRouteControlFeatures
+ _kMXSessionProperty_AvailableRouteControlFeaturesKey_EchoCancelledInput
+ _kMXSessionProperty_AvailableRouteControlFeaturesKey_RouteControlFeatures
+ _kMXSessionProperty_ConstantOutputVolumeLeveldB
+ _kMXSessionProperty_CoreSessionIDInternal
+ _kMXSessionProperty_HasEchoCancelledInput
+ _kMXSessionProperty_PreferredRouteControlFeatures
+ _kMXSessionProperty_PreferredRouteControlFeaturesKey_RouteControlFeatures
+ _kMXSessionProperty_PrefersEchoCancelledInput
+ _kMXSessionProperty_RouteControlFeatures
+ _kMXSessionProperty_RouteControlFeaturesKey_RouteControlFeatures
+ _kMXSystemControllerMediaEndowmentPayload_AuditToken
+ _kMXSystemControllerMediaEndowmentPayload_BundleID
+ _kMXSystemControllerMediaEndowmentPayload_RecordingWebsite
+ _kMXSystemControllerProperty_ClientAuditToken
+ _kMXSystemStatusInfo_RecordingClientAttributedAuditToken
+ _kVirtualAudioPlugInSessionDescriptionPreferIndependentRoute_CFString
+ _kVirtualAudioPlugInSessionDescriptionSharingKey_CFString
+ _mx_runningBoardServices_removePIDFromApplicationStateCache
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_beginInterruptionWithSecTask:andFlags:
+ _objc_msgSend$_endInterruptionWithSecTask:andStatus:
+ _objc_msgSend$additiveRoutingInfo
+ _objc_msgSend$bundleID
+ _objc_msgSend$canSessionsCoexistDueToIndependentRecording:victim:
+ _objc_msgSend$childrenLinks:
+ _objc_msgSend$constantOutputVolumeLeveldB
+ _objc_msgSend$copyActiveSessionsInfo
+ _objc_msgSend$copyActiveSessionsInfoForAdditiveRouting
+ _objc_msgSend$copyActiveVoiceOverSessionPlayingToOnDemandVAD
+ _objc_msgSend$copyAndUpdateSessionInformation:
+ _objc_msgSend$copySessionWithAudioSessionID:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$dumpDebugInfo
+ _objc_msgSend$endowmentTreeForNamespace:
+ _objc_msgSend$getRecordingAttributions:
+ _objc_msgSend$grantMediaEndowment:environmentID:endowmentPayload:
+ _objc_msgSend$grantMediaEndowmentWithEnvironmentID:endowmentPayload:
+ _objc_msgSend$grantWithNamespace:endowment:
+ _objc_msgSend$handleEndowmentTreeUpdate
+ _objc_msgSend$initWithSet:
+ _objc_msgSend$isAirPlaySession:
+ _objc_msgSend$isRoutedToOnDemandVAD
+ _objc_msgSend$isSiriSessionActiveAndRoutedToSiriOutputVAD
+ _objc_msgSend$iterateEndowmentTree:rootPID:environment:endowmentLinks:
+ _objc_msgSend$loadMediaEndowments
+ _objc_msgSend$mostRecentActiveSessions
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$performSelector:
+ _objc_msgSend$preferredRouteControlFeatures
+ _objc_msgSend$prefersEchoCancelledInput
+ _objc_msgSend$previousState
+ _objc_msgSend$processStateUpdateHandler:process:update:
+ _objc_msgSend$refreshAssertions
+ _objc_msgSend$refreshDomainAssertions:currentlyActivePIDs:
+ _objc_msgSend$refreshEndowmentTrees
+ _objc_msgSend$revokeMediaEndowment:environmentID:
+ _objc_msgSend$revokeMediaEndowmentWithEnvironmentID:
+ _objc_msgSend$rootLinks
+ _objc_msgSend$sendActiveSessionsInfoToVA
+ _objc_msgSend$sessionUtilizesIndependentRecordingOnly:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setConstantOutputVolumeLeveldB:
+ _objc_msgSend$setMostRecentActiveSessions:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setPreferredRouteControlFeatures:
+ _objc_msgSend$setPrefersEchoCancelledInput:
+ _objc_msgSend$storeMediaEndowments
+ _objc_msgSend$subscribeToNotifications:
+ _objc_msgSend$targetEnvironment
+ _objc_msgSend$targetPid
+ _objc_msgSend$targetWithPid:environmentIdentifier:
+ _objc_msgSend$waitUntilDate:
+ _objc_msgSend$willRouteToOnDemandVADOnActivation
+ _objc_terminate
+ _predictedRouting_UpdatePredictedRoute.sSystemMusicIsIndependent
+ _remoteSystemController_createMediaEndowment
+ _remoteSystemController_invalidateMediaEndowment
+ _sFigBufferedAirPlayGlobalRoutingRegistryStartServer
+ _systemController_GrantMediaEndowment
+ _systemController_RevokeMediaEndowment
+ _vaeSignalOwnershipIsTaken
+ _vaemGetVirtualAudioPlugin
+ _vaemIsDefaultVADInItsDefaultConfiguration
+ _vaemIsPersistentRouteActive
+ _vaemSetStreamASBD
+ _vaemUpdateCurrentOutputRoutesInfo
- +[MXSession(InternalUse) copySetPropertiesOrder]
- -[MXCoreSession applicationState]
- -[MXCoreSession audioBehaviour]
- -[MXCoreSession audioDestinationPriority]
- -[MXCoreSession hasEntitlementForWebsiteInfo]
- -[MXCoreSession setApplicationState:]
- -[MXCoreSession setAudioBehaviour:]
- -[MXCoreSession setAudioDestinationPriority:]
- -[MXCoreSession setHasEntitlementForWebsiteInfo:]
- -[MXSession(InterfaceImpl) _beginInterruptionWithSecTask:flags:]
- -[MXSession(InterfaceImpl) _endInterruptionWithSecTask:interruptionStatus:]
- -[MXSessionManager copyDetailedRouteDescription:]
- -[MXSessionManager copySessionInformationFromVARouteConfiguration:]
- -[MXSessionManager setVadIDToName:]
- -[MXSessionManager setVadNameToID:]
- -[MXSessionManager updateActiveSessionInformation]
- -[MXSessionManager updateDetailedRouteDescription:]
- -[MXSessionManager vadIDToName]
- -[MXSessionManager vadNameToID]
- GCC_except_table102
- GCC_except_table107
- GCC_except_table108
- GCC_except_table119
- GCC_except_table40
- GCC_except_table97
- _CMSMUtility_CopyCMSessionWithAudioSessionID
- _CMSMVAUtility_CopyActiveSessionsInfoForAdditiveRouting
- _CMSMVAUtility_CopyActiveVoiceOverSessionPlayingToOnDemandVAD
- _CMSMVAUtility_CopySessionInfoForAdditiveRouting
- _CMSMVAUtility_IsAirPlayLowLatencyPortAvailable
- _CMSUtility_IsSessionRoutedToOnDemandVAD
- _CMSUtility_WillSessionGoingActiveRouteToOnDemandVAD
- _FigRoutingMangerCreateBluetoothEndpointManager.sBluetoothEndpointManagerSetup
- _MXSessionCopySetPropertiesOrder
- _OBJC_IVAR_$_MXCoreSession._applicationState
- _OBJC_IVAR_$_MXCoreSession._audioBehaviour
- _OBJC_IVAR_$_MXCoreSession._audioDestinationPriority
- _OBJC_IVAR_$_MXCoreSession._hasEntitlementForWebsiteInfo
- _OBJC_IVAR_$_MXSessionManager._vadIDToName
- _OBJC_IVAR_$_MXSessionManager._vadNameToID
- __ZNKSt3__16vectorI11VARouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI12CMSRouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI11VARouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI12CMSRouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___CMSMUtility_UpdateSharePlayVolumeBehaviours_block_invoke.398
- ___FigRoutingMangerCreateBluetoothEndpointManager_block_invoke
- ___FigRoutingMangerCreateBluetoothEndpointManager_block_invoke.cold.1
- ___MXCoreSessionSetProperty_block_invoke.128
- ___MXCoreSessionSetProperty_block_invoke.131
- ___MX_SystemStatus_PublishRecordingClientsInfo_block_invoke.22
- ___block_descriptor_68_e8_32o40o48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.133
- ___block_literal_global.147
- ___block_literal_global.164
- ___block_literal_global.189
- ___block_literal_global.192
- ___block_literal_global.218
- ___block_literal_global.225
- ___block_literal_global.23
- ___block_literal_global.261
- ___block_literal_global.268
- ___block_literal_global.272
- ___block_literal_global.275
- ___block_literal_global.29
- ___block_literal_global.3
- ___block_literal_global.38
- ___block_literal_global.397
- ___block_literal_global.406
- ___block_literal_global.408
- ___block_literal_global.59
- ___block_literal_global.61
- ___block_literal_global.67
- ___block_literal_global.84
- ___block_literal_global.95
- ___cmsCopyDisplayIdentifierToSession_block_invoke
- ___cmsSetIsPlaying_block_invoke.119
- ___cmsmInitializeCMSessionManager_block_invoke.24
- ___cmsmScreenIsBlankedChangedCallback_block_invoke.266
- ___cmsm_IDSServer_ProcessLocalIsPlayingDoneMessage_block_invoke
- ___cmsm_IDSServer_ProcessRemoteInterruptionStartMessage_block_invoke.125
- ___mx_runningBoardServices_initializeMonitoring_block_invoke.27
- ___mx_runningBoardServices_initializeMonitoring_block_invoke.37
- _gOwnershipStatusSemaphore
- _gVAEM.22
- _gVAEM.47
- _kMXPreferredVolumeManagerNotificationKey_ActiveAudioCategory
- _kMXSystemControllerProperty_ClientSecTask
- _kMXSystemStatusInfo_RecordingClientHasEntitlementForWebsite
- _mx_runningBoardServices_createAndStoreAssertionForPIDWithInvalidationHandler
- _objc_msgSend$_beginInterruptionWithSecTask:flags:
- _objc_msgSend$_endInterruptionWithSecTask:interruptionStatus:
- _objc_msgSend$copySessionInformationFromVARouteConfiguration:
- _objc_msgSend$copySetPropertiesOrder
- _objc_msgSend$getCleanupSessionAssertionReasonString:
- _objc_msgSend$hasEntitlementForWebsiteInfo
- _objc_msgSend$setHasEntitlementForWebsiteInfo:
- _objc_msgSend$updateActiveSessionInformation
- _vaeSignalOwnershipStatusSemaphore
- _vaemSetActiveSessionsInfoRouteConfigurationDictionaryOnVAD
CStrings:
+ "%{public}s %{public}s:%i Invalidating unaccounted assertion %p for reason %u as its explanation contains matching session id %{public}@"
+ "%{public}s %{public}s:%i Resetting Default VAD to Audio/Video as no other non IDS client is active on VAD"
+ "%{public}s %{public}s:%i Resetting Default VAD to Audio/Video as there are no ther non IDS clients active on VAD with non Default VAD configuration"
+ "-AVSystemController- %s: grantMediaEndowmentWithEnvironmentID:endowmentPayload: returned error %d"
+ "-AVSystemController- %s: revokeMediaEndowmentWithEnvironmentID: returned error %d"
+ "-CMSMNotificationUtilities- %s: Posting %{public}@ for %{public}@ [%p] with payload %{public}@."
+ "-CMSMUtilities- %s: Returning AudioQueueOptions for session %{public}@ [%p] duckVolume = %0.3f fadeDuration = %0.3f isSilentMute = %{BOOL}u"
+ "-CMSMUtilities- %s: Using host process attribution attribution {attributedEntityBundleID:%{public}@}"
+ "-CMSMUtilities- %s: Using media endowment attribution {attributedEntityBundleID:%{public}@}"
+ "-CMSM_IDSServer- %s: Ignore idle timer since current route is not builtin."
+ "-CMSUtilities- %s: Interruptor %{public}@ and victim %{public}@ can coexist because one is record-only, using independent resources, and mixes with everyone."
+ "-CMSUtilities- %s: Returning consolidatedSourceFormatInfo for MXCoreSession %{public}@ "
+ "-CMSessionMgr- %s: Available route control features are %{public}@, is echo-cancelled input available? = %{BOOL}u for session %{public}@ [%p] with %{public}@ category; willRouteToOnDemandVADOnActivation = %{BOOL}u."
+ "-CMSessionMgr- %s: Client %{public}@ [%p] changing %{public}@ to %{BOOL}u"
+ "-CMSessionMgr- %s: Client %{public}@ [%p] hasEchoCancelledInput = %{BOOL}u; isRoutedToOnDemandVAD = %{BOOL}u, category = %{public}@."
+ "-CMSessionMgr- %s: Client %{public}@ [%p] setting %{public}@ to %{public}@; session is active = %{BOOL}u"
+ "-CMSessionMgr- %s: Client '%{public}@' changed isRecordingMuted to %{BOOL}u"
+ "-CMSessionMgr- %s: Client '%{public}@' resetting WantsToPauseSpokenAudio while it's active"
+ "-CMSessionMgr- %s: Client '%{public}@' setting WantsToPauseSpokenAudio to '%{BOOL}u'"
+ "-CMSessionMgr- %s: CurrentSpeechDetectionDeviceSampleRate=%{public}@ using %{public}@"
+ "-CMSessionMgr- %s: Resetting start and stop play time for client session %{public}@ current active state %{BOOL}u new active state %{BOOL}u"
+ "-CMSessionMgr- %s: Session %{public}@ [%p] setting %{public}@ to %{public}@."
+ "-CMSessionMgr- %s: Session %{public}@ [%p] will play to on-demand VAD, resetting flags to 0 since it should not control routing nor volume."
+ "-CMSessionMgr- %s: Session %{public}@ is routed to an on-demand VAD, letting %{public}@ keep their flags."
+ "-CMSessionMgr- %s: Skipping trying to take control as session %{public}@ [%p] is routed to an on-demand VAD."
+ "-CMVAEndpoint- %s: Ownership is taken, blocked for %0.3f ms"
+ "-CMVAEndptMgr- %s: ERROR getting AudioObjectID for the VirtualAudio plug-in (result = 0x%.08X, AudioObjectID = %lu). This is a serious error.  Please file a radar against Audio - Routing"
+ "-CMVAEndptMgr- %s: Failed to get default VADID, err='%c%c%c%c'"
+ "-CMVAEndptMgr- %s: Route changed. Reason '%c%c%c%c' (%{public}@)."
+ "-CMVAEndptMgr- %s: VA Initialization failed virtualDevicePlugInID=%u, err=%c%c%c%c"
+ "-CMVAEndptMgr- %s: VA initialization ended - Elapsed time=%.3f milliseconds"
+ "-CMVAEndptMgr- %s: VA initialization started"
+ "-CMVAEndptUtl- %s: No session information provided!"
+ "-FigEndpointUIAgent- %s: Showing error prompt for endpointUIAgent [%p]"
+ "-FigPredictedRouting- %s: Called due to reason=%{public}@, isBTManagedPortPresent=%{BOOL}u, isBTManagedPortInEar=%{BOOL}u, routeIsBuiltIn=%{BOOL}u, predictedRouteConditionChanged=%{BOOL}u, cachedSessionIsPlaying=%{BOOL}u, predictedRouteChanged=%{BOOL}u, sSystemMusicIsIndependent=%{BOOL}u, predictedRouteChangedForSystemMusic=%{BOOL}u, predictedRouteName=%{public}@, predictedRouteUID=%{private}@"
+ "-FigRouteDiscoveryManager- %s: Not adding watchdog for this device."
+ "-FigRoutingManager_SystemRemotePool- %s: Endpoint with name=%{public}@ is getting added to SystemRemotePool aggregate"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: This is unexpected. Please file a radar to MediaExperience (New Bugs) | All."
+ "-MXAdditiveRoutingManager- %s: Cache doesn't contain the requested detailed route description for virtualAudioDeviceID=%u"
+ "-MXAdditiveRoutingManager- %s: Device info missing deviceID and deviceUID!"
+ "-MXAdditiveRoutingManager- %s: Failed to get detailed route description for %{public}@"
+ "-MXAdditiveRoutingManager- %s: NOTICE: Active session %{public}@ [%p] has lost an on-demand VAD, call BeginInterruption again."
+ "-MXAdditiveRoutingManager- %s: Removing %{public}@ from detailed route descriptions."
+ "-MXAdditiveRoutingManager- %s: Resetting default audio behaviour for session %{public}@ who's VADs went away."
+ "-MXAdditiveRoutingManager- %s: Session not found for audio session ID %d"
+ "-MXAdditiveRoutingManager- %s: Setting route configuration %{public}@ for active sessions."
+ "-MXAdditiveRoutingManager- %s: Updating audio behaviour for %{public}@ with audioSessionID %d from %{public}@."
+ "-MXAdditiveRoutingManager- %s: Updating detailed route description for %{public}@ with deviceID %{public}@"
+ "-MXAdditiveRoutingManager- %s: Updating maps; IDToName = %{public}@ and NameToID = %{public}@"
+ "-MXAdditiveRoutingManager- %s: Updating session %{public}@ to %{public}@ after VAD went away."
+ "-MXAdditiveRoutingManager- %s: cmsBeginInterruptionGuts returned err = %d, INTERRUPTING %{public}@ [%p]."
+ "-MXAdditiveRoutingManager- %s: vaemSetRouteConfigurationDictionaryOnVAD of SetActiveSessionInfoOnVA failed with %d / `%{public}.4s'\n"
+ "-MXCoreSession_Embedded- %s: Encountered error %d querying On-demand-VAD support for session %{public}@ [%p] with additive routing info: %{public}@."
+ "-MXCoreSession_Embedded- %s: Will session %{public}@ [%p] with info %{public}@ route to an on-demand VAD? %{BOOL}u"
+ "-MXInitialzation_Embedded- %s: FigBufferedAirPlayGlobalRoutingRegistryStartServer is NULL"
+ "-MXMediaEndowmentManager- %s: \t\t\t\t %{public}@: '%{public}@',"
+ "-MXMediaEndowmentManager- %s: \t\t\t %{public}@ = {"
+ "-MXMediaEndowmentManager- %s: \t\t\t %{public}@: '%{public}@',"
+ "-MXMediaEndowmentManager- %s: \t\t\t %{public}@: ['%{public}@'],"
+ "-MXMediaEndowmentManager- %s: \t\t\t }"
+ "-MXMediaEndowmentManager- %s: \t\t %{public}@ = {"
+ "-MXMediaEndowmentManager- %s: \t\t %{public}@: '%{public}@'"
+ "-MXMediaEndowmentManager- %s: \t\t }"
+ "-MXMediaEndowmentManager- %s: \t ================================================== %{public}@ Debug Info =================================================="
+ "-MXMediaEndowmentManager- %s: \t ======================================================================================================================================="
+ "-MXMediaEndowmentManager- %s: \t mEndowmentPayloads = {"
+ "-MXMediaEndowmentManager- %s: \t mEndowmentTrees = {"
+ "-MXMediaEndowmentManager- %s: \t mEndowments = {"
+ "-MXMediaEndowmentManager- %s: \t mMediaPlaybackAssertions = {"
+ "-MXMediaEndowmentManager- %s: \t }"
+ "-MXMediaEndowmentManager- %s: %{public}@ assertion has been invalidated! clientPID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: %{public}@ assertion is taken successfully! clientPID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: All endowments were revoked from clientPID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Assertions endowment was granted to process '{name=%{public}@, pid=%d}'"
+ "-MXMediaEndowmentManager- %s: Assertions endowment was revoked from process '{name=%{public}@, pid=%d}'"
+ "-MXMediaEndowmentManager- %s: Endowment was granted successfully! clientPID='%{public}@', environmentID='%{public}@', endowmentPayload='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Endowment was not found! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Endowment was not recovered! clientPID='%{public}@', environmentID='%{public}@', endowmentPayload='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Endowment was recovered successfully! clientPID='%{public}@', environmentID='%{public}@', endowmentPayload='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Endowment was revoked successfully! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Failed to create RBSAssertion! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Failed to create RBSEndowmentGrant! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Failed to create RBSTarget! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Missing required parameter! clientPID='%d', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Missing required parameter! clientPID='%d', environmentID='%{public}@', auditTokenData='%{public}@', bundleID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: RBSAssertion acquisition failed! clientPID='%{public}@', assertion='%{public}@', error='%{public}@'"
+ "-MXMediaEndowmentManager- %s: RBSAssertion acquisition failed! clientPID='%{public}@', environmentID='%{public}@', assertion='%{public}@', error='%{public}@'"
+ "-MXMediaEndowmentManager- %s: Revoking old endowment! clientPID='%{public}@', environmentID='%{public}@'"
+ "-MXMediaEndowmentManager- %s: System is booting up, media endowments cache was cleared"
+ "-MXMediaEndowmentManager- %s: Unexpected DomainName %{public}@"
+ "-MXSession- %s: %{public}@ setting mutePriority to %{public}@ from existing mutePriority %{public}@"
+ "-MXSessionManager- %s: Failed to retrieve session info dictionary for %{public}@ [%p]."
+ "-MXSessionManagerUtilities- %s: Interruptor %{public}@ and victim %{public}@ %{public}@ co-exist because %{public}@ %{public}@ entitlement to record during call."
+ "-MXSessionManagerUtilities- %s: Interruptor %{public}@ or victim %{public}@ has SoundRecognition mode, sessions can co-exist while active."
+ "-MXSessionManagerUtilities- %s: MXSessionManager INTERRUPTING '%{public}@' because %{public}@"
+ "-MXSystemSounds- %s: Calling AudioToolbox::AudioSessionKillClientSystemSounds before it gets set! Please file a radar against 'MediaExperience Session | All'"
+ "-MXSystemSounds- %s: Suppressing system sound because Wombat is enabled!"
+ "-MXSystemSounds- %s: SystemSound is unskippable!"
+ "-MXSystemSounds- %s: SystemSound plists haven't been loaded, no system sound will play or vibrate!"
+ "-MX_FeatureFlags- %s: VirtualAudio/startup_sequence_change feature is %{public}s"
+ "-MX_RunningBoardServices- %s: %{public}@:\t\t %{public}@"
+ "-MX_RunningBoardServices- %s: -------------------------- Application State Cache --------------------------"
+ "-MX_RunningBoardServices- %s: Failed to create RBSProcessHandle for %{public}@"
+ "-MX_RunningBoardServices- %s: PID cannot be nil nor zero! pid=%{public}@"
+ "-MX_RunningBoardServices- %s: Process '%{public}@' state is updated to '%{public}@'"
+ "-MX_SystemStatus- %s: Creating ST attribution info object with ActiveEntity %{public}@, ActiveEntity executablePath: %{public}@, AttributedEntity bundleID: %{public}@ pid: %d"
+ "-MX_SystemStatus- %s: Publishing recording clients info while SystemStatus is not initialized!"
+ "-[AVSystemController grantMediaEndowmentWithEnvironmentID:endowmentPayload:]"
+ "-[AVSystemController revokeMediaEndowmentWithEnvironmentID:]"
+ "-[MXAdditiveRoutingManager copyAndUpdateSessionInformation:]"
+ "-[MXAdditiveRoutingManager copyDetailedRouteDescription:]"
+ "-[MXAdditiveRoutingManager sendActiveSessionsInfoToVA]"
+ "-[MXAdditiveRoutingManager updateDetailedRouteDescription:]"
+ "-[MXCoreSession willRouteToOnDemandVADOnActivation]"
+ "-[MXMediaEndowmentManager dumpDebugInfo]"
+ "-[MXMediaEndowmentManager dumpDebugInfo]_block_invoke"
+ "-[MXMediaEndowmentManager getRecordingAttributions:]"
+ "-[MXMediaEndowmentManager grantMediaEndowment:environmentID:endowmentPayload:]"
+ "-[MXMediaEndowmentManager grantMediaEndowment:environmentID:endowmentPayload:]_block_invoke"
+ "-[MXMediaEndowmentManager loadMediaEndowments]"
+ "-[MXMediaEndowmentManager processStateUpdateHandler:process:update:]"
+ "-[MXMediaEndowmentManager refreshAssertions]"
+ "-[MXMediaEndowmentManager refreshDomainAssertions:currentlyActivePIDs:]"
+ "-[MXMediaEndowmentManager refreshEndowmentTrees]"
+ "-[MXMediaEndowmentManager refreshEndowmentTrees]_block_invoke"
+ "-[MXMediaEndowmentManager revokeMediaEndowment:environmentID:]"
+ "-[MXMediaEndowmentManager revokeMediaEndowment:environmentID:]_block_invoke"
+ "-[MXSessionManager copyActiveSessionsInfoForAdditiveRouting]"
+ "-[MXSessionManager(Utilities) canSessionsCoexistDueToIndependentRecording:victim:]"
+ "-[MXSessionManager(Utilities) interruptAllSessionsAndSystemSounds:]"
+ "21:19:17"
+ "@\"NSData\""
+ "@\"RBSProcessMonitor\""
+ "AttributedAuditToken"
+ "AudioPlayback_DataUpdate"
+ "AudioSessionInfoChanged"
+ "AvailableRouteControlFeatures"
+ "CMSMNotificationUtility_PostSessionRouteControlFeaturesDidChange"
+ "CMSMNotificationUtility_PostSessionRouteControlFeaturesDidChange_block_invoke"
+ "CMSMUtility_CopyRecordingClientsInfoForSystemStatus"
+ "CMSMUtility_CreateAudioQueueOptionsDictionary"
+ "CMSMVAUtility_WillSessionWithDescriptionRouteToOnDemandVADOnActivation"
+ "CMSM_IDSServer_StartAutomaticOwnershipTransferToPhoneTimer_block_invoke"
+ "CMSessionMgrCopyDisplayIdentifierToSession"
+ "CMSystemSoundMgr_StopSystemSoundsforPID"
+ "ClientAuditToken"
+ "ConstantOutputVolumeLeveldB"
+ "CoreSessionID"
+ "DefaultVAD"
+ "EchoCancellationVoice"
+ "EchoCancelledInput"
+ "EndowmentPayload"
+ "EnvironmentID"
+ "Exception thrown: %s, %s, %s:%d, %llu, %llu"
+ "Feb 16 2024"
+ "FigBufferedAirPlayGlobalRoutingRegistryStartServer"
+ "FigRouteDiscoveryManagerLowerBTDiscoveryModeFromDetailed_block_invoke_2"
+ "FigRoutingMangerCreateBluetoothEndpointManager"
+ "HasEchoCancelledInput"
+ "IndependentRoute"
+ "IndependentVolume"
+ "MXAdditiveRoutingManager"
+ "MXMediaEndowmentManager"
+ "MXSessionManagerBase"
+ "MX_FeatureFlags_IsStartupSequenceChangeEnabled_block_invoke"
+ "MX_MediaEndowmentManager.m"
+ "PreferredRouteControlFeatures"
+ "PrefersEchoCancelledInput"
+ "RBSProcessEverythingPredicate"
+ "RouteControlFeatures"
+ "RouteControlFeaturesDidChange"
+ "SpeechDetectionVAD"
+ "T@\"NSArray\",&,V_mostRecentActiveSessions"
+ "T@\"NSData\",&,V_auditToken"
+ "T@\"NSDictionary\",&,V_preferredRouteControlFeatures"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSSet\",&,N,V_notificationsSubscribedTo"
+ "T@\"NSString\",&,V_bundleID"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_prefersEchoCancelledInput"
+ "Tf,N,V_constantOutputVolumeLeveldB"
+ "This is an abstract method and should be overriden! Please file a radar against 'MediaExperience Session | All'"
+ "WirelessLatencyChanged"
+ "_beginInterruptionWithSecTask:andFlags:"
+ "_bundleID"
+ "_constantOutputVolumeLeveldB"
+ "_endInterruptionWithSecTask:andStatus:"
+ "_mostRecentActiveSessions"
+ "_preferredRouteControlFeatures"
+ "_prefersEchoCancelledInput"
+ "additiveRoutingInfo"
+ "bundleID"
+ "can"
+ "canSessionsCoexistDueToIndependentRecording:victim:"
+ "cannot"
+ "childrenLinks:"
+ "com.apple.mediaexperience.MediaEndowmentManager"
+ "com.apple.mediaexperience.session-Media"
+ "constantOutputVolumeLeveldB"
+ "constantOutputVolumeLeveldB ="
+ "copyActiveSessionsInfo"
+ "copyActiveSessionsInfoForAdditiveRouting"
+ "copyActiveVoiceOverSessionPlayingToOnDemandVAD"
+ "copyAndUpdateSessionInformation:"
+ "copySessionWithAudioSessionID:"
+ "dateWithTimeIntervalSinceNow:"
+ "discoveryManager_updateDiscoveryModeForType_block_invoke"
+ "does not have"
+ "dumpDebugInfo"
+ "endowmentTreeForNamespace:"
+ "everythingPredicate"
+ "figEndpointUIAgent_showError"
+ "getRecordingAttributions:"
+ "getSetPropertiesOrder"
+ "grantMediaEndowment:environmentID:endowmentPayload:"
+ "grantMediaEndowmentWithEnvironmentID:endowmentPayload:"
+ "grantWithNamespace:endowment:"
+ "handleEndowmentTreeUpdate"
+ "has"
+ "i28@0:8i16@20"
+ "i36@0:8i16@20@28"
+ "initWithSet:"
+ "interruptAllSessionsAndSystemSounds:"
+ "isAirPlaySession:"
+ "isRoutedToOnDemandVAD"
+ "isSessionUsingBuiltInMic:"
+ "isSiriSessionActiveAndRoutedToSiriOutputVAD"
+ "iterateEndowmentTree:rootPID:environment:endowmentLinks:"
+ "loadMediaEndowments"
+ "mEndowmentPayloads"
+ "mEndowmentTrees"
+ "mEndowments"
+ "mMediaPlaybackAssertions"
+ "mProcessMonitor"
+ "mSerialQueue"
+ "mediaEndowments"
+ "mostRecentActiveSessions"
+ "mx_runningBoardServices_addPIDToApplicationStateCache"
+ "mx_runningBoardServices_getApplicationStateFromCache"
+ "mx_runningBoardServices_removePIDFromApplicationStateCache"
+ "mx_runningBoardServices_setApplicationStateToCache"
+ "numberFromString:"
+ "prefer independent route"
+ "preferredRouteControlFeatures"
+ "preferredRouteControlFeatures ="
+ "prefersEchoCancelledInput"
+ "prefersEchoCancelledInput ="
+ "previousState"
+ "processStateUpdateHandler:process:update:"
+ "refreshAssertions"
+ "refreshDomainAssertions:currentlyActivePIDs:"
+ "refreshEndowmentTrees"
+ "remoteSystemController_createMediaEndowment"
+ "remoteSystemController_invalidateMediaEndowment"
+ "revokeMediaEndowment:environmentID:"
+ "revokeMediaEndowmentWithEnvironmentID:"
+ "rootLinks"
+ "sendActiveSessionsInfoToVA"
+ "sessionUtilizesIndependentRecordingOnly:"
+ "setBundleID:"
+ "setConstantOutputVolumeLeveldB:"
+ "setMostRecentActiveSessions:"
+ "setNumberStyle:"
+ "setPreferredRouteControlFeatures:"
+ "setPrefersEchoCancelledInput:"
+ "share route"
+ "startup_sequence_change"
+ "storeMediaEndowments"
+ "subscribeToNotifications:"
+ "targetEnvironment"
+ "targetPid"
+ "targetWithPid:environmentIdentifier:"
+ "vaemGetVirtualAudioPlugin"
+ "vaemWaitUntilVAIsFullyInitialized"
+ "waitUntilDate:"
+ "willRouteToOnDemandVADOnActivation"
+ "{originator:\"com.apple.mediaexperience\", bundleID:\"%@\" clientPID:%d, environmentID:\"%@\"}"
+ "{originator:\"com.apple.mediaexperience\", clientPID:%@ DomainName:%@}"
- "%{public}s %{public}s:%i Invalidating assertion %p for reason %u as its explanation %{public}@ contains matching session id %{public}@ and it is unaccounted for"
- "%{public}s %{public}s:%i Invalidating un-accounted assertions if needed for session id 0x%x(%u) client %{public}@ for reason %{public}@"
- "%{public}s %{public}s:%i Skipping invalidating assertion %{public}@ as assertionExplanationContainsSessionId = %{BOOL}u accountedAssertionSetContainsAssertion = %{BOOL}u"
- "%{public}s %{public}s:%i Starting session assertion audit timer for client %{public}@"
- "%{public}s %{public}s:%i Stopping assertion audit timer for client %{public}@"
- "%{public}s %{public}s:%i Stopping assertion audit timer for client %{public}@ as active state is changing"
- "%{public}s %{public}s:%i Stopping assertion audit timer for client '%{public}@'"
- "-CMSUtilities- %s: Error getting kVirtualAudioPlugInPropertyOnDemandRouteSupported for session %{public}@ [%p] going active %{public}@: %d"
- "-CMSUtilities- %s: Failed to retrieve session info for session going active %{public}@ [%p]."
- "-CMSUtilities- %s: NULL session!"
- "-CMSUtilities- %s: Returning consolidatedSourceFormatInfo: %{public}@ for MXCoreSession %{public}@"
- "-CMSUtilities- %s: Sending session going active info to VA: %{public}@ to query on-demand route capability."
- "-CMSUtilities- %s: Will session %{public}@ [%p] going active route to on-demand VAD? %{BOOL}u"
- "-CMSessionMgr- %s: %{public}@ start and stop play time for client session %{public}@ current active state %{BOOL}u new active state %{BOOL}u"
- "-CMSessionMgr- %s: Client %{public}@, returning AudioQueueOptions : %{public}@"
- "-CMSessionMgr- %s: Session '%{public}@' is subscribing for the following notifications: '%{public}@'"
- "-CMSessionMgr- %s: Session '%{public}@' isRecordingMuted updated to '%d'"
- "-CMSessionMgr- %s: Session '%{public}@' setting InterruptionStyle to %{public}s"
- "-CMSessionMgr- %s: Session '%{public}@' setting doesntActuallyPlayAudio value to '%d'"
- "-CMSessionMgr- %s: SoundRecognition session %{public}@ [%p] will play to on-demand VAD, resetting flags to 0 since it should not control routing nor volume."
- "-CMSessionMgr- %s: SpeechDetectionVADID %{public}@, device sample rate = %{public}@"
- "-CMVAEndpoint- %s: Ownership semaphore was blocked for %0.3f ms"
- "-CMVAEndpoint- %s: vaeSetBTPortOwnsSharedAudioConnection returned an error=%d"
- "-CMVAEndpoint- %s: vaeWaitOnOwnershipSemaphore: Timeout occurred for port: %d for reason=%{public}@"
- "-CMVAEndptMgr- %s: Route changed. Reason %{public}.4s (%{public}@)."
- "-CMVAEndptMgr- %s: Setting route configuration %{public}@ for active sessions."
- "-CMVAEndptMgr- %s: vaemSetRouteConfigurationDictionaryOnVAD of SetActiveSessionInfoOnVA failed with %d / `%{public}.4s'\n"
- "-CMVAEndptUtl- %s: Failed to retrieve session info dictionary for %{public}@ [%p]."
- "-FigPredictedRouting- %s: Called due to reason=%{public}@, isBTManagedPortPresent=%{BOOL}u, isBTManagedPortInEar=%{BOOL}u, routeIsBuiltIn=%{BOOL}u, predictedRouteConditionChanged=%{BOOL}u, cachedSessionIsPlaying=%{BOOL}u, predictedRouteChanged=%{BOOL}u, predictedRouteName=%{public}@, predictedRouteUID=%{private}@"
- "-FigRoutingManager_SystemRemotePool- %s: Endpoint with name=%{public}@ is already in SystemRemotePool, notify client this is a no-op request"
- "-MXSession- %s: %{public}@ setting mutePriority to %{public}@"
- "-MXSessionManager- %s: Cache doesn't contain the requested detailed route description for virtualAudioDeviceID=%u"
- "-MXSessionManager- %s: Device info missing deviceID and deviceUID!"
- "-MXSessionManager- %s: Failed to update detailed route description for %{public}@"
- "-MXSessionManager- %s: NOTICE: Active session has lost an on-demand VAD, call BeginInterruption again (this should not happen in v1)."
- "-MXSessionManager- %s: Removing %{public}@ from detailed route descriptions."
- "-MXSessionManager- %s: Resetting default audio behaviour for session %{public}@ who's VADs went away."
- "-MXSessionManager- %s: Session not found for audio session ID %d"
- "-MXSessionManager- %s: Updating audio behaviour for %{public}@ with audioSessionID %d from %{public}@."
- "-MXSessionManager- %s: Updating detailed route description for %{public}@ with deviceID %{public}@"
- "-MXSessionManager- %s: Updating maps; IDToName = %{public}@ and NameToID = %{public}@"
- "-MXSessionManager- %s: Updating session %{public}@ to %{public}@ after VAD went away."
- "-MXSessionManagerUtilities-"
- "-MXSystemSounds- %s: Suppressing system sound because Wombat is enabled (and we are not playing pong sound)."
- "-MXSystemSounds- %s: Suppressing system sound because device is in AC3 mode and it is using Apple TV."
- "-MXSystemSounds- %s: Suppressing system sound because it's an Apple TV that's AirPlay-ing."
- "-MX_RunningBoardServices- %s: Returning host process pid %d for pid %d"
- "-MX_SystemStatus- %s: Creating ST attribution info object with ActiveEntity %{public}@, ActiveEntity executablePath: %{public}@, AttributedEntity bundleID: %{public}@ and if available recording websiteInfo: %{public}@ , pid: %d, hasEntitlementForWebsiteInfo: %{public}s"
- "-MX_SystemStatus- %s: HasEntitlementForWebsiteInfo: %{public}s, Creating ST attribution info object with ActiveEntity PID: %d"
- "-[MXSessionManager copyDetailedRouteDescription:]"
- "-[MXSessionManager copySessionInformationFromVARouteConfiguration:]"
- "-[MXSessionManager updateDetailedRouteDescription:]"
- "-[MXSessionManager(Utilities) cleanupSessionAssertionsIfNeeded:cleanupReason:]_block_invoke"
- "18:23:37"
- "@\"NSArray\"16@0:8"
- "CMSMVAUtility_CopyActiveSessionsInfoForAdditiveRouting"
- "CMSUtility_IsSessionRoutedToOnDemandVAD"
- "CMSUtility_WillSessionGoingActiveRouteToOnDemandVAD"
- "Dec 20 2023"
- "FigRoutingMangerCreateBluetoothEndpointManager_block_invoke"
- "HasEntitlementForWebsite"
- "Not resetting"
- "Resetting"
- "TB,N,V_hasEntitlementForWebsiteInfo"
- "_beginInterruptionWithSecTask:flags:"
- "_endInterruptionWithSecTask:interruptionStatus:"
- "_hasEntitlementForWebsiteInfo"
- "cmsCopyDisplayIdentifierToSession"
- "com.apple.private.mediaexperience.recordingWebsite.allow"
- "copySessionInformationFromVARouteConfiguration:"
- "copySetPropertiesOrder"
- "discoveryManager_updateDiscoveryModeForType"
- "hasEntitlementForWebsiteInfo"
- "hasEntitlementForWebsiteInfo ="
- "mx_runningBoardServices_getHostProcessIDForProcessID"
- "setHasEntitlementForWebsiteInfo:"
- "tvairplay"
- "updateActiveSessionInformation"
- "vaemSetActiveSessionsInfoRouteConfigurationDictionaryOnVAD"

```
