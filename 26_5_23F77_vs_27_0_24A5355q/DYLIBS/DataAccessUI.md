## DataAccessUI

> `/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x5f3c
-  __TEXT.__auth_stubs: 0x310
+2703.0.0.0.0
+  __TEXT.__text: 0x5a10
   __TEXT.__objc_methlist: 0x87c
-  __TEXT.__cstring: 0x3c1
+  __TEXT.__cstring: 0x3c5
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x64
+  __TEXT.__gcc_except_tab: 0x54
   __TEXT.__oslogstring: 0x282
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_classname: 0x11d
-  __TEXT.__objc_methname: 0x1ebc
-  __TEXT.__objc_methtype: 0x2c0
-  __TEXT.__objc_stubs: 0x1e00
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9f8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x1a8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0xc40
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x1e8

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 681B8135-A0F9-3BDF-AAFF-CE1704E87447
+  UUID: AD9C9F31-712B-34AC-A2F0-886DACA398EB
   Functions: 147
-  Symbols:   743
-  CStrings:  520
+  Symbols:   751
+  CStrings:  116
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_retain_x24
Functions:
~ -[DASettingsDataclassConfigurationViewController dealloc] : 120 -> 116
~ -[DASettingsDataclassConfigurationViewController accountDescriptionForFirstTimeSetup] : 84 -> 76
~ -[DASettingsDataclassConfigurationViewController _navTitle] : 124 -> 112
~ -[DASettingsDataclassConfigurationViewController loadView] : 132 -> 124
~ -[DASettingsDataclassConfigurationViewController viewDidLoad] : 128 -> 120
~ -[DASettingsDataclassConfigurationViewController viewWillAppear:] : 136 -> 128
~ -[DASettingsDataclassConfigurationViewController daAccount] : 108 -> 96
~ -[DASettingsDataclassConfigurationViewController reloadAccount] : 132 -> 120
~ -[DASettingsDataclassConfigurationViewController accountFromSpecifier] : 320 -> 296
~ -[DASettingsDataclassConfigurationViewController specifiers] : 96 -> 92
~ -[DASettingsDataclassConfigurationViewController otherSpecifiers] : 384 -> 352
~ -[DASettingsDataclassConfigurationViewController accountInfoControllerClass] : 152 -> 144
~ -[DASettingsDataclassConfigurationViewController operationsHelper:didRemoveAccount:withSuccess:error:] : 172 -> 176
~ -[DASettingsDataclassConfigurationViewController cancelButtonClicked:] : 88 -> 84
~ -[DASettingsDataclassConfigurationViewController setDaAccount:] : 80 -> 20
~ +[PSSpecifier(DASettingsAdditions) switchSpecifierWithTitle:target:setter:getter:key:] : 180 -> 176
~ +[PSSpecifier(DASettingsAdditions) buttonSpecifierWithTitle:target:action:confirmationInfo:] : 220 -> 228
~ +[DADiagnosticsPSController linkSpecifier] : 244 -> 232
~ +[DADiagnosticsPSController dumpRuntimeStateSpecifiers] : 292 -> 272
~ -[DADiagnosticsPSController diagnosticSpecifiers] : 140 -> 128
~ -[DADiagnosticsPSController specifiers] : 328 -> 324
~ -[DADiagnosticsPSController alertView:clickedButtonAtIndex:] : 204 -> 208
~ -[DADiagnosticsPSController alertView:didDismissWithButtonIndex:] : 100 -> 104
~ -[DADiagnosticsPSController setBooleanProperty:withSpecifier:] : 152 -> 144
~ -[DADiagnosticsPSController booleanPropertyWithSpecifier:] : 160 -> 148
~ -[DADiagnosticsPSController saveFileAtPath:toDirectory:withExtension:error:] : 368 -> 352
~ -[DADiagnosticsPSController saveLogsWithNotes:] : 896 -> 872
~ _validPathsForPaths : 376 -> 364
~ ___47-[DADiagnosticsPSController saveLogsWithNotes:]_block_invoke : 348 -> 324
~ -[DADiagnosticsPSController _presentNotesController] : 444 -> 436
~ -[DADiagnosticsPSController handleSaveAllLogsStep2] : 336 -> 312
~ -[DADiagnosticsPSController handleSaveAllLogsForSpecifier:] : 516 -> 492
~ -[DADiagnosticsPSController suspend] : 128 -> 124
~ -[DADiagnosticsPSController purgeFileAtPath:] : 172 -> 156
~ -[DADiagnosticsNotesController _disableButtons] : 224 -> 200
~ -[DADiagnosticsNotesController _enableButtons] : 196 -> 176
~ -[DADiagnosticsNotesController _cancelButtonPressed] : 68 -> 64
~ -[DADiagnosticsNotesController _okButtonPressed] : 288 -> 276
~ ___48-[DADiagnosticsNotesController _okButtonPressed]_block_invoke_2 : 92 -> 88
~ -[DADiagnosticsNotesController init] : 508 -> 480
~ -[DADiagnosticsNotesController viewWillAppear:] : 96 -> 92
~ -[DADiagnosticsNotesController shouldAutorotateToInterfaceOrientation:] : 92 -> 88
~ -[DADiagnosticsNotesPane becomeFirstResponder] : 16 -> 20
~ -[DADiagnosticsNotesPane preferenceValue] : 16 -> 20
~ -[DASettingsAccountsUIController account] : 492 -> 416
~ -[DASettingsAccountsUIController reloadAccount] : 132 -> 120
~ -[DASettingsAccountsUIController accountFromSpecifier] : 200 -> 184
~ -[DASettingsAccountsUIController daAccountWithBackingAccountInfo:] : 128 -> 124
~ -[DASettingsAccountsUIController newDefaultAccount] : 128 -> 124
~ -[DASettingsAccountsUIController specifiers] : 196 -> 176
~ -[DASettingsAccountsUIController tableView:cellForRowAtIndexPath:] : 388 -> 364
~ -[DASettingsAccountsUIController showAlertWithButtons:title:message:completion:] : 520 -> 528
~ -[DASettingsAccountsUIController validateAccount] : 128 -> 124
~ -[DASettingsAccountsUIController showIdenticalAccountFailureView] : 396 -> 368
~ -[DASettingsAccountsUIController showSSLFailureView] : 592 -> 556
~ -[DASettingsAccountsUIController didConfirmTryWithoutSSL:] : 332 -> 304
~ -[DASettingsAccountsUIController didConfirmSaveUnvalidatedAccount:] : 116 -> 112
~ -[DASettingsAccountsUIController _confirmSaveUnvalidatedAccount] : 476 -> 448
~ -[DASettingsAccountsUIController account:isValid:validationError:] : 188 -> 184
~ -[DASettingsAccountsUIController finishedAccountSetup] : 376 -> 360
~ -[DASettingsAccountsUIController doneButtonTapped:] : 268 -> 264
~ -[DASettingsAccountsUIController cancelButtonTapped:] : 160 -> 152
~ -[DASettingsAccountsUIController setNeedsSaveAndValidation:] : 36 -> 44
~ -[DASettingsAccountsUIController updateDoneButton] : 364 -> 348
~ -[DASettingsAccountsUIController haveEnoughValues] : 128 -> 124
~ -[DASettingsAccountsUIController setHostString:] : 808 -> 716
~ -[DASettingsAccountsUIController setAccountProperty:withSpecifier:] : 856 -> 788
~ -[DASettingsAccountsUIController accountPropertyWithSpecifier:] : 456 -> 392
~ -[DASettingsAccountsUIController setAccountBooleanProperty:withSpecifier:] : 184 -> 176
~ -[DASettingsAccountsUIController accountBooleanPropertyWithSpecifier:] : 168 -> 156
~ -[DASettingsAccountsUIController _deleteAccount] : 224 -> 208
~ -[DASettingsAccountsUIController operationsHelper:didRemoveAccount:withSuccess:error:] : 260 -> 268
~ ___86-[DASettingsAccountsUIController operationsHelper:didRemoveAccount:withSuccess:error:]_block_invoke : 240 -> 192
~ -[DASettingsAccountsUIController _finishSaveAccountDismissWhenDone:] : 280 -> 264
~ -[DASettingsAccountsUIController _saveAccountDismissWhenDone:] : 264 -> 244
~ -[DASettingsAccountsUIController operationsHelper:didSaveAccount:withSuccess:error:] : 260 -> 268
~ ___84-[DASettingsAccountsUIController operationsHelper:didSaveAccount:withSuccess:error:]_block_invoke : 280 -> 232
~ -[DASettingsAccountsUIController isRunningFromMobileMailApp] : 104 -> 96
~ -[DASettingsAccountsUIController hideProgressWithPrompt:] : 412 -> 388
~ -[DASettingsAccountsUIController dealloc] : 104 -> 100
~ -[DASettingsAccountsUIController viewWillDisappear:] : 312 -> 292
~ -[DASettingsAccountsUIController indexOfCurrentlyEditingCell] : 136 -> 132
~ -[DASettingsAccountsUIController currentlyEditingCell] : 232 -> 220
~ -[DASettingsAccountsUIController lastGroupSpecifierInSpecifiers:] : 156 -> 152
~ -[DASettingsAccountsUIController localizedAccountTitleString] : 144 -> 128
~ -[DASettingsAccountsUIController deleteAccountButtonTapped] : 176 -> 168
~ -[DASettingsAccountsUIController accountIsManaged] : 184 -> 160
~ -[DASettingsAccountsUIController didSetFullHostURL] : 16 -> 20
~ -[DASettingsAccountsUIController setDidSetFullHostURL:] : 16 -> 20
~ -[DASettingsAccountsUIController needsSave] : 16 -> 20
~ -[DASettingsAccountsUIController setNeedsSave:] : 16 -> 20
~ -[DASettingsAccountsUIController attemptedValidation] : 16 -> 20
~ -[DASettingsAccountsUIController setAttemptedValidation:] : 16 -> 20
~ -[DASettingsAccountsUIController setAccount:] : 80 -> 20
~ -[DASettingsAccountsUIController isSettingUpNewAccount] : 16 -> 20
~ -[DASettingsAccountsUIController setIsSettingUpNewAccount:] : 16 -> 20
~ -[DASettingsAccountsUIController accountNeedsAdd] : 16 -> 20
~ -[DASettingsAccountsUIController setAccountNeedsAdd:] : 16 -> 20
~ -[DASettingsAccountsUIController validatedSuccessfully] : 16 -> 20
~ -[DASettingsAccountsUIController setValidatedSuccessfully:] : 16 -> 20
~ -[DASettingsAccountsUIController confirmedUnvalidatedAccount] : 16 -> 20
~ -[DASettingsAccountsUIController setConfirmedUnvalidatedAccount:] : 16 -> 20
~ -[DASettingsAccountsUIController haveRegisteredForAccountsChanged] : 16 -> 20
~ -[DASettingsAccountsUIController setHaveRegisteredForAccountsChanged:] : 16 -> 20
~ -[DASettingsAccountsUIController transitioningToFinishedAccountSetup] : 16 -> 20
~ -[DASettingsAccountsUIController setTransitioningToFinishedAccountSetup:] : 16 -> 20
~ _DAAccountDescriptionFromHostname : 184 -> 168
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"DAAccount\""
- "@\"NSString\"16@0:8"
- "@\"UIAlertView\""
- "@\"UITextView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24:32@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@56@0:8@16@24:32:40@48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIAlertView\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B48@0:8@16@24@32^@40"
- "DADiagnosticSaveNotesDelegate"
- "DADiagnosticsNotesController"
- "DADiagnosticsNotesPane"
- "DADiagnosticsPSController"
- "DASettingsAccountsUIController"
- "DASettingsAdditions"
- "DASettingsDataclassConfigurationViewController"
- "DAValidityCheckConsumer"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"DAAccount\",&,N,V_account"
- "T@\"DAAccount\",&,N,V_daAccount"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_accountNeedsAdd"
- "TB,N,V_attemptedValidation"
- "TB,N,V_confirmedUnvalidatedAccount"
- "TB,N,V_didSetFullHostURL"
- "TB,N,V_haveRegisteredForAccountsChanged"
- "TB,N,V_isSettingUpNewAccount"
- "TB,N,V_needsSave"
- "TB,N,V_transitioningToFinishedAccountSetup"
- "TB,N,V_validatedSuccessfully"
- "TQ,R"
- "UIActionSheetDelegate"
- "UIAlertViewDelegate"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_account"
- "_accountNeedsAdd"
- "_accountsChanged:"
- "_attemptedValidation"
- "_beginAccountValidation"
- "_cancelButtonPressed"
- "_confirmSaveUnvalidatedAccount"
- "_confirmedUnvalidatedAccount"
- "_daAccount"
- "_defaultAccountDescription"
- "_deleteAccount"
- "_didSetFullHostURL"
- "_disableButtons"
- "_dismissAndUpdateParent"
- "_dismissSavingDataAlert"
- "_enableButtons"
- "_finishSaveAccountDismissWhenDone:"
- "_haveRegisteredForAccountsChanged"
- "_isSettingUpNewAccount"
- "_listenForAccountsChangedNotifications"
- "_navTitle"
- "_needsSave"
- "_notesView"
- "_okButtonPressed"
- "_presentNotesController"
- "_saveAccountDismissWhenDone:"
- "_savingDataAlert"
- "_simpleAlert"
- "_simpleConfirmSheetDismissedSEL"
- "_transitioningToFinishedAccountSetup"
- "_validatedSuccessfully"
- "absoluteString"
- "account"
- "account:isValid:validationError:"
- "accountBooleanPropertyWithSpecifier:"
- "accountDescription"
- "accountDescriptionForFirstTimeSetup"
- "accountFromSpecifier"
- "accountInfoControllerClass"
- "accountIsManaged"
- "accountNeedsAdd"
- "accountOperationsHelper"
- "accountPropertyWithSpecifier:"
- "accountSpecifiers"
- "accountStore"
- "actionSheet:clickedButtonAtIndex:"
- "actionSheet:didDismissWithButtonIndex:"
- "actionSheet:willDismissWithButtonIndex:"
- "actionSheetCancel:"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTask:"
- "alertControllerWithTitle:message:preferredStyle:"
- "alertView:clickedButtonAtIndex:"
- "alertView:didDismissWithButtonIndex:"
- "alertView:willDismissWithButtonIndex:"
- "alertViewCancel:"
- "alertViewShouldEnableFirstOtherButton:"
- "array"
- "arrayWithObjects:count:"
- "attemptedValidation"
- "autorelease"
- "backingAccountInfo"
- "becomeFirstResponder"
- "boolValue"
- "booleanPropertyWithSpecifier:"
- "bundleForClass:"
- "bundleIdentifier"
- "buttonSpecifierWithTitle:target:action:confirmationInfo:"
- "calendarDate"
- "cancelButtonClicked:"
- "cancelButtonTapped:"
- "capitalizedString"
- "class"
- "cleanupAccountFiles"
- "componentsSeparatedByString:"
- "confirmedUnvalidatedAccount"
- "conformsToProtocol:"
- "containsObject:"
- "control"
- "controller:didFinishSettingUpAccount:"
- "copyItemAtPath:toPath:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentDevice"
- "currentHandler"
- "currentlyEditingCell"
- "daAccount"
- "daAccountWithBackingAccountInfo:"
- "daemonAppropriateAccountClassForACAccount:"
- "dealloc"
- "deallocating"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "deleteAccountButtonTapped"
- "description"
- "descriptionWithCalendarFormat:"
- "diagnosticSpecifiers"
- "diagnosticsVisible"
- "didConfirmSaveUnvalidatedAccount:"
- "didConfirmTryWithoutSSL:"
- "didPresentActionSheet:"
- "didPresentAlertView:"
- "didSetFullHostURL"
- "dismiss"
- "dismissAnimated:"
- "dismissViewControllerAnimated:completion:"
- "dismissWithClickedButtonIndex:animated:"
- "dismissesAfterInitialSetup"
- "doneButton"
- "doneButtonTapped:"
- "dumpRuntimeStateSpecifiers"
- "emailAddress"
- "emptyGroupSpecifier"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "finishedAccountSetup"
- "firstResponder"
- "friendlyName"
- "groupSpecifierWithName:"
- "handleClearAllLogsForSpecifier:"
- "handleDumpRuntimeStateForSpecifier:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleSaveAllLogsForSpecifier:"
- "handleSaveAllLogsStep2"
- "hasAccountWithDescription:"
- "hasPrefix:"
- "hash"
- "haveEnoughValues"
- "haveRegisteredForAccountsChanged"
- "hideProgressWithPrompt:"
- "host"
- "i16@0:8"
- "identifier"
- "indexForIndexPath:"
- "indexOfCurrentlyEditingCell"
- "indexPathForCell:"
- "init"
- "initWithBackingAccountInfo:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithFrame:"
- "initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:"
- "initWithTitle:style:target:action:"
- "isEqual:"
- "isEqualToString:"
- "isFirstTimeSetup"
- "isKindOfClass:"
- "isLoggingEnabledForSpecifier:"
- "isMemberOfClass:"
- "isProxy"
- "isRunningFromMobileMailApp"
- "isSettingUpNewAccount"
- "isSuspended"
- "isSuspendedEventsOnly"
- "lastGroupSpecifierInSpecifiers:"
- "lastObject"
- "lastPathComponent"
- "leftBarButtonItem"
- "length"
- "linkSpecifier"
- "loadView"
- "localizedAccountSetupTitleString"
- "localizedAccountTitleString"
- "localizedConfirmSaveUnvalidatedAccountMessageString"
- "localizedConfirmSaveUnvalidatedAccountTitleString"
- "localizedIdenticalAccountFailureMessage"
- "localizedStringForKey:value:table:"
- "localizedValidationFailureTitleString"
- "mainBundle"
- "managingOwnerIdentifier"
- "mcBackingProfile"
- "mutableCopy"
- "navigationController"
- "navigationItem"
- "needsSave"
- "newDefaultAccount"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "operationsHelper:didRemoveAccount:withSuccess:error:"
- "operationsHelper:didSaveAccount:withSuccess:error:"
- "otherSpecifiers"
- "pane"
- "parentController"
- "passwordWithExpected:"
- "pathExtension"
- "pathsOfAllLogFiles"
- "pathsOfPurgableFiles"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferenceValue"
- "presentViewController:animated:completion:"
- "principalURL"
- "properties"
- "propertyForKey:"
- "propertyValueChanged:"
- "purgeFileAtPath:"
- "pushController:"
- "rangeOfString:"
- "release"
- "reload"
- "reloadAccount"
- "reloadParentSpecifier"
- "reloadSpecifierID:"
- "reloadSpecifiers"
- "removeAccount:"
- "removeItemAtPath:error:"
- "removeObject:"
- "removeObserver:"
- "removeObserver:name:object:"
- "removeParentSpecifier"
- "reportActiveExchangeOAuthAccountsCount"
- "resignFirstResponder"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rightBarButtonItem"
- "rootController"
- "runSimpleAlertWithTitle:message:"
- "runSimpleAlertWithTitle:message:dismissedSelector:"
- "saveAccount:requireVerification:"
- "saveFileAtPath:toDirectory:withExtension:error:"
- "saveLogsWithNotes:"
- "saveModifiedPropertiesOnBackingAccount"
- "saveNotesInBackground:"
- "savedLogsDirectoryNameForSpecifier:"
- "self"
- "setAccount:"
- "setAccountBooleanProperty:withSpecifier:"
- "setAccountDescription:"
- "setAccountNeedsAdd:"
- "setAccountProperty:withSpecifier:"
- "setAttemptedValidation:"
- "setAuthenticated:"
- "setAutoresizingMask:"
- "setBooleanProperty:withSpecifier:"
- "setBounces:"
- "setCellsChecked:"
- "setConfirmedUnvalidatedAccount:"
- "setDaAccount:"
- "setDidSetFullHostURL:"
- "setEditable:"
- "setEmailAddress:"
- "setEnabled:"
- "setFont:"
- "setHaveRegisteredForAccountsChanged:"
- "setHost:"
- "setHostString:"
- "setIgnoresInteractionEvents:"
- "setIsSettingUpNewAccount:"
- "setKeyboardType:"
- "setLeftBarButtonItem:"
- "setLoggingEnabled:forSpecifier:"
- "setNeedsSave:"
- "setNeedsSaveAndValidation:"
- "setObject:forKeyedSubscript:"
- "setOn:animated:"
- "setParentController:"
- "setPassword:"
- "setPrincipalURL:"
- "setPrompt:"
- "setProperty:forKey:"
- "setRightBarButtonItem:"
- "setSelectedRange:"
- "setShouldDoInitialAutodiscovery:"
- "setShouldShowDeleteAccountButton:"
- "setSpecifier:"
- "setStatusBarShowsProgress:"
- "setTaskCompletionAssertionEnabled:"
- "setTitle:"
- "setTransitioningToFinishedAccountSetup:"
- "setUseSSL:"
- "setUsername:"
- "setValidatedSuccessfully:"
- "setupWithDictionary:"
- "sharedApplication"
- "sharedInstance"
- "shouldAutorotateToInterfaceOrientation:"
- "shouldVerifyBeforeAccountSave"
- "show"
- "showAlertWithButtons:title:message:completion:"
- "showConfirmationForDeletingAccount:completion:"
- "showConfirmationWithButtons:title:message:destructive:completion:"
- "showIdenticalAccountFailureView"
- "showSSLFailureView"
- "specifier"
- "specifierAtIndex:"
- "specifierForID:"
- "specifiers"
- "stopValidationWithPrompt:showButtons:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringWithFormat:"
- "superclass"
- "superview"
- "suspend"
- "switchSpecifierWithTitle:target:setter:getter:key:"
- "systemFontOfSize:"
- "table"
- "tableView:cellForRowAtIndexPath:"
- "taskFinished:"
- "text"
- "textField"
- "topViewController"
- "transitioningToFinishedAccountSetup"
- "transitionsAfterInitialSetup"
- "updateDoneButton"
- "useSSL"
- "userInfo"
- "userInterfaceIdiom"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIActionSheet\"16"
- "v24@0:8@\"UIAlertView\"16"
- "v24@0:8@16"
- "v28@0:8B16@20"
- "v32@0:8@\"UIActionSheet\"16q24"
- "v32@0:8@\"UIAlertView\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v36@0:8@\"DAAccount\"16B24@\"NSError\"28"
- "v36@0:8@16B24@28"
- "v40@0:8@16@24:32"
- "v44@0:8@16@24B32@36"
- "v48@0:8@16@24@32@?40"
- "validateAccount"
- "validatedSuccessfully"
- "validationInProgress"
- "view"
- "viewControllers"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"
- "willPresentActionSheet:"
- "willPresentAlertView:"
- "window"
- "writeToFile:atomically:encoding:error:"
- "zone"

```
