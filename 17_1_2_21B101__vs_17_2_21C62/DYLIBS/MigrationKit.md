## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-17.0.1.0.0
-  __TEXT.__text: 0x30358
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x3434
+17.2.5.0.0
+  __TEXT.__text: 0x301a4
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x343c
   __TEXT.__const: 0x44c
-  __TEXT.__cstring: 0x2fb5
-  __TEXT.__oslogstring: 0x23da
-  __TEXT.__gcc_except_tab: 0xc84
-  __TEXT.__unwind_info: 0xce0
+  __TEXT.__cstring: 0x3011
+  __TEXT.__oslogstring: 0x2345
+  __TEXT.__gcc_except_tab: 0xc24
+  __TEXT.__unwind_info: 0xcd0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x820
-  __TEXT.__objc_methname: 0x6ec4
-  __TEXT.__objc_methtype: 0xfaf
-  __TEXT.__objc_stubs: 0x6da0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x5e8
+  __TEXT.__objc_classname: 0x803
+  __TEXT.__objc_methname: 0x6ea0
+  __TEXT.__objc_methtype: 0xf58
+  __TEXT.__objc_stubs: 0x6de0
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6b60
-  __DATA_CONST.__objc_selrefs: 0x1dc8
+  __DATA_CONST.__objc_const: 0x6a48
+  __DATA_CONST.__objc_selrefs: 0x1dd8
   __DATA_CONST.__objc_arraydata: 0x480
   __AUTH_CONST.__objc_intobj: 0xc00
-  __AUTH_CONST.__cfstring: 0x44e0
-  __AUTH_CONST.__objc_const: 0x1e50
+  __AUTH_CONST.__cfstring: 0x4520
+  __AUTH_CONST.__objc_const: 0x1e98
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x610
   __AUTH.__objc_data: 0x1f40
-  __DATA.__objc_classrefs: 0x518
+  __DATA.__objc_classrefs: 0x508
   __DATA.__objc_superrefs: 0x250
-  __DATA.__objc_ivar: 0x580
-  __DATA.__data: 0x5a0
+  __DATA.__objc_ivar: 0x578
+  __DATA.__data: 0x540
   __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
-  - /System/Library/PrivateFrameworks/Message.framework/Message
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A99ED3C7-9B51-3977-9B66-188CDE37C591
-  Functions: 1335
-  Symbols:   5201
-  CStrings:  3195
+  UUID: 6D22C982-D38D-3866-8D46-E72790F2C1CA
+  Functions: 1332
+  Symbols:   5181
+  CStrings:  3194
 
Symbols:
+ +[MKSRPServer generateRandomPassword]
+ -[MKCrypto setUseCFB8Mode:]
+ -[MKCrypto useCFB8Mode]
+ -[MKSRPServer initWithUsername:password:]
+ _ACAccountTypeIdentifierGmail
+ _OBJC_CLASS_$_ACAccount
+ _OBJC_IVAR_$_MKAccountMigrator._accountTypes
+ _OBJC_IVAR_$_MKAccountMigrator._existingAccounts
+ _OBJC_IVAR_$_MKCrypto._useCFB8Mode
+ __OBJC_$_CLASS_METHODS_MKSRPServer
+ _objc_msgSend$accountTypeWithAccountTypeIdentifier:
+ _objc_msgSend$accountsWithAccountType:
+ _objc_msgSend$initWithAccountType:
+ _objc_msgSend$initWithUsername:password:
+ _objc_msgSend$saveVerifiedAccount:error:
+ _objc_msgSend$setAccountDescription:
+ _objc_msgSend$setEnabled:forDataclass:
+ _objc_msgSend$setProvisioned:forDataclass:
+ _objc_msgSend$supportedDataclasses
+ _objc_msgSend$useCFB8Mode
- -[MKAccountMigrator accountStoreDidImportAccount:success:error:]
- -[MKAccountMigrator accountValidator:finishedValidationOfAccount:usedSSL:]
- -[MKAccountMigrator import:].cold.1
- -[MKAccountMigrator import:].cold.2
- -[MKAccountMigrator import]
- -[MKSRPServer generateRandomPassword]
- _MFMailAccountDescription
- _MFMailAccountUsername
- _MFOAuth2RefreshToken
- _MFOAuth2Token
- _NSStringFromClass
- _OBJC_CLASS_$_GmailAccount
- _OBJC_CLASS_$_MFAccountValidator
- _OBJC_CLASS_$_MailAccount
- _OBJC_IVAR_$_MKAccountMigrator._accountValidator
- _OBJC_IVAR_$_MKAccountMigrator._completedOperationCount
- _OBJC_IVAR_$_MKAccountMigrator._isImporting
- _OBJC_IVAR_$_MKAccountMigrator._startDatesByAccountName
- _OBJC_IVAR_$_MKAccountMigrator._totalOperationCount
- __OBJC_$_PROP_LIST_MKAccountMigrator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MFAccountValidatorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MFAccountValidatorDelegate
- __OBJC_$_PROTOCOL_REFS_MFAccountValidatorDelegate
- __OBJC_CLASS_PROTOCOLS_$_MKAccountMigrator
- __OBJC_LABEL_PROTOCOL_$_MFAccountValidatorDelegate
- __OBJC_PROTOCOL_$_MFAccountValidatorDelegate
- ___74-[MKAccountMigrator accountValidator:finishedValidationOfAccount:usedSSL:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
- _objc_msgSend$accountStoreDidImportAccount:success:error:
- _objc_msgSend$displayedAccountTypeString
- _objc_msgSend$existingAccountWithType:hostname:username:
- _objc_msgSend$hasAccountWithDescription:
- _objc_msgSend$newAccountWithDictionary:
- _objc_msgSend$persistentAccount
- _objc_msgSend$saveAccount:withDataclassActions:doVerify:completion:
- _objc_msgSend$validateAccount:useSSL:
CStrings:
+ "%@ account already exists. type=%@, name=%@"
+ "%@ account store did store an account. error=%@"
+ "%@ received an account. type=%@, name=%@"
+ "MKAccountErrorDomain"
+ "TB,V_useCFB8Mode"
+ "_accountTypes"
+ "_existingAccounts"
+ "_useCFB8Mode"
+ "accountTypeWithAccountTypeIdentifier:"
+ "accountsWithAccountType:"
+ "initWithAccountType:"
+ "initWithUsername:password:"
+ "invalid argument"
+ "saveVerifiedAccount:error:"
+ "setAccountDescription:"
+ "setEnabled:forDataclass:"
+ "setProvisioned:forDataclass:"
+ "setUseCFB8Mode:"
+ "supportedDataclasses"
+ "useCFB8Mode"
- "%@ account is missing."
- "%@ account validator will verify an account. type=%@"
- "%@ did import an account."
- "%@ did receive an event from account validator."
- "%@ found the existing account."
- "%@ received an account. type=%@"
- "3"
- "@\"MFAccountValidator\""
- "MFAccountValidatorDelegate"
- "MKAccountError"
- "_accountValidator"
- "_startDatesByAccountName"
- "accountStoreDidImportAccount:success:error:"
- "accountValidator:finishedValidationOfAccount:usedSSL:"
- "displayedAccountTypeString"
- "existingAccountWithType:hostname:username:"
- "hasAccountWithDescription:"
- "newAccountWithDictionary:"
- "persistentAccount"
- "saveAccount:withDataclassActions:doVerify:completion:"
- "v36@0:8@\"MFAccountValidator\"16@\"MFAccount\"24B32"
- "v36@0:8@16B24@28"
- "validateAccount:useSSL:"

```
