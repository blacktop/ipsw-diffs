## SemanticStyleV1

> `/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1`

```diff

-664.62.12.0.0
-  __TEXT.__text: 0xeb74
-  __TEXT.__auth_stubs: 0x4f0
+665.80.6.0.0
+  __TEXT.__text: 0xf070
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__objc_methlist: 0xadc
   __TEXT.__const: 0xc80
   __TEXT.__objc_methname: 0x2a86
-  __TEXT.__cstring: 0x1050
-  __TEXT.__oslogstring: 0xd4
+  __TEXT.__cstring: 0x1ad1
+  __TEXT.__oslogstring: 0x215
   __TEXT.__objc_classname: 0xb1
   __TEXT.__objc_methtype: 0x95e
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x280
+  __TEXT.__unwind_info: 0x2c8
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__cfstring: 0x520
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA.__bss: 0x40
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 544B5140-A3BD-3C11-8699-F4030AE6E425
-  Functions: 302
-  Symbols:   116
-  CStrings:  735
+  UUID: E569EAF8-39EF-37F1-8E87-6920BCD3E5D5
+  Functions: 308
+  Symbols:   119
+  CStrings:  813
 
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
+ "<<<< LKT IIR Filter >>>> %s: metalContext is nil"
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
+ "maskToFilter is nil"
+ "opticalFlowDisplacementPixelBuffer is NULL"
+ "semstyle_filtering_trace"
- "%s signalled err=%d at <>:%d"

```
