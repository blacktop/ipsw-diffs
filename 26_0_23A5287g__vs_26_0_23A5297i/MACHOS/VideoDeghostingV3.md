## VideoDeghostingV3

> `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/VideoDeghostingV3`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x30950
+661.0.0.0.3
+  __TEXT.__text: 0x31414
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x29a0
   __TEXT.__objc_methlist: 0x1c24
-  __TEXT.__const: 0xec8
-  __TEXT.__objc_methname: 0x6e42
-  __TEXT.__oslogstring: 0x1972
-  __TEXT.__cstring: 0x5acc
-  __TEXT.__objc_classname: 0x286
-  __TEXT.__objc_methtype: 0x49e5
-  __TEXT.__gcc_except_tab: 0x310
+  __TEXT.__const: 0xeb8
+  __TEXT.__objc_methname: 0x6e6c
+  __TEXT.__oslogstring: 0x19fa
+  __TEXT.__cstring: 0x5cc5
+  __TEXT.__objc_classname: 0x287
+  __TEXT.__objc_methtype: 0x4c51
+  __TEXT.__gcc_except_tab: 0x31c
   __TEXT.__unwind_info: 0x7c0
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0x1180
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__cfstring: 0x1360
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x4510
+  __DATA.__objc_const: 0x4530
   __DATA.__objc_selrefs: 0xf98
-  __DATA.__objc_ivar: 0x598
+  __DATA.__objc_ivar: 0x59c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x2c8
   __DATA.__common: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DEB1BD7-807D-3FCD-964A-CCDB377367E3
+  UUID: EEA3D3A6-2711-3F48-BDDD-9896AA57E7E0
   Functions: 888
-  Symbols:   2125
-  CStrings:  2180
+  Symbols:   2141
+  CStrings:  2214
 
Symbols:
+ OBJC_IVAR_$_VideoDeghostingDetectionV3._lightweightDetectorInputs
+ ___block_descriptor_76_e8_32s_e31_v24?0i8I12^{__CFDictionary=}16ls32l8
+ _kVGGMDetectionResult_LightweightDetector1FalseNegative
+ _kVGGMDetectionResult_LightweightDetector1FalsePositive
+ _kVGGMDetectionResult_LightweightDetector1TruePositive
+ _kVGGMDetectionResult_LightweightDetector2FalseNegative
+ _kVGGMDetectionResult_LightweightDetector2FalsePositive
+ _kVGGMDetectionResult_LightweightDetector2TruePositive
+ _kVGGMDetectionResult_LightweightDetector3FalseNegative
+ _kVGGMDetectionResult_LightweightDetector3FalsePositive
+ _kVGGMDetectionResult_LightweightDetector3TruePositive
+ _kVGGMDetectionResult_LightweightDetector4FalseNegative
+ _kVGGMDetectionResult_LightweightDetector4FalsePositive
+ _kVGGMDetectionResult_LightweightDetector4TruePositive
+ _kVGGMDetectionResult_LightweightDetector5FalseNegative
+ _kVGGMDetectionResult_LightweightDetector5FalsePositive
+ _kVGGMDetectionResult_LightweightDetector5TruePositive
- ___block_descriptor_80_e8_32s_e31_v24?0i8I12^{__CFDictionary=}16ls32l8
Functions:
~ -[MitigationHW spatialTemporalRepairThenFuseInplaceYUVInputBuf:frmIdx:frRef0Buf:frRef1Buf:metaBuf:ref0MetaBuf:ref1MetaBuf:metaBufHW:info:infoTPlusOrMinus1:infoTPlusOrMinus2:usePastAsRef:] : 2968 -> 3300
~ ___187-[MitigationHW spatialTemporalRepairThenFuseInplaceYUVInputBuf:frmIdx:frRef0Buf:frRef1Buf:metaBuf:ref0MetaBuf:ref1MetaBuf:metaBufHW:info:infoTPlusOrMinus1:infoTPlusOrMinus2:usePastAsRef:]_block_invoke : 640 -> 636
~ _packDetectionResult : 1472 -> 2872
~ -[VideoDeghostingDetectionV3 _initParamsWithTuningParamsDict:isLowLight:] : 852 -> 860
~ -[VideoDeghostingDetectionV3 prepareDataForNextFrameWithFrameData:outputFutureOpticalCenter:outputFutureLightSourceMaskTotalArea:doLite:] : 1264 -> 1268
~ -[VideoDeghostingDetectionV3 getWeightsOriginalFromInfo:] : 144 -> 212
~ -[VideoDeghostingDetectionV3 process:metaData:ispTimeStamp:keypoints:lightSourceMask:futureFrames:] : 3976 -> 3960
~ -[VideoDeghostingDetectionV3 configuration] : 28 -> 24
~ -[VideoDeghostingDetectionV3 setConfiguration:] : 28 -> 24
~ -[CMIVideoDeghostingV3 initWithCommandQueue:imageDimensions:tuningParameters:] : 1888 -> 1892
~ -[CMIVideoDeghostingV3 statistics] : 396 -> 424
~ -[CMIVideoDeghostingV3 repair] : 800 -> 1580
~ -[CMIVideoDeghostingV3 resetState] : 368 -> 384
~ -[RawMetaDataReader readMetaDataInfoFromSimulation:] : 1396 -> 1464
~ +[RawMetaDataReader readMetaDataFromDictionary:andValidWidth:andValidHeight:andLightSource:andKeyPoints:] : 1684 -> 1760
CStrings:
+ "<<<< VEVideoDeghostingV3 >>>> %s: GGCount buffer is not in the range. GGCount: %d"
+ "<<<< VEVideoDeghostingV3 >>>> %s: meta buffer is NULL"
+ "LightweightDetector1FalseNegative"
+ "LightweightDetector1FalsePositive"
+ "LightweightDetector1TruePositive"
+ "LightweightDetector2FalseNegative"
+ "LightweightDetector2FalsePositive"
+ "LightweightDetector2TruePositive"
+ "LightweightDetector3FalseNegative"
+ "LightweightDetector3FalsePositive"
+ "LightweightDetector3TruePositive"
+ "LightweightDetector4FalseNegative"
+ "LightweightDetector4FalsePositive"
+ "LightweightDetector4TruePositive"
+ "LightweightDetector5FalseNegative"
+ "LightweightDetector5FalsePositive"
+ "LightweightDetector5TruePositive"
+ "T{CMIVideoDeghostingStatistics=ddddddddddddddddddddd},R,N"
+ "_lightweightDetectorInputs"
+ "{?=\"scaleAdjustedTotalClippedPixelsCount\"f\"luxLevel\"i\"exposureTime\"f}"
+ "{CMIVideoDeghostingStatistics=\"averageGhostArea\"d\"averageGhostCount\"d\"opticalCenterOffsetMag\"d\"opticalCenterOffsetX\"d\"opticalCenterOffsetY\"d\"opticalCenterEstConfidence\"d\"lightweightDetector1TruePositive\"d\"lightweightDetector1FalsePositive\"d\"lightweightDetector1FalseNegative\"d\"lightweightDetector2TruePositive\"d\"lightweightDetector2FalsePositive\"d\"lightweightDetector2FalseNegative\"d\"lightweightDetector3TruePositive\"d\"lightweightDetector3FalsePositive\"d\"lightweightDetector3FalseNegative\"d\"lightweightDetector4TruePositive\"d\"lightweightDetector4FalsePositive\"d\"lightweightDetector4FalseNegative\"d\"lightweightDetector5TruePositive\"d\"lightweightDetector5FalsePositive\"d\"lightweightDetector5FalseNegative\"d}"
+ "{CMIVideoDeghostingStatistics=ddddddddddddddddddddd}16@0:8"
- "T{CMIVideoDeghostingStatistics=dddddd},R,N"
- "{CMIVideoDeghostingStatistics=\"averageGhostArea\"d\"averageGhostCount\"d\"opticalCenterOffsetMag\"d\"opticalCenterOffsetX\"d\"opticalCenterOffsetY\"d\"opticalCenterEstConfidence\"d}"
- "{CMIVideoDeghostingStatistics=dddddd}16@0:8"

```
