## AppSupport

> `/System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport`

```diff

-2672.0.0.0.0
-  __TEXT.__text: 0x2c5ac
+2672.1.5.0.0
+  __TEXT.__text: 0x2c770
   __TEXT.__objc_methlist: 0x12a0
   __TEXT.__cstring: 0x4df7
   __TEXT.__const: 0x4dc0

   __AUTH_CONST.__cfstring: 0x38e0
   __AUTH_CONST.__objc_const: 0x2880
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xf60
+  __AUTH_CONST.__auth_got: 0xf68
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x5f0
   __AUTH.__data: 0x38
   __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0x551
-  __DATA.__bss: 0x1f8
+  __DATA.__data: 0x591
+  __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x109
   __DATA_DIRTY.__bss: 0x158

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 1173
-  Symbols:   2814
+  Symbols:   2817
   CStrings:  737
 
Symbols:
+ ___yieldRegisteredDatabases
+ ___yieldStateLock
+ _sleep
Functions:
~ _CPSqliteDatabaseClose : 120 -> 180
~ _CPSqliteRegisterYieldNotifyBlock : 100 -> 140
~ _CPSqliteDatabaseSetShouldYieldWhenRequested : 280 -> 492
~ ___updateNotifyRegistration_block_invoke : 64 -> 204
```
