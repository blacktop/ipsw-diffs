## DisplayAndBrightnessSettings

> `/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`

```diff

-1182.0.0.0.0
-  __TEXT.__text: 0x284ec
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x298c
+1184.102.0.0.0
+  __TEXT.__text: 0x2b918
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0x2c54
   __TEXT.__const: 0x2f4
-  __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__cstring: 0x2cfc
-  __TEXT.__oslogstring: 0x66a
+  __TEXT.__gcc_except_tab: 0x440
+  __TEXT.__cstring: 0x317c
+  __TEXT.__oslogstring: 0x6f1
   __TEXT.__constg_swiftt: 0x84
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x9c0
-  __TEXT.__objc_classname: 0x7e4
-  __TEXT.__objc_methname: 0x82ee
-  __TEXT.__objc_methtype: 0xeb2
-  __TEXT.__objc_stubs: 0x6e80
-  __DATA_CONST.__got: 0x638
+  __TEXT.__unwind_info: 0xa50
+  __TEXT.__objc_classname: 0x84c
+  __TEXT.__objc_methname: 0x8860
+  __TEXT.__objc_methtype: 0xebd
+  __TEXT.__objc_stubs: 0x7320
+  __DATA_CONST.__got: 0x660
   __DATA_CONST.__const: 0x600
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2150
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x3000
-  __AUTH_CONST.__objc_const: 0x4700
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__objc_const: 0x4998
+  __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xc40
+  __AUTH.__objc_data: 0xd30
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x318
+  __DATA.__objc_ivar: 0x324
   __DATA.__data: 0x768
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1585A63D-F705-3FE0-ACD0-45CAF1BBB5FC
-  Functions: 903
-  Symbols:   3789
-  CStrings:  2460
+  UUID: 5C9167AF-7DF6-320F-9CA3-43B0701406ED
+  Functions: 963
+  Symbols:   3981
+  CStrings:  2583
 
Symbols:
+ +[DBSLiquidGlassController glassLegibilitySetting]
+ +[DBSLiquidGlassController setGlassLegibilitySetting:]
+ +[DBSLiquidGlassPreviewTableCell previewImageForGlassLegibilitySetting:]
+ +[DBSLiquidGlassPreviewTableCell previewImageNameForGlassLegibilitySetting:]
+ -[DBSColorTemperatureController _setBlueLightReductionEnabled:forSpecifier:]
+ -[DBSColorTemperatureController getBlueLightReductionManualEnabled:]
+ -[DBSColorTemperatureController getBlueLightReductionManualEnabled:].cold.1
+ -[DBSColorTemperatureController setBlueLightReductionManualEnabled:forSpecifier:]
+ -[DBSExternalDisplayAdvancedPreferencesController _updateAdaptiveSyncIfNecessary]
+ -[DBSExternalDisplayAdvancedPreferencesController _updateCurrentHDRModeIfNecessary]
+ -[DBSExternalDisplayAdvancedPreferencesController _updateLimitRefreshRateIfNecessary]
+ -[DBSExternalDisplayAdvancedPreferencesController adaptiveSyncEnabled:]
+ -[DBSExternalDisplayAdvancedPreferencesController adaptiveSyncSpecifiersFooterText]
+ -[DBSExternalDisplayAdvancedPreferencesController adaptiveSyncSpecifiers]
+ -[DBSExternalDisplayAdvancedPreferencesController connectedDisplayDidUpdate:]
+ -[DBSExternalDisplayAdvancedPreferencesController currentHDRMode]
+ -[DBSExternalDisplayAdvancedPreferencesController dealloc]
+ -[DBSExternalDisplayAdvancedPreferencesController displayModeSpecifiersFooterText]
+ -[DBSExternalDisplayAdvancedPreferencesController displayModeSpecifiers]
+ -[DBSExternalDisplayAdvancedPreferencesController init]
+ -[DBSExternalDisplayAdvancedPreferencesController limitRefreshRateEnabled:]
+ -[DBSExternalDisplayAdvancedPreferencesController limitRefreshRateSpecifiers]
+ -[DBSExternalDisplayAdvancedPreferencesController matchContentEnabled:]
+ -[DBSExternalDisplayAdvancedPreferencesController setAdaptiveSyncEnabled:specifier:]
+ -[DBSExternalDisplayAdvancedPreferencesController setCurrentHDRMode:]
+ -[DBSExternalDisplayAdvancedPreferencesController setLimitRefreshRateEnabled:specifier:]
+ -[DBSExternalDisplayAdvancedPreferencesController setMatchContentEnabled:specifier:]
+ -[DBSExternalDisplayAdvancedPreferencesController specifiers]
+ -[DBSExternalDisplayAdvancedPreferencesController tableView:didSelectRowAtIndexPath:]
+ -[DBSExternalDisplayAdvancedPreferencesController tableView:shouldHighlightRowAtIndexPath:]
+ -[DBSExternalDisplayAdvancedPreferencesController valueForSpecifier:]
+ -[DBSExternalDisplayAdvancedPreferencesController viewDidLoad]
+ -[DBSExternalDisplayAdvancedPreferencesController viewWillAppear:]
+ -[DBSExternalDisplayManager adaptiveSyncEnabled]
+ -[DBSExternalDisplayManager limitRefreshRate]
+ -[DBSExternalDisplayManager setAdaptiveSyncEnabled:]
+ -[DBSExternalDisplayManager setLimitRefreshRate:]
+ -[DBSExternalDisplayManager supportedHDRModesWithHighRefreshRate]
+ -[DBSExternalDisplayManager supportedHDRModesWithVRR]
+ -[DBSLiquidGlassController .cxx_destruct]
+ -[DBSLiquidGlassController accessibilityOptionDidChange:]
+ -[DBSLiquidGlassController canChangeSetting]
+ -[DBSLiquidGlassController changeGlassLegibilitySetting:]
+ -[DBSLiquidGlassController dealloc]
+ -[DBSLiquidGlassController initWithNibName:bundle:]
+ -[DBSLiquidGlassController jumpToAccessibilitySettings:]
+ -[DBSLiquidGlassController radioGroup]
+ -[DBSLiquidGlassController setRadioGroup:]
+ -[DBSLiquidGlassController specifiers]
+ -[DBSLiquidGlassController tableView:didSelectRowAtIndexPath:]
+ -[DBSLiquidGlassController tableView:willDisplayCell:forRowAtIndexPath:]
+ -[DBSLiquidGlassPreviewTableCell .cxx_destruct]
+ -[DBSLiquidGlassPreviewTableCell glassLegibilitySetting]
+ -[DBSLiquidGlassPreviewTableCell initWithStyle:reuseIdentifier:]
+ -[DBSLiquidGlassPreviewTableCell previewImageView]
+ -[DBSLiquidGlassPreviewTableCell setGlassLegibilitySetting:]
+ -[DBSLiquidGlassPreviewTableCell setPreviewImageView:]
+ -[DBSSettingsController liquidGlassLegibilitySettingForSpecifier:]
+ GCC_except_table11
+ GCC_except_table15
+ GCC_except_table42
+ GCC_except_table5
+ _DBS_LocalizedStringForConnectedDisplays_J8xx
+ _OBJC_CLASS_$_CADisplayModeCriteria
+ _OBJC_CLASS_$_DBSExternalDisplayAdvancedPreferencesController
+ _OBJC_CLASS_$_DBSLiquidGlassController
+ _OBJC_CLASS_$_DBSLiquidGlassPreviewTableCell
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_IVAR_$_DBSLiquidGlassController._radioGroup
+ _OBJC_IVAR_$_DBSLiquidGlassPreviewTableCell._glassLegibilitySetting
+ _OBJC_IVAR_$_DBSLiquidGlassPreviewTableCell._previewImageView
+ _OBJC_METACLASS_$_DBSExternalDisplayAdvancedPreferencesController
+ _OBJC_METACLASS_$_DBSLiquidGlassController
+ _OBJC_METACLASS_$_DBSLiquidGlassPreviewTableCell
+ _UIAccessibilityDarkerSystemColorsEnabled
+ _UIAccessibilityDarkerSystemColorsStatusDidChangeNotification
+ _UIAccessibilityIsReduceTransparencyEnabled
+ _UIAccessibilityReduceTransparencyStatusDidChangeNotification
+ _UIViewGlassGetLegibilitySetting
+ _UIViewGlassSetLegibilitySetting
+ __OBJC_$_CLASS_METHODS_DBSLiquidGlassController
+ __OBJC_$_CLASS_METHODS_DBSLiquidGlassPreviewTableCell
+ __OBJC_$_CLASS_PROP_LIST_DBSLiquidGlassController
+ __OBJC_$_INSTANCE_METHODS_DBSExternalDisplayAdvancedPreferencesController
+ __OBJC_$_INSTANCE_METHODS_DBSLiquidGlassController
+ __OBJC_$_INSTANCE_METHODS_DBSLiquidGlassPreviewTableCell
+ __OBJC_$_INSTANCE_VARIABLES_DBSLiquidGlassController
+ __OBJC_$_INSTANCE_VARIABLES_DBSLiquidGlassPreviewTableCell
+ __OBJC_$_PROP_LIST_DBSLiquidGlassController
+ __OBJC_$_PROP_LIST_DBSLiquidGlassPreviewTableCell
+ __OBJC_CLASS_RO_$_DBSExternalDisplayAdvancedPreferencesController
+ __OBJC_CLASS_RO_$_DBSLiquidGlassController
+ __OBJC_CLASS_RO_$_DBSLiquidGlassPreviewTableCell
+ __OBJC_METACLASS_RO_$_DBSExternalDisplayAdvancedPreferencesController
+ __OBJC_METACLASS_RO_$_DBSLiquidGlassController
+ __OBJC_METACLASS_RO_$_DBSLiquidGlassPreviewTableCell
+ ___60-[DBSLiquidGlassPreviewTableCell setGlassLegibilitySetting:]_block_invoke
+ ___76-[DBSColorTemperatureController _setBlueLightReductionEnabled:forSpecifier:]_block_invoke
+ ___76-[DBSColorTemperatureController _setBlueLightReductionEnabled:forSpecifier:]_block_invoke_2
+ ___77-[DBSExternalDisplayAdvancedPreferencesController connectedDisplayDidUpdate:]_block_invoke
+ ___77-[DBSExternalDisplayPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke.90
+ ___85-[DBSExternalDisplayAdvancedPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke
+ ___85-[DBSExternalDisplayAdvancedPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke.76
+ _objc_msgSend$_setBlueLightReductionEnabled:forSpecifier:
+ _objc_msgSend$_setContinuousCornerRadius:
+ _objc_msgSend$_updateAdaptiveSyncIfNecessary
+ _objc_msgSend$_updateCurrentHDRModeIfNecessary
+ _objc_msgSend$_updateLimitRefreshRateIfNecessary
+ _objc_msgSend$adaptiveSyncEnabled
+ _objc_msgSend$adaptiveSyncSpecifiers
+ _objc_msgSend$adaptiveSyncSpecifiersFooterText
+ _objc_msgSend$cachedCellForSpecifierID:
+ _objc_msgSend$canChangeSetting
+ _objc_msgSend$changeGlassLegibilitySetting:
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$displayModeSpecifiersFooterText
+ _objc_msgSend$glassLegibilitySetting
+ _objc_msgSend$imageNamed:inBundle:
+ _objc_msgSend$leftAnchor
+ _objc_msgSend$limitRefreshRate
+ _objc_msgSend$limitRefreshRateSpecifiers
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$prefersHighRefreshRate
+ _objc_msgSend$prefersVariableRefreshRate
+ _objc_msgSend$previewImageForGlassLegibilitySetting:
+ _objc_msgSend$previewImageNameForGlassLegibilitySetting:
+ _objc_msgSend$previewImageView
+ _objc_msgSend$rightAnchor
+ _objc_msgSend$setAdaptiveSyncEnabled:
+ _objc_msgSend$setGlassLegibilitySetting:
+ _objc_msgSend$setHighRefreshRate:
+ _objc_msgSend$setLimitRefreshRate:
+ _objc_msgSend$setPrefersHighRefreshRate:
+ _objc_msgSend$setPrefersVariableRefreshRate:
+ _objc_msgSend$setRadioGroup:
+ _objc_msgSend$setVariableRefreshRate:
+ _objc_msgSend$supportedHDRModesWithCriteria:
+ _objc_msgSend$supportedHDRModesWithHighRefreshRate
+ _objc_msgSend$supportedHDRModesWithVRR
+ _objc_msgSend$transitionWithView:duration:options:animations:completion:
- -[DBSColorTemperatureController getBlueLightReductionEnabled:]
- -[DBSColorTemperatureController getBlueLightReductionEnabled:].cold.1
- -[DBSColorTemperatureController setBlueLightReductionEnabled:forSpecifier:]
- GCC_except_table10
- GCC_except_table36
- ___75-[DBSColorTemperatureController setBlueLightReductionEnabled:forSpecifier:]_block_invoke
- ___75-[DBSColorTemperatureController setBlueLightReductionEnabled:forSpecifier:]_block_invoke_2
- ___77-[DBSExternalDisplayPreferencesController tableView:didSelectRowAtIndexPath:]_block_invoke.83
CStrings:
+ "-[DBSColorTemperatureController getBlueLightReductionManualEnabled:]"
+ "@24@0:8q16"
+ "ADAPTIVE_SYNC"
+ "ADAPTIVE_SYNC_FOOTER"
+ "ADAPTIVE_SYNC_FOOTER_NOT_SUPPORT_DOLBY_VISION"
+ "ADAPTIVE_SYNC_FOOTER_NOT_SUPPORT_HDR"
+ "ADAPTIVE_SYNC_FOOTER_NOT_SUPPORT_SDR"
+ "ADAPTIVE_SYNC_FOOTER_REQUIRE_DOLBY_VISION"
+ "ADAPTIVE_SYNC_FOOTER_REQUIRE_HDR"
+ "ADAPTIVE_SYNC_FOOTER_REQUIRE_SDR"
+ "ADAPTIVE_SYNC_GROUP"
+ "CLEAR"
+ "COLOR_SETTING_FOOTER_NOT_SUPPORT_DOLBY_VISION"
+ "COLOR_SETTING_FOOTER_NOT_SUPPORT_HDR"
+ "COLOR_SETTING_FOOTER_NOT_SUPPORT_SDR"
+ "COLOR_SETTING_FOOTER_REQUIRE_DOLBY_VISION"
+ "COLOR_SETTING_FOOTER_REQUIRE_HDR"
+ "COLOR_SETTING_FOOTER_REQUIRE_SDR"
+ "DBSExternalDisplayAdvancedPreferencesController"
+ "DBSLiquidGlassController"
+ "DBSLiquidGlassPreviewTableCell"
+ "External Display: Setting adaptive sync preference enabled to: %@"
+ "External Display: Setting limit refresh rate preference to value: %@"
+ "ExternalDisplays_J8xx"
+ "Footer for the 'Adaptive Sync' section that explains what the 'Adaptive Sync' switch does."
+ "Footer for the 'Limit Refresh Rate' section that explains what the 'Limit Refresh Rate' switch does."
+ "LIMIT_REFRESH_RATE"
+ "LIMIT_REFRESH_RATE_FOOTER"
+ "LIMIT_REFRESH_RATE_GROUP"
+ "LIQUID_GLASS"
+ "LIQUID_GLASS_PREVIEW"
+ "LIQUID_GLASS_SETTING_ACCESSIBILITY_FOOTER"
+ "LIQUID_GLASS_SETTING_ACCESSIBILITY_LINK_FOOTER"
+ "LIQUID_GLASS_SETTING_FOOTER"
+ "LiquidGlassLegibilityRegular"
+ "LiquidGlassLegibilityTinted"
+ "T@\"PSSpecifier\",&,N,V_radioGroup"
+ "T@\"UIImageView\",&,N,V_previewImageView"
+ "TINTED"
+ "Title for the adaptive async switch cell."
+ "Title for the limit refresh rate switch cell."
+ "Tq,N"
+ "Tq,N,V_glassLegibilitySetting"
+ "_glassLegibilitySetting"
+ "_setBlueLightReductionEnabled:forSpecifier:"
+ "_setContinuousCornerRadius:"
+ "_updateAdaptiveSyncIfNecessary"
+ "_updateCurrentHDRModeIfNecessary"
+ "_updateLimitRefreshRateIfNecessary"
+ "accessibilityOptionDidChange:"
+ "adaptiveSyncEnabled"
+ "adaptiveSyncEnabled:"
+ "adaptiveSyncSpecifiers"
+ "adaptiveSyncSpecifiersFooterText"
+ "cachedCellForSpecifierID:"
+ "canChangeSetting"
+ "changeGlassLegibilitySetting:"
+ "defaultWorkspace"
+ "displayModeSpecifiersFooterText"
+ "getBlueLightReductionManualEnabled:"
+ "glassLegibilitySetting"
+ "imageNamed:inBundle:"
+ "jumpToAccessibilitySettings:"
+ "leftAnchor"
+ "limitRefreshRate"
+ "limitRefreshRateEnabled:"
+ "limitRefreshRateSpecifiers"
+ "liquidGlassLegibilitySettingForSpecifier:"
+ "openSensitiveURL:withOptions:"
+ "prefersHighRefreshRate"
+ "prefersVariableRefreshRate"
+ "prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT"
+ "previewImageForGlassLegibilitySetting:"
+ "previewImageNameForGlassLegibilitySetting:"
+ "previewImageView"
+ "radioGroup"
+ "rightAnchor"
+ "setAdaptiveSyncEnabled:"
+ "setAdaptiveSyncEnabled:specifier:"
+ "setBlueLightReductionManualEnabled:forSpecifier:"
+ "setGlassLegibilitySetting:"
+ "setHighRefreshRate:"
+ "setLimitRefreshRate:"
+ "setLimitRefreshRateEnabled:specifier:"
+ "setPrefersHighRefreshRate:"
+ "setPrefersVariableRefreshRate:"
+ "setPreviewImageView:"
+ "setRadioGroup:"
+ "setVariableRefreshRate:"
+ "supportedHDRModesWithCriteria:"
+ "supportedHDRModesWithHighRefreshRate"
+ "supportedHDRModesWithVRR"
+ "transitionWithView:duration:options:animations:completion:"
- "-[DBSColorTemperatureController getBlueLightReductionEnabled:]"
- "getBlueLightReductionEnabled:"
- "setBlueLightReductionEnabled:forSpecifier:"

```
