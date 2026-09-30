## ProactiveSupport

> `/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport`

```diff

-414.0.0.0.0
-  __TEXT.__text: 0x62a74
+415.1.0.0.0
+  __TEXT.__text: 0x62bf8
   __TEXT.__auth_stubs: 0x2120
-  __TEXT.__objc_methlist: 0x3d54
-  __TEXT.__const: 0xc8b
+  __TEXT.__objc_methlist: 0x3da4
+  __TEXT.__const: 0xc93
   __TEXT.__objc_databytes: 0x1
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_capture: 0xac

   __TEXT.__gcc_except_tab: 0x1b84
   __TEXT.__oslogstring: 0x42fc
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0x1948
+  __TEXT.__unwind_info: 0x1950
   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_classname: 0x98b
-  __TEXT.__objc_methname: 0x8d83
-  __TEXT.__objc_methtype: 0x1a2c
-  __TEXT.__objc_stubs: 0x6120
+  __TEXT.__objc_methname: 0x8e31
+  __TEXT.__objc_methtype: 0x1a71
+  __TEXT.__objc_stubs: 0x61c0
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x19e0
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c0
+  __DATA_CONST.__objc_selrefs: 0x22f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__const: 0xce8
   __AUTH_CONST.__cfstring: 0x4940
-  __AUTH_CONST.__objc_const: 0x6cd0
+  __AUTH_CONST.__objc_const: 0x6d50
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xfa0
   __AUTH.__data: 0x220
   __AUTH.__objc_dataobj: 0x18
-  __DATA.__objc_ivar: 0x418
+  __DATA.__objc_ivar: 0x428
   __DATA.__data: 0x9e8
   __DATA.__bss: 0x1788
   __DATA_DIRTY.__objc_data: 0x1130

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 43E718FE-BA50-3769-AAEC-CDE048F49C29
-  Functions: 1928
-  Symbols:   6203
-  CStrings:  3507
+  UUID: 8E727EDC-DC90-3CF1-B6F7-4A81C5074137
+  Functions: 1934
+  Symbols:   6224
+  CStrings:  3518
 
Symbols:
+ -[_PASSQLTelemetryApi sqlTelemetryContext]
+ -[_PASSQLTelemetryContext bloomHashArray]
+ -[_PASSQLTelemetryContext bloomfilter]
+ -[_PASSQLTelemetryContext filterLog:]
+ -[_PASSQLTelemetryContext initWithConnection:sqlQuery:filterPii:bloomFilter:bloomHashes:]
+ -[_PASSQLTelemetryContext initWithConnectionAndSettings:sqlQuery:filterPii:bloomFilter:bloomHashes:targetProcess:]
+ -[_PASSQLTelemetryContext sqlEventLogRaw]
+ -[_PASSqliteDatabase sqlTelemetryApi]
+ GCC_except_table1392
+ GCC_except_table1393
+ GCC_except_table1401
+ GCC_except_table1404
+ GCC_except_table1408
+ GCC_except_table1447
+ GCC_except_table1455
+ GCC_except_table1562
+ GCC_except_table1563
+ GCC_except_table1589
+ GCC_except_table1591
+ GCC_except_table1599
+ GCC_except_table1610
+ GCC_except_table1617
+ GCC_except_table1624
+ GCC_except_table1625
+ GCC_except_table1636
+ GCC_except_table1644
+ GCC_except_table1655
+ GCC_except_table1672
+ GCC_except_table1673
+ OBJC_IVAR_$__PASSqliteDatabase._bloomFilter
+ OBJC_IVAR_$__PASSqliteDatabase._hashArray
+ _OBJC_IVAR_$__PASSQLTelemetryContext._bloomFilter
+ _OBJC_IVAR_$__PASSQLTelemetryContext._bloomHashes
+ ___33-[_PASSqliteDatabase userVersion]_block_invoke.241
+ ___42-[_PASSqliteDatabase languageForFTSTable:]_block_invoke.278
+ ___58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.128
+ ___58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.132
+ ___Block_byref_object_copy_.3437
+ ___Block_byref_object_copy_.4125
+ ___Block_byref_object_dispose_.3438
+ ___Block_byref_object_dispose_.4126
+ ___block_literal_global.243
+ ___block_literal_global.280
+ ___block_literal_global.3596
+ ___block_literal_global.397.4123
+ ___block_literal_global.4037
+ ___block_literal_global.4127
+ ___block_literal_global.4186
+ ___block_literal_global.49.4038
+ ___block_literal_global.57.4039
+ ___block_literal_global.91
+ _objc_msgSend$bloomFilterInMemoryWithNumberOfValuesN:errorRateP:
+ _objc_msgSend$computeHashesForString:reuse:
+ _objc_msgSend$filterLog:
+ _objc_msgSend$getWithHashes:
+ _objc_msgSend$initWithConnection:sqlQuery:filterPii:bloomFilter:bloomHashes:
+ _objc_msgSend$initWithConnectionAndSettings:sqlQuery:filterPii:bloomFilter:bloomHashes:targetProcess:
+ _objc_msgSend$setWithHashes:
- -[_PASSQLTelemetryContext initWithConnection:sqlQuery:filterPii:]
- -[_PASSQLTelemetryContext initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:]
- GCC_except_table1387
- GCC_except_table1388
- GCC_except_table1391
- GCC_except_table1399
- GCC_except_table1403
- GCC_except_table1435
- GCC_except_table1449
- GCC_except_table1556
- GCC_except_table1557
- GCC_except_table1583
- GCC_except_table1585
- GCC_except_table1593
- GCC_except_table1604
- GCC_except_table1607
- GCC_except_table1611
- GCC_except_table1618
- GCC_except_table1630
- GCC_except_table1638
- GCC_except_table1643
- GCC_except_table1666
- GCC_except_table1667
- ___33-[_PASSqliteDatabase userVersion]_block_invoke.240
- ___42-[_PASSqliteDatabase languageForFTSTable:]_block_invoke.277
- ___58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.127
- ___58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.131
- ___Block_byref_object_copy_.3442
- ___Block_byref_object_copy_.4074
- ___Block_byref_object_dispose_.3443
- ___Block_byref_object_dispose_.4075
- ___block_literal_global.242
- ___block_literal_global.279
- ___block_literal_global.3578
- ___block_literal_global.397.4072
- ___block_literal_global.3995
- ___block_literal_global.4076
- ___block_literal_global.4135
- ___block_literal_global.49.3996
- ___block_literal_global.57.3997
- ___block_literal_global.90.3939
- _objc_msgSend$initWithConnection:sqlQuery:filterPii:
- _objc_msgSend$initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:
CStrings:
+ "@\"_PASBloomFilterForWriting\""
+ "@\"_PASBloomFilterHashArray\""
+ "@52@0:8^{sqlite3=}16@24B32@36@44"
+ "@60@0:8^{sqlite3=}16@24B32@36@44@52"
+ "_bloomFilter"
+ "_bloomHashes"
+ "_hashArray"
+ "bloomHashArray"
+ "bloomfilter"
+ "filterLog:"
+ "initWithConnection:sqlQuery:filterPii:bloomFilter:bloomHashes:"
+ "initWithConnectionAndSettings:sqlQuery:filterPii:bloomFilter:bloomHashes:targetProcess:"
+ "sqlEventLogRaw"
+ "sqlTelemetryApi"
+ "sqlTelemetryContext"
- "@36@0:8^{sqlite3=}16@24B32"
- "@44@0:8^{sqlite3=}16@24B32@36"
- "initWithConnection:sqlQuery:filterPii:"
- "initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:"

```
