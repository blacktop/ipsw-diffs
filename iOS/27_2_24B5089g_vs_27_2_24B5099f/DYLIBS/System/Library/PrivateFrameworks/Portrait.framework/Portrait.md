## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-560.40.3.0.0
-  __TEXT.__text: 0x97624
+560.40.5.0.0
+  __TEXT.__text: 0x92258
   __TEXT.__delay_helper: 0x264
-  __TEXT.__objc_methlist: 0xa15c
-  __TEXT.__const: 0x20b10
-  __TEXT.__cstring: 0x52e3
-  __TEXT.__oslogstring: 0x6133
-  __TEXT.__gcc_except_tab: 0x1af4
+  __TEXT.__objc_methlist: 0x9af4
+  __TEXT.__const: 0x20af0
+  __TEXT.__cstring: 0x5329
+  __TEXT.__oslogstring: 0x5ff3
+  __TEXT.__gcc_except_tab: 0x1b00
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2fb0
+  __TEXT.__unwind_info: 0x2e40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55a0
+  __DATA_CONST.__objc_selrefs: 0x52e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x510
-  __DATA_CONST.__objc_arraydata: 0x758
-  __DATA_CONST.__got: 0x8b8
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0x1e620
+  __DATA_CONST.__objc_superrefs: 0x4d8
+  __DATA_CONST.__objc_arraydata: 0x878
+  __DATA_CONST.__got: 0x8a0
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x5520
+  __AUTH_CONST.__objc_const: 0x1d7a0
   __AUTH_CONST.__objc_intobj: 0xaf8
-  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x1920
+  __DATA.__objc_ivar: 0x18a4
   __DATA.__data: 0x18
-  __DATA_DIRTY.__objc_data: 0x37a0
+  __DATA_DIRTY.__objc_data: 0x3570
   __DATA_DIRTY.__data: 0x798
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4122
-  Symbols:   7015
-  CStrings:  1528
+  Functions: 3973
+  Symbols:   6787
+  CStrings:  1554
 
Symbols:
+ -[PTCinematographyFocusSmoother didEmitSample]
+ -[PTCinematographyFocusSmoother setDidEmitSample:]
+ -[PTCinematographyScript focusDistancesUnavailable]
+ -[PTCinematographyScript forcePostCaptureDisparity]
+ -[PTCinematographyScript overwriteRenderingVersion]
+ -[PTCinematographyScript setFocusDistancesUnavailable:]
+ -[PTCinematographyScript setForcePostCaptureDisparity:]
+ -[PTCinematographyScript setOverwriteRenderingVersion:]
+ GCC_except_table22
+ _CNUModelSpecificName
+ _OBJC_IVAR_$_PTCinematographyFocusSmoother._didEmitSample
+ _OBJC_IVAR_$_PTCinematographyScript._focusDistancesUnavailable
+ _OBJC_IVAR_$_PTCinematographyScript._forcePostCaptureDisparity
+ _OBJC_IVAR_$_PTCinematographyScript._overwriteRenderingVersion
+ ___43-[PTCinematographyFocusSmoother addSample:]_block_invoke
+ ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_2
+ ___69-[PTCinematographyScript loadWithAsset:changesDictionary:completion:]_block_invoke_3
+ ___block_descriptor_120_e8_32s40s48s56s64r72r80r88r96r104r_e5_v8?0lr64l8s32l8r72l8r80l8r88l8s40l8r96l8s48l8r104l8s56l8
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8r48l8r56l8r64l8s40l8
+ ___isNetworkVariantSupportedOnDevice_block_invoke
+ _addSample:.onceToken
+ _isNetworkVariantSupportedOnDevice
+ _isNetworkVariantSupportedOnDevice.onceToken
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
- _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._focusDistances
- _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._startTime
- _OBJC_IVAR_$_PTCinematographyFocusDistanceTrack._timeline
- _OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._focusDistances
- _OBJC_IVAR_$_PTCinematographyFrameFocusDistancesAccumulator._times
- _OBJC_IVAR_$_PTCinematographyScript._colorBufferProvider
- _OBJC_IVAR_$_PTCinematographyScript._disparityProvider
- _OBJC_IVAR_$_PTCinematographyScript._missingSomeFocusDistances
- _OBJC_IVAR_$_PTCinematographyScript._options
- _OBJC_IVAR_$_PTCinematographyScript._rackFocusDisparitySlope
- _OBJC_IVAR_$_PTCinematographyScript._videoDimensions
- _OBJC_IVAR_$_PTCinematographyScriptFocusData._frameTrack
- _OBJC_IVAR_$_PTCinematographyScriptFocusData._generation
- _OBJC_IVAR_$_PTCinematographyScriptFocusData._tracks
- _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._finalized
- _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._frameAccumulator
- _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._generation
- _OBJC_IVAR_$_PTCinematographyScriptFocusDataBuilder._trackAccumulators
- _OBJC_IVAR_$_PTCinematographyScriptOptions._disableDetectionSmoothing
- _OBJC_IVAR_$_PTCinematographyScriptOptions._disparityPrecompute
- _OBJC_IVAR_$_PTCinematographyScriptOptions._disparityProvider
- _OBJC_IVAR_$_PTCinematographyScriptOptions._downloadTimeout
- _OBJC_IVAR_$_PTCinematographyScriptOptions._forcePostCaptureCinematic
- _OBJC_IVAR_$_PTCinematographyScriptOptions._overwriteRenderingVersion
- _OBJC_IVAR_$_PTCinematographyScriptOptions._postcaptureQuality
- _OBJC_IVAR_$_PTCinematographyScriptOptions._temporalFilteringEnabled
- _OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._focusDistances
- _OBJC_IVAR_$_PTCinematographyTrackFocusDistancesAccumulator._startFrameIndex
- _OBJC_IVAR_$_PTColorBufferProvider._assetReader
- _OBJC_IVAR_$_PTColorBufferProvider._colorProviderLock
- _OBJC_IVAR_$_PTColorBufferProvider._lastFrame
- _OBJC_IVAR_$_PTColorBufferProvider._processingQueue
- _OBJC_IVAR_$_PTColorBufferProvider._videoAsset
- _OBJC_IVAR_$_PTMonocularDisparityProvider._lastTime
- _OBJC_IVAR_$_PTMonocularDisparityProvider._processingQueue
- _OBJC_METACLASS_$_PTCinematographyFocusDistanceTrack
- _OBJC_METACLASS_$_PTCinematographyFrameFocusDistancesAccumulator
- _OBJC_METACLASS_$_PTCinematographyScriptFocusData
- _OBJC_METACLASS_$_PTCinematographyScriptFocusDataBuilder
- _OBJC_METACLASS_$_PTCinematographyScriptOptions
- _OBJC_METACLASS_$_PTCinematographyTrackFocusDistancesAccumulator
- _OBJC_METACLASS_$_PTColorBufferProvider
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
- __monocularDisparityProviderSettingsForQuality:.onceToken
- __rackFocusDisparityForFrame:.onceToken
- __setRackFocusIfNeededForFrame:.onceToken
CStrings:
+ "DisparitySampler: Unexpected pixel buffer format '%@' or size (%zdx%zd) - must be DisparityFloat16 or DisparityFloat32"
+ "PTCinematographyFocusSmoother: discarding un-drained sample %g - callers must drain output as it becomes available, otherwise results are truncated to the end of the input"
+ "Unknown chip id"
+ "Unsupported device %d network variant %lu model %@"
+ "Unsupported network variant %lu"
+ "Unsupported network variant on device"
+ "j407"
+ "j408"
+ "j410"
+ "j411"
+ "j507"
+ "j508"
+ "j517"
+ "j517x"
+ "j518"
+ "j518x"
+ "j522"
+ "j522x"
+ "j523"
+ "j523x"
+ "j537"
+ "j538"
+ "j607"
+ "j608"
+ "j617"
+ "j618"
+ "j620"
+ "j621"
+ "j637"
+ "j638"
+ "j707"
+ "j708"
+ "j717"
+ "j718"
+ "j720"
+ "j721"
+ "j737"
+ "j738"
+ "j817"
+ "j818"
+ "j820"
+ "j821"
- "Attempt to rack focus from frame at (%lld, %d) without computed focus distance"
- "Attempt to rack focus to decision frame at (%lld, %d) without pre-computed focus distance"
- "Failed to seek color reader to (%lld / %d): %@"
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
