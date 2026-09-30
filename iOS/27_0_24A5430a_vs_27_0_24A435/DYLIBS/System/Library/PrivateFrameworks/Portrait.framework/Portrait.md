## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

 560.22.2.0.0
-  __TEXT.__text: 0x88b78
+  __TEXT.__text: 0x985a0
   __TEXT.__delay_helper: 0x264
-  __TEXT.__objc_methlist: 0x936c
-  __TEXT.__const: 0x20a70
-  __TEXT.__cstring: 0x4e42
-  __TEXT.__oslogstring: 0x4b9a
-  __TEXT.__gcc_except_tab: 0x19e0
+  __TEXT.__objc_methlist: 0xa0c4
+  __TEXT.__const: 0x20b00
+  __TEXT.__cstring: 0x52dd
+  __TEXT.__oslogstring: 0x5e30
+  __TEXT.__gcc_except_tab: 0x1af4
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x1e98
+  __TEXT.__unwind_info: 0x21a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x918
-  __DATA_CONST.__objc_classlist: 0x518
+  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ec8
+  __DATA_CONST.__objc_selrefs: 0x5548
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x498
-  __DATA_CONST.__objc_arraydata: 0x718
-  __DATA_CONST.__got: 0x820
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0x1c670
-  __AUTH_CONST.__objc_intobj: 0xa98
+  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_arraydata: 0x758
+  __DATA_CONST.__got: 0x8b8
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x50a0
+  __AUTH_CONST.__objc_const: 0x1e5a8
+  __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x1778
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x1918
   __DATA.__data: 0x7b0
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3718
-  Symbols:   8429
-  CStrings:  1385
+  Functions: 4109
+  Symbols:   9145
+  CStrings:  1518
 
Symbols:
+ +[PTCinematographyDetection(Private) _setFocusDistancesOfDetections:disparityBuffer:priorDetections:]
+ +[PTCinematographyPostcaptureRefinement maximumLookaheadDurationSecondsForFrameRate:]
+ +[PTCinematographyPostcaptureRefinement maximumLookaheadDuration]
+ +[PTCinematographyScriptFocusData(Serialization) objectFromAtomStream:]
+ +[PTCinematographyScriptFocusData(Serialization) registerForSerialization]
+ +[PTCinematographyScriptSnapshot(Private) _generationOfDictionaryRepresentation:]
+ +[PTMonocularDisparityNetworkManager keepInstanceAlive:forSeconds:]
+ +[PTMonocularDisparityNetworkManager managerForSettings:downloadTimeout:initializationCallback:]
+ +[PTMonocularDisparityNetworkManager networkDimensionsForSettings:]
+ +[PTMonocularDisparityNetworkManager networkVariantForInputSource:renderVersion:]
+ +[PTMonocularDisparityProvider defaultRenderingMetadataWithRenderVersion:]
+ +[PTMonocularDisparityProvider disparitySettingsCacheKey:]
+ +[PTMonocularDisparityProvider disparitySizeForSettings:]
+ +[PTMonocularDisparityProvider isSupported]
+ +[PTMonocularDisparityProvider prewarmForCameraCaptured]
+ +[PTMonocularDisparityProvider resourceStatusCache]
+ +[PTMonocularDisparityProvider resourceStatusForSettings:]
+ -[PTCinematographyFocusDisparitySampler .cxx_destruct]
+ -[PTCinematographyFocusDisparitySampler computeFocusDisparityForAllDetections]
+ -[PTCinematographyFocusDisparitySampler focusDisparityForFrame:disparityBuffer:]
+ -[PTCinematographyFocusDisparitySampler init]
+ -[PTCinematographyFocusDisparitySampler setComputeFocusDisparityForAllDetections:]
+ -[PTCinematographyFocusDistanceTrack .cxx_destruct]
+ -[PTCinematographyFocusDistanceTrack focusDistanceAtTime:]
+ -[PTCinematographyFocusDistanceTrack focusDistances]
+ -[PTCinematographyFocusDistanceTrack initWithTimeline:focusDistances:startTime:]
+ -[PTCinematographyFocusDistanceTrack setFocusDistances:]
+ -[PTCinematographyFocusDistanceTrack setStartTime:]
+ -[PTCinematographyFocusDistanceTrack setTimeline:]
+ -[PTCinematographyFocusDistanceTrack startTime]
+ -[PTCinematographyFocusDistanceTrack timeline]
+ -[PTCinematographyFrame _focalLenIn35mmFilm]
+ -[PTCinematographyFrame focalLenIn35mmFilm]
+ -[PTCinematographyFrame setFocalLenIn35mmFilm:]
+ -[PTCinematographyFrame set_focalLenIn35mmFilm:]
+ -[PTCinematographyFrame(Private) _hasFocusDistances]
+ -[PTCinematographyFrame(Private) _setFocusDistancesUsingDisparityBuffer:priorFrame:]
+ -[PTCinematographyFrameFocusDistancesAccumulator .cxx_destruct]
+ -[PTCinematographyFrameFocusDistancesAccumulator addTime:focusDistance:]
+ -[PTCinematographyFrameFocusDistancesAccumulator finalizeFrameTrack]
+ -[PTCinematographyFrameFocusDistancesAccumulator focusDistances]
+ -[PTCinematographyFrameFocusDistancesAccumulator init]
+ -[PTCinematographyFrameFocusDistancesAccumulator setFocusDistances:]
+ -[PTCinematographyFrameFocusDistancesAccumulator setTimes:]
+ -[PTCinematographyFrameFocusDistancesAccumulator times]
+ -[PTCinematographyPostcaptureRefinement .cxx_destruct]
+ -[PTCinematographyPostcaptureRefinement _advanceToNextInputFrame]
+ -[PTCinematographyPostcaptureRefinement _currentInputFrame]
+ -[PTCinematographyPostcaptureRefinement _enforcePipelineBufferCapWithLatestInputTime:]
+ -[PTCinematographyPostcaptureRefinement _moveAvailableFramesFromSmootherToFocuser]
+ -[PTCinematographyPostcaptureRefinement _priorInputFrame]
+ -[PTCinematographyPostcaptureRefinement currentInputFrameIndex]
+ -[PTCinematographyPostcaptureRefinement deserializeState:]
+ -[PTCinematographyPostcaptureRefinement deserializeState:error:]
+ -[PTCinematographyPostcaptureRefinement endInputs]
+ -[PTCinematographyPostcaptureRefinement expectedInputTime]
+ -[PTCinematographyPostcaptureRefinement focuser]
+ -[PTCinematographyPostcaptureRefinement frames]
+ -[PTCinematographyPostcaptureRefinement generation]
+ -[PTCinematographyPostcaptureRefinement initWithScript:]
+ -[PTCinematographyPostcaptureRefinement initWithScript:samplesAllDetections:]
+ -[PTCinematographyPostcaptureRefinement inputsHaveBeenEnded]
+ -[PTCinematographyPostcaptureRefinement isInputExpected]
+ -[PTCinematographyPostcaptureRefinement isNextFrameAtEnd]
+ -[PTCinematographyPostcaptureRefinement isNextFrameAvailable]
+ -[PTCinematographyPostcaptureRefinement maximumPipelineBufferDuration]
+ -[PTCinematographyPostcaptureRefinement nextFrame]
+ -[PTCinematographyPostcaptureRefinement processNextDisparityBuffer:]
+ -[PTCinematographyPostcaptureRefinement serializeState:]
+ -[PTCinematographyPostcaptureRefinement serializeState]
+ -[PTCinematographyPostcaptureRefinement setCurrentInputFrameIndex:]
+ -[PTCinematographyPostcaptureRefinement setGeneration:]
+ -[PTCinematographyPostcaptureRefinement setInputsHaveBeenEnded:]
+ -[PTCinematographyPostcaptureRefinement setMaximumPipelineBufferDuration:]
+ -[PTCinematographyPostcaptureRefinement smoother]
+ -[PTCinematographyPostcaptureRefinement trackDecisions]
+ -[PTCinematographyRackFocusOptions fastRackStartTimeForDecisionTime:previousDecisionTime:]
+ -[PTCinematographyScript _disparityPixelBufferAtTime:]
+ -[PTCinematographyScript _ensureDisparityProvider]
+ -[PTCinematographyScript _frameBeforeFrame:]
+ -[PTCinematographyScript _frameBeforeTime:]
+ -[PTCinematographyScript _internalizeGenerationFromChangesDictionary:]
+ -[PTCinematographyScript _invalidateFocusDistancesInFrame:]
+ -[PTCinematographyScript _invalidateFocusDistancesInFrames:]
+ -[PTCinematographyScript _invalidateFocusDistancesOfDetectionsInFrame:]
+ -[PTCinematographyScript _monocularDisparityProviderSettingsForQuality:]
+ -[PTCinematographyScript _rackFocusDisparityForFrame:]
+ -[PTCinematographyScript _removeAvailableFramesFromFrameDetectionSmoother:]
+ -[PTCinematographyScript _setFocusDistancesAtTime:tolerance:usingDisparityBuffer:]
+ -[PTCinematographyScript _setRackFocusIfNeededForFrame:]
+ -[PTCinematographyScript _smoothDetectionsOfFramesInIndexRange:]
+ -[PTCinematographyScript _smoothDetectionsOfFramesInTimeRange:]
+ -[PTCinematographyScript _snapshot]
+ -[PTCinematographyScript _updateFastRackStartFocusDistancesAfterRemovingDecisionsAtOrderedTimes:]
+ -[PTCinematographyScript _updateFastRackStartIfNeededBeforeDecision:]
+ -[PTCinematographyScript _updateFastRackStartIfNeededBetweenDecision:previousDecision:]
+ -[PTCinematographyScript _updateFocusDistancesForAffectedDecisionsFromTime:originalNextDecision:]
+ -[PTCinematographyScript _updateFocusDistancesForFrame:priorFrame:]
+ -[PTCinematographyScript _updateFocusDistancesForFramesInIndexRange:]
+ -[PTCinematographyScript _updateFocusDistancesForFramesInTimeRange:]
+ -[PTCinematographyScript _updateFrameFocusDistancesAtTime:]
+ -[PTCinematographyScript _updateFrameFocusDistancesForDecision:]
+ -[PTCinematographyScript _updateFrameFocusDistancesForDecisions:indexRange:]
+ -[PTCinematographyScript _updateFrameFocusDistancesForDecisions:timeRange:]
+ -[PTCinematographyScript applyFocusData:]
+ -[PTCinematographyScript colorBufferProvider]
+ -[PTCinematographyScript disparityProvider]
+ -[PTCinematographyScript focusData]
+ -[PTCinematographyScript generation]
+ -[PTCinematographyScript loadWithAsset:changesDictionary:disparityProvider:completion:]
+ -[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]
+ -[PTCinematographyScript missingSomeFocusDistances]
+ -[PTCinematographyScript options]
+ -[PTCinematographyScript renderingGlobals]
+ -[PTCinematographyScript setColorBufferProvider:]
+ -[PTCinematographyScript setDisparityProvider:]
+ -[PTCinematographyScript setGeneration:]
+ -[PTCinematographyScript setMissingSomeFocusDistances:]
+ -[PTCinematographyScript setOptions:]
+ -[PTCinematographyScript setRenderingGlobals:]
+ -[PTCinematographyScript setVideoDimensions:]
+ -[PTCinematographyScript videoDimensions]
+ -[PTCinematographyScriptFocusData .cxx_destruct]
+ -[PTCinematographyScriptFocusData _initWithGeneration:frameTrack:tracks:]
+ -[PTCinematographyScriptFocusData dataRepresentation]
+ -[PTCinematographyScriptFocusData focusDistanceAtTime:]
+ -[PTCinematographyScriptFocusData focusDistanceAtTime:trackIdentifier:]
+ -[PTCinematographyScriptFocusData frameTrack]
+ -[PTCinematographyScriptFocusData generation]
+ -[PTCinematographyScriptFocusData initWithDataRepresentation:]
+ -[PTCinematographyScriptFocusData initWithFrames:generation:]
+ -[PTCinematographyScriptFocusData setFrameTrack:]
+ -[PTCinematographyScriptFocusData setGeneration:]
+ -[PTCinematographyScriptFocusData setTracks:]
+ -[PTCinematographyScriptFocusData tracks]
+ -[PTCinematographyScriptFocusData(Serialization) sizeOfSerializedObjectWithOptions:]
+ -[PTCinematographyScriptFocusData(Serialization) supportsVersion:]
+ -[PTCinematographyScriptFocusData(Serialization) writeToAtomWriter:options:]
+ -[PTCinematographyScriptFocusDataBuilder .cxx_destruct]
+ -[PTCinematographyScriptFocusDataBuilder addFrame:]
+ -[PTCinematographyScriptFocusDataBuilder finalFocusData]
+ -[PTCinematographyScriptFocusDataBuilder finalized]
+ -[PTCinematographyScriptFocusDataBuilder frameAccumulator]
+ -[PTCinematographyScriptFocusDataBuilder generation]
+ -[PTCinematographyScriptFocusDataBuilder initWithGeneration:]
+ -[PTCinematographyScriptFocusDataBuilder setFinalized:]
+ -[PTCinematographyScriptFocusDataBuilder setFrameAccumulator:]
+ -[PTCinematographyScriptFocusDataBuilder setGeneration:]
+ -[PTCinematographyScriptFocusDataBuilder setTrackAccumulators:]
+ -[PTCinematographyScriptFocusDataBuilder trackAccumulators]
+ -[PTCinematographyScriptOptions .cxx_destruct]
+ -[PTCinematographyScriptOptions copyWithZone:]
+ -[PTCinematographyScriptOptions disableDetectionSmoothing]
+ -[PTCinematographyScriptOptions disparityPrecompute]
+ -[PTCinematographyScriptOptions disparityProvider]
+ -[PTCinematographyScriptOptions downloadTimeout]
+ -[PTCinematographyScriptOptions fastPreview]
+ -[PTCinematographyScriptOptions forcePostCaptureCinematic]
+ -[PTCinematographyScriptOptions initWithScriptOptions:]
+ -[PTCinematographyScriptOptions init]
+ -[PTCinematographyScriptOptions mutableCopyWithZone:]
+ -[PTCinematographyScriptOptions overwriteRenderingVersion]
+ -[PTCinematographyScriptOptions postcaptureQuality]
+ -[PTCinematographyScriptOptions setDisableDetectionSmoothing:]
+ -[PTCinematographyScriptOptions setDisparityPrecompute:]
+ -[PTCinematographyScriptOptions setDisparityProvider:]
+ -[PTCinematographyScriptOptions setDownloadTimeout:]
+ -[PTCinematographyScriptOptions setFastPreview:]
+ -[PTCinematographyScriptOptions setForcePostCaptureCinematic:]
+ -[PTCinematographyScriptOptions setOverwriteRenderingVersion:]
+ -[PTCinematographyScriptOptions setPostcaptureQuality:]
+ -[PTCinematographyScriptOptions setTemporalFilteringEnabled:]
+ -[PTCinematographyScriptOptions temporalFilteringEnabled]
+ -[PTCinematographyScriptSnapshot .cxx_destruct]
+ -[PTCinematographyScriptSnapshot _createSmootherAndFocuser]
+ -[PTCinematographyScriptSnapshot _resetToFrameIndex:]
+ -[PTCinematographyScriptSnapshot currentFrameIndex]
+ -[PTCinematographyScriptSnapshot focusDetections]
+ -[PTCinematographyScriptSnapshot focusDistanceAtTime:disparityBuffer:]
+ -[PTCinematographyScriptSnapshot focusPuller]
+ -[PTCinematographyScriptSnapshot focuser]
+ -[PTCinematographyScriptSnapshot frames]
+ -[PTCinematographyScriptSnapshot generation]
+ -[PTCinematographyScriptSnapshot isRacking]
+ -[PTCinematographyScriptSnapshot latestProcessedFrame]
+ -[PTCinematographyScriptSnapshot rackFocusOptions]
+ -[PTCinematographyScriptSnapshot setCurrentFrameIndex:]
+ -[PTCinematographyScriptSnapshot setFocusDetections:]
+ -[PTCinematographyScriptSnapshot setFocusPuller:]
+ -[PTCinematographyScriptSnapshot setFocuser:]
+ -[PTCinematographyScriptSnapshot setFrames:]
+ -[PTCinematographyScriptSnapshot setLatestProcessedFrame:]
+ -[PTCinematographyScriptSnapshot setRackFocusOptions:]
+ -[PTCinematographyScriptSnapshot setSmoother:]
+ -[PTCinematographyScriptSnapshot setTrackDecisions:]
+ -[PTCinematographyScriptSnapshot smoother]
+ -[PTCinematographyScriptSnapshot trackDecisions]
+ -[PTCinematographyScriptSnapshot userAperture]
+ -[PTCinematographyScriptSnapshot(Private) _applyProcessedFocusDistancesToFrame:]
+ -[PTCinematographyScriptSnapshot(Private) _copyFocusDetectionFromFrame:]
+ -[PTCinematographyScriptSnapshot(Private) _initWithScript:generation:]
+ -[PTCinematographyScriptSnapshot(Private) dictionaryRepresentation]
+ -[PTCinematographyScriptSnapshot(Private) initWithDictionaryRepresentation:]
+ -[PTCinematographyTrackFilter .cxx_destruct]
+ -[PTCinematographyTrackFilter initWithTrackDecisions:maximumRackPullTime:]
+ -[PTCinematographyTrackFilter neededTrackIdentifiersAtTime:]
+ -[PTCinematographyTrackFocusDistancesAccumulator .cxx_destruct]
+ -[PTCinematographyTrackFocusDistancesAccumulator addFrameIndex:focusDistance:]
+ -[PTCinematographyTrackFocusDistancesAccumulator finalizeWithFrameTimeline:frameStartTime:]
+ -[PTCinematographyTrackFocusDistancesAccumulator focusDistances]
+ -[PTCinematographyTrackFocusDistancesAccumulator init]
+ -[PTCinematographyTrackFocusDistancesAccumulator setFocusDistances:]
+ -[PTCinematographyTrackFocusDistancesAccumulator setStartFrameIndex:]
+ -[PTCinematographyTrackFocusDistancesAccumulator startFrameIndex]
+ -[PTDisparityProviderInitializationStatus .cxx_destruct]
+ -[PTDisparityProviderInitializationStatus error]
+ -[PTDisparityProviderInitializationStatus estimatedTimeRemaining]
+ -[PTDisparityProviderInitializationStatus initWithState:totalExpectedBytes:totalWrittenBytes:estimatedTimeRemaining:error:]
+ -[PTDisparityProviderInitializationStatus state]
+ -[PTDisparityProviderInitializationStatus totalExpectedBytes]
+ -[PTDisparityProviderInitializationStatus totalWrittenBytes]
+ -[PTDisparityProviderModelStatusCacheValue .cxx_destruct]
+ -[PTDisparityProviderModelStatusCacheValue initWithStatus:]
+ -[PTDisparityProviderModelStatusCacheValue initWithStatus:lifetimeSeconds:]
+ -[PTDisparityProviderModelStatusCacheValue isObjectAlive]
+ -[PTDisparityProviderModelStatusCacheValue status]
+ -[PTMonocularDisparityNetworkManager .cxx_destruct]
+ -[PTMonocularDisparityNetworkManager createOperation:]
+ -[PTMonocularDisparityNetworkManager initWithSettings:downloadTimeout:callback:]
+ -[PTMonocularDisparityNetworkManager monocularVideoPipeline]
+ -[PTMonocularDisparityNetworkManager outputHeight]
+ -[PTMonocularDisparityNetworkManager outputWidth]
+ -[PTMonocularDisparityProvider .cxx_destruct]
+ -[PTMonocularDisparityProvider _disparityForColorBuffer:focalLenIn35mmFilm:time:outputBuffer:]
+ -[PTMonocularDisparityProvider _initializeInstanceSpecificResources]
+ -[PTMonocularDisparityProvider currentFlowMatchingPixelBuffer]
+ -[PTMonocularDisparityProvider currentRecurrentPixelBuffer]
+ -[PTMonocularDisparityProvider dealloc]
+ -[PTMonocularDisparityProvider deserializeState:]
+ -[PTMonocularDisparityProvider deserializeState:error:]
+ -[PTMonocularDisparityProvider disparityForColorBuffer:focalLenIn35mmFilm:]
+ -[PTMonocularDisparityProvider disparityForColorBuffer:focalLenIn35mmFilm:outputBuffer:]
+ -[PTMonocularDisparityProvider disparityForColorBuffer:timedRenderingMetadata:outputBuffer:]
+ -[PTMonocularDisparityProvider disparityForColorBuffer:timedRenderingMetadata:time:outputBuffer:]
+ -[PTMonocularDisparityProvider disparityPixelFormat]
+ -[PTMonocularDisparityProvider disparitySize]
+ -[PTMonocularDisparityProvider initWithQuality:inputSize:]
+ -[PTMonocularDisparityProvider initWithSettings:]
+ -[PTMonocularDisparityProvider initWithSettings:downloadTimeout:initializationCallback:]
+ -[PTMonocularDisparityProvider initWithSettings:downloadTimeout:initializationCallback:prewarmOnly:]
+ -[PTMonocularDisparityProvider maxTimeDiffBeforeReset]
+ -[PTMonocularDisparityProvider networkInputPixelBuffer]
+ -[PTMonocularDisparityProvider quality]
+ -[PTMonocularDisparityProvider requestDisparityForColorBuffer:focalLenIn35mmFilm:completionHandler:]
+ -[PTMonocularDisparityProvider resetStateIfNeededAtTime:]
+ -[PTMonocularDisparityProvider resetState]
+ -[PTMonocularDisparityProvider serializeState:]
+ -[PTMonocularDisparityProvider serializeState]
+ -[PTMonocularDisparityProvider willResetStateBeforeNextDisparityRequest]
+ -[PTMonocularDisparitySettings initWithQuality:globalMetadata:inputSize:]
+ -[PTMonocularDisparitySettings initWithQuality:globalMetadata:inputSize:temporalFilteringEnabled:]
+ -[PTMonocularDisparitySettings inputSize]
+ -[PTMonocularDisparitySettings inputSource]
+ -[PTMonocularDisparitySettings quality]
+ -[PTMonocularDisparitySettings renderVersion]
+ -[PTMonocularDisparitySettings temporalFilteringEnabled]
+ -[PTTapToTrack addDetectionAndStartTrackingRect:time:colorBuffer:]
+ -[PTTapToTrack addDetectionForNextFrameAt:colorBuffer:]
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table38
+ _BindPixelBufferToPort
+ _CreateAndBindPixelBufferToE5Port
+ _CreateEmptyPixelBufferOfSameType
+ _DetectionTrackOSType
+ _DetectionTracksContainerOSType
+ _FocusDataHeaderOSType
+ _FocusDataOSType
+ _FrameFocusDistancesOSType
+ _FrameTimelineOSType
+ _OBJC_CLASS_$_ADImageDimensions
+ _OBJC_CLASS_$_ADMonocularVideoPipeline
+ _OBJC_CLASS_$_ADMonocularVideoPipelineParameters
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_PTCinematographyFocusDisparitySampler
+ _OBJC_CLASS_$_PTCinematographyFocusDistanceTrack
+ _OBJC_CLASS_$_PTCinematographyFrameFocusDistancesAccumulator
+ _OBJC_CLASS_$_PTCinematographyPostcaptureRefinement
+ _OBJC_CLASS_$_PTCinematographyScriptFocusData
+ _OBJC_CLASS_$_PTCinematographyScriptFocusDataBuilder
+ _OBJC_CLASS_$_PTCinematographyScriptOptions
+ _OBJC_CLASS_$_PTCinematographyScriptSnapshot
+ _OBJC_CLASS_$_PTCinematographyTrackFilter
+ _OBJC_CLASS_$_PTCinematographyTrackFocusDistancesAccumulator
+ _OBJC_CLASS_$_PTDisparityProviderInitializationStatus
+ _OBJC_CLASS_$_PTDisparityProviderModelStatusCacheValue
+ _OBJC_CLASS_$_PTMonocularDisparityNetworkManager
+ _OBJC_CLASS_$_PTMonocularDisparityProvider
+ _OBJC_CLASS_$_PTMonocularDisparitySettings
+ _OBJC_IVAR_$_PTCinematographyFocusDisparitySampler._computeFocusDisparityForAllDetections
+ _OBJC_IVAR_$_PTCinematographyFocusDisparitySampler._lastInputTime
+ _OBJC_IVAR_$_PTCinematographyFocusDisparitySampler._priorFrame
+ _OBJC_IVAR_$_PTCinematographyFocusDisparitySampler._smoother
+ _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._focusDistances
+ _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._startTime
+ _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._timeline
+ _OBJC_IVAR_$_PTCinematographyFrame._focalLenIn35mmFilm
+ _OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._focusDistances
+ _OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._times
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._currentInputFrameIndex
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._focuser
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._frames
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._generation
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._inputsHaveBeenEnded
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._maximumPipelineBufferDuration
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._smoother
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._trackDecisions
+ _OBJC_IVAR_$_PTCinematographyScript._colorBufferProvider
+ _OBJC_IVAR_$_PTCinematographyScript._disparityProvider
+ _OBJC_IVAR_$_PTCinematographyScript._generation
+ _OBJC_IVAR_$_PTCinematographyScript._missingSomeFocusDistances
+ _OBJC_IVAR_$_PTCinematographyScript._options
+ _OBJC_IVAR_$_PTCinematographyScript._renderingGlobals
+ _OBJC_IVAR_$_PTCinematographyScript._videoDimensions
+ _OBJC_IVAR_$_PTCinematographyScriptFocusData._frameTrack
+ _OBJC_IVAR_$_PTCinematographyScriptFocusData._generation
+ _OBJC_IVAR_$_PTCinematographyScriptFocusData._tracks
+ _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._finalized
+ _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._frameAccumulator
+ _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._generation
+ _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._trackAccumulators
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._disableDetectionSmoothing
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._disparityPrecompute
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._disparityProvider
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._downloadTimeout
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._forcePostCaptureCinematic
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._overwriteRenderingVersion
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._postcaptureQuality
+ _OBJC_IVAR_$_PTCinematographyScriptOptions._temporalFilteringEnabled
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._currentFrameIndex
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._focusDetections
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._focusPuller
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._focuser
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._frames
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._generation
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._latestProcessedFrame
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._rackFocusOptions
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._smoother
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._trackDecisions
+ _OBJC_IVAR_$_PTCinematographyScriptSnapshot._userAperture
+ _OBJC_IVAR_$_PTCinematographyTrackFilter._maximumRackPullTime
+ _OBJC_IVAR_$_PTCinematographyTrackFilter._trackDecisions
+ _OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._focusDistances
+ _OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._startFrameIndex
+ _OBJC_IVAR_$_PTDisparityProviderInitializationStatus._error
+ _OBJC_IVAR_$_PTDisparityProviderInitializationStatus._estimatedTimeRemaining
+ _OBJC_IVAR_$_PTDisparityProviderInitializationStatus._state
+ _OBJC_IVAR_$_PTDisparityProviderInitializationStatus._totalExpectedBytes
+ _OBJC_IVAR_$_PTDisparityProviderInitializationStatus._totalWrittenBytes
+ _OBJC_IVAR_$_PTDisparityProviderModelStatusCacheValue._lifetimeSeconds
+ _OBJC_IVAR_$_PTDisparityProviderModelStatusCacheValue._startTime
+ _OBJC_IVAR_$_PTDisparityProviderModelStatusCacheValue._status
+ _OBJC_IVAR_$_PTMonocularDisparityNetworkManager._lock
+ _OBJC_IVAR_$_PTMonocularDisparityNetworkManager._monocularVideoPipeline
+ _OBJC_IVAR_$_PTMonocularDisparityNetworkManager._outputHeight
+ _OBJC_IVAR_$_PTMonocularDisparityNetworkManager._outputWidth
+ _OBJC_IVAR_$_PTMonocularDisparityNetworkManager._quality
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._disableExtrapolation
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._disparityNetworkOutputBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._disparityProviderLock
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._disparitySize
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5InputPortFlowMatching
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5InputPortRecurrent
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5Operation
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5OutputPortDisparity
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5OutputPortFlowMatching
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5OutputPortRecurrent
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5RgbInputPort
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._e5Stream
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._flowMatchingInitPixelBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._flowMatchingPixelBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._inputIndexIsZero
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._inputScalePixelBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._inputSize
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._lastFrameWasExtrapolated
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._lastPresentationTime
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._lastTime
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._metalContext
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._msrDownscaler
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._networkManager
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._outputBufferIndex
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._processingQueue
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._quality
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._recurrentInitPixelBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._recurrentPixelBuffer
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._resetState
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._temporalFilter
+ _OBJC_IVAR_$_PTMonocularDisparityProvider._temporalFilteringEnabled
+ _OBJC_IVAR_$_PTMonocularDisparitySettings._inputSize
+ _OBJC_IVAR_$_PTMonocularDisparitySettings._inputSource
+ _OBJC_IVAR_$_PTMonocularDisparitySettings._quality
+ _OBJC_IVAR_$_PTMonocularDisparitySettings._renderVersion
+ _OBJC_IVAR_$_PTMonocularDisparitySettings._temporalFilteringEnabled
+ _OBJC_METACLASS_$_PTCinematographyFocusDisparitySampler
+ _OBJC_METACLASS_$_PTCinematographyFocusDistanceTrack
+ _OBJC_METACLASS_$_PTCinematographyFrameFocusDistancesAccumulator
+ _OBJC_METACLASS_$_PTCinematographyPostcaptureRefinement
+ _OBJC_METACLASS_$_PTCinematographyScriptFocusData
+ _OBJC_METACLASS_$_PTCinematographyScriptFocusDataBuilder
+ _OBJC_METACLASS_$_PTCinematographyScriptOptions
+ _OBJC_METACLASS_$_PTCinematographyScriptSnapshot
+ _OBJC_METACLASS_$_PTCinematographyTrackFilter
+ _OBJC_METACLASS_$_PTCinematographyTrackFocusDistancesAccumulator
+ _OBJC_METACLASS_$_PTDisparityProviderInitializationStatus
+ _OBJC_METACLASS_$_PTDisparityProviderModelStatusCacheValue
+ _OBJC_METACLASS_$_PTMonocularDisparityNetworkManager
+ _OBJC_METACLASS_$_PTMonocularDisparityProvider
+ _OBJC_METACLASS_$_PTMonocularDisparitySettings
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _PTCinematographyScriptErrorDomain_block_invoke.onceToken
+ _PTMonocularDisparityQualityToString
+ __OBJC_$_CLASS_METHODS_PTCinematographyPostcaptureRefinement
+ __OBJC_$_CLASS_METHODS_PTCinematographyScriptFocusData(Serialization)
+ __OBJC_$_CLASS_METHODS_PTCinematographyScriptSnapshot(Private)
+ __OBJC_$_CLASS_METHODS_PTMonocularDisparityNetworkManager
+ __OBJC_$_CLASS_METHODS_PTMonocularDisparityProvider
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyFocusDisparitySampler
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyFocusDistanceTrack
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyFrameFocusDistancesAccumulator
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyPostcaptureRefinement
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptFocusData(Serialization)
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptFocusDataBuilder
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptOptions
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptSnapshot(Private)
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyTrackFilter
+ __OBJC_$_INSTANCE_METHODS_PTCinematographyTrackFocusDistancesAccumulator
+ __OBJC_$_INSTANCE_METHODS_PTDisparityProviderInitializationStatus
+ __OBJC_$_INSTANCE_METHODS_PTDisparityProviderModelStatusCacheValue
+ __OBJC_$_INSTANCE_METHODS_PTMonocularDisparityNetworkManager
+ __OBJC_$_INSTANCE_METHODS_PTMonocularDisparityProvider
+ __OBJC_$_INSTANCE_METHODS_PTMonocularDisparitySettings
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyFocusDisparitySampler
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyFocusDistanceTrack
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyFrameFocusDistancesAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyPostcaptureRefinement
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptFocusData
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptFocusDataBuilder
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptOptions
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyTrackFilter
+ __OBJC_$_INSTANCE_VARIABLES_PTCinematographyTrackFocusDistancesAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_PTDisparityProviderInitializationStatus
+ __OBJC_$_INSTANCE_VARIABLES_PTDisparityProviderModelStatusCacheValue
+ __OBJC_$_INSTANCE_VARIABLES_PTMonocularDisparityNetworkManager
+ __OBJC_$_INSTANCE_VARIABLES_PTMonocularDisparityProvider
+ __OBJC_$_INSTANCE_VARIABLES_PTMonocularDisparitySettings
+ __OBJC_$_PROP_LIST_PTCinematographyFocusDisparitySampler
+ __OBJC_$_PROP_LIST_PTCinematographyFocusDistanceTrack
+ __OBJC_$_PROP_LIST_PTCinematographyFrameFocusDistancesAccumulator
+ __OBJC_$_PROP_LIST_PTCinematographyPostcaptureRefinement
+ __OBJC_$_PROP_LIST_PTCinematographyScriptFocusDataBuilder
+ __OBJC_$_PROP_LIST_PTCinematographyScriptOptions
+ __OBJC_$_PROP_LIST_PTCinematographyScriptSnapshot
+ __OBJC_$_PROP_LIST_PTCinematographyTrackFocusDistancesAccumulator
+ __OBJC_$_PROP_LIST_PTDisparityProviderInitializationStatus
+ __OBJC_$_PROP_LIST_PTDisparityProviderModelStatusCacheValue
+ __OBJC_$_PROP_LIST_PTMonocularDisparityNetworkManager
+ __OBJC_$_PROP_LIST_PTMonocularDisparityProvider
+ __OBJC_$_PROP_LIST_PTMonocularDisparitySettings
+ __OBJC_CLASS_PROTOCOLS_$_PTCinematographyScriptFocusData(Serialization)
+ __OBJC_CLASS_PROTOCOLS_$_PTCinematographyScriptOptions
+ __OBJC_CLASS_RO_$_PTCinematographyFocusDisparitySampler
+ __OBJC_CLASS_RO_$_PTCinematographyFocusDistanceTrack
+ __OBJC_CLASS_RO_$_PTCinematographyFrameFocusDistancesAccumulator
+ __OBJC_CLASS_RO_$_PTCinematographyPostcaptureRefinement
+ __OBJC_CLASS_RO_$_PTCinematographyScriptFocusData
+ __OBJC_CLASS_RO_$_PTCinematographyScriptFocusDataBuilder
+ __OBJC_CLASS_RO_$_PTCinematographyScriptOptions
+ __OBJC_CLASS_RO_$_PTCinematographyScriptSnapshot
+ __OBJC_CLASS_RO_$_PTCinematographyTrackFilter
+ __OBJC_CLASS_RO_$_PTCinematographyTrackFocusDistancesAccumulator
+ __OBJC_CLASS_RO_$_PTDisparityProviderInitializationStatus
+ __OBJC_CLASS_RO_$_PTDisparityProviderModelStatusCacheValue
+ __OBJC_CLASS_RO_$_PTMonocularDisparityNetworkManager
+ __OBJC_CLASS_RO_$_PTMonocularDisparityProvider
+ __OBJC_CLASS_RO_$_PTMonocularDisparitySettings
+ __OBJC_METACLASS_RO_$_PTCinematographyFocusDisparitySampler
+ __OBJC_METACLASS_RO_$_PTCinematographyFocusDistanceTrack
+ __OBJC_METACLASS_RO_$_PTCinematographyFrameFocusDistancesAccumulator
+ __OBJC_METACLASS_RO_$_PTCinematographyPostcaptureRefinement
+ __OBJC_METACLASS_RO_$_PTCinematographyScriptFocusData
+ __OBJC_METACLASS_RO_$_PTCinematographyScriptFocusDataBuilder
+ __OBJC_METACLASS_RO_$_PTCinematographyScriptOptions
+ __OBJC_METACLASS_RO_$_PTCinematographyScriptSnapshot
+ __OBJC_METACLASS_RO_$_PTCinematographyTrackFilter
+ __OBJC_METACLASS_RO_$_PTCinematographyTrackFocusDistancesAccumulator
+ __OBJC_METACLASS_RO_$_PTDisparityProviderInitializationStatus
+ __OBJC_METACLASS_RO_$_PTDisparityProviderModelStatusCacheValue
+ __OBJC_METACLASS_RO_$_PTMonocularDisparityNetworkManager
+ __OBJC_METACLASS_RO_$_PTMonocularDisparityProvider
+ __OBJC_METACLASS_RO_$_PTMonocularDisparitySettings
+ ___100-[PTMonocularDisparityProvider requestDisparityForColorBuffer:focalLenIn35mmFilm:completionHandler:]_block_invoke
+ ___51+[PTMonocularDisparityProvider resourceStatusCache]_block_invoke
+ ___54-[PTCinematographyScript _rackFocusDisparityForFrame:]_block_invoke
+ ___56-[PTCinematographyScript _setRackFocusIfNeededForFrame:]_block_invoke
+ ___65+[PTCinematographyPostcaptureRefinement maximumLookaheadDuration]_block_invoke
+ ___67+[PTMonocularDisparityNetworkManager keepInstanceAlive:forSeconds:]_block_invoke
+ ___72-[PTCinematographyScript _monocularDisparityProviderSettingsForQuality:]_block_invoke
+ ___72-[PTCinematographyScriptSnapshot(Private) _copyFocusDetectionFromFrame:]_block_invoke
+ ___74+[PTCinematographyScriptFocusData(Serialization) registerForSerialization]_block_invoke
+ ___76-[PTCinematographyScriptFocusData(Serialization) writeToAtomWriter:options:]_block_invoke
+ ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke
+ ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke_2
+ ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke_3
+ ___80-[PTMonocularDisparityNetworkManager initWithSettings:downloadTimeout:callback:]_block_invoke
+ ___87-[PTCinematographyScript loadWithAsset:changesDictionary:disparityProvider:completion:]_block_invoke
+ ___96+[PTMonocularDisparityNetworkManager managerForSettings:downloadTimeout:initializationCallback:]_block_invoke
+ ____defaultNoLookahead_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64r72r80r88r96r104r112r_e5_v8?0lr64l8s32l8r72l8r80l8r88l8r96l8s40l8r104l8s48l8r112l8s56l8
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e31_q24?0"NSNumber"8"NSNumber"16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e40_v16?0"ADPipelineInitializationStatus"8lr40l8s32l8
+ ___block_descriptor_60_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0ls32l8r48l8r56l8r64l8r72l8s40l8
+ __copyFocusDetectionFromFrame:.onceToken
+ __defaultNoLookahead.onceToken
+ __monocularDisparityProviderSettingsForQuality:.onceToken
+ __rackFocusDisparityForFrame:.onceToken
+ __setRackFocusIfNeededForFrame:.onceToken
+ _e5rt_io_port_is_surface
+ _e5rt_precompiled_compute_op_create_options_create
+ _e5rt_precompiled_compute_op_create_options_set_allocate_intermediate_buffers
+ _e5rt_precompiled_compute_op_create_options_set_anef_procedure_variant_hint
+ _kMediaCharacteristicDepth
+ _kMediaCharacteristicDepthPostCapture
+ _kPTDisparityProviderDownloadTimeoutDefault
+ _kPTSensorIDs_Tele_modules
+ _managerForSettings:downloadTimeout:initializationCallback:.managers
+ _managerForSettings:downloadTimeout:initializationCallback:.managersLock
+ _managerForSettings:downloadTimeout:initializationCallback:.onceToken
+ _maximumLookaheadDuration.onceToken
+ _maximumLookaheadDuration.sRackFocusDuration
+ _objc_msgSend$_advanceToNextInputFrame
+ _objc_msgSend$_copyFocusDetectionFromFrame:
+ _objc_msgSend$_createSmootherAndFocuser
+ _objc_msgSend$_currentInputFrame
+ _objc_msgSend$_detectionByTrackIdentifier:fromArray:
+ _objc_msgSend$_disparityForColorBuffer:focalLenIn35mmFilm:time:outputBuffer:
+ _objc_msgSend$_disparityPixelBufferAtTime:
+ _objc_msgSend$_enforcePipelineBufferCapWithLatestInputTime:
+ _objc_msgSend$_ensureDisparityProvider
+ _objc_msgSend$_focalLenIn35mmFilm
+ _objc_msgSend$_focusDistanceForDetection:lockedDisparityBufferAddress:width:height:bytesPerRow:formatType:priorDetection:
+ _objc_msgSend$_frameBeforeFrame:
+ _objc_msgSend$_frameBeforeTime:
+ _objc_msgSend$_hasFocusDistances
+ _objc_msgSend$_initWithGeneration:frameTrack:tracks:
+ _objc_msgSend$_initWithScript:generation:
+ _objc_msgSend$_initializeInstanceSpecificResources
+ _objc_msgSend$_internalizeGenerationFromChangesDictionary:
+ _objc_msgSend$_invalidateFocusDistancesInFrame:
+ _objc_msgSend$_invalidateFocusDistancesInFrames:
+ _objc_msgSend$_invalidateFocusDistancesOfDetectionsInFrame:
+ _objc_msgSend$_monocularDisparityProviderSettingsForQuality:
+ _objc_msgSend$_moveAvailableFramesFromSmootherToFocuser
+ _objc_msgSend$_priorInputFrame
+ _objc_msgSend$_rackFocusDisparityForFrame:
+ _objc_msgSend$_removeAvailableFramesFromFrameDetectionSmoother:
+ _objc_msgSend$_resetToFrameIndex:
+ _objc_msgSend$_setFocusDistancesAtTime:tolerance:usingDisparityBuffer:
+ _objc_msgSend$_setFocusDistancesOfDetections:disparityBuffer:priorDetections:
+ _objc_msgSend$_setFocusDistancesUsingDisparityBuffer:priorFrame:
+ _objc_msgSend$_smoothDetectionsOfFramesInIndexRange:
+ _objc_msgSend$_smoothDetectionsOfFramesInTimeRange:
+ _objc_msgSend$_trackDecisionsInTimeRange:
+ _objc_msgSend$_updateFastRackStartFocusDistancesAfterRemovingDecisionsAtOrderedTimes:
+ _objc_msgSend$_updateFastRackStartIfNeededBeforeDecision:
+ _objc_msgSend$_updateFastRackStartIfNeededBetweenDecision:previousDecision:
+ _objc_msgSend$_updateFocusDistancesForAffectedDecisionsFromTime:originalNextDecision:
+ _objc_msgSend$_updateFocusDistancesForFrame:priorFrame:
+ _objc_msgSend$_updateFocusDistancesForFramesInIndexRange:
+ _objc_msgSend$_updateFocusDistancesForFramesInTimeRange:
+ _objc_msgSend$_updateFrameFocusDistancesAtTime:
+ _objc_msgSend$_updateFrameFocusDistancesForDecision:
+ _objc_msgSend$_updateFrameFocusDistancesForDecisions:indexRange:
+ _objc_msgSend$_updateFrameFocusDistancesForDecisions:timeRange:
+ _objc_msgSend$addFrameIndex:focusDistance:
+ _objc_msgSend$addTime:focusDistance:
+ _objc_msgSend$availabilityForParameters:
+ _objc_msgSend$colorFeaturesOutput
+ _objc_msgSend$createOperation:
+ _objc_msgSend$date
+ _objc_msgSend$decisionAtOrAfterTime:
+ _objc_msgSend$defaultRenderingMetadataWithRenderVersion:
+ _objc_msgSend$depthFeaturesOutput
+ _objc_msgSend$dimensions
+ _objc_msgSend$disparityForColorBuffer:focalLenIn35mmFilm:
+ _objc_msgSend$disparityForColorBuffer:focalLenIn35mmFilm:outputBuffer:
+ _objc_msgSend$disparityForColorBuffer:timedRenderingMetadata:time:outputBuffer:
+ _objc_msgSend$disparityPrecompute
+ _objc_msgSend$disparityProvider
+ _objc_msgSend$disparitySettingsCacheKey:
+ _objc_msgSend$downloadTimeout
+ _objc_msgSend$endInputs
+ _objc_msgSend$estimatedTimeRemaining
+ _objc_msgSend$fastRackStartTimeForDecisionTime:previousDecisionTime:
+ _objc_msgSend$finalFocusData
+ _objc_msgSend$finalizeFrameTrack
+ _objc_msgSend$finalizeWithFrameTimeline:frameStartTime:
+ _objc_msgSend$finalized
+ _objc_msgSend$focusDistanceAtTime:
+ _objc_msgSend$focusDistanceAtTime:trackIdentifier:
+ _objc_msgSend$focusDistances
+ _objc_msgSend$forcePostCaptureCinematic
+ _objc_msgSend$forceProcessNextFrame
+ _objc_msgSend$formatDescription
+ _objc_msgSend$frameAccumulator
+ _objc_msgSend$frameIndexForTime:
+ _objc_msgSend$frameTrack
+ _objc_msgSend$generation
+ _objc_msgSend$getMetricScaleFactorFor35mmFocalLength:
+ _objc_msgSend$groupCount
+ _objc_msgSend$groups
+ _objc_msgSend$hasDisparityTrack
+ _objc_msgSend$imageDescriptor
+ _objc_msgSend$imageDimensionsWithWidth:height:
+ _objc_msgSend$initWithDuration:frameCount:
+ _objc_msgSend$initWithFrames:generation:
+ _objc_msgSend$initWithGeneration:
+ _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
+ _objc_msgSend$initWithMetalContext:disparitySize:colorSize:disparityPixelFormat:colorPixelFormat:
+ _objc_msgSend$initWithParameters:
+ _objc_msgSend$initWithQuality:globalMetadata:inputSize:
+ _objc_msgSend$initWithQuality:globalMetadata:inputSize:temporalFilteringEnabled:
+ _objc_msgSend$initWithScript:samplesAllDetections:
+ _objc_msgSend$initWithScriptOptions:
+ _objc_msgSend$initWithSettings:
+ _objc_msgSend$initWithSettings:downloadTimeout:callback:
+ _objc_msgSend$initWithSettings:downloadTimeout:initializationCallback:
+ _objc_msgSend$initWithSettings:downloadTimeout:initializationCallback:prewarmOnly:
+ _objc_msgSend$initWithState:totalExpectedBytes:totalWrittenBytes:estimatedTimeRemaining:error:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$initWithStatus:lifetimeSeconds:
+ _objc_msgSend$initWithTimeline:focusDistances:startTime:
+ _objc_msgSend$initWithTimes:
+ _objc_msgSend$initWithTrackDecisions:maximumRackPullTime:
+ _objc_msgSend$initWithTrackDecisions:rackFocusOptions:focusPuller:detectionSmoother:
+ _objc_msgSend$initializationStatus
+ _objc_msgSend$inputSize
+ _objc_msgSend$inputSource
+ _objc_msgSend$isInput
+ _objc_msgSend$isInputExpected
+ _objc_msgSend$isObjectAlive
+ _objc_msgSend$isRacking
+ _objc_msgSend$keepInstanceAlive:forSeconds:
+ _objc_msgSend$loadWithAsset:changesDictionary:options:completion:
+ _objc_msgSend$longLongValue
+ _objc_msgSend$managerForSettings:downloadTimeout:initializationCallback:
+ _objc_msgSend$maxTimeDiffBeforeReset
+ _objc_msgSend$maximumLookaheadDuration
+ _objc_msgSend$missingSomeFocusDistances
+ _objc_msgSend$monocularVideoPipeline
+ _objc_msgSend$neededTrackIdentifiersAtTime:
+ _objc_msgSend$networkDimensionsForSettings:
+ _objc_msgSend$networkVariant
+ _objc_msgSend$networkVariantForInputSource:renderVersion:
+ _objc_msgSend$outputHeight
+ _objc_msgSend$outputScale
+ _objc_msgSend$outputWidth
+ _objc_msgSend$overwriteRenderingVersion
+ _objc_msgSend$pendingInputFrameTime
+ _objc_msgSend$postcaptureQuality
+ _objc_msgSend$prevColorFeaturesInput
+ _objc_msgSend$prevDepthFeaturesInput
+ _objc_msgSend$processExtrapolateWithColorRGBA:outDisparity:
+ _objc_msgSend$processWithInDisparity:inColorRGBA:outDisparity:
+ _objc_msgSend$renderVersion
+ _objc_msgSend$renderingGlobals
+ _objc_msgSend$requestedDimensions
+ _objc_msgSend$resetState
+ _objc_msgSend$resetStateIfNeededAtTime:
+ _objc_msgSend$resourceStatusCache
+ _objc_msgSend$setDisparityPrecompute:
+ _objc_msgSend$setDisparityProvider:
+ _objc_msgSend$setDownloadTimeout:
+ _objc_msgSend$setFilterType:
+ _objc_msgSend$setFinalized:
+ _objc_msgSend$setForcePostCaptureCinematic:
+ _objc_msgSend$setFrameAccumulator:
+ _objc_msgSend$setInitializationProgressCallback:
+ _objc_msgSend$setMissingSomeFocusDistances:
+ _objc_msgSend$setNetworkVariant:
+ _objc_msgSend$setOverwriteRenderingVersion:
+ _objc_msgSend$setPostcaptureQuality:
+ _objc_msgSend$setRequestedDimensions:
+ _objc_msgSend$setStartFrameIndex:
+ _objc_msgSend$setTemporalFilteringEnabled:
+ _objc_msgSend$setTrackAccumulators:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$set_focalLenIn35mmFilm:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$startFrameIndex
+ _objc_msgSend$startTime
+ _objc_msgSend$state
+ _objc_msgSend$subTimelineWithRange:
+ _objc_msgSend$supportedDimensions
+ _objc_msgSend$supportedDimensionsForParameters:
+ _objc_msgSend$temporalFilteringEnabled
+ _objc_msgSend$timeForFrameIndex:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timeline
+ _objc_msgSend$times
+ _objc_msgSend$totalExpectedBytes
+ _objc_msgSend$totalWrittenBytes
+ _objc_msgSend$trackAccumulators
+ _objc_msgSend$videoDimensions
+ _resourceStatusCache.onceToken
+ _resourceStatusCache.resourceStatusCache
- GCC_except_table20
- ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_2
- ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_3
- ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r_e5_v8?0lr64l8s32l8r72l8r80l8s40l8r88l8s48l8r96l8s56l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
CStrings:
+ "  error: %s\n"
+ "  estimatedTimeRemaining: %f\n"
+ "  state: %ld\n"
+ "  totalExpectedBytes: %zu\n"
+ "  totalWrittenBytes: %zu\n"
+ "%ld|%i|%d|%d"
+ "(null)"
+ "=======\n"
+ "ADPipelineInitializationStatus %f status %i %@"
+ "ADPipelineInitializationStatus:\n"
+ "AppleDepth resourceStatusForSettings availability.type %i initializationStatus.state %i"
+ "Attempt to rack focus from frame at (%lld, %d) without computed focus distance"
+ "Attempt to rack focus to decision frame at (%lld, %d) without pre-computed focus distance"
+ "Back"
+ "Base decision filtering enabled"
+ "CMM"
+ "CNUMSRResize downscale failed with error %i"
+ "Cannot determine CMM supportedDimensions!"
+ "CinematographyNoLookahead: %@"
+ "Could not determine disparity dimensions for settings %@"
+ "Disparity extrapolation failed with error %d"
+ "E5RT execution failed with error %u (%s)"
+ "E5RT operation setup failed with error %u (%s)"
+ "E5RT options setup failed with error %u (%s)"
+ "Error deserializing cinematographyPostcaptureRefinement %@"
+ "Error deserializing disparity provider %@"
+ "Error deserializing disparity provider internal state: %@, %@"
+ "Error serializeState cinematographyPostcaptureRefinement %@"
+ "Error serializeState disparity provider %@"
+ "Error serializing flowMatching %@ or recurrent %@"
+ "Espresso Port %@ is not a surface"
+ "Export"
+ "FAILURE: \"%s\" returned error = %u. msg = %s\n"
+ "Failed to alloacted buffer"
+ "Failed to allocate output disparity buffer"
+ "Failed to allocate pixel buffer"
+ "Failed to bind inputs or outputs to network!"
+ "Failed to create ADMonocularVideoPipeline"
+ "Failed to create Espresso operation"
+ "Failed to decode disparity provider internal state"
+ "Failed to get network manager for CMM disparity"
+ "Failed to initialize instance-specific E5RT resources"
+ "Failed to initialize temporal filter"
+ "Filtering: removing short-lived base decision %@ (duration %@)"
+ "Filtering: skipping consecutive same-track decision %@"
+ "FocusDisparitySampler: resetting state (discontinuity)"
+ "FocusDisparitySampler: smoothed focus distance is unknown (%.4f) at time %lld/%d — returning 0"
+ "Frame at (%lld/%d) has no autofocus detection!"
+ "Frame at (%lld/%d) missing focus detection -- using autoFocus instead"
+ "Front"
+ "Global metadata error, not metadata version 2)"
+ "Global metadata is nil"
+ "Init monocular network with downloadTimeout %f variant %lu size %lu x %lu"
+ "Invalid render version %i minimum requirement %lu"
+ "Invalid render version for monocular disparity. Was %i expected %lu or later"
+ "Invalid settings"
+ "Loaded Monocular pipeline for %@ camera with resolution %i x %i"
+ "Model URL or configuration for CMM network is invalid, failing"
+ "MonocularDisparityProvider: Invalid metadata"
+ "PTDisparityResourceStatus cache update for %@ to %i"
+ "PTDisparityResourceStatus hit for %@ value %i"
+ "PTDisparityResourceStatus miss for %@"
+ "PTDisparityResourceStatus set for %@ to %i network variant %i (%i x %i)"
+ "PTMonocularDisparityProvider: Aspect ratio must be close to 16:9 or 9:16!"
+ "PTMonocularDisparityProvider: Computing CMM disparity for time=%.4f"
+ "PTMonocularDisparityProvider: Extrapolating disparity (skipping ANE inference) for time=%.4f"
+ "PTMonocularDisparityProvider: Extrapolation supported: %@"
+ "PTMonocularDisparityProvider: Invalid input size provided!"
+ "PTMonocularDisparityProvider: Network input and output size don't match, that is unexpected! Failing!"
+ "PTMonocularDisparityProvider: One or more input/output ports failed to bind, failing!"
+ "PTMonocularDisparityProvider: resetState called"
+ "Pass 1: new first decision on track %ld (moved to time 0)"
+ "Post-capture Cinematic requires PTTimedRenderingMetadataVersion2"
+ "Preview"
+ "Provided outputDisparityPixelBuffer format does not match expected format!"
+ "Provided outputDisparityPixelBuffer size does not match expected size!"
+ "Requested CMM dimensions are not supported!"
+ "Snapshot dictionaryRepresentation: %lu detections, %lu frames, %lu decisions, rackFocusOptions=%@, focusPuller=%@"
+ "Snapshot initWithDictionary: %lu detections, %lu frames, %lu decisions, rackFocusOptions=%@, focusPuller=%@"
+ "Snapshot pipeline created: %lu frames, %lu decisions, rackFocusOptions=%@, focusPuller=%@"
+ "Snapshot: focuser returned nil at index %lu time %lld/%d"
+ "Snapshot: index %lu >= frames.count %lu (detections=%lu) at time %lld/%d"
+ "Snapshot: index=%lu time=%lld/%d focusDistance=%.4f"
+ "Snapshot: seek detected, resetting from %lu to %lu"
+ "Temporal filtering failed with error %d"
+ "Unexpected input source %i"
+ "Unexpected rendererVersion %i"
+ "Unsupported availability type %i"
+ "Url does not exist %@"
+ "V63"
+ "V64"
+ "V64s"
+ "V68"
+ "_msrDownscaler"
+ "applyFocusData: generation mismatch (focusData=%lu, script=%lu) - focusData is stale"
+ "availabilityForParameters returned nil"
+ "color buffer provider not initialized"
+ "colorTexture"
+ "com.apple.cinematic.monoculardisparity"
+ "com.apple.quicktime.cinematic-video-map.depth"
+ "com.apple.quicktime.cinematic-video-map.depth-post-capture"
+ "currentInputFrameIndex"
+ "disparity provider not initialized"
+ "e5rt_execution_stream_create(&_e5Stream)"
+ "e5rt_execution_stream_operation_retain_input_port(operation, descriptor.name.UTF8String, outPort)"
+ "e5rt_execution_stream_operation_retain_output_port(operation, descriptor.name.UTF8String, outPort)"
+ "e5rt_io_port_bind_surface_object(port, surfaceObject)"
+ "e5rt_io_port_is_surface(*outPort, &isSurface)"
+ "e5rt_io_port_release(&e5ScaleInputPort)"
+ "e5rt_surface_object_create_from_iosurface(&surfaceObject, CVPixelBufferGetIOSurface(pixelBuffer))"
+ "e5rt_surface_object_release(&surfaceObject)"
+ "flowMatching"
+ "focusDetections"
+ "focuser"
+ "generation"
+ "global rendering metadata is required but missing"
+ "inDisparityTexture"
+ "inputsHaveBeenEnded"
+ "lktFilterState"
+ "maximumDisparityPerSecond"
+ "maximumPipelineBufferDuration"
+ "maximumRackFocusTime"
+ "minimumRackFocusTime"
+ "missing focusDetection at (%lld / %d), substituting autoFocus"
+ "outDisparityTexture"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "rack focus requires frame (at %lld/%d) focus distance to have been computed"
+ "recurrent"
+ "replacing focus distance %.3f with rack focus distance %.3f in frame at %lld/%d"
+ "smoother"
+ "userAperture"
+ "v16@?0@\"ADPipelineInitializationStatus\"8"
+ "video dimensions are required but missing"
```
