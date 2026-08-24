## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference`

```diff

-2235.57.1.0.0
-  __TEXT.__text: 0x7c0788
+2235.63.5.2.0
+  __TEXT.__text: 0x7c8cc0
   __TEXT.__realtime: 0xea4
-  __TEXT.__objc_methlist: 0x39c68
-  __TEXT.__const: 0x184d8
-  __TEXT.__cstring: 0x9afd2
-  __TEXT.__oslogstring: 0x13eb70
+  __TEXT.__objc_methlist: 0x39ec8
+  __TEXT.__const: 0x184e8
+  __TEXT.__cstring: 0x9b912
+  __TEXT.__oslogstring: 0x140e62
   __TEXT.__gcc_except_tab: 0x3188
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x12458
+  __TEXT.__unwind_info: 0x12578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ea0
+  __DATA_CONST.__const: 0x3ec8
   __DATA_CONST.__objc_classlist: 0x14a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x183a0
+  __DATA_CONST.__objc_selrefs: 0x184d0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1248
-  __DATA_CONST.__objc_arraydata: 0x2780
-  __DATA_CONST.__got: 0x1b58
-  __AUTH_CONST.__const: 0x8958
-  __AUTH_CONST.__cfstring: 0x28dc0
-  __AUTH_CONST.__objc_const: 0x6c3b8
+  __DATA_CONST.__objc_arraydata: 0x2790
+  __DATA_CONST.__got: 0x1b68
+  __AUTH_CONST.__const: 0x8a58
+  __AUTH_CONST.__cfstring: 0x290e0
+  __AUTH_CONST.__objc_const: 0x6c678
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x4e00
   __AUTH_CONST.__objc_arrayobj: 0x1d58
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x1e0
+  __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x2b78
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x7630
+  __DATA.__objc_ivar: 0x7678
   __DATA.__data: 0x7e50
-  __DATA.__bss: 0x998
+  __DATA.__bss: 0x9b8
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0xcd50
   __DATA_DIRTY.__data: 0x428

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35222
-  Symbols:   54381
-  CStrings:  33180
+  Functions: 35328
+  Symbols:   54515
+  CStrings:  33326
 
Symbols:
+ +[AVCCameraTestUtils isDualCameraCaptureSupported]
+ +[VCHardwareSettings supportsSquarePreviewCapture]
+ -[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]
+ -[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]
+ -[AVConferenceXPCServer stripUnspoofableInboundKeysFromDictionary:]
+ -[LoopbackSocketTunnel dealloc]
+ -[VCAVFoundationCapture _applySecondaryAspectRatioLocked:]
+ -[VCAVFoundationCapture addSecondaryCameraLiveForDualCapture:]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]
+ -[VCAVFoundationCapture dispatchedEnableDualCapture:]
+ -[VCAVFoundationCapture dispatchedEnableDualCapture:reapplyPrimaryFormat:]
+ -[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement:]
+ -[VCAVFoundationCapture squarePreviewAdjustedRequestSizeForCaptureSize:]
+ -[VCAVFoundationCapture tearDownSecondaryCameraResourcesLocked]
+ -[VCAVFoundationCapture updateSecondaryCameraResizeConverterForAspectRatio:]
+ -[VCAudioRelayIOController updateDirectionForClient:newDirection:]
+ -[VCCoreAudio_AudioUnitMockInstance duckingLevelWasSet]
+ -[VCCoreAudio_AudioUnitMockInstance duckingLevel]
+ -[VCCoreAudio_AudioUnitMockInstance setDuckingLevel:]
+ -[VCCoreAudio_AudioUnitMockInstance setDuckingLevelWasSet:]
+ -[VCDatagramChannelIDS idsChannel]
+ -[VCDatagramChannelIDS setIdsChannel:]
+ -[VCMediaAnalyzer dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:]
+ -[VCMediaStream onSetCurrentUplinkTargetBitrate:]
+ -[VCMediaStream setCurrentUplinkTargetBitrate:]
+ -[VCNetworkAgent clearMediaInformationAssertionLocked]
+ -[VCRateControlAlgorithmBase rateSharingFactor]
+ -[VCRateControlAlgorithmBase setRateSharingFactor:]
+ -[VCRateControllerManager removeRateControllerSharingGroup:]
+ -[VCRateSharingGroup countActiveRateControllersForInterfaceType:]
+ -[VCRateSharingGroup countInactiveRateControllersForInterfaceType:]
+ -[VCRedundancyControlAlgorithmVideo currentTargetBitrate]
+ -[VCRedundancyControlAlgorithmVideo setCurrentTargetBitrate:]
+ -[VCRedundancyControllerVideo setCurrentUplinkTargetBitrate:]
+ -[VCSession shouldStopParticipantOnMediaDecryptionTimeout]
+ -[VCSession validateConfiguration:]
+ -[VCVideoCaptureServer applyCameraUIDsToCaptureBackendWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:]
+ -[VCVideoCaptureServer applyPrimarySecondaryCameraUIDsWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:hasAspectRatio:]
+ -[VCVideoCaptureServer didSetPrimarySecondaryCameraUIDsWithError:]
+ -[VCVideoCaptureServer reconcileDualCaptureEnableAfterBatchWithSecondaryUID:hasSecondary:batchSPIHandledEnable:wasDualCaptureEnabled:]
+ -[VCVideoCaptureServer setViewPointCorrectionDisabled:forReason:]
+ -[VCVideoCaptureServer validationErrorForPrimaryUID:secondaryUID:aspectRatio:hasAspectRatio:]
+ -[VCVideoStream onSetCurrentUplinkTargetBitrate:]
+ -[VCVideoStreamConfig validateRemoteEndpointCount]
+ AppendBinaryBody
+ GCC_except_table104
+ GCC_except_table121
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table141
+ GCC_except_table145
+ GCC_except_table165
+ GCC_except_table172
+ GCC_except_table184
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table238
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table318
+ GCC_except_table94
+ GCC_except_table97
+ OBJC_IVAR_$_AVConferencePreview._setPrimarySecondaryCompletionHandler
+ OBJC_IVAR_$_CameraConferenceSynchronizer._blockLock
+ OBJC_IVAR_$_LoopbackSocketTunnel._stop
+ OBJC_IVAR_$_LoopbackSocketTunnel._tid
+ OBJC_IVAR_$_VCAVFoundationCapture._clientRequestedSize
+ OBJC_IVAR_$_VCAVFoundationCapture._configuringForCapture
+ OBJC_IVAR_$_VCAVFoundationCapture._pendingDesiredSecondaryCameraAspectRatio
+ OBJC_IVAR_$_VCAVFoundationCapture._squarePreviewOverrideActive
+ OBJC_IVAR_$_VCAVFoundationCapture._userEyeContactPref
+ OBJC_IVAR_$_VCCoreAudio_AudioUnitMockInstance._duckingLevel
+ OBJC_IVAR_$_VCCoreAudio_AudioUnitMockInstance._duckingLevelWasSet
+ OBJC_IVAR_$_VCDatagramChannelIDS._idsChannelLock
+ OBJC_IVAR_$_VCExperimentManager._disableAllExperiments
+ OBJC_IVAR_$_VCRateControlAlgorithmBase._rateSharingFactor
+ OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._currentTargetBitrate
+ OBJC_IVAR_$_VCRedundancyControllerVideo._acceptsTargetBitrateUpdates
+ OBJC_IVAR_$_VCRedundancyControllerVideo._algorithmLock
+ OBJC_IVAR_$_VCVideoCaptureServer._viewPointCorrectionDisableReasons
+ VCAudioRedBuilder_GetPrimaryPayloadAndAppendSamples
+ _AVCPreviewCameraSessionErrorDomain
+ _GKSConnectivitySettings_GetDoubleValueWithClientOption
+ _VCAbTestEnableAudioDeferredLossThreshold
+ _VCAudioDeferredLossOutOfOrderThreshold
+ _VCAudioDeferredLossOutOfOrderWindow
+ _VCRTCSamplingThresholdInternal
+ _VCRTCSamplingThresholdRelease
+ _VCReduceKPIVariationGracefulStopInTierB
+ __101-[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]_block_invoke
+ __61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_5
+ __71-[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]_block_invoke
+ __VCNetworkConditionMonitor_ExecuteOnStateQueue
+ __ZL38_AUIOLoadDynamicDuckerHALLevelOverrideP7tagAUIOj
+ ___101-[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]_block_invoke
+ ___30-[AVConferencePreview dealloc]_block_invoke
+ ___47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_14
+ ___49-[VCMediaNegotiator localeWithMediaBlobLanguage:]_block_invoke
+ ___49-[VCMediaNegotiator mediaBlobLanguageWithLocale:]_block_invoke
+ ___50+[VCHardwareSettings supportsSquarePreviewCapture]_block_invoke
+ ___50-[VCAudioRelayIOController updateClient:settings:]_block_invoke
+ ___53-[VCVideoCaptureServer getCaptureFrameRateForSource:]_block_invoke_2
+ ___66-[VCVideoCaptureServer didSetPrimarySecondaryCameraUIDsWithError:]_block_invoke
+ ___67-[VCMediaAnalyzer configure:forAnalysisType:mediaProperties:error:]_block_invoke
+ ___71-[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]_block_invoke
+ ___73-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke
+ ___block_descriptor_352_e8_32o_e5_v8?0l
+ ___block_descriptor_63_e8_32o40o48o_e5_v8?0l
+ ___block_descriptor_72_e8_32o40o48b56r_e5_v8?0l
+ ___block_descriptor_72_e8_32o40o48o56b_e5_v8?0l
+ ___copy_helper_block_e8_32o40o48b56r
+ ___destroy_helper_block_e8_32o40o48b56r
+ _kVCExperimentEnableAudioDeferredLoss
+ _kVCNetworkConditionMonitorStateQueueKey
+ _objc_msgSend$_applySecondaryAspectRatioLocked:
+ _objc_msgSend$addSecondaryCameraLiveForDualCapture:
+ _objc_msgSend$applyCameraUIDsToCaptureBackendWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:
+ _objc_msgSend$applyPrimarySecondaryCameraUIDsWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:hasAspectRatio:
+ _objc_msgSend$bandwidthEstimation
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:aspectRatio:
+ _objc_msgSend$countActiveRateControllersForInterfaceType:
+ _objc_msgSend$countInactiveRateControllersForInterfaceType:
+ _objc_msgSend$didSetPrimarySecondaryCameraUIDsWithError:
+ _objc_msgSend$dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:
+ _objc_msgSend$dispatchedEnableDualCapture:
+ _objc_msgSend$dispatchedEnableDualCapture:reapplyPrimaryFormat:
+ _objc_msgSend$idsChannel
+ _objc_msgSend$notifyDidSetPrimarySecondaryCameraUIDsWithError:
+ _objc_msgSend$onSetCurrentUplinkTargetBitrate:
+ _objc_msgSend$rateSharingFactor
+ _objc_msgSend$reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement:
+ _objc_msgSend$reconcileDualCaptureEnableAfterBatchWithSecondaryUID:hasSecondary:batchSPIHandledEnable:wasDualCaptureEnabled:
+ _objc_msgSend$removeRateControllerSharingGroup:
+ _objc_msgSend$setCurrentTargetBitrate:
+ _objc_msgSend$setDuckingLevel:
+ _objc_msgSend$setDuckingLevelWasSet:
+ _objc_msgSend$setIdsChannel:
+ _objc_msgSend$setViewPointCorrectionDisabled:forReason:
+ _objc_msgSend$shouldStopParticipantOnMediaDecryptionTimeout
+ _objc_msgSend$squarePreviewAdjustedRequestSizeForCaptureSize:
+ _objc_msgSend$stripUnspoofableInboundKeysFromDictionary:
+ _objc_msgSend$supportsSquarePreviewCapture
+ _objc_msgSend$tearDownSecondaryCameraResourcesLocked
+ _objc_msgSend$updateDirectionForClient:newDirection:
+ _objc_msgSend$updateSecondaryCameraResizeConverterForAspectRatio:
+ _objc_msgSend$validateRemoteEndpointCount
+ _objc_msgSend$validationErrorForPrimaryUID:secondaryUID:aspectRatio:hasAspectRatio:
+ localeWithMediaBlobLanguage:.onceToken
+ mediaBlobLanguageWithLocale:.onceToken
+ supportsSquarePreviewCapture.onceToken
+ supportsSquarePreviewCapture.resolved
- -[VCVideoCaptureServer setViewPointCorrectionEnabled:]
- GCC_except_table102
- GCC_except_table124
- GCC_except_table125
- GCC_except_table128
- GCC_except_table134
- GCC_except_table152
- GCC_except_table159
- GCC_except_table163
- GCC_except_table207
- GCC_except_table209
- GCC_except_table211
- GCC_except_table229
- GCC_except_table254
- GCC_except_table266
- GCC_except_table269
- GCC_except_table309
- GCC_except_table92
- GCC_except_table96
- VCExperimentManager_GetExperimentGroup
- ___block_descriptor_344_e5_v8?0l
CStrings:
+ " [%s] %s:%d %@(%p) AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d %@(%p) AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d %@(%p) Add multicast client=%p into existing _multicastRateSharingClientMap with count=%u"
+ " [%s] %s:%d %@(%p) Dropping oversized active-stream update event with %lu active streams (capacity %d)"
+ " [%s] %s:%d %@(%p) Removed sharingGroup=%p for keys=%@"
+ " [%s] %s:%d %@(%p) Video remote endpoints count=%lu exceeds transmitter max=%d, rejecting config"
+ " [%s] %s:%d %@(%p) [FTDC] deferring secondary AR=%d: dualCaptureEnabled=%d, secondaryCameraDevice=%p"
+ " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d %@(%p) audioChannelIndex changed %u -> %u for streamGroup=%s"
+ " [%s] %s:%d %@(%p) isDecryptionContextSet=%d"
+ " [%s] %s:%d %@(%p) isDecryptionContextSet=%d, result=%d"
+ " [%s] %s:%d %@(%p) isEncryptionContextSet=%d"
+ " [%s] %s:%d %@(%p) isEncryptionContextSet=%d, result=%d"
+ " [%s] %s:%d %@(%p) setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ " [%s] %s:%d %@(%p) sharingGroup must not be nil"
+ " [%s] %s:%d %d->%d, enabled=%d, userPref=%d"
+ " [%s] %s:%d AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d Add multicast client=%p into existing _multicastRateSharingClientMap with count=%u"
+ " [%s] %s:%d Dropping oversized active-stream update event with %lu active streams (capacity %d)"
+ " [%s] %s:%d Failed to decompress feature list string"
+ " [%s] %s:%d Failed to decompress feature list string for stream group id=%s"
+ " [%s] %s:%d Failed to decompress video feature list string for group id=%s"
+ " [%s] %s:%d Lost data packet count exceeds capacity, count=%d max=%d"
+ " [%s] %s:%d Received parity packet count exceeds capacity, count=%d max=%d"
+ " [%s] %s:%d Releasing the mediaQueue:%p, numPacketsFailedToSend=%u"
+ " [%s] %s:%d Removed sharingGroup=%p for keys=%@"
+ " [%s] %s:%d Target Bitrate too low. Can't support BDATV2 Redundancy"
+ " [%s] %s:%d VCFeatureExperimentSetting: Non-AB rollout default: experiment=%s thresholdValue=%f internalOrSeed=%d resolvedGroup=%u (reason: storebag active + UUID not A/B-sampled: reserved or unobservable)"
+ " [%s] %s:%d VCFeatureExperimentSetting: Non-AB storebag override: experiment=%s resolvedGroup=%u"
+ " [%s] %s:%d VCFeatureExperimentSetting: Override skipped: experiment not in client set (expected for non-A/B / rollout-default). name=%s"
+ " [%s] %s:%d VCHardwareSettings: squarePreviewCapture support overridden by user default: outOfBox=%d override=%d"
+ " [%s] %s:%d Video remote endpoints count=%lu exceeds transmitter max=%d, rejecting config"
+ " [%s] %s:%d [AR_TX] _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, previewOnly=%d, prefersSquarePreview=%d, captureAspectRatio=%@, overrideByDefault=%d"
+ " [%s] %s:%d [FTDC] Suppressing cached primary camera restore: remote still transmitting Dual Capture, front camera must stay square, _dualCaptureReceiverEnabled=%d"
+ " [%s] %s:%d [FTDC] aspectRatio=%d, current=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d [FTDC] deferring secondary AR=%d: dualCaptureEnabled=%d, secondaryCameraDevice=%p"
+ " [%s] %s:%d [FTDC] enable=%d, _dualCaptureEnabled=%d, _dualCaptureSupported=%d, reapplyPrimaryFormat=%d"
+ " [%s] %s:%d [FTDC] ignoring non-secondary cameraSessionType=%d"
+ " [%s] %s:%d [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d [FTDC] selectedDevice=%@ conflicts with secondary camera, tearing down DC"
+ " [%s] %s:%d already in effective=%d, enabled=%d, userPref=%d"
+ " [%s] %s:%d audioChannelIndex changed %u -> %u for streamGroup=%s"
+ " [%s] %s:%d compressedData=%p length=%lu"
+ " [%s] %s:%d compressedData=%p length=0"
+ " [%s] %s:%d double free detected for pool=%p pointer=%p!"
+ " [%s] %s:%d isDecryptionContextSet=%d"
+ " [%s] %s:%d isDecryptionContextSet=%d, result=%d"
+ " [%s] %s:%d isEncryptionContextSet=%d"
+ " [%s] %s:%d isEncryptionContextSet=%d, result=%d"
+ " [%s] %s:%d parameter can't be NULL fecConsumer=%p"
+ " [%s] %s:%d ring buffer miss for frameIndex=%d, repeating last frame"
+ " [%s] %s:%d rollback addDeviceInput failed, savedInput=%@"
+ " [%s] %s:%d setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ " [%s] %s:%d setUpCaptureDevice failed hResult=0x%x, rolling back to savedInput=%@"
+ " [%s] %s:%d sharingGroup must not be nil"
+ " [%s] %s:%d targetDecayHysteresisSampleCount was not configured, defaulting to targetDecayHysteresisSampleCount=%u samples"
+ "+[VCHardwareSettings supportsSquarePreviewCapture]_block_invoke"
+ "-[AVCPreviewCameraSession dispatchedNotifyDidSetCameraUID:error:]"
+ "-[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]_block_invoke"
+ "-[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]_block_invoke"
+ "-[VCAVFoundationCapture _applySecondaryAspectRatioLocked:]"
+ "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke"
+ "-[VCAVFoundationCapture dispatchedEnableDualCapture:reapplyPrimaryFormat:]"
+ "-[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement:]"
+ "-[VCAVFoundationCapture updateSecondaryCameraResizeConverterForAspectRatio:]"
+ "-[VCAudioStreamReceiveGroup setAudioChannelIndex:]_block_invoke"
+ "-[VCAudioTransmitter setStreamIDs:]"
+ "-[VCMediaAnalyzer dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:]"
+ "-[VCRateControllerManager removeRateControllerSharingGroup:]"
+ "-[VCVideoCaptureServer applyCameraUIDsToCaptureBackendWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:]"
+ "-[VCVideoCaptureServer applyPrimarySecondaryCameraUIDsWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:hasAspectRatio:]"
+ "-[VCVideoCaptureServer didSetPrimarySecondaryCameraUIDsWithError:]"
+ "-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_14"
+ "-[VCVideoStreamConfig applyVideoStreamClientDictionary:]"
+ "-[VCVideoStreamConfig validateRemoteEndpointCount]"
+ "-[VideoConference updatedConnectedPeers:]"
+ "-[VideoConference(AudioProcessing) updateMeter:forParticipant:atIndex:]"
+ "-nonab-rollout"
+ "2235.63.5.2"
+ "<null>"
+ "@:@ AVConferencePreview-didSetPrimarySecondaryCameraUIDs"
+ "AVCPreviewCameraSession [%s] %s:%d %@(%p) Unspecified aspectRatio is not valid for the standalone setter"
+ "AVCPreviewCameraSession [%s] %s:%d %@(%p) syncing _cameraUID from [%@] to daemon-confirmed [%@]"
+ "AVCPreviewCameraSession [%s] %s:%d Unspecified aspectRatio is not valid for the standalone setter"
+ "AVCPreviewCameraSession [%s] %s:%d syncing _cameraUID from [%@] to daemon-confirmed [%@]"
+ "AVCRC [%s] %s:%d %@(%p) Deferred request probing sequence for mode=%d, bwe=%u, rateSharingCount=%u, rateSharingFactor=%.1f, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
+ "AVCRC [%s] %s:%d %@(%p) isDelegateCallbackDeferralEnabled=%u, dumpID=%s"
+ "AVCRC [%s] %s:%d Deferred request probing sequence for mode=%d, bwe=%u, rateSharingCount=%u, rateSharingFactor=%.1f, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
+ "AVCRC [%s] %s:%d isDelegateCallbackDeferralEnabled=%u, dumpID=%s"
+ "AVConferencePreview [%s] %s:%d @:@ AVConferencePreview-didSetPrimarySecondaryCameraUIDs (%p) error=%@"
+ "AVConferencePreview [%s] %s:%d aborting setPrimaryCameraUID: code=%ld (%@)"
+ "AVConferencePreview [%s] %s:%d no completionHandler, error=%@"
+ "AVConferencePreview [%s] %s:%d primaryUID=%@, secondaryUID=%@, secondaryAspectRatio=%ld"
+ "AVConferencePreview deallocated with a pending request"
+ "Cannot add remote endpoint, max number of remote endpoints reached"
+ "Failed to allocate request"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody NULL param"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody overflow [headerLen=%d + bodySize=%d > capacity=%d]"
+ "Secondary aspect ratio requires dual capture"
+ "Too many remote endpoints"
+ "Unknown primary camera UID"
+ "Unknown secondary camera UID"
+ "Unspecified aspect ratio is only supported by the atomic camera setter"
+ "VCAudioRedBuilder [%s] %s:%d Discarding RED payload that exceeds max UDP size, bufferSize=%u"
+ "VCMediaQueue [%s] %s:%d Dropping malformed packet: extensionOffset=%u, dataSizeByte=%u, bufferLength=%zu"
+ "VCMediaQueue [%s] %s:%d Skipping control info for malformed packet: extensionOffset=%u, dataSizeByte=%u, bufferLength=%zu"
+ "VCSession [%s] %s:%d %@(%p) KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d includeInTierB=%d)"
+ "VCSession [%s] %s:%d %@(%p) Rejecting U+1 config update - remoteParticipantCount=%lu"
+ "VCSession [%s] %s:%d %@(%p) Stopping participant:%@ on media decryption timeout; session continues"
+ "VCSession [%s] %s:%d %@(%p) Stopping session on media decryption timeout for participant:%@"
+ "VCSession [%s] %s:%d %@(%p) sessionMode=%ld hasExistingSpatialAudioPool=%d"
+ "VCSession [%s] %s:%d KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d includeInTierB=%d)"
+ "VCSession [%s] %s:%d Rejecting U+1 config update - remoteParticipantCount=%lu"
+ "VCSession [%s] %s:%d Stopping participant:%@ on media decryption timeout; session continues"
+ "VCSession [%s] %s:%d Stopping session on media decryption timeout for participant:%@"
+ "VCSession [%s] %s:%d sessionMode=%ld hasExistingSpatialAudioPool=%d"
+ "VCVideoCaptureServer [%s] %s:%d [FTDC] error=%@"
+ "VCVideoCaptureServer [%s] %s:%d _avCapture=%p does not support setCameraUID: either; dropping"
+ "VCVideoCaptureServer [%s] %s:%d aspect ratio value is not NSNumber"
+ "VCVideoCaptureServer [%s] %s:%d batch SPI unavailable on _avCapture, falling back to sequential setCameraUID:"
+ "VCVideoCaptureServer [%s] %s:%d primary value is not NSString"
+ "VCVideoCaptureServer [%s] %s:%d primaryUID=%@, secondaryUID=%@ (hasSecondary=%d), hasAspectRatio=%d, aspectRatio=%ld"
+ "VCVideoCaptureServer [%s] %s:%d requested secondary aspectRatio=%d not applied: _avCapture=%p lacks batchSetCameraUIDsPrimary:secondary:aspectRatio:"
+ "VCVideoCaptureServer [%s] %s:%d secondary value is not nil/NSString/NSNull"
+ "VCVideoCaptureServer [%s] %s:%d validation failed, error=%@"
+ "VCVideoStream [%s] %s:%d %@(%p) Cannot add remote endpoint: at max=%d"
+ "VCVideoStream [%s] %s:%d %@(%p) isDecryptionContextSet=%d, result=%d"
+ "VCVideoStream [%s] %s:%d %@(%p) isEncryptionContextSet=%d, result=%d"
+ "VCVideoStream [%s] %s:%d %@(%p) repairStreamIDs count=%lu exceeds max=%d, rejecting config"
+ "VCVideoStream [%s] %s:%d Cannot add remote endpoint: at max=%d"
+ "VCVideoStream [%s] %s:%d isDecryptionContextSet=%d, result=%d"
+ "VCVideoStream [%s] %s:%d isEncryptionContextSet=%d, result=%d"
+ "VCVideoStream [%s] %s:%d repairStreamIDs count=%lu exceeds max=%d, rejecting config"
+ "VideoConference [%s] %s:%d %@(%p) dropped OOB participantIndex=%u max=%zu"
+ "VideoConference [%s] %s:%d %@(%p) rejected oversize newConnectedPeers count=%lu max=%zu"
+ "VideoConference [%s] %s:%d dropped OOB participantIndex=%u max=%zu"
+ "VideoConference [%s] %s:%d rejected oversize newConnectedPeers count=%lu max=%zu"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] FEC parity packet count out of bounds parityPacketsExpected=%d max=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] number of symbols per packet must not be 0"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] parityIndex=%d out of range, startPosition=%d, numberOfSymbolsPerPacket=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] startPosition=%d out of range, numberOfSymbolsPerPacket=%d"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] Reinitializing decoder (ImgDesc path) due to protected/unprotected content toggle"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] Reinitializing decoder (SPS/PPS path) due to protected/unprotected content toggle"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] Suppressing PSFB FIR: waiting for SFrame key (streamIndex=%d)"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] VideoPacketBuffer=%p stream=%p Sending PSFB FIR"
+ "_VCExperimentManager_NonABRolloutGroupForExperiment"
+ "en-US"
+ "enableAudioDeferredLoss"
+ "excludeFromNonABRollout"
+ "forceAdvancedDynamicDucker"
+ "forceSquarePreviewCapture"
+ "previewDidSetPrimarySecondaryCameraUIDs"
+ "previewPrimaryCameraUID"
+ "previewSecondaryCameraUID"
+ "previewSetPrimarySecondaryCameraUIDs"
+ "primary camera UID must not be nil"
+ "reduceKPIVariationGracefulStopInTierB"
+ "superseded by a newer setPrimaryCameraUID: request"
+ "vc-abtest-audio-deferred-loss-threshold"
+ "vc-audio-deferred-loss-ooo-threshold"
+ "vc-audio-deferred-loss-ooo-window"
+ "vc-kpi-var-graceful-stop-in-tier-b"
+ "vc-rtc-sampling-threshold-internal"
+ "vc-rtc-sampling-threshold-release"
- " [%s] %s:%d %d->%d"
- " [%s] %s:%d All %lu encodeDecodeFeatures blobs failed validation"
- " [%s] %s:%d Releasing the mediaQueue:%p"
- " [%s] %s:%d VCFeatureExperimentSetting: Failed to override experiment group. Error in retrieving experiment group"
- " [%s] %s:%d [AR_TX] _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, captureAspectRatio=%@, overrideByDefault=%d"
- " [%s] %s:%d [FTDC] aspectRatio=%d, cameraSessionType=%d, current=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d [FTDC] enable=%d, _dualCaptureEnabled=%d, _dualCaptureSupported=%d"
- " [%s] %s:%d already in enabled=%d"
- " [%s] %s:%d compressedData=%p, length=%lu"
- " [%s] %s:%d parameter can't be NULL newInstance=%p"
- "-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_4"
- "-[VCAVFoundationCapture enableDualCapture:]_block_invoke"
- "-[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement]"
- "2235.57.1"
- "AVCRC [%s] %s:%d %@(%p) Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
- "AVCRC [%s] %s:%d Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
- "VCSession [%s] %s:%d %@(%p) KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
- "VCSession [%s] %s:%d KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
- "VideoReceiver [%s] %s:%d VideoReceiver[%p] Suppressing FIR increment: waiting for SFrame key (streamIndex=%d)"
- "VideoReceiver [%s] %s:%d VideoReceiver[%p] VideoPacketBuffer[%p] stream[%p] Sending PSFB FIR"
```
