## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference`

```diff

-2055.53.1.0.0
-  __TEXT.__text: 0x69f1d4
+2055.56.1.0.0
+  __TEXT.__text: 0x6a53c0
   __TEXT.__auth_stubs: 0x4e30
-  __TEXT.__objc_methlist: 0x2cbb8
-  __TEXT.__const: 0x13c08
-  __TEXT.__cstring: 0x7b1df
-  __TEXT.__oslogstring: 0xeebdb
-  __TEXT.__gcc_except_tab: 0x2824
+  __TEXT.__objc_methlist: 0x2ce08
+  __TEXT.__const: 0x13c58
+  __TEXT.__cstring: 0x7b947
+  __TEXT.__oslogstring: 0xefa5e
+  __TEXT.__gcc_except_tab: 0x2864
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd0f0
-  __TEXT.__objc_classname: 0x4728
-  __TEXT.__objc_methname: 0x6f5b9
-  __TEXT.__objc_methtype: 0x2400c
-  __TEXT.__objc_stubs: 0x45ae0
-  __DATA_CONST.__got: 0x14d8
-  __DATA_CONST.__const: 0x3070
-  __DATA_CONST.__objc_classlist: 0x1160
+  __TEXT.__unwind_info: 0xd170
+  __TEXT.__objc_classname: 0x475f
+  __TEXT.__objc_methname: 0x6fa13
+  __TEXT.__objc_methtype: 0x24093
+  __TEXT.__objc_stubs: 0x45e60
+  __DATA_CONST.__got: 0x14e0
+  __DATA_CONST.__const: 0x3098
+  __DATA_CONST.__objc_classlist: 0x1168
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x438
+  __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x140d0
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xf78
+  __DATA_CONST.__objc_selrefs: 0x141b8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0xf80
   __DATA_CONST.__objc_arraydata: 0x2040
   __AUTH_CONST.__auth_got: 0x2730
   __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__const: 0x6c28
-  __AUTH_CONST.__cfstring: 0x21660
-  __AUTH_CONST.__objc_const: 0x60120
-  __AUTH_CONST.__objc_intobj: 0x3f90
+  __AUTH_CONST.__const: 0x6c88
+  __AUTH_CONST.__cfstring: 0x21820
+  __AUTH_CONST.__objc_const: 0x603b8
+  __AUTH_CONST.__objc_intobj: 0x3ff0
   __AUTH_CONST.__objc_arrayobj: 0x16f8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH.__objc_data: 0x9a10
+  __AUTH.__objc_data: 0x9a60
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x6268
-  __DATA.__data: 0x7470
-  __DATA.__bss: 0xbc0
+  __DATA.__objc_ivar: 0x6298
+  __DATA.__data: 0x74d0
+  __DATA.__bss: 0xbd8
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__data: 0x4c
-  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27525
-  Symbols:   53531
-  CStrings:  12986
+  Functions: 27594
+  Symbols:   53668
+  CStrings:  13028
 
Symbols:
+ +[AVCMomentsRequest invalidDelegateInstanceError]
+ +[VCAudioSmartRoutingManager addClient:]
+ +[VCAudioSmartRoutingManager removeClient:]
+ +[VCAudioSmartRoutingManager sharedInstance]
+ +[VCCannedAudioInjector defaultReaderOutputSettings]
+ +[VCCellularAudioTap stringFromTapType:]
+ +[VCHardwareSettings supportsDecodingSquareCameraVideo]
+ -[AVCBasebandAudioTap cleanUpPowerSpectrumMeter]
+ -[AVCBasebandAudioTap delegate]
+ -[AVCBasebandAudioTap dispatchedDelegate]
+ -[AVCBasebandAudioTap init].cold.3
+ -[AVCBasebandAudioTap meterServerDidDisconnect:]
+ -[AVCBasebandAudioTap setDelegate:]
+ -[AVCBasebandAudioTap setUpPowerSpectrumMeter]
+ -[AVCBasebandAudioTapRegistrationResult description]
+ -[VCAnsweringMachine dispatchQueue]
+ -[VCAnsweringMachine setDispatchQueue:]
+ -[VCAudioIOControllerClient optOutOfSmartRouting]
+ -[VCAudioIOControllerClient setOptOutOfSmartRouting:]
+ -[VCAudioSmartRoutingManager addClient:]
+ -[VCAudioSmartRoutingManager addClient:].cold.1
+ -[VCAudioSmartRoutingManager applyAudioScoreForOptOutOfSmartRouting:error:]
+ -[VCAudioSmartRoutingManager dealloc]
+ -[VCAudioSmartRoutingManager init]
+ -[VCAudioSmartRoutingManager removeClient:]
+ -[VCAudioSmartRoutingManager removeClient:].cold.1
+ -[VCAudioSmartRoutingManager updateOptOutOfSmartRouting]
+ -[VCAudioStream cleanUpCaptionsCoordinators]
+ -[VCAudioStream cleanUpMediaRecorder]
+ -[VCAudioStream setUpMediaRecorder]
+ -[VCAudioStream setUpMediaRecorder].cold.1
+ -[VCAudioStream setupCaptionsCoordinatorsWithFormat:]
+ -[VCAudioStream setupCaptionsCoordinatorsWithFormat:].cold.1
+ -[VCAudioTransmitter isStandaloneStreamMode]
+ -[VCCellularAudioTap cleanUpCaptionsCoordinator]
+ -[VCCellularAudioTap cleanUpMediaRecorder]
+ -[VCCellularAudioTap cleanUpPeriodicReporting]
+ -[VCCellularAudioTap clientSpecificUserInfo]
+ -[VCCellularAudioTap handleThermalPressureNotification:]
+ -[VCCellularAudioTap printAudioTapHealth]
+ -[VCCellularAudioTap registerForThermalNotifications]
+ -[VCCellularAudioTap setUpCallRecordingComponents]
+ -[VCCellularAudioTap setUpCaptionsCoordinator]
+ -[VCCellularAudioTap setUpCaptionsCoordinator].cold.1
+ -[VCCellularAudioTap setUpMediaRecorder]
+ -[VCCellularAudioTap setUpMediaRecorder].cold.1
+ -[VCCellularAudioTap setUpPeriodicReporting]
+ -[VCCellularAudioTap setUpReportingAgent]
+ -[VCCellularAudioTap setUpReportingAgent].cold.1
+ -[VCCellularAudioTap unregisterForThermalNotifications]
+ -[VCCellularAudioTapIO mediaRecorder]
+ -[VCCellularAudioTapIO setMediaRecorder:]
+ -[VCHardwareSettingsEmbedded supportsDecodingSquareCameraVideo]
+ -[VCHardwareSettingsMac supportsDecodingSquareCameraVideo]
+ -[VCVideoCaptureServer populateThermalFrameRateThresholdsForCaptureSourceID:captureConfig:]
+ -[VCVideoCaptureServer screenFrameRateForThermalLevel:configuredFrameRate:captureSourceID:]
+ -[VCVideoCaptureServer setScreenCaptureFrameRate:captureSourceID:]
+ -[VCVideoStreamReceiver createDecodeSession:].cold.1
+ -[VCVideoStreamReceiver createDecodeSession:].cold.2
+ -[VCVideoStreamReceiver decodeFrame:showFrame:].cold.1
+ GCC_except_table124
+ GCC_except_table149
+ GCC_except_table180
+ GCC_except_table220
+ GCC_except_table44
+ OBJC_IVAR_$_AVCBasebandAudioTap._delegateQueue
+ OBJC_IVAR_$_AVCBasebandAudioTap._weakDelegate
+ OBJC_IVAR_$_AVCMomentsRequest._weakDelegate
+ OBJC_IVAR_$_VCAudioIOControllerClient._optOutOfSmartRouting
+ OBJC_IVAR_$_VCAudioSmartRoutingManager._optOutOfSmartRouting
+ OBJC_IVAR_$_VCAudioStream._captionsCoordinator
+ OBJC_IVAR_$_VCAudioStream._captionsFormat
+ OBJC_IVAR_$_VCAudioStream._isCaptionsFormatValid
+ OBJC_IVAR_$_VCAudioStream._mediaRecorder
+ OBJC_IVAR_$_VCAudioStream._shouldSetUpCaptions
+ OBJC_IVAR_$_VCCellularAudioTap._captionsCoordinator
+ OBJC_IVAR_$_VCCellularAudioTap._mediaRecorder
+ OBJC_IVAR_$_VCVideoCaptureServer._screenCaptureThermalFrameRateThresholds
+ VCAudioBufferList_SetSilenceInQueue.cold.1
+ VCFeatureFlagManager_CallRecordingEnabled.flag
+ VCFeatureFlagManager_CallRecordingEnabled.onceToken
+ _JitterQueue_QueueEmptyOrAllDTX
+ _OBJC_$_PROP_LIST_VCVideoCaptureServer.807
+ _OBJC_CLASS_$_AVAudioSession
+ _OBJC_CLASS_$_VCAudioSmartRoutingManager
+ _OBJC_METACLASS_$_VCAudioSmartRoutingManager
+ _RTCPTransport_ParsePacket.cold.14
+ _VCAudioBufferList_SetSilenceInQueue
+ _VCFeatureFlagManager_CallRecordingEnabled
+ _VCVideoSourceConfig_CaptureFrameRateThermalLevelHeavy
+ _VCVideoSourceConfig_CaptureFrameRateThermalLevelModerate
+ __28-[VCVideoCaptureServer init]_block_invoke.35
+ __28-[VCVideoCaptureServer init]_block_invoke.39
+ __35-[VCVideoStream updateVideoConfig:]_block_invoke.155
+ __36-[VCVideoCaptureServer pausePreview]_block_invoke.389
+ __36-[VCVideoStream setupReportingAgent]_block_invoke.214
+ __41-[VCCellularAudioTap setUpReportingAgent]_block_invoke.cold.1
+ __46-[VCVideoCaptureServer setFollowSystemCamera:]_block_invoke.266
+ __47-[AVCBasebandAudioTap registerForTapWithError:]_block_invoke.cold.3
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.101
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.114
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.122
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.122.cold.1
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.122.cold.2
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.122.cold.3
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.129
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.66
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.68
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.86
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.86.cold.1
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.91
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.91.cold.1
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.96
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.97
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_2.131
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_3.133
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_4.135
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_5.137
+ __48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.344
+ __48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.348
+ __49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.350
+ __49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.354
+ __49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.418
+ __51-[VCVideoCaptureServer handleAVCaptureError:error:]_block_invoke.181
+ __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.206
+ __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.215
+ __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.228
+ __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.240
+ __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke_2.231
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.209
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.228
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.230
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.237
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.244
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.251
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.255
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.259
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.264
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.264.cold.1
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.269
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.269.cold.1
+ __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.274
+ __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.119
+ __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.124
+ __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.124.cold.1
+ __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.130
+ __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.133
+ __66-[VCVideoCaptureServer setScreenCaptureFrameRate:captureSourceID:]_block_invoke.cold.1
+ __66-[VCVideoCaptureServer setScreenCaptureFrameRate:captureSourceID:]_block_invoke.cold.2
+ __70-[VCVideoCaptureServer registerForVideoFramesFromSource:sourceConfig:]_block_invoke.312
+ __OBJC_$_CLASS_METHODS_AVCMomentsRequest
+ __OBJC_$_CLASS_METHODS_VCAudioSmartRoutingManager
+ __OBJC_$_INSTANCE_METHODS_VCAudioSmartRoutingManager
+ __OBJC_$_INSTANCE_VARIABLES_VCAudioSmartRoutingManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVCBasebandAudioTapDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCBasebandAudioTapDelegate
+ __OBJC_$_PROTOCOL_REFS_AVCBasebandAudioTapDelegate
+ __OBJC_CLASS_RO_$_VCAudioSmartRoutingManager
+ __OBJC_LABEL_PROTOCOL_$_AVCBasebandAudioTapDelegate
+ __OBJC_METACLASS_RO_$_VCAudioSmartRoutingManager
+ __OBJC_PROTOCOL_$_AVCBasebandAudioTapDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_AVCAudioPowerSpectrumMeterDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_AVCBasebandAudioTapDelegate
+ __VCVideoCaptureServer_ApplyPressureLevelChanges_block_invoke.271
+ ___31-[AVCBasebandAudioTap delegate]_block_invoke
+ ___35-[AVCBasebandAudioTap setDelegate:]_block_invoke
+ ___41-[VCCellularAudioTap printAudioTapHealth]_block_invoke
+ ___41-[VCCellularAudioTap setUpReportingAgent]_block_invoke
+ ___44+[VCAudioSmartRoutingManager sharedInstance]_block_invoke
+ ___44-[VCCellularAudioTap setUpPeriodicReporting]_block_invoke
+ ___45-[VCAudioCaptionsCoordinator enableCaptions:]_block_invoke
+ ___48-[AVCBasebandAudioTap meterServerDidDisconnect:]_block_invoke
+ ___60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke_2
+ ___66-[VCVideoCaptureServer setScreenCaptureFrameRate:captureSourceID:]_block_invoke
+ ___VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.236
+ ___VCFeatureFlagManager_CallRecordingEnabled_block_invoke
+ ___VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.815
+ ___VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.817
+ ___VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.812
+ ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.829
+ ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.834
+ __block_descriptor_tmp.420
+ __block_descriptor_tmp.469
+ __block_descriptor_tmp.471
+ __block_literal_global.393
+ _objc_msgSend$applyAudioScoreForOptOutOfSmartRouting:error:
+ _objc_msgSend$cleanUpCaptionsCoordinator
+ _objc_msgSend$cleanUpCaptionsCoordinators
+ _objc_msgSend$cleanUpMediaRecorder
+ _objc_msgSend$cleanUpPeriodicReporting
+ _objc_msgSend$cleanUpPowerSpectrumMeter
+ _objc_msgSend$defaultReaderOutputSettings
+ _objc_msgSend$dispatchedDelegate
+ _objc_msgSend$invalidDelegateInstanceError
+ _objc_msgSend$isStandaloneStreamMode
+ _objc_msgSend$optOutOfSmartRouting
+ _objc_msgSend$populateThermalFrameRateThresholdsForCaptureSourceID:captureConfig:
+ _objc_msgSend$printAudioTapHealth
+ _objc_msgSend$screenFrameRateForThermalLevel:configuredFrameRate:captureSourceID:
+ _objc_msgSend$serverDidDisconnectForTap:
+ _objc_msgSend$setOptOutOfSmartRouting:
+ _objc_msgSend$setPreferredOutputAudioScoreForSmartRouting:error:
+ _objc_msgSend$setPreparesMediaDataForRealTimeConsumption:
+ _objc_msgSend$setScreenCaptureFrameRate:captureSourceID:
+ _objc_msgSend$setUpCallRecordingComponents
+ _objc_msgSend$setUpCaptions
+ _objc_msgSend$setUpCaptionsCoordinator
+ _objc_msgSend$setUpMediaRecorder
+ _objc_msgSend$setUpPeriodicReporting
+ _objc_msgSend$setUpPowerSpectrumMeter
+ _objc_msgSend$setupCaptionsCoordinatorsWithFormat:
+ _objc_msgSend$stringFromTapType:
+ _objc_msgSend$supportsDecodingSquareCameraVideo
+ _objc_msgSend$updateOptOutOfSmartRouting
+ sharedInstance._sharedSmartRoutingManager
- +[VCCannedAudioInjector setupReader:forAsset:assetAudioFormat:trackOutput:].cold.2
- +[VCCannedAudioInjector setupReader:forAsset:assetAudioFormat:trackOutput:].cold.3
- +[VCCannedAudioInjector setupReader:forAsset:assetAudioFormat:trackOutput:].cold.4
- +[VCCannedAudioInjector setupReader:forAsset:assetAudioFormat:trackOutput:].cold.5
- +[VCHardwareSettings supportsCameraDecodeSquare]
- -[VCHardwareSettingsEmbedded supportsCameraDecodeSquare]
- -[VCHardwareSettingsMac supportsCameraDecodeSquare]
- GCC_except_table105
- GCC_except_table147
- GCC_except_table177
- GCC_except_table217
- GCC_except_table43
- OBJC_IVAR_$_AVCMomentsRequest._delegate
- _OBJC_$_PROP_LIST_VCVideoCaptureServer.796
- __28-[VCVideoCaptureServer init]_block_invoke.32
- __28-[VCVideoCaptureServer init]_block_invoke.36
- __35-[VCVideoStream updateVideoConfig:]_block_invoke.151
- __36-[VCVideoCaptureServer pausePreview]_block_invoke.384
- __36-[VCVideoStream setupReportingAgent]_block_invoke.210
- __46-[VCVideoCaptureServer setFollowSystemCamera:]_block_invoke.260
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.111
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.119
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.119.cold.1
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.119.cold.2
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.119.cold.3
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.126
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.63
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.65
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.83
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.83.cold.1
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.88
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.88.cold.1
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.93
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.94
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke.98
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_2.128
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_3.130
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_4.132
- __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_5.134
- __48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.339
- __48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.343
- __49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.345
- __49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.349
- __49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.413
- __51-[VCVideoCaptureServer handleAVCaptureError:error:]_block_invoke.178
- __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.203
- __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.212
- __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.225
- __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.237
- __51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke_2.228
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.203
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.222
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.224
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.231
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.238
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.245
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.247
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.249
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.258
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.258.cold.1
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.263
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.263.cold.1
- __56-[AVCAudioStream registerBlocksForDelegateNotifications]_block_invoke.268
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.67
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.72
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.72.cold.1
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.79
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.81
- __60-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke.84
- __70-[VCVideoCaptureServer registerForVideoFramesFromSource:sourceConfig:]_block_invoke.307
- __VCVideoCaptureServer_ApplyPressureLevelChanges_block_invoke.265
- ___29-[VCAnsweringMachine dealloc]_block_invoke
- ___50-[VCVideoCaptureServer setScreenCaptureFrameRate:]_block_invoke
- ___VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.232
- ___VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.804
- ___VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.806
- ___VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.801
- ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.825
- ___VCVideoStream_DidReceiveRemoteFrame_block_invoke.830
- __block_descriptor_tmp.417
- __block_descriptor_tmp.466
- __block_descriptor_tmp.468
- _objc_msgSend$supportsCameraDecodeSquare
CStrings:
+ "%!s(MISSING)(%!p(MISSING)) Failed to get audio track from tracks=%!s(MISSING) asset=%!s(MISSING)"
+ "%!s(MISSING)(%!p(MISSING)) Instantiation of AVAssetReaderTrackOutput for track=%!s(MISSING) with settings=%!s(MISSING) failed for asset=%!s(MISSING)"
+ "%!s(MISSING)(%!u(MISSING))"
+ "+[VCAudioSmartRoutingManager sharedInstance]_block_invoke"
+ "-[AVCAudioPowerSpectrumMeter registerBlocksForNotifications]_block_invoke_2"
+ "-[AVCBasebandAudioTap registerForTapWithError:]"
+ "-[AVCBasebandAudioTap setDelegate:]"
+ "-[AVCBasebandAudioTap unregisterFromTapWithError:]"
+ "-[VCAudioSmartRoutingManager addClient:]"
+ "-[VCAudioSmartRoutingManager applyAudioScoreForOptOutOfSmartRouting:error:]"
+ "-[VCAudioSmartRoutingManager removeClient:]"
+ "-[VCAudioSmartRoutingManager updateOptOutOfSmartRouting]"
+ "-[VCAudioStream setUpMediaRecorder]"
+ "-[VCAudioStream setupCaptionsCoordinatorsWithFormat:]"
+ "-[VCCellularAudioTap printAudioTapHealth]_block_invoke"
+ "-[VCCellularAudioTap setUpCallRecordingComponents]"
+ "-[VCCellularAudioTap setUpCaptionsCoordinator]"
+ "-[VCCellularAudioTap setUpMediaRecorder]"
+ "-[VCCellularAudioTap setUpReportingAgent]"
+ "-[VCCellularAudioTap setUpReportingAgent]_block_invoke"
+ "-[VCVideoCaptureServer screenFrameRateForThermalLevel:configuredFrameRate:captureSourceID:]"
+ "-[VCVideoCaptureServer setScreenCaptureFrameRate:captureSourceID:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCAudioStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCQoSMonitor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSessionParticipant.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCVideoStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVConference.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptions.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioTransmitter.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSessionCategories.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCaptionsStreamSendGroup.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamGroup.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamTransport.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+Messaging.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipant.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipantLocal.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTextStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoCaptureServer.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConference.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AVConference/Common/VCMediaDevice.m"
+ "2055.56.1"
+ "Attempting to invoke on request with no valid parent class"
+ "CallRecording"
+ "CaptureThermalLevelHeavy"
+ "CaptureThermalLevelModerate"
+ "CurrentFrameRate"
+ "Downlink"
+ "Failed to get audio track from tracks=%!s(MISSING) asset=%!s(MISSING)"
+ "Failed to set up XPC connection for AVCBasebandAudioTap"
+ "Instantiation of AVAssetReaderTrackOutput for track=%!s(MISSING) with settings=%!s(MISSING) failed for asset=%!s(MISSING)"
+ "Uplink"
+ "VCAudioBufferList_SetSilenceInQueue"
+ "VFIRFSCnt"
+ "_VCAudioPlayer_ProcessDiscardState"
+ "callRecordingEnabled"
+ "callrecordingcaptions"
+ "com.apple.AVConference.AVCBasebandAudioTap.delegateQueue"
+ "enableDeferredNetworkUplinkClockUpdate"
+ "preferDecodingSquareCameraVideo"
+ "streamToken=%!@(MISSING) tapType=%!@(MISSING) averagePower=%!f(MISSING) "
+ "vcMediaStreamSetUpCaptioning"
+ "vcMediaStreamSetUpRecording"
+ "{ %!@(MISSING) success=%!s(MISSING) tapToken=%!l(MISSING)d uplinkToken=%!l(MISSING)d downlinkToken=%!l(MISSING)d }"
- "-[VCHardwareSettingsEmbedded supportsCameraDecodeSquare]"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCAudioStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCQoSMonitor.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCSessionParticipant.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVCVideoStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AVConference.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptions.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/SIP/SIP.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/TCPTunnelClient.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCAudioTransmitter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCallSessionCategories.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCCaptionsStreamSendGroup.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamGroup.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCMediaStreamTransport.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+Messaging.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession+OneToOne.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSession.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipant.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCSessionParticipantLocal.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTextStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCTransportSessionLegacy.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoCaptureServer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VCVideoStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/VideoConference.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AVConference/Common/VCMediaDevice.m"
- "2055.53.1"
- "CameraVideoPreferSquare"

```
