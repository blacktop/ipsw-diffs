## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x2e1444
-  __TEXT.__objc_methlist: 0x12e78
-  __TEXT.__const: 0x1031d8
-  __TEXT.__cstring: 0x5ec62
+761.0.0.0.3
+  __TEXT.__text: 0x2e5618
+  __TEXT.__objc_methlist: 0x130f8
+  __TEXT.__const: 0x1031f8
+  __TEXT.__cstring: 0x5f250
   __TEXT.__gcc_except_tab: 0x1cd8
-  __TEXT.__oslogstring: 0x442ad
+  __TEXT.__oslogstring: 0x447da
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x5708
+  __TEXT.__unwind_info: 0x57a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x14f0
-  __DATA_CONST.__objc_classlist: 0xe18
+  __DATA_CONST.__objc_classlist: 0xe38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f00
+  __DATA_CONST.__objc_selrefs: 0x6f88
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xae8
+  __DATA_CONST.__objc_superrefs: 0xb08
   __DATA_CONST.__objc_arraydata: 0xf08
   __DATA_CONST.__got: 0xf00
   __AUTH_CONST.__const: 0x9a0
-  __AUTH_CONST.__cfstring: 0x148c0
-  __AUTH_CONST.__objc_const: 0x3b168
+  __AUTH_CONST.__cfstring: 0x149c0
+  __AUTH_CONST.__objc_const: 0x3b9e0
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xc30
-  __AUTH_CONST.__objc_intobj: 0xa08
+  __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_floatobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x500
   __AUTH_CONST.__auth_got: 0x860
-  __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x3f38
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x3f94
   __DATA.__data: 0xc68
   __DATA.__common: 0x50
   __DATA.__bss: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15543
-  Symbols:   17708
-  CStrings:  14205
+  Functions: 15641
+  Symbols:   17824
+  CStrings:  14262
 
Symbols:
+ -[CMIPostConfig enableSRL]
+ -[CMIPostConfig setEnableSRL:]
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:processingTypes:]
+ -[RawDFProcessor _computeProxyGainMapWithInput:secondInput:outputTexture:referenceFrame:darkestFrame:delegate:]
+ -[SoftISPCalibrationConfig initWithStaticParameters:prepareDescriptor:]
+ -[SoftISPCalibrationShaders .cxx_destruct]
+ -[SoftISPCalibrationShaders clearSkipMask]
+ -[SoftISPCalibrationShaders downsample]
+ -[SoftISPCalibrationShaders initWithMetalContext:]
+ -[SoftISPCalibrationShaders markSkipPositions]
+ -[SoftISPCalibrationStage .cxx_destruct]
+ -[SoftISPCalibrationStage appendFocusPixelPositionsForInputFrame:to:]
+ -[SoftISPCalibrationStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[SoftISPCalibrationStage auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:]
+ -[SoftISPCalibrationStage awbGainsForInputFrame:]
+ -[SoftISPCalibrationStage bytesRequiredForConfig:]
+ -[SoftISPCalibrationStage configForPrepareDescriptor:outputCompressionLevel:]
+ -[SoftISPCalibrationStage createArgsWithConfig:bounds:inputFrame:outputFrame:]
+ -[SoftISPCalibrationStage createIntermediateMetalTexture:width:height:pixelFormat:]
+ -[SoftISPCalibrationStage ensureSkipMaskForWidth:height:cfaLayout:needsRebuildOut:]
+ -[SoftISPCalibrationStage initWithMetalContext:staticParameters:]
+ -[SoftISPCalibrationStage metal]
+ -[SoftISPCalibrationStage outputDownscaleFactor]
+ -[SoftISPCalibrationStage outputPixelFormatForInputPixelFormat:outputCompressionLevel:]
+ -[SoftISPCalibrationStage prepareToProcessWithDescriptor:]
+ -[SoftISPCalibrationStage producesOutputPixelBuffer]
+ -[SoftISPCalibrationStage runWithArgs:]
+ -[SoftISPCalibrationStage shaders]
+ -[SoftISPCalibrationStage skipPositionsForInputFrame:]
+ -[SoftISPCalibrationStage staticParameters]
+ -[SoftISPCalibrationStage validateInputFrame:config:]
+ -[SoftISPCalibrationStageArgs .cxx_destruct]
+ -[SoftISPCalibrationStageArgs bounds]
+ -[SoftISPCalibrationStageArgs config]
+ -[SoftISPCalibrationStageArgs dealloc]
+ -[SoftISPCalibrationStageArgs initWithConfig:bounds:inputFrame:outputFrame:]
+ -[SoftISPCalibrationStageArgs inputFrame]
+ -[SoftISPCalibrationStageArgs inputTex]
+ -[SoftISPCalibrationStageArgs outputFrame]
+ -[SoftISPCalibrationStageArgs setBounds:]
+ -[SoftISPCalibrationStageArgs setConfig:]
+ -[SoftISPCalibrationStageArgs setInputFrame:]
+ -[SoftISPCalibrationStageArgs setInputTex:]
+ -[SoftISPCalibrationStageArgs setOutputFrame:]
+ -[SoftISPInputFrame sensorBitDepth]
+ -[SoftISPPipeline producesOutputPixelBuffer]
+ -[SoftISPPipeline setProducesOutputPixelBuffer:]
+ -[SoftISPPrepareDescriptor downscaleFactor]
+ -[SoftISPPrepareDescriptor setDownscaleFactor:]
+ -[SoftISPProcessor pipelineProducesOutputPixelBuffer:]
+ -[SoftLTM isCalcGlobalHistOnROIEnabled:]
+ -[ToneMappingStage runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:enableSRL:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:]
+ _OBJC_CLASS_$_SoftISPCalibrationConfig
+ _OBJC_CLASS_$_SoftISPCalibrationShaders
+ _OBJC_CLASS_$_SoftISPCalibrationStage
+ _OBJC_CLASS_$_SoftISPCalibrationStageArgs
+ _OBJC_IVAR_$_CMIPostConfig._enableSRL
+ _OBJC_IVAR_$_SRLv4Plist._maxCurveBoostT
+ _OBJC_IVAR_$_SoftISPCalibrationShaders._clearSkipMask
+ _OBJC_IVAR_$_SoftISPCalibrationShaders._downsample
+ _OBJC_IVAR_$_SoftISPCalibrationShaders._markSkipPositions
+ _OBJC_IVAR_$_SoftISPCalibrationStage._8to10ExpansionLUT
+ _OBJC_IVAR_$_SoftISPCalibrationStage._8to12ExpansionLUT
+ _OBJC_IVAR_$_SoftISPCalibrationStage._metal
+ _OBJC_IVAR_$_SoftISPCalibrationStage._outputDownscaleFactor
+ _OBJC_IVAR_$_SoftISPCalibrationStage._shaders
+ _OBJC_IVAR_$_SoftISPCalibrationStage._skipMaskCFALayout
+ _OBJC_IVAR_$_SoftISPCalibrationStage._skipMaskHeight
+ _OBJC_IVAR_$_SoftISPCalibrationStage._skipMaskTex
+ _OBJC_IVAR_$_SoftISPCalibrationStage._skipMaskWidth
+ _OBJC_IVAR_$_SoftISPCalibrationStage._skipPositionsBuf
+ _OBJC_IVAR_$_SoftISPCalibrationStage._staticParameters
+ _OBJC_IVAR_$_SoftISPCalibrationStageArgs._bounds
+ _OBJC_IVAR_$_SoftISPCalibrationStageArgs._config
+ _OBJC_IVAR_$_SoftISPCalibrationStageArgs._inputFrame
+ _OBJC_IVAR_$_SoftISPCalibrationStageArgs._inputTex
+ _OBJC_IVAR_$_SoftISPCalibrationStageArgs._outputFrame
+ _OBJC_IVAR_$_SoftISPPipeline._producesOutputPixelBuffer
+ _OBJC_IVAR_$_SoftISPPrepareDescriptor._downscaleFactor
+ _OBJC_METACLASS_$_SoftISPCalibrationConfig
+ _OBJC_METACLASS_$_SoftISPCalibrationShaders
+ _OBJC_METACLASS_$_SoftISPCalibrationStage
+ _OBJC_METACLASS_$_SoftISPCalibrationStageArgs
+ __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationConfig
+ __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationShaders
+ __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationStage
+ __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationStageArgs
+ __OBJC_$_INSTANCE_VARIABLES_SoftISPCalibrationShaders
+ __OBJC_$_INSTANCE_VARIABLES_SoftISPCalibrationStage
+ __OBJC_$_INSTANCE_VARIABLES_SoftISPCalibrationStageArgs
+ __OBJC_$_PROP_LIST_SoftISPCalibrationShaders
+ __OBJC_$_PROP_LIST_SoftISPCalibrationStage
+ __OBJC_$_PROP_LIST_SoftISPCalibrationStageArgs
+ __OBJC_CLASS_PROTOCOLS_$_SoftISPCalibrationStage
+ __OBJC_CLASS_PROTOCOLS_$_SoftISPCalibrationStageArgs
+ __OBJC_CLASS_RO_$_SoftISPCalibrationConfig
+ __OBJC_CLASS_RO_$_SoftISPCalibrationShaders
+ __OBJC_CLASS_RO_$_SoftISPCalibrationStage
+ __OBJC_CLASS_RO_$_SoftISPCalibrationStageArgs
+ __OBJC_METACLASS_RO_$_SoftISPCalibrationConfig
+ __OBJC_METACLASS_RO_$_SoftISPCalibrationShaders
+ __OBJC_METACLASS_RO_$_SoftISPCalibrationStage
+ __OBJC_METACLASS_RO_$_SoftISPCalibrationStageArgs
+ _objc_msgSend$_computeProxyGainMapWithInput:secondInput:outputTexture:referenceFrame:darkestFrame:delegate:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendFocusPixelPositionsForInputFrame:to:
+ _objc_msgSend$awbGainsForInputFrame:
+ _objc_msgSend$clearSkipMask
+ _objc_msgSend$downsample
+ _objc_msgSend$downscaleFactor
+ _objc_msgSend$enableSRL
+ _objc_msgSend$ensureSkipMaskForWidth:height:cfaLayout:needsRebuildOut:
+ _objc_msgSend$isCalcGlobalHistOnROIEnabled:
+ _objc_msgSend$markSkipPositions
+ _objc_msgSend$producesOutputPixelBuffer
+ _objc_msgSend$runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:enableSRL:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:
+ _objc_msgSend$setEnableSRL:
+ _objc_msgSend$setProducesOutputPixelBuffer:
+ _objc_msgSend$skipPositionsForInputFrame:
- -[LearnedHRNRProcessor(Tuning) prepareTuning:]
- -[ToneMappingStage runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:]
- _objc_msgSend$runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:
CStrings:
+ "%@(inputPixelFormat=%c%c%c%c, maximumWidth=%u, maximumHeight=%u, downscaleFactor=%u)"
+ "-[LearnedHRNRProcessor(Tuning) prepareTuning:processingTypes:]"
+ "-[RawDFProcessor _computeProxyGainMapWithInput:secondInput:outputTexture:referenceFrame:darkestFrame:delegate:]"
+ "-[SoftISPCalibrationShaders initWithMetalContext:]"
+ "-[SoftISPCalibrationStage awbGainsForInputFrame:]"
+ "-[SoftISPCalibrationStage ensureSkipMaskForWidth:height:cfaLayout:needsRebuildOut:]"
+ "-[SoftISPCalibrationStage initWithMetalContext:staticParameters:]"
+ "-[SoftISPCalibrationStage prepareToProcessWithDescriptor:]"
+ "-[SoftISPCalibrationStage runWithArgs:]"
+ "-[SoftISPCalibrationStage validateInputFrame:config:]"
+ "-[SoftISPCalibrationStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[SoftISPProcessor pipelineProducesOutputPixelBuffer:]"
+ "-[ToneMappingStage runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:enableSRL:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFLanczos.m %s: RawDFLanczos: unsupported scale ratio %.4f (input: %lux%lu, output: %lux%lu). Only sqrt(2)≈%.4f, %.4f, %.4f, %.4f, and ≈1.0 ratios are supported"
+ "<<<< RawDFProcessor >>>> %s: _computeProxyGainMap failed, bailing (%d)"
+ "<<<< RawDFProxy >>>> %s: height for input ev0 (%d) and output (%d) do not match."
+ "<<<< RawDFProxy >>>> %s: output height for luma (%d) & chroma (%d) incorrect."
+ "<<<< RawDFProxy >>>> %s: output width for luma (%d) & chroma (%d) incorrect."
+ "<<<< RawDFProxy >>>> %s: width for input ev0 (%d) and output (%d) do not match."
+ "<<<< RawDFTuning >>>> %s: Tunning config: processingType: %d, sensorPort: %@, sensorID: %@, rawDFTuningType: %@, deviceGeneration: %d"
+ "<<<< RawProcInputFrame >>>> %s: rgbTex height (%d) does not match base height (%d * %d)"
+ "<<<< RawProcInputFrame >>>> %s: rgbTex width (%d) does not match base width (%d * %d)"
+ "<<<< SoftISP >>>> %s: Failed to allocate calibration shaders"
+ "<<<< SoftISP >>>> %s: Failed to create SoftISPCalibrationPipeline"
+ "<<<< SoftISP >>>> %s: Failed to create calibrationStage"
+ "<<<< SoftISP >>>> %s: Requested pipeline not found in supported set"
+ "<<<< SoftISP >>>> %s: SoftISPCalibration::clearSkipMask is nil"
+ "<<<< SoftISP >>>> %s: SoftISPCalibration::downsample is nil"
+ "<<<< SoftISP >>>> %s: SoftISPCalibration::markSkipPositions is nil"
+ "<<<< SoftISP >>>> %s: SoftISPCalibrationStage: AWB combo gains unavailable; skipping white-balance correction"
+ "<<<< SoftISP >>>> %s: SoftISPCalibrationStage: [super init] returned nil"
+ "<<<< SoftISP >>>> %s: SoftISPCalibrationStage: metal context is nil"
+ "<<<< SoftISP >>>> %s: SoftISPCalibrationStage: staticParameters is nil"
+ "<<<< SoftISP >>>> %s: Unsupported pipeline type"
+ "<<<< SoftISP >>>> %s: decompand8To10ToU16 failed; err=%d"
+ "<<<< SoftISP >>>> %s: decompand8To12To10ToU16 failed; err=%d"
+ "<<<< SoftISP >>>> %s: pipelines have not been initialised - cameraInfoByPort property needs to be set first."
+ "Calibration"
+ "Calibration shaders not loaded ( LCB disabled )"
+ "EnableGlobalHistOnROI"
+ "Failed to allocate skip positions buffer"
+ "Failed to create output texture"
+ "Failed to create skip-mask descriptor"
+ "Failed to create skip-mask texture"
+ "LCB"
+ "LastShownBuild:RawNightModeProcessorV4.m:849"
+ "LastShownDate:RawNightModeProcessorV4.m:849"
+ "Output dimensions degenerate"
+ "SoftISPCalibration::clearSkipMask"
+ "SoftISPCalibration::downsample"
+ "SoftISPCalibration::markSkipPositions"
+ "SoftISPCalibrationConfig.m"
+ "SoftISPCalibrationOutput"
+ "SoftISPCalibrationShaders.m"
+ "SoftISPCalibrationSkipMask"
+ "SoftISPCalibrationStage.m"
+ "SoftISPCalibrationStageArgs.m"
+ "_clearSkipMask"
+ "_downsample"
+ "_learnedHRNRNetworkStage is nil"
+ "_markSkipPositions"
+ "_skipMaskTex"
+ "_skipPositionsBuf"
+ "calibrationStage"
+ "calibrationStage addStage failed"
+ "createSoftISPCalibrationPipeline"
+ "downscaleFactor below minimum for this CFA layout"
+ "downscaleFactor must be a power of 2"
+ "invalid processingType - must be NRF_ProcessingType_RawNightMode"
+ "outputConfig missing for outputStageName"
+ "unsupported input pixel format"
+ "\xfa"
- "%@(inputPixelFormat=%c%c%c%c, maximumWidth=%u, maximumHeight=%u)"
- "-[LearnedHRNRProcessor(Tuning) prepareTuning:]"
- "-[ToneMappingStage runToneMapping:bilateralGrid:bilateralGridHomography:tmPlist:darkestFrameMetadata:ev0FrameMetadata:scaleInput:colorCorrection:hasChromaBias:quality:gridScaleFactor:inputIsLinear:stfAllowed:isLowLight:]"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFLanczos.m %s: RawDFLanczos: unsupported scale ratio %.4f (input: %lux%lu, output: %lux%lu). Only sqrt(2)≈%.4f, %.4f, %.4f, and %.4f ratios are supported"
- "<<<< RawDFProxy >>>> %s: height for input ev0 and output do not match."
- "<<<< RawDFProxy >>>> %s: output height for luma/chroma incorrect."
- "<<<< RawDFProxy >>>> %s: output width for luma/chroma incorrect."
- "<<<< RawDFProxy >>>> %s: width for input ev0 and output do not match."
- "<<<< RawProcInputFrame >>>> %s: rgbTex height does not match base height"
- "<<<< RawProcInputFrame >>>> %s: rgbTex width does not match base width"
- "LastShownBuild:RawNightModeProcessorV4.m:842"
- "LastShownDate:RawNightModeProcessorV4.m:842"
- "invalid processingType - must be NRF_ProcessingType_RawNightMode or NRF_ProcessingType_AdaptiveFusion"
- "outputStageName nil"
- "\xf9"
```
