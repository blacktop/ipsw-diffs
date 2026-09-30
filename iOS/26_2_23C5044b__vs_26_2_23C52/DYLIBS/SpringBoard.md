## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.2.6.103.0
-  __TEXT.__text: 0xa9ad84
-  __TEXT.__auth_stubs: 0x5580
+4557.2.6.104.0
+  __TEXT.__text: 0xa9be84
+  __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb86b8
-  __TEXT.__const: 0x12ed0
-  __TEXT.__oslogstring: 0x5e79d
-  __TEXT.__cstring: 0x7d712
+  __TEXT.__objc_methlist: 0xb87b8
+  __TEXT.__const: 0x12ec0
+  __TEXT.__oslogstring: 0x5e7e7
+  __TEXT.__cstring: 0x7d739
   __TEXT.__gcc_except_tab: 0x19b84
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c7e8
+  __TEXT.__unwind_info: 0x2c818
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x222c9
-  __TEXT.__objc_methname: 0x1d258d
+  __TEXT.__objc_classname: 0x222f5
+  __TEXT.__objc_methname: 0x1d2984
   __TEXT.__objc_methtype: 0x4d430
-  __TEXT.__objc_stubs: 0xf5240
-  __DATA_CONST.__got: 0xa318
+  __TEXT.__objc_stubs: 0xf5560
+  __DATA_CONST.__got: 0xa320
   __DATA_CONST.__const: 0x1cc08
-  __DATA_CONST.__objc_classlist: 0x52a0
-  __DATA_CONST.__objc_catlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x52a8
+  __DATA_CONST.__objc_catlist: 0x370
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0c8
+  __DATA_CONST.__objc_selrefs: 0x4b1b8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fc0
+  __DATA_CONST.__objc_superrefs: 0x3fc8
   __DATA_CONST.__objc_arraydata: 0x1870
-  __AUTH_CONST.__auth_got: 0x2ad8
+  __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH_CONST.__const: 0x10cb8
-  __AUTH_CONST.__cfstring: 0x6f6e0
-  __AUTH_CONST.__objc_const: 0x26c228
+  __AUTH_CONST.__cfstring: 0x6f740
+  __AUTH_CONST.__objc_const: 0x26c4a0
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10900
-  __DATA.__objc_ivar: 0xf544
+  __AUTH.__objc_data: 0x10950
+  __DATA.__objc_ivar: 0xf558
   __DATA.__data: 0x1f8b8
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 480B2C56-70B8-3117-B918-24EE2D1FB89D
-  Functions: 70415
-  Symbols:   238129
-  CStrings:  104706
+  UUID: 400708DB-4861-3381-B85F-F063752BA0A4
+  Functions: 70433
+  Symbols:   238212
+  CStrings:  104756
 
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
+ -[SBSlideOverGlassMaterialView setSDFGaussianRadius:]
+ -[SBSlideOverTongueView _updateCornerRadius]
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
+ _OBJC_IVAR_$_SBSlideOverTongueView._continuousCornerRadius
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
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.659
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.661
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1210
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.754
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.785
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.816
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.922
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.809
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.926
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1781
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.938
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.361
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1633
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1635
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1637
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1641
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1764
+ ___block_literal_global.1056
+ ___block_literal_global.1101
+ ___block_literal_global.1153
+ ___block_literal_global.1156
+ ___block_literal_global.1161
+ ___block_literal_global.1167
+ ___block_literal_global.1460
+ ___block_literal_global.1607
+ ___block_literal_global.1611
+ ___block_literal_global.1643
+ ___block_literal_global.1654
+ ___block_literal_global.1656
+ ___block_literal_global.1658
+ ___block_literal_global.1674
+ ___block_literal_global.1790
+ ___block_literal_global.1813
+ ___block_literal_global.1838
+ ___block_literal_global.586
+ ___block_literal_global.636
+ ___block_literal_global.637
+ ___block_literal_global.639
+ ___block_literal_global.642
+ ___block_literal_global.664
+ ___block_literal_global.691
+ ___block_literal_global.697
+ ___block_literal_global.785
+ ___block_literal_global.820
+ ___block_literal_global.822
+ ___block_literal_global.846
+ ___block_literal_global.856
+ ___block_literal_global.859
+ ___block_literal_global.887
+ ___block_literal_global.892
+ ___block_literal_global.898
+ ___block_literal_global.902
+ ___block_literal_global.904
+ ___block_literal_global.908
+ ___block_literal_global.910
+ ___block_literal_global.914
+ ___block_literal_global.916
+ ___block_literal_global.920
+ ___block_literal_global.922
+ ___block_literal_global.926
+ ___block_literal_global.928
+ ___block_literal_global.932
+ ___block_literal_global.940
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
+ _objc_msgSend$setSDFGaussianRadius:
+ _sscanf
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.668
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.670
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1219
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.763
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.794
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.825
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.931
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.818
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.935
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1790
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.947
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.370
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1642
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1644
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1646
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1650
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1773
- ___block_literal_global.1074
- ___block_literal_global.1110
- ___block_literal_global.1162
- ___block_literal_global.1165
- ___block_literal_global.1170
- ___block_literal_global.1176
- ___block_literal_global.1469
- ___block_literal_global.1616
- ___block_literal_global.1620
- ___block_literal_global.1661
- ___block_literal_global.1663
- ___block_literal_global.1665
- ___block_literal_global.1667
- ___block_literal_global.1683
- ___block_literal_global.1799
- ___block_literal_global.1831
- ___block_literal_global.1847
- ___block_literal_global.554
- ___block_literal_global.645
- ___block_literal_global.646
- ___block_literal_global.648
- ___block_literal_global.651
- ___block_literal_global.673
- ___block_literal_global.706
- ___block_literal_global.794
- ___block_literal_global.821
- ___block_literal_global.829
- ___block_literal_global.831
- ___block_literal_global.855
- ___block_literal_global.865
- ___block_literal_global.868
- ___block_literal_global.901
- ___block_literal_global.905
- ___block_literal_global.907
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.917
- ___block_literal_global.919
- ___block_literal_global.923
- ___block_literal_global.925
- ___block_literal_global.929
- ___block_literal_global.931
- ___block_literal_global.935
- ___block_literal_global.937
- ___block_literal_global.941
- ___block_literal_global.949
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
+ "gaussianRadius"
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
+ "setSDFGaussianRadius:"
- "_shouldShowAlertForSeed"

```
