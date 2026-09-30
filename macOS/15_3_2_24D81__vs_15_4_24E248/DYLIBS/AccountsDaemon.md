## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/Versions/A/AccountsDaemon`

```diff

-995.1.0.0.0
-  __TEXT.__text: 0x7da24
-  __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x328c
-  __TEXT.__const: 0x726
-  __TEXT.__oslogstring: 0x831f
-  __TEXT.__cstring: 0x3df3
-  __TEXT.__gcc_except_tab: 0x25bc
+999.4.0.0.0
+  __TEXT.__text: 0x7f154
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x3b1c
+  __TEXT.__const: 0x736
+  __TEXT.__oslogstring: 0x843f
+  __TEXT.__cstring: 0x3b33
+  __TEXT.__gcc_except_tab: 0x25a0
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__swift5_capture: 0xa8
   __TEXT.__swift5_reflstr: 0x151

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x1a10
-  __TEXT.__eh_frame: 0x270
-  __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0xb0e1
-  __TEXT.__objc_methtype: 0x245c
-  __TEXT.__objc_stubs: 0x8fa0
-  __DATA_CONST.__got: 0xca0
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__unwind_info: 0x1af8
+  __TEXT.__eh_frame: 0x2c8
+  __TEXT.__objc_classname: 0x61b
+  __TEXT.__objc_methname: 0xb1cf
+  __TEXT.__objc_methtype: 0x247c
+  __TEXT.__objc_stubs: 0x9060
+  __DATA_CONST.__got: 0xcb0
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2768
+  __DATA_CONST.__objc_selrefs: 0x2900
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0x1c40
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x56b0
+  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__const: 0x1c70
+  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__objc_const: 0x4728
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x2e0
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x29c
+  __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x780
   __DATA.__bss: 0x9b8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 21FF7A5D-A0F9-3515-A5F4-80E4AD4A1BA0
-  Functions: 2119
-  Symbols:   4902
-  CStrings:  3468
+  UUID: BADF7F26-B252-3057-8516-60B96D3E96D3
+  Functions: 2203
+  Symbols:   5004
+  CStrings:  3465
 
Symbols:
+ +[ACDAccountStore accountCache].cold.1
+ +[ACDDatabasePersistentConfiguration accountTypes].cold.1
+ +[ACDDatabasePersistentConfiguration dataclasses].cold.1
+ +[ACDEventLedger sharedLedger].cold.1
+ +[ACDKeychain _knownMigratedKeychainItems].cold.1
+ +[ACDKeychain _passwordForServiceName:username:accessGroup:checkInKeybag:options:error:].cold.1
+ +[ACDKeychain addItemWithServiceName:username:accessGroup:passwordData:options:error:].cold.1
+ +[ACDKeychain addSyncItemWithServiceName:username:accessGroup:options:extension:error:].cold.1
+ +[ACDKeychain removeItemForServiceName:username:accessGroup:options:error:].cold.2
+ +[ACDKeychain removeTombstoneForServiceName:username:accessGroup:extension:error:].cold.1
+ +[ACDKeychain updateItemForServiceName:username:accessGroup:newValues:options:error:].cold.1
+ +[ACDKeychain updateSyncItemForServiceName:username:accessGroup:newValues:extension:error:].cold.1
+ +[ACDKeychainCleanupActivity sharedActivity].cold.1
+ +[ACDKeychainManager _fallbackToUnsyncedOAuthTokens:].cold.1
+ +[ACDKeychainManager _saveCredential:forAccount:clientID:error:].cold.1
+ +[ACDPairedDeviceAccountCache sharedInstance].cold.1
+ +[ACDPluginLoader gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:]
+ +[ACDPluginLoader gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:].cold.1
+ +[ACDPluginLoader gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:].cold.2
+ +[ACDPreferences sharedPreferences].cold.1
+ +[ACRemoteDeviceMessage _whitelistedClasses].cold.1
+ +[ACRemoteDeviceMessage(Action) actionMessageWithCommand:account:options:].cold.1
+ +[ACRemoteDeviceMessage(Reply) replyForMessage:withSuccess:result:error:].cold.1
+ -[ACDAccountCache _clearCacheIncludingRemote:]
+ -[ACDAccountCache setupMemoryNotifications]
+ -[ACDAccountNotifier canRemoveAccount:inStore:error:].cold.2
+ -[ACDAccountNotifier canRemoveAccount:inStore:error:].cold.3
+ -[ACDAccountNotifier canRemoveAccount:inStore:error:].cold.4
+ -[ACDAccountNotifier canSaveAccount:inStore:error:].cold.2
+ -[ACDAccountNotifier canSaveAccount:inStore:error:].cold.3
+ -[ACDAccountNotifier canSaveAccount:inStore:error:].cold.4
+ -[ACDAccountNotifier postDidChangeNotificationForType:inStore:newAccount:oldAccount:].cold.2
+ -[ACDAccountNotifier postDidChangeNotificationForType:inStore:newAccount:oldAccount:].cold.3
+ -[ACDAccountNotifier postDidPerformDataclassActionsOnAccount:forDataclasses:].cold.2
+ -[ACDAccountNotifier postDidPerformDataclassActionsOnAccount:forDataclasses:].cold.3
+ -[ACDAccountNotifier postWillChangeNotificationForType:inStore:newAccount:oldAccount:].cold.1
+ -[ACDAccountNotifier postWillChangeNotificationForType:inStore:newAccount:oldAccount:].cold.2
+ -[ACDAccountNotifier postWillPerformDataclassActionsOnAccount:forDataclasses:].cold.2
+ -[ACDAccountNotifier postWillPerformDataclassActionsOnAccount:forDataclasses:].cold.3
+ -[ACDAccountStore _clientTokenQueue].cold.1
+ -[ACDAccountStore _lockForAccountType:].cold.1
+ -[ACDAccountStore _pruneDuplicateAccountsForAccountType:withUserName:error:].cold.4
+ -[ACDAccountStore _setAccountManagedObjectRelationships:withAccount:oldAccount:error:].cold.5
+ -[ACDAccountStore _setAccountManagedObjectRelationships:withAccount:oldAccount:error:].cold.6
+ -[ACDDatabase _performBackupToURL:unverifiedBackupURL:error:].cold.1
+ -[ACDDatabase _performBackupToURL:unverifiedBackupURL:error:].cold.2
+ -[ACDDatabase initWithDatabaseURL:storeOptions:].cold.5
+ -[ACDDatabase initWithDatabaseURL:storeOptions:].cold.6
+ -[ACDDatabaseConnection _beginObservingManagedObjectContextDidSaveNotifications].cold.1
+ -[ACDDatabaseConnection _delegate_databaseConnectionEncounteredUnrecoverableError:].cold.1
+ -[ACDDatabaseConnection _endObservingManagedObjectContextDidSaveNotifications].cold.1
+ -[ACDDatabaseConnection _managedObjectContextDidSave:].cold.1
+ -[ACDDatabaseConnection _persistentStore].cold.1
+ -[ACDDatabaseConnection _setupMemoryNotifications]
+ -[ACDDatabaseConnection _teardownMemoryNotifications]
+ -[ACDDatabaseConnection setVersion:].cold.1
+ -[ACDDatabaseInitializer _addDCAAccountType]
+ -[ACDDatabaseInitializer initWithDatabaseConnection:].cold.1
+ -[ACDEventLedger recordEvent:].cold.2
+ -[ACDServer _isHomePod].cold.1
+ -[ACDServer createClientForConnection:].cold.1
+ -[ACDServer createDatabaseConnection].cold.1
+ -[ACDServer initWithAccountStoreListener:oauthSignerListener:authenticationDialogListener:].cold.1
+ -[ACDServer initWithAccountStoreListener:oauthSignerListener:authenticationDialogListener:].cold.2
+ -[ACDServer initWithAccountStoreListener:oauthSignerListener:authenticationDialogListener:].cold.3
+ -[ACDServer listener:shouldAcceptNewConnection:].cold.6
+ -[ACDTestManager startTestServer].cold.1
+ -[ACDTimeMachineAccountStore initWithTimeMachineSnapshotHomeFolderPath:].cold.4
+ -[ACDTimeMachineAccountStore initWithTimeMachineSnapshotHomeFolderPath:].cold.5
+ -[ACDTimeMachineAccountStore initWithTimeMachineSnapshotHomeFolderPath:].cold.6
+ -[ACRemoteDeviceMessage initWithData:].cold.2
+ ExplicitAllowedPluginsByChangeType.cold.1
+ GCC_except_table28
+ GCC_except_table348
+ GCC_except_table39
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table78
+ OBJC_IVAR_$_ACDAccountCache._memoryNotificationSource
+ OBJC_IVAR_$_ACDDatabaseConnection._memoryNotificationSource
+ _ACAccountTypeIdentifierDCA
+ _ACDConnectionLogSystem.cold.1
+ _ACDEntitlementLogSystem.cold.1
+ _ACDKeychainLogSystem.cold.1
+ _ACDLazyArrayInitializeIfNecessary.cold.1
+ _ACDLogSystem.cold.1
+ _ACDManagedObjectModel.cold.1
+ _ACDNotificationLogSystem.cold.1
+ _ACDNotificationSignpostSystem.cold.1
+ _ACDPluginLogSystem.cold.1
+ _ACDSaveLogSystem.cold.1
+ __43-[ACDAccountCache setupMemoryNotifications]_block_invoke.cold.1
+ __46-[ACDAccountCache _clearCacheIncludingRemote:]_block_invoke.26
+ __50-[ACDDatabaseConnection _setupMemoryNotifications]_block_invoke.cold.1
+ ___43-[ACDAccountCache setupMemoryNotifications]_block_invoke
+ ___46-[ACDAccountCache _clearCacheIncludingRemote:]_block_invoke
+ ___50-[ACDDatabaseConnection _setupMemoryNotifications]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.157
+ __dispatch_source_type_memorypressure
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _kACDDetachedCAFullAccessEntitlement
+ _objc_msgSend$_addDCAAccountType
+ _objc_msgSend$_clearCacheIncludingRemote:
+ _objc_msgSend$_setupMemoryNotifications
+ _objc_msgSend$_teardownMemoryNotifications
+ _objc_msgSend$gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:
+ _objc_msgSend$setupMemoryNotifications
- +[ACDPluginLoader _buildPluginCache].cold.2
- +[ACDPluginLoader _buildPluginCache].cold.3
- GCC_except_table345
- GCC_except_table35
- GCC_except_table37
- GCC_except_table44
- GCC_except_table69
- GCC_except_table71
- GCC_except_table72
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- ___29-[ACDAccountCache clearCache]_block_invoke
- __block_literal_global.154
- _swift_arrayDestroy
CStrings:
+ "\"%{public}s error, account %{private}@ lacks an account type identifier\""
+ "\"ACDAccountCache: Memory pressure notification received, flushing cache\""
+ "\"ACDDatabaseConnection: Memory pressure notification received, flushing cache\""
+ "\"The plugin %@ for accountType %@ is being overwritten with plugin %@\""
+ "\"Using fallback Game Center ACD plugin.\""
+ "\"Using modern Game Center ACD plugin.\""
+ "+[ACDKeychainManager _saveCredential:forAccount:clientID:error:]"
+ "@\"NSObject<OS_dispatch_source>\""
+ "Detached Child Account"
+ "Q"
+ "_addDCAAccountType"
+ "_clearCacheIncludingRemote:"
+ "_memoryNotificationSource"
+ "_setupMemoryNotifications"
+ "_teardownMemoryNotifications"
+ "com.apple.iCloudIDAuthentication"
+ "gameCenterPluginNameFromPlugins:modernPluginEnabled:fallbackPluginID:modernPluginID:"
+ "setupMemoryNotifications"
- "\"Filtering out AAGKAuthenticationPlugin.\""
- "\"Filtering out GameCenterAccountAuthenticationPlugin.\""
- "%"
- "A"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "com.apple.AAGKAuthenticationPlugin"
- "invalid Collection: less than 'count' elements in collection"

```
