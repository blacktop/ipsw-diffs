## SemanticStyleV1

> `/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0xdf70
-  __TEXT.__auth_stubs: 0x4c0
+650.0.0.122.4
+  __TEXT.__text: 0xf084
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__objc_methlist: 0xaec
-  __TEXT.__const: 0xc60
+  __TEXT.__const: 0xc80
   __TEXT.__objc_methname: 0x2aa4
-  __TEXT.__cstring: 0x109a
+  __TEXT.__cstring: 0x1ad1
+  __TEXT.__oslogstring: 0x215
   __TEXT.__objc_classname: 0xb1
   __TEXT.__objc_methtype: 0x95e
-  __TEXT.__unwind_info: 0x2a8
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x58
-  __DATA_CONST.__cfstring: 0x600
+  __TEXT.__unwind_info: 0x2d8
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x40
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 558FB4EF-097E-3DBB-99FD-E0365C26A317
-  Functions: 291
-  Symbols:   112
-  CStrings:  738
+  UUID: ADAA3133-44DB-3303-89B7-64603ED8939A
+  Functions: 309
+  Symbols:   118
+  CStrings:  815
 
Symbols:
+ _FigSignalErrorAt3
+ __NSConcreteGlobalBlock
+ __os_log_impl
+ __os_log_send_and_compose_impl
+ _dispatch_once
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_release_x1
+ _os_log_create
+ _os_log_type_enabled
- _FigSignalErrorAt
- _NSLog
- ___stack_chk_fail
- ___stack_chk_guard
- _fig_log_get_emitter
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[FigLKTIIRFilter allocateResourcesForMaskSize:]"
+ "-[FigLKTIIRFilter computeLKTIIRFilter:inputSegmentationMask:filteredSegmentationMask:]"
+ "-[FigLKTIIRFilter computeOpticalFlow:inputImage:]"
+ "-[FigLKTIIRFilter initWithMetalContext:]"
+ "-[FigSemanticStyleFilteringV1 _compileShaders]"
+ "-[FigSemanticStyleFilteringV1 _textureFromPixelBuffer:usage:]"
+ "-[FigSemanticStyleFilteringV1 initWithCommandQueue:]"
+ "-[FigSemanticStyleFilteringV1 prepareToProcess:]"
+ "-[FigSemanticStyleFilteringV1 prewarm]"
+ "-[FigSemanticStyleFilteringV1 process]"
+ "<<<< LKT IIR Filter >>>>"
+ "<<<< LKT IIR Filter >>>> %s: metalContext is nil"
+ "<<<< SemanticStyle Filtering >>>>"
+ "<<<< SemanticStyle Filtering >>>> %s: Could not init _metalContext"
+ "<<<< SemanticStyle Filtering >>>> %s: Init completed with no error"
+ "<<<< SemanticStyle Filtering >>>> %s: Mask interpolation is %@"
+ "<<<< SemanticStyle Filtering >>>> %s: Unsupported pixel format for caching"
+ "Could not allocate MPSImageGaussianBlur"
+ "Could not allocate MPSImageMultiply"
+ "Could not allocate _blurredMask"
+ "Could not allocate _featheredMask"
+ "Could not allocate _nonFeatheredMask"
+ "Could not allocate _resizedInputImageToMaskSize"
+ "Could not allocate _smoothedMask"
+ "Could not allocate command buffer"
+ "Could not allocate resources for FigLKTIIRFilter"
+ "Could not get displacementFWD from pixelbuffer"
+ "Could not get inputImageTexture from pixelbuffer"
+ "Could not get inputMaskTexture from pixelbuffer"
+ "Could not get outputMaskTexture from pixelbuffer"
+ "Could not init FigLKTIIRFilter"
+ "Input image pixel buffer is NULL"
+ "Input mask is not kCVPixelFormatType_OneComponent16Half"
+ "No command buffer provided"
+ "Optical flow is not available."
+ "Optical has already been computed. This should not happen"
+ "Output mask pixel buffer is NULL"
+ "SemanticStyleFilteringStatusFeatheringFailed"
+ "SemanticStyleFilteringStatusInputError"
+ "SemanticStyleFilteringStatusLKTFilterAllocationFailed"
+ "SemanticStyleFilteringStatusLKTFilterFailed"
+ "SemanticStyleFilteringStatusLKTFilterInitFailed"
+ "SemanticStyleFilteringStatusMPSAllocationFailed"
+ "SemanticStyleFilteringStatusMetalAllocationFailed"
+ "SemanticStyleFilteringStatusMetalTextureAllocationFailed"
+ "SemanticStyleFilteringStatusOtherError"
+ "Shaders compilation failed"
+ "Unable to create a metal texture cache"
+ "_applyFeathering failed"
+ "_copyAndCenterMask failed"
+ "_imageArray textures allocation failed"
+ "_inputSegmentationMaskF16 is nil."
+ "_keyFrameAndMask is nil."
+ "_maskArray textures allocation failed"
+ "_pipelineStates[COPY_AND_CENTER_MASK] is NULL"
+ "_pipelineStates[SMOOTH_STEP] is NULL"
+ "_previousMaskWarped is nil."
+ "_tempMaskTexture is nil."
+ "_tmpCoord is nil."
+ "_tmpDisplacementMap is nil."
+ "_warpedKeyFrameToCurrentFrameCoord is nil."
+ "_warpedKeyFrameToCurrentFrameDisplacementMap is nil."
+ "_warpedKeyFrameToCurrentFrameImage is nil."
+ "_warpedKeyFrameToCurrentFrameMask is nil."
+ "cacheInputMask failed"
+ "computeLKTIIRFilter failed"
+ "disabled"
+ "enabled"
+ "filteredSegmentationMask is nil."
+ "inputImage is nil."
+ "inputSegmentationMask is nil."
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "legacyLog"
+ "maskToFilter is nil"
+ "opticalFlowDisplacementPixelBuffer is NULL"
+ "semstyle_filtering_trace"
+ "v8@?0"

```
