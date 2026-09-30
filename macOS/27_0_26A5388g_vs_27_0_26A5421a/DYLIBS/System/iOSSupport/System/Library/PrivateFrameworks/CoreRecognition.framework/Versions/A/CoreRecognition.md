## CoreRecognition

> `/System/iOSSupport/System/Library/PrivateFrameworks/CoreRecognition.framework/Versions/A/CoreRecognition`

```diff

-446.11.0.0.0
-  __TEXT.__text: 0x55a90
-  __TEXT.__objc_methlist: 0x2384
-  __TEXT.__const: 0x7c4
-  __TEXT.__cstring: 0x3748
+446.13.0.0.0
+  __TEXT.__text: 0x55914
+  __TEXT.__objc_methlist: 0x23d4
+  __TEXT.__const: 0x74c
+  __TEXT.__cstring: 0x3772
   __TEXT.__ustring: 0x1282
-  __TEXT.__gcc_except_tab: 0x85a4
+  __TEXT.__gcc_except_tab: 0x85b8
   __TEXT.__oslogstring: 0x3d6
-  __TEXT.__unwind_info: 0x14c0
+  __TEXT.__unwind_info: 0x14c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__const: 0xa88
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc0
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x2008
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x3dc0
-  __DATA_CONST.__got: 0x580
+  __DATA_CONST.__got: 0x588
   __AUTH_CONST.__const: 0x9b0
-  __AUTH_CONST.__cfstring: 0xfae0
-  __AUTH_CONST.__objc_const: 0x3900
+  __AUTH_CONST.__cfstring: 0xfb00
+  __AUTH_CONST.__objc_const: 0x3938
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x90

   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_ivar: 0x2cc
   __DATA.__data: 0x240
   __DATA.__bss: 0x90
   __DATA.__common: 0x60

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1116
-  Symbols:   3252
-  CStrings:  2105
+  Symbols:   3259
+  CStrings:  2106
 
Symbols:
+ +[CRCameraReader boundsForPaddedCornersOfBoundingBox:padding:topLeft:topRight:bottomRight:bottomLeft:]
+ +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:inputImage:]
+ +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:inputImage:]
+ +[CRCameraReader inputOrientationForCaptureAngle:]
+ -[CRCameraReader findIDObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]
+ -[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]
+ -[CRDefaultCaptureSessionManager captureBufferRotationAngle]
+ -[CRDefaultCaptureSessionManager dealloc]
+ -[CRDefaultCaptureSessionManager observeValueForKeyPath:ofObject:change:context:]
+ -[CRDefaultCaptureSessionManager rotationCoordinator]
+ -[CRDefaultCaptureSessionManager setRotationCoordinator:]
+ -[CRDefaultCaptureSessionManager setupRotationCoordinatorForDevice:]
+ -[CRDefaultCaptureSessionManager teardownRotationCoordinator]
+ -[CRDefaultCaptureSessionManager updatePreviewRotationFromCoordinator]
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table146
+ GCC_except_table165
+ GCC_except_table171
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table200
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table360
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table41
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table96
+ OBJC_IVAR_$_CRDefaultCaptureSessionManager._rotationCoordinator
+ _OBJC_CLASS_$_AVCaptureDeviceRotationCoordinator
+ __Z10ccCardRectf
+ __Z18ccUnitRectToMMRect6CGRect
+ __Z18isLeastBlurryFrameP7CIImageP14NSMutableArrayi
+ __Z27ccArea1RectScaleIndependentv
+ __Z27ccArea2RectScaleIndependentv
+ __Z28ccUnitRectToMMRectIsPortrait6CGRectb
+ __ZL24CRCameraReaderFrameImageP10__CVBufferPK14__CFDictionary
+ ___26-[CRCameraReader loadView]_block_invoke_3
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_10
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_11
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_12
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_13
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_14
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_15
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_17
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_2
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_3
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_4
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_5
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_6
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_7
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_8
+ ___85-[CRCameraReader findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:]_block_invoke_9
+ ___block_descriptor_56_ea8_32s40s48s_e42_v48?0^{__CVBuffer=}8"NSData"16{?=qiIq}24ls32l8s40l8s48l8
+ _kCRPreviewRotationContext
+ _objc_msgSend$captureBufferRotationAngle
+ _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:inputImage:
+ _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:inputImage:
+ _objc_msgSend$findIDObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:
+ _objc_msgSend$findObjects:inPixelBuffer:frameImage:cameraIntrinsicData:frameTime:
+ _objc_msgSend$initWithDevice:previewLayer:
+ _objc_msgSend$inputOrientationForCaptureAngle:
+ _objc_msgSend$isVideoRotationAngleSupported:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$rotationCoordinator
+ _objc_msgSend$setRotationCoordinator:
+ _objc_msgSend$setVideoRotationAngle:
+ _objc_msgSend$setupRotationCoordinatorForDevice:
+ _objc_msgSend$teardownRotationCoordinator
+ _objc_msgSend$updatePreviewRotationFromCoordinator
+ _objc_msgSend$videoRotationAngle
+ _objc_msgSend$videoRotationAngleForHorizonLevelCapture
+ _objc_msgSend$videoRotationAngleForHorizonLevelPreview
+ _objc_release_x2
- +[ActivationMapTools colInImage:forPoint:inActivationMapWithSize:]
- +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:cameraIntrinsicData:]
- +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:]
- +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:]
- +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:]
- -[CRCameraReader aetPlacementTextColor:]
- -[CRCameraReader findIDObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]
- -[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]
- GCC_except_table100
- GCC_except_table107
- GCC_except_table111
- GCC_except_table114
- GCC_except_table126
- GCC_except_table128
- GCC_except_table131
- GCC_except_table134
- GCC_except_table139
- GCC_except_table147
- GCC_except_table166
- GCC_except_table172
- GCC_except_table182
- GCC_except_table185
- GCC_except_table188
- GCC_except_table191
- GCC_except_table193
- GCC_except_table195
- GCC_except_table203
- GCC_except_table204
- GCC_except_table31
- GCC_except_table34
- GCC_except_table359
- GCC_except_table362
- GCC_except_table365
- GCC_except_table40
- GCC_except_table42
- GCC_except_table52
- GCC_except_table60
- GCC_except_table65
- GCC_except_table70
- GCC_except_table71
- _CFDataGetBytePtr
- _CGDataProviderCopyData
- _CGImageGetAlphaInfo
- _CGImageGetBitsPerPixel
- _CGImageGetBytesPerRow
- _CGImageGetDataProvider
- _CGImageGetHeight
- _CGImageGetWidth
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_10
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_11
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_12
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_13
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_14
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_15
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_17
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_2
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_3
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_4
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_5
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_6
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_7
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_8
- ___74-[CRCameraReader findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:]_block_invoke_9
- ___block_descriptor_48_ea8_32s40s_e42_v48?0^{__CVBuffer=}8"NSData"16{?=qiIq}24ls32l8s40l8
- _allocatePixel8Buffer
- _calculateImageBlur
- _ccArea1Rect
- _ccArea1RectScaleIndependent
- _ccArea2Rect
- _ccArea2RectScaleIndependent
- _ccCardRect
- _ccMMRectToUnitRect
- _ccMMRectToUnitRectIsPortait
- _ccUnitRectToMMRect
- _ccUnitRectToMMRectIsPortrait
- _createPlanar420PixelBufferFromImageFile
- _isLeastBlurryFrame
- _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:
- _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:
- _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:
- _objc_msgSend$findIDObjects:inPixelBuffer:cameraIntrinsicData:frameTime:
- _objc_msgSend$findObjects:inPixelBuffer:cameraIntrinsicData:frameTime:
- _objc_msgSend$setVideoOrientation:
- _objc_msgSend$videoOrientation
- _rotateBuffer180
- _vImageRotate90_Planar8
CStrings:
+ "videoRotationAngleForHorizonLevelPreview"
```
