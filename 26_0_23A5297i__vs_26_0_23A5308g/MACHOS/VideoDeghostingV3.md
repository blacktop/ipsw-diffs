## VideoDeghostingV3

> `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/VideoDeghostingV3`

```diff

-661.0.0.0.3
-  __TEXT.__text: 0x31414
-  __TEXT.__auth_stubs: 0xa80
+664.0.0.0.2
+  __TEXT.__text: 0x2c580
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_stubs: 0x29a0
   __TEXT.__objc_methlist: 0x1c24
-  __TEXT.__const: 0xeb8
   __TEXT.__objc_methname: 0x6e6c
-  __TEXT.__oslogstring: 0x19fa
-  __TEXT.__cstring: 0x5cc5
+  __TEXT.__cstring: 0x44d3
   __TEXT.__objc_classname: 0x287
   __TEXT.__objc_methtype: 0x4c51
-  __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__unwind_info: 0x7c0
-  __DATA_CONST.__auth_got: 0x558
+  __TEXT.__const: 0xe88
+  __TEXT.__oslogstring: 0x1df
+  __TEXT.__gcc_except_tab: 0x2d0
+  __TEXT.__unwind_info: 0x740
+  __DATA_CONST.__auth_got: 0x560
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__cfstring: 0x1360
+  __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x59c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x2c8
-  __DATA.__common: 0x50
   __DATA.__bss: 0x30
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EEA3D3A6-2711-3F48-BDDD-9896AA57E7E0
-  Functions: 888
-  Symbols:   2141
-  CStrings:  2214
+  UUID: 6B75C0D0-2ACF-3ECD-A61A-72881DAA4CF3
+  Functions: 847
+  Symbols:   2086
+  CStrings:  2002
 
Symbols:
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:].cold.1
+ -[MitigationHW spatialTemporalRepairThenFuseInplaceYUVInputBuf:frmIdx:frRef0Buf:frRef1Buf:metaBuf:ref0MetaBuf:ref1MetaBuf:metaBufHW:info:infoTPlusOrMinus1:infoTPlusOrMinus2:usePastAsRef:].cold.1
+ _FigSignalErrorAtGM
+ ___block_descriptor_104_e8_32s_e46_v32?0i8I12^{__CFDictionary=}16^{__CFArray=}24ls32l8
+ ___block_descriptor_68_e8_32s_e31_v24?0i8I12^{__CFDictionary=}16ls32l8
+ _fig_log_get_emitter
- -[CMIVideoDeghostingV3 _extractAndCheckTuningParameters:].cold.2
- -[CMIVideoDeghostingV3 _extractAndCheckTuningParameters:].cold.3
- -[CMIVideoDeghostingV3 _extractAndCheckTuningParameters:].cold.4
- -[GGMMetalToolBox initWithMetalContext:].cold.1
- -[GGMMetalToolBox initWithMetalContext:].cold.2
- -[GGMMetalToolBox initWithMetalContext:].cold.3
- -[GGMMetalToolBox initWithMetalContext:].cold.4
- -[GGMMetalToolBox initWithMetalContext:tuningParamDict:].cold.1
- -[GGMMetalToolBoxHWSim initWithMetalContext:tuningParamDict:].cold.1
- -[GGMMetalToolBoxHWSim initWithMetalContext:tuningParamDict:].cold.2
- -[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:].cold.1
- -[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:].cold.2
- -[RepairWeightsGenerator updateQueuesWithInputFrame:info:meta:meta_HW:index:].cold.1
- -[VEVideoDeghostingDetectionAndTrackingV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.1
- -[VEVideoDeghostingDetectionAndTrackingV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.2
- -[VEVideoDeghostingDetectionAndTrackingV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.3
- -[VEVideoDeghostingRepairV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.1
- -[VEVideoDeghostingRepairV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.2
- -[VEVideoDeghostingRepairV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.3
- -[VEVideoDeghostingRepairV3 initWithMetalContext:imageDimensions:tuningParameters:].cold.4
- -[VideoMitigation initWithConfig:metalContext:imageDimensions:tuningParameters:].cold.1
- -[VideoMitigation initWithConfig:metalContext:imageDimensions:tuningParameters:].cold.2
- -[VideoMitigation initWithConfig:metalContext:imageDimensions:tuningParameters:].cold.3
- -[VideoMitigation updateMetaQueuesWithInfo:index:].cold.1
- -[VideoMitigation updateMetaQueuesWithInfo:index:].cold.2
- -[VideoMitigation updateMetaQueuesWithInfo:index:].cold.3
- -[VideoMitigation updateQueuesWithFutureFrame:futureFrameIndex:atBaseIndex:].cold.1
- -[VideoMitigation updateQueuesWithFutureFrame:futureFrameIndex:atBaseIndex:].cold.2
- _FigSignalErrorAt3
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___block_descriptor_112_e8_32s_e46_v32?0i8I12^{__CFDictionary=}16^{__CFArray=}24ls32l8
- ___block_descriptor_76_e8_32s_e31_v24?0i8I12^{__CFDictionary=}16ls32l8
- _gVEDetectionAndTrackingTrace
- _gVERepairTrace
- _gVEVideoDeghostingV3
- createSingleCachedTextureFromPixelBuffer.cold.1
- createSingleCachedTextureFromPixelBuffer.cold.2
- createSingleCachedTextureFromPixelBuffer.cold.3
- createSingleCachedTextureFromPixelBuffer.cold.4
- createSingleCachedTextureFromPixelBuffer.cold.5
- syncWeightsSpatial.cold.1
- syncWeightsSpatialForSWWeights.cold.1
- warpPrevMetaBuffer.cold.1
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "( -73465 )"
- "-[CMIVideoDeghostingV3 _extractAndCheckTuningParameters:]"
- "-[CMIVideoDeghostingV3 _shouldResetRepair:]"
- "-[CMIVideoDeghostingV3 _shouldRunRepair:]"
- "-[CMIVideoDeghostingV3 finishProcessing]"
- "-[CMIVideoDeghostingV3 initGhostInformationLookAheadForSize:]"
- "-[CMIVideoDeghostingV3 initWithCommandQueue:imageDimensions:tuningParameters:]"
- "-[CMIVideoDeghostingV3 process]"
- "-[CMIVideoDeghostingV3 resetState]"
- "-[CMIVideoDeghostingV3 setSensorBinningFactorHorizontal:]"
- "-[CMIVideoDeghostingV3 setSensorBinningFactorVertical:]"
- "-[CMIVideoDeghostingV3 statistics]"
- "-[GGMController buildInputParamsToRepairFromMetaInfo:andDetectedResults:lookaheadDetectedResults:]"
- "-[GGMController initWithConfig:metalContext:imageDimensions:tuningParameters:forDetection:]"
- "-[GGMController initWithConfigDict:metalContext:imageDimensions:forDetection:]"
- "-[GGMController setConfigureFromDefaultsWrite:]"
- "-[GGMController updateConfig:withConfigureDict:]"
- "-[GGMMetalToolBox _compileShaders]"
- "-[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:]"
- "-[GGMMetalToolBox initWithMetalContext:]"
- "-[GGMMetalToolBox initWithMetalContext:tuningParamDict:]"
- "-[GGMMetalToolBox setRepairTuningParams:withDict:]"
- "-[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:frameDim:lightSourceMaskTotalArea:]"
- "-[GGMMetalToolBoxHWSim initWithMetalContext:tuningParamDict:]"
- "-[MaskToRoi getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:]"
- "-[MaskToRoi getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:]"
- "-[MitigationHW spatialTemporalRepairThenFuseInplaceYUVInputBuf:frmIdx:frRef0Buf:frRef1Buf:metaBuf:ref0MetaBuf:ref1MetaBuf:metaBufHW:info:infoTPlusOrMinus1:infoTPlusOrMinus2:usePastAsRef:]"
- "-[MitigationHW spatialTemporalRepairThenFuseInplaceYUVInputBuf:frmIdx:frRef0Buf:frRef1Buf:metaBuf:ref0MetaBuf:ref1MetaBuf:metaBufHW:info:infoTPlusOrMinus1:infoTPlusOrMinus2:usePastAsRef:]_block_invoke"
- "-[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:]"
- "-[RepairWeightsGenerator computeBlendingWeightsYUVInputBuf:frRef0Buf:frRef1Buf:hmgrphy0:hmgrphy1:frmIdx:metadataBuf:meta_HW:metaTPlusOrMinus1_HW:metaTPlusOrMinus2_HW:]_block_invoke"
- "-[RepairWeightsGenerator updateQueuesWithInputFrame:info:meta:meta_HW:index:]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 dealloc]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 finishProcessing]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 initWithMetalContext:imageDimensions:tuningParameters:]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 prepareToProcess:]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 prewarm]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 process]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 resetState]"
- "-[VEVideoDeghostingDetectionAndTrackingV3 setup]"
- "-[VEVideoDeghostingRepairV3 collectDetectionResultsForLookAheadBuffer:]"
- "-[VEVideoDeghostingRepairV3 dealloc]"
- "-[VEVideoDeghostingRepairV3 finishProcessing]"
- "-[VEVideoDeghostingRepairV3 initWithMetalContext:imageDimensions:tuningParameters:]"
- "-[VEVideoDeghostingRepairV3 prepareToProcess:]"
- "-[VEVideoDeghostingRepairV3 prewarm]"
- "-[VEVideoDeghostingRepairV3 process]"
- "-[VEVideoDeghostingRepairV3 resetState]"
- "-[VEVideoDeghostingRepairV3 setup]"
- "-[VideoDeghostingDetectionV3 _initParamsWithTuningParamsDict:isLowLight:]"
- "-[VideoDeghostingDetectionV3 getRoisFromPackedHwLsMask:opticalCenter:prevMetaContainer:considerDist2PrevGhostWhenSort:lightSourceMaskTotalArea:]"
- "-[VideoDeghostingDetectionV3 initWithMetalContext:config:tuningParamDict:imageDimensions:]"
- "-[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:]"
- "-[VideoDeghostingDetectionV3 process:metaData:ispTimeStamp:keypoints:lightSourceMask:futureFrames:]"
- "-[VideoMitigation initWithConfig:metalContext:imageDimensions:tuningParameters:]"
- "-[VideoMitigation updateMetaQueuesWithInfo:index:]"
- "-[VideoMitigation updateQueuesWithFutureFrame:futureFrameIndex:atBaseIndex:]"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Called"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: ghost look-ahead size:    %d"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: horizontal binning:          %d"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: input dimensions:            %d x %d"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: lux level gating enabled:    %s"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: lux level hysteresis:        [%d;%d]"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: repair enabled:              %s"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Configuration: vertical binning:            %d"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Detection pipe was reset, reset the repair pipe"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Gating disabled: turning ON video deghosting"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Keeping repair %s"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Keeping video deghosting %s"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Repair bypassed"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Statistics: opticalCenterMag = %f, opticalCenterOffsetX = %f, opticalCenterOffsetY = %f, opticalCenterEstConfidence = %f, averageGhostCount = %f, averageGhostArea = %f"
- "<<<< CMIVideoDeghostingV3 >>>> %s: Turning OFF and reset repair function because there is no valid detection result"
- "<<<< CMIVideoDeghostingV3 >>>> %s: called"
- "<<<< VEVideoDeghostingDetectionAndTrackingV3 >>>> %s: Called"
- "<<<< VEVideoDeghostingDetectionAndTrackingV3 >>>> %s: Unable to initialize green ghost controller"
- "<<<< VEVideoDeghostingDetectionAndTrackingV3 >>>> %s: look ahead frame extraction in detection failed"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: Called"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: Configuration: input dimensions:            %d x %d"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: Unable to initialize VERepair"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: Unable to initialize green ghost controller"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: detection did not run on frame: %d, skipping the following frames"
- "<<<< VEVideoDeghostingRepairV3 >>>> %s: look ahead frame extraction in repair failed"
- "<<<< VEVideoDeghostingV3 >>>> %s:  format: %c%c%c%c can't be supported"
- "<<<< VEVideoDeghostingV3 >>>> %s: # of LS bbox(es): %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: # of ROI(s) to repair: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: BBox Weight[%d] strongSpatialWeight:%f, spatialWeight:%f, spatioTemporalWeight:%f\n"
- "<<<< VEVideoDeghostingV3 >>>> %s: BBox[%d]: MaxGrad: %d, MaxDiff: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: BBox[%d]: SSPA_HW: %.4f, SPA_HW: %.4f"
- "<<<< VEVideoDeghostingV3 >>>> %s: Configuration: lookaheadFrames array size:    %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: Detected ROI count exceeds the limit of %d. Some ROIs are not packed to repair"
- "<<<< VEVideoDeghostingV3 >>>> %s: Empty input"
- "<<<< VEVideoDeghostingV3 >>>> %s: Empty lookahead data"
- "<<<< VEVideoDeghostingV3 >>>> %s: Error!. Frame %ld, VTDeghostingSessionMitigateGhosts returned error = %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: Error. Frame %ld, Repair failed"
- "<<<< VEVideoDeghostingV3 >>>> %s: Error. Frame %ld, Statistics failed"
- "<<<< VEVideoDeghostingV3 >>>> %s: Error: format is not supported "
- "<<<< VEVideoDeghostingV3 >>>> %s: Frame #%d repair done (err = %d)"
- "<<<< VEVideoDeghostingV3 >>>> %s: Frame %ld: Stats done (err = %d)"
- "<<<< VEVideoDeghostingV3 >>>> %s: GG count: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: GGCount buffer is not in the range. GGCount: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: Input buffer is NULL. Current: %p, Ref0: %p Ref1: %p"
- "<<<< VEVideoDeghostingV3 >>>> %s: Key -(%s) is not valid init option"
- "<<<< VEVideoDeghostingV3 >>>> %s: Metal tool box shaders compilation failed"
- "<<<< VEVideoDeghostingV3 >>>> %s: Null detection results"
- "<<<< VEVideoDeghostingV3 >>>> %s: ROI to repair: (%f, %f), (%f, %f)"
- "<<<< VEVideoDeghostingV3 >>>> %s: Total Clipped Pixels Count (scale adjusted): %f"
- "<<<< VEVideoDeghostingV3 >>>> %s: Total area to repair (before potential rescaling from perf control): %.2f"
- "<<<< VEVideoDeghostingV3 >>>> %s: Tuning parameters not given from plist, will use macros"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to cache pixel buffer texture"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to get metal texture address"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to initialize HW mitigator"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to initialize Pixel memory class"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to initialize homography instance"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to initialize metal tool box"
- "<<<< VEVideoDeghostingV3 >>>> %s: Unable to initialize video mitigation"
- "<<<< VEVideoDeghostingV3 >>>> %s: Using AVE"
- "<<<< VEVideoDeghostingV3 >>>> %s: Using GPU emulation"
- "<<<< VEVideoDeghostingV3 >>>> %s: [GGM MSG] The video is captured in %@ light enviroment: "
- "<<<< VEVideoDeghostingV3 >>>> %s: [GGM MSG] The video is forced to bright light mode"
- "<<<< VEVideoDeghostingV3 >>>> %s: [GGM MSG] The video is forced to low light mode"
- "<<<< VEVideoDeghostingV3 >>>> %s: [GGM MSG] Version %d.%d"
- "<<<< VEVideoDeghostingV3 >>>> %s: bbox count %ld exceeds the limit: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: buffer is NULL"
- "<<<< VEVideoDeghostingV3 >>>> %s: cmivdg_force_lossless_format = %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: cmivdg_sync_ave = %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: cmivdg_use_gpumodel = %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: detection result in look-ahead frame %d is nil, detection might be reset !"
- "<<<< VEVideoDeghostingV3 >>>> %s: format is not supported in this function"
- "<<<< VEVideoDeghostingV3 >>>> %s: light source bounding box count: %ld exeed the limit: %d"
- "<<<< VEVideoDeghostingV3 >>>> %s: meta buffer is NULL"
- "<<<< VEVideoDeghostingV3 >>>> %s: meta buffer is null"
- "<<<< VEVideoDeghostingV3 >>>> %s: meta buffer not available"
- "<<<< VEVideoDeghostingV3 >>>> %s: nil detection metadata"
- "<<<< VEVideoDeghostingV3 >>>> %s: nil metadata from detection"
- "<<<< VEVideoDeghostingV3 >>>> %s: pixelBuffer is NULL"
- "<<<< VEVideoDeghostingV3 >>>> %s: stashedMeta buffer is null"
- "<<<< VEVideoDeghostingV3 >>>> %s: total clipped pixel count is not enough, detection is skipped"
- "<<<< VEVideoDeghostingV3 >>>> %s: total cluster is %d, bigger than limit, not all GGs are mitigated "
- "<<<< VEVideoDeghostingV3 >>>> %s: warped/prevMeta buffers not available"
- "CreateBoundingBoxWeightsWithMetadata"
- "NO"
- "OFF"
- "ON"
- "Repair parameters are missing"
- "Unable to create a metal texture cache"
- "YES"
- "_bmSearch1RefFixedSampleCntYUV is NULL"
- "_bmTransferGray is NULL"
- "_bmTransferGray2RefsLowLight is NULL"
- "_bmTransferGray3RefsLowLight is NULL"
- "_bmTransferGray4RefsLowLight is NULL"
- "_bmTransferYUV is NULL"
- "_collectClusterMaxAndAvgLuma is NULL"
- "_collectClusterMaxProb is NULL"
- "_collectClusterMv is NULL"
- "_collectClusterTempRepairErr is NULL"
- "_collectMetaContainers is NULL"
- "_collectOpticalCenterEstStats is NULL"
- "_combineMapWithRefMap is NULL"
- "_combineMapWithRefMapLite is NULL"
- "_conditionalDilate2ProbMapsYUVHardR2SoftR2Simd is NULL"
- "_conditionalDilateProbMapYUV is NULL"
- "_conditionalDilateProbMapYUVHardR2SoftR2Simd is NULL"
- "_copyInput4DetectionYUV is NULL"
- "_dilate2ProbMaps is NULL"
- "_dilate3ProbMapsHardR2SoftR2Simd is NULL"
- "_dilateGrayImg is NULL"
- "_dilateProbMap is NULL"
- "_dilateProbMapHardR2SoftR2Simd is NULL"
- "_dilateReflLsMap is NULL"
- "_fuse4DetectionYUV is NULL"
- "_fuseSpatialOnly4DetectionYUV is NULL"
- "_getBlobSaliencyMapYUV is NULL"
- "_getGhostProbMapYUV is NULL"
- "_getMotionMapYUV is NULL"
- "_getMvFromLs is NULL"
- "_getRoiMaxAndAvgLumaYUV is NULL"
- "_getSaliencyMapYUV is NULL"
- "_getTempRepairedBgAlignErrYUV is NULL"
- "_getTrackingHmgrphyAlignmentErrorYUV is NULL"
- "_preprocessInputs4MotionCueYUV is NULL"
- "_refineFutureHwLsMapWithTrackingYUV is NULL"
- "_reflectYUVImg2 is NULL"
- "_setWOri is NULL"
- "_spatialTemporalRepair4DetectionYUV is NULL"
- "_syncStats is NULL"
- "_trackingRoiAvoidListBuf is NULL"
- "_unpackLsMask is NULL"
- "_updateEstOpticalCenterOffset is NULL"
- "_upscaleThenReflectLsMap is NULL"
- "_warpRefMeta is NULL"
- "bright "
- "createSingleCachedTextureFromPixelBuffer"
- "createTextureFromCVPixelBufferWithReadFmt"
- "extractFutureReferenceFrames"
- "fetchOneFrameFromSampleBufferForRepair"
- "getMetalFormat"
- "initLookAheadFrameArray"
- "isLowLightingCondition"
- "kCMBaseObjectError_ParamErr"
- "low "
- "syncWeightsSpatial"
- "syncWeightsSpatialForSWWeights"
- "tuningParameters LuxLevelThresholdOFF missing"
- "tuningParameters LuxLevelThresholdON missing"
- "tuningParameters are missing"
- "vevdg_detection_and_tracking_trace"
- "vevdg_repair_trace"
- "warpPrevMetaBuffer"

```
