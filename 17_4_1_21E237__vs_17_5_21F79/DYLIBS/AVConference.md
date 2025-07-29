## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2015.3.1.0.0
-  __TEXT.__text: 0x63b6f8
+2025.5.1.0.0
+  __TEXT.__text: 0x63c920
   __TEXT.__auth_stubs: 0x4c30
-  __TEXT.__objc_methlist: 0x2ac48
+  __TEXT.__objc_methlist: 0x2ac50
   __TEXT.__const: 0x7a08
-  __TEXT.__cstring: 0x751a4
-  __TEXT.__oslogstring: 0xd9da9
+  __TEXT.__cstring: 0x75388
+  __TEXT.__oslogstring: 0xda269
   __TEXT.__gcc_except_tab: 0x1f84
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xc728
+  __TEXT.__unwind_info: 0xc6d4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x42d9
-  __TEXT.__objc_methname: 0x69646
-  __TEXT.__objc_methtype: 0x211b9
-  __TEXT.__objc_stubs: 0x42be0
+  __TEXT.__objc_methname: 0x6975a
+  __TEXT.__objc_methtype: 0x21266
+  __TEXT.__objc_stubs: 0x42c20
   __DATA_CONST.__got: 0x1118
-  __DATA_CONST.__const: 0x5a18
+  __DATA_CONST.__const: 0x5a28
   __DATA_CONST.__objc_classlist: 0x1088
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f190
-  __DATA_CONST.__objc_selrefs: 0x13250
+  __DATA_CONST.__objc_const: 0x4f1e0
+  __DATA_CONST.__objc_selrefs: 0x13258
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x1200
   __DATA_CONST.__objc_superrefs: 0xee8
   __DATA_CONST.__objc_arraydata: 0x1eb8
-  __AUTH_CONST.__cfstring: 0x1fe20
-  __AUTH_CONST.__objc_intobj: 0x3a38
+  __AUTH_CONST.__cfstring: 0x1ff20
+  __AUTH_CONST.__objc_intobj: 0x3a68
   __AUTH_CONST.__objc_arrayobj: 0x1548
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x150
-  __AUTH_CONST.__const: 0x558
+  __AUTH_CONST.__const: 0x238
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__auth_got: 0x2630
-  __DATA.__objc_ivar: 0x5d90
-  __DATA.__data: 0x6f98
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x5db0
+  __DATA.__data: 0x6fa8
   __DATA.__bss: 0xa30
   __DATA.__common: 0x55
-  __DATA_DIRTY.__const: 0x2b18
+  __DATA_DIRTY.__const: 0x2e38
   __DATA_DIRTY.__objc_const: 0xc980
-  __DATA_DIRTY.__objc_data: 0xa550
+  __DATA_DIRTY.__objc_data: 0xa500
   __DATA_DIRTY.__data: 0x148
-  __DATA_DIRTY.__bss: 0x358
+  __DATA_DIRTY.__bss: 0x350
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 53B82FBF-7F1B-3AF1-8DA1-EB4BA60BEE2E
-  Functions: 28122
-  Symbols:   79033
-  CStrings:  48045
+  UUID: 30A5F3E1-9C2A-3805-9D0D-010C15B5A7DB
+  Functions: 28125
+  Symbols:   79051
+  CStrings:  48085
 
Symbols:
+ +[VCSessionParticipantRemote maxBdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
+ +[VCSessionParticipantRemote maxCameraQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]
+ +[VCSessionParticipantRemote maxCameraQualityIndexForVideoQuality:useWiFiTable:isSharingEnabled:]
+ +[VCSessionParticipantRemote maxCameraQualityIndexWithRedundancyForVideoQuality:useWiFiTable:]
+ +[VCSessionParticipantRemote maxFdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
+ +[VCSessionParticipantRemote maxFtxtQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
+ +[VCSessionParticipantRemote maxQualityIndexForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]
+ +[VCSessionParticipantRemote maxWebRTCCameraQualityIndexForVideoQuality:isLocalOnWiFi:isSharingEnabled:]
+ -[VCAudioStream reportTimestampJumpsWithReportingDictionary:]
+ -[VCSessionParticipantRemote appendStreamGroup:maxQualityIndex:mediaEntries:]
+ -[VCSessionParticipantRemote detectConnectionTimingSource]
+ -[VCSessionParticipantRemote reportConnectionTiming]
+ GCC_except_table169
+ _OBJC_IVAR_$_AVCRateController._lastRecordedHighRTT
+ _OBJC_IVAR_$_AVCRateController._lastUpdatedTargetBitrate
+ _OBJC_IVAR_$_VCAudioStream._periodicReportingMetrics
+ _OBJC_IVAR_$_VCRateControlServerBag._defaultExperimentConfigString
+ _OBJC_IVAR_$_VCSession._noPacketsSymptomReported
+ _OBJC_IVAR_$_VCSessionParticipantRemote._isCameraUsedForConnectionTiming
+ _OBJC_IVAR_$_VCSessionParticipantRemote._isConnectionTimingReported
+ _OBJC_IVAR_$_VCSessionParticipantRemote._isConnectionTimingSourceDetected
+ _OBJC_IVAR_$_VCVideoStreamReceiveGroup._lastRecordedExtendedPoorConnection
+ _VCNackGeneratorNackGenerationMaxPLR
+ _VCNackGeneratorNackGenerationMaxRTT
+ __VideoReceiver_CreateReportingEventDictionary
+ __VideoReceiver_CreateReportingEventDictionary.cold.1
+ ___35-[VCVideoStream updateVideoConfig:]_block_invoke.152
+ ___36-[VCVideoStream setupReportingAgent]_block_invoke.211
+ ___45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.49
+ ___52-[VCSessionParticipantRemote reportConnectionTiming]_block_invoke
+ ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.146
+ ___72-[VCAudioStreamReceiveGroup vcMediaStream:didReceiveFirstFrameWithTime:]_block_invoke_2
+ ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.100
+ ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.102
+ ____VCVideoStream_DidReceiveRemoteFrame_block_invoke.795
+ ___block_descriptor_40_e8_32o_e28_v32?0r^v8I16B20"NSError"24ls32l8
+ ___block_descriptor_tmp.211
+ _objc_msgSend$appendStreamGroup:maxQualityIndex:mediaEntries:
+ _objc_msgSend$detectConnectionTimingSource
+ _objc_msgSend$maxBdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
+ _objc_msgSend$maxCameraQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:
+ _objc_msgSend$maxCameraQualityIndexForVideoQuality:useWiFiTable:isSharingEnabled:
+ _objc_msgSend$maxCameraQualityIndexWithRedundancyForVideoQuality:useWiFiTable:
+ _objc_msgSend$maxFdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
+ _objc_msgSend$maxFtxtQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
+ _objc_msgSend$maxQualityIndexForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:
+ _objc_msgSend$maxWebRTCCameraQualityIndexForVideoQuality:isLocalOnWiFi:isSharingEnabled:
+ _objc_msgSend$reportConnectionTiming
+ _objc_msgSend$reportTimestampJumpsWithReportingDictionary:
- +[VCSessionParticipantRemote maxBdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
- +[VCSessionParticipantRemote maxCameraNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]
- +[VCSessionParticipantRemote maxCameraNetworkBitrateForVideoQuality:useWiFiBitrate:isSharingEnabled:]
- +[VCSessionParticipantRemote maxCameraNetworkBitrateWithRedundancyForVideoQuality:useWiFiBitrate:]
- +[VCSessionParticipantRemote maxFdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
- +[VCSessionParticipantRemote maxFtxtNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:]
- +[VCSessionParticipantRemote maxNetworkBitrateForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]
- -[VCDefaults multiwayVideoNetworkBitrateCapCellular]
- -[VCDefaults multiwayVideoNetworkBitrateCapWifi]
- -[VCHardwareSettings maxNetworkBitrateMultiwayVideoOnWifi:]
- -[VCSessionParticipantRemote appendStreamGroup:maxBitrate:mediaEntries:]
- GCC_except_table165
- _OBJC_IVAR_$_VCVideoStreamReceiveGroup._didReportExtendedPoorConnection
- ___35-[VCVideoStream updateVideoConfig:]_block_invoke.150
- ___36-[VCVideoStream setupReportingAgent]_block_invoke.209
- ___45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.40
- ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.128
- ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.82
- ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.84
- ____VCVideoStream_DidReceiveRemoteFrame_block_invoke.793
- ____VideoReceiver_SendRTCP_block_invoke.cold.1
- ___block_descriptor_48_e8_32o40o_e28_v32?0r^v8I16B20"NSError"24ls32l8s40l8
- ___block_descriptor_tmp.208
- _objc_msgSend$appendStreamGroup:maxBitrate:mediaEntries:
- _objc_msgSend$maxBdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
- _objc_msgSend$maxCameraNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:
- _objc_msgSend$maxCameraNetworkBitrateForVideoQuality:useWiFiBitrate:isSharingEnabled:
- _objc_msgSend$maxCameraNetworkBitrateWithRedundancyForVideoQuality:useWiFiBitrate:
- _objc_msgSend$maxFdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
- _objc_msgSend$maxFtxtNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:
- _objc_msgSend$maxNetworkBitrateForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:
- _objc_msgSend$multiwayVideoNetworkBitrateCapCellular
- _objc_msgSend$multiwayVideoNetworkBitrateCapWifi
CStrings:
+ " [%s] %s:%d %@(%p) Changed redundancyPercentage=%d applying _redundancyPercentage=%d"
+ " [%s] %s:%d Changed redundancyPercentage=%d applying _redundancyPercentage=%d"
+ " [%s] %s:%d Not sending NACK because [nackGenerated=%d throttleNackGeneration=%d missingPacketIsTooOld=%d] ssrc=%u ssrc=0x%x and seqNum=%u seqNum=0x%x arrivalTime=%f timeOfRequest=%f diff=%f timeOfFirstRequest=%f diff=%f rtt=%2.3fs plr=%3.2f%% nackGenerationThrottlingFactor=%f isSameSeqNum=%d seqNumRequested=%u seqNumHash=%d highPacketLossRatioObserved=%d highRTTObserved=%d disableNACKDueToUnsuitableNetworkConditions=%d"
+ "+[VCSessionParticipantRemote maxCameraQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]"
+ "+[VCSessionParticipantRemote maxWebRTCCameraQualityIndexForVideoQuality:isLocalOnWiFi:isSharingEnabled:]"
+ "-[VCRateControlServerBag getExperimentConfig:defaultValue:]"
+ "-[VCSessionParticipantRemote detectConnectionTimingSource]"
+ "-[VCSessionParticipantRemote didReceiveFirstFrameForStreamGroup:]"
+ "-[VCSessionParticipantRemote reportConnectionTiming]_block_invoke"
+ "2025.5.1"
+ "@64@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}16@24r^{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}32^{opaqueRTCReporting=}40@48^{tagHANDLE=i}56"
+ "AFECL"
+ "AVCRC [%s] %s:%d Use default experiment string:%@"
+ "T{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd},V_videoReceiverConfig"
+ "VCASTimestampJumpCount"
+ "VCASTimestampJumpDuration"
+ "VCASTimestampJumpMax"
+ "VCCallSession [%s] %s:%d %@(%p) Not continuing version check because we're not in FaceTime. operatingMode=%d, deviceRole=%d, isGKVoiceChat=%{BOOL}d, remoteCallInfo.frameworkVersion=%@"
+ "VCCallSession [%s] %s:%d Not continuing version check because we're not in FaceTime. operatingMode=%d, deviceRole=%d, isGKVoiceChat=%{BOOL}d, remoteCallInfo.frameworkVersion=%@"
+ "VCSession [%s] %s:%d Call is stalling for=%f seconds and cellular links are available"
+ "VCSession [%s] %s:%d Call is stalling for=%f seconds and no links available"
+ "VCSession [%s] %s:%d Call is stalling for=%f seconds and only WLAN links are available"
+ "VCSessionParticipantRemote [%s] %s:%d %@(%p) VideoQuality=%d isRedundancyRequested=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxQualityIndex=%d"
+ "VCSessionParticipantRemote [%s] %s:%d %@(%p) videoQuality=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxQualityIndex=%d"
+ "VCSessionParticipantRemote [%s] %s:%d Connection timing for participantID=%llu clocked by %@ for this call"
+ "VCSessionParticipantRemote [%s] %s:%d Participant=%@ received first media frame for streamGroup=%@, "
+ "VCSessionParticipantRemote [%s] %s:%d Remote participantID=%llu connection timing=%f clocked by '%@' streamGroup"
+ "VCSessionParticipantRemote [%s] %s:%d VideoQuality=%d isRedundancyRequested=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxQualityIndex=%d"
+ "VCSessionParticipantRemote [%s] %s:%d videoQuality=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxQualityIndex=%d"
+ "VCVideoStream [%s] %s:%d Loaded storebag values for VCNackGenerator: nackGeneratorStorebagConfigVersion=%u nackSeqNumAgingDuration=%f isExtraDelayForPacketRetransmissionsEnabled=%d nackThrottlingBitRateLimitingMaxRatio=%f nackThrottlingPlrBuckets[%@] nackThrottlingFactorBuckets[%@] nackGenerationMaxPLR=%f nackGenerationMaxRTT=%f"
+ "_defaultExperimentConfigString"
+ "_isCameraUsedForConnectionTiming"
+ "_isConnectionTimingReported"
+ "_isConnectionTimingSourceDetected"
+ "_lastRecordedExtendedPoorConnection"
+ "_lastRecordedHighRTT"
+ "_lastUpdatedTargetBitrate"
+ "_noPacketsSymptomReported"
+ "_periodicReportingMetrics"
+ "appendStreamGroup:maxQualityIndex:mediaEntries:"
+ "came"
+ "detectConnectionTimingSource"
+ "disableBBAdaptation"
+ "disableBBFlush"
+ "maxBdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
+ "maxCameraQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:"
+ "maxCameraQualityIndexForVideoQuality:useWiFiTable:isSharingEnabled:"
+ "maxCameraQualityIndexWithRedundancyForVideoQuality:useWiFiTable:"
+ "maxFdatQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
+ "maxFtxtQualityIndexForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
+ "maxQualityIndexForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:"
+ "maxWebRTCCameraQualityIndexForVideoQuality:isLocalOnWiFi:isSharingEnabled:"
+ "mic"
+ "reportConnectionTiming"
+ "reportTimestampJumpsWithReportingDictionary:"
+ "v1376@0:8{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}16"
+ "v24@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}16"
+ "v32@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}16@24"
+ "vc-nack-generator-nack-generation-max-plr"
+ "vc-nack-generator-nack-generation-max-rtt"
+ "vcrcExperimentConfig"
+ "{tagVCAudioStreamPeriodicReportingMetrics=\"timestampJumpCount\"AI\"timestampJumpDuration\"AQ\"timestampJumpMax\"AQ}"
+ "{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}24@0:8@16"
+ "{tagVCVideoPacketBufferConfig=SIi^v[200c]iBB^{__CFAllocator}BBB{tagVCVideoPacketBufferFrameDecryptionCallbackContext=^v^?}{tagVCVideoPacketBufferEnqueueFailedFrameToJitterBufferCallbackContext=^v^?}B^{tagVCNACKGenerator}{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}}24@0:8^{_RTPMediaPacket=iiiSIISBdBBBQ[12S]CC{?=iiBQ}Q{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}BBBC}16"
+ "{tagVCVideoReceiverConfig=\"streamCount\"I\"streamConfigs\"[9{tagVCVideoReceiverStreamConfig=\"streamInfo\"{tagVCVideoReceiverStreamIDInfo=\"streamID\"S\"repairStreamID\"S\"baseStreamID\"S\"subStreamCount\"I\"subStreamIDs\"[9S]\"subStreamRepairIDs\"[9S]}\"rtpHandle\"^{tagHANDLE}\"featureListStrings\"^{__CFDictionary}\"onDemandIDR\"B\"framerate\"S\"tileIndex\"C\"isOneToOne\"B\"isTemporalScalingEnabled\"B\"sframeCryptor\"^{tagVCCryptor}\"mediaControlInfoGenerator\"^v\"statisticsCollector\"^v\"mode\"i\"isLTRPEnabled\"B\"isRTCPForLossFeedbackEnabled\"B\"isRTCPForLTRPAckEnabled\"B\"ltrAckRTCPPacketType\"i\"shouldEnableMLEnhance\"B}]\"mode\"i\"jitterBufferMode\"i\"streamToken\"q\"audioTSRate\"i\"videoTSRate\"i\"enableVPBLogging\"i\"dumpID\"I\"enableControlByte\"i\"enableBitstreamCapture\"i\"enableRxDecodeYUVDump\"i\"enableUEP\"i\"enableRecvBitstreamDump\"i\"reportingParentID\"i\"shouldEnableFaceZoom\"B\"useDisplayLink\"B\"enableDeferredAssembly\"B\"deferredAssemblyOffset\"d\"callbackContext\"^v\"remoteFrameCallback\"^?\"sampleBufferCallback\"^?\"streamSwitchCallback\"^?\"keyFrameGenerationCallback\"^?\"sendLTRAckCallback\"^?\"ackLTRFrameCallback\"^?\"modeSwitchCallback\"^?\"idsParticipantID\"Q\"triggerSoundAlarmOnRTPReceive\"B\"decoderNumOfTiles\"S\"useInternalRTPThreading\"B\"wrmInfo\"^{tagWRMMetricsInfo}\"maxDisplayRefreshRate\"I\"enableJitterBufferInReceiver\"B\"enableJitterBufferInPlayer\"B\"enableImmediateDecode\"B\"isLTRPEnabled\"B\"isAsyncDecodingEnabled\"B\"isReceiverSideVCRCFeedbackEnabled\"B\"isVCRCStatsOnlyVideoBased\"B\"fecHeaderV1Enabled\"B\"enableQueueAlarmForDisplay\"B\"useRTCPForFIR\"B\"sendRTCP_PSFB_FIR\"B\"enableJBDynamicModeSwitch\"B\"useInternalClockForPresentation\"B\"mediaControlInfoGenerator\"^v\"isVariableSliceModeEnabled\"B\"streamSwitchEnabled\"B\"cvoExtensionID\"I\"videoJBEnabled\"B\"enableAVLooseSync\"B\"targetDisplayAlarmCount\"S\"jbTargetEstimatorSynchronizer\"^{tagVCJBTargetEstimatorSynchronizer}\"participantId\"^{__CFString}\"sessionId\"^{__CFString}\"streamGroupID\"I\"isReferenceFrameEnabled\"B\"isLateFrameRecoveryEnabled\"B\"enableHighWatermarkQueueDiscard\"B\"externalPresentationClockType\"i\"isServerPacketRetransmissionEnabled\"B\"isRTTBasedFIRThrottlingEnabled\"B\"nackGeneratorStoreBagsConfig\"{tagVCNACKGeneratorStoreBagsConfig=\"nackGeneratorStorebagConfigVersion\"C\"nackSeqNumAgingDuration\"f\"nackThrottlingBitRateLimitingMaxRatio\"f\"isExtraDelayForPacketRetransmissionsEnabled\"B\"nackThrottlingFactorBuckets\"[4f]\"nackThrottlingPlrBuckets\"[4f]\"nackGenerationMaxPLR\"f\"nackGenerationMaxRTT\"f}\"forceZeroRegionOfInterestOrigin\"B\"cannedReplayContext\"^v\"rateAdaptation\"^v\"overlayToken\"q\"minPlaybackInterval\"d}"
+ "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}16@0:8"
+ "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]ff}B^v^vqd}24@0:8@16"
- " [%s] %s:%d %@(%p) redundancyPercentage=%d"
- " [%s] %s:%d Not sending NACK because [nackGenerated=%d throttleNackGeneration=%d missingPacketIsTooOld=%d] ssrc=%u ssrc=0x%x and seqNum=%u seqNum=0x%x arrivalTime=%f timeOfRequest=%f diff=%f timeOfFirstRequest=%f diff=%f rtt=%2.3fs plr=%3.2f%% nackGenerationThrottlingFactor=%f isSameSeqNum=%d seqNumRequested=%u seqNumHash=%d"
- " [%s] %s:%d redundancyPercentage=%d"
- "+[VCSessionParticipantRemote maxCameraNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:]"
- "2015.3.1"
- "@64@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}16@24r^{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}32^{opaqueRTCReporting=}40@48^{tagHANDLE=i}56"
- "T{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd},V_videoReceiverConfig"
- "VCCallSession [%s] %s:%d %@(%p) Not continuing version check because we're not in FaceTime. operatingMode=%d, deviceRole=%d, isGKVoiceChat=%{BOOL}d"
- "VCCallSession [%s] %s:%d Not continuing version check because we're not in FaceTime. operatingMode=%d, deviceRole=%d, isGKVoiceChat=%{BOOL}d"
- "VCSessionParticipantRemote [%s] %s:%d %@(%p) useForcedNetworkBitrate=%d videoQuality=%d isRedundancyRequested=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxNetworkBitrate=%d"
- "VCSessionParticipantRemote [%s] %s:%d useForcedNetworkBitrate=%d videoQuality=%d isRedundancyRequested=%d isLocalOnWiFi=%d isDeviceLargeScreen=%d isSharingEnabled=%d, shouldLimitCameraQualityForSharing=%d, maxNetworkBitrate=%d"
- "VCVideoStream [%s] %s:%d Loaded storebag values for VCNackGenerator: nackGeneratorStorebagConfigVersion=%u nackSeqNumAgingDuration=%f isExtraDelayForPacketRetransmissionsEnabled=%d nackThrottlingBitRateLimitingMaxRatio=%f nackThrottlingPlrBuckets[%@] nackThrottlingFactorBuckets[%@]"
- "_didReportExtendedPoorConnection"
- "appendStreamGroup:maxBitrate:mediaEntries:"
- "maxBdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
- "maxCameraNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:"
- "maxCameraNetworkBitrateForVideoQuality:useWiFiBitrate:isSharingEnabled:"
- "maxCameraNetworkBitrateWithRedundancyForVideoQuality:useWiFiBitrate:"
- "maxFdatNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
- "maxFtxtNetworkBitrateForVideoQuality:isLocalOnWiFi:isRedundancyRequested:"
- "maxNetworkBitrateForStreamGroupID:videoQuality:isLocalOnWiFi:isRedundancyRequested:isSharingEnabled:"
- "maxNetworkBitrateMultiwayVideoOnWifi:"
- "multiwayVideoNetworkBitrateCapCellular"
- "multiwayVideoNetworkBitrateCapWifi"
- "v1368@0:8{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}16"
- "v24@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}16"
- "v32@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}16@24"
- "{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}24@0:8@16"
- "{tagVCVideoPacketBufferConfig=SIi^v[200c]iBB^{__CFAllocator}BBB{tagVCVideoPacketBufferFrameDecryptionCallbackContext=^v^?}{tagVCVideoPacketBufferEnqueueFailedFrameToJitterBufferCallbackContext=^v^?}B^{tagVCNACKGenerator}{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}}24@0:8^{_RTPMediaPacket=iiiSIISBdBBBQ[12S]CC{?=iiBQ}Q{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}BBBC}16"
- "{tagVCVideoReceiverConfig=\"streamCount\"I\"streamConfigs\"[9{tagVCVideoReceiverStreamConfig=\"streamInfo\"{tagVCVideoReceiverStreamIDInfo=\"streamID\"S\"repairStreamID\"S\"baseStreamID\"S\"subStreamCount\"I\"subStreamIDs\"[9S]\"subStreamRepairIDs\"[9S]}\"rtpHandle\"^{tagHANDLE}\"featureListStrings\"^{__CFDictionary}\"onDemandIDR\"B\"framerate\"S\"tileIndex\"C\"isOneToOne\"B\"isTemporalScalingEnabled\"B\"sframeCryptor\"^{tagVCCryptor}\"mediaControlInfoGenerator\"^v\"statisticsCollector\"^v\"mode\"i\"isLTRPEnabled\"B\"isRTCPForLossFeedbackEnabled\"B\"isRTCPForLTRPAckEnabled\"B\"ltrAckRTCPPacketType\"i\"shouldEnableMLEnhance\"B}]\"mode\"i\"jitterBufferMode\"i\"streamToken\"q\"audioTSRate\"i\"videoTSRate\"i\"enableVPBLogging\"i\"dumpID\"I\"enableControlByte\"i\"enableBitstreamCapture\"i\"enableRxDecodeYUVDump\"i\"enableUEP\"i\"enableRecvBitstreamDump\"i\"reportingParentID\"i\"shouldEnableFaceZoom\"B\"useDisplayLink\"B\"enableDeferredAssembly\"B\"deferredAssemblyOffset\"d\"callbackContext\"^v\"remoteFrameCallback\"^?\"sampleBufferCallback\"^?\"streamSwitchCallback\"^?\"keyFrameGenerationCallback\"^?\"sendLTRAckCallback\"^?\"ackLTRFrameCallback\"^?\"modeSwitchCallback\"^?\"idsParticipantID\"Q\"triggerSoundAlarmOnRTPReceive\"B\"decoderNumOfTiles\"S\"useInternalRTPThreading\"B\"wrmInfo\"^{tagWRMMetricsInfo}\"maxDisplayRefreshRate\"I\"enableJitterBufferInReceiver\"B\"enableJitterBufferInPlayer\"B\"enableImmediateDecode\"B\"isLTRPEnabled\"B\"isAsyncDecodingEnabled\"B\"isReceiverSideVCRCFeedbackEnabled\"B\"isVCRCStatsOnlyVideoBased\"B\"fecHeaderV1Enabled\"B\"enableQueueAlarmForDisplay\"B\"useRTCPForFIR\"B\"sendRTCP_PSFB_FIR\"B\"enableJBDynamicModeSwitch\"B\"useInternalClockForPresentation\"B\"mediaControlInfoGenerator\"^v\"isVariableSliceModeEnabled\"B\"streamSwitchEnabled\"B\"cvoExtensionID\"I\"videoJBEnabled\"B\"enableAVLooseSync\"B\"targetDisplayAlarmCount\"S\"jbTargetEstimatorSynchronizer\"^{tagVCJBTargetEstimatorSynchronizer}\"participantId\"^{__CFString}\"sessionId\"^{__CFString}\"streamGroupID\"I\"isReferenceFrameEnabled\"B\"isLateFrameRecoveryEnabled\"B\"enableHighWatermarkQueueDiscard\"B\"externalPresentationClockType\"i\"isServerPacketRetransmissionEnabled\"B\"isRTTBasedFIRThrottlingEnabled\"B\"nackGeneratorStoreBagsConfig\"{tagVCNACKGeneratorStoreBagsConfig=\"nackGeneratorStorebagConfigVersion\"C\"nackSeqNumAgingDuration\"f\"nackThrottlingBitRateLimitingMaxRatio\"f\"isExtraDelayForPacketRetransmissionsEnabled\"B\"nackThrottlingFactorBuckets\"[4f]\"nackThrottlingPlrBuckets\"[4f]}\"forceZeroRegionOfInterestOrigin\"B\"cannedReplayContext\"^v\"rateAdaptation\"^v\"overlayToken\"q\"minPlaybackInterval\"d}"
- "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}16@0:8"
- "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiB}]iiqiiiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSB^{tagWRMMetricsInfo}IBBBBBBBBBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]}B^v^vqd}24@0:8@16"

```
