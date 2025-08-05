## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.57.1.0.0
-  __TEXT.__text: 0x7902e0
+2145.61.1.0.0
+  __TEXT.__text: 0x792424
   __TEXT.__auth_stubs: 0x5600
-  __TEXT.__objc_methlist: 0x357c0
+  __TEXT.__objc_methlist: 0x35968
   __TEXT.__const: 0xc760
-  __TEXT.__cstring: 0x8ea45
-  __TEXT.__oslogstring: 0x10e0e2
-  __TEXT.__gcc_except_tab: 0x2ae8
-  __TEXT.__ustring: 0x1a8
-  __TEXT.__unwind_info: 0x107d8
+  __TEXT.__cstring: 0x8ef1a
+  __TEXT.__oslogstring: 0x10e57a
+  __TEXT.__gcc_except_tab: 0x2ab0
+  __TEXT.__ustring: 0x2d4
+  __TEXT.__unwind_info: 0x10828
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d491
-  __TEXT.__objc_methtype: 0x28248
-  __TEXT.__objc_stubs: 0x4e880
+  __TEXT.__objc_methname: 0x7d752
+  __TEXT.__objc_methtype: 0x28277
+  __TEXT.__objc_stubs: 0x4e9c0
   __DATA_CONST.__got: 0x1a30
-  __DATA_CONST.__const: 0x6a10
+  __DATA_CONST.__const: 0x6a80
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16878
+  __DATA_CONST.__objc_selrefs: 0x168d0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b18
   __AUTH_CONST.__const: 0x3bc8
-  __AUTH_CONST.__cfstring: 0x26040
-  __AUTH_CONST.__objc_const: 0x63088
+  __AUTH_CONST.__cfstring: 0x261c0
+  __AUTH_CONST.__objc_const: 0x63388
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x6bf8
+  __AUTH.__objc_data: 0x1590
+  __DATA.__objc_ivar: 0x6c38
   __DATA.__data: 0x7870
-  __DATA.__bss: 0xd28
+  __DATA.__bss: 0xd20
   __DATA.__common: 0x55
-  __DATA_DIRTY.__objc_data: 0xa9b0
+  __DATA_DIRTY.__objc_data: 0xa780
   __DATA_DIRTY.__data: 0x160
   __DATA_DIRTY.__bss: 0x468
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E813D7A2-B9D6-346B-BAA8-1455A2002CD6
-  Functions: 31480
-  Symbols:   97106
-  CStrings:  57034
+  UUID: 5516BA11-CC7A-3B3B-88C4-72E2D68714DA
+  Functions: 31529
+  Symbols:   97231
+  CStrings:  57117
 
Symbols:
+ +[VCStringUtils cStringFromTierPickerMode:]
+ +[VideoUtil lowPowerModeEncodingResolutionForMaxResolution:]
+ +[VideoUtil maxCaptureEncodingResolutionForStreamConfigResolution:lowPowerModeEnabled:]
+ -[AVCCaptionsConfig isFormatForNewLinesEnabled]
+ -[AVCCaptionsConfig setFormatForNewLinesEnabled:]
+ -[VCAudioCaptions dispatchedSetFormatForNewLinesEnabled:]
+ -[VCAudioCaptions isFormatForNewLinesEnabled]
+ -[VCAudioCaptions setFormatForNewLinesEnabled:]
+ -[VCAudioStream setOperatingMode:]
+ -[VCAudioStreamGroupCommon isVADFilteringEnabled]
+ -[VCAudioStreamGroupCommon setVADFilteringEnabled:]
+ -[VCAudioStreamReceiveGroup isVADFilteringEnabled]
+ -[VCAudioStreamReceiveGroup setVADFilteringEnabled:]
+ -[VCAudioStreamReceiveGroup updateActiveVoiceOnly:]
+ -[VCAudioStreamSendGroup updateOperatingMode:]
+ -[VCAudioTransmitter setTierPickerMode:]
+ -[VCAudioTransmitter tierPickerMode]
+ -[VCCaptionsConfig initWithCoder:].cold.9
+ -[VCCaptionsConfig isFormatForNewLinesEnabled]
+ -[VCCaptionsConfig setFormatForNewLinesEnabled:]
+ -[VCCaptionsStreamSendGroup isVADFilteringEnabled]
+ -[VCCaptionsStreamSendGroup setVADFilteringEnabled:]
+ -[VCMediaNegotiationBlobV2GeneralInfo hasRtxVersion]
+ -[VCMediaNegotiationBlobV2GeneralInfo rtxVersion]
+ -[VCMediaNegotiationBlobV2GeneralInfo setHasRtxVersion:]
+ -[VCMediaNegotiationBlobV2GeneralInfo setRtxVersion:]
+ -[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:rtxVersion:]
+ -[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:rtxVersion:].cold.1
+ -[VCMediaNegotiatorLocalConfiguration rtxVersion]
+ -[VCMediaNegotiatorLocalConfiguration setRtxVersion:]
+ -[VCMediaNegotiatorResults rtxVersion]
+ -[VCMediaNegotiatorResults setRtxVersion:]
+ -[VCSession enableVCOverlay]
+ -[VCSessionParticipantConfig p2pEncryptionEnabled]
+ -[VCSessionParticipantConfig setP2pEncryptionEnabled:]
+ -[VCSessionParticipantRemote enableVADFiltering]
+ -[VCSessionParticipantRemote setEnableVADFiltering:]
+ -[VCSessionParticipantRemote updateActiveVoiceOnly]
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table158
+ GCC_except_table194
+ _OBJC_IVAR_$_AVCCaptionsConfig._formatForNewLinesEnabled
+ _OBJC_IVAR_$_AVCRateController._rateSharingClientID
+ _OBJC_IVAR_$_VCAudioCaptions._formatForNewLinesEnabled
+ _OBJC_IVAR_$_VCAudioCaptions._previousConverterSamplesAllocator
+ _OBJC_IVAR_$_VCAudioStreamGroupCommon._isVADFilteringEnabled
+ _OBJC_IVAR_$_VCAudioStreamReceiveGroup._isVADFilteringEnabled
+ _OBJC_IVAR_$_VCCaptionsConfig._formatForNewLinesEnabled
+ _OBJC_IVAR_$_VCCaptionsStreamSendGroup._isVADFilteringEnabled
+ _OBJC_IVAR_$_VCMediaNegotiationBlobV2GeneralInfo._rtxVersion
+ _OBJC_IVAR_$_VCMediaNegotiatorLocalConfiguration._rtxVersion
+ _OBJC_IVAR_$_VCMediaNegotiatorResults._rtxVersion
+ _OBJC_IVAR_$_VCPowerManager._forceDisableThermal
+ _OBJC_IVAR_$_VCRateSharingGroup._lastProbingSequenceAllowedTime
+ _OBJC_IVAR_$_VCSessionParticipantConfig._p2pEncryptionEnabled
+ _OBJC_IVAR_$_VCSessionParticipantLocal._p2pEncryptionEnabled
+ _OBJC_IVAR_$_VCSessionParticipantRemote._enableVADFiltering
+ _VCAudioReceiver_SetVADFiltering
+ _VCAudioReceiver_SetVADFiltering.cold.1
+ _VCJitterBuffer_SetVADFilteringEnabled
+ _VCOverlayManager_updateOverlayState
+ _VCOverlayManager_updateOverlayState.cold.1
+ _VCRateSharingGroup_IsProbingSequenceAllowed
+ ___28-[VCSession dispatchedStart]_block_invoke.605
+ ___28-[VCSession dispatchedStart]_block_invoke.606
+ ___45-[VCAudioCaptions isFormatForNewLinesEnabled]_block_invoke
+ ___47-[VCAudioCaptions setFormatForNewLinesEnabled:]_block_invoke
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.600
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.601
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.602
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.618
+ ___52-[VCAudioStreamReceiveGroup setVADFilteringEnabled:]_block_invoke
+ ___52-[VCSessionParticipantRemote setEnableVADFiltering:]_block_invoke
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.617
+ ___57-[VCAudioCaptions dispatchedSetFormatForNewLinesEnabled:]_block_invoke
+ ___VCOverlayManager_updateOverlayState_block_invoke
+ ___block_descriptor_49_e8_32o40o_e101_v36?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16B24"NSObject<OS_nw_error>"28ls32l8s40l8
+ ___block_descriptor_68_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.488
+ ___block_descriptor_tmp.552
+ ___block_descriptor_tmp.554
+ _objc_msgSend$cStringFromTierPickerMode:
+ _objc_msgSend$dispatchedSetFormatForNewLinesEnabled:
+ _objc_msgSend$enableVCOverlay
+ _objc_msgSend$initWithClientIdentifier:audioFormat:formatForNewLines:transcriberResultDelegate:endpointingResultDelegate:languageDetectorResultDelegate:speechDetectorResultDelegate:queue:transcriberOptions:options:languageDetectorOptions:speechDetectorOptions:restrictedLogging:contextualNamedEntities:didChangeVolatileRange:
+ _objc_msgSend$initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:rtxVersion:
+ _objc_msgSend$isFormatForNewLinesEnabled
+ _objc_msgSend$isP2PEncryptionExperimentEnabled
+ _objc_msgSend$lowPowerModeEncodingResolutionForMaxResolution:
+ _objc_msgSend$maxCaptureEncodingResolutionForStreamConfigResolution:lowPowerModeEnabled:
+ _objc_msgSend$p2pEncryptionEnabled
+ _objc_msgSend$rtxVersion
+ _objc_msgSend$setFormatForNewLinesEnabled:
+ _objc_msgSend$setRtxVersion:
+ _objc_msgSend$updateOperatingMode:
- -[VCHardwareSettingsEmbedded deviceShouldEnableLowPowerMode]
- -[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:]
- -[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:].cold.1
- -[VCSession reportInitialThermalLevel]
- GCC_except_table104
- GCC_except_table115
- GCC_except_table157
- GCC_except_table191
- GCC_except_table99
- __VCOverlayManager_updateOverlayState
- __VCOverlayManager_updateOverlayState.cold.1
- __VideoReceiver_AssembleAndEnqueueFrame.cold.2
- ___28-[VCSession dispatchedStart]_block_invoke.602
- ___28-[VCSession dispatchedStart]_block_invoke.603
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.594
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.598
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.599
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.615
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.614
- ____VCOverlayManager_updateOverlayState_block_invoke
- ___block_descriptor_49_e8_32o_e101_v36?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16B24"NSObject<OS_nw_error>"28ls32l8
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.485
- ___block_descriptor_tmp.549
- ___block_descriptor_tmp.551
- _objc_msgSend$deviceShouldEnableLowPowerMode
- _objc_msgSend$initWithClientIdentifier:audioFormat:transcriberResultDelegate:endpointingResultDelegate:languageDetectorResultDelegate:speechDetectorResultDelegate:queue:transcriberOptions:options:languageDetectorOptions:speechDetectorOptions:restrictedLogging:contextualNamedEntities:didChangeVolatileRange:
- _objc_msgSend$initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:
- _objc_msgSend$reportInitialThermalLevel
CStrings:
+ " [%s] %s:%d %@(%p) Missing value formatForNewLinesEnabled"
+ " [%s] %s:%d %@(%p) Negotiated p2pEncryptionExperimentEnabled=%d"
+ " [%s] %s:%d %@(%p) Update to formatForNewLinesEnabled=%{BOOL}d, state=%u"
+ " [%s] %s:%d Disable subframe dirty region detection on encoder for stitched layout"
+ " [%s] %s:%d Missing value formatForNewLinesEnabled"
+ " [%s] %s:%d Negotiated p2pEncryptionExperimentEnabled=%d"
+ " [%s] %s:%d Picking tier operatingMode=%s"
+ " [%s] %s:%d Setting one-to-one remote participant data for operatingMode=%s"
+ " [%s] %s:%d Setting tierPickerMode=%s. Resetting the audio tier picker"
+ " [%s] %s:%d Setting vadfilteringEnabled=%d"
+ " [%s] %s:%d Sharing group disallow probing sequence for registrationID=%d at time=%f and lastProbingSequenceAllowTime=%f"
+ " [%s] %s:%d Update to formatForNewLinesEnabled=%{BOOL}d, state=%u"
+ " [%s] %s:%d Updating operatingMode=%d"
+ " [%s] %s:%d VCFeatureExperimentSetting: Local rtxVersion=%d"
+ " [%s] %s:%d [AR_TX] .ratio is zero due to invalid input parameter(s); releasing remoteScreenAttributes"
+ " [%s] %s:%d operatingMode changed to %s"
+ "+[VCAudioTierPicker operatingModeToTierPickerMode:isLowLatency:preferPlistForTierTable:]"
+ "+[VideoUtil maxCaptureEncodingResolutionForStreamConfigResolution:lowPowerModeEnabled:]"
+ "-[VCAudioCaptions dispatchedSetFormatForNewLinesEnabled:]"
+ "-[VCAudioStream setOperatingMode:]"
+ "-[VCAudioStreamReceiveGroup updateActiveVoiceOnly:]"
+ "-[VCAudioStreamSendGroup updateOperatingMode:]"
+ "-[VCAudioTransmitter setOperatingMode:]"
+ "-[VCAudioTransmitter setTierPickerMode:]"
+ "-[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:rtxVersion:]"
+ "-[VCSession enableVCOverlay]"
+ "2145.61.1"
+ "@136@0:8{tagVCSFSpeechAnalyzerConfig=@@@@@@@@@@@B@B}16@?128"
+ "@52@0:8(tagNTP=Q{?=II})16{CGSize=dd}24I40C44C48"
+ "DisableDirtyDetection"
+ "L4SHUDEnabled"
+ "T@\"VCAudioTransmitter\",&,N,V_audioTransmitter"
+ "TB,N,GisFormatForNewLinesEnabled"
+ "TB,N,GisFormatForNewLinesEnabled,V_formatForNewLinesEnabled"
+ "TB,N,GisP2PEncryptionExperimentEnabled,V_p2pEncryptionExperimentEnabled"
+ "TB,N,SsetVADFilteringEnabled:"
+ "TB,N,V_p2pEncryptionEnabled"
+ "TC,N,V_rtxVersion"
+ "TI,N,V_rtxVersion"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B},R,VaudioReceiver"
+ "VCAudioReceiver_SetVADFiltering"
+ "VCAudioStream [%s] %s:%d operatingMode=%s tierPickerMode=%s"
+ "VCAudioTierPickerModeAudioOnlyV1"
+ "VCAudioTierPickerModeAudioOnlyV2"
+ "VCAudioTierPickerModeAudioVideoV1"
+ "VCAudioTierPickerModeAudioVideoV2"
+ "VCAudioTierPickerModeDefault"
+ "VCAudioTierPickerModeLowLatencyAudioOnly"
+ "VCAudioTierPickerModeLowLatencyAudioVideo"
+ "VCAudioTierPickerModeMultiway"
+ "VCAudioTierPickerModeTinCan"
+ "VCJitterBuffer_SetVADFilteringEnabled"
+ "VCRateSharingGroup_IsProbingSequenceAllowed"
+ "VCSession [%s] %s:%d %@(%p) L4SHUD key exist=%d, L4SHUDEnabled=%d"
+ "VCSession [%s] %s:%d L4SHUD key exist=%d, L4SHUDEnabled=%d"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}16@0:8"
+ "_formatForNewLinesEnabled"
+ "_lastProbingSequenceAllowedTime"
+ "_previousConverterSamplesAllocator"
+ "_rtxVersion"
+ "audioPlayerOvershootResiliencyDesiredQueueSampleThreshold"
+ "audioPlayerOvershootResiliencyMaxFrameConsiderationWindow"
+ "audioPlayerOvershootResiliencyMinorAdjustmentInterval"
+ "audioPlayerOvershootResiliencyObservationWindow"
+ "audioStreamEnableFixedJitterBufferInitialOvershootResiliency"
+ "cStringFromTierPickerMode:"
+ "dispatchedSetFormatForNewLinesEnabled:"
+ "enableSpeechFormatForNewLines"
+ "enableVCOverlay"
+ "formatForNewLinesEnabled"
+ "hasRtxVersion"
+ "initWithClientIdentifier:audioFormat:formatForNewLines:transcriberResultDelegate:endpointingResultDelegate:languageDetectorResultDelegate:speechDetectorResultDelegate:queue:transcriberOptions:options:languageDetectorOptions:speechDetectorOptions:restrictedLogging:contextualNamedEntities:didChangeVolatileRange:"
+ "initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:rtxVersion:"
+ "isFormatForNewLinesEnabled"
+ "lowPowerModeEncodingResolutionForMaxResolution:"
+ "maxCaptureEncodingResolutionForStreamConfigResolution:lowPowerModeEnabled:"
+ "rtxVersion"
+ "setFormatForNewLinesEnabled:"
+ "setHasRtxVersion:"
+ "setRtxVersion:"
+ "updateOperatingMode:"
+ "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}16"
+ "vcCaptionsFormatForNewLinesEnabled"
+ "videoPlayerQueueSizeOverrideEnabled"
+ "{?=\"ntpTime\"b1\"abSwitches\"b1\"fecHeaderVersion\"b1\"rtxVersion\"b1\"screenRes\"b1}"
+ "{CGSize=dd}28@0:8q16B24"
- " [%s] %s:%d Setting one-to-one remote participant data"
- "-[VCMediaNegotiationBlobV2GeneralInfo(Utils) initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:]"
- "-[VCSessionParticipantLocal captureEncodingSize]"
- "-[VCVideoStreamSendGroup getCaptureEncodingSize]"
- "2145.57.1"
- "@128@0:8{tagVCSFSpeechAnalyzerConfig=@@@@@@@@@@@B@}16@?120"
- "@48@0:8(tagNTP=Q{?=II})16{CGSize=dd}24I40C44"
- "T@\"VCAudioTransmitter\",&,V_audioTransmitter"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}},R,VaudioReceiver"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}16@0:8"
- "deviceShouldEnableLowPowerMode"
- "initWithClientIdentifier:audioFormat:transcriberResultDelegate:endpointingResultDelegate:languageDetectorResultDelegate:speechDetectorResultDelegate:queue:transcriberOptions:options:languageDetectorOptions:speechDetectorOptions:restrictedLogging:contextualNamedEntities:didChangeVolatileRange:"
- "initWithCreationTime:screenResolution:abSwitches:fecHeaderVersion:"
- "reportInitialThermalLevel"
- "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}16"
- "{?=\"ntpTime\"b1\"abSwitches\"b1\"fecHeaderVersion\"b1\"screenRes\"b1}"

```
