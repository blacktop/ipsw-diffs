## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1817.2.0.0.0
-  __TEXT.__text: 0x193570
-  __TEXT.__auth_stubs: 0x4e30
-  __TEXT.__objc_stubs: 0x25040
-  __TEXT.__objc_methlist: 0x158d4
-  __TEXT.__const: 0x2b34
+1817.4.1.0.0
+  __TEXT.__text: 0x1934a0
+  __TEXT.__auth_stubs: 0x4ea0
+  __TEXT.__objc_stubs: 0x250e0
+  __TEXT.__objc_methlist: 0x1592c
+  __TEXT.__const: 0x28c4
   __TEXT.__gcc_except_tab: 0x3e50
-  __TEXT.__objc_methname: 0x3524f
-  __TEXT.__cstring: 0x18417
+  __TEXT.__objc_methname: 0x3537c
+  __TEXT.__cstring: 0x18407
   __TEXT.__oslogstring: 0x3d2f
   __TEXT.__objc_classname: 0x439d
-  __TEXT.__objc_methtype: 0x61b3
+  __TEXT.__objc_methtype: 0x61c9
   __TEXT.__dlopen_cstrs: 0x28e
   __TEXT.__ustring: 0x2e
-  __TEXT.__swift5_typeref: 0x7a20
-  __TEXT.__constg_swiftt: 0x11b4
-  __TEXT.__swift5_fieldmd: 0x804
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x44d
-  __TEXT.__swift5_assocty: 0x4b8
-  __TEXT.__swift5_capture: 0x404
-  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_typeref: 0x7a0e
+  __TEXT.__constg_swiftt: 0x11fc
+  __TEXT.__swift5_fieldmd: 0x81c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x49d
+  __TEXT.__swift5_assocty: 0x488
+  __TEXT.__swift5_capture: 0x400
+  __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0x11c
-  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x5e68
-  __TEXT.__eh_frame: 0xb20
-  __DATA_CONST.__auth_got: 0x2728
-  __DATA_CONST.__got: 0x24e8
-  __DATA_CONST.__auth_ptr: 0x740
-  __DATA_CONST.__const: 0x5a90
-  __DATA_CONST.__cfstring: 0x1cc60
-  __DATA_CONST.__objc_classlist: 0xeb8
+  __TEXT.__unwind_info: 0x5e70
+  __TEXT.__eh_frame: 0xb90
+  __DATA_CONST.__auth_got: 0x2760
+  __DATA_CONST.__got: 0x24b0
+  __DATA_CONST.__auth_ptr: 0x770
+  __DATA_CONST.__const: 0x5aa0
+  __DATA_CONST.__cfstring: 0x1cd00
+  __DATA_CONST.__objc_classlist: 0xec0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xb30
+  __DATA_CONST.__objc_superrefs: 0xb38
   __DATA_CONST.__objc_intobj: 0x1db8
   __DATA_CONST.__objc_arraydata: 0x12f8
   __DATA_CONST.__objc_arrayobj: 0x738
   __DATA_CONST.__objc_doubleobj: 0x1c0
   __DATA_CONST.__objc_dictobj: 0xaa0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x1e740
-  __DATA.__objc_selrefs: 0xcdc8
-  __DATA.__objc_ivar: 0xe68
-  __DATA.__objc_data: 0x9ee8
-  __DATA.__data: 0x3dc8
-  __DATA.__bss: 0x2530
+  __DATA.__objc_const: 0x1e840
+  __DATA.__objc_selrefs: 0xcdf0
+  __DATA.__objc_ivar: 0xe6c
+  __DATA.__objc_data: 0x9f08
+  __DATA.__data: 0x3dd0
+  __DATA.__bss: 0x2020
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore
   - /System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices
-  - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7EFA9ECA-BEF7-3D3F-AE6E-E2E14A310DD5
-  Functions: 8812
-  Symbols:   19975
-  CStrings:  17093
+  UUID: 8B1B6E16-7765-3E15-A7F2-1C05E104FBE6
+  Functions: 8794
+  Symbols:   19981
+  CStrings:  17109
 
Symbols:
+ -[AXSwitchTableCell refreshCellContentsWithSpecifier:]
+ -[AccessibilitySettingsController deferredURLStateUpdated:]
+ -[AccessibilitySettingsController deferredURLState]
+ -[AccessibilitySettingsController handleResourcesDictionaryDidChange:]
+ -[AccessibilitySettingsController setDeferredURLState:]
+ -[AccessibilitySettingsController setSpecifier:]
+ -[TypingFeedbackController quickTypePredictionFeedbackEnabled:]
+ -[TypingFeedbackController setQuickTypePredictionFeedbackEnabled:specifier:]
+ -[VoiceOverBrailleUIController setShowsBackButton:specifier:]
+ -[VoiceOverBrailleUIController showsBackButton:]
+ GCC_except_table72
+ OBJC_IVAR_$_AccessibilitySettingsController._deferredURLState
+ _AXAssistiveTouchDisallowedBaseActions
+ _OBJC_CLASS_$_AXDeferredURLState
+ _OBJC_CLASS_$_PESettingsFeatureDescriptionCell
+ _OBJC_CLASS_$_PSListControllerCellHighlightingSelectionInvocationRelay
+ _OBJC_METACLASS_$_AXDeferredURLState
+ _PSAXDeferredURLStateKey
+ _PSListControllerCellHighlightingSelectionInvocationRelayKey
+ _PSTableCellSubtitleTextKey
+ __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.491
+ __DATA_AXDeferredURLState
+ __DATA__TtC21AccessibilitySettings33AccessibilitySettingsPluginLoader
+ __INSTANCE_METHODS_AXDeferredURLState
+ __IVARS_AXDeferredURLState
+ __METACLASS_DATA_AXDeferredURLState
+ __METACLASS_DATA__TtC21AccessibilitySettings33AccessibilitySettingsPluginLoader
+ __OBJC_$_INSTANCE_METHODS_AXSwitchTableCell
+ __PROPERTIES_AXDeferredURLState
+ ___72-[AXDisplayTextMotionSpecifiersHelper setDarkenColorsEnabled:specifier:]_block_invoke
+ __block_literal_global.465
+ __block_literal_global.467
+ __block_literal_global.493
+ __block_literal_global.495
+ __block_literal_global.531
+ __block_literal_global.584
+ __block_literal_global.915
+ __block_literal_global.942
+ _associated conformance 21AccessibilitySettings0aB12PluginLoaderC0B001_b10ExperienceC7LoadingAA4BodyAdEP_AD0bE0
+ _associated conformance 21AccessibilitySettingsAAV0B00B10ExperienceAA4BodyAcDP_AC0bC7Content
+ _objc_msgSend$handleResourcesDictionaryDidChange:
+ _objc_msgSend$handleURL:withCompletion:
+ _objc_msgSend$pe_isSettingsFeatureDescriptionCellSupported
+ _objc_msgSend$quickTypePredictionFeedbackEnabled
+ _objc_msgSend$resourcesDictionary
+ _objc_msgSend$setDeferredURLState:
+ _objc_msgSend$setQuickTypePredictionFeedbackEnabled:
+ _objc_msgSend$setVoiceOverTouchBrailleUIShowsBackButton:
+ _objc_msgSend$voiceOverTouchBrailleUIShowsBackButton
+ _symbolic $s8Settings01_A23ExperiencePluginLoadingP
+ _symbolic $s8Settings0A10ExperienceP
+ _symbolic SDySS_____GSg s11AnyHashableV
+ _symbolic SS_SSt
+ _symbolic So56PSListControllerCellHighlightingSelectionInvocationRelayC
+ _symbolic _____ 21AccessibilitySettings0aB12PluginLoaderC
+ _symbolic _____ 21AccessibilitySettings16DeferredURLStateC
+ _symbolic _____ 21AccessibilitySettingsAAV
+ _symbolic _____Sg 10Foundation13URLComponentsV
+ _symbolic _____yAAy_____y_____y______SSQo__Qo______G_____G 7SwiftUI15ModifiedContentV AA4ViewPAAE29navigationBarTitleDisplayModeyQrAA010NavigationG4ItemV0hiJ0OFQO AeAE0fH0yQrqd__SyRd__lFQO 21AccessibilitySettings013SwitchDetailsE10ControllerV AA30_SafeAreaRegionsIgnoringLayoutV AA25_AppearanceActionModifierV
+ _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____y______SSQo_ 7SwiftUI4ViewPAAE15navigationTitleyQrqd__SyRd__lFQO 19PreferencesExtended0f10ControllerC0V
+ _symbolic _____y_____y______SSQo_G 8Settings0A4PaneV 7SwiftUI4ViewPADE15navigationTitleyQrqd__SyRd__lFQO 19PreferencesExtended0h10ControllerE0V
+ _symbolic _____y_____y______y_____G_____y_____y_____yAFy______A2ISgtGG_____y__________y_____GGG_AFy_____Sg_AItGSgtGGAMyAMy_____y_____y______SSQo__Qo______G_____GG 23AccessibilitySettingsUI18AXSUISpecifierLinkV 05SwiftC013_VariadicViewO4TreeV AD11_LayoutRootV AD03AnyJ0V AD05TupleH0V AD5LabelV AD6VStackV AD4TextV AD15ModifiedContentV AD5ImageV AD24_ForegroundStyleModifierV AD5ColorV AD6SpacerV AD0H0PADE29navigationBarTitleDisplayModeyQrAD010NavigationZ4ItemV16TitleDisplayModeOFQO A4_ADE0Y5TitleyQrqd__SyRd__lFQO 0aB0013SwitchDetailsH10ControllerV AD024_SafeAreaRegionsIgnoringJ0V AD017_AppearanceActionV0V
+ _symbolic _____y_____y_____y______SSQo_G_Qo_ 8Settings0A17ExperienceContentPAAE02onaB7OpenURL7performQrAA0abE9URLActionV6ResultVAG5InputVYacn_tFQO AA0A4PaneV 7SwiftUI4ViewPANE15navigationTitleyQrqd__SyRd__lFQO 19PreferencesExtended0q10ControllerN0V
+ _symbolic _____y_____y_____y______y_____G_____y_____y_____yAFy______A2ISgtGG_____y__________y_____GGG_AFy_____Sg_AItGSgtGGAMyAMy_____y_____y______SSQo__Qo______G_____GG_Qo_ 7SwiftUI4ViewP021AccessibilitySettingsB0E11axSpecifieryQrSSFQO AD18AXSUISpecifierLinkV AA09_VariadicC0O4TreeV AA11_LayoutRootV AA03AnyL0V AA05TupleC0V AA5LabelV AA6VStackV AA4TextV AA15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA6SpacerV AcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQO AcAE15navigationTitleyQrqd__SyRd__lFQO 0dE0013SwitchDetailsC10ControllerV AA024_SafeAreaRegionsIgnoringL0V AA017_AppearanceActionX0V
+ _type_layout_string 21AccessibilitySettingsAAV
+ _type_layout_string So13CLFListLayouta
+ get_witness_table qd__7SwiftUI4ViewHD2_AaBP021AccessibilitySettingsB0E11axSpecifieryQrSSFQOyAD18AXSUISpecifierLinkVyAA09_VariadicC0O4TreeVy_AA11_LayoutRootVyAA03AnyL0VGAA05TupleC0VyAA5LabelVyAA6VStackVyARyAA4TextV_A2XSgtGGAA15ModifiedContentVyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGG_ARyAA6SpacerVSg_AXtGSgtGGA1_yA1_yAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0dE0013SwitchDetailsC10ControllerV_SSQo__Qo_AA024_SafeAreaRegionsIgnoringL0VGAA017_AppearanceActionX0VGG_Qo_HO.123
+ get_witness_table qd__8Settings0A17ExperienceContentHD2_AaBPAAE02onaB7OpenURL7performQrAA0abE9URLActionV6ResultVAG5InputVYacn_tFQOyAA0A4PaneVy7SwiftUI4ViewPANE15navigationTitleyQrqd__SyRd__lFQOy19PreferencesExtended0q10ControllerN0V_SSQo_G_Qo_HO.9
- -[AXUIScrollSpeedSlider newControl]
- -[TypingFeedbackController quickTypeWordFeedbackEnabled:]
- -[TypingFeedbackController setQuickTypeWordFeedbackEnabled:specifier:]
- GCC_except_table68
- _AXAssistiveTouchIconTypeCustom
- _AXAssistiveTouchIconTypeDevice
- _AXAssistiveTouchIconTypeDwell
- _AXAssistiveTouchIconTypeGestures
- _AXAssistiveTouchIconTypeRotateScreen
- _AXAssistiveTouchIconTypeScroll
- _AXAssistiveTouchIconTypeSiriShortcutsMenu
- _NSForegroundColorAttributeName
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$__TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell
- _OBJC_METACLASS_$__TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell
- __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.488
- __DATA__TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell
- __INSTANCE_METHODS__TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell
- __METACLASS_DATA__TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell
- __block_literal_global.462
- __block_literal_global.490
- __block_literal_global.492
- __block_literal_global.528
- __block_literal_global.574
- __block_literal_global.905
- __block_literal_global.932
- _associated conformance So21NSAttributedStringKeyaSHSCSQ
- _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCSY
- _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _associated conformance So38UIApplicationOpenExternalURLOptionsKeyaSHSCSQ
- _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCSY
- _associated conformance So38UIApplicationOpenExternalURLOptionsKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _objc_msgSend$quickTypeWordFeedbackEnabled
- _objc_msgSend$setBackButtonTitle:
- _objc_msgSend$setMaximumTrackTintColor:
- _objc_msgSend$setQuickTypeWordFeedbackEnabled:
- _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
- _symbolic So11PSTableCellC
- _symbolic So16UINavigationItemCSg
- _symbolic So7UILabelC
- _symbolic _____ 10Foundation3URLV
- _symbolic _____ 21AccessibilitySettings0aB11PlacardCellC
- _symbolic _____ 7SwiftUI13TextAlignmentO
- _symbolic _____ So21NSAttributedStringKeya
- _symbolic _____ So38UIApplicationOpenExternalURLOptionsKeya
- _symbolic _____Sg 10Foundation3URLV
- _symbolic ______ypt So21NSAttributedStringKeya
- _symbolic ______ypt So38UIApplicationOpenExternalURLOptionsKeya
- _symbolic _____yAAy_____y_____y_____GG_____y_____GG_____G 7SwiftUI15ModifiedContentV 8Settings0E11PlacardViewV 014_IconServices_aB005AsyncH5ImageV AA0K0V AA30_EnvironmentKeyWritingModifierV AA13TextAlignmentO AA023AccessibilityAttachmentO0V
- _symbolic _____y_____G 7SwiftUI30_EnvironmentKeyWritingModifierV AA13TextAlignmentO
- _symbolic _____y______yptG s23_ContiguousArrayStorageC So21NSAttributedStringKeya
- _symbolic _____y_____yABy_____y_____y_____GG_____y_____GG_____G_____G 7SwiftUI22UIHostingConfigurationV AA15ModifiedContentV 8Settings0G11PlacardViewV 014_IconServices_aB005AsyncJ5ImageV AA0M0V AA30_EnvironmentKeyWritingModifierV AA13TextAlignmentO AA023AccessibilityAttachmentQ0V AA05EmptyI0V
- _symbolic _____y_____y_____GG 8Settings0A11PlacardViewV 21_IconServices_SwiftUI05AsyncD5ImageV 0fG00I0V
- _symbolic _____y_____y______y_____G_____y_____y_____yAFy______A2ISgtGG_____y__________y_____GGG_AFy_____Sg_AItGSgtGGAMy_____y_____y______SSQo__Qo______GG 23AccessibilitySettingsUI18AXSUISpecifierLinkV 05SwiftC013_VariadicViewO4TreeV AD11_LayoutRootV AD03AnyJ0V AD05TupleH0V AD5LabelV AD6VStackV AD4TextV AD15ModifiedContentV AD5ImageV AD24_ForegroundStyleModifierV AD5ColorV AD6SpacerV AD0H0PADE29navigationBarTitleDisplayModeyQrAD010NavigationZ4ItemV16TitleDisplayModeOFQO A4_ADE0Y5TitleyQrqd__SyRd__lFQO 0aB0013SwitchDetailsH10ControllerV AD024_SafeAreaRegionsIgnoringJ0V
- _symbolic _____y_____y_____y_____GG_____y_____GG 7SwiftUI15ModifiedContentV 8Settings0E11PlacardViewV 014_IconServices_aB005AsyncH5ImageV AA0K0V AA30_EnvironmentKeyWritingModifierV AA13TextAlignmentO
- _symbolic _____y_____y_____y______y_____G_____y_____y_____yAFy______A2ISgtGG_____y__________y_____GGG_AFy_____Sg_AItGSgtGGAMy_____y_____y______SSQo__Qo______GG_Qo_ 7SwiftUI4ViewP021AccessibilitySettingsB0E11axSpecifieryQrSSFQO AD18AXSUISpecifierLinkV AA09_VariadicC0O4TreeV AA11_LayoutRootV AA03AnyL0V AA05TupleC0V AA5LabelV AA6VStackV AA4TextV AA15ModifiedContentV AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA6SpacerV AcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQO AcAE15navigationTitleyQrqd__SyRd__lFQO 0dE0013SwitchDetailsC10ControllerV AA024_SafeAreaRegionsIgnoringL0V
- _symbolic _____y_____ypG s18_DictionaryStorageC So21NSAttributedStringKeya
- _symbolic _____y_____ypG s18_DictionaryStorageC So38UIApplicationOpenExternalURLOptionsKeya
- _type_layout_string So21NSAttributedStringKeya
- get_witness_table qd__7SwiftUI4ViewHD2_AaBP021AccessibilitySettingsB0E11axSpecifieryQrSSFQOyAD18AXSUISpecifierLinkVyAA09_VariadicC0O4TreeVy_AA11_LayoutRootVyAA03AnyL0VGAA05TupleC0VyAA5LabelVyAA6VStackVyARyAA4TextV_A2XSgtGGAA15ModifiedContentVyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGG_ARyAA6SpacerVSg_AXtGSgtGGA1_yAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0dE0013SwitchDetailsC10ControllerV_SSQo__Qo_AA024_SafeAreaRegionsIgnoringL0VGG_Qo_HO.120
- objectdestroy.80Tm
CStrings:
+ "$"
+ "?"
+ "@\"AXDeferredURLState\""
+ "AXDeferredURLState"
+ "DeferredURLState"
+ "DeferredURLStateUpdated"
+ "MotionCuesAppearanceButtonText"
+ "SHOW_BACK_BUTTON"
+ "SWITCHES_LIST_ALPHABETICAL"
+ "SWITCHES_LIST_SOURCE"
+ "SWITCHES_LIST_STATE"
+ "T@\"AXDeferredURLState\",&,N,V_deferredURLState"
+ "T@\"NSDictionary\",N,C"
+ "_TtC21AccessibilitySettings33AccessibilitySettingsPluginLoader"
+ "_deferredURLState"
+ "deferredURLState"
+ "deferredURLStateUpdated:"
+ "handleResourcesDictionaryDidChange:"
+ "handleURL:withCompletion:"
+ "pe_isSettingsFeatureDescriptionCellSupported"
+ "quickTypePredictionFeedbackEnabled"
+ "quickTypePredictionFeedbackEnabled:"
+ "resourcesDictionary"
+ "setDeferredURLState:"
+ "setQuickTypePredictionFeedbackEnabled:"
+ "setQuickTypePredictionFeedbackEnabled:specifier:"
+ "setResourcesDictionary:"
+ "setShowsBackButton:specifier:"
+ "setVoiceOverTouchBrailleUIShowsBackButton:"
+ "showsBackButton:"
+ "voiceOverTouchBrailleUIShowsBackButton"
- "#"
- "AX_SETTINGS_PLACARD_VIEW"
- "Alphabetical (Default)"
- "PLACARD_LEARN_MORE"
- "UICTFontTextStyleShortEmphasizedBody"
- "_TtC21AccessibilitySettings32AccessibilitySettingsPlacardCell"
- "canOpenURL:"
- "helpkit://open?topic=ipad9a2465f9"
- "helpkit://open?topic=iph3e2e4367"
- "newControl"
- "openURL:options:completionHandler:"
- "quickTypeWordFeedbackEnabled"
- "quickTypeWordFeedbackEnabled:"
- "setAttributedText:"
- "setBackButtonTitle:"
- "setMaximumTrackTintColor:"
- "setQuickTypeWordFeedbackEnabled:"
- "setQuickTypeWordFeedbackEnabled:specifier:"
- "target"

```
