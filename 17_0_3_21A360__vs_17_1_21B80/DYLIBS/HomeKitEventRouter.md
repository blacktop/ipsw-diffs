## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter`

```diff

-1054.1.7.1.4
-  __TEXT.__text: 0x15ad8
+1076.2.8.1.1
+  __TEXT.__text: 0x15ffc
   __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x119c
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__cstring: 0xb09
-  __TEXT.__oslogstring: 0x193f
-  __TEXT.__unwind_info: 0x5ec
+  __TEXT.__gcc_except_tab: 0x3f8
+  __TEXT.__cstring: 0xb1b
+  __TEXT.__oslogstring: 0x1bdb
+  __TEXT.__unwind_info: 0x5f0
   __TEXT.__objc_classname: 0x2ac
   __TEXT.__objc_methname: 0x3193
   __TEXT.__objc_methtype: 0xa12

   __DATA_CONST.__objc_const: 0x21a8
   __DATA_CONST.__objc_selrefs: 0xa80
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 451
-  Symbols:   1675
-  CStrings:  883
+  Functions: 452
+  Symbols:   1677
+  CStrings:  894
 
Symbols:
+ -[HMELastEventStore _cleanupResetRecreateAndRestartAfterIntegrityError]
+ GCC_except_table100
+ GCC_except_table234
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table369
+ GCC_except_table378
+ GCC_except_table395
+ GCC_except_table81
- GCC_except_table233
- GCC_except_table239
- GCC_except_table243
- GCC_except_table245
- GCC_except_table248
- GCC_except_table250
- GCC_except_table252
- GCC_except_table254
- GCC_except_table362
- GCC_except_table364
- GCC_except_table368
- GCC_except_table377
- GCC_except_table394
- GCC_except_table80
- GCC_except_table99
CStrings:
+ "Already attempted repair, fail."
+ "Could not perform integrity check failed %@"
+ "Error executing delete statement key: %@, deleteEventByKeyLikePreparedStatement is nil"
+ "Error executing delete statement key: %@, deleteEventByKeyPreparedStatement is nil"
+ "Error executing delete statement timestamp: %f, deleteBeforeTimestampPreparedStatement is nil"
+ "Error executing insert statement topic: %@, insertEventPreparedStatement is nil"
+ "Error executing insert statement topic: %@, replaceEventIfMoreRecentOrDifferentSourcePreparedStatement is nil"
+ "Error executing select statement key: %@, selectEventByKeyPreparedStatement is nil"
+ "Unable to create eventstore table %@"
+ "Unable to open %@ sqlite DB (%@)"
+ "Unable to read journal mode but no integrity error, fail."
+ "in memory"
+ "on disk"
- "Unable to open in memory sqlite DB"
- "Unable to open in memory sqlite DB %@"

```
