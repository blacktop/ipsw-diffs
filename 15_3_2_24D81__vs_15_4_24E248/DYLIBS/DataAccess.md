## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/Versions/A/DataAccess`

```diff

-2673.0.0.0.0
-  __TEXT.__text: 0x37554
+2673.5.2.0.0
+  __TEXT.__text: 0x380e4
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x365c
+  __TEXT.__objc_methlist: 0x3b1c
   __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x1758
+  __TEXT.__gcc_except_tab: 0x176c
   __TEXT.__cstring: 0x2b4e
   __TEXT.__oslogstring: 0x4351
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__objc_classname: 0x633
   __TEXT.__objc_methname: 0xa221
   __TEXT.__objc_methtype: 0x1a62

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2730
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x2c00
-  __AUTH_CONST.__objc_const: 0x58e8
+  __AUTH_CONST.__objc_const: 0x4fe8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1090

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F2C9143-B514-385D-BE79-1300D2C122B1
-  Functions: 1272
-  Symbols:   3294
+  UUID: 4FDB5EB4-8636-389B-B1A0-99D93B94D13C
+  Functions: 1346
+  Symbols:   3376
   CStrings:  2920
 
Symbols:
+ +[DAAccount(AuthenticationExtensions) _leafAccountTypes].cold.1
+ +[DAAccountLoader _findPrivateFrameworks].cold.1
+ +[DAAccountMonitor sharedMonitor].cold.1
+ +[DABabysitter sharedBabysitter].cold.1
+ +[DALocalDBGateKeeper sharedGateKeeper].cold.1
+ +[DALocalDBHelper os_log].cold.1
+ +[DALocalDBWatcher sharedDBWatcher].cold.1
+ +[DAPriorityManager sharedManager].cold.1
+ +[DAStoreSyncStatusUpdater _eventStorePurger].cold.1
+ +[DATransactionMonitor sharedTransactionMonitor].cold.1
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.1
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.2
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.3
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.4
+ +[DAiCalendarLogger sharedLogger].cold.1
+ -[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:].cold.1
+ -[ACAccountStore(DAExtensions) da_accountsWithAccountTypeIdentifiers:outError:].cold.1
+ -[DAAccount copyStorageSession].cold.1
+ -[DAAction encodeWithCoder:].cold.1
+ -[DAAction initWithCoder:].cold.1
+ -[DACalDBHelper _openDatabaseForPath:clientID:createdDatabaseToConsume:].cold.1
+ -[DACalDBHelper openDatabaseForAuxDatabaseRef:clientID:].cold.1
+ -[DADataHandler initWithContainer:changeTrackingID:].cold.1
+ -[DAEditPropertyAction encodeWithCoder:].cold.1
+ -[DAEditPropertyAction initWithCoder:].cold.1
+ -[DALocalDBGateKeeper dealloc].cold.1
+ -[DALocalDBGateKeeper dealloc].cold.2
+ -[DALocalDBHelper calOpenDatabaseForAccountID:clientID:].cold.1
+ -[DALocalDBHelper calOpenDatabaseForAuxDatabaseRef:clientID:].cold.1
+ -[DAMoveAction encodeWithCoder:].cold.1
+ -[DAMoveAction initWithCoder:].cold.1
+ -[DAPowerAssertionManager _retainAssertionForContext:].cold.1
+ -[DAPowerAssertionManager powerAssertionRetainCount:].cold.1
+ -[DAPowerAssertionManager releasePowerAssertion:].cold.1
+ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.1
+ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.2
+ -[DAPriorityManager appIDsToDataclasses].cold.1
+ -[DAPriorityManager requestPriority:forClient:dataclasses:].cold.1
+ -[DAResponse encodeWithCoder:].cold.1
+ -[DAResponse initWithCoder:].cold.1
+ -[DATaskManager _makeStateTransition].cold.1
+ -[DATaskManager _makeStateTransition].cold.10
+ -[DATaskManager _makeStateTransition].cold.11
+ -[DATaskManager _makeStateTransition].cold.12
+ -[DATaskManager _makeStateTransition].cold.13
+ -[DATaskManager _makeStateTransition].cold.14
+ -[DATaskManager _makeStateTransition].cold.15
+ -[DATaskManager _makeStateTransition].cold.16
+ -[DATaskManager _makeStateTransition].cold.17
+ -[DATaskManager _makeStateTransition].cold.18
+ -[DATaskManager _makeStateTransition].cold.19
+ -[DATaskManager _makeStateTransition].cold.2
+ -[DATaskManager _makeStateTransition].cold.3
+ -[DATaskManager _makeStateTransition].cold.4
+ -[DATaskManager _makeStateTransition].cold.5
+ -[DATaskManager _makeStateTransition].cold.6
+ -[DATaskManager _makeStateTransition].cold.7
+ -[DATaskManager _makeStateTransition].cold.8
+ -[DATaskManager _makeStateTransition].cold.9
+ -[DATaskManager _startModal:].cold.1
+ -[DATaskManager taskRequestModal:].cold.1
+ -[DATrafficLogger _ensureCustomLogFile].cold.1
+ -[DATransactionMonitor incrementTransactionCountForTransaction:].cold.1
+ -[DATrustHandler _serverSuffixesToAlwaysFail].cold.1
+ -[DATrustHandler handleTrustChallenge:forAccount:completionHandler:].cold.1
+ DAModelString.cold.1
+ DAProductString.cold.1
+ _NotificationHandlerMap.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __64-[DATransactionMonitor decrementTransactionCountForTransaction:]_block_invoke.cold.1
+ __setPasswordInKeychain
+ daDeviceID.cold.1
+ sharedDAAccountStore.cold.1

```
