## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x1e065c
-  __TEXT.__auth_stubs: 0x50d0
-  __TEXT.__objc_methlist: 0x67c
-  __TEXT.__cstring: 0x74045
-  __TEXT.__const: 0xfd80
-  __TEXT.__gcc_except_tab: 0x94c
+890.61.4.11.2
+  __TEXT.__text: 0x20e730
+  __TEXT.__auth_stubs: 0x5530
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__cstring: 0x80aa6
+  __TEXT.__const: 0xfe00
+  __TEXT.__gcc_except_tab: 0x96c
   __TEXT.__dlopen_cstrs: 0x61d
-  __TEXT.__oslogstring: 0x6da
-  __TEXT.__unwind_info: 0x49e0
-  __TEXT.__eh_frame: 0xaa8
-  __TEXT.__objc_classname: 0x174
-  __TEXT.__objc_methname: 0x1a01
-  __TEXT.__objc_methtype: 0xa56
-  __TEXT.__objc_stubs: 0x17c0
-  __DATA_CONST.__got: 0x1d78
-  __DATA_CONST.__const: 0x6398
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__oslogstring: 0x794
+  __TEXT.__unwind_info: 0x5058
+  __TEXT.__objc_classname: 0x1c5
+  __TEXT.__objc_methname: 0x20e6
+  __TEXT.__objc_methtype: 0xd78
+  __TEXT.__objc_stubs: 0x1d80
+  __DATA_CONST.__got: 0x1fb0
+  __DATA_CONST.__const: 0x6a70
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c8
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2878
-  __AUTH_CONST.__const: 0x77e0
-  __AUTH_CONST.__cfstring: 0x10e80
-  __AUTH_CONST.__objc_const: 0xb88
-  __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x598
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x183c8
-  __DATA.__bss: 0x9d0
-  __DATA.__common: 0xa08
+  __DATA_CONST.__objc_selrefs: 0x9a8
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_arraydata: 0x88
+  __AUTH_CONST.__auth_got: 0x2aa8
+  __AUTH_CONST.__const: 0x7e80
+  __AUTH_CONST.__cfstring: 0x12220
+  __AUTH_CONST.__objc_const: 0xec0
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x190
+  __AUTH.__data: 0x7b0
+  __DATA.__objc_ivar: 0x88
+  __DATA.__data: 0x18648
+  __DATA.__bss: 0xa60
+  __DATA.__common: 0xa10
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xc50
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__data: 0xcc8
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/APTransport.framework/APTransport
+  - /System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver
   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B34BBEF-CD9F-372E-A543-0A93184DD346
-  Functions: 8767
-  Symbols:   22374
-  CStrings:  12046
+  UUID: 1E013AE1-6DCC-3F1D-9679-5A277E9C2B33
+  Functions: 9625
+  Symbols:   24270
+  CStrings:  13292
 
Symbols:
+ +[APHTTPProxyMonitorClientManager obtainSharedInstanceOrCreate:]
+ -[APHTTPProxyMonitorClient dealloc]
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:]
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.1
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.2
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.3
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.4
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.5
+ -[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:].cold.6
+ -[APHTTPProxyMonitorClient deviceIsRegisteredDidChange:isRegistered:]
+ -[APHTTPProxyMonitorClient initWithCallback:forLink:forIP:]
+ -[APHTTPProxyMonitorClient registerToDeviceManager]
+ -[APHTTPProxyMonitorClient registerToDeviceManager].cold.1
+ -[APHTTPProxyMonitorClient registerToDeviceManager].cold.2
+ -[APHTTPProxyMonitorClient registerToDeviceManager].cold.3
+ -[APHTTPProxyMonitorClient registerToDeviceManager].cold.4
+ -[APHTTPProxyMonitorClientManager dealloc]
+ -[APHTTPProxyMonitorClientManager init]
+ -[APHTTPProxyMonitorClientManager removeMonitorClientForKey:]
+ -[APHTTPProxyMonitorClientManager removeMonitorClientForKey:].cold.1
+ -[APHTTPProxyMonitorClientManager removeMonitorClientForKey:].cold.2
+ -[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:]
+ -[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:].cold.1
+ -[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:].cold.2
+ -[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:].cold.3
+ -[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:].cold.4
+ GCC_except_table40
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table96
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName
+ _APAudioEngineBufferedAdapterCreate
+ _APAudioEngineBufferedAdapterCreate.cold.1
+ _APAudioEngineBufferedAdapterCreate.cold.10
+ _APAudioEngineBufferedAdapterCreate.cold.11
+ _APAudioEngineBufferedAdapterCreate.cold.12
+ _APAudioEngineBufferedAdapterCreate.cold.13
+ _APAudioEngineBufferedAdapterCreate.cold.14
+ _APAudioEngineBufferedAdapterCreate.cold.15
+ _APAudioEngineBufferedAdapterCreate.cold.16
+ _APAudioEngineBufferedAdapterCreate.cold.17
+ _APAudioEngineBufferedAdapterCreate.cold.18
+ _APAudioEngineBufferedAdapterCreate.cold.19
+ _APAudioEngineBufferedAdapterCreate.cold.2
+ _APAudioEngineBufferedAdapterCreate.cold.20
+ _APAudioEngineBufferedAdapterCreate.cold.21
+ _APAudioEngineBufferedAdapterCreate.cold.22
+ _APAudioEngineBufferedAdapterCreate.cold.3
+ _APAudioEngineBufferedAdapterCreate.cold.4
+ _APAudioEngineBufferedAdapterCreate.cold.5
+ _APAudioEngineBufferedAdapterCreate.cold.6
+ _APAudioEngineBufferedAdapterCreate.cold.7
+ _APAudioEngineBufferedAdapterCreate.cold.8
+ _APAudioEngineBufferedAdapterCreate.cold.9
+ _APAudioEngineBufferedCreate.cold.40
+ _APAudioEngineBufferedCreate.cold.41
+ _APAudioEngineRealTimeCreate.cold.32
+ _APAudioEngineRealTimeCreate.cold.33
+ _APAudioEngineRealTimeCreate.cold.34
+ _APAudioEngineRealTimeCreate.cold.35
+ _APAudioEngineRealTimeCreate.cold.36
+ _APAudioEngineRealTimeCreate.cold.37
+ _APAudioEngineRealTimeCreate.cold.38
+ _APAudioFormatCopyPreferredRealTimeAudioFormatsSender
+ _APBrowserControllerRegisterInternalClientNeedsDiscovery
+ _APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber
+ _APDemoManagerStartWithClientPid
+ _APDemoManagerStartWithClientPid.cold.1
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.1
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.2
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.3
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.4
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.5
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.6
+ _APEndpointDescriptionAirPlayCreateWithBonjourInfo.cold.7
+ _APEndpointDescriptionMockCreate
+ _APEndpointManagerPlusCreate
+ _APEndpointManagerPlusCreate.cold.1
+ _APEndpointManagerPlusCreate.cold.2
+ _APEndpointManagerPlusCreate.cold.3
+ _APEndpointManagerPlusCreate.cold.4
+ _APEndpointManagerUpdateInternalClientNeedingDiscovery
+ _APEndpointManagerUpdateInternalClientNeedingDiscovery.cold.1
+ _APEndpointManagerUpdateInternalClientNeedingDiscovery.cold.2
+ _APEndpointPlaybackSessionRemoteControlCreate.cold.12
+ _APEndpointPlaybackSessionRemoteControlCreate.cold.13
+ _APEndpointPlusAddSubEndpoint
+ _APEndpointPlusAddSubEndpoint.cold.1
+ _APEndpointPlusAddSubEndpoint.cold.2
+ _APEndpointPlusAddSubEndpoint.cold.3
+ _APEndpointPlusAddSubEndpoint.cold.4
+ _APEndpointPlusCopyInner
+ _APEndpointPlusCopySubEndpoint
+ _APEndpointPlusCreate
+ _APEndpointPlusCreate.cold.1
+ _APEndpointPlusCreate.cold.2
+ _APEndpointPlusCreateWithBonjourInfo
+ _APEndpointPlusCreateWithBonjourInfo.cold.1
+ _APEndpointPlusCreateWithBonjourInfo.cold.2
+ _APEndpointPlusCreateWithBonjourInfo.cold.3
+ _APEndpointPlusCreateWithBonjourInfo.cold.4
+ _APEndpointPlusCreateWithBonjourInfo.cold.5
+ _APEndpointPlusCreateWithBonjourInfo.cold.6
+ _APEndpointPlusCreateWithInnerEndpoint
+ _APEndpointPlusCreateWithInnerEndpoint.cold.1
+ _APEndpointPlusCreateWithInnerEndpoint.cold.2
+ _APEndpointPlusCreateWithInnerEndpoint.cold.3
+ _APEndpointPlusCreateWithInnerEndpoint.cold.4
+ _APEndpointPlusGetSubEndpointCount
+ _APEndpointPlusRemoveSubEndpoint
+ _APEndpointPlusRemoveSubEndpoint.cold.1
+ _APEndpointPlusRemoveSubEndpoint.cold.2
+ _APEndpointPlusRemoveSubEndpoint.cold.3
+ _APEndpointPlusRemoveSubEndpoint.cold.4
+ _APEndpointPlusSetInner
+ _APEndpointPlusUtils_CopyClusterIDFromBonjourInfo
+ _APEndpointPlusUtils_CopyDeviceIDFromBonjourInfo
+ _APEndpointPlusUtils_CopyDeviceIDFromEndpointDescription
+ _APEndpointPlusUtils_CopyDeviceIDFromEndpointDescription.cold.1
+ _APEndpointPlusUtils_GetEndpointType
+ _APEndpointPlusUtils_GetTypeString
+ _APEndpointStreamAudioCreate.cold.27
+ _APEndpointStreamAudioCreate.cold.28
+ _APEndpointStreamAudioCreate.cold.29
+ _APEndpointStreamAudioCreate.cold.30
+ _APEndpointStreamLocalCreate.cold.9
+ _APEndpointStreamScreenCreate.cold.29
+ _APEndpointStreamScreenUDPCreate.cold.29
+ _APEndpointTriggerAudioHALDeviceCreationEx
+ _APEndpointTriggerAudioHALDeviceCreationEx.cold.1
+ _APEndpointTriggerAudioHALDeviceCreationEx.cold.2
+ _APEndpointUGLWrapperAddShadowEndpoint
+ _APEndpointUGLWrapperCreate
+ _APEndpointUGLWrapperCreate.cold.1
+ _APEndpointUGLWrapperCreate.cold.2
+ _APEndpointUGLWrapperCreate.cold.3
+ _APEndpointUGLWrapperCreate.cold.4
+ _APEndpointUGLWrapperCreate.cold.5
+ _APEndpointUGLWrapperCreate.cold.6
+ _APEndpointUGLWrapperCreate.cold.7
+ _APEndpointUGLWrapperIsEmpty
+ _APEndpointUGLWrapperRemoveShadowEndpoint
+ _APEndpointUGLWrapperUpdateWithTransportDevice
+ _APEndpointUGLWrapper_AcquireAndCopyResource
+ _APEndpointUGLWrapper_ActivateForFeaturesWithCompletionCallback
+ _APEndpointUGLWrapper_BorrowScreen
+ _APEndpointUGLWrapper_CloseAllCommChannels
+ _APEndpointUGLWrapper_CloseAllCommChannels.cold.1
+ _APEndpointUGLWrapper_CloseCommChannel
+ _APEndpointUGLWrapper_CopyDebugDescription
+ _APEndpointUGLWrapper_CopyProperty
+ _APEndpointUGLWrapper_CreateCommChannel
+ _APEndpointUGLWrapper_CreateCommChannel.cold.1
+ _APEndpointUGLWrapper_CreatePlaybackSession
+ _APEndpointUGLWrapper_CreatePlaybackSession.cold.1
+ _APEndpointUGLWrapper_CreateRemoteControlSession
+ _APEndpointUGLWrapper_CreateRemoteControlSession.cold.1
+ _APEndpointUGLWrapper_DeactivateWithCompletionCallback
+ _APEndpointUGLWrapper_DeactivateWithCompletionCallback.cold.1
+ _APEndpointUGLWrapper_Dissociate
+ _APEndpointUGLWrapper_Dissociate.cold.1
+ _APEndpointUGLWrapper_DuckAudio
+ _APEndpointUGLWrapper_EnsureAuthorizedWithCompletionCallback
+ _APEndpointUGLWrapper_EnsureAuthorizedWithCompletionCallback.cold.1
+ _APEndpointUGLWrapper_Finalize
+ _APEndpointUGLWrapper_Finalize.cold.1
+ _APEndpointUGLWrapper_RelinquishResource
+ _APEndpointUGLWrapper_SendCommand
+ _APEndpointUGLWrapper_SendData
+ _APEndpointUGLWrapper_SetDelegate
+ _APEndpointUGLWrapper_SetDelegateRemoteControl
+ _APEndpointUGLWrapper_SetDelegateRouting
+ _APEndpointUGLWrapper_SetDelegateVolumeAndMute
+ _APEndpointUGLWrapper_SetProperty
+ _APEndpointUGLWrapper_UnborrowScreen
+ _APHTTPProxyMonitorClientRegisterHTTPProxyMonitor
+ _APHTTPProxyMonitorClientRegisterHTTPProxyMonitor.cold.1
+ _APHTTPProxyMonitorClientUnregisterHTTPProxyMonitor
+ _APHTTPProxyMonitorClientUnregisterHTTPProxyMonitor.cold.1
+ _APMulticastProbeSenderCopySSMGroupInfo
+ _APMulticastProbeSenderCreate
+ _APMulticastProbeSenderCreate.cold.1
+ _APMulticastProbeSenderGetCMBaseObject
+ _APMulticastProbeSenderGetShared
+ _APMulticastProbeSenderGetShared.cold.1
+ _APMulticastProbeSenderGetShared.multicastProbeSender
+ _APMulticastProbeSenderGetShared.once
+ _APMulticastProbeSenderRegister
+ _APMulticastProbeSenderRegister.cold.1
+ _APMulticastProbeSenderRegister.cold.10
+ _APMulticastProbeSenderRegister.cold.11
+ _APMulticastProbeSenderRegister.cold.12
+ _APMulticastProbeSenderRegister.cold.13
+ _APMulticastProbeSenderRegister.cold.14
+ _APMulticastProbeSenderRegister.cold.15
+ _APMulticastProbeSenderRegister.cold.16
+ _APMulticastProbeSenderRegister.cold.17
+ _APMulticastProbeSenderRegister.cold.18
+ _APMulticastProbeSenderRegister.cold.2
+ _APMulticastProbeSenderRegister.cold.3
+ _APMulticastProbeSenderRegister.cold.4
+ _APMulticastProbeSenderRegister.cold.5
+ _APMulticastProbeSenderRegister.cold.6
+ _APMulticastProbeSenderRegister.cold.7
+ _APMulticastProbeSenderRegister.cold.8
+ _APMulticastProbeSenderRegister.cold.9
+ _APMulticastProbeSenderReleaseSSMGroupInfo
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.1
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.2
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.3
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.4
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.5
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.6
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.7
+ _APMulticastProbeSenderReleaseSSMGroupInfo.cold.8
+ _APMulticastProbeSenderUnregister
+ _APMulticastProbeSenderUnregister.cold.1
+ _APMulticastProbeSenderUnregister.cold.10
+ _APMulticastProbeSenderUnregister.cold.11
+ _APMulticastProbeSenderUnregister.cold.12
+ _APMulticastProbeSenderUnregister.cold.2
+ _APMulticastProbeSenderUnregister.cold.3
+ _APMulticastProbeSenderUnregister.cold.4
+ _APMulticastProbeSenderUnregister.cold.5
+ _APMulticastProbeSenderUnregister.cold.6
+ _APMulticastProbeSenderUnregister.cold.7
+ _APMulticastProbeSenderUnregister.cold.8
+ _APMulticastProbeSenderUnregister.cold.9
+ _APMulticastProbeSenderUpdateMC2UC
+ _APMulticastProbeSenderUpdateMC2UC.cold.1
+ _APMulticastProbeSenderUpdateMC2UC.cold.2
+ _APMulticastProbeSenderUpdateMC2UC.cold.3
+ _APMulticastProbeSenderUpdateMC2UC.cold.4
+ _APPWDKeyExchangeSenderSessionCopyEncoderEncryptionKeyID
+ _APPWDKeyExchangeSenderSessionCopyEncoderEncryptionKeyID.cold.1
+ _APSAudioFormatDescriptionCreateWithAudioFormatIndex
+ _APSAudioFormatDescriptionGetChannelLayoutTag
+ _APSAudioFormatDescriptionIsPassthroughFormatForCurrentDeviceAsSender
+ _APSAudioFormatDescriptionListCopyChannelLayoutTagsDataArray
+ _APSAudioFormatDescriptionListCreateCopy
+ _APSAudioHoseMetricCollectorCreate
+ _APSAudioHoseMetricCollectorDeregisterHose
+ _APSAudioHoseMetricCollectorRegisterHose
+ _APSAudioHoseMetricCollectorReportMetrics
+ _APSAudioHoseMetricCollectorSetPlaybackStateForHose
+ _APSAudioHoseMetricCollectorUpdateMediaTimeStatsForHose
+ _APSAudioHoseMetricCollectorUpdateSendRateForHose
+ _APSAudioLatencyForSystemAudioInClusterModelMs
+ _APSAudioProtocolDriverHoseControlEnableLoudnessNormalization
+ _APSAudioProtocolDriverHoseControlGetAnchor
+ _APSAudioProtocolDriverHoseControlProtocolGetProtocolID
+ _APSAudioProtocolDriverHoseDataAPATProtocolGetProtocolID
+ _APSAudioProtocolDriverHoseDataBaseProtocolGetProtocolID
+ _APSAudioProtocolDriverSenderAPATCreate
+ _APSAudioProtocolDriverSenderGetCMBaseObject
+ _APSAudioProtocolDriverSenderLocalCreate
+ _APSAudioProtocolDriverTriggerBurst
+ _APSCFDictionarySetSockAddr
+ _APSCFStringToSockAddr
+ _APSCopyNetworkInterfaceType
+ _APSDataPacerBitRateCreate
+ _APSDataPacerBitRateUpdate
+ _APSDataPacerGetTypeID
+ _APSDataPacerHoseCountCreateWithDefaultCapacityForCurrentDevice
+ _APSDataPacerHoseCountDecrement
+ _APSDataPacerHoseCountIncrement
+ _APSDynamicLatencyManagerGetRef
+ _APSEventRecorderGetTimeBetweenEventRecorderTimeAndEventInMilliSecond
+ _APSEventRecorderGetTimeFromDictionaryIfPresent
+ _APSEventRecorderSetTimeInDictionary
+ _APSFeaturesCreateFromStringRepresentation
+ _APSIsOpenNANSenderEnabled
+ _APSRealTimeAllocatorAllocate
+ _APSRealTimeAllocatorDeallocate
+ _APSRealTimeDispatcherAsync
+ _APSRealTimeDispatcherCreate
+ _APSSettingsGetUInt64IfPresent
+ _APSenderSessionAirPlayCreate.cold.16
+ _APSenderSessionShouldEstablishNetworkClockLink
+ _APSenderSessionShouldPerformNetworkClockSETPEERS
+ _APTransportDeviceCopyInfo
+ _APTransportDeviceCreateWithNetworkAddresses
+ _AirPlayDebugIPCDisableForEndpointManager.cold.5
+ _AirPlayDebugIPCEnableForEndpointManager.cold.7
+ _AirPlayDebugIPCEnableForEndpointManager.initOnce
+ _AirPlayReceiverServerControl
+ _AirPlayReceiverServerCopyProperty
+ _AirPlayReceiverServerCreate
+ _AirPlayReceiverServerGetDispatchQueue
+ _AirPlayReceiverServerSetProperty
+ _AirPlayStartServicesInMXProcess.cold.1
+ _AirPlayStartServicesInMXProcess.cold.2
+ _AirPlayXPCServicesStart.cold.1
+ _AirPlayXPCServicesStart.cold.10
+ _AirPlayXPCServicesStart.cold.11
+ _AirPlayXPCServicesStart.cold.12
+ _AirPlayXPCServicesStart.cold.13
+ _AirPlayXPCServicesStart.cold.2
+ _AirPlayXPCServicesStart.cold.3
+ _AirPlayXPCServicesStart.cold.4
+ _AirPlayXPCServicesStart.cold.5
+ _AirPlayXPCServicesStart.cold.6
+ _AirPlayXPCServicesStart.cold.7
+ _AirPlayXPCServicesStart.cold.8
+ _AirPlayXPCServicesStart.cold.9
+ _BonjourDevice_CopyCFString
+ _CFAllocatorAllocateTyped
+ _CFAllocatorReallocateTyped
+ _CFDataGetEmpty
+ _CFObjectControlSync
+ _CFStringGetCharacterAtIndex
+ _CMAudioFormatDescriptionCreate
+ _CMBaseObjectCopyProperty
+ _CMBaseObjectSetProperty
+ _CUObfuscatedPtr
+ _CreateUsableInterfaceList
+ _FVDUtilsHEVCEncoderSupports44410
+ _FVDUtilsSupportedProtectionFlags
+ _FigCFArrayAppendInt64
+ _FigCFArrayApplyBlock
+ _FigCFArrayContainsInt64
+ _FigCFArrayCreateConcatenationOfTwoArrays
+ _FigCFArrayCreateCopy
+ _FigCFArrayGetValueAtIndex
+ _FigCFDictionaryGetArrayValue
+ _FigCFDictionaryGetDictionaryValue
+ _FigCFDictionaryGetValueIfPresent
+ _FigCFSetApplyBlock
+ _FigEndpointAudioSourceCopyProperty
+ _FigEndpointAudioSourceResume
+ _FigEndpointAudioSourceSetWriteHandler
+ _FigEndpointManagerCopyProperty
+ _FigEndpointStreamAudioEngineResumeSync
+ _FigEndpointStreamAudioEngineSetEndpointStreamSync
+ _FigEndpointStreamAudioEngineSuspendSync
+ _FigGetUpTime
+ _FigPWDKeyExchangeSenderInitializeAMS
+ _FigSignalErrorAt3
+ _FigVirtualDisplaySinkGetCMBaseObject
+ _FigVirtualDisplaySourceGetCMBaseObject
+ _GestaltGetDeviceClass
+ _IsAnUGLWrapperEndpoint
+ _OBJC_CLASS_$_APBonjourCacheHomeKit
+ _OBJC_CLASS_$_APHTTPProxyMonitorClient
+ _OBJC_CLASS_$_APHTTPProxyMonitorClientManager
+ _OBJC_CLASS_$_NRDeviceIdentifier
+ _OBJC_CLASS_$_NRDeviceManager
+ _OBJC_CLASS_$_NRDeviceMonitor
+ _OBJC_CLASS_$_NRDeviceOperationalProperties
+ _OBJC_CLASS_$_NRDevicePairingProperties
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._desiredSockAddr
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._dispatchQueue
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._handleProxyParametersChanged
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._hasDesiredSockAddr
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._isWireless
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._nrDeviceID
+ _OBJC_IVAR_$_APHTTPProxyMonitorClient._nrMonitor
+ _OBJC_IVAR_$_APHTTPProxyMonitorClientManager._mutex
+ _OBJC_IVAR_$_APHTTPProxyMonitorClientManager._requesterDict
+ _OBJC_METACLASS_$_APHTTPProxyMonitorClient
+ _OBJC_METACLASS_$_APHTTPProxyMonitorClientManager
+ _ReleaseUsableInterfaceList
+ _SockAddrCompareAddr
+ _SocketSetMulticastInterface
+ __APMulticastProbeSenderFormattingDescription
+ __HandleFailureCallback
+ __MergedGlobals.894
+ __OBJC_$_CLASS_METHODS_APHTTPProxyMonitorClientManager
+ __OBJC_$_INSTANCE_METHODS_APHTTPProxyMonitorClient
+ __OBJC_$_INSTANCE_METHODS_APHTTPProxyMonitorClientManager
+ __OBJC_$_INSTANCE_VARIABLES_APHTTPProxyMonitorClient
+ __OBJC_$_INSTANCE_VARIABLES_APHTTPProxyMonitorClientManager
+ __OBJC_$_PROP_LIST_APHTTPProxyMonitorClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_NRDeviceMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_APHTTPProxyMonitorClient
+ __OBJC_CLASS_RO_$_APHTTPProxyMonitorClient
+ __OBJC_CLASS_RO_$_APHTTPProxyMonitorClientManager
+ __OBJC_LABEL_PROTOCOL_$_NRDeviceMonitorDelegate
+ __OBJC_METACLASS_RO_$_APHTTPProxyMonitorClient
+ __OBJC_METACLASS_RO_$_APHTTPProxyMonitorClientManager
+ __OBJC_PROTOCOL_$_NRDeviceMonitorDelegate
+ ___51-[APHTTPProxyMonitorClient registerToDeviceManager]_block_invoke
+ ___51-[APHTTPProxyMonitorClient registerToDeviceManager]_block_invoke.cold.1
+ ___64+[APHTTPProxyMonitorClientManager obtainSharedInstanceOrCreate:]_block_invoke
+ ___APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke
+ ___APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke.cold.1
+ ___APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke.cold.2
+ ___APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke.cold.3
+ ___APDemoManagerCopyDeviceInfo_block_invoke.cold.3
+ ___APEndpointUGLWrapper_Dissociate_block_invoke
+ ___APGetEndpointManager_block_invoke.cold.8
+ ___APMulticastProbeSenderGetShared_block_invoke
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.1
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.2
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.3
+ ___APMulticastProbeSenderGetShared_block_invoke.cold.4
+ ___AirPlayDebugIPCEnableForEndpointManager_block_invoke
+ ___apsession_copyActiveStreamConnectionIDs_block_invoke
+ ___apsession_copyActiveStreamConnectionIDs_block_invoke.cold.1
+ ___apsession_copyNetworkPropertyInternal_block_invoke
+ ___apsession_copyNetworkPropertyInternal_block_invoke.cold.1
+ ___apsession_getKeepAliveMode_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e47_v28?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20l
+ ___block_descriptor_40_e8_32o_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32o_e47_v28?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20ls32l8
+ ___block_descriptor_40_e8_32o_e68_v36?0^{OpaqueFigEndpoint=}8^{__CFString=}16C24r^^{__CFDictionary}28ls32l8
+ ___block_descriptor_40_e8_32r_e10_v16?0r^v8lr32l8
+ ___block_descriptor_41_e47_v28?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20l
+ ___block_descriptor_48_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32o_e37_v24?0^{__CFString=}8^{__CFString=}16ls32l8
+ ___block_descriptor_48_e8_32o_e38_v24?0^{__CFString=}8r^^{__CFString}16ls32l8
+ ___block_descriptor_64_e8_32o40o48o56o_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e5_v8?0l
+ ___block_descriptor_72_e5_v8?0l
+ ___block_descriptor_76_e5_v8?0l
+ ___block_descriptor_tmp.1025
+ ___block_descriptor_tmp.1026
+ ___block_descriptor_tmp.1030
+ ___block_descriptor_tmp.1032
+ ___block_descriptor_tmp.1033
+ ___block_descriptor_tmp.1049
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.1079
+ ___block_descriptor_tmp.1084
+ ___block_descriptor_tmp.1089
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.1091
+ ___block_descriptor_tmp.1095
+ ___block_descriptor_tmp.1096
+ ___block_descriptor_tmp.1097
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.1102
+ ___block_descriptor_tmp.1104
+ ___block_descriptor_tmp.1114
+ ___block_descriptor_tmp.1116
+ ___block_descriptor_tmp.1137
+ ___block_descriptor_tmp.1139
+ ___block_descriptor_tmp.1144
+ ___block_descriptor_tmp.1145
+ ___block_descriptor_tmp.1152
+ ___block_descriptor_tmp.1153
+ ___block_descriptor_tmp.1164
+ ___block_descriptor_tmp.1166
+ ___block_descriptor_tmp.1177
+ ___block_descriptor_tmp.1186
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.1209
+ ___block_descriptor_tmp.1210
+ ___block_descriptor_tmp.1218
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.1221
+ ___block_descriptor_tmp.1226
+ ___block_descriptor_tmp.1230
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.176
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.206
+ ___block_descriptor_tmp.238
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.248
+ ___block_descriptor_tmp.279
+ ___block_descriptor_tmp.282
+ ___block_descriptor_tmp.304
+ ___block_descriptor_tmp.310
+ ___block_descriptor_tmp.329
+ ___block_descriptor_tmp.33
+ ___block_descriptor_tmp.334
+ ___block_descriptor_tmp.340
+ ___block_descriptor_tmp.350
+ ___block_descriptor_tmp.362
+ ___block_descriptor_tmp.367
+ ___block_descriptor_tmp.401
+ ___block_descriptor_tmp.406
+ ___block_descriptor_tmp.439
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.440
+ ___block_descriptor_tmp.444
+ ___block_descriptor_tmp.446
+ ___block_descriptor_tmp.447
+ ___block_descriptor_tmp.450
+ ___block_descriptor_tmp.456
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.470
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.494
+ ___block_descriptor_tmp.498
+ ___block_descriptor_tmp.502
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.512
+ ___block_descriptor_tmp.524
+ ___block_descriptor_tmp.525
+ ___block_descriptor_tmp.526
+ ___block_descriptor_tmp.531
+ ___block_descriptor_tmp.578
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.614
+ ___block_descriptor_tmp.635
+ ___block_descriptor_tmp.713
+ ___block_descriptor_tmp.715
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.721
+ ___block_descriptor_tmp.723
+ ___block_descriptor_tmp.727
+ ___block_descriptor_tmp.729
+ ___block_descriptor_tmp.730
+ ___block_descriptor_tmp.77
+ ___block_descriptor_tmp.777
+ ___block_descriptor_tmp.778
+ ___block_descriptor_tmp.779
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.781
+ ___block_descriptor_tmp.782
+ ___block_descriptor_tmp.783
+ ___block_descriptor_tmp.802
+ ___block_descriptor_tmp.803
+ ___block_descriptor_tmp.804
+ ___block_descriptor_tmp.806
+ ___block_descriptor_tmp.808
+ ___block_descriptor_tmp.811
+ ___block_descriptor_tmp.814
+ ___block_descriptor_tmp.822
+ ___block_descriptor_tmp.824
+ ___block_descriptor_tmp.827
+ ___block_descriptor_tmp.828
+ ___block_descriptor_tmp.840
+ ___block_descriptor_tmp.842
+ ___block_descriptor_tmp.853
+ ___block_descriptor_tmp.861
+ ___block_descriptor_tmp.867
+ ___block_descriptor_tmp.933
+ ___block_descriptor_tmp.96
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.115
+ ___block_literal_global.121
+ ___block_literal_global.163
+ ___block_literal_global.169
+ ___block_literal_global.173
+ ___block_literal_global.181
+ ___block_literal_global.223
+ ___block_literal_global.236
+ ___block_literal_global.28
+ ___block_literal_global.312
+ ___block_literal_global.323
+ ___block_literal_global.426
+ ___block_literal_global.472
+ ___block_literal_global.494
+ ___block_literal_global.574
+ ___block_literal_global.61
+ ___block_literal_global.68
+ ___block_literal_global.808
+ ___bufferedAudioEngine_audioTimer_block_invoke
+ ___bufferedAudioEngine_audioTimer_block_invoke.cold.1
+ ___bufferedAudioEngine_flushHoseWithinSampleRange_block_invoke
+ ___bufferedAudioEngine_flushHose_block_invoke
+ ___bufferedAudioEngine_flushInternal_block_invoke
+ ___bufferedAudioEngine_flushWithinSampleRangeInternal_block_invoke
+ ___bufferedAudioEngine_hoseFlushCallbackCompletionHandlerInternal_block_invoke
+ ___bufferedAudioEngine_hoseFlushWithinSampleRangeCallbackCompletionHandlerInternal_block_invoke
+ ___bufferedAudioEngine_pruneMessageRingToCurrentRemoteMediaTimeWithForwardMargin_block_invoke_2
+ ___carEndpoint_Activate_block_invoke.cold.10
+ ___carEndpoint_Activate_block_invoke.cold.11
+ ___carEndpoint_Activate_block_invoke.cold.12
+ ___carEndpoint_Activate_block_invoke.cold.13
+ ___carEndpoint_Activate_block_invoke.cold.14
+ ___carEndpoint_Activate_block_invoke.cold.15
+ ___carEndpoint_Activate_block_invoke.cold.16
+ ___carEndpoint_Activate_block_invoke.cold.17
+ ___carEndpoint_Activate_block_invoke.cold.18
+ ___carEndpoint_Activate_block_invoke.cold.19
+ ___carEndpoint_Activate_block_invoke.cold.2
+ ___carEndpoint_Activate_block_invoke.cold.20
+ ___carEndpoint_Activate_block_invoke.cold.21
+ ___carEndpoint_Activate_block_invoke.cold.22
+ ___carEndpoint_Activate_block_invoke.cold.23
+ ___carEndpoint_Activate_block_invoke.cold.24
+ ___carEndpoint_Activate_block_invoke.cold.25
+ ___carEndpoint_Activate_block_invoke.cold.26
+ ___carEndpoint_Activate_block_invoke.cold.27
+ ___carEndpoint_Activate_block_invoke.cold.28
+ ___carEndpoint_Activate_block_invoke.cold.29
+ ___carEndpoint_Activate_block_invoke.cold.3
+ ___carEndpoint_Activate_block_invoke.cold.30
+ ___carEndpoint_Activate_block_invoke.cold.31
+ ___carEndpoint_Activate_block_invoke.cold.32
+ ___carEndpoint_Activate_block_invoke.cold.33
+ ___carEndpoint_Activate_block_invoke.cold.34
+ ___carEndpoint_Activate_block_invoke.cold.35
+ ___carEndpoint_Activate_block_invoke.cold.36
+ ___carEndpoint_Activate_block_invoke.cold.37
+ ___carEndpoint_Activate_block_invoke.cold.38
+ ___carEndpoint_Activate_block_invoke.cold.39
+ ___carEndpoint_Activate_block_invoke.cold.4
+ ___carEndpoint_Activate_block_invoke.cold.40
+ ___carEndpoint_Activate_block_invoke.cold.41
+ ___carEndpoint_Activate_block_invoke.cold.42
+ ___carEndpoint_Activate_block_invoke.cold.43
+ ___carEndpoint_Activate_block_invoke.cold.44
+ ___carEndpoint_Activate_block_invoke.cold.45
+ ___carEndpoint_Activate_block_invoke.cold.46
+ ___carEndpoint_Activate_block_invoke.cold.47
+ ___carEndpoint_Activate_block_invoke.cold.48
+ ___carEndpoint_Activate_block_invoke.cold.49
+ ___carEndpoint_Activate_block_invoke.cold.5
+ ___carEndpoint_Activate_block_invoke.cold.50
+ ___carEndpoint_Activate_block_invoke.cold.51
+ ___carEndpoint_Activate_block_invoke.cold.52
+ ___carEndpoint_Activate_block_invoke.cold.53
+ ___carEndpoint_Activate_block_invoke.cold.6
+ ___carEndpoint_Activate_block_invoke.cold.7
+ ___carEndpoint_Activate_block_invoke.cold.8
+ ___carEndpoint_Activate_block_invoke.cold.9
+ ___carEndpoint_UpdateFeaturesWithCompletionCallback_block_invoke
+ ___carEndpoint_activateInternal_block_invoke.135
+ ___carEndpoint_activateInternal_block_invoke.135.cold.1
+ ___carEndpoint_activateInternal_block_invoke.135.cold.2
+ ___carEndpoint_activateInternal_block_invoke.135.cold.3
+ ___carEndpoint_activateInternal_block_invoke.135.cold.4
+ ___carEndpoint_activateInternal_block_invoke.135.cold.5
+ ___carEndpoint_activateInternal_block_invoke.135.cold.6
+ ___carEndpoint_activateInternal_block_invoke.135.cold.7
+ ___carEndpoint_activateInternal_block_invoke.135.cold.8
+ ___carEndpoint_activateInternal_block_invoke.135.cold.9
+ ___carEndpoint_activateInternal_block_invoke_2.140.cold.1
+ ___carEndpoint_activateInternal_block_invoke_2.140.cold.2
+ ___carEndpoint_activateInternal_block_invoke_2.151
+ ___carEndpoint_activateInternal_block_invoke_3.156
+ ___carEndpoint_activateInternal_block_invoke_3.156.cold.1
+ ___carEndpoint_copyStateProperty_block_invoke_2
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke.cold.1
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke.cold.2
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke.cold.3
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke.cold.4
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke.cold.5
+ ___carEndpoint_createPlaybackSessionInternal_block_invoke_2
+ ___carEndpoint_deactivateInternal_block_invoke_6
+ ___carEndpoint_logStats_block_invoke
+ ___carEndpoint_registerForHTTPProxy_block_invoke
+ ___carEndpoint_registerForHTTPProxy_block_invoke.cold.1
+ ___carEndpoint_registerForHTTPProxy_block_invoke.cold.2
+ ___carEndpoint_registerForHTTPProxy_block_invoke.cold.3
+ ___carEndpoint_registerForHTTPProxy_block_invoke_2
+ ___carEndpoint_runTestCommand_block_invoke
+ ___carEndpoint_updateActiveStreamConnectionIDs_block_invoke
+ ___carEndpoint_updateVideoPlaybackAllowed_block_invoke
+ ___carManager_updateCurrentEndpoint_block_invoke.256
+ ___demoManagerGetModelSpecificName_block_invoke
+ ___emp_copyAvailableEndpoints_block_invoke
+ ___emp_evictAllCachedEndpoints_block_invoke
+ ___emp_getCachePromotionDeadlineDuration_block_invoke
+ ___emp_getCachePromotionDeadlineDuration_block_invoke.cold.1
+ ___emp_handleNotification_block_invoke
+ ___emp_handleNotification_block_invoke.cold.1
+ ___emp_handleNotification_block_invoke.cold.10
+ ___emp_handleNotification_block_invoke.cold.11
+ ___emp_handleNotification_block_invoke.cold.12
+ ___emp_handleNotification_block_invoke.cold.13
+ ___emp_handleNotification_block_invoke.cold.14
+ ___emp_handleNotification_block_invoke.cold.2
+ ___emp_handleNotification_block_invoke.cold.3
+ ___emp_handleNotification_block_invoke.cold.4
+ ___emp_handleNotification_block_invoke.cold.5
+ ___emp_handleNotification_block_invoke.cold.6
+ ___emp_handleNotification_block_invoke.cold.7
+ ___emp_handleNotification_block_invoke.cold.8
+ ___emp_handleNotification_block_invoke.cold.9
+ ___emp_introspector_copyDescription_block_invoke
+ ___emp_postDelayedAvailableEndpointsChanged_block_invoke
+ ___emp_postNotification_block_invoke
+ ___emp_postNotification_block_invoke.cold.1
+ ___emp_postNotification_block_invoke.cold.2
+ ___emp_restartCachePromotionDeadlineIfNecessary_block_invoke
+ ___emp_restartCachePromotionDeadlineIfNecessary_block_invoke.cold.1
+ ___emp_setupCache_block_invoke
+ ___emp_setupCache_block_invoke.cold.1
+ ___emp_setupCache_block_invoke.cold.2
+ ___emp_setupCache_block_invoke.cold.3
+ ___emp_setupCache_block_invoke.cold.4
+ ___emp_setupCache_block_invoke.cold.5
+ ___emp_setupCache_block_invoke.cold.6
+ ___emp_setupCache_block_invoke_2
+ ___emp_setupCache_block_invoke_2.cold.1
+ ___emp_setupCache_block_invoke_3
+ ___emp_shouldAllowCacheableType_block_invoke
+ ___endpointUGLWrapper_copyActivatedShadowEndpoints_block_invoke
+ ___endpointUGLWrapper_copySortedShadowEndpoints_block_invoke
+ ___endpointUGLWrapper_copySortedShadowEndpoints_block_invoke.cold.1
+ ___endpointUGLWrapper_deactivateInternal_block_invoke
+ ___endpoint_createHandleNANAuthorizationRequestBlockWrapper_block_invoke
+ ___endpoint_createSetAuthorizationStringBlockWrapper_block_invoke
+ ___endpoint_createSetAuthorizationStringBlockWrapper_block_invoke.cold.1
+ ___endpoint_createSetAuthorizationStringBlockWrapper_block_invoke.cold.2
+ ___endpoint_handleAuthorizationRequired_block_invoke
+ ___epp_activationCallback_block_invoke
+ ___epp_completionCallback_block_invoke
+ ___epp_getClusterDescriptionKeyMap_block_invoke
+ ___epp_getDescriptionKeyMap_block_invoke
+ ___epp_postNotificationAsync_block_invoke
+ ___epp_postNotificationAsync_block_invoke.cold.1
+ ___epp_sendCommandCallback_block_invoke
+ ___epp_sendDataCallback_block_invoke
+ ___getCRFetchScaledDisplaysForCertificateSerialNumberSymbolLoc_block_invoke
+ ___kCFBooleanTrue
+ ___manager_createEndpoint_block_invoke
+ ___manager_createEndpoint_block_invoke.cold.1
+ ___manager_createEndpoint_block_invoke.cold.2
+ ___manager_create_block_invoke_2.cold.1
+ ___manager_create_block_invoke_5
+ ___manager_create_block_invoke_5.cold.1
+ ___multicastProbeSender_GetClassID_block_invoke
+ ___multicastProbeSender_clearSocketList_block_invoke
+ ___multicastProbeSender_updateTxProbePacketsForClients_block_invoke
+ ___screenstreamudp_Control_block_invoke.cold.12
+ ___screenstreamudp_Control_block_invoke.cold.13
+ ___session_handleMetadataEvent_block_invoke_2
+ ___session_handleMetadataEvent_block_invoke_2.cold.1
+ ___shouldDumpCryptorAuxData_block_invoke
+ ___spendpoint_resetActivationState_block_invoke
+ ___uglWrapper_createNetworkAddressesArray_block_invoke
+ ___uglWrapper_createNetworkAddressesArray_block_invoke.cold.1
+ ___uglWrapper_handleFailedInternal_block_invoke
+ ___uglWrapper_handleFailedInternal_block_invoke.cold.1
+ _airPlayDescriptionMock_CopyFeatures
+ _airPlayDescriptionMock_CopyProperty
+ _airPlayDescriptionMock_Finalize
+ _airPlayDescriptionMock_HasFeature
+ _airPlayDescription_SetEndpointInfo.cold.11
+ _airPlayDescription_copyCarPlayVideoFeaturesInternal
+ _airPlayDescription_copyVolumeControlTypeEx.cold.2
+ _airPlayDescription_hasCarPlayVideoFeatureInternal
+ _airPlayDescription_hasCarPlayVideoFeatureInternal.cold.1
+ _airPlayDescription_updateWithAdvertiserAndPSGInfosNotifyingClients.cold.1
+ _airPlayDescription_updateWithAdvertiserAndPSGInfosNotifyingClients.cold.2
+ _airplayDescription_copySupportsSharedReceiverClock
+ _airplayDescription_supportsAnyMedia
+ _apPlayback_BroadcastCoordinatedPlaybackState
+ _apPlayback_BroadcastCoordinatedPlaybackState.cold.1
+ _apPlayback_CopyProperty.cold.2
+ _apsession_SetProperty.cold.10
+ _apsession_SetProperty.cold.11
+ _apsession_SetProperty.cold.8
+ _apsession_SetProperty.cold.9
+ _apsession_appendControlSetupRequest.cold.12
+ _apsession_appendControlSetupRequest.cold.13
+ _apsession_broadcastKeysForDiagnosticsDataInternal.cold.20
+ _apsession_ensureUsableLocalNetworkAddresses
+ _apsession_isClusterSession
+ _apsession_isClusterSession.cold.1
+ _apsession_isTightSyncBuddyConnection
+ _apsession_isTightSyncBuddyConnection.cold.1
+ _apsession_supportsLowLatencyNAN
+ _audioEngineBufferedAdapter_CompressionSourceWriteDataCallback
+ _audioEngineBufferedAdapter_CopyDebugDescription
+ _audioEngineBufferedAdapter_CopyProperty
+ _audioEngineBufferedAdapter_CopyProperty.cold.1
+ _audioEngineBufferedAdapter_CopyProperty.cold.2
+ _audioEngineBufferedAdapter_CopyProperty.cold.3
+ _audioEngineBufferedAdapter_CopyPropertyInternal
+ _audioEngineBufferedAdapter_CopyPropertyInternal.cold.1
+ _audioEngineBufferedAdapter_CopyPropertyInternal.cold.2
+ _audioEngineBufferedAdapter_CopyPropertyInternal.cold.3
+ _audioEngineBufferedAdapter_CopyPropertyInternal.cold.4
+ _audioEngineBufferedAdapter_CopyPropertyInternal.cold.5
+ _audioEngineBufferedAdapter_Finalize
+ _audioEngineBufferedAdapter_Finalize.cold.1
+ _audioEngineBufferedAdapter_Flush
+ _audioEngineBufferedAdapter_FlushData
+ _audioEngineBufferedAdapter_FlushData.cold.1
+ _audioEngineBufferedAdapter_FlushData.cold.2
+ _audioEngineBufferedAdapter_FlushData.cold.3
+ _audioEngineBufferedAdapter_FlushData.cold.4
+ _audioEngineBufferedAdapter_Resume
+ _audioEngineBufferedAdapter_Resume.cold.1
+ _audioEngineBufferedAdapter_Resume.cold.2
+ _audioEngineBufferedAdapter_Resume.cold.3
+ _audioEngineBufferedAdapter_ResumeComplete
+ _audioEngineBufferedAdapter_ResumeInternal
+ _audioEngineBufferedAdapter_SendData
+ _audioEngineBufferedAdapter_SetEndpointStream
+ _audioEngineBufferedAdapter_SetEndpointStream.cold.1
+ _audioEngineBufferedAdapter_SetEndpointStream.cold.2
+ _audioEngineBufferedAdapter_SetEndpointStreamComplete
+ _audioEngineBufferedAdapter_SetEndpointStreamComplete.cold.1
+ _audioEngineBufferedAdapter_SetEndpointStreamInternal
+ _audioEngineBufferedAdapter_SetEndpointStreamInternal.cold.1
+ _audioEngineBufferedAdapter_SetProperty
+ _audioEngineBufferedAdapter_SetProperty.cold.1
+ _audioEngineBufferedAdapter_SetProperty.cold.2
+ _audioEngineBufferedAdapter_SetProperty.cold.3
+ _audioEngineBufferedAdapter_Suspend
+ _audioEngineBufferedAdapter_Suspend.cold.1
+ _audioEngineBufferedAdapter_Suspend.cold.2
+ _audioEngineBufferedAdapter_Suspend.cold.3
+ _audioEngineBufferedAdapter_SuspendComplete
+ _audioEngineBufferedAdapter_SuspendInternal
+ _audioEngineBufferedAdapter_SuspendInternal_Guts
+ _audioStream_SetProperty.cold.7
+ _audioStream_audioDataBatchCallback.cold.4
+ _audioStream_audioDataBatchCallback.cold.5
+ _audioStream_audioDataBatchCallback.cold.6
+ _audioStream_audioDataCallback.cold.4
+ _audioStream_audioDataCallback.cold.5
+ _audioStream_audioDataCallback.cold.6
+ _audioStream_dataHoseAPATSetRTCPCallbacks
+ _audioStream_dataHoseAPATSetRTPCallbacks
+ _audioStream_dataHoseAPATSignalRTCPDataAvailable
+ _audioStream_dataHoseAPATSignalRTCPDataAvailable.cold.1
+ _audioStream_dataHoseAPATSignalRTPDataAvailable
+ _audioStream_dataHoseAPATSignalRTPDataAvailable.cold.1
+ _audioStream_dataHoseGetLastSentMediaTime
+ _audioStream_dataHoseGetLastSentMediaTime.cold.1
+ _audioStream_dataHoseSetLastSentMediaTime
+ _audioStream_protocolDriverHoseApplyVolumeFade
+ _audioStream_protocolDriverHoseControlProtocolCopyDebugDescription
+ _audioStream_protocolDriverHoseDataAPATProtocolCopyDebugDescription
+ _audioStream_protocolDriverHoseDataBaseProtocolCopyDebugDescription
+ _audioStream_protocolDriverHoseEnableLoudnessNormalization
+ _audioStream_protocolDriverHoseEnableMATAtmosPlayback
+ _audioStream_protocolDriverHoseGetAnchor
+ _audioStream_protocolDriverHoseLegacyFlush
+ _audioStream_protocolDriverHoseLegacyFlushWithinSampleRange
+ _audioStream_protocolDriverHoseSetCryptor
+ _audioStream_protocolDriverHoseSetMagicCookie
+ _audioStream_protocolDriverHoseSetRate
+ _audioStream_protocolDriverHoseSetRateAndAnchorTime
+ _audioStream_receivedAudioDataMessage.cold.2
+ _audioStream_receivedAudioDataMessage.cold.3
+ _audioStream_receivedAudioDataMessage.cold.4
+ _audioStream_receivedMediaDataEventMessage
+ _audioStream_receivedMediaDataEventMessage.cold.1
+ _audioStream_receivedMediaDataEventMessage.cold.10
+ _audioStream_receivedMediaDataEventMessage.cold.11
+ _audioStream_receivedMediaDataEventMessage.cold.12
+ _audioStream_receivedMediaDataEventMessage.cold.13
+ _audioStream_receivedMediaDataEventMessage.cold.14
+ _audioStream_receivedMediaDataEventMessage.cold.15
+ _audioStream_receivedMediaDataEventMessage.cold.16
+ _audioStream_receivedMediaDataEventMessage.cold.17
+ _audioStream_receivedMediaDataEventMessage.cold.18
+ _audioStream_receivedMediaDataEventMessage.cold.2
+ _audioStream_receivedMediaDataEventMessage.cold.3
+ _audioStream_receivedMediaDataEventMessage.cold.4
+ _audioStream_receivedMediaDataEventMessage.cold.5
+ _audioStream_receivedMediaDataEventMessage.cold.6
+ _audioStream_receivedMediaDataEventMessage.cold.7
+ _audioStream_receivedMediaDataEventMessage.cold.8
+ _audioStream_receivedMediaDataEventMessage.cold.9
+ _browserController_registerInternalClientNeedsDiscovery
+ _browserController_registerInternalClientNeedsDiscovery.cold.1
+ _bufferedAudioEngine_addHose
+ _bufferedAudioEngine_addHose.cold.1
+ _bufferedAudioEngine_addHose.cold.2
+ _bufferedAudioEngine_addHose.cold.3
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHose
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal.cold.1
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal.cold.2
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal.cold.3
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal.cold.4
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacy
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacyInternal
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacyInternal.cold.1
+ _bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacyInternal.cold.2
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHose
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.1
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.10
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.11
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.12
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.13
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.14
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.15
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.16
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.2
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.3
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.4
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.5
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.6
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.7
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.8
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal.cold.9
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacy
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacy.callbacks
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.1
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.2
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.3
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.4
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.5
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.6
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.7
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.8
+ _bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal.cold.9
+ _bufferedAudioEngine_audioHoseSetEchoCancellationIfNeccessary
+ _bufferedAudioEngine_copyAudioDataBBufDispatchInternal.cold.10
+ _bufferedAudioEngine_copyAudioDataBBufDispatchInternal.cold.11
+ _bufferedAudioEngine_copyAudioDataBBufDispatchInternal.cold.12
+ _bufferedAudioEngine_copyPropertyDispatch.cold.11
+ _bufferedAudioEngine_copyPropertyDispatch.cold.12
+ _bufferedAudioEngine_destroyProtocolDriverTickTimer
+ _bufferedAudioEngine_flushHose
+ _bufferedAudioEngine_flushHose.cold.1
+ _bufferedAudioEngine_flushHoseWithinSampleRange
+ _bufferedAudioEngine_flushHoseWithinSampleRange.cold.1
+ _bufferedAudioEngine_generateNewFirstRemoteMediaTime.cold.3
+ _bufferedAudioEngine_getFirstValidBufferTimestamp
+ _bufferedAudioEngine_getFirstValidBufferTimestamp.cold.1
+ _bufferedAudioEngine_getLastDeliveredRemoteMediaTimeForHose.cold.5
+ _bufferedAudioEngine_getLastSentRemoteMediaTimeForHose
+ _bufferedAudioEngine_getSentBufferLevelTime
+ _bufferedAudioEngine_initProtocolDriverIfNecessary
+ _bufferedAudioEngine_isHoseLocal
+ _bufferedAudioEngine_logBufferFullness
+ _bufferedAudioEngine_logForSendRate.cold.1
+ _bufferedAudioEngine_logProtocolDriverBufferFullness
+ _bufferedAudioEngine_protocolDriverDescriptorDictionaryCallbacks
+ _bufferedAudioEngine_protocolDriverDescriptorDictionaryRelease
+ _bufferedAudioEngine_protocolDriverDescriptorDictionaryRelease.cold.1
+ _bufferedAudioEngine_protocolDriverDescriptorDictionaryRetain
+ _bufferedAudioEngine_protocolDriverDescriptorDictionaryRetain.cold.1
+ _bufferedAudioEngine_resumeInternalStage1.cold.33
+ _bufferedAudioEngine_resumeInternalStage1.cold.34
+ _bufferedAudioEngine_resumeInternalStage1.cold.35
+ _bufferedAudioEngine_resumeInternalStage1.cold.36
+ _bufferedAudioEngine_resumeInternalStage1.cold.37
+ _bufferedAudioEngine_resumeInternalStage1.cold.38
+ _bufferedAudioEngine_resumeInternalStage1.cold.39
+ _bufferedAudioEngine_resumeInternalStage1.cold.40
+ _bufferedAudioEngine_resumeInternalStage1.cold.41
+ _bufferedAudioEngine_resumeInternalStage1.cold.42
+ _bufferedAudioEngine_resumeInternalStage1.cold.43
+ _bufferedAudioEngine_resumeInternalStage1.cold.44
+ _bufferedAudioEngine_setAllCryptorsForHose
+ _bufferedAudioEngine_setAllMagicCookiesForHose
+ _bufferedAudioEngine_setEndpointStreamInternalStage5.cold.4
+ _bufferedAudioEngine_updateStartupConfiguration
+ _bufferedAudioEngine_updateStartupConfiguration.cold.1
+ _bufferedAudioEngine_weakProtocolDriverTickTimer
+ _bufferedAudioEngine_weakProtocolDriverTickTimer.cold.1
+ _bufferedAudioEngine_weakProtocolDriverTickTimer.cold.2
+ _carEndpoint_CopyProperty.cold.21
+ _carEndpoint_CopyProperty.cold.22
+ _carEndpoint_CopyProperty.cold.23
+ _carEndpoint_CreatePlaybackSession
+ _carEndpoint_CreateRemoteControlSession.cold.8
+ _carEndpoint_CreateRemoteControlSession.cold.9
+ _carEndpoint_SendCommand.cold.7
+ _carEndpoint_SendCommand.cold.8
+ _carEndpoint_SendCommand.cold.9
+ _carEndpoint_UpdateFeaturesWithCompletionCallback
+ _carEndpoint_UpdateFeaturesWithCompletionCallback.cold.1
+ _carEndpoint_handlePlaybackSessionInvalidated
+ _carEndpoint_handlePlaybackSessionRemove
+ _carEndpoint_handleRemoteControlSessionEvent.cold.3
+ _carEndpoint_setupStreams.cold.46
+ _carEndpoint_setupStreams.cold.47
+ _carEndpoint_setupStreams.cold.48
+ _carEndpoint_setupStreams.cold.49
+ _carEndpoint_updateActiveStreamConnectionIDs
+ _carEndpoint_updateVideoPlaybackAllowed
+ _conduitsource_WriteDataInternal.cold.2
+ _connect
+ _demoManagerActivateEndpointIfNeeded.cold.12
+ _demoManagerGetModelSpecificName.once
+ _demoManagerGetModelSpecificName.sModelNameStr
+ _dispatch_activate
+ _emp_CopyProperty
+ _emp_CopyProperty.cold.1
+ _emp_CopyProperty.cold.2
+ _emp_CopyRemoteControlDepotEndpoint
+ _emp_CopyRemoteControlDepotEndpoint.cold.1
+ _emp_CreateAggregateEndpoint
+ _emp_DumpHierarchy
+ _emp_Finalize
+ _emp_Finalize.cold.1
+ _emp_Invalidate
+ _emp_Invalidate.cold.1
+ _emp_Invalidate.cold.2
+ _emp_SetDiscoveryMode
+ _emp_SetProperty
+ _emp_addEndpoint
+ _emp_copyAvailableEndpoints
+ _emp_ensureCachedEndpointWithType
+ _emp_evictCachedEndpoint
+ _emp_forEachEndpoint
+ _emp_getCachePromotionDeadlineDuration.onceToken
+ _emp_handleEndpointWantsCacheEviction
+ _emp_handleNotification
+ _emp_introspector_copyDescription
+ _emp_introspector_showManagerPlus
+ _emp_isEndpointCacheable
+ _emp_isEndpointCacheable.cold.1
+ _emp_postDelayedAvailableEndpointsChanged
+ _emp_postNotification
+ _emp_removeCachedEndpointWithType
+ _emp_removeCachedEndpointWithType.cold.1
+ _emp_removeCachedEndpointWithType.cold.2
+ _emp_removeCachedEndpointWithType.cold.3
+ _emp_removeEndpoint
+ _emp_reportEndpointToCache
+ _emp_restartCachePromotionDeadlineIfNecessary
+ _emp_shouldAllowCacheableType
+ _emp_shouldAllowCacheableType.allowAirPlay
+ _emp_shouldAllowCacheableType.allowCluster
+ _emp_shouldAllowCacheableType.allowRemoteControl
+ _emp_shouldAllowCacheableType.cold.1
+ _emp_shouldAllowCacheableType.onceToken
+ _emp_syncSubEndpoints_createTable
+ _emp_syncSubEndpoints_createTable.cold.1
+ _endpointAggregate_copyActivationOptionsToStorage.cold.5
+ _endpointAggregate_isUpdateUGLRCServerNeeded
+ _endpointUGLWrapper_activateInternal
+ _endpointUGLWrapper_activateInternal.cold.1
+ _endpointUGLWrapper_activateInternal.cold.2
+ _endpointUGLWrapper_activateInternal.cold.3
+ _endpointUGLWrapper_addRCShadowListeners
+ _endpointUGLWrapper_checkForUGLServerInfo
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.1
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.2
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.3
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.4
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.5
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.6
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.7
+ _endpointUGLWrapper_checkForUGLServerInfo.cold.8
+ _endpointUGLWrapper_copyWrappedEndpoint
+ _endpointUGLWrapper_createMXDescriptor
+ _endpointUGLWrapper_createMXDescriptor.cold.1
+ _endpointUGLWrapper_deactivateInternal
+ _endpointUGLWrapper_deactivateInternal.cold.1
+ _endpointUGLWrapper_deactivateInternal.cold.2
+ _endpointUGLWrapper_getActivationSeed
+ _endpointUGLWrapper_handleRCEndpointDescriptionChanged
+ _endpointUGLWrapper_handleWrappedNotification
+ _endpointUGLWrapper_setWrappedEndpoint
+ _endpointUGLWrapper_updateMXDescriptor
+ _endpointUGLWrapper_updateMXDescriptor.cold.1
+ _endpoint_authorizationRequestCompletionCallback
+ _endpoint_authorizationRequestCompletionCallback.cold.1
+ _endpoint_authorizationRequestCompletionCallback.cold.2
+ _endpoint_copyExternalPlaybackCompetingStreams
+ _endpoint_copyExternalPlaybackCompetingStreams.cold.1
+ _endpoint_copyUsesExternalPlaybackByDefault
+ _endpoint_copyUsesExternalPlaybackByDefault.cold.1
+ _endpoint_deactivateInternal.cold.10
+ _endpoint_deactivateInternal.cold.11
+ _endpoint_deactivateInternal.cold.8
+ _endpoint_deactivateInternal.cold.9
+ _endpoint_handleAuthorizationRequired
+ _endpoint_handleAuthorizationRequired.cold.1
+ _endpoint_handleAuthorizationRequired.cold.10
+ _endpoint_handleAuthorizationRequired.cold.11
+ _endpoint_handleAuthorizationRequired.cold.12
+ _endpoint_handleAuthorizationRequired.cold.13
+ _endpoint_handleAuthorizationRequired.cold.2
+ _endpoint_handleAuthorizationRequired.cold.3
+ _endpoint_handleAuthorizationRequired.cold.4
+ _endpoint_handleAuthorizationRequired.cold.5
+ _endpoint_handleAuthorizationRequired.cold.6
+ _endpoint_handleAuthorizationRequired.cold.7
+ _endpoint_handleAuthorizationRequired.cold.8
+ _endpoint_handleAuthorizationRequired.cold.9
+ _endpoint_handleEventMessageCreatingReply.cold.19
+ _endpoint_handleUpdateMC2UCStatus
+ _endpoint_isInLocalStereoPair
+ _endpoint_updateUGLRCServerIfNeeded
+ _epp_AcquireAndCopyResource
+ _epp_AcquireAndCopyResource.cold.1
+ _epp_AcquireAndCopyResource.cold.2
+ _epp_ActivateForFeaturesWithCompletionCallback
+ _epp_ActivateForFeaturesWithCompletionCallback.cold.1
+ _epp_ActivateForFeaturesWithCompletionCallback.cold.2
+ _epp_BorrowScreen
+ _epp_BorrowScreen.cold.1
+ _epp_BorrowScreen.cold.2
+ _epp_CloseAllCommChannels
+ _epp_CloseCommChannel
+ _epp_CloseCommChannel.cold.1
+ _epp_CloseCommChannel.cold.2
+ _epp_CopyCurrentViewArea
+ _epp_CopyCurrentViewArea.cold.1
+ _epp_CopyCurrentViewArea.cold.2
+ _epp_CopyDebugDescription
+ _epp_CopyHIDInputMode
+ _epp_CopyHIDInputMode.cold.1
+ _epp_CopyHIDInputMode.cold.2
+ _epp_CopyProperty
+ _epp_CopyProperty.cold.1
+ _epp_CopyProperty.cold.2
+ _epp_CopyProperty.cold.3
+ _epp_CreateCommChannel
+ _epp_CreateCommChannel.cold.1
+ _epp_CreateCommChannel.cold.2
+ _epp_CreatePlaybackSession
+ _epp_CreatePlaybackSession.cold.1
+ _epp_CreatePlaybackSession.cold.2
+ _epp_CreateRemoteControlSession
+ _epp_CreateRemoteControlSession.cold.1
+ _epp_CreateRemoteControlSession.cold.2
+ _epp_DeactivateWithCompletionCallback
+ _epp_DeactivateWithCompletionCallback.cold.1
+ _epp_DeactivateWithCompletionCallback.cold.2
+ _epp_DisableBluetooth
+ _epp_DisableBluetooth.cold.1
+ _epp_DisableBluetooth.cold.2
+ _epp_Dissociate
+ _epp_Dissociate.cold.1
+ _epp_DuckAudio
+ _epp_DuckAudio.cold.1
+ _epp_DuckAudio.cold.2
+ _epp_DumpHierarchy
+ _epp_EnsureAuthorizedWithCompletionCallback
+ _epp_EnsureAuthorizedWithCompletionCallback.cold.1
+ _epp_Finalize
+ _epp_Finalize.cold.1
+ _epp_RelinquishResource
+ _epp_RelinquishResource.cold.1
+ _epp_RelinquishResource.cold.2
+ _epp_RequestCarUI
+ _epp_RequestCarUI.cold.1
+ _epp_RequestCarUI.cold.2
+ _epp_RequestViewArea
+ _epp_RequestViewArea.cold.1
+ _epp_RequestViewArea.cold.2
+ _epp_SendCommand
+ _epp_SendCommand.cold.1
+ _epp_SendCommand.cold.2
+ _epp_SendData
+ _epp_SendData.cold.1
+ _epp_SetDelegate
+ _epp_SetDelegateRemoteControl
+ _epp_SetDelegateRouting
+ _epp_SetDelegateVolumeAndMute
+ _epp_SetHIDInputMode
+ _epp_SetHIDInputMode.cold.1
+ _epp_SetHIDInputMode.cold.2
+ _epp_SetProperty
+ _epp_SetProperty.cold.1
+ _epp_TakeScreen
+ _epp_TakeScreen.cold.1
+ _epp_TakeScreen.cold.2
+ _epp_UnborrowScreen
+ _epp_UnborrowScreen.cold.1
+ _epp_UnborrowScreen.cold.2
+ _epp_UpdateFeaturesWithCompletionCallback
+ _epp_UpdateFeaturesWithCompletionCallback.cold.1
+ _epp_UpdateFeaturesWithCompletionCallback.cold.2
+ _epp_activationCallback
+ _epp_completionCallback
+ _epp_copyCachedClusterProperty
+ _epp_copyCachedClusterProperty.cold.1
+ _epp_copyCachedClusterProperty.cold.10
+ _epp_copyCachedClusterProperty.cold.2
+ _epp_copyCachedClusterProperty.cold.3
+ _epp_copyCachedClusterProperty.cold.4
+ _epp_copyCachedClusterProperty.cold.5
+ _epp_copyCachedClusterProperty.cold.6
+ _epp_copyCachedClusterProperty.cold.7
+ _epp_copyCachedClusterProperty.cold.8
+ _epp_copyCachedClusterProperty.cold.9
+ _epp_copyCachedDescriptionProperty
+ _epp_copyCachedDescriptionProperty.cold.1
+ _epp_copyCachedDescriptionProperty.cold.2
+ _epp_copyCachedDescriptionProperty.cold.3
+ _epp_copyCachedDescriptionProperty.cold.4
+ _epp_copyCachedDescriptionProperty.cold.5
+ _epp_copyCachedDescriptionProperty.cold.6
+ _epp_copyCachedDescriptionProperty.cold.7
+ _epp_copyCachedDescriptionProperty.cold.8
+ _epp_copyCachedProperty
+ _epp_copyCachedProperty.cold.1
+ _epp_copyCachedProperty.cold.2
+ _epp_copyCachedProperty.cold.3
+ _epp_copyCachedProperty.cold.4
+ _epp_copyEndpointPropertyToDestination
+ _epp_copyEndpointPropertyToDestination.cold.1
+ _epp_copyEndpointPropertyToDestination.cold.2
+ _epp_copyEndpointPropertyToDestination.cold.3
+ _epp_copyInner
+ _epp_copyInnerExtended
+ _epp_copySubEndpoint
+ _epp_copySubEndpoint.cold.1
+ _epp_copySubEndpoint.cold.2
+ _epp_copySubEndpoint.cold.3
+ _epp_copySubEndpoint.cold.4
+ _epp_copySubEndpointsArray
+ _epp_copySubEndpointsArray.cold.1
+ _epp_copySubEndpointsArray.cold.2
+ _epp_copySubEndpointsArray.cold.3
+ _epp_copySubEndpointsArray.cold.4
+ _epp_delegate_handleAuthRequired
+ _epp_delegate_handleAuthRequired.cold.1
+ _epp_delegate_handleAuthRequired.cold.10
+ _epp_delegate_handleAuthRequired.cold.2
+ _epp_delegate_handleAuthRequired.cold.3
+ _epp_delegate_handleAuthRequired.cold.4
+ _epp_delegate_handleAuthRequired.cold.5
+ _epp_delegate_handleAuthRequired.cold.6
+ _epp_delegate_handleAuthRequired.cold.7
+ _epp_delegate_handleAuthRequired.cold.8
+ _epp_delegate_handleAuthRequired.cold.9
+ _epp_delegate_handleAuthRequiredCallback
+ _epp_delegate_handleAuthRequiredCallback.cold.1
+ _epp_delegate_handleConnectedStateChanged
+ _epp_delegate_handleConnectedStateChanged.cold.1
+ _epp_delegate_handleConnectedStateChanged.cold.2
+ _epp_delegate_handleConnectedStateChanged.cold.3
+ _epp_delegate_handleCopyProperty
+ _epp_delegate_handleCopyProperty.cold.1
+ _epp_delegate_handleCopyProperty.cold.2
+ _epp_delegate_handleCopyProperty.cold.3
+ _epp_delegate_handleDidCloseCommChannel
+ _epp_delegate_handleDidCloseCommChannel.cold.1
+ _epp_delegate_handleDidCloseCommChannel.cold.2
+ _epp_delegate_handleDidCloseCommChannel.cold.3
+ _epp_delegate_handleDidReceiveDataFromCommChannel
+ _epp_delegate_handleDidReceiveDataFromCommChannel.cold.1
+ _epp_delegate_handleDidReceiveDataFromCommChannel.cold.2
+ _epp_delegate_handleDidReceiveDataFromCommChannel.cold.3
+ _epp_delegate_handleFailed
+ _epp_delegate_handleFailed.cold.1
+ _epp_delegate_handleFailed.cold.2
+ _epp_delegate_handleFailed.cold.3
+ _epp_delegate_handleIncomingRemoteControlSessionCreated
+ _epp_delegate_handleIncomingRemoteControlSessionCreated.cold.1
+ _epp_delegate_handleIncomingRemoteControlSessionCreated.cold.2
+ _epp_delegate_handleIncomingRemoteControlSessionCreated.cold.3
+ _epp_delegate_handleSetProperty
+ _epp_delegate_handleSetProperty.cold.1
+ _epp_delegate_handleSetProperty.cold.2
+ _epp_delegate_handleSetProperty.cold.3
+ _epp_delegate_handleStreamsChanged
+ _epp_delegate_handleStreamsChanged.cold.1
+ _epp_delegate_handleStreamsChanged.cold.2
+ _epp_delegate_handleStreamsChanged.cold.3
+ _epp_getCachedClusterSupportedFeatures
+ _epp_getCachedClusterSupportedFeatures.cold.1
+ _epp_getClusterDescriptionKeyMap.keyMap
+ _epp_getClusterDescriptionKeyMap.onceToken
+ _epp_getClusterLeaderOrAny
+ _epp_getDescriptionKeyMap.keyMap
+ _epp_getDescriptionKeyMap.onceToken
+ _epp_handleInnerNotification
+ _epp_handleInnerNotification.cold.1
+ _epp_postNotificationAsync
+ _epp_removeInnerListeners
+ _epp_sendCommandCallback
+ _epp_sendDataCallback
+ _epp_updateDelegateRemoteControl
+ _epp_updateDelegateRouting
+ _epp_updateDescription
+ _epp_updateDescription.cold.1
+ _epp_updateDescription.cold.2
+ _epp_updateDescriptionFromEndpoint
+ _epp_updateDescriptionFromEndpoint.cold.1
+ _epp_updateDescriptionFromEndpoint.cold.2
+ _epp_updateDescriptionFromInner
+ _fig_log_get_emitter
+ _gLogCategory_APAudioEngineBufferedAdapter
+ _gLogCategory_APEndpointPlus
+ _gLogCategory_APEndpointUGLWrapper
+ _gLogCategory_APHTTPProxyMonitorClient
+ _gLogCategory_APMulticastProbeSender
+ _getCRFetchScaledDisplaysForCertificateSerialNumberSymbolLoc.ptr
+ _getsockname
+ _if_nametoindex
+ _introspector_getCollectionOfActiveCarPlayEndpoints.coll
+ _introspector_getCollectionOfActiveCarPlayEndpoints.once
+ _kAPAudioEngineBufferedAdapterVTable
+ _kAPAudioEngineBufferedAdapter_APAudioEngineClass
+ _kAPAudioEngineBufferedAdapter_BaseClassWrapper
+ _kAPBrowserControllerCreationOption_OpenNANAllowed
+ _kAPBrowserCreationOption_OpenNANAllowed
+ _kAPEndpointActivationOptionKey_IsUGLRCServerUpdateNeeded
+ _kAPEndpointCreationOption_UGLRCServerUpdateCallback
+ _kAPEndpointDescriptionMockVTable
+ _kAPEndpointDescriptionMock_BaseClassWrapper
+ _kAPEndpointDescriptionNotificationPayloadKey_UGLServerInfoAdded
+ _kAPEndpointDescriptionNotificationPayloadKey_UGLSessionActiveDidChange
+ _kAPEndpointDescriptionProperty_ForwardCryptorSubsampleAuxData
+ _kAPEndpointDescriptionProperty_ForwardFrameUserData
+ _kAPEndpointDescriptionProperty_IsThirdPartyReceiver
+ _kAPEndpointDescriptionProperty_IsUGLReceiverSessionActive
+ _kAPEndpointDescriptionProperty_SupportsAnyMedia
+ _kAPEndpointDescriptionProperty_SupportsBufferedAPAT
+ _kAPEndpointDescriptionProperty_SupportsSharedReceiverClock
+ _kAPEndpointDescriptionProperty_SupportsUGLAssistedDiscovery
+ _kAPEndpointDescriptionProperty_UGLServerInfo
+ _kAPEndpointDescription_APEndpointDescriptionMockClass
+ _kAPEndpointDisplayDescriptionProperty_ZoomFactor
+ _kAPEndpointManagerPlusClass
+ _kAPEndpointManagerPlusVTable
+ _kAPEndpointManagerPlus_BaseClass
+ _kAPEndpointNotificationPayloadKey_UGLServerInfoAdded
+ _kAPEndpointNotificationPayloadKey_UGLSessionActiveDidChange
+ _kAPEndpointPlaybackSessionCreationOptionKey_SupportsV2ArtworkMetadata
+ _kAPEndpointPlusClass
+ _kAPEndpointPlusExtendedClass
+ _kAPEndpointPlusVTable
+ _kAPEndpointPlus_BaseClass
+ _kAPEndpointPlus_EndpointHierarchyProtocol
+ _kAPEndpointPlus_EndpointHierarchyProtocolVTable
+ _kAPEndpointPlus_baseProtocol
+ _kAPEndpointPlus_protocolEntries
+ _kAPEndpointPlus_protocolTable
+ _kAPEndpointProperty_HALVolumeDB
+ _kAPEndpointProperty_SupportsAnyMedia
+ _kAPEndpointProperty_SupportsUGLAssistedDiscovery
+ _kAPEndpointSharedContextParsingAudioEngineOption_PerceivedClusterType
+ _kAPEndpointStreamAudioCreationOption_DisableRemoteAudioRender
+ _kAPEndpointStreamAudioEngineCreationOption_ClusterModel
+ _kAPEndpointStreamAudioEngineCreationOption_PerceivedClusterType
+ _kAPEndpointStreamAudioEngineCreationOption_SenderNetworkClock
+ _kAPEndpointStreamAudioEngineNotification_DynamicLatencyOffsetChanged
+ _kAPEndpointStreamAudioEngineProperty_DynamicLatencyOffsetMs
+ _kAPEndpointStreamAudioEngineProperty_StartupOptions
+ _kAPEndpointStreamBufferedAudioEngineCreationOption_ZeroFirstRemoteMediaTime
+ _kAPEndpointStreamBufferedAudioEngineNotificationPayloadKey_PlaybackStateType
+ _kAPEndpointStreamBufferedAudioEngineNotification_DiscontinuityFound
+ _kAPEndpointStreamBufferedAudioEngineNotification_PlaybackStateChanged
+ _kAPEndpointStreamBufferedAudioEngineProperty_CurrentPlaybackState
+ _kAPEndpointStreamBufferedAudioEngineProperty_NextRemoteMediaTimestamp
+ _kAPEndpointStreamBuffered_protocolDriverHoseControlProtocolProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseControlProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseControlProtocol_BaseProtocol
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataAPATProtocolProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataAPATProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataAPATProtocol_BaseProtocol
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataBaseProtocolProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataBaseProtocolVTable
+ _kAPEndpointStreamBuffered_protocolDriverHoseDataBaseProtocol_BaseProtocol
+ _kAPEndpointStreamConnectionType_APAT
+ _kAPEndpointStreamCreationOptionKey_OverrideCanvasSize
+ _kAPEndpointStreamProperty_SupportsAPAT
+ _kAPEndpointStreamProtectionOptionsKey_EncoderEncryptionKeyID
+ _kAPEndpointStreamResumeOption_ClientAuditToken
+ _kAPEndpointStreamResumeOption_PrefersAPAT
+ _kAPEndpointStreamResumeOption_UseAPAT
+ _kAPEndpointUGLWrapperClass
+ _kAPEndpointUGLWrapperVTable
+ _kAPEndpointUGLWrapper_BaseClass
+ _kAPHALAudioDeviceCreationOption_AudioStreamOverride
+ _kAPMulticastProbeSenderVTable
+ _kAPMulticastProbeSender_APMulticastProbeSenderClassWrapper
+ _kAPMulticastProbeSender_BaseClassWrapper
+ _kAPPairingClientHeader_NANMACAddress
+ _kAPPairingClientHeader_UsingNANDiversifiedPINAsSetupCode
+ _kAPSAudioPerformanceReportKey_LiveAdaptiveGlitchHistogram
+ _kAPSAudioProtocolDriverHoseProperty_AudioBufferSize
+ _kAPSAudioProtocolDriverHoseProperty_ClusterSize
+ _kAPSAudioProtocolDriverHoseProperty_ClusterType
+ _kAPSAudioProtocolDriverHoseProperty_ClusterUUID
+ _kAPSAudioProtocolDriverHoseProperty_DataPacer
+ _kAPSAudioProtocolDriverHoseProperty_EchoCancellationIsEnabled
+ _kAPSAudioProtocolDriverHoseProperty_HasAudioDataBeenSent
+ _kAPSAudioProtocolDriverHoseProperty_InputEncryptionKey
+ _kAPSAudioProtocolDriverHoseProperty_IsAppleTV
+ _kAPSAudioProtocolDriverHoseProperty_IsClusterLeader
+ _kAPSAudioProtocolDriverHoseProperty_IsCritical
+ _kAPSAudioProtocolDriverHoseProperty_IsDolbyCertified
+ _kAPSAudioProtocolDriverHoseProperty_IsTimelineEstablished
+ _kAPSAudioProtocolDriverHoseProperty_LastDeliveredAudioDataBBuf
+ _kAPSAudioProtocolDriverHoseProperty_Model
+ _kAPSAudioProtocolDriverHoseProperty_Name
+ _kAPSAudioProtocolDriverHoseProperty_OSBuildVersion
+ _kAPSAudioProtocolDriverHoseProperty_OutputEncryptionKey
+ _kAPSAudioProtocolDriverHoseProperty_SupportsReceiverChoosesAnchor
+ _kAPSAudioProtocolDriverHoseProperty_WASCalibrationSupportsMATAtmos
+ _kAPSAudioProtocolDriverSenderProperty_BufferFullnessBytes
+ _kAPSAudioProtocolDriverSenderProperty_BufferFullnessCount
+ _kAPSAudioProtocolDriverSenderProperty_FirstValidBufferTimestamp
+ _kAPSAudioProtocolDriverSenderProperty_OutputCryptorOverhead
+ _kAPSAudioProtocolDriverSenderProperty_PreferedTickIntervalMs
+ _kAPSAudioProtocolDriverSenderType_APAT
+ _kAPSAudioProtocolDriverSenderType_Local
+ _kAPSDynamicLatencyManagerPerformanceReportKey_IsLiveAdaptive
+ _kAPSDynamicLatencyManagerVariantIdentifier_ScreenDefault
+ _kAPSDynamicLatencyManagerVariantIdentifier_ScreenHigh
+ _kAPSDynamicLatencyManagerVariantIdentifier_ScreenHomeTheater
+ _kAPSDynamicLatencyManagerVariantIdentifier_ScreenLow
+ _kAPSEndpointStreamAudioHoseProtocolProperty_DataPacer
+ _kAPSEndpointStreamAudioHoseRegistrarProperty_UseProtocolDriverHoseInterface
+ _kAPSEndpointStreamAudioHoseSBARCreationOption_ClientAuditToken
+ _kAPSenderSessionActivationTimingInformationKey_NetworkingMs
+ _kAPSenderSessionActivationTimingInformationKey_ReceiverMessageProcessingMs
+ _kAPSenderSessionActivationTimingInformationKey_TimeToConnectMs
+ _kAPSenderSessionActivationTimingInformationKey_TotalMessageTimeMs
+ _kAPSenderSessionActivationTimingInformationKey_UnspecifiedRemoteTimeMs
+ _kAPSenderSessionProperty_ActivationTimingInformation
+ _kAPSenderSessionProperty_ActiveStreamConnectionIDs
+ _kAPSenderSessionProperty_MC2UCToken
+ _kAPSenderSessionProperty_NANMACAddress
+ _kAPSenderSessionProperty_PWDEncryptorEncryptionKeyID
+ _kAPSenderSessionProperty_RCServerInfo
+ _kAPSenderSessionProperty_ShouldUseNANDiversifiedPIN
+ _kAPSenderSessionTransportStreamOption_TransportProtocol
+ _kAPTransportSessionOption_HandleNANAuthorizationRequestBlock
+ _kAPTransportSessionOption_NANAuthorizationType
+ _kAPTransportSessionOption_SetNANAuthorizationStringBlock
+ _kAPTransportStreamProperty_DataPacer
+ _kAPTransportStreamProperty_TimingInformation
+ _kAirPlayReceiverServerOption_ForcedDisabledFeaturesMask
+ _kAirPlayReceiverServerOption_ReceiverAssistedMode
+ _kAirPlayReceiverServerOption_SupportsRemoteControl
+ _kAirPlayReceiverServerOption_UGLRCServerMode
+ _kAirPlayReceiverServerOption_UseDynamicPort
+ _kAirPlayReceiverServerOption_UsesHomeKitIntegration
+ _kCFCopyStringDictionaryKeyCallBacks
+ _kCMSampleAttachmentKey_CryptorSubsampleAuxiliaryData
+ _kFigEndpointActivateOptionKey_CorrelationID
+ _kFigEndpointDescriptorKey_IsCached
+ _kFigEndpointDescriptorKey_IsGroupable
+ _kFigEndpointExtendedRemoteUGLWrapperClass
+ _kFigEndpointManagerProperty_AvailableEndpointsExtended
+ _kFigEndpointPlaybackSessionBroadcastCoordinatedPlaybackStateKey_State
+ _kFigEndpointPlaybackSessionProperty_ClientPID
+ _kFigEndpointProperty_ExternalPlaybackCompetingStreams
+ _kFigEndpointProperty_IsCached
+ _kFigEndpointProperty_IsDissociated
+ _kFigEndpointProperty_UsesExternalPlaybackByDefault
+ _kFigEndpointRemoteControlSessionClientTypeUUIDKey_CarPlayVideoSettings
+ _kFigEndpointStreamAudioEngineSampleBufferAttachmentKey_FlushRangeEnd
+ _kFigPWDKeyExchangeSenderCreationOption_ProtectionOptions
+ _kFigPWDKeyExchangeSenderProperty_KeyID
+ _kFigRoutingContextSelectRouteOptionKey_ClientPID
+ _kFigVirtualDisplayOption_DefaultBitrate
+ _kFigVirtualDisplayOption_HDRToneMappingMode
+ _kFigVirtualDisplaySourceProperty_Type
+ _kSCNetworkInterfaceTypeIEEE80211
+ _kWHAPrimingConfig
+ _manager_create.cold.41
+ _manager_create.cold.42
+ _manager_create.cold.43
+ _manager_create.cold.44
+ _manager_create.cold.45
+ _manager_create.cold.46
+ _manager_createEndpoint
+ _manager_createEndpoint.cold.1
+ _manager_createEndpoint.cold.2
+ _manager_createEndpoint.cold.3
+ _manager_createUGLRCServer
+ _manager_handleBrowserAddOrUpdateEvent.cold.8
+ _manager_handleBrowserAddOrUpdateEvent.cold.9
+ _manager_handleShadowEndpointEvent
+ _manager_handleShadowEndpointEvent.cold.1
+ _manager_handleShadowEndpointEvent.cold.2
+ _manager_handleShadowEndpointEvent.cold.3
+ _manager_handleShadowEndpointEvent.cold.4
+ _manager_introspector_activateEndpoint
+ _manager_introspector_activateEndpoint.cold.1
+ _manager_introspector_deactivateEndpoint
+ _manager_introspector_deactivateEndpoint.cold.1
+ _manager_introspector_deactivateEndpoint.cold.2
+ _manager_introspector_printRWUsage
+ _manager_introspector_sendUGLreceiverCommand
+ _manager_introspector_sendUGLreceiverCommand.cold.1
+ _manager_introspector_setDiscoveryMode
+ _manager_introspector_setDiscoveryMode.cold.1
+ _manager_removeShadowEndpointFromUGLWrapper
+ _manager_removeUGLWrapperEndpointIfEmpty
+ _manager_removeUGLWrapperEndpointIfEmpty.cold.1
+ _manager_startOrStopUGLRCServer
+ _mcs_BroadcastCoordinatedPlaybackState
+ _mcs_BroadcastCoordinatedPlaybackState.cold.1
+ _mcs_CopyProperty.cold.3
+ _multicastProbeSender_Finalize
+ _multicastProbeSender_Finalize.cold.1
+ _multicastProbeSender_Finalize.cold.2
+ _multicastProbeSender_GetClassID.classID
+ _multicastProbeSender_GetClassID.descriptor
+ _multicastProbeSender_GetClassID.onceToken
+ _multicastProbeSender_Invalidate
+ _multicastProbeSender_create.isMC2UCDetectionEnabled
+ _multicastProbeSender_decrementRefCountForSSMGroupInfo
+ _multicastProbeSender_decrementRefCountForSSMGroupInfo.cold.1
+ _multicastProbeSender_incrementRefCountForSSMGroupInfo
+ _multicastProbeSender_incrementRefCountForSSMGroupInfo.cold.1
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$componentsWithString:
+ _objc_msgSend$copyDescription
+ _objc_msgSend$copySharedDeviceManager
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$evictCachedDeviceWithID:
+ _objc_msgSend$host
+ _objc_msgSend$httpConnectPSK
+ _objc_msgSend$httpConnectPSKIdentity
+ _objc_msgSend$httpConnectPassword
+ _objc_msgSend$httpConnectURLs
+ _objc_msgSend$httpConnectUserName
+ _objc_msgSend$initWithCallback:forLink:forIP:
+ _objc_msgSend$initWithDeviceIdentifier:delegate:queue:
+ _objc_msgSend$newEphemeralDeviceIdentifier
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$obtainSharedInstanceOrCreate:
+ _objc_msgSend$port
+ _objc_msgSend$proxyInfo
+ _objc_msgSend$realDeviceFound:
+ _objc_msgSend$registerDevice:properties:operationalproperties:queue:completionBlock:
+ _objc_msgSend$registerToDeviceManager
+ _objc_msgSend$removeMonitorClientForKey:
+ _objc_msgSend$scheme
+ _objc_msgSend$setAllowedLinkTypes:
+ _objc_msgSend$setCachedDeviceFoundHandler:
+ _objc_msgSend$setCachedDeviceLostHandler:
+ _objc_msgSend$setIsExternalPairing:
+ _objc_msgSend$setMonitorCallbackIfNotExists:forKey:forLink:forIP:
+ _objc_msgSend$setPdEncryptionContext:
+ _objc_msgSend$setPdProtectionOptions:
+ _objc_msgSend$setProxyCapability:
+ _objc_msgSend$setProxyProviderAuthMode:
+ _objc_msgSend$setProxyProviderType:
+ _objc_msgSend$setUsePresentDeviceStashing:
+ _objc_msgSend$setUseStrictNetworkSignatureMatching:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$unregisterDevice:
+ _objc_msgSend$unsignedIntValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x25
+ _obtainSharedInstanceOrCreate:.once
+ _obtainSharedInstanceOrCreate:.singleton
+ _realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener
+ _realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener.cold.1
+ _realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener.cold.2
+ _realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener.cold.3
+ _realTimeAudioEngine_copyPropertyDispatch.cold.6
+ _realTimeAudioEngine_setAudioLatency.cold.2
+ _realTimeAudioEngine_setTransportAudioFormatInternal
+ _realTimeAudioEngine_setTransportAudioFormatInternal.cold.1
+ _realTimeAudioEngine_setTransportAudioFormatInternal.cold.2
+ _sbpd_encryptBBuf
+ _send
+ _session_AuthorizeItem.cold.4
+ _session_BroadcastCoordinatedPlaybackState
+ _session_BroadcastCoordinatedPlaybackState.cold.1
+ _session_CopyProperty.cold.3
+ _session_GetPlaybackInfo.cold.3
+ _session_GetProxiedProperty.cold.3
+ _session_Invalidate.cold.1
+ _session_PerformRemoteAction.cold.5
+ _session_Play.cold.3
+ _session_RemovePlayQueueItem.cold.3
+ _session_SeekToDate.cold.3
+ _session_SeekToTime.cold.3
+ _session_SetEventHandler.cold.1
+ _session_SetProperty.cold.2
+ _session_SetRate.cold.5
+ _session_Stop.cold.4
+ _session_setEventHandlerInternal.cold.1
+ _session_setProxiedPropertyInternal.cold.3
+ _streamAggregateAudio_copyTransportFormatDescriptionForSourceContentFormatDescription.cold.10
+ _streamAggregateAudio_copyTransportFormatDescriptionForSourceContentFormatDescription.cold.11
+ _streamAggregateAudio_triggerSuspendOrResume.cold.12
+ _streamAggregateAudio_updateDynamicProperties.cold.14
+ _streamAggregateAudio_updateDynamicProperties.cold.15
+ _streamAggregateAudio_updateDynamicProperties.cold.16
+ _streamAggregateAudio_updateDynamicProperties.cold.17
+ _streamAggregateAudio_updateDynamicProperties.cold.18
+ _streamAggregateAudio_updateDynamicProperties.cold.19
+ _uglWrapper_deactivateShadowCompletionCallback
+ _uglWrapper_deactivationCompletionCallback
+ _uglWrapper_deactivationCompletionCallback.cold.1
+ _uglWrapper_endpointCompletionCallback
+ _uglWrapper_freeEndpointActivationContext
+ _uglWrapper_freeEndpointActivationContext.cold.1
+ _uglWrapper_handleFailedInternal
+ _uglWrapper_sendCommandCompletionCallback
+ _uglWrapper_sendDataCompletionCallback
+ _uglWrapper_shadowActivationCompletionCallback
+ _uglWrapper_wrappedActivationCompletionCallback
+ _vdsink_CopyProperty.cold.1
+ _vdsink_CopyProperty.cold.2
+ _vdsink_CopyProperty.cold.3
+ _vdsink_CopyProperty.cold.4
+ _vdsink_CopyProperty.cold.5
+ _vdsink_CopyProperty.cold.6
- GCC_except_table14
- GCC_except_table26
- GCC_except_table41
- GCC_except_table78
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName
- _APAudioEngineSetProperty
- _APAudioFormatAtmosIsAllowedForCurrentDeviceAsSender
- _APAudioFormatCopyPreferredRealTimeAudioFormats
- _APAudioFormatToCompressionType
- _APAudioHoseManagerBufferedSetCryptor
- _APAudioHoseManagerBufferedSetMagicCookie
- _APAuthenticationClientCopyProperty
- _APBrowserControllerConfigureForMaximumDiscovery
- _APBrowserControllerRegisterClusterNeedsDiscovery
- _APCarPlay_CRFetchScaledDisplays
- _APEndpointTriggerAudioHALDeviceCreation.cold.2
- _APPairingClientCopyProperty
- _APSAudioFormatDescriptionCreateAndAppendAudioFormatToList
- _APSAudioFormatDescriptionListAddSupportedFormatsForPassthrough
- _APSAudioFormatDescriptionListCreateForLowLatencySender
- _APSAudioFormatDescriptionListCreateForRealTimeSender
- _APSAudioLatencyForSystemAudioMs
- _APSDynamicLatencyManagerGetLLA
- _APSEndpointStreamAudioHoseGetAnchor
- _APSEventRecorderGetTimeBetweenCFAbsoluteTimeAndEventInMilliSecond
- _APSShouldClusterEngageOnActivation
- _APSenderSessionCopyProperty
- _APTransportDeviceIsSameDevice
- _CFAllocatorAllocate
- _CFAllocatorReallocate
- _CMTimeMinimum
- _FigCFNumberCreateUInt16
- _FigCPECryptorCopyProperty
- _FigEndpointStreamResumeWithCompletionCallback
- _FigSignalErrorAt
- _FigTransportSessionCopyProperty
- _FigTransportStreamCopyProperty
- _OUTLINED_FUNCTION_146
- _OUTLINED_FUNCTION_147
- _OUTLINED_FUNCTION_148
- _OUTLINED_FUNCTION_149
- _OUTLINED_FUNCTION_150
- _OUTLINED_FUNCTION_151
- _OUTLINED_FUNCTION_152
- _OUTLINED_FUNCTION_153
- _OUTLINED_FUNCTION_154
- _OUTLINED_FUNCTION_155
- _OUTLINED_FUNCTION_156
- _OUTLINED_FUNCTION_157
- _OUTLINED_FUNCTION_158
- _OUTLINED_FUNCTION_159
- _OUTLINED_FUNCTION_160
- _OUTLINED_FUNCTION_161
- _OUTLINED_FUNCTION_162
- _OUTLINED_FUNCTION_163
- _OUTLINED_FUNCTION_164
- _OUTLINED_FUNCTION_165
- _OUTLINED_FUNCTION_166
- _OUTLINED_FUNCTION_167
- _OUTLINED_FUNCTION_168
- _OUTLINED_FUNCTION_169
- _OUTLINED_FUNCTION_170
- _OUTLINED_FUNCTION_171
- _OUTLINED_FUNCTION_172
- _OUTLINED_FUNCTION_173
- _OUTLINED_FUNCTION_174
- _OUTLINED_FUNCTION_175
- _OUTLINED_FUNCTION_176
- _OUTLINED_FUNCTION_177
- _OUTLINED_FUNCTION_178
- __CompletedCallback
- __MergedGlobals.902
- ___APCarPlay_CRFetchScaledDisplays_block_invoke
- ___APCarPlay_CRFetchScaledDisplays_block_invoke.cold.1
- ___APCarPlay_CRFetchScaledDisplays_block_invoke.cold.2
- ___APCarPlay_CRFetchScaledDisplays_block_invoke.cold.3
- ___block_descriptor_41_e5_v8?0l
- ___block_descriptor_52_e5_v8?0l
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.1013
- ___block_descriptor_tmp.1017
- ___block_descriptor_tmp.1018
- ___block_descriptor_tmp.1021
- ___block_descriptor_tmp.1023
- ___block_descriptor_tmp.1027
- ___block_descriptor_tmp.1028
- ___block_descriptor_tmp.1029
- ___block_descriptor_tmp.1034
- ___block_descriptor_tmp.1036
- ___block_descriptor_tmp.1045
- ___block_descriptor_tmp.1057
- ___block_descriptor_tmp.1059
- ___block_descriptor_tmp.1064
- ___block_descriptor_tmp.1065
- ___block_descriptor_tmp.1072
- ___block_descriptor_tmp.1073
- ___block_descriptor_tmp.1081
- ___block_descriptor_tmp.1110
- ___block_descriptor_tmp.1117
- ___block_descriptor_tmp.1120
- ___block_descriptor_tmp.1129
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.191
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.196
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.220
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.239
- ___block_descriptor_tmp.242
- ___block_descriptor_tmp.249
- ___block_descriptor_tmp.266
- ___block_descriptor_tmp.271
- ___block_descriptor_tmp.274
- ___block_descriptor_tmp.292
- ___block_descriptor_tmp.313
- ___block_descriptor_tmp.320
- ___block_descriptor_tmp.324
- ___block_descriptor_tmp.326
- ___block_descriptor_tmp.328
- ___block_descriptor_tmp.330
- ___block_descriptor_tmp.336
- ___block_descriptor_tmp.338
- ___block_descriptor_tmp.345
- ___block_descriptor_tmp.348
- ___block_descriptor_tmp.353
- ___block_descriptor_tmp.372
- ___block_descriptor_tmp.387
- ___block_descriptor_tmp.420
- ___block_descriptor_tmp.425
- ___block_descriptor_tmp.426
- ___block_descriptor_tmp.428
- ___block_descriptor_tmp.430
- ___block_descriptor_tmp.432
- ___block_descriptor_tmp.436
- ___block_descriptor_tmp.459
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.481
- ___block_descriptor_tmp.484
- ___block_descriptor_tmp.485
- ___block_descriptor_tmp.486
- ___block_descriptor_tmp.505
- ___block_descriptor_tmp.509
- ___block_descriptor_tmp.547
- ___block_descriptor_tmp.549
- ___block_descriptor_tmp.560
- ___block_descriptor_tmp.602
- ___block_descriptor_tmp.647
- ___block_descriptor_tmp.682
- ___block_descriptor_tmp.688
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.690
- ___block_descriptor_tmp.694
- ___block_descriptor_tmp.696
- ___block_descriptor_tmp.697
- ___block_descriptor_tmp.744
- ___block_descriptor_tmp.745
- ___block_descriptor_tmp.746
- ___block_descriptor_tmp.748
- ___block_descriptor_tmp.749
- ___block_descriptor_tmp.750
- ___block_descriptor_tmp.769
- ___block_descriptor_tmp.770
- ___block_descriptor_tmp.771
- ___block_descriptor_tmp.773
- ___block_descriptor_tmp.789
- ___block_descriptor_tmp.794
- ___block_descriptor_tmp.795
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.872
- ___block_descriptor_tmp.963
- ___block_descriptor_tmp.964
- ___block_descriptor_tmp.965
- ___block_descriptor_tmp.966
- ___block_descriptor_tmp.967
- ___block_descriptor_tmp.983
- ___block_literal_global.103
- ___block_literal_global.124
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.134
- ___block_literal_global.209
- ___block_literal_global.222
- ___block_literal_global.233
- ___block_literal_global.340
- ___block_literal_global.351
- ___block_literal_global.444
- ___block_literal_global.487
- ___block_literal_global.498
- ___block_literal_global.511
- ___block_literal_global.775
- ___bufferedAudioEngine_soundCheckChanged_block_invoke.cold.1
- ___carEndpoint_activateInternal_block_invoke.127
- ___carEndpoint_activateInternal_block_invoke.127.cold.1
- ___carEndpoint_activateInternal_block_invoke.127.cold.2
- ___carEndpoint_activateInternal_block_invoke.127.cold.3
- ___carEndpoint_activateInternal_block_invoke.127.cold.4
- ___carEndpoint_activateInternal_block_invoke.127.cold.5
- ___carEndpoint_activateInternal_block_invoke.127.cold.6
- ___carEndpoint_activateInternal_block_invoke.127.cold.7
- ___carEndpoint_activateInternal_block_invoke.127.cold.8
- ___carEndpoint_activateInternal_block_invoke_2.132
- ___carEndpoint_activateInternal_block_invoke_2.132.cold.1
- ___carEndpoint_activateInternal_block_invoke_2.132.cold.2
- ___carEndpoint_activateInternal_block_invoke_3.145
- ___carEndpoint_activateInternal_block_invoke_3.145.cold.1
- ___carEndpoint_copyStateProperty_block_invoke.cold.16
- ___carEndpoint_getStreamInfoForDisplayUUID_block_invoke.cold.1
- ___carManager_updateCurrentEndpoint_block_invoke.253
- ___endpointLocal_setIsMuted_block_invoke
- ___endpointLocal_setIsMuted_block_invoke.cold.1
- ___endpointLocal_setVolumeSlider_block_invoke
- ___getCRFetchScaledDisplaysSymbolLoc_block_invoke
- ___manager_create_block_invoke_3.cold.1
- _airPlayDebugIPC_initEndpointManagerArray
- _airPlayDescription_isLegacyAirPlaySpeaker.cold.1
- _airPlayDescription_isLegacyAirPlaySpeaker.cold.2
- _apsession_ensureConnectedInternal.cold.58
- _apsession_ensureConnectedInternal.cold.59
- _apsession_ensureDisconnected.cold.1
- _apsession_handleTransportSessionDisconnected.cold.1
- _apsession_updateReceiverInfoForRTCStats
- _audioStream_isPassthroughSupportedForFormatDescription.cold.5
- _audioStream_receivedMediaDataControlMessage
- _audioStream_receivedMediaDataControlMessage.cold.1
- _audioStream_receivedMediaDataControlMessage.cold.10
- _audioStream_receivedMediaDataControlMessage.cold.11
- _audioStream_receivedMediaDataControlMessage.cold.12
- _audioStream_receivedMediaDataControlMessage.cold.13
- _audioStream_receivedMediaDataControlMessage.cold.14
- _audioStream_receivedMediaDataControlMessage.cold.15
- _audioStream_receivedMediaDataControlMessage.cold.16
- _audioStream_receivedMediaDataControlMessage.cold.17
- _audioStream_receivedMediaDataControlMessage.cold.2
- _audioStream_receivedMediaDataControlMessage.cold.3
- _audioStream_receivedMediaDataControlMessage.cold.4
- _audioStream_receivedMediaDataControlMessage.cold.5
- _audioStream_receivedMediaDataControlMessage.cold.6
- _audioStream_receivedMediaDataControlMessage.cold.7
- _audioStream_receivedMediaDataControlMessage.cold.8
- _audioStream_receivedMediaDataControlMessage.cold.9
- _browserController_configureForMaximumDiscovery
- _browserController_configureForMaximumDiscovery.cold.1
- _browserController_registerClusterNeedsDiscovery
- _bufferedAudioEngine_FlushWithinSampleRange.cold.2
- _bufferedAudioEngine_audioHoseRegistrarDeregisterHose
- _bufferedAudioEngine_audioHoseRegistrarDeregisterHoseInternal
- _bufferedAudioEngine_audioHoseRegistrarDeregisterHoseInternal.cold.1
- _bufferedAudioEngine_audioHoseRegistrarDeregisterHoseInternal.cold.2
- _bufferedAudioEngine_audioHoseRegistrarRegisterHose
- _bufferedAudioEngine_audioHoseRegistrarRegisterHose.callbacks
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.1
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.10
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.2
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.3
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.4
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.5
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.6
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.7
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.8
- _bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal.cold.9
- _bufferedAudioEngine_cancelRTCUnderrunForHose
- _bufferedAudioEngine_createAndResumeAudioTimerInternal
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.1
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.2
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.3
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.4
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.5
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.6
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.7
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.8
- _bufferedAudioEngine_createAndResumeAudioTimerInternal.cold.9
- _bufferedAudioEngine_engineBufferedToStartWaterMark.cold.1
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.14
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.15
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.16
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.17
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.18
- _bufferedAudioEngine_handleTerminalSetRateErrorForHoseManager
- _bufferedAudioEngine_handleTerminalSetRateErrorForHoseManager.cold.1
- _bufferedAudioEngine_handleTerminalSetRateErrorForHoseManager.cold.2
- _bufferedAudioEngine_handleTerminalSetRateErrorForHoseManager.cold.3
- _bufferedAudioEngine_hoseManagerSetRateCallbackCompletionHandler
- _bufferedAudioEngine_hoseManagerSetRateCallbackCompletionHandlerInternal
- _bufferedAudioEngine_initializeRTCReporting
- _bufferedAudioEngine_initializeResumeState
- _bufferedAudioEngine_isRateZero
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.1
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.10
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.11
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.12
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.13
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.14
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.2
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.3
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.4
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.5
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.6
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.7
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.8
- _bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses.cold.9
- _bufferedAudioEngine_resetAllRTCDataForHose
- _bufferedAudioEngine_updateRTCUnderrunStatisticsForHose
- _bufferedAudioEngine_updateStartWatermarkTime
- _carEndpoint_AccumulateSignpostsAndSendToTimeStore
- _carEndpoint_AccumulateSignpostsAndSendToTimeStore.cold.1
- _carEndpoint_activateInternal
- _carEndpoint_getDisplayUUIDForStream
- _carEndpoint_logStreamStats
- _carEndpoint_postPerformanceReport
- _carEndpoint_postPerformanceReport.cold.1
- _carEndpoint_registerForOverrideTurnByTurnConfigurationChangedNotification
- _carEndpoint_setupNotificationsAndInitialParametersForJarvis
- _endpointAggregate_copyPropertyInternal.cold.11
- _endpointAggregate_handleSubEndpointVolumeCacheClear
- _endpointCluster_handleSubEndpointVolumeCacheClear
- _endpointLocal_Activate.cold.1
- _endpointLocal_Activate.cold.2
- _endpoint_UpdateFeatures.cold.1
- _endpoint_activateInternal.cold.21
- _endpoint_activateInternal.cold.22
- _endpoint_activateInternal.cold.23
- _endpoint_activateInternal.cold.24
- _endpoint_activateInternal.cold.25
- _endpoint_authHandlingComplete
- _endpoint_authHandlingComplete.cold.1
- _endpoint_authHandlingComplete.cold.2
- _endpoint_callDelegateHandleAuthRequired
- _endpoint_isInLocalStereoPairPersistentConnection
- _getCRFetchScaledDisplaysSymbolLoc.ptr
- _kAPBrowserControllerCreationOption_OpenFullNANAllowed
- _kAPBrowserControllerProperty_IsConfiguredForMaximumDiscovery
- _kAPBrowserControllerProperty_RadiosNeededForMaximumDiscovery
- _kAPBrowserCreationOption_OpenFullNANAllowed
- _kAPBrowserProperty_IsConfiguredForMaximumDiscovery
- _kAPBrowserProperty_RadiosNeededForMaximumDiscovery
- _kAPEndpointClusterOptionKey_LocalSPPCEnabledOverride
- _kAPEndpointCreationOption_IsPersistentConnectionOverride
- _kAPEndpointProperty_IsDissociated
- _kAPEndpointStreamResumeOption_FigAudioSession
- _kAPEndpointStreamResumeOption_FramesPerPacket
- _kAPEndpointStreamResumeOption_InitialTransportAudioFormat
- _kAPSEndpointStreamAudioHoseSBARCreationOption_FigAudioSession
- _kAPSenderSessionProperty_ActivationConnectionTimeMs
- _kAPSenderSessionProperty_ActivationMsgsProcessingTotalTimeMs
- _kAPSenderSessionProperty_ActivationMsgsRoundTripTotalTimeMs
- _kAPSenderSessionTransportStreamOption_UseQUIC
- _kAPTransportStreamProperty_AllMsgsProcessingTotalTimeMs
- _kAPTransportStreamProperty_AllMsgsRoundTripTotalTimeMs
- _kFigEndpointNotification_VolumeCacheShouldBeCleared
- _localStream_isPassthroughSupportedForFormatDescription.cold.6
- _manager_ConfigureForMaximumDiscovery
- _manager_ConfigureForMaximumDiscovery.cold.1
- _manager_handleEndpointEvent.cold.4
- _manager_handleEndpointEvent.cold.5
- _manager_handleEndpointEvent.cold.6
- _manager_transportDeviceEqual
- _manager_transportDeviceHash
- _realTimeAudioEngine_endpointStreamResumeInternal.cold.10
- _realTimeAudioEngine_endpointStreamResumeInternal.cold.8
- _realTimeAudioEngine_endpointStreamResumeInternal.cold.9
- _realTimeAudioEngine_resumeSubPhase3_Internal.cold.9
- _realTimeAudioEngine_setTransportAudioFormatASBDInternal
- _realTimeAudioEngine_setTransportAudioFormatASBDInternal.cold.1
- _realTimeAudioEngine_setTransportAudioFormatASBDInternal.cold.2
- _sbpd_convertTimestampToNetworkTime
- _spmanager_browserEventHandler.cold.20
- _spmanager_transportDeviceEqual
- _spmanager_transportDeviceHash
- _streamAggregateAudio_CopyProperty.cold.12
- _streamAggregateAudio_CopyProperty.cold.13
- _streamAggregateAudio_CopyProperty.cold.14
- _streamAggregateAudio_CopyProperty.cold.15
- _vdsink_GetPropertyAsync.cold.1
- _vdsink_GetPropertyAsync.cold.2
- _vdsink_GetPropertyAsync.cold.3
- _vdsink_GetPropertyAsync.cold.4
- _vdsink_GetPropertyAsync.cold.5
- _vdsink_GetPropertyAsync.cold.6
CStrings:
+ "\tDetection stats\t: \"MC2UC Status\" = %s\n"
+ "\tDetection stats\t: \"Probes Rx\" = %d\n"
+ "\tDetection stats\t: \"Probes Tx\" = %d\n"
+ "\tDetection stats\t: \"Time-to-detect\" = %dms\n"
+ "        %@\n"
+ "     including -w means it must be an UGL wrapper endpoint\n"
+ "     omitting -r|w means it must be the non-remote-control, non-wrapper endpoint\n"
+ "    %@\n"
+ "   %llu\n"
+ "  %s 'HomePod' ba RoutingContextUUID:s:test-routing-id\n"
+ "  %s -r 'Living Room' c\n"
+ "  - b|%@: Turn on background discovery\n"
+ "  - d|%@: Turn on full detailed discovery\n"
+ "  - n|%@: Turn off discovery\n"
+ "  - p|%@: Turn on presence scanning\n"
+ "  -r|w is used when endpoint is specified with name or ID:\n"
+ "  For example, %s %@\n"
+ "  features are a combination of characters: s)creen, a)udio, p)layback, b)uffered audio, c)ontrol\n"
+ "  mode is one of the kFigEndpointManagerDiscoveryMode... constants:\n"
+ "  start: start the receiver server.\n"
+ "  stop: stop the receiver server.\n"
+ " (%llu ms sender, %llu ms connection, %llu ms networking, %llu ms receiver, %llu ms remote)"
+ " INVALIDATED"
+ " [%{ptr}] Medium Latency supported formats extended=%@"
+ " from user defaults"
+ "### %@ ESAE setrate timed out. Continuing Async.\n"
+ "### APMulticastProbeSender Finalized\n"
+ "### [%{ptr}] ESAE resume failed err=%#m\n"
+ "### [%{ptr}] ESAE resume failed for auth. Continuing.\n"
+ "### [%{ptr}] ESAE resume timed out. Continuing Async.\n"
+ "### [%{ptr}] ESAE suspend failed err=%#m\n"
+ "### [%{ptr}] ESAE suspend timed out. Continuing Async.\n"
+ "### [%{ptr}] Failed to parse MDE message plist. %@\n"
+ "### [%{ptr}] delegateContextRemoteControl was not yet set or already cleared"
+ "%###s called, context [%{ptr}]\n"
+ "%###s called, playbackSession [%{ptr}], shouldSendMetadata [%s]. inMetadata [%@]\n"
+ "%###s called, remoteControlSession [%{ptr}], eventType [%@], payload [%{ptr}], client context [%{ptr}]\n"
+ "%###s called, status [%#m], authorize response [%@], context [%{ptr}]\n"
+ "%###s called, status [%#m], params [%@], context [%{ptr}]\n"
+ "%###s called, status [%#m], playbackInfo [%@], context [%{ptr}]\n"
+ "%###s called, status [%#m], property info [%@], context [%{ptr}]\n"
+ "%###s called, status [%#m], seek completion info [%@], context [%{ptr}]\n"
+ "%###s called, status [%#m], streaming key info [%@], context [%{ptr}]\n"
+ "%###s called: context [%{ptr}]\n"
+ "%###s ended: err [%#m]\n"
+ "%###s request count: %d\n"
+ "%###s: There are %d internal clients requiring Detailed discovery\n"
+ "%###s: callback [%{ptr}], context [%{ptr}]\n"
+ "%###s: callback [%{ptr}], context [%{ptr}], item [%@], PICData [%@], playerGUID [%@]\n"
+ "%###s: callback [%{ptr}], context [%{ptr}], key [%@], value [%@]\n"
+ "%###s: callback [%{ptr}], context [%{ptr}], payload [%@]\n"
+ "%###s: callback [%{ptr}], context [%{ptr}], updated streaming key info  [%@]\n"
+ "%##a"
+ "%@ AudioCompressionSource - vbrBitRate = %d, maxBufferSize = %u, CodecType:%@"
+ "%@ AudioEngineBufferedAdapter using audio latency %d ms, audio latency min %d ms, audio latency adjust %d ms, audio latency offset %d ms\n"
+ "%@ AudioEngineRealTime using stream type %@ and audio format %@"
+ "%@ Changing Audio Frames Per Packet was=%u is=%u (for LL or AAC_ELD Spatial Mirroring)"
+ "%@ Data path has overrun in the buffered audio engine\n"
+ "%@ Data path has underrun in the audio source\n"
+ "%@ DynamicLatencyManager is using variant=%@ latencyTierIdx=%d latencyMs=%d \n"
+ "%@ Endpoint stream set\n"
+ "%@ Failed to retrieve data from the audio source\n"
+ "%@ Flushed\n"
+ "%@ Flushing...\n"
+ "%@ New AudioAnchorTime %1.3f (now: %1.3f) -> HostAnchorTime %1.3f (now: %1.3f)\n"
+ "%@ PWD activation options: %@\n"
+ "%@ Resumed\n"
+ "%@ Set dynamic latency offset to %d\n"
+ "%@ Set dynamic latency offset to %d and live adaptive latency offset to %1.3f\n"
+ "%@ TransportASBD: [%{asbd}]. transportAudioFormat: %@"
+ "%@ Updating dynamic latency offset from %d to %d ms\n"
+ "%@ Updating live adaptive latency offset from %1.3f to %1.3f. Applying to currently running session\n"
+ "%@ cryptor subsample aux data: %@\n"
+ "%@ dynamic latency offset change payload is NULL\n"
+ "%@ forward cryptor aux data: %s\n"
+ "%@ forward frame user data: %s\n"
+ "%@ override canvas size is available\n"
+ "%@ overwriting pixel format to '%C'\n"
+ "%@ vbrBitRate = %d. CodecType:%@"
+ "%@ vbrMaxPacketSize = %d. CodecType:%@"
+ "%@-%u"
+ "%@:%@"
+ "%@://%@"
+ "%p-%llu"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "%s_%u"
+ "(?=\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]}\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})"
+ "(Fig)"
+ "-[APHTTPProxyMonitorClient deviceInfoDidChange:deviceInfo:]"
+ "-[APHTTPProxyMonitorClient deviceIsRegisteredDidChange:isRegistered:]"
+ "-[APHTTPProxyMonitorClient initWithCallback:forLink:forIP:]"
+ "-[APHTTPProxyMonitorClient registerToDeviceManager]"
+ "-[APHTTPProxyMonitorClient registerToDeviceManager]_block_invoke"
+ "-[APHTTPProxyMonitorClientManager init]"
+ "-[APHTTPProxyMonitorClientManager removeMonitorClientForKey:]"
+ "-[APHTTPProxyMonitorClientManager setMonitorCallbackIfNotExists:forKey:forLink:forIP:]"
+ "1.1"
+ "890.61.4.11.2"
+ "<APAudioEngineBufferedAdapter>"
+ "<APEndpointManagerIntrospector> [%{ptr}] didn't match endpoint [%{ptr}] for ID %@, name %@, hash %@, remote %s, wrapper %s"
+ "<APEndpointPlus %{ptr} %s>"
+ "<APEndpointUGLWrapper [%p]: wrapped=%p>"
+ "<APUGL> Clearing rc server groupUUID: %@ -> nil"
+ "<APUGL> Updating rc server groupUUID: %@ -> %@"
+ "<APUGL> Updating rc server: could not get groupUUID from endpoint [%{ptr}]!"
+ "<PWDKeyExchange> [%{ptr}] Completed (%.3f)"
+ "<PWDKeyExchange> [%{ptr}] Failed to copy PWD KeyID from [%{ptr}] with error: %#m"
+ "<PWDKeyExchange> [%{ptr}] Failed with status=%#m"
+ "=== Endpoint Manager: %@ [%{ptr}]\n"
+ "==============================================================\n"
+ "@\"NRDeviceIdentifier\""
+ "@\"NRDeviceMonitor\""
+ "@20@0:8B16"
+ "@36@0:8@?16C24^{__CFString=}28"
+ "@?"
+ "ADD"
+ "AIRPLAY_SIGNPOST_AUDIOENGINE_HOSE_REGISTERED"
+ "AIRPLAY_SIGNPOST_AUDIOENGINE_RATE_TO_1_REQUEST"
+ "AIRPLAY_SIGNPOST_AUDIOENGINE_RESUME_INTERVAL"
+ "AIRPLAY_SIGNPOST_AUDIOENGINE_SETENDPOINTSTREAM_INTERVAL"
+ "AIRPLAY_SIGNPOST_BUFFERED_EPS_SETUP_AUDIOSTREAM_INTERVAL"
+ "AIRPLAY_SIGNPOST_BUFFERED_EPS_TRANSPORT_AUDIO_INTERVAL"
+ "AIRPLAY_SIGNPOST_BUFFERED_EPS_TRANSPORT_CONTROL_INTERVAL"
+ "APAC/48000/9.1.6"
+ "APAT"
+ "APAT_Buffered"
+ "APAT_Realtime"
+ "APAudioEngineBufferedAdapter"
+ "APAudioEngineBufferedAdapter.c"
+ "APAudioEngineBufferedAdapterCreate"
+ "APEndpoint.m"
+ "APEndpointDescriptionAirPlayCreateWithBonjourInfo"
+ "APEndpointManagerPlus"
+ "APEndpointManagerPlusCreate"
+ "APEndpointManagerUpdateInternalClientNeedingDiscovery"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointPlus"
+ "APEndpointPlusCreate"
+ "APEndpointPlusCreateWithBonjourInfo"
+ "APEndpointPlusCreateWithInnerEndpoint"
+ "APEndpointPlusUtils_CopyDeviceIDFromEndpointDescription"
+ "APEndpointStreamAggregateAudio.c"
+ "APEndpointStreamBuffered <APSAudioProtocolDriverHoseControlProtocol> on <%p>"
+ "APEndpointStreamBufferedAudio <APEndpointStreamBufferedHoseStreamingProtocol> on <%p>"
+ "APEndpointStreamBufferedAudio <APSAudioProtocolDriverHoseDataAPATProtocol> on <%p>"
+ "APEndpointStreamBufferedAudio <APSAudioProtocolDriverHoseDataBaseProtocol> on <%p>"
+ "APEndpointTriggerAudioHALDeviceCreationEx"
+ "APEndpointUGLWrapper"
+ "APEndpointUGLWrapper.%{ptr}.notification"
+ "APEndpointUGLWrapperCreate"
+ "APEndpointUGLWrapperUpdateWithTransportDevice"
+ "APHTTPProxyMonitorClient"
+ "APHTTPProxyMonitorClient-%{ptr}.monitorCallback"
+ "APHTTPProxyMonitorClientManager"
+ "APHTTPProxyMonitorClientRegisterHTTPProxyMonitor"
+ "APHTTPProxyMonitorClientUnregisterHTTPProxyMonitor"
+ "APMulticastProbeSender"
+ "APMulticastProbeSenderCopySSMGroupInfo"
+ "APMulticastProbeSenderRegister"
+ "APMulticastProbeSenderReleaseSSMGroupInfo"
+ "APMulticastProbeSenderUnregister"
+ "APMulticastProbeSenderUpdateMC2UC"
+ "APPWDKeyExchangeSenderSessionCopyEncoderEncryptionKeyID"
+ "APSenderSessionAirPlay %{ptr} with name %@ created (usage=%s).\n"
+ "APVirtualDisplayTestSink.c"
+ "AVConferenceSupportsPWD"
+ "Action not supported"
+ "Activated endpoint [%{ptr}], features 0x%llx, options (%@): success\n"
+ "Activating endpoint [%{ptr}] '%@' with features 0x%llx, correlationID: %'@, options: %@\n"
+ "ActivationTimingInformation"
+ "ActiveStreamConnectionIDs"
+ "Addresses"
+ "AdminControl"
+ "AirPlay Plus"
+ "AirPlayAudioEngineAdapter.%{ptr}.%@.request"
+ "AirPlayAudioEngineAdapter.%{ptr}.%@.response"
+ "AirPlayAudioEngineAdapter.%{ptr}.io"
+ "AirPlayVideoPlaybackAudioOnlyMode"
+ "Allocation error"
+ "ArtworkData"
+ "ArtworkMIMEType"
+ "AudioStreamOverride"
+ "Available Endpoints:\n"
+ "BAE [%{ptr}] %s### Could not create APSAudioHoseMetricCollector. err=%d\n"
+ "BAE [%{ptr}] %s%@ is an unsupported ProtocolDriver Type"
+ "BAE [%{ptr}] %s(startup) zeroFirstRemoteMediaTime: %d\n"
+ "BAE [%{ptr}] %sAPSAudioProtocolDriverSenderSendAudioData failed with err=%d\n"
+ "BAE [%{ptr}] %sBAE is in %s mode, stream hint [%{ptr}]"
+ "BAE [%{ptr}] %sDeregistering hoseControl [%{ptr}] with audio engine (current hoseCount = %d)\n"
+ "BAE [%{ptr}] %sRegistered hoseControl [%{ptr}] (%@) (%s) registered (stream count %d) audioBufferSize = %d\n"
+ "BAE [%{ptr}] %sRegistering audio hose [%{ptr}] with audio engine (current hoseCount = %d)\n"
+ "BAE [%{ptr}] %sRegistering hoseControl [%{ptr}] with audio engine (current hoseCount = %d)\n"
+ "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Could not process all invalid samples at this time. Discard Count: %u lastRemoteMediaTimeDiscarded %1.3f (sample time %1.3f), flushSampleRangeStart %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Could not process all valid samples at this time. Prepared: %u nextRemoteMediaTimestamp %1.3f (sample time %1.3f), flushSampleRangeStart %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] (burst) Not flushing hose [%{ptr}] (%@) since ( rate == 0.0 ) AND ( hose has not started sending audio data )\n"
+ "BAE [%{ptr}] %s[0x%04X] APSAudioProtocolDriverHoseControlSetCryptor failed for hose [%{ptr}] with err= %d \n "
+ "BAE [%{ptr}] %s[0x%04X] APSAudioProtocolDriverHoseControlSetMagicCookie failed for hose [%{ptr}] with err= %d \n "
+ "BAE [%{ptr}] %s[0x%04X] Discarded invalid sample buffer [%p] OPTS: %1.3f (media time: %1.3f), flush sample range start: %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] End of flush range processing, nextRemoteMediaTimestamp: %1.6f (%lld/%d)\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Discarding all invalid samples: nextRemoteMediaTimestamp %1.3f end %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Process valid samples complete: Prepared: %u nextRemoteMediaTimestamp %1.3f (sample time %1.3f)\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Processed invalid samples complete: Discard Count: %u lastRemoteMediaTimeDiscarded %1.3f (sample time %1.3f)\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Processing all valid samples: nextRemoteMediaTimestamp %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Trimm of unwanted samples from message ring complete: next valid message media time %1.3f (sample time %1.3f)\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: currentMediaTime = %1.3f nextRemoteMediaTimestamp = %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: flushRangeRemoteMediaTime %1.3f:%1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: sampleRange %1.3f:%1.3f (sbufEndOutputPTS %1.3f)\n"
+ "BAE [%{ptr}] %s[0x%04X] Found TrimAtEnd attachment with duration=%1.3f seconds, trimAtEndStartPTS=%1.3f(%lld/%d), sbuf.PTS=%1.3f, sbuf.duration=%1.3f \n"
+ "BAE [%{ptr}] %s[0x%04X] Found TrimAtStart attachment with duration %1.3f seconds, sbuf_pts: %1.3f, sbuf_opts: %1.3f, sbuf_dur: %1.3f, sbuf_odur: %1.3f  trimAtStartEndPTS=%1.3f(%lld/%d) \n"
+ "BAE [%{ptr}] %s[0x%04X] Posting notification for discontinuity sbufEndOutputPTS(%1.3f) sbufOPTS(%1.3f)"
+ "BAE [%{ptr}] %s[0x%04X] Process valid sample buffer [%p] OPTS: %1.3f (media time: %1.3f), flush sample range start: %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] ProtocolDriver: [%{ptr}] BufferCount %lu, BufferLevelBytes %d, FirstBufferTime: %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] SetRateAndAnchorTime - set firstSampleTimeAfterReset to %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] TrimAtEndPostAdjustment new adjusted nextRemoteMediaTimestamp=%1.3f(%lld/%d) trimAtEndPostAdjustment=%1.3f \n"
+ "BAE [%{ptr}] %s[0x%04X] bufferedAudioEngine_protocolDriverTickTimer requestedPlaybackRate=%f, mediaTime=%1.3f, hostTime=%1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] flushSampleRangeStart but should not discard opts=%1.3f endopts=%1.3f oduration=%1.3f"
+ "BAE [%{ptr}] %s[0x%04X] need to add TrimDurationAtEnd %1.3f since flushSampleRangeStart falls within sbuf."
+ "BAE [%{ptr}] %sflushWithinRangeLimitTime set to %1.1f seconds\n"
+ "BAE [%{ptr}] %sresumed for %s, APAT enabled %s, stream [%{ptr}] does%s support APAT. Posting 'ActiveConfigurationDidBecomeInvalid'!\n"
+ "BAE [%{ptr}] %sresumed for %s, APAT enabled %s, stream [%{ptr}] no longer supports APAT. Posting 'ActiveConfigurationDidBecomeInvalid'!\n"
+ "BAE [%{ptr}] %swhaPrimingOptimization set to %u\n"
+ "BAE [%{ptr}] %szeroFirstRemoteMediaTime is true.  Zero firstRemoteMediaTime"
+ "BAEA ['HLA'-%{ptr}]"
+ "BES [%{ptr}] APAT Data Hose callback is NULL."
+ "BES [%{ptr}] was told to use APAT, but it is not supported!\n"
+ "Basic %@"
+ "Boolean APEndpointUGLWrapperIsEmpty(FigEndpointRef)"
+ "Boolean APSenderSessionShouldEstablishNetworkClockLink(APSenderSessionUsage, APEndpointDescriptionRef, CFStringRef, void *)"
+ "Boolean bufferedAudioEngine_shouldDiscardSampleBuffer(FigEndpointStreamAudioEngineRef, CMSampleBufferRef)"
+ "Boolean carEndpoint_overrideFeatureKeyWithPrefValue(FigEndpointRef, CFMutableArrayRef, CFStringRef, CFStringRef)"
+ "Boolean emp_isEndpointCacheable(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
+ "Boolean emp_shouldAllowCacheableType(APEndpointPlusType)_block_invoke"
+ "Boolean endpointAggregate_isUpdateUGLRCServerNeeded(FigEndpointRef, FigEndpointRef)"
+ "CARAirPlaySessionEndTimeInfo"
+ "CFArrayRef apsession_copyActiveStreamConnectionIDs(APSenderSessionRef)_block_invoke"
+ "CFDataRef multicastProbeSender_createPayloadForMC2UC(APMulticastProbeSenderRef, uint32_t)"
+ "CFDictionaryCreateMutable failed"
+ "CFMutableArrayRef endpointUGLWrapper_copyActivatedShadowEndpoints(FigEndpointRef)"
+ "CFMutableArrayRef endpointUGLWrapper_copySortedShadowEndpoints(FigEndpointRef)"
+ "CFMutableArrayRef endpointUGLWrapper_copySortedShadowEndpoints(FigEndpointRef)_block_invoke"
+ "CRFetchScaledDisplaysForCertificateSerialNumber"
+ "CRFetchScaledDisplaysForCertificateSerialNumber completion handler successful, took %lu ms\n"
+ "Cacheable Cluster IDs: %lu\n"
+ "Cacheable Device IDs: %lu\n"
+ "CachedActivationFailure"
+ "CachedEndpointAdded"
+ "CachedEndpointRemoved"
+ "Calling CRFetchScaledDisplaysForCertificateSerialNumber...\n"
+ "Cannot register path"
+ "CarPlayVideoOverlayUI"
+ "CarPlayVideoSettings"
+ "Carplay is not supported with APAT"
+ "Checking condition for UGL-RCServer update FF %d | SM %d"
+ "Cleaning up pending request: %@\n"
+ "ClientAuditToken"
+ "Cluster"
+ "ClusterEndpoint:[%{ptr}] (%s %@) %''@ PGUUID:%@ Parent:[%{ptr}]\n"
+ "Creating buffered audio engine adapter\n"
+ "DEMOTE"
+ "Deactivated endpoint [%{ptr}]: success\n"
+ "Disable RC endpoint plus as %s is %s"
+ "DisableRemoteAudioRender"
+ "DiscontinuityFound"
+ "Discovery Mode:      %@\n"
+ "EVICT"
+ "Endpoint:[%{ptr}] (%s) %''@ DiscoveryID:%llu Parent:[%{ptr}]\n"
+ "Endpoint:[%{ptr}] (Local) %''@ DeviceID:%@ Parent:[%{ptr}]\n"
+ "EndpointManagerPlus:[%{ptr}] inner [%{ptr}] type %@\n"
+ "EndpointPlus:[%{ptr}] Parent:[%{ptr}]\n"
+ "Error: Failed to activate endpoint [%{ptr}], features 0x%llx, options (%@): %#m\n"
+ "Error: Failed to deactivate endpoint [%{ptr}]: %#m\n"
+ "Error: Missing argument: features\n"
+ "Error: Missing argument: mode\n"
+ "Examples:\n"
+ "FVDFrameUserData"
+ "Failed allocating audio buffer"
+ "Failed to allocate memory for io queue"
+ "Failed to allocate memory for request queue"
+ "Failed to allocate memory for response queue"
+ "Failed to create APMulticastProbeSender with err=%#m, %s\n"
+ "Failed to create deep copy"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "FigEndpointAcquireAndCopyResource"
+ "FigEndpointBorrowScreen"
+ "FigEndpointCloseCommChannel"
+ "FigEndpointCopyCurrentScreenViewArea"
+ "FigEndpointCopyHIDInputMode"
+ "FigEndpointCreateCommChannel"
+ "FigEndpointCreatePlaybackSession"
+ "FigEndpointCreateRemoteControlSession"
+ "FigEndpointDisableBluetoothConnectivityToDevice"
+ "FigEndpointDuckAudio"
+ "FigEndpointRef manager_introspector_copyMatchingEndpoint(FigEndpointManagerRef, CFStringRef, Boolean, Boolean)"
+ "FigEndpointRelinquishResource"
+ "FigEndpointRequestCarUI"
+ "FigEndpointRequestScreenViewArea"
+ "FigEndpointSetHIDInputMode"
+ "FigEndpointTakeScreen"
+ "FigEndpointUnborrowScreen"
+ "ForwardCryptorSubsampleAuxData"
+ "ForwardFrameUserData"
+ "Forwarding %@ from [%{ptr}] to [%{ptr}], payload %@"
+ "GenericControl"
+ "GroupPlayback"
+ "HALVolumeDB"
+ "HTPlayback"
+ "HTTPProxy for CarPlay is turned off with defaults com.apple.airplay/carPlayForceHTTPProxyDisabled"
+ "Inner:               [0x%04X]\n"
+ "IsEndpointPlus"
+ "IsThirdPartyReceiver"
+ "IsUGLRCServerUpdateNeeded"
+ "IsUGLReceiverSessionActive"
+ "Item is NULL"
+ "Last Session deactivation time: %f (file access timeMS: %llu)\n"
+ "Legacy"
+ "Local Cluster ID:    %@\n"
+ "Local ID:            %@\n"
+ "LocalControl"
+ "MC2UCCryptor"
+ "MC2UCDetection"
+ "MC2UCInterface"
+ "MC2UCReferenceCount"
+ "MC2UCRxCount"
+ "MC2UCSSMGroupInfo"
+ "MC2UCSocketFd"
+ "MC2UCStatus"
+ "MC2UCTimeToDetect"
+ "MC2UCToken"
+ "MC2UCTxCount"
+ "NANMACAddress"
+ "NRDeviceManager registerDevice completion callback with error: %#m"
+ "NRDeviceMonitorDelegate"
+ "NetworkingMs"
+ "NextRemoteMediaTimestamp"
+ "No URL matching desired IP %##a"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "No mc2uc metrics found\n"
+ "Non-numeric remote media timestamp"
+ "NullSource"
+ "OSStatus APAudioEngineBufferedAdapterCreate(CFAllocatorRef, CFDictionaryRef, FigEndpointStreamAudioEngineRef, FigEndpointStreamAudioEngineRef *)"
+ "OSStatus APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber(CFDataRef, CFArrayRef, CFArrayRef *)"
+ "OSStatus APCarPlay_CRFetchScaledDisplaysForCertificateSerialNumber(CFDataRef, CFArrayRef, CFArrayRef *)_block_invoke"
+ "OSStatus APEndpointManagerPlusCreate(APEndpointManagerPlusType, FigEndpointManagerRef, FigEndpointManagerRef *)"
+ "OSStatus APEndpointPlaybackSessionRemoteControlCreate(CFStringRef, APSenderSessionRef, CFStringRef, CFDictionaryRef, FigEndpointPlaybackSessionRef *)"
+ "OSStatus APEndpointPlusCreate(APEndpointPlusType, FigEndpointRef *)"
+ "OSStatus APEndpointUGLWrapperCreate(FigEndpointRef, CFStringRef, CFDictionaryRef, FigEndpointRef *)"
+ "OSStatus APEndpointUGLWrapperUpdateWithTransportDevice(FigEndpointRef, APTransportDeviceRef, Boolean)"
+ "OSStatus APEndpointUGLWrapper_AcquireAndCopyResource(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef, CFTypeRef *)"
+ "OSStatus APEndpointUGLWrapper_ActivateForFeaturesWithCompletionCallback(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus APEndpointUGLWrapper_BorrowScreen(FigEndpointExtendedRef, CFStringRef, CFStringRef)"
+ "OSStatus APEndpointUGLWrapper_CloseCommChannel(FigEndpointExtendedRef, CFStringRef)"
+ "OSStatus APEndpointUGLWrapper_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus APEndpointUGLWrapper_CreateCommChannel(FigEndpointExtendedRef, CFDictionaryRef, CFStringRef *)"
+ "OSStatus APEndpointUGLWrapper_CreatePlaybackSession(FigEndpointRef, FigEndpointPlaybackSessionRef *)"
+ "OSStatus APEndpointUGLWrapper_CreateRemoteControlSession(FigEndpointExtendedRef, CFDictionaryRef, FigEndpointRemoteControlSessionRef *)"
+ "OSStatus APEndpointUGLWrapper_DeactivateWithCompletionCallback(FigEndpointRef, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus APEndpointUGLWrapper_Dissociate(FigEndpointRef)"
+ "OSStatus APEndpointUGLWrapper_DuckAudio(FigEndpointExtendedRef, CFDictionaryRef)"
+ "OSStatus APEndpointUGLWrapper_EnsureAuthorizedWithCompletionCallback(FigEndpointRef, CFDictionaryRef, FigEndpointCompletionCallback, void *)"
+ "OSStatus APEndpointUGLWrapper_RelinquishResource(FigEndpointExtendedRef, CFStringRef, CFTypeRef)"
+ "OSStatus APEndpointUGLWrapper_SendCommand(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef, FigEndpointSendCommandCompletionCallback, void *)"
+ "OSStatus APEndpointUGLWrapper_SendData(FigEndpointExtendedRef, CFStringRef, CFDataRef, FigEndpointSendDataCompletion, void *)"
+ "OSStatus APEndpointUGLWrapper_SetDelegate(FigEndpointRef, const FigEndpointDelegate *)"
+ "OSStatus APEndpointUGLWrapper_SetDelegateRemoteControl(FigEndpointRef, const FigEndpointDelegateRemoteControl *)"
+ "OSStatus APEndpointUGLWrapper_SetDelegateRouting(FigEndpointRef, const FigEndpointDelegateRouting *)"
+ "OSStatus APEndpointUGLWrapper_SetDelegateVolumeAndMute(FigEndpointRef, const FigEndpointDelegateVolumeAndMute *)"
+ "OSStatus APEndpointUGLWrapper_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus APEndpointUGLWrapper_UnborrowScreen(FigEndpointExtendedRef, CFStringRef, CFStringRef)"
+ "OSStatus APHTTPProxyMonitorClientRegisterHTTPProxyMonitor(CFTypeRef, Boolean, CFStringRef _Nullable, HTTPProxyParamterChangedHandler)"
+ "OSStatus APHTTPProxyMonitorClientUnregisterHTTPProxyMonitor(CFTypeRef)"
+ "OSStatus APMulticastProbeSenderRegister(CMBaseObjectRef, CFStringRef, CFStringRef)"
+ "OSStatus APMulticastProbeSenderReleaseSSMGroupInfo(CMBaseObjectRef, CFStringRef, sa_family_t)"
+ "OSStatus APMulticastProbeSenderUnregister(CMBaseObjectRef, CFStringRef, CFDictionaryRef *)"
+ "OSStatus APMulticastProbeSenderUpdateMC2UC(CMBaseObjectRef, CFStringRef, uint32_t, MC2UCFeatureStatus, int32_t)"
+ "OSStatus APSenderSessionAirPlayCreate(CFAllocatorRef, CFStringRef, APEndpointDescriptionRef, APSConnectionInterfaceManagerRef, APSenderSessionUsage, APSClusterType, dispatch_queue_t, Boolean, Boolean, Boolean, APSNetworkClockRef, CFStringRef, CFStringRef, Boolean, double, CFDictionaryRef, APSWrapperRef, APSWrapperRef, APSenderSessionRef *)"
+ "OSStatus AirPlayDebugIPCEnableForEndpointManager(FigEndpointManagerRef, CFStringRef)"
+ "OSStatus airPlayDescription_updateWithAdvertiserAndPSGInfosNotifyingClients(APEndpointDescriptionRef, APAdvertiserInfoRef, CFDictionaryRef, CFMutableDictionaryRef)"
+ "OSStatus apPlayback_BroadcastCoordinatedPlaybackState(FigEndpointPlaybackSessionRef, CFStringRef, CFDictionaryRef)"
+ "OSStatus audioEngineBufferedAdapter_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus audioEngineBufferedAdapter_Flush(FigEndpointStreamAudioEngineRef, CFDictionaryRef)"
+ "OSStatus audioEngineBufferedAdapter_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus audioEngineBufferedAdapter_SetRateAndAnchorTime(FigEndpointStreamAudioEngineRef, CMTime)"
+ "OSStatus audioStream_createAndResumeTransportBufferedAudioDataStream(FigEndpointStreamRef, APSenderSessionRef, int, APTransportStreamType, APTransportConnectionTransportProtocol, FigTransportStreamRef *)"
+ "OSStatus audioStream_handleCommandSetMode(FigEndpointStreamRef, CFDictionaryRef)"
+ "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, CFNumberRef, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, APTransportStreamType, CFDataRef, Boolean, APTransportConnectionTransportProtocol, uint64_t *, uint64_t *, Boolean *, int *, int32_t *, int *, CFDataRef *)"
+ "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, int, CFDictionaryRef, APSAudioFormatDescriptionRef, Boolean, CFDataRef, uint64_t, uint64_t *, int *, int *, CFDictionaryRef *, int *, uint32_t *, APSCryptorRef *)"
+ "OSStatus browserController_registerInternalClientNeedsDiscovery(void *)"
+ "OSStatus bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal(void *)"
+ "OSStatus bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacyInternal(void *)"
+ "OSStatus bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal(void *)"
+ "OSStatus bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal(void *)"
+ "OSStatus bufferedAudioEngine_flushWithinSampleRangeInternal(void *)"
+ "OSStatus bufferedAudioEngine_initProtocolDriverIfNecessary(FigEndpointStreamAudioEngineRef, CFStringRef, Boolean *)"
+ "OSStatus bufferedAudioEngine_pruneMessageRingToCurrentRemoteMediaTimeWithForwardMargin(FigEndpointStreamAudioEngineRef, CMTime)"
+ "OSStatus bufferedAudioEngine_removeHose(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, APSEndpointStreamAudioHoseRef)"
+ "OSStatus bufferedAudioEngine_sendFlushWithinSampleRangeInternal(FigEndpointStreamAudioEngineRef, uint16_t, uint32_t, uint32_t, CMTime, uint32_t, uint32_t, CMTime)"
+ "OSStatus carEndpoint_CreatePlaybackSession(FigEndpointRef, FigEndpointPlaybackSessionRef *)"
+ "OSStatus carEndpoint_UpdateFeaturesWithCompletionCallback(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus carEndpoint_activateInternal(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)"
+ "OSStatus carEndpoint_activateInternal(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke"
+ "OSStatus carEndpoint_activateInternal(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke_2"
+ "OSStatus carEndpoint_activateInternal(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke_3"
+ "OSStatus carEndpoint_copyNonStateProperty(FigEndpointRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus carEndpoint_createPlaybackSessionInternal(FigEndpointRef, FigEndpointPlaybackSessionRef *)_block_invoke"
+ "OSStatus carEndpoint_registerForHTTPProxy(FigEndpointRef, APSenderSessionRef, uint32_t)"
+ "OSStatus carEndpoint_registerForHTTPProxy(FigEndpointRef, APSenderSessionRef, uint32_t)_block_invoke"
+ "OSStatus carEndpoint_updateVideoPlaybackAllowed(FigEndpointRef, CFDictionaryRef, Boolean)"
+ "OSStatus carEndpoint_validateEnabledFeaturesWithAccessory(FigEndpointRef, CFDictionaryRef)"
+ "OSStatus coreUtilsPairing_performSetupInternal(APPairingClientRef, const CFStringRef, APPairingType, Boolean, Boolean, CFStringRef, CFStringRef *, CFDataRef *, CFDataRef *, CFTypeRef *)"
+ "OSStatus coreUtilsPairing_sendPairSetupRequest(APPairingClientRef, APPairingType, Boolean, CFStringRef, const uint8_t *, size_t, CMBlockBufferRef *)"
+ "OSStatus emp_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus emp_CopyRemoteControlDepotEndpoint(FigEndpointManagerRef, FigEndpointRef *)"
+ "OSStatus emp_CreateAggregateEndpoint(FigEndpointManagerRef, FigEndpointAggregateType, FigEndpointRef *)"
+ "OSStatus emp_Invalidate(CMBaseObjectRef)"
+ "OSStatus emp_SetDiscoveryMode(FigEndpointManagerRef, CFStringRef, CFDictionaryRef)"
+ "OSStatus emp_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus emp_addCachedSubEndpoint(FigEndpointManagerRef, FigEndpointRef, CFDictionaryRef)"
+ "OSStatus emp_addEndpoint(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType)"
+ "OSStatus emp_demoteSubEndpoints(FigEndpointManagerRef, FigEndpointRef)"
+ "OSStatus emp_ensureCachedEndpointWithType(FigEndpointManagerRef, CFDictionaryRef, CFStringRef, APEndpointPlusType)"
+ "OSStatus emp_ensureRealEndpointWithType(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType)"
+ "OSStatus emp_removeCachedSubEndpoint(FigEndpointManagerRef, FigEndpointRef, CFStringRef)"
+ "OSStatus emp_removeEndpoint(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
+ "OSStatus emp_removeRealEndpointWithType(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
+ "OSStatus emp_reportEndpointToCache(FigEndpointManagerRef, FigEndpointRef)"
+ "OSStatus emp_setupCache(FigEndpointManagerRef)_block_invoke_3"
+ "OSStatus emp_syncSubEndpointAvailable(FigEndpointManagerRef, FigEndpointRef, NSMutableDictionary *, NSMutableDictionary *)"
+ "OSStatus emp_syncSubEndpointRemovals(FigEndpointManagerRef, FigEndpointRef, NSMutableDictionary *, NSMutableDictionary *)"
+ "OSStatus endpointAggregate_copyFromActivationOptionsOrCreateGroupID(FigEndpointRef, CFDictionaryRef, CFStringRef *, Boolean *)"
+ "OSStatus endpointUGLWrapper_activateInternal(EndpointActivationCallbackContext *)"
+ "OSStatus endpointUGLWrapper_createWrappedEndpoint(FigEndpointRef, FigEndpointRef *)"
+ "OSStatus endpointUGLWrapper_deactivateInternal(FigEndpointRef, FigEndpointRef, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus endpointUGLWrapper_deactivateInternal(FigEndpointRef, FigEndpointRef, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)_block_invoke"
+ "OSStatus endpointUGLWrapper_updateMXDescriptor(FigEndpointRef, CFAllocatorRef, CFDictionaryRef *)"
+ "OSStatus endpoint_copyExternalPlaybackCompetingStreams(FigEndpointRef, CFTypeRef *)"
+ "OSStatus endpoint_copyUsesExternalPlaybackByDefault(FigEndpointRef, CFTypeRef *)"
+ "OSStatus endpoint_createAuthorizationSemaphore(FigEndpointRef, dispatch_semaphore_t *)"
+ "OSStatus endpoint_createSenderSession(FigEndpointRef, APSConnectionInterfaceManagerRef, CFStringRef, FigEndpointFeatures, Boolean, Boolean, Boolean, Boolean, Boolean, APSClusterType, APSNetworkClockRef, CFStringRef, CFStringRef, Boolean, double, APSenderSessionFactoryRef, CFDictionaryRef, APSWrapperRef, APSWrapperRef, APSenderSessionRef *)"
+ "OSStatus endpoint_handleAuthorizationRequired(FigEndpointRef, CFStringRef, uint64_t, APEndpointActivationStage, CFStringRef *)"
+ "OSStatus endpoint_updateUGLRCServerIfNeeded(FigEndpointRef, APSenderSessionRef, CFStringRef, Boolean)"
+ "OSStatus endpointdelegate_setIsMuted(FigEndpointRef, Boolean, Boolean, Boolean)"
+ "OSStatus endpointdelegate_setVolumeSliderInternal(FigEndpointRef, Float32, Boolean, Boolean, Boolean, Boolean)"
+ "OSStatus endpointdelegate_translateIsMutedToVolumeOperation(FigEndpointRef, Boolean, Boolean)"
+ "OSStatus epp_AcquireAndCopyResource(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef, CFTypeRef *)"
+ "OSStatus epp_ActivateForFeaturesWithCompletionCallback(FigEndpointRef _Nonnull, FigEndpointFeatures, CFDictionaryRef _Nullable, FigEndpointActivationCompletionCallback _Nullable, void * _Nullable)"
+ "OSStatus epp_BorrowScreen(FigEndpointExtendedRef, CFStringRef, CFStringRef)"
+ "OSStatus epp_CloseCommChannel(FigEndpointExtendedRef, CFStringRef)"
+ "OSStatus epp_CopyCurrentViewArea(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef *)"
+ "OSStatus epp_CopyHIDInputMode(FigEndpointExtendedRef, CFStringRef, CFAllocatorRef, CFNumberRef *)"
+ "OSStatus epp_CreateCommChannel(FigEndpointExtendedRef, CFDictionaryRef, CFStringRef *)"
+ "OSStatus epp_CreatePlaybackSession(FigEndpointRef, FigEndpointPlaybackSessionRef *)"
+ "OSStatus epp_CreateRemoteControlSession(FigEndpointExtendedRef, CFDictionaryRef, FigEndpointRemoteControlSessionRef *)"
+ "OSStatus epp_DeactivateWithCompletionCallback(FigEndpointRef _Nonnull, CFDictionaryRef _Nullable, FigEndpointActivationCompletionCallback _Nullable, void * _Nullable)"
+ "OSStatus epp_DisableBluetooth(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef)"
+ "OSStatus epp_DuckAudio(FigEndpointExtendedRef, CFDictionaryRef)"
+ "OSStatus epp_EnsureAuthorizedWithCompletionCallback(FigEndpointRef _Nonnull, CFDictionaryRef _Nullable, FigEndpointCompletionCallback _Nonnull, void * _Nullable)"
+ "OSStatus epp_RelinquishResource(FigEndpointExtendedRef, CFStringRef, CFTypeRef)"
+ "OSStatus epp_RequestCarUI(FigEndpointExtendedRef, CFStringRef, CFURLRef)"
+ "OSStatus epp_RequestViewArea(FigEndpointExtendedRef, CFStringRef, CFIndex)"
+ "OSStatus epp_SendCommand(FigEndpointExtendedRef, CFStringRef, CFDictionaryRef, FigEndpointSendCommandCompletionCallback, void *)"
+ "OSStatus epp_SendData(FigEndpointExtendedRef, CFStringRef, CFDataRef, FigEndpointSendDataCompletion, void *)"
+ "OSStatus epp_SetHIDInputMode(FigEndpointExtendedRef, CFStringRef, CFNumberRef)"
+ "OSStatus epp_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus epp_TakeScreen(FigEndpointExtendedRef, CFStringRef, CFStringRef)"
+ "OSStatus epp_UnborrowScreen(FigEndpointExtendedRef, CFStringRef, CFStringRef)"
+ "OSStatus epp_UpdateFeaturesWithCompletionCallback(FigEndpointRef _Nonnull, FigEndpointFeatures, CFDictionaryRef _Nullable, FigEndpointActivationCompletionCallback _Nonnull, void * _Nullable)"
+ "OSStatus epp_addSubEndpoint(FigEndpointRef, FigEndpointRef)"
+ "OSStatus epp_copyCachedClusterProperty(FigEndpointRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus epp_copyCachedDescriptionProperty(FigEndpointRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus epp_copyEndpointPropertyToDestination(FigEndpointRef, FigEndpointRef, CFStringRef, void *)"
+ "OSStatus epp_removeSubEndpoint(FigEndpointRef, CFStringRef)"
+ "OSStatus epp_setDescriptionProperty(FigEndpointRef, CFStringRef, CFTypeRef)"
+ "OSStatus epp_setInner(FigEndpointRef, FigEndpointRef)"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_2"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_5"
+ "OSStatus manager_createAndAddUGLWrapperEndpoint(FigEndpointManagerRef, CFStringRef, FigEndpointRef *)"
+ "OSStatus manager_updateEndpoint(FigEndpointManagerRef, APTransportDeviceRef, FigEndpointRef)"
+ "OSStatus mcs_BroadcastCoordinatedPlaybackState(FigEndpointPlaybackSessionRef, CFStringRef, CFDictionaryRef)"
+ "OSStatus multicastProbeSender_create(CFDictionaryRef, APMulticastProbeSenderRef *)"
+ "OSStatus multicastProbeSender_createEncryptionKeyAndCryptor(APMulticastProbeSenderRef, CFDataRef *, APSCryptorRef *)"
+ "OSStatus multicastProbeSender_createMulticastGroupInfo(APMulticastProbeSenderRef, CFStringRef, sa_family_t, CFDictionaryRef *)"
+ "OSStatus multicastProbeSender_decrementRefCountForSSMGroupInfo(APMulticastProbeSenderRef, CFStringRef, CFMutableDictionaryRef)"
+ "OSStatus multicastProbeSender_incrementRefCountForSSMGroupInfo(APMulticastProbeSenderRef, CFStringRef, CFMutableDictionaryRef)"
+ "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, const char *, sa_family_t)"
+ "OSStatus multicastProbeSender_updateTxProbePacketsForClients(CMBaseObjectRef, int)_block_invoke"
+ "OSStatus realTimeAudioEngine_setTransportAudioFormatInternal(FigEndpointStreamAudioEngineRef, AudioStreamBasicDescription *)"
+ "OSStatus realTimeAudioEngine_tas_ResumeInternal(APRTAETranscoderAndSender *, APSAudioFormatDescriptionRef, FigEndpointAudioSourceRef, APSCryptorRef, CMClockRef, CMTimebaseRef, CMTimebaseRef, APSRTPPacketHandlerRef, APTransportStreamSendBackingProviderRef, APMessageRingRef, APMessageRingRef)"
+ "OSStatus sbpd_createUserDataBBuf(SBufProcessingData *, CMSampleBufferRef, CMBlockBufferRef *)"
+ "OSStatus screenstreamudp_resumeInternal(FigEndpointStreamRef, CFDictionaryRef, StreamScreenUDPCompletionContext)"
+ "OSStatus screenstreamudp_setupStream(FigEndpointStreamRef, StreamScreenUDPCompletionContext)"
+ "OSStatus screenstreamudp_suspendInternal(FigEndpointStreamRef, CFDictionaryRef, StreamScreenUDPCompletionContext)"
+ "OSStatus session_AuthorizeItem(FigEndpointPlaybackSessionRef, CFDataRef, CFStringRef, FigEndpointPlaybackSessionAuthorizeItemCompletion, void *)"
+ "OSStatus session_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus session_GetPlaybackInfo(FigEndpointPlaybackSessionRef, FigEndpointPlaybackSessionGetPlaybackInfoCompletion, void *)"
+ "OSStatus session_GetProxiedProperty(FigEndpointPlaybackSessionRef, CFStringRef, CFDictionaryRef, FigEndpointPlaybackSessionGetProxiedPropertyCompletion, void *)"
+ "OSStatus session_Invalidate(CMBaseObjectRef)"
+ "OSStatus session_PerformRemoteAction(FigEndpointPlaybackSessionRef, CFStringRef, CFTypeRef, FigEndpointPlaybackSessionRemoteActionCompletion, void *)"
+ "OSStatus session_Play(FigEndpointPlaybackSessionRef, CFDictionaryRef, FigEndpointPlaybackSessionStandardCompletion, void *)"
+ "OSStatus session_SeekToDate(FigEndpointPlaybackSessionRef, CFDateRef, CFDictionaryRef, FigEndpointPlaybackSessionSeekCompletion, void *)"
+ "OSStatus session_SeekToTime(FigEndpointPlaybackSessionRef, CMTime, CFDictionaryRef, FigEndpointPlaybackSessionSeekCompletion, void *)"
+ "OSStatus session_SetEventHandler(FigEndpointPlaybackSessionRef, FigEndpointPlaybackSessionHandleEvent, void *, CFTypeRef)"
+ "OSStatus session_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus session_ensureRemoteControlSessionCreated(FigEndpointPlaybackSessionRef)"
+ "OSStatus session_setProxiedPropertyInternal(FigEndpointPlaybackSessionRef, CFStringRef, CFDictionaryRef, CFTypeRef)"
+ "Object invalidated"
+ "Open NAN Full"
+ "Open NAN full"
+ "Open NAN partial"
+ "PCM/48000/16/9.1.6"
+ "PCM/48000/32f/9.1.6"
+ "PROMOTE"
+ "PWDEncryptorEncryptionKeyID"
+ "Password"
+ "PlaybackStateType"
+ "Port"
+ "PrefersAPAT"
+ "Private"
+ "Processed command %@, result = %d\n"
+ "RCServerInfo"
+ "REMOVE"
+ "RealEndpointsChanged"
+ "Reason"
+ "ReceiverMessageProcessingMs"
+ "RegisterHTTPProxyMonitor: key = %{ptr},  err = %#m"
+ "Removed"
+ "Returned from CRFetchScaledDisplaysForCertificateSerialNumber\n"
+ "SPPCPlayback"
+ "ScreenCapture"
+ "ScreenCaptureControl"
+ "ScreenSpatialAudioSender"
+ "Secure NAN partial"
+ "SenderSession:[%{ptr}] (%s) Parent:[%{ptr}]\n"
+ "Sent a probe packet on interface[%s] bytesSent=%d"
+ "Set discovery mode to %@; result %d\n"
+ "ShouldUseNANDiversifiedPIN"
+ "SidePlay"
+ "SingleReceiverPlayback"
+ "Started UGL-RCServer result %#m"
+ "Starting UGL-RCServer"
+ "Stopped UGL-RCServer result = %#m"
+ "Stopping UGL-RCServer"
+ "SupportsAPAP"
+ "SupportsAPAT"
+ "SupportsAnyMedia"
+ "SupportsBufferedAPAT"
+ "SupportsSharedReceiverClock"
+ "SupportsUGLAssistedDiscovery"
+ "SupportsV2ArtworkMetadata"
+ "TCPPacing"
+ "TimeToConnectMs"
+ "TotalMessageTimeMs"
+ "TransportProtocol"
+ "Type:                %@\n"
+ "UGL iPhone"
+ "UGLRCServerUpdateCallback"
+ "UGLServerInfoAdded"
+ "UGLSessionActiveDidChange"
+ "UN1/Ut4OFbgwIQw"
+ "UPDATE"
+ "Unrecognized command: %@\n"
+ "UnregisterHTTPProxyMonitor: key = %{ptr},  err = %#m"
+ "UnspecifiedRemoteTimeMs"
+ "Updated"
+ "Updated active streamConnectionIDs: [\n"
+ "Usage: %s <mode>\n"
+ "Usage: %s <start|stop>\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr>\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr> <command> [key1:type1:val1] [key2:type2:val2] ...\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr> <features> [key1:type1:val1] [key2:type2:val2] ...\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr> <propertyKey> <propertyValue>\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr> <subEndpointID> <propertyKey>\n"
+ "Usage: %s [-r|w] <name|ID|hash|ptr> <subEndpointID> <propertyKey> <propertyValue>\n"
+ "Usage: %s [-r|w] [desc@]<name|ID|hash|ptr|-> <propertyKey>\n"
+ "UseAPAT"
+ "Using cache promotion deadline duration of %llums %s"
+ "WHAInstantDiscovery_Caching"
+ "WHAInstantDiscovery_ThrottleReduction"
+ "WHAPrimingOptimization"
+ "WantsCacheEviction"
+ "X-Apple-NANMACAddress"
+ "X-Apple-UsingNANDiversifiedPINAsSetupCode"
+ "ZoomFactor"
+ "[%{ptr}] %###s called: PICRequest [%@], ItemUUID [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: date [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: handler [%{ptr}], context [%{ptr}], clientRef [%@]\n"
+ "[%{ptr}] %###s called: item [%@], afterItem [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: item [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: params [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: propertyKey [%@], params [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: propertyKey [%@], params [%@], value [%@]\n"
+ "[%{ptr}] %###s called: propertyKey [%@], propertyValue [%@]\n"
+ "[%{ptr}] %###s called: rate [%.3f], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: time [%.3f], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s called: type [%@], params [%@], completion [%{ptr}], context [%{ptr}]\n"
+ "[%{ptr}] %###s ended\n"
+ "[%{ptr}] %###s: UGL TODO: Update transport for endpoint [%{ptr}], transport %@\n"
+ "[%{ptr}] %@ stream not found.\n"
+ "[%{ptr}] %@: %@"
+ "[%{ptr}] %s %s Plus [%{ptr}] %@ %'@"
+ "[%{ptr}] %s UGL-RCServer Info (err %#m)"
+ "[%{ptr}] %s subEndpointPlus [%{ptr}] %@ for clusterPlus [%{ptr}] %@"
+ "[%{ptr}] <APUGL> HandleShadowEndpoint: groupID %@ for discoveryID %@ matches local server groupID; ignore it"
+ "[%{ptr}] <APUGL> Setting uglServerInfo from endpoint [%{ptr}]%?{end}: %@"
+ "[%{ptr}] <APUGL> handleBrowserAddOrUpdate create RC for local device, discoveryID %@"
+ "[%{ptr}] <APUGL> handleBrowserAddOrUpdate for discoveryID %@"
+ "[%{ptr}] <APUGL> handleBrowserAddOrUpdate handle; isRC=%s, requiredAPFeatures=%s, addAP=%s, addRC=%s"
+ "[%{ptr}] <APUGLActivation> Activating shadow endpoint [%{ptr}]"
+ "[%{ptr}] <APUGLActivation> Activating wrapped endpoint [%{ptr}]"
+ "[%{ptr}] <APUGLActivation> Couldn't activate wrapper because no wrapped endpoint after attempting shadow endpoints"
+ "[%{ptr}] <APUGLActivation> Deactivating shadow endpoint [%{ptr}], status %#m"
+ "[%{ptr}] <APUGLActivation> Deactivating wrapped endpoint [%{ptr}]"
+ "[%{ptr}] <APUGLActivation> Overall deactivation complete (seed %llu), result %#m; calling callback on behalf of wrapper"
+ "[%{ptr}] <APUGLActivation> Shadow endpoint [%{ptr}] activation complete (seed %llu), result %#m; activating next shadow or wrapped endpoint"
+ "[%{ptr}] <APUGLActivation> Wrapped endpoint [%{ptr}] activation complete (seed %llu), result %#m; calling callback on behalf of wrapper"
+ "[%{ptr}] <APUGLActivation> deactivateInternal, wrapped: [%{ptr}]"
+ "[%{ptr}] <APUGLActivation> uglWrapper_freeEndpointActivationContext [%{ptr}] freed"
+ "[%{ptr}] <APUGLActivation> uglWrapper_freeEndpointDeactivationContext [%{ptr}] freed"
+ "[%{ptr}] <PWDKeyExchange> Done pre-roll: %#m.\n"
+ "[%{ptr}] <PWDKeyExchange> Scheduling pre-roll.\n"
+ "[%{ptr}] <PWDKeyExchange> Starting pre-roll.\n"
+ "[%{ptr}] APAT %s supported across all substreams."
+ "[%{ptr}] APEndpointUGLWrapperUpdateWithTransportDevice(%@, forWrapped=%s)"
+ "[%{ptr}] APMulticastProbeSenderUpdateMC2UC deviceName=%@, probeBurstID=%u, mc2ucStatus=%d packetCount=%d\n"
+ "[%{ptr}] AcquireAndCopyResource(%@, ...)"
+ "[%{ptr}] Activate with inner [%{ptr}] context %@"
+ "[%{ptr}] ActivateForFeaturesWithCompletionCallback(0x%llx)"
+ "[%{ptr}] Activated shadow endpoints: %ld"
+ "[%{ptr}] Activation %s. Duration: %llu ms%?@, correlationID: %'@\n"
+ "[%{ptr}] Activation callback with inner [%{ptr}] context %@ forward? %s"
+ "[%{ptr}] Actively using APAT, but no longer supported across all substreams. Posting 'ActiveConfigurationDidBecomeInvalid'!"
+ "[%{ptr}] Add subEndpointPlus [%{ptr}] %@"
+ "[%{ptr}] AddShadowEndpoint(%@ -> [%{ptr}], RC [%{ptr}])"
+ "[%{ptr}] Adding UGL wrapper [%{ptr}] for groupID %@"
+ "[%{ptr}] Adding discoveryID %@ -> UGL wrapper [%{ptr}]"
+ "[%{ptr}] An entry already exists for device='%@'\n"
+ "[%{ptr}] An entry already exists for ifaceName_addressFamily='%@', socket=%d\n"
+ "[%{ptr}] Appending other shadow [%{ptr}]"
+ "[%{ptr}] Appending peer list (size: %d) to SETUP Request%?{end}: %@\n%@"
+ "[%{ptr}] Authorization failed with err=%#m"
+ "[%{ptr}] Authorization request completion callback for inner %s [%{ptr}] result %#m"
+ "[%{ptr}] Authorization request completion callback with result = %#m"
+ "[%{ptr}] Available %s IDs: %@"
+ "[%{ptr}] BorrowScreen(%@, %@)"
+ "[%{ptr}] Cancel cache promotion deadline"
+ "[%{ptr}] CarPlay videoPlayback supported: %s\n"
+ "[%{ptr}] CarPlay videoPlayback: Sender does not support CarPlay video, not expected to see in featureList from setup response"
+ "[%{ptr}] ChaCha Cryptor created with shared key\n"
+ "[%{ptr}] Cleared socketList.\n"
+ "[%{ptr}] CloseAllCommChannels"
+ "[%{ptr}] CloseCommChannel(%@)"
+ "[%{ptr}] Closed socket[%d] for key='%@'\n"
+ "[%{ptr}] Completion callback with inner [%{ptr}] context %@ forward? %s"
+ "[%{ptr}] CopyProperty for key %@\n"
+ "[%{ptr}] CopyProperty returning %#m\n"
+ "[%{ptr}] CopyProperty(%@)"
+ "[%{ptr}] CopyProperty: %@"
+ "[%{ptr}] CopyRemoteControlDepotEndpoint"
+ "[%{ptr}] Couldn't get endpointDescription from endpoint [%{ptr}]"
+ "[%{ptr}] CreateAggregateEndpoint type %u"
+ "[%{ptr}] CreateCommChannel()"
+ "[%{ptr}] CreatePlaybackSession"
+ "[%{ptr}] CreateRemoteControlSession()"
+ "[%{ptr}] Created APEndpointManagerPlus type %u"
+ "[%{ptr}] Created APEndpointPlus %s"
+ "[%{ptr}] Created APEndpointUGLWrapper, wrapping [%{ptr}] with ID %@"
+ "[%{ptr}] Created APMulticastProbeSender\n"
+ "[%{ptr}] Created wrapped endpoint [%{ptr}] for deviceID %@/%lu"
+ "[%{ptr}] Deactivate with inner [%{ptr}] context %@"
+ "[%{ptr}] DeactivateWithCompletionCallback"
+ "[%{ptr}] Deactivating shadow endpoint [%{ptr}] before dissociating"
+ "[%{ptr}] Deactivation callback (seed %llu) - could not find shadow endpoint [%{ptr}] to remove"
+ "[%{ptr}] Deactivation callback (seed %llu) - matched shadowEndpoint [%{ptr}], result %#m"
+ "[%{ptr}] Deactivation callback (seed %llu) - matched wrappedEndpoint [%{ptr}], result %#m"
+ "[%{ptr}] Disable RC connection preference is %s"
+ "[%{ptr}] Display description count: %d\n"
+ "[%{ptr}] Dissociate"
+ "[%{ptr}] DuckAudio(%@)"
+ "[%{ptr}] Ensure Authorized with inner [%{ptr}] context %@"
+ "[%{ptr}] EnsureAuthorizedWithCompletionCallback"
+ "[%{ptr}] Error %#m occurred when updating active streamConnectionIDs"
+ "[%{ptr}] Establish PTP Clock=%s (isClusterLeader=%s isHTSession=%s isSPPCSession=%s isStereoBuddyConnection=%s)"
+ "[%{ptr}] Failed to activate cache: %@"
+ "[%{ptr}] Failed to add MC2UC group info with err=%#m\n"
+ "[%{ptr}] Failed to allocate array for message\n"
+ "[%{ptr}] Failed to create socket with err=%#m\n"
+ "[%{ptr}] Failed to create wrapped endpoint, result %#m"
+ "[%{ptr}] Failed to encrypt probing msg\n"
+ "[%{ptr}] Failed to form msg data\n"
+ "[%{ptr}] Failed to get %@ from the stream description: %@"
+ "[%{ptr}] Failed to register [%@] for MC2UC detection, error=%#m.\n"
+ "[%{ptr}] Failed to register device for MC2UC detection.\n"
+ "[%{ptr}] Failed to remove reference for < interfaceName_addressFamily, <socket, SSM group info> >.\n"
+ "[%{ptr}] Failed to retrieve the socket fd for ifaceName_addressFamily='%@' with err=%#m\n"
+ "[%{ptr}] Failed to send MC2UC probe packets.\n"
+ "[%{ptr}] Failed to send inParameters from HTTPProxyMonitor to HU: %#m"
+ "[%{ptr}] Failed to stop UGL-RCServer (err: %#m)"
+ "[%{ptr}] Failing authorization as activation seed has changed during authorization."
+ "[%{ptr}] Failing authorization as activation seed has changed prior to authorization."
+ "[%{ptr}] Failing authorization as activation stage has changed during authorization."
+ "[%{ptr}] Failing authorization as activation stage has changed prior to authorization."
+ "[%{ptr}] Failing authorization as routing delegate went away."
+ "[%{ptr}] Feedback received, \"statsDictionary\":\n %@"
+ "[%{ptr}] Feedback received, \"statsDictionary\": numStaleStreams: %u"
+ "[%{ptr}] Finalize"
+ "[%{ptr}] Finalize with inner [%{ptr}] type %@"
+ "[%{ptr}] Finalize with inner [%{ptr}] type %u"
+ "[%{ptr}] Forward inner notification %@%?{end} payload %@"
+ "[%{ptr}] Get RCS message [%@]\n"
+ "[%{ptr}] Handle cache promotion deadline"
+ "[%{ptr}] HandleShadowEndpoint: add groupID %@, wrapperEndpoint [%{ptr}], discoveryID %@"
+ "[%{ptr}] HandleShadowEndpoint: no groupID %@ for discoveryID %@"
+ "[%{ptr}] HandleShadowEndpoint: no wrapperEndpoint for discoveryID %@"
+ "[%{ptr}] HandleShadowEndpoint: remove wrapperEndpoint [%{ptr}], discoveryID %@ - shouldAdd=%s, isUGLActive=%s"
+ "[%{ptr}] InsertPlayQueueItem params: %@\n"
+ "[%{ptr}] Inserting HPshadow [%{ptr}] at %ld"
+ "[%{ptr}] Inserting local RC shadow [%{ptr}] at front"
+ "[%{ptr}] Invalid endpoint activation state; ignoring authorization completion callback"
+ "[%{ptr}] Invalidate with inner [%{ptr}] type %@"
+ "[%{ptr}] Invalidating %@ (invalid=%s usage=%s)"
+ "[%{ptr}] Invalidating.\n"
+ "[%{ptr}] IsEmpty(wrapped [%{ptr}], shadow count %ld) returns %s"
+ "[%{ptr}] MC2UC - Decrement the ref count for interface=%@ by 1\n"
+ "[%{ptr}] MC2UC - Unregistered device name=%@\n"
+ "[%{ptr}] MC2UC - Unregistering device name=%@\n"
+ "[%{ptr}] MC2UC Successfully registered device='%@'\n"
+ "[%{ptr}] MC2UC added entry for interface_family [%@]\n"
+ "[%{ptr}] MDE request '%C'\n"
+ "[%{ptr}] Mc2UcDetectionEnabled=%d, isGroupPlaybackSession=%d, interfaceName=%@"
+ "[%{ptr}] MediaData disconnected, suspending...\n"
+ "[%{ptr}] Most likely stale callback, currentActivationSeed %d vs captured activationSeed %d"
+ "[%{ptr}] No auth delegate set."
+ "[%{ptr}] PWD configured, no AVConference based mirroring ('AVConferenceSupportsPWD' not enabled)\n"
+ "[%{ptr}] PWD key exchange failed with error %#m - continuing without protection\n"
+ "[%{ptr}] PWDKeyExchangeSender HandleFailure called with status %#m"
+ "[%{ptr}] PlaybackCoordinationMedium state broadcasting not supported"
+ "[%{ptr}] Posting %@%?{end} %@"
+ "[%{ptr}] Posting %@%?{end} payload %@"
+ "[%{ptr}] Prefers using APAT, and APAT now supported across all substreams. Posting 'ActiveConfigurationDidBecomeInvalid'!"
+ "[%{ptr}] RCEndpointDescriptionChanged for rc/shadow endpoint [%{ptr}], uglSessionActive did change/serverInfoAdded"
+ "[%{ptr}] RCS ref creation complete for: %@, err = %m\n"
+ "[%{ptr}] Received MC2UC feedback from [%@] MC2UCProbeBurstID=%d, TimeToDetect(RTT)=%dms, MC2UCStatus=%s.\n"
+ "[%{ptr}] Reconfirming device on connection failure %#m...\n"
+ "[%{ptr}] Registering device name=%@, interface=%@ for MC2UC probing.\n"
+ "[%{ptr}] RelinquishResource(%@, [%{ptr}])"
+ "[%{ptr}] Remove UGL wrapper [%{ptr}] if empty"
+ "[%{ptr}] Remove subEndpointPlus [%{ptr}] %@"
+ "[%{ptr}] RemoveShadowEndpoint(%@ -> RC [%{ptr}])"
+ "[%{ptr}] RemoveShadowEndpoint(%@ -> [%{ptr}])"
+ "[%{ptr}] RemoveShadowEndpoint: couldn't find groupID from wrapperEndpoint [%{ptr}]"
+ "[%{ptr}] RemoveShadowEndpoint: couldn't find wrapperEndpoint for discoveryID %@"
+ "[%{ptr}] RemoveShadowEndpointFromUGLWrapper: Removing UGL wrapper [%{ptr}] for groupID %@"
+ "[%{ptr}] RemoveShadowEndpointFromUGLWrapper: wrapperEndpoint [%{ptr}], discoveryID %@"
+ "[%{ptr}] Report (remote) audio performance: protVer=%u sessionDuration=%u[s] renderDeadlineMin=%lld[ms] isLiveAdaptive=%s %@"
+ "[%{ptr}] Report MC2UC KPIs for [%@]:\n"
+ "[%{ptr}] Report to cache info for %'@"
+ "[%{ptr}] Requesting delegate to handle authorization"
+ "[%{ptr}] Requesting delegate to handle authorization for inner %s [%{ptr}]%?{end} inner subEndpoint [%{ptr}]"
+ "[%{ptr}] Restart cache promotion deadline (%llums)"
+ "[%{ptr}] Running custom test with params %@\n"
+ "[%{ptr}] Screen stream doesn't exist during copy property %s\n"
+ "[%{ptr}] Send Command callback with inner [%{ptr}] context %@ forward? %s"
+ "[%{ptr}] Send Command with inner [%{ptr}] context %@"
+ "[%{ptr}] Send Data callback with inner [%{ptr}] context %@ forward? %s"
+ "[%{ptr}] Send Data with inner [%{ptr}] context %@"
+ "[%{ptr}] SendCommand(%@)"
+ "[%{ptr}] SendData(%@)"
+ "[%{ptr}] Sending AirPlay Signposts to Timestore: %@"
+ "[%{ptr}] Set authorization string%?s%?#m%?{end}, authString=%@"
+ "[%{ptr}] Set refCount=%d for key='%@'\n"
+ "[%{ptr}] SetDelegate([%{ptr}])"
+ "[%{ptr}] SetDelegateRemoteControl([%{ptr}])"
+ "[%{ptr}] SetDelegateRouting([%{ptr}])"
+ "[%{ptr}] SetDelegateVolumeAndMute([%{ptr}])"
+ "[%{ptr}] SetDiscoveryMode: %@ -> %@"
+ "[%{ptr}] SetProperty(%@)"
+ "[%{ptr}] SetProperty: %@"
+ "[%{ptr}] SetWrappedEndpoint: [%{ptr}] -> [%{ptr}]"
+ "[%{ptr}] Setting media presentation latency to %d ms and media presentation mode to %s.\n"
+ "[%{ptr}] Setting traffic registration options for AirPlay to ht group: %@.\n"
+ "[%{ptr}] Should%s establish Network Clock link%?{end} due to %s"
+ "[%{ptr}] Skipping PWD key exchange due to the lack of display protection support\n"
+ "[%{ptr}] Socket address %##a\n"
+ "[%{ptr}] SocketSetMulticastInterface failed with err=%#m\n"
+ "[%{ptr}] Starting teardown of the streams and the session, using HTTP timeout of %d sec (%s)"
+ "[%{ptr}] Teardown of session [%{ptr}] took %llu ms (err: %#m)\n"
+ "[%{ptr}] Timed out waiting for authorization completion after %u secs"
+ "[%{ptr}] UGL Session Active change: %s -> %s\n"
+ "[%{ptr}] UGL has ServerInfo change: %s -> %s\n"
+ "[%{ptr}] UnborrowScreen(%@, %@)"
+ "[%{ptr}] Unhandled copy cached cluster property: %@"
+ "[%{ptr}] Unhandled copy cached description property: %@"
+ "[%{ptr}] Update features with 0x%X; storage->videoPlaybackSupported %d; playbackSelected: %d\n"
+ "[%{ptr}] Update features with inner [%{ptr}] context %@"
+ "[%{ptr}] Updated Tx probe packet count for '%@' with TxProbePktsCount=%d.\n"
+ "[%{ptr}] Updated reference count=%d for key='%@'\n"
+ "[%{ptr}] Updating dynamic audio latency offset to %d ms\n"
+ "[%{ptr}] Updating media presentation mode to %s\n"
+ "[%{ptr}] Using random UUID for groupID: %@\n"
+ "[%{ptr}] Waiting for auth completion sema"
+ "[%{ptr}] We received an APAT message, but we are not using APAT\n"
+ "[%{ptr}] [TIMED %llums] %s"
+ "[%{ptr}] [probeBurstID=%u] keysDict = %@\n"
+ "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d \n"
+ "[%{ptr}] connect failed with err=%#m\n"
+ "[%{ptr}] copy %@: %@ err = %#m"
+ "[%{ptr}] copyClusterProperty %@"
+ "[%{ptr}] copyProperty(%@) failed to create MX descriptor with error %#m"
+ "[%{ptr}] copyProperty(%@) failed with error %#m"
+ "[%{ptr}] copyProperty(%@) returning PropertyNotSupported"
+ "[%{ptr}] created new RCS [%{ptr}]\n"
+ "[%{ptr}] creating playback session.\n"
+ "[%{ptr}] defaults write ssmGroupIPv4Addr=%@"
+ "[%{ptr}] defaults write ssmGroupIPv6Addr=%@"
+ "[%{ptr}] diff metadata [%@]\n"
+ "[%{ptr}] dissociating shadow endpoint [%{ptr}] after deactivating it (result %#m)"
+ "[%{ptr}] endpoint is no longer activated"
+ "[%{ptr}] endpoint is not activated during copy property %s\n"
+ "[%{ptr}] getsockname failed with err=%#m\n"
+ "[%{ptr}] inParameters from HTTPProxyMonitor are invalid (NULL)"
+ "[%{ptr}] inner is updated [%{ptr}] -> [%{ptr}]"
+ "[%{ptr}] internal client with identifier %@ does%s need discovery\n"
+ "[%{ptr}] new endpoint info: %@"
+ "[%{ptr}] not maintaining cache-only %s"
+ "[%{ptr}] pending auth operation already?"
+ "[%{ptr}] registerForMC2UCDetection [DeviceName '%@' - Supports MC2UCDetection=%d], isMC2UCDetectionEnabled=%d, isGroupPlayback=%d\n"
+ "[%{ptr}] sending artwork metadata \n"
+ "[%{ptr}] setDescriptionProperty: %@"
+ "[%{ptr}] sorted shadow endpoints: %ld"
+ "[%{ptr}] ssmGroupIPv4Addr=%##a"
+ "[%{ptr}] ssmGroupIPv6Addr=%##a"
+ "[%{ptr}] update %@%?{end} from %@ to %@"
+ "[%{ptr}] updateMXDescriptor: updated RouteUUID with our ID %@"
+ "[%{ptr}] videoPlaybackAllowed now changed to%s allowed\n"
+ "[%{ptr}] was requested to use APAT, but it is not supported!\n"
+ "[%{ptr}], message [%@], event.handler [%{ptr}], event.context [%{ptr}], clientRef [%@]\n"
+ "[0x%04X] APEndpointManagerPlus"
+ "[0x%04X]->[0x%04X] %s %@ '%@' %@"
+ "[APMulticastProbeSender %p]"
+ "]"
+ "^{OpaqueFigSimpleMutex=}"
+ "^{__CFDictionary=}"
+ "_desiredSockAddr"
+ "_dispatchQueue"
+ "_handleProxyParametersChanged"
+ "_hasDesiredSockAddr"
+ "_isWireless"
+ "_mutex"
+ "_nrDeviceID"
+ "_nrMonitor"
+ "_requesterDict"
+ "activate a specified endpoint"
+ "activateWithCompletion:"
+ "activateendpoint"
+ "activationConnectionMs"
+ "activationNetworkingMs"
+ "activationReceiverProcessingMs"
+ "activationSenderProcessingMs"
+ "addObjectsFromArray:"
+ "airPlayDescription_copyCarPlayVideoFeaturesInternal"
+ "airPlayDescription_hasCarPlayVideoFeatureInternal"
+ "allKeys"
+ "alloc failed"
+ "allowCacheableAirPlay"
+ "allowCacheableCluster"
+ "allowCacheableRemoteControl"
+ "appendFormat:"
+ "appendString:"
+ "apsession_copyActiveStreamConnectionIDs_block_invoke"
+ "apsession_copyStatePropertyInternal"
+ "apsession_ensureUsableLocalNetworkAddresses"
+ "apsession_isClusterSession"
+ "apsession_isTightSyncBuddyConnection"
+ "apsession_registerForMC2UCDetection"
+ "array"
+ "audioEngineBufferedAdapter_CopyProperty"
+ "audioEngineBufferedAdapter_CopyPropertyInternal"
+ "audioEngineBufferedAdapter_Flush"
+ "audioEngineBufferedAdapter_FlushData"
+ "audioEngineBufferedAdapter_Resume"
+ "audioEngineBufferedAdapter_ResumeInternal"
+ "audioEngineBufferedAdapter_SendData"
+ "audioEngineBufferedAdapter_SetEndpointStream"
+ "audioEngineBufferedAdapter_SetEndpointStreamInternal"
+ "audioEngineBufferedAdapter_SetProperty"
+ "audioEngineBufferedAdapter_SetRateAndAnchorTime"
+ "audioEngineBufferedAdapter_Suspend"
+ "audioEngineBufferedAdapter_SuspendInternal"
+ "audioStream_dataHoseAPATSignalRTCPDataAvailable"
+ "audioStream_dataHoseAPATSignalRTPDataAvailable"
+ "audioStream_dataHoseGetLastSentMediaTime"
+ "audioStream_receivedAudioDataMessage"
+ "audioStream_receivedMediaDataEventMessage"
+ "base64EncodedStringWithOptions:"
+ "bridge"
+ "bridge[0-9]+"
+ "bufferedAudioAdapter_VBRBitRate"
+ "bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseInternal"
+ "bufferedAudioEngine_audioHoseRegistrarDeregisterProtocolDriverHoseLegacyInternal"
+ "bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseInternal"
+ "bufferedAudioEngine_audioHoseRegistrarRegisterProtocolDriverHoseLegacyInternal"
+ "bufferedAudioEngine_audioTimer_block_invoke"
+ "bufferedAudioEngine_createAndResumeTickTimerInternal"
+ "bufferedAudioEngine_getFirstValidBufferTimestamp"
+ "bufferedAudioEngine_initProtocolDriverIfNecessary"
+ "bufferedAudioEngine_logProtocolDriverBufferFullness"
+ "bufferedAudioEngine_protocolDriverDescriptorDictionaryRelease"
+ "bufferedAudioEngine_protocolDriverDescriptorDictionaryRetain"
+ "bufferedAudioEngine_protocolDriverTickTimer"
+ "bufferedAudio_flushForwardLimitSecs"
+ "burstID"
+ "cachePromotionDeadlineDurationMs"
+ "can't find valid video track"
+ "carEndpoint_createPlaybackSessionInternal_block_invoke"
+ "carEndpoint_getOverrideCanvasSize"
+ "carEndpoint_postVideoPlaybackChangedNotification"
+ "carEndpoint_registerForHTTPProxy"
+ "carEndpoint_runTestCommand"
+ "carEndpoint_updateVideoPlaybackAllowed"
+ "carPlayForceHTTPProxyDisabled"
+ "changeVideoPlaybackToAudioOnly"
+ "clusterModel"
+ "componentsWithString:"
+ "connection already invalid"
+ "connection still valid"
+ "control UGL recevier"
+ "copyDescription"
+ "copySharedDeviceManager"
+ "couldn't create proxyParameters dictionary"
+ "currentPlaybackState"
+ "dataPacerMode"
+ "dataUsingEncoding:"
+ "deactivate a specified endpoint"
+ "deactivateendpoint"
+ "deviceHasUnpairedBluetooth:"
+ "deviceInfo argument is NULL"
+ "deviceInfoDidChange:deviceInfo:"
+ "deviceIsAsleepDidChange:isAsleep:"
+ "deviceIsClassCConnectedDidChange:isClassCConnected:"
+ "deviceIsCloudConnectedDidChange:isCloudConnected:"
+ "deviceIsConnectedDidChange:isConnected:"
+ "deviceIsEnabledDidChange:isEnabled:"
+ "deviceIsNearbyDidChange:isNearby:"
+ "deviceIsRegisteredDidChange:isRegistered:"
+ "deviceLinkTypeDidChange:linkType:"
+ "deviceLinkTypeDidChange:linkType:linkSubtype:"
+ "devicePluggedInStateDidChange:pluggedIn:"
+ "deviceProxyServiceInterfaceNameDidChange:interfaceName:"
+ "deviceThermalPressureLevelDidChange:thermalPressureLevel:"
+ "disableAPVideoForPWD"
+ "disableRCConnections"
+ "disableRCEndpoint: %s\n"
+ "dumpCryptorAuxDataAttachments"
+ "dynamicLatencyOffsetChanged"
+ "dynamicLatencyOffsetMs"
+ "emp_CopyProperty"
+ "emp_DumpHierarchy"
+ "emp_Invalidate"
+ "emp_addCachedSubEndpoint"
+ "emp_demoteSubEndpoints"
+ "emp_ensureCachedEndpointWithType"
+ "emp_ensureRealEndpointWithType"
+ "emp_filterAndAddNewlyAvailableRealEndpoints"
+ "emp_handleCacheEventFound"
+ "emp_handleCacheEventLost"
+ "emp_handleCacheFoundAirPlay"
+ "emp_handleCacheFoundCluster"
+ "emp_postNotification_block_invoke"
+ "emp_processAvailableEndpointChanges"
+ "emp_removeCachedEndpointWithType"
+ "emp_removeCachedSubEndpoint"
+ "emp_removeRealEndpointWithType"
+ "emp_reportEndpointToCache"
+ "emp_syncSubEndpointAvailable"
+ "emp_syncSubEndpointRemovals"
+ "emp_syncSubEndpoints"
+ "emp_syncSubEndpoints_createTable"
+ "enableCarPlayVideoPlayback"
+ "encoderEncryptionKeyID"
+ "endpointUGLWrapper_copyActivatedShadowEndpoints"
+ "endpointUGLWrapper_copySortedShadowEndpoints"
+ "endpointUGLWrapper_createMXDescriptor"
+ "endpointUGLWrapper_createWrappedEndpoint"
+ "endpointUGLWrapper_updateMXDescriptor"
+ "endpoint_authorizationRequestCompletionCallback"
+ "endpoint_collectMC2UCMetrics"
+ "endpoint_createAuthorizationDelegateCompletionContext"
+ "endpoint_createAuthorizationSemaphore"
+ "endpoint_createHandleNANAuthorizationRequestBlockWrapper"
+ "endpoint_createSetAuthorizationStringBlockWrapper"
+ "endpoint_createSetAuthorizationStringBlockWrapper_block_invoke"
+ "endpoint_handleAuthorizationRequired"
+ "endpoint_handleUpdateMC2UCStatus"
+ "endpoint_updateUGLRCServerIfNeeded"
+ "epp_AcquireAndCopyResource"
+ "epp_ActivateForFeaturesWithCompletionCallback"
+ "epp_BorrowScreen"
+ "epp_CloseCommChannel"
+ "epp_CopyCurrentViewArea"
+ "epp_CopyHIDInputMode"
+ "epp_CopyProperty"
+ "epp_CreateCommChannel"
+ "epp_CreatePlaybackSession"
+ "epp_CreateRemoteControlSession"
+ "epp_DeactivateWithCompletionCallback"
+ "epp_DisableBluetooth"
+ "epp_DuckAudio"
+ "epp_DumpHierarchy"
+ "epp_EnsureAuthorizedWithCompletionCallback"
+ "epp_RelinquishResource"
+ "epp_RequestCarUI"
+ "epp_RequestViewArea"
+ "epp_SendCommand"
+ "epp_SendData"
+ "epp_SetDelegate"
+ "epp_SetDelegateRemoteControl"
+ "epp_SetDelegateRouting"
+ "epp_SetDelegateVolumeAndMute"
+ "epp_SetHIDInputMode"
+ "epp_SetProperty"
+ "epp_TakeScreen"
+ "epp_UnborrowScreen"
+ "epp_UpdateFeaturesWithCompletionCallback"
+ "epp_addSubEndpoint"
+ "epp_copyCachedClusterProperty"
+ "epp_copyCachedDescriptionProperty"
+ "epp_copyCachedMXDescriptor"
+ "epp_copyCachedProperty"
+ "epp_copyEndpointPropertyToDestination"
+ "epp_copySubEndpoint"
+ "epp_copySubEndpointForRealSubEndpoint"
+ "epp_copySubEndpointsArray"
+ "epp_delegate_handleAuthRequired"
+ "epp_delegate_handleAuthRequiredCallback"
+ "epp_delegate_handleConnectedStateChanged"
+ "epp_delegate_handleCopyProperty"
+ "epp_delegate_handleDidCloseCommChannel"
+ "epp_delegate_handleDidReceiveDataFromCommChannel"
+ "epp_delegate_handleFailed"
+ "epp_delegate_handleIncomingRemoteControlSessionCreated"
+ "epp_delegate_handleSetProperty"
+ "epp_delegate_handleStreamsChanged"
+ "epp_getCachedClusterSupportedFeatures"
+ "epp_getCachedSupportedFeatures"
+ "epp_removeSubEndpoint"
+ "epp_setInner"
+ "epp_shouldAllowEndpoint"
+ "epp_updateDescription"
+ "epp_updateDescriptionFromEndpoint"
+ "epp_updateDescriptionFromInner"
+ "err"
+ "evictCachedDeviceWithID:"
+ "external Cluster connection to non-Cluster leader"
+ "failed with err="
+ "forceInfraMirroring"
+ "forcedMode=%@ endpointsActivated=%s endpointRequiredDiscoveryMode=%s internalClientsRequiringDiscovery=%d\n"
+ "forwardCryptorSubsampleAuxData"
+ "forwardFrameUserData"
+ "groupEncryptionKey"
+ "groupIPv4Addr"
+ "httpConnectPSK"
+ "httpConnectPSKIdentity"
+ "httpConnectPassword"
+ "httpConnectURLs"
+ "httpConnectUserName"
+ "i24@0:8^v16"
+ "i24@0:8^{?={CGSize=dd}i@@C^{__CFString}@C^vQ}16"
+ "i32@0:8^{?={CGSize=dd}i@@C^{__CFString}@C^vQ}16@24"
+ "i44@0:8@?16^v24C32^{__CFString=}36"
+ "i48@0:8^@16q24^{?={CGSize=dd}i@@C^{__CFString}@C^vQ}32@40"
+ "i64@0:8[16C]16@24^{?={CGSize=dd}i@@C^{__CFString}@C^vQ}32{?=^?^vi}40"
+ "iPhone14,3"
+ "inKeyHolder is NULL!"
+ "inactive"
+ "initWithCallback:forLink:forIP:"
+ "initWithDeviceIdentifier:delegate:queue:"
+ "int multicastProbeSender_socketForMC2UCProbing(APMulticastProbeSenderRef, const char *, sa_family_t)"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "kFigEndpointStreamAudioEngineError_AllocationFailed"
+ "keyHolder is NULL!"
+ "manager_createAndAddUGLWrapperEndpoint"
+ "manager_createEndpoint"
+ "manager_createUGLRCServer"
+ "manager_create_block_invoke_5"
+ "manager_handleShadowEndpointEvent"
+ "manager_introspector_activateEndpoint"
+ "manager_introspector_deactivateEndpoint"
+ "manager_introspector_sendUGLreceiverCommand"
+ "manager_introspector_setDiscoveryMode"
+ "manager_startOrStopUGLRCServer"
+ "manager_updateEndpoint"
+ "mc2ucDetectionSSMGroupIPv4Addr"
+ "mc2ucDetectionSSMGroupIPv6Addr"
+ "mc2ucDetectionSSMGroupInfo"
+ "mc2ucPktCnt"
+ "mc2ucProbeBurstID"
+ "mc2ucStatus"
+ "mediumLatencyAudioStream"
+ "mediumLatencyPathway"
+ "messageID is missing in response event"
+ "mock::DisplaysArray"
+ "multicastProbeSender_create"
+ "multicastProbeSender_create isMC2UCDetectionEnabled=%d"
+ "multicastProbeSender_createEncryptionKeyAndCryptor"
+ "multicastProbeSender_createMulticastGroupInfo"
+ "multicastProbeSender_createPayloadForMC2UC"
+ "multicastProbeSender_decrementRefCountForSSMGroupInfo"
+ "multicastProbeSender_incrementRefCountForSSMGroupInfo"
+ "multicastProbeSender_probeForMC2UC"
+ "multicastProbeSender_socketForMC2UCProbing"
+ "multicastProbeSender_updateTxProbePacketsForClients"
+ "multicastToUnicastReceivedPacketCount"
+ "multicastToUnicastStatus"
+ "multicastToUnicastTimeToDetectMs"
+ "multicastToUnicastTransmittedPacketCount"
+ "newEphemeralDeviceIdentifier"
+ "numberWithInt:"
+ "numberWithUnsignedInt:"
+ "obtainSharedInstanceOrCreate:"
+ "openNANAllowed"
+ "overriden asbd for PCM Array to [%{asbd}]"
+ "perceivedClusterType"
+ "playbackCoordinationMedium"
+ "playbackStateChanged"
+ "playbackStatus"
+ "port"
+ "process available endpoint changes"
+ "proxyAuthorization"
+ "proxyInfo"
+ "proxyInfo argument is NULL"
+ "proxyInfo contains no URLs"
+ "proxyParameters: %@\n"
+ "proxyPort"
+ "proxyPsk"
+ "proxyPskIdentity"
+ "proxyUrl"
+ "psgid"
+ "ptpReenablePortMatchingOverride"
+ "ptpReenableRedundantClusterLinks"
+ "realDeviceFound:"
+ "realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener"
+ "realTimeAudioEngine_setAudioStreamInfoArrayForRTC"
+ "realTimeAudioEngine_setTransportAudioFormatInternal"
+ "registerDevice:properties:operationalproperties:queue:completionBlock:"
+ "registerToDeviceManager"
+ "removeMonitorClientForKey:"
+ "runTest"
+ "rw"
+ "sbpd_createUserDataBBuf"
+ "sbpd_encryptBBuf"
+ "scheme"
+ "senderNetworkClock"
+ "senduglreceivercommand"
+ "session_BroadcastCoordinatedPlaybackState"
+ "set discovery mode"
+ "setAllowedLinkTypes:"
+ "setCachedDeviceFoundHandler:"
+ "setCachedDeviceLostHandler:"
+ "setIsExternalPairing:"
+ "setMonitorCallbackIfNotExists:forKey:forLink:forIP:"
+ "setPdEncryptionContext:"
+ "setPdProtectionOptions:"
+ "setProxyCapability:"
+ "setProxyParameters"
+ "setProxyProviderAuthMode:"
+ "setProxyProviderType:"
+ "setUsePresentDeviceStashing:"
+ "setUseStrictNetworkSignatureMatching:"
+ "setVideoPlaybackAllowed"
+ "setdiscoverymode"
+ "show caching manager info"
+ "showManagerPlus"
+ "sourceIPv4Addr"
+ "startupOptions"
+ "streamConnectionTypeAPAT"
+ "stringWithFormat:"
+ "supportsV2ArtworkMetadata"
+ "terminusd reset, re-registration successful"
+ "testParams"
+ "testRequestUI"
+ "testToRun"
+ "tsid"
+ "txt"
+ "type is missing in response event"
+ "ugl"
+ "uglAssistedDiscovery"
+ "uglServerInfo"
+ "uglWrapper_createNetworkAddressesArray"
+ "uglWrapper_createNetworkAddressesArray_block_invoke"
+ "uint64_t emp_getCachePromotionDeadlineDuration(void)_block_invoke"
+ "uint64_t emp_timedBlock(FigEndpointManagerRef, const char *, void (^)(void))"
+ "unregisterDevice:"
+ "unsignedIntValue"
+ "updateMC2UCStatus"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0^{__CFDictionary=}8"
+ "v24@0:8@\"NRDeviceMonitor\"16"
+ "v24@?0^{__CFString=}8^{__CFString=}16"
+ "v24@?0^{__CFString=}8r^^{__CFString}16"
+ "v28@0:8@\"NRDeviceMonitor\"16B24"
+ "v28@0:8@\"NRDeviceMonitor\"16C24"
+ "v28@0:8@\"NRDeviceMonitor\"16i24"
+ "v28@0:8@16C24"
+ "v28@0:8@16i24"
+ "v28@?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NRDeviceInfo\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NSString\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16C24C28"
+ "v32@0:8@16C24C28"
+ "v36@?0^{OpaqueFigEndpoint=}8^{__CFString=}16C24r^^{__CFDictionary}28"
+ "v40@0:8^{?={CGSize=dd}i@@C^{__CFString}@C^vQ}16^Q24^Q32"
+ "v40@0:8{?=^?^vi}16"
+ "vdsink_CopyProperty"
+ "video2"
+ "video2Info"
+ "videoPlaybackAllowed"
+ "void APEndpointUGLWrapperAddShadowEndpoint(FigEndpointRef, APTransportDeviceRef, FigEndpointRef, FigEndpointRef)"
+ "void APEndpointUGLWrapperRemoveShadowEndpoint(FigEndpointRef, APTransportDeviceRef)"
+ "void APEndpointUGLWrapper_CloseAllCommChannels(FigEndpointExtendedRef)"
+ "void APEndpointUGLWrapper_Finalize(CMBaseObjectRef)"
+ "void _HandleFailureCallback(CFTypeRef, OSStatus)"
+ "void apsession_addMC2UCDetectionInfo(APSenderSessionRef, CFMutableDictionaryRef)"
+ "void apsession_registerForMC2UCDetection(APSenderSessionRef)"
+ "void audioEngineBufferedAdapter_Finalize(CMBaseObjectRef)"
+ "void audioEngineBufferedAdapter_FlushData(void *)"
+ "void audioEngineBufferedAdapter_Resume(FigEndpointStreamAudioEngineRef, CFDictionaryRef, FigEndpointStreamAudioEngineResumeCallback, void *)"
+ "void audioEngineBufferedAdapter_ResumeInternal(void *)"
+ "void audioEngineBufferedAdapter_SendData(void *)"
+ "void audioEngineBufferedAdapter_SetEndpointStream(FigEndpointStreamAudioEngineRef, FigEndpointStreamRef, FigEndpointStreamAudioEngineSetEndpointStreamCallback, void *)"
+ "void audioEngineBufferedAdapter_SetEndpointStreamComplete(void *)"
+ "void audioEngineBufferedAdapter_SetEndpointStreamInternal(void *)"
+ "void audioEngineBufferedAdapter_Suspend(FigEndpointStreamAudioEngineRef, CFDictionaryRef, FigEndpointStreamAudioEngineSuspendCallback, void *)"
+ "void audioEngineBufferedAdapter_SuspendInternal(void *)"
+ "void audioStream_receivedMediaDataEventMessage(FigTransportStreamRef, OSType, CMBlockBufferRef, void *)"
+ "void bufferedAudioEngine_audioTimer(void *)_block_invoke"
+ "void bufferedAudioEngine_handleErrorWithReceiverAnchor(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, OSStatus)"
+ "void bufferedAudioEngine_handleTerminalSetRateError(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, OSStatus, Boolean)"
+ "void bufferedAudioEngine_logProtocolDriverBufferFullness(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverSenderRef)"
+ "void bufferedAudioEngine_maybeTriggerTTR(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, CFStringRef, OSStatus)"
+ "void bufferedAudioEngine_protocolDriverTickTimer(void *)"
+ "void bufferedAudioEngine_updateStartWatermarkAndMaxWaitTime(FigEndpointStreamAudioEngineRef)"
+ "void carEndpoint_deactivateInternal(FigEndpointRef, Boolean, CFStringRef, uint32_t *)_block_invoke_5"
+ "void carEndpoint_logStats(FigEndpointRef, CFDictionaryRef)"
+ "void carEndpoint_logStats(FigEndpointRef, CFDictionaryRef)_block_invoke"
+ "void carEndpoint_runTestCommand(FigEndpointRef, CFStringRef, CFDictionaryRef)"
+ "void carEndpoint_teardownSenderSession(FigEndpointRef, APSenderSessionRef, Boolean)"
+ "void carEndpoint_updateActiveStreamConnectionIDs(FigEndpointRef)"
+ "void carManager_collectAnalyticsIfNeeded(FigEndpointManagerRef, FigEndpointRef, FigEndpointRef, int32_t)"
+ "void emp_Finalize(CMBaseObjectRef)"
+ "void emp_cancelCachePromotionDeadlineIfNecessary(FigEndpointManagerRef)"
+ "void emp_evictCachedEndpoint(FigEndpointManagerRef, FigEndpointRef)"
+ "void emp_handleCachePromotionDeadline(FigEndpointManagerRef)"
+ "void emp_postNotification(CMNotificationCenterRef, CFStringRef, FigEndpointManagerRef, CFTypeRef)_block_invoke"
+ "void emp_processAvailableEndpointChanges(FigEndpointManagerRef)"
+ "void emp_restartCachePromotionDeadlineIfNecessary(FigEndpointManagerRef)"
+ "void endpointUGLWrapper_checkForUGLServerInfo(FigEndpointRef, FigEndpointRef)"
+ "void endpointUGLWrapper_handleRCEndpointDescriptionChanged(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointUGLWrapper_handleWrappedNotification(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointUGLWrapper_setWrappedEndpoint(FigEndpointRef, FigEndpointRef)"
+ "void endpoint_authorizationRequestCompletionCallback(FigEndpointRef, CFStringRef, OSStatus, void *)"
+ "void endpoint_collectMC2UCMetrics(FigEndpointRef, APSenderSessionRef, CFMutableDictionaryRef)"
+ "void endpoint_createSetAuthorizationStringBlockWrapper(FigEndpointRef, APSWrapperRef *)_block_invoke"
+ "void endpoint_gatherActivationMetricsIfNeeded(FigEndpointRef, APSenderSessionRef, APSEventRecorderRef, CFStringRef, OSStatus)"
+ "void epp_Finalize(CMBaseObjectRef)"
+ "void epp_activationCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
+ "void epp_completionCallback(FigEndpointRef, OSStatus, void *)"
+ "void epp_delegate_handleAuthRequired(FigEndpointRef _Nonnull, FigEndpointRef _Nullable, uint64_t, CFTypeRef _Nullable, CFStringRef _Nonnull, FigEndpointAuthHandlingCompletionCallback _Nonnull, void * _Nullable)"
+ "void epp_delegate_handleAuthRequiredCallback(FigEndpointRef _Nonnull, CFStringRef _Nullable, OSStatus, void * _Nullable)"
+ "void epp_handleInnerNotification(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void epp_postNotificationAsync(FigEndpointRef, CFStringRef, CFDictionaryRef)_block_invoke"
+ "void epp_sendCommandCallback(FigEndpointExtendedRef, OSStatus, CFDictionaryRef, void *)"
+ "void epp_sendDataCallback(FigEndpointExtendedRef, CFStringRef, OSStatus, void *)"
+ "void manager_handleShadowEndpointEvent(FigEndpointManagerRef, APTransportDeviceRef, APEndpointDescriptionRef, Boolean, Boolean)"
+ "void manager_removeShadowEndpointForTransportDevice(FigEndpointManagerRef, APTransportDeviceRef)"
+ "void manager_removeShadowEndpointFromUGLWrapper(FigEndpointManagerRef, APTransportDeviceRef, FigEndpointRef)"
+ "void manager_removeUGLWrapperEndpointIfEmpty(FigEndpointManagerRef, FigEndpointRef)"
+ "void manager_startOrStopUGLRCServer(FigEndpointManagerRef, Boolean)"
+ "void manager_updateUGLRCServerandCopyInfo(FigEndpointManagerRef, FigEndpointRef, CFStringRef, Boolean, CFDictionaryRef *)"
+ "void multicastProbeSender_Finalize(CMBaseObjectRef)"
+ "void multicastProbeSender_clearSocketList(APMulticastProbeSenderRef)"
+ "void multicastProbeSender_configureSSM(APMulticastProbeSenderRef)"
+ "void realTimeAudioEngine_DynamicLatencyOffsetDidChangeListener(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void realTimeAudioEngine_setAudioLatency(FigEndpointStreamAudioEngineRef, float, Boolean)"
+ "void realTimeAudioEngine_setEndpointStreamInternal(void *)"
+ "void realTimeAudioEngine_updateDynamicLatencyIfNeeded(FigEndpointStreamAudioEngineRef, Boolean, Boolean)"
+ "void session_authorizeItemCompletion(OSStatus, CFDictionaryRef, void *)"
+ "void session_cleanupPendingRequests(void *)"
+ "void session_cleanupPendingRequests(void *)_block_invoke"
+ "void session_getProxiedPropertyCompletion(OSStatus, CFDictionaryRef, void *)"
+ "void session_handleMetadataArtworkEventInternal(FigEndpointPlaybackSessionRef, CFDictionaryRef)"
+ "void session_handleRemoteControlSessionEventInternal(void *)"
+ "void session_performActionRequestForStreamingKeyCompletion(OSStatus, CFDictionaryRef, void *)"
+ "void session_performActionUnhandledURLResponseCompletion(OSStatus, CFTypeRef, void *)"
+ "void session_playbackInfoCompletion(OSStatus, CFDictionaryRef, void *)"
+ "void session_seekCompletion(OSStatus, CFDictionaryRef, void *)"
+ "void session_sendDiffVideoV2ArtworkMetadata(FigEndpointPlaybackSessionRef, CFDictionaryRef)"
+ "void session_setEventHandlerInternal(void *)"
+ "void session_standardCompletion(OSStatus, CFTypeRef, void *)"
+ "void soft_CRFetchScaledDisplaysForCertificateSerialNumber(NSData *, NSArray<NSDictionary *> *, void (^)(NSArray<NSDictionary *> *, NSError *))"
+ "void uglWrapper_deactivateShadowCompletionCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
+ "void uglWrapper_deactivationCompletionCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
+ "void uglWrapper_freeEndpointActivationContext(EndpointActivationCallbackContext *)"
+ "void uglWrapper_freeEndpointDeactivationContext(EndpointDeactivationCallbackContext *)"
+ "void uglWrapper_handleFailedInternal(FigEndpointRef, uint64_t, CFDictionaryRef, CFTypeRef)"
+ "void uglWrapper_handleFailedInternal(FigEndpointRef, uint64_t, CFDictionaryRef, CFTypeRef)_block_invoke"
+ "void uglWrapper_shadowActivationCompletionCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
+ "void uglWrapper_wrappedActivationCompletionCallback(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
+ "zeroFirstRemoteMediaTime"
+ "zoomFactor"
+ "| %-40@: %@\n"
+ "| %-40s: %@\n"
- "     omitting -r means it must be the non-remote-control endpoint\n"
- "  -r is used when endpoint is specified with name or ID:\n"
- "### [%{ptr}] Failed to parse MDC message plist. %@\n"
- "%###s: There are %d clusters requiring Detailed discovery\n"
- "%@ AudioEngineRealTime using audio format %s and stream type %@\n"
- "%@ DynamicLatencyManager is used variant=%@ latencyTierIdx=%d latencyMs=%d \n"
- "%@ TransportASBD: [%{asbd}]. transportAudioFormat: %s. \n"
- "%@ vbrBitRate = %d. CodecType: %s\n"
- "%@ vbrMaxPacketSize = %d. CodecType: %s\n"
- "%{ptr} ### pending auth operation already?\n"
- "%{ptr} %###s weakDelegateContextRouting is not NULL, but handleAuthRequiredCompletionCallbackContext is NULL.\n"
- "%{ptr} activation state has changed...\n"
- "%{ptr} auth completion, result %#m\n"
- "%{ptr} endpoint activation state has changed; ignoring auth completion callback...\n"
- "%{ptr} no auth delegate set...\n"
- "%{ptr} start auth...\n"
- "860.7.1"
- "<APEndpointManagerIntrospector> [%{ptr}] didn't match endpoint [%{ptr}] for ID %@, name %@, hash %@, remote %s"
- "<PWDKeyExchange> [%{ptr}] Completed with status=%#m"
- "AIRPLAY_SIGNPOST_AUDIOENGINE_RESUME_END"
- "AIRPLAY_SIGNPOST_AUDIOENGINE_RESUME_START"
- "APEndpointStreamBuffered <APEndpointStreamBufferedHoseStreamingProtocol> on <%p>"
- "APSenderSessionAirPlay %{ptr} with name %@ created.\n"
- "Activating endpoint [%{ptr}] '%@' with features 0x%llx and options %@\n"
- "ActivationConnectionTimeMs"
- "ActivationMsgsProcessingTimeMs"
- "ActivationMsgsRoundTripTimeMs"
- "AirPlayPerf_LocalStereoPairClusterPersistentConnection"
- "AirPlayStartServicesInMXProcess"
- "AudioEngineHoseManager"
- "BAE [%{ptr}] %s### [0x%04X] HoseManager [%{ptr}] has encountered terminal errors during SetRate, dissociating...\n"
- "BAE [%{ptr}] %s### [0x%04X] HoseManager [%{ptr}] hit too many retries trying to resolve errors, dissociating...\n"
- "BAE [%{ptr}] %sBufferLevel RTC Metrics Send Rate Statistics: Min: %@, Max: %@, Mean: %@, Median: %@"
- "BAE [%{ptr}] %sBufferLevel RTC Metrics Summary: Model: %@, Build: %@, HoseCount: %lu, hist: %@, Topology Duration (ms): %@"
- "BAE [%{ptr}] %sBufferLevel RTC Metrics Underruns: Underrun Count: %lu, Total Underrun Duration: %@, Min Underrun Duration: %@, Max Underrun Duration: %@, Mean Underrun Duration: %@, Median Underrun Duration: %@, ( Total Underrun Duration / Topology Duration ): %1.4f"
- "BAE [%{ptr}] %sHose [%{ptr}] (%@) started underrunning at: %1.6f"
- "BAE [%{ptr}] %sHose [%{ptr}] (%@) stopped underrunning at: %1.6f underrun duration: %1.6f, count: %lu"
- "BAE [%{ptr}] %sHose [%{ptr}] (%@) stopped underrunning at: %1.6f. Underrun duration: %1.6f, count: %lu"
- "BAE [%{ptr}] %sHose [%{ptr}] lastDeliveredRemoteMediaTime: %1.6f, inHoseDescriptor->rtcStats.underrun.start: %1.6f, currentRemoteMediaTime: %1.6f"
- "BAE [%{ptr}] %sRegistering hose [%{ptr}] with audio engine (current hoseCount = %d)\n"
- "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Could not process all invalid samples of the next song. Discard Count: %u lastRemoteMediaTimeDiscarded (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Could not process all valid samples of the current song. Prepared: %u NextRTP (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] ### FlushWithinSampleRange: Failed with err = %d\n"
- "BAE [%{ptr}] %s[0x%04X] (burst) Not flushing hose [%{ptr}] (%@) since ( rate == 0.0 ) AND ( sentPacketCount == 0 )\n"
- "BAE [%{ptr}] %s[0x%04X] APSEndpointStreamAudioHoseSetCryptor failed for hose [%{ptr}] with err= %d \n "
- "BAE [%{ptr}] %s[0x%04X] APSEndpointStreamAudioHoseSetMagicCookie failed for hose [%{ptr}] with err= %d \n "
- "BAE [%{ptr}] %s[0x%04X] Cancel pending SetRate 1 hoseManager [%{ptr}]\n"
- "BAE [%{ptr}] %s[0x%04X] Cannot start timebase with receiver anchor for hoseManager [%{ptr}] err = %d \n"
- "BAE [%{ptr}] %s[0x%04X] Discarding sbuf with opts %1.3f for current flush time range: start = %1.3f, end = %1.3f \n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Discarding all invalid samples: Next (%ld/%d) Start (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Process valid samples complete: Prepared: %u NextRemoteMediaTimestamp (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Processed invalid samples complete: Discard Count: %u lastRemoteMediaTimeDiscarded (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: Processing all valid samples: Next (%ld/%d) Start (%ld/%d)\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: currentRTP = (%u / %f) CURR nextRTP_TS = (%u / %f) NEW nextRTP_TS = (%u / %f)\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: flushRangeRemoteMediaTime.start.value = %ld flushRangeRemoteMediaTime.start.ts = %d flushRangeRemoteMediaTime.duration.value = %ld flushRangeRemoteMediaTime.duration.ts = %d\n"
- "BAE [%{ptr}] %s[0x%04X] FlushWithinSampleRange: sampleRange.start.value = %ld sampleRange.start.ts = %d duration.value = %ld duration.ts = %d first.value = %lu first.ts = %d\n"
- "BAE [%{ptr}] %s[0x%04X] Found TrimAtEnd attachment with duration %1.3f seconds\n"
- "BAE [%{ptr}] %s[0x%04X] Found TrimAtStart attachment with duration %1.3f seconds, sbuf_pts: %1.3f, sbuf_opts: %1.3f, sbuf_dur: %1.3f, sbuf_odur: %1.3f\n"
- "BAE [%{ptr}] %s[0x%04X] SetRate 1 FAILURE for hoseManager [%{ptr}] err = %d SetRate Not Supported\n "
- "BAE [%{ptr}] %s[0x%04X] SetRate 1 FAILURE for hoseManager [%{ptr}] err = %d, calling callback.\n"
- "BAE [%{ptr}] %s[0x%04X] SetRate 1 success for hoseManager [%{ptr}] \n"
- "BAE [%{ptr}] %s[0x%04X] hoseManager [%{ptr}] not found during set rate completion callback."
- "BAE [%{ptr}] %s[0x%04X] inHoseManager is NULL"
- "BAE [%{ptr}] %sbufferLevelPercentage %1.4f hose %@, bufferLevelTime: %1.4f currentRemoteMediaTime: %1.4f, durationInMessageRing: %1.4f, maxBufferLevelTime: %1.4f"
- "BAE [%{ptr}] %screating BufferLevelHistogram for hose %@"
- "BAE [%{ptr}] %sremoving BufferLevelHistogram for hose %@"
- "BAE [%{ptr}] %sreporting BufferLevelHistogram for hose %@"
- "Boolean apsession_isCancelled(APSenderSessionRef)"
- "Browser IsConfiguredForMaximumDiscovery property's Status Changed"
- "CRFetchScaledDisplays"
- "CRFetchScaledDisplays completion handler successful, took %lu ms\n"
- "Calling CRFetchScaledDisplays...\n"
- "ClusterEndpoint:[%{ptr}] (%s %@) %''@ Parent:[%{ptr}]\n"
- "Configure for discovery\n"
- "Endpoint %{ptr}: waiting for auth completion timeout after %u secs\n"
- "Endpoint:[%{ptr}] (%s) %''@ Parent:[%{ptr}]\n"
- "Endpoint:[%{ptr}] (Local) %''@ Parent:[%{ptr}]\n"
- "FAILURE hose=0x%x"
- "Feedback received, \"statsDictionary\":\n %@"
- "FigAudioSession"
- "FigEndpointRef manager_introspector_copyMatchingEndpoint(FigEndpointManagerRef, CFStringRef, Boolean)"
- "FramesPerPacket"
- "Histogram_ReceiverBufferLevel"
- "InitialTransportAudioFormat"
- "IsDissociated"
- "IsPersistentConnectionOverride"
- "Last Session deactivation time: %f\n"
- "NAN partial"
- "OSStatus APCarPlay_CRFetchScaledDisplays(CFArrayRef, CFArrayRef *)"
- "OSStatus APCarPlay_CRFetchScaledDisplays(CFArrayRef, CFArrayRef *)_block_invoke"
- "OSStatus APSenderSessionAirPlayCreate(CFAllocatorRef, CFStringRef, APEndpointDescriptionRef, APSConnectionInterfaceManagerRef, APSenderSessionUsage, APSClusterType, dispatch_queue_t, Boolean, Boolean, Boolean, APSNetworkClockRef, CFStringRef, CFStringRef, Boolean, double, CFDictionaryRef, APSenderSessionRef *)"
- "OSStatus AirPlayDebugIPCEnableForEndpointManager(FigEndpointManagerRef)"
- "OSStatus airPlayDescription_updateWithAdvertiserAndPSGInfosNotifyingClients(APEndpointDescriptionRef, APAdvertiserInfoRef, CFDictionaryRef)"
- "OSStatus audioStream_createAndResumeTransportBufferedAudioDataStream(FigEndpointStreamRef, APSenderSessionRef, int, Boolean, Boolean, FigTransportStreamRef *)"
- "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, Boolean, CFDataRef, Boolean, Boolean, uint64_t *, uint64_t *, Boolean *, int *, int32_t *, int *, CFDataRef *)"
- "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, int, CFDictionaryRef, APAudioFormat, Boolean, CFDataRef, uint64_t, uint64_t *, int *, int *, CFDictionaryRef *, int *, uint32_t *, APSCryptorRef *)"
- "OSStatus browserController_configureForMaximumDiscovery(void *)"
- "OSStatus bufferedAudioEngine_audioHoseRegistrarDeregisterHoseInternal(void *)"
- "OSStatus bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal(void *)"
- "OSStatus bufferedAudioEngine_pruneMessageRingToCurrentRemoteMediaTimeWithForwardMargin(FigEndpointStreamAudioEngineRef)"
- "OSStatus bufferedAudioEngine_removeHose(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef)"
- "OSStatus bufferedAudioEngine_sendFlushWithinSampleRangeInternal(FigEndpointStreamAudioEngineRef, uint16_t, uint32_t, CMTime, uint32_t, CMTime)"
- "OSStatus bufferedAudioEngine_updateRTCHistogramForHose(FigEndpointStreamAudioEngineRef, APAudioEngineHoseDescriptor *)"
- "OSStatus carEndpoint_activateInternal(FigEndpointRef, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)"
- "OSStatus carEndpoint_activateInternal(FigEndpointRef, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke"
- "OSStatus carEndpoint_activateInternal(FigEndpointRef, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke_2"
- "OSStatus carEndpoint_activateInternal(FigEndpointRef, CFDictionaryRef, dispatch_semaphore_t, uint32_t *)_block_invoke_3"
- "OSStatus carEndpoint_overrideFeatureKeyWithPrefValue(FigEndpointRef, CFMutableArrayRef, CFStringRef, CFStringRef)"
- "OSStatus carEndpoint_validateEnabledFeaturesWithAccessory(FigEndpointRef)"
- "OSStatus coreUtilsPairing_performSetupInternal(APPairingClientRef, const CFStringRef, APPairingType, Boolean, CFStringRef *, CFDataRef *, CFDataRef *, CFTypeRef *)"
- "OSStatus coreUtilsPairing_sendPairSetupRequest(APPairingClientRef, APPairingType, const uint8_t *, size_t, CMBlockBufferRef *)"
- "OSStatus endpointLocal_setSystemMute(FigEndpointRef, Boolean)"
- "OSStatus endpointLocal_setSystemVolume(FigEndpointRef, Float32)"
- "OSStatus endpoint_createSenderSession(FigEndpointRef, APSConnectionInterfaceManagerRef, CFStringRef, FigEndpointFeatures, Boolean, Boolean, Boolean, Boolean, Boolean, APSClusterType, APSNetworkClockRef, CFStringRef, CFStringRef, Boolean, double, APSenderSessionFactoryRef, CFDictionaryRef, APSenderSessionRef *)"
- "OSStatus endpoint_handleAuthRequiredSync(FigEndpointRef, uint64_t, APEndpointActivationStage)"
- "OSStatus endpointdelegate_setIsMuted(FigEndpointRef, Boolean, Boolean)"
- "OSStatus endpointdelegate_setVolumeSliderInternal(FigEndpointRef, Float32, Boolean, Boolean, Boolean)"
- "OSStatus endpointdelegate_translateIsMutedToVolumeOperation(FigEndpointRef, Boolean)"
- "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_3"
- "OSStatus realTimeAudioEngine_setTransportAudioFormatASBDInternal(FigEndpointStreamAudioEngineRef, APAudioFormat)"
- "OSStatus realTimeAudioEngine_tas_ResumeInternal(APRTAETranscoderAndSender *, AudioStreamBasicDescription, FigEndpointAudioSourceRef, APSCryptorRef, CMClockRef, CMTimebaseRef, CMTimebaseRef, APSRTPPacketHandlerRef, APTransportStreamSendBackingProviderRef, APMessageRingRef, APMessageRingRef)"
- "OSStatus screenstreamudp_resumeInternal(FigEndpointStreamRef, CFDictionaryRef, StreamScreenUDPCompletionContext *)"
- "OSStatus screenstreamudp_setupStream(FigEndpointStreamRef, StreamScreenUDPCompletionContext *)"
- "OSStatus screenstreamudp_suspendInternal(FigEndpointStreamRef, CFDictionaryRef, StreamScreenUDPCompletionContext *)"
- "PRIMED hose 0x%x, bufferLevelTime %1.3f"
- "REQUEST hose=0x%x"
- "Returned from CRFetchScaledDisplays\n"
- "SUCCESS hose=0x%x"
- "SenderSession:[%{ptr}] Parent:[%{ptr}]\n"
- "SetRate encountered terminal error"
- "SupportAPAP"
- "Usage: %s [-r] <name|ID|hash|ptr> <command> [key1:type1:val1] [key2:type2:val2] ...\n"
- "Usage: %s [-r] <name|ID|hash|ptr> <propertyKey> <propertyValue>\n"
- "Usage: %s [-r] <name|ID|hash|ptr> <subEndpointID> <propertyKey>\n"
- "Usage: %s [-r] <name|ID|hash|ptr> <subEndpointID> <propertyKey> <propertyValue>\n"
- "Usage: %s [-r] [desc@]<name|ID|hash|ptr|-> <propertyKey>\n"
- "UseQUIC"
- "[%p] Display description count: %d\n"
- "[%{ptr}] ### LowLatency requested, but endpoint not in Persistent Group!\n"
- "[%{ptr}] ### LowLatency requested, but not in same Persistent Group!\n"
- "[%{ptr}] <AirPlayVolume> can't set system mute = %s; not supported on this platform\n"
- "[%{ptr}] <AirPlayVolume> can't set system volume = %f; not supported on this platform\n"
- "[%{ptr}] Activation complete. Duration: %llu ms%?{end} (%llu ms sender, %llu ms connection, %llu ms networking, %llu ms receiver)\n"
- "[%{ptr}] Appending peer list (size: %d) to SETUP Request%?{end}: %@"
- "[%{ptr}] Invalidating %@ (invalid=%s)"
- "[%{ptr}] MDC disconnected, suspending...\n"
- "[%{ptr}] MDC request '%C'\n"
- "[%{ptr}] Not sending Screen signposts to CARConnectionTimeStore"
- "[%{ptr}] PWD configured, no AVConference based mirroring\n"
- "[%{ptr}] PWDKeyExchangeSender Completed called completionStatus %#m"
- "[%{ptr}] RCS ref creation complete for: %@\n"
- "[%{ptr}] Reconfirming device on connection failure...\n"
- "[%{ptr}] Report (remote) audio performance: protVer=%d sessionDuration=%d[s] renderDeadlineMin=%ld[ms] %@"
- "[%{ptr}] Setting dynamic audio latency offset to %d ms\n"
- "[%{ptr}] Setting traffic registration options for mirroring to ht group: %@.\n"
- "[%{ptr}] Want subEndpoint activation [%{ptr}]: %s - only if engaged, b/c not engaging on activation\n"
- "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d, previousActivationSeed: %d\n"
- "[%{ptr}] forwarding volume cache clear from subEndpoint [%{ptr}].\n"
- "[%{ptr}] isPassthroughSupported=%s, stroage->supportedFormats=%@"
- "allowOpenNANBrowsing"
- "apsession_copyPropertyInternal"
- "audioStream_receivedMediaDataControlMessage"
- "browserController_configureForMaximumDiscovery"
- "bufferedAudioEngine_addRTCHistogramForHose"
- "bufferedAudioEngine_audioHoseRegistrarDeregisterHoseInternal"
- "bufferedAudioEngine_audioHoseRegistrarRegisterHoseInternal"
- "bufferedAudioEngine_cancelRTCUnderrunForHose"
- "bufferedAudioEngine_isTimeWithinBounds"
- "bufferedAudioEngine_reportRTCBufferLevelAndUnderrunDataForHose"
- "bufferedAudioEngine_updateRTCHistogramForHose"
- "bufferedAudioEngine_updateRTCUnderrunForHose"
- "changed asbd for PCM Array to [%{asbd}]"
- "endpointAggregate_clearNetworkClockLocalPeerInfoIfNecessary"
- "endpointLocal_setSystemMute"
- "endpointLocal_setSystemVolume"
- "endpointManager[%d] %{ptr}"
- "endpoint_authHandlingComplete"
- "forcedMode=%@ endpointsActivated=%s endpointRequiredDiscoveryMode=%s clustersRequiringDiscovery=%d\n"
- "i24@0:8^{?={CGSize=dd}i@@C^{__CFString}@C}16"
- "i32@0:8^{?={CGSize=dd}i@@C^{__CFString}@C}16@24"
- "i48@0:8[16C]16@24^{?={CGSize=dd}i@@C^{__CFString}@C}32^{?=^?^vi}40"
- "i48@0:8^@16q24^{?={CGSize=dd}i@@C^{__CFString}@C}32@40"
- "isConfiguredForMaximumDiscovery"
- "isProvisionedForHDCP2"
- "localSPPCEnabledOverride"
- "manager_ConfigureForMaximumDiscovery"
- "manager_create_block_invoke_4"
- "openFullNANAllowed"
- "r"
- "radiosNeededForMaximumDiscovery"
- "realTimeAudioEngine_setTransportAudioFormatASBDInternal"
- "receiverBufferLevelEventBufferLevelHistogram"
- "receiverBufferLevelEventBufferedDeliveryTrackingEnabled"
- "receiverBufferLevelEventDeviceCount"
- "receiverBufferLevelEventMaxSendRateMsgsPerMs"
- "receiverBufferLevelEventMaxUnderrunDurationSecs"
- "receiverBufferLevelEventMeanSendRateMsgsPerMs"
- "receiverBufferLevelEventMeanUnderrunDurationSecs"
- "receiverBufferLevelEventMedianSendRateMsgsPerMs"
- "receiverBufferLevelEventMedianUnderrunDurationSecs"
- "receiverBufferLevelEventMinSendRateMsgsPerMs"
- "receiverBufferLevelEventMinUnderrunDurationSecs"
- "receiverBufferLevelEventModel"
- "receiverBufferLevelEventOSBuildVersion"
- "receiverBufferLevelEventReceiverIsLocal"
- "receiverBufferLevelEventSessionDurationMs"
- "receiverBufferLevelEventTotalUnderrunCount"
- "receiverBufferLevelEventTotalUnderrunDurationSecs"
- "sbpd_encryptFrameBBuf"
- "v24@0:8^{?=^?^vi}16"
- "v40@0:8^{?={CGSize=dd}i@@C^{__CFString}@C}16^Q24^Q32"
- "vdsink_GetPropertyAsync"
- "void _CompletedCallback(CFTypeRef, OSStatus)"
- "void audioStream_receivedMediaDataControlMessage(FigTransportStreamRef, OSType, CMBlockBufferRef, void *)"
- "void bufferedAudioEngine_cancelRTCUnderrunForHose(FigEndpointStreamAudioEngineRef, APAudioEngineHoseDescriptor *)"
- "void bufferedAudioEngine_flushWithinSampleRangeInternal(void *)"
- "void bufferedAudioEngine_handleErrorWithReceiverAnchor(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef, OSStatus)"
- "void bufferedAudioEngine_handleTerminalSetRateError(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef, OSStatus, Boolean)"
- "void bufferedAudioEngine_handleTerminalSetRateErrorForHoseManager(FigEndpointStreamAudioEngineRef, APAudioHoseManagerBufferedRef, OSStatus, Boolean)"
- "void bufferedAudioEngine_hoseManagerSetRateCallbackCompletionHandlerInternal(void *)"
- "void bufferedAudioEngine_maybeTriggerTTR(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef, CFStringRef, OSStatus)"
- "void bufferedAudioEngine_reportAndResetRTCBufferLevelAndUnderrunDataForAllExistingHoses(FigEndpointStreamAudioEngineRef)"
- "void bufferedAudioEngine_reportRTCBufferLevelAndUnderrunDataForHose(FigEndpointStreamAudioEngineRef, APAudioEngineHoseDescriptor *)"
- "void bufferedAudioEngine_updateRTCUnderrunForHose(FigEndpointStreamAudioEngineRef, APAudioEngineHoseDescriptor *)"
- "void bufferedAudioEngine_updateStartWatermarkTime(FigEndpointStreamAudioEngineRef)"
- "void carEndpoint_logStreamStats(const void *, const void *, void *)"
- "void endpointAggregate_handleSubEndpointVolumeCacheClear(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
- "void endpointCluster_handleSubEndpointVolumeCacheClear(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
- "void endpoint_authHandlingComplete(FigEndpointRef, CFStringRef, OSStatus, void *)"
- "void endpoint_gatherActivationMetricsIfNeeded(FigEndpointRef, APSenderSessionRef, APSEventRecorderRef, OSStatus)"
- "void realTimeAudioEngine_setAudioLatency(FigEndpointStreamAudioEngineRef, float)"
- "void realTimeAudioEngine_updateDynamicLatencyIfNeeded(FigEndpointStreamAudioEngineRef, Boolean)"
- "void soft_CRFetchScaledDisplays(NSArray<NSDictionary *> *, void (^)(NSArray<NSDictionary *> *, NSError *))"
- "| %-40@: %lf ( %@ )\n"
- "| %-40s: %lf ( %@ )\n"

```
