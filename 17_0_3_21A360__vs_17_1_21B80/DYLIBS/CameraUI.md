## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4002.113.5.0.0
-  __TEXT.__text: 0x1da124
+4005.6.0.0.0
+  __TEXT.__text: 0x1da320
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x14f68
+  __TEXT.__objc_methlist: 0x14f98
   __TEXT.__const: 0x2d70
-  __TEXT.__gcc_except_tab: 0x23c4
-  __TEXT.__cstring: 0x12409
+  __TEXT.__gcc_except_tab: 0x23b8
+  __TEXT.__cstring: 0x1248f
   __TEXT.__oslogstring: 0x11cbf
   __TEXT.__dlopen_cstrs: 0x310
   __TEXT.__ustring: 0x8
-  __TEXT.__objc_const_ax: 0xe6e8
-  __TEXT.__unwind_info: 0x83d4
+  __TEXT.__objc_const_ax: 0xe6f8
+  __TEXT.__unwind_info: 0x83c0
   __TEXT.__objc_classname: 0x4994
-  __TEXT.__objc_methname: 0x7e937
+  __TEXT.__objc_methname: 0x7ea29
   __TEXT.__objc_methtype: 0xd697
-  __TEXT.__objc_stubs: 0x492c0
-  __DATA_CONST.__got: 0x1158
+  __TEXT.__objc_stubs: 0x49340
+  __DATA_CONST.__got: 0x1160
   __DATA_CONST.__const: 0x6128
   __DATA_CONST.__objc_classlist: 0xea8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x5d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3afe8
-  __DATA_CONST.__objc_selrefs: 0x14368
+  __DATA_CONST.__objc_const: 0x3b048
+  __DATA_CONST.__objc_selrefs: 0x14388
   __DATA_CONST.__objc_arraydata: 0xcf0
-  __AUTH_CONST.__cfstring: 0x12720
+  __AUTH_CONST.__cfstring: 0x127a0
   __AUTH_CONST.__objc_const: 0x9e60
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_doubleobj: 0x500

   __DATA.__objc_protorefs: 0x68
   __DATA.__objc_classrefs: 0x1670
   __DATA.__objc_superrefs: 0xc50
-  __DATA.__objc_ivar: 0x3118
+  __DATA.__objc_ivar: 0x3120
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x46b8
   __DATA.__bss: 0x208

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13672
-  Symbols:   46641
-  CStrings:  22255
+  Functions: 13676
+  Symbols:   46656
+  CStrings:  22268
 
Symbols:
+ -[CAMCaptureCapabilities _allowSpatialOverCaptureInPortraitMode]
+ -[CAMCaptureCapabilities _isSpatialOverCaptureSupportedForDevice:]
+ -[CAMCaptureCapabilities spatialOverCaptureSupportForMode:device:]
+ -[CAMImageWell _setThumbnailUpdateID:]
+ -[CAMImageWell _thumbnailUpdateID]
+ -[CAMSystemPressureState isCameraTooHot]
+ -[CAMZoomControl gestureRecognizerShouldBegin:]
+ GCC_except_table127
+ GCC_except_table138
+ _AVCaptureSystemPressureLevelShutdown
+ _OBJC_IVAR_$_CAMCaptureCapabilities.__allowSpatialOverCaptureInPortraitMode
+ _OBJC_IVAR_$_CAMImageWell.__thumbnailUpdateID
+ ___block_descriptor_56_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ __unnamed_array_storage.100
+ __unnamed_array_storage.130
+ __unnamed_array_storage.329
+ __unnamed_array_storage.335
+ __unnamed_array_storage.355
+ __unnamed_array_storage.359
+ __unnamed_array_storage.383
+ __unnamed_array_storage.388
+ __unnamed_array_storage.393
+ __unnamed_array_storage.437
+ _objc_msgSend$_allowSpatialOverCaptureInPortraitMode
+ _objc_msgSend$_isSpatialOverCaptureSupportedForDevice:
+ _objc_msgSend$_setThumbnailUpdateID:
+ _objc_msgSend$_thumbnailUpdateID
+ _objc_msgSend$isCameraTooHot
+ _objc_msgSend$level
+ _objc_msgSend$spatialOverCaptureSupportForMode:device:
- -[CAMCaptureCapabilities isSpatialOverCapturePreviewSupportedForMode:device:]
- -[CAMSystemPressureState hasCameraTemperatureFactor]
- GCC_except_table126
- GCC_except_table137
- ___62-[CAMCameraRollController _setExternalStorageBrowsingSession:]_block_invoke_2
- ___block_descriptor_40_e8_32w_e32_v32?0"UIImage"8"NSError"16q24lw32l8
- __unnamed_array_storage.118
- __unnamed_array_storage.326
- __unnamed_array_storage.332
- __unnamed_array_storage.337
- __unnamed_array_storage.356
- __unnamed_array_storage.374
- __unnamed_array_storage.385
- __unnamed_array_storage.390
- __unnamed_array_storage.422
- __unnamed_array_storage.97
- _objc_msgSend$hasCameraTemperatureFactor
- _objc_msgSend$isSpatialOverCapturePreviewSupportedForMode:device:
- _objc_msgSend$requestImageForStartingAssetFillingTargetSize:resultHandler:
CStrings:
+ "CAMFeatureDevelopmentAllowSpatialOverCaptureInPortraitMode"
+ "PPTPresentCameraRollDelayMilliseconds"
+ "TB,R,N,GisCameraTooHot"
+ "TB,R,N,V__allowSpatialOverCaptureInPortraitMode"
+ "TQ,N,S_setThumbnailUpdateID:,V__thumbnailUpdateID"
+ "_UISheetInteractionBackgroundDismissRecognizer"
+ "__allowSpatialOverCaptureInPortraitMode"
+ "__thumbnailUpdateID"
+ "_allowSpatialOverCaptureInPortraitMode"
+ "_isSpatialOverCaptureSupportedForDevice:"
+ "_setThumbnailUpdateID:"
+ "_thumbnailUpdateID"
+ "cameraTooHot"
+ "isCameraTooHot"
+ "level"
+ "presentCameraRollDelay"
+ "spatialOverCaptureSupportForMode:device:"
- "hasCameraTemperatureFactor"
- "isSpatialOverCapturePreviewSupportedForMode:device:"
- "requestImageForStartingAssetFillingTargetSize:resultHandler:"
- "v32@?0@\"UIImage\"8@\"NSError\"16q24"

```
