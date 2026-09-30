## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-999.4.0.0.0
-  __TEXT.__text: 0x590e0
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x3fc4
+1014.0.0.0.0
+  __TEXT.__text: 0x5c7d4
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x42e4
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3dc4
-  __TEXT.__cstring: 0x3b24
-  __TEXT.__oslogstring: 0x539a
-  __TEXT.__unwind_info: 0x1970
-  __TEXT.__objc_classname: 0x549
-  __TEXT.__objc_methname: 0x8195
-  __TEXT.__objc_methtype: 0x1543
-  __TEXT.__objc_stubs: 0x5da0
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x2510
-  __DATA_CONST.__objc_classlist: 0x190
-  __DATA_CONST.__objc_catlist: 0x28
+  __TEXT.__gcc_except_tab: 0x3ecc
+  __TEXT.__cstring: 0x3c7b
+  __TEXT.__oslogstring: 0x5245
+  __TEXT.__unwind_info: 0x1a78
+  __TEXT.__objc_classname: 0x599
+  __TEXT.__objc_methname: 0x89ab
+  __TEXT.__objc_methtype: 0x150f
+  __TEXT.__objc_stubs: 0x6520
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x2518
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2088
+  __DATA_CONST.__objc_selrefs: 0x2280
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x4720
-  __AUTH_CONST.__objc_const: 0x58e8
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x4860
+  __AUTH_CONST.__objc_const: 0x5e18
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_intobj: 0x558
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_ivar: 0x3dc
   __DATA.__data: 0x4d0
-  __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA.__bss: 0x109
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F5CA2AC-01B9-3A72-8E97-FAA56D719F1B
-  Functions: 1885
-  Symbols:   6492
-  CStrings:  3318
+  UUID: 17372AD6-E5EF-33E7-AFBE-B852F8C4B8FC
+  Functions: 1958
+  Symbols:   6750
+  CStrings:  3426
 
Symbols:
+ +[ACAccountUniquingCache sharedUniqueCache]
+ +[ACAccountUniquingCache sharedUniqueCache].cold.1
+ +[ACCredentialCache __enableCache]
+ +[ACCredentialCache _cacheEnabled]
+ +[ACCredentialCache _credentialKeyForAccount:serviceID:]
+ +[ACLoggingHashCache sharedCache]
+ +[ACLoggingHashCache sharedCache].cold.1
+ +[ACProtobufAccount enabledEnumDataclassesType]
+ +[ACProtobufAccount provisionedEnumDataclassesType]
+ +[ACProtobufAccountType supportedEnumDataclassesType]
+ +[ACProtobufAccountType syncableEnumDataclassesType]
+ -[ACAccount _cacheParentAccountID]
+ -[ACAccount _cachedParentAccountID]
+ -[ACAccountStoreCache credentialCache]
+ -[ACAccountStoreCache setCredentialCache:]
+ -[ACAccountUniquingCache .cxx_destruct]
+ -[ACAccountUniquingCache _lock_cacheParentChain:]
+ -[ACAccountUniquingCache _lock_clearParentChains:]
+ -[ACAccountUniquingCache _lock_hydrateParentChain:]
+ -[ACAccountUniquingCache cacheAccounts:]
+ -[ACAccountUniquingCache cachedAccountsByIdentifiers:]
+ -[ACAccountUniquingCache clearAccountsByIdentifiers:]
+ -[ACAccountUniquingCache init]
+ -[ACCredentialCache .cxx_destruct]
+ -[ACCredentialCache _clearAllCaches]
+ -[ACCredentialCache _handleKeyagFirstUnlocked]
+ -[ACCredentialCache cacheCredential:forAccount:serviceID:]
+ -[ACCredentialCache cachedCredentialForAccount:serviceID:]
+ -[ACCredentialCache cachedCredentials]
+ -[ACCredentialCache clearCachedCredentialsForAccount:]
+ -[ACCredentialCache clearCachedCredentialsForAccountID:]
+ -[ACCredentialCache dealloc]
+ -[ACCredentialCache expirersByCredentialKey]
+ -[ACCredentialCache initWithValidityDuration:]
+ -[ACCredentialCache setCachedCredentials:]
+ -[ACCredentialCache setExpirersByCredentialKey:]
+ -[ACLoggingHashCache .cxx_destruct]
+ -[ACLoggingHashCache hashedString:]
+ -[ACLoggingHashCache initWithMaxCapacity:]
+ -[ACNotifyAccountCache _lock_clearCachedAccounts]
+ -[ACProtobufAccount addEnabledEnumDataclasses:]
+ -[ACProtobufAccount addProvisionedEnumDataclasses:]
+ -[ACProtobufAccount clearEnabledEnumDataclasses]
+ -[ACProtobufAccount clearProvisionedEnumDataclasses]
+ -[ACProtobufAccount enabledEnumDataclassesAtIndex:]
+ -[ACProtobufAccount enabledEnumDataclassesCount]
+ -[ACProtobufAccount enabledEnumDataclasses]
+ -[ACProtobufAccount provisionedEnumDataclassesAtIndex:]
+ -[ACProtobufAccount provisionedEnumDataclassesCount]
+ -[ACProtobufAccount provisionedEnumDataclasses]
+ -[ACProtobufAccount setEnabledEnumDataclasses:]
+ -[ACProtobufAccount setProvisionedEnumDataclasses:]
+ -[ACProtobufAccountType addSupportedEnumDataclasses:]
+ -[ACProtobufAccountType addSyncableEnumDataclasses:]
+ -[ACProtobufAccountType clearSupportedEnumDataclasses]
+ -[ACProtobufAccountType clearSyncableEnumDataclasses]
+ -[ACProtobufAccountType setSupportedEnumDataclasses:]
+ -[ACProtobufAccountType setSyncableEnumDataclasses:]
+ -[ACProtobufAccountType supportedEnumDataclassesAtIndex:]
+ -[ACProtobufAccountType supportedEnumDataclassesCount]
+ -[ACProtobufAccountType supportedEnumDataclasses]
+ -[ACProtobufAccountType syncableEnumDataclassesAtIndex:]
+ -[ACProtobufAccountType syncableEnumDataclassesCount]
+ -[ACProtobufAccountType syncableEnumDataclasses]
+ -[NSString(ACLoggingHashing) ac_sha512HashString]
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table114
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table86
+ _ACAccountDataclassDeviceEnrollments
+ _ACAccountDataclassForACDataclass
+ _ACAccountDataclassForACDataclass.cold.1
+ _ACAccountDataclassForACDataclass.dataclassArray
+ _ACAccountDataclassForACDataclass.onceToken
+ _ACDataclassForACAccountDataclass
+ _ACDataclassForACAccountDataclass.cold.1
+ _ACDataclassForACAccountDataclass.onceToken
+ _ACDataclassForACAccountDataclass.stringsToEnumDict
+ _ACHashedString
+ _CC_SHA512
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _OBJC_CLASS_$_ACAccountUniquingCache
+ _OBJC_CLASS_$_ACCredentialCache
+ _OBJC_CLASS_$_ACLoggingHashCache
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_ACAccount._cachedParentAccountID
+ _OBJC_IVAR_$_ACAccount._enabledEnumDataclasses
+ _OBJC_IVAR_$_ACAccount._provisionedEnumDataclasses
+ _OBJC_IVAR_$_ACAccountStoreCache._credentialCache
+ _OBJC_IVAR_$_ACAccountType._supportedEnumDataclasses
+ _OBJC_IVAR_$_ACAccountType._syncableEnumDataclasses
+ _OBJC_IVAR_$_ACAccountUniquingCache._cachedAccounts
+ _OBJC_IVAR_$_ACAccountUniquingCache._uniqueCachedAccountsLock
+ _OBJC_IVAR_$_ACCredentialCache._cachedCredentials
+ _OBJC_IVAR_$_ACCredentialCache._credentialCacheLock
+ _OBJC_IVAR_$_ACCredentialCache._credentialsDidChangeObserver
+ _OBJC_IVAR_$_ACCredentialCache._expirersByCredentialKey
+ _OBJC_IVAR_$_ACCredentialCache._expirersLock
+ _OBJC_IVAR_$_ACCredentialCache._validityDuration
+ _OBJC_IVAR_$_ACLoggingHashCache._cacheDictionary
+ _OBJC_IVAR_$_ACLoggingHashCache._cacheLock
+ _OBJC_IVAR_$_ACLoggingHashCache._maxCapacity
+ _OBJC_IVAR_$_ACLoggingHashCache._oldestKeys
+ _OBJC_IVAR_$_ACNotifyAccountCache._cachedAccountIDs
+ _OBJC_IVAR_$_ACProtobufAccount._enabledEnumDataclasses
+ _OBJC_IVAR_$_ACProtobufAccount._provisionedEnumDataclasses
+ _OBJC_IVAR_$_ACProtobufAccountType._supportedEnumDataclasses
+ _OBJC_IVAR_$_ACProtobufAccountType._syncableEnumDataclasses
+ _OBJC_METACLASS_$_ACAccountUniquingCache
+ _OBJC_METACLASS_$_ACCredentialCache
+ _OBJC_METACLASS_$_ACLoggingHashCache
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_ACLoggingHashing
+ __OBJC_$_CATEGORY_NSString_$_ACLoggingHashing
+ __OBJC_$_CLASS_METHODS_ACAccountUniquingCache
+ __OBJC_$_CLASS_METHODS_ACCredentialCache
+ __OBJC_$_CLASS_METHODS_ACLoggingHashCache
+ __OBJC_$_CLASS_METHODS_ACProtobufAccountType
+ __OBJC_$_INSTANCE_METHODS_ACAccountUniquingCache
+ __OBJC_$_INSTANCE_METHODS_ACCredentialCache
+ __OBJC_$_INSTANCE_METHODS_ACLoggingHashCache
+ __OBJC_$_INSTANCE_VARIABLES_ACAccountUniquingCache
+ __OBJC_$_INSTANCE_VARIABLES_ACCredentialCache
+ __OBJC_$_INSTANCE_VARIABLES_ACLoggingHashCache
+ __OBJC_$_PROP_LIST_ACAccountStoreCache
+ __OBJC_$_PROP_LIST_ACCredentialCache
+ __OBJC_CLASS_RO_$_ACAccountUniquingCache
+ __OBJC_CLASS_RO_$_ACCredentialCache
+ __OBJC_CLASS_RO_$_ACLoggingHashCache
+ __OBJC_METACLASS_RO_$_ACAccountUniquingCache
+ __OBJC_METACLASS_RO_$_ACCredentialCache
+ __OBJC_METACLASS_RO_$_ACLoggingHashCache
+ ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke.220
+ ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke_2.221
+ ___28-[ACAccountStore handleURL:]_block_invoke.253
+ ___28-[ACAccountStore handleURL:]_block_invoke.253.cold.1
+ ___28-[ACAccountStore handleURL:]_block_invoke.253.cold.2
+ ___33+[ACLoggingHashCache sharedCache]_block_invoke
+ ___35-[ACLoggingHashCache hashedString:]_block_invoke
+ ___36-[ACAccountStore shutdownAccountsD:]_block_invoke.259
+ ___36-[ACAccountStore shutdownAccountsD:]_block_invoke_2.260
+ ___36-[ACCredentialCache _clearAllCaches]_block_invoke
+ ___36-[ACCredentialCache _clearAllCaches]_block_invoke_2
+ ___40-[ACAccountUniquingCache cacheAccounts:]_block_invoke
+ ___41-[ACAccountStore removeObsoleteAccounts:]_block_invoke.236
+ ___43+[ACAccountUniquingCache sharedUniqueCache]_block_invoke
+ ___45-[ACAccountStore credentialForAccount:error:]_block_invoke.171
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.254
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.256
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.255
+ ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.255.cold.1
+ ___46-[ACCredentialCache initWithValidityDuration:]_block_invoke
+ ___48-[ACAccountStore childAccountsForAccount:error:]_block_invoke.187
+ ___48-[ACAccountStore parentAccountForAccount:error:]_block_invoke.186
+ ___53-[ACAccountStore enabledDataclassesForAccount:error:]_block_invoke.191
+ ___53-[ACAccountUniquingCache clearAccountsByIdentifiers:]_block_invoke
+ ___53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.24
+ ___54-[ACAccountStore triggerKeychainMigrationIfNecessary:]_block_invoke.233
+ ___54-[ACAccountUniquingCache cachedAccountsByIdentifiers:]_block_invoke
+ ___55-[ACAccountStore credentialForAccount:serviceID:error:]_block_invoke.172
+ ___55-[ACAccountStore dataclassActionsForAccountSave:error:]_block_invoke.195
+ ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke.193
+ ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke_2.194
+ ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke.257
+ ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke_2.258
+ ___56-[ACCredentialCache clearCachedCredentialsForAccountID:]_block_invoke
+ ___56-[ACCredentialCache clearCachedCredentialsForAccountID:]_block_invoke_2
+ ___57-[ACAccountStore provisionedDataclassesForAccount:error:]_block_invoke.192
+ ___58-[ACCredentialCache cacheCredential:forAccount:serviceID:]_block_invoke
+ ___58-[ACCredentialCache cacheCredential:forAccount:serviceID:]_block_invoke_2
+ ___58-[ACCredentialCache cacheCredential:forAccount:serviceID:]_block_invoke_3
+ ___58-[ACCredentialCache cacheCredential:forAccount:serviceID:]_block_invoke_4
+ ___58-[ACCredentialCache cachedCredentialForAccount:serviceID:]_block_invoke
+ ___59-[ACAccountStore dataclassActionsForAccountDeletion:error:]_block_invoke.196
+ ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke.184
+ ___59-[ACAccountStore setCredential:forAccount:serviceID:error:]_block_invoke.174
+ ___61-[ACAccountStore _removeObsoleteAccountsInternal:completion:]_block_invoke.238
+ ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke.182
+ ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2.183
+ ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke.185
+ ___63-[ACAccountStore isPerformingDataclassActionsForAccount:error:]_block_invoke.197
+ ___66-[ACAccountStore discoverPropertiesForAccount:options:completion:]_block_invoke.207
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.224
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.226
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.225
+ ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.225.cold.1
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.230
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.232
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.231
+ ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.231.cold.1
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.227
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.229
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.228
+ ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.228.cold.1
+ ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke.211
+ ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke_2.212
+ ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.222
+ ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.222.cold.1
+ ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.223
+ ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.223.cold.1
+ ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke.205
+ ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke_2.206
+ ___ACAccountDataclassForACDataclass_block_invoke
+ ___ACDataclassForACAccountDataclass_block_invoke
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"NSString"8"ACAccountCredential"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_8?0ls32l8s40l8s48l8
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.235
+ ___block_literal_global.263
+ ___credentialCacheEnabled
+ ___handleKeyagFirstUnlocked
+ _objc_msgSend$_cacheEnabled
+ _objc_msgSend$_cacheParentAccountID
+ _objc_msgSend$_cachedParentAccountID
+ _objc_msgSend$_credentialKeyForAccount:serviceID:
+ _objc_msgSend$_handleKeyagFirstUnlocked
+ _objc_msgSend$_lock_cacheParentChain:
+ _objc_msgSend$_lock_clearCachedAccounts
+ _objc_msgSend$_lock_clearParentChains:
+ _objc_msgSend$_lock_hydrateParentChain:
+ _objc_msgSend$_resetParentAccount:
+ _objc_msgSend$_setError
+ _objc_msgSend$ac_sha512HashString
+ _objc_msgSend$addEnabledEnumDataclasses:
+ _objc_msgSend$addProvisionedEnumDataclasses:
+ _objc_msgSend$addSupportedEnumDataclasses:
+ _objc_msgSend$addSyncableEnumDataclasses:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$cacheCredential:forAccount:serviceID:
+ _objc_msgSend$cachedAccountsByIdentifiers:
+ _objc_msgSend$cachedCredentialForAccount:serviceID:
+ _objc_msgSend$cachedCredentials
+ _objc_msgSend$clearAccountsByIdentifiers:
+ _objc_msgSend$clearCachedCredentialsForAccount:
+ _objc_msgSend$clearCachedCredentialsForAccountID:
+ _objc_msgSend$clearEnabledEnumDataclasses
+ _objc_msgSend$clearProvisionedEnumDataclasses
+ _objc_msgSend$clearSupportedEnumDataclasses
+ _objc_msgSend$clearSyncableEnumDataclasses
+ _objc_msgSend$credentialCache
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$enabledEnumDataclasses
+ _objc_msgSend$enabledEnumDataclassesAtIndex:
+ _objc_msgSend$enabledEnumDataclassesCount
+ _objc_msgSend$expirersByCredentialKey
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hashedString:
+ _objc_msgSend$initWithMaxCapacity:
+ _objc_msgSend$initWithValidityDuration:
+ _objc_msgSend$lastObject
+ _objc_msgSend$nonPersistentKeysForAccountTypeIdentifier:credentialType:
+ _objc_msgSend$position
+ _objc_msgSend$provisionedEnumDataclasses
+ _objc_msgSend$provisionedEnumDataclassesAtIndex:
+ _objc_msgSend$provisionedEnumDataclassesCount
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setCredentialCache:
+ _objc_msgSend$setEnabledEnumDataclasses:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setProvisionedEnumDataclasses:
+ _objc_msgSend$setSupportedEnumDataclasses:
+ _objc_msgSend$setSyncableEnumDataclasses:
+ _objc_msgSend$sharedUniqueCache
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$supportedEnumDataclasses
+ _objc_msgSend$supportedEnumDataclassesAtIndex:
+ _objc_msgSend$supportedEnumDataclassesCount
+ _objc_msgSend$syncableEnumDataclasses
+ _objc_msgSend$syncableEnumDataclassesAtIndex:
+ _objc_msgSend$syncableEnumDataclassesCount
+ _sharedCache.sharedCache
+ _sharedUniqueCache._sharedUniqueCache
+ _sharedUniqueCache.onceToken
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:].cold.1
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:].cold.2
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:]
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:].cold.1
- -[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:].cold.2
- -[ACNotifyAccountCache _lock_clearCcachedAccounts]
- GCC_except_table110
- GCC_except_table126
- GCC_except_table133
- GCC_except_table424
- GCC_except_table430
- GCC_except_table88
- GCC_except_table92
- GCC_except_table93
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_IVAR_$_ACMonitoredAccountStore._remoteAccountDidChangeObserver
- _OBJC_IVAR_$_ACNotifyAccountCache._cachedAccounts
- ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke.219
- ___114-[ACAccountStore openAuthenticationURLForAccount:withDelegateClassName:fromBundleAtPath:shouldConfirm:completion:]_block_invoke_2.220
- ___28-[ACAccountStore handleURL:]_block_invoke.252
- ___28-[ACAccountStore handleURL:]_block_invoke.252.cold.1
- ___28-[ACAccountStore handleURL:]_block_invoke.252.cold.2
- ___36-[ACAccountStore shutdownAccountsD:]_block_invoke.258
- ___36-[ACAccountStore shutdownAccountsD:]_block_invoke_2.259
- ___41-[ACAccountStore removeObsoleteAccounts:]_block_invoke.235
- ___45-[ACAccountStore credentialForAccount:error:]_block_invoke.170
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.253
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke.255
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.254
- ___46-[ACAccountStore scheduleBackupIfNonexistent:]_block_invoke_2.254.cold.1
- ___47-[ACAccountStoreCache setupMemoryNotifications]_block_invoke.cold.1
- ___48-[ACAccountStore childAccountsForAccount:error:]_block_invoke.186
- ___48-[ACAccountStore parentAccountForAccount:error:]_block_invoke.185
- ___53-[ACAccountStore enabledDataclassesForAccount:error:]_block_invoke.190
- ___53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.26
- ___54-[ACAccountStore triggerKeychainMigrationIfNecessary:]_block_invoke.232
- ___55-[ACAccountStore credentialForAccount:serviceID:error:]_block_invoke.171
- ___55-[ACAccountStore dataclassActionsForAccountSave:error:]_block_invoke.194
- ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke.192
- ___55-[ACAccountStore preloadDataclassOwnersWithCompletion:]_block_invoke_2.193
- ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke.256
- ___56-[ACAccountStore resetDatabaseToVersion:withCompletion:]_block_invoke_2.257
- ___57-[ACAccountStore provisionedDataclassesForAccount:error:]_block_invoke.191
- ___59-[ACAccountStore dataclassActionsForAccountDeletion:error:]_block_invoke.195
- ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke.183
- ___59-[ACAccountStore setCredential:forAccount:serviceID:error:]_block_invoke.173
- ___61-[ACAccountStore _removeObsoleteAccountsInternal:completion:]_block_invoke.237
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke.181
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2.182
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke.184
- ___63-[ACAccountStore isPerformingDataclassActionsForAccount:error:]_block_invoke.196
- ___66-[ACAccountStore discoverPropertiesForAccount:options:completion:]_block_invoke.206
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.223
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke.225
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.224
- ___67-[ACAccountStore saveAccount:toPairedDeviceWithOptions:completion:]_block_invoke_2.224.cold.1
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.229
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke.231
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.230
- ___71-[ACAccountStore removeAccountFromPairedDevice:withOptions:completion:]_block_invoke_2.230.cold.1
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.226
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke.228
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.227
- ___71-[ACAccountStore removeAccountsFromPairedDeviceWithOptions:completion:]_block_invoke_2.227.cold.1
- ___74-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:]_block_invoke
- ___74-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:]_block_invoke.260
- ___74-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:]_block_invoke_2
- ___74-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:error:]_block_invoke_2.cold.1
- ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke.210
- ___76-[ACAccountStore openAuthenticationURL:forAccount:shouldConfirm:completion:]_block_invoke_2.211
- ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.221
- ___78-[ACAccountStore notifyRemoteDevicesOfModifiedAccount:withOptions:completion:]_block_invoke.221.cold.1
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke.261
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke.263
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke_2
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke_2.262
- ___79-[ACAccountStore accountsOfTypeID:customProperty:value:cacheSuffix:completion:]_block_invoke_2.262.cold.1
- ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.222
- ___81-[ACAccountStore notifyRemoteDevicesOfUpdatedCredentials:withOptions:completion:]_block_invoke.222.cold.1
- ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke.204
- ___96-[ACAccountStore accountIdentifiersEnabledForDataclasses:withAccountTypeIdentifiers:completion:]_block_invoke_2.205
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e40_v16?0"<ACRemoteAccountStoreProtocol>"8ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e40_v16?0"<ACRemoteAccountStoreProtocol>"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.234
- ___block_literal_global.266
- _objc_msgSend$_lock_clearCcachedAccounts
- _objc_msgSend$accountsWithTypeIdentifier:propertyKey:value:cacheSuffix:completion:
- _xpc_dictionary_create_reply
- _xpc_dictionary_send_reply
CStrings:
+ "%02x"
+ "%@.%@"
+ "@\"ACCredentialCache\""
+ "@20@0:8I16"
+ "ACAccountUniquingCache"
+ "ACClientSideCredentialCache"
+ "ACCredentialCache"
+ "ACLoggingHashCache"
+ "ACLoggingHashing"
+ "END [%lld] %fs: AccountsWithTypesWithPropertiesSync %@%@"
+ "END [%lld] %fs: PermissionForAccountType %{public}@"
+ "H:"
+ "I"
+ "S"
+ "T@\"ACCredentialCache\",&,V_credentialCache"
+ "T@\"NSMutableArray\",&,N,V_enabledEnumDataclasses"
+ "T@\"NSMutableArray\",&,N,V_provisionedEnumDataclasses"
+ "T@\"NSMutableArray\",&,N,V_supportedEnumDataclasses"
+ "T@\"NSMutableArray\",&,N,V_syncableEnumDataclasses"
+ "T@\"NSMutableDictionary\",&,V_cachedCredentials"
+ "T@\"NSMutableDictionary\",&,V_expirersByCredentialKey"
+ "UnhashedLogging"
+ "__enableCache"
+ "_cacheDictionary"
+ "_cacheEnabled"
+ "_cacheLock"
+ "_cacheParentAccountID"
+ "_cachedAccountIDs"
+ "_cachedCredentials"
+ "_cachedParentAccountID"
+ "_credentialCache"
+ "_credentialCacheLock"
+ "_credentialKeyForAccount:serviceID:"
+ "_enabledEnumDataclasses"
+ "_expirersByCredentialKey"
+ "_expirersLock"
+ "_handleKeyagFirstUnlocked"
+ "_lock_cacheParentChain:"
+ "_lock_clearCachedAccounts"
+ "_lock_clearParentChains:"
+ "_lock_hydrateParentChain:"
+ "_maxCapacity"
+ "_oldestKeys"
+ "_provisionedEnumDataclasses"
+ "_setError"
+ "_supportedEnumDataclasses"
+ "_syncableEnumDataclasses"
+ "_uniqueCachedAccountsLock"
+ "_validityDuration"
+ "ac_sha512HashString"
+ "addEnabledEnumDataclasses:"
+ "addProvisionedEnumDataclasses:"
+ "addSupportedEnumDataclasses:"
+ "addSyncableEnumDataclasses:"
+ "appendFormat:"
+ "appendString:"
+ "cacheCredential:forAccount:serviceID:"
+ "cachedAccountsByIdentifiers:"
+ "cachedCredentialForAccount:serviceID:"
+ "cachedCredentials"
+ "clearAccountsByIdentifiers:"
+ "clearCachedCredentialsForAccount:"
+ "clearCachedCredentialsForAccountID:"
+ "clearEnabledEnumDataclasses"
+ "clearProvisionedEnumDataclasses"
+ "clearSupportedEnumDataclasses"
+ "clearSyncableEnumDataclasses"
+ "com.apple.Dataclass.DeviceEnrollments"
+ "com.apple.mobile.keybagd.lock_status"
+ "credentialCache"
+ "dataUsingEncoding:"
+ "enabledDataclassesEnumValues"
+ "enabledEnumDataclasses"
+ "enabledEnumDataclassesAtIndex:"
+ "enabledEnumDataclassesCount"
+ "enabledEnumDataclassesType"
+ "enumValue"
+ "expirersByCredentialKey"
+ "getBytes:range:"
+ "hasError"
+ "hashedString:"
+ "initWithMaxCapacity:"
+ "initWithValidityDuration:"
+ "lastObject"
+ "position"
+ "provisionedDataclassesEnumValues"
+ "provisionedEnumDataclasses"
+ "provisionedEnumDataclassesAtIndex:"
+ "provisionedEnumDataclassesCount"
+ "provisionedEnumDataclassesType"
+ "removeObjectsForKeys:"
+ "setCachedCredentials:"
+ "setCredentialCache:"
+ "setEnabledEnumDataclasses:"
+ "setExpirersByCredentialKey:"
+ "setPosition:"
+ "setProvisionedEnumDataclasses:"
+ "setSupportedEnumDataclasses:"
+ "setSyncableEnumDataclasses:"
+ "sharedUniqueCache"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "supportedEnumDataclasses"
+ "supportedEnumDataclassesAtIndex:"
+ "supportedEnumDataclassesCount"
+ "supportedEnumDataclassesType"
+ "syncableEnumDataclasses"
+ "syncableEnumDataclassesAtIndex:"
+ "syncableEnumDataclassesCount"
+ "syncableEnumDataclassesType"
+ "type:%@\nidentifier: %@\naccountDescription: %@\nusername: %@ (%@)\nobjectID: %@\nprovisionedDataclasses: %@\nenabledDataclasses: %@\ndataclassProperties: %@\nproperties: %@\nparentAccount: %@\nowningBundleID:%@\nauthenticated: %@\nlastCredentialRenewalRejectedDate: %@\nsupportsAuthentication: %@\nauthenticationType: %@\ncredentialType: %@\ncredential: %@\ncreated: %@\nactive: %@\nvisible: %@\nwarmingUp: %@"
+ "v32@?0@\"NSString\"8@\"ACAccountCredential\"16^B24"
+ "v40@0:8@16@24@32"
- "\"ACAccountStoreCache: Memory pressure notification received, flushing cache\""
- "@56@0:8@16@24@32@40^@48"
- "AccountsForPropertyValue"
- "AccountsForPropertyValueSync"
- "BEGIN [%lld]: AccountsForPropertyValue "
- "BEGIN [%lld]: AccountsForPropertyValueSync "
- "END [%lld] %fs: AccountsForPropertyValue %@%@"
- "END [%lld] %fs: AccountsForPropertyValueSync %@%@"
- "END [%lld] %fs: ClearPermissionsForAccountType %{public}@"
- "_lock_clearCcachedAccounts"
- "_remoteAccountDidChangeObserver"
- "accounts/accounts-with-property-value"
- "accounts/accounts-with-property-value-sync"
- "accountsOfTypeID:customProperty:value:cacheSuffix:completion:"
- "accountsOfTypeID:customProperty:value:cacheSuffix:error:"
- "accountsWithTypeIdentifier:propertyKey:value:cacheSuffix:completion:"
- "ping"
- "type:%@\nidentifier: %@\naccountDescription: %@\nusername: %@\nobjectID: %@\nprovisionedDataclasses: %@\nenabledDataclasses: %@\ndataclassProperties: %@\nproperties: %@\nparentAccount: %@\nowningBundleID:%@\nauthenticated: %@\nlastCredentialRenewalRejectedDate: %@\nsupportsAuthentication: %@\nauthenticationType: %@\ncredentialType: %@\ncredential: %@\ncreated: %@\nactive: %@\nvisible: %@\nwarmingUp: %@"
- "v56@0:8@\"NSString\"16@\"NSString\"24@32@\"NSString\"40@?<v@?@\"NSArray\"@\"NSError\">48"

```
