## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x1513b0
+661.0.0.0.3
+  __TEXT.__text: 0x151648
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0xdef4
+  __TEXT.__objc_methlist: 0xdf04
   __TEXT.__const: 0x960
-  __TEXT.__gcc_except_tab: 0x28b8
-  __TEXT.__cstring: 0x27aa2
+  __TEXT.__gcc_except_tab: 0x28cc
+  __TEXT.__cstring: 0x27ab3
   __TEXT.__oslogstring: 0x1f59e
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x4780
+  __TEXT.__unwind_info: 0x4790
   __TEXT.__objc_classname: 0x17ef
-  __TEXT.__objc_methname: 0x26f6b
+  __TEXT.__objc_methname: 0x26fbb
   __TEXT.__objc_methtype: 0x3c6c
-  __TEXT.__objc_stubs: 0x16c40
-  __DATA_CONST.__got: 0x27a8
+  __TEXT.__objc_stubs: 0x16ca0
+  __DATA_CONST.__got: 0x27c0
   __DATA_CONST.__const: 0x7100
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7220
+  __DATA_CONST.__objc_selrefs: 0x7238
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x428
   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x13ae0
+  __AUTH_CONST.__cfstring: 0x13b00
   __AUTH_CONST.__objc_const: 0x16920
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /System/Library/PrivateFrameworks/Quagga.framework/Quagga
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A28D6FA-F0AA-3DF2-BEE3-283ACE1FC92A
-  Functions: 5916
-  Symbols:   21000
-  CStrings:  13436
+  UUID: 75648989-F9F7-368F-AB7F-3D82C3C9C299
+  Functions: 5917
+  Symbols:   21009
+  CStrings:  13441
 
Symbols:
+ -[AVCaptureVideoPreviewLayer _updatePreferredDynamicRange:]
+ _CADynamicRangeHigh
+ _CADynamicRangeStandard
+ ___block_descriptor_457_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r448r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8r448l8
+ ___block_descriptor_56_e8_32o40o48o_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ _kFigCaptureSessionPreviewSinkNotification_DidDisplayFirstPreviewFrame
+ _objc_msgSend$_updatePreferredDynamicRange:
+ _objc_msgSend$focusLockGestureEnabled
+ _objc_msgSend$setPreferredDynamicRange:
- ___block_descriptor_449_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8
- ___block_descriptor_48_e8_32o40o_e17_v16?0"NSError"8ls32l8s40l8
Functions:
~ _avccm_commonDisallowListForVideoEffectsAndMicModes : 160 -> 168
~ -[AVCaptureConnection setupInternalStorage] : 2340 -> 2320
~ -[AVCaptureSession _activateControlsOverlayIfNecessary] : 156 -> 168
~ -[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:] : 1316 -> 1332
~ -[AVCaptureVideoDataOutput preparesCellularRadioForNetworkConnection] : 160 -> 180
~ -[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:] : 7224 -> 7312
~ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke : 8064 -> 8096
~ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_19 : 108 -> 128
~ -[AVCaptureVideoPreviewLayer handleChangedActiveFormat:forDevice:] : 72 -> 104
~ -[AVCaptureVideoPreviewLayer attachSafelyToFigCaptureSession:] : 292 -> 328
~ -[AVCaptureVideoPreviewLayer detachSafelyFromFigCaptureSession:] : 292 -> 328
~ -[AVCaptureVideoPreviewLayer _handleNotification:payload:] : 2584 -> 2656
+ -[AVCaptureVideoPreviewLayer _updatePreferredDynamicRange:]
~ -[AVCaptureControlsOverlay _sendControlsIsolated] : 788 -> 796
~ ___49-[AVCaptureControlsOverlay _sendControlsIsolated]_block_invoke : 560 -> 572
~ -[AVCaptureMetadataOutput _processSampleBuffer:] : 8576 -> 8592
~ -[AVCaptureInputPort figCaptureSourceConfigurationForSessionPreset:] : 2876 -> 2948
CStrings:
+ "2OOOA"
+ "73fe176ff11b2279f9f6854cedc56746ea4ae41d"
+ "786b8494a04f5622b574567bbfe5f23e8669ae2b"
+ "LastShownBuild:AVCaptureConnection.m:799"
+ "LastShownBuild:AVCaptureVideoPreviewLayer.m:1916"
+ "LastShownDate:AVCaptureConnection.m:799"
+ "LastShownDate:AVCaptureVideoPreviewLayer.m:1916"
+ "_updatePreferredDynamicRange:"
+ "com.google.paisa"
+ "description=CameraCapture_AVF-661.0.0.0.3"
+ "focusLockGestureEnabled"
+ "setPreferredDynamicRange:"
- "0fc71cd6c11007070fa06c9f109046af164392d6"
- "2OOO@"
- "4c8026313c8deb46069197fa963180c366d4c374"
- "LastShownBuild:AVCaptureConnection.m:801"
- "LastShownBuild:AVCaptureVideoPreviewLayer.m:1908"
- "LastShownDate:AVCaptureConnection.m:801"
- "LastShownDate:AVCaptureVideoPreviewLayer.m:1908"
- "description=CameraCapture_AVF-659.0.0.0.4"

```
