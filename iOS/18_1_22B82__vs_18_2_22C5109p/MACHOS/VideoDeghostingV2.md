## VideoDeghostingV2

> `/System/Library/VideoProcessors/VideoDeghostingV2.bundle/VideoDeghostingV2`

```diff

-580.14.5.0.0
-  __TEXT.__text: 0x262ac
-  __TEXT.__auth_stubs: 0x7e0
+587.60.6.0.0
+  __TEXT.__text: 0x2e104
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0x1a40
-  __TEXT.__const: 0xe00
+  __TEXT.__const: 0xe20
   __TEXT.__objc_methname: 0x69cc
-  __TEXT.__cstring: 0x3197
+  __TEXT.__cstring: 0x4d63
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
+  __DATA_CONST.__cfstring: 0xba0
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
+  CStrings:  1909
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAt
- _fig_log_get_emitter
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "%!s(MISSING)_C_%!d(MISSING)x%!d(MISSING).%!@(MISSING)"
+ "%!s(MISSING)_F_%!d(MISSING)x%!d(MISSING).%!@(MISSING)"
+ "%!s(MISSING)_L_%!d(MISSING)x%!d(MISSING).%!@(MISSING)"
+ "%!s(MISSING)_R_%!d(MISSING)x%!d(MISSING).%!@(MISSING)"
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
+ "<<<< CMIVideoDeghostingV2 >>>>"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Called"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: ghost look-ahead size:    %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: horizontal binning:          %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: input dimensions:            %!d(MISSING) x %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lux level gating enabled:    %!s(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lux level hysteresis:        [%!d(MISSING);%!d(MISSING)]"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: repair enabled:              %!s(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Configuration: vertical binning:            %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Detection pipe was reset, reset the repair pipe"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Gating disabled: turning ON video deghosting"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Keeping repair %!s(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Keeping video deghosting %!s(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF and reset repair function because there is no valid detection result"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF video deghosting because stream is not from Wide camera"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning OFF video deghosting due to lux level: %!d(MISSING) > %!d(MISSING)"
+ "<<<< CMIVideoDeghostingV2 >>>> %!s(MISSING): Turning ON video deghosting due to lux level: %!d(MISSING) <= %!d(MISSING)"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): Called"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingDetectionAndTrackingV2 >>>> %!s(MISSING): look ahead frame extraction in detection failed"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Called"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Configuration: input dimensions:            %!d(MISSING) x %!d(MISSING)"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Unable to initialize VERepair"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): Unable to initialize green ghost controller"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): detection did not run on frame: %!d(MISSING), skipping the following frames"
+ "<<<< VEVideoDeghostingRepairV2 >>>> %!s(MISSING): look ahead frame extraction in repair failed"
+ "<<<< VEVideoDeghostingV2 >>>>"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING):  format: %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) can't be supported"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): # of LS bbox(es): %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): # of ROI(s) to repair: %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): After pruning using matched LS info: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): After pruning w/ trajectory: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Before pruning using matched LS info: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Before pruning w/ trajectory: ROI# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Clipped pixel-based Gating Disabled. Keeping detecton ON."
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Configuration: lookaheadFrames array size:    %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen ghosts are more than capacity"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen keypoint count: %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): DesGen keypoints are not available, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detected ROI count exceeds the limit of %!d(MISSING). Some ROIs are not packed to repair"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection + tracking: GG# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection skipped because of too many light sources"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Detection: GG# %!u(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Empty input"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Empty lookahead data"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost cnt (before merge) exceeds hard gating threshold. All ghosts are discarded"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost cnt (before merge) exceeds soft gating threshold. Only keeping top %!d(MISSING) ghosts"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Ghost count exceeds Max prev %!l(MISSING)u and cur %!l(MISSING)u "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Key -(%!s(MISSING)) is not valid init option"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): LS Gating Disabled. Keeping detecton ON."
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Lux Level Gating Disabled. Keeping detecton ON."
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Metal tool box shaders compilation failed"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No input locations to find tiny keypoints"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No input texture or prev LS boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): No prev LS boxes to updates DoG and luma features"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Null detection results"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Prev Ghost Id count exceeds Max %!l(MISSING)u "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): ROI count: %!d(MISSING) / GG count: %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): ROI to repair: (%!f(MISSING), %!f(MISSING)), (%!f(MISSING), %!f(MISSING))"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Tiny ghosts are more than capacity"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total Clipped Pixels Count (scale adjusted): %!f(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total Key points count clipped from %!l(MISSING)u to %!d(MISSING) "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total ROI count clipped from %!d(MISSING) to %!d(MISSING) in updateDoGAndLumaFeature for prevLS"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total ROI count clipped from %!d(MISSING) to %!d(MISSING) in updateDoGAndLumaFeatures"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total allocate metal buffer size %!d(MISSING) bytes"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total area to repair (before potential rescaling from perf control): %!f(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total key point count exceeds hard gating threshold. Discard all key points"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total keypoint count clipped from %!d(MISSING) to %!d(MISSING) in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Total light source count clipped from %!d(MISSING) to %!d(MISSING) in findGhostCandidatesFromDesGenAndTinyKeypointsFromInputTexture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Tuning parameters not given from plist, will use macros"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because clipped pixel count %!d(MISSING) < %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because of exposure %!d(MISSING) > %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection OFF because of light source count %!d(MISSING) > %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because clipped pixel count %!d(MISSING) > %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because of exposure %!d(MISSING) < %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Turning detection back ON because of light source count %!d(MISSING) < %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to allocate input texture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to cache pixel buffer texture"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to create feature descriptor, feature length is zero"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to create feature descriptor, feature sums are zero"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to get metal texture address"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize cpu mitigator"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize gpu mitigator"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize gpu mitigator "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize homography instance"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize metal tool box"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize mitigation CPU"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): Unable to initialize video mitigation"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is captured in %!@(MISSING) light enviroment: "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is forced to bright light mode"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] The video is forced to low light mode"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): [GGM MSG] Version %!d(MISSING).%!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): _allocateMetalBuffers failed"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): _detectionInit failed"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): detection result in look-ahead frame %!d(MISSING) is nil, detection might be reset !"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): getTopGhostsInList failed to trim Ghost count from %!d(MISSING) to %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): homography type: %!d(MISSING) is not supported, force to identity matrix."
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): light source bounding box count: %!l(MISSING)d exeed the limit: %!d(MISSING)"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): light source mask is not available, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): lux Level gated, detection is skipped"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): meta buffer is null"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): meta buffer not available"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): metal buffer is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): next frame texture is nil, skipping prev ls box generation"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): nil detection metadata"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): nil metadata from detection"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): no previous LS ROIs for feature extraction"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): packed format is not supported in this function"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): pixelBuffer is NULL"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): stashedMeta buffer is null"
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): total cluster is %!d(MISSING), bigger than limit, not all GGs are mitigated "
+ "<<<< VEVideoDeghostingV2 >>>> %!s(MISSING): totalClippedPixelsCount is not enough, detection is skipped"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
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
+ "f16"
+ "f32"
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
- "%!s(MISSING)_C_%!d(MISSING)x%!d(MISSING).f32"
- "%!s(MISSING)_L_%!d(MISSING)x%!d(MISSING).f32"
- "%!s(MISSING)_R_%!d(MISSING)x%!d(MISSING).f32"

```
