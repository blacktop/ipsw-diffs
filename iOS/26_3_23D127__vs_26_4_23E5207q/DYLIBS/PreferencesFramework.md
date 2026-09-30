## PreferencesFramework

> `/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x7b50
-  __TEXT.__auth_stubs: 0x3e0
+3005.16.0.0.0
+  __TEXT.__text: 0x8114
+  __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x1024
-  __TEXT.__cstring: 0x189d
+  __TEXT.__cstring: 0x191b
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0xd99
   __TEXT.__objc_methname: 0x15da
   __TEXT.__objc_methtype: 0x1c7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6d0
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x200
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x2020
   __AUTH_CONST.__objc_const: 0x2fd0

   - /usr/lib/libMobileCheckpoint.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08AB50D6-9D90-3399-85D3-3EBB46EE9909
+  UUID: 39D4B088-9CC5-35CA-AB2F-D502883687A0
   Functions: 298
-  Symbols:   1351
+  Symbols:   1346
   CStrings:  879
 
Symbols:
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ +[AXPreferencesFrameworkGlue accessibilityInitializeBundle] : 192 -> 200
~ ___59+[AXPreferencesFrameworkGlue accessibilityInitializeBundle]_block_invoke : 756 -> 760
~ ___59+[AXPreferencesFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___59+[AXPreferencesFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 812 -> 820
~ ___59+[AXPreferencesFrameworkGlue accessibilityInitializeBundle]_block_invoke_5 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[PSSpecifierSliderConfigurationCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityLabel] : 156 -> 172
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityHint] : 84 -> 92
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityTraits] : 136 -> 140
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityValue] : 144 -> 156
~ -[PSSpecifierSliderConfigurationCellAccessibility _accessibilityAbsoluteValue] : 84 -> 92
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityIncrement] : 172 -> 176
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityDecrement] : 172 -> 176
~ -[PSSpecifierSliderConfigurationCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[PSSpecifierSliderConfigurationCellAccessibility _axSpecifier] : 132 -> 140
~ -[PSSpecifierSliderConfigurationCellAccessibility _axBumpSliderValue:] : 244 -> 248
~ -[PSSpecifierSliderConfigurationCellAccessibility _axSliderIncreaseAmount:] : 276 -> 280
~ -[PSSpecifierSliderConfigurationCellAccessibility _axMinimumValue] : 92 -> 100
~ -[PSSpecifierSliderConfigurationCellAccessibility _axMaximumValue] : 108 -> 116
~ -[PSSpecifierSliderConfigurationCellAccessibility _axIsSegmented] : 92 -> 100
~ -[PSSpecifierSliderConfigurationCellAccessibility _axLocksToSegment] : 100 -> 108
~ -[PSSpecifierSliderConfigurationCellAccessibility _axSegmentCount] : 92 -> 100
~ +[PSSpecifierContentConfigurationCellAccessibility _accessibilityPerformValidations:] : 256 -> 264
~ -[PSSpecifierContentConfigurationCellAccessibility accessibilityTraits] : 336 -> 348
~ -[PSSpecifierContentConfigurationCellAccessibility accessibilityLabel] : 348 -> 376
~ ___70-[PSSpecifierContentConfigurationCellAccessibility accessibilityLabel]_block_invoke_2 : 116 -> 124
~ ___70-[PSSpecifierContentConfigurationCellAccessibility accessibilityLabel]_block_invoke_3 : 136 -> 140
~ -[PSSpecifierContentConfigurationCellAccessibility accessibilityUserInputLabels] : 212 -> 228
~ -[PSSpecifierContentConfigurationCellAccessibility _accessibilitySupplementaryFooterViews] : 200 -> 212
~ -[PSSpecifierContentConfigurationCellAccessibility _accessorySwitchView] : 116 -> 120
~ -[UISplitViewControllerPanelImplAccessibility__Preferences__UIKit _viewControllerChildViewControllersDidChange:] : 264 -> 280
~ -[PSReversedSubtitleDisclosureTableCellAccessibility _axCellSelf] : 108 -> 112
~ -[PSReversedSubtitleDisclosureTableCellAccessibility accessibilityLabel] : 176 -> 200
~ -[PSReversedSubtitleDisclosureTableCellAccessibility accessibilityValue] : 100 -> 112
~ -[PSViewControllerAccessibility _accessibilityHandleNavigationControllerDidEndTransition] : 772 -> 832
~ +[AlphanumericPINTextFieldAccessibility _accessibilityPerformValidations:] : 112 -> 120
~ ___66-[AlphanumericPINTextFieldAccessibility _accessibilityInsertText:]_block_invoke : 120 -> 128
~ ___92-[AlphanumericPINTextFieldAccessibility _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke : 120 -> 128
~ -[DevicePINKeypadAccessibility accessibilityFrame] : 176 -> 180
~ +[PSSpecifierToggleContentConfigurationCellAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ +[DevicePINPaneAccessibility _accessibilityPerformValidations:] : 388 -> 396
~ -[DevicePINPaneAccessibility slideToNewPasscodeField:requiresKeyboard:numericOnly:transition:showsOptionsButton:] : 168 -> 180
~ -[DevicePINPaneAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[DevicePINPaneAccessibility _accessibilityResponderElement] : 172 -> 184
~ -[DevicePINPaneAccessibility _accessibilityHandwritingAttributePreferredCharacterSet] : 72 -> 76
~ -[DevicePINPaneAccessibility _accessibilityHandwritingAttributeAllowedCharacterSets] : 76 -> 80
~ -[DevicePINPaneAccessibility _accessibilityReplaceCharactersAtCursor:withString:] : 152 -> 160
~ -[FailureBarViewAccessibility setFailureCount:] : 132 -> 140
~ -[FailureBarViewAccessibility accessibilityLabel] : 84 -> 92
~ -[PINKeypadAccessibility _accessibilityInternalChildren] : 1012 -> 996
~ ___56-[PINKeypadAccessibility _accessibilityInternalChildren]_block_invoke.338 : 80 -> 84
~ -[PSBadgedTableCellAccessibility badgeWithInteger:] : 120 -> 124
~ -[PSBadgedTableCellAccessibility accessibilityValue] : 204 -> 220
~ +[PSCapacityBarCellAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[PSCapacityBarCellAccessibility accessibilityValue] : 552 -> 580
~ -[PSControlTableCellAccessibility accessibilityLabel] : 212 -> 228
~ -[PSControlTableCellAccessibility accessibilityTraits] : 216 -> 224
~ -[PSControlTableCellAccessibility _accessibilityAbsoluteValue] : 84 -> 92
~ -[PSControlTableCellAccessibility accessibilityIncrement] : 152 -> 160
~ -[PSControlTableCellAccessibility accessibilityDecrement] : 152 -> 160
~ -[PSEditableTableCellAccessibility _accessibilityChildren] : 232 -> 248
~ -[PSEditableTableCellAccessibility _accessibilitySetSelectedTextRange:] : 88 -> 92
~ -[PSEditableTableCellAccessibility _accessibilitySelectedTextRange] : 72 -> 76
~ -[PSEditableTableCellAccessibility accessibilityLabel] : 228 -> 248
~ -[PSEditableTableCellAccessibility accessibilityValue] : 76 -> 84
~ -[PSEditableTableCellAccessibility accessibilityTraits] : 56 -> 60
~ +[PSFooterHyperlinkViewAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[PSFooterHyperlinkViewAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[PSKeyboardNavigationSearchBarAccessibility keyCommands] : 112 -> 120
~ +[PSKeychainSyncSecurityCodeControllerAccessibility _accessibilityPerformValidations:] : 160 -> 168
~ -[PSKeychainSyncSecurityCodeControllerAccessibility _accessibilityMarkupTable] : 176 -> 188
~ -[PSKeychainSyncSecurityCodeControllerAccessibility _configureTextEntryCell] : 104 -> 108
~ +[PSListControllerAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ ___68-[PSListControllerAccessibility loadSpecifiersFromPlistName:target:]_block_invoke : 144 -> 152
~ ___58-[PSListControllerAccessibility highlightSpecifierWithID:]_block_invoke : 80 -> 84
~ -[PSListControllerAccessibility _accessibilityHandleNavigationControllerDidEndTransition] : 984 -> 1056
~ -[PSListControllerAccessibility reloadSpecifierAtIndex:animated:] : 120 -> 124
~ +[PSPasscodeFieldAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PSPasscodeFieldAccessibility accessibilityValue] : 192 -> 208
~ +[PSSegmentableSliderAccessibility _accessibilityPerformValidations:] : 288 -> 296
~ -[PSSegmentableSliderAccessibility _accessibilityIncreaseAmount:] : 484 -> 500
~ +[PSSliderTableCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[PSSliderTableCellAccessibility accessibilityActivationPoint] : 80 -> 84
~ -[PSSpecifierAccessibility accessibilityIdentification] : 248 -> 268
~ -[PSSubtitleSwitchTableCellAccessibility accessibilityValue] : 172 -> 188
~ +[PSDateTimePickerCellAccessibility _accessibilityPerformValidations:] : 216 -> 228
~ -[PSDateTimePickerCellAccessibility isAccessibilityElement] : 64 -> 68
~ -[PSDateTimePickerCellAccessibility accessibilityLabel] : 172 -> 188
~ -[PSDateTimePickerCellAccessibility accessibilityValue] : 76 -> 84
~ -[PSDateTimePickerCellAccessibility accessibilityHint] : 76 -> 84
~ -[PSDateTimePickerCellAccessibility accessibilityActivationPoint] : 72 -> 76
~ -[PSDateTimePickerCellAccessibility accessibilityTraits] : 56 -> 60
~ -[PSDateTimePickerCellAccessibility accessibilityPickerTimeView] : 84 -> 92
~ +[PSTableCellAccessibility _accessibilityPerformValidations:] : 316 -> 324
~ +[PSTableCellAccessibility _setAccessibilityData:onCell:] : 672 -> 736
~ -[PSTableCellAccessibility _accessibilityLanguageOverriddesUser] : 120 -> 124
~ -[PSTableCellAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[PSTableCellAccessibility _accessibilityLoadAccessibilityInformationWithSpecifier:] : 88 -> 92
~ -[PSTableCellAccessibility _accessibilityHitTest:withEvent:] : 308 -> 324
~ -[PSTableCellAccessibility automationElements] : 276 -> 296
~ -[PSTableCellAccessibility isAccessibilityElement] : 124 -> 128
~ -[PSTableCellAccessibility accessibilityTraits] : 396 -> 408
~ -[PSTableCellAccessibility accessibilityLabel] : 1044 -> 1132
~ -[PSTableCellAccessibility accessibilityActivationPoint] : 144 -> 148
~ -[PSTableCellAccessibility accessibilityValue] : 504 -> 556
~ -[PSTableCellAccessibility accessibilityIncrement] : 144 -> 148
~ -[PSTableCellAccessibility accessibilityDecrement] : 144 -> 148
~ -[PSTableCellAccessibility accessibilityHint] : 164 -> 176
~ -[PSTableCellAccessibility _accessibilityMinScrubberPosition] : 140 -> 144
~ -[PSTableCellAccessibility _accessibilityMaxScrubberPosition] : 140 -> 144
~ -[PSTableCellAccessibility accessibilityRespondsToUserInteraction] : 116 -> 120
~ -[PSTableCellAccessibility canPerformAction:withSender:] : 180 -> 188
~ +[PSTimeRangeCellAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[PSTimeRangeCellAccessibility accessibilityLabel] : 296 -> 332
~ -[UITableViewCellAccessibility__Preferences__UIKit accessibilityLabel] : 280 -> 304
~ -[PSUsageBundleCellAccessibility accessibilityLabel] : 360 -> 388
~ +[PSUsageSizeHeaderAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[PSUsageSizeHeaderAccessibility accessibilityLabel] : 188 -> 208
~ -[PreferencesPSTableCellAccessibility accessibilityLabel] : 604 -> 660
~ +[DiagnosticDataControllerAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[DiagnosticDataControllerAccessibility viewDidLoad] : 148 -> 156
~ +[UITableViewAccessibility__Preferences__UIKit _accessibilityPerformValidations:] : 112 -> 120
~ -[UITableViewAccessibility__Preferences__UIKit _axIsDynamicTypeTable] : 64 -> 68
~ -[UITableViewAccessibility__Preferences__UIKit _accessibilityHitTest:withEvent:] : 168 -> 176
~ -[UITableViewAccessibility__Preferences__UIKit _accessibilityFooterElement] : 176 -> 188
CStrings:
+ "/Library/Caches/com.apple.xbs/FDBC4160-ED96-4D0B-B2D6-F3AE9446FEDF/TemporaryDirectory.FqHR68/Sources/AccessibilityBundles_Alias5/PreferencesAccessibility/Accessibility/FrameworkAccessibility/PSListControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/FDBC4160-ED96-4D0B-B2D6-F3AE9446FEDF/TemporaryDirectory.FqHR68/Sources/AccessibilityBundles_Alias5/PreferencesAccessibility/Accessibility/FrameworkAccessibility/PSSpecifierSliderConfigurationCellAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/PreferencesAccessibility/Accessibility/FrameworkAccessibility/PSListControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/PreferencesAccessibility/Accessibility/FrameworkAccessibility/PSSpecifierSliderConfigurationCellAccessibility.m"

```
