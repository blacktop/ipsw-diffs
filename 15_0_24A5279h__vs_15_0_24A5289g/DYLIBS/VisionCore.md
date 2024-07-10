## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/Versions/A/VisionCore`

```diff

-8.0.30.0.0
+8.0.32.2.0
   __TEXT.__text: 0x2f43c
   __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x24e4

   __TEXT.__dlopen_cstrs: 0x130
   __TEXT.__oslogstring: 0x1d5
   __TEXT.__unwind_info: 0xf08
-  __TEXT.__objc_classname: 0xa09
-  __TEXT.__objc_methname: 0x74b9
-  __TEXT.__objc_methtype: 0x20a9
+  __TEXT.__objc_classname: 0xa13
+  __TEXT.__objc_methname: 0x74c3
+  __TEXT.__objc_methtype: 0x20b3
   __TEXT.__objc_stubs: 0x3c80
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x3b8
Symbols:
+ -[VisionCoreLKTSparseGPU .cxx_destruct]
+ -[VisionCoreLKTSparseGPU _enqueueFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]
+ -[VisionCoreLKTSparseGPU _enqueueFeaturesWithCommandBuffer:in_tex:out_tex:]
+ -[VisionCoreLKTSparseGPU _enqueueImagePyramidWithCommandBuffer:inputTexture:index:]
+ -[VisionCoreLKTSparseGPU _enqueueMatchingBidirectionalWithCommandBuffer:in_f0_tex:in_f1_tex:in_f0_dxdy_tex:in_f1_dxdy_tex:in_kpts_buf:in_kptd_buf:out_kptd_buf:out_status_buf:bidirectional_error:num_keypoints:scale_kpts:scale_kptd:]
+ -[VisionCoreLKTSparseGPU _enqueueMatchingWithCommandBuffer:in_f0_tex:in_f1_tex:in_f0_dxdy_tex:in_kpts_buf:in_kptd_buf:out_kptd_buf:out_status_buf:num_keypoints:scale_kpts:scale_kptd:]
+ -[VisionCoreLKTSparseGPU _initMemory:height:nscales:]
+ -[VisionCoreLKTSparseGPU _setDefaultParameters]
+ -[VisionCoreLKTSparseGPU _setupBuffer]
+ -[VisionCoreLKTSparseGPU _setupPipelines]
+ -[VisionCoreLKTSparseGPU computeMatchingBidirectionalFromReferenceTexture:targetTexture:kptsBuffer:bidirectionalError:numKeypoints:]
+ -[VisionCoreLKTSparseGPU computeMatchingFromReferenceTexture:targetTexture:kptsBuffer:numKeypoints:]
+ -[VisionCoreLKTSparseGPU dealloc]
+ -[VisionCoreLKTSparseGPU initWithMetalContext:width:height:nscales:]
+ -[VisionCoreLKTSparseGPU keypointsStatus]
+ -[VisionCoreLKTSparseGPU keypointsTarget]
+ -[VisionCoreLKTSparseGPU nscales]
+ -[VisionCoreLKTSparseGPU ref_size]
+ -[VisionCoreLKTSparseGPU tgt_size]
+ -[VisionCoreLKTSparseGPU waitUntilCompleted]
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F0_dxdy_pxbuf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F0_dxdy_tex
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F0_pxbuf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F0_tex
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F1_dxdy_pxbuf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F1_dxdy_tex
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F1_pxbuf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._F1_tex
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._I_tex
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._commandQueue
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._computePipelines
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._kptd_buf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._maxThreadExecutionWidth
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._mtlContext
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._nscales
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._ref_pyr_size
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._ref_size
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._status_buf
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._tgt_pyr_size
+ OBJC_IVAR_$_VisionCoreLKTSparseGPU._tgt_size
+ _OBJC_CLASS_$_VisionCoreLKTSparseGPU
+ _OBJC_METACLASS_$_VisionCoreLKTSparseGPU
+ __OBJC_$_INSTANCE_METHODS_VisionCoreLKTSparseGPU
+ __OBJC_$_INSTANCE_VARIABLES_VisionCoreLKTSparseGPU
+ __OBJC_$_PROP_LIST_VisionCoreLKTSparseGPU
+ __OBJC_CLASS_RO_$_VisionCoreLKTSparseGPU
+ __OBJC_METACLASS_RO_$_VisionCoreLKTSparseGPU
- -[LKTSparseGPU .cxx_destruct]
- -[LKTSparseGPU _enqueueFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]
- -[LKTSparseGPU _enqueueFeaturesWithCommandBuffer:in_tex:out_tex:]
- -[LKTSparseGPU _enqueueImagePyramidWithCommandBuffer:inputTexture:index:]
- -[LKTSparseGPU _enqueueMatchingBidirectionalWithCommandBuffer:in_f0_tex:in_f1_tex:in_f0_dxdy_tex:in_f1_dxdy_tex:in_kpts_buf:in_kptd_buf:out_kptd_buf:out_status_buf:bidirectional_error:num_keypoints:scale_kpts:scale_kptd:]
- -[LKTSparseGPU _enqueueMatchingWithCommandBuffer:in_f0_tex:in_f1_tex:in_f0_dxdy_tex:in_kpts_buf:in_kptd_buf:out_kptd_buf:out_status_buf:num_keypoints:scale_kpts:scale_kptd:]
- -[LKTSparseGPU _initMemory:height:nscales:]
- -[LKTSparseGPU _setDefaultParameters]
- -[LKTSparseGPU _setupBuffer]
- -[LKTSparseGPU _setupPipelines]
- -[LKTSparseGPU computeMatchingBidirectionalFromReferenceTexture:targetTexture:kptsBuffer:bidirectionalError:numKeypoints:]
- -[LKTSparseGPU computeMatchingFromReferenceTexture:targetTexture:kptsBuffer:numKeypoints:]
- -[LKTSparseGPU dealloc]
- -[LKTSparseGPU initWithMetalContext:width:height:nscales:]
- -[LKTSparseGPU keypointsStatus]
- -[LKTSparseGPU keypointsTarget]
- -[LKTSparseGPU nscales]
- -[LKTSparseGPU ref_size]
- -[LKTSparseGPU tgt_size]
- -[LKTSparseGPU waitUntilCompleted]
- OBJC_IVAR_$_LKTSparseGPU._F0_dxdy_pxbuf
- OBJC_IVAR_$_LKTSparseGPU._F0_dxdy_tex
- OBJC_IVAR_$_LKTSparseGPU._F0_pxbuf
- OBJC_IVAR_$_LKTSparseGPU._F0_tex
- OBJC_IVAR_$_LKTSparseGPU._F1_dxdy_pxbuf
- OBJC_IVAR_$_LKTSparseGPU._F1_dxdy_tex
- OBJC_IVAR_$_LKTSparseGPU._F1_pxbuf
- OBJC_IVAR_$_LKTSparseGPU._F1_tex
- OBJC_IVAR_$_LKTSparseGPU._I_tex
- OBJC_IVAR_$_LKTSparseGPU._commandQueue
- OBJC_IVAR_$_LKTSparseGPU._computePipelines
- OBJC_IVAR_$_LKTSparseGPU._kptd_buf
- OBJC_IVAR_$_LKTSparseGPU._maxThreadExecutionWidth
- OBJC_IVAR_$_LKTSparseGPU._mtlContext
- OBJC_IVAR_$_LKTSparseGPU._nscales
- OBJC_IVAR_$_LKTSparseGPU._ref_pyr_size
- OBJC_IVAR_$_LKTSparseGPU._ref_size
- OBJC_IVAR_$_LKTSparseGPU._status_buf
- OBJC_IVAR_$_LKTSparseGPU._tgt_pyr_size
- OBJC_IVAR_$_LKTSparseGPU._tgt_size
- _OBJC_CLASS_$_LKTSparseGPU
- _OBJC_METACLASS_$_LKTSparseGPU
- __OBJC_$_INSTANCE_METHODS_LKTSparseGPU
- __OBJC_$_INSTANCE_VARIABLES_LKTSparseGPU
- __OBJC_$_PROP_LIST_LKTSparseGPU
- __OBJC_CLASS_RO_$_LKTSparseGPU
- __OBJC_METACLASS_RO_$_LKTSparseGPU
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Homography.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Normalization.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/RANSAC/RANSAC_Common.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Homography.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/Geometry2D/Geometry2D_Normalization.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/VisionCore/Libraries/cvml-Core/RANSAC/RANSAC_Common.c"

```
