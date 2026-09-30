## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2235.55.1.0.0
-  __TEXT.__text: 0x7d4120
-  __TEXT.__objc_methlist: 0x3a8e8
-  __TEXT.__const: 0xc6b0
-  __TEXT.__cstring: 0x9ead7
-  __TEXT.__oslogstring: 0x13e750
-  __TEXT.__gcc_except_tab: 0x2d08
+2235.57.1.0.0
+  __TEXT.__text: 0x7d7380
+  __TEXT.__objc_methlist: 0x3a968
+  __TEXT.__const: 0xc6c0
+  __TEXT.__cstring: 0x9eef2
+  __TEXT.__oslogstring: 0x13f959
+  __TEXT.__gcc_except_tab: 0x2cf8
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x12490
+  __TEXT.__unwind_info: 0x124c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7698
+  __DATA_CONST.__const: 0x7718
   __DATA_CONST.__objc_classlist: 0x14b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18bf0
+  __DATA_CONST.__objc_selrefs: 0x18c38
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1268
   __DATA_CONST.__objc_arraydata: 0x27c8
   __DATA_CONST.__got: 0x1e30
-  __AUTH_CONST.__const: 0x4528
-  __AUTH_CONST.__cfstring: 0x298e0
-  __AUTH_CONST.__objc_const: 0x6cd98
+  __AUTH_CONST.__const: 0x45c8
+  __AUTH_CONST.__cfstring: 0x299c0
+  __AUTH_CONST.__objc_const: 0x6ce28
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x52e0
+  __AUTH_CONST.__objc_intobj: 0x52f8
   __AUTH_CONST.__objc_arrayobj: 0x1d88
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x1d0
+  __AUTH_CONST.__objc_doubleobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x2c38
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x76b8
+  __DATA.__objc_ivar: 0x76c4
   __DATA.__data: 0x7d48
-  __DATA.__bss: 0x910
+  __DATA.__bss: 0x930
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xcf30
   __DATA_DIRTY.__data: 0x420
-  __DATA_DIRTY.__bss: 0xaf0
+  __DATA_DIRTY.__bss: 0xae0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35352
-  Symbols:   52949
-  CStrings:  33855
+  Functions: 35388
+  Symbols:   52994
+  CStrings:  33917
 
Symbols:
+ +[VCHardwareSettings supportsVideoPresentationOrientation]
+ -[AVConferenceXPCServer drainListenerQueues]
+ -[VCAudioCaptions reportEnabledRealtimeStats:]
+ -[VCAudioCaptions reportPostDisableRealtimeStats:]
+ -[VCConnectionManager safeDispatch:]
+ -[VCRateControlAlgorithmBase enableRampUpStuckFix]
+ -[VCRateControlAlgorithmBase setEnableRampUpStuckFix:]
+ -[VCSessionParticipantLocal _uplinkOvershootFixTargetForConnection:oldUplinkTargetBitrate:]
+ -[VCSessionParticipantRemote rtpTimestampRateForHomeKitSecureVideoModeWithStreamGroupID:fallbackRate:]
+ GCC_except_table104
+ GCC_except_table115
+ GCC_except_table126
+ GCC_except_table162
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table98
+ _CListCreate
+ _CListRelease
+ _OBJC_IVAR_$_VCRateControlAlgorithmBase._enableRampUpStuckFix
+ _OBJC_IVAR_$_VCRateControlAlgorithmLowLatencyContinuousTierMultiLink._maxMissingCount
+ _OBJC_IVAR_$_VCRateControlAlgorithmLowLatencyContinuousTierMultiLink._maxMissingLinkSSRC
+ _OBJC_IVAR_$_VCRateControlAlgorithmLowLatencyContinuousTierMultiLink._missingFeedbackCount
+ _VCFeatureFlagManager_ReduceKPIVariation.logOnceToken
+ _VCFeatureFlagManager_ReduceKPIVariation.osFlag
+ _VCMediaQueuePacketBundler_SetPropagateEnqueueError
+ _VCRateControlOscillationAvoidanceThreshold
+ _VCReduceKPIVariationKillSwitch
+ _VCReduceKPIVariationTierAThreshold
+ _VCReduceKPIVariationTierBThreshold
+ __VideoTransmitter_RetransmitPacketDispatched
+ ___36-[VCConnectionManager safeDispatch:]_block_invoke
+ ___44-[AVConferenceXPCServer drainListenerQueues]_block_invoke
+ ___44-[AVConferenceXPCServer drainListenerQueues]_block_invoke_2
+ ___44-[AVConferenceXPCServer drainListenerQueues]_block_invoke_3
+ ___58+[VCHardwareSettings supportsVideoPresentationOrientation]_block_invoke
+ ___VCFeatureFlagManager_ReduceKPIVariation_block_invoke_2
+ ____VideoTransmitter_RetransmitPacketDispatched_block_invoke
+ ____VideoTransmitter_RetransmitPacketsSerialized_block_invoke
+ ___block_descriptor_32_e521_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8l
+ ___block_descriptor_34_e5_v8?0l
+ ___block_descriptor_40_e8_32o_e521_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
+ ___block_descriptor_40_e8_32o_e522_v16?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
+ _kVCCMNWConnectionMonitorQueueKey
+ _kVCExperimentEnableRateControlOscillationAvoidance
+ _kVCExperimentReduceKPIVariationTierA
+ _kVCExperimentReduceKPIVariationTierB
+ _objc_msgSend$_uplinkOvershootFixTargetForConnection:oldUplinkTargetBitrate:
+ _objc_msgSend$enableRampUpStuckFix
+ _objc_msgSend$reportEnabledRealtimeStats:
+ _objc_msgSend$reportPostDisableRealtimeStats:
+ _objc_msgSend$rtpTimestampRateForHomeKitSecureVideoModeWithStreamGroupID:fallbackRate:
+ _objc_msgSend$safeDispatch:
+ _objc_msgSend$setEnableRampUpStuckFix:
+ _objc_msgSend$supportsVideoPresentationOrientation
+ _supportsVideoPresentationOrientation.onceToken
+ _supportsVideoPresentationOrientation.resolved
- GCC_except_table102
- GCC_except_table113
- GCC_except_table65
- GCC_except_table78
- GCC_except_table79
- _OBJC_IVAR_$_VCMediaStream._statisticsHandler
- _VCFeatureFlagManager_ReduceKPIVariation.flag
- ___VideoTransmitter_RetransmitPackets_block_invoke
- ___block_descriptor_40_e8_32o_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
- ___block_descriptor_40_e8_32o_e521_v16?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
- ___block_descriptor_48_e8_32r40r_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8lr32l8r40l8
CStrings:
+ " [%s] %s:%d %@(%p) Cannot start interrupt thread: selected client format is nil, will retry when audio unit properties are available"
+ " [%s] %s:%d %@(%p) KPI-VAR-STATE: multiwayImprovedFactor=%d"
+ " [%s] %s:%d %@(%p) KPI-VAR-STATE: uplinkOvershootFix=%d"
+ " [%s] %s:%d %@(%p) [FTDC] All camera connections disabled, stopping session to clear privacy indicator"
+ " [%s] %s:%d %@(%p) [FTDC] Camera connection enabled while previewing with session stopped, restarting session"
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/Others/RTPTransport.c:%d: RTP packet too short for CSRC list and extension header. size=%d expectedSize=%d"
+ " [%s] %s:%d @=@ Health: VCAudioCaptions Reporting post-disable Captions RealTime Stats: captionTaskCount=%u utteranceDuration=%d isUplink=%d"
+ " [%s] %s:%d Cannot start interrupt thread: selected client format is nil, will retry when audio unit properties are available"
+ " [%s] %s:%d Failure status=%d for streamId=%d, requestIntra=%d, isNonBaseLayerOfTemporalStream=%d RTPTimestamp=%u referenceMissing=%d decoding-order=%llu tileID=%llu"
+ " [%s] %s:%d Failure status=%d for streamId=%d, requestIntra=%d, isNonBaseLayerOfTemporalStream=%d RTPTimestamp=%u showFrame=%d referenceMissing=%d"
+ " [%s] %s:%d KPI-VAR-STATE: enableRTXSerializationFix=%d (videoTransmitter=%p)"
+ " [%s] %s:%d KPI-VAR-STATE: multiwayImprovedFactor=%d"
+ " [%s] %s:%d KPI-VAR-STATE: uplinkOvershootFix=%d"
+ " [%s] %s:%d Stream group=%s has no valid stream configurations"
+ " [%s] %s:%d Stream group=%s. Failed to initialize the video stream config"
+ " [%s] %s:%d VCHardwareSettings: videoPresentationOrientation support overridden by user default: outOfBox=%d override=%d"
+ " [%s] %s:%d VideoTransmitter[%p] TransmitQueue is NULL"
+ " [%s] %s:%d [FTDC] All camera connections disabled, stopping session to clear privacy indicator"
+ " [%s] %s:%d [FTDC] Camera connection enabled while previewing with session stopped, restarting session"
+ " [%s] %s:%d controllerIO is NULL"
+ "+[VCHardwareSettings supportsVideoPresentationOrientation]_block_invoke"
+ "-[AVCRateController loadDefaultVCRCFeatureFlags:]"
+ "-[VCAudioCaptions reportEnabledRealtimeStats:]"
+ "-[VCAudioCaptions reportPostDisableRealtimeStats:]"
+ "-[VCAudioRelayIOController removeAllClientsForIO:]"
+ "-[VCConnectionManager safeDispatch:]"
+ "-[VCRedundancyControlAlgorithmVideoMultiway initWithExperimentManager:]"
+ "-[VCSessionParticipantLocal _uplinkOvershootFixTargetForConnection:oldUplinkTargetBitrate:]"
+ "-[VCSessionParticipantRemote rtpTimestampRateForHomeKitSecureVideoModeWithStreamGroupID:fallbackRate:]"
+ "2235.57.1"
+ "AVCRC [%s] %s:%d %@(%p) KPI-VAR-STATE: enableInitialRampUpFix=%d"
+ "AVCRC [%s] %s:%d %@(%p) KPI-VAR-STATE: enableRampUpStuckFix=%d"
+ "AVCRC [%s] %s:%d %@(%p) KPI-VAR-STATE: isExperimentingRampUpTuning=%d"
+ "AVCRC [%s] %s:%d %@(%p) KPI-VAR-STATE: oscillationAvoidance=%d (experimentEnabled=%d)"
+ "AVCRC [%s] %s:%d KPI-VAR-STATE: enableInitialRampUpFix=%d"
+ "AVCRC [%s] %s:%d KPI-VAR-STATE: enableRampUpStuckFix=%d"
+ "AVCRC [%s] %s:%d KPI-VAR-STATE: isExperimentingRampUpTuning=%d"
+ "AVCRC [%s] %s:%d KPI-VAR-STATE: oscillationAvoidance=%d (experimentEnabled=%d)"
+ "CListCreate"
+ "CListRelease"
+ "KPI-VAR-STATE: ReduceKPIVariation=%{BOOL}d (osFlag=%{BOOL}d, killSwitchTriggered=%{BOOL}d)"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: Failed to create CLIST object"
+ "SIP [%s] %s:%d cList must not be nil"
+ "SIP [%s] %s:%d cList object is already NULL"
+ "VCFeatureFlagManager: ReduceKPIVariationSendAllFeedbackToRedundancyController=%{BOOL}d (defaultValue=%{BOOL}d)"
+ "VCMediaQueuePacketBundler_SetPropagateEnqueueError"
+ "VCRC [%s] %s:%d Poorest Link updated from [oldOwrd=%f,oldBWE=%d,oldDelay=%f,ssrc=0x%x] to [newOwrd=%f,newBWE=%d,newDelay=%f,ssrc=0x%x], worstLinkIndex=%d, totalNum=%u, maxMissing=[ssrc=0x%x, count=%u], arrivalTime=%f"
+ "VCSession [%s] %s:%d %@(%p) KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
+ "VCSession [%s] %s:%d %@(%p) KPI-VAR-STATE: propagateBundlerEnqueueError=%d (session)"
+ "VCSession [%s] %s:%d KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
+ "VCSession [%s] %s:%d KPI-VAR-STATE: propagateBundlerEnqueueError=%d (session)"
+ "VCSessionParticipantRemote [%s] %s:%d %@(%p) No HomeKit Secure Video RTP timestamp clock mapping for streamGroupID=%s; using negotiated rate fallbackRate=%u"
+ "VCSessionParticipantRemote [%s] %s:%d No HomeKit Secure Video RTP timestamp clock mapping for streamGroupID=%s; using negotiated rate fallbackRate=%u"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Assembled frame for decode TS=%u frameSequenceNumber=%d isRefreshFrame=%d didArriveAfterPlayout=%d isLate=%d isLTRPFrame=%d isIntraFrame=%d hasRetransmittedPackets=%d iLTRBits=0x%x decodingOrder=%u futureFramesSize=%u incompleteFramesSize=%u"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Frame not submitted TS=%u seq=%u frameSequenceNumber=%d isRefreshFrame=%d isLTRPFrame=%d isIntraFrame=%d iLTRBits=0x%x hasRetransmittedPackets=%d isLate=%d keyFrameRequestReason=%s futureFramesSize=%u incompleteFramesSize=%u"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Freeing frame TS=%u frameSequenceNumber=%d isLate=%d fScheduled=%d isFailedCompleteFrame=%d isLTRPFrame=%d isIntraFrame=%d hasRetransmittedPackets=%d"
+ "VideoReceiver [%s] %s:%d KPI-VAR-STATE: enableAdaptiveRTTWait=%d (videoReceiver=%p)"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] [recovery] Submitting late-recovered frame to decoder timestamp=%u showFrame=%d didFrameArriveLate=%d canDequeue=%d isRefreshFrame=%d decodingOrder=%d frameSequenceNumber=%d"
+ "_AVCRateController_CreateVCRateControlAlgorithm"
+ "_VideoPacketBuffer_FreeFrame"
+ "_VideoTransmitter_AccumulateRTXSendResult"
+ "_VideoTransmitter_RetransmitPacketDispatched"
+ "_VideoTransmitter_UpdateParametersForABTesting"
+ "enableCapture"
+ "enableReduceKPIVariationTierA"
+ "enableReduceKPIVariationTierB"
+ "forceHWSupportVideoPresentationOrientation"
+ "v16@?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
+ "v208@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
+ "vc-experiment-rate-control-oscillation-avoidance-threshold"
+ "vc-experiment-reduce-kpi-variation-tier-a-threshold"
+ "vc-experiment-reduce-kpi-variation-tier-b-threshold"
+ "vc-reduce-kpi-variation-kill-switch"
- " [%s] %s:%d Failed to initialize the video stream config"
- " [%s] %s:%d Failure status=%d for streamId=%d, requestIntra=%d, isNonBaseLayerOfTemporalStream=%d"
- "-[VCAudioCaptions gatherRealtimeStats:]"
- "2235.55.1"
- "VCFeatureFlagManager: ReduceKPIVariation=%d (defaultValue=%d)"
- "VCFeatureFlagManager: ReduceKPIVariation=%d (feature flag=%d)"
- "VCRC [%s] %s:%d Poorest Link updated from [oldOwrd=%f,oldBWE=%d,ssrc=0x%x] to [newOwrd=%f,newBWE=%d,ssrc=0x%x], worstLinkIndex=%d, arrivalTime=%f"
- "VideoTransmitter_RetransmitPackets_block_invoke"
- "forceSupportVideoPresentationOrientation"
- "v16@?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
- "v208@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
```
