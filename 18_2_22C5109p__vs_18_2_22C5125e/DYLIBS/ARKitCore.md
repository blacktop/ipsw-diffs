## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-631.5.5.1.0
-  __TEXT.__text: 0x172e54
-  __TEXT.__auth_stubs: 0x3c60
-  __TEXT.__objc_methlist: 0xf4a0
+631.5.7.0.0
+  __TEXT.__text: 0x173a88
+  __TEXT.__auth_stubs: 0x3c70
+  __TEXT.__objc_methlist: 0xf4e8
   __TEXT.__const: 0x2e464
-  __TEXT.__gcc_except_tab: 0x12bfc
-  __TEXT.__oslogstring: 0x13458
-  __TEXT.__cstring: 0x1d24e
+  __TEXT.__gcc_except_tab: 0x12c84
+  __TEXT.__oslogstring: 0x13735
+  __TEXT.__cstring: 0x1d316
   __TEXT.__ustring: 0x140
-  __TEXT.__unwind_info: 0x6098
+  __TEXT.__unwind_info: 0x5f98
   __TEXT.__objc_classname: 0x1eac
-  __TEXT.__objc_methname: 0x2862d
-  __TEXT.__objc_methtype: 0xc1d2
-  __TEXT.__objc_stubs: 0x19be0
-  __DATA_CONST.__got: 0x15e8
-  __DATA_CONST.__const: 0x35d0
+  __TEXT.__objc_methname: 0x287bd
+  __TEXT.__objc_methtype: 0xc1da
+  __TEXT.__objc_stubs: 0x19c20
+  __DATA_CONST.__got: 0x1610
+  __DATA_CONST.__const: 0x35e8
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7700
+  __DATA_CONST.__objc_selrefs: 0x7720
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x758
   __DATA_CONST.__objc_arraydata: 0x830
-  __AUTH_CONST.__auth_got: 0x1e48
+  __AUTH_CONST.__auth_got: 0x1e50
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x2fd8
-  __AUTH_CONST.__cfstring: 0xfe40
-  __AUTH_CONST.__objc_const: 0x3c940
+  __AUTH_CONST.__cfstring: 0xfe80
+  __AUTH_CONST.__objc_const: 0x3c9f0
   __AUTH_CONST.__objc_intobj: 0x3180
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x33e0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1e74
+  __DATA.__objc_ivar: 0x1e84
   __DATA.__data: 0x19f8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x17d0
+  __DATA.__bss: 0x17c0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1d60
   __DATA_DIRTY.__bss: 0x471

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 7024
-  Symbols:   9781
-  CStrings:  11414
+  Functions: 7033
+  Symbols:   9798
+  CStrings:  11433
 
Symbols:
+ _ARCaptureLensFromMakerNotesDictionary
+ _ARCreateFixedPriorityDispatchQueueWithPropagatedQOS
+ _ARWorldTrackingPushVisionDataIntrinsicsDefaultsKey
+ _ARWorldTrackingUseFullResolutionVisionDataIntrinsicsDefaultsKey
+ _ARWorldTrackingUsePerFrameCameraIntrinsicsForBravoDefaultsKey
+ _AVCaptureDeviceTypeBuiltInDualCamera
+ _CV3DSLAMCalibrationForceToUsePerFrameCameraIntrinsics
+ _CV3DSLAMCameraFrameAddHWFPWithIntrinsics
+ _kCGImagePropertyExifDictionary
+ _kCGImagePropertyMakerAppleDictionary
+ _kCGImagePropertyTIFFDictionary
+ _kFigAppleMakerNote_Camera
- _CV3DSLAMCameraFrameAddHWFP
CStrings:
+ "%!{(MISSING)public}@ <%!p(MISSING)>: Clearing relocalization after sensor data drop as SLAM is nominal again."
+ "%!{(MISSING)public}@ <%!p(MISSING)>: Configured SLAM calibration to use per-frame camera intrinsics."
+ "%!{(MISSING)public}@ <%!p(MISSING)>: Disabled per-frame camera intrinsics through user defaults."
+ "%!{(MISSING)public}@ <%!p(MISSING)>: Error configuring SLAM calibration to use per-frame camera intrinsics: %!@(MISSING)"
+ "%!{(MISSING)public}@ <%!p(MISSING)>: Not setting ARRelocalizationStateRelocalizingAfterSensorDataDrop, because we're already in state: %!l(MISSING)u"
+ "%!{(MISSING)public}@ <%!p(MISSING)>: World tracking will %!@(MISSING)push scale vision intrinsics for full resolution"
+ "%!{(MISSING)public}@ <%!p(MISSING)>: World tracking will %!@(MISSING)push vision data intrinsics"
+ "@144@0:8^{__CVBuffer=}16q24@32@40{?=qiIq}48{?=[3]}72@120@128Q136"
+ "@176@0:8{?=[3]}16{CGSize=dd}64q80Q8896128d144@152@160Q168"
+ "Could not retrieve MakerNotes dictionary from metadata."
+ "Could not retrieve lens information from MakerNotes dictionary."
+ "TB,N,V_dropInitialFramesOutsideExposureTarget"
+ "VisionDataCameraIntrinsicMatrix"
+ "_dropInitialFramesOutsideExposureTarget"
+ "_shouldPushVisionDataIntrinsics"
+ "_shouldUseFullResolutionVisionDataIntrinsics"
+ "com.apple.arkit.worldtracking.pushVisionDataIntrinsics"
+ "com.apple.arkit.worldtracking.useFullResolutionVisionDataIntrinsics"
+ "com.apple.arkit.worldtracking.usePerFrameCameraIntrinsicsForBravo"
+ "dropInitialFramesOutsideExposureTarget"
+ "initWithIntrinsics:imageResolution:devicePosition:lensType:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:"
+ "initWithPixelBuffer:captureFramePerSecond:captureDevice:captureSession:timestamp:intrinsics:exif:tiff:captureLens:"
+ "isBravoCameraEnabled"
+ "setDropInitialFramesOutsideExposureTarget:"
+ "supportedVideoFormatsForHiResOrX420ForDevicePosition:deviceType:"
+ "supportedVideoFormatsForStillImageCaptureForDevicePosition:deviceType:"
- "@136@0:8^{__CVBuffer=}16q24@32@40{?=qiIq}48{?=[3]}72@120@128"
- "@168@0:8{?=[3]}16{CGSize=dd}64q80Q8896128d144@152@160"
- "FocalLenIn35mmFilm"
- "_captureLensFromEXIFData:"
- "initWithIntrinsics:imageResolution:devicePosition:lensType:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:"
- "initWithPixelBuffer:captureFramePerSecond:captureDevice:captureSession:timestamp:intrinsics:exif:tiff:"
- "{Exif}"
- "{TIFF}"

```
