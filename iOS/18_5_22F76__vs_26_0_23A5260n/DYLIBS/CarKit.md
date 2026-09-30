## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-606.23.0.0.0
-  __TEXT.__text: 0x4751c
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x4f0c
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x481d
-  __TEXT.__gcc_except_tab: 0x9ec
-  __TEXT.__oslogstring: 0x4ee3
+733.2.0.0.0
+  __TEXT.__text: 0x531e0
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_methlist: 0x591c
+  __TEXT.__const: 0x38a
+  __TEXT.__cstring: 0x5101
+  __TEXT.__oslogstring: 0x5ab8
+  __TEXT.__gcc_except_tab: 0xa44
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__unwind_info: 0x1478
-  __TEXT.__objc_classname: 0x9f3
-  __TEXT.__objc_methname: 0xddec
-  __TEXT.__objc_methtype: 0x1f82
-  __TEXT.__objc_stubs: 0x82a0
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x1c08
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__swift5_typeref: 0x3e
+  __TEXT.__constg_swiftt: 0x58
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x9
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x1730
+  __TEXT.__objc_classname: 0xa6b
+  __TEXT.__objc_methname: 0xf9c7
+  __TEXT.__objc_methtype: 0x2306
+  __TEXT.__objc_stubs: 0x8f00
+  __DATA_CONST.__got: 0x760
+  __DATA_CONST.__const: 0x1e90
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d08
-  __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x1440
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0xcdc0
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0xf28
-  __DATA.__bss: 0x398
-  __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_CONST.__objc_selrefs: 0x3238
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__const: 0x1640
+  __AUTH_CONST.__cfstring: 0x5460
+  __AUTH_CONST.__objc_const: 0xe448
+  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0xf20
+  __AUTH.__data: 0x30
+  __DATA.__objc_ivar: 0x6b0
+  __DATA.__data: 0xfa0
+  __DATA.__bss: 0x4d0
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92A591F2-0FE4-3929-BF4A-AD6375AD218B
-  Functions: 2218
-  Symbols:   7834
-  CStrings:  4261
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 5B764175-9984-3210-9647-8A031465F9DA
+  Functions: 2576
+  Symbols:   8668
+  CStrings:  4757
 
Symbols:
+ +[CARPrototypePref liveActivitiesDisabled]
+ +[CARPrototypePref liveActivitiesDisabled].cold.1
+ +[CRCarPlayCapabilities _newCapabilitiesFromGlobalDomainWithIdentifier:]
+ +[CRCarPlayCapabilities _newCapabilitiesFromGlobalDomainWithIdentifier:].cold.1
+ +[CRCarPlayCapabilities _newCapabilitiesFromGlobalDomainWithIdentifier:].cold.2
+ +[CRCarPlayCapabilities fetchCarCapabilitiesWithIdentifier:]
+ +[CRCarPlayCapabilities fetchCarCapabilitiesWithIdentifier:].cold.1
+ +[CRCarPlayPreferences hasShownEditWidgetsNotification]
+ +[CRCarPlayPreferences setHasShownEditWidgetsNotification:]
+ +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:]
+ +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:].cold.1
+ +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:].cold.2
+ +[CROEMPunchThroughsAppData supportsSecureCoding]
+ +[CRScreenScaleHeuristics scaledDisplays:withDisplayScaling:reply:]
+ +[CRSubtitleSettings defaultSettings]
+ +[CRSubtitleSettings supportsSecureCoding]
+ -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:]
+ -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:].cold.1
+ -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:].cold.2
+ -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:].cold.3
+ -[CARScreenInfo initWithPropertySupplier:screenType:carCapabilities:]
+ -[CARScreenInfo setZoomFactor:]
+ -[CARScreenInfo zoomFactor]
+ -[CARScreenInfo(CRDisplayScaling) allowedDisplayScaleModes]
+ -[CARScreenInfo(CRDisplayScaling) canvasPixelSizeForDisplayScaleMode:]
+ -[CARScreenInfo(CRDisplayScaling) defaultDisplayMode]
+ -[CARScreenInfo(CRDisplayScaling) displayScaleModesForCanvasPixelSize:]
+ -[CARSession _handleEndpointDescriptionChanged]
+ -[CARSession _handleIsPlayingVideoFromApp:]
+ -[CARSession cachedVideoPlaybackAvailable]
+ -[CARSession sendStopSessionWithReason:]
+ -[CARSession setCachedVideoPlaybackAvailable:]
+ -[CARSession setCanvasOverrideSize:forScreenID:]
+ -[CARSession setCanvasOverrideSize:forScreenID:].cold.1
+ -[CARSession videoPlaybackAvailable]
+ -[CARSession videoPlaybackAvailable].cold.1
+ -[CARSessionConfiguration supportedStopSessionDisconnectReasons]
+ -[CARSessionConfiguration supportsFileTransfer]
+ -[CARSessionConfiguration supportsStopSessionDisconnectForThisDrive]
+ -[CARSessionConfiguration supportsStopSession]
+ -[CARSessionConfiguration videoPlaybackSupported]
+ -[CARSessionRequestHost initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:]
+ -[CARSessionRequestHost isRemoteDeviceConnected]
+ -[CARSessionRequestHost setRemoteDeviceConnected:]
+ -[CRCarPlayAppDeclaration setSupportsAutomakerAppService:]
+ -[CRCarPlayAppDeclaration setSupportsVideo:]
+ -[CRCarPlayAppDeclaration supportsAutomakerAppService]
+ -[CRCarPlayAppDeclaration supportsVideo]
+ -[CRCarPlayAppPolicy isSessionDependentPolicy]
+ -[CRCarPlayAppPolicy setSessionDependentPolicy:]
+ -[CRCarPlayAppPolicyEvaluator _applicationCategoryForAppDeclaration:policy:].cold.1
+ -[CRCarPlayAppPolicyEvaluator _automakerAppServiceContainsAppDeclaration:]
+ -[CRCarPlayAppPolicyEvaluator _hideAppIfPunchThroughExistsForBundleIdentifier:withPunchThroughsAppData:andAppPolicy:]
+ -[CRCarPlayAppPolicyEvaluator _hideAppIfPunchThroughExistsForBundleIdentifier:withVerifiedPunchThroughs:andAppPolicy:]
+ -[CRCarPlayAppPolicyEvaluator _retrievePunchThroughIdentifiersFromInfoResponse]
+ -[CRCarPlayAppPolicyEvaluator _vehicleForCurrentSession]
+ -[CRCarPlayAppPolicyEvaluator effectivePolicyForAppDeclaration:withVerifiedPunchThroughs:]
+ -[CRCarPlayAppPolicyEvaluator initWithSession:]
+ -[CRCarPlayAppPolicyEvaluator pairedVehicleManager]
+ -[CRCarPlayAppPolicyEvaluator session]
+ -[CRCarPlayCapabilities setZoomFactor:]
+ -[CRCarPlayCapabilities zoomFactor]
+ -[CRDisplayScaleInfo .cxx_destruct]
+ -[CRDisplayScaleInfo _customZoomEnabled]
+ -[CRDisplayScaleInfo _heuristicPixelSize]
+ -[CRDisplayScaleInfo _minDisplaySize]
+ -[CRDisplayScaleInfo _minViewAreaPixelSize]
+ -[CRDisplayScaleInfo _optimalScaleFactorWithPointScale:]
+ -[CRDisplayScaleInfo _pointScaleForSize:]
+ -[CRDisplayScaleInfo _scaleMode]
+ -[CRDisplayScaleInfo allowedScaleModes]
+ -[CRDisplayScaleInfo canvasPixelSizeForDisplayScaleMode:]
+ -[CRDisplayScaleInfo defaultDisplayMode]
+ -[CRDisplayScaleInfo description]
+ -[CRDisplayScaleInfo displayScaleModesForCanvasPixelSize:]
+ -[CRDisplayScaleInfo initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:]
+ -[CRDisplayScaleInfo initWithScreenInfo:]
+ -[CRDisplayScaleInfo isHeuristicScalable]
+ -[CRDisplayScaleInfo optimizedPointScale]
+ -[CRDisplayScaleInfo originalPointScale]
+ -[CRDisplayScaleInfo physicalSize]
+ -[CRDisplayScaleInfo pixelSize]
+ -[CRDisplayScaleInfo pointScaleForMode:]
+ -[CRDisplayScaleInfo preferredPointScale]
+ -[CRDisplayScaleInfo preferredToOriginalScaleRatio]
+ -[CRDisplayScaleInfo screenType]
+ -[CRDisplayScaleInfo setPhysicalSize:]
+ -[CRDisplayScaleInfo setPixelSize:]
+ -[CRDisplayScaleInfo setScreenType:]
+ -[CRDisplayScaleInfo setSquaredPixelSize:]
+ -[CRDisplayScaleInfo setViewAreas:]
+ -[CRDisplayScaleInfo setZoomFactor:]
+ -[CRDisplayScaleInfo squaredPixelSize]
+ -[CRDisplayScaleInfo viewAreas]
+ -[CRDisplayScaleInfo zoomFactor]
+ -[CRDisplayThemeData currentHomeScreenStyle]
+ -[CRDisplayThemeData currentHomeScreenStyle].cold.1
+ -[CRDisplayThemeData homeScreenStyleForLayout]
+ -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:homeScreenStyleForLayout:]
+ -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:homeScreenStyleForLayout:].cold.1
+ -[CRDisplayThemeData themeDataWithCurrentHomeScreenStyle:]
+ -[CROEMPunchThroughsAppData .cxx_destruct]
+ -[CROEMPunchThroughsAppData encodeWithCoder:]
+ -[CROEMPunchThroughsAppData initWithCoder:]
+ -[CROEMPunchThroughsAppData initWithPunchThroughIDs:]
+ -[CROEMPunchThroughsAppData punchThroughs]
+ -[CRPairedVehicleManager fetchViewAreasForVehicleIdentifier:completion:]
+ -[CRPairedVehicleManager saveViewAreas:forVehicleIdentifier:completion:]
+ -[CRPairedVehicleManager syncFetchViewAreasForVehicleIdentifier:completion:]
+ -[CRSubtitleSettings allowBackgroundColorOverride]
+ -[CRSubtitleSettings allowBackgroundOpacityOverride]
+ -[CRSubtitleSettings allowFontColorOverride]
+ -[CRSubtitleSettings allowFontNameOverride]
+ -[CRSubtitleSettings allowFontSizeOverride]
+ -[CRSubtitleSettings allowTextEdgeStyleOverride]
+ -[CRSubtitleSettings allowTextHighlightOverride]
+ -[CRSubtitleSettings allowTextOpacityOverride]
+ -[CRSubtitleSettings backgroundColor]
+ -[CRSubtitleSettings backgroundOpacity]
+ -[CRSubtitleSettings closedCaptionsEnabled]
+ -[CRSubtitleSettings copyWithZone:]
+ -[CRSubtitleSettings description]
+ -[CRSubtitleSettings dictionaryRepresentation]
+ -[CRSubtitleSettings encodeWithCoder:]
+ -[CRSubtitleSettings fontColor]
+ -[CRSubtitleSettings fontName]
+ -[CRSubtitleSettings fontSize]
+ -[CRSubtitleSettings initWithCoder:]
+ -[CRSubtitleSettings initWithDictionaryRepresentation:]
+ -[CRSubtitleSettings setAllowBackgroundColorOverride:]
+ -[CRSubtitleSettings setAllowBackgroundOpacityOverride:]
+ -[CRSubtitleSettings setAllowFontColorOverride:]
+ -[CRSubtitleSettings setAllowFontNameOverride:]
+ -[CRSubtitleSettings setAllowFontSizeOverride:]
+ -[CRSubtitleSettings setAllowTextEdgeStyleOverride:]
+ -[CRSubtitleSettings setAllowTextHighlightOverride:]
+ -[CRSubtitleSettings setAllowTextOpacityOverride:]
+ -[CRSubtitleSettings setBackgroundColor:]
+ -[CRSubtitleSettings setBackgroundOpacity:]
+ -[CRSubtitleSettings setClosedCaptionsEnabled:]
+ -[CRSubtitleSettings setFontColor:]
+ -[CRSubtitleSettings setFontName:]
+ -[CRSubtitleSettings setFontSize:]
+ -[CRSubtitleSettings setTextEdgeStyle:]
+ -[CRSubtitleSettings setTextHighlightColor:]
+ -[CRSubtitleSettings setTextHighlightOpacity:]
+ -[CRSubtitleSettings setTextOpacity:]
+ -[CRSubtitleSettings textEdgeStyle]
+ -[CRSubtitleSettings textHighlightColor]
+ -[CRSubtitleSettings textHighlightOpacity]
+ -[CRSubtitleSettings textOpacity]
+ -[CRVehicle displayScaleMode]
+ -[CRVehicle homeScreenStyleDataForDisplayWithID:]
+ -[CRVehicle homeScreenStyleDataForDisplayWithID:].cold.1
+ -[CRVehicle homeScreenStyleData]
+ -[CRVehicle oemPunchThroughsAsApp]
+ -[CRVehicle setDisplayScaleMode:]
+ -[CRVehicle setHomeScreenStyle:forDisplayWithID:]
+ -[CRVehicle setHomeScreenStyle:forDisplayWithID:].cold.1
+ -[CRVehicle setHomeScreenStyleData:]
+ -[CRVehicle setOemPunchThroughsAsApp:]
+ -[CRVehicle setSubtitleSettings:]
+ -[CRVehicle setTextSizePreference:]
+ -[CRVehicle setVideoDiagnosticsEnabled:]
+ -[CRVehicle setViewAreas:]
+ -[CRVehicle subtitleSettings]
+ -[CRVehicle textSizePreference]
+ -[CRVehicle videoDiagnosticsEnabled]
+ -[CRVehicle viewAreas]
+ -[CRVehicleVideoSettings .cxx_destruct]
+ -[CRVehicleVideoSettings diagnosticsEnabled]
+ -[CRVehicleVideoSettings diagnosticsEnabled].cold.1
+ -[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]
+ -[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:].cold.1
+ -[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]
+ -[CRVehicleVideoSettings fetchLicensesTextWithCompletion:].cold.1
+ -[CRVehicleVideoSettings initWithVehicleIdentifier:]
+ -[CRVehicleVideoSettings initWithVehicleIdentifier:].cold.1
+ -[CRVehicleVideoSettings serviceClient]
+ -[CRVehicleVideoSettings setDiagnosticsEnabled:]
+ -[CRVehicleVideoSettings setServiceClient:]
+ -[CRVehicleVideoSettings setSubtitleSettings:]
+ -[CRVehicleVideoSettings subtitleSettings]
+ -[CRVehicleVideoSettings subtitleSettings].cold.1
+ -[CRVehicleVideoSettings vehicleID]
+ -[CRViewArea description]
+ -[CRViewArea initWithAirPlayDictionary:]
+ -[CRViewArea initWithVisiblePixelFrame:safeAreaPixelFrame:]
+ -[CRViewArea safeAreaPixelFrame]
+ -[CRViewArea setSafeAreaPixelFrame:]
+ -[CRViewArea setVisiblePixelFrame:]
+ -[CRViewArea visiblePixelFrame]
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table122
+ GCC_except_table144
+ GCC_except_table167
+ GCC_except_table173
+ GCC_except_table199
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ _BSEqualObjects
+ _BSStringFromBOOL
+ _BSStringFromCGRect
+ _CARSessionInfoKeySessionManagementInfo
+ _CARSessionInfoKeyStopSession
+ _CARSessionVideoPlaybackAvailabilityChangedNotification
+ _CARkAPEndpointInfoResponseKey_FileTransfer
+ _CARkAPEndpointInfoResponseKey_LogTransfer
+ _CARkAPEndpointInfoResponseKey_VideoInfo
+ _CGSizeScaledBy
+ _CRAirPlayZoomFactorKey
+ _CRCanvasSizeOverridesWithAirplayDisplays
+ _CRCarKitDisplayScaleError
+ _CRDisplayScaleAdjustedPointScale
+ _CRFetchOverrideCanvasSizeForCertificateSerialNumber
+ _CRFetchScaledDisplaysForCertificateSerialNumber
+ _CROverrideCanvasSizeKey
+ _CRScaledDisplaysWithAirplayDisplays
+ _CRScaledDisplaysWithAirplayDisplays.cold.1
+ _CRScaledDisplaysWithAirplayDisplays.cold.2
+ _CRSizeFromAirPlayDictionaryForKey
+ _CRSizeFromAirPlayDictionaryForKey.cold.1
+ _CRStopSessionWithSessionIdentifier
+ _CRZoomFactorKey
+ _CarDisplayScaleLogging
+ _CarDisplayScaleLogging.cold.1
+ _CarDisplayScaleLogging.facility
+ _CarDisplayScaleLogging.onceToken
+ _MobileGestalt_copy_hwModelDescriptionForAnalytics_obj
+ _MobileGestalt_get_current_device
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CRDisplayScaleInfo
+ _OBJC_CLASS_$_CRHomeScreenStyleData
+ _OBJC_CLASS_$_CROEMPunchThroughsAppData
+ _OBJC_CLASS_$_CRSubtitleSettings
+ _OBJC_CLASS_$_CRVehicleVideoSettings
+ _OBJC_CLASS_$_CRViewArea
+ _OBJC_IVAR_$_CARScreenInfo._zoomFactor
+ _OBJC_IVAR_$_CARSession._cachedVideoPlaybackAvailable
+ _OBJC_IVAR_$_CARSessionConfiguration._supportedStopSessionDisconnectReasons
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsFileTransfer
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsStopSession
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsStopSessionDisconnectForThisDrive
+ _OBJC_IVAR_$_CARSessionConfiguration._videoPlaybackSupported
+ _OBJC_IVAR_$_CARSessionRequestHost._remoteDeviceConnected
+ _OBJC_IVAR_$_CRCarPlayAppDeclaration._supportsAutomakerAppService
+ _OBJC_IVAR_$_CRCarPlayAppDeclaration._supportsVideo
+ _OBJC_IVAR_$_CRCarPlayAppPolicy._sessionDependentPolicy
+ _OBJC_IVAR_$_CRCarPlayAppPolicyEvaluator._pairedVehicleManager
+ _OBJC_IVAR_$_CRCarPlayAppPolicyEvaluator._session
+ _OBJC_IVAR_$_CRCarPlayCapabilities._zoomFactor
+ _OBJC_IVAR_$_CRDisplayScaleInfo._physicalSize
+ _OBJC_IVAR_$_CRDisplayScaleInfo._pixelSize
+ _OBJC_IVAR_$_CRDisplayScaleInfo._screenType
+ _OBJC_IVAR_$_CRDisplayScaleInfo._squaredPixelSize
+ _OBJC_IVAR_$_CRDisplayScaleInfo._viewAreas
+ _OBJC_IVAR_$_CRDisplayScaleInfo._zoomFactor
+ _OBJC_IVAR_$_CRDisplayThemeData._homeScreenStyleForLayout
+ _OBJC_IVAR_$_CROEMPunchThroughsAppData._punchThroughs
+ _OBJC_IVAR_$_CRSubtitleSettings._allowBackgroundColorOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowBackgroundOpacityOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowFontColorOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowFontNameOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowFontSizeOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowTextEdgeStyleOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowTextHighlightOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._allowTextOpacityOverride
+ _OBJC_IVAR_$_CRSubtitleSettings._backgroundColor
+ _OBJC_IVAR_$_CRSubtitleSettings._backgroundOpacity
+ _OBJC_IVAR_$_CRSubtitleSettings._closedCaptionsEnabled
+ _OBJC_IVAR_$_CRSubtitleSettings._fontColor
+ _OBJC_IVAR_$_CRSubtitleSettings._fontName
+ _OBJC_IVAR_$_CRSubtitleSettings._fontSize
+ _OBJC_IVAR_$_CRSubtitleSettings._textEdgeStyle
+ _OBJC_IVAR_$_CRSubtitleSettings._textHighlightColor
+ _OBJC_IVAR_$_CRSubtitleSettings._textHighlightOpacity
+ _OBJC_IVAR_$_CRSubtitleSettings._textOpacity
+ _OBJC_IVAR_$_CRVehicle._displayScaleMode
+ _OBJC_IVAR_$_CRVehicle._homeScreenStyleData
+ _OBJC_IVAR_$_CRVehicle._oemPunchThroughsAsApp
+ _OBJC_IVAR_$_CRVehicle._subtitleSettings
+ _OBJC_IVAR_$_CRVehicle._textSizePreference
+ _OBJC_IVAR_$_CRVehicle._videoDiagnosticsEnabled
+ _OBJC_IVAR_$_CRVehicle._viewAreas
+ _OBJC_IVAR_$_CRVehicleVideoSettings._serviceClient
+ _OBJC_IVAR_$_CRVehicleVideoSettings._vehicleID
+ _OBJC_IVAR_$_CRViewArea._safeAreaPixelFrame
+ _OBJC_IVAR_$_CRViewArea._visiblePixelFrame
+ _OBJC_METACLASS_$_CRDisplayScaleInfo
+ _OBJC_METACLASS_$_CRHomeScreenStyleData
+ _OBJC_METACLASS_$_CROEMPunchThroughsAppData
+ _OBJC_METACLASS_$_CRSubtitleSettings
+ _OBJC_METACLASS_$_CRVehicleVideoSettings
+ _OBJC_METACLASS_$_CRViewArea
+ __CLASS_METHODS_CRHomeScreenStyleData
+ __CLASS_PROPERTIES_CRHomeScreenStyleData
+ __DATA_CRHomeScreenStyleData
+ __INSTANCE_METHODS_CRHomeScreenStyleData
+ __IVARS_CRHomeScreenStyleData
+ __METACLASS_DATA_CRHomeScreenStyleData
+ __OBJC_$_CLASS_METHODS_CRDisplayScaleInfo
+ __OBJC_$_CLASS_METHODS_CROEMPunchThroughsAppData
+ __OBJC_$_CLASS_METHODS_CRSubtitleSettings
+ __OBJC_$_CLASS_PROP_LIST_CROEMPunchThroughsAppData
+ __OBJC_$_CLASS_PROP_LIST_CRSubtitleSettings
+ __OBJC_$_INSTANCE_METHODS_CARScreenInfo(CRDisplayScaling)
+ __OBJC_$_INSTANCE_METHODS_CRDisplayScaleInfo
+ __OBJC_$_INSTANCE_METHODS_CROEMPunchThroughsAppData
+ __OBJC_$_INSTANCE_METHODS_CRSubtitleSettings
+ __OBJC_$_INSTANCE_METHODS_CRVehicleVideoSettings
+ __OBJC_$_INSTANCE_METHODS_CRViewArea
+ __OBJC_$_INSTANCE_VARIABLES_CRDisplayScaleInfo
+ __OBJC_$_INSTANCE_VARIABLES_CROEMPunchThroughsAppData
+ __OBJC_$_INSTANCE_VARIABLES_CRSubtitleSettings
+ __OBJC_$_INSTANCE_VARIABLES_CRVehicleVideoSettings
+ __OBJC_$_INSTANCE_VARIABLES_CRViewArea
+ __OBJC_$_PROP_LIST_CRDisplayScaleInfo
+ __OBJC_$_PROP_LIST_CROEMPunchThroughsAppData
+ __OBJC_$_PROP_LIST_CRSubtitleSettings
+ __OBJC_$_PROP_LIST_CRVehicleVideoSettings
+ __OBJC_$_PROP_LIST_CRViewArea
+ __OBJC_CLASS_PROTOCOLS_$_CROEMPunchThroughsAppData
+ __OBJC_CLASS_PROTOCOLS_$_CRSubtitleSettings
+ __OBJC_CLASS_RO_$_CRDisplayScaleInfo
+ __OBJC_CLASS_RO_$_CROEMPunchThroughsAppData
+ __OBJC_CLASS_RO_$_CRSubtitleSettings
+ __OBJC_CLASS_RO_$_CRVehicleVideoSettings
+ __OBJC_CLASS_RO_$_CRViewArea
+ __OBJC_METACLASS_RO_$_CRDisplayScaleInfo
+ __OBJC_METACLASS_RO_$_CROEMPunchThroughsAppData
+ __OBJC_METACLASS_RO_$_CRSubtitleSettings
+ __OBJC_METACLASS_RO_$_CRVehicleVideoSettings
+ __OBJC_METACLASS_RO_$_CRViewArea
+ __PROPERTIES_CRHomeScreenStyleData
+ __PROTOCOLS_CRHomeScreenStyleData
+ __PROTOCOLS_CRHomeScreenStyleData.2
+ ___118-[CRCarPlayAppPolicyEvaluator _hideAppIfPunchThroughExistsForBundleIdentifier:withVerifiedPunchThroughs:andAppPolicy:]_block_invoke
+ ___118-[CRCarPlayAppPolicyEvaluator _hideAppIfPunchThroughExistsForBundleIdentifier:withVerifiedPunchThroughs:andAppPolicy:]_block_invoke.cold.1
+ ___120-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:]_block_invoke
+ ___120-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:]_block_invoke_2
+ ___120-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:]_block_invoke_3
+ ___24-[CARSession suggestUI:]_block_invoke.419
+ ___41+[CARPrototypePref statusBarEdgeOverride]_block_invoke.354
+ ___41-[CRDisplayScaleInfo initWithScreenInfo:]_block_invoke
+ ___42+[CARPrototypePref liveActivitiesDisabled]_block_invoke
+ ___42+[CARPrototypePref liveActivitiesDisabled]_block_invoke_2
+ ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke
+ ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke.21
+ ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke.21.cold.1
+ ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke_2
+ ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke_2.cold.1
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.36
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.36.cold.1
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke_2
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke_2.cold.1
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke.26
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke.26.cold.1
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2.cold.1
+ ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2.cold.2
+ ___47-[CRCarPlayAppPolicyEvaluator initWithSession:]_block_invoke
+ ___48+[CARPrototypePref statusBarHorizontalThreshold]_block_invoke.367
+ ___48-[CARSessionConfiguration updateCarCapabilities]_block_invoke
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.41
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.41.cold.1
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke_2
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke_2.cold.1
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke_2.cold.2
+ ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.355
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.75
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.75.cold.1
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.cold.1
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.49
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.49.cold.1
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke_2
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke_2.cold.1
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.45
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.45.cold.1
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke_2
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke_2.cold.1
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.151
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.151.cold.1
+ ___67+[CRScreenScaleHeuristics scaledDisplays:withDisplayScaling:reply:]_block_invoke
+ ___67+[CRScreenScaleHeuristics scaledDisplays:withDisplayScaling:reply:]_block_invoke.cold.1
+ ___72-[CRPairedVehicleManager fetchViewAreasForVehicleIdentifier:completion:]_block_invoke
+ ___72-[CRPairedVehicleManager fetchViewAreasForVehicleIdentifier:completion:]_block_invoke_2
+ ___72-[CRPairedVehicleManager saveViewAreas:forVehicleIdentifier:completion:]_block_invoke
+ ___72-[CRPairedVehicleManager saveViewAreas:forVehicleIdentifier:completion:]_block_invoke_2
+ ___72-[CRPairedVehicleManager saveViewAreas:forVehicleIdentifier:completion:]_block_invoke_3
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.602
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.602.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.602.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.607
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.611
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.612
+ ___74-[CRCarPlayAppPolicyEvaluator _automakerAppServiceContainsAppDeclaration:]_block_invoke
+ ___74-[CRCarPlayAppPolicyEvaluator _automakerAppServiceContainsAppDeclaration:]_block_invoke.cold.1
+ ___76-[CRPairedVehicleManager syncFetchViewAreasForVehicleIdentifier:completion:]_block_invoke
+ ___76-[CRPairedVehicleManager syncFetchViewAreasForVehicleIdentifier:completion:]_block_invoke_2
+ ___81+[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:]_block_invoke
+ ___CARHandleSuggestUI_block_invoke.414
+ ___CRCollectCarPlayDiagnostics_block_invoke.161
+ ___CRCollectVehicleLogs_block_invoke.165
+ ___CRFetchOverrideCanvasSizeForCertificateSerialNumber_block_invoke
+ ___CRFetchOverrideCanvasSizeForCertificateSerialNumber_block_invoke_2
+ ___CRFetchOverrideCanvasSizeForCertificateSerialNumber_block_invoke_3
+ ___CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke
+ ___CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke_2
+ ___CRFetchScaledDisplaysForCertificateSerialNumber_block_invoke_3
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.169
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.169.cold.1
+ ___CRPostBannerToPhone_block_invoke.153
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.179
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.179.cold.1
+ ___CRStopSessionWithSessionIdentifier_block_invoke
+ ___CRStopSessionWithSessionIdentifier_block_invoke_2
+ ___CRStopSessionWithSessionIdentifier_block_invoke_3
+ ___CarDisplayScaleLogging_block_invoke
+ ___block_descriptor_32_e22_16?0"NSDictionary"8l
+ ___block_descriptor_32_e31_v24?0"CRVehicle"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e40_v24?0"CRSubtitleSettings"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32s_e21_B20?0"NSString"8B16ls32l8
+ ___block_descriptor_40_e8_32s_e21_i20?0"NSString"8i16ls32l8
+ ___block_descriptor_40_e8_32s_e34_v32?0"CARScreenViewArea"8Q16^B24ls32l8
+ ___block_descriptor_41_e8_32s_e27_v16?0"<CRCarKitService>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"<CRCarKitService>"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"<CRCarKitService>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.150
+ ___block_literal_global.160
+ ___block_literal_global.164
+ ___block_literal_global.168
+ ___block_literal_global.194
+ ___block_literal_global.199
+ ___block_literal_global.218
+ ___block_literal_global.234
+ ___block_literal_global.283
+ ___block_literal_global.288
+ ___block_literal_global.297
+ ___block_literal_global.311
+ ___block_literal_global.327
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.379
+ ___block_literal_global.38
+ ___block_literal_global.381
+ ___block_literal_global.388
+ ___block_literal_global.396
+ ___block_literal_global.413
+ ___block_literal_global.424
+ ___block_literal_global.47
+ ___block_literal_global.617
+ ___block_literal_global.634
+ ___block_literal_global.739
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __os_feature_enabled_impl
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CarKit
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_CarKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CarKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CarKit
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CarKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CarKit
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_CarKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CarKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CarKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CarKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CarKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CarKit
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CarKit
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_CarKit
+ __swift_stdlib_reportUnimplementedInitializer
+ _figEndpointNotificationCallback.cold.5
+ _figEndpointNotificationCallback.cold.6
+ _initWithSession:.onceToken
+ _kCRCarPlayEntitlementVideo
+ _kFigEndpointCarEntityHasScreenForAirPlayVideoKey_SourceAppBundleID
+ _kFigEndpointCentralNotification_CarEntityHasScreenForAirPlayVideo
+ _kFigEndpointNotification_EndpointDescriptionChanged
+ _kFigEndpointProperty_SupportedFeatures
+ _keypath_get_selector_luminance
+ _keypath_get_selector_saturation
+ _keypath_get_selector_styleType
+ _keypath_get_selector_styleVariant
+ _keypath_get_selector_variation
+ _liveActivitiesDisabled._liveActivitiesDisabled
+ _liveActivitiesDisabled.onceToken
+ _objc_allocWithZone
+ _objc_msgSend$_automakerAppServiceContainsAppDeclaration:
+ _objc_msgSend$_customZoomEnabled
+ _objc_msgSend$_handleEndpointDescriptionChanged
+ _objc_msgSend$_handleIsPlayingVideoFromApp:
+ _objc_msgSend$_hideAppIfPunchThroughExistsForBundleIdentifier:withPunchThroughsAppData:andAppPolicy:
+ _objc_msgSend$_hideAppIfPunchThroughExistsForBundleIdentifier:withVerifiedPunchThroughs:andAppPolicy:
+ _objc_msgSend$_minDisplaySize
+ _objc_msgSend$_minViewAreaPixelSize
+ _objc_msgSend$_newCapabilitiesFromGlobalDomainWithIdentifier:
+ _objc_msgSend$_optimalScaleFactorWithPointScale:
+ _objc_msgSend$_pointScaleForSize:
+ _objc_msgSend$_retrievePunchThroughIdentifiersFromInfoResponse
+ _objc_msgSend$_scaleMode
+ _objc_msgSend$_vehicleForCurrentSession
+ _objc_msgSend$allowedScaleModes
+ _objc_msgSend$bounds
+ _objc_msgSend$cachedVideoPlaybackAvailable
+ _objc_msgSend$canvasPixelSizeForDisplayScaleMode:
+ _objc_msgSend$currentHomeScreenStyle
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$defaultDisplayMode
+ _objc_msgSend$displayScaleInfoWithDictionary:screenType:zoomFactor:error:
+ _objc_msgSend$displayScaleMode
+ _objc_msgSend$displayScaleModesForCanvasPixelSize:
+ _objc_msgSend$effectivePolicyForAppDeclaration:withVerifiedPunchThroughs:
+ _objc_msgSend$fetchCarCapabilitiesWithIdentifier:
+ _objc_msgSend$fetchOverrideCanvasSizeWithCertificateSerialNumber:displays:reply:
+ _objc_msgSend$fetchScaledDisplaysWithCertificateSerialNumber:displays:reply:
+ _objc_msgSend$fetchViewAreasForVehicleIdentifier:reply:
+ _objc_msgSend$homeScreenStyleData
+ _objc_msgSend$homeScreenStyleForLayout
+ _objc_msgSend$initWithAirPlayDictionary:
+ _objc_msgSend$initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:homeScreenStyleForLayout:
+ _objc_msgSend$initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:
+ _objc_msgSend$initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:
+ _objc_msgSend$initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:
+ _objc_msgSend$initWithPunchThroughIDs:
+ _objc_msgSend$initWithScreenInfo:
+ _objc_msgSend$initWithSession:
+ _objc_msgSend$initWithVisiblePixelFrame:safeAreaPixelFrame:
+ _objc_msgSend$isHeuristicScalable
+ _objc_msgSend$isRemoteDeviceConnected
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$oemPunchThroughsAsApp
+ _objc_msgSend$optimizedPointScale
+ _objc_msgSend$originalPointScale
+ _objc_msgSend$pairedVehicleManager
+ _objc_msgSend$preferredPointScale
+ _objc_msgSend$preferredToOriginalScaleRatio
+ _objc_msgSend$punchThroughs
+ _objc_msgSend$safeAreaPixelFrame
+ _objc_msgSend$saveViewAreas:forVehicleIdentifier:reply:
+ _objc_msgSend$scaledDisplays:withDisplayScaling:reply:
+ _objc_msgSend$session:isPlayingVideoFromApp:
+ _objc_msgSend$setAllowBackgroundColorOverride:
+ _objc_msgSend$setAllowBackgroundOpacityOverride:
+ _objc_msgSend$setAllowFontColorOverride:
+ _objc_msgSend$setAllowFontNameOverride:
+ _objc_msgSend$setAllowFontSizeOverride:
+ _objc_msgSend$setAllowTextHighlightOverride:
+ _objc_msgSend$setAllowTextOpacityOverride:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setBackgroundOpacity:
+ _objc_msgSend$setCachedVideoPlaybackAvailable:
+ _objc_msgSend$setClosedCaptionsEnabled:
+ _objc_msgSend$setDisplayScaleMode:
+ _objc_msgSend$setFontColor:
+ _objc_msgSend$setFontName:
+ _objc_msgSend$setFontSize:
+ _objc_msgSend$setHomeScreenStyleData:
+ _objc_msgSend$setOemPunchThroughsAsApp:
+ _objc_msgSend$setSessionDependentPolicy:
+ _objc_msgSend$setSubtitleSettings:
+ _objc_msgSend$setSupportsAutomakerAppService:
+ _objc_msgSend$setSupportsVideo:
+ _objc_msgSend$setTextEdgeStyle:
+ _objc_msgSend$setTextHighlightColor:
+ _objc_msgSend$setTextHighlightOpacity:
+ _objc_msgSend$setTextOpacity:
+ _objc_msgSend$setTextSizePreference:
+ _objc_msgSend$setVideoDiagnosticsEnabled:
+ _objc_msgSend$setVideoDiagnosticsEnabled:forVehicleIdentifier:reply:
+ _objc_msgSend$setVideoSubtitleSettings:forVehicleIdentifier:reply:
+ _objc_msgSend$setViewAreas:
+ _objc_msgSend$setZoomFactor:
+ _objc_msgSend$squaredPixelSize
+ _objc_msgSend$stopSessionWithSessionIdentifier:reason:reply:
+ _objc_msgSend$subtitleSettings
+ _objc_msgSend$supportsAutomakerAppService
+ _objc_msgSend$supportsVideo
+ _objc_msgSend$textSizePreference
+ _objc_msgSend$themeDataWithCurrentHomeScreenStyle:
+ _objc_msgSend$unadjustedSafeFrame
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$vehicleID
+ _objc_msgSend$videoAnalyticsForVehicleIdentifier:reply:
+ _objc_msgSend$videoDiagnosticsEnabled
+ _objc_msgSend$videoDiagnosticsEnabledForVehicleIdentifier:reply:
+ _objc_msgSend$videoLicensesTextForVehicleIdentifier:reply:
+ _objc_msgSend$videoPlaybackAvailable
+ _objc_msgSend$videoPlaybackSupported
+ _objc_msgSend$videoSubtitleSettingsForVehicleIdentifier:reply:
+ _objc_msgSend$visiblePixelFrame
+ _objc_msgSend$zoomFactor
+ _objc_opt_self
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_initStackObject
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic $sSY
+ _symbolic SS_ypt
+ _symbolic Si
+ _symbolic _____ So21CRHomeScreenStyleTypeV
+ _symbolic _____ So24CRHomeScreenStyleVariantV
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic ypSg
- +[CRCarPlayCapabilities fetchCarCapabilities]
- +[CRCarPlayCapabilities fetchCarCapabilities].cold.1
- +[CRCarPlayCapabilities newCapabilitiesFromGlobalDomain]
- +[CRCarPlayCapabilities newCapabilitiesFromGlobalDomain].cold.1
- +[CRCarPlayCapabilities newCapabilitiesFromGlobalDomain].cold.2
- +[CRScreenScaleHeuristics scaledDisplays:reply:]
- -[CARScreenInfo initWithPropertySupplier:screenType:]
- -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:]
- -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:].cold.1
- -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:].cold.2
- -[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:].cold.3
- -[CARSessionRequestHost initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:]
- -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:]
- -[CRDisplayThemeData initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:].cold.1
- GCC_except_table101
- GCC_except_table104
- GCC_except_table116
- GCC_except_table137
- GCC_except_table160
- GCC_except_table166
- GCC_except_table192
- GCC_except_table28
- GCC_except_table32
- GCC_except_table34
- GCC_except_table35
- GCC_except_table95
- _CARkAPEndpointInfoResponseKey_LogTransferDataChannels
- __OBJC_$_INSTANCE_METHODS_CARScreenInfo
- ___104-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:]_block_invoke
- ___104-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:]_block_invoke_2
- ___104-[CARScreenInfo initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:]_block_invoke_3
- ___24-[CARSession suggestUI:]_block_invoke.414
- ___35-[CRCarPlayAppPolicyEvaluator init]_block_invoke
- ___41+[CARPrototypePref statusBarEdgeOverride]_block_invoke.344
- ___48+[CARPrototypePref statusBarHorizontalThreshold]_block_invoke.357
- ___48+[CRScreenScaleHeuristics scaledDisplays:reply:]_block_invoke
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke.350
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.148
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.148.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.584
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.584.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.584.cold.2
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.588
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.592
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.593
- ___CARHandleSuggestUI_block_invoke.409
- ___CRCollectCarPlayDiagnostics_block_invoke.140
- ___CRCollectVehicleLogs_block_invoke.144
- ___CRIsPreflightThemeAssetEnabled_block_invoke.148
- ___CRIsPreflightThemeAssetEnabled_block_invoke.148.cold.1
- ___CRPostBannerToPhone_block_invoke.132
- ___CRSetPreflightThemeAssetEnabled_block_invoke.158
- ___CRSetPreflightThemeAssetEnabled_block_invoke.158.cold.1
- ___block_descriptor_48_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
- ___block_descriptor_64_e8_32s40s48s56s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_literal_global.139
- ___block_literal_global.143
- ___block_literal_global.147
- ___block_literal_global.157
- ___block_literal_global.173
- ___block_literal_global.213
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.317
- ___block_literal_global.325
- ___block_literal_global.333
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.359
- ___block_literal_global.361
- ___block_literal_global.376
- ___block_literal_global.378
- ___block_literal_global.408
- ___block_literal_global.419
- ___block_literal_global.598
- ___block_literal_global.601
- ___block_literal_global.705
- _init.onceToken
- _objc_msgSend$fetchCarCapabilities
- _objc_msgSend$initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:
- _objc_msgSend$initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:
- _objc_msgSend$initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:
- _objc_msgSend$newCapabilitiesFromGlobalDomain
- _objc_msgSend$scaledDisplays:reply:
CStrings:
+ "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, supportsLoD: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
+ "%@ {currentLayoutID: %@ paletteIDForLayout: %@ wallpaperForLayout: %@ homeScreenStyleForLayout: %@}"
+ "+[CRCarPlayCapabilities _newCapabilitiesFromGlobalDomainWithIdentifier:]"
+ "-[CRDisplayThemeData currentHomeScreenStyle]"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
+ "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@, zoomFactor = %@"
+ "@\"CRHomeScreenStyleData\""
+ "@\"CRPairedVehicleManager\""
+ "@\"CRSubtitleSettings\""
+ "@108@0:8@16@24@32q40@48@56@64@72B80@84@92B100B104"
+ "@16@?0@\"NSDictionary\"8"
+ "@24@0:8^v16"
+ "@32@0:8q16q24"
+ "@32@0:8{CGSize=dd}16"
+ "@40@0:8@?16Q24@32"
+ "@48@0:8@16Q24@32^@40"
+ "@56@0:8q16q24d32d40d48"
+ "@72@0:8{CGSize=dd}16{CGSize=dd}32@48Q56@64"
+ "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "@88@0:8@?16Q24{NSEdgeInsets=dddd}32@64@72@80"
+ "Allowed scale modes: defaultSize:%{public}@, optimizedSize:%{public}@; Original equals to default: %{public}@"
+ "App with unknown category: %@"
+ "AppClips"
+ "AppPolicy No punchThrough identifier in CRVehicle for app: %@"
+ "AppPolicy asset punchThroughs check"
+ "AppPolicy hiding app: %@"
+ "AppPolicy infoResponse punchThroughs check"
+ "AppPolicy no punchThroughs match between asset and infoResponse"
+ "B20@?0@\"NSString\"8B16"
+ "CARSessionVideoPlaybackAvailabilityChangedNotification"
+ "CRCanvasSizeOverridesWithAirplayDisplays: CRDisplayScaleInfo: %@"
+ "CRCapabilitiesZoomFactorKeyKey"
+ "CRDisplayScaleInfo"
+ "CRDisplayScaling"
+ "CRHomeScreenStyleData"
+ "CROEMPunchThroughsAppData"
+ "CRScaledDisplaysWithAirplayDisplays: CRDisplayScaleInfo: %@"
+ "CRScaledDisplaysWithAirplayDisplays: error creating CRDisplayScaleInfo, empty no error provided"
+ "CRScaledDisplaysWithAirplayDisplays: error creating CRDisplayScaleInfo: %@"
+ "CRScreenScaleHeuristics: error creating CRDisplayScaleInfo: %@"
+ "CRSizeFromAirPlayDictionaryForKey"
+ "CRSubtitleSettings"
+ "CRUtilities.m"
+ "CRVehicleVideoSettings"
+ "CRVehicleVideoSettings init with vehicleID: %@"
+ "CRViewArea"
+ "CRViewArea: visibleFrame: %@; safeAreaFrame: %@"
+ "CarKit.CRHomeScreenStyleData"
+ "Credenza"
+ "Default display scale canvas size calculated: Result(%@)=SquaredPixelSize(%@) x PreferredToOriginalRatio(%@) at PointScale(%@); minSize(%@)\nDisplayInfo: %@"
+ "Display height is less than minimum: Size(%@) < Min(%@); Returning minimal size"
+ "DisplayInfo: physicalSize: %@; pixelSize: %@; squaredPixelSize: %@; viewAreas: %@; screenType: %@; zoomFactor: %@"
+ "DisplayScale"
+ "DisplayScaling"
+ "Endpoint description changed"
+ "Failed to get home screen style, no display with id: %@"
+ "Failed to save vehicle with OEM PunchThroughs as app with error: %@"
+ "Failed to set home screen style on display %@: %@"
+ "HasShownEditWidgets"
+ "Height"
+ "Invalid palette ID, expected string:data, found: %@:%@"
+ "LogTransfer"
+ "Optimal[no ZoomFactor] display scale canvas size calculated: Result(%@) = PixelSize(%@) x OptimalScaleFactor(%@) at PointScale(%@)\nDisplayInfo: %@"
+ "Optimal[with ZoomFactor] display scale canvas size calculated: Result(%@) = SquaredPixelSize(%@) x AdjustedScale(%@); AdjustedScale=PreferredToOriginalScaleRatio(%@)/zoomFactor(%@)\nDisplayInfo: %@"
+ "OverrideCanvasSize"
+ "Q32@0:8{CGSize=dd}16"
+ "Returning home screen style using themeData for display with id: %@"
+ "Returning system home screen style data"
+ "SessionManagement"
+ "Set home screen style using themeData and display id: %@"
+ "Set system home screen style"
+ "SetCanvasOverrideSize to %@: (%f,%f)"
+ "SetCanvasOverrideSize: Unable to find screenID: %@"
+ "T@\"CRHomeScreenStyleData\",C,N,V_homeScreenStyleData"
+ "T@\"CRHomeScreenStyleData\",R,N"
+ "T@\"CRPairedVehicleManager\",R,N,V_pairedVehicleManager"
+ "T@\"CRSubtitleSettings\",&,N"
+ "T@\"CRSubtitleSettings\",&,N,V_subtitleSettings"
+ "T@\"NSArray\",&,N,V_viewAreas"
+ "T@\"NSArray\",R,C,N,V_punchThroughs"
+ "T@\"NSDictionary\",C,N,V_oemPunchThroughsAsApp"
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSDictionary\",R,C,N,V_homeScreenStyleForLayout"
+ "T@\"NSNumber\",&,N,V_cachedVideoPlaybackAvailable"
+ "T@\"NSNumber\",&,N,V_videoDiagnosticsEnabled"
+ "T@\"NSNumber\",&,N,V_zoomFactor"
+ "T@\"NSSet\",R,N,V_supportedStopSessionDisconnectReasons"
+ "T@\"NSString\",N,R"
+ "T@\"NSUUID\",R,N,V_vehicleID"
+ "TB,N,GisRemoteDeviceConnected,V_remoteDeviceConnected"
+ "TB,N,GisSessionDependentPolicy,V_sessionDependentPolicy"
+ "TB,N,R"
+ "TB,N,V_allowBackgroundColorOverride"
+ "TB,N,V_allowBackgroundOpacityOverride"
+ "TB,N,V_allowFontColorOverride"
+ "TB,N,V_allowFontNameOverride"
+ "TB,N,V_allowFontSizeOverride"
+ "TB,N,V_allowTextEdgeStyleOverride"
+ "TB,N,V_allowTextHighlightOverride"
+ "TB,N,V_allowTextOpacityOverride"
+ "TB,N,V_closedCaptionsEnabled"
+ "TB,N,V_supportsAutomakerAppService"
+ "TB,N,V_supportsVideo"
+ "TB,R,N,V_supportsFileTransfer"
+ "TB,R,N,V_supportsStopSessionDisconnectForThisDrive"
+ "TB,R,N,V_videoPlaybackSupported"
+ "TQ,N,V_screenType"
+ "TQ,R,N,V_supportsStopSession"
+ "Td,N,V_zoomFactor"
+ "Td,N,Vluminance"
+ "Td,N,Vsaturation"
+ "Td,N,Vvariation"
+ "Ti,N,V_backgroundColor"
+ "Ti,N,V_backgroundOpacity"
+ "Ti,N,V_fontColor"
+ "Ti,N,V_fontName"
+ "Ti,N,V_fontSize"
+ "Ti,N,V_textEdgeStyle"
+ "Ti,N,V_textHighlightColor"
+ "Ti,N,V_textHighlightOpacity"
+ "Ti,N,V_textOpacity"
+ "Tq,N,V_displayScaleMode"
+ "Tq,N,V_textSizePreference"
+ "Tq,N,VstyleType"
+ "Tq,N,VstyleVariant"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_safeAreaPixelFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visiblePixelFrame"
+ "T{CGSize=dd},N,V_physicalSize"
+ "T{CGSize=dd},N,V_pixelSize"
+ "T{CGSize=dd},N,V_squaredPixelSize"
+ "Unable to parse display physical size"
+ "Unable to parse display pixel size"
+ "Video"
+ "Width"
+ "ZoomFactor"
+ "_allowBackgroundColorOverride"
+ "_allowBackgroundOpacityOverride"
+ "_allowFontColorOverride"
+ "_allowFontNameOverride"
+ "_allowFontSizeOverride"
+ "_allowTextEdgeStyleOverride"
+ "_allowTextHighlightOverride"
+ "_allowTextOpacityOverride"
+ "_automakerAppServiceContainsAppDeclaration:"
+ "_backgroundColor"
+ "_backgroundOpacity"
+ "_cachedVideoPlaybackAvailable"
+ "_closedCaptionsEnabled"
+ "_customZoomEnabled"
+ "_displayScaleMode"
+ "_fontColor"
+ "_fontName"
+ "_fontSize"
+ "_handleEndpointDescriptionChanged"
+ "_handleIsPlayingVideoFromApp:"
+ "_heuristicPixelSize"
+ "_hideAppIfPunchThroughExistsForBundleIdentifier:withPunchThroughsAppData:andAppPolicy:"
+ "_hideAppIfPunchThroughExistsForBundleIdentifier:withVerifiedPunchThroughs:andAppPolicy:"
+ "_homeScreenStyleData"
+ "_homeScreenStyleForLayout"
+ "_minDisplaySize"
+ "_minViewAreaPixelSize"
+ "_newCapabilitiesFromGlobalDomainWithIdentifier:"
+ "_oemPunchThroughsAsApp"
+ "_optimalScaleFactorWithPointScale:"
+ "_pairedVehicleManager"
+ "_pointScaleForSize:"
+ "_punchThroughs"
+ "_remoteDeviceConnected"
+ "_retrievePunchThroughIdentifiersFromInfoResponse"
+ "_safeAreaPixelFrame"
+ "_scaleMode"
+ "_sessionDependentPolicy"
+ "_subtitleSettings"
+ "_supportedStopSessionDisconnectReasons"
+ "_supportsAutomakerAppService"
+ "_supportsFileTransfer"
+ "_supportsStopSession"
+ "_supportsStopSessionDisconnectForThisDrive"
+ "_supportsVideo"
+ "_textEdgeStyle"
+ "_textHighlightColor"
+ "_textHighlightOpacity"
+ "_textOpacity"
+ "_textSizePreference"
+ "_vehicleForCurrentSession"
+ "_vehicleID"
+ "_videoDiagnosticsEnabled"
+ "_videoPlaybackSupported"
+ "_visiblePixelFrame"
+ "_zoomFactor"
+ "allowBackgroundColorOverride"
+ "allowBackgroundOpacityOverride"
+ "allowFontColorOverride"
+ "allowFontNameOverride"
+ "allowFontSizeOverride"
+ "allowTextEdgeStyleOverride"
+ "allowTextHighlightOverride"
+ "allowTextOpacityOverride"
+ "allowedDisplayScaleModes"
+ "allowedScaleModes"
+ "analytics call failed: %@"
+ "analytics call failed: %{public}@"
+ "backgroundColor"
+ "backgroundOpacity"
+ "bounds"
+ "cachedVideoPlaybackAvailable"
+ "canvasPixelSizeForDisplayScaleMode:"
+ "closedCaptionsEnabled"
+ "com.apple.CarPlay.internal.refreshLiveActivity"
+ "com.apple.developer.carplay-automaker"
+ "com.apple.developer.carplay-video"
+ "createRemoteControlSession for channel uuid: %{public}@"
+ "currentHomeScreenStyle"
+ "d24@0:8Q16"
+ "d24@0:8q16"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeDoubleForKey:"
+ "decodeIntForKey:"
+ "defaultDisplayMode"
+ "defaultSettings"
+ "diagnosticsEnabled"
+ "diagnosticsEnabled call failed: %@"
+ "diagnosticsEnabled call failed: %{public}@"
+ "diagnosticsEnabled: %{public}@"
+ "disconnectReason"
+ "displayScaleInfoWithDictionary:screenType:zoomFactor:error:"
+ "displayScaleMode"
+ "displayScaleModeUserPreference"
+ "displayScaleModesForCanvasPixelSize:"
+ "effectivePolicyForAppDeclaration:withVerifiedPunchThroughs:"
+ "encodeDouble:forKey:"
+ "failed to fetch app clip declarations: %@"
+ "failed to get supported features for endpoint"
+ "fetch analytics"
+ "fetch diagnosticsEnabled"
+ "fetch licensesText"
+ "fetch subtitleSettings"
+ "fetchAnalyticsDataWithCompletion:"
+ "fetchCarCapabilitiesWithIdentifier:"
+ "fetchLicensesTextWithCompletion:"
+ "fetchOverrideCanvasSizeWithCertificateSerialNumber:displays:reply:"
+ "fetchScaledDisplaysWithCertificateSerialNumber:displays:reply:"
+ "fetchViewAreasForVehicleIdentifier:completion:"
+ "fetchViewAreasForVehicleIdentifier:reply:"
+ "fetched analytics"
+ "fetched licensesText"
+ "fileTransferInfo"
+ "fontColor"
+ "fontName"
+ "fontSize"
+ "hasShownEditWidgetsNotification"
+ "homeScreenStyleData"
+ "homeScreenStyleDataForDisplayWithID:"
+ "homeScreenStyleForLayout"
+ "i20@?0@\"NSString\"8i16"
+ "init()"
+ "initWithAirPlayDictionary:"
+ "initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:homeScreenStyleForLayout:"
+ "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:"
+ "initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:"
+ "initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:carCapabilities:"
+ "initWithPropertySupplier:screenType:carCapabilities:"
+ "initWithPunchThroughIDs:"
+ "initWithScreenInfo:"
+ "initWithSession:"
+ "initWithStyleType:styleVariant:"
+ "initWithStyleType:styleVariant:variation:luminance:saturation:"
+ "initWithVehicleIdentifier:"
+ "initWithVisiblePixelFrame:safeAreaPixelFrame:"
+ "isHeuristicScalable"
+ "isRemoteDeviceConnected"
+ "isSessionDependentPolicy"
+ "kCRPunchThroughIdentifiersKey"
+ "licensesText call failed: %@"
+ "licensesText call failed: %{public}@"
+ "liveActivitiesDisabled"
+ "luminance"
+ "luminanceKey"
+ "no source app for CarEntityHasScreenForAirPlayVideo"
+ "numberWithDouble:"
+ "oemPunchThroughsAsApp"
+ "optimizedPointScale"
+ "originalPointScale"
+ "pairedVehicleManager"
+ "pointScaleForMode:"
+ "preferredPointScale"
+ "preferredToOriginalScaleRatio"
+ "property_key_BackgroundColor"
+ "property_key_BackgroundColorOverride"
+ "property_key_BackgroundOpacity"
+ "property_key_BackgroundOpacityOverride"
+ "property_key_ClosedCaptionsAndSDH_Enabled"
+ "property_key_FontColor"
+ "property_key_FontColorOverride"
+ "property_key_FontName"
+ "property_key_FontNameOverride"
+ "property_key_FontSize"
+ "property_key_FontSizeOverride"
+ "property_key_TextEdgeStyle"
+ "property_key_TextEdgeStyleOverride"
+ "property_key_TextHighlightColor"
+ "property_key_TextHighlightOpacity"
+ "property_key_TextHighlightOverride"
+ "property_key_TextOpacity"
+ "property_key_TextOpacityOverride"
+ "punchThroughs"
+ "remoteControlSessionStart for channel %{public}@"
+ "remoteDeviceConnected"
+ "safeAreaPixelFrame"
+ "saturation"
+ "saturationKey"
+ "saveViewAreas:forVehicleIdentifier:completion:"
+ "saveViewAreas:forVehicleIdentifier:reply:"
+ "scaledDisplays:withDisplayScaling:reply:"
+ "sendStopSessionWithReason %lu"
+ "sendStopSessionWithReason:"
+ "session:isPlayingVideoFromApp:"
+ "sessionDependentPolicy"
+ "sessionManagement"
+ "sessionManagementInfo"
+ "setAllowBackgroundColorOverride:"
+ "setAllowBackgroundOpacityOverride:"
+ "setAllowFontColorOverride:"
+ "setAllowFontNameOverride:"
+ "setAllowFontSizeOverride:"
+ "setAllowTextEdgeStyleOverride:"
+ "setAllowTextHighlightOverride:"
+ "setAllowTextOpacityOverride:"
+ "setBackgroundColor:"
+ "setBackgroundOpacity:"
+ "setCachedVideoPlaybackAvailable:"
+ "setCanvasOverrideSize:forScreenID:"
+ "setClosedCaptionsEnabled:"
+ "setDiagnosticsEnabled call failed: %@"
+ "setDiagnosticsEnabled succeeded"
+ "setDiagnosticsEnabled:"
+ "setDiagnosticsEnabled: %{public}@"
+ "setDisplayScaleMode:"
+ "setFontColor:"
+ "setFontName:"
+ "setFontSize:"
+ "setHasShownEditWidgetsNotification:"
+ "setHomeScreenStyle:forDisplayWithID:"
+ "setHomeScreenStyleData:"
+ "setLuminance:"
+ "setOemPunchThroughsAsApp:"
+ "setPhysicalSize:"
+ "setPixelSize:"
+ "setRemoteDeviceConnected:"
+ "setSafeAreaPixelFrame:"
+ "setSaturation:"
+ "setScreenType:"
+ "setSessionDependentPolicy:"
+ "setSquaredPixelSize:"
+ "setStyleType:"
+ "setStyleVariant:"
+ "setSubtitleSettings call failed: %@"
+ "setSubtitleSettings succeeded"
+ "setSubtitleSettings:"
+ "setSubtitleSettings: %{public}@"
+ "setSupportsAutomakerAppService:"
+ "setSupportsVideo:"
+ "setTextEdgeStyle:"
+ "setTextHighlightColor:"
+ "setTextHighlightOpacity:"
+ "setTextOpacity:"
+ "setTextSizePreference:"
+ "setVariation:"
+ "setVideoDiagnosticsEnabled:"
+ "setVideoDiagnosticsEnabled:forVehicleIdentifier:reply:"
+ "setVideoSubtitleSettings:forVehicleIdentifier:reply:"
+ "setViewAreas:"
+ "setVisiblePixelFrame:"
+ "setZoomFactor:"
+ "size != nil"
+ "starting video playback for app: %@"
+ "stopSession"
+ "stopSessionWithSessionIdentifier:reason:reply:"
+ "styleType"
+ "styleTypeKey"
+ "styleVariant"
+ "styleVariantKey"
+ "subtitle settings missing bool value for: %{public}@"
+ "subtitle settings missing int value for: %{public}@"
+ "subtitleSettings"
+ "subtitleSettings call failed: %@"
+ "subtitleSettings call failed: %{public}@"
+ "subtitleSettings: %{public}@"
+ "supportedStopSessionDisconnectReasons"
+ "supportsAutomakerAppService"
+ "supportsFileTransfer"
+ "supportsStopSession"
+ "supportsStopSessionDisconnectForThisDrive"
+ "supportsVideo"
+ "syncFetchViewAreasForVehicleIdentifier:completion:"
+ "textEdgeStyle"
+ "textHighlightColor"
+ "textHighlightOpacity"
+ "textOpacity"
+ "textSizePreference"
+ "themeDataWithCurrentHomeScreenStyle:"
+ "unsignedLongLongValue"
+ "v24@?0@\"CRSubtitleSettings\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"CARSession\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"CRSubtitleSettings\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
+ "v32@0:8{CGSize=dd}16"
+ "v36@0:8@16B24@?28"
+ "v36@0:8B16@\"NSUUID\"20@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@\"CRSubtitleSettings\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSArray\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8{CGSize=dd}16@32"
+ "variation"
+ "variationKey"
+ "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@\nzoomFactor = %@"
+ "vehicleID"
+ "video playback availability changed, now available: %@"
+ "video2"
+ "video2Info"
+ "videoAnalyticsForVehicleIdentifier:reply:"
+ "videoDiagnosticsEnabled"
+ "videoDiagnosticsEnabledForVehicleIdentifier:reply:"
+ "videoLicensesTextForVehicleIdentifier:reply:"
+ "videoPlaybackAvailable"
+ "videoPlaybackSupported"
+ "videoSubtitleSettingsForVehicleIdentifier:reply:"
+ "visiblePixelFrame"
+ "zoomFactor"
+ "{CGSize=dd}24@0:8q16"
+ "\xf0\xf01"
- "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, supportsLoD: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
- "%@ {currentLayoutID: %@ paletteIDForLayout: %@ wallpaperForLayout: %@}"
- "+[CRCarPlayCapabilities newCapabilitiesFromGlobalDomain]"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %@, userInterfaceStyle = %@, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@"
- "<%@: %p> version = %@, disabledFeature = %@, nowPlayingAlbumArtMode = %ld, userInterfaceStyle = %ld, viewAreaInset = %@, dashboardRoundedCorners = %@, userInfo = %@, persisted = %@"
- "@104@0:8@16@24@32q40@48@56@64@72B80@84@92B100"
- "@32@0:8@?16Q24"
- "@80@0:8@?16Q24{NSEdgeInsets=dddd}32@64@72"
- "HWModelStr"
- "fetchCarCapabilities"
- "initWithCurrentLayoutID:paletteIDForLayout:wallpaperForLayout:"
- "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:"
- "initWithPropertySupplier:screenType:"
- "initWithPropertySupplier:screenType:additionalInsets:displayDictionary:physicalDisplay:"
- "newCapabilitiesFromGlobalDomain"
- "scaledDisplays:reply:"
- "vehicle identifier = %@\nplist version = %@\ndisabledFeature mask = %@\nnowPlayingAlbumArtMode = %@\nuserInterfaceStyle = %@\nviewAreaInset = %@\ndashboardRoundedCorners = %@\nuserInfo = %@, persisted = %@"

```
