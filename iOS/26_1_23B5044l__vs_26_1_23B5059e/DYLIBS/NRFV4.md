## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0x31c818
+664.40.15.122.3
+  __TEXT.__text: 0x31d098
   __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x11bd8
+  __TEXT.__objc_methlist: 0x11c08
   __TEXT.__const: 0x102fd8
-  __TEXT.__cstring: 0x5f724
+  __TEXT.__cstring: 0x5f744
   __TEXT.__gcc_except_tab: 0x2284
-  __TEXT.__oslogstring: 0x67719
+  __TEXT.__oslogstring: 0x67a7f
   __TEXT.__dlopen_cstrs: 0x10c
   __TEXT.__unwind_info: 0x5328
-  __TEXT.__objc_classname: 0x31f2
-  __TEXT.__objc_methname: 0x3410a
-  __TEXT.__objc_methtype: 0x171e6
-  __TEXT.__objc_stubs: 0x16400
+  __TEXT.__objc_classname: 0x31f3
+  __TEXT.__objc_methname: 0x341b1
+  __TEXT.__objc_methtype: 0x1722f
+  __TEXT.__objc_stubs: 0x16480
   __DATA_CONST.__got: 0xc28
   __DATA_CONST.__const: 0x13e0
   __DATA_CONST.__objc_classlist: 0xd98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6718
+  __DATA_CONST.__objc_selrefs: 0x6738
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa68

   __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0x820
   __AUTH_CONST.__cfstring: 0x13d00
-  __AUTH_CONST.__objc_const: 0x37358
+  __AUTH_CONST.__objc_const: 0x373b8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xb58
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH.__objc_data: 0x1220
-  __DATA.__objc_ivar: 0x3a3c
+  __DATA.__objc_ivar: 0x3a44
   __DATA.__data: 0xba8
   __DATA.__common: 0x30
   __DATA.__bss: 0x14

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F368552-9D54-3104-97A7-A6DA77E92A42
-  Functions: 13491
-  Symbols:   40712
-  CStrings:  25211
+  UUID: FB5DE18E-CA13-3B26-96AF-43269FCE46D1
+  Functions: 13497
+  Symbols:   40734
+  CStrings:  25226
 
Symbols:
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.14
+ -[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:].cold.4
+ -[LearnedFusionNetworkStageShared areRawAndLumaDiffRes]
+ -[LearnedFusionNetworkStageShared rawToLumaScale]
+ -[LearnedFusionNetworkStageShared setAreRawAndLumaDiffRes:]
+ -[LearnedFusionNetworkStageShared setRawToLumaScale:]
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._areRawAndLumaDiffRes
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._rawToLumaScale
+ _objc_msgSend$areRawAndLumaDiffRes
+ _objc_msgSend$rawToLumaScale
+ _objc_msgSend$setAreRawAndLumaDiffRes:
+ _objc_msgSend$setRawToLumaScale:
CStrings:
+ "-"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: hrGainDownRatio should be >= 1.0f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: %@: areRawAndLumaDiffRes: %d,  rawToLumaScale = {%f, %f}"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Invalid outputLuma to derive scale"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Scale factors must be >= 1.0 (got {%f, %f})"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: hrGainDownRatio should be >= 1.0f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFLanczos.m %s: RawDFLanczos: unsupported scale ratio %.4f (input: %lux%lu, output: %lux%lu). Only sqrt(2)≈%.4f, %.4f, and %.4f ratios are supported"
+ "T,N,V_rawToLumaScale"
+ "TB,N,V_areRawAndLumaDiffRes"
+ "^{?=Bffffffffff{?=ff}{?=ffff}fB}16@0:8"
+ "^{?=ffBB}16@0:8"
+ "_areRawAndLumaDiffRes"
+ "_rawToLumaScale"
+ "areRawAndLumaDiffRes"
+ "consts->hrGainDownRatio >= 1.0f"
+ "rawToLumaScale"
+ "setAreRawAndLumaDiffRes:"
+ "setRawToLumaScale:"
+ "{?=\"outGain\"f\"hrGainDownRatio\"f\"rotateTile180\"B\"isQuadra\"B}"
+ "{?=\"rotate180\"B\"hrGainDownRatio\"f\"lumaAddBackWeight\"f\"lumaAddBackBand0Weight\"f\"lumaAddBackClipToSNR\"f\"lumaAddBackLSCModulation\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f\"lumaAddBackSkinSlopeFactor\"f\"lumaAddBackSkySlopeFactor\"f\"lumaAddBackPersonSlopeFactor\"f\"whiteBalanceGains\"\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}\"lumaAddbackNoiseVars\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}\"fusedToFullScale\"\"sampleSizePixs\"f\"useDiffResPath\"B}"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFLanczos.m %s: RawDFLanczos: unsupported scale ratio %.4f (input: %lux%lu, output: %lux%lu). Only sqrt(2)≈1.414 and 1.1212 ratios are supported"
- "^{?=Bffffffffff{?=ff}{?=ffff}}16@0:8"
- "^{?=fBB}16@0:8"
- "{?=\"outGain\"f\"rotateTile180\"B\"isQuadra\"B}"
- "{?=\"rotate180\"B\"hrGainDownRatio\"f\"lumaAddBackWeight\"f\"lumaAddBackBand0Weight\"f\"lumaAddBackClipToSNR\"f\"lumaAddBackLSCModulation\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f\"lumaAddBackSkinSlopeFactor\"f\"lumaAddBackSkySlopeFactor\"f\"lumaAddBackPersonSlopeFactor\"f\"whiteBalanceGains\"\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}\"lumaAddbackNoiseVars\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}}"

```
