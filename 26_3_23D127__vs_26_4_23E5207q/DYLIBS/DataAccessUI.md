## DataAccessUI

> `/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0x5a08
-  __TEXT.__auth_stubs: 0x380
+2691.4.5.0.0
+  __TEXT.__text: 0x5f3c
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x87c
   __TEXT.__cstring: 0x3c1
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x70
+  __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x282
-  __TEXT.__unwind_info: 0x200
+  __TEXT.__unwind_info: 0x218
   __TEXT.__objc_classname: 0x11d
   __TEXT.__objc_methname: 0x1ebc
   __TEXT.__objc_methtype: 0x2c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9f8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__objc_const: 0xc40

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 522025F9-3E4B-3063-B9CB-1FE8EE5CC32E
+  UUID: FDB6A11A-CD26-3316-A7B5-B642DF926377
   Functions: 147
-  Symbols:   750
+  Symbols:   743
   CStrings:  520
 
Symbols:
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ -[DASettingsDataclassConfigurationViewController dealloc] : 116 -> 120
~ -[DASettingsDataclassConfigurationViewController accountDescriptionForFirstTimeSetup] : 76 -> 84
~ -[DASettingsDataclassConfigurationViewController _navTitle] : 112 -> 124
~ -[DASettingsDataclassConfigurationViewController loadView] : 124 -> 132
~ -[DASettingsDataclassConfigurationViewController viewDidLoad] : 120 -> 128
~ -[DASettingsDataclassConfigurationViewController viewWillDisappear:] : 144 -> 148
~ -[DASettingsDataclassConfigurationViewController _listenForAccountsChangedNotifications] : 140 -> 144
~ -[DASettingsDataclassConfigurationViewController viewWillAppear:] : 128 -> 136
~ -[DASettingsDataclassConfigurationViewController daAccount] : 92 -> 108
~ -[DASettingsDataclassConfigurationViewController reloadAccount] : 120 -> 132
~ -[DASettingsDataclassConfigurationViewController accountFromSpecifier] : 296 -> 320
~ -[DASettingsDataclassConfigurationViewController specifiers] : 92 -> 96
~ -[DASettingsDataclassConfigurationViewController otherSpecifiers] : 352 -> 384
~ -[DASettingsDataclassConfigurationViewController accountInfoControllerClass] : 144 -> 152
~ -[DASettingsDataclassConfigurationViewController operationsHelper:didRemoveAccount:withSuccess:error:] : 176 -> 172
~ -[DASettingsDataclassConfigurationViewController cancelButtonClicked:] : 84 -> 88
~ -[DASettingsDataclassConfigurationViewController setDaAccount:] : 20 -> 80
~ +[PSSpecifier(DASettingsAdditions) switchSpecifierWithTitle:target:setter:getter:key:] : 176 -> 180
~ +[PSSpecifier(DASettingsAdditions) buttonSpecifierWithTitle:target:action:confirmationInfo:] : 224 -> 220
~ +[DADiagnosticsPSController linkSpecifier] : 232 -> 244
~ +[DADiagnosticsPSController dumpRuntimeStateSpecifiers] : 272 -> 292
~ -[DADiagnosticsPSController diagnosticSpecifiers] : 128 -> 140
~ -[DADiagnosticsPSController specifiers] : 316 -> 328
~ -[DADiagnosticsPSController runSimpleAlertWithTitle:message:dismissedSelector:] : 308 -> 312
~ -[DADiagnosticsPSController setBooleanProperty:withSpecifier:] : 144 -> 152
~ -[DADiagnosticsPSController booleanPropertyWithSpecifier:] : 148 -> 160
~ -[DADiagnosticsPSController saveFileAtPath:toDirectory:withExtension:error:] : 352 -> 368
~ -[DADiagnosticsPSController saveLogsWithNotes:] : 864 -> 896
~ _validPathsForPaths : 360 -> 376
~ ___47-[DADiagnosticsPSController saveLogsWithNotes:]_block_invoke : 324 -> 348
~ -[DADiagnosticsPSController _presentNotesController] : 428 -> 444
~ -[DADiagnosticsPSController handleSaveAllLogsStep2] : 312 -> 336
~ -[DADiagnosticsPSController _dismissSavingDataAlert] : 128 -> 132
~ -[DADiagnosticsPSController handleSaveAllLogsForSpecifier:] : 488 -> 516
~ -[DADiagnosticsPSController suspend] : 124 -> 128
~ -[DADiagnosticsPSController handleClearAllLogsForSpecifier:] : 244 -> 248
~ -[DADiagnosticsPSController purgeFileAtPath:] : 156 -> 172
~ -[DADiagnosticsNotesController _disableButtons] : 200 -> 224
~ -[DADiagnosticsNotesController _enableButtons] : 176 -> 196
~ -[DADiagnosticsNotesController _cancelButtonPressed] : 64 -> 68
~ -[DADiagnosticsNotesController _okButtonPressed] : 276 -> 288
~ ___48-[DADiagnosticsNotesController _okButtonPressed]_block_invoke_2 : 88 -> 92
~ -[DADiagnosticsNotesController init] : 480 -> 508
~ -[DADiagnosticsNotesController viewWillAppear:] : 92 -> 96
~ -[DADiagnosticsNotesController shouldAutorotateToInterfaceOrientation:] : 88 -> 92
~ -[DADiagnosticsNotesPane initWithFrame:] : 288 -> 292
~ -[DASettingsAccountsUIController account] : 456 -> 492
~ -[DASettingsAccountsUIController reloadAccount] : 120 -> 132
~ -[DASettingsAccountsUIController accountFromSpecifier] : 184 -> 200
~ -[DASettingsAccountsUIController daAccountWithBackingAccountInfo:] : 124 -> 128
~ -[DASettingsAccountsUIController newDefaultAccount] : 124 -> 128
~ -[DASettingsAccountsUIController specifiers] : 172 -> 196
~ -[DASettingsAccountsUIController tableView:cellForRowAtIndexPath:] : 364 -> 388
~ -[DASettingsAccountsUIController showAlertWithButtons:title:message:completion:] : 524 -> 520
~ -[DASettingsAccountsUIController validateAccount] : 124 -> 128
~ -[DASettingsAccountsUIController showIdenticalAccountFailureView] : 368 -> 396
~ -[DASettingsAccountsUIController showSSLFailureView] : 556 -> 592
~ -[DASettingsAccountsUIController didConfirmTryWithoutSSL:] : 304 -> 332
~ -[DASettingsAccountsUIController didConfirmSaveUnvalidatedAccount:] : 112 -> 116
~ -[DASettingsAccountsUIController _confirmSaveUnvalidatedAccount] : 448 -> 476
~ -[DASettingsAccountsUIController account:isValid:validationError:] : 184 -> 188
~ -[DASettingsAccountsUIController finishedAccountSetup] : 360 -> 376
~ -[DASettingsAccountsUIController doneButtonTapped:] : 260 -> 268
~ -[DASettingsAccountsUIController cancelButtonTapped:] : 148 -> 160
~ -[DASettingsAccountsUIController updateDoneButton] : 344 -> 364
~ -[DASettingsAccountsUIController haveEnoughValues] : 124 -> 128
~ -[DASettingsAccountsUIController setHostString:] : 768 -> 808
~ -[DASettingsAccountsUIController setAccountProperty:withSpecifier:] : 788 -> 856
~ -[DASettingsAccountsUIController accountPropertyWithSpecifier:] : 392 -> 456
~ -[DASettingsAccountsUIController setAccountBooleanProperty:withSpecifier:] : 176 -> 184
~ -[DASettingsAccountsUIController accountBooleanPropertyWithSpecifier:] : 156 -> 168
~ -[DASettingsAccountsUIController _deleteAccount] : 208 -> 224
~ -[DASettingsAccountsUIController operationsHelper:didRemoveAccount:withSuccess:error:] : 268 -> 260
~ ___86-[DASettingsAccountsUIController operationsHelper:didRemoveAccount:withSuccess:error:]_block_invoke : 236 -> 240
~ -[DASettingsAccountsUIController _finishSaveAccountDismissWhenDone:] : 264 -> 280
~ -[DASettingsAccountsUIController _saveAccountDismissWhenDone:] : 244 -> 264
~ -[DASettingsAccountsUIController operationsHelper:didSaveAccount:withSuccess:error:] : 268 -> 260
~ ___84-[DASettingsAccountsUIController operationsHelper:didSaveAccount:withSuccess:error:]_block_invoke : 276 -> 280
~ -[DASettingsAccountsUIController isRunningFromMobileMailApp] : 96 -> 104
~ -[DASettingsAccountsUIController hideProgressWithPrompt:] : 388 -> 412
~ -[DASettingsAccountsUIController dealloc] : 100 -> 104
~ -[DASettingsAccountsUIController viewWillDisappear:] : 292 -> 312
~ -[DASettingsAccountsUIController indexOfCurrentlyEditingCell] : 128 -> 136
~ -[DASettingsAccountsUIController currentlyEditingCell] : 220 -> 232
~ -[DASettingsAccountsUIController lastGroupSpecifierInSpecifiers:] : 148 -> 156
~ -[DASettingsAccountsUIController localizedAccountTitleString] : 128 -> 144
~ -[DASettingsAccountsUIController deleteAccountButtonTapped] : 168 -> 176
~ -[DASettingsAccountsUIController accountIsManaged] : 160 -> 184
~ -[DASettingsAccountsUIController setAccount:] : 20 -> 80
~ _DAAccountDescriptionFromHostname : 168 -> 184

```
