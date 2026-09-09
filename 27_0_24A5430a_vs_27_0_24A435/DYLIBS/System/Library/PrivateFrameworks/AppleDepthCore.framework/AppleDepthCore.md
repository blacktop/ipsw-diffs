## AppleDepthCore

> `/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`

```diff

 174.2.1.0.0
-  __TEXT.__text: 0x600b0
+  __TEXT.__text: 0x5fc08
   __TEXT.__objc_methlist: 0x2424
   __TEXT.__const: 0x21c0
   __TEXT.__gcc_except_tab: 0x5688
Functions:
~ -[ADInterSessionFilter insertEntry:withWeight:] : 4640 -> 4656
~ __ZL47reprojectUndistortedDepthMapWithInputImmediatesIfLj1717855600EElP10__CVBuffer13simd_float3x313simd_float4x3S2_S1_S1_ : 22284 -> 22028
~ __ZL47reprojectUndistortedDepthMapWithInputImmediatesIDhLj1751410032EElP10__CVBuffer13simd_float3x313simd_float4x3S2_S1_S1_ : 22496 -> 22240
~ __ZL47reprojectUndistortedDepthMapWithInputImmediatesIfLj1717856627EElP10__CVBuffer13simd_float3x313simd_float4x3S2_S1_S1_ : 22284 -> 22028
~ __ZL47reprojectUndistortedDepthMapWithInputImmediatesIDhLj1751411059EElP10__CVBuffer13simd_float3x313simd_float4x3S2_S1_S1_ : 22496 -> 22240
~ __ZL47reprojectUndistortedDepthMapWithInputImmediatesItLj825437747EElP10__CVBuffer13simd_float3x313simd_float4x3S2_S1_S1_ : 22672 -> 22436
~ -[ADInterSessionFilter dealloc] : 540 -> 548
~ -[ADInterSessionFilter persistenceData] : 864 -> 872
~ __ZNSt3__114__split_bufferIPP4NodeNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_ : 248 -> 252
~ __ZN27ADJasperPerformanceOverride11initFromCsvERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1936 -> 1944
~ +[UtilsForTests compareVImageBuffer:pixelTypeResult:offset:toRefBuffer:pixelTypeRef:ignoreResultZeros:ignoreRefZeros:outlierPercentile:] : 3848 -> 3860
~ __Z17compareRawBuffersIffE19BaselineTestStats_sPT_mPT0_mmmbbf : 1004 -> 1008
~ __Z17compareRawBuffersIDhDhE19BaselineTestStats_sPT_mPT0_mmmbbf : 1012 -> 1016
~ __Z17compareRawBuffersIDhfE19BaselineTestStats_sPT_mPT0_mmmbbf : 1008 -> 1012
~ +[UtilsForTests getJasperPointCloudFromPath:] : 836 -> 840
~ +[UtilsForTests pointsVectorFromFilePath:] : 2572 -> 2576
~ __ZN16PixelBufferUtils13forEveryPixelEP10__CVBufferS1_U13block_pointerFvPvjS2_jEi : 764 -> 768
~ __ZN16PixelBufferUtils22savePlyFromDepthBufferEP10__CVBufferPKcf7CGPointfffbb : 1184 -> 1188
~ -[ADReprojection updateWarpWithWarpedDepthBuffer:dimensions:validPixels:] : 2872 -> 2864
~ -[ADCameraCalibration hash] : 492 -> 484
```
