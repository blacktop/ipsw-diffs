## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/Versions/A/HomeKitBackingStore`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x9aa8c
+1278.5.13.4.2
+  __TEXT.__text: 0x9a904
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x4fd8
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x5300
-  __TEXT.__cstring: 0x738e
-  __TEXT.__oslogstring: 0xd16f
-  __TEXT.__unwind_info: 0x1ea8
-  __TEXT.__objc_classname: 0xede
-  __TEXT.__objc_methname: 0xcf5c
-  __TEXT.__objc_methtype: 0x1949
-  __TEXT.__objc_stubs: 0x9980
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x658
+  __TEXT.__objc_methlist: 0x54f4
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x5328
+  __TEXT.__cstring: 0x7382
+  __TEXT.__oslogstring: 0xd1da
+  __TEXT.__unwind_info: 0x1eb0
+  __TEXT.__objc_classname: 0xeed
+  __TEXT.__objc_methname: 0xd0a2
+  __TEXT.__objc_methtype: 0x197d
+  __TEXT.__objc_stubs: 0x9aa0
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2cf8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0xb0
+  __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x30d0
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0xb588
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0xadd0
+  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x5c8
-  __DATA.__data: 0xa18
+  __DATA.__objc_ivar: 0x5cc
+  __DATA.__data: 0x8b0
   __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation
+  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/Versions/A/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4897A434-A218-30B8-A5D8-ABB40B9ACEE1
-  Functions: 2208
-  Symbols:   5806
-  CStrings:  4684
+  UUID: 41E001BD-E520-33D0-8ABE-ED8F01FEA5E8
+  Functions: 2212
+  Symbols:   5829
+  CStrings:  4696
 
Symbols:
+ -[HMBSQLContext _clearPreparedStatementsCache]
+ -[HMBSQLContext _configureMemoryPressureHandler]
+ -[HMBSQLContext initWithURL:preparedStatementsCache:memoryMonitor:]
+ -[HMBSQLContext memoryMonitor:didReceiveMemoryEvent:]
+ -[HMBSQLContext memoryMonitor]
+ GCC_except_table1001
+ GCC_except_table1020
+ GCC_except_table1021
+ GCC_except_table1029
+ GCC_except_table1031
+ GCC_except_table1033
+ GCC_except_table1042
+ GCC_except_table1046
+ GCC_except_table1053
+ GCC_except_table1063
+ GCC_except_table1064
+ GCC_except_table107
+ GCC_except_table1073
+ GCC_except_table1076
+ GCC_except_table1105
+ GCC_except_table111
+ GCC_except_table1113
+ GCC_except_table1121
+ GCC_except_table1131
+ GCC_except_table1225
+ GCC_except_table1254
+ GCC_except_table1256
+ GCC_except_table1257
+ GCC_except_table1258
+ GCC_except_table1339
+ GCC_except_table1346
+ GCC_except_table1371
+ GCC_except_table1381
+ GCC_except_table1383
+ GCC_except_table1385
+ GCC_except_table1389
+ GCC_except_table1418
+ GCC_except_table1419
+ GCC_except_table142
+ GCC_except_table1420
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1436
+ GCC_except_table1443
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1449
+ GCC_except_table1458
+ GCC_except_table1475
+ GCC_except_table1493
+ GCC_except_table1497
+ GCC_except_table1557
+ GCC_except_table1561
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1569
+ GCC_except_table1584
+ GCC_except_table1619
+ GCC_except_table1621
+ GCC_except_table1645
+ GCC_except_table1667
+ GCC_except_table1687
+ GCC_except_table1701
+ GCC_except_table1703
+ GCC_except_table1705
+ GCC_except_table174
+ GCC_except_table1776
+ GCC_except_table1777
+ GCC_except_table1778
+ GCC_except_table178
+ GCC_except_table1780
+ GCC_except_table1781
+ GCC_except_table1810
+ GCC_except_table1811
+ GCC_except_table1812
+ GCC_except_table182
+ GCC_except_table1822
+ GCC_except_table184
+ GCC_except_table1843
+ GCC_except_table1857
+ GCC_except_table1859
+ GCC_except_table1861
+ GCC_except_table1864
+ GCC_except_table1866
+ GCC_except_table1868
+ GCC_except_table1887
+ GCC_except_table1890
+ GCC_except_table1892
+ GCC_except_table1899
+ GCC_except_table1901
+ GCC_except_table1906
+ GCC_except_table1915
+ GCC_except_table1917
+ GCC_except_table1919
+ GCC_except_table1924
+ GCC_except_table1926
+ GCC_except_table1928
+ GCC_except_table1931
+ GCC_except_table1936
+ GCC_except_table1945
+ GCC_except_table1947
+ GCC_except_table1952
+ GCC_except_table1955
+ GCC_except_table1957
+ GCC_except_table1994
+ GCC_except_table1997
+ GCC_except_table2002
+ GCC_except_table2005
+ GCC_except_table2024
+ GCC_except_table2027
+ GCC_except_table203
+ GCC_except_table2032
+ GCC_except_table2034
+ GCC_except_table2036
+ GCC_except_table2053
+ GCC_except_table2055
+ GCC_except_table2057
+ GCC_except_table209
+ GCC_except_table2178
+ GCC_except_table2183
+ GCC_except_table2188
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2197
+ GCC_except_table2208
+ GCC_except_table2210
+ GCC_except_table243
+ GCC_except_table247
+ GCC_except_table260
+ GCC_except_table277
+ GCC_except_table36
+ GCC_except_table370
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table386
+ GCC_except_table447
+ GCC_except_table481
+ GCC_except_table499
+ GCC_except_table508
+ GCC_except_table509
+ GCC_except_table510
+ GCC_except_table511
+ GCC_except_table53
+ GCC_except_table537
+ GCC_except_table54
+ GCC_except_table549
+ GCC_except_table618
+ GCC_except_table628
+ GCC_except_table631
+ GCC_except_table646
+ GCC_except_table657
+ GCC_except_table709
+ GCC_except_table755
+ GCC_except_table776
+ GCC_except_table780
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table786
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table813
+ GCC_except_table814
+ GCC_except_table815
+ GCC_except_table865
+ GCC_except_table867
+ GCC_except_table88
+ GCC_except_table923
+ GCC_except_table925
+ GCC_except_table940
+ GCC_except_table951
+ GCC_except_table963
+ GCC_except_table964
+ OBJC_IVAR_$_HMBSQLContext._memoryMonitor
+ _OBJC_CLASS_$_HMFMemoryMonitor
+ __Block_byref_object_copy_.1725
+ __Block_byref_object_copy_.1800
+ __Block_byref_object_copy_.2201
+ __Block_byref_object_copy_.2598
+ __Block_byref_object_copy_.3434
+ __Block_byref_object_copy_.4056
+ __Block_byref_object_copy_.4627
+ __Block_byref_object_copy_.5294
+ __Block_byref_object_copy_.538
+ __Block_byref_object_copy_.5511
+ __Block_byref_object_copy_.5743
+ __Block_byref_object_copy_.5875
+ __Block_byref_object_copy_.6450
+ __Block_byref_object_copy_.6582
+ __Block_byref_object_copy_.6671
+ __Block_byref_object_copy_.6883
+ __Block_byref_object_copy_.695
+ __Block_byref_object_copy_.7507
+ __Block_byref_object_copy_.7681
+ __Block_byref_object_copy_.7901
+ __Block_byref_object_dispose_.1726
+ __Block_byref_object_dispose_.1801
+ __Block_byref_object_dispose_.2202
+ __Block_byref_object_dispose_.2599
+ __Block_byref_object_dispose_.3435
+ __Block_byref_object_dispose_.4057
+ __Block_byref_object_dispose_.4628
+ __Block_byref_object_dispose_.5295
+ __Block_byref_object_dispose_.539
+ __Block_byref_object_dispose_.5512
+ __Block_byref_object_dispose_.5744
+ __Block_byref_object_dispose_.5876
+ __Block_byref_object_dispose_.6451
+ __Block_byref_object_dispose_.6583
+ __Block_byref_object_dispose_.6672
+ __Block_byref_object_dispose_.6884
+ __Block_byref_object_dispose_.696
+ __Block_byref_object_dispose_.7508
+ __Block_byref_object_dispose_.7682
+ __Block_byref_object_dispose_.7902
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFMemoryObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFMemoryObserver
+ __OBJC_$_PROTOCOL_REFS_HMFMemoryObserver
+ __OBJC_LABEL_PROTOCOL_$_HMFMemoryObserver
+ __OBJC_PROTOCOL_$_HMFMemoryObserver
+ _____removeParticipantFromShare_block_invoke
+ ____fetchNextBatch_block_invoke.5297
+ ____fetchNextBatch_block_invoke_2.5300
+ __block_literal_global.108
+ __block_literal_global.12.2994
+ __block_literal_global.12.6381
+ __block_literal_global.120
+ __block_literal_global.126.6401
+ __block_literal_global.1271
+ __block_literal_global.1512
+ __block_literal_global.2028
+ __block_literal_global.2103
+ __block_literal_global.2193
+ __block_literal_global.230
+ __block_literal_global.2329
+ __block_literal_global.2705
+ __block_literal_global.2874
+ __block_literal_global.3001
+ __block_literal_global.3081
+ __block_literal_global.3275
+ __block_literal_global.33
+ __block_literal_global.3452
+ __block_literal_global.36
+ __block_literal_global.3835
+ __block_literal_global.39.5238
+ __block_literal_global.3940
+ __block_literal_global.4167
+ __block_literal_global.4245
+ __block_literal_global.433
+ __block_literal_global.5195
+ __block_literal_global.5992
+ __block_literal_global.6134
+ __block_literal_global.6389
+ __block_literal_global.6483
+ __block_literal_global.6584
+ __block_literal_global.6805
+ __block_literal_global.6887
+ __block_literal_global.7095
+ __block_literal_global.7426
+ __block_literal_global.7512
+ __block_literal_global.7708
+ __block_literal_global.822
+ __block_literal_global.8319
+ __block_literal_global.8463
+ __block_literal_global.977
+ _objc_msgSend$_clearPreparedStatementsCache
+ _objc_msgSend$_configureMemoryPressureHandler
+ _objc_msgSend$addObserver:debounceInterval:events:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithURL:preparedStatementsCache:memoryMonitor:
+ _objc_msgSend$memoryMonitor
+ _objc_msgSend$redactedDescription
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$timeIntervalSince1970
+ hmbProperties._properties.231
+ hmbProperties._properties.3002
+ hmbProperties._properties.3276
+ hmbProperties._properties.6484
+ hmbProperties._properties.7923
+ hmbProperties.onceToken.229
+ hmbProperties.onceToken.3000
+ hmbProperties.onceToken.3274
+ hmbProperties.onceToken.6482
+ hmbProperties.onceToken.7922
+ logCategory._hmf_once_t0.4166
+ logCategory._hmf_once_t7.6804
+ logCategory._hmf_once_v1.4168
+ logCategory._hmf_once_v8.6806
- GCC_except_table1009
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table1023
- GCC_except_table1026
- GCC_except_table1036
- GCC_except_table1037
- GCC_except_table1048
- GCC_except_table1058
- GCC_except_table1059
- GCC_except_table106
- GCC_except_table1068
- GCC_except_table1071
- GCC_except_table1100
- GCC_except_table1108
- GCC_except_table1116
- GCC_except_table1126
- GCC_except_table1220
- GCC_except_table1244
- GCC_except_table1251
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table1334
- GCC_except_table1336
- GCC_except_table1366
- GCC_except_table137
- GCC_except_table1374
- GCC_except_table1376
- GCC_except_table1378
- GCC_except_table1380
- GCC_except_table1408
- GCC_except_table1412
- GCC_except_table1414
- GCC_except_table1415
- GCC_except_table1416
- GCC_except_table1431
- GCC_except_table1433
- GCC_except_table1440
- GCC_except_table1441
- GCC_except_table1444
- GCC_except_table1453
- GCC_except_table1470
- GCC_except_table1482
- GCC_except_table1488
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1562
- GCC_except_table1563
- GCC_except_table1564
- GCC_except_table1578
- GCC_except_table1613
- GCC_except_table1615
- GCC_except_table1639
- GCC_except_table1649
- GCC_except_table1681
- GCC_except_table1685
- GCC_except_table1689
- GCC_except_table169
- GCC_except_table1693
- GCC_except_table173
- GCC_except_table177
- GCC_except_table1770
- GCC_except_table1771
- GCC_except_table1772
- GCC_except_table1774
- GCC_except_table1775
- GCC_except_table179
- GCC_except_table1800
- GCC_except_table1804
- GCC_except_table1805
- GCC_except_table1816
- GCC_except_table1837
- GCC_except_table1847
- GCC_except_table1849
- GCC_except_table1851
- GCC_except_table1858
- GCC_except_table1860
- GCC_except_table1862
- GCC_except_table1881
- GCC_except_table1884
- GCC_except_table1886
- GCC_except_table1891
- GCC_except_table1893
- GCC_except_table1895
- GCC_except_table1900
- GCC_except_table1905
- GCC_except_table1907
- GCC_except_table1916
- GCC_except_table1918
- GCC_except_table1920
- GCC_except_table1925
- GCC_except_table1927
- GCC_except_table1930
- GCC_except_table1935
- GCC_except_table1937
- GCC_except_table1946
- GCC_except_table1951
- GCC_except_table198
- GCC_except_table1988
- GCC_except_table1991
- GCC_except_table1996
- GCC_except_table1999
- GCC_except_table2003
- GCC_except_table2006
- GCC_except_table2026
- GCC_except_table2028
- GCC_except_table2030
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table204
- GCC_except_table2171
- GCC_except_table2172
- GCC_except_table2175
- GCC_except_table2182
- GCC_except_table2184
- GCC_except_table2186
- GCC_except_table2191
- GCC_except_table2202
- GCC_except_table2204
- GCC_except_table238
- GCC_except_table242
- GCC_except_table255
- GCC_except_table272
- GCC_except_table365
- GCC_except_table372
- GCC_except_table374
- GCC_except_table381
- GCC_except_table442
- GCC_except_table476
- GCC_except_table494
- GCC_except_table503
- GCC_except_table504
- GCC_except_table505
- GCC_except_table506
- GCC_except_table51
- GCC_except_table52
- GCC_except_table532
- GCC_except_table544
- GCC_except_table613
- GCC_except_table623
- GCC_except_table626
- GCC_except_table641
- GCC_except_table652
- GCC_except_table704
- GCC_except_table750
- GCC_except_table770
- GCC_except_table771
- GCC_except_table773
- GCC_except_table777
- GCC_except_table781
- GCC_except_table795
- GCC_except_table802
- GCC_except_table804
- GCC_except_table808
- GCC_except_table810
- GCC_except_table83
- GCC_except_table860
- GCC_except_table862
- GCC_except_table918
- GCC_except_table920
- GCC_except_table935
- GCC_except_table936
- GCC_except_table958
- GCC_except_table959
- GCC_except_table97
- GCC_except_table996
- __Block_byref_object_copy_.1726
- __Block_byref_object_copy_.1801
- __Block_byref_object_copy_.2202
- __Block_byref_object_copy_.2593
- __Block_byref_object_copy_.3424
- __Block_byref_object_copy_.4046
- __Block_byref_object_copy_.4618
- __Block_byref_object_copy_.5283
- __Block_byref_object_copy_.5497
- __Block_byref_object_copy_.555
- __Block_byref_object_copy_.5729
- __Block_byref_object_copy_.5861
- __Block_byref_object_copy_.6438
- __Block_byref_object_copy_.6570
- __Block_byref_object_copy_.6659
- __Block_byref_object_copy_.6871
- __Block_byref_object_copy_.717
- __Block_byref_object_copy_.7494
- __Block_byref_object_copy_.7668
- __Block_byref_object_copy_.7885
- __Block_byref_object_dispose_.1727
- __Block_byref_object_dispose_.1802
- __Block_byref_object_dispose_.2203
- __Block_byref_object_dispose_.2594
- __Block_byref_object_dispose_.3425
- __Block_byref_object_dispose_.4047
- __Block_byref_object_dispose_.4619
- __Block_byref_object_dispose_.5284
- __Block_byref_object_dispose_.5498
- __Block_byref_object_dispose_.556
- __Block_byref_object_dispose_.5730
- __Block_byref_object_dispose_.5862
- __Block_byref_object_dispose_.6439
- __Block_byref_object_dispose_.6571
- __Block_byref_object_dispose_.6660
- __Block_byref_object_dispose_.6872
- __Block_byref_object_dispose_.718
- __Block_byref_object_dispose_.7495
- __Block_byref_object_dispose_.7669
- __Block_byref_object_dispose_.7886
- ____fetchNextBatch_block_invoke.5286
- ____fetchNextBatch_block_invoke_2.5289
- __block_literal_global.114
- __block_literal_global.12.2984
- __block_literal_global.12.6367
- __block_literal_global.126.6387
- __block_literal_global.1288
- __block_literal_global.129.6392
- __block_literal_global.1514
- __block_literal_global.2027
- __block_literal_global.2104
- __block_literal_global.2194
- __block_literal_global.22
- __block_literal_global.2325
- __block_literal_global.245
- __block_literal_global.25
- __block_literal_global.2701
- __block_literal_global.28
- __block_literal_global.2860
- __block_literal_global.2991
- __block_literal_global.3071
- __block_literal_global.3265
- __block_literal_global.3442
- __block_literal_global.3826
- __block_literal_global.3930
- __block_literal_global.4159
- __block_literal_global.4237
- __block_literal_global.452
- __block_literal_global.5186
- __block_literal_global.5978
- __block_literal_global.6120
- __block_literal_global.6375
- __block_literal_global.6471
- __block_literal_global.6572
- __block_literal_global.6793
- __block_literal_global.6875
- __block_literal_global.7082
- __block_literal_global.7413
- __block_literal_global.7499
- __block_literal_global.7695
- __block_literal_global.8296
- __block_literal_global.8437
- __block_literal_global.844
- __block_literal_global.993
- _objc_msgSend$initWithVersionString:
- hmbProperties._properties.246
- hmbProperties._properties.2992
- hmbProperties._properties.3266
- hmbProperties._properties.6472
- hmbProperties._properties.7907
- hmbProperties.onceToken.244
- hmbProperties.onceToken.2990
- hmbProperties.onceToken.3264
- hmbProperties.onceToken.6470
- hmbProperties.onceToken.7906
- logCategory._hmf_once_t0.4158
- logCategory._hmf_once_t7.6792
- logCategory._hmf_once_v1.4160
- logCategory._hmf_once_v8.6794
CStrings:
+ "%{public}@Clearing cache after receiving memory pressure notification"
+ "%{public}@Not removing participant from share: No equal participant exists on the share"
+ "%{public}@[%{public}@] Aborting block %lu because there are no records to push"
+ "%{public}@[%{public}@] Failed to abort block %lu: %@"
+ "%{public}@[%{public}@] Lost localZone in __fetchChanges"
+ "%{public}@[%{public}@] Received and decoded record: %{public}@/%{public}@/%@/%{timespec}.*P"
+ "@\"HMFMemoryMonitor\""
+ "HMFMemoryObserver"
+ "T@\"HMFMemoryMonitor\",R,N,V_memoryMonitor"
+ "_clearPreparedStatementsCache"
+ "_configureMemoryPressureHandler"
+ "_memoryMonitor"
+ "addObserver:debounceInterval:events:"
+ "initWithString:"
+ "initWithURL:preparedStatementsCache:memoryMonitor:"
+ "memoryMonitor"
+ "memoryMonitor:didReceiveMemoryEvent:"
+ "redactedDescription"
+ "removeObserver:"
+ "substringToIndex:"
+ "timeIntervalSince1970"
+ "v32@0:8@\"HMFMemoryMonitor\"16q24"
- "%{public}@Didn't find requested participant %@ on share %@. Considering this success"
- "%{public}@Lost localZone in __fetchChanges"
- "%{public}@Not removing participant %@ from share because it doesn't exist on share: %@"
- "%{public}@[%{public}@] No valid records to push; aborting"
- "%{public}@[%{public}@] Received and decoded record: %@/%@"
- "1.0.0"
- "4.0.0"
- "initWithVersionString:"

```
