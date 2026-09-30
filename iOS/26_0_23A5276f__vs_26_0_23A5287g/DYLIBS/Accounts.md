## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-1016.0.0.0.0
-  __TEXT.__text: 0x5c968
+1018.0.0.0.0
+  __TEXT.__text: 0x5c9d8
   __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x42ec
+  __TEXT.__objc_methlist: 0x42dc
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3ee8
-  __TEXT.__cstring: 0x3ca9
-  __TEXT.__oslogstring: 0x5245
-  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__gcc_except_tab: 0x3ed0
+  __TEXT.__cstring: 0x3ca5
+  __TEXT.__oslogstring: 0x52b5
+  __TEXT.__unwind_info: 0x1a78
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x8996
+  __TEXT.__objc_methname: 0x8997
   __TEXT.__objc_methtype: 0x1523
   __TEXT.__objc_stubs: 0x6560
   __DATA_CONST.__got: 0x340

   __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x4880
-  __AUTH_CONST.__objc_const: 0x5e60
+  __AUTH_CONST.__objc_const: 0x5e40
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3e4
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x109
   __DATA_DIRTY.__objc_data: 0x730

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B59E5F9C-3C35-39C3-9676-05E5C77A84E4
-  Functions: 1960
-  Symbols:   6761
-  CStrings:  3430
+  UUID: 08727E04-C2CE-348C-8DB8-FB3B86D221E9
+  Functions: 1959
+  Symbols:   6757
+  CStrings:  3432
 
Symbols:
+ -[ACAccountStore credentialForAccount:error:].cold.2
+ -[ACCredentialCache _handleKeybagFirstUnlocked]
+ ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke.219
+ ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke_2.220
+ ___28-[ACAccountStore handleURL:]_block_invoke.252
+ ___28-[ACAccountStore handleURL:]_block_invoke.252.cold.1
+ ___28-[ACAccountStore handleURL:]_block_invoke.252.cold.2
+ ___36-[ACAccountStore shutdownAccountsD:]_block_invoke.258
+ ___36-[ACAccountStore shutdownAccountsD:]_block_invoke_2.259
+ ___41-[ACAccountStore removeObsoleteAccounts:]_block_invoke.235
+ ___45-[ACAccountStore credentialForAccount:error:]_block_invoke.170
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.253
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.255
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.254
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.254.cold.1
+ ___48-[ACAccountStore childAccountsForAccount:error:]_block_invoke.186
+ ___48-[ACAccountStore parentAccountForAccount:error:]_block_invoke.185
+ ___53-[ACAccountStore enabledDataclassesForAccount:error:]_block_invoke.190
+ ___54-[ACAccountStore triggerKeychainMigrationIfNecessary:]_block_invoke.232
+ ___55-[ACAccountStore credentialForAccount:serviceID:error:]_block_invoke.171
+ ___55-[ACAccountStore dataclassActionsForAccountSave:error:]_block_invoke.194
+ ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke.192
+ ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke_2.193
+ ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke.256
+ ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke_2.257
+ ___57-[ACAccountStore provisionedDataclassesForAccount:error:]_block_invoke.191
+ ___59-[ACAccountStore dataclassActionsForAccountDeletion:error:]_block_invoke.195
+ ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke.183
+ ___59-[ACAccountStore setCredential:forAccount:serviceID:error:]_block_invoke.173
+ ___61-[ACAccountStore _removeObsoleteAccountsInternal:completion:]_block_invoke.237
+ ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke.181
+ ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2.182
+ ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke.184
+ ___63-[ACAccountStore isPerformingDataclassActionsForAccount:error:]_block_invoke.196
+ ___66-[ACAccountStore discoverPropertiesForAccount:options:completion:]_block_invoke.206
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.223
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.225
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.224
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.224.cold.1
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.229
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.231
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.230
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.230.cold.1
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.226
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.228
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.227
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.227.cold.1
+ ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke.210
+ ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke_2.211
+ ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.221
+ ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.221.cold.1
+ ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.222
+ ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.222.cold.1
+ ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke.204
+ ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke_2.205
+ ___block_descriptor_72_e8_32s40s48s56s64r_e40_v16?0"<ACRemoteAccountStoreProtocol>"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.234
+ ___block_literal_global.262
+ _objc_msgSend$_handleKeybagFirstUnlocked
- -[ACCredentialCache _handleKeyagFirstUnlocked]
- -[ACCredentialCache dealloc]
- _OBJC_IVAR_$_ACCredentialCache._credentialsDidChangeObserver
- ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke.220
- ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke_2.221
- ___28-[ACAccountStore handleURL:]_block_invoke.253
- ___28-[ACAccountStore handleURL:]_block_invoke.253.cold.1
- ___28-[ACAccountStore handleURL:]_block_invoke.253.cold.2
- ___36-[ACAccountStore shutdownAccountsD:]_block_invoke.259
- ___36-[ACAccountStore shutdownAccountsD:]_block_invoke_2.260
- ___41-[ACAccountStore removeObsoleteAccounts:]_block_invoke.236
- ___45-[ACAccountStore credentialForAccount:error:]_block_invoke.171
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.254
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.256
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.255
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.255.cold.1
- ___46-[ACCredentialCache initWithValidityDuration:]_block_invoke
- ___48-[ACAccountStore childAccountsForAccount:error:]_block_invoke.187
- ___48-[ACAccountStore parentAccountForAccount:error:]_block_invoke.186
- ___53-[ACAccountStore enabledDataclassesForAccount:error:]_block_invoke.191
- ___54-[ACAccountStore triggerKeychainMigrationIfNecessary:]_block_invoke.233
- ___55-[ACAccountStore credentialForAccount:serviceID:error:]_block_invoke.172
- ___55-[ACAccountStore dataclassActionsForAccountSave:error:]_block_invoke.195
- ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke.193
- ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke_2.194
- ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke.257
- ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke_2.258
- ___57-[ACAccountStore provisionedDataclassesForAccount:error:]_block_invoke.192
- ___59-[ACAccountStore dataclassActionsForAccountDeletion:error:]_block_invoke.196
- ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke.184
- ___59-[ACAccountStore setCredential:forAccount:serviceID:error:]_block_invoke.174
- ___61-[ACAccountStore _removeObsoleteAccountsInternal:completion:]_block_invoke.238
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke.182
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2.183
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke.185
- ___63-[ACAccountStore isPerformingDataclassActionsForAccount:error:]_block_invoke.197
- ___66-[ACAccountStore discoverPropertiesForAccount:options:completion:]_block_invoke.207
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.224
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.226
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.225
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.225.cold.1
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.230
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.232
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.231
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.231.cold.1
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.227
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.229
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.228
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.228.cold.1
- ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke.211
- ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke_2.212
- ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.222
- ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.222.cold.1
- ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.223
- ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.223.cold.1
- ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke.205
- ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke_2.206
- ___block_descriptor_64_e8_32s40s48s56r_e40_v16?0"<ACRemoteAccountStoreProtocol>"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.235
- ___block_literal_global.263
- _objc_msgSend$_handleKeyagFirstUnlocked
CStrings:
+ "."
+ "@\"Returning cached credential %@ for account %@\""
+ "@\"Returning cached credential %@ for account %@, serviceID %@\""
+ "_handleKeybagFirstUnlocked"
- "%@.%@"
- "_handleKeyagFirstUnlocked"

```
