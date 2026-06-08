## MobileSync

> `/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync`

```diff

-1015.120.3.0.0
-  __TEXT.__text: 0x1538c
-  __TEXT.__auth_stubs: 0x1540
+1023.0.0.0.0
+  __TEXT.__text: 0x153c0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0x7c46
   __TEXT.__const: 0x20
   __TEXT.__unwind_info: 0x2a0
-  __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x6dc
-  __TEXT.__objc_methtype: 0x26
-  __TEXT.__objc_stubs: 0xae0
-  __DATA_CONST.__got: 0x3a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xaa8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x5660
   __AUTH_CONST.__objc_const: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x8
   __DATA.__bss: 0x3d0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5D9DB22A-B847-3F21-808F-AB7AFCF362FB
+  UUID: 9519F961-556E-30DA-B91E-D801AA7BBF58
   Functions: 193
   Symbols:   1007
-  CStrings:  1605
+  CStrings:  1512
 
Functions:
~ _ContactsDataSourceGetSyncTypeAndExchangeSyncAnchors : 1284 -> 1288
~ __reallyCopySetOfEmailAddressesFromMessageFramework : 420 -> 424
~ __AccumulateAlarms : 1044 -> 1052
~ _BookmarksDataSourceGetSyncTypeAndExchangeSyncAnchors : 620 -> 628
~ -[ACAccountStore(SyncPrivate) hasMailAccountsForSync] : 308 -> 312
~ -[ACAccountStore(SyncPrivate) mailAccountsForSync] : 340 -> 344
~ _MailAccountsDataSourceProcessChanges : 424 -> 428
~ _MailAccountsDataSourceCommit : 1324 -> 1328
~ ____bestiCloudUsernameFromEmails_block_invoke_2 : 252 -> 256
~ ____bestiCloudUsernameFromEmails_block_invoke_3 : 564 -> 568
~ __processRecord : 1756 -> 1760
CStrings:
- "@16@0:8"
- "@24@0:8@16"
- "B16@0:8"
- "SyncPrivate"
- "_mailAccountTypeIdentifiers"
- "_usernameFromProperties:"
- "aa_needsRegistration"
- "aa_primaryAppleAccount"
- "aa_setPrimaryAccount:"
- "aa_setPrimaryEmailVerified:"
- "aa_setSyncedAccount:"
- "aa_updatePropertiesForAppleAccount:completion:"
- "absoluteString"
- "accountPropertyForKey:"
- "accountType"
- "accountTypeWithAccountTypeIdentifier:"
- "accountWithAccountTypeIdentifier:error:"
- "accountWithIdentifier:"
- "accounts"
- "addObject:"
- "addObjectsFromArray:"
- "applySyncProperties:"
- "arrayWithObjects:count:"
- "beginSyncTransaction"
- "bookmarksDictionary"
- "boolValue"
- "bundleWithPath:"
- "bytes"
- "commitSyncTransaction"
- "compare:"
- "containsObject:"
- "countByEnumeratingWithState:objects:count:"
- "credential"
- "credentialType"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "emailAddresses"
- "enumerateKeysAndObjectsUsingBlock:"
- "generation"
- "hasMailAccountsForSync"
- "hasPrefix:"
- "hasSuffix:"
- "identifier"
- "initWithAccountType:"
- "initWithPassword:"
- "integerValue"
- "isEqualToString:"
- "isMobileMeAccount"
- "length"
- "load"
- "lowercaseString"
- "mailAccounts"
- "mailAccountsForSync"
- "mergeWithBookmarksDictionary:clearHidden:error:"
- "mutableCopy"
- "numberWithInt:"
- "objectAtIndex:"
- "objectForKey:"
- "parentAccount"
- "password"
- "persistentAccount"
- "rangeOfString:"
- "removeItemAtPath:error:"
- "removeObjectForKey:"
- "rollbackSyncTransaction"
- "safariBookmarkCollection"
- "saveVerifiedAccount:withCompletionHandler:"
- "setAccountDescription:"
- "setAccountProperty:forKey:"
- "setAuthenticated:"
- "setCredential:"
- "setCredentialType:"
- "setEnabled:forDataclass:"
- "setObject:forKey:"
- "setPasswordFromSync:"
- "setProvisioned:forDataclass:"
- "setUsername:"
- "setValue:forKey:"
- "setWithObjects:"
- "sortedArrayUsingComparator:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByExpandingTildeInPath"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportedDataclasses"
- "syncIdentityString"
- "syncSetString:forKey:"
- "syncStringForKey:"
- "username"
- "v24@0:8@16"

```
