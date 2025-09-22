## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.62.1.2.0
-  __TEXT.__text: 0x793058
-  __TEXT.__auth_stubs: 0x5610
-  __TEXT.__objc_methlist: 0x359a8
-  __TEXT.__const: 0xc760
-  __TEXT.__cstring: 0x8f09e
-  __TEXT.__oslogstring: 0x10e79c
-  __TEXT.__gcc_except_tab: 0x2a80
+2175.9.2.0.0
+  __TEXT.__text: 0x796360
+  __TEXT.__auth_stubs: 0x5620
+  __TEXT.__objc_methlist: 0x35bc0
+  __TEXT.__const: 0xc780
+  __TEXT.__cstring: 0x8f509
+  __TEXT.__oslogstring: 0x10f1f7
+  __TEXT.__gcc_except_tab: 0x2aac
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10838
+  __TEXT.__unwind_info: 0x10898
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d880
-  __TEXT.__objc_methtype: 0x28278
-  __TEXT.__objc_stubs: 0x4ea40
-  __DATA_CONST.__got: 0x1a58
-  __DATA_CONST.__const: 0x6a50
+  __TEXT.__objc_methname: 0x7dda0
+  __TEXT.__objc_methtype: 0x282af
+  __TEXT.__objc_stubs: 0x4ee80
+  __DATA_CONST.__got: 0x1a60
+  __DATA_CONST.__const: 0x6b10
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16900
+  __DATA_CONST.__objc_selrefs: 0x169e8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b20
-  __AUTH_CONST.__const: 0x3c08
-  __AUTH_CONST.__cfstring: 0x26240
-  __AUTH_CONST.__objc_const: 0x633c0
-  __AUTH_CONST.__objc_intobj: 0x4968
-  __AUTH_CONST.__objc_arrayobj: 0x1b30
+  __AUTH_CONST.__auth_got: 0x2b28
+  __AUTH_CONST.__const: 0x3c88
+  __AUTH_CONST.__cfstring: 0x26400
+  __AUTH_CONST.__objc_const: 0x63770
+  __AUTH_CONST.__objc_intobj: 0x4a10
+  __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
-  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6c3c
+  __DATA.__objc_ivar: 0x6c90
   __DATA.__data: 0x78b0
-  __DATA.__bss: 0xd30
+  __DATA.__bss: 0xd78
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xa780
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BF52978D-0DD4-31FD-B6C2-2500A929ECEA
-  Functions: 31539
-  Symbols:   97272
-  CStrings:  57145
+  UUID: 8517BE3D-B554-3DDC-934E-BE1559312E5D
+  Functions: 31600
+  Symbols:   97446
+  CStrings:  57261
 
Symbols:
+ +[VCSessionMediaStreamConfigurationProvider addCodecConfigurationToStreamConfig:codecType:preferredMode:isV2Codec:]
+ +[VCSessionMediaStreamConfigurationProvider setUpCodecConfig:payload:preferredMode:]
+ +[VCSessionMediaStreamConfigurationProvider setUpV2CodecConfig:payload:preferredMode:]
+ -[AVCSession handleEndConfigurationOnParticipantAdd:]
+ -[VCAudioPayloadConfig acc24Bitrate]
+ -[VCAudioPayloadConfig createSupportedBitratesForACC24]
+ -[VCAudioPayloadConfig isACC24FixedBitrateModeEnabled]
+ -[VCAudioPayloadConfig setIsACC24FixedBitrateModeEnabled:]
+ -[VCAudioRuleCollection isACC24ForGFTEnabled]
+ -[VCAudioRuleCollection isACC24ForU1Enabled]
+ -[VCAudioRuleCollection setIsACC24ForGFTEnabled:]
+ -[VCAudioRuleCollection setIsACC24ForU1Enabled:]
+ -[VCAudioRuleCollectionConfiguration addACC24]
+ -[VCAudioRuleCollectionConfiguration setAddACC24:]
+ -[VCAudioStream getCodecConfigForPayload:streamConfig:]
+ -[VCAudioStream shouldStartTransportSessionBeforeStream]
+ -[VCAudioStream updateOperatingMode:]
+ -[VCAudioStreamCodecConfig isACC24FixedBitrateModeEnabled]
+ -[VCAudioStreamCodecConfig setIsACC24FixedBitrateModeEnabled:]
+ -[VCAudioStreamConfig externalSampleReblockingEnabled]
+ -[VCAudioStreamConfig isACC24ForGFTEnabled]
+ -[VCAudioStreamConfig isACC24ForU1Enabled]
+ -[VCAudioStreamConfig setExternalSampleReblockingEnabled:]
+ -[VCAudioStreamConfig setIsACC24ForGFTEnabled:]
+ -[VCAudioStreamConfig setIsACC24ForU1Enabled:]
+ -[VCAudioTierPicker addPayloadsFromGFTPayloadsArray:isACC24Supported:]
+ -[VCAudioTierPicker addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:isACC24Supported:]
+ -[VCAudioTierPicker setUpFeatureFlagToEnablementMapping]
+ -[VCAudioTierPicker setUpFeatureFlagToEnablementMapping].cold.1
+ -[VCAudioTransmitterConfig isACC24Enabled]
+ -[VCAudioTransmitterConfig setIsACC24Enabled:]
+ -[VCDefaults separateString:]
+ -[VCMediaNegotiatorLocalConfiguration enableACC24ForGFT]
+ -[VCMediaNegotiatorLocalConfiguration enableACC24ForU1]
+ -[VCMediaNegotiatorLocalConfiguration setEnableACC24ForGFT:]
+ -[VCMediaNegotiatorLocalConfiguration setEnableACC24ForU1:]
+ -[VCMediaNegotiatorResultsAudio enableACC24ForU1]
+ -[VCMediaNegotiatorResultsAudio initWithACC24ForU1Enabled:]
+ -[VCMediaNegotiatorResultsAudio setEnableACC24ForU1:]
+ -[VCMediaNegotiatorStreamGroupConfiguration enableACC24ForGFT]
+ -[VCMediaNegotiatorStreamGroupConfiguration setEnableACC24ForGFT:]
+ -[VCMediaNegotiatorStreamGroupU1Configuration enableACC24ForU1]
+ -[VCMediaNegotiatorStreamGroupU1Configuration setEnableACC24ForU1:]
+ -[VCMediaStream handleStartTransportSessionCompletionBlockDidSucceed:withError:]
+ -[VCMediaStream shouldStartTransportSessionBeforeStream]
+ -[VCMediaStream startTransportSessionWithCompletion:]
+ -[VCMediaStreamMultiwayConfigAudio enableACC24ForGFT]
+ -[VCMediaStreamMultiwayConfigAudio setEnableACC24ForGFT:]
+ -[VCMediaStreamReceiveGroup streamConfigForStreamID:]
+ -[VCSession reportInitialThermalLevel]
+ -[VCSessionParticipantConfig isACC24ForGFTEnabled]
+ -[VCSessionParticipantConfig isACC24ForU1Enabled]
+ -[VCSessionParticipantConfig setIsACC24ForGFTEnabled:]
+ -[VCSessionParticipantConfig setIsACC24ForU1Enabled:]
+ -[VCSessionParticipantRemote updateACC24ExperimentOverrides]
+ -[VCSessionParticipantRemote updateAndHandleVideoMediaStall:]
+ -[VCVirtualAVCaptureDevice setOutputAspectRatio:completionHandler:]
+ GCC_except_table101
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table195
+ GCC_except_table35
+ GCC_except_table99
+ _AVGQCB54MH3XAXNGTVD2SAMOV5WWOQ
+ _AVGestaltGetBoolAnswer
+ _OBJC_IVAR_$_VCAVFoundationCapture._memojiWithoutDepthEnabled
+ _OBJC_IVAR_$_VCAudioPayloadConfig._isACC24FixedBitrateModeEnabled
+ _OBJC_IVAR_$_VCAudioRuleCollection._isACC24ForGFTEnabled
+ _OBJC_IVAR_$_VCAudioRuleCollection._isACC24ForU1Enabled
+ _OBJC_IVAR_$_VCAudioRuleCollectionConfiguration._addACC24
+ _OBJC_IVAR_$_VCAudioStream._isACC24ForGFTEnabled
+ _OBJC_IVAR_$_VCAudioStream._isACC24ForU1Enabled
+ _OBJC_IVAR_$_VCAudioStreamCodecConfig._isACC24FixedBitrateModeEnabled
+ _OBJC_IVAR_$_VCAudioStreamConfig._externalSampleReblockingEnabled
+ _OBJC_IVAR_$_VCAudioStreamConfig._isACC24ForGFTEnabled
+ _OBJC_IVAR_$_VCAudioStreamConfig._isACC24ForU1Enabled
+ _OBJC_IVAR_$_VCAudioTierPicker._plistFeatureFlagToEnablementMapping
+ _OBJC_IVAR_$_VCAudioTransmitter._isACC24Enabled
+ _OBJC_IVAR_$_VCAudioTransmitterConfig._isACC24Enabled
+ _OBJC_IVAR_$_VCCoreAudio_AudioUnitMock._cycleCount
+ _OBJC_IVAR_$_VCCoreAudio_AudioUnitMock._startTime
+ _OBJC_IVAR_$_VCMediaNegotiatorLocalConfiguration._enableACC24ForGFT
+ _OBJC_IVAR_$_VCMediaNegotiatorLocalConfiguration._enableACC24ForU1
+ _OBJC_IVAR_$_VCMediaNegotiatorResultsAudio._enableACC24ForU1
+ _OBJC_IVAR_$_VCMediaNegotiatorStreamGroupConfiguration._enableACC24ForGFT
+ _OBJC_IVAR_$_VCMediaNegotiatorStreamGroupU1Configuration._enableACC24ForU1
+ _OBJC_IVAR_$_VCMediaStream._startTransportSessionCompletionBlock
+ _OBJC_IVAR_$_VCMediaStreamMultiwayConfigAudio._enableACC24ForGFT
+ _OBJC_IVAR_$_VCSessionParticipantConfig._isACC24ForGFTEnabled
+ _OBJC_IVAR_$_VCSessionParticipantConfig._isACC24ForU1Enabled
+ _SoundDec_Encode.cold.1
+ _SoundDec_Encode.cold.2
+ _SoundDec_Encode.cold.3
+ _SoundDec_Encode.cold.4
+ _VCAbTestEnableACC24FixedBitrateMode
+ _VCAbTestEnableACC24ForGFT
+ _VCAbTestEnableACC24ForU1
+ _VCDefaults_Prod_GetEyeContactEnabledBoolValue
+ _VCDefaults_Prod_GetUserPreferenceAFBDisabled
+ _VCFeatureFlagManager_AudioCodecACC24FixedBitrateMode
+ _VCFeatureFlagManager_AudioCodecACC24FixedBitrateMode.cold.1
+ _VCFeatureFlagManager_AudioCodecACC24FixedBitrateMode.flag
+ _VCFeatureFlagManager_AudioCodecACC24FixedBitrateMode.onceToken
+ _VCFeatureFlagManager_DetectInactiveAudioFramesACC24
+ _VCFeatureFlagManager_DetectInactiveAudioFramesACC24.cold.1
+ _VCFeatureFlagManager_DetectInactiveAudioFramesACC24.flag
+ _VCFeatureFlagManager_DetectInactiveAudioFramesACC24.onceToken
+ _VCFeatureFlagManager_UseAudioCodecACC24ForGFT
+ _VCFeatureFlagManager_UseAudioCodecACC24ForGFT.cold.1
+ _VCFeatureFlagManager_UseAudioCodecACC24ForGFT.isACC24Supported
+ _VCFeatureFlagManager_UseAudioCodecACC24ForGFT.onceToken
+ _VCFeatureFlagManager_UseAudioCodecACC24ForGFT.result
+ _VCFeatureFlagManager_UseAudioCodecACC24ForU1
+ _VCFeatureFlagManager_UseAudioCodecACC24ForU1.cold.1
+ _VCFeatureFlagManager_UseAudioCodecACC24ForU1.isACC24Supported
+ _VCFeatureFlagManager_UseAudioCodecACC24ForU1.onceToken
+ _VCFeatureFlagManager_UseAudioCodecACC24ForU1.result
+ _VCFeatureFlagManager_UseShortREDWithACC24
+ _VCFeatureFlagManager_UseShortREDWithACC24._result
+ _VCFeatureFlagManager_UseShortREDWithACC24.cold.1
+ _VCFeatureFlagManager_UseShortREDWithACC24.onceToken
+ _VCVideoAttributeOrientationToAggregatorOrientation
+ _VCVideoAttributeOrientationToAggregatorOrientation.cold.1
+ __OBJC_$_PROP_LIST_VCVideoCaptureServer.860
+ __VCAVFoundationCapture_AttachPropagatableAFB
+ __VCAudioReceiver_UnregisterTransportCallbacks
+ __VideoDecoder_ShouldSkipReleasingDecodingArgs
+ ___28-[VCSession dispatchedStart]_block_invoke.608
+ ___28-[VCSession dispatchedStart]_block_invoke.609
+ ___44-[VCMediaStream startWithCompletionHandler:]_block_invoke_2
+ ___44-[VCMediaStream startWithCompletionHandler:]_block_invoke_3
+ ___44-[VCMediaStream startWithCompletionHandler:]_block_invoke_3.cold.1
+ ___44-[VCMediaStream startWithCompletionHandler:]_block_invoke_4
+ ___45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.72
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.200
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.201
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.201.cold.1
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.603
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.604
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.605
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.621
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.620
+ ___53-[VCSessionParticipantRemote setOneToOneModeEnabled:]_block_invoke.179
+ ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.181
+ ___60-[VCSessionParticipantRemote updateRemoteDeviceOrientation:]_block_invoke.185
+ ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.234
+ ___67-[VCVirtualAVCaptureDevice setOutputAspectRatio:completionHandler:]_block_invoke
+ ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.293
+ ___69-[VCSession updateParticipantConfigurations:sessionPresentationInfo:]_block_invoke.349
+ ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.131
+ ___VCFeatureFlagManager_AudioCodecACC24FixedBitrateMode_block_invoke
+ ___VCFeatureFlagManager_DetectInactiveAudioFramesACC24_block_invoke
+ ___VCFeatureFlagManager_UseAudioCodecACC24ForGFT_block_invoke
+ ___VCFeatureFlagManager_UseAudioCodecACC24ForU1_block_invoke
+ ___VCFeatureFlagManager_UseShortREDWithACC24_block_invoke
+ ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.871
+ ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.873
+ ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.875
+ ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.865
+ ___block_descriptor_40_e8_32o_e25_v16?0?<v?B"NSError">8ls32l8
+ ___block_descriptor_49_e8_32o40b_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_57_e8_32o40b48b_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_tmp.170
+ ___block_literal_global.112
+ ___block_literal_global.124
+ ___block_literal_global.130
+ ___block_literal_global.136
+ ___block_literal_global.142
+ ___block_literal_global.148
+ ___block_literal_global.167
+ ___block_literal_global.171
+ ___block_literal_global.177
+ ___block_literal_global.190
+ ___block_literal_global.196
+ ___block_literal_global.202
+ ___block_literal_global.208
+ ___block_literal_global.220
+ ___block_literal_global.226
+ ___block_literal_global.232
+ ___block_literal_global.239
+ ___block_literal_global.244
+ ___block_literal_global.250
+ ___block_literal_global.407
+ ___block_literal_global.54
+ ___block_literal_global.60
+ ___block_literal_global.66
+ ___block_literal_global.72
+ ___block_literal_global.78
+ ___block_literal_global.92
+ _kVCAudioPayloadConfigKeyACC24FixedBitrateModeEnabled
+ _kVCExperimentEnableACC24FixedBitrateMode
+ _kVCExperimentEnableACC24ForGFT
+ _kVCExperimentEnableACC24ForU1
+ _objc_msgSend$acc24Bitrate
+ _objc_msgSend$addACC24
+ _objc_msgSend$addCodecConfigurationToStreamConfig:codecType:preferredMode:isV2Codec:
+ _objc_msgSend$addPayloadsFromGFTPayloadsArray:isACC24Supported:
+ _objc_msgSend$addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:isACC24Supported:
+ _objc_msgSend$createSupportedBitratesForACC24
+ _objc_msgSend$defaultDeviceWithMediaType:
+ _objc_msgSend$enableACC24ForGFT
+ _objc_msgSend$enableACC24ForU1
+ _objc_msgSend$externalSampleReblockingEnabled
+ _objc_msgSend$featureFlag
+ _objc_msgSend$getCodecConfigForPayload:streamConfig:
+ _objc_msgSend$handleEndConfigurationOnParticipantAdd:
+ _objc_msgSend$handleStartTransportSessionCompletionBlockDidSucceed:withError:
+ _objc_msgSend$initWithACC24ForU1Enabled:
+ _objc_msgSend$isACC24Enabled
+ _objc_msgSend$isACC24FixedBitrateModeEnabled
+ _objc_msgSend$isACC24ForGFTEnabled
+ _objc_msgSend$isACC24ForU1Enabled
+ _objc_msgSend$overrideExperimentGroup:forExperiment:
+ _objc_msgSend$payloadsVersion
+ _objc_msgSend$reportInitialThermalLevel
+ _objc_msgSend$separateString:
+ _objc_msgSend$setAddACC24:
+ _objc_msgSend$setEnableACC24ForGFT:
+ _objc_msgSend$setEnableACC24ForU1:
+ _objc_msgSend$setExternalSampleReblockingEnabled:
+ _objc_msgSend$setIsACC24Enabled:
+ _objc_msgSend$setIsACC24FixedBitrateModeEnabled:
+ _objc_msgSend$setIsACC24ForGFTEnabled:
+ _objc_msgSend$setIsACC24ForU1Enabled:
+ _objc_msgSend$setUpCodecConfig:payload:preferredMode:
+ _objc_msgSend$setUpFeatureFlagToEnablementMapping
+ _objc_msgSend$setUpV2CodecConfig:payload:preferredMode:
+ _objc_msgSend$setupLocalABTestSwitches
+ _objc_msgSend$setupLocalOnOffSwitches
+ _objc_msgSend$shouldStartTransportSessionBeforeStream
+ _objc_msgSend$startTransportSessionWithCompletion:
+ _objc_msgSend$updateACC24ExperimentOverrides
+ _objc_msgSend$updateAndHandleVideoMediaStall:
+ _reportingSetPeriodicAggregationOccurredHandler
- +[AVCCameraTestUtils findExpectedFramerate:forDevice:].cold.1
- +[VCSessionMediaStreamConfigurationProvider configureAudioStreams:withCodecConfiguration:payloadsVersion:].cold.1
- +[VCVideoCaptureServer backCameraSupportsFullBleedCapture]
- +[VCVideoCaptureServer cameraSupportsFullBleedCaptureWithFormatList:]
- +[VCVideoCaptureServer frontCameraSupportsFullBleedCapture]
- -[AVCMediaStreamNegotiatorSettingsImmersiveVideo dealloc]
- -[AVCMediaStreamNegotiatorSettingsiPadCompanion dealloc]
- -[VCAudioStream setOperatingMode:]
- -[VCAudioTierPicker addPayloadsFromGFTPayloadsArray:]
- -[VCAudioTierPicker addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:]
- -[VCDefaults seperateString:]
- -[VCMediaNegotiatorResultsAudio init]
- -[VCSessionParticipantRemote updateAndHandleVideoMediaStall:isOneToOneStream:]
- GCC_except_table100
- GCC_except_table107
- GCC_except_table194
- GCC_except_table60
- _OBJC_IVAR_$_AVCMediaStreamNegotiatorSettingsCompositorServicesStereoVideo._videoBufferDescription
- _OBJC_IVAR_$_AVCMediaStreamNegotiatorSettingsImmersiveVideo._videoBufferDescription
- _OBJC_IVAR_$_VCAVFoundationCapture._supportNoDepthMemoji
- _OBJC_IVAR_$_VCSessionParticipantRemote._oneToOneVideoEnabled
- _VCDefaults_GetEyeContactEnabledBoolValue
- _VideoDecoder_VTDecompressionCallback.cold.3
- _VideoDecoder_VTDecompressionCallback.cold.4
- __OBJC_$_PROP_LIST_VCVideoCaptureServer.863
- __SoundDec_HandleCodecModeRequest
- __SoundDec_HandleCodecModeRequest.cold.1
- __SoundDec_HandleCodecModeRequest.cold.2
- __SoundDec_HandleCodecModeRequest.cold.3
- __SoundDec_HandleCodecModeRequest.cold.4
- __SoundDec_SetEVSRFParams
- __VCAudioRecevier_UnregisterTransportCallbacks
- ___28-[VCSession dispatchedStart]_block_invoke.605
- ___28-[VCSession dispatchedStart]_block_invoke.606
- ___44-[VCMediaStream startWithCompletionHandler:]_block_invoke.cold.1
- ___45-[VCSessionParticipantRemote setAudioPaused:]_block_invoke.69
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.198
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.199
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.199.cold.1
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.597
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.601
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.602
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.618
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.617
- ___53-[VCSessionParticipantRemote setOneToOneModeEnabled:]_block_invoke.177
- ___54+[AVCCameraTestUtils findExpectedFramerate:forDevice:]_block_invoke
- ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.179
- ___59+[VCVideoCaptureServer frontCameraSupportsFullBleedCapture]_block_invoke
- ___60-[VCSessionParticipantRemote updateRemoteDeviceOrientation:]_block_invoke.180
- ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.232
- ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.290
- ___69-[VCSession updateParticipantConfigurations:sessionPresentationInfo:]_block_invoke.346
- ___81-[VCSessionParticipantRemote redundancyController:redundancyPercentageDidChange:]_block_invoke.127
- ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.874
- ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.876
- ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.878
- ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.868
- ___block_descriptor_tmp.169
- ___block_literal_global.103
- ___block_literal_global.109
- ___block_literal_global.115
- ___block_literal_global.121
- ___block_literal_global.140
- ___block_literal_global.144
- ___block_literal_global.150
- ___block_literal_global.163
- ___block_literal_global.169
- ___block_literal_global.175
- ___block_literal_global.181
- ___block_literal_global.187
- ___block_literal_global.193
- ___block_literal_global.199
- ___block_literal_global.205
- ___block_literal_global.211
- ___block_literal_global.217
- ___block_literal_global.223
- ___block_literal_global.404
- ___block_literal_global.62
- ___block_literal_global.71
- ___block_literal_global.84
- ___block_literal_global.91
- ___block_literal_global.97
- _findExpectedFramerate:forDevice:._exceptionDeviceFramerateDict
- _findExpectedFramerate:forDevice:.onceToken
- _frontCameraSupportsFullBleedCapture.cameraSupportsFullBleedCapture
- _frontCameraSupportsFullBleedCapture.onceToken
- _objc_msgSend$addPayloadsFromGFTPayloadsArray:
- _objc_msgSend$addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:
- _objc_msgSend$cameraSupportsFullBleedCaptureWithFormatList:
- _objc_msgSend$frontCameraSupportsFullBleedCapture
- _objc_msgSend$seperateString:
- _objc_msgSend$updateAndHandleVideoMediaStall:isOneToOneStream:
- _reportingSetPeriodicAggregationOccuredHandler
CStrings:
+ " [%s] %s:%d %@(%p) AVAudioSession=%@ applying pre-cached mute state=%{BOOL}d on initial setActive call"
+ " [%s] %s:%d %@(%p) Detected entryFeatureFlag=%@ which is NOT enabled. Skipping entry for bitrate=%ld with codecBitrate=%lu bundle=%lu RED=%lu"
+ " [%s] %s:%d %@(%p) Empty supported payload: device classType=%ld, decodeSupported=%d, encodeSupported=%d"
+ " [%s] %s:%d %@(%p) Failed to allocate plistFeatureFlagToEnablementMapping"
+ " [%s] %s:%d %@(%p) Failed to create bandwidth allocator array"
+ " [%s] %s:%d %@(%p) Failed to initialize audio stream group"
+ " [%s] %s:%d %@(%p) Failed to initialize video stream group"
+ " [%s] %s:%d %@(%p) Health Monitor for Video Stream Receive GroupID=%s StreamID[main:%u repair:%u] Video[%ukbps %4.1ffps] VideoResolution=%@ syncUpdateCalled=%ld videoDisplayLatency=%f activeStreamID=%@"
+ " [%s] %s:%d %@(%p) Peer subscribed streams update occurred while in OneToOne mode. Ignoring subscribed streams update now. Will re-apply subscribedStreams after switching to multiwayMode"
+ " [%s] %s:%d %@(%p) Timeout occurred while waiting for audio IO start!"
+ " [%s] %s:%d %@(%p) Timeout occurred while waiting for audio IO stop!"
+ " [%s] %s:%d %@(%p) Updating operatingMode in streamConfig.oneToOneOperatingMode=%d"
+ " [%s] %s:%d @=@ Health: VideoTransmitter streamID=%d, streamGroupId=%s, toBeBufferedFrameCount=%d, bufferedFrameCount=%d, encoderProcCount=%d, transmitterProcCount=%d toBeEncodedFrameCount=%d, encodedFullFrameCount=%d, encodedFullFrameRate=%f, encodedFrameCount=%d, encodedFrameRate=%f, transmittedFrameCount=%d, transmittedNonFECFrameCount=%d, singlePacketFrameCount=%d, currentMediaBitrate=%f, currentHeaderBitrate=%f, currentFECBitrate=%f, currentTotalBitrate=%f, currentFECOverhead=%2.4f targetBitrate=%d deltaKeyFramesSent=%d"
+ " [%s] %s:%d AVAudioSession=%@ applying pre-cached mute state=%{BOOL}d on initial setActive call"
+ " [%s] %s:%d Attempt to force ACC24 bitrate to unsupported value=%d. Using default=%d instead."
+ " [%s] %s:%d Decoder returned frame with RTPTimestamp=%u, showFrame=%d, streamID=%d, decoding-order=%llu, tileID=%llu"
+ " [%s] %s:%d Detected entryFeatureFlag=%@ which is NOT enabled. Skipping entry for bitrate=%ld with codecBitrate=%lu bundle=%lu RED=%lu"
+ " [%s] %s:%d Empty connection info passed"
+ " [%s] %s:%d Empty supported payload: device classType=%ld, decodeSupported=%d, encodeSupported=%d"
+ " [%s] %s:%d Empty supported payload: device classType=%ld, supportsMVHEVCDecode=%d"
+ " [%s] %s:%d Empty supported payload: device classType=%ld, vcpSupportsHEVCEncoder=%d"
+ " [%s] %s:%d Empty supported payload: supportsMVHEVCEncode=%d"
+ " [%s] %s:%d FaceTime user setting prefers to disable AFB"
+ " [%s] %s:%d Failed to allocate plistFeatureFlagToEnablementMapping"
+ " [%s] %s:%d Failed to create bandwidth allocator array"
+ " [%s] %s:%d Failed to initialize audio stream group"
+ " [%s] %s:%d Failed to initialize video stream group"
+ " [%s] %s:%d Found payload=%u entry in tier table, but the payload is not supported. Skipping entry for bitrate=%ld with codecBitrate=%lu bundle=%lu RED=%lu"
+ " [%s] %s:%d Health Monitor for Video Stream Receive GroupID=%s StreamID[main:%u repair:%u] Video[%ukbps %4.1ffps] VideoResolution=%@ syncUpdateCalled=%ld videoDisplayLatency=%f activeStreamID=%@"
+ " [%s] %s:%d Invalid pointer"
+ " [%s] %s:%d MLEnhancedStats dictionary attached without an enhancement mode"
+ " [%s] %s:%d Peer subscribed streams update occurred while in OneToOne mode. Ignoring subscribed streams update now. Will re-apply subscribedStreams after switching to multiwayMode"
+ " [%s] %s:%d Skipped applying VCAudioSessionProperty_ClientPID for processID=%d"
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d Timeout occurred while waiting for audio IO start!"
+ " [%s] %s:%d Timeout occurred while waiting for audio IO stop!"
+ " [%s] %s:%d Updating operatingMode in streamConfig.oneToOneOperatingMode=%d"
+ " [%s] %s:%d VCAudioTransmitter[%p] AudioTierPicker was reset. Current audioTier info from default tier: payload=%u audioCodecBitrate=%u redNumPayloads=%u packetsPerBundle=%u operatingMode=%d."
+ " [%s] %s:%d VCAudioTransmitter[%p] Setting tierPickerMode=%s. Resetting the audio tier picker"
+ " [%s] %s:%d VCAudioTransmitter[%p] Tier Table for operatingMode=%d and tierPickerMode=%d"
+ " [%s] %s:%d VCAudioTransmitter[%p] operatingMode changed to %s"
+ " [%s] %s:%d VCNAT64ResolverRegisterForPrefixUpdate: successfully registered context %08X on interface %s"
+ " [%s] %s:%d VCPDecompressionSession: Decoder returned a NULL frame for streamID=%d, showFrame=%d, RTPTimestamp=%u"
+ " [%s] %s:%d VCPDecompressionSession: Decoder returned a NULL frame with showFrame=%d, RTPTimestamp=%u, decoding-order=%llu, tileID=%llu"
+ " [%s] %s:%d VCVirtualAVCaptureDevice setOutputAspectRatio: aspectRatio=[%@] (mocked)"
+ " [%s] %s:%d Video effect toggled: keyPath=%@, value=%d"
+ " [%s] %s:%d [AVC SPATIAL AUDIO] Receiving presentation info: rect=[%f, %f, %f, %f] didplayID=%u layout=%d state=%u"
+ " [%s] %s:%d force ACC24 bitrate to preferredBitrate=%d"
+ " [%s] %s:%d invalid orientation=%d!"
+ " [%s] %s:%d isFrontCamera=%d, _effectsApplied=%d, _supportNoDepthMemoji=%d, _deviceSupportsTrueDepthSwitchForEffects=%d"
+ " [%s] %s:%d result=%d"
+ " [%s] %s:%d success streamToken=%u"
+ " isEnabledACC24InactiveFrameDetection=%d"
+ "%s \n"
+ "+[VCHardwareSettings supportsFrontCameraFullBleedCapture]"
+ "+[VCSessionMediaStreamConfigurationProvider addCodecConfigurationToStreamConfig:codecType:preferredMode:isV2Codec:]"
+ "-[VCAudioPayloadConfig acc24Bitrate]"
+ "-[VCAudioStream updateOperatingMode:]"
+ "-[VCAudioTierPicker addEntryMatchingPayloadToAudioTierMap:config:entry:bitrateTier:forcedPayload:]"
+ "-[VCAudioTierPicker setUpFeatureFlagToEnablementMapping]"
+ "-[VCHardwareSettingsEmbedded supportsFrontCameraFullBleedCapture]"
+ "-[VCMediaStream startWithCompletionHandler:]_block_invoke_3"
+ "-[VCSession reportInitialThermalLevel]"
+ "-[VCSessionParticipantRemote updateACC24ExperimentOverrides]"
+ "-[VCVirtualAVCaptureDevice setOutputAspectRatio:completionHandler:]"
+ "2175.9.2"
+ "@36@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}24I32"
+ "@72@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}16"
+ "ACC24"
+ "AUIO [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: System Audio Tap initialization failed(%X)"
+ "AudioCodecACC24FixedBitrateMode"
+ "B52@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}24@32@40i48"
+ "B56@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}24B32B36I40I44@48"
+ "B72@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}16"
+ "DetectInactiveAudioFramesACC24"
+ "ORTNLocal"
+ "ORTNRemote"
+ "TB,N,V_addACC24"
+ "TB,N,V_enableACC24ForGFT"
+ "TB,N,V_enableACC24ForU1"
+ "TB,N,V_externalSampleReblockingEnabled"
+ "TB,N,V_isACC24Enabled"
+ "TB,N,V_isACC24FixedBitrateModeEnabled"
+ "TB,N,V_isACC24ForGFTEnabled"
+ "TB,N,V_isACC24ForU1Enabled"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B},R,VaudioReceiver"
+ "T{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB},V_config"
+ "UseAudioCodecACC24ForGFT"
+ "UseAudioCodecACC24ForGFT=%d isOOPAudioDecodingEnabled=%d"
+ "UseAudioCodecACC24ForU1"
+ "UseAudioCodecACC24ForU1=%d isOOPAudioDecodingEnabled=%d"
+ "UseShortREDWithACC24"
+ "UseShortREDWithACC24=%d"
+ "VCAudioPlayer [%s] %s:%d Didn't decode any samples this cycle. Output buffer should compensate to return erased samples to caller. Moving up the inputSamplesTS to account for implicit erasure. originalInputSamplesTS=%u samples=%d sampleCount=%d"
+ "VCAudioPlayer [%s] %s:%d requiredTimestamp=%d samplesNeeded=%d sampleCount=%d"
+ "VCAudioPlayer [%s] %s:%d requiredTimestamp=%d selectedTimestamp=%d dtx=%{bool}d sequenceNumber=%hu decodedCount=%d samples=%d decodedSamples=%d"
+ "VCAudioStream [%s] %s:%d Setting audioTransmitterConfig.operatingMode=%d streamConfig.multiwayConfig.isOneToOne=%d streamConfig.oneToOneOperatingMode=%d _operatingMode=%d"
+ "VCAudioStream [%s] %s:%d Setting operatingMode and tierPickerMode on VCAudioTransmitter[%p] -> operatingMode=%s tierPickerMode=%s"
+ "VCAudioStream [%s] %s:%d operatingMode=%d based on audioStreamMode defaultConfig.audioStreamMode=%ld"
+ "VCFeatureFlagManager: AudioCodecACC24FixedBitrateMode=%d (feature flag=%d)"
+ "VCFeatureFlagManager: DetectInactiveAudioFramesACC24=%d (feature flag=%d)"
+ "VCMediaStream [%s] %s:%d @:@ VCMediaStream-onStart %@ (%p) streamToken=%d, operatingMode=%d, shouldStartTransportSessionBeforeStream=%d"
+ "VCMediaStreamCodecTypeACC24"
+ "VCSession [%s] %s:%d %@(%p) Reporting thermalLevel=%d as initial thermal level"
+ "VCSession [%s] %s:%d Reporting thermalLevel=%d as initial thermal level"
+ "VCSessionParticipantRemote [%s] %s:%d VCExperimentManager GFT override RTCReporting for experimentName=%@ value=%u result=%d"
+ "VCSessionParticipantRemote [%s] %s:%d VCExperimentManager U+1 override RTCReporting for experimentName=%@ value=%u result=%d"
+ "VCTextReceiver [%s] %s:%d Failed to initialize the text receiver thread"
+ "VCVideoAttributeOrientationToAggregatorOrientation"
+ "VideoPacketBuffer [%s] %s:%d Error! Missing initial frames, seq:%d"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdIdB{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}16@0:8"
+ "_SoundDec_AudioConverterInstantiationOptions"
+ "_VideoDecoder_ShouldSkipReleasingDecodingArgs"
+ "_addACC24"
+ "_cycleCount"
+ "_enableACC24ForGFT"
+ "_enableACC24ForU1"
+ "_externalSampleReblockingEnabled"
+ "_isACC24Enabled"
+ "_isACC24FixedBitrateModeEnabled"
+ "_isACC24ForGFTEnabled"
+ "_isACC24ForU1Enabled"
+ "_memojiWithoutDepthEnabled"
+ "_plistFeatureFlagToEnablementMapping"
+ "_startTransportSessionCompletionBlock"
+ "acc24Bitrate"
+ "addACC24"
+ "addCodecConfigurationToStreamConfig:codecType:preferredMode:isV2Codec:"
+ "addPayloadsFromGFTPayloadsArray:isACC24Supported:"
+ "addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:isACC24Supported:"
+ "audioReceivedPkts"
+ "createSupportedBitratesForACC24"
+ "defaultDeviceWithMediaType:"
+ "enableACC24FixedBitrateMode"
+ "enableACC24ForGFT"
+ "enableACC24ForU1"
+ "externalSampleReblockingEnabled"
+ "forceACC24FixedBitrate"
+ "getCodecConfigForPayload:streamConfig:"
+ "handleEndConfigurationOnParticipantAdd:"
+ "handleStartTransportSessionCompletionBlockDidSucceed:withError:"
+ "initWithACC24ForU1Enabled:"
+ "isACC24Enabled"
+ "isACC24FixedBitrateModeEnabled"
+ "isACC24ForGFTEnabled"
+ "isACC24ForU1Enabled"
+ "reportInitialThermalLevel"
+ "separateString:"
+ "setAddACC24:"
+ "setEnableACC24ForGFT:"
+ "setEnableACC24ForU1:"
+ "setExternalSampleReblockingEnabled:"
+ "setIsACC24Enabled:"
+ "setIsACC24FixedBitrateModeEnabled:"
+ "setIsACC24ForGFTEnabled:"
+ "setIsACC24ForU1Enabled:"
+ "setUpCodecConfig:payload:preferredMode:"
+ "setUpFeatureFlagToEnablementMapping"
+ "setUpV2CodecConfig:payload:preferredMode:"
+ "shouldStartTransportSessionBeforeStream"
+ "skipApplyingAudioSessionClientPID"
+ "startTransportSessionWithCompletion:"
+ "streamConfigForStreamID:"
+ "totalReceivedKBytes"
+ "updateACC24ExperimentOverrides"
+ "updateAndHandleVideoMediaStall:"
+ "userPreferTxAFBDisabled"
+ "v16@?0@?<v@?B@\"NSError\">8"
+ "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBBB}16"
+ "v24@0:8r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}16"
+ "v40@0:8@16q24i32B36"
+ "v40@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}24@32"
+ "v48@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}24@32B40B44"
+ "v72@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}16"
+ "vc-ab-testing-enable-ACC24-fixed-bitrate-mode"
+ "vc-ab-testing-use-audio-codec-ACC24-for-GFT"
+ "vc-ab-testing-use-audio-codec-ACC24-for-U1"
+ "vcAudioPayloadConfigKeyACC24FixedBitrateModeEnabled"
+ "videoReceivedPkts"
+ "{ %@ audioPayloads=%@ chosenAudioPayload=%@ chosenDTXPayload=%@ chosenRedPayloadType=%d packetsPerBundle=%d useRateControl=%s bundlingScheme=%d allowAudioSwitching=%s supportsAdaptation=%s operatingMode=%d isRedEnabled=%s transmitROC=%s ignoreSilence=%s useWifiTiers=%s qualityIndex=%d ramStadSRCEnabled=%s isHigherAudioREDCutoverU1Enabled=%s isACC24Enabled=%s }"
+ "{?=\"mode\"C\"supportedAudioPayloadConfigs\"^{__CFArray}\"supportedPacketsPerBundle\"^{__CFArray}\"supportedRedNumPayloads\"^{__CFArray}\"headerSize\"I\"usingCellular\"B\"isUseCaseWatchContinuity\"B\"defaultMaxCap\"I\"alwaysOnAudioRedundancyEnabled\"B\"cellularAllowRedLowBitratesEnabled\"B\"wifiAllowRedLowBitratesEnabled\"B\"isIPv4\"B\"isACC24Supported\"B}"
+ "{?=\"timeStamp\"S\"bandwidthEstimation\"S\"videoBurstLoss\"S\"videoReceivedPkts\"S\"audioBurstLoss\"S\"audioReceivedPkts\"S\"totalReceivedKBytes\"I\"receiveQueueTarget\"I\"queuingDelay\"I\"sendTimestamp\"S\"owrd\"I\"connectionStatsBuffer\"I\"ecnECT1Count\"S\"ecnCECount\"S}"
+ "{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBBB}16@0:8"
- " [%s] %s:%d %@(%p) AVAudioSession=%@ applying pre-cached mute state=%{BOOL}d on inital setActive call"
- " [%s] %s:%d %@(%p) Empty suppported payload: device classType=%ld, decodeSupported=%d, encodeSupported=%d"
- " [%s] %s:%d %@(%p) Failed to create bandwith allocator array"
- " [%s] %s:%d %@(%p) Failed to initalize audio stream group"
- " [%s] %s:%d %@(%p) Failed to initalize video stream group"
- " [%s] %s:%d %@(%p) Health Monitor for Video Stream Receive GroupID=%s StreamID[main:%u repair:%u] Video[%ukbps %4.1ffps] VideoResolution=%@ syncUpdateCalled=%ld videoDisplayLatency=%f"
- " [%s] %s:%d %@(%p) Peer subscribed streams update occured while in OneToOne mode. Ignoring subscribed streams update now. Will re-apply subscribedStreams after switching to multiwayMode"
- " [%s] %s:%d %@(%p) Timeout occured while waiting for audio IO start!"
- " [%s] %s:%d %@(%p) Timeout occured while waiting for audio IO stop!"
- " [%s] %s:%d @=@ Health: VideoTransmitter streamID=%d, toBeBufferedFrameCount=%d, bufferedFrameCount=%d, encoderProcCount=%d, transmitterProcCount=%d toBeEncodedFrameCount=%d, encodedFullFrameCount=%d, encodedFullFrameRate=%f, encodedFrameCount=%d, encodedFrameRate=%f, transmittedFrameCount=%d, transmittedNonFECFrameCount=%d, singlePacketFrameCount=%d, currentMediaBitrate=%f, currentHeaderBitrate=%f, currentFECBitrate=%f, currentTotalBitrate=%f, currentFECOverhead=%2.4f targetBitrate=%d deltaKeyFramesSent=%d"
- " [%s] %s:%d AVAudioSession=%@ applying pre-cached mute state=%{BOOL}d on inital setActive call"
- " [%s] %s:%d AudioTierPicker was reset. Current audioTier info from default tier: payload=%u audioCodecBitrate=%u redNumPayloads=%u packetsPerBundle=%u."
- " [%s] %s:%d Decoder returned frame with RTPTimestamp=%u, showFrame %d, streamID %d, decoding order %llu, tileID %llu"
- " [%s] %s:%d Empty connnection info passed"
- " [%s] %s:%d Empty suppported payload: device classType=%ld, decodeSupported=%d, encodeSupported=%d"
- " [%s] %s:%d Empty suppported payload: device classType=%ld, supportsMVHEVCDecode=%d"
- " [%s] %s:%d Empty suppported payload: device classType=%ld, vcpSupportsHEVCEncoder=%d"
- " [%s] %s:%d Empty suppported payload: supportsMVHEVCEncode=%d"
- " [%s] %s:%d Failed to create bandwith allocator array"
- " [%s] %s:%d Failed to initalize audio stream group"
- " [%s] %s:%d Failed to initalize video stream group"
- " [%s] %s:%d Health Monitor for Video Stream Receive GroupID=%s StreamID[main:%u repair:%u] Video[%ukbps %4.1ffps] VideoResolution=%@ syncUpdateCalled=%ld videoDisplayLatency=%f"
- " [%s] %s:%d Invalid poitner"
- " [%s] %s:%d Peer subscribed streams update occured while in OneToOne mode. Ignoring subscribed streams update now. Will re-apply subscribedStreams after switching to multiwayMode"
- " [%s] %s:%d Setting tierPickerMode=%s. Resetting the audio tier picker"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- " [%s] %s:%d Tier Table for Operating Mode %d"
- " [%s] %s:%d Timeout occured while waiting for audio IO start!"
- " [%s] %s:%d Timeout occured while waiting for audio IO stop!"
- " [%s] %s:%d VCNAT64ResolverRegisterForPrefixUpdate: succesfully registered context %08X on interface %s"
- " [%s] %s:%d VCPDecompressionSession Error: Decoder returned a NULL frame for stream %d, showFrame %d, RTPTimestamp=%u"
- " [%s] %s:%d VCPDecompressionSession Error: Decoder returned a NULL frame with showFrame %d, RTPTimestamp=%u, decoding order %llu, tileID %llu"
- " [%s] %s:%d [AVC SPATIAL AUDIO] Receivieng presentation info: rect=[%f, %f, %f, %f] didplayID=%u layout=%d state=%u"
- " [%s] %s:%d isFrontCamera=%d, _effectsApplied=%d, _supportNoDepthMemoji=%d, _frontCameraSupportsFullBleedCapture=%d"
- " [%s] %s:%d keyPath=%@, value=%d"
- " [%s] %s:%d operatingMode changed to %s"
- " [%s] %s:%d sucess streamToken=%u"
- "+[VCSessionMediaStreamConfigurationProvider configureAudioStreams:withCodecConfiguration:payloadsVersion:]"
- "+[VCVideoCaptureServer frontCameraSupportsFullBleedCapture]"
- "-[VCAudioStream setOperatingMode:]"
- "-[VCSessionParticipantRemote updateAndHandleVideoMediaStall:isOneToOneStream:]"
- "2145.62.1.2"
- "@36@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}24I32"
- "@64@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}16"
- "AUIO [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: System Audio Tap initalization failed(%X)"
- "B52@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}24@32@40i48"
- "B56@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}24B32B36I40I44@48"
- "B64@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}16"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B},R,VaudioReceiver"
- "T{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB},V_config"
- "VCAudioPlayer [%s] %s:%d Decode : RequiredTimeStamp[%d] SelectedTimeStamp[%d] DTX[%d] seq[%d]"
- "VCAudioStream [%s] %s:%d operatingMode=%s tierPickerMode=%s"
- "VCMediaStream [%s] %s:%d @:@ VCMediaStream-onStart %@ (%p) streamToken=%d, operatingMode=%d"
- "VCSessionParticipantRemote [%s] %s:%d We are experiencing a video stall too soon after we switch video on. Ignoring... currentTime=%f lastVideoExpectationSwitch=%f diff=%f"
- "VCTextReceiver [%s] %s:%d Failed to initalize the text receiver thread"
- "VCVideoCaptureServer [%s] %s:%d [FrontCamera] cameraSupportsFullBleedCapture=%d"
- "VideoPacketBuffer [%s] %s:%d Error! Missing inital frames, seq:%d"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}B}16@0:8"
- "_oneToOneVideoEnabled"
- "_supportNoDepthMemoji"
- "addPayloadsFromGFTPayloadsArray:"
- "addPayloadsFromGFTRedNumPayloadsDict:isDeviceClassWolf:"
- "audioReceviedPkts"
- "backCameraSupportsFullBleedCapture"
- "bandwithEstimation"
- "cameraSupportsFullBleedCaptureWithFormatList:"
- "frontCameraSupportsFullBleedCapture"
- "iPad7,11"
- "iPad7,12"
- "iPad7,5"
- "iPad7,6"
- "seperateString:"
- "totalReceviedKBytes"
- "updateAndHandleVideoMediaStall:isOneToOneStream:"
- "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBBB}16"
- "v24@0:8r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}16"
- "v40@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}24@32"
- "v48@0:8@16r^{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}24@32B40B44"
- "v64@0:8{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}16"
- "videoReceviedPkts"
- "{ %@ audioPayloads=%@ chosenAudioPayload=%@ chosenDTXPayload=%@ chosenRedPayloadType=%d packetsPerBundle=%d useRateControl=%s bundlingScheme=%d allowAudioSwitching=%s supportsAdaptation=%s operatingMode=%d isRedEnabled=%s transmitROC=%s ignoreSilence=%s useWifiTiers=%s qualityIndex=%d ramStadSRCEnabled=%s isHigherAudioREDCutoverU1Enabled=%s }"
- "{?=\"mode\"C\"supportedAudioPayloadConfigs\"^{__CFArray}\"supportedPacketsPerBundle\"^{__CFArray}\"supportedRedNumPayloads\"^{__CFArray}\"headerSize\"I\"usingCellular\"B\"isUseCaseWatchContinuity\"B\"defaultMaxCap\"I\"alwaysOnAudioRedundancyEnabled\"B\"cellularAllowRedLowBitratesEnabled\"B\"wifiAllowRedLowBitratesEnabled\"B\"isIPv4\"B}"
- "{?=\"timeStamp\"S\"bandwithEstimation\"S\"videoBurstLoss\"S\"videoReceviedPkts\"S\"audioBurstLoss\"S\"audioReceviedPkts\"S\"totalReceivedKBytes\"I\"receiveQueueTarget\"I\"queuingDelay\"I\"sendTimestamp\"S\"owrd\"I\"connectionStatsBuffer\"I\"ecnECT1Count\"S\"ecnCECount\"S}"
- "{?=C^{__CFArray}^{__CFArray}^{__CFArray}IBBIBBBB}16@0:8"

```
