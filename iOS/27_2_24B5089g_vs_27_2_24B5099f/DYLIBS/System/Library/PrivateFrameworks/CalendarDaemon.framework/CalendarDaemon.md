## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1246.1.4.0.0
-  __TEXT.__text: 0x75964
+1246.2.1.0.0
+  __TEXT.__text: 0x75a48
   __TEXT.__objc_methlist: 0x697c
   __TEXT.__cstring: 0x7520
   __TEXT.__const: 0x190
-  __TEXT.__oslogstring: 0x8da3
+  __TEXT.__oslogstring: 0x8ddb
   __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4

   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1c70
+  __AUTH_CONST.__auth_got: 0x1c80
   __AUTH.__objc_data: 0x8c0
   __AUTH.__data: 0xa50
   __DATA.__objc_ivar: 0x868

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 2350
-  Symbols:   5612
-  CStrings:  1818
+  Symbols:   5614
+  CStrings:  1819
 
Symbols:
+ +[CADOperationGroupUtil _defaultCalendarIDForNewEventsInStoreWithID:connection:inDatabase:updateDefaultIfNeeded:defaultExists:]
+ _CalDatabaseClearDefaultCalendarIfDefaultIsInAuxDatabaseWithID
+ _CalDatabaseCopyOrCreateDefaultCalendarForNewEventsUpdateIfNeeded
- +[CADOperationGroupUtil defaultCalendarIDForNewEventsInStoreWithID:connection:inDatabase:defaultExists:]
Functions:
~ ___142-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseCommitDeletes:updatesAndInserts:options:andFetchChangesSinceTimestamp:withReply:]_block_invoke_2.38 : 1400 -> 1428
~ ___116-[CADXPCImplementation(CADDatabaseOperationGroup) findDatabaseForObject:withUpdates:personas:accounts:nextTempDBID:]_block_invoke : 852 -> 984
~ +[CADOperationGroupUtil defaultCalendarIDForNewEventsInStoreWithID:connection:inDatabase:defaultExists:] -> +[CADOperationGroupUtil _defaultCalendarIDForNewEventsInStoreWithID:connection:inDatabase:updateDefaultIfNeeded:defaultExists:] : 956 -> 968
~ ___98+[CADOperationGroupUtil defaultCalendarForNewEventsInDelegateSource:withConnection:limitedAccess:]_block_invoke_2 : 324 -> 368
~ ___98+[CADOperationGroupUtil defaultCalendarForNewEventsInDelegateSource:withConnection:limitedAccess:]_block_invoke_3 : 88 -> 92
~ ___98+[CADOperationGroupUtil defaultCalendarForNewEventsInDelegateSource:withConnection:limitedAccess:]_block_invoke_4 : 336 -> 340
~ ___98+[CADOperationGroupUtil defaultCalendarForNewEventsInDelegateSource:withConnection:limitedAccess:]_block_invoke_5 : 76 -> 80
CStrings:
+ "Failed to get container info for account %{public}@: %@"
```
