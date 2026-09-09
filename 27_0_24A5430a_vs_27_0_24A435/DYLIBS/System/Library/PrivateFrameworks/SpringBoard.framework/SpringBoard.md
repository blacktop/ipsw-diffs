## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

 4636.115.0.0.0
-  __TEXT.__text: 0xb0a100
+  __TEXT.__text: 0xb10074
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbdc30
-  __TEXT.__const: 0x11270
-  __TEXT.__oslogstring: 0x64e7b
-  __TEXT.__cstring: 0x84f3f
-  __TEXT.__gcc_except_tab: 0x18640
+  __TEXT.__objc_methlist: 0xbe0a8
+  __TEXT.__const: 0x11370
+  __TEXT.__oslogstring: 0x65862
+  __TEXT.__cstring: 0x85315
+  __TEXT.__gcc_except_tab: 0x18660
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x2e548
+  __TEXT.__unwind_info: 0x2e670
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d990
-  __DATA_CONST.__objc_classlist: 0x54d0
-  __DATA_CONST.__objc_catlist: 0x338
+  __DATA_CONST.__const: 0x1d9e8
+  __DATA_CONST.__objc_classlist: 0x5518
+  __DATA_CONST.__objc_catlist: 0x350
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2ad8
+  __DATA_CONST.__objc_protolist: 0x2af0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e920
+  __DATA_CONST.__objc_selrefs: 0x4eb30
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x4088
-  __DATA_CONST.__objc_arraydata: 0x1888
-  __DATA_CONST.__got: 0xa900
-  __AUTH_CONST.__const: 0x10b88
-  __AUTH_CONST.__cfstring: 0x746a0
-  __AUTH_CONST.__objc_const: 0x287bc8
+  __DATA_CONST.__objc_superrefs: 0x40a8
+  __DATA_CONST.__objc_arraydata: 0x18b8
+  __DATA_CONST.__got: 0xa9a0
+  __AUTH_CONST.__const: 0x10bc8
+  __AUTH_CONST.__cfstring: 0x74ba0
+  __AUTH_CONST.__objc_const: 0x289388
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x1728
+  __AUTH_CONST.__objc_arrayobj: 0x1740
   __AUTH_CONST.__objc_doubleobj: 0x850
   __AUTH_CONST.__objc_intobj: 0x2ca0
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2bc0
-  __AUTH.__objc_data: 0xe470
-  __DATA.__objc_ivar: 0xfc5c
-  __DATA.__data: 0x20f20
+  __AUTH_CONST.__auth_got: 0x2c00
+  __AUTH.__objc_data: 0xe6f0
+  __DATA.__objc_ivar: 0xfcb8
+  __DATA.__data: 0x21040
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x26bb0
+  __DATA_DIRTY.__objc_data: 0x26c00
   __DATA_DIRTY.__data: 0x140
   __DATA_DIRTY.__bss: 0x18c8
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73508
-  Symbols:   152075
-  CStrings:  23491
+  Functions: 73613
+  Symbols:   152364
+  CStrings:  23565
 
Symbols:
+ +[SBActivationInfoViewController _queue_readShipModeComplianceSupported:readyToShip:]
+ +[SBDeviceEmulationController applicationInitializationContext]
+ +[SBDeviceEmulationController deviceContext]
+ +[SBDeviceEmulationController displayContext]
+ +[SBFDIDeviceControlCoordinator _scene:hasEntitlement:]
+ +[SBFDIDeviceControlCoordinator addSceneExtensionIfNeeded:]
+ +[SBScreenEdgeCompensationDisplayTransformer isScreenEdgeCompensationEnabled]
+ +[SBScreenEdgeCompensationDisplayTransformer sceneTransformForWindowScene:]
+ +[SBScreenEdgeCompensationDisplayTransformer transformedConfigurationForConfiguration:]
+ -[SBAbstractWindowSceneDelegate(ForWindowSceneOnly) phoneRLController]
+ -[SBActivationInfoViewController _updateShipModeCompliance]
+ -[SBFDIDeviceControlBacklightInformer isRestricting]
+ -[SBFDIDeviceControlBacklightInformer setRestricting:]
+ -[SBFDIDeviceControlBacklightInformer shouldTurnOnScreenForBacklightSource:]
+ -[SBFDIDeviceControlCoordinator .cxx_destruct]
+ -[SBFDIDeviceControlCoordinator _updateBacklightRestrictionForWindowScene:wantsRestriction:]
+ -[SBFDIDeviceControlCoordinator _updateLiftToWakeForWindowScenes:wantsSuppression:]
+ -[SBFDIDeviceControlCoordinator _updateShieldButtonsRestrictionForWindowScenes:wantsRestriction:]
+ -[SBFDIDeviceControlCoordinator _updateTapToWakeForWindowScenes:wantsSuppression:]
+ -[SBFDIDeviceControlCoordinator applyFDIDeviceControlClientSettings:]
+ -[SBFDIDeviceControlCoordinator init]
+ -[SBFDIDeviceControlCoordinator invalidate]
+ -[SBPhoneRLController .cxx_destruct]
+ -[SBPhoneRLController _applyRootWindowTransform]
+ -[SBPhoneRLController _modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:forReason:]
+ -[SBPhoneRLController _phoneRLEnabledDidChange:]
+ -[SBPhoneRLController _phoneRLModeDidChange:]
+ -[SBPhoneRLController _phoneRLRecommendedNitsDidChange:]
+ -[SBPhoneRLController _reevaluatePhoneRLActivationStateForReason:]
+ -[SBPhoneRLController _setPhoneRLActive:]
+ -[SBPhoneRLController _transform]
+ -[SBPhoneRLController _transitionWithTransformer:fromTransform:toTransform:forReason:]
+ -[SBPhoneRLController associatedWindowScene]
+ -[SBPhoneRLController blankingStateDidChange:forDisplayRegion:onWindowScene:forBundleIDs:]
+ -[SBPhoneRLController blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:]
+ -[SBPhoneRLController createPhoneRLWindowWithWindowScene:]
+ -[SBPhoneRLController dealloc]
+ -[SBPhoneRLController ignoreWindowForPhoneRL:]
+ -[SBPhoneRLController initWithAssociatedWindowScene:displayRegionBlankingCoordinator:]
+ -[SBPhoneRLController invalidate]
+ -[SBPhoneRLController isPhoneRLActive]
+ -[SBPhoneRLController tearDownPhoneRLWindowWithWindowScene:]
+ -[SBPhoneRLView .cxx_destruct]
+ -[SBPhoneRLView _setupLayers]
+ -[SBPhoneRLView initWithFrame:]
+ -[SBPhoneRLView layoutSubviews]
+ -[SBPhoneRLView phoneRLLayer]
+ -[SBPhoneRLView setPhoneRLLayer:]
+ -[SBPhoneRLView setPhoneRLWidth:animated:]
+ -[SBPhoneRLView setWidth:]
+ -[SBPhoneRLView updatePhoneRLColor]
+ -[SBPhoneRLView updatePhoneRLPath]
+ -[SBPhoneRLView width]
+ -[SBPhoneRLViewController .cxx_destruct]
+ -[SBPhoneRLViewController _setupPhoneRLView]
+ -[SBPhoneRLViewController viewDidLoad]
+ -[SBPhoneRLViewController viewWillAppear:]
+ -[SBPhoneRLViewController viewWillDisappear:]
+ -[SBPhoneRLWindowSceneDelegate .cxx_destruct]
+ -[SBPhoneRLWindowSceneDelegate _associatedWindowScene]
+ -[SBPhoneRLWindowSceneDelegate scene:willConnectToSession:options:]
+ -[SBPhoneRLWindowSceneDelegate sceneDidDisconnect:]
+ -[SBSAPlatformMetricsContext _setSensorVariant:]
+ -[SBSAPlatformMetricsContext copyBySettingSensorVariant:]
+ -[SBSAPlatformMetricsContext sensorVariant]
+ -[SBSAPlatformMetricsContextMutator sensorVariant]
+ -[SBSAPlatformMetricsContextMutator setSensorVariant:]
+ -[SBTelephonyManager isPhysicalSIMActive]
+ -[SBWindowScene phoneRLController]
+ -[SBWindowSceneContext phoneRLController]
+ -[SBWindowSceneContext setPhoneRLController:]
+ -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
+ _AVControlCenterVideoEffectRingLight
+ _AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification
+ _AVControlCenterVideoEffectsModuleGetRingLightModeForBundleID
+ _AVControlCenterVideoEffectsModuleGetRingLightRecommendedNitsFloorForBundleID
+ _AVControlCenterVideoEffectsModuleIsEffectEnabledForBundleID
+ _AVControlCenterVideoEffectsModuleRingLightModeDidChangeNotification
+ _AVControlCenterVideoEffectsModuleRingLightRecommendedNitsFloorDidChangeNotification
+ _AVControlCenterVideoEffectsModuleSetRingLightActiveForBundleID
+ _IOPSShippingChargeLimitGetState
+ _MGIsDeviceOneOfType
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_SBDeviceEmulationController
+ _OBJC_CLASS_$_SBFDIDeviceControlBacklightInformer
+ _OBJC_CLASS_$_SBFDIDeviceControlCoordinator
+ _OBJC_CLASS_$_SBPhoneRLController
+ _OBJC_CLASS_$_SBPhoneRLView
+ _OBJC_CLASS_$_SBPhoneRLViewController
+ _OBJC_CLASS_$_SBPhoneRLWindowScene
+ _OBJC_CLASS_$_SBPhoneRLWindowSceneDelegate
+ _OBJC_CLASS_$_SBSFDIDeviceControlHostComponent
+ _OBJC_CLASS_$_SBSFDIDeviceControlSceneExtension
+ _OBJC_CLASS_$_SBScreenEdgeCompensationDisplayTransformer
+ _OBJC_CLASS_$_SSKHostingConfiguration
+ _OBJC_CLASS_$_SSKLayerConfiguration
+ _OBJC_IVAR_$_SBActivationInfoViewController._isReadyToShip
+ _OBJC_IVAR_$_SBActivationInfoViewController._isShipChargeLimitSupported
+ _OBJC_IVAR_$_SBApplicationInfo._disableD2026ClassicMode
+ _OBJC_IVAR_$_SBFDIDeviceControlBacklightInformer._restricting
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._backlightInformer
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableLiftToWakeAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableShieldButtonsAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._disableTapToWakeAssertions
+ _OBJC_IVAR_$_SBFDIDeviceControlCoordinator._restrictedBacklightControllers
+ _OBJC_IVAR_$_SBPhoneRLController._associatedWindowScene
+ _OBJC_IVAR_$_SBPhoneRLController._displayRegionBlankingAssociatedBundleID
+ _OBJC_IVAR_$_SBPhoneRLController._displayRegionBlankingCoordinator
+ _OBJC_IVAR_$_SBPhoneRLController._displayRegionBlankingState
+ _OBJC_IVAR_$_SBPhoneRLController._forcePhoneRLActivateObserver
+ _OBJC_IVAR_$_SBPhoneRLController._ignoredWindows
+ _OBJC_IVAR_$_SBPhoneRLController._phoneRLActive
+ _OBJC_IVAR_$_SBPhoneRLController._testingDefaults
+ _OBJC_IVAR_$_SBPhoneRLController._window
+ _OBJC_IVAR_$_SBPhoneRLView._phoneRLLayer
+ _OBJC_IVAR_$_SBPhoneRLView._width
+ _OBJC_IVAR_$_SBPhoneRLViewController._phoneRLView
+ _OBJC_IVAR_$_SBPhoneRLWindowSceneDelegate._phoneRLWindowScene
+ _OBJC_IVAR_$_SBWindowSceneContext._phoneRLController
+ _OBJC_METACLASS_$_SBDeviceEmulationController
+ _OBJC_METACLASS_$_SBFDIDeviceControlBacklightInformer
+ _OBJC_METACLASS_$_SBFDIDeviceControlCoordinator
+ _OBJC_METACLASS_$_SBPhoneRLController
+ _OBJC_METACLASS_$_SBPhoneRLView
+ _OBJC_METACLASS_$_SBPhoneRLViewController
+ _OBJC_METACLASS_$_SBPhoneRLWindowScene
+ _OBJC_METACLASS_$_SBPhoneRLWindowSceneDelegate
+ _OBJC_METACLASS_$_SBScreenEdgeCompensationDisplayTransformer
+ _SBBooleanFromShipChargeLimitDict
+ _SBLogDisplayTransforming
+ _SBLogFDIDeviceControl
+ _SBShipModeComplianceQueue
+ _SBShipModeComplianceQueue.onceToken
+ _SBShipModeComplianceQueue.queue
+ _SBUIWindowSceneSessionRolePhoneRL
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
+ __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
+ __OBJC_$_CLASS_METHODS_SBActivationInfoViewController
+ __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
+ __OBJC_$_CLASS_METHODS_SBFDIDeviceControlCoordinator
+ __OBJC_$_CLASS_METHODS_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
+ __OBJC_$_INSTANCE_METHODS_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_INSTANCE_METHODS_SBFDIDeviceControlCoordinator
+ __OBJC_$_INSTANCE_METHODS_SBPhoneRLController
+ __OBJC_$_INSTANCE_METHODS_SBPhoneRLView
+ __OBJC_$_INSTANCE_METHODS_SBPhoneRLViewController
+ __OBJC_$_INSTANCE_METHODS_SBPhoneRLWindowSceneDelegate
+ __OBJC_$_INSTANCE_VARIABLES_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_INSTANCE_VARIABLES_SBFDIDeviceControlCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBPhoneRLController
+ __OBJC_$_INSTANCE_VARIABLES_SBPhoneRLView
+ __OBJC_$_INSTANCE_VARIABLES_SBPhoneRLViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBPhoneRLWindowSceneDelegate
+ __OBJC_$_PROP_LIST_SBFDIDeviceControlBacklightInformer
+ __OBJC_$_PROP_LIST_SBFDIDeviceControlCoordinator
+ __OBJC_$_PROP_LIST_SBPhoneRLController
+ __OBJC_$_PROP_LIST_SBPhoneRLView
+ __OBJC_$_PROP_LIST_SBPhoneRLWindowSceneDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SDUDisplayRegionBlankingObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBBacklightInforming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSFDIDeviceControlCoordinating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDUDisplayRegionBlankingObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBBacklightInforming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSFDIDeviceControlCoordinating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SDUDisplayRegionBlankingObserver
+ __OBJC_$_PROTOCOL_REFS_SBBacklightInforming
+ __OBJC_$_PROTOCOL_REFS_SBSFDIDeviceControlCoordinating
+ __OBJC_$_PROTOCOL_REFS_SDUDisplayRegionBlankingObserver
+ __OBJC_CLASS_PROTOCOLS_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_CLASS_PROTOCOLS_$_SBFDIDeviceControlCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_SBPhoneRLController
+ __OBJC_CLASS_PROTOCOLS_$_SBPhoneRLWindowSceneDelegate
+ __OBJC_CLASS_RO_$_SBDeviceEmulationController
+ __OBJC_CLASS_RO_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_CLASS_RO_$_SBFDIDeviceControlCoordinator
+ __OBJC_CLASS_RO_$_SBPhoneRLController
+ __OBJC_CLASS_RO_$_SBPhoneRLView
+ __OBJC_CLASS_RO_$_SBPhoneRLViewController
+ __OBJC_CLASS_RO_$_SBPhoneRLWindowScene
+ __OBJC_CLASS_RO_$_SBPhoneRLWindowSceneDelegate
+ __OBJC_CLASS_RO_$_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_LABEL_PROTOCOL_$_SBBacklightInforming
+ __OBJC_LABEL_PROTOCOL_$_SBSFDIDeviceControlCoordinating
+ __OBJC_LABEL_PROTOCOL_$_SDUDisplayRegionBlankingObserver
+ __OBJC_METACLASS_RO_$_SBDeviceEmulationController
+ __OBJC_METACLASS_RO_$_SBFDIDeviceControlBacklightInformer
+ __OBJC_METACLASS_RO_$_SBFDIDeviceControlCoordinator
+ __OBJC_METACLASS_RO_$_SBPhoneRLController
+ __OBJC_METACLASS_RO_$_SBPhoneRLView
+ __OBJC_METACLASS_RO_$_SBPhoneRLViewController
+ __OBJC_METACLASS_RO_$_SBPhoneRLWindowScene
+ __OBJC_METACLASS_RO_$_SBPhoneRLWindowSceneDelegate
+ __OBJC_METACLASS_RO_$_SBScreenEdgeCompensationDisplayTransformer
+ __OBJC_PROTOCOL_$_SBBacklightInforming
+ __OBJC_PROTOCOL_$_SBSFDIDeviceControlCoordinating
+ __OBJC_PROTOCOL_$_SDUDisplayRegionBlankingObserver
+ __SBDoesTargetSubtypeHavePrefix
+ __SBUseLegacyIslandForScreenType
+ __SBUseLegacyIslandForScreenType.__onceToken
+ __SBUseLegacyIslandForScreenType.__result
+ __UISceneRegionCMCLBodyIdentifierKey
+ ___115-[SBPhoneRLController _modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:forReason:]_block_invoke
+ ___115-[SBPhoneRLController _modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:forReason:]_block_invoke_2
+ ___42-[SBPhoneRLView setPhoneRLWidth:animated:]_block_invoke
+ ___45-[SBPhoneRLController _phoneRLModeDidChange:]_block_invoke
+ ___48-[SBPhoneRLController _phoneRLEnabledDidChange:]_block_invoke
+ ___56-[SBPhoneRLController _phoneRLRecommendedNitsDidChange:]_block_invoke
+ ___57-[SBSAPlatformMetricsContext copyBySettingSensorVariant:]_block_invoke
+ ___58-[SBPhoneRLController createPhoneRLWindowWithWindowScene:]_block_invoke
+ ___58-[SBPhoneRLController createPhoneRLWindowWithWindowScene:]_block_invoke_2
+ ___59-[SBActivationInfoViewController _updateShipModeCompliance]_block_invoke
+ ___59-[SBActivationInfoViewController _updateShipModeCompliance]_block_invoke_2
+ ___85+[SBActivationInfoViewController _queue_readShipModeComplianceSupported:readyToShip:]_block_invoke
+ ___91-[SBPhoneRLController blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:]_block_invoke
+ ___SBShipModeComplianceQueue_block_invoke
+ ____SBUseLegacyIslandForScreenType_block_invoke
+ ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e48_v16?0"UIMutableSceneLayerPresentationContext"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e43_v16?0"UIMutableScenePresentationContext"8ls32l8s40l8s48l8s56l8s64l8
+ __queue_readShipModeComplianceSupported:readyToShip:.onceToken
+ _kCAFillRuleEvenOdd
+ _objc_msgSend$_modifyDefaultPresentationContextHostTransformForWindow:fromTransform:toTransform:forReason:
+ _objc_msgSend$_queue_readShipModeComplianceSupported:readyToShip:
+ _objc_msgSend$_reevaluatePhoneRLActivationStateForReason:
+ _objc_msgSend$_scene:hasEntitlement:
+ _objc_msgSend$_setPhoneRLActive:
+ _objc_msgSend$_setSensorVariant:
+ _objc_msgSend$_setupPhoneRLView
+ _objc_msgSend$_transform
+ _objc_msgSend$_transitionWithTransformer:fromTransform:toTransform:forReason:
+ _objc_msgSend$_updateBacklightRestrictionForWindowScene:wantsRestriction:
+ _objc_msgSend$_updateLiftToWakeForWindowScenes:wantsSuppression:
+ _objc_msgSend$_updateShieldButtonsRestrictionForWindowScenes:wantsRestriction:
+ _objc_msgSend$_updateShipModeCompliance
+ _objc_msgSend$_updateTapToWakeForWindowScenes:wantsSuppression:
+ _objc_msgSend$acquireDisableButtonsAssertionForReason:
+ _objc_msgSend$acquireDisableLiftToWakeAssertionForReason:
+ _objc_msgSend$applyFDIDeviceControlClientSettings:
+ _objc_msgSend$cornerIndicatorEdgeInset
+ _objc_msgSend$createPhoneRLWindowWithWindowScene:
+ _objc_msgSend$deviceContext
+ _objc_msgSend$disablesLiftToWake
+ _objc_msgSend$disablesTapToWake
+ _objc_msgSend$displayContext
+ _objc_msgSend$emulatedDeviceBounds
+ _objc_msgSend$emulatedDeviceClass
+ _objc_msgSend$emulatedDisplayCornerRadius
+ _objc_msgSend$emulatedHomeButtonType
+ _objc_msgSend$hasEmulatedDeviceBounds
+ _objc_msgSend$ignoreWindowForPhoneRL:
+ _objc_msgSend$initWithAssociatedWindowScene:displayRegionBlankingCoordinator:
+ _objc_msgSend$isEmulatedDevice
+ _objc_msgSend$isEuiccActiveWithError:
+ _objc_msgSend$isPhoneRLActive
+ _objc_msgSend$isPhysicalSIMActive
+ _objc_msgSend$isRestricting
+ _objc_msgSend$isScreenEdgeCompensationEnabled
+ _objc_msgSend$phoneRLController
+ _objc_msgSend$phoneRLLayer
+ _objc_msgSend$regionWithIdentifier:referenceFrame:type:active:metadata:
+ _objc_msgSend$registerInformer:
+ _objc_msgSend$requestEUICCHardware:completion:
+ _objc_msgSend$restrictsToConfigurationA
+ _objc_msgSend$sb_configureForDeviceEmulation
+ _objc_msgSend$sceneTransformForWindowScene:
+ _objc_msgSend$sensorVariant
+ _objc_msgSend$setCoordinator:
+ _objc_msgSend$setCurrentMode:preferredMode:otherModes:
+ _objc_msgSend$setDeviceContext:
+ _objc_msgSend$setDisplayContext:
+ _objc_msgSend$setFillRule:
+ _objc_msgSend$setHostingConfiguration:
+ _objc_msgSend$setPhoneRLController:
+ _objc_msgSend$setPhoneRLLayer:
+ _objc_msgSend$setPhoneRLWidth:animated:
+ _objc_msgSend$setRestricting:
+ _objc_msgSend$setSceneTransformLayerConfiguration:
+ _objc_msgSend$setSensorVariant:
+ _objc_msgSend$setUsesEvenOddFillRule:
+ _objc_msgSend$testForcePhoneRLActivate
+ _objc_msgSend$testForcePhoneRLActivateExists
+ _objc_msgSend$transformedConfigurationForConfiguration:
+ _objc_msgSend$unregisterInformer:
+ _objc_msgSend$updatePhoneRLColor
+ _objc_msgSend$updatePhoneRLPath
- -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
- ___block_descriptor_33_e31_v16?0"SSKDisplayPreferences"8l
- _objc_msgSend$_shouldShowAlertForSeed
CStrings:
+ "%{public}@: screen edge compensation transform built: %{BOOL}u"
+ "Adding window to ignored windows list: %{public}@"
+ "Applying root window transform: %{public}@ (from: %{public}@, to: %{public}@)"
+ "Applying screen edge compensation: D76 main display size matched; rewriting bounds from %{public}@ to %{public}@"
+ "B306BF46-7EBA-48D3-A730-C667BF9799C0"
+ "Blanking state changed"
+ "Blanking state will change to: %ld for bundleIDs: %{public}@"
+ "Can't create second RL window."
+ "CoverSheetCommon-V64"
+ "Creating Phone RL window for window scene: %{public}@"
+ "D6A60FD6-4DFA-466A-8F53-0929EF56D20B"
+ "D93VM"
+ "D94VM"
+ "EdgeSwipeBandExpansionEnabled"
+ "Enabled state changed"
+ "Evaluating Phone RL activation state for bundleID: %{public}@, with reason: %{public}@, enabled: %d, mode: %ld, recommendedNits: %f"
+ "FDIDeviceControl"
+ "Force Phone RL testing defaults changed"
+ "IOPSShippingChargeLimitGetState failed: result=0x%x dict=%p"
+ "Mode changed"
+ "No RL window available."
+ "No associated bundle ID, Phone RL activation state remain unchanged"
+ "Only supports one RL window scene"
+ "Phone RL should %{public}@ (auto mode, recommendedNits: %f)"
+ "Phone RL should activate (manual mode)"
+ "Phone RL should not activate: disabled in Control Center for %{public}@"
+ "Phone RL should not activate: display not blanked (state=%ld)"
+ "Phone RL state transition: %{public}@ → %{public}@ (bundleID: %{public}@)"
+ "READY_TO_SHIP"
+ "READY_TO_SHIP_LABEL"
+ "READY_TO_SHIP_NO"
+ "READY_TO_SHIP_YES"
+ "Recommended nits changed"
+ "SBDisableD2026ClassicMode"
+ "SBFDIDeviceControlCoordinator: acquired lift-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: acquired shield-buttons disable across %lu non-main-root window scenes"
+ "SBFDIDeviceControlCoordinator: acquired tap-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: attached FDI device control extension to entitled scene %{public}@"
+ "SBFDIDeviceControlCoordinator: invalidate"
+ "SBFDIDeviceControlCoordinator: powered off + registered wake veto on non-main-root display for scene %{public}@"
+ "SBFDIDeviceControlCoordinator: released lift-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: released shield-buttons disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: released tap-to-wake disable across %lu window scenes"
+ "SBFDIDeviceControlCoordinator: removed wake veto from non-main-root display for scene %{public}@"
+ "SBFDIDeviceControlCoordinator: updating FDI device control (liftToWake=%{BOOL}u tapToWake=%{BOOL}u configurationA=%{BOOL}u) across %lu window scenes"
+ "SBPhoneRLController.m"
+ "SBPhoneRLWindowSceneDelegate.m"
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "Skipping screen edge compensation: isMainD76Display=%{BOOL}u"
+ "TargetSubType"
+ "Tearing down Phone RL window for window scene: %{public}@"
+ "Testing override exists, forcing Phone RL %{public}@ with associated bundleID: %{public}@"
+ "Tried to tear down a window scene thats associated with a different SBWindowScene"
+ "Unable to build screen edge compensated display configuration: %{public}@ from configuration: %{public}@"
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "Unexpected role '%@' for SBPhoneRLWindowSceneDelegate"
+ "Unlock for Share Identity"
+ "V53VM"
+ "V54VM"
+ "V57VM"
+ "V63"
+ "V64"
+ "[SBTelephonyManager] Failed to query isEuiccActive: %{public}@"
+ "[SBTelephonyManager] Failed to request EUICC hardware: %{public}@"
+ "com.apple.Energy"
+ "com.apple.SpringBoard.ship-mode-compliance"
+ "com.apple.springboard.surface1"
+ "com.apple.springboard.surface2"
+ "iPhone RL is %@"
+ "not activate"
+ "sensorVariant"
+ "testForcePhoneRLActivate"
```
