## VideoDeghostingV2

> `/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2`

```diff

-664.62.12.0.0
-  __TEXT.__text: 0x2757c
-  __TEXT.__auth_stubs: 0x7f0
+665.80.6.0.0
+  __TEXT.__text: 0x2e848
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x3080
   __TEXT.__objc_methlist: 0x1e0c
   __TEXT.__const: 0xe70
   __TEXT.__objc_methname: 0x6a28
-  __TEXT.__cstring: 0x329c
+  __TEXT.__cstring: 0x4de8
+  __TEXT.__oslogstring: 0x237c
   __TEXT.__objc_classname: 0x233
   __TEXT.__objc_methtype: 0x369b
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__oslogstring: 0x74
-  __TEXT.__unwind_info: 0x6d0
-  __DATA_CONST.__auth_got: 0x410
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__unwind_info: 0x730
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x180
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A9C0753-34CB-39F1-BD9A-7C0A9DAF61FD
-  Functions: 796
-  Symbols:   192
-  CStrings:  1746
+  UUID: 498114A6-ED45-3587-A403-C4B70F4391F5
+  Functions: 853
+  Symbols:   195
+  CStrings:  1996
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
- _FigSignalErrorAtGM
- _fig_log_get_emitter
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[CMIVideoDeghostingV2 _extractAndCheckTuningParameters:]"
+ "-[CMIVideoDeghostingV2 _shouldResetRepair:]"
+ "-[CMIVideoDeghostingV2 _shouldRunRepair:]"
+ "-[CMIVideoDeghostingV2 _shouldRunVideoDeghosting:]"
+ "-[CMIVideoDeghostingV2 initGhostInformationLookAheadForSize:]"
+ "-[CMIVideoDeghostingV2 initWithCommandQueue:imageDimensions:tuningParameters:]"
+ "-[CMIVideoDeghostingV2 process]"
+ "-[CMIVideoDeghostingV2 resetState]"
+ "-[CMIVideoDeghostingV2 setSensorBinningFactorHorizontal:]"
+ "-[CMIVideoDeghostingV2 setSensorBinningFactorVertical:]"
+ "-[GGMController buildInputParamsToRepairFromMetaInfo:andDetectedResults:lookaheadDetectedResults:]"
+ "-[GGMController initWithConfig:metalContext:imageDimensions:tuningParameters:]"
+ "-[GGMController initWithConfigDict:metalContext:imageDimensions:]"
+ "-[GGMController updateConfig:withConfigureDict:]"
+ "-[GGMMetalToolBox YCbCrToRGB:outputImage:waitForComplete:]"
+ "-[GGMMetalToolBox _compileShaders]"
+ "-[GGMMetalToolBox backWarpYUV:warped:withHomography:waitForComplete:]"
+ "-[GGMMetalToolBox computeBlendingWeightsSpatialOnlyYUVInput:metadataBuf:]"
+ "-[GGMMetalToolBox computeDiffForLocalMotion:andYUVImage:outputImage:waitForComplete:]"
+ "-[GGMMetalToolBox computeIntegralBinImageFromInput:toIntegral:waitForComplete:]"
+ "-[GGMMetalToolBox findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture:ref4LocalMotionTexture:inputTPlus1Texture:LSList:desGenKeypoints:homography:colorParams:computeLocalMotion:LSDilation:LSReflectCenter:maxLightSourceCount:maxDesGenKeypoints:maxTinyKeypoints:metalBuffers:isPrevLSFeaturesAvailable:]"
+ "-[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:]"
+ "-[GGMMetalToolBox initWithMetalContext:]"
+ "-[GGMMetalToolBox initWithMetalContext:tuningParamDict:]"
+ "-[GGMMetalToolBox setRepairTuningParams:withDict:]"
+ "-[GGMMetalToolBox updateMetaContainerBuffer:WithDetectedROI:isLowLight:]"
+ "-[MaskToRoi getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:]"
+ "-[MitigationCPU initWithMetalToolBox:]"
+ "-[MitigationGPU _compileShaders]"
+ "-[MitigationGPU initWithMetalToolBox:metalContext:imageDimensions:]"
+ "-[MitigationGPU spatialTemporalRepairThenFuseInplaceYUVInput:frRef0:frRef1:trRef0:trRef1:hmgrphy0:hmgrphy1:metaBuf:ref0MetaBuf:ref1MetaBuf:trInput:waitForComplete:]"
+ "-[ROI getPixelFeatureMatchCostWith:]"
+ "-[RepairWeightsGenerator _computeBlendingWeightsYUVInput:frRefTPlusOrMinus1:frRefTPlusOrMinus2:trRefTPlusOrMinus1:trRefTPlusOrMinus2:meta:metaTPlusOrMinus1:metaTPlusOrMinus2:info:infoTPlusOrMinus1:infoTPlusOrMinus2:config:trInput:usePastAsRef:]"
+ "-[RepairWeightsGenerator updateQueuesWithInputFrame:info:meta:index:]"
+ "-[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:]"
+ "-[VDGDetectionUtilsV2 getTopGhostsInList:k:opticalCenter:ghostCntGatingTh:]"
+ "-[VDGDetectionUtilsV2 pruneUsingTrajectoryGGList:]"
+ "-[VDGDetectionUtilsV2 updateDoGAndLumaFeaturesWithMetalBuffers:]"
+ "-[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 dealloc]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 finishProcessing]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 initWithMetalContext:imageDimensions:tuningParameters:]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 prepareToProcess:]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 prewarm]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 process]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 resetState]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 setup]"
+ "-[VEVideoDeghostingRepairV2 collectDetectionResultsForLookAheadBuffer:]"
+ "-[VEVideoDeghostingRepairV2 dealloc]"
+ "-[VEVideoDeghostingRepairV2 finishProcessing]"
+ "-[VEVideoDeghostingRepairV2 initWithMetalContext:imageDimensions:tuningParameters:]"
+ "-[VEVideoDeghostingRepairV2 prepareToProcess:]"
+ "-[VEVideoDeghostingRepairV2 prewarm]"
+ "-[VEVideoDeghostingRepairV2 process]"
+ "-[VEVideoDeghostingRepairV2 resetState]"
+ "-[VEVideoDeghostingRepairV2 setup]"
+ "-[VideoDeghostingDetectionV2 _allocateMetalBuffers]"
+ "-[VideoDeghostingDetectionV2 _detectionInit:metaData:futureFrames:]"
+ "-[VideoDeghostingDetectionV2 _ghostCandidateGenerationViaKeypointBuffer:opticalCenterFromMetaData:mappingInfo:GGList:LSList:kpCntHardGatingTh:kpCntSoftGatingTh:]"
+ "-[VideoDeghostingDetectionV2 _ghostDetectionWithInputPixelBuffer:reflectedLSMaskOri:lowLight:opticalCenterFromMetaData:simKeyPoint:simLightSourceMask:metaData:futureFrames:]"
+ "-[VideoDeghostingDetectionV2 _initParamsWithTuningParamsDict:isLowLight:]"
+ "-[VideoDeghostingDetectionV2 _mergeBboxesWithTrackingForMitigation:prevFrameGhostList:]"
+ "-[VideoDeghostingDetectionV2 _pruneUsingMatchedLSInfo:dilation:]"
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionClippedPixelBased:]"
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionLSBased:]"
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionLuxLevelBased:]"
+ "-[VideoDeghostingDetectionV2 _trackGhosts:ghostCandidates:LSList:]"
+ "-[VideoDeghostingDetectionV2 initWithMetalToolBox:config:tuningParamDict:imageDimensions:]"
+ "-[VideoMitigation initWithConfig:metalToolBox:MetalContext:imageDimensions:]"
+ "-[VideoMitigation updateQueuesWithInputFrame:info:index:]"
+ "-[VideoMitigation updateQueuesWithTwoFutureFrames:atBaseIndex:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Called"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: ghost look-ahead size:    %d"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: horizontal binning:          %d"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: input dimensions:            %d x %d"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: lux level gating enabled:    %s"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: lux level hysteresis:        [%d;%d]"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: repair enabled:              %s"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Configuration: vertical binning:            %d"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Detection pipe was reset, reset the repair pipe"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Gating disabled: turning ON video deghosting"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Keeping repair %s"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Keeping video deghosting %s"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Turning OFF and reset repair function because there is no valid detection result"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Turning OFF video deghosting because stream is not from Wide camera"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Turning OFF video deghosting due to lux level: %d > %d"
+ "<<<< CMIVideoDeghostingV2 >>>> %s: Turning ON video deghosting due to lux level: %d <= %d"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %s: Called"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %s: Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %s: look ahead frame extraction in detection failed"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: Called"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: Configuration: input dimensions:            %d x %d"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: Unable to initialize VERepair"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: detection did not run on frame: %d, skipping the following frames"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %s: look ahead frame extraction in repair failed"
+ "<<<< VEVideoDeghostingV2 >>>> %s:  format: %c%c%c%c can't be supported"
+ "<<<< VEVideoDeghostingV2 >>>> %s: # of LS bbox(es): %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: # of ROI(s) to repair: %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: After pruning using matched LS info: ROI# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: After pruning w/ trajectory: ROI# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Before pruning using matched LS info: ROI# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Before pruning w/ trajectory: ROI# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Clipped pixel-based Gating Disabled. Keeping detection ON."
+ "<<<< VEVideoDeghostingV2 >>>> %s: Configuration: lookaheadFrames array size:    %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: DesGen KeypointDescriptorData are not available, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %s: DesGen ghosts are more than capacity"
+ "<<<< VEVideoDeghostingV2 >>>> %s: DesGen keypoint count: %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Detected ROI count exceeds the limit of %d. Some ROIs are not packed to repair"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Detection + tracking: GG# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Detection skipped because of too many light sources"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Detection: GG# %u"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Empty input"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Empty lookahead data"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Ghost cnt (before merge) exceeds hard gating threshold. All ghosts are discarded"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Ghost cnt (before merge) exceeds soft gating threshold. Only keeping top %d ghosts"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Ghost count exceeds Max prev %lu and cur %lu "
+ "<<<< VEVideoDeghostingV2 >>>> %s: Key -(%s) is not valid init option"
+ "<<<< VEVideoDeghostingV2 >>>> %s: LS Gating Disabled. Keeping detection ON."
+ "<<<< VEVideoDeghostingV2 >>>> %s: LightSourceMask is not available, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Lux Level Gating Disabled. Keeping detection ON."
+ "<<<< VEVideoDeghostingV2 >>>> %s: Metal tool box shaders compilation failed"
+ "<<<< VEVideoDeghostingV2 >>>> %s: No boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %s: No input locations to find tiny keypoints"
+ "<<<< VEVideoDeghostingV2 >>>> %s: No input texture or prev LS boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %s: No prev LS boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Null detection results"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Prev Ghost Id count exceeds Max %lu "
+ "<<<< VEVideoDeghostingV2 >>>> %s: ROI count: %d / GG count: %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: ROI to repair: (%f, %f), (%f, %f)"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Tiny ghosts are more than capacity"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total Clipped Pixels Count (scale adjusted): %f"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total Key points count clipped from %lu to %d "
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total ROI count clipped from %d to %d in updateDoGAndLumaFeature for prevLS"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total ROI count clipped from %d to %d in updateDoGAndLumaFeatures"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total allocate metal buffer size %d bytes"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total area to repair (before potential rescaling from perf control): %.2f"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total key point count exceeds hard gating threshold. Discard all key points"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total keypoint count clipped from %d to %d in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Total light source count clipped from %d to %d in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Tuning parameters not given from plist, will use macros"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection OFF because clipped pixel count %d < %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection OFF because of exposure %d > %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection OFF because of light source count %d > %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection back ON because clipped pixel count %d > %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection back ON because of exposure %d < %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Turning detection back ON because of light source count %d < %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to allocate input texture"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to create feature descriptor, feature length is zero"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to create feature descriptor, feature sums are zero"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to get metal texture address"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize cpu mitigator"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize gpu mitigator"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize gpu mitigator "
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize homography instance"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize metal tool box"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize mitigation CPU"
+ "<<<< VEVideoDeghostingV2 >>>> %s: Unable to initialize video mitigation"
+ "<<<< VEVideoDeghostingV2 >>>> %s: [GGM MSG] The video is captured in %@ light environment: "
+ "<<<< VEVideoDeghostingV2 >>>> %s: [GGM MSG] The video is forced to bright light mode"
+ "<<<< VEVideoDeghostingV2 >>>> %s: [GGM MSG] The video is forced to low light mode"
+ "<<<< VEVideoDeghostingV2 >>>> %s: [GGM MSG] Version %d.%d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: _allocateMetalBuffers failed"
+ "<<<< VEVideoDeghostingV2 >>>> %s: _detectionInit failed"
+ "<<<< VEVideoDeghostingV2 >>>> %s: detection result in look-ahead frame %d is nil, detection might be reset !"
+ "<<<< VEVideoDeghostingV2 >>>> %s: getTopGhostsInList failed to trim Ghost count from %d to %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: homography type: %d is not supported, force to identity matrix."
+ "<<<< VEVideoDeghostingV2 >>>> %s: light source bounding box count: %ld exceed the limit: %d"
+ "<<<< VEVideoDeghostingV2 >>>> %s: lux Level gated, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %s: meta buffer is null"
+ "<<<< VEVideoDeghostingV2 >>>> %s: meta buffer not available"
+ "<<<< VEVideoDeghostingV2 >>>> %s: metal buffer is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %s: next frame texture is nil, skipping prev ls box generation"
+ "<<<< VEVideoDeghostingV2 >>>> %s: nil detection metadata"
+ "<<<< VEVideoDeghostingV2 >>>> %s: nil metadata from detection"
+ "<<<< VEVideoDeghostingV2 >>>> %s: no previous LS ROIs for feature extraction"
+ "<<<< VEVideoDeghostingV2 >>>> %s: packed format is not supported in this function"
+ "<<<< VEVideoDeghostingV2 >>>> %s: pixelBuffer is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %s: stashedMeta buffer is null"
+ "<<<< VEVideoDeghostingV2 >>>> %s: total cluster is %d, bigger than limit, not all GGs are mitigated "
+ "<<<< VEVideoDeghostingV2 >>>> %s: totalClippedPixelsCount is not enough, detection is skipped"
+ "NO"
+ "OFF"
+ "ON"
+ "Repair parameters are missing"
+ "Unable to create a metal texture cache"
+ "YES"
+ "_YCbCrToRGB is NULL"
+ "_backwarpWithHomographyYUV is NULL"
+ "_collectClusterStats is NULL"
+ "_computeBlendingWeightsSpatialOnlyYUV is NULL"
+ "_computeBlendingWeightsYUV is NULL"
+ "_computeBoxDoG is NULL"
+ "_computeBoxLumaFeatureVector is NULL"
+ "_computeDiffForLocalMotionYUV is NULL"
+ "_findGhostKeypointsFromDesGen is NULL"
+ "_findTinyKPs is NULL"
+ "_fuseYUV is NULL"
+ "_getGhostMaxLumaYUV is NULL"
+ "_getRefTypeYUV is NULL"
+ "_integralBinImageCol is NULL"
+ "_integralBinImageRow is NULL"
+ "_metalBuffers.DoGAndLumaFeaturesBuf is NULL"
+ "_metalBuffers.DoGAndLumaFeaturesBufForPrevLS is NULL"
+ "_metalBuffers.DoGAndLumaInputBoxesBuf is NULL"
+ "_metalBuffers.DoGAndLumaInputBoxesBufForPrevLS is NULL"
+ "_metalBuffers.DoGAndLumaTotalBoxes is NULL"
+ "_metalBuffers.DoGAndLumaTotalBoxesForPrevLS is NULL"
+ "_metalBuffers.desGenGhostIdxBuf is NULL"
+ "_metalBuffers.desGenGhostsBuf is NULL"
+ "_metalBuffers.desGenMappingInfoBuf is NULL"
+ "_metalBuffers.reflectedLsBboxListBuf is NULL"
+ "_metalBuffers.tinyGhostIdxBuf is NULL"
+ "_metalBuffers.tinyGhostInputLocationsBuf is NULL"
+ "_metalBuffers.tinyGhostInputLocationsSize is NULL"
+ "_metalBuffers.tinyGhostsBuf is NULL"
+ "_spatialTemporalRepairYUV is NULL"
+ "_strongTemporalRepairYUV is NULL"
+ "_syncMaxLuma is NULL"
+ "_syncRefType is NULL"
+ "bright "
+ "cmivdg_trace"
+ "com.apple.coremedia"
+ "commandBuffer is NULL"
+ "commandBufferForDoGLumaPrev is NULL"
+ "createSingleCachedTextureFromPixelBuffer"
+ "createTextureFromCVPixelBufferWithReadFmt"
+ "extractFutureReferenceFrames"
+ "fetchOneFrameFromSampleBufferForRepair"
+ "getMetalFormat"
+ "initLookAheadFrameArray"
+ "isLowLightingCondition"
+ "kCMBaseObjectError_ParamErr"
+ "low "
+ "syncWeightsSpatial"
+ "tuningParameters LuxLevelThresholdOFF missing"
+ "tuningParameters LuxLevelThresholdON missing"
+ "tuningParameters are missing"
+ "vevdg_detection_and_tracking_trace"
+ "vevdg_repair_trace"
+ "vevdg_trace"
- "%s signalled err=%d at <>:%d"

```
