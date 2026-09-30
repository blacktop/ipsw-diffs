## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

 664.2.10.0.0
-  __TEXT.__text: 0x39dbc
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_stubs: 0x2e80
-  __TEXT.__objc_methlist: 0x191c
-  __TEXT.__objc_classname: 0x1d4
-  __TEXT.__objc_methname: 0x50d1
-  __TEXT.__objc_methtype: 0x14ae
-  __TEXT.__cstring: 0x4920
-  __TEXT.__const: 0x670
+  __TEXT.__text: 0x3c4e4
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x30e0
+  __TEXT.__objc_methlist: 0x1b04
+  __TEXT.__const: 0x6c0
+  __TEXT.__objc_methname: 0x58ba
+  __TEXT.__objc_classname: 0x226
+  __TEXT.__objc_methtype: 0x17b7
+  __TEXT.__cstring: 0x4b96
   __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__unwind_info: 0x700
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x7f8
+  __TEXT.__unwind_info: 0x780
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x858
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0x900
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x858
   __DATA_CONST.__objc_arraydata: 0x2760
   __DATA_CONST.__objc_dictobj: 0x988
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x3de8
-  __DATA.__objc_selrefs: 0xeb0
-  __DATA.__objc_ivar: 0x438
-  __DATA.__objc_data: 0x460
+  __DATA.__objc_const: 0x4390
+  __DATA.__objc_selrefs: 0xf78
+  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_data: 0x550
   __DATA.__data: 0x300
   __DATA.__bss: 0x2c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8AB74D0-C4E0-3E4D-890B-12D03A06B77D
-  Functions: 1144
-  Symbols:   2469
-  CStrings:  1697
+  UUID: 12A98600-C20B-3DEF-9A0F-48880AEF8B92
+  Functions: 1197
+  Symbols:   2599
+  CStrings:  1787
 
Symbols:
+ -[GVSFacePosePreprocessor init]
+ -[GVSFacePosePreprocessor reset]
+ -[GVSFacePosePreprocessor updateWithFacePose:faceIdentifier:]
+ -[GVSFaceSelectionProcessor _computeFaceRectangleScore:finalCropRect:imageCenterNormalized:]
+ -[GVSFaceSelectionProcessor faceIdentifier]
+ -[GVSFaceSelectionProcessor faceRectangle]
+ -[GVSFaceSelectionProcessor init]
+ -[GVSFaceSelectionProcessor reset]
+ -[GVSFaceSelectionProcessor updateFaceSelectionWithFaceDetections:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:]
+ -[GVSFaceStabilizationProcessor .cxx_destruct]
+ -[GVSFaceStabilizationProcessor _convertFaceRectangleToFacePose:withCameraPose:focalLength:imageCenter:]
+ -[GVSFaceStabilizationProcessor dealloc]
+ -[GVSFaceStabilizationProcessor faceCorrection]
+ -[GVSFaceStabilizationProcessor facePose]
+ -[GVSFaceStabilizationProcessor init]
+ -[GVSFaceStabilizationProcessor init].cold.1
+ -[GVSFaceStabilizationProcessor init].cold.2
+ -[GVSFaceStabilizationProcessor reset]
+ -[GVSFaceStabilizationProcessor setFaceCorrection:]
+ -[GVSFaceStabilizationProcessor updateBiasTrackingAndFaceCorrectionQuaternionWithFaceSmoothingArrays:biasTrackingSigma:centerFrameOffset:]
+ -[GVSFaceStabilizationProcessor updateFaceCorrectionStrengthWithFaceSmoothingArrays:]
+ -[GVSFaceStabilizationProcessor updateFaceFilteredQuaternionsWithFaceSmoothingArrays:faceFilteringSigma:centerFrameOffset:]
+ -[GVSFaceStabilizationProcessor updateFacePoseWithFaceDetections:cameraPose:focalLength:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:]
+ -[GVSSmoothingBuffers _allocateBuffersWithOptions:].cold.20
+ -[GVSSmoothingBuffers _allocateBuffersWithOptions:].cold.21
+ -[GVSSmoothingBuffers faceStabilizationDataInput]
+ -[GVSSmoothingBuffers getFaceSmoothingArrays]
+ -[GVSSmoothingBuffers rotationRateInput]
+ -[GVSSmoothingBuffers setFaceStabilizationDataInput:]
+ -[GVSSmoothingBuffers setRotationRateInput:]
+ -[VISConfigurationV2 faceStabilizationEnabled]
+ -[VISConfigurationV2 faceStabilizationSigmaMultiplierForBiasTracking]
+ -[VISConfigurationV2 faceStabilizationSigmaMultiplierForFaceFiltering]
+ -[VISConfigurationV2 setFaceStabilizationEnabled:]
+ -[VISConfigurationV2 setFaceStabilizationSigmaMultiplierForBiasTracking:]
+ -[VISConfigurationV2 setFaceStabilizationSigmaMultiplierForFaceFiltering:]
+ FigSampleBufferProcessorCreateForGyroVideoStabilization.cold.69
+ GVSComputeSmoothedFaceQuaternion.cold.1
+ GVSComputeSmoothedFaceQuaternion.cold.2
+ GVSConfineRectToCircle.cold.1
+ GVSConfineRectToCircle.cold.2
+ GVSConfineRectToCircle.cold.3
+ GVSExtractMetadataFromTopToBottomRows.cold.18
+ GVSExtractMetadataFromTopToBottomRows.cold.19
+ GVSExtractMetadataFromTopToBottomRows.cold.20
+ GVSExtractMetadataFromTopToBottomRows.cold.21
+ GVSExtractMetadataFromTopToBottomRows.cold.22
+ OBJC_IVAR_$_GVSFacePosePreprocessor._integratedFacePose
+ OBJC_IVAR_$_GVSFacePosePreprocessor._previousFaceIdentifier
+ OBJC_IVAR_$_GVSFacePosePreprocessor._previousFacePose
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._faceIdentifier
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._faceLatestActiveTime
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._faceRectangle
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._minScoreForEntry
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._minScoreForTracking
+ OBJC_IVAR_$_GVSFaceSelectionProcessor._waitTimeForExit
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._enableFaceStrengthModulation
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._faceCorrection
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._facePose
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._facePosePreprocessor
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._faceSelectionProcessor
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._maximumStrengthSlope
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._rotationRateForFullStrength
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._rotationRateForZeroStrength
+ OBJC_IVAR_$_GVSFaceStabilizationProcessor._tripodRotationRateThreshold
+ OBJC_IVAR_$_GVSSmoothingBuffers._faceStabilizationData
+ OBJC_IVAR_$_GVSSmoothingBuffers._rotationRate
+ OBJC_IVAR_$_VISConfigurationV2._faceStabilizationEnabled
+ OBJC_IVAR_$_VISConfigurationV2._faceStabilizationSigmaMultiplierForBiasTracking
+ OBJC_IVAR_$_VISConfigurationV2._faceStabilizationSigmaMultiplierForFaceFiltering
+ _CGRectContainsRect
+ _FigCFDictionaryGetCGPointIfPresent
+ _FigCFDictionaryGetCGSizeIfPresent
+ _GVSApplyFaceCorrectionQuaternionToStabilizedQuaternion
+ _GVSComputeSmoothedFaceQuaternion
+ _GVSConfineRectToCircle
+ _GVSDenormalizeRectangle
+ _GVSInterpolateQuatfLERP
+ _GVSQuatfFromDeltaRotation
+ _OBJC_CLASS_$_GVSFacePosePreprocessor
+ _OBJC_CLASS_$_GVSFaceSelectionProcessor
+ _OBJC_CLASS_$_GVSFaceStabilizationProcessor
+ _OBJC_METACLASS_$_GVSFacePosePreprocessor
+ _OBJC_METACLASS_$_GVSFaceSelectionProcessor
+ _OBJC_METACLASS_$_GVSFaceStabilizationProcessor
+ __OBJC_$_INSTANCE_METHODS_GVSFacePosePreprocessor
+ __OBJC_$_INSTANCE_METHODS_GVSFaceSelectionProcessor
+ __OBJC_$_INSTANCE_METHODS_GVSFaceStabilizationProcessor
+ __OBJC_$_INSTANCE_VARIABLES_GVSFacePosePreprocessor
+ __OBJC_$_INSTANCE_VARIABLES_GVSFaceSelectionProcessor
+ __OBJC_$_INSTANCE_VARIABLES_GVSFaceStabilizationProcessor
+ __OBJC_$_PROP_LIST_GVSFaceSelectionProcessor
+ __OBJC_$_PROP_LIST_GVSFaceStabilizationProcessor
+ __OBJC_CLASS_RO_$_GVSFacePosePreprocessor
+ __OBJC_CLASS_RO_$_GVSFaceSelectionProcessor
+ __OBJC_CLASS_RO_$_GVSFaceStabilizationProcessor
+ __OBJC_METACLASS_RO_$_GVSFacePosePreprocessor
+ __OBJC_METACLASS_RO_$_GVSFaceSelectionProcessor
+ __OBJC_METACLASS_RO_$_GVSFaceStabilizationProcessor
+ _kFigCaptureSampleBufferMetadata_FinalCropRect
+ _kFigCaptureSampleBufferMetadata_ImageCircle
+ _kFigCaptureSampleBufferMetadata_ImageCircleKey_Center
+ _kFigCaptureSampleBufferMetadata_ImageCircleKey_Radius
+ _kFigCaptureStreamDetectedObjectsInfoKey_HumanFaces
+ _kFigCaptureStreamDetectedObjectsKey_ObjectsArray
+ _kFigCaptureStreamMetadata_DetectedObjectsInfo
+ _kFigCaptureStreamMetadata_FaceID
+ _kFigCaptureStreamMetadata_Rect
+ _kFigVideoStabilizationSampleBufferProcessorOption_FaceStabilizationEnabled
+ _kFigVideoStabilizationSampleBufferProcessorOption_FaceStabilizationSigmaMultiplierForBiasTracking
+ _kFigVideoStabilizationSampleBufferProcessorOption_FaceStabilizationSigmaMultiplierForFaceFiltering
+ _objc_msgSend$_computeFaceRectangleScore:finalCropRect:imageCenterNormalized:
+ _objc_msgSend$_convertFaceRectangleToFacePose:withCameraPose:focalLength:imageCenter:
+ _objc_msgSend$faceCorrection
+ _objc_msgSend$faceIdentifier
+ _objc_msgSend$facePose
+ _objc_msgSend$faceRectangle
+ _objc_msgSend$faceStabilizationEnabled
+ _objc_msgSend$faceStabilizationSigmaMultiplierForBiasTracking
+ _objc_msgSend$faceStabilizationSigmaMultiplierForFaceFiltering
+ _objc_msgSend$getDefaultProcessorConfigurationForStreamingSquareAspectRatio
+ _objc_msgSend$getFaceSmoothingArrays
+ _objc_msgSend$setFaceStabilizationDataInput:
+ _objc_msgSend$setRotationRateInput:
+ _objc_msgSend$updateBiasTrackingAndFaceCorrectionQuaternionWithFaceSmoothingArrays:biasTrackingSigma:centerFrameOffset:
+ _objc_msgSend$updateFaceCorrectionStrengthWithFaceSmoothingArrays:
+ _objc_msgSend$updateFaceFilteredQuaternionsWithFaceSmoothingArrays:faceFilteringSigma:centerFrameOffset:
+ _objc_msgSend$updateFacePoseWithFaceDetections:cameraPose:focalLength:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:
+ _objc_msgSend$updateFaceSelectionWithFaceDetections:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:
+ _objc_msgSend$updateWithFacePose:faceIdentifier:
- _objc_retain_x28
CStrings:
+ "@\"GVSFacePosePreprocessor\""
+ "@\"GVSFaceSelectionProcessor\""
+ "B32@0:8^{GVSFaceSmoothingArrays=^{GVSFaceStabilizationData}^f^d^fiiiii}16f24i28"
+ "FigCFDictionaryGetCGPointIfPresent( imageCircleDict, kFigCaptureSampleBufferMetadata_ImageCircleKey_Center, &center )"
+ "FigCFDictionaryGetCGSizeIfPresent( imageCircleDict, kFigCaptureSampleBufferMetadata_ImageCircleKey_Radius, &radius )"
+ "GVSFacePosePreprocessor"
+ "GVSFaceSelectionProcessor"
+ "GVSFaceStabilizationProcessor"
+ "GVSFaceStabilizationUtilities.m"
+ "GVSGetImageCircleIfPresent( metadataDict, transformContext->width, transformContext->height, &imageCircle )"
+ "TB,N,V_faceStabilizationEnabled"
+ "Tf,N,V_faceStabilizationSigmaMultiplierForBiasTracking"
+ "Tf,N,V_faceStabilizationSigmaMultiplierForFaceFiltering"
+ "Ti,R,N,V_faceIdentifier"
+ "T{?=},N,V_faceCorrection"
+ "T{?=},R,N,V_facePose"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_faceRectangle"
+ "T{GVSFaceStabilizationData={?=}{?=}f},N"
+ "^{GVSFaceStabilizationData={?=}{?=}f}"
+ "_computeFaceRectangleScore:finalCropRect:imageCenterNormalized:"
+ "_convertFaceRectangleToFacePose:withCameraPose:focalLength:imageCenter:"
+ "_enableFaceStrengthModulation"
+ "_faceCorrection"
+ "_faceIdentifier"
+ "_faceLatestActiveTime"
+ "_facePose"
+ "_facePosePreprocessor"
+ "_faceRectangle"
+ "_faceSelectionProcessor"
+ "_faceStabilizationData"
+ "_faceStabilizationEnabled"
+ "_faceStabilizationSigmaMultiplierForBiasTracking"
+ "_faceStabilizationSigmaMultiplierForFaceFiltering"
+ "_integratedFacePose"
+ "_maximumStrengthSlope"
+ "_minScoreForEntry"
+ "_minScoreForTracking"
+ "_previousFaceIdentifier"
+ "_previousFacePose"
+ "_rotationRate"
+ "_rotationRateForFullStrength"
+ "_rotationRateForZeroStrength"
+ "_tripodRotationRateThreshold"
+ "_waitTimeForExit"
+ "f88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}4880"
+ "faceCorrection"
+ "faceIdentifier"
+ "facePose"
+ "faceRectangle"
+ "faceSmoothingArrays->count >= 2"
+ "faceStabilizationDataInput"
+ "faceStabilizationEnabled"
+ "faceStabilizationSigmaMultiplierForBiasTracking"
+ "faceStabilizationSigmaMultiplierForFaceFiltering"
+ "getDefaultProcessorConfigurationForStreamingSquareAspectRatio"
+ "getFaceSmoothingArrays"
+ "imageCircleDict"
+ "rad > 0.f"
+ "rad > minX"
+ "rad > minY"
+ "rotationRateInput"
+ "setFaceCorrection:"
+ "setFaceStabilizationDataInput:"
+ "setFaceStabilizationEnabled:"
+ "setFaceStabilizationSigmaMultiplierForBiasTracking:"
+ "setFaceStabilizationSigmaMultiplierForFaceFiltering:"
+ "setRotationRateInput:"
+ "smartStyle.video.reversibilityUses3x4Spotlights"
+ "storage->faceStabilizationContext.processor"
+ "updateBiasTrackingAndFaceCorrectionQuaternionWithFaceSmoothingArrays:biasTrackingSigma:centerFrameOffset:"
+ "updateFaceCorrectionStrengthWithFaceSmoothingArrays:"
+ "updateFaceFilteredQuaternionsWithFaceSmoothingArrays:faceFilteringSigma:centerFrameOffset:"
+ "updateFacePoseWithFaceDetections:cameraPose:focalLength:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:"
+ "updateFaceSelectionWithFaceDetections:imageCenter:sourcePixelBufferDimensions:finalCropRect:currentCaptureTime:"
+ "updateWithFacePose:faceIdentifier:"
+ "v116@0:8@16{?=dddd}24f566068{CGRect={CGPoint=dd}{CGSize=dd}}76d108"
+ "v24@0:8^{GVSFaceSmoothingArrays=^{GVSFaceStabilizationData}^f^d^fiiiii}16"
+ "v32@0:8^{GVSFaceSmoothingArrays=^{GVSFaceStabilizationData}^f^d^fiiiii}16f24i28"
+ "v64@0:8{GVSFaceStabilizationData={?=}{?=}f}16"
+ "v80@0:8@162432{CGRect={CGPoint=dd}{CGSize=dd}}40d72"
+ "{?=\"vector\"}"
+ "{?=}36@0:8{?=}16i32"
+ "{?=}92@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{?=dddd}48f8084"
+ "{GVSFaceSmoothingArrays=^{GVSFaceStabilizationData}^f^d^fiiiii}16@0:8"
+ "{GVSFaceStabilizationData={?=}{?=}f}16@0:8"

```
