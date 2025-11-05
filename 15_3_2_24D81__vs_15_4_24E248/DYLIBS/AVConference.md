## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference`

```diff

-2100.5.1.0.0
-  __TEXT.__text: 0x6b6508
+2105.10.1.0.0
+  __TEXT.__text: 0x6bffec
   __TEXT.__auth_stubs: 0x4f00
-  __TEXT.__objc_methlist: 0x2d4c0
-  __TEXT.__const: 0x13cd8
-  __TEXT.__cstring: 0x7d3f5
-  __TEXT.__oslogstring: 0xf2c11
-  __TEXT.__gcc_except_tab: 0x289c
+  __TEXT.__objc_methlist: 0x307c0
+  __TEXT.__const: 0x138e0
+  __TEXT.__cstring: 0x7d689
+  __TEXT.__oslogstring: 0xf356b
+  __TEXT.__gcc_except_tab: 0x2a90
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd350
+  __TEXT.__unwind_info: 0xef80
   __TEXT.__objc_classname: 0x47b9
-  __TEXT.__objc_methname: 0x70f4e
-  __TEXT.__objc_methtype: 0x24449
-  __TEXT.__objc_stubs: 0x46980
-  __DATA_CONST.__got: 0x1500
-  __DATA_CONST.__const: 0x31c0
+  __TEXT.__objc_methname: 0x712d8
+  __TEXT.__objc_methtype: 0x244bc
+  __TEXT.__objc_stubs: 0x46b20
+  __DATA_CONST.__got: 0x1510
+  __DATA_CONST.__const: 0x3198
   __DATA_CONST.__objc_classlist: 0x1170
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x144d0
+  __DATA_CONST.__objc_selrefs: 0x146a0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xf88
   __DATA_CONST.__objc_arraydata: 0x2558
   __AUTH_CONST.__auth_got: 0x2798
-  __AUTH_CONST.__const: 0x6d78
-  __AUTH_CONST.__cfstring: 0x22120
-  __AUTH_CONST.__objc_const: 0x61110
-  __AUTH_CONST.__objc_intobj: 0x4080
+  __AUTH_CONST.__const: 0x6d80
+  __AUTH_CONST.__cfstring: 0x221c0
+  __AUTH_CONST.__objc_const: 0x5b6d0
+  __AUTH_CONST.__objc_intobj: 0x4098
   __AUTH_CONST.__objc_arrayobj: 0x1a28
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x9ab0
-  __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x63b4
-  __DATA.__data: 0x75c8
-  __DATA.__bss: 0xc08
+  __AUTH.__data: 0xb0
+  __DATA.__objc_ivar: 0x63dc
+  __DATA.__data: 0x75e8
+  __DATA.__bss: 0xaf8
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0x13b0
-  __DATA_DIRTY.__data: 0x4c
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__bss: 0x318
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7482BFA3-031A-36E5-A1A4-D3C8A0558347
-  Functions: 27850
-  Symbols:   54157
-  CStrings:  51000
+  UUID: 5A57B66F-3CDD-3340-9EAA-8A496F98744F
+  Functions: 28435
+  Symbols:   56254
+  CStrings:  51072
 
Symbols:
+ +[AVCBasebandAudioTap sharedInstance].cold.1
+ +[AVCCameraTestUtils expectedGFTResolutionForDevice:ratio:].cold.1
+ +[AVCCameraTestUtils expectedPreviewResolutionForDevice:width:height:].cold.1
+ +[AVCCameraTestUtils findExpectedFramerate:forDevice:].cold.1
+ +[AVCCaptionsClient serializeConfiguration:].cold.3
+ +[LogDumpUtility createLogDumpListSortedByTimestamp:]
+ +[LogDumpUtility removeLogDumpsInDirectory:olderThan:]
+ +[LogDumpUtility shouldCleanupFiles].cold.1
+ +[NetworkUtils encryptionInfoForKey:].cold.1
+ +[VCAnsweringMachineManager sharedInstance].cold.1
+ +[VCAudioClientManager sharedInstance].cold.1
+ +[VCAudioManager sharedSystemAudioInputInstance].cold.1
+ +[VCAudioManager sharedSystemAudioOutputInstance].cold.1
+ +[VCAudioManager sharedVoiceChatInstance].cold.1
+ +[VCAudioPowerSpectrumManager sharedInstance].cold.1
+ +[VCAudioRelayIOController sharedInstanceClientFacing].cold.1
+ +[VCAudioRelayIOController sharedInstanceSafeViewClientFacing].cold.1
+ +[VCAudioRelayIOController sharedInstanceSafeViewRemoteFacing].cold.1
+ +[VCAudioSmartRoutingManager sharedInstance].cold.1
+ +[VCAudioTierPicker loadVCAudioTierFromTierTable:config:allowRedAtLowBitrate:alwaysOnAudioRedundancyDisabled:redNumPayloads:tierBitrate:outEntryArray:].cold.3
+ +[VCAudioToolboxAudioComponentMock sharedInstance].cold.1
+ +[VCBTNotificationMonitor sharedInstance].cold.1
+ +[VCCannedAVSync sharedCannedAVSync].cold.1
+ +[VCCannedVideoPacketSource createFileAtPath:].cold.2
+ +[VCCannedVideoPacketSource removeFileAtPath:].cold.1
+ +[VCCaptionsManager defaultManager].cold.1
+ +[VCCoreAudio_AudioUnitMock sharedInstance].cold.1
+ +[VCDaemonProcessInfoManager sharedManager].cold.1
+ +[VCDatagramChannelManager sharedInstance].cold.1
+ +[VCDispatchQueue defaultManager].cold.1
+ +[VCHardwareSettings virtualHardwareSettings:].cold.2
+ +[VCMediaNegotiationBlobV2StreamGroupStream(Utils) payloadSpecWithStreamConfig:payloadConfigs:payloadSpecs:].cold.1
+ +[VCMediaNegotiatorStreamGroupU1Configuration negotiatedMicrophoneSettingsBetweenLocalU1Config:remoteU1Config:].cold.2
+ +[VCMediaNegotiatorStreamGroupU1Configuration negotiatedScreenSettingsBetweenLocalU1Config:remoteU1Config:].cold.3
+ +[VCMediaNegotiatorStreamGroupU1Configuration negotiatedScreenSettingsBetweenLocalU1Config:remoteU1Config:].cold.4
+ +[VCMediaNegotiatorStreamGroupU1Configuration negotiatedVideoSettingsBetweenLocalU1Config:remoteU1Config:streamGroupID:].cold.2
+ +[VCMediaNegotiatorStreamGroupU1Configuration negotiatedVideoSettingsBetweenLocalU1Config:remoteU1Config:streamGroupID:].cold.3
+ +[VCMediaNegotiatorStreamGroupU1Configuration updateBodyDataU1Config:bodyDataConfiguration:].cold.2
+ +[VCMediaNegotiatorStreamGroupU1Configuration updateFaceTextureU1Config:faceTextureConfiguration:].cold.3
+ +[VCMediaNegotiatorStreamGroupU1Configuration updateScreenU1Config:screenConfiguration:].cold.4
+ +[VCMediaNegotiatorV2 updateCameraU1Config:forNegotiationBlob:localSupportedVideoPayloads:u1AuthTagEnabled:].cold.5
+ +[VCMediaRecorderManager sharedInstance].cold.1
+ +[VCMediaStreamManager defaultManager].cold.1
+ +[VCMockIDSDatagramChannelController sharedInstance].cold.1
+ +[VCMockRouter sharedInstance].cold.1
+ +[VCNetworkAgent sharedInstance].cold.1
+ +[VCNetworkSimulator sharedInstance].cold.1
+ +[VCQoSMonitorManager sharedInstance].cold.1
+ +[VCRateControllerManager sharedInstance].cold.1
+ +[VCServerBag sharedInstance].cold.1
+ +[VCSessionManager sharedInstance].cold.1
+ +[VCStreamInputManager sharedInstance].cold.1
+ +[VCStreamOutputManager sharedInstance].cold.1
+ +[VCStringUtils cStringFromOperatingMode:]
+ +[VCSystemAudioCapture newAudioTapWithSessionType:audioFormat:].cold.1
+ +[VCTestMonitorManager sharedManager].cold.1
+ +[VCVideoDecoder streamTokenDecoderMap].cold.1
+ +[VCVideoHardwareDumpWriter sharedInstance].cold.1
+ +[VCVideoRuleCollectionsCameraMac sharedInstance].cold.1
+ +[VCVideoRuleCollectionsRemoteCameraMac sharedInstance].cold.1
+ +[VCVideoRuleCollectionsScreenAirplayEmbedded sharedInstance].cold.1
+ +[VCVideoRuleCollectionsScreenAirplayMac sharedInstance].cold.1
+ +[VCVideoRuleCollectionsScreenSecondaryMac sharedInstance].cold.1
+ +[VCVideoSourceTokenManager sharedManager].cold.1
+ +[VideoUtil convertPixelBuffer:toImageType:withAssetIdentifier:cameraStatusBits:allowTimeMetaData:].cold.10
+ -[AVAudioClient setupXPCConnection].cold.2
+ -[AVCCaptionsClient initWithDelegate:streamToken:].cold.6
+ -[AVCMoments didEndProcessingRequestHelperWithResult:].cold.3
+ -[AVCMomentsRequest setUpDirectoryURLWithConfiguration:].cold.5
+ -[AVCScreenCaptureAttributes initWithConfiguration:].cold.5
+ -[AVCStatisticsCollector start].cold.1
+ -[AVCStatisticsCollector stop].cold.1
+ -[AVCStreamInput initializeServerSideInputStream].cold.6
+ -[AVConference setRelayedCallType:forCallID:].cold.1
+ -[AVConferencePreview applyTransform:forLayer:]
+ -[AVConferencePreview applyTransform:forLayer:].cold.1
+ -[CannedEncodedVideoCapture createPixelBufferForFrameIndex:].cold.6
+ -[CannedEncodedVideoCapture createPixelBufferForFrameIndex:].cold.7
+ -[GKNATObserverInternal nameForNetworkWithIPPort:interfaceName:].cold.2
+ -[VCAVFoundationCapture dispatchedCurrentVideoFeatureStatus:].cold.1
+ -[VCAVFoundationCapture dispatchedCurrentVideoFeatureStatus:].cold.2
+ -[VCAVFoundationCapture updateVideoDataOutputVideoSettingResolution:requestHeight:captureFormat:]
+ -[VCAnsweringMachineManager answeringMachine:didStop:recordingURL:error:].cold.2
+ -[VCAudioCaptions createSampleBufferWithFormat:samples:numSamples:].cold.1
+ -[VCAudioCaptions createSampleBufferWithFormat:samples:numSamples:].cold.2
+ -[VCAudioCaptions createSampleBufferWithFormat:samples:numSamples:].cold.3
+ -[VCAudioCaptions dumpCaptionsIfNeededForCaptionsTranscription:final:].cold.1
+ -[VCAudioCaptionsBufferInfoCollection initWithBufferLength:].cold.2
+ -[VCAudioCaptionsCoordinator setUpSecondaryBufferQueue].cold.2
+ -[VCAudioCaptionsCoordinator setUpSecondaryBufferQueue].cold.3
+ -[VCAudioHALPluginDevice stop].cold.2
+ -[VCAudioIO startWithCompletionHandler:].cold.2
+ -[VCAudioIO startWithCompletionHandler:].cold.3
+ -[VCAudioIO stopWithCompletionHandlerInternal:].cold.1
+ -[VCAudioIO stopWithCompletionHandlerInternal:].cold.2
+ -[VCAudioManager applySpatialMetadata:].cold.1
+ -[VCAudioManager applyVoiceMixingMedia]
+ -[VCAudioManager setupVAD].cold.2
+ -[VCAudioPowerSpectrumManager serviceHandlerRegisterListenerWithArguments:error:].cold.3
+ -[VCAudioPowerSpectrumManager serviceHandlerRegisterListenerWithArguments:error:].cold.4
+ -[VCAudioPowerSpectrumManager serviceHandlerUnregisterListenerWithArguments:error:].cold.2
+ -[VCAudioRelay startRelayIO:otherRelayIO:].cold.2
+ -[VCAudioRelay startRelayIO:otherRelayIO:].cold.3
+ -[VCAudioRelay startRelayIO:otherRelayIO:].cold.4
+ -[VCAudioRelay startRelayIO:otherRelayIO:].cold.5
+ -[VCAudioRelay startRelayIO:otherRelayIO:].cold.6
+ -[VCAudioRelay stopRelayIO:otherRelayIO:].cold.4
+ -[VCAudioRelayIOController relay]
+ -[VCAudioRelayIOController waitIdleForClient:]
+ -[VCAudioSmartRoutingManager addClient:].cold.2
+ -[VCAudioSmartRoutingManager removeClient:].cold.2
+ -[VCAudioStream setUpMediaRecorder].cold.2
+ -[VCAudioStream shouldCreateReceiveSideTransmitter]
+ -[VCAudioStream(Telephony) getCodecModeChangeEvent:forCodecBitrate:payload:].cold.2
+ -[VCAudioStream(Telephony) handleCodecModeChangeEvent:].cold.2
+ -[VCAudioStream(Telephony) handleCodecModeChangeEvent:].cold.3
+ -[VCAudioStream(Telephony) rateAdaptation:targetBitrateDidChange:rateChangeCounter:].cold.3
+ -[VCAudioStreamGroupCommon configureAudioIOWithDeviceRole:operatingMode:].cold.1
+ -[VCAudioStreamGroupCommon configureStreams:withRateControlConfig:].cold.2
+ -[VCAudioStreamGroupCommon operatingMode]
+ -[VCAudioStreamReceiveGroup operatingMode]
+ -[VCAudioStreamSendGroup didStart]
+ -[VCAudioStreamSendGroup operatingMode]
+ -[VCAudioStreamSendGroup reportOperatingMode:]
+ -[VCCallSession newMediaBlobWithRemoteMediaBlob:localCallID:isLowBitrateCodecPreferred:].cold.5
+ -[VCCallSession newMediaBlobWithRemoteMediaBlob:localCallID:isLowBitrateCodecPreferred:].cold.6
+ -[VCCallSession(PrivateMethods) sendSIPInviteWithError:].cold.6
+ -[VCCallSession(VideoConferencing) createVideoReceiverWithReportingAgent:fecHeaderV1Enabled:videoJBEnabled:error:].cold.1
+ -[VCCannedAudioInjectorConfig isValid].cold.7
+ -[VCCaptionsStreamSendGroup operatingMode]
+ -[VCConnectionManager checkpointPrimaryConnection:].cold.1
+ -[VCConnectionManager processConnectionHealthFromControlInfo:].cold.1
+ -[VCConnectionManagerIDS applyConstrainWithThreshold:inBandwidth:thredshold:].cold.1
+ -[VCConnectionSelector isPrimaryConnectionSameAsConnection:].cold.3
+ -[VCConnectionStatisticsCollector addConnectionBasedTopPacketCountsTelemetry:reportingKey:reportingTickCounts:mapLinkIDToLinkUUID:packetCountsPerConnection:].cold.1
+ -[VCConnectionStatisticsCollector connectionBasedTopPacketCountsWithUpdateTickCounts:isOutgoing:].cold.2
+ -[VCConnectionStatisticsCollector updateHistory:].cold.1
+ -[VCControlChannelDialog sendReliableMessage:withTopic:timeout:withOptions:].cold.1
+ -[VCControlChannelDialog sendReliableMessage:withTopic:timeout:withOptions:].cold.2
+ -[VCControlChannelDialogV1 newDataFromMessage:topic:transactionID:isReliable:transactionDelegate:].cold.2
+ -[VCControlChannelDialogV1 newDataFromMessage:topic:transactionID:isReliable:transactionDelegate:].cold.3
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.2
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.3
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.4
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.5
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.6
+ -[VCControlChannelDialogV1 processMessageData:participantID:topic:transactionID:messageStatus:isInternalMessage:].cold.7
+ -[VCControlChannelDialogV2 initWithSessionID:participantID:participantUUID:participantConfig:transactionDelegate:].cold.1
+ -[VCControlChannelDialogV2 initWithSessionID:participantID:participantUUID:participantConfig:transactionDelegate:].cold.2
+ -[VCControlChannelDialogV2 initWithSessionID:participantID:participantUUID:participantConfig:transactionDelegate:].cold.3
+ -[VCControlChannelMultiWay(Encryption) updateEncryption:derivedSSRC:].cold.4
+ -[VCDatagramChannelIDS sharedIDSService].cold.1
+ -[VCDatagramChannelManager addDatagramChannelWithDescriptor:eventHandler:writeCompletionHandler:error:].cold.3
+ -[VCDefaults forceMultiwayHWI].cold.1
+ -[VCDisplayLink activate].cold.1
+ -[VCDisplayLink activate].cold.2
+ -[VCDisplayLink initWithHandler:preferredFrameRate:].cold.3
+ -[VCDisplayLink initWithHandler:preferredFrameRate:].cold.4
+ -[VCIDSSessionInfoSynchronizer sendVCIDSSessionInfoSubscribedStreamIDs:].cold.3
+ -[VCImageQueue createCAContextWithSize:].cold.6
+ -[VCMacScreenCaptureScreenCaptureKit stream:didOutputSampleBuffer:ofType:].cold.15
+ -[VCMediaControlInfoFaceTimeVideo configureWithBuffer:length:optionalControlInfo:].cold.10
+ -[VCMediaControlInfoFaceTimeVideo configureWithBuffer:length:optionalControlInfo:].cold.9
+ -[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:].cold.1
+ -[VCMediaNegotiationBlobV2MomentsSettings(Utils) initWithVideoCodecs:imageTypes:capabilitiesOneToOne:capabilitiesMultiway:].cold.1
+ -[VCMediaNegotiationBlobV2SettingsU1(Utils) loadEncodeDecodeFeatures:].cold.1
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) initSSRC:].cold.1
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) initSSRC:].cold.2
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) initWithStreamConfig:payloadConfigs:streamGroupID:].cold.6
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) optionalPackedPayloaWithDefaultConfig:].cold.1
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) optionalPackedPayloaWithDefaultConfig:].cold.2
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) optionalPackedPayloaWithDefaultConfig:].cold.3
+ -[VCMediaNegotiationBlobV2StreamGroupStream(Utils) streamConfigWithPayloadConfigs:payloadConfigSampleRates:streamGroupID:].cold.7
+ -[VCMediaNegotiator negotiateMomentsWithMomentsSettings:].cold.1
+ -[VCMediaNegotiator negotiateVideoSettings:].cold.6
+ -[VCMediaNegotiator selectBestVideoRuleForTransport:payload:encodingType:localVideoRuleCollection:remoteVideoSettings:negotiatedVideoSettings:isScreen:].cold.1
+ -[VCMediaNegotiator setupCaptionsForMediaBlob:].cold.2
+ -[VCMediaNegotiator setupMomentsForMediaBlob:].cold.2
+ -[VCMediaNegotiatorLocalConfiguration setupBandwidthConfigurationsWithArbiter:].cold.3
+ -[VCMediaNegotiatorLocalConfiguration setupBandwidthExtensionConfiguration:].cold.4
+ -[VCMediaNegotiatorStreamGroupU1Configuration initStreamGroupU1ConfigForGroupId:withLocalConfig:].cold.2
+ -[VCMediaNegotiatorV2 negotiateStreamGroupConfig:remoteInviteBlob:].cold.2
+ -[VCMediaNegotiatorV2 selectBestDecodeVideoRuleForTransport:payload:localVideoRuleCollection:remoteVideoRuleCollection:].cold.1
+ -[VCMediaNegotiatorV2 selectBestDecodeVideoRuleForTransport:payload:localVideoRuleCollection:remoteVideoRuleCollection:].cold.2
+ -[VCMediaNegotiatorV2 setupNegotiatedMomentsResultsWithRemoteMediaBlob:].cold.1
+ -[VCMediaNegotiatorV2 setupNegotiatedMomentsResultsWithRemoteMediaBlob:].cold.2
+ -[VCMediaNegotiatorV2 setupNegotiatedMomentsResultsWithRemoteMediaBlob:].cold.3
+ -[VCMediaNegotiatorV2 setupNegotiatedMomentsResultsWithRemoteMediaBlob:].cold.4
+ -[VCMediaNegotiatorV2 setupNegotiatedVideoSettingsWithRemoteMediaBlob:].cold.4
+ -[VCMediaNegotiatorV2 setupNegotiatedVideoSettingsWithRemoteMediaBlob:].cold.5
+ -[VCMediaNegotiatorV2 setupNegotiatedVideoSettingsWithRemoteMediaBlob:].cold.6
+ -[VCMediaRecorderHistory handleSinglePendingRequestWithTransactionID:sourceURL:].cold.1
+ -[VCMediaRecorderHistoryBuffer flushBuffer].cold.1
+ -[VCMediaStream getInvalidParamErrorForSetPause:didSucceed:].cold.2
+ -[VCMediaStream setMediaQueueInStreamConfig:].cold.1
+ -[VCMediaStream startMediaTransportsWithError:].cold.1
+ -[VCMediaStreamGroup setParticipantJoinedToFirstMKITimer].cold.3
+ -[VCMediaStreamTransport updateLastGeneratedKeyMaterial].cold.2
+ -[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:]
+ -[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenSpuriousLagDetected]
+ -[VCRateSharingGroup initWithIdentifier:].cold.1
+ -[VCRemoteVideoManager slotForStreamToken:videoMode:].cold.1
+ -[VCSecureDataChannel convertEncryptedData:toData:encrypted:].cold.4
+ -[VCSession dispatchedUpdateConfiguration:].cold.3
+ -[VCSession newEncryptionLabelWithLocalUUID:remoteUUID:].cold.1
+ -[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:].cold.2
+ -[VCSession(OneToOne) startOneToOne].cold.1
+ -[VCSession(OneToOne) startOneToOne].cold.2
+ -[VCSession(OneToOne) startOneToOne].cold.3
+ -[VCSessionMediaStreamPresenceConfigurationProvider newVideoMultiwayConfigWithPList:codecType:streamIDGenerator:ssrc:].cold.21
+ -[VCSessionMessaging newDictionaryFromUnpackedMessageV2:].cold.2
+ -[VCSessionMessaging newDictionaryFromUnpackedMessageV2:].cold.3
+ -[VCSessionMessaging newPackedMessageFromDictionaryV2:].cold.3
+ -[VCSessionParticipant dispatchedSetAudioPaused:].cold.4
+ -[VCSessionParticipant dispatchedSetAudioPaused:].cold.5
+ -[VCSessionParticipant updateMediaStatesWithConfig:].cold.2
+ -[VCSessionParticipantLocal newAudioSendGroupConfigWithStreamGroupID:streamGroupConfiguration:].cold.2
+ -[VCSessionParticipantLocal newVideoSendGroupConfigWithStreamGroupID:streamGroupConfiguration:].cold.2
+ -[VCSessionParticipantRemote addOneToOneStreamConfigToMediaStreamInfo:negotiatorStreamGroupConfig:].cold.3
+ -[VCSessionParticipantRemote addOneToOneStreamConfigToMediaStreamInfo:negotiatorStreamGroupConfig:].cold.4
+ -[VCSessionParticipantRemote isMediaTypeExpected:]
+ -[VCSessionParticipantRemote reportConnectionTimingDispatchedWithStreamGroup:]
+ -[VCSessionParticipantRemote setupAudioStreamConfiguration:withStreamGroupConfig:streamGroupStreamConfig:].cold.2
+ -[VCSessionParticipantRemote setupSpatialAudioWithMetadata:spatialMetadataEntryMap:].cold.5
+ -[VCSessionParticipantRemote setupStreamConfigWithCodecs:streamConfig:codecConfigs:featureStringsDict:].cold.1
+ -[VCSessionParticipantRemote shouldReportConnectionTimingWithStreamGroup:]
+ -[VCSessionParticipantRemote updateCameraUsedForConnectionTiming]
+ -[VCSessionUplinkBandwidthAllocatorOneToOne targetBitratesForStreamToken:targetNetworkBitrate:preferNetworkBitrates:].cold.2
+ -[VCSessionUplinkVideoStreamController handleStreamsResetIDR].cold.1
+ -[VCSessionUplinkVideoStreamController handleStreamsResetIDR].cold.2
+ -[VCSessionUplinkVideoStreamController restart].cold.1
+ -[VCSessionUplinkVideoStreamController setIsLocalOnCellular:cappedVideoStreamIDs:].cold.3
+ -[VCSpeechFrameworkWrapper loadSpeechFramework].cold.1
+ -[VCSpeechFrameworkWrapper loadSpeechFramework].cold.2
+ -[VCStreamIOAudioController startInputForClient:error:].cold.2
+ -[VCStreamIOAudioController startInputForClient:error:].cold.3
+ -[VCStreamIOAudioController startInputForClient:error:].cold.4
+ -[VCStreamInputCaptureSource setDelegate:].cold.1
+ -[VCStreamOutput initWithStreamToken:clientProcessID:delegate:delegateQueue:].cold.2
+ -[VCStreamOutput initWithStreamToken:clientProcessID:delegate:delegateQueue:].cold.3
+ -[VCSystemAudioCapture startAudioQueue].cold.10
+ -[VCSystemAudioCapture startAudioQueue].cold.9
+ -[VCTextReceiver start].cold.1
+ -[VCTransportSessionNW initializeInterfaceType].cold.1
+ -[VCTransportSessionNW initializeInterfaceType].cold.2
+ -[VCTransportSessionNW initializeIsIPv6].cold.1
+ -[VCTransportSessionNW initializeIsIPv6].cold.2
+ -[VCTransportSessionNW initializeNetworkMTU].cold.1
+ -[VCTransportSessionSocket setRemoteAddress:remoteRTCPPort:].cold.4
+ -[VCVideoCapture addSink:].cold.1
+ -[VCVideoCapture removeSink:].cold.1
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.4
+ -[VCVideoCaptureServer setThermalLightMitigationsEnabled:]
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupH264Rules].cold.4
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.10
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.11
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.4
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.5
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.6
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.7
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.8
+ -[VCVideoRuleCollectionsScreenAirplayEmbedded setupHEVCRules].cold.9
+ -[VCVideoRuleCollectionsScreenAirplayMac setupH264Rules].cold.1
+ -[VCVideoRuleCollectionsScreenAirplayMac setupH264Rules].cold.2
+ -[VCVideoRuleCollectionsScreenAirplayMac setupHEVCRules].cold.1
+ -[VCVideoRuleCollectionsScreenAirplayMac setupHEVCRules].cold.2
+ -[VCVideoRuleCollectionsScreenSecondaryEmbedded setupH264Rules].cold.4
+ -[VCVideoRuleCollectionsScreenSecondaryEmbedded setupH264Rules].cold.5
+ -[VCVideoRuleCollectionsScreenSecondaryEmbedded setupHEVCRules].cold.4
+ -[VCVideoRuleCollectionsScreenSecondaryMac setupH264Rules].cold.1
+ -[VCVideoRuleCollectionsScreenSecondaryMac setupH264Rules].cold.2
+ -[VCVideoRuleCollectionsScreenSecondaryMac setupHEVCRules].cold.1
+ -[VCVideoRuleCollectionsScreenSecondaryMac setupHEVCRules].cold.2
+ -[VCVideoStream enableRateControlFeebackInConfig:].cold.1
+ -[VCVideoStream enableRedundancyController:].cold.2
+ -[VCVideoStream setLocalParticipantInfo:networkSockets:withError:]
+ -[VCVideoStream setupInternalRedundancyControllerWithStreamConfig:].cold.2
+ -[VCVideoStreamReceiver createDecodeSession:].cold.3
+ -[VCVideoStreamReceiver createDecodeSession:].cold.4
+ -[VCVideoTransmitterDefault initWithConfig:].cold.2
+ -[VCVideoTransmitterDefault startVideo].cold.1
+ -[VCVideoTransmitterDefault stopVideo].cold.1
+ -[VCVirtualAVCaptureSession addInput:].cold.1
+ -[VCVirtualAVCaptureSession addOutput:].cold.1
+ -[VCVirtualAVCaptureSession removeInput:].cold.1
+ -[VCVirtualAVCaptureSession removeOutput:].cold.1
+ -[VCVirtualAVCaptureSession startInputDevices].cold.1
+ -[VCVirtualAVCaptureSession stopInputDevices].cold.1
+ -[VideoConference setupNATObserver].cold.1
+ -[VideoConference warmupForCall].cold.1
+ AUIOStart.cold.1
+ AUIOStop.cold.1
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table178
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table257
+ GCC_except_table329
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table408
+ GCC_except_table413
+ GCC_except_table420
+ GCC_except_table422
+ GCC_except_table88
+ OBJC_IVAR_$_VCMediaStream._mediaConnectionTimeStartToStartComplete
+ OBJC_IVAR_$_VCRateControlAlgorithmBase._abnormalNetworkDetected
+ OBJC_IVAR_$_VCRateControlOWRDEstimator._previousOOOReceiveTimestamp
+ OBJC_IVAR_$_VCRateControlOWRDEstimator._previousOOOSendTimestamp
+ OBJC_IVAR_$_VCRateControlOWRDEstimator._receiveTimestampOOORecoveredCount
+ OBJC_IVAR_$_VCRateControlOWRDEstimator._sendTimestampOOORecoveredCount
+ OBJC_IVAR_$_VCRateControlOWRDEstimator._spuriousLagWithoutSpikeCount
+ OBJC_IVAR_$_VCSession._thermalLightMitigationsEnabled
+ OBJC_IVAR_$_VCSystemAudioCaptureSession._shouldResetAudioBufferPool
+ OBJC_IVAR_$_VCVideoCaptureServer._thermalLightMitigationsEnabled
+ OBJC_IVAR_$_VCVideoStream._isHomeKitStreamRemote
+ RTCPGetSummaryReportBlock.cold.1
+ RTCPGetSummaryReportBlock.cold.2
+ RTCPGetVoIPMetricsReportBlock.cold.1
+ RTCPGetVoIPMetricsReportBlock.cold.2
+ RTPMediaQueueSecurityCallback.cold.8
+ RTPPackGenericDataPacket.cold.1
+ RTPProcessMediaControlInfo.cold.1
+ RTPRecvRTP.cold.1
+ RTPSendRTCP.cold.23
+ RTPSendRTCP.cold.24
+ RTPSendRTCP.cold.25
+ RTPSetRemoteSSRC.cold.2
+ RTPSetTransportStreams.cold.5
+ SIPStartListen.cold.4
+ SIPStopListenOnInterface.cold.1
+ SRTPVerifyAuthenticationTag.cold.11
+ SRTPVerifyAuthenticationTag.cold.12
+ TPListenOnPhysicalInterface.cold.2
+ VCAudioBufferAllocatorCreate.cold.6
+ VCAudioBufferList_CreateSampleBufferAllocateWithAllocator.cold.1
+ VCAudioBufferList_CreateSampleBufferWithFormatWithAllocator.cold.1
+ VCAudioBufferList_CreateSampleBufferWithFormatWithAllocator.cold.2
+ VCAudioCaptionsCoordinator_PushAudioSamples.cold.5
+ VCAudioDucker_Allocate.cold.2
+ VCAudioDucker_Start.cold.16
+ VCAudioDucker_Start.cold.17
+ VCAudioFrameDelay_Create.cold.7
+ VCAudioIOControllerIOState_RegisterClientIO.cold.1
+ VCAudioIOControllerIOState_RegisterClientIO.cold.2
+ VCAudioIOControllerIOState_RegisterClientIO.cold.3
+ VCAudioIOControllerIOState_UnregisterClientIO.cold.1
+ VCAudioIOControllerIOState_UnregisterClientIO.cold.2
+ VCAudioIOControllerIOState_UnregisterClientIO.cold.3
+ VCAudioIssueDetectorUtil_Configure.cold.1
+ VCAudioIssueDetectorUtil_Configure.cold.2
+ VCAudioIssueDetector_GetReportingStats.cold.1
+ VCAudioIssueDetector_ProcessFrame.cold.1
+ VCAudioLimiter_Allocate.cold.2
+ VCAudioPlayerDTMF_ProcessDTMF.cold.1
+ VCAudioPlayer_GetSamples.cold.4
+ VCAudioPlayer_GetSamples.cold.5
+ VCAudioReceiver_SetupDecoders.cold.3
+ VCAudioReceiver_SetupDecoders.cold.4
+ VCCaptionsDecoder_Decode.cold.4
+ VCCaptionsEncoder_Encode.cold.7
+ VCConnectionHealthMonitor_IsPrimaryConnectionImprovedFromHistory.cold.1
+ VCConnectionHealthMonitor_IsPrimaryConnectionImprovedFromHistory.cold.2
+ VCConnectionHealthMonitor_IsPrimaryConnectionImprovedFromHistory.cold.3
+ VCConnectionHealthMonitor_ReportConnectionHealthWithStatsHistory.cold.1
+ VCConnectionHealthMonitor_ReportConnectionHealthWithStatsHistory.cold.2
+ VCConnectionHealthMonitor_UpdateReceiveStats.cold.1
+ VCConnectionManager_AreAllLinkProbingTriggersInactive.cold.1
+ VCConnectionManager_CopySuggestedLinkTypeCombo.cold.1
+ VCConnectionManager_IsDuplicationConnectionCandidate.cold.1
+ VCConnectionManager_UpdateReceivedPacketsAndBytes.cold.1
+ VCConnectionManager_UseCellPrimaryInterface.cold.1
+ VCConnectionSelector_UpdateConnectionForDuplication.cold.1
+ VCConnectionSelector_UpdateConnectionForDuplication.cold.2
+ VCConnection_ReportingConnectionInterface.cold.1
+ VCConnection_ReportingConnectionType.cold.1
+ VCCryptor_Create.cold.6
+ VCCryptor_Encrypt.cold.12
+ VCDuplicationHandler_EnableDuplication.cold.1
+ VCDuplicationHandler_HandleDuplicationStateUpdateEvent.cold.1
+ VCFECFeedbackAnalyzer_Create.cold.6
+ VCFECGenerator_Create.cold.9
+ VCFeatureFlagManager_CallRecordingEnabled.cold.1
+ VCFeatureFlagManager_FoveationEnabled.cold.1
+ VCFeatureFlagManager_LocalRecordingEnabled.cold.1
+ VCFeatureFlagManager_PreviewMSROptimizationForEmbedded.cold.1
+ VCFeatureFlagManager_RecordingResiliencyEnabled.cold.1
+ VCFeatureFlagManager_SessionBasedMutingEnabled.cold.1
+ VCFeatureFlagManager_SkipNonInfraWiFiAssertion.cold.1
+ VCFeatureFlagManager_U1AuthTagEnabled.cold.1
+ VCFeatureFlagManager_UseAnalyzerSpeechAPI.cold.1
+ VCFeatureFlagManager_UseAvconferenced.cold.1
+ VCFeatureFlagManager_UseShortMKI.cold.1
+ VCFeatureFlagManager_UseTLE.cold.1
+ VCFramingOverheadCalculationUtils_PerPacketMediaFramingOverheadWithRTPHandle.cold.2
+ VCFramingOverheadCalculationUtils_PerPacketMediaFramingOverheadWithRTPHandle.cold.3
+ VCImageQueue_EnqueueAttributes.cold.1
+ VCJBTargetEstimatorSynchronizer_Create.cold.5
+ VCMediaControlInfoFaceTimeVideo_SerializeBuffer.cold.3
+ VCMediaControlInfoSerializeWithData.cold.6
+ VCMediaControlInfoUnserializeWithData.cold.6
+ VCMediaControlInfoUnserializeWithData.cold.7
+ VCMediaQueuePacketBundler_AddPacket.cold.5
+ VCMediaQueuePacketBundler_Create.cold.4
+ VCMediaQueueSendProc.cold.1
+ VCMediaQueue_AddPacket.cold.2
+ VCMediaQueue_Create.cold.9
+ VCMediaQueue_FreeMediaPacket.cold.3
+ VCMediaQueue_FreeMediaPacket.cold.4
+ VCMediaRecorderHistoryBuffer_UpdateBufferWithSample.cold.5
+ VCMediaRecorderHistory_AddLocalVideoSampleBuffer.cold.2
+ VCMemoryUtil_IsAddressSanitizerEnabled.cold.1
+ VCMemoryUtil_IsProbabilisticGuardMallocEnabled.cold.1
+ VCNACKConsumer_Create.cold.5
+ VCNACKGenerator_Create.cold.7
+ VCNWConnectionMonitorUtils_GetCDRXCycleFromNWNotification.cold.1
+ VCNetworkConditionMonitor_Create.cold.6
+ VCOverlayManager_createOverlaySourceForToken.cold.1
+ VCOverlayManager_dispatchedIsOverlayEnabled.cold.1
+ VCOverlayManager_dispatchedIsOverlayEnabled.cold.2
+ VCOverlayManager_isOverlayEnabled.cold.1
+ VCOverlayManager_registerOverlayForToken.cold.1
+ VCOverlayManager_releaseOverlaySourceWithToken.cold.1
+ VCOverlayManager_unregisterOverlayForToken.cold.1
+ VCOverlayManager_updateOverlayEnabledState.cold.1
+ VCOverlaySource_Create.cold.6
+ VCPacketBundler_BundleAudio.cold.2
+ VCPacketBundler_BundleAudio.cold.3
+ VCPacketBundler_BundleAudio.cold.4
+ VCPacketBundler_ExtractBundledPackets.cold.1
+ VCPacketFilterGetClassID.cold.1
+ VCPixelBufferOverlay_updateOverlayWithPixelBuffer.cold.1
+ VCPixelBufferOverlay_updateOverlayWithPixelBuffer.cold.2
+ VCPixelTransferSession_TransferPixelBuffer.cold.4
+ VCRateControlAlgorithmStabilizedNOWRDPriv_UpdateInternalStatistics.cold.3
+ VCRemoteVideoManager_DefaultManager.cold.1
+ VCSFrameCryptorH264_Decrypt.cold.8
+ VCSFrameCryptorH264_Encrypt.cold.14
+ VCScreenCaptureManager_SharedInstance.cold.2
+ VCSecurityKeyHolder_Create.cold.6
+ VCSignalHandler_Initialize.cold.1
+ VCSpatialAudioMetadata_Create.cold.12
+ VCSpatialAudioMetadata_Create.cold.13
+ VCSpatialAudioMetadata_CreateEntry.cold.5
+ VCStreamInputUtil_DecodeFormatDescription.cold.11
+ VCStreamInputUtil_DecodeSampleBuffer.cold.7
+ VCStreamInputUtil_DecodeSampleBuffer.cold.8
+ VCTransportStreamGetClassID.cold.1
+ VCTransportStreamRunLoopGetClassID.cold.1
+ VCVideoStreamEncoderProc.cold.2
+ VCVoiceDetector_Create.cold.4
+ VCWRMHandler_ProcessLocalWRMNotification.cold.1
+ VCWRMHandler_ShouldForceWRMRecommendationUsingUserDefaults.cold.1
+ VCWRMHandler_ShouldRequestWRMNotificationWithDuplicationReason.cold.1
+ VCWRMHandler_UpdateWRMNotificationRequestTime.cold.1
+ VRLogfileZip.cold.1
+ VRLogfileZip.cold.2
+ VTP_CopyPreferredSendQueue.cold.3
+ VTP_NWConnectionContext.cold.1
+ VTP_NWConnectionQueue.cold.1
+ VTP_ProcessPacketType.cold.10
+ VTP_ProcessPacketType.cold.11
+ VTP_ProcessPacketType.cold.12
+ VTP_ProcessPacketType.cold.13
+ VTP_ProcessPacketType.cold.14
+ VTP_ProcessPacketType.cold.15
+ VTP_ProcessPacketType.cold.16
+ VTP_ProcessPacketType.cold.17
+ VTP_ProcessPacketType.cold.9
+ VTP_Send.cold.6
+ VTP_Send.cold.7
+ VTP_Send.cold.8
+ VTU_ReallocPktsInfo.cold.7
+ VideoPacketBuffer_UpdateMaxFrameBurstLossStatistics.cold.5
+ VideoTransmitter_EncoderProc.cold.3
+ VideoTransmitter_RetransmitPackets.cold.2
+ _OBJC_$_PROP_LIST_VCVideoCaptureServer.835
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _RTCPPacketCallback.cold.2
+ _RTPGetRTPSocketForMediaQueue.cold.3
+ _RTPRecvWithSocket.cold.2
+ _RTPSocketRTPAndBBNoteCallback.cold.3
+ _RTPSocketRTPAndBBNoteCallback.cold.4
+ _RTPTransportStreamRTCPCallback.cold.3
+ _RTPTransportStreamRTPAndBBNoteCallback.cold.3
+ _RTPTransport_ParseMediaPacket.cold.19
+ _RTPTransport_ParseMediaPacket.cold.20
+ _VCAbTestThermalLightMitigationsEnabled
+ _VCAudioIOControllerIOState_CompareControllerEntries
+ _VCAudioIOControllerIOState_NewAudioEvent
+ _VCAudioIOControllerIOState_RegisterClientIO
+ _VCAudioIOControllerIOState_ReleaseAudioEvent
+ _VCAudioIOControllerIOState_UnregisterClientIO
+ _VCAudioReceiver_HandleRTPPacket.cold.13
+ _VCAudioStreamGroup_AddSyncDestination.cold.2
+ _VCAudioStream_ActiveStreamChangeCallback.cold.1
+ _VCAudioTransmitter_SendAudioBundle.cold.8
+ _VCCannedVideoPacketSource_ReadBlockBufferFromFile.cold.5
+ _VCConnectionIDS_ReportingQRServerConfig.cold.2
+ _VCConnectionManager_UseCellPrimaryInterfaceInternal.cold.1
+ _VCConnectionManager_UseCellPrimaryInterfaceInternal.cold.2
+ _VCCryptor_ValidateCryptographyInputParameters.cold.5
+ _VCFECGenerator_Finalize.cold.1
+ _VCJBTargetEstimatorSynchronizer_StoreCurrentSize.cold.1
+ _VCMediaQueue_FreeMediaPacketList.cold.1
+ _VCMediaRecorderHistory_EmitSetVisibleRectSignpost.cold.1
+ _VCOverlayInfo_copyOverlayInfoForToken.cold.1
+ _VCOverlayManager_AddSourceToDictionary.cold.1
+ _VCPacketFilterBBNotificationCopyProperty.cold.3
+ _VCPacketFilterBBNotificationSetProperty.cold.3
+ _VCPacketFilterRTCPCopyProperty.cold.3
+ _VCPacketFilterRTCPCopyProperty.cold.4
+ _VCPacketFilterRTCPCopyProperty.cold.5
+ _VCPacketFilterRTCPSetProperty.cold.3
+ _VCPacketFilterRTPCopyProperty.cold.3
+ _VCPacketFilterRTPSetProperty.cold.3
+ _VCSFrameCryptorH264_FindAndExtractSliceNalu.cold.6
+ _VCSFrameCryptorH264_FindAndExtractSliceNalu.cold.7
+ _VCStreamIOAudioController_SampleBufferCallback.cold.2
+ _VCStreamIOAudioController_SampleBufferCallback.cold.3
+ _VCStreamInputUtil_DecodeDataSampleBuffer.cold.9
+ _VCTransportStreamVTPCopyProperty.cold.2
+ _VCTransportStreamVTPHandlePacketReceived.cold.2
+ _VCTransportStreamVTPHandlePacketReceived.cold.3
+ _VCTransportStreamVTPPerformReceive.cold.2
+ _VCTransportStreamVTPPerformReceive.cold.3
+ _VCTransportStreamVTPPerformReceive.cold.4
+ _VCTransportStreamVTPPerformReceive.cold.5
+ _VCTransportStreamVTPSetProperty.cold.6
+ _VCTransportStreamVTPSetRemoteSSRCOnVFD.cold.5
+ _VCUniqueIDGenerator_GenerateIDInternal.cold.1
+ _VCVideoCaptureServer_ProcessPreviewSampleBuffer.cold.4
+ _VideoReceiver_DecoderCallback.cold.3
+ _VideoReceiver_DecoderCallback.cold.4
+ _VideoReceiver_DequeueAndDecode.cold.13
+ _VideoReceiver_DequeueAndDecode.cold.14
+ _VideoReceiver_DequeueAndDecode.cold.15
+ _VideoReceiver_DequeueAndDecode.cold.16
+ _VideoReceiver_EnqueueDecodedFrameForDisplay.cold.2
+ _VideoReceiver_RTPPacketCallback.cold.1
+ _VideoTransmitter_RetransmitPacketDispatched.cold.1
+ _VideoTransmitter_UpdateCompoundStreamIDs.cold.1
+ _ZL23AUIOSetupSystemAudioTapP7tagAUIOdj.cold.2
+ _ZL23AUIOSetupSystemAudioTapP7tagAUIOdj.cold.3
+ _ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev.259
+ _ZTINSt3__112system_errorE.127
+ _ZTSNSt3__112system_errorE.128
+ __23-[AVCPacketRelay start]_block_invoke.cold.1
+ __35-[VCVideoStream updateVideoConfig:]_block_invoke.167
+ __36-[VCVideoStream setupReportingAgent]_block_invoke.228
+ __40-[VCVirtualAVCaptureSession stopRunning]_block_invoke.cold.2
+ __41-[VCVirtualAVCaptureSession startRunning]_block_invoke.cold.2
+ __43-[VCVirtualAVCaptureDevice addDeviceInput:]_block_invoke.cold.1
+ __45-[VCMediaRecorder processRemotePhotoRequest:]_block_invoke.113
+ __45-[VCMediaRecorder processRemotePhotoRequest:]_block_invoke_2.114
+ __45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.60
+ __46-[VCVirtualAVCaptureDevice removeDeviceInput:]_block_invoke.cold.1
+ __48-[VCAudioStreamReceiveGroup addSyncDestination:]_block_invoke.cold.3
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.189
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.203
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.203.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.203.cold.2
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.203.cold.3
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.203.cold.4
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.232
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.247
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.263
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.263.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.278
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.289
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.289.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.296
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.296.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.303
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.303.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.310
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.310.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.317
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.317.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.324
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.324.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.331
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.331.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.338
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.349
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.360
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.362
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.370
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.236
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.255
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.282
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.282.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.345
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.345.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.356
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.356.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.368
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.240
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.240.cold.1
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.257
+ __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.257.cold.1
+ __49-[VCMediaRecorder processRemoteLivePhotoRequest:]_block_invoke.109
+ __49-[VCMediaRecorder processRemoteLivePhotoRequest:]_block_invoke_2.110
+ __50-[AVCBasebandAudioTap unregisterFromTapWithError:]_block_invoke.cold.3
+ __51-[VCAudioStreamReceiveGroup removeSyncDestination:]_block_invoke.cold.3
+ __51-[VCSession(Messaging) setupCellTechChangeMessages]_block_invoke.cold.2
+ __51-[VCSession(Messaging) setupCellTechChangeMessages]_block_invoke.cold.3
+ __54-[VCAudioStreamSendGroup setDeviceRole:operatingMode:]_block_invoke.cold.4
+ __55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.185
+ __55-[VCSessionParticipantRemote setRemoteMediaTypeStates:]_block_invoke.79
+ __59-[VCSessionParticipantLocal streamGroup:didSuspendStreams:]_block_invoke.246
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.104
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.123
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.123.cold.1
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.123.cold.2
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.128
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.153
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.77
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.93.cold.1
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.95
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_2.130
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_3.135
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_4.143
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_5.148
+ __65-[VCVirtualAVCaptureDevice configureResizingConverterWithFormat:]_block_invoke.cold.2
+ __70-[VCIDSSessionInfoSynchronizer setVCIDSSessionInfoPublishedStreamIDs:]_block_invoke.cold.2
+ __70-[VCIDSSessionInfoSynchronizer setVCIDSSessionInfoPublishedStreamIDs:]_block_invoke.cold.3
+ __81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.134
+ __81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.136
+ __84-[VCSecureDataChannel initWithLocalCallID:remoteCallID:isCaller:sharedSecret:error:]_block_invoke.cold.3
+ __VCAudioPlayer_DecodeDup
+ __VCAudioStreamSendGroup_UpdateActiveAudioStreams_block_invoke.176
+ __VCFeatureFlagManager_U1AuthTagEnabled_block_invoke.cold.1
+ __VRDump_VideoReceiverDumpEventType_EventNameForType
+ __VTP_NWConnectionQueue_block_invoke.cold.1
+ __VideoReceiver_HandlePrecedingLossOnBaseLayerOfTemporalStream
+ __ZNKSt3__16vectorI24CAStreamBasicDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110shared_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS4_EEEENS1_23shared_instance_managerIS4_E8observerEEEE18__enable_weak_thisB8ne190102ISB_SB_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110unique_ptrI9DFTSetupsNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__114__split_bufferINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEERNS_9allocatorISD_EEED2Ev
+ __ZNSt3__115allocate_sharedB8ne190102IN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS4_EEEENS1_23shared_instance_managerIS4_E8observerEEENS_9allocatorISB_EEJS7_SA_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI24CAStreamBasicDescriptionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI32tagVCAudioHALPluginTimestampInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSI_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEEC2B8ne190102EmRKS1_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne190102IPKjS6_EEvT_T0_m
+ __ZNSt3__19remove_ifB8ne190102INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___47-[AVConferencePreview applyTransform:forLayer:]_block_invoke
+ ___53+[LogDumpUtility createLogDumpListSortedByTimestamp:]_block_invoke
+ ___58-[VCVideoCaptureServer setThermalLightMitigationsEnabled:]_block_invoke
+ ___AVCRateController_SetupDelayedReportingSmartBrake_block_invoke.877
+ ___VCMediaQueue_ReportingRegisterPeriodicTask_block_invoke.cold.1
+ ___VCUtil_GenerateSpindump_block_invoke.114
+ ___VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.843
+ ___VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.845
+ ___VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.840
+ ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.861
+ ___ZL31_AUIOSetupDefaultDeviceListenerP9tagHANDLEP7tagAUIO_block_invoke.cold.3
+ ___block_descriptor_168_e8_32o_e5_v8?0l
+ __block_descriptor_tmp.110
+ __block_descriptor_tmp.116
+ __block_descriptor_tmp.117
+ __block_descriptor_tmp.121
+ __block_descriptor_tmp.432
+ __block_descriptor_tmp.481
+ __block_descriptor_tmp.483
+ __block_literal_global.1043
+ __block_literal_global.120
+ __block_literal_global.124
+ __block_literal_global.191
+ __block_literal_global.234
+ __block_literal_global.238
+ __block_literal_global.249
+ __block_literal_global.265
+ __block_literal_global.291
+ __block_literal_global.298
+ __block_literal_global.305
+ __block_literal_global.312
+ __block_literal_global.319
+ __block_literal_global.326
+ __block_literal_global.340
+ __block_literal_global.347
+ __block_literal_global.351
+ __block_literal_global.358
+ __block_literal_global.47
+ __block_literal_global.49
+ __block_literal_global.89
+ _network_config_get_l4s_enabled
+ _objc_msgSend$applyTransform:forLayer:
+ _objc_msgSend$applyVoiceMixingMedia
+ _objc_msgSend$cStringFromOperatingMode:
+ _objc_msgSend$createLogDumpListSortedByTimestamp:
+ _objc_msgSend$isMediaTypeExpected:
+ _objc_msgSend$isVideoSettingsAspectRatioOverrideSupported
+ _objc_msgSend$removeLogDumpsInDirectory:olderThan:
+ _objc_msgSend$reportConnectionTimingDispatchedWithStreamGroup:
+ _objc_msgSend$reportOperatingMode:
+ _objc_msgSend$setCompanionSettingsVideoDataOutput:
+ _objc_msgSend$setThermalLightMitigationsEnabled:
+ _objc_msgSend$setVideoSettingsAspectRatioOverrideEnabled:
+ _objc_msgSend$shouldCreateReceiveSideTransmitter
+ _objc_msgSend$shouldReportConnectionTimingWithStreamGroup:
+ _objc_msgSend$shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:
+ _objc_msgSend$shouldResumeOWRDEstimationWhenSpuriousLagDetected
+ _objc_msgSend$updateCameraUsedForConnectionTiming
+ _sRTCReportingSafeViewScreenSharingClientName
+ _sRTCReportingSafeViewSystemAudioSharingClientName
+ h264bridge_se_pull.cold.1
+ h264bridge_u_pull.cold.1
+ h264bridge_u_pulllong.cold.1
+ h264bridge_u_pulllong.cold.2
+ h264bridge_ue_pull.cold.1
+ h264bridge_ue_pulllong.cold.1
+ h264bridge_ue_pulllong.cold.2
+ h264bridge_ue_pulllong.cold.3
+ h264bridge_ue_pulllong.cold.4
+ h264bridge_ue_pulllong.cold.5
+ h264bridge_ue_pulllong.cold.6
+ init_APSCopyPairingIdentity.cold.1
+ init_WiFiCopyCurrentNetworkInfoEx.cold.1
+ init_WiFiManagerCreate.cold.1
+ init_WiFiManagerDoApple80211.cold.1
+ init_WiFiManagerSetProperty.cold.1
+ initkWiFiManagerPropertyInterfaceName.cold.1
+ machTimeScale.cold.1
+ setRealTimeConstraints.cold.1
- +[LogDumpUtility createFileListSortedByTimestamp:]
- +[LogDumpUtility removeFilesInDirectory:olderThan:]
- +[VCAirPlayAudioHALPlugin createConduitCreationOptionsWithDeviceInfo:inOptions:].cold.1
- +[VCAirPlayAudioHALPlugin createConduitCreationOptionsWithDeviceInfo:inOptions:].cold.2
- +[VCAirPlayAudioHALPlugin sharedAirPlayAudioHALPluginNullDevice].cold.1
- +[VCAudioHALPluginDevice sharedAudioHALPluginNullDevice].cold.1
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.1
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.2
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.3
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.4
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.5
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.6
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.7
- +[VCSessionParticipant participantDataWithParticipantData:isReinit:].cold.8
- +[VCSystemAudioCapture isValidConfiguration:].cold.10
- +[VCSystemAudioCapture isValidConfiguration:].cold.6
- +[VCSystemAudioCapture isValidConfiguration:].cold.7
- +[VCSystemAudioCapture isValidConfiguration:].cold.8
- +[VCSystemAudioCapture isValidConfiguration:].cold.9
- +[VCSystemAudioCaptureController isValidConfiguration:].cold.5
- +[VCSystemAudioCaptureController isValidConfiguration:].cold.6
- +[VCSystemAudioCaptureController isValidConfiguration:].cold.7
- +[VCSystemAudioCaptureController isValidConfiguration:].cold.8
- +[VCVideoStreamConfig validateClientDictionary:].cold.1
- +[VCVideoStreamConfig validateClientDictionary:].cold.2
- +[VCVideoStreamConfig validateClientDictionary:].cold.3
- +[VCVideoStreamConfig validateClientDictionary:].cold.4
- -[AVCAudioStream setupAudioStreamInProcessWithClientArgs:networkSockets:error:].cold.1
- -[AVCMediaStreamNegotiator createOffer].cold.5
- -[AVCMediaStreamNegotiator generateMediaStreamConfigurationWithError:].cold.4
- -[AVCMediaStreamNegotiator generateMediaStreamConfigurationWithError:].cold.5
- -[AVCMediaStreamNegotiator generateMediaStreamInitOptionsWithError:].cold.2
- -[AVCMediaStreamNegotiator initWithMode:options:error:].cold.5
- -[AVCMediaStreamNegotiator initWithMode:options:error:].cold.6
- -[AVCMediaStreamNegotiator initWithOffer:options:error:].cold.10
- -[AVCMediaStreamNegotiator initWithOffer:options:error:].cold.11
- -[AVCMediaStreamNegotiator initWithOffer:options:error:].cold.12
- -[AVCMediaStreamNegotiator setAnswer:withError:].cold.6
- -[AVCPreviewCALayerHost layoutSublayers].cold.1
- -[AVCPreviewCALayerHost layoutSublayers].cold.2
- -[AVCRemoteVideoClient setLayerHostBounds:].cold.1
- -[AVCSession didAddParticipantHandlerWithResult:].cold.1
- -[AVCSessionParticipant storeMediaState:forMediaType:].cold.1
- -[AVCSessionParticipant storeMediaState:forMediaType:].cold.2
- -[AVCStreamInput processOptions:].cold.1
- -[AVCStreamInput processOptions:].cold.2
- -[AVCStreamOutput validateAccessWithProcessName:accessControlPlist:].cold.1
- -[VCAirPlayAudioHALPlugin suspendAndReleaseConduitDeviceLocked].cold.1
- -[VCAnsweringMachine initWithConfiguration:delegate:delegateQueue:].cold.5
- -[VCAnsweringMachine setUpAnnouncementAssetInjection].cold.1
- -[VCAnsweringMachine setUpInternalStateWithConfiguration:].cold.1
- -[VCAnsweringMachine setUpInternalStateWithConfiguration:].cold.2
- -[VCAnsweringMachineManager init].cold.3
- -[VCAudioCaptions recognizerBufferSetupWithError:].cold.1
- -[VCAudioCaptions recognizerBufferSetupWithError:].cold.2
- -[VCAudioManager updateSpatialAudioWithClient:settings:isClientRegistered:].cold.1
- -[VCAudioManager updateVoiceProcessingWithClient:settings:isClientRegistered:].cold.1
- -[VCAudioPowerSpectrumManager dispatchedCleanUpPowerSpectrumSetForCellularTapType:].cold.1
- -[VCAudioStream setupCaptionsCoordinatorsWithFormat:direction:].cold.1
- -[VCAudioStreamGroupCommon initWithConfig:audioCallback:context:audioDirection:stateQueue:].cold.5
- -[VCAudioStreamGroupCommon initWithConfig:audioCallback:context:audioDirection:stateQueue:].cold.6
- -[VCAudioStreamSendGroup setupRedundancyControllerForMode:].cold.1
- -[VCCALayerHost layoutSublayers].cold.1
- -[VCCellularAudioTap registerAudioTapForStreamToken:tapType:].cold.1
- -[VCCellularAudioTap registerAudioTapForStreamToken:tapType:].cold.2
- -[VCCellularAudioTap registerAudioTapForStreamToken:tapType:].cold.3
- -[VCCellularAudioTap startAudioForStreamToken:isInitialization:].cold.1
- -[VCCellularAudioTap stopAudioForStreamToken:isDeinitialization:].cold.1
- -[VCDatagramChannelIDS start].cold.1
- -[VCMacScreenCapture setFrameRate:].cold.1
- -[VCMacScreenCapture setFrameRate:].cold.2
- -[VCMediaControlInfoMultiwayAudio configureWithBuffer:length:optionalControlInfo:].cold.1
- -[VCMediaNegotiationBlobV2CameraSettingsU1(Utils) addVideoRules:encodingType:payload:videoRuleCollections:].cold.1
- -[VCMediaNegotiatorV2 appendMicrophoneOneToOneSettingsToMediaBlob:].cold.1
- -[VCMediaNegotiatorV2 appendMomentsSettingsToMediaBlob:].cold.1
- -[VCMediaNegotiatorV2 negotiationData].cold.1
- -[VCMediaNegotiatorV2 negotiationData].cold.2
- -[VCMediaRecorderHistory dispatchedStartRecordingWithContext:fileURL:completionHandler:].cold.1
- -[VCMediaStreamGroup pauseMediaStreams].cold.1
- -[VCMediaStreamGroup resumeMediaStreams].cold.1
- -[VCMediaStreamTransport setupRTPWithTransportStreams].cold.1
- -[VCNWConnectionInfo newParametersFromConnection].cold.1
- -[VCRateControlSmartBrake bindLSTMBuffers].cold.1
- -[VCSandboxedURL consumeToken].cold.1
- -[VCSandboxedURL consumeToken].cold.2
- -[VCSandboxedURL consumeToken].cold.3
- -[VCScreenCapture processAndSendIdleBlackFrame].cold.1
- -[VCScreenCapture processAndSendIdleBlackFrame].cold.2
- -[VCScreenCapture setFrameRate:].cold.1
- -[VCScreenCaptureManager picker:pickedContentFilter:forStream:error:].cold.1
- -[VCScreenCaptureManager stopScreenShareAndNotifyDelegate:].cold.1
- -[VCSessionParticipant updateMediaState:forStreamGroups:].cold.1
- -[VCSessionParticipantLocal processCachedParticipantData:].cold.1
- -[VCSessionParticipantLocal processCachedParticipantData:].cold.2
- -[VCSessionParticipantLocal processCachedParticipantData:].cold.3
- -[VCSessionParticipantLocal processCachedParticipantData:].cold.4
- -[VCSessionParticipantRemote reportConnectionTimingDispatched]
- -[VCSessionParticipantRemote setupStreamGroupWithConfig:].cold.1
- -[VCSessionParticipantRemote setupStreamGroupWithConfig:].cold.2
- -[VCSessionParticipantRemote setupStreamGroupWithConfig:].cold.3
- -[VCSessionParticipantRemote setupStreamGroupWithConfig:].cold.4
- -[VCSessionParticipantRemote setupStreamGroupWithConfig:].cold.5
- -[VCSessionParticipantRemote spatialMetadataEntryForMediaType:].cold.1
- -[VCStreamInputManager clientProcessDiedWithXPCArguments:result:error:].cold.1
- -[VCStreamOutputManager serviceHandlerStreamOutputTerminateWithArguments:error:].cold.1
- -[VCSystemAudioCapture initWithConfiguration:].cold.10
- -[VCSystemAudioCapture initWithConfiguration:].cold.7
- -[VCSystemAudioCapture initWithConfiguration:].cold.8
- -[VCSystemAudioCapture initWithConfiguration:].cold.9
- -[VCSystemAudioCapture setupCannedAudioInjection].cold.1
- -[VCSystemAudioCapture setupCannedAudioInjection].cold.2
- -[VCSystemAudioCaptureSession createAudioBufferPool].cold.3
- -[VCSystemAudioCaptureSession createAudioBufferPool].cold.4
- -[VCSystemAudioCaptureSession initWithConfiguration:].cold.10
- -[VCSystemAudioCaptureSession initWithConfiguration:].cold.6
- -[VCSystemAudioCaptureSession initWithConfiguration:].cold.7
- -[VCSystemAudioCaptureSession initWithConfiguration:].cold.8
- -[VCSystemAudioCaptureSession initWithConfiguration:].cold.9
- -[VCSystemAudioCaptureSession resetAudioBufferPool]
- -[VCTransportSession createTransportStream:withType:options:].cold.1
- -[VCTransportSession createTransportStream:withType:options:].cold.2
- -[VCTransportSessionIDSMultiLink handleLinkConnectedWithInfo:].cold.1
- -[VCTransportSessionIDSSingleLink createVFD:forStreamType:].cold.1
- -[VCTransportSessionIDSSingleLink createVFD:forStreamType:].cold.2
- -[VCTransportSessionNW createVFD:forStreamType:].cold.1
- -[VCTransportSessionNW createVFD:forStreamType:].cold.2
- -[VCTransportSessionNW createVFD:forStreamType:].cold.3
- -[VCTransportSessionNW createVFD:forStreamType:].cold.4
- -[VCTransportSessionNW createVFD:forStreamType:].cold.5
- -[VCTransportSessionNW createVFD:forStreamType:].cold.6
- -[VCTransportSessionNW destroyNWConnection:].cold.1
- -[VCTransportSessionNW setRemoteAddress:remoteRTCPPort:].cold.1
- -[VCTransportSessionNW setRemoteAddress:remoteRTCPPort:].cold.2
- -[VCTransportSessionProxy createVFD:forStreamType:].cold.1
- -[VCTransportSessionProxy createVFD:forStreamType:].cold.2
- -[VCVideoCaptureServer dispatchedUpdateCaptureRuleForClient:width:height:frameRate:].cold.1
- -[VCVideoCaptureServer setUpImageConverters].cold.1
- -[VCVideoCaptureServer setUpImageConverters].cold.2
- -[VCVideoReceiverDefault initWithConfig:delegate:delegateFunctions:reportingAgent:statisticsCollector:transmitterHandle:].cold.1
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.1
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.2
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.3
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.4
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.5
- -[VCVideoRuleCollectionsCameraEmbedded setupH264Rules].cold.6
- -[VCVideoStreamReceiveGroup setupRedundancyController].cold.1
- -[VCVideoStreamSendGroup dispatchedEnableRedundancy:].cold.1
- -[VCVideoStreamSendGroup setupRedundancyControllerForMode:].cold.1
- -[VCVideoStreamSendGroup uplinkVideoStreamControllerForMode:].cold.1
- EncoderVTSetBitRate.cold.1
- EncoderVTSetBitRate.cold.2
- EncoderVTSetBitRate.cold.3
- GCC_except_table124
- GCC_except_table128
- GCC_except_table182
- GCC_except_table187
- GCC_except_table222
- GCC_except_table225
- GCC_except_table255
- GCC_except_table327
- GCC_except_table389
- GCC_except_table390
- GCC_except_table406
- GCC_except_table407
- GCC_except_table419
- GCC_except_table421
- GCC_except_table72
- GCC_except_table87
- JTargetJBEstimator_Process.cold.1
- JTargetJBEstimator_Process.cold.2
- OBJC_IVAR_$_VCRateControlAlgorithmStabilizedNOWRD._abnormalNetworkDetected
- VCAllocatorFirstCome_Create.cold.4
- VCAudioFrameDelay_GetTypeID.initOnce
- VCAudioFrameDelay_GetTypeID.typeID
- VCAudioIssueDetectorUtil_ProcessFrame.cold.1
- VCAudioPowerSpectrum_PushAudioSamples.cold.23
- VCAudioReceiver_ProcessCellularNetworkNotification.cold.1
- VCAudioReceiver_SendEndCallReport.cold.1
- VCCannedVideoPacketSource_RegisterForCannedReplay.cold.4
- VCCryptorGetTypeID.initOnce
- VCCryptorGetTypeID.typeID
- VCCryptor_Decrypt.cold.1
- VCCryptor_Decrypt.cold.10
- VCCryptor_Decrypt.cold.11
- VCCryptor_Decrypt.cold.12
- VCCryptor_Decrypt.cold.2
- VCCryptor_Decrypt.cold.3
- VCCryptor_Decrypt.cold.4
- VCCryptor_Decrypt.cold.5
- VCCryptor_Decrypt.cold.6
- VCCryptor_Decrypt.cold.7
- VCCryptor_Decrypt.cold.8
- VCCryptor_Decrypt.cold.9
- VCFECFeedbackAnalyzerGetTypeID.initOnce
- VCFECFeedbackAnalyzerGetTypeID.typeID
- VCFECGeneratorGetTypeID.initOnce
- VCFECGeneratorGetTypeID.typeID
- VCJBTargetEstimatorSynchronizerGetTypeID.initOnce
- VCJBTargetEstimatorSynchronizerGetTypeID.typeID
- VCMediaQueuePacketBundlerGetTypeID.initOnce
- VCMediaQueuePacketBundlerGetTypeID.typeID
- VCMediaRecorderHistoryBuffer_DequeueOneFrame.cold.1
- VCNACKConsumerGetTypeID.initOnce
- VCNACKConsumerGetTypeID.typeID
- VCNACKGeneratorGetTypeID.initOnce
- VCNACKGeneratorGetTypeID.typeID
- VCNACKGenerator_UpdatePlayoutRTPTimestamp.cold.1
- VCNetworkConditionMonitorGetTypeID.initOnce
- VCNetworkConditionMonitorGetTypeID.typeID
- VCOverlaySource_GetTypeID.initOnce
- VCOverlaySource_GetTypeID.typeID
- VCRateControlAlgorithmStabilizedNOWRDPriv_DoRateControlWithNWStatistics.cold.1
- VCRateControlAlgorithmStabilizedNOWRDPriv_DoRateControlWithNWStatistics.cold.2
- VCRateControlAlgorithmStabilizedNOWRDPriv_DoRateControlWithNWStatistics.cold.3
- VCRateControlAlgorithmStabilizedNOWRDPriv_ShouldFastRampUp.cold.1
- VCRateControlAlgorithmStabilizedNOWRDPriv_ShouldRampDown.cold.1
- VCRateControlFeedbackController_UpdateTxLinkType.cold.1
- VCRateControlMediaController_ComputePacketLoss.cold.1
- VCRateControlMediaController_MediaQueueRateChangeCounter.cold.1
- VCRateControlMediaController_MediaQueueSettings.cold.1
- VCSecurityKeyHolderGetTypeID.initOnce
- VCSecurityKeyHolderGetTypeID.typeID
- VCSpatialAudioMetadataEntry_GetTypeID.initOnce
- VCSpatialAudioMetadataEntry_GetTypeID.typeID
- VCSpatialAudioMetadata_GetTypeID.initOnce
- VCSpatialAudioMetadata_GetTypeID.typeID
- VTP_Initialize.cold.21
- VTP_Initialize.cold.22
- VTP_Initialize.cold.23
- VTP_Initialize.cold.24
- VTP_SocketWithNWConnection.cold.6
- VTU_SplitGenericDataIntoPackets.cold.1
- VTU_SplitGenericDataIntoPackets.cold.2
- VTU_SplitGenericDataIntoPackets.cold.3
- VTU_SplitGenericDataIntoPackets.cold.4
- VTU_SplitGenericDataIntoPackets.cold.5
- VTU_SplitGenericDataIntoPackets.cold.6
- VTU_SplitGenericDataIntoPackets.cold.7
- VTU_SplitGenericDataIntoPackets.cold.8
- VTU_SplitGenericDataIntoPackets.cold.9
- VideoPacketBuffer_Create.cold.8
- VideoPacketBuffer_Create.cold.9
- VideoTransmitter_CreateHandle.cold.29
- _OBJC_$_PROP_LIST_VCVideoCaptureServer.833
- _RTPEnsureTransportStreamsActivated.cold.1
- _RTPEnsureTransportStreamsDeactivated.cold.1
- _RTPSetCellularUniqueTagOnPacketFilters.cold.1
- _RTPSetCellularUniqueTagOnPacketFilters.cold.2
- _VCAudioIssueDetectorUtil_StateMachine.cold.4
- _VCAudioIssueDetectorUtil_StateMachine.cold.5
- _VCAudioManager_NewAudioEvent
- _VCAudioManager_ReleaseAudioEvent
- _VCAudioPlayerDTMF_ShouldPurgeJitterQueue.cold.1
- _VCAudioReceiver_SendEndCallReport
- _VCAudioStream_NWConnectionNotificationHandler.cold.1
- _VCAudioStream_NWConnectionNotificationHandler.cold.2
- _VCAudioStream_NWConnectionNotificationHandler.cold.3
- _VCAudioStream_NWConnectionNotificationHandler.cold.4
- _VCCannedAudioInjector_AudioConverterInput.cold.1
- _VCCannedAudioInjector_AudioConverterInput.cold.2
- _VCCannedAudioInjector_AudioConverterInput.cold.3
- _VCCannedAudioInjector_AudioConverterInput.cold.4
- _VCCannedVideoPacketSource_ReadDataFromFile.cold.1
- _VCCannedVideoPacketSource_ReadPacketTypeFromFile.cold.1
- _VCMacScreenCapture_handleFrame.cold.1
- _VCMacScreenCapture_handleFrame.cold.2
- _VCMacScreenCapture_handleFrame.cold.3
- _VCMacScreenCapture_handleFrame.cold.4
- _VCMacScreenCapture_handleFrame.cold.5
- _VCMacScreenCapture_handleFrame.cold.6
- _VCMacScreenCapture_handleFrame.cold.7
- _VCMacScreenCapture_handleFrame.cold.8
- _VCMediaQueueGetTypeID.initOnce
- _VCMediaQueueGetTypeID.typeID
- _VCRateControlAlgorithmLowLatencyContinuousTier_DoRateControl.cold.1
- _VCRateControlAlgorithmLowLatencyContinuousTier_DoRateControl.cold.2
- _VCStreamInputUtil_DecodeSampleBufferAttachments.cold.1
- _VCStreamInputUtil_EncodeSampleBufferAttachments.cold.1
- _VCTransportStreamRunLoopVTPIterateTransportStreams.cold.1
- _VCTransportStreamRunLoopVTPIterateTransportStreams.cold.2
- _VCTransportStreamRunLoopVTPUpdateFDSet.cold.1
- _VCTransportStreamRunLoopVTPUpdateFDSet.cold.2
- _VCTransportStreamRunLoopVTPWaitForReceive.cold.1
- _VCTransportStreamRunLoopVTPWaitForReceive.cold.2
- _VCTransportStreamRunLoopVTPWaitForReceive.cold.3
- _VCTransportStreamRunLoopVTPWaitForReceive.cold.4
- _VCTransportStreamRunLoopVTPWaitForReceive.cold.5
- _VCTransportStreamVTPSetPacketFilter.cold.1
- _VCTransportStreamVTPSetPacketFilter.cold.10
- _VCTransportStreamVTPSetPacketFilter.cold.11
- _VCTransportStreamVTPSetPacketFilter.cold.12
- _VCTransportStreamVTPSetPacketFilter.cold.13
- _VCTransportStreamVTPSetPacketFilter.cold.14
- _VCTransportStreamVTPSetPacketFilter.cold.15
- _VCTransportStreamVTPSetPacketFilter.cold.16
- _VCTransportStreamVTPSetPacketFilter.cold.2
- _VCTransportStreamVTPSetPacketFilter.cold.3
- _VCTransportStreamVTPSetPacketFilter.cold.4
- _VCTransportStreamVTPSetPacketFilter.cold.5
- _VCTransportStreamVTPSetPacketFilter.cold.6
- _VCTransportStreamVTPSetPacketFilter.cold.7
- _VCTransportStreamVTPSetPacketFilter.cold.8
- _VCTransportStreamVTPSetPacketFilter.cold.9
- _VCVideoPacketBuffer_AssembleFrame.cold.1
- _VCVideoPacketBuffer_AssembleFrame.cold.2
- _VCVideoPacketBuffer_AssembleFrame.cold.3
- _VCVideoPacketBuffer_AssembleFrame.cold.4
- _VCVideoPacketBuffer_AssembleFrame.cold.5
- _VCVideoPacketBuffer_AssembleFrame.cold.6
- _VCVideoPacketBuffer_AssembleFrame.cold.7
- _VTP_CreatePacketRoutingInfoListWithVFD.cold.1
- _VTP_CreatePacketRoutingInfoListWithVFD.cold.2
- _VTP_CreatePacketRoutingInfoListWithVFD.cold.3
- _VTP_ReportIDSOnTheWireBytesLocked.cold.1
- _VTP_ReportIDSOnTheWireBytesLocked.cold.2
- _VTP_SocketWithRealSocketFromFVDList.cold.7
- _VTP_SocketWithRealSocketFromFVDList.cold.8
- _VTU_ReallocateBuffer.cold.1
- _VideoReceiver_EnqueueFailedFrameToJitterBuffer.cold.1
- _VideoTransmitter_GetStreamIndexFromAttachment.cold.1
- _ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev.279
- _ZTINSt3__112system_errorE.126
- _ZTSNSt3__112system_errorE.127
- __30-[VCTransportSessionIDS start]_block_invoke.40.cold.1
- __35-[VCVideoStream updateVideoConfig:]_block_invoke.165
- __36-[VCVideoStream setupReportingAgent]_block_invoke.226
- __45-[VCMediaRecorder processRemotePhotoRequest:]_block_invoke.115
- __45-[VCMediaRecorder processRemotePhotoRequest:]_block_invoke_2.116
- __45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.59
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.190
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.204
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.204.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.204.cold.2
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.204.cold.3
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.204.cold.4
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.233
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.264
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.264.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.279
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.290
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.290.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.297
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.297.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.304
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.304.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.311
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.311.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.318
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.318.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.325
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.325.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.332
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.332.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.339
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.350
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.361
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.366
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke.373
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.237
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.256
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.283
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.283.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.346
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.346.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.357
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.357.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.370
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.241
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.241.cold.1
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.258
- __48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.258.cold.1
- __49-[VCMediaRecorder processRemoteLivePhotoRequest:]_block_invoke.110
- __49-[VCMediaRecorder processRemoteLivePhotoRequest:]_block_invoke_2.111
- __55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.191
- __55-[VCSessionParticipantRemote setRemoteMediaTypeStates:]_block_invoke.78
- __57-[VCCellularAudioTap removeAudioTapForStreamToken:error:]_block_invoke.cold.1
- __59-[VCSessionParticipantLocal streamGroup:didSuspendStreams:]_block_invoke.245
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.121
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.121.cold.1
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.121.cold.2
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.126
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.151
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.75
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.91
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.91.cold.1
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke.98
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_2.128
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_3.133
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_4.141
- __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_5.146
- __68-[AVCAnsweringMachine registerServerDidDisconnectBlockWithInstance:]_block_invoke.cold.1
- __70-[VCAudioManager setSpatialMetadata:audioSessionId:completionHandler:]_block_invoke.cold.1
- __70-[VCVideoCaptureServer deregisterForVideoFramesFromSource:withClient:]_block_invoke.cold.1
- __81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.140
- __81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.142
- __VCAudioManager_CheckVoiceDetectorEnabled
- __VCAudioManager_RegisterClientIO
- __VCAudioManager_UnregisterClientIO
- __VCAudioManger_CompareControllerEntries
- __VCAudioRelayIOController_CompareControllerEntries
- __VCAudioRelayIOController_RegisterClientIO
- __VCAudioRelayIOController_UnregisterClientIO
- __VCAudioStreamSendGroup_UpdateActiveAudioStreams_block_invoke.166
- __VCMediaQueue_ReleaseExternalDataBuffer
- __VCRateControlAlgorithmStabilizedNOWRD_CongestionLevelThreshold
- __VTP_CreatePacketRoutingInfoListWithVFD
- __VideoReceiver_ResetStreamStats
- __ZNKSt3__16vectorI24CAStreamBasicDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110shared_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS4_EEEENS1_23shared_instance_managerIS4_E8observerEEEE18__enable_weak_thisB8ne180100ISB_SB_vEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110unique_ptrI9DFTSetupsNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__115allocate_sharedB8ne180100IN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS4_EEEENS1_23shared_instance_managerIS4_E8observerEEENS_9allocatorISB_EEJS7_SA_EvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI24CAStreamBasicDescriptionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI32tagVCAudioHALPluginTimestampInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI32tagVCAudioHALPluginTimestampInfoNS_9allocatorIS1_EEEC2EmRKS1_
- __ZNSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE12emplace_backIJRNS_10shared_ptrISC_EEEEERSD_DpOT_
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne180100IPKjS6_EEvT_T0_m
- __ZNSt3__19remove_ifB8ne180100INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI9DFTSetupsNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ56+[VCAudioHALPluginDevice sharedAudioHALPluginNullDevice]E23_sharedPlugInNullDevice
- __ZZ56+[VCAudioHALPluginDevice sharedAudioHALPluginNullDevice]E9onceToken
- ___50+[LogDumpUtility createFileListSortedByTimestamp:]_block_invoke
- ___AVCRateController_SetupDelayedReportingSmartBrake_block_invoke.874
- ___VCAudioReceiver_RegisterStatistics_block_invoke.cold.1
- ___VCAudioReceiver_RegisterStatistics_block_invoke.cold.2
- ___VCUtil_GenerateSpindump_block_invoke.116
- ___VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.841
- ___VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.843
- ___VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.838
- ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.854
- __block_descriptor_tmp.112
- __block_descriptor_tmp.118
- __block_descriptor_tmp.119
- __block_descriptor_tmp.123
- __block_descriptor_tmp.426
- __block_descriptor_tmp.475
- __block_descriptor_tmp.477
- __block_literal_global.1044
- __block_literal_global.121
- __block_literal_global.125
- __block_literal_global.192
- __block_literal_global.195
- __block_literal_global.235
- __block_literal_global.239
- __block_literal_global.243
- __block_literal_global.250
- __block_literal_global.266
- __block_literal_global.285
- __block_literal_global.292
- __block_literal_global.299
- __block_literal_global.306
- __block_literal_global.313
- __block_literal_global.320
- __block_literal_global.334
- __block_literal_global.341
- __block_literal_global.348
- __block_literal_global.359
- __block_literal_global.368
- __block_literal_global.46
- __block_literal_global.83
- _fmodf
- _fuzz_packet
- _getkWiFiManagerPropertyInterfaceName
- _objc_msgSend$createFileListSortedByTimestamp:
- _objc_msgSend$removeFilesInDirectory:olderThan:
- _objc_msgSend$reportConnectionTimingDispatched
- _objc_msgSend$resetAudioBufferPool
- _softLink_WiFiManagerCreate
- _softLink_WiFiManagerDoApple80211
- _softLink_WiFiManagerSetProperty
- machTimeScale.did_init
- machTimeScale.timeScale
- sharedAirPlayAudioHALPluginNullDevice._sharedAirPlayHALPlugin
- sharedAirPlayAudioHALPluginNullDevice.onceToken
CStrings:
+ " [%s] %s:%d %@(%p) Choosing to stop capture, streamGroupMode=%u audioIOState=%u"
+ " [%s] %s:%d %@(%p) Skipping configuration because device role and operating mode have NOT changed"
+ " [%s] %s:%d %@(%p) _captureFormatPrefer16By9ForSquare=%d"
+ " [%s] %s:%d %@(%p) isAnyCameraMediaTypeEnabled=%{BOOL}d operatingMode=%s [%u] oneToOneModeEnabled=%{BOOL}d"
+ " [%s] %s:%d %@(%p) isMixingVoiceWithMediaEnabled=%d"
+ " [%s] %s:%d %@(%p) isMixingVoiceWithMediaEnabled=%d failed. result=%08X"
+ " [%s] %s:%d %sEntry is NULL"
+ " [%s] %s:%d %sEntry reference is NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCMediaStreamConfig.m:%d: Unexpected pixel format type: %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: %s: failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverProc failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: AVCPacketRelayDriverProc start failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: CreateHandle failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: calloc(%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: %@ supports (%dx%d) @[%f-%f] '%s'"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIO Get Camera List failed %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyData for kCMIOStreamPropertyFrameRateRanges failed error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyData kCMIODevicePropertySuspendedByUser failed with %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyDataSize for kCMIOStreamPropertyFrameRateRanges failed error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: frameRateRanges malloc failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: isFrameRateRangeSupportedForStreamID failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: Invalid network outage detection event passed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: Processing event=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: brokenBackhaulDetectionStarted=%d "
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: connectionManager must not be NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isLocal=%d isLocalNetworkBroken=%d isRemoteNetworkBroken=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isLocalActiveOnCellular=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isRemoteNetworkQualityBad=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/FECUtil.c:%d: Bad FEC header (%d)!"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/FECUtil.c:%d: WRONG, cannot have %d packets per group"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: connect refused (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: connect timed out %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: read failed with error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: select failed for connect (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: server terminated"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: write failed with error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: connectTCPSocket: connect failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: createTCPSocket: bind() failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: createTCPSocket: socket() failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: CreateHandle failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: MQ_Rexmit: missing packet wSN(%04X) iSN(%08X)\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: Media queue closing, free packet!"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: MediaQueue_LastSN failed (%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: Request buffer size(%d) too big!"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: calloc(%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: pthread_create(MediaQueueSendProc) failed (%08X)\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP APP packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP PSFB ALFB packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Drop RTCP packet from a unknown connection."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add RTCP header"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add the Statistics Summary Report Block. status=%X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add the VoIP Metrics Report Block. status=%X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to finalize the XR packet. status=%X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP BYE message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP FIR message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP NACK message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP PSFB message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP Packet(packetType=%d, version=%d, count=%d, padding=%d) useReducedSizePackets=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP RR packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP RTPFB message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP SDES message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP SR packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP header"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP packet length"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP version"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Not enough space for the RTCP XR packet"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: RTCP packet failed Version, padding bit, packet type check"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Received RTCP SR packet PayloadType=%d NTP Seconds=%u RTPTimestamp=%u"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Sending RTCP SR packet PayloadType=%d NTP Seconds=%u RTPTimestamp=%u"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Unsupported PSFB ALFB app type=%u"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH263.c:%d: Invalid length (%d) for H263PHMODEA"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH263.c:%d: Invalid length (%d) for H263PHMODEB"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: Invalid fragmentation unit length (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: Invalid packet size, does not include DON: unit length (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: data size too big (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPLRP.c:%d: Invalid aggregation unit length (%d) for H264NALU_STAP_A packet, discarded."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPLRP.c:%d: Invalid fragmentation unit length (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Bad RTP extension length (%ld)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Bad version(%u) of RTP header extension!"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: CreateHandle failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Drop RTP packet from a unknown source"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate send buffer"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the RTP block buffer allocator"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the block buffer allocator"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the channel data format allocator"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the packet metadata allocator"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the rtpPacket allocator"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to create the rtcpPacket allocator (error:%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: First RTP packet had sequence number 0. Dropping"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: RTP Handle invalid"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: RTP extension length(%u) invalid."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Unknown Payload Type(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: VTP_SocketWithIDSDescriptor for RTCP failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: VTP_SocketWithIDSDescriptor for RTP failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Wrong connection index: %d."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: bind on %s failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: calloc failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: getaddrinfo(%s,%s) failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: malloc(%zu) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: set sockopt IP_BOUND_IF failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: socket failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPUncompressedVideo.c:%d: data size too big (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPrivatePropertyAMRPayloadFormat %d with error %08x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPropertyBitRateControlMode with error %08x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPropertyConcealmentMode %d with error %08x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioConverterPrimeMethod with error %08x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set DTX encoder primer sample buffer[%p] bytes[%d] err[%d]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set bitrate[%d]: %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set max packet size[%d] for bitrate[%d] with err[%d]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/Util.c:%d: CreateHandle failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/Util.c:%d: calloc failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: %s: Can't extract avcC from format description"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: %s: Can't extract format description from saved buffer"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: Created encoder session=%p with tilesPerframe=%d, pixelFormat=%s, width=%d, height=%d codec=%s videoTransmitterHandle=0x%x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: Encoder callback is NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: HandoverReport: fUsingCellular=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: VCPCompressionSessionCreate %i"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: VCPCompressionSessionEncodeFrame failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: readAVCCAndEncodeH264SPSPPS %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: Can't allocate imageDescDataBE"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: Can't recreate avcC from SPS/PPS %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreate: error: %X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreate: error: %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreateFromBigEndianImageDescriptionData: error: %d "
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: ReadCodecConfigParams: error: %X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: VCPDecompressionSessionDecodeFrame: error: %d for stream %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] Failed to transmit the video packet with FECv2. result=%08lX"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] VCFECGenerator flush failed result=%08lX"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] VCFECGenerator output packest is not zero, will force a flush numOutputPackets=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter_TransmitOneFrame failed (RTP_E_RESTART) result=%08lX i=%d  isParity=%d\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter_TransmitOneFrame failed! result=%08lX i=%d isParity=%d\n"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: isUplinkRetransmissionEnabled oldValue=%d newValue=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Allocation of %d bytes failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Failed to allocate entry"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Failed to allocate new entry"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid adjustedMTU=%d MTU=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid size iGobs = %d, iHeads = %d, buffer size = %u, dataLen = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid size lineLen = %d, head = %d, buffer size = %d, dataLen = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid slice length (%d), discarded."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Max number of GOBs reached (%d), discarded."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: calloc %d bytes failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: malloc %d bytes failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: Can't extract avcC from format description"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigBlockBufferGetDataPointer %i"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigSampleBufferGetFormatDescription returned NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: Unknown pixel format '%s'"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: gksVCPParseConfigurationRecordAndCreateParameterSets failed with err = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: No ']' after '[' for an IPv6 address[%s]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: No colon after sip scheme[%s]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: Unknown URI parameter[%s]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Error parsing TURN message (%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for Allocate request."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for ChannelBinding request."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for Refresh request."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Only Carrier interface available."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: ProcessAllocateResponse failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Request timed out after %5.2f sec."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Socket error, tear down the connection."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: TCP/SSL socket is closed while accepting packets"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: We can't connect: %d, %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create read source."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create socket"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create write source."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't reserver buffer pool"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: handshake error: %d, %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: malloc error for a new node"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: malloc error for buffer %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: no port to bind to."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: not found in buffer pool %p"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: socket error, tear down the connection."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: throw away TURN Message(%x)."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: Unknown types: %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendAllocateMsg: MakeAllocateRequest error: %x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendAllocateMsg: STUNEncodeMessage error: %x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendChannelBindingMsg: MakeChannelBindRequest error: %x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendChannelBindingMsg: STUNEncodeMessage error: %x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendRefreshMsg: STUNEncodeMessage error: %x"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphCreateAndConfigureForUnits failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphGetProperty(input device clock) failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphSetProperty(pixelBufferAttributes) failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CreateGraph: kCMIOGraphProperty_RetainDiscreteGPU failed with %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: FigBufferQueueCreate(preview) failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: ToCVPixelBufferConsumer_Setup failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: pthread_create failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: pthread_create failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioIO.m:%d: "
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioIssueDetectorUtil.c:%d: Unexpected log event"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: CMSession:[%u] AUIOCreateHandle failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: Failed to create the audio limiter"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: Failed to start the audio limiter"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: [CMSession]:%u AUIOStart failed(%08lX)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioPowerSpectrumMeter.m:%d: streamToken %d is registered to source %p with spectrum %p"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to allocate secondary buffer"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to create the audio limiter"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to create the relay IO"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to start the audio limiter"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to start the relay IO"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStreamReceiveGroup.m:%d: ActiveCount:%d audioPriority:%d audioActive:%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStreamReceiveGroup.m:%d: Updating audio priority %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Bad ACK, #dropped SN doesn't match(%d != %u)."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Bad ACK, #dropped SN exceeds limit(%d > %d)."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Got PTs more than VC_BBNOTE_MAX_PAYLOAD_TYPES (%d) in a DropACK"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc send: sentBytes = %d, errno = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc: VTP_Recvfrom failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc: VTP_Select failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VTPRecvProcVCCR thread create failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: bind on %s failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: getaddrinfo(%s,%s) failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: relayIDSPacket: VTP_Sendto: sentBytes = %d, errno = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: relayIDSPacket: recv failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: setupVTPSocket failed(%x)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: socket failed(%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay VTP_SetClientRelayMode(%d) failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay: _idsReadQueue creation failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay: _idsReadSource creation failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Applying layer transforms either on timeout or while we are not waiting for UI layout change, vcImageQueue=%p contentsRectDidChange=%d tranformDidChange=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Detected iPhone in Domino mode orientation %d width %f height %f"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed configure image queue error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create image queue error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create video target error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create video target options"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to add fence=%p for remote layer=%p with context=%p"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to add image queue to config error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to create master clock, error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to set rate and anchor time, error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to set timebase, error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Invalid CAContext"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Invalid CALayer"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Timed out waiting for layout change"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Transform updated for orientation=%d or ContentsRect changed to=%@ from=%@"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: configureCALayerBounds: frameRect=%@"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: effectsEnabled=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: fence=%p for layer=%p and context=%p resolved successfully"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: vcImageQueue=%p LocalVideoAttributes=%@"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: videoAttributes=%s"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCNWConnectionMonitor.c:%d: Failed to create status monitor after state ready! monitor=%p"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCPayloadUtils.m:%d: Unsupported payload type: %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRealTimeThread.c:%d: Failed to start the thread"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRealTimeThread.c:%d: Thread creation failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: %s Error no VCRemoteVideoState for this stream token"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to DidReceiveFirstRemoteFrameForStreamToken"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to RemoteScreenAttributesDidChange"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to RemoteVideoAttributesDidChange"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: token[%ld] state[%s]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSecurityKeyManager.m:%d: Adjusted mediaKeyIndex to '%@'"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSecurityKeyManager.m:%d: Notified of new keyMaterial '%@'"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m:%d: [%p] OneToOne session should reconnect (ids reinit)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: VCCallSession: StartConnectionCheck failed(%X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: createRelayUpdateDictionary: requestResponse is %s"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict bailing because relay is not allowed."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict bailing because relayState is %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict: can't find relay type info in the dictionary"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict bailing because relay is not allowed."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict: can't find relay type info in the dictionary"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict: wait until allocation is finished %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoEncoder_VT.c:%d: Encoder callback is NULL"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoReceiverDefault.m:%d: VideoReceiver[%p] startVideo failed (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStreamTransmitter.m:%d: VideoTransmitter transmitGroup failed (%08lX) for group (%d) #packet (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s failed due to VFDList not found."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) error. Empty buffer returned!"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) failed (%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) returned 0: empty message"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: connectionManager is nil"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: datagramOptions is nil"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: CreateHandle failed with errno=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: DTLS_Write failed %08X."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed VTP check-in"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed VTP check-in."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed due to invalid handle"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed due to invalid parameter."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed to create VTP memory allocators"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed to create metadata for service class"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid FaceTime traffic class value=%d, ignore."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT MAC, discard."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT RTP header version with bad CRC, discard."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT RTP header version, discard."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT header, discard."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid relay server type(%d)."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD found for connection result with localIPPort %s"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD found for default result key."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD result found."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No key available to generate MAC, reset flag."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: OFT packet (%d) missing OFT MAC, discard."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: PrepareOFTCRC32 failed due to invalid parameter."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: RealSocketForConnectionResult returned invalid socket"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Select timeout, VTP has received a total of %d packets"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: SessionID is NULL, cannot generate MAC, reset flag."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: SessionID length 0, cannot generate MAC, reset flag."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VCDatagramChannelReadHandler failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed, result=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed. Datagram size=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed. Datagram size=%lu"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPCallback failed due to undefined pointer."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc thread failed, osStatus=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc thread=%p started. g_hVTP:[%p]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Cleanup failed due to invalid handle. g_hVTP:[%p]"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_GetSendRecvStats failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_GetVFD returned invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_NotifyAFRCRxEstimate"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_RecvPkt recv bad message=0x%04X"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Select failed due to invalid parameter."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid packet type (%d)."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid parameter."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetAFRCRecvMode failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetPayloadList failed to alloc."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetRTPSrc failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Socket failed due to invalid handle."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: bind failed(%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: calloc failed to allocate=%d bytes"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: calloc(%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: fd=%d > FD_SETSIZE"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: if_indextoname failed for index %d (%d)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: index=%d, statsID = %d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: ioctl(SIOCSIFLOG) for interface=%s failed with error=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: out-of-bound OFT type."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: realSocket=%d > FD_SETSIZE=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: realloc (%d) failed"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: select failed (%08X)"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket failed with errno=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket failed. We may run out of file descriptors"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket=%d > FD_SETSIZE=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: unrecognized openfacetime type=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: vfd=%d is out-of-range."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConferenceManager.m:%d: VTPCallback error: unknown notificaiton %d."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/WRMClient.m:%d: WRMClient: invalid configuration event with kMessageID %llu."
+ " [%s] %s:%d Authentication tag doesn't match for non-RCCM2 cipher. Authentication failed"
+ " [%s] %s:%d Authentication tag doesn't match when no roll-over detected. Authentication failed"
+ " [%s] %s:%d Choosing to stop capture, streamGroupMode=%u audioIOState=%u"
+ " [%s] %s:%d Controller is NULL"
+ " [%s] %s:%d Failed to create CVDisplayLink : `CVDisplayLinkSetOutputCallback` failed with error=%d"
+ " [%s] %s:%d Failed to create CVDisplayLink: `CVDisplayLinkCreateWithActiveCGDisplays` failed  with error=%d"
+ " [%s] %s:%d Generated 'CCReliableDataNotReceived' symptom for participantID=%@ with topic=%@"
+ " [%s] %s:%d Skipping configuration because device role and operating mode have NOT changed"
+ " [%s] %s:%d _captureFormatPrefer16By9ForSquare=%d"
+ " [%s] %s:%d isAnyCameraMediaTypeEnabled=%{BOOL}d operatingMode=%s [%u] oneToOneModeEnabled=%{BOOL}d"
+ " [%s] %s:%d isMixingVoiceWithMediaEnabled=%d"
+ " [%s] %s:%d isMixingVoiceWithMediaEnabled=%d failed. result=%08X"
+ " [%s] %s:%d pick 1088x1088 cameraFormat=%@"
+ " [%s] %s:%d set companionSettingsVideoDataOutput"
+ "+[LogDumpUtility createLogDumpListSortedByTimestamp:]"
+ "+[LogDumpUtility removeLogDumpsInDirectory:olderThan:]"
+ "-[AVConferencePreview applyTransform:forLayer:]"
+ "-[VCAVFoundationCapture updateVideoDataOutputVideoSettingResolution:requestHeight:captureFormat:]"
+ "-[VCAudioManager applyVoiceMixingMedia]"
+ "-[VCAudioRelayIOController waitIdleForClient:]"
+ "-[VCAudioStreamSendGroup stopCaptureForEndToEndStreamIfNeeded]"
+ "-[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:]"
+ "-[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenSpuriousLagDetected]"
+ "-[VCSessionParticipantRemote reportConnectionTimingDispatchedWithStreamGroup:]"
+ "-[VCVideoCaptureServer setThermalLightMitigationsEnabled:]_block_invoke"
+ ".db"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCAudioStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCQoSMonitor.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSessionParticipant.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCVideoStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVConference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioTransmitter.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSessionCategories.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCaptionsStreamSendGroup.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamGroup.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamTransport.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+Messaging.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipant.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipantLocal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTextStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoCaptureServer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/Common/VCMediaDevice.m"
+ "2105.10.1"
+ "@24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p AudioOutputUnitStart() completed"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p AudioUnitGetProperty(MicOut) failed(%d)"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p ERROR AudioOutputUnitStart returned %d"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p Failed to start the packet thread result=%x"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentCopyName() gave a NULL name!"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentCopyName() returned error %d"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentInstanceNew failed(%X)"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioOutputUnitStart completed"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioOutputUnitStart returned %d"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitGetProperty(SpkrIn) failed(%d)"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitSetProperty failed(%X)"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitSetProperty(SpkrIn) failed(%d)"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: CFStringGetCString() failed!"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: Failed to restart the packet thread result=%x"
+ "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: System Audio Tap initalization failed(%X)"
+ "AVConferenceOperatingModeAirPlayMirroring"
+ "AVConferenceOperatingModeAppleCalling"
+ "AVConferenceOperatingModeFaceTime"
+ "AVConferenceOperatingModeHomeKit"
+ "AVConferenceOperatingModeMultiway"
+ "AVConferenceOperatingModeRemoteCamera"
+ "AVConferenceOperatingModeRemoteMic"
+ "AVConferenceOperatingModeScreenSharing"
+ "AVConferenceOperatingModeSecondDisplay"
+ "AVConferenceOperatingModeSystemAudioSharing"
+ "AVConferenceOperatingModeTinCan"
+ "AVConferenceOperatingModeWifiCalling"
+ "AVConferencePreview [%s] %s:%d Invalid layer: layer=%p"
+ "B24@0:8I16B20"
+ "B32@0:8i16i20@24"
+ "EnableThermalLightMitigations"
+ "NoTopic"
+ "ProtocolStringEnableThermalLightMitigations"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: CreateHandle failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: Invalid Request message(%p)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: Invalid Response message(%p,%d,%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: MQCreateHandle failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: CreateHandle failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: Message Queue Closed during MQGet"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: ppSipMsg is NULL"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Bad Transport Protocol(%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Call SIPStartListen first."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Call(%d) is in state %d"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CallID(%d) is invalid"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find a dialog to cancel, sending 481"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find a dialog to hangup, sending 481"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find call ID(%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateAck failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateBye failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateCancel failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateGenericStatus failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateHandle failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateInvite failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateMessageInDialog failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateSKEMessageInDialog failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateStatus failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLCountActiveDialogs(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLCreateHandle failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLGetMsg failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLGetMsg returned NULL message"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLPutMsg failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUnlock: failed to unlock also."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUnlock: failed to unlock."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUpdate failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Found no-match: Discard message(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Invalid SIP Handle"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SIPSetCellConditionChangeHandler: Invalid SIP Handle"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SIPSetMessageDelegateForCallID: Invalid SIP Handle"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKENodeCreateAsInitiator failed(%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKENodeCreateAsResponder (%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: DLGetMsg returned null"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: oom: %d"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: seq %d > %d"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SecKeyExchangeUpdate failed (%d, %d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SendTAStatus cancelled"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SendTAStatus failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TACreateHandle failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TASetRetransmitTimeoutCap failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TAStart failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TPCreateHandle failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TPSend failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: fpAppCallback is NULL"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: pthread_create failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: CreateReasonHdr: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Invalid protocol version[%s] in Via"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: More Via than the maximum %d"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Multiple Event packages in Event header[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No '%c' in the header[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No '>' in SIP URI[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No ']' after '[' for an IPv6 address[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No header field name[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: ParseReasonHdr calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Unsupported header[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: malloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: # of Via exceeded the maximum %d < %d+%d"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CopySipHeader failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAcceptHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAllowEventsHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAllowHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateCSeqHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateCallIDHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContactHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContentLengthHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContentTypeHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateExpiresHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateFromHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateMaxForwardsHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateMinExpires failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateReasonHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateSKESeqHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateToHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateUserAgentHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateViaHdr failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: DLGetData failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: Invalid SIP Message(%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: malloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Extension Method is not supported[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid SIP version in Request-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid SIP version in Status-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid status code(%d[%s])"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No Method found in Request-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No RequestURI found in Request-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No SIP Version found in Status-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No Topline found in the message[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No status code found in Status-Line[%s]"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: ParseSipUri failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: CreateCancel failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: Invalid Transaction Handle"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: MQPut failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: pthread_create failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-LENGTH incorrect (%d/%d)."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-LENGTH less than 0 (%d)."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-TYPE null when body not empty."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CSeq header missing"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CallSIPMessageCallback failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress Binary SDP failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress INVITE/200 SDP failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress other SIP SDP failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ConstructSipMsg failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CreateSocketAndBind failed in TPAddIPPortToCLIST = (%08x)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Decompress failed: %d, %d, (%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICEAddOneInterface failed in TPAddIPPortToCLIST = (%08x)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICECreateHandle failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICESetEnableLoopbackInterface failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: INVITE doesn't have Contact header."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: No network interface found."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ParseMessage failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Remote candidate data is invalid (data:%p len:%d)."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Retry SIP packet using default result key failed (%08lX)."
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: SipMsg doesn't have a Via header"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPConnectedCallback: CheckInHandle failed in the dispatched block"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPNewCandidatesCallback: CheckInHandle failed in the dispatched block"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPRemoveIPPort: CheckInHandle failed in the dispatched block"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Via header missing or no field value"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: bind on %d failed(%d)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: calloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getaddrinfo failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getaddrinfo returned NULL"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getsockname failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: malloc(%d) failed"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: pthread_create(TPRecvProc) failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: recvfrom(%d) failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: recvfrom(%d) returned 0: empty message"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: select failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: socket failed(%08X)"
+ "SymptomReporterOptionalKeyCCMEssageTopic"
+ "T@\"VCAudioRelay\",R,N,V_relay"
+ "T^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB},R"
+ "Ti,R,N,V_operatingMode"
+ "VCAudioIOControllerIOState_RegisterClientIO"
+ "VCAudioIOControllerIOState_UnregisterClientIO"
+ "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: Benign Error (possibly not): We started audio before we negotiated our codec."
+ "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: resetting SourceState for syncSourceDelegate=%p"
+ "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: updating syncSourceDelegates=(%@) with ntpTime=%.6f and rtpTimestamp=%u"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: AFRCCreateHandle failed (%08X)"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: Benign Error (possibly not): We started audio before we negotiated our codec."
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: MediaCallback: notificaiton %d unknown, no action."
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: MediaQueue_CreateHandle failed (%08X)"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: RTPGetLocalSSRC for audio failed (%08X) handle = %p"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: RTPGetLocalSSRC for video failed (%08X)"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayRequestResponseDict bailing because (![self isCallOngoing] == %d)"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayUpdateDict bailing because (![self isCallOngoing] == %d)"
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayUpdateDict: remoteCallInfo is nil."
+ "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: setSessionConferenceState: invalid state"
+ "VCMSConnectionType"
+ "VCMediaStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m:%d: MediaCallback: notificaiton %d unknown, no action."
+ "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: AFRCCreateHandle failed"
+ "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Bad ACK, #dropped SN doesn't match(%d != %u)."
+ "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Bad ACK, #dropped SN exceeds limit(%d > %d)."
+ "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Got PTs more than MAX_PAYLOADTYPES(%d) in a DropACK"
+ "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: calloc(%d) failed"
+ "VCRC [%s] %s:%d Lag=%f with receiveDiff=%f and sendDiff=%f looks spurious (shortLag=%f, longLag=%f, threshold=%f), discarding"
+ "VCRC [%s] %s:%d No consecutive out of order with %sTimestamp=%u, previous%sTimestamp=%u, increment oooContinuousRecoveredCount=%d"
+ "VCRC [%s] %s:%d Reset oooContinuousRecoveredCount, since consecutively out of order with %sTimestamp=%u, previous%sTimestamp=%u"
+ "VCRC [%s] %s:%d Spurious lag detected with _sendTimestampSpikeDetected=%d, _sendTimestampSpikeDetected=%d"
+ "VCRC [%s] %s:%d Spurious lag detected without _sendTimestampSpikeDetected=%d, _sendTimestampSpikeDetected=%d, increment _spuriousLagWithoutSpikeCount=%d"
+ "VCSession [%s] %s:%d %@(%p) Forced ECN setting via networking layer default"
+ "VCSession [%s] %s:%d %@(%p) Forced turned off ECN via network config settings"
+ "VCSession [%s] %s:%d %@(%p) Forced turned on ECN via network config settings"
+ "VCSession [%s] %s:%d %@(%p) _isECNEnabled=%d, _isECNCapable=%d, buildSettingECNParam=%d, _ecnLinkType=%d"
+ "VCSession [%s] %s:%d Forced turned off ECN via network config settings"
+ "VCSession [%s] %s:%d Forced turned on ECN via network config settings"
+ "VCSessionParticipantRemote [%s] %s:%d Remote participantID=%llu V2 connection timing=%f, connection timing started=%f clocked by '%s' streamGroup"
+ "VCVideoCaptureServer [%s] %s:%d capture-started, width=%d height=%d rate=%dfps cappedFrameRate=%dfps"
+ "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: no image queue/layer to draw to... This should be reported!"
+ "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: null object was passed to DidReceiveRemoteFrame"
+ "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: null object was passed to DidReceiveSampleBuffer"
+ "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] RSU_Decode failed (%d)"
+ "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] malloc failed"
+ "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] packet size (%d) is too big"
+ "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] payload size (%d) is too big"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] Can't extract avcC from format description"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] VideoPlayer_DecodeFrame failed (%08X)"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] VideoReceiver_RecvProc thread create failed(%d)"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] deep copy of rtcp send control params failed (%08X)"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] readAVCCAndEncodeH264SPSPPS %d"
+ "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] send rtcp failed (%08X)"
+ "VideoReceiver [%s] %s:%d Optional dictionary for reporting NoVideoDisplayedFailSafeFIR ABC symptom is NULL"
+ "^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16@0:8"
+ "_VCSystemAudioCaptureSession_ResetAudioBufferPool"
+ "_VideoReceiver_SendReportingSymptomForNoVideoDisplayedFailSafeFIR"
+ "_isHomeKitStreamRemote"
+ "_mediaConnectionTimeStartToStartComplete"
+ "_previousOOOReceiveTimestamp"
+ "_previousOOOSendTimestamp"
+ "_receiveTimestampOOORecoveredCount"
+ "_sendTimestampOOORecoveredCount"
+ "_shouldResetAudioBufferPool"
+ "_spuriousLagWithoutSpikeCount"
+ "_thermalLightMitigationsEnabled"
+ "applyTransform:forLayer:"
+ "applyVoiceMixingMedia"
+ "cStringFromOperatingMode:"
+ "createLogDumpListSortedByTimestamp:"
+ "isMediaTypeExpected:"
+ "isVideoSettingsAspectRatioOverrideSupported"
+ "receive"
+ "removeLogDumpsInDirectory:olderThan:"
+ "reportConnectionTimingDispatchedWithStreamGroup:"
+ "reportOperatingMode:"
+ "setCompanionSettingsVideoDataOutput:"
+ "setThermalLightMitigationsEnabled:"
+ "setVideoSettingsAspectRatioOverrideEnabled:"
+ "shouldCreateReceiveSideTransmitter"
+ "shouldReportConnectionTimingWithStreamGroup:"
+ "shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:"
+ "shouldResumeOWRDEstimationWhenSpuriousLagDetected"
+ "updateCameraUsedForConnectionTiming"
+ "updateVideoDataOutputVideoSettingResolution:requestHeight:captureFormat:"
+ "v152@0:8{CATransform3D=dddddddddddddddd}16@144"
+ "v24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
+ "vc-ab-test-thermal-light-mitigations-enabled"
+ "{tagSRTPINFO=\"fSRTPInitialized\"i\"fCancelled\"i\"xWait\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"cWait\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}\"dwSSRC\"I\"dwRTPROC\"I\"wFirstRTPSeq\"S\"wHighestRTPSeq\"S\"lastAuthenticatedSequenceNumber\"S\"dwFirstRTCPSeq\"I\"dwHighestRTCPSeq\"I\"SRTPIndex\"Q\"mediaKeyLength\"i\"sessionKeyLength\"i\"MediaKey\"[32C]\"MasterSalt\"[14C]\"SessionKey\"[32C]\"SessionSalt\"[14C]\"SessionAuthenticationKey\"[32C]\"MKIAccess\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"mediaKeyIndex\"^v\"mediaKeyIndexInPacket\"^v\"SRTCPIndex\"I\"dwDerivationRate\"I\"cryptContextLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"cryptContext\"{tagSRTPCryptContext=\"ccCryptorRef\"^{_CCCryptor}}\"policy\"{tagSRTPTransformPolicy=\"cipherMode\"i\"mediaKeyLength\"i\"sessionKeyLength\"i\"sessionSaltLength\"i\"authenticationMode\"i\"sessionAuthenticationKeyLength\"i\"sessionAuthenticationTagLength\"i\"cipherSuite\"i\"maxTagBufferSize\"I}\"operatingMode\"I\"enableEncryptionDebug\"B}"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCMediaStreamConfig.m:%d: Unexpected pixel format type: %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: %s: failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverProc failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: AVCPacketRelayDriverProc start failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: CreateHandle failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCPacketRelayDriverThread.m:%d: AVCPacketRelayDriverThread: calloc(%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: %@ supports (%dx%d) @[%f-%f] '%s'"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIO Get Camera List failed %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyData for kCMIOStreamPropertyFrameRateRanges failed error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyData kCMIODevicePropertySuspendedByUser failed with %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: CMIOObjectGetPropertyDataSize for kCMIOStreamPropertyFrameRateRanges failed error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: frameRateRanges malloc failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCamera.m:%d: isFrameRateRangeSupportedForStreamID failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: Invalid network outage detection event passed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: Processing event=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: VCCM: brokenBackhaulDetectionStarted=%d "
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCConnectionManager.m:%d: connectionManager must not be NULL"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isLocal=%d isLocalNetworkBroken=%d isRemoteNetworkBroken=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isLocalActiveOnCellular=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/ConnectionManager/VCNetworkConditionMonitor.c:%d: NetworkConditionMonitor: isRemoteNetworkQualityBad=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/FECUtil.c:%d: Bad FEC header (%d)!"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/FECUtil.c:%d: WRONG, cannot have %d packets per group"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: connect refused (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: connect timed out %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: read failed with error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: select failed for connect (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: server terminated"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: write failed with error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: connectTCPSocket: connect failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: createTCPSocket: bind() failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: createTCPSocket: socket() failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: CreateHandle failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: MQ_Rexmit: missing packet wSN(%04X) iSN(%08X)\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: Media queue closing, free packet!"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: MediaQueue_LastSN failed (%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: Request buffer size(%d) too big!"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: calloc(%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/MediaQueue.c:%d: pthread_create(MediaQueueSendProc) failed (%08X)\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP APP packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP PSFB ALFB packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Bad RTCP packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Drop RTCP packet from a unknown connection."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add RTCP header"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add the Statistics Summary Report Block. status=%X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to add the VoIP Metrics Report Block. status=%X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Failed to finalize the XR packet. status=%X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP BYE message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP FIR message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP NACK message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP PSFB message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP Packet(packetType=%d, version=%d, count=%d, padding=%d) useReducedSizePackets=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP RR packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP RTPFB message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP SDES message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP SR packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP header"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP packet length"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP version"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Not enough space for the RTCP XR packet"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: RTCP packet failed Version, padding bit, packet type check"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Received RTCP SR packet PayloadType=%d NTP Seconds=%u RTPTimestamp=%u"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Sending RTCP SR packet PayloadType=%d NTP Seconds=%u RTPTimestamp=%u"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Unsupported PSFB ALFB app type=%u"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH263.c:%d: Invalid length (%d) for H263PHMODEA"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH263.c:%d: Invalid length (%d) for H263PHMODEB"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: Invalid fragmentation unit length (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: Invalid packet size, does not include DON: unit length (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPH264.c:%d: data size too big (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPLRP.c:%d: Invalid aggregation unit length (%d) for H264NALU_STAP_A packet, discarded."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPLRP.c:%d: Invalid fragmentation unit length (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Bad RTP extension length (%ld)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Bad version(%u) of RTP header extension!"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: CreateHandle failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Drop RTP packet from a unknown source"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate send buffer"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the RTP block buffer allocator"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the block buffer allocator"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the channel data format allocator"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the packet metadata allocator"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to allocate the rtpPacket allocator"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Failed to create the rtcpPacket allocator (error:%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: First RTP packet had sequence number 0. Dropping"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: RTP Handle invalid"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: RTP extension length(%u) invalid."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Unknown Payload Type(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: VTP_SocketWithIDSDescriptor for RTCP failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: VTP_SocketWithIDSDescriptor for RTP failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: Wrong connection index: %d."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: bind on %s failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: calloc failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: getaddrinfo(%s,%s) failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: malloc(%zu) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: set sockopt IP_BOUND_IF failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: socket failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTPUncompressedVideo.c:%d: data size too big (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPrivatePropertyAMRPayloadFormat %d with error %08x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPropertyBitRateControlMode with error %08x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioCodecPropertyConcealmentMode %d with error %08x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: AudioConverterSetProperty failed to set property kAudioConverterPrimeMethod with error %08x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set DTX encoder primer sample buffer[%p] bytes[%d] err[%d]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set bitrate[%d]: %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/SoundDec.c:%d: Failed to set max packet size[%d] for bitrate[%d] with err[%d]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/Util.c:%d: CreateHandle failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/Util.c:%d: calloc failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: %s: Can't extract avcC from format description"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: %s: Can't extract format description from saved buffer"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: Created encoder session=%p with tilesPerframe=%d, pixelFormat=%s, width=%d, height=%d codec=%s videoTransmitterHandle=0x%x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: Encoder callback is NULL"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: HandoverReport: fUsingCellular=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: VCPCompressionSessionCreate %i"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: VCPCompressionSessionEncodeFrame failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: readAVCCAndEncodeH264SPSPPS %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: Can't allocate imageDescDataBE"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: Can't recreate avcC from SPS/PPS %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreate: error: %X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreate: error: %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: FigVideoFormatDescriptionCreateFromBigEndianImageDescriptionData: error: %d "
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: ReadCodecConfigParams: error: %X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoDecoder.c:%d: VCPDecompressionSessionDecodeFrame: error: %d for stream %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] Failed to transmit the video packet with FECv2. result=%08lX"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] VCFECGenerator flush failed result=%08lX"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter[%p] VCFECGenerator output packest is not zero, will force a flush numOutputPackets=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter_TransmitOneFrame failed (RTP_E_RESTART) result=%08lX i=%d  isParity=%d\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: VideoTransmitter_TransmitOneFrame failed! result=%08lX i=%d isParity=%d\n"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitter.c:%d: isUplinkRetransmissionEnabled oldValue=%d newValue=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Allocation of %d bytes failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Failed to allocate entry"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Failed to allocate new entry"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid adjustedMTU=%d MTU=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid size iGobs = %d, iHeads = %d, buffer size = %u, dataLen = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid size lineLen = %d, head = %d, buffer size = %d, dataLen = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Invalid slice length (%d), discarded."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: Max number of GOBs reached (%d), discarded."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: calloc %d bytes failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoTransmitterUtils.c:%d: malloc %d bytes failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: Can't extract avcC from format description"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigBlockBufferGetDataPointer %i"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigSampleBufferGetFormatDescription returned NULL"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: FigVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: Unknown pixel format '%s'"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoUtil.m:%d: gksVCPParseConfigurationRecordAndCreateParameterSets failed with err = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: No ']' after '[' for an IPv6 address[%s]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: No colon after sip scheme[%s]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipUri.c:%d: Unknown URI parameter[%s]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Error parsing TURN message (%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for Allocate request."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for ChannelBinding request."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Got error response for Refresh request."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Only Carrier interface available."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: ProcessAllocateResponse failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Request timed out after %5.2f sec."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: Socket error, tear down the connection."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: TCP/SSL socket is closed while accepting packets"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: We can't connect: %d, %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create read source."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create socket"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't create write source."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: can't reserver buffer pool"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: handshake error: %d, %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: malloc error for a new node"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: malloc error for buffer %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: no port to bind to."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: not found in buffer pool %p"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: socket error, tear down the connection."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: TCPTUNNEL: throw away TURN Message(%x)."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: Unknown types: %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendAllocateMsg: MakeAllocateRequest error: %x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendAllocateMsg: STUNEncodeMessage error: %x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendChannelBindingMsg: MakeChannelBindRequest error: %x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendChannelBindingMsg: STUNEncodeMessage error: %x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m:%d: sendRefreshMsg: STUNEncodeMessage error: %x"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphCreateAndConfigureForUnits failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphGetProperty(input device clock) failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CMIOGraphSetProperty(pixelBufferAttributes) failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: CreateGraph: kCMIOGraphProperty_RetainDiscreteGPU failed with %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: FigBufferQueueCreate(preview) failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: ToCVPixelBufferConsumer_Setup failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: pthread_create failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TundraVideoCapture.m:%d: pthread_create failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioIO.m:%d: "
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioIssueDetectorUtil.c:%d: Unexpected log event"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: CMSession:[%u] AUIOCreateHandle failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: Failed to create the audio limiter"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: Failed to start the audio limiter"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioManager.m:%d: [CMSession]:%u AUIOStart failed(%08lX)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioPowerSpectrumMeter.m:%d: streamToken %d is registered to source %p with spectrum %p"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to allocate secondary buffer"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to create the audio limiter"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to create the relay IO"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to start the audio limiter"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioRelayIOController.m:%d: Failed to start the relay IO"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStreamReceiveGroup.m:%d: ActiveCount:%d audioPriority:%d audioActive:%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStreamReceiveGroup.m:%d: Updating audio priority %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Bad ACK, #dropped SN doesn't match(%d != %u)."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Bad ACK, #dropped SN exceeds limit(%d > %d)."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCBasebandNotificationParser.c:%d: Got PTs more than VC_BBNOTE_MAX_PAYLOAD_TYPES (%d) in a DropACK"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc send: sentBytes = %d, errno = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc: VTP_Recvfrom failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VCClientRelayVTPReceiveProc: VTP_Select failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: VTPRecvProcVCCR thread create failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: bind on %s failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: getaddrinfo(%s,%s) failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: relayIDSPacket: VTP_Sendto: sentBytes = %d, errno = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: relayIDSPacket: recv failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: setupVTPSocket failed(%x)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: socket failed(%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay VTP_SetClientRelayMode(%d) failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay: _idsReadQueue creation failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCClientRelay.m:%d: startRelay: _idsReadSource creation failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Applying layer transforms either on timeout or while we are not waiting for UI layout change, vcImageQueue=%p contentsRectDidChange=%d tranformDidChange=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Detected iPhone in Domino mode orientation %d width %f height %f"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed configure image queue error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create image queue error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create video target error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed create video target options"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to add fence=%p for remote layer=%p with context=%p"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to add image queue to config error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to create master clock, error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to set rate and anchor time, error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Failed to set timebase, error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Invalid CAContext"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Invalid CALayer"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Timed out waiting for layout change"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: Transform updated for orientation=%d or ContentsRect changed to=%@ from=%@"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: configureCALayerBounds: frameRect=%@"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: effectsEnabled=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: fence=%p for layer=%p and context=%p resolved successfully"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: vcImageQueue=%p LocalVideoAttributes=%@"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCImageQueue.m:%d: videoAttributes=%s"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCNWConnectionMonitor.c:%d: Failed to create status monitor after state ready! monitor=%p"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCPayloadUtils.m:%d: Unsupported payload type: %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRealTimeThread.c:%d: Failed to start the thread"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRealTimeThread.c:%d: Thread creation failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: %s Error no VCRemoteVideoState for this stream token"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to DidReceiveFirstRemoteFrameForStreamToken"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to RemoteScreenAttributesDidChange"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: VCRemoteVideoManager: null object was passed to RemoteVideoAttributesDidChange"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCRemoteVideoManager.m:%d: token[%ld] state[%s]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSecurityKeyManager.m:%d: Adjusted mediaKeyIndex to '%@'"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSecurityKeyManager.m:%d: Notified of new keyMaterial '%@'"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m:%d: [%p] OneToOne session should reconnect (ids reinit)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: VCCallSession: StartConnectionCheck failed(%X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: createRelayUpdateDictionary: requestResponse is %s"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict bailing because relay is not allowed."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict bailing because relayState is %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayRequestResponseDict: can't find relay type info in the dictionary"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict bailing because relay is not allowed."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict: can't find relay type info in the dictionary"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m:%d: processRelayUpdateDict: wait until allocation is finished %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoEncoder_VT.c:%d: Encoder callback is NULL"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoReceiverDefault.m:%d: VideoReceiver[%p] startVideo failed (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStreamTransmitter.m:%d: VideoTransmitter transmitGroup failed (%08lX) for group (%d) #packet (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s failed due to VFDList not found."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) error. Empty buffer returned!"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) failed (%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s(%d) returned 0: empty message"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: connectionManager is nil"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: datagramOptions is nil"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: %s: failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: CreateHandle failed with errno=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: DTLS_Write failed %08X."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed VTP check-in"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed VTP check-in."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed due to invalid handle"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed due to invalid parameter."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed to create VTP memory allocators"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Failed to create metadata for service class"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid FaceTime traffic class value=%d, ignore."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT MAC, discard."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT RTP header version with bad CRC, discard."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT RTP header version, discard."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid OFT header, discard."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Invalid relay server type(%d)."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD found for connection result with localIPPort %s"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD found for default result key."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No VFD result found."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: No key available to generate MAC, reset flag."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: OFT packet (%d) missing OFT MAC, discard."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: PrepareOFTCRC32 failed due to invalid parameter."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: RealSocketForConnectionResult returned invalid socket"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: Select timeout, VTP has received a total of %d packets"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: SessionID is NULL, cannot generate MAC, reset flag."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: SessionID length 0, cannot generate MAC, reset flag."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VCDatagramChannelReadHandler failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed, result=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed. Datagram size=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP packet allocation failed. Datagram size=%lu"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPCallback failed due to undefined pointer."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc thread failed, osStatus=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTPRecvProc thread=%p started. g_hVTP:[%p]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Cleanup failed due to invalid handle. g_hVTP:[%p]"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_GetSendRecvStats failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_GetVFD returned invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_NotifyAFRCRxEstimate"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_RecvPkt recv bad message=0x%04X"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Select failed due to invalid parameter."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid packet type (%d)."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Sendto failed due to invalid parameter."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetAFRCRecvMode failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetPayloadList failed to alloc."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_SetRTPSrc failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: VTP_Socket failed due to invalid handle."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: bind failed(%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: calloc failed to allocate=%d bytes"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: calloc(%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: fd=%d > FD_SETSIZE"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: if_indextoname failed for index %d (%d)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: index=%d, statsID = %d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: ioctl(SIOCSIFLOG) for interface=%s failed with error=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: out-of-bound OFT type."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: realSocket=%d > FD_SETSIZE=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: realloc (%d) failed"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: select failed (%08X)"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket failed with errno=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket failed. We may run out of file descriptors"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: socket=%d > FD_SETSIZE=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: unrecognized openfacetime type=%d"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VTP/VTransport.m:%d: vfd=%d is out-of-range."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConferenceManager.m:%d: VTPCallback error: unknown notificaiton %d."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/WRMClient.m:%d: WRMClient: invalid configuration event with kMessageID %llu."
- " [%s] %s:%d Got unsupported SIMD fetch type %d for packetOffset=%d"
- " [%s] %s:%d Registering clientIO[%p]"
- " [%s] %s:%d Setting Voice Mixing Enabled=%d"
- " [%s] %s:%d Unexpected event in silence state for direction=%d"
- " [%s] %s:%d Unexpected event in speech state in direction=%d"
- " [%s] %s:%d Unregistering clientIO[%p]"
- "+[LogDumpUtility createFileListSortedByTimestamp:]"
- "+[LogDumpUtility removeFilesInDirectory:olderThan:]"
- "-[VCAudioManager stateSessionStartedWithAudioUnitProperties:sessionProperties:client:newState:]"
- "-[VCSessionParticipantRemote reportConnectionTimingDispatched]"
- "-[VCSystemAudioCaptureSession resetAudioBufferPool]"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCAudioStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCQoSMonitor.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSession.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSessionParticipant.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCVideoStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVConference.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptions.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioTransmitter.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSessionCategories.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCaptionsStreamSendGroup.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamGroup.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamManager.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamTransport.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+Messaging.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionManager.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipant.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipantLocal.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTextStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoCaptureServer.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConference.m"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/Common/VCMediaDevice.m"
- "2100.5.1"
- "@24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
- "AS"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p AudioOutputUnitStart() completed"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p AudioUnitGetProperty(MicOut) failed(%d)"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p ERROR AudioOutputUnitStart returned %d"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p Failed to start the packet thread result=%x"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentCopyName() gave a NULL name!"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentCopyName() returned error %d"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioComponentInstanceNew failed(%X)"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioOutputUnitStart completed"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioOutputUnitStart returned %d"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitGetProperty(SpkrIn) failed(%d)"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitSetProperty failed(%X)"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AudioUnitSetProperty(SpkrIn) failed(%d)"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: CFStringGetCString() failed!"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: Failed to restart the packet thread result=%x"
- "AUIO [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: System Audio Tap initalization failed(%X)"
- "LF"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: CreateHandle failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: Invalid Request message(%p)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: Invalid Response message(%p,%d,%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: MQCreateHandle failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Dialog.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: CreateHandle failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: Message Queue Closed during MQGet"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/MsgQue.c:%d: ppSipMsg is NULL"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Bad Transport Protocol(%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Call SIPStartListen first."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Call(%d) is in state %d"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CallID(%d) is invalid"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find a dialog to cancel, sending 481"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find a dialog to hangup, sending 481"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Cannot find call ID(%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateAck failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateBye failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateCancel failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateGenericStatus failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateHandle failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateInvite failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateMessageInDialog failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateSKEMessageInDialog failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: CreateStatus failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLCountActiveDialogs(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLCreateHandle failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLGetMsg failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLGetMsg returned NULL message"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLPutMsg failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUnlock: failed to unlock also."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUnlock: failed to unlock."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: DLUpdate failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Found no-match: Discard message(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: Invalid SIP Handle"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SIPSetCellConditionChangeHandler: Invalid SIP Handle"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SIPSetMessageDelegateForCallID: Invalid SIP Handle"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKENodeCreateAsInitiator failed(%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKENodeCreateAsResponder (%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: DLGetMsg returned null"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: oom: %d"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SKEProc: seq %d > %d"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SecKeyExchangeUpdate failed (%d, %d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SendTAStatus cancelled"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: SendTAStatus failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TACreateHandle failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TASetRetransmitTimeoutCap failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TAStart failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TPCreateHandle failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: TPSend failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: fpAppCallback is NULL"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c:%d: pthread_create failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: CreateReasonHdr: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Invalid protocol version[%s] in Via"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: More Via than the maximum %d"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Multiple Event packages in Event header[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No '%c' in the header[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No '>' in SIP URI[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No ']' after '[' for an IPv6 address[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: No header field name[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: ParseReasonHdr calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: Unsupported header[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipHdr.c:%d: malloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: # of Via exceeded the maximum %d < %d+%d"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CopySipHeader failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAcceptHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAllowEventsHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateAllowHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateCSeqHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateCallIDHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContactHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContentLengthHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateContentTypeHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateExpiresHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateFromHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateMaxForwardsHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateMinExpires failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateReasonHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateSKESeqHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateToHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateUserAgentHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: CreateViaHdr failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: DLGetData failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: Invalid SIP Message(%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipMsg.c:%d: malloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Extension Method is not supported[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid SIP version in Request-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid SIP version in Status-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: Invalid status code(%d[%s])"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No Method found in Request-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No RequestURI found in Request-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No SIP Version found in Status-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No Topline found in the message[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: No status code found in Status-Line[%s]"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: ParseSipUri failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SipParse.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: CreateCancel failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: Invalid Transaction Handle"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: MQPut failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transaction.c:%d: pthread_create failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-LENGTH incorrect (%d/%d)."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-LENGTH less than 0 (%d)."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CONTENT-TYPE null when body not empty."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CSeq header missing"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CallSIPMessageCallback failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress Binary SDP failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress INVITE/200 SDP failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Compress other SIP SDP failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ConstructSipMsg failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: CreateSocketAndBind failed in TPAddIPPortToCLIST = (%08x)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Decompress failed: %d, %d, (%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICEAddOneInterface failed in TPAddIPPortToCLIST = (%08x)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICECreateHandle failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ICESetEnableLoopbackInterface failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: INVITE doesn't have Contact header."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: No network interface found."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: ParseMessage failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Remote candidate data is invalid (data:%p len:%d)."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Retry SIP packet using default result key failed (%08lX)."
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: SipMsg doesn't have a Via header"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPConnectedCallback: CheckInHandle failed in the dispatched block"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPNewCandidatesCallback: CheckInHandle failed in the dispatched block"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: TPRemoveIPPort: CheckInHandle failed in the dispatched block"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Via header missing or no field value"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: bind on %d failed(%d)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: calloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getaddrinfo failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getaddrinfo returned NULL"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: getsockname failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: malloc(%d) failed"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: pthread_create(TPRecvProc) failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: recvfrom(%d) failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: recvfrom(%d) returned 0: empty message"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: select failed(%08X)"
- "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: socket failed(%08X)"
- "T^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB},R"
- "VCAudioReceiver_SendEndCallReport"
- "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: Benign Error (possibly not): We started audio before we negotiated our codec."
- "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: resetting SourceState for syncSourceDelegate=%p"
- "VCAudioStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m:%d: updating syncSourceDelegates=(%@) with ntpTime=%.6f and rtpTimestamp=%u"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: AFRCCreateHandle failed (%08X)"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: Benign Error (possibly not): We started audio before we negotiated our codec."
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: MediaCallback: notificaiton %d unknown, no action."
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: MediaQueue_CreateHandle failed (%08X)"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: RTPGetLocalSSRC for audio failed (%08X) handle = %p"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: RTPGetLocalSSRC for video failed (%08X)"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayRequestResponseDict bailing because (![self isCallOngoing] == %d)"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayUpdateDict bailing because (![self isCallOngoing] == %d)"
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: processRelayUpdateDict: remoteCallInfo is nil."
- "VCCallSession [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m:%d: setSessionConferenceState: invalid state"
- "VCMediaStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m:%d: MediaCallback: notificaiton %d unknown, no action."
- "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: AFRCCreateHandle failed"
- "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Bad ACK, #dropped SN doesn't match(%d != %u)."
- "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Bad ACK, #dropped SN exceeds limit(%d > %d)."
- "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: Got PTs more than MAX_PAYLOADTYPES(%d) in a DropACK"
- "VCRC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/MediaQueue/AFRC.c:%d: calloc(%d) failed"
- "VCRC [%s] %s:%d Lag=%f with receiveDiff=%f and sendDiff=%f looks spurios (shortLag=%f, longLag=%f, threshold=%f), discarding"
- "VCSessionParticipantRemote [%s] %s:%d Remote participantID=%llu V2 connection timing=%f, connection timing started=%f clocked by '%@' streamGroup"
- "VCVideoCaptureServer [%s] %s:%d capture-started, video settings width=%d height=%d rate=%dfps cappedFrameRate=%dfps"
- "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: no image queue/layer to draw to... This should be reported!"
- "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: null object was passed to DidReceiveRemoteFrame"
- "VCVideoStream [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m:%d: VCVideoStream: null object was passed to DidReceiveSampleBuffer"
- "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] RSU_Decode failed (%d)"
- "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] malloc failed"
- "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] packet size (%d) is too big"
- "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] payload size (%d) is too big"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] Can't extract avcC from format description"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] VideoPlayer_DecodeFrame failed (%08X)"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] VideoReceiver_RecvProc thread create failed(%d)"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] deep copy of rtcp send control params failed (%08X)"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] readAVCCAndEncodeH264SPSPPS %d"
- "VideoReceiver [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VideoReceiver.c:%d: VideoReceiver[%p] send rtcp failed (%08X)"
- "^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16@0:8"
- "_RSU_GatherDecodedDataOneSymbol"
- "_RSU_GatherDecodedDataTwoSymbols"
- "_RSU_ScatterRecoveryDataToSimdFourSymbols"
- "_RSU_ScatterRecoveryDataToSimdOneSymbol"
- "_RSU_ScatterRecoveryDataToSimdTwoSymbols"
- "_RSU_ScatterToCodewordLaneFourSymbols"
- "_RSU_ScatterToCodewordLaneOneSymbol"
- "_RSU_ScatterToCodewordLaneTwoSymbols"
- "_VCAudioIssueDetectorUtil_HandleSilenceStateEvents"
- "_VCAudioIssueDetectorUtil_HandleSpeechStateEvents"
- "_VCAudioManager_RegisterClientIO"
- "_VCAudioManager_UnregisterClientIO"
- "_VCAudioRelayIOController_RegisterClientIO"
- "_VCAudioRelayIOController_UnregisterClientIO"
- "came"
- "createFileListSortedByTimestamp:"
- "mic"
- "removeFilesInDirectory:olderThan:"
- "reportConnectionTimingDispatched"
- "resetAudioBufferPool"
- "v24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
- "{tagSRTPINFO=\"fSRTPInitialized\"i\"fCancelled\"i\"xWait\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"cWait\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}\"dwSSRC\"I\"dwRTPROC\"I\"wFirstRTPSeq\"S\"wHighestRTPSeq\"S\"dwFirstRTCPSeq\"I\"dwHighestRTCPSeq\"I\"SRTPIndex\"Q\"mediaKeyLength\"i\"sessionKeyLength\"i\"MediaKey\"[32C]\"MasterSalt\"[14C]\"SessionKey\"[32C]\"SessionSalt\"[14C]\"SessionAuthenticationKey\"[32C]\"MKIAccess\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"mediaKeyIndex\"^v\"mediaKeyIndexInPacket\"^v\"SRTCPIndex\"I\"dwDerivationRate\"I\"cryptContextLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"cryptContext\"{tagSRTPCryptContext=\"ccCryptorRef\"^{_CCCryptor}}\"policy\"{tagSRTPTransformPolicy=\"cipherMode\"i\"mediaKeyLength\"i\"sessionKeyLength\"i\"sessionSaltLength\"i\"authenticationMode\"i\"sessionAuthenticationKeyLength\"i\"sessionAuthenticationTagLength\"i\"cipherSuite\"i\"maxTagBufferSize\"I}\"operatingMode\"I\"enableEncryptionDebug\"B}"

```
