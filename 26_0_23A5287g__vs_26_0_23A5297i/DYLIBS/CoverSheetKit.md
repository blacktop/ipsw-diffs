## CoverSheetKit

> `/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit`

```diff

-101.100.0.0.0
-  __TEXT.__text: 0x34bf8
-  __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x27bc
-  __TEXT.__const: 0x1e04
-  __TEXT.__cstring: 0xd97
-  __TEXT.__gcc_except_tab: 0x19c
+104.101.0.0.0
+  __TEXT.__text: 0x34364
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_methlist: 0x28e4
+  __TEXT.__const: 0x1cb4
+  __TEXT.__cstring: 0xde7
+  __TEXT.__gcc_except_tab: 0x1c8
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__oslogstring: 0x1c8
   __TEXT.__ustring: 0x14
-  __TEXT.__constg_swiftt: 0x9c8
-  __TEXT.__swift5_typeref: 0x16bb
-  __TEXT.__swift5_fieldmd: 0x464
-  __TEXT.__swift5_types: 0x64
+  __TEXT.__constg_swiftt: 0x9fc
+  __TEXT.__swift5_typeref: 0x16c9
+  __TEXT.__swift5_fieldmd: 0x48c
+  __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_reflstr: 0x3a3
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x84
+  __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf68
-  __TEXT.__eh_frame: 0x220
-  __TEXT.__objc_classname: 0x44d
-  __TEXT.__objc_methname: 0x7f76
-  __TEXT.__objc_methtype: 0x128b
-  __TEXT.__objc_stubs: 0x5780
-  __DATA_CONST.__got: 0x548
-  __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__eh_frame: 0x228
+  __TEXT.__objc_classname: 0x476
+  __TEXT.__objc_methname: 0x8415
+  __TEXT.__objc_methtype: 0x1317
+  __TEXT.__objc_stubs: 0x59c0
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc0
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_selrefs: 0x1e98
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH_CONST.__const: 0x1e30
+  __AUTH_CONST.__auth_got: 0x9c0
+  __AUTH_CONST.__const: 0x1ed0
   __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x4558
+  __AUTH_CONST.__objc_const: 0x47d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xae8
-  __AUTH.__data: 0x518
-  __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x748
-  __DATA.__bss: 0x1350
+  __AUTH.__objc_data: 0xb48
+  __AUTH.__data: 0x520
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__data: 0x758
+  __DATA.__bss: 0x1450
   __DATA.__common: 0x180
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 036240C7-ECDA-3330-82F8-CB1896E58D2E
-  Functions: 1509
-  Symbols:   3335
-  CStrings:  1692
+  UUID: 248D3A29-7E71-3199-A4F9-1A32F377E2D5
+  Functions: 1550
+  Symbols:   3429
+  CStrings:  1746
 
Symbols:
+ +[CSProminentLayoutController _subtitleElementBoundingTopY]
+ +[CSProminentLayoutController _subtitleElementFontSize]
+ +[CSProminentLayoutController subtitleElementBoundingHeight]
+ -[CSProminentButtonControl glassLuminanceValue]
+ -[CSProminentButtonControl setGlassLuminanceValue:]
+ -[CSProminentButtonsView glassLuminanceValue]
+ -[CSProminentButtonsView setGlassLuminanceValue:]
+ -[CSProminentDisplayTransientSubtitle .cxx_destruct]
+ -[CSProminentDisplayTransientSubtitle displayDate]
+ -[CSProminentDisplayTransientSubtitle displayDuration]
+ -[CSProminentDisplayTransientSubtitle initWithText:priority:displayDuration:]
+ -[CSProminentDisplayTransientSubtitle priority]
+ -[CSProminentDisplayTransientSubtitle setDisplayDate:]
+ -[CSProminentDisplayTransientSubtitle setDisplayDuration:]
+ -[CSProminentDisplayTransientSubtitle text]
+ -[CSProminentDisplayViewController _reevaluateTransientSubtitle]
+ -[CSProminentDisplayViewController _setTransientSubtitle:timeout:]
+ -[CSProminentDisplayViewController activeTransientSubtitleTimer]
+ -[CSProminentDisplayViewController activeTransientSubtitle]
+ -[CSProminentDisplayViewController clearTransientSubtitleForPriority:]
+ -[CSProminentDisplayViewController requestedTransientSubtitles]
+ -[CSProminentDisplayViewController setActiveTransientSubtitle:]
+ -[CSProminentDisplayViewController setActiveTransientSubtitleTimer:]
+ -[CSProminentDisplayViewController setRequestedTransientSubtitles:]
+ -[CSProminentDisplayViewController setTransientSubtitleText:priority:timeout:]
+ -[CSProminentLayoutController _complicationRowHorizontalReticleInsetWithBoundingRect:]
+ -[CSProminentLayoutController _complicationRowVerticalReticleInsetWithBoundingRect:]
+ -[CSProminentLayoutController complicationElementEditingOffsetWithBoundingRect:]
+ -[CSProminentLayoutController subtitleElementEditingOffsetWithBoundingRect:]
+ -[CSProminentTimeView _selectFontForTextHeight:updatingState:]
+ GCC_except_table103
+ GCC_except_table111
+ GCC_except_table59
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CSProminentDisplayTransientSubtitle
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$_CSProminentButtonControl._glassLuminanceValue
+ _OBJC_IVAR_$_CSProminentButtonsView._glassLuminanceValue
+ _OBJC_IVAR_$_CSProminentDisplayTransientSubtitle._displayDate
+ _OBJC_IVAR_$_CSProminentDisplayTransientSubtitle._displayDuration
+ _OBJC_IVAR_$_CSProminentDisplayTransientSubtitle._priority
+ _OBJC_IVAR_$_CSProminentDisplayTransientSubtitle._text
+ _OBJC_IVAR_$_CSProminentDisplayViewController._activeTransientSubtitle
+ _OBJC_IVAR_$_CSProminentDisplayViewController._activeTransientSubtitleTimer
+ _OBJC_IVAR_$_CSProminentDisplayViewController._requestedTransientSubtitles
+ _OBJC_IVAR_$_CSProminentTimeView._adaptiveBaseFont
+ _OBJC_METACLASS_$_CSProminentDisplayTransientSubtitle
+ __OBJC_$_INSTANCE_METHODS_CSProminentDisplayTransientSubtitle
+ __OBJC_$_INSTANCE_VARIABLES_CSProminentDisplayTransientSubtitle
+ __OBJC_$_PROP_LIST_CSProminentDisplayTransientSubtitle
+ __OBJC_CLASS_RO_$_CSProminentDisplayTransientSubtitle
+ __OBJC_METACLASS_RO_$_CSProminentDisplayTransientSubtitle
+ ___51-[CSProminentTimeView setUsesLightTimeFontVariant:]_block_invoke_3
+ ___64-[CSProminentDisplayViewController _reevaluateTransientSubtitle]_block_invoke
+ ___66-[CSProminentDisplayViewController _setTransientSubtitle:timeout:]_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSTimer"8lw40l8s32l8
+ ___block_literal_global.53
+ ___swift_memcpy9_8
+ _associated conformance 13CoverSheetKit14TitleLabelViewV11CoordinatorC10TextUpdateVSHAASQ
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewP20TextAnimationSupportE27textGlassWipeTransitionTint5colorQrAA5ColorVSg_tFQOyAeFE0ijkL8AnimatedyQrSbFQOyAA0F0VAFE0ijkL09alignmentQrAA19HorizontalAlignmentV_tFQOy_Qo__Qo__Qo_ANGAaDHPqd__AaDHD2_AUHO_AnaDHPyHCHC.56
+ _get_witness_table 7SwiftUI19_ConditionalContentVyACyAA6HStackVyAA9TupleViewVyAA6ZStackVyAGyAA08ModifiedD0VyACyAKyAKyAKyAKyAKyACyAA0G0P20TextAnimationSupportE27textGlassWipeTransitionTint5colorQrAA5ColorVSg_tFQOyAmNE0mnoP8AnimatedyQrSbFQOyAA0J0VANE0mnoP09alignmentQrAA19HorizontalAlignmentV_tFQOy_Qo__Qo__Qo_AVGAA30_SafeAreaRegionsIgnoringLayoutVGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGA7_y12CoreGraphics7CGFloatVGGA7_ySiSgGGAA16_FixedSizeLayoutVGAKyA23_AA24_ForegroundStyleModifierVyARGGGAA14_OpacityEffectVG_AKyAKyAKyAKyAKyAKyAKyA2_A26_GA4_GA11_GA16_GA19_GA22_GA30_GtGG_AA6SpacerVtGGAEyAGyA42__A40_tGGGA40_GAaLHPA47_AaLHPA44_AaLHPyHC_A46_AaLHPyHCHC_A40_AaLHPyHCHC.54
+ _get_witness_table 7SwiftUI4ViewRzlAA19_ConditionalContentVyxAA08ModifiedE0VyxAA24_ForegroundStyleModifierVyAA5ColorVGGGAaBHPxAaBHD1__AlaBHPxAaBHD1__AkA0cI0HPyHCHCHC.55
+ _objc_msgSend$_complicationRowHorizontalReticleInsetWithBoundingRect:
+ _objc_msgSend$_complicationRowVerticalReticleInsetWithBoundingRect:
+ _objc_msgSend$_reevaluateTransientSubtitle
+ _objc_msgSend$_selectFontForTextHeight:updatingState:
+ _objc_msgSend$_setTransientSubtitle:timeout:
+ _objc_msgSend$_subtitleElementBoundingTopY
+ _objc_msgSend$_subtitleElementFontSize
+ _objc_msgSend$adaptiveBaseFont
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$allKeys
+ _objc_msgSend$complicationElementEditingOffsetWithBoundingRect:
+ _objc_msgSend$cs_setLockPickGlassBackgroundWithLuminance:
+ _objc_msgSend$displayDate
+ _objc_msgSend$displayDuration
+ _objc_msgSend$glassLuminanceValue
+ _objc_msgSend$initWithText:priority:displayDuration:
+ _objc_msgSend$invalidate
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$now
+ _objc_msgSend$priority
+ _objc_msgSend$reticleSpacing
+ _objc_msgSend$setDisplayDuration:
+ _objc_msgSend$setGlassLuminanceValue:
+ _objc_msgSend$setTransientSubtitleText:priority:timeout:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$subtitleElementEditingOffsetWithBoundingRect:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timerWithTimeInterval:repeats:block:
+ _symbolic _____ 13CoverSheetKit14TitleLabelViewV11CoordinatorC10TextUpdateV
+ _type_layout_string 13CoverSheetKit14TitleLabelViewV11CoordinatorC10TextUpdateV
- +[CSProminentLayoutController complicationElementEditingOffset]
- +[CSProminentLayoutController landscapePadTimeElementBoundingTopY]
- +[CSProminentLayoutController subtitleElementBoundingTopY]
- +[CSProminentLayoutController subtitleElementFontSize]
- -[CSProminentLayoutController subtitleElementBoundingHeight]
- -[CSProminentLayoutController subtitleElementEditingOffset]
- GCC_except_table106
- GCC_except_table38
- GCC_except_table93
- _UIFontWeightMedium
- ___73-[CSProminentDisplayViewController setTransientSubtitleText:withTimeout:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- _dispatch_after
- _dispatch_time
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewP20TextAnimationSupportE27textGlassWipeTransitionTint5colorQrAA5ColorVSg_tFQOyAeFE0ijkL8AnimatedyQrSbFQOyAA0F0VAFE0ijkL09alignmentQrAA19HorizontalAlignmentV_tFQOy_Qo__Qo__Qo_ANGAaDHPqd__AaDHD2_AUHO_AnaDHPyHCHC.53
- _get_witness_table 7SwiftUI19_ConditionalContentVyACyAA6HStackVyAA9TupleViewVyAA6ZStackVyAGyAA08ModifiedD0VyACyAKyAKyAKyAKyAKyACyAA0G0P20TextAnimationSupportE27textGlassWipeTransitionTint5colorQrAA5ColorVSg_tFQOyAmNE0mnoP8AnimatedyQrSbFQOyAA0J0VANE0mnoP09alignmentQrAA19HorizontalAlignmentV_tFQOy_Qo__Qo__Qo_AVGAA30_SafeAreaRegionsIgnoringLayoutVGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGA7_y12CoreGraphics7CGFloatVGGA7_ySiSgGGAA16_FixedSizeLayoutVGAKyA23_AA24_ForegroundStyleModifierVyARGGGAA14_OpacityEffectVG_AKyAKyAKyAKyAKyAKyAKyA2_A26_GA4_GA11_GA16_GA19_GA22_GA30_GtGG_AA6SpacerVtGGAEyAGyA42__A40_tGGGA40_GAaLHPA47_AaLHPA44_AaLHPyHC_A46_AaLHPyHCHC_A40_AaLHPyHCHC.51
- _get_witness_table 7SwiftUI4ViewRzlAA19_ConditionalContentVyxAA08ModifiedE0VyxAA24_ForegroundStyleModifierVyAA5ColorVGGGAaBHPxAaBHD1__AlaBHPxAaBHD1__AkA0cI0HPyHCHCHC.52
- _objc_msgSend$_isSalvadorEnabled
- _objc_msgSend$_landscapeReductionFactor
- _objc_msgSend$_maximumTimeElementFontSize
- _objc_msgSend$_minimumTimeElementFontSize
- _objc_msgSend$complicationElementEditingOffset
- _objc_msgSend$cs_setLockPickGlassBackground
- _objc_msgSend$setTransientSubtitleText:
- _objc_msgSend$subtitleElementBoundingTopY
- _objc_msgSend$subtitleElementEditingOffset
- _objc_msgSend$subtitleElementFontSize
- _objc_release_x28
CStrings:
+ "@\"CSProminentDisplayTransientSubtitle\""
+ "@\"NSTimer\""
+ "@28@0:8d16B24"
+ "@40@0:8@16q24d32"
+ "CSProminentDisplayTransientSubtitle"
+ "T@\"CSProminentDisplayTransientSubtitle\",&,N,V_activeTransientSubtitle"
+ "T@\"NSMutableDictionary\",&,N,V_requestedTransientSubtitles"
+ "T@\"NSString\",R,N,V_text"
+ "T@\"NSTimer\",&,N,V_activeTransientSubtitleTimer"
+ "T@\"UIFont\",N,R"
+ "Td,N,V_displayDuration"
+ "Td,N,V_glassLuminanceValue"
+ "Tq,R,N,V_priority"
+ "_activeTransientSubtitle"
+ "_activeTransientSubtitleTimer"
+ "_adaptiveBaseFont"
+ "_complicationRowHorizontalReticleInsetWithBoundingRect:"
+ "_complicationRowVerticalReticleInsetWithBoundingRect:"
+ "_displayDuration"
+ "_glassLuminanceValue"
+ "_priority"
+ "_reevaluateTransientSubtitle"
+ "_requestedTransientSubtitles"
+ "_selectFontForTextHeight:updatingState:"
+ "_setTransientSubtitle:timeout:"
+ "_subtitleElementBoundingTopY"
+ "_subtitleElementFontSize"
+ "_text"
+ "_textUpdate"
+ "activeTransientSubtitle"
+ "activeTransientSubtitleTimer"
+ "adaptiveBaseFont"
+ "addTimer:forMode:"
+ "allKeys"
+ "clearTransientSubtitleForPriority:"
+ "complicationElementEditingOffsetWithBoundingRect:"
+ "cs_setLockPickGlassBackgroundWithLuminance:"
+ "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "displayDuration"
+ "glassLuminanceValue"
+ "initWithText:priority:displayDuration:"
+ "invalidate"
+ "mainRunLoop"
+ "now"
+ "priority"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "requestedTransientSubtitles"
+ "setActiveTransientSubtitle:"
+ "setActiveTransientSubtitleTimer:"
+ "setDisplayDuration:"
+ "setGlassLuminanceValue:"
+ "setRequestedTransientSubtitles:"
+ "setTransientSubtitleText:priority:timeout:"
+ "sortedArrayUsingComparator:"
+ "subtitleElementEditingOffsetWithBoundingRect:"
+ "timeIntervalSinceNow"
+ "timerWithTimeInterval:repeats:block:"
+ "v16@?0@\"NSTimer\"8"
+ "v20@0:8f16"
+ "v40@0:8@16q24d32"
- "_attributedText"
- "complicationElementEditingOffset"
- "cs_setLockPickGlassBackground"
- "landscapePadTimeElementBoundingTopY"
- "subtitleElementBoundingTopY"
- "subtitleElementEditingOffset"
- "subtitleElementFontSize"

```
