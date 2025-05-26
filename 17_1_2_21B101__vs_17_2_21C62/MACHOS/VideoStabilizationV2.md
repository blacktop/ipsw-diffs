## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-465.15.2.0.0
-  __TEXT.__text: 0x28874
+470.16.1.0.0
+  __TEXT.__text: 0x28e30
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0x2700
-  __TEXT.__objc_methlist: 0xfe0
+  __TEXT.__objc_stubs: 0x2740
+  __TEXT.__objc_methlist: 0xff8
   __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methname: 0x4447
+  __TEXT.__objc_methname: 0x44f9
   __TEXT.__objc_methtype: 0x126b
-  __TEXT.__cstring: 0x39a9
-  __TEXT.__const: 0x5d0
+  __TEXT.__cstring: 0x3a85
+  __TEXT.__const: 0x5e0
   __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__unwind_info: 0x498
   __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__got: 0x598
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xcd8
   __DATA_CONST.__objc_arrayobj: 0x5d0
   __DATA_CONST.__objc_dictobj: 0x460
-  __DATA.__objc_const: 0x4730
-  __DATA.__objc_selrefs: 0xc10
+  __DATA.__objc_const: 0x47b0
+  __DATA.__objc_selrefs: 0xc28
   __DATA.__objc_classrefs: 0xd0
   __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0x3d0
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__bss: 0x24

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 466
-  Symbols:   400
-  CStrings:  1445
+  Functions: 469
+  Symbols:   403
+  CStrings:  1455
 
Symbols:
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputBiasRotationQuaternion
+ _kFigVideoStabilizationSampleBufferAttachmentKey_StabilizedOutputCameraGeometry
+ _kFigVideoStabilizationSampleBufferProcessorOption_AttachStabilizedOutputCameraTrajectory
+ _kFigVideoStabilizationSampleBufferProcessorOption_DisableTransformLimitsForPredeterminedTrajectory
+ _kFigVideoStabilizationSampleBufferProcessorOption_MotionBlurShimmerMitigationMethod
+ _objc_retain_x26
+ _objc_retain_x28
- _kFigVideoStabilizationSampleBufferProcessorOption_AttachStabilizedOutputCenterQuaternion
- _kFigVideoStabilizationSampleBufferProcessorOption_DisableTransformLimitsForPreComputedTrajectory
- _objc_retain_x24
- _objc_retain_x27
CStrings:
+ "( (storage->smoothingMethod) == kFigVideoStabilizationSmoothingMethod_PredeterminedTrajectory )"
+ "/tmp/transformLog_%p.txt"
+ "/tmp/transformLog_0x%p.txt"
+ "TB,N,V_attachStabilizedOutputCameraTrajectory"
+ "TB,N,V_disableTransformLimitsForPredeterminedTrajectory"
+ "Ti,N,V_motionBlurShimmerMitigationMethod"
+ "_attachStabilizedOutputCameraTrajectory"
+ "_disableTransformLimitsForPredeterminedTrajectory"
+ "_motionBlurShimmerMitigationMethod"
+ "attachStabilizedOutputCameraTrajectory"
+ "data && data.length == sizeof( *stabilizedCameraGeometry )"
+ "dataWithBytes:length:"
+ "disableTransformLimitsForPredeterminedTrajectory"
+ "motionBlurShimmerMitigationMethod"
+ "rotationBiasData.length == sizeof( simd_quatf )"
+ "sampleBuffer && rotationBiasQuaternion"
+ "sampleBuffer && storage && cameraMetadata"
+ "setAttachStabilizedOutputCameraTrajectory:"
+ "setDisableTransformLimitsForPredeterminedTrajectory:"
+ "setMotionBlurShimmerMitigationMethod:"
- "( (storage->smoothingMethod) == kFigVideoStabilizationSmoothingMethod_PreComputedTrajectory )"
- "/tmp/transformLog.txt"
- "TB,N,V_attachStabilizedOutputCenterQuaternion"
- "TB,N,V_disableTransformLimitsForPreComputedTrajectory"
- "_attachStabilizedOutputCenterQuaternion"
- "_disableTransformLimitsForPreComputedTrajectory"
- "attachStabilizedOutputCenterQuaternion"
- "disableTransformLimitsForPreComputedTrajectory"
- "setAttachStabilizedOutputCenterQuaternion:"
- "setDisableTransformLimitsForPreComputedTrajectory:"

```
