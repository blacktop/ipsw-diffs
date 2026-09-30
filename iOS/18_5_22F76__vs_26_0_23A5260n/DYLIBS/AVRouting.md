## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/AVRouting`

```diff

-240.6.1.0.0
-  __TEXT.__text: 0x3550
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x360
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x5aa
-  __TEXT.__oslogstring: 0x9d7
+270.59.4.11.2
+  __TEXT.__text: 0x677fc
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x6478
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0x720
+  __TEXT.__cstring: 0xdc7b
+  __TEXT.__oslogstring: 0xb749
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methname: 0x964
-  __TEXT.__objc_methtype: 0x13b
-  __TEXT.__objc_stubs: 0x8e0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x1830
+  __TEXT.__objc_classname: 0x16d4
+  __TEXT.__objc_methname: 0x93da
+  __TEXT.__objc_methtype: 0x2b42
+  __TEXT.__objc_stubs: 0x66a0
+  __DATA_CONST.__got: 0x1068
+  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__objc_classlist: 0x3e0
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x130
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x6c0
-  __DATA.__objc_ivar: 0x50
-  __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_CONST.__objc_selrefs: 0x1f60
+  __DATA_CONST.__objc_superrefs: 0x2d0
+  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__const: 0x3f0
+  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__objc_const: 0xba28
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x1bd0
+  __DATA.__objc_ivar: 0x534
+  __DATA.__data: 0xbd0
+  __DATA.__bss: 0x108
+  __DATA.__common: 0x140
+  __DATA_DIRTY.__objc_data: 0xaf0
+  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__common: 0xb0
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
+  - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EA5112B-6BA6-362F-9010-9223209051CE
-  Functions: 90
-  Symbols:   386
-  CStrings:  253
+  UUID: F19C3F16-0718-361C-A1BD-C116F5808A82
+  Functions: 2218
+  Symbols:   7765
+  CStrings:  3973
 
Symbols:
+ +[AVExecutionEnvironment currentPlatformIdentifier]
+ +[AVExecutionEnvironment initialize]
+ +[AVExecutionEnvironment resetPlatformIdentifierForQueue:]
+ +[AVExecutionEnvironment setPlatformIdentifier:forQueue:]
+ +[AVExecutionEnvironment sharedExecutionEnvironment]
+ +[AVExecutionEnvironment sharedExecutionEnvironment].cold.1
+ +[AVFigEndpointFigRoutingContextOutputDeviceTranslator sharedOutputDeviceTranslator]
+ +[AVFigEndpointUIAgentOutputContextManagerImpl copySharedEndpointUIAgent]
+ +[AVFigEndpointUIAgentOutputContextManagerImpl copySharedEndpointUIAgent].cold.1
+ +[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator sharedOutputDeviceTranslator]
+ +[AVFigRoutingContextInputContextImpl inputContextImplForID:type:]
+ +[AVFigRoutingContextInputContextImpl routingContextFactory]
+ +[AVFigRoutingContextInputContextImpl sharedSystemAudioInputContext]
+ +[AVFigRoutingContextOutputContextImpl addSharedAudioOutputContextImpl]
+ +[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]
+ +[AVFigRoutingContextOutputContextImpl auxiliaryOutputContext]
+ +[AVFigRoutingContextOutputContextImpl copySystemVideoRoutingContext]
+ +[AVFigRoutingContextOutputContextImpl defaultSharedOutputContextImpl]
+ +[AVFigRoutingContextOutputContextImpl iTunesAudioContext]
+ +[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]
+ +[AVFigRoutingContextOutputContextImpl outputContextImplForControllingOutputDeviceGroupWithID:options:]
+ +[AVFigRoutingContextOutputContextImpl outputContextImplForID:type:]
+ +[AVFigRoutingContextOutputContextImpl platformDependentScreenOrVideoContext]
+ +[AVFigRoutingContextOutputContextImpl resetOutputDeviceForAllOutputContexts]
+ +[AVFigRoutingContextOutputContextImpl routingContextFactory]
+ +[AVFigRoutingContextOutputContextImpl sharedAudioPresentationOutputContext]
+ +[AVFigRoutingContextOutputContextImpl sharedSystemAudioContext]
+ +[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]
+ +[AVFigRoutingContextOutputContextImpl sharedSystemRemotePoolContext]
+ +[AVFigRoutingContextOutputContextImpl sharedSystemScreenContext]
+ +[AVInputContext defaultInputContextImplClass]
+ +[AVInputContext initialize]
+ +[AVInputContext inputContextForID:]
+ +[AVInputContext sharedSystemAudioInputContext]
+ +[AVInputContext supportsSecureCoding]
+ +[AVInputDevice initialize]
+ +[AVInputDevice(FigRouteDescriptor) inputDeviceWithRouteDescriptor:routeDiscoverer:]
+ +[AVInputDevice(FigRouteDescriptor) inputDeviceWithRouteDescriptor:withRoutingContext:]
+ +[AVInputDevice(FigRouteDescriptor) inputDeviceWithRouteDescriptor:withRoutingContext:].cold.1
+ +[AVInputDeviceDiscoverySession initialize]
+ +[AVOutputContext addSharedAudioOutputContext]
+ +[AVOutputContext allSharedAudioOutputContexts]
+ +[AVOutputContext auxiliaryOutputContext]
+ +[AVOutputContext defaultOutputContextImplClass]
+ +[AVOutputContext defaultSharedOutputContext]
+ +[AVOutputContext iTunesAudioContext]
+ +[AVOutputContext initialize]
+ +[AVOutputContext outputContextExistsWithRemoteOutputDevice]
+ +[AVOutputContext outputContextForControllingOutputDeviceGroupWithID:]
+ +[AVOutputContext outputContextForControllingOutputDeviceGroupWithID:options:]
+ +[AVOutputContext outputContextForID:]
+ +[AVOutputContext outputContext]
+ +[AVOutputContext resetOutputDeviceForAllOutputContexts]
+ +[AVOutputContext sharedAudioPresentationOutputContext]
+ +[AVOutputContext sharedSystemAudioContext]
+ +[AVOutputContext sharedSystemRemoteDisplayContext]
+ +[AVOutputContext sharedSystemRemotePoolContext]
+ +[AVOutputContext sharedSystemScreenContext]
+ +[AVOutputContext supportsSecureCoding]
+ +[AVOutputContext(AVAudioSession) preferredOutputDevicesForAudioSession:]
+ +[AVOutputContext(FigRoutingContext) commChannelUUIDCommunicationChannelManagerCreator]
+ +[AVOutputContext(FigRoutingContext) defaultCommunicationChannelManagerCreator]
+ +[AVOutputContext(FigRoutingContext) outputContextWithFigRoutingContextCreator:]
+ +[AVOutputContext(FigRoutingContext) outputContextWithFigRoutingContextCreator:communicationChannelManagerCreator:]
+ +[AVOutputContext(FigRoutingContext) outputContextWithFigRoutingContextCreator:outputDeviceTranslator:]
+ +[AVOutputContext(FigRoutingContext) outputContextWithFigRoutingContextCreator:volumeController:]
+ +[AVOutputContextFactory sharedInstance]
+ +[AVOutputContextFactory sharedInstance].cold.1
+ +[AVOutputContextManager outputContextManagerForAllOutputContexts]
+ +[AVOutputContextManager outputContextManagerForAllOutputContexts].cold.1
+ +[AVOutputDevice initialize]
+ +[AVOutputDevice localDeviceDidChange]
+ +[AVOutputDevice sharedLocalDevice]
+ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:]
+ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:]
+ +[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:]
+ +[AVOutputDevice(FigRouteDescriptor) outputDeviceWithRouteDescriptor:]
+ +[AVOutputDevice(FigRouteDescriptor) outputDeviceWithRouteDescriptor:routeDiscoverer:]
+ +[AVOutputDevice(FigRouteDescriptor) outputDeviceWithRouteDescriptor:routingContextFactory:]
+ +[AVOutputDevice(FigRouteDescriptor) outputDeviceWithRouteDescriptor:volumeController:]
+ +[AVOutputDevice(FigRouteDescriptor) outputDeviceWithRouteDescriptor:withRoutingContext:]
+ +[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors]
+ +[AVOutputDeviceAuthorizationSession initialize]
+ +[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]
+ +[AVOutputDeviceAuthorizationSession sharedAuthorizationSession].cold.1
+ +[AVOutputDeviceAuthorizationSession(FigEndpointUIAgent) outputDeviceAuthorizationSessionWithEndpointUIAgent:]
+ +[AVOutputDeviceDiscoverySession initialize]
+ +[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionFactory]
+ +[AVOutputDeviceDiscoverySessionAvailableOutputDevices(AVOutputDeviceDiscoverySessionAvailableOutputDevices_FigEndpointImpl) outputDeviceDiscoverySessionAvailableOutputDevicesWithAvailableFigEndpoints:]
+ +[AVOutputDeviceFrecencyManager _applicationSupportPath]
+ +[AVOutputDeviceFrecencyManager _frecentsContainerPath]
+ +[AVOutputDeviceFrecencyManager _frecentsFilePath]
+ +[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary]
+ +[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary].cold.1
+ +[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary].cold.2
+ +[AVOutputDeviceFrecencyManager _frecentsWriter]
+ +[AVOutputDeviceFrecencyManager _frecentsWriter].cold.1
+ +[AVOutputDeviceFrecencyManager _migrateFrecentsFromCFPreferencesToFrecentsFilePath:]
+ +[AVOutputDeviceFrecencyManager frecencyScoreForDeviceID:]
+ +[AVOutputDeviceFrecencyManager updateFrecencyListForDeviceID:]
+ +[AVOutputDeviceGroup initialize]
+ +[AVOutputDeviceLegacyFrecentsReader defaultFrecentsReader]
+ +[AVOutputDeviceLegacyFrecentsWriter defaultFrecentsWriter]
+ +[AVPairedDevice pairedDevicesConnectedToOutputDevice:]
+ +[AVRoutingAmbienceLevelRamp ambienceLevelRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingAmbienceLevelRamp boundsAdjustedFloatValue:]
+ +[AVRoutingAmbienceLevelRamp defaultFloatValue]
+ +[AVRoutingAmbienceLoudnessRamp ambienceLoudnessRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingAmbienceLoudnessRamp boundsAdjustedFloatValue:]
+ +[AVRoutingAmbienceLoudnessRamp defaultFloatValue]
+ +[AVRoutingCMNotificationDispatcher initialize]
+ +[AVRoutingCMNotificationDispatcher notificationDispatcherForCMNotificationCenter:]
+ +[AVRoutingCMNotificationDispatcherListenerKey listenerKeyWithWeakReferenceToListener:callback:name:object:]
+ +[AVRoutingCallbackContextRegistry initialize]
+ +[AVRoutingCallbackContextRegistry sharedCallbackContextRegistry]
+ +[AVRoutingContextCommandOutputDeviceConfiguration initialize]
+ +[AVRoutingContextCommandOutputDeviceConfigurationModification initialize]
+ +[AVRoutingContextRouteChangeOperation initialize]
+ +[AVRoutingContextSendConfigureDeviceCommandOperation initialize]
+ +[AVRoutingDepartureAnnouncingObjectMonitor attachDepartureAnnouncingObjectMonitorToObject:monitoringObject:]
+ +[AVRoutingDialogLevelRamp boundsAdjustedFloatValue:]
+ +[AVRoutingDialogLevelRamp defaultFloatValue]
+ +[AVRoutingDialogLevelRamp dialogLevelRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingDialogLoudnessRamp boundsAdjustedFloatValue:]
+ +[AVRoutingDialogLoudnessRamp defaultFloatValue]
+ +[AVRoutingDialogLoudnessRamp dialogLoudnessRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingDialogMixBiasRamp boundsAdjustedFloatValue:]
+ +[AVRoutingDialogMixBiasRamp defaultFloatValue]
+ +[AVRoutingDialogMixBiasRamp dialogMixBiasRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingGlobalOperationQueue defaultQueue]
+ +[AVRoutingGlobalOperationQueue defaultQueue].cold.1
+ +[AVRoutingMutableScheduledAudioParameters scheduledAudioParameters]
+ +[AVRoutingOperation initialize]
+ +[AVRoutingOperation(ArrayOfOperations) statusOfOperations:error:]
+ +[AVRoutingPlaybackArbiter sharedRoutingPlaybackArbiter]
+ +[AVRoutingRecordingLoudnessRamp boundsAdjustedFloatValue:]
+ +[AVRoutingRecordingLoudnessRamp defaultFloatValue]
+ +[AVRoutingRecordingLoudnessRamp recordingLoudnessRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingRenderingStyleRamp boundsAdjustedFloatValue:]
+ +[AVRoutingRenderingStyleRamp defaultFloatValue]
+ +[AVRoutingRenderingStyleRamp renderingStyleRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation initialize]
+ +[AVRoutingScheduledFloatValueRamp boundsAdjustedFloatValue:]
+ +[AVRoutingScheduledFloatValueRamp defaultFloatValue]
+ +[AVRoutingScheduledFloatValueRamp defaultValue]
+ +[AVRoutingScheduledFloatValueRamp scheduledFloatValueRampWithStartValue:endValue:timeRange:]
+ +[AVRoutingScheduledParameterRamp _defaultAdditionalFigRepresentationObjects]
+ +[AVRoutingScheduledParameterRamp defaultValue]
+ +[AVRoutingScheduledParameterRamp(AVRoutingScheduledParameterRampSerialization) scheduledParameterRampWithPropertyList:]
+ +[AVRoutingScheduledVolumeRamp _defaultAdditionalFigRepresentationObjects]
+ +[AVRoutingScheduledVolumeRamp volumeRampWithStartVolume:endVolume:timeRange:rampMode:]
+ +[AVRoutingSerializedMostlySynchronousReentrantBlockScheduler initialize]
+ +[AVRoutingSessionManager initialize]
+ +[AVRoutingSessionManager longFormVideoManagerCanHaveCurrentSessionWithDestinationOfType:subType:]
+ +[AVRoutingSessionManager longFormVideoRoutingSessionManager]
+ +[AVRoutingWeakReference allocWithZone:]
+ +[AVRoutingWeakReference initialize]
+ +[AVSystemRemotePoolOutputDeviceCommunicationChannelManager sharedSystemRemotePoolImpl]
+ +[AVSystemRemotePoolOutputDeviceCommunicationChannelManager sharedSystemRemotePool]
+ +[CMAVRoutingTimeAsValue supportsSecureCoding]
+ +[CMAVRoutingTimeAsValue valueWithCMTime:]
+ +[CMAVRoutingTimeMappingAsValue supportsSecureCoding]
+ +[CMAVRoutingTimeMappingAsValue valueWithCMTimeMapping:]
+ +[CMAVRoutingTimeRangeAsValue supportsSecureCoding]
+ +[CMAVRoutingTimeRangeAsValue valueWithCMTimeRange:]
+ +[NSValue(NSValueCMTimeExtensions) valueWithCMTime:]
+ +[NSValue(NSValueCMTimeExtensions) valueWithCMTimeMapping:]
+ +[NSValue(NSValueCMTimeExtensions) valueWithCMTimeRange:]
+ +[NSValue(NSValueCMVideoDimensionsExtensions) valueWithCMVideoDimensions:]
+ -[AVClusterComponentOutputDeviceDescription dealloc]
+ -[AVClusterComponentOutputDeviceDescription deviceID]
+ -[AVClusterComponentOutputDeviceDescription deviceName]
+ -[AVClusterComponentOutputDeviceDescription deviceSubType]
+ -[AVClusterComponentOutputDeviceDescription deviceType]
+ -[AVClusterComponentOutputDeviceDescription initWithDeviceID:deviceName:deviceSubType:isClusterLeader:modelID:]
+ -[AVClusterComponentOutputDeviceDescription isClusterLeader]
+ -[AVClusterComponentOutputDeviceDescription modelID]
+ -[AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices allDevices]
+ -[AVExecutionEnvironment platformIdentifier]
+ -[AVFigCommChannelUUIDCommunicationChannelManager .cxx_destruct]
+ -[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]
+ -[AVFigCommChannelUUIDCommunicationChannelManager dealloc]
+ -[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]
+ -[AVFigCommChannelUUIDCommunicationChannelManager initWithRoutingContext:]
+ -[AVFigCommChannelUUIDCommunicationChannelManager init]
+ -[AVFigCommChannelUUIDCommunicationChannelManager openCommunicationChannelWithOptions:error:]
+ -[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]
+ -[AVFigCommChannelUUIDCommunicationChannelManager parentOutputContextImpl]
+ -[AVFigCommChannelUUIDCommunicationChannelManager setParentOutputContextImpl:]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl .cxx_destruct]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl commChannelUUID]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl dealloc]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl initWithRoutingContext:commChannelUUID:]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl init]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl parentCommunicationChannel]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl sendData:completionHandler:]
+ -[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl setParentCommunicationChannel:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator initForUsingRouteConfigUpdatedNotification:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator init]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl allDevices]
+ -[AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl dealloc]
+ -[AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl initWithAvailableFigEndpoints:]
+ -[AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl init]
+ -[AVFigEndpointOutputDeviceImpl .cxx_destruct]
+ -[AVFigEndpointOutputDeviceImpl HAPConformance]
+ -[AVFigEndpointOutputDeviceImpl ID]
+ -[AVFigEndpointOutputDeviceImpl MFiCertificateSerialNumber]
+ -[AVFigEndpointOutputDeviceImpl OEMIconLabel]
+ -[AVFigEndpointOutputDeviceImpl OEMIconVisible]
+ -[AVFigEndpointOutputDeviceImpl OEMIcons]
+ -[AVFigEndpointOutputDeviceImpl _canMuteDidChangeForEndpointWithID:]
+ -[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]
+ -[AVFigEndpointOutputDeviceImpl _carPlayTestNotification:]
+ -[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]
+ -[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:]
+ -[AVFigEndpointOutputDeviceImpl _handleFigEndpointEvent:payload:]
+ -[AVFigEndpointOutputDeviceImpl _iOSUIRequestedNotification:]
+ -[AVFigEndpointOutputDeviceImpl _mutedDidChangeForEndpointWithID:]
+ -[AVFigEndpointOutputDeviceImpl _siriRequestedNotification:]
+ -[AVFigEndpointOutputDeviceImpl _unhandledRemoteCommandNotification:]
+ -[AVFigEndpointOutputDeviceImpl _vehicleInformationDidChange:]
+ -[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:]
+ -[AVFigEndpointOutputDeviceImpl _volumeForEndpointDidChange:forRoomID:]
+ -[AVFigEndpointOutputDeviceImpl airPlayProperties]
+ -[AVFigEndpointOutputDeviceImpl allowsHeadTrackedSpatialAudio]
+ -[AVFigEndpointOutputDeviceImpl alternateTransportType]
+ -[AVFigEndpointOutputDeviceImpl authenticationType]
+ -[AVFigEndpointOutputDeviceImpl automaticallyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVFigEndpointOutputDeviceImpl availableBluetoothListeningModes]
+ -[AVFigEndpointOutputDeviceImpl batteryLevel]
+ -[AVFigEndpointOutputDeviceImpl borrowScreenForClient:reason:]
+ -[AVFigEndpointOutputDeviceImpl canAccessAppleMusic]
+ -[AVFigEndpointOutputDeviceImpl canAccessRemoteAssets]
+ -[AVFigEndpointOutputDeviceImpl canAccessiCloudMusicLibrary]
+ -[AVFigEndpointOutputDeviceImpl canBeGroupLeader]
+ -[AVFigEndpointOutputDeviceImpl canBeGrouped]
+ -[AVFigEndpointOutputDeviceImpl canCommunicateWithAllLogicalDeviceMembers]
+ -[AVFigEndpointOutputDeviceImpl canFetchMediaDataFromSender]
+ -[AVFigEndpointOutputDeviceImpl canMute]
+ -[AVFigEndpointOutputDeviceImpl canPlayEncryptedProgressiveDownloadAssets]
+ -[AVFigEndpointOutputDeviceImpl canRelayCommunicationChannel]
+ -[AVFigEndpointOutputDeviceImpl canSetVolume]
+ -[AVFigEndpointOutputDeviceImpl carOwnsMainAudio]
+ -[AVFigEndpointOutputDeviceImpl carOwnsScreen]
+ -[AVFigEndpointOutputDeviceImpl caseBatteryLevel]
+ -[AVFigEndpointOutputDeviceImpl clusterID]
+ -[AVFigEndpointOutputDeviceImpl clusterType]
+ -[AVFigEndpointOutputDeviceImpl clusteredDeviceDescriptions]
+ -[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]
+ -[AVFigEndpointOutputDeviceImpl configuredClusterSize]
+ -[AVFigEndpointOutputDeviceImpl connectedPairedDevices]
+ -[AVFigEndpointOutputDeviceImpl currentBluetoothListeningMode]
+ -[AVFigEndpointOutputDeviceImpl currentScreenViewAreaForScreenID:]
+ -[AVFigEndpointOutputDeviceImpl dealloc]
+ -[AVFigEndpointOutputDeviceImpl decreaseVolumeByCount:]
+ -[AVFigEndpointOutputDeviceImpl delegate]
+ -[AVFigEndpointOutputDeviceImpl deviceFeatures]
+ -[AVFigEndpointOutputDeviceImpl deviceSubType]
+ -[AVFigEndpointOutputDeviceImpl deviceType]
+ -[AVFigEndpointOutputDeviceImpl displayCornerMasks]
+ -[AVFigEndpointOutputDeviceImpl electronicTollCollection]
+ -[AVFigEndpointOutputDeviceImpl figEndpoint]
+ -[AVFigEndpointOutputDeviceImpl firmwareVersion]
+ -[AVFigEndpointOutputDeviceImpl groupContainsGroupLeader]
+ -[AVFigEndpointOutputDeviceImpl groupID]
+ -[AVFigEndpointOutputDeviceImpl hash]
+ -[AVFigEndpointOutputDeviceImpl headTrackedSpatialAudioMode]
+ -[AVFigEndpointOutputDeviceImpl identifyingMACAddress]
+ -[AVFigEndpointOutputDeviceImpl implEventListener]
+ -[AVFigEndpointOutputDeviceImpl increaseVolumeByCount:]
+ -[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]
+ -[AVFigEndpointOutputDeviceImpl init]
+ -[AVFigEndpointOutputDeviceImpl isActivatedForContinuityScreen]
+ -[AVFigEndpointOutputDeviceImpl isActivated]
+ -[AVFigEndpointOutputDeviceImpl isAppleAccessory]
+ -[AVFigEndpointOutputDeviceImpl isCached]
+ -[AVFigEndpointOutputDeviceImpl isClusterLeader]
+ -[AVFigEndpointOutputDeviceImpl isConversationDetectionEnabled]
+ -[AVFigEndpointOutputDeviceImpl isEqual:]
+ -[AVFigEndpointOutputDeviceImpl isGroupLeader]
+ -[AVFigEndpointOutputDeviceImpl isHeadTrackedSpatialAudioActive]
+ -[AVFigEndpointOutputDeviceImpl isInEar]
+ -[AVFigEndpointOutputDeviceImpl isInUseByPairedDevice]
+ -[AVFigEndpointOutputDeviceImpl isLogicalDeviceLeader]
+ -[AVFigEndpointOutputDeviceImpl isMuted]
+ -[AVFigEndpointOutputDeviceImpl isNightModeSupported]
+ -[AVFigEndpointOutputDeviceImpl leftBatteryLevel]
+ -[AVFigEndpointOutputDeviceImpl limitedUIElements]
+ -[AVFigEndpointOutputDeviceImpl limitedUI]
+ -[AVFigEndpointOutputDeviceImpl logicalDeviceID]
+ -[AVFigEndpointOutputDeviceImpl manufacturer]
+ -[AVFigEndpointOutputDeviceImpl modelID]
+ -[AVFigEndpointOutputDeviceImpl name]
+ -[AVFigEndpointOutputDeviceImpl navigationAidedDriving]
+ -[AVFigEndpointOutputDeviceImpl nightMode]
+ -[AVFigEndpointOutputDeviceImpl onlyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVFigEndpointOutputDeviceImpl outputDeviceHIDs]
+ -[AVFigEndpointOutputDeviceImpl outputDeviceInfo]
+ -[AVFigEndpointOutputDeviceImpl ownsTurnByTurnNavigation]
+ -[AVFigEndpointOutputDeviceImpl participatesInGroupPlayback]
+ -[AVFigEndpointOutputDeviceImpl performHapticFeedbackForUUID:withHapticType:completionHandler:]
+ -[AVFigEndpointOutputDeviceImpl presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets]
+ -[AVFigEndpointOutputDeviceImpl producesLowFidelityAudio]
+ -[AVFigEndpointOutputDeviceImpl proposedGroupID]
+ -[AVFigEndpointOutputDeviceImpl recognizingSpeech]
+ -[AVFigEndpointOutputDeviceImpl requestCarUIForURL:withUUID:]
+ -[AVFigEndpointOutputDeviceImpl requestTurnByTurnNavigationOwnership]
+ -[AVFigEndpointOutputDeviceImpl requestViewArea:forScreenID:]
+ -[AVFigEndpointOutputDeviceImpl requiresAuthorization]
+ -[AVFigEndpointOutputDeviceImpl rightBatteryLevel]
+ -[AVFigEndpointOutputDeviceImpl rightHandDrive]
+ -[AVFigEndpointOutputDeviceImpl screens]
+ -[AVFigEndpointOutputDeviceImpl serialNumber]
+ -[AVFigEndpointOutputDeviceImpl setActivatedDeviceClusterMembersVolume:withRoomID:]
+ -[AVFigEndpointOutputDeviceImpl setAllowsHeadTrackedSpatialAudio:error:]
+ -[AVFigEndpointOutputDeviceImpl setConversationDetectionEnabled:error:]
+ -[AVFigEndpointOutputDeviceImpl setCurrentBluetoothListeningMode:]
+ -[AVFigEndpointOutputDeviceImpl setCurrentBluetoothListeningMode:error:]
+ -[AVFigEndpointOutputDeviceImpl setDelegate:]
+ -[AVFigEndpointOutputDeviceImpl setDisplayCornerMasks:]
+ -[AVFigEndpointOutputDeviceImpl setHeadTrackedSpatialAudioMode:error:]
+ -[AVFigEndpointOutputDeviceImpl setImplEventListener:]
+ -[AVFigEndpointOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVFigEndpointOutputDeviceImpl setMuted:]
+ -[AVFigEndpointOutputDeviceImpl setSecondDisplayEnabled:]
+ -[AVFigEndpointOutputDeviceImpl setSecondDisplayMode:completionHandler:]
+ -[AVFigEndpointOutputDeviceImpl setSiriForwardingEnabled:]
+ -[AVFigEndpointOutputDeviceImpl setVolume:]
+ -[AVFigEndpointOutputDeviceImpl siriForwardingEnabled]
+ -[AVFigEndpointOutputDeviceImpl suggestUIWithURLs:completionHandler:]
+ -[AVFigEndpointOutputDeviceImpl supportedFeatures]
+ -[AVFigEndpointOutputDeviceImpl supportsBluetoothSharing]
+ -[AVFigEndpointOutputDeviceImpl supportsBufferedAirPlay]
+ -[AVFigEndpointOutputDeviceImpl supportsConversationDetection]
+ -[AVFigEndpointOutputDeviceImpl supportsDataOverACLProtocol]
+ -[AVFigEndpointOutputDeviceImpl supportsHeadTrackedSpatialAudio]
+ -[AVFigEndpointOutputDeviceImpl takeScreenForClient:reason:]
+ -[AVFigEndpointOutputDeviceImpl transportType]
+ -[AVFigEndpointOutputDeviceImpl voiceTriggerMode]
+ -[AVFigEndpointOutputDeviceImpl volumeControlType]
+ -[AVFigEndpointOutputDeviceImpl volumeForActivatedDeviceClusterMembersWithRoomID:]
+ -[AVFigEndpointOutputDeviceImpl volume]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl .cxx_destruct]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl _didCloseCommunicationChannel]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl _didReceiveData:]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl close]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl dealloc]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl initWithRemoteControlSession:]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl parentChannel]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl sendData:completionHandler:]
+ -[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl setParentChannel:]
+ -[AVFigEndpointSecondDisplayModeToken dealloc]
+ -[AVFigEndpointSecondDisplayModeToken initWithEndpoint:]
+ -[AVFigEndpointSecondDisplayModeToken init]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl .cxx_destruct]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl dealloc]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl parentOutputContextManager]
+ -[AVFigEndpointUIAgentOutputContextManagerImpl setParentOutputContextManager:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl .cxx_destruct]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl ID]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl authorizationTokenType]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl cancel]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl dealloc]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl enterTerminalStatus:error:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl initWithID:outputDevice:authorizationTokenType:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl outputDevice]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl parentAuthorizationSessionImpl]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl respondWithAuthorizationToken:completionHandler:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl setParentAuthorizationSessionImpl:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl .cxx_destruct]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _finishedWithPrompt]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _showAuthPromptWithUniqueID:routeDescriptor:pinMode:reason:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl dealloc]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl figEndpointUIAgent]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl outputDeviceAuthorizationRequestImpl:didRespondWithAuthorizationToken:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl outputDeviceAuthorizationRequestImplDidCancel:]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl parentAuthorizationSession]
+ -[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl setParentAuthorizationSession:]
+ -[AVFigRemoteRouteDiscovererFactory createRouteDiscovererWithAllocator:options:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator dealloc]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator initForUsingRouteConfigUpdatedNotification:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator init]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDeviceFromRoutingContext:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator outputDevicesFromRoutingContext:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator predictedOutputDeviceFromRoutingContext:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorInputDeviceImpl .cxx_destruct]
+ -[AVFigRouteDescriptorInputDeviceImpl ID]
+ -[AVFigRouteDescriptorInputDeviceImpl _handleRouteDescriptionEvent:payload:]
+ -[AVFigRouteDescriptorInputDeviceImpl _routeDescriptionDidChange:]
+ -[AVFigRouteDescriptorInputDeviceImpl _withEndpoint:]
+ -[AVFigRouteDescriptorInputDeviceImpl dealloc]
+ -[AVFigRouteDescriptorInputDeviceImpl deviceFeatures]
+ -[AVFigRouteDescriptorInputDeviceImpl deviceSubType]
+ -[AVFigRouteDescriptorInputDeviceImpl deviceType]
+ -[AVFigRouteDescriptorInputDeviceImpl hash]
+ -[AVFigRouteDescriptorInputDeviceImpl implEventListener]
+ -[AVFigRouteDescriptorInputDeviceImpl initWithRouteDescriptor:routeDiscoverer:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]
+ -[AVFigRouteDescriptorInputDeviceImpl init]
+ -[AVFigRouteDescriptorInputDeviceImpl inputDeviceInfo]
+ -[AVFigRouteDescriptorInputDeviceImpl isAppleAccessory]
+ -[AVFigRouteDescriptorInputDeviceImpl isConversationDetectionEnabled]
+ -[AVFigRouteDescriptorInputDeviceImpl isEqual:]
+ -[AVFigRouteDescriptorInputDeviceImpl isHighQualityContentCaptureEnabled]
+ -[AVFigRouteDescriptorInputDeviceImpl manufacturer]
+ -[AVFigRouteDescriptorInputDeviceImpl modelID]
+ -[AVFigRouteDescriptorInputDeviceImpl name]
+ -[AVFigRouteDescriptorInputDeviceImpl routeDescriptor]
+ -[AVFigRouteDescriptorInputDeviceImpl setImplEventListener:]
+ -[AVFigRouteDescriptorInputDeviceImpl setRouteDescriptor:]
+ -[AVFigRouteDescriptorInputDeviceImpl supportsConversationDetection]
+ -[AVFigRouteDescriptorInputDeviceImpl supportsHighQualityContentCapture]
+ -[AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl allDevices]
+ -[AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl dealloc]
+ -[AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl initWithRouteDescriptors:routeDiscoverer:]
+ -[AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl init]
+ -[AVFigRouteDescriptorOutputDeviceImpl .cxx_destruct]
+ -[AVFigRouteDescriptorOutputDeviceImpl HAPConformance]
+ -[AVFigRouteDescriptorOutputDeviceImpl ID]
+ -[AVFigRouteDescriptorOutputDeviceImpl MFiCertificateSerialNumber]
+ -[AVFigRouteDescriptorOutputDeviceImpl OEMIconLabel]
+ -[AVFigRouteDescriptorOutputDeviceImpl OEMIconVisible]
+ -[AVFigRouteDescriptorOutputDeviceImpl OEMIcons]
+ -[AVFigRouteDescriptorOutputDeviceImpl _canMuteDidChangeForEndpointWithID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _carPlayTestNotification:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _handleRouteDescriptionEvent:payload:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _iOSUIRequestedNotification:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _mutedDidChangeForEndpointWithID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _routeDescriptionDidChange:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _siriRequestedNotification:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _unhandledRemoteCommandNotification:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _vehicleInformationDidChange:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _volumeDidChangeForEndpointWithID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _volumeForEndpointDidChange:forRoomID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl _withEndpoint:]
+ -[AVFigRouteDescriptorOutputDeviceImpl airPlayProperties]
+ -[AVFigRouteDescriptorOutputDeviceImpl allowsHeadTrackedSpatialAudio]
+ -[AVFigRouteDescriptorOutputDeviceImpl alternateTransportType]
+ -[AVFigRouteDescriptorOutputDeviceImpl authenticationType]
+ -[AVFigRouteDescriptorOutputDeviceImpl automaticallyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVFigRouteDescriptorOutputDeviceImpl availableBluetoothListeningModes]
+ -[AVFigRouteDescriptorOutputDeviceImpl batteryLevel]
+ -[AVFigRouteDescriptorOutputDeviceImpl borrowScreenForClient:reason:]
+ -[AVFigRouteDescriptorOutputDeviceImpl canAccessAppleMusic]
+ -[AVFigRouteDescriptorOutputDeviceImpl canAccessRemoteAssets]
+ -[AVFigRouteDescriptorOutputDeviceImpl canAccessiCloudMusicLibrary]
+ -[AVFigRouteDescriptorOutputDeviceImpl canBeGroupLeader]
+ -[AVFigRouteDescriptorOutputDeviceImpl canBeGrouped]
+ -[AVFigRouteDescriptorOutputDeviceImpl canCommunicateWithAllLogicalDeviceMembers]
+ -[AVFigRouteDescriptorOutputDeviceImpl canFetchMediaDataFromSender]
+ -[AVFigRouteDescriptorOutputDeviceImpl canMute]
+ -[AVFigRouteDescriptorOutputDeviceImpl canPlayEncryptedProgressiveDownloadAssets]
+ -[AVFigRouteDescriptorOutputDeviceImpl canRelayCommunicationChannel]
+ -[AVFigRouteDescriptorOutputDeviceImpl canSetVolume]
+ -[AVFigRouteDescriptorOutputDeviceImpl carOwnsMainAudio]
+ -[AVFigRouteDescriptorOutputDeviceImpl carOwnsScreen]
+ -[AVFigRouteDescriptorOutputDeviceImpl caseBatteryLevel]
+ -[AVFigRouteDescriptorOutputDeviceImpl clusterID]
+ -[AVFigRouteDescriptorOutputDeviceImpl clusterType]
+ -[AVFigRouteDescriptorOutputDeviceImpl clusteredDeviceDescriptions]
+ -[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl configuredClusterSize]
+ -[AVFigRouteDescriptorOutputDeviceImpl connectedPairedDevices]
+ -[AVFigRouteDescriptorOutputDeviceImpl currentBluetoothListeningMode]
+ -[AVFigRouteDescriptorOutputDeviceImpl currentScreenViewAreaForScreenID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl dealloc]
+ -[AVFigRouteDescriptorOutputDeviceImpl decreaseVolumeByCount:]
+ -[AVFigRouteDescriptorOutputDeviceImpl delegate]
+ -[AVFigRouteDescriptorOutputDeviceImpl deviceFeatures]
+ -[AVFigRouteDescriptorOutputDeviceImpl deviceSubType]
+ -[AVFigRouteDescriptorOutputDeviceImpl deviceType]
+ -[AVFigRouteDescriptorOutputDeviceImpl displayCornerMasks]
+ -[AVFigRouteDescriptorOutputDeviceImpl electronicTollCollection]
+ -[AVFigRouteDescriptorOutputDeviceImpl firmwareVersion]
+ -[AVFigRouteDescriptorOutputDeviceImpl groupContainsGroupLeader]
+ -[AVFigRouteDescriptorOutputDeviceImpl groupID]
+ -[AVFigRouteDescriptorOutputDeviceImpl hash]
+ -[AVFigRouteDescriptorOutputDeviceImpl headTrackedSpatialAudioMode]
+ -[AVFigRouteDescriptorOutputDeviceImpl identifyingMACAddress]
+ -[AVFigRouteDescriptorOutputDeviceImpl implEventListener]
+ -[AVFigRouteDescriptorOutputDeviceImpl increaseVolumeByCount:]
+ -[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]
+ -[AVFigRouteDescriptorOutputDeviceImpl init]
+ -[AVFigRouteDescriptorOutputDeviceImpl isActivatedForContinuityScreen]
+ -[AVFigRouteDescriptorOutputDeviceImpl isActivated]
+ -[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory]
+ -[AVFigRouteDescriptorOutputDeviceImpl isCached]
+ -[AVFigRouteDescriptorOutputDeviceImpl isCarPlayVideoActive]
+ -[AVFigRouteDescriptorOutputDeviceImpl isCarPlayVideoAllowed]
+ -[AVFigRouteDescriptorOutputDeviceImpl isClusterLeader]
+ -[AVFigRouteDescriptorOutputDeviceImpl isConversationDetectionEnabled]
+ -[AVFigRouteDescriptorOutputDeviceImpl isEligibleToBePredictedOutputDevice]
+ -[AVFigRouteDescriptorOutputDeviceImpl isEqual:]
+ -[AVFigRouteDescriptorOutputDeviceImpl isGroupLeader]
+ -[AVFigRouteDescriptorOutputDeviceImpl isHeadTrackedSpatialAudioActive]
+ -[AVFigRouteDescriptorOutputDeviceImpl isInEar]
+ -[AVFigRouteDescriptorOutputDeviceImpl isInUseByPairedDevice]
+ -[AVFigRouteDescriptorOutputDeviceImpl isLogicalDeviceLeader]
+ -[AVFigRouteDescriptorOutputDeviceImpl isMuted]
+ -[AVFigRouteDescriptorOutputDeviceImpl isNightModeSupported]
+ -[AVFigRouteDescriptorOutputDeviceImpl leftBatteryLevel]
+ -[AVFigRouteDescriptorOutputDeviceImpl limitedUIElements]
+ -[AVFigRouteDescriptorOutputDeviceImpl limitedUI]
+ -[AVFigRouteDescriptorOutputDeviceImpl logicalDeviceID]
+ -[AVFigRouteDescriptorOutputDeviceImpl manufacturer]
+ -[AVFigRouteDescriptorOutputDeviceImpl mediaSessionStatus]
+ -[AVFigRouteDescriptorOutputDeviceImpl modelID]
+ -[AVFigRouteDescriptorOutputDeviceImpl name]
+ -[AVFigRouteDescriptorOutputDeviceImpl navigationAidedDriving]
+ -[AVFigRouteDescriptorOutputDeviceImpl nightMode]
+ -[AVFigRouteDescriptorOutputDeviceImpl onlyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVFigRouteDescriptorOutputDeviceImpl outputDeviceHIDs]
+ -[AVFigRouteDescriptorOutputDeviceImpl outputDeviceInfo]
+ -[AVFigRouteDescriptorOutputDeviceImpl ownsTurnByTurnNavigation]
+ -[AVFigRouteDescriptorOutputDeviceImpl participatesInGroupPlayback]
+ -[AVFigRouteDescriptorOutputDeviceImpl performHapticFeedbackForUUID:withHapticType:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets]
+ -[AVFigRouteDescriptorOutputDeviceImpl producesLowFidelityAudio]
+ -[AVFigRouteDescriptorOutputDeviceImpl proposedGroupID]
+ -[AVFigRouteDescriptorOutputDeviceImpl recognizingSpeech]
+ -[AVFigRouteDescriptorOutputDeviceImpl requestCarUIForURL:withUUID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl requestTurnByTurnNavigationOwnership]
+ -[AVFigRouteDescriptorOutputDeviceImpl requestViewArea:forScreenID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl requiresAuthorization]
+ -[AVFigRouteDescriptorOutputDeviceImpl rightBatteryLevel]
+ -[AVFigRouteDescriptorOutputDeviceImpl rightHandDrive]
+ -[AVFigRouteDescriptorOutputDeviceImpl routeDescriptor]
+ -[AVFigRouteDescriptorOutputDeviceImpl screens]
+ -[AVFigRouteDescriptorOutputDeviceImpl serialNumber]
+ -[AVFigRouteDescriptorOutputDeviceImpl setActivatedDeviceClusterMembersVolume:withRoomID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setAllowsHeadTrackedSpatialAudio:error:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setCarPlayVideoActive:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setConversationDetectionEnabled:error:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setCurrentBluetoothListeningMode:error:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setDelegate:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setDisplayCornerMasks:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setHeadTrackedSpatialAudioMode:error:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setImplEventListener:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setMuted:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setRouteDescriptor:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setSecondDisplayEnabled:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setSecondDisplayMode:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setSiriForwardingEnabled:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setVolume:]
+ -[AVFigRouteDescriptorOutputDeviceImpl siriForwardingEnabled]
+ -[AVFigRouteDescriptorOutputDeviceImpl suggestUIWithURLs:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportedFeatures]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsBluetoothSharing]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsBufferedAirPlay]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsConversationDetection]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsDataOverACLProtocol]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsFitnessDataDestination]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsHeadTrackedSpatialAudio]
+ -[AVFigRouteDescriptorOutputDeviceImpl supportsScreenMirroringControls]
+ -[AVFigRouteDescriptorOutputDeviceImpl takeScreenForClient:reason:]
+ -[AVFigRouteDescriptorOutputDeviceImpl transportType]
+ -[AVFigRouteDescriptorOutputDeviceImpl voiceTriggerMode]
+ -[AVFigRouteDescriptorOutputDeviceImpl volumeControlType]
+ -[AVFigRouteDescriptorOutputDeviceImpl volumeForActivatedDeviceClusterMembersWithRoomID:]
+ -[AVFigRouteDescriptorOutputDeviceImpl volume]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl .cxx_destruct]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _availableRoutesChanged]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _endpointDescriptorChanged]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _routePresentChanged]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _serverDied]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _serverDied].cold.1
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl audioSessionId]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl availableInputDevices]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl dealloc]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl devicePresenceDetected]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl fallbackInputDevice]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl init]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl parentInputDeviceDiscoverySession]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl routeDiscoverer]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl setAudioSessionId:]
+ -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl setParentInputDeviceDiscoverySession:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory dealloc]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory initWithRouteDiscovererFactory:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory init]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory routeDiscovererFactory]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl .cxx_destruct]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _availableGroupsChanged]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _availableRoutesChanged]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _endpointDescriptorChanged]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _routePresentChanged]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied].cold.1
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl dealloc]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl init]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionBluetoothOnlyDiscoveryDidChange:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionCachedDiscoveryDidChange:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl parentOutputDeviceDiscoverySession]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl routeDiscoverer]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setParentOutputDeviceDiscoverySession:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setTargetAudioSession:]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl targetAudioSession]
+ -[AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext completionHandler]
+ -[AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext dealloc]
+ -[AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext initWithCompletionHandler:]
+ -[AVFigRoutingContextInputContextCompletionContext completionHandler]
+ -[AVFigRoutingContextInputContextCompletionContext dealloc]
+ -[AVFigRoutingContextInputContextCompletionContext initWithCompletionHandler:]
+ -[AVFigRoutingContextInputContextImpl .cxx_destruct]
+ -[AVFigRoutingContextInputContextImpl ID]
+ -[AVFigRoutingContextInputContextImpl _createSelectRouteOptionsForSetInputDeviceOptions:]
+ -[AVFigRoutingContextInputContextImpl _createUserPreferredRouteModificationDictionary:]
+ -[AVFigRoutingContextInputContextImpl _currentRouteChanged]
+ -[AVFigRoutingContextInputContextImpl _routeChangeEndedWithID:reason:]
+ -[AVFigRoutingContextInputContextImpl _routeChangeStartedWithID:]
+ -[AVFigRoutingContextInputContextImpl _routeConfigUpdateEndedWithID:reason:]
+ -[AVFigRoutingContextInputContextImpl _routeConfigUpdateStartedWithID:]
+ -[AVFigRoutingContextInputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]
+ -[AVFigRoutingContextInputContextImpl _serverConnectionDied]
+ -[AVFigRoutingContextInputContextImpl clearUserPreferredInputDevice:error:]
+ -[AVFigRoutingContextInputContextImpl clearUserPreferredInputDevice:error:].cold.1
+ -[AVFigRoutingContextInputContextImpl dealloc]
+ -[AVFigRoutingContextInputContextImpl figRoutingContext]
+ -[AVFigRoutingContextInputContextImpl hash]
+ -[AVFigRoutingContextInputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:]
+ -[AVFigRoutingContextInputContextImpl initWithFigRoutingContextCreator:]
+ -[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]
+ -[AVFigRoutingContextInputContextImpl init]
+ -[AVFigRoutingContextInputContextImpl inputContextDidChangeApplicationProcessID:]
+ -[AVFigRoutingContextInputContextImpl inputContextType]
+ -[AVFigRoutingContextInputContextImpl inputDevice]
+ -[AVFigRoutingContextInputContextImpl isEqual:]
+ -[AVFigRoutingContextInputContextImpl parentInputContext]
+ -[AVFigRoutingContextInputContextImpl routingContextUUID]
+ -[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]
+ -[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:].cold.1
+ -[AVFigRoutingContextInputContextImpl setParentInputContext:]
+ -[AVFigRoutingContextInputContextImpl userPreferredInputDevice:]
+ -[AVFigRoutingContextInputContextImpl userPreferredInputDevice:].cold.1
+ -[AVFigRoutingContextOutputContextCompletionContext _getFigEndpointTypeFromAVOutputDeviceType:]
+ -[AVFigRoutingContextOutputContextCompletionContext completionHandler]
+ -[AVFigRoutingContextOutputContextCompletionContext dealloc]
+ -[AVFigRoutingContextOutputContextCompletionContext devicesType]
+ -[AVFigRoutingContextOutputContextCompletionContext initWithCompletionHandler:outputDevices:figRoutingContext:]
+ -[AVFigRoutingContextOutputContextCompletionContext reportModificationMetrics:]
+ -[AVFigRoutingContextOutputContextImpl .cxx_destruct]
+ -[AVFigRoutingContextOutputContextImpl ID]
+ -[AVFigRoutingContextOutputContextImpl _canMuteDidChangeForRoutingContextWithID:]
+ -[AVFigRoutingContextOutputContextImpl _canSetMasterVolumeDidChangeForRoutingContextWithID:]
+ -[AVFigRoutingContextOutputContextImpl _canUseForRoutingContextDidChangeForRoutingContextWIthID:]
+ -[AVFigRoutingContextOutputContextImpl _createSelectRouteOptionsForSetOutputDeviceOptions:]
+ -[AVFigRoutingContextOutputContextImpl _currentRouteChanged]
+ -[AVFigRoutingContextOutputContextImpl _groupConfigurationChanged]
+ -[AVFigRoutingContextOutputContextImpl _masterVolumeControlTypeDidChangeForRoutingContextWithID:]
+ -[AVFigRoutingContextOutputContextImpl _masterVolumeDidChangeForRoutingContextWithID:]
+ -[AVFigRoutingContextOutputContextImpl _muteDidChangeForRoutingContextWithID:]
+ -[AVFigRoutingContextOutputContextImpl _predictedSelectedRouteDescriptorChanged]
+ -[AVFigRoutingContextOutputContextImpl _remoteControlChannelAvailabilityChanged]
+ -[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:]
+ -[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:]
+ -[AVFigRoutingContextOutputContextImpl _routeConfigUpdateEndedWithID:reason:]
+ -[AVFigRoutingContextOutputContextImpl _routeConfigUpdateStartedWithID:]
+ -[AVFigRoutingContextOutputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]
+ -[AVFigRoutingContextOutputContextImpl _sendCommand:completionHandler:]
+ -[AVFigRoutingContextOutputContextImpl _serverConnectionDied]
+ -[AVFigRoutingContextOutputContextImpl _systemPickerVideoRouteChanged]
+ -[AVFigRoutingContextOutputContextImpl addOutputDevice:options:completionHandler:]
+ -[AVFigRoutingContextOutputContextImpl associatedAudioDeviceID]
+ -[AVFigRoutingContextOutputContextImpl canMute]
+ -[AVFigRoutingContextOutputContextImpl canSetVolume]
+ -[AVFigRoutingContextOutputContextImpl communicationChannelManager:didCloseCommunicationChannel:]
+ -[AVFigRoutingContextOutputContextImpl communicationChannelManager:didReceiveData:fromCommunicationChannel:]
+ -[AVFigRoutingContextOutputContextImpl dealloc]
+ -[AVFigRoutingContextOutputContextImpl decreaseVolumeByCount:]
+ -[AVFigRoutingContextOutputContextImpl figRoutingContext]
+ -[AVFigRoutingContextOutputContextImpl hash]
+ -[AVFigRoutingContextOutputContextImpl increaseVolumeByCount:]
+ -[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:]
+ -[AVFigRoutingContextOutputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:]
+ -[AVFigRoutingContextOutputContextImpl initWithFigRoutingContextCreator:]
+ -[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]
+ -[AVFigRoutingContextOutputContextImpl init]
+ -[AVFigRoutingContextOutputContextImpl isEqual:]
+ -[AVFigRoutingContextOutputContextImpl isMuted]
+ -[AVFigRoutingContextOutputContextImpl openCommunicationChannelWithOptions:error:]
+ -[AVFigRoutingContextOutputContextImpl outgoingCommunicationChannel]
+ -[AVFigRoutingContextOutputContextImpl outputContextDidChangeApplicationProcessID:]
+ -[AVFigRoutingContextOutputContextImpl outputContextType]
+ -[AVFigRoutingContextOutputContextImpl outputDevice]
+ -[AVFigRoutingContextOutputContextImpl outputDevices]
+ -[AVFigRoutingContextOutputContextImpl parentOutputContext]
+ -[AVFigRoutingContextOutputContextImpl predictedOutputDevice]
+ -[AVFigRoutingContextOutputContextImpl providesControlForAllVolumeFeatures]
+ -[AVFigRoutingContextOutputContextImpl removeOutputDevice:options:completionHandler:]
+ -[AVFigRoutingContextOutputContextImpl resetPredictedOutputDevice]
+ -[AVFigRoutingContextOutputContextImpl routingContextUUID]
+ -[AVFigRoutingContextOutputContextImpl setMuted:]
+ -[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:]
+ -[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:]
+ -[AVFigRoutingContextOutputContextImpl setParentOutputContext:]
+ -[AVFigRoutingContextOutputContextImpl setVolume:]
+ -[AVFigRoutingContextOutputContextImpl supportsMultipleBluetoothOutputDevices]
+ -[AVFigRoutingContextOutputContextImpl supportsMultipleOutputDevices]
+ -[AVFigRoutingContextOutputContextImpl volumeControlType]
+ -[AVFigRoutingContextOutputContextImpl volume]
+ -[AVInputContext ID]
+ -[AVInputContext applicationProcessID]
+ -[AVInputContext clearUserPreferredInputDevice:error:]
+ -[AVInputContext contextID]
+ -[AVInputContext dealloc]
+ -[AVInputContext description]
+ -[AVInputContext deviceName]
+ -[AVInputContext encodeWithCoder:]
+ -[AVInputContext getApplicationProcessID:]
+ -[AVInputContext hash]
+ -[AVInputContext impl]
+ -[AVInputContext initWithCoder:]
+ -[AVInputContext initWithInputContextImpl:]
+ -[AVInputContext init]
+ -[AVInputContext inputContextImpl:didChangeInputDeviceWithInitiator:]
+ -[AVInputContext inputContextImpl:didExpireWithReplacement:]
+ -[AVInputContext inputContextImpl:didInitiateDestinationChange:]
+ -[AVInputContext inputContextType]
+ -[AVInputContext inputDevice]
+ -[AVInputContext isEqual:]
+ -[AVInputContext setApplicationProcessID:]
+ -[AVInputContext setInputDevice:options:completionHandler:]
+ -[AVInputContext userPreferredInputDevice:]
+ -[AVInputContextDestinationChange _setStatus:]
+ -[AVInputContextDestinationChange dealloc]
+ -[AVInputContextDestinationChange description]
+ -[AVInputContextDestinationChange init]
+ -[AVInputContextDestinationChange markAsFailed]
+ -[AVInputContextDestinationChange markAsFinished]
+ -[AVInputContextDestinationChange markAsInProgress]
+ -[AVInputContextDestinationChange status]
+ -[AVInputContextDestinationChange(FigRoutingContextAdditions) changeToTerminalStatusBasedOnInputRouteChangeEndedReason:]
+ -[AVInputContextDestinationChange(FigRoutingContextAdditions) changeToTerminalStatusBasedOnInputRouteConfigUpdatedReason:]
+ -[AVInputDevice dealloc]
+ -[AVInputDevice description]
+ -[AVInputDevice deviceID]
+ -[AVInputDevice deviceName]
+ -[AVInputDevice deviceSubType]
+ -[AVInputDevice deviceType]
+ -[AVInputDevice impl]
+ -[AVInputDevice initWithInputDeviceImpl:]
+ -[AVInputDevice init]
+ -[AVInputDevice isAppleAccessory]
+ -[AVInputDevice isConversationDetectionEnabled]
+ -[AVInputDevice isHighQualityContentCaptureEnabled]
+ -[AVInputDevice manufacturer]
+ -[AVInputDevice modelID]
+ -[AVInputDevice supportsHighQualityContentCapture]
+ -[AVInputDeviceDiscoverySession audioSessionID]
+ -[AVInputDeviceDiscoverySession availableInputDevices]
+ -[AVInputDeviceDiscoverySession dealloc]
+ -[AVInputDeviceDiscoverySession devicePresenceDetected]
+ -[AVInputDeviceDiscoverySession discoveryMode]
+ -[AVInputDeviceDiscoverySession fallbackInputDevice]
+ -[AVInputDeviceDiscoverySession impl]
+ -[AVInputDeviceDiscoverySession initWithDeviceFeatures:]
+ -[AVInputDeviceDiscoverySession initWithInputDeviceDiscoverySessionImpl:]
+ -[AVInputDeviceDiscoverySession inputDeviceDiscoverySessionImpl:didExpireWithReplacement:]
+ -[AVInputDeviceDiscoverySession inputDeviceDiscoverySessionImplDidChangeAvailableInputDevices:]
+ -[AVInputDeviceDiscoverySession setAudioSessionID:]
+ -[AVInputDeviceDiscoverySession setDiscoveryMode:]
+ -[AVInputDeviceDiscoverySession setDiscoveryMode:forClientIdentifiers:]
+ -[AVInputDeviceDiscoverySession(FigRouteDiscoverer) routeDiscoverer]
+ -[AVLocalOutputDeviceImpl .cxx_destruct]
+ -[AVLocalOutputDeviceImpl HAPConformance]
+ -[AVLocalOutputDeviceImpl ID]
+ -[AVLocalOutputDeviceImpl MFiCertificateSerialNumber]
+ -[AVLocalOutputDeviceImpl OEMIconLabel]
+ -[AVLocalOutputDeviceImpl OEMIconVisible]
+ -[AVLocalOutputDeviceImpl OEMIcons]
+ -[AVLocalOutputDeviceImpl airPlayProperties]
+ -[AVLocalOutputDeviceImpl allowsHeadTrackedSpatialAudio]
+ -[AVLocalOutputDeviceImpl alternateTransportType]
+ -[AVLocalOutputDeviceImpl authenticationType]
+ -[AVLocalOutputDeviceImpl automaticallyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVLocalOutputDeviceImpl availableBluetoothListeningModes]
+ -[AVLocalOutputDeviceImpl batteryLevel]
+ -[AVLocalOutputDeviceImpl borrowScreenForClient:reason:]
+ -[AVLocalOutputDeviceImpl canAccessAppleMusic]
+ -[AVLocalOutputDeviceImpl canAccessRemoteAssets]
+ -[AVLocalOutputDeviceImpl canAccessiCloudMusicLibrary]
+ -[AVLocalOutputDeviceImpl canBeGroupLeader]
+ -[AVLocalOutputDeviceImpl canBeGrouped]
+ -[AVLocalOutputDeviceImpl canCommunicateWithAllLogicalDeviceMembers]
+ -[AVLocalOutputDeviceImpl canFetchMediaDataFromSender]
+ -[AVLocalOutputDeviceImpl canMute]
+ -[AVLocalOutputDeviceImpl canPlayEncryptedProgressiveDownloadAssets]
+ -[AVLocalOutputDeviceImpl canRelayCommunicationChannel]
+ -[AVLocalOutputDeviceImpl canSetVolume]
+ -[AVLocalOutputDeviceImpl carOwnsMainAudio]
+ -[AVLocalOutputDeviceImpl carOwnsScreen]
+ -[AVLocalOutputDeviceImpl caseBatteryLevel]
+ -[AVLocalOutputDeviceImpl clusterID]
+ -[AVLocalOutputDeviceImpl clusterType]
+ -[AVLocalOutputDeviceImpl clusteredDeviceDescriptions]
+ -[AVLocalOutputDeviceImpl configureUsingBlock:options:completionHandler:]
+ -[AVLocalOutputDeviceImpl configuredClusterSize]
+ -[AVLocalOutputDeviceImpl connectedPairedDevices]
+ -[AVLocalOutputDeviceImpl currentBluetoothListeningMode]
+ -[AVLocalOutputDeviceImpl currentScreenViewAreaForScreenID:]
+ -[AVLocalOutputDeviceImpl decreaseVolumeByCount:]
+ -[AVLocalOutputDeviceImpl delegate]
+ -[AVLocalOutputDeviceImpl deviceFeatures]
+ -[AVLocalOutputDeviceImpl deviceSubType]
+ -[AVLocalOutputDeviceImpl deviceType]
+ -[AVLocalOutputDeviceImpl displayCornerMasks]
+ -[AVLocalOutputDeviceImpl electronicTollCollection]
+ -[AVLocalOutputDeviceImpl firmwareVersion]
+ -[AVLocalOutputDeviceImpl groupContainsGroupLeader]
+ -[AVLocalOutputDeviceImpl groupID]
+ -[AVLocalOutputDeviceImpl hash]
+ -[AVLocalOutputDeviceImpl headTrackedSpatialAudioMode]
+ -[AVLocalOutputDeviceImpl identifyingMACAddress]
+ -[AVLocalOutputDeviceImpl implEventListener]
+ -[AVLocalOutputDeviceImpl increaseVolumeByCount:]
+ -[AVLocalOutputDeviceImpl isActivatedForContinuityScreen]
+ -[AVLocalOutputDeviceImpl isActivated]
+ -[AVLocalOutputDeviceImpl isAppleAccessory]
+ -[AVLocalOutputDeviceImpl isCached]
+ -[AVLocalOutputDeviceImpl isCarPlayVideoActive]
+ -[AVLocalOutputDeviceImpl isCarPlayVideoAllowed]
+ -[AVLocalOutputDeviceImpl isClusterLeader]
+ -[AVLocalOutputDeviceImpl isConversationDetectionEnabled]
+ -[AVLocalOutputDeviceImpl isEligibleToBePredictedOutputDevice]
+ -[AVLocalOutputDeviceImpl isEqual:]
+ -[AVLocalOutputDeviceImpl isGroupLeader]
+ -[AVLocalOutputDeviceImpl isHeadTrackedSpatialAudioActive]
+ -[AVLocalOutputDeviceImpl isInEar]
+ -[AVLocalOutputDeviceImpl isInUseByPairedDevice]
+ -[AVLocalOutputDeviceImpl isLogicalDeviceLeader]
+ -[AVLocalOutputDeviceImpl isMuted]
+ -[AVLocalOutputDeviceImpl isNightModeSupported]
+ -[AVLocalOutputDeviceImpl leftBatteryLevel]
+ -[AVLocalOutputDeviceImpl limitedUIElements]
+ -[AVLocalOutputDeviceImpl limitedUI]
+ -[AVLocalOutputDeviceImpl logicalDeviceID]
+ -[AVLocalOutputDeviceImpl manufacturer]
+ -[AVLocalOutputDeviceImpl mediaSessionStatus]
+ -[AVLocalOutputDeviceImpl modelID]
+ -[AVLocalOutputDeviceImpl name]
+ -[AVLocalOutputDeviceImpl navigationAidedDriving]
+ -[AVLocalOutputDeviceImpl nightMode]
+ -[AVLocalOutputDeviceImpl onlyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVLocalOutputDeviceImpl outputDeviceHIDs]
+ -[AVLocalOutputDeviceImpl outputDeviceInfo]
+ -[AVLocalOutputDeviceImpl ownsTurnByTurnNavigation]
+ -[AVLocalOutputDeviceImpl participatesInGroupPlayback]
+ -[AVLocalOutputDeviceImpl performHapticFeedbackForUUID:withHapticType:completionHandler:]
+ -[AVLocalOutputDeviceImpl presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets]
+ -[AVLocalOutputDeviceImpl producesLowFidelityAudio]
+ -[AVLocalOutputDeviceImpl proposedGroupID]
+ -[AVLocalOutputDeviceImpl recognizingSpeech]
+ -[AVLocalOutputDeviceImpl requestCarUIForURL:withUUID:]
+ -[AVLocalOutputDeviceImpl requestTurnByTurnNavigationOwnership]
+ -[AVLocalOutputDeviceImpl requestViewArea:forScreenID:]
+ -[AVLocalOutputDeviceImpl requiresAuthorization]
+ -[AVLocalOutputDeviceImpl rightBatteryLevel]
+ -[AVLocalOutputDeviceImpl rightHandDrive]
+ -[AVLocalOutputDeviceImpl screens]
+ -[AVLocalOutputDeviceImpl serialNumber]
+ -[AVLocalOutputDeviceImpl setActivatedDeviceClusterMembersVolume:withRoomID:]
+ -[AVLocalOutputDeviceImpl setAllowsHeadTrackedSpatialAudio:error:]
+ -[AVLocalOutputDeviceImpl setCarPlayVideoActive:completionHandler:]
+ -[AVLocalOutputDeviceImpl setConversationDetectionEnabled:error:]
+ -[AVLocalOutputDeviceImpl setCurrentBluetoothListeningMode:error:]
+ -[AVLocalOutputDeviceImpl setDelegate:]
+ -[AVLocalOutputDeviceImpl setDisplayCornerMasks:]
+ -[AVLocalOutputDeviceImpl setHeadTrackedSpatialAudioMode:error:]
+ -[AVLocalOutputDeviceImpl setImplEventListener:]
+ -[AVLocalOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVLocalOutputDeviceImpl setMuted:]
+ -[AVLocalOutputDeviceImpl setSecondDisplayEnabled:]
+ -[AVLocalOutputDeviceImpl setSecondDisplayMode:completionHandler:]
+ -[AVLocalOutputDeviceImpl setSiriForwardingEnabled:]
+ -[AVLocalOutputDeviceImpl setVolume:]
+ -[AVLocalOutputDeviceImpl siriForwardingEnabled]
+ -[AVLocalOutputDeviceImpl suggestUIWithURLs:completionHandler:]
+ -[AVLocalOutputDeviceImpl supportedFeatures]
+ -[AVLocalOutputDeviceImpl supportsBluetoothSharing]
+ -[AVLocalOutputDeviceImpl supportsBufferedAirPlay]
+ -[AVLocalOutputDeviceImpl supportsConversationDetection]
+ -[AVLocalOutputDeviceImpl supportsDataOverACLProtocol]
+ -[AVLocalOutputDeviceImpl supportsFitnessDataDestination]
+ -[AVLocalOutputDeviceImpl supportsHeadTrackedSpatialAudio]
+ -[AVLocalOutputDeviceImpl supportsScreenMirroringControls]
+ -[AVLocalOutputDeviceImpl takeScreenForClient:reason:]
+ -[AVLocalOutputDeviceImpl transportType]
+ -[AVLocalOutputDeviceImpl voiceTriggerMode]
+ -[AVLocalOutputDeviceImpl volumeControlType]
+ -[AVLocalOutputDeviceImpl volumeForActivatedDeviceClusterMembersWithRoomID:]
+ -[AVLocalOutputDeviceImpl volume]
+ -[AVOutputContext ID]
+ -[AVOutputContext _initWithWebKitPropertyListData:]
+ -[AVOutputContext _webKitPropertyListData]
+ -[AVOutputContext addOutputDevice:]
+ -[AVOutputContext addOutputDevice:options:completionHandler:]
+ -[AVOutputContext applicationProcessID]
+ -[AVOutputContext canMute]
+ -[AVOutputContext canSetVolume]
+ -[AVOutputContext communicationChannelDelegate]
+ -[AVOutputContext contextID]
+ -[AVOutputContext dealloc]
+ -[AVOutputContext decreaseVolumeByCount:]
+ -[AVOutputContext description]
+ -[AVOutputContext deviceName]
+ -[AVOutputContext encodeWithCoder:]
+ -[AVOutputContext getApplicationProcessID:]
+ -[AVOutputContext hash]
+ -[AVOutputContext impl]
+ -[AVOutputContext increaseVolumeByCount:]
+ -[AVOutputContext initWithCoder:]
+ -[AVOutputContext initWithOutputContextImpl:]
+ -[AVOutputContext init]
+ -[AVOutputContext isEqual:]
+ -[AVOutputContext isMuted]
+ -[AVOutputContext openCommunicationChannelWithOptions:error:]
+ -[AVOutputContext outgoingCommunicationChannel]
+ -[AVOutputContext outputContextImpl:didChangeOutputDeviceWithInitiator:]
+ -[AVOutputContext outputContextImpl:didChangeOutputDevicesWithInitiator:reason:deviceID:previousDeviceIDs:]
+ -[AVOutputContext outputContextImpl:didCloseCommunicationChannel:]
+ -[AVOutputContext outputContextImpl:didExpireWithReplacement:]
+ -[AVOutputContext outputContextImpl:didInitiateDestinationChange:]
+ -[AVOutputContext outputContextImpl:didReceiveData:fromCommunicationChannel:]
+ -[AVOutputContext outputContextImplDidChangeCanMute:]
+ -[AVOutputContext outputContextImplDidChangeCanSetVolume:]
+ -[AVOutputContext outputContextImplDidChangeGlobalOutputDeviceConfiguration:]
+ -[AVOutputContext outputContextImplDidChangeGlobalOutputDeviceConfiguration:].cold.1
+ -[AVOutputContext outputContextImplDidChangeMute:]
+ -[AVOutputContext outputContextImplDidChangePredictedOutputDevice:]
+ -[AVOutputContext outputContextImplDidChangeProvidesControlForAllVolumeFeatures:]
+ -[AVOutputContext outputContextImplDidChangeVolume:]
+ -[AVOutputContext outputContextImplDidChangeVolumeControlType:]
+ -[AVOutputContext outputContextImplOutgoingCommunicationChannelDidBecomeAvailable:]
+ -[AVOutputContext outputContextType]
+ -[AVOutputContext outputDeviceFeatures]
+ -[AVOutputContext outputDevice]
+ -[AVOutputContext outputDevices]
+ -[AVOutputContext predictedOutputDevice]
+ -[AVOutputContext providesControlForAllVolumeFeatures]
+ -[AVOutputContext removeOutputDevice:]
+ -[AVOutputContext removeOutputDevice:options:completionHandler:]
+ -[AVOutputContext resetPredictedOutputDevice]
+ -[AVOutputContext setApplicationProcessID:]
+ -[AVOutputContext setCommunicationChannelDelegate:]
+ -[AVOutputContext setMuted:]
+ -[AVOutputContext setOutputDevice:forFeatures:]
+ -[AVOutputContext setOutputDevice:options:]
+ -[AVOutputContext setOutputDevice:options:completionHandler:]
+ -[AVOutputContext setOutputDevices:]
+ -[AVOutputContext setOutputDevices:options:completionHandler:]
+ -[AVOutputContext setVolume:]
+ -[AVOutputContext supportsMultipleBluetoothOutputDevices]
+ -[AVOutputContext supportsMultipleOutputDevices]
+ -[AVOutputContext volumeControlType]
+ -[AVOutputContext volume]
+ -[AVOutputContext(FigRoutingContext) figRoutingContext]
+ -[AVOutputContextCommunicationChannel dealloc]
+ -[AVOutputContextCommunicationChannel impl]
+ -[AVOutputContextCommunicationChannel initWithOutputContextCommunicationChannelImpl:]
+ -[AVOutputContextCommunicationChannel init]
+ -[AVOutputContextCommunicationChannel sendData:completionHandler:]
+ -[AVOutputContextCommunicationChannel(FigCommChannelUUID) commChannelUUID]
+ -[AVOutputContextDestinationChange _setStatus:cancellationReason:]
+ -[AVOutputContextDestinationChange cancellationReason]
+ -[AVOutputContextDestinationChange dealloc]
+ -[AVOutputContextDestinationChange description]
+ -[AVOutputContextDestinationChange init]
+ -[AVOutputContextDestinationChange markAsCancelledWithReason:]
+ -[AVOutputContextDestinationChange markAsFailed]
+ -[AVOutputContextDestinationChange markAsFinished]
+ -[AVOutputContextDestinationChange markAsInProgress]
+ -[AVOutputContextDestinationChange status]
+ -[AVOutputContextDestinationChange(FigRoutingContextAdditions) changeToTerminalStatusBasedOnRouteChangeEndedReason:]
+ -[AVOutputContextDestinationChange(FigRoutingContextAdditions) changeToTerminalStatusBasedOnRouteConfigUpdatedReason:]
+ -[AVOutputContextFactory dealloc]
+ -[AVOutputContextFactory init]
+ -[AVOutputContextFactory outputContextForContextID:]
+ -[AVOutputContextFactory setOutputContext:forContextID:]
+ -[AVOutputContextInternal .cxx_destruct]
+ -[AVOutputContextManager dealloc]
+ -[AVOutputContextManager initWithOutputContextManagerImpl:]
+ -[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:]
+ -[AVOutputContextManager outputContextManagerImplDidExpireWithReplacementImpl:]
+ -[AVOutputContextModificationResult cancellationReason]
+ -[AVOutputContextModificationResult dealloc]
+ -[AVOutputContextModificationResult initWithFigRouteConfigUpdatedReason:metrics:]
+ -[AVOutputContextModificationResult modificationMetrics]
+ -[AVOutputContextModificationResult status]
+ -[AVOutputDevice HAPConformance]
+ -[AVOutputDevice ID]
+ -[AVOutputDevice MFiCertificateSerialNumber]
+ -[AVOutputDevice OEMIconLabel]
+ -[AVOutputDevice OEMIconVisible]
+ -[AVOutputDevice OEMIcons]
+ -[AVOutputDevice _shouldHideAirPlayInfoDuringDemo]
+ -[AVOutputDevice _shouldHideAirPlayInfoDuringDemo].cold.1
+ -[AVOutputDevice activatedDeviceClusterMembersDidChangeVolume:forRoomID:]
+ -[AVOutputDevice airPlayProperties]
+ -[AVOutputDevice allowsHeadTrackedSpatialAudio]
+ -[AVOutputDevice alternateTransportType]
+ -[AVOutputDevice authenticationType]
+ -[AVOutputDevice automaticallyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVOutputDevice availableBluetoothListeningModes]
+ -[AVOutputDevice batteryLevel]
+ -[AVOutputDevice borrowScreenForClient:reason:]
+ -[AVOutputDevice canAccessAppleMusic]
+ -[AVOutputDevice canAccessRemoteAssets]
+ -[AVOutputDevice canAccessiCloudMusicLibrary]
+ -[AVOutputDevice canBeGroupLeader]
+ -[AVOutputDevice canBeGrouped]
+ -[AVOutputDevice canCommunicateWithAllLogicalDeviceMembers]
+ -[AVOutputDevice canFetchMediaDataFromSender]
+ -[AVOutputDevice canMute]
+ -[AVOutputDevice canPlayEncryptedProgressiveDownloadAssets]
+ -[AVOutputDevice canRelayCommunicationChannel]
+ -[AVOutputDevice canSetVolume]
+ -[AVOutputDevice carOwnsMainAudio]
+ -[AVOutputDevice carOwnsScreen]
+ -[AVOutputDevice clusterID]
+ -[AVOutputDevice clusterType]
+ -[AVOutputDevice clusteredDeviceDescriptions]
+ -[AVOutputDevice communicationChannelDelegate]
+ -[AVOutputDevice communicationChannelManager:didCloseCommunicationChannel:]
+ -[AVOutputDevice communicationChannelManager:didReceiveData:fromCommunicationChannel:]
+ -[AVOutputDevice configureUsingBlock:completionHandler:]
+ -[AVOutputDevice configureUsingBlock:options:completionHandler:]
+ -[AVOutputDevice configuredClusterSize]
+ -[AVOutputDevice connectedPairedDevices]
+ -[AVOutputDevice currentBluetoothListeningMode]
+ -[AVOutputDevice currentScreenViewAreaForScreenID:]
+ -[AVOutputDevice dealloc]
+ -[AVOutputDevice decreaseVolumeByCount:]
+ -[AVOutputDevice delegate]
+ -[AVOutputDevice description]
+ -[AVOutputDevice deviceFeatures]
+ -[AVOutputDevice deviceID]
+ -[AVOutputDevice deviceName]
+ -[AVOutputDevice deviceSubType]
+ -[AVOutputDevice deviceType]
+ -[AVOutputDevice displayCornerMasks]
+ -[AVOutputDevice electronicTollCollection]
+ -[AVOutputDevice firmwareVersion]
+ -[AVOutputDevice frecencyScore]
+ -[AVOutputDevice groupContainsGroupLeader]
+ -[AVOutputDevice groupID]
+ -[AVOutputDevice hasBatteryLevel]
+ -[AVOutputDevice hash]
+ -[AVOutputDevice headTrackedSpatialAudioMode]
+ -[AVOutputDevice identifyingMACAddress]
+ -[AVOutputDevice impl]
+ -[AVOutputDevice increaseVolumeByCount:]
+ -[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:]
+ -[AVOutputDevice init]
+ -[AVOutputDevice isActivatedForContinuityScreen]
+ -[AVOutputDevice isActivated]
+ -[AVOutputDevice isAppleAccessory]
+ -[AVOutputDevice isCached]
+ -[AVOutputDevice isCarPlayVideoActive]
+ -[AVOutputDevice isCarPlayVideoAllowed]
+ -[AVOutputDevice isClusterLeader]
+ -[AVOutputDevice isConversationDetectionEnabled]
+ -[AVOutputDevice isEligibleToBePredictedOutputDevice]
+ -[AVOutputDevice isEqual:]
+ -[AVOutputDevice isGroupLeader]
+ -[AVOutputDevice isHeadTrackedSpatialAudioActive]
+ -[AVOutputDevice isInUseByPairedDevice]
+ -[AVOutputDevice isLogicalDeviceLeader]
+ -[AVOutputDevice isMuted]
+ -[AVOutputDevice isNightModeSupported]
+ -[AVOutputDevice limitedUIElements]
+ -[AVOutputDevice limitedUI]
+ -[AVOutputDevice logicalDeviceID]
+ -[AVOutputDevice manufacturer]
+ -[AVOutputDevice mediaSessionStatus]
+ -[AVOutputDevice modelID]
+ -[AVOutputDevice modelSpecificInformation]
+ -[AVOutputDevice name]
+ -[AVOutputDevice navigationAidedDriving]
+ -[AVOutputDevice nightMode]
+ -[AVOutputDevice onlyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVOutputDevice openCommunicationChannelToDestination:options:completionHandler:]
+ -[AVOutputDevice openCommunicationChannelWithOptions:completionHandler:]
+ -[AVOutputDevice outputDeviceHIDs]
+ -[AVOutputDevice outputDeviceImplCanMuteDidChange:]
+ -[AVOutputDevice outputDeviceImplDidChangeCanChangeVolume:]
+ -[AVOutputDevice outputDeviceImplDidChangeMute:]
+ -[AVOutputDevice outputDeviceImplDidChangeProposedGroupID:]
+ -[AVOutputDevice outputDeviceImplDidChangeVolume:]
+ -[AVOutputDevice outputDeviceImplDidChangeVolumeControlType:]
+ -[AVOutputDevice outputDeviceInfo]
+ -[AVOutputDevice ownsTurnByTurnNavigation]
+ -[AVOutputDevice participatesInGroupPlayback]
+ -[AVOutputDevice performHapticFeedbackForUUID:withHapticType:completionHandler:]
+ -[AVOutputDevice postNotification:fromImpl:]
+ -[AVOutputDevice postNotification:withPayload:fromImpl:]
+ -[AVOutputDevice presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets]
+ -[AVOutputDevice producesLowFidelityAudio]
+ -[AVOutputDevice proposedGroupID]
+ -[AVOutputDevice recognizingSpeech]
+ -[AVOutputDevice requestCarUIForURL:withUUID:]
+ -[AVOutputDevice requestTurnByTurnNavigationOwnership]
+ -[AVOutputDevice requestViewArea:forScreenID:]
+ -[AVOutputDevice requiresAuthorization]
+ -[AVOutputDevice rightHandDrive]
+ -[AVOutputDevice screens]
+ -[AVOutputDevice serialNumber]
+ -[AVOutputDevice setActivatedDeviceClusterMembersVolume:withRoomID:]
+ -[AVOutputDevice setAllowsHeadTrackedSpatialAudio:error:]
+ -[AVOutputDevice setCarPlayVideoActive:completionHandler:]
+ -[AVOutputDevice setCommunicationChannelDelegate:]
+ -[AVOutputDevice setConversationDetectionEnabled:error:]
+ -[AVOutputDevice setCurrentBluetoothListeningMode:]
+ -[AVOutputDevice setCurrentBluetoothListeningMode:error:]
+ -[AVOutputDevice setDelegate:]
+ -[AVOutputDevice setDisplayCornerMasks:]
+ -[AVOutputDevice setHeadTrackedSpatialAudioMode:error:]
+ -[AVOutputDevice setMediaRemoteData:completionHandler:]
+ -[AVOutputDevice setMuted:]
+ -[AVOutputDevice setSecondDisplayEnabled:]
+ -[AVOutputDevice setSecondDisplayMode:completionHandler:]
+ -[AVOutputDevice setSiriForwardingEnabled:]
+ -[AVOutputDevice setVolume:]
+ -[AVOutputDevice siriForwardingEnabled]
+ -[AVOutputDevice suggestUIWithURLs:completionHandler:]
+ -[AVOutputDevice supportedFeatures]
+ -[AVOutputDevice supportsBluetoothSharing]
+ -[AVOutputDevice supportsBufferedAirPlay]
+ -[AVOutputDevice supportsConversationDetection]
+ -[AVOutputDevice supportsFitnessDataDestination]
+ -[AVOutputDevice supportsHeadTrackedSpatialAudio]
+ -[AVOutputDevice supportsScreenMirroringControls]
+ -[AVOutputDevice takeScreenForClient:reason:]
+ -[AVOutputDevice transportType]
+ -[AVOutputDevice updateFrecencyScore]
+ -[AVOutputDevice voiceTriggerMode]
+ -[AVOutputDevice volumeControlType]
+ -[AVOutputDevice volumeForActivatedDeviceClusterMembersWithRoomID:]
+ -[AVOutputDevice volume]
+ -[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) figEndpointOutputDeviceImpl]
+ -[AVOutputDeviceAuthorizationRequest ID]
+ -[AVOutputDeviceAuthorizationRequest authorizationTokenType]
+ -[AVOutputDeviceAuthorizationRequest cancel]
+ -[AVOutputDeviceAuthorizationRequest dealloc]
+ -[AVOutputDeviceAuthorizationRequest description]
+ -[AVOutputDeviceAuthorizationRequest error]
+ -[AVOutputDeviceAuthorizationRequest impl]
+ -[AVOutputDeviceAuthorizationRequest initWithOutputDeviceAuthorizationRequestImpl:]
+ -[AVOutputDeviceAuthorizationRequest outputDevice]
+ -[AVOutputDeviceAuthorizationRequest respondWithAuthorizationToken:completionHandler:]
+ -[AVOutputDeviceAuthorizationRequest status]
+ -[AVOutputDeviceAuthorizationSession dealloc]
+ -[AVOutputDeviceAuthorizationSession delegate]
+ -[AVOutputDeviceAuthorizationSession impl]
+ -[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:]
+ -[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImpl:didProvideAuthorizationRequest:]
+ -[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImpl:shouldRetryAuthorizationRequest:reason:]
+ -[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]
+ -[AVOutputDeviceAuthorizationSession setDelegate:]
+ -[AVOutputDeviceAuthorizationSessionInternal .cxx_destruct]
+ -[AVOutputDeviceAuthorizedPeer dealloc]
+ -[AVOutputDeviceAuthorizedPeer hasAdministratorPrivileges]
+ -[AVOutputDeviceAuthorizedPeer hash]
+ -[AVOutputDeviceAuthorizedPeer initWithID:publicKey:hasAdministratorPrivileges:]
+ -[AVOutputDeviceAuthorizedPeer init]
+ -[AVOutputDeviceAuthorizedPeer isEqual:]
+ -[AVOutputDeviceAuthorizedPeer peerID]
+ -[AVOutputDeviceAuthorizedPeer publicKey]
+ -[AVOutputDeviceCommunicationChannel .cxx_destruct]
+ -[AVOutputDeviceCommunicationChannel close]
+ -[AVOutputDeviceCommunicationChannel communicationChannelImpl:didReceiveData:]
+ -[AVOutputDeviceCommunicationChannel communicationChannelImplDidClose:]
+ -[AVOutputDeviceCommunicationChannel dealloc]
+ -[AVOutputDeviceCommunicationChannel delegate]
+ -[AVOutputDeviceCommunicationChannel initWithOutputDeviceCommunicationChannelImpl:]
+ -[AVOutputDeviceCommunicationChannel sendData:completionHandler:]
+ -[AVOutputDeviceCommunicationChannel setDelegate:]
+ -[AVOutputDeviceDiscoverySession availableOutputDevicesObject]
+ -[AVOutputDeviceDiscoverySession availableOutputDevices]
+ -[AVOutputDeviceDiscoverySession cachedDiscoveryEnabled]
+ -[AVOutputDeviceDiscoverySession dealloc]
+ -[AVOutputDeviceDiscoverySession devicePresenceDetected]
+ -[AVOutputDeviceDiscoverySession discoveryMode]
+ -[AVOutputDeviceDiscoverySession impl]
+ -[AVOutputDeviceDiscoverySession initWithDeviceFeatures:]
+ -[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:]
+ -[AVOutputDeviceDiscoverySession init]
+ -[AVOutputDeviceDiscoverySession onlyDiscoversBluetoothDevices]
+ -[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImpl:didExpireWithReplacement:]
+ -[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:]
+ -[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:]
+ -[AVOutputDeviceDiscoverySession setCachedDiscoveryEnabled:]
+ -[AVOutputDeviceDiscoverySession setDiscoveryMode:]
+ -[AVOutputDeviceDiscoverySession setDiscoveryMode:forClientIdentifiers:]
+ -[AVOutputDeviceDiscoverySession setOnlyDiscoversBluetoothDevices:]
+ -[AVOutputDeviceDiscoverySession setTargetAudioSession:]
+ -[AVOutputDeviceDiscoverySession targetAudioSession]
+ -[AVOutputDeviceDiscoverySession(FigRouteDiscoverer) routeDiscoverer]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices _loadOutputDevices]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices dealloc]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices hash]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices impl]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices initWithOutputDeviceDiscoverySessionAvailableOutputDevicesImpl:]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices init]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices isEqual:]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices]
+ -[AVOutputDeviceDiscoverySessionAvailableOutputDevices recentlyUsedDevices]
+ -[AVOutputDeviceFrecentsReader dealloc]
+ -[AVOutputDeviceFrecentsReader deviceIDs]
+ -[AVOutputDeviceFrecentsReader frecencyInfoForDeviceWithID:]
+ -[AVOutputDeviceFrecentsReader initWithFrecentsFilePath:error:]
+ -[AVOutputDeviceFrecentsReader init]
+ -[AVOutputDeviceFrecentsWriter dealloc]
+ -[AVOutputDeviceFrecentsWriter initWithFrecentsFilePath:]
+ -[AVOutputDeviceFrecentsWriter init]
+ -[AVOutputDeviceFrecentsWriter numberOfKeysToBeSet]
+ -[AVOutputDeviceFrecentsWriter persistToDiskReturningError:]
+ -[AVOutputDeviceFrecentsWriter removeFrecencyInfoForDeviceID:]
+ -[AVOutputDeviceFrecentsWriter setFrecencyInfo:forDeviceID:]
+ -[AVOutputDeviceGroup addOutputDevice:withOptions:completionHandler:]
+ -[AVOutputDeviceGroup dealloc]
+ -[AVOutputDeviceGroup description]
+ -[AVOutputDeviceGroup groupLeader]
+ -[AVOutputDeviceGroup hash]
+ -[AVOutputDeviceGroup impl]
+ -[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:]
+ -[AVOutputDeviceGroup isEqual:]
+ -[AVOutputDeviceGroup outputDeviceGroupImpl:didChangeOutputDevicesWithInitiator:]
+ -[AVOutputDeviceGroup outputDeviceGroupImplDidChangeVolume:]
+ -[AVOutputDeviceGroup outputDeviceGroupImplDidChangeVolumeControlType:]
+ -[AVOutputDeviceGroup outputDevices]
+ -[AVOutputDeviceGroup receivesLongFormAudioFromLocalDevice]
+ -[AVOutputDeviceGroup removeOutputDevice:withOptions:completionHandler:]
+ -[AVOutputDeviceGroup setVolume:]
+ -[AVOutputDeviceGroup volumeControlType]
+ -[AVOutputDeviceGroup volume]
+ -[AVOutputDeviceGroupMembershipChangeResult cancellationReason]
+ -[AVOutputDeviceGroupMembershipChangeResult dealloc]
+ -[AVOutputDeviceGroupMembershipChangeResult initWithStatus:cancellationReason:]
+ -[AVOutputDeviceGroupMembershipChangeResult status]
+ -[AVOutputDeviceHID UUID]
+ -[AVOutputDeviceHID dealloc]
+ -[AVOutputDeviceHID initWithUUID:screenUUID:endpoint:]
+ -[AVOutputDeviceHID inputMode]
+ -[AVOutputDeviceHID screenID]
+ -[AVOutputDeviceHID setInputMode:]
+ -[AVOutputDeviceIcon dealloc]
+ -[AVOutputDeviceIcon imageData]
+ -[AVOutputDeviceIcon initWithDict:]
+ -[AVOutputDeviceIcon isPrerendered]
+ -[AVOutputDeviceIcon pixelSize]
+ -[AVOutputDeviceInternal .cxx_destruct]
+ -[AVOutputDeviceLegacyFrecentsReader deviceIDs]
+ -[AVOutputDeviceLegacyFrecentsReader frecencyInfoForDeviceWithID:]
+ -[AVOutputDeviceLegacyFrecentsWriter dealloc]
+ -[AVOutputDeviceLegacyFrecentsWriter init]
+ -[AVOutputDeviceLegacyFrecentsWriter numberOfKeysToBeSet]
+ -[AVOutputDeviceLegacyFrecentsWriter persistToDiskReturningError:]
+ -[AVOutputDeviceLegacyFrecentsWriter removeFrecencyInfoForDeviceID:]
+ -[AVOutputDeviceLegacyFrecentsWriter setFrecencyInfo:forDeviceID:]
+ -[AVOutputDeviceScreenBorrowToken client]
+ -[AVOutputDeviceScreenBorrowToken dealloc]
+ -[AVOutputDeviceScreenBorrowToken initWithEndpoint:client:reason:]
+ -[AVOutputDeviceScreenBorrowToken init]
+ -[AVOutputDeviceScreenBorrowToken reason]
+ -[AVOutputDeviceScreenInfo ID]
+ -[AVOutputDeviceScreenInfo applicationURL]
+ -[AVOutputDeviceScreenInfo cornerMasks]
+ -[AVOutputDeviceScreenInfo dealloc]
+ -[AVOutputDeviceScreenInfo initWithDict:]
+ -[AVOutputDeviceScreenInfo initialApplicationURL]
+ -[AVOutputDeviceScreenInfo inputCapabilities]
+ -[AVOutputDeviceScreenInfo isLimitedUI]
+ -[AVOutputDeviceScreenInfo isNightMode]
+ -[AVOutputDeviceScreenInfo limitedUIElements]
+ -[AVOutputDeviceScreenInfo maxFPS]
+ -[AVOutputDeviceScreenInfo physicalSize]
+ -[AVOutputDeviceScreenInfo pixelSize]
+ -[AVOutputDeviceScreenInfo primaryInputDevice]
+ -[AVOutputDeviceScreenInfo squarePixelSize]
+ -[AVOutputDeviceScreenInfo viewAreas]
+ -[AVOutputDeviceScreenInfo viewHeightScaleFactor]
+ -[AVOutputDeviceTurnByTurnToken dealloc]
+ -[AVOutputDeviceTurnByTurnToken initWithEndpoint:]
+ -[AVOutputDeviceTurnByTurnToken init]
+ -[AVOutputDeviceViewAreaInfo dealloc]
+ -[AVOutputDeviceViewAreaInfo initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:]
+ -[AVOutputDeviceViewAreaInfo safeArea]
+ -[AVOutputDeviceViewAreaInfo statusBarEdge]
+ -[AVOutputDeviceViewAreaInfo supportsFocusTransfer]
+ -[AVOutputDeviceViewAreaInfo transitionControl]
+ -[AVOutputDeviceViewAreaInfo viewArea]
+ -[AVPairedDevice ID]
+ -[AVPairedDevice dealloc]
+ -[AVPairedDevice initWithName:ID:modelID:playing:productName:]
+ -[AVPairedDevice isPlaying]
+ -[AVPairedDevice modelID]
+ -[AVPairedDevice name]
+ -[AVPairedDevice pairedDeviceID]
+ -[AVPairedDevice productName]
+ -[AVRoutingBlockOperation cancel]
+ -[AVRoutingBlockOperation dealloc]
+ -[AVRoutingBlockOperation initWithBlock:]
+ -[AVRoutingBlockOperation initWithBlock:].cold.1
+ -[AVRoutingBlockOperation init]
+ -[AVRoutingBlockOperation start]
+ -[AVRoutingCMNotificationDispatcher CMNotificationCenter]
+ -[AVRoutingCMNotificationDispatcher _copyAndRemoveObserverForWeakReferenceToListener:callback:name:object:]
+ -[AVRoutingCMNotificationDispatcher addListenerWithWeakReference:callback:name:object:flags:]
+ -[AVRoutingCMNotificationDispatcher dealloc]
+ -[AVRoutingCMNotificationDispatcher initWithCMNotificationCenter:]
+ -[AVRoutingCMNotificationDispatcher initWithCMNotificationCenter:].cold.1
+ -[AVRoutingCMNotificationDispatcher init]
+ -[AVRoutingCMNotificationDispatcher removeListenerWithWeakReference:callback:name:object:]
+ -[AVRoutingCMNotificationDispatcherListenerKey copyWithZone:]
+ -[AVRoutingCMNotificationDispatcherListenerKey dealloc]
+ -[AVRoutingCMNotificationDispatcherListenerKey hash]
+ -[AVRoutingCMNotificationDispatcherListenerKey initWithWeakReferenceToListener:callback:name:object:]
+ -[AVRoutingCMNotificationDispatcherListenerKey init]
+ -[AVRoutingCMNotificationDispatcherListenerKey isEqual:]
+ -[AVRoutingCallbackContextRegistry callbackContextForToken:]
+ -[AVRoutingCallbackContextRegistry dealloc]
+ -[AVRoutingCallbackContextRegistry init]
+ -[AVRoutingCallbackContextRegistry registerCallbackContextObject:]
+ -[AVRoutingCallbackContextRegistry unregisterCallbackContextForToken:]
+ -[AVRoutingContextCommandOutputDeviceConfiguration automaticallyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVRoutingContextCommandOutputDeviceConfiguration dealloc]
+ -[AVRoutingContextCommandOutputDeviceConfiguration deviceID]
+ -[AVRoutingContextCommandOutputDeviceConfiguration deviceName]
+ -[AVRoutingContextCommandOutputDeviceConfiguration devicePassword]
+ -[AVRoutingContextCommandOutputDeviceConfiguration devicePublicKey]
+ -[AVRoutingContextCommandOutputDeviceConfiguration initWithRoutingContextComandResponse:]
+ -[AVRoutingContextCommandOutputDeviceConfiguration init]
+ -[AVRoutingContextCommandOutputDeviceConfiguration onlyAllowsConnectionsFromPeersInHomeGroup]
+ -[AVRoutingContextCommandOutputDeviceConfiguration peersInHomeGroup]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification addPeerToHomeGroup:]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification dealloc]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification init]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification removePeerWithIDFromHomeGroup:]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification routingContextCommandPayload]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification setDeviceName:]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification setDevicePassword:]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:]
+ -[AVRoutingContextCommandOutputDeviceConfigurationModification stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup]
+ -[AVRoutingContextRouteChangeOperation _routeChangeComplete]
+ -[AVRoutingContextRouteChangeOperation _routeChangeStartedWithID:]
+ -[AVRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]
+ -[AVRoutingContextRouteChangeOperation _setResultIfNotAlreadySet:]
+ -[AVRoutingContextRouteChangeOperation _setResultInputIfNotAlreadySet:]
+ -[AVRoutingContextRouteChangeOperation dealloc]
+ -[AVRoutingContextRouteChangeOperation initWithRoutingContext:successNotification:routeChangeBlock:isInputContextOperation:]
+ -[AVRoutingContextRouteChangeOperation init]
+ -[AVRoutingContextRouteChangeOperation isAsynchronous]
+ -[AVRoutingContextRouteChangeOperation resultInput]
+ -[AVRoutingContextRouteChangeOperation result]
+ -[AVRoutingContextRouteChangeOperation start]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation dealloc]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation finalConfiguration]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation initWithRoutingContext:configuratorBlock:]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation init]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation isAsynchronous]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation setFinalConfiguration:]
+ -[AVRoutingContextSendConfigureDeviceCommandOperation start]
+ -[AVRoutingDepartureAnnouncingObjectMonitor dealloc]
+ -[AVRoutingDepartureAnnouncingObjectMonitor initWithMonitoringObject:]
+ -[AVRoutingDispatchOnce init]
+ -[AVRoutingDispatchOnce runBlockOnce:]
+ -[AVRoutingEventWaiter dealloc]
+ -[AVRoutingEventWaiter init]
+ -[AVRoutingEventWaiter markEventAsCompleted]
+ -[AVRoutingEventWaiter waitUntilEventIsCompleted]
+ -[AVRoutingGlobalOperationQueue dealloc]
+ -[AVRoutingGlobalOperationQueue description]
+ -[AVRoutingGlobalOperationQueue enqueueOperation:]
+ -[AVRoutingGlobalOperationQueue init]
+ -[AVRoutingGlobalOperationQueue unfinishedOperations]
+ -[AVRoutingMutableScheduledAudioParameters _setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:]
+ -[AVRoutingMutableScheduledAudioParameters copyWithZone:]
+ -[AVRoutingMutableScheduledAudioParameters setVolume:atTime:]
+ -[AVRoutingMutableScheduledAudioParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:]
+ -[AVRoutingMutableScheduledAudioParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:]
+ -[AVRoutingOperation _setStatus:error:resultingStatus:failureReason:]
+ -[AVRoutingOperation dealloc]
+ -[AVRoutingOperation didEnterTerminalState]
+ -[AVRoutingOperation error]
+ -[AVRoutingOperation evaluateDependenciesAndMarkAsExecuting]
+ -[AVRoutingOperation init]
+ -[AVRoutingOperation isExecuting]
+ -[AVRoutingOperation isFinished]
+ -[AVRoutingOperation isReady]
+ -[AVRoutingOperation markAsCancelled]
+ -[AVRoutingOperation markAsCompleted]
+ -[AVRoutingOperation markAsFailedWithError:]
+ -[AVRoutingOperation status]
+ -[AVRoutingOperationQueueWithFundamentalDependency addOperation:]
+ -[AVRoutingOperationQueueWithFundamentalDependency addOperations:waitUntilFinished:]
+ -[AVRoutingOperationQueueWithFundamentalDependency dealloc]
+ -[AVRoutingOperationQueueWithFundamentalDependency initWithFundamentalOperation:]
+ -[AVRoutingPlaybackArbiter _externalPlaybackIsActiveForParticipant:]
+ -[AVRoutingPlaybackArbiter _externalPlaybackPriorityForParticipant:]
+ -[AVRoutingPlaybackArbiter _nonMixablePriorityForParticipant:]
+ -[AVRoutingPlaybackArbiter _setDefaultExternalPlaybackPriorityForParticipant:]
+ -[AVRoutingPlaybackArbiter _setDefaultNonMixableAudioPriorityForParticipant:]
+ -[AVRoutingPlaybackArbiter _setExternalPlaybackPriority:forParticipant:]
+ -[AVRoutingPlaybackArbiter _setNonMixableAudioPriority:forParticipant:]
+ -[AVRoutingPlaybackArbiter _setWeakRefToPreferredParticipantForExternalPlayback:]
+ -[AVRoutingPlaybackArbiter _setWeakRefToPreferredParticipantForNonMixableAudio:]
+ -[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]
+ -[AVRoutingPlaybackArbiter _updatePreferredParticipantForExternalPlaybackFrom:toParticipant:checkingAllParticipants:]
+ -[AVRoutingPlaybackArbiter _updatePreferredParticipantForNonMixableAudioRouteFrom:toParticipant:checkingAllParticipants:]
+ -[AVRoutingPlaybackArbiter dealloc]
+ -[AVRoutingPlaybackArbiter init]
+ -[AVRoutingPlaybackArbiter preferredParticipantForExternalPlayback]
+ -[AVRoutingPlaybackArbiter preferredParticipantForNonMixableAudioRoutes]
+ -[AVRoutingPlaybackArbiter setPreferredParticipantForExternalPlayback:]
+ -[AVRoutingPlaybackArbiter setPreferredParticipantForNonMixableAudioRoutes:]
+ -[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _addTrackedParticipant:]
+ -[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _allTrackedParticipants]
+ -[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _removeTrackedParticipant:]
+ -[AVRoutingPlaybackArbiter(AVRoutingPlaybackParticipantRegistration) deregisterParticipant:]
+ -[AVRoutingPlaybackArbiter(AVRoutingPlaybackParticipantRegistration) registerParticipant:]
+ -[AVRoutingRetainReleaseWeakReference dealloc]
+ -[AVRoutingRetainReleaseWeakReference description]
+ -[AVRoutingRetainReleaseWeakReference initWithReferencedObject:]
+ -[AVRoutingRetainReleaseWeakReference init]
+ -[AVRoutingRetainReleaseWeakReference referencedObject]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _routeConfigUpdateWithID:endedWithReason:]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _setResultIfNotAlreadySet:]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _setResultInputIfNotAlreadySet:]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation dealloc]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation initWithRoutingContext:routeChangeID:routeChangeBlock:isInputContextOperation:]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation init]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation isAsynchronous]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation resultInput]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation result]
+ -[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation start]
+ -[AVRoutingScheduledAudioParameters _isScheduledRampClass:]
+ -[AVRoutingScheduledAudioParameters _rampsOfClass:]
+ -[AVRoutingScheduledAudioParameters _ramps]
+ -[AVRoutingScheduledAudioParameters _setRamps:]
+ -[AVRoutingScheduledAudioParameters _volumeCurveKeysForScheduledRampClassNames]
+ -[AVRoutingScheduledAudioParameters _volumeCurveKeysForScheduledRampClassNames].cold.1
+ -[AVRoutingScheduledAudioParameters copyWithZone:]
+ -[AVRoutingScheduledAudioParameters dealloc]
+ -[AVRoutingScheduledAudioParameters description]
+ -[AVRoutingScheduledAudioParameters getVolumeRampForTime:startVolume:endVolume:timeRange:]
+ -[AVRoutingScheduledAudioParameters getVolumeRampForTime:startVolume:endVolume:timeRange:rampMode:]
+ -[AVRoutingScheduledAudioParameters hash]
+ -[AVRoutingScheduledAudioParameters initWithPropertyList:]
+ -[AVRoutingScheduledAudioParameters init]
+ -[AVRoutingScheduledAudioParameters isEqual:]
+ -[AVRoutingScheduledAudioParameters mutableCopyWithZone:]
+ -[AVRoutingScheduledAudioParameters propertyList]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _audioCurveOfClass:]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _audioVolumeCurve]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _figAudioCurves]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _getRampOfClass:forTime:timeRange:]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _setRamp:]
+ -[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _volumeCurveAsString]
+ -[AVRoutingScheduledFloatValueRamp _interpolatedValueAtTime:]
+ -[AVRoutingScheduledFloatValueRamp _makeRampWithTruncatedTimeRange:endValue:]
+ -[AVRoutingScheduledFloatValueRamp _parameterRampMode]
+ -[AVRoutingScheduledFloatValueRamp endFloatValue]
+ -[AVRoutingScheduledFloatValueRamp endValue]
+ -[AVRoutingScheduledFloatValueRamp initWithStartValue:endValue:timeRange:]
+ -[AVRoutingScheduledFloatValueRamp scheduledParameterRampInterpolatedToTime:]
+ -[AVRoutingScheduledFloatValueRamp startFloatValue]
+ -[AVRoutingScheduledFloatValueRamp startValue]
+ -[AVRoutingScheduledFloatValueRamp(AVRoutingScheduledParameterRampSerialization) initWithPropertyList:]
+ -[AVRoutingScheduledFloatValueRamp(AVRoutingScheduledParameterRampSerialization) propertyList]
+ -[AVRoutingScheduledParameterRamp _additionalFigRepresentationObjects]
+ -[AVRoutingScheduledParameterRamp copyWithZone:]
+ -[AVRoutingScheduledParameterRamp description]
+ -[AVRoutingScheduledParameterRamp endValue]
+ -[AVRoutingScheduledParameterRamp hash]
+ -[AVRoutingScheduledParameterRamp initWithTimeRange:]
+ -[AVRoutingScheduledParameterRamp isEqual:]
+ -[AVRoutingScheduledParameterRamp scheduledParameterRampInterpolatedToTime:]
+ -[AVRoutingScheduledParameterRamp startValue]
+ -[AVRoutingScheduledParameterRamp timeRange]
+ -[AVRoutingScheduledParameterRamp(AVRoutingScheduledParameterRampSerialization) initWithPropertyList:]
+ -[AVRoutingScheduledParameterRamp(AVRoutingScheduledParameterRampSerialization) propertyList]
+ -[AVRoutingScheduledVolumeRamp _additionalFigRepresentationObjects]
+ -[AVRoutingScheduledVolumeRamp _makeRampWithTruncatedTimeRange:endValue:]
+ -[AVRoutingScheduledVolumeRamp _parameterRampMode]
+ -[AVRoutingScheduledVolumeRamp endVolume]
+ -[AVRoutingScheduledVolumeRamp initWithStartVolume:endVolume:timeRange:rampMode:]
+ -[AVRoutingScheduledVolumeRamp rampMode]
+ -[AVRoutingScheduledVolumeRamp startVolume]
+ -[AVRoutingScheduledVolumeRamp(AVRoutingScheduledParameterRampSerialization) initWithPropertyList:]
+ -[AVRoutingScheduledVolumeRamp(AVRoutingScheduledParameterRampSerialization) propertyList]
+ -[AVRoutingSerializedMostlySynchronousReentrantBlockScheduler dealloc]
+ -[AVRoutingSerializedMostlySynchronousReentrantBlockScheduler init]
+ -[AVRoutingSerializedMostlySynchronousReentrantBlockScheduler scheduleBlock:]
+ -[AVRoutingSession dealloc]
+ -[AVRoutingSession description]
+ -[AVRoutingSession destination]
+ -[AVRoutingSession establishedAutomaticallyFromLikelyDestination]
+ -[AVRoutingSession initWithFigRoutingSession:]
+ -[AVRoutingSession init]
+ -[AVRoutingSessionDestination _canQueryOutputDeviceDescriptionsAndReturnCurrentValue:]
+ -[AVRoutingSessionDestination dealloc]
+ -[AVRoutingSessionDestination description]
+ -[AVRoutingSessionDestination initWithFigRoutingSessionDestination:]
+ -[AVRoutingSessionDestination init]
+ -[AVRoutingSessionDestination outputDeviceDescriptions]
+ -[AVRoutingSessionDestination probability]
+ -[AVRoutingSessionDestination providesExternalVideoPlayback]
+ -[AVRoutingSessionManager allLikelyDestinations]
+ -[AVRoutingSessionManager currentRoutingSession]
+ -[AVRoutingSessionManager dealloc]
+ -[AVRoutingSessionManager description]
+ -[AVRoutingSessionManager initWithFigRoutingSessionManager:]
+ -[AVRoutingSessionManager init]
+ -[AVRoutingSessionManager likelyExternalDestinations]
+ -[AVRoutingSessionManager prefersLikelyDestinationsOverCurrentRoutingSession]
+ -[AVRoutingSessionManager startRoutingSessionForHighConfidenceExternalDestinationIfPresentWithCompletionHandler:]
+ -[AVRoutingSessionManager startRoutingSessionWithOutputDeviceDescriptions:error:]
+ -[AVRoutingSessionManager startSuppressingLikelyDestinationsUntilNextPlayEventAndReturnError:]
+ -[AVRoutingSessionManager stopSuppressingLikelyDestinationsAndReturnError:]
+ -[AVRoutingSessionManager updateCurrentRoutingSessionFromLikelyDestinationsWithCompletionHandler:]
+ -[AVRoutingSynchronousBlockScheduler scheduleBlock:]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _balanceMonitoringIsFinishedSemaphore]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _monitoredObject]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _registerForObjectNotifications]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _signalMonitoringIsFinishedIfNeeded]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _unregisterForObjectNotifications]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation _waitUntilFinishedIfNeeded]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation cancel]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation dealloc]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation initWithObject:notificationNames:]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation main]
+ -[AVRoutingWaitForNotificationOrDeallocationOperation monitoredObjectHasDeparted]
+ -[AVRoutingWeakReference initWithReferencedObject:]
+ -[AVRoutingWeakReference referencedObject]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl .cxx_destruct]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl close]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl dealloc]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl initWithDeviceID:channelUUID:outputContext:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl parentChannel]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl sendData:completionHandler:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl setParentChannel:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager .cxx_destruct]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didReceiveData:fromDeviceWithID:fromChannelWithUUID:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _initializeIfNeededAndGetSystemRemotePool]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager parentOutputDevice]
+ -[AVSystemRemotePoolOutputDeviceCommunicationChannelManager setParentOutputDevice:]
+ -[AVVolumeController dealloc]
+ -[AVVolumeController getMaximumVolumeLimitForBuiltInSpeaker:]
+ -[AVVolumeController initWithType:]
+ -[AVVolumeController setMaximumVolumeLimitForBuiltInSpeaker:]
+ -[AVVolumeController type]
+ -[CMAVRoutingTimeAsValue CMTimeValue]
+ -[CMAVRoutingTimeAsValue boolValue]
+ -[CMAVRoutingTimeAsValue charValue]
+ -[CMAVRoutingTimeAsValue classForCoder]
+ -[CMAVRoutingTimeAsValue copyWithZone:]
+ -[CMAVRoutingTimeAsValue description]
+ -[CMAVRoutingTimeAsValue doubleValue]
+ -[CMAVRoutingTimeAsValue encodeWithCoder:]
+ -[CMAVRoutingTimeAsValue floatValue]
+ -[CMAVRoutingTimeAsValue getValue:]
+ -[CMAVRoutingTimeAsValue hash]
+ -[CMAVRoutingTimeAsValue initWithCoder:]
+ -[CMAVRoutingTimeAsValue intValue]
+ -[CMAVRoutingTimeAsValue integerValue]
+ -[CMAVRoutingTimeAsValue isEqualToValue:]
+ -[CMAVRoutingTimeAsValue longLongValue]
+ -[CMAVRoutingTimeAsValue longValue]
+ -[CMAVRoutingTimeAsValue objCType]
+ -[CMAVRoutingTimeAsValue shortValue]
+ -[CMAVRoutingTimeAsValue unsignedCharValue]
+ -[CMAVRoutingTimeAsValue unsignedIntValue]
+ -[CMAVRoutingTimeAsValue unsignedIntegerValue]
+ -[CMAVRoutingTimeAsValue unsignedLongLongValue]
+ -[CMAVRoutingTimeAsValue unsignedLongValue]
+ -[CMAVRoutingTimeAsValue unsignedShortValue]
+ -[CMAVRoutingTimeMappingAsValue CMTimeMappingValue]
+ -[CMAVRoutingTimeMappingAsValue classForCoder]
+ -[CMAVRoutingTimeMappingAsValue copyWithZone:]
+ -[CMAVRoutingTimeMappingAsValue description]
+ -[CMAVRoutingTimeMappingAsValue encodeWithCoder:]
+ -[CMAVRoutingTimeMappingAsValue getValue:]
+ -[CMAVRoutingTimeMappingAsValue hash]
+ -[CMAVRoutingTimeMappingAsValue initWithCoder:]
+ -[CMAVRoutingTimeMappingAsValue isEqualToValue:]
+ -[CMAVRoutingTimeMappingAsValue objCType]
+ -[CMAVRoutingTimeRangeAsValue CMTimeRangeValue]
+ -[CMAVRoutingTimeRangeAsValue classForCoder]
+ -[CMAVRoutingTimeRangeAsValue copyWithZone:]
+ -[CMAVRoutingTimeRangeAsValue description]
+ -[CMAVRoutingTimeRangeAsValue encodeWithCoder:]
+ -[CMAVRoutingTimeRangeAsValue getValue:]
+ -[CMAVRoutingTimeRangeAsValue hash]
+ -[CMAVRoutingTimeRangeAsValue initWithCoder:]
+ -[CMAVRoutingTimeRangeAsValue isEqualToValue:]
+ -[CMAVRoutingTimeRangeAsValue objCType]
+ -[NSCoder(AVTimeCoding) decodeCMTimeForKey:]
+ -[NSCoder(AVTimeCoding) decodeCMTimeMappingForKey:]
+ -[NSCoder(AVTimeCoding) decodeCMTimeRangeForKey:]
+ -[NSCoder(AVTimeCoding) encodeCMTime:forKey:]
+ -[NSCoder(AVTimeCoding) encodeCMTimeMapping:forKey:]
+ -[NSCoder(AVTimeCoding) encodeCMTimeRange:forKey:]
+ -[NSValue(NSValueCMTimeExtensions) CMTimeMappingValue]
+ -[NSValue(NSValueCMTimeExtensions) CMTimeRangeValue]
+ -[NSValue(NSValueCMTimeExtensions) CMTimeValue]
+ -[NSValue(NSValueCMVideoDimensionsExtensions) CMVideoDimensionsValue]
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table123
+ GCC_except_table127
+ GCC_except_table131
+ GCC_except_table133
+ GCC_except_table14
+ GCC_except_table141
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table17
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table18
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table7
+ GCC_except_table74
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table95
+ GCC_except_table97
+ OBJC_IVAR_$_AVOutputDeviceScreenBorrowToken._client
+ OBJC_IVAR_$_AVOutputDeviceScreenBorrowToken._endpoint
+ OBJC_IVAR_$_AVOutputDeviceScreenBorrowToken._reason
+ OBJC_IVAR_$_AVOutputDeviceTurnByTurnToken._endpoint
+ _AVCommChannelDidClose
+ _AVCommChannelDidReceiveData
+ _AVCreateFigRouteDescriptorFromOutputDeviceDescription
+ _AVCreateRouteDiscovererWithType
+ _AVDefaultRoutingContextFactory
+ _AVDictionaryWithTime
+ _AVDictionaryWithTimeRange
+ _AVExecutionEnvironmentReleaseObject
+ _AVFigEndpointOutputDeviceImplCanSetEndpointVolumeDidChange
+ _AVFigEndpointOutputDeviceImplEndpointCanMuteDidChange
+ _AVFigEndpointOutputDeviceImplEndpointMutedDidChange
+ _AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange
+ _AVFigEndpointOutputDeviceImplEndpointVolumeControlTypeDidChange
+ _AVFigEndpointOutputDeviceImplEndpointVolumeDidChange
+ _AVFigEndpointOutputDeviceImplFigEndpointNotification
+ _AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImplHandleEvent
+ _AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImplSendDataCompletion
+ _AVFigEndpointUIAgentOutputContextManagerSharedEndpointUIAgentDidChangeNotification
+ _AVFigRouteDescriptorInputDeviceImplRouteDescriptionEvent
+ _AVFigRouteDescriptorOutputDeviceImplCanSetEndpointVolumeDidChange
+ _AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange
+ _AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange
+ _AVFigRouteDescriptorOutputDeviceImplEndpointRoomVolumeDidChange
+ _AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange
+ _AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange
+ _AVFigRouteDescriptorOutputDeviceImplRouteDescriptionEvent
+ _AVFigRouteDiscovererAvailableRoutesChanged
+ _AVFigRouteDiscovererEndpointDescriptorChanged
+ _AVFigRouteDiscovererFactoryCreateRouteDiscovererWithType
+ _AVFigRouteDiscovererFactoryGetCurrent
+ _AVFigRouteDiscovererFactoryReleaseObject
+ _AVFigRouteDiscovererFactorySetFactoryForQueue
+ _AVFigRouteDiscovererRoutePresentChanged
+ _AVFigRouteDiscovererRouteServerDied
+ _AVFigRouteDiscovererUpdateEndpointFeaturesCompletionCallback
+ _AVFigRoutingContextCurrentRouteChanged
+ _AVFigRoutingContextGroupConfigurationChanged
+ _AVFigRoutingContextModificationCallback
+ _AVFigRoutingContextOutputContextImplSetShowErrorPromptDictionaryToEcho
+ _AVFigRoutingContextPredictedSelectedRouteDescriptorChanged
+ _AVFigRoutingContextRemoteControlChannelAvailabilityChanged
+ _AVFigRoutingContextRouteChangeEnded
+ _AVFigRoutingContextRouteChangeStarted
+ _AVFigRoutingContextRouteConfigUpdated
+ _AVFigRoutingContextSendDataCompletion
+ _AVFigRoutingContextServerConnectionDied
+ _AVFigRoutingContextSystemAudioRouteConfigUpdated
+ _AVFigRoutingContextSystemPickerVideoRouteChanged
+ _AVFigVolumeControllerCanMuteDidChange
+ _AVFigVolumeControllerCanSetMasterVolumeDidChange
+ _AVFigVolumeControllerCanUseForRoutingContextDidChange
+ _AVFigVolumeControllerMasterVolumeControlTypeDidChange
+ _AVFigVolumeControllerMasterVolumeDidChange
+ _AVFigVolumeControllerMuteDidChange
+ _AVFoundationErrorDomain
+ _AVFullMethodName
+ _AVInputContextDestinationChangeInitiatedNotification
+ _AVInputContextDestinationChangeInitiatorKey
+ _AVInputContextDestinationChangeKey
+ _AVInputContextInputDeviceDidChangeNotification
+ _AVInputContextSetInputDeviceHostApplicationBundleIDKey
+ _AVInputContextSetInputDeviceInitiatorKey
+ _AVInputContextTypeSharedSystemAudioInput
+ _AVInputDeviceCopySharedRouteDiscovererForRouteDescriptor.gAVInputDeviceRouteDiscoverer_Once
+ _AVInputDeviceDiscoverySessionAvailableInputDevicesDidChangeNotification
+ _AVInputDeviceGetDeviceTypeAndSubTypeFromRouteDescriptor
+ _AVInputDeviceGetFigRouteDescriptor
+ _AVLocalizedError
+ _AVLocalizedErrorWithUnderlyingOSStatus
+ _AVLocalizedStringFromTable
+ _AVMakeAddEndpointOperation
+ _AVMakeAddRouteDescriptorOperation
+ _AVMakeRemoveEndpointOperation
+ _AVMakeRemoveRouteDescriptorOperation
+ _AVMakeSelectEndpointOperation
+ _AVMakeSelectEndpointsOperation
+ _AVMakeSelectRouteDescriptorOperation
+ _AVMakeSelectRouteDescriptorsOperation
+ _AVMediaTypeVideo
+ _AVMethodExceptionReasonWithObjectAndSelector
+ _AVOSStatusToNSError
+ _AVOutputContextAddOutputDeviceOptionAuthorizationToken
+ _AVOutputContextAddOutputDeviceOptionCancelIfAuthRequired
+ _AVOutputContextAddOutputDeviceOptionCorrelationID
+ _AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _AVOutputContextAddOutputDeviceOptionFadePlayback
+ _AVOutputContextAddOutputDeviceOptionInitiator
+ _AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished
+ _AVOutputContextCanMuteDidChangeNotification
+ _AVOutputContextCanSetVolumeDidChangeNotification
+ _AVOutputContextCommunicationChannelControlTypeDirect
+ _AVOutputContextCommunicationChannelControlTypeRelayed
+ _AVOutputContextCommunicationChannelOptionControlType
+ _AVOutputContextCreatePlatformDependentScreenOrVideoRoutingContext
+ _AVOutputContextDestinationChangeCancellationReasonAuthorizationSkipped
+ _AVOutputContextDestinationChangeCancellationReasonAuthorizationSkipped_block_invoke.notificationToken
+ _AVOutputContextDestinationChangeDeviceIDKey
+ _AVOutputContextDestinationChangeInitiatedNotification
+ _AVOutputContextDestinationChangeInitiatorKey
+ _AVOutputContextDestinationChangeKey
+ _AVOutputContextDestinationChangePreviousDeviceIDsKey
+ _AVOutputContextDestinationChangeReasonIdleDisconnect
+ _AVOutputContextDestinationChangeReasonKey
+ _AVOutputContextDeviceConnectionFailureReasonDeviceInUse
+ _AVOutputContextDeviceConnectionFailureReasonDeviceNotConnectedToInternet
+ _AVOutputContextDeviceConnectionFailureReasonDeviceNotMFiCertified
+ _AVOutputContextDeviceConnectionFailureReasonDeviceOutOfRange
+ _AVOutputContextDeviceConnectionFailureReasonInfraRelayFailed2GHzNetwork
+ _AVOutputContextDeviceConnectionFailureReasonInfraRelayFailedMultiDFSNetwork
+ _AVOutputContextDeviceConnectionFailureReasonNotAPeerInHomeGroup
+ _AVOutputContextDeviceGroupControlOptionCancelAddDeviceIfAuthRequired
+ _AVOutputContextGetDefaultDeviceTranslator
+ _AVOutputContextGlobalOutputDeviceConfigurationDidChangeNotification
+ _AVOutputContextIsSystemContextAllowed
+ _AVOutputContextIsSystemContextAllowed.cold.1
+ _AVOutputContextIsSystemContextAllowed.isAllowed
+ _AVOutputContextIsSystemContextAllowed.onceToken
+ _AVOutputContextManagerDidFailToConnectToOutputDeviceUserInfoKey
+ _AVOutputContextManagerFailureReasonKey
+ _AVOutputContextManagerOutputContextDidFailToConnectToOutputDeviceNotification
+ _AVOutputContextManagerOutputDeviceKey
+ _AVOutputContextManagerServerConnectionDied
+ _AVOutputContextManagerShowErrorPrompt
+ _AVOutputContextMutedDidChangeNotification
+ _AVOutputContextOutputDeviceDidChangeNotification
+ _AVOutputContextOutputDevicesDidChangeNotification
+ _AVOutputContextOutputDevicesModificationOptionCorrelationID
+ _AVOutputContextOutputDevicesModificationOptionUserInitiated
+ _AVOutputContextPredictedOutputDeviceDidChangeNotification
+ _AVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification
+ _AVOutputContextRemoveOutputDeviceOptionContinuePlayingAfterLastDeviceRemoved
+ _AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo
+ _AVOutputContextRemoveOutputDeviceOptionFadePlayback
+ _AVOutputContextRemoveOutputDeviceOptionInitiator
+ _AVOutputContextSendCommandCompletion
+ _AVOutputContextSetOutputDeviceCancelIfAuthRequiredKey
+ _AVOutputContextSetOutputDeviceDefaultAudioToLocalKey
+ _AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey
+ _AVOutputContextSetOutputDeviceFadePlaybackKey
+ _AVOutputContextSetOutputDeviceInitiatorKey
+ _AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey
+ _AVOutputContextSetOutputDevicePasswordKey
+ _AVOutputContextSetOutputDeviceSuppressUserInteractionOnSenderOnlyKey
+ _AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo
+ _AVOutputContextSetOutputDevicesOptionFadePlayback
+ _AVOutputContextSetOutputDevicesOptionInitiator
+ _AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished
+ _AVOutputContextTypeAudio
+ _AVOutputContextTypeGroupControl
+ _AVOutputContextTypeScreen
+ _AVOutputContextTypeSharedAudioPresentation
+ _AVOutputContextTypeSharedSystemAudio
+ _AVOutputContextTypeSharedSystemRemotePool
+ _AVOutputContextTypeSharedSystemScreen
+ _AVOutputContextTypeSystemRemoteDisplay
+ _AVOutputContextTypeVideo
+ _AVOutputContextUsesRouteConfigUpdatedNotification
+ _AVOutputContextUsesRoutingContextCallbacks
+ _AVOutputContextVolumeControlTypeDidChangeNotification
+ _AVOutputContextVolumeDidChangeNotification
+ _AVOutputDeviceAVFBluetoothAlternateTransportForFigAlternateTransport
+ _AVOutputDeviceAVFListeningModeForFigListeningMode
+ _AVOutputDeviceAVOutputDeviceIconsFromOEMIcons
+ _AVOutputDeviceAVOutputDeviceScreenInfoFromFigScreens
+ _AVOutputDeviceActivatedClusterMembersRoomIDKey
+ _AVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification
+ _AVOutputDeviceAuthenticationTypeFromFigAuthenticationType
+ _AVOutputDeviceAuthorizationRequestRetryReasonIncorrectAuthorizationToken
+ _AVOutputDeviceAuthorizationSessionShowAuthPrompt
+ _AVOutputDeviceAuthorizationSessionShowFinishedWithPrompt
+ _AVOutputDeviceAuthorizationTokenTypePIN
+ _AVOutputDeviceAuthorizationTokenTypePIN_block_invoke.notificationToken
+ _AVOutputDeviceAuthorizationTokenTypePassword
+ _AVOutputDeviceBatteryLevelCaseKey
+ _AVOutputDeviceBatteryLevelLeftKey
+ _AVOutputDeviceBatteryLevelRightKey
+ _AVOutputDeviceBluetoothAlternateTransportTypeDefault
+ _AVOutputDeviceBluetoothAlternateTransportTypeUSBC
+ _AVOutputDeviceBluetoothListeningModeActiveNoiseCancellation
+ _AVOutputDeviceBluetoothListeningModeAudioTransparency
+ _AVOutputDeviceBluetoothListeningModeAutomatic
+ _AVOutputDeviceBluetoothListeningModeNormal
+ _AVOutputDeviceCanMuteDidChangeNotification
+ _AVOutputDeviceCanSetVolumeDidChangeNotification
+ _AVOutputDeviceCarPlayTestNotification
+ _AVOutputDeviceCommunicationChannelControlTypeDirect
+ _AVOutputDeviceCommunicationChannelControlTypeRelayed
+ _AVOutputDeviceCommunicationChannelDataDestinationCarPlayClusterControl
+ _AVOutputDeviceCommunicationChannelDataDestinationCarPlayData
+ _AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataLogging
+ _AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataUpdate
+ _AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataVersionTwo
+ _AVOutputDeviceCommunicationChannelDataDestinationFitness
+ _AVOutputDeviceCommunicationChannelDataDestinationMediaRemote
+ _AVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped
+ _AVOutputDeviceCommunicationChannelOptionAwaitReply
+ _AVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired
+ _AVOutputDeviceCommunicationChannelOptionClientUUID
+ _AVOutputDeviceCommunicationChannelOptionControlType
+ _AVOutputDeviceCommunicationChannelOptionCorrelationID
+ _AVOutputDeviceCommunicationChannelOptionInitiator
+ _AVOutputDeviceCommunicationChannelOptionQualityOfService
+ _AVOutputDeviceCommunicationChannelOptionStreamPriority
+ _AVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate
+ _AVOutputDeviceConfigurationCancellationReasonAuthorizationSkipped
+ _AVOutputDeviceConfigurationOptionCancelConfigurationIfAuthRequired
+ _AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor
+ _AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor.cold.1
+ _AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor.gAVOutputDeviceRouteDiscoverer_Once
+ _AVOutputDeviceDescriptionsFromFigDescriptions
+ _AVOutputDeviceDiscoverySessionAvailableOutputDeviceGroupsDidChangeNotification
+ _AVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification
+ _AVOutputDeviceElectronicTollCollectionStateChangedNotification
+ _AVOutputDeviceElectronicTollCollectionStateFromVehicleInfo
+ _AVOutputDeviceEndpointSendCommandCompleted
+ _AVOutputDeviceFeatureEnhancedRequestCarUI
+ _AVOutputDeviceFigListeningModeForAVFListeningMode
+ _AVOutputDeviceGetCurrentScreenViewAreaFromEndpoint
+ _AVOutputDeviceGetDeviceTypeAndSubTypeFromRouteDescriptor
+ _AVOutputDeviceGetDisplayCornerMasksFromEndpoint
+ _AVOutputDeviceGetFigEndpoint
+ _AVOutputDeviceGetFigRouteDescriptor
+ _AVOutputDeviceGetSiriRequestedActionFromFigAction
+ _AVOutputDeviceGroupAddOutputDeviceOptionAuthorizationToken
+ _AVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequired
+ _AVOutputDeviceGroupAddOutputDeviceOptionInitiator
+ _AVOutputDeviceGroupMembershipChangeInitiatorKey
+ _AVOutputDeviceGroupMembershipChangeResultCancellationReasonAuthorizationSkipped
+ _AVOutputDeviceGroupOutputDevicesDidChangeNotification
+ _AVOutputDeviceGroupRemoveOutputDeviceOptionContinuePlayingAfterLastDeviceRemoved
+ _AVOutputDeviceGroupRemoveOutputDeviceOptionInitiator
+ _AVOutputDeviceGroupVolumeControlTypeDidChangeNotification
+ _AVOutputDeviceGroupVolumeDidChangeNotification
+ _AVOutputDeviceHeadTrackedSpatialAudioModeAlways
+ _AVOutputDeviceHeadTrackedSpatialAudioModeAutomatic
+ _AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode
+ _AVOutputDeviceHeadTrackedSpatialAudioModeMultichannelOnly
+ _AVOutputDeviceHeadTrackedSpatialAudioModeNever
+ _AVOutputDeviceImplCanMuteForEndpointID
+ _AVOutputDeviceImplChangeRoomVolumeForEndpoint
+ _AVOutputDeviceImplChangeVolumeByCount
+ _AVOutputDeviceImplIsMutedForEndpointID
+ _AVOutputDeviceImplSetMutedForEndpointID
+ _AVOutputDeviceIsAutoANCFeatureEnabled
+ _AVOutputDeviceIsConversationDetectionFeatureEnabled
+ _AVOutputDeviceIsInEarKey
+ _AVOutputDeviceLimitedUIChangedNotification
+ _AVOutputDeviceLimitedUIElementJapanMaps
+ _AVOutputDeviceLimitedUIElementMusicLists
+ _AVOutputDeviceLimitedUIElementNonMusicLists
+ _AVOutputDeviceLimitedUIElementSoftKeyboard
+ _AVOutputDeviceLimitedUIElementSoftPhoneKeypad
+ _AVOutputDeviceLocalDeviceDidChangeNotification
+ _AVOutputDeviceMFiCertificateSerialNumberChangedNotification
+ _AVOutputDeviceMakeAVOutputDeviceHIDsFromFigHIDs
+ _AVOutputDeviceMediaSessionStatusDidChangeNotification
+ _AVOutputDeviceMutedDidChangeNotification
+ _AVOutputDeviceNavigationAidedDrivingStateChangedNotification
+ _AVOutputDeviceNavigationAidedDrivingStateFromVehicleInfo
+ _AVOutputDeviceNightModeChangedNotification
+ _AVOutputDeviceNotificationFromFigNotification
+ _AVOutputDeviceNotificationFromFigNotification.cold.1
+ _AVOutputDeviceNotificationFromFigNotification.createFigToAVFNotificationMappingOnce
+ _AVOutputDeviceNotificationFromFigNotification.figToAVFNotificationMapping
+ _AVOutputDeviceOwnsTurnByTurnNavigationChangedNotification
+ _AVOutputDevicePerformHapticFeedback
+ _AVOutputDevicePerformanceReportPostedNotification
+ _AVOutputDeviceProposedGroupIDDidChangeNotification
+ _AVOutputDeviceRequestCarUIForEndpoint
+ _AVOutputDeviceRequestViewAreaForFigEndpoint
+ _AVOutputDeviceRouteDiscovererServerDeathNotificationCallback
+ _AVOutputDeviceScreenBecameAvailableNotification
+ _AVOutputDeviceScreenBecameUnavailableNotification
+ _AVOutputDeviceScreenInputCapabilityHighFidelityTouch
+ _AVOutputDeviceScreenInputCapabilityKnobs
+ _AVOutputDeviceScreenInputCapabilityLowFidelityTouch
+ _AVOutputDeviceScreenInputCapabilityTouchpad
+ _AVOutputDeviceSecondDisplayModeDefault
+ _AVOutputDeviceSecondDisplayModeMediaPresentation
+ _AVOutputDeviceSetAllowsHeadTrackedSpatialAudioOnEndpoint
+ _AVOutputDeviceSetAlternateSiriOnEndpoint
+ _AVOutputDeviceSetDisplayCornerMasksEndpoint
+ _AVOutputDeviceSetHeadTrackedSpatialAudioModeOnEndpoint
+ _AVOutputDeviceSetMediaRemoteDataOnEndpoint
+ _AVOutputDeviceSetSecondDisplayEnabledOnEndpoint
+ _AVOutputDeviceSetSecondDisplayModeOnEndpoint
+ _AVOutputDeviceSiriRequestedActionKey
+ _AVOutputDeviceSiriRequestedNotification
+ _AVOutputDeviceSiriRequestedTimestampKey
+ _AVOutputDeviceSubTypeFromFigSubType
+ _AVOutputDeviceSuggestUIWithURLSAndCompletionHandler
+ _AVOutputDeviceSupportedListeningModesForFigListeningModes
+ _AVOutputDeviceSupportsDataOverACLProtocolKey
+ _AVOutputDeviceTakeScreenForClient
+ _AVOutputDeviceTransportTypeFromFigTransportType
+ _AVOutputDeviceUnhandledRemoteEventCommandParametersKey
+ _AVOutputDeviceUnhandledRemoteEventCommandTypeKey
+ _AVOutputDeviceUnhandledRemoteEventNotification
+ _AVOutputDeviceVehicleHasMainAudioNotification
+ _AVOutputDeviceVehicleHasScreenForAirPlayVideoNotification
+ _AVOutputDeviceViewAreaInfoNSRectFromDictionary
+ _AVOutputDeviceVoiceTriggerModeChangedNotification
+ _AVOutputDeviceVolumeControlTypeDidChangeNotification
+ _AVOutputDeviceVolumeControlTypeFromFigType
+ _AVOutputDeviceVolumeDidChangeNotification
+ _AVOutputDeviceiOSEntityHasMainAudioNotification
+ _AVOutputDeviceiOSUIRequestedApplicationURLKey
+ _AVOutputDeviceiOSUIRequestedDisplayUUIDKey
+ _AVOutputDeviceiOSUIRequestedNotification
+ _AVPlatformIdentifierIOS
+ _AVPlatformIdentifierMacOS
+ _AVPlatformIdentifierTVOS
+ _AVPlatformIdentifierWatchOS
+ _AVPlatformIdentifierXROS
+ _AVRequestConcreteImplementation
+ _AVRequireConcreteObject
+ _AVRoutingContextRouteChangeOperationRouteChangeComplete
+ _AVRoutingContextRouteChangeOperationRouteChangeEnded
+ _AVRoutingContextRouteChangeOperationRouteChangeStarted
+ _AVRoutingPlaybackParticipantExternalPlaybackStatusDidChangeNotification
+ _AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperationRouteConfigUpdated
+ _AVRoutingScheduledParameterRampsIncludesRampThatOverlapsTimeRange
+ _AVRoutingScheduledParameterRampsIncludesRampThatOverlapsTimeRange.slopTime
+ _AVRoutingSessionManagerAllLikelyDestinationsDidChangeNotification
+ _AVRoutingSessionManagerCurrentSessionChanged
+ _AVRoutingSessionManagerCurrentSessionDidChangeNotification
+ _AVRoutingSessionManagerGetLikelyDestinationsFromFig
+ _AVRoutingSessionManagerInvokeStartHighConfidenceCompletionHandler
+ _AVRoutingSessionManagerLikelyDestinationsChanged
+ _AVRoutingSessionManagerLikelyExternalDestinationsDidChangeNotification
+ _AVRoutingSessionManagerStartHighConfidenceDestinationComplete
+ _AVRoutingWaitForNotificationOrDeallocationOperationNotificationHandler
+ _AVSendCommandCompletion
+ _AVStringForOSType
+ _AVSuccinctEndpointDescription
+ _AVSuccinctEndpointsDescription
+ _AVSuccinctRouteDescriptorDescription
+ _AVSuccinctRouteDescriptorsDescription
+ _AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel
+ _AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData
+ _AVSystemRemotePoolOutputDeviceCommunicationChannelSendDataCompletion
+ _CFArrayAppendValue
+ _CFArrayCreate
+ _CFArrayCreateMutable
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDataGetLength
+ _CFDictionaryAddValue
+ _CFDictionaryCreate
+ _CFDictionaryCreateMutable
+ _CFDictionaryCreateMutableCopy
+ _CFDictionaryGetValue
+ _CFDictionaryRemoveValue
+ _CFDictionarySetValue
+ _CFGetTypeID
+ _CFNumberCreate
+ _CFNumberGetValue
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyAppValue
+ _CFPreferencesCopyKeyList
+ _CFPreferencesGetAppBooleanValue
+ _CFPreferencesSetMultiple
+ _CFRelease
+ _CFRetain
+ _CGRectMakeWithDictionaryRepresentation
+ _CGRectZero
+ _CGSizeMakeWithDictionaryRepresentation
+ _CGSizeZero
+ _CMBaseObjectGetVTable
+ _CMBaseObjectIsMemberOfClass
+ _CMNotificationCenterAddListener
+ _CMNotificationCenterGetDefaultLocalCenter
+ _CMNotificationCenterRemoveListener
+ _CMTimeCompare
+ _CMTimeConvertScale
+ _CMTimeCopyAsDictionary
+ _CMTimeCopyDescription
+ _CMTimeGetSeconds
+ _CMTimeHash
+ _CMTimeMakeFromDictionary
+ _CMTimeMakeWithSeconds
+ _CMTimeRangeContainsTime
+ _CMTimeRangeCopyAsDictionary
+ _CMTimeRangeCopyDescription
+ _CMTimeRangeEqual
+ _CMTimeRangeGetEnd
+ _CMTimeRangeGetIntersection
+ _CMTimeRangeMake
+ _CMTimeRangeMakeFromDictionary
+ _CMTimeSubtract
+ _FigCFDictionaryCreateMutableCopy
+ _FigCFDictionaryGetBooleanIfPresent
+ _FigCFDictionaryGetFloatIfPresent
+ _FigCFDictionaryGetValue
+ _FigCFDictionarySetInt32
+ _FigCFDictionarySetInt64
+ _FigCFDictionarySetValue
+ _FigCFEqual
+ _FigCFNumberCreateSInt32
+ _FigCFNumberCreateUInt64
+ _FigDebugIsInternalBuild
+ _FigEndpointExtendedGetClassID
+ _FigEndpointGetCMBaseObject
+ _FigEndpointUIAgentXPCRemoteCreate
+ _FigGetCFPreferenceBooleanWithDefault
+ _FigGetUpTimeNanoseconds
+ _FigNote_AllowInternalDefaultLogs
+ _FigNotificationCenterAddListeners
+ _FigNotificationCenterAddWeakListener
+ _FigNotificationCenterRemoveListeners
+ _FigNotificationCenterRemoveWeakListener
+ _FigReadWriteLockCreate
+ _FigReadWriteLockDestroy
+ _FigReadWriteLockLockForRead
+ _FigReadWriteLockLockForWrite
+ _FigReadWriteLockUnlockForRead
+ _FigReadWriteLockUnlockForWrite
+ _FigReentrantMutexCreate
+ _FigReentrantMutexDestroy
+ _FigReentrantMutexTryLock
+ _FigReentrantMutexUnlock
+ _FigRemoteRoutingContextFactoryGetCurrent
+ _FigResilientRemoteRoutingContextFactoryGetCurrent
+ _FigRouteDiscovererXPCRemoteCreate
+ _FigRoutingSessionGetCMBaseObject
+ _FigRoutingSessionManagerGetConfidenceThresholds
+ _FigRoutingSessionManagerResilientRemoteCopyLongFormVideoManager
+ _FigSignalErrorAt3
+ _FigSimpleMutexCreate
+ _FigSimpleMutexDestroy
+ _FigSimpleMutexLock
+ _FigSimpleMutexUnlock
+ _FigVolumeControllerCopySharedControllerRemote
+ _NSClassFromString
+ _NSCocoaErrorDomain
+ _NSDebugDescriptionErrorKey
+ _NSDictionaryFromCMTime
+ _NSInternalInconsistencyException
+ _NSInvalidArgumentException
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _NSLocalizedRecoverySuggestionErrorKey
+ _NSLog
+ _NSOSStatusErrorDomain
+ _NSPOSIXErrorDomain
+ _NSShouldRetainWithZone
+ _NSStringFromClass
+ _NSStringFromSelector
+ _NSURLErrorDomain
+ _NSURLErrorKey
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_AVClusterComponentOutputDeviceDescription
+ _OBJC_CLASS_$_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ _OBJC_CLASS_$_AVExecutionEnvironment
+ _OBJC_CLASS_$_AVFigCommChannelUUIDCommunicationChannelManager
+ _OBJC_CLASS_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ _OBJC_CLASS_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ _OBJC_CLASS_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ _OBJC_CLASS_$_AVFigEndpointOutputDeviceImpl
+ _OBJC_CLASS_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ _OBJC_CLASS_$_AVFigEndpointSecondDisplayModeToken
+ _OBJC_CLASS_$_AVFigEndpointUIAgentOutputContextManagerImpl
+ _OBJC_CLASS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ _OBJC_CLASS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ _OBJC_CLASS_$_AVFigRemoteRouteDiscovererFactory
+ _OBJC_CLASS_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ _OBJC_CLASS_$_AVFigRouteDescriptorInputDeviceImpl
+ _OBJC_CLASS_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ _OBJC_CLASS_$_AVFigRouteDescriptorOutputDeviceImpl
+ _OBJC_CLASS_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ _OBJC_CLASS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ _OBJC_CLASS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ _OBJC_CLASS_$_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ _OBJC_CLASS_$_AVFigRoutingContextInputContextCompletionContext
+ _OBJC_CLASS_$_AVFigRoutingContextInputContextImpl
+ _OBJC_CLASS_$_AVFigRoutingContextOutputContextCompletionContext
+ _OBJC_CLASS_$_AVFigRoutingContextOutputContextImpl
+ _OBJC_CLASS_$_AVInputContext
+ _OBJC_CLASS_$_AVInputContextDestinationChange
+ _OBJC_CLASS_$_AVInputContextDestinationChangeInternal
+ _OBJC_CLASS_$_AVInputContextInternal
+ _OBJC_CLASS_$_AVInputDevice
+ _OBJC_CLASS_$_AVInputDeviceDiscoverySession
+ _OBJC_CLASS_$_AVInputDeviceDiscoverySessionInternal
+ _OBJC_CLASS_$_AVInputDeviceInternal
+ _OBJC_CLASS_$_AVLocalOutputDeviceImpl
+ _OBJC_CLASS_$_AVOutputContext
+ _OBJC_CLASS_$_AVOutputContextCommunicationChannel
+ _OBJC_CLASS_$_AVOutputContextCommunicationChannelInternal
+ _OBJC_CLASS_$_AVOutputContextDestinationChange
+ _OBJC_CLASS_$_AVOutputContextDestinationChangeInternal
+ _OBJC_CLASS_$_AVOutputContextFactory
+ _OBJC_CLASS_$_AVOutputContextInternal
+ _OBJC_CLASS_$_AVOutputContextManager
+ _OBJC_CLASS_$_AVOutputContextManagerInternal
+ _OBJC_CLASS_$_AVOutputContextModificationResult
+ _OBJC_CLASS_$_AVOutputDevice
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizationRequest
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizationRequestInternal
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizationSession
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizationSessionInternal
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizedPeer
+ _OBJC_CLASS_$_AVOutputDeviceAuthorizedPeerInternal
+ _OBJC_CLASS_$_AVOutputDeviceCommunicationChannel
+ _OBJC_CLASS_$_AVOutputDeviceDiscoverySession
+ _OBJC_CLASS_$_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ _OBJC_CLASS_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal
+ _OBJC_CLASS_$_AVOutputDeviceDiscoverySessionInternal
+ _OBJC_CLASS_$_AVOutputDeviceFrecencyManager
+ _OBJC_CLASS_$_AVOutputDeviceFrecentsReader
+ _OBJC_CLASS_$_AVOutputDeviceFrecentsWriter
+ _OBJC_CLASS_$_AVOutputDeviceGroup
+ _OBJC_CLASS_$_AVOutputDeviceGroupMembershipChangeResult
+ _OBJC_CLASS_$_AVOutputDeviceHID
+ _OBJC_CLASS_$_AVOutputDeviceIcon
+ _OBJC_CLASS_$_AVOutputDeviceInternal
+ _OBJC_CLASS_$_AVOutputDeviceLegacyFrecentsReader
+ _OBJC_CLASS_$_AVOutputDeviceLegacyFrecentsWriter
+ _OBJC_CLASS_$_AVOutputDeviceScreenBorrowToken
+ _OBJC_CLASS_$_AVOutputDeviceScreenInfo
+ _OBJC_CLASS_$_AVOutputDeviceTurnByTurnToken
+ _OBJC_CLASS_$_AVOutputDeviceViewAreaInfo
+ _OBJC_CLASS_$_AVPairedDevice
+ _OBJC_CLASS_$_AVPairedDeviceInternal
+ _OBJC_CLASS_$_AVRoutingAmbienceLevelRamp
+ _OBJC_CLASS_$_AVRoutingAmbienceLoudnessRamp
+ _OBJC_CLASS_$_AVRoutingBlockOperation
+ _OBJC_CLASS_$_AVRoutingCMNotificationDispatcher
+ _OBJC_CLASS_$_AVRoutingCMNotificationDispatcherListenerKey
+ _OBJC_CLASS_$_AVRoutingCallbackContextRegistry
+ _OBJC_CLASS_$_AVRoutingContextCommandOutputDeviceConfiguration
+ _OBJC_CLASS_$_AVRoutingContextCommandOutputDeviceConfigurationModification
+ _OBJC_CLASS_$_AVRoutingContextRouteChangeOperation
+ _OBJC_CLASS_$_AVRoutingContextSendConfigureDeviceCommandOperation
+ _OBJC_CLASS_$_AVRoutingDepartureAnnouncingObjectMonitor
+ _OBJC_CLASS_$_AVRoutingDialogLevelRamp
+ _OBJC_CLASS_$_AVRoutingDialogLoudnessRamp
+ _OBJC_CLASS_$_AVRoutingDialogMixBiasRamp
+ _OBJC_CLASS_$_AVRoutingDispatchOnce
+ _OBJC_CLASS_$_AVRoutingEventWaiter
+ _OBJC_CLASS_$_AVRoutingGlobalOperationQueue
+ _OBJC_CLASS_$_AVRoutingMutableScheduledAudioParameters
+ _OBJC_CLASS_$_AVRoutingOperation
+ _OBJC_CLASS_$_AVRoutingOperationQueueWithFundamentalDependency
+ _OBJC_CLASS_$_AVRoutingPlaybackArbiter
+ _OBJC_CLASS_$_AVRoutingRecordingLoudnessRamp
+ _OBJC_CLASS_$_AVRoutingRenderingStyleRamp
+ _OBJC_CLASS_$_AVRoutingRetainReleaseWeakReference
+ _OBJC_CLASS_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ _OBJC_CLASS_$_AVRoutingScheduledAudioParameters
+ _OBJC_CLASS_$_AVRoutingScheduledAudioParametersInternal
+ _OBJC_CLASS_$_AVRoutingScheduledFloatValueRamp
+ _OBJC_CLASS_$_AVRoutingScheduledParameterRamp
+ _OBJC_CLASS_$_AVRoutingScheduledVolumeRamp
+ _OBJC_CLASS_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ _OBJC_CLASS_$_AVRoutingSession
+ _OBJC_CLASS_$_AVRoutingSessionDestination
+ _OBJC_CLASS_$_AVRoutingSessionDestinationInternal
+ _OBJC_CLASS_$_AVRoutingSessionInternal
+ _OBJC_CLASS_$_AVRoutingSessionManager
+ _OBJC_CLASS_$_AVRoutingSessionManagerInternal
+ _OBJC_CLASS_$_AVRoutingSynchronousBlockScheduler
+ _OBJC_CLASS_$_AVRoutingWaitForNotificationOrDeallocationOperation
+ _OBJC_CLASS_$_AVRoutingWeakReference
+ _OBJC_CLASS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ _OBJC_CLASS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ _OBJC_CLASS_$_AVVolumeController
+ _OBJC_CLASS_$_CMAVRoutingTimeAsValue
+ _OBJC_CLASS_$_CMAVRoutingTimeMappingAsValue
+ _OBJC_CLASS_$_CMAVRoutingTimeRangeAsValue
+ _OBJC_CLASS_$_NSCoder
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNotification
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSOperation
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSOrderedCollectionDifference
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_UTType
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._deviceID
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._deviceName
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._deviceSubType
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._deviceType
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._isClusterLeader
+ _OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._modelID
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._communicationChannelsForUUIDs
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._ivarAccessQueue
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._outgoingCommChannelUUID
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._parentOutputContextImpl
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._routingContext
+ _OBJC_IVAR_$_AVFigCommChannelUUIDCommunicationChannelManager._weakObserver
+ _OBJC_IVAR_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl._commChannelUUID
+ _OBJC_IVAR_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl._parentChannel
+ _OBJC_IVAR_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl._routingContext
+ _OBJC_IVAR_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator._useRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl._figEndpoints
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._delegate
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._figEndpoint
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._implSupportEventListener
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._routingContextFactory
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._useRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._volumeController
+ _OBJC_IVAR_$_AVFigEndpointOutputDeviceImpl._weakObserver
+ _OBJC_IVAR_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl._parentChannel
+ _OBJC_IVAR_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl._remoteControlSession
+ _OBJC_IVAR_$_AVFigEndpointSecondDisplayModeToken._endpoint
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputContextManagerImpl._agent
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputContextManagerImpl._parentManager
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputContextManagerImpl._weakObserver
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl._completionHandler
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl._outputDevice
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl._parentSession
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl._tokenType
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl._uniqueID
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl._agent
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl._currentRequest
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl._currentRequestImpl
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl._parentSession
+ _OBJC_IVAR_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator._useRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator._useRoutingContextCallbacks
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._implSupportEventListener
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._routeDescriptionRWLock
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._routeDescriptor
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._routeDiscoverer
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._routingContext
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._routingContextFactory
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._useRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigRouteDescriptorInputDeviceImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl._routeDescriptors
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl._routeDiscoverer
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._delegate
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._implSupportEventListener
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._routeDescriptionRWLock
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._routeDescriptor
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._routeDiscoverer
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._routingContext
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._routingContextFactory
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._useRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._volumeController
+ _OBJC_IVAR_$_AVFigRouteDescriptorOutputDeviceImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl._discoverer
+ _OBJC_IVAR_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl._parentSession
+ _OBJC_IVAR_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl._routeDiscovererCreator
+ _OBJC_IVAR_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory._routeDiscovererFactory
+ _OBJC_IVAR_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl._discoverer
+ _OBJC_IVAR_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl._parentSession
+ _OBJC_IVAR_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl._routeDiscovererCreator
+ _OBJC_IVAR_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext._completionHandler
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextCompletionContext._completionHandler
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._destinationChangesForRouteChangeIDs
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._ivarAccessQueue
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._parentContext
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._parentInputContext
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._routingContext
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._routingContextCreator
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._usesRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigRoutingContextInputContextImpl._weakObserver
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextCompletionContext._completionHandler
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextCompletionContext._devicesType
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextCompletionContext.mFigRoutingContext
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._commChannelManager
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._commChannelManagerCreator
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._destinationChangesForRouteChangeIDs
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._deviceTranslator
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._ivarAccessQueue
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._parentContext
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._routingContext
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._routingContextCreator
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._usesRouteConfigUpdatedNotification
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._volumeController
+ _OBJC_IVAR_$_AVFigRoutingContextOutputContextImpl._weakObserver
+ _OBJC_IVAR_$_AVInputContext._inputContext
+ _OBJC_IVAR_$_AVInputContextDestinationChange._ivars
+ _OBJC_IVAR_$_AVInputContextDestinationChangeInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVInputContextDestinationChangeInternal.status
+ _OBJC_IVAR_$_AVInputContextInternal.applicationPID
+ _OBJC_IVAR_$_AVInputContextInternal.applicationPIDWasSet
+ _OBJC_IVAR_$_AVInputContextInternal.impl
+ _OBJC_IVAR_$_AVInputContextInternal.inputDeviceFeatures
+ _OBJC_IVAR_$_AVInputContextInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVInputDevice._inputDevice
+ _OBJC_IVAR_$_AVInputDeviceDiscoverySession._discoveryMode
+ _OBJC_IVAR_$_AVInputDeviceDiscoverySession._inputDeviceDiscoverySession
+ _OBJC_IVAR_$_AVInputDeviceDiscoverySessionInternal.discoveryMode
+ _OBJC_IVAR_$_AVInputDeviceDiscoverySessionInternal.impl
+ _OBJC_IVAR_$_AVInputDeviceDiscoverySessionInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVInputDeviceInternal.ID
+ _OBJC_IVAR_$_AVInputDeviceInternal.deviceSubType
+ _OBJC_IVAR_$_AVInputDeviceInternal.deviceType
+ _OBJC_IVAR_$_AVInputDeviceInternal.impl
+ _OBJC_IVAR_$_AVInputDeviceInternal.manufacturer
+ _OBJC_IVAR_$_AVInputDeviceInternal.modelID
+ _OBJC_IVAR_$_AVInputDeviceInternal.name
+ _OBJC_IVAR_$_AVLocalOutputDeviceImpl._implSupportEventListener
+ _OBJC_IVAR_$_AVLocalOutputDeviceImpl.alternateTransportType
+ _OBJC_IVAR_$_AVOutputContext._outputContext
+ _OBJC_IVAR_$_AVOutputContextCommunicationChannel._ivars
+ _OBJC_IVAR_$_AVOutputContextCommunicationChannelInternal.impl
+ _OBJC_IVAR_$_AVOutputContextDestinationChange._ivars
+ _OBJC_IVAR_$_AVOutputContextDestinationChangeInternal.cancellationReason
+ _OBJC_IVAR_$_AVOutputContextDestinationChangeInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputContextDestinationChangeInternal.status
+ _OBJC_IVAR_$_AVOutputContextFactory._weakContextLock
+ _OBJC_IVAR_$_AVOutputContextFactory._weakContexts
+ _OBJC_IVAR_$_AVOutputContextInternal.applicationPID
+ _OBJC_IVAR_$_AVOutputContextInternal.applicationPIDWasSet
+ _OBJC_IVAR_$_AVOutputContextInternal.communicationChannelDelegate
+ _OBJC_IVAR_$_AVOutputContextInternal.impl
+ _OBJC_IVAR_$_AVOutputContextInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputContextInternal.outputDeviceFeatures
+ _OBJC_IVAR_$_AVOutputContextManager._ivars
+ _OBJC_IVAR_$_AVOutputContextManagerInternal.impl
+ _OBJC_IVAR_$_AVOutputContextManagerInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputContextModificationResult._modificationMetrics
+ _OBJC_IVAR_$_AVOutputContextModificationResult.mCancellationReason
+ _OBJC_IVAR_$_AVOutputContextModificationResult.mStatus
+ _OBJC_IVAR_$_AVOutputDevice._outputDevice
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationRequest._ivars
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationRequestInternal.error
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationRequestInternal.impl
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationRequestInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationRequestInternal.status
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationSession._ivars
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationSessionInternal.delegate
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationSessionInternal.impl
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizationSessionInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizedPeer._ivars
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizedPeerInternal.ID
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizedPeerInternal.isAdmin
+ _OBJC_IVAR_$_AVOutputDeviceAuthorizedPeerInternal.publicKey
+ _OBJC_IVAR_$_AVOutputDeviceCommunicationChannel._delegate
+ _OBJC_IVAR_$_AVOutputDeviceCommunicationChannel._impl
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySession._outputDeviceDiscoverySession
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionAvailableOutputDevices._availableOutputDevices
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal._otherDevices
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal._recentlyUsedDevices
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal.impl
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionInternal.cachedDiscoveryEnabled
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionInternal.discoveryMode
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionInternal.impl
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionInternal.ivarAccessQueue
+ _OBJC_IVAR_$_AVOutputDeviceDiscoverySessionInternal.onlyDiscoversBluetoothDevices
+ _OBJC_IVAR_$_AVOutputDeviceFrecentsReader._frecents
+ _OBJC_IVAR_$_AVOutputDeviceFrecentsWriter._frecents
+ _OBJC_IVAR_$_AVOutputDeviceFrecentsWriter._frecentsFilePath
+ _OBJC_IVAR_$_AVOutputDeviceGroup._impl
+ _OBJC_IVAR_$_AVOutputDeviceGroupMembershipChangeResult._cancellationReason
+ _OBJC_IVAR_$_AVOutputDeviceGroupMembershipChangeResult._status
+ _OBJC_IVAR_$_AVOutputDeviceHID._UUID
+ _OBJC_IVAR_$_AVOutputDeviceHID._endpoint
+ _OBJC_IVAR_$_AVOutputDeviceHID._inputMode
+ _OBJC_IVAR_$_AVOutputDeviceHID._screenID
+ _OBJC_IVAR_$_AVOutputDeviceIcon._imageData
+ _OBJC_IVAR_$_AVOutputDeviceIcon._pixelSize
+ _OBJC_IVAR_$_AVOutputDeviceIcon._prerendered
+ _OBJC_IVAR_$_AVOutputDeviceInternal.ID
+ _OBJC_IVAR_$_AVOutputDeviceInternal.MACAddress
+ _OBJC_IVAR_$_AVOutputDeviceInternal.commChannelManager
+ _OBJC_IVAR_$_AVOutputDeviceInternal.communicationChannelDelegate
+ _OBJC_IVAR_$_AVOutputDeviceInternal.deviceFeatures
+ _OBJC_IVAR_$_AVOutputDeviceInternal.deviceSubType
+ _OBJC_IVAR_$_AVOutputDeviceInternal.deviceType
+ _OBJC_IVAR_$_AVOutputDeviceInternal.firmwareVersion
+ _OBJC_IVAR_$_AVOutputDeviceInternal.impl
+ _OBJC_IVAR_$_AVOutputDeviceInternal.manufacturer
+ _OBJC_IVAR_$_AVOutputDeviceInternal.modelID
+ _OBJC_IVAR_$_AVOutputDeviceInternal.name
+ _OBJC_IVAR_$_AVOutputDeviceInternal.serialNumber
+ _OBJC_IVAR_$_AVOutputDeviceLegacyFrecentsWriter._keysToRemove
+ _OBJC_IVAR_$_AVOutputDeviceLegacyFrecentsWriter._updatedFrecentsList
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._ID
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._applicationURL
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._cornerMasks
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._initialApplicationURL
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._inputCapabilities
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._limitedUI
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._limitedUIElements
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._maxFPS
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._nightMode
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._physicalSize
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._pixelSize
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._primaryInputDevice
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._squarePixelSize
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._viewAreas
+ _OBJC_IVAR_$_AVOutputDeviceScreenInfo._viewHeightScaleFactor
+ _OBJC_IVAR_$_AVOutputDeviceViewAreaInfo._safeArea
+ _OBJC_IVAR_$_AVOutputDeviceViewAreaInfo._statusBarEdge
+ _OBJC_IVAR_$_AVOutputDeviceViewAreaInfo._supportsFocusTransfer
+ _OBJC_IVAR_$_AVOutputDeviceViewAreaInfo._transitionControl
+ _OBJC_IVAR_$_AVOutputDeviceViewAreaInfo._viewArea
+ _OBJC_IVAR_$_AVPairedDevice._ivars
+ _OBJC_IVAR_$_AVPairedDeviceInternal.ID
+ _OBJC_IVAR_$_AVPairedDeviceInternal.modelID
+ _OBJC_IVAR_$_AVPairedDeviceInternal.name
+ _OBJC_IVAR_$_AVPairedDeviceInternal.playing
+ _OBJC_IVAR_$_AVPairedDeviceInternal.productName
+ _OBJC_IVAR_$_AVRoutingBlockOperation._block
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcher._cmNotificationCenter
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcher._listenerObjectsQueue
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcher._observersForListenerKeys
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcherListenerKey._callback
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcherListenerKey._name
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcherListenerKey._object
+ _OBJC_IVAR_$_AVRoutingCMNotificationDispatcherListenerKey._weakReferenceToListener
+ _OBJC_IVAR_$_AVRoutingCallbackContextRegistry._contextsForTokens
+ _OBJC_IVAR_$_AVRoutingCallbackContextRegistry._currentToken
+ _OBJC_IVAR_$_AVRoutingCallbackContextRegistry._readWriteQueue
+ _OBJC_IVAR_$_AVRoutingContextCommandOutputDeviceConfiguration._response
+ _OBJC_IVAR_$_AVRoutingContextCommandOutputDeviceConfigurationModification._payload
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._actOnRouteChangeNotifications
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._inputRoutePicked
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._notificationManagementQueue
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._result
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._resultInput
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._routeChangeBlock
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._routeChangeID
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._routingContext
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._successNotification
+ _OBJC_IVAR_$_AVRoutingContextRouteChangeOperation._weakObserver
+ _OBJC_IVAR_$_AVRoutingContextSendConfigureDeviceCommandOperation._configuratorBlock
+ _OBJC_IVAR_$_AVRoutingContextSendConfigureDeviceCommandOperation._finalConfiguration
+ _OBJC_IVAR_$_AVRoutingContextSendConfigureDeviceCommandOperation._routingContext
+ _OBJC_IVAR_$_AVRoutingDepartureAnnouncingObjectMonitor._weakReferenceToMonitoringObject
+ _OBJC_IVAR_$_AVRoutingDispatchOnce._lock
+ _OBJC_IVAR_$_AVRoutingDispatchOnce._testFlag
+ _OBJC_IVAR_$_AVRoutingEventWaiter._condition
+ _OBJC_IVAR_$_AVRoutingEventWaiter._eventCompleted
+ _OBJC_IVAR_$_AVRoutingGlobalOperationQueue._operationQueue
+ _OBJC_IVAR_$_AVRoutingMutableScheduledAudioParameters._mutableScheduledParametersInternal
+ _OBJC_IVAR_$_AVRoutingOperation._error
+ _OBJC_IVAR_$_AVRoutingOperation._ivarAccessQueue
+ _OBJC_IVAR_$_AVRoutingOperation._status
+ _OBJC_IVAR_$_AVRoutingOperationQueueWithFundamentalDependency._fundamentalOperation
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._allTrackedParticipants
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._dispatchQueue
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._externalPlaybackStatusChangedNotificationToken
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._ivarAccessQueue
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._weakReferenceToPreferredParticipantForExternalPlayback
+ _OBJC_IVAR_$_AVRoutingPlaybackArbiter._weakReferenceToPreferredParticipantForNonMixableAudio
+ _OBJC_IVAR_$_AVRoutingRetainReleaseWeakReference._cachedReferencedObjectDescription
+ _OBJC_IVAR_$_AVRoutingRetainReleaseWeakReference._weakStorage
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._inputRoutePicked
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._result
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._resultInput
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._routeChangeBlock
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._routeChangeID
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._routeChangeIvarAccessQueue
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._routingContext
+ _OBJC_IVAR_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation._weakObserver
+ _OBJC_IVAR_$_AVRoutingScheduledAudioParameters._scheduledParametersInternal
+ _OBJC_IVAR_$_AVRoutingScheduledAudioParametersInternal.parameterRamps
+ _OBJC_IVAR_$_AVRoutingScheduledFloatValueRamp._endValue
+ _OBJC_IVAR_$_AVRoutingScheduledFloatValueRamp._startValue
+ _OBJC_IVAR_$_AVRoutingScheduledParameterRamp._timeRange
+ _OBJC_IVAR_$_AVRoutingScheduledVolumeRamp._rampMode
+ _OBJC_IVAR_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler._blockSerializationLock
+ _OBJC_IVAR_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler._blocks
+ _OBJC_IVAR_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler._ivarAccessLock
+ _OBJC_IVAR_$_AVRoutingSession._ivars
+ _OBJC_IVAR_$_AVRoutingSessionDestination._ivars
+ _OBJC_IVAR_$_AVRoutingSessionDestinationInternal.figDestination
+ _OBJC_IVAR_$_AVRoutingSessionInternal.figRoutingSession
+ _OBJC_IVAR_$_AVRoutingSessionManager._ivars
+ _OBJC_IVAR_$_AVRoutingSessionManagerInternal.figRoutingSessionManager
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._finished
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._monitoringIsFinishedSemaphore
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._notificationNames
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._operationStateSerializationQueue
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._registeredForObjectNotifications
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._started
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._weakReferenceToMonitoredObject
+ _OBJC_IVAR_$_AVRoutingWaitForNotificationOrDeallocationOperation._weakReferenceToSelf
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl._commChannelUUID
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl._deviceID
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl._outputContext
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl._parentChannel
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager._communicationChannelsForUUIDs
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager._deviceID
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager._ivarAccessQueue
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager._outputContext
+ _OBJC_IVAR_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager._parentOutputDevice
+ _OBJC_IVAR_$_AVVolumeController._type
+ _OBJC_IVAR_$_CMAVRoutingTimeAsValue._time
+ _OBJC_IVAR_$_CMAVRoutingTimeMappingAsValue._timeMapping
+ _OBJC_IVAR_$_CMAVRoutingTimeRangeAsValue._timeRange
+ _OBJC_METACLASS_$_AVClusterComponentOutputDeviceDescription
+ _OBJC_METACLASS_$_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ _OBJC_METACLASS_$_AVExecutionEnvironment
+ _OBJC_METACLASS_$_AVFigCommChannelUUIDCommunicationChannelManager
+ _OBJC_METACLASS_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ _OBJC_METACLASS_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ _OBJC_METACLASS_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ _OBJC_METACLASS_$_AVFigEndpointOutputDeviceImpl
+ _OBJC_METACLASS_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ _OBJC_METACLASS_$_AVFigEndpointSecondDisplayModeToken
+ _OBJC_METACLASS_$_AVFigEndpointUIAgentOutputContextManagerImpl
+ _OBJC_METACLASS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ _OBJC_METACLASS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ _OBJC_METACLASS_$_AVFigRemoteRouteDiscovererFactory
+ _OBJC_METACLASS_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ _OBJC_METACLASS_$_AVFigRouteDescriptorInputDeviceImpl
+ _OBJC_METACLASS_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ _OBJC_METACLASS_$_AVFigRouteDescriptorOutputDeviceImpl
+ _OBJC_METACLASS_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ _OBJC_METACLASS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ _OBJC_METACLASS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ _OBJC_METACLASS_$_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ _OBJC_METACLASS_$_AVFigRoutingContextInputContextCompletionContext
+ _OBJC_METACLASS_$_AVFigRoutingContextInputContextImpl
+ _OBJC_METACLASS_$_AVFigRoutingContextOutputContextCompletionContext
+ _OBJC_METACLASS_$_AVFigRoutingContextOutputContextImpl
+ _OBJC_METACLASS_$_AVInputContext
+ _OBJC_METACLASS_$_AVInputContextDestinationChange
+ _OBJC_METACLASS_$_AVInputContextDestinationChangeInternal
+ _OBJC_METACLASS_$_AVInputContextInternal
+ _OBJC_METACLASS_$_AVInputDevice
+ _OBJC_METACLASS_$_AVInputDeviceDiscoverySession
+ _OBJC_METACLASS_$_AVInputDeviceDiscoverySessionInternal
+ _OBJC_METACLASS_$_AVInputDeviceInternal
+ _OBJC_METACLASS_$_AVLocalOutputDeviceImpl
+ _OBJC_METACLASS_$_AVOutputContext
+ _OBJC_METACLASS_$_AVOutputContextCommunicationChannel
+ _OBJC_METACLASS_$_AVOutputContextCommunicationChannelInternal
+ _OBJC_METACLASS_$_AVOutputContextDestinationChange
+ _OBJC_METACLASS_$_AVOutputContextDestinationChangeInternal
+ _OBJC_METACLASS_$_AVOutputContextFactory
+ _OBJC_METACLASS_$_AVOutputContextInternal
+ _OBJC_METACLASS_$_AVOutputContextManager
+ _OBJC_METACLASS_$_AVOutputContextManagerInternal
+ _OBJC_METACLASS_$_AVOutputContextModificationResult
+ _OBJC_METACLASS_$_AVOutputDevice
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizationRequest
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizationRequestInternal
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizationSession
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizationSessionInternal
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizedPeer
+ _OBJC_METACLASS_$_AVOutputDeviceAuthorizedPeerInternal
+ _OBJC_METACLASS_$_AVOutputDeviceCommunicationChannel
+ _OBJC_METACLASS_$_AVOutputDeviceDiscoverySession
+ _OBJC_METACLASS_$_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ _OBJC_METACLASS_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal
+ _OBJC_METACLASS_$_AVOutputDeviceDiscoverySessionInternal
+ _OBJC_METACLASS_$_AVOutputDeviceFrecencyManager
+ _OBJC_METACLASS_$_AVOutputDeviceFrecentsReader
+ _OBJC_METACLASS_$_AVOutputDeviceFrecentsWriter
+ _OBJC_METACLASS_$_AVOutputDeviceGroup
+ _OBJC_METACLASS_$_AVOutputDeviceGroupMembershipChangeResult
+ _OBJC_METACLASS_$_AVOutputDeviceHID
+ _OBJC_METACLASS_$_AVOutputDeviceIcon
+ _OBJC_METACLASS_$_AVOutputDeviceInternal
+ _OBJC_METACLASS_$_AVOutputDeviceLegacyFrecentsReader
+ _OBJC_METACLASS_$_AVOutputDeviceLegacyFrecentsWriter
+ _OBJC_METACLASS_$_AVOutputDeviceScreenBorrowToken
+ _OBJC_METACLASS_$_AVOutputDeviceScreenInfo
+ _OBJC_METACLASS_$_AVOutputDeviceTurnByTurnToken
+ _OBJC_METACLASS_$_AVOutputDeviceViewAreaInfo
+ _OBJC_METACLASS_$_AVPairedDevice
+ _OBJC_METACLASS_$_AVPairedDeviceInternal
+ _OBJC_METACLASS_$_AVRoutingAmbienceLevelRamp
+ _OBJC_METACLASS_$_AVRoutingAmbienceLoudnessRamp
+ _OBJC_METACLASS_$_AVRoutingBlockOperation
+ _OBJC_METACLASS_$_AVRoutingCMNotificationDispatcher
+ _OBJC_METACLASS_$_AVRoutingCMNotificationDispatcherListenerKey
+ _OBJC_METACLASS_$_AVRoutingCallbackContextRegistry
+ _OBJC_METACLASS_$_AVRoutingContextCommandOutputDeviceConfiguration
+ _OBJC_METACLASS_$_AVRoutingContextCommandOutputDeviceConfigurationModification
+ _OBJC_METACLASS_$_AVRoutingContextRouteChangeOperation
+ _OBJC_METACLASS_$_AVRoutingContextSendConfigureDeviceCommandOperation
+ _OBJC_METACLASS_$_AVRoutingDepartureAnnouncingObjectMonitor
+ _OBJC_METACLASS_$_AVRoutingDialogLevelRamp
+ _OBJC_METACLASS_$_AVRoutingDialogLoudnessRamp
+ _OBJC_METACLASS_$_AVRoutingDialogMixBiasRamp
+ _OBJC_METACLASS_$_AVRoutingDispatchOnce
+ _OBJC_METACLASS_$_AVRoutingEventWaiter
+ _OBJC_METACLASS_$_AVRoutingGlobalOperationQueue
+ _OBJC_METACLASS_$_AVRoutingMutableScheduledAudioParameters
+ _OBJC_METACLASS_$_AVRoutingOperation
+ _OBJC_METACLASS_$_AVRoutingOperationQueueWithFundamentalDependency
+ _OBJC_METACLASS_$_AVRoutingPlaybackArbiter
+ _OBJC_METACLASS_$_AVRoutingRecordingLoudnessRamp
+ _OBJC_METACLASS_$_AVRoutingRenderingStyleRamp
+ _OBJC_METACLASS_$_AVRoutingRetainReleaseWeakReference
+ _OBJC_METACLASS_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ _OBJC_METACLASS_$_AVRoutingScheduledAudioParameters
+ _OBJC_METACLASS_$_AVRoutingScheduledAudioParametersInternal
+ _OBJC_METACLASS_$_AVRoutingScheduledFloatValueRamp
+ _OBJC_METACLASS_$_AVRoutingScheduledParameterRamp
+ _OBJC_METACLASS_$_AVRoutingScheduledVolumeRamp
+ _OBJC_METACLASS_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ _OBJC_METACLASS_$_AVRoutingSession
+ _OBJC_METACLASS_$_AVRoutingSessionDestination
+ _OBJC_METACLASS_$_AVRoutingSessionDestinationInternal
+ _OBJC_METACLASS_$_AVRoutingSessionInternal
+ _OBJC_METACLASS_$_AVRoutingSessionManager
+ _OBJC_METACLASS_$_AVRoutingSessionManagerInternal
+ _OBJC_METACLASS_$_AVRoutingSynchronousBlockScheduler
+ _OBJC_METACLASS_$_AVRoutingWaitForNotificationOrDeallocationOperation
+ _OBJC_METACLASS_$_AVRoutingWeakReference
+ _OBJC_METACLASS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ _OBJC_METACLASS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ _OBJC_METACLASS_$_AVVolumeController
+ _OBJC_METACLASS_$_CMAVRoutingTimeAsValue
+ _OBJC_METACLASS_$_CMAVRoutingTimeMappingAsValue
+ _OBJC_METACLASS_$_CMAVRoutingTimeRangeAsValue
+ _OBJC_METACLASS_$_NSOperation
+ _OBJC_METACLASS_$_NSOperationQueue
+ _OBJC_METACLASS_$_NSValue
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
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _TEMP_kFigEndpointCentralNotification_CarEntityHasScreenForAirPlayVideo
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_AVTimeCoding
+ __OBJC_$_CATEGORY_NSCoder_$_AVTimeCoding
+ __OBJC_$_CATEGORY_NSValue_$_NSValueCMVideoDimensionsExtensions
+ __OBJC_$_CLASS_METHODS_AVExecutionEnvironment
+ __OBJC_$_CLASS_METHODS_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_CLASS_METHODS_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_$_CLASS_METHODS_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_CLASS_METHODS_AVFigRoutingContextInputContextImpl
+ __OBJC_$_CLASS_METHODS_AVFigRoutingContextOutputContextImpl
+ __OBJC_$_CLASS_METHODS_AVInputContext
+ __OBJC_$_CLASS_METHODS_AVInputDevice(FigRouteDescriptor)
+ __OBJC_$_CLASS_METHODS_AVInputDeviceDiscoverySession
+ __OBJC_$_CLASS_METHODS_AVOutputContext(AVAudioSession|FigRoutingContext)
+ __OBJC_$_CLASS_METHODS_AVOutputContextFactory
+ __OBJC_$_CLASS_METHODS_AVOutputContextManager
+ __OBJC_$_CLASS_METHODS_AVOutputDevice(AVOutputDeviceFigEndpointImplFetching|FigRouteDescriptor)
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceAuthorizationSession(FigEndpointUIAgent)
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceDiscoverySession
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceDiscoverySessionAvailableOutputDevices(AVOutputDeviceDiscoverySessionAvailableOutputDevices_FigEndpointImpl)
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceFrecencyManager
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceGroup
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_$_CLASS_METHODS_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_$_CLASS_METHODS_AVPairedDevice
+ __OBJC_$_CLASS_METHODS_AVRoutingAmbienceLevelRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingAmbienceLoudnessRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingCMNotificationDispatcher
+ __OBJC_$_CLASS_METHODS_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_$_CLASS_METHODS_AVRoutingCallbackContextRegistry
+ __OBJC_$_CLASS_METHODS_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_$_CLASS_METHODS_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_$_CLASS_METHODS_AVRoutingContextRouteChangeOperation
+ __OBJC_$_CLASS_METHODS_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_$_CLASS_METHODS_AVRoutingDepartureAnnouncingObjectMonitor
+ __OBJC_$_CLASS_METHODS_AVRoutingDialogLevelRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingDialogLoudnessRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingDialogMixBiasRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingGlobalOperationQueue
+ __OBJC_$_CLASS_METHODS_AVRoutingMutableScheduledAudioParameters
+ __OBJC_$_CLASS_METHODS_AVRoutingOperation(ArrayOfOperations)
+ __OBJC_$_CLASS_METHODS_AVRoutingPlaybackArbiter
+ __OBJC_$_CLASS_METHODS_AVRoutingRecordingLoudnessRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingRenderingStyleRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_$_CLASS_METHODS_AVRoutingScheduledFloatValueRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingScheduledParameterRamp(AVRoutingScheduledParameterRampSerialization)
+ __OBJC_$_CLASS_METHODS_AVRoutingScheduledVolumeRamp
+ __OBJC_$_CLASS_METHODS_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_$_CLASS_METHODS_AVRoutingSessionManager
+ __OBJC_$_CLASS_METHODS_AVRoutingWeakReference
+ __OBJC_$_CLASS_METHODS_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_$_CLASS_METHODS_CMAVRoutingTimeAsValue
+ __OBJC_$_CLASS_METHODS_CMAVRoutingTimeMappingAsValue
+ __OBJC_$_CLASS_METHODS_CMAVRoutingTimeRangeAsValue
+ __OBJC_$_CLASS_METHODS_NSValue(NSValueCMVideoDimensionsExtensions|NSValueCMTimeExtensions)
+ __OBJC_$_CLASS_PROP_LIST_AVInputContext
+ __OBJC_$_CLASS_PROP_LIST_AVRoutingScheduledFloatValueRamp
+ __OBJC_$_CLASS_PROP_LIST_AVRoutingScheduledParameterRamp
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_AVClusterComponentOutputDeviceDescription
+ __OBJC_$_INSTANCE_METHODS_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_$_INSTANCE_METHODS_AVExecutionEnvironment
+ __OBJC_$_INSTANCE_METHODS_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_$_INSTANCE_METHODS_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointOutputDeviceImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointSecondDisplayModeToken
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRemoteRouteDiscovererFactory
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ __OBJC_$_INSTANCE_METHODS_AVFigRoutingContextInputContextCompletionContext
+ __OBJC_$_INSTANCE_METHODS_AVFigRoutingContextInputContextImpl
+ __OBJC_$_INSTANCE_METHODS_AVFigRoutingContextOutputContextCompletionContext
+ __OBJC_$_INSTANCE_METHODS_AVFigRoutingContextOutputContextImpl
+ __OBJC_$_INSTANCE_METHODS_AVInputContext
+ __OBJC_$_INSTANCE_METHODS_AVInputContextDestinationChange(FigRoutingContextAdditions)
+ __OBJC_$_INSTANCE_METHODS_AVInputDevice
+ __OBJC_$_INSTANCE_METHODS_AVInputDeviceDiscoverySession(FigRouteDiscoverer)
+ __OBJC_$_INSTANCE_METHODS_AVLocalOutputDeviceImpl
+ __OBJC_$_INSTANCE_METHODS_AVOutputContext(AVAudioSession|FigRoutingContext)
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextCommunicationChannel(FigCommChannelUUID)
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextDestinationChange(FigRoutingContextAdditions)
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextFactory
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextInternal
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextManager
+ __OBJC_$_INSTANCE_METHODS_AVOutputContextModificationResult
+ __OBJC_$_INSTANCE_METHODS_AVOutputDevice(AVOutputDeviceFigEndpointImplFetching|FigRouteDescriptor)
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceAuthorizationRequest
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceAuthorizationSession
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceAuthorizationSessionInternal
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceAuthorizedPeer
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceCommunicationChannel
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceDiscoverySession(FigRouteDiscoverer)
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceFrecentsReader
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceFrecentsWriter
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceGroup
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceGroupMembershipChangeResult
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceHID
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceIcon
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceInternal
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceScreenBorrowToken
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceScreenInfo
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceTurnByTurnToken
+ __OBJC_$_INSTANCE_METHODS_AVOutputDeviceViewAreaInfo
+ __OBJC_$_INSTANCE_METHODS_AVPairedDevice
+ __OBJC_$_INSTANCE_METHODS_AVRoutingBlockOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingCMNotificationDispatcher
+ __OBJC_$_INSTANCE_METHODS_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_$_INSTANCE_METHODS_AVRoutingCallbackContextRegistry
+ __OBJC_$_INSTANCE_METHODS_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_$_INSTANCE_METHODS_AVRoutingContextRouteChangeOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingDepartureAnnouncingObjectMonitor
+ __OBJC_$_INSTANCE_METHODS_AVRoutingDispatchOnce
+ __OBJC_$_INSTANCE_METHODS_AVRoutingEventWaiter
+ __OBJC_$_INSTANCE_METHODS_AVRoutingGlobalOperationQueue
+ __OBJC_$_INSTANCE_METHODS_AVRoutingMutableScheduledAudioParameters
+ __OBJC_$_INSTANCE_METHODS_AVRoutingOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingOperationQueueWithFundamentalDependency
+ __OBJC_$_INSTANCE_METHODS_AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport|AVRoutingPlaybackParticipantRegistration)
+ __OBJC_$_INSTANCE_METHODS_AVRoutingRetainReleaseWeakReference
+ __OBJC_$_INSTANCE_METHODS_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal)
+ __OBJC_$_INSTANCE_METHODS_AVRoutingScheduledFloatValueRamp(AVRoutingScheduledParameterRampSerialization)
+ __OBJC_$_INSTANCE_METHODS_AVRoutingScheduledParameterRamp(AVRoutingScheduledParameterRampSerialization)
+ __OBJC_$_INSTANCE_METHODS_AVRoutingScheduledVolumeRamp(AVRoutingScheduledParameterRampSerialization)
+ __OBJC_$_INSTANCE_METHODS_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_$_INSTANCE_METHODS_AVRoutingSession
+ __OBJC_$_INSTANCE_METHODS_AVRoutingSessionDestination
+ __OBJC_$_INSTANCE_METHODS_AVRoutingSessionManager
+ __OBJC_$_INSTANCE_METHODS_AVRoutingSynchronousBlockScheduler
+ __OBJC_$_INSTANCE_METHODS_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_$_INSTANCE_METHODS_AVRoutingWeakReference
+ __OBJC_$_INSTANCE_METHODS_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_$_INSTANCE_METHODS_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_$_INSTANCE_METHODS_AVVolumeController
+ __OBJC_$_INSTANCE_METHODS_CMAVRoutingTimeAsValue
+ __OBJC_$_INSTANCE_METHODS_CMAVRoutingTimeMappingAsValue
+ __OBJC_$_INSTANCE_METHODS_CMAVRoutingTimeRangeAsValue
+ __OBJC_$_INSTANCE_METHODS_NSValue(NSValueCMVideoDimensionsExtensions|NSValueCMTimeExtensions)
+ __OBJC_$_INSTANCE_VARIABLES_AVClusterComponentOutputDeviceDescription
+ __OBJC_$_INSTANCE_VARIABLES_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_$_INSTANCE_VARIABLES_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointOutputDeviceImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointSecondDisplayModeToken
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRoutingContextInputContextCompletionContext
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRoutingContextInputContextImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRoutingContextOutputContextCompletionContext
+ __OBJC_$_INSTANCE_VARIABLES_AVFigRoutingContextOutputContextImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVInputContext
+ __OBJC_$_INSTANCE_VARIABLES_AVInputContextDestinationChange
+ __OBJC_$_INSTANCE_VARIABLES_AVInputContextDestinationChangeInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVInputContextInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVInputDevice
+ __OBJC_$_INSTANCE_VARIABLES_AVInputDeviceDiscoverySession
+ __OBJC_$_INSTANCE_VARIABLES_AVInputDeviceDiscoverySessionInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVInputDeviceInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVLocalOutputDeviceImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContext
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextCommunicationChannel
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextCommunicationChannelInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextDestinationChange
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextDestinationChangeInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextFactory
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextManager
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextManagerInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputContextModificationResult
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDevice
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizationRequest
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizationRequestInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizationSession
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizationSessionInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizedPeer
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceAuthorizedPeerInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceCommunicationChannel
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceDiscoverySession
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceDiscoverySessionInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceFrecentsReader
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceFrecentsWriter
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceGroup
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceGroupMembershipChangeResult
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceHID
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceIcon
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceScreenBorrowToken
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceScreenInfo
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceTurnByTurnToken
+ __OBJC_$_INSTANCE_VARIABLES_AVOutputDeviceViewAreaInfo
+ __OBJC_$_INSTANCE_VARIABLES_AVPairedDevice
+ __OBJC_$_INSTANCE_VARIABLES_AVPairedDeviceInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingBlockOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingCMNotificationDispatcher
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingCallbackContextRegistry
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingContextRouteChangeOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingDepartureAnnouncingObjectMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingDispatchOnce
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingEventWaiter
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingGlobalOperationQueue
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingMutableScheduledAudioParameters
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingOperationQueueWithFundamentalDependency
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingPlaybackArbiter
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingRetainReleaseWeakReference
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingScheduledAudioParameters
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingScheduledAudioParametersInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingScheduledFloatValueRamp
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingScheduledParameterRamp
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingScheduledVolumeRamp
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSession
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSessionDestination
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSessionDestinationInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSessionInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingSessionManagerInternal
+ __OBJC_$_INSTANCE_VARIABLES_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_$_INSTANCE_VARIABLES_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_$_INSTANCE_VARIABLES_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_$_INSTANCE_VARIABLES_AVVolumeController
+ __OBJC_$_INSTANCE_VARIABLES_CMAVRoutingTimeAsValue
+ __OBJC_$_INSTANCE_VARIABLES_CMAVRoutingTimeMappingAsValue
+ __OBJC_$_INSTANCE_VARIABLES_CMAVRoutingTimeRangeAsValue
+ __OBJC_$_PROP_LIST_AVClusterComponentOutputDeviceDescription
+ __OBJC_$_PROP_LIST_AVDestinationChangeResultSource
+ __OBJC_$_PROP_LIST_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_$_PROP_LIST_AVExecutionEnvironment
+ __OBJC_$_PROP_LIST_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_$_PROP_LIST_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_PROP_LIST_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointOutputDeviceImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_PROP_LIST_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_PROP_LIST_AVFigRemoteRouteDiscovererFactory
+ __OBJC_$_PROP_LIST_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_PROP_LIST_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_$_PROP_LIST_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROP_LIST_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_$_PROP_LIST_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_$_PROP_LIST_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_$_PROP_LIST_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_$_PROP_LIST_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ __OBJC_$_PROP_LIST_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_$_PROP_LIST_AVFigRoutingContextInputContextCompletionContext
+ __OBJC_$_PROP_LIST_AVFigRoutingContextInputContextImpl
+ __OBJC_$_PROP_LIST_AVFigRoutingContextOutputContextCompletionContext
+ __OBJC_$_PROP_LIST_AVFigRoutingContextOutputContextImpl
+ __OBJC_$_PROP_LIST_AVInputContext
+ __OBJC_$_PROP_LIST_AVInputContextDestinationChange
+ __OBJC_$_PROP_LIST_AVInputContextImpl
+ __OBJC_$_PROP_LIST_AVInputDevice
+ __OBJC_$_PROP_LIST_AVInputDeviceDiscoverySessionImpl
+ __OBJC_$_PROP_LIST_AVInputDeviceImpl
+ __OBJC_$_PROP_LIST_AVLocalOutputDeviceImpl
+ __OBJC_$_PROP_LIST_AVOutputContextCommunicationChannelImpl
+ __OBJC_$_PROP_LIST_AVOutputContextDestinationChange
+ __OBJC_$_PROP_LIST_AVOutputContextImpl
+ __OBJC_$_PROP_LIST_AVOutputContextManagerImpl
+ __OBJC_$_PROP_LIST_AVOutputContextModificationResult
+ __OBJC_$_PROP_LIST_AVOutputDeviceAuthorizationRequest
+ __OBJC_$_PROP_LIST_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceAuthorizationSession
+ __OBJC_$_PROP_LIST_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceAuthorizedPeer
+ __OBJC_$_PROP_LIST_AVOutputDeviceCommunicationChannel
+ __OBJC_$_PROP_LIST_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceCommunicationChannelManager
+ __OBJC_$_PROP_LIST_AVOutputDeviceConfigurationRetrieval
+ __OBJC_$_PROP_LIST_AVOutputDeviceDescription
+ __OBJC_$_PROP_LIST_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_$_PROP_LIST_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceFrecentsReader
+ __OBJC_$_PROP_LIST_AVOutputDeviceFrecentsReading
+ __OBJC_$_PROP_LIST_AVOutputDeviceFrecentsWriter
+ __OBJC_$_PROP_LIST_AVOutputDeviceFrecentsWriting
+ __OBJC_$_PROP_LIST_AVOutputDeviceGroup
+ __OBJC_$_PROP_LIST_AVOutputDeviceGroupMembershipChangeResult
+ __OBJC_$_PROP_LIST_AVOutputDeviceHID
+ __OBJC_$_PROP_LIST_AVOutputDeviceIcon
+ __OBJC_$_PROP_LIST_AVOutputDeviceImpl
+ __OBJC_$_PROP_LIST_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_$_PROP_LIST_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_$_PROP_LIST_AVOutputDeviceScreenBorrowToken
+ __OBJC_$_PROP_LIST_AVOutputDeviceScreenInfo
+ __OBJC_$_PROP_LIST_AVOutputDeviceViewAreaInfo
+ __OBJC_$_PROP_LIST_AVPairedDevice
+ __OBJC_$_PROP_LIST_AVRoutingCMNotificationDispatcher
+ __OBJC_$_PROP_LIST_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_$_PROP_LIST_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_$_PROP_LIST_AVRoutingContextRouteChangeOperation
+ __OBJC_$_PROP_LIST_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_$_PROP_LIST_AVRoutingGlobalOperationQueue
+ __OBJC_$_PROP_LIST_AVRoutingOperation
+ __OBJC_$_PROP_LIST_AVRoutingPlaybackArbiter
+ __OBJC_$_PROP_LIST_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_$_PROP_LIST_AVRoutingScheduledAudioParameters
+ __OBJC_$_PROP_LIST_AVRoutingScheduledFloatValueRamp
+ __OBJC_$_PROP_LIST_AVRoutingScheduledParameterRamp
+ __OBJC_$_PROP_LIST_AVRoutingScheduledVolumeRamp
+ __OBJC_$_PROP_LIST_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_$_PROP_LIST_AVRoutingSession
+ __OBJC_$_PROP_LIST_AVRoutingSessionDestination
+ __OBJC_$_PROP_LIST_AVRoutingSessionManager
+ __OBJC_$_PROP_LIST_AVRoutingSynchronousBlockScheduler
+ __OBJC_$_PROP_LIST_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_$_PROP_LIST_AVRoutingWeakReference
+ __OBJC_$_PROP_LIST_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROP_LIST_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_$_PROP_LIST_AVVolumeController
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_NSValue_$_NSValueCMVideoDimensionsExtensions
+ __OBJC_$_PROTOCOL_CLASS_METHODS_AVInputContextImpl
+ __OBJC_$_PROTOCOL_CLASS_METHODS_AVOutputContextImpl
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVBlockScheduler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVDestinationChangeResultSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFigRouteDiscovererFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVInputContextImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVInputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVInputDeviceImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputContextCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputContextImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputContextManagerImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceCommunicationChannelManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceConfigurationModification
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceConfigurationRetrieval
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceDiscoverySessionFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceFrecentsReading
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceFrecentsWriting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVOutputDeviceImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSMutableCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVObjectMonitoring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVOutputDeviceDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WebKitSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVBlockScheduler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVDestinationChangeResultSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFigRouteDiscovererFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVInputContextImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVInputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVInputDeviceImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVObjectMonitoring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputContextCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputContextImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputContextManagerImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceCommunicationChannelManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceConfigurationModification
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceConfigurationRetrieval
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceDescription
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceDiscoverySessionFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceFrecentsReading
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceFrecentsWriting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVOutputDeviceImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSMutableCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WebKitSecureCoding
+ __OBJC_$_PROTOCOL_REFS_AVBlockScheduler
+ __OBJC_$_PROTOCOL_REFS_AVDestinationChangeResultSource
+ __OBJC_$_PROTOCOL_REFS_AVFigRouteDiscovererFactory
+ __OBJC_$_PROTOCOL_REFS_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_$_PROTOCOL_REFS_AVFigRoutingContextOutputDeviceTranslator
+ __OBJC_$_PROTOCOL_REFS_AVInputContextImpl
+ __OBJC_$_PROTOCOL_REFS_AVInputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_REFS_AVInputDeviceImpl
+ __OBJC_$_PROTOCOL_REFS_AVObjectMonitoring
+ __OBJC_$_PROTOCOL_REFS_AVOutputContextCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputContextImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputContextManagerImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceCommunicationChannelManager
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceConfigurationModification
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceConfigurationRetrieval
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceDescription
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceDiscoverySessionFactory
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceFrecentsReading
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceFrecentsWriting
+ __OBJC_$_PROTOCOL_REFS_AVOutputDeviceImpl
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_AVClusterComponentOutputDeviceDescription
+ __OBJC_CLASS_PROTOCOLS_$_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_CLASS_PROTOCOLS_$_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_CLASS_PROTOCOLS_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointOutputDeviceImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRemoteRouteDiscovererFactory
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRoutingContextInputContextImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVFigRoutingContextOutputContextImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVInputContext
+ __OBJC_CLASS_PROTOCOLS_$_AVLocalOutputDeviceImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVOutputContext
+ __OBJC_CLASS_PROTOCOLS_$_AVOutputDeviceFrecentsReader
+ __OBJC_CLASS_PROTOCOLS_$_AVOutputDeviceFrecentsWriter
+ __OBJC_CLASS_PROTOCOLS_$_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_CLASS_PROTOCOLS_$_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingContextRouteChangeOperation
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingScheduledAudioParameters
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingScheduledParameterRamp
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingSynchronousBlockScheduler
+ __OBJC_CLASS_PROTOCOLS_$_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_CLASS_PROTOCOLS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_CLASS_PROTOCOLS_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_CLASS_RO_$_AVClusterComponentOutputDeviceDescription
+ __OBJC_CLASS_RO_$_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_CLASS_RO_$_AVExecutionEnvironment
+ __OBJC_CLASS_RO_$_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_CLASS_RO_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_CLASS_RO_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointOutputDeviceImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointSecondDisplayModeToken
+ __OBJC_CLASS_RO_$_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_CLASS_RO_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_CLASS_RO_$_AVFigRemoteRouteDiscovererFactory
+ __OBJC_CLASS_RO_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_CLASS_RO_$_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_CLASS_RO_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_CLASS_RO_$_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_CLASS_RO_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_CLASS_RO_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_CLASS_RO_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_CLASS_RO_$_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ __OBJC_CLASS_RO_$_AVFigRoutingContextInputContextCompletionContext
+ __OBJC_CLASS_RO_$_AVFigRoutingContextInputContextImpl
+ __OBJC_CLASS_RO_$_AVFigRoutingContextOutputContextCompletionContext
+ __OBJC_CLASS_RO_$_AVFigRoutingContextOutputContextImpl
+ __OBJC_CLASS_RO_$_AVInputContext
+ __OBJC_CLASS_RO_$_AVInputContextDestinationChange
+ __OBJC_CLASS_RO_$_AVInputContextDestinationChangeInternal
+ __OBJC_CLASS_RO_$_AVInputContextInternal
+ __OBJC_CLASS_RO_$_AVInputDevice
+ __OBJC_CLASS_RO_$_AVInputDeviceDiscoverySession
+ __OBJC_CLASS_RO_$_AVInputDeviceDiscoverySessionInternal
+ __OBJC_CLASS_RO_$_AVInputDeviceInternal
+ __OBJC_CLASS_RO_$_AVLocalOutputDeviceImpl
+ __OBJC_CLASS_RO_$_AVOutputContext
+ __OBJC_CLASS_RO_$_AVOutputContextCommunicationChannel
+ __OBJC_CLASS_RO_$_AVOutputContextCommunicationChannelInternal
+ __OBJC_CLASS_RO_$_AVOutputContextDestinationChange
+ __OBJC_CLASS_RO_$_AVOutputContextDestinationChangeInternal
+ __OBJC_CLASS_RO_$_AVOutputContextFactory
+ __OBJC_CLASS_RO_$_AVOutputContextInternal
+ __OBJC_CLASS_RO_$_AVOutputContextManager
+ __OBJC_CLASS_RO_$_AVOutputContextManagerInternal
+ __OBJC_CLASS_RO_$_AVOutputContextModificationResult
+ __OBJC_CLASS_RO_$_AVOutputDevice
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizationRequest
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizationRequestInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizationSession
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizationSessionInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizedPeer
+ __OBJC_CLASS_RO_$_AVOutputDeviceAuthorizedPeerInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceCommunicationChannel
+ __OBJC_CLASS_RO_$_AVOutputDeviceDiscoverySession
+ __OBJC_CLASS_RO_$_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_CLASS_RO_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceDiscoverySessionInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceFrecencyManager
+ __OBJC_CLASS_RO_$_AVOutputDeviceFrecentsReader
+ __OBJC_CLASS_RO_$_AVOutputDeviceFrecentsWriter
+ __OBJC_CLASS_RO_$_AVOutputDeviceGroup
+ __OBJC_CLASS_RO_$_AVOutputDeviceGroupMembershipChangeResult
+ __OBJC_CLASS_RO_$_AVOutputDeviceHID
+ __OBJC_CLASS_RO_$_AVOutputDeviceIcon
+ __OBJC_CLASS_RO_$_AVOutputDeviceInternal
+ __OBJC_CLASS_RO_$_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_CLASS_RO_$_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_CLASS_RO_$_AVOutputDeviceScreenBorrowToken
+ __OBJC_CLASS_RO_$_AVOutputDeviceScreenInfo
+ __OBJC_CLASS_RO_$_AVOutputDeviceTurnByTurnToken
+ __OBJC_CLASS_RO_$_AVOutputDeviceViewAreaInfo
+ __OBJC_CLASS_RO_$_AVPairedDevice
+ __OBJC_CLASS_RO_$_AVPairedDeviceInternal
+ __OBJC_CLASS_RO_$_AVRoutingAmbienceLevelRamp
+ __OBJC_CLASS_RO_$_AVRoutingAmbienceLoudnessRamp
+ __OBJC_CLASS_RO_$_AVRoutingBlockOperation
+ __OBJC_CLASS_RO_$_AVRoutingCMNotificationDispatcher
+ __OBJC_CLASS_RO_$_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_CLASS_RO_$_AVRoutingCallbackContextRegistry
+ __OBJC_CLASS_RO_$_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_CLASS_RO_$_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_CLASS_RO_$_AVRoutingContextRouteChangeOperation
+ __OBJC_CLASS_RO_$_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_CLASS_RO_$_AVRoutingDepartureAnnouncingObjectMonitor
+ __OBJC_CLASS_RO_$_AVRoutingDialogLevelRamp
+ __OBJC_CLASS_RO_$_AVRoutingDialogLoudnessRamp
+ __OBJC_CLASS_RO_$_AVRoutingDialogMixBiasRamp
+ __OBJC_CLASS_RO_$_AVRoutingDispatchOnce
+ __OBJC_CLASS_RO_$_AVRoutingEventWaiter
+ __OBJC_CLASS_RO_$_AVRoutingGlobalOperationQueue
+ __OBJC_CLASS_RO_$_AVRoutingMutableScheduledAudioParameters
+ __OBJC_CLASS_RO_$_AVRoutingOperation
+ __OBJC_CLASS_RO_$_AVRoutingOperationQueueWithFundamentalDependency
+ __OBJC_CLASS_RO_$_AVRoutingPlaybackArbiter
+ __OBJC_CLASS_RO_$_AVRoutingRecordingLoudnessRamp
+ __OBJC_CLASS_RO_$_AVRoutingRenderingStyleRamp
+ __OBJC_CLASS_RO_$_AVRoutingRetainReleaseWeakReference
+ __OBJC_CLASS_RO_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_CLASS_RO_$_AVRoutingScheduledAudioParameters
+ __OBJC_CLASS_RO_$_AVRoutingScheduledAudioParametersInternal
+ __OBJC_CLASS_RO_$_AVRoutingScheduledFloatValueRamp
+ __OBJC_CLASS_RO_$_AVRoutingScheduledParameterRamp
+ __OBJC_CLASS_RO_$_AVRoutingScheduledVolumeRamp
+ __OBJC_CLASS_RO_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_CLASS_RO_$_AVRoutingSession
+ __OBJC_CLASS_RO_$_AVRoutingSessionDestination
+ __OBJC_CLASS_RO_$_AVRoutingSessionDestinationInternal
+ __OBJC_CLASS_RO_$_AVRoutingSessionInternal
+ __OBJC_CLASS_RO_$_AVRoutingSessionManager
+ __OBJC_CLASS_RO_$_AVRoutingSessionManagerInternal
+ __OBJC_CLASS_RO_$_AVRoutingSynchronousBlockScheduler
+ __OBJC_CLASS_RO_$_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_CLASS_RO_$_AVRoutingWeakReference
+ __OBJC_CLASS_RO_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_CLASS_RO_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_CLASS_RO_$_AVVolumeController
+ __OBJC_CLASS_RO_$_CMAVRoutingTimeAsValue
+ __OBJC_CLASS_RO_$_CMAVRoutingTimeMappingAsValue
+ __OBJC_CLASS_RO_$_CMAVRoutingTimeRangeAsValue
+ __OBJC_LABEL_PROTOCOL_$_AVBlockScheduler
+ __OBJC_LABEL_PROTOCOL_$_AVDestinationChangeResultSource
+ __OBJC_LABEL_PROTOCOL_$_AVFigRouteDiscovererFactory
+ __OBJC_LABEL_PROTOCOL_$_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_LABEL_PROTOCOL_$_AVFigRoutingContextOutputDeviceTranslator
+ __OBJC_LABEL_PROTOCOL_$_AVInputContextImpl
+ __OBJC_LABEL_PROTOCOL_$_AVInputDeviceDiscoverySessionImpl
+ __OBJC_LABEL_PROTOCOL_$_AVInputDeviceImpl
+ __OBJC_LABEL_PROTOCOL_$_AVObjectMonitoring
+ __OBJC_LABEL_PROTOCOL_$_AVOutputContextCommunicationChannelImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputContextImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputContextManagerImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceCommunicationChannelManager
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceConfigurationModification
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceConfigurationRetrieval
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceDescription
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceDiscoverySessionFactory
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceFrecentsReading
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceFrecentsWriting
+ __OBJC_LABEL_PROTOCOL_$_AVOutputDeviceImpl
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSMutableCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_WebKitSecureCoding
+ __OBJC_METACLASS_RO_$_AVClusterComponentOutputDeviceDescription
+ __OBJC_METACLASS_RO_$_AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_METACLASS_RO_$_AVExecutionEnvironment
+ __OBJC_METACLASS_RO_$_AVFigCommChannelUUIDCommunicationChannelManager
+ __OBJC_METACLASS_RO_$_AVFigCommChannelUUIDOutputContextCommunicationChannelImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointFigRoutingContextOutputDeviceTranslator
+ __OBJC_METACLASS_RO_$_AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointOutputDeviceImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointSecondDisplayModeToken
+ __OBJC_METACLASS_RO_$_AVFigEndpointUIAgentOutputContextManagerImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl
+ __OBJC_METACLASS_RO_$_AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl
+ __OBJC_METACLASS_RO_$_AVFigRemoteRouteDiscovererFactory
+ __OBJC_METACLASS_RO_$_AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator
+ __OBJC_METACLASS_RO_$_AVFigRouteDescriptorInputDeviceImpl
+ __OBJC_METACLASS_RO_$_AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_METACLASS_RO_$_AVFigRouteDescriptorOutputDeviceImpl
+ __OBJC_METACLASS_RO_$_AVFigRouteDiscovererInputDeviceDiscoverySessionImpl
+ __OBJC_METACLASS_RO_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory
+ __OBJC_METACLASS_RO_$_AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl
+ __OBJC_METACLASS_RO_$_AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext
+ __OBJC_METACLASS_RO_$_AVFigRoutingContextInputContextCompletionContext
+ __OBJC_METACLASS_RO_$_AVFigRoutingContextInputContextImpl
+ __OBJC_METACLASS_RO_$_AVFigRoutingContextOutputContextCompletionContext
+ __OBJC_METACLASS_RO_$_AVFigRoutingContextOutputContextImpl
+ __OBJC_METACLASS_RO_$_AVInputContext
+ __OBJC_METACLASS_RO_$_AVInputContextDestinationChange
+ __OBJC_METACLASS_RO_$_AVInputContextDestinationChangeInternal
+ __OBJC_METACLASS_RO_$_AVInputContextInternal
+ __OBJC_METACLASS_RO_$_AVInputDevice
+ __OBJC_METACLASS_RO_$_AVInputDeviceDiscoverySession
+ __OBJC_METACLASS_RO_$_AVInputDeviceDiscoverySessionInternal
+ __OBJC_METACLASS_RO_$_AVInputDeviceInternal
+ __OBJC_METACLASS_RO_$_AVLocalOutputDeviceImpl
+ __OBJC_METACLASS_RO_$_AVOutputContext
+ __OBJC_METACLASS_RO_$_AVOutputContextCommunicationChannel
+ __OBJC_METACLASS_RO_$_AVOutputContextCommunicationChannelInternal
+ __OBJC_METACLASS_RO_$_AVOutputContextDestinationChange
+ __OBJC_METACLASS_RO_$_AVOutputContextDestinationChangeInternal
+ __OBJC_METACLASS_RO_$_AVOutputContextFactory
+ __OBJC_METACLASS_RO_$_AVOutputContextInternal
+ __OBJC_METACLASS_RO_$_AVOutputContextManager
+ __OBJC_METACLASS_RO_$_AVOutputContextManagerInternal
+ __OBJC_METACLASS_RO_$_AVOutputContextModificationResult
+ __OBJC_METACLASS_RO_$_AVOutputDevice
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizationRequest
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizationRequestInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizationSession
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizationSessionInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizedPeer
+ __OBJC_METACLASS_RO_$_AVOutputDeviceAuthorizedPeerInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceCommunicationChannel
+ __OBJC_METACLASS_RO_$_AVOutputDeviceDiscoverySession
+ __OBJC_METACLASS_RO_$_AVOutputDeviceDiscoverySessionAvailableOutputDevices
+ __OBJC_METACLASS_RO_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceDiscoverySessionInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceFrecencyManager
+ __OBJC_METACLASS_RO_$_AVOutputDeviceFrecentsReader
+ __OBJC_METACLASS_RO_$_AVOutputDeviceFrecentsWriter
+ __OBJC_METACLASS_RO_$_AVOutputDeviceGroup
+ __OBJC_METACLASS_RO_$_AVOutputDeviceGroupMembershipChangeResult
+ __OBJC_METACLASS_RO_$_AVOutputDeviceHID
+ __OBJC_METACLASS_RO_$_AVOutputDeviceIcon
+ __OBJC_METACLASS_RO_$_AVOutputDeviceInternal
+ __OBJC_METACLASS_RO_$_AVOutputDeviceLegacyFrecentsReader
+ __OBJC_METACLASS_RO_$_AVOutputDeviceLegacyFrecentsWriter
+ __OBJC_METACLASS_RO_$_AVOutputDeviceScreenBorrowToken
+ __OBJC_METACLASS_RO_$_AVOutputDeviceScreenInfo
+ __OBJC_METACLASS_RO_$_AVOutputDeviceTurnByTurnToken
+ __OBJC_METACLASS_RO_$_AVOutputDeviceViewAreaInfo
+ __OBJC_METACLASS_RO_$_AVPairedDevice
+ __OBJC_METACLASS_RO_$_AVPairedDeviceInternal
+ __OBJC_METACLASS_RO_$_AVRoutingAmbienceLevelRamp
+ __OBJC_METACLASS_RO_$_AVRoutingAmbienceLoudnessRamp
+ __OBJC_METACLASS_RO_$_AVRoutingBlockOperation
+ __OBJC_METACLASS_RO_$_AVRoutingCMNotificationDispatcher
+ __OBJC_METACLASS_RO_$_AVRoutingCMNotificationDispatcherListenerKey
+ __OBJC_METACLASS_RO_$_AVRoutingCallbackContextRegistry
+ __OBJC_METACLASS_RO_$_AVRoutingContextCommandOutputDeviceConfiguration
+ __OBJC_METACLASS_RO_$_AVRoutingContextCommandOutputDeviceConfigurationModification
+ __OBJC_METACLASS_RO_$_AVRoutingContextRouteChangeOperation
+ __OBJC_METACLASS_RO_$_AVRoutingContextSendConfigureDeviceCommandOperation
+ __OBJC_METACLASS_RO_$_AVRoutingDepartureAnnouncingObjectMonitor
+ __OBJC_METACLASS_RO_$_AVRoutingDialogLevelRamp
+ __OBJC_METACLASS_RO_$_AVRoutingDialogLoudnessRamp
+ __OBJC_METACLASS_RO_$_AVRoutingDialogMixBiasRamp
+ __OBJC_METACLASS_RO_$_AVRoutingDispatchOnce
+ __OBJC_METACLASS_RO_$_AVRoutingEventWaiter
+ __OBJC_METACLASS_RO_$_AVRoutingGlobalOperationQueue
+ __OBJC_METACLASS_RO_$_AVRoutingMutableScheduledAudioParameters
+ __OBJC_METACLASS_RO_$_AVRoutingOperation
+ __OBJC_METACLASS_RO_$_AVRoutingOperationQueueWithFundamentalDependency
+ __OBJC_METACLASS_RO_$_AVRoutingPlaybackArbiter
+ __OBJC_METACLASS_RO_$_AVRoutingRecordingLoudnessRamp
+ __OBJC_METACLASS_RO_$_AVRoutingRenderingStyleRamp
+ __OBJC_METACLASS_RO_$_AVRoutingRetainReleaseWeakReference
+ __OBJC_METACLASS_RO_$_AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation
+ __OBJC_METACLASS_RO_$_AVRoutingScheduledAudioParameters
+ __OBJC_METACLASS_RO_$_AVRoutingScheduledAudioParametersInternal
+ __OBJC_METACLASS_RO_$_AVRoutingScheduledFloatValueRamp
+ __OBJC_METACLASS_RO_$_AVRoutingScheduledParameterRamp
+ __OBJC_METACLASS_RO_$_AVRoutingScheduledVolumeRamp
+ __OBJC_METACLASS_RO_$_AVRoutingSerializedMostlySynchronousReentrantBlockScheduler
+ __OBJC_METACLASS_RO_$_AVRoutingSession
+ __OBJC_METACLASS_RO_$_AVRoutingSessionDestination
+ __OBJC_METACLASS_RO_$_AVRoutingSessionDestinationInternal
+ __OBJC_METACLASS_RO_$_AVRoutingSessionInternal
+ __OBJC_METACLASS_RO_$_AVRoutingSessionManager
+ __OBJC_METACLASS_RO_$_AVRoutingSessionManagerInternal
+ __OBJC_METACLASS_RO_$_AVRoutingSynchronousBlockScheduler
+ __OBJC_METACLASS_RO_$_AVRoutingWaitForNotificationOrDeallocationOperation
+ __OBJC_METACLASS_RO_$_AVRoutingWeakReference
+ __OBJC_METACLASS_RO_$_AVSystemRemotePoolOutputDeviceCommunicationChannelImpl
+ __OBJC_METACLASS_RO_$_AVSystemRemotePoolOutputDeviceCommunicationChannelManager
+ __OBJC_METACLASS_RO_$_AVVolumeController
+ __OBJC_METACLASS_RO_$_CMAVRoutingTimeAsValue
+ __OBJC_METACLASS_RO_$_CMAVRoutingTimeMappingAsValue
+ __OBJC_METACLASS_RO_$_CMAVRoutingTimeRangeAsValue
+ __OBJC_PROTOCOL_$_AVBlockScheduler
+ __OBJC_PROTOCOL_$_AVDestinationChangeResultSource
+ __OBJC_PROTOCOL_$_AVFigRouteDiscovererFactory
+ __OBJC_PROTOCOL_$_AVFigRoutingContextCommunicationChannelManager
+ __OBJC_PROTOCOL_$_AVFigRoutingContextOutputDeviceTranslator
+ __OBJC_PROTOCOL_$_AVInputContextImpl
+ __OBJC_PROTOCOL_$_AVInputDeviceDiscoverySessionImpl
+ __OBJC_PROTOCOL_$_AVInputDeviceImpl
+ __OBJC_PROTOCOL_$_AVObjectMonitoring
+ __OBJC_PROTOCOL_$_AVOutputContextCommunicationChannelImpl
+ __OBJC_PROTOCOL_$_AVOutputContextImpl
+ __OBJC_PROTOCOL_$_AVOutputContextManagerImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceAuthorizationRequestImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceAuthorizationSessionImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceCommunicationChannelImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceCommunicationChannelManager
+ __OBJC_PROTOCOL_$_AVOutputDeviceConfigurationModification
+ __OBJC_PROTOCOL_$_AVOutputDeviceConfigurationRetrieval
+ __OBJC_PROTOCOL_$_AVOutputDeviceDescription
+ __OBJC_PROTOCOL_$_AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceDiscoverySessionFactory
+ __OBJC_PROTOCOL_$_AVOutputDeviceDiscoverySessionImpl
+ __OBJC_PROTOCOL_$_AVOutputDeviceFrecentsReading
+ __OBJC_PROTOCOL_$_AVOutputDeviceFrecentsWriting
+ __OBJC_PROTOCOL_$_AVOutputDeviceImpl
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSMutableCopying
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_WebKitSecureCoding
+ ___102-[AVFigRouteDescriptorOutputDeviceImpl performHapticFeedbackForUUID:withHapticType:completionHandler:]_block_invoke
+ ___102-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _initializeIfNeededAndGetSystemRemotePool]_block_invoke
+ ___103+[AVFigRoutingContextOutputContextImpl outputContextImplForControllingOutputDeviceGroupWithID:options:]_block_invoke
+ ___103-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]_block_invoke
+ ___106-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]_block_invoke
+ ___107-[AVRoutingCMNotificationDispatcher _copyAndRemoveObserverForWeakReferenceToListener:callback:name:object:]_block_invoke
+ ___114-[AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory outputDeviceDiscoverySessionOfClass:withDeviceFeatures:]_block_invoke
+ ___114-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didReceiveData:fromDeviceWithID:fromChannelWithUUID:]_block_invoke
+ ___115-[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _getRampOfClass:forTime:timeRange:]_block_invoke
+ ___115-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]_block_invoke
+ ___115-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]_block_invoke.11
+ ___119-[AVFigEndpointFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke
+ ___119-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke
+ ___120-[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke
+ ___124-[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke
+ ___126-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator addOutputDevice:withOptions:toRoutingContext:completionHandler:]_block_invoke
+ ___126-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:]_block_invoke
+ ___127-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:]_block_invoke
+ ___131-[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:]_block_invoke
+ ___22-[AVInputContext impl]_block_invoke
+ ___23-[AVOutputContext impl]_block_invoke
+ ___27-[AVRoutingOperation error]_block_invoke
+ ___28-[AVRoutingOperation status]_block_invoke
+ ___32+[AVOutputContext outputContext]_block_invoke
+ ___37-[AVInputDeviceDiscoverySession impl]_block_invoke
+ ___38-[AVOutputDeviceDiscoverySession impl]_block_invoke
+ ___39-[AVOutputContext outputDeviceFeatures]_block_invoke
+ ___40+[AVOutputContextFactory sharedInstance]_block_invoke
+ ___41-[AVInputContextDestinationChange status]_block_invoke
+ ___42-[AVInputContext getApplicationProcessID:]_block_invoke
+ ___42-[AVInputContext setApplicationProcessID:]_block_invoke
+ ___42-[AVOutputContextDestinationChange status]_block_invoke
+ ___42-[AVOutputDeviceAuthorizationSession impl]_block_invoke
+ ___43-[AVOutputContext getApplicationProcessID:]_block_invoke
+ ___43-[AVOutputContext setApplicationProcessID:]_block_invoke
+ ___43-[AVOutputDeviceAuthorizationRequest error]_block_invoke
+ ___44-[AVOutputDeviceAuthorizationRequest status]_block_invoke
+ ___45+[AVRoutingGlobalOperationQueue defaultQueue]_block_invoke
+ ___45-[AVRoutingContextRouteChangeOperation start]_block_invoke
+ ___46-[AVInputContextDestinationChange _setStatus:]_block_invoke
+ ___46-[AVInputDeviceDiscoverySession discoveryMode]_block_invoke
+ ___46-[AVRoutingContextRouteChangeOperation result]_block_invoke
+ ___47-[AVOutputContext setOutputDevice:forFeatures:]_block_invoke
+ ___47-[AVOutputContext setOutputDevice:forFeatures:]_block_invoke_2
+ ___47-[AVOutputDeviceDiscoverySession discoveryMode]_block_invoke
+ ___48-[AVRoutingSessionManager allLikelyDestinations]_block_invoke
+ ___50+[AVOutputDeviceFrecencyManager _frecentsFilePath]_block_invoke
+ ___50-[AVOutputDevice _shouldHideAirPlayInfoDuringDemo]_block_invoke
+ ___51-[AVRoutingContextRouteChangeOperation resultInput]_block_invoke
+ ___52+[AVExecutionEnvironment sharedExecutionEnvironment]_block_invoke
+ ___53-[AVRoutingSessionManager likelyExternalDestinations]_block_invoke
+ ___54-[AVOutputContextDestinationChange cancellationReason]_block_invoke
+ ___56+[AVRoutingPlaybackArbiter sharedRoutingPlaybackArbiter]_block_invoke
+ ___56-[AVFigRouteDescriptorOutputDeviceImpl outputDeviceHIDs]_block_invoke
+ ___56-[AVInputDeviceDiscoverySession initWithDeviceFeatures:]_block_invoke
+ ___56-[AVOutputDevice configureUsingBlock:completionHandler:]_block_invoke
+ ___56-[AVOutputDeviceDiscoverySession availableOutputDevices]_block_invoke
+ ___56-[AVOutputDeviceDiscoverySession cachedDiscoveryEnabled]_block_invoke
+ ___57-[AVOutputDevice setSecondDisplayMode:completionHandler:]_block_invoke
+ ___58+[AVFigRoutingContextOutputContextImpl iTunesAudioContext]_block_invoke
+ ___58-[AVFigRouteDescriptorOutputDeviceImpl displayCornerMasks]_block_invoke
+ ___58-[AVFigRouteDescriptorOutputDeviceImpl mediaSessionStatus]_block_invoke
+ ___58-[AVOutputDevice setCarPlayVideoActive:completionHandler:]_block_invoke
+ ___59-[AVInputContext setInputDevice:options:completionHandler:]_block_invoke
+ ___60-[AVFigRouteDescriptorOutputDeviceImpl isCarPlayVideoActive]_block_invoke
+ ___60-[AVInputContext inputContextImpl:didExpireWithReplacement:]_block_invoke
+ ___60-[AVOutputDeviceDiscoverySession setCachedDiscoveryEnabled:]_block_invoke
+ ___60-[AVRoutingCallbackContextRegistry callbackContextForToken:]_block_invoke
+ ___60-[AVRoutingContextRouteChangeOperation _routeChangeComplete]_block_invoke
+ ___61-[AVFigRouteDescriptorOutputDeviceImpl isCarPlayVideoAllowed]_block_invoke
+ ___61-[AVOutputContext addOutputDevice:options:completionHandler:]_block_invoke
+ ___61-[AVOutputContext setOutputDevice:options:completionHandler:]_block_invoke
+ ___62+[AVFigRoutingContextOutputContextImpl auxiliaryOutputContext]_block_invoke
+ ___62-[AVFigRouteDescriptorOutputDeviceImpl setDisplayCornerMasks:]_block_invoke
+ ___62-[AVOutputContext outputContextImpl:didExpireWithReplacement:]_block_invoke
+ ___62-[AVOutputContext setOutputDevices:options:completionHandler:]_block_invoke
+ ___63-[AVOutputDeviceDiscoverySession onlyDiscoversBluetoothDevices]_block_invoke
+ ___64+[AVFigRoutingContextOutputContextImpl sharedSystemAudioContext]_block_invoke
+ ___64+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke
+ ___64+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2
+ ___64-[AVFigRouteDescriptorOutputDeviceImpl setSecondDisplayEnabled:]_block_invoke
+ ___64-[AVOutputContext removeOutputDevice:options:completionHandler:]_block_invoke
+ ___64-[AVOutputDevice configureUsingBlock:options:completionHandler:]_block_invoke
+ ___65+[AVFigRoutingContextOutputContextImpl sharedSystemScreenContext]_block_invoke
+ ___65-[AVFigRouteDescriptorOutputDeviceImpl setSiriForwardingEnabled:]_block_invoke
+ ___65-[AVFigRoutingContextInputContextImpl _routeChangeStartedWithID:]_block_invoke
+ ___66+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke
+ ___66+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2
+ ___66-[AVFigRoutingContextOutputContextImpl _routeChangeStartedWithID:]_block_invoke
+ ___66-[AVOutputContextDestinationChange _setStatus:cancellationReason:]_block_invoke
+ ___66-[AVRoutingCallbackContextRegistry registerCallbackContextObject:]_block_invoke
+ ___66-[AVRoutingContextRouteChangeOperation _routeChangeStartedWithID:]_block_invoke
+ ___66-[AVRoutingContextRouteChangeOperation _setResultIfNotAlreadySet:]_block_invoke
+ ___67-[AVFigRouteDescriptorOutputDeviceImpl takeScreenForClient:reason:]_block_invoke
+ ___67-[AVOutputDeviceDiscoverySession setOnlyDiscoversBluetoothDevices:]_block_invoke
+ ___67-[AVRoutingPlaybackArbiter preferredParticipantForExternalPlayback]_block_invoke
+ ___68+[AVFigRoutingContextInputContextImpl sharedSystemAudioInputContext]_block_invoke
+ ___68-[AVFigRouteDescriptorOutputDeviceImpl requestCarUIForURL:withUUID:]_block_invoke
+ ___68-[AVFigRouteDescriptorOutputDeviceImpl requestViewArea:forScreenID:]_block_invoke
+ ___69+[AVFigRoutingContextOutputContextImpl sharedSystemRemotePoolContext]_block_invoke
+ ___69-[AVFigRouteDescriptorOutputDeviceImpl borrowScreenForClient:reason:]_block_invoke
+ ___69-[AVOutputDeviceGroup addOutputDevice:withOptions:completionHandler:]_block_invoke
+ ___69-[AVRoutingOperation _setStatus:error:resultingStatus:failureReason:]_block_invoke
+ ___70+[AVFigRoutingContextOutputContextImpl defaultSharedOutputContextImpl]_block_invoke
+ ___70-[AVFigRoutingContextInputContextImpl _routeChangeEndedWithID:reason:]_block_invoke
+ ___70-[AVRoutingCallbackContextRegistry unregisterCallbackContextForToken:]_block_invoke
+ ___71+[AVFigRoutingContextOutputContextImpl addSharedAudioOutputContextImpl]_block_invoke
+ ___71-[AVFigRoutingContextInputContextImpl _routeConfigUpdateStartedWithID:]_block_invoke
+ ___71-[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]_block_invoke
+ ___71-[AVFigRoutingContextOutputContextImpl _routeChangeEndedWithID:reason:]_block_invoke
+ ___71-[AVInputDeviceDiscoverySession setDiscoveryMode:forClientIdentifiers:]_block_invoke
+ ___71-[AVRoutingContextRouteChangeOperation _setResultInputIfNotAlreadySet:]_block_invoke
+ ___71-[AVRoutingPlaybackArbiter setPreferredParticipantForExternalPlayback:]_block_invoke
+ ___72+[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]_block_invoke
+ ___72+[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]_block_invoke
+ ___72-[AVFigRoutingContextOutputContextImpl _routeConfigUpdateStartedWithID:]_block_invoke
+ ___72-[AVFigRoutingContextOutputContextImpl initWithRoutingContextUUID:type:]_block_invoke
+ ___72-[AVOutputDeviceDiscoverySession setDiscoveryMode:forClientIdentifiers:]_block_invoke
+ ___72-[AVOutputDeviceGroup removeOutputDevice:withOptions:completionHandler:]_block_invoke
+ ___72-[AVRoutingPlaybackArbiter preferredParticipantForNonMixableAudioRoutes]_block_invoke
+ ___73+[AVFigEndpointUIAgentOutputContextManagerImpl copySharedEndpointUIAgent]_block_invoke
+ ___73+[AVFigEndpointUIAgentOutputContextManagerImpl copySharedEndpointUIAgent]_block_invoke_2
+ ___73+[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary]_block_invoke
+ ___73-[AVFigRouteDescriptorOutputDeviceImpl currentScreenViewAreaForScreenID:]_block_invoke
+ ___74-[AVOutputDeviceDiscoverySessionAvailableOutputDevices _loadOutputDevices]_block_invoke
+ ___74-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation result]_block_invoke
+ ___75-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]_block_invoke
+ ___75-[AVRoutingContextRouteChangeOperation _routeChangeWithID:endedWithReason:]_block_invoke
+ ___76+[AVFigRoutingContextOutputContextImpl sharedAudioPresentationOutputContext]_block_invoke
+ ___76-[AVFigRouteDescriptorOutputDeviceImpl requestTurnByTurnNavigationOwnership]_block_invoke
+ ___76-[AVFigRouteDescriptorOutputDeviceImpl suggestUIWithURLs:completionHandler:]_block_invoke
+ ___76-[AVFigRoutingContextInputContextImpl _routeConfigUpdateEndedWithID:reason:]_block_invoke
+ ___76-[AVRoutingPlaybackArbiter setPreferredParticipantForNonMixableAudioRoutes:]_block_invoke
+ ___77+[AVFigRoutingContextOutputContextImpl platformDependentScreenOrVideoContext]_block_invoke
+ ___77-[AVFigRouteDescriptorOutputDeviceImpl setHeadTrackedSpatialAudioMode:error:]_block_invoke
+ ___77-[AVFigRouteDescriptorOutputDeviceImpl setMediaRemoteData:completionHandler:]_block_invoke
+ ___77-[AVFigRoutingContextOutputContextImpl _routeConfigUpdateEndedWithID:reason:]_block_invoke
+ ___78-[AVFigRouteDescriptorOutputDeviceImpl setConversationDetectionEnabled:error:]_block_invoke
+ ___79-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke
+ ___79-[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke
+ ___79-[AVFigRouteDescriptorOutputDeviceImpl setAllowsHeadTrackedSpatialAudio:error:]_block_invoke
+ ___79-[AVFigRouteDescriptorOutputDeviceImpl setSecondDisplayMode:completionHandler:]_block_invoke
+ ___79-[AVFigRoutingContextOutputContextCompletionContext reportModificationMetrics:]_block_invoke
+ ___79-[AVOutputContextManager outputContextManagerImplDidExpireWithReplacementImpl:]_block_invoke
+ ___79-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation resultInput]_block_invoke
+ ___79-[AVRoutingScheduledAudioParameters _volumeCurveKeysForScheduledRampClassNames]_block_invoke
+ ___80-[AVFigRouteDescriptorOutputDeviceImpl setCarPlayVideoActive:completionHandler:]_block_invoke
+ ___80-[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]_block_invoke
+ ___80-[AVRoutingPlaybackArbiter _setWeakRefToPreferredParticipantForNonMixableAudio:]_block_invoke
+ ___81-[AVRoutingPlaybackArbiter _setWeakRefToPreferredParticipantForExternalPlayback:]_block_invoke
+ ___81-[AVRoutingWaitForNotificationOrDeallocationOperation _waitUntilFinishedIfNeeded]_block_invoke
+ ___82-[AVOutputDevice openCommunicationChannelToDestination:options:completionHandler:]_block_invoke
+ ___83+[AVRoutingCMNotificationDispatcher notificationDispatcherForCMNotificationCenter:]_block_invoke
+ ___86-[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke
+ ___86-[AVOutputDeviceAuthorizationRequest respondWithAuthorizationToken:completionHandler:]_block_invoke
+ ___86-[AVOutputDeviceAuthorizationRequest respondWithAuthorizationToken:completionHandler:]_block_invoke_2
+ ___87+[AVOutputContext(FigRoutingContext) commChannelUUIDCommunicationChannelManagerCreator]_block_invoke
+ ___87+[AVSystemRemotePoolOutputDeviceCommunicationChannelManager sharedSystemRemotePoolImpl]_block_invoke
+ ___87-[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]_block_invoke
+ ___90-[AVInputDeviceDiscoverySession inputDeviceDiscoverySessionImpl:didExpireWithReplacement:]_block_invoke
+ ___90-[AVRoutingPlaybackArbiter(AVRoutingPlaybackParticipantRegistration) registerParticipant:]_block_invoke
+ ___90-[AVRoutingScheduledAudioParameters(AVRoutingScheduledAudioParameters_Internal) _setRamp:]_block_invoke
+ ___90-[AVRoutingWaitForNotificationOrDeallocationOperation _signalMonitoringIsFinishedIfNeeded]_block_invoke
+ ___91-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]_block_invoke
+ ___91-[AVRoutingPlaybackArbiter _updateExternalPlaybackStatusNotificationListenerToParticipant:]_block_invoke.26
+ ___92-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImpl:didExpireWithReplacement:]_block_invoke
+ ___92-[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _addTrackedParticipant:]_block_invoke
+ ___92-[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _allTrackedParticipants]_block_invoke
+ ___93-[AVFigCommChannelUUIDCommunicationChannelManager openCommunicationChannelWithOptions:error:]_block_invoke
+ ___93-[AVRoutingCMNotificationDispatcher addListenerWithWeakReference:callback:name:object:flags:]_block_invoke
+ ___93-[AVRoutingCMNotificationDispatcher addListenerWithWeakReference:callback:name:object:flags:]_block_invoke_2
+ ___94-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _setResultIfNotAlreadySet:]_block_invoke
+ ___95-[AVRoutingPlaybackArbiter(AVRoutingPlaybackArbiterInternalSupport) _removeTrackedParticipant:]_block_invoke
+ ___99-[AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation _setResultInputIfNotAlreadySet:]_block_invoke
+ ___AVInputDeviceCopySharedRouteDiscovererForRouteDescriptor_block_invoke
+ ___AVInputDeviceCopySharedRouteDiscovererForRouteDescriptor_block_invoke_2
+ ___AVMakeAddEndpointOperation_block_invoke
+ ___AVMakeAddEndpointOperation_block_invoke.29
+ ___AVMakeAddRouteDescriptorOperation_block_invoke
+ ___AVMakeAddRouteDescriptorOperation_block_invoke.33
+ ___AVMakeRemoveEndpointOperation_block_invoke
+ ___AVMakeRemoveEndpointOperation_block_invoke.37
+ ___AVMakeRemoveRouteDescriptorOperation_block_invoke
+ ___AVMakeRemoveRouteDescriptorOperation_block_invoke.41
+ ___AVMakeSelectEndpointOperation_block_invoke
+ ___AVMakeSelectEndpointOperation_block_invoke.12
+ ___AVMakeSelectEndpointsOperation_block_invoke
+ ___AVMakeSelectEndpointsOperation_block_invoke.21
+ ___AVMakeSelectRouteDescriptorOperation_block_invoke
+ ___AVMakeSelectRouteDescriptorOperation_block_invoke.17
+ ___AVMakeSelectRouteDescriptorsOperation_block_invoke
+ ___AVMakeSelectRouteDescriptorsOperation_block_invoke.25
+ ___AVOutputContextIsSystemContextAllowed_block_invoke
+ ___AVOutputContextManagerServerConnectionDied_block_invoke
+ ___AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor_block_invoke
+ ___AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor_block_invoke_2
+ ___AVOutputDeviceNotificationFromFigNotification_block_invoke
+ ___AVOutputDevicePerformHapticFeedback_block_invoke
+ ___AVOutputDeviceRouteDiscovererServerDeathNotificationCallback_block_invoke
+ ___AVOutputDeviceSetMediaRemoteDataOnEndpoint_block_invoke
+ ___AVOutputDeviceSetSecondDisplayModeOnEndpoint_block_invoke
+ ___AVOutputDeviceSuggestUIWithURLSAndCompletionHandler_block_invoke
+ ___AVRoutingScheduledParameterRampsIncludesRampThatOverlapsTimeRange_block_invoke
+ ___Block_byref_object_copy_.15
+ ___Block_byref_object_dispose_.16
+ ___NSArray0__struct
+ ____AVRoutingDepartureAnnouncingObjectMonitorAnnounceDeparture_block_invoke
+ ___block_descriptor_112_e8_32o40o48o56o64o72o80o88o96o104b_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e24_v16?0"NSNotification"8l
+ ___block_descriptor_32_e37_B16?0"AVRoutingSessionDestination"8l
+ ___block_descriptor_32_e83_"AVFigCommChannelUUIDCommunicationChannelManager"16?0^{OpaqueFigRoutingContext=}8l
+ ___block_descriptor_33_e28_i16?0^{OpaqueFigEndpoint=}8l
+ ___block_descriptor_36_e32_^{OpaqueFigRouteDiscoverer=}8?0l
+ ___block_descriptor_40_e31_^{OpaqueFigRoutingContext=}8?0l
+ ___block_descriptor_40_e8_32b_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_40_e8_32b_e51_v16?0"AVOutputDeviceGroupMembershipChangeResult"8ls32l8
+ ___block_descriptor_40_e8_32b_e76_v40?0q8"<AVOutputDeviceConfigurationRetrieval>"16"NSString"24"NSError"32ls32l8
+ ___block_descriptor_40_e8_32b_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32o_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8
+ ___block_descriptor_40_e8_32o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8
+ ___block_descriptor_40_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e28_i16?0^{OpaqueFigEndpoint=}8lr32l8
+ ___block_descriptor_41_e8_32b_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_41_e8_32o_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8
+ ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_44_e8_32o_e32_^{OpaqueFigRouteDiscoverer=}8?0ls32l8
+ ___block_descriptor_44_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32o40b_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32o40b_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0i8ls40l8s32l8
+ ___block_descriptor_48_e8_32o40o_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32o40r_e28_i16?0^{OpaqueFigEndpoint=}8lr40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32o_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8
+ ___block_descriptor_48_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e5_i8?0l
+ ___block_descriptor_56_e8_32o40b48r_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32o40o48b_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o40o48r_e28_i16?0^{OpaqueFigEndpoint=}8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32o40o48w_e24_v16?0"NSNotification"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o_e24_v16?0"NSNotification"8ls32l8s40l8
+ ___block_descriptor_56_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32o40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32r40r48r_e28_i16?0^{OpaqueFigEndpoint=}8lr32l8r40l8r48l8
+ ___block_descriptor_60_e8_32o40b48r_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8s40l8r48l8
+ ___block_descriptor_60_e8_32o40o48o_e31_^{OpaqueFigRoutingContext=}8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48b_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32o40o48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32o_e5_i8?0ls32l8
+ ___block_descriptor_64_e8_32r_e15_B32?08Q16^B24lr32l8
+ ___block_descriptor_68_e8_32o40o48b56r_e28_i16?0^{OpaqueFigEndpoint=}8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32o40o48o56b_e41_v16?0"AVInputContextDestinationChange"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32o40o48o56b_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e15_B32?08Q16^B24l
+ ___block_descriptor_80_e8_32o40o48o56o64b_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32o40o48o56o64o72b_e42_v16?0"AVOutputContextDestinationChange"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_96_e8_32o40o48r56r64r72r_e5_v8?0lr48l8s32l8r56l8r64l8s40l8r72l8
+ ___block_literal_global.140
+ ___block_literal_global.23
+ ___block_literal_global.25
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.418
+ ___block_literal_global.438
+ ___block_literal_global.443
+ ___block_literal_global.507
+ ___block_literal_global.579
+ ___strncpy_chk
+ __concreteAVRoutingWeakReferenceClass
+ __dispatch_queue_attr_concurrent
+ __frecentsFilePath.pathLoggingOnce
+ __frecentsReaderAfterMigrationIfNecessary.loggingOnce
+ __os_feature_enabled_impl
+ __os_log_send_and_compose_impl
+ __sSharedCallbackContextRegistry
+ __shouldHideAirPlayInfoDuringDemo.onceToken
+ __shouldHideAirPlayInfoDuringDemo.sHideAirPlayRoutingInfoDemoMode
+ __volumeCurveKeysForScheduledRampClassNames.figKeysForRampClassNames
+ __volumeCurveKeysForScheduledRampClassNames.onceToken
+ _av_readwrite_dispatch_queue_create
+ _av_readwrite_dispatch_queue_read
+ _av_readwrite_dispatch_queue_write
+ _copySharedEndpointUIAgent.onceToken
+ _defaultQueue.sDefaultQueue
+ _defaultQueue.sSharedManagerOnce
+ _dispatch_async
+ _dispatch_barrier_sync
+ _dispatch_get_global_queue
+ _dispatch_get_specific
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_overcommit
+ _dispatch_queue_create
+ _dispatch_queue_set_specific
+ _dispatch_release
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _ensureUserInfoDictionaryContainsObjectForKey
+ _exp2
+ _figEndpointNotifications
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work
+ _fig_note_initialize_logging
+ _gAVBlockSchedulerTrace
+ _gAVFigRoutingContextUtilitiesTrace
+ _gAVInputContextTrace
+ _gAVInputDeviceDiscoverySessionTrace
+ _gAVInputDeviceRouteDiscovererQueue
+ _gAVInputDeviceRouteDiscoverer_AudioInputDiscoverer
+ _gAVInputDeviceTrace
+ _gAVOutputContextTrace
+ _gAVOutputDeviceAuthorizationSessionTrace
+ _gAVOutputDeviceDiscoverySessionTrace
+ _gAVOutputDeviceGroupTrace
+ _gAVOutputDeviceRouteDiscovererQueue
+ _gAVOutputDeviceRouteDiscoverer_AudioVideo
+ _gAVOutputDeviceRouteDiscoverer_Screen
+ _gAVOutputDeviceTrace
+ _gAVPlatformUtilitiesTrace
+ _gAVRoutingCallbackContextRegistryTrace
+ _gAVRoutingErrorTrace
+ _gAVRoutingOperationTrace
+ _gAVRoutingPlaybackArbiterTrace
+ _gAVRoutingScheduledAudioParameters
+ _gAVRoutingSessionManagerTrace
+ _gScheduledParameterRampTrace
+ _kCFAllocatorDefault
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFCopyStringDictionaryKeyCallBacks
+ _kCFErrorDebugDescriptionKey
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kCFTypeArrayCallBacks
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kCMTimeInvalid
+ _kCMTimePositiveInfinity
+ _kCMTimeRangeInvalid
+ _kCMTimeZero
+ _kFigAudioCurvesKey_AmbienceLevel
+ _kFigAudioCurvesKey_AmbienceLoudness
+ _kFigAudioCurvesKey_DialogLevel
+ _kFigAudioCurvesKey_DialogLoudness
+ _kFigAudioCurvesKey_DialogMixBias
+ _kFigAudioCurvesKey_RecordingLoudness
+ _kFigAudioCurvesKey_RenderingStyle
+ _kFigAudioCurvesKey_Volume
+ _kFigEndPointNotification_EnhancedSiriParametersChanged
+ _kFigEndpointAuthenticationType_MFiMutualAuth
+ _kFigEndpointAuthenticationType_MFiSAP
+ _kFigEndpointBatteryLevel_Case
+ _kFigEndpointBatteryLevel_Left
+ _kFigEndpointBatteryLevel_Right
+ _kFigEndpointBatteryLevel_Single
+ _kFigEndpointCentralNotification_CarEntityHasMainAudio
+ _kFigEndpointCentralNotification_ScreenBecameAvailable
+ _kFigEndpointCentralNotification_ScreenBecameUnavailable
+ _kFigEndpointCentralNotification_iOSEntityHasMainAudio
+ _kFigEndpointCentralNotification_iOSEntityIsDoingTurnByTurnChanged
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_IsClusterLeader
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_Model
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_RouteName
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_RouteUID
+ _kFigEndpointClusterCompositionDeviceDescriptionKey_SubType
+ _kFigEndpointClusterType_HT
+ _kFigEndpointClusterType_StereoPair
+ _kFigEndpointCommChannelCreationOptionClientTypeUUID_MediaRemote
+ _kFigEndpointCommChannelCreationOption_ChannelID
+ _kFigEndpointCommChannelCreationOption_ClientTypeUUID
+ _kFigEndpointCommChannelCreationOption_ControlType
+ _kFigEndpointConfigurationPeerDescription_Identifier
+ _kFigEndpointConfigurationPeerDescription_Permissions
+ _kFigEndpointConfigurationPeerDescription_PublicKey
+ _kFigEndpointConfigurationRequest_PeersToAdd
+ _kFigEndpointConfigurationRequest_PeersToRemove
+ _kFigEndpointConfigurationResponse_PeersList
+ _kFigEndpointConfiguration_DeviceName
+ _kFigEndpointConfiguration_EnableHKAccessControl
+ _kFigEndpointConfiguration_HKAccessControlLevel
+ _kFigEndpointConfiguration_Password
+ _kFigEndpointDescriptorKey_AdvertisesHAPSupport
+ _kFigEndpointDescriptorKey_AirPlayEndpointProperties
+ _kFigEndpointDescriptorKey_AirPlaySecurity
+ _kFigEndpointDescriptorKey_AllowsHeadTrackedSpatialAudio
+ _kFigEndpointDescriptorKey_AudioRouteName
+ _kFigEndpointDescriptorKey_AudioRouteName_AirTunes
+ _kFigEndpointDescriptorKey_AudioRouteName_BluetoothLEOutput
+ _kFigEndpointDescriptorKey_AudioRouteName_CarAudioOutput
+ _kFigEndpointDescriptorKey_AudioRouteName_HDMI
+ _kFigEndpointDescriptorKey_AudioRouteName_HDMIOutput
+ _kFigEndpointDescriptorKey_AudioRouteName_Headphone
+ _kFigEndpointDescriptorKey_AudioRouteName_HeadphonesBT
+ _kFigEndpointDescriptorKey_AudioRouteName_Headset
+ _kFigEndpointDescriptorKey_AudioRouteName_HeadsetBT
+ _kFigEndpointDescriptorKey_AudioRouteName_LineOut
+ _kFigEndpointDescriptorKey_AudioRouteName_PersistentLineOut
+ _kFigEndpointDescriptorKey_AudioRouteName_Receiver
+ _kFigEndpointDescriptorKey_AudioRouteName_SPDIF
+ _kFigEndpointDescriptorKey_AudioRouteName_Speaker
+ _kFigEndpointDescriptorKey_AudioRouteName_USB
+ _kFigEndpointDescriptorKey_AudioRouteSubType
+ _kFigEndpointDescriptorKey_AudioRouteSubType_AppleTV
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ClusterGeneric
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ClusterHomeTheater
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ClusterStereoPair
+ _kFigEndpointDescriptorKey_AudioRouteSubType_FirstPartySpeaker
+ _kFigEndpointDescriptorKey_AudioRouteSubType_HomePod
+ _kFigEndpointDescriptorKey_AudioRouteSubType_Mac
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ThirdPartySetTopBox
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ThirdPartySpeaker
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ThirdPartyTV
+ _kFigEndpointDescriptorKey_AudioRouteSubType_ThirdPartyTVStick
+ _kFigEndpointDescriptorKey_AudioRouteSubType_iOS
+ _kFigEndpointDescriptorKey_BTDetails_BatteryLevelCase
+ _kFigEndpointDescriptorKey_BTDetails_BatteryLevelLeft
+ _kFigEndpointDescriptorKey_BTDetails_BatteryLevelRight
+ _kFigEndpointDescriptorKey_BTDetails_BatteryLevelSingle
+ _kFigEndpointDescriptorKey_BTDetails_EndpointType
+ _kFigEndpointDescriptorKey_BTDetails_HighQualityContentCaptureEnabled
+ _kFigEndpointDescriptorKey_BTDetails_IsBTManaged
+ _kFigEndpointDescriptorKey_BTDetails_ListeningMode
+ _kFigEndpointDescriptorKey_BTDetails_SupportedListeningModes
+ _kFigEndpointDescriptorKey_BTDetails_SupportsDoAP
+ _kFigEndpointDescriptorKey_BTDetails_SupportsHighQualityContentCapture
+ _kFigEndpointDescriptorKey_CloudLibraryIsOn
+ _kFigEndpointDescriptorKey_ClusterComposition
+ _kFigEndpointDescriptorKey_ClusterSize
+ _kFigEndpointDescriptorKey_ClusterType
+ _kFigEndpointDescriptorKey_ConversationDetectEnable
+ _kFigEndpointDescriptorKey_EndpointInfo
+ _kFigEndpointDescriptorKey_ExternalPlaybackCannotFetchMediaFromSender
+ _kFigEndpointDescriptorKey_ExternalPlaybackDoesNotShowProperUIForAudioOnlyAssets
+ _kFigEndpointDescriptorKey_ExternalPlaybackDoesNotSupportEncryptedCRABS
+ _kFigEndpointDescriptorKey_FirmwareVersion
+ _kFigEndpointDescriptorKey_GroupContainsGroupLeader
+ _kFigEndpointDescriptorKey_GroupUUID
+ _kFigEndpointDescriptorKey_HKAccessControlLevel
+ _kFigEndpointDescriptorKey_HeadTrackedSpatialAudioIsActive
+ _kFigEndpointDescriptorKey_HeadTrackedSpatialAudioMode
+ _kFigEndpointDescriptorKey_IsAppleMusicSubscriber
+ _kFigEndpointDescriptorKey_IsBluetoothShareable
+ _kFigEndpointDescriptorKey_IsClusterLeader
+ _kFigEndpointDescriptorKey_IsCurrentlyPickedOnPairedDevice
+ _kFigEndpointDescriptorKey_IsGenuineAppleAccessory
+ _kFigEndpointDescriptorKey_IsGroupLeader
+ _kFigEndpointDescriptorKey_IsGroupable
+ _kFigEndpointDescriptorKey_IsHKAccessControlEnabled
+ _kFigEndpointDescriptorKey_IsLowFidelity
+ _kFigEndpointDescriptorKey_IsMediaRemoteControllable
+ _kFigEndpointDescriptorKey_IsSilentPrimary
+ _kFigEndpointDescriptorKey_MACAddress
+ _kFigEndpointDescriptorKey_Manufacturer
+ _kFigEndpointDescriptorKey_Model
+ _kFigEndpointDescriptorKey_OtherDevicesConnected
+ _kFigEndpointDescriptorKey_OtherDevicesConnected_ModelIdentifier
+ _kFigEndpointDescriptorKey_OtherDevicesConnected_Name
+ _kFigEndpointDescriptorKey_OtherDevicesConnected_Playing
+ _kFigEndpointDescriptorKey_OtherDevicesConnected_ProductName
+ _kFigEndpointDescriptorKey_OtherDevicesConnected_UniqueID
+ _kFigEndpointDescriptorKey_PersistentGroupUUID
+ _kFigEndpointDescriptorKey_PreferredExternalRouteDetails_IsActive
+ _kFigEndpointDescriptorKey_RouteCurrentlyPicked
+ _kFigEndpointDescriptorKey_RouteHasAirPlayCloudConnectivity
+ _kFigEndpointDescriptorKey_RouteName
+ _kFigEndpointDescriptorKey_RouteSubtype
+ _kFigEndpointDescriptorKey_RouteSupportsAirPlayScreen
+ _kFigEndpointDescriptorKey_RouteSupportsAirPlayVideo
+ _kFigEndpointDescriptorKey_RouteSupportsAudio
+ _kFigEndpointDescriptorKey_RouteUID
+ _kFigEndpointDescriptorKey_SerialNumber
+ _kFigEndpointDescriptorKey_SupportsConversationDetect
+ _kFigEndpointDescriptorKey_SupportsExtendedWHAFeatures
+ _kFigEndpointDescriptorKey_SupportsHeadTrackedSpatialAudio
+ _kFigEndpointDescriptorKey_SupportsRelay
+ _kFigEndpointDescriptorKey_TightSyncBuddyNotReachable
+ _kFigEndpointDescriptorKey_TightSyncIsGroupLeader
+ _kFigEndpointDescriptorKey_TightSyncUUID
+ _kFigEndpointDescriptor_BTDetails_EndpointType_Speakers
+ _kFigEndpointDescriptor_BTDetails_EndpointType_Vehicle
+ _kFigEndpointDescriptor_ClusterType_HT
+ _kFigEndpointDescriptor_ClusterType_StereoPair
+ _kFigEndpointHIDKey_ScreenID
+ _kFigEndpointHIDKey_UUID
+ _kFigEndpointNotification_AuthenticationSucceeded
+ _kFigEndpointNotification_CarPlayTest
+ _kFigEndpointNotification_LimitedUIChanged
+ _kFigEndpointNotification_NightModeChanged
+ _kFigEndpointNotification_PerformanceReportPosted
+ _kFigEndpointNotification_SiriRequested
+ _kFigEndpointNotification_UnhandledRemoteEvent
+ _kFigEndpointNotification_VehicleInformationChanged
+ _kFigEndpointNotification_ViewAreaChanged
+ _kFigEndpointNotification_iOSUIRequested
+ _kFigEndpointProperty_AdvertisesHAPSupport
+ _kFigEndpointProperty_AirPlayEndpointProperties
+ _kFigEndpointProperty_AirPlayFromCloudSupported
+ _kFigEndpointProperty_AirPlaySecurity
+ _kFigEndpointProperty_AirPlayVideoV2Supported
+ _kFigEndpointProperty_AllowsHeadTrackedSpatialAudio
+ _kFigEndpointProperty_AlternateSiri
+ _kFigEndpointProperty_AuthenticationData
+ _kFigEndpointProperty_AuthenticationType
+ _kFigEndpointProperty_BatteryLevel
+ _kFigEndpointProperty_CarEntityIsDoingTurnByTurn
+ _kFigEndpointProperty_CarEntityIsDoingVoiceRecognition
+ _kFigEndpointProperty_CarEntityOwnsMainAudio
+ _kFigEndpointProperty_CarEntityOwnsScreen
+ _kFigEndpointProperty_CloudLibraryIsOn
+ _kFigEndpointProperty_ClusterComposition
+ _kFigEndpointProperty_ClusterSize
+ _kFigEndpointProperty_ClusterType
+ _kFigEndpointProperty_ConversationDetectEnable
+ _kFigEndpointProperty_DisplayCornerMasks
+ _kFigEndpointProperty_ExtendedFeatures
+ _kFigEndpointProperty_ExternalPlaybackCannotFetchMediaFromSender
+ _kFigEndpointProperty_ExternalPlaybackDoesNotShowProperUIForAudioOnlyAssets
+ _kFigEndpointProperty_ExternalPlaybackDoesNotSupportEncryptedCRABS
+ _kFigEndpointProperty_FirmwareVersion
+ _kFigEndpointProperty_GroupContainsGroupLeader
+ _kFigEndpointProperty_GroupUUID
+ _kFigEndpointProperty_HIDs
+ _kFigEndpointProperty_HKAccessControlLevel
+ _kFigEndpointProperty_HeadTrackedSpatialAudioIsActive
+ _kFigEndpointProperty_HeadTrackedSpatialAudioMode
+ _kFigEndpointProperty_ID
+ _kFigEndpointProperty_IsActivated
+ _kFigEndpointProperty_IsAppleMusicSubscriber
+ _kFigEndpointProperty_IsBluetoothShareable
+ _kFigEndpointProperty_IsClusterLeader
+ _kFigEndpointProperty_IsGenuineAppleAccessory
+ _kFigEndpointProperty_IsGroupLeader
+ _kFigEndpointProperty_IsGroupable
+ _kFigEndpointProperty_IsHKAccessControlEnabled
+ _kFigEndpointProperty_IsLowFidelity
+ _kFigEndpointProperty_IsURLPlaybackEnabled
+ _kFigEndpointProperty_LimitedUI
+ _kFigEndpointProperty_LimitedUIElements
+ _kFigEndpointProperty_ListeningMode
+ _kFigEndpointProperty_MACAddress
+ _kFigEndpointProperty_Manufacturer
+ _kFigEndpointProperty_MediaRemoteControllable
+ _kFigEndpointProperty_Model
+ _kFigEndpointProperty_Name
+ _kFigEndpointProperty_NightMode
+ _kFigEndpointProperty_OEMIconLabel
+ _kFigEndpointProperty_OEMIconVisible
+ _kFigEndpointProperty_OEMIcons
+ _kFigEndpointProperty_PersistentGroupUUID
+ _kFigEndpointProperty_RightHandDrive
+ _kFigEndpointProperty_ScreenInfo
+ _kFigEndpointProperty_SerialNumber
+ _kFigEndpointProperty_SilentPrimary
+ _kFigEndpointProperty_SubType
+ _kFigEndpointProperty_SupportedFeatures
+ _kFigEndpointProperty_SupportedListeningModes
+ _kFigEndpointProperty_SupportsConversationDetect
+ _kFigEndpointProperty_SupportsExtendedWHAFeatures
+ _kFigEndpointProperty_SupportsHeadTrackedSpatialAudio
+ _kFigEndpointProperty_SupportsRelay
+ _kFigEndpointProperty_TightSyncBuddyNotReachable
+ _kFigEndpointProperty_TightSyncIsGroupLeader
+ _kFigEndpointProperty_TightSyncUUID
+ _kFigEndpointProperty_TransportType
+ _kFigEndpointProperty_Type
+ _kFigEndpointProperty_VehicleInformation
+ _kFigEndpointProperty_VoiceActivationType
+ _kFigEndpointProperty_iOSEntityIsDoingTurnByTurn
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayClusterControl
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayLoggingData
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayProtocolData
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayProtocolData2
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayUpdateData
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_FitnessUIOverlay
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_MediaRemote
+ _kFigEndpointRemoteControlSessionCreationOption_ClientTypeUUID
+ _kFigEndpointRemoteControlSessionCreationOption_ClientUUID
+ _kFigEndpointRemoteControlSessionCreationOption_ControlType
+ _kFigEndpointRemoteControlSessionCreationOption_QualityOfService
+ _kFigEndpointRemoteControlSessionCreationOption_SendMessageWithoutReply
+ _kFigEndpointRemoteControlSessionCreationOption_SessionType
+ _kFigEndpointRemoteControlSessionCreationOption_StreamPriority
+ _kFigEndpointRemoteControlSessionEvent_IncomingMessage
+ _kFigEndpointRemoteControlSessionEvent_Invalidated
+ _kFigEndpointScreenInfoKey_ApplicationURL
+ _kFigEndpointScreenInfoKey_CornerMasks
+ _kFigEndpointScreenInfoKey_ID
+ _kFigEndpointScreenInfoKey_InitialApplicationURL
+ _kFigEndpointScreenInfoKey_InputCapabilities
+ _kFigEndpointScreenInfoKey_IsLimitedUI
+ _kFigEndpointScreenInfoKey_IsNightMode
+ _kFigEndpointScreenInfoKey_LimitedUIElements
+ _kFigEndpointScreenInfoKey_MaxFPS
+ _kFigEndpointScreenInfoKey_PhysicalSize
+ _kFigEndpointScreenInfoKey_PixelSize
+ _kFigEndpointScreenInfoKey_PrimaryInputDevice
+ _kFigEndpointScreenInfoKey_SquarePixelSize
+ _kFigEndpointScreenInfoKey_ViewAreas
+ _kFigEndpointScreenInfoKey_ViewHeightScaleFactor
+ _kFigEndpointScreenInfoViewAreaKey_SafeArea
+ _kFigEndpointScreenInfoViewAreaKey_StatusBarEdge
+ _kFigEndpointScreenInfoViewAreaKey_ViewArea
+ _kFigEndpointScreenInfoViewAreaKey_ViewAreaSupportsFocusTransfer
+ _kFigEndpointScreenInfoViewAreaKey_ViewAreaTransitionControl
+ _kFigEndpointSecondDisplayMode
+ _kFigEndpointSendCommand_CommandType_Configure
+ _kFigEndpointSendCommand_CommandType_SetMRInfo
+ _kFigEndpointSendCommand_CommandType_SetSecondDisplayMode
+ _kFigEndpointSendCommand_Param_MRInfo
+ _kFigEndpointSiriRequestedAction_ButtonDown
+ _kFigEndpointSiriRequestedAction_ButtonUp
+ _kFigEndpointSiriRequestedAction_Prewarm
+ _kFigEndpointSiriRequestedKey_Action
+ _kFigEndpointSiriRequestedKey_Timestamp
+ _kFigEndpointSubType_AppleTV
+ _kFigEndpointSubType_ClusterGeneric
+ _kFigEndpointSubType_ClusterHomeTheater
+ _kFigEndpointSubType_ClusterStereoPair
+ _kFigEndpointSubType_HomePod
+ _kFigEndpointSubType_Mac
+ _kFigEndpointSubType_ThirdPartySetTopBox
+ _kFigEndpointSubType_ThirdPartySpeaker
+ _kFigEndpointSubType_ThirdPartyTV
+ _kFigEndpointSubType_ThirdPartyTVStick
+ _kFigEndpointSubType_iOS
+ _kFigEndpointSubType_visionOS
+ _kFigEndpointTransportType_AWDL
+ _kFigEndpointTransportType_Ethernet
+ _kFigEndpointTransportType_USB
+ _kFigEndpointTransportType_WiFi
+ _kFigEndpointType_AirPlay
+ _kFigEndpointType_Bluetooth
+ _kFigEndpointType_CarPlay
+ _kFigEndpointUIAgentNotificationPayloadKey_ShowAuthPromptInfo
+ _kFigEndpointUIAgentNotificationPayloadKey_ShowErrorPromptInfo
+ _kFigEndpointUIAgentNotification_FinishedWithPrompt
+ _kFigEndpointUIAgentNotification_ServerConnectionDied
+ _kFigEndpointUIAgentNotification_ShowAuthPrompt
+ _kFigEndpointUIAgentNotification_ShowErrorPrompt
+ _kFigEndpointUIAgentPromptInfo_PINMode
+ _kFigEndpointUIAgentPromptInfo_Reason
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorAuthenticationFailed
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorHijackFailed
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorInfraRelayFailed2G
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorInfraRelayFailedMultiDFS
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorReceiverIsOffline
+ _kFigEndpointUIAgentPromptInfo_ReasonErrorUnauthorizedNotHomeUser
+ _kFigEndpointUIAgentPromptInfo_ReasonInitialPrompt
+ _kFigEndpointUIAgentPromptInfo_ReasonPromptForIncorrectAuthInfo
+ _kFigEndpointUIAgentPromptInfo_ReasonStartErrorLowSignal
+ _kFigEndpointUIAgentPromptInfo_RouteDescriptor
+ _kFigEndpointUIAgentPromptInfo_UniqueID
+ _kFigEndpointUnhandledRemoteEventKey_CommandParams
+ _kFigEndpointUnhandledRemoteEventKey_CommandType
+ _kFigEndpointVehicleInformationChangedKey_NewVehicleInformation
+ _kFigEndpointVehicleInformationEntry_ETC
+ _kFigEndpointVehicleInformationEntry_NavigationAidedDriving
+ _kFigEndpointiOSUIRequestedKey_ApplicationURL
+ _kFigEndpointiOSUIRequestedKey_UUID
+ _kFigPlaybackItemAudioCurveVolumeRampStyle_EqualPower
+ _kFigPlaybackItemAudioCurveVolumeRampStyle_Linear
+ _kFigRouteDiscovererCreationOption_DiscovererType
+ _kFigRouteDiscovererDiscoveryMode_AirPlayInfraOnly
+ _kFigRouteDiscovererDiscoveryMode_DetailedDiscovery
+ _kFigRouteDiscovererDiscoveryMode_None
+ _kFigRouteDiscovererDiscoveryMode_PresenceScan
+ _kFigRouteDiscovererNotification_AvailableRoutesChanged
+ _kFigRouteDiscovererNotification_EndpointDescriptorChanged
+ _kFigRouteDiscovererNotification_RoutePresentChanged
+ _kFigRouteDiscovererNotification_ServerConnectionDied
+ _kFigRouteDiscovererProperty_AudioSessionID
+ _kFigRouteDiscovererProperty_AvailableRouteDescriptors
+ _kFigRouteDiscovererProperty_AvailableRoutes
+ _kFigRouteDiscovererProperty_BluetoothRoutesOnly
+ _kFigRouteDiscovererProperty_DiscoveryMode
+ _kFigRouteDiscovererProperty_OnBehalfOf
+ _kFigRouteDiscovererProperty_UserSelectionAvailable
+ _kFigRoutingContextCreateOption_AvoidAuthPrompt
+ _kFigRoutingContextCreateOption_ContextType
+ _kFigRoutingContextCreateOption_ContextUUID
+ _kFigRoutingContextCreateOption_RemoteGroupID
+ _kFigRoutingContextNotificationPayloadKey_CommChannelUUID
+ _kFigRoutingContextNotificationPayloadKey_ConfigUpdateReasonEndedFailed_CurrentRoutes
+ _kFigRoutingContextNotificationPayloadKey_ConfigUpdateReasonEndedFailed_DeviceID
+ _kFigRoutingContextNotificationPayloadKey_ConfigUpdateReasonEndedFailed_ErrorString
+ _kFigRoutingContextNotificationPayloadKey_Data
+ _kFigRoutingContextNotificationPayloadKey_DeviceID
+ _kFigRoutingContextNotificationPayloadKey_RouteChangeEndedReason
+ _kFigRoutingContextNotificationPayloadKey_RouteChangeID
+ _kFigRoutingContextNotificationPayloadKey_RouteConfigUpdateID
+ _kFigRoutingContextNotificationPayloadKey_RouteConfigUpdateInitiator
+ _kFigRoutingContextNotificationPayloadKey_RouteConfigUpdateReason
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedApplicationStateChanged
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedBottomUpRouteChange
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedFailed
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedFailed_IdleDisconnect
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedNoOp
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedSuccess
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedUnauthorized
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedUnauthorizedNoPrompt
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndedUserCancelled
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndpointDescriptorChanged
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndpointDescriptorChanged_RouteDescriptor
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndpointDescriptorChanged_RouteNotification
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonEndpointDescriptorChanged_RoutePayload
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonGroupDevicesChanged
+ _kFigRoutingContextNotificationPayloadValue_ConfigUpdateReasonStarted
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonAuthInfoFailed
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonClientRequest
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonFailed
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonSuccess
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonUnauthorizedNoPrompt
+ _kFigRoutingContextNotificationPayloadValue_EndedReasonUserCancelled
+ _kFigRoutingContextNotification_CommChannelDidClose
+ _kFigRoutingContextNotification_CurrentGroupConfigurationChanged
+ _kFigRoutingContextNotification_CurrentRouteChanged
+ _kFigRoutingContextNotification_DidReceiveData
+ _kFigRoutingContextNotification_PredictedSelectedRouteDescriptorChanged
+ _kFigRoutingContextNotification_RemoteControlChannelAvailabilityChanged
+ _kFigRoutingContextNotification_RouteChangeEnded
+ _kFigRoutingContextNotification_RouteChangeStarted
+ _kFigRoutingContextNotification_RouteConfigUpdated
+ _kFigRoutingContextNotification_RouteDescriptionEvent
+ _kFigRoutingContextNotification_ServerConnectionDied
+ _kFigRoutingContextNotification_SystemPickerVideoRouteChanged
+ _kFigRoutingContextProperty_AssociatedAudioDevice
+ _kFigRoutingContextProperty_ContextType
+ _kFigRoutingContextProperty_ContextUUID
+ _kFigRoutingContextProperty_RemoteControlChannelAvailable
+ _kFigRoutingContextProperty_SupportsBluetoothMultiDeviceRouting
+ _kFigRoutingContextProperty_SupportsWHAMultiDeviceRouting
+ _kFigRoutingContextRemoveRouteOptionKey_ContinuePlaybackWhenLastRouteIsRemoved
+ _kFigRoutingContextSelectRouteOptionKey_AuthInfo
+ _kFigRoutingContextSelectRouteOptionKey_AvoidAuthPrompt
+ _kFigRoutingContextSelectRouteOptionKey_ClientCorrelationID
+ _kFigRoutingContextSelectRouteOptionKey_ClientPID
+ _kFigRoutingContextSelectRouteOptionKey_ClientRouteRequestID
+ _kFigRoutingContextSelectRouteOptionKey_CrossfadePlayback
+ _kFigRoutingContextSelectRouteOptionKey_Initiator
+ _kFigRoutingContextSelectRouteOptionKey_SilentSender
+ _kFigRoutingSessionDestinationKey_Probability
+ _kFigRoutingSessionDestinationKey_ProvidesExternalVideoPlayback
+ _kFigRoutingSessionDestinationKey_RouteDescriptors
+ _kFigRoutingSessionManagerNotification_CurrentSessionChanged
+ _kFigRoutingSessionManagerNotification_LikelyDestinationsChanged
+ _kFigRoutingSessionProperty_EstablishedAutomaticallyFromLikelyDestination
+ _kFigVolumeControllerEndpointVolumeKey_EndpointID
+ _kFigVolumeControllerMasterVolumeKey_RoutingContextUUID
+ _kFigVolumeControllerNotification_CanSetEndpointVolumeDidChange
+ _kFigVolumeControllerNotification_CanSetMasterVolumeDidChange
+ _kFigVolumeControllerNotification_CanUseForRoutingContextDidChange
+ _kFigVolumeControllerNotification_EndpointMutedByUserDidChange
+ _kFigVolumeControllerNotification_EndpointVolumeControlTypeDidChange
+ _kFigVolumeControllerNotification_EndpointVolumeDidChange
+ _kFigVolumeControllerNotification_MasterVolumeControlTypeDidChange
+ _kFigVolumeControllerNotification_MasterVolumeDidChange
+ _kFigVolumeControllerNotification_MuteControlSupportDidChange
+ _kFigVolumeControllerNotification_MuteControlSupportForRoutingContextDidChange
+ _kFigVolumeControllerNotification_MutedByUserOnRoutingContextDidChange
+ _kFigVolumeControllerNotification_RoomVolumeDidChange
+ _kFigVolumeControllerRoomVolumeKey_RoomID
+ _notificationDispatcherForCMNotificationCenter:.sSharedDispatcher
+ _notificationDispatcherForCMNotificationCenter:.sSharedDispatcherOnce
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_exception_throw
+ _objc_msgSend$CMNotificationCenter
+ _objc_msgSend$CMTimeMappingValue
+ _objc_msgSend$CMTimeRangeValue
+ _objc_msgSend$CMTimeValue
+ _objc_msgSend$HAPConformance
+ _objc_msgSend$ID
+ _objc_msgSend$MFiCertificateSerialNumber
+ _objc_msgSend$OEMIconLabel
+ _objc_msgSend$OEMIconVisible
+ _objc_msgSend$OEMIcons
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_addTrackedParticipant:
+ _objc_msgSend$_additionalFigRepresentationObjects
+ _objc_msgSend$_allTrackedParticipants
+ _objc_msgSend$_applicationSupportPath
+ _objc_msgSend$_audioCurveOfClass:
+ _objc_msgSend$_audioVolumeCurve
+ _objc_msgSend$_availableRoutesChanged
+ _objc_msgSend$_balanceMonitoringIsFinishedSemaphore
+ _objc_msgSend$_canMuteDidChangeForEndpointWithID:
+ _objc_msgSend$_canMuteDidChangeForRoutingContextWithID:
+ _objc_msgSend$_canQueryOutputDeviceDescriptionsAndReturnCurrentValue:
+ _objc_msgSend$_canSetEndpointVolumeDidChangeForEndpointWithID:
+ _objc_msgSend$_canSetMasterVolumeDidChangeForRoutingContextWithID:
+ _objc_msgSend$_canUseForRoutingContextDidChangeForRoutingContextWIthID:
+ _objc_msgSend$_carPlayTestNotification:
+ _objc_msgSend$_copyAndRemoveObserverForWeakReferenceToListener:callback:name:object:
+ _objc_msgSend$_createSelectRouteOptionsForSetInputDeviceOptions:
+ _objc_msgSend$_createSelectRouteOptionsForSetOutputDeviceOptions:
+ _objc_msgSend$_createUserPreferredRouteModificationDictionary:
+ _objc_msgSend$_currentRouteChanged
+ _objc_msgSend$_defaultAdditionalFigRepresentationObjects
+ _objc_msgSend$_didCloseCommChannelWithUUID:forDeviceWithID:
+ _objc_msgSend$_didCloseCommunicationChannel
+ _objc_msgSend$_didReceiveData:
+ _objc_msgSend$_didReceiveData:fromCommChannelUUID:
+ _objc_msgSend$_didReceiveData:fromDeviceWithID:fromChannelWithUUID:
+ _objc_msgSend$_endpointDescriptorChanged
+ _objc_msgSend$_endpointVolumeControlTypeDidChangeForEndpointWithID:
+ _objc_msgSend$_externalPlaybackIsActiveForParticipant:
+ _objc_msgSend$_externalPlaybackPriorityForParticipant:
+ _objc_msgSend$_figEndpointPropertyValueForKey:
+ _objc_msgSend$_finishedWithPrompt
+ _objc_msgSend$_frecentsContainerPath
+ _objc_msgSend$_frecentsFilePath
+ _objc_msgSend$_frecentsReaderAfterMigrationIfNecessary
+ _objc_msgSend$_frecentsWriter
+ _objc_msgSend$_getFigEndpointTypeFromAVOutputDeviceType:
+ _objc_msgSend$_getRampOfClass:forTime:timeRange:
+ _objc_msgSend$_groupConfigurationChanged
+ _objc_msgSend$_handleFigEndpointEvent:payload:
+ _objc_msgSend$_handleRouteDescriptionEvent:payload:
+ _objc_msgSend$_iOSUIRequestedNotification:
+ _objc_msgSend$_initializeIfNeededAndGetSystemRemotePool
+ _objc_msgSend$_interpolatedValueAtTime:
+ _objc_msgSend$_isScheduledRampClass:
+ _objc_msgSend$_loadOutputDevices
+ _objc_msgSend$_makeRampWithTruncatedTimeRange:endValue:
+ _objc_msgSend$_masterVolumeControlTypeDidChangeForRoutingContextWithID:
+ _objc_msgSend$_masterVolumeDidChangeForRoutingContextWithID:
+ _objc_msgSend$_migrateFrecentsFromCFPreferencesToFrecentsFilePath:
+ _objc_msgSend$_monitoredObject
+ _objc_msgSend$_muteDidChangeForRoutingContextWithID:
+ _objc_msgSend$_mutedDidChangeForEndpointWithID:
+ _objc_msgSend$_notifyCurrentRequestOfTerminalStatus:error:
+ _objc_msgSend$_parameterRampMode
+ _objc_msgSend$_predictedSelectedRouteDescriptorChanged
+ _objc_msgSend$_ramps
+ _objc_msgSend$_rampsOfClass:
+ _objc_msgSend$_registerForObjectNotifications
+ _objc_msgSend$_remoteControlChannelAvailabilityChanged
+ _objc_msgSend$_removeTrackedParticipant:
+ _objc_msgSend$_routeChangeComplete
+ _objc_msgSend$_routeChangeEndedWithID:reason:
+ _objc_msgSend$_routeChangeStartedWithID:
+ _objc_msgSend$_routeChangeWithID:endedWithReason:
+ _objc_msgSend$_routeConfigUpdateEndedWithID:reason:
+ _objc_msgSend$_routeConfigUpdateStartedWithID:
+ _objc_msgSend$_routeConfigUpdateWithID:endedWithReason:
+ _objc_msgSend$_routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:
+ _objc_msgSend$_routeDescriptionDidChange:
+ _objc_msgSend$_routePresentChanged
+ _objc_msgSend$_serverConnectionDied
+ _objc_msgSend$_serverDied
+ _objc_msgSend$_setDefaultExternalPlaybackPriorityForParticipant:
+ _objc_msgSend$_setDefaultNonMixableAudioPriorityForParticipant:
+ _objc_msgSend$_setExternalPlaybackPriority:forParticipant:
+ _objc_msgSend$_setNonMixableAudioPriority:forParticipant:
+ _objc_msgSend$_setRamp:
+ _objc_msgSend$_setRamps:
+ _objc_msgSend$_setResultIfNotAlreadySet:
+ _objc_msgSend$_setResultInputIfNotAlreadySet:
+ _objc_msgSend$_setStatus:
+ _objc_msgSend$_setStatus:cancellationReason:
+ _objc_msgSend$_setStatus:error:resultingStatus:failureReason:
+ _objc_msgSend$_setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:
+ _objc_msgSend$_setWeakRefToPreferredParticipantForExternalPlayback:
+ _objc_msgSend$_setWeakRefToPreferredParticipantForNonMixableAudio:
+ _objc_msgSend$_shouldHideAirPlayInfoDuringDemo
+ _objc_msgSend$_showAuthPromptWithUniqueID:routeDescriptor:pinMode:reason:
+ _objc_msgSend$_showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:
+ _objc_msgSend$_signalMonitoringIsFinishedIfNeeded
+ _objc_msgSend$_siriRequestedNotification:
+ _objc_msgSend$_startNewRequest:impl:
+ _objc_msgSend$_systemPickerVideoRouteChanged
+ _objc_msgSend$_unhandledRemoteCommandNotification:
+ _objc_msgSend$_unregisterForObjectNotifications
+ _objc_msgSend$_updateExternalPlaybackStatusNotificationListenerToParticipant:
+ _objc_msgSend$_updatePreferredParticipantForExternalPlaybackFrom:toParticipant:checkingAllParticipants:
+ _objc_msgSend$_updatePreferredParticipantForNonMixableAudioRouteFrom:toParticipant:checkingAllParticipants:
+ _objc_msgSend$_vehicleInformationDidChange:
+ _objc_msgSend$_volumeCurveAsString
+ _objc_msgSend$_volumeCurveKeysForScheduledRampClassNames
+ _objc_msgSend$_volumeDidChangeForEndpointWithID:
+ _objc_msgSend$_volumeForEndpointDidChange:forRoomID:
+ _objc_msgSend$_waitUntilFinishedIfNeeded
+ _objc_msgSend$_web_errorWithDomain:code:URL:
+ _objc_msgSend$_withEndpoint:
+ _objc_msgSend$activatedDeviceClusterMembersDidChangeVolume:forRoomID:
+ _objc_msgSend$addDependency:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addListenerWithWeakReference:callback:name:object:flags:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$addOperation:
+ _objc_msgSend$addOutputDevice:options:completionHandler:
+ _objc_msgSend$addOutputDevice:withOptions:completionHandler:
+ _objc_msgSend$addOutputDevice:withOptions:toRoutingContext:completionHandler:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$addSharedAudioOutputContextImpl
+ _objc_msgSend$airPlayProperties
+ _objc_msgSend$allDevices
+ _objc_msgSend$allKeys
+ _objc_msgSend$allLikelyDestinations
+ _objc_msgSend$allObjects
+ _objc_msgSend$allSharedAudioOutputContextImpls
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowsHeadTrackedSpatialAudio
+ _objc_msgSend$allowsKeyedCoding
+ _objc_msgSend$alternateTransportType
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$arrayByApplyingDifference:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attachDepartureAnnouncingObjectMonitorToObject:monitoringObject:
+ _objc_msgSend$audioSessionId
+ _objc_msgSend$authenticationType
+ _objc_msgSend$authorizationTokenType
+ _objc_msgSend$automaticallyAllowsConnectionsFromPeersInHomeGroup
+ _objc_msgSend$auxiliaryOutputContext
+ _objc_msgSend$availableBluetoothListeningModes
+ _objc_msgSend$availableInputDevices
+ _objc_msgSend$availableOutputDevicesObject
+ _objc_msgSend$batteryLevel
+ _objc_msgSend$boolValue
+ _objc_msgSend$borrowScreenForClient:reason:
+ _objc_msgSend$boundsAdjustedFloatValue:
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$cachedDiscoveryEnabled
+ _objc_msgSend$canAccessAppleMusic
+ _objc_msgSend$canAccessRemoteAssets
+ _objc_msgSend$canAccessiCloudMusicLibrary
+ _objc_msgSend$canBeGroupLeader
+ _objc_msgSend$canBeGrouped
+ _objc_msgSend$canCommunicateWithAllLogicalDeviceMembers
+ _objc_msgSend$canFetchMediaDataFromSender
+ _objc_msgSend$canMute
+ _objc_msgSend$canPlayEncryptedProgressiveDownloadAssets
+ _objc_msgSend$canRelayCommunicationChannel
+ _objc_msgSend$canSetVolume
+ _objc_msgSend$cancel
+ _objc_msgSend$cancellationReason
+ _objc_msgSend$carOwnsMainAudio
+ _objc_msgSend$carOwnsScreen
+ _objc_msgSend$caseBatteryLevel
+ _objc_msgSend$changeToTerminalStatusBasedOnInputRouteChangeEndedReason:
+ _objc_msgSend$changeToTerminalStatusBasedOnInputRouteConfigUpdatedReason:
+ _objc_msgSend$changeToTerminalStatusBasedOnRouteChangeEndedReason:
+ _objc_msgSend$changeToTerminalStatusBasedOnRouteConfigUpdatedReason:
+ _objc_msgSend$charValue
+ _objc_msgSend$clearUserPreferredInputDevice:error:
+ _objc_msgSend$close
+ _objc_msgSend$clusterID
+ _objc_msgSend$clusterType
+ _objc_msgSend$clusteredDeviceDescriptions
+ _objc_msgSend$code
+ _objc_msgSend$commChannelUUID
+ _objc_msgSend$commChannelUUIDCommunicationChannelManagerCreator
+ _objc_msgSend$communicationChannel:didReceiveData:
+ _objc_msgSend$communicationChannelDelegate
+ _objc_msgSend$communicationChannelDidClose:
+ _objc_msgSend$communicationChannelImpl:didReceiveData:
+ _objc_msgSend$communicationChannelImplDidClose:
+ _objc_msgSend$communicationChannelManager:didCloseCommunicationChannel:
+ _objc_msgSend$communicationChannelManager:didReceiveData:fromCommunicationChannel:
+ _objc_msgSend$completionBlock
+ _objc_msgSend$completionHandler
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$configureUsingBlock:options:completionHandler:
+ _objc_msgSend$configuredClusterSize
+ _objc_msgSend$connectedPairedDevices
+ _objc_msgSend$contextID
+ _objc_msgSend$copy
+ _objc_msgSend$copyAllAudioContexts:
+ _objc_msgSend$copyContextForUUIDWithAllocator:options:context:
+ _objc_msgSend$copyDefaultContextWithAllocator:options:context:
+ _objc_msgSend$copyDisplayMenuVideoContextWithAllocator:options:context:
+ _objc_msgSend$copySharedEndpointUIAgent
+ _objc_msgSend$copySystemAudioContextWithAllocator:options:context:
+ _objc_msgSend$copySystemAudioInputContextWithAllocator:options:context:
+ _objc_msgSend$copySystemMirroringContextWithAllocator:options:context:
+ _objc_msgSend$copySystemMusicContextWithAllocator:options:context:
+ _objc_msgSend$copySystemRemoteDisplayContextWithAllocator:options:context:
+ _objc_msgSend$copySystemRemotePoolContextWithAllocator:options:context:
+ _objc_msgSend$copySystemVideoRoutingContext
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$createAudioContextWithAllocator:options:context:
+ _objc_msgSend$createControlChannelOnlyContextWithAllocator:options:context:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createPerAppSecondDisplayContextWithAllocator:options:context:
+ _objc_msgSend$createRemoteMusicControllerContextWithAllocator:options:context:
+ _objc_msgSend$createRouteDiscovererWithAllocator:options:
+ _objc_msgSend$createVideoContextWithAllocator:options:context:
+ _objc_msgSend$currentBluetoothListeningMode
+ _objc_msgSend$currentPlatformIdentifier
+ _objc_msgSend$currentRoutingSession
+ _objc_msgSend$currentScreenViewAreaForScreenID:
+ _objc_msgSend$data
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$decodeCMTimeForKey:
+ _objc_msgSend$decodeCMTimeMappingForKey:
+ _objc_msgSend$decodeCMTimeRangeForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$decreaseVolumeByCount:
+ _objc_msgSend$defaultCommunicationChannelManagerCreator
+ _objc_msgSend$defaultFloatValue
+ _objc_msgSend$defaultFrecentsReader
+ _objc_msgSend$defaultFrecentsWriter
+ _objc_msgSend$defaultInputContextImplClass
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultOutputContextImplClass
+ _objc_msgSend$defaultQueue
+ _objc_msgSend$defaultSharedOutputContextImpl
+ _objc_msgSend$defaultValue
+ _objc_msgSend$dependencies
+ _objc_msgSend$description
+ _objc_msgSend$destination
+ _objc_msgSend$deviceFeatures
+ _objc_msgSend$deviceID
+ _objc_msgSend$deviceIDs
+ _objc_msgSend$deviceName
+ _objc_msgSend$devicePresenceDetected
+ _objc_msgSend$deviceSubType
+ _objc_msgSend$deviceType
+ _objc_msgSend$devicesType
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$didCloseCommChannelUUID:
+ _objc_msgSend$didEnterTerminalState
+ _objc_msgSend$discoveryMode
+ _objc_msgSend$displayCornerMasks
+ _objc_msgSend$domain
+ _objc_msgSend$doubleValue
+ _objc_msgSend$electronicTollCollection
+ _objc_msgSend$encodeCMTime:forKey:
+ _objc_msgSend$encodeCMTimeMapping:forKey:
+ _objc_msgSend$encodeCMTimeRange:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endFloatValue
+ _objc_msgSend$endValue
+ _objc_msgSend$endVolume
+ _objc_msgSend$enqueueOperation:
+ _objc_msgSend$enterTerminalStatus:error:
+ _objc_msgSend$error
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$establishedAutomaticallyFromLikelyDestination
+ _objc_msgSend$evaluateDependenciesAndMarkAsExecuting
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$externalPlaybackIsActive
+ _objc_msgSend$externalPlaybackPriority
+ _objc_msgSend$fallbackInputDevice
+ _objc_msgSend$figEndpoint
+ _objc_msgSend$figEndpointOutputDeviceImpl
+ _objc_msgSend$figRoutingContext
+ _objc_msgSend$finalConfiguration
+ _objc_msgSend$firmwareVersion
+ _objc_msgSend$firstObject
+ _objc_msgSend$floatValue
+ _objc_msgSend$frecencyInfoForDeviceWithID:
+ _objc_msgSend$frecencyScore
+ _objc_msgSend$frecencyScoreForDeviceID:
+ _objc_msgSend$getApplicationProcessID:
+ _objc_msgSend$getValue:
+ _objc_msgSend$getVolumeRampForTime:startVolume:endVolume:timeRange:rampMode:
+ _objc_msgSend$groupContainsGroupLeader
+ _objc_msgSend$groupID
+ _objc_msgSend$groupLeader
+ _objc_msgSend$hasAdministratorPrivileges
+ _objc_msgSend$headTrackedSpatialAudioMode
+ _objc_msgSend$iTunesAudioContext
+ _objc_msgSend$identifyingMACAddress
+ _objc_msgSend$impl
+ _objc_msgSend$implEventListener
+ _objc_msgSend$increaseVolumeByCount:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$indexSet
+ _objc_msgSend$indexSetWithIndex:
+ _objc_msgSend$init
+ _objc_msgSend$initForUsingRouteConfigUpdatedNotification:
+ _objc_msgSend$initWithAvailableFigEndpoints:
+ _objc_msgSend$initWithCMNotificationCenter:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCompletionHandler:
+ _objc_msgSend$initWithCompletionHandler:outputDevices:figRoutingContext:
+ _objc_msgSend$initWithDeviceFeatures:
+ _objc_msgSend$initWithDeviceID:
+ _objc_msgSend$initWithDeviceID:channelUUID:outputContext:
+ _objc_msgSend$initWithDeviceID:deviceName:deviceSubType:isClusterLeader:modelID:
+ _objc_msgSend$initWithDict:
+ _objc_msgSend$initWithEndpoint:
+ _objc_msgSend$initWithEndpoint:client:reason:
+ _objc_msgSend$initWithEndpointUIAgent:
+ _objc_msgSend$initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:
+ _objc_msgSend$initWithFigEndpointUIAgent:
+ _objc_msgSend$initWithFigRouteConfigUpdatedReason:metrics:
+ _objc_msgSend$initWithFigRouteDiscovererCreator:
+ _objc_msgSend$initWithFigRoutingContext:routingContextReplacementBlock:
+ _objc_msgSend$initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:
+ _objc_msgSend$initWithFigRoutingContextCreator:
+ _objc_msgSend$initWithFigRoutingSession:
+ _objc_msgSend$initWithFigRoutingSessionDestination:
+ _objc_msgSend$initWithFigRoutingSessionManager:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithFrecentsFilePath:
+ _objc_msgSend$initWithFrecentsFilePath:error:
+ _objc_msgSend$initWithID:outputDevice:authorizationTokenType:
+ _objc_msgSend$initWithID:publicKey:hasAdministratorPrivileges:
+ _objc_msgSend$initWithInputContextImpl:
+ _objc_msgSend$initWithInputDeviceDiscoverySessionImpl:
+ _objc_msgSend$initWithInputDeviceImpl:
+ _objc_msgSend$initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:
+ _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
+ _objc_msgSend$initWithMonitoringObject:
+ _objc_msgSend$initWithName:ID:modelID:playing:productName:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithObjectsAndKeys:
+ _objc_msgSend$initWithOutputContextCommunicationChannelImpl:
+ _objc_msgSend$initWithOutputContextImpl:
+ _objc_msgSend$initWithOutputContextManagerImpl:
+ _objc_msgSend$initWithOutputDeviceAuthorizationRequestImpl:
+ _objc_msgSend$initWithOutputDeviceAuthorizationSessionImpl:
+ _objc_msgSend$initWithOutputDeviceCommunicationChannelImpl:
+ _objc_msgSend$initWithOutputDeviceDiscoverySessionAvailableOutputDevicesImpl:
+ _objc_msgSend$initWithOutputDeviceDiscoverySessionImpl:
+ _objc_msgSend$initWithOutputDeviceImpl:commChannelManager:
+ _objc_msgSend$initWithPropertyList:
+ _objc_msgSend$initWithReferencedObject:
+ _objc_msgSend$initWithRemoteControlSession:
+ _objc_msgSend$initWithRouteDescriptor:routeDiscoverer:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:
+ _objc_msgSend$initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:
+ _objc_msgSend$initWithRouteDescriptors:routeDiscoverer:
+ _objc_msgSend$initWithRouteDiscovererFactory:
+ _objc_msgSend$initWithRoutingContext:
+ _objc_msgSend$initWithRoutingContext:commChannelUUID:
+ _objc_msgSend$initWithRoutingContext:configuratorBlock:
+ _objc_msgSend$initWithRoutingContext:routeChangeID:routeChangeBlock:isInputContextOperation:
+ _objc_msgSend$initWithRoutingContext:successNotification:routeChangeBlock:isInputContextOperation:
+ _objc_msgSend$initWithRoutingContextComandResponse:
+ _objc_msgSend$initWithRoutingContextUUID:type:
+ _objc_msgSend$initWithStartValue:endValue:timeRange:
+ _objc_msgSend$initWithStartVolume:endVolume:timeRange:rampMode:
+ _objc_msgSend$initWithUUID:screenUUID:endpoint:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:
+ _objc_msgSend$initWithWeakReferenceToListener:callback:name:object:
+ _objc_msgSend$inputContextDidChangeApplicationProcessID:
+ _objc_msgSend$inputContextImpl:didChangeInputDeviceWithInitiator:
+ _objc_msgSend$inputContextImpl:didExpireWithReplacement:
+ _objc_msgSend$inputContextImpl:didInitiateDestinationChange:
+ _objc_msgSend$inputContextImplForID:type:
+ _objc_msgSend$inputContextType
+ _objc_msgSend$inputDevice
+ _objc_msgSend$inputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:
+ _objc_msgSend$inputDeviceDiscoverySessionImpl:didExpireWithReplacement:
+ _objc_msgSend$inputDeviceDiscoverySessionImplDidChangeAvailableInputDevices:
+ _objc_msgSend$inputDeviceWithRouteDescriptor:routeDiscoverer:
+ _objc_msgSend$inputDeviceWithRouteDescriptor:withRoutingContext:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$isActivated
+ _objc_msgSend$isActivatedForContinuityScreen
+ _objc_msgSend$isAppleAccessory
+ _objc_msgSend$isCached
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isCarPlayVideoActive
+ _objc_msgSend$isCarPlayVideoAllowed
+ _objc_msgSend$isClusterLeader
+ _objc_msgSend$isConversationDetectionEnabled
+ _objc_msgSend$isEligibleToBePredictedOutputDevice
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isFinished
+ _objc_msgSend$isGroupLeader
+ _objc_msgSend$isHeadTrackedSpatialAudioActive
+ _objc_msgSend$isHighQualityContentCaptureEnabled
+ _objc_msgSend$isInEar
+ _objc_msgSend$isInUseByPairedDevice
+ _objc_msgSend$isLogicalDeviceLeader
+ _objc_msgSend$isMuted
+ _objc_msgSend$isNightModeSupported
+ _objc_msgSend$lastObject
+ _objc_msgSend$leftBatteryLevel
+ _objc_msgSend$length
+ _objc_msgSend$likelyExternalDestinations
+ _objc_msgSend$limitedUI
+ _objc_msgSend$limitedUIElements
+ _objc_msgSend$listenerKeyWithWeakReferenceToListener:callback:name:object:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedStandardCompare:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$lock
+ _objc_msgSend$logicalDeviceID
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$manufacturer
+ _objc_msgSend$markAsCancelled
+ _objc_msgSend$markAsCancelledWithReason:
+ _objc_msgSend$markAsCompleted
+ _objc_msgSend$markAsFailed
+ _objc_msgSend$markAsFailedWithError:
+ _objc_msgSend$markAsFinished
+ _objc_msgSend$markAsInProgress
+ _objc_msgSend$markEventAsCompleted
+ _objc_msgSend$mediaSessionStatus
+ _objc_msgSend$modelID
+ _objc_msgSend$modificationMetrics
+ _objc_msgSend$monitoredObjectHasDeparted
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$navigationAidedDriving
+ _objc_msgSend$nightMode
+ _objc_msgSend$nonMixableAudioPriority
+ _objc_msgSend$notificationDispatcherForCMNotificationCenter:
+ _objc_msgSend$notificationWithName:object:userInfo:
+ _objc_msgSend$numberOfKeysToBeSet
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objCType
+ _objc_msgSend$object
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$onlyAllowsConnectionsFromPeersInHomeGroup
+ _objc_msgSend$onlyDiscoversBluetoothDevices
+ _objc_msgSend$opaqueSessionID
+ _objc_msgSend$openCommunicationChannelToDestination:options:completionHandler:
+ _objc_msgSend$openCommunicationChannelWithOptions:error:
+ _objc_msgSend$operations
+ _objc_msgSend$otherDevices
+ _objc_msgSend$outgoingCommunicationChannel
+ _objc_msgSend$outputContext:didCloseCommunicationChannel:
+ _objc_msgSend$outputContext:didReceiveData:fromCommunicationChannel:
+ _objc_msgSend$outputContextDidChangeApplicationProcessID:
+ _objc_msgSend$outputContextExistsWithRemoteOutputDevice
+ _objc_msgSend$outputContextForContextID:
+ _objc_msgSend$outputContextForControllingOutputDeviceGroupWithID:options:
+ _objc_msgSend$outputContextImpl:didChangeOutputDeviceWithInitiator:
+ _objc_msgSend$outputContextImpl:didChangeOutputDevicesWithInitiator:reason:deviceID:previousDeviceIDs:
+ _objc_msgSend$outputContextImpl:didCloseCommunicationChannel:
+ _objc_msgSend$outputContextImpl:didExpireWithReplacement:
+ _objc_msgSend$outputContextImpl:didInitiateDestinationChange:
+ _objc_msgSend$outputContextImpl:didReceiveData:fromCommunicationChannel:
+ _objc_msgSend$outputContextImplDidChangeCanMute:
+ _objc_msgSend$outputContextImplDidChangeCanSetVolume:
+ _objc_msgSend$outputContextImplDidChangeGlobalOutputDeviceConfiguration:
+ _objc_msgSend$outputContextImplDidChangeMute:
+ _objc_msgSend$outputContextImplDidChangePredictedOutputDevice:
+ _objc_msgSend$outputContextImplDidChangeProvidesControlForAllVolumeFeatures:
+ _objc_msgSend$outputContextImplDidChangeVolume:
+ _objc_msgSend$outputContextImplDidChangeVolumeControlType:
+ _objc_msgSend$outputContextImplForControllingOutputDeviceGroupWithID:options:
+ _objc_msgSend$outputContextImplForID:type:
+ _objc_msgSend$outputContextImplOutgoingCommunicationChannelDidBecomeAvailable:
+ _objc_msgSend$outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:
+ _objc_msgSend$outputContextManagerImplDidExpireWithReplacementImpl:
+ _objc_msgSend$outputContextOutgoingCommunicationChannelDidBecomeAvailable:
+ _objc_msgSend$outputContextType
+ _objc_msgSend$outputDevice
+ _objc_msgSend$outputDevice:didCloseCommunicationChannel:
+ _objc_msgSend$outputDevice:didReceiveData:fromCommunicationChannel:
+ _objc_msgSend$outputDeviceAuthorizationRequestImpl:didRespondWithAuthorizationToken:
+ _objc_msgSend$outputDeviceAuthorizationRequestImplDidCancel:
+ _objc_msgSend$outputDeviceAuthorizationSession:didProvideAuthorizationRequest:
+ _objc_msgSend$outputDeviceAuthorizationSession:shouldRetryAuthorizationRequest:reason:
+ _objc_msgSend$outputDeviceAuthorizationSessionImpl:didProvideAuthorizationRequest:
+ _objc_msgSend$outputDeviceAuthorizationSessionImpl:shouldRetryAuthorizationRequest:reason:
+ _objc_msgSend$outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:
+ _objc_msgSend$outputDeviceDiscoverySessionBluetoothOnlyDiscoveryDidChange:
+ _objc_msgSend$outputDeviceDiscoverySessionCachedDiscoveryDidChange:
+ _objc_msgSend$outputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:
+ _objc_msgSend$outputDeviceDiscoverySessionFactory
+ _objc_msgSend$outputDeviceDiscoverySessionImpl:didExpireWithReplacement:
+ _objc_msgSend$outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:
+ _objc_msgSend$outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:
+ _objc_msgSend$outputDeviceDiscoverySessionOfClass:withDeviceFeatures:
+ _objc_msgSend$outputDeviceFromRoutingContext:
+ _objc_msgSend$outputDeviceHIDs
+ _objc_msgSend$outputDeviceImplCanMuteDidChange:
+ _objc_msgSend$outputDeviceImplDidChangeCanChangeVolume:
+ _objc_msgSend$outputDeviceImplDidChangeMute:
+ _objc_msgSend$outputDeviceImplDidChangeVolume:
+ _objc_msgSend$outputDeviceImplDidChangeVolumeControlType:
+ _objc_msgSend$outputDeviceInfo
+ _objc_msgSend$outputDeviceWithFigEndpoint:
+ _objc_msgSend$outputDeviceWithRouteDescriptor:routeDiscoverer:
+ _objc_msgSend$outputDeviceWithRouteDescriptor:withRoutingContext:
+ _objc_msgSend$outputDevices
+ _objc_msgSend$outputDevicesFromRoutingContext:
+ _objc_msgSend$ownsTurnByTurnNavigation
+ _objc_msgSend$pairedDeviceID
+ _objc_msgSend$parentAuthorizationSession
+ _objc_msgSend$parentAuthorizationSessionImpl
+ _objc_msgSend$parentChannel
+ _objc_msgSend$parentInputContext
+ _objc_msgSend$parentInputDeviceDiscoverySession
+ _objc_msgSend$parentOutputContext
+ _objc_msgSend$parentOutputContextImpl
+ _objc_msgSend$parentOutputContextManager
+ _objc_msgSend$parentOutputDevice
+ _objc_msgSend$parentOutputDeviceDiscoverySession
+ _objc_msgSend$participatesInGroupPlayback
+ _objc_msgSend$peerID
+ _objc_msgSend$performHapticFeedbackForUUID:withHapticType:completionHandler:
+ _objc_msgSend$persistToDiskReturningError:
+ _objc_msgSend$platformDependentScreenOrVideoContext
+ _objc_msgSend$platformIdentifier
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$postNotification:
+ _objc_msgSend$postNotification:fromImpl:
+ _objc_msgSend$postNotification:withPayload:fromImpl:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$predictedOutputDevice
+ _objc_msgSend$predictedOutputDeviceFromRoutingContext:
+ _objc_msgSend$preferredParticipantForExternalPlayback
+ _objc_msgSend$preferredParticipantForNonMixableAudioRoutes
+ _objc_msgSend$prefersLikelyDestinationsOverCurrentRoutingSession
+ _objc_msgSend$prefersRouteDescriptors
+ _objc_msgSend$presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets
+ _objc_msgSend$probability
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$producesLowFidelityAudio
+ _objc_msgSend$propertyList
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$proposedGroupID
+ _objc_msgSend$providesControlForAllVolumeFeatures
+ _objc_msgSend$providesExternalVideoPlayback
+ _objc_msgSend$publicKey
+ _objc_msgSend$raise:format:
+ _objc_msgSend$rampMode
+ _objc_msgSend$receivesLongFormAudioFromLocalDevice
+ _objc_msgSend$recentlyUsedDevices
+ _objc_msgSend$recognizingSpeech
+ _objc_msgSend$referencedObject
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeFrecencyInfoForDeviceID:
+ _objc_msgSend$removeListenerWithWeakReference:callback:name:object:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeOutputDevice:options:completionHandler:
+ _objc_msgSend$removeOutputDevice:withOptions:completionhandler:
+ _objc_msgSend$removeOutputDevice:withOptions:fromRoutingContext:completionHandler:
+ _objc_msgSend$removePointerAtIndex:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$reportModificationMetrics:
+ _objc_msgSend$requestCarUIForURL:withUUID:
+ _objc_msgSend$requestTurnByTurnNavigationOwnership
+ _objc_msgSend$requestViewArea:forScreenID:
+ _objc_msgSend$requiresAuthorization
+ _objc_msgSend$resetOutputDeviceForAllOutputContexts
+ _objc_msgSend$resetPredictedOutputDevice
+ _objc_msgSend$respondWithAuthorizationToken:completionHandler:
+ _objc_msgSend$result
+ _objc_msgSend$resultInput
+ _objc_msgSend$retrieveSessionWithID:
+ _objc_msgSend$rightBatteryLevel
+ _objc_msgSend$rightHandDrive
+ _objc_msgSend$routeConfigUpdateReason
+ _objc_msgSend$routeDescriptor
+ _objc_msgSend$routeDiscoverer
+ _objc_msgSend$routeDiscovererFactory
+ _objc_msgSend$routingContextCommandPayload
+ _objc_msgSend$routingContextFactory
+ _objc_msgSend$routingContextUUID
+ _objc_msgSend$scheduledFloatValueRampWithStartValue:endValue:timeRange:
+ _objc_msgSend$scheduledParameterRampInterpolatedToTime:
+ _objc_msgSend$screens
+ _objc_msgSend$sendData:completionHandler:
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setActivatedDeviceClusterMembersVolume:withRoomID:
+ _objc_msgSend$setAllowsHeadTrackedSpatialAudio:error:
+ _objc_msgSend$setAudioSessionId:
+ _objc_msgSend$setCarPlayVideoActive:completionHandler:
+ _objc_msgSend$setClientModificationFinishedTimestamp:
+ _objc_msgSend$setClientModificationStartedTimestamp:
+ _objc_msgSend$setCompletionBlock:
+ _objc_msgSend$setConversationDetectionEnabled:error:
+ _objc_msgSend$setCurrentBluetoothListeningMode:error:
+ _objc_msgSend$setDefaultExternalPlaybackPriority
+ _objc_msgSend$setDefaultNonMixableAudioPriority
+ _objc_msgSend$setDiscoveryMode:forClientIdentifiers:
+ _objc_msgSend$setDisplayCornerMasks:
+ _objc_msgSend$setExternalPlaybackPriority:
+ _objc_msgSend$setFigEndpointType:
+ _objc_msgSend$setFinalConfiguration:
+ _objc_msgSend$setFrecencyInfo:forDeviceID:
+ _objc_msgSend$setHeadTrackedSpatialAudioMode:error:
+ _objc_msgSend$setImplEventListener:
+ _objc_msgSend$setInputDevice:options:completionHandler:
+ _objc_msgSend$setMediaRemoteData:completionHandler:
+ _objc_msgSend$setMuted:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNonMixableAudioPriority:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOutputContext:forContextID:
+ _objc_msgSend$setOutputDevice:options:completionHandler:
+ _objc_msgSend$setOutputDevice:withOptions:onRoutingContext:completionHandler:
+ _objc_msgSend$setOutputDevices:options:completionHandler:
+ _objc_msgSend$setOutputDevices:withOptions:onRoutingContext:completionHandler:
+ _objc_msgSend$setParentAuthorizationSession:
+ _objc_msgSend$setParentAuthorizationSessionImpl:
+ _objc_msgSend$setParentChannel:
+ _objc_msgSend$setParentCommunicationChannel:
+ _objc_msgSend$setParentInputContext:
+ _objc_msgSend$setParentInputDeviceDiscoverySession:
+ _objc_msgSend$setParentOutputContext:
+ _objc_msgSend$setParentOutputContextImpl:
+ _objc_msgSend$setParentOutputContextManager:
+ _objc_msgSend$setParentOutputDevice:
+ _objc_msgSend$setParentOutputDeviceDiscoverySession:
+ _objc_msgSend$setParentOutputDeviceGroup:
+ _objc_msgSend$setPreferredParticipantForExternalPlayback:
+ _objc_msgSend$setPreferredParticipantForNonMixableAudioRoutes:
+ _objc_msgSend$setRouteDescriptor:
+ _objc_msgSend$setSecondDisplayEnabled:
+ _objc_msgSend$setSecondDisplayMode:completionHandler:
+ _objc_msgSend$setSiriForwardingEnabled:
+ _objc_msgSend$setTargetAudioSession:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setViewAreaIndex:andAdjacentViewAreas:forScreenID:
+ _objc_msgSend$setVolume:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sharedAudioPresentationOutputContext
+ _objc_msgSend$sharedExecutionEnvironment
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedLocalDevice
+ _objc_msgSend$sharedSystemAudioContext
+ _objc_msgSend$sharedSystemAudioInputContext
+ _objc_msgSend$sharedSystemRemoteDisplayContext
+ _objc_msgSend$sharedSystemRemotePool
+ _objc_msgSend$sharedSystemRemotePoolContext
+ _objc_msgSend$sharedSystemRemotePoolImpl
+ _objc_msgSend$sharedSystemScreenContext
+ _objc_msgSend$shortValue
+ _objc_msgSend$signal
+ _objc_msgSend$siriForwardingEnabled
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$start
+ _objc_msgSend$startFloatValue
+ _objc_msgSend$startValue
+ _objc_msgSend$startVolume
+ _objc_msgSend$status
+ _objc_msgSend$statusOfOperations:error:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAbbreviatingWithTildeInPath
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$stringWithValidatedFormat:validFormatSpecifiers:error:
+ _objc_msgSend$suggestUIWithURLs:completionHandler:
+ _objc_msgSend$supportedFeatures
+ _objc_msgSend$supportsBluetoothSharing
+ _objc_msgSend$supportsBufferedAirPlay
+ _objc_msgSend$supportsConversationDetection
+ _objc_msgSend$supportsDataOverACLProtocol
+ _objc_msgSend$supportsFitnessDataDestination
+ _objc_msgSend$supportsHeadTrackedSpatialAudio
+ _objc_msgSend$supportsHighQualityContentCapture
+ _objc_msgSend$supportsMultipleBluetoothOutputDevices
+ _objc_msgSend$supportsMultipleOutputDevices
+ _objc_msgSend$supportsScreenMirroringControls
+ _objc_msgSend$takeScreenForClient:reason:
+ _objc_msgSend$targetAudioSession
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeRange
+ _objc_msgSend$transportType
+ _objc_msgSend$typeWithIdentifier:
+ _objc_msgSend$unfinishedOperations
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$updateFrecencyListForDeviceID:
+ _objc_msgSend$updateFrecencyScore
+ _objc_msgSend$userInfo
+ _objc_msgSend$userPreferredInputDevice:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_msgSend$valueWithCMTime:
+ _objc_msgSend$valueWithCMTimeMapping:
+ _objc_msgSend$valueWithCMTimeRange:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$valueWithRect:
+ _objc_msgSend$valueWithSize:
+ _objc_msgSend$voiceTriggerMode
+ _objc_msgSend$volume
+ _objc_msgSend$volumeControlType
+ _objc_msgSend$volumeForActivatedDeviceClusterMembersWithRoomID:
+ _objc_msgSend$volumeRampWithStartVolume:endVolume:timeRange:rampMode:
+ _objc_msgSend$wait
+ _objc_msgSend$waitUntilEventIsCompleted
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_msgSend$willChangeValueForKey:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_msgSend$zone
+ _objc_release
+ _objc_release_x19
+ _objc_release_x2
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x24
+ _objc_release_x25
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x8
+ _objc_setAssociatedObject
+ _objc_setProperty_nonatomic
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _outputContext.onceToken
+ _outputContext.sSharedContext
+ _outputContextManagerForAllOutputContexts.onceToken
+ _outputContextManagerForAllOutputContexts.sSharedManager
+ _sSharedAgent
+ _sSharedAgentQueue
+ _sharedAuthorizationSession.onceToken
+ _sharedAuthorizationSession.session
+ _sharedExecutionEnvironment.onceToken
+ _sharedExecutionEnvironment.sSharedExecutionEnvironment
+ _sharedInstance.onceToken
+ _sharedInstance.sharedFactory
+ _sharedRoutingPlaybackArbiter.sAVRoutingPlaybackArbiter_Once
+ _sharedRoutingPlaybackArbiter.sRoutingPlaybackArbiter
+ _sin
+ _strcmp
+ _stringWithValidatedFormatString
+ _sysdir_get_next_search_path_enumeration
+ _sysdir_start_search_path_enumeration_private
CStrings:
+ ""
+ " with %@ ramp style"
+ "!"
+ "#16@0:8"
+ "%@"
+ "%@ %@"
+ "%@ only supports listening to notifications from CMNotificationCenterGetDefaultLocalCenter"
+ "%@ read/write queue"
+ "%@, "
+ "%@.plist"
+ "%@: %@"
+ "%c[%@ %@]"
+ "%d"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "'%@'"
+ "(error %d)"
+ "(name: %@, ID: %@)"
+ "*** %@"
+ "*** -%@ cannot be sent to an abstract object of class %@: Create a concrete instance!"
+ "*** -%@ only defined for abstract class.  Define %@!"
+ "*** initialization method -%@ cannot be sent to an abstract object of class %@: Create a concrete instance!"
+ "+[AVFigRoutingContextOutputContextImpl allSharedAudioOutputContextImpls]"
+ "+[AVFigRoutingContextOutputContextImpl outputContextExistsWithRemoteOutputDevice]"
+ "+[AVFigRoutingContextOutputContextImpl resetOutputDeviceForAllOutputContexts]"
+ "+[AVFigRoutingContextOutputContextImpl sharedSystemRemoteDisplayContext]"
+ "+[AVInputContext defaultInputContextImplClass]"
+ "+[AVOutputContext defaultOutputContextImplClass]"
+ "+[AVOutputContext resetOutputDeviceForAllOutputContexts]"
+ "+[AVOutputContext(AVAudioSession) preferredOutputDevicesForAudioSession:]"
+ "+[AVOutputContextManager outputContextManagerForAllOutputContexts]_block_invoke_2"
+ "+[AVOutputDevice localDeviceDidChange]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:routingContextFactory:]"
+ "+[AVOutputDevice(AVOutputDeviceFigEndpointImplFetching) outputDeviceWithFigEndpoint:volumeController:]"
+ "+[AVOutputDevice(FigRouteDescriptor) prefersRouteDescriptors]"
+ "+[AVOutputDeviceAuthorizationSession sharedAuthorizationSession]_block_invoke_2"
+ "+[AVOutputDeviceFrecencyManager _frecentsFilePath]_block_invoke"
+ "+[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary]_block_invoke"
+ "+[AVOutputDeviceFrecencyManager _migrateFrecentsFromCFPreferencesToFrecentsFilePath:]"
+ "+[AVOutputDeviceFrecencyManager frecencyScoreForDeviceID:]"
+ "+[AVOutputDeviceFrecencyManager updateFrecencyListForDeviceID:]"
+ "+[AVRoutingOperation(ArrayOfOperations) statusOfOperations:error:]"
+ "+[AVRoutingSessionManager longFormVideoRoutingSessionManager]"
+ ", "
+ ", changes instantaneously to "
+ ", holds steady at "
+ ", ramps to "
+ "-[AVFigCommChannelUUIDCommunicationChannelManager _didReceiveData:fromCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager didCloseCommChannelUUID:]_block_invoke"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager openCommunicationChannelWithOptions:error:]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]"
+ "-[AVFigCommChannelUUIDCommunicationChannelManager outgoingCommunicationChannel]_block_invoke"
+ "-[AVFigCommChannelUUIDOutputContextCommunicationChannelImpl sendData:completionHandler:]"
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
+ "-[AVFigEndpointOutputDeviceImpl _canMuteDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _figEndpointPropertyValueForKey:]"
+ "-[AVFigEndpointOutputDeviceImpl _mutedDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _volumeDidChangeForEndpointWithID:]"
+ "-[AVFigEndpointOutputDeviceImpl _volumeForEndpointDidChange:forRoomID:]"
+ "-[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]"
+ "-[AVFigEndpointOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke"
+ "-[AVFigEndpointOutputDeviceImpl connectedPairedDevices]"
+ "-[AVFigEndpointOutputDeviceImpl deviceSubType]"
+ "-[AVFigEndpointOutputDeviceImpl deviceType]"
+ "-[AVFigEndpointOutputDeviceImpl initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:]"
+ "-[AVFigEndpointOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigEndpointOutputDeviceImpl isInEar]"
+ "-[AVFigEndpointOutputDeviceImpl isInUseByPairedDevice]"
+ "-[AVFigEndpointOutputDeviceImpl setCurrentBluetoothListeningMode:]"
+ "-[AVFigEndpointOutputDeviceImpl setCurrentBluetoothListeningMode:error:]"
+ "-[AVFigEndpointOutputDeviceImpl setVolume:]"
+ "-[AVFigEndpointOutputDeviceImpl supportsDataOverACLProtocol]"
+ "-[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl _didCloseCommunicationChannel]"
+ "-[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl _didReceiveData:]"
+ "-[AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl sendData:completionHandler:]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:]"
+ "-[AVFigEndpointUIAgentOutputContextManagerImpl initWithEndpointUIAgent:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _finishedWithPrompt]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _notifyCurrentRequestOfTerminalStatus:error:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _showAuthPromptWithUniqueID:routeDescriptor:pinMode:reason:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl _startNewRequest:impl:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl initWithFigEndpointUIAgent:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl outputDeviceAuthorizationRequestImpl:didRespondWithAuthorizationToken:]"
+ "-[AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl outputDeviceAuthorizationRequestImplDidCancel:]"
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
+ "-[AVFigRouteDescriptorInputDeviceImpl _withEndpoint:]"
+ "-[AVFigRouteDescriptorInputDeviceImpl initWithRouteDescriptor:routeDiscoverer:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
+ "-[AVFigRouteDescriptorInputDeviceImpl isAppleAccessory]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _canMuteDidChangeForEndpointWithID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _canSetEndpointVolumeDidChangeForEndpointWithID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _endpointVolumeControlTypeDidChangeForEndpointWithID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _mutedDidChangeForEndpointWithID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _volumeDidChangeForEndpointWithID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _volumeForEndpointDidChange:forRoomID:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl _withEndpoint:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl configureUsingBlock:options:completionHandler:]_block_invoke"
+ "-[AVFigRouteDescriptorOutputDeviceImpl initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl isAppleAccessory]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl setCurrentBluetoothListeningMode:error:]"
+ "-[AVFigRouteDescriptorOutputDeviceImpl setVolume:]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _endpointDescriptorChanged]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _routePresentChanged]"
+ "-[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl _serverDied]"
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
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl availableOutputDevicesObject]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl devicePresenceDetected]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl initWithFigRouteDiscovererCreator:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionBluetoothOnlyDiscoveryDidChange:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionCachedDiscoveryDidChange:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl setTargetAudioSession:]"
+ "-[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl targetAudioSession]"
+ "-[AVFigRoutingContextInputContextImpl _createSelectRouteOptionsForSetInputDeviceOptions:]"
+ "-[AVFigRoutingContextInputContextImpl _currentRouteChanged]"
+ "-[AVFigRoutingContextInputContextImpl _routeChangeEndedWithID:reason:]"
+ "-[AVFigRoutingContextInputContextImpl _routeChangeStartedWithID:]"
+ "-[AVFigRoutingContextInputContextImpl _routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:]"
+ "-[AVFigRoutingContextInputContextImpl _serverConnectionDied]"
+ "-[AVFigRoutingContextInputContextImpl clearUserPreferredInputDevice:error:]"
+ "-[AVFigRoutingContextInputContextImpl initWithFigRoutingContext:routingContextReplacementBlock:]"
+ "-[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]"
+ "-[AVFigRoutingContextInputContextImpl initWithRoutingContextUUID:type:]_block_invoke"
+ "-[AVFigRoutingContextInputContextImpl inputDevice]"
+ "-[AVFigRoutingContextInputContextImpl routingContextUUID]"
+ "-[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextInputContextImpl setInputDevice:options:completionHandler:]_block_invoke"
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
+ "-[AVFigRoutingContextOutputContextImpl resetPredictedOutputDevice]"
+ "-[AVFigRoutingContextOutputContextImpl routingContextUUID]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevice:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setOutputDevices:options:completionHandler:]"
+ "-[AVFigRoutingContextOutputContextImpl setVolume:]"
+ "-[AVInputContext ID]"
+ "-[AVInputContext encodeWithCoder:]"
+ "-[AVInputContext initWithCoder:]"
+ "-[AVInputContext initWithInputContextImpl:]"
+ "-[AVInputContext inputContextImpl:didChangeInputDeviceWithInitiator:]"
+ "-[AVInputContext inputContextImpl:didExpireWithReplacement:]"
+ "-[AVInputContext inputContextImpl:didInitiateDestinationChange:]"
+ "-[AVInputContext inputDevice]"
+ "-[AVInputContext setApplicationProcessID:]"
+ "-[AVInputContext setInputDevice:options:completionHandler:]"
+ "-[AVInputContext setInputDevice:options:completionHandler:]_block_invoke"
+ "-[AVInputContextDestinationChange _setStatus:]"
+ "-[AVInputDevice initWithInputDeviceImpl:]"
+ "-[AVInputDeviceDiscoverySession devicePresenceDetected]"
+ "-[AVInputDeviceDiscoverySession impl]"
+ "-[AVInputDeviceDiscoverySession initWithDeviceFeatures:]"
+ "-[AVInputDeviceDiscoverySession initWithInputDeviceDiscoverySessionImpl:]"
+ "-[AVInputDeviceDiscoverySession inputDeviceDiscoverySessionImplDidChangeAvailableInputDevices:]"
+ "-[AVOutputContext ID]"
+ "-[AVOutputContext addOutputDevice:]"
+ "-[AVOutputContext addOutputDevice:options:completionHandler:]"
+ "-[AVOutputContext addOutputDevice:options:completionHandler:]_block_invoke"
+ "-[AVOutputContext encodeWithCoder:]"
+ "-[AVOutputContext initWithCoder:]"
+ "-[AVOutputContext initWithOutputContextImpl:]"
+ "-[AVOutputContext openCommunicationChannelWithOptions:error:]"
+ "-[AVOutputContext outputContextImpl:didChangeOutputDeviceWithInitiator:]"
+ "-[AVOutputContext outputContextImpl:didChangeOutputDevicesWithInitiator:reason:deviceID:previousDeviceIDs:]"
+ "-[AVOutputContext outputContextImpl:didCloseCommunicationChannel:]"
+ "-[AVOutputContext outputContextImpl:didExpireWithReplacement:]"
+ "-[AVOutputContext outputContextImpl:didInitiateDestinationChange:]"
+ "-[AVOutputContext outputContextImpl:didReceiveData:fromCommunicationChannel:]"
+ "-[AVOutputContext outputContextImplDidChangeCanMute:]"
+ "-[AVOutputContext outputContextImplDidChangeCanSetVolume:]"
+ "-[AVOutputContext outputContextImplDidChangeGlobalOutputDeviceConfiguration:]"
+ "-[AVOutputContext outputContextImplDidChangeMute:]"
+ "-[AVOutputContext outputContextImplDidChangePredictedOutputDevice:]"
+ "-[AVOutputContext outputContextImplDidChangeProvidesControlForAllVolumeFeatures:]"
+ "-[AVOutputContext outputContextImplDidChangeVolume:]"
+ "-[AVOutputContext outputContextImplDidChangeVolumeControlType:]"
+ "-[AVOutputContext outputContextImplOutgoingCommunicationChannelDidBecomeAvailable:]"
+ "-[AVOutputContext outputDevice]"
+ "-[AVOutputContext outputDevices]"
+ "-[AVOutputContext predictedOutputDevice]"
+ "-[AVOutputContext removeOutputDevice:]"
+ "-[AVOutputContext removeOutputDevice:options:completionHandler:]"
+ "-[AVOutputContext removeOutputDevice:options:completionHandler:]_block_invoke"
+ "-[AVOutputContext resetPredictedOutputDevice]"
+ "-[AVOutputContext setApplicationProcessID:]"
+ "-[AVOutputContext setCommunicationChannelDelegate:]"
+ "-[AVOutputContext setOutputDevice:forFeatures:]"
+ "-[AVOutputContext setOutputDevice:options:]"
+ "-[AVOutputContext setOutputDevice:options:completionHandler:]"
+ "-[AVOutputContext setOutputDevice:options:completionHandler:]_block_invoke"
+ "-[AVOutputContext setOutputDevices:]"
+ "-[AVOutputContext setOutputDevices:options:completionHandler:]"
+ "-[AVOutputContext setOutputDevices:options:completionHandler:]_block_invoke"
+ "-[AVOutputContextCommunicationChannel sendData:completionHandler:]"
+ "-[AVOutputContextDestinationChange _setStatus:cancellationReason:]"
+ "-[AVOutputContextManager outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:]"
+ "-[AVOutputDevice activatedDeviceClusterMembersDidChangeVolume:forRoomID:]"
+ "-[AVOutputDevice communicationChannelManager:didCloseCommunicationChannel:]"
+ "-[AVOutputDevice communicationChannelManager:didReceiveData:fromCommunicationChannel:]"
+ "-[AVOutputDevice configureUsingBlock:completionHandler:]"
+ "-[AVOutputDevice configureUsingBlock:completionHandler:]_block_invoke"
+ "-[AVOutputDevice configureUsingBlock:options:completionHandler:]"
+ "-[AVOutputDevice configureUsingBlock:options:completionHandler:]_block_invoke"
+ "-[AVOutputDevice decreaseVolumeByCount:]"
+ "-[AVOutputDevice increaseVolumeByCount:]"
+ "-[AVOutputDevice initWithOutputDeviceImpl:commChannelManager:]"
+ "-[AVOutputDevice openCommunicationChannelToDestination:options:completionHandler:]"
+ "-[AVOutputDevice openCommunicationChannelToDestination:options:completionHandler:]_block_invoke"
+ "-[AVOutputDevice openCommunicationChannelWithOptions:completionHandler:]"
+ "-[AVOutputDevice outputDeviceImplCanMuteDidChange:]"
+ "-[AVOutputDevice outputDeviceImplDidChangeCanChangeVolume:]"
+ "-[AVOutputDevice outputDeviceImplDidChangeMute:]"
+ "-[AVOutputDevice outputDeviceImplDidChangeProposedGroupID:]"
+ "-[AVOutputDevice outputDeviceImplDidChangeVolume:]"
+ "-[AVOutputDevice outputDeviceImplDidChangeVolumeControlType:]"
+ "-[AVOutputDevice postNotification:fromImpl:]"
+ "-[AVOutputDevice postNotification:withPayload:fromImpl:]"
+ "-[AVOutputDevice setActivatedDeviceClusterMembersVolume:withRoomID:]"
+ "-[AVOutputDevice setAllowsHeadTrackedSpatialAudio:error:]"
+ "-[AVOutputDevice setCarPlayVideoActive:completionHandler:]"
+ "-[AVOutputDevice setCarPlayVideoActive:completionHandler:]_block_invoke"
+ "-[AVOutputDevice setCommunicationChannelDelegate:]"
+ "-[AVOutputDevice setCurrentBluetoothListeningMode:]"
+ "-[AVOutputDevice setCurrentBluetoothListeningMode:error:]"
+ "-[AVOutputDevice setDelegate:]"
+ "-[AVOutputDevice setHeadTrackedSpatialAudioMode:error:]"
+ "-[AVOutputDevice setMuted:]"
+ "-[AVOutputDevice setSecondDisplayEnabled:]"
+ "-[AVOutputDevice setSecondDisplayMode:completionHandler:]"
+ "-[AVOutputDevice setSecondDisplayMode:completionHandler:]_block_invoke"
+ "-[AVOutputDevice setVolume:]"
+ "-[AVOutputDeviceAuthorizationRequest cancel]"
+ "-[AVOutputDeviceAuthorizationRequest respondWithAuthorizationToken:completionHandler:]"
+ "-[AVOutputDeviceAuthorizationRequest respondWithAuthorizationToken:completionHandler:]_block_invoke"
+ "-[AVOutputDeviceAuthorizationSession initWithOutputDeviceAuthorizationSessionImpl:]"
+ "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImpl:didProvideAuthorizationRequest:]"
+ "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImpl:shouldRetryAuthorizationRequest:reason:]"
+ "-[AVOutputDeviceAuthorizationSession outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:]"
+ "-[AVOutputDeviceAuthorizationSession setDelegate:]"
+ "-[AVOutputDeviceCommunicationChannel communicationChannelImpl:didReceiveData:]"
+ "-[AVOutputDeviceCommunicationChannel communicationChannelImplDidClose:]"
+ "-[AVOutputDeviceCommunicationChannel setDelegate:]"
+ "-[AVOutputDeviceDiscoverySession availableOutputDevices]"
+ "-[AVOutputDeviceDiscoverySession devicePresenceDetected]"
+ "-[AVOutputDeviceDiscoverySession impl]"
+ "-[AVOutputDeviceDiscoverySession initWithOutputDeviceDiscoverySessionImpl:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:]"
+ "-[AVOutputDeviceDiscoverySession outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:]"
+ "-[AVOutputDeviceDiscoverySession setCachedDiscoveryEnabled:]"
+ "-[AVOutputDeviceDiscoverySession setDiscoveryMode:forClientIdentifiers:]"
+ "-[AVOutputDeviceDiscoverySession setOnlyDiscoversBluetoothDevices:]"
+ "-[AVOutputDeviceDiscoverySession setTargetAudioSession:]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices otherDevices]"
+ "-[AVOutputDeviceDiscoverySessionAvailableOutputDevices recentlyUsedDevices]"
+ "-[AVOutputDeviceFrecentsReader frecencyInfoForDeviceWithID:]"
+ "-[AVOutputDeviceFrecentsReader initWithFrecentsFilePath:error:]"
+ "-[AVOutputDeviceGroup addOutputDevice:withOptions:completionHandler:]"
+ "-[AVOutputDeviceGroup addOutputDevice:withOptions:completionHandler:]_block_invoke"
+ "-[AVOutputDeviceGroup initWithOutputDeviceGroupImpl:]"
+ "-[AVOutputDeviceGroup outputDeviceGroupImpl:didChangeOutputDevicesWithInitiator:]"
+ "-[AVOutputDeviceGroup outputDeviceGroupImplDidChangeVolume:]"
+ "-[AVOutputDeviceGroup outputDeviceGroupImplDidChangeVolumeControlType:]"
+ "-[AVOutputDeviceGroup outputDevices]"
+ "-[AVOutputDeviceGroup removeOutputDevice:withOptions:completionHandler:]"
+ "-[AVOutputDeviceGroup removeOutputDevice:withOptions:completionHandler:]_block_invoke"
+ "-[AVOutputDeviceHID initWithUUID:screenUUID:endpoint:]"
+ "-[AVOutputDeviceHID setInputMode:]"
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
+ "-[AVRoutingContextSendConfigureDeviceCommandOperation start]"
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
+ "-[AVRoutingSerializedMostlySynchronousReentrantBlockScheduler scheduleBlock:]"
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
+ "-[AVRoutingSessionManager startRoutingSessionForHighConfidenceExternalDestinationIfPresentWithCompletionHandler:]"
+ "-[AVRoutingSessionManager startRoutingSessionWithOutputDeviceDescriptions:error:]"
+ "-[AVRoutingSessionManager startSuppressingLikelyDestinationsUntilNextPlayEventAndReturnError:]"
+ "-[AVRoutingSessionManager stopSuppressingLikelyDestinationsAndReturnError:]"
+ "-[AVRoutingSessionManager updateCurrentRoutingSessionFromLikelyDestinationsWithCompletionHandler:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelImpl sendData:completionHandler:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didCloseCommChannelWithUUID:forDeviceWithID:]_block_invoke"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager _didReceiveData:fromDeviceWithID:fromChannelWithUUID:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager dealloc]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager initWithDeviceID:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]_block_invoke"
+ "-[AVSystemRemotePoolOutputDeviceCommunicationChannelManager openCommunicationChannelWithOptions:completionHandler:]_block_invoke_2"
+ "11"
+ "<%@: %p, ID=%@, outputDevice=%@, tokenType=%@>"
+ "<%@: %p, ID=%@, type=%@>"
+ "<%@: %p, currentRoutingSession=%@, likelyExternalDestinations=%@, allLikelyDestinations=%@, prefersLikelyDestinationsOverCurrentRoutingSession=%d>"
+ "<%@: %p, establishedAutomaticallyFromLikelyDestination=%s, destination=%@>"
+ "<%@: %p, outputDeviceDescriptions=%@, probability=%f, providesExternalVideoPlayback=%@>"
+ "<%@: %p, referencedObject = %@>"
+ "<%@: %p, status=%d, cancellationReason=%@>"
+ "<%@: %p, status=%d>"
+ "<%@: %p, timeRange:%@ startValue:%@ endValue:%@ extras:%@>"
+ "<%@: %p, unfinishedOperations=%@>"
+ "<%@: %p, volume mix: %@>"
+ "<%@: %p>"
+ "<<<< AVBlockScheduler >>>> %s: Some thread is already running a block with this serializer.  Enqueued this block and letting that thread execute it"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Assuming route change with ID %@ corresponds to the route change we just initiated"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (notificationName=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextAddToSelectedRouteDescriptors (routeDescriptor: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextAddToSelectedRouteDescriptors (routeDescriptor: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextAddToSelectedRoutes (endpoint: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextAddToSelectedRoutes (endpoint: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextRemoveFromSelectedRouteDescriptors (routeDescriptor: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextRemoveFromSelectedRouteDescriptors (routeDescriptor: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextRemoveFromSelectedRoutes (endpoint: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextRemoveFromSelectedRoutes (endpoint: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRoute (endpoint: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRoute (endpoint: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRouteDescriptor (routeDescriptor: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRouteDescriptor (routeDescriptor: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRouteDescriptors (routeDescriptors: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRouteDescriptors (routeDescriptors: %{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRoutes (endpoints: %{private}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Calling FigRoutingContextSelectRoutes (endpoints=%{private}@, clientRouteRequestID=%{public}@, authInfo? %d, avoidAuthPrompt=%{public}@, initiator=%{public}@, clientPID=%{public}@)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Sending kFigEndpointSendCommand_CommandType_Configure (deviceName? %d, password? %d, enableHKAccessControl=%{public}@, HKAccessControlLevel=%{public}@, peersToAdd? %d, peersToRemove? %d)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVRoutingErrorIncorrectPassword, since we do not know whether it was a PIN or password"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using AVRoutingErrorUnknown, since we have no more detailed error information"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: Using value %d for %@"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (deviceName=%{private}@, password=%{private}@, identifier=%{private}@, publicKey=%{private}@, enableHKAccessControl=%{public}@, HKAccessControlLevel=%{public}@, peersList=%{private}@, err=%d)"
+ "<<<< AVFigRoutingContextUtilities >>>> %s: called (err=%d)"
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
+ "<<<< AVInputContext (FigRoutingContext) >>>>"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s:  called (context=%p, routeConfigUpdateID=%{public}@, reason=%{public}@, initiator=%{public}@ errorString=%{public}@, deviceID=%{private}@, previousDeviceIDs=%{private}@, deviceID provided?=%{public}@, previous deviceIDs provided?=%{public}@"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: *** kFigRoutingContextProperty_ContextUUID = NULL (err=%d) ***"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopyPredictedSelectedRouteDescriptorWithOptions yielded %@ (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextCopySelectedRouteDescriptor yielded %@ (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: FigRoutingContextResetPredictedSelectedRouteDescriptorWithOptions yielded (err: %d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (context=%p)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (context=%p, routeChangeID=%{public}@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (context=%p, routeChangeID=%{public}@, routeChangeReason=%{public}@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, inputDevice=%@, options=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, bundleID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, contextUUID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, inputDevice=%@, options=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeChangeID=%@, reason=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routeUpdateID=%@, reason=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: called (self=%p, routingContext=%@, routingContextCreator=%@)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: kFigRoutingContextProperty_ContextUUID = %@ (err=%d)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: operation finished"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: returning %@ (self=%p)"
+ "<<<< AVInputContext (FigRoutingContext) >>>> %s: using clientPID %d"
+ "<<<< AVInputContext >>>> %s: Defaulting to AVInputContext impl %@"
+ "<<<< AVInputContext >>>> %s: Posting %{public}@ with destination change %{public}@ for context=%p"
+ "<<<< AVInputContext >>>> %s: Posting %{public}@ with initiator %{public}@ for context=%p"
+ "<<<< AVInputContext >>>> %s: Result: %{public}@ for context=%p, inputDevice=%{private}@, initiator=%{public}@, timeTaken=%llu ms"
+ "<<<< AVInputContext >>>> %s: called (context=%p, inputDevice=%{private}@, initiator=%{public}@"
+ "<<<< AVInputContext >>>> %s: called (self=%p)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, impl=%@, replacementImpl=%@)"
+ "<<<< AVInputContext >>>> %s: called (self=%p, status=%d)"
+ "<<<< AVInputContext >>>> %s: contextID = %@"
+ "<<<< AVInputContext >>>> %s: inputDevice = %@"
+ "<<<< AVInputContext >>>> %s: setting applicationProcessID to %d"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>>"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: AVInputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: AudioRouteName is %{public}@, BT Endpoint is %{public}@"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: Grabbing endpoint for route descriptor %{private}@"
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: Input Device is nil. Cannot find the route descriptor. "
+ "<<<< AVInputDevice (FigRouteDescriptor) >>>> %s: called (self=%p)"
+ "<<<< AVInputDevice >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>>"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Failed to create replacement AVIDDS impl"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting kFigRouteDiscovererProperty_AudioSessionID to %@"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AudioSessionID = %@ (err=%d)"
+ "<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: *** nil impl! ***"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Posting %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Returning %@"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: Unsupported device feature combination %d"
+ "<<<< AVInputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: *** kFigRoutingContextProperty_ContextUUID = NULL (err=%d) ***"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Calling FigRoutingContextCreateCommChannel (control type: %d, clientTypeUUID: %{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Calling FigRoutingContextResetPredictedSelectedRouteDescriptor"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Calling FigVolumeControllerSetMasterVolumeOfRoutingContext (context=%p, volume=%f)"
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
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: FigRoutingContextSendData finished for comm channel ID %{public}@ (err=%d))"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Listener should be the shared endpoint agent queue"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: No comm channel found for ID %@, synthesizing one for the delegate (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Operation finished synchronously.  Blocking until completion handler is called, so that we preserve the synchronous nature of the operation"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Output context exists with associated remote output device"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Resetting global video output device selection via FigRoutingContextSelectRoute"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Sending %d bytes through comm channel ID %{public}@ via FigRoutingContextSendData"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Storing new outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Trying comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Unhandled routing context type %d.  Falling back to fetching context by ID %@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using comm channel ID %@ (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: Using pre-existing outgoing communication channel (self=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (commChannelUUID=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (commChannelUUID=%{public}@, dataLength=%d)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (context=%p)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (context=%p, routeChangeID=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (context=%p, routeChangeID=%{public}@, routeChangeReason=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (context=%p, routeConfigUpdateID=%{public}@, reason=%{public}@, initiator=%{public}@ errorString=%{public}@, deviceID=%{private}@, previousDeviceIDs=%{private}@, deviceID provided?=%{public}@, previous deviceIDs provided?=%{public}@"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (modificationResult=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routeDescriptor=%{private}@, reason=%{public}@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevice=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContext=%@, outputDevices=%@, options=%@)"
+ "<<<< AVOutputContext (FigRoutingContext) >>>> %s: called (routingContextID=%{private}@)"
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
+ "<<<< AVOutputContext >>>> %s: Delegate missing or does not implement -outputContext:didCloseCommunicationChannel:"
+ "<<<< AVOutputContext >>>> %s: Delegate missing or does not implement -outputContext:didReceiveData:fromCommunicationChannel:"
+ "<<<< AVOutputContext >>>> %s: Delegate missing or does not implement -outputContextOutgoingCommunicationChannelDidBecomeAvailable:"
+ "<<<< AVOutputContext >>>> %s: Invoking -outputContext:didCloseCommunicationChannel:"
+ "<<<< AVOutputContext >>>> %s: Invoking -outputContext:didReceiveData:fromCommunicationChannel: with %d bytes"
+ "<<<< AVOutputContext >>>> %s: Invoking -outputContextOutgoingCommunicationChannelDidBecomeAvailable:"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@ with destination change %{public}@ for context=%p"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@ with initiator %{public}@ for context=%p"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@ with initiator %{public}@, reason %{public}@, deviceID %{private}@, and previousDeviceIDs %{private}@ for context=%p"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@ with outputDevice: %{private}@ failureReason: %{public}@ didFailToConnectToOutputDeviceDictionary: %{private}@"
+ "<<<< AVOutputContext >>>> %s: Posting %{public}@)"
+ "<<<< AVOutputContext >>>> %s: Received notification %@"
+ "<<<< AVOutputContext >>>> %s: Result: %{public}@ for context=%p, device=%{private}@, initiator=%{public}@, correlationID=%{public}@, timeTaken=%llu ms"
+ "<<<< AVOutputContext >>>> %s: Result: %{public}@ for context=%p, devices=%{private}@, initiator=%{public}@, correlationID=%{public}@, timeTaken=%llu ms"
+ "<<<< AVOutputContext >>>> %s: Result: %{public}@ for context=%p, outputDevice=%{private}@, initiator=%{public}@, correlationID=%{public}@, timeTaken=%llu ms"
+ "<<<< AVOutputContext >>>> %s: called"
+ "<<<< AVOutputContext >>>> %s: called (context=%p, device=%{private}@, authToken? %d, cancelIfAuthRequired=%{public}@, initiator=%{public}@, correlationID=%{public}@, fadePlayback=%{public}@)"
+ "<<<< AVOutputContext >>>> %s: called (context=%p, device=%{private}@, initiator=%{public}@, correlationID=%{public}@. fadePlayback=%{public}@)"
+ "<<<< AVOutputContext >>>> %s: called (context=%p, devices=%{private}@, initiator=%{public}@, correlationID=%{public}@, fadePlayback=%{public}@)"
+ "<<<< AVOutputContext >>>> %s: called (context=%p, outputDevice=%{private}@, password? %d, cancelIfAuthRequired=%{public}@, suppressUserInteractionOnSenderOnly=%{public}@, initiator=%{public}@, correlationID=%{public}@ fadePlayback=%{public}@, defaultAudioToLocal=%{public}@)"
+ "<<<< AVOutputContext >>>> %s: called (controlType=%{public}@)"
+ "<<<< AVOutputContext >>>> %s: called (delegate? %d>)"
+ "<<<< AVOutputContext >>>> %s: called (device=%{private}@)"
+ "<<<< AVOutputContext >>>> %s: called (devices=%{private}@)"
+ "<<<< AVOutputContext >>>> %s: called (outputDevice=%{private}@, features=%d)"
+ "<<<< AVOutputContext >>>> %s: called (outputDevice=%{private}@, password? %d, cancelIfAuthRequired=%{public}@, suppressUserInteractionOnSenderOnly=%{public}@, initiator=%{public}@, fadePlayback=%{public}@)"
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
+ "<<<< AVOutputContext >>>> %s: sending %d bytes"
+ "<<<< AVOutputContext >>>> %s: setting applicationProcessID to %d"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigRoutingContextSelectRoute (endpoint=NULL)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerCanSetMuteOfEndpointWithID (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerChangeVolumeOfEndpointWithID (endpointID=%{private}@, count=%ld)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerGetMuteOfEndpointWithID (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerSetMuteOfEndpointWithID (endpointID=%{private}@ muted=%{BOOL}u)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerSetVolumeOfEndpointWithID (endpointID=%{private}@, volume=%f)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Calling FigVolumeControllerSetVolumeOfEndpointWithRoomID (endpointID=%{private}@, roomID=%{private}@, volume=%f)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Creating control channel-only routing context"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' has value: %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Endpoint property '%@' not supported"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: RouteUID %@ or RouteName %@ is nil, can't construct description."
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Sending %{public}@ command"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Sending %{public}@ command with display mode %llu"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Sending performHapticFeedback command"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Sending suggestUI command"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Setting %@ = %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized head-tracked spatial audio mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Unrecognized mode %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  Only a subset of possible device types can be communicated by FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover connected paired devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to discover detailed device subtype for most devices from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get DataOverACL information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Warning: FigEndpoint implementation is only intended for use on macOS.  There is no way to get isInEar information from FigEndpoint"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called (self=%p, figEndpoint=%@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: called with endpoint %p client %@ reason %@"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: calling FigEndpointBorrowScreen (clientName=%{public}@, reason=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: calling FigEndpointUnborrowScreen (clientName=%{public}@, reason=%{private}@)"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: setting kFigEndpointProperty_ListeningMode to %d"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>>"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVFigRouteDiscovereUpdateEndpointFeaturesCompletionCallback: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d."
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVFigRouteDiscovererUpdateEndpointFeatures: endpointName = %{public}@, inFeatures=%d, inActivateOptions=%{public}@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: AVOutputDevice %@ already bound to incompatible impl %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Calling FigRoutingContextSelectRouteDescriptor (routeDescriptor=NULL)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Calling FigVolumeControllerSetVolumeOfEndpointWithID (endpointID=%{private}@, volume=%f)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Creating control channel-only routing context"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: GAPA feature not enabled"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Grabbing endpoint for route descriptor %{private}@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Listener should be the output device route discoverer queue"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Operations finished with status %d, error %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Setting kFigEndpointProperty_ListeningMode to %d"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Using value %d for %@"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (endpointID=%{private}@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, ID=%@, endpointID=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, configuratorBlock=%@, options=%@, completionHandler=%@)"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: called (self=%p, routeDescriptor=%@)"
+ "<<<< AVOutputDevice >>>> %s: ...done setting carplay video to %d (error=%{public}@/%d)"
+ "<<<< AVOutputDevice >>>> %s: ...done setting second display mode (token=%{public}@, error=%{public}@/%d)"
+ "<<<< AVOutputDevice >>>> %s: Calling FigEndpointCreateRemoteControlSession (control type: %d, clientTypeUUID: %{public}@, correlationID: %{private}@)"
+ "<<<< AVOutputDevice >>>> %s: Delegate missing or does not implement -communicationChannel:didReceiveData: for channel=%p"
+ "<<<< AVOutputDevice >>>> %s: Delegate missing or does not implement -communicationChannelDidClose: for channel=%p"
+ "<<<< AVOutputDevice >>>> %s: Delegate missing or does not implement -outputDevice:didCloseCommunicationChannel:"
+ "<<<< AVOutputDevice >>>> %s: Delegate missing or does not implement -outputDevice:didReceiveData:fromCommunicationChannel"
+ "<<<< AVOutputDevice >>>> %s: Ignoring failure to read plist from data %{private}@ (%{private}@)"
+ "<<<< AVOutputDevice >>>> %s: Ignoring invalid frecents plist \"%{private}@\""
+ "<<<< AVOutputDevice >>>> %s: Ignoring malformed frecents entry \"%{private}@\" for device %{private}@"
+ "<<<< AVOutputDevice >>>> %s: Ignoring non-date last used timestamp \"%{private}@\" for device %{private}@"
+ "<<<< AVOutputDevice >>>> %s: Ignoring non-number frecency score \"%{private}@\" for device %{private}@"
+ "<<<< AVOutputDevice >>>> %s: Invoking -communicationChannel:didReceiveData: with %d bytes for channel=%p"
+ "<<<< AVOutputDevice >>>> %s: Invoking -communicationChannelDidClose: for channel=%p"
+ "<<<< AVOutputDevice >>>> %s: Invoking -outputDevice:didCloseCommunicationChannel:"
+ "<<<< AVOutputDevice >>>> %s: Invoking -outputDevice:didReceiveData:fromCommunicationChannel: with %d bytes"
+ "<<<< AVOutputDevice >>>> %s: Migrating frecents from CFPreferences to %{public}@"
+ "<<<< AVOutputDevice >>>> %s: No Output Context to add to!"
+ "<<<< AVOutputDevice >>>> %s: Open comm channel completed (err=%d, channel=%p, correlationID=%{private}@)"
+ "<<<< AVOutputDevice >>>> %s: Posting %{public}@"
+ "<<<< AVOutputDevice >>>> %s: Removing frecents entry for device %{private}@ which previously had an invalid or missing LastUsedTimestamp"
+ "<<<< AVOutputDevice >>>> %s: Using frecents file at %{public}@"
+ "<<<< AVOutputDevice >>>> %s: Using legacy CFPreferences-based frecents"
+ "<<<< AVOutputDevice >>>> %s: [%p] Posting %{public}@"
+ "<<<< AVOutputDevice >>>> %s: called"
+ "<<<< AVOutputDevice >>>> %s: called (allows=%d)"
+ "<<<< AVOutputDevice >>>> %s: called (cancelIfAuthRequired=%{public}@)"
+ "<<<< AVOutputDevice >>>> %s: called (channel=%p, delegate? %d)"
+ "<<<< AVOutputDevice >>>> %s: called (count=%ld)"
+ "<<<< AVOutputDevice >>>> %s: called (delegate? %d)"
+ "<<<< AVOutputDevice >>>> %s: called (device=%{private}@, dataDestination=%{public}@, cancelIfAuthRequired=%{public}@, correlationID=%{private}@, initiator=%{private}@, controlType=%{public}@)"
+ "<<<< AVOutputDevice >>>> %s: called (enabled=%d)"
+ "<<<< AVOutputDevice >>>> %s: called (mode=%{public}@)"
+ "<<<< AVOutputDevice >>>> %s: called (muted=%{BOOL}u)"
+ "<<<< AVOutputDevice >>>> %s: called (outputDevice=%p, delegate? %d)"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDevice >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDevice >>>> %s: called (volume=%f)"
+ "<<<< AVOutputDevice >>>> %s: result=%d, cancellationReason=%{public}@, error=%{public}@"
+ "<<<< AVOutputDevice >>>> %s: setting carplay video to %{BOOL}u"
+ "<<<< AVOutputDevice >>>> %s: setting second display mode to %{public}@..."
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: Calling FigEndpointUIAgentSetAuthValue (token=%{private}@, promptDismissed=%d)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: NULL prompt reason.  Assuming %{public}@"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: Unrecognized prompt reason %{public}@"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, request=%@, requestImpl=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, status=%d, error=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (self=%p, uniqueID=%@, routeDescriptor=%@, pinMode=%d, reason=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession (FigEndpointUIAgent) >>>> %s: called (uniqueID=%{public}@, PINMode=%d, reason=%{public}@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Calling -outputDeviceAuthorizationSession:didProvideAuthorizationRequest: on delegate (request/ID=%{public}@, request/outputDevice=%{private}@, request/authorizationTokenType=%{public}@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Calling -outputDeviceAuthorizationSession:shouldRetryAuthorizationRequest:reason: on delegate (request/ID=%{public}@, reason=%{public}@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Not messaging delegate because there is no delegate or it does not respond to -outputDeviceAuthorizationSession:didProvideAuthorizationRequest:"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Not messaging delegate because there is no delegate or it does not respond to -outputDeviceAuthorizationSession:shouldRetryAuthorizationRequest:reason:"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Received notification %@"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: Result: %d (error: %{public}@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (authorizationToken=%{private}@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: called (self=%p, delegate=%@)"
+ "<<<< AVOutputDeviceAuthorizationSession >>>> %s: self=%p, impl=%@, replacementImpl=%@"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: FigEndpointRemoteControlSessionSendMessage finished with response params %{public}@ (err=%d)"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: Sending %d bytes through comm channel via FigEndpointRemoteControlSessionSendMessage for channel=%p"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: Unrecognized event type: %@"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: called (channel=%p)"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: called (channel=%p, dataLength=%d)"
+ "<<<< AVOutputDeviceCommunicationChannel (FigRemoteControlSession) >>>> %s: called (channel=%p, inEventType=%{public}@, dataLength=%d)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Calling FigRoutingContextCreateCommChannelForDeviceID (control type: %d, clientTypeUUID: %{public}@ correlationID: %{private}@)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: FigRoutingContextSendDataForDeviceID finished for comm channel ID %{public}@ (err=%d)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No AVOutputDevice to connect to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No System Remote Pool to add to!"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: No comm channel found for ID %@ for device %@, synthesizing one for the delegate."
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Open comm channel completed for comm channel ID %{public}@ (err=%d)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Removing comm channel UUID %@ for device with ID %@"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: Sending %d bytes through comm channel ID %{public}@ via FigRoutingContextSendDataForDeviceID"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (commChannelUUID=%{public}@ dataLength=%d)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (commChannelUUID=%{public}@)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (device=%{private}@, cancelIfAuthRequired=%{public}@, correlationID=%{private}@, initiator=%{private}@)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: called (self=%p, options=%@, completionHandler=%p)"
+ "<<<< AVOutputDeviceCommunicationChannelManager (System Remote Pool) >>>> %s: initialized (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Failed to create replacement AVODDS impl"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_AvailableRouteDescriptors returned: %@ (err: %d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting cachedDiscoveryEnabled to %{BOOL}u (client: %{public}@) for session=%p"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting device discovery mode to %{public}@ (client: %{public}@) for session=%p"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting kFigRouteDiscovererProperty_AudioSessionID to %@"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Setting onlyDiscoversBluetoothDevices to %{BOOL}u (client: %{public}@) for session=%p"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: Unsupported device feature combination %d"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (payload=%@), (timeTaken: %llu ms)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%@, class=%@, deviceFeatures=%u)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: called (self=%p, routeDiscovererCreator=%@)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AudioSessionID = %@ (err=%d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_AvailableRoutes = %@ (err=%d)"
+ "<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> %s: kFigRouteDiscovererProperty_UserSelectionAvailable = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: *** nil impl! ***"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Available output devices: %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Posting %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: Returning %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (session=%p, discoveryMode=%d, clientIdentifiers=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (session=%p, setCachedDiscoveryEnabled=%{BOOL}u)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (session=%p, setOnlyDiscoversBluetoothDevices=%{BOOL}u)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: called (targetAudioSession=%@)"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: otherDevices = %@"
+ "<<<< AVOutputDeviceDiscoverySession >>>> %s: recentlyUsedDevices = %@"
+ "<<<< AVOutputDeviceGroup >>>> %s: Posting %{public}@"
+ "<<<< AVOutputDeviceGroup >>>> %s: Posting %{public}@ with initiator %{public}@"
+ "<<<< AVOutputDeviceGroup >>>> %s: Result: %{public}@"
+ "<<<< AVOutputDeviceGroup >>>> %s: called (device=%{private}@ authToken? %d cancelIfAuthRequired=%{public}@, initiator=%{public}@)"
+ "<<<< AVOutputDeviceGroup >>>> %s: called (device=%{private}@, initiator=%{public}@"
+ "<<<< AVOutputDeviceGroup >>>> %s: called (self=%p, impl=%@)"
+ "<<<< AVOutputDeviceGroup >>>> %s: outputDevices = %@"
+ "<<<< AVOutputDeviceHID >>>> %s: Setting input mode to %ld"
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
+ "<<<< AVRoutingError >>>> %s: Returning error (%{public}@ / %d) status (%d)"
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
+ "<<<< AVRoutingSessionManager >>>> %s: Calling FigRoutingSessionManagerStartSessionWithRouteDescriptors (routeDescriptors: %{private}@)"
+ "<<<< AVRoutingSessionManager >>>> %s: Calling FigRoutingSessionManagerStartSuppressingLikelyDestinationsUntilNextPlayEvent"
+ "<<<< AVRoutingSessionManager >>>> %s: Calling FigRoutingSessionManagerStopSuppressingLikelyDestinations"
+ "<<<< AVRoutingSessionManager >>>> %s: External destination confidence %f below threshold %f, clearing array (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: Fetched %d from %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: Result: %d)"
+ "<<<< AVRoutingSessionManager >>>> %s: Returning %@"
+ "<<<< AVRoutingSessionManager >>>> %s: Sum of external destination confidence: %f (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: called"
+ "<<<< AVRoutingSessionManager >>>> %s: called (deviceDescriptions=%{private}@)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (result=%d)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSession=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionDestination=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: called (self=%p, figRoutingSessionManager=%@)"
+ "<<<< AVRoutingSessionManager >>>> %s: calling FigRoutingSessionManagerStartSessionForHighConfidenceDestination"
+ "<<<< AVRoutingSessionManager >>>> %s: calling FigRoutingSessionManagerUpdateCurrentSessionFromLikelyDestinations"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (err: %d)"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: fetched %@ from FigRoutingSession (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: invoking completion handler with error %{public}@"
+ "<<<< AVRoutingSessionManager >>>> %s: kFigRoutingSessionProperty_EstablishedAutomaticallyFromLikelyDestination = %@"
+ "<<<< AVRoutingSessionManager >>>> %s: posting %{public}@"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %@ (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %d"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %d (self=%p)"
+ "<<<< AVRoutingSessionManager >>>> %s: returning %f (self=%p)"
+ "<missing entitlement>"
+ "@"
+ "@\"<AVFigRouteDiscovererFactory>\""
+ "@\"<AVFigRoutingContextCommunicationChannelManager>\""
+ "@\"<AVFigRoutingContextOutputDeviceTranslator>\""
+ "@\"<AVInputContextImpl>\""
+ "@\"<AVInputDeviceDiscoverySessionImpl>\""
+ "@\"<AVInputDeviceImpl>\""
+ "@\"<AVInputDeviceImplSupport>\""
+ "@\"<AVInputDeviceImplSupport>\"16@0:8"
+ "@\"<AVOutputContextCommunicationChannelDelegate>\""
+ "@\"<AVOutputContextCommunicationChannelImpl>\""
+ "@\"<AVOutputContextImpl>\""
+ "@\"<AVOutputContextManagerImpl>\""
+ "@\"<AVOutputDeviceAuthorizationRequestImpl>\""
+ "@\"<AVOutputDeviceAuthorizationSessionDelegate>\""
+ "@\"<AVOutputDeviceAuthorizationSessionImpl>\""
+ "@\"<AVOutputDeviceCommunicationChannelDelegate>\""
+ "@\"<AVOutputDeviceCommunicationChannelImpl>\""
+ "@\"<AVOutputDeviceCommunicationChannelManager>\""
+ "@\"<AVOutputDeviceConfigurationRetrieval>\""
+ "@\"<AVOutputDeviceDelegate>\""
+ "@\"<AVOutputDeviceDelegate>\"16@0:8"
+ "@\"<AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl>\""
+ "@\"<AVOutputDeviceDiscoverySessionImpl>\""
+ "@\"<AVOutputDeviceGroupImpl>\""
+ "@\"<AVOutputDeviceImpl>\""
+ "@\"<AVOutputDeviceImplSupport>\""
+ "@\"<AVOutputDeviceImplSupport>\"16@0:8"
+ "@\"<FigRoutingContextFactory>\""
+ "@\"AVAudioSession\"16@0:8"
+ "@\"AVFigCommChannelUUIDCommunicationChannelManager\"16@?0^{OpaqueFigRoutingContext=}8"
+ "@\"AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl\""
+ "@\"AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl\""
+ "@\"AVFigRoutingContextOutputContextImpl\""
+ "@\"AVFigRoutingContextOutputContextImpl\"16@0:8"
+ "@\"AVInputContext\""
+ "@\"AVInputContext\"16@0:8"
+ "@\"AVInputContextDestinationChange\""
+ "@\"AVInputContextDestinationChange\"16@0:8"
+ "@\"AVInputContextDestinationChangeInternal\""
+ "@\"AVInputContextInternal\""
+ "@\"AVInputDevice\"16@0:8"
+ "@\"AVInputDevice\"24@0:8@\"NSString\"16"
+ "@\"AVInputDeviceDiscoverySession\""
+ "@\"AVInputDeviceDiscoverySession\"16@0:8"
+ "@\"AVInputDeviceDiscoverySessionInternal\""
+ "@\"AVInputDeviceInternal\""
+ "@\"AVOutputContext\""
+ "@\"AVOutputContext\"16@0:8"
+ "@\"AVOutputContextCommunicationChannel\""
+ "@\"AVOutputContextCommunicationChannel\"16@0:8"
+ "@\"AVOutputContextCommunicationChannel\"32@0:8@\"NSDictionary\"16^@24"
+ "@\"AVOutputContextCommunicationChannelInternal\""
+ "@\"AVOutputContextDestinationChange\""
+ "@\"AVOutputContextDestinationChange\"16@0:8"
+ "@\"AVOutputContextDestinationChangeInternal\""
+ "@\"AVOutputContextInternal\""
+ "@\"AVOutputContextManager\""
+ "@\"AVOutputContextManager\"16@0:8"
+ "@\"AVOutputContextManagerInternal\""
+ "@\"AVOutputDevice\""
+ "@\"AVOutputDevice\"16@0:8"
+ "@\"AVOutputDevice\"24@0:8^{OpaqueFigRoutingContext=}16"
+ "@\"AVOutputDeviceAuthorizationRequest\""
+ "@\"AVOutputDeviceAuthorizationRequestInternal\""
+ "@\"AVOutputDeviceAuthorizationSession\""
+ "@\"AVOutputDeviceAuthorizationSession\"16@0:8"
+ "@\"AVOutputDeviceAuthorizationSessionInternal\""
+ "@\"AVOutputDeviceAuthorizedPeerInternal\""
+ "@\"AVOutputDeviceCommunicationChannel\""
+ "@\"AVOutputDeviceCommunicationChannel\"16@0:8"
+ "@\"AVOutputDeviceDiscoverySession\""
+ "@\"AVOutputDeviceDiscoverySession\"16@0:8"
+ "@\"AVOutputDeviceDiscoverySession\"32@0:8#16Q24"
+ "@\"AVOutputDeviceDiscoverySessionAvailableOutputDevices\"16@0:8"
+ "@\"AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal\""
+ "@\"AVOutputDeviceDiscoverySessionInternal\""
+ "@\"AVOutputDeviceInternal\""
+ "@\"AVPairedDeviceInternal\""
+ "@\"AVRoutingMutableScheduledAudioParametersInternal\""
+ "@\"AVRoutingScheduledAudioParametersInternal\""
+ "@\"AVRoutingSessionDestinationInternal\""
+ "@\"AVRoutingSessionInternal\""
+ "@\"AVRoutingSessionManagerInternal\""
+ "@\"AVRoutingWeakReference\""
+ "@\"MXRoutingContextModificationMetrics\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"24@0:8^{OpaqueFigRoutingContext=}16"
+ "@\"NSCondition\""
+ "@\"NSData\"16@0:8"
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSDictionary\"24@0:8@\"NSString\"16"
+ "@\"NSError\""
+ "@\"NSLock\""
+ "@\"NSMapTable\""
+ "@\"NSMutableArray\""
+ "@\"NSMutableDictionary\""
+ "@\"NSNumber\""
+ "@\"NSNumber\"16@0:8"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSOperation\""
+ "@\"NSOperationQueue\""
+ "@\"NSPointerArray\""
+ "@\"NSString\"16@0:8"
+ "@\"NSURL\""
+ "@\"NSValue\""
+ "@112@0:8{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}}16"
+ "@20@0:8B16"
+ "@20@0:8I16"
+ "@24@0:8#16"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@\"NSDictionary\"16"
+ "@24@0:8@?16"
+ "@24@0:8Q16"
+ "@24@0:8^v16"
+ "@24@0:8^{OpaqueFigEndpoint=}16"
+ "@24@0:8^{OpaqueFigEndpointRemoteControlSession=}16"
+ "@24@0:8^{OpaqueFigEndpointUIAgent=}16"
+ "@24@0:8^{OpaqueFigRoutingContext=}16"
+ "@24@0:8^{OpaqueFigRoutingSession=}16"
+ "@24@0:8^{OpaqueFigRoutingSessionManager=}16"
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8^{__CFDictionary=}16"
+ "@24@0:8^{__CFString=}16"
+ "@24@0:8^{opaqueCMNotificationCenter=}16"
+ "@24@0:8{?=ii}16"
+ "@32@0:8#16Q24"
+ "@32@0:8:16@24"
+ "@32@0:8@\"NSString\"16@\"NSDictionary\"24"
+ "@32@0:8@\"NSString\"16@\"NSString\"24"
+ "@32@0:8@16^@24"
+ "@32@0:8@16^{OpaqueFigRouteDiscoverer=}24"
+ "@32@0:8@?16@24"
+ "@32@0:8@?16@?24"
+ "@32@0:8@?16^{OpaqueFigVolumeControllerState=}24"
+ "@32@0:8^{OpaqueFigEndpoint=}16@24"
+ "@32@0:8^{OpaqueFigEndpoint=}16^{OpaqueFigVolumeControllerState=}24"
+ "@32@0:8^{OpaqueFigRoutingContext=}16@?24"
+ "@32@0:8^{OpaqueFigRoutingContext=}16^{__CFString=}24"
+ "@32@0:8^{__CFDictionary=}16@24"
+ "@32@0:8^{__CFDictionary=}16^{OpaqueFigRouteDiscoverer=}24"
+ "@32@0:8^{__CFDictionary=}16^{OpaqueFigRoutingContext=}24"
+ "@32@0:8^{__CFDictionary=}16^{OpaqueFigVolumeControllerState=}24"
+ "@32@0:8^{__CFString=}16@24"
+ "@32@0:8q16@24"
+ "@36@0:8@16@24B32"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16@24^{OpaqueFigEndpoint=}32"
+ "@40@0:8@16^{__CFString=}24@32"
+ "@40@0:8@?16@24^{OpaqueFigRoutingContext=}32"
+ "@40@0:8^{OpaqueFigEndpoint=}16@24@32"
+ "@40@0:8{?=qiIq}16"
+ "@44@0:8^{OpaqueFigEndpoint=}16^{OpaqueFigVolumeControllerState=}24@32B40"
+ "@44@0:8^{OpaqueFigRoutingContext=}16^{__CFString=}24@?32B40"
+ "@48@0:8@16B24B28@32@40"
+ "@48@0:8@16^?24@32^v40"
+ "@48@0:8@16^?24^{__CFString=}32^v40"
+ "@52@0:8@16@24@32B40@44"
+ "@52@0:8@16@24q32B40@44"
+ "@52@0:8^{__CFDictionary=}16^{OpaqueFigRouteDiscoverer=}24@32B40^{OpaqueFigRoutingContext=}44"
+ "@56@0:8#16{?=qiIq}24^{?={?=qiIq}{?=qiIq}}48"
+ "@56@0:8^{OpaqueFigRoutingContext=}16@?24@32^{OpaqueFigVolumeControllerState=}40@?48"
+ "@60@0:8^{__CFDictionary=}16^{OpaqueFigRouteDiscoverer=}24^{OpaqueFigVolumeControllerState=}32@40B48^{OpaqueFigRoutingContext=}52"
+ "@64@0:8{?={?=qiIq}{?=qiIq}}16"
+ "@68@0:8{?={?=qiIq}{?=qiIq}}16f64"
+ "@72@0:8f16f20{?={?=qiIq}{?=qiIq}}24"
+ "@80@0:8f16f20{?={?=qiIq}{?=qiIq}}24q72"
+ "@?"
+ "@?16@0:8"
+ "A"
+ "AVAudioSession"
+ "AVBlockScheduler"
+ "AVClusterComponentOutputDeviceDescription"
+ "AVCommChannelDidClose"
+ "AVCommChannelDidReceiveData"
+ "AVCurrentRouteDiscovererFactoryKey"
+ "AVDefaultRoutingContextFactory"
+ "AVDestinationChangeResultSource"
+ "AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices"
+ "AVExecutionEnvironment"
+ "AVExecutionEnvironmentCurrentPlatformIdentifierKey"
+ "AVFigCommChannelUUIDCommunicationChannelManager"
+ "AVFigCommChannelUUIDOutputContextCommunicationChannelImpl"
+ "AVFigEndpointFigRoutingContextOutputDeviceTranslator"
+ "AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl"
+ "AVFigEndpointOutputDeviceImpl"
+ "AVFigEndpointOutputDeviceImplCanSetEndpointVolumeDidChange"
+ "AVFigEndpointOutputDeviceImplEndpointCanMuteDidChange"
+ "AVFigEndpointOutputDeviceImplEndpointMutedDidChange"
+ "AVFigEndpointOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigEndpointOutputDeviceImplEndpointVolumeControlTypeDidChange"
+ "AVFigEndpointOutputDeviceImplEndpointVolumeDidChange"
+ "AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImpl"
+ "AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImplHandleEvent"
+ "AVFigEndpointRemoteControlSessionOutputDeviceCommunicationChannelImplSendDataCompletion"
+ "AVFigEndpointSecondDisplayModeToken"
+ "AVFigEndpointUIAgentOutputContextManagerImpl"
+ "AVFigEndpointUIAgentOutputContextManagerSharedEndpointUIAgentDidChangeNotification"
+ "AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl"
+ "AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl"
+ "AVFigRemoteRouteDiscovererFactory"
+ "AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator"
+ "AVFigRouteDescriptorInputDeviceImpl"
+ "AVFigRouteDescriptorInputDeviceImpl.m"
+ "AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl"
+ "AVFigRouteDescriptorOutputDeviceImpl"
+ "AVFigRouteDescriptorOutputDeviceImpl.m"
+ "AVFigRouteDescriptorOutputDeviceImplCanSetEndpointVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointCanMuteDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointMutedDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointRoomVolumeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeControlTypeDidChange"
+ "AVFigRouteDescriptorOutputDeviceImplEndpointVolumeDidChange"
+ "AVFigRouteDiscovererAvailableRoutesChanged"
+ "AVFigRouteDiscovererEndpointDescriptorChanged"
+ "AVFigRouteDiscovererFactory"
+ "AVFigRouteDiscovererInputDeviceDiscoverySessionImpl"
+ "AVFigRouteDiscovererInputDeviceDiscoverySessionImpl.m"
+ "AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory"
+ "AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl"
+ "AVFigRouteDiscovererRoutePresentChanged"
+ "AVFigRouteDiscovererRouteServerDied"
+ "AVFigRouteDiscovererUpdateEndpointFeatures"
+ "AVFigRouteDiscovererUpdateEndpointFeaturesCompletionCallback"
+ "AVFigRouteDiscovererUpdateEndpointFeaturesCompletionContext"
+ "AVFigRoutingContextCommunicationChannelManager"
+ "AVFigRoutingContextCurrentRouteChanged"
+ "AVFigRoutingContextGroupConfigurationChanged"
+ "AVFigRoutingContextInputContextCompletionContext"
+ "AVFigRoutingContextInputContextImpl"
+ "AVFigRoutingContextInputContextImpl.m"
+ "AVFigRoutingContextModificationCallback"
+ "AVFigRoutingContextOutputContextCompletionContext"
+ "AVFigRoutingContextOutputContextImpl"
+ "AVFigRoutingContextOutputDeviceTranslator"
+ "AVFigRoutingContextPredictedSelectedRouteDescriptorChanged"
+ "AVFigRoutingContextRemoteControlChannelAvailabilityChanged"
+ "AVFigRoutingContextRouteChangeEnded"
+ "AVFigRoutingContextRouteChangeStarted"
+ "AVFigRoutingContextRouteConfigUpdated"
+ "AVFigRoutingContextSendDataCompletion"
+ "AVFigRoutingContextServerConnectionDied"
+ "AVFigRoutingContextSystemAudioRouteConfigUpdated"
+ "AVFigRoutingContextSystemPickerVideoRouteChanged"
+ "AVFigVolumeControllerCanMuteDidChange"
+ "AVFigVolumeControllerCanSetMasterVolumeDidChange"
+ "AVFigVolumeControllerCanUseForRoutingContextDidChange"
+ "AVFigVolumeControllerMasterVolumeControlTypeDidChange"
+ "AVFigVolumeControllerMasterVolumeDidChange"
+ "AVFigVolumeControllerMuteDidChange"
+ "AVFoundationErrorDomain"
+ "AVInputContext"
+ "AVInputContextDestinationChange"
+ "AVInputContextDestinationChangeInitiatedNotification"
+ "AVInputContextDestinationChangeInitiatorKey"
+ "AVInputContextDestinationChangeInternal"
+ "AVInputContextDestinationChangeKey"
+ "AVInputContextImpl"
+ "AVInputContextInputDeviceDidChangeNotification"
+ "AVInputContextInternal"
+ "AVInputContextSerializationKeyContextID"
+ "AVInputContextSerializationKeyContextType"
+ "AVInputContextSetInputDeviceHostApplicationBundleIDKey"
+ "AVInputContextSetInputDeviceInitiatorKey"
+ "AVInputContextTypeSharedSystemAudioInput"
+ "AVInputDevice"
+ "AVInputDeviceDiscoverySession"
+ "AVInputDeviceDiscoverySessionAvailableInputDevicesDidChangeNotification"
+ "AVInputDeviceDiscoverySessionImpl"
+ "AVInputDeviceDiscoverySessionInternal"
+ "AVInputDeviceGetDeviceTypeAndSubTypeFromRouteDescriptor"
+ "AVInputDeviceGetFigRouteDescriptor"
+ "AVInputDeviceImpl"
+ "AVInputDeviceInternal"
+ "AVLocalOutputDeviceImpl"
+ "AVLocalizedError"
+ "AVLocalizedErrorWithUnderlyingOSStatus"
+ "AVMakeAddEndpointOperation_block_invoke"
+ "AVMakeAddRouteDescriptorOperation_block_invoke"
+ "AVMakeRemoveEndpointOperation_block_invoke"
+ "AVMakeRemoveRouteDescriptorOperation_block_invoke"
+ "AVMakeSelectEndpointOperation_block_invoke"
+ "AVMakeSelectEndpointsOperation_block_invoke"
+ "AVMakeSelectRouteDescriptorOperation_block_invoke"
+ "AVMakeSelectRouteDescriptorsOperation_block_invoke"
+ "AVObjectMonitoring"
+ "AVOutputContext"
+ "AVOutputContextAddOutputDeviceCancelIfAuthRequiredKey"
+ "AVOutputContextAddOutputDeviceOptionAuthorizationToken"
+ "AVOutputContextAddOutputDeviceOptionCorrelationID"
+ "AVOutputContextAddOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextAddOutputDeviceOptionFadePlayback"
+ "AVOutputContextAddOutputDeviceOptionInitiator"
+ "AVOutputContextAddOutputDeviceOptionMuteUntilContextModificationIsFinished"
+ "AVOutputContextCanMuteDidChangeNotification"
+ "AVOutputContextCanSetVolumeDidChangeNotification"
+ "AVOutputContextCommunicationChannel"
+ "AVOutputContextCommunicationChannelControlTypeDirect"
+ "AVOutputContextCommunicationChannelControlTypeRelayed"
+ "AVOutputContextCommunicationChannelImpl"
+ "AVOutputContextCommunicationChannelInternal"
+ "AVOutputContextCommunicationChannelOptionControlType"
+ "AVOutputContextDestinationChange"
+ "AVOutputContextDestinationChangeCancellationReasonAuthorizationSkipped"
+ "AVOutputContextDestinationChangeDeviceIDKey"
+ "AVOutputContextDestinationChangeInitiatedNotification"
+ "AVOutputContextDestinationChangeInitiatorKey"
+ "AVOutputContextDestinationChangeInternal"
+ "AVOutputContextDestinationChangeKey"
+ "AVOutputContextDestinationChangePreviousDeviceIDsKey"
+ "AVOutputContextDestinationChangeReasonIdleDisconnect"
+ "AVOutputContextDestinationChangeReasonKey"
+ "AVOutputContextDeviceConnectionFailureReasonDeviceInUse"
+ "AVOutputContextDeviceConnectionFailureReasonDeviceNotConnectedToInternet"
+ "AVOutputContextDeviceConnectionFailureReasonDeviceNotMFiCertified"
+ "AVOutputContextDeviceConnectionFailureReasonDeviceOutOfRange"
+ "AVOutputContextDeviceConnectionFailureReasonInfraRelayFailed2GHzNetwork"
+ "AVOutputContextDeviceConnectionFailureReasonInfraRelayFailedMultiDFSNetwork"
+ "AVOutputContextDeviceConnectionFailureReasonNotAPeerInHomeGroup"
+ "AVOutputContextDeviceGroupControlOptionCancelAddDeviceIfAuthRequired"
+ "AVOutputContextFactory"
+ "AVOutputContextGlobalOutputDeviceConfigurationDidChangeNotification"
+ "AVOutputContextImpl"
+ "AVOutputContextInternal"
+ "AVOutputContextManager"
+ "AVOutputContextManagerDidFailToConnectToOutputDeviceUserInfoKey"
+ "AVOutputContextManagerFailureReasonKey"
+ "AVOutputContextManagerImpl"
+ "AVOutputContextManagerInternal"
+ "AVOutputContextManagerOutputContextDidFailToConnectToOutputDeviceNotification"
+ "AVOutputContextManagerOutputDeviceKey"
+ "AVOutputContextManagerServerConnectionDied"
+ "AVOutputContextManagerShowErrorPrompt"
+ "AVOutputContextModificationResult"
+ "AVOutputContextMutedDidChangeNotification"
+ "AVOutputContextOutputDeviceDidChangeNotification"
+ "AVOutputContextOutputDevicesDidChangeNotification"
+ "AVOutputContextOutputDevicesModificationOptionCorrelationID"
+ "AVOutputContextOutputDevicesModificationOptionUserInitiated"
+ "AVOutputContextPredictedOutputDeviceDidChangeNotification"
+ "AVOutputContextProvidesControlForAllVolumeFeaturesDidChangeNotification"
+ "AVOutputContextRemoveOutputDeviceOptionContinuePlayingAfterLastDeviceRemoved"
+ "AVOutputContextRemoveOutputDeviceOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextRemoveOutputDeviceOptionFadePlayback"
+ "AVOutputContextRemoveOutputDeviceOptionInitiator"
+ "AVOutputContextSerializationKeyContextID"
+ "AVOutputContextSerializationKeyContextType"
+ "AVOutputContextSetOutputDeviceCancelIfAuthRequiredKey"
+ "AVOutputContextSetOutputDeviceDefaultAudioToLocalKey"
+ "AVOutputContextSetOutputDeviceDidFailToConnectToOutputDeviceUserInfoKey"
+ "AVOutputContextSetOutputDeviceFadePlaybackKey"
+ "AVOutputContextSetOutputDeviceInitiatorKey"
+ "AVOutputContextSetOutputDeviceMuteUntilContextModificationIsFinishedKey"
+ "AVOutputContextSetOutputDevicePasswordKey"
+ "AVOutputContextSetOutputDeviceSuppressUserInteractionOnSenderOnlyKey"
+ "AVOutputContextSetOutputDevicesOptionDidFailToConnectToOutputDeviceUserInfo"
+ "AVOutputContextSetOutputDevicesOptionFadePlayback"
+ "AVOutputContextSetOutputDevicesOptionInitiator"
+ "AVOutputContextSetOutputDevicesOptionMuteUntilContextModificationIsFinished"
+ "AVOutputContextTypeAudio"
+ "AVOutputContextTypeGroupControl"
+ "AVOutputContextTypeScreen"
+ "AVOutputContextTypeSharedAudioPresentation"
+ "AVOutputContextTypeSharedSystemAudio"
+ "AVOutputContextTypeSharedSystemRemotePool"
+ "AVOutputContextTypeSharedSystemScreen"
+ "AVOutputContextTypeSystemRemoteDisplay"
+ "AVOutputContextTypeVideo"
+ "AVOutputContextUsesRouteConfigUpdatedNotification"
+ "AVOutputContextVolumeControlTypeDidChangeNotification"
+ "AVOutputContextVolumeDidChangeNotification"
+ "AVOutputDevice"
+ "AVOutputDeviceActivatedClusterMembersRoomIDKey"
+ "AVOutputDeviceActivatedClusterMembersRoomVolumeDidChangeNotification"
+ "AVOutputDeviceAuthorizationRequest"
+ "AVOutputDeviceAuthorizationRequestImpl"
+ "AVOutputDeviceAuthorizationRequestInternal"
+ "AVOutputDeviceAuthorizationRequestRetryReasonIncorrectAuthorizationToken"
+ "AVOutputDeviceAuthorizationSession"
+ "AVOutputDeviceAuthorizationSessionImpl"
+ "AVOutputDeviceAuthorizationSessionInternal"
+ "AVOutputDeviceAuthorizationSessionShowAuthPrompt"
+ "AVOutputDeviceAuthorizationSessionShowFinishedWithPrompt"
+ "AVOutputDeviceAuthorizationTokenTypePIN"
+ "AVOutputDeviceAuthorizationTokenTypePassword"
+ "AVOutputDeviceAuthorizedPeer"
+ "AVOutputDeviceAuthorizedPeerInternal"
+ "AVOutputDeviceBatteryLevelCaseKey"
+ "AVOutputDeviceBatteryLevelLeftKey"
+ "AVOutputDeviceBatteryLevelRightKey"
+ "AVOutputDeviceBluetoothAlternateTransportTypeDefault"
+ "AVOutputDeviceBluetoothAlternateTransportTypeUSBC"
+ "AVOutputDeviceBluetoothListeningModeActiveNoiseCancellation"
+ "AVOutputDeviceBluetoothListeningModeAudioTransparency"
+ "AVOutputDeviceBluetoothListeningModeAutomatic"
+ "AVOutputDeviceBluetoothListeningModeNormal"
+ "AVOutputDeviceCanMuteDidChangeNotification"
+ "AVOutputDeviceCanSetVolumeDidChangeNotification"
+ "AVOutputDeviceCarPlayTestNotification"
+ "AVOutputDeviceCommunicationChannel"
+ "AVOutputDeviceCommunicationChannelControlTypeDirect"
+ "AVOutputDeviceCommunicationChannelControlTypeRelayed"
+ "AVOutputDeviceCommunicationChannelDataDestinationCarPlayClusterControl"
+ "AVOutputDeviceCommunicationChannelDataDestinationCarPlayData"
+ "AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataLogging"
+ "AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataUpdate"
+ "AVOutputDeviceCommunicationChannelDataDestinationCarPlayDataVersionTwo"
+ "AVOutputDeviceCommunicationChannelDataDestinationFitness"
+ "AVOutputDeviceCommunicationChannelDataDestinationMediaRemote"
+ "AVOutputDeviceCommunicationChannelImpl"
+ "AVOutputDeviceCommunicationChannelManager"
+ "AVOutputDeviceCommunicationChannelOpenCancellationReasonAuthorizationSkipped"
+ "AVOutputDeviceCommunicationChannelOptionAwaitReply"
+ "AVOutputDeviceCommunicationChannelOptionCancelIfAuthRequired"
+ "AVOutputDeviceCommunicationChannelOptionClientUUID"
+ "AVOutputDeviceCommunicationChannelOptionControlType"
+ "AVOutputDeviceCommunicationChannelOptionCorrelationID"
+ "AVOutputDeviceCommunicationChannelOptionInitiator"
+ "AVOutputDeviceCommunicationChannelOptionQualityOfService"
+ "AVOutputDeviceCommunicationChannelOptionStreamPriority"
+ "AVOutputDeviceCommunicationChannelOptionUsePerCommChannelDelegate"
+ "AVOutputDeviceConfigurationCancellationReasonAuthorizationSkipped"
+ "AVOutputDeviceConfigurationModification"
+ "AVOutputDeviceConfigurationOptionCancelConfigurationIfAuthRequired"
+ "AVOutputDeviceConfigurationRetrieval"
+ "AVOutputDeviceCopyFigModeForSpatialAudioMode"
+ "AVOutputDeviceDescription"
+ "AVOutputDeviceDescriptionsFromFigDescriptions"
+ "AVOutputDeviceDiscoverySession"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDeviceGroupsDidChangeNotification"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDevices"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDevicesDidChangeNotification"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDevicesImpl"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal"
+ "AVOutputDeviceDiscoverySessionAvailableOutputDevices_FigEndpointImpl"
+ "AVOutputDeviceDiscoverySessionFactory"
+ "AVOutputDeviceDiscoverySessionImpl"
+ "AVOutputDeviceDiscoverySessionInternal"
+ "AVOutputDeviceElectronicTollCollectionStateChangedNotification"
+ "AVOutputDeviceFigEndpointImplFetching"
+ "AVOutputDeviceFrecencyManager"
+ "AVOutputDeviceFrecentsReader"
+ "AVOutputDeviceFrecentsReading"
+ "AVOutputDeviceFrecentsWriter"
+ "AVOutputDeviceFrecentsWriting"
+ "AVOutputDeviceGetFigEndpoint"
+ "AVOutputDeviceGetFigRouteDescriptor"
+ "AVOutputDeviceGroup"
+ "AVOutputDeviceGroupAddOutputDeviceOptionAuthorizationToken"
+ "AVOutputDeviceGroupAddOutputDeviceOptionCancelIfAuthRequiredKey"
+ "AVOutputDeviceGroupAddOutputDeviceOptionInitiator"
+ "AVOutputDeviceGroupMembershipChangeInitiator"
+ "AVOutputDeviceGroupMembershipChangeResult"
+ "AVOutputDeviceGroupMembershipChangeResultCancellationReasonAuthorizationSkipped"
+ "AVOutputDeviceGroupOutputDevicesDidChangeNotification"
+ "AVOutputDeviceGroupRemoveOutputDeviceOptionContinuePlayingAfterLastDeviceRemoved"
+ "AVOutputDeviceGroupRemoveOutputDeviceOptionInitiator"
+ "AVOutputDeviceGroupVolumeControlTypeDidChangeNotification"
+ "AVOutputDeviceGroupVolumeDidChangeNotification"
+ "AVOutputDeviceHID"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeAlways"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeAutomatic"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeFromFigMode"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeMultichannelOnly"
+ "AVOutputDeviceHeadTrackedSpatialAudioModeNever"
+ "AVOutputDeviceIcon"
+ "AVOutputDeviceImpl"
+ "AVOutputDeviceImplCanMuteForEndpointID"
+ "AVOutputDeviceImplChangeRoomVolumeForEndpoint"
+ "AVOutputDeviceImplChangeVolumeByCount"
+ "AVOutputDeviceImplIsMutedForEndpointID"
+ "AVOutputDeviceImplSetMutedForEndpointID"
+ "AVOutputDeviceInternal"
+ "AVOutputDeviceIsInEarKey"
+ "AVOutputDeviceLegacyFrecentsReader"
+ "AVOutputDeviceLegacyFrecentsWriter"
+ "AVOutputDeviceLimitedUIChangedNotification"
+ "AVOutputDeviceLocalDeviceDidChangeNotification"
+ "AVOutputDeviceMFiCertificateSerialNumberChangedNotification"
+ "AVOutputDeviceMediaSessionStatusDidChangeNotification"
+ "AVOutputDeviceMutedDidChangeNotification"
+ "AVOutputDeviceNavigationAidedDrivingStateChangedNotification"
+ "AVOutputDeviceNightModeChangedNotification"
+ "AVOutputDeviceOwnsTurnByTurnNavigationChangedNotification"
+ "AVOutputDevicePerformHapticFeedback"
+ "AVOutputDevicePerformanceReportPostedNotification"
+ "AVOutputDeviceProposedGroupIDDidChangeNotification"
+ "AVOutputDeviceRouteDiscovererServerDeathNotificationCallback"
+ "AVOutputDeviceScreenBecameAvailableNotification"
+ "AVOutputDeviceScreenBecameUnavailableNotification"
+ "AVOutputDeviceScreenBorrowToken"
+ "AVOutputDeviceScreenInfo"
+ "AVOutputDeviceSecondDisplayModeDefault"
+ "AVOutputDeviceSecondDisplayModeMediaPresentation"
+ "AVOutputDeviceSetAllowsHeadTrackedSpatialAudioOnEndpoint"
+ "AVOutputDeviceSetHeadTrackedSpatialAudioModeOnEndpoint"
+ "AVOutputDeviceSetMediaRemoteDataOnEndpoint"
+ "AVOutputDeviceSetSecondDisplayEnabledOnEndpoint"
+ "AVOutputDeviceSetSecondDisplayModeOnEndpoint"
+ "AVOutputDeviceSiriRequestedActionKey"
+ "AVOutputDeviceSiriRequestedNotification"
+ "AVOutputDeviceSiriRequestedTimestampKey"
+ "AVOutputDeviceSuggestUIWithURLSAndCompletionHandler"
+ "AVOutputDeviceSupportsDataOverACLProtocolKey"
+ "AVOutputDeviceTurnByTurnToken"
+ "AVOutputDeviceUnhandledRemoteEventCommandParametersKey"
+ "AVOutputDeviceUnhandledRemoteEventCommandTypeKey"
+ "AVOutputDeviceUnhandledRemoteEventNotification"
+ "AVOutputDeviceVehicleHasMainAudioNotification"
+ "AVOutputDeviceVehicleHasScreenForAirPlayVideoNotification"
+ "AVOutputDeviceViewAreaInfo"
+ "AVOutputDeviceVoiceTriggerModeChangedNotification"
+ "AVOutputDeviceVolumeControlTypeDidChangeNotification"
+ "AVOutputDeviceVolumeDidChangeNotification"
+ "AVOutputDeviceiOSEntityHasMainAudioNotification"
+ "AVOutputDeviceiOSUIRequestedApplicationURLKey"
+ "AVOutputDeviceiOSUIRequestedDisplayUUIDKey"
+ "AVOutputDeviceiOSUIRequestedNotification"
+ "AVPairedDevice"
+ "AVPairedDeviceInternal"
+ "AVPlatformIdentifierIOS"
+ "AVPlatformIdentifierMacOS"
+ "AVPlatformIdentifierTVOS"
+ "AVPlatformIdentifierWatchOS"
+ "AVPlatformIdentifierXROS"
+ "AVRoutingAmbienceLevelRamp"
+ "AVRoutingAmbienceLoudnessRamp"
+ "AVRoutingBlockOperation"
+ "AVRoutingCMNotificationDispatcher"
+ "AVRoutingCMNotificationDispatcherListenerKey"
+ "AVRoutingCallbackContextRegistry"
+ "AVRoutingContextCommandOutputDeviceConfiguration"
+ "AVRoutingContextCommandOutputDeviceConfigurationModification"
+ "AVRoutingContextRouteChangeOperation"
+ "AVRoutingContextRouteChangeOperationRouteChangeComplete"
+ "AVRoutingContextSendConfigureDeviceCommandOperation"
+ "AVRoutingDepartureAnnouncingObjectMonitor"
+ "AVRoutingDepartureAnnouncingObjectMonitorKey"
+ "AVRoutingDialogLevelRamp"
+ "AVRoutingDialogLoudnessRamp"
+ "AVRoutingDialogMixBiasRamp"
+ "AVRoutingDispatchOnce"
+ "AVRoutingError"
+ "AVRoutingErrorAirPlayControllerRequiresInternet"
+ "AVRoutingErrorAirPlayReceiverRequiresInternet"
+ "AVRoutingErrorAirPlayReceiverTemporarilyUnavailable"
+ "AVRoutingErrorApplicationIsNotAuthorized"
+ "AVRoutingErrorApplicationIsNotAuthorizedToUseDevice"
+ "AVRoutingErrorClientProgrammingError"
+ "AVRoutingErrorCompositionTrackSegmentsNotContiguous"
+ "AVRoutingErrorContentIsNotAuthorized"
+ "AVRoutingErrorContentIsProtected"
+ "AVRoutingErrorContentIsUnavailable"
+ "AVRoutingErrorContentNotUpdated"
+ "AVRoutingErrorDecodeFailed"
+ "AVRoutingErrorDecoderNotFound"
+ "AVRoutingErrorDecoderTemporarilyUnavailable"
+ "AVRoutingErrorDeviceAlreadyUsedByAnotherSession"
+ "AVRoutingErrorDeviceInUseByAnotherApplication"
+ "AVRoutingErrorDeviceIsNotAvailableInBackground"
+ "AVRoutingErrorDeviceKey"
+ "AVRoutingErrorDeviceLockedForConfigurationByAnotherProcess"
+ "AVRoutingErrorDeviceNotConnected"
+ "AVRoutingErrorDeviceWasDisconnected"
+ "AVRoutingErrorDiskFull"
+ "AVRoutingErrorEncodeFailed"
+ "AVRoutingErrorEncoderNotFound"
+ "AVRoutingErrorEncoderTemporarilyUnavailable"
+ "AVRoutingErrorExportFailed"
+ "AVRoutingErrorExternalPlaybackNotSupportedForAsset"
+ "AVRoutingErrorFailedToLoadMediaData"
+ "AVRoutingErrorFailedToLoadSampleData"
+ "AVRoutingErrorFailedToParse"
+ "AVRoutingErrorFileAlreadyExists"
+ "AVRoutingErrorFileChecksumFailed"
+ "AVRoutingErrorFileFailedToParse"
+ "AVRoutingErrorFileFormatNotRecognized"
+ "AVRoutingErrorFileTypeDoesNotSupportSampleReferences"
+ "AVRoutingErrorFileTypeKey"
+ "AVRoutingErrorFileWritingExceededPredeterminedSize"
+ "AVRoutingErrorFormatUnsupported"
+ "AVRoutingErrorFourCharCode"
+ "AVRoutingErrorIncompatibleAsset"
+ "AVRoutingErrorIncorrectPIN"
+ "AVRoutingErrorIncorrectPassword"
+ "AVRoutingErrorIncorrectlyConfigured"
+ "AVRoutingErrorInvalidCompositionTrackSegmentDuration"
+ "AVRoutingErrorInvalidCompositionTrackSegmentSourceDuration"
+ "AVRoutingErrorInvalidCompositionTrackSegmentSourceStartTime"
+ "AVRoutingErrorInvalidFileAtDownloadDestinationURL"
+ "AVRoutingErrorInvalidOutputURLPathExtension"
+ "AVRoutingErrorInvalidSampleCursor"
+ "AVRoutingErrorInvalidSourceMedia"
+ "AVRoutingErrorInvalidVideoComposition"
+ "AVRoutingErrorMalformedDepth"
+ "AVRoutingErrorMaximumDurationReached"
+ "AVRoutingErrorMaximumFileSizeReached"
+ "AVRoutingErrorMaximumNumberOfSamplesForFileFormatReached"
+ "AVRoutingErrorMaximumStillImageCaptureRequestsExceeded"
+ "AVRoutingErrorMediaChanged"
+ "AVRoutingErrorMediaDataWritingExceededPredeterminedSize"
+ "AVRoutingErrorMediaDiscontinuity"
+ "AVRoutingErrorMediaServicesWereReset"
+ "AVRoutingErrorMediaTypeKey"
+ "AVRoutingErrorNoCompatibleAlternatesForExternalDisplay"
+ "AVRoutingErrorNoDataCaptured"
+ "AVRoutingErrorNoImageAtTime"
+ "AVRoutingErrorNoLongerPlayable"
+ "AVRoutingErrorNoSourceTrack"
+ "AVRoutingErrorOperationCancelled"
+ "AVRoutingErrorOperationInterrupted"
+ "AVRoutingErrorOperationNotAllowed"
+ "AVRoutingErrorOperationNotSupportedForAsset"
+ "AVRoutingErrorOperationNotSupportedForPreset"
+ "AVRoutingErrorOperationRequiresBothBudsInEar"
+ "AVRoutingErrorOutOfMemory"
+ "AVRoutingErrorPointlessOverCapture"
+ "AVRoutingErrorRecordingAlreadyInProgress"
+ "AVRoutingErrorRecordingNotAllowedWhenMultipleAppsAreForeground"
+ "AVRoutingErrorReferenceForbiddenByReferencePolicy"
+ "AVRoutingErrorRosettaNotInstalled"
+ "AVRoutingErrorSandboxExtensionDenied"
+ "AVRoutingErrorSegmentStartedWithNonSyncSample"
+ "AVRoutingErrorServerIncorrectlyConfigured"
+ "AVRoutingErrorSessionConfigurationChanged"
+ "AVRoutingErrorSessionHardwareCostOverage"
+ "AVRoutingErrorSessionNotRunning"
+ "AVRoutingErrorSessionWasInterrupted"
+ "AVRoutingErrorTorchLevelUnavailable"
+ "AVRoutingErrorUndecodableMediaData"
+ "AVRoutingErrorUnknown"
+ "AVRoutingErrorUnsupportedDeviceActiveFormat"
+ "AVRoutingErrorUnsupportedOutputSettings"
+ "AVRoutingErrorVideoCompositorFailed"
+ "AVRoutingError_trace"
+ "AVRoutingEventWaiter"
+ "AVRoutingGlobalOperationQueue"
+ "AVRoutingMutableScheduledAudioParameters"
+ "AVRoutingOperation"
+ "AVRoutingOperationQueueWithFundamentalDependency"
+ "AVRoutingOperationStatusResolveOldAndNew"
+ "AVRoutingOperation_trace"
+ "AVRoutingPlaybackArbiter"
+ "AVRoutingPlaybackArbiterInternalSupport"
+ "AVRoutingPlaybackParticipantExternalPlaybackStatusDidChangeNotification"
+ "AVRoutingPlaybackParticipantRegistration"
+ "AVRoutingRecordingLoudnessRamp"
+ "AVRoutingRenderingStyleRamp"
+ "AVRoutingRetainReleaseWeakReference"
+ "AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperation"
+ "AVRoutingRouteConfigUpdatedFigRoutingContextRouteChangeOperationRouteConfigUpdated"
+ "AVRoutingScheduledAudioParameters"
+ "AVRoutingScheduledAudioParametersInternal"
+ "AVRoutingScheduledAudioParameters_Internal"
+ "AVRoutingScheduledFloatValueRamp"
+ "AVRoutingScheduledParameterRamp"
+ "AVRoutingScheduledParameterRampSerialization"
+ "AVRoutingScheduledVolumeRamp"
+ "AVRoutingSerializedMostlySynchronousReentrantBlockScheduler"
+ "AVRoutingSession"
+ "AVRoutingSessionDestination"
+ "AVRoutingSessionDestinationInternal"
+ "AVRoutingSessionInternal"
+ "AVRoutingSessionManager"
+ "AVRoutingSessionManagerAllLikelyDestinationsDidChangeNotification"
+ "AVRoutingSessionManagerCurrentSessionChanged"
+ "AVRoutingSessionManagerCurrentSessionDidChangeNotification"
+ "AVRoutingSessionManagerGetLikelyDestinationsFromFig"
+ "AVRoutingSessionManagerInternal"
+ "AVRoutingSessionManagerInvokeStartHighConfidenceCompletionHandler"
+ "AVRoutingSessionManagerLikelyDestinationsChanged"
+ "AVRoutingSessionManagerLikelyExternalDestinationsDidChangeNotification"
+ "AVRoutingSessionManagerStartHighConfidenceDestinationComplete"
+ "AVRoutingSynchronousBlockScheduler"
+ "AVRoutingWaitForNotificationOrDeallocationOperation"
+ "AVRoutingWeakReference"
+ "AVSendCommandCompletion"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelImpl"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManager"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidCloseCommChannel"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelManagerDidReceiveData"
+ "AVSystemRemotePoolOutputDeviceCommunicationChannelSendDataCompletion"
+ "AVTimeCoding"
+ "AVVolumeController"
+ "Add endpoint %@ to routing context %@"
+ "Add route descriptor %@ to routing context %@"
+ "AirPlayVideoPlaybackAudioOnlyMode"
+ "AlternateSiri"
+ "ArrayOfOperations"
+ "AuthenticationData"
+ "AuthenticationType"
+ "AutoANC"
+ "B16@?0@\"AVRoutingSessionDestination\"8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8^@16"
+ "B24@0:8^i16"
+ "B28@0:8B16^@20"
+ "B32@0:8@\"NSString\"16^@24"
+ "B32@0:8@16Q24"
+ "B32@0:8@16^@24"
+ "B32@0:8q16q24"
+ "B32@?0@8Q16^B24"
+ "B40@0:8@16@24@32"
+ "B48@0:8q16@24^q32^@40"
+ "B64@0:8{?=qiIq}16^f40^f48^{?={?=qiIq}{?=qiIq}}56"
+ "B72@0:8{?=qiIq}16^f40^f48^{?={?=qiIq}{?=qiIq}}56^q64"
+ "BTDetails_AlternateTransport"
+ "Blitting failed"
+ "BluetoothFeatures"
+ "BluetoothLEInput"
+ "C16@0:8"
+ "CMAVRoutingTimeAsValue"
+ "CMAVRoutingTimeMappingAsValue"
+ "CMAVRoutingTimeRangeAsValue"
+ "CMNotificationCenter"
+ "CMTIMERANGE_IS_VALID(timeRange)"
+ "CMTime"
+ "CMTime: %@"
+ "CMTimeMapping"
+ "CMTimeMapping: {%@, %@}"
+ "CMTimeMappingValue"
+ "CMTimeRange"
+ "CMTimeRange: %@"
+ "CMTimeRangeValue"
+ "CMTimeValue"
+ "CMVideoDimensionsValue"
+ "CachedDiscovery"
+ "Can only use kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs for MV-HEVC video"
+ "Cannot append media data after ending session"
+ "Cannot append tagged buffer group due to left and right view IDs mismatch"
+ "Cannot append tagged buffer group due to video layer IDs mismatch"
+ "Cannot append tagged buffer that contains no CVPixelBuffers"
+ "Cannot enter a terminal state until the receiver starts executing"
+ "Cannot look up token %p that was not vended by %@.  Break on AVRoutingCallbackContextRegistryUnrecognizedTokenBreak() to debug."
+ "Cannot regress from a terminal state %d to a non-terminal state %d"
+ "Cannot remove a listener %@ (callback %p) for %@ from object %p that was never added.  Break on AVRoutingCMNotificationDispatcherUnbalancedUnregistrationBreak() to debug."
+ "Cannot unregister token %p that was not vended by %@.  Break on AVRoutingCallbackContextRegistryUnrecognizedTokenBreak() to debug."
+ "CarEntityHasScreenForAirPlayVideo"
+ "CarEntityIsDoingTurnByTurn"
+ "CarEntityIsDoingVoiceRecognition"
+ "CarEntityOwnsMainAudio"
+ "CarEntityOwnsScreen"
+ "ConversationDetect"
+ "ConversationDetectEnable"
+ "CoreAnimation image queue does not support this image type"
+ "CoreAnimation image queue does not support this pixel format"
+ "CoreAnimation image queue is full"
+ "CoreAnimation image queue registration failed"
+ "Custom compositor failed with client NSError"
+ "Destination frame unsupported format"
+ "EndpointInfo"
+ "Error retrieving system remote pool context."
+ "Expected a NSDictionary for didFailToConnectToOutputDeviceUserInfo"
+ "ExtendedFeatures"
+ "Failed to copy predicted selected route descriptor"
+ "Failed to create FigRoutingContext"
+ "Failed to reset predicted selected route descriptor"
+ "FigCommChannelUUID"
+ "FigEndpointUIAgent"
+ "FigRouteDescriptor"
+ "FigRouteDiscoverer"
+ "FigRouteDiscovererCopyProperty / kFigRouteDiscovererProperty_FallbackRouteDescriptor failed"
+ "FigRoutingContext"
+ "FigRoutingContextAdditions"
+ "Frame was cancelled"
+ "FrecencyScore"
+ "Frecents"
+ "GAPA"
+ "HAPConformance"
+ "HIDs"
+ "HighFidelityTouch"
+ "HostApplicationBundleID"
+ "I"
+ "I16@0:8"
+ "ID"
+ "Invalid composition instruction"
+ "Invalid parameter"
+ "IsActivated"
+ "IsAnyLongFormVideoSessionActive"
+ "IsCached"
+ "IsContinuityScreenOutput"
+ "IsGenuineAppleAccessory"
+ "JSON format error"
+ "Knobs"
+ "LastUsedTimestamp"
+ "LimitedUI"
+ "LimitedUIElements"
+ "LineIn"
+ "LowFidelityTouch"
+ "MACAddress"
+ "MFiCertificateSerialNumber"
+ "Media format - format description has an incompatible format (e.g. unknown format / incompatible atom)"
+ "Media format - format description is invalid (e.g. invalid size)"
+ "Media format - invalid parameter"
+ "Media format - sample description is invalid (e.g. invalid size)"
+ "Media format - sample description is unsupported for the specified format flavor"
+ "Media format - slice has an invalid value"
+ "Media writing - invalid edit"
+ "Media writing - invalid format"
+ "Media writing - invalid timestamp"
+ "Media writing - no such property"
+ "Media writing - no such track"
+ "Media writing - predetermined file size too small"
+ "Media writing - predetermined media data size too small"
+ "Media writing - read only property"
+ "Media writing - segment is not allowed to star with a non-sync sample."
+ "MediaExperience"
+ "MicrophoneBluetooth"
+ "MicrophoneWired"
+ "Missing required entitlement com.apple.avfoundation.allow-identifying-output-device-details"
+ "Missing required entitlement com.apple.avfoundation.allows-set-output-device"
+ "My Device"
+ "N"
+ "NO"
+ "NSCoding"
+ "NSCopying"
+ "NSMutableCopying"
+ "NSObject"
+ "NSSecureCoding"
+ "NSValueCMTimeExtensions"
+ "NSValueCMVideoDimensionsExtensions"
+ "NightMode"
+ "Nil"
+ "No custom callbacks"
+ "No endpoint found for route descriptor"
+ "No output callback"
+ "Not available"
+ "Not available.  Use %@ instead"
+ "Not available.  Use %@ instead."
+ "OEMIconLabel"
+ "OEMIconVisible"
+ "OEMIcons"
+ "Output device %@ screen %@"
+ "PreemptivePortConnection"
+ "Q"
+ "Remove endpoint %@ from routing context %@"
+ "Remove route descriptor %@ from routing context %@"
+ "Render dimensions unknown"
+ "RightHandDrive"
+ "RoutingContextCallbacks"
+ "S16@0:8"
+ "ScreenInfo"
+ "Select endpoint %@ on routing context %@"
+ "Select endpoints %@ on routing context %@"
+ "Select route descriptor %@ on routing context %@"
+ "Select route descriptors %@ on routing context %@"
+ "Set configuration on device represented by %@ (impl=%@)"
+ "Set configuration on device represented by (impl=%@)"
+ "SomeLongFormVideoClientIsActiveDidChange"
+ "Source frame missing"
+ "Source frame unsupported format"
+ "SupportsConversationDetect"
+ "SupportsFitnessUIOverlay"
+ "SupportsScreenMirroringControls"
+ "T#,R"
+ "T@\"<AVFigRouteDiscovererFactory>\",R,N,V_routeDiscovererFactory"
+ "T@\"<AVInputDeviceImplSupport>\",W"
+ "T@\"<AVInputDeviceImplSupport>\",W,V_implSupportEventListener"
+ "T@\"<AVOutputContextCommunicationChannelImpl>\",R,N"
+ "T@\"<AVOutputDeviceAuthorizationSessionDelegate>\",W"
+ "T@\"<AVOutputDeviceCommunicationChannelDelegate>\",W"
+ "T@\"<AVOutputDeviceConfigurationRetrieval>\",&,N,V_finalConfiguration"
+ "T@\"<AVOutputDeviceDelegate>\",W"
+ "T@\"<AVOutputDeviceDelegate>\",W,V_delegate"
+ "T@\"<AVOutputDeviceImplSupport>\",W"
+ "T@\"<AVOutputDeviceImplSupport>\",W,V_implSupportEventListener"
+ "T@\"<AVRoutingPlaybackParticipant>\",W,N"
+ "T@\"AVAudioSession\",&,N"
+ "T@\"AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl\",W,V_parentSession"
+ "T@\"AVFigRoutingContextOutputContextImpl\",W"
+ "T@\"AVFigRoutingContextOutputContextImpl\",W,V_parentOutputContextImpl"
+ "T@\"AVInputContext\",W"
+ "T@\"AVInputContext\",W,V_parentContext"
+ "T@\"AVInputContextDestinationChange\",R,N"
+ "T@\"AVInputDevice\",R,N"
+ "T@\"AVInputDeviceDiscoverySession\",W"
+ "T@\"AVInputDeviceDiscoverySession\",W,V_parentSession"
+ "T@\"AVOutputContext\",W"
+ "T@\"AVOutputContext\",W,V_parentContext"
+ "T@\"AVOutputContextCommunicationChannel\",R,N"
+ "T@\"AVOutputContextCommunicationChannel\",W"
+ "T@\"AVOutputContextCommunicationChannel\",W,V_parentChannel"
+ "T@\"AVOutputContextDestinationChange\",R,N"
+ "T@\"AVOutputContextManager\",W"
+ "T@\"AVOutputContextManager\",W,V_parentManager"
+ "T@\"AVOutputDevice\",R"
+ "T@\"AVOutputDevice\",R,N"
+ "T@\"AVOutputDevice\",R,N,V_outputDevice"
+ "T@\"AVOutputDevice\",W"
+ "T@\"AVOutputDevice\",W,V_parentOutputDevice"
+ "T@\"AVOutputDeviceAuthorizationSession\",W"
+ "T@\"AVOutputDeviceAuthorizationSession\",W,V_parentSession"
+ "T@\"AVOutputDeviceCommunicationChannel\",W"
+ "T@\"AVOutputDeviceCommunicationChannel\",W,V_parentChannel"
+ "T@\"AVOutputDeviceDiscoverySession\",W"
+ "T@\"AVOutputDeviceDiscoverySession\",W,V_parentSession"
+ "T@\"AVOutputDeviceDiscoverySessionAvailableOutputDevices\",R,N"
+ "T@\"AVRoutingSession\",R"
+ "T@\"AVRoutingSessionDestination\",R"
+ "T@\"MXRoutingContextModificationMetrics\",R,&,N,V_modificationMetrics"
+ "T@\"NSArray\",R"
+ "T@\"NSArray\",R,&,N,V_devicesType"
+ "T@\"NSArray\",R,C"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSArray\",R,G_additionalFigRepresentationObjects"
+ "T@\"NSArray\",R,G_defaultAdditionalFigRepresentationObjects"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_inputCapabilities"
+ "T@\"NSArray\",R,N,V_limitedUIElements"
+ "T@\"NSArray\",R,N,V_viewAreas"
+ "T@\"NSData\",R,C,N"
+ "T@\"NSData\",R,N"
+ "T@\"NSData\",R,N,V_imageData"
+ "T@\"NSDictionary\",&,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSError\",R"
+ "T@\"NSMutableDictionary\",C,N,G_ramps,S_setRamps:"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSNumber\",R,N,V_maxFPS"
+ "T@\"NSNumber\",R,N,V_statusBarEdge"
+ "T@\"NSNumber\",R,N,V_viewHeightScaleFactor"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSString\",?,R,N,V_modelID"
+ "T@\"NSString\",R"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_ID"
+ "T@\"NSString\",R,N,V_UUID"
+ "T@\"NSString\",R,N,V_client"
+ "T@\"NSString\",R,N,V_deviceID"
+ "T@\"NSString\",R,N,V_deviceName"
+ "T@\"NSString\",R,N,V_primaryInputDevice"
+ "T@\"NSString\",R,N,V_reason"
+ "T@\"NSString\",R,N,V_screenID"
+ "T@\"NSString\",R,N,V_tokenType"
+ "T@\"NSString\",R,N,V_uniqueID"
+ "T@\"NSString\",R,N,ValternateTransportType"
+ "T@\"NSURL\",R,N,V_applicationURL"
+ "T@\"NSURL\",R,N,V_initialApplicationURL"
+ "T@\"NSValue\",R,N,V_physicalSize"
+ "T@\"NSValue\",R,N,V_pixelSize"
+ "T@\"NSValue\",R,N,V_safeArea"
+ "T@\"NSValue\",R,N,V_squarePixelSize"
+ "T@\"NSValue\",R,N,V_viewArea"
+ "T@,R"
+ "T@,R,W"
+ "T@?,R,C,N,V_completionHandler"
+ "T@?,R,N"
+ "TB"
+ "TB,?,R,N"
+ "TB,?,R,N,V_isClusterLeader"
+ "TB,GisMuted"
+ "TB,N"
+ "TB,R"
+ "TB,R,GisCarPlayVideoActive"
+ "TB,R,GisCarPlayVideoAllowed"
+ "TB,R,N"
+ "TB,R,N,GisActivated"
+ "TB,R,N,GisActivatedForContinuityScreen"
+ "TB,R,N,GisAppleAccessory"
+ "TB,R,N,GisCached"
+ "TB,R,N,GisConversationDetectionEnabled"
+ "TB,R,N,GisEligibleToBePredictedOutputDevice"
+ "TB,R,N,GisHeadTrackedSpatialAudioActive"
+ "TB,R,N,GisHighQualityContentCaptureEnabled"
+ "TB,R,N,GisInUseByPairedDevice"
+ "TB,R,N,GisLimitedUI,V_limitedUI"
+ "TB,R,N,GisNightMode,V_nightMode"
+ "TB,R,N,GisNightModeSupported"
+ "TB,R,N,GisPlaying"
+ "TB,R,N,GisPrerendered,V_prerendered"
+ "TB,R,N,V_cornerMasks"
+ "TB,R,N,V_supportsFocusTransfer"
+ "TB,R,N,V_transitionControl"
+ "TI,R,N,V_type"
+ "TQ,R"
+ "TQ,R,N"
+ "T^{OpaqueFigEndpointUIAgent=},R,N"
+ "T^{OpaqueFigRouteDiscoverer=},R"
+ "T^{OpaqueFigRouteDiscoverer=},R,N,V_discoverer"
+ "T^{OpaqueFigRoutingContext=},R,N"
+ "T^{OpaqueFigRoutingContext=},R,N,V_routingContext"
+ "T^{__CFDictionary=},N"
+ "T^{__CFDictionary=},R,N,V_payload"
+ "T^{__CFString=},R,N"
+ "T^{__CFString=},R,N,V_commChannelUUID"
+ "T^{opaqueCMNotificationCenter=},R,N"
+ "Tf,R"
+ "Tf,R,N"
+ "The time of a volume setting must be numeric."
+ "The timeRange of a ramp must not overlap the timeRange of an existing ramp."
+ "The timeRange of a volume ramp must have a numeric start time and a numeric duration."
+ "Ti,N"
+ "Touchpad"
+ "Tq,?,R,N"
+ "Tq,?,R,N,V_deviceSubType"
+ "Tq,?,R,N,V_deviceType"
+ "Tq,N"
+ "Tq,N,V_discoveryMode"
+ "Tq,R"
+ "Tq,R,N"
+ "TransportType"
+ "T{?=ii},R"
+ "T{?={?=qiIq}{?=qiIq}},R"
+ "URLWithString:"
+ "USBInput"
+ "UTF8String"
+ "UseFigRouteDescriptor"
+ "UseFigRoutingContextResilientRemote"
+ "UseRouteConfigUpdatedNotification"
+ "Value at index 0 for kVTCompressionPropertyKey_MVHEVCVideoLayerIDs is not 0"
+ "Value for kVTDecompressionPropertyKey_RequestedMVHEVCVideoLayerIDs does not match content"
+ "Values for kVTCompressionPropertyKey_MVHEVCVideoLayerIDs are invalid"
+ "VehicleInformation"
+ "VoiceActivationType"
+ "Vv16@0:8"
+ "WebKitSecureCoding"
+ "Y"
+ "YES"
+ "[coder allowsKeyedCoding]"
+ "[propertyList isKindOfClass:[NSDictionary class]]"
+ "^?"
+ "^v"
+ "^v24@0:8@16"
+ "^{OpaqueFigEndpoint=}"
+ "^{OpaqueFigEndpoint=}16@0:8"
+ "^{OpaqueFigEndpointRemoteControlSession=}"
+ "^{OpaqueFigEndpointUIAgent=}"
+ "^{OpaqueFigEndpointUIAgent=}16@0:8"
+ "^{OpaqueFigReadWriteLock=}"
+ "^{OpaqueFigReentrantMutex=}"
+ "^{OpaqueFigRouteDiscoverer=}"
+ "^{OpaqueFigRouteDiscoverer=}16@0:8"
+ "^{OpaqueFigRouteDiscoverer=}32@0:8^{__CFAllocator=}16^{__CFDictionary=}24"
+ "^{OpaqueFigRouteDiscoverer=}8@?0"
+ "^{OpaqueFigRoutingContext=}"
+ "^{OpaqueFigRoutingContext=}16@0:8"
+ "^{OpaqueFigRoutingContext=}8@?0"
+ "^{OpaqueFigRoutingSession=}"
+ "^{OpaqueFigRoutingSessionManager=}"
+ "^{OpaqueFigSimpleMutex=}"
+ "^{OpaqueFigVolumeControllerState=}"
+ "^{_NSZone=}16@0:8"
+ "^{__CFDictionary=}"
+ "^{__CFDictionary=}16@0:8"
+ "^{__CFDictionary=}24@0:8@16"
+ "^{__CFNumber=}"
+ "^{__CFString=}"
+ "^{__CFString=}16@0:8"
+ "^{opaqueCMNotificationCenter=}"
+ "^{opaqueCMNotificationCenter=}16@0:8"
+ "_%@"
+ "_Description"
+ "_FailureReason"
+ "_ID"
+ "_RecoverySuggestion"
+ "_UUID"
+ "_actOnRouteChangeNotifications"
+ "_addTrackedParticipant:"
+ "_additionalFigRepresentationObjects"
+ "_agent"
+ "_allTrackedParticipants"
+ "_applicationSupportPath"
+ "_applicationURL"
+ "_audioCurveOfClass:"
+ "_audioVolumeCurve"
+ "_availableGroupsChanged"
+ "_availableOutputDevices"
+ "_availableRoutesChanged"
+ "_balanceMonitoringIsFinishedSemaphore"
+ "_block"
+ "_blockSerializationLock"
+ "_blocks"
+ "_cachedReferencedObjectDescription"
+ "_callback"
+ "_canMuteDidChangeForEndpointWithID:"
+ "_canMuteDidChangeForRoutingContextWithID:"
+ "_canQueryOutputDeviceDescriptionsAndReturnCurrentValue:"
+ "_canSetEndpointVolumeDidChangeForEndpointWithID:"
+ "_canSetMasterVolumeDidChangeForRoutingContextWithID:"
+ "_canUseForRoutingContextDidChangeForRoutingContextWIthID:"
+ "_cancellationReason"
+ "_carPlayTestNotification:"
+ "_client"
+ "_cmNotificationCenter"
+ "_commChannelManager"
+ "_commChannelManagerCreator"
+ "_commChannelUUID"
+ "_communicationChannelsForUUIDs"
+ "_completionHandler"
+ "_condition"
+ "_configuratorBlock"
+ "_contextsForTokens"
+ "_copyAndRemoveObserverForWeakReferenceToListener:callback:name:object:"
+ "_cornerMasks"
+ "_createSelectRouteOptionsForSetInputDeviceOptions:"
+ "_createSelectRouteOptionsForSetOutputDeviceOptions:"
+ "_createUserPreferredRouteModificationDictionary:"
+ "_currentRequest"
+ "_currentRequestImpl"
+ "_currentRouteChanged"
+ "_currentToken"
+ "_defaultAdditionalFigRepresentationObjects"
+ "_destinationChangesForRouteChangeIDs"
+ "_deviceID"
+ "_deviceName"
+ "_deviceSubType"
+ "_deviceTranslator"
+ "_deviceType"
+ "_devicesType"
+ "_didCloseCommChannelWithUUID:forDeviceWithID:"
+ "_didCloseCommunicationChannel"
+ "_didReceiveData:"
+ "_didReceiveData:fromCommChannelUUID:"
+ "_didReceiveData:fromDeviceWithID:fromChannelWithUUID:"
+ "_discoverer"
+ "_discoveryMode"
+ "_dispatchQueue"
+ "_endValue"
+ "_endpoint"
+ "_endpointDescriptorChanged"
+ "_endpointVolumeControlTypeDidChangeForEndpointWithID:"
+ "_error"
+ "_eventCompleted"
+ "_externalPlaybackIsActiveForParticipant:"
+ "_externalPlaybackPriorityForParticipant:"
+ "_externalPlaybackStatusChangedNotificationToken"
+ "_figAudioCurves"
+ "_figEndpoint"
+ "_figEndpointPropertyValueForKey:"
+ "_figEndpoints"
+ "_finalConfiguration"
+ "_finished"
+ "_finishedWithPrompt"
+ "_frecents"
+ "_frecentsContainerPath"
+ "_frecentsFilePath"
+ "_frecentsReaderAfterMigrationIfNecessary"
+ "_frecentsWriter"
+ "_fundamentalOperation"
+ "_getFigEndpointTypeFromAVOutputDeviceType:"
+ "_getRampOfClass:forTime:timeRange:"
+ "_groupConfigurationChanged"
+ "_handleFigEndpointEvent:payload:"
+ "_handleRouteDescriptionEvent:payload:"
+ "_iOSUIRequestedNotification:"
+ "_imageData"
+ "_impl"
+ "_implSupportEventListener"
+ "_initWithWebKitPropertyListData:"
+ "_initialApplicationURL"
+ "_initializeIfNeededAndGetSystemRemotePool"
+ "_inputCapabilities"
+ "_inputContext"
+ "_inputDevice"
+ "_inputDeviceDiscoverySession"
+ "_inputMode"
+ "_inputRoutePicked"
+ "_interpolatedValueAtTime:"
+ "_isClusterLeader"
+ "_isScheduledRampClass:"
+ "_ivarAccessLock"
+ "_ivarAccessQueue"
+ "_ivars"
+ "_keysToRemove"
+ "_limitedUI"
+ "_limitedUIElements"
+ "_listenerObjectsQueue"
+ "_loadOutputDevices"
+ "_lock"
+ "_makeRampWithTruncatedTimeRange:endValue:"
+ "_masterVolumeControlTypeDidChangeForRoutingContextWithID:"
+ "_masterVolumeDidChangeForRoutingContextWithID:"
+ "_maxFPS"
+ "_migrateFrecentsFromCFPreferencesToFrecentsFilePath:"
+ "_modelID"
+ "_modificationMetrics"
+ "_monitoredObject"
+ "_monitoringIsFinishedSemaphore"
+ "_mutableScheduledParametersInternal"
+ "_muteDidChangeForRoutingContextWithID:"
+ "_mutedDidChangeForEndpointWithID:"
+ "_name"
+ "_nightMode"
+ "_nonMixablePriorityForParticipant:"
+ "_notificationManagementQueue"
+ "_notificationNames"
+ "_notifyCurrentRequestOfTerminalStatus:error:"
+ "_object"
+ "_observersForListenerKeys"
+ "_operationQueue"
+ "_operationStateSerializationQueue"
+ "_otherDevices"
+ "_outgoingCommChannelUUID"
+ "_outputContext"
+ "_outputDevice"
+ "_outputDeviceDiscoverySession"
+ "_parameterRampMode"
+ "_parentChannel"
+ "_parentContext"
+ "_parentInputContext"
+ "_parentManager"
+ "_parentOutputContextImpl"
+ "_parentOutputDevice"
+ "_parentSession"
+ "_payload"
+ "_physicalSize"
+ "_pixelSize"
+ "_predictedSelectedRouteDescriptorChanged"
+ "_prerendered"
+ "_primaryInputDevice"
+ "_rampMode"
+ "_ramps"
+ "_rampsOfClass:"
+ "_readWriteQueue"
+ "_recentlyUsedDevices"
+ "_registerForObjectNotifications"
+ "_registeredForObjectNotifications"
+ "_remoteControlChannelAvailabilityChanged"
+ "_remoteControlSession"
+ "_removeTrackedParticipant:"
+ "_response"
+ "_result"
+ "_resultInput"
+ "_routeChangeBlock"
+ "_routeChangeComplete"
+ "_routeChangeEndedWithID:reason:"
+ "_routeChangeID"
+ "_routeChangeIvarAccessQueue"
+ "_routeChangeStartedWithID:"
+ "_routeChangeWithID:endedWithReason:"
+ "_routeConfigUpdateEndedWithID:reason:"
+ "_routeConfigUpdateStartedWithID:"
+ "_routeConfigUpdateWithID:endedWithReason:"
+ "_routeConfigUpdatedWithID:reason:initiator:endedError:deviceID:previousDeviceIDs:"
+ "_routeDescriptionDidChange:"
+ "_routeDescriptionRWLock"
+ "_routeDescriptor"
+ "_routeDescriptors"
+ "_routeDiscoverer"
+ "_routeDiscovererCreator"
+ "_routeDiscovererFactory"
+ "_routePresentChanged"
+ "_routingContext"
+ "_routingContextCreator"
+ "_routingContextFactory"
+ "_safeArea"
+ "_scheduledParametersInternal"
+ "_screenID"
+ "_sendCommand:completionHandler:"
+ "_serverConnectionDied"
+ "_serverDied"
+ "_setDefaultExternalPlaybackPriorityForParticipant:"
+ "_setDefaultNonMixableAudioPriorityForParticipant:"
+ "_setExternalPlaybackPriority:forParticipant:"
+ "_setNonMixableAudioPriority:forParticipant:"
+ "_setRamp:"
+ "_setRamps:"
+ "_setResultIfNotAlreadySet:"
+ "_setResultInputIfNotAlreadySet:"
+ "_setStatus:"
+ "_setStatus:cancellationReason:"
+ "_setStatus:error:resultingStatus:failureReason:"
+ "_setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:"
+ "_setWeakRefToPreferredParticipantForExternalPlayback:"
+ "_setWeakRefToPreferredParticipantForNonMixableAudio:"
+ "_shouldHideAirPlayInfoDuringDemo"
+ "_showAuthPromptWithUniqueID:routeDescriptor:pinMode:reason:"
+ "_showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:"
+ "_signalMonitoringIsFinishedIfNeeded"
+ "_siriRequestedNotification:"
+ "_squarePixelSize"
+ "_startNewRequest:impl:"
+ "_startValue"
+ "_started"
+ "_status"
+ "_statusBarEdge"
+ "_successNotification"
+ "_supportsFocusTransfer"
+ "_systemPickerVideoRouteChanged"
+ "_testFlag"
+ "_time"
+ "_timeMapping"
+ "_timeRange"
+ "_tokenType"
+ "_transitionControl"
+ "_unhandledRemoteCommandNotification:"
+ "_uniqueID"
+ "_unregisterForObjectNotifications"
+ "_updateExternalPlaybackStatusNotificationListenerToParticipant:"
+ "_updatePreferredParticipantForExternalPlaybackFrom:toParticipant:checkingAllParticipants:"
+ "_updatePreferredParticipantForNonMixableAudioRouteFrom:toParticipant:checkingAllParticipants:"
+ "_updatedFrecentsList"
+ "_useRouteConfigUpdatedNotification"
+ "_useRoutingContextCallbacks"
+ "_usesRouteConfigUpdatedNotification"
+ "_vehicleInformationDidChange:"
+ "_viewArea"
+ "_viewAreas"
+ "_viewHeightScaleFactor"
+ "_volumeController"
+ "_volumeCurveAsString"
+ "_volumeCurveKeysForScheduledRampClassNames"
+ "_volumeDidChangeForEndpointWithID:"
+ "_volumeForEndpointDidChange:forRoomID:"
+ "_waitUntilFinishedIfNeeded"
+ "_weakContextLock"
+ "_weakContexts"
+ "_weakObserver"
+ "_weakReferenceToListener"
+ "_weakReferenceToMonitoredObject"
+ "_weakReferenceToMonitoringObject"
+ "_weakReferenceToPreferredParticipantForExternalPlayback"
+ "_weakReferenceToPreferredParticipantForNonMixableAudio"
+ "_weakReferenceToSelf"
+ "_weakStorage"
+ "_webKitPropertyListData"
+ "_web_errorWithDomain:code:URL:"
+ "_withEndpoint:"
+ "activated"
+ "activatedDeviceClusterMembersDidChangeVolume:forRoomID:"
+ "activatedForContinuityScreen"
+ "addDependency:"
+ "addEntriesFromDictionary:"
+ "addListenerWithWeakReference:callback:name:object:flags:"
+ "addObjectsFromArray:"
+ "addObserverForName:object:queue:usingBlock:"
+ "addOperation:"
+ "addOperations:waitUntilFinished:"
+ "addOutputDevice:"
+ "addOutputDevice:options:completionHandler:"
+ "addOutputDevice:withOptions:completionHandler:"
+ "addOutputDevice:withOptions:toRoutingContext:completionHandler:"
+ "addPeerToHomeGroup:"
+ "addPointer:"
+ "addSharedAudioOutputContext"
+ "addSharedAudioOutputContextImpl"
+ "additionalFigRepresentationObjects"
+ "adjacentViewAreas"
+ "airPlayProperties"
+ "airplayvideo:"
+ "allDevices"
+ "allKeys"
+ "allLikelyDestinations"
+ "allObjects"
+ "allSharedAudioOutputContextImpls"
+ "allSharedAudioOutputContexts"
+ "allocWithZone:"
+ "allowsHeadTrackedSpatialAudio"
+ "allowsKeyedCoding"
+ "alternateTransportType"
+ "ambienceLevelRampWithStartValue:endValue:timeRange:"
+ "ambienceLoudnessRampWithStartValue:endValue:timeRange:"
+ "appendFormat:"
+ "appendString:"
+ "appleAccessory"
+ "applicationPID"
+ "applicationPIDWasSet"
+ "applicationProcessID"
+ "applicationURL"
+ "arrayByApplyingDifference:"
+ "arrayWithCapacity:"
+ "arrayWithObject:"
+ "arrayWithObjects:count:"
+ "associatedAudioDeviceID"
+ "at"
+ "attachDepartureAnnouncingObjectMonitorToObject:monitoringObject:"
+ "audioSessionID"
+ "audioSessionId"
+ "authenticationType"
+ "authorizationTokenType"
+ "automaticallyAllowsConnectionsFromPeersInHomeGroup"
+ "autorelease"
+ "auxiliaryOutputContext"
+ "availableBluetoothListeningModes"
+ "availableInputDevices"
+ "availableOutputDevices"
+ "availableOutputDevicesObject"
+ "avblockserializer_trace"
+ "batteryLevel"
+ "block != nil"
+ "boolValue"
+ "borrowScreenForClient:reason:"
+ "boundsAdjustedFloatValue:"
+ "bundleWithIdentifier:"
+ "c16@0:8"
+ "cached"
+ "cachedDiscoveryEnabled"
+ "callbackContext != nil"
+ "callbackContextForToken:"
+ "callbackContextToken != AVCallbackContextTokenInvalid"
+ "can't interpolate outside of the timeRange of the receiver"
+ "canAccessAppleMusic"
+ "canAccessRemoteAssets"
+ "canAccessiCloudMusicLibrary"
+ "canBeGroupLeader"
+ "canBeGrouped"
+ "canCommunicateWithAllLogicalDeviceMembers"
+ "canFetchMediaDataFromSender"
+ "canMute"
+ "canPlayEncryptedProgressiveDownloadAssets"
+ "canRelayCommunicationChannel"
+ "canSetVolume"
+ "cancel"
+ "cancellationReason"
+ "carOwnsMainAudio"
+ "carOwnsScreen"
+ "carPlayVideoActive"
+ "carPlayVideoAllowed"
+ "caseBatteryLevel"
+ "ccr_trace"
+ "changeToTerminalStatusBasedOnInputRouteChangeEndedReason:"
+ "changeToTerminalStatusBasedOnInputRouteConfigUpdatedReason:"
+ "changeToTerminalStatusBasedOnRouteChangeEndedReason:"
+ "changeToTerminalStatusBasedOnRouteConfigUpdatedReason:"
+ "charValue"
+ "class"
+ "classForCoder"
+ "clearUserPreferredInputDevice:error:"
+ "client"
+ "close"
+ "clusterID"
+ "clusterType"
+ "clusteredDeviceDescriptions"
+ "cmNotificationCenter != NULL"
+ "code"
+ "com.apple.AVFCore"
+ "com.apple.UIKit.screenpicker"
+ "com.apple.avfoundation"
+ "com.apple.avfoundation.AVRoutingCMNotificationDispatcher.ivars"
+ "com.apple.avfoundation.AVRoutingOperation.ivars"
+ "com.apple.avfoundation.allow-system-wide-context"
+ "com.apple.avfoundation.avidds.ivars"
+ "com.apple.avfoundation.avodds.ivars"
+ "com.apple.avfoundation.avoutputcontext.uiagentqueue"
+ "com.apple.avfoundation.avoutputdevice.routediscovererqueue"
+ "com.apple.avfoundation.communication-channel-manager"
+ "com.apple.avfoundation.device-comm-channel-manager"
+ "com.apple.avfoundation.frecents"
+ "com.apple.avfoundation.globaloperationqueue.%p"
+ "com.apple.avfoundation.inputcontext.destinationchange"
+ "com.apple.avfoundation.inputcontext.figroutingcontext"
+ "com.apple.avfoundation.inputcontext.ivars"
+ "com.apple.avfoundation.output-device-auth-session.ivars"
+ "com.apple.avfoundation.outputcontext.destinationchange"
+ "com.apple.avfoundation.outputcontext.figroutingcontext"
+ "com.apple.avfoundation.outputcontext.ivars"
+ "com.apple.avfoundation.outputcontextmanager.ivars"
+ "com.apple.avfoundation.outputdeviceauthorizationsession.ivars"
+ "com.apple.avfoundation.route-change-operation.ivars"
+ "com.apple.avfoundation.waitForNotificationOrDeallocationOperation"
+ "com.apple.avrouting.routingplaybackarbiterdispatch"
+ "com.apple.avrouting.routingplaybackarbiterivars"
+ "com.apple.coremedia"
+ "commChannelManager"
+ "commChannelUUID"
+ "commChannelUUIDCommunicationChannelManagerCreator"
+ "communicationChannel:didReceiveData:"
+ "communicationChannelDelegate"
+ "communicationChannelDidClose:"
+ "communicationChannelImpl:didReceiveData:"
+ "communicationChannelImplDidClose:"
+ "communicationChannelManager:didCloseCommunicationChannel:"
+ "communicationChannelManager:didReceiveData:fromCommunicationChannel:"
+ "completionBlock"
+ "completionHandler"
+ "componentsJoinedByString:"
+ "configUpdateReasonEndpointDescriptorChanged_RouteDescriptor"
+ "configUpdateReasonEndpointDescriptorChanged_RouteNotification"
+ "configUpdateReasonEndpointDescriptorChanged_RoutePayload"
+ "configureUsingBlock:completionHandler:"
+ "configureUsingBlock:options:completionHandler:"
+ "configuredClusterSize"
+ "conformsToProtocol:"
+ "connectedPairedDevices"
+ "contextID"
+ "contextType"
+ "conversationDetectionEnabled"
+ "copy"
+ "copyAllAudioContexts:"
+ "copyContextForUUIDWithAllocator:options:context:"
+ "copyDefaultContextWithAllocator:options:context:"
+ "copyDisplayMenuVideoContextWithAllocator:options:context:"
+ "copySharedEndpointUIAgent"
+ "copySystemAudioContextWithAllocator:options:context:"
+ "copySystemAudioInputContextWithAllocator:options:context:"
+ "copySystemMirroringContextWithAllocator:options:context:"
+ "copySystemMusicContextWithAllocator:options:context:"
+ "copySystemRemoteDisplayContextWithAllocator:options:context:"
+ "copySystemRemotePoolContextWithAllocator:options:context:"
+ "copySystemVideoRoutingContext"
+ "copyWithZone:"
+ "cornerMasks"
+ "createAudioContextWithAllocator:options:context:"
+ "createControlChannelOnlyContextWithAllocator:options:context:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createPerAppSecondDisplayContextWithAllocator:options:context:"
+ "createRemoteMusicControllerContextWithAllocator:options:context:"
+ "createRouteDiscovererWithAllocator:options:"
+ "createVideoContextWithAllocator:options:context:"
+ "currentBluetoothListeningMode"
+ "currentPlatformIdentifier"
+ "currentRoutingSession"
+ "currentScreenViewAreaForScreenID:"
+ "d16@0:8"
+ "d24@0:8@16"
+ "data"
+ "dataWithContentsOfFile:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "date"
+ "debugDescription"
+ "decodeCMTimeForKey:"
+ "decodeCMTimeMappingForKey:"
+ "decodeCMTimeRangeForKey:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "decreaseVolumeByCount:"
+ "defaultAdditionalFigRepresentationObjects"
+ "defaultAudioToLocal"
+ "defaultCommunicationChannelManagerCreator"
+ "defaultFloatValue"
+ "defaultFrecentsReader"
+ "defaultFrecentsWriter"
+ "defaultInputContextImplClass"
+ "defaultManager"
+ "defaultOutputContextImplClass"
+ "defaultQueue"
+ "defaultSharedOutputContext"
+ "defaultSharedOutputContextImpl"
+ "defaultValue"
+ "dependencies"
+ "deregisterParticipant:"
+ "destination"
+ "deviceFeatures"
+ "deviceID"
+ "deviceIDs"
+ "deviceName"
+ "devicePassword"
+ "devicePresenceDetected"
+ "devicePublicKey"
+ "deviceSubType"
+ "deviceType"
+ "devicesType"
+ "dialogLevelRampWithStartValue:endValue:timeRange:"
+ "dialogLoudnessRampWithStartValue:endValue:timeRange:"
+ "dialogMixBiasRampWithStartValue:endValue:timeRange:"
+ "dictionary"
+ "dictionaryWithCapacity:"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObject:forKey:"
+ "dictionaryWithObjects:forKeys:count:"
+ "dictionaryWithObjectsAndKeys:"
+ "didChangeValueForKey:"
+ "didCloseCommChannelUUID:"
+ "didEnterTerminalState"
+ "disable"
+ "discoveryMode"
+ "displayCornerMasks"
+ "domain"
+ "doubleValue"
+ "echoedDictionary"
+ "electronicTollCollection"
+ "eligibleToBePredictedOutputDevice"
+ "enable"
+ "encodeCMTime:forKey:"
+ "encodeCMTimeMapping:forKey:"
+ "encodeCMTimeRange:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "endFloatValue"
+ "endValue"
+ "endVolume"
+ "enhancedRequestCarUI"
+ "enqueueOperation:"
+ "enterTerminalStatus:error:"
+ "err"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "establishedAutomaticallyFromLikelyDestination"
+ "evaluateDependenciesAndMarkAsExecuting"
+ "exceptionWithName:reason:userInfo:"
+ "externalPlaybackIsActive"
+ "externalPlaybackPriority"
+ "f"
+ "f16@0:8"
+ "f20@0:8f16"
+ "f24@0:8@\"NSString\"16"
+ "f24@0:8@16"
+ "f40@0:8{?=qiIq}16"
+ "fallbackInputDevice"
+ "fallbackRouteDescriptor"
+ "figDestination"
+ "figEndpoint"
+ "figEndpoint != NULL"
+ "figEndpointOutputDeviceImpl"
+ "figEndpointUIAgent"
+ "figRoutingContext"
+ "figRoutingSession"
+ "figRoutingSessionManager"
+ "finalConfiguration"
+ "firmwareVersion"
+ "firstObject"
+ "floatValue"
+ "frecencyInfoForDeviceWithID:"
+ "frecencyScore"
+ "frecencyScoreForDeviceID:"
+ "getApplicationProcessID:"
+ "getMaximumVolumeLimitForBuiltInSpeaker:"
+ "getValue:"
+ "getVolumeRampForTime:startVolume:endVolume:timeRange:"
+ "getVolumeRampForTime:startVolume:endVolume:timeRange:rampMode:"
+ "groupContainsGroupLeader"
+ "groupID"
+ "groupID != nil"
+ "groupLeader"
+ "hapticFeedbackType"
+ "hasAdministratorPrivileges"
+ "hasBatteryLevel"
+ "headTrackedSpatialAudioActive"
+ "headTrackedSpatialAudioMode"
+ "heightPixels"
+ "hideAirPlayRoutingInfoDuringDemo"
+ "highQualityContentCaptureEnabled"
+ "i"
+ "i16@0:8"
+ "i16@?0^{OpaqueFigEndpoint=}8"
+ "i20@0:8f16"
+ "i24@0:8@?16"
+ "i24@0:8^f16"
+ "i8@?0"
+ "iTT requires languageCode or extendedLanguageTag property to be set"
+ "iTunesAudioContext"
+ "identifyingMACAddress"
+ "imageData"
+ "impl"
+ "implEventListener"
+ "inUseByPairedDevice"
+ "increaseVolumeByCount:"
+ "indexOfObjectPassingTest:"
+ "indexSet"
+ "indexSetWithIndex:"
+ "initForUsingRouteConfigUpdatedNotification:"
+ "initWithAvailableFigEndpoints:"
+ "initWithBlock:"
+ "initWithCMNotificationCenter:"
+ "initWithCapacity:"
+ "initWithCoder:"
+ "initWithCompletionHandler:"
+ "initWithCompletionHandler:outputDevices:figRoutingContext:"
+ "initWithDeviceFeatures:"
+ "initWithDeviceID:"
+ "initWithDeviceID:channelUUID:outputContext:"
+ "initWithDeviceID:deviceName:deviceSubType:isClusterLeader:modelID:"
+ "initWithDict:"
+ "initWithEndpoint:"
+ "initWithEndpoint:client:reason:"
+ "initWithEndpointUIAgent:"
+ "initWithFigEndpoint:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:"
+ "initWithFigEndpointUIAgent:"
+ "initWithFigRouteConfigUpdatedReason:metrics:"
+ "initWithFigRouteDiscovererCreator:"
+ "initWithFigRoutingContext:routingContextReplacementBlock:"
+ "initWithFigRoutingContext:routingContextReplacementBlock:outputDeviceTranslator:volumeController:communicationChannelManagerCreator:"
+ "initWithFigRoutingContextCreator:"
+ "initWithFigRoutingSession:"
+ "initWithFigRoutingSessionDestination:"
+ "initWithFigRoutingSessionManager:"
+ "initWithFormat:"
+ "initWithFormat:arguments:"
+ "initWithFrecentsFilePath:"
+ "initWithFrecentsFilePath:error:"
+ "initWithFundamentalOperation:"
+ "initWithID:outputDevice:authorizationTokenType:"
+ "initWithID:publicKey:hasAdministratorPrivileges:"
+ "initWithInputContextImpl:"
+ "initWithInputDeviceDiscoverySessionImpl:"
+ "initWithInputDeviceImpl:"
+ "initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "initWithMonitoringObject:"
+ "initWithName:ID:modelID:playing:productName:"
+ "initWithObject:notificationNames:"
+ "initWithObjects:"
+ "initWithObjectsAndKeys:"
+ "initWithOutputContextCommunicationChannelImpl:"
+ "initWithOutputContextImpl:"
+ "initWithOutputContextManagerImpl:"
+ "initWithOutputDeviceAuthorizationRequestImpl:"
+ "initWithOutputDeviceAuthorizationSessionImpl:"
+ "initWithOutputDeviceCommunicationChannelImpl:"
+ "initWithOutputDeviceDiscoverySessionAvailableOutputDevicesImpl:"
+ "initWithOutputDeviceDiscoverySessionImpl:"
+ "initWithOutputDeviceGroupImpl:"
+ "initWithOutputDeviceImpl:commChannelManager:"
+ "initWithPropertyList:"
+ "initWithReferencedObject:"
+ "initWithRemoteControlSession:"
+ "initWithRouteDescriptor:routeDiscoverer:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:"
+ "initWithRouteDescriptor:routeDiscoverer:volumeController:routingContextFactory:useRouteConfigUpdatedNotification:routingContext:"
+ "initWithRouteDescriptors:routeDiscoverer:"
+ "initWithRouteDiscovererFactory:"
+ "initWithRoutingContext:"
+ "initWithRoutingContext:commChannelUUID:"
+ "initWithRoutingContext:configuratorBlock:"
+ "initWithRoutingContext:routeChangeID:routeChangeBlock:isInputContextOperation:"
+ "initWithRoutingContext:successNotification:routeChangeBlock:isInputContextOperation:"
+ "initWithRoutingContextComandResponse:"
+ "initWithRoutingContextUUID:type:"
+ "initWithStartValue:endValue:timeRange:"
+ "initWithStartVolume:endVolume:timeRange:rampMode:"
+ "initWithStatus:cancellationReason:"
+ "initWithTimeRange:"
+ "initWithType:"
+ "initWithUUID:screenUUID:endpoint:"
+ "initWithUUIDString:"
+ "initWithViewArea:transitionControl:supportsFocusTransfer:statusBarEdge:safeArea:"
+ "initWithWeakReferenceToListener:callback:name:object:"
+ "initialApplicationURL"
+ "initialize"
+ "inputCapabilities"
+ "inputContextDidChangeApplicationProcessID:"
+ "inputContextForID:"
+ "inputContextImpl:didChangeInputDeviceWithInitiator:"
+ "inputContextImpl:didExpireWithReplacement:"
+ "inputContextImpl:didInitiateDestinationChange:"
+ "inputContextImplForID:type:"
+ "inputContextType"
+ "inputDevice"
+ "inputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:"
+ "inputDeviceDiscoverySessionImpl:didExpireWithReplacement:"
+ "inputDeviceDiscoverySessionImplDidChangeAvailableInputDevices:"
+ "inputDeviceFeatures"
+ "inputDeviceInfo"
+ "inputDeviceWithRouteDescriptor:routeDiscoverer:"
+ "inputDeviceWithRouteDescriptor:withRoutingContext:"
+ "inputMode"
+ "inputcontext_trace"
+ "inputdevice_trace"
+ "inputdevicediscoverysession_trace"
+ "insertObject:atIndex:"
+ "intValue"
+ "integerValue"
+ "invalid parameter not satisfying: %s"
+ "isActivated"
+ "isActivatedForContinuityScreen"
+ "isAdmin"
+ "isAppleAccessory"
+ "isAsynchronous"
+ "isCached"
+ "isCancelled"
+ "isCarPlayVideoActive"
+ "isCarPlayVideoAllowed"
+ "isClusterLeader"
+ "isConversationDetectionEnabled"
+ "isEligibleToBePredictedOutputDevice"
+ "isEqualToData:"
+ "isEqualToValue:"
+ "isExecuting"
+ "isFinished"
+ "isGroupLeader"
+ "isHeadTrackedSpatialAudioActive"
+ "isHighQualityContentCaptureEnabled"
+ "isInEar"
+ "isInUseByPairedDevice"
+ "isKindOfClass:"
+ "isLimitedUI"
+ "isLogicalDeviceLeader"
+ "isMemberOfClass:"
+ "isMuted"
+ "isNightMode"
+ "isNightModeSupported"
+ "isPlaying"
+ "isPrerendered"
+ "isProxy"
+ "isReady"
+ "ivarAccessQueue"
+ "japanMaps"
+ "kFigRouteDiscovererError_InvalidParameter"
+ "lastObject"
+ "leftBatteryLevel"
+ "length"
+ "likelyExternalDestinations"
+ "limitedUI"
+ "limitedUIElements"
+ "listenerKeyWithWeakReferenceToListener:callback:name:object:"
+ "localDeviceDidChange"
+ "localizedDescription"
+ "localizedName"
+ "localizedStandardCompare:"
+ "localizedStringForKey:value:table:"
+ "lock"
+ "logicalDeviceID"
+ "longFormVideoManagerCanHaveCurrentSessionWithDestinationOfType:subType:"
+ "longFormVideoRoutingSessionManager"
+ "longLongValue"
+ "longValue"
+ "mCancellationReason"
+ "mFigRoutingContext"
+ "mStatus"
+ "main"
+ "manufacturer"
+ "markAsCancelled"
+ "markAsCancelledWithReason:"
+ "markAsCompleted"
+ "markAsFailed"
+ "markAsFailedWithError:"
+ "markAsFinished"
+ "markAsInProgress"
+ "markEventAsCompleted"
+ "maxFPS"
+ "mediaSessionStatus"
+ "modelID"
+ "modelSpecificInformation"
+ "modificationMetrics"
+ "monitoredObjectHasDeparted"
+ "musicLists"
+ "mutableCopy"
+ "mutableCopyWithZone:"
+ "muted"
+ "navigationAidedDriving"
+ "nightMode"
+ "nightModeSupported"
+ "nil"
+ "non-"
+ "non-nil"
+ "nonMixableAudioPriority"
+ "nonMusicLists"
+ "notificationDispatcherForCMNotificationCenter:"
+ "notificationTimestamp"
+ "notificationWithName:object:userInfo:"
+ "numberOfKeysToBeSet"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithFloat:"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "objCType"
+ "object"
+ "objectAtIndex:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "onlyAllowsConnectionsFromPeersInHomeGroup"
+ "onlyDiscoversBluetoothDevices"
+ "opaqueSessionID"
+ "openCommunicationChannelToDestination:options:completionHandler:"
+ "openCommunicationChannelWithOptions:completionHandler:"
+ "openCommunicationChannelWithOptions:error:"
+ "operations"
+ "otherDevices"
+ "outgoingCommunicationChannel"
+ "outputContext"
+ "outputContext:didCloseCommunicationChannel:"
+ "outputContext:didReceiveData:fromCommunicationChannel:"
+ "outputContextDidChangeApplicationProcessID:"
+ "outputContextExistsWithRemoteOutputDevice"
+ "outputContextForContextID:"
+ "outputContextForControllingOutputDeviceGroupWithID:"
+ "outputContextForControllingOutputDeviceGroupWithID:options:"
+ "outputContextForID:"
+ "outputContextImpl:didChangeOutputDeviceWithInitiator:"
+ "outputContextImpl:didChangeOutputDevicesWithInitiator:reason:deviceID:previousDeviceIDs:"
+ "outputContextImpl:didCloseCommunicationChannel:"
+ "outputContextImpl:didExpireWithReplacement:"
+ "outputContextImpl:didInitiateDestinationChange:"
+ "outputContextImpl:didReceiveData:fromCommunicationChannel:"
+ "outputContextImplDidChangeCanMute:"
+ "outputContextImplDidChangeCanSetVolume:"
+ "outputContextImplDidChangeGlobalOutputDeviceConfiguration:"
+ "outputContextImplDidChangeMute:"
+ "outputContextImplDidChangePredictedOutputDevice:"
+ "outputContextImplDidChangeProvidesControlForAllVolumeFeatures:"
+ "outputContextImplDidChangeVolume:"
+ "outputContextImplDidChangeVolumeControlType:"
+ "outputContextImplForControllingOutputDeviceGroupWithID:options:"
+ "outputContextImplForID:type:"
+ "outputContextImplOutgoingCommunicationChannelDidBecomeAvailable:"
+ "outputContextManagerForAllOutputContexts"
+ "outputContextManagerImpl:observedFailureToConnectToOutputDevice:reason:didFailToConnectToOutputDeviceDictionary:"
+ "outputContextManagerImplDidExpireWithReplacementImpl:"
+ "outputContextOutgoingCommunicationChannelDidBecomeAvailable:"
+ "outputContextType"
+ "outputContextWithFigRoutingContextCreator:"
+ "outputContextWithFigRoutingContextCreator:communicationChannelManagerCreator:"
+ "outputContextWithFigRoutingContextCreator:outputDeviceTranslator:"
+ "outputContextWithFigRoutingContextCreator:volumeController:"
+ "outputDevice"
+ "outputDevice:didCloseCommunicationChannel:"
+ "outputDevice:didReceiveData:fromCommunicationChannel:"
+ "outputDeviceAuthorizationRequestImpl:didRespondWithAuthorizationToken:"
+ "outputDeviceAuthorizationRequestImplDidCancel:"
+ "outputDeviceAuthorizationSession:didProvideAuthorizationRequest:"
+ "outputDeviceAuthorizationSession:shouldRetryAuthorizationRequest:reason:"
+ "outputDeviceAuthorizationSessionImpl:didProvideAuthorizationRequest:"
+ "outputDeviceAuthorizationSessionImpl:shouldRetryAuthorizationRequest:reason:"
+ "outputDeviceAuthorizationSessionImplDidExpireWithReplacementImpl:"
+ "outputDeviceAuthorizationSessionWithEndpointUIAgent:"
+ "outputDeviceDescriptions"
+ "outputDeviceDiscoverySessionAvailableOutputDevicesWithAvailableFigEndpoints:"
+ "outputDeviceDiscoverySessionBluetoothOnlyDiscoveryDidChange:"
+ "outputDeviceDiscoverySessionCachedDiscoveryDidChange:"
+ "outputDeviceDiscoverySessionDidChangeDiscoveryMode:forClientIdentifiers:"
+ "outputDeviceDiscoverySessionFactory"
+ "outputDeviceDiscoverySessionImpl:didExpireWithReplacement:"
+ "outputDeviceDiscoverySessionImplDidChangeAvailableOutputDeviceGroups:"
+ "outputDeviceDiscoverySessionImplDidChangeAvailableOutputDevices:"
+ "outputDeviceDiscoverySessionOfClass:withDeviceFeatures:"
+ "outputDeviceFeatures"
+ "outputDeviceFromRoutingContext:"
+ "outputDeviceGroupImpl:didChangeOutputDevicesWithInitiator:"
+ "outputDeviceGroupImplDidChangeVolume:"
+ "outputDeviceGroupImplDidChangeVolumeControlType:"
+ "outputDeviceHIDs"
+ "outputDeviceImplCanMuteDidChange:"
+ "outputDeviceImplDidChangeCanChangeVolume:"
+ "outputDeviceImplDidChangeMute:"
+ "outputDeviceImplDidChangeProposedGroupID:"
+ "outputDeviceImplDidChangeVolume:"
+ "outputDeviceImplDidChangeVolumeControlType:"
+ "outputDeviceInfo"
+ "outputDeviceWithFigEndpoint:"
+ "outputDeviceWithFigEndpoint:routingContextFactory:"
+ "outputDeviceWithFigEndpoint:volumeController:"
+ "outputDeviceWithRouteDescriptor:"
+ "outputDeviceWithRouteDescriptor:routeDiscoverer:"
+ "outputDeviceWithRouteDescriptor:routingContextFactory:"
+ "outputDeviceWithRouteDescriptor:volumeController:"
+ "outputDeviceWithRouteDescriptor:withRoutingContext:"
+ "outputDevices"
+ "outputDevicesFromRoutingContext:"
+ "outputcontext_trace"
+ "outputdevice_trace"
+ "outputdeviceauthorizationsession_trace"
+ "outputdevicediscoverysession_trace"
+ "outputdevicegroup_trace"
+ "ownsTurnByTurnNavigation"
+ "pairedDeviceID"
+ "pairedDevicesConnectedToOutputDevice:"
+ "parameterRamps"
+ "parentAuthorizationSession"
+ "parentAuthorizationSessionImpl"
+ "parentChannel"
+ "parentCommunicationChannel"
+ "parentInputContext"
+ "parentInputDeviceDiscoverySession"
+ "parentOutputContext"
+ "parentOutputContextImpl"
+ "parentOutputContextManager"
+ "parentOutputDevice"
+ "parentOutputDeviceDiscoverySession"
+ "participatesInGroupPlayback"
+ "peerID"
+ "peersInHomeGroup"
+ "performHapticFeedback"
+ "performHapticFeedbackForUUID:withHapticType:completionHandler:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "persistToDiskReturningError:"
+ "physicalSize"
+ "pixelSize"
+ "platformDependentScreenOrVideoContext"
+ "platformIdentifier"
+ "platformutilities_trace"
+ "playing"
+ "pointerAtIndex:"
+ "postNotification:"
+ "postNotification:fromImpl:"
+ "postNotification:withPayload:fromImpl:"
+ "postNotificationName:object:userInfo:"
+ "predictedOutputDevice"
+ "predictedOutputDeviceFromRoutingContext:"
+ "preferredOutputDevicesForAudioSession:"
+ "preferredParticipantForExternalPlayback"
+ "preferredParticipantForNonMixableAudioRoutes"
+ "prefersLikelyDestinationsOverCurrentRoutingSession"
+ "prefersRouteDescriptors"
+ "prerendered"
+ "presentsOptimizedUserInterfaceWhenPlayingFetchedAudioOnlyAssets"
+ "primaryInputDevice"
+ "probability"
+ "processInfo"
+ "processName"
+ "producesLowFidelityAudio"
+ "productName"
+ "propertyList"
+ "propertyListWithData:options:format:error:"
+ "proposedGroupID"
+ "providesControlForAllVolumeFeatures"
+ "providesExternalVideoPlayback"
+ "publicKey"
+ "q24@?0@8@16"
+ "q32@0:8@16^@24"
+ "r*16@0:8"
+ "raise:format:"
+ "rampMode"
+ "ramps"
+ "receivesLongFormAudioFromLocalDevice"
+ "recentlyUsedDevices"
+ "recognizingSpeech"
+ "recordingLoudnessRampWithStartValue:endValue:timeRange:"
+ "referencedObject"
+ "registerCallbackContextObject:"
+ "registerParticipant:"
+ "release"
+ "removeAllObjects"
+ "removeFrecencyInfoForDeviceID:"
+ "removeListenerWithWeakReference:callback:name:object:"
+ "removeObjectAtIndex:"
+ "removeObjectForKey:"
+ "removeOutputDevice:"
+ "removeOutputDevice:options:completionHandler:"
+ "removeOutputDevice:withOptions:completionHandler:"
+ "removeOutputDevice:withOptions:completionhandler:"
+ "removeOutputDevice:withOptions:fromRoutingContext:completionHandler:"
+ "removePeerWithIDFromHomeGroup:"
+ "removePointerAtIndex:"
+ "renderingStyleRampWithStartValue:endValue:timeRange:"
+ "replaceObjectAtIndex:withObject:"
+ "reportModificationMetrics:"
+ "requestCarUIForURL:withUUID:"
+ "requestTurnByTurnNavigationOwnership"
+ "requestViewArea:forScreenID:"
+ "requestedStatus != AVRoutingOperationStatusUnknown"
+ "requiresAuthorization"
+ "resetOutputDeviceForAllOutputContexts"
+ "resetPlatformIdentifierForQueue:"
+ "resetPredictedOutputDevice"
+ "respondWithAuthorizationToken:completionHandler:"
+ "respondsToSelector:"
+ "result"
+ "resultInput"
+ "retain"
+ "retainCount"
+ "retrieveSessionWithID:"
+ "rightBatteryLevel"
+ "rightHandDrive"
+ "routeConfigUpdateReason"
+ "routeDescriptionEvent"
+ "routeDescriptor"
+ "routeDiscoverer"
+ "routeDiscovererFactory"
+ "routingContextCommandPayload"
+ "routingContextFactory"
+ "routingContextUUID"
+ "routingplaybackarbiter_trace"
+ "routingsession_trace"
+ "routingutilities_trace"
+ "runBlockOnce:"
+ "s16@0:8"
+ "safeArea"
+ "scheduleBlock:"
+ "scheduledAudioParameters"
+ "scheduledFloatValueRampWithStartValue:endValue:timeRange:"
+ "scheduledParameterRampInterpolatedToTime:"
+ "scheduledParameterRampWithPropertyList:"
+ "scheduledaudioparameters_trace"
+ "screenID"
+ "screens"
+ "self"
+ "sendData:completionHandler:"
+ "serialNumber"
+ "server death"
+ "setActivatedDeviceClusterMembersVolume:withRoomID:"
+ "setAllowsHeadTrackedSpatialAudio:error:"
+ "setApplicationProcessID:"
+ "setAudioSessionID:"
+ "setAudioSessionId:"
+ "setCachedDiscoveryEnabled:"
+ "setCarPlayVideoActive:completionHandler:"
+ "setClientModificationFinishedTimestamp:"
+ "setClientModificationStartedTimestamp:"
+ "setCommunicationChannelDelegate:"
+ "setCompletionBlock:"
+ "setConversationDetectionEnabled:error:"
+ "setCurrentBluetoothListeningMode:"
+ "setCurrentBluetoothListeningMode:error:"
+ "setDefaultExternalPlaybackPriority"
+ "setDefaultNonMixableAudioPriority"
+ "setDeviceName:"
+ "setDevicePassword:"
+ "setDiscoveryMode:"
+ "setDiscoveryMode:forClientIdentifiers:"
+ "setDisplayCornerMasks:"
+ "setExternalPlaybackPriority:"
+ "setFigEndpointType:"
+ "setFinalConfiguration:"
+ "setFrecencyInfo:forDeviceID:"
+ "setHeadTrackedSpatialAudioMode:error:"
+ "setImplEventListener:"
+ "setInputDevice:options:completionHandler:"
+ "setInputMode:"
+ "setMaximumVolumeLimitForBuiltInSpeaker:"
+ "setMediaRemoteData:completionHandler:"
+ "setMuted:"
+ "setName:"
+ "setNonMixableAudioPriority:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setOnlyDiscoversBluetoothDevices:"
+ "setOutputContext:forContextID:"
+ "setOutputDevice:forFeatures:"
+ "setOutputDevice:options:"
+ "setOutputDevice:options:completionHandler:"
+ "setOutputDevice:withOptions:onRoutingContext:completionHandler:"
+ "setOutputDevices:"
+ "setOutputDevices:options:completionHandler:"
+ "setOutputDevices:withOptions:onRoutingContext:completionHandler:"
+ "setParentAuthorizationSession:"
+ "setParentAuthorizationSessionImpl:"
+ "setParentChannel:"
+ "setParentCommunicationChannel:"
+ "setParentInputContext:"
+ "setParentInputDeviceDiscoverySession:"
+ "setParentOutputContext:"
+ "setParentOutputContextImpl:"
+ "setParentOutputContextManager:"
+ "setParentOutputDevice:"
+ "setParentOutputDeviceDiscoverySession:"
+ "setParentOutputDeviceGroup:"
+ "setPlatformIdentifier:forQueue:"
+ "setPreferredParticipantForExternalPlayback:"
+ "setPreferredParticipantForNonMixableAudioRoutes:"
+ "setRouteDescriptor:"
+ "setSecondDisplayEnabled:"
+ "setSecondDisplayMode:completionHandler:"
+ "setSiriForwardingEnabled:"
+ "setTargetAudioSession:"
+ "setValue:forKey:"
+ "setViewAreaIndex:andAdjacentViewAreas:forScreenID:"
+ "setVolume:"
+ "setVolume:atTime:"
+ "setVolumeRampFromStartVolume:toEndVolume:timeRange:"
+ "setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:"
+ "setWithObjects:"
+ "sharedAudioPresentationOutputContext"
+ "sharedAuthorizationSession"
+ "sharedCallbackContextRegistry"
+ "sharedExecutionEnvironment"
+ "sharedInstance"
+ "sharedLocalDevice"
+ "sharedOutputDeviceTranslator"
+ "sharedRoutingPlaybackArbiter"
+ "sharedSystemAudioContext"
+ "sharedSystemAudioInputContext"
+ "sharedSystemRemoteDisplayContext"
+ "sharedSystemRemotePool"
+ "sharedSystemRemotePoolContext"
+ "sharedSystemRemotePoolImpl"
+ "sharedSystemScreenContext"
+ "shortValue"
+ "showErrorPromptDictionaryToEcho"
+ "signal"
+ "siriForwardingEnabled"
+ "softKeyboard"
+ "softPhoneKeypad"
+ "sortUsingComparator:"
+ "squarePixelSize"
+ "start"
+ "startAutomaticallyAllowingConnectionsFromPeersInHomeGroupAndRejectOtherConnections:"
+ "startFloatValue"
+ "startRoutingSessionForHighConfidenceExternalDestinationIfPresentWithCompletionHandler:"
+ "startRoutingSessionWithOutputDeviceDescriptions:error:"
+ "startSuppressingLikelyDestinationsUntilNextPlayEventAndReturnError:"
+ "startValue"
+ "startVolume"
+ "status"
+ "statusBarEdge"
+ "statusOfOperations:error:"
+ "stopAutomaticallyAllowingConnectionsFromPeersInHomeGroup"
+ "stopSuppressingLikelyDestinationsAndReturnError:"
+ "string"
+ "stringByAbbreviatingWithTildeInPath"
+ "stringByAppendingFormat:"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingString:"
+ "stringWithCString:encoding:"
+ "stringWithString:"
+ "stringWithValidatedFormat:validFormatSpecifiers:error:"
+ "stringWithValidatedFormatInteger"
+ "stringWithValidatedFormatString"
+ "suggestUI"
+ "suggestUIWithURLs:completionHandler:"
+ "superclass"
+ "supportedFeatures"
+ "supportsBluetoothSharing"
+ "supportsBufferedAirPlay"
+ "supportsConversationDetection"
+ "supportsDataOverACLProtocol"
+ "supportsFitnessDataDestination"
+ "supportsFocusTransfer"
+ "supportsHeadTrackedSpatialAudio"
+ "supportsHighQualityContentCapture"
+ "supportsMultipleBluetoothOutputDevices"
+ "supportsMultipleOutputDevices"
+ "supportsScreenMirroringControls"
+ "supportsSecureCoding"
+ "takeScreenForClient:reason:"
+ "targetAudioSession"
+ "through"
+ "time"
+ "timeIntervalSinceDate:"
+ "timeRange"
+ "transitionControl"
+ "transportType"
+ "typeWithIdentifier:"
+ "unfinishedOperations"
+ "unlock"
+ "unregisterCallbackContextForToken:"
+ "unsignedCharValue"
+ "unsignedIntValue"
+ "unsignedIntegerValue"
+ "unsignedLongLongValue"
+ "unsignedLongValue"
+ "unsignedShortValue"
+ "updateCurrentRoutingSessionFromLikelyDestinationsWithCompletionHandler:"
+ "updateFrecencyListForDeviceID:"
+ "updateFrecencyScore"
+ "urls"
+ "userInfo"
+ "userInitiated"
+ "userPreferredInputDevice:"
+ "uuid"
+ "v120@0:8{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}}16@112"
+ "v12@?0i8"
+ "v16@?0@\"AVInputContextDestinationChange\"8"
+ "v16@?0@\"AVOutputContextDestinationChange\"8"
+ "v16@?0@\"AVOutputDeviceGroupMembershipChangeResult\"8"
+ "v16@?0@\"NSNotification\"8"
+ "v20@0:8f16"
+ "v20@0:8i16"
+ "v24@0:8@\"<AVInputDeviceImplSupport>\"16"
+ "v24@0:8@\"<AVOutputDeviceDelegate>\"16"
+ "v24@0:8@\"<AVOutputDeviceImplSupport>\"16"
+ "v24@0:8@\"AVAudioSession\"16"
+ "v24@0:8@\"AVFigRoutingContextOutputContextImpl\"16"
+ "v24@0:8@\"AVInputContext\"16"
+ "v24@0:8@\"AVInputDeviceDiscoverySession\"16"
+ "v24@0:8@\"AVOutputContext\"16"
+ "v24@0:8@\"AVOutputContextCommunicationChannel\"16"
+ "v24@0:8@\"AVOutputContextManager\"16"
+ "v24@0:8@\"AVOutputDevice\"16"
+ "v24@0:8@\"AVOutputDeviceAuthorizationSession\"16"
+ "v24@0:8@\"AVOutputDeviceAuthorizedPeer\"16"
+ "v24@0:8@\"AVOutputDeviceCommunicationChannel\"16"
+ "v24@0:8@\"AVOutputDeviceDiscoverySession\"16"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8^v16"
+ "v24@0:8^{__CFDictionary=}16"
+ "v24@0:8^{__CFNumber=}16"
+ "v24@0:8^{__CFString=}16"
+ "v24@?0@8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v28@0:8@16B24"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v28@0:8f16@\"NSString\"20"
+ "v28@0:8f16@20"
+ "v32@0:8@\"AVInputDeviceDiscoverySession\"16@\"NSArray\"24"
+ "v32@0:8@\"AVOutputDeviceDiscoverySession\"16@\"NSArray\"24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"AVOutputDeviceCommunicationChannel\"@\"NSError\"@\"NSString\">24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8@16@24"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^{__CFString=}24"
+ "v32@0:8@?16@?24"
+ "v32@0:8^{__CFData=}16^{__CFString=}24"
+ "v32@0:8^{__CFNumber=}16^{__CFString=}24"
+ "v32@0:8^{__CFString=}16@24"
+ "v32@0:8^{__CFString=}16@?24"
+ "v32@0:8^{__CFString=}16^{__CFString=}24"
+ "v32@0:8q16@\"NSString\"24"
+ "v40@0:8@\"AVInputDevice\"16@\"NSDictionary\"24@?<v@?@\"AVInputContextDestinationChange\">32"
+ "v40@0:8@\"AVOutputDevice\"16@\"NSDictionary\"24@?<v@?@\"AVOutputContextDestinationChange\">32"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"AVOutputContextDestinationChange\">32"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8@?16@24@?32"
+ "v40@0:8@?<v@?@\"<AVOutputDeviceConfigurationModification>\">16@\"NSDictionary\"24@?<v@?q@\"<AVOutputDeviceConfigurationRetrieval>\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8^{__CFData=}16^{__CFString=}24^{__CFString=}32"
+ "v40@0:8^{__CFDictionary=}16^{__CFString=}24^{__CFDictionary=}32"
+ "v40@?0q8@\"<AVOutputDeviceConfigurationRetrieval>\"16@\"NSString\"24@\"NSError\"32"
+ "v44@0:8@16^{__CFDictionary=}24B32^{__CFString=}36"
+ "v44@0:8f16{?=qiIq}20"
+ "v48@0:8@\"AVOutputDevice\"16^{__CFDictionary=}24^{OpaqueFigRoutingContext=}32@?<v@?@\"AVOutputContextDestinationChange\">40"
+ "v48@0:8@\"NSArray\"16^{__CFDictionary=}24^{OpaqueFigRoutingContext=}32@?<v@?@\"AVOutputContextDestinationChange\">40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16^?24^{__CFString=}32^v40"
+ "v48@0:8@16^{__CFDictionary=}24^{OpaqueFigRoutingContext=}32@?40"
+ "v48@0:8{?=qiIq}16@40"
+ "v52@0:8@16^?24^{__CFString=}32^v40I48"
+ "v56@0:8@16@24@32@40@48"
+ "v64@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32^{__CFString=}40^{__CFString=}48^{__CFArray=}56"
+ "v72@0:8f16f20{?={?=qiIq}{?=qiIq}}24"
+ "v72@0:8{?={?=qiIq}{?=qiIq}}16@64"
+ "v80@0:8f16f20{?={?=qiIq}{?=qiIq}}24q72"
+ "valueForKey:"
+ "valueWithBytes:objCType:"
+ "valueWithCMTime:"
+ "valueWithCMTimeMapping:"
+ "valueWithCMTimeRange:"
+ "valueWithCMVideoDimensions:"
+ "valueWithPointer:"
+ "valueWithRect:"
+ "valueWithSize:"
+ "vide"
+ "viewArea"
+ "viewAreaIndex"
+ "viewAreas"
+ "viewHeightScaleFactor"
+ "visionOS"
+ "voiceTriggerMode"
+ "volume"
+ "volume %1.3f %@ time %1.3f%@%@"
+ "volumeControlType"
+ "volumeForActivatedDeviceClusterMembersWithRoomID:"
+ "volumeRampWithStartVolume:endVolume:timeRange:rampMode:"
+ "wait"
+ "waitUntilEventIsCompleted"
+ "weakObjectsPointerArray"
+ "widthPixels"
+ "willChangeValueForKey:"
+ "writeToFile:options:error:"
+ "xxxxDefaultValuexxxx"
+ "zone"
+ "{?=\"source\"{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}\"target\"{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}}"
+ "{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}"
+ "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
+ "{?=ii}"
+ "{?=ii}16@0:8"
+ "{?=qiIq}"
+ "{?=qiIq}16@0:8"
+ "{?=qiIq}24@0:8@16"
+ "{?={?=qiIq}{?=qiIq}}"
+ "{?={?=qiIq}{?=qiIq}}16@0:8"
+ "{?={?=qiIq}{?=qiIq}}24@0:8@16"
+ "{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}}"
+ "{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}}16@0:8"
+ "{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}}24@0:8@16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "\xb1"

```
