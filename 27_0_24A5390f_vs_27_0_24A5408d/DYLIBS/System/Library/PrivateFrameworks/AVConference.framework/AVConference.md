## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2235.57.1.0.0
-  __TEXT.__text: 0x7d7380
-  __TEXT.__objc_methlist: 0x3a968
-  __TEXT.__const: 0xc6c0
-  __TEXT.__cstring: 0x9eef2
-  __TEXT.__oslogstring: 0x13f959
+2235.63.1.1.0
+  __TEXT.__text: 0x7dfa1c
+  __TEXT.__objc_methlist: 0x3abe8
+  __TEXT.__const: 0xc690
+  __TEXT.__cstring: 0x9f9b5
+  __TEXT.__oslogstring: 0x141b50
   __TEXT.__gcc_except_tab: 0x2cf8
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x124c8
+  __TEXT.__unwind_info: 0x12600
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7718
+  __DATA_CONST.__const: 0x77e0
   __DATA_CONST.__objc_classlist: 0x14b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18c38
+  __DATA_CONST.__objc_selrefs: 0x18d88
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1268
-  __DATA_CONST.__objc_arraydata: 0x27c8
-  __DATA_CONST.__got: 0x1e30
-  __AUTH_CONST.__const: 0x45c8
-  __AUTH_CONST.__cfstring: 0x299c0
-  __AUTH_CONST.__objc_const: 0x6ce28
+  __DATA_CONST.__objc_arraydata: 0x27d8
+  __DATA_CONST.__got: 0x1e40
+  __AUTH_CONST.__const: 0x4608
+  __AUTH_CONST.__cfstring: 0x29d00
+  __AUTH_CONST.__objc_const: 0x6d128
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52f8
   __AUTH_CONST.__objc_arrayobj: 0x1d88
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x1e0
+  __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x2c38
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x76c4
+  __DATA.__objc_ivar: 0x7714
   __DATA.__data: 0x7d48
-  __DATA.__bss: 0x930
+  __DATA.__bss: 0x950
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xcf30
   __DATA_DIRTY.__data: 0x420

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35388
-  Symbols:   52994
-  CStrings:  33917
+  Functions: 35499
+  Symbols:   53133
+  CStrings:  34064
 
Symbols:
+ +[AVCCameraTestUtils isDualCameraCaptureSupported]
+ +[VCHardwareSettings supportsSquarePreviewCapture]
+ +[VideoUtil dualCameraPrimary1280SquareEncodingSize]
+ -[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]
+ -[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]
+ -[AVConferenceXPCServer stripUnspoofableInboundKeysFromDictionary:]
+ -[LoopbackSocketTunnel dealloc]
+ -[VCAVFoundationCapture _applySecondaryAspectRatioLocked:]
+ -[VCAVFoundationCapture addSecondaryCameraLiveForDualCapture:]
+ -[VCAVFoundationCapture applyDualCaptureResolutionToPrimaryCamera]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]
+ -[VCAVFoundationCapture dispatchedEnableDualCapture:]
+ -[VCAVFoundationCapture dispatchedEnableDualCapture:reapplyPrimaryFormat:]
+ -[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement:]
+ -[VCAVFoundationCapture squarePreviewAdjustedRequestSizeForCaptureSize:]
+ -[VCAVFoundationCapture tearDownSecondaryCameraResourcesLocked]
+ -[VCAVFoundationCapture updateSecondaryCameraResizeConverterForAspectRatio:]
+ -[VCAudioManager anyClientNeedsMicInputWithPreferredClient:]
+ -[VCAudioManager updateMicAttributionForClient:shouldAdd:]
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
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table158
+ GCC_except_table168
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table211
+ GCC_except_table220
+ GCC_except_table245
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table300
+ GCC_except_table72
+ GCC_except_table84
+ GCC_except_table89
+ _AVCPreviewCameraSessionErrorDomain
+ _GKSConnectivitySettings_GetDoubleValueWithClientOption
+ _OBJC_IVAR_$_AVConferencePreview._setPrimarySecondaryCompletionHandler
+ _OBJC_IVAR_$_CameraConferenceSynchronizer._blockLock
+ _OBJC_IVAR_$_LoopbackSocketTunnel._stop
+ _OBJC_IVAR_$_LoopbackSocketTunnel._tid
+ _OBJC_IVAR_$_VCAVFoundationCapture._clientRequestedSize
+ _OBJC_IVAR_$_VCAVFoundationCapture._configuringForCapture
+ _OBJC_IVAR_$_VCAVFoundationCapture._dualCamPrimaryPrefers1280SquareCapture
+ _OBJC_IVAR_$_VCAVFoundationCapture._pendingDesiredSecondaryCameraAspectRatio
+ _OBJC_IVAR_$_VCAVFoundationCapture._squarePreviewOverrideActive
+ _OBJC_IVAR_$_VCAVFoundationCapture._userEyeContactPref
+ _OBJC_IVAR_$_VCAudioManager._hasActiveMicClients
+ _OBJC_IVAR_$_VCCoreAudio_AudioUnitMockInstance._duckingLevel
+ _OBJC_IVAR_$_VCCoreAudio_AudioUnitMockInstance._duckingLevelWasSet
+ _OBJC_IVAR_$_VCDatagramChannelIDS._idsChannelLock
+ _OBJC_IVAR_$_VCExperimentManager._disableAllExperiments
+ _OBJC_IVAR_$_VCRateControlAlgorithmBase._rateSharingFactor
+ _OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._currentTargetBitrate
+ _OBJC_IVAR_$_VCRedundancyControllerVideo._acceptsTargetBitrateUpdates
+ _OBJC_IVAR_$_VCRedundancyControllerVideo._algorithmLock
+ _OBJC_IVAR_$_VCVideoCaptureServer._viewPointCorrectionDisableReasons
+ _VCAbTestEnableAudioDeferredLossThreshold
+ _VCAudioDeferredLossOutOfOrderThreshold
+ _VCAudioDeferredLossOutOfOrderWindow
+ _VCRTCSamplingThresholdInternal
+ _VCRTCSamplingThresholdRelease
+ _VCReduceKPIVariationGracefulStopInTierB
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
+ ___54-[VCAVFoundationCapture initializeViewpointCorrection]_block_invoke
+ ___61-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_6
+ ___65-[VCVideoCaptureServer setViewPointCorrectionDisabled:forReason:]_block_invoke
+ ___66-[VCVideoCaptureServer didSetPrimarySecondaryCameraUIDsWithError:]_block_invoke
+ ___67-[VCMediaAnalyzer configure:forAnalysisType:mediaProperties:error:]_block_invoke
+ ___71-[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]_block_invoke
+ ___73-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke
+ ___block_descriptor_352_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_63_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40o48b56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40o48o56b_e5_v8?0ls32l8s40l8s48l8s56l8
+ _kVCExperimentEnableAudioDeferredLoss
+ _kVCNetworkConditionMonitorStateQueueKey
+ _localeWithMediaBlobLanguage:.onceToken
+ _mediaBlobLanguageWithLocale:.onceToken
+ _objc_msgSend$_applySecondaryAspectRatioLocked:
+ _objc_msgSend$addSecondaryCameraLiveForDualCapture:
+ _objc_msgSend$anyClientNeedsMicInputWithPreferredClient:
+ _objc_msgSend$applyCameraUIDsToCaptureBackendWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:
+ _objc_msgSend$applyDualCaptureResolutionToPrimaryCamera
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
+ _objc_msgSend$dualCameraPrimary1280SquareEncodingSize
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
+ _objc_msgSend$updateMicAttributionForClient:shouldAdd:
+ _objc_msgSend$updateSecondaryCameraResizeConverterForAspectRatio:
+ _objc_msgSend$validateRemoteEndpointCount
+ _objc_msgSend$validationErrorForPrimaryUID:secondaryUID:aspectRatio:hasAspectRatio:
+ _supportsSquarePreviewCapture.onceToken
+ _supportsSquarePreviewCapture.resolved
- -[VCVideoCaptureServer setViewPointCorrectionEnabled:]
- GCC_except_table109
- GCC_except_table114
- GCC_except_table117
- GCC_except_table122
- GCC_except_table149
- GCC_except_table153
- GCC_except_table160
- GCC_except_table188
- GCC_except_table190
- GCC_except_table192
- GCC_except_table210
- GCC_except_table235
- GCC_except_table244
- GCC_except_table247
- GCC_except_table250
- GCC_except_table290
- GCC_except_table70
- GCC_except_table82
- GCC_except_table88
- GCC_except_table98
- ___block_descriptor_344_e5_v8?0l
CStrings:
+ " [%s] %s:%d %@(%p) AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d %@(%p) AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d %@(%p) Add multicast client=%p into existing _multicastRateSharingClientMap with count=%u"
+ " [%s] %s:%d %@(%p) Applying mute property for audioSessionId=%d, isMuted=%d (sessionMute=%@ _isMicrophoneMuted=%d hasActiveMicClients=%d)"
+ " [%s] %s:%d %@(%p) Dropping oversized active-stream update event with %lu active streams (capacity %d)"
+ " [%s] %s:%d %@(%p) Removed sharingGroup=%p for keys=%@"
+ " [%s] %s:%d %@(%p) Video remote endpoints count=%lu exceeds transmitter max=%d, rejecting config"
+ " [%s] %s:%d %@(%p) [FTDC] deferring secondary AR=%d: dualCaptureEnabled=%d, secondaryCameraDevice=%p"
+ " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d %@(%p) isDecryptionContextSet=%d"
+ " [%s] %s:%d %@(%p) isDecryptionContextSet=%d, result=%d"
+ " [%s] %s:%d %@(%p) isEncryptionContextSet=%d"
+ " [%s] %s:%d %@(%p) isEncryptionContextSet=%d, result=%d"
+ " [%s] %s:%d %@(%p) setMicrophoneMuted=%d"
+ " [%s] %s:%d %@(%p) setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ " [%s] %s:%d %@(%p) sharingGroup must not be nil"
+ " [%s] %s:%d %d->%d, enabled=%d, userPref=%d"
+ " [%s] %s:%d AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d Add multicast client=%p into existing _multicastRateSharingClientMap with count=%u"
+ " [%s] %s:%d Applying mute property for audioSessionId=%d, isMuted=%d (sessionMute=%@ _isMicrophoneMuted=%d hasActiveMicClients=%d)"
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
+ " [%s] %s:%d setMicrophoneMuted=%d"
+ " [%s] %s:%d setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ " [%s] %s:%d setUpCaptureDevice failed hResult=0x%x, rolling back to savedInput=%@"
+ " [%s] %s:%d sharingGroup must not be nil"
+ " [%s] %s:%d targetDecayHysteresisSampleCount was not configured, defaulting to targetDecayHysteresisSampleCount=%u samples"
+ "+[VCHardwareSettings supportsSquarePreviewCapture]_block_invoke"
+ "-[AVCPreviewCameraSession dispatchedNotifyDidSetCameraUID:error:]"
+ "-[AVConferencePreview notifyDidSetPrimarySecondaryCameraUIDsWithError:]_block_invoke"
+ "-[AVConferencePreview registerBlocksForDelegateNotifications]_block_invoke_6"
+ "-[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]_block_invoke"
+ "-[AVConferencePreview setPrimaryCameraUID:secondaryCameraUID:secondaryAspectRatio:completionHandler:]_block_invoke_2"
+ "-[VCAVFoundationCapture _applySecondaryAspectRatioLocked:]"
+ "-[VCAVFoundationCapture addSecondaryCameraLiveForDualCapture:]"
+ "-[VCAVFoundationCapture applyDualCaptureResolutionToPrimaryCamera]"
+ "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke"
+ "-[VCAVFoundationCapture dispatchedEnableDualCapture:reapplyPrimaryFormat:]"
+ "-[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement:]"
+ "-[VCAVFoundationCapture updateSecondaryCameraResizeConverterForAspectRatio:]"
+ "-[VCAudioTransmitter setStreamIDs:]"
+ "-[VCMediaAnalyzer dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:]"
+ "-[VCRateControllerManager removeRateControllerSharingGroup:]"
+ "-[VCVideoCaptureServer applyCameraUIDsToCaptureBackendWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:]"
+ "-[VCVideoCaptureServer applyPrimarySecondaryCameraUIDsWithPrimaryUID:secondaryUID:aspectRatio:hasPrimary:hasSecondary:hasAspectRatio:]"
+ "-[VCVideoCaptureServer didSetPrimarySecondaryCameraUIDsWithError:]"
+ "-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_14"
+ "-[VCVideoCaptureServer setViewPointCorrectionDisabled:forReason:]"
+ "-[VCVideoStreamConfig applyVideoStreamClientDictionary:]"
+ "-[VCVideoStreamConfig validateRemoteEndpointCount]"
+ "-[VideoConference updatedConnectedPeers:]"
+ "-[VideoConference(AudioProcessing) updateMeter:forParticipant:atIndex:]"
+ "-nonab-rollout"
+ "2235.63.1.1"
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
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody NULL param"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody failed(%08X)"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody overflow [headerLen=%d + bodySize=%d > capacity=%d]"
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
+ "VCSession [%s] %s:%d KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d includeInTierB=%d)"
+ "VCSession [%s] %s:%d Rejecting U+1 config update - remoteParticipantCount=%lu"
+ "VCSession [%s] %s:%d Stopping participant:%@ on media decryption timeout; session continues"
+ "VCSession [%s] %s:%d Stopping session on media decryption timeout for participant:%@"
+ "VCVideoCaptureServer [%s] %s:%d [FTDC] error=%@"
+ "VCVideoCaptureServer [%s] %s:%d _avCapture=%p does not support setCameraUID: either; dropping"
+ "VCVideoCaptureServer [%s] %s:%d aspect ratio value is not NSNumber"
+ "VCVideoCaptureServer [%s] %s:%d batch SPI unavailable on _avCapture, falling back to sequential setCameraUID:"
+ "VCVideoCaptureServer [%s] %s:%d disabled=%d, reason=%lu (0x%lx), shouldUpdateViewPointCorrection=%d"
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
+ "dualCamPrimaryPrefers1280SquareCapture"
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
- " [%s] %s:%d %@(%p) Applying mute property for audioSessionId=%d, isMuted=%d"
- " [%s] %s:%d %@(%p) setMicrophoneMuted:%d"
- " [%s] %s:%d %d->%d"
- " [%s] %s:%d All %lu encodeDecodeFeatures blobs failed validation"
- " [%s] %s:%d Applying mute property for audioSessionId=%d, isMuted=%d"
- " [%s] %s:%d Releasing the mediaQueue:%p"
- " [%s] %s:%d VCFeatureExperimentSetting: Failed to override experiment group. Error in retrieving experiment group"
- " [%s] %s:%d [AR_TX] _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, captureAspectRatio=%@, overrideByDefault=%d"
- " [%s] %s:%d [FTDC] aspectRatio=%d, cameraSessionType=%d, current=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d [FTDC] enable=%d, _dualCaptureEnabled=%d, _dualCaptureSupported=%d"
- " [%s] %s:%d already in enabled=%d"
- " [%s] %s:%d compressedData=%p, length=%lu"
- " [%s] %s:%d parameter can't be NULL newInstance=%p"
- " [%s] %s:%d setMicrophoneMuted:%d"
- "-[VCAVFoundationCapture enableDualCapture:]_block_invoke"
- "-[VCAVFoundationCapture reapplyCachedPrimaryCameraFormatAfterDualCaptureDisablement]"
- "-[VCVideoCaptureServer setViewPointCorrectionEnabled:]"
- "2235.57.1"
- "AVCRC [%s] %s:%d %@(%p) Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
- "AVCRC [%s] %s:%d Deferred request probing sequence for mode=%d, targetBitrate=%u, probingSequenceSize=%u, probingSequenceID=%u"
- "VCSession [%s] %s:%d %@(%p) KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
- "VCSession [%s] %s:%d KPI-VAR-STATE: groupSessionLeavingAutoStop=%d (oneToOneModeEnabled=%d)"
- "VCVideoCaptureServer [%s] %s:%d enabled=%d, shouldUpdateViewPointCorrection=%d"
- "VideoReceiver [%s] %s:%d VideoReceiver[%p] Suppressing FIR increment: waiting for SFrame key (streamIndex=%d)"
- "VideoReceiver [%s] %s:%d VideoReceiver[%p] VideoPacketBuffer[%p] stream[%p] Sending PSFB FIR"
```
