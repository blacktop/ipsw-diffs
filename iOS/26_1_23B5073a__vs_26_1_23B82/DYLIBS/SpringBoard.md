## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.1.19.106.0
-  __TEXT.__text: 0xa91794
-  __TEXT.__auth_stubs: 0x5590
+4557.1.19.109.0
+  __TEXT.__text: 0xa928a8
+  __TEXT.__auth_stubs: 0x55b0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb8020
-  __TEXT.__const: 0x12f40
-  __TEXT.__oslogstring: 0x5e3ba
-  __TEXT.__cstring: 0x7d1d7
+  __TEXT.__objc_methlist: 0xb8118
+  __TEXT.__const: 0x12f30
+  __TEXT.__oslogstring: 0x5e404
+  __TEXT.__cstring: 0x7d1ef
   __TEXT.__gcc_except_tab: 0x19690
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c590
+  __TEXT.__unwind_info: 0x2c5c0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x2220f
-  __TEXT.__objc_methname: 0x1d13eb
+  __TEXT.__objc_classname: 0x2223b
+  __TEXT.__objc_methname: 0x1d1838
   __TEXT.__objc_methtype: 0x4d12c
-  __TEXT.__objc_stubs: 0xf4d00
-  __DATA_CONST.__got: 0xa2e0
+  __TEXT.__objc_stubs: 0xf5000
+  __DATA_CONST.__got: 0xa2e8
   __DATA_CONST.__const: 0x1cb58
-  __DATA_CONST.__objc_classlist: 0x5278
-  __DATA_CONST.__objc_catlist: 0x368
+  __DATA_CONST.__objc_classlist: 0x5280
+  __DATA_CONST.__objc_catlist: 0x380
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4af30
+  __DATA_CONST.__objc_selrefs: 0x4b028
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fa0
+  __DATA_CONST.__objc_superrefs: 0x3fa8
   __DATA_CONST.__objc_arraydata: 0x1868
-  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__auth_got: 0x2af0
   __AUTH_CONST.__const: 0x10c58
-  __AUTH_CONST.__cfstring: 0x6f140
-  __AUTH_CONST.__objc_const: 0x26b5f0
+  __AUTH_CONST.__cfstring: 0x6f180
+  __AUTH_CONST.__objc_const: 0x26b878
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x770
-  __AUTH_CONST.__objc_intobj: 0x2ce8
+  __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10770
-  __DATA.__objc_ivar: 0xf474
+  __AUTH.__objc_data: 0x107c0
+  __DATA.__objc_ivar: 0xf488
   __DATA.__data: 0x1f8b8
   __DATA.__bss: 0xaa0
   __DATA.__common: 0xa40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: E0CB9C34-EC30-31F6-9D54-D2B52A8C85E4
-  Functions: 70249
-  Symbols:   237648
-  CStrings:  104480
+  UUID: F692FE14-DE59-3E46-BF44-5CEF681D64A3
+  Functions: 70267
+  Symbols:   237730
+  CStrings:  104531
 
Symbols:
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
+ -[SBHomeGestureDismissableCoverSheetViewController hasHomeGestureOwnership]
+ -[SBHomeGestureDismissableCoverSheetViewController setHasHomeGestureOwnership:]
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
+ -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ _FBSDisplayRotationFromRadians
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_SBDeviceEmulationController
+ _OBJC_IVAR_$_SBHomeGestureDismissableCoverSheetViewController._hasHomeGestureOwnership
+ _OBJC_IVAR_$_SBRootSceneWindow._backgroundColor
+ _OBJC_IVAR_$_SBRootSceneWindow._bezelLayer
+ _OBJC_IVAR_$_SBRootSceneWindow._layerForBackgroundColor
+ _OBJC_IVAR_$_SBRootSceneWindow._maskLayer
+ _OBJC_METACLASS_$_SBDeviceEmulationController
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
+ __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
+ __OBJC_$_INSTANCE_METHODS_SBRootSceneWindow
+ __OBJC_$_INSTANCE_VARIABLES_SBRootSceneWindow
+ __OBJC_$_PROP_LIST_SBRootSceneWindow
+ __OBJC_CLASS_RO_$_SBDeviceEmulationController
+ __OBJC_METACLASS_RO_$_SBDeviceEmulationController
+ ___81-[SBIdleTimerGlobalStateMonitor _boolMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.73
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
+ ___89-[SBIdleTimerGlobalStateMonitor _timeIntervalMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.74
+ _colorForSpecifierString
+ _objc_msgSend$_updateRootLayerBackgroundColor
+ _objc_msgSend$_updateTransformLayer
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
+ _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
+ _objc_msgSend$hasEmulatedDeviceBounds
+ _objc_msgSend$insertSublayer:below:
+ _objc_msgSend$isEmulatedDevice
+ _objc_msgSend$renderingCenter
+ _objc_msgSend$rootLayerBackgroundColorString
+ _objc_msgSend$sb_configureForDeviceEmulation
+ _objc_msgSend$scalingStyle
+ _objc_msgSend$setDeviceContext:
+ _objc_msgSend$setDisplayContext:
+ _sscanf
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- ___81-[SBIdleTimerGlobalStateMonitor _boolMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.77
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
- ___89-[SBIdleTimerGlobalStateMonitor _timeIntervalMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.78
- _objc_msgSend$_shouldShowAlertForSeed
CStrings:
+ "%@Color"
+ "%x"
+ "([\\dA-F]{6})"
+ "DeviceEmulation"
+ "SBDeviceEmulationController"
+ "T@\"CALayer\",R,N,V_bezelLayer"
+ "T@\"CALayer\",R,N,V_layerForBackgroundColor"
+ "T@\"CALayer\",R,N,V_maskLayer"
+ "T@\"UIColor\",R,N,V_backgroundColor"
+ "T@\"UISApplicationInitializationContext\",R,C,N"
+ "T@\"UISDeviceContext\",R,C,N"
+ "T@\"UISDisplayContext\",R,C,N"
+ "TB,N,V_hasHomeGestureOwnership"
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "_bezelLayer"
+ "_configureRootLayer:sceneTransformLayer:transformLayer:"
+ "_hasHomeGestureOwnership"
+ "_layerForBackgroundColor"
+ "_maskLayer"
+ "_updateRootLayerBackgroundColor"
+ "_updateTransformLayer"
+ "applicationInitializationContext"
+ "bezelLayer"
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
+ "hasDifferentColorAppearanceComparedToTraitCollection:"
+ "hasEmulatedDeviceBounds"
+ "hasHomeGestureOwnership"
+ "insertSublayer:below:"
+ "isEmulatedDevice"
+ "layerForBackgroundColor"
+ "maskLayer"
+ "renderingCenter"
+ "rootLayerBackgroundColorString"
+ "sb_configureForDeviceEmulation"
+ "scalingStyle"
+ "setDeviceContext:"
+ "setDisplayContext:"
+ "setHasHomeGestureOwnership:"
- "_shouldShowAlertForSeed"

```
