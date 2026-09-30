## ColourConstancyV1

> `/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x18378
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0x29a0
-  __TEXT.__objc_methlist: 0x110c
-  __TEXT.__const: 0x100
-  __TEXT.__objc_methname: 0x7165
-  __TEXT.__objc_classname: 0x437
-  __TEXT.__objc_methtype: 0x13ed
-  __TEXT.__cstring: 0x5091
-  __TEXT.__unwind_info: 0x2c0
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__cfstring: 0x1140
+580.2.0.0.0
+  __TEXT.__text: 0x1cb78
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x2a60
+  __TEXT.__objc_methlist: 0x116c
+  __TEXT.__const: 0x150
+  __TEXT.__objc_methname: 0x769d
+  __TEXT.__objc_classname: 0x436
+  __TEXT.__objc_methtype: 0x1425
+  __TEXT.__cstring: 0x61bd
+  __TEXT.__oslogstring: 0x1dab
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__cfstring: 0x11c0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3ab8
-  __DATA.__objc_selrefs: 0xba8
-  __DATA.__objc_ivar: 0x37c
+  __DATA.__objc_const: 0x3ba8
+  __DATA.__objc_selrefs: 0xbf0
+  __DATA.__objc_ivar: 0x394
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x1e0
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 349
-  Symbols:   161
-  CStrings:  1356
+  Functions: 358
+  Symbols:   166
+  CStrings:  1502
 
Symbols:
+ ___stack_chk_fail
+ __os_log_send_and_compose_impl
+ ___stack_chk_guard
+ _FigSignalErrorAt3
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
- _FigSignalErrorAt
- _fig_log_get_emitter
CStrings:
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Metal allocator has already been set up"
+ "_styleTransferAccuracyZeroThreshold"
+ "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
+ "-[CMIColourConstancyProcessorV1 externalMemoryDescriptorForConfiguration:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): WARNING: Strobe Calibration Data not found. Defaulting to hard coded calibration gains. Please ensure your device is up to date."
+ "-[CMIColourConstancyClippingRecoveryV1 _encodeColourAccuracyClippedRegionRecovery:inputAmbientLumaTexture:inputAmbientChromaTexture:inoutFlashLumaTexture:inoutFlashChromaTexture:ambientToFlashRegistrationHomography:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Minimum Valid Buffer Crop Rectangle For GDC (Pixel Coordinates). [Sizes: Width:%!d(MISSING) Height:%!d(MISSING)] [Offsets: X:%!d(MISSING) Y:%!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash LSC gains compensation. [FlashLSCMaxGain: %!f(MISSING), BaseLSCMaxGain: %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Thumbnail flash frame. [Luma: Width: %!d(MISSING), Height: %!d(MISSING)] [Chroma: Width: %!d(MISSING), Height: %!d(MISSING)] [ThumbnailOutput: Width: %!d(MISSING), Height: %!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Finished processing."
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Gaussian filtering of flash weighted thumbnail. [GaussianSigma: %!f(MISSING), SigmaToFilterScale: %!f(MISSING)]"
+ "-[CMIColourConstancyClippingRecoveryConfigurationV1 init]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeFusionMapExtraction failed"
+ "setStyleTransferAccuracyGammaCorrection:"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Create flash weighted thumbnail. [Input: Width: %!d(MISSING), Height: %!d(MISSING)] [OutputThumbnail: Width: %!d(MISSING), Height: %!d(MISSING)]"
+ "ColourConstancy::reconstructStyleTargetFromSourceWithQualityModeV1"
+ "self is NULL"
+ "_reconstructStyleTargetFromSourceWithQualityModePipelineState"
+ "\r"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Could not initialize 'CMIColourConstancyMicroHazeDetectionConfigurationV1'"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "-[CMIColourConstancyRegistrationV1 initWithMetalContext:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Create target transfer learning thumbnail. [InputTarget: Width: %!d(MISSING), Height: %!d(MISSING)] [OutputThumbnail: Width: %!d(MISSING), Height: %!d(MISSING), Sharpness:%!f(MISSING), SigmaToFilterScale:%!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash Sensor Crop Rectangle. [Sizes: Width:%!d(MISSING) Height:%!d(MISSING)] [Offsets: X:%!d(MISSING) Y:%!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash sensor space conversion. [WhitePoint: R: %!f(MISSING), G: %!f(MISSING), B: %!f(MISSING)] [IntegrationTimeScale: %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Thumbnail ambient frame with registration warping. [Luma: Width: %!d(MISSING), Height: %!d(MISSING)] [Chroma: Width: %!d(MISSING), Height: %!d(MISSING)] [ThumbnailOutput: Width: %!d(MISSING), Height: %!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Forward fftTransform encoding failed"
+ "_styleTransferAccuracyGammaCorrection"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Constructing the balanced intensity density histogram. [balanceDenseToSparseExponentFactor: %!f(MISSING), minimumProbabilityDensity: %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Received QSub capture. Assuming 2x crop."
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Center Weighted Mean Colour Accuracy Confidence Level: %!f(MISSING)"
+ "-[CMIColourConstancyStyleTransferV1 finishProcessing]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeImagePyramidGeneration failed"
+ "calculateColourAccuracyConfidence:strobeComponentRGBATexture:strobeBalancedThumbnailRGBTexture:strobeReconstructedBalancedThumbnailRGBTexture:outputColourAccuracyConfidenceTexture:"
+ "+[CMIColourConstancyCommon getStrobeColourCorrectionMatrix:outputMatrix:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Register ambient bracket to flash bracket"
+ "allocatorBackend is  nil"
+ "Failed to create Metal allocator"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): White balance the strobe component. [StrobeWhitePoint: R: %!f(MISSING), G: %!f(MISSING), B: %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Using external metal allocator (size:%!l(MISSING)u MB)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeImageReconstruction failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Decompose the strobe component image from the flash and ambient sensor space images"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeMixMapGeneration failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Initializing ColourConstancyProcessor allocator with size: %!l(MISSING)u, descriptor: %!@(MISSING)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeGradientExtraction:[ambient] failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): addFrame called with unsupported frameType:%!d(MISSING)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Style transfer (MainAlgo). [ClippingCorrection: Enabled:%!@(MISSING), Gain:%!f(MISSING), Exponent:%!f(MISSING)]"
+ "styleTransferAccuracyZeroThreshold"
+ "-[CMIColourConstancyCoreV1 applyWithAmbientLumaTexture:ambientChromaTexture:flashLumaTexture:flashChromaTexture:ambientYUVOffsets:flashYUVOffsets:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:ambientWhitePoint:flashWhitePoint:strobeWhitePoint:ambientIntegrationTime:flashIntegrationTime:cropRect:LSCCropRect:fullSizeDimensions:strobeCCM:outputColourAccuracyConfidenceTexture:outputLumaTexture:outputChromaTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): LSC Crop Rectangle. [Sizes: Width:%!d(MISSING) Height:%!d(MISSING)] [Offsets: X:%!d(MISSING) Y:%!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeMicroHazeFusionMapExtraction failed"
+ "-[CMIColourConstancyConfidenceV1 calculateStrobeIlluminationConfidence:strobeComponentRGBTexture:outputStrobeIlluminationConfidenceRTexture:]"
+ "-[CMIColourConstancyRegistrationV1 registerImage:referenceLumaTexture:]"
+ "Failed to create ColourConstancy::reconstructStyleTargetFromSourceWithQualityModeV1 MTLComputePipelineState."
+ "allocatorDesc is NULL"
+ "_strobeReconstructedBalancedThumbnailRGBTexture"
+ "-[CMIColourConstancyClippingRecoveryV1 _encodeGradientImageFusion:channel:]"
+ "_encodeStyleTargetFromSourceWithSpeedModeReconstruct:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:outputReconstructedTargetThumbnailRGBTexture:"
+ "err"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Could not initialize 'CMIColourConstancyClippingRecoveryConfigurationV1'"
+ "_reconstructStyleTargetFromSourceWithSpeedModePipelineState"
+ "-[CMIColourConstancyProcessorV1 addFrame:metadata:frameType:frameParams:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash integration time: %!f(MISSING)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeGradientExtraction:[flash] failed"
+ "Tf,N,V_styleTransferAccuracyGammaCorrection"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeGradientImageFusion failed"
+ "-[CMIColourConstancyWhiteBalanceStrobeV1 applyWhiteBalanceAndFlashFusion:strobeSensorRGBTexture:flashBalancedRGBTexture:strobeIlluminationConfidenceRTexture:strobeWhitePoint:outputStrobeBalancedRGBTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash brightness and white balance matching with fusion. [FlashToStrobeIntensityFusionMixFactor: %!f(MISSING)]"
+ "No Metal allocator"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Prepared memory size on the external metal allocator is too small (required:%!l(MISSING)u bytes, got:%!l(MISSING)u bytes)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Style transfer tonal and white balancing changes to full resolution."
+ "i56@0:8@16@24@32@40@48"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash LSC max gain: %!f(MISSING)"
+ "<<<< CMIColourConstancy >>>>"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Constructing the kernel weighted intensity density histogram. [kernelSupportGaussianSigma: %!f(MISSING), kernelSupportSigmaToFilterScale: %!f(MISSING)]"
+ "setStyleTransferAccuracyZeroThreshold:"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Setting up ColourConstancy processor with provided metal command queue."
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Strobe beam profile correction. [CorrectionScale: Min: %!f(MISSING), Max: %!f(MISSING)] [Component: Edge0: %!f(MISSING), Edge1: %!f(MISSING)]"
+ "_encodeStyleTargetFromSourceWithQualityModeReconstruct:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:styleEngineCoefficientsTexture:styleEngineLinearSystemStatusFlagBuffer:styleEngineGammaCorrection:outputReconstructedTargetThumbnailRGBTexture:"
+ "Tf,N,V_styleTransferAccuracyOneThreshold"
+ "styleTransferAccuracyOneThreshold"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Registration of Luma frames. Homography: [%!f(MISSING), %!f(MISSING), %!f(MISSING); %!f(MISSING), %!f(MISSING), %!f(MISSING); %!f(MISSING), %!f(MISSING), %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Strobe white balance gains: [R:%!f(MISSING), G:%!f(MISSING), B:%!f(MISSING)]"
+ "-[CMIColourConstancyToneCompressionV1 calculateToneCompressionCurve:strobeComponentRGBTexture:strobeCCM:]"
+ "-[CMIColourConstancyProcessorV1 calculateColourConstancyWithCropRect:LSCCropRect:fullSizeCropRect:]"
+ "YES"
+ "-[CMIColourConstancyMicroHazeDetectionV1 _encodeMicroHazeFusionMapExtraction:inputAmbientTexture:inputFlashTexture:outputFusionMapTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): WARNING: Strobe Modulated CCM not found. Defaulting to Flash Modulated CCM. Please ensure your device is up to date."
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Ambient sensor space conversion. [WhitePoint: R: %!f(MISSING), G: %!f(MISSING), B: %!f(MISSING)] [IntegrationTimeScale, %!f(MISSING)]"
+ "-[CMIColourConstancyStrobeCorrectionV1 applyStrobeCorrection:strobeComponentRGBTexture:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:lscCropRect:fullSizeDimensions:outputStrobeCorrectedRGBTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Reconstruct target thumbnail using style transfer (SpeedMode)."
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Constructing the colour intensity histogram. [numHistogramBins: %!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Output Crop Rectangle. [Sizes: Width:%!d(MISSING) Height:%!d(MISSING)] [Offsets: X:%!d(MISSING) Y:%!d(MISSING)]"
+ "CMIColourConstancyStatusMetalAllocationFailed"
+ "_metalContext.allocator is NULL"
+ "-[CMIColourConstancyConfidenceV1 calculateColourAccuracyConfidence:strobeComponentRGBATexture:strobeBalancedThumbnailRGBTexture:strobeReconstructedBalancedThumbnailRGBTexture:outputColourAccuracyConfidenceTexture:]"
+ "-1"
+ "_encodeColourAccuracyConfidenceCalculate:strobeComponentRGBATexture:strobeBalancedThumbnailRGBTexture:strobeReconstructedBalancedThumbnailRGBTexture:strobeIlluminationZeroThreshold:strobeIlluminationOneThreshold:styleTransferAccuracyZeroThreshold:styleTransferAccuracyOneThreshold:styleTransferAccuracyGammaCorrection:outputColourAccuracyConfidenceTexture:"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Create strobe weighted thumbnail. [Input: Width: %!d(MISSING), Height: %!d(MISSING)] [OutputThumbnail: Width: %!d(MISSING), Height: %!d(MISSING)]"
+ "commandBuffer is NULL"
+ "styleTransferAccuracyGammaCorrection"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Inverse fftTransform encoding failed"
+ "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedLSCGainsTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Final Crop Rectangle (Normalized Coordinates). [Sizes: Width:%!f(MISSING) Height:%!f(MISSING)] [Offsets: X:%!f(MISSING) Y:%!f(MISSING)]"
+ "Tf,N,V_styleTransferAccuracyZeroThreshold"
+ "_regWarpGPU is NULL"
+ "-[CMIColourConstancyProcessorV1 process]"
+ "-[CMIColourConstancyStyleTransferV1 applyStyleTransferWithBufferClearing:inputChromaTexture:appliedLSCGainsTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Ambient LSC max gain: %!f(MISSING)"
+ "-[CMIColourConstancyProcessorV1 setup]"
+ "-[CMIColourConstancyClippingRecoveryV1 _encodeGradientExtraction:frame:channel:]"
+ "Failed to create ColourConstancy::reconstructStyleTargetFromSourceWithSpeedModeV1 MTLComputePipelineState."
+ "-[CMIColourConstancyMicroHazeDetectionV1 microHazeFusionMapExtraction:inputAmbientTexture:inputFlashTexture:outputFusionMapTexture:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Input texture sizes. Ambient: [Width: %!d(MISSING), Height: %!d(MISSING)] Flash: [Width: %!d(MISSING), Height: %!d(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeShadowEdgeMapExtraction failed"
+ "+[CMIColourConstancyCommon getStrobeWhiteBalanceGains:metadata:outputVector:]"
+ "Failed to initialize Metal context"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Create source transfer learning thumbnail. [InputSource: Width: %!d(MISSING), Height: %!d(MISSING)] [OutputThumbnail: Width: %!d(MISSING), Height: %!d(MISSING), Sharpness:%!f(MISSING), SigmaToFilterScale:%!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeClassifierMasksExtraction failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Ambient integration time: %!f(MISSING)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Constructing the tone compression curve."
+ "_styleTransferAccuracyOneThreshold"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeIntensityImageGeneration failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): externalMemoryDescriptor is nil"
+ "NO"
+ "-[CMIColourConstancyMicroHazeDetectionConfigurationV1 initWithFusionMapWidth:fusionMapHeight:]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Estimate Colour Accuracy Confidence. [StrobeIllumination: Edge0: %!f(MISSING), Edge1: %!f(MISSING)]"
+ "i68@0:8@16@24@32@40@48f56@60"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Ambient white balance gains: [R:%!f(MISSING), G:%!f(MISSING), B:%!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Flash white balance gains: [R:%!f(MISSING), G:%!f(MISSING), B:%!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Estimate the Strobe Illumination Confidence. [StrobeIllumination: Edge0: %!f(MISSING), Edge1: %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeIntensityGainTransformsGeneration failed"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Gaussian filtering of strobe weighted thumbnail. [GaussianSigma: %!f(MISSING), SigmaToFilterScale: %!f(MISSING)]"
+ "-[CMIColourConstancyProcessorV1 prepareToProcess:]"
+ "-[CMIColourConstancyProcessorV1 requiredMetalAllocatorMemorySize]"
+ "Encoding of speed mode style target reconstruction failed."
+ "FigMetalAllocator setupWithDescriptor failed"
+ "setStyleTransferAccuracyOneThreshold:"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Style transfer (SpeedMode). [ClippingCorrection: Enabled:%!@(MISSING), Gain:%!f(MISSING), Exponent:%!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): CMIStyleEngineProcessor linear system could not be solved, fallback to SpeedMode transfer"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): prepareToProcess for %!d(MISSING)"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Calculated full silicon size dimensions: [Width:%!d(MISSING) Height:%!d(MISSING)]"
+ "ColourConstancy::reconstructStyleTargetFromSourceWithSpeedModeV1"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Strobe CCM: [%!f(MISSING), %!f(MISSING), %!f(MISSING); %!f(MISSING), %!f(MISSING), %!f(MISSING); %!f(MISSING), %!f(MISSING), %!f(MISSING)]"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): encodeIntensityGainMapGeneration failed"
+ "i216@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}80{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}96116f124128{?=[3]}144@192@200@208"
+ "-[CMIColourConstancyRegistrationV1 prepareToProcess:]"
+ "metalContext is NULL"
- "_encodeColourAccuracyConfidenceCalculate:strobeComponentRGBATexture:strobeIlluminationZeroThreshold:strobeIlluminationOneThreshold:outputColourAccuracyConfidenceTexture:"
- "calculateColourAccuracyConfidence:strobeComponentRGBATexture:outputColourAccuracyConfidenceTexture:"
- "\x0f\x03"
- "i208@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}80{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}96116f124128{?=[3]}144@192@200"
- "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedLSCGainsTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:strobeCCM:outputLumaTexture:outputChromaTexture:"

```
