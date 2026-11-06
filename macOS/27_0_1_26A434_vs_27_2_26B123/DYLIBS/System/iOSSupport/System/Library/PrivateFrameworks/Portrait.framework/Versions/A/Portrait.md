## Portrait

> `/System/iOSSupport/System/Library/PrivateFrameworks/Portrait.framework/Versions/A/Portrait`

```diff

-560.21.2.0.0
-  __TEXT.__text: 0x9bd34
+560.40.5.0.0
+  __TEXT.__text: 0x972e4
   __TEXT.__delay_helper: 0x264
-  __TEXT.__objc_methlist: 0xa174
-  __TEXT.__const: 0x20b10
-  __TEXT.__cstring: 0x5567
-  __TEXT.__oslogstring: 0x613d
+  __TEXT.__objc_methlist: 0x9ba4
+  __TEXT.__const: 0x20b00
+  __TEXT.__cstring: 0x54fb
+  __TEXT.__oslogstring: 0x6277
   __TEXT.__gcc_except_tab: 0x1b50
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2240
+  __TEXT.__unwind_info: 0x2110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x598
+  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55e0
+  __DATA_CONST.__objc_selrefs: 0x5370
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x868
-  __DATA_CONST.__got: 0x8d8
-  __AUTH_CONST.__const: 0x460
+  __DATA_CONST.__got: 0x8c0
+  __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0x1ebf8
+  __AUTH_CONST.__objc_const: 0x1ddf0
   __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x194c
-  __DATA.__data: 0x7a8
-  __DATA.__bss: 0x278
-  __DATA_DIRTY.__objc_data: 0x2f30
-  __DATA_DIRTY.__data: 0x4
+  __DATA.__objc_ivar: 0x18d8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x250
+  __DATA_DIRTY.__objc_data: 0x35c0
+  __DATA_DIRTY.__data: 0x79c
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4148
-  Symbols:   9289
-  CStrings:  1576
+  Functions: 4006
+  Symbols:   8988
+  CStrings:  1572
 
Symbols:
+ -[PTCinematographyFocusSmoother didEmitSample]
+ -[PTCinematographyFocusSmoother setDidEmitSample:]
+ -[PTCinematographyPostcaptureRefinement _advanceToInputFrameNearestTime:]
+ -[PTCinematographyPostcaptureRefinement _checkForInputStallAtTime:]
+ -[PTCinematographyPostcaptureRefinement _inputFrameSpacing]
+ -[PTCinematographyPostcaptureRefinement _lastProcessedInputFrame]
+ -[PTCinematographyPostcaptureRefinement didReportInputStall]
+ -[PTCinematographyPostcaptureRefinement firstInputTimeWithoutOutput]
+ -[PTCinematographyPostcaptureRefinement lastProcessedInputFrameIndex]
+ -[PTCinematographyPostcaptureRefinement processNextDisparityBuffer:atTime:]
+ -[PTCinematographyPostcaptureRefinement setDidReportInputStall:]
+ -[PTCinematographyPostcaptureRefinement setFirstInputTimeWithoutOutput:]
+ -[PTCinematographyPostcaptureRefinement setLastProcessedInputFrameIndex:]
+ -[PTCinematographyScript focusDistancesUnavailable]
+ -[PTCinematographyScript forcePostCaptureDisparity]
+ -[PTCinematographyScript overwriteRenderingVersion]
+ -[PTCinematographyScript setFocusDistancesUnavailable:]
+ -[PTCinematographyScript setForcePostCaptureDisparity:]
+ -[PTCinematographyScript setOverwriteRenderingVersion:]
+ -[PTPixelBufferCache removePixelBufferForTime:withinTolerance:]
+ GCC_except_table22
+ OBJC_IVAR_$_PTCinematographyFocusSmoother._didEmitSample
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._didReportInputStall
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._firstInputTimeWithoutOutput
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._lastProcessedInputFrameIndex
+ OBJC_IVAR_$_PTCinematographyScript._focusDistancesUnavailable
+ OBJC_IVAR_$_PTCinematographyScript._forcePostCaptureDisparity
+ OBJC_IVAR_$_PTCinematographyScript._overwriteRenderingVersion
+ __43-[PTCinematographyFocusSmoother addSample:]_block_invoke
+ __69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke
+ __69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_2
+ ___43-[PTCinematographyFocusSmoother addSample:]_block_invoke
+ ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_2
+ ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_3
+ ___block_descriptor_120_e8_32s40s48s56s64r72r80r88r96r104r_e5_v8?0lr64l8s32l8r72l8r80l8r88l8s40l8r96l8s48l8r104l8s56l8
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8r48l8r56l8r64l8s40l8
+ _objc_msgSend$_advanceToInputFrameNearestTime:
+ _objc_msgSend$_checkForInputStallAtTime:
+ _objc_msgSend$_inputFrameSpacing
+ _objc_msgSend$_lastProcessedInputFrame
+ _objc_msgSend$expectedInputTime
+ _objc_msgSend$focusDistancesUnavailable
+ _objc_msgSend$forcePostCaptureDisparity
+ _objc_msgSend$processNextDisparityBuffer:atTime:
+ addSample:.onceToken
- +[PTCinematographyScriptFocusData(Serialization) objectFromAtomStream:]
- +[PTCinematographyScriptFocusData(Serialization) registerForSerialization]
- +[PTMonocularDisparityProvider isSupported]
- -[PTCinematographyFocusDistanceTrack .cxx_destruct]
- -[PTCinematographyFocusDistanceTrack focusDistanceAtTime:]
- -[PTCinematographyFocusDistanceTrack focusDistances]
- -[PTCinematographyFocusDistanceTrack initWithTimeline:focusDistances:startTime:]
- -[PTCinematographyFocusDistanceTrack setFocusDistances:]
- -[PTCinematographyFocusDistanceTrack setStartTime:]
- -[PTCinematographyFocusDistanceTrack setTimeline:]
- -[PTCinematographyFocusDistanceTrack startTime]
- -[PTCinematographyFocusDistanceTrack timeline]
- -[PTCinematographyFrameFocusDistancesAccumulator .cxx_destruct]
- -[PTCinematographyFrameFocusDistancesAccumulator addTime:focusDistance:]
- -[PTCinematographyFrameFocusDistancesAccumulator finalizeFrameTrack]
- -[PTCinematographyFrameFocusDistancesAccumulator focusDistances]
- -[PTCinematographyFrameFocusDistancesAccumulator init]
- -[PTCinematographyFrameFocusDistancesAccumulator setFocusDistances:]
- -[PTCinematographyFrameFocusDistancesAccumulator setTimes:]
- -[PTCinematographyFrameFocusDistancesAccumulator times]
- -[PTCinematographyPostcaptureRefinement _priorInputFrame]
- -[PTCinematographyScript _disparityPixelBufferAtTime:]
- -[PTCinematographyScript _ensureDisparityProvider]
- -[PTCinematographyScript _frameBeforeFrame:]
- -[PTCinematographyScript _frameBeforeTime:]
- -[PTCinematographyScript _invalidateFocusDistancesInFrame:]
- -[PTCinematographyScript _invalidateFocusDistancesOfDetectionsInFrame:]
- -[PTCinematographyScript _monocularDisparityProviderSettingsForQuality:]
- -[PTCinematographyScript _rackFocusDisparityForFrame:]
- -[PTCinematographyScript _removeAvailableFramesFromFrameDetectionSmoother:]
- -[PTCinematographyScript _setFocusDistancesAtTime:tolerance:usingDisparityBuffer:]
- -[PTCinematographyScript _setRackFocusIfNeededForFrame:]
- -[PTCinematographyScript _smoothDetectionsOfFramesInIndexRange:]
- -[PTCinematographyScript _smoothDetectionsOfFramesInTimeRange:]
- -[PTCinematographyScript _updateFastRackStartFocusDistancesAfterRemovingDecisionsAtOrderedTimes:]
- -[PTCinematographyScript _updateFastRackStartIfNeededBeforeDecision:]
- -[PTCinematographyScript _updateFastRackStartIfNeededBetweenDecision:previousDecision:]
- -[PTCinematographyScript _updateFocusDistancesForAffectedDecisionsFromTime:originalNextDecision:]
- -[PTCinematographyScript _updateFocusDistancesForFrame:priorFrame:]
- -[PTCinematographyScript _updateFocusDistancesForFramesInIndexRange:]
- -[PTCinematographyScript _updateFocusDistancesForFramesInTimeRange:]
- -[PTCinematographyScript _updateFrameFocusDistancesAtTime:]
- -[PTCinematographyScript _updateFrameFocusDistancesForDecision:]
- -[PTCinematographyScript _updateFrameFocusDistancesForDecisions:indexRange:]
- -[PTCinematographyScript _updateFrameFocusDistancesForDecisions:timeRange:]
- -[PTCinematographyScript applyFocusData:]
- -[PTCinematographyScript colorBufferProvider]
- -[PTCinematographyScript disparityProvider]
- -[PTCinematographyScript focusData]
- -[PTCinematographyScript loadWithAsset:changesDictionary:disparityProvider:completion:]
- -[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]
- -[PTCinematographyScript missingSomeFocusDistances]
- -[PTCinematographyScript options]
- -[PTCinematographyScript setColorBufferProvider:]
- -[PTCinematographyScript setDisparityProvider:]
- -[PTCinematographyScript setMissingSomeFocusDistances:]
- -[PTCinematographyScript setOptions:]
- -[PTCinematographyScript setVideoDimensions:]
- -[PTCinematographyScript videoDimensions]
- -[PTCinematographyScriptFocusData .cxx_destruct]
- -[PTCinematographyScriptFocusData _initWithGeneration:frameTrack:tracks:]
- -[PTCinematographyScriptFocusData dataRepresentation]
- -[PTCinematographyScriptFocusData focusDistanceAtTime:]
- -[PTCinematographyScriptFocusData focusDistanceAtTime:trackIdentifier:]
- -[PTCinematographyScriptFocusData frameTrack]
- -[PTCinematographyScriptFocusData generation]
- -[PTCinematographyScriptFocusData initWithDataRepresentation:]
- -[PTCinematographyScriptFocusData initWithFrames:generation:]
- -[PTCinematographyScriptFocusData setFrameTrack:]
- -[PTCinematographyScriptFocusData setGeneration:]
- -[PTCinematographyScriptFocusData setTracks:]
- -[PTCinematographyScriptFocusData tracks]
- -[PTCinematographyScriptFocusData(Serialization) sizeOfSerializedObjectWithOptions:]
- -[PTCinematographyScriptFocusData(Serialization) supportsVersion:]
- -[PTCinematographyScriptFocusData(Serialization) writeToAtomWriter:options:]
- -[PTCinematographyScriptFocusDataBuilder .cxx_destruct]
- -[PTCinematographyScriptFocusDataBuilder addFrame:]
- -[PTCinematographyScriptFocusDataBuilder finalFocusData]
- -[PTCinematographyScriptFocusDataBuilder finalized]
- -[PTCinematographyScriptFocusDataBuilder frameAccumulator]
- -[PTCinematographyScriptFocusDataBuilder generation]
- -[PTCinematographyScriptFocusDataBuilder initWithGeneration:]
- -[PTCinematographyScriptFocusDataBuilder setFinalized:]
- -[PTCinematographyScriptFocusDataBuilder setFrameAccumulator:]
- -[PTCinematographyScriptFocusDataBuilder setGeneration:]
- -[PTCinematographyScriptFocusDataBuilder setTrackAccumulators:]
- -[PTCinematographyScriptFocusDataBuilder trackAccumulators]
- -[PTCinematographyScriptOptions .cxx_destruct]
- -[PTCinematographyScriptOptions copyWithZone:]
- -[PTCinematographyScriptOptions disableDetectionSmoothing]
- -[PTCinematographyScriptOptions disparityPrecompute]
- -[PTCinematographyScriptOptions disparityProvider]
- -[PTCinematographyScriptOptions downloadTimeout]
- -[PTCinematographyScriptOptions fastPreview]
- -[PTCinematographyScriptOptions forcePostCaptureCinematic]
- -[PTCinematographyScriptOptions initWithScriptOptions:]
- -[PTCinematographyScriptOptions init]
- -[PTCinematographyScriptOptions mutableCopyWithZone:]
- -[PTCinematographyScriptOptions overwriteRenderingVersion]
- -[PTCinematographyScriptOptions postcaptureQuality]
- -[PTCinematographyScriptOptions setDisableDetectionSmoothing:]
- -[PTCinematographyScriptOptions setDisparityPrecompute:]
- -[PTCinematographyScriptOptions setDisparityProvider:]
- -[PTCinematographyScriptOptions setDownloadTimeout:]
- -[PTCinematographyScriptOptions setFastPreview:]
- -[PTCinematographyScriptOptions setForcePostCaptureCinematic:]
- -[PTCinematographyScriptOptions setOverwriteRenderingVersion:]
- -[PTCinematographyScriptOptions setPostcaptureQuality:]
- -[PTCinematographyScriptOptions setTemporalFilteringEnabled:]
- -[PTCinematographyScriptOptions temporalFilteringEnabled]
- -[PTCinematographyTrackFocusDistancesAccumulator .cxx_destruct]
- -[PTCinematographyTrackFocusDistancesAccumulator addFrameIndex:focusDistance:]
- -[PTCinematographyTrackFocusDistancesAccumulator finalizeWithFrameTimeline:frameStartTime:]
- -[PTCinematographyTrackFocusDistancesAccumulator focusDistances]
- -[PTCinematographyTrackFocusDistancesAccumulator init]
- -[PTCinematographyTrackFocusDistancesAccumulator setFocusDistances:]
- -[PTCinematographyTrackFocusDistancesAccumulator setStartFrameIndex:]
- -[PTCinematographyTrackFocusDistancesAccumulator startFrameIndex]
- -[PTColorBufferProvider .cxx_destruct]
- -[PTColorBufferProvider assetReader]
- -[PTColorBufferProvider initWithAsset:]
- -[PTColorBufferProvider lastFrame]
- -[PTColorBufferProvider pixelBufferAtTime:]
- -[PTColorBufferProvider processingQueue]
- -[PTColorBufferProvider requestPixelBufferAtTime:completionHandler:]
- -[PTColorBufferProvider setAssetReader:]
- -[PTColorBufferProvider setLastFrame:]
- -[PTColorBufferProvider setProcessingQueue:]
- -[PTColorBufferProvider setVideoAsset:]
- -[PTColorBufferProvider videoAsset]
- -[PTMonocularDisparityProvider deserializeState:]
- -[PTMonocularDisparityProvider disparityForColorBuffer:focalLenIn35mmFilm:]
- -[PTMonocularDisparityProvider disparityForColorBuffer:focalLenIn35mmFilm:outputBuffer:]
- -[PTMonocularDisparityProvider disparityForColorBuffer:timedRenderingMetadata:outputBuffer:]
- -[PTMonocularDisparityProvider initWithQuality:inputSize:]
- -[PTMonocularDisparityProvider maxTimeDiffBeforeReset]
- -[PTMonocularDisparityProvider requestDisparityForColorBuffer:focalLenIn35mmFilm:completionHandler:]
- -[PTMonocularDisparityProvider resetStateIfNeededAtTime:]
- -[PTMonocularDisparityProvider serializeState]
- GCC_except_table29
- GCC_except_table38
- OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._focusDistances
- OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._startTime
- OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._timeline
- OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._focusDistances
- OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._times
- OBJC_IVAR_$_PTCinematographyScript._colorBufferProvider
- OBJC_IVAR_$_PTCinematographyScript._disparityProvider
- OBJC_IVAR_$_PTCinematographyScript._missingSomeFocusDistances
- OBJC_IVAR_$_PTCinematographyScript._options
- OBJC_IVAR_$_PTCinematographyScript._rackFocusDisparitySlope
- OBJC_IVAR_$_PTCinematographyScript._videoDimensions
- OBJC_IVAR_$_PTCinematographyScriptFocusData._frameTrack
- OBJC_IVAR_$_PTCinematographyScriptFocusData._generation
- OBJC_IVAR_$_PTCinematographyScriptFocusData._tracks
- OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._finalized
- OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._frameAccumulator
- OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._generation
- OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._trackAccumulators
- OBJC_IVAR_$_PTCinematographyScriptOptions._disableDetectionSmoothing
- OBJC_IVAR_$_PTCinematographyScriptOptions._disparityPrecompute
- OBJC_IVAR_$_PTCinematographyScriptOptions._disparityProvider
- OBJC_IVAR_$_PTCinematographyScriptOptions._downloadTimeout
- OBJC_IVAR_$_PTCinematographyScriptOptions._forcePostCaptureCinematic
- OBJC_IVAR_$_PTCinematographyScriptOptions._overwriteRenderingVersion
- OBJC_IVAR_$_PTCinematographyScriptOptions._postcaptureQuality
- OBJC_IVAR_$_PTCinematographyScriptOptions._temporalFilteringEnabled
- OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._focusDistances
- OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._startFrameIndex
- OBJC_IVAR_$_PTColorBufferProvider._assetReader
- OBJC_IVAR_$_PTColorBufferProvider._colorProviderLock
- OBJC_IVAR_$_PTColorBufferProvider._lastFrame
- OBJC_IVAR_$_PTColorBufferProvider._processingQueue
- OBJC_IVAR_$_PTColorBufferProvider._videoAsset
- OBJC_IVAR_$_PTDisparityFilterDEMA_LKT._erodeMonocularDisparity
- OBJC_IVAR_$_PTMonocularDisparityProvider._lastTime
- OBJC_IVAR_$_PTMonocularDisparityProvider._processingQueue
- _DetectionTrackOSType
- _DetectionTracksContainerOSType
- _FocusDataHeaderOSType
- _FocusDataOSType
- _FrameFocusDistancesOSType
- _FrameTimelineOSType
- _OBJC_CLASS_$_PTCinematographyFocusDistanceTrack
- _OBJC_CLASS_$_PTCinematographyFrameFocusDistancesAccumulator
- _OBJC_CLASS_$_PTCinematographyScriptFocusData
- _OBJC_CLASS_$_PTCinematographyScriptFocusDataBuilder
- _OBJC_CLASS_$_PTCinematographyScriptOptions
- _OBJC_CLASS_$_PTCinematographyTrackFocusDistancesAccumulator
- _OBJC_CLASS_$_PTColorBufferProvider
- _OBJC_METACLASS_$_PTCinematographyFocusDistanceTrack
- _OBJC_METACLASS_$_PTCinematographyFrameFocusDistancesAccumulator
- _OBJC_METACLASS_$_PTCinematographyScriptFocusData
- _OBJC_METACLASS_$_PTCinematographyScriptFocusDataBuilder
- _OBJC_METACLASS_$_PTCinematographyScriptOptions
- _OBJC_METACLASS_$_PTCinematographyTrackFocusDistancesAccumulator
- _OBJC_METACLASS_$_PTColorBufferProvider
- _OUTLINED_FUNCTION_11
- __54-[PTCinematographyScript _rackFocusDisparityForFrame:]_block_invoke
- __72-[PTCinematographyScript _monocularDisparityProviderSettingsForQuality:]_block_invoke
- __77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke
- __77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke_2
- __OBJC_$_CLASS_METHODS_PTCinematographyScriptFocusData(Serialization)
- __OBJC_$_INSTANCE_METHODS_PTCinematographyFocusDistanceTrack
- __OBJC_$_INSTANCE_METHODS_PTCinematographyFrameFocusDistancesAccumulator
- __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptFocusData(Serialization)
- __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptFocusDataBuilder
- __OBJC_$_INSTANCE_METHODS_PTCinematographyScriptOptions
- __OBJC_$_INSTANCE_METHODS_PTCinematographyTrackFocusDistancesAccumulator
- __OBJC_$_INSTANCE_METHODS_PTColorBufferProvider
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyFocusDistanceTrack
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyFrameFocusDistancesAccumulator
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptFocusData
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptFocusDataBuilder
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyScriptOptions
- __OBJC_$_INSTANCE_VARIABLES_PTCinematographyTrackFocusDistancesAccumulator
- __OBJC_$_INSTANCE_VARIABLES_PTColorBufferProvider
- __OBJC_$_PROP_LIST_PTCinematographyFocusDistanceTrack
- __OBJC_$_PROP_LIST_PTCinematographyFrameFocusDistancesAccumulator
- __OBJC_$_PROP_LIST_PTCinematographyScriptFocusDataBuilder
- __OBJC_$_PROP_LIST_PTCinematographyScriptOptions
- __OBJC_$_PROP_LIST_PTCinematographyTrackFocusDistancesAccumulator
- __OBJC_$_PROP_LIST_PTColorBufferProvider
- __OBJC_CLASS_PROTOCOLS_$_PTCinematographyScriptFocusData(Serialization)
- __OBJC_CLASS_PROTOCOLS_$_PTCinematographyScriptOptions
- __OBJC_CLASS_RO_$_PTCinematographyFocusDistanceTrack
- __OBJC_CLASS_RO_$_PTCinematographyFrameFocusDistancesAccumulator
- __OBJC_CLASS_RO_$_PTCinematographyScriptFocusData
- __OBJC_CLASS_RO_$_PTCinematographyScriptFocusDataBuilder
- __OBJC_CLASS_RO_$_PTCinematographyScriptOptions
- __OBJC_CLASS_RO_$_PTCinematographyTrackFocusDistancesAccumulator
- __OBJC_CLASS_RO_$_PTColorBufferProvider
- __OBJC_METACLASS_RO_$_PTCinematographyFocusDistanceTrack
- __OBJC_METACLASS_RO_$_PTCinematographyFrameFocusDistancesAccumulator
- __OBJC_METACLASS_RO_$_PTCinematographyScriptFocusData
- __OBJC_METACLASS_RO_$_PTCinematographyScriptFocusDataBuilder
- __OBJC_METACLASS_RO_$_PTCinematographyScriptOptions
- __OBJC_METACLASS_RO_$_PTCinematographyTrackFocusDistancesAccumulator
- __OBJC_METACLASS_RO_$_PTColorBufferProvider
- ___100-[PTMonocularDisparityProvider requestDisparityForColorBuffer:focalLenIn35mmFilm:completionHandler:]_block_invoke
- ___54-[PTCinematographyScript _rackFocusDisparityForFrame:]_block_invoke
- ___56-[PTCinematographyScript _setRackFocusIfNeededForFrame:]_block_invoke
- ___68-[PTColorBufferProvider requestPixelBufferAtTime:completionHandler:]_block_invoke
- ___72-[PTCinematographyScript _monocularDisparityProviderSettingsForQuality:]_block_invoke
- ___74+[PTCinematographyScriptFocusData(Serialization) registerForSerialization]_block_invoke
- ___76-[PTCinematographyScriptFocusData(Serialization) writeToAtomWriter:options:]_block_invoke
- ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke
- ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke_2
- ___77-[PTCinematographyScript loadWithAsset:changesDictionary:options:completion:]_block_invoke_3
- ___87-[PTCinematographyScript loadWithAsset:changesDictionary:disparityProvider:completion:]_block_invoke
- ___block_descriptor_128_e8_32s40s48s56s64r72r80r88r96r104r112r_e5_v8?0lr64l8s32l8r72l8r80l8r88l8r96l8s40l8r104l8s48l8r112l8s56l8
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32s_e31_q24?0"NSNumber"8"NSNumber"16ls32l8
- ___block_descriptor_60_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_72_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0ls32l8r48l8r56l8r64l8r72l8s40l8
- _monocularDisparityProviderSettingsForQuality:.onceToken
- _objc_msgSend$_disparityPixelBufferAtTime:
- _objc_msgSend$_ensureDisparityProvider
- _objc_msgSend$_frameBeforeFrame:
- _objc_msgSend$_frameBeforeTime:
- _objc_msgSend$_initWithGeneration:frameTrack:tracks:
- _objc_msgSend$_invalidateFocusDistancesInFrame:
- _objc_msgSend$_invalidateFocusDistancesOfDetectionsInFrame:
- _objc_msgSend$_monocularDisparityProviderSettingsForQuality:
- _objc_msgSend$_priorInputFrame
- _objc_msgSend$_rackFocusDisparityForFrame:
- _objc_msgSend$_removeAvailableFramesFromFrameDetectionSmoother:
- _objc_msgSend$_setFocusDistancesAtTime:tolerance:usingDisparityBuffer:
- _objc_msgSend$_smoothDetectionsOfFramesInIndexRange:
- _objc_msgSend$_smoothDetectionsOfFramesInTimeRange:
- _objc_msgSend$_updateFastRackStartFocusDistancesAfterRemovingDecisionsAtOrderedTimes:
- _objc_msgSend$_updateFastRackStartIfNeededBeforeDecision:
- _objc_msgSend$_updateFastRackStartIfNeededBetweenDecision:previousDecision:
- _objc_msgSend$_updateFocusDistancesForAffectedDecisionsFromTime:originalNextDecision:
- _objc_msgSend$_updateFocusDistancesForFrame:priorFrame:
- _objc_msgSend$_updateFocusDistancesForFramesInIndexRange:
- _objc_msgSend$_updateFocusDistancesForFramesInTimeRange:
- _objc_msgSend$_updateFrameFocusDistancesAtTime:
- _objc_msgSend$_updateFrameFocusDistancesForDecision:
- _objc_msgSend$_updateFrameFocusDistancesForDecisions:indexRange:
- _objc_msgSend$_updateFrameFocusDistancesForDecisions:timeRange:
- _objc_msgSend$addFrameIndex:focusDistance:
- _objc_msgSend$addTime:focusDistance:
- _objc_msgSend$decisionAtOrAfterTime:
- _objc_msgSend$disparityForColorBuffer:focalLenIn35mmFilm:
- _objc_msgSend$disparityForColorBuffer:focalLenIn35mmFilm:outputBuffer:
- _objc_msgSend$disparityForColorBuffer:timedRenderingMetadata:time:outputBuffer:
- _objc_msgSend$disparityPrecompute
- _objc_msgSend$disparityProvider
- _objc_msgSend$downloadTimeout
- _objc_msgSend$fastRackStartTimeForDecisionTime:previousDecisionTime:
- _objc_msgSend$finalFocusData
- _objc_msgSend$finalizeFrameTrack
- _objc_msgSend$finalizeWithFrameTimeline:frameStartTime:
- _objc_msgSend$finalized
- _objc_msgSend$focusDistanceAtTime:
- _objc_msgSend$focusDistanceAtTime:trackIdentifier:
- _objc_msgSend$focusDistances
- _objc_msgSend$forcePostCaptureCinematic
- _objc_msgSend$formatDescription
- _objc_msgSend$frameAccumulator
- _objc_msgSend$frameIndexForTime:
- _objc_msgSend$frameTrack
- _objc_msgSend$groupCount
- _objc_msgSend$groups
- _objc_msgSend$initWithDuration:frameCount:
- _objc_msgSend$initWithFrames:generation:
- _objc_msgSend$initWithGeneration:
- _objc_msgSend$initWithQuality:globalMetadata:inputSize:
- _objc_msgSend$initWithScriptOptions:
- _objc_msgSend$initWithSettings:
- _objc_msgSend$initWithTimeline:focusDistances:startTime:
- _objc_msgSend$initWithTimes:
- _objc_msgSend$loadWithAsset:changesDictionary:options:completion:
- _objc_msgSend$longLongValue
- _objc_msgSend$maxTimeDiffBeforeReset
- _objc_msgSend$missingSomeFocusDistances
- _objc_msgSend$overwriteRenderingVersion
- _objc_msgSend$pixelBufferAtTime:
- _objc_msgSend$postcaptureQuality
- _objc_msgSend$resetState
- _objc_msgSend$resetStateIfNeededAtTime:
- _objc_msgSend$setDisparityPrecompute:
- _objc_msgSend$setDisparityProvider:
- _objc_msgSend$setFinalized:
- _objc_msgSend$setForcePostCaptureCinematic:
- _objc_msgSend$setFrameAccumulator:
- _objc_msgSend$setMissingSomeFocusDistances:
- _objc_msgSend$setOverwriteRenderingVersion:
- _objc_msgSend$setPostcaptureQuality:
- _objc_msgSend$setStartFrameIndex:
- _objc_msgSend$setTemporalFilteringEnabled:
- _objc_msgSend$setTrackAccumulators:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$startFrameIndex
- _objc_msgSend$startTime
- _objc_msgSend$subTimelineWithRange:
- _objc_msgSend$supportedDimensions
- _objc_msgSend$timeForFrameIndex:
- _objc_msgSend$timeline
- _objc_msgSend$times
- _objc_msgSend$trackAccumulators
- _objc_msgSend$videoDimensions
- _objc_retain_x10
- _rackFocusDisparityForFrame:.onceToken
- _setRackFocusIfNeededForFrame:.onceToken
CStrings:
+ "Base decision filtering: %lu decisions in, %lu out"
+ "Cinematography: fast (per-frame metadata sampler, no decisions)"
+ "Cinematography: refined (generation %lu, %lu frames, %lu decisions)"
+ "Cinematography: snapshot (generation %lu, %lu frames, %lu decisions)"
+ "DisparitySampler: Unexpected pixel buffer format '%@' or size (%zdx%zd) - must be DisparityFloat16 or DisparityFloat32"
+ "Input time %@ is not within half a frame of any script frame (nearest is %@); ignoring disparity buffer"
+ "Input time %@ precedes expected input time %@; ignoring disparity buffer"
+ "No frame near input time %@ to apply disparity buffer to"
+ "No output frame after inputs spanning %.2fs from %@; inputs may be too sparse (about 24 per second of source are needed)"
+ "No timestamp within tolerance %f seconds of the requested timestamp found in cache"
+ "PTCinematographyFocusSmoother: discarding un-drained sample %g - callers must drain output as it becomes available, otherwise results are truncated to the end of the input"
+ "Skipping %lu input frame(s) to reach input time %@"
+ "Tolerance passed to removePixelBufferForTime:withinTolerance: must be numeric, finite and non-negative"
+ "lastProcessedInputFrameIndex"
- "Attempt to rack focus from frame at (%lld, %d) without computed focus distance"
- "Attempt to rack focus to decision frame at (%lld, %d) without pre-computed focus distance"
- "Failed to seek color reader to (%lld / %d): %@"
- "PTDisparityFilterDEMA_LKT enabling disparity erosion with strength: %.2f"
- "PortTypeFrontSuperWide"
- "Requested time (%lld / %d) is not within range of asset %@"
- "Unable to create asset reader"
- "Unable to start reading color frames"
- "applyFocusData: generation mismatch (focusData=%lu, script=%lu) - focusData is stale"
- "color buffer provider not initialized"
- "com.apple.cinematic.colorbufferprovider"
- "com.apple.cinematic.monoculardisparity"
- "disparity provider not initialized"
- "global rendering metadata is required but missing"
- "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
- "rack focus requires frame (at %lld/%d) focus distance to have been computed"
- "replacing focus distance %.3f with rack focus distance %.3f in frame at %lld/%d"
- "video dimensions are required but missing"
```
