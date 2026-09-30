## VideoDeghostingV3

> `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/VideoDeghostingV3`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 764.22.13.0.0
-  __TEXT.__text: 0x29c0c
+  __TEXT.__text: 0x29c70
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x29a0
   __TEXT.__objc_methlist: 0x1c24
Functions:
~ -[disparityDebugUtils saveF32FPBuffer:AsPPMFile:scale:] : 456 -> 460
~ -[disparityDebugUtils saveF16Buffer:AsPPMFile:scale:] : 460 -> 464
~ -[disparityDebugUtils saveF16Texture:AsPPMFile:] : 460 -> 464
~ -[disparityDebugUtils saveF16DisparityBuffer:AsPPMFile:] : 288 -> 296
~ -[disparityDebugUtils saveF16DisparityBufferAsTurbo:AsPPMFile:WithMin:WithMax:] : 424 -> 428
~ -[disparityDebugUtils saveF16DisparityBuffer:AsGrayScalePPMFile:range:] : 552 -> 564
~ -[disparityDebugUtils saveF16Texture:AsGrayScalePPMFile:range:] : 620 -> 632
~ -[disparityDebugUtils saveU16Texture:AsPGMFile:] : 348 -> 352
~ -[disparityDebugUtils saveF16DisparityTexture:AsPPMFile:] : 344 -> 352
~ -[disparityDebugUtils saveRgbaF32PixelBuffer:AsPPMFile:] : 560 -> 564
~ -[disparityDebugUtils saveRGBAF16PixelBuffer:out_width:out_height:AsPPMFile:] : 560 -> 564
~ -[disparityDebugUtils saveRGBAF16PixelBuffer:out_width:out_height:AsPPMFileWithAlpha:] : 576 -> 580
~ -[disparityDebugUtils saveAccumulationFrom:asBinaryFiles:forSize:costLineSize:] : 1048 -> 1052
~ -[disparityDebugUtils saveRGBA16FTexture:AsPPMFile:] : 532 -> 536
~ -[disparityDebugUtils saveRGBA16FTexture:AsF32File:] : 400 -> 404
~ -[disparityDebugUtils saveRGB10A2Texture:AsPPMFile:] : 516 -> 520
~ _BoundingBoxToBuffer : 228 -> 232
~ -[RepairWeightsProcessor _temporalFilterMetaContainerAtIndex:ofQueue:lookaheadBufferLen:] : 2556 -> 2536
~ -[MaskToRoi getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:] : 632 -> 636
~ -[VideoDeghostingDetectionV3 process:metaData:ispTimeStamp:keypoints:lightSourceMask:futureFrames:] : 3208 -> 3220
~ -[HWGPUSimBridge pixelIsGhostWithDilationWithDilation:location:curGGCoord:GGCount:posInx:] : 132 -> 136
~ -[HWGPUSimBridge getWSpatialUsingTempAlignQualityLowLight_HWGPUWithGGCoord:GGCount:GGCountRef0:GGCountRef1:ggIndex:input:ref0:ref1:diffMax:] : 1044 -> 1052
~ -[CalcHomography _ispHomographyFromISPInfoFunc:] : 588 -> 592
~ -[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:] : 1316 -> 1320
~ _OUTLINED_FUNCTION_4 : 24 -> 64
~ _getWSpatialFromOverlap : 588 -> 592
~ _warpPrevMetaBuffer : 436 -> 448
~ -[CMIVideoDeghostingV3 _shouldRunVideoDeghosting:] : 772 -> 708
```
