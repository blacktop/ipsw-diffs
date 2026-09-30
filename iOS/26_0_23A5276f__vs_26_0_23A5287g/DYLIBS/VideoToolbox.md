## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`

```diff

-3255.66.6.11.2
-  __TEXT.__text: 0x5129d8
+3255.68.6.11.3
+  __TEXT.__text: 0x5136e8
   __TEXT.__auth_stubs: 0x38f0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0xe2c
-  __TEXT.__const: 0x4188
-  __TEXT.__cstring: 0x38f69
+  __TEXT.__const: 0x4198
+  __TEXT.__cstring: 0x38feb
   __TEXT.__oslogstring: 0x28328
   __TEXT.__gcc_except_tab: 0xf0
   __TEXT.__dlopen_cstrs: 0x9b
-  __TEXT.__unwind_info: 0x5958
+  __TEXT.__unwind_info: 0x5978
   __TEXT.__eh_frame: 0x5b54
   __TEXT.__objc_classname: 0x37a
-  __TEXT.__objc_methname: 0x2451
-  __TEXT.__objc_methtype: 0x950
+  __TEXT.__objc_methname: 0x2460
+  __TEXT.__objc_methtype: 0x94e
   __TEXT.__objc_stubs: 0x18c0
   __DATA_CONST.__got: 0xdb0
-  __DATA_CONST.__const: 0x3a00
+  __DATA_CONST.__const: 0x3a78
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x1c88
   __AUTH_CONST.__const: 0x4d460
-  __AUTH_CONST.__cfstring: 0x24480
+  __AUTH_CONST.__cfstring: 0x244e0
   __AUTH_CONST.__objc_const: 0x3390
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D0C81F02-6B40-38A7-9FC8-47B5FF548ED6
-  Functions: 9018
-  Symbols:   22208
-  CStrings:  14584
+  UUID: F812A110-2956-3179-A2FB-F2BAF3286ECB
+  Functions: 9027
+  Symbols:   22237
+  CStrings:  14590
 
Symbols:
+ -[VTTemporalNoiseFilterParameters hasDiscontinuity]
+ -[VTTemporalNoiseFilterParameters initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:hasDiscontinuity:]
+ -[VTTemporalNoiseFilterParameters setHasDiscontinuity:]
+ GCC_except_table78
+ _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._hasDiscontinuity
+ _VTDecompressionSessionCopyAnalysisOptions
+ _VTDecompressionSessionSetContentAnalyzer2
+ _VTInitializeFunctionConstants
+ _VTLoadVTMetalTransferLibrary
+ ___VTDecompressionSessionRemoteXPC_Invalidate_block_invoke
+ ___VTDecompressionSessionSetContentAnalyzer_block_invoke
+ ___block_descriptor_76_e8_32r40r_e124_B108?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92^q100lr32l8r40l8
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.82
+ ___block_descriptor_tmp.88
+ ___block_literal_global.150
+ ___block_literal_global.54
+ ___block_literal_global.58
+ ___block_literal_global.69
+ ___block_literal_global.84
+ ___block_literal_global.90
+ _kVTCompressionPropertyKey_TemporalNoiseReductionLatencyMode
+ _kVTDecodeFrameOptionKey_ContentAnalyzerCropRectangle
+ _kVTDecodeFrameOptionKey_ContentAnalyzerRotation
+ _kVTTemporalNoiseReductionLatencyMode_Auto
+ _kVTTemporalNoiseReductionLatencyMode_Low
+ _kVTTemporalNoiseReductionLatencyMode_Medium
+ _objc_msgSend$hasDiscontinuity
+ _vtParavirtualizationHostDecoderSession_lookupRetainAndForgetPendingTilePixelBuffersAndUUIDsAndMappingIDs
+ _vtmtsGetRotationAndScale
- -[VTTemporalNoiseFilterParameters discontinuity]
- -[VTTemporalNoiseFilterParameters initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:discontinuity:]
- -[VTTemporalNoiseFilterParameters setDiscontinuity:]
- GCC_except_table76
- _OBJC_IVAR_$_VTTemporalNoiseFilterParameters._discontinuity
- ___block_descriptor_68_e8_32r_e124_B108?0{CGColorConversionIteratorData=Iqqqqqq^^{CGColorTRCData}^^{CGColorMatrixData}^^{CGColorNxMTransformData}}8q84q92^q100lr32l8
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.86
- ___block_literal_global.148
- ___block_literal_global.53
- ___block_literal_global.57
- ___block_literal_global.68
- ___block_literal_global.78
- ___block_literal_global.82
- ___block_literal_global.88
- _objc_msgSend$discontinuity
- _vtCreateVTMTSRenderPass
CStrings:
+ "ContentAnalyzerCropRectangle"
+ "ContentAnalyzerRotation"
+ "MCTFLatencyMode"
+ "TB,N,V_hasDiscontinuity"
+ "_hasDiscontinuity"
+ "description=CoreMedia_VideoToolbox-3255.68.6.11.3"
+ "hasDiscontinuity"
+ "initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:hasDiscontinuity:"
+ "setHasDiscontinuity:"
+ "v20@0:8B16"
+ "v56@?0^{__CVBuffer=}8{?=qiIq}16^{__CFDictionary=}40^{?=CC}48"
- "C"
- "TC,N,V_discontinuity"
- "_discontinuity"
- "description=CoreMedia_VideoToolbox-3255.66.6.11.2"
- "discontinuity"
- "initWithSourceFrame:nextFrames:previousFrames:destinationFrame:filterStrength:discontinuity:"
- "setDiscontinuity:"
- "v20@0:8C16"

```
