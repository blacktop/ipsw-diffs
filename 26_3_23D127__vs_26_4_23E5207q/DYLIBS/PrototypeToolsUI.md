## PrototypeToolsUI

> `/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI`

```diff

 160.0.0.0.0
-  __TEXT.__text: 0x8fd8
-  __TEXT.__auth_stubs: 0x370
+  __TEXT.__text: 0x961c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x1200
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__cstring: 0x31d
   __TEXT.__ustring: 0x28a
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_classname: 0x32e
   __TEXT.__objc_methname: 0x2f8e
   __TEXT.__objc_methtype: 0x102d

   __DATA_CONST.__objc_selrefs: 0xeb0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x2bb8

   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2150D61A-C336-3BC4-9212-6E98EC9B85B6
+  UUID: B269078F-11BF-3A46-8FD0-DA0C1039B53D
   Functions: 263
-  Symbols:   1303
+  Symbols:   1299
   CStrings:  776
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ _PTUINumericKeypadSetNeededWithWindow : 16 -> 64
~ -[_KeypadButton initWithKeyType:digit:target:] : 584 -> 620
~ __KeypadForegroundColor : 68 -> 84
~ __KeypadBackgroundColor : 68 -> 84
~ -[_KeypadButton _updateBackgroundColor] : 108 -> 116
~ -[_KeypadDismissButton initWithFrame:] : 340 -> 372
~ -[_KeypadDismissButton setHighlighted:] : 128 -> 136
~ +[PTUINumericKeypad sharedKeypad] : 160 -> 176
~ -[PTUINumericKeypad init] : 1016 -> 1072
~ -[PTUINumericKeypad showAnimated:forDelegate:] : 508 -> 512
~ -[PTUINumericKeypad doubleValue] : 356 -> 368
~ -[PTUINumericKeypad setDoubleValue:] : 768 -> 792
~ -[PTUINumericKeypad stringValue] : 452 -> 460
~ -[PTUINumericKeypad layoutSubviews] : 876 -> 940
~ -[PTUINumericKeypad _layoutButtonRow:atY:stretch:] : 472 -> 488
~ -[PTUINumericKeypad _updateDisplayedValue] : 156 -> 160
~ -[PTUINumericKeypad keyPress:] : 184 -> 192
~ -[PTUINumericKeypad _appendDigit:] : 252 -> 260
~ ___27-[PTUINumericKeypad _flash]_block_invoke_3 : 104 -> 108
~ ____KeypadForegroundColor_block_invoke : 72 -> 76
~ ____KeypadBackgroundColor_block_invoke : 76 -> 80
~ ____KeypadFlashColor_block_invoke : 72 -> 76
~ -[PTUIModifiedChangesViewController _populateTableDataAndChildren] : 556 -> 596
~ -[PTUIModifiedChangesViewController viewDidLoad] : 228 -> 236
~ -[PTUIModifiedChangesViewController initWithParameterRecords:withTitle:] : 160 -> 156
~ -[PTUIModifiedChangesViewController tableView:didSelectRowAtIndexPath:] : 324 -> 336
~ -[PTUIModifiedChangesViewController tableView:cellForRowAtIndexPath:] : 416 -> 440
~ -[PTUIEditingServer initWithDataSource:delegate:forRemoteEditing:] : 404 -> 408
~ -[PTUIEditingServer reloadDomains] : 152 -> 160
~ -[PTUIEditingServer reloadTestRecipes] : 140 -> 148
~ -[PTUIEditingServer proxyDefinitionChanged:] : 368 -> 408
~ -[PTUIEditingServer rootSettingsForDomainID:] : 132 -> 140
~ -[PTUIEditingServer domainIDForRootSettings:] : 336 -> 340
~ -[PTUIEditingServer domainGroupNames] : 248 -> 268
~ ___37-[PTUIEditingServer domainGroupNames]_block_invoke : 88 -> 92
~ -[PTUIEditingServer domainIDsInGroup:] : 364 -> 360
~ ___38-[PTUIEditingServer domainIDsInGroup:]_block_invoke : 128 -> 132
~ ___38-[PTUIEditingServer domainIDsInGroup:]_block_invoke_2 : 184 -> 200
~ -[PTUIEditingServer displayNameForDomainID:] : 80 -> 88
~ -[PTUIEditingServer groupNameForDomainID:] : 80 -> 88
~ -[PTUIEditingServer testRecipeIDsForDomainID:] : 364 -> 360
~ ___46-[PTUIEditingServer testRecipeIDsForDomainID:]_block_invoke : 128 -> 132
~ ___46-[PTUIEditingServer testRecipeIDsForDomainID:]_block_invoke_2 : 184 -> 200
~ -[PTUIEditingServer titleForTestRecipeID:] : 80 -> 88
~ -[PTUIEditingServer testRecipeSelectionModule] : 192 -> 204
~ -[PTUIEditingServer settingsEditingModule] : 192 -> 204
~ -[PTUIEditingServer settings:changedValueForKeyPath:] : 176 -> 184
~ -[PTUIEditingServer settingsDidRestoreDefaults:] : 100 -> 104
~ -[PTUIEditingServer _loadRootSettingsOrProxyForDomainID:] : 564 -> 592
~ __RecursivelyObserveOutletsForSettingsAtKeyPathWithBlock : 320 -> 300
~ -[PTUIEditingServer _testRecipeSection] : 656 -> 668
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke : 92 -> 108
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke_2 : 124 -> 132
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke_3 : 236 -> 260
~ -[PTUIEditingServer _settingsSection] : 356 -> 372
~ -[PTUIEditingServer _settingsGroupRow:] : 276 -> 292
~ -[PTUIEditingServer _settingsDomainGroupModule:] : 440 -> 464
~ -[PTUIEditingServer _settingsDomainRow:] : 308 -> 328
~ -[PTUIEditingServer choiceRow:titleForSection:] : 352 -> 348
~ ___47-[PTUIEditingServer choiceRow:titleForSection:]_block_invoke : 216 -> 224
~ -[PTUIEditingServer choiceRow:valueForRow:inSection:] : 80 -> 84
~ -[PTUIEditingServer choiceRow:titleForRow:inSection:] : 112 -> 120
~ -[PTUIEditingServer _enumerateDomainsWithOneOrMoreTestRecipesUsingBlock:] : 528 -> 540
~ -[PTUIEditingServer _recipeIDForRow:inSection:] : 308 -> 304
~ ___47-[PTUIEditingServer _recipeIDForRow:inSection:]_block_invoke : 128 -> 132
~ ____RecursivelyObserveOutletsForSettingsAtKeyPathWithBlock_block_invoke_3 : 160 -> 164
~ -[PTUIRowTableViewCell setRow:] : 140 -> 136
~ -[PTUIRowTableViewCell updateDisplayedContent] : 196 -> 220
~ -[PTUIRowTableViewCell updateCellCharacteristics] : 208 -> 228
~ -[PTUISwitchRowTableViewCell initWithStyle:reuseIdentifier:] : 212 -> 220
~ -[PTUISwitchRowTableViewCell updateDisplayedValue] : 120 -> 128
~ -[PTUISwitchRowTableViewCell _valueChanged:] : 136 -> 144
~ -[PTUISliderRowTableViewCell initWithStyle:reuseIdentifier:] : 520 -> 532
~ ___41-[PTUISliderRowTableViewCell updateLabel]_block_invoke : 428 -> 444
~ ___55-[PTUISliderRowTableViewCell updateCellCharacteristics]_block_invoke : 160 -> 164
~ ___50-[PTUISliderRowTableViewCell updateDisplayedValue]_block_invoke : 132 -> 140
~ ___44-[PTUISliderRowTableViewCell _valueChanged:]_block_invoke : 152 -> 160
~ -[PTUISliderRowTableViewCell textFieldDidBeginEditing:] : 172 -> 184
~ -[PTUISliderRowTableViewCell textFieldDidEndEditing:] : 192 -> 208
~ ___55-[PTUISliderRowTableViewCell numericKeypadWillDismiss:]_block_invoke : 152 -> 156
~ -[PTUIChoiceRowTableViewCell updateDisplayedValue] : 248 -> 276
~ -[PTUIEditRowTableViewCell initWithStyle:reuseIdentifier:] : 280 -> 300
~ -[PTUIEditRowTableViewCell updateDisplayedValue] : 144 -> 160
~ -[PTUIEditRowTableViewCell textFieldDidBeginEditing:] : 200 -> 212
~ -[PTUIEditRowTableViewCell textFieldDidEndEditing:] : 236 -> 256
~ ___56-[PTUIEditRowTableViewCell numericKeypadDidUpdateValue:]_block_invoke : 144 -> 156
~ ___53-[PTUIEditRowTableViewCell numericKeypadWillDismiss:]_block_invoke : 68 -> 72
~ -[PTUIEditFloatRowTableViewCell textForValue:] : 180 -> 188
~ -[PTUIEditStringRowTableViewCell textForValue:] : 8 -> 56
~ -[PTUIEditStringRowTableViewCell valueForText:] : 8 -> 56
~ ___53-[PTUIDrillDownRowTableViewCell updateDisplayedValue]_block_invoke : 120 -> 132
~ -[PTUIButtonRowTableViewCell initWithStyle:reuseIdentifier:] : 240 -> 264
~ ___49-[PTUIPushViewControllerRowAction defaultHandler]_block_invoke : 180 -> 184
~ -[PTUIModuleController initWithSettings:presentingRow:] : 112 -> 116
~ -[PTUIModuleController _initWithModule:presentingRow:] : 244 -> 252
~ -[PTUIModuleController _reloadWithModule:] : 192 -> 196
~ -[PTUIModuleController _updateTitle] : 168 -> 184
~ -[PTUIModuleController module:didInsertSections:deleteSections:] : 204 -> 216
~ -[PTUIModuleController module:didInsertRows:deleteRows:] : 204 -> 216
~ -[PTUIModuleController moduleDidReload:] : 64 -> 68
~ -[PTUIModuleController tableView:numberOfRowsInSection:] : 72 -> 76
~ -[PTUIModuleController tableView:viewForHeaderInSection:] : 200 -> 212
~ -[PTUIModuleController tableView:titleForFooterInSection:] : 132 -> 144
~ -[PTUIModuleController tableView:cellForRowAtIndexPath:] : 224 -> 236
~ -[PTUIModuleController tableView:heightForRowAtIndexPath:] : 88 -> 92
~ -[PTUIModuleController tableView:didSelectRowAtIndexPath:] : 320 -> 340
~ -[PTUIModuleController showActionsForRowTableViewCell:] : 260 -> 272
~ -[PTUIChoiceViewController initWithPresentingRow:] : 260 -> 276
~ -[PTUIChoiceViewController rowDidReload:] : 64 -> 68
~ -[PTUIChoiceViewController tableView:viewForHeaderInSection:] : 180 -> 188
~ -[PTUIChoiceViewController tableView:cellForRowAtIndexPath:] : 316 -> 332
~ -[PTUIChoiceViewController tableView:didSelectRowAtIndexPath:] : 216 -> 224
~ -[PTUIChoiceViewController _checkAppropriateCell] : 248 -> 272
~ -[PTUIChoiceViewController setRow:] : 20 -> 80
~ -[_PTUIChoiceCell setTitle:] : 96 -> 100
~ -[_PTUIChoiceCell setChecked:] : 152 -> 164
~ -[PTDrillDownRow(UI) defaultUIAction] : 140 -> 144
~ ___37-[PTDrillDownRow(UI) defaultUIAction]_block_invoke : 168 -> 172
~ -[PTUISettingsController initWithRootModuleController:] : 76 -> 80
~ -[PTUISettingsController viewDidLoad] : 232 -> 248
~ -[PTUISettingsController setDismissButton:] : 316 -> 324
~ -[PTUISettingsController pushViewController:animated:] : 132 -> 140
~ -[PTUISettingsController _didTap:] : 68 -> 72
~ -[PTUISettingsController _dismiss] : 72 -> 76
~ -[PTUISettingsController _reloadWithRootModule:] : 224 -> 244

```
