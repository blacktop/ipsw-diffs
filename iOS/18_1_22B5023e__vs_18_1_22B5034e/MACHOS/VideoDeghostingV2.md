## VideoDeghostingV2

> `/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x2627c
-  __TEXT.__auth_stubs: 0x7e0
+580.2.0.0.0
+  __TEXT.__text: 0x2df38
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0x1a40
-  __TEXT.__const: 0xe00
+  __TEXT.__const: 0xe20
   __TEXT.__objc_methname: 0x69cc
-  __TEXT.__cstring: 0x3197
+  __TEXT.__cstring: 0x4d35
+  __TEXT.__oslogstring: 0x22f8
   __TEXT.__objc_classname: 0x233
   __TEXT.__objc_methtype: 0x3660
-  __TEXT.__gcc_except_tab: 0x2c8
-  __TEXT.__unwind_info: 0x640
-  __DATA_CONST.__auth_got: 0x408
+  __TEXT.__gcc_except_tab: 0x344
+  __TEXT.__unwind_info: 0x648
+  __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x4a8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x240
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 593
-  Symbols:   191
-  CStrings:  1660
+  Symbols:   195
+  CStrings:  1906
 
Symbols:
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
+ _fig_note_initialize_category_with_default_work_cf
+ __os_log_send_and_compose_impl
- _FigSignalErrorAt
- _fig_log_get_emitter
CStrings:
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because of exposure %!d(MISSING) > %!d(MISSING)"
+ "_integralBinImageRow is NULL"
+ "_metalBuffers.tinyGhostsBuf is NULL"
+ "commandBuffer is NULL"
+ "-[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost cnt (before merge) exceeds soft gating threshold. Only keeping top %!d(MISSING) ghosts"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): detection did not run on frame: %!d(MISSING), skipping the following frames"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): ROI to repair: (%!f(MISSING), %!f(MISSING)), (%!f(MISSING), %!f(MISSING))"
+ "_strongTemporalRepairYUV is NULL"
+ "-[GGMMetalToolBox YCbCrToRGB:outputImage:waitForComplete:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): totalClippedPixelsCount is not enough, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Metal tool box shaders compilation failed"
+ "-[CMIVideoDeghostingV2 setSensorBinningFactorHorizontal:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): meta buffer not available"
+ "-[GGMMetalToolBox initWithMetalContext:tuningParamDict:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: ghost look-ahead size:    %!d(MISSING)"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 initWithMetalContext:imageDimensions:tuningParameters:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize metal tool box"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): _allocateMetalBuffers failed"
+ "-[GGMController buildInputParamsToRepairFromMetaInfo:andDetectedResults:lookaheadDetectedResults:]"
+ "initLookAheadFrameArray"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): light source mask is not available, detection is skipped"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: input dimensions:            %!d(MISSING) x %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total allocate metal buffer size %!d(MISSING) bytes"
+ "-[MaskToRoi getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:]"
+ "getMetalFormat"
+ "_syncMaxLuma is NULL"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): no previous LS ROIs for feature extraction"
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionClippedPixelBased:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Empty input"
+ "_findTinyKPs is NULL"
+ "<<<< VEVideoDeghostingV2 >>>>"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection: GG# %!u(MISSING)"
+ "_metalBuffers.DoGAndLumaFeaturesBuf is NULL"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 dealloc]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lookaheadFrames array size:    %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because of light source count %!d(MISSING) < %!d(MISSING)"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because of exposure %!d(MISSING) < %!d(MISSING)"
+ "_collectClusterStats is NULL"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 finishProcessing]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): ROI count: %!d(MISSING) / GG count: %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total ROI count clipped from %!d(MISSING) to %!d(MISSING) in updateDoGAndLumaFeature for prevLS"
+ "-[VideoDeghostingDetectionV2 initWithMetalToolBox:config:tuningParamDict:imageDimensions:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Keeping repair %!s(MISSING)"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize homography instance"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because clipped pixel count %!d(MISSING) < %!d(MISSING)"
+ "_metalBuffers.DoGAndLumaFeaturesBufForPrevLS is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total Clipped Pixels Count (scale adjusted): %!f(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: repair enabled:              %!s(MISSING)"
+ "_metalBuffers.tinyGhostIdxBuf is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): detection result in look-ahead frame %!d(MISSING) is nil, detection might be reset !"
+ "-[GGMController initWithConfig:metalContext:imageDimensions:tuningParameters:]"
+ "-[VEVideoDeghostingRepairV2 finishProcessing]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to allocate input texture"
+ "_computeBlendingWeightsSpatialOnlyYUV is NULL"
+ "commandBufferForDoGLumaPrev is NULL"
+ "-[GGMMetalToolBox initWithMetalContext:]"
+ "-[VideoDeghostingDetectionV2 _ghostDetectionWithInputPixelBuffer:reflectedLSMaskOri:lowLight:opticalCenterFromMetaData:simKeyPoint:simLightSourceMask:metaData:futureFrames:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize mitigation CPU"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 setup]"
+ "-[VEVideoDeghostingRepairV2 resetState]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen keypoint count: %!d(MISSING)"
+ "-[VEVideoDeghostingRepairV2 prepareToProcess:]"
+ "-[VideoDeghostingDetectionV2 _detectionInit:metaData:futureFrames:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lux level hysteresis:        [%!d(MISSING);%!d(MISSING)]"
+ "_YCbCrToRGB is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): getTopGhostsInList failed to trim Ghost count from %!d(MISSING) to %!d(MISSING)"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Unable to initialize VERepair"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): pixelBuffer is NULL"
+ "-[VideoMitigation updateQueuesWithTwoFutureFrames:atBaseIndex:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total keypoint count clipped from %!d(MISSING) to %!d(MISSING) in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "-[MitigationGPU initWithMetalToolBox:metalContext:imageDimensions:]"
+ "kCMBaseObjectError_ParamErr"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): After pruning w/ trajectory: ROI# %!u(MISSING)"
+ "-[VideoDeghostingDetectionV2 _ghostCandidateGenerationViaKeypointBuffer:opticalCenterFromMetaData:mappingInfo:GGList:LSList:kpCntHardGatingTh:kpCntSoftGatingTh:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lux level gating enabled:    %!s(MISSING)"
+ "-[CMIVideoDeghostingV2 resetState]"
+ "extractFutureReferenceFrames"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): After pruning using matched LS info: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Configuration: input dimensions:            %!d(MISSING) x %!d(MISSING)"
+ "createSingleCachedTextureFromPixelBuffer"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Called"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because clipped pixel count %!d(MISSING) > %!d(MISSING)"
+ "-[GGMMetalToolBox updateMetaContainerBuffer:WithDetectedROI:isLowLight:]"
+ "-[GGMMetalToolBox computeIntegralBinImageFromInput:toIntegral:waitForComplete:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen keypoints are not available, detection is skipped"
+ "-[VEVideoDeghostingRepairV2 collectDetectionResultsForLookAheadBuffer:]"
+ "-[CMIVideoDeghostingV2 process]"
+ "-[CMIVideoDeghostingV2 _shouldRunVideoDeghosting:]"
+ "-[RepairWeightsGenerator updateQueuesWithInputFrame:info:meta:index:]"
+ "-[GGMMetalToolBox computeDiffForLocalMotion:andYUVImage:outputImage:waitForComplete:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): light source bounding box count: %!l(MISSING)d exeed the limit: %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Detection pipe was reset, reset the repair pipe"
+ "-[VDGDetectionUtilsV2 updateDoGAndLumaFeaturesWithMetalBuffers:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): # of ROI(s) to repair: %!d(MISSING)"
+ "low "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection + tracking: GG# %!u(MISSING)"
+ "isLowLightingCondition"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): next frame texture is nil, skipping prev ls box generation"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to cache pixel buffer texture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): homography type: %!d(MISSING) is not supported, force to identity matrix."
+ "-[GGMController initWithConfigDict:metalContext:imageDimensions:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Gating disabled: turning ON video deghosting"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No input texture or prev LS boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Tuning parameters not given from plist, will use macros"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection skipped because of too many light sources"
+ "vevdg_detection_and_tracking_trace"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to get metal texture address"
+ "-1"
+ "-[GGMMetalToolBox backWarpYUV:warped:withHomography:waitForComplete:]"
+ "-[CMIVideoDeghostingV2 initGhostInformationLookAheadForSize:]"
+ "-[MitigationGPU spatialTemporalRepairThenFuseInplaceYUVInput:frRef0:frRef1:trRef0:trRef1:hmgrphy0:hmgrphy1:metaBuf:ref0MetaBuf:ref1MetaBuf:trInput:waitForComplete:]"
+ "_computeBoxDoG is NULL"
+ "-[VEVideoDeghostingRepairV2 setup]"
+ "fetchOneFrameFromSampleBufferForRepair"
+ "-[GGMController updateConfig:withConfigureDict:]"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 resetState]"
+ "_metalBuffers.desGenGhostIdxBuf is NULL"
+ "_findGhostKeypointsFromDesGen is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): meta buffer is null"
+ "_metalBuffers.desGenGhostsBuf is NULL"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: horizontal binning:          %!d(MISSING)"
+ "_computeDiffForLocalMotionYUV is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Before pruning using matched LS info: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No prev LS boxes to updates DoG and luma features"
+ "-[MitigationCPU initWithMetalToolBox:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] Version %!d(MISSING).%!d(MISSING)"
+ "syncWeightsSpatial"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detected ROI count exceeds the limit of %!d(MISSING). Some ROIs are not packed to repair"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize video mitigation"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Null detection results"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): nil metadata from detection"
+ "vevdg_repair_trace"
+ "-[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:]"
+ "-[GGMMetalToolBox _compileShaders]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Tiny ghosts are more than capacity"
+ "<<<< CMIVideoDeghostingV2 >>>>"
+ "ON"
+ "tuningParameters LuxLevelThresholdOFF missing"
+ "-[VEVideoDeghostingRepairV2 initWithMetalContext:imageDimensions:tuningParameters:]"
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionLSBased:]"
+ "-[VideoDeghostingDetectionV2 _initParamsWithTuningParamsDict:isLowLight:]"
+ "-[VEVideoDeghostingRepairV2 dealloc]"
+ "-[VDGDetectionUtilsV2 getTopGhostsInList:k:opticalCenter:ghostCntGatingTh:]"
+ "-[ROI getPixelFeatureMatchCostWith:]"
+ "-[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total area to repair (before potential rescaling from perf control): %!f(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Prev Ghost Id count exceeds Max %!l(MISSING)u "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize gpu mitigator "
+ "vevdg_trace"
+ "-[VideoDeghostingDetectionV2 _allocateMetalBuffers]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): nil detection metadata"
+ "-[CMIVideoDeghostingV2 initWithCommandQueue:imageDimensions:tuningParameters:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is forced to low light mode"
+ "-[VEVideoDeghostingRepairV2 process]"
+ "_metalBuffers.DoGAndLumaTotalBoxesForPrevLS is NULL"
+ "createTextureFromCVPixelBufferWithReadFmt"
+ "OFF"
+ "NO"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total ROI count clipped from %!d(MISSING) to %!d(MISSING) in updateDoGAndLumaFeatures"
+ "Unable to create a metal texture cache"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): LS Gating Disabled. Keeping detecton ON."
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen ghosts are more than capacity"
+ "_computeBlendingWeightsYUV is NULL"
+ "-[VEVideoDeghostingRepairV2 prewarm]"
+ "cmivdg_trace"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): lux Level gated, detection is skipped"
+ "-[VideoDeghostingDetectionV2 _pruneUsingMatchedLSInfo:dilation:]"
+ "_spatialTemporalRepairYUV is NULL"
+ "-[VideoDeghostingDetectionV2 _mergeBboxesWithTrackingForMitigation:prevFrameGhostList:]"
+ "_metalBuffers.tinyGhostInputLocationsSize is NULL"
+ "YES"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF video deghosting due to lux level: %!d(MISSING) > %!d(MISSING)"
+ "_getRefTypeYUV is NULL"
+ "_metalBuffers.DoGAndLumaInputBoxesBufForPrevLS is NULL"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Keeping video deghosting %!s(MISSING)"
+ "bright "
+ "-[CMIVideoDeghostingV2 _shouldRunRepair:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize cpu mitigator"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost cnt (before merge) exceeds hard gating threshold. All ghosts are discarded"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): Called"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because of light source count %!d(MISSING) > %!d(MISSING)"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 process]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is captured in %!@(MISSING) light enviroment: "
+ "_metalBuffers.DoGAndLumaInputBoxesBuf is NULL"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF video deghosting because stream is not from Wide camera"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total key point count exceeds hard gating threshold. Discard all key points"
+ "-[MitigationGPU _compileShaders]"
+ "com.apple.coremedia"
+ "tuningParameters LuxLevelThresholdON missing"
+ "-[CMIVideoDeghostingV2 _extractAndCheckTuningParameters:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Lux Level Gating Disabled. Keeping detecton ON."
+ "-[RepairWeightsGenerator _computeBlendingWeightsYUVInput:frRefTPlusOrMinus1:frRefTPlusOrMinus2:trRefTPlusOrMinus1:trRefTPlusOrMinus2:meta:metaTPlusOrMinus1:metaTPlusOrMinus2:info:infoTPlusOrMinus1:infoTPlusOrMinus2:config:trInput:usePastAsRef:]"
+ "-[CMIVideoDeghostingV2 _shouldResetRepair:]"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): look ahead frame extraction in detection failed"
+ "_fuseYUV is NULL"
+ "-[GGMMetalToolBox setRepairTuningParams:withDict:]"
+ "-[VideoMitigation initWithConfig:metalToolBox:MetalContext:imageDimensions:]"
+ "_metalBuffers.desGenMappingInfoBuf is NULL"
+ "_metalBuffers.DoGAndLumaTotalBoxes is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total light source count clipped from %!d(MISSING) to %!d(MISSING) in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Before pruning w/ trajectory: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): # of LS bbox(es): %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Empty lookahead data"
+ "-[CMIVideoDeghostingV2 setSensorBinningFactorVertical:]"
+ "-[GGMMetalToolBox computeBlendingWeightsSpatialOnlyYUVInput:metadataBuf:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Key -(%!s(MISSING)) is not valid init option"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 prepareToProcess:]"
+ "_metalBuffers.tinyGhostInputLocationsBuf is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): _detectionInit failed"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): look ahead frame extraction in repair failed"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No input locations to find tiny keypoints"
+ "-[VEVideoDeghostingDetectionAndTrackingV2 prewarm]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to create feature descriptor, feature length is zero"
+ "-[VideoMitigation updateQueuesWithInputFrame:info:index:]"
+ "_metalBuffers.reflectedLsBboxListBuf is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): metal buffer is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize gpu mitigator"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: vertical binning:            %!d(MISSING)"
+ "_computeBoxLumaFeatureVector is NULL"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Called"
+ "-[VDGDetectionUtilsV2 pruneUsingTrajectoryGGList:]"
+ "-[GGMMetalToolBox findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture:ref4LocalMotionTexture:inputTPlus1Texture:LSList:desGenKeypoints:homography:colorParams:computeLocalMotion:LSDilation:LSReflectCenter:maxLightSourceCount:maxDesGenKeypoints:maxTinyKeypoints:metalBuffers:isPrevLSFeaturesAvailable:]"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is forced to bright light mode"
+ "_syncRefType is NULL"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning ON video deghosting due to lux level: %!d(MISSING) <= %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost count exceeds Max prev %!l(MISSING)u and cur %!l(MISSING)u "
+ "_backwarpWithHomographyYUV is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING):  format: %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) can't be supported"
+ "-[VideoDeghostingDetectionV2 _trackGhosts:ghostCandidates:LSList:]"
+ "_getGhostMaxLumaYUV is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): packed format is not supported in this function"
+ "Repair parameters are missing"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total Key points count clipped from %!l(MISSING)u to %!d(MISSING) "
+ "-[VideoDeghostingDetectionV2 _shouldRunGGDetectionLuxLevelBased:]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF and reset repair function because there is no valid detection result"
+ "tuningParameters are missing"
+ "_integralBinImageCol is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): stashedMeta buffer is null"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): total cluster is %!d(MISSING), bigger than limit, not all GGs are mitigated "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to create feature descriptor, feature sums are zero"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Clipped pixel-based Gating Disabled. Keeping detecton ON."

```
