## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.4.12.104.0
-  __TEXT.__text: 0xb1f190
-  __TEXT.__auth_stubs: 0x55b0
+4557.5.3.0.0
+  __TEXT.__text: 0xb1ea4c
+  __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb9a28
-  __TEXT.__const: 0x130f0
-  __TEXT.__oslogstring: 0x5ed13
-  __TEXT.__cstring: 0x7e6ba
-  __TEXT.__gcc_except_tab: 0x19558
+  __TEXT.__objc_methlist: 0xb9980
+  __TEXT.__const: 0x13100
+  __TEXT.__oslogstring: 0x5ee0e
+  __TEXT.__cstring: 0x7e6a2
+  __TEXT.__gcc_except_tab: 0x195ac
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x303c8
+  __TEXT.__unwind_info: 0x303b0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x22561
-  __TEXT.__objc_methname: 0x1d5dd9
+  __TEXT.__objc_classname: 0x22535
+  __TEXT.__objc_methname: 0x1d5b4f
   __TEXT.__objc_methtype: 0x4d89f
-  __TEXT.__objc_stubs: 0xf6a80
-  __DATA_CONST.__got: 0xa498
-  __DATA_CONST.__const: 0x1cf38
-  __DATA_CONST.__objc_classlist: 0x5318
-  __DATA_CONST.__objc_catlist: 0x370
+  __TEXT.__objc_stubs: 0xf6820
+  __DATA_CONST.__got: 0xa4a0
+  __DATA_CONST.__const: 0x1cf60
+  __DATA_CONST.__objc_classlist: 0x5310
+  __DATA_CONST.__objc_catlist: 0x358
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b830
+  __DATA_CONST.__objc_selrefs: 0x4b788
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x4018
+  __DATA_CONST.__objc_superrefs: 0x4010
   __DATA_CONST.__objc_arraydata: 0x1870
-  __AUTH_CONST.__auth_got: 0x2af0
-  __AUTH_CONST.__const: 0x10228
-  __AUTH_CONST.__cfstring: 0x70520
-  __AUTH_CONST.__objc_const: 0x26f650
+  __AUTH_CONST.__auth_got: 0x2ae8
+  __AUTH_CONST.__const: 0x10248
+  __AUTH_CONST.__cfstring: 0x704e0
+  __AUTH_CONST.__objc_const: 0x26f450
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x108b0
-  __DATA.__objc_ivar: 0xf6fc
+  __AUTH.__objc_data: 0x10860
+  __DATA.__objc_ivar: 0xf6f4
   __DATA.__data: 0x1fb08
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa48

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7354B62A-C2E7-32E9-88E7-B3468C96C336
-  Functions: 71502
-  Symbols:   241886
-  CStrings:  105373
+  UUID: E28D32EF-D36F-3588-B35D-756D60D7B0A0
+  Functions: 71494
+  Symbols:   241838
+  CStrings:  105343
 
Symbols:
+ -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
+ -[SBNCSoundController _mediaServicesWereReset:]
+ -[SBNCSoundController playingNotifications]
+ -[SBNCSoundController setPlayingNotifications:]
+ -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:]
+ -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:].cold.1
+ -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:].cold.2
+ GCC_except_table189
+ _AVAudioSessionMediaServicesWereResetNotification
+ _NSStringFromTLAlertPlaybackCompletionType
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._savedIconGlassGroupingBehaviors
+ _OBJC_IVAR_$_SBNCSoundController._playingNotifications
+ ___47-[SBNCSoundController _mediaServicesWereReset:]_block_invoke
+ ___51-[SBStatusBarStateAggregator _updateTetheringState]_block_invoke.233
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_46
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_47
+ ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.46
+ ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.40
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.225
+ ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.242
+ ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.242.cold.1
+ ___93-[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:]_block_invoke
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.214
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.218
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke_2.219
+ ___block_descriptor_48_e8_32s40r_e36_v32?0"NSString"8"SBUISound"16^B24lr40l8s32l8
+ _kFigRoutingContextNotification_PredictedSelectedRouteDescriptorChanged
+ _objc_msgSend$_postNotificationRequest:shouldAnnounce:shouldPreprocess:
+ _objc_msgSend$_shouldShowAlertForSeed
+ _objc_msgSend$iconGlassGroupingBehavior
+ _objc_msgSend$playingNotifications
+ _objc_msgSend$setIconGlassGroupingBehavior:
+ _objc_msgSend$setIconsFromIconListModel:
+ _objc_msgSend$visibleIconListViews
- +[SBDeviceEmulationController applicationInitializationContext]
- +[SBDeviceEmulationController deviceContext]
- +[SBDeviceEmulationController displayContext]
- -[SBMainDisplayConfigurationTransformer transformDisplayConfiguration:].cold.2
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:]
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:].cold.1
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:].cold.2
- -[SBRootSceneWindow .cxx_destruct]
- -[SBRootSceneWindow _configureRootLayer:sceneTransformLayer:transformLayer:]
- -[SBRootSceneWindow _updateRootLayerBackgroundColor]
- -[SBRootSceneWindow backgroundColor]
- -[SBRootSceneWindow bezelLayer]
- -[SBRootSceneWindow initWithDisplayConfiguration:]
- -[SBRootSceneWindow layerForBackgroundColor]
- -[SBRootSceneWindow maskLayer]
- -[SBRootSceneWindow traitCollectionDidChange:]
- -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
- _FBSDisplayRotationFromRadians
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_SBDeviceEmulationController
- _OBJC_IVAR_$_SBRootSceneWindow._backgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._bezelLayer
- _OBJC_IVAR_$_SBRootSceneWindow._layerForBackgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._maskLayer
- _OBJC_METACLASS_$_SBDeviceEmulationController
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
- __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
- __OBJC_$_INSTANCE_METHODS_SBRootSceneWindow
- __OBJC_$_INSTANCE_VARIABLES_SBRootSceneWindow
- __OBJC_$_PROP_LIST_SBRootSceneWindow
- __OBJC_CLASS_RO_$_SBDeviceEmulationController
- __OBJC_METACLASS_RO_$_SBDeviceEmulationController
- ___51-[SBStatusBarStateAggregator _updateTetheringState]_block_invoke.231
- ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.45
- ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.39
- ___76-[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:]_block_invoke
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.226
- ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.240
- ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.240.cold.1
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.212
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.216
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke_2.217
- ___block_literal_global.215
- ___block_literal_global.266
- _colorForSpecifierString
- _objc_msgSend$_postNotificationRequest:shouldAnnounce:
- _objc_msgSend$_updateRootLayerBackgroundColor
- _objc_msgSend$_updateTransformLayer
- _objc_msgSend$customScaleFactorX
- _objc_msgSend$customScaleFactorY
- _objc_msgSend$customTranslationOffsetX
- _objc_msgSend$customTranslationOffsetY
- _objc_msgSend$deviceContext
- _objc_msgSend$displayContext
- _objc_msgSend$emulatedDeviceBezelImageName
- _objc_msgSend$emulatedDeviceBounds
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDeviceImageContainingBundle
- _objc_msgSend$emulatedDeviceMaskImageName
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
- _objc_msgSend$hasEmulatedDeviceBounds
- _objc_msgSend$insertSublayer:below:
- _objc_msgSend$isEmulatedDevice
- _objc_msgSend$renderingCenter
- _objc_msgSend$rootLayerBackgroundColorString
- _objc_msgSend$sb_configureForDeviceEmulation
- _objc_msgSend$scalingStyle
- _objc_msgSend$setDeviceContext:
- _objc_msgSend$setDisplayContext:
- _sscanf
CStrings:
+ "CarPlay setting up deferred announce deactivation for %{public}@ on announce finish since this is the last notification to be announced"
+ "CarPlay withdrawing currently announcing notification request %{public}@ as it is starting announce for request %{public}@"
+ "CarPlay withdrawing notification request %{public}@ on announce finish while pending other announce notifications"
+ "Media services were reset. Checking for sounds that should replay."
+ "No replable sound to play"
+ "Play sound did finish for notification %{public}@ : %{public}@"
+ "Replaying sound for notification %{public}@"
+ "T@\"NSMutableDictionary\",&,N,V_playingNotifications"
+ "_mediaServicesWereReset:"
+ "_playingNotifications"
+ "_postNotificationRequest:shouldAnnounce:shouldPreprocess:"
+ "_savedIconGlassGroupingBehaviors"
+ "_shouldShowAlertForSeed"
+ "activityAlertClient:didPresentAlertProvider:"
+ "iconGlassGroupingBehavior"
+ "kill all sounds with lock state changed to unlocked."
+ "play alert completion for sound: %{public}@ completionType: %{public}@ "
+ "playingNotifications"
+ "setIconGlassGroupingBehavior:"
+ "setIconsFromIconListModel:"
+ "setPlayingNotifications:"
+ "visibleIconListViews"
+ "\x96"
- "%@Color"
- "%x"
- "([\\dA-F]{6})"
- "Carplay setting up deferred announce deactivation for %{public}@ on announce finish since this is the last notification to be announced"
- "Carplay withdrawing currently announcing notification request %{public}@ as it is starting announce for request %{public}@"
- "Carplay withdrawing notification request %{public}@ on announce finish while pending other announce notifications"
- "DeviceEmulation"
- "SBDeviceEmulationController"
- "T@\"CALayer\",R,N,V_bezelLayer"
- "T@\"CALayer\",R,N,V_layerForBackgroundColor"
- "T@\"CALayer\",R,N,V_maskLayer"
- "T@\"UIColor\",R,N,V_backgroundColor"
- "T@\"UISApplicationInitializationContext\",R,C,N"
- "T@\"UISDeviceContext\",R,C,N"
- "T@\"UISDisplayContext\",R,C,N"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "_bezelLayer"
- "_configureRootLayer:sceneTransformLayer:transformLayer:"
- "_layerForBackgroundColor"
- "_maskLayer"
- "_postNotificationRequest:shouldAnnounce:"
- "_updateRootLayerBackgroundColor"
- "_updateTransformLayer"
- "applicationInitializationContext"
- "bezelLayer"
- "customScaleFactorX"
- "customScaleFactorY"
- "customTranslationOffsetX"
- "customTranslationOffsetY"
- "deviceContext"
- "displayContext"
- "emulatedDeviceBezelImageName"
- "emulatedDeviceBounds"
- "emulatedDeviceClass"
- "emulatedDeviceImageContainingBundle"
- "emulatedDeviceMaskImageName"
- "emulatedDisplayCornerRadius"
- "emulatedHomeButtonType"
- "hasDifferentColorAppearanceComparedToTraitCollection:"
- "hasEmulatedDeviceBounds"
- "insertSublayer:below:"
- "isEmulatedDevice"
- "layerForBackgroundColor"
- "maskLayer"
- "renderingCenter"
- "rootLayerBackgroundColorString"
- "sb_configureForDeviceEmulation"
- "scalingStyle"
- "setDeviceContext:"
- "setDisplayContext:"
- "\x95"

```
