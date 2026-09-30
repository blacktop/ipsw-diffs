## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x14fc54
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xde8c
-  __TEXT.__const: 0x930
-  __TEXT.__gcc_except_tab: 0x28c8
-  __TEXT.__cstring: 0x279bb
-  __TEXT.__oslogstring: 0x1f0b0
+655.0.0.122.4
+  __TEXT.__text: 0x150278
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0xde9c
+  __TEXT.__const: 0x960
+  __TEXT.__gcc_except_tab: 0x28b4
+  __TEXT.__cstring: 0x2798a
+  __TEXT.__oslogstring: 0x1f1bd
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x45f8
-  __TEXT.__objc_classname: 0x17e1
-  __TEXT.__objc_methname: 0x26ddd
-  __TEXT.__objc_methtype: 0x3c0f
-  __TEXT.__objc_stubs: 0x16ac0
-  __DATA_CONST.__got: 0x27b0
-  __DATA_CONST.__const: 0x6f30
+  __TEXT.__unwind_info: 0x45e8
+  __TEXT.__objc_classname: 0x17e6
+  __TEXT.__objc_methname: 0x26e2c
+  __TEXT.__objc_methtype: 0x3c28
+  __TEXT.__objc_stubs: 0x16b00
+  __DATA_CONST.__got: 0x27c8
+  __DATA_CONST.__const: 0x7088
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71c8
+  __DATA_CONST.__objc_selrefs: 0x71d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x428
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x13940
-  __AUTH_CONST.__objc_const: 0x16908
+  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x13920
+  __AUTH_CONST.__objc_const: 0x168a0
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x17dc
-  __DATA.__data: 0xc70
+  __DATA.__objc_ivar: 0x17d8
+  __DATA.__data: 0xc60
   __DATA.__common: 0x280
   __DATA.__bss: 0x6f0
   __DATA_DIRTY.__objc_data: 0x2fd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F3DBC2B-AA9F-3344-891D-6898C4329F49
+  UUID: 1B713B7B-26AD-3409-AB9D-CFD501414446
   Functions: 5907
-  Symbols:   20967
-  CStrings:  13379
+  Symbols:   20970
+  CStrings:  13381
 
Symbols:
+ -[AVCaptureControl overlayDidMakeControlActive:]
+ -[AVCaptureDeviceFormat _defaultPhotoDimensionsInNativeSensorOrientationWithHighResolutionCaptureEnabled:]
+ -[AVCaptureDeviceRotationCoordinator externalDisplayLayerObserver:visibiltyChanged:]
+ -[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]
+ -[AVCaptureVisibilityHelperLayer dealloc]
+ -[AVCaptureVisibilityHelperLayer initWithDelegate:]
+ -[AVCaptureVisibilityHelperLayer layerDidBecomeVisible:]
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table224
+ GCC_except_table230
+ GCC_except_table239
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table273
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table287
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table313
+ GCC_except_table334
+ GCC_except_table345
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table355
+ GCC_except_table369
+ GCC_except_table392
+ GCC_except_table402
+ GCC_except_table414
+ GCC_except_table429
+ GCC_except_table432
+ GCC_except_table459
+ GCC_except_table463
+ GCC_except_table474
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table495
+ GCC_except_table500
+ GCC_except_table507
+ GCC_except_table515
+ GCC_except_table525
+ GCC_except_table539
+ GCC_except_table562
+ GCC_except_table573
+ GCC_except_table583
+ GCC_except_table597
+ GCC_except_table613
+ GCC_except_table632
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table684
+ GCC_except_table686
+ GCC_except_table688
+ GCC_except_table712
+ GCC_except_table724
+ GCC_except_table726
+ GCC_except_table728
+ GCC_except_table734
+ GCC_except_table736
+ GCC_except_table779
+ GCC_except_table783
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table884
+ GCC_except_table886
+ GCC_except_table888
+ _AVAppleMakerNote_FirstSupportedReleaseVersion
+ _AVAppleMakerNote_NominalFocalLengthIn35mmFilm
+ _AVGQCaptureDICOMSupported
+ _AVGQFrontFacingCameraFocalLengthIn35mm
+ _FigCaptureGetDeviceToCameraTransform
+ _OBJC_CLASS_$_AVCaptureVisibilityHelperLayer
+ _OBJC_IVAR_$_AVCaptureControlsOverlay._activeControlIdentifier
+ _OBJC_IVAR_$_AVCaptureVisibilityHelperLayer._delegate
+ _OBJC_METACLASS_$_AVCaptureVisibilityHelperLayer
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVisibilityHelperLayer
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureVisibilityHelperLayer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVCaptureVisibilityHelperLayerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCaptureVisibilityHelperLayerDelegate
+ __OBJC_CLASS_RO_$_AVCaptureVisibilityHelperLayer
+ __OBJC_LABEL_PROTOCOL_$_AVCaptureVisibilityHelperLayerDelegate
+ __OBJC_METACLASS_RO_$_AVCaptureVisibilityHelperLayer
+ __OBJC_PROTOCOL_$_AVCaptureVisibilityHelperLayerDelegate
+ ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.437
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.439
+ ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke.551
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.694
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.705
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.705.cold.1
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.707
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.712
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.715
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.732
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.736
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.737
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.744
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.749
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.751
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.762
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.695
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.711
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.713
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.716
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.724
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.743
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.748
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.750
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.755
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.760
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.696
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.714
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.725
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.761
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.700
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.701
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.702
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.703
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.704
+ ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.635
+ ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke.346
+ ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke.202
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.338
+ ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.457
+ ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.510
+ ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.688
+ ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.424
+ ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.452
+ ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke
+ ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke.350
+ ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.508
+ ___block_descriptor_40_e8_32o_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_449_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8
+ ___block_descriptor_73_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_81_e8_32o40r48r56r64r72r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8
+ ___block_descriptor_81_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_literal_global.1101
+ ___block_literal_global.1103
+ ___block_literal_global.1375
+ ___block_literal_global.1382
+ ___block_literal_global.1677
+ ___block_literal_global.181
+ ___block_literal_global.186
+ ___block_literal_global.283
+ ___block_literal_global.376
+ ___block_literal_global.461
+ ___block_literal_global.487
+ ___block_literal_global.544
+ ___block_literal_global.549
+ ___block_literal_global.553
+ _kFigCapturePortType_FrontFacingCamera
+ _kFigCapturePortType_FrontFacingSuperWideCamera
+ _kVTCompressionPropertyKey_PreserveDynamicHDRMetadata
+ _objc_msgSend$_defaultPhotoDimensionsInNativeSensorOrientationWithHighResolutionCaptureEnabled:
+ _objc_msgSend$_setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:
+ _objc_msgSend$externalDisplayLayerObserver:visibiltyChanged:
+ _objc_msgSend$maxContinuousZoomFactorForDepthDataDelivery
+ _objc_msgSend$overlayDidMakeControlActive:
+ _objc_msgSend$setCameraExtrinsicMatrix:
- -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeOverlayVisible:]
- -[AVCaptureDeviceFormat _defaultPhotoDimensionsWithHighResolutionCaptureEnabled:]
- -[AVCaptureDeviceRotationCoordinator layer:didBecomeVisible:]
- -[AVCaptureRotationHelperLayer dealloc]
- -[AVCaptureRotationHelperLayer initWithDelegate:]
- -[AVCaptureRotationHelperLayer layerDidBecomeVisible:]
- GCC_except_table157
- GCC_except_table160
- GCC_except_table199
- GCC_except_table218
- GCC_except_table223
- GCC_except_table229
- GCC_except_table238
- GCC_except_table250
- GCC_except_table253
- GCC_except_table272
- GCC_except_table278
- GCC_except_table281
- GCC_except_table284
- GCC_except_table286
- GCC_except_table294
- GCC_except_table297
- GCC_except_table312
- GCC_except_table333
- GCC_except_table344
- GCC_except_table346
- GCC_except_table348
- GCC_except_table354
- GCC_except_table368
- GCC_except_table391
- GCC_except_table401
- GCC_except_table413
- GCC_except_table428
- GCC_except_table431
- GCC_except_table458
- GCC_except_table462
- GCC_except_table473
- GCC_except_table481
- GCC_except_table488
- GCC_except_table494
- GCC_except_table499
- GCC_except_table506
- GCC_except_table514
- GCC_except_table524
- GCC_except_table538
- GCC_except_table561
- GCC_except_table572
- GCC_except_table582
- GCC_except_table596
- GCC_except_table612
- GCC_except_table631
- GCC_except_table652
- GCC_except_table655
- GCC_except_table683
- GCC_except_table685
- GCC_except_table687
- GCC_except_table711
- GCC_except_table723
- GCC_except_table725
- GCC_except_table727
- GCC_except_table733
- GCC_except_table735
- GCC_except_table778
- GCC_except_table782
- GCC_except_table835
- GCC_except_table837
- GCC_except_table839
- GCC_except_table841
- GCC_except_table883
- GCC_except_table885
- GCC_except_table887
- _AVCaptureBundleCameraPhotographicStylesOptOut
- _AVCaptureBundleCameraPhotographicStylesOptOutDescription
- _AVCaptureDeviceLensSmudgeDetectionStatusChangedKeyStatus
- _AVCaptureDeviceLensSmudgeDetectionStatusChangedNotification
- _AVSmartStyleSettingsSystemStyleEnabledDefaultPreferenceKey
- _OBJC_CLASS_$_AVCaptureRotationHelperLayer
- _OBJC_IVAR_$_AVCaptureRotationHelperLayer._delegate
- _OBJC_IVAR_$_AVCaptureSessionInternal.smartStyleInThirdPartyAppsEnabled
- _OBJC_IVAR_$_AVCaptureSessionInternal.smartStyleInVideoModeEnabled
- _OBJC_METACLASS_$_AVCaptureRotationHelperLayer
- __OBJC_$_INSTANCE_METHODS_AVCaptureRotationHelperLayer
- __OBJC_$_INSTANCE_VARIABLES_AVCaptureRotationHelperLayer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVCaptureRotationHelperLayerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVCaptureRotationHelperLayerDelegate
- __OBJC_$_PROTOCOL_REFS_AVCaptureRotationHelperLayerDelegate
- __OBJC_CLASS_RO_$_AVCaptureRotationHelperLayer
- __OBJC_LABEL_PROTOCOL_$_AVCaptureRotationHelperLayerDelegate
- __OBJC_METACLASS_RO_$_AVCaptureRotationHelperLayer
- __OBJC_PROTOCOL_$_AVCaptureRotationHelperLayerDelegate
- ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.428
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.442
- ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke.554
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.685
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.696
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.696.cold.1
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.698
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.703
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.706
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.714
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.727
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.728
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.733
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.735
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.740
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.747
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.686
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.702
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.704
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.707
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.715
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.732
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.734
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.739
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.746
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.751
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.687
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.705
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.716
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.752
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.691
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.692
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.693
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.694
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.695
- ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.626
- ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke.337
- ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke.208
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.341
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.329
- ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.448
- ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.501
- ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.679
- ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.415
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.443
- ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.499
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_441_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8
- ___block_descriptor_65_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_73_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_literal_global.1110
- ___block_literal_global.1115
- ___block_literal_global.1378
- ___block_literal_global.1385
- ___block_literal_global.1669
- ___block_literal_global.187
- ___block_literal_global.192
- ___block_literal_global.287
- ___block_literal_global.380
- ___block_literal_global.464
- ___block_literal_global.490
- ___block_literal_global.547
- ___block_literal_global.552
- ___block_literal_global.556
- _objc_msgSend$_defaultPhotoDimensionsWithHighResolutionCaptureEnabled:
- _objc_msgSend$cameraOverlayConnection:didChangeOverlayVisible:activeControlIdentifier:
- _objc_msgSend$clientMaxContinuousZoomFactorForDepthDataDelivery
- _objc_msgSend$layer:didBecomeVisible:
CStrings:
+ "-[AVCaptureConnection clientRetainedBufferCount]"
+ "-[AVCaptureDeviceRotationCoordinator externalDisplayLayerObserver:visibiltyChanged:]"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke"
+ "2OOO@"
+ "6cce482db0e978aa552469d2202544b27a85953f"
+ "97"
+ "98"
+ "<<<< AVCaptureConnection >>>> %s: %p clientRetainedBufferCount for connection to %@ is %d"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send control update (%@) to the overlay (%@) for %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Overlay changed active control identifier: %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Overlay changed visible: %d, active control identifier: %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent control value update (%@) to the overlay for %@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: Unsupported rotation of %d degrees"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled, active format is not photo format %@"
+ "@\"AVCaptureVisibilityHelperLayer\""
+ "AVCaptureVisibilityHelperLayer"
+ "AVCaptureVisibilityHelperLayerDelegate"
+ "AVGQCaptureDICOMSupported"
+ "AVGQFrontFacingCameraFocalLengthIn35mm"
+ "LastShownBuild:AVCaptureConnection.m:801"
+ "LastShownDate:AVCaptureConnection.m:801"
+ "_activeControlIdentifier"
+ "_defaultPhotoDimensionsInNativeSensorOrientationWithHighResolutionCaptureEnabled:"
+ "_setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:"
+ "a1f7aeecd16c4ee262e82496405ddd12bf40fbc6"
+ "avcmdo_detectedObjectsCollectionForSampleBuffer"
+ "com.microsoft.teams2"
+ "description=CameraCapture_AVF-655.0.0.122.4"
+ "ed6240ee295d09fa1ebcb64acd38b914cbb5013c"
+ "externalDisplayLayerObserver:visibiltyChanged:"
+ "i44@0:8{?=qiIq}16B40"
+ "maxContinuousZoomFactorForDepthDataDelivery"
+ "overlayDidMakeControlActive:"
+ "setCameraExtrinsicMatrix:"
+ "v28@0:8@\"AVCaptureVisibilityHelperLayer\"16B24"
- "%@systemstyle-enabled-default"
- "-[AVCaptureDeviceRotationCoordinator layer:didBecomeVisible:]"
- "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]"
- "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke"
- "-[AVCaptureSession isApplicationOptedOutByDefaultToSmartStyles]"
- "0f4ec8652c6ac8093cc67a178a48c7d5260463ef"
- "16c20df05460c3f1051d8276a8d50b236cb7c3ec"
- "2OOO"
- "580bcf2268cc115fc76e8d7941782a46a93070c2"
- "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send control update to the overlay (%@)"
- "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent control value update to the overlay"
- "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for video mode and active format is not photo format %@"
- "<<<< AVCaptureSession >>>> %s: Could not find LSApplicationRecord for bundleID: %@"
- "@\"AVCaptureRotationHelperLayer\""
- "AVCaptureDeviceLensSmudgeDetectionStatusChangedKeyStatus"
- "AVCaptureDeviceLensSmudgeDetectionStatusChangedNotification"
- "AVCaptureRotationHelperLayer"
- "AVCaptureRotationHelperLayerDelegate"
- "CFBundleName"
- "Camera"
- "LastShownBuild:AVCaptureConnection.m:800"
- "LastShownDate:AVCaptureConnection.m:800"
- "NSCameraPhotographicStylesOptOut"
- "NSCameraPhotographicStylesOptOutDescription"
- "Sandwich"
- "_defaultPhotoDimensionsWithHighResolutionCaptureEnabled:"
- "cameraOverlayConnection:didChangeOverlayVisible:"
- "clientMaxContinuousZoomFactorForDepthDataDelivery"
- "description=CameraCapture_AVF-650.0.0.122.4"
- "layer:didBecomeVisible:"
- "smartStyleInThirdPartyAppsEnabled"
- "smartStyleInVideoModeEnabled"
- "v28@0:8@\"AVCaptureRotationHelperLayer\"16B24"

```
