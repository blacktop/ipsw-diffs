## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

 616.100.0.0.0
-  __TEXT.__text: 0x355ab8
-  __TEXT.__objc_methlist: 0x2606c
-  __TEXT.__const: 0x8ee4
+  __TEXT.__text: 0x355d24
+  __TEXT.__objc_methlist: 0x26074
+  __TEXT.__const: 0x8ef4
   __TEXT.__dlopen_cstrs: 0x563
   __TEXT.__constg_swiftt: 0x1f2c
   __TEXT.__swift5_typeref: 0x1f06

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x254b8
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x10778
+  __TEXT.__unwind_info: 0x10770
   __TEXT.__eh_frame: 0x2ae8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x7e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x135a8
+  __DATA_CONST.__objc_selrefs: 0x135b0
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0xda8
   __DATA_CONST.__objc_arraydata: 0x920
   __DATA_CONST.__got: 0x22c8
   __AUTH_CONST.__const: 0x85d0
   __AUTH_CONST.__cfstring: 0xe780
-  __AUTH_CONST.__objc_const: 0x48dd8
+  __AUTH_CONST.__objc_const: 0x48df0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x460
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x1e20
+  __AUTH_CONST.__auth_got: 0x1e28
   __AUTH.__objc_data: 0xa698
   __AUTH.__data: 0xc20
   __DATA.__objc_ivar: 0x2cb8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 18461
-  Symbols:   40881
+  Symbols:   40882
   CStrings:  3595
 
Symbols:
+ _MGGetProductType
Functions:
~ __ZN25PKFunctionPiecewiseBezier5solveEv : 1368 -> 1376
~ __ZNK15PKBSplineFilter24calculateStepsForSegmentEmRK14_PKStrokePointS2_ : 1320 -> 1336
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ86-[PKTiledView updateTilesForVisibleRectRendering:offscreen:overrideAdditionalStrokes:]E3$_0P18AttachmentTileInfoLb0EEEvT1_S6_T0_NS_15iterator_traitsIS6_E15difference_typeEb : 3328 -> 3332
~ __ZNSt3__16vectorI12PKInputPointNS_9allocatorIS1_EEE6resizeEm : 372 -> 376
~ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ __Z26PKArcLengthsFromPointArrayRKNSt3__16vectorI7CGPointNS_9allocatorIS1_EEEERNS0_IdNS2_IdEEEE : 248 -> 252
~ __ZNSt3__16vectorIP6CGPathNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 184 -> 176
~ -[PKPaletteView allowedPalettePositions] : 96 -> 132
~ __ZNSt3__16vectorI23PKCompressedStrokePointNS_9allocatorIS1_EEE6resizeEm : 372 -> 376
~ -[PKPaletteToolPickerAndColorPickerView _compactToolsContainerMaximumWidth] : 68 -> 272
~ +[PKStroke(SynthesizeSupport) _createStrokesFromCHDrawing:transform:inputScale:sourceStrokes:strokeClass:newInk:suggestedHeight:shouldSetSynthesizedFlag:] : 3848 -> 3840
~ __ZNK18CGPathRandomAccess12clipperPathsEd : 1896 -> 1900
~ ____ZN18CGPathRandomAccess7addPathEPK6CGPath_block_invoke.4 : 2000 -> 2016
~ __ZNSt3__16vectorIlNS_9allocatorIlEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIPN10ClipperLib8PolyNodeENS_9allocatorIS3_EEE6resizeEm : 284 -> 288
~ __ZN10ClipperLib11ClipperBase7AddPathERKNSt3__16vectorINS_8IntPointENS1_9allocatorIS3_EEEENS_8PolyTypeEb : 2400 -> 2380
~ __ZN10ClipperLib13ClipperOffset8DoOffsetEd : 4108 -> 4092
~ __ZN10ClipperLib12CleanPolygonERKNSt3__16vectorINS_8IntPointENS0_9allocatorIS2_EEEERS5_d : 760 -> 764
~ __ZN10ClipperLib13CleanPolygonsERKNSt3__16vectorINS1_INS_8IntPointENS0_9allocatorIS2_EEEENS3_IS5_EEEERS7_d : 212 -> 224
~ __ZN10ClipperLib9MinkowskiERKNSt3__16vectorINS_8IntPointENS0_9allocatorIS2_EEEES7_RNS1_IS5_NS3_IS5_EEEEbb : 3116 -> 3072
~ __ZN10ClipperLib12MinkowskiSumERKNSt3__16vectorINS_8IntPointENS0_9allocatorIS2_EEEERKNS1_IS5_NS3_IS5_EEEERS9_b : 856 -> 860
~ __ZNSt3__16vectorIPN10ClipperLib6OutRecENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 184 -> 176
~ __ZNSt3__16vectorIxNS_9allocatorIxEEE24__emplace_back_slow_pathIJRKxEEEPxDpOT_ : 184 -> 176
~ -[PKStroke(Slicing) _appendPointsOfInterestForSelectionMasked:] : 700 -> 704
~ +[PKStroke(Slicing) sliceWithEraser:toClip:clipType:] : 4328 -> 4340
~ -[PKDrawing(Slicing) sliceWithEraseStroke:honoringErasable:] : 4688 -> 4704
~ __ZNSt3__16vectorIPN10ClipperLib8PolyNodeENS_9allocatorIS3_EEE18__insert_with_sizeB9foe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS3_EESB_EESB_NS9_IPKS3_EET0_T1_l : 552 -> 568
~ __ZNSt3__16vectorIU8__strongP7NSArrayIP8PKStrokeENS_9allocatorIS6_EEEC2B9foe220106EmRU8__strongKS5_ : 120 -> 128
~ __ZNSt3__16vectorIU8__strongP8PKStrokeNS_9allocatorIS3_EEEC2B9foe220106EmRU8__strongKS2_ : 148 -> 156
~ -[PKHoverController _handleHoverInputPoint:] : 1516 -> 1512
~ -[PKHoverController currentMovementSpeed] : 436 -> 432
~ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 500 -> 496
~ __ZNSt3__114__split_bufferI7CGPointRNS_9allocatorIS1_EEE12emplace_backIJRKS1_EEEvDpOT_ : 264 -> 268
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIP10PolarPointEEEEvT1_S9_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeESE_PNSD_10value_typeEl : 1324 -> 1328
~ -[PKPaletteHostView _updatePaletteViewLayoutGuideInsets] : 284 -> 508
~ __ZNSt3__16vectorIN2PB4DataENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 272 -> 268
~ -[PKMetalRenderer generatePaintCacheForStroke:animatingStroke:segmentSteps:liveStrokePoints:liveStrokeStartTime:duration:] : 2532 -> 2536
~ -[PKMetalRenderer generateParticleCacheForStroke:animatingStroke:starts:ends:secondaryParticles:] : 2408 -> 2404
~ -[PKMetalRenderer generateCacheForStroke:points:segmentSteps:] : 3216 -> 3244
~ -[PKMetal3DObject initWithCommandQueue:modelFile:library:pixelSize:maxTextureBlur:] : 3628 -> 3632
~ -[PKShapeDrawingController _strokeFromPoints:inputScale:averageInputPoint:sourceStroke:] : 1912 -> 1904
~ __ZNSt3__16vectorI17TimestampedAnglesNS_9allocatorIS1_EEE6resizeEm : 284 -> 288
~ _PKPaletteContentTopInset : 424 -> 500
~ __ZN22PKPixelSmoothingFilter25copyUpdatedRangeFromIndexEmPNSt3__16vectorI12PKInputPointNS0_9allocatorIS2_EEEE : 820 -> 824
~ __ZN17PKStartHookFilter25copyUpdatedRangeFromIndexEmPNSt3__16vectorI12PKInputPointNS0_9allocatorIS2_EEEE : 732 -> 720
~ __ZN15PKEndHookFilter25copyUpdatedRangeFromIndexEmPNSt3__16vectorI12PKInputPointNS0_9allocatorIS2_EEEE : 1236 -> 1224
~ __ZN27PKVelocityCalculationFilter25copyUpdatedRangeFromIndexEmPNSt3__16vectorI12PKInputPointNS0_9allocatorIS2_EEEE : 2380 -> 2384
~ _$ss20_ArrayBufferProtocolPsE22_arrayOutOfPlaceUpdateyys011_ContiguousaB0Vy7ElementQzGz_S2iySpyAGG_SitXEtFs06_SliceB0Vy9PencilKit13PKRefineMorphV5MatchV0P2ToVG_Tg5 : 592 -> 596
~ _$s9PencilKit13PKRefineMorphV11calcMatches11fromDrawing02toH07maxDistSayAC5MatchVGAC8NDrawingV_AL12CoreGraphics7CGFloatVtFZTf4nnnd_n : 2964 -> 2968
~ _$ss20_ArrayBufferProtocolPsE15replaceSubrange_4with10elementsOfySnySiG_Siqd__ntSlRd__7ElementQyd__AGRtzlFs01_aB0Vy9PencilKit13PKRefineMorphV5MatchV0N2ToVG_s0A5SliceVyARGTg5Tf4nngn_n : 304 -> 316
~ _$ss20_ArrayBufferProtocolPsE15replaceSubrange_4with10elementsOfySnySiG_Siqd__ntSlRd__7ElementQyd__AGRtzlFs011_ContiguousaB0Vy9PencilKit13PKRefineMorphV5MatchV0O2ToVG_s15EmptyCollectionVyARGTg5Tf4nndn_n : 184 -> 192
~ _$s9PencilKit13PKRefineMorphV07computeD04from2to0F9ViewFrame0ghI009transformH7ToModelAC8GridMeshV_AKtSayAA8PKStrokeVG_ANSo6CGRectVAPSo17CGAffineTransformVtFZTf4nnnnnd_n : 5032 -> 5028
~ ___83-[PKMetalRendererController liveStrokeParticlesToFrame:strokes:startTime:duration:]_block_invoke : 1628 -> 1636
```
