## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-472.1.2.0.0
-  __TEXT.__text: 0x1eede0
-  __TEXT.__auth_stubs: 0xea0
+475.31.1.0.0
+  __TEXT.__text: 0x1ee928
+  __TEXT.__auth_stubs: 0xe90
   __TEXT.__objc_methlist: 0xde54
   __TEXT.__const: 0x102580
   __TEXT.__cstring: 0x2bc89
-  __TEXT.__gcc_except_tab: 0xdc4
+  __TEXT.__gcc_except_tab: 0xdcc
   __TEXT.__oslogstring: 0x1ef02
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x2d7c
+  __TEXT.__unwind_info: 0x2d88
   __TEXT.__objc_classname: 0x18a4d
-  __TEXT.__objc_methname: 0x2d4c0
-  __TEXT.__objc_methtype: 0x5863e
-  __TEXT.__objc_stubs: 0x12a40
+  __TEXT.__objc_methname: 0x2d64a
+  __TEXT.__objc_methtype: 0x586c4
+  __TEXT.__objc_stubs: 0x12a80
   __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0xc80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28298
-  __DATA_CONST.__objc_selrefs: 0x5510
+  __DATA_CONST.__objc_const: 0x282b8
+  __DATA_CONST.__objc_selrefs: 0x5520
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0xdd8
+  __DATA_CONST.__objc_superrefs: 0x930
   __DATA_CONST.__objc_arraydata: 0xc38
   __AUTH_CONST.__objc_const: 0x8c00
   __AUTH_CONST.__cfstring: 0x11560

   __AUTH_CONST.__objc_dictobj: 0x500
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x7d00
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xdd8
-  __DATA.__objc_superrefs: 0x930
   __DATA.__objc_ivar: 0x3080
   __DATA.__data: 0x950
   __DATA.__common: 0x100

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4783
-  Symbols:   18937
-  CStrings:  14448
+  Functions: 4784
+  Symbols:   18940
+  CStrings:  14463
 
Symbols:
+ _flushIOUnifiedAddressTranslatorWithDummyBuffer
+ _objc_msgSend$createMetalDevice
+ _objc_msgSend$setPurgeableState:
- _ldexp
CStrings:
+ "\x01\x92\xd2"
+ "\x04\xf0\xf0\xf0\xf2"
+ "T@\"<MTLTexture>\",?,&,N"
+ "T@\"CMIExternalMemoryResource\",?,&,N"
+ "T@\"CMIExternalMemoryResource\",?,&,N,V_externalMemoryResource"
+ "T@\"NRFProgressiveBracketingParameters\",?,&,N"
+ "T@\"NRFProgressiveBracketingParameters\",?,&,N,V_progressiveBracketingParameters"
+ "T@\"NSMutableDictionary\",?,&,N"
+ "T@\"NSMutableDictionary\",?,&,N,V_linearOutputMetadata"
+ "T@\"NSMutableDictionary\",?,&,N,V_quadraForEnhancedResOutputMetadata"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,V_learnedNREnabled"
+ "TB,?,N,V_stfAllowed"
+ "TB,?,R,N"
+ "T^{?=ff[8f][8f]f},R,N,V_gdcParameters"
+ "T^{__CVBuffer=},?,&,N"
+ "T^{__CVBuffer=},?,&,N,V_linearOutputPixelBuffer"
+ "T^{__CVBuffer=},?,&,N,V_quadraForEnhancedResInferenceInputPixelBuffer"
+ "T^{__CVBuffer=},?,&,N,V_quadraForEnhancedResOutputPixelBuffer"
+ "Ti,?,N"
+ "Ti,?,N,V_deepFusionProcessingMode"
+ "Ti,?,N,V_fusionMode"
+ "Ti,?,N,V_progressiveBatchSize"
+ "Ti,?,R,N"
+ "Ti,?,R,N,V_batchCount"
+ "T{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}},N,V_fusionParams"
+ "^{?=ff[8f][8f]f}"
+ "^{?=ff[8f][8f]f}16@0:8"
+ "createMetalDevice"
+ "i40@0:8@16@24^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}}32"
+ "i76@0:8@16[4@]24[4@]32[4@]40@48^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}}5664@68"
+ "i76@0:8@16i24@28r^{?=[3]}36@44@52^{?=ff[8f][8f]f}60^{?=ff[8f][8f]f}68"
+ "i84@0:8@16@24@32^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}}40485256@60B68B72I76I80"
+ "setOwnerWithIdentity:"
+ "v480@0:8{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}}16"
+ "{?=\"noiseModel\"{CMINoiseModel=\"invalid\"i\"shotNoiseVariance\"f\"readNoiseVariance\"f\"darkCurrentNoiseVariance\"f\"quantizationNoiseVariance\"f}\"homographies\"[4{?=\"columns\"[3]}]\"demWarpConfig\"{?=\"firstPix\"i\"isQuadra\"B\"applyGDC\"B\"inputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]\"forwardValidRadiusSqr\"f}\"outputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]\"forwardValidRadiusSqr\"f}\"useDense\"B}\"lscWbgParams\"{?=\"whiteBalanceGains\"\"lscParams\"{?=\"lscOffset\"\"lscNormalizationDims\"\"lscGridMaxGain\"f}}}"
+ "{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]\"forwardValidRadiusSqr\"f}"
+ "{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]f}{?=ff[8f][8f]f}B}{?={?=f}}}16@0:8"
+ "{RawNightModePreFusionParams=\"demWarpConfig\"{?=\"firstPix\"i\"isQuadra\"B\"applyGDC\"B\"inputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]\"forwardValidRadiusSqr\"f}\"outputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]\"forwardValidRadiusSqr\"f}\"useDense\"B}\"lscWbgParams\"{?=\"whiteBalanceGains\"\"lscParams\"{?=\"lscOffset\"\"lscNormalizationDims\"\"lscGridMaxGain\"f}}\"noiseMapScaling\"f}"
- "\x01\x92\xc2"
- "\x04\xf0\xf0\xf0\xd2"
- "T@\"CMIExternalMemoryResource\",&,N"
- "T@\"NRFProgressiveBracketingParameters\",&,N"
- "T@\"NRFProgressiveBracketingParameters\",&,N,V_progressiveBracketingParameters"
- "T@\"NSMutableDictionary\",&,N,V_quadraForEnhancedResOutputMetadata"
- "TB,N,V_learnedNREnabled"
- "T^{?=ff[8f][8f]},R,N,V_gdcParameters"
- "T^{__CVBuffer=},&,N,V_quadraForEnhancedResInferenceInputPixelBuffer"
- "T^{__CVBuffer=},&,N,V_quadraForEnhancedResOutputPixelBuffer"
- "Ti,N,V_deepFusionProcessingMode"
- "Ti,N,V_progressiveBatchSize"
- "Ti,R,N,V_batchCount"
- "T{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}},N,V_fusionParams"
- "^{?=ff[8f][8f]}"
- "^{?=ff[8f][8f]}16@0:8"
- "i40@0:8@16@24^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}}32"
- "i76@0:8@16[4@]24[4@]32[4@]40@48^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}}5664@68"
- "i76@0:8@16i24@28r^{?=[3]}36@44@52^{?=ff[8f][8f]}60^{?=ff[8f][8f]}68"
- "i84@0:8@16@24@32^{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}}40485256@60B68B72I76I80"
- "v464@0:8{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}}16"
- "{?=\"noiseModel\"{CMINoiseModel=\"invalid\"i\"shotNoiseVariance\"f\"readNoiseVariance\"f\"darkCurrentNoiseVariance\"f\"quantizationNoiseVariance\"f}\"homographies\"[4{?=\"columns\"[3]}]\"demWarpConfig\"{?=\"firstPix\"i\"isQuadra\"B\"applyGDC\"B\"inputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"outputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"useDense\"B}\"lscWbgParams\"{?=\"whiteBalanceGains\"\"lscParams\"{?=\"lscOffset\"\"lscNormalizationDims\"\"lscGridMaxGain\"f}}}"
- "{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}"
- "{?={CMINoiseModel=iffff}[4{?=[3]}]{?=iBB{?=ff[8f][8f]}{?=ff[8f][8f]}B}{?={?=f}}}16@0:8"
- "{RawNightModePreFusionParams=\"demWarpConfig\"{?=\"firstPix\"i\"isQuadra\"B\"applyGDC\"B\"inputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"outputFrameGDCParams\"{?=\"pixelPitch\"\"distortionCenter\"\"inverseScalingLUTBinSizeRecip\"f\"radiusScalingNormFactor\"f\"forwardCoefficients\"[8f]\"inverseCoefficients\"[8f]}\"useDense\"B}\"lscWbgParams\"{?=\"whiteBalanceGains\"\"lscParams\"{?=\"lscOffset\"\"lscNormalizationDims\"\"lscGridMaxGain\"f}}\"noiseMapScaling\"f}"

```
