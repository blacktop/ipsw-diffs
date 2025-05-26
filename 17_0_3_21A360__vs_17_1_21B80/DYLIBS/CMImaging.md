## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

-458.3.12.1.0
-  __TEXT.__text: 0x5d220
+465.15.2.0.0
+  __TEXT.__text: 0x5e094
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x3d88
-  __TEXT.__cstring: 0xbd6b
-  __TEXT.__const: 0x1fc0
+  __TEXT.__objc_methlist: 0x3df0
+  __TEXT.__cstring: 0xc076
+  __TEXT.__const: 0x1ff0
   __TEXT.__gcc_except_tab: 0x134
   __TEXT.__oslogstring: 0x490a
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0xc1c
+  __TEXT.__unwind_info: 0xc2c
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0xb8a
-  __TEXT.__objc_methname: 0x10ea0
-  __TEXT.__objc_methtype: 0x63a6
-  __TEXT.__objc_stubs: 0x55c0
+  __TEXT.__objc_classname: 0xbaa
+  __TEXT.__objc_methname: 0x110c8
+  __TEXT.__objc_methtype: 0x63d6
+  __TEXT.__objc_stubs: 0x5620
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x124e0
-  __DATA_CONST.__objc_selrefs: 0x1fd8
-  __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x438
+  __DATA_CONST.__objc_const: 0x12728
+  __DATA_CONST.__objc_selrefs: 0x2000
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x480
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH.__objc_data: 0x410
+  __AUTH.__objc_data: 0x460
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x330
+  __DATA.__objc_classrefs: 0x328
   __DATA.__objc_superrefs: 0x238
-  __DATA.__objc_ivar: 0x9e4
+  __DATA.__objc_ivar: 0xa10
   __DATA.__data: 0x9e0
   __DATA.__common: 0x20
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1424
-  Symbols:   5366
-  CStrings:  4870
+  Functions: 1433
+  Symbols:   5401
+  CStrings:  4922
 
Symbols:
+ -[FigRegWarpPPGPU _setTuningParams]
+ -[FigRegWarpPPGPU setTuningParams:]
+ -[FigRegWarpPPGPU tuningParams]
+ -[FigRegWarpPPGPUTuningParams .cxx_destruct]
+ -[FigRegWarpPPGPUTuningParams getMinCornerResponseThreshold:forBand:]
+ -[FigRegWarpPPGPUTuningParams maxNumberOfPyramidLevels]
+ -[FigRegWarpPPGPUTuningParams minCornerResponseThreshold]
+ -[FigRegWarpPPGPUTuningParams normalizeCornerResponse]
+ -[FigRegWarpPPGPUTuningParams performHistEq]
+ -[FigRegWarpPPGPUTuningParams readPlist:]
+ -[FigRegWarpPPGPUTuningParams useHalfPrecisionCornerResponse]
+ _OBJC_CLASS_$_FigRegWarpPPGPUTuningParams
+ _OBJC_IVAR_$_FigRegWarpPPGPU._normalizeCornerResponse
+ _OBJC_IVAR_$_FigRegWarpPPGPU._tuningParams
+ _OBJC_IVAR_$_FigRegWarpPPGPU._useHalfPrecisionCornerResponse
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFinalPassHalfPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFinalPassShortPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFirstPass4x4HalfPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFirstPass4x4ShortPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerResponseHalfPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerResponseShortPipeline
+ _OBJC_IVAR_$_FigRegWarpPPGPUTuningParams._maxNumberOfPyramidLevels
+ _OBJC_IVAR_$_FigRegWarpPPGPUTuningParams._minCornerResponseThreshold
+ _OBJC_IVAR_$_FigRegWarpPPGPUTuningParams._normalizeCornerResponse
+ _OBJC_IVAR_$_FigRegWarpPPGPUTuningParams._performHistEq
+ _OBJC_IVAR_$_FigRegWarpPPGPUTuningParams._useHalfPrecisionCornerResponse
+ _OBJC_METACLASS_$_FigRegWarpPPGPUTuningParams
+ __OBJC_$_INSTANCE_METHODS_FigRegWarpPPGPUTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_FigRegWarpPPGPUTuningParams
+ __OBJC_$_PROP_LIST_FigRegWarpPPGPUTuningParams
+ __OBJC_CLASS_RO_$_FigRegWarpPPGPUTuningParams
+ __OBJC_METACLASS_RO_$_FigRegWarpPPGPUTuningParams
+ ___block_descriptor_tmp.87
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.91
+ ___block_descriptor_tmp.93
+ __unnamed_array_storage.58
+ _bfpn_correct_nuhm
+ _objc_msgSend$_setTuningParams
+ _objc_msgSend$getMinCornerResponseThreshold:forBand:
+ _objc_msgSend$maxNumberOfPyramidLevels
+ _objc_msgSend$normalizeCornerResponse
+ _objc_msgSend$performHistEq
+ _objc_msgSend$useHalfPrecisionCornerResponse
- -[FigRegWarpPPGPU _setDefaultCornerMatchingParams]
- -[FigRegWarpPPGPU maxNumberOfPyramidLevels]
- -[FigRegWarpPPGPU setMaxNumberOfPyramidLevels:]
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSSet
- _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFinalPassPipeline
- _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerDetectionFirstPass4x4Pipeline
- _OBJC_IVAR_$_FigRegWarpPPGPUShaders._cornerResponsePipeline
- ___block_descriptor_tmp.86
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.90
- ___block_descriptor_tmp.92
- __unnamed_array_storage.59
- __unnamed_array_storage.72
- _objc_msgSend$_setDefaultCornerMatchingParams
- _objc_msgSend$intersectsSet:
- _objc_msgSend$setWithArray:
CStrings:
+ "\x02\x8f\x0f\x02\xf0\xf0\xf0\xf0\xf0\x82\xf0\xf0Q"
+ "\x0f\x01"
+ "@\"FigRegWarpPPGPUTuningParams\""
+ "Bands"
+ "C"
+ "FigRegWarpPPGPUTuningParams"
+ "MaxNumberOfPyramidLevels"
+ "MinCornerResponseThreshold"
+ "NormalizeCornerResponse"
+ "PerformHistEq"
+ "T@\"FigRegWarpPPGPUTuningParams\",&,N,V_tuningParams"
+ "T@\"NSArray\",R,N,V_minCornerResponseThreshold"
+ "TB,R,N,V_normalizeCornerResponse"
+ "TB,R,N,V_performHistEq"
+ "TB,R,N,V_useHalfPrecisionCornerResponse"
+ "TI,R,N,V_maxNumberOfPyramidLevels"
+ "UseHalfPrecisionCornerResponse"
+ "_cornerDetectionFinalPassHalfPipeline"
+ "_cornerDetectionFinalPassShortPipeline"
+ "_cornerDetectionFirstPass4x4HalfPipeline"
+ "_cornerDetectionFirstPass4x4ShortPipeline"
+ "_cornerResponseHalfPipeline"
+ "_cornerResponseShortPipeline"
+ "_minCornerResponseThreshold"
+ "_normalizeCornerResponse"
+ "_setTuningParams"
+ "_tuningParams"
+ "_useHalfPrecisionCornerResponse"
+ "band < _minCornerResponseThreshold.count"
+ "bandsTuning.count == _maxNumberOfPyramidLevels"
+ "bfpn_correct_nuhm failed"
+ "bfpn_correct_nuhm.c"
+ "g11p"
+ "getMinCornerResponseThreshold:forBand:"
+ "i28@0:8^f16I24"
+ "minCornerResponseThreshold"
+ "normalizeCornerResponse"
+ "performHistEq"
+ "readPlist:"
+ "retNUHMDCOffset != ((void*)0)"
+ "retNUHMDCOffset == NULL"
+ "retNUHMOPBOffset != ((void*)0)"
+ "retNUHMOPBOffset == NULL"
+ "rwppCornerDetectFinalPassHalf"
+ "rwppCornerDetectFinalPassShort"
+ "rwppCornerDetectFirstPass4x4Half"
+ "rwppCornerDetectFirstPass4x4Short"
+ "rwppCornerResponseHalf"
+ "rwppCornerResponseShort"
+ "setTuningParams:"
+ "supportsPartialRenderMemoryBarrier"
+ "threadgroupWidth * threadgroupHeight <= pipelineState.maxTotalThreadsPerThreadgroup"
+ "threshold"
+ "thumbImageF != ((void*)0)"
+ "thumbImageF == NULL"
+ "thumbImageF rowBytes incorrect"
+ "thumbImageF->data != ((void*)0)"
+ "thumbImageF->data == NULL"
+ "thumbImageF->height == ( 24 )"
+ "thumbImageF->height incorrect"
+ "thumbImageF->rowBytes >= sizeof( float ) * thumbImageF->width"
+ "thumbImageF->width == ( 33 )"
+ "thumbImageF->width incorrect"
+ "tuningParams"
+ "useHalfPrecisionCornerResponse"
+ "{?=\"dims\"{?=\"w\"I\"h\"I}\"roi\"{?=\"x\"I\"y\"I\"width\"I\"height\"I}\"normCoef\"{?=\"normX\"[2f]\"normY\"[2f]\"inverseX\"[2f]\"inverseY\"[2f]}\"minNCCThreshold\"f\"minCornerResponseThreshold\"f\"refGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"nrfGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"applyGDC\"B}"
- "\x02\x8f\x0f\x02\xf0\xf0\xf0\xf0\xf0\x82"
- "\r"
- "TI,N,V_maxNumberOfPyramidLevels"
- "_cornerDetectionFinalPassPipeline"
- "_cornerDetectionFirstPass4x4Pipeline"
- "_cornerResponsePipeline"
- "_setDefaultCornerMatchingParams"
- "flash2"
- "intersectsSet:"
- "rwppCornerDetectFinalPass"
- "rwppCornerDetectFirstPass4x4"
- "rwppCornerResponse"
- "setMaxNumberOfPyramidLevels:"
- "setWithArray:"
- "threadgroupWidth * threadgroupHeight <= _shaders->_cornerDetectionFirstPass4x4Pipeline.maxTotalThreadsPerThreadgroup"
- "threadgroupWidth * threadgroupHeight <= _shaders->_cornerResponsePipeline.maxTotalThreadsPerThreadgroup"
- "{?=\"dims\"{?=\"w\"I\"h\"I}\"roi\"{?=\"x\"I\"y\"I\"width\"I\"height\"I}\"normCoef\"{?=\"normX\"[2f]\"normY\"[2f]\"inverseX\"[2f]\"inverseY\"[2f]}\"minNCCThreshold\"f\"minCornerResponseThreshold\"s\"refGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"nrfGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"applyGDC\"B}"

```
