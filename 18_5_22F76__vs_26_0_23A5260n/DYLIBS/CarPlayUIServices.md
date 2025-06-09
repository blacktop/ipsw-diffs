## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-385.24.1.0.0
-  __TEXT.__text: 0x19f8c
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x2b1c
-  __TEXT.__const: 0xc8
+512.2.4.0.0
+  __TEXT.__text: 0x1ae40
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x2c54
+  __TEXT.__const: 0x178
   __TEXT.__oslogstring: 0xc48
-  __TEXT.__cstring: 0x12e1
+  __TEXT.__cstring: 0x13e4
   __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__unwind_info: 0x898
-  __TEXT.__objc_classname: 0xe30
-  __TEXT.__objc_methname: 0x551c
-  __TEXT.__objc_methtype: 0x124c
-  __TEXT.__objc_stubs: 0x3900
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x830
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__unwind_info: 0x900
+  __TEXT.__objc_classname: 0xe9d
+  __TEXT.__objc_methname: 0x5991
+  __TEXT.__objc_methtype: 0x12c3
+  __TEXT.__objc_stubs: 0x3c00
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1478
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x168
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0xe6b8
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x2fc
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__objc_const: 0xedc8
+  __AUTH_CONST.__objc_doubleobj: 0x80
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x31c
   __DATA.__data: 0xea8
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x1590

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9383C832-CFF8-3844-8487-39188C890D42
-  Functions: 885
-  Symbols:   3847
-  CStrings:  1569
+  UUID: F079921A-8A68-3F0C-A9B4-C8B1E30A2C40
+  Functions: 913
+  Symbols:   3986
+  CStrings:  1636
 
Symbols:
+ +[CRSUIWallpaperDimmingView layerClass]
+ +[UIImage(CarPlayUIServices) crsui_nowPlayingIconImageWthTraitCollection:]
+ +[UIImage(CarPlayUIServices) crsui_symbolImageNamed:tintColor:compatibleWithTraitCollection:]
+ -[CRSUIClimateOverlaySceneClientSettings isOverlayHidden]
+ -[CRSUIClimateOverlaySceneSettings primaryDockFrame]
+ -[CRSUIClimateOverlaySceneSettings secondaryDockFrame]
+ -[CRSUIClimateQuickControlRequestAction initWithClimateZone:]
+ -[CRSUIClimateQuickControlRequestActionHandler .cxx_destruct]
+ -[CRSUIClimateQuickControlRequestActionHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]
+ -[CRSUIClimateQuickControlRequestActionHandler delegate]
+ -[CRSUIClimateQuickControlRequestActionHandler initWithDelegate:]
+ -[CRSUIClimateQuickControlRequestActionHandler setDelegate:]
+ -[CRSUIMutableClimateOverlaySceneClientSettings isOverlayHidden]
+ -[CRSUIMutableClimateOverlaySceneClientSettings setIsOverlayHidden:]
+ -[CRSUIMutableClimateOverlaySceneSettings primaryDockFrame]
+ -[CRSUIMutableClimateOverlaySceneSettings secondaryDockFrame]
+ -[CRSUIMutableClimateOverlaySceneSettings setPrimaryDockFrame:]
+ -[CRSUIMutableClimateOverlaySceneSettings setSecondaryDockFrame:]
+ -[CRSUIMutableWallpaperSceneSettings isDimmed]
+ -[CRSUIMutableWallpaperSceneSettings setIsDimmed:]
+ -[CRSUIWallpaperDimmingView .cxx_destruct]
+ -[CRSUIWallpaperDimmingView initWithFrame:]
+ -[CRSUIWallpaperDimmingView setDim:animated:]
+ -[CRSUIWallpaperDimmingView setUseDimStyle:]
+ -[CRSUIWallpaperSceneSettings isDimmed]
+ -[UITraitCollection(CarPlayUIServices) iconStyledUserInterfaceStyle]
+ _BSSettingFlagForBool
+ _CRSUIWallpaper2025Blue
+ _OBJC_CLASS_$_CABackdropLayer
+ _OBJC_CLASS_$_CAFilter
+ _OBJC_CLASS_$_CRSUIClimateQuickControlRequestAction
+ _OBJC_CLASS_$_CRSUIClimateQuickControlRequestActionHandler
+ _OBJC_CLASS_$_CRSUIWallpaperDimmingView
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_IVAR_$_CRSUIClimateQuickControlRequestActionHandler._delegate
+ _OBJC_IVAR_$_CRSUIMutableClimateOverlaySceneSettings._primaryDockFrame
+ _OBJC_IVAR_$_CRSUIMutableClimateOverlaySceneSettings._secondaryDockFrame
+ _OBJC_IVAR_$_CRSUIMutableWallpaperSceneSettings._isDimmed
+ _OBJC_IVAR_$_CRSUIWallpaperDimmingView._currentDimStyle
+ _OBJC_IVAR_$_CRSUIWallpaperDimmingView._dimmingColorMatrixFilter
+ _OBJC_IVAR_$_CRSUIWallpaperDimmingView._luminanceCurveMapFilter
+ _OBJC_IVAR_$_CRSUIWallpaperDimmingView._saturationFilter
+ _OBJC_METACLASS_$_CRSUIClimateQuickControlRequestAction
+ _OBJC_METACLASS_$_CRSUIClimateQuickControlRequestActionHandler
+ _OBJC_METACLASS_$_CRSUIWallpaperDimmingView
+ _UIRectFill
+ __OBJC_$_CLASS_METHODS_CRSUIWallpaperDimmingView
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateQuickControlRequestAction
+ __OBJC_$_INSTANCE_METHODS_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_$_INSTANCE_METHODS_CRSUIWallpaperDimmingView
+ __OBJC_$_INSTANCE_METHODS_UITraitCollection(CRSUITraits|CarPlayUIServices)
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIMutableClimateOverlaySceneSettings
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIWallpaperDimmingView
+ __OBJC_$_PROP_LIST_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_CLASS_RO_$_CRSUIClimateQuickControlRequestAction
+ __OBJC_CLASS_RO_$_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_CLASS_RO_$_CRSUIWallpaperDimmingView
+ __OBJC_METACLASS_RO_$_CRSUIClimateQuickControlRequestAction
+ __OBJC_METACLASS_RO_$_CRSUIClimateQuickControlRequestActionHandler
+ __OBJC_METACLASS_RO_$_CRSUIWallpaperDimmingView
+ ___110-[CRSUIClimateQuickControlRequestActionHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke
+ ___110-[CRSUIClimateQuickControlRequestActionHandler _respondToActions:forFBSScene:inUIScene:fromTransitionContext:]_block_invoke_2
+ ___45-[CRSUIWallpaperDimmingView setDim:animated:]_block_invoke
+ ___74+[UIImage(CarPlayUIServices) crsui_nowPlayingIconImageWthTraitCollection:]_block_invoke
+ ___93+[UIImage(CarPlayUIServices) crsui_symbolImageNamed:tintColor:compatibleWithTraitCollection:]_block_invoke
+ ___block_descriptor_40_e8_32s_e27_v16?0"<UIMutableTraits>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e51_v24?0"CRSUIClimateQuickControlRequestAction"8^B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ _kCAFilterColorMatrix
+ _kCAFilterColorSaturate
+ _kCAFilterInputAmount
+ _kCAFilterInputColorMatrix
+ _kCAFilterInputValues
+ _kCAFilterLuminanceCurveMap
+ _objc_msgSend$CGRectValue
+ _objc_msgSend$_animateUsingSpringWithDuration:delay:options:mass:stiffness:damping:initialVelocity:animations:completion:
+ _objc_msgSend$appearanceType
+ _objc_msgSend$boolForSetting:
+ _objc_msgSend$drawInRect:blendMode:alpha:
+ _objc_msgSend$filterWithType:
+ _objc_msgSend$iconStyledUserInterfaceStyle
+ _objc_msgSend$imageWithActions:
+ _objc_msgSend$imageWithTintColor:
+ _objc_msgSend$initWithSize:
+ _objc_msgSend$requestQuickControl:
+ _objc_msgSend$sbh_iconImageAppearance
+ _objc_msgSend$setFill
+ _objc_msgSend$setFilters:
+ _objc_msgSend$setFlag:forSetting:
+ _objc_msgSend$setName:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setUseDimStyle:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$systemImageNamed:
+ _objc_msgSend$traitCollectionByModifyingTraits:
+ _objc_msgSend$valueWithCAColorMatrix:
+ _objc_msgSend$valueWithCGRect:
- -[CRSUIClimateOverlaySceneSettings containerHeight]
- -[CRSUIMutableClimateOverlaySceneSettings containerHeight]
- -[CRSUIMutableClimateOverlaySceneSettings setContainerHeight:]
- _CRSUIWallpaperRedBlueDynamic
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UITraitCollection_$_CRSUITraits
CStrings:
+ "@\"<CRSUIClimateQuickControlRequestActionDelegate>\""
+ "@\"CAFilter\""
+ "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "CARWallpaper2025BlueDynamic"
+ "CGRectValue"
+ "CRSUIClimateQuickControlRequestAction"
+ "CRSUIClimateQuickControlRequestActionHandler"
+ "CRSUIWallpaperDimmingView"
+ "CarDisplayCanvasIcon-com.apple.cardisplay.nowplaying"
+ "DIMMING_COLOR_MATRIX"
+ "DIMMING_LUMINANCE_CURVE_MAP"
+ "DIMMING_SATURATION"
+ "T@\"<CRSUIClimateQuickControlRequestActionDelegate>\",W,N,V_delegate"
+ "TB,N,V_isDimmed"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_primaryDockFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_secondaryDockFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
+ "Wallpaper2025Blue"
+ "WallpaperCell2025Blue"
+ "_animateUsingSpringWithDuration:delay:options:mass:stiffness:damping:initialVelocity:animations:completion:"
+ "_currentDimStyle"
+ "_dimmingColorMatrixFilter"
+ "_isDimmed"
+ "_luminanceCurveMapFilter"
+ "_primaryDockFrame"
+ "_saturationFilter"
+ "_secondaryDockFrame"
+ "appearanceType"
+ "boolForSetting:"
+ "crsui_nowPlayingIconImageWthTraitCollection:"
+ "crsui_symbolImageNamed:tintColor:compatibleWithTraitCollection:"
+ "drawInRect:blendMode:alpha:"
+ "filterWithType:"
+ "i"
+ "iconStyledUserInterfaceStyle"
+ "imageWithActions:"
+ "imageWithTintColor:"
+ "initWithClimateZone:"
+ "initWithSize:"
+ "inputAmount"
+ "isDimmed"
+ "isOverlayHidden"
+ "layerClass"
+ "primaryDockFrame"
+ "requestQuickControl:"
+ "sbh_iconImageAppearance"
+ "secondaryDockFrame"
+ "setDim:animated:"
+ "setFill"
+ "setFilters:"
+ "setFlag:forSetting:"
+ "setIsDimmed:"
+ "setIsOverlayHidden:"
+ "setName:"
+ "setOpacity:"
+ "setPrimaryDockFrame:"
+ "setSecondaryDockFrame:"
+ "setUseDimStyle:"
+ "setUserInterfaceStyle:"
+ "setValue:forKey:"
+ "systemImageNamed:"
+ "traitCollectionByModifyingTraits:"
+ "v16@?0@\"<UIMutableTraits>\"8"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
+ "v24@?0@\"CRSUIClimateQuickControlRequestAction\"8^B16"
+ "v28@0:8d16B24"
+ "valueWithCAColorMatrix:"
+ "valueWithCGRect:"
- "CARWallpaperRedBlueDynamic"
- "T@\"NSNumber\",&,N"
- "WallpaperCellRedBlue"
- "WallpaperRedBlue"
- "containerHeight"
- "setContainerHeight:"

```
