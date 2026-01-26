## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4097.80.9.0.0
-  __TEXT.__text: 0x3f7554
-  __TEXT.__auth_stubs: 0x68f0
-  __TEXT.__objc_methlist: 0x2fc30
-  __TEXT.__const: 0x22c64
-  __TEXT.__gcc_except_tab: 0x3208
-  __TEXT.__cstring: 0x1f6f7
-  __TEXT.__oslogstring: 0x16474
+4097.80.14.0.0
+  __TEXT.__text: 0x3fc924
+  __TEXT.__auth_stubs: 0x6920
+  __TEXT.__objc_methlist: 0x2fcf8
+  __TEXT.__const: 0x23084
+  __TEXT.__gcc_except_tab: 0x31ec
+  __TEXT.__cstring: 0x1fa67
+  __TEXT.__oslogstring: 0x16554
   __TEXT.__dlopen_cstrs: 0x3b9
   __TEXT.__ustring: 0x8
-  __TEXT.__constg_swiftt: 0x5e64
-  __TEXT.__swift5_typeref: 0x27e8e
-  __TEXT.__swift5_reflstr: 0x608a
-  __TEXT.__swift5_fieldmd: 0x51bc
+  __TEXT.__constg_swiftt: 0x5fe8
+  __TEXT.__swift5_typeref: 0x27ff4
+  __TEXT.__swift5_reflstr: 0x625a
+  __TEXT.__swift5_fieldmd: 0x537c
   __TEXT.__swift5_builtin: 0x438
-  __TEXT.__swift5_assocty: 0x15e8
-  __TEXT.__swift5_proto: 0xa6c
-  __TEXT.__swift5_types: 0x55c
-  __TEXT.__swift5_capture: 0x29c8
+  __TEXT.__swift5_assocty: 0x1648
+  __TEXT.__swift5_proto: 0xab4
+  __TEXT.__swift5_types: 0x568
+  __TEXT.__swift5_capture: 0x2978
   __TEXT.__swift_as_entry: 0xd4
   __TEXT.__swift_as_ret: 0xc8
-  __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xee80
-  __TEXT.__eh_frame: 0x2d58
-  __TEXT.__objc_classname: 0x5671
-  __TEXT.__objc_methname: 0x9ec2e
-  __TEXT.__objc_methtype: 0x1089a
-  __TEXT.__objc_stubs: 0x5ab00
-  __DATA_CONST.__got: 0x4460
-  __DATA_CONST.__const: 0x7e30
-  __DATA_CONST.__objc_classlist: 0x1228
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__unwind_info: 0xef60
+  __TEXT.__eh_frame: 0x2f68
+  __TEXT.__objc_classname: 0x568d
+  __TEXT.__objc_methname: 0x9ed11
+  __TEXT.__objc_methtype: 0x108dd
+  __TEXT.__objc_stubs: 0x5abe0
+  __DATA_CONST.__got: 0x4478
+  __DATA_CONST.__const: 0x7ea8
+  __DATA_CONST.__objc_classlist: 0x1230
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x7b0
+  __DATA_CONST.__objc_protolist: 0x7c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19fe8
-  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x1a030
+  __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1048
-  __AUTH_CONST.__auth_got: 0x3488
-  __AUTH_CONST.__const: 0xe560
+  __AUTH_CONST.__auth_got: 0x34a0
+  __AUTH_CONST.__const: 0xe8a8
   __AUTH_CONST.__cfstring: 0x16700
-  __AUTH_CONST.__objc_const: 0x508a8
+  __AUTH_CONST.__objc_const: 0x50a70
   __AUTH_CONST.__objc_intobj: 0x1860
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x5ea8
-  __AUTH.__data: 0xf20
-  __DATA.__objc_ivar: 0x3c68
-  __DATA.__data: 0xb5c0
-  __DATA.__bss: 0x11620
-  __DATA.__common: 0x1a0
+  __AUTH.__objc_data: 0x5f40
+  __AUTH.__data: 0x1040
+  __DATA.__objc_ivar: 0x3c64
+  __DATA.__data: 0xb688
+  __DATA.__bss: 0x11a50
+  __DATA.__common: 0x1b0
   __DATA_DIRTY.__objc_data: 0x7710
-  __DATA_DIRTY.__data: 0x3408
+  __DATA_DIRTY.__data: 0x3410
   __DATA_DIRTY.__bss: 0x3f40
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50F82DC8-3C7F-3947-A89E-1E3F8656C549
-  Functions: 26246
-  Symbols:   60249
-  CStrings:  31548
+  UUID: 2026A816-02C3-33D0-9053-C77CD70ECBCA
+  Functions: 26357
+  Symbols:   60297
+  CStrings:  31590
 
Symbols:
+ -[CAMMotionController _beginUpdatingOrientationModelIfNeeded]
+ -[CAMMotionController _beginUpdatingOrientationModel]
+ -[CAMMotionController _endUpdatingOrientationModelIfNeeded]
+ -[CAMMotionController _shouldEndUpdatingOrientationModel]
+ -[CAMMotionController orientationModel:didChangeInterfaceOrientation:]
+ -[CAMMotionController roughOrientationDidChange:]
+ -[CAMMotionController setUseOrientationModelOnlyWhileFlat:]
+ -[CAMMotionController useOrientationModelOnlyWhileFlat]
+ -[CAMViewfinderViewController _shouldDisableModeForActiveCall:]
+ -[CAMViewfinderViewController _updateChromeWithOrientationModel]
+ GCC_except_table1323
+ GCC_except_table1451
+ _CAMAnalyticsStringForCaptureMode
+ _CAMAnalyticsStringForDevicePosition
+ _OBJC_IVAR_$_CAMMotionController._useOrientationModelOnlyWhileFlat
+ __DATA__TtC8CameraUI39ChromeAnalyticsEventControlPanelSession
+ __IVARS__TtC8CameraUI39ChromeAnalyticsEventControlPanelSession
+ __METACLASS_DATA__TtC8CameraUI39ChromeAnalyticsEventControlPanelSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CAMOrientationModelDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMOrientationModelDelegate
+ __OBJC_LABEL_PROTOCOL_$_CAMOrientationModelDelegate
+ __OBJC_PROTOCOL_$_CAMOrientationModelDelegate
+ __PROTOCOL_CAMOrientationModelDelegate
+ __PROTOCOL_INSTANCE_METHODS_OPT_CAMOrientationModelDelegate
+ __PROTOCOL_METHOD_TYPES_CAMOrientationModelDelegate
+ _associated conformance 8CameraUI39ChromeAnalyticsEventControlPanelSessionC07ChangedF0OSHAASQ
+ _associated conformance 8CameraUI39ChromeAnalyticsEventControlPanelSessionC0E4KeysOSHAASQ
+ _associated conformance 8CameraUI39ChromeAnalyticsEventControlPanelSessionC0E4KeysOs12CaseIterableAA8AllCasessAFP_Sl
+ _associated conformance 8CameraUI39ChromeAnalyticsEventControlPanelSessionCAA0cdE0AA0E4KeysAaDP_SY
+ _associated conformance 8CameraUI39ChromeAnalyticsEventControlPanelSessionCAA0cdE0AA0E4KeysAaDP_s12CaseIterable
+ _flat unique So27CAMOrientationModelDelegate_p
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAE15sensoryFeedback_7triggerQrAA07SensoryK0V_qd__tSQRd__lFQOyAeAE7gesture_9includingQrqd___AA11GestureMaskVtAA0P0Rd__lFQOyAeAE012simultaneousP0_ANQrqd___APtAaQRd__lFQOyACyAA6VStackVyAA05TupleE0VyAE06PhotosA6UICoreE6hiddenyQrSbFQOyACyACy06CameraB028ApplicationMaterialContainerVyACyACyAA6ZStackVyAVyACyACyACyAY20ChromeDynamicShutterVAA16_FixedSizeLayoutVGAA23_GeometryActionModifierVySo6CGRectVA10_SQ12CoreGraphicsyHCg_GGAY017DetectInteractionP8ModifierVG_AA6HStackVyAVyACyACyACyAY9ImageWellVAA22_MatchedGeometryEffectVySSGGAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGA15_G_AA6SpacerVtGGSgtGGAA14_PaddingLayoutVGA40_GGA40_GAY21ShutterAccessoryViewsVyAY20OrientationIndicatorVSgAA05EmptyE0VGG_Qo_Sg_A1_yAVyAA012_ConditionalD0VyACyACyACyACyACyACyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyACyAeAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyA1_yA57_yACyACyAY026ChromeControlPanelExpandedD0VAY32ConditionalMatchedGeometryEffectVySSGGAA30_EnvironmentKeyWritingModifierVyAA0D12SizeCategoryOGGACyACyACyACyAY24ChromeBottomControlPanelVA66_GAA12_ScaleEffectVGA29_GAA01_Q15AlignmentEffectVyACyAA16RoundedRectangleVA66_GGGGSgGA29_G_Qo_AA31AccessibilityAttachmentModifierVGAA19_BackgroundModifierVyACyACyACyAeAE14materialEffect_2inQrAA0Z0V_AA9_ShapeSetVtFQOyAA5ColorV_Qo_A66_GA66_GA78_GGG_SbQo_A12_GA40_GA29_GAY26CapturingBurstHideModifierVGAY30CapturingFromTimerHideModifierVGAY0E17ModelHideModifierVGACyA51_A12_GG_ACyACyA57_yACyACyA105_AA12_FrameLayoutVGAA25_AllowsHitTestingModifierVGACyACyACyAeAE20accessibilityFocusedyQrAA23AccessibilityFocusStateV7BindingVySb_GFQOyACyAY12ModeWheelRowVyACyAA5GroupVyA57_yAY24GlassCircleElementButtonVACyACyA24_AA14_OpacityEffectVGA15_GGGA40_GACyA142_yA57_yACyACyACyACyA144_AY26RecordingVideoHideModifierVGA120_GAY25HideDuringQuietUIModifierVGAA32_EnvironmentKeyTransformModifierVySbGGACyACyA144_A146_GA15_GGGA40_GGA5_G_Qo_AA26_OverlayPreferenceModifierVyAY22ModeLoupePreferenceKeyVAA14GeometryReaderVyACyACyACyACyACyAY9ModeLoupeVA66_GA66_GA128_GAA15_PositionLayoutVGAA18_AnimationModifierVys11AnyHashableVSgGGGSgGGA186_ySbGGA123_GGA40_GA40_GtGGtGGAA01_D13ShapeModifierVyAA9RectangleVGG_AA06_EndedP0VyAA08_ChangedP0VyAA04DragP0VGGSgQo__A220_Qo__SiQo__SbQo__SbQo__SbQo__AY13ChromeElementOSgQo__SbQo__A229_Qo__SSSgQo_A196_GA196_GA186_yA11_7CGFloatVGGA239_GAaDHPA240_AaDHPA236_AaDHPA235_AaDHPqd0__AaDHD3_A234_HO_A196_AA0E8ModifierHPyHCHC_A196_AAA242_HPyHCHC_A239_AAA242_HPyHCHC_A239_AAA242_HPyHCHC.353
+ _keypath_get.480Tm
+ _keypath_get.515Tm
+ _keypath_get.637Tm
+ _keypath_get.667Tm
+ _keypath_get.871Tm
+ _keypath_set.408Tm
+ _keypath_set.582Tm
+ _objc_msgSend$_beginUpdatingOrientationModel
+ _objc_msgSend$_beginUpdatingOrientationModelIfNeeded
+ _objc_msgSend$_endUpdatingOrientationModelIfNeeded
+ _objc_msgSend$_shouldDisableModeForActiveCall:
+ _objc_msgSend$_shouldEndUpdatingOrientationModel
+ _objc_msgSend$_updateChromeWithOrientationModel
+ _objc_msgSend$isUpright
+ _objc_msgSend$setUseOrientationModelOnlyWhileFlat:
+ _objc_msgSend$updateAnalyticsForUserChangedSmartStylePreset
+ _objc_msgSend$useOrientationModelOnlyWhileFlat
+ _swift_unexpectedError
+ _symbolic $s8CameraUI20ChromeAnalyticsEventP
+ _symbolic $s8CameraUI24OrientationModelDelegateP
+ _symbolic $s8CameraUI25PublishingNameConvertibleP
+ _symbolic $s8CameraUI26PublishingValueConvertibleP
+ _symbolic 9EventKeys_____Qz 8CameraUI20ChromeAnalyticsEventP
+ _symbolic SS_So8NSObjectCt
+ _symbolic Say_____G 8CameraUI39ChromeAnalyticsEventControlPanelSessionC0E4KeysO
+ _symbolic Shy_____G 8CameraUI39ChromeAnalyticsEventControlPanelSessionC07ChangedF0O
+ _symbolic _____ 8CameraUI16OrientationModelC12YawReference33_066F33B1B548941972E875719D022C2CLLV
+ _symbolic _____ 8CameraUI39ChromeAnalyticsEventControlPanelSessionC
+ _symbolic _____ 8CameraUI39ChromeAnalyticsEventControlPanelSessionC07ChangedF0O
+ _symbolic _____ 8CameraUI39ChromeAnalyticsEventControlPanelSessionC0E4KeysO
+ _symbolic _____Sg 8CameraUI16OrientationModelC12YawReference33_066F33B1B548941972E875719D022C2CLLV
+ _symbolic _____Sg 8CameraUI39ChromeAnalyticsEventControlPanelSessionC
+ _symbolic _____SgXw 8CameraUI16OrientationModelC
+ _symbolic ______pSg 8CameraUI24OrientationModelDelegateP
+ _symbolic ______pSgXw 8CameraUI24OrientationModelDelegateP
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s11_SetStorageC 8CameraUI39ChromeAnalyticsEventControlPanelSessionC07ChangedH0O
+ _type_layout_string 8CameraUI16OrientationModelC12YawReference33_066F33B1B548941972E875719D022C2CLLV
- -[CAMCaptureCapabilities _disablePortraitBravoDevices]
- -[CAMCaptureCapabilities _disableSuperBravoDevice]
- GCC_except_table1322
- GCC_except_table1449
- GCC_except_table25
- _OBJC_IVAR_$_CAMCaptureCapabilities.__disablePortraitBravoDevices
- _OBJC_IVAR_$_CAMCaptureCapabilities.__disableSuperBravoDevice
- ___53-[CAMMotionController beginUpdatingOrientationModel:]_block_invoke
- ___block_descriptor_40_e8_32w_e8_v16?0q8lw32l8
- _block_copy_helper.116
- _block_descriptor.118
- _block_destroy_helper.117
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA4ViewPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAeAE15sensoryFeedback_7triggerQrAA07SensoryK0V_qd__tSQRd__lFQOyAeAE7gesture_9includingQrqd___AA11GestureMaskVtAA0P0Rd__lFQOyAeAE012simultaneousP0_ANQrqd___APtAaQRd__lFQOyACyAA6VStackVyAA05TupleE0VyAE06PhotosA6UICoreE6hiddenyQrSbFQOyACyACy06CameraB028ApplicationMaterialContainerVyACyACyAA6ZStackVyAVyACyACyACyAY20ChromeDynamicShutterVAA16_FixedSizeLayoutVGAA23_GeometryActionModifierVySo6CGRectVA10_SQ12CoreGraphicsyHCg_GGAY017DetectInteractionP8ModifierVG_AA6HStackVyAVyACyACyACyAY9ImageWellVAA22_MatchedGeometryEffectVySSGGAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGA15_G_AA6SpacerVtGGSgtGGAA14_PaddingLayoutVGA40_GGA40_GAY21ShutterAccessoryViewsVyAY20OrientationIndicatorVSgAA05EmptyE0VGG_Qo_Sg_A1_yAVyAA012_ConditionalD0VyACyACyACyACyACyACyAeAEAfgH_Qrqd___Sbyqd___qd__tctSQRd__lFQOyACyACyAeAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyA1_yA57_yACyACyAY026ChromeControlPanelExpandedD0VAY32ConditionalMatchedGeometryEffectVySSGGAA30_EnvironmentKeyWritingModifierVyAA0D12SizeCategoryOGGACyACyACyACyAY24ChromeBottomControlPanelVA66_GAA12_ScaleEffectVGA29_GAA01_Q15AlignmentEffectVyACyAA16RoundedRectangleVA66_GGGGSgGA29_G_Qo_AA31AccessibilityAttachmentModifierVGAA19_BackgroundModifierVyACyACyACyAeAE14materialEffect_2inQrAA0Z0V_AA9_ShapeSetVtFQOyAA5ColorV_Qo_A66_GA66_GA78_GGG_SbQo_A12_GA40_GA29_GAY26CapturingBurstHideModifierVGAY30CapturingFromTimerHideModifierVGAY0E17ModelHideModifierVGACyA51_A12_GG_ACyACyA57_yACyACyA105_AA12_FrameLayoutVGAA25_AllowsHitTestingModifierVGACyACyACyAeAE20accessibilityFocusedyQrAA23AccessibilityFocusStateV7BindingVySb_GFQOyACyAY12ModeWheelRowVyACyAA5GroupVyA57_yAY24GlassCircleElementButtonVACyACyA24_AA14_OpacityEffectVGA15_GGGA40_GACyA142_yA57_yACyACyACyACyA144_AY26RecordingVideoHideModifierVGA120_GAY25HideDuringQuietUIModifierVGAA32_EnvironmentKeyTransformModifierVySbGGACyACyA144_A146_GA15_GGGA40_GGA5_G_Qo_AA26_OverlayPreferenceModifierVyAY22ModeLoupePreferenceKeyVAA14GeometryReaderVyACyACyACyACyACyAY9ModeLoupeVA66_GA66_GA128_GAA15_PositionLayoutVGAA18_AnimationModifierVys11AnyHashableVSgGGGSgGGA186_ySbGGA123_GGA40_GA40_GtGGtGGAA01_D13ShapeModifierVyAA9RectangleVGG_AA06_EndedP0VyAA08_ChangedP0VyAA04DragP0VGGSgQo__A220_Qo__SiQo__SbQo__SbQo__SbQo__AY13ChromeElementOSgQo__SbQo__A229_Qo__SSSgQo_A196_GA196_GA186_yA11_7CGFloatVGGA239_GAaDHPA240_AaDHPA236_AaDHPA235_AaDHPqd0__AaDHD3_A234_HO_A196_AA0E8ModifierHPyHCHC_A196_AAA242_HPyHCHC_A239_AAA242_HPyHCHC_A239_AAA242_HPyHCHC.345
- _keypath_get.476Tm
- _keypath_get.511Tm
- _keypath_get.633Tm
- _keypath_get.663Tm
- _keypath_get.867Tm
- _keypath_set.402Tm
- _keypath_set.578Tm
- _objc_msgSend$_disablePortraitBravoDevices
- _objc_msgSend$_disableSuperBravoDevice
- _objc_msgSend$setInterfaceOrientationDidChange:
- _symbolic _____ 8CameraUI16OrientationModelC9Reference33_066F33B1B548941972E875719D022C2CLLV
- _symbolic _____Iegy_ So22UIInterfaceOrientationV
- _symbolic _____IeyBy_ So22UIInterfaceOrientationV
- _symbolic _____Sg 8CameraUI16OrientationModelC9Reference33_066F33B1B548941972E875719D022C2CLLV
- _symbolic _____ytIegnr_ So22UIInterfaceOrientationV
- _symbolic y_____cSg So22UIInterfaceOrientationV
- _type_layout_string 8CameraUI16OrientationModelC9Reference33_066F33B1B548941972E875719D022C2CLLV
CStrings:
+ " reference orientation "
+ " yaw reference: "
+ "@\"NSDictionary\"8@?0"
+ "CAMOrientationModelDelegate"
+ "Duplicate values for key: '"
+ "MotionController Configured New OrientationModel"
+ "MotionController Removed OrientationModel"
+ "Swift/Dictionary.swift"
+ "Swift/NativeDictionary.swift"
+ "T@\"<CAMOrientationModelDelegate>\",N,W"
+ "T@\"<CAMOrientationModelDelegate>\",N,W,V_delegate"
+ "TB,N,V_useOrientationModelOnlyWhileFlat"
+ "UIInterfaceOrientation.clockwiseOrder is missing one of the given orientations: Current - %s, Reference - %s"
+ "Update UI Orientation to: %@"
+ "Updated Orientation: "
+ "_TtC8CameraUI39ChromeAnalyticsEventControlPanelSession"
+ "_analyticsControlPanelSession"
+ "_beginUpdatingOrientationModel"
+ "_beginUpdatingOrientationModelIfNeeded"
+ "_didFullyProcessGravityReading"
+ "_endUpdatingOrientationModelIfNeeded"
+ "_flatBaselineYawReference"
+ "_shouldDisableModeForActiveCall:"
+ "_shouldEndUpdatingOrientationModel"
+ "_updateChromeWithOrientationModel"
+ "_useOrientationModelOnlyWhileFlat"
+ "actionMode"
+ "com.apple.cameraui"
+ "dualCapture"
+ "eventDomain"
+ "exposureBias"
+ "flash"
+ "isUpright"
+ "orientationModel:didChangeInterfaceOrientation:"
+ "portraitAperture"
+ "roughOrientationDidChange:"
+ "setNeedsReevaluateOrientationFromGravity"
+ "setUseOrientationModelOnlyWhileFlat:"
+ "set_delegate:"
+ "smartStyleDPad"
+ "smartStyleIntensity"
+ "smartStylePreset"
+ "smartStyleResetButton"
+ "torch"
+ "updateAnalyticsForUserChangedSmartStylePreset"
+ "useOrientationModelOnlyWhileFlat"
+ "v24@0:8@\"CAMOrientationModel\"16"
+ "v32@0:8@\"CAMOrientationModel\"16q24"
- "T@?,N,C"
- "TB,R,N,V__disablePortraitBravoDevices"
- "TB,R,N,V__disableSuperBravoDevice"
- "__disablePortraitBravoDevices"
- "__disableSuperBravoDevice"
- "_disablePortraitBravoDevices"
- "_disableSuperBravoDevice"
- "_interfaceOrientationDidChange"
- "_reference"
- "inferredInterfaceOrientation (flat/yaw): "
- "interfaceOrientationDidChange"
- "setInterfaceOrientationDidChange:"
- "set_interfaceOrientationDidChange:"

```
