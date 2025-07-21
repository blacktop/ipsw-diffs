## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-587.140.8.0.0
-  __TEXT.__text: 0x59a94
+587.140.9.0.0
+  __TEXT.__text: 0x5a094
   __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x2f40
+  __TEXT.__objc_stubs: 0x2f60
   __TEXT.__objc_methlist: 0x18dc
   __TEXT.__objc_classname: 0x1d4
-  __TEXT.__objc_methname: 0x5058
+  __TEXT.__objc_methname: 0x506e
   __TEXT.__objc_methtype: 0x14ae
   __TEXT.__const: 0x6a0
-  __TEXT.__oslogstring: 0xccd3
-  __TEXT.__cstring: 0x8dbb
+  __TEXT.__oslogstring: 0xcd97
+  __TEXT.__cstring: 0x8f87
   __TEXT.__gcc_except_tab: 0x620
   __TEXT.__unwind_info: 0x860
   __DATA_CONST.__auth_got: 0x680

   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_arrayobj: 0x1680
   __DATA.__objc_const: 0x3d98
-  __DATA.__objc_selrefs: 0xec0
+  __DATA.__objc_selrefs: 0xec8
   __DATA.__objc_ivar: 0x434
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC30D250-C457-3C4B-B334-AE76C317129A
-  Functions: 1165
-  Symbols:   2523
-  CStrings:  2716
+  UUID: B2C08332-5A19-3456-BD96-5DD4E143CEA3
+  Functions: 1174
+  Symbols:   2532
+  CStrings:  2728
 
Symbols:
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _objc_msgSend$forceMetalCachesFlush
+ _objc_msgSend$size
+ sbp_gvs_cinematicAddMetadataToQuaternionAndSphereRingBuffers.cold.2
+ sbp_gvs_createStabilizedSampleBuffer.cold.43
+ sbp_gvs_createStabilizedSampleBuffer.cold.44
+ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.12
+ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.13
- _objc_msgSend$inputIndex
Functions (modified):
~ _sbp_gvs_processSampleBuffer : 11332 -> 11316
~ _sbp_gvs_cinematicAddMetadataToQuaternionAndSphereRingBuffers : 5792 -> 5804
~ _sbp_gvs_gaussianAverageGetStabilizedSampleBuffer : 10300 -> 10352
~ _sbp_gvs_createStabilizedSampleBuffer : 15484 -> 15516
~ _OUTLINED_FUNCTION_26 : 36 -> 44
~ _OUTLINED_FUNCTION_27 : 44 -> 36
~ _OUTLINED_FUNCTION_31 : 28 -> 12
~ _OUTLINED_FUNCTION_38 : 16 -> 24
~ _OUTLINED_FUNCTION_39 : 24 -> 32
~ _OUTLINED_FUNCTION_41 : 32 -> 28
~ _OUTLINED_FUNCTION_43 : 28 -> 12
~ _OUTLINED_FUNCTION_44 : 12 -> 32
~ _OUTLINED_FUNCTION_45 : 32 -> 12
~ _OUTLINED_FUNCTION_46 : 12 -> 20
~ _OUTLINED_FUNCTION_47 : 20 -> 16
~ _OUTLINED_FUNCTION_55 : 24 -> 28
~ _OUTLINED_FUNCTION_57 : 12 -> 24
~ _OUTLINED_FUNCTION_68 : 20 -> 24
~ _OUTLINED_FUNCTION_74 : 32 -> 12
~ _sbp_gvs_finishPendingProcessing : 1636 -> 1944
~ __runSmartStyleFilterForwardLearning : 2572 -> 2588
~ _sbp_gvs_extractDistortionData : 2436 -> 2452
~ __enqueueCoefficientsForSmartStyleFilterForwardLearningFromCoefficientsSampleBuffer : 912 -> 928
~ FigSampleBufferProcessorCreateForGyroVideoStabilization.cold.34 : 208 -> 204
~ sbp_gvs_processSampleBuffer.cold.1 : 184 -> 176
~ sbp_gvs_processSampleBuffer.cold.16 : 208 -> 204
~ sbp_ltm_checkPerVideoDisablement.cold.1 : 184 -> 176
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.1 : 264 -> 176
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.2 : 244 -> 260
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.4 : 96 -> 244
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.6 : 176 -> 96
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.7 : 96 -> 176
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.10 : 124 -> 96
~ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.11 : 96 -> 168
~ sbp_gvs_createStabilizedSampleBuffer.cold.35 : 184 -> 176

Functions (added):
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_8
+ sbp_gvs_cinematicAddMetadataToQuaternionAndSphereRingBuffers.cold.2
+ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.12
+ sbp_gvs_gaussianAverageGetStabilizedSampleBuffer.cold.13
+ sbp_gvs_createStabilizedSampleBuffer.cold.43
+ sbp_gvs_createStabilizedSampleBuffer.cold.44
CStrings:
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Overscan analytics index out of bounds due to wrong quadraBinningFactor."
+ "<<<< GyroVideoStabilizationV2 >>>> %s: Unsupported port type in overscan analytics."
+ "cameraMetadata->currentPort <= kFigPortIndex_FrontFacingSuperWideCamera"
+ "cameraMetadata->quadraBinningFactor <= (2)"
+ "centerIndex overflow during stabilization."
+ "centerIndex overflow while flushing buffers."
+ "centerIndex underflow detected when loading metadata. VIS has received more metadata than was allocated for."
+ "centerIndex underflow during stabilization."
+ "centerIndex underflow while flushing buffers."
+ "forceMetalCachesFlush"
+ "smBuf.centerIndex >= 0"
+ "storage->smoothingBuffer.centerIndex < storage->smoothingBuffer.size"
+ "storage->smoothingBuffer.centerIndex >= 0"
- "storage->smoothingBuffer.centerIndex != storage->smoothingBuffer.inputIndex"

```
