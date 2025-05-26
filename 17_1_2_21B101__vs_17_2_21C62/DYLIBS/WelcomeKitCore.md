## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-17.0.1.0.0
-  __TEXT.__text: 0x353ac
+17.2.5.0.0
+  __TEXT.__text: 0x354b0
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x2f8c
+  __TEXT.__objc_methlist: 0x2f44
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0xb162
+  __TEXT.__cstring: 0xb000
   __TEXT.__gcc_except_tab: 0xc54
-  __TEXT.__unwind_info: 0xcb8
-  __TEXT.__objc_classname: 0x59a
-  __TEXT.__objc_methname: 0x87b7
-  __TEXT.__objc_methtype: 0x178c
-  __TEXT.__objc_stubs: 0x7820
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__objc_classname: 0x56d
+  __TEXT.__objc_methname: 0x874d
+  __TEXT.__objc_methtype: 0x1762
+  __TEXT.__objc_stubs: 0x7800
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x1148
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3fb8
-  __DATA_CONST.__objc_selrefs: 0x2038
+  __DATA_CONST.__objc_const: 0x3f28
+  __DATA_CONST.__objc_selrefs: 0x2028
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__objc_const: 0x1930
+  __AUTH_CONST.__objc_const: 0x18e8
   __AUTH_CONST.__cfstring: 0x6b60
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH.__objc_data: 0x1220
-  __DATA.__objc_classrefs: 0x3e0
+  __AUTH.__objc_data: 0x11d0
+  __DATA.__objc_classrefs: 0x3d0
   __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x340
-  __DATA.__data: 0x3d0
+  __DATA.__objc_ivar: 0x344
+  __DATA.__data: 0x370
   __DATA.__bss: 0x138
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1153
-  Symbols:   4553
-  CStrings:  2712
+  Functions: 1147
+  Symbols:   4523
+  CStrings:  2709
 
Symbols:
+ _ACAccountTypeIdentifierGmail
+ _OBJC_CLASS_$_ACAccount
+ _OBJC_IVAR_$_WLMailAccountMigrator._accountTypes
+ _OBJC_IVAR_$_WLMailAccountMigrator._existingAccounts
+ _objc_msgSend$accountTypeWithAccountTypeIdentifier:
+ _objc_msgSend$accountsWithAccountType:
+ _objc_msgSend$initWithAccountType:
+ _objc_msgSend$saveVerifiedAccount:error:
+ _objc_msgSend$setAccountDescription:
+ _objc_msgSend$setEnabled:forDataclass:
+ _objc_msgSend$setProvisioned:forDataclass:
+ _objc_msgSend$setUsername:
+ _objc_msgSend$supportedDataclasses
- -[WLMFAccountValidator .cxx_destruct]
- -[WLMFAccountValidator completion]
- -[WLMFAccountValidator setCompletion:]
- -[WLMailAccountMigrator _importGoogleAccountWithUsername:completion:]
- -[WLMailAccountMigrator accountValidator:finishedValidationOfAccount:usedSSL:]
- _MFMailAccountDescription
- _MFMailAccountUsername
- _MFOAuth2RefreshToken
- _MFOAuth2Token
- _OBJC_CLASS_$_GmailAccount
- _OBJC_CLASS_$_MFAccountValidator
- _OBJC_CLASS_$_MailAccount
- _OBJC_CLASS_$_WLMFAccountValidator
- _OBJC_IVAR_$_WLMFAccountValidator._completion
- _OBJC_METACLASS_$_MFAccountValidator
- _OBJC_METACLASS_$_WLMFAccountValidator
- __OBJC_$_INSTANCE_METHODS_WLMFAccountValidator
- __OBJC_$_INSTANCE_VARIABLES_WLMFAccountValidator
- __OBJC_$_PROP_LIST_WLMFAccountValidator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MFAccountValidatorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MFAccountValidatorDelegate
- __OBJC_$_PROTOCOL_REFS_MFAccountValidatorDelegate
- __OBJC_CLASS_RO_$_WLMFAccountValidator
- __OBJC_LABEL_PROTOCOL_$_MFAccountValidatorDelegate
- __OBJC_METACLASS_RO_$_WLMFAccountValidator
- __OBJC_PROTOCOL_$_MFAccountValidatorDelegate
- ___78-[WLMailAccountMigrator accountValidator:finishedValidationOfAccount:usedSSL:]_block_invoke
- _objc_msgSend$_importGoogleAccountWithUsername:completion:
- _objc_msgSend$displayedAccountTypeString
- _objc_msgSend$existingAccountWithType:hostname:username:
- _objc_msgSend$hasAccountWithDescription:
- _objc_msgSend$hostname
- _objc_msgSend$newAccountWithDictionary:
- _objc_msgSend$persistentAccount
- _objc_msgSend$saveAccount:withDataclassActions:doVerify:completion:
- _objc_msgSend$setCompletion:
- _objc_msgSend$validateAccount:useSSL:
CStrings:
+ "\x02\x11"
+ "%@ account already exists. type=%@, name=%@"
+ "%@ account store did store an account. error=%@"
+ "%@ received an account. type=%@, name=%@"
+ "%@ will import an account."
+ "%@ will skip an account. type=%@"
+ "@\"NSMutableDictionary\""
+ "WLAccountErrorDomain"
+ "_accountTypes"
+ "_existingAccounts"
+ "accountTypeWithAccountTypeIdentifier:"
+ "accountsWithAccountType:"
+ "cannot continue to import an account due to an ACAccountStore error."
+ "initWithAccountType:"
+ "invalid argument"
+ "saveVerifiedAccount:error:"
+ "setAccountDescription:"
+ "setEnabled:forDataclass:"
+ "setProvisioned:forDataclass:"
+ "setUsername:"
+ "supportedDataclasses"
- "%@ importRecordData:summary:account:completion: ignoring account of type %@ with username %@"
- "%@ importRecordData:summary:account:completion: will import account of type %@ with username %@"
- "%@: _importGoogleAccountWithUsername: %@ did save ACAccount with success %@ error %@"
- "%@: _importGoogleAccountWithUsername: %@ did validate mail account"
- "%@: _importGoogleAccountWithUsername: %@ skipping import because MailAccount with that username already exists"
- "%@: _importGoogleAccountWithUsername: %@ will save ACAccount"
- "%@: _importGoogleAccountWithUsername: %@ will validate mail account"
- "%@: import failed because accountsd could not initialize ACAccountStore."
- "MFAccountValidatorDelegate"
- "T@?,C,N,V_completion"
- "WLMFAccountValidator"
- "_importGoogleAccountWithUsername:completion:"
- "accountValidator:finishedValidationOfAccount:usedSSL:"
- "displayedAccountTypeString"
- "existingAccountWithType:hostname:username:"
- "hasAccountWithDescription:"
- "hostname"
- "newAccountWithDictionary:"
- "persistentAccount"
- "saveAccount:withDataclassActions:doVerify:completion:"
- "setCompletion:"
- "v36@0:8@\"MFAccountValidator\"16@\"MFAccount\"24B32"
- "v36@0:8@16@24B32"
- "validateAccount:useSSL:"

```
