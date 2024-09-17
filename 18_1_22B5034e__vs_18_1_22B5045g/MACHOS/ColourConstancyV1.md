## ColourConstancyV1

> `/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1`

```diff

-580.2.0.0.0
-  __TEXT.__text: 0x1cb78
+580.6.21.0.0
+  __TEXT.__text: 0x1cdcc
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x2a60
-  __TEXT.__objc_methlist: 0x116c
+  __TEXT.__objc_stubs: 0x2aa0
+  __TEXT.__objc_methlist: 0x1184
   __TEXT.__const: 0x150
-  __TEXT.__objc_methname: 0x769d
-  __TEXT.__objc_classname: 0x436
-  __TEXT.__objc_methtype: 0x1425
-  __TEXT.__cstring: 0x61bd
-  __TEXT.__oslogstring: 0x1dab
+  __TEXT.__objc_methname: 0x7799
+  __TEXT.__objc_classname: 0x439
+  __TEXT.__objc_methtype: 0x11d9
+  __TEXT.__cstring: 0x632e
+  __TEXT.__oslogstring: 0x1e0d
   __TEXT.__unwind_info: 0x2d0
   __DATA_CONST.__auth_got: 0x220
   __DATA_CONST.__got: 0x160
-  __DATA_CONST.__cfstring: 0x11c0
+  __DATA_CONST.__cfstring: 0x11e0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3ba8
-  __DATA.__objc_selrefs: 0xbf0
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_const: 0x3c28
+  __DATA.__objc_selrefs: 0xc00
+  __DATA.__objc_ivar: 0x3a4
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x1e0
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 358
+  Functions: 360
   Symbols:   166
-  CStrings:  1502
+  CStrings:  1519
 
Symbols:
+ _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "_encodeScaledLSCGainsAndStrobeBeamProfileCalculate:ambientLSCGainsTexture:flashLSCGainsTexture:cropRect:LSCCropRect:fullSizeDimensions:ambientLSCMaxGain:flashLSCMaxGain:outputAmbientScaledLSCGainsRGBTexture:outputFlashScaledLSCGainsRGBTexture:outputStrobeBeamProfileGainRTexture:"
+ "_calculateScaledLSCGainsAndStrobeBeamProfilePipelineState"
+ "_encodeStyleTransferWithQualityMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:styleEngineCoefficientsTexture:styleEngineLinearSystemStatusFlagBuffer:styleEngineGammaCorrection:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
+ "i172@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{?=[3]}88136f152f156f160@164"
+ "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:"
+ "Encoding Scaled LSC gains and Strobe Beam Profile gains failed."
+ "i132@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}7288f104f108f112@116@124"
+ "i232@0:8@16@24@32@40@48@56@64@72@80f8892{CMIColourConstancyCropRect=iiii}108124B140f144f148{?=[3]}152f200f204B208f212@216@224"
+ "i164@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{?=[3]}88136f152@156"
+ "calculateScaledLSCGainsAndStrobeBeamProfile:ambientLSCGainsTexture:flashLSCGainsTexture:cropRect:LSCCropRect:fullSizeDimensions:ambientLSCMaxGain:flashLSCMaxGain:outputAmbientScaledLSCGainsRGBTexture:outputFlashScaledLSCGainsRGBTexture:outputStrobeBeamProfileGainRTexture:"
+ "i124@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}7288f104@108@116"
+ "_encodeStyleTransferWithSpeedMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
+ "_encodeStrobeCorrectionCalculate:strobeComponentRGBTexture:strobeBeamProfileGainRTexture:strobeBeamProfileScaleMinimum:strobeBeamProfileScaleMaximum:strobeBeamProfileComponentZeroThreshold:strobeBeamProfileComponentOneThreshold:outputStrobeCorrectedRGBTexture:"
+ "convertYUVtoNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:baseScaledLSCGainsRGBTexture:yuvOffsets:cropRect:appliedWhitePoint:integrationTimeScale:outputBalancedThumbnailRGBATexture:outputSensorThumbnailRGBATexture:"
+ "-[CMIColourConstancyStrobeCorrectionV1 applyStrobeCorrection:strobeComponentRGBTexture:strobeBeamProfileGainRTexture:outputStrobeCorrectedRGBTexture:]"
+ "_ambientScaledLSCThumbnailRGBTexture"
+ "convertYUVtoRegisteredNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:baseScaledLSCGainsRGBTexture:yuvOffsets:cropRect:registrationHomography:appliedWhitePoint:integrationTimeScale:outputWarpedSensorThumbnailRGBATexture:"
+ "i64@0:8@16@24@32f40f44f48f52@56"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "Failed to create ColourConstancy::calculateScaledLSCGainsAndStrobeBeamProfileV1 MTLComputePipelineState."
+ "applyStrobeCorrection:strobeComponentRGBTexture:strobeBeamProfileGainRTexture:outputStrobeCorrectedRGBTexture:"
+ "i184@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}8096{?=[3]}112@160@168@176"
+ "-[CMIColourConstancyStyleTransferV1 applyStyleTransferWithBufferClearing:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:]"
+ "_encodeYUVtoNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:baseScaledLSCGainsRGBTexture:yuvOffsets:cropRect:appliedWhitePoint:integrationTimeScale:clippedLikelihoodScale:clippedLikelihoodExponent:outputBalancedThumbnailRGBATexture:outputSensorThumbnailRGBATexture:"
+ "\x0f\a"
+ "i116@0:8@16@24@32{CMIColourConstancyCropRect=iiii}40{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}5676f84f88@92@100@108"
+ "_flashScaledLSCThumbnailRGBTexture"
+ "_strobeBeamProfileGainRTexture"
+ "i212@0:8@16@24@32@40@48@56@6472{CMIColourConstancyCropRect=iiii}88104B120f124f128{?=[3]}132f180f184B188f192@196@204"
+ "\x05"
+ "<<<< CMIColourConstancy >>>> %!s(MISSING): Reconstruct target thumbnail using style transfer (QualityMode)."
+ "Calculating the Scaled LSC gains and Strobe beam profile failed."
+ "_encodeYUVtoRegisteredNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:baseScaledLSCGainsRGBTexture:yuvOffsets:cropRect:registrationHomography:appliedWhitePoint:integrationTimeScale:clippedLikelihoodScale:clippedLikelihoodExponent:outputWarpedSensorThumbnailRGBATexture:"
+ "ColourConstancy::calculateScaledLSCGainsAndStrobeBeamProfileV1"
- "_encodeYUVtoNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:baseLSCGainsTexture:yuvOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedWhitePoint:appliedLSCMaxGain:baseLSCMaxGain:integrationTimeScale:clippedLikelihoodScale:clippedLikelihoodExponent:outputBalancedThumbnailRGBATexture:outputSensorThumbnailRGBATexture:"
- "convertYUVtoRegisteredNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:baseLSCGainsTexture:yuvOffsets:cropRect:LSCCropRect:fullSizeDimensions:registrationHomography:appliedWhitePoint:appliedLSCMaxGain:baseLSCMaxGain:integrationTimeScale:outputWarpedSensorThumbnailRGBATexture:"
- "i208@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}88108{?=[3]}116164f180f184f188f192f196@200"
- "convertYUVtoNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:baseLSCGainsTexture:yuvOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedWhitePoint:appliedLSCMaxGain:baseLSCMaxGain:integrationTimeScale:outputBalancedThumbnailRGBATexture:outputSensorThumbnailRGBATexture:"
- "_encodeStyleTransferWithSpeedMode:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
- "i92@0:8@16@24@32@40f48f52{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}5676@84"
- "_encodeStrobeCorrectionCalculate:strobeComponentRGBTexture:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:lscCropRect:fullSizeDimensions:strobeBeamProfileScaleMinimum:strobeBeamProfileScaleMaximum:strobeBeamProfileComponentZeroThreshold:strobeBeamProfileComponentOneThreshold:outputStrobeCorrectedRGBTexture:"
- "applyStrobeCorrection:strobeComponentRGBTexture:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:lscCropRect:fullSizeDimensions:outputStrobeCorrectedRGBTexture:"
- "-[CMIColourConstancyStyleTransferV1 applyStyleTransferWithBufferClearing:inputChromaTexture:appliedLSCGainsTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:]"
- "-[CMIColourConstancyStrobeCorrectionV1 applyStrobeCorrection:strobeComponentRGBTexture:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:lscCropRect:fullSizeDimensions:outputStrobeCorrectedRGBTexture:]"
- "i216@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}80{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}96116f124128{?=[3]}144@192@200@208"
- "i108@0:8@16@24@32@40f48f52{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}5676f84f88f92f96@100"
- "i244@0:8@16@24@32@40@48@56@6472{CMIColourConstancyCropRect=iiii}88{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}104124f132136B152f156f160{?=[3]}164f212f216B220f224@228@236"
- "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedLSCGainsTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:"
- "i200@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}88108{?=[3]}116164f180f184f188@192"
- "\x04"
- "i160@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}88108116f132f136f140@144@152"
- "i264@0:8@16@24@32@40@48@56@64@72@80f8892{CMIColourConstancyCropRect=iiii}108{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}124144f152156B172f176f180{?=[3]}184f232f236B240f244@248@256"
- "i168@0:8@16@24@32@40@4856{CMIColourConstancyCropRect=iiii}72{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}88108116f132f136f140f144f148@152@160"
- "_encodeStyleTransferWithQualityMode:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:styleEngineCoefficientsTexture:styleEngineLinearSystemStatusFlagBuffer:styleEngineGammaCorrection:inputYUVOffsets:cropRect:LSCCropRect:fullSizeDimensions:appliedLSCMaxGain:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
- "_encodeYUVtoRegisteredNormSensorSpaceThumbnail:inputLumaTexture:inputChromaTexture:appliedLSCGainsTexture:baseLSCGainsTexture:yuvOffsets:cropRect:LSCCropRect:fullSizeDimensions:registrationHomography:appliedWhitePoint:appliedLSCMaxGain:baseLSCMaxGain:integrationTimeScale:clippedLikelihoodScale:clippedLikelihoodExponent:outputWarpedSensorThumbnailRGBATexture:"

```
