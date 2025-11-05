## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience`

```diff

-225.3.1.0.0
-  __TEXT.__text: 0x87f30
-  __TEXT.__auth_stubs: 0x12c0
-  __TEXT.__objc_methlist: 0x10b4
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0xe92a
-  __TEXT.__oslogstring: 0xb311
-  __TEXT.__gcc_except_tab: 0xac0
+230.17.1.0.0
+  __TEXT.__text: 0x80cdc
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x124c
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0xe7a2
+  __TEXT.__oslogstring: 0xaf58
+  __TEXT.__gcc_except_tab: 0xb5c
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x1560
-  __TEXT.__objc_classname: 0x20d
-  __TEXT.__objc_methname: 0x3945
-  __TEXT.__objc_methtype: 0xad2
-  __TEXT.__objc_stubs: 0x2760
+  __TEXT.__unwind_info: 0x1670
+  __TEXT.__objc_classname: 0x207
+  __TEXT.__objc_methname: 0x3666
+  __TEXT.__objc_methtype: 0xa0e
+  __TEXT.__objc_stubs: 0x25c0
   __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0x24b0
+  __DATA_CONST.__const: 0x24c8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc20
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x970
-  __AUTH_CONST.__const: 0x1f60
+  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__const: 0x1f40
   __AUTH_CONST.__cfstring: 0x92a0
-  __AUTH_CONST.__objc_const: 0x2288
+  __AUTH_CONST.__objc_const: 0x1d78
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x2b8
   __DATA.__common: 0x1c0
-  __DATA.__bss: 0x8f0
+  __DATA.__bss: 0x8d8
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE046AC8-F1BC-3CA5-B283-506BB729ECC2
-  Functions: 1672
-  Symbols:   4201
-  CStrings:  4226
+  UUID: EC47B2D8-DB7D-33E8-A9D0-B419D71420AF
+  Functions: 1900
+  Symbols:   4597
+  CStrings:  4173
 
Symbols:
+ +[MXDebugPlatform sharedInstance].cold.1
+ +[MXEndpointDescriptorCache sharedInstance].cold.1
+ +[MXHALInterface sharedInstance]
+ +[MXInitialization notifyMXIsFullyInitialized].cold.1
+ +[MXInitialization start].cold.1
+ +[MXNowPlayingServices sharedInstance].cold.1
+ +[MXRoutingContextCallbackHelper _sharedLock].cold.1
+ +[MXSessionManager sharedInstance].cold.1
+ -[FigRemoteRoutingContextFactory copySidePlayContextWithAllocator:options:context:].cold.1
+ -[FigRemoteRoutingContextFactory copySidePlayContextWithAllocator:options:context:].cold.2
+ -[FigRemoteRoutingContextFactory copySystemAudioContextWithAllocator:options:context:].cold.1
+ -[FigRemoteRoutingContextFactory copySystemAudioContextWithAllocator:options:context:].cold.2
+ -[FigRemoteRoutingContextFactory copySystemMirroringContextWithAllocator:options:context:].cold.1
+ -[FigRemoteRoutingContextFactory copySystemMirroringContextWithAllocator:options:context:].cold.2
+ -[FigRemoteRoutingContextFactory copySystemMusicContextWithAllocator:options:context:].cold.1
+ -[FigRemoteRoutingContextFactory copySystemMusicContextWithAllocator:options:context:].cold.2
+ -[FigRemoteRoutingContextFactory copySystemRemoteDisplayContextWithAllocator:options:context:].cold.1
+ -[FigRemoteRoutingContextFactory copySystemRemoteDisplayContextWithAllocator:options:context:].cold.2
+ -[MXHALInterface dealloc]
+ -[MXHALInterface initInternal]
+ -[MXNowPlayingServices isThisABrowser:].cold.1
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.1
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.10
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.11
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.12
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.13
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.14
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.15
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.16
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.2
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.3
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.4
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.5
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.6
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.7
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.8
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:].cold.9
+ -[MXSessionBase setOrderedPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:].cold.1
+ -[MXSessionBase setOrderedPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:].cold.2
+ -[MXSessionBase setPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:].cold.1
+ -[MXSessionBase setPropertiesInternal:usingErrorHandlingStrategy:outPropertiesErrors:].cold.2
+ -[MXSessionManager copyMXCoreSessionList]
+ -[MXSessionManager mxCoreSessionListLock]
+ -[MXSessionManager setMxCoreSessionListLock:]
+ -[MXSessionManager(InterruptionActionMapper) getSessionPriority:forTipi:].cold.1
+ -[MXSystemController initWithPID:].cold.1
+ CreateRoutingContextServerState.cold.1
+ DisposeRoutingContextServerState.cold.1
+ FigEndpointAuthRequestHandler_AddRequest.cold.1
+ FigEndpointAuthRequestHandler_CallbackFromUIAgent.cold.1
+ FigEndpointAuthRequestHandler_GetCurrentAuthToProcess.cold.1
+ FigEndpointAuthRequestHandler_HasEndpoint.cold.1
+ FigEndpointAuthRequestHandler_IsAuthListEmpty.cold.1
+ FigEndpointAuthRequestHandler_ProcessRequest.cold.1
+ FigEndpointAuthRequestHandler_RemoveRequest.cold.1
+ FigEndpointAuthRequestHandler_ReplaceRequest.cold.1
+ FigEndpointAuthRequestHandler_SetProcessNextRequest.cold.1
+ FigEndpointDescriptorUtility_CopyDescriptorsForEndpoints.cold.1
+ FigEndpointUIAgentGetClassID.cold.1
+ FigEndpointUIAgentGetTypeID.cold.1
+ FigEndpointUIAgentHelper_DisplayAuthPrompt.cold.1
+ FigEndpointUIAgentHelper_RegisterEventHandler.cold.1
+ FigEndpointUIAgentHelper_SetNewUIAgent.cold.1
+ FigEndpointUIAgentHelper_ShowError.cold.1
+ FigEndpointUIAgentStartServer.cold.1
+ FigRouteDiscovererGetClassID.cold.1
+ FigRouteDiscovererGetTypeID.cold.1
+ FigRouteDiscovererRemoteXPC_CopyProperty.cold.1
+ FigRouteDiscovererXPCRemoteCreate.cold.1
+ FigRouteDiscoveryManagerAddDiscoverer.cold.1
+ FigRouteDiscoveryManagerAddToCachedDiscoverers.cold.1
+ FigRouteDiscoveryManagerCopyCachedAudioSessionRouteInformation.cold.1
+ FigRouteDiscoveryManagerCopyRoutePresentForType.cold.1
+ FigRouteDiscoveryManagerCopyRoutesForTypeAndAudioSessionID.cold.1
+ FigRouteDiscoveryManagerGetDiscoveryQueue.cold.1
+ FigRouteDiscoveryManagerGetNotificationQueue.cold.1
+ FigRouteDiscoveryManagerGetSharedQueue.cold.1
+ FigRouteDiscoveryManagerInit.cold.1
+ FigRouteDiscoveryManagerLowerBTDiscoveryModeFromDetailed.cold.1
+ FigRouteDiscoveryManagerRegisterEndpointManager.cold.1
+ FigRouteDiscoveryManagerRegisterEndpointManager.cold.2
+ FigRouteDiscoveryManagerRemoveCachedDiscoverers.cold.1
+ FigRouteDiscoveryManagerRunBlockWhileEndpointManagerInfoLockIsLocked.cold.1
+ FigRouteDiscoveryManagerStart.cold.1
+ FigRouteDiscoveryManagerStart.cold.2
+ FigRouteDiscoveryManagerUpdateDiscoveryMode.cold.1
+ FigRoutingContextCreateSystemAudioContextInternal.cold.1
+ FigRoutingContextGetClassID.cold.1
+ FigRoutingContextGetTypeID.cold.1
+ FigRoutingContextRemoteCopyAllAudioContexts.cold.1
+ FigRoutingContextResilientRemoteCopyDefaultContext.cold.1
+ FigRoutingContextResilientRemoteCreate.cold.1
+ FigRoutingContextResilientRemoteCreate.cold.2
+ FigRoutingContextUtilities_CopyLeaderUUIDArrayForContext.cold.1
+ FigRoutingContextUtilities_CopyLeaderUUIDForContext.cold.1
+ FigRoutingContextUtilities_CreateStateInfoStringForContext.cold.1
+ FigRoutingContextUtilities_IsFollowingAnotherContext.cold.1
+ FigRoutingContextUtilities_RemoveLeaderUUIDFromContext.cold.1
+ FigRoutingContextUtilities_SetLeaderUUIDForContext.cold.1
+ FigRoutingManagerContextUtilities_AddActivatedEndpoint.cold.1
+ FigRoutingManagerContextUtilities_AddContext.cold.1
+ FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoint.cold.1
+ FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoints.cold.1
+ FigRoutingManagerContextUtilities_AddCurrentlyActivatingSubEndpoints.cold.1
+ FigRoutingManagerContextUtilities_AppendCurrentlyActivatingEndpointInfo.cold.1
+ FigRoutingManagerContextUtilities_CopyActivatedEndpointsInfo.cold.1
+ FigRoutingManagerContextUtilities_CopyAggregateEndpointAsFigEndpoint.cold.1
+ FigRoutingManagerContextUtilities_CopyAggregateEndpointAsFigEndpointAggregate.cold.1
+ FigRoutingManagerContextUtilities_CopyAllAudioContexts.cold.1
+ FigRoutingManagerContextUtilities_CopyAllRoutingContextUUIDs.cold.1
+ FigRoutingManagerContextUtilities_CopyArrayOfFollowerUUIDs.cold.1
+ FigRoutingManagerContextUtilities_CopyAudioContextUUIDs.cold.1
+ FigRoutingManagerContextUtilities_CopyCachedSelectedRouteDescriptors.cold.1
+ FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpointInfoAtIndex.cold.1
+ FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpoints.cold.1
+ FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpointsInfo.cold.1
+ FigRoutingManagerContextUtilities_CopyCurrentlyActivatingSubEndpoints.cold.1
+ FigRoutingManagerContextUtilities_CopyHijackID.cold.1
+ FigRoutingManagerContextUtilities_CopyHypotheticalPickedEndpointAfterRemoval.cold.1
+ FigRoutingManagerContextUtilities_CopyPickedContexts.cold.1
+ FigRoutingManagerContextUtilities_CopyPickedEndpointAtIndex.cold.1
+ FigRoutingManagerContextUtilities_CopyPickedEndpointForRemoteControl.cold.1
+ FigRoutingManagerContextUtilities_CopyPickedEndpoints.cold.1
+ FigRoutingManagerContextUtilities_CopyPickedIndividualEndpoints.cold.1
+ FigRoutingManagerContextUtilities_CopyRoutingContextForContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopyRoutingContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemAudioContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemAudioInputContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemMirroringContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemMusicContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemRemoteDisplayContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemRemotePoolContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopySystemRoutingContext.cold.1
+ FigRoutingManagerContextUtilities_CopySystemVideoDisplayMenuContextUUID.cold.1
+ FigRoutingManagerContextUtilities_CopyVideoContextUUIDs.cold.1
+ FigRoutingManagerContextUtilities_Create.cold.1
+ FigRoutingManagerContextUtilities_GetActivationSeedForEndpoint.cold.1
+ FigRoutingManagerContextUtilities_GetContextString.cold.1
+ FigRoutingManagerContextUtilities_GetContextType.cold.1
+ FigRoutingManagerContextUtilities_GetIndexOfCurrentlyActivatingEndpoint.cold.1
+ FigRoutingManagerContextUtilities_GetMainVolumeScaleFactorForEndpointID.cold.1
+ FigRoutingManagerContextUtilities_GetPickingState.cold.1
+ FigRoutingManagerContextUtilities_IsContextSystemMusicAndIndependent.cold.1
+ FigRoutingManagerContextUtilities_IsContextSystemRemoteDisplay.cold.1
+ FigRoutingManagerContextUtilities_IsContextValid.cold.1
+ FigRoutingManagerContextUtilities_PostNotificationToClientsOfContextWithUUIDAndItsFollowers.cold.1
+ FigRoutingManagerContextUtilities_PostSystemPickerVideoRouteChangedNotification.cold.1
+ FigRoutingManagerContextUtilities_RemoveActivatedEndpoint.cold.1
+ FigRoutingManagerContextUtilities_RemoveContext.cold.1
+ FigRoutingManagerContextUtilities_RemoveCurrentlyActivatingEndpointInfoAtIndex.cold.1
+ FigRoutingManagerContextUtilities_ResetCurrentlyActivatingEndpointInfo.cold.1
+ FigRoutingManagerContextUtilities_ResetCurrentlyActivatingSubEndpointsInfo.cold.1
+ FigRoutingManagerContextUtilities_SaveCommChannelUUID.cold.1
+ FigRoutingManagerContextUtilities_SetAggregateEndpoint.cold.1
+ FigRoutingManagerContextUtilities_SetMainVolumeScaleFactorForEndpointID.cold.1
+ FigRoutingManagerContextUtilities_SetPickedEndpointAsAnArray.cold.1
+ FigRoutingManagerContextUtilities_SetPickedEndpoints.cold.1
+ FigRoutingManagerContextUtilities_SetPickingState.cold.1
+ FigRoutingManagerContextUtilities_UpdateRouteDescriptorForGivenContext.cold.1
+ FigRoutingManagerCopyPickedEndpointsForRoutingContext.cold.1
+ FigRoutingManagerCopySelectedBufferedEndpoint.cold.1
+ FigRoutingManagerGetSharedManager.cold.1
+ FigRoutingManagerGetSharedQueue.cold.1
+ FigRoutingManagerInitMacOS.cold.1
+ FigRoutingManagerInitMacOS.cold.2
+ FigRoutingManagerRegisterAndCopyContext.cold.1
+ FigRoutingManager_CloseRelayCommChannels.cold.1
+ FigRoutingManager_GetDataTransmissionQueue.cold.1
+ FigSTSCreate.cold.1
+ FigSTSCreate.cold.2
+ FigSTSCreate.cold.3
+ FigSTSCreate.cold.4
+ FigSTSGetClassID.cold.1
+ FigSTSGetTypeID.cold.1
+ FigVolumeControllerCopySharedController.cold.1
+ FigVolumeControllerGetClassID.cold.1
+ FigVolumeControllerGetTypeID.cold.1
+ MXBluetoothServices_RegisterForAudioAccessoryServicesDeathNotification.cold.1
+ MXBluetoothServices_UpdateAppState.cold.1
+ MXGetAssertionLog.cold.1
+ MXGetNotificationSenderQueue.cold.1
+ MXGetPerformanceLog.cold.1
+ MXGetSerialQueue.cold.1
+ MXGetSessionLog.cold.1
+ MXInitialize.cold.1
+ MXIntegrationTestInitialize.cold.1
+ MXSessionBeginInterruption.cold.1
+ MXSessionCopyProperty.cold.1
+ MXSessionCopyProperty.cold.2
+ MXSessionCopyProperty.cold.3
+ MXSessionCreate.cold.1
+ MXSessionEndInterruption.cold.1
+ MXSessionSetProperty.cold.1
+ MXSessionSetProperty.cold.2
+ MXSystemAudio_macOSAppSpecificAudioEnabled.cold.1
+ MXSystemRemotePool_ActivateAggregateEndpoint.cold.1
+ MX_FeatureFlags_IsAVODDiscoveryEnhancementEnabled.cold.1
+ MX_FeatureFlags_IsAudioSessionOnMacEnabled.cold.1
+ MX_FeatureFlags_IsConversationDetectSupported.cold.1
+ MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.cold.1
+ MX_FeatureFlags_IsSystemRemoteDisplayContextEnabled.cold.1
+ MX_FeatureFlags_UseRouteDescriptors.cold.1
+ OBJC_IVAR_$_MXSessionManager._mxCoreSessionListLock
+ _OBJC_CLASS_$_MXHALInterface
+ _OBJC_METACLASS_$_MXHALInterface
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __FigRouteDiscoveryManagerActivityMonitorEnsureStarted_block_invoke.cold.1
+ __FigRouteDiscoveryManagerActivityMonitorEnsureStarted_block_invoke.cold.2
+ __FigRouteDiscoveryManagerActivityMonitorEnsureStarted_block_invoke.cold.3
+ __FigRouteDiscoveryManagerInit_block_invoke.cold.1
+ __FigRouteDiscoveryManagerRegisterEndpointManager_block_invoke.cold.1
+ __FigRouteDiscoveryManagerRegisterEndpointManager_block_invoke.cold.2
+ __FigRouteDiscoveryManagerRegisterEndpointManager_block_invoke.cold.3
+ __FigRouteDiscoveryManagerRegisterEndpointManager_block_invoke.cold.4
+ __FigRoutingContextRemoteCopyContextForUUID_block_invoke.cold.1
+ __FigRoutingManagerAggregateAddEndpointCompletionCallback_block_invoke.cold.1
+ __FigRoutingManagerAggregateAddEndpointCompletionCallback_block_invoke.cold.2
+ __MXBluetoothServices_RegisterForAudioAccessoryServicesDeathNotification_block_invoke.cold.1
+ __MXBluetoothServices_RequestForSharedRoute_block_invoke.cold.1
+ __MXInitialize_block_invoke.cold.1
+ __MXIntegrationTestInitialize_block_invoke.cold.1
+ __MXIntegrationTestInitialize_block_invoke.cold.2
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_MXHALInterface
+ __OBJC_$_INSTANCE_METHODS_MXHALInterface
+ __OBJC_CLASS_RO_$_MXHALInterface
+ __OBJC_METACLASS_RO_$_MXHALInterface
+ ___discoveryManager_updateDiscoveryModeForType_block_invoke_3
+ __routingContextRemoteXPC_EnsureClientEstablished_block_invoke.cold.1
+ __routingContextRemoteXPC_EnsureClientEstablished_block_invoke.cold.2
+ __routingContextRemoteXPC_EnsureClientEstablished_block_invoke.cold.3
+ __routingContextUtilities_getSharedContextUtilities_block_invoke.cold.1
+ _discoverer_getTypeString
+ _discoveryManager_mapDiscovererTypeToEndpointFeatures
+ _kFigEndpointDescriptorKey_BTDetails_AlternateTransport
+ _kMXSessionNotification_StravinskyServicesWereLost
+ _kMXSessionNotification_StravinskyServicesWereReset
+ _objc_msgSend$copyMXCoreSessionList
+ _routingContextUtilities_checkActivationTimeout.cold.1
+ _routingContextUtilities_copySystemRoutingContext.cold.1
+ _routingContextUtilities_notifyClientsOfChangeInPickedEndpoints.cold.1
+ _routingContextUtilities_postNotificationToContextAndItsFollowers.cold.1
+ _routingContextUtilities_postRouteConfigUpdatedToClientsOfContextWithUUIDAndItsFollowers.cold.1
+ _routingContextUtilities_removeCurrentlyActivatingEndpointWithID.cold.1
+ _routingContextUtilities_setLeaderUUIDForContext.cold.1
+ audioAccessoryServicesDiedCallback.cold.1
+ discoveryManager_notificationHandler.cold.1
+ discoveryManager_removeFreedWeakRefs.cold.1
+ endpointAggregate_Deactivate.cold.1
+ endpointAggregate_WithRemoteAggregateEndpoint.cold.1
+ endpointAggregate_WithRemoteAggregateEndpoint.cold.2
+ endpointUIAgentHelper_UIAgentPasswordCallback.cold.1
+ figRouteDiscoveryManager_stopTimerForActivityMonitoring.cold.1
+ figRouteDiscoveryManager_stopTimerForActivityMonitoring.cold.2
+ mxBluetoothServices_isBluetoothServicesLoaded.cold.1
+ mxSystemRemotePool_processAddEndpoint.cold.1
+ remoteXPCRouteDiscoverer_GetObjectID.cold.1
+ remoteXPCRoutingContext_CreateInternal.cold.1
+ remoteXPCRoutingContext_GetObjectID.cold.1
+ remoteXPCendpointAgent_GetObjectID.cold.1
+ remoteXPCendpointAgent_GetObjectID.cold.2
+ routingContextRemoteXPC_CloseCommChannelForDeviceID.cold.1
+ routingContextRemoteXPC_CloseCommChannelForDeviceID.cold.2
+ routingContextRemoteXPC_CopyProperty.cold.1
+ routingContextRemoteXPC_CreateCommChannelForDeviceID.cold.1
+ routingContextRemoteXPC_EnsureClientEstablished.cold.1
+ routingContextRemoteXPC_SendData.cold.1
+ routingContextRemoteXPC_SendDataForDeviceID.cold.1
+ routingContextRemoteXPC_SendDataForDeviceID.cold.2
+ routingContextRemoteXPC_SendDataForDeviceID.cold.3
+ routingContext_IsOperationOnSystemInputContextAllowedInternal.cold.1
+ routingContext_collectPickedEndpoints.cold.1
+ routingManager_pickingTimeoutCallback.cold.1
+ singletonVolumeController_copyCachedRemoteVolumeController.cold.1
+ singletonVolumeController_copyRemoteVolumeController.cold.1
+ volumeControllerRemote_getObjectID.cold.1
+ volumeControllerRemote_getObjectID.cold.2
- +[MXHALEndpointManager sharedInstance]
- -[MXHALEndpointManager copyDictionaryForDevice:enableTapStream:]
- -[MXHALEndpointManager copyName:]
- -[MXHALEndpointManager dealloc]
- -[MXHALEndpointManager getAudioDeviceForUID:]
- -[MXHALEndpointManager getBuiltInSpeakerDeviceID]
- -[MXHALEndpointManager getCurrentDataSourceID:channel:deviceID:]
- -[MXHALEndpointManager getNumberOfChannels:isUsingInput:]
- -[MXHALEndpointManager getNumberStreams:isUsingInput:]
- -[MXHALEndpointManager getPropertyDataSize:deviceID:qualifierDataSize:qualifierData:]
- -[MXHALEndpointManager hasDataSourceControl:channel:deviceID:]
- -[MXHALEndpointManager initInternal]
- -[MXHALEndpointManager isAlive:]
- -[MXSessionManager copyCoreSessionList]
- -[MXSessionManager mxCoreSessionListActiveReaders]
- -[MXSessionManager mxCoreSessionListReadLock]
- -[MXSessionManager mxCoreSessionListWriteSemaphore]
- -[MXSessionManager setMxCoreSessionListActiveReaders:]
- -[MXSessionManager setMxCoreSessionListReadLock:]
- -[MXSessionManager setMxCoreSessionListWriteSemaphore:]
- -[MXSessionManager(Common) mxCoreSessionListBeginIteration]
- -[MXSessionManager(Common) mxCoreSessionListEndIteration]
- FigEndpointUIAgentHelper_GetSharedHelper.endpointUIAgentHelperObj
- FigEndpointUIAgentHelper_GetSharedHelper.sFigEndpointUIAgentSetupOnce
- FigEndpointUIAgentRemoteXPC_EnsureClientEstablished.err
- FigEndpointUIAgentRemoteXPC_EnsureClientEstablished.onceToken
- FigRoutingManagerGetSharedManager.manager
- FigRoutingManagerGetSharedManager.sFigRoutingManagerStateSetupOnce
- FigSTSGetClassID.sFigSTSClassID
- FigSTSGetClassID.sRegisterFigSTSBaseTypeOnce
- FigVolumeControllerCopySharedControllerRemote.sInitSingletonOnce
- FigVolumeControllerGetClassID.sFigVolumeControllerClassID
- FigVolumeControllerGetClassID.sRegisterFigVolumeControllerBaseTypeOnce
- GCC_except_table13
- OBJC_IVAR_$_MXHALEndpointManager.mAOPDevicePresent
- OBJC_IVAR_$_MXHALEndpointManager.mHALServerDied
- OBJC_IVAR_$_MXSessionManager._mxCoreSessionListActiveReaders
- OBJC_IVAR_$_MXSessionManager._mxCoreSessionListReadLock
- OBJC_IVAR_$_MXSessionManager._mxCoreSessionListWriteSemaphore
- _AudioObjectHasProperty
- _MGGetBoolAnswer
- _OBJC_CLASS_$_MXHALEndpointManager
- _OBJC_METACLASS_$_MXHALEndpointManager
- __OBJC_$_CLASS_METHODS_MXHALEndpointManager
- __OBJC_$_INSTANCE_METHODS_MXHALEndpointManager
- __OBJC_$_INSTANCE_VARIABLES_MXHALEndpointManager
- __OBJC_CLASS_RO_$_MXHALEndpointManager
- __OBJC_METACLASS_RO_$_MXHALEndpointManager
- ___36-[MXHALEndpointManager initInternal]_block_invoke
- ___38+[MXHALEndpointManager sharedInstance]_block_invoke
- _gFigEndpointUIAgentRemoteClient
- _gSharedInstance
- _gSingletonVolumeController
- _objc_msgSend$copyCoreSessionList
- _objc_msgSend$copyName:
- _objc_msgSend$getCurrentDataSourceID:channel:deviceID:
- _objc_msgSend$getNumberOfChannels:isUsingInput:
- _objc_msgSend$getNumberStreams:isUsingInput:
- _objc_msgSend$getPropertyDataSize:deviceID:qualifierDataSize:qualifierData:
- _objc_msgSend$hasDataSourceControl:channel:deviceID:
- _objc_msgSend$initInternal
- _objc_msgSend$mxCoreSessionListActiveReaders
- _objc_msgSend$mxCoreSessionListBeginIteration
- _objc_msgSend$mxCoreSessionListEndIteration
- _objc_msgSend$mxCoreSessionListReadLock
- _objc_msgSend$mxCoreSessionListWriteSemaphore
- _objc_msgSend$setMxCoreSessionListActiveReaders:
- initInternal.onceToken
- volumeControllerRemote_ensureClientEstablished.err
- volumeControllerRemote_ensureClientEstablished.onceToken
CStrings:
+ "-FigRouteDiscoveryManager- %s: Error: %d. Trying to update discovery mode again for endpointManager: %{public}@"
+ "21:12:52"
+ "BTDetails_AlternateTransport"
+ "MXHALInterface"
+ "Mar  7 2025"
+ "StravinskyServicesWereLost"
+ "StravinskyServicesWereReset"
+ "T@\"NSLock\",&,N,V_mxCoreSessionListLock"
+ "_mxCoreSessionListLock"
+ "copyMXCoreSessionList"
+ "discoveryManager_updateDiscoveryModeForType_block_invoke_3"
+ "mxCoreSessionListLock"
+ "setMxCoreSessionListLock:"
- "-MXHALEndpointManager- %s: AudioObjectSetPropertyData failed for setting tapStreamEnabled %d"
- "-MXHALEndpointManager- %s: Channels In : %d Out : %d for device ID %{private}@(%d)"
- "-MXHALEndpointManager- %s: Device supports AOP = %{BOOL}u"
- "-MXHALEndpointManager- %s: Failed to copyAudioDevices, error = %d"
- "-MXHALEndpointManager- %s: Failed to get deviceUID, err = %d"
- "-MXHALEndpointManager- %s: Got an error %d getting the property data size"
- "-MXHALEndpointManager- %s: Got an error getting dataSource, err = %d"
- "-MXHALEndpointManager- %s: Got an error getting deviceUID, err = %d"
- "-MXHALEndpointManager- %s: Got an error getting the bufferList, err = %d"
- "-MXHALEndpointManager- %s: Got an error getting the deviceIsAlive, err = %d"
- "-MXHALEndpointManager- %s: Got an error getting the name, err = %d"
- "-MXHALEndpointManager- %s: Sub device dictionary %{public}@:"
- "-MXHALEndpointManager- %s: Tap Stream Enabled (%d) for device ID %{public}@(%d)"
- "-MXHALEndpointManager- %s: device ID : %d, dataSource : %c%c%c%c\n"
- "-MXHALEndpointManager- %s: no data source control for device ID : %d\n"
- "-[MXHALEndpointManager copyDictionaryForDevice:enableTapStream:]"
- "-[MXHALEndpointManager copyName:]"
- "-[MXHALEndpointManager getAudioDeviceForUID:]"
- "-[MXHALEndpointManager getBuiltInSpeakerDeviceID]"
- "-[MXHALEndpointManager getCurrentDataSourceID:channel:deviceID:]"
- "-[MXHALEndpointManager getNumberOfChannels:isUsingInput:]"
- "-[MXHALEndpointManager getPropertyDataSize:deviceID:qualifierDataSize:qualifierData:]"
- "-[MXHALEndpointManager initInternal]_block_invoke"
- "-[MXHALEndpointManager isAlive:]"
- "18:14:16"
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@20@0:8I16"
- "@24@0:8I16B20"
- "B20@0:8I16"
- "B28@0:8I16I20I24"
- "Dec 14 2024"
- "I24@0:8I16B20"
- "I24@0:8^{__CFString=}16"
- "I28@0:8I16I20I24"
- "I40@0:8^{AudioObjectPropertyAddress=III}16I24I28^v32"
- "MXHALEndpointManager"
- "T@\"NSLock\",&,N,V_mxCoreSessionListReadLock"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_mxCoreSessionListWriteSemaphore"
- "TI,N,V_mxCoreSessionListActiveReaders"
- "U+73bmG4kBGj6kpreQXUTQ"
- "_mxCoreSessionListActiveReaders"
- "_mxCoreSessionListReadLock"
- "_mxCoreSessionListWriteSemaphore"
- "channels-in"
- "channels-out"
- "copyCoreSessionList"
- "copyDictionaryForDevice:enableTapStream:"
- "copyName:"
- "getAudioDeviceForUID:"
- "getBuiltInSpeakerDeviceID"
- "getCurrentDataSourceID:channel:deviceID:"
- "getNumberOfChannels:isUsingInput:"
- "getNumberStreams:isUsingInput:"
- "getPropertyDataSize:deviceID:qualifierDataSize:qualifierData:"
- "hasDataSourceControl:channel:deviceID:"
- "isAlive:"
- "mAOPDevicePresent"
- "mHALServerDied"
- "mxCoreSessionListActiveReaders"
- "mxCoreSessionListBeginIteration"
- "mxCoreSessionListEndIteration"
- "mxCoreSessionListReadLock"
- "mxCoreSessionListWriteSemaphore"
- "setMxCoreSessionListActiveReaders:"
- "setMxCoreSessionListReadLock:"
- "setMxCoreSessionListWriteSemaphore:"

```
