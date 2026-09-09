## HRTFEnrollment

> `/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment`

```diff

-40.41.1.1.7
-  __TEXT.__text: 0x969c
-  __TEXT.__objc_methlist: 0x8d8
-  __TEXT.__const: 0xd4
-  __TEXT.__cstring: 0x9a7
-  __TEXT.__oslogstring: 0x52d
+40.41.1.1.10
+  __TEXT.__text: 0xb118
+  __TEXT.__objc_methlist: 0x928
+  __TEXT.__const: 0xe4
+  __TEXT.__cstring: 0x9ac
+  __TEXT.__oslogstring: 0x719
   __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x200
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x1ea8
+  __AUTH_CONST.__objc_const: 0x1ec8
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x3a8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 189
-  Symbols:   791
-  CStrings:  164
+  Functions: 196
+  Symbols:   810
+  CStrings:  175
 
Symbols:
+ -[HRTFEnrollmentSession _verifyNonDepthFormatCaptureDevice:]
+ -[HRTFEnrollmentSession didReceiveNonDepthFormatVideoData:colorData:depthData:faceObject:]
+ -[HRTFEnrollmentSession initializeNonDepthFormatDevice]
+ -[HRTFSyncedCaptureSource _configureNonDepthFormatVideoOutputsForDevice:inSession:]
+ -[HRTFSyncedCaptureSource _initializeForNonDepthFormat]
+ -[HRTFSyncedCaptureSource _verifyNonDepthFormatCaptureDevice:]
+ -[HRTFSyncedCaptureSource dataOutputSynchronizerForNonDepthFormat:didOutputSynchronizedDataCollection:]
+ _AVCaptureDeviceTypeBuiltInWideAngleCamera
+ _CGPointZero
+ _HRTFDepthFormatNotSupported.sDepthFormatNotSupported
+ _MGIsDeviceOfType
+ _OBJC_IVAR_$_HRTFEnrollmentSession._dummyDepthPixelBuffer
+ _objc_msgSend$_configureNonDepthFormatVideoOutputsForDevice:inSession:
+ _objc_msgSend$_initializeForNonDepthFormat
+ _objc_msgSend$_verifyNonDepthFormatCaptureDevice:
+ _objc_msgSend$dataOutputSynchronizerForNonDepthFormat:didOutputSynchronizedDataCollection:
+ _objc_msgSend$didReceiveNonDepthFormatVideoData:colorData:depthData:faceObject:
+ _objc_msgSend$initializeNonDepthFormatDevice
+ _objc_retain_x27
CStrings:
+ "Non Depth: capture device color format: %s"
+ "Non Depth: failed to verify color format for capture device"
+ "NonDepth: Depth format not supported, fill in with dummy data for cameraCalibrationData"
+ "NonDepth: Depth format not supported, fill in with dummy data for depthPixelBuffer"
+ "NonDepth: cannot retrieve exposure time"
+ "NonDepth: color data is absent"
+ "NonDepth: color instrinsics data is absent"
+ "NonDepth: depth data is absent"
+ "NonDepth: lense calibration data is absent"
+ "NonDepth: video frame arrived"
+ "True"
+ "\xf0Q"
- "\xf0A"
```
