## ColourConstancyV1

> `/System/Library/VideoProcessors/ColourConstancyV1.bundle/ColourConstancyV1`

```diff

-587.62.18.0.0
-  __TEXT.__text: 0x18f6c
+587.80.7.0.1
+  __TEXT.__text: 0x19208
   __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_stubs: 0x2a80
-  __TEXT.__objc_methlist: 0x1184
+  __TEXT.__objc_methlist: 0x119c
   __TEXT.__const: 0x100
-  __TEXT.__objc_methname: 0x7799
-  __TEXT.__objc_classname: 0x439
-  __TEXT.__objc_methtype: 0x11d9
-  __TEXT.__cstring: 0x549c
+  __TEXT.__objc_methname: 0x787c
+  __TEXT.__objc_classname: 0x43a
+  __TEXT.__objc_methtype: 0x1210
+  __TEXT.__cstring: 0x5668
   __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x158

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3c28
-  __DATA.__objc_selrefs: 0xbf8
-  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_const: 0x3ca8
+  __DATA.__objc_selrefs: 0xc08
+  __DATA.__objc_ivar: 0x3a8
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x1e0
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 359
+  Functions: 361
   Symbols:   161
-  CStrings:  1398
+  CStrings:  1406
 
CStrings:
+ "\x01\x11\"/\x01\x13\""
+ "( outputLinearRGBWidth == cropRectPixelCoords.width && outputLinearRGBHeight == cropRectPixelCoords.height ) || ( outputLinearRGBWidth == cropRectPixelCoords.width / 2 && outputLinearRGBHeight == cropRectPixelCoords.height / 2 )"
+ "Only the kCVPixelFormatType_128RGBAFloat format is supported as the linear RGB output type for CMIColourConstancyProcessorV1"
+ "T^{__CVBuffer=},&,N,V_outputLinearRGBPixelBuffer"
+ "_encodeStyleTransferWithQualityMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:styleEngineCoefficientsTexture:styleEngineLinearSystemStatusFlagBuffer:styleEngineGammaCorrection:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:"
+ "_encodeStyleTransferWithSpeedMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:"
+ "_outputLinearRGBPixelBuffer"
+ "_processorData.outputLinearRGBTexture"
+ "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:"
+ "applyWithAmbientLumaTexture:ambientChromaTexture:flashLumaTexture:flashChromaTexture:ambientYUVOffsets:flashYUVOffsets:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:ambientWhitePoint:flashWhitePoint:strobeWhitePoint:ambientIntegrationTime:flashIntegrationTime:cropRect:LSCCropRect:fullSizeDimensions:strobeCCM:outputColourAccuracyConfidenceTexture:outputLumaTexture:outputChromaTexture:outputLinearRGBTexture:"
+ "i192@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}8096{?=[3]}112@160@168@176@184"
+ "i220@0:8@16@24@32@40@48@56@6472{CMIColourConstancyCropRect=iiii}88104B120f124f128{?=[3]}132f180f184B188f192@196@204@212"
+ "i240@0:8@16@24@32@40@48@56@64@72@80f8892{CMIColourConstancyCropRect=iiii}108124B140f144f148{?=[3]}152f200f204B208f212@216@224@232"
+ "i284@0:8@16@24@32@404864@80@88f96f100104120136f152f156{CMIColourConstancyCropRect=iiii}160{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}176196{?=[3]}204@252@260@268@276"
+ "outputLinearRGBPixelBuffer"
+ "outputLinearRGBPixelBufferFormat == kCVPixelFormatType_128RGBAFloat"
+ "setOutputLinearRGBPixelBuffer:"
+ "{CMIColourConstancyProcessorDataV1=\"brackets\"[2{CMIColourConstancyBracketDataV1=\"lumaTexture\"@\"<MTLTexture>\"\"chromaTexture\"@\"<MTLTexture>\"\"bracketMetadata\"@\"NSDictionary\"\"lscGainsTexture\"@\"<MTLTexture>\"\"lscParams\"@\"NSDictionary\"}]\"outputLumaTexture\"@\"<MTLTexture>\"\"outputChromaTexture\"@\"<MTLTexture>\"\"outputColourAccuracyConfidenceTexture\"@\"<MTLTexture>\"\"outputLinearRGBTexture\"@\"<MTLTexture>\"}"
+ "\xf0\xf0A"
- "\x01\x11\"/\x13\x12"
- "_encodeStyleTransferWithQualityMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:styleEngineCoefficientsTexture:styleEngineLinearSystemStatusFlagBuffer:styleEngineGammaCorrection:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
- "_encodeStyleTransferWithSpeedMode:inputLumaTexture:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceThumbnailRGBTexture:targetThumbnailRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:clippingCorrectionEnabled:clippingCorrectionTransitionGain:clippingCorrectionTransitionExponent:strobeCCM:colourSaturationBoostGain:gammaCorrection:globalRGBToneCurveEnabled:globalRGBToneCurveBrightnessBoostFactor:outputLumaTexture:outputChromaTexture:"
- "applyStyleTransferWithBufferClearing:inputChromaTexture:appliedScaledLSCGainsRGBTexture:sourceRGBTexture:targetRGBTexture:toneCompressionCurveTexture:inputYUVOffsets:cropRect:appliedWhitePoint:strobeCCM:outputReconstructedTargetRGBTexture:outputLumaTexture:outputChromaTexture:"
- "applyWithAmbientLumaTexture:ambientChromaTexture:flashLumaTexture:flashChromaTexture:ambientYUVOffsets:flashYUVOffsets:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:ambientWhitePoint:flashWhitePoint:strobeWhitePoint:ambientIntegrationTime:flashIntegrationTime:cropRect:LSCCropRect:fullSizeDimensions:strobeCCM:outputColourAccuracyConfidenceTexture:outputLumaTexture:outputChromaTexture:"
- "i184@0:8@16@24@32@40@48@5664{CMIColourConstancyCropRect=iiii}8096{?=[3]}112@160@168@176"
- "i212@0:8@16@24@32@40@48@56@6472{CMIColourConstancyCropRect=iiii}88104B120f124f128{?=[3]}132f180f184B188f192@196@204"
- "i232@0:8@16@24@32@40@48@56@64@72@80f8892{CMIColourConstancyCropRect=iiii}108124B140f144f148{?=[3]}152f200f204B208f212@216@224"
- "i276@0:8@16@24@32@404864@80@88f96f100104120136f152f156{CMIColourConstancyCropRect=iiii}160{CMIColourConstancyLSCCropRect={CMIColourConstancyCropRect=iiii}B}176196{?=[3]}204@252@260@268"
- "{CMIColourConstancyProcessorDataV1=\"brackets\"[2{CMIColourConstancyBracketDataV1=\"lumaTexture\"@\"<MTLTexture>\"\"chromaTexture\"@\"<MTLTexture>\"\"bracketMetadata\"@\"NSDictionary\"\"lscGainsTexture\"@\"<MTLTexture>\"\"lscParams\"@\"NSDictionary\"}]\"outputLumaTexture\"@\"<MTLTexture>\"\"outputChromaTexture\"@\"<MTLTexture>\"\"outputColourAccuracyConfidenceTexture\"@\"<MTLTexture>\"}"
- "\xf0\xf0!"

```
