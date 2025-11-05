## CDDataAccess

> `/System/Library/PrivateFrameworks/CDDataAccess.framework/Versions/A/CDDataAccess`

```diff

-1205.0.0.0.0
-  __TEXT.__text: 0x29188
+1225.1.0.0.0
+  __TEXT.__text: 0x29ab4
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x2b60
+  __TEXT.__objc_methlist: 0x2e50
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x1274
+  __TEXT.__gcc_except_tab: 0x1284
   __TEXT.__cstring: 0x212c
   __TEXT.__oslogstring: 0x29bd
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__unwind_info: 0x9f0
   __TEXT.__objc_classname: 0x4ab
   __TEXT.__objc_methname: 0x7620
   __TEXT.__objc_methtype: 0xd68

   __AUTH_CONST.__auth_got: 0x440
   __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x3ed8
+  __AUTH_CONST.__objc_const: 0x3930
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xb90
   __DATA.__objc_ivar: 0x234

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34EF9E3B-BA5D-3446-8B6F-4455907C58FC
-  Functions: 999
-  Symbols:   2483
+  UUID: 4C937FB3-D2D3-3FB3-A797-6DA8F1D1D04A
+  Functions: 1059
+  Symbols:   2551
   CStrings:  2194
 
Symbols:
+ +[DAAccount(AuthenticationExtensions) _leafAccountTypes].cold.1
+ +[DAAccountLoader _findPrivateFrameworks].cold.1
+ +[DAAccountMonitor sharedMonitor].cold.1
+ +[DABabysitter sharedBabysitter].cold.1
+ +[DALocalDBGateKeeper sharedGateKeeper].cold.1
+ +[DATransactionMonitor sharedTransactionMonitor].cold.1
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.1
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.2
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.3
+ +[DAUserNotificationUtilities showUserNotification:groupIdentifier:callbackQueue:sourceRunLoop:completionBlock:].cold.4
+ +[DAiCalendarLogger sharedLogger].cold.1
+ -[ACAccountStore(DAExtensions) _daAccountsWithAccountTypeIdentifiers:enabledForDADataclasses:filterOnDataclasses:withCompletion:].cold.1
+ -[DAAccount copyStorageSession].cold.1
+ -[DAAction encodeWithCoder:].cold.1
+ -[DAAction initWithCoder:].cold.1
+ -[DADataHandler initWithContainer:changeTrackingID:].cold.1
+ -[DALocalDBGateKeeper dealloc].cold.1
+ -[DALocalDBGateKeeper dealloc].cold.2
+ -[DAMoveAction encodeWithCoder:].cold.1
+ -[DAMoveAction initWithCoder:].cold.1
+ -[DAPowerAssertionManager _retainAssertionForContext:].cold.1
+ -[DAPowerAssertionManager powerAssertionRetainCount:].cold.1
+ -[DAPowerAssertionManager releasePowerAssertion:].cold.1
+ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.1
+ -[DAPowerAssertionManager retainPowerAssertion:withGroupIdentifier:].cold.2
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

```
