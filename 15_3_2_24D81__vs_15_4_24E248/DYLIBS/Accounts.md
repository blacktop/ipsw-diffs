## Accounts

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Accounts`

```diff

-995.1.0.0.0
-  __TEXT.__text: 0x5f480
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x398c
+999.4.0.0.0
+  __TEXT.__text: 0x606a4
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x3fac
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x3eac
-  __TEXT.__cstring: 0x3b55
-  __TEXT.__oslogstring: 0x53f6
-  __TEXT.__unwind_info: 0x1938
+  __TEXT.__gcc_except_tab: 0x3e60
+  __TEXT.__cstring: 0x3ba1
+  __TEXT.__oslogstring: 0x543e
+  __TEXT.__unwind_info: 0x19f0
   __TEXT.__objc_classname: 0x549
-  __TEXT.__objc_methname: 0x8132
+  __TEXT.__objc_methname: 0x819d
   __TEXT.__objc_methtype: 0x1543
-  __TEXT.__objc_stubs: 0x5d60
+  __TEXT.__objc_stubs: 0x5da0
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__const: 0xef8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe0
+  __DATA_CONST.__objc_selrefs: 0x2080
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x1b70
-  __AUTH_CONST.__cfstring: 0x4780
-  __AUTH_CONST.__objc_const: 0x6460
+  __AUTH_CONST.__cfstring: 0x47e0
+  __AUTH_CONST.__objc_const: 0x58e8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x4d8
   __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D355DF6E-43C2-3D7B-9F32-0CE5EAF9C5D6
-  Functions: 1859
-  Symbols:   4496
-  CStrings:  3328
+  UUID: 3B502966-35AB-3E59-8D2B-0C4B1A14C6F8
+  Functions: 1932
+  Symbols:   4579
+  CStrings:  3339
 
Symbols:
+ +[ACAccountCredential allSupportedKeys].cold.1
+ +[ACAccountStore _obsoleteAccountTypeIDsToRemove].cold.1
+ +[ACAccountStore defaultStore].cold.1
+ +[ACAccountStoreCache sharedCache].cold.1
+ +[ACAccountType allIdentifiers].cold.1
+ +[ACManagedDefaults sharedInstance].cold.1
+ +[ACNotificationRebroadcaster sharedRebroadcaster].cold.1
+ +[ACNotifyAccountCache _getUID].cold.1
+ +[ACPersonaManager sharedInstance].cold.1
+ +[ACXPCEventSubscriber sharedSubscriber].cold.1
+ +[NSSet(ACTrackingSet) setWithTrackedSet:].cold.1
+ -[ACAccount _initWithProtobufData:].cold.1
+ -[ACAccount setEnabled:forDataclass:].cold.2
+ -[ACAccount setEnabledDataclasses:].cold.2
+ -[ACAccount setSecIdentity:].cold.2
+ -[ACAccountCredential _initWithProtobufData:].cold.1
+ -[ACAccountStore _checkSaveRateLimitForAccountType:].cold.2
+ -[ACAccountType _initWithProtobufData:].cold.1
+ -[ACCredentialItem _initWithProtobufData:].cold.1
+ -[ACDataclassAction _initWithProtobufData:].cold.1
+ -[ACMonitoredAccountStore _lock_accountWasAdded:]
+ -[ACMonitoredAccountStore _lock_accountWasModified:]
+ -[ACMonitoredAccountStore _lock_accountWasRemoved:]
+ -[ACMonitoredAccountStore _lock_processAccountsListForNotifications:forType:]
+ -[ACRemoteAccountStoreSession _locked_configureRemoteAccountStoreWithConnection:].cold.1
+ -[ACRemoteAccountStoreSession _locked_connection:setEffectiveBundleID:].cold.1
+ -[ACRemoteAccountStoreSession _locked_connection:setNotificationsEnabled:].cold.1
+ -[ACTrackedSet _initWithEnumerable:count:].cold.1
+ -[ACTrackedSet _initWithEnumerable:count:].cold.2
+ -[ACTrackedSet _initWithUnderlyingSet:changesDictionary:].cold.1
+ -[ACTrackedSet _initWithUnderlyingSet:changesDictionary:].cold.2
+ -[ACTrackedSet initWithArray:].cold.1
+ -[ACTrackedSet initWithCoder:].cold.1
+ -[ACTrackedSet initWithSet:].cold.1
+ -[ACZeroingString initWithBytes:length:encoding:].cold.1
+ -[ACZeroingString initWithBytes:length:encoding:].cold.2
+ -[ACZeroingString initWithBytes:length:encoding:].cold.3
+ -[ACZeroingString initWithCharacters:length:].cold.1
+ -[ACZeroingString initWithString:].cold.1
+ -[ACZeroingString initWithUTF8String:].cold.1
+ -[NSArray(Accounts) ac_filter:].cold.1
+ -[NSArray(Accounts) ac_firstObjectPassingTest:].cold.1
+ -[NSArray(Accounts) ac_map:].cold.1
+ -[NSArray(Accounts) ac_mapNullable:].cold.1
+ -[NSDictionary(Accounts) ac_mapValues:].cold.1
+ -[NSDictionary(Accounts) ac_mapValuesNullable:].cold.1
+ -[NSManagedObject(Accounts) _obsoleteAttributes].cold.1
+ -[NSSet(ACTrackingSet) initWithTrackedSet:].cold.1
+ -[NSSet(Accounts) ac_map:].cold.1
+ -[NSSet(Accounts) ac_mapNullable:].cold.1
+ ACAccountTypeIdentifierForASSAccountType.cold.1
+ ACDGetTeamIDForBundleURL.cold.4
+ ACDataclassForASSDataclass.cold.1
+ ACIsAccountsd.cold.1
+ ACIsInternal.cold.1
+ GCC_except_table37
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table58
+ OBJC_IVAR_$_ACMonitoredAccountStore._monitoredAccountsCacheLock
+ _ACAccountTypeIdentifierDCA
+ _ACLogCache.cold.1
+ _ACLogSystem.cold.1
+ _ACPLogSystem.cold.1
+ _ACSignpostGetNanoseconds.cold.1
+ _ACSignpostLogSystem.cold.1
+ __38-[ACAccountStoreCache _clearAllCaches]_block_invoke.12
+ __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.32
+ __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.36
+ __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.36.cold.1
+ __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.37
+ __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.cold.1
+ __65-[ACMonitoredAccountStore _registerAccountMonitorWithCompletion:]_block_invoke.21
+ __65-[ACMonitoredAccountStore _registerAccountMonitorWithCompletion:]_block_invoke.25
+ __76-[ACMonitoredAccountStore _registerForApplicationStateDidChangeNotification]_block_invoke.cold.1
+ ___44-[ACMonitoredAccountStore monitoredAccounts]_block_invoke
+ ___49-[ACMonitoredAccountStore _lock_accountWasAdded:]_block_invoke
+ ___50-[ACMonitoredAccountStore _accountsListPopulated:]_block_invoke
+ ___51-[ACMonitoredAccountStore _lock_accountWasRemoved:]_block_invoke
+ ___52-[ACMonitoredAccountStore _lock_accountWasModified:]_block_invoke
+ ___58-[ACMonitoredAccountStore monitoredAccountWithIdentifier:]_block_invoke
+ __block_literal_global.112
+ __block_literal_global.123
+ __block_literal_global.133
+ __block_literal_global.139
+ _ac_dispatch_remote_sync_try.cold.1
+ _ac_dispatch_remote_sync_try.cold.2
+ _ac_dispatch_remote_sync_try.cold.3
+ _ac_dispatch_remote_try.cold.1
+ _ac_dispatch_remote_try.cold.2
+ _ac_dispatch_remote_try.cold.3
+ _kACDDetachedCAFullAccessEntitlement
+ _objc_msgSend$_lock_accountWasAdded:
+ _objc_msgSend$_lock_accountWasModified:
+ _objc_msgSend$_lock_accountWasRemoved:
+ _objc_msgSend$_lock_processAccountsListForNotifications:forType:
+ ac_dispatch_remote.cold.1
+ ac_dispatch_remote.cold.2
+ ac_dispatch_remote.cold.3
+ ac_dispatch_remote_sync.cold.1
+ ac_dispatch_remote_sync.cold.2
- -[ACMonitoredAccountStore _processAccountsListForNotifications:forType:]
- -[ACMonitoredAccountStore accountWasAdded:]
- -[ACMonitoredAccountStore accountWasModified:]
- -[ACMonitoredAccountStore accountWasRemoved:]
- GCC_except_table14
- GCC_except_table54
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.31
- __53-[ACMonitoredAccountStore _reregisterForAccountType:]_block_invoke.31.cold.1
- __65-[ACMonitoredAccountStore _registerAccountMonitorWithCompletion:]_block_invoke.18
- __65-[ACMonitoredAccountStore _registerAccountMonitorWithCompletion:]_block_invoke.22
- ___38-[ACAccountStoreCache _clearAllCaches]_block_invoke_2
- __block_literal_global.117
- __block_literal_global.130
- __block_literal_global.136
- _fmod
- _objc_msgSend$_processAccountsListForNotifications:forType:
- _objc_msgSend$monitoredAccounts
CStrings:
+ "\"ACMonitoredAccountStore UIApplicationDidBecomeActiveNotification received, refreshing\""
+ "\"ACMonitoredAccountStore: Failed to fetch accounts: %@\""
+ "\"ACMonitoredAccountStore: Fetched Accounts\""
+ "\"ACMonitoredAccountStore: Fetching accounts of account type %@...\""
+ "UIApplicationDidBecomeActiveNotification"
+ "_lock_accountWasAdded:"
+ "_lock_accountWasModified:"
+ "_lock_accountWasRemoved:"
+ "_lock_processAccountsListForNotifications:forType:"
+ "_monitoredAccountsCacheLock"
+ "com.apple.account.DCA"
+ "com.apple.account.dca.fullaccess"
+ "com.apple.gs.idms.pet"
- "\"ACMonitoredAccountStore: Attempting to reconnect to accountsd...\""
- "\"ACMonitoredAccountStore: Failed to reconnect to accountsd: %@\""
- "\"ACMonitoredAccountStore: Reconnected to accountsd\""
- "UIApplicationWillResignActiveNotification"
- "_processAccountsListForNotifications:forType:"

```
