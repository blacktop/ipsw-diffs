## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-587.60.6.0.0
-  __TEXT.__text: 0x14b084
-  __TEXT.__auth_stubs: 0x1970
-  __TEXT.__objc_methlist: 0xd250
+587.60.10.122.3
+  __TEXT.__text: 0x14bb0c
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0xd2a0
   __TEXT.__const: 0x938
-  __TEXT.__gcc_except_tab: 0x2c40
-  __TEXT.__cstring: 0x25058
-  __TEXT.__oslogstring: 0x1d412
+  __TEXT.__gcc_except_tab: 0x2c78
+  __TEXT.__cstring: 0x25219
+  __TEXT.__oslogstring: 0x1d526
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x4078
+  __TEXT.__unwind_info: 0x4098
   __TEXT.__objc_classname: 0x1755
-  __TEXT.__objc_methname: 0x2517b
+  __TEXT.__objc_methname: 0x25344
   __TEXT.__objc_methtype: 0x39f2
-  __TEXT.__objc_stubs: 0x15b80
+  __TEXT.__objc_stubs: 0x15c40
   __DATA_CONST.__got: 0x26a8
   __DATA_CONST.__const: 0x7660
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c00
+  __DATA_CONST.__objc_selrefs: 0x6c48
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x408
-  __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x12280
-  __AUTH_CONST.__objc_const: 0x16448
+  __AUTH_CONST.__auth_got: 0xcd8
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0x122e0
+  __AUTH_CONST.__objc_const: 0x164b0
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x1704
+  __DATA.__objc_ivar: 0x170c
   __DATA.__data: 0xc48
   __DATA.__common: 0x270
-  __DATA.__bss: 0x6a0
+  __DATA.__bss: 0x680
   __DATA_DIRTY.__objc_data: 0x2f80
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x280
-  __DATA_DIRTY.__bss: 0x348
+  __DATA_DIRTY.__bss: 0x358
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5338
-  Symbols:   7619
-  CStrings:  10336
+  Functions: 5349
+  Symbols:   7632
+  CStrings:  10357
 
Symbols:
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_get_qos_class
CStrings:
+ "-[AVCDOSDataOutputStorage updateDelegateOverrideCallbackQueueQOSClass:]"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeFocusLocked:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]_block_invoke"
+ "0768b2d285641ba5388a2d860099ffdd95eba2f3"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %!s(MISSING): (%!p(MISSING)) updating QOS to %!d(MISSING)"
+ "<<<< AVCaptureSession >>>> %!s(MISSING): Ignored focus locked update because the session was deallocated"
+ "<<<< AVCaptureSession >>>> %!s(MISSING): Not calling -session:didChangeFocusLocked: on delegate on an unsupported client"
+ "Video settings dimensions must have a valid aspect ratio"
+ "VisionDataCameraIntrinsicMatrix"
+ "cameraOverlayConnection:didChangeFocusLocked:"
+ "description=CameraCapture_AVF-587.60.10.122.3"
+ "emitsEmptyObjectDetectionMetadata"
+ "f36362b8d82893a515a980896dd16d8b172661db"
+ "handleControlsOverlay:didChangeFocusLocked:"
+ "isVideoSettingsAspectRatioOverrideEnabled"
+ "isVideoSettingsAspectRatioOverrideSupported"
+ "session:controlsDidChangeAutoFocusLocked:"
+ "setEmitsEmptyObjectDetectionMetadata:"
+ "setVideoSettingsAspectRatioOverrideEnabled:"
+ "updateDelegateOverrideCallbackQueueQOSClass:"
+ "videoSettingsAspectRatioOverrideEnabled"
+ "videoSettingsAspectRatioOverrideSupported is false, cannot enable"
+ "willStartProcessingBuffer:withStatus:"
- "0a993ba543e84d6a0531ae7a0a4fb0fb916227a4"
- "8616b3db09b5bdb850a5f76a5af7c7f58dc86dbf"
- "description=CameraCapture_AVF-587.60.6"

```
