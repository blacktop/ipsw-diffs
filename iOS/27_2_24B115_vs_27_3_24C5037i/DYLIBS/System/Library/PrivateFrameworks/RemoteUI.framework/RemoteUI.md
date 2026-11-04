## RemoteUI

> `/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI`

```diff

-640.125.6.1.0
-  __TEXT.__text: 0x1495cc
-  __TEXT.__objc_methlist: 0x9094
-  __TEXT.__const: 0xfd94
-  __TEXT.__cstring: 0x570d
-  __TEXT.__oslogstring: 0x2c8e
-  __TEXT.__gcc_except_tab: 0x7f8
-  __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__swift5_typeref: 0xa5ba
-  __TEXT.__swift5_reflstr: 0x2d0a
+640.250.4.0.0
+  __TEXT.__text: 0x14ffe8
+  __TEXT.__objc_methlist: 0x952c
+  __TEXT.__const: 0xff34
+  __TEXT.__cstring: 0x58fd
+  __TEXT.__oslogstring: 0x2d6e
+  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__dlopen_cstrs: 0x369
+  __TEXT.__swift5_typeref: 0xa904
+  __TEXT.__swift5_reflstr: 0x2dca
   __TEXT.__swift5_assocty: 0x14d8
-  __TEXT.__constg_swiftt: 0x5744
-  __TEXT.__swift5_fieldmd: 0x3b04
+  __TEXT.__constg_swiftt: 0x5850
+  __TEXT.__swift5_fieldmd: 0x3bd4
   __TEXT.__swift5_proto: 0x978
-  __TEXT.__swift5_types: 0x4bc
-  __TEXT.__swift5_capture: 0xd94
+  __TEXT.__swift5_types: 0x4cc
+  __TEXT.__swift5_capture: 0xdb4
   __TEXT.__swift_as_entry: 0x128
   __TEXT.__swift_as_ret: 0x12c
   __TEXT.__swift_as_cont: 0x1c0
   __TEXT.__swift5_protos: 0x7c
-  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x72c8
-  __TEXT.__eh_frame: 0x506c
+  __TEXT.__unwind_info: 0x74c8
+  __TEXT.__eh_frame: 0x5114
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16a0
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x17b0
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x57c0
+  __DATA_CONST.__objc_selrefs: 0x59e8
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x12e8
-  __AUTH_CONST.__const: 0x8af0
-  __AUTH_CONST.__cfstring: 0x44a0
-  __AUTH_CONST.__objc_const: 0xf270
+  __DATA_CONST.__got: 0x1310
+  __AUTH_CONST.__const: 0x8ce0
+  __AUTH_CONST.__cfstring: 0x4540
+  __AUTH_CONST.__objc_const: 0xf9e8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2220
-  __AUTH.__objc_data: 0x4030
-  __AUTH.__data: 0x3300
-  __DATA.__objc_ivar: 0x848
-  __DATA.__data: 0x4bc0
+  __AUTH_CONST.__auth_got: 0x2270
+  __AUTH.__objc_data: 0x4348
+  __AUTH.__data: 0x3358
+  __DATA.__objc_ivar: 0x89c
+  __DATA.__data: 0x4cd8
   __DATA.__objc_stublist: 0x8
-  __DATA.__common: 0xa8
+  __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0x208
   __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8263
-  Symbols:   6722
-  CStrings:  1149
+  Functions: 8417
+  Symbols:   6906
+  CStrings:  1170
 
Symbols:
+ +[RUIDefaultAppearanceStyle styleName]
+ +[RUIDefaultStyle styleName]
+ +[RUIFrontRow2Style styleName]
+ +[RUIFrontRowStyle styleName]
+ +[RUIOsloStyle styleName]
+ +[RUIProxCardStyle styleName]
+ +[RUISetupAssistantModalStyle styleName]
+ +[RUISetupAssistantStyle styleName]
+ +[RUIStyle proxCardStyle]
+ +[RUIStyle styleName]
+ +[RemoteUIController _setAllowsPresentationWhileLockedForTesting:]
+ +[RemoteUIController allowsPresentationWhileLocked]
+ -[OBButtonTray(RemoteUI) rui_headerView]
+ -[RUIAlertView _addAction:toController:]
+ -[RUIAlertView _alertControllerWasDismissedByAction]
+ -[RUIAlertView _keepsAlertPresentedForButtonAttributes:]
+ -[RUIElementViewController _canShowWhileLocked]
+ -[RUIEmbeddedPickerCell layoutSubviews]
+ -[RUIEmbeddedPickerCell prepareForReuse]
+ -[RUILocalPasscodeValidator init]
+ -[RUILocalPasscodeValidator setUnlockDeviceHandler:]
+ -[RUILocalPasscodeValidator setVerifyPasscodeHandler:]
+ -[RUILocalPasscodeValidator unlockDeviceHandler]
+ -[RUILocalPasscodeValidator verifyPasscodeHandler]
+ -[RUILockScreenAwareBaseWelcomeController _canShowWhileLocked]
+ -[RUIModalPresentationController _fittedDetent]
+ -[RUIModalPresentationController _scheduleFittedHeightUpdate]
+ -[RUIModalPresentationController _sheetWidth]
+ -[RUIModalPresentationController _topPage]
+ -[RUIModalPresentationController _updateFittedHeight]
+ -[RUINavigationController _canShowWhileLocked]
+ -[RUINavigationController dismissFlowAnimated:completion:]
+ -[RUINavigationController dismissesFromPresenter]
+ -[RUIPage _canShowWhileLocked]
+ -[RUIPage _updateToolbarInsets]
+ -[RUIPage fittedAdaptiveSheetHeightForWidth:]
+ -[RUIPage fittedContentDidChange]
+ -[RUIPage usesFittedAdaptiveSheetLayout]
+ -[RUIProxCardStyle applyToObjectModel:]
+ -[RUIProxCardStyle backgroundColorForCellInTableView:]
+ -[RUIProxCardStyle hidesNavigationTitle]
+ -[RUIProxCardStyle init]
+ -[RUIScrollableWelcomeController _canShowWhileLocked]
+ -[RUISetupAssistantStyle backgroundColorForCellInTableView:]
+ -[RUIStyle backgroundColorForCellInTableView:]
+ -[RUIStyle hidesNavigationTitle]
+ -[RUITableView _fittingHeightOfSectionView:inTableView:fallback:]
+ -[RUITableView omitsTrailingFooterSpacing]
+ -[RUITableView requiresExactContentSize]
+ -[RUITableView setOmitsTrailingFooterSpacing:]
+ -[RUITableView setRequiresExactContentSize:]
+ -[RUITableView tableView:estimatedHeightForFooterInSection:]
+ -[RUITableView tableView:estimatedHeightForHeaderInSection:]
+ -[RUITableWelcomeController _applyManualContentInsets]
+ -[RUITableWelcomeController _canShowWhileLocked]
+ -[RUITableWelcomeController _updateButtonTrayTableFooterContainerSizeIfNeeded]
+ -[RUITableWelcomeController _updateScrollViewInsets]
+ -[RUITableWelcomeController setUsesManualContentInsets:]
+ -[RUITableWelcomeController usesManualContentInsets]
+ -[RemoteUIWebViewController _canShowWhileLocked]
+ -[UIViewController(RUISheetSizing) rui_sheetPresentationStyle]
+ -[UIViewController(RUISheetSizing) rui_sheetSizesToPreferredContentSize]
+ -[UIViewController(RemoteUI) firstDescendantOfClass:]
+ -[_RUIAlertActionDescriptor .cxx_destruct]
+ -[_RUIAlertActionDescriptor handler]
+ -[_RUIAlertActionDescriptor preferred]
+ -[_RUIAlertActionDescriptor setHandler:]
+ -[_RUIAlertActionDescriptor setPreferred:]
+ -[_RUIAlertActionDescriptor setShouldDismiss:]
+ -[_RUIAlertActionDescriptor setStyle:]
+ -[_RUIAlertActionDescriptor setTitle:]
+ -[_RUIAlertActionDescriptor shouldDismiss]
+ -[_RUIAlertActionDescriptor style]
+ -[_RUIAlertActionDescriptor title]
+ GCC_except_table10
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table144
+ GCC_except_table18
+ GCC_except_table28
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table6
+ GCC_except_table79
+ GCC_except_table8
+ _CGRectNull
+ _MobileKeyBagLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_RUIEmbeddedPickerCell
+ _OBJC_CLASS_$_RUILockScreenAwareBaseWelcomeController
+ _OBJC_CLASS_$_RUIProxCardStyle
+ _OBJC_CLASS_$__RUIAlertActionDescriptor
+ _OBJC_CLASS_$__TtC8RemoteUI21DualHeroContainerView
+ _OBJC_CLASS_$__TtC8RemoteUI37RUILockScreenAwareOBWelcomeController
+ _OBJC_IVAR_$_RUIAlertView._actionDescriptors
+ _OBJC_IVAR_$_RUIAlertView._alertControllerStyle
+ _OBJC_IVAR_$_RUIAlertView._hasAlertControllerStyle
+ _OBJC_IVAR_$_RUIEmbeddedPickerCell._lastContentWidth
+ _OBJC_IVAR_$_RUILocalPasscodeValidator._unlockDeviceHandler
+ _OBJC_IVAR_$_RUILocalPasscodeValidator._verifyPasscodeHandler
+ _OBJC_IVAR_$_RUIModalPresentationController._fittedHeight
+ _OBJC_IVAR_$_RUIModalPresentationController._fittedHeightUpdateDeferred
+ _OBJC_IVAR_$_RUIModalPresentationController._fittedHeightUpdateScheduled
+ _OBJC_IVAR_$_RUIModalPresentationController._measuringFittedHeight
+ _OBJC_IVAR_$_RUIModalPresentationController._usesFittedDetent
+ _OBJC_IVAR_$_RUIPage._leadingToolbarInsetItem
+ _OBJC_IVAR_$_RUIPage._trailingToolbarInsetItem
+ _OBJC_IVAR_$_RUITableView._omitsTrailingFooterSpacing
+ _OBJC_IVAR_$_RUITableView._requiresExactContentSize
+ _OBJC_IVAR_$_RUITableWelcomeController._buttonTrayBottomInset
+ _OBJC_IVAR_$_RUITableWelcomeController._usesManualContentInsets
+ _OBJC_IVAR_$__RUIAlertActionDescriptor._handler
+ _OBJC_IVAR_$__RUIAlertActionDescriptor._preferred
+ _OBJC_IVAR_$__RUIAlertActionDescriptor._shouldDismiss
+ _OBJC_IVAR_$__RUIAlertActionDescriptor._style
+ _OBJC_IVAR_$__RUIAlertActionDescriptor._title
+ _OBJC_METACLASS_$_RUIEmbeddedPickerCell
+ _OBJC_METACLASS_$_RUILockScreenAwareBaseWelcomeController
+ _OBJC_METACLASS_$_RUIProxCardStyle
+ _OBJC_METACLASS_$__RUIAlertActionDescriptor
+ _OBJC_METACLASS_$__TtC8RemoteUI21DualHeroContainerView
+ _OBJC_METACLASS_$__TtC8RemoteUI37RUILockScreenAwareOBWelcomeController
+ _RUILocalPasscodeValidatorErrorDomain
+ _UIEdgeInsetsInsetRect
+ __DATA__TtC8RemoteUI21DualHeroContainerView
+ __DATA__TtC8RemoteUI37RUILockScreenAwareOBWelcomeController
+ __INSTANCE_METHODS__TtC8RemoteUI21DualHeroContainerView
+ __INSTANCE_METHODS__TtC8RemoteUI35RUILockScreenAwareHostingController
+ __INSTANCE_METHODS__TtC8RemoteUI37RUILockScreenAwareOBWelcomeController
+ __IVARS__TtC8RemoteUI21DualHeroContainerView
+ __METACLASS_DATA__TtC8RemoteUI21DualHeroContainerView
+ __METACLASS_DATA__TtC8RemoteUI37RUILockScreenAwareOBWelcomeController
+ __OBJC_$_CLASS_METHODS_RUIDefaultStyle
+ __OBJC_$_CLASS_METHODS_RUIFrontRow2Style
+ __OBJC_$_CLASS_METHODS_RUIFrontRowStyle
+ __OBJC_$_CLASS_METHODS_RUIOsloStyle
+ __OBJC_$_CLASS_METHODS_RUIProxCardStyle
+ __OBJC_$_CLASS_METHODS_RUISetupAssistantModalStyle
+ __OBJC_$_CLASS_METHODS_RUISetupAssistantStyle
+ __OBJC_$_CLASS_METHODS_RemoteUIController
+ __OBJC_$_CLASS_PROP_LIST_RUIStyle
+ __OBJC_$_INSTANCE_METHODS_RUIEmbeddedPickerCell
+ __OBJC_$_INSTANCE_METHODS_RUILockScreenAwareBaseWelcomeController
+ __OBJC_$_INSTANCE_METHODS_RUIProxCardStyle
+ __OBJC_$_INSTANCE_METHODS_RUITableViewRow(Scripting|RemoteUI|RemoteUI1)
+ __OBJC_$_INSTANCE_METHODS_UIViewController(RemoteUI|RUISheetSizing|RUISettingsNavigation)
+ __OBJC_$_INSTANCE_METHODS__RUIAlertActionDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_RUIEmbeddedPickerCell
+ __OBJC_$_INSTANCE_VARIABLES__RUIAlertActionDescriptor
+ __OBJC_$_PROP_LIST__RUIAlertActionDescriptor
+ __OBJC_CLASS_RO_$_RUIEmbeddedPickerCell
+ __OBJC_CLASS_RO_$_RUILockScreenAwareBaseWelcomeController
+ __OBJC_CLASS_RO_$_RUIProxCardStyle
+ __OBJC_CLASS_RO_$__RUIAlertActionDescriptor
+ __OBJC_METACLASS_RO_$_RUIEmbeddedPickerCell
+ __OBJC_METACLASS_RO_$_RUILockScreenAwareBaseWelcomeController
+ __OBJC_METACLASS_RO_$_RUIProxCardStyle
+ __OBJC_METACLASS_RO_$__RUIAlertActionDescriptor
+ __PROPERTIES_RUIXMLSanitizer
+ __UIEnhancedLandscapeBarEnabled
+ ___33-[RUILocalPasscodeValidator init]_block_invoke
+ ___33-[RUILocalPasscodeValidator init]_block_invoke_2
+ ___47-[RUIModalPresentationController _fittedDetent]_block_invoke
+ ___50-[RUITableWelcomeController viewDidLayoutSubviews]_block_invoke
+ ___51+[RemoteUIController allowsPresentationWhileLocked]_block_invoke
+ ___53-[RUIModalPresentationController _updateFittedHeight]_block_invoke
+ ___53-[RUIModalPresentationController _updateFittedHeight]_block_invoke_2
+ ___61-[RUIModalPresentationController _scheduleFittedHeightUpdate]_block_invoke
+ ___67-[RUIAlertView addButtonWithTitle:URL:style:attributes:xmlElement:]_block_invoke_2
+ ___67-[RUIAlertView addButtonWithTitle:URL:style:attributes:xmlElement:]_block_invoke_3
+ ___MobileKeyBagLibraryCore_block_invoke
+ ___RUIInsetGroupedCellBackgroundColor_block_invoke
+ ___block_descriptor_32_e18_i16?0"NSString"8l
+ ___block_descriptor_32_e22_B24?0"NSString"8^16l
+ ___block_descriptor_40_e8_32w_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8lw32l8
+ ___block_descriptor_40_e8_32w_e64_d16?0"<UISheetPresentationControllerDetentResolutionContext>"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___getMKBUnlockDeviceSymbolLoc_block_invoke
+ _allowsPresentationWhileLocked.onceToken
+ _audit_stringMobileKeyBag
+ _gAllowsPresentationWhileLocked
+ _getMKBUnlockDeviceSymbolLoc.ptr
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQOyAE06RemoteB0E06appendE7ContextyQrAI0eM0OFQOyAA03AnyE0V_Qo__Qo_AA25_AppearanceActionModifierVGAaDHPqd__AaDHD2_APHO_ArA0eQ0HPyHCHC
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA5GroupVyAA012_ConditionalD0VyAA7AnyViewVAGyAA6ButtonVyAA6HStackVyAA05TupleD0VyAA5ImageVSg_AA4TextVQPGGGACyACyACy06RemoteB08MarkdownVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGA0_yAA5ColorVSgGGAX011OpenURLViewS0VGGGGAA01_pq9TransformS0VySayAX0H7ContextOGGGAA0H0HPA16_AAA24_HPA15_AAA24_HPAiAA24_HPyHC_A14_AAA24_HPAwAA24_HPyHC_A13_AAA24_HPA10_AAA24_HPA5_AAA24_HPAzAA24_HPyHC_A4_AA0hS0HPyHCHC_A9_AAA25_HPyHCHC_A12_AAA25_HPyHCHCHCHC_HC_A22_AAA25_HPyHCHC
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6VStackVyAA05TupleD0VyAA6SpacerV_AA7AnyViewVACyAiA16_FlexFrameLayoutVGAkGyAN_ACy06RemoteB0018CenteringContainerI0VAA01_kL0VGQPGSgAKSgAnwIQPGGAA024_SafeAreaRegionsIgnoringL0VGAA0I0HPAyAA1_HPyHC_A_AA0I8ModifierHPyHCHC
+ _get_witness_table 7SwiftUI6VStackVyAA12TupleContentVyAA08ModifiedE0VyAGyAA6HStackVyAEyAA6SpacerV_AGyAA7AnyViewVAA12_FrameLayoutVGAKQPGGAA08_PaddingL0VGAA30_EnvironmentKeyWritingModifierVyAA13TextAlignmentOGGSg_AGyAGyAGyAGyAA0R0VAZGAWyAA4FontVSgGGAWySiSgGGAA010_FixedSizeL0VGAGyAGyAGyAGyAGyAMA7_GAZGAWyy10Foundation16AttributedStringVzcGGA10_GA13_GSgQPGGAA0J0HPyHC
+ _keypath_get_selector_contentInset
+ _swift_task_getMainExecutor
+ _swift_task_isCurrentExecutor
+ _symbolic So12UIScrollViewC
+ _symbolic So12UIScrollViewCSgXw
+ _symbolic So18NSLayoutConstraintCSg
+ _symbolic So19OBWelcomeControllerC
+ _symbolic _____ 8RemoteUI21DualHeroContainerViewC
+ _symbolic _____ 8RemoteUI35RUILockScreenAwareHostingControllerC
+ _symbolic _____ 8RemoteUI37RUILockScreenAwareOBWelcomeControllerC
+ _symbolic _____ So12UIEdgeInsetsV
+ _symbolic _____Sg So6UIViewC5UIKitE12LayoutRegionV14AdaptivityAxisO
+ _symbolic _____SgXw 8RemoteUI21DualHeroContainerViewC
+ _symbolic _____yAAyAAyAAyAAy__________y_____SgGGACy_____GGACyy_____zcGGACySiSgGG_____GSg 7SwiftUI15ModifiedContentV AA7AnyViewV AA30_EnvironmentKeyWritingModifierV AA4FontV AA13TextAlignmentO 10Foundation16AttributedStringV AA16_FixedSizeLayoutV
+ _symbolic _____yAAyAAyAAy__________y_____GGACy_____SgGGACySiSgGG_____G 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO AA4FontV AA16_FixedSizeLayoutV
+ _symbolic _____yAAyAAyAAy__________y_____SgGGACy_____GGACyy_____zcGGACySiSgGG 7SwiftUI15ModifiedContentV AA7AnyViewV AA30_EnvironmentKeyWritingModifierV AA4FontV AA13TextAlignmentO 10Foundation16AttributedStringV
+ _symbolic _____yAAyAAy__________y_____GGACy_____SgGGACySiSgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA0E9AlignmentO AA4FontV
+ _symbolic _____yAAyAAy__________y_____SgGGACy_____GGACyy_____zcGG 7SwiftUI15ModifiedContentV AA7AnyViewV AA30_EnvironmentKeyWritingModifierV AA4FontV AA13TextAlignmentO 10Foundation16AttributedStringV
+ _symbolic _____yAAyAAy__________y_____SgGGACy_____SgGG_____G 7SwiftUI15ModifiedContentV 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AD011OpenURLViewJ0V
+ _symbolic _____yAAy_____y_____y______AAy__________GADQPGG_____G_____y_____GGSg 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA6SpacerV AA7AnyViewV AA12_FrameLayoutV AA08_PaddingK0V AA30_EnvironmentKeyWritingModifierV AA13TextAlignmentO
+ _symbolic _____y_____AAy_____y_____y_____y_____Sg______QPGGG_____yALyALy__________y_____SgGGANy_____SgGG_____GGG 7SwiftUI19_ConditionalContentV AA7AnyViewV AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA08ModifiedD0V 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AR011OpenURLViewR0V
+ _symbolic _____y_____G 8RemoteUI35RUILockScreenAwareHostingControllerC 05SwiftB07AnyViewV
+ _symbolic _____y_____G 8RemoteUI35RUILockScreenAwareHostingControllerC AA9WatermarkV
+ _symbolic _____y______Qo_ 7SwiftUI4ViewP06RemoteB0E06appendC7ContextyQrAD0cF0OFQO AA03AnyC0V
+ _symbolic _____y__________y_____y_____y_____y_____Sg______QPGGG_____yAMyAMy__________y_____SgGGAOy_____SgGG_____GG_G 7SwiftUI19_ConditionalContentV7StorageO AA7AnyViewV AC AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA08ModifiedD0V 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AT011OpenURLViewS0V
+ _symbolic _____y_____y_____ABy_____y_____y_____y_____Sg______QPGGG_____yAMyAMy__________y_____SgGGAOy_____SgGG_____GGGG 7SwiftUI5GroupV AA19_ConditionalContentV AA7AnyViewV AA6ButtonV AA6HStackV AA05TupleE0V AA5ImageV AA4TextV AA08ModifiedE0V 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AT011OpenURLViewS0V
+ _symbolic _____y_____y______Qo__Qo_ 7SwiftUI4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AC06RemoteB0E06appendC7ContextyQrAG0cK0OFQO AA03AnyC0V
+ _symbolic _____y_____y__________G_ABy__________GQPGSg 7SwiftUI12TupleContentV AA08ModifiedD0V AA6SpacerV AA16_FlexFrameLayoutV 06RemoteB022CenteringContainerViewV AA01_hI0V
+ _symbolic _____y_____y________________yAC_____GAdByAG_AEy__________GQPGSgADSgAgmCQPGG 7SwiftUI6VStackV AA12TupleContentV AA6SpacerV AA7AnyViewV AA08ModifiedE0V AA16_FlexFrameLayoutV 06RemoteB0018CenteringContainerH0V AA01_kL0V
+ _symbolic _____y_____y_____yACy_____yABy______ACy__________GAEQPGG_____G_____y_____GGSg_ACyACyACyACy_____AOGAMy_____SgGGAMySiSgGG_____GACyACyACyACyACyAfVGAOGAMyy_____zcGGAYGA_GSgQPGG 7SwiftUI6VStackV AA12TupleContentV AA08ModifiedE0V AA6HStackV AA6SpacerV AA7AnyViewV AA12_FrameLayoutV AA08_PaddingL0V AA30_EnvironmentKeyWritingModifierV AA13TextAlignmentO AA0R0V AA4FontV AA010_FixedSizeL0V 10Foundation16AttributedStringV
+ _symbolic _____y_____y_____y_____ACy_____y_____y_____y_____Sg______QPGGGAAyAAyAAy__________y_____SgGGAOy_____SgGG_____GGGG_____ySay_____GGG 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V AA7AnyViewV AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AT011OpenURLViewS0V AA01_pq9TransformS0V AT0H7ContextO
+ _symbolic _____y_____y_____y______Qo__Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AE06RemoteB0E06appendE7ContextyQrAI0eM0OFQO AA03AnyE0V AA25_AppearanceActionModifierV
+ _symbolic _____y_____y_____y___________AAyAD_____GAeCyAG_AAy__________GQPGSgAESgAgmDQPGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA6SpacerV AA7AnyViewV AA16_FlexFrameLayoutV 06RemoteB0018CenteringContainerI0V AA01_kL0V AA024_SafeAreaRegionsIgnoringL0V
+ _symbolic _____y_____y_____y_____y_____Sg______QPGGG_____yAKyAKy__________y_____SgGGAMy_____SgGG_____GG 7SwiftUI19_ConditionalContentV AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA08ModifiedD0V 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AP011OpenURLViewP0V
+ _symbolic _____y_____y_____y_____y_____Sg______QPGGG_____yAKyAKy__________y_____SgGGAMy_____SgGG_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA08ModifiedD0V 06RemoteB08MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV AR011OpenURLViewQ0V
+ _symbolic ytSg______pIgrzo_ s5ErrorP
+ _type_layout_string So12UIEdgeInsetsV
- -[RUIDefaultStyle styleName]
- -[RUIFrontRow2Style styleName]
- -[RUIFrontRowStyle styleName]
- -[RUISetupAssistantStyle .cxx_destruct]
- -[RUISetupAssistantStyle insetGroupedCellBackgroundColor]
- -[RUISetupAssistantStyle setSetupAssistantLayout:]
- -[RUISetupAssistantStyle setupAssistantLayout]
- -[RUISetupAssistantStyle styleName]
- GCC_except_table102
- GCC_except_table103
- GCC_except_table105
- GCC_except_table113
- GCC_except_table12
- GCC_except_table137
- GCC_except_table33
- GCC_except_table36
- GCC_except_table37
- GCC_except_table39
- GCC_except_table42
- GCC_except_table44
- GCC_except_table76
- _OBJC_IVAR_$_RUISetupAssistantStyle._setupAssistantLayout
- __OBJC_$_INSTANCE_METHODS_RUIDefaultStyle
- __OBJC_$_INSTANCE_METHODS_RUITableViewRow(Scripting|RemoteUI|RemoteUI)
- __OBJC_$_INSTANCE_METHODS_UIViewController(RemoteUI|RUISettingsNavigation)
- __OBJC_$_INSTANCE_VARIABLES_RUISetupAssistantStyle
- __OBJC_$_PROP_LIST_RUISetupAssistantStyle
- ___57-[RUISetupAssistantStyle insetGroupedCellBackgroundColor]_block_invoke
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQOyACyAA03AnyE0VAA012_EnvironmentJ17TransformModifierVySay06RemoteB00E7ContextOGGG_Qo_AA017_AppearanceActionN0VGAaDHPqd__AaDHD2_ASHO_AuA0eN0HPyHCHC
- _get_witness_table 7SwiftUI6VStackVyAA12TupleContentVyAA7AnyViewV_AA08ModifiedE0VyAA6SpacerVAA12_FrameLayoutVGAgEyAN_06RemoteB0018CenteringContainerG0VQPGSgAkGSgAkTQPGGAA0G0HPyHC
- _get_witness_table qd__7SwiftUI4ViewHD2_AaBP06RemoteB0E06appendC7ContextyQrAD0cF0OFQOyAA5GroupVyAA19_ConditionalContentVyAA03AnyC0VAKyAA6ButtonVyAA6HStackVyAA05TupleI0VyAA5ImageVSg_AA4TextVQPGGGAcDE11openURLView4withQrAD9URLLoaderV_tFQOyAA08ModifiedI0VyA5_yAD8MarkdownVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGA9_yAA5ColorVSgGG_Qo_GGG_Qo_HO
- _symbolic _____y_____AAy_____y_____y_____y_____Sg______QPGGG_____y_____yALy__________y_____SgGGANy_____SgGG_Qo_GG 7SwiftUI19_ConditionalContentV AA7AnyViewV AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA0F0P06RemoteB0E11openURLView4withQrAR9URLLoaderV_tFQO AA08ModifiedD0V AR8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 06RemoteB09WatermarkV
- _symbolic _____y__________ySay_____GGG 7SwiftUI15ModifiedContentV AA7AnyViewV AA32_EnvironmentKeyTransformModifierV 06RemoteB00F7ContextO
- _symbolic _____y__________y_____y_____y_____y_____Sg______QPGGG_____y_____yAMy__________y_____SgGGAOy_____SgGG_Qo_G_G 7SwiftUI19_ConditionalContentV7StorageO AA7AnyViewV AC AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA0G0P06RemoteB0E11openURLView4withQrAT9URLLoaderV_tFQO AA08ModifiedD0V AT8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____yAAy__________ySay_____GGG_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AA03AnyE0V AA012_EnvironmentJ17TransformModifierV 06RemoteB00E7ContextO AA017_AppearanceActionN0V
- _symbolic _____y_____y_____ABy_____y_____y_____y_____Sg______QPGGG_____y_____yAMy__________y_____SgGGAOy_____SgGG_Qo_GGG 7SwiftUI5GroupV AA19_ConditionalContentV AA7AnyViewV AA6ButtonV AA6HStackV AA05TupleE0V AA5ImageV AA4TextV AA0G0P06RemoteB0E11openURLView4withQrAT9URLLoaderV_tFQO AA08ModifiedE0V AT8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____y__________G______QPGSg 7SwiftUI12TupleContentV AA08ModifiedD0V AA6SpacerV AA12_FrameLayoutV 06RemoteB022CenteringContainerViewV
- _symbolic _____y_____y___________y__________GAcByAG______QPGSgAeCSgAeKQPGG 7SwiftUI6VStackV AA12TupleContentV AA7AnyViewV AA08ModifiedE0V AA6SpacerV AA12_FrameLayoutV 06RemoteB0018CenteringContainerG0V
- _symbolic _____y_____y__________ySay_____GGG_Qo_ 7SwiftUI4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AA15ModifiedContentV AA03AnyC0V AA012_EnvironmentH17TransformModifierV 06RemoteB00C7ContextO
- _symbolic _____y_____y_____y_____ABy_____y_____y_____y_____Sg______QPGGG_____y_____yAMy__________y_____SgGGAOy_____SgGG_Qo_GGG_Qo_ 7SwiftUI4ViewP06RemoteB0E06appendC7ContextyQrAD0cF0OFQO AA5GroupV AA19_ConditionalContentV AA03AnyC0V AA6ButtonV AA6HStackV AA05TupleI0V AA5ImageV AA4TextV AcDE11openURLView4withQrAD9URLLoaderV_tFQO AA08ModifiedI0V AD8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____y_____y_____y_____Sg______QPGGG_____y_____yAKy__________y_____SgGGAMy_____SgGG_Qo_G 7SwiftUI19_ConditionalContentV AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA4ViewP06RemoteB0E11openURLView4withQrAP9URLLoaderV_tFQO AA08ModifiedD0V AP8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
- _symbolic _____y_____y_____y_____y_____Sg______QPGGG_____y_____yAKy__________y_____SgGGAMy_____SgGG_Qo__G 7SwiftUI19_ConditionalContentV7StorageO AA6ButtonV AA6HStackV AA05TupleD0V AA5ImageV AA4TextV AA4ViewP06RemoteB0E11openURLView4withQrAR9URLLoaderV_tFQO AA08ModifiedD0V AR8MarkdownV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
CStrings:
+ "B"
+ "B24@?0@\"NSString\"8^@16"
+ "B8@?0"
+ "Cannot verify passcode without unlocking (%d), falling back to unlocking the device"
+ "Dismissing RUI navigation controller."
+ "Error! Passcode did not validate on device unlock: %@"
+ "Error! Passcode did not validate: %d"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "MKBUnlockDevice"
+ "Passcode validated by unlocking the device"
+ "Passcode validated without unlocking the device"
+ "RUIAdaptiveSheetFittedDetent"
+ "RUIAllowsPresentationWhileLocked"
+ "RUILocalPasscodeValidatorErrorDomain"
+ "RemoteUI.DualHeroContainerView"
+ "RemoteUI/WelcomeController.swift"
+ "VerifyOnly"
+ "d16@?0@\"<UISheetPresentationControllerDetentResolutionContext>\"8"
+ "i16@?0@\"NSString\"8"
+ "int _MKBUnlockDevice(CFDataRef, CFDictionaryRef)"
+ "proxCard"
+ "scrollPocketInteraction"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "void *MobileKeyBagLibrary(void)"
+ "\xb1\xf0Q"
- "Error! Entered passcode does not validate: %@"
- "Validating local passcode"
- "frontRow"
- "\xb1\xf01"
```
