## RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0x11f1c
+664.40.15.122.3
+  __TEXT.__text: 0x128d0
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0xce0
+  __TEXT.__objc_stubs: 0x1400
+  __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x17c9
-  __TEXT.__oslogstring: 0x2060
-  __TEXT.__objc_methname: 0x285b
+  __TEXT.__cstring: 0x17ec
+  __TEXT.__oslogstring: 0x21a8
+  __TEXT.__objc_methname: 0x2985
   __TEXT.__objc_classname: 0x28a
-  __TEXT.__objc_methtype: 0x1033
-  __TEXT.__gcc_except_tab: 0x5c0
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__objc_methtype: 0x10c6
+  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__unwind_info: 0x428
   __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x23a8
-  __DATA.__objc_selrefs: 0x770
+  __DATA.__objc_const: 0x2408
+  __DATA.__objc_selrefs: 0x7a0
   __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F0543B0-EF89-31D0-9FF2-D30E06C4A369
-  Functions: 274
-  Symbols:   913
-  CStrings:  866
+  UUID: 9C3A8360-D40F-3D02-A5DD-06F702E7F2FE
+  Functions: 280
+  Symbols:   922
+  CStrings:  879
 
Symbols:
+ -[RTSCProcessorV1 _processPreview]
+ -[RTSCProcessorV1 rollingShutterCompensationEnabled]
+ -[RTSCProcessorV1 setRollingShutterCompensationEnabled:]
+ -[RTSCProcessorV1 setStabilizationSmoothingDisabled:]
+ -[RTSCProcessorV1 stabilizationSmoothingDisabled]
+ -[RTSCRealTimeStabilization _applyFinalAdjustmentsToStabilizedCameraForInputPose:cameraMetadata:]
+ -[RTSCRealTimeStabilization _clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]
+ -[RTSCRealTimeStabilization _computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:]
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table40
+ OBJC_IVAR_$_RTSCProcessorV1._rollingShutterCompensationEnabled
+ OBJC_IVAR_$_RTSCProcessorV1._stabilizationSmoothingDisabled
+ OBJC_IVAR_$_RTSCRealTimeStabilization._smoothedCameraModel
+ _objc_msgSend$_applyFinalAdjustmentsToStabilizedCameraForInputPose:cameraMetadata:
+ _objc_msgSend$_clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:
+ _objc_msgSend$_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:
+ _objc_msgSend$_processPreview
- -[RTSCRealTimeStabilization _clampStabilizedCameraToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]
- -[RTSCRealTimeStabilization _computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:computeAdjustment:]
- GCC_except_table25
- GCC_except_table32
- GCC_except_table34
- GCC_except_table37
- GCC_except_table39
- OBJC_IVAR_$_RTSCRealTimeStabilization._faceCorrectionUpdated
- OBJC_IVAR_$_RTSCRealTimeStabilization._postStabilizationAdjustment
- OBJC_IVAR_$_RTSCRealTimeStabilization._stabilizedCameraModel
- _objc_msgSend$_clampStabilizedCameraToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:
- _objc_msgSend$_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:computeAdjustment:
CStrings:
+ "-[RTSCProcessorV1 _processPreview]"
+ "-[RTSCRealTimeStabilization _clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]"
+ "<<<< RTSCProcessorV1 >>>> %s: Forcing identity transform for preview. _rollingShutterCompensationEnabled %d. _stabilizationSmoothingDisabled %d"
+ "<<<< RTSCProcessorV1 >>>> %s: enableFaceReframing is not supported for processingType: %d"
+ "<<<< RTSCProcessorV1 >>>> %s: zoomOutForMultiSubjects is not supported for processingType: %d"
+ "TB,N,V_rollingShutterCompensationEnabled"
+ "TB,N,V_stabilizationSmoothingDisabled"
+ "_applyFinalAdjustmentsToStabilizedCameraForInputPose:cameraMetadata:"
+ "_clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:"
+ "_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:"
+ "_processPreview"
+ "_rollingShutterCompensationEnabled"
+ "_smoothedCameraModel"
+ "_stabilizationSmoothingDisabled"
+ "pinholeCameraFocalLength > 0.0f"
+ "rollingShutterCompensationEnabled"
+ "setRollingShutterCompensationEnabled:"
+ "setStabilizationSmoothingDisabled:"
+ "stabilizationSmoothingDisabled"
+ "v220@0:8{RTSCameraSmoothingModel={?=}}16{?=[2]}48{RTSEllipse=}80f96{?=}100116{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}124"
+ "{?=[3]}168@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}72"
+ "{RTSCameraSmoothingModel={?=}}128@0:8{?=}16{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x94!"
- "-[RTSCRealTimeStabilization _clampStabilizedCameraToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]"
- "_clampStabilizedCameraToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:"
- "_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:computeAdjustment:"
- "_faceCorrectionUpdated"
- "_postStabilizationAdjustment"
- "_stabilizedCameraModel"
- "pinholeCameraFocalLength != 0.0f"
- "v188@0:8{?=[2]}16{RTSEllipse=}48f64{?=}6884{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}92"
- "{?=[3]}172@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}72B168"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb4!"

```
