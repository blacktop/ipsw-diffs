## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12880.200.21.0.0
-  __TEXT.__text: 0x76c20
+12880.200.21.2.1
+  __TEXT.__text: 0x76f68
   __TEXT.__objc_methlist: 0x307c
   __TEXT.__const: 0x371
-  __TEXT.__cstring: 0x2708d
-  __TEXT.__oslogstring: 0x306b
+  __TEXT.__cstring: 0x271a8
+  __TEXT.__oslogstring: 0x316e
   __TEXT.__gcc_except_tab: 0x644
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x2428
+  __TEXT.__unwind_info: 0x2438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x5d8
   __AUTH_CONST.__const: 0xf20
-  __AUTH_CONST.__cfstring: 0xde80
+  __AUTH_CONST.__cfstring: 0xdee0
   __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2645
-  Symbols:   4459
-  CStrings:  2562
+  Functions: 2649
+  Symbols:   4461
+  CStrings:  2569
 
Symbols:
+ GCC_except_table114
+ _ABCDBContextIsMissingPersonIndexStatistics
+ __ABCDBContextIntegerResultForStatisticsQuery
- GCC_except_table112
CStrings:
+ "Failed to check statistics: No database connection available"
+ "Failed to prepare statistics query: (%d) %{public}s, sql: %{public}@"
+ "Failed to run statistics query: (%d) %{public}s, sql: %{public}@"
+ "Person indexes are missing statistics. Should analyze database."
+ "SELECT EXISTS (SELECT 1 FROM ABPerson);"
+ "SELECT count() FROM sqlite_master AS m WHERE m.type = 'index' AND m.tbl_name = 'ABPerson' AND NOT EXISTS (SELECT 1 FROM sqlite_stat1 AS s WHERE s.idx = m.name);"
+ "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'sqlite_stat1';"
```
