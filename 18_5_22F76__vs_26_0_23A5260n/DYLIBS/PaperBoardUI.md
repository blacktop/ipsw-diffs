## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-228.5.12.0.0
-  __TEXT.__text: 0x7f6dc
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x9fe4
-  __TEXT.__const: 0x8d8
-  __TEXT.__cstring: 0x71b3
-  __TEXT.__oslogstring: 0x4083
-  __TEXT.__gcc_except_tab: 0x1294
-  __TEXT.__dlopen_cstrs: 0x31c
-  __TEXT.__unwind_info: 0x2ac8
-  __TEXT.__objc_classname: 0x1798
-  __TEXT.__objc_methname: 0x16eb9
-  __TEXT.__objc_methtype: 0x456c
-  __TEXT.__objc_stubs: 0x11d40
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x27a8
-  __DATA_CONST.__objc_classlist: 0x3f8
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x268
+276.105.0.0.0
+  __TEXT.__text: 0x7ef28
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x9edc
+  __TEXT.__const: 0x838
+  __TEXT.__cstring: 0x781f
+  __TEXT.__oslogstring: 0x41fa
+  __TEXT.__gcc_except_tab: 0x119c
+  __TEXT.__dlopen_cstrs: 0x1a6
+  __TEXT.__unwind_info: 0x2b20
+  __TEXT.__objc_classname: 0x15f0
+  __TEXT.__objc_methname: 0x177c4
+  __TEXT.__objc_methtype: 0x405e
+  __TEXT.__objc_stubs: 0x11c20
+  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__const: 0x2898
+  __DATA_CONST.__objc_classlist: 0x3c8
+  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52e8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0xb58
-  __AUTH_CONST.__cfstring: 0x6920
-  __AUTH_CONST.__objc_const: 0x1dbf8
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH.__objc_data: 0x2300
+  __DATA_CONST.__objc_selrefs: 0x52b8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_arraydata: 0x1c8
+  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0x62a0
+  __AUTH_CONST.__objc_const: 0x1c528
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_doubleobj: 0x90
+  __AUTH.__objc_data: 0x2210
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x9f8
-  __DATA.__data: 0x1d00
-  __DATA.__bss: 0x3a0
-  __DATA_DIRTY.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0xa18
+  __DATA.__data: 0x18e0
+  __DATA.__bss: 0x3f8
+  __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCEDAB0F-C5B5-35FF-B60B-23523EE3D2BE
-  Functions: 3890
-  Symbols:   13772
-  CStrings:  6543
+  UUID: 299A3A42-44F9-3643-AA18-6345FF966986
+  Functions: 3930
+  Symbols:   13615
+  CStrings:  6462
 
Symbols:
+ +[PBUIHomeVariantStyleState stateWithTintColorStyle:suggestedTintColor:tintSource:isHomeScreenDimmed:iconSize:iconStyle:iconStyleVariant:lastUserSelectedVariantForStyleTypeOption:]
+ +[PBUIPosterHUDController isHUDEnabled]
+ +[PBUIPosterHUDController sharedInstance]
+ +[_PBUIDimmingView layerClass]
+ -[PBUIHUDWindow .cxx_destruct]
+ -[PBUIHUDWindow hitTest:withEvent:]
+ -[PBUIHUDWindow hitTestViews]
+ -[PBUIHUDWindow setHitTestViews:]
+ -[PBUIHomeVariantStyleState iconStyleVariant]
+ -[PBUIHomeVariantStyleState initWithTintColorStyle:suggestedTintColor:tintSource:isHomeScreenDimmed:iconSize:iconStyle:iconStyleVariant:lastUserSelectedVariantForStyleTypeOption:]
+ -[PBUIHomeVariantStyleState lastUserSelectedVariantForStyleTypeOption]
+ -[PBUIHomeVariantStyleState tintSource]
+ -[PBUIPosterHUDController .cxx_destruct]
+ -[PBUIPosterHUDController _updateOrientation]
+ -[PBUIPosterHUDController containerView]
+ -[PBUIPosterHUDController handlePanGesture:]
+ -[PBUIPosterHUDController hideHUD]
+ -[PBUIPosterHUDController hudWindow]
+ -[PBUIPosterHUDController init]
+ -[PBUIPosterHUDController isHUDVisible]
+ -[PBUIPosterHUDController lastPosition]
+ -[PBUIPosterHUDController panGestureRecognizer]
+ -[PBUIPosterHUDController posterActiveLabel]
+ -[PBUIPosterHUDController setContainerView:]
+ -[PBUIPosterHUDController setHudWindow:]
+ -[PBUIPosterHUDController setIsHUDVisible:]
+ -[PBUIPosterHUDController setLastPosition:]
+ -[PBUIPosterHUDController setPanGestureRecognizer:]
+ -[PBUIPosterHUDController setPosterActiveLabel:]
+ -[PBUIPosterHUDController setupAndShowHUDWindow]
+ -[PBUIPosterHUDController showHUDIfEnabled]
+ -[PBUIPosterHUDController updateWithLockSceneActivityMode:homeSceneActivityMode:activeVariant:wallpaperStyle:homeAndLockAreSame:isActivelyRequired:activelyRequiredReasons:assertionReasons:]
+ -[PBUIPosterHomeViewController _updateDimHomeScreenWallpaperViewAnimated]
+ -[PBUIPosterHomeViewController _updatedDimStyle]
+ -[PBUIPosterHomeViewController init]
+ -[PBUIPosterHomeViewController isDimmed]
+ -[PBUIPosterHomeViewController updatePresentation:]
+ -[PBUIPosterHomeViewController updatePresentation:].cold.1
+ -[PBUIPosterLockViewController _motionEffectWithFactor:]
+ -[PBUIPosterLockViewController _updatePosterLayers]
+ -[PBUIPosterLockViewController areMotionEffectsEnabled]
+ -[PBUIPosterLockViewController removeAllMotionEffects]
+ -[PBUIPosterLockViewController setMotionEffectsEnabled:]
+ -[PBUIPosterLockViewController setMotionEffectsWithFloating:foreground:background:]
+ -[PBUIPosterLockViewController updatePresentation:]
+ -[PBUIPosterSceneLayerHostView .cxx_destruct]
+ -[PBUIPosterSceneLayerHostView cacheIdentifier]
+ -[PBUIPosterSceneLayerHostView contextID]
+ -[PBUIPosterSceneLayerHostView effectsAreBakedIn]
+ -[PBUIPosterSceneLayerHostView identifier]
+ -[PBUIPosterSceneLayerHostView invalidate]
+ -[PBUIPosterSceneLayerHostView legibilitySettings]
+ -[PBUIPosterSceneLayerHostView scene]
+ -[PBUIPosterSceneLayerHostView setContextID:]
+ -[PBUIPosterSceneLayerHostView setContextID:scene:]
+ -[PBUIPosterSceneLayerHostView setIdentifier:]
+ -[PBUIPosterSceneLayerHostView setScene:]
+ -[PBUIPosterSceneLayerHostView targetView]
+ -[PBUIPosterVariantViewController _checkIfPresentationIsUpdatedAndSnapshot]
+ -[PBUIPosterVariantViewController _updateEffectiveMotionEffectsModeForSupportedMode:disabled:]
+ -[PBUIPosterVariantViewController adaptiveTimeHonorsPreferredSalientContentRectangle]
+ -[PBUIPosterVariantViewController preferredDeviceMotionUpdateInterval]
+ -[PBUIPosterVariantViewController preferredSalientContentRectangle]
+ -[PBUIPosterVariantViewController snapshotIfNeeded:].cold.2
+ -[PBUIPosterVariantViewController updatePresentation:]
+ -[PBUIPosterViewController _finalizeActiveVariantTransitionWithReason:]
+ -[PBUIPosterViewController _invalidateComponents]
+ -[PBUIPosterViewController _isSceneContentReady]
+ -[PBUIPosterViewController _prepareActiveVariantTransition]
+ -[PBUIPosterViewController _updateActivePosterSceneMode]
+ -[PBUIPosterViewController _updateActiveVariantTransitionProgress:]
+ -[PBUIPosterViewController _updateDebugHUD]
+ -[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]
+ -[PBUIPosterViewController _userInterfaceStyleTraitDidChange:previousTraitCollection:]
+ -[PBUIPosterViewController activelyRequiredReasons]
+ -[PBUIPosterViewController adaptiveTimeHonorsPreferredSalientContentRectangle]
+ -[PBUIPosterViewController beginActiveVariantTransition]
+ -[PBUIPosterViewController deviceMotionEventGenerationDidStop]
+ -[PBUIPosterViewController deviceMotionEventGenerationWillStart]
+ -[PBUIPosterViewController deviceMotionUpdateInterval]
+ -[PBUIPosterViewController devicePitch]
+ -[PBUIPosterViewController deviceRoll]
+ -[PBUIPosterViewController deviceYaw]
+ -[PBUIPosterViewController endActiveVariantTransition]
+ -[PBUIPosterViewController hasRequestedDeviceMotionEvents]
+ -[PBUIPosterViewController isTransitioningActiveVariant]
+ -[PBUIPosterViewController posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:]
+ -[PBUIPosterViewController posterComponent:didUpdateDeviceMotionEventsRequested:]
+ -[PBUIPosterViewController posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:]
+ -[PBUIPosterViewController posterComponent:didUpdatePreferredSalientContentRectangle:]
+ -[PBUIPosterViewController posterComponent:didUpdateSalientContentRectangleUpdatesRequested:]
+ -[PBUIPosterViewController preferredDeviceMotionUpdateInterval]
+ -[PBUIPosterViewController preferredSalientContentRectangle]
+ -[PBUIPosterViewController renderingServiceEndpoint]
+ -[PBUIPosterViewController rotation]
+ -[PBUIPosterViewController salientContentRectangleUpdatesRequested]
+ -[PBUIPosterViewController salientContentRectangle]
+ -[PBUIPosterViewController scene:didUpdateSettings:]
+ -[PBUIPosterViewController setActivelyRequiredReasons:]
+ -[PBUIPosterViewController setDeviceMotionUpdateInterval:]
+ -[PBUIPosterViewController setDevicePitch:]
+ -[PBUIPosterViewController setDeviceRoll:]
+ -[PBUIPosterViewController setDeviceYaw:]
+ -[PBUIPosterViewController setRenderingServiceEndpoint:]
+ -[PBUIPosterViewController setRotation:]
+ -[PBUIPosterViewController setSalientContentRectangle:]
+ -[PBUIPosterViewController setTransitioningActiveVariant:]
+ -[PBUIPosterViewController updateActiveVariantTransitionProgress:]
+ -[PBUIPosterViewController updateMotionWithRotation:]
+ -[PBUIPosterViewController updateMotionWithRotation:].cold.1
+ -[PBUIPosterViewController wantsDefaultParallaxTreatment]
+ -[PBUIPosterWallpaperRemoteViewController _fireObserverRespondingToSelector:variant:block:]
+ -[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperDidChangeForVariant:]
+ -[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperDidChange]
+ -[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperWillChangeForVariant:]
+ -[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperWillChange]
+ -[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]
+ -[PBUIPosterWallpaperRemoteViewController _observerLock_observersForVariant:]
+ -[PBUIPosterWallpaperRemoteViewController adaptiveTimeHonorsPreferredSalientContentRectangle]
+ -[PBUIPosterWallpaperRemoteViewController beginActiveVariantTransition]
+ -[PBUIPosterWallpaperRemoteViewController deviceMotionUpdateInterval]
+ -[PBUIPosterWallpaperRemoteViewController endActiveVariantTransition]
+ -[PBUIPosterWallpaperRemoteViewController hostDidEndDeviceMotionEventGeneration]
+ -[PBUIPosterWallpaperRemoteViewController hostWillStartDeviceMotionEventGeneration]
+ -[PBUIPosterWallpaperRemoteViewController legibilityEnvironment]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateDeviceMotionEventsRequested:]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdatePreferredSalientContentRectangle:]
+ -[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateSalientContentRectangleUpdatesRequested:]
+ -[PBUIPosterWallpaperRemoteViewController posterHasRequestedDeviceMotionEvents]
+ -[PBUIPosterWallpaperRemoteViewController posterWantsDefaultParallax]
+ -[PBUIPosterWallpaperRemoteViewController preferredDeviceMotionUpdateInterval]
+ -[PBUIPosterWallpaperRemoteViewController preferredSalientContentRectangle]
+ -[PBUIPosterWallpaperRemoteViewController setDeviceMotionUpdateInterval:]
+ -[PBUIPosterWallpaperRemoteViewController updateActiveVariantTransitionProgress:]
+ -[PBUIPosterWallpaperRemoteViewController updateSalientContentRectangle:]
+ -[PBUIPosterWallpaperRemoteViewController updateWallpaperAnimationWithPitch:roll:yaw:]
+ -[PBUIPosterWallpaperRemoteViewController updateWallpaperAnimationWithRotation:]
+ -[PBUIPosterWallpaperViewController adaptiveTimeHonorsPreferredSalientContentRectangle]
+ -[PBUIPosterWallpaperViewController beginActiveVariantTransition]
+ -[PBUIPosterWallpaperViewController deviceMotionUpdateInterval]
+ -[PBUIPosterWallpaperViewController devicePitch]
+ -[PBUIPosterWallpaperViewController deviceRoll]
+ -[PBUIPosterWallpaperViewController deviceYaw]
+ -[PBUIPosterWallpaperViewController endActiveVariantTransition]
+ -[PBUIPosterWallpaperViewController isDeviceMotionEventGenerationActive]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdateDeviceMotionEventsRequested:]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdatePreferredSalientContentRectangle:]
+ -[PBUIPosterWallpaperViewController posterComponent:didUpdateSalientContentRectangleUpdatesRequested:]
+ -[PBUIPosterWallpaperViewController posterHasRequestedDeviceMotionEvents]
+ -[PBUIPosterWallpaperViewController posterWantsDefaultParallax]
+ -[PBUIPosterWallpaperViewController preferredDeviceMotionUpdateInterval]
+ -[PBUIPosterWallpaperViewController preferredSalientContentRectangle]
+ -[PBUIPosterWallpaperViewController salientContentRectangle]
+ -[PBUIPosterWallpaperViewController setDeviceMotionEventGenerationActive:]
+ -[PBUIPosterWallpaperViewController setDeviceMotionUpdateInterval:]
+ -[PBUIPosterWallpaperViewController setDevicePitch:]
+ -[PBUIPosterWallpaperViewController setDevicePitch:roll:yaw:]
+ -[PBUIPosterWallpaperViewController setDeviceRoll:]
+ -[PBUIPosterWallpaperViewController setDeviceYaw:]
+ -[PBUIPosterWallpaperViewController setRotation:]
+ -[PBUIPosterWallpaperViewController setSalientContentRectangle:]
+ -[PBUIPosterWallpaperViewController updateActiveVariantTransitionProgress:]
+ -[PBUIWallpaperEffectViewBase wallpaperLegibilityEnvironmentDidChange:]
+ -[PBUIWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]
+ -[PBUIWallpaperRemoteViewController currentHomeVariantStyleState]
+ -[PBUIWallpaperRemoteViewController legibilityEnvironment]
+ -[PBUIWallpaperView legibilityEnvironment]
+ -[PBUIWallpaperViewController _updateInactiveBlurEffectForWallpaperMode:]
+ -[PBUIWallpaperViewController currentHomeVariantStyleState]
+ -[PBUIWallpaperViewController loadView]
+ -[PBUIWallpaperViewController setExternalDisplayConfiguration:]
+ -[_PBUIDimmingView .cxx_destruct]
+ -[_PBUIDimmingView initWithFrame:]
+ -[_PBUIDimmingView setDim:animated:]
+ -[_PBUIDimmingView setUseDimStyle:]
+ -[_PBUIDimmingView setUseDimmingColorMatrix:]
+ -[_PBUIDimmingView useDimmingColorMatrix]
+ -[_PBUIWallpaperBlurAnimatingView _shouldAnimatePropertyWithKey:]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table176
+ GCC_except_table186
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table98
+ _BSFloatGreaterThanFloat
+ _NSStringFromFBSSceneActivityMode
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_PBUIHUDWindow
+ _OBJC_CLASS_$_PBUIPosterHUDController
+ _OBJC_CLASS_$_PBUIPosterSceneLayerHostView
+ _OBJC_CLASS_$_UICubicTimingParameters
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$_UIViewPropertyAnimator
+ _OBJC_CLASS_$_UIWindow
+ _OBJC_CLASS_$__PBUIDimmingView
+ _OBJC_CLASS_$__PBUIWallpaperBlurAnimatingView
+ _OBJC_IVAR_$_PBUIHUDWindow._hitTestViews
+ _OBJC_IVAR_$_PBUIHomeVariantStyleState._iconStyleVariant
+ _OBJC_IVAR_$_PBUIHomeVariantStyleState._lastUserSelectedVariantForStyleTypeOption
+ _OBJC_IVAR_$_PBUIHomeVariantStyleState._tintSource
+ _OBJC_IVAR_$_PBUIPosterHUDController._containerView
+ _OBJC_IVAR_$_PBUIPosterHUDController._hudWindow
+ _OBJC_IVAR_$_PBUIPosterHUDController._isHUDVisible
+ _OBJC_IVAR_$_PBUIPosterHUDController._lastPosition
+ _OBJC_IVAR_$_PBUIPosterHUDController._panGestureRecognizer
+ _OBJC_IVAR_$_PBUIPosterHUDController._posterActiveLabel
+ _OBJC_IVAR_$_PBUIPosterHomeViewController._homeScreenDimStyle
+ _OBJC_IVAR_$_PBUIPosterLockViewController._backgroundEffect
+ _OBJC_IVAR_$_PBUIPosterLockViewController._floatingEffect
+ _OBJC_IVAR_$_PBUIPosterLockViewController._foregroundEffect
+ _OBJC_IVAR_$_PBUIPosterLockViewController._motionEffectsEnabled
+ _OBJC_IVAR_$_PBUIPosterLockViewController._realBackgroundView
+ _OBJC_IVAR_$_PBUIPosterLockViewController._realForegroundView
+ _OBJC_IVAR_$_PBUIPosterSceneLayerHostView._contextID
+ _OBJC_IVAR_$_PBUIPosterSceneLayerHostView._identifier
+ _OBJC_IVAR_$_PBUIPosterSceneLayerHostView._presenter
+ _OBJC_IVAR_$_PBUIPosterSceneLayerHostView._scene
+ _OBJC_IVAR_$_PBUIPosterViewController._activePosterSceneDefaultModeAssertion
+ _OBJC_IVAR_$_PBUIPosterViewController._activelyRequiredReasons
+ _OBJC_IVAR_$_PBUIPosterViewController._deviceMotionUpdateInterval
+ _OBJC_IVAR_$_PBUIPosterViewController._devicePitch
+ _OBJC_IVAR_$_PBUIPosterViewController._deviceRoll
+ _OBJC_IVAR_$_PBUIPosterViewController._deviceYaw
+ _OBJC_IVAR_$_PBUIPosterViewController._renderingServiceEndpoint
+ _OBJC_IVAR_$_PBUIPosterViewController._renderingServiceSceneComponent
+ _OBJC_IVAR_$_PBUIPosterViewController._renderingServiceServerKeepAliveAssertionManager
+ _OBJC_IVAR_$_PBUIPosterViewController._rotation
+ _OBJC_IVAR_$_PBUIPosterViewController._salientContentRectangle
+ _OBJC_IVAR_$_PBUIPosterViewController._transitioningActiveVariant
+ _OBJC_IVAR_$_PBUIPosterViewController._unlockingKeepRunningAssertion
+ _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._currentLegibilityEnvironment
+ _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._deviceMotionUpdateInterval
+ _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._legibilityEnvironmentBuilder
+ _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._observerLock_homeScreenObservers
+ _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._observerLock_lockScreenObservers
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._deviceMotionEventGenerationActive
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._deviceMotionUpdateInterval
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._devicePitch
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._deviceRoll
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._deviceYaw
+ _OBJC_IVAR_$_PBUIPosterWallpaperViewController._salientContentRectangle
+ _OBJC_IVAR_$_PBUIWallpaperRemoteViewController._currentHomeVariantStyleState
+ _OBJC_IVAR_$_PBUIWallpaperRemoteViewController._currentLegibilityEnvironment
+ _OBJC_IVAR_$_PBUIWallpaperRemoteViewController._legibilityEnvironmentBuilder
+ _OBJC_IVAR_$_PBUIWallpaperViewController._currentHomeVariantStyleState
+ _OBJC_IVAR_$__PBUIDimmingView._currentDimStyle
+ _OBJC_IVAR_$__PBUIDimmingView._dimmingColorMatrixFilter
+ _OBJC_IVAR_$__PBUIDimmingView._luminanceCurveMapFilter
+ _OBJC_IVAR_$__PBUIDimmingView._saturationFilter
+ _OBJC_IVAR_$__PBUIDimmingView._useDimmingColorMatrix
+ _OBJC_METACLASS_$_PBUIHUDWindow
+ _OBJC_METACLASS_$_PBUIPosterHUDController
+ _OBJC_METACLASS_$_PBUIPosterSceneLayerHostView
+ _OBJC_METACLASS_$_UIWindow
+ _OBJC_METACLASS_$__PBUIDimmingView
+ _OBJC_METACLASS_$__PBUIWallpaperBlurAnimatingView
+ _PBUILogRuntime
+ _PBUILogRuntime.__logObj
+ _PBUILogRuntime.cold.1
+ _PBUILogRuntime.onceToken
+ _PosterFuturesKitLibrary
+ _PosterFuturesKitLibrary.cold.1
+ _PosterFuturesKitLibraryCore
+ _PosterFuturesKitLibraryCore.frameworkLibrary
+ _PosterKitLibrary
+ _PosterKitLibrary.cold.1
+ _PosterKitLibraryCore
+ _PosterKitLibraryCore.frameworkLibrary
+ _PosterLegibilityKitLibrary
+ _PosterLegibilityKitLibrary.cold.1
+ _PosterLegibilityKitLibraryCore
+ _PosterLegibilityKitLibraryCore.frameworkLibrary
+ __BSIsInternalInstall
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_FBSMutableSceneSettings_$_PaperBoard
+ __OBJC_$_CLASS_METHODS_PBUIPosterHUDController
+ __OBJC_$_CLASS_METHODS__PBUIDimmingView
+ __OBJC_$_INSTANCE_METHODS_PBUIHUDWindow
+ __OBJC_$_INSTANCE_METHODS_PBUIPosterHUDController
+ __OBJC_$_INSTANCE_METHODS_PBUIPosterSceneLayerHostView
+ __OBJC_$_INSTANCE_METHODS__PBUIDimmingView
+ __OBJC_$_INSTANCE_METHODS__PBUIWallpaperBlurAnimatingView
+ __OBJC_$_INSTANCE_VARIABLES_PBUIHUDWindow
+ __OBJC_$_INSTANCE_VARIABLES_PBUIPosterHUDController
+ __OBJC_$_INSTANCE_VARIABLES_PBUIPosterSceneLayerHostView
+ __OBJC_$_INSTANCE_VARIABLES__PBUIDimmingView
+ __OBJC_$_PROP_LIST_PBUIHUDWindow
+ __OBJC_$_PROP_LIST_PBUIPosterHUDController
+ __OBJC_$_PROP_LIST_PBUIPosterSceneLayerHostView
+ __OBJC_$_PROP_LIST_PBUIWallpaperLegibilityProviding
+ __OBJC_$_PROP_LIST__PBUIDimmingView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PBUIWallpaperLegibilityProviding
+ __OBJC_CLASS_PROTOCOLS_$_PBUIPosterSceneLayerHostView
+ __OBJC_CLASS_RO_$_PBUIHUDWindow
+ __OBJC_CLASS_RO_$_PBUIPosterHUDController
+ __OBJC_CLASS_RO_$_PBUIPosterSceneLayerHostView
+ __OBJC_CLASS_RO_$__PBUIDimmingView
+ __OBJC_CLASS_RO_$__PBUIWallpaperBlurAnimatingView
+ __OBJC_METACLASS_RO_$_PBUIHUDWindow
+ __OBJC_METACLASS_RO_$_PBUIPosterHUDController
+ __OBJC_METACLASS_RO_$_PBUIPosterSceneLayerHostView
+ __OBJC_METACLASS_RO_$__PBUIDimmingView
+ __OBJC_METACLASS_RO_$__PBUIWallpaperBlurAnimatingView
+ __UISolariumEnabled
+ ___101-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdatePreferredSalientContentRectangle:]_block_invoke
+ ___102-[PBUIPosterWallpaperViewController posterComponent:didUpdateSalientContentRectangleUpdatesRequested:]_block_invoke
+ ___104-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:]_block_invoke
+ ___109-[PBUIPosterVariantViewController scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke
+ ___119-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:]_block_invoke
+ ___32-[PBUIPosterViewController init]_block_invoke_8
+ ___36-[_PBUIDimmingView setDim:animated:]_block_invoke
+ ___41+[PBUIPosterHUDController sharedInstance]_block_invoke
+ ___43-[PBUIPosterViewController updateHomeScene]_block_invoke.70
+ ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke.51
+ ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke_3
+ ___51-[PBUIPosterHomeViewController updatePresentation:]_block_invoke
+ ___51-[PBUIPosterHomeViewController updatePresentation:]_block_invoke.cold.1
+ ___51-[PBUIPosterSceneLayerHostView setContextID:scene:]_block_invoke
+ ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke.87
+ ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke_2.88
+ ___61-[PBUIPosterViewController willRotateToInterfaceOrientation:]_block_invoke_2
+ ___61-[PBUIPosterWallpaperViewController setDevicePitch:roll:yaw:]_block_invoke
+ ___63-[PBUIPosterWallpaperViewController endActiveVariantTransition]_block_invoke
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.220
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.220.cold.1
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.221
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.235
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.249
+ ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke_2.236
+ ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.75
+ ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.78
+ ___64-[PBUIPosterWallpaperViewController setSalientContentRectangle:]_block_invoke
+ ___65-[PBUIPosterWallpaperViewController beginActiveVariantTransition]_block_invoke
+ ___67-[PBUIPosterWallpaperViewController setDeviceMotionUpdateInterval:]_block_invoke
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.151
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.152
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.153
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.156
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.160
+ ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.169
+ ___73-[PBUIWallpaperViewController _updateInactiveBlurEffectForWallpaperMode:]_block_invoke
+ ___73-[PBUIWallpaperViewController _updateInactiveBlurEffectForWallpaperMode:]_block_invoke.44
+ ___75-[PBUIPosterVariantViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3
+ ___75-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperDidChange]_block_invoke
+ ___75-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperDidChange]_block_invoke_2
+ ___75-[PBUIPosterWallpaperViewController updateActiveVariantTransitionProgress:]_block_invoke
+ ___76-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperWillChange]_block_invoke
+ ___76-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperWillChange]_block_invoke_2
+ ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke
+ ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke.116
+ ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke_2
+ ___77-[PBUIPosterViewController _updatePosterScenesForReasons:updater:completion:]_block_invoke_3
+ ___85-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateHideDimmingLayer:]_block_invoke
+ ___86-[PBUIPosterViewController _userInterfaceStyleTraitDidChange:previousTraitCollection:]_block_invoke
+ ___86-[PBUIPosterViewController _userInterfaceStyleTraitDidChange:previousTraitCollection:]_block_invoke_2
+ ___86-[PBUIPosterViewController _userInterfaceStyleTraitDidChange:previousTraitCollection:]_block_invoke_3
+ ___86-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperDidChangeForVariant:]_block_invoke
+ ___87-[PBUIPosterWallpaperRemoteViewController _fireObserversWallpaperWillChangeForVariant:]_block_invoke
+ ___91-[PBUIPosterWallpaperRemoteViewController _fireObserverRespondingToSelector:variant:block:]_block_invoke
+ ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke
+ ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_2
+ ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_3
+ ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_4
+ ___92-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdatePreferredProminentColor:]_block_invoke
+ ___94-[PBUIPosterVariantViewController _updateEffectiveMotionEffectsModeForSupportedMode:disabled:]_block_invoke
+ ___96-[PBUIPosterWallpaperRemoteViewController posterComponent:didUpdateDeviceMotionEventsRequested:]_block_invoke
+ ___PBUILogRuntime_block_invoke
+ ___PosterFuturesKitLibraryCore_block_invoke
+ ___PosterKitLibraryCore_block_invoke
+ ___PosterLegibilityKitLibraryCore_block_invoke
+ ___block_descriptor_181_e16_64s72bs_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24ls64l8s72l8
+ ___block_descriptor_32_e18_B16?0"CAFilter"8l
+ ___block_descriptor_32_e30_v16?0"<PBUIPosterUpdating>"8l
+ ___block_descriptor_32_e33_v16?0"<PBUIWallpaperObserver>"8l
+ ___block_descriptor_33_e33_v16?0"<PBUIWallpaperObserver>"8l
+ ___block_descriptor_40_e33_v16?0"<PBUIWallpaperObserver>"8l
+ ___block_descriptor_40_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_40_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24l
+ ___block_descriptor_40_e8_32bs_e33_v16?0"PUIPosterSnapshotBundle"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"<PBUIWallpaperObserver>"8ls32l8
+ ___block_descriptor_41_e8_32s_e30_v16?0"<PBUIPosterUpdating>"8ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_48_e8_32s_e33_v16?0"<PBUIWallpaperObserver>"8ls32l8
+ ___block_descriptor_56_e30_v16?0"<PBUIPosterUpdating>"8l
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e30_v16?0"<PBUIPosterUpdating>"8l
+ ___block_descriptor_64_e33_v16?0"<PBUIWallpaperObserver>"8l
+ ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lw56l8s32l8s40l8r48l8
+ ___block_literal_global.129
+ ___block_literal_global.134
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.225
+ ___block_literal_global.240
+ ___block_literal_global.248
+ ___block_literal_global.251
+ ___block_literal_global.277
+ ___block_literal_global.309
+ ___block_literal_global.496
+ ___block_literal_global.793
+ ___block_literal_global.94
+ ___block_literal_global.98
+ ___getPFDeviceMotionUtilitiesClass_block_invoke
+ ___getPFDeviceMotionUtilitiesClass_block_invoke.cold.1
+ ___getPFTSchedulerClass_block_invoke
+ ___getPFTSchedulerClass_block_invoke.cold.1
+ ___getPLKLegibilityDescriptorClass_block_invoke
+ ___getPLKLegibilityDescriptorClass_block_invoke.cold.1
+ ___getPLKLegibilityEnvironmentBuilderClass_block_invoke
+ ___getPLKLegibilityEnvironmentBuilderClass_block_invoke.cold.1
+ ___getPLKLegibilityEnvironmentClass_block_invoke
+ ___getPLKLegibilityEnvironmentClass_block_invoke.cold.1
+ ___getPLKLegibilityEnvironmentVariantDefaultSymbolLoc_block_invoke
+ ___getPLKLegibilityEnvironmentVariantHomeScreenSymbolLoc_block_invoke
+ ___getPLKLegibilityEnvironmentVariantLockScreenSymbolLoc_block_invoke
+ ___getPRPosterPathModelObjectCacheClass_block_invoke
+ ___getPRPosterPathModelObjectCacheClass_block_invoke.cold.1
+ ___getPRRenderingServiceEndpointDidChangeActionClass_block_invoke
+ ___getPRRenderingServiceEndpointDidChangeActionClass_block_invoke.cold.1
+ ___getPRRenderingServiceSceneComponentClass_block_invoke
+ ___getPRRenderingServiceSceneComponentClass_block_invoke.cold.1
+ ___getPRRenderingServiceServerClass_block_invoke
+ ___getPRRenderingServiceServerClass_block_invoke.cold.1
+ ___getPRRenderingServiceServerKeepAliveAssertionManagerClass_block_invoke
+ ___getPRRenderingServiceServerKeepAliveAssertionManagerClass_block_invoke.cold.1
+ ___getPRUISPosterWorkspaceClass_block_invoke
+ ___getPRUISPosterWorkspaceClass_block_invoke.cold.1
+ ___getPUICARemoteRendererClass_block_invoke
+ ___getPUICARemoteRendererClass_block_invoke.cold.1
+ ___getPUICodableImageClass_block_invoke
+ ___getPUICodableImageClass_block_invoke.cold.1
+ ___getPUIMaterialTreatmentClass_block_invoke
+ ___getPUIMaterialTreatmentClass_block_invoke.cold.1
+ ___getPUIPosterLevelSetClass_block_invoke
+ ___getPUIPosterLevelSetClass_block_invoke.cold.1
+ ___getPUIPosterSnapshotAnalysisDescriptorClass_block_invoke
+ ___getPUIPosterSnapshotAnalysisDescriptorClass_block_invoke.cold.1
+ ___getPUIPosterSnapshotDescriptorClass_block_invoke
+ ___getPUIPosterSnapshotDescriptorClass_block_invoke.cold.1
+ ___getPUIPosterSnapshotDestinationClass_block_invoke
+ ___getPUIPosterSnapshotDestinationClass_block_invoke.cold.1
+ ___getPUIPosterSnapshotOutputDescriptorClass_block_invoke
+ ___getPUIPosterSnapshotOutputDescriptorClass_block_invoke.cold.1
+ ___getPUIPosterSnapshotUISceneDescriptorClass_block_invoke
+ ___getPUIPosterSnapshotUISceneDescriptorClass_block_invoke.cold.1
+ ___getPUITreatImageRequestClass_block_invoke
+ ___getPUITreatImageRequestClass_block_invoke.cold.1
+ ___getPUIWallpaperInactiveTreatmentClass_block_invoke
+ ___getPUIWallpaperInactiveTreatmentClass_block_invoke.cold.1
+ ___getPUIWallpaperLegibilityTreatmentClass_block_invoke
+ ___getPUIWallpaperLegibilityTreatmentClass_block_invoke.cold.1
+ __os_feature_enabled_impl
+ _asin
+ _atan2
+ _atan2f
+ _getPFDeviceMotionUtilitiesClass
+ _getPFDeviceMotionUtilitiesClass.softClass
+ _getPFTSchedulerClass
+ _getPFTSchedulerClass.softClass
+ _getPLKLegibilityDescriptorClass
+ _getPLKLegibilityDescriptorClass.softClass
+ _getPLKLegibilityEnvironmentBuilderClass
+ _getPLKLegibilityEnvironmentBuilderClass.softClass
+ _getPLKLegibilityEnvironmentClass
+ _getPLKLegibilityEnvironmentClass.softClass
+ _getPLKLegibilityEnvironmentVariantDefault
+ _getPLKLegibilityEnvironmentVariantDefault.cold.1
+ _getPLKLegibilityEnvironmentVariantDefaultSymbolLoc
+ _getPLKLegibilityEnvironmentVariantDefaultSymbolLoc.ptr
+ _getPLKLegibilityEnvironmentVariantHomeScreen
+ _getPLKLegibilityEnvironmentVariantHomeScreen.cold.1
+ _getPLKLegibilityEnvironmentVariantHomeScreenSymbolLoc
+ _getPLKLegibilityEnvironmentVariantHomeScreenSymbolLoc.ptr
+ _getPLKLegibilityEnvironmentVariantLockScreen
+ _getPLKLegibilityEnvironmentVariantLockScreen.cold.1
+ _getPLKLegibilityEnvironmentVariantLockScreenSymbolLoc
+ _getPLKLegibilityEnvironmentVariantLockScreenSymbolLoc.ptr
+ _getPRPosterPathModelObjectCacheClass
+ _getPRPosterPathModelObjectCacheClass.softClass
+ _getPRRenderingServiceEndpointDidChangeActionClass
+ _getPRRenderingServiceEndpointDidChangeActionClass.softClass
+ _getPRRenderingServiceSceneComponentClass
+ _getPRRenderingServiceSceneComponentClass.softClass
+ _getPRRenderingServiceServerClass
+ _getPRRenderingServiceServerClass.softClass
+ _getPRRenderingServiceServerKeepAliveAssertionManagerClass
+ _getPRRenderingServiceServerKeepAliveAssertionManagerClass.softClass
+ _getPRUISPosterWorkspaceClass
+ _getPRUISPosterWorkspaceClass.softClass
+ _getPUICARemoteRendererClass
+ _getPUICARemoteRendererClass.softClass
+ _getPUICodableImageClass
+ _getPUICodableImageClass.softClass
+ _getPUIMaterialTreatmentClass
+ _getPUIMaterialTreatmentClass.softClass
+ _getPUIPosterLevelSetClass
+ _getPUIPosterLevelSetClass.softClass
+ _getPUIPosterSnapshotAnalysisDescriptorClass
+ _getPUIPosterSnapshotAnalysisDescriptorClass.softClass
+ _getPUIPosterSnapshotDescriptorClass
+ _getPUIPosterSnapshotDescriptorClass.softClass
+ _getPUIPosterSnapshotDestinationClass
+ _getPUIPosterSnapshotDestinationClass.softClass
+ _getPUIPosterSnapshotOutputDescriptorClass
+ _getPUIPosterSnapshotOutputDescriptorClass.softClass
+ _getPUIPosterSnapshotUISceneDescriptorClass
+ _getPUIPosterSnapshotUISceneDescriptorClass.softClass
+ _getPUITreatImageRequestClass
+ _getPUITreatImageRequestClass.softClass
+ _getPUIWallpaperInactiveTreatmentClass
+ _getPUIWallpaperInactiveTreatmentClass.softClass
+ _getPUIWallpaperLegibilityTreatmentClass
+ _getPUIWallpaperLegibilityTreatmentClass.softClass
+ _kCAFilterColorMatrix
+ _kCAFilterGaussianBlur
+ _kCAFilterInputAmount
+ _kCAFilterInputColorMatrix
+ _kCAFilterInputQuality
+ _kCAFilterInputRadius
+ _kCAFilterInputValues
+ _kCAFilterLuminanceCurveMap
+ _objc_msgSend$_animateUsingSpringWithDuration:delay:options:mass:stiffness:damping:initialVelocity:animations:completion:
+ _objc_msgSend$_checkIfPresentationIsUpdatedAndSnapshot
+ _objc_msgSend$_finalizeActiveVariantTransitionWithReason:
+ _objc_msgSend$_fireObserverRespondingToSelector:variant:block:
+ _objc_msgSend$_fireObserversWallpaperDidChange
+ _objc_msgSend$_fireObserversWallpaperDidChangeForVariant:
+ _objc_msgSend$_fireObserversWallpaperWillChange
+ _objc_msgSend$_fireObserversWallpaperWillChangeForVariant:
+ _objc_msgSend$_initWithPath:
+ _objc_msgSend$_invalidateComponents
+ _objc_msgSend$_isSceneContentReady
+ _objc_msgSend$_legibilityUpdatedWithDictionary:notifyObservers:
+ _objc_msgSend$_motionEffectWithFactor:
+ _objc_msgSend$_observerLock_observersForVariant:
+ _objc_msgSend$_prepareActiveVariantTransition
+ _objc_msgSend$_updateActivePosterSceneMode
+ _objc_msgSend$_updateActiveVariantTransitionProgress:
+ _objc_msgSend$_updateDebugHUD
+ _objc_msgSend$_updateEffectiveMotionEffectsModeForSupportedMode:disabled:
+ _objc_msgSend$_updateInactiveBlurEffectForWallpaperMode:
+ _objc_msgSend$_updatePosterLayers
+ _objc_msgSend$_updatePosterScenesForReasons:updater:completion:
+ _objc_msgSend$_updatedDimStyle
+ _objc_msgSend$activelyRequired
+ _objc_msgSend$activelyRequiredReasons
+ _objc_msgSend$adaptiveTimeHonorsPreferredSalientContentRectangle
+ _objc_msgSend$addAnimations:
+ _objc_msgSend$addFailureBlock:scheduler:
+ _objc_msgSend$addSuccessBlock:scheduler:
+ _objc_msgSend$animateWithSettings:actions:
+ _objc_msgSend$areMotionEffectsEnabled
+ _objc_msgSend$beginActiveVariantTransition
+ _objc_msgSend$blurPhotosWallpaperInAlwaysOn
+ _objc_msgSend$bs_array
+ _objc_msgSend$bs_performAfterSynchronizedCommit:
+ _objc_msgSend$bs_setSafeObject:forKey:
+ _objc_msgSend$buildWithError:
+ _objc_msgSend$colorStatistics
+ _objc_msgSend$compositeLevelSet
+ _objc_msgSend$copyWithShouldDetermineColorStatistics:
+ _objc_msgSend$defaultAnalysisDescriptor
+ _objc_msgSend$descriptionForRotation:
+ _objc_msgSend$deviceMotionEventGenerationDidStop
+ _objc_msgSend$deviceMotionEventGenerationWillStart
+ _objc_msgSend$dimStyle
+ _objc_msgSend$endActiveVariantTransition
+ _objc_msgSend$filters
+ _objc_msgSend$hasRequestedDeviceMotionEvents
+ _objc_msgSend$hitTestViews
+ _objc_msgSend$iconStyleVariant
+ _objc_msgSend$iconTintSource
+ _objc_msgSend$iconUserInterfaceStyleVariant
+ _objc_msgSend$initWithAnimationCurve:
+ _objc_msgSend$initWithDuration:timingParameters:
+ _objc_msgSend$initWithLevelSets:snapshotDefinitionIdentifier:
+ _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:
+ _objc_msgSend$initWithScene:renderingServiceServerKeepAliveAssertionManager:
+ _objc_msgSend$initWithTintColorStyle:suggestedTintColor:tintSource:isHomeScreenDimmed:iconSize:iconStyle:iconStyleVariant:lastUserSelectedVariantForStyleTypeOption:
+ _objc_msgSend$invalidateModelObjectCacheForPath:
+ _objc_msgSend$isDescendantOfView:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$lastUserSelectedVariantForStyleTypeOption
+ _objc_msgSend$legibilityEnvironment
+ _objc_msgSend$legibilityEnvironmentContextForVariant:
+ _objc_msgSend$legibilityEnvironmentForUILegibilitySettings:
+ _objc_msgSend$noteWorkspaceInstanceSetupForScene:poster:userInfo:
+ _objc_msgSend$noteWorkspaceInstanceTeardownForScene:poster:userInfo:
+ _objc_msgSend$noteWorkspaceUpdateForScene:poster:userInfo:
+ _objc_msgSend$pf_shortDesc
+ _objc_msgSend$posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:
+ _objc_msgSend$posterComponent:didUpdateDeviceMotionEventsRequested:
+ _objc_msgSend$posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:
+ _objc_msgSend$posterComponent:didUpdatePreferredSalientContentRectangle:
+ _objc_msgSend$posterComponent:didUpdateSalientContentRectangleUpdatesRequested:
+ _objc_msgSend$posterDidUpdateWantsMotionEvents:
+ _objc_msgSend$posterHasRequestedDeviceMotionEvents
+ _objc_msgSend$posterWantsDefaultParallax
+ _objc_msgSend$pr_adaptiveTimeMode
+ _objc_msgSend$pr_adaptiveTimeModeDidChange
+ _objc_msgSend$pr_areMotionEffectsDisabled
+ _objc_msgSend$pr_deviceMotionEventsRequested
+ _objc_msgSend$pr_deviceMotionEventsRequestedDidChange
+ _objc_msgSend$pr_effectiveMotionEffectsMode
+ _objc_msgSend$pr_preferredDeviceMotionUpdateInterval
+ _objc_msgSend$pr_preferredDeviceMotionUpdateIntervalDidChange
+ _objc_msgSend$pr_requestedRenderingEventTypes
+ _objc_msgSend$pr_setDeviceMotionRotation:
+ _objc_msgSend$pr_setDeviceMotionUpdateInterval:
+ _objc_msgSend$pr_setDevicePitch:
+ _objc_msgSend$pr_setDeviceRoll:
+ _objc_msgSend$pr_setDeviceYaw:
+ _objc_msgSend$pr_setEffectiveMotionEffectsMode:
+ _objc_msgSend$pr_supportedMotionEffectsMode
+ _objc_msgSend$pr_supportedMotionEffectsModeDidChange
+ _objc_msgSend$preferredDeviceMotionUpdateInterval
+ _objc_msgSend$preferredSalientContentRectangle
+ _objc_msgSend$pui_determineProminentColorWithCompletion:
+ _objc_msgSend$pui_didFinishInitialization
+ _objc_msgSend$pui_executeSnapshotForDescriptor:
+ _objc_msgSend$pui_preferredSalientContentRectangle
+ _objc_msgSend$pui_preferredSalientContentRectangleDidChange
+ _objc_msgSend$pui_salientContentRectangleUpdatesRequested
+ _objc_msgSend$pui_salientContentRectangleUpdatesRequestedDidChange
+ _objc_msgSend$pui_setSalientContentRectangle:
+ _objc_msgSend$pui_setUserInterfaceStyle:
+ _objc_msgSend$reasons
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$removeAllMotionEffects
+ _objc_msgSend$renderingServiceServer
+ _objc_msgSend$salientContentRectangleUpdatesRequested
+ _objc_msgSend$schedulerWithDispatchQueue:
+ _objc_msgSend$setActivelyRequiredReasons:
+ _objc_msgSend$setContextID:
+ _objc_msgSend$setContextID:scene:
+ _objc_msgSend$setDeviceMotionEventGenerationActive:
+ _objc_msgSend$setDeviceMotionUpdateInterval:
+ _objc_msgSend$setDevicePitch:
+ _objc_msgSend$setDevicePitch:roll:yaw:
+ _objc_msgSend$setDeviceRoll:
+ _objc_msgSend$setDeviceYaw:
+ _objc_msgSend$setDim:animated:
+ _objc_msgSend$setLog:
+ _objc_msgSend$setMotionEffectsEnabled:
+ _objc_msgSend$setMotionEffectsWithFloating:foreground:background:
+ _objc_msgSend$setRotation:
+ _objc_msgSend$setSalientContentRectangle:
+ _objc_msgSend$setScene:
+ _objc_msgSend$setUseDimStyle:
+ _objc_msgSend$setValue:forKeyPath:
+ _objc_msgSend$setView:
+ _objc_msgSend$sharedInstanceForStyle:
+ _objc_msgSend$showHUDIfEnabled
+ _objc_msgSend$showsSnapshot
+ _objc_msgSend$snapshotForLevelSet:
+ _objc_msgSend$snapshotLevelSets
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$startAnimation
+ _objc_msgSend$tintSource
+ _objc_msgSend$updateActiveVariantTransitionProgress:
+ _objc_msgSend$updateMotionWithRotation:
+ _objc_msgSend$updatePresentation:
+ _objc_msgSend$updateSettings:
+ _objc_msgSend$updateWithLegibilitySettings:variants:
+ _objc_msgSend$updateWithLockSceneActivityMode:homeSceneActivityMode:activeVariant:wallpaperStyle:homeAndLockAreSame:isActivelyRequired:activelyRequiredReasons:assertionReasons:
+ _objc_msgSend$userSelectedVariantsForStyleTypes
+ _objc_msgSend$valueWithCAColorMatrix:
+ _objc_msgSend$variants
+ _objc_msgSend$wallpaperDidUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:
+ _objc_msgSend$wallpaperDidUpdatePreferredDeviceMotionUpdateInterval:
+ _objc_msgSend$wallpaperDidUpdatePreferredSalientContentRectangle:
+ _objc_msgSend$wallpaperLegibilityEnvironmentDidChange:
+ _objc_msgSend$wantsDefaultParallaxTreatment
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
- +[PBUICARemoteRenderer remoteRendererIfPossible]
- +[PBUICARemoteRenderer secureCodableRequestClasses]
- +[PBUICARemoteRenderer secureCodableRequestClasses].cold.1
- +[PBUICARemoteRenderer shouldUseXPCServiceForRendering]
- +[PBUICodableImage bs_encodeRepresentation:value:withCoder:]
- +[PBUICodableImage createCGImageFromCPBitmapData:error:]
- +[PBUICodableImage createCGImageFromData:error:]
- +[PBUICodableImage createCGImageFromData:error:].cold.1
- +[PBUICodableImage createCGImageFromData:error:].cold.2
- +[PBUICodableImage createCGImageFromURL:error:]
- +[PBUICodableImage createCGImageFromURL:error:].cold.1
- +[PBUICodableImage createCGImageFromURL:error:].cold.2
- +[PBUICodableImage dataRepresentationForImage:error:]
- +[PBUICodableImage encodeRepresentation:value:withCoder:]
- +[PBUICodableImage makeWithOther:]
- +[PBUICodableImage supportsBSXPCSecureCoding]
- +[PBUICodableImage supportsSecureCoding]
- +[PBUIHomeVariantStyleState stateWithTintColorStyle:suggestedTintColor:isHomeScreenDimmed:iconSize:iconStyle:]
- +[PBUIImageContainerLayer layer]
- +[PBUIImageTreatmentOptions identity]
- +[PBUIMaterialTreatment supportsSecureCoding]
- +[PBUIRemoteRendererXPCConnection defaultConnection]
- +[PBUIRemoteRendererXPCConnection defaultConnection].cold.1
- +[PBUITreatImageRequest secureCodableTreatmentClasses]
- +[PBUITreatImageRequest secureCodableTreatmentClasses].cold.1
- +[PBUITreatImageRequest supportsSecureCoding]
- +[PBUIWallpaperInactiveTreatment supportsSecureCoding]
- +[PBUIWallpaperLegibilityTreatment supportsSecureCoding]
- -[FBSMutableSceneSettings(LegacyPoster) pb_applyLegacySettings]
- -[PBUICALocalRenderer .cxx_destruct]
- -[PBUICALocalRenderer CIContext]
- -[PBUICALocalRenderer archiveRenderingOfRequest:toURL:error:]
- -[PBUICALocalRenderer colorSpace]
- -[PBUICALocalRenderer commandQueue]
- -[PBUICALocalRenderer configureWithTransaction:]
- -[PBUICALocalRenderer dealloc]
- -[PBUICALocalRenderer device]
- -[PBUICALocalRenderer identifier]
- -[PBUICALocalRenderer initWithColorSpace:]
- -[PBUICALocalRenderer initWithDevice:colorSpace:]
- -[PBUICALocalRenderer initWithDevice:commmandQueue:colorSpace:]
- -[PBUICALocalRenderer init]
- -[PBUICALocalRenderer logger]
- -[PBUICALocalRenderer newCommandBufferWithCompletion:]
- -[PBUICALocalRenderer newSurfaceWithSize:colorSpace:outOptions:]
- -[PBUICALocalRenderer newTextureWithSize:colorSpace:]
- -[PBUICALocalRenderer nextFrameHandlerWithCompletion:]
- -[PBUICALocalRenderer pixelFormatForBSIOSurfaceOptions:]
- -[PBUICALocalRenderer renderCIImage:toSurface:completionHandler:]
- -[PBUICALocalRenderer renderFrameToTexture:configureWithTransaction:completionHandler:]
- -[PBUICALocalRenderer renderRequest:completionHandler:]
- -[PBUICALocalRenderer renderRequest:error:]
- -[PBUICALocalRenderer renderState:completionHandler:]
- -[PBUICALocalRenderer renderState:error:]
- -[PBUICALocalRenderer rendererForDestination:]
- -[PBUICALocalRenderer resetState]
- -[PBUICALocalRenderer setIdentifier:]
- -[PBUICALocalRenderer setLogger:]
- -[PBUICALocalRenderer setRenderState:]
- -[PBUICALocalRenderer updateStateWithTransaction:]
- -[PBUICALocalRenderer usesCoreImageForState:]
- -[PBUICARemoteRenderer .cxx_destruct]
- -[PBUICARemoteRenderer colorSpace]
- -[PBUICARemoteRenderer dealloc]
- -[PBUICARemoteRenderer initWithUnderlyingConnection:]
- -[PBUICARemoteRenderer init]
- -[PBUICARemoteRenderer renderRequest:completionHandler:]
- -[PBUICARemoteRenderer renderRequest:error:]
- -[PBUICARemoteRenderer supportsRequest:orError:]
- -[PBUICARemoteRenderer underlyingConnection]
- -[PBUICodableImage .cxx_destruct]
- -[PBUICodableImage CGImage]
- -[PBUICodableImage buildCGImageWithError:]
- -[PBUICodableImage copyWithZone:]
- -[PBUICodableImage dealloc]
- -[PBUICodableImage encodeWithBSXPCCoder:]
- -[PBUICodableImage encodeWithCoder:]
- -[PBUICodableImage initFromSourceData:scale:error:]
- -[PBUICodableImage initFromURL:scale:error:]
- -[PBUICodableImage initWithBSXPCCoder:]
- -[PBUICodableImage initWithBSXPCCoder:].cold.1
- -[PBUICodableImage initWithCGImage:scale:error:]
- -[PBUICodableImage initWithCoder:]
- -[PBUICodableImage initWithIOSurface:scale:error:]
- -[PBUICodableImage initWithUIImage:error:]
- -[PBUICodableImage isEqualRepresentation:]
- -[PBUICodableImage refersToIdenticalImageFrom:]
- -[PBUICodableImage scale]
- -[PBUICodableImage setImage:]
- -[PBUICodableImage surfaceCreatingIfNecessary:]
- -[PBUICodableImage wrappedIOSurface]
- -[PBUIHomeVariantStyleState initWithTintColorStyle:suggestedTintColor:isHomeScreenDimmed:iconSize:iconStyle:]
- -[PBUIImageContainerLayer .cxx_destruct]
- -[PBUIImageContainerLayer animationForKey:]
- -[PBUIImageContainerLayer encodeWithCoder:]
- -[PBUIImageContainerLayer imageLayer]
- -[PBUIImageContainerLayer initWithCoder:]
- -[PBUIImageContainerLayer initWithLayer:]
- -[PBUIImageContainerLayer init]
- -[PBUIImageContainerLayer layoutSublayers]
- -[PBUIImageContainerLayer setImageLayer:]
- -[PBUIImageTreatmentOptions copyWithZone:]
- -[PBUIImageTreatmentOptions initWithFixedScale:]
- -[PBUIImageTreatmentOptions initWithOriginalScale:reducedScale:]
- -[PBUIImageTreatmentOptions originalScale]
- -[PBUIImageTreatmentOptions reducedScale]
- -[PBUIImageTreatmentOptions scaleReductionFactor]
- -[PBUIMaterialTreatment .cxx_destruct]
- -[PBUIMaterialTreatment backdropScaleAdjustment]
- -[PBUIMaterialTreatment canInterpolateToLowerScales]
- -[PBUIMaterialTreatment commitToRenderingTree:options:error:]
- -[PBUIMaterialTreatment copyWithZone:]
- -[PBUIMaterialTreatment descriptionBuilderWithMultilinePrefix:]
- -[PBUIMaterialTreatment descriptionWithMultilinePrefix:]
- -[PBUIMaterialTreatment description]
- -[PBUIMaterialTreatment encodeWithCoder:]
- -[PBUIMaterialTreatment initWithCoder:]
- -[PBUIMaterialTreatment initWithRecipeName:fromBundle:]
- -[PBUIMaterialTreatment layoutSublayersOfLayer:]
- -[PBUIMaterialTreatment recipeBundle]
- -[PBUIMaterialTreatment recipeName]
- -[PBUIMaterialTreatment resolvedBackdropScale]
- -[PBUIMaterialTreatment setBackdropScaleAdjustment:]
- -[PBUIMaterialTreatment setRecipeBundle:]
- -[PBUIMaterialTreatment setRecipeName:]
- -[PBUIMaterialTreatment setWeighting:]
- -[PBUIMaterialTreatment succinctDescriptionBuilder]
- -[PBUIMaterialTreatment succinctDescription]
- -[PBUIMaterialTreatment usesStaticBackdropScaleFactor]
- -[PBUIMaterialTreatment weighting]
- -[PBUIPosterHomeViewController updatePresentation]
- -[PBUIPosterHomeViewController updatePresentation].cold.1
- -[PBUIPosterLockViewController _updateFloatingLayer]
- -[PBUIPosterLockViewController updatePresentation]
- -[PBUIPosterVariantViewController _updateParallax]
- -[PBUIPosterVariantViewController _updatePresentation]
- -[PBUIPosterVariantViewController updatePresentation]
- -[PBUIPosterViewController traitCollectionDidChange:]
- -[PBUIPosterWallpaperRemoteViewController _observers]
- -[PBUIPosterWallpaperRemoteViewController addObserver:]
- -[PBUIPosterWallpaperRemoteViewController addObserver:forVariant:].cold.1
- -[PBUIPosterWallpaperRemoteViewController removeObserver:]
- -[PBUIPosterWallpaperRemoteViewController removeObserver:forVariant:].cold.1
- -[PBUIRemoteRendererXPCConnection .cxx_destruct]
- -[PBUIRemoteRendererXPCConnection connectionActivateIfNeededWithError:]
- -[PBUIRemoteRendererXPCConnection dealloc]
- -[PBUIRemoteRendererXPCConnection initToEndpoint:]
- -[PBUIRemoteRendererXPCConnection initToEndpoint:].cold.1
- -[PBUIRemoteRendererXPCConnection initToServiceName:]
- -[PBUIRemoteRendererXPCConnection initToServiceName:].cold.1
- -[PBUIRemoteRendererXPCConnection remoteObjectProxyWithErrorHandler:]
- -[PBUIRemoteRendererXPCConnection synchronousRemoteObjectProxyWithErrorHandler:]
- -[PBUITreatImageRequest .cxx_destruct]
- -[PBUITreatImageRequest CIImage]
- -[PBUITreatImageRequest configureState:error:]
- -[PBUITreatImageRequest copyWithZone:]
- -[PBUITreatImageRequest dealloc]
- -[PBUITreatImageRequest descriptionBuilderWithMultilinePrefix:]
- -[PBUITreatImageRequest descriptionWithMultilinePrefix:]
- -[PBUITreatImageRequest description]
- -[PBUITreatImageRequest downscaleFactor]
- -[PBUITreatImageRequest encodeWithCoder:]
- -[PBUITreatImageRequest identifier]
- -[PBUITreatImageRequest imagePixelSize]
- -[PBUITreatImageRequest image]
- -[PBUITreatImageRequest initWithCoder:]
- -[PBUITreatImageRequest initWithImage:downscaleFactor:treatment:]
- -[PBUITreatImageRequest initWithImage:scale:downscaleFactor:treatment:]
- -[PBUITreatImageRequest layoutSublayersOfLayer:]
- -[PBUITreatImageRequest requestedOutputSizeInPixels]
- -[PBUITreatImageRequest requestedOutputSizeInPointsAtScale:]
- -[PBUITreatImageRequest scale]
- -[PBUITreatImageRequest setDownscaleFactor:]
- -[PBUITreatImageRequest setIdentifier:]
- -[PBUITreatImageRequest setImage:]
- -[PBUITreatImageRequest setScale:]
- -[PBUITreatImageRequest setTreatment:]
- -[PBUITreatImageRequest succinctDescriptionBuilder]
- -[PBUITreatImageRequest succinctDescription]
- -[PBUITreatImageRequest treatmentOptions]
- -[PBUITreatImageRequest treatment]
- -[PBUITreatImageRequest usesCoreImageForTreatment:]
- -[PBUIViewportLayer .cxx_destruct]
- -[PBUIViewportLayer animationForKey:]
- -[PBUIViewportLayer contentLayer]
- -[PBUIViewportLayer initWithCoder:]
- -[PBUIViewportLayer initWithLayer:]
- -[PBUIViewportLayer initWithScale:]
- -[PBUIViewportLayer layoutSublayers]
- -[PBUIViewportLayer scale]
- -[PBUIViewportLayer setScale:]
- -[PBUIWallpaperEffectViewBase wallpaperDidChangeForVariant:]
- -[PBUIWallpaperEffectViewBase wallpaperLegibilitySettingsDidChange:forVariant:]
- -[PBUIWallpaperInactiveTreatment applyToImage:options:error:]
- -[PBUIWallpaperInactiveTreatment commitToRenderingTree:options:error:]
- -[PBUIWallpaperInactiveTreatment copyWithZone:]
- -[PBUIWallpaperInactiveTreatment encodeWithCoder:]
- -[PBUIWallpaperInactiveTreatment initWithCoder:]
- -[PBUIWallpaperLegibilityTreatment .cxx_destruct]
- -[PBUIWallpaperLegibilityTreatment averageColor]
- -[PBUIWallpaperLegibilityTreatment colorByDimmingColor:]
- -[PBUIWallpaperLegibilityTreatment commitToRenderingTree:options:error:]
- -[PBUIWallpaperLegibilityTreatment copyWithZone:]
- -[PBUIWallpaperLegibilityTreatment encodeWithCoder:]
- -[PBUIWallpaperLegibilityTreatment initWithCoder:]
- -[PBUIWallpaperLegibilityTreatment layoutSublayersOfLayer:]
- -[PBUIWallpaperLegibilityTreatment luminanceTreatmentFilters]
- -[PBUIWallpaperLegibilityTreatment luminanceTreatmentFilters].cold.1
- -[PBUIWallpaperLegibilityTreatment luminanceTreatmentFilters].cold.2
- -[PBUIWallpaperLegibilityTreatment luminanceTreatmentFilters].cold.3
- -[PBUIWallpaperLegibilityTreatment makeDimmingLayer]
- -[PBUIWallpaperLegibilityTreatment makeGradientLayer]
- -[PBUIWallpaperLegibilityTreatment makeLuminanceBackdropLayer]
- -[PBUIWallpaperLegibilityTreatment needsDimmingTreatment]
- -[PBUIWallpaperLegibilityTreatment needsLuminanceTreatment]
- -[PBUIWallpaperLegibilityTreatment setAverageColor:]
- -[PBUIWallpaperLegibilityTreatment setNeedsDimmingTreatment:]
- -[PBUIWallpaperLegibilityTreatment setNeedsLuminanceTreatment:]
- -[RBSProcessHandle(PaperBoard) pb_shortDesc]
- GCC_except_table110
- GCC_except_table147
- GCC_except_table155
- GCC_except_table158
- GCC_except_table174
- GCC_except_table18
- GCC_except_table182
- GCC_except_table27
- GCC_except_table44
- GCC_except_table50
- GCC_except_table52
- GCC_except_table58
- GCC_except_table64
- GCC_except_table70
- GCC_except_table71
- GCC_except_table73
- GCC_except_table76
- GCC_except_table79
- GCC_except_table8
- GCC_except_table85
- GCC_except_table97
- _BSRectWithSize
- _BSSizeGreaterThanOrEqualToSize
- _CAMLEncodeLayerTreeToPathWithOptions
- _CATransform3DScale
- _CFAbsoluteTimeGetCurrent
- _CFRetain
- _CGColorCreate
- _CGColorCreateSRGB
- _CGColorRelease
- _CGColorSpaceCopyPropertyList
- _CGColorSpaceCreateWithName
- _CGColorSpaceGetName
- _CGColorSpaceIsWideGamutRGB
- _CGImageCopyJPEGData
- _CGImageCopySourceData
- _CGImageCreateFromIOSurface
- _CGImageDestinationAddImage
- _CGImageDestinationCreateWithData
- _CGImageDestinationFinalize
- _CGImageGetHash
- _CGImageGetIdentifier
- _CGImageGetImageSource
- _CGImageSourceCreateWithURL
- _CoreMaterialLibraryCore.frameworkLibrary
- _IOSurfaceGetID
- _IOSurfaceSetValue
- _MTLCreateSystemDefaultDevice
- _NSDebugDescriptionErrorKey
- _NSLocalizedDescriptionKey
- _NSLocalizedFailureErrorKey
- _NSLocalizedRecoverySuggestionErrorKey
- _NSURLErrorKey
- _OBJC_CLASS_$_CARenderer
- _OBJC_CLASS_$_CASpringAnimation
- _OBJC_CLASS_$_CIContext
- _OBJC_CLASS_$_CIImage
- _OBJC_CLASS_$_CIRenderDestination
- _OBJC_CLASS_$_IOSurface
- _OBJC_CLASS_$_MTLTextureDescriptor
- _OBJC_CLASS_$_NSMutableData
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_PBUICALocalRenderer
- _OBJC_CLASS_$_PBUICARemoteRenderer
- _OBJC_CLASS_$_PBUICodableImage
- _OBJC_CLASS_$_PBUIImageContainerLayer
- _OBJC_CLASS_$_PBUIImageTreatmentOptions
- _OBJC_CLASS_$_PBUIMaterialTreatment
- _OBJC_CLASS_$_PBUIRemoteRendererXPCConnection
- _OBJC_CLASS_$_PBUITreatImageRequest
- _OBJC_CLASS_$_PBUIViewportLayer
- _OBJC_CLASS_$_PBUIWallpaperInactiveTreatment
- _OBJC_CLASS_$_PBUIWallpaperLegibilityTreatment
- _OBJC_CLASS_$_RBSProcessHandle
- _OBJC_IVAR_$_PBUICALocalRenderer._ciContext
- _OBJC_IVAR_$_PBUICALocalRenderer._colorSpace
- _OBJC_IVAR_$_PBUICALocalRenderer._commandQueue
- _OBJC_IVAR_$_PBUICALocalRenderer._currentRenderState
- _OBJC_IVAR_$_PBUICALocalRenderer._device
- _OBJC_IVAR_$_PBUICALocalRenderer._encodingLock
- _OBJC_IVAR_$_PBUICALocalRenderer._identifier
- _OBJC_IVAR_$_PBUICALocalRenderer._logger
- _OBJC_IVAR_$_PBUICALocalRenderer._viewportLayer
- _OBJC_IVAR_$_PBUICARemoteRenderer._colorSpace
- _OBJC_IVAR_$_PBUICARemoteRenderer._underlyingConnection
- _OBJC_IVAR_$_PBUICodableImage._bitmapSourceData
- _OBJC_IVAR_$_PBUICodableImage._cachedImage
- _OBJC_IVAR_$_PBUICodableImage._representation
- _OBJC_IVAR_$_PBUICodableImage._scale
- _OBJC_IVAR_$_PBUICodableImage._sourceImage
- _OBJC_IVAR_$_PBUICodableImage._surface
- _OBJC_IVAR_$_PBUICodableImage._url
- _OBJC_IVAR_$_PBUIImageContainerLayer._imageLayer
- _OBJC_IVAR_$_PBUIImageTreatmentOptions._originalScale
- _OBJC_IVAR_$_PBUIImageTreatmentOptions._reducedScale
- _OBJC_IVAR_$_PBUIMaterialTreatment._backdropScaleAdjustment
- _OBJC_IVAR_$_PBUIMaterialTreatment._recipeBundle
- _OBJC_IVAR_$_PBUIMaterialTreatment._recipeName
- _OBJC_IVAR_$_PBUIMaterialTreatment._usesStaticBackdropScaleFactor
- _OBJC_IVAR_$_PBUIMaterialTreatment._weighting
- _OBJC_IVAR_$_PBUIPosterWallpaperRemoteViewController._observers
- _OBJC_IVAR_$_PBUIRemoteRendererXPCConnection._connectionLock
- _OBJC_IVAR_$_PBUIRemoteRendererXPCConnection._endpoint
- _OBJC_IVAR_$_PBUIRemoteRendererXPCConnection._lock_connection
- _OBJC_IVAR_$_PBUIRemoteRendererXPCConnection._serviceName
- _OBJC_IVAR_$_PBUITreatImageRequest._codableImage
- _OBJC_IVAR_$_PBUITreatImageRequest._downscaleFactor
- _OBJC_IVAR_$_PBUITreatImageRequest._identifier
- _OBJC_IVAR_$_PBUITreatImageRequest._image
- _OBJC_IVAR_$_PBUITreatImageRequest._scale
- _OBJC_IVAR_$_PBUITreatImageRequest._treatment
- _OBJC_IVAR_$_PBUIViewportLayer._contentLayer
- _OBJC_IVAR_$_PBUIViewportLayer._scale
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._averageColor
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._dimmedColorLayer
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._dimmingLayer
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._gradientLayer
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._luminanceBackdropLayer
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._needsDimmingTreatment
- _OBJC_IVAR_$_PBUIWallpaperLegibilityTreatment._needsLuminanceTreatment
- _OBJC_METACLASS_$_PBUICALocalRenderer
- _OBJC_METACLASS_$_PBUICARemoteRenderer
- _OBJC_METACLASS_$_PBUICodableImage
- _OBJC_METACLASS_$_PBUIImageContainerLayer
- _OBJC_METACLASS_$_PBUIImageTreatmentOptions
- _OBJC_METACLASS_$_PBUIMaterialTreatment
- _OBJC_METACLASS_$_PBUIRemoteRendererXPCConnection
- _OBJC_METACLASS_$_PBUITreatImageRequest
- _OBJC_METACLASS_$_PBUIViewportLayer
- _OBJC_METACLASS_$_PBUIWallpaperInactiveTreatment
- _OBJC_METACLASS_$_PBUIWallpaperLegibilityTreatment
- _PBUIRendererErrorDomain
- _PBUIRendererServiceErrorDomain
- _PBUIWallpaperTreatmentBundle
- _PBUIWallpaperTreatmentBundle.__onceToken
- _PBUIWallpaperTreatmentBundle.__paperBoardUIBundle
- _PBUIWallpaperTreatmentBundle.cold.1
- _PhotoImagingLibraryCore.frameworkLibrary
- _UTTypeHEIC
- __OBJC_$_CATEGORY_INSTANCE_METHODS_RBSProcessHandle_$_PaperBoard
- __OBJC_$_CATEGORY_RBSProcessHandle_$_PaperBoard
- __OBJC_$_CLASS_METHODS_PBUICARemoteRenderer
- __OBJC_$_CLASS_METHODS_PBUICodableImage
- __OBJC_$_CLASS_METHODS_PBUIImageContainerLayer
- __OBJC_$_CLASS_METHODS_PBUIMaterialTreatment
- __OBJC_$_CLASS_METHODS_PBUIRemoteRendererXPCConnection
- __OBJC_$_CLASS_METHODS_PBUITreatImageRequest
- __OBJC_$_CLASS_METHODS_PBUIWallpaperInactiveTreatment
- __OBJC_$_CLASS_METHODS_PBUIWallpaperLegibilityTreatment
- __OBJC_$_CLASS_PROP_LIST_PBUICARemoteRenderer
- __OBJC_$_CLASS_PROP_LIST_PBUICodableImage
- __OBJC_$_CLASS_PROP_LIST_PBUIMaterialTreatment
- __OBJC_$_CLASS_PROP_LIST_PBUIRemoteRendererXPCConnection
- __OBJC_$_CLASS_PROP_LIST_PBUITreatImageRequest
- __OBJC_$_CLASS_PROP_LIST_PBUIWallpaperInactiveTreatment
- __OBJC_$_CLASS_PROP_LIST_PBUIWallpaperLegibilityTreatment
- __OBJC_$_INSTANCE_METHODS_FBSMutableSceneSettings(PaperBoard|LegacyPoster)
- __OBJC_$_INSTANCE_METHODS_PBUICALocalRenderer
- __OBJC_$_INSTANCE_METHODS_PBUICARemoteRenderer
- __OBJC_$_INSTANCE_METHODS_PBUICodableImage
- __OBJC_$_INSTANCE_METHODS_PBUIImageContainerLayer
- __OBJC_$_INSTANCE_METHODS_PBUIImageTreatmentOptions
- __OBJC_$_INSTANCE_METHODS_PBUIMaterialTreatment
- __OBJC_$_INSTANCE_METHODS_PBUIRemoteRendererXPCConnection
- __OBJC_$_INSTANCE_METHODS_PBUITreatImageRequest
- __OBJC_$_INSTANCE_METHODS_PBUIViewportLayer
- __OBJC_$_INSTANCE_METHODS_PBUIWallpaperInactiveTreatment
- __OBJC_$_INSTANCE_METHODS_PBUIWallpaperLegibilityTreatment
- __OBJC_$_INSTANCE_VARIABLES_PBUICALocalRenderer
- __OBJC_$_INSTANCE_VARIABLES_PBUICARemoteRenderer
- __OBJC_$_INSTANCE_VARIABLES_PBUICodableImage
- __OBJC_$_INSTANCE_VARIABLES_PBUIImageContainerLayer
- __OBJC_$_INSTANCE_VARIABLES_PBUIImageTreatmentOptions
- __OBJC_$_INSTANCE_VARIABLES_PBUIMaterialTreatment
- __OBJC_$_INSTANCE_VARIABLES_PBUIRemoteRendererXPCConnection
- __OBJC_$_INSTANCE_VARIABLES_PBUITreatImageRequest
- __OBJC_$_INSTANCE_VARIABLES_PBUIViewportLayer
- __OBJC_$_INSTANCE_VARIABLES_PBUIWallpaperLegibilityTreatment
- __OBJC_$_PROP_LIST_PBUICALocalRenderer
- __OBJC_$_PROP_LIST_PBUICARemoteRenderer
- __OBJC_$_PROP_LIST_PBUICodableImage
- __OBJC_$_PROP_LIST_PBUIImageContainerLayer
- __OBJC_$_PROP_LIST_PBUIImageTreatment
- __OBJC_$_PROP_LIST_PBUIImageTreatmentOptions
- __OBJC_$_PROP_LIST_PBUIMaterialTreatment
- __OBJC_$_PROP_LIST_PBUIRemoteRendererXPCConnection
- __OBJC_$_PROP_LIST_PBUIRenderer
- __OBJC_$_PROP_LIST_PBUITreatImageRequest
- __OBJC_$_PROP_LIST_PBUIViewportLayer
- __OBJC_$_PROP_LIST_PBUIWallpaperInactiveTreatment
- __OBJC_$_PROP_LIST_PBUIWallpaperLegibilityTreatment
- __OBJC_$_PROTOCOL_CLASS_METHODS_BSXPCSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CABackdropLayerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CALayerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PBUIImageTreatment
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIImageTreatment
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIRemoteRendererConnection
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIRenderRequest
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIRenderServiceInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PBUIRenderer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISAnalysisServiceInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISSnapshotServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCSecureCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CABackdropLayerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CALayerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIImageTreatment
- __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIRemoteRendererConnection
- __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIRenderRequest
- __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIRenderServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_PBUIRenderer
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISAnalysisServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISSnapshotServiceInterface
- __OBJC_$_PROTOCOL_REFS_BSXPCSecureCoding
- __OBJC_$_PROTOCOL_REFS_CABackdropLayerDelegate
- __OBJC_$_PROTOCOL_REFS_CALayerDelegate
- __OBJC_$_PROTOCOL_REFS_PBUICARemoteRendererServiceInterfaces
- __OBJC_$_PROTOCOL_REFS_PBUIImageTreatment
- __OBJC_$_PROTOCOL_REFS_PBUIRemoteRendererConnection
- __OBJC_$_PROTOCOL_REFS_PBUIRenderRequest
- __OBJC_$_PROTOCOL_REFS_PBUIRenderServiceInterface
- __OBJC_$_PROTOCOL_REFS_PBUIRenderer
- __OBJC_CLASS_PROTOCOLS_$_PBUICALocalRenderer
- __OBJC_CLASS_PROTOCOLS_$_PBUICARemoteRenderer
- __OBJC_CLASS_PROTOCOLS_$_PBUICodableImage
- __OBJC_CLASS_PROTOCOLS_$_PBUIImageTreatmentOptions
- __OBJC_CLASS_PROTOCOLS_$_PBUIMaterialTreatment
- __OBJC_CLASS_PROTOCOLS_$_PBUIPosterFloatingView
- __OBJC_CLASS_PROTOCOLS_$_PBUIRemoteRendererXPCConnection
- __OBJC_CLASS_PROTOCOLS_$_PBUITreatImageRequest
- __OBJC_CLASS_PROTOCOLS_$_PBUIWallpaperInactiveTreatment
- __OBJC_CLASS_PROTOCOLS_$_PBUIWallpaperLegibilityTreatment
- __OBJC_CLASS_RO_$_PBUICALocalRenderer
- __OBJC_CLASS_RO_$_PBUICARemoteRenderer
- __OBJC_CLASS_RO_$_PBUICodableImage
- __OBJC_CLASS_RO_$_PBUIImageContainerLayer
- __OBJC_CLASS_RO_$_PBUIImageTreatmentOptions
- __OBJC_CLASS_RO_$_PBUIMaterialTreatment
- __OBJC_CLASS_RO_$_PBUIRemoteRendererXPCConnection
- __OBJC_CLASS_RO_$_PBUITreatImageRequest
- __OBJC_CLASS_RO_$_PBUIViewportLayer
- __OBJC_CLASS_RO_$_PBUIWallpaperInactiveTreatment
- __OBJC_CLASS_RO_$_PBUIWallpaperLegibilityTreatment
- __OBJC_LABEL_PROTOCOL_$_BSXPCSecureCoding
- __OBJC_LABEL_PROTOCOL_$_CABackdropLayerDelegate
- __OBJC_LABEL_PROTOCOL_$_CALayerDelegate
- __OBJC_LABEL_PROTOCOL_$_PBUICARemoteRendererServiceInterfaces
- __OBJC_LABEL_PROTOCOL_$_PBUIImageTreatment
- __OBJC_LABEL_PROTOCOL_$_PBUIRemoteRendererConnection
- __OBJC_LABEL_PROTOCOL_$_PBUIRenderRequest
- __OBJC_LABEL_PROTOCOL_$_PBUIRenderServiceInterface
- __OBJC_LABEL_PROTOCOL_$_PBUIRenderer
- __OBJC_LABEL_PROTOCOL_$_PRUISAnalysisServiceInterface
- __OBJC_LABEL_PROTOCOL_$_PRUISSnapshotServiceInterface
- __OBJC_METACLASS_RO_$_PBUICALocalRenderer
- __OBJC_METACLASS_RO_$_PBUICARemoteRenderer
- __OBJC_METACLASS_RO_$_PBUICodableImage
- __OBJC_METACLASS_RO_$_PBUIImageContainerLayer
- __OBJC_METACLASS_RO_$_PBUIImageTreatmentOptions
- __OBJC_METACLASS_RO_$_PBUIMaterialTreatment
- __OBJC_METACLASS_RO_$_PBUIRemoteRendererXPCConnection
- __OBJC_METACLASS_RO_$_PBUITreatImageRequest
- __OBJC_METACLASS_RO_$_PBUIViewportLayer
- __OBJC_METACLASS_RO_$_PBUIWallpaperInactiveTreatment
- __OBJC_METACLASS_RO_$_PBUIWallpaperLegibilityTreatment
- __OBJC_PROTOCOL_$_BSXPCSecureCoding
- __OBJC_PROTOCOL_$_CABackdropLayerDelegate
- __OBJC_PROTOCOL_$_CALayerDelegate
- __OBJC_PROTOCOL_$_PBUICARemoteRendererServiceInterfaces
- __OBJC_PROTOCOL_$_PBUIImageTreatment
- __OBJC_PROTOCOL_$_PBUIRemoteRendererConnection
- __OBJC_PROTOCOL_$_PBUIRenderRequest
- __OBJC_PROTOCOL_$_PBUIRenderServiceInterface
- __OBJC_PROTOCOL_$_PBUIRenderer
- __OBJC_PROTOCOL_$_PRUISAnalysisServiceInterface
- __OBJC_PROTOCOL_$_PRUISSnapshotServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_PBUICARemoteRendererServiceInterfaces
- __UIImageGetCGImageRepresentation
- ___39-[PBUIMaterialTreatment initWithCoder:]_block_invoke
- ___41-[PBUICALocalRenderer renderState:error:]_block_invoke
- ___43-[PBUIPosterViewController updateHomeScene]_block_invoke_4
- ___44-[PBUICARemoteRenderer renderRequest:error:]_block_invoke
- ___44-[PBUICARemoteRenderer renderRequest:error:]_block_invoke_2
- ___48+[PBUICARemoteRenderer remoteRendererIfPossible]_block_invoke
- ___48-[PBUIPosterViewController updateConfiguration:]_block_invoke.27
- ___50-[PBUIPosterHomeViewController updatePresentation]_block_invoke
- ___50-[PBUIPosterVariantViewController _updateParallax]_block_invoke
- ___51+[PBUICARemoteRenderer secureCodableRequestClasses]_block_invoke
- ___52+[PBUIRemoteRendererXPCConnection defaultConnection]_block_invoke
- ___52-[PBUIPosterLockViewController _updateFloatingLayer]_block_invoke
- ___53-[PBUICALocalRenderer renderState:completionHandler:]_block_invoke
- ___53-[PBUICALocalRenderer renderState:completionHandler:]_block_invoke_2
- ___53-[PBUICALocalRenderer renderState:completionHandler:]_block_invoke_3
- ___53-[PBUIPosterViewController traitCollectionDidChange:]_block_invoke
- ___54+[PBUITreatImageRequest secureCodableTreatmentClasses]_block_invoke
- ___54-[PBUICALocalRenderer newCommandBufferWithCompletion:]_block_invoke
- ___56-[PBUICARemoteRenderer renderRequest:completionHandler:]_block_invoke
- ___56-[PBUICARemoteRenderer renderRequest:completionHandler:]_block_invoke_2
- ___61-[PBUICALocalRenderer archiveRenderingOfRequest:toURL:error:]_block_invoke
- ___61-[PBUIMaterialTreatment commitToRenderingTree:options:error:]_block_invoke
- ___61-[PBUIMaterialTreatment commitToRenderingTree:options:error:]_block_invoke_2
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.213
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.213.cold.1
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.214
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.228
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke.242
- ___63-[PBUIWallpaperRemoteViewController _setupSceneWithCompletion:]_block_invoke_2.229
- ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.64
- ___64-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke.67
- ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke
- ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke.59
- ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke_2
- ___69-[PBUIPosterViewController _updatePosterScenesForReasons:completion:]_block_invoke_3
- ___71-[PBUIRemoteRendererXPCConnection connectionActivateIfNeededWithError:]_block_invoke
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke.82
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_2.83
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3.84
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_4.87
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_5.91
- ___72-[PBUIPosterHomeViewController performSnapshotOnQueue:scene:completion:]_block_invoke_6.101
- ___CoreMaterialLibraryCore_block_invoke
- ___PBUIWallpaperTreatmentBundle_block_invoke
- ___PhotoImagingLibraryCore_block_invoke
- ___block_descriptor_40_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32bs_e28_v16?0"<MTLCommandBuffer>"8ls32l8
- ___block_descriptor_40_e8_32bs_e31_v24?0"IOSurface"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_40_e8_d16?0d8l
- ___block_descriptor_48_e8_32r40r_e31_v24?0"IOSurface"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_48_e8_32s40bs_e55_v28?0B8"PUIPosterSnapshotBundleBuilder"12"NSError"20ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e14_d32?0d8d16d24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_d16?0d8lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_68_e8_32s_e75_v32?0"FBScene"8"FBSMutableSceneSettings"16"FBSSceneTransitionContext"24ls32l8
- ___block_descriptor_80_e8_32s40n17_8_8_t0w24_s24_s32_e5_v8?0l
- ___block_literal_global.118
- ___block_literal_global.120
- ___block_literal_global.122
- ___block_literal_global.127
- ___block_literal_global.149
- ___block_literal_global.218
- ___block_literal_global.233
- ___block_literal_global.241
- ___block_literal_global.244
- ___block_literal_global.270
- ___block_literal_global.303
- ___block_literal_global.479
- ___block_literal_global.749
- ___copy_assignment_8_8_t0w24_s24_s32
- ___copy_helper_block_e8_40n17_8_8_t0w24_s24_s32
- ___destroy_helper_block_e8_40n9_8_s24_s32
- ___destructor_8_s24_s32
- ___getMTMaterialLayerClass_block_invoke
- ___getMTMaterialLayerClass_block_invoke.cold.1
- ___getMTMaterialLayerClass_block_invoke.cold.2
- ___getPIParallaxLegacyPosterStyleClass_block_invoke
- ___getPIParallaxLegacyPosterStyleClass_block_invoke.cold.1
- ___getPIParallaxLegacyPosterStyleClass_block_invoke.cold.2
- ___getPRUISAnalysisServiceClass_block_invoke
- ___getPRUISAnalysisServiceClass_block_invoke.cold.1
- ___getPRUISSnapshotServiceClass_block_invoke
- ___getPRUISSnapshotServiceClass_block_invoke.cold.1
- __xpc_type_mach_send
- _audit_stringCoreMaterial
- _audit_stringPhotoImaging
- _audit_stringPosterBoardUIServices
- _audit_stringPosterUIFoundation
- _defaultConnection.__result
- _defaultConnection.onceToken
- _getMTMaterialLayerClass.softClass
- _getPIParallaxLegacyPosterStyleClass.softClass
- _getPRUISAnalysisServiceClass
- _getPRUISAnalysisServiceClass.softClass
- _getPRUISSnapshotServiceClass
- _getPRUISSnapshotServiceClass.softClass
- _kCACodingImageFormat
- _kCAFillModeForwards
- _kCAFilterDarkenSourceOver
- _kCAFilterLuminanceMap
- _kCAFilterMultiplyBlendMode
- _kCAGravityResize
- _kCARendererColorSpace
- _kCARendererMetalCommandQueue
- _kCGColorSpaceExtendedSRGB
- _kCGColorSpaceGenericGrayGamma2_2
- _kCGColorSpaceSRGB
- _kCIContextCacheIntermediates
- _kCIContextDisableSoftwareFallback
- _kCIContextIntermediateMemoryTarget
- _kCIContextName
- _kCIContextUseMetalRenderer
- _kIOSurfaceColorSpace
- _objc_msgSend$CIContext
- _objc_msgSend$CIImage
- _objc_msgSend$URLForResource:withExtension:
- _objc_msgSend$_observers
- _objc_msgSend$_updateFloatingLayer
- _objc_msgSend$_updatePresentation
- _objc_msgSend$addCompletedHandler:
- _objc_msgSend$animationWithKeyPath:
- _objc_msgSend$anyObject
- _objc_msgSend$applyInactiveStyleToImage:error:
- _objc_msgSend$applyToImage:options:error:
- _objc_msgSend$backdropScaleAdjustment
- _objc_msgSend$beginFrameAtTime:timeStamp:
- _objc_msgSend$blurRadiusTransformer
- _objc_msgSend$bs_IOSurfaceWithWidth:height:options:
- _objc_msgSend$bs_encodeRepresentation:value:withCoder:
- _objc_msgSend$buildCGImageWithError:
- _objc_msgSend$bundleURL
- _objc_msgSend$bundleWithURL:
- _objc_msgSend$canInterpolateToLowerScales
- _objc_msgSend$capturedColorStatistics
- _objc_msgSend$capturedSnapshotForLevelSet:
- _objc_msgSend$capturedSnapshotLevelSets
- _objc_msgSend$colorByDimmingColor:
- _objc_msgSend$commandBuffer
- _objc_msgSend$commitToRenderingTree:options:error:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$configureState:error:
- _objc_msgSend$configureWithTransaction:
- _objc_msgSend$connectionActivateIfNeededWithError:
- _objc_msgSend$contentLayer
- _objc_msgSend$contextWithMTLCommandQueue:options:
- _objc_msgSend$copyWithZone:
- _objc_msgSend$createCGImageFromCPBitmapData:error:
- _objc_msgSend$createCGImageFromData:error:
- _objc_msgSend$createCGImageFromURL:error:
- _objc_msgSend$data
- _objc_msgSend$dataRepresentationForImage:error:
- _objc_msgSend$decodeXPCObjectOfType:forKey:
- _objc_msgSend$defaultConnection
- _objc_msgSend$defaults
- _objc_msgSend$downscaleFactor
- _objc_msgSend$encodeRepresentation:value:withCoder:
- _objc_msgSend$encodeXPCObject:forKey:
- _objc_msgSend$endFrame
- _objc_msgSend$enqueue
- _objc_msgSend$failWithError:
- _objc_msgSend$flush
- _objc_msgSend$grayColor
- _objc_msgSend$height
- _objc_msgSend$imageByApplyingTransform:
- _objc_msgSend$imageLayer
- _objc_msgSend$imagePixelSize
- _objc_msgSend$imageWithCGImage:options:
- _objc_msgSend$initFromSourceData:scale:error:
- _objc_msgSend$initFromURL:scale:error:
- _objc_msgSend$initToServiceName:
- _objc_msgSend$initWithCGImage:scale:error:
- _objc_msgSend$initWithColorSpace:
- _objc_msgSend$initWithDevice:colorSpace:
- _objc_msgSend$initWithDevice:commmandQueue:colorSpace:
- _objc_msgSend$initWithIOSurface:
- _objc_msgSend$initWithIOSurface:scale:error:
- _objc_msgSend$initWithImage:scale:downscaleFactor:treatment:
- _objc_msgSend$initWithListenerEndpoint:
- _objc_msgSend$initWithScale:
- _objc_msgSend$initWithServiceName:
- _objc_msgSend$initWithTintColorStyle:suggestedTintColor:isHomeScreenDimmed:iconSize:iconStyle:
- _objc_msgSend$initWithTypeRecord:destinationOptions:addImageOptions:
- _objc_msgSend$initWithUnderlyingConnection:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$iosurface
- _objc_msgSend$isEqualRepresentation:
- _objc_msgSend$isFrontBoard
- _objc_msgSend$lastObject
- _objc_msgSend$layoutSublayers
- _objc_msgSend$luminanceTreatmentFilters
- _objc_msgSend$makeDimmingLayer
- _objc_msgSend$makeGradientLayer
- _objc_msgSend$makeLuminanceBackdropLayer
- _objc_msgSend$newCommandBufferWithCompletion:
- _objc_msgSend$newCommandQueue
- _objc_msgSend$newSurfaceWithSize:colorSpace:outOptions:
- _objc_msgSend$newTextureWithDescriptor:iosurface:plane:
- _objc_msgSend$newTextureWithSize:colorSpace:
- _objc_msgSend$nextFrameHandlerWithCompletion:
- _objc_msgSend$nextFrameTime
- _objc_msgSend$opacity
- _objc_msgSend$pb_applyLegacySettings
- _objc_msgSend$pb_shortDesc
- _objc_msgSend$pid
- _objc_msgSend$pixelFormatForBSIOSurfaceOptions:
- _objc_msgSend$pr_contentSize
- _objc_msgSend$pr_contentSizeDidChange
- _objc_msgSend$pr_isParallaxEffectivelyEnabled
- _objc_msgSend$pr_setParallaxEnabled:
- _objc_msgSend$presentationLayer
- _objc_msgSend$pruis_determineProminentColorWithCompletion:
- _objc_msgSend$pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$reducedScale
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$removeFromSuperlayer
- _objc_msgSend$render
- _objc_msgSend$renderCIImage:toSurface:completionHandler:
- _objc_msgSend$renderFrameToTexture:configureWithTransaction:completionHandler:
- _objc_msgSend$renderRequest:reply:
- _objc_msgSend$renderState:completionHandler:
- _objc_msgSend$renderState:error:
- _objc_msgSend$rendererForDestination:
- _objc_msgSend$rendererWithMTLTexture:options:
- _objc_msgSend$replaceSublayer:with:
- _objc_msgSend$requestedOutputSizeInPixels
- _objc_msgSend$resetState
- _objc_msgSend$resolveAddImageOptionsForImage:
- _objc_msgSend$resolveDestinationOptionsForImage:
- _objc_msgSend$resolvedBackdropScale
- _objc_msgSend$scaleReductionFactor
- _objc_msgSend$secureCodableRequestClasses
- _objc_msgSend$secureCodableResponseClasses
- _objc_msgSend$secureCodableTreatmentClasses
- _objc_msgSend$setAllowGPUOptimizedContents:
- _objc_msgSend$setBackdropScaleAdjustment:
- _objc_msgSend$setBlurRadiusTransformer:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setContentsGravity:
- _objc_msgSend$setDamping:
- _objc_msgSend$setDestination:
- _objc_msgSend$setFromValue:
- _objc_msgSend$setInitialVelocity:
- _objc_msgSend$setLabel:
- _objc_msgSend$setLayer:
- _objc_msgSend$setMass:
- _objc_msgSend$setPurgeableState:
- _objc_msgSend$setRecipeBundle:
- _objc_msgSend$setRecipeName:
- _objc_msgSend$setRecipeName:fromBundle:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$setRenderState:
- _objc_msgSend$setScale:
- _objc_msgSend$setStiffness:
- _objc_msgSend$setToValue:
- _objc_msgSend$setUsage:
- _objc_msgSend$shouldUseXPCServiceForRendering
- _objc_msgSend$startTaskToRender:toDestination:error:
- _objc_msgSend$sublayers
- _objc_msgSend$supportsRequest:orError:
- _objc_msgSend$supportsSecureCoding
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
- _objc_msgSend$treatment
- _objc_msgSend$treatmentOptions
- _objc_msgSend$typeIdentifier
- _objc_msgSend$underlyingConnection
- _objc_msgSend$updatePresentation
- _objc_msgSend$usesCoreImageForState:
- _objc_msgSend$usesCoreImageForTreatment:
- _objc_msgSend$usesStaticBackdropScaleFactor
- _objc_msgSend$valueForKey:
- _objc_msgSend$waitUntilCompleted
- _objc_msgSend$wrappedIOSurface
- _objc_retainAutoreleasedReturnValue
- _os_unfair_recursive_lock_lock_with_options
- _os_unfair_recursive_lock_unlock
- _remoteRendererIfPossible.__renderer
- _remoteRendererIfPossible.onceToken
- _renderRequest:error:.count
- _secureCodableRequestClasses.onceToken
- _secureCodableRequestClasses.result
- _secureCodableTreatmentClasses.onceToken
- _secureCodableTreatmentClasses.result
CStrings:
+ "#1"
+ "%@-background"
+ "%@-foreground"
+ "(?=\"\"{?=\"vector\"}\"quaternion\"{?=\"vector\"})"
+ "(?={?=}{?=})16@0:8"
+ "-[PBUIPosterViewController _updateDebugHUD]"
+ "-[PBUIPosterWallpaperViewController requireWallpaperWithReason:]_block_invoke"
+ "-[PBUIPosterWallpaperViewController updateConfiguration:withAnimationSettings:]_block_invoke_2"
+ "-[PBUIPosterWallpaperViewController updateConfiguration:withAnimationSettings:]_block_invoke_6"
+ "/AppleInternal/Library/Frameworks/PosterFuturesKit.framework/PosterFuturesKit"
+ "/AppleInternal/Library/Frameworks/PosterKit.framework/PosterKit"
+ "/AppleInternal/Library/Frameworks/PosterLegibilityKit.framework/PosterLegibilityKit"
+ "/System/AppleInternal/Library/Frameworks/PosterFuturesKit.framework/PosterFuturesKit"
+ "/System/AppleInternal/Library/Frameworks/PosterKit.framework/PosterKit"
+ "/System/AppleInternal/Library/Frameworks/PosterLegibilityKit.framework/PosterLegibilityKit"
+ "/System/Library/Frameworks/PosterFuturesKit.framework/PosterFuturesKit"
+ "/System/Library/Frameworks/PosterKit.framework/PosterKit"
+ "/System/Library/Frameworks/PosterLegibilityKit.framework/PosterLegibilityKit"
+ "/System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit"
+ "/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit"
+ "/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit"
+ "@\"<PUIRenderer>\""
+ "@\"BSServiceConnectionEndpoint\""
+ "@\"CAFilter\""
+ "@\"NSArray\"16@0:8"
+ "@\"PBUIHUDWindow\""
+ "@\"PBUIPosterSceneLayerHostView\""
+ "@\"PLKLegibilityEnvironment\""
+ "@\"PLKLegibilityEnvironment\"16@0:8"
+ "@\"PLKLegibilityEnvironmentBuilder\""
+ "@\"PRRenderingServiceSceneComponent\""
+ "@\"PRRenderingServiceServerKeepAliveAssertionManager\""
+ "@\"UIPanGestureRecognizer\""
+ "@\"_PBUIDimmingView\""
+ "@\"_UIParallaxMotionEffect\""
+ "@40@0:8{CGPoint=dd}16@32"
+ "@76@0:8@16@24@32B40@44@52@60@68"
+ "Active Poster assertion noted that poster should be running for reasons: %@"
+ "Active Poster assertions are gone; poster should not be active."
+ "Actively required reasons were updated: %@"
+ "Actively required was updated: %{BOOL}u"
+ "B16@?0@\"CAFilter\"8"
+ "B20@0:8B16"
+ "Booting up poster..."
+ "Class getPFDeviceMotionUtilitiesClass(void)_block_invoke"
+ "Class getPFTSchedulerClass(void)_block_invoke"
+ "Class getPLKLegibilityDescriptorClass(void)_block_invoke"
+ "Class getPLKLegibilityEnvironmentBuilderClass(void)_block_invoke"
+ "Class getPLKLegibilityEnvironmentClass(void)_block_invoke"
+ "Class getPRPosterPathModelObjectCacheClass(void)_block_invoke"
+ "Class getPRRenderingServiceEndpointDidChangeActionClass(void)_block_invoke"
+ "Class getPRRenderingServiceSceneComponentClass(void)_block_invoke"
+ "Class getPRRenderingServiceServerClass(void)_block_invoke"
+ "Class getPRRenderingServiceServerKeepAliveAssertionManagerClass(void)_block_invoke"
+ "Class getPRUISPosterWorkspaceClass(void)_block_invoke"
+ "Class getPUICARemoteRendererClass(void)_block_invoke"
+ "Class getPUICodableImageClass(void)_block_invoke"
+ "Class getPUIMaterialTreatmentClass(void)_block_invoke"
+ "Class getPUIPosterLevelSetClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotAnalysisDescriptorClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotDescriptorClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotDestinationClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotOutputDescriptorClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotUISceneDescriptorClass(void)_block_invoke"
+ "Class getPUITreatImageRequestClass(void)_block_invoke"
+ "Class getPUIWallpaperInactiveTreatmentClass(void)_block_invoke"
+ "Class getPUIWallpaperLegibilityTreatmentClass(void)_block_invoke"
+ "Created new lock poster scene: %@"
+ "DIMMING_COLOR_MATRIX"
+ "DIMMING_LUMINANCE_CURVE_MAP"
+ "DIMMING_SATURATION"
+ "I16@0:8"
+ "Ignoring motion update because the content is not ready for scene: %@"
+ "Jun  2 2025 21:05:57"
+ "PBUIHUDWindow"
+ "PBUIPosterHUDController"
+ "PBUIPosterLockViewController parallax: setMotionEffectsWithFactors called -- motion effects applied."
+ "PBUIPosterLockViewController parallax: setMotionEffectsWithFactors called without parallax enabled -- motion effects not applied."
+ "PBUIPosterSceneLayerHostView"
+ "PFDeviceMotionUtilities"
+ "PFTScheduler"
+ "PLKLegibilityDescriptor"
+ "PLKLegibilityEnvironment"
+ "PLKLegibilityEnvironmentBuilder"
+ "PLKLegibilityEnvironmentVariantDefault"
+ "PLKLegibilityEnvironmentVariantHomeScreen"
+ "PLKLegibilityEnvironmentVariantLockScreen"
+ "PRPosterPathModelObjectCache"
+ "PRRenderingEventTypeTap"
+ "PRRenderingServiceEndpointDidChangeAction"
+ "PRRenderingServiceSceneComponent"
+ "PRRenderingServiceServer"
+ "PRRenderingServiceServerKeepAliveAssertionManager"
+ "PRUISPosterWorkspace"
+ "PUICARemoteRenderer"
+ "PUICodableImage"
+ "PUIMaterialTreatment"
+ "PUIPosterLevelSet"
+ "PUIPosterSnapshotAnalysisDescriptor"
+ "PUIPosterSnapshotDescriptor"
+ "PUIPosterSnapshotDestination"
+ "PUIPosterSnapshotOutputDescriptor"
+ "PUIPosterSnapshotUISceneDescriptor"
+ "PUITreatImageRequest"
+ "PUIWallpaperInactiveTreatment"
+ "PUIWallpaperLegibilityTreatment"
+ "Poster didUpdateDeviceMotionEventsRequested:%{BOOL}u"
+ "Runtime"
+ "RuntimeSnapshot"
+ "SBBlurPhotosWallpaperInAlwaysOn"
+ "SHOW_POSTER_HUD"
+ "SUTU"
+ "T(?={?=}{?=}),N"
+ "T(?={?=}{?=}),N,V_rotation"
+ "T@\"<PUIRenderer>\",&,N,V_renderer"
+ "T@\"BSServiceConnectionEndpoint\",&,N,V_renderingServiceEndpoint"
+ "T@\"BSUIOrientationTransformWrapperView\",&,N,V_containerView"
+ "T@\"FBScene\",&,N,V_scene"
+ "T@\"NSArray\",&,N,V_hitTestViews"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",R,C,N,V_activelyRequiredReasons"
+ "T@\"NSDictionary\",R,C,N,V_lastUserSelectedVariantForStyleTypeOption"
+ "T@\"NSString\",R,C,N,V_iconStyleVariant"
+ "T@\"NSString\",R,C,N,V_tintSource"
+ "T@\"PBUIHUDWindow\",&,N,V_hudWindow"
+ "T@\"PBUIHomeVariantStyleState\",?,R,N"
+ "T@\"PBUIHomeVariantStyleState\",?,R,N,V_currentHomeVariantStyleState"
+ "T@\"PLKLegibilityEnvironment\",?,R,N"
+ "T@\"PLKLegibilityEnvironment\",R,N"
+ "T@\"UILabel\",&,N,V_posterActiveLabel"
+ "T@\"UIPanGestureRecognizer\",&,N,V_panGestureRecognizer"
+ "TB,N,GareMotionEffectsEnabled,V_motionEffectsEnabled"
+ "TB,N,GisDeviceMotionEventGenerationActive,V_deviceMotionEventGenerationActive"
+ "TB,N,GisTransitioningActiveVariant,V_transitioningActiveVariant"
+ "TB,N,V_isHUDVisible"
+ "TB,N,V_useDimmingColorMatrix"
+ "TI,N,V_contextID"
+ "Td,?,N"
+ "Td,?,N,V_deviceMotionUpdateInterval"
+ "Td,?,R,N"
+ "Td,N,V_deviceMotionUpdateInterval"
+ "Td,N,V_devicePitch"
+ "Td,N,V_deviceRoll"
+ "Td,N,V_deviceYaw"
+ "T{CGPoint=dd},N,V_lastPosition"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_salientContentRectangle"
+ "Updating activity mode for scene %@ to %{public}@"
+ "Vertigo"
+ "VertigoParallax"
+ "[%{public}@]\t--> snapshot failure reason '%{public}@'"
+ "[%{public}@]\tSnapshot executing..."
+ "[%{public}@] forcing update; home configuration was updated"
+ "[%{public}@] forcing update; we can now show a snapshot"
+ "[%{public}@] isShowingSnapshot: %{BOOL}u (same)"
+ "[%{public}@] isShowingSnapshot: %{BOOL}u (updated)"
+ "_PBUIDimmingView"
+ "_PBUIWallpaperBlurAnimatingView"
+ "_activePosterSceneDefaultModeAssertion"
+ "_activelyRequiredReasons"
+ "_animateUsingSpringWithDuration:delay:options:mass:stiffness:damping:initialVelocity:animations:completion:"
+ "_backgroundEffect"
+ "_checkIfPresentationIsUpdatedAndSnapshot"
+ "_contextID"
+ "_currentDimStyle"
+ "_currentLegibilityEnvironment"
+ "_deviceMotionEventGenerationActive"
+ "_deviceMotionUpdateInterval"
+ "_devicePitch"
+ "_deviceRoll"
+ "_deviceYaw"
+ "_dimmingColorMatrixFilter"
+ "_finalizeActiveVariantTransitionWithReason:"
+ "_fireObserverRespondingToSelector:variant:block:"
+ "_fireObserversWallpaperDidChange"
+ "_fireObserversWallpaperDidChangeForVariant:"
+ "_fireObserversWallpaperWillChange"
+ "_fireObserversWallpaperWillChangeForVariant:"
+ "_floatingEffect"
+ "_foregroundEffect"
+ "_hitTestViews"
+ "_homeScreenDimStyle"
+ "_hudWindow"
+ "_iconStyleVariant"
+ "_initWithPath:"
+ "_invalidateComponents"
+ "_isHUDVisible"
+ "_isSceneContentReady"
+ "_lastPosition"
+ "_lastUserSelectedVariantForStyleTypeOption"
+ "_legibilityEnvironmentBuilder"
+ "_legibilityUpdatedWithDictionary:notifyObservers:"
+ "_luminanceCurveMapFilter"
+ "_motionEffectWithFactor:"
+ "_observerLock_homeScreenObservers"
+ "_observerLock_lockScreenObservers"
+ "_observerLock_observersForVariant:"
+ "_panGestureRecognizer"
+ "_posterActiveLabel"
+ "_prepareActiveVariantTransition"
+ "_realBackgroundView"
+ "_realForegroundView"
+ "_renderingServiceEndpoint"
+ "_renderingServiceSceneComponent"
+ "_renderingServiceServerKeepAliveAssertionManager"
+ "_rotation"
+ "_salientContentRectangle"
+ "_saturationFilter"
+ "_shouldAnimatePropertyWithKey:"
+ "_tintSource"
+ "_transitioningActiveVariant"
+ "_unlockingKeepRunningAssertion"
+ "_updateActivePosterSceneMode"
+ "_updateActiveVariantTransitionProgress:"
+ "_updateDebugHUD"
+ "_updateDimHomeScreenWallpaperViewAnimated"
+ "_updateEffectiveMotionEffectsModeForSupportedMode:disabled:"
+ "_updateInactiveBlurEffectForWallpaperMode:"
+ "_updateOrientation"
+ "_updatePosterLayers"
+ "_updatePosterScenesForReasons:updater:completion:"
+ "_updatedDimStyle"
+ "_useDimmingColorMatrix"
+ "_userInterfaceStyleTraitDidChange:previousTraitCollection:"
+ "activePosterSceneDefaultModeAssertion"
+ "activelyRequiredReasons"
+ "adaptiveTimeHonorsPreferredSalientContentRectangle"
+ "addAnimations:"
+ "addFailureBlock:scheduler:"
+ "addSuccessBlock:scheduler:"
+ "animateWithSettings:actions:"
+ "areMotionEffectsEnabled"
+ "beginActiveVariantTransition"
+ "blurPhotosWallpaperInAlwaysOn"
+ "bs_array"
+ "bs_performAfterSynchronizedCommit:"
+ "bs_setSafeObject:forKey:"
+ "buildWithError:"
+ "compare:"
+ "compositeLevelSet"
+ "containerView"
+ "copyWithShouldDetermineColorStatistics:"
+ "defaultAnalysisDescriptor"
+ "descriptionForRotation:"
+ "deviceMotionEventGenerationActive"
+ "deviceMotionEventGenerationDidStop"
+ "deviceMotionEventGenerationWillStart"
+ "deviceMotionUpdateInterval"
+ "devicePitch"
+ "deviceRoll"
+ "deviceYaw"
+ "dimStyle"
+ "endActiveVariantTransition"
+ "filters"
+ "filters.gaussianBlur.inputRadius"
+ "gaussianBlur"
+ "handlePanGesture:"
+ "hasRequestedDeviceMotionEvents"
+ "hideHUD"
+ "hitTest:withEvent:"
+ "hitTestViews"
+ "hostDidEndDeviceMotionEventGeneration"
+ "hostWillStartDeviceMotionEventGeneration"
+ "hudWindow"
+ "iconStyleVariant"
+ "iconTintSource"
+ "iconUserInterfaceStyleVariant"
+ "initWithAnimationCurve:"
+ "initWithDuration:timingParameters:"
+ "initWithLevelSets:snapshotDefinitionIdentifier:"
+ "initWithOutputDescriptor:sceneDescriptor:attachments:analysis:"
+ "initWithScene:renderingServiceServerKeepAliveAssertionManager:"
+ "initWithTintColorStyle:suggestedTintColor:tintSource:isHomeScreenDimmed:iconSize:iconStyle:iconStyleVariant:lastUserSelectedVariantForStyleTypeOption:"
+ "interface orientation change from %lu to %lu"
+ "invalidateModelObjectCacheForPath:"
+ "invalidated poster scene: %@"
+ "isDescendantOfView:"
+ "isDeviceMotionEventGenerationActive"
+ "isEqualToArray:"
+ "isHUDEnabled"
+ "isHUDVisible"
+ "isTransitioningActiveVariant"
+ "lastPosition"
+ "lastUserSelectedVariantForStyleTypeOption"
+ "legibilityEnvironment"
+ "legibilityEnvironmentContextForVariant:"
+ "legibilityEnvironmentForUILegibilitySettings:"
+ "motionEffectsEnabled"
+ "noteWorkspaceInstanceSetupForScene:poster:userInfo:"
+ "noteWorkspaceInstanceTeardownForScene:poster:userInfo:"
+ "noteWorkspaceUpdateForScene:poster:userInfo:"
+ "pf_shortDesc"
+ "posterActiveLabel"
+ "posterComponent:didUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:"
+ "posterComponent:didUpdateDeviceMotionEventsRequested:"
+ "posterComponent:didUpdatePreferredDeviceMotionUpdateInterval:"
+ "posterComponent:didUpdatePreferredSalientContentRectangle:"
+ "posterComponent:didUpdateSalientContentRectangleUpdatesRequested:"
+ "posterDidUpdateWantsMotionEvents:"
+ "posterHasRequestedDeviceMotionEvents"
+ "posterWantsDefaultParallax"
+ "pr_adaptiveTimeMode"
+ "pr_adaptiveTimeModeDidChange"
+ "pr_areMotionEffectsDisabled"
+ "pr_deviceMotionEventsRequested"
+ "pr_deviceMotionEventsRequestedDidChange"
+ "pr_effectiveMotionEffectsMode"
+ "pr_preferredDeviceMotionUpdateInterval"
+ "pr_preferredDeviceMotionUpdateIntervalDidChange"
+ "pr_requestedRenderingEventTypes"
+ "pr_setDeviceMotionRotation:"
+ "pr_setDeviceMotionUpdateInterval:"
+ "pr_setDevicePitch:"
+ "pr_setDeviceRoll:"
+ "pr_setDeviceYaw:"
+ "pr_setEffectiveMotionEffectsMode:"
+ "pr_supportedMotionEffectsMode"
+ "pr_supportedMotionEffectsModeDidChange"
+ "preferredDeviceMotionUpdateInterval"
+ "preferredSalientContentRectangle"
+ "pui_determineProminentColorWithCompletion:"
+ "pui_didFinishInitialization"
+ "pui_executeSnapshotForDescriptor:"
+ "pui_preferredSalientContentRectangle"
+ "pui_preferredSalientContentRectangleDidChange"
+ "pui_salientContentRectangleUpdatesRequested"
+ "pui_salientContentRectangleUpdatesRequestedDidChange"
+ "pui_setSalientContentRectangle:"
+ "pui_setUserInterfaceStyle:"
+ "reasons"
+ "registerForTraitChanges:withAction:"
+ "removeAllMotionEffects"
+ "renderingServiceEndpoint"
+ "renderingServiceServer"
+ "rotation"
+ "salientContentRectangle"
+ "salientContentRectangleUpdatesRequested"
+ "scene settings were updated"
+ "schedulerWithDispatchQueue:"
+ "setActivelyRequiredReasons:"
+ "setContainerView:"
+ "setContextID:"
+ "setContextID:scene:"
+ "setDeviceMotionEventGenerationActive:"
+ "setDeviceMotionUpdateInterval:"
+ "setDevicePitch:"
+ "setDevicePitch:roll:yaw:"
+ "setDeviceRoll:"
+ "setDeviceYaw:"
+ "setDim:animated:"
+ "setHitTestViews:"
+ "setHudWindow:"
+ "setIsHUDVisible:"
+ "setLastPosition:"
+ "setLog:"
+ "setMotionEffectsEnabled:"
+ "setMotionEffectsWithFloating:foreground:background:"
+ "setPanGestureRecognizer:"
+ "setPosterActiveLabel:"
+ "setRenderingServiceEndpoint:"
+ "setRotation:"
+ "setSalientContentRectangle:"
+ "setScene:"
+ "setTransitioningActiveVariant:"
+ "setUseDimStyle:"
+ "setUseDimmingColorMatrix:"
+ "setValue:forKeyPath:"
+ "setView:"
+ "setupAndShowHUDWindow"
+ "sharedInstanceForStyle:"
+ "showHUDIfEnabled"
+ "snapshotForLevelSet:"
+ "snapshotLevelSets"
+ "sortedArrayUsingSelector:"
+ "startAnimation"
+ "stateWithTintColorStyle:suggestedTintColor:tintSource:isHomeScreenDimmed:iconSize:iconStyle:iconStyleVariant:lastUserSelectedVariantForStyleTypeOption:"
+ "tintSource"
+ "transitioningActiveVariant"
+ "typeof (((typeof (PLKLegibilityEnvironmentVariantDefault) (*)(void))0)()) getPLKLegibilityEnvironmentVariantDefault(void)"
+ "typeof (((typeof (PLKLegibilityEnvironmentVariantHomeScreen) (*)(void))0)()) getPLKLegibilityEnvironmentVariantHomeScreen(void)"
+ "typeof (((typeof (PLKLegibilityEnvironmentVariantLockScreen) (*)(void))0)()) getPLKLegibilityEnvironmentVariantLockScreen(void)"
+ "unlock progress"
+ "updateActiveVariantTransitionProgress:"
+ "updateMotionWithRotation:"
+ "updatePresentation:"
+ "updateSalientContentRectangle:"
+ "updateSettings:"
+ "updateWallpaperAnimationWithPitch:roll:yaw:"
+ "updateWallpaperAnimationWithRotation:"
+ "updateWithLegibilitySettings:variants:"
+ "updateWithLockSceneActivityMode:homeSceneActivityMode:activeVariant:wallpaperStyle:homeAndLockAreSame:isActivelyRequired:activelyRequiredReasons:assertionReasons:"
+ "useDimmingColorMatrix"
+ "user interface style did change"
+ "userSelectedVariantsForStyleTypes"
+ "v16@?0@\"<PBUIWallpaperObserver>\"8"
+ "v16@?0@\"PUIPosterSnapshotBundle\"8"
+ "v20@0:8I16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@\"PLKLegibilityEnvironment\"16"
+ "v28@0:8I16@20"
+ "v28@0:8Q16B24"
+ "v32@0:8@\"<PBUIPosterComponent>\"16d24"
+ "v40@0:8:16q24@?32"
+ "v40@0:8d16d24d32"
+ "v40@0:8q16@?24@?32"
+ "v48@0:8(?={?=}{?=})16"
+ "v56@0:8@\"<PBUIPosterComponent>\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v64@0:8c16c20q24q32B40B44@48@56"
+ "valueWithCAColorMatrix:"
+ "variants"
+ "void *PosterFuturesKitLibrary(void)"
+ "void *PosterKitLibrary(void)"
+ "void *PosterLegibilityKitLibrary(void)"
+ "wallpaperDidUpdateAdaptiveTimeHonorsPreferredSalientContentRectangle:"
+ "wallpaperDidUpdatePreferredDeviceMotionUpdateInterval:"
+ "wallpaperDidUpdatePreferredSalientContentRectangle:"
+ "wallpaperLegibilityEnvironmentDidChange:"
+ "wantsDefaultParallaxTreatment"
+ "\xf0\xc1"
+ "\xf0\xf0!"
+ "\xf0\xf1"
- "%@.CoreImage-Context"
- "%@.command-queue"
- "%@.next-frame-waiter"
- "%@:%d"
- "%f (%@)"
- "("
- "(%d) end %{public}s; completed in %.4f"
- "(%d) start %{public}s"
- "-[PBUICALocalRenderer renderRequest:error:]"
- "-[PBUIWallpaperLegibilityTreatment luminanceTreatmentFilters]"
- "0\"1"
- "<PIParallaxLegacyPosterStyle> could not be loaded."
- "@\"<CAAction>\"32@0:8@\"CALayer\"16@\"NSString\"24"
- "@\"<MTLCommandQueue>\""
- "@\"<MTLDevice>\""
- "@\"<PBUIImageTreatment>\""
- "@\"<PBUIRemoteRendererConnection>\""
- "@\"<PBUIRenderServiceInterface>\"24@0:8@?<v@?@\"NSError\">16"
- "@\"<PBUIRenderer>\""
- "@\"CABackdropLayer\""
- "@\"CAGradientLayer\""
- "@\"CALayer\""
- "@\"CIContext\""
- "@\"CIImage\"40@0:8@\"CIImage\"16@\"PBUIImageTreatmentOptions\"24o^@32"
- "@\"IOSurface\"32@0:8@\"<PBUIRenderRequest>\"16o^@24"
- "@\"NSBundle\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSProgress\"32@0:8@\"PRUISAnalysisServiceRequest\"16@?<v@?@\"PRUISAnalysisServiceResponse\"@\"NSError\">24"
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@\"PBUICodableImage\""
- "@\"PBUIViewportLayer\""
- "@\"PRUISAnalysisServiceResponse\"32@0:8@\"PRUISAnalysisServiceRequest\"16o^@24"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8^{CGColorSpace=}16"
- "@32@0:8@16^{CGColorSpace=}24"
- "@32@0:8@16o^@24"
- "@32@0:8^{CGImage=}16o^@24"
- "@40@0:8@16@24^{CGColorSpace=}32"
- "@40@0:8@16d24@32"
- "@40@0:8@16d24o^@32"
- "@40@0:8^{CGImage=}16d24o^@32"
- "@40@0:8{CGSize=dd}16^{CGColorSpace=}32"
- "@48@0:8^{CGImage=}16d24d32@40"
- "@48@0:8{CGSize=dd}16^{CGColorSpace=}32^Q40"
- "@52@0:8@16@24B32@36@44"
- "@64@0:8{PBUIRenderState={CGSize=dd}d@@}16o^@56"
- "@?16@0:8"
- "Apr 19 2025 02:54:05"
- "AverageColor"
- "B32@0:8N^{PBUIRenderState={CGSize=dd}d@@}16o^@24"
- "B40@0:8@\"PBUIImageContainerLayer\"16@\"PBUIImageTreatmentOptions\"24o^@32"
- "B40@0:8@16@24o^@32"
- "B40@0:8q16@24@32"
- "B56@0:8{PBUIRenderState={CGSize=dd}d@@}16"
- "BSXPCSecureCoding"
- "CABackdropLayerDelegate"
- "CALayerDelegate"
- "CGImageSource could not create an image."
- "CIContext"
- "CIImage"
- "CPBitmap file contained no images."
- "Check CoreAnimation logs."
- "Check os_log for errors from ImageIO."
- "Check that it should exist on this platform and that you are able to link it."
- "Check that the current process is able to link CoreMaterial and MaterialKit."
- "Class getMTMaterialLayerClass(void)_block_invoke"
- "Class getPIParallaxLegacyPosterStyleClass(void)_block_invoke"
- "Class getPRUISAnalysisServiceClass(void)_block_invoke"
- "Class getPRUISSnapshotServiceClass(void)_block_invoke"
- "Connection to service (%@) refused on activation."
- "CoreAnimation failed to write .ca file to URL."
- "Created new poster scene: %@"
- "DIM_ANIMATION"
- "Data is not a valid image format."
- "DownscaleFactor"
- "Ensure this process has the correct sandbox for connection and that the service is not crashing or failing to load."
- "IOSurface failed to be made into a CGImage."
- "Identifier"
- "Image"
- "Image Layer"
- "Image creation failed."
- "Image destination failed to be created to Data."
- "Image did not have a valid representation."
- "Image final encoding failed for unknown reasons in CoreGraphics."
- "LegacyPoster"
- "MTMaterialLayer"
- "MTMaterialLayer could not be loaded."
- "NSString *getPUIImageEncoderErrorDomain(void)"
- "NeedsDimmingTreatment"
- "NeedsLuminanceTreatment"
- "PBUICALocalRenderer"
- "PBUICARemoteRenderer"
- "PBUICARemoteRenderer.m"
- "PBUICARemoteRendererServiceInterfaces"
- "PBUICodableImage"
- "PBUICodableImage BSXPCDecoding failed: %@"
- "PBUICodableImage.m"
- "PBUIImageContainerLayer"
- "PBUIImageTreatment"
- "PBUIImageTreatmentOptions"
- "PBUIMaterialTreatment"
- "PBUIMaterialTreatment.m"
- "PBUIRemoteRendererConnection"
- "PBUIRemoteRendererXPCConnection"
- "PBUIRenderRequest"
- "PBUIRenderServiceInterface"
- "PBUIRenderer"
- "PBUITreatImageRequest"
- "PBUIViewportLayer"
- "PBUIWallpaperInactiveTreatment"
- "PBUIWallpaperInactiveTreatment does not support CoreAnimation rendering."
- "PBUIWallpaperInactiveTreatment.m"
- "PBUIWallpaperLegibilityTreatment"
- "PBUIWallpaperLegibilityTreatment.m"
- "PIParallaxLegacyPosterStyle"
- "PRUISAnalysisService"
- "PRUISAnalysisServiceInterface"
- "PRUISSnapshotService"
- "PRUISSnapshotServiceInterface"
- "Parallax is enabled, %@ provided content size %@ and %@ is needed."
- "Parallax is enabled, but %@ provided content size %@ when %@ is needed. Parallax will be disabled."
- "Q24@0:8Q16"
- "RecipeBundle_URL"
- "RecipeName"
- "Request cannot be rendered remotely."
- "Request class (`%@`) is not <NSSecureCoding> with `+(BOOL)supportsSecureCoding` returning `YES`"
- "ResolvedBackdropScaleAdjustment"
- "Scale Layer"
- "Somehow a PBUICodableImage was made that had no actual source or image."
- "T@\"<MTLCommandQueue>\",R,N,V_commandQueue"
- "T@\"<MTLDevice>\",R,N,V_device"
- "T@\"<PBUIImageTreatment>\",&,N,V_treatment"
- "T@\"<PBUIRemoteRendererConnection>\",R,N,V_underlyingConnection"
- "T@\"<PBUIRenderer>\",&,N,V_renderer"
- "T@\"<PBUIRenderer>\",R,N"
- "T@\"CALayer\",&,N,V_imageLayer"
- "T@\"CALayer\",R,N,V_contentLayer"
- "T@\"NSBundle\",&,N,V_recipeBundle"
- "T@\"NSObject<OS_os_log>\",&,N,V_logger"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",C,N,V_recipeName"
- "T@\"PBUIRemoteRendererXPCConnection\",R,N"
- "T@\"UIColor\",&,N,V_averageColor"
- "T@?,C,N,V_backdropScaleAdjustment"
- "TB,N,V_needsDimmingTreatment"
- "TB,N,V_needsLuminanceTreatment"
- "TB,R,N,V_usesStaticBackdropScaleFactor"
- "T^{CGColorSpace=},R,N"
- "T^{CGImage=},N,V_image"
- "Td,N,V_downscaleFactor"
- "Td,N,V_scale"
- "Td,N,V_weighting"
- "Td,R,N,V_originalScale"
- "Td,R,N,V_reducedScale"
- "Td,R,N,V_scale"
- "The bitmap file was valid, it just had no images."
- "TreatImage(%@)"
- "Treatment"
- "UNREACHABLE: no image or any source was avaliable to encode."
- "URL is either not readable or is not a valid image file."
- "URLForResource:withExtension:"
- "Use a PBUIRenderer that support CoreImage."
- "Viewport Layer"
- "WallpaperLuminanceMap"
- "Weighting"
- "[%{public}@]\t--> '%{public}@'"
- "[Possibly Expected Error] CPBitmap read failed will fallback to ImageIO. The source data is unlikely a cpbitmap so you can normally ignore this: %@"
- "[Possibly Expected Error] CPBitmap read failed. The source data is unlikely a cpbitmap so you can normally ignore this: %@"
- "^{CGColorSpace=}"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{CGImage=}24@0:8^@16"
- "^{CGImage=}32@0:8@16o^@24"
- "_averageColor"
- "_backdropScaleAdjustment"
- "_bitmapSourceData"
- "_cachedImage"
- "_ciContext"
- "_codableImage"
- "_colorSpace"
- "_commandQueue"
- "_connectionLock"
- "_contentLayer"
- "_currentRenderState"
- "_device"
- "_dimmedColorLayer"
- "_dimmingLayer"
- "_downscaleFactor"
- "_encodingLock"
- "_endpoint"
- "_gradientLayer"
- "_imageLayer"
- "_lock_connection"
- "_logger"
- "_luminanceBackdropLayer"
- "_needsDimmingTreatment"
- "_needsLuminanceTreatment"
- "_originalScale"
- "_recipeBundle"
- "_recipeName"
- "_reducedScale"
- "_representation"
- "_serviceName"
- "_sourceImage"
- "_surface"
- "_treatment"
- "_underlyingConnection"
- "_updateFloatingLayer"
- "_updatePresentation"
- "_usesStaticBackdropScaleFactor"
- "_viewportLayer"
- "_weighting"
- "actionForLayer:forKey:"
- "addCompletedHandler:"
- "animationWithKeyPath:"
- "anyObject"
- "applyInactiveStyleToImage:error:"
- "applyToImage:options:error:"
- "archiveRenderingOfRequest:toURL:error:"
- "backdropLayer:didChangeLuma:"
- "backdropScale"
- "backdropScaleAdjustment"
- "beginFrameAtTime:timeStamp:"
- "blurRadiusTransformer"
- "bs_IOSurfaceWithWidth:height:options:"
- "bs_encodeRepresentation:value:withCoder:"
- "buildCGImageWithError:"
- "bundleURL"
- "bundleWithURL:"
- "cachedSnapshotForRequest:reply:"
- "canInterpolateToLowerScales"
- "cancelRequest:"
- "capturedColorStatistics"
- "capturedSnapshotForLevelSet:"
- "capturedSnapshotLevelSets"
- "checkinWithReply:"
- "colorByDimmingColor:"
- "colorSpace"
- "com.apple.PaperBoardUI.PBUIRenderer"
- "com.apple.PaperBoardUI.RendererService"
- "com.apple.springboard.SBRendererService"
- "commandBuffer"
- "commandQueue"
- "commitToRenderingTree:options:error:"
- "componentsSeparatedByString:"
- "configureState:error:"
- "configureWithTransaction:"
- "connectionActivateIfNeededWithError:"
- "contentDidChange:%@ needsUpdateForInterfaceStyle:%@"
- "contentLayer"
- "contextWithMTLCommandQueue:options:"
- "createCGImageFromCPBitmapData:error:"
- "createCGImageFromData:error:"
- "createCGImageFromURL:error:"
- "d32@?0d8d16d24"
- "data"
- "data != ((void*)0)"
- "dataRepresentationForImage:error:"
- "decodeXPCObjectOfType:forKey:"
- "defaultConnection"
- "depends-on-weight"
- "device"
- "displayLayer:"
- "downscaleFactor"
- "drawLayer:inContext:"
- "encodeRepresentation:value:withCoder:"
- "encodeWithBSXPCCoder:"
- "encodeXPCObject:forKey:"
- "endFrame"
- "endpoint"
- "enqueue"
- "executeAnalysisRequest:error:"
- "executeAnalysisRequest:reply:"
- "executeSnapshotRequest:reply:"
- "failWithError:"
- "fetchColorSpaceNameWithReply:"
- "fileURL"
- "fixed"
- "flush"
- "grayColor"
- "height"
- "imageByApplyingTransform:"
- "imageData"
- "imageLayer"
- "imagePixelSize"
- "imageRef"
- "imageWithCGImage:options:"
- "initFromSourceData:scale:error:"
- "initFromURL:scale:error:"
- "initToEndpoint:"
- "initToServiceName:"
- "initWithBSXPCCoder:"
- "initWithCGImage:scale:error:"
- "initWithColorSpace:"
- "initWithDevice:colorSpace:"
- "initWithDevice:commmandQueue:colorSpace:"
- "initWithIOSurface:"
- "initWithIOSurface:scale:error:"
- "initWithImage:scale:downscaleFactor:treatment:"
- "initWithLayer:"
- "initWithListenerEndpoint:"
- "initWithScale:"
- "initWithServiceName:"
- "initWithTintColorStyle:suggestedTintColor:isHomeScreenDimmed:iconSize:iconStyle:"
- "initWithTypeRecord:destinationOptions:addImageOptions:"
- "initWithUnderlyingConnection:"
- "inputColorMap"
- "interfaceWithProtocol:"
- "invalid variant %ld"
- "iosurface"
- "isEqualRepresentation:"
- "isFrontBoard"
- "kCARendererFlags"
- "lastObject"
- "layerWillDraw:"
- "layoutSublayers"
- "layoutSublayersOfLayer:"
- "logger"
- "luminanceMapURL"
- "luminanceTreatmentFilters"
- "makeDimmingLayer"
- "makeGradientLayer"
- "makeLuminanceBackdropLayer"
- "makeWithOther:"
- "needsDimmingTreatment"
- "needsLuminanceTreatment"
- "newCommandBufferWithCompletion:"
- "newCommandQueue"
- "newSurfaceWithSize:colorSpace:outOptions:"
- "newTextureWithDescriptor:iosurface:plane:"
- "newTextureWithSize:colorSpace:"
- "nextFrameHandlerWithCompletion:"
- "nextFrameTime"
- "originalScale"
- "pb_applyLegacySettings"
- "pb_shortDesc"
- "pid"
- "pixelFormatForBSIOSurfaceOptions:"
- "png"
- "pr_contentSize"
- "pr_contentSizeDidChange"
- "pr_isParallaxEffectivelyEnabled"
- "pr_setParallaxEnabled:"
- "presentationLayer"
- "pruis_determineProminentColorWithCompletion:"
- "pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:"
- "rangeOfString:"
- "recipe"
- "recipeBundle"
- "recipeName"
- "reducedScale"
- "refersToIdenticalImageFrom:"
- "remoteObjectProxyWithErrorHandler:"
- "removeFromSuperlayer"
- "render"
- "renderCIImage:toSurface:completionHandler:"
- "renderFrameToTexture:configureWithTransaction:completionHandler:"
- "renderRequest:completionHandler:"
- "renderRequest:reply:"
- "renderState:completionHandler:"
- "renderState:error:"
- "rendererForDestination:"
- "rendererWithMTLTexture:options:"
- "replaceSublayer:with:"
- "representation"
- "requestedOutputSizeInPixels"
- "requestedOutputSizeInPointsAtScale:"
- "resetState"
- "resolveAddImageOptionsForImage:"
- "resolveDestinationOptionsForImage:"
- "resolvedBackdropScale"
- "scaleReductionFactor"
- "secureCodableRequestClasses"
- "secureCodableResponseClasses"
- "secureCodableTreatmentClasses"
- "serviceName"
- "service_warmup:"
- "setAllowGPUOptimizedContents:"
- "setBackdropScaleAdjustment:"
- "setBlurRadiusTransformer:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setContentsGravity:"
- "setDamping:"
- "setDestination:"
- "setDownscaleFactor:"
- "setFromValue:"
- "setImageLayer:"
- "setInitialVelocity:"
- "setLabel:"
- "setLayer:"
- "setLogger:"
- "setMass:"
- "setPurgeableState:"
- "setRecipeBundle:"
- "setRecipeName:"
- "setRecipeName:fromBundle:"
- "setRemoteObjectInterface:"
- "setRenderState:"
- "setScale:"
- "setStiffness:"
- "setToValue:"
- "setTreatment:"
- "setUsage:"
- "shouldUseXPCServiceForRendering"
- "softlink:r:path:/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial"
- "softlink:r:path:/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging"
- "softlink:r:path:/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices"
- "softlink:r:path:/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation"
- "startTaskToRender:toDestination:error:"
- "stateWithTintColorStyle:suggestedTintColor:isHomeScreenDimmed:iconSize:iconStyle:"
- "sublayers"
- "supportsBSXPCSecureCoding"
- "supportsRequest:orError:"
- "surface"
- "surfaceCreatingIfNecessary:"
- "sync render request"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "treatment"
- "treatmentOptions"
- "typeIdentifier"
- "underlyingConnection"
- "updatePresentation"
- "updateStateWithTransaction:"
- "usesCoreImageForState:"
- "usesCoreImageForTreatment:"
- "usesStaticBackdropScaleFactor"
- "v16@?0@\"<MTLCommandBuffer>\"8"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"CALayer\"16"
- "v24@0:8@\"PRUISAnalysisServiceRequest\"16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8^{CGImage=}16"
- "v24@?0@\"IOSurface\"8@\"NSError\"16"
- "v28@?0B8@\"PUIPosterSnapshotBundleBuilder\"12@\"NSError\"20"
- "v32@0:8@\"<PBUIRenderRequest>\"16@?<v@?@\"IOSurface\"@\"NSError\">24"
- "v32@0:8@\"<PBUIRenderRequest><NSSecureCoding>\"16@?<v@?@\"IOSurface\"@\"NSError\">24"
- "v32@0:8@\"CABackdropLayer\"16d24"
- "v32@0:8@\"CALayer\"16^{CGContext=}24"
- "v32@0:8@\"PRUISSnapshotServiceRequest\"16@?<v@?@\"PRUISSnapshotServiceResponse\"@\"NSError\">24"
- "v32@0:8@16^{CGContext=}24"
- "v56@0:8{PBUIRenderState={CGSize=dd}d@@}16"
- "v64@0:8{PBUIRenderState={CGSize=dd}d@@}16@?56"
- "valueForKey:"
- "void *CoreMaterialLibrary(void)"
- "void *PhotoImagingLibrary(void)"
- "waitUntilCompleted"
- "{PBUIRenderState=\"outputPixelSize\"{CGSize=\"width\"d\"height\"d}\"scale\"d\"layer\"@\"CALayer\"\"image\"@\"CIImage\"}"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "\xd1"
- "\xf0q"
- "\xf0\xd1"

```
