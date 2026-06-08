## PrototypeToolsUI

> `/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI`

```diff

-160.0.0.0.0
-  __TEXT.__text: 0x961c
-  __TEXT.__auth_stubs: 0x330
+163.0.0.0.0
+  __TEXT.__text: 0x91b4
   __TEXT.__objc_methlist: 0x1200
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__cstring: 0x31d
+  __TEXT.__cstring: 0x32a
   __TEXT.__ustring: 0x28a
-  __TEXT.__unwind_info: 0x3e8
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x2f8e
-  __TEXT.__objc_methtype: 0x102d
-  __TEXT.__objc_stubs: 0x2640
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x460
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x40

   __DATA_CONST.__objc_selrefs: 0xeb0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x2bb8
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0x540

   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A454908B-58EC-31E1-81BB-45789AB0DCEE
+  UUID: BA4357D1-5E99-39C9-A528-272C44703B89
   Functions: 263
-  Symbols:   1299
-  CStrings:  776
+  Symbols:   1303
+  CStrings:  63
 
Symbols:
+ ___block_literal_global.141
+ ___block_literal_global.143
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- ___block_literal_global.142
- ___block_literal_global.144
- _objc_retainAutoreleasedReturnValue
Functions:
~ _PTUINumericKeypadSetNeededWithWindow : 64 -> 16
~ -[_KeypadButton initWithKeyType:digit:target:] : 620 -> 592
~ __KeypadForegroundColor : 84 -> 68
~ __KeypadBackgroundColor : 84 -> 68
~ -[_KeypadButton _updateBackgroundColor] : 116 -> 108
~ -[_KeypadButton keyType] : 16 -> 20
~ -[_KeypadButton digit] : 16 -> 20
~ -[_KeypadDismissButton initWithFrame:] : 372 -> 340
~ -[_KeypadDismissButton setHighlighted:] : 136 -> 128
~ +[PTUINumericKeypad sharedKeypad] : 176 -> 160
~ -[PTUINumericKeypad init] : 1072 -> 1056
~ -[PTUINumericKeypad hideAnimated:] : 284 -> 292
~ ___34-[PTUINumericKeypad hideAnimated:]_block_invoke_2 : 28 -> 32
~ -[PTUINumericKeypad doubleValue] : 368 -> 372
~ -[PTUINumericKeypad setDoubleValue:] : 792 -> 780
~ -[PTUINumericKeypad stringValue] : 460 -> 472
~ -[PTUINumericKeypad layoutSubviews] : 940 -> 908
~ -[PTUINumericKeypad pointInside:withEvent:] : 176 -> 180
~ -[PTUINumericKeypad _layoutButtonRow:atY:stretch:] : 488 -> 472
~ -[PTUINumericKeypad _updateDisplayedValue] : 160 -> 172
~ -[PTUINumericKeypad keyPress:] : 192 -> 184
~ -[PTUINumericKeypad _appendDigit:] : 260 -> 264
~ -[PTUINumericKeypad _remainingAllowedDigits] : 88 -> 96
~ -[PTUINumericKeypad _appendDot] : 32 -> 36
~ -[PTUINumericKeypad _changeSign] : 24 -> 28
~ -[PTUINumericKeypad _clear] : 108 -> 124
~ -[PTUINumericKeypad _backspace] : 196 -> 212
~ -[PTUINumericKeypad _dismissButtonPress] : 76 -> 80
~ ___27-[PTUINumericKeypad _flash]_block_invoke : 96 -> 100
~ ____KeypadForegroundColor_block_invoke : 76 -> 72
~ ____KeypadBackgroundColor_block_invoke : 80 -> 76
~ ____KeypadFlashColor_block_invoke : 76 -> 72
~ -[PTUIModifiedChangesViewController _populateTableDataAndChildren] : 596 -> 568
~ -[PTUIModifiedChangesViewController viewDidLoad] : 236 -> 228
~ -[PTUIModifiedChangesViewController initWithParameterRecords:withTitle:] : 156 -> 160
~ -[PTUIModifiedChangesViewController tableView:didSelectRowAtIndexPath:] : 336 -> 332
~ -[PTUIModifiedChangesViewController tableView:numberOfRowsInSection:] : 44 -> 48
~ -[PTUIModifiedChangesViewController tableView:cellForRowAtIndexPath:] : 440 -> 424
~ -[PTUIEditingServer initWithDataSource:delegate:forRemoteEditing:] : 408 -> 404
~ -[PTUIEditingServer reloadDomains] : 160 -> 152
~ -[PTUIEditingServer reloadTestRecipes] : 148 -> 140
~ -[PTUIEditingServer proxyDefinitionChanged:] : 408 -> 368
~ -[PTUIEditingServer rootSettingsForDomainID:] : 140 -> 132
~ -[PTUIEditingServer domainGroupNames] : 268 -> 248
~ ___37-[PTUIEditingServer domainGroupNames]_block_invoke : 92 -> 88
~ -[PTUIEditingServer domainIDsInGroup:] : 360 -> 364
~ ___38-[PTUIEditingServer domainIDsInGroup:]_block_invoke : 132 -> 128
~ ___38-[PTUIEditingServer domainIDsInGroup:]_block_invoke_2 : 200 -> 184
~ -[PTUIEditingServer displayNameForDomainID:] : 88 -> 80
~ -[PTUIEditingServer groupNameForDomainID:] : 88 -> 80
~ -[PTUIEditingServer testRecipeIDsForDomainID:] : 360 -> 364
~ ___46-[PTUIEditingServer testRecipeIDsForDomainID:]_block_invoke : 132 -> 128
~ ___46-[PTUIEditingServer testRecipeIDsForDomainID:]_block_invoke_2 : 200 -> 184
~ -[PTUIEditingServer titleForTestRecipeID:] : 88 -> 80
~ -[PTUIEditingServer testRecipeSelectionModule] : 204 -> 192
~ -[PTUIEditingServer settingsEditingModule] : 204 -> 192
~ -[PTUIEditingServer settings:changedValueForKeyPath:] : 184 -> 176
~ -[PTUIEditingServer settingsDidRestoreDefaults:] : 104 -> 100
~ -[PTUIEditingServer _loadRootSettingsOrProxyForDomainID:] : 592 -> 564
~ __RecursivelyObserveOutletsForSettingsAtKeyPathWithBlock : 300 -> 320
~ -[PTUIEditingServer _testRecipeSection] : 668 -> 656
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke : 108 -> 92
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke_2 : 132 -> 124
~ ___39-[PTUIEditingServer _testRecipeSection]_block_invoke_3 : 260 -> 236
~ -[PTUIEditingServer _settingsSection] : 372 -> 360
~ -[PTUIEditingServer _settingsGroupRow:] : 292 -> 276
~ -[PTUIEditingServer _settingsDomainGroupModule:] : 464 -> 444
~ -[PTUIEditingServer _settingsDomainRow:] : 328 -> 308
~ -[PTUIEditingServer choiceRow:titleForSection:] : 348 -> 352
~ ___47-[PTUIEditingServer choiceRow:titleForSection:]_block_invoke : 224 -> 216
~ -[PTUIEditingServer choiceRow:valueForRow:inSection:] : 84 -> 80
~ -[PTUIEditingServer choiceRow:titleForRow:inSection:] : 120 -> 112
~ -[PTUIEditingServer _enumerateDomainsWithOneOrMoreTestRecipesUsingBlock:] : 540 -> 532
~ -[PTUIEditingServer _recipeIDForRow:inSection:] : 304 -> 308
~ ___47-[PTUIEditingServer _recipeIDForRow:inSection:]_block_invoke : 132 -> 128
~ ____RecursivelyObserveOutletsForSettingsAtKeyPathWithBlock_block_invoke_3 : 164 -> 160
~ -[PTUIRowTableViewCell dealloc] : 88 -> 92
~ -[PTUIRowTableViewCell setRow:] : 136 -> 144
~ -[PTUIRowTableViewCell updateDisplayedContent] : 220 -> 196
~ -[PTUIRowTableViewCell updateCellCharacteristics] : 228 -> 208
~ -[PTUIRowTableViewCell row] : 16 -> 20
~ -[PTUISwitchRowTableViewCell initWithStyle:reuseIdentifier:] : 220 -> 216
~ -[PTUISwitchRowTableViewCell updateDisplayedValue] : 128 -> 124
~ -[PTUISwitchRowTableViewCell _valueChanged:] : 144 -> 140
~ -[PTUISliderRowTableViewCell initWithStyle:reuseIdentifier:] : 532 -> 528
~ ___41-[PTUISliderRowTableViewCell updateLabel]_block_invoke : 444 -> 440
~ ___55-[PTUISliderRowTableViewCell updateCellCharacteristics]_block_invoke : 164 -> 168
~ ___50-[PTUISliderRowTableViewCell updateDisplayedValue]_block_invoke : 140 -> 136
~ ___44-[PTUISliderRowTableViewCell _valueChanged:]_block_invoke : 160 -> 156
~ -[PTUISliderRowTableViewCell textFieldDidBeginEditing:] : 184 -> 172
~ -[PTUISliderRowTableViewCell textFieldDidEndEditing:] : 208 -> 196
~ ___58-[PTUISliderRowTableViewCell numericKeypadDidUpdateValue:]_block_invoke : 108 -> 116
~ -[PTUIChoiceRowTableViewCell updateDisplayedValue] : 276 -> 248
~ -[PTUIEditRowTableViewCell initWithStyle:reuseIdentifier:] : 300 -> 280
~ -[PTUIEditRowTableViewCell updateDisplayedValue] : 160 -> 144
~ -[PTUIEditRowTableViewCell textFieldDidBeginEditing:] : 212 -> 200
~ -[PTUIEditRowTableViewCell textFieldDidEndEditing:] : 256 -> 236
~ ___56-[PTUIEditRowTableViewCell numericKeypadDidUpdateValue:]_block_invoke : 156 -> 144
~ ___53-[PTUIEditRowTableViewCell numericKeypadWillDismiss:]_block_invoke : 72 -> 68
~ -[PTUIEditFloatRowTableViewCell textForValue:] : 188 -> 180
~ -[PTUIEditStringRowTableViewCell textForValue:] : 56 -> 8
~ -[PTUIEditStringRowTableViewCell valueForText:] : 56 -> 8
~ ___53-[PTUIDrillDownRowTableViewCell updateDisplayedValue]_block_invoke : 132 -> 120
~ -[PTUIButtonRowTableViewCell initWithStyle:reuseIdentifier:] : 264 -> 240
~ +[PTUIPushViewControllerRowAction actionWithViewControllerCreator:] : 120 -> 124
~ -[PTUIPushViewControllerRowAction viewControllerCreator] : 16 -> 20
~ +[PTUIPresentViewControllerRowAction actionWithViewControllerCreator:] : 120 -> 124
~ ___52-[PTUIPresentViewControllerRowAction defaultHandler]_block_invoke : 160 -> 164
~ -[PTUIPresentViewControllerRowAction viewControllerCreator] : 16 -> 20
~ -[PTUIModuleController initWithSettings:presentingRow:] : 116 -> 112
~ -[PTUIModuleController _initWithModule:presentingRow:] : 252 -> 248
~ -[PTUIModuleController settings] : 16 -> 20
~ -[PTUIModuleController _reloadWithModule:] : 196 -> 200
~ -[PTUIModuleController _updateTitle] : 184 -> 172
~ -[PTUIModuleController module:didInsertSections:deleteSections:] : 216 -> 204
~ -[PTUIModuleController module:didInsertRows:deleteRows:] : 216 -> 204
~ -[PTUIModuleController moduleDidReload:] : 68 -> 64
~ -[PTUIModuleController numberOfSectionsInTableView:] : 16 -> 20
~ -[PTUIModuleController tableView:viewForHeaderInSection:] : 212 -> 204
~ -[PTUIModuleController tableView:titleForFooterInSection:] : 144 -> 136
~ -[PTUIModuleController tableView:cellForRowAtIndexPath:] : 236 -> 228
~ -[PTUIModuleController tableView:didSelectRowAtIndexPath:] : 340 -> 324
~ -[PTUIModuleController showActionsForRowTableViewCell:] : 272 -> 260
~ -[PTUIChoiceViewController initWithPresentingRow:] : 276 -> 268
~ -[PTUIChoiceViewController dealloc] : 88 -> 92
~ -[PTUIChoiceViewController rowDidReload:] : 68 -> 64
~ -[PTUIChoiceViewController numberOfSectionsInTableView:] : 16 -> 20
~ -[PTUIChoiceViewController tableView:numberOfRowsInSection:] : 20 -> 24
~ -[PTUIChoiceViewController tableView:viewForHeaderInSection:] : 188 -> 184
~ -[PTUIChoiceViewController tableView:cellForRowAtIndexPath:] : 332 -> 312
~ -[PTUIChoiceViewController tableView:didSelectRowAtIndexPath:] : 224 -> 220
~ -[PTUIChoiceViewController _checkAppropriateCell] : 272 -> 248
~ -[PTUIChoiceViewController row] : 16 -> 20
~ -[PTUIChoiceViewController setRow:] : 80 -> 20
~ -[_PTUIChoiceCell setTitle:] : 100 -> 96
~ -[_PTUIChoiceCell setChecked:] : 164 -> 152
~ -[PTDrillDownRow(UI) defaultUIAction] : 144 -> 140
~ ___37-[PTDrillDownRow(UI) defaultUIAction]_block_invoke : 172 -> 168
~ -[PTUISettingsController initWithRootModuleController:] : 80 -> 76
~ -[PTUISettingsController viewDidLoad] : 248 -> 232
~ -[PTUISettingsController setDismissButton:] : 324 -> 316
~ -[PTUISettingsController pushViewController:animated:] : 140 -> 136
~ -[PTUISettingsController _didTap:] : 72 -> 68
~ -[PTUISettingsController _dismiss] : 76 -> 72
~ -[PTUISettingsController _reloadWithRootModule:] : 244 -> 224
~ -[PTUISettingsController dismissButton] : 16 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PTEditingServerDataSource>\""
- "@\"<PTEditingServerDelegate>\""
- "@\"<PTUINumericKeypadDelegate>\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSDictionary\""
- "@\"NSIndexPath\""
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"PTChoiceRow\"16q24"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"NSString\"40@0:8@\"PTChoiceRow\"16q24q32"
- "@\"PTChoiceRow\""
- "@\"PTModule\""
- "@\"PTParameterRecords\""
- "@\"PTRow\""
- "@\"UIBarButtonItem\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UILabel\""
- "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UISlider\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UISwitch\""
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UITextField\""
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"_KeypadButton\""
- "@\"_KeypadDismissButton\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8q16@24"
- "@32@0:8q16q24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@\"PTChoiceRow\"16q24q32"
- "@40@0:8@16@24@32"
- "@40@0:8@16q24q32"
- "@40@0:8q16Q24@32"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@\"UITextField\"16"
- "B24@0:8@16"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B40@0:8{CGPoint=dd}16@32"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16:24@32@40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "CGColor"
- "NSObject"
- "PTChoiceRowDataSource"
- "PTModuleObserver"
- "PTRowObserver"
- "PTSettingsKeyPathObserver"
- "PTUIButtonRowTableViewCell"
- "PTUIChoiceRowTableViewCell"
- "PTUIChoiceViewController"
- "PTUIClient"
- "PTUIDrillDownRowTableViewCell"
- "PTUIEditFloatRowTableViewCell"
- "PTUIEditRowTableViewCell"
- "PTUIEditStringRowTableViewCell"
- "PTUIEditingServer"
- "PTUIModifiedChangesViewController"
- "PTUIModuleController"
- "PTUINumericKeypad"
- "PTUINumericKeypadDelegate"
- "PTUIPaddedHeaderLabel"
- "PTUIPresentViewControllerRowAction"
- "PTUIPushViewControllerRowAction"
- "PTUIRowTableViewCell"
- "PTUIServer"
- "PTUISettingsController"
- "PTUISliderRowTableViewCell"
- "PTUISwitchRowTableViewCell"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"PTChoiceRow\",&,N,V_row"
- "T@\"PTRow\",&,N,V_row"
- "T@\"PTSettings\",R,N"
- "T@\"UIBarButtonItem\",&,N,V_dismissButton"
- "T@?,R,N,V_viewControllerCreator"
- "TB,N,V_forRemoteEditing"
- "TQ,R"
- "TQ,R,N,V_digit"
- "Td,N"
- "Tq,R,N,V_keyType"
- "UI"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "UITextFieldDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_KeypadButton"
- "_KeypadButtonTarget"
- "_KeypadDismissButton"
- "_PTSettingsRestoreDefaultsObserver"
- "_PTUIChoiceCell"
- "_appendDigit:"
- "_appendDot"
- "_archiveValueForKeyPath:"
- "_backgroundView"
- "_backspace"
- "_backspaceButton"
- "_cachedNumberValue"
- "_cachedStringValue"
- "_canShowWhileLocked"
- "_changeSign"
- "_checkAppropriateCell"
- "_children"
- "_clear"
- "_clearButton"
- "_dataSource"
- "_defaultDismissButton"
- "_delegate"
- "_didTap:"
- "_digit"
- "_digitButtons"
- "_digitsAfterDot"
- "_digitsBeforeDot"
- "_dismiss"
- "_dismissButton"
- "_dismissButtonPress"
- "_domainGroupNames"
- "_domainIDsByGroupName"
- "_domainInfoByID"
- "_dotButton"
- "_enumerateChildrenWithBlock:"
- "_enumerateDomainsWithOneOrMoreTestRecipesUsingBlock:"
- "_enumerateOutletsWithBlock:"
- "_flash"
- "_forRemoteEditing"
- "_hasDot"
- "_initWithModule:presentingRow:"
- "_keyType"
- "_layoutButtonRow:atY:"
- "_layoutButtonRow:atY:stretch:"
- "_loadRootSettingsOrProxyForDomainID:"
- "_module"
- "_moduleControllerByDomainID"
- "_negative"
- "_parameterRecords"
- "_populateTableDataAndChildren"
- "_proxyDefinitionsByDomainID"
- "_recipeIDForRow:inSection:"
- "_reloadWithModule:"
- "_reloadWithRootModule:"
- "_remainingAllowedDigits"
- "_rootSettingsByDomainID"
- "_row"
- "_rowTitle"
- "_setContinuousCornerRadius:"
- "_setObservationEnabled:"
- "_setRestoreDefaultsObserver:"
- "_settingsDomainGroupModule:"
- "_settingsDomainRow:"
- "_settingsGroupRow:"
- "_settingsSection"
- "_showing"
- "_signButton"
- "_slider"
- "_switch"
- "_tableData"
- "_tableView"
- "_testRecipeIDsByDomainID"
- "_testRecipeInfoByID"
- "_testRecipeSection"
- "_textField"
- "_title"
- "_updateBackgroundColor"
- "_updateDisplayedValue"
- "_updateTitle"
- "_valueChanged:"
- "_valueIndexPath"
- "_valueLabel"
- "_viewControllerCreator"
- "action"
- "action:"
- "actionWithViewControllerCreator:"
- "activeTestRecipeID"
- "addAction:"
- "addGestureRecognizer:"
- "addKeyPathObserver:"
- "addObject:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "allKeys"
- "allObjects"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "animateWithDuration:delay:options:animations:completion:"
- "appendFormat:"
- "appendString:"
- "applyArchiveValue:forRootSettingsKeyPath:domainID:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "beginUpdates"
- "boldSystemFontOfSize:"
- "boolValue"
- "bounds"
- "bringSubviewToFront:"
- "cellForRowAtIndexPath:"
- "cellHeightForRow:"
- "cellStyleForRow:"
- "changedValue"
- "childKeyPath"
- "childSettingsForKeyPath:"
- "choiceRow:numberOfRowsInSection:"
- "choiceRow:shortTitleForRow:inSection:"
- "choiceRow:titleForRow:inSection:"
- "choiceRow:titleForSection:"
- "choiceRow:valueForRow:inSection:"
- "class"
- "clearColor"
- "colorWithWhite:alpha:"
- "compare:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "convertPoint:fromView:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "d24@0:8@16"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16d24"
- "d32@0:8@16q24"
- "d36@0:8@16d24B32"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultContentConfiguration"
- "defaultHandler"
- "defaultUIAction"
- "definitionForSettingsClass:"
- "deleteRowsAtIndexPaths:withRowAnimation:"
- "deleteSections:withRowAnimation:"
- "dequeueReusableCellWithIdentifier:"
- "description"
- "deselectRowAtIndexPath:animated:"
- "deselectsRowOnSuccess"
- "detailTextLabel"
- "digit"
- "dismissButton"
- "dismissViewControllerAnimated:completion:"
- "displayNameForDomainID:"
- "domainGroupName"
- "domainGroupNames"
- "domainIDForRootSettings:"
- "domainIDsInGroup:"
- "domainIdentifier"
- "domainInfoByID"
- "domainName"
- "doubleValue"
- "drawTextInRect:"
- "editableTextField"
- "endEditing:"
- "endUpdates"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "events"
- "firstObject"
- "floatValue"
- "footerTextGetter"
- "forRemoteEditing"
- "frame"
- "groupNameForDomainID:"
- "handlePrototypingEvent:"
- "handler"
- "hash"
- "hideAnimated:"
- "image"
- "imageView"
- "indexPathForPreferredFocusedViewInTableView:"
- "indexPathForRow:"
- "indexPathForValue:"
- "init"
- "initWithActivityItems:applicationActivities:"
- "initWithArrangedSubviews:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithDataSource:delegate:forRemoteEditing:"
- "initWithDefaultValues"
- "initWithDictionary:"
- "initWithDigit:target:"
- "initWithFrame:"
- "initWithFrame:style:"
- "initWithKeyType:digit:target:"
- "initWithKeyType:target:"
- "initWithObjects:"
- "initWithParameterRecords:withTitle:"
- "initWithPresentingRow:"
- "initWithReuseIdentifier:"
- "initWithRootModule:"
- "initWithRootModuleController:"
- "initWithRootSettings:"
- "initWithRootViewController:"
- "initWithSettings:"
- "initWithSettings:presentingRow:"
- "initWithStyle:"
- "initWithStyle:reuseIdentifier:"
- "initWithTarget:action:"
- "insertObject:atIndex:"
- "insertRowsAtIndexPaths:withRowAnimation:"
- "insertSections:withRowAnimation:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "invokeOutletAtKeyPath:domainID:"
- "isEditing"
- "isEqual:"
- "isEqualToString:"
- "isHighlighted"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOn"
- "isProxy"
- "isSubclassOfClass:"
- "keyPress:"
- "keyType"
- "killSpringBoard"
- "lastObject"
- "launchForRemoteEditing"
- "layer"
- "layoutSubviews"
- "length"
- "loadSettingsClassBundleIfNecessary"
- "maxValue"
- "minValue"
- "module:didInsertRows:deleteRows:"
- "module:didInsertSections:deleteSections:"
- "moduleDidReload:"
- "moduleWithSettings:"
- "moduleWithTitle:contents:"
- "navigationController"
- "navigationItem"
- "numberOfRows"
- "numberOfRowsInSection:"
- "numberOfSections"
- "numberOfSectionsForChoiceRow:"
- "numberOfSectionsInTableView:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithUnsignedInteger:"
- "numericKeypadDidUpdateValue:"
- "numericKeypadWillDismiss:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "orangeColor"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointInside:withEvent:"
- "popToViewController:animated:"
- "popViewControllerAnimated:"
- "postNotificationName:object:"
- "precision"
- "preferredFontForTextStyle:"
- "prepareForReuse"
- "presentViewController:animated:completion:"
- "presentingViewController"
- "proxyDefinitionChanged:"
- "proxyWithDefinition:"
- "pushViewController:animated:"
- "q"
- "q16@0:8"
- "q24@0:8@\"PTChoiceRow\"16"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"PTChoiceRow\"16q24"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "recipeDescription"
- "recordDictionary"
- "registerClass:forCellReuseIdentifier:"
- "release"
- "reloadData"
- "reloadDomains"
- "reloadSection"
- "reloadTestRecipes"
- "removeAllObjects"
- "removeFromSuperview"
- "removeLastObject"
- "removeObjectAtIndex:"
- "removeObserver:"
- "removeObserver:name:object:"
- "replaceObjectAtIndex:withObject:"
- "resignFirstResponder"
- "respondsToSelector:"
- "restoreDefaultValuesForDomainID:"
- "restoreFromArchiveDictionary:"
- "retain"
- "retainCount"
- "reuseIdentifierForRow:"
- "rootSettingsArchiveForDomainID:"
- "rootSettingsForDomainID:"
- "rootSettingsProxyDefinitionForDomainID:"
- "row"
- "rowAtIndexPath:"
- "rowDidChangeImage:"
- "rowDidChangeTitle:"
- "rowDidChangeValue:"
- "rowDidReload:"
- "rowWithTitle:valueGetter:valueSetter:"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondaryLabelColor"
- "section"
- "sectionAtIndex:"
- "sectionIndexTitlesForTableView:"
- "sectionWithRows:"
- "sectionWithRows:title:"
- "self"
- "sendActionsForControlEvents:"
- "set"
- "setAccessoryType:"
- "setAccessoryView:"
- "setActiveTestRecipeID:"
- "setAlpha:"
- "setAxis:"
- "setBackgroundColor:"
- "setBorderColor:"
- "setBorderWidth:"
- "setCancelsTouchesInView:"
- "setCenter:"
- "setChecked:"
- "setClearButtonMode:"
- "setContentConfiguration:"
- "setContinuous:"
- "setCornerRadius:"
- "setDataSource:"
- "setDelegate:"
- "setDismissButton:"
- "setDoubleValue:"
- "setEditing:animated:"
- "setFont:"
- "setFooterTextGetter:"
- "setForRemoteEditing:"
- "setFrame:"
- "setHighlighted:"
- "setImage:"
- "setKeyboardType:"
- "setMaximumValue:"
- "setMinimumValue:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOn:"
- "setOnTintColor:"
- "setRightBarButtonItem:"
- "setRow:"
- "setSecondaryText:"
- "setSelectionStyle:"
- "setShadowOffset:"
- "setShadowOpacity:"
- "setShadowRadius:"
- "setSpacing:"
- "setStringValue:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTintColor:"
- "setTitle:"
- "setTitle:forState:"
- "setTitleColor:forState:"
- "setTransform:"
- "setUnregisterBlock:"
- "setUserInteractionEnabled:"
- "setValue:"
- "settings"
- "settings:changedValueForKeyPath:"
- "settingsClassName"
- "settingsDidRestoreDefaults:"
- "settingsEditingModule"
- "settingsOrProxyWithDefinition:"
- "settingsWillRestoreDefaults:"
- "sharedKeypad"
- "shortTitleForRow:inSection:"
- "showActionsForRowTableViewCell:"
- "showAnimated:forDelegate:"
- "sizeThatFits:"
- "sizeToFit"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "staticTitle:"
- "string"
- "stringByAppendingFormat:"
- "stringValue"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "superclass"
- "superview"
- "systemFontOfSize:"
- "systemFontOfSize:weight:"
- "tableView"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewCellClass"
- "tableViewDidEndMultipleSelectionInteraction:"
- "testRecipeIDsForDomainID:"
- "testRecipeInfoByID"
- "testRecipeSelectionModule"
- "text"
- "textField:editMenuForCharactersInRange:suggestedActions:"
- "textField:editMenuForCharactersInRanges:suggestedActions:"
- "textField:insertInputSuggestion:"
- "textField:shouldChangeCharactersInRange:replacementString:"
- "textField:shouldChangeCharactersInRanges:replacementString:"
- "textField:willDismissEditMenuWithAnimator:"
- "textField:willPresentEditMenuWithAnimator:"
- "textFieldDidBeginEditing:"
- "textFieldDidChangeSelection:"
- "textFieldDidEndEditing:"
- "textFieldDidEndEditing:reason:"
- "textFieldShouldBeginEditing:"
- "textFieldShouldClear:"
- "textFieldShouldEndEditing:"
- "textFieldShouldReturn:"
- "textForValue:"
- "textLabel"
- "tintColor"
- "title"
- "titleForRow:inSection:"
- "titleForSection:"
- "titleForTestRecipeID:"
- "titleLabel"
- "updateCellCharacteristics"
- "updateDisplayedContent"
- "updateDisplayedValue"
- "updateLabel"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"PTModule\"16"
- "v24@0:8@\"PTRow\"16"
- "v24@0:8@\"PTSettings\"16"
- "v24@0:8@\"PTUINumericKeypad\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@\"UITextField\"16"
- "v24@0:8@\"_KeypadButton\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v32@0:8@\"PTSettings\"16@\"NSString\"24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextField\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v40@0:8@\"PTModule\"16@\"NSArray\"24@\"NSArray\"32"
- "v40@0:8@\"PTModule\"16@\"NSIndexSet\"24@\"NSIndexSet\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "value"
- "valueForRow:inSection:"
- "valueForText:"
- "valueStringFormatter"
- "view"
- "viewControllerCreator"
- "viewControllers"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "whiteColor"
- "window"
- "windowScene"
- "zone"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
