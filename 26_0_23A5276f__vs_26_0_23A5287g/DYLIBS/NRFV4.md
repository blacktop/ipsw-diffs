## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x2dc95c
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x103b8
-  __TEXT.__const: 0x1027b8
-  __TEXT.__cstring: 0x5a9ed
-  __TEXT.__gcc_except_tab: 0x1d08
-  __TEXT.__oslogstring: 0x4f125
+659.0.0.0.4
+  __TEXT.__text: 0x2de3b0
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x10400
+  __TEXT.__const: 0x1027c8
+  __TEXT.__cstring: 0x5b01b
+  __TEXT.__gcc_except_tab: 0x1d20
+  __TEXT.__oslogstring: 0x4f8e7
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4d38
+  __TEXT.__unwind_info: 0x4d48
   __TEXT.__objc_classname: 0x2dc0
-  __TEXT.__objc_methname: 0x31757
-  __TEXT.__objc_methtype: 0x15ece
-  __TEXT.__objc_stubs: 0x14ee0
-  __DATA_CONST.__got: 0xc10
-  __DATA_CONST.__const: 0x1330
+  __TEXT.__objc_methname: 0x31897
+  __TEXT.__objc_methtype: 0x15ee6
+  __TEXT.__objc_stubs: 0x14fa0
+  __DATA_CONST.__got: 0xc18
+  __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6170
+  __DATA_CONST.__objc_selrefs: 0x61b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x13060
-  __AUTH_CONST.__objc_const: 0x32808
+  __AUTH_CONST.__cfstring: 0x13180
+  __AUTH_CONST.__objc_const: 0x328a8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xae0
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x34fc
+  __DATA.__objc_ivar: 0x350c
   __DATA.__data: 0xb48
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0x7440
   __DATA_DIRTY.__bss: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59E94348-38D0-35BC-916C-B8E06FB9BEA1
-  Functions: 12554
-  Symbols:   37863
-  CStrings:  23630
+  UUID: 156B3B1E-F7A0-378E-857D-FAD6A16F00BC
+  Functions: 12571
+  Symbols:   37919
+  CStrings:  23698
 
Symbols:
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.2
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.3
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.4
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.5
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.6
+ -[LSCGainsPlist fillLSCGainsTextureFrom:tex:maxValuesRGBA:].cold.7
+ -[LearnedNRNetworkStage getNetworkPath].cold.1
+ -[NRFFrameProperties originalFrameHeight]
+ -[NRFFrameProperties originalFrameWidth]
+ -[NRFFrameProperties setOriginalFrameHeight:]
+ -[NRFFrameProperties setOriginalFrameWidth:]
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:]
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.1
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.10
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.2
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.3
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.4
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.5
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.6
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.7
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.8
+ -[RawDFProcessor addInputResource:backingPixelBufferDimensions:].cold.9
+ -[RawNightModeInferenceEspresso dealloc]
+ -[RawProcFrames _overrideRegistrationStatusIfNeeded:framePtr:isReferenceFrame:]
+ -[RawProcFrames registrationPolicy]
+ -[RawProcFrames setRegistrationPolicy:]
+ -[SoftISPInputFrame pixelFormat]
+ _FigCapturePixelFormatHasRegroupedLayoutDownscale
+ _NRFReportRecoverableError
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_DenoiseAndSharpeningPlist.enableEvenDownsample
+ _OBJC_IVAR_$_DenoiseAndSharpeningPlist.enableUpsampleOffset
+ _OBJC_IVAR_$_NRFFrameProperties._originalFrameHeight
+ _OBJC_IVAR_$_NRFFrameProperties._originalFrameWidth
+ _OBJC_IVAR_$_RawProcFrames._registrationPolicy
+ _OUTLINED_FUNCTION_46
+ ___NRFReportRecoverableError_block_invoke
+ _enableEvenDownsampleOverride
+ _enableUpsampleOffsetOverride
+ _espresso_plan_get_error_info
+ _exit
+ _getprogname
+ _kAMBNR_EnableEvenDownsample
+ _kAMBNR_EnableUpsampleOffset
+ _objc_msgSend$_overrideRegistrationStatusIfNeeded:framePtr:isReferenceFrame:
+ _objc_msgSend$addInputResource:backingPixelBufferDimensions:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$originalFrameHeight
+ _objc_msgSend$originalFrameWidth
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$setOriginalFrameHeight:
+ _objc_msgSend$setOriginalFrameWidth:
+ _strcmp
- -[CMIPostConfig ambnrInputPyramidGenerationEnabled]
- -[CMIPostConfig setAmbnrInputPyramidGenerationEnabled:]
- -[RawDFProcessor addInputResource:]
- -[RawDFProcessor addInputResource:].cold.1
- -[RawDFProcessor addInputResource:].cold.10
- -[RawDFProcessor addInputResource:].cold.2
- -[RawDFProcessor addInputResource:].cold.3
- -[RawDFProcessor addInputResource:].cold.4
- -[RawDFProcessor addInputResource:].cold.5
- -[RawDFProcessor addInputResource:].cold.6
- -[RawDFProcessor addInputResource:].cold.7
- -[RawDFProcessor addInputResource:].cold.8
- -[RawDFProcessor addInputResource:].cold.9
- _OBJC_IVAR_$_CMIPostConfig._ambnrInputPyramidGenerationEnabled
- _objc_msgSend$ambnrInputPyramidGenerationEnabled
- _objc_msgSend$setAmbnrInputPyramidGenerationEnabled:
CStrings:
+ "-[RawDFProcessor addInputResource:backingPixelBufferDimensions:]"
+ "-[RawNightModeInferenceEspresso loadEspressoNetworkFromPath:withStorageType:]"
+ "-[RawNightModeInferenceEspresso resetState]"
+ "-[RawProcFrames _overrideRegistrationStatusIfNeeded:framePtr:isReferenceFrame:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: Deferred processing: exiting due to recoverable error ( %@ )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/Common/NRFCommon.m %s: NRFReportRecoverableError called with message=%@, status=%d, doProcessAbortAndTTR=%s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: %{private}@ finishProcessing: %{private}s(err=%{public}d), stage = %{private}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _learnedNRNetworkStage final status error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed getting network path with err = %d, for model: %@, isBayer: %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _shared.networkModel is nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: networkIdentifier is nil for model: %@, isBayer: %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableEvenDownsampleOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableUpsampleOffsetOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableEvenDownsample value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableUpsampleOffset value; was '%d', now '%d'"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: %{private}@ finishProcessing: %{private}s(err=%{public}d), stage = %{private}@"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _backgroundLearnedNR final status error (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _rawDFNetworkStage final status error (%d)"
+ "<<<< RawNightMode >>>> %s: Failed to add network from '%{public}s': %{private}s (err:%{public}d)"
+ "<<<< RawNightMode >>>> %s: Failed to build plan from '%{public}s': %{private}s (err:%{public}d)"
+ "<<<< RawNightMode >>>> %s: Failed to destroy Espresso context (err:%{public}d)"
+ "<<<< RawNightMode >>>> %s: Failed to destroy Espresso plan: %{private}s (err:%{public}d)"
+ "<<<< RawProcFrames >>>> %s: Ignoring registraion error, frameID: %d, isReferenceFrame : %s, isEVM : %s"
+ "<<<< RawProcFrames >>>> %s: Incrementing _nRegisteredFrames, frameID: %d, isReferenceFrame : %s, isEVM : %s"
+ "<<<< RawProcFrames >>>> %s: Setting homography to identity, frameID: %d, isReferenceFrame : %s, isEVM : %s"
+ "EnableEvenDownsample"
+ "EnableUpsampleOffset"
+ "LSC table B channel starting index is incorrect"
+ "LSC table Gb channel starting index is incorrect"
+ "LSC table Gr channel starting index is incorrect"
+ "LSC table R channel starting index is incorrect"
+ "LSC table size is not normal"
+ "LSCGainGrid->data.version1.offsetToBCoefficients == LSCGainGrid->data.version1.xGridPointCount * LSCGainGrid->data.version1.yGridPointCount * 2"
+ "LSCGainGrid->data.version1.offsetToGbCoefficients == LSCGainGrid->data.version1.xGridPointCount * LSCGainGrid->data.version1.yGridPointCount * 3"
+ "LSCGainGrid->data.version1.offsetToGrCoefficients == 0"
+ "LSCGainGrid->data.version1.offsetToRCoefficients == LSCGainGrid->data.version1.xGridPointCount * LSCGainGrid->data.version1.yGridPointCount"
+ "LSCGainGrid->data.version1.xGridPointCount > 12 && LSCGainGrid->data.version1.xGridPointCount < 220 && LSCGainGrid->data.version1.yGridPointCount > 12 && LSCGainGrid->data.version1.yGridPointCount < 220"
+ "LSCGainGrid->version == FigCaptureStreamLSCGainGridVersion_1"
+ "NRFReportRecoverableError"
+ "NRFReportRecoverableError_block_invoke"
+ "Network error during processing with message < %@ >, status: %d"
+ "TQ,N,V_originalFrameHeight"
+ "TQ,N,V_originalFrameWidth"
+ "Tq,N,V_registrationPolicy"
+ "V1 LSC table is expected"
+ "_originalFrameHeight"
+ "_originalFrameWidth"
+ "_overrideRegistrationStatusIfNeeded:framePtr:isReferenceFrame:"
+ "_registrationPolicy"
+ "addInputResource:backingPixelBufferDimensions:"
+ "backgroundLearnedNR"
+ "com.apple.cameracapture.gpu-error"
+ "continuation"
+ "defaultCenter"
+ "deferredmediad"
+ "enableEvenDownsample"
+ "enableUpsampleOffset"
+ "i128@0:8@16@24@32@40@48@56@64@72@80@88@96104^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffBQQ}120"
+ "i56@0:8^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffBQQ}16@24@32I40I44B48B52"
+ "i64@0:8@16@24@32@40@48^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffBQQ}56"
+ "learnednoisereduction-quadra-v1"
+ "learnednoisereduction-quadra-v2"
+ "newFrameMetadata"
+ "newMetadata"
+ "nrf.abort_deferred_on_hard_failure"
+ "originalFrameHeight"
+ "originalFrameWidth"
+ "postNotificationName:object:userInfo:"
+ "registrationPolicy"
+ "setOriginalFrameHeight:"
+ "setOriginalFrameWidth:"
+ "setRegistrationPolicy:"
+ "title"
+ "v36@0:8^i16@24B32"
- "-[RawDFProcessor addInputResource:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: learnedNRNetworkStage getFinalProcessingStatus (finish) status error (%d)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Temporarily recovering from loading LearnedNR bayer v4 network back to v3"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Temporarily recovering from loading LearnedNR quadra v3 network back to: %@"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: %{private}@ finishProcessing: %{private}s(%{public}d)"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: backgroundLearnedNR final status error (%d)"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: rawDFNetworkStage final status error (%d)"
- "TB,N,V_ambnrInputPyramidGenerationEnabled"
- "_ambnrInputPyramidGenerationEnabled"
- "ambnrInputPyramidGenerationEnabled"
- "i128@0:8@16@24@32@40@48@56@64@72@80@88@96104^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}120"
- "i56@0:8^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}16@24@32I40I44B48B52"
- "i64@0:8@16@24@32@40@48^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}56"
- "learnednoisereduction-quadra-%@"
- "setAmbnrInputPyramidGenerationEnabled:"

```
