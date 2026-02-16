## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-746.24.2.0.0
-  __TEXT.__text: 0x58ec8
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x5dbc
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x56f1
-  __TEXT.__oslogstring: 0x64aa
-  __TEXT.__gcc_except_tab: 0xa50
-  __TEXT.__ustring: 0x24
+774.8.0.0.0
+  __TEXT.__text: 0x5dbb4
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_methlist: 0x6244
+  __TEXT.__const: 0x41a
+  __TEXT.__gcc_except_tab: 0xa20
+  __TEXT.__oslogstring: 0x648a
+  __TEXT.__cstring: 0x549d
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__swift5_typeref: 0x91
-  __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x6e
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_fieldmd: 0xac
-  __TEXT.__unwind_info: 0x18e0
-  __TEXT.__objc_classname: 0xae7
-  __TEXT.__objc_methname: 0x107bf
-  __TEXT.__objc_methtype: 0x23bc
-  __TEXT.__objc_stubs: 0x9580
-  __DATA_CONST.__got: 0x788
-  __DATA_CONST.__const: 0x1ec0
-  __DATA_CONST.__objc_classlist: 0x248
+  __TEXT.__swift5_typeref: 0x7e
+  __TEXT.__constg_swiftt: 0xd8
+  __TEXT.__swift5_reflstr: 0x23
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__eh_frame: 0x80
+  __TEXT.__objc_classname: 0xbc3
+  __TEXT.__objc_methname: 0x11101
+  __TEXT.__objc_methtype: 0x2613
+  __TEXT.__objc_stubs: 0x9640
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x1f58
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3498
+  __DATA_CONST.__objc_selrefs: 0x3558
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x740
-  __AUTH_CONST.__const: 0x1b50
-  __AUTH_CONST.__cfstring: 0x5980
-  __AUTH_CONST.__objc_const: 0xee98
-  __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x10c0
-  __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x708
-  __DATA.__data: 0x1098
-  __DATA.__bss: 0x8d0
-  __DATA.__common: 0x18
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0x808
+  __AUTH_CONST.__const: 0x1a28
+  __AUTH_CONST.__cfstring: 0x5780
+  __AUTH_CONST.__objc_const: 0xf9e0
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x11d8
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x778
+  __DATA.__data: 0x10c0
+  __DATA.__bss: 0x690
   __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
+  - /System/Library/PrivateFrameworks/CarPlayDisplayUtils.framework/CarPlayDisplayUtils
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IAP.framework/IAP
+  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EEA9DA44-1E5B-30B7-B9DF-15522209B24D
-  Functions: 2778
-  Symbols:   9116
-  CStrings:  5010
+  UUID: 25399FB9-8F12-3504-B05E-AF0F25279A99
+  Functions: 2915
+  Symbols:   9491
+  CStrings:  5038
 
Symbols:
+ +[CARPrototypePref overrideBundleIDsForAppIntentsTesting]
+ +[CARPrototypePref overrideBundleIDsForAppIntentsTesting].cold.1
+ +[CARPrototypePref rightHandDrive]
+ +[CARPrototypePref rightHandDrive].cold.1
+ +[CARPrototypePref splitViewEnabled]
+ +[CARPrototypePref splitViewEnabled].cold.1
+ +[CRCarPlayAppPolicyEvaluator isLinkServicesLinked]
+ +[CRCertificationOverridesClient fetchEnhancedSiriOverridesWithCompletion:]
+ +[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]
+ +[CREnhancedSiriOverrides supportsSecureCoding]
+ +[CRSubtitleSettings _defaultStyleID]
+ +[CRSubtitleStyle supportsSecureCoding]
+ +[CRSubtitleStylesManager availableStyles]
+ +[CRSubtitleStylesManager deleteUserCreatedStyle:]
+ +[CRSubtitleStylesManager saveUserCreatedStyle:]
+ -[CARConnectionTimeStore sendConnectionSessionFailureInformation:completion:]
+ -[CARScreenInfo debugDescription]
+ -[CARScreenInfo(CRDisplayScaling) canvasPixelSizeForDisplayScaleMode:pointScale:]
+ -[CARScreenInfo(CRDisplayScaling) displayScaleDescription]
+ -[CARScreenInfo(CRDisplayScaling) displayScaleInfo]
+ -[CARScreenInfo(CRDisplayScaling) matchesScaleMode:canvasSize:pointScale:]
+ -[CARScreenInfo(CRDisplayScaling) resolvedDisplayModeWithMode:]
+ -[CARSession takeScreenForAirPlayOverlayClient:reason:]
+ -[CARSession videoPlayerVersion]
+ -[CARSessionConfiguration dolbyAtmosAudioSupported]
+ -[CARSessionConfiguration spatialAudioSupported]
+ -[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]
+ -[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]
+ -[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]
+ -[CARSessionRequestClient applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:]
+ -[CARSessionRequestClient startAdvertisingCarPlayControlForUSBWithHost:]
+ -[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:host:]
+ -[CARSessionRequestHandlerProxy service_applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:reply:]
+ -[CARSessionRequestHandlerProxy service_startAdvertisingCarPlayControlForUSBWithHost:withReply:]
+ -[CARSessionRequestHandlerProxy service_startAdvertisingCarPlayControlForWiFiUUID:host:reply:]
+ -[CARSessionRequestHost displayConfiguration]
+ -[CARSessionRequestHost displayScaleMode]
+ -[CARSessionRequestHost initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:displayScaleMode:zoomFactor:]
+ -[CARSessionRequestHost setDisplayScaleMode:]
+ -[CARSessionRequestHost setZoomFactor:]
+ -[CARSessionRequestHost zoomFactor]
+ -[CRCarPlayAppDeclaration setSupportsVoiceConversational:]
+ -[CRCarPlayAppDeclaration supportsVoiceConversational]
+ -[CRCarPlayAppPolicyEvaluator applicationConformsToIntentsSchemaIdentifier:bundleIdentifier:]
+ -[CRCarPlayAppPolicyEvaluator provider]
+ -[CREnhancedSiriOverrides .cxx_destruct]
+ -[CREnhancedSiriOverrides description]
+ -[CREnhancedSiriOverrides encodeWithCoder:]
+ -[CREnhancedSiriOverrides initWithCoder:]
+ -[CREnhancedSiriOverrides initWithVoiceTriggerMode:timestampOffset:language:]
+ -[CREnhancedSiriOverrides language]
+ -[CREnhancedSiriOverrides timestampOffset]
+ -[CREnhancedSiriOverrides voiceTriggerMode]
+ -[CRSubtitleSettings .cxx_destruct]
+ -[CRSubtitleSettings selectedStyleID]
+ -[CRSubtitleSettings setSelectedStyleID:]
+ -[CRSubtitleStyle .cxx_destruct]
+ -[CRSubtitleStyle allowBackgroundColorOverride]
+ -[CRSubtitleStyle allowBackgroundOpacityOverride]
+ -[CRSubtitleStyle allowFontColorOverride]
+ -[CRSubtitleStyle allowFontNameOverride]
+ -[CRSubtitleStyle allowFontSizeOverride]
+ -[CRSubtitleStyle allowTextEdgeStyleOverride]
+ -[CRSubtitleStyle allowTextHighlightOverride]
+ -[CRSubtitleStyle allowTextOpacityOverride]
+ -[CRSubtitleStyle backgroundColor]
+ -[CRSubtitleStyle backgroundOpacity]
+ -[CRSubtitleStyle copyWithZone:]
+ -[CRSubtitleStyle cornerRadius]
+ -[CRSubtitleStyle dictionaryRepresentation]
+ -[CRSubtitleStyle displayName]
+ -[CRSubtitleStyle encodeWithCoder:]
+ -[CRSubtitleStyle fontColor]
+ -[CRSubtitleStyle fontName]
+ -[CRSubtitleStyle fontSize]
+ -[CRSubtitleStyle initWithCoder:]
+ -[CRSubtitleStyle initWithDictionaryRepresentation:]
+ -[CRSubtitleStyle isUserCreated]
+ -[CRSubtitleStyle setAllowBackgroundColorOverride:]
+ -[CRSubtitleStyle setAllowBackgroundOpacityOverride:]
+ -[CRSubtitleStyle setAllowFontColorOverride:]
+ -[CRSubtitleStyle setAllowFontNameOverride:]
+ -[CRSubtitleStyle setAllowFontSizeOverride:]
+ -[CRSubtitleStyle setAllowTextEdgeStyleOverride:]
+ -[CRSubtitleStyle setAllowTextHighlightOverride:]
+ -[CRSubtitleStyle setAllowTextOpacityOverride:]
+ -[CRSubtitleStyle setBackgroundColor:]
+ -[CRSubtitleStyle setBackgroundOpacity:]
+ -[CRSubtitleStyle setCornerRadius:]
+ -[CRSubtitleStyle setDisplayName:]
+ -[CRSubtitleStyle setFontColor:]
+ -[CRSubtitleStyle setFontName:]
+ -[CRSubtitleStyle setFontSize:]
+ -[CRSubtitleStyle setTextEdgeStyle:]
+ -[CRSubtitleStyle setTextHighlightColor:]
+ -[CRSubtitleStyle setTextHighlightOpacity:]
+ -[CRSubtitleStyle setTextOpacity:]
+ -[CRSubtitleStyle setUniqueID:]
+ -[CRSubtitleStyle setUserCreated:]
+ -[CRSubtitleStyle textEdgeStyle]
+ -[CRSubtitleStyle textHighlightColor]
+ -[CRSubtitleStyle textHighlightOpacity]
+ -[CRSubtitleStyle textOpacity]
+ -[CRSubtitleStyle uniqueID]
+ -[CRVehicle completedFirstConnection]
+ -[CRVehicle setCompletedFirstConnection:]
+ -[CRVehicle setSupportsDolbyAtmos:]
+ -[CRVehicle setSupportsEnhancedSiriVoice:]
+ -[CRVehicle setSupportsLiveActivities:]
+ -[CRVehicle setSupportsSpatialAudio:]
+ -[CRVehicle supportsDolbyAtmos]
+ -[CRVehicle supportsEnhancedSiriVoice]
+ -[CRVehicle supportsLiveActivities]
+ -[CRVehicle supportsSpatialAudio]
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table122
+ GCC_except_table127
+ GCC_except_table145
+ GCC_except_table168
+ GCC_except_table174
+ GCC_except_table200
+ _AppIntentSchemaIdentifierSendMessageIntent
+ _AppIntentSchemaIdentifierStartCallIntent
+ _CARkAPEndpointInfoResponseKey_AudioFormats
+ _CARkAPEndpointInfoResponseKey_MainBufferedInfo
+ _CARkAudioFormats_Extended
+ _CARkMainBufferedAudio_DCX
+ _CRFetchScaledDisplaysForDisplayScaleMode
+ _CRPointScaleOverride
+ _CRScaledDisplaysWithDisplayMode
+ _CRScaledDisplaysWithDisplayMode.cold.1
+ _CRScaledDisplaysWithDisplayMode.cold.2
+ _CarVideoLogging
+ _CarVideoLogging.cold.1
+ _CarVideoLogging.facility
+ _CarVideoLogging.onceToken
+ _FigEndpointScreenInfoKey_PhysicalSize
+ _FigEndpointScreenInfoKey_PixelSize
+ _OBJC_CLASS_$_CARSessionRequestBonjourHost
+ _OBJC_CLASS_$_CARSessionRequestDisplayConfiguration
+ _OBJC_CLASS_$_CREnhancedSiriOverrides
+ _OBJC_CLASS_$_CRSubtitleStyle
+ _OBJC_CLASS_$_CRSubtitleStylesManager
+ _OBJC_CLASS_$_LNActionMetadata
+ _OBJC_CLASS_$_LNMetadataProvider
+ _OBJC_CLASS_$__TtC6CarKit18CRDisplayScaleInfo
+ _OBJC_IVAR_$_CARSessionConfiguration._dolbyAtmosAudioSupported
+ _OBJC_IVAR_$_CARSessionConfiguration._spatialAudioSupported
+ _OBJC_IVAR_$_CARSessionRequestHost._displayConfiguration
+ _OBJC_IVAR_$_CARSessionRequestHost._displayScaleMode
+ _OBJC_IVAR_$_CARSessionRequestHost._zoomFactor
+ _OBJC_IVAR_$_CRCarPlayAppDeclaration._supportsVoiceConversational
+ _OBJC_IVAR_$_CRCarPlayAppPolicyEvaluator._provider
+ _OBJC_IVAR_$_CREnhancedSiriOverrides._language
+ _OBJC_IVAR_$_CREnhancedSiriOverrides._timestampOffset
+ _OBJC_IVAR_$_CREnhancedSiriOverrides._voiceTriggerMode
+ _OBJC_IVAR_$_CRSubtitleSettings._selectedStyleID
+ _OBJC_IVAR_$_CRSubtitleStyle._allowBackgroundColorOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowBackgroundOpacityOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowFontColorOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowFontNameOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowFontSizeOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowTextEdgeStyleOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowTextHighlightOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._allowTextOpacityOverride
+ _OBJC_IVAR_$_CRSubtitleStyle._backgroundColor
+ _OBJC_IVAR_$_CRSubtitleStyle._backgroundOpacity
+ _OBJC_IVAR_$_CRSubtitleStyle._cornerRadius
+ _OBJC_IVAR_$_CRSubtitleStyle._displayName
+ _OBJC_IVAR_$_CRSubtitleStyle._fontColor
+ _OBJC_IVAR_$_CRSubtitleStyle._fontName
+ _OBJC_IVAR_$_CRSubtitleStyle._fontSize
+ _OBJC_IVAR_$_CRSubtitleStyle._textEdgeStyle
+ _OBJC_IVAR_$_CRSubtitleStyle._textHighlightColor
+ _OBJC_IVAR_$_CRSubtitleStyle._textHighlightOpacity
+ _OBJC_IVAR_$_CRSubtitleStyle._textOpacity
+ _OBJC_IVAR_$_CRSubtitleStyle._uniqueID
+ _OBJC_IVAR_$_CRSubtitleStyle._userCreated
+ _OBJC_IVAR_$_CRVehicle._completedFirstConnection
+ _OBJC_IVAR_$_CRVehicle._supportsDolbyAtmos
+ _OBJC_IVAR_$_CRVehicle._supportsEnhancedSiriVoice
+ _OBJC_IVAR_$_CRVehicle._supportsLiveActivities
+ _OBJC_IVAR_$_CRVehicle._supportsSpatialAudio
+ _OBJC_METACLASS_$_CARSessionRequestBonjourHost
+ _OBJC_METACLASS_$_CARSessionRequestDisplayConfiguration
+ _OBJC_METACLASS_$_CREnhancedSiriOverrides
+ _OBJC_METACLASS_$_CRSubtitleStyle
+ _OBJC_METACLASS_$_CRSubtitleStylesManager
+ _OBJC_METACLASS_$__TtC6CarKit18CRDisplayScaleInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __CLASS_METHODS_CARSessionRequestBonjourHost
+ __CLASS_METHODS_CARSessionRequestDisplayConfiguration
+ __CLASS_PROPERTIES_CARSessionRequestBonjourHost
+ __CLASS_PROPERTIES_CARSessionRequestDisplayConfiguration
+ __DATA_CARSessionRequestBonjourHost
+ __DATA_CARSessionRequestDisplayConfiguration
+ __DATA__TtC6CarKit18CRDisplayScaleInfo
+ __INSTANCE_METHODS_CARSessionRequestBonjourHost
+ __INSTANCE_METHODS_CARSessionRequestDisplayConfiguration
+ __IVARS_CARSessionRequestBonjourHost
+ __IVARS_CARSessionRequestDisplayConfiguration
+ __IVARS__TtC6CarKit18CRDisplayScaleInfo
+ __METACLASS_DATA_CARSessionRequestBonjourHost
+ __METACLASS_DATA_CARSessionRequestDisplayConfiguration
+ __METACLASS_DATA__TtC6CarKit18CRDisplayScaleInfo
+ __OBJC_$_CLASS_METHODS_CREnhancedSiriOverrides
+ __OBJC_$_CLASS_METHODS_CRSubtitleStyle
+ __OBJC_$_CLASS_METHODS_CRSubtitleStylesManager
+ __OBJC_$_CLASS_PROP_LIST_CREnhancedSiriOverrides
+ __OBJC_$_CLASS_PROP_LIST_CRSubtitleStyle
+ __OBJC_$_INSTANCE_METHODS_CREnhancedSiriOverrides
+ __OBJC_$_INSTANCE_METHODS_CRSubtitleStyle
+ __OBJC_$_INSTANCE_METHODS__TtC6CarKit18CRDisplayScaleInfo(CarKit)
+ __OBJC_$_INSTANCE_VARIABLES_CREnhancedSiriOverrides
+ __OBJC_$_INSTANCE_VARIABLES_CRSubtitleStyle
+ __OBJC_$_PROP_LIST_CREnhancedSiriOverrides
+ __OBJC_$_PROP_LIST_CRSubtitleStyle
+ __OBJC_CLASS_PROTOCOLS_$_CREnhancedSiriOverrides
+ __OBJC_CLASS_PROTOCOLS_$_CRSubtitleStyle
+ __OBJC_CLASS_RO_$_CREnhancedSiriOverrides
+ __OBJC_CLASS_RO_$_CRSubtitleStyle
+ __OBJC_CLASS_RO_$_CRSubtitleStylesManager
+ __OBJC_METACLASS_RO_$_CREnhancedSiriOverrides
+ __OBJC_METACLASS_RO_$_CRSubtitleStyle
+ __OBJC_METACLASS_RO_$_CRSubtitleStylesManager
+ __PROPERTIES_CARSessionRequestBonjourHost
+ __PROPERTIES_CARSessionRequestDisplayConfiguration
+ __PROTOCOLS_CARSessionRequestBonjourHost
+ __PROTOCOLS_CARSessionRequestBonjourHost.7
+ __PROTOCOLS_CARSessionRequestDisplayConfiguration
+ __PROTOCOLS_CARSessionRequestDisplayConfiguration.2
+ ___100-[CARSessionRequestClient applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:]_block_invoke
+ ___100-[CARSessionRequestClient applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:]_block_invoke.82
+ ___100-[CARSessionRequestClient applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:]_block_invoke.cold.1
+ ___24-[CARSession suggestUI:]_block_invoke.430
+ ___34+[CARPrototypePref rightHandDrive]_block_invoke
+ ___34+[CARPrototypePref rightHandDrive]_block_invoke_2
+ ___36+[CARPrototypePref splitViewEnabled]_block_invoke
+ ___36+[CARPrototypePref splitViewEnabled]_block_invoke_2
+ ___41-[CARSessionRequestClient cancelRequests]_block_invoke.77
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke.20
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke.20.cold.1
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke.cold.1
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.36
+ ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.36.cold.1
+ ___57+[CARPrototypePref overrideBundleIDsForAppIntentsTesting]_block_invoke
+ ___57+[CARPrototypePref overrideBundleIDsForAppIntentsTesting]_block_invoke_2
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.267
+ ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.267.cold.1
+ ___59-[CARSessionRequestClient stoppedSessionForHostIdentifier:]_block_invoke.49
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.268
+ ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.268.cold.1
+ ___62-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSB]_block_invoke.55
+ ___62-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSB]_block_invoke.55.cold.1
+ ___63-[CARSessionRequestClient startAdvertisingCarPlayControlForUSB]_block_invoke.54
+ ___65-[CARSessionRequestClient prepareForRemovingWiFiUUID:completion:]_block_invoke.74
+ ___66-[CARConnectionTimeStore removeConnectionEventsBefore:completion:]_block_invoke.270
+ ___66-[CARConnectionTimeStore removeConnectionEventsBefore:completion:]_block_invoke.270.cold.1
+ ___68-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:]_block_invoke.57
+ ___68-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:]_block_invoke.57.cold.1
+ ___69-[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke.64
+ ___70+[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]_block_invoke
+ ___70+[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]_block_invoke.74
+ ___70+[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]_block_invoke.74.cold.1
+ ___70+[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]_block_invoke_2
+ ___70+[CRCertificationOverridesClient setEnhancedSiriOverrides:completion:]_block_invoke_2.cold.1
+ ___71-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]_block_invoke
+ ___71-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]_block_invoke.61
+ ___71-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]_block_invoke.61.cold.1
+ ___71-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]_block_invoke_2
+ ___71-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSBWithHost:]_block_invoke_2.cold.1
+ ___72-[CARSessionRequestClient startAdvertisingCarPlayControlForUSBWithHost:]_block_invoke
+ ___72-[CARSessionRequestClient startAdvertisingCarPlayControlForUSBWithHost:]_block_invoke.59
+ ___72-[CARSessionRequestClient startAdvertisingCarPlayControlForUSBWithHost:]_block_invoke.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.635
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.635.cold.1
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.635.cold.2
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.640
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.644
+ ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.645
+ ___73-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]_block_invoke
+ ___73-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]_block_invoke.64
+ ___73-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]_block_invoke.64.cold.1
+ ___73-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]_block_invoke_2
+ ___73-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:host:]_block_invoke_2.cold.1
+ ___74-[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:host:]_block_invoke
+ ___74-[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:host:]_block_invoke.69
+ ___74-[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:host:]_block_invoke.cold.1
+ ___75+[CRCertificationOverridesClient fetchEnhancedSiriOverridesWithCompletion:]_block_invoke
+ ___75+[CRCertificationOverridesClient fetchEnhancedSiriOverridesWithCompletion:]_block_invoke.78
+ ___75+[CRCertificationOverridesClient fetchEnhancedSiriOverridesWithCompletion:]_block_invoke.78.cold.1
+ ___75+[CRCertificationOverridesClient fetchEnhancedSiriOverridesWithCompletion:]_block_invoke_2
+ ___75-[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]_block_invoke
+ ___75-[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]_block_invoke.68
+ ___75-[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]_block_invoke.68.cold.1
+ ___75-[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]_block_invoke_2
+ ___75-[CARSessionRequestAgent restrictedModeAuthorizationsForCertificateSerial:]_block_invoke_2.cold.1
+ ___77-[CARConnectionTimeStore sendConnectionSessionFailureInformation:completion:]_block_invoke
+ ___77-[CARConnectionTimeStore sendConnectionSessionFailureInformation:completion:]_block_invoke.269
+ ___77-[CARConnectionTimeStore sendConnectionSessionFailureInformation:completion:]_block_invoke.269.cold.1
+ ___77-[CARSessionRequestClient startSessionWithHost:requestIdentifier:completion:]_block_invoke.45
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.68
+ ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.68.cold.1
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.71
+ ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.71.cold.1
+ ___CARHandleSuggestUI_block_invoke.426
+ ___CRCollectCarPlayDiagnostics_block_invoke.166
+ ___CRCollectVehicleLogs_block_invoke.170
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.174
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.174.cold.1
+ ___CRPostBannerToPhone_block_invoke.158
+ ___CRServiceConnectionPerform_block_invoke.122
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.184
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.184.cold.1
+ ___CarVideoLogging_block_invoke
+ ___block_descriptor_40_e8_32s_e41_"NSString"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e45_v24?0"CREnhancedSiriOverrides"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32r40r_e27_v16?0"<CRCarKitService>"8lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e53_v28?0B8"CARSessionRequestBonjourHost"12"NSError"20lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e20_v24?0Q8"NSError"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e27_v16?0"<CRCarKitService>"8ls32l8r40l8r48l8
+ ___block_literal_global.169
+ ___block_literal_global.173
+ ___block_literal_global.183
+ ___block_literal_global.204
+ ___block_literal_global.221
+ ___block_literal_global.227
+ ___block_literal_global.232
+ ___block_literal_global.237
+ ___block_literal_global.317
+ ___block_literal_global.425
+ ___block_literal_global.435
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.449
+ ___block_literal_global.451
+ ___block_literal_global.459
+ ___block_literal_global.461
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.476
+ ___block_literal_global.48
+ ___block_literal_global.53
+ ___block_literal_global.58
+ ___block_literal_global.61
+ ___block_literal_global.63
+ ___block_literal_global.638
+ ___block_literal_global.650
+ ___block_literal_global.66
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.73
+ ___block_literal_global.743
+ ___block_literal_global.81
+ ___chkstk_darwin
+ _kCRCarPlayEntitlementVoiceConversational
+ _kFigEndpointProperty_ExternalPlaybackCapabilities
+ _keypath_get_selector_displayConfiguration
+ _keypath_get_selector_displayScaleMode
+ _keypath_get_selector_zoomFactor
+ _objc_msgSend$_defaultStyleID
+ _objc_msgSend$actionsForSchemaIdentifier:error:
+ _objc_msgSend$applicationConformsToIntentsSchemaIdentifier:bundleIdentifier:
+ _objc_msgSend$applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:
+ _objc_msgSend$canvasPixelSizeWithDisplayScaleMode:pointScale:
+ _objc_msgSend$completedFirstConnection
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$displayConfiguration
+ _objc_msgSend$displayScaleDescription
+ _objc_msgSend$displayScaleInfo
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$fetchCarPlayControlAdvertisingForUSBWithReply:
+ _objc_msgSend$fetchCarPlayControlAdvertisingForWiFiUUID:reply:
+ _objc_msgSend$fetchEnhancedSiriOverridesWithCompletion:
+ _objc_msgSend$initWithBSXPCCoder:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithDictionary:screenType:zoomPercent:error:
+ _objc_msgSend$initWithDisplayConfiguration:
+ _objc_msgSend$initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:displayScaleMode:zoomFactor:
+ _objc_msgSend$initWithDisplayScaleMode:zoomFactor:
+ _objc_msgSend$initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomSetting:pointScaleOverride:
+ _objc_msgSend$initWithStyleType:styleVariant:
+ _objc_msgSend$initWithStyleType:styleVariant:variation:luminance:saturation:
+ _objc_msgSend$initWithVoiceTriggerMode:timestampOffset:language:
+ _objc_msgSend$internalSettingsState
+ _objc_msgSend$isLinkServicesLinked
+ _objc_msgSend$language
+ _objc_msgSend$luminance
+ _objc_msgSend$luminanceKey
+ _objc_msgSend$matchesWithScaleMode:canvasSize:pointScale:
+ _objc_msgSend$preferredPointScaleFor:
+ _objc_msgSend$resolvedDisplayModeWithMode:
+ _objc_msgSend$restrictedModeAuthorizationsForCertificateSerial:reply:
+ _objc_msgSend$saturation
+ _objc_msgSend$saturationKey
+ _objc_msgSend$sendConnectionSessionFailureInformation:completion:
+ _objc_msgSend$service_applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:reply:
+ _objc_msgSend$service_startAdvertisingCarPlayControlForUSBWithHost:withReply:
+ _objc_msgSend$service_startAdvertisingCarPlayControlForWiFiUUID:host:reply:
+ _objc_msgSend$setCompletedFirstConnection:
+ _objc_msgSend$setDisplayConfiguration:
+ _objc_msgSend$setEnhancedSiriOverrides:completion:
+ _objc_msgSend$setLuminance:
+ _objc_msgSend$setSaturation:
+ _objc_msgSend$setSelectedStyleID:
+ _objc_msgSend$setStyleType:
+ _objc_msgSend$setStyleVariant:
+ _objc_msgSend$setSupportsDolbyAtmos:
+ _objc_msgSend$setSupportsEnhancedSiriVoice:
+ _objc_msgSend$setSupportsLiveActivities:
+ _objc_msgSend$setSupportsSpatialAudio:
+ _objc_msgSend$setSupportsVoiceConversational:
+ _objc_msgSend$setVariation:
+ _objc_msgSend$startAdvertisingCarPlayControlForUSBWithHost:
+ _objc_msgSend$startAdvertisingCarPlayControlForWiFiUUID:host:
+ _objc_msgSend$styleType
+ _objc_msgSend$styleTypeKey
+ _objc_msgSend$styleVariant
+ _objc_msgSend$styleVariantKey
+ _objc_msgSend$supportsDolbyAtmos
+ _objc_msgSend$supportsEnhancedSiriVoice
+ _objc_msgSend$supportsLiveActivities
+ _objc_msgSend$supportsSpatialAudio
+ _objc_msgSend$supportsVoiceConversational
+ _objc_msgSend$takeScreenForClient:reason:
+ _objc_msgSend$timestampOffset
+ _objc_msgSend$variation
+ _objc_msgSend$variationKey
+ _objc_msgSend$voiceTriggerMode
+ _overrideBundleIDsForAppIntentsTesting._overrideBundleIDsForAppIntentsTesting
+ _overrideBundleIDsForAppIntentsTesting.onceToken
+ _rightHandDrive._rightHandDrive
+ _rightHandDrive.onceToken
+ _splitViewEnabled._splitViewEnabled
+ _splitViewEnabled.onceToken
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_deallocPartialClassInstance
+ _swift_errorRelease
+ _swift_getSingletonMetadata
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic Sb
+ _symbolic _____ 19CarPlayDisplayUtils0C9ScaleInfoV
+ _symbolic _____ 6CarKit18CRDisplayScaleInfoC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 19CarPlayDisplayUtils8ViewAreaV
- +[CARDNDUtility sharedInstance]
- +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:]
- +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:].cold.1
- +[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:].cold.2
- -[CARDNDUtility .cxx_destruct]
- -[CARDNDUtility DNDStatus]
- -[CARDNDUtility init]
- -[CARDNDUtility outputFromRhodesUtility]
- -[CARDNDUtility outputFromRhodesUtility].cold.1
- -[CARDNDUtility setDNDStatus:]
- -[CARScreenInfo(CRDisplayScaling) canvasPixelSizeForDisplayScaleMode:]
- -[CARScreenInfo(CRDisplayScaling) defaultDisplayMode]
- -[CARScreenInfo(CRDisplayScaling) displayScaleModesForCanvasPixelSize:]
- -[CARSessionRequestHost initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:]
- -[CRDisplayScaleInfo .cxx_destruct]
- -[CRDisplayScaleInfo _allowedScaleModes]
- -[CRDisplayScaleInfo _heuristicPixelSize]
- -[CRDisplayScaleInfo _minHeightDisplaySize]
- -[CRDisplayScaleInfo _minWidthDisplaySize]
- -[CRDisplayScaleInfo _optimalScaleFactorWithPointScale:]
- -[CRDisplayScaleInfo _pixelSizeByClampingToMinSize:pointScale:]
- -[CRDisplayScaleInfo _scaleMode]
- -[CRDisplayScaleInfo _scaledToOriginalRatio]
- -[CRDisplayScaleInfo allowsSmartZoom]
- -[CRDisplayScaleInfo canvasPixelSizeForDisplayScaleMode:]
- -[CRDisplayScaleInfo defaultDisplayMode]
- -[CRDisplayScaleInfo description]
- -[CRDisplayScaleInfo displayScaleModesForCanvasPixelSize:]
- -[CRDisplayScaleInfo initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:]
- -[CRDisplayScaleInfo initWithScreenInfo:]
- -[CRDisplayScaleInfo isHeuristicScalable]
- -[CRDisplayScaleInfo optimizedPointScaleForMode:]
- -[CRDisplayScaleInfo originalPointScale]
- -[CRDisplayScaleInfo physicalSize]
- -[CRDisplayScaleInfo pixelSize]
- -[CRDisplayScaleInfo preferredPointScaleForMode:]
- -[CRDisplayScaleInfo preferredToOriginalScaleRatioForMode:]
- -[CRDisplayScaleInfo screenType]
- -[CRDisplayScaleInfo setPhysicalSize:]
- -[CRDisplayScaleInfo setPixelSize:]
- -[CRDisplayScaleInfo setScreenType:]
- -[CRDisplayScaleInfo setSquaredPixelSize:]
- -[CRDisplayScaleInfo setViewAreas:]
- -[CRDisplayScaleInfo setZoomFactor:]
- -[CRDisplayScaleInfo squaredPixelSize]
- -[CRDisplayScaleInfo viewAreas]
- -[CRDisplayScaleInfo zoomFactor]
- -[CRViewArea description]
- -[CRViewArea initWithAirPlayDictionary:]
- -[CRViewArea initWithVisiblePixelFrame:safeAreaPixelFrame:]
- -[CRViewArea safeAreaPixelFrame]
- -[CRViewArea setSafeAreaPixelFrame:]
- -[CRViewArea setVisiblePixelFrame:]
- -[CRViewArea visiblePixelFrame]
- GCC_except_table103
- GCC_except_table107
- GCC_except_table113
- GCC_except_table121
- GCC_except_table126
- GCC_except_table143
- GCC_except_table166
- GCC_except_table172
- GCC_except_table198
- _BSStringFromBOOL
- _BSStringFromCGRect
- _CARDatePreferenceDescription._formatter
- _CARDatePreferenceDescription.onceToken
- _CGSizeScaledBy
- _CGSizeSquaredPixelSizeWithPhysicalSize
- _CRAirPlayZoomFactorKey
- _CRCarKitDisplayScaleError
- _CRMinViewAreaPixelSize
- _CRPointScaleWithSize
- _CRScaledDisplaysWithAirplayDisplays.cold.1
- _CRScaledDisplaysWithAirplayDisplays.cold.2
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_CARDNDUtility
- _OBJC_CLASS_$_CMVehicleState
- _OBJC_CLASS_$_CRDisplayScaleInfo
- _OBJC_CLASS_$_CRViewArea
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$__TtC6CarKit14DisplayScaling
- _OBJC_IVAR_$_CARDNDUtility._DNDStatus
- _OBJC_IVAR_$_CRDisplayScaleInfo._physicalSize
- _OBJC_IVAR_$_CRDisplayScaleInfo._pixelSize
- _OBJC_IVAR_$_CRDisplayScaleInfo._screenType
- _OBJC_IVAR_$_CRDisplayScaleInfo._squaredPixelSize
- _OBJC_IVAR_$_CRDisplayScaleInfo._viewAreas
- _OBJC_IVAR_$_CRDisplayScaleInfo._zoomFactor
- _OBJC_IVAR_$_CRViewArea._safeAreaPixelFrame
- _OBJC_IVAR_$_CRViewArea._visiblePixelFrame
- _OBJC_METACLASS_$_CARDNDUtility
- _OBJC_METACLASS_$_CRDisplayScaleInfo
- _OBJC_METACLASS_$_CRViewArea
- _OBJC_METACLASS_$__TtC6CarKit14DisplayScaling
- __CLASS_METHODS__TtC6CarKit14DisplayScaling
- __DATA__TtC6CarKit14DisplayScaling
- __INSTANCE_METHODS__TtC6CarKit14DisplayScaling
- __METACLASS_DATA__TtC6CarKit14DisplayScaling
- __OBJC_$_CLASS_METHODS_CARDNDUtility
- __OBJC_$_CLASS_METHODS_CRDisplayScaleInfo
- __OBJC_$_INSTANCE_METHODS_CARDNDUtility
- __OBJC_$_INSTANCE_METHODS_CRDisplayScaleInfo
- __OBJC_$_INSTANCE_METHODS_CRViewArea
- __OBJC_$_INSTANCE_VARIABLES_CARDNDUtility
- __OBJC_$_INSTANCE_VARIABLES_CRDisplayScaleInfo
- __OBJC_$_INSTANCE_VARIABLES_CRViewArea
- __OBJC_$_PROP_LIST_CARDNDUtility
- __OBJC_$_PROP_LIST_CRDisplayScaleInfo
- __OBJC_$_PROP_LIST_CRViewArea
- __OBJC_CLASS_RO_$_CARDNDUtility
- __OBJC_CLASS_RO_$_CRDisplayScaleInfo
- __OBJC_CLASS_RO_$_CRViewArea
- __OBJC_METACLASS_RO_$_CARDNDUtility
- __OBJC_METACLASS_RO_$_CRDisplayScaleInfo
- __OBJC_METACLASS_RO_$_CRViewArea
- ___24-[CARSession suggestUI:]_block_invoke.427
- ___31+[CARDNDUtility sharedInstance]_block_invoke
- ___40-[CARDNDUtility outputFromRhodesUtility]_block_invoke
- ___40-[CARDNDUtility outputFromRhodesUtility]_block_invoke_2
- ___41-[CARSessionRequestClient cancelRequests]_block_invoke.60
- ___41-[CRDisplayScaleInfo initWithScreenInfo:]_block_invoke
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.75
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.75.cold.1
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.265
- ___57-[CARConnectionTimeStore sendConnectionEvent:completion:]_block_invoke.265.cold.1
- ___59-[CARSessionRequestClient stoppedSessionForHostIdentifier:]_block_invoke.42
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.266
- ___61-[CARConnectionTimeStore syncSendConnectionEvent:completion:]_block_invoke.266.cold.1
- ___62-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSB]_block_invoke.45
- ___62-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForUSB]_block_invoke.45.cold.1
- ___63-[CARSessionRequestClient startAdvertisingCarPlayControlForUSB]_block_invoke.47
- ___65-[CARSessionRequestClient prepareForRemovingWiFiUUID:completion:]_block_invoke.57
- ___66-[CARConnectionTimeStore removeConnectionEventsBefore:completion:]_block_invoke.267
- ___66-[CARConnectionTimeStore removeConnectionEventsBefore:completion:]_block_invoke.267.cold.1
- ___68-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:]_block_invoke.47
- ___68-[CARSessionRequestAgent wantsCarPlayControlAdvertisingForWiFiUUID:]_block_invoke.47.cold.1
- ___69-[CARSessionRequestClient startAdvertisingCarPlayControlForWiFiUUID:]_block_invoke.52
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617.cold.1
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.617.cold.2
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.622
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke.626
- ___73-[CARSessionConfiguration initWithSessionStatusOptions:propertySupplier:]_block_invoke_2.627
- ___77-[CARSessionRequestClient startSessionWithHost:requestIdentifier:completion:]_block_invoke.38
- ___81+[CRDisplayScaleInfo displayScaleInfoWithDictionary:screenType:zoomFactor:error:]_block_invoke
- ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.21
- ___89+[CRCertificationOverridesClient setNextSessionOverrideAirPlayFeatureStrings:completion:]_block_invoke.21.cold.1
- ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.24
- ___94+[CRCertificationOverridesClient fetchNextSessionOverrideAirPlayFeatureStringsWithCompletion:]_block_invoke.24.cold.1
- ___CARDatePreferenceDescription_block_invoke
- ___CARHandleSuggestUI_block_invoke.423
- ___CRCollectCarPlayDiagnostics_block_invoke.161
- ___CRCollectVehicleLogs_block_invoke.165
- ___CRIsPreflightThemeAssetEnabled_block_invoke.169
- ___CRIsPreflightThemeAssetEnabled_block_invoke.169.cold.1
- ___CRPostBannerToPhone_block_invoke.153
- ___CRServiceConnectionPerform_block_invoke.117
- ___CRSetPreflightThemeAssetEnabled_block_invoke.179
- ___CRSetPreflightThemeAssetEnabled_block_invoke.179.cold.1
- ___block_descriptor_32_e22_16?0"NSDictionary"8l
- ___block_descriptor_40_e8_32s_e34_v32?0"CARScreenViewArea"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.168
- ___block_literal_global.178
- ___block_literal_global.194
- ___block_literal_global.230
- ___block_literal_global.235
- ___block_literal_global.26
- ___block_literal_global.303
- ___block_literal_global.41
- ___block_literal_global.422
- ___block_literal_global.432
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.446
- ___block_literal_global.54
- ___block_literal_global.62
- ___block_literal_global.632
- ___block_literal_global.737
- ___swift_allocate_value_buffer
- ___swift_memcpy16_8
- ___swift_memcpy1_1
- ___swift_memcpy41_8
- ___swift_noop_void_return
- ___swift_project_value_buffer
- _associated conformance 6CarKit14DisplayScalingC0D9ExceptionOSHAASQ
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$DNDStatus
- _objc_msgSend$_allowedScaleModes
- _objc_msgSend$_detachObservers
- _objc_msgSend$_minHeightDisplaySize
- _objc_msgSend$_minWidthDisplaySize
- _objc_msgSend$_optimalScaleFactorWithPointScale:
- _objc_msgSend$_pixelSizeByClampingToMinSize:pointScale:
- _objc_msgSend$_scaleMode
- _objc_msgSend$_scaledToOriginalRatio
- _objc_msgSend$appendString:
- _objc_msgSend$canvasPixelSizeForDisplayScaleMode:
- _objc_msgSend$defaultDisplayMode
- _objc_msgSend$disableTimerTimestamp
- _objc_msgSend$displayScaleInfoWithDictionary:screenType:zoomFactor:error:
- _objc_msgSend$displayScaleModesForCanvasPixelSize:
- _objc_msgSend$exceptionPointScaleWithScreenType:physicalSize:pixelSize:
- _objc_msgSend$fetchAutomaticDNDAssertionWithReply:
- _objc_msgSend$fetchAutomaticDNDExitConfirmationWithReply:
- _objc_msgSend$hasAdjustedTriggerMethod
- _objc_msgSend$hasMigratedToDriving
- _objc_msgSend$initWithAirPlayDictionary:
- _objc_msgSend$initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:
- _objc_msgSend$initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:
- _objc_msgSend$initWithScreenInfo:
- _objc_msgSend$initWithVisiblePixelFrame:safeAreaPixelFrame:
- _objc_msgSend$isAutomaticDNDInternalExitConfirmationOverrideEnabledPreference
- _objc_msgSend$isAutomaticDNDInternalForceOverrideEnabledPreference
- _objc_msgSend$isAutomaticDNDInternalShowGeofencingAlertsEnabledPreference
- _objc_msgSend$isAutomaticDNDInternalShowUserAlertsEnabledPreference
- _objc_msgSend$isAvailable
- _objc_msgSend$isExceptionWithScreenType:physicalSize:pixelSize:
- _objc_msgSend$isHeuristicScalable
- _objc_msgSend$optimizedPointScaleForMode:
- _objc_msgSend$originalPointScale
- _objc_msgSend$preferredPointScaleForMode:
- _objc_msgSend$preferredToOriginalScaleRatioForMode:
- _objc_msgSend$safeAreaPixelFrame
- _objc_msgSend$setAllowBackgroundColorOverride:
- _objc_msgSend$setAllowBackgroundOpacityOverride:
- _objc_msgSend$setAllowFontColorOverride:
- _objc_msgSend$setAllowFontNameOverride:
- _objc_msgSend$setAllowFontSizeOverride:
- _objc_msgSend$setAllowTextEdgeStyleOverride:
- _objc_msgSend$setAllowTextHighlightOverride:
- _objc_msgSend$setAllowTextOpacityOverride:
- _objc_msgSend$setBackgroundColor:
- _objc_msgSend$setBackgroundOpacity:
- _objc_msgSend$setDateStyle:
- _objc_msgSend$setFontColor:
- _objc_msgSend$setFontName:
- _objc_msgSend$setFontSize:
- _objc_msgSend$setTextEdgeStyle:
- _objc_msgSend$setTextHighlightColor:
- _objc_msgSend$setTextHighlightOpacity:
- _objc_msgSend$setTextOpacity:
- _objc_msgSend$setTimeStyle:
- _objc_msgSend$squaredPixelSize
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$vehicularHints
- _objc_msgSend$vehicularOperatorState
- _objc_msgSend$vehicularState
- _objc_msgSend$visiblePixelFrame
- _objc_msgSend$zoomFactorHeuristicsWithScreenType:physicalSize:pixelSize:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _sharedInstance.__utility
- _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_getWitnessTable
- _swift_once
- _symbolic Su
- _symbolic _____ 12CoreGraphics7CGFloatV
- _symbolic _____ 6CarKit14DisplayScalingC
- _symbolic _____ 6CarKit14DisplayScalingC0C5SizesV
- _symbolic _____ 6CarKit14DisplayScalingC0D9ExceptionO
- _symbolic _____ So6CGSizeV
- _symbolic _____Sg So6CGSizeV
- _type_layout_string 6CarKit14DisplayScalingC0C5SizesV
- _type_layout_string So6CGSizeV
CStrings:
+ "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, routeSharing: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, supportsEnhancedSiriVoice: %@, supportsDolbyAtmos: %@, supportsSpatialAudio: %@, supportsLiveActivities: %@, albumArtUserPreference: %@,  %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
+ "%@, displayScaleInformation: %@"
+ "%@, identifier: %@, availableInteractionModels: %@, primaryInteractionModel: %@, isLimited: %@, isNightMode: %@, supportsHiFi: %@, maxFPS: %lu, physicalSize: %@, pixelSize: %@, wantsCornerMasks: %@, initialFocusOwner: %@, viewAreas: %@, displayScaleInformation: %@"
+ "@\"CARSessionRequestDisplayConfiguration\""
+ "@\"LNMetadataProvider\""
+ "@\"NSString\"24@?0@\"NSString\"8@\"NSString\"16"
+ "@124@0:8@16@24@32q40@48@56@64@72B80@84@92B100B104q108@116"
+ "@32@0:8q16@24"
+ "@40@0:8q16@24@32"
+ "@80@0:8{CGSize=dd}16{CGSize=dd}32@48Q56@64@72"
+ "B32@0:8@16^@24"
+ "B48@0:8q16{CGSize=dd}24d40"
+ "CARConnectionTimeStore failed with sendConnectionSessionFailureInformation: %@ error: %@"
+ "CARConnectionTimeStore sendConnectionSessionFailureInformation: %@"
+ "CARRightHandDrive"
+ "CARSessionRequestBonjourHost"
+ "CARSessionRequestBonjourHost [displayConfiguration: "
+ "CARSessionRequestDisplayConfiguration"
+ "CARSessionRequestDisplayConfiguration [displayScaleMode: "
+ "CARSplitViewEnabled"
+ "CREnhancedSiriOverrides"
+ "CRFetchScaledDisplaysForDisplayMode: using scale mode: %@, zoomFactor: %@"
+ "CRSubtitleStyle"
+ "CRSubtitleStylesManager"
+ "CarKit.CRDisplayScaleInfo"
+ "CarKit_Private.CARSessionRequestBonjourHost"
+ "CarKit_Private.CARSessionRequestDisplayConfiguration"
+ "DCXEnabled"
+ "Error calling restrictedModeAuthorizationsForCertificateSerial %@"
+ "Error from restrictedModeAuthorizationsForCertificateSerial: %@"
+ "Fetching restrictedModeAuthorizationsForCertificateSerial:%{private}@"
+ "Received applyUpdatedRestrictedModeAuthorizations: %lu forCertificateSerial:%{private}@"
+ "Received startAdvertisingCarPlayControlForWiFiUUID for Wi-Fi UUID: %@, host: %@"
+ "Right Hand Drive"
+ "Split View Enabled"
+ "T@\"CARSessionRequestDisplayConfiguration\",N,&,VdisplayConfiguration"
+ "T@\"CARSessionRequestDisplayConfiguration\",R,N,V_displayConfiguration"
+ "T@\"LNMetadataProvider\",R,N,V_provider"
+ "T@\"NSNumber\",&,N,V_completedFirstConnection"
+ "T@\"NSNumber\",N,&,VzoomFactor"
+ "T@\"NSNumber\",R,C,N,V_timestampOffset"
+ "T@\"NSString\",&,N,V_selectedStyleID"
+ "T@\"NSString\",C,N,V_uniqueID"
+ "T@\"NSString\",R,C,N,V_language"
+ "TB,N,GisUserCreated,V_userCreated"
+ "TB,N,R,VallowsSmartZoom"
+ "TB,N,V_supportsDolbyAtmos"
+ "TB,N,V_supportsEnhancedSiriVoice"
+ "TB,N,V_supportsLiveActivities"
+ "TB,N,V_supportsSpatialAudio"
+ "TB,N,V_supportsVoiceConversational"
+ "TB,R,N,V_dolbyAtmosAudioSupported"
+ "TB,R,N,V_spatialAudioSupported"
+ "Td,N,V_cornerRadius"
+ "Tq,N,VdisplayScaleMode"
+ "Unknown CARScreenType: %s"
+ "VideoBrowse"
+ "[DISPLAY_CONFIGURATION] CARSessionRequestHost encodeWithCoder: encoded displayConfiguration: %@"
+ "[DISPLAY_CONFIGURATION] CARSessionRequestHost initWithCoder: decoded displayConfiguration: %@"
+ "[DISPLAY_CONFIGURATION] CARSessionRequestHost initWithHostProperties: parsed displayScaleMode=%ld from hostProperties"
+ "[DISPLAY_CONFIGURATION] CARSessionRequestHost initWithHostProperties: parsed zoomFactor=%@ from hostProperties"
+ "[DISPLAY_CONFIGURATION] Received startAdvertisingCarPlayControl for USB with host: %@"
+ "[DISPLAY_CONFIGURATION] Received startAdvertisingCarPlayControl with host, but using an old startAdvertisingCarPlayControlForUSB method"
+ "[DISPLAY_CONFIGURATION] Received startAdvertisingCarPlayControlForWiFiUUID for USB with host: %@"
+ "[DISPLAY_CONFIGURATION] Received startAdvertisingCarPlayControlForWiFiUUID with host, but using an old startAdvertisingCarPlayControlForWiFiUUID method"
+ "[DISPLAY_CONFIGURATION] starting CarPlay Control advertising over USB with host: %@"
+ "_TtC6CarKit18CRDisplayScaleInfo"
+ "_completedFirstConnection"
+ "_cornerRadius"
+ "_defaultStyleID"
+ "_displayConfiguration"
+ "_dolbyAtmosAudioSupported"
+ "_language"
+ "_provider"
+ "_selectedStyleID"
+ "_spatialAudioSupported"
+ "_supportsDolbyAtmos"
+ "_supportsEnhancedSiriVoice"
+ "_supportsLiveActivities"
+ "_supportsSpatialAudio"
+ "_supportsVoiceConversational"
+ "_timestampOffset"
+ "_uniqueID"
+ "_userCreated"
+ "a"
+ "actionsForSchemaIdentifier:error:"
+ "applicationConformsToIntentsSchemaIdentifier:bundleIdentifier:"
+ "applyUpdatedRestrictedModeAuthorizations %lu forCertificateSerial:%{private}@"
+ "applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:"
+ "applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:completion:"
+ "audioFormats"
+ "audioOutputFormatsExtended"
+ "availableStyles"
+ "b"
+ "canvasPixelSizeForDisplayScaleMode:pointScale:"
+ "canvasPixelSizeWithDisplayScaleMode:pointScale:"
+ "com.appIntents Bundle Ids Allowed"
+ "com.apple.developer.carplay-voice-based-conversation"
+ "completedFirstConnection"
+ "cornerRadius"
+ "deleteUserCreatedStyle:"
+ "displayConfiguration"
+ "displayScaleDescription"
+ "displayScaleInfo"
+ "dolbyAtmosAudioSupported"
+ "edgeStyle"
+ "fetchCarPlayControlAdvertisingForUSBWithReply:"
+ "fetchCarPlayControlAdvertisingForWiFiUUID:reply:"
+ "fetchEnhancedSiriOverridesWithCompletion"
+ "fetchEnhancedSiriOverridesWithCompletion failed: %{public}@"
+ "fetchEnhancedSiriOverridesWithCompletion:"
+ "fetchEnhancedSiriOverridesWithCompletion: %{public}@ error: %{public}@"
+ "font"
+ "highlightColor"
+ "highlightOpacity"
+ "initWithDictionary:screenType:zoomPercent:error:"
+ "initWithDisplayConfiguration:"
+ "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:displayScaleMode:zoomFactor:"
+ "initWithDisplayScaleMode:zoomFactor:"
+ "initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomSetting:pointScaleOverride:"
+ "initWithVoiceTriggerMode:timestampOffset:language:"
+ "isLinkServicesLinked"
+ "isUserCreated"
+ "language"
+ "mainBufferedInfo"
+ "matchesScaleMode:canvasSize:pointScale:"
+ "matchesWithScaleMode:canvasSize:pointScale:"
+ "messages.sendMessage"
+ "overrideBundleIDsForAppIntentsTesting"
+ "phone.startCall"
+ "preferredPointScaleFor:"
+ "property_key_captionstyles_selectedstyle"
+ "provider"
+ "q24@0:8q16"
+ "resolvedDisplayModeWithMode:"
+ "restrictedModeAuthorizationsForCertificateSerial:"
+ "restrictedModeAuthorizationsForCertificateSerial:reply:"
+ "saveUserCreatedStyle:"
+ "scaleInfo"
+ "selectedStyleID"
+ "sendConnectionSessionFailureInformation:completion:"
+ "service_applyUpdatedRestrictedModeAuthorizations:forCertificateSerial:reply:"
+ "service_startAdvertisingCarPlayControlForUSBWithHost:withReply:"
+ "service_startAdvertisingCarPlayControlForWiFiUUID:host:reply:"
+ "setCompletedFirstConnection:"
+ "setCornerRadius:"
+ "setDisplayConfiguration:"
+ "setEnhancedSiriOverrides failed: %{public}@"
+ "setEnhancedSiriOverrides succeeded"
+ "setEnhancedSiriOverrides: %{public}@"
+ "setEnhancedSiriOverrides:completion:"
+ "setSelectedStyleID:"
+ "setSupportsDolbyAtmos:"
+ "setSupportsEnhancedSiriVoice:"
+ "setSupportsLiveActivities:"
+ "setSupportsSpatialAudio:"
+ "setSupportsVoiceConversational:"
+ "setUniqueID:"
+ "setUserCreated:"
+ "spatialAudioSupported"
+ "splitViewEnabled"
+ "startAdvertisingCarPlayControlForUSBWithHost:"
+ "startAdvertisingCarPlayControlForWiFiUUID:host:"
+ "starting CarPlay Control advertising for Wi-Fi UUID: %@, host: %@"
+ "subtitle settings missing string value for: %{public}@"
+ "supportsDolbyAtmos"
+ "supportsEnhancedSiriVoice"
+ "supportsLiveActivities"
+ "supportsSpatialAudio"
+ "supportsVoiceConversational"
+ "takeScreenForAirPlayOverlayClient:reason:"
+ "textColor"
+ "timestampOffset"
+ "uniqueID"
+ "userCreated"
+ "using restrictedModeAuthorizations: %lu forCertificateSerial:%{private}@"
+ "v24@0:8@?<v@?@\"CREnhancedSiriOverrides\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"CARSessionRequestBonjourHost\"@\"NSError\">16"
+ "v24@?0@\"CREnhancedSiriOverrides\"8@\"NSError\"16"
+ "v28@?0B8@\"CARSessionRequestBonjourHost\"12@\"NSError\"20"
+ "v32@0:8@\"CARSessionRequestBonjourHost\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"CREnhancedSiriOverrides\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"CARSessionRequestBonjourHost\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"CARSessionRequestBonjourHost\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8Q16@\"NSData\"24@?<v@?B@\"NSError\">32"
+ "videoPlayerVersion"
+ "videoShouldOverrideBackgroundColor"
+ "videoShouldOverrideBackgroundOpacity"
+ "videoShouldOverrideEdgeStyle"
+ "videoShouldOverrideFont"
+ "videoShouldOverrideSize"
+ "videoShouldOverrideTextColor"
+ "videoShouldOverrideTextHighlight"
+ "videoShouldOverrideTextOpacity"
+ "voiceTriggerMode: %li, timestampOffset: %@, language: %@"
+ "wantsCarPlayControlAdvertisingForUSBWithHost:"
+ "wantsCarPlayControlAdvertisingForWiFiUUID:host:"
+ "webAppVersion"
+ "{CGSize=dd}32@0:8q16d24"
- "     %@: %@\n"
- "  %@  %@\n"
- "  %@ %@\n"
- "  %@ Driving Mode \n"
- "  %@ Lock Screen Exit Confirmation \n"
- "  Core Motion Operator State: %@ (%@)\n"
- "  Core Motion Vehicular Hints: %@ (%@)\n"
- "  Core Motion Vehicular State: %@ (%@)\n"
- "  Location Services Status: %@ (%@)\n"
- "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, routeSharing: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@,  %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
- "%@, identifier: %@, availableInteractionModels: %@, primaryInteractionModel: %@, isLimited: %@, isNightMode: %@, supportsHiFi: %@, maxFPS: %lu, physicalSize: %@, pixelSize: %@, wantsCornerMasks: %@, initialFocusOwner: %@, viewAreas: %@, displayScaleInfo: %@"
- "0️⃣"
- "1️⃣"
- "2️⃣"
- ";"
- "@\"CARAutomaticDNDStatus\""
- "@108@0:8@16@24@32q40@48@56@64@72B80@84@92B100B104"
- "@16@?0@\"NSDictionary\"8"
- "@32@0:8{CGSize=dd}16"
- "@72@0:8{CGSize=dd}16{CGSize=dd}32@48Q56@64"
- "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "Allowed scale modes: defaultSize:%{public}@, optimizedSize:%{public}@; Original equals to default?: %{public}@"
- "Available"
- "B56@0:8Q16{CGSize=dd}24{CGSize=dd}40"
- "Baseband"
- "Bluetooth"
- "CARDNDUtility"
- "CRDisplayScaleInfo"
- "CRViewArea"
- "CRViewArea: visibleFrame: %@; safeAreaFrame: %@"
- "Connect Standard"
- "DNDStatus"
- "Default primary display scale canvas size calculated: Result(%{public}@)=SquaredPixelSize(%{public}@) x PreferredToOriginalRatio(%{public}@) at PointScale(%{public}@)\nDisplayInfo: %{public}@"
- "Device State:\n"
- "DisplayInfo: physicalSize: %@; pixelSize: %@; squaredPixelSize: %@; viewAreas: %@; screenType: %@; Scale Information = PreferredToOriginalScaleRatio(%@)/ZoomFactor(%@) at PointScale(%@);"
- "DisplaySizes: screenType:"
- "ERROR fetching Driving state: %@"
- "ERROR fetching EC state: %@"
- "EnableCarPlaySetup"
- "GPS"
- "Horizontal density is too low: pixelSize:%{public}@; physicalSize:%{public}@"
- "INVALID"
- "Internal Preferences:\n"
- "Internal settings zoom factor specified: %{public}@"
- "Jumping to 3x scale: pixelSize:%{public}@, ratio: %{public}@"
- "Motion"
- "Not Available"
- "Optimal size is within 0.05 tolerance AND not equal to the original size AND it's currently ON (new connection) AND the screen is >880x528px, we compare against smaller threshold to use 3x more often"
- "Optimal[no ZoomFactor] primary display scale canvas size calculated: Result(%{public}@) = PixelSize(%{public}@) x OptimalScaleFactor(%{public}@) at PointScale(%{public}@)\nDisplayInfo: %{public}@"
- "Optimal[with ZoomFactor] primary display scale canvas size calculated: Result(%{public}@) = SquaredPixelSize(%{public}@) x AdjustedScale(%{public}@); AdjustedScale=PreferredToOriginalScaleRatio(%{public}@)/zoomFactor(%{public}@)\nDisplayInfo: %{public}@"
- "Overall Feature States:\n"
- "Physical size is not valid, applying default size Result(%{public}@) = PointSize(%{public}@)/CROptimalPointsPerMM(%{public}@)"
- "Physical size is zero, applying default size Result(%{public}@) = PointSize(%{public}@)/CROptimalPointsPerMM(%{public}@)"
- "Physical size is zero, pixel density is not valid"
- "Primary"
- "Primary display size is less than minimum: Size(%{public}@) < Min(%{public}@); Returning minimal size;\n minSize(%{public}@)"
- "Q24@0:8q16"
- "ScalingException: (%{public}s) match special case (%s. Point Scale set to %{public}ld"
- "ScalingException: (%{public}s) match special case (%s. Scale zoomFactor set to %{public}f"
- "Secondary"
- "Secondary display size after scaling: Size(%{public}@) = SquaredPixelSize(%{public}@) x Scale(%{public}@); Scale = PreferredToOriginalScaleRatio(%{public}@)/ZoomFactor(%{public}@) at PointScale(%{public}@)"
- "T@\"CARAutomaticDNDStatus\",&,N,V_DNDStatus"
- "T@\"NSArray\",&,N,V_viewAreas"
- "TQ,N,V_screenType"
- "Td,N,V_zoomFactor"
- "The screen is an exception, only optimized display scale allowed"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_safeAreaPixelFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visiblePixelFrame"
- "T{CGSize=dd},N,V_physicalSize"
- "T{CGSize=dd},N,V_pixelSize"
- "T{CGSize=dd},N,V_squaredPixelSize"
- "Unable to parse display physical size"
- "Unable to parse display physical size: %{public}@"
- "Unable to parse display pixel size"
- "Unable to parse display pixel size: %{public}@"
- "User Preferences:\n"
- "Vehicle Queries "
- "Vertical density is too low: pixelSize:%{public}@; physicalSize:%{public}@"
- "Wi-Fi"
- "ZoomFactor"
- "_DNDStatus"
- "_TtC6CarKit14DisplayScaling"
- "_allowedScaleModes"
- "_heuristicPixelSize"
- "_minHeightDisplaySize"
- "_minWidthDisplaySize"
- "_optimalScaleFactorWithPointScale:"
- "_pixelSizeByClampingToMinSize:pointScale:"
- "_safeAreaPixelFrame"
- "_scaleMode"
- "_scaledToOriginalRatio"
- "_visiblePixelFrame"
- "appendString:"
- "canvasPixelSizeForDisplayScaleMode:"
- "com.apple.CarKit"
- "d24@0:8Q16"
- "d24@0:8q16"
- "d56@0:8Q16{CGSize=dd}24{CGSize=dd}40"
- "defaultDisplayMode"
- "displayScaleInfoWithDictionary:screenType:zoomFactor:error:"
- "displayScaleModesForCanvasPixelSize:"
- "exceptionPointScaleWithScreenType:physicalSize:pixelSize:"
- "initWithAirPlayDictionary:"
- "initWithDisplayName:wiredIPv6Addresses:wirelessIPv6Addresses:port:carplayWiFiUUID:deviceIdentifier:publicKey:sourceVersion:supportsMutualAuthentication:authenticationCertificateSerial:pairedVehicleIdentifier:wiredCarPlaySimulator:remoteDeviceConnected:"
- "initWithPhysicalSize:pixelSize:viewAreas:screenType:zoomFactor:"
- "initWithScreenInfo:"
- "initWithVisiblePixelFrame:safeAreaPixelFrame:"
- "isAvailable"
- "isExceptionWithScreenType:physicalSize:pixelSize:"
- "isHeuristicScalable"
- "non-vehicular"
- "not operating"
- "operating"
- "optimizedPointScaleForMode:"
- "originalPointScale"
- "outputFromRhodesUtility"
- "preferredPointScaleForMode:"
- "preferredToOriginalScaleRatioForMode:"
- "property_key_BackgroundColor"
- "property_key_BackgroundColorOverride"
- "property_key_BackgroundOpacity"
- "property_key_BackgroundOpacityOverride"
- "property_key_FontColor"
- "property_key_FontColorOverride"
- "property_key_FontName"
- "property_key_FontNameOverride"
- "property_key_FontSize"
- "property_key_FontSizeOverride"
- "property_key_TextEdgeStyle"
- "property_key_TextEdgeStyleOverride"
- "property_key_TextHighlightColor"
- "property_key_TextHighlightOpacity"
- "property_key_TextHighlightOverride"
- "property_key_TextOpacity"
- "property_key_TextOpacityOverride"
- "q56@0:8Q16{CGSize=dd}24{CGSize=dd}40"
- "safeAreaPixelFrame"
- "setDNDStatus:"
- "setDateStyle:"
- "setPhysicalSize:"
- "setPixelSize:"
- "setSafeAreaPixelFrame:"
- "setScreenType:"
- "setSquaredPixelSize:"
- "setTimeStyle:"
- "setVisiblePixelFrame:"
- "stringByAppendingString:"
- "v32@0:8{CGSize=dd}16"
- "vehicular"
- "vehicularHints"
- "vehicularOperatorState"
- "vehicularState"
- "visiblePixelFrame"
- "zoomFactorHeuristicsWithScreenType:physicalSize:pixelSize:"
- "{CGSize=dd}24@0:8q16"
- "{CGSize=dd}40@0:8{CGSize=dd}16Q32"
- "✅ "
- "❌ "

```
