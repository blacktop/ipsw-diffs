## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

 1667.22.1.0.0
-  __TEXT.__text: 0x349728
-  __TEXT.__objc_methlist: 0x15990
+  __TEXT.__text: 0x3497a0
+  __TEXT.__objc_methlist: 0x159b0
   __TEXT.__const: 0xe198
   __TEXT.__gcc_except_tab: 0xa868
   __TEXT.__cstring: 0x1049a8

   __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0xa8b0
+  __TEXT.__unwind_info: 0xa8a8
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e38
+  __DATA_CONST.__objc_selrefs: 0x8e50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1488
   __DATA_CONST.__got: 0xaf8
   __AUTH_CONST.__const: 0xde40
   __AUTH_CONST.__cfstring: 0x1dba0
-  __AUTH_CONST.__objc_const: 0x2b488
+  __AUTH_CONST.__objc_const: 0x2b4c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xdc8
   __AUTH_CONST.__objc_dictobj: 0x410

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15165
+  Functions: 15164
   Symbols:   28584
   CStrings:  8881
 
Functions:
~ __ZN2CI7Context16recursive_renderEPKNS_17RenderDestinationEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb : 6060 -> 6056
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE18__construct_at_endIPbS5_EEvT_T0_m : 196 -> 204
~ __ZN2CIL37RemoveFromStartUntilAtOrBelowCapacityEv : 648 -> 652
~ __ZN2CIL11convert_cpuEPNS_7ContextE13vImage_BufferS2_xxS2_S2_xxNS_11ConvertTypeE : 18456 -> 18452
~ ____ZN2CIL26get_converter_roi_callbackEPNS_4NodeENS_13ConvertReasonE_block_invoke : 768 -> 772
~ __ZNK2CI21SoftwareDAGDescriptor5printEP7__sFILE : 1668 -> 1684
~ __ZNK2CI21SoftwareDAGDescriptor7executeEPNS_26SWRendererFunctionArgumentE6CGRectPKNS_13BitmapSamplerE : 756 -> 784
~ __ZN2CI9DAGHelper17add_function_infoEPKNS_11ProgramNodeEPKNS_17GeneralKernelNodeEPNS_20SerialObjectPtrArrayEmmNS_11OtherDigestEPchRm : 3384 -> 3376
~ __ZNK2CI18SWRendererPipeline16execute_scanlineEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEmP10SamplerObjPviii : 408 -> 412
~ ___36-[CIAreaHistogram outputImageNonMPS]_block_invoke_2 : 1292 -> 1296
~ +[TiledHistogram processWithInputs:arguments:output:error:] : 580 -> 588
~ ___35-[CIAreaHoughTransform outputImage]_block_invoke : 376 -> 384
~ -[CIContext(_createCGImageInternal) _createCGImage:fromRect:format:premultiplied:colorSpace:deferred:renderCallback:] : 6032 -> 5992
~ ___122-[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:]_block_invoke.230 : 244 -> 248
~ -[CIContext(CIDepthBlurEffect) _performFaceDetection:image:orientation:filter:] : 1564 -> 1568
~ __ZN2CI20sw_convolutionrgb7x7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 4640 -> 4656
~ __ZN2CI17sw_convolution7x7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 4632 -> 4640
~ __ZN2CI14sw_crystallizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 1080 -> 1076
~ __ZN2CI21sw_faceMaskCalculatorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 1232 -> 1260
~ __ZN2CI16sw_gaussianBlur7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 416 -> 412
~ ___66+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]_block_invoke_2 : 2384 -> 2412
~ __ZN2CI8Tileable40TileRectGridMakeFromWidthAndHeightArraysENSt3__16vectorImNS1_9allocatorImEEEES5_ : 420 -> 424
~ __ZN16CIKLLibraryMaker9tokenizerEPKcP7__sFILEU13block_pointerFvS1_itS3_E : 420 -> 428
~ __ZN2CI24sw_raw_dm_interleaveRGGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 288 -> 292
~ __ZN2CI9sw_mesh16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 2604 -> 2620
~ __ZN2CI9sw_mesh32ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 5068 -> 5092
~ __ZL17CriticalPointsDOD6CGRect17CGAffineTransformP7CGPoint : 244 -> 256
~ __ZL11pageCurlROIi6CGRect17CGAffineTransformS0_S0_S_S_ : 1052 -> 1080
~ __ZN2CI31sw_pageCurlWithShadowTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 1888 -> 1900
~ __ZN2CI23sw_planarToInterleaved3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 364 -> 360
~ __ZN2CI23sw_planarToInterleaved4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm : 428 -> 424
~ -[CITemperatureAndTint setInputNeutral:] : 1980 -> 1984
~ _ConvertYCbCrtoREDEYEFORMAT : 1560 -> 1536
~ -[CIRedEyeRepair3(CIRedEyeRepair3Analyze) magnitudeMap:fromGabor:] : 136 -> 144
~ -[CIRedEyeRepair3(CIRedEyeRepair3Analyze) renderConvexHull:distance:fieldToBitmap:] : 1408 -> 1396
~ -[CIRedEyeRepair3(CIRedEyeRepair3Analyze) analyzeMask:usingConvexHull:producingOptimizedMask:] : 2108 -> 2112
~ -[CIRedEyeRepair3(CIRedEyeRepair3Analyze) attemptClosureOfThreadIndex:] : 1332 -> 1336
~ -[CIRedEyeRepair3(CIRedEyeRepair3Analyze) prominenceConvexHull:facts:] : 2724 -> 2736
~ _computeBitmask : 5632 -> 5636
~ _redEyeCancellation : 2004 -> 2032
~ _whiteEyeCancellation : 3568 -> 3580
~ _cornealReflectionBitmask : 1260 -> 1252
~ _infillChannelWithBitmask : 5308 -> 5312
~ _computePupilAlphaMap : 3908 -> 3920
~ _computeOutlineByTracingSnake : 3828 -> 3812
~ _computeBorderForAlpha : 916 -> 924
~ _minEnergyHopperInsert : 152 -> 156
~ -[CIRedEyeRepair redEyeRemovalWithPoint:alignPupilShades:matching:force:IOD:tap:] : 4132 -> 4160
~ ___getBytesAtPositionCallback_YCbYCr_block_invoke : 212 -> 216
~ ___getBytesAtPositionCallback_CbYCrY_block_invoke : 216 -> 220
~ ___getBytesAtPositionCallback_YCbYCrFull_block_invoke : 268 -> 272
~ ___getBytesAtPositionCallback_CbYCrYFull_block_invoke : 272 -> 276
~ ___getBytesAtPositionCallback_2C08_block_invoke : 76 -> 80
~ ___getBytesAtPositionCallback_1C08_block_invoke : 76 -> 80
~ ___getBytesAtPositionCallback_1C08_lut_block_invoke : 232 -> 236
~ ___getBytesAtPositionCallback_A008_block_invoke : 72 -> 76
~ _CI_xy_to_TempTint : 328 -> 332
~ __ZN2CIL20convert_ycch_to_420pEmm13vImage_BufferS0_S0_xx : 652 -> 656
~ __ZN2CIL20convert_ycch_to_444nEhmm13vImage_BufferS0_S0_xx : 424 -> 436
~ __ZN2CIL18convert_ycc_to_420IDF16_EEvmm13vImage_BufferS1_S1_xx : 376 -> 388
~ __block_invoke : 692 -> 696
~ ____ZNK2CI13ProviderImage20cgimage_for_graphvizEv_block_invoke_2 : 380 -> 388
~ __ZN2CI14MetalDAGHelper17add_function_infoEPKNS_11ProgramNodeEPKNS_17GeneralKernelNodeEPNS_20SerialObjectPtrArrayEmmNS_11OtherDigestEPchRmh : 6292 -> 6200
- __ZNSt3__16vectorINS_4pairIiiEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
~ __ZN2CI13TileCacheNode20getIntersectingTilesEPNS_8TileableE6CGRect : 648 -> 652
~ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKS1_EESA_EENS7_IPS1_EESA_T0_T1_l : 516 -> 532
~ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE12emplace_backIJS4_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryERNS_9allocatorIS4_EEE12emplace_backIJS4_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__insert_with_sizeB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l : 492 -> 508
~ __ZNK2CI8TileTask15pixelsOverdrawnEv : 1256 -> 1260
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_Lb0EEEvT1_SH_T0_NS_15iterator_traitsISH_E15difference_typeEb : 3132 -> 3136
```
