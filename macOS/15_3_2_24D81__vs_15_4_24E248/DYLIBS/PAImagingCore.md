## PAImagingCore

> `/System/Library/PrivateFrameworks/PAImagingCore.framework/Versions/A/PAImagingCore`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0xd764
+751.0.104.0.0
+  __TEXT.__text: 0xd560
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0xebc
-  __TEXT.__const: 0x12aa
-  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__objc_methlist: 0xed4
+  __TEXT.__const: 0x12ca
+  __TEXT.__gcc_except_tab: 0x748
   __TEXT.__cstring: 0x131b
-  __TEXT.__unwind_info: 0x6d0
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__objc_classname: 0x1e7
   __TEXT.__objc_methname: 0x1dec
   __TEXT.__objc_methtype: 0xb91

   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x348
   __AUTH_CONST.__cfstring: 0xbe0
-  __AUTH_CONST.__objc_const: 0x1c28
+  __AUTH_CONST.__objc_const: 0x1c08
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A65A7975-0DC3-3582-9F21-029BEDAC870A
-  Functions: 420
+  UUID: 38478A22-6422-39C3-B3D4-0EC5F2A07F93
+  Functions: 416
   Symbols:   1123
   CStrings:  776
 
Symbols:
+ __ZNKSt3__16vectorI11MeasurementNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11MeasurementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorI11MeasurementNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne190102IPdS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__16vectorI11MeasurementNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI11MeasurementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorI11MeasurementNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne180100IPdS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
Functions:
~ __Z17intersectionPointRKN2PA6Quad2dES2_RK8CGVectord : 620 -> 516
- sub_1d34356ac
~ __Z15projectionPointRKN2PA8Vector2dERKNS_13LineSegment2dE : 140 -> 136
~ __ZNK2PA6Quad2d14simpleContainsERKNS_8Vector2dE : 260 -> 252
~ __Z35deriveScaledRectFromConstrainedRect6CGRectS_N2PA6Quad2dE7CGPoint : 628 -> 636
- sub_1d343604c
~ __Z17pointFromVertexIDRK6CGRecti : 280 -> 328
- sub_1d3436a48
~ -[PMRMutableDataSet appendDataSet:] : 624 -> 476
~ __ZN7DataSet6AppendEd : 212 -> 216
~ -[PMRMutableDataSet initWithCapacity:] : 244 -> 228
~ -[PMRStatistics initWithDataSet:] : 664 -> 656
~ __ZL6MedianRK7DataSet : 220 -> 216
~ -[PMRMeasurementList reserve:] : 188 -> 172
~ -[PMRMeasurementList appendMeasurementList:] : 784 -> 540
~ -[PMRMeasurementList appendMeasurements:] : 676 -> 688
~ -[PMRMeasurementList appendMeasurement:] : 432 -> 428
~ -[PMRMeasurementList copyWithZone:] : 244 -> 248
~ -[PMRStdDevMeasurementFilter filterDataSet:] : 384 -> 380
~ -[PMRStdDevMeasurementFilter filterMeasurementList:] : 396 -> 392
~ -[PMRStdDevMeasurementFilter filterMeasurements:] : 384 -> 380
~ -[PMRStreamingStatistics standardDeviation] : 52 -> 56
~ -[PMRStreamingStatistics variance] : 52 -> 56
~ -[PMRStreamingStatistics average] : 52 -> 56
~ -[PMRStreamingStatistics olympicMean] : 52 -> 56
~ -[PMRStreamingStatistics arithmeticMean] : 52 -> 56
~ -[PMRStreamingStatistics observeValue:] : 116 -> 124
~ -[IPARenderedImageData computeHistogram] : 132 -> 120
~ _CompareLab : 3752 -> 3712
~ _conv_setup : 576 -> 620
~ _convertScanLine : 1088 -> 1184
~ -[RKExportSettings exportFormat] : 228 -> 252
- sub_1d343ef04
~ -[PACropModel masterImageSize] : 56 -> 60
~ -[PACropModel getCropRect:newCropRect:straightenAngle:constrainWithAnchorPoint:strict:hitVertexId:] : 2284 -> 2212
~ -[PACropModel _getBoundingQuadFromAngle:withExpansionTol:] : 440 -> 436
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PrivateHeaders/IPAQuad2.h"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/Export/Requests/Image/PAExportImageFormat.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/Launch/PALauncher.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/PACropModel.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/PACropModelAlgo.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PrivateHeaders/IPAQuad2.h"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/Export/Requests/Image/PAExportImageFormat.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/Launch/PALauncher.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/PACropModel.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/paimagingcore/source/PACropModelAlgo.mm"

```
