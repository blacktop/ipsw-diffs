## AppSupport

> `/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`

```diff

-2672.1.3.0.0
-  __TEXT.__text: 0x2d3dc
+2672.1.5.0.0
+  __TEXT.__text: 0x2d588
   __TEXT.__objc_methlist: 0x12d0
   __TEXT.__cstring: 0x527c
   __TEXT.__const: 0x4dd0

   __AUTH.__objc_data: 0x690
   __AUTH.__data: 0x38
   __DATA.__objc_ivar: 0x25c
-  __DATA.__data: 0x551
+  __DATA.__data: 0x591
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x149
   __DATA_DIRTY.__bss: 0x170

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 1194
-  Symbols:   2472
+  Symbols:   2474
   CStrings:  787
 
Symbols:
+ ___yieldRegisteredDatabases
+ ___yieldStateLock
Functions:
~ _CPSqliteDatabaseClose : 108 -> 168
~ _CPSqliteRegisterYieldNotifyBlock : 88 -> 128
~ _CPSqliteDatabaseSetShouldYieldWhenRequested : 280 -> 492
~ ___updateNotifyRegistration_block_invoke : 64 -> 180
```
