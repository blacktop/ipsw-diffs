## AccountsUI

> `/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI`

```diff

-331.1.0.0.0
-  __TEXT.__text: 0x3b918
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x148c
-  __TEXT.__cstring: 0x2929
-  __TEXT.__gcc_except_tab: 0x55c
+339.1.0.0.0
+  __TEXT.__text: 0x3d7b4
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x153c
+  __TEXT.__cstring: 0x2a55
+  __TEXT.__gcc_except_tab: 0x580
   __TEXT.__const: 0x38
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__oslogstring: 0x14cc
+  __TEXT.__oslogstring: 0x1553
   __TEXT.__ustring: 0x10
   __TEXT.__objc_const_ax: 0x180
-  __TEXT.__unwind_info: 0x50c
-  __TEXT.__objc_classname: 0x475
-  __TEXT.__objc_methname: 0x625e
-  __TEXT.__objc_methtype: 0x1043
-  __TEXT.__objc_stubs: 0x5600
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0x9f8
+  __TEXT.__unwind_info: 0x52c
+  __TEXT.__objc_classname: 0x489
+  __TEXT.__objc_methname: 0x6730
+  __TEXT.__objc_methtype: 0x1176
+  __TEXT.__objc_stubs: 0x58a0
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0xa48
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3890
-  __DATA_CONST.__objc_selrefs: 0x1910
+  __DATA_CONST.__objc_const: 0x3e00
+  __DATA_CONST.__objc_selrefs: 0x19d8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__cfstring: 0x2140
   __AUTH_CONST.__objc_const: 0xa58
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x2e0
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x6a0
+  __DATA.__data: 0x700
   __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70D930A8-3A2B-350A-BDB9-0F8BAE60A46A
-  Functions: 591
-  Symbols:   2778
-  CStrings:  1885
+  UUID: 3E19CFEE-8C05-3B7E-BEEF-C3DA946F70F0
+  Functions: 610
+  Symbols:   2860
+  CStrings:  1961
 
Symbols:
+ -[ACUIAddAccountViewController _allowedToAddAccountTypeID:fromSpecifier:]
+ -[ACUIDataclassConfigurationViewController _getDescription:]
+ -[ACUIDataclassConfigurationViewController _setDescription:]
+ -[ACUIDataclassConfigurationViewController _textFieldValueDidChange:]
+ -[ACUIDataclassConfigurationViewController _updateDoneButton]
+ -[ACUIDataclassConfigurationViewController dataclassLinkListStateForSpecifier:]
+ -[ACUIDataclassConfigurationViewController dataclassStateForSpecifier:]
+ -[ACUIDataclassConfigurationViewController dealloc]
+ -[ACUIDataclassConfigurationViewController isAccountDataclassListRedesignFFEnabled]
+ -[ACUIDataclassConfigurationViewController setShouldEnableAccountSettingsCell:]
+ -[ACUIDataclassConfigurationViewController shouldEnableAccountSettingsCell]
+ -[ACUIDataclassConfigurationViewController specifierForAccountSettingsCell]
+ -[ACUIDataclassConfigurationViewController tableView:cellForRowAtIndexPath:]
+ -[ACUIDataclassConfigurationViewController textFieldShouldReturn:]
+ -[ACUIDataclassConfigurationViewController viewWillDisappear:]
+ GCC_except_table101
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table92
+ GCC_except_table95
+ GCC_except_table98
+ _LARatchetErrorUserInfoKeyState
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_PSTextFieldSpecifier
+ _OBJC_IVAR_$_ACUIDataclassConfigurationViewController._accountSettingsCellSpecifier
+ _OBJC_IVAR_$_ACUIDataclassConfigurationViewController._initialAccountDescription
+ _OBJC_IVAR_$_ACUIDataclassConfigurationViewController._shouldEnableAccountSettingsCell
+ _OBJC_IVAR_$_ACUIDataclassConfigurationViewController._textFieldTextDidChangeObserver
+ _UITextFieldTextDidChangeNotification
+ __ACLogSystem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UITextFieldDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITextFieldDelegate
+ __OBJC_$_PROTOCOL_REFS_UITextFieldDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ACUIDataclassConfigurationViewController
+ __OBJC_LABEL_PROTOCOL_$_UITextFieldDelegate
+ __OBJC_PROTOCOL_$_UITextFieldDelegate
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.129
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.131
+ ___62-[ACUIDataclassConfigurationViewController viewWillDisappear:]_block_invoke
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.177
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.178
+ ___76-[ACUIDataclassConfigurationViewController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___87-[ACUIDataclassConfigurationViewController _setDataclass:enabled:onAccount:completion:]_block_invoke.136
+ ___assert_rtn
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_descriptor_56_e8_32s40s48s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.342
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_2_1_8_64
+ __unnamed_array_storage.240
+ _objc_msgSend$_allowedToAddAccountTypeID:fromSpecifier:
+ _objc_msgSend$_setDescription:
+ _objc_msgSend$_textFieldValueDidChange:
+ _objc_msgSend$_updateDoneButton
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$armWithOptions:completion:
+ _objc_msgSend$code
+ _objc_msgSend$dataclassStateForSpecifier:
+ _objc_msgSend$groupSpecifierWithID:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$isAccountDataclassListRedesignFFEnabled
+ _objc_msgSend$isEditing
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$resignFirstResponder
+ _objc_msgSend$saveAccount:withCompletionHandler:
+ _objc_msgSend$setAccountDescription:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setKeyboardType:autoCaps:autoCorrection:
+ _objc_msgSend$setShouldEnableAccountSettingsCell:
+ _objc_msgSend$shouldEnableAccountSettingsCell
+ _objc_msgSend$specifierForAccountSettingsCell
+ _objc_msgSend$textField
- GCC_except_table28
- GCC_except_table38
- GCC_except_table40
- GCC_except_table45
- GCC_except_table67
- GCC_except_table71
- GCC_except_table74
- GCC_except_table86
- GCC_except_table89
- ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.116
- ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke_2
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.160
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.161
- ___87-[ACUIDataclassConfigurationViewController _setDataclass:enabled:onAccount:completion:]_block_invoke.105
- ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
- ___block_literal_global.105
- ___block_literal_global.112
- ___block_literal_global.319
- __unnamed_array_storage.209
- _objc_msgSend$openURL:withCompletionHandler:
CStrings:
+ "\x12\x15\x13\x14"
+ "%s (%d) \"Account did not save\""
+ "%s (%d) \"Error occurred while saving account. Error: %@\""
+ "-[ACUIAddAccountViewController _allowedToAddAccountTypeID:fromSpecifier:]"
+ "-[ACUIDataclassConfigurationViewController dataclassStateForSpecifier:]"
+ "-[ACUIDataclassConfigurationViewController viewWillDisappear:]_block_invoke"
+ "@\"Ratchet armed! Showing the exchange account login flow\""
+ "@\"Ratchet not armed. Reason: %@\""
+ "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
+ "@48@0:8@16{_NSRange=QQ}24@40"
+ "ACCOUNT_SETTINGS"
+ "ACUIAddAccountViewController.m"
+ "AccountDataclassListRedesign"
+ "AppleAccountUI"
+ "B24@0:8@\"UITextField\"16"
+ "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
+ "B48@0:8@16{_NSRange=QQ}24@40"
+ "EXCHANGE_DTO_LOCALIZED_CALLOUT"
+ "EXCHANGE_DTO_LOCALIZED_REASON"
+ "EXCHANGE_DTO_RATCHET_COUNTDOWN_TEXT"
+ "EXCHANGE_DTO_RATCHET_TEXT"
+ "EXCHANGE_DTO_RATCHET_TITLE"
+ "ON"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIBarButtonItem\",&,N"
+ "TB,N,V_shouldEnableAccountSettingsCell"
+ "UITextFieldDelegate"
+ "_accountSettingsCellSpecifier"
+ "_allowedToAddAccountTypeID:fromSpecifier:"
+ "_getDescription:"
+ "_initialAccountDescription"
+ "_setDescription:"
+ "_shouldEnableAccountSettingsCell"
+ "_textFieldTextDidChangeObserver"
+ "_textFieldValueDidChange:"
+ "_updateDoneButton"
+ "accountSettingsSpecifier"
+ "addObserverForName:object:queue:usingBlock:"
+ "armWithOptions:completion:"
+ "code"
+ "com.apple.account.Exchange.add"
+ "dataclassLinkListStateForSpecifier:"
+ "dataclassStateForSpecifier:"
+ "groupSpecifierWithID:"
+ "initWithIdentifier:"
+ "isAccountDataclassListRedesignFFEnabled"
+ "isEditing"
+ "prefs:root=ACCOUNTS_AND_PASSWORDS"
+ "removeObserver:name:object:"
+ "resignFirstResponder"
+ "result != nil || error != nil"
+ "saveAccount:withCompletionHandler:"
+ "setAccountDescription:"
+ "setHidden:"
+ "setKeyboardType:autoCaps:autoCorrection:"
+ "setShouldEnableAccountSettingsCell:"
+ "shouldEnableAccountSettingsCell"
+ "specifierForAccountSettingsCell"
+ "textField"
+ "textField:editMenuForCharactersInRange:suggestedActions:"
+ "textField:shouldChangeCharactersInRange:replacementString:"
+ "textField:willDismissEditMenuWithAnimator:"
+ "textField:willPresentEditMenuWithAnimator:"
+ "textFieldDidBeginEditing:"
+ "textFieldDidChangeSelection:"
+ "textFieldDidEndEditing:"
+ "textFieldDidEndEditing:reason:"
+ "textFieldShouldBeginEditing:"
+ "textFieldShouldClear:"
+ "textFieldShouldEndEditing:"
+ "textFieldShouldReturn:"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8@\"UITextField\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
+ "v32@0:8@\"UITextField\"16q24"
+ "viewWillDisappear:"
- "\x12\x14\x11\x14"
- "%s (%d) \"DTO: Failed to open support link.\""
- "-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke_2"
- "-[ACUIDataclassConfigurationViewController dataclassSwitchStateForSpecifier:]"
- "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_LEARN_MORE_ACTION_TITLE"
- "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_MESSAGE"
- "DTO_ENABLED_ADD_EXCHANGE_ACCOUNT_ALERT_TITLE"
- "https://support.apple.com/kb/HT212510"
- "openURL:withCompletionHandler:"

```
