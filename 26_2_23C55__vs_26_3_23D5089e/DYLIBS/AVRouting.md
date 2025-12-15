## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/AVRouting`

```diff

-305.6.1.1.0
-  __TEXT.__text: 0x52240
-  __TEXT.__auth_stubs: 0xb60
+315.2.1.0.0
+  __TEXT.__text: 0x6a50c
+  __TEXT.__auth_stubs: 0xb50
   __TEXT.__objc_methlist: 0x65b0
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__cstring: 0x9763
-  __TEXT.__oslogstring: 0x631a
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0x708
+  __TEXT.__cstring: 0xe1d8
+  __TEXT.__oslogstring: 0xbc30
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1818
+  __TEXT.__unwind_info: 0x18f8
   __TEXT.__objc_classname: 0x16d1
   __TEXT.__objc_methname: 0x95eb
   __TEXT.__objc_methtype: 0x2b9e
   __TEXT.__objc_stubs: 0x6840
   __DATA_CONST.__got: 0x1078
-  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__const: 0x11b8
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1fd0
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x410
-  __AUTH_CONST.__cfstring: 0x3fc0
+  __AUTH_CONST.__cfstring: 0x3fe0
   __AUTH_CONST.__objc_const: 0xbb60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x19a0
   __DATA.__objc_ivar: 0x53c
   __DATA.__data: 0xbd0
   __DATA.__bss: 0xd8
-  __DATA.__common: 0xc0
+  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xa0
-  __DATA_DIRTY.__common: 0xe0
+  __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0B92F145-94B6-35F9-878E-8D00BC090D43
-  Functions: 2182
-  Symbols:   7651
-  CStrings:  3516
+  UUID: 86390E05-39AA-3E20-91A6-4002AC441022
+  Functions: 2216
+  Symbols:   7745
+  CStrings:  4029
 
Symbols:
+ -[AVFigRoutingContextInputContextImpl setInputGain:error:].cold.2
+ GCC_except_table141
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table95
+ _FigSignalErrorAt3
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___91-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]_block_invoke.26
+ ___Block_byref_object_copy_.15
+ ___Block_byref_object_dispose_.16
+ ___block_descriptor_60_e8_32o40o48o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.143
+ ___block_literal_global.163
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.418
+ ___block_literal_global.576
+ _gAVPlatformUtilitiesTrace
+ _gAVRoutingCallbackContextRegistryTrace
+ _gAVRoutingOperationTrace
+ _gAVRoutingScheduledAudioParameters
+ _gScheduledParameterRampTrace
+ _stringWithValidatedFormatString
- GCC_except_table140
- GCC_except_table161
- GCC_except_table163
- GCC_except_table171
- GCC_except_table177
- GCC_except_table182
- GCC_except_table184
- GCC_except_table45
- GCC_except_table94
- GCC_except_table96
- _FigSignalErrorAtGM
- ___91-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]_block_invoke_2
- ___Block_byref_object_copy_.11
- ___Block_byref_object_dispose_.12
- ___block_descriptor_52_e8_32o40o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8
- ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
- ___block_literal_global.137
- ___block_literal_global.160
- ___block_literal_global.370
- ___block_literal_global.373
- ___block_literal_global.412
- ___block_literal_global.573
- _objc_release_x28
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "+[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]"
+ "+[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]"
+ "+[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]"
+ "+[AVInputContext defaultInputContextImplClass]"
+ "+[AVOutputContext defaultOutputContextImplClass]"
+ "+[AVOutputContext(AVAudioSession) preferredOutputDevicesForAudioSession:]"
+ "+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:]"
+ "+[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors]"
+ "+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2"
+ "+[AVRoutingOperation(ArrayOfOperations) statusOfOperations:error:]"
+ "+[AVRoutingSessionManager longFormVideoRoutingSessionManager]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]_block_invoke"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:]"
+ "-[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl connectedPairedDevices]"
+ "-[AVFigEndpointOutputDeviceImpl deviceSubType]"
+ "-[AVFigEndpointOutputDeviceImpl deviceType]"
+ "-[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]"
+ "-[AVFigEndpointOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigEndpointOutputDeviceImpl isInEar]"
+ "-[AVFigEndpointOutputDeviceImpl isInUseByPairedDevice]"
+ "-[AVFigEndpointOutputDeviceImpl supportsDataOverACLProtocol]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _finishedWithPrompt]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]"
+ "-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorInputDeviceImpl initWithRouteDescriptor:routeDiscoverer:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
+ "-[AVFigRouteDescriptorInputDeviceImpl isAppleAccessory]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _endpointDescriptorChanged]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _routePresentChanged]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl audioSessionId]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl availableInputDevices]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl devicePresenceDetected]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl fallbackInputDevice]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl setAudioSessionId:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _endpointDescriptorChanged]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _routePresentChanged]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setTargetAudioSession:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl targetAudioSession]"
+ "-[AVFigRoutingContextInputContextImpl _canSetMainVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextInputContextImpl _createSelectRouteOptionsForSetInputDeviceOptions:]"
+ "-[AVFigRoutingContextInputContextImpl _currentRouteChanged]"
+ "-[AVFigRoutingContextInputContextImpl _mainVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextInputContextImpl _routeChangeEndedWithID:reason:]"
+ "-[AVFigRoutingContextInputContextImpl _routeChangeStartedWithID:]"
+ "-[AVFigRoutingContextInputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]"
+ "-[AVFigRoutingContextInputContextImpl _serverConnectionDied]"
+ "-[AVFigRoutingContextInputContextImpl canSetInputGain]"
+ "-[AVFigRoutingContextInputContextImpl clearUserPreferredInputDevice:error:]"
+ "-[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]"
+ "-[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]_block_invoke"
+ "-[AVFigRoutingContextInputContextImpl inputDevice]"
+ "-[AVFigRoutingContextInputContextImpl inputGain]"
+ "-[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]_block_invoke"
+ "-[AVFigRoutingContextInputContextImpl setInputGain:error:]"
+ "-[AVFigRoutingContextInputContextImpl userPreferredInputDevice:]"
+ "-[AVFigRoutingContextOutputContextCompletionContext dealloc]"
+ "-[AVFigRoutingContextOutputContextCompletionContext initWithCompletionHandler:outputDevices:figRoutingContext:]"
+ "-[AVFigRoutingContextOutputContextImpl _canMuteDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _canSetMasterVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _canUseForRoutingContextDidChangeForRoutingContextWIthID:]"
+ "-[AVFigRoutingContextOutputContextImpl _createSelectRouteOptionsForSetOutputDeviceOptions:]"
+ "-[AVFigRoutingContextOutputContextImpl _currentRouteChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _groupConfigurationChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _masterVolumeControlTypeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _masterVolumeDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _muteDidChangeForRoutingContextWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _remoteControlChannelAvailabilityChanged]"
+ "-[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:]"
+ "-[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:]"
+ "-[AVFigRoutingContextOutputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]"
+ "-[AVFigRoutingContextOutputContextImpl _serverConnectionDied]"
+ "-[AVFigRoutingContextOutputContextImpl _systemPickerVideoRouteChanged]"
+ "-[AVFigRoutingContextOutputContextImpl addOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl associatedAudioDeviceID]"
+ "-[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:]"
+ "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]"
+ "-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]_block_invoke"
+ "-[AVFigRoutingContextOutputContextImpl outputDevice]"
+ "-[AVFigRoutingContextOutputContextImpl removeOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:]"
+ "-[AVInputContext ID]"
+ "-[AVInputContext encodeWithCoder:]"
+ "-[AVInputContext initWithCoder:]"
+ "-[AVInputContext initWithInputContextImpl:]"
+ "-[AVInputContext inputContextImpl:didExpireWithReplacement:]"
+ "-[AVInputContext inputDevice]"
+ "-[AVInputContextDestinationChange _setStatus:]"
+ "-[AVInputDevice initWithInputDeviceImpl:]"
+ "-[AVInputDeviceDiscoverySession devicePresenceDetected]"
+ "-[AVInputDeviceDiscoverySession initWithDeviceFeatures:]"
+ "-[AVInputDeviceDiscoverySession initWithInputDeviceDiscoverySessionImpl:]"
+ "-[AVInputDeviceDiscoverySession inputDeviceDiscoverySessionImplDidChangeAvailableInputDevices:]"
+ "-[AVOutputContext ID]"
+ "-[AVOutputContext encodeWithCoder:]"
+ "-[AVOutputContext initWithCoder:]"
+ "-[AVOutputContext initWithOutputContextImpl:]"
+ "-[AVOutputContext outputContextImpl:didExpireWithReplacement:]"
+ "-[AVOutputContext outputDevice]"
+ "-[AVOutputContext outputDevices]"
+ "-[AVOutputContext predictedOutputDevice]"
+ "-[AVOutputContextDestinationChange _setStatus:cancellationReason:]"
+ "-[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:]"
+ "-[AVOutputDevice openCommunicationChannelWithOptions:completionHandler:]"
+ "-[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:]"
+ "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]"
+ "-[AVOutputDeviceAuthorizationSession setDelegate:]"
+ "-[AVOutputDeviceDiscoverySession availableOutputDevices]"
+ "-[AVOutputDeviceDiscoverySession devicePresenceDetected]"
+ "-[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:]"
+ "-[AVOutputDeviceDiscoverySession setTargetAudioSession:]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices recentlyUsedDevices]"
+ "-[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:]"
+ "-[AVOutputDeviceGroup outputDevices]"
+ "-[AVOutputDeviceHID initWithUUID:screenUUID:endpoint:]"
+ "-[AVOutputDeviceIcon initWithDict:]"
+ "-[AVOutputDeviceScreenBorrowToken initWithEndpoint:client:reason:]"
+ "-[AVOutputDeviceScreenInfo initWithDict:]"
+ "-[AVOutputDeviceTurnByTurnToken dealloc]"
+ "-[AVOutputDeviceTurnByTurnToken initWithEndpoint:]"
+ "-[AVOutputDeviceViewAreaInfo initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:]"
+ "-[AVRoutingBlockOperation cancel]"
+ "-[AVRoutingBlockOperation start]"
+ "-[AVRoutingCallbackContextRegistry registerCallbackContextObject:]_block_invoke"
+ "-[AVRoutingCallbackContextRegistry unregisterCallbackContextForToken:]_block_invoke"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification addPeerToHomeGroup:]"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:]"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:]"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:]"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:]"
+ "-[AVRoutingContextCommandOutputDeviceConfigurationModification stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup]"
+ "-[AVRoutingContextRouteChangeOperation _routeChangeComplete]"
+ "-[AVRoutingContextRouteChangeOperation _routeChangeStartedWithID:]"
+ "-[AVRoutingContextRouteChangeOperation _routeChangeStartedWithID:]_block_invoke"
+ "-[AVRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]"
+ "-[AVRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]_block_invoke"
+ "-[AVRoutingContextRouteChangeOperation start]"
+ "-[AVRoutingOperation _setStatus:error:resultingStatus:failureReason:]_block_invoke"
+ "-[AVRoutingOperation didEnterTerminalState]"
+ "-[AVRoutingOperation evaluateDependenciesAndMarkAsExecuting]"
+ "-[AVRoutingOperation markAsCancelled]"
+ "-[AVRoutingOperation markAsCompleted]"
+ "-[AVRoutingOperation markAsFailedWithError:]"
+ "-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]"
+ "-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]_block_invoke"
+ "-[AVRoutingPlaybackArbiter _updatePreferredParticipantForExternalPlaybackFrom:toParticipant:checkingAllParticipants:]"
+ "-[AVRoutingPlaybackArbiter _updatePreferredParticipantForNonMixableAudioRouteFrom:toParticipant:checkingAllParticipants:]"
+ "-[AVRoutingPlaybackArbiter(AVRoutingPlaybackParticipantRegistration) deregisterParticipant:]"
+ "-[AVRoutingPlaybackArbiter(AVRoutingPlaybackParticipantRegistration) registerParticipant:]"
+ "-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _routeConfigUpdateWithID:endedWithReason:]"
+ "-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation start]"
+ "-[AVRoutingScheduledAudioParameters initWithPropertyList:]"
+ "-[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _setRamp:]"
+ "-[AVRoutingScheduledFloatValueRamp _interpolatedValueAtTime:]"
+ "-[AVRoutingSession dealloc]"
+ "-[AVRoutingSession destination]"
+ "-[AVRoutingSession establishedAutomaticallyFromLikelyDestination]"
+ "-[AVRoutingSession initWithFigRoutingSession:]"
+ "-[AVRoutingSessionDestination dealloc]"
+ "-[AVRoutingSessionDestination initWithFigRoutingSessionDestination:]"
+ "-[AVRoutingSessionDestination outputDeviceDescriptions]"
+ "-[AVRoutingSessionDestination probability]"
+ "-[AVRoutingSessionDestination providesExternalVideoPlayback]"
+ "-[AVRoutingSessionManager allLikelyDestinations]"
+ "-[AVRoutingSessionManager currentRoutingSession]"
+ "-[AVRoutingSessionManager dealloc]"
+ "-[AVRoutingSessionManager initWithFigRoutingSessionManager:]"
+ "-[AVRoutingSessionManager likelyExternalDestinations]"
+ "-[AVRoutingSessionManager prefersLikelyDestinationsOverCurrentRoutingSession]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]_block_invoke"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:]"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Assuming route change with ID %@ corresponds to the route change we just initiated"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (notificationName=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVRoutingErrorIncorrectPassword, since we do not know whether it was a PIN or password"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVRoutingErrorUnknown, since we have no more detailed error information"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using value %d for %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (routingContext=%@, configuratorBlock=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, deviceName=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, password=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peer=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, peerID=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (self=%p, rejectOtherConnections=%d)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because it does not match the expected ID %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeEnded for ID %@ because we have not yet executed the route change operation"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we already received a route change started notification"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring kFigRoutingContextNotification_RouteChangeStarted for ID %@ because we have not yet executed the route change operation"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring non-terminal route config update reason %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: ignoring route change ID %@ because it does not match the expected ID %@"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopyPredictedSelectedRouteDescriptorWithOptions yielded %@ (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptor yielded %@ (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextResetPredictedSelectedRouteDescriptorWithOptions yielded (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigVolumeControllerCanSetMainVolume yielded (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigVolumeControllerGetMainVolumeOfRoutingContext yielded (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigVolumeControllerSetMasterVolumeOfRoutingContext yielded (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, inputDevice=%@, options=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, bundleID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, contextUUID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, inputDevice=%@, options=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeUpdateID=%@, reason=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContext=%@, routingContextCreator=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContextID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_ContextUUID = %@ (err=%d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: operation finished"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: returning %@ (self=%p)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: using clientPID %d"
+ "<<<< AVInputContext >>>> %s: Defaulting to AVInputContext impl %@"
+ "<<<< AVInputContext >>>> %s: called (self=%p)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, impl=%@, replacementImpl=%@)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, status=%d)"
+ "<<<< AVInputContext >>>> %s: contextID = %@"
+ "<<<< AVInputContext >>>> %s: inputDevice = %@"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: AVInputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: Listener should be the input device route discoverer queue"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: called (self=%p)"
+ "<<<< AVInputDevice >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting kFigRouteDiscovererProperty_AudioSessionID to %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AudioSessionID = %@ (err=%d)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Posting %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Returning %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Unsupported device feature combination %d"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying all audio contexts not supported!"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Copying system remote display context not supported!"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for endpoint %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Failed to create AVOutputDevice for route descriptor %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopyPredictedSelectedRouteDescriptor yielded %@ (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded %@NULL endpoint (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoute yielded endpoint %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptor yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptors yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRoutes yielded %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Listener should be the shared endpoint agent queue"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: No comm channel found for ID %@, synthesizing one for the delegate (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Output context exists with associated remote output device"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Storing new outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Trying comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using pre-existing outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (modificationResult=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevice=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevices=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, agent=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, commChannelUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, contextUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, data=%@, commChannelUUID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevice=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, outputDevices=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routeUpdateID=%@, reason=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContext=%@, routingContextCreator=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContextID=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_AssociatedAudioDevice = %@ (err: %d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_ContextUUID = %@ (err=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: operation finished"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: returning %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: using clientPID %d"
+ "<<<< AVOutputContext >>>> %s: Defaulting to AVOutputContext impl %@"
+ "<<<< AVOutputContext >>>> %s: Received notification %@"
+ "<<<< AVOutputContext >>>> %s: called (self=%p)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, channel=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, data=%@, channel=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, impl=%@, replacementImpl=%@)"
+ "<<<< AVOutputContext >>>> %s: called (self=%p, status=%d)"
+ "<<<< AVOutputContext >>>> %s: contextID = %@"
+ "<<<< AVOutputContext >>>> %s: outputDevice = %@"
+ "<<<< AVOutputContext >>>> %s: outputDevices = %@"
+ "<<<< AVOutputContext >>>> %s: predictedOutputDevice = %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerGetMuteOfEndpointWithID (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' has value: %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' not supported"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: RouteUID %@ or RouteName %@ is nil, can't construct description."
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized head-tracked spatial audio mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  Only a subset of possible device types can be communicated by FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover connected paired devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover detailed device subtype for most devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get DataOverACL information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get isInEar information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, figEndpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p client %@ reason %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Listener should be the output device route discoverer queue"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Using value %d for %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, routeDescriptor=%@)"
+ "<<<< AVOutputDevice >>>> %s: No Output Context to add to!"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, request=%@, requestImpl=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, status=%d, error=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, uniqueID=%@, routeDescriptor=%@, pinMode=%d, reason=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Received notification %@"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p, delegate=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: self=%p, impl=%@, replacementImpl=%@"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: Unrecognized event type: %@"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No AVOutputDevice to connect to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No System Remote Pool to add to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No comm channel found for ID %@ for device %@, synthesizing one for the delegate."
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Removing comm channel UUID %@ for device with ID %@"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: initialized (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@ (err: %d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting kFigRouteDiscovererProperty_AudioSessionID to %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Unsupported device feature combination %d"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@), (timeTaken: %llu ms)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%@, class=%@, deviceFeatures=%u)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AudioSessionID = %@ (err=%d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AvailableRoutes = %@ (err=%d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Available output devices: %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Posting %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (targetAudioSession=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: otherDevices = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: recentlyUsedDevices = %@"
+ "<<<< AVOutputDeviceGroup >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceGroup >>>> %s: outputDevices = %@"
+ "<<<< AVOutputDeviceHID >>>> %s: called (uuid=%@, screenUUID=%@ endpoint=%p)"
+ "<<<< AVOutputDeviceIcon >>>> %s: called (dict=%@)"
+ "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (dict=%@)"
+ "<<<< AVOutputDeviceViewAreaInfo >>>> %s: called (viewArea=%@, transitionControl=%{BOOL}u, supportsFocusTransfer=%{BOOL}u, statusBarEdge=%@, safeArea=%@)"
+ "<<<< AVRoutingCallbackContextRegistry >>>> %s: registering observer %p (token %p), new observer count %d (self=%p)"
+ "<<<< AVRoutingCallbackContextRegistry >>>> %s: unregistering callback context token %p, new observer count %d (self=%p)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized description for %@ %ld (%@)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized description for %@ %ld (%@) (%@)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized failure reason for %@ %ld (%@)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized failure reason for %@ %ld (%@) (%@)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized recovery suggestion for %@ %ld (%@)"
+ "<<<< AVRoutingError >>>> %s: Could not load localized recovery suggestion or failure reason for %@ %ld (%@)"
+ "<<<< AVRoutingError >>>> %s: Invalid format string '%@', error %@, %@ %ld (%@)"
+ "<<<< AVRoutingOperation >>>> %s: Client block cancelled with status %d (self=%p)"
+ "<<<< AVRoutingOperation >>>> %s: Got unrecognized status %d"
+ "<<<< AVRoutingOperation >>>> %s: Ignoring attempt to cancel before execution has begun.  The expectation is that the implementation will notice the cancelled state as part of normal execution"
+ "<<<< AVRoutingOperation >>>> %s: advancing status from %d to %d (self=%p)"
+ "<<<< AVRoutingOperation >>>> %s: already cancelled (self=%p)"
+ "<<<< AVRoutingOperation >>>> %s: called (self=%@)"
+ "<<<< AVRoutingOperation >>>> %s: called (self=%@, error=%@)"
+ "<<<< AVRoutingOperation >>>> %s: called (self=%p)"
+ "<<<< AVRoutingOperation >>>> %s: called (self=%p, name=%@)"
+ "<<<< AVRoutingOperation >>>> %s: ignoring attempt to move from terminal status %d to status %d"
+ "<<<< AVRoutingOperation >>>> %s: marking as cancelled due to cancellation of dependency (self=%@)"
+ "<<<< AVRoutingOperation >>>> %s: marking as failed due to previous failure in dependency (self=%@)"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: clearing current external playback status notification listener. adding listener to participant %@"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: defer setting external playback priority"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: deregistering participant %@"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: received AVRoutingPlaybackParticipantExternalPlaybackStatusDidChangeNotification"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: registering participant %@"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: reset external playback priority to default for all participants"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: reset nonmixable audio priority to default for all participants"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: setting external playback priority on participant %@"
+ "<<<< AVRoutingPlaybackArbiter >>>> %s: setting preferred participant from %@ to %@"
+ "<<<< AVRoutingScheduledAudioParameters >>>> %s: not a valid scheduled ramp class"
+ "<<<< AVRoutingScheduledParameterRamp >>>> %s: Unknown ramp mode: %d"
+ "<<<< AVRoutingSessionManager >>>> %s: All likely external destinations %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: External destination confidence %f below threshold %f, clearing array (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: Fetched %d from %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: Returning %@"
+ "<<<< AVRoutingSessionManager >>>> %s: Sum of external destination confidence: %f (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: called"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSession=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionDestination=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionManager=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (err: %d)"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from FigRoutingSession (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: kFigRoutingSessionProperty_EstablishedAutomaticallyFromLikelyDestination = %@"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %d"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %d (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %f (self=%p)"
+ "AVDefaultRoutingContextFactory"
+ "AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigRouteDescriptorInputDeviceImpl.m"
+ "AVFigRouteDescriptorOutputDeviceImpl.m"
+ "AVFigRouteDescriptorOutputDeviceImplCanSetEndpointVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange"
+ "AVFigRouteDiscovererAvailableRoutesChanged"
+ "AVFigRouteDiscovererEndpointDescriptorChanged"
+ "AVFigRouteDiscovererInputDeviceDiscoverySessionImpl.m"
+ "AVFigRouteDiscovererRoutePresentChanged"
+ "AVFigRoutingContextInputContextImpl.m"
+ "AVFigRoutingContextModificationCallback"
+ "AVInputDeviceRouteDiscovererServerDeathNotificationCallback"
+ "AVLocalizedError"
+ "AVOutputContextUsesRouteConfigUpdatedNotification"
+ "AVOutputDeviceCopyFigModeForSpatialAudioMode"
+ "AVOutputDeviceDescriptionsFromFigDescriptions"
+ "AVOutputDeviceGetFigEndpoint"
+ "AVOutputDeviceGetFigRouteDescriptor"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode"
+ "AVOutputDeviceImplIsMutedForEndpointID"
+ "AVRoutingContextRouteChangeOperationRouteChangeComplete"
+ "AVRoutingOperationStatusResolveOldAndNew"
+ "AVRoutingOperation_trace"
+ "AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperationRouteConfigUpdated"
+ "AVRoutingSessionManagerGetLikelyDestinationsFromFig"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData"
+ "Failed to copy predicted selected route descriptor"
+ "Failed to get CanSetVolume of routing context"
+ "Failed to get input volume of routing context"
+ "Failed to reset predicted selected route descriptor"
+ "Failed to set input volume of routing context"
+ "FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_FallbackRouteDescriptor failed"
+ "No endpoint found for route descriptor"
+ "VolumeController failed to setup, returning"
+ "ccr_trace"
+ "err"
+ "kFigRouteDiscovererError_InvalidParameter"
+ "kMXError_AllocationFailed"
+ "non-"
+ "platformutilities_trace"
+ "scheduledaudioparameters_trace"
+ "stringWithValidatedFormatInteger"
+ "stringWithValidatedFormatString"
- "%s signalled err=%d at <>:%d"

```
