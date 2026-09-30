## Pegasus

> `/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`

```diff

-297.0.0.0.0
-  __TEXT.__text: 0x42b04
+299.100.0.0.0
+  __TEXT.__text: 0x43520
   __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x43dc
-  __TEXT.__const: 0x1ea
+  __TEXT.__objc_methlist: 0x449c
+  __TEXT.__const: 0x212
   __TEXT.__cstring: 0x468e
   __TEXT.__oslogstring: 0x1acc
   __TEXT.__gcc_except_tab: 0x5e4
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__swift5_typeref: 0x1c
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__unwind_info: 0x1440
-  __TEXT.__objc_classname: 0x8b4
-  __TEXT.__objc_methname: 0xda63
-  __TEXT.__objc_methtype: 0x276b
-  __TEXT.__objc_stubs: 0x9060
+  __TEXT.__unwind_info: 0x1450
+  __TEXT.__objc_classname: 0x8d7
+  __TEXT.__objc_methname: 0xdce9
+  __TEXT.__objc_methtype: 0x281d
+  __TEXT.__objc_stubs: 0x9220
   __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x1bf0
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0x1c00
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b90
+  __DATA_CONST.__objc_selrefs: 0x2c08
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x558
-  __AUTH_CONST.__const: 0x438
+  __AUTH_CONST.__const: 0x458
   __AUTH_CONST.__cfstring: 0x2e20
-  __AUTH_CONST.__objc_const: 0xa988
+  __AUTH_CONST.__objc_const: 0xab08
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x5a4
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x5ac
   __DATA.__data: 0x970
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D15C6ABE-5409-3709-92D5-F43E395679F5
-  Functions: 1706
-  Symbols:   6508
-  CStrings:  3307
+  UUID: 6CF4FC76-2DE9-31C3-8C25-13D4EF977907
+  Functions: 1723
+  Symbols:   6563
+  CStrings:  3327
 
Symbols:
+ +[PGCABackdropLayerView blurFilters]
+ +[PGCABackdropLayerView blurFilters].cold.1
+ +[PGControlsViewLayoutMetrics sharedInstance]
+ +[PGPictureInPictureViewController contentCornerRadiusForViewSize:]
+ -[PGCABackdropLayerView initWithFrame:captureOnly:wantsGlassBackground:]
+ -[PGControlsViewLayoutMetrics _currentScaleForViewSize:]
+ -[PGControlsViewLayoutMetrics adjustedControlsAndPaddingScaleForViewSize:]
+ -[PGControlsViewLayoutMetrics adjustedSpacingScaleForViewSize:]
+ -[PGControlsViewLayoutMetrics concentricCornerRadiusForViewSize:]
+ -[PGControlsViewLayoutMetrics defaultActionButtonGlyphSize]
+ -[PGControlsViewLayoutMetrics defaultActionButtonSize]
+ -[PGControlsViewLayoutMetrics defaultControlsViewPadding]
+ -[PGControlsViewLayoutMetrics defaultPrerollIndicatorHeight]
+ -[PGControlsViewLayoutMetrics defaultPrerollLiveIndicatorPadding]
+ -[PGControlsViewLayoutMetrics defaultProgressIndicatorCompleteTrackPadding]
+ -[PGControlsViewLayoutMetrics defaultProgressIndicatorHeight]
+ -[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsGlyphSize]
+ -[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsSize]
+ -[PGControlsViewLayoutMetrics defaultSkipButtonsGlyphSize]
+ -[PGControlsViewLayoutMetrics defaultSkipButtonsSize]
+ -[PGControlsViewModel preferredMinimumHeight]
+ -[PGDimmingView initWithFrame:wantsGlassBackground:]
+ -[PGPictureInPictureController pictureInPictureRemoteObject:displayConfigurationForApplication:]
+ -[PGPictureInPictureRemoteObject sourceSceneSettingsDisplayConfiguration]
+ -[PGPictureInPictureViewController viewDidLayoutSubviews]
+ -[PGProgressIndicator customElapsedTrackTintColor]
+ -[PGProgressIndicator setCustomElapsedTrackTintColor:]
+ -[PGVibrantFillView hitTest:withEvent:]
+ -[PGVibrantFillView initWithFrame:wantsGlassBackground:]
+ -[PGVibrantFillView tintColorDidChange]
+ -[PGVibrantFillView(PGVibrancyEffects) PG_updateVibrancyEffectForTintColor]
+ GCC_except_table100
+ GCC_except_table160
+ GCC_except_table196
+ GCC_except_table221
+ GCC_except_table26
+ GCC_except_table266
+ GCC_except_table32
+ GCC_except_table94
+ _OBJC_CLASS_$_PGControlsViewLayoutMetrics
+ _OBJC_CLASS_$_PGVibrantFillView
+ _OBJC_IVAR_$_PGCABackdropLayerView._wantsGlassBackground
+ _OBJC_IVAR_$_PGDimmingView._wantsGlassBackground
+ _OBJC_IVAR_$_PGProgressIndicator._blurView
+ _OBJC_IVAR_$_PGProgressIndicator._customElapsedTrackTintColor
+ _OBJC_IVAR_$_PGVibrantFillView._wantsGlassBackground
+ _OBJC_METACLASS_$_PGControlsViewLayoutMetrics
+ _OBJC_METACLASS_$_PGVibrantFillView
+ __OBJC_$_CLASS_METHODS_PGControlsViewLayoutMetrics
+ __OBJC_$_INSTANCE_METHODS_PGControlsViewLayoutMetrics
+ __OBJC_$_INSTANCE_METHODS_PGVibrantFillView(PGVibrancyEffects)
+ __OBJC_$_INSTANCE_VARIABLES_PGDimmingView
+ __OBJC_$_INSTANCE_VARIABLES_PGVibrantFillView
+ __OBJC_$_PROP_LIST_PGControlsViewLayoutMetrics
+ __OBJC_CLASS_RO_$_PGControlsViewLayoutMetrics
+ __OBJC_CLASS_RO_$_PGVibrantFillView
+ __OBJC_METACLASS_RO_$_PGControlsViewLayoutMetrics
+ __OBJC_METACLASS_RO_$_PGVibrantFillView
+ ___36+[PGCABackdropLayerView blurFilters]_block_invoke
+ ___45+[PGControlsViewLayoutMetrics sharedInstance]_block_invoke
+ ___53-[PGPictureInPictureViewController setStashProgress:]_block_invoke.145
+ ___79-[PGPictureInPictureViewController performStartAnimated:withCompletionHandler:]_block_invoke.166
+ ___block_descriptor_48_e8_32s_e33_v16?0"FBSMutableSceneSettings"8ls32l8
+ ___block_descriptor_48_e8_32s_e35_v16?0"FBSMutableSceneParameters"8ls32l8
+ ___block_literal_global.115
+ ___block_literal_global.123
+ ___block_literal_global.23
+ _blurFilters.blurFilters
+ _blurFilters.onceToken
+ _objc_msgSend$_currentScaleForViewSize:
+ _objc_msgSend$adjustedControlsAndPaddingScaleForViewSize:
+ _objc_msgSend$adjustedSpacingScaleForViewSize:
+ _objc_msgSend$blurFilters
+ _objc_msgSend$concentricCornerRadiusForViewSize:
+ _objc_msgSend$customElapsedTrackTintColor
+ _objc_msgSend$defaultActionButtonGlyphSize
+ _objc_msgSend$defaultActionButtonSize
+ _objc_msgSend$defaultControlsViewPadding
+ _objc_msgSend$defaultPrerollIndicatorHeight
+ _objc_msgSend$defaultPrerollLiveIndicatorPadding
+ _objc_msgSend$defaultProgressIndicatorCompleteTrackPadding
+ _objc_msgSend$defaultProgressIndicatorHeight
+ _objc_msgSend$defaultRestoreCancelButtonsGlyphSize
+ _objc_msgSend$defaultRestoreCancelButtonsSize
+ _objc_msgSend$defaultSkipButtonsGlyphSize
+ _objc_msgSend$defaultSkipButtonsSize
+ _objc_msgSend$initWithFrame:captureOnly:wantsGlassBackground:
+ _objc_msgSend$pictureInPictureController:displayConfigurationForApplication:
+ _objc_msgSend$pictureInPictureRemoteObject:displayConfigurationForApplication:
+ _objc_msgSend$setCustomElapsedTrackTintColor:
+ _objc_msgSend$sourceSceneSettingsDisplayConfiguration
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- -[PGCABackdropLayerView initWithCoder:]
- -[PGCABackdropLayerView initWithFrame:]
- -[PGCABackdropLayerView initWithFrame:captureOnly:]
- -[PGControlsContainerView _setControlsHidden:animated:]
- -[PGControlsContainerView viewModel]
- -[PGControlsView updateControlsHidden]
- -[PGDimmingView initWithFrame:]
- -[PGFillView .cxx_destruct]
- -[PGFillView fillColor]
- -[PGFillView hitTest:withEvent:]
- -[PGFillView initWithFrame:wantsGlassBackground:]
- -[PGFillView setFillColor:]
- -[PGFillView(PGVibrancyEffects) PG_updateVibrancyEffectForTintColor]
- -[PGPictureInPictureViewController preferredMinimumWidth]
- -[PGProgressIndicator customElapsedTrackFillColor]
- -[PGProgressIndicator setCustomElapsedTrackFillColor:]
- GCC_except_table159
- GCC_except_table161
- GCC_except_table195
- GCC_except_table220
- GCC_except_table265
- GCC_except_table28
- GCC_except_table34
- GCC_except_table93
- GCC_except_table99
- _OBJC_CLASS_$_PGFillView
- _OBJC_IVAR_$_PGFillView._fillColor
- _OBJC_IVAR_$_PGFillView._wantsGlassBackground
- _OBJC_IVAR_$_PGProgressIndicator._customElapsedTrackFillColor
- _OBJC_METACLASS_$_PGFillView
- __OBJC_$_INSTANCE_METHODS_PGFillView(PGVibrancyEffects)
- __OBJC_$_INSTANCE_VARIABLES_PGFillView
- __OBJC_$_PROP_LIST_PGFillView
- __OBJC_CLASS_RO_$_PGFillView
- __OBJC_METACLASS_RO_$_PGFillView
- ___53-[PGPictureInPictureViewController setStashProgress:]_block_invoke.144
- ___79-[PGPictureInPictureViewController performStartAnimated:withCompletionHandler:]_block_invoke.165
- ___block_descriptor_40_e35_v16?0"FBSMutableSceneParameters"8l
- ___block_literal_global.117
- ___block_literal_global.124
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Pegasus
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Pegasus
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Pegasus
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Pegasus
- _objc_msgSend$_setControlsHidden:animated:
- _objc_msgSend$colorWithAlphaComponent:
- _objc_msgSend$customElapsedTrackFillColor
- _objc_msgSend$initWithFrame:captureOnly:
- _objc_msgSend$lightGrayColor
- _objc_msgSend$setCustomElapsedTrackFillColor:
- _objc_msgSend$setFillColor:
- _objc_msgSend$systemBlackColor
CStrings:
+ "@\"FBSDisplayConfiguration\"32@0:8@\"PGPictureInPictureRemoteObject\"16@\"PGPictureInPictureApplication\"24"
+ "@\"PGVibrantFillView\""
+ "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48B52"
+ "A"
+ "PGControlsViewLayoutMetrics"
+ "PGVibrantFillView"
+ "T@\"FBSDisplayConfiguration\",R,N"
+ "T@\"UIColor\",&,N,V_customElapsedTrackTintColor"
+ "T{CGSize=dd},R,N"
+ "_blurView"
+ "_currentScaleForViewSize:"
+ "_customElapsedTrackTintColor"
+ "adjustedControlsAndPaddingScaleForViewSize:"
+ "adjustedSpacingScaleForViewSize:"
+ "blurFilters"
+ "concentricCornerRadiusForViewSize:"
+ "contentCornerRadiusForViewSize:"
+ "customElapsedTrackTintColor"
+ "d32@0:8{CGSize=dd}16"
+ "defaultActionButtonGlyphSize"
+ "defaultActionButtonSize"
+ "defaultControlsViewPadding"
+ "defaultPrerollIndicatorHeight"
+ "defaultPrerollLiveIndicatorPadding"
+ "defaultProgressIndicatorCompleteTrackPadding"
+ "defaultProgressIndicatorHeight"
+ "defaultRestoreCancelButtonsGlyphSize"
+ "defaultRestoreCancelButtonsSize"
+ "defaultSkipButtonsGlyphSize"
+ "defaultSkipButtonsSize"
+ "initWithFrame:captureOnly:wantsGlassBackground:"
+ "pictureInPictureController:displayConfigurationForApplication:"
+ "pictureInPictureRemoteObject:displayConfigurationForApplication:"
+ "preferredMinimumHeight"
+ "setCustomElapsedTrackTintColor:"
+ "sourceSceneSettingsDisplayConfiguration"
+ "viewDidLayoutSubviews"
- "1"
- "@\"PGFillView\""
- "PGFillView"
- "T@\"UIColor\",&,N,V_customElapsedTrackFillColor"
- "T@\"UIColor\",C,N,V_fillColor"
- "_customElapsedTrackFillColor"
- "_fillColor"
- "_setControlsHidden:animated:"
- "colorWithAlphaComponent:"
- "customElapsedTrackFillColor"
- "fillColor"
- "initWithFrame:captureOnly:"
- "lightGrayColor"
- "setCustomElapsedTrackFillColor:"
- "setFillColor:"
- "systemBlackColor"
- "updateControlsHidden"

```
