## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.10.111.0
-  __TEXT.__text: 0xa85708
-  __TEXT.__auth_stubs: 0x5530
+4557.0.10.114.0
+  __TEXT.__text: 0xa88254
+  __TEXT.__auth_stubs: 0x5570
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7a48
-  __TEXT.__const: 0x12cf0
-  __TEXT.__oslogstring: 0x5e502
-  __TEXT.__cstring: 0x7cdcb
+  __TEXT.__objc_methlist: 0xb7b70
+  __TEXT.__const: 0x12fa0
+  __TEXT.__oslogstring: 0x5e54c
+  __TEXT.__cstring: 0x7ce29
   __TEXT.__gcc_except_tab: 0x17898
-  __TEXT.__ustring: 0xcac
+  __TEXT.__ustring: 0xcf4
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c0e8
+  __TEXT.__unwind_info: 0x2c118
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x220c0
-  __TEXT.__objc_methname: 0x1ceda5
+  __TEXT.__objc_classname: 0x2211b
+  __TEXT.__objc_methname: 0x1cf260
   __TEXT.__objc_methtype: 0x4c859
-  __TEXT.__objc_stubs: 0xf38e0
-  __DATA_CONST.__got: 0xa120
-  __DATA_CONST.__const: 0x1cca8
-  __DATA_CONST.__objc_classlist: 0x5238
-  __DATA_CONST.__objc_catlist: 0x348
+  __TEXT.__objc_stubs: 0xf3ca0
+  __DATA_CONST.__got: 0xa140
+  __DATA_CONST.__const: 0x1cce0
+  __DATA_CONST.__objc_classlist: 0x5248
+  __DATA_CONST.__objc_catlist: 0x360
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a900
+  __DATA_CONST.__objc_selrefs: 0x4aa20
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f70
+  __DATA_CONST.__objc_superrefs: 0x3f78
   __DATA_CONST.__objc_arraydata: 0x1850
-  __AUTH_CONST.__auth_got: 0x2ab0
-  __AUTH_CONST.__const: 0x10978
-  __AUTH_CONST.__cfstring: 0x6ee00
-  __AUTH_CONST.__objc_const: 0x269308
+  __AUTH_CONST.__auth_got: 0x2ad0
+  __AUTH_CONST.__const: 0x10998
+  __AUTH_CONST.__cfstring: 0x6efc0
+  __AUTH_CONST.__objc_const: 0x269638
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x680
   __AUTH_CONST.__objc_intobj: 0x2bc8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10400
-  __DATA.__objc_ivar: 0xf320
+  __AUTH.__objc_data: 0x104a0
+  __DATA.__objc_ivar: 0xf338
   __DATA.__data: 0x1f8b8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xaa0
+  __DATA.__bss: 0xab0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x23230
   __DATA_DIRTY.__data: 0x180

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 29240BCF-63FC-34A5-A4A3-F4DE3DF56786
-  Functions: 70029
-  Symbols:   236776
-  CStrings:  104062
+  UUID: 8676BE2A-9484-3492-888E-7DE10333250F
+  Functions: 70051
+  Symbols:   236885
+  CStrings:  104141
 
Symbols:
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
+ +[SBMenuBarAppearanceTransitionBackdropLayerView layerClass]
+ -[SBLockScreenManager coverSheetViewControllerIsTransitioningToSecureApp:]
+ -[SBMainDisplayConfigurationTransformer transformDisplayConfiguration:].cold.2
+ -[SBRootSceneWindow .cxx_destruct]
+ -[SBRootSceneWindow _configureRootLayer:sceneTransformLayer:transformLayer:]
+ -[SBRootSceneWindow _updateRootLayerBackgroundColor]
+ -[SBRootSceneWindow backgroundColor]
+ -[SBRootSceneWindow bezelLayer]
+ -[SBRootSceneWindow initWithDisplayConfiguration:]
+ -[SBRootSceneWindow layerForBackgroundColor]
+ -[SBRootSceneWindow maskLayer]
+ -[SBRootSceneWindow traitCollectionDidChange:]
+ -[SBWallpaperIconStyleCoordinator _enclosureAccentColor]
+ -[SBWallpaperIconStyleCoordinator _enclosureAccentColor].cold.1
+ -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ GCC_except_table251
+ GCC_except_table257
+ _FBSDebugOptionKeyEnableMTE
+ _FBSDisplayRotationFromRadians
+ _MGGetProductType
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_SBDeviceEmulationController
+ _OBJC_CLASS_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ _OBJC_IVAR_$_SBLockScreenManager._performingWakeToAppTransition
+ _OBJC_IVAR_$_SBRootSceneWindow._backgroundColor
+ _OBJC_IVAR_$_SBRootSceneWindow._bezelLayer
+ _OBJC_IVAR_$_SBRootSceneWindow._layerForBackgroundColor
+ _OBJC_IVAR_$_SBRootSceneWindow._maskLayer
+ _OBJC_IVAR_$_SBWallpaperIconStyleCoordinator._caseAccentColor
+ _OBJC_METACLASS_$_SBDeviceEmulationController
+ _OBJC_METACLASS_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
+ __OBJC_$_CLASS_METHODS_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
+ __OBJC_$_INSTANCE_METHODS_SBRootSceneWindow
+ __OBJC_$_INSTANCE_VARIABLES_SBRootSceneWindow
+ __OBJC_$_PROP_LIST_SBRootSceneWindow
+ __OBJC_CLASS_RO_$_SBDeviceEmulationController
+ __OBJC_CLASS_RO_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ __OBJC_METACLASS_RO_$_SBDeviceEmulationController
+ __OBJC_METACLASS_RO_$_SBMenuBarAppearanceTransitionBackdropLayerView
+ __SBF_Private_IsD23Like
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.85
+ ___56-[SBWallpaperIconStyleCoordinator _enclosureAccentColor]_block_invoke
+ ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_2
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.81
+ ___block_literal_global.90
+ __enclosureAccentColor.enclosureAccentColor
+ __enclosureAccentColor.onceToken
+ _colorForSpecifierString
+ _kBCBatteryDeviceA173ProductIdentifier
+ _objc_msgSend$_enclosureAccentColor
+ _objc_msgSend$_updateRootLayerBackgroundColor
+ _objc_msgSend$_updateTransformLayer
+ _objc_msgSend$caseAccentColor
+ _objc_msgSend$customScaleFactorX
+ _objc_msgSend$customScaleFactorY
+ _objc_msgSend$customTranslationOffsetX
+ _objc_msgSend$customTranslationOffsetY
+ _objc_msgSend$deviceContext
+ _objc_msgSend$displayContext
+ _objc_msgSend$emulatedDeviceBezelImageName
+ _objc_msgSend$emulatedDeviceBounds
+ _objc_msgSend$emulatedDeviceClass
+ _objc_msgSend$emulatedDeviceImageContainingBundle
+ _objc_msgSend$emulatedDeviceMaskImageName
+ _objc_msgSend$emulatedDisplayCornerRadius
+ _objc_msgSend$emulatedHomeButtonType
+ _objc_msgSend$enclosureAccentColor
+ _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
+ _objc_msgSend$hasEmulatedDeviceBounds
+ _objc_msgSend$insertSublayer:below:
+ _objc_msgSend$isEmulatedDevice
+ _objc_msgSend$renderingCenter
+ _objc_msgSend$rootLayerBackgroundColorString
+ _objc_msgSend$sb_configureForDeviceEmulation
+ _objc_msgSend$scalingStyle
+ _objc_msgSend$setCaseAccentColor:
+ _objc_msgSend$setDeviceContext:
+ _objc_msgSend$setDisplayContext:
+ _objc_msgSend$setEnableMTE:
+ _objc_msgSend$setEnclosureAccentColor:
+ _sscanf
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- GCC_except_table173
- GCC_except_table323
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.82
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.78
- _objc_msgSend$_shouldShowAlertForSeed
CStrings:
+ "%@Color"
+ "%x"
+ "([\\dA-F]{6})"
+ "17"
+ "18"
+ "7"
+ "8"
+ "9"
+ "DeviceEmulation"
+ "DeviceEnclosureColor"
+ "SBDeviceEmulationController"
+ "SBMenuBarAppearanceTransitionBackdropLayerView"
+ "T@\"CALayer\",R,N,V_bezelLayer"
+ "T@\"CALayer\",R,N,V_layerForBackgroundColor"
+ "T@\"CALayer\",R,N,V_maskLayer"
+ "T@\"UIColor\",R,N,V_backgroundColor"
+ "T@\"UISApplicationInitializationContext\",R,C,N"
+ "T@\"UISDeviceContext\",R,C,N"
+ "T@\"UISDisplayContext\",R,C,N"
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "_bezelLayer"
+ "_caseAccentColor"
+ "_configureRootLayer:sceneTransformLayer:transformLayer:"
+ "_enclosureAccentColor"
+ "_layerForBackgroundColor"
+ "_maskLayer"
+ "_performingWakeToAppTransition"
+ "_updateRootLayerBackgroundColor"
+ "_updateTransformLayer"
+ "applicationInitializationContext"
+ "bezelLayer"
+ "caseAccentColor"
+ "caseColor"
+ "coverSheetViewControllerIsTransitioningToSecureApp:"
+ "customScaleFactorX"
+ "customScaleFactorY"
+ "customTranslationOffsetX"
+ "customTranslationOffsetY"
+ "deviceContext"
+ "displayContext"
+ "emulatedDeviceBezelImageName"
+ "emulatedDeviceBounds"
+ "emulatedDeviceClass"
+ "emulatedDeviceImageContainingBundle"
+ "emulatedDeviceMaskImageName"
+ "emulatedDisplayCornerRadius"
+ "emulatedHomeButtonType"
+ "enableMTE"
+ "enclosureAccentColor"
+ "enclosureColor"
+ "hasDifferentColorAppearanceComparedToTraitCollection:"
+ "hasEmulatedDeviceBounds"
+ "insertSublayer:below:"
+ "isEmulatedDevice"
+ "layerForBackgroundColor"
+ "maskLayer"
+ "renderingCenter"
+ "rootLayerBackgroundColorString"
+ "sb_configureForDeviceEmulation"
+ "scalingStyle"
+ "setCaseAccentColor:"
+ "setDeviceContext:"
+ "setDisplayContext:"
+ "setEnableMTE:"
+ "setEnclosureAccentColor:"
- "_shouldShowAlertForSeed"

```
