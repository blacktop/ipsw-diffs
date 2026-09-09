## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`

```diff

 10.0.45.0.0
-  __TEXT.__text: 0x40720
+  __TEXT.__text: 0x40698
   __TEXT.__objc_methlist: 0x326c
   __TEXT.__const: 0x560
   __TEXT.__dlopen_cstrs: 0x228

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x409c
+  __TEXT.__gcc_except_tab: 0x40a8
   __TEXT.__oslogstring: 0x1d5
   __TEXT.__unwind_info: 0x1718
   __TEXT.__eh_frame: 0x80

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1298
+  Functions: 1297
   Symbols:   3845
   CStrings:  654
 
Functions:
~ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJmEEEPmDpOT_ : 184 -> 176
~ -[VisionCoreSparseOpticalFlowQuad generateGridKeypointsWithMaxKeypoints:minGridFrequency:] : 972 -> 980
~ -[VisionCoreSparseOpticalFlowSession updateMemoryKeypointsWithOpticalFlowResultsSourceBuffer:destBuffer:matchBuffer:start:] : 1188 -> 1196
~ __ZNSt3__16vectorIDhNS_9allocatorIDhEEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPDhEES8_EES8_NS6_IPKDhEET0_T1_l : 540 -> 556
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJRiEEEPiDpOT_ : 184 -> 176
~ -[VisionCoreValueConfidenceCurve confidenceForValue:] : 196 -> 204
~ -[VisionCoreValueConfidenceCurve encodeWithCoder:] : 856 -> 868
- __ZNSt3__16vectorI30VisionCoreValueConfidencePointNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
~ -[VisionCoreTensorStrides initWithShape:dataType:] : 632 -> 628
~ -[VisionCoreLKTSparseGPU _enqueueImagePyramidWithCommandBuffer:inputTexture:index:] : 648 -> 656
```
