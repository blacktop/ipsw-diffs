## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1817.4.3.0.0
-  __TEXT.__text: 0x1958e4
-  __TEXT.__auth_stubs: 0x4ea0
-  __TEXT.__objc_stubs: 0x25120
-  __TEXT.__objc_methlist: 0x15954
-  __TEXT.__const: 0x3494
-  __TEXT.__gcc_except_tab: 0x3e50
-  __TEXT.__objc_methname: 0x35407
-  __TEXT.__cstring: 0x184b7
+1817.4.7.0.0
+  __TEXT.__text: 0x196360
+  __TEXT.__auth_stubs: 0x4ec0
+  __TEXT.__objc_stubs: 0x25240
+  __TEXT.__objc_methlist: 0x159d4
+  __TEXT.__const: 0x34c4
+  __TEXT.__gcc_except_tab: 0x3e74
+  __TEXT.__objc_methname: 0x35677
+  __TEXT.__cstring: 0x18587
   __TEXT.__oslogstring: 0x3d2f
   __TEXT.__objc_classname: 0x439d
-  __TEXT.__objc_methtype: 0x61c9
+  __TEXT.__objc_methtype: 0x61d1
   __TEXT.__dlopen_cstrs: 0x28e
   __TEXT.__ustring: 0x2e
   __TEXT.__swift5_typeref: 0x7a0e

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x49d
   __TEXT.__swift5_assocty: 0x488
-  __TEXT.__swift5_capture: 0x400
+  __TEXT.__swift5_capture: 0x410
   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0x11c
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x5e58
+  __TEXT.__unwind_info: 0x5e88
   __TEXT.__eh_frame: 0xb90
-  __DATA_CONST.__auth_got: 0x2760
+  __DATA_CONST.__auth_got: 0x2770
   __DATA_CONST.__got: 0x24b0
   __DATA_CONST.__auth_ptr: 0x770
-  __DATA_CONST.__const: 0x5aa0
-  __DATA_CONST.__cfstring: 0x1cda0
+  __DATA_CONST.__const: 0x5ab0
+  __DATA_CONST.__cfstring: 0x1cea0
   __DATA_CONST.__objc_classlist: 0xec0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xb38
-  __DATA_CONST.__objc_intobj: 0x1db8
+  __DATA_CONST.__objc_superrefs: 0xb40
+  __DATA_CONST.__objc_intobj: 0x1e00
   __DATA_CONST.__objc_arraydata: 0x12f8
   __DATA_CONST.__objc_arrayobj: 0x738
   __DATA_CONST.__objc_doubleobj: 0x1c0
   __DATA_CONST.__objc_dictobj: 0xaa0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x1e840
-  __DATA.__objc_selrefs: 0xce10
-  __DATA.__objc_ivar: 0xe6c
+  __DATA.__objc_const: 0x1e890
+  __DATA.__objc_selrefs: 0xce80
+  __DATA.__objc_ivar: 0xe74
   __DATA.__objc_data: 0x9f08
   __DATA.__data: 0x3dd0
   __DATA.__bss: 0x2020

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C43D914C-D0F8-38FB-82F6-5BFFBB21D070
-  Functions: 8807
-  Symbols:   19986
-  CStrings:  17123
+  UUID: 08DD5998-4E5A-343A-9151-654F716E104B
+  Functions: 8821
+  Symbols:   20011
+  CStrings:  17156
 
Symbols:
+ -[AXFlashForLEDController tableView:didSelectRowAtIndexPath:]
+ -[ButtonClickController eligibilityDidChange]
+ -[ButtonClickController refreshAssistantSpecifiers]
+ -[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:isReverse:]
+ -[ClarityUIAdminPasscodeSetupController _constraintsForPasscodeInputView:position:bottomConstraint:horizontalConstraint:]
+ -[ClarityUIAdminPasscodeSetupController _horizontalConstraintForPasscodeInputView:position:]
+ -[ClarityUIAdminPasscodeSetupController passcodeHorizontalConstraint]
+ -[ClarityUIAdminPasscodeSetupController setPasscodeHorizontalConstraint:]
+ -[VoiceOverTypingController isQuickNavEnabled]
+ -[VoiceOverTypingController isSingleLetterQuickNavEnabled]
+ -[VoiceOverTypingController setQuickNavEnabled:]
+ -[VoiceOverTypingController setSingleLetterQuickNavEnabled:]
+ OBJC_IVAR_$_ButtonClickController._shouldRestrictAssistantSpecifiers
+ OBJC_IVAR_$_ClarityUIAdminPasscodeSetupController._passcodeHorizontalConstraint
+ ___80-[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:isReverse:]_block_invoke
+ ___80-[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:isReverse:]_block_invoke_2
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_AccessibilitySettings
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftMapKit_$_AccessibilitySettings
+ _objc_msgSend$_axTransitionToPasscodeInput:isReverse:
+ _objc_msgSend$_constraintsForPasscodeInputView:position:bottomConstraint:horizontalConstraint:
+ _objc_msgSend$_horizontalConstraintForPasscodeInputView:position:
+ _objc_msgSend$passcodeHorizontalConstraint
+ _objc_msgSend$refreshAssistantSpecifiers
+ _objc_msgSend$setPasscodeHorizontalConstraint:
+ _objc_msgSend$setVisualAlertsType:
+ _objc_msgSend$setVoiceOverQuickNavEnabled:
+ _objc_msgSend$setVoiceOverTouchSingleLetterQuickNavEnabled:
+ _objc_msgSend$visualAlertsType
+ _objc_msgSend$voiceOverQuickNavEnabled
+ _objc_msgSend$voiceOverTouchSingleLetterQuickNavEnabled
+ get_witness_table 7SwiftUI7ForEachVySay21AccessibilitySettings13SCSwitchGroupVGSSAA7SectionVyAA4TextVAA15ModifiedContentVyACySaySo8AXSwitchCG10Foundation4UUIDVAD9SwitchRowVGAA21_TraitWritingModifierVyAA08OnDeleteR3KeyVGGAA9EmptyViewVGGAA0Y0HPA3_AAA5_HPAkAA5_HPyHC_A0_AAA5_HPAvAA5_HPAuAA5_HPyHC_HC_A_AA0yT0HPyHCHCA2_AAA5_HPyHCHC_HC.115
+ get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAHyAcAE9listStyleyQrqd__AA04ListK0Rd__lFQOyAcAE7toolbar7contentQrqd__yXE_tAA07ToolbarI0Rd__lFQOy021AccessibilitySettingsB0017AXSUIPlatformFormlC0VyAA05TupleC0VyARyAA7SectionVyAA05EmptyC0VAcNE11axSpecifieryQrSSFQOyAcAE5sheet11isPresented0D7DismissALQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAA6ButtonVyAA4TextVG_AA15NavigationStackVyAA14NavigationPathVAHyAcAEAkLQrqd__yXE_tAaMRd__lFQOyAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0pQ022SwitchSourceControllerV_SSQo__Qo__AA0oI7BuilderV10buildBlockyQrxAaMRzlFZQOy_AA0O4ItemVyytAHyA4_yAA5ImageVGAA0P18AttachmentModifierVGGQo_Qo_AA30_SafeAreaRegionsIgnoringLayoutVGGQo__Qo_AA012_ConditionalI0VyA44_yA6_A6_GA44_yA6_AVGGG_ATyAvN18AXSUISpecifierLinkVyA6_AHyAcAEA17_yQrqd__SyRd__lFQOyA18_26BluetoothDevicesControllerV_SSQo_A38_GGAVGSgtG_A18_06SwitchL0VtGG_A24_A25_yQrxAaMRzlFZQOy_AA0O9ItemGroupVyAHyAHyAHyAHyAHyAHyAcAE04menuK0yQrqd__AA04MenuK0Rd__lFQOyAA4MenuVyA29_ATyAvcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA6PickerVyA6_A18_17SCSwitchGroupTypeOAA7ForEachVySayA72_GA72_A6_GG_A72_Qo_AVGG_AA010ButtonMenuK0VQo_AA14_PaddingLayoutVGAA01_I17ShapeKindModifierVyAA6CircleVGGAA011_ForegroundK8ModifierVyAA5ColorVGGAA19_BackgroundModifierVyAA06_ShapeC0VyA90_A96_GSgGGA32_GA32_GGQo_Qo__AA07SidebarlK0VQo_AA30_EnvironmentKeyWritingModifierVyA18_10SCSettingsCGGAA25_AppearanceActionModifierVG_SbQo_HO.81
+ get_witness_table qd__7SwiftUI4ViewHD2_AaBP021AccessibilitySettingsB0E11axSpecifieryQrSSFQOyAD18AXSUISpecifierLinkVyAA09_VariadicC0O4TreeVy_AA11_LayoutRootVyAA03AnyL0VGAA05TupleC0VyAA5LabelVyAA6VStackVyARyAA4TextV_A2XSgtGGAA15ModifiedContentVyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGG_ARyAA6SpacerVSg_AXtGSgtGGA1_yA1_yAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0dE0013SwitchDetailsC10ControllerV_SSQo__Qo_AA024_SafeAreaRegionsIgnoringL0VGAA017_AppearanceActionX0VGG_Qo_HO.126
+ objectdestroy.117Tm
- -[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:withAnimation:]
- ___84-[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:withAnimation:]_block_invoke
- ___84-[ClarityUIAdminPasscodeSetupController _axTransitionToPasscodeInput:withAnimation:]_block_invoke_2
- ___block_descriptor_100_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_msgSend$_axTransitionToPasscodeInput:withAnimation:
- _objc_msgSend$center
- _objc_msgSend$setCenter:
- get_witness_table 7SwiftUI7ForEachVySay21AccessibilitySettings13SCSwitchGroupVGSSAA7SectionVyAA4TextVAA15ModifiedContentVyACySaySo8AXSwitchCG10Foundation4UUIDVAD9SwitchRowVGAA21_TraitWritingModifierVyAA08OnDeleteR3KeyVGGAA9EmptyViewVGGAA0Y0HPA3_AAA5_HPAkAA5_HPyHC_A0_AAA5_HPAvAA5_HPAuAA5_HPyHC_HC_A_AA0yT0HPyHCHCA2_AAA5_HPyHCHC_HC.112
- get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA15ModifiedContentVyAHyAcAE9listStyleyQrqd__AA04ListK0Rd__lFQOyAcAE7toolbar7contentQrqd__yXE_tAA07ToolbarI0Rd__lFQOy021AccessibilitySettingsB0017AXSUIPlatformFormlC0VyAA05TupleC0VyARyAA7SectionVyAA05EmptyC0VAcNE11axSpecifieryQrSSFQOyAcAE5sheet11isPresented0D7DismissALQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQOyAA6ButtonVyAA4TextVG_AA15NavigationStackVyAA14NavigationPathVAHyAcAEAkLQrqd__yXE_tAaMRd__lFQOyAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0pQ022SwitchSourceControllerV_SSQo__Qo__AA0oI7BuilderV10buildBlockyQrxAaMRzlFZQOy_AA0O4ItemVyytAHyA4_yAA5ImageVGAA0P18AttachmentModifierVGGQo_Qo_AA30_SafeAreaRegionsIgnoringLayoutVGGQo__Qo_AA012_ConditionalI0VyA44_yA6_A6_GA44_yA6_AVGGG_ATyAvN18AXSUISpecifierLinkVyA6_AHyAcAEA17_yQrqd__SyRd__lFQOyA18_26BluetoothDevicesControllerV_SSQo_A38_GGAVGSgtG_A18_06SwitchL0VtGG_A24_A25_yQrxAaMRzlFZQOy_AA0O9ItemGroupVyAHyAHyAHyAHyAHyAHyAcAE04menuK0yQrqd__AA04MenuK0Rd__lFQOyAA4MenuVyA29_ATyAvcAEAdeF_Qrqd___Sbyqd___qd__tctSQRd__lFQOyAA6PickerVyA6_A18_17SCSwitchGroupTypeOAA7ForEachVySayA72_GA72_A6_GG_A72_Qo_AVGG_AA010ButtonMenuK0VQo_AA14_PaddingLayoutVGAA01_I17ShapeKindModifierVyAA6CircleVGGAA011_ForegroundK8ModifierVyAA5ColorVGGAA19_BackgroundModifierVyAA06_ShapeC0VyA90_A96_GSgGGA32_GA32_GGQo_Qo__AA07SidebarlK0VQo_AA30_EnvironmentKeyWritingModifierVyA18_10SCSettingsCGGAA25_AppearanceActionModifierVG_SbQo_HO.78
- get_witness_table qd__7SwiftUI4ViewHD2_AaBP021AccessibilitySettingsB0E11axSpecifieryQrSSFQOyAD18AXSUISpecifierLinkVyAA09_VariadicC0O4TreeVy_AA11_LayoutRootVyAA03AnyL0VGAA05TupleC0VyAA5LabelVyAA6VStackVyARyAA4TextV_A2XSgtGGAA15ModifiedContentVyAA5ImageVAA24_ForegroundStyleModifierVyAA5ColorVGGG_ARyAA6SpacerVSg_AXtGSgtGGA1_yA1_yAcAE29navigationBarTitleDisplayModeyQrAA17NavigationBarItemV16TitleDisplayModeOFQOyAcAE15navigationTitleyQrqd__SyRd__lFQOy0dE0013SwitchDetailsC10ControllerV_SSQo__Qo_AA024_SafeAreaRegionsIgnoringL0VGAA017_AppearanceActionX0VGG_Qo_HO.123
- objectdestroy.114Tm
CStrings:
+ "%@\n"
+ "@48@0:8@16q24^@32^@40"
+ "FLASH_FOR_ALERTS"
+ "HomeButtonAssistantNotAvailableFooter"
+ "QUICK_NAV_TITLE"
+ "SINGLE_LETTER_QUICK_NAV_TITLE"
+ "T@\"NSLayoutConstraint\",&,N,V_passcodeHorizontalConstraint"
+ "VISUAL_ALERT_TYPE_BOTH"
+ "VISUAL_ALERT_TYPE_GROUP"
+ "VISUAL_ALERT_TYPE_LED"
+ "VISUAL_ALERT_TYPE_SCREEN"
+ "VISUAL_ALERT_TYPE_VALUE"
+ "_axTransitionToPasscodeInput:isReverse:"
+ "_constraintsForPasscodeInputView:position:bottomConstraint:horizontalConstraint:"
+ "_horizontalConstraintForPasscodeInputView:position:"
+ "_passcodeHorizontalConstraint"
+ "_shouldRestrictAssistantSpecifiers"
+ "eligibilityDidChange"
+ "isQuickNavEnabled"
+ "isSingleLetterQuickNavEnabled"
+ "passcodeHorizontalConstraint"
+ "refreshAssistantSpecifiers"
+ "setPasscodeHorizontalConstraint:"
+ "setQuickNavEnabled:"
+ "setSingleLetterQuickNavEnabled:"
+ "setVisualAlertsType:"
+ "setVoiceOverQuickNavEnabled:"
+ "setVoiceOverTouchSingleLetterQuickNavEnabled:"
+ "visualAlertsType"
+ "voiceOverQuickNavEnabled"
+ "voiceOverTouchSingleLetterQuickNavEnabled"
- "%@\n\n%@"
- "FLASH_LED"
- "_axTransitionToPasscodeInput:withAnimation:"
- "center"
- "setCenter:"
- "v28@0:8@16i24"

```
