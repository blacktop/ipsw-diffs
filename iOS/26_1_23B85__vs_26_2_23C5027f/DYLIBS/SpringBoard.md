## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.1.19.109.0
-  __TEXT.__text: 0xa928a8
-  __TEXT.__auth_stubs: 0x55b0
+4557.2.2.101.0
+  __TEXT.__text: 0xa92018
+  __TEXT.__auth_stubs: 0x5590
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb8118
-  __TEXT.__const: 0x12f30
-  __TEXT.__oslogstring: 0x5e404
-  __TEXT.__cstring: 0x7d1ef
-  __TEXT.__gcc_except_tab: 0x19690
+  __TEXT.__objc_methlist: 0xb80a0
+  __TEXT.__const: 0x12f40
+  __TEXT.__oslogstring: 0x5e4c8
+  __TEXT.__cstring: 0x7d254
+  __TEXT.__gcc_except_tab: 0x1969c
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__unwind_info: 0x2c5c0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x2223b
-  __TEXT.__objc_methname: 0x1d1838
-  __TEXT.__objc_methtype: 0x4d12c
-  __TEXT.__objc_stubs: 0xf5000
-  __DATA_CONST.__got: 0xa2e8
-  __DATA_CONST.__const: 0x1cb58
-  __DATA_CONST.__objc_classlist: 0x5280
-  __DATA_CONST.__objc_catlist: 0x380
+  __TEXT.__objc_classname: 0x2220f
+  __TEXT.__objc_methname: 0x1d1695
+  __TEXT.__objc_methtype: 0x4d132
+  __TEXT.__objc_stubs: 0xf4e00
+  __DATA_CONST.__got: 0xa2f0
+  __DATA_CONST.__const: 0x1cb98
+  __DATA_CONST.__objc_classlist: 0x5278
+  __DATA_CONST.__objc_catlist: 0x368
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b028
+  __DATA_CONST.__objc_selrefs: 0x4af88
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fa8
+  __DATA_CONST.__objc_superrefs: 0x3fa0
   __DATA_CONST.__objc_arraydata: 0x1868
-  __AUTH_CONST.__auth_got: 0x2af0
-  __AUTH_CONST.__const: 0x10c58
-  __AUTH_CONST.__cfstring: 0x6f180
-  __AUTH_CONST.__objc_const: 0x26b878
+  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__const: 0x10c78
+  __AUTH_CONST.__cfstring: 0x6f1a0
+  __AUTH_CONST.__objc_const: 0x26b6f8
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x770
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x107c0
-  __DATA.__objc_ivar: 0xf488
+  __AUTH.__objc_data: 0x10770
+  __DATA.__objc_ivar: 0xf484
   __DATA.__data: 0x1f8b8
-  __DATA.__bss: 0xaa0
+  __DATA.__bss: 0xab0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x23140
   __DATA_DIRTY.__data: 0x180

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NotificationCenter.framework/NotificationCenter
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: F692FE14-DE59-3E46-BF44-5CEF681D64A3
-  Functions: 70267
-  Symbols:   237730
-  CStrings:  104531
+  UUID: 6E2A351D-2519-33A7-B1AF-5F9704146E1D
+  Functions: 70264
+  Symbols:   237698
+  CStrings:  104514
 
Symbols:
+ -[SBApplication iconShouldBeDimmed:]
+ -[SBApplication isDemoScreenSaverApplication]
+ -[SBApplication isWebBrowser]
+ -[SBApplicationInfo isDemoScreenSaverApplication]
+ -[SBApplicationInfo isDemoScreenSaverApplication].cold.1
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController dismiss]
+ -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
+ -[SBMainWorkspaceTransitionRequest setShouldBypassAgeRestriction:]
+ -[SBMainWorkspaceTransitionRequest shouldBypassAgeRestriction]
+ -[SBUIController _accessoryEndpointAttached:reportToLockScreen:]
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table184
+ GCC_except_table92
+ _OBJC_CLASS_$_APRequestHandler
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._cachedAppLayoutsGenCount
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._cachedAppLayoutsGenCount
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._selectedIndex
+ _OBJC_IVAR_$_SBMainWorkspaceTransitionRequest._shouldBypassAgeRestriction
+ _SBExperiencesBundleIdentifier
+ _SBExploreBundleIdentifier
+ _SBLaunchAppBypassAgeRestrictionEntitlement
+ _SBSOpenApplicationOptionKeyBypassAgeRestriction
+ __SBWorkspaceCanLaunchApplicationWithValidScene
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.1
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.2
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.3
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.4
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.5
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.6
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.7
+ __SBWorkspaceCanLaunchApplicationWithValidScene.cold.8
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.255
+ ___49-[SBApplicationInfo isDemoScreenSaverApplication]_block_invoke
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.393
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.396
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.395
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.509
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.516
+ ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.385
+ ___64-[SBUIController _accessoryEndpointAttached:reportToLockScreen:]_block_invoke
+ ___64-[SBUIController _accessoryEndpointAttached:reportToLockScreen:]_block_invoke.293
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.402
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.424
+ ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.477
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.454
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.649
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.671
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.686
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.690
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.698
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.405
+ ____SBWorkspaceCanLaunchApplication_block_invoke
+ ___block_descriptor_40_e8_32s_e31_v28?0B8"NSUUID"12"NSError"20ls32l8
+ ___block_literal_global.1204
+ ___block_literal_global.1252
+ ___block_literal_global.249
+ ___block_literal_global.254
+ ___block_literal_global.255
+ ___block_literal_global.258
+ ___block_literal_global.306
+ ___block_literal_global.318
+ ___block_literal_global.476
+ ___block_literal_global.480
+ ___block_literal_global.500
+ ___block_literal_global.809
+ ___block_literal_global.816
+ ___block_literal_global.821
+ ___block_literal_global.823
+ _isDemoScreenSaverApplication.demoScreenSaverApplicationBundleIdentifiers
+ _isDemoScreenSaverApplication.onceToken
+ _objc_msgSend$_accessoryEndpointAttached:reportToLockScreen:
+ _objc_msgSend$_shouldShowAlertForSeed
+ _objc_msgSend$addExceptionRequestWithUUID:type:bundleIdentifier:withCompletion:
+ _objc_msgSend$iconAllowsLaunch:
+ _objc_msgSend$isDemoScreenSaverApplication
+ _objc_msgSend$isWebBrowser
+ _objc_msgSend$performSelector:withObject:withObject:
+ _objc_msgSend$setShouldBypassAgeRestriction:
+ _objc_msgSend$shouldBypassAgeRestriction
- +[SBDeviceEmulationController applicationInitializationContext]
- +[SBDeviceEmulationController deviceContext]
- +[SBDeviceEmulationController displayContext]
- -[SBMainDisplayConfigurationTransformer transformDisplayConfiguration:].cold.2
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
- GCC_except_table169
- GCC_except_table178
- GCC_except_table186
- _FBSDisplayRotationFromRadians
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_SBDeviceEmulationController
- _OBJC_IVAR_$_SBFullScreenSwitcherSceneLiveContentOverlay._activeAppearance
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
- __SBWorkspaceCanLaunchApplication.cold.2
- __SBWorkspaceCanLaunchApplication.cold.3
- __SBWorkspaceCanLaunchApplication.cold.4
- __SBWorkspaceCanLaunchApplication.cold.5
- __SBWorkspaceCanLaunchApplication.cold.6
- __SBWorkspaceCanLaunchApplication.cold.7
- __SBWorkspaceCanLaunchApplication.cold.8
- ___45-[SBUIController _accessoryEndpointAttached:]_block_invoke
- ___45-[SBUIController _accessoryEndpointAttached:]_block_invoke.293
- ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.254
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.392
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.395
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.394
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.500
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.507
- ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.376
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.401
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.423
- ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.468
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.453
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.640
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.662
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.677
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.681
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.689
- ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.404
- ___block_literal_global.1195
- ___block_literal_global.1243
- ___block_literal_global.246
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.305
- ___block_literal_global.309
- ___block_literal_global.387
- ___block_literal_global.467
- ___block_literal_global.471
- ___block_literal_global.499
- ___block_literal_global.800
- ___block_literal_global.805
- ___block_literal_global.807
- _colorForSpecifierString
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
+ "Attempted to launch age restricted application %{public}@"
+ "Cannot launch %{public}@, pending browser choice"
+ "Launch age restricted application %{public}@ with bypass option"
+ "Q1a"
+ "Request ask permission alert for: %{public}@ succeeded %u with error %@"
+ "SFDefaultBrowserRemoteAlertService"
+ "Should show browser choice"
+ "TB,N,V_shouldBypassAgeRestriction"
+ "TB,R,N,GisDemoScreenSaverApplication"
+ "TB,R,N,GisLaunchDisallowedForRatingRank"
+ "TB,R,N,GisWebBrowser"
+ "_accessoryEndpointAttached:reportToLockScreen:"
+ "_cachedAppLayoutsGenCount"
+ "_shouldBypassAgeRestriction"
+ "_shouldShowAlertForSeed"
+ "addExceptionRequestWithUUID:type:bundleIdentifier:withCompletion:"
+ "com.apple.ist.DemoDiscoveryApp"
+ "com.apple.springboard.launchAppBypassAgeRestriction"
+ "com.retailtech.arkenstone"
+ "createDefaultBrowserRemoteAlertWithBundleID:URL:"
+ "demoScreenSaverApplication"
+ "iconShouldBeDimmed:"
+ "isDemoScreenSaverApplication"
+ "isWebBrowser"
+ "launchDisallowedForRatingRank"
+ "setShouldBypassAgeRestriction:"
+ "shouldBypassAgeRestriction"
+ "shouldCreateDefaultBrowserRemoteAlert"
+ "v28@?0B8@\"NSUUID\"12@\"NSError\"20"
+ "webBrowser"
+ "{vector<std::vector<BezierCurve>, std::allocator<std::vector<BezierCurve>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
- "%@Color"
- "%x"
- "([\\dA-F]{6})"
- "DeviceEmulation"
- "Q1q"
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
- "_updateRootLayerBackgroundColor"
- "_updateTransformLayer"
- "applicationInitializationContext"
- "bezelLayer"
- "com.apple.springboard.private.ringer-button-events"
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
- "{vector<std::vector<BezierCurve>, std::allocator<std::vector<BezierCurve>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"

```
