## HomeKitBackingStore

> `/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`

```diff

-1092.4.10.0.0
-  __TEXT.__text: 0x80898
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x4f9c
+1124.5.8.1.1
+  __TEXT.__text: 0x84bb4
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x4fc4
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x32a4
-  __TEXT.__cstring: 0x723a
-  __TEXT.__oslogstring: 0xca7b
-  __TEXT.__unwind_info: 0x1aec
+  __TEXT.__gcc_except_tab: 0x34d0
+  __TEXT.__cstring: 0x7399
+  __TEXT.__oslogstring: 0xcc09
+  __TEXT.__unwind_info: 0x1adc
   __TEXT.__objc_classname: 0xede
-  __TEXT.__objc_methname: 0xd403
-  __TEXT.__objc_methtype: 0x18e0
+  __TEXT.__objc_methname: 0xd437
+  __TEXT.__objc_methtype: 0x18d7
   __TEXT.__objc_stubs: 0x9a00
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x25a8
+  __DATA_CONST.__const: 0x25f0
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8b18
+  __DATA_CONST.__objc_const: 0x8a70
   __DATA_CONST.__objc_selrefs: 0x2c90
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x598
+  __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__objc_const: 0x30c0
-  __AUTH_CONST.__cfstring: 0x47a0
-  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__objc_const: 0x3150
+  __AUTH_CONST.__cfstring: 0x4840
+  __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x590
-  __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0x6b8
-  __DATA.__data: 0x8e0
-  __DATA.__bss: 0xc0
+  __DATA.__objc_ivar: 0x6a8
+  __DATA.__data: 0x8c0
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 54A0E1CE-08DD-335F-BA1C-DD72936D2359
-  Functions: 2071
-  Symbols:   7658
-  CStrings:  4767
+  UUID: A4A492AB-874C-32BC-9AEA-A314CE006B94
+  Functions: 2077
+  Symbols:   7680
+  CStrings:  4779
 
Symbols:
+ +[HMBLocalSQLContext openWithURL:error:]
+ +[HMBLocalSQLQueryTable logCategory]
+ +[HMBSQLFile _close:]
+ +[HMBSQLFile _openContextWithURL:usingSubclass:error:]
+ +[HMBSQLFile openContextWithURL:usingSubclass:error:]
+ +[HMBSQLStatement logCategory]
+ -[HMBLocalDatabaseConfiguration mutableCopyWithZone:]
+ -[HMBLocalSQLContext initWithURL:]
+ -[HMBLocalSQLContext initializeNewlyCreatedDatabaseWithError:]
+ -[HMBLocalSQLContext prepareWithError:]
+ -[HMBLocalSQLQueryTable logIdentifier]
+ -[HMBMutableLocalDatabaseConfiguration mutableCopyWithZone:]
+ -[HMBSQLContext initWithURL:]
+ -[HMBSQLContext initializeNewlyCreatedDatabaseWithError:]
+ -[HMBSQLContext prepareWithError:]
+ -[HMBSQLStatement logIdentifier]
+ -[NSError(HMB) _hmbHasCKUnderlyingErrorWithCode:]
+ -[NSError(HMB) _hmbIsCKErrorOrHasPartialFailurePassingFilter:]
+ -[NSError(HMB) _hmbIsCKUnderlyingErrorWithCode:]
+ -[NSError(HMB) hmbCKUnderlyingError]
+ -[NSError(HMB) hmbIsCloudKitUnderlyingError]
+ GCC_except_table107
+ GCC_except_table1126
+ GCC_except_table1150
+ GCC_except_table1155
+ GCC_except_table1157
+ GCC_except_table1158
+ GCC_except_table1159
+ GCC_except_table1240
+ GCC_except_table1242
+ GCC_except_table1247
+ GCC_except_table1272
+ GCC_except_table1279
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1308
+ GCC_except_table1309
+ GCC_except_table1310
+ GCC_except_table1324
+ GCC_except_table1331
+ GCC_except_table1332
+ GCC_except_table1335
+ GCC_except_table1344
+ GCC_except_table137
+ GCC_except_table1375
+ GCC_except_table1376
+ GCC_except_table1380
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table1439
+ GCC_except_table1440
+ GCC_except_table145
+ GCC_except_table1450
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table1466
+ GCC_except_table1501
+ GCC_except_table1503
+ GCC_except_table1525
+ GCC_except_table1545
+ GCC_except_table1570
+ GCC_except_table1584
+ GCC_except_table1586
+ GCC_except_table1588
+ GCC_except_table1658
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1662
+ GCC_except_table1663
+ GCC_except_table1685
+ GCC_except_table1713
+ GCC_except_table1718
+ GCC_except_table1733
+ GCC_except_table1739
+ GCC_except_table1763
+ GCC_except_table1776
+ GCC_except_table1778
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1785
+ GCC_except_table1787
+ GCC_except_table1815
+ GCC_except_table1839
+ GCC_except_table1848
+ GCC_except_table1901
+ GCC_except_table1903
+ GCC_except_table1905
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table2040
+ GCC_except_table2045
+ GCC_except_table2053
+ GCC_except_table2055
+ GCC_except_table2056
+ GCC_except_table2060
+ GCC_except_table2071
+ GCC_except_table2073
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table315
+ GCC_except_table317
+ GCC_except_table324
+ GCC_except_table381
+ GCC_except_table413
+ GCC_except_table428
+ GCC_except_table433
+ GCC_except_table442
+ GCC_except_table443
+ GCC_except_table444
+ GCC_except_table445
+ GCC_except_table478
+ GCC_except_table522
+ GCC_except_table54
+ GCC_except_table551
+ GCC_except_table561
+ GCC_except_table564
+ GCC_except_table577
+ GCC_except_table639
+ GCC_except_table683
+ GCC_except_table69
+ GCC_except_table701
+ GCC_except_table704
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table720
+ GCC_except_table725
+ GCC_except_table733
+ GCC_except_table734
+ GCC_except_table735
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table858
+ GCC_except_table863
+ GCC_except_table868
+ GCC_except_table880
+ GCC_except_table881
+ GCC_except_table918
+ GCC_except_table937
+ GCC_except_table941
+ GCC_except_table942
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table954
+ GCC_except_table955
+ GCC_except_table957
+ GCC_except_table959
+ GCC_except_table962
+ GCC_except_table969
+ GCC_except_table979
+ GCC_except_table984
+ GCC_except_table987
+ _CKUnderlyingErrorDomain
+ __HMFPreconditionFailureWithFormat
+ __OBJC_$_CLASS_METHODS_HMBLocalSQLQueryTable
+ __OBJC_$_INSTANCE_METHODS_HMBMutableLocalDatabaseConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_HMBLocalSQLQueryTable
+ __OBJC_CLASS_PROTOCOLS_$_HMBSQLStatement
+ ___30+[HMBSQLStatement logCategory]_block_invoke
+ ___36+[HMBLocalSQLQueryTable logCategory]_block_invoke
+ ___37-[HMBCloudDatabase removeZoneWithID:]_block_invoke.86
+ ___37-[HMBCloudDatabase removeZoneWithID:]_block_invoke.88
+ ___39-[NSError(HMB) hmbIsCKZoneDeletedError]_block_invoke
+ ___54+[HMBSQLFile _openContextWithURL:usingSubclass:error:]_block_invoke
+ ___62-[NSError(HMB) _hmbIsCKErrorOrHasPartialFailurePassingFilter:]_block_invoke
+ ___65-[HMBCloudDatabase _retryCloudKitOperationAfterError:retryBlock:]_block_invoke.89
+ ___Block_byref_object_copy_.1597
+ ___Block_byref_object_copy_.1739
+ ___Block_byref_object_copy_.1988
+ ___Block_byref_object_copy_.2357
+ ___Block_byref_object_copy_.3180
+ ___Block_byref_object_copy_.4323
+ ___Block_byref_object_copy_.4982
+ ___Block_byref_object_copy_.5375
+ ___Block_byref_object_copy_.5498
+ ___Block_byref_object_copy_.554
+ ___Block_byref_object_copy_.6050
+ ___Block_byref_object_copy_.6182
+ ___Block_byref_object_copy_.6267
+ ___Block_byref_object_copy_.6509
+ ___Block_byref_object_copy_.7061
+ ___Block_byref_object_copy_.7290
+ ___Block_byref_object_copy_.7466
+ ___Block_byref_object_copy_.7731
+ ___Block_byref_object_dispose_.1598
+ ___Block_byref_object_dispose_.1740
+ ___Block_byref_object_dispose_.1989
+ ___Block_byref_object_dispose_.2358
+ ___Block_byref_object_dispose_.3181
+ ___Block_byref_object_dispose_.4324
+ ___Block_byref_object_dispose_.4983
+ ___Block_byref_object_dispose_.5376
+ ___Block_byref_object_dispose_.5499
+ ___Block_byref_object_dispose_.555
+ ___Block_byref_object_dispose_.6051
+ ___Block_byref_object_dispose_.6183
+ ___Block_byref_object_dispose_.6268
+ ___Block_byref_object_dispose_.6510
+ ___Block_byref_object_dispose_.7062
+ ___Block_byref_object_dispose_.7291
+ ___Block_byref_object_dispose_.7467
+ ___Block_byref_object_dispose_.7732
+ _____checkLockAcquire_block_invoke.175
+ _____checkLockAcquire_block_invoke.182
+ _____checkLockAcquire_block_invoke_2.189
+ _____fetchNextBatch_block_invoke.4985
+ _____fetchNextBatch_block_invoke_2.4988
+ _____pushChunk_block_invoke.234
+ _____pushChunk_block_invoke.239
+ _____reindexTable_block_invoke.85
+ _____reindexTable_block_invoke.87
+ _____startUp_block_invoke.249
+ _____updateIndexesForClass_block_invoke.193
+ ___block_descriptor_32_e17_B16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e17_B16?0"NSError"8ls32l8
+ ___block_literal_global.1099
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.12.2738
+ ___block_literal_global.12.5995
+ ___block_literal_global.127
+ ___block_literal_global.1331
+ ___block_literal_global.164
+ ___block_literal_global.167
+ ___block_literal_global.181
+ ___block_literal_global.1818
+ ___block_literal_global.1890
+ ___block_literal_global.1982
+ ___block_literal_global.20
+ ___block_literal_global.201
+ ___block_literal_global.2105
+ ___block_literal_global.2462
+ ___block_literal_global.2618
+ ___block_literal_global.262
+ ___block_literal_global.2745
+ ___block_literal_global.2826
+ ___block_literal_global.3022
+ ___block_literal_global.3195
+ ___block_literal_global.3550
+ ___block_literal_global.3660
+ ___block_literal_global.3880
+ ___block_literal_global.3960
+ ___block_literal_global.40
+ ___block_literal_global.437
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.448
+ ___block_literal_global.4888
+ ___block_literal_global.5610
+ ___block_literal_global.5749
+ ___block_literal_global.6003
+ ___block_literal_global.6084
+ ___block_literal_global.6184
+ ___block_literal_global.6398
+ ___block_literal_global.6513
+ ___block_literal_global.656
+ ___block_literal_global.6719
+ ___block_literal_global.7177
+ ___block_literal_global.7484
+ ___block_literal_global.77
+ ___block_literal_global.801
+ ___block_literal_global.8122
+ ___block_literal_global.8263
+ __openContextWithURL:usingSubclass:error:.dispatchOnce
+ __unnamed_array_storage.1135
+ __unnamed_array_storage.1757
+ __unnamed_array_storage.373
+ __unnamed_array_storage.4162
+ __unnamed_array_storage.7495
+ _hmbProperties._properties.128
+ _hmbProperties._properties.2746
+ _hmbProperties._properties.3023
+ _hmbProperties._properties.6085
+ _hmbProperties._properties.7740
+ _hmbProperties.onceToken.126
+ _hmbProperties.onceToken.2744
+ _hmbProperties.onceToken.3021
+ _hmbProperties.onceToken.6083
+ _hmbProperties.onceToken.7739
+ _logCategory._hmf_once_t0.3879
+ _logCategory._hmf_once_t13.7176
+ _logCategory._hmf_once_t16.3212
+ _logCategory._hmf_once_t18
+ _logCategory._hmf_once_t4.2825
+ _logCategory._hmf_once_v1.3881
+ _logCategory._hmf_once_v14.7178
+ _logCategory._hmf_once_v17.3213
+ _logCategory._hmf_once_v19
+ _logCategory._hmf_once_v5.2827
+ _objc_msgSend$_close:
+ _objc_msgSend$_hmbHasCKUnderlyingErrorWithCode:
+ _objc_msgSend$_hmbIsCKErrorOrHasPartialFailurePassingFilter:
+ _objc_msgSend$_hmbIsCKUnderlyingErrorWithCode:
+ _objc_msgSend$_openContextWithURL:usingSubclass:error:
+ _objc_msgSend$hmbCKUnderlyingError
+ _objc_msgSend$hmbIsCloudKitUnderlyingError
+ _objc_msgSend$hmfErrorWithCode:reason:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$initializeNewlyCreatedDatabaseWithError:
+ _objc_msgSend$isCurrentUser
+ _objc_msgSend$openContextWithURL:usingSubclass:error:
+ _objc_msgSend$openWithURL:error:
+ _objc_msgSend$role
- +[HMBLocalSQLContext openWithURL:readOnly:error:]
- +[HMBSQLFile open:readOnly:using:error:]
- +[NSError(HMB) hmbIsUnretriableCKInternalErrorCode:]
- -[HMBLocalDatabaseConfiguration readOnly]
- -[HMBLocalDatabaseConfiguration setReadOnly:]
- -[HMBLocalSQLContext initWithURL:readOnly:]
- -[HMBLocalSQLContext initialize]
- -[HMBLocalSQLContext prepare]
- -[HMBSQLContext _finalize]
- -[HMBSQLContext _prepareFrom:]
- -[HMBSQLContext initWithURL:readOnly:]
- -[HMBSQLContext initialize]
- -[HMBSQLContext mutation]
- -[HMBSQLContext prepare]
- -[HMBSQLContext queue]
- -[HMBSQLContext readOnly]
- -[HMBSQLContext setMutation:]
- -[NSError(HMB) hmbCKInternalError]
- -[NSError(HMB) hmbIsCloudKitInternalError]
- GCC_except_table104
- GCC_except_table1120
- GCC_except_table1144
- GCC_except_table1149
- GCC_except_table1151
- GCC_except_table1152
- GCC_except_table1153
- GCC_except_table1234
- GCC_except_table1236
- GCC_except_table1241
- GCC_except_table1266
- GCC_except_table1273
- GCC_except_table1298
- GCC_except_table1299
- GCC_except_table1301
- GCC_except_table1302
- GCC_except_table1303
- GCC_except_table1318
- GCC_except_table1320
- GCC_except_table1323
- GCC_except_table1325
- GCC_except_table1338
- GCC_except_table134
- GCC_except_table1364
- GCC_except_table1369
- GCC_except_table1374
- GCC_except_table138
- GCC_except_table140
- GCC_except_table142
- GCC_except_table1433
- GCC_except_table1434
- GCC_except_table1438
- GCC_except_table1445
- GCC_except_table1446
- GCC_except_table1460
- GCC_except_table1495
- GCC_except_table1497
- GCC_except_table1519
- GCC_except_table1527
- GCC_except_table1564
- GCC_except_table1568
- GCC_except_table1572
- GCC_except_table1576
- GCC_except_table1648
- GCC_except_table1649
- GCC_except_table1650
- GCC_except_table1652
- GCC_except_table1653
- GCC_except_table1675
- GCC_except_table1707
- GCC_except_table1712
- GCC_except_table1728
- GCC_except_table1729
- GCC_except_table1757
- GCC_except_table1766
- GCC_except_table1768
- GCC_except_table1770
- GCC_except_table1777
- GCC_except_table1779
- GCC_except_table1781
- GCC_except_table1809
- GCC_except_table1833
- GCC_except_table1842
- GCC_except_table1891
- GCC_except_table1895
- GCC_except_table1899
- GCC_except_table195
- GCC_except_table197
- GCC_except_table2033
- GCC_except_table2034
- GCC_except_table2037
- GCC_except_table2044
- GCC_except_table2047
- GCC_except_table2054
- GCC_except_table2065
- GCC_except_table2067
- GCC_except_table210
- GCC_except_table217
- GCC_except_table312
- GCC_except_table314
- GCC_except_table321
- GCC_except_table377
- GCC_except_table407
- GCC_except_table421
- GCC_except_table422
- GCC_except_table436
- GCC_except_table437
- GCC_except_table438
- GCC_except_table439
- GCC_except_table472
- GCC_except_table516
- GCC_except_table53
- GCC_except_table545
- GCC_except_table555
- GCC_except_table558
- GCC_except_table571
- GCC_except_table633
- GCC_except_table66
- GCC_except_table677
- GCC_except_table695
- GCC_except_table696
- GCC_except_table698
- GCC_except_table700
- GCC_except_table703
- GCC_except_table71
- GCC_except_table714
- GCC_except_table719
- GCC_except_table721
- GCC_except_table723
- GCC_except_table728
- GCC_except_table73
- GCC_except_table779
- GCC_except_table781
- GCC_except_table834
- GCC_except_table836
- GCC_except_table851
- GCC_except_table852
- GCC_except_table862
- GCC_except_table874
- GCC_except_table875
- GCC_except_table912
- GCC_except_table924
- GCC_except_table929
- GCC_except_table931
- GCC_except_table938
- GCC_except_table940
- GCC_except_table948
- GCC_except_table949
- GCC_except_table951
- GCC_except_table953
- GCC_except_table956
- GCC_except_table963
- GCC_except_table972
- GCC_except_table973
- GCC_except_table981
- _CKInternalErrorDomain
- _OBJC_IVAR_$_HMBLocalDatabaseConfiguration._readOnly
- _OBJC_IVAR_$_HMBSQLContext._mutation
- _OBJC_IVAR_$_HMBSQLContext._queue
- _OBJC_IVAR_$_HMBSQLContext._readOnly
- ___37-[HMBCloudDatabase removeZoneWithID:]_block_invoke.87
- ___37-[HMBCloudDatabase removeZoneWithID:]_block_invoke.89
- ___40+[HMBSQLFile open:readOnly:using:error:]_block_invoke
- ___65-[HMBCloudDatabase _retryCloudKitOperationAfterError:retryBlock:]_block_invoke.91
- ___Block_byref_object_copy_.1522
- ___Block_byref_object_copy_.1676
- ___Block_byref_object_copy_.1943
- ___Block_byref_object_copy_.2297
- ___Block_byref_object_copy_.3100
- ___Block_byref_object_copy_.4244
- ___Block_byref_object_copy_.4897
- ___Block_byref_object_copy_.5290
- ___Block_byref_object_copy_.531
- ___Block_byref_object_copy_.5411
- ___Block_byref_object_copy_.5956
- ___Block_byref_object_copy_.6089
- ___Block_byref_object_copy_.6173
- ___Block_byref_object_copy_.6414
- ___Block_byref_object_copy_.6980
- ___Block_byref_object_copy_.7181
- ___Block_byref_object_copy_.7361
- ___Block_byref_object_copy_.7615
- ___Block_byref_object_dispose_.1523
- ___Block_byref_object_dispose_.1677
- ___Block_byref_object_dispose_.1944
- ___Block_byref_object_dispose_.2298
- ___Block_byref_object_dispose_.3101
- ___Block_byref_object_dispose_.4245
- ___Block_byref_object_dispose_.4898
- ___Block_byref_object_dispose_.5291
- ___Block_byref_object_dispose_.532
- ___Block_byref_object_dispose_.5412
- ___Block_byref_object_dispose_.5957
- ___Block_byref_object_dispose_.6090
- ___Block_byref_object_dispose_.6174
- ___Block_byref_object_dispose_.6415
- ___Block_byref_object_dispose_.6981
- ___Block_byref_object_dispose_.7182
- ___Block_byref_object_dispose_.7362
- ___Block_byref_object_dispose_.7616
- _____checkLockAcquire_block_invoke.174
- _____checkLockAcquire_block_invoke.181
- _____checkLockAcquire_block_invoke_2.188
- _____fetchNextBatch_block_invoke.4900
- _____fetchNextBatch_block_invoke_2.4903
- _____pushChunk_block_invoke.233
- _____pushChunk_block_invoke.238
- _____reindexTable_block_invoke.84
- _____reindexTable_block_invoke.86
- _____startUp_block_invoke.248
- _____updateIndexesForClass_block_invoke.144
- ___block_literal_global.103
- ___block_literal_global.107
- ___block_literal_global.1078
- ___block_literal_global.117
- ___block_literal_global.12.2674
- ___block_literal_global.12.5903
- ___block_literal_global.1260
- ___block_literal_global.132
- ___block_literal_global.1766
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.1846
- ___block_literal_global.1937
- ___block_literal_global.2059
- ___block_literal_global.2391
- ___block_literal_global.2554
- ___block_literal_global.261
- ___block_literal_global.2681
- ___block_literal_global.2759
- ___block_literal_global.2954
- ___block_literal_global.3115
- ___block_literal_global.3479
- ___block_literal_global.3589
- ___block_literal_global.3806
- ___block_literal_global.3887
- ___block_literal_global.436
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.447
- ___block_literal_global.4803
- ___block_literal_global.5519
- ___block_literal_global.5656
- ___block_literal_global.5911
- ___block_literal_global.5990
- ___block_literal_global.6091
- ___block_literal_global.630
- ___block_literal_global.6303
- ___block_literal_global.6418
- ___block_literal_global.6621
- ___block_literal_global.7071
- ___block_literal_global.7378
- ___block_literal_global.76
- ___block_literal_global.776
- ___block_literal_global.8016
- ___block_literal_global.8166
- __unnamed_array_storage.1114
- __unnamed_array_storage.1696
- __unnamed_array_storage.369
- __unnamed_array_storage.4083
- __unnamed_array_storage.7392
- _hmbProperties._properties.104
- _hmbProperties._properties.2682
- _hmbProperties._properties.2955
- _hmbProperties._properties.5991
- _hmbProperties._properties.7624
- _hmbProperties.onceToken.102
- _hmbProperties.onceToken.2680
- _hmbProperties.onceToken.2953
- _hmbProperties.onceToken.5989
- _hmbProperties.onceToken.7623
- _logCategory._hmf_once_t0.3805
- _logCategory._hmf_once_t16.3132
- _logCategory._hmf_once_t5.7070
- _logCategory._hmf_once_v1.3807
- _logCategory._hmf_once_v17.3133
- _logCategory._hmf_once_v6.7072
- _objc_msgSend$_finalize
- _objc_msgSend$_prepareFrom:
- _objc_msgSend$hashTableWithOptions:
- _objc_msgSend$hmbCKInternalError
- _objc_msgSend$hmbIsCloudKitInternalError
- _objc_msgSend$hmbIsUnretriableCKInternalErrorCode:
- _objc_msgSend$initWithURL:readOnly:
- _objc_msgSend$initialize
- _objc_msgSend$mutation
- _objc_msgSend$open:readOnly:using:error:
- _objc_msgSend$openWithURL:readOnly:error:
- _objc_msgSend$prepare
- _objc_msgSend$setMutation:
- _objc_msgSend$weakToWeakObjectsMapTable
- _open:readOnly:using:error:.dispatchOnce
CStrings:
+ "\x03\x16"
+ "%{public}@Can't open context %p without creating because no database exists already at %@: %{public}@"
+ "%{public}@Cannot remove participant from share: Cannot remove the current user from the share"
+ "%{public}@Cannot remove participant from share: Cannot remove the owner from a share"
+ "%{public}@Closing SQL context: %@"
+ "%{public}@Closing database for SQL context"
+ "%{public}@Current user participant with non-owner role %ld cannot remove participants from a share"
+ "%{public}@Failed re-open of WAL-enabled context %@: %{public}@"
+ "%{public}@Failed to close database: %s (%d)"
+ "%{public}@Failed to create SQLite datastore %@: %@"
+ "%{public}@Failed to initialize newly created database for context %@: %@"
+ "%{public}@Failed to open context %p at %@: %{public}@"
+ "%{public}@Failed to open existing private cloud zone for removal: %@"
+ "%{public}@Failed to open existing shared cloud zone for removal: %@"
+ "%{public}@Failed to prepare context %@: %{public}@"
+ "%{public}@Failed to prepare context during newly created database initialization: %@"
+ "%{public}@Failed to prepare tables: %@"
+ "%{public}@Failed to set sqlite cache size to %ld: %{public}@"
+ "%{public}@Failed to turn on WAL for context %@: %{public}@"
+ "%{public}@Failed to turn on foreign key enforcement: %{public}@"
+ "%{public}@Finalizing table"
+ "%{public}@Found other context still using database: %@"
+ "%{public}@Migration failed for context %@: %{public}@"
+ "%{public}@Opened SQL context with existing database: %@"
+ "%{public}@Opened SQL context with new database: %@"
+ "%{public}@Opening SQL context"
+ "%{public}@Re-opening newly created database after successfully turning on WAL for context: %@"
+ "Asked to open HMBSQLContext subclass of class %@ while one has already been opened with class %@ and matching URL %@"
+ "B\x11"
+ "B24@0:8@?16"
+ "Cannot remove the current user from the share"
+ "Cannot remove the owner from a share"
+ "Current user participant with non-owner role %ld cannot remove participants from a share"
+ "Finalized called twice on table"
+ "LocalSQLQueryTable"
+ "SQLContext"
+ "SQLStatement"
+ "T@\"NSMutableSet\",R,N,V_userQueries"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N"
+ "Table deallocating before being finalized"
+ "_close:"
+ "_hmbHasCKUnderlyingErrorWithCode:"
+ "_hmbIsCKErrorOrHasPartialFailurePassingFilter:"
+ "_hmbIsCKUnderlyingErrorWithCode:"
+ "_openContextWithURL:usingSubclass:error:"
+ "hmbCKUnderlyingError"
+ "hmbIsCloudKitUnderlyingError"
+ "hmfErrorWithCode:reason:"
+ "initWithURL:"
+ "initializeNewlyCreatedDatabaseWithError:"
+ "isCurrentUser"
+ "openContextWithURL:usingSubclass:error:"
+ "openWithURL:error:"
+ "role"
- "\x02\x17"
- "%{public}@Closing database context: %@"
- "%{public}@Closing sqlite database for context: %@"
- "%{public}@Deallocation called on table for %@ without finalize."
- "%{public}@Failed re-open of WAL-enabled context %@: %@"
- "%{public}@Failed to close database, status: %d"
- "%{public}@Failed to open context %p at %@: %@"
- "%{public}@Failed to open existing private zone for removal: %@"
- "%{public}@Failed to open existing shared zone for removal: %@"
- "%{public}@Failed to prepare context %@: %@"
- "%{public}@Failed to turn on WAL for context %@: %@"
- "%{public}@Finalized called on table %@ twice."
- "%{public}@Found context still using database: %@"
- "%{public}@Have opened a DB in read-only mode with a different schema version than our version (%ld != %ld). This may end badly."
- "%{public}@Migration failed for context %@: %@"
- "%{public}@Newly created sqlite db failed to verify tables: %@"
- "%{public}@Opening new SQL context: %@"
- "%{public}@Returning existing SQL context: %@"
- "%{public}@Successfully turned on WAL for context %@"
- "%{public}@Unable to set hmb sqlite cache size to %ld: %@"
- "%{public}@[HMBSQLFile: %@] Unable to turn on foreign key enforcement: %@"
- "%{public}@finalizing table for: %@"
- "%{public}@unable to instantiate SQLite datastore %@: %@"
- "@44@0:8@16B24#28^@36"
- "B\x12"
- "ReadOnly"
- "SQL"
- "T@\"NSHashTable\",R,N,V_userQueries"
- "T@\"NSOperationQueue\",R,N,V_queue"
- "TB,R,N,V_readOnly"
- "TQ,N,V_mutation"
- "_finalize"
- "_mutation"
- "_prepareFrom:"
- "hashTableWithOptions:"
- "hmbCKInternalError"
- "hmbIsCloudKitInternalError"
- "hmbIsUnretriableCKInternalErrorCode:"
- "initWithURL:readOnly:"
- "initialize"
- "mutation"
- "open:readOnly:using:error:"
- "openWithURL:readOnly:error:"
- "prepare"
- "self.finalized != NO"
- "self.finalized == NO"
- "setMutation:"
- "weakToWeakObjectsMapTable"

```
