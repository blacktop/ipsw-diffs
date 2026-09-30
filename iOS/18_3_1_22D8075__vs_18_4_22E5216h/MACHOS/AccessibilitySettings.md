## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1773.3.10.0.0
-  __TEXT.__text: 0x1620b0
-  __TEXT.__auth_stubs: 0x42f0
-  __TEXT.__objc_stubs: 0x22640
-  __TEXT.__objc_methlist: 0x11c24
-  __TEXT.__const: 0x1a10
-  __TEXT.__gcc_except_tab: 0x3294
-  __TEXT.__objc_methname: 0x30bee
-  __TEXT.__cstring: 0x1748c
-  __TEXT.__oslogstring: 0x37cd
-  __TEXT.__objc_classname: 0x3f0c
-  __TEXT.__objc_methtype: 0x5dae
+1773.7.4.0.0
+  __TEXT.__text: 0x15f794
+  __TEXT.__auth_stubs: 0x4280
+  __TEXT.__objc_stubs: 0x22520
+  __TEXT.__objc_methlist: 0x1362c
+  __TEXT.__const: 0x1b80
+  __TEXT.__gcc_except_tab: 0x3290
+  __TEXT.__objc_methname: 0x30b9c
+  __TEXT.__cstring: 0x1729c
+  __TEXT.__oslogstring: 0x382d
+  __TEXT.__objc_classname: 0x3f2f
+  __TEXT.__objc_methtype: 0x5e20
   __TEXT.__dlopen_cstrs: 0x28e
   __TEXT.__ustring: 0x2e
-  __TEXT.__swift5_typeref: 0x2050
+  __TEXT.__swift5_typeref: 0x2012
   __TEXT.__constg_swiftt: 0xa54
   __TEXT.__swift5_fieldmd: 0x484
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x14c
-  __TEXT.__unwind_info: 0x5128
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__unwind_info: 0x5068
   __TEXT.__eh_frame: 0x170
-  __DATA_CONST.__auth_got: 0x2188
-  __DATA_CONST.__got: 0x2168
+  __DATA_CONST.__auth_got: 0x2150
+  __DATA_CONST.__got: 0x2150
   __DATA_CONST.__auth_ptr: 0x4b0
-  __DATA_CONST.__const: 0x4be8
-  __DATA_CONST.__cfstring: 0x1a220
-  __DATA_CONST.__objc_classlist: 0xd70
+  __DATA_CONST.__const: 0x4c80
+  __DATA_CONST.__cfstring: 0x1a3a0
+  __DATA_CONST.__objc_classlist: 0xd78
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa50
-  __DATA_CONST.__objc_intobj: 0x19b0
+  __DATA_CONST.__objc_superrefs: 0xa58
+  __DATA_CONST.__objc_intobj: 0x19f8
   __DATA_CONST.__objc_arraydata: 0x12b0
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x1c0
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0xa78
-  __DATA.__objc_const: 0x1ed18
-  __DATA.__objc_selrefs: 0xb500
+  __DATA.__objc_const: 0x1bf38
+  __DATA.__objc_selrefs: 0xbdb0
   __DATA.__objc_ivar: 0xd54
-  __DATA.__objc_data: 0x8c60
+  __DATA.__objc_data: 0x8cb0
   __DATA.__data: 0x2b52
-  __DATA.__bss: 0x18fd
+  __DATA.__bss: 0x1900
   __DATA.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/HearingUI.framework/HearingUI
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/HelpKit.framework/HelpKit
-  - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7693
-  Symbols:   18318
-  CStrings:  12547
+  Functions: 7795
+  Symbols:   18475
+  CStrings:  12542
 
Symbols:
+ +[AXLargeTextController initialize].cold.1
+ +[AXVoiceOverTraitFeedbackController descriptionForOption:]
+ +[ClarityUIAppSetupCoordinator sharedInstance].cold.1
+ +[SoundActionsAssetsDownloadManager sharedInstance].cold.1
+ +[SoundActionsPracticeAudioManager sharedInstance].cold.1
+ +[SoundActionsPracticeUtilities sharedInstance].cold.1
+ -[AXAssistiveTouchSoundActionsController supportsIconType:].cold.1
+ -[AXCallAudioRoutingDelayController _showSiriSettings:]
+ -[AXCallAudioRoutingDelayController configureSpecifier:]
+ -[AXPronunciationEntryViewController _assetUpdaterClient].cold.1
+ -[AXPronunciationEntryViewController _canSpeakSample]
+ -[AXPronunciationEntryViewController viewDidLoad].cold.1
+ -[AXPronunciationListViewController _assetUpdaterClient].cold.1
+ -[AXReorderableCheckmarkListController _updateCell:forIndexPath:].cold.1
+ -[AXVocabularyListController viewDidAppear:]
+ -[AXVoiceOverTraitFeedbackController specifiers]
+ -[AXVoiceOverTraitFeedbackController tableView:didSelectRowAtIndexPath:]
+ -[AXVoiceOverTraitFeedbackController tableView:willDisplayCell:forRowAtIndexPath:]
+ -[AccessibilitySettingsBaseController detailClassForFeature:].cold.1
+ -[AccessibilitySettingsController specifiers].cold.1
+ -[ClarityUIAppSetupCoordinator _bundleIdentifierProvidesOwnSettings:].cold.1
+ -[ClarityUISettingsWrapperController _axValidateAuthenticationController].cold.2
+ -[ClarityUISettingsWrapperController _axValidateAuthenticationController].cold.3
+ -[ClarityUISettingsWrapperController _axValidateAuthenticationController].cold.4
+ -[ClarityUISettingsWrapperController _axValidateAuthenticationController].cold.5
+ -[CustomGestureController nameForItem:].cold.1
+ -[GuidedAccessAutoLockController specifiers].cold.1
+ -[HoverTextFontPickerViewController _isDisallowedFontFamily:].cold.1
+ -[SCATSwitchSourceController _shouldEnableCameraSource].cold.1
+ -[VoiceOverAudioController _interestingOutputDevices].cold.1
+ -[VoiceOverVerbosityController traitFeedbackString:]
+ ACMContextGetExternalForm.cold.1
+ AXAssetAndDataClient.cold.1
+ AXCaptionColors.cold.1
+ AXCaptionFonts.cold.1
+ AXCaptionTextEdgeStyles.cold.1
+ AXCaptionTextSizes.cold.1
+ AXCaptionTransparency.cold.1
+ AXFlipsIconRightToLeftForAppID.cold.1
+ GAXSLocString.cold.1
+ GAXSTimeRestrictionsLocString.cold.1
+ GCC_except_table64
+ _OBJC_CLASS_$_AXVoiceOverTraitFeedbackController
+ _OBJC_METACLASS_$_AXVoiceOverTraitFeedbackController
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_AXVoiceOverTraitFeedbackController
+ __OBJC_$_INSTANCE_METHODS_AXVoiceOverTraitFeedbackController
+ __OBJC_CLASS_RO_$_AXVoiceOverTraitFeedbackController
+ __OBJC_METACLASS_RO_$_AXVoiceOverTraitFeedbackController
+ ___42-[VoiceOverVerbosityController specifiers]_block_invoke_20
+ ___42-[VoiceOverVerbosityController specifiers]_block_invoke_21
+ ___43-[VoiceOverVerbosityController viewDidLoad]_block_invoke_14
+ ___74-[AssistiveTouchCustomizeBaseActionPickerController localizedSortedIcons:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___swift_async_entry_functlets
+ __block_literal_global.379
+ __block_literal_global.398
+ __block_literal_global.400
+ __block_literal_global.414
+ __block_literal_global.418
+ __block_literal_global.437
+ __block_literal_global.439
+ __block_literal_global.451
+ __block_literal_global.455
+ __block_literal_global.464
+ __block_literal_global.476
+ __block_literal_global.486
+ __block_literal_global.488
+ __block_literal_global.510
+ __block_literal_global.533
+ __block_literal_global.539
+ __block_literal_global.541
+ __block_literal_global.560
+ __block_literal_global.562
+ __block_literal_global.842
+ __block_literal_global.870
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AccessibilitySettings
+ _objc_msgSend$_canSpeakSample
+ _objc_msgSend$isEmergencyRTTSupportedForContext:
+ _objc_msgSend$isEmergencyRelayRTTSupported
+ _objc_msgSend$resolvedVoiceIdentifierForLanguageCode:
+ _objc_msgSend$setVoiceOverTraitFeedback:
+ _objc_msgSend$voiceOverTraitFeedback
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _type_layout_string 21AccessibilitySettings23SpokenContentVoicesViewV
+ _type_layout_string 21AccessibilitySettings24ClarityOnboardingChevronV
+ _type_layout_string 21AccessibilitySettings32SpokenContentDetectLanguagesViewV
+ _type_layout_string 21AccessibilitySettings32SpokenContentDetectLanguagesViewV13SelectionCellV
+ _type_layout_string 21AccessibilitySettings34ClarityLockScreenDevicePreviewViewV
+ _type_layout_string 21AccessibilitySettings34ClarityOnboardingAdminSettingGroupV
+ _type_layout_string 21AccessibilitySettings34ClarityOnboardingDevicePreviewViewV
+ _type_layout_string 21AccessibilitySettings36ClarityOnboardingBackButtonRectangleV
+ _type_layout_string 21AccessibilitySettings39ClarityOnboardingDeviceAdminPreviewViewV
+ _type_layout_string 21AccessibilitySettings40ClarityOnboardingDeviceBackgroundAndAppsV
+ _type_layout_string 21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleV
+ _type_layout_string So21NSAttributedStringKeya
+ _type_layout_string So26AXSVoiceOverFeedbackOptionV
+ get_aks_client_connection.cold.1
+ get_witness_table 7SwiftUI15ModifiedContentVy21AccessibilitySettings38ClarityOnboardingAdminSettingRectangleVAA16_OverlayModifierVyAD0gH6ToggleVGGAA4ViewHPAfaMHPyHC_AkA0oM0HPyHCHC.28
+ get_witness_table 7SwiftUI15ModifiedContentVy21AccessibilitySettings38ClarityOnboardingAdminSettingRectangleVAA16_OverlayModifierVyAD0gH7ChevronVGGAA4ViewHPAfaMHPyHC_AkA0oM0HPyHCHC.27
+ get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyAA6HStackVyAA05TupleE0VyAA4TextV_AA6SpacerVAeAE10fontWeightyQrAA4FontV0Q0VSgFQOyACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGG_Qo_SgtGGAA01_d5ShapeV0VyAA9RectangleVGG_Qo_AA0i10AttachmentV0VGAaDHPqd__AaDHD2_A14_HO_A16_AA0eV0HPyHCHC.23
+ get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVG_ACyAA09_VariadicG0O4TreeVy_AA11_LayoutRootVyAA03AnyS0VGAGyACyAjA012_AspectRatioS0VG_ACyAjA010_FlexFrameS0VGtGGAA08_PaddingS0VGtGGA_GAA0G0HPA7_AAA9_HPyHC_A_AA0G8ModifierHPyHCHC.43
+ get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVGAA14_PaddingLayoutVG_ACyAjA010_FlexFrameR0VGtGGARGAA0G0HPAuaWHPyHC_ArA0G8ModifierHPyHCHC.44
+ get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings33ClarityOnboardingDeviceLockScreenVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0pO0HPyHCHC_AkaNHPyHCHC.23
+ get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings40ClarityOnboardingDeviceBackgroundAndAppsVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0qP0HPyHCHC_AkaNHPyHCHC.22
+ get_witness_table 7SwiftUI15ModifiedContentVyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedE0VGGAA4ViewHPAkaRHPAeaRHPyHC_AjA0mH0HPyHCHC_ApaSHPyHCHC.45
+ get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA08_OverlayH0VyAA10_ShapeViewVyAA08_StrokedK0VyAE6_InsetVGAIGGGAA12_FrameLayoutVGAA0L0HPAwAA_HPAkAA_HPAeAA_HPyHC_AjA0lH0HPyHCHC_AvAA0_HPyHCHC_AyAA0_HPyHCHC.26
+ get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA5ImageVAA18_AspectRatioLayoutVGAA24_ForegroundStyleModifierVyAA5ColorVGGAA06_FrameH0VGAA08_PaddingH0VGAA4ViewHPAqaUHPAnaUHPAhaUHPAeaUHPyHC_AgA0oK0HPyHCHC_AmaVHPyHCHC_ApaVHPyHCHC_AsaVHPyHCHC.29
+ get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEyAEyAEyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedF0VGGAA14_PaddingLayoutVGAA06_FrameO0VGAYGAA4ViewHPAyAA_HPAvAA_HPAsAA_HPAmAA_HPAgAA_HPyHC_AlA0qI0HPyHCHC_ArAA0_HPyHCHC_AuAA0_HPyHCHC_AxAA0_HPyHCHC_AyAA_HPAvAA_HPAsAA_HPAmAA_HPAgAA_HPyHC_AlAA0_HPyHCHC_ArAA0_HPyHCHC_AuAA0_HPyHCHC_AxAA0_HPyHCHCHC.13
+ get_witness_table 7SwiftUI6VStackVyAA9TupleViewVy21AccessibilitySettings35ClarityOnboardingAdminToggleSettingV_AF0hij4ListL0VAjA15ModifiedContentVyAA6SpacerVAA12_FrameLayoutVGAF0hijL9RectangleVtGGAA0E0HPyHC.14
+ get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGG_AGyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameS0VGATGSgAA6VStackVyAEyAGyAA6SpacerVA0_G_AGy21AccessibilitySettings024ClarityOnboardingPreviewoH0VAA05_FlextS0VGA7_A9_0Y23LockScreenPreviewButtonVtGGtGGAA0E0HPyHC.42
+ get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA7CapsuleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA12_FrameLayoutVGAA08_PaddingN0VG_AA012_ConditionalG0VyAGyAGyAGyAGyAA6CircleVANGAQGATGAA13_OffsetEffectVGA3_GtGGAA0E0HPyHC.30
+ get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGGAA07_ShadowN0VG_AGyAGyAA6VStackVyAEyAGyAA6SpacerVAA12_FrameLayoutVG_AA7ForEachVySnySiGSi21AccessibilitySettings33ClarityOnboardingPreviewAppButtonVGtGGAA08_PaddingT0VGAA08_OpacityN0VGAGyAZyAEyA3__AGyAA9LazyVGridVyA10_GA14_GtGGA17_GtGGAA0E0HPyHC.41
+ updateLogLevelFromKext.cold.1
- -[AccessibilitySettingsController _customGraphicIconWithSymbol:systemColor:]
- -[AccessibilitySettingsController _customGraphicIconWithSymbol:systemColor:bundleURL:]
- -[AccessibilitySettingsController _customGraphicIconWithSymbol:systemColor:useHierarchical:]
- -[AccessibilitySettingsController _graphicIconForBundleIdentifier:]
- -[AccessibilitySettingsController _iconImageFromISIcon:]
- -[AccessibilitySettingsController _predefinedGraphicIconNamed:]
- -[AccessibilitySettingsController _shouldUseGraphicsRecipes]
- GCC_except_table71
- _AXResizeImageWithSize
- _OBJC_CLASS_$_IFColor
- _OBJC_CLASS_$_IFGraphicSymbolDescriptor
- _OBJC_CLASS_$_IFSymbol
- _OBJC_CLASS_$_ISIcon
- _OBJC_CLASS_$_PKIconImageCache
- _PKHomeScreenIconKey
- __block_literal_global.399
- __block_literal_global.403
- __block_literal_global.422
- __block_literal_global.424
- __block_literal_global.434
- __block_literal_global.440
- __block_literal_global.446
- __block_literal_global.471
- __block_literal_global.473
- __block_literal_global.508
- __block_literal_global.524
- __block_literal_global.526
- __block_literal_global.540
- __block_literal_global.545
- __block_literal_global.848
- __block_literal_global.875
- __connect
- __initialized
- __isNullOrEqualMem2
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AccessibilitySettings
- _objc_msgSend$_customGraphicIconWithSymbol:systemColor:useHierarchical:
- _objc_msgSend$_iconImageFromISIcon:
- _objc_msgSend$_shouldUseGraphicsRecipes
- _objc_msgSend$imageForGraphicSymbolDescriptor:
- _objc_msgSend$imageForImageDescriptor:
- _objc_msgSend$imageForKey:
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$initWithSize:scale:
- _objc_msgSend$initWithSymbolName:bundleURL:
- _objc_msgSend$initWithSystemColor:
- _objc_msgSend$isRTTSupported
- _objc_msgSend$setEnclosureColors:
- _objc_msgSend$setRenderingMode:
- _objc_msgSend$setSymbolColors:
- _objc_msgSend$settingsIconCache
- _objc_retain_x11
- _swift_initStructMetadata
- _symbolic _____y_____yAByAByABy__________y_____GG_____G_____G_____GAM_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA6CircleV AA24_ForegroundStyleModifierV AA5ColorV AA12_FrameLayoutV AA08_PaddingM0V AA13_OffsetEffectV
- get_witness_table 7SwiftUI15ModifiedContentVy21AccessibilitySettings38ClarityOnboardingAdminSettingRectangleVAA16_OverlayModifierVyAD0gH6ToggleVGGAA4ViewHPAfaMHPyHC_AkA0oM0HPyHCHC.15
- get_witness_table 7SwiftUI15ModifiedContentVy21AccessibilitySettings38ClarityOnboardingAdminSettingRectangleVAA16_OverlayModifierVyAD0gH7ChevronVGGAA4ViewHPAfaMHPyHC_AkA0oM0HPyHCHC.14
- get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyAA6HStackVyAA05TupleE0VyAA4TextV_AA6SpacerVAeAE10fontWeightyQrAA4FontV0Q0VSgFQOyACyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGG_Qo_SgtGGAA01_d5ShapeV0VyAA9RectangleVGG_Qo_AA0i10AttachmentV0VGAaDHPqd__AaDHD2_A14_HO_A16_AA0eV0HPyHCHC.18
- get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVG_ACyAA09_VariadicG0O4TreeVy_AA11_LayoutRootVyAA03AnyS0VGAGyACyAjA012_AspectRatioS0VG_ACyAjA010_FlexFrameS0VGtGGAA08_PaddingS0VGtGGA_GAA0G0HPA7_AAA9_HPyHC_A_AA0G8ModifierHPyHCHC.26
- get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVGAA14_PaddingLayoutVG_ACyAjA010_FlexFrameR0VGtGGARGAA0G0HPAuaWHPyHC_ArA0G8ModifierHPyHCHC.27
- get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings33ClarityOnboardingDeviceLockScreenVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0pO0HPyHCHC_AkaNHPyHCHC.12
- get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings40ClarityOnboardingDeviceBackgroundAndAppsVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0qP0HPyHCHC_AkaNHPyHCHC.11
- get_witness_table 7SwiftUI15ModifiedContentVyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedE0VGGAA4ViewHPAkaRHPAeaRHPyHC_AjA0mH0HPyHCHC_ApaSHPyHCHC.28
- get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA08_OverlayH0VyAA10_ShapeViewVyAA08_StrokedK0VyAE6_InsetVGAIGGGAA12_FrameLayoutVGAA0L0HPAwAA_HPAkAA_HPAeAA_HPyHC_AjA0lH0HPyHCHC_AvAA0_HPyHCHC_AyAA0_HPyHCHC.13
- get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA5ImageVAA18_AspectRatioLayoutVGAA24_ForegroundStyleModifierVyAA5ColorVGGAA06_FrameH0VGAA08_PaddingH0VGAA4ViewHPAqaUHPAnaUHPAhaUHPAeaUHPyHC_AgA0oK0HPyHCHC_AmaVHPyHCHC_ApaVHPyHCHC_AsaVHPyHCHC.16
- get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEyAEyAEyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedF0VGGAA14_PaddingLayoutVGAA06_FrameO0VGAYGAA4ViewHPAyAA_HPAvAA_HPAsAA_HPAmAA_HPAgAA_HPyHC_AlA0qI0HPyHCHC_ArAA0_HPyHCHC_AuAA0_HPyHCHC_AxAA0_HPyHCHC_AyAA_HPAvAA_HPAsAA_HPAmAA_HPAgAA_HPyHC_AlAA0_HPyHCHC_ArAA0_HPyHCHC_AuAA0_HPyHCHC_AxAA0_HPyHCHCHC.10
- get_witness_table 7SwiftUI6VStackVyAA9TupleViewVy21AccessibilitySettings35ClarityOnboardingAdminToggleSettingV_AF0hij4ListL0VAjA15ModifiedContentVyAA6SpacerVAA12_FrameLayoutVGAF0hijL9RectangleVtGGAA0E0HPyHC.11
- get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGG_AGyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameS0VGATGSgAA6VStackVyAEyAGyAA6SpacerVA0_G_AGy21AccessibilitySettings024ClarityOnboardingPreviewoH0VAA05_FlextS0VGA7_A9_0Y23LockScreenPreviewButtonVtGGtGGAA0E0HPyHC.25
- get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA7CapsuleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA12_FrameLayoutVGAA08_PaddingN0VG_AA012_ConditionalG0VyAGyAGyAGyAGyAA6CircleVANGAQGATGAA13_OffsetEffectVGA3_GtGGAA0E0HPyHC.17
- get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGGAA07_ShadowN0VG_AGyAGyAA6VStackVyAEyAGyAA6SpacerVAA12_FrameLayoutVG_AA7ForEachVySnySiGSi21AccessibilitySettings33ClarityOnboardingPreviewAppButtonVGtGGAA08_PaddingT0VGAA08_OpacityN0VGAGyAZyAEyA3__AGyAA9LazyVGridVyA10_GA14_GtGGA17_GtGGAA0E0HPyHC.24
CStrings:
+ "ASTVirtualTrackpadToggleFooter"
+ "AXSVoiceOverTraitFeedback"
+ "AXVoiceOverTraitFeedbackController"
+ "BrailleKeyboardInput"
+ "CHANGE_ADMIN_PASSCODE_FOOTER"
+ "FEEDBACK_SPEAK_AFTER"
+ "FEEDBACK_SPEAK_BEFORE"
+ "FEEDBACK_SPEAK_NONE"
+ "Per-App Settings Controller: remove app %{sensitive}@"
+ "Per-App Settings Controller: setEditing %d"
+ "RTT_CALL_ANSWER"
+ "RTT_SOFTWARE_NO_EMERGENCY_FOOTER_FACETIME"
+ "RTT_SOFTWARE_NO_EMERGENCY_FOOTER_PHONE"
+ "TRAIT_FEEDBACK"
+ "_canSpeakSample"
+ "_showSiriSettings:"
+ "assistantConnection:replayAll:with:"
+ "assistantConnection:replayAt:with:"
+ "assistantConnection:setReplayEnabled:"
+ "assistantConnection:setReplayOverridePath:"
+ "com.apple.graphic-icon.notifications"
+ "configureSpecifier:"
+ "isEmergencyRTTSupportedForContext:"
+ "isEmergencyRelayRTTSupported"
+ "pencil"
+ "prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRI_SETTINGS_VOICE_ACTIVATION_ALWAYS_ALLOW"
+ "resolvedVoiceIdentifierForLanguageCode:"
+ "setVoiceOverTraitFeedback:"
+ "textField:insertInputSuggestion:"
+ "traitFeedbackString:"
+ "v24@0:8^@16"
+ "v32@0:8@\"AFConnection\"16@\"NSURL\"24"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v40@0:8@\"AFConnection\"16Q24@\"NSURL\"32"
+ "v40@0:8@16Q24@32"
+ "voiceOverTraitFeedback"
- "@36@0:8@16q24B32"
- "@40@0:8@16q24@32"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "ENTER_BRAILLE_CHORDS_ON_KEYBOARD"
- "ENTER_BRAILLE_CHORDS_ON_KEYBOARD_FOOTER"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Pencil"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_customGraphicIconWithSymbol:systemColor:"
- "_customGraphicIconWithSymbol:systemColor:bundleURL:"
- "_customGraphicIconWithSymbol:systemColor:useHierarchical:"
- "_graphicIconForBundleIdentifier:"
- "_iconImageFromISIcon:"
- "_predefinedGraphicIconNamed:"
- "_shouldUseGraphicsRecipes"
- "imageForGraphicSymbolDescriptor:"
- "imageForImageDescriptor:"
- "imageWithCGImage:"
- "initWithSize:scale:"
- "initWithSymbolName:bundleURL:"
- "initWithSystemColor:"
- "invalid Collection: less than 'count' elements in collection"
- "isRTTSupported"
- "setEnclosureColors:"
- "setRenderingMode:"
- "setSymbolColors:"
- "settingsIconCache"

```
