## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`

```diff

-1076.2.8.1.1
-  __TEXT.__text: 0x80744
+1092.3.10.1.2
+  __TEXT.__text: 0x80898
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x4fcc
+  __TEXT.__objc_methlist: 0x4f9c
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x32dc
-  __TEXT.__cstring: 0x7216
-  __TEXT.__oslogstring: 0xc904
-  __TEXT.__unwind_info: 0x1b10
-  __TEXT.__objc_classname: 0xef4
-  __TEXT.__objc_methname: 0xd41f
-  __TEXT.__objc_methtype: 0x1907
-  __TEXT.__objc_stubs: 0x9a20
+  __TEXT.__gcc_except_tab: 0x32a4
+  __TEXT.__cstring: 0x723a
+  __TEXT.__oslogstring: 0xca7b
+  __TEXT.__unwind_info: 0x1aec
+  __TEXT.__objc_classname: 0xede
+  __TEXT.__objc_methname: 0xd403
+  __TEXT.__objc_methtype: 0x18e0
+  __TEXT.__objc_stubs: 0x9a00
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x2618
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__const: 0x25a8
+  __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8b90
-  __DATA_CONST.__objc_selrefs: 0x2ca0
+  __DATA_CONST.__objc_const: 0x8b18
+  __DATA_CONST.__objc_selrefs: 0x2c90
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__objc_const: 0x3108
-  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__objc_const: 0x30c0
+  __AUTH_CONST.__cfstring: 0x47a0
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x468
-  __AUTH.__objc_data: 0x870
+  __AUTH.__objc_data: 0x820
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x598
+  __DATA.__objc_classrefs: 0x590
   __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0x6bc
-  __DATA.__data: 0x8c0
-  __DATA.__bss: 0xa8
+  __DATA.__objc_ivar: 0x6b8
+  __DATA.__data: 0x8e0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2080
-  Symbols:   7686
-  CStrings:  4193
+  Functions: 2071
+  Symbols:   7658
+  CStrings:  4194
 
Symbols:
+ +[NSError(sqlite3) errorMessageForSQLite3Context:]
+ -[HMBLocalSQLContext(Queryable) prepareTablesWithError:]
+ -[HMBLocalSQLQueryTable initWithContext:queryModel:]
+ -[HMBLocalSQLQueryTable prepareWithError:]
+ -[NSError(HMB) hmbIsSQLiteDatabaseCorruptedError]
+ GCC_except_table1120
+ GCC_except_table1144
+ GCC_except_table1149
+ GCC_except_table1153
+ GCC_except_table1234
+ GCC_except_table1236
+ GCC_except_table1241
+ GCC_except_table1266
+ GCC_except_table1273
+ GCC_except_table1299
+ GCC_except_table1304
+ GCC_except_table1318
+ GCC_except_table1320
+ GCC_except_table1323
+ GCC_except_table1326
+ GCC_except_table1329
+ GCC_except_table1338
+ GCC_except_table1364
+ GCC_except_table1370
+ GCC_except_table1374
+ GCC_except_table1434
+ GCC_except_table1438
+ GCC_except_table1446
+ GCC_except_table1460
+ GCC_except_table1495
+ GCC_except_table1497
+ GCC_except_table1519
+ GCC_except_table1527
+ GCC_except_table1533
+ GCC_except_table1539
+ GCC_except_table1564
+ GCC_except_table1574
+ GCC_except_table1648
+ GCC_except_table1649
+ GCC_except_table1650
+ GCC_except_table1675
+ GCC_except_table1707
+ GCC_except_table1728
+ GCC_except_table1729
+ GCC_except_table1757
+ GCC_except_table1766
+ GCC_except_table1768
+ GCC_except_table1770
+ GCC_except_table1772
+ GCC_except_table1777
+ GCC_except_table1779
+ GCC_except_table1781
+ GCC_except_table1809
+ GCC_except_table1833
+ GCC_except_table1842
+ GCC_except_table1891
+ GCC_except_table1895
+ GCC_except_table1897
+ GCC_except_table2033
+ GCC_except_table2034
+ GCC_except_table2037
+ GCC_except_table2039
+ GCC_except_table2043
+ GCC_except_table2044
+ GCC_except_table2049
+ GCC_except_table2050
+ GCC_except_table2054
+ GCC_except_table2065
+ GCC_except_table2067
+ GCC_except_table407
+ GCC_except_table422
+ GCC_except_table427
+ GCC_except_table439
+ GCC_except_table472
+ GCC_except_table516
+ GCC_except_table545
+ GCC_except_table555
+ GCC_except_table558
+ GCC_except_table571
+ GCC_except_table633
+ GCC_except_table677
+ GCC_except_table696
+ GCC_except_table698
+ GCC_except_table700
+ GCC_except_table703
+ GCC_except_table706
+ GCC_except_table714
+ GCC_except_table719
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table729
+ GCC_except_table779
+ GCC_except_table781
+ GCC_except_table834
+ GCC_except_table836
+ GCC_except_table852
+ GCC_except_table857
+ GCC_except_table862
+ GCC_except_table875
+ GCC_except_table912
+ GCC_except_table924
+ GCC_except_table931
+ GCC_except_table936
+ GCC_except_table938
+ GCC_except_table940
+ GCC_except_table949
+ GCC_except_table951
+ GCC_except_table953
+ GCC_except_table956
+ GCC_except_table963
+ GCC_except_table973
+ GCC_except_table978
+ GCC_except_table981
+ ___40+[HMBSQLFile open:readOnly:using:error:]_block_invoke
+ ___42-[HMBLocalSQLQueryTable prepareWithError:]_block_invoke
+ ___52-[HMBLocalSQLQueryTable initWithContext:queryModel:]_block_invoke
+ ___52-[HMBLocalSQLQueryTable initWithContext:queryModel:]_block_invoke_2
+ ___56-[HMBLocalSQLContext(Queryable) prepareTablesWithError:]_block_invoke
+ ___56-[HMBLocalSQLContext(Queryable) prepareTablesWithError:]_block_invoke.45
+ ___56-[HMBLocalSQLContext(Queryable) prepareTablesWithError:]_block_invoke.51
+ ___56-[HMBLocalSQLContext(Queryable) prepareTablesWithError:]_block_invoke_2
+ ___Block_byref_object_copy_.1676
+ ___Block_byref_object_copy_.1943
+ ___Block_byref_object_copy_.2297
+ ___Block_byref_object_copy_.3100
+ ___Block_byref_object_copy_.4244
+ ___Block_byref_object_copy_.4897
+ ___Block_byref_object_copy_.5290
+ ___Block_byref_object_copy_.5411
+ ___Block_byref_object_copy_.5956
+ ___Block_byref_object_copy_.6089
+ ___Block_byref_object_copy_.6173
+ ___Block_byref_object_copy_.6414
+ ___Block_byref_object_copy_.6980
+ ___Block_byref_object_copy_.7181
+ ___Block_byref_object_copy_.7361
+ ___Block_byref_object_copy_.7615
+ ___Block_byref_object_dispose_.1677
+ ___Block_byref_object_dispose_.1944
+ ___Block_byref_object_dispose_.2298
+ ___Block_byref_object_dispose_.3101
+ ___Block_byref_object_dispose_.4245
+ ___Block_byref_object_dispose_.4898
+ ___Block_byref_object_dispose_.5291
+ ___Block_byref_object_dispose_.5412
+ ___Block_byref_object_dispose_.5957
+ ___Block_byref_object_dispose_.6090
+ ___Block_byref_object_dispose_.6174
+ ___Block_byref_object_dispose_.6415
+ ___Block_byref_object_dispose_.6981
+ ___Block_byref_object_dispose_.7182
+ ___Block_byref_object_dispose_.7362
+ ___Block_byref_object_dispose_.7616
+ _____fetchNextBatch_block_invoke.4900
+ _____fetchNextBatch_block_invoke_2.4903
+ _____parseExistingTables_block_invoke.83
+ _____updateIndexesForClass_block_invoke.144
+ ___block_literal_global.1078
+ ___block_literal_global.12.2674
+ ___block_literal_global.12.5903
+ ___block_literal_global.1260
+ ___block_literal_global.132
+ ___block_literal_global.1766
+ ___block_literal_global.179
+ ___block_literal_global.182
+ ___block_literal_global.1846
+ ___block_literal_global.1937
+ ___block_literal_global.2059
+ ___block_literal_global.2391
+ ___block_literal_global.2554
+ ___block_literal_global.2681
+ ___block_literal_global.2759
+ ___block_literal_global.2954
+ ___block_literal_global.3115
+ ___block_literal_global.3479
+ ___block_literal_global.3589
+ ___block_literal_global.3806
+ ___block_literal_global.3887
+ ___block_literal_global.4803
+ ___block_literal_global.5519
+ ___block_literal_global.5656
+ ___block_literal_global.5911
+ ___block_literal_global.5990
+ ___block_literal_global.6091
+ ___block_literal_global.6303
+ ___block_literal_global.6418
+ ___block_literal_global.6621
+ ___block_literal_global.7071
+ ___block_literal_global.7378
+ ___block_literal_global.8016
+ ___block_literal_global.8166
+ __unnamed_array_storage.1114
+ __unnamed_array_storage.1696
+ __unnamed_array_storage.4083
+ __unnamed_array_storage.7392
+ _hmbProperties._properties.2682
+ _hmbProperties._properties.2955
+ _hmbProperties._properties.5991
+ _hmbProperties._properties.7624
+ _hmbProperties.onceToken.2680
+ _hmbProperties.onceToken.2953
+ _hmbProperties.onceToken.5989
+ _hmbProperties.onceToken.7623
+ _logCategory._hmf_once_t0.3805
+ _logCategory._hmf_once_t16.3132
+ _logCategory._hmf_once_t23
+ _logCategory._hmf_once_t5.7070
+ _logCategory._hmf_once_v1.3807
+ _logCategory._hmf_once_v17.3133
+ _logCategory._hmf_once_v24
+ _logCategory._hmf_once_v6.7072
+ _objc_msgSend$errorMessageForSQLite3Context:
+ _objc_msgSend$hmbIsSQLiteDatabaseCorruptedError
+ _objc_msgSend$initWithContext:queryModel:
+ _objc_msgSend$prepareTablesWithError:
+ _objc_msgSend$prepareWithError:
+ _open:readOnly:using:error:.dispatchOnce
- +[HMBSQLFile open:]
- +[HMBSQLFile open:readOnly:error:initializer:]
- -[HMBLocalSQLContext(Queryable) prepareTables]
- -[HMBLocalSQLContext(Queryable) verifyTables]
- -[HMBLocalSQLQueryTable initWithContext:queryModel:prepareOnly:]
- -[HMBSQLContextConcrete .cxx_destruct]
- -[HMBSQLContextConcrete initBlock]
- -[HMBSQLContextConcrete initialize]
- -[HMBSQLContextConcrete setInitBlock:]
- GCC_except_table1119
- GCC_except_table1143
- GCC_except_table1148
- GCC_except_table1150
- GCC_except_table1233
- GCC_except_table1235
- GCC_except_table1240
- GCC_except_table1265
- GCC_except_table1272
- GCC_except_table1297
- GCC_except_table1300
- GCC_except_table1317
- GCC_except_table1319
- GCC_except_table1322
- GCC_except_table1324
- GCC_except_table1328
- GCC_except_table1337
- GCC_except_table1363
- GCC_except_table1368
- GCC_except_table1373
- GCC_except_table1432
- GCC_except_table1437
- GCC_except_table1443
- GCC_except_table1459
- GCC_except_table1496
- GCC_except_table1499
- GCC_except_table1523
- GCC_except_table1531
- GCC_except_table1537
- GCC_except_table1543
- GCC_except_table1584
- GCC_except_table1586
- GCC_except_table1651
- GCC_except_table1655
- GCC_except_table1656
- GCC_except_table1678
- GCC_except_table1717
- GCC_except_table1733
- GCC_except_table1740
- GCC_except_table1765
- GCC_except_table1776
- GCC_except_table1778
- GCC_except_table1780
- GCC_except_table1782
- GCC_except_table1785
- GCC_except_table1787
- GCC_except_table1789
- GCC_except_table1817
- GCC_except_table1841
- GCC_except_table1850
- GCC_except_table1903
- GCC_except_table1905
- GCC_except_table1907
- GCC_except_table2041
- GCC_except_table2042
- GCC_except_table2045
- GCC_except_table2051
- GCC_except_table2052
- GCC_except_table2055
- GCC_except_table2057
- GCC_except_table2058
- GCC_except_table2062
- GCC_except_table2073
- GCC_except_table2075
- GCC_except_table406
- GCC_except_table420
- GCC_except_table426
- GCC_except_table435
- GCC_except_table471
- GCC_except_table515
- GCC_except_table544
- GCC_except_table554
- GCC_except_table557
- GCC_except_table570
- GCC_except_table632
- GCC_except_table676
- GCC_except_table694
- GCC_except_table697
- GCC_except_table699
- GCC_except_table701
- GCC_except_table705
- GCC_except_table713
- GCC_except_table718
- GCC_except_table720
- GCC_except_table722
- GCC_except_table726
- GCC_except_table778
- GCC_except_table780
- GCC_except_table833
- GCC_except_table835
- GCC_except_table850
- GCC_except_table856
- GCC_except_table861
- GCC_except_table873
- GCC_except_table911
- GCC_except_table923
- GCC_except_table928
- GCC_except_table934
- GCC_except_table937
- GCC_except_table939
- GCC_except_table947
- GCC_except_table950
- GCC_except_table952
- GCC_except_table955
- GCC_except_table962
- GCC_except_table971
- GCC_except_table977
- GCC_except_table980
- _OBJC_CLASS_$_HMBSQLContextConcrete
- _OBJC_IVAR_$_HMBSQLContextConcrete._initBlock
- _OBJC_METACLASS_$_HMBSQLContextConcrete
- __OBJC_$_INSTANCE_METHODS_HMBSQLContextConcrete
- __OBJC_$_INSTANCE_VARIABLES_HMBSQLContextConcrete
- __OBJC_$_PROP_LIST_HMBSQLContextConcrete
- __OBJC_CLASS_RO_$_HMBSQLContextConcrete
- __OBJC_METACLASS_RO_$_HMBSQLContextConcrete
- ___19+[HMBSQLFile open:]_block_invoke
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke.45
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke.49
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke.53
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke.62
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke_2
- ___45-[HMBLocalSQLContext(Queryable) verifyTables]_block_invoke_3
- ___46-[HMBLocalSQLContext(Queryable) prepareTables]_block_invoke
- ___64-[HMBLocalSQLQueryTable initWithContext:queryModel:prepareOnly:]_block_invoke
- ___64-[HMBLocalSQLQueryTable initWithContext:queryModel:prepareOnly:]_block_invoke_2
- ___64-[HMBLocalSQLQueryTable initWithContext:queryModel:prepareOnly:]_block_invoke_3
- ___Block_byref_object_copy_.1666
- ___Block_byref_object_copy_.1930
- ___Block_byref_object_copy_.2286
- ___Block_byref_object_copy_.3092
- ___Block_byref_object_copy_.4235
- ___Block_byref_object_copy_.4892
- ___Block_byref_object_copy_.5285
- ___Block_byref_object_copy_.5406
- ___Block_byref_object_copy_.5951
- ___Block_byref_object_copy_.6085
- ___Block_byref_object_copy_.6172
- ___Block_byref_object_copy_.6413
- ___Block_byref_object_copy_.6979
- ___Block_byref_object_copy_.7168
- ___Block_byref_object_copy_.7351
- ___Block_byref_object_copy_.7603
- ___Block_byref_object_dispose_.1667
- ___Block_byref_object_dispose_.1931
- ___Block_byref_object_dispose_.2287
- ___Block_byref_object_dispose_.3093
- ___Block_byref_object_dispose_.4236
- ___Block_byref_object_dispose_.4893
- ___Block_byref_object_dispose_.5286
- ___Block_byref_object_dispose_.5407
- ___Block_byref_object_dispose_.5952
- ___Block_byref_object_dispose_.6086
- ___Block_byref_object_dispose_.6173
- ___Block_byref_object_dispose_.6414
- ___Block_byref_object_dispose_.6980
- ___Block_byref_object_dispose_.7169
- ___Block_byref_object_dispose_.7352
- ___Block_byref_object_dispose_.7604
- _____fetchNextBatch_block_invoke.4895
- _____fetchNextBatch_block_invoke_2.4898
- _____parseExistingTables_block_invoke.88
- _____updateIndexesForClass_block_invoke.143
- ___block_descriptor_40_e30_v32?0"HMBModelQuery"8Q16^B24lu32l8
- ___block_descriptor_40_e8_32s_e12_v24?0#8^B16ls32l8
- ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
- ___block_literal_global.1079
- ___block_literal_global.12.2666
- ___block_literal_global.12.5899
- ___block_literal_global.1261
- ___block_literal_global.131
- ___block_literal_global.1760
- ___block_literal_global.1833
- ___block_literal_global.191
- ___block_literal_global.1924
- ___block_literal_global.194
- ___block_literal_global.2045
- ___block_literal_global.2380
- ___block_literal_global.2546
- ___block_literal_global.2673
- ___block_literal_global.2751
- ___block_literal_global.2946
- ___block_literal_global.3107
- ___block_literal_global.3464
- ___block_literal_global.3576
- ___block_literal_global.3799
- ___block_literal_global.3880
- ___block_literal_global.4798
- ___block_literal_global.5514
- ___block_literal_global.5651
- ___block_literal_global.5907
- ___block_literal_global.5985
- ___block_literal_global.6087
- ___block_literal_global.6302
- ___block_literal_global.6417
- ___block_literal_global.6616
- ___block_literal_global.6856
- ___block_literal_global.7364
- ___block_literal_global.8005
- ___block_literal_global.8153
- __unnamed_array_storage.1115
- __unnamed_array_storage.1683
- __unnamed_array_storage.4079
- __unnamed_array_storage.7377
- _hmbProperties._properties.2674
- _hmbProperties._properties.2947
- _hmbProperties._properties.5986
- _hmbProperties._properties.7612
- _hmbProperties.onceToken.2672
- _hmbProperties.onceToken.2945
- _hmbProperties.onceToken.5984
- _hmbProperties.onceToken.7611
- _logCategory._hmf_once_t0.3798
- _logCategory._hmf_once_t16.3124
- _logCategory._hmf_once_t20
- _logCategory._hmf_once_t5.6855
- _logCategory._hmf_once_v1.3800
- _logCategory._hmf_once_v17.3125
- _logCategory._hmf_once_v21
- _logCategory._hmf_once_v6.6857
- _objc_msgSend$initBlock
- _objc_msgSend$initWithContext:queryModel:prepareOnly:
- _objc_msgSend$open:
- _objc_msgSend$prepareTables
- _objc_msgSend$setInitBlock:
- _objc_msgSend$verifyTables
- _open:.dispatchOnce
CStrings:
+ "%{public}@Could not convert SQLite error into NSString: %s"
+ "%{public}@Failed to clean up queryable table: %@"
+ "%{public}@Failed to clean up sentinel index table (not fatal): %@"
+ "%{public}@Failed to clean up sentinel table (not fatal): %@"
+ "%{public}@Failed to create index for query table for %@: %@"
+ "%{public}@Failed to create query table for %@: %@"
+ "%{public}@Failed to prepare query context for %@: %@"
+ "%{public}@Failed to prepare tables after migration: %@"
+ "%{public}@Failing DB open during migration because we might corrupt things (open in read-only)"
+ "%{public}@Newly created sqlite db failed to verify tables: %@"
+ "%{public}@Opening new SQL context: %@"
+ "%{public}@Preparing query contexts for %@"
+ "%{public}@Requiring re-init after migration because all required tables do not exist"
+ "%{public}@Returning existing SQL context: %@"
+ "<NULL SQLite3 error>"
+ "<Unknown SQLite3 error>"
+ "DROP TABLE IF EXISTS %@"
+ "errorMessageForSQLite3Context:"
+ "hmbIsSQLiteDatabaseCorruptedError"
+ "initWithContext:queryModel:"
+ "prepareTablesWithError:"
+ "prepareWithError:"
- "%{public}@Cleaning up sentinel table result (not fatal): %@"
- "%{public}@Failed to clean up queryable table (non-fatal): %@"
- "%{public}@Failing DB open during migration becaues we might corrupt things (open in read-only)"
- "%{public}@Opening database context: %@"
- "%{public}@Preparing query contexts..."
- "%{public}@Reusing existing open database context: %@"
- "%{public}@Unable to prepare query context for class: %@"
- "%{public}@unhandled migration result: %ld"
- "@36@0:8@16#24B32"
- "@44@0:8@16B24^@28@?36"
- "HMBSQLContextConcrete"
- "NULL SQLite3 error for statement"
- "T@?,C,N,V_initBlock"
- "_initBlock"
- "initBlock"
- "initWithContext:queryModel:prepareOnly:"
- "open:"
- "open:readOnly:error:initializer:"
- "prepareTables"
- "setInitBlock:"
- "verifyTables"

```
