## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.3.8.0.0
-  __TEXT.__text: 0xa9c4c4
-  __TEXT.__auth_stubs: 0x5580
+4557.3.9.101.0
+  __TEXT.__text: 0xa9d800
+  __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb8750
-  __TEXT.__const: 0x12ed0
-  __TEXT.__oslogstring: 0x5e79d
-  __TEXT.__cstring: 0x7d874
+  __TEXT.__objc_methlist: 0xb8830
+  __TEXT.__const: 0x12ec0
+  __TEXT.__oslogstring: 0x5e94c
+  __TEXT.__cstring: 0x7d88c
   __TEXT.__gcc_except_tab: 0x19c34
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c820
+  __TEXT.__unwind_info: 0x2c840
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x2230d
-  __TEXT.__objc_methname: 0x1d27e7
-  __TEXT.__objc_methtype: 0x4d3df
-  __TEXT.__objc_stubs: 0xf5300
-  __DATA_CONST.__got: 0xa330
+  __TEXT.__objc_classname: 0x22338
+  __TEXT.__objc_methname: 0x1d2b60
+  __TEXT.__objc_methtype: 0x4d3e0
+  __TEXT.__objc_stubs: 0xf5600
+  __DATA_CONST.__got: 0xa338
   __DATA_CONST.__const: 0x1cc10
-  __DATA_CONST.__objc_classlist: 0x52b0
-  __DATA_CONST.__objc_catlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x52b8
+  __DATA_CONST.__objc_catlist: 0x370
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b100
+  __DATA_CONST.__objc_selrefs: 0x4b1e8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fd0
+  __DATA_CONST.__objc_superrefs: 0x3fd8
   __DATA_CONST.__objc_arraydata: 0x1870
-  __AUTH_CONST.__auth_got: 0x2ad8
+  __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH_CONST.__const: 0x10cd8
-  __AUTH_CONST.__cfstring: 0x6f840
-  __AUTH_CONST.__objc_const: 0x26c3f8
+  __AUTH_CONST.__cfstring: 0x6f880
+  __AUTH_CONST.__objc_const: 0x26c630
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x109a0
-  __DATA.__objc_ivar: 0xf558
+  __AUTH.__objc_data: 0x109f0
+  __DATA.__objc_ivar: 0xf564
   __DATA.__data: 0x1f8b8
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: DF88A4E4-3177-3DDF-ADC1-92D01727F99C
-  Functions: 70436
-  Symbols:   238196
-  CStrings:  104739
+  UUID: 370371B3-C02B-3032-A678-71B19D395352
+  Functions: 70452
+  Symbols:   238272
+  CStrings:  104788
 
Symbols:
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
+ -[SBDisplayItemLayoutAttributesCalculator _frameForLayoutRole:inAppLayout:layoutAttributesMap:bounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:]
+ -[SBDisplayItemLayoutAttributesCalculator frameForLayoutRole:inAppLayout:bounds:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
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
+ -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
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
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
+ _colorForSpecifierString
+ _objc_msgSend$_frameForLayoutRole:inAppLayout:layoutAttributesMap:bounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:
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
+ _objc_msgSend$frameForLayoutRole:inAppLayout:bounds:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
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
+ _objc_msgSend$windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
+ _sscanf
- -[SBDisplayItemLayoutAttributesCalculator _frameForLayoutRole:inAppLayout:layoutAttributesMap:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:]
- -[SBDisplayItemLayoutAttributesCalculator frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
- _OBJC_IVAR_$_SBSwitcherWindowingSettings._cachedWindowingConfiguration_nativeContainerReferencePixelBounds
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
- _objc_msgSend$_frameForLayoutRole:inAppLayout:layoutAttributesMap:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:
- _objc_msgSend$_shouldShowAlertForSeed
- _objc_msgSend$frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
CStrings:
+ "%@Color"
+ "%x"
+ "([\\dA-F]{6})"
+ "@120@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48d56d64d72d80d88d96B104B108B112B116"
+ "DeviceEmulation"
+ "Icon image frame conversion for %{public}@ resulted in an unusable value (%{public}@ -> %{public}@); defaulting to CGRectNull"
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
+ "_frameForLayoutRole:inAppLayout:layoutAttributesMap:bounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:"
+ "_layerForBackgroundColor"
+ "_maskLayer"
+ "_updateRootLayerBackgroundColor"
+ "_updateTransformLayer"
+ "applicationInitializationContext"
+ "bezelLayer"
+ "containerBounds %@{public}@ resulted in no grid heights (prefersStripHidden: %{BOOL}u; prefersDockHidden: %{BOOL}u)"
+ "containerBounds %@{public}@ resulted in no grid widths (prefersStripHidden: %{BOOL}u; prefersDockHidden: %{BOOL}u)"
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
+ "frameForLayoutRole:inAppLayout:bounds:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
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
+ "windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}200@0:8q16@24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64q96d104d112B120B124B128B132{CGRect={CGPoint=dd}{CGSize=dd}}136{CGRect={CGPoint=dd}{CGSize=dd}}168"
- "@152@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80d88d96d104d112d120d128B136B140B144B148"
- "_cachedWindowingConfiguration_nativeContainerReferencePixelBounds"
- "_frameForLayoutRole:inAppLayout:layoutAttributesMap:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:skipAutoLayout:"
- "_shouldShowAlertForSeed"
- "frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}168@0:8q16@24{CGRect={CGPoint=dd}{CGSize=dd}}32q64d72d80B88B92B96B100{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136"

```
