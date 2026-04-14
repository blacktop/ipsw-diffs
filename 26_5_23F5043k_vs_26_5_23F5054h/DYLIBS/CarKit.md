## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-774.19.0.0.0
-  __TEXT.__text: 0x5f0f0
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x63a4
-  __TEXT.__const: 0x45a
-  __TEXT.__gcc_except_tab: 0xa20
-  __TEXT.__oslogstring: 0x67ba
-  __TEXT.__cstring: 0x54fd
+774.23.0.0.0
+  __TEXT.__text: 0x5f960
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x625c
+  __TEXT.__const: 0x47a
+  __TEXT.__gcc_except_tab: 0xa08
+  __TEXT.__oslogstring: 0x67ea
+  __TEXT.__cstring: 0x55ed
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__swift5_typeref: 0x8a
   __TEXT.__constg_swiftt: 0xf8

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1cf8
+  __TEXT.__unwind_info: 0x1d00
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xc13
-  __TEXT.__objc_methname: 0x11361
-  __TEXT.__objc_methtype: 0x26d3
-  __TEXT.__objc_stubs: 0x97e0
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__const: 0x1fd0
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__objc_methname: 0x11651
+  __TEXT.__objc_methtype: 0x26b3
+  __TEXT.__objc_stubs: 0x9d20
+  __DATA_CONST.__got: 0x7d0
+  __DATA_CONST.__const: 0x1fc8
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35d0
+  __DATA_CONST.__objc_selrefs: 0x3678
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x810
-  __AUTH_CONST.__const: 0x1b08
-  __AUTH_CONST.__cfstring: 0x5800
-  __AUTH_CONST.__objc_const: 0x105c0
-  __AUTH_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__const: 0x1ae8
+  __AUTH_CONST.__cfstring: 0x5a40
+  __AUTH_CONST.__objc_const: 0x100f0
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1280
+  __AUTH.__objc_data: 0x1230
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x78c
+  __DATA.__objc_ivar: 0x750
   __DATA.__data: 0x1130
   __DATA.__bss: 0x6a0
   __DATA_DIRTY.__objc_data: 0x690

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
+  - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7601D892-7C2B-3A0D-88E5-7D31D93DE974
-  Functions: 2962
-  Symbols:   9644
-  CStrings:  5094
+  UUID: A998365F-F2D5-3C74-8971-0A7BFB7A7779
+  Functions: 2931
+  Symbols:   9613
+  CStrings:  5155
 
Symbols:
+ +[CRSubtitleStyle(MediaAccessibilty) _maStyleIDForVideoSettingsStyleID:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleColorForColorRef:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleColorForColorRef:].cold.1
+ +[CRSubtitleStyle(MediaAccessibilty) _styleColorForColorRef:].cold.2
+ +[CRSubtitleStyle(MediaAccessibilty) _styleFontNameForFontDescriptor:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleFontSizeForRelativeFontSize:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleForStyleID:]
+ +[CRSubtitleStyle(MediaAccessibilty) _stylePercentForPercent:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleTextEdgeStyleForTextEdgeStyle:]
+ +[CRSubtitleStyle(MediaAccessibilty) _styleTextEdgeStyleForTextEdgeStyle:].cold.1
+ +[CRSubtitleStyle(MediaAccessibilty) _styleTextOpacityForOpacity:]
+ +[CRSubtitleStyle(MediaAccessibilty) _videoSettingsStyleForMAStyleID:]
+ -[CARDisplayInfo _overrideShowsInstrumentsFromCapabilitiesWithIdentifier:]
+ -[CARDisplayInfo _showsInstrumentsFromCapabilitiesWithIdentifier:defaultValue:]
+ -[CARSessionConfiguration supportsHighFrameRateMaps]
+ -[CRSubtitleStylesManager .cxx_destruct]
+ -[CRSubtitleStylesManager _defaultStyleID]
+ -[CRSubtitleStylesManager _handleSubtitleSettingsChanged:]
+ -[CRSubtitleStylesManager _updateSelectedStyleID]
+ -[CRSubtitleStylesManager availableStyles]
+ -[CRSubtitleStylesManager cachedAvailableStyles]
+ -[CRSubtitleStylesManager cachedClosedCaptionsEnabled]
+ -[CRSubtitleStylesManager closedCaptionsEnabled]
+ -[CRSubtitleStylesManager customStyles]
+ -[CRSubtitleStylesManager delegate]
+ -[CRSubtitleStylesManager description]
+ -[CRSubtitleStylesManager init]
+ -[CRSubtitleStylesManager selectedStyleID]
+ -[CRSubtitleStylesManager selectedSubtitleStyleAsVideoSettingsStyleID]
+ -[CRSubtitleStylesManager setCachedAvailableStyles:]
+ -[CRSubtitleStylesManager setCachedClosedCaptionsEnabled:]
+ -[CRSubtitleStylesManager setClosedCaptionsEnabled:]
+ -[CRSubtitleStylesManager setDelegate:]
+ -[CRSubtitleStylesManager setSelectedStyleID:]
+ -[CRSubtitleStylesManager setSelectedSubtitleStyleFromVideoSettingsStyleID:]
+ _CGColorGetComponents
+ _CGColorGetNumberOfComponents
+ _CTFontDescriptorCopyAttribute
+ _MACaptionAppearanceCopyBackgroundColor
+ _MACaptionAppearanceCopyFontDescriptorForStyle
+ _MACaptionAppearanceCopyForegroundColor
+ _MACaptionAppearanceCopyProfileIDs
+ _MACaptionAppearanceCopyProfileName
+ _MACaptionAppearanceCopyWindowColor
+ _MACaptionAppearanceExecuteBlockForProfileID
+ _MACaptionAppearanceGetBackgroundOpacity
+ _MACaptionAppearanceGetForegroundOpacity
+ _MACaptionAppearanceGetRelativeCharacterSize
+ _MACaptionAppearanceGetTextEdgeStyle
+ _MACaptionAppearanceGetWindowOpacity
+ _MACaptionAppearanceIsCustomized
+ _MACaptionAppearancePrefCopyActiveProfileID
+ _MACaptionAppearancePrefCopyPreferAccessibleCaptions
+ _MACaptionAppearancePrefSetActiveProfileID
+ _MACaptionAppearancePrefSetPreferAccessibleCaptions
+ _MACaptionAppearanceSetDisplayType
+ _MTLCreateSystemDefaultDevice
+ _OBJC_CLASS_$_BSColor
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsHighFrameRateMaps
+ _OBJC_IVAR_$_CRSubtitleStylesManager._cachedAvailableStyles
+ _OBJC_IVAR_$_CRSubtitleStylesManager._cachedClosedCaptionsEnabled
+ _OBJC_IVAR_$_CRSubtitleStylesManager._delegate
+ _OBJC_IVAR_$_CRSubtitleStylesManager._selectedStyleID
+ __OBJC_$_CLASS_METHODS_CRSubtitleStyle(MediaAccessibilty)
+ __OBJC_$_INSTANCE_METHODS_CRSubtitleStylesManager
+ __OBJC_$_INSTANCE_VARIABLES_CRSubtitleStylesManager
+ __OBJC_$_PROP_LIST_CRSubtitleStylesManager
+ ___39-[CRSubtitleStylesManager customStyles]_block_invoke
+ ___42-[CRSubtitleStylesManager availableStyles]_block_invoke
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.27
+ ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.27.cold.1
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.32
+ ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.32.cold.1
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke.22
+ ___52-[CRSubtitleStyle initWithDictionaryRepresentation:]_block_invoke.22.cold.1
+ ___55+[CRSubtitleStyle(MediaAccessibilty) _styleForStyleID:]_block_invoke
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.40
+ ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.40.cold.1
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.37
+ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.37.cold.1
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.209
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.209.cold.1
+ ___CRCollectCarPlayDiagnostics_block_invoke.164
+ ___CRCollectVehicleLogs_block_invoke.168
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.172
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.172.cold.1
+ ___CRPostBannerToPhone_block_invoke.156
+ ___CRServiceConnectionPerform_block_invoke.120
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.182
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.182.cold.1
+ ___block_descriptor_32_e25_B16?0"CRSubtitleStyle"8l
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.154
+ ___block_literal_global.181
+ ___block_literal_global.197
+ ___block_literal_global.202
+ ___block_literal_global.203
+ ___block_literal_global.42
+ _kCTFontNameAttribute
+ _kMACaptionAppearanceSettingsChangedNotification
+ _objc_msgSend$_maStyleIDForVideoSettingsStyleID:
+ _objc_msgSend$_overrideShowsInstrumentsFromCapabilitiesWithIdentifier:
+ _objc_msgSend$_showsInstrumentsFromCapabilitiesWithIdentifier:defaultValue:
+ _objc_msgSend$_styleColorForColorRef:
+ _objc_msgSend$_styleFontNameForFontDescriptor:
+ _objc_msgSend$_styleFontSizeForRelativeFontSize:
+ _objc_msgSend$_styleForStyleID:
+ _objc_msgSend$_stylePercentForPercent:
+ _objc_msgSend$_styleTextEdgeStyleForTextEdgeStyle:
+ _objc_msgSend$_styleTextOpacityForOpacity:
+ _objc_msgSend$_updateSelectedStyleID
+ _objc_msgSend$_videoSettingsStyleForMAStyleID:
+ _objc_msgSend$availableStyles
+ _objc_msgSend$bs_reverse
+ _objc_msgSend$cachedAvailableStyles
+ _objc_msgSend$cachedClosedCaptionsEnabled
+ _objc_msgSend$closedCaptionsEnabled
+ _objc_msgSend$colorWithRed:green:blue:alpha:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$isUserCreated
+ _objc_msgSend$selectedStyleID
+ _objc_msgSend$setAllowBackgroundColorOverride:
+ _objc_msgSend$setAllowBackgroundOpacityOverride:
+ _objc_msgSend$setAllowFontColorOverride:
+ _objc_msgSend$setAllowFontNameOverride:
+ _objc_msgSend$setAllowFontSizeOverride:
+ _objc_msgSend$setAllowTextEdgeStyleOverride:
+ _objc_msgSend$setAllowTextHighlightOverride:
+ _objc_msgSend$setAllowTextOpacityOverride:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setBackgroundOpacity:
+ _objc_msgSend$setCachedAvailableStyles:
+ _objc_msgSend$setCachedClosedCaptionsEnabled:
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setFontColor:
+ _objc_msgSend$setFontName:
+ _objc_msgSend$setFontSize:
+ _objc_msgSend$setTextEdgeStyle:
+ _objc_msgSend$setTextHighlightColor:
+ _objc_msgSend$setTextHighlightOpacity:
+ _objc_msgSend$setTextOpacity:
+ _objc_msgSend$setUniqueID:
+ _objc_msgSend$setUserCreated:
+ _objc_msgSend$subtitleStylesManager:didChangeAvailableStyles:
+ _objc_msgSend$subtitleStylesManager:didSelectStyleID:
+ _objc_msgSend$subtitleStylesManager:didSetClosedCaptionsEnabled:
+ _objc_msgSend$supportsFamily:
- +[CRSubtitleSettings _defaultStyleID]
- +[CRSubtitleSettings defaultSettings]
- +[CRSubtitleSettings supportsSecureCoding]
- +[CRSubtitleStylesManager availableStyles]
- +[CRSubtitleStylesManager deleteUserCreatedStyle:]
- +[CRSubtitleStylesManager saveUserCreatedStyle:]
- -[CRSubtitleSettings .cxx_destruct]
- -[CRSubtitleSettings allowBackgroundColorOverride]
- -[CRSubtitleSettings allowBackgroundOpacityOverride]
- -[CRSubtitleSettings allowFontColorOverride]
- -[CRSubtitleSettings allowFontNameOverride]
- -[CRSubtitleSettings allowFontSizeOverride]
- -[CRSubtitleSettings allowTextEdgeStyleOverride]
- -[CRSubtitleSettings allowTextHighlightOverride]
- -[CRSubtitleSettings allowTextOpacityOverride]
- -[CRSubtitleSettings backgroundColor]
- -[CRSubtitleSettings backgroundOpacity]
- -[CRSubtitleSettings closedCaptionsEnabled]
- -[CRSubtitleSettings copyWithZone:]
- -[CRSubtitleSettings description]
- -[CRSubtitleSettings dictionaryRepresentation]
- -[CRSubtitleSettings encodeWithCoder:]
- -[CRSubtitleSettings fontColor]
- -[CRSubtitleSettings fontName]
- -[CRSubtitleSettings fontSize]
- -[CRSubtitleSettings initWithCoder:]
- -[CRSubtitleSettings initWithDictionaryRepresentation:]
- -[CRSubtitleSettings selectedStyleID]
- -[CRSubtitleSettings setAllowBackgroundColorOverride:]
- -[CRSubtitleSettings setAllowBackgroundOpacityOverride:]
- -[CRSubtitleSettings setAllowFontColorOverride:]
- -[CRSubtitleSettings setAllowFontNameOverride:]
- -[CRSubtitleSettings setAllowFontSizeOverride:]
- -[CRSubtitleSettings setAllowTextEdgeStyleOverride:]
- -[CRSubtitleSettings setAllowTextHighlightOverride:]
- -[CRSubtitleSettings setAllowTextOpacityOverride:]
- -[CRSubtitleSettings setBackgroundColor:]
- -[CRSubtitleSettings setBackgroundOpacity:]
- -[CRSubtitleSettings setClosedCaptionsEnabled:]
- -[CRSubtitleSettings setFontColor:]
- -[CRSubtitleSettings setFontName:]
- -[CRSubtitleSettings setFontSize:]
- -[CRSubtitleSettings setSelectedStyleID:]
- -[CRSubtitleSettings setTextEdgeStyle:]
- -[CRSubtitleSettings setTextHighlightColor:]
- -[CRSubtitleSettings setTextHighlightOpacity:]
- -[CRSubtitleSettings setTextOpacity:]
- -[CRSubtitleSettings textEdgeStyle]
- -[CRSubtitleSettings textHighlightColor]
- -[CRSubtitleSettings textHighlightOpacity]
- -[CRSubtitleSettings textOpacity]
- -[CRVehicle setSubtitleSettings:]
- -[CRVehicle subtitleSettings]
- -[CRVehicleVideoSettings setSubtitleSettings:]
- -[CRVehicleVideoSettings subtitleSettings]
- -[CRVehicleVideoSettings subtitleSettings].cold.1
- GCC_except_table11
- _OBJC_CLASS_$_CRSubtitleSettings
- _OBJC_IVAR_$_CRSubtitleSettings._allowBackgroundColorOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowBackgroundOpacityOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowFontColorOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowFontNameOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowFontSizeOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowTextEdgeStyleOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowTextHighlightOverride
- _OBJC_IVAR_$_CRSubtitleSettings._allowTextOpacityOverride
- _OBJC_IVAR_$_CRSubtitleSettings._backgroundColor
- _OBJC_IVAR_$_CRSubtitleSettings._backgroundOpacity
- _OBJC_IVAR_$_CRSubtitleSettings._closedCaptionsEnabled
- _OBJC_IVAR_$_CRSubtitleSettings._fontColor
- _OBJC_IVAR_$_CRSubtitleSettings._fontName
- _OBJC_IVAR_$_CRSubtitleSettings._fontSize
- _OBJC_IVAR_$_CRSubtitleSettings._selectedStyleID
- _OBJC_IVAR_$_CRSubtitleSettings._textEdgeStyle
- _OBJC_IVAR_$_CRSubtitleSettings._textHighlightColor
- _OBJC_IVAR_$_CRSubtitleSettings._textHighlightOpacity
- _OBJC_IVAR_$_CRSubtitleSettings._textOpacity
- _OBJC_IVAR_$_CRVehicle._subtitleSettings
- _OBJC_METACLASS_$_CRSubtitleSettings
- __OBJC_$_CLASS_METHODS_CRSubtitleSettings
- __OBJC_$_CLASS_METHODS_CRSubtitleStyle
- __OBJC_$_CLASS_METHODS_CRSubtitleStylesManager
- __OBJC_$_CLASS_PROP_LIST_CRSubtitleSettings
- __OBJC_$_INSTANCE_METHODS_CRSubtitleSettings
- __OBJC_$_INSTANCE_VARIABLES_CRSubtitleSettings
- __OBJC_$_PROP_LIST_CRSubtitleSettings
- __OBJC_CLASS_PROTOCOLS_$_CRSubtitleSettings
- __OBJC_CLASS_RO_$_CRSubtitleSettings
- __OBJC_METACLASS_RO_$_CRSubtitleSettings
- ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke
- ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke.21
- ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke.21.cold.1
- ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke_2
- ___42-[CRVehicleVideoSettings subtitleSettings]_block_invoke_2.cold.1
- ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.36
- ___44-[CRVehicleVideoSettings diagnosticsEnabled]_block_invoke.36.cold.1
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke.26
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke.26.cold.1
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2.cold.1
- ___46-[CRVehicleVideoSettings setSubtitleSettings:]_block_invoke_2.cold.2
- ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.41
- ___48-[CRVehicleVideoSettings setDiagnosticsEnabled:]_block_invoke.41.cold.1
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.36
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.36.cold.1
- ___55-[CRSubtitleSettings initWithDictionaryRepresentation:]_block_invoke.cold.1
- ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.49
- ___58-[CRVehicleVideoSettings fetchLicensesTextWithCompletion:]_block_invoke.49.cold.1
- ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.46
- ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke.46.cold.1
- ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.213
- ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.213.cold.1
- ___CRCollectCarPlayDiagnostics_block_invoke.168
- ___CRCollectVehicleLogs_block_invoke.172
- ___CRIsPreflightThemeAssetEnabled_block_invoke.176
- ___CRIsPreflightThemeAssetEnabled_block_invoke.176.cold.1
- ___CRPostBannerToPhone_block_invoke.160
- ___CRServiceConnectionPerform_block_invoke.124
- ___CRSetPreflightThemeAssetEnabled_block_invoke.186
- ___CRSetPreflightThemeAssetEnabled_block_invoke.186.cold.1
- ___block_descriptor_40_e8_32r_e40_v24?0"CRSubtitleSettings"8"NSError"16lr32l8
- ___block_descriptor_48_e8_32s40s_e27_v16?0"<CRCarKitService>"8ls32l8s40l8
- ___block_literal_global.185
- ___block_literal_global.201
- ___block_literal_global.204
- ___block_literal_global.206
- ___block_literal_global.207
- ___block_literal_global.38
- _objc_msgSend$setClosedCaptionsEnabled:
- _objc_msgSend$setSubtitleSettings:
- _objc_msgSend$setVideoSubtitleSettings:forVehicleIdentifier:reply:
- _objc_msgSend$subtitleSettings
- _objc_msgSend$videoSubtitleSettingsForVehicleIdentifier:reply:
CStrings:
+ "(subtitles enabled: %@, style: %@)"
+ ".AppleSystemUIFont"
+ ".AppleSystemUIFontBold"
+ ".AppleSystemUIFontMedium"
+ ".AppleSystemUIFontMonospaced-"
+ "@\"<CRSubtitleStylesDelegate>\""
+ "AvenirNext-"
+ "B16@?0@\"CRSubtitleStyle\"8"
+ "Copperplate-"
+ "Courier-"
+ "Device supports high maps framerate %@"
+ "Found a cluster display identifier in capabilities for screen with identifier %@, setting showsInstruments to %@"
+ "Helvetica-"
+ "MACaptionProfile-Classic"
+ "MACaptionProfile-Default"
+ "MACaptionProfile-LargeText"
+ "MACaptionProfile-OutlineText"
+ "MediaAccessibilty"
+ "Menlo-"
+ "No cluster display identifier found in capabilities for screen with identifier %@, using default showsInstruments: %@"
+ "T@\"<CRSubtitleStylesDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_cachedAvailableStyles"
+ "TB,N,V_cachedClosedCaptionsEnabled"
+ "TB,R,N,V_supportsHighFrameRateMaps"
+ "_cachedAvailableStyles"
+ "_cachedClosedCaptionsEnabled"
+ "_handleSubtitleSettingsChanged:"
+ "_maStyleIDForVideoSettingsStyleID:"
+ "_overrideShowsInstrumentsFromCapabilitiesWithIdentifier:"
+ "_showsInstrumentsFromCapabilitiesWithIdentifier:defaultValue:"
+ "_styleColorForColorRef:"
+ "_styleFontNameForFontDescriptor:"
+ "_styleFontSizeForRelativeFontSize:"
+ "_styleForStyleID:"
+ "_stylePercentForPercent:"
+ "_styleTextEdgeStyleForTextEdgeStyle:"
+ "_styleTextOpacityForOpacity:"
+ "_supportsHighFrameRateMaps"
+ "_updateSelectedStyleID"
+ "_videoSettingsStyleForMAStyleID:"
+ "bs_reverse"
+ "cachedAvailableStyles"
+ "cachedClosedCaptionsEnabled"
+ "colorWithRed:green:blue:alpha:"
+ "customStyles"
+ "hasPrefix:"
+ "i24@0:8^{CGColor=}16"
+ "i24@0:8^{__CTFontDescriptor=}16"
+ "i24@0:8d16"
+ "i24@0:8q16"
+ "mapped font descriptor %{public}@ to value %i"
+ "read style from MA: %@"
+ "selectedSubtitleStyleAsVideoSettingsStyleID"
+ "setCachedAvailableStyles:"
+ "setCachedClosedCaptionsEnabled:"
+ "setSelectedSubtitleStyleFromVideoSettingsStyleID:"
+ "setting style to MA: %@"
+ "style: %@ has fontDescriptor: %@"
+ "subtitleStylesManager:didChangeAvailableStyles:"
+ "subtitleStylesManager:didSelectStyleID:"
+ "subtitleStylesManager:didSetClosedCaptionsEnabled:"
+ "supportsFamily:"
+ "supportsHighFrameRateMaps"
+ "system_1"
+ "system_2"
+ "system_3"
+ "system_5"
+ "uniqueId"
+ "unsupported color for subtitle color: %{public}@"
+ "unsupported colorspace for subtitle color"
+ "unsupported text edge style: %d"
- "@\"CRSubtitleSettings\""
- "CRSubtitleSettings"
- "Found a cluster display identifier in capabilities for secondary screen with identifier %@, setting showsInstruments to %@"
- "No cluster display identifier found in capabilities for secondary screen with identifier %@, setting showsInstruments to YES"
- "T@\"CRSubtitleSettings\",&,N"
- "T@\"CRSubtitleSettings\",&,N,V_subtitleSettings"
- "TB,N,V_closedCaptionsEnabled"
- "_closedCaptionsEnabled"
- "_subtitleSettings"
- "a"
- "defaultSettings"
- "deleteUserCreatedStyle:"
- "fetch subtitleSettings"
- "property_key_ClosedCaptionsAndSDH_Enabled"
- "property_key_captionstyles_selectedstyle"
- "saveUserCreatedStyle:"
- "setSubtitleSettings call failed: %@"
- "setSubtitleSettings succeeded"
- "setSubtitleSettings:"
- "setSubtitleSettings: %{public}@"
- "setVideoSubtitleSettings:forVehicleIdentifier:reply:"
- "subtitleSettings"
- "subtitleSettings call failed: %@"
- "subtitleSettings call failed: %{public}@"
- "subtitleSettings: %{public}@"
- "v24@?0@\"CRSubtitleSettings\"8@\"NSError\"16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"CRSubtitleSettings\"@\"NSError\">24"
- "v40@0:8@\"CRSubtitleSettings\"16@\"NSUUID\"24@?<v@?B@\"NSError\">32"
- "videoSubtitleSettingsForVehicleIdentifier:reply:"

```
