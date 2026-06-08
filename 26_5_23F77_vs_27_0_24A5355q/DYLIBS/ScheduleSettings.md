## ScheduleSettings

> `/System/Library/PreferenceBundles/ScheduleSettings.bundle/ScheduleSettings`

```diff

 91.0.0.0.0
-  __TEXT.__text: 0x312c
-  __TEXT.__auth_stubs: 0x240
+  __TEXT.__text: 0x329c
   __TEXT.__objc_methlist: 0x3e0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x35e
   __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x71
-  __TEXT.__objc_methname: 0xf56
-  __TEXT.__objc_methtype: 0x258
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x1d0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x570
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x168

   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B080A57-09AD-38C9-9C2C-2C00D9925A00
+  UUID: 43ABC53E-F3D9-3C19-9D95-CD1542255ED1
   Functions: 63
   Symbols:   428
-  CStrings:  343
+  CStrings:  89
 
Functions:
~ +[PushedMailboxTableCell _iconForType:nested:] : 120 -> 132
~ -[PushedMailboxTableCell initWithStyle:reuseIdentifier:] : 156 -> 160
~ -[PushedMailboxTableCell dealloc] : 100 -> 108
~ -[PushedMailboxTableCell _setupMailFolderIconForImage:] : 148 -> 152
~ -[PushedMailboxTableCell setType:] : 88 -> 92
~ -[PushedMailboxTableCell setMailboxName:] : 16 -> 20
~ -[PushedMailboxTableCell setEnabled:] : 120 -> 124
~ -[PushedMailboxTableCell layoutSubviews] : 560 -> 572
~ -[PushedMailboxTableCell level] : 16 -> 20
~ -[PushedMailboxTableCell setLevel:] : 16 -> 20
~ -[ScheduleSettingsController initForContentSize:] : 172 -> 180
~ -[ScheduleSettingsController dealloc] : 120 -> 128
~ -[ScheduleSettingsController _lowPowerModeChangedNotification:] : 156 -> 160
~ -[ScheduleSettingsController specifiers] : 1136 -> 1152
~ -[ScheduleSettingsController _makeMCCSpecifiers] : 552 -> 560
~ -[ScheduleSettingsController _specifiersForMCCAccount:] : 432 -> 436
~ -[ScheduleSettingsController _specifierForMCCAccount:dataclasses:canPush:canFetch:canManual:] : 864 -> 876
~ -[ScheduleSettingsController _mccSchedule:] : 156 -> 160
~ -[ScheduleSettingsController _readScheduleSettings] : 476 -> 496
~ -[ScheduleSettingsController pushEnabled:] : 100 -> 104
~ -[ScheduleSettingsController setPushEnabled:specifier:] : 100 -> 108
~ -[ScheduleSettingsController setPollInterval:specifier:] : 260 -> 280
~ -[ScheduleSettingsController updateRadioGroupText] : 368 -> 372
~ -[ScheduleSettingsController listItemSelected:] : 368 -> 392
~ -[ScheduleSettingsController tableView:cellForRowAtIndexPath:] : 216 -> 224
~ -[ScheduleSettingsController tableView:willDisplayCell:forRowAtIndexPath:] : 108 -> 112
~ -[ScheduleSettingsController tableView:didSelectRowAtIndexPath:] : 168 -> 172
~ -[ScheduleSettingsController tableView:heightForRowAtIndexPath:] : 120 -> 124
~ -[ScheduleSettingsStyleController dealloc] : 152 -> 168
~ -[ScheduleSettingsStyleController viewWillAppear:] : 228 -> 232
~ -[ScheduleSettingsStyleController viewWillDisappear:] : 164 -> 168
~ -[ScheduleSettingsStyleController specifiers] : 1124 -> 1156
~ -[ScheduleSettingsStyleController reloadFolders] : 332 -> 344
~ ___48-[ScheduleSettingsStyleController reloadFolders]_block_invoke : 324 -> 340
~ -[ScheduleSettingsStyleController shouldShowMailboxes] : 120 -> 132
~ -[ScheduleSettingsStyleController notAvailableText] : 216 -> 224
~ -[ScheduleSettingsStyleController setPushStateForMailbox:state:] : 224 -> 232
~ ___64-[ScheduleSettingsStyleController setPushStateForMailbox:state:]_block_invoke : 20 -> 24
~ -[ScheduleSettingsStyleController _reloadFoldersAndSpecifiersForced:] : 240 -> 252
~ -[ScheduleSettingsStyleController tableView:cellForRowAtIndexPath:] : 376 -> 384
~ -[ScheduleSettingsStyleController tableView:didSelectRowAtIndexPath:] : 292 -> 300
CStrings:
- "#16@0:8"
- "@\"ACAccount\""
- "@\"ACAccountStore\""
- "@\"NSArray\""
- "@\"NSMutableSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PSSpecifier\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@32@0:8{CGSize=dd}16"
- "@40@0:8:16@24@32"
- "@44@0:8@16@24B32B36B40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I"
- "I16@0:8"
- "NSObject"
- "Q16@0:8"
- "ScheduleSettingsController"
- "ScheduleSettingsStyleController"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TI,N,V_level"
- "TQ,R"
- "UIActionSheetDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_account"
- "_accountStore"
- "_accountsChanged"
- "_cacheIndexForType:"
- "_checkedSpecifier"
- "_fetchDividerRow"
- "_iconForType:nested:"
- "_ignoringNotifications"
- "_isExchangeAccount"
- "_isLowPowerMode"
- "_isNaturallyRTL"
- "_level"
- "_lowPowerModeChangedNotification:"
- "_mailAccountUniqueId"
- "_mailboxIcon"
- "_mailboxInfos"
- "_mailboxName"
- "_makeMCCSpecifiers"
- "_mccSchedule:"
- "_monitored"
- "_radioGroup"
- "_readScheduleSettings"
- "_reloadFoldersAndSpecifiers"
- "_reloadFoldersAndSpecifiersForced:"
- "_rowToSelect"
- "_setMCCSchedule:specifier:"
- "_setMarginWidth:"
- "_setShouldHaveFullLengthBottomSeparator:"
- "_setupMailFolderIconForImage:"
- "_specifierForMCCAccount:dataclasses:canPush:canFetch:canManual:"
- "_specifiersForMCCAccount:"
- "_supportsUserPushedMailboxes"
- "_systemInteractionTintColor"
- "accessoryType"
- "accountType"
- "accountWithUniqueId:"
- "accountsWithAccountType:"
- "actionSheet:clickedButtonAtIndex:"
- "actionSheet:didDismissWithButtonIndex:"
- "actionSheet:willDismissWithButtonIndex:"
- "actionSheetCancel:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "allAccountTypes"
- "allObjects"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bounds"
- "bundleForClass:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "cellForRowAtIndexPath:"
- "class"
- "configureFetchDividerCell:atIndexPath:"
- "conformsToProtocol:"
- "containsObject:"
- "contentView"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d32@0:8@16@24"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "dequeueReusableCellWithIdentifier:"
- "description"
- "deselectRowAtIndexPath:animated:"
- "dictionaryWithObjects:forKeys:count:"
- "didPresentActionSheet:"
- "enabledDataclasses"
- "frame"
- "getGroup:row:ofSpecifierID:"
- "groupSpecifierWithName:"
- "hash"
- "i24@0:8q16"
- "i32@0:8@16@24"
- "identifier"
- "imageWithTintColor:"
- "indexForIndexPath:"
- "indexOfObject:"
- "indexPathForIndex:"
- "init"
- "initForContentSize:"
- "initWithFrame:"
- "initWithImage:"
- "initWithObjects:"
- "initWithStyle:reuseIdentifier:"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "isChecked"
- "isEqual:"
- "isEqualToSet:"
- "isEqualToString:"
- "isExcludedAccountType:"
- "isKindOfClass:"
- "isLowPowerModeEnabled"
- "isMemberOfClass:"
- "isProxy"
- "isUserInteractionEnabled"
- "labelColor"
- "layoutSubviews"
- "level"
- "listItemSelected:"
- "loadSpecifiersFromPlistName:target:"
- "localizedStringForKey:value:table:"
- "longValue"
- "mailAccounts"
- "mailboxListingForAccountWithUniqueIdentifier:keys:completionBlock:"
- "mutableCopy"
- "navigationController"
- "notAvailableText"
- "noteNumberOfRowsChanged"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLong:"
- "objectAtIndex:"
- "objectForKey:"
- "parentAccount"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "popViewControllerAnimated:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "prepareForReuse"
- "processInfo"
- "propertyForKey:"
- "pushEnabled:"
- "q"
- "release"
- "reloadData"
- "reloadFolders"
- "reloadSpecifier:"
- "reloadSpecifiers"
- "removeObject:"
- "removeObserver:"
- "removePropertyForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "secondaryLabelColor"
- "self"
- "setAccessoryType:"
- "setAccessoryView:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setCellAction:"
- "setCellTarget:"
- "setChecked:"
- "setContentMode:"
- "setEnabled:"
- "setFont:"
- "setFrame:"
- "setImage:"
- "setLevel:"
- "setMailboxName:"
- "setName:"
- "setPollInterval:specifier:"
- "setProperty:forKey:"
- "setPushEnabled:specifier:"
- "setPushStateForMailbox:state:"
- "setPushStateForMailboxWithPath:account:pushState:error:"
- "setTarget:"
- "setText:"
- "setTextColor:"
- "setType:"
- "setUserInfo:"
- "setValue:"
- "setValues:titles:"
- "shouldShowMailboxes"
- "sizeToFit"
- "specifier"
- "specifierAtIndex:"
- "specifierForID:"
- "specifierWithStyle:account:detailControllerClass:presentationStyle:"
- "specifiers"
- "styleForAccount:uniqueIdentifier:"
- "superclass"
- "supportsPush"
- "supportsUserPushedMailboxes"
- "systemFontOfSize:"
- "systemImageNamed:"
- "table"
- "tableSeparatorLightColor"
- "tableView:cellForRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tag"
- "uniqueID"
- "uniqueIdForPersistentConnection"
- "updateRadioGroupText"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"UIActionSheet\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"UIActionSheet\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v40@0:8@16@24@32"
- "values"
- "viewWillAppear:"
- "viewWillDisappear:"
- "willPresentActionSheet:"
- "zone"

```
