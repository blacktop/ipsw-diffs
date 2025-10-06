## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2000.8.1.1.1
-  __TEXT.__text: 0x633550
-  __TEXT.__auth_stubs: 0x4c40
-  __TEXT.__objc_methlist: 0x2ab1c
-  __TEXT.__const: 0x7968
-  __TEXT.__cstring: 0x74625
-  __TEXT.__oslogstring: 0xd93a4
+2005.6.1.1.2
+  __TEXT.__text: 0x639118
+  __TEXT.__auth_stubs: 0x4c30
+  __TEXT.__objc_methlist: 0x2ab94
+  __TEXT.__const: 0x7a18
+  __TEXT.__cstring: 0x74dce
+  __TEXT.__oslogstring: 0xd999b
   __TEXT.__gcc_except_tab: 0x1f84
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xc64c
+  __TEXT.__unwind_info: 0xc6bc
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x42d9
-  __TEXT.__objc_methname: 0x6916a
-  __TEXT.__objc_methtype: 0x20e62
-  __TEXT.__objc_stubs: 0x42960
+  __TEXT.__objc_methname: 0x69396
+  __TEXT.__objc_methtype: 0x20f39
+  __TEXT.__objc_stubs: 0x42a80
   __DATA_CONST.__got: 0x1110
-  __DATA_CONST.__const: 0x5970
+  __DATA_CONST.__const: 0x5a18
   __DATA_CONST.__objc_classlist: 0x1088
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4efc0
-  __DATA_CONST.__objc_selrefs: 0x131a8
+  __DATA_CONST.__objc_const: 0x4f040
+  __DATA_CONST.__objc_selrefs: 0x131f0
   __DATA_CONST.__objc_arraydata: 0x1e38
-  __AUTH_CONST.__cfstring: 0x1f620
-  __AUTH_CONST.__objc_intobj: 0x39d8
+  __AUTH_CONST.__cfstring: 0x1faa0
+  __AUTH_CONST.__objc_intobj: 0x3a20
   __AUTH_CONST.__objc_arrayobj: 0x14e8
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__const: 0x358
   __AUTH_CONST.__objc_dictobj: 0x2a8
-  __AUTH_CONST.__auth_got: 0x2638
+  __AUTH_CONST.__auth_got: 0x2630
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x1208
   __DATA.__objc_superrefs: 0xee8
-  __DATA.__objc_ivar: 0x5d58
+  __DATA.__objc_ivar: 0x5d68
   __DATA.__data: 0x6f98
   __DATA.__bss: 0xa20
   __DATA.__common: 0x55

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BBC1FF10-7831-31CA-8C11-2242EC92F2F8
-  Functions: 28027
-  Symbols:   78794
-  CStrings:  47805
+  UUID: A3577B55-B808-3AF6-A9BB-09DD969DD974
+  Functions: 28077
+  Symbols:   78915
+  CStrings:  47930
 
Symbols:
+ +[GKSConnectivitySettings readStorebagValueForStorebagKey:userDefaultKey:defaultValue:isDoubleType:]
+ -[AVCRateController isNetworkForcingECNDefaultSet]
+ -[AVCRateController isNetworkForcingECNEnabled]
+ -[VCConnection compareInterfacePriority:isPrimary:preferWired:]
+ -[VCConnectionManagerIDS shouldPreferWiredConnections]
+ -[VCConnectionSelector isPrimaryConnectionSameAsConnection:].cold.1
+ -[VCConnectionSelector isPrimaryConnectionSameAsConnection:].cold.2
+ -[VCConnectionSelector updateConnectionSelectionPolicy:]
+ -[VCConnectionSelector updateConnectionSelectionPolicy:].cold.1
+ -[VCIDSSessionInfoSynchronizer(PrivateMethods) resetPeerSubscribedStreams]
+ -[VCMediaStream applyClientSessionID:clientUserInfo:]
+ -[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:collectSubtype:]
+ -[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:collectSubtype:].cold.1
+ -[VCSession getStorebagValueForIntegerKey:defaultValue:]
+ -[VCSession readAndSetABCSymptomsReportingThresholdsFromStorebags:]
+ -[VCSession readAndSetABCSymptomsReportingThresholdsFromStorebags:].cold.1
+ -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:]
+ -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:].cold.1
+ -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:].cold.2
+ -[VCSession reportingSessionParticipantEvent:withParticipant:withStreamGroupID:withStreamID:]
+ -[VCSession setOneToOneModeEnabled:configurationDict:]
+ -[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]
+ -[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:]
+ -[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:].cold.1
+ -[VCSessionUplinkVideoStreamController setStreamIDsCell:].cold.1
+ -[VCSessionUplinkVideoStreamController setStreamIDsWifi:].cold.1
+ -[VCSystemAudioCapture initWithConfiguration:].cold.10
+ -[VCVideoStream setupColorInfo:].cold.2
+ -[VCVideoStream setupColorInfo:].cold.3
+ -[VCVideoStream setupVideoTransmitterConfigColorInfo:]
+ GCC_except_table138
+ GCC_except_table73
+ _AudioQueueNewInputWithDispatchQueue
+ _JTargetJBEstimator_GetSpikeReportingMetrics
+ _MakeSessionKey
+ _OBJC_IVAR_$_AVCRateController._isNetworkForcingECNDefaultSet
+ _OBJC_IVAR_$_VCAudioTransmitter._lastReportedRTPIngresspackets
+ _OBJC_IVAR_$_VCNetworkFeedbackController._wrmClientQueue
+ _OBJC_IVAR_$_VCSystemAudioCapture._callbackQueue
+ _OBJC_IVAR_$_VCVideoStream._colorInfo
+ _RTPGetDownlinkReportingStats
+ _RTPGetDownlinkReportingStats.cold.1
+ _RTPGetDownlinkReportingStats.cold.2
+ _RTPGetUplinkReportingStats
+ _RTPGetUplinkReportingStats.cold.1
+ _RTPGetUplinkReportingStats.cold.2
+ _SRTPGenerateAuthenticationTag
+ _SRTPGetKeyDerivationCryptoSet
+ _SRTPInitializedEncryption
+ _SRTPIsAuthenticationEnabled
+ _SRTPIsAuthenticationEnabled.cold.1
+ _SRTPUseEncryptionInternal
+ _VCConnectionManager_ConnectionInterfaceType
+ _VCConnectionPreferWiredOverWiFiEnabled
+ _VCConnection_IsLocalOnWiFiOrWired
+ _VCConnection_IsLocalOnWired
+ _VCConnection_IsRemoteOnWiFiOrWired
+ _VCConnection_IsRemoteOnWired
+ _VCReportingAudioConnectionTimeSymptomThreshold
+ _VCReportingAudioErasurePercentageSymptomThreshold
+ _VCReportingPoorConnectionPercentageSymptomThreshold
+ _VCReportingVideoConnectionTimeSymptomThreshold
+ _VCReportingVideoStallPercentageSymptomThreshold
+ _WaitUseEncryption
+ __SRTPCancelEncryption
+ __SRTPCancelEncryption.cold.1
+ __SRTPUpdateEncryption
+ __SRTPUpdateEncryption.cold.1
+ __VCConnectionIDS_IsLocalOnWiFiOrWired
+ __VCConnectionIDS_IsLocalOnWired
+ __VCConnectionIDS_IsOnSameInterfacesWithConnection.cold.3
+ __VCConnectionIDS_IsOnSameInterfacesWithConnection.cold.4
+ __VCConnectionIDS_IsRemoteOnWiFiOrWired
+ __VCConnectionIDS_IsRemoteOnWired
+ __VCConnectionLegacy_IsLocalOnWiFiOrWired
+ __VCConnectionLegacy_IsLocalOnWired
+ __VCConnectionLegacy_IsRemoteOnWiFiOrWired
+ __VCConnectionLegacy_IsRemoteOnWired
+ __VideoTransmitter_GetStreamIndexFromAttachment
+ __VideoTransmitter_GetStreamIndexFromAttachment.cold.1
+ ___28-[VCSession dispatchedStart]_block_invoke.433
+ ___28-[VCSession dispatchedStart]_block_invoke.434
+ ___29-[VCSystemAudioCapture start]_block_invoke
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.1
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.10
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.11
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.12
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.13
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.14
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.2
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.3
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.4
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.5
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.6
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.7
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.8
+ ___29-[VCSystemAudioCapture start]_block_invoke.cold.9
+ ___35-[VCNetworkFeedbackController stop]_block_invoke
+ ___37-[VCSystemAudioCapture getQueueState]_block_invoke
+ ___38-[VCSystemAudioCapture setQueueState:]_block_invoke
+ ___48-[VCNetworkFeedbackController reportWRMMetrics:]_block_invoke
+ ___48-[VCNetworkFeedbackController sendStatusUpdate:]_block_invoke
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.427
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.429
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.430
+ ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.226
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.441
+ ___51-[VCNetworkFeedbackController updateMetricsConfig:]_block_invoke
+ ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.221
+ ___53-[VCNetworkFeedbackController requestWRMNotification]_block_invoke
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.440
+ ___54-[VCNetworkFeedbackController startWithMetricsConfig:]_block_invoke
+ ___54-[VCSession setOneToOneModeEnabled:configurationDict:]_block_invoke
+ ___55-[VCNetworkFeedbackController setRSSIThresholdEnabled:]_block_invoke
+ ___60-[VCNetworkFeedbackController sendFeedbackControllerReport:]_block_invoke
+ ___62-[VCNetworkFeedbackController reportImmediateWRMMetric:value:]_block_invoke
+ ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.178
+ ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.188
+ ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.150
+ ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.160
+ ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.165
+ ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.227
+ ___82-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:]_block_invoke
+ ___82-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:]_block_invoke.70
+ ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.214
+ ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.213
+ ___85-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]_block_invoke
+ ___85-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]_block_invoke.58
+ ___85-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]_block_invoke.cold.1
+ ___85-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]_block_invoke.cold.2
+ ___block_descriptor_344_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32o_e177_v44?0^{OpaqueAudioQueue=}8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}24I32r^{AudioStreamPacketDescription=qII}36ls32l8
+ ___block_descriptor_49_e8_32o40o_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_51_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.366
+ ___block_descriptor_tmp.418
+ ___block_descriptor_tmp.420
+ ___block_literal_global.328
+ __unnamed_array_storage.225
+ _objc_msgSend$applyClientSessionID:clientUserInfo:
+ _objc_msgSend$clear
+ _objc_msgSend$collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:collectSubtype:
+ _objc_msgSend$compareInterfacePriority:isPrimary:preferWired:
+ _objc_msgSend$completionHandlerOneToOneEnabled:didSucceed:configurationDict:
+ _objc_msgSend$dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:
+ _objc_msgSend$getStorebagValueForIntegerKey:defaultValue:
+ _objc_msgSend$isNetworkForcingECNDefaultSet
+ _objc_msgSend$isNetworkForcingECNEnabled
+ _objc_msgSend$readAndSetABCSymptomsReportingThresholdsFromStorebags:
+ _objc_msgSend$readStorebagValueForStorebagKey:userDefaultKey:defaultValue:isDoubleType:
+ _objc_msgSend$reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:
+ _objc_msgSend$reportingSessionParticipantEvent:withParticipant:withStreamGroupID:withStreamID:
+ _objc_msgSend$resetPeerSubscribedStreams
+ _objc_msgSend$setOneToOneModeEnabled:configurationDict:
+ _objc_msgSend$setupVideoTransmitterConfigColorInfo:
+ _objc_msgSend$shouldPreferWiredConnections
+ _objc_msgSend$updateConnectionSelectionPolicy:
+ _setTransformPolicyFromCipherSuite
- -[VCConnection compareInterfacePriority:isPrimary:]
- -[VCMediaStream composeClientUserInfo:]
- -[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamID:collectSubtype:]
- -[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamID:collectSubtype:].cold.1
- -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:]
- -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:].cold.1
- -[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:].cold.2
- -[VCSession reportingSessionParticipantEvent:withStreamID:]
- -[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]
- -[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:]
- -[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:].cold.1
- -[VCVideoStream setVideoTransmitterConfigColorInfo:]
- GCC_except_table137
- _AudioQueueNewInput
- _OBJC_IVAR_$_VCVideoStream._hdrColorInfo
- _VCBoundsSafety_AllocatorDefault
- _VCBoundsSafety_ArrayCreateMutable
- _VCBoundsSafety_NumberCreate
- _VCBoundsSafety_PreferencesCopyAppValue
- _VCBoundsSafety_Retain
- _VCBoundsSafety_RuntimeCreateInstance
- __VCMediaQueue_SendAndFreePackets.cold.3
- __VCSystemAudioCapture_handleInputBuffer
- __VCSystemAudioCapture_handleInputBuffer.cold.1
- __VCSystemAudioCapture_handleInputBuffer.cold.10
- __VCSystemAudioCapture_handleInputBuffer.cold.11
- __VCSystemAudioCapture_handleInputBuffer.cold.12
- __VCSystemAudioCapture_handleInputBuffer.cold.13
- __VCSystemAudioCapture_handleInputBuffer.cold.2
- __VCSystemAudioCapture_handleInputBuffer.cold.3
- __VCSystemAudioCapture_handleInputBuffer.cold.4
- __VCSystemAudioCapture_handleInputBuffer.cold.5
- __VCSystemAudioCapture_handleInputBuffer.cold.6
- __VCSystemAudioCapture_handleInputBuffer.cold.7
- __VCSystemAudioCapture_handleInputBuffer.cold.8
- __VCSystemAudioCapture_handleInputBuffer.cold.9
- __VideoTransmitter_TransmitEncodedVideoFrame.cold.12
- __Z33setTransformPolicyFromCipherSuite15SRTPCipherSuiteP22tagSRTPTransformPolicyb
- __ZL14MakeSessionKeybPKhiS0_jtjhPhd
- __ZL17WaitUseEncryptionP11tagSRTPINFOPd
- __ZL21_SRTPCancelEncryptionP10tagRTPINFO
- __ZL21_SRTPCancelEncryptionP10tagRTPINFO.cold.1
- __ZL21_SRTPUpdateEncryptionP10tagRTPINFOP21SRTPKeyDerivationInfo
- __ZL21_SRTPUpdateEncryptionP10tagRTPINFOP21SRTPKeyDerivationInfo.cold.1
- __ZL25SRTPInitializedEncryptionP11tagSRTPINFOb
- __ZL25SRTPUseEncryptionInternalP11tagSRTPINFOPhiS1_iPKvbb
- __ZL27SRTPIsAuthenticationEnabledP11tagSRTPINFOPb
- __ZL27SRTPIsAuthenticationEnabledP11tagSRTPINFOPb.cold.1
- __ZL29SRTPGenerateAuthenticationTagP11tagSRTPINFObtPhiS1_i
- __ZL29SRTPGetKeyDerivationCryptoSetP21SRTPKeyDerivationInfoPK14__CFDictionary
- ___28-[VCSession dispatchedStart]_block_invoke.428
- ___28-[VCSession dispatchedStart]_block_invoke.429
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.422
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.424
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.425
- ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.223
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.436
- ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.218
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.435
- ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.175
- ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.185
- ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.147
- ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.157
- ___64-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:]_block_invoke
- ___64-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:]_block_invoke.70
- ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.162
- ___67-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]_block_invoke
- ___67-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]_block_invoke.58
- ___67-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]_block_invoke.cold.1
- ___67-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]_block_invoke.cold.2
- ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.224
- ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.211
- ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.210
- ___block_descriptor_41_e8_32o_e8_v12?0B8ls32l8
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.190
- ___block_descriptor_tmp.354
- ___block_descriptor_tmp.400
- ___block_descriptor_tmp.402
- ___block_descriptor_tmp.70
- ___block_literal_global.326
- __unnamed_array_storage.222
- _objc_msgSend$collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamID:collectSubtype:
- _objc_msgSend$compareInterfacePriority:isPrimary:
- _objc_msgSend$completionHandlerOneToOneEnabled:didSucceed:
- _objc_msgSend$composeClientUserInfo:
- _objc_msgSend$dispatchedSetOneToOneModeEnabled:isLocal:
- _objc_msgSend$reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:
- _objc_msgSend$reportingSessionParticipantEvent:withStreamID:
- _objc_msgSend$setVideoTransmitterConfigColorInfo:
- _objc_msgSend$updateConnectionSelectionPolicyWithPreferRelayOverP2P:preferNonVPN:preferE2E:
- _objc_release_x9
CStrings:
+ " [%s] %s:%d %@(%p) Failed to allocate system audio callback queue"
+ " [%s] %s:%d %@(%p) Peer subscribed streams update occured while in OneToOne mode. Ignoring subscribed streams update"
+ " [%s] %s:%d %@(%p) Session[%@] received callback for didUpdateConfig didSucceed=%{BOOL}d"
+ " [%s] %s:%d %@(%p) injector=%@, _audioSampleCount=%d, _loopLength=%f, _samplesInLoop=%d"
+ " [%s] %s:%d %@(%p) injector=%@, _samplesInLoop=%d, loopLength=%f"
+ " [%s] %s:%d ConnectionSelectionPolicy updated: preferRelayOverP2P=%d preferIPv6OverIPv4=%d preferNonVPN=%d e2eCriteriaEnabled=%d preferE2E=%d preferWired=%d"
+ " [%s] %s:%d Different non-cell interface type"
+ " [%s] %s:%d Different wired interface type"
+ " [%s] %s:%d Failed to allocate system audio callback queue"
+ " [%s] %s:%d Invalid reportingStats"
+ " [%s] %s:%d Peer subscribed streams update occured while in OneToOne mode. Ignoring subscribed streams update"
+ " [%s] %s:%d Reset peer subscribed streams: current subscription=%@"
+ " [%s] %s:%d Session[%@] received callback for didUpdateConfig didSucceed=%{BOOL}d"
+ " [%s] %s:%d current connection is nil"
+ " [%s] %s:%d injector=%@, _audioSampleCount=%d, _loopLength=%f, _samplesInLoop=%d"
+ " [%s] %s:%d injector=%@, _samplesInLoop=%d, loopLength=%f"
+ " [%s] %s:%d new connection is nil"
+ " [%s] %s:%d new connection selection policy is nil"
+ " [%s] %s:%d recvmsg failed for socket=%d"
+ " [%s] %s:%d stopped processing audio packets"
+ "%@ path=%@, fromBeginning=%d, base=%0.2f, modulo=%0.2f"
+ "%d:%d:%d:%d:%d:%d:%d:%d:%d"
+ "-[AVCRateController isNetworkForcingECNEnabled]"
+ "-[VCCannedAudioInjector loadEncodedAudioSamples]_block_invoke"
+ "-[VCCannedAudioInjector setupAVSyncWithStartHostTime:loopLength:]"
+ "-[VCConnectionSelector isPrimaryConnectionSameAsConnection:]"
+ "-[VCConnectionSelector updateConnectionSelectionPolicy:]"
+ "-[VCIDSSessionInfoSynchronizer(PrivateMethods) resetPeerSubscribedStreams]"
+ "-[VCNetworkFeedbackController requestWRMNotification]_block_invoke"
+ "-[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:collectSubtype:]"
+ "-[VCSession readAndSetABCSymptomsReportingThresholdsFromStorebags:]"
+ "-[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:]"
+ "-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:configurationDict:]_block_invoke"
+ "-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:]"
+ "-g"
+ "2005"
+ "2005.6.1.1.2"
+ "AVCRC [%s] %s:%d Network layer ECN Default is set=%d"
+ "JBJumpSpikeCount"
+ "JBSlopeSpikeCount"
+ "JBSpikeSizeDelta"
+ "NonCellular"
+ "RTPDownlinkEgressAudioPkts"
+ "RTPDownlinkEgressVideoPkts"
+ "RTPDownlinkIngressAudioPkts"
+ "RTPDownlinkIngressNonDupMediaPkts"
+ "RTPDownlinkIngressVideoPkts"
+ "RTPGetDownlinkReportingStats"
+ "RTPGetUplinkReportingStats"
+ "RTPUplinkIngressAudioPkts"
+ "RTPUplinkIngressVideoPkts"
+ "RedOverheadDelay"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}},R,VaudioReceiver"
+ "VCConnection_IsLocalOnWiFiOrWired"
+ "VCConnection_IsLocalOnWired"
+ "VCConnection_IsRemoteOnWiFiOrWired"
+ "VCConnection_IsRemoteOnWired"
+ "VCMQEgressAudioPkts"
+ "VCMQEgressNonDupAudioPkts"
+ "VCMQEgressNonDupPkts"
+ "VCMQEgressNonDupVideoPkts"
+ "VCMQEgressPkts"
+ "VCMQEgressVideoPkts"
+ "VCMQFlushedPkts"
+ "VCMQIngressAudioPkts"
+ "VCMQIngressPkts"
+ "VCMQIngressQueuedPkts"
+ "VCMQIngressVideoPkts"
+ "VCMediaQueue [%s] %s:%d Not sending the malformatted packet out from VCMediaQueue! with timestamp=%d"
+ "VCSession [%s] %s:%d Threshold values: audioConnectionTime=%d, audioErasurePercentage=%d, poorConnectionPercentage=%d, videoConnectionTime=%d, videoStallPercentage=%d"
+ "VCSession [%s] %s:%d reportingConfig is nil!"
+ "VCVideoStream [%s] %s:%d %@(%p) ITU_R_2020 color settings used to configure capture and encoder"
+ "VCVideoStream [%s] %s:%d %@(%p) No color settings applied"
+ "VCVideoStream [%s] %s:%d %@(%p) P3D65-PQ color settings used to configure capture and encoder"
+ "VCVideoStream [%s] %s:%d ITU_R_2020 color settings used to configure capture and encoder"
+ "VCVideoStream [%s] %s:%d Memory allocation for colorInfo dictionary failed"
+ "VCVideoStream [%s] %s:%d No color settings applied"
+ "VCVideoStream [%s] %s:%d P3D65-PQ color settings used to configure capture and encoder"
+ "VRxIDRC"
+ "VideoReceiver [%s] %s:%d Failed to create reporting dictionary"
+ "^{?=BBBBBB}16@0:8"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}16@0:8"
+ "_VCAudioReceiver_CalculateAndReportRTPMetrics"
+ "_VTP_RecvFromDatagramSocket"
+ "_VideoReceiver_ReportFIRFBReceived"
+ "_VideoTransmitter_GetStreamIndexFromAttachment"
+ "_isNetworkForcingECNDefaultSet"
+ "_lastReportedRTPIngresspackets"
+ "_wrmClientQueue"
+ "applyClientSessionID:clientUserInfo:"
+ "collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:collectSubtype:"
+ "com.apple.AVConference.VCSystemAudioCapture.systemAudioQueue"
+ "com.apple.AVConference.vcNetworkFeedbackController.serialQueue"
+ "compareInterfacePriority:isPrimary:preferWired:"
+ "completionHandlerOneToOneEnabled:didSucceed:configurationDict:"
+ "dispatchedSetOneToOneModeEnabled:isLocal:configurationDict:"
+ "getStorebagValueForIntegerKey:defaultValue:"
+ "interfaceWired"
+ "isNetworkForcingECNDefaultSet"
+ "isNetworkForcingECNEnabled"
+ "network_enable_l4s"
+ "preferWiredOverWiFiEnabled"
+ "q32@0:8@16B24B28"
+ "q32@0:8@16^{?=BBBBBB}24"
+ "q36@0:8@\"<VCConnectionProtocol>\"16B24^{?=BBBBBB}28"
+ "q36@0:8@16B24^{?=BBBBBB}28"
+ "qrse_und2"
+ "readAndSetABCSymptomsReportingThresholdsFromStorebags:"
+ "readStorebagValueForStorebagKey:userDefaultKey:defaultValue:isDoubleType:"
+ "reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamGroupID:withStreamID:"
+ "reportingSessionParticipantEvent:withParticipant:withStreamGroupID:withStreamID:"
+ "resetPeerSubscribedStreams"
+ "setOneToOneModeEnabled:configurationDict:"
+ "setupVideoTransmitterConfigColorInfo:"
+ "shouldPreferWiredConnections"
+ "updateConnectionSelectionPolicy:"
+ "v24@0:8^{?=BBBBBB}16"
+ "v24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}}16"
+ "v36@0:8S16@20I28S32"
+ "v44@?0^{OpaqueAudioQueue=}8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}24I32r^{AudioStreamPacketDescription=qII}36"
+ "v52@0:8S16@20@28@36I44S48"
+ "v68@0:8^{__CFDictionary=}16S24@28@36@44I52S56^S60"
+ "vc-prefer-wired-over-wifi"
+ "vc-reporting-audio-connection-time-symptom-threshold"
+ "vc-reporting-audio-erasure-percentage-symptom-threshold"
+ "vc-reporting-poor-connection-percentage-symptom-threshold"
+ "vc-reporting-video-connection-time-symptom-threshold"
+ "vc-reporting-video-stall-percentage-symptom-threshold"
+ "wired"
+ "{?=\"preferRelayOverP2P\"B\"preferIPv6OverIPv4\"B\"preferNonVPN\"B\"e2eCriteriaEnabled\"B\"preferE2E\"B\"preferWired\"B}"
+ "{tagVCConnectionProtocolRealtimeVTable=\"matchesSourceDestinationInfo\"^?\"sourceDestinationInfo\"^?\"isRelay\"^?\"equal\"^?\"isLocalOnCellular\"^?\"isRemoteOnCellular\"^?\"isIPv6\"^?\"localCellTech\"^?\"setLocalCellTech\"^?\"remoteCellTech\"^?\"setRemoteCellTech\"^?\"copyDescription\"^?\"isLocalOnWiFiOrWired\"^?\"isRemoteOnWiFiOrWired\"^?\"isLocalOnWiFi\"^?\"isRemoteOnWiFi\"^?\"isLocalOnWired\"^?\"isRemoteOnWired\"^?\"isOnSameInterfacesWithConnection\"^?\"isEndToEndLink\"^?\"connectionID\"^?\"isLocalExpensive\"^?\"isLocalConstrained\"^?\"isRemoteExpensive\"^?\"isRemoteConstrained\"^?\"reportingIPVersion\"^?\"reportingQRServerConfig\"^?\"isHopByHopEncryptionSupported\"^?}"
- " [%s] %s:%d %@(%p) received callback for didUpdateConfig"
- " [%s] %s:%d received callback for didUpdateConfig"
- "%d:%d:%d:%d"
- "-[VCNetworkFeedbackController requestWRMNotification]"
- "-[VCSession collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamID:collectSubtype:]"
- "-[VCSession reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:]"
- "-[VCSession(OneToOne) completionHandlerOneToOneEnabled:didSucceed:]_block_invoke"
- "-[VCSession(OneToOne) dispatchedSetOneToOneModeEnabled:isLocal:]"
- "2000.8.1.1.1"
- "CannedAudioInjector[%p] path=%@, fromBeginning=%d, base=%0.2f, modulo=%0.2f>"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}},R,VaudioReceiver"
- "VCMediaQueue [%s] %s:%d Not sending bundled packets with multiple transmission attempts!"
- "VCMediaQueue [%s] %s:%d Not sending the malformatted packet out from VCMediaQueue!"
- "VCVideoStream [%s] %s:%d %@(%p) ITU_R_2020 color settings will be used to configure capture and encoder"
- "VCVideoStream [%s] %s:%d %@(%p) Memory allocation for HDR color settings failed"
- "VCVideoStream [%s] %s:%d %@(%p) P3D65 color settings will be used to configure capture and encoder"
- "VCVideoStream [%s] %s:%d ITU_R_2020 color settings will be used to configure capture and encoder"
- "VCVideoStream [%s] %s:%d Memory allocation for HDR color settings failed"
- "VCVideoStream [%s] %s:%d P3D65 color settings will be used to configure capture and encoder"
- "^{?=BBBBB}16@0:8"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}16@0:8"
- "_VCAudioReceiver_CalculateRTPMetrics"
- "_VideoTransmitter_ProcessTileIdAttachment"
- "_hdrColorInfo"
- "collectSessionEventKeyFieldsAndSubtype:eventType:withParticipant:keyChangeReason:newMKI:withStreamID:collectSubtype:"
- "compareInterfacePriority:isPrimary:"
- "completionHandlerOneToOneEnabled:didSucceed:"
- "composeClientUserInfo:"
- "dispatchedSetOneToOneModeEnabled:isLocal:"
- "q28@0:8@16B24"
- "q32@0:8@16^{?=BBBBB}24"
- "q36@0:8@\"<VCConnectionProtocol>\"16B24^{?=BBBBB}28"
- "q36@0:8@16B24^{?=BBBBB}28"
- "qrse_und"
- "reportingSessionParticipantEvent:withParticipant:keyChangeReason:newMKI:withStreamID:"
- "reportingSessionParticipantEvent:withStreamID:"
- "setVideoTransmitterConfigColorInfo:"
- "v24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B}16"
- "v48@0:8S16@20@28@36S44"
- "v64@0:8^{__CFDictionary=}16S24@28@36@44S52^S56"
- "{?=\"preferRelayOverP2P\"B\"preferIPv6OverIPv4\"B\"preferNonVPN\"B\"e2eCriteriaEnabled\"B\"preferE2E\"B}"
- "{tagVCConnectionProtocolRealtimeVTable=\"matchesSourceDestinationInfo\"^?\"sourceDestinationInfo\"^?\"isRelay\"^?\"equal\"^?\"isLocalOnCellular\"^?\"isRemoteOnCellular\"^?\"isIPv6\"^?\"localCellTech\"^?\"setLocalCellTech\"^?\"remoteCellTech\"^?\"setRemoteCellTech\"^?\"copyDescription\"^?\"isLocalOnWiFi\"^?\"isRemoteOnWiFi\"^?\"isOnSameInterfacesWithConnection\"^?\"isEndToEndLink\"^?\"connectionID\"^?\"isLocalExpensive\"^?\"isLocalConstrained\"^?\"isRemoteExpensive\"^?\"isRemoteConstrained\"^?\"reportingIPVersion\"^?\"reportingQRServerConfig\"^?\"isHopByHopEncryptionSupported\"^?}"

```
