## SemanticStyleV1

> `/System/Library/VideoProcessors/SemanticStyleV1.bundle/SemanticStyleV1`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0xd478
-  __TEXT.__auth_stubs: 0x4d0
+580.2.0.0.0
+  __TEXT.__text: 0xde5c
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0x1140
   __TEXT.__objc_methlist: 0x8e8
-  __TEXT.__const: 0xc70
+  __TEXT.__const: 0xc80
   __TEXT.__objc_methname: 0x2aa4
-  __TEXT.__cstring: 0x1087
+  __TEXT.__cstring: 0x1b58
   __TEXT.__objc_classname: 0xb1
   __TEXT.__objc_methtype: 0x95e
-  __TEXT.__unwind_info: 0x280
-  __DATA_CONST.__auth_got: 0x270
+  __TEXT.__oslogstring: 0x141
+  __TEXT.__unwind_info: 0x288
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x58
-  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x120
+  __DATA.__common: 0x20
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 206
-  Symbols:   113
-  CStrings:  692
+  Symbols:   117
+  CStrings:  770
 
Symbols:
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_note_initialize_category_with_default_work_cf
+ _FigSignalErrorAt3
- _FigSignalErrorAt
- _fig_log_get_emitter
CStrings:
+ "-[FigLKTIIRFilter initWithMetalContext:]"
+ "Could not allocate _smoothedMask"
+ "Optical has already been computed. This should not happen"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "cacheInputMask failed"
+ "_imageArray textures allocation failed"
+ "kCMBaseObjectError_ParamErr"
+ "SemanticStyleFilteringStatusLKTFilterFailed"
+ "-[FigSemanticStyleFilteringV1 initWithCommandQueue:]"
+ "-[FigSemanticStyleFilteringV1 _textureFromPixelBuffer:usage:]"
+ "_warpedKeyFrameToCurrentFrameMask is nil."
+ "enabled"
+ "_warpedKeyFrameToCurrentFrameDisplacementMap is nil."
+ "Could not allocate _featheredMask"
+ "Could not allocate _resizedInputImageToMaskSize"
+ "_pipelineStates[SMOOTH_STEP] is NULL"
+ "<<<< SemanticStyle Filtering >>>> %!s(MISSING): Unsupported pixel format for caching"
+ "Could not allocate command buffer"
+ "<<<< LKT IIR Filter >>>>"
+ "Output mask pixel buffer is NULL"
+ "Unable to create a metal texture cache"
+ "_tempMaskTexture is nil."
+ "Could not get inputImageTexture from pixelbuffer"
+ "No command buffer provided"
+ "_maskArray textures allocation failed"
+ "Could not allocate resources for FigLKTIIRFilter"
+ "semstyle_filtering_trace"
+ "Could not allocate _blurredMask"
+ "computeLKTIIRFilter failed"
+ "SemanticStyleFilteringStatusLKTFilterAllocationFailed"
+ "-1"
+ "-[FigLKTIIRFilter allocateResourcesForMaskSize:]"
+ "inputSegmentationMask is nil."
+ "_pipelineStates[COPY_AND_CENTER_MASK] is NULL"
+ "Input mask is not kCVPixelFormatType_OneComponent16Half"
+ "-[FigSemanticStyleFilteringV1 prepareToProcess:]"
+ "_tmpDisplacementMap is nil."
+ "_tmpCoord is nil."
+ "SemanticStyleFilteringStatusMetalAllocationFailed"
+ "Could not init FigLKTIIRFilter"
+ "inputImage is nil."
+ "<<<< LKT IIR Filter >>>> %!s(MISSING): metalContext is nil"
+ "Could not allocate MPSImageGaussianBlur"
+ "Input image pixel buffer is NULL"
+ "SemanticStyleFilteringStatusLKTFilterInitFailed"
+ "SemanticStyleFilteringStatusMPSAllocationFailed"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "_warpedKeyFrameToCurrentFrameImage is nil."
+ "filteredSegmentationMask is nil."
+ "-[FigSemanticStyleFilteringV1 prewarm]"
+ "SemanticStyleFilteringStatusInputError"
+ "SemanticStyleFilteringStatusOtherError"
+ "<<<< SemanticStyle Filtering >>>> %!s(MISSING): Could not init _metalContext"
+ "Could not allocate MPSImageMultiply"
+ "Shaders compilation failed"
+ "_warpedKeyFrameToCurrentFrameCoord is nil."
+ "SemanticStyleFilteringStatusMetalTextureAllocationFailed"
+ "_inputSegmentationMaskF16 is nil."
+ "Could not get inputMaskTexture from pixelbuffer"
+ "disabled"
+ "Could not get displacementFWD from pixelbuffer"
+ "-[FigSemanticStyleFilteringV1 _compileShaders]"
+ "Could not get outputMaskTexture from pixelbuffer"
+ "-[FigLKTIIRFilter computeLKTIIRFilter:inputSegmentationMask:filteredSegmentationMask:]"
+ "_applyFeathering failed"
+ "_keyFrameAndMask is nil."
+ "-[FigLKTIIRFilter computeOpticalFlow:inputImage:]"
+ "<<<< SemanticStyle Filtering >>>> %!s(MISSING): Mask interpolation is %!@(MISSING)"
+ "-[FigSemanticStyleFilteringV1 process]"
+ "maskToFilter is nil"
+ "<<<< SemanticStyle Filtering >>>> %!s(MISSING): Init completed with no error"
+ "<<<< SemanticStyle Filtering >>>>"
+ "SemanticStyleFilteringStatusFeatheringFailed"
+ "Could not allocate _nonFeatheredMask"
+ "Optical flow is not available."
+ "opticalFlowDisplacementPixelBuffer is NULL"
+ "_copyAndCenterMask failed"
+ "_previousMaskWarped is nil."

```
