## MediaToolbox

> `/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`

```diff

-3175.4.1.0.0
-  __TEXT.__text: 0xf4a098
-  __TEXT.__auth_stubs: 0xbaf0
+3175.6.2.11.2
+  __TEXT.__text: 0xf4ecec
+  __TEXT.__auth_stubs: 0xbb20
   __TEXT.__objc_methlist: 0x1cb0
-  __TEXT.__cstring: 0x1153ec
-  __TEXT.__const: 0x55630
-  __TEXT.__oslogstring: 0x12746f
+  __TEXT.__cstring: 0x115963
+  __TEXT.__const: 0x557a0
+  __TEXT.__oslogstring: 0x128896
   __TEXT.__ustring: 0x1f8
   __TEXT.__gcc_except_tab: 0x135c
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x11640
+  __TEXT.__unwind_info: 0x11668
   __TEXT.__eh_frame: 0x4458
   __TEXT.__objc_classname: 0x7ee
   __TEXT.__objc_methname: 0x5cf8
   __TEXT.__objc_methtype: 0x247d
   __TEXT.__objc_stubs: 0x56e0
-  __DATA_CONST.__got: 0x3500
-  __DATA_CONST.__const: 0x213d8
+  __DATA_CONST.__got: 0x34f8
+  __DATA_CONST.__const: 0x21508
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x5d90
+  __AUTH_CONST.__auth_got: 0x5da8
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x3e078
-  __AUTH_CONST.__cfstring: 0x4f760
+  __AUTH_CONST.__const: 0x3e098
+  __AUTH_CONST.__cfstring: 0x4f900
   __AUTH_CONST.__objc_const: 0x52c8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0xae0
   __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x18400
-  __DATA.__bss: 0x3858
+  __DATA.__bss: 0x3848
   __DATA.__common: 0x2e89
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x240

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 23424
-  Symbols:   33476
-  CStrings:  52446
+  Functions: 23436
+  Symbols:   33518
+  CStrings:  52536
 
Symbols:
+ _kFigAudioRenderPipelineProperty_CinematicAudioParameters
+ _kFigSampleBufferAudioRendererAudioCurvesKey_RecordingLoudness
+ _kFigAudioCurvesKey_AmbienceLoudness
+ _kFigAssetReaderSourceTrackArrayKey_CinematicAudioParameters
+ _kFigSampleBufferAudioRendererAudioCurvesKey_DialogMixBias
+ _kFigAudioQueueProperty_CinematicAudioParameters
+ _FigAudioFormatDescriptionGetCinematicAudioEffectEligibility
+ _kFigSampleBufferAudioRendererAudioCurvesKey_DialogLevel
+ _AudioConverterFillComplexBufferWithPacketDependencyInfo
+ _CFStringGetMaximumSizeOfFileSystemRepresentation
+ _CMAudioFormatDescriptionGetMostCompatibleFormatAndChannelLayout
+ _kFigAudioCurvesKey_DialogMixBias
+ _kFigAudioQueueAudioCurvesKey_RecordingLoudness
+ _kFigSampleBufferAudioRendererAudioCurvesKey_DialogLoudness
+ _kFigAudioQueueAudioCurvesKey_AmbienceLevel
+ _kFigAudioCurvesKey_DialogLevel
+ _FigAudioStreamPacketDependencyInfoCopyAsSampleDependencyAttributeDictionary
+ _kFigPlaybackItemTrackProperty_CinematicAudioParameters
+ _kFigAudioQueueAudioCurvesKey_AmbienceLoudness
+ _FigContentKeySpecifierGetCryptKeySize
+ _kFigSampleBufferAudioRendererAudioCurvesKey_AmbienceLoudness
+ _kFigSampleBufferAudioRendererAudioCurvesKey_AmbienceLevel
+ _kFigAudioCurvesKey_RenderingStyle
+ _kFigRemakerAudioMixdown_CinematicAudioParameters
+ _FigContentKeySpecifierGetCryptBlockSize
+ _kFigSampleBufferAudioRendererAudioCurvesKey_RenderingStyle
+ _kFigAudioCurvesKey_DialogLoudness
+ _kFigAudioCurvesKey_RecordingLoudness
+ _kFigAudioQueueAudioCurvesKey_DialogLoudness
+ _kFigBufferedAirPlayAudioChainSubPipeProperty_CurrentFormatDescription
+ _kFigAssetExportSessionPresetICPLHighFPSHEVC1920x1920WithHDR
+ _kFigAudioCurvesKey_AmbienceLevel
+ _kFigAudioQueueAudioCurvesKey_DialogLevel
+ _kFigAudioQueueAudioCurvesKey_RenderingStyle
+ _kFigAudioQueueAudioCurvesKey_DialogMixBias
- _kFigMemoryRecipientNotification_ServerDied
- _FigMemoryOriginGetObjectID
- _FigMemoryOriginServerCopyMemoryOriginForObjectID
CStrings:
+ "can only copy Cinematic Audio parameters on an audio track"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!p(MISSING) %!{(MISSING)public}s re-evaluate auto selection criterion based on audio curves"
+ "CurrentFormatDescription"
+ "<<<< FAQ >>>> %!s(MISSING): FigAudioQueueTimingShimSetProperty(CinematicAudioEnabled) returned %!d(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): begin schedule %!d(MISSING) parameters"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): player %!p(MISSING) %!{(MISSING)public}s auto selection defaults changed, re-apply auto selection to item %!p(MISSING) %!{(MISSING)public}s"
+ "<<<< FAQ >>>> %!s(MISSING): FigAudioQueueTimingShimSetProperty(CinematicAudioEnabled)"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicAmbienceLevel (%!f(MISSING)) err=%!d(MISSING)"
+ "videoMentorFrameNodeAddDependentNode"
+ "<<<< FAC >>>> %!s(MISSING): Unable to set the kAudioCodecPrivatePropertyEnableGlobalPostProcessingReverb property either because of an error (possibly not supported), it is the wrong size or it is not writable, err: %!d(MISSING), propertySize: %!d(MISSING) vs %!d(MISSING), isPropertyWritable: %!@(MISSING)"
+ "bad format in destASBD"
+ "<<<< FigBufferedAirPlaySubPipeManagerForRenderPipeline >>>> %!s(MISSING): [%!p(MISSING)] %!{(MISSING)public}s not checking for subpipetype for emptyMedia"
+ "<<<< FAQ >>>> %!s(MISSING): [%!p(MISSING):%!p(MISSING)] Set Cinematic Audio parameters on audio queue:[%!p(MISSING) )"
+ "AssetReaderSource_CinematicAudioParameters"
+ "<<<< VideoMentor >>>> %!s(MISSING): Unexpected VideoMentor state in mediaplaybackd (err = %!d(MISSING)): %!s(MISSING) handles %!d(MISSING) dependent nodes and analyses %!d(MISSING) nodes on stack."
+ "Unexpected 'cnpm' atom version (should be 0)"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicAudioRecordingLoudness (%!f(MISSING)) err=%!d(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): Transferring reporting agent to pump %!p(MISSING)"
+ "Parameter atom structure is incorrect"
+ "Invalid header atom size for 'cnhd' atom"
+ "kCMSampleBufferError_RequiredParameterMissing"
+ "<< FramePrefetcher >> %!s(MISSING):  %!p(MISSING): Created the reporting agent with error %!d(MISSING), %!p(MISSING)"
+ "AudioCurves_DialogMixBias"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): called"
+ "<<<< FAC >>>> %!s(MISSING): set input and output channel layouts"
+ "parseCinematicAudioHeaderAtom"
+ "<<<< FAQ >>>> %!s(MISSING): do not enable spatialization for a destination with spatial channel layout"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): Audio track ID %!d(MISSING) needed for Cinematic Audio effect"
+ "<<<< FAC >>>> %!s(MISSING): kAudioCodecPrivatePropertyASPFrequency: %!d(MISSING)"
+ "subaq_setCinematicAudioBulkParameters"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicAudioDialogLoudness (%!f(MISSING)) err=%!d(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): starting run %!d(MISSING) at cadence %!g(MISSING)"
+ "Could not create dispatch source"
+ "AudioCurves_AmbienceLevel"
+ "<<<< FSAC >>>> %!s(MISSING): [%!p(MISSING)] set property %!@(MISSING): value is the same as current, do nothing."
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!{(MISSING)public}s set itemTrackStorage->audio.cinematicAudioParameters=%!@(MISSING)"
+ "<<<< FigStreamPlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s>: setup finished with error %!d(MISSING)"
+ "Could not create weak reference holder"
+ "AudioCurves_DialogLevel"
+ "bad Cinematic Audio parameters"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!p(MISSING) %!{(MISSING)public}s re-evaluate auto selection criterion based on cinematic audio parameters"
+ "<<<< FAC >>>> %!s(MISSING): Setting the kAudioCodecPrivatePropertyEnableGlobalPostProcessingReverb property failed: nonFatalErr: %!d(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): got duration %!g(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!p(MISSING) %!{(MISSING)public}s Defer set cinematic audio parameters because no renderPipeline"
+ "Invalid parameters atom size for 'cnhd' atom"
+ "<<<< VideoCompositionProcessor >>>> %!s(MISSING): numberOfSourceFramesWithSceneLux: %!d(MISSING). We should not have more than one source track with scene lux."
+ "<<<< FigVideoQueueServer >>>> %!s(MISSING): App is in BackgroundRunning state and FVQ detected ImageQueue not being serviced for 10 seconds. invalidating video queue [%!p(MISSING) : %!p(MISSING)]"
+ "parseCinematicAudioParametersAtom"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicAudioRecordingStyle (%!f(MISSING)) err=%!d(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): step %!d(MISSING) from %!g(MISSING) to %!g(MISSING), interval %!f(MISSING)"
+ "subaq_ensureCinematicAudioEnabled"
+ "<<<< FAC >>>> %!s(MISSING): AudioConverterSetProperty / kAudioCodecPrivatePropertyASPFrequency failed, err: %!d(MISSING)"
+ "AudioCurves_DialogLoudness"
+ "Already servicing a step request"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!p(MISSING) %!{(MISSING)public}s Assigning new Cinematic Audio parameters to track ID %!d(MISSING) with render pipeline %!@(MISSING), may disturb playback %!d(MISSING)"
+ "AudioCurves_RecordingLoudness"
+ "CinematicAudioParameters"
+ "Could not allocate context->parameters"
+ "<<<< FAQ >>>> %!s(MISSING): [%!p(MISSING):%!p(MISSING)] Cinematic Audio parameters is not CFData"
+ "sample dependency attributes for an audio format that requires them are missing"
+ "RemakerAudioMixdown_CinematicAudioParameters"
+ "<<<< FAC >>>> %!s(MISSING): Calling AudioConverterFillComplexBufferWithPacketDependencyInfo for %!d(MISSING) packets"
+ "<<<< FAC >>>> %!s(MISSING): kAudioCodecPropertyDynamicRangeControlConfig: %!d(MISSING)"
+ "<<<< FAC >>>> %!s(MISSING): kAudioCodecPrivatePropertyContentSource: %!d(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): player %!p(MISSING):%!{(MISSING)public}s received SelectionCriteriaChanged for item %!{(MISSING)public}s"
+ "<<<< FAQ >>>> %!s(MISSING): Track is eligible for Cinematic Audio processing"
+ "playerfig_dispatchAsyncAutoSelectionCriteriaChangedForItem"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): Skipping set because old and new parameters are the same. Old: %!@(MISSING), New: %!@(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s> Reuse metadata pipeline %!p(MISSING) for track %!d(MISSING) to be collected"
+ "AudioCurves_AmbienceLoudness"
+ "AudioConverterSetProperty / kAudioConverterOutputChannelLayout failed"
+ "<<<< FAQ >>>> %!s(MISSING): Deferring (CinematicAudioEnabled)"
+ "<<<< FAQ >>>> %!s(MISSING): pre subaq_ensureCinematicAudioEnabled() eager"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicRemixAmount (%!f(MISSING)) err=%!d(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicAudioAmbienceLoudness (%!f(MISSING)) err=%!d(MISSING)"
+ "kFigAudioQueueError_InvalidPropertyStructure"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): I-frame prefetch COMPLETED%!s(MISSING). TotalCachedSize = %!l(MISSING)d; TotalCachedCount = %!l(MISSING)d; Error = %!d(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): received i-frame %!d(MISSING) for %!g(MISSING)"
+ "fpfsi_IFramePrefetchCompleted"
+ "can only set Cinematic Audio parameters on an audio track"
+ "com.apple.coreaudio.allow-apac-codec"
+ "<<<< FAQ >>>> %!s(MISSING): fig_kAudioQueueParam_CinematicDialogLevel (%!f(MISSING)) err=%!d(MISSING)"
+ "Invalid 'cnhd' atom size"
+ "Invalid 'cnpm' atom size"
+ "<<<< FAC >>>> %!s(MISSING): Fatal: sample dependency attributes for an audio format that requires them are absent; FigAudioStreamPacketDependencyInfoCopyAsSampleDependencyAttributeDictionary returned %!d(MISSING)"
+ "<<<< FigVideoQueueServer >>>> %!s(MISSING): app state is background running.  setting a 10 second timer to check if app becomes suspended, in which case we will invalidate the video queue [%!p(MISSING) : %!p(MISSING)]"
+ "<<<< FAQ >>>> %!s(MISSING): enable spatialization as source has spatial channel layout, destination does not"
+ "com.apple.coremedia.videoqueue.timer"
+ "<<<< FAQ >>>> %!s(MISSING): pre subaq_ensureCinematicAudioEnabled() not eager"
+ "Null kFigRenderPipelineProperty_SourceSampleBufferQueue when try to resuse render pipeline"
+ "AVAssetExportPresetICPLHighFPSHEVC1920x1920WithHDR"
+ "<<<< VideoMentor >>>> %!s(MISSING): Cannot add the same node as a dependent"
+ "itemfig_autoSelectionCriteriaChangedForItemAsync"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): culling track ID %!d(MISSING) as non playable: (Atmos:%!d(MISSING), Enhanced AC-3:%!d(MISSING), AC-3:%!d(MISSING), APAC:%!d(MISSING), Cinematic Audio prepared:%!d(MISSING))"
+ "<<<< FAQ >>>> %!s(MISSING): hasCinematicAudioBeenEnabled is now true"
+ "failed to convert version list to C string"
+ "subaq_scheduleCinematicForMediaTimeRange"
+ "<<<< FigExportCommmon >>>> %!s(MISSING): (%!p(MISSING)) trackID %!d(MISSING) cinematic audio parameters %!p(MISSING)"
+ "videoQueueServer_makeWrapperForVideoQueueInternal_block_invoke_2"
+ "<<<< FAQ >>>> %!s(MISSING): AudioQueue not enabled for Cinematic Audio, returned %!d(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): [%!p(MISSING)|%!{(MISSING)public}s] <%!p(MISSING)|%!{(MISSING)public}s> Created metadata pipeline %!p(MISSING) for track %!d(MISSING) to be collected"
+ "fvcp_pendingFrame_prepareSceneLuxToPropagate"
+ "<<<< FAC >>>> %!s(MISSING): Set kAudioCodecPrivatePropertyEnableGlobalPostProcessingReverb to %!@(MISSING)"
+ "<<<< FAC >>>> %!s(MISSING): Unable to set codec property %!@(MISSING), err: %!d(MISSING), isWritable: %!d(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): cinematicAudioEnabled is not enabled"
+ "<<<< FAQ >>>> %!s(MISSING): schedule cinematic"
+ "Unexpected 'cnhd' atom version (should be 0)"
+ "<<<< FAC >>>> %!s(MISSING): AudioConverterSetProperty / kAudioCodecPrivatePropertyContentSource failed, err: %!d(MISSING)"
+ "<<<< FAC >>>> %!s(MISSING): AudioConverterSetProperty / kAudioCodecPropertyDynamicRangeControlConfig failed, err: %!d(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): post subaq_ensureCinematicAudioEnabled() not eager"
+ "itemfig_isTrackForcingCinematicAudioEffect"
+ "Can't step without having learned duration"
+ "<<<< FAQ >>>> %!s(MISSING): post subaq_ensureCinematicAudioEnabled() eager"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): got pump %!p(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): parameter[%!d(MISSING)]='%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'(%!d(MISSING)) (%!f(MISSING)) err=%!d(MISSING)"
+ "<<<< FigFilePlayer >>>> %!s(MISSING): %!p(MISSING) %!{(MISSING)public}s Set property \"%!@(MISSING)\" on audio track ID %!d(MISSING). New value: %!@(MISSING), old value: %!@(MISSING)"
+ " WITH ERROR"
+ "<<<< FAC >>>> %!s(MISSING): Fatal: AudioConverterFillComplexBufferWithPacketDependencyInfo returned %!d(MISSING)"
+ "AudioCurves_RenderingStyle"
+ "<<<< FigBufferedAirPlaySubPipeManagerForRenderPipeline >>>> %!s(MISSING): [%!p(MISSING)] %!{(MISSING)public}s The current subPipe(%!p(MISSING)) for sbuf is different from the required subPipe, or the transport requires a new sub-pipe.  configurePassthroughMode=%!c(MISSING). baoSupportsPassthrough=%!c(MISSING). rateSupportsPassthrough=%!c(MISSING) (pipelineRate=%!f(MISSING)). transportRequiresSubPipeChange=%!c(MISSING), sourceFormatDescriptionChanged=%!c(MISSING) baoSupportsReceiverSideSoundCheck=%!c(MISSING). baoSupportsDecryption=%!c(MISSING). audioTap=%!p(MISSING) PTS=%!f(MISSING). OPTS=%!f(MISSING) contentFormatDescription=%!@(MISSING)"
+ "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING): deactivated. No prefetcher is now active"
+ "CinematicAudioParametersChanged"
+ "<<<< FAQ >>>> %!s(MISSING): end schedule %!d(MISSING) parameters"
+ "<<<< FAQ >>>> %!s(MISSING): (%!p(MISSING)) current (possibly dynamic) latency: %!f(MISSING)"
+ "<<<< FAQ >>>> %!s(MISSING): (%!p(MISSING)) failed to retrieve dynamic latency, return default 0"
- "<< FramePrefetcher >> %!s(MISSING): Created the reporting agent with error %!d(MISSING), %!p(MISSING)"
- "CreateRemoteSampleGenerator"
- "<<<< VideoMentor >>>> %!s(MISSING): Unexpected VideoMentor state in mediaplaybackd (err = %!d(MISSING)): %!s(MISSING) handles %!d(MISSING) dependent nodes."
- "sampleBufferGenerator_disposeConnectionRefcon"
- "FigCryptGetKeySize"
- "<< FSGRemoteXPC >> %!s(MISSING): Forgetting memoryRecipient %!p(MISSING)"
- "<< FramePrefetcher >> %!s(MISSING): step %!d(MISSING) from %!g(MISSING) to %!g(MISSING), interval %!f(MISSING)"
- "<< FramePrefetcher >> %!s(MISSING): %!p(MISSING) got duration %!g(MISSING)"
- "<<<< FigFilePlayer >>>> %!s(MISSING): culling track ID %!d(MISSING) as non playable: (Atmos:%!d(MISSING), Enhanced AC-3:%!d(MISSING), AC-3:%!d(MISSING), APAC:%!d(MISSING))"
- "MemoryRecipient was NULL"
- "SampleGeneratorServerConnectionRefcon NULL"
- "sampleBufferGenerator_setupMemoryOrigin"
- "HandleSampleGeneratorEstablishMemoryRecipient2"
- "<< FramePrefetcher >> %!s(MISSING): received i-frame %!d(MISSING) for %!g(MISSING)"
- "<<<< FigBufferedAirPlaySubPipeManagerForRenderPipeline >>>> %!s(MISSING): [%!p(MISSING)] %!{(MISSING)public}s The current subPipe(%!p(MISSING)) for sbuf is different from the required subPipe, or the transport requires a new sub-pipe.  configurePassthroughMode=%!c(MISSING). baoSupportsPassthrough=%!c(MISSING). rateSupportsPassthrough=%!c(MISSING) (pipelineRate=%!f(MISSING)). transportRequiresSubPipeChange=%!c(MISSING), baoSupportsReceiverSideSoundCheck=%!c(MISSING). baoSupportsDecryption=%!c(MISSING). audioTap=%!p(MISSING) PTS=%!f(MISSING). OPTS=%!f(MISSING) contentFormatDescription=%!@(MISSING)"
- "<SEGPUMP> %!s(MISSING): %!{(MISSING)public}@: haven't received a media playlist yet - assume we will be able to continue without a gap"
- "<< FigSampleGeneratorXPCServer >> %!s(MISSING): Established MemoryOrigin == (%!l(MISSING)lx) -> %!p(MISSING)"
- "MemoryOriginServer indicated memoryOrigin is bad"
- "existing discoInfoQueueCount is 0"
- "<SEGPUMP> %!s(MISSING): %!{(MISSING)public}@:%!l(MISSING)d: Refresh index immediately since network connection comes back up"
- "Invalid MemoryOriginObjectID."
- "<< FramePrefetcher >> %!s(MISSING): called %!@(MISSING)"
- "<< FramePrefetcher >> %!s(MISSING): starting run %!d(MISSING) at cadence %!g(MISSING)"
- "<< FigSampleGeneratorXPCServer >> %!s(MISSING): MemoryOrigin (%!p(MISSING)/%!l(MISSING)lx)"
- "<< FSGRemoteXPC >> %!s(MISSING): Setting memoryRecipient %!p(MISSING) into storage %!p(MISSING)"
- "HandleSampleGeneratorEstablishMemoryRecipient1"
- "<< FramePrefetcher >> %!s(MISSING): Deactivated %!p(MISSING). No prefetcher is now active"
- "MemoryOriginObjectID could not be obtained, as SampleGeneratorServerConnectionRefcon is NULL"
- "<< FramePrefetcher >> %!s(MISSING): Transferring reporting agent from framePrefetcher %!p(MISSING) to pump %!p(MISSING)"
- "remoteSampleGenerator_memoryRecipientDeathNotificationHandler"
- "segPumpGetIndexFileRefreshTimestamp"
- "<< FramePrefetcher >> %!s(MISSING): i-frame prefetch halted abnormally with error %!d(MISSING)"
- "<< FramePrefetcher >> %!s(MISSING): completed; totalCachedSize %!l(MISSING)d, totalCachedCount %!l(MISSING)d"
- "<< FSGRemoteXPC >> %!s(MISSING): Heard %!@(MISSING) from memoryRecipient %!p(MISSING)"
- "<<<< FigFilePlayer >>>> %!s(MISSING): Building Timed Metadata Pipeline for track %!l(MISSING)d of type %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)"

```
