## libfaceCore.dylib

> `/System/Library/Frameworks/Vision.framework/libfaceCore.dylib`

```diff

-9.0.53.0.0
-  __TEXT.__text: 0x592594
+9.3.0.0.0
+  __TEXT.__text: 0x5925f0
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_methlist: 0x408
   __TEXT.__const: 0x7a128

   __TEXT.__eh_frame: 0xe38
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methname: 0xb66
-  __TEXT.__objc_methtype: 0x52d
+  __TEXT.__objc_methtype: 0x53b
   __TEXT.__objc_stubs: 0xb80
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x380

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBC1C27E-888D-3B94-B47C-576172F29A10
+  UUID: 8A1A15B0-2B92-3297-9F1E-2835896EFFC4
   Functions: 790
   Symbols:   2518
   CStrings:  423
Functions:
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE7reserveEm : 232 -> 248
~ __ZNK5apple6vision9libraries8facecore10processing9detection11FaceManager10groupFacesERNSt3__16vectorINS2_12FaceInternalENS6_9allocatorIS8_EEEEiffi : 1464 -> 1468
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRKS5_EEEPS5_DpOT_ : 328 -> 332
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE18__assign_with_sizeB8ne200100IPS5_SA_EEvT_T0_l : 424 -> 436
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 80 -> 84
~ __ZNSt3__16vectorIPN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS6_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS5_EESC_EESC_NSA_IPKS5_EET_T0_l : 572 -> 568
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS5_RS7_EEPS5_ : 188 -> 192
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em : 68 -> 72
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore10processing8tracking15keypointtracker14datastructures13KMatchingElemENS_9allocatorIS9_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNK5apple6vision9libraries8facecore10processing9detection9histogram13FaceHistogram24GetFaceHistogramAccuracyERNSt3__16vectorIdNS7_9allocatorIdEEEE : 992 -> 1008
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore4FaceENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJRKS5_EEEPS5_DpOT_ : 328 -> 332
~ __ZNSt3__16vectorINS0_IN5apple6vision9libraries8facecore12FaceInternalENS_9allocatorIS5_EEEENS6_IS8_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZN5apple6vision9libraries8facecore10processing9detection14PostProcessing11postProcessERNSt3__16vectorINS2_12FaceInternalENS6_9allocatorIS8_EEEEPhjj : 2104 -> 2108
~ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore4FaceENS_9allocatorIS5_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS5_EESC_EESC_NSA_IPKS5_EET_T0_l : 572 -> 568
~ __ZNSt3__16vectorIN5apple6vision9libraries8facecore4FaceENS_9allocatorIS5_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS5_RS7_EEPS5_ : 188 -> 192
CStrings:
+ "{Face=i{coord=ii}{coord=ii}{coord=ii}{coord=ii}fii{vector<double, std::allocator<double>>=^d^d{?=^d}}i{vector<apple::vision::libraries::facecore::coord, std::allocator<apple::vision::libraries::facecore::coord>>=^{coord}^{coord}{?=^{coord}}}iBBffBfBf^{naturalSmileData}}32@0:8@16@24"
+ "{unique_ptr<apple::vision::libraries::facecore::FaceCoreAPI, std::default_delete<apple::vision::libraries::facecore::FaceCoreAPI>>=\"\"{?=\"__ptr_\"^{FaceCoreAPI}}}"
- "{Face=i{coord=ii}{coord=ii}{coord=ii}{coord=ii}fii{vector<double, std::allocator<double>>=^d^d^d}i{vector<apple::vision::libraries::facecore::coord, std::allocator<apple::vision::libraries::facecore::coord>>=^{coord}^{coord}^{coord}}iBBffBfBf^{naturalSmileData}}32@0:8@16@24"
- "{unique_ptr<apple::vision::libraries::facecore::FaceCoreAPI, std::default_delete<apple::vision::libraries::facecore::FaceCoreAPI>>=\"__ptr_\"^{FaceCoreAPI}}"

```
