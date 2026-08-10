## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-446.11.0.0.0
-  __TEXT.__text: 0x5b654
-  __TEXT.__objc_methlist: 0x2394
-  __TEXT.__const: 0x7bc
-  __TEXT.__cstring: 0x4b56
+446.13.0.0.0
+  __TEXT.__text: 0x5b2dc
+  __TEXT.__objc_methlist: 0x23ec
+  __TEXT.__const: 0x744
+  __TEXT.__cstring: 0x4b5f
   __TEXT.__ustring: 0x1282
-  __TEXT.__gcc_except_tab: 0x8744
+  __TEXT.__gcc_except_tab: 0x8758
   __TEXT.__oslogstring: 0x3d6
   __TEXT.__unwind_info: 0x14f0
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xac8
+  __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2030
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x2078
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x3dc0
-  __DATA_CONST.__got: 0x5e0
+  __DATA_CONST.__got: 0x5a0
   __AUTH_CONST.__const: 0x9b0
   __AUTH_CONST.__cfstring: 0xfbe0
-  __AUTH_CONST.__objc_const: 0x3900
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
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1124
-  Symbols:   3297
-  CStrings:  2129
+  Functions: 1122
+  Symbols:   3288
+  CStrings:  2127
 
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
+ GCC_except_table109
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table149
+ GCC_except_table168
+ GCC_except_table174
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table203
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table369
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table99
+ _OBJC_CLASS_$_AVCaptureDeviceRotationCoordinator
+ _OBJC_IVAR_$_CRDefaultCaptureSessionManager._rotationCoordinator
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
- GCC_except_table103
- GCC_except_table110
- GCC_except_table114
- GCC_except_table117
- GCC_except_table129
- GCC_except_table131
- GCC_except_table134
- GCC_except_table142
- GCC_except_table150
- GCC_except_table169
- GCC_except_table175
- GCC_except_table185
- GCC_except_table188
- GCC_except_table191
- GCC_except_table194
- GCC_except_table196
- GCC_except_table198
- GCC_except_table206
- GCC_except_table207
- GCC_except_table31
- GCC_except_table34
- GCC_except_table362
- GCC_except_table365
- GCC_except_table368
- GCC_except_table40
- GCC_except_table42
- GCC_except_table52
- GCC_except_table65
- GCC_except_table70
- GCC_except_table71
- GCC_except_table77
- GCC_except_table78
- GCC_except_table96
- _CFDataGetBytePtr
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CGDataProviderCopyData
- _CGImageGetAlphaInfo
- _CGImageGetBitsPerPixel
- _CGImageGetBytesPerRow
- _CGImageGetDataProvider
- _CGImageGetHeight
- _CGImageGetWidth
- _CVPixelBufferCreate
- _IOServiceGetMatchingService
- _IOServiceMatching
- __ZL11setIntValueP14__CFDictionaryPK10__CFStringi
- __ZL6hasVXDv
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
- _kCVPixelBufferIOSurfacePropertiesKey
- _kIOMainPortDefault
- _kIOSurfaceAllocSize
- _kIOSurfaceBytesPerRow
- _kIOSurfaceCacheMode
- _kIOSurfaceHeight
- _kIOSurfaceMemoryRegion
- _kIOSurfacePixelFormat
- _kIOSurfaceWidth
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
+ "CoreRecognition: Unable to display camera view due to connection inturrupted notification %@"
+ "CoreRecognition: Unable to display camera view due to device in use by another client %@"
+ "CoreRecognition: Unable to display camera view due to device unavailable in the background %@"
+ "CoreRecognition: Unable to display camera view while running multiple foreground applications %@"
+ "videoRotationAngleForHorizonLevelPreview"
- "AppleVXD375"
- "AppleVXD390"
- "CoreRecogntion: Unable to display camera view due to connection inturrupted notification %@"
- "CoreRecogntion: Unable to display camera view due to device in use by another client %@"
- "CoreRecogntion: Unable to display camera view due to device unavailable in the background %@"
- "CoreRecogntion: Unable to display camera view while running multiple foreground applications %@"
- "PurpleGfxMem"
```
