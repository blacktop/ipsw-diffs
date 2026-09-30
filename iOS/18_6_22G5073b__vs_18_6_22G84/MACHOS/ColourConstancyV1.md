## ColourConstancyV1

> `/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1`

```diff

-587.140.9.0.0
-  __TEXT.__text: 0x1f5a4
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x2aa0
+587.140.11.0.1
+  __TEXT.__text: 0x1c034
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x2a80
   __TEXT.__objc_methlist: 0x14cc
-  __TEXT.__const: 0x150
+  __TEXT.__const: 0x100
   __TEXT.__objc_methname: 0x787c
   __TEXT.__objc_classname: 0x43a
   __TEXT.__objc_methtype: 0x1210
-  __TEXT.__cstring: 0x6528
-  __TEXT.__oslogstring: 0x1e0d
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__cfstring: 0x11e0
+  __TEXT.__cstring: 0x5668
+  __TEXT.__unwind_info: 0x360
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 731B1C42-1257-33FD-9E05-8874283C28A3
-  Functions: 763
-  Symbols:   166
-  CStrings:  1661
+  UUID: 85983611-BD2A-31B8-8054-23B95A06C78E
+  Functions: 768
+  Symbols:   161
+  CStrings:  1538
 
Symbols:
+ _FigSignalErrorAt
+ _fig_log_get_emitter
- _FigSignalErrorAt3
- ___stack_chk_fail
- ___stack_chk_guard
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "+[CMIColourConstancyCommon getStrobeColourCorrectionMatrix:outputMatrix:]"
- "+[CMIColourConstancyCommon getStrobeWhiteBalanceGains:metadata:outputVector:]"
- "-1"
- "-[CMIColourConstancyClippingRecoveryConfigurationV1 init]"
- "-[CMIColourConstancyClippingRecoveryV1 _encodeColourAccuracyClippedRegionRecovery:inputAmbientLumaTexture:inputAmbientChromaTexture:inoutFlashLumaTexture:inoutFlashChromaTexture:ambientToFlashRegistrationHomography:]"
- "-[CMIColourConstancyClippingRecoveryV1 _encodeGradientExtraction:frame:channel:]"
- "-[CMIColourConstancyClippingRecoveryV1 _encodeGradientImageFusion:channel:]"
- "-[CMIColourConstancyConfidenceV1 calculateColourAccuracyConfidence:strobeComponentRGBATexture:strobeBalancedThumbnailRGBTexture:strobeReconstructedBalancedThumbnailRGBTexture:outputColourAccuracyConfidenceTexture:]"
- "-[CMIColourConstancyConfidenceV1 calculateStrobeIlluminationConfidence:strobeComponentRGBTexture:outputStrobeIlluminationConfidenceRTexture:]"
- "-[CMIColourConstancyCoreV1 applyWithAmbientLumaTexture:ambientChromaTexture:flashLumaTexture:flashChromaTexture:ambientYUVOffsets:flashYUVOffsets:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:ambientWhitePoint:flashWhitePoint:strobeWhitePoint:ambientIntegrationTime:flashIntegrationTime:cropRect:LSCCropRect:fullSizeDimensions:strobeCCM:outputColourAccuracyConfidenceTexture:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:]"
- "-[CMIColourConstancyMicroHazeDetectionConfigurationV1 initWithFusionMapWidth:fusionMapHeight:]"
- "-[CMIColourConstancyMicroHazeDetectionV1 _encodeMicroHazeFusionMapExtraction:inputAmbientTexture:inputFlashTexture:outputFusionMapTexture:]"
- "-[CMIColourConstancyMicroHazeDetectionV1 microHazeFusionMapExtraction:inputAmbientTexture:inputFlashTexture:outputFusionMapTexture:]"
- "-[CMIColourConstancyProcessorV1 addFrame:metadata:frameType:frameParams:]"
- "-[CMIColourConstancyProcessorV1 calculateColourConstancyWithCropRect:LSCCropRect:fullSizeCropRect:]"
- "-[CMIColourConstancyProcessorV1 externalMemoryDescriptorForConfiguration:]"
- "-[CMIColourConstancyProcessorV1 prepareToProcess:]"
- "-[CMIColourConstancyProcessorV1 process]"
- "-[CMIColourConstancyProcessorV1 requiredMetalAllocatorMemorySize]"
- "-[CMIColourConstancyProcessorV1 setup]"
- "-[CMIColourConstancyRegistrationV1 initWithMetalContext:]"
- "-[CMIColourConstancyRegistrationV1 prepareToProcess:]"
- "-[CMIColourConstancyRegistrationV1 registerImage:referenceLumaTexture:]"
- "-[CMIColourConstancyStrobeCorrectionV1 applyStrobeCorrection:strobeComponentRGBTexture:strobeBeamProfileGainRTexture:outputStrobeCorrectedRGBTexture:]"
- "-[CMIColourConstancyStyleTransferV1 applyStyleTransferWithBufferClearing:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:]"
- "-[CMIColourConstancyStyleTransferV1 finishProcessing]"
- "-[CMIColourConstancyToneCompressionV1 calculateToneCompressionCurve:strobeComponentRGBTexture:strobeCCM:]"
- "-[CMIColourConstancyWhiteBalanceStrobeV1 applyWhiteBalanceAndFlashFusion:strobeSensorRGBTexture:flashBalancedRGBTexture:strobeIlluminationConfidenceRTexture:strobeWhitePoint:outputStrobeBalancedRGBTexture:]"
- "<<<< CMIColourConstancy >>>>"
- "<<<< CMIColourConstancy >>>> %s: Ambient LSC max gain: %f"
- "<<<< CMIColourConstancy >>>> %s: Ambient integration time: %f"
- "<<<< CMIColourConstancy >>>> %s: Ambient sensor space conversion. [WhitePoint: R: %.3f, G: %.3f, B: %.3f] [IntegrationTimeScale, %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Ambient white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: CMIStyleEngineProcessor linear system could not be solved, fallback to SpeedMode transfer"
- "<<<< CMIColourConstancy >>>> %s: Calculated full silicon size dimensions: [Width:%d Height:%d]"
- "<<<< CMIColourConstancy >>>> %s: Center Weighted Mean Colour Accuracy Confidence Level: %f"
- "<<<< CMIColourConstancy >>>> %s: Constructing the balanced intensity density histogram. [balanceDenseToSparseExponentFactor: %.3f, minimumProbabilityDensity: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Constructing the colour intensity histogram. [numHistogramBins: %d]"
- "<<<< CMIColourConstancy >>>> %s: Constructing the kernel weighted intensity density histogram. [kernelSupportGaussianSigma: %.3f, kernelSupportSigmaToFilterScale: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Constructing the tone compression curve."
- "<<<< CMIColourConstancy >>>> %s: Could not initialize 'CMIColourConstancyClippingRecoveryConfigurationV1'"
- "<<<< CMIColourConstancy >>>> %s: Could not initialize 'CMIColourConstancyMicroHazeDetectionConfigurationV1'"
- "<<<< CMIColourConstancy >>>> %s: Create flash weighted thumbnail. [Input: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d]"
- "<<<< CMIColourConstancy >>>> %s: Create source transfer learning thumbnail. [InputSource: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d, Sharpness:%.3f, SigmaToFilterScale:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Create strobe weighted thumbnail. [Input: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d]"
- "<<<< CMIColourConstancy >>>> %s: Create target transfer learning thumbnail. [InputTarget: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d, Sharpness:%.3f, SigmaToFilterScale:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Decompose the strobe component image from the flash and ambient sensor space images"
- "<<<< CMIColourConstancy >>>> %s: Estimate Colour Accuracy Confidence. [StrobeIllumination: Edge0: %.3f, Edge1: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Estimate the Strobe Illumination Confidence. [StrobeIllumination: Edge0: %.3f, Edge1: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Final Crop Rectangle (Normalized Coordinates). [Sizes: Width:%0.3f Height:%0.3f] [Offsets: X:%0.3f Y:%0.3f]"
- "<<<< CMIColourConstancy >>>> %s: Finished processing."
- "<<<< CMIColourConstancy >>>> %s: Flash LSC gains compensation. [FlashLSCMaxGain: %.3f, BaseLSCMaxGain: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Flash LSC max gain: %f"
- "<<<< CMIColourConstancy >>>> %s: Flash Sensor Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
- "<<<< CMIColourConstancy >>>> %s: Flash brightness and white balance matching with fusion. [FlashToStrobeIntensityFusionMixFactor: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Flash integration time: %f"
- "<<<< CMIColourConstancy >>>> %s: Flash sensor space conversion. [WhitePoint: R: %.3f, G: %.3f, B: %.3f] [IntegrationTimeScale: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Flash white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Forward fftTransform encoding failed"
- "<<<< CMIColourConstancy >>>> %s: Gaussian filtering of flash weighted thumbnail. [GaussianSigma: %.3f, SigmaToFilterScale: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Gaussian filtering of strobe weighted thumbnail. [GaussianSigma: %.3f, SigmaToFilterScale: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Initializing ColourConstancyProcessor allocator with size: %lu, descriptor: %@"
- "<<<< CMIColourConstancy >>>> %s: Input texture sizes. Ambient: [Width: %d, Height: %d] Flash: [Width: %d, Height: %d]"
- "<<<< CMIColourConstancy >>>> %s: Inverse fftTransform encoding failed"
- "<<<< CMIColourConstancy >>>> %s: LSC Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
- "<<<< CMIColourConstancy >>>> %s: Metal allocator has already been set up"
- "<<<< CMIColourConstancy >>>> %s: Minimum Valid Buffer Crop Rectangle For GDC (Pixel Coordinates). [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
- "<<<< CMIColourConstancy >>>> %s: Output Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
- "<<<< CMIColourConstancy >>>> %s: Prepared memory size on the external metal allocator is too small (required:%lu bytes, got:%lu bytes)"
- "<<<< CMIColourConstancy >>>> %s: Received QSub capture. Assuming 2x crop."
- "<<<< CMIColourConstancy >>>> %s: Reconstruct target thumbnail using style transfer (QualityMode)."
- "<<<< CMIColourConstancy >>>> %s: Reconstruct target thumbnail using style transfer (SpeedMode)."
- "<<<< CMIColourConstancy >>>> %s: Register ambient bracket to flash bracket"
- "<<<< CMIColourConstancy >>>> %s: Registration of Luma frames. Homography: [%.3f, %.3f, %.3f; %.3f, %.3f, %.3f; %.3f, %.3f, %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Setting up ColourConstancy processor with provided metal command queue."
- "<<<< CMIColourConstancy >>>> %s: Strobe CCM: [%.3f, %.3f, %.3f; %.3f, %.3f, %.3f; %.3f, %.3f, %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Strobe beam profile correction. [CorrectionScale: Min: %.3f, Max: %.3f] [Component: Edge0: %.3f, Edge1: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: Strobe white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Style transfer (MainAlgo). [ClippingCorrection: Enabled:%@, Gain:%.3f, Exponent:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Style transfer (SpeedMode). [ClippingCorrection: Enabled:%@, Gain:%.3f, Exponent:%.3f]"
- "<<<< CMIColourConstancy >>>> %s: Style transfer tonal and white balancing changes to full resolution."
- "<<<< CMIColourConstancy >>>> %s: Thumbnail ambient frame with registration warping. [Luma: Width: %d, Height: %d] [Chroma: Width: %d, Height: %d] [ThumbnailOutput: Width: %d, Height: %d]"
- "<<<< CMIColourConstancy >>>> %s: Thumbnail flash frame. [Luma: Width: %d, Height: %d] [Chroma: Width: %d, Height: %d] [ThumbnailOutput: Width: %d, Height: %d]"
- "<<<< CMIColourConstancy >>>> %s: Using external metal allocator (size:%lu MB)"
- "<<<< CMIColourConstancy >>>> %s: WARNING: Strobe Calibration Data not found. Defaulting to hard coded calibration gains. Please ensure your device is up to date."
- "<<<< CMIColourConstancy >>>> %s: WARNING: Strobe Modulated CCM not found. Defaulting to Flash Modulated CCM. Please ensure your device is up to date."
- "<<<< CMIColourConstancy >>>> %s: White balance the strobe component. [StrobeWhitePoint: R: %.3f, G: %.3f, B: %.3f]"
- "<<<< CMIColourConstancy >>>> %s: addFrame called with unsupported frameType:%d"
- "<<<< CMIColourConstancy >>>> %s: encodeClassifierMasksExtraction failed"
- "<<<< CMIColourConstancy >>>> %s: encodeFusionMapExtraction failed"
- "<<<< CMIColourConstancy >>>> %s: encodeGradientExtraction:[ambient] failed"
- "<<<< CMIColourConstancy >>>> %s: encodeGradientExtraction:[flash] failed"
- "<<<< CMIColourConstancy >>>> %s: encodeGradientImageFusion failed"
- "<<<< CMIColourConstancy >>>> %s: encodeImagePyramidGeneration failed"
- "<<<< CMIColourConstancy >>>> %s: encodeImageReconstruction failed"
- "<<<< CMIColourConstancy >>>> %s: encodeIntensityGainMapGeneration failed"
- "<<<< CMIColourConstancy >>>> %s: encodeIntensityGainTransformsGeneration failed"
- "<<<< CMIColourConstancy >>>> %s: encodeIntensityImageGeneration failed"
- "<<<< CMIColourConstancy >>>> %s: encodeMicroHazeFusionMapExtraction failed"
- "<<<< CMIColourConstancy >>>> %s: encodeMixMapGeneration failed"
- "<<<< CMIColourConstancy >>>> %s: encodeShadowEdgeMapExtraction failed"
- "<<<< CMIColourConstancy >>>> %s: externalMemoryDescriptor is nil"
- "<<<< CMIColourConstancy >>>> %s: prepareToProcess for %d"
- "CMIColourConstancyStatusMetalAllocationFailed"
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "Failed to create Metal allocator"
- "Failed to initialize Metal context"
- "FigMetalAllocator setupWithDescriptor failed"
- "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
- "NO"
- "No Metal allocator"
- "YES"
- "_metalContext.allocator is NULL"
- "_regWarpGPU is NULL"
- "allocatorBackend is  nil"
- "allocatorDesc is NULL"
- "commandBuffer is NULL"
- "err"
- "metalContext is NULL"
- "self is NULL"

```
