## NanoMailCompanionUI

> `/System/Library/PrivateFrameworks/NanoMailCompanionUI.framework/NanoMailCompanionUI`

```diff

-852.6.0.0.0
-  __TEXT.__text: 0x7174
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0xa58
+861.1.0.0.0
+  __TEXT.__text: 0x69e4
+  __TEXT.__objc_methlist: 0xad0
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__cstring: 0x610
+  __TEXT.__gcc_except_tab: 0x240
+  __TEXT.__cstring: 0x5f5
   __TEXT.__dlopen_cstrs: 0x1cc
-  __TEXT.__oslogstring: 0x1a2
-  __TEXT.__unwind_info: 0x2f8
-  __TEXT.__objc_classname: 0x10d
-  __TEXT.__objc_methname: 0x248c
-  __TEXT.__objc_methtype: 0xb98
-  __TEXT.__objc_stubs: 0x1660
-  __DATA_CONST.__got: 0x168
+  __TEXT.__oslogstring: 0x1fd
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b8
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0xb48
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0xee0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x1e0
+  __DATA.__data: 0x240
   __DATA.__bss: 0xa0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EC828A2-F864-37C7-A7E5-815F5C365A7B
-  Functions: 171
-  Symbols:   800
-  CStrings:  580
+  UUID: 821EF751-6ED0-3401-BEA5-B598E6AA7C96
+  Functions: 168
+  Symbols:   798
+  CStrings:  109
 
Symbols:
+ -[NMCUICloudNotificationAccountDataSource registry:didActivate:]
+ -[NMCUICloudNotificationAccountDataSource registry:didUnpair:]
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table25
+ GCC_except_table5
+ _OBJC_CLASS_$_PDRRegistry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_REFS_PDRRegistryDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NMCUICloudNotificationAccountDataSource
+ __OBJC_LABEL_PROTOCOL_$_PDRRegistryDelegate
+ __OBJC_PROTOCOL_$_PDRRegistryDelegate
+ ___114-[NMCUICloudNotificationAccountDataSource savePCCCredentialForAccount:identity:viewController:stateUpdateHandler:]_block_invoke.100
+ ___114-[NMCUICloudNotificationAccountDataSource savePCCCredentialForAccount:identity:viewController:stateUpdateHandler:]_block_invoke.100.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x9
- -[NMCUICloudNotificationAccountDataSource _handleDidUnpair]
- -[NMCUICloudNotificationAccountDataSource _handlePairedDeviceChanged]
- -[NMCUICloudNotificationAccountDataSource dealloc]
- GCC_except_table17
- GCC_except_table22
- GCC_except_table28
- GCC_except_table6
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_NSUUID
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___114-[NMCUICloudNotificationAccountDataSource savePCCCredentialForAccount:identity:viewController:stateUpdateHandler:]_block_invoke.69
- ___114-[NMCUICloudNotificationAccountDataSource savePCCCredentialForAccount:identity:viewController:stateUpdateHandler:]_block_invoke.69.cold.1
- _objc_autorelease
- _objc_msgSend$activePairedDeviceSelectorBlock
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$defaultCenter
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$removeObserver:name:object:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "Received Paired Device Changed notification from PDR"
+ "Received Unpair notification from PDR"
- "#16@0:8"
- ".cxx_destruct"
- "62a0825b-34dd-490e-9db9-d13ae37f601b"
- "@\"<NMCUIAccountDataSource>\""
- "@\"ACAccount\""
- "@\"NMCUICloudNotificationAccountDataSource\""
- "@\"NNMKAccount\""
- "@\"NPSDomainAccessor\""
- "@\"NPSManager\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSLayoutConstraint\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"PSListController\""
- "@\"UIActivityIndicatorView\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UILabel\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16:24:32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "JSONObjectWithData:options:error:"
- "NMCUIAccount"
- "NMCUIAccountDataSourceObserver"
- "NMCUIAccountsSettingsViewCell"
- "NMCUICloudNotificationAccountDataSource"
- "NMCUICloudNotificationOnboardingViewController"
- "NMCUISpecifierController"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<NMCUIAccountDataSource>\",&,N,V_accountDataSource"
- "T@\"ACAccount\",&,V_acAccount"
- "T@\"NMCUICloudNotificationAccountDataSource\",&,N,V_dataSource"
- "T@\"NNMKAccount\",&,V_nnmkAccount"
- "T@\"NPSDomainAccessor\",&,N,V_domainAccessor"
- "T@\"NPSManager\",&,N,V_syncManager"
- "T@\"NSArray\",&,N,V_accounts"
- "T@\"NSArray\",&,V_notificationSubsections"
- "T@\"NSLayoutConstraint\",&,N,V_tableViewHeightConstraint"
- "T@\"NSMutableSet\",&,N,V_pendingAccountIds"
- "T@\"NSNumber\",&,N,V_deviceSupportsPCC"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"PSListController\",W,N,V_listController"
- "T@\"UIActivityIndicatorView\",&,N,V_spinner"
- "T@\"UILabel\",&,N,V_warningLabel"
- "T@?,C,N,V_completion"
- "TB,N"
- "TB,N,V_cloudNotificationsDecommissioned"
- "TB,N,V_isTinker"
- "TB,N,V_showsAlerts"
- "TB,R,N"
- "TQ,R"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_acAccount"
- "_accountDataSource"
- "_accountSpecifierTapped:"
- "_accounts"
- "_cloudNotificationsDecommissioned"
- "_cloudNotificationsEnabled:"
- "_completion"
- "_dataSource"
- "_deviceSupportsPCC"
- "_displayFailedToSaveAlertShouldDismiss:viewController:"
- "_domainAccessor"
- "_emailAddressFromJWTToken:error:"
- "_ensureValidBase64String:"
- "_getValueForKey:"
- "_handleDidUnpair"
- "_handlePairedDeviceChanged"
- "_isIcloud"
- "_isTinker"
- "_listController"
- "_nnmkAccount"
- "_notificationSubsections"
- "_pendingAccountIds"
- "_setCloudNotificationsEnabled:withSpecifier:"
- "_setValue:forKey:"
- "_showsAlerts"
- "_spinner"
- "_syncManager"
- "_tableViewHeightConstraint"
- "_warningLabel"
- "acAccount"
- "ac_filter:"
- "accountDataSource"
- "accountDataSourceAccountsChanged:"
- "accountDescription"
- "accountHasCredentials:"
- "accountId"
- "accountIsPending:"
- "accountPropertyForKey:"
- "accountShowsAlerts:"
- "accountSupportsNotifications:"
- "accountSupportsNotifications:forceEnabled:"
- "accountType"
- "accountTypeIdentifier"
- "accounts"
- "accountsRequiringCredentials"
- "actionWithTitle:style:handler:"
- "activePairedDeviceSelectorBlock"
- "addAction:"
- "addButton:"
- "addConstraint:"
- "addObject:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addTarget:action:forControlEvents:"
- "alertControllerWithTitle:message:preferredStyle:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "boldButton"
- "boolValue"
- "bundleWithIdentifier:"
- "buttonTray"
- "class"
- "cloudNotificationsDecommissioned"
- "cloudNotificationsEnabled"
- "code"
- "compare:options:"
- "completion"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "constraintEqualToConstant:"
- "containsObject:"
- "contentSize"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "dataSource"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultEmailAddress"
- "dequeueReusableCellWithIdentifier:forIndexPath:"
- "description"
- "detailTextForAccounts:"
- "detailTextLabel"
- "deviceSupportsCloudNotifications"
- "deviceSupportsPCC"
- "dictionaryWithObjects:forKeys:count:"
- "directPushNotificationsSupported"
- "dismissViewControllerAnimated:completion:"
- "displayName"
- "domain"
- "domainAccessor"
- "emailAddress"
- "emailAddressToken"
- "emailAddresses"
- "enableButtonTapped:"
- "enabled"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "groupSpecifierForTinker:"
- "groupSpecifierWithID:"
- "handleAccountAuthenication:viewController:stateUpdateHandler:"
- "hasCloudNotificationAccounts"
- "hash"
- "heightAnchor"
- "identifier"
- "indexPathForPreferredFocusedViewInTableView:"
- "init"
- "initWithACAccount:"
- "initWithAccount:dataSource:completion:"
- "initWithAccountDataSource:"
- "initWithAccounts:dataSource:completion:"
- "initWithActivityIndicatorStyle:"
- "initWithBase64EncodedString:options:"
- "initWithCapacity:"
- "initWithDomain:"
- "initWithEmailOnlyScope:presentationBlock:"
- "initWithFrame:style:"
- "initWithListController:dataSource:isTinker:"
- "initWithNNMKAccount:"
- "initWithStyle:reuseIdentifier:"
- "initWithTitle:detailText:symbolName:"
- "initWithUUIDString:"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTinker"
- "isiCloudEmailAddress:"
- "item"
- "layoutIfNeeded"
- "length"
- "linkButton"
- "listController"
- "localizedStringForKey:value:table:"
- "mailNotificationURL"
- "missingCredentialsForAccounts:"
- "nnmkAccount"
- "notNowButtonTapped:"
- "notificationSubsections"
- "numberOfSectionsInTableView:"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "parentAccount"
- "pendingAccountIds"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "postRequestWithBaseURLString:path:body:token:needsBAA:completion:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "prepareForReuse"
- "presentViewController:animated:completion:"
- "propertyForKey:"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "refreshCellContentsWithSpecifier:"
- "registerClass:forCellReuseIdentifier:"
- "release"
- "reloadData"
- "reloadSpecifiers"
- "removeObject:"
- "removeObserver:"
- "removeObserver:name:object:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reuseIdentifier"
- "rootAccount:"
- "saveAccount:completion:"
- "saveCredential:emailAddress:forAccount:completion:"
- "savePCCCredentialForAccount:identity:viewController:stateUpdateHandler:"
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
- "sectionIndexTitlesForTableView:"
- "self"
- "setAcAccount:"
- "setAccessoryView:"
- "setAccountDataSource:"
- "setAccountProperty:forKey:"
- "setAccounts:"
- "setButtonAction:"
- "setCaptionText:"
- "setCloudNotificationsDecommissioned"
- "setCloudNotificationsDecommissioned:"
- "setCloudNotificationsEnabled:"
- "setCompletion:"
- "setConstant:"
- "setDataSource:"
- "setDelegate:"
- "setDeviceSupportsPCC:"
- "setDomainAccessor:"
- "setEmailAddressToken:"
- "setEnabled:"
- "setFont:"
- "setHidesWhenStopped:"
- "setIsTinker:"
- "setListController:"
- "setName:"
- "setNnmkAccount:"
- "setNotificationSubsections:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPccEmailAddress:"
- "setPendingAccountIds:"
- "setProperty:forKey:"
- "setScrollEnabled:"
- "setSelectionStyle:"
- "setSelectionTintColor:"
- "setShowsAlerts:"
- "setSpinner:"
- "setSyncManager:"
- "setTableView:"
- "setTableViewHeightConstraint:"
- "setText:"
- "setTextColor:"
- "setTitle:forState:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setWarningLabel:"
- "setWithObject:"
- "settingSpecifierWithTarget:set:get:"
- "setupView"
- "sharedInstance"
- "shouldPromptToEnableNotifications:"
- "showsAlerts"
- "sizeToFit"
- "specifierForAccount:onTap:"
- "specifiers"
- "spinner"
- "standaloneState"
- "startAnimating"
- "stopAnimating"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringWithFormat:"
- "superclass"
- "supportsCapability:"
- "syncManager"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "systemFontOfSize:"
- "systemFontSize"
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
- "tableViewDidEndMultipleSelectionInteraction:"
- "tableViewHeightConstraint"
- "textLabel"
- "titleLabel"
- "titleSettingSpecifier"
- "typeIdentifier"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<NMCUIAccountDataSource>\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "view"
- "viewDidLayoutSubviews"
- "viewForZoomingInScrollView:"
- "warningLabel"
- "zone"

```
