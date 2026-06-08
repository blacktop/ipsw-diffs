## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-417.4.4.0.0
-  __TEXT.__text: 0x1e878
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x2564
-  __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x1e7d
-  __TEXT.__oslogstring: 0x14dc
-  __TEXT.__gcc_except_tab: 0x30c
+437.100.0.0.0
+  __TEXT.__text: 0x1e5ac
+  __TEXT.__objc_methlist: 0x265c
+  __TEXT.__const: 0x27c
+  __TEXT.__cstring: 0x207d
+  __TEXT.__oslogstring: 0x17cc
+  __TEXT.__gcc_except_tab: 0x410
   __TEXT.__dlopen_cstrs: 0x4ae
-  __TEXT.__unwind_info: 0xb38
-  __TEXT.__objc_classname: 0x832
-  __TEXT.__objc_methname: 0x6600
-  __TEXT.__objc_methtype: 0xfc5
-  __TEXT.__objc_stubs: 0x5a20
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0xb00
+  __TEXT.__unwind_info: 0xb40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xba8
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b88
+  __DATA_CONST.__objc_selrefs: 0x1c80
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x490
-  __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0x1f20
-  __AUTH_CONST.__objc_const: 0x4b90
+  __DATA_CONST.__got: 0x6e8
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x2060
+  __AUTH_CONST.__objc_const: 0x4d60
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x268
-  __DATA.__data: 0x6e0
-  __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xf0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x284
+  __DATA.__data: 0x740
+  __DATA.__bss: 0x178
+  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B08A631F-B0CA-3FB0-A1DC-7721E6957A8F
-  Functions: 955
-  Symbols:   3838
-  CStrings:  2062
+  UUID: 16BCE485-94B8-398D-A3A6-C629CAD384C0
+  Functions: 981
+  Symbols:   3940
+  CStrings:  746
 
Symbols:
+ +[SSChromeHelper availableRectForFullscreenContent:layoutBounds:bleedToBottom:topBarHeight:bottomBarHeight:userInterfaceIdiom:multipleScreenshots:isPhoneLandscape:]
+ +[SSChromeHelper screenshotBottomMargin:isPhoneLandscape:]
+ +[SSChromeHelper screenshotBottomMarginPhoneIsLandscape:]
+ +[SSScreenSnapshot snapshotWithImage:fromWindowScene:]
+ +[SSScreenSnapshotter snapshotterForWindowScene:]
+ +[SSScreenshotCapturingContext contextWithScreen:]
+ +[SSScreenshotCapturingContext contextWithWindowScene:]
+ -[SSActiveInterfaceOrientationObserver _notifyActiveInterfaceOrientationDidChangeToOrientation:withDuration:]
+ -[SSEnvironmentDescription displayIdentity]
+ -[SSEnvironmentDescription setDisplayIdentity:]
+ -[SSImageSurface initWithScale:imageOrientation:]
+ -[SSMainScreenSnapshotter _snapshotOptions]
+ -[SSOtherScreenSnapshotter _snapshotOptions]
+ -[SSRemoteAlertHandleProvider _screenshotServicesAlertHandle]
+ -[SSRemoteAlertHandleProvider _screenshotServicesAlertHandle].cold.1
+ -[SSRemoteAlertHandleProvider _screenshotServicesAlertHandle].cold.2
+ -[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:completion:]
+ -[SSScreenCapturer _takeScreenshotWithOptionsCollection:serviceOptions:presentationOptions:appleInternalOptions:].cold.1
+ -[SSScreenCapturerScreenshotOptionsCollection screenshotOptionsForWindowScene:]
+ -[SSScreenCapturerScreenshotOptionsCollection setScreenshotOptions:forWindowScene:]
+ -[SSScreenSnapshot _initWithImage:screen:windowScene:]
+ -[SSScreenSnapshot windowScene]
+ -[SSScreenSnapshotter _snapshotOptions]
+ -[SSScreenSnapshotter initWithWindowScene:]
+ -[SSScreenSnapshotter screenshotRenderingOverrides]
+ -[SSScreenSnapshotter setScreenshotRenderingOverrides:]
+ -[SSScreenSnapshotter windowScene]
+ -[SSScreenshotAssetManagerRegistrationOptions isPDFImage]
+ -[SSScreenshotAssetManagerRegistrationOptions setIsPDFImage:]
+ -[SSScreenshotCapturingContext .cxx_destruct]
+ -[SSScreenshotCapturingContext _initWithWindowScene:screen:]
+ -[SSScreenshotCapturingContext screen]
+ -[SSScreenshotCapturingContext screenshotRenderingOverrides]
+ -[SSScreenshotCapturingContext setScreenshotRenderingOverrides:]
+ -[SSScreenshotCapturingContext windowScene]
+ -[SSScreenshotsWindow _updateBacklightObservationForWindowScene:]
+ -[SSScreenshotsWindow backlight:didCompleteUpdateToState:forEvent:]
+ -[SSScreenshotsWindow setWindowScene:]
+ -[SSSnapshotter _captureScreenshotWithCapturingContext:screenshotOptionsCollection:]
+ -[SSSnapshotter captureSnapshotsForScreenshotCapturingContexts:withOptionsCollection:didFindOnenessScreens:]
+ GCC_except_table22
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table35
+ GCC_except_table41
+ _AFVisualIntelligenceScreenshotsRestricted
+ _BSEqualObjects
+ _NSStringFromSelector
+ _OBJC_CLASS_$_BLSBacklight
+ _OBJC_CLASS_$_BLSDisplayReference
+ _OBJC_CLASS_$_CADisplay
+ _OBJC_CLASS_$_FBSDisplayIdentity
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SSScreenshotCapturingContext
+ _OBJC_IVAR_$_SSEnvironmentDescription._displayIdentity
+ _OBJC_IVAR_$_SSScreenCapturer._initialLayoutGroup
+ _OBJC_IVAR_$_SSScreenSnapshot._windowScene
+ _OBJC_IVAR_$_SSScreenSnapshotter._screenshotRenderingOverrides
+ _OBJC_IVAR_$_SSScreenSnapshotter._windowScene
+ _OBJC_IVAR_$_SSScreenshotAssetManagerRegistrationOptions._isPDFImage
+ _OBJC_IVAR_$_SSScreenshotCapturingContext._screen
+ _OBJC_IVAR_$_SSScreenshotCapturingContext._screenshotRenderingOverrides
+ _OBJC_IVAR_$_SSScreenshotCapturingContext._windowScene
+ _OBJC_IVAR_$_SSScreenshotsWindow._backlight
+ _OBJC_METACLASS_$_SSScreenshotCapturingContext
+ __OBJC_$_CLASS_METHODS_SSScreenshotCapturingContext
+ __OBJC_$_INSTANCE_METHODS_SSScreenshotCapturingContext
+ __OBJC_$_INSTANCE_VARIABLES_SSScreenshotCapturingContext
+ __OBJC_$_PROP_LIST_SSScreenshotCapturingContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_REFS_BLSBacklightStateObserving
+ __OBJC_CLASS_RO_$_SSScreenshotCapturingContext
+ __OBJC_LABEL_PROTOCOL_$_BLSBacklightStateObserving
+ __OBJC_METACLASS_RO_$_SSScreenshotCapturingContext
+ __OBJC_PROTOCOL_$_BLSBacklightStateObserving
+ __SSDeviceSupportsHDRCaptureForWindowScene
+ __SSDisableMDMRestrictionForVI
+ __SSEnableHighQualityCapture
+ __SSHighQualityCaptureEnabled
+ __SSVisualIntelligenceEnabled_iPad
+ __SSVisualIntelligenceV2DeviceSupported.deviceSupported
+ __SSVisualIntelligenceV2DeviceSupported.onceToken
+ __SSVisualIntelligenceV2Elegible.cold.1
+ __SSVisualIntelligenceV2EnabledIgnoringOrientation.cold.1
+ __SSVisualIntelligenceV2EnabledIgnoringOrientation.cold.2
+ ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.54
+ ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.54.cold.1
+ ___106-[SSApplicationScreenshotSupplementalDataCapturer _sendRequestForEnvironmentElement:info:completionBlock:]_block_invoke.17
+ ___106-[SSApplicationScreenshotSupplementalDataCapturer _sendRequestForEnvironmentElement:info:completionBlock:]_block_invoke.21
+ ___113-[SSScreenCapturer _takeScreenshotWithOptionsCollection:serviceOptions:presentationOptions:appleInternalOptions:]_block_invoke.76
+ ___162-[SSScreenshotAssetManagerPhotoLibraryBackend updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:]_block_invoke.70
+ ___24-[SSScreenCapturer init]_block_invoke
+ ___24-[SSScreenCapturer init]_block_invoke.19
+ ___24-[SSScreenCapturer init]_block_invoke_2
+ ___37-[SSScreenSnapshotter takeScreenshot]_block_invoke
+ ___65-[SSScreenshotsWindow _updateBacklightObservationForWindowScene:]_block_invoke
+ ___79-[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:completion:]_block_invoke
+ ___79-[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:completion:]_block_invoke.cold.1
+ ___SBUIGetUserAgent
+ ___SBUIGetUserAgent.cold.1
+ ____SSVisualIntelligenceV2DeviceSupported_block_invoke
+ ___block_descriptor_40_e8_32bs_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24ls32l8
+ ___block_descriptor_40_e8_32s_e19_B16?0"CADisplay"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e26_v16?0"BSActionResponse"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e18_v16?0"NSString"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e21_v20?0B8"NSString"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.126
+ ___block_literal_global.131
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.368
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.376
+ ___block_literal_global.378
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.39
+ ___block_literal_global.47
+ ___block_literal_global.52
+ ___block_literal_global.60
+ ___block_literal_global.73
+ ___block_literal_global.76
+ ___block_literal_global.80
+ ___block_literal_global.83
+ __bs_set_crash_log_message
+ __os_log_default
+ _kUIRenderingSourceWindowScene
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_captureScreenshotWithCapturingContext:screenshotOptionsCollection:
+ _objc_msgSend$_initWithImage:screen:windowScene:
+ _objc_msgSend$_initWithWindowScene:screen:
+ _objc_msgSend$_notifyActiveInterfaceOrientationDidChangeToOrientation:withDuration:
+ _objc_msgSend$_saveImageToPhotoLibrary:environmentDescription:completion:
+ _objc_msgSend$_screenshotServicesAlertHandle
+ _objc_msgSend$_snapshotOptions
+ _objc_msgSend$_updateBacklightObservationForWindowScene:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$allKeys
+ _objc_msgSend$availableRectForFullscreenContent:layoutBounds:bleedToBottom:topBarHeight:bottomBarHeight:userInterfaceIdiom:multipleScreenshots:isPhoneLandscape:
+ _objc_msgSend$bs_dictionaryByAddingEntriesFromDictionary:
+ _objc_msgSend$bs_filter:
+ _objc_msgSend$captureSnapshotsForScreenshotCapturingContexts:withOptionsCollection:didFindOnenessScreens:
+ _objc_msgSend$display
+ _objc_msgSend$displayIdentity
+ _objc_msgSend$displays
+ _objc_msgSend$doesMatchCADisplay:
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$identityForEmbeddedApplicationIdentifier:
+ _objc_msgSend$initForDisplay:
+ _objc_msgSend$initWithScale:imageOrientation:
+ _objc_msgSend$initWithSceneProvidingProcess:configurationIdentifier:
+ _objc_msgSend$initWithWindowScene:
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$isEnhancedSiriAvailable
+ _objc_msgSend$isEnhancedSiriEnabled
+ _objc_msgSend$isPDFImage
+ _objc_msgSend$lookupHandlesForDefinition:creatingIfNone:configurationContext:
+ _objc_msgSend$referenceForCADisplay:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$screenCapturer:didCaptureScreenshotsOfWindowScenes:
+ _objc_msgSend$screenshotBottomMargin:isPhoneLandscape:
+ _objc_msgSend$screenshotBottomMarginPhoneIsLandscape:
+ _objc_msgSend$screenshotCapturingContextsToCapture:
+ _objc_msgSend$screenshotOptionsForWindowScene:
+ _objc_msgSend$screenshotRenderingOverrides
+ _objc_msgSend$setDisplayIdentity:
+ _objc_msgSend$setScreenshotOptions:forScreen:
+ _objc_msgSend$setScreenshotRenderingOverrides:
+ _objc_msgSend$setTransitionHandler:
+ _objc_msgSend$settings
+ _objc_msgSend$snapshotWithImage:fromWindowScene:
+ _objc_msgSend$snapshotterForWindowScene:
+ _objc_msgSend$uniqueId
+ _objc_msgSend$windowScene
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- +[SSChromeHelper availableRectForFullscreenContent:layoutBounds:bleedToBottom:topBarHeight:bottomBarHeight:userInterfaceIdiom:multipleScreenshots:]
- +[SSChromeHelper screenshotBottomMargin:]
- +[SSChromeHelper screenshotBottomMarginPhone]
- -[SSActiveInterfaceOrientationObserver _observeActiveInterfaceOrientationChangeToOrientation:withDuration:]
- -[SSActiveInterfaceOrientationObserver _registerForActiveInterfaceOrientationChanges]
- -[SSActiveInterfaceOrientationObserver _sbUIUserAgent]
- -[SSActiveInterfaceOrientationObserver _sbUIUserAgent].cold.1
- -[SSActiveInterfaceOrientationObserver _unregisterForActiveInterfaceOrientationChanges]
- -[SSImageSurface init]
- -[SSMainScreenSnapshotter takeScreenshot]
- -[SSOtherScreenSnapshotter takeScreenshot]
- -[SSRemoteAlertHandleProvider _screenshotServicesServiceAlertDefinition]
- -[SSRemoteAlertHandleProvider screenshotServicesAlertHandle]
- -[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:]
- -[SSScreenshotsWindow _deviceBacklightChanged:]
- -[SSSnapshotter _captureScreen:withScreenshotOptions:]
- -[SSSnapshotter _screensThatAreCaptureableDidFindOnenessScreens:]
- -[SSSnapshotter captureAvailableSnapshotsWithOptionsCollection:didFindOnenessScreens:]
- -[_SSScreenCaptureResults .cxx_destruct]
- -[_SSScreenCaptureResults failureReasonIfImageIsNil]
- -[_SSScreenCaptureResults image]
- -[_SSScreenCaptureResults setFailureReasonIfImageIsNil:]
- -[_SSScreenCaptureResults setImage:]
- GCC_except_table19
- GCC_except_table2
- GCC_except_table26
- GCC_except_table27
- GCC_except_table33
- GCC_except_table34
- GCC_except_table39
- _AFVisualIntelligenceCameraRestricted
- _OBJC_CLASS_$__SSScreenCaptureResults
- _OBJC_IVAR_$_SSScreenshotsWindow._backlightNotificationToken
- _OBJC_IVAR_$__SSScreenCaptureResults._failureReasonIfImageIsNil
- _OBJC_IVAR_$__SSScreenCaptureResults._image
- _OBJC_METACLASS_$__SSScreenCaptureResults
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- __OBJC_$_INSTANCE_METHODS__SSScreenCaptureResults
- __OBJC_$_INSTANCE_VARIABLES__SSScreenCaptureResults
- __OBJC_$_PROP_LIST__SSScreenCaptureResults
- __OBJC_CLASS_RO_$__SSScreenCaptureResults
- __OBJC_METACLASS_RO_$__SSScreenCaptureResults
- ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.51
- ___103-[SSScreenshotAssetManagerPhotoLibraryBackend _registerEntryWithImage:options:retry:identifierHandler:]_block_invoke.51.cold.1
- ___162-[SSScreenshotAssetManagerPhotoLibraryBackend updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:]_block_invoke.67
- ___27-[SSScreenshotsWindow init]_block_invoke_4
- ___27-[SSScreenshotsWindow init]_block_invoke_5
- ___41-[SSMainScreenSnapshotter takeScreenshot]_block_invoke
- ___42-[SSOtherScreenSnapshotter takeScreenshot]_block_invoke
- ___65-[SSSnapshotter _screensThatAreCaptureableDidFindOnenessScreens:]_block_invoke
- ___65-[SSSnapshotter _screensThatAreCaptureableDidFindOnenessScreens:]_block_invoke_2
- ___68-[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:]_block_invoke
- ___68-[SSScreenCapturer _saveImageToPhotoLibrary:environmentDescription:]_block_invoke.cold.1
- ___block_descriptor_32_e18_B16?0"UIScreen"8l
- ___block_descriptor_56_e8_32s40s48s_e21_v20?0B8"NSString"12ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48bs_e18_v16?0"UIScreen"8ls48l8s32l8s40l8
- ___block_literal_global.119
- ___block_literal_global.343
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.36
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.375
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.385
- ___block_literal_global.387
- ___block_literal_global.45
- ___block_literal_global.49
- ___block_literal_global.54
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.74
- ___block_literal_global.77
- _objc_autorelease
- _objc_msgSend$_captureScreen:withScreenshotOptions:
- _objc_msgSend$_deviceBacklightChanged:
- _objc_msgSend$_observeActiveInterfaceOrientationChangeToOrientation:withDuration:
- _objc_msgSend$_registerForActiveInterfaceOrientationChanges
- _objc_msgSend$_saveImageToPhotoLibrary:environmentDescription:
- _objc_msgSend$_sbUIUserAgent
- _objc_msgSend$_screensThatAreCaptureableDidFindOnenessScreens:
- _objc_msgSend$_screenshotServicesServiceAlertDefinition
- _objc_msgSend$_unregisterForActiveInterfaceOrientationChanges
- _objc_msgSend$arrayWithObject:
- _objc_msgSend$availableRectForFullscreenContent:layoutBounds:bleedToBottom:topBarHeight:bottomBarHeight:userInterfaceIdiom:multipleScreenshots:
- _objc_msgSend$captureAvailableSnapshotsWithOptionsCollection:didFindOnenessScreens:
- _objc_msgSend$currentSession
- _objc_msgSend$initWithServiceName:viewControllerClassName:
- _objc_msgSend$isCarDisplay
- _objc_msgSend$isCarInstrumentsDisplay
- _objc_msgSend$lookupHandlesForDefinition:creatingIfNone:
- _objc_msgSend$mirroredScreen
- _objc_msgSend$rootIdentity
- _objc_msgSend$screenshotBottomMargin:
- _objc_msgSend$screenshotBottomMarginPhone
- _objc_msgSend$screenshotServicesAlertHandle
- _objc_msgSend$setFailureReasonIfImageIsNil:
- _objc_msgSend$setOrientation:
- _objc_msgSend$setWithObject:
- _objc_msgSend$sizeToFit
- _objc_retain_x27
CStrings:
+ "#"
+ "<nil>"
+ "Applying snapshot rendering overrides for: %@"
+ "B16@?0@\"CADisplay\"8"
+ "Disable MDM restriction for VI with internal default"
+ "Draining initial layout group: %@"
+ "Failed to create process identity for bundle identifier: %{private}@"
+ "Failed to lookup remote alert handle"
+ "Invalid condition not satisfying: %@"
+ "No snapshots captured, returning early."
+ "SSEnvironmentDescriptionDisplayIdentityKey"
+ "SSPreferencesHighQualityCaptureEnabled"
+ "SSScreenCapturer.m"
+ "Scheduling env description send for session %@"
+ "ScreenshotServicesRemoteAlert"
+ "ScreenshotsVI_iPad"
+ "Sending env description for session %@: waitedMs=%.1f elementCount=%lu bundleID=%@"
+ "Unable to get screenshot image data from image %@, is PDF Image: %{BOOL}d"
+ "VIV2 disabled on iPad due to Enhanced Siri not enabled"
+ "a"
+ "backlight state changed, %ld"
+ "begin observing, userAgent: %p"
+ "com.apple.ScreenshotServices.disableMDMRestrictionForVI"
+ "delegate != ((void *)0)"
+ "displayId: %@"
+ "enable High Quality preference: %{BOOL}d"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "layout received elementCount=%lu firstBundleID=%@"
+ "orientation changed to %ld, duration=%.2f"
+ "skip enable High Quality preference: %{BOOL}d"
+ "stop observing, userAgent: %p"
+ "timeout (FrontBoard did not deliver initial layout)"
+ "timeout waiting for metadata response from %@"
+ "v16@?0@\"NSString\"8"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "\xc1"
- "\t"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SSActiveInterfaceOrientationObserverDelegate>\""
- "@\"<SSDittoHostViewControllerDelegate>\""
- "@\"<SSRemoteAlertHandleProviderDelegate>\""
- "@\"<SSScreenCapturerDelegate>\""
- "@\"<SSScreenshotAssetManagerBackend>\""
- "@\"<SSScreenshotsWindowDelegate>\""
- "@\"<SSTestingCoordinatorDelegate>\""
- "@\"<SSUIServiceServerDelegate>\""
- "@\"CAFilter\""
- "@\"CARSessionStatus\""
- "@\"FBSDisplayLayoutMonitor\""
- "@\"FBSOpenApplicationService\""
- "@\"FBSServiceFacilityClient\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"PHPhotoLibrary\""
- "@\"RCPEventStreamRecorder\""
- "@\"RCPMovie\""
- "@\"RCPScreenRecorder\""
- "@\"SBSRemoteAlertHandle\""
- "@\"SSActiveInterfaceOrientationObserver\""
- "@\"SSApplicationScreenshotSupplementalDataCapturer\""
- "@\"SSBlurView\""
- "@\"SSChromePlaceholderView\""
- "@\"SSDittoRemoteConnection\""
- "@\"SSEnvironmentDescriptionAppleInternalOptions\""
- "@\"SSHarvestedApplicationDocument\""
- "@\"SSHarvestedApplicationMetadata\""
- "@\"SSImageSurface\""
- "@\"SSScreenshotsWindow\""
- "@\"SSScreenshotsWindowRootViewController\""
- "@\"SSSnapshotter\""
- "@\"SSTestingCoordinator\""
- "@\"SSUIRunPPTServiceRequest\""
- "@\"SSUIServiceClient\""
- "@\"SSUIServiceOptions\""
- "@\"SSUIServiceOptionsAssetMetadata\""
- "@\"SSUIServiceServer\""
- "@\"SSVellumOpacityControl\""
- "@\"UIBarButtonItem\""
- "@\"UIColor\""
- "@\"UIImage\""
- "@\"UIImageView\""
- "@\"UINavigationBar\""
- "@\"UINavigationItem\""
- "@\"UIScreen\""
- "@\"UISlider\""
- "@\"UIStackView\""
- "@\"UIView\""
- "@\"UIViewController\""
- "@\"UIViewPropertyAnimator\""
- "@\"VKCImageAnalysis\""
- "@\"VKImageAnalysisBarButtonItem\""
- "@\"_SSSFlashSuperColorView\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"<BSXPCDecoding>\"16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^B16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@28@0:8@16B24"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16^B24"
- "@36@0:8@16B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8{CGPoint=dd}16@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?"
- "B"
- "B16@0:8"
- "B16@?0@\"UIScreen\"8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"UINavigationBar\"16@\"UINavigationItem\"24"
- "B32@0:8@16@24"
- "BSXPCSecureCoding"
- "CGColor"
- "CGContext"
- "CGImage"
- "CGRectValue"
- "I"
- "I16@0:8"
- "Ignoring defunct car screen %{public}@"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PDFData"
- "PDFPage"
- "PDFVisibleRect"
- "Q"
- "Q16@0:8"
- "SBSRemoteAlertHandleObserver"
- "SBUIActiveOrientationObserver"
- "SSActiveInterfaceOrientationObserverDelegate"
- "SSApplicationScreenshotSupplementalDataCapturer"
- "SSBlurView"
- "SSBlurringFlashView"
- "SSChromeFactory"
- "SSChromeHelper"
- "SSChromePlaceholderView"
- "SSChromePlaceholderViewController"
- "SSDittoHostViewController"
- "SSDittoHostViewControllerDelegate"
- "SSDittoRemoteConnection"
- "SSDocumentUpdateAction"
- "SSEnvironmentDescription"
- "SSEnvironmentElement"
- "SSEnvironmentElementDocumentUpdate"
- "SSEnvironmentElementMetadata"
- "SSEnvironmentElementMetadataUpdate"
- "SSFlashView"
- "SSHarvestedApplicationDocument"
- "SSHarvestedApplicationMetadata"
- "SSImageIdentifierAction"
- "SSImageIdentifierUpdate"
- "SSImageSurface"
- "SSLoggable"
- "SSMainScreenSnapshotter"
- "SSMaterial"
- "SSMetadataUpdateAction"
- "SSOtherScreenSnapshotter"
- "SSPreferences"
- "SSPreheatAction"
- "SSReduceTransparencyFlashView"
- "SSRemoteAlertHandleProvider"
- "SSRemoteViewControllerHostToServiceInterface"
- "SSRemoteViewControllerServiceToHostInterface"
- "SSSAdditions"
- "SSSDismissalContext"
- "SSScreenCaptureAbilityCheck"
- "SSScreenCapturer"
- "SSScreenCapturerPresentationOptions"
- "SSScreenCapturerScreenshotOptions"
- "SSScreenCapturerScreenshotOptionsCollection"
- "SSScreenSnapshot"
- "SSScreenSnapshotter"
- "SSScreenshotAction"
- "SSScreenshotAssetManager"
- "SSScreenshotAssetManagerBackend"
- "SSScreenshotAssetManagerPhotoLibraryBackend"
- "SSScreenshotAssetManagerRegistrationOptions"
- "SSScreenshotMetadataHarvester"
- "SSScreenshotsWindow"
- "SSScreenshotsWindowDelegate"
- "SSScreenshotsWindowRootViewController"
- "SSSnapshotter"
- "SSStatisticsManager"
- "SSTestingCoordinator"
- "SSTestingCoordinatorDelegate"
- "SSUIRunPPTServiceRequest"
- "SSUIService"
- "SSUIServiceClient"
- "SSUIServiceOptions"
- "SSUIServiceOptionsAssetMetadata"
- "SSUIServiceServer"
- "SSUIServiceServerDelegate"
- "SSUIShowScreenshotServiceRequest"
- "SSUIShowScreenshotUIWithImageServiceRequest"
- "SSVellumOpacityControl"
- "SSXPCEncodableRectWrapper"
- "T#,R"
- "T@\"<SSActiveInterfaceOrientationObserverDelegate>\",W,N,V_delegate"
- "T@\"<SSDittoHostViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<SSRemoteAlertHandleProviderDelegate>\",W,N,V_delegate"
- "T@\"<SSScreenCapturerDelegate>\",W,N,V_delegate"
- "T@\"<SSScreenshotsWindowDelegate>\",W,N,V_delegate"
- "T@\"<SSTestingCoordinatorDelegate>\",W,N,V_delegate"
- "T@\"<SSUIServiceServerDelegate>\",W,N,V_delegate"
- "T@\"BSSettings\",R,N"
- "T@\"CAFilter\",R,N"
- "T@\"NSArray\",C,N,V_assetDescription"
- "T@\"NSArray\",C,N,V_contentRects"
- "T@\"NSArray\",C,N,V_harvestedMetadata"
- "T@\"NSArray\",C,N,V_rectsInElement"
- "T@\"NSArray\",R,N,V_elements"
- "T@\"NSData\",C,N,V_PDFData"
- "T@\"NSDate\",&,N,V_date"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,SsetUserActivityTitle:,V_userActivityTitle"
- "T@\"NSString\",C,N,V_applicationBundleID"
- "T@\"NSString\",C,N,V_betaApplicationBundleID"
- "T@\"NSString\",C,N,V_betaApplicationName"
- "T@\"NSString\",C,N,V_environmentDescriptionIdentifier"
- "T@\"NSString\",C,N,V_environmentElementIdentifier"
- "T@\"NSString\",C,N,V_failureReasonIfImageIsNil"
- "T@\"NSString\",C,N,V_imageIdentifier"
- "T@\"NSString\",C,N,V_reasonForNotBeingAbleToTakeScreenshots"
- "T@\"NSString\",C,N,V_sessionIdentifier"
- "T@\"NSString\",C,N,V_testName"
- "T@\"NSString\",C,N,V_userActivityTitle"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSURL\",C,N,V_userActivityURL"
- "T@\"RCPMovie\",&,N,V_recapMovie"
- "T@\"SSEnvironmentDescriptionAppleInternalOptions\",&,N,V_appleInternalOptions"
- "T@\"SSHarvestedApplicationDocument\",&,N,V_document"
- "T@\"SSHarvestedApplicationMetadata\",&,N,V_metadata"
- "T@\"SSImageSurface\",&,N,V_imageSurface"
- "T@\"SSUIRunPPTServiceRequest\",&,N,V_runPPTServiceRequest"
- "T@\"SSUIServiceOptions\",&,N,V_options"
- "T@\"SSUIServiceOptions\",&,N,V_serviceOptions"
- "T@\"SSUIServiceOptionsAssetMetadata\",C,N,V_assetMetadata"
- "T@\"UIColor\",R,N"
- "T@\"UIImage\",&,N,V_image"
- "T@\"UIImage\",&,N,V_preparedImage"
- "T@\"UIImage\",R,N"
- "T@\"UIScreen\",R,N"
- "T@\"UIScreen\",R,N,V_screen"
- "T@\"UIViewController\",&,N,V_managedViewController"
- "T@\"UIWindow\",R,N"
- "T@\"VKCImageAnalysis\",&,V_earlyVIAnalysis"
- "TB,N,V_appearedFullScreen"
- "TB,N,V_canAutosaveToFiles"
- "TB,N,V_canGenerateDocument"
- "TB,N,V_cropUsed"
- "TB,N,V_didShare"
- "TB,N,V_hasOnenessScreen"
- "TB,N,V_isAbleToTakeScreenshots"
- "TB,N,V_markupUsed"
- "TB,N,V_skipShutterSound"
- "TB,N,V_success"
- "TB,N,V_viAvailable"
- "TB,N,V_viUsed"
- "TB,R"
- "TB,R,N"
- "TI,N,V_externalFlashLayerContextID"
- "TQ,N,V_dismissAnimationStyle"
- "TQ,N,V_dismissalType"
- "TQ,N,V_externalFlashLayerRenderID"
- "TQ,N,V_flashStyle"
- "TQ,N,V_numberOfRequiredScreenshots"
- "TQ,N,V_presentationMode"
- "TQ,N,V_saveLocation"
- "TQ,N,V_style"
- "TQ,R"
- "TQ,R,N"
- "T^{__IOSurface=},N,V_backingSurface"
- "T^{__IOSurface=},N,V_hdrBackingSurface"
- "Td,N"
- "Td,N,V_contentAlpha"
- "Td,N,V_imageScale"
- "Td,N,V_scale"
- "Td,R,N"
- "Tq,N,V_PDFPage"
- "Tq,N,V_numberOfScreenshots"
- "Tq,N,V_orientation"
- "Tq,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_PDFVisibleRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGSize=dd},N,V_imagePixelSize"
- "T{CGSize=dd},R,N"
- "T{UIEdgeInsets=dddd},N,V_screenshotsWindowSafeAreaInsets"
- "UIBarPositioningDelegate"
- "UINavigationBarDelegate"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unable to get screenshot image data from image %@"
- "Unknown"
- "Vv16@0:8"
- "^{CGImage=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__IOSurface=}"
- "^{__IOSurface=}16@0:8"
- "_ARKitImageDataFromImage:"
- "_FBSScene"
- "_PDFData"
- "_PDFPage"
- "_PDFVisibleRect"
- "_SSSFlashSuperColorView"
- "_SSScreenCaptureResults"
- "__shouldHostRemoteTextEffectsWindow"
- "_aaBarButtonItem"
- "_activeInterfaceOrientationObserver"
- "_annotationEnabledButton"
- "_appearedFullScreen"
- "_appendSettingsAndSendEvent:block:"
- "_appleInternalOptions"
- "_applicationBundleID"
- "_applicationProxyForCurrentApp"
- "_applicationScreenshotServiceWithPrivateDelegate:"
- "_assetDescription"
- "_assetMetadata"
- "_backdropLayer"
- "_backend"
- "_backingSurface"
- "_backlightNotificationToken"
- "_barItems"
- "_betaApplicationBundleID"
- "_betaApplicationName"
- "_betaFeedbackEnabled:"
- "_blurView"
- "_blurViewRadiusAnimator"
- "_blurViewRadiusAnimatorCompleted"
- "_bundleIDForCurrentApplication"
- "_bundleIdentifier"
- "_callDelegate:"
- "_canAutosaveToFiles"
- "_canBecomeKeyWindow"
- "_canGenerateDocument"
- "_canShowWhileLocked"
- "_captureAndSendDocumentForEnvironmentElement:"
- "_captureAndSendMetadataAndDocumentForEnvironmentDescription:metadataCaptureCompletion:"
- "_captureAndSendMetadataForEnvironmentElement:metadataCapture:sendCompletion:"
- "_captureScreen:withScreenshotOptions:"
- "_carSessionStatus"
- "_cleanupCurrentHandleNotifyDelegate:"
- "_client"
- "_closeItem"
- "_color"
- "_colorView"
- "_completionBlock"
- "_containerStackView"
- "_contentAlpha"
- "_contentRects"
- "_contentRectsForMetadata"
- "_copyIOSurface"
- "_cornerRadius"
- "_crawlView:executingBlock:"
- "_crawlViewController:executingBlock:"
- "_cropUsed"
- "_currentDisplayLayout"
- "_currentUserActivityUUID"
- "_date"
- "_decodedRectsForEncodedRects:"
- "_delayedHandleRunPPTRequest:"
- "_delegate"
- "_deleteItem"
- "_deviceBacklightChanged:"
- "_deviceLockStateChanged:"
- "_didShare"
- "_dismiss"
- "_dismissAnimationStyle"
- "_dismissalType"
- "_dittoRemoteConnection"
- "_document"
- "_doneItem"
- "_earlyVIAnalysis"
- "_elementIdentifier"
- "_elements"
- "_encodableRects"
- "_environmentDescriptionFromImage:"
- "_environmentDescriptionIdentifier"
- "_environmentElementIdentifier"
- "_externalFlashLayerContextID"
- "_externalFlashLayerRenderID"
- "_facilityClient"
- "_failureReasonIfImageIsNil"
- "_fetchUserActivityWithUUID:completionHandler:"
- "_filesAppExistsOnSystem"
- "_filter"
- "_flashStyle"
- "_flashViewClass"
- "_gameHighlightsImageDataFromImage:withOptions:"
- "_gameHighlightsImageDataFromImageData:withOptions:"
- "_grabPDFRepresentationForIdentifier:withCallback:"
- "_grabUserActivityTitleWithCallback:"
- "_handle"
- "_handleHasAnySSUIServiceEntitlement:"
- "_harvestedMetadata"
- "_hasKeyboardFocus"
- "_hasOnenessScreen"
- "_hdrBackingSurface"
- "_hostViewControllerIfExists"
- "_identifier"
- "_image"
- "_imageIdentifier"
- "_imagePixelSize"
- "_imageScale"
- "_imageSurface"
- "_initWithFilterType:color:"
- "_initWithSDRIOSurface:HDRIOSurface:scale:orientation:"
- "_initializeBarButtonItems"
- "_isAbleToTakeScreenshots"
- "_isCompletingFlashWithNewTimingParameters"
- "_isSecure"
- "_lastActiveInterfaceOrientation"
- "_lastScreenshotTime"
- "_lastUsedPresentationMode"
- "_layoutMonitor"
- "_layoutTopBar"
- "_leadingImageView"
- "_leftImageView"
- "_lockNotificationToken"
- "_managedNavigationItem"
- "_managedViewController"
- "_markupUsed"
- "_maxTrackView"
- "_metadata"
- "_metadataCapturer"
- "_metadataIdentifierBlocklist"
- "_minTrackView"
- "_notifyQueue"
- "_numberOfRequiredScreenshots"
- "_numberOfScreenshots"
- "_observeActiveInterfaceOrientationChangeToOrientation:withDuration:"
- "_oldCompletionBlock"
- "_opacityControl"
- "_opacityItem"
- "_opacityView"
- "_openAppService"
- "_openApplicationService"
- "_options"
- "_orientation"
- "_photoLibrary"
- "_placeholderView"
- "_preferredStatusBarVisibility"
- "_preheatAndTakeScreenshotIfPossibleWithOptionsCollection:presentationOptions:appleInternalOptions:"
- "_prepareRemoteViewControllerWithCompletionHandler:"
- "_preparedImage"
- "_presentationMode"
- "_reasonForNotBeingAbleToTakeScreenshots"
- "_recap"
- "_recapMovie"
- "_recapSnapshotter"
- "_rect"
- "_rectsInElement"
- "_redoItem"
- "_registerEntryWithImage:options:retry:identifierHandler:"
- "_registerForActiveInterfaceOrientationChanges"
- "_rightImageView"
- "_root"
- "_runCompletionBlockIfAppropriate"
- "_runPPTNamed:numberOfRequiredScreenshots:"
- "_runPPTServiceRequest"
- "_saveImageToPhotoLibrary:environmentDescription:"
- "_saveLocation"
- "_sbUIUserAgent"
- "_scale"
- "_screen"
- "_screenToScreenshotOptions"
- "_screensThatAreCaptureableDidFindOnenessScreens:"
- "_screenshotServiceForWindowScene:wantsPrivateDelegate:"
- "_screenshotServiceIfPresent"
- "_screenshotServicesDelegateWithIdentifier:"
- "_screenshotServicesServiceAlertDefinition"
- "_screenshotServicesServiceBundle"
- "_screenshotWasTakenOverBetaApp"
- "_screenshotWindowWasDismissed"
- "_screenshotWindowWillBeDisplayed"
- "_screenshotsWindowSafeAreaInsets"
- "_sendAction:"
- "_sendAction:completion:"
- "_sendEnvironmentDescription:savingImageToPhotos:withCompletion:"
- "_sendEnvironmentDescription:withCompletion:"
- "_sendEvent:block:"
- "_sendRequestForEnvironmentElement:info:completionBlock:"
- "_serviceOptions"
- "_serviceProxy"
- "_serviceWindow"
- "_sessionIdentifier"
- "_setCornerRadius:"
- "_setFlexible:"
- "_setIgnoreAppSupportedOrientations:"
- "_setOverrideUserInterfaceStyle:"
- "_setRotatableViewOrientation:duration:"
- "_setRotatableViewOrientation:duration:force:"
- "_setWindowControlsStatusBarOrientation:"
- "_shareItem"
- "_shouldAnimatePropertyWithKey:"
- "_shouldAutorotateToInterfaceOrientation:"
- "_shouldControlAutorotation"
- "_skipShutterSound"
- "_slider"
- "_snapshotter"
- "_ss_vi2Enabled"
- "_sss_cropItemWithTarget:action:"
- "_sss_redoItemWithTarget:action:"
- "_sss_shareItemWithTarget:action:"
- "_sss_trashItemWithTarget:action:"
- "_sss_undoItemWithTarget:action:"
- "_statisticsEnabled"
- "_style"
- "_success"
- "_superColorView"
- "_superColorViewBackgroundColorAnimatorCompleted"
- "_superColorViewOpacityAnimator"
- "_takeScreenshotWithOptionsCollection:serviceOptions:presentationOptions:appleInternalOptions:"
- "_testName"
- "_testingCoordinator"
- "_topBar"
- "_topBarBackground"
- "_topBarSeparatorLine"
- "_trailingImageView"
- "_triggerTypeForPresentationMode:"
- "_uiServiceServer"
- "_undoItem"
- "_undoRedoSpacerItem"
- "_unregisterForActiveInterfaceOrientationChanges"
- "_updateBackgroundColor"
- "_updateBarButtonItemPositionsAnimated:"
- "_userActivityTitle"
- "_userActivityURL"
- "_viAvailable"
- "_viUsed"
- "abilityCheck"
- "absoluteString"
- "absoluteURL"
- "activate"
- "activateConstraints:"
- "activateRemoteViewControllerIfAppropriate"
- "activateWithContext:"
- "activationState"
- "activeInterfaceOrientation"
- "activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:"
- "activeInterfaceOrientationObserver:observedChangeToInterfaceOrientation:withDuration:"
- "activeInterfaceOrientationWillChangeToOrientation:"
- "addActiveInterfaceOrientationObserver:"
- "addAnimations:"
- "addChildViewController:"
- "addCompletion:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "analysisButtonWithTarget:action:mode:"
- "animateWithDuration:delay:options:animations:completion:"
- "animationStyleString"
- "appState"
- "appearedFullScreen"
- "appendFormat:"
- "appendString:"
- "appleInternalOptions"
- "applicationBundleID"
- "applicationProxyForIdentifier:"
- "applicationType"
- "applicationWithBundleIdentifier:"
- "applyToView:"
- "array"
- "arrayByAddingObject:"
- "arrayWithArray:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assetDescription"
- "assetMetadata"
- "autorelease"
- "availableRectForFullscreenContent:layoutBounds:bleedToBottom:topBarHeight:bottomBarHeight:userInterfaceIdiom:multipleScreenshots:"
- "backend"
- "backgroundBlurEffectStyle"
- "backingSurface"
- "barButtonItemsLeftOfOpacitySlider"
- "barSeparatorColor"
- "barSeparatorSize"
- "becomeFirstResponder"
- "beginObserving"
- "betaApplicationBundleID"
- "betaApplicationName"
- "blackColor"
- "blurRadius"
- "boolForKey:"
- "boolValue"
- "bounds"
- "bringSubviewToFront:"
- "bsSettings"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "cStringUsingEncoding:"
- "canAutosaveToFiles"
- "canGenerateDocument"
- "canGenerateDocumentForIdentifier:"
- "canSendResponse"
- "captureAvailableSnapshotsWithOptionsCollection:didFindOnenessScreens:"
- "captureDocumentForEnvironmentElement:withCompletionBlock:"
- "captureMetadataForEnvironmentElement:withCompletionBlock:"
- "carPlaySettingsChanged"
- "centerYAnchor"
- "changeRequestForAsset:"
- "childViewControllers"
- "class"
- "clearColor"
- "closeBarButtonItem"
- "code"
- "coder"
- "coderWithMessage:"
- "color"
- "colorAlpha"
- "colorWithAlphaComponent:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "com.apple.backboardd.backlight.changed"
- "componentsJoinedByString:"
- "configurationForDefaultMainDisplayMonitor"
- "configurationWithTextStyle:scale:"
- "configureNavigationBarAppearance:"
- "conformsToProtocol:"
- "connectedScenes"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "containsObject:"
- "contentAlpha"
- "contentRects"
- "contentSwitcherPadding"
- "controlPoint1"
- "controlPoint2"
- "convertRect:fromCoordinateSpace:"
- "convertRect:fromView:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countIndicatorOffset"
- "createFixedSpaceBarButtonItemWithWidth:"
- "createMessage"
- "creationRequestForAssetFromImageData:options:"
- "cropHandle"
- "cropsCornerColor"
- "cropsCornerContentPadding"
- "cropsCornerEdgeLength"
- "cropsCornerLength"
- "cropsCornerLengthLong"
- "cropsCornerLineWidth"
- "cropsCornerWidth"
- "cropsHandleOutset"
- "currentApplicationBundleID"
- "currentDevice"
- "currentLayout"
- "currentSession"
- "currentUser"
- "d"
- "d16@0:8"
- "d24@0:8Q16"
- "d24@0:8q16"
- "d32@0:8@16@24"
- "data"
- "date"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeCGRectForKey:"
- "decodeCGSizeForKey:"
- "decodeCollectionOfClass:containingClass:forKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeUInt64ForKey:"
- "decodeXPCObjectOfType:forKey:"
- "defaultBarButtonSpacing"
- "defaultBarButtonWidth"
- "defaultFormat"
- "defaultManager"
- "defaultShellEndpoint"
- "delegate"
- "deleteAssets:"
- "description"
- "device lock state changed, %llu"
- "deviceIsEligibleForVI"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didAccidentallyDraw"
- "didChangeOpacityOnFullPage"
- "didChangeOpacityOnNormalScreenshot"
- "didCopyDeleteScreenshots"
- "didCropInFullPageMode"
- "didCropInNormalMode"
- "didDeleteScreenshotDueToVI"
- "didDeleteScreenshots"
- "didMoveToParentViewController:"
- "didRenameScreenshot"
- "didSaveFullPagePDFToFiles"
- "didSaveImageToFiles"
- "didSaveImageToPhotos"
- "didSaveImageToQuickNote"
- "didSaveMixedAllToFiles"
- "didSaveMixedToPhotosAndFiles"
- "didSaveMixedToQuickNoteAndFiles"
- "didSavePDFImageToPhotos"
- "didShare"
- "didShareFullPageMixedScreenshots"
- "didShareFullPageScreenshotAsAutomaticImage"
- "didShareFullPageScreenshotAsAutomaticPDF"
- "didShareFullPageScreenshotAsImage"
- "didShareFullPageScreenshotAsPDF"
- "didShareScreenMultipleScreenshots"
- "didShareScreenSingleScreenshots"
- "didSubmitFeedbackWithAnnotationCount:"
- "didTapBetaFeedbackButton"
- "didTapFullPageSegment"
- "disconnect"
- "dismiss"
- "dismissAnimationStyle"
- "dismissScreenshotExperience"
- "dismissViewControllerAnimated:completion:"
- "dismissalString"
- "displayConfiguration"
- "displayGamut"
- "displayScale"
- "document"
- "domain"
- "doubleValue"
- "drewStrokes:"
- "earlyVIAnalysis"
- "effectWithStyle:"
- "effectivePresentationMode"
- "effectiveUserInterfaceLayoutDirection"
- "elementIdentifier"
- "elements"
- "encodeBool:forKey:"
- "encodeCGRect:forKey:"
- "encodeCGSize:forKey:"
- "encodeCollection:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeRects:inDictionary:forKey:"
- "encodeToXPC"
- "encodeUInt64:forKey:"
- "encodeWithBSXPCCoder:"
- "encodeWithCoder:"
- "encodeXPCObject:forKey:"
- "encodedRectsInDictionary:forKey:"
- "entitlement"
- "enumerateObjectsUsingBlock:"
- "environmentDescriptionIdentifier"
- "environmentElementIdentifier"
- "error"
- "exceptionWithName:reason:userInfo:"
- "expectedAnimationDurationForStyle:"
- "expirationDate"
- "exportedInterface"
- "externalFlashLayerContextID"
- "externalFlashLayerRenderID"
- "failureReasonIfImageIsNil"
- "fetchAssetsWithLocalIdentifiers:options:"
- "fetchPDFRepresentationWithCompletion:"
- "fileExistsAtPath:"
- "fileFormatIsHDRSettingsChanged"
- "fileURLWithPath:"
- "filename"
- "filter"
- "filterWithType:"
- "finishedIPTest:"
- "firstObject"
- "fixedSpaceItemOfWidth:"
- "flagForSetting:"
- "flashStyle"
- "flashViewForStyle:"
- "flashWithCompletion:"
- "floatValue"
- "frame"
- "fullScreenPreviewsSettingsChanged"
- "fullscreenExperienceHadCropEvent"
- "getRed:green:blue:alpha:"
- "getRotationContentSettings:forWindow:"
- "handleRunPPTRequest:"
- "handleStatusBarChangeFromHeight:toHeight:"
- "harvestScreenshotMetadataAndRespondToAction:"
- "harvestedMetadata"
- "hasEntitlement:"
- "hasKeyboardFocus"
- "hasOnenessScreen"
- "hasRemoteViewController"
- "hash"
- "hdrBackingSurface"
- "hdrSurface"
- "heightAnchor"
- "hitTest:withEvent:"
- "i16@0:8"
- "i28@0:8@16B24"
- "identifier"
- "identity"
- "image"
- "imageDescription"
- "imageForPreviouslyRegisteredIdentifier:imageHandler:"
- "imageIdentifier"
- "imageModificationData"
- "imageOrientation"
- "imagePixelSize"
- "imagePointSize"
- "imageScale"
- "imageSurface"
- "imageWithActions:"
- "imageWithCGImage:scale:orientation:"
- "imageWithData:"
- "imageWithPreviouslyRegisteredIdentifier:withAccessBlock:"
- "imageWithRenderingMode:"
- "imageWithSymbolConfiguration:"
- "info"
- "init"
- "initForAppWithIdentifier:"
- "initWithArrangedSubviews:"
- "initWithBSXPCCoder:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithCGImage:scale:orientation:"
- "initWithCalendarIdentifier:"
- "initWithCoder:"
- "initWithConfigurator:"
- "initWithContentEditingInput:withOptions:"
- "initWithControlPoint1:controlPoint2:"
- "initWithCustomView:"
- "initWithDelegate:"
- "initWithDisplayLayoutElement:"
- "initWithDuration:timingParameters:"
- "initWithEventStream:snapshots:"
- "initWithFormatIdentifier:formatVersion:data:"
- "initWithFrame:"
- "initWithIdentifier:queue:"
- "initWithImage:"
- "initWithImage:menu:"
- "initWithImage:style:target:action:"
- "initWithInfo:timeout:forResponseOnQueue:withHandler:"
- "initWithMessagePacker:"
- "initWithNibName:bundle:"
- "initWithOptions:"
- "initWithPhotoLibraryURL:"
- "initWithScreen:"
- "initWithServiceName:viewControllerClassName:"
- "initWithSize:"
- "initWithSize:format:"
- "initWithSuiteName:"
- "initWithType:"
- "initWithXPC:"
- "integerValue"
- "interfaceWithProtocol:"
- "intrinsicContentSize"
- "invalidate"
- "isAbleToTakeScreenshots"
- "isActive"
- "isAppLauncher"
- "isBetaApp"
- "isCarDisplay"
- "isCarInstrumentsDisplay"
- "isContinuityDisplay"
- "isEqual:"
- "isEqualToString:"
- "isHighDynamicRange"
- "isInstalled"
- "isKindOfClass:"
- "isLocked"
- "isLoginUser"
- "isMemberOfClass:"
- "isProactiveFeedbackEnabledForInstalledVersion"
- "isProxy"
- "isScreenShotAllowed"
- "isSharedIPad"
- "isValid"
- "itemID"
- "itemName"
- "jpegImageDataFromImage:withProperties:"
- "keyWindow"
- "layer"
- "layerClass"
- "layoutIfNeeded"
- "layoutSubviews"
- "leadingAnchor"
- "length"
- "librarySpecificFetchOptions"
- "localIdentifier"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "localizedStringFromNumber:numberStyle:"
- "logTotalAnnotations:"
- "loggableDescription"
- "lookupHandlesForDefinition:creatingIfNone:"
- "mainBundle"
- "mainScreen"
- "makeKeyWindow"
- "managedViewController"
- "metadata"
- "mirroredScreen"
- "monitorWithConfiguration:"
- "mutableCopy"
- "navigationBar:didPopItem:"
- "navigationBar:didPushItem:"
- "navigationBar:shouldPopItem:"
- "navigationBar:shouldPushItem:"
- "navigationBarNSToolbarSection:"
- "noteDidReceiveMessage:withType:fromClient:"
- "numberOfRequiredScreenshots"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:inDomain:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "openApplication:withOptions:completion:"
- "options"
- "optionsWithDictionary:"
- "orientation"
- "payload"
- "performChanges:completionHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "photoLibrary"
- "pid"
- "pipDragEndedSuccessfully"
- "pipExpanded"
- "pipSlidOffscreenDueToTimeout"
- "placeholderForCreatedAsset"
- "playScreenshotSound"
- "popNavigationItemAnimated:"
- "positionForBar:"
- "potentialEDRHeadroom"
- "preferredStatusBarStyle"
- "preferredWidth"
- "preheat"
- "preheatDittoProcess"
- "preheatWithPresentationOptions:"
- "prepare"
- "preparedImage"
- "presentationMode"
- "presentedViewController"
- "presentingViewController"
- "privateDelegate"
- "processHandle"
- "purpleColor"
- "pushNavigationItem:animated:"
- "q16@0:8"
- "q24@0:8@\"<UIBarPositioning>\"16"
- "q24@0:8@\"UINavigationBar\"16"
- "q24@0:8@16"
- "queueWithDispatchQueue:"
- "reasonForNotBeingAbleToTakeScreenshots"
- "recapMovie"
- "recordEditsToPersistable:inTransition:withCompletionBlock:"
- "recordEditsToPersistableForPDF:withCompletionBlock:"
- "recordPersistableToTemporaryLocation:withCompletionBlock:"
- "recorderWithConfiguration:"
- "rect"
- "rectsInElement"
- "registerEntryWithImage:options:identifierHandler:"
- "registerImageForPersistable:options:withRegistrationBlock:"
- "registerObserver:"
- "registrationOptions"
- "release"
- "remoteAlertHandle:didInvalidateWithError:"
- "remoteAlertHandleDidActivate:"
- "remoteAlertHandleDidDeactivate:"
- "remoteAlertHandleProvider:didInvalidateWithError:"
- "remoteAlertHandleProviderDidActivate:"
- "remoteAlertHandleProviderDidDeactivate:"
- "remoteViewControllerDisconnectedFromHostViewController:withError:"
- "remoteViewControllerOfHostViewControllerHasDismissedScreenshots:"
- "removeActiveInterfaceOrientationObserver:"
- "removeEntryWithIdentifier:completionHandler:"
- "removeFromParentViewController"
- "removeFromSuperview"
- "removeObjectForKey:"
- "removePDF"
- "removePersistable:deleteOptions:withCompletionBlock:"
- "renderedContentURL"
- "requestContentEditingInputWithOptions:completionHandler:"
- "requestImageForAsset:targetSize:contentMode:options:resultHandler:"
- "requestImageInTransition:withBlock:"
- "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
- "resetBackend"
- "respondsToSelector:"
- "responseWithInfo:"
- "retain"
- "retainCount"
- "rootIdentity"
- "rootViewController"
- "roundedCropHandleThickness"
- "roundedCropsCornerRadius"
- "roundedCropsLength"
- "runPPTServiceRequest"
- "safeAreaInsets"
- "safeAreaInsetsDidChange"
- "saveImageDataToTemporaryLocation:persistable:completionHandler:"
- "saveImageDataToTemporaryLocation:withName:imageDescription:completionHandler:"
- "saveImageToTemporaryLocation:withName:imageDescription:completionHandler:"
- "saveLocation"
- "savePDFWithBlock:"
- "screen"
- "screenCapturer:didCaptureScreenshotsOfScreens:"
- "screens"
- "screenshotBottomMargin:"
- "screenshotBottomMarginPhone"
- "screenshotContentFrame"
- "screenshotExperienceHasDismissed"
- "screenshotGestureTriggered:"
- "screenshotGestureTriggeredWhileAnotherScreenshotWasShowing:"
- "screenshotOptionsForScreen:"
- "screenshotService:generatePDFRepresentationWithCompletion:"
- "screenshotServiceWithIdentifier:"
- "screenshotServicesAlertHandle"
- "screenshotTopBottomMarginPad"
- "screenshotTopMargin:"
- "screenshotTopMarginPhone"
- "screenshotWindowWasDismissed"
- "screenshotWindowWillBeDisplayed"
- "screenshotsWindow"
- "screenshotsWindowSafeAreaInsets"
- "sdrSurface"
- "secondaryLabelColor"
- "self"
- "sendDismissalEventWithContext:"
- "sendDittoProcessDocumentUpdate:"
- "sendDittoProcessEnvironmentDescription:completion:"
- "sendDittoProcessImageIdentifierUpdate:"
- "sendDittoProcessMetadataUpdate:completion:"
- "sendDittoProcessPreheatRequestWithPresentationMode:completion:"
- "sendMessage:withType:"
- "sendMessage:withType:replyHandler:waitForReply:timeout:"
- "sendReplyMessageWithPacker:"
- "sendRequest:withCompletion:"
- "sendResponse:"
- "sendResponseForAction:withObject:forKey:"
- "separatorColor"
- "separatorView"
- "server:handleRequest:withCompletion:"
- "serviceOptions"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "serviceWithDefaultShellEndpoint"
- "sessionIdentifier"
- "set"
- "setAccessibilityDescription:"
- "setAdjustmentData:"
- "setAlignment:"
- "setAllowsGroupOpacity:"
- "setAlpha:"
- "setAppearedFullScreen:"
- "setAppleInternalOptions:"
- "setApplicationBundleID:"
- "setAssetDescription:"
- "setAssetMetadata:"
- "setAxis:"
- "setBackend:"
- "setBackgroundColor:"
- "setBackgroundEffects:"
- "setBackgroundImage:forBarMetrics:"
- "setBackingSurface:"
- "setBarTintColor:"
- "setBetaApplicationBundleID:"
- "setBetaApplicationName:"
- "setBlurRadius:"
- "setBool:forKey:"
- "setBorderColor:"
- "setBorderWidth:"
- "setCalendar:"
- "setCalloutQueue:"
- "setCanAutosaveToFiles:"
- "setCanGenerateDocument:"
- "setCenter:"
- "setCompositingFilter:"
- "setContentAlpha:"
- "setContentEditingOutput:"
- "setContentRects:"
- "setCornerRadius:"
- "setCropUsed:"
- "setDate:"
- "setDateFormat:"
- "setDebugElements:"
- "setDelegate:"
- "setDeliveryMode:"
- "setDeviceUsagePageArray:"
- "setDidShare:"
- "setDisableUpdateMask:"
- "setDismissAnimationStyle:"
- "setDismissalType:"
- "setDocument:"
- "setEarlyVIAnalysis:"
- "setEnabled:"
- "setEndpoint:"
- "setEnvironmentDescriptionIdentifier:"
- "setEnvironmentElementIdentifier:"
- "setExternalFlashLayerContextID:"
- "setExternalFlashLayerRenderID:"
- "setFailureReasonIfImageIsNil:"
- "setFilters:"
- "setFlag:forSetting:"
- "setFlashStyle:"
- "setFrame:"
- "setHarvestedMetadata:"
- "setHasOnenessScreen:"
- "setHdrBackingSurface:"
- "setHidden:"
- "setIdentifier:"
- "setImage:"
- "setImageIdentifier:"
- "setImagePixelSize:"
- "setImageScale:"
- "setImageSurface:"
- "setImportedByBundleIdentifier:"
- "setInteger:forKey:"
- "setIsAbleToTakeScreenshots:"
- "setLeftBarButtonItems:animated:"
- "setLocale:"
- "setManagedViewController:"
- "setMarkupUsed:"
- "setMaxDuration:"
- "setMaxStreamDuration:"
- "setMaximumTrackTintColor:"
- "setMaximumValue:"
- "setMetadata:"
- "setMinimumTrackTintColor:"
- "setMinimumValue:"
- "setModalPresentationStyle:"
- "setName:"
- "setNeedsLayout"
- "setNumberOfRequiredScreenshots:"
- "setNumberOfScreenshots:"
- "setObject:forKey:"
- "setObject:forKey:inDomain:"
- "setObject:forKeyedSubscript:"
- "setObject:forSetting:"
- "setOpaque:"
- "setOptions:"
- "setOrientation:"
- "setOverrideUserInterfaceStyle:"
- "setPDFData:"
- "setPDFPage:"
- "setPDFVisibleRect:"
- "setPreferHEICForRenderedImages:"
- "setPrefersEmbeddedDisplayPresentation:"
- "setPreparedImage:"
- "setPresentationMode:"
- "setReasonForNotBeingAbleToTakeScreenshots:"
- "setRecapMovie:"
- "setRect:"
- "setRectsInElement:"
- "setResizeMode:"
- "setRightBarButtonItems:animated:"
- "setRootViewController:"
- "setRunPPTServiceRequest:"
- "setSaveLocation:"
- "setScale:"
- "setScreenshotOptions:forScreen:"
- "setScreenshotsWindowSafeAreaInsets:"
- "setServiceOptions:"
- "setServiceQuality:"
- "setSessionIdentifier:"
- "setShadowImage:"
- "setShouldCreateScreenshot:"
- "setShowsLargeContentViewer:"
- "setSkipShutterSound:"
- "setSpacing:"
- "setStyle:"
- "setSuccess:"
- "setSynchronous:"
- "setTestName:"
- "setThumbImage:forState:"
- "setTintColor:"
- "setTitle:"
- "setTitleTextAttributes:"
- "setTitleView:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setTranslucent:"
- "setUseRecoverableStagingDirectory:"
- "setUserActivityTitle:"
- "setUserActivityURL:"
- "setUserInteractionEnabled:"
- "setValue:"
- "setValue:forKey:"
- "setValue:forKeyPath:"
- "setViAvailable:"
- "setViUsed:"
- "setWidth:"
- "setWindowLevel:"
- "setWithObject:"
- "setWithObjects:"
- "settingsForDocumentCapture:elementIdentifier:"
- "sharedApplication"
- "sharedAssetManager"
- "sharedConnection"
- "sharedManager"
- "sharedStatisticsManager"
- "shorterLoggableString"
- "shouldUseScreenCapturerForScreenshots"
- "showScreenshotUI"
- "showScreenshotUIForImage:options:"
- "showScreenshotUIForImage:options:withCompletion:"
- "size"
- "sizeThatFits:"
- "sizeToFit"
- "skipShutterSound"
- "snapshotWithImage:fromScreen:"
- "snapshots"
- "snapshotterForScreen:"
- "ss_CGImageBacked"
- "ss_cgImageBackedImageFromImageSurface:"
- "ss_dataWithFileFormat:addProperties:imageDescription:"
- "ss_hdrSurfaceCGImage"
- "ss_heicDataWithImageDescription:"
- "ss_imageDataWithDataType:sdrImage:hdrImage:properties:imageDescription:"
- "ss_imageFromImageSurface:"
- "ss_imageProperties"
- "ss_imageSurfaceFromImage"
- "ss_ioSurfaceImageData"
- "ss_isHDRImage"
- "ss_isHEICImageData:"
- "ss_pngDataWithImageDescription:"
- "ss_sdrSurfaceCGImage"
- "standardUserDefaults"
- "startAnimationAfterDelay:"
- "startRecap"
- "startRecording"
- "startedIPTest:"
- "statusBarStyle"
- "statusBarVisibilityForTraitCollection:isPortrait:"
- "stopObserving"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "style"
- "substringToIndex:"
- "subviews"
- "success"
- "superclass"
- "supportedAnalysisTypes"
- "supportedInterfaceOrientations"
- "supportsBSXPCSecureCoding"
- "supportsMetadataCapture"
- "supportsSecureCoding"
- "systemImageNamed:"
- "systemPhotoLibraryURL"
- "takeElementsFromDisplayLayout:"
- "takeScreenshot"
- "takeScreenshotWithOptions:"
- "takeScreenshotWithOptionsCollection:presentationOptions:"
- "takeScreenshotWithPresentationOptions:"
- "tearDownScreenshotExperience"
- "testName"
- "testingCoordinator:requestsTakingScreenshotForRunPPTRequest:"
- "timeIntervalSince1970"
- "tintColorDidChange"
- "title"
- "topBarHeight"
- "topItem"
- "trailingAnchor"
- "traitCollection"
- "traitCollectionDidChange:"
- "typeWithIdentifier:"
- "unregisterObserver:"
- "unsignedIntegerValue"
- "updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:"
- "userActivityTitle"
- "userActivityURL"
- "userInitiated"
- "userInterfaceIdiom"
- "userInterfaceStyle"
- "v16@0:8"
- "v16@?0@\"UIScreen\"8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"<BSXPCEncoding>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"SBSRemoteAlertHandle\"16"
- "v24@0:8@\"SSDittoHostViewController\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{__IOSurface=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"NSString\"16@?<v@?@\"UIImage\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
- "v32@0:8@\"SSDittoHostViewController\"16@\"NSError\"24"
- "v32@0:8@\"SSTestingCoordinator\"16@\"SSUIRunPPTServiceRequest\"24"
- "v32@0:8@\"UINavigationBar\"16@\"UINavigationItem\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@?24"
- "v32@0:8^{?=BBBBBdi}16@24"
- "v32@0:8d16d24"
- "v32@0:8q16d24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"SSActiveInterfaceOrientationObserver\"16q24d32"
- "v40@0:8@\"SSUIServiceServer\"16@\"SSUIServiceRequest\"24@?<v@?>32"
- "v40@0:8@\"UIImage\"16@\"SSScreenshotAssetManagerRegistrationOptions\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@16:24Q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24d32"
- "v40@0:8q16d24q32"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSURL\"@\"NSError\">40"
- "v48@0:8@\"UIImage\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSURL\"@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"SSScreenshotAssetManagerRegistrationOptions\"40@\"NSString\"48@?<v@?B@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "value"
- "valueForKey:"
- "valueForKeyPath:"
- "valueWithCGRect:"
- "vellumOpacitySliderTrack"
- "vellumOpacitySliderValueImage"
- "view"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewIfLoaded"
- "viewServiceDidTerminateWithError:"
- "visiblePeripheralFrame"
- "webpageURL"
- "whiteColor"
- "widthAnchor"
- "widthForContentSwitcher:forView:"
- "widthForOpacityControlInView:withContentSwitcher:"
- "willMoveToParentViewController:"
- "window"
- "writeToURL:atomically:"
- "writeToURL:options:error:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}112@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48B80d84d92q100B108"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"
- "\xb1"

```
