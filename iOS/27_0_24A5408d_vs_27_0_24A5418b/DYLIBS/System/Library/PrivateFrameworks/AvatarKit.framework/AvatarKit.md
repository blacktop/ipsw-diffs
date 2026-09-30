## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

```diff

-367.0.0.0.0
-  __TEXT.__text: 0x77bb0
-  __TEXT.__objc_methlist: 0x54b4
-  __TEXT.__const: 0xa4c
-  __TEXT.__cstring: 0x1df64
+368.0.0.0.0
+  __TEXT.__text: 0x777d8
+  __TEXT.__objc_methlist: 0x54c4
+  __TEXT.__const: 0xb2c
+  __TEXT.__cstring: 0x1df4c
   __TEXT.__oslogstring: 0x2ec0
   __TEXT.__ustring: 0x66
-  __TEXT.__gcc_except_tab: 0xde4
-  __TEXT.__unwind_info: 0x1be0
+  __TEXT.__gcc_except_tab: 0xdd0
+  __TEXT.__unwind_info: 0x1bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2818
+  __DATA_CONST.__const: 0x27f0
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d78
+  __DATA_CONST.__objc_selrefs: 0x3d88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x625a8
-  __DATA_CONST.__got: 0x9e8
+  __DATA_CONST.__got: 0x9e0
   __AUTH_CONST.__const: 0xa40
   __AUTH_CONST.__cfstring: 0x249a0
-  __AUTH_CONST.__objc_const: 0xdd58
+  __AUTH_CONST.__objc_const: 0xdd48
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x7bd8
   __AUTH_CONST.__objc_doubleobj: 0x2370
   __AUTH_CONST.__objc_dictobj: 0x4ede0
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x1888
-  __DATA.__objc_ivar: 0xa54
+  __DATA.__objc_ivar: 0xa50
   __DATA.__data: 0x788
   __DATA.__bss: 0xab8
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2530
-  Symbols:   6294
-  CStrings:  5160
+  Functions: 2529
+  Symbols:   6290
+  CStrings:  5159
 
Symbols:
+ +[AVTFaceTrackingInfo dataWithARFrame:videoRotationAngle:]
+ +[AVTFaceTrackingInfo trackingInfoWithARFrame:worldAlignment:videoRotationAngle:]
+ +[AVTFaceTrackingInfo trackingInfoWithARFrame:worldAlignment:videoRotationAngle:constrainHeadPose:]
+ -[AVTARMaskRenderer updateWithARFrame:fallBackDepthData:videoRotationAngle:mirroredDepthData:]
+ -[AVTFaceTracker captureDevicePreviewLayer]
+ -[AVTFaceTracker session:didChangeViewRotationAngle:]
+ -[AVTFaceTracker setCaptureDevicePreviewLayer:]
+ -[AVTFaceTracker updateWithARFrame:videoRotationAngle:constrainHeadPose:mirroredDepthData:]
+ -[AVTFaceTracker updateWithARFrame:worldAlignment:fallBackDepthData:videoRotationAngle:constrainHeadPose:mirroredDepthData:]
+ -[AVTFaceTracker videoRotationAngle]
+ GCC_except_table115
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table82
+ GCC_except_table92
+ _OBJC_IVAR_$_AVTARMaskRenderer._indexedVideoRotationAngle
+ _OBJC_IVAR_$_AVTFaceTracker._captureDevicePreviewLayer
+ _OBJC_IVAR_$_AVTFaceTracker._indexedVideoRotationAngle
+ __AVTConvertARFaceAnchorTransformToVFXTransform
+ __AVTConvertARFaceAnchorTransformToVFXTransform.kAVTRotationMatrices
+ __AVTGetVideoRotationAngleFromCaptureOrientationAndInterfaceOrientation
+ __AVTGetVideoRotationAngleFromCaptureOrientationAndInterfaceOrientation.kIndexedRotationAngles
+ ___124-[AVTFaceTracker updateWithARFrame:worldAlignment:fallBackDepthData:videoRotationAngle:constrainHeadPose:mirroredDepthData:]_block_invoke
+ _kAVTCaptureDeviceTextureCoordinates
+ _objc_msgSend$setCaptureDevicePreviewLayer:
+ _objc_msgSend$setCullMode:
+ _objc_msgSend$setFrontFacingWinding:
+ _objc_msgSend$setViewLayer:
+ _objc_msgSend$trackingInfoWithARFrame:worldAlignment:videoRotationAngle:constrainHeadPose:
+ _objc_msgSend$updateWithARFrame:fallBackDepthData:videoRotationAngle:mirroredDepthData:
+ _objc_msgSend$updateWithARFrame:worldAlignment:fallBackDepthData:videoRotationAngle:constrainHeadPose:mirroredDepthData:
+ _objc_msgSend$videoRotationAngle
+ _projectionMatrixForViewportSize:zNear:zFar:.kRotationAngles
+ _session:didChangeViewRotationAngle:.kIndexedRotationAngles
+ _trackingInfoWithARFrame:inputOrientation:outputOrientation:constrainHeadPose:.kAVTInterfaceOrientationsToCaptureVideoOrientations
- +[AVTFaceTrackingInfo dataWithARFrame:captureOrientation:interfaceOrientation:]
- +[AVTFaceTrackingInfo trackingInfoWithARFrame:worldAlignment:captureOrientation:interfaceOrientation:]
- +[AVTFaceTrackingInfo trackingInfoWithARFrame:worldAlignment:captureOrientation:interfaceOrientation:constrainHeadPose:]
- -[AVTARMaskRenderer updateWithARFrame:fallBackDepthData:captureOrientation:interfaceOrientation:mirroredDepthData:]
- -[AVTARMaskRenderer updateWithDepthTexture:captureOrientation:interfaceOrientation:mirroredDepthData:]
- -[AVTFaceTracker captureVideoOrientation]
- -[AVTView _windowDidRotateNotification:]
- -[AVTView didMoveToWindow]
- GCC_except_table118
- GCC_except_table44
- GCC_except_table50
- GCC_except_table55
- GCC_except_table85
- GCC_except_table95
- _ARCameraToDisplayRotation
- _AVTARKitTransformToSceneKitTransformMatrix
- _AVTARKitTransformToSceneKitTransformMatrix.rotationMatrices
- _AVTSceneKitTextureCoordinatesForCaptureDeviceTexture
- _AVTVideoCaptureOrientationFromInterfaceOrientation.orientations
- _OBJC_IVAR_$_AVTARMaskRenderer._interfaceOrientation
- _OBJC_IVAR_$_AVTFaceTracker._captureVideoOrientation
- _OBJC_IVAR_$_AVTFaceTracker._interfaceOrientation
- _OBJC_IVAR_$_AVTView._windowDidRotateObserver
- _UIWindowDidRotateNotification
- ___112-[AVTFaceTracker updateWithARFrame:captureOrientation:interfaceOrientation:constrainHeadPose:mirroredDepthData:]_block_invoke
- ___145-[AVTFaceTracker updateWithARFrame:worldAlignment:fallBackDepthData:captureOrientation:interfaceOrientation:constrainHeadPose:mirroredDepthData:]_block_invoke
- ___26-[AVTView didMoveToWindow]_block_invoke
- ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
- __convertARFaceAnchorTransformToSceneKitTransform
- _objc_msgSend$_windowDidRotateNotification:
- _objc_msgSend$addObserverForName:object:queue:usingBlock:
- _objc_msgSend$captureVideoOrientation
- _objc_msgSend$interfaceOrientation
- _objc_msgSend$setInterfaceOrientation:
- _objc_msgSend$trackingInfoWithARFrame:worldAlignment:captureOrientation:interfaceOrientation:constrainHeadPose:
- _objc_msgSend$updateInterfaceOrientation
- _objc_msgSend$updateWithARFrame:fallBackDepthData:captureOrientation:interfaceOrientation:mirroredDepthData:
- _objc_msgSend$window
- _objc_msgSend$windowScene
CStrings:
- "v16@?0@\"NSNotification\"8"
```
