## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.4.12.102.0
-  __TEXT.__text: 0xb1dfe4
-  __TEXT.__auth_stubs: 0x5590
+4557.4.12.104.0
+  __TEXT.__text: 0xb1f190
+  __TEXT.__auth_stubs: 0x55b0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb9948
-  __TEXT.__const: 0x13100
-  __TEXT.__oslogstring: 0x5ecc9
-  __TEXT.__cstring: 0x7e6a2
+  __TEXT.__objc_methlist: 0xb9a28
+  __TEXT.__const: 0x130f0
+  __TEXT.__oslogstring: 0x5ed13
+  __TEXT.__cstring: 0x7e6ba
   __TEXT.__gcc_except_tab: 0x19558
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x303a0
+  __TEXT.__unwind_info: 0x303c8
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x22535
-  __TEXT.__objc_methname: 0x1d59f8
+  __TEXT.__objc_classname: 0x22561
+  __TEXT.__objc_methname: 0x1d5dd9
   __TEXT.__objc_methtype: 0x4d89f
-  __TEXT.__objc_stubs: 0xf6780
-  __DATA_CONST.__got: 0xa490
+  __TEXT.__objc_stubs: 0xf6a80
+  __DATA_CONST.__got: 0xa498
   __DATA_CONST.__const: 0x1cf38
-  __DATA_CONST.__objc_classlist: 0x5310
-  __DATA_CONST.__objc_catlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x5318
+  __DATA_CONST.__objc_catlist: 0x370
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b748
+  __DATA_CONST.__objc_selrefs: 0x4b830
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x4010
+  __DATA_CONST.__objc_superrefs: 0x4018
   __DATA_CONST.__objc_arraydata: 0x1870
-  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__auth_got: 0x2af0
   __AUTH_CONST.__const: 0x10228
-  __AUTH_CONST.__cfstring: 0x704e0
-  __AUTH_CONST.__objc_const: 0x26f3f8
+  __AUTH_CONST.__cfstring: 0x70520
+  __AUTH_CONST.__objc_const: 0x26f650
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10860
-  __DATA.__objc_ivar: 0xf6ec
+  __AUTH.__objc_data: 0x108b0
+  __DATA.__objc_ivar: 0xf6fc
   __DATA.__data: 0x1fb08
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa48

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 611A44A6-7BBE-3A5E-AD55-61E8348FD8BD
-  Functions: 71485
-  Symbols:   241807
-  CStrings:  105326
+  UUID: 7354B62A-C2E7-32E9-88E7-B3468C96C336
+  Functions: 71502
+  Symbols:   241886
+  CStrings:  105373
 
Symbols:
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
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
+ ___55-[SBHomeGestureToZoomDownSwitcherModifier handleEvent:]_block_invoke
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.226
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
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.225
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
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "_bezelLayer"
+ "_configureRootLayer:sceneTransformLayer:transformLayer:"
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
- "_shouldShowAlertForSeed"

```
