## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3255.68.6.11.3
-  __TEXT.__text: 0xfa218c
-  __TEXT.__auth_stubs: 0xb350
-  __TEXT.__objc_methlist: 0x23d4
-  __TEXT.__const: 0x544d0
-  __TEXT.__cstring: 0x12ce56
-  __TEXT.__oslogstring: 0x143579
+3255.73.1.11.3
+  __TEXT.__text: 0xfa8b70
+  __TEXT.__auth_stubs: 0xb3a0
+  __TEXT.__objc_methlist: 0x23f4
+  __TEXT.__const: 0x546e0
+  __TEXT.__cstring: 0x12d4ae
+  __TEXT.__oslogstring: 0x144650
   __TEXT.__ustring: 0x23e
-  __TEXT.__gcc_except_tab: 0x17dc
+  __TEXT.__gcc_except_tab: 0x17a0
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__unwind_info: 0x13a98
+  __TEXT.__unwind_info: 0x13a90
   __TEXT.__eh_frame: 0x220
   __TEXT.__objc_classname: 0x805
-  __TEXT.__objc_methname: 0x6a72
-  __TEXT.__objc_methtype: 0x2876
-  __TEXT.__objc_stubs: 0x6160
-  __DATA_CONST.__got: 0x3860
-  __DATA_CONST.__const: 0x23288
+  __TEXT.__objc_methname: 0x6abd
+  __TEXT.__objc_methtype: 0x28a3
+  __TEXT.__objc_stubs: 0x6180
+  __DATA_CONST.__got: 0x3858
+  __DATA_CONST.__const: 0x232c8
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x1ff8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x59c0
+  __AUTH_CONST.__auth_got: 0x59e8
   __AUTH_CONST.__const: 0x40e50
-  __AUTH_CONST.__cfstring: 0x52840
-  __AUTH_CONST.__objc_const: 0x4c80
+  __AUTH_CONST.__cfstring: 0x528e0
+  __AUTH_CONST.__objc_const: 0x4cc0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x8e8
-  __DATA.__objc_ivar: 0x320
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x183f0
   __DATA.__common: 0x2fc8
   __DATA.__bss: 0x25e0
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x4e8
-  __DATA_DIRTY.__bss: 0x1890
+  __DATA_DIRTY.__bss: 0x18a0
   __DATA_DIRTY.__common: 0x370
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3DA062D3-370B-33B6-BA5A-3991736CAE25
-  Functions: 43420
-  Symbols:   117034
-  CStrings:  66297
+  UUID: 1330E4CC-BD48-3D85-A6CA-EFDA2BB46DA9
+  Functions: 43446
+  Symbols:   117146
+  CStrings:  66380
 
Symbols:
+ -[FigVideoContainerLayer _checkIfRebuildIsRequiredWhileHoldingVideoTargetMutex]
+ -[FigVideoContainerLayer _createAndSetupVideoReceiverWithDeferredTransaction:]
+ -[FigVideoContainerLayer copyVideoReceiver]
+ -[FigVideoContainerLayer rebuild]
+ -[FigVideoContainerLayer requiresRebuild]
+ GCC_except_table287
+ GCC_except_table290
+ _CFBagSetValue
+ _CGColorCreateSRGB
+ _CGPathAddCurveToPoint
+ _CMRemoveAllAttachments
+ _EditMentorSetModeToDoNothing_fun
+ _EditMentorSetModeToEmptyEdit_fun
+ _EditMentorSetModeToForwardPlayback_fun
+ _EditMentorSetModeToReversePlayback_fun
+ _EditMentorSetModeToScrub_fun
+ _EditMentorSetModeToScrub_fun.cold.1
+ _EditMentorSetModeToScrub_fun.cold.2
+ _EditMentorSetProperty_fun
+ _FigAudioQueueOfflineMixerStartDrainingSampleBuffers
+ _FigAudioQueueOfflineMixerStartDrainingSampleBuffers.cold.1
+ _FigHLSPersistentStreamInfoCreate.cold.44
+ _FigHLSPersistentStreamInfoCreate.cold.45
+ _FigHLSTapToRadar
+ _FigMediaRequestDeliverOnceWithCacheCreate.cold.3
+ _FigXPCRemoteClientGetServerPIDSync
+ _MovieHeaderMakerSetShouldAllow64BitDataOffsetInTrackRunAtom
+ _MovieHeaderMakerSetShouldAllow64BitDataOffsetInTrackRunAtom.cold.1
+ _OBJC_CLASS_$_CAShapeLayer
+ _OBJC_IVAR_$_FigBaseCALayer._DRMFallbackIconLayer
+ _OBJC_IVAR_$_FigVideoContainerLayer._createdForVideoReceiver
+ _OBJC_IVAR_$_FigVideoContainerLayer._videoTargetAndReceiverMutex
+ _OUTLINED_FUNCTION_1161
+ _OUTLINED_FUNCTION_1162
+ _OUTLINED_FUNCTION_1163
+ _OUTLINED_FUNCTION_1164
+ _OUTLINED_FUNCTION_1165
+ _OUTLINED_FUNCTION_1166
+ _OUTLINED_FUNCTION_1167
+ _OUTLINED_FUNCTION_1168
+ _OUTLINED_FUNCTION_1169
+ _OUTLINED_FUNCTION_1170
+ __ZL18fim_NewAudioStreamP17OpaqueFigManifold
+ __ZL22fim_DestroyAudioStreamP13IcyAudioTrack
+ ___35-[FigBaseCALayer enableDRMFallback]_block_invoke_2
+ ___airplayRoute_setNewFigAudioSession_block_invoke.220
+ ___block_descriptor_tmp.189
+ ___block_descriptor_tmp.221
+ ___block_descriptor_tmp.230
+ ___block_literal_global.270
+ ___block_literal_global.299
+ ___block_literal_global.375
+ ___block_literal_global.463
+ ___block_literal_global.625
+ ___fbapspManager_flushFromTime_block_invoke.196
+ ___fpic_EnsureNextEventWillBuffer_block_invoke.245
+ ___fpic_EnsureNextEventWillBuffer_block_invoke.245.cold.1
+ ___fpic_HTTPReadCallback_block_invoke.210
+ ___fpic_NotifyServiceCurrentEvent_block_invoke.301
+ ___fpic_customURLReadCallback_block_invoke.220
+ _copy64BitDataOffsetInTrackRunAtomPolicy
+ _editMentorChildMentorPrerollComplete_orderQueue
+ _editMentorChildMentorStoppedDueToCompletion_orderQueue
+ _editMentorChildMentorStoppedDueToError_orderQueue
+ _editMentorEditsChanged_orderQueue
+ _editMentorForwardNotificationFromChildMentor_orderQueue
+ _editMentorTimeRangesMayNoLongerIncrease_orderQueue
+ _fbapspManager_HandlePendingSbufsOnSubPipeFinishCallback
+ _fbapspManager_processPendingSbufsOnSubPipeFinished
+ _figMovieWriter_SetProperty.cold.28
+ _fpfs_ShouldSyncAudioByMatchingWaveformOnce
+ _fpfs_SyncAudioBuffer.cold.1
+ _fpfs_SyncAudioBuffer.cold.2
+ _fpic_applyAutomaticLegibleMediaSelectionForItem
+ _kFigBytePumpAttachmentKey_FakeFormatDescription
+ _kFigFormatWriter64BitDataOffsetInTrackRunAtomPolicy_Allow
+ _kFigFormatWriter64BitDataOffsetInTrackRunAtomPolicy_DoNotAllow
+ _kFigFormatWriterProperty_64BitDataOffsetInTrackRunAtomPolicy
+ _kFigPlayerInterstitialNotification_CurrentEventChangePrimaryPlaybackState
+ _kFigTrialFactor_radar_153096490_TTREnabled
+ _kFigVideoTargetProperty_IsValid
+ _kStatsCounterShortNames
+ _mrdowc_handleNotificationAsync
+ _mrdowc_initializeHandlerQueue
+ _objc_msgSend$_checkIfRebuildIsRequiredWhileHoldingVideoTargetMutex
+ _objc_msgSend$_createAndSetupVideoReceiverWithDeferredTransaction:
+ _objc_msgSend$copyVideoReceiver
+ _objc_msgSend$setAllowsEdgeAntialiasing:
+ _objc_msgSend$setFillColor:
+ _objc_msgSend$setPath:
+ _remoteXPCVideoTarget_isValid
+ _remoteXPCVideoTarget_isValid.cold.1
+ _remoteXPCVideoTarget_postLoadingStateDidChangeNotification
+ _remoteXPCVideoTarget_postLoadingStateDidChangeNotification.cold.1
+ _segPumpSentEndCallbackForAnyStream.cold.1
+ _segPumpSentEndCallbackForAnyStreamHandleTTR
+ _segPumpSentEndCallbackForAnyStreamHandleTTR.cold.1
+ _segPumpSentEndCallbackForAnyStreamHandleTTR.cold.2
+ _set64BitDataOffsetInTrackRunAtomPolicy
+ _unlockRoot
- -[FigVideoContainerLayer _createAndSetupVideoReceiver]
- -[FigVideoContainerLayer videoReceiver]
- GCC_except_table284
- GCC_except_table289
- GCC_except_table56
- GCC_except_table57
- _EditMentorSetModeToScrub.cold.1
- _EditMentorSetModeToScrub.cold.2
- _FBLSupportAppendDeferredTransactionChangeToRemoveCAPackageFromSuperLayerAndReleaseIt
- _FBLSupportAppendDeferredTransactionChangeToRemoveCAPackageFromSuperLayerAndReleaseIt.cold.1
- _FigEndpointCopyProperty
- _FigHLSPersistentStoreCreateAtURL.cold.22
- _FigHLSPersistentStoreCreateAtURL.cold.23
- _FigHLSPersistentStoreCreateAtURL.cold.24
- _OBJC_CLASS_$_CAPackage
- _OBJC_IVAR_$_FigBaseCALayer._DRMFallbackIconPackage
- __ZL17fim_EndAudioTrackP17OpaqueFigManifoldi
- __ZL17fim_NewAudioTrackP17OpaqueFigManifold
- __ZL21fim_DestroyAudioTrackP13IcyAudioTrack
- ___35-[FigBaseCALayer enableDRMFallback]_block_invoke.48
- ___35-[FigBaseCALayer enableDRMFallback]_block_invoke.cold.1
- ___35-[FigBaseCALayer enableDRMFallback]_block_invoke.cold.2
- ___FigVideoReceiverConnectionHelperCreate_block_invoke_2.cold.1
- ___airplayRoute_setNewFigAudioSession_block_invoke.217
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.187
- ___block_descriptor_tmp.220
- ___block_descriptor_tmp.226
- ___block_literal_global.268
- ___block_literal_global.296
- ___block_literal_global.371
- ___block_literal_global.459
- ___block_literal_global.621
- ___fbapspManager_flushFromTime_block_invoke.192
- ___fpic_EnsureNextEventWillBuffer_block_invoke.242
- ___fpic_EnsureNextEventWillBuffer_block_invoke.242.cold.1
- ___fpic_HTTPReadCallback_block_invoke.207
- ___fpic_NotifyServiceCurrentEvent_block_invoke.298
- ___fpic_customURLReadCallback_block_invoke.217
- ___remoteXPCVideoTarget_establishServerConnection_block_invoke.cold.1
- _copyDescriptionForRemoveCAPackageFromSuperLayerAndReleaseItContext
- _disposeRemoveCAPackageFromSuperLayerAndReleaseItContext
- _editMentorAdjustSettingsFollowingChildPrerollComplete
- _editMentorEditsChanged_deferred
- _editMentorSetModeChangePolicyToPreservePreviousOutput
- _editMentorTimeRangesMayNoLongerIncrease_deferred
- _favd_copyFormatDescriptionToSidebandVideoPropertiesLookupIDMappingCommon
- _favd_copyFormatDescriptionToSidebandVideoPropertiesLookupIDMappingCommon.cold.1
- _favd_copySidebandVideoPropertiesArrayCommon
- _fbapspManager_SendPendingSbufOnSubPipeFinished
- _fpfs_RelockMutexWithCaller
- _fpfs_UnlockMutexCompletelyWithCaller
- _kCAPackageTypeArchive
- _kFigAggregateVideoDestinationProperty_MappingFromFormatDescriptionsToSidebandVideoPropertiesLookupIDs
- _kStatsCounterNames
- _objc_msgSend$_createAndSetupVideoReceiver
- _objc_msgSend$fileURLWithPath:isDirectory:
- _objc_msgSend$packageWithContentsOfURL:type:options:error:
- _objc_msgSend$pathForResource:ofType:
- _objc_msgSend$rootLayer
- _removeCAPackageFromSuperLayerAndReleaseIt
- _segPumpStreamProceedAfterMediaAndKeyArrival.cold.2
CStrings:
+ " %s %2d |"
+ "-[FigVideoContainerLayer _createAndSetupVideoReceiverWithDeferredTransaction:]"
+ "-[FigVideoContainerLayer rebuild]"
+ "64BitDataOffsetInTrackRunAtomPolicy"
+ "64BitDataOffset_Allow"
+ "64BitDataOffset_DoNotAllow"
+ "<<< FFR_Movie >>> %s: \t\t\t    DataOffset:             %lld"
+ "<<<< CENTRAL >>>> %s: [%p] %{public}s setting kMXSessionProperty_IsPlaying to %{public}s since rate = %1.1f "
+ "<<<< FAQ >>>> %s: [%p:%p] %{public}s FigAudioQueueTimingShimGetCurrentTime -> timeStamp { mFlags 0x%x,  mSampleTime %lld (%.3f seconds), faq->srcASBD->mSampleRate %d, mHostTime %llu (%.3f seconds) }"
+ "<<<< FAQ >>>> %s: [%p:%p] calling AudioQueueEnqueueBuffer(%p), sample rate = %d, raw PTS = {%lld/%d=%1.3f}, output PTS = {%lld/%d=%1.3f}, raw duration = {%lld/%d=%1.3f}, output duration = {%lld/%d=%1.3f}, mAudioDataByteSize = %u, mAudioDataBytesCapacity = %u (trim %d frames at start, %d frames at end)"
+ "<<<< FAQ >>>> %s: [%p] subAQ queueTime %.3f timestamp { mFlags 0x%x, mSampleTime %lld (%.3f seconds), subAQ->srcASBD->mSampleRate %.3f, mHostTime %llu (%.3f seconds) }"
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s Draining out mixer."
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s Mixer draining finished"
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s called. Run: %d AQStarted: %d HighWater: %d LowWater: %d Discard: %d Interrupt: %d Draining: %d"
+ "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s returning. Run: %d AQStarted: %d HighWater: %d LowWater: %d Discard: %d Interrupt: %d Draining: %d Processed: %.3f [%.3f:%.3f] (%d sample buffers)"
+ "<<<< FAQ Offline Mixer >>>> %s: currentTime isn't valid."
+ "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStart(%p), aqStartTimeStampPtr NULL"
+ "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStart(%p), mSampleTime %lld, mHostTime %llu (%.3f seconds), mFlags 0x%x"
+ "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStartWithFlags(%p, 0x%x), aqStartTimeStampPtr NULL"
+ "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStartWithFlags(%p, 0x%x), mSampleTime %lld, mHostTime %llu (%.3f seconds), mFlags 0x%x"
+ "<<<< FAQRP >>>> %s: (%p %{public}s) timebase %p effective rate changed, new rate %1.3f, current time %1.3f, current host time %1.3f"
+ "<<<< FIM >>>> %s: closing audio stream of type  %c%c%c%c"
+ "<<<< FIM >>>> %s: initializing audio stream of type  %c%c%c%c"
+ "<<<< FigAirPlay_Route >>>> %s: [%p] %{public}s Disallowing AP Video on session %p"
+ "<<<< FigAssetWriter >>>> %s: (%p) id %d track queue is above high water level in real time mode"
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@] Have pipelineRequestedRetransmissionMixStartMediaTime %1.3f."
+ "<<<< FigBufferedAirPlayOutputProxy >>>> %s: [%p] %{public}s rpID[%@] Using BAO mixStartMediaTime %1.3f."
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Data %s flow to subPipe. inputBufferQueue(count %ld, duration %1.3f), pipelineRateIsValid=%s, subPipeTerminationInFlight=%s, currentSubPipe=%p"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s HandlePendingSbufsOnSubpipeFinishCallback. Found FlushRangeEnd %@ "
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s No op. (mixing + outro + milestoneSet)  We will wait for milestone for state change.\n"
+ "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Set subPipe TimelineMilestone with overlapEndTimeWithOffset %1.3f because sbufEndOPTS %1.3f is past the overlapEndTime %1.3f."
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: %g(item1 L2)=%g(shared L1)=%g(item2 L2)"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Applied a forwardEndTime on track %d at {%lld/%d=%1.3f}, now %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Attempting to apply a forward end time at L3 {%lld/%d=%1.3f}, now L2 %g (L3 %g)"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Committing to recoveryAlternate"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Created manifold[%i:%p] with type - manifoldType: %{public}@"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: ILLEGAL STATE CHANGE: track %ld (state %d) with invalid discontinuityOffset asked to change to %d. Resetting to INIT (0)."
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Not switching, suggested alternate is in penalty box - expect another suggestion soon!"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Sample buffer ignored for track %d with invalid discontinuityOffset, startTime %f, raw %f, discDomain %d, cachedPumpTime %f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: WARNING: found track %d already in state %d, not adjusting the discontinuityOffset - it may be out of sync"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: audio track %d priming duration {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: cached anchor host time %1.3f is now in the past (= now %1.3f %+1.3f), buffered duration %1.3f -- DISCARDING ANCHOR HOST TIME"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: cannot set Properties at transition %d"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: deferring discontinuityOffset determination for sparse track %d"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: first sample of track %d, PTS L1: {%lld/%d=%1.3f}, Output PTS L2: {%lld/%d=%1.3f}, discDomain %d %{public}s, raw duration: {%lld/%d=%1.3f}, startTime L2: {%lld/%d=%1.3f}, discontinuityOffset: {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: found timeshift while changing gears %lld %u (%1.5g) updated discontinuityOffset {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: lastplaying is %d updated discontinuityOffset %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: locking track %ld to audio (%1.5g) updated discontinuityOffset %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: map sbuf %p L1 PTS {%lld/%d=%1.3f} to L2 OutputPTS {%lld/%d=%1.3f} duration {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: must reset pumpOffset anchor: drift=%1.3f, new anchorPumpTime=%1.3f, new anchorL2Time=%1.3f, old anchorPumpTime=%1.3f, old anchorL2Time=%1.3f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: new pumpOffset %1.3f, now %1.3f, anchorPumpTime %1.3f, anchorL2Time %1.3f"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: raw PTS L1 {%lld/%d=%1.3f}, old output PTS L2 {%lld/%d=%1.3f}, new output PTS L2 {%lld/%d=%1.3f}, trim duration {%lld/%d=%1.3f}, startTime L2 {%lld/%d=%1.3f}, sbuf end L2 {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: remove trim from start of sbuf %p (oldTrim {%lld/%d=%1.3f})"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: set discontinuityOffset %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: shifting track %d by {%lld/%d=%1.3f} - changing its discontinuityOffset from {%lld/%d=%1.3f} to {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: shifting track %d by {%lld/%d=%1.3f} - changing its first sample from {%lld/%d=%1.3f} to {%lld/%d=%1.3f}, discontinuityOffset from {%lld/%d=%1.3f} to {%lld/%d=%1.3f}"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: startTime %g pts %g primingDuration %g updated discontinuityOffset %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: startupQueue is not empty"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d abandoned sync before getting discontinuityOffset - harvested %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d discontinuityOffset cannot be set from previous track - set to %g so sbuf lands at startTime"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d inheriting cached discontinuityOffset %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d requires discontinuityOffset fix-up to %g; start at %g"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d start time is %g, gets discontinuityOffset %g from track %d, first sample is %f, raw: %f %s"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: trim {%lld/%d=%1.3f} from start of sbuf %p (oldTrim {%lld/%d=%1.3f})"
+ "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: waveform matching disabled by defaults write"
+ "<<<< FigVenueDescriptionMetadataSupplier >>>> %s: [%p|%{public}@]: updateResourcesAndTransferMetadata failed %d"
+ "<<<< FigVideoContainerLayer >>>> %s: _createAndSetupVideoReceiverWithDeferredTransaction failed with error %d"
+ "<<<< FigVirtualDisplayProcessor >>>>%@ %s: stats/sec: |%@"
+ "<<<< HLSPersistentStore >>>> %s: [%p] Attempting to create new movpkg: %@"
+ "<<<< HLSPersistentStore >>>> %s: [%p] Found valid movpkg: %@"
+ "<<<< HLSPersistentStore >>>> %s: [%p] Successfully created new movpkg: %@"
+ "<<<< Warehouse RP >>>> %s: %{public}s (%p) gradualDecoderRefresh=%ld, gradualDecoderRefreshIsAuthoritative=%d"
+ "<<<< fbarprocessor >>>> %s: [%p] %{public}s Process TransitionID '%@' Last sbuf endtime %1.3f Cumulative sbuf endtime %1.3f, sbufStartTime %1.3f"
+ "<SEGPUMP> %s: NULL pump"
+ "<SEGPUMP> %s: NULL pump. Cannot determine TTR enablement status."
+ "<SEGPUMP> %s: NULL storeBagSessionConfig. Cannot determine TTR enablement status."
+ "<SEGPUMP> %s: NULL stream for streamIndex %ld"
+ "<SEGPUMP> %s: Unexpected mData retain count: %ld; expected 2. Segment %p"
+ "@\"CAShapeLayer\""
+ "Clears"
+ "Could not enable dirstats on root directory (does not exist)"
+ "Could not rename (does not exist)"
+ "Could not write out Boot.xml (does not exist)"
+ "Could not write out Root.xml (does not exist)"
+ "Could not write out StreamInfoRoot (file does not exist)"
+ "Could not write streamInfo (does not exist)"
+ "EditMentorSetModeToDoNothing_orderQueue"
+ "EditMentorSetModeToEmptyEdit_orderQueue"
+ "EditMentorSetModeToForwardPlayback_orderQueue"
+ "EditMentorSetModeToReversePlayback_orderQueue"
+ "EditMentorSetModeToScrub_orderQueue"
+ "EditMentorSetProperty_orderQueue"
+ "EncDrops"
+ "EncIdlDrops"
+ "EncQDrops"
+ "Encodes"
+ "FBPAKey_FakeFormatDescription"
+ "FigAudioQueueOfflineMixerStartDrainingSampleBuffers"
+ "File does not exist when writing boot"
+ "IdlEncodes"
+ "MovieHeaderMakerSetShouldAllow64BitDataOffsetInTrackRunAtom"
+ "NULL pointer within %s. pump: %@"
+ "Non CFString kFigFormatWriterProperty_64BitDataOffsetInTrackRunAtomPolicy."
+ "Root file does not exist"
+ "SinkODrops"
+ "Submits"
+ "TB,R,N"
+ "_DRMFallbackIconLayer"
+ "_checkIfRebuildIsRequiredWhileHoldingVideoTargetMutex"
+ "_createAndSetupVideoReceiverWithDeferredTransaction:"
+ "_createdForVideoReceiver"
+ "_videoTargetAndReceiverMutex"
+ "airplayRoute_audioSessionDisallowsVideo"
+ "com.apple.coremedia.editmentor"
+ "copyVideoReceiver"
+ "create temp dir failed (does not exist)"
+ "delete of boot file failed (does not exist)"
+ "editMentorChildMentorPrerollComplete_orderQueue"
+ "editMentorChildMentorStoppedDueToCompletion_orderQueue"
+ "editMentorChildMentorStoppedDueToError_orderQueue"
+ "editMentorForwardNotificationFromChildMentor_orderQueue"
+ "ensureLockFileIsOpen"
+ "favd_copySidebandVideoPropertiesArray"
+ "fbapspManager_HandlePendingSbufsOnSubPipeFinishCallback"
+ "fbapspManager_subPipeFinishedProcessingData_block_invoke"
+ "fim_DestroyAudioStream"
+ "fim_NewAudioStream"
+ "flock failed (does not exist)"
+ "flock failed (file does not exist)"
+ "flock of movpkg failed (does not exist)"
+ "fpfs_TrimBufferAtStartToTime"
+ "fpfs_getCachedAnchorTimeForItem"
+ "fpfsi_metricEventPublishVariantChangeOrVariantChangeStartEvent"
+ "fpiCurrentEventChangePrimaryPlaybackState"
+ "fpic_applyAutomaticLegibleMediaSelectionForAllItems"
+ "fpic_createAutomaticLegibleMediaSelectionArray"
+ "funlock failed (does not exist)"
+ "funlock failed (file does not exist)"
+ "i24@0:8^{OpaqueFigDeferredTransaction=}16"
+ "invalidTimeDict allocation failed"
+ "kFigBytePumpError_AlternateInPenaltyBox"
+ "kFigFilePlatformError_DoesNotExist"
+ "lockLockFile"
+ "media request already cancelled"
+ "media request custom URL request IDs do not match"
+ "media type is invalid"
+ "movpkg file does not exist"
+ "mrdowc-handler"
+ "mrdowc_handleNotificationAsync"
+ "overlapEndTimeDict allocation failed"
+ "playlist does not exist)"
+ "radar_153096490_TTREnabled"
+ "rebuild"
+ "recursive delete failed (does not exist)"
+ "rename failed (does not exist)"
+ "requiresRebuild"
+ "segPumpSentEndCallbackForAnyStreamHandleTTR"
+ "set64BitDataOffsetInTrackRunAtomPolicy"
+ "setAllowsEdgeAntialiasing:"
+ "setFillColor:"
+ "setPath:"
+ "shouldSyncAudioByMatchingWaveform"
+ "stream info does not exist"
+ "subaq_getCurrentQueueTime"
+ "temp dir does not exist"
+ "unlockLockFileAndClose"
+ "unlockRoot"
+ "unlockRootAndClose"
- "\nrelease CAPackage: %@"
- "-[FigBaseCALayer dealloc]"
- "-[FigBaseCALayer enableDRMFallback]_block_invoke"
- "-[FigVideoContainerLayer _createAndSetupVideoReceiver]"
- ".caar"
- "<<< FFR_Movie >>> %s: \t\t\t    DataOffset:             %d"
- "<<<< FAQ >>>> %s: [%p:%p] %{public}s FigAudioQueueTimingShimGetCurrentTime -> timeStamp.mSampleTime %lld, faq->srcASBD->mSampleRate %d"
- "<<<< FAQ >>>> %s: [%p:%p] calling AudioQueueEnqueueBuffer(%p), originalPTS = %.3f, duration = %.3f, mAudioDataByteSize = %u, mAudioDataBytesCapacity = %u\t(trim %d frames at start, %d frames at end)"
- "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s called. Run: %d AQStarted: %d HighWater: %d LowWater: %d Discard: %d Interrupt: %d"
- "<<<< FAQ Offline Mixer >>>> %s: [%p] %{public}s returning. Run: %d AQStarted: %d HighWater: %d LowWater: %d Discard: %d Interrupt: %d Processed: %.3f [%.3f:%.3f] (%d sample buffers)"
- "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStart(%p)"
- "<<<< FAQ TIMING SHIM >>>> %s: [%p] Calling AudioQueueStartWithFlags(%p, 0x%x)"
- "<<<< FAQRP >>>> %s: (%p %{public}s) timebase %p effective rate changed, new rate %1.3f"
- "<<<< FIM >>>> %s: initializing track of type  %c%c%c%c"
- "<<<< FigBaseCALayer >>>> %s: FigCreateDRMFallbackCAPackage failed"
- "<<<< FigBaseCALayer >>>> %s: cannot find DRM Fallback icon"
- "<<<< FigBaseCALayer >>>> %s: fileURLWithPath failed"
- "<<<< FigBaseCALayer >>>> %s: packageWithContentsOfURL failed with %d"
- "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s Data %s flow to subPipe. pipelineRateIsValid=%s, subPipeTerminationInFlight=%s, currentSubPipe=%p"
- "<<<< FigBufferedAirPlaySubPipeManager >>>> %s: [%p] %{public}s SendPendingSbufOnSubPipeFinished. Found FlushRangeEnd %@ "
- "<<<< FigPlayerOverlap >>>> %s: <%p|%{public}s> end time is %1.3f"
- "<<<< FigPlayerOverlap >>>> %s: copy end time failed"
- "<<<< FigPlayerOverlap >>>> %s: end time dictionaty is null"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Applied a forwardEndTime on track %d at %{public}@, now %g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Attempting to apply a forward end time at L3 %{public}@, now L2 %g (L3 %g)"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Created manifold[%i] with type - manifoldType: %{public}@"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: ILLEGAL STATE CHANGE: track %ld (state %d) with invalid timeOffset asked to change to %d. Resetting to INIT (0)."
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: Sample buffer ignored for track %d with invalid timeOffset, startTime %f, raw %f, discDomain %d, cachedPumpTime %f"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: WARNING: found track %d already in state %d, not adjusting the timeOffset - it may be out of sync"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: audio track %d priming duration %1.5g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: cannot set Properties at transistion %d"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: deferring timeOffset determination for sparse track %d"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: first sample of track %d is %1.5g, startTime is %1.5g, timeOffset is %1.7g, raw: %1.7g, discDomain %d %s"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: found timeshift while changing gears %lld %u (%1.4g)"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: item2 zero is raw %g, so t maps to %g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: lastplaying is %d"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: locking track %ld to audio (%1.5g)"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: must reset pumpOffset anchor: drift=%1.5g, pumpTime=%1.5g, timebase=%1.5g, oldAnchor timebase=%1.5g, pump=%1.5g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: new pumpOffset %1.5g, now %1.5g, dataStart %1.5g, pts %1.5g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: shifting track %d by %g - changing its first sample from %1.5g to %1.5g, timeOffset from %f to %f"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d abandoned sync before getting timeOffset - harvested %g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d inheriting cached timeOffset"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d requires timeOffset fix-up to %1.5g; start at %1.5g"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d start time is %g, gets timeOffset %f from track %d, first sample is %f, raw: %f %s"
- "<<<< FigStreamPlayer >>>> %s: [%p|%{public}s] <%p|%{public}s>: track %d timeOffset cannot be set from previous track - set to %g so sbuf lands at startTime"
- "<<<< FigStreamPlayer >>>> %s: trim %g from %g to %g"
- "<<<< FigStreamPlayer >>>> %s: trim %g from %g to %g,Adjust output PTS from %g to %g"
- "<<<< FigVirtualDisplayProcessor >>>>%@ %s: %s/sec: %d"
- "<<<< fbarprocessor >>>> %s: [%p] %{public}s Process TransitionID '%@' Last sbuf endtime %1.3f Cumulative sbuf endtime %1.3f"
- "@\"CAPackage\""
- "BytesSent"
- "ClearScreens"
- "EditMentorSetModeToDoNothing"
- "EditMentorSetModeToEmptyEdit"
- "EditMentorSetModeToForwardPlayback"
- "EditMentorSetModeToReversePlayback"
- "EditMentorSetModeToScrub"
- "EditMentorSetProperty"
- "EncoderDrops"
- "EncoderIdleDrops"
- "EncoderQueueDrops"
- "FBLSupportAppendDeferredTransactionChangeToRemoveCAPackageFromSuperLayerAndReleaseIt"
- "FigDRMFallbackCAPackage"
- "FrameEncodes"
- "FrameSubmits"
- "IdleFrameEncodes"
- "NULL pointer within %s. pump: %@, stream: %@, streamIndex: %d"
- "SinkOverflowDrops"
- "T^{OpaqueFigVideoReceiver=},R,N"
- "_DRMFallbackIconPackage"
- "_createAndSetupVideoReceiver"
- "com.apple.coremedia.editmentor.notification"
- "connectionHelper is no longer valid"
- "editMentorChildMentorPrerollComplete"
- "editMentorChildMentorStoppedDueToCompletion"
- "editMentorChildMentorStoppedDueToError"
- "editMentorForwardNotificationFromChildMentor"
- "editMentorSetModeChangePolicyToPreservePreviousOutput"
- "favd_copyFormatDescriptionToSidebandVideoPropertiesLookupIDMappingCommon"
- "favd_copySidebandVideoPropertiesArrayCommon"
- "fbapspManager_SendPendingSbufOnSubPipeFinished"
- "fileURLWithPath:isDirectory:"
- "fim_NewAudioTrack"
- "invalidated during FigAudioSession set rate"
- "itemoverlap_getEndTime"
- "mrdowc_streamingCacheNotificationHandler"
- "packageWithContentsOfURL:type:options:error:"
- "pathForResource:ofType:"
- "rootLayer"
- "videoReceiver"

```
