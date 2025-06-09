## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.600.7.0.0
-  __TEXT.__text: 0x280840
-  __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0xe07c
-  __TEXT.__const: 0x260a0
+4025.100.95.0.0
+  __TEXT.__text: 0x2a06c4
+  __TEXT.__auth_stubs: 0x1fa0
+  __TEXT.__objc_methlist: 0xe49c
+  __TEXT.__const: 0x26400
   __TEXT.__dlopen_cstrs: 0x277
-  __TEXT.__gcc_except_tab: 0x139bc
-  __TEXT.__cstring: 0x68a30
-  __TEXT.__oslogstring: 0x1b08c
+  __TEXT.__gcc_except_tab: 0x14318
+  __TEXT.__cstring: 0x6a547
+  __TEXT.__oslogstring: 0x1ba8d
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x7120
-  __TEXT.__eh_frame: 0x1cb8
-  __TEXT.__objc_classname: 0x1962
-  __TEXT.__objc_methname: 0x1ecf8
-  __TEXT.__objc_methtype: 0x541c
-  __TEXT.__objc_stubs: 0x14c80
-  __DATA_CONST.__got: 0xb50
-  __DATA_CONST.__const: 0x92a8
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __TEXT.__unwind_info: 0x7028
+  __TEXT.__eh_frame: 0x100
+  __TEXT.__objc_classname: 0x1980
+  __TEXT.__objc_methname: 0x1f694
+  __TEXT.__objc_methtype: 0x4bc2
+  __TEXT.__objc_stubs: 0x15180
+  __DATA_CONST.__got: 0xb20
+  __DATA_CONST.__const: 0x93d0
+  __DATA_CONST.__objc_classlist: 0x700
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c30
+  __DATA_CONST.__objc_selrefs: 0x6e28
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x520
-  __DATA_CONST.__objc_arraydata: 0x10c8
-  __AUTH_CONST.__auth_got: 0xff8
-  __AUTH_CONST.__const: 0x123f0
-  __AUTH_CONST.__cfstring: 0x25620
-  __AUTH_CONST.__objc_const: 0x15250
+  __DATA_CONST.__objc_superrefs: 0x528
+  __DATA_CONST.__objc_arraydata: 0x10e0
+  __AUTH_CONST.__auth_got: 0xfe8
+  __AUTH_CONST.__const: 0x12d20
+  __AUTH_CONST.__cfstring: 0x26000
+  __AUTH_CONST.__objc_const: 0x156b8
   __AUTH_CONST.__objc_arrayobj: 0x20e8
-  __AUTH_CONST.__objc_intobj: 0x1ba8
+  __AUTH_CONST.__objc_intobj: 0x1de8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xeb8
-  __DATA.__data: 0x1968
-  __DATA.__bss: 0xc00
-  __DATA.__common: 0xa5c
-  __DATA_DIRTY.__objc_data: 0x4470
-  __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0x11c8
+  __AUTH.__objc_data: 0x1f40
+  __AUTH.__data: 0x118
+  __DATA.__objc_ivar: 0xef0
+  __DATA.__data: 0xf68
+  __DATA.__bss: 0xc70
+  __DATA.__common: 0x1430
+  __DATA_DIRTY.__objc_data: 0x26c0
+  __DATA_DIRTY.__data: 0x88
+  __DATA_DIRTY.__bss: 0x11d8
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D1D7C7B7-2477-34AC-BAC1-5970B8CCAB9B
-  Functions: 8117
-  Symbols:   24711
-  CStrings:  17373
+  UUID: 9C70757B-F39A-3252-AAEC-D782C7B8C21B
+  Functions: 8264
+  Symbols:   25157
+  CStrings:  17671
 
Symbols:
+ +[ML3Album collectionWithPersistentID:addedToLibrary:]
+ +[ML3Album deleteFromLibrary:deletionType:persistentIDs:count:usingConnection:]
+ +[ML3AlbumArtist collectionWithPersistentID:addedToLibrary:]
+ +[ML3Collection collectionWithPersistentID:addedToLibrary:]
+ +[ML3Container deleteFromLibrary:deletionType:persistentIDs:count:preserveUndeletableEntities:]
+ +[ML3Container sagaIDTreeForPlaylistWithIdentifier:inLibrary:includeUndeletablePlaylists:]
+ +[ML3Container sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:]
+ +[ML3Container userUndeleteablePlaylistPersistentIDSInLibrary:]
+ +[ML3Entity _deleteRowsFromLibraryPinsTableForPersistentIDs:count:library:usingConnection:]
+ +[ML3LibraryPin allProperties]
+ +[ML3LibraryPin databaseTable]
+ +[ML3LibraryPin defaultOrderingTerms]
+ +[ML3LibraryPin predisambiguatedProperties]
+ +[ML3LibraryPin revisionTrackingCode]
+ -[MIPLibraryPin .cxx_destruct]
+ -[MIPLibraryPin cloudItemID]
+ -[MIPLibraryPin cloudLibraryID]
+ -[MIPLibraryPin copyTo:]
+ -[MIPLibraryPin copyWithZone:]
+ -[MIPLibraryPin defaultAction]
+ -[MIPLibraryPin description]
+ -[MIPLibraryPin dictionaryRepresentation]
+ -[MIPLibraryPin entityType]
+ -[MIPLibraryPin hasCloudItemID]
+ -[MIPLibraryPin hasCloudLibraryID]
+ -[MIPLibraryPin hasDefaultAction]
+ -[MIPLibraryPin hasEntityType]
+ -[MIPLibraryPin hasPositionUUID]
+ -[MIPLibraryPin hasPosition]
+ -[MIPLibraryPin hash]
+ -[MIPLibraryPin isEqual:]
+ -[MIPLibraryPin mergeFrom:]
+ -[MIPLibraryPin positionUUID]
+ -[MIPLibraryPin position]
+ -[MIPLibraryPin readFrom:]
+ -[MIPLibraryPin setCloudItemID:]
+ -[MIPLibraryPin setCloudLibraryID:]
+ -[MIPLibraryPin setDefaultAction:]
+ -[MIPLibraryPin setEntityType:]
+ -[MIPLibraryPin setHasCloudItemID:]
+ -[MIPLibraryPin setHasDefaultAction:]
+ -[MIPLibraryPin setHasEntityType:]
+ -[MIPLibraryPin setHasPosition:]
+ -[MIPLibraryPin setPosition:]
+ -[MIPLibraryPin setPositionUUID:]
+ -[MIPLibraryPin writeTo:]
+ -[ML3ClientImportItem initWithMultiverseIdentifier:playlistItem:]
+ -[ML3ClientImportItem playlistItem]
+ -[ML3ClientImportServiceSession addContainer:persistentID:]
+ -[ML3ClientImportServiceSession removeContainer:persistentID:]
+ -[ML3ClientImportServiceSession updateContainer:persistentID:]
+ -[ML3ClientImportSession addContainersReturningResult:]
+ -[ML3ClientImportSession removeContainersReturningResult:]
+ -[ML3ClientImportSession sessionFailedToAddContainer:completion:]
+ -[ML3ClientImportSession sessionFailedToRemoveContainer:completion:]
+ -[ML3ClientImportSession sessionFailedToUpdateContainer:completion:]
+ -[ML3ClientImportSession updateContainersReturningResult:]
+ -[ML3Container parentPlaylistPersistentIdsAndNames]
+ -[ML3DAAPImportOperation _processLibraryPinElement:]
+ -[ML3DAAPImportOperation _processMaxPinCount:]
+ -[ML3DAAPImportOperation _processPinCount:]
+ -[ML3DAAPImportOperation libraryPinImportItemFromDAAPElement:]
+ -[ML3DatabaseImport initWithLibraryPath:trackData:playlistData:albumArtistData:albumData:libraryPinsData:clientIdentity:]
+ -[ML3DatabaseImport libraryPinsData]
+ -[ML3ExportSession exportLibraryPinWithCloudItemID:cloudLibraryID:defaultAtion:type:position:positionUUID:]
+ -[ML3MatchImportOperation libraryPinImportItemFromDAAPElement:]
+ -[ML3MusicLibrary enumerateLibraryPinsPersistentIDsAfterRevision:revisionTrackingCode:usingBlock:]
+ -[ML3MusicLibrary hasUserPinnedLibraryEntity]
+ -[ML3MusicLibrary(RemoveSourceOrTracks) _removeLibraryPinsForDeletedTracksUsingConnection:]
+ -[ML3MusicLibrary(Saga) clearSagaForcePerformDeltaSync]
+ -[ML3MusicLibrary(Saga) clearSagaMaxLibraryPinCount]
+ -[ML3MusicLibrary(Saga) sagaForcePerformDeltaSync]
+ -[ML3MusicLibrary(Saga) sagaMaximumLibraryPinCount]
+ -[ML3MusicLibrary(Saga) setSagaForcePerformDeltaSync:]
+ -[ML3MusicLibrary(Saga) setSagaMaximumLibraryPinCount:]
+ -[ML3ProtoSyncExportSession exportLibraryPinWithCloudItemID:cloudLibraryID:defaultAtion:type:position:positionUUID:]
+ -[ML3ProtoSyncImportOperation _processLibraryPinOperation:withImportSession:]
+ -[MSPMediaSyncOperation hasLibraryPin]
+ -[MSPMediaSyncOperation libraryPin]
+ -[MSPMediaSyncOperation setLibraryPin:]
+ -[_ML3DatabaseConnectionSubPool _checkoutConnection:ignoreSubPoolClosedState:]
+ -[_ML3DatabaseConnectionSubPool setSubPoolIsClosed]
+ GCC_except_table1010
+ GCC_except_table1020
+ GCC_except_table1023
+ GCC_except_table1024
+ GCC_except_table1030
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table104
+ GCC_except_table1040
+ GCC_except_table1041
+ GCC_except_table1042
+ GCC_except_table1058
+ GCC_except_table1062
+ GCC_except_table1077
+ GCC_except_table1084
+ GCC_except_table1086
+ GCC_except_table109
+ GCC_except_table1093
+ GCC_except_table1095
+ GCC_except_table1169
+ GCC_except_table119
+ GCC_except_table1206
+ GCC_except_table1226
+ GCC_except_table123
+ GCC_except_table127
+ GCC_except_table1309
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table1390
+ GCC_except_table1397
+ GCC_except_table1404
+ GCC_except_table1413
+ GCC_except_table1426
+ GCC_except_table143
+ GCC_except_table1433
+ GCC_except_table1439
+ GCC_except_table1441
+ GCC_except_table1468
+ GCC_except_table1475
+ GCC_except_table148
+ GCC_except_table1484
+ GCC_except_table1490
+ GCC_except_table1513
+ GCC_except_table1517
+ GCC_except_table1524
+ GCC_except_table1529
+ GCC_except_table154
+ GCC_except_table1550
+ GCC_except_table1552
+ GCC_except_table1554
+ GCC_except_table1564
+ GCC_except_table1568
+ GCC_except_table157
+ GCC_except_table1570
+ GCC_except_table1572
+ GCC_except_table1578
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table1599
+ GCC_except_table1604
+ GCC_except_table161
+ GCC_except_table1615
+ GCC_except_table1640
+ GCC_except_table1657
+ GCC_except_table1659
+ GCC_except_table1682
+ GCC_except_table1688
+ GCC_except_table1713
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1722
+ GCC_except_table1728
+ GCC_except_table1730
+ GCC_except_table1732
+ GCC_except_table1739
+ GCC_except_table1741
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1745
+ GCC_except_table1784
+ GCC_except_table1789
+ GCC_except_table1797
+ GCC_except_table1799
+ GCC_except_table1804
+ GCC_except_table1813
+ GCC_except_table1820
+ GCC_except_table1860
+ GCC_except_table1867
+ GCC_except_table1869
+ GCC_except_table1889
+ GCC_except_table1893
+ GCC_except_table1905
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table1931
+ GCC_except_table1940
+ GCC_except_table1942
+ GCC_except_table2012
+ GCC_except_table2013
+ GCC_except_table2014
+ GCC_except_table2015
+ GCC_except_table2040
+ GCC_except_table2041
+ GCC_except_table2042
+ GCC_except_table2046
+ GCC_except_table2048
+ GCC_except_table2049
+ GCC_except_table2068
+ GCC_except_table2069
+ GCC_except_table2074
+ GCC_except_table2075
+ GCC_except_table2076
+ GCC_except_table2082
+ GCC_except_table2083
+ GCC_except_table2084
+ GCC_except_table2086
+ GCC_except_table2093
+ GCC_except_table2094
+ GCC_except_table2095
+ GCC_except_table2108
+ GCC_except_table2112
+ GCC_except_table2113
+ GCC_except_table2117
+ GCC_except_table2119
+ GCC_except_table2136
+ GCC_except_table2138
+ GCC_except_table2139
+ GCC_except_table2144
+ GCC_except_table2147
+ GCC_except_table2148
+ GCC_except_table2149
+ GCC_except_table2151
+ GCC_except_table2152
+ GCC_except_table2167
+ GCC_except_table2168
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2184
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2197
+ GCC_except_table2200
+ GCC_except_table2201
+ GCC_except_table2203
+ GCC_except_table2204
+ GCC_except_table2206
+ GCC_except_table2207
+ GCC_except_table2208
+ GCC_except_table2209
+ GCC_except_table2210
+ GCC_except_table2211
+ GCC_except_table2212
+ GCC_except_table2221
+ GCC_except_table2224
+ GCC_except_table2225
+ GCC_except_table2226
+ GCC_except_table2227
+ GCC_except_table2228
+ GCC_except_table2234
+ GCC_except_table2235
+ GCC_except_table2236
+ GCC_except_table2252
+ GCC_except_table2260
+ GCC_except_table2263
+ GCC_except_table2264
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2267
+ GCC_except_table2269
+ GCC_except_table2270
+ GCC_except_table2276
+ GCC_except_table2277
+ GCC_except_table2408
+ GCC_except_table2430
+ GCC_except_table2434
+ GCC_except_table2493
+ GCC_except_table2522
+ GCC_except_table2527
+ GCC_except_table2532
+ GCC_except_table2539
+ GCC_except_table2542
+ GCC_except_table2553
+ GCC_except_table2555
+ GCC_except_table2559
+ GCC_except_table2561
+ GCC_except_table2566
+ GCC_except_table2570
+ GCC_except_table2574
+ GCC_except_table2580
+ GCC_except_table2586
+ GCC_except_table2587
+ GCC_except_table2588
+ GCC_except_table2809
+ GCC_except_table2858
+ GCC_except_table2861
+ GCC_except_table2866
+ GCC_except_table2889
+ GCC_except_table2918
+ GCC_except_table2929
+ GCC_except_table2933
+ GCC_except_table2936
+ GCC_except_table2945
+ GCC_except_table2952
+ GCC_except_table2954
+ GCC_except_table2956
+ GCC_except_table2962
+ GCC_except_table2997
+ GCC_except_table3000
+ GCC_except_table3010
+ GCC_except_table3012
+ GCC_except_table3013
+ GCC_except_table3021
+ GCC_except_table3076
+ GCC_except_table3083
+ GCC_except_table3086
+ GCC_except_table3103
+ GCC_except_table3104
+ GCC_except_table3105
+ GCC_except_table3113
+ GCC_except_table3119
+ GCC_except_table3120
+ GCC_except_table3122
+ GCC_except_table3123
+ GCC_except_table3124
+ GCC_except_table3133
+ GCC_except_table3134
+ GCC_except_table3135
+ GCC_except_table3167
+ GCC_except_table3173
+ GCC_except_table3176
+ GCC_except_table3179
+ GCC_except_table3182
+ GCC_except_table3186
+ GCC_except_table3188
+ GCC_except_table3199
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3203
+ GCC_except_table3210
+ GCC_except_table3221
+ GCC_except_table3223
+ GCC_except_table3226
+ GCC_except_table3230
+ GCC_except_table3272
+ GCC_except_table3322
+ GCC_except_table3323
+ GCC_except_table3335
+ GCC_except_table3336
+ GCC_except_table3344
+ GCC_except_table3345
+ GCC_except_table3352
+ GCC_except_table3355
+ GCC_except_table3356
+ GCC_except_table3357
+ GCC_except_table3358
+ GCC_except_table3359
+ GCC_except_table3360
+ GCC_except_table3361
+ GCC_except_table3362
+ GCC_except_table3363
+ GCC_except_table3364
+ GCC_except_table3368
+ GCC_except_table3369
+ GCC_except_table3370
+ GCC_except_table3371
+ GCC_except_table3372
+ GCC_except_table3373
+ GCC_except_table3374
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3382
+ GCC_except_table3384
+ GCC_except_table3385
+ GCC_except_table3393
+ GCC_except_table3396
+ GCC_except_table3397
+ GCC_except_table3402
+ GCC_except_table3405
+ GCC_except_table3406
+ GCC_except_table3407
+ GCC_except_table3408
+ GCC_except_table3409
+ GCC_except_table3410
+ GCC_except_table3415
+ GCC_except_table3416
+ GCC_except_table3417
+ GCC_except_table3418
+ GCC_except_table3419
+ GCC_except_table3433
+ GCC_except_table3458
+ GCC_except_table3493
+ GCC_except_table3792
+ GCC_except_table3802
+ GCC_except_table3804
+ GCC_except_table382
+ GCC_except_table3827
+ GCC_except_table3829
+ GCC_except_table3839
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table3998
+ GCC_except_table4002
+ GCC_except_table4007
+ GCC_except_table4013
+ GCC_except_table4022
+ GCC_except_table4025
+ GCC_except_table4026
+ GCC_except_table4027
+ GCC_except_table403
+ GCC_except_table4032
+ GCC_except_table4040
+ GCC_except_table4051
+ GCC_except_table4075
+ GCC_except_table4080
+ GCC_except_table4083
+ GCC_except_table4086
+ GCC_except_table4090
+ GCC_except_table4094
+ GCC_except_table4098
+ GCC_except_table4101
+ GCC_except_table4104
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table4183
+ GCC_except_table4186
+ GCC_except_table423
+ GCC_except_table424
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table4283
+ GCC_except_table429
+ GCC_except_table4297
+ GCC_except_table4299
+ GCC_except_table430
+ GCC_except_table4301
+ GCC_except_table4302
+ GCC_except_table4303
+ GCC_except_table4306
+ GCC_except_table4312
+ GCC_except_table4317
+ GCC_except_table4321
+ GCC_except_table4340
+ GCC_except_table4342
+ GCC_except_table435
+ GCC_except_table445
+ GCC_except_table447
+ GCC_except_table4520
+ GCC_except_table4534
+ GCC_except_table4535
+ GCC_except_table4536
+ GCC_except_table4542
+ GCC_except_table460
+ GCC_except_table4609
+ GCC_except_table4610
+ GCC_except_table4611
+ GCC_except_table4612
+ GCC_except_table4616
+ GCC_except_table4625
+ GCC_except_table4627
+ GCC_except_table4637
+ GCC_except_table4641
+ GCC_except_table4646
+ GCC_except_table466
+ GCC_except_table4661
+ GCC_except_table4662
+ GCC_except_table4767
+ GCC_except_table4770
+ GCC_except_table4774
+ GCC_except_table4777
+ GCC_except_table4795
+ GCC_except_table4796
+ GCC_except_table4798
+ GCC_except_table4914
+ GCC_except_table4916
+ GCC_except_table4920
+ GCC_except_table4924
+ GCC_except_table4925
+ GCC_except_table5013
+ GCC_except_table5018
+ GCC_except_table5022
+ GCC_except_table5026
+ GCC_except_table5040
+ GCC_except_table5045
+ GCC_except_table5048
+ GCC_except_table5053
+ GCC_except_table5054
+ GCC_except_table5056
+ GCC_except_table5057
+ GCC_except_table5058
+ GCC_except_table5059
+ GCC_except_table5063
+ GCC_except_table5065
+ GCC_except_table5068
+ GCC_except_table507
+ GCC_except_table5070
+ GCC_except_table5072
+ GCC_except_table5073
+ GCC_except_table5074
+ GCC_except_table5075
+ GCC_except_table5076
+ GCC_except_table5079
+ GCC_except_table5080
+ GCC_except_table509
+ GCC_except_table5092
+ GCC_except_table510
+ GCC_except_table5135
+ GCC_except_table5139
+ GCC_except_table5141
+ GCC_except_table5143
+ GCC_except_table5145
+ GCC_except_table5148
+ GCC_except_table5150
+ GCC_except_table5153
+ GCC_except_table5155
+ GCC_except_table5159
+ GCC_except_table5161
+ GCC_except_table5168
+ GCC_except_table5196
+ GCC_except_table5201
+ GCC_except_table5206
+ GCC_except_table5215
+ GCC_except_table5216
+ GCC_except_table5217
+ GCC_except_table5219
+ GCC_except_table5224
+ GCC_except_table5230
+ GCC_except_table5296
+ GCC_except_table5298
+ GCC_except_table5299
+ GCC_except_table5301
+ GCC_except_table5303
+ GCC_except_table5393
+ GCC_except_table5396
+ GCC_except_table5397
+ GCC_except_table5401
+ GCC_except_table5402
+ GCC_except_table5403
+ GCC_except_table5417
+ GCC_except_table5418
+ GCC_except_table5419
+ GCC_except_table5423
+ GCC_except_table5430
+ GCC_except_table5432
+ GCC_except_table5434
+ GCC_except_table5435
+ GCC_except_table5436
+ GCC_except_table5437
+ GCC_except_table5441
+ GCC_except_table5442
+ GCC_except_table5456
+ GCC_except_table5492
+ GCC_except_table550
+ GCC_except_table5501
+ GCC_except_table553
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table559
+ GCC_except_table5599
+ GCC_except_table5605
+ GCC_except_table5611
+ GCC_except_table5617
+ GCC_except_table5623
+ GCC_except_table5629
+ GCC_except_table5635
+ GCC_except_table5641
+ GCC_except_table5642
+ GCC_except_table5643
+ GCC_except_table5649
+ GCC_except_table5650
+ GCC_except_table5656
+ GCC_except_table5662
+ GCC_except_table5668
+ GCC_except_table5676
+ GCC_except_table5683
+ GCC_except_table5689
+ GCC_except_table569
+ GCC_except_table5692
+ GCC_except_table570
+ GCC_except_table5718
+ GCC_except_table573
+ GCC_except_table5746
+ GCC_except_table5754
+ GCC_except_table5767
+ GCC_except_table5775
+ GCC_except_table5803
+ GCC_except_table581
+ GCC_except_table5862
+ GCC_except_table5881
+ GCC_except_table5884
+ GCC_except_table5887
+ GCC_except_table589
+ GCC_except_table5894
+ GCC_except_table5895
+ GCC_except_table5897
+ GCC_except_table591
+ GCC_except_table5923
+ GCC_except_table5924
+ GCC_except_table5925
+ GCC_except_table5926
+ GCC_except_table5931
+ GCC_except_table5932
+ GCC_except_table5961
+ GCC_except_table5985
+ GCC_except_table5988
+ GCC_except_table5990
+ GCC_except_table5993
+ GCC_except_table5995
+ GCC_except_table6004
+ GCC_except_table604
+ GCC_except_table6046
+ GCC_except_table6092
+ GCC_except_table6093
+ GCC_except_table6094
+ GCC_except_table6120
+ GCC_except_table6121
+ GCC_except_table6123
+ GCC_except_table6124
+ GCC_except_table6126
+ GCC_except_table6128
+ GCC_except_table6129
+ GCC_except_table6130
+ GCC_except_table6131
+ GCC_except_table6133
+ GCC_except_table6134
+ GCC_except_table6135
+ GCC_except_table6138
+ GCC_except_table6139
+ GCC_except_table614
+ GCC_except_table6143
+ GCC_except_table6148
+ GCC_except_table6151
+ GCC_except_table6152
+ GCC_except_table6153
+ GCC_except_table6154
+ GCC_except_table6155
+ GCC_except_table6157
+ GCC_except_table6159
+ GCC_except_table6160
+ GCC_except_table6161
+ GCC_except_table6165
+ GCC_except_table6166
+ GCC_except_table6167
+ GCC_except_table6168
+ GCC_except_table617
+ GCC_except_table6171
+ GCC_except_table6172
+ GCC_except_table6174
+ GCC_except_table6175
+ GCC_except_table6176
+ GCC_except_table6177
+ GCC_except_table6179
+ GCC_except_table618
+ GCC_except_table6180
+ GCC_except_table6181
+ GCC_except_table6182
+ GCC_except_table6192
+ GCC_except_table6195
+ GCC_except_table6196
+ GCC_except_table621
+ GCC_except_table6225
+ GCC_except_table6229
+ GCC_except_table6231
+ GCC_except_table6237
+ GCC_except_table6288
+ GCC_except_table6289
+ GCC_except_table629
+ GCC_except_table632
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6349
+ GCC_except_table6350
+ GCC_except_table6351
+ GCC_except_table6352
+ GCC_except_table6353
+ GCC_except_table6354
+ GCC_except_table6362
+ GCC_except_table6364
+ GCC_except_table6365
+ GCC_except_table6368
+ GCC_except_table6369
+ GCC_except_table6371
+ GCC_except_table6372
+ GCC_except_table6374
+ GCC_except_table6375
+ GCC_except_table6380
+ GCC_except_table6394
+ GCC_except_table6395
+ GCC_except_table6396
+ GCC_except_table6398
+ GCC_except_table6402
+ GCC_except_table6411
+ GCC_except_table6419
+ GCC_except_table6424
+ GCC_except_table6434
+ GCC_except_table6440
+ GCC_except_table6443
+ GCC_except_table6445
+ GCC_except_table6451
+ GCC_except_table6452
+ GCC_except_table6453
+ GCC_except_table6454
+ GCC_except_table6455
+ GCC_except_table6456
+ GCC_except_table6457
+ GCC_except_table6458
+ GCC_except_table6468
+ GCC_except_table6470
+ GCC_except_table6474
+ GCC_except_table6482
+ GCC_except_table6487
+ GCC_except_table6492
+ GCC_except_table6493
+ GCC_except_table6496
+ GCC_except_table6497
+ GCC_except_table651
+ GCC_except_table6515
+ GCC_except_table652
+ GCC_except_table6525
+ GCC_except_table6526
+ GCC_except_table6533
+ GCC_except_table6534
+ GCC_except_table6536
+ GCC_except_table6537
+ GCC_except_table6538
+ GCC_except_table6539
+ GCC_except_table654
+ GCC_except_table6540
+ GCC_except_table6541
+ GCC_except_table6542
+ GCC_except_table655
+ GCC_except_table6552
+ GCC_except_table6555
+ GCC_except_table6557
+ GCC_except_table6558
+ GCC_except_table6559
+ GCC_except_table6566
+ GCC_except_table6567
+ GCC_except_table6568
+ GCC_except_table6570
+ GCC_except_table6571
+ GCC_except_table6572
+ GCC_except_table6574
+ GCC_except_table6575
+ GCC_except_table6577
+ GCC_except_table6578
+ GCC_except_table6579
+ GCC_except_table6581
+ GCC_except_table6582
+ GCC_except_table6583
+ GCC_except_table6586
+ GCC_except_table6589
+ GCC_except_table659
+ GCC_except_table6590
+ GCC_except_table6598
+ GCC_except_table6602
+ GCC_except_table6604
+ GCC_except_table6606
+ GCC_except_table6608
+ GCC_except_table6623
+ GCC_except_table6627
+ GCC_except_table6631
+ GCC_except_table6633
+ GCC_except_table6635
+ GCC_except_table6637
+ GCC_except_table6639
+ GCC_except_table6641
+ GCC_except_table6643
+ GCC_except_table6645
+ GCC_except_table6646
+ GCC_except_table665
+ GCC_except_table672
+ GCC_except_table6771
+ GCC_except_table6776
+ GCC_except_table6786
+ GCC_except_table6787
+ GCC_except_table6788
+ GCC_except_table6791
+ GCC_except_table6792
+ GCC_except_table6794
+ GCC_except_table6809
+ GCC_except_table6810
+ GCC_except_table6811
+ GCC_except_table6817
+ GCC_except_table6822
+ GCC_except_table6823
+ GCC_except_table6824
+ GCC_except_table6860
+ GCC_except_table6861
+ GCC_except_table6867
+ GCC_except_table6869
+ GCC_except_table6870
+ GCC_except_table6871
+ GCC_except_table6872
+ GCC_except_table6873
+ GCC_except_table6874
+ GCC_except_table6875
+ GCC_except_table6876
+ GCC_except_table6883
+ GCC_except_table6884
+ GCC_except_table6885
+ GCC_except_table6886
+ GCC_except_table6887
+ GCC_except_table6893
+ GCC_except_table6894
+ GCC_except_table6895
+ GCC_except_table6908
+ GCC_except_table6909
+ GCC_except_table6910
+ GCC_except_table6911
+ GCC_except_table6912
+ GCC_except_table6913
+ GCC_except_table6914
+ GCC_except_table6915
+ GCC_except_table6920
+ GCC_except_table6921
+ GCC_except_table6928
+ GCC_except_table6929
+ GCC_except_table6930
+ GCC_except_table6932
+ GCC_except_table6936
+ GCC_except_table6937
+ GCC_except_table6939
+ GCC_except_table6960
+ GCC_except_table6982
+ GCC_except_table7004
+ GCC_except_table7013
+ GCC_except_table7020
+ GCC_except_table7044
+ GCC_except_table7067
+ GCC_except_table7068
+ GCC_except_table7069
+ GCC_except_table7092
+ GCC_except_table7097
+ GCC_except_table7100
+ GCC_except_table7124
+ GCC_except_table7129
+ GCC_except_table7207
+ GCC_except_table7252
+ GCC_except_table726
+ GCC_except_table727
+ GCC_except_table7272
+ GCC_except_table728
+ GCC_except_table729
+ GCC_except_table735
+ GCC_except_table736
+ GCC_except_table7361
+ GCC_except_table737
+ GCC_except_table738
+ GCC_except_table746
+ GCC_except_table753
+ GCC_except_table7532
+ GCC_except_table7538
+ GCC_except_table7544
+ GCC_except_table7545
+ GCC_except_table7546
+ GCC_except_table756
+ GCC_except_table7561
+ GCC_except_table7565
+ GCC_except_table757
+ GCC_except_table758
+ GCC_except_table761
+ GCC_except_table7611
+ GCC_except_table7617
+ GCC_except_table762
+ GCC_except_table7621
+ GCC_except_table765
+ GCC_except_table786
+ GCC_except_table789
+ GCC_except_table7924
+ GCC_except_table7925
+ GCC_except_table7926
+ GCC_except_table7932
+ GCC_except_table7934
+ GCC_except_table7935
+ GCC_except_table7938
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table808
+ GCC_except_table814
+ GCC_except_table820
+ GCC_except_table826
+ GCC_except_table864
+ GCC_except_table928
+ GCC_except_table93
+ GCC_except_table930
+ GCC_except_table936
+ GCC_except_table963
+ GCC_except_table971
+ GCC_except_table975
+ OBJC_IVAR_$_MIPLibraryPin._cloudItemID
+ OBJC_IVAR_$_MIPLibraryPin._cloudLibraryID
+ OBJC_IVAR_$_MIPLibraryPin._defaultAction
+ OBJC_IVAR_$_MIPLibraryPin._entityType
+ OBJC_IVAR_$_MIPLibraryPin._has
+ OBJC_IVAR_$_MIPLibraryPin._position
+ OBJC_IVAR_$_MIPLibraryPin._positionUUID
+ OBJC_IVAR_$_MSPMediaSyncOperation._libraryPin
+ _CFAllocatorAllocateTyped
+ _MIPLibraryPinReadFrom
+ _ML3MigrationFunction2240032to2240040
+ _ML3MigrationFunction2240040to2300000
+ _ML3MigrationFunction2300000to2300010
+ _ML3MigrationFunction2300010to2300020
+ _ML3TrackPropertyStoreImmersiveDeeplinkURL
+ _MSVFastHexStringFromBytes.hexCharacters.28075
+ _OBJC_CLASS_$_MIPLibraryPin
+ _OBJC_CLASS_$_ML3LibraryPin
+ _OBJC_IVAR_$_ML3ClientImportItem._playlistItem
+ _OBJC_IVAR_$_ML3DAAPImportOperation._maxLibraryPinsCount
+ _OBJC_IVAR_$_ML3DAAPImportOperation._processedLibraryPinsCount
+ _OBJC_IVAR_$_ML3DAAPImportOperation._totalLibraryPinsCount
+ _OBJC_IVAR_$_ML3DatabaseImport._libraryPinsData
+ _OBJC_IVAR_$__ML3DatabaseConnectionSubPool._isSubPoolClosed
+ _OBJC_METACLASS_$_MIPLibraryPin
+ _OBJC_METACLASS_$_ML3LibraryPin
+ __MSV_XXH_XXH32_update.28066
+ __MSV_XXH_XXH64_digest.28071
+ __MSV_XXH_XXH64_update.28067
+ __OBJC_$_CLASS_METHODS_ML3LibraryPin
+ __OBJC_$_INSTANCE_METHODS_MIPLibraryPin
+ __OBJC_$_INSTANCE_VARIABLES_MIPLibraryPin
+ __OBJC_$_PROP_LIST_MIPLibraryPin
+ __OBJC_CLASS_PROTOCOLS_$_MIPLibraryPin
+ __OBJC_CLASS_RO_$_MIPLibraryPin
+ __OBJC_CLASS_RO_$_ML3LibraryPin
+ __OBJC_METACLASS_RO_$_MIPLibraryPin
+ __OBJC_METACLASS_RO_$_ML3LibraryPin
+ __ZN16ML3ImportSession15updateContainerENSt3__110shared_ptrI13ML3ImportItemEEb
+ __ZN16ML3ImportSession21_reconcileLibraryPinsEv
+ __ZN16ML3ImportSession22addLibraryPinnedEntityENSt3__110shared_ptrI13ML3ImportItemEE
+ __ZN16ML3ImportSession34setMaxAllowedLibraryPinnedEntitiesEi
+ __ZN18ML3LibraryPinsDataC2ExxxxxxRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_
+ __ZN28ML3MatchLibraryPinImportItem7isValidEv
+ __ZN28ML3MatchLibraryPinImportItemD0Ev
+ __ZN28ML3MatchLibraryPinImportItemD1Ev
+ __ZN32ML3ProtoSyncLibraryPinImportItem7isValidEv
+ __ZN32ML3ProtoSyncLibraryPinImportItemD0Ev
+ __ZN32ML3ProtoSyncLibraryPinImportItemD1Ev
+ __ZNK28ML3MatchLibraryPinImportItem14getDescriptionEv
+ __ZNK28ML3MatchLibraryPinImportItem14getStringValueEj
+ __ZNK28ML3MatchLibraryPinImportItem15getIntegerValueEj
+ __ZNK28ML3MatchLibraryPinImportItem8hasValueEj
+ __ZNK32ML3ProtoSyncLibraryPinImportItem14getDescriptionEv
+ __ZNK32ML3ProtoSyncLibraryPinImportItem14getStringValueEj
+ __ZNK32ML3ProtoSyncLibraryPinImportItem15getIntegerValueEj
+ __ZNK6ML3CPP7Element11stringValueEv
+ __ZNKSt3__111__copy_implclB8ne200100IPKNS_10shared_ptrI27ML3DatabaseImportDataSourceEES6_PS4_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__copy_implclB8ne200100IPNS_10shared_ptrI13ML3ImportItemEES5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__114default_deleteIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS_10shared_ptrI13ML3ImportItemEEE26_ContainerItemReactionInfoEclB8ne200100EPS5_
+ __ZNKSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNKSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt11range_errorC1B8ne200100EPKc
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110shared_ptrI10ML3CPPDataEC2B8ne200100IS1_Li0EEEPT_
+ __ZNSt3__110shared_ptrI12ML3AlbumDataED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI12ML3GenreDataED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI13ML3ArtistDataED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I25ML3SubscriptionImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I26ML3ContainerItemImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I27ML3ProtoSyncAlbumImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I27ML3ProtoSyncTrackImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I28ML3ContainerAuthorImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I28ML3ITunesSyncAlbumImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I28ML3ITunesSyncTrackImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I28ML3ProtoSyncArtistImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I28ML3ProtoSyncDeleteImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I29ML3ITunesSyncArtistImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I31ML3ProtoSyncContainerImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I32ML3ITunesSyncContainerImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne200100I34ML3ContainerItemReactionImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI15ML3ComposerDataED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI27ML3DatabaseImportDataSourceEC2B8ne200100I36ML3ItemStoreDatabaseImportDataSourceLi0EEEPT_
+ __ZNSt3__110shared_ptrIN6ML3CPP7ElementEE18__enable_weak_thisB8ne200100IS2_S2_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEENS_22__tree_node_destructorINS6_ISH_EEEEED1B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_10shared_ptrI18ML3LibraryPinsDataEEEENS_22__unordered_map_hasherIxS5_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS5_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_10shared_ptrI18ML3LibraryPinsDataEEEENS_22__unordered_map_hasherIxS5_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIxJNS_4pairIxS4_EEEEENSI_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_10shared_ptrI18ML3LibraryPinsDataEEEENS_22__unordered_map_hasherIxS5_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxNS_10shared_ptrI18ML3LibraryPinsDataEEEENS_22__unordered_map_hasherIxS5_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS5_SA_S8_Lb1EEENS_9allocatorIS5_EEED2Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__114__split_bufferIPNS_10shared_ptrIN6ML3CPP6Parser15ParserContainerEEENS_9allocatorIS6_EEE12emplace_backIJRS6_EEEvDpOT_
+ __ZNSt3__115allocate_sharedB8ne200100I12ML3AlbumDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_RiSB_SB_SB_R12ML3NameOrderSB_S4_S4_SA_SB_RbS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_S9_S9_S4_R12ML3NameOrderSC_S4_SA_RbRiS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_SA_SA_S4_R12ML3NameOrderSC_S4_S9_RbiiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I18ML3AlbumImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI12ML3AlbumDataEERNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERbRU8__strongP6NSDataxRxSJ_SE_ELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I18ML3LibraryPinsDataNS_9allocatorIS1_EEJRxS4_13ML3EntityTypeS4_S4_S4_RA1_KcRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I18ML3LibraryPinsDataNS_9allocatorIS1_EEJRxS4_13ML3EntityTypeS4_S4_S4_RNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESB_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I19ML3ArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I29ML3SetCloudIDArtistImportItemNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne200100Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEEEEE7destroyB8ne200100INS_4pairIKS8_SE_EEvLi0EEEvRSI_PT_
+ __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED0B8ne200100Ev
+ __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED1B8ne200100Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_10shared_ptrIN6ML3CPP7ElementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPNS_10shared_ptrIN6ML3CPP6Parser15ParserContainerEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIwEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119__throw_range_errorB8ne200100EPKc
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__optional_copy_baseINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELb0EEC2B8ne200100ERKSC_
+ __ZNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__throw_bad_weak_ptrB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj14ML3ImportValueINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEPvEEEEEclB8ne200100EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIx20ML3CollectionInfoSetEEPvEEEEEclB8ne200100EPS7_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3AlbumDataEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3GenreDataEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ArtistDataEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI15ML3ComposerDataEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI18ML3LibraryPinsDataEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_6vectorINS_4pairIxxEENS1_IS6_EEEEEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__126__throw_bad_variant_accessB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPSE_EEED2B8ne200100Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_10shared_ptrI27ML3DatabaseImportDataSourceEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEC1B8ne200100ERKSJ_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEaSB8ne200100ERKSJ_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExNS_4lessIS6_EENS4_INS_4pairIKS6_xEEEEED1B8ne200100Ev
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEED2Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCache9__advanceB8ne200100Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCacheD1B8ne200100Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE9push_backB8ne200100EOS3_
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPKS3_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPKS3_S9_EEvT_T0_l
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne200100IPKS6_SB_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne200100IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_mapIxyNS_4hashIxEENS_8equal_toIxEENS_9allocatorINS_4pairIKxyEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_mapIyxNS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyxEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__init_with_sizeB8ne200100IPSD_SH_EEvT_T0_m
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE24__emplace_back_slow_pathIJRKSD_EEEPSD_DpOT_
+ __ZNSt3__16vectorINS_4pairIx14ML3ArtworkTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIxxEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEENS6_ISD_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEENS6_ISD_EEE16__init_with_sizeB8ne200100IPKSD_SI_EEvT_T0_m
+ __ZNSt3__16vectorIP11_constraintNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP17_constraint_stateNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE9push_backB8ne200100ERKh
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne200100IPxS5_EEvT_T0_m
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE9push_backB8ne200100EOx
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE9push_backB8ne200100ERKx
+ __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B8ne200100Em
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100ERKy
+ __ZNSt3__18optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEaSB8ne200100IS7_vEERSC_OT_
+ __ZNSt3__19allocatorI18DAAPParserDelegateE9constructB8ne200100IS1_JRU8__strongKP22ML3DAAPImportOperationRNS_10shared_ptrIN6ML3CPP6ParserEEER32ML3DAAPImportOperationEntityTypebEEEvPT_DpOT0_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTI28ML3MatchLibraryPinImportItem
+ __ZTI32ML3ProtoSyncLibraryPinImportItem
+ __ZTINSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEEE
+ __ZTINSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZTINSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZTS28ML3MatchLibraryPinImportItem
+ __ZTS32ML3ProtoSyncLibraryPinImportItem
+ __ZTSNSt3__110shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS1_32ML3ProtoSyncLibraryPinImportItemEE
+ __ZTSNSt3__110shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS1_28ML3MatchLibraryPinImportItemEE
+ __ZTSNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZTV28ML3MatchLibraryPinImportItem
+ __ZTV32ML3ProtoSyncLibraryPinImportItem
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI18ML3LibraryPinsDataNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP28ML3MatchLibraryPinImportItemNS_10shared_ptrI17ML3DAAPImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIP32ML3ProtoSyncLibraryPinImportItemNS_10shared_ptrI13ML3ImportItemE27__shared_ptr_default_deleteIS4_S1_EENS_9allocatorIS1_EEEE
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE38__pinnedEntityDefaultActionDescription
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE38__pinnedEntityDefaultActionDescription.23081
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE38__pinnedEntityDefaultActionDescription.4952
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE9onceToken
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE9onceToken.23080
+ __ZZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinActionE9onceToken.4951
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE29__pinnedEntityTypeDescription
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE29__pinnedEntityTypeDescription.23079
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE29__pinnedEntityTypeDescription.4950
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE9onceToken
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE9onceToken.23078
+ __ZZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityTypeE9onceToken.4948
+ ___103+[ML3Track deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:usingConnection:]_block_invoke.2510
+ ___103-[ML3UpdateSpotlightIndexOperation _indexItemsFromLibrarySinceRevision:targetRevision:completionBlock:]_block_invoke.44
+ ___104+[ML3Entity deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:usingConnection:]_block_invoke.228
+ ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.112
+ ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.117
+ ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.125
+ ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.127
+ ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.95
+ ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke.2538
+ ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke.2544
+ ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke_2.2542
+ ___136-[ML3MusicLibrary enumeratePersistentIDsAfterRevision:revisionTrackingCode:maximumRevisionType:forMediaTypes:inUsersLibrary:usingBlock:]_block_invoke.633
+ ___141-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.689
+ ___143-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.700
+ ___150-[ML3MusicLibrary(RemoveSourceOrTracks) _removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:]_block_invoke.146
+ ___150-[ML3MusicLibrary(RemoveSourceOrTracks) _removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:]_block_invoke.151
+ ___152-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]_block_invoke.696
+ ___43-[ML3RemoveCloudSourcesOperation _execute:]_block_invoke.40
+ ___43-[ML3RemoveCloudSourcesOperation _execute:]_block_invoke.50
+ ___43-[ML3RemoveCloudSourcesOperation _execute:]_block_invoke.68
+ ___43-[ML3UpdateSpotlightIndexOperation execute]_block_invoke.21
+ ___45-[ML3MusicLibrary hasUserPinnedLibraryEntity]_block_invoke
+ ___46-[ML3ClientImportSession _xpcClientConnection]_block_invoke.127
+ ___51-[ML3Container parentPlaylistPersistentIdsAndNames]_block_invoke
+ ___51-[_ML3DatabaseConnectionSubPool setSubPoolIsClosed]_block_invoke
+ ___52-[ML3MusicLibrary removeOrphanedTracksOnlyInCaches:]_block_invoke.766
+ ___54+[ML3Album collectionWithPersistentID:addedToLibrary:]_block_invoke
+ ___55-[ML3ClientImportSession addContainersReturningResult:]_block_invoke
+ ___55-[ML3ClientImportSession addContainersReturningResult:]_block_invoke.23
+ ___58-[ML3ClientImportSession removeContainersReturningResult:]_block_invoke
+ ___58-[ML3ClientImportSession removeContainersReturningResult:]_block_invoke.31
+ ___58-[ML3ClientImportSession updateContainersReturningResult:]_block_invoke
+ ___58-[ML3ClientImportSession updateContainersReturningResult:]_block_invoke.27
+ ___58-[ML3MusicLibrary _closeAndLockCurrentDatabaseConnections]_block_invoke.997
+ ___59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.496
+ ___59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.525
+ ___59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke_2.504
+ ___60+[ML3AlbumArtist collectionWithPersistentID:addedToLibrary:]_block_invoke
+ ___63+[ML3Container userUndeleteablePlaylistPersistentIDSInLibrary:]_block_invoke
+ ___63-[ML3MusicLibrary _removeOrphanedArtworkAssetsUsingConnection:]_block_invoke.967
+ ___65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.943
+ ___65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.956
+ ___71-[ML3DatabaseValidation _validateLibraryDatabaseIfNecessary:withError:]_block_invoke.19
+ ___74-[ML3UpdateSpotlightIndexOperation _batchIndexWithObject:completionBlock:]_block_invoke.49
+ ___76-[ML3MusicLibrary sanitizeSortMapContentsUsingConnection:didSortMapEntries:]_block_invoke.909
+ ___77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.716
+ ___78-[_ML3DatabaseConnectionSubPool _checkoutConnection:ignoreSubPoolClosedState:]_block_invoke
+ ___78-[_ML3DatabaseConnectionSubPool _checkoutConnection:ignoreSubPoolClosedState:]_block_invoke_2
+ ___83-[ML3UpdateSpotlightIndexOperation _createSearchableItemsForTracksWithQuery:error:]_block_invoke.79
+ ___84+[ML3Container sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:]_block_invoke
+ ___84+[ML3Container sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:]_block_invoke_2
+ ___84+[ML3Container sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:]_block_invoke_3
+ ___91-[ML3MusicLibrary(RemoveSourceOrTracks) _removeLibraryPinsForDeletedTracksUsingConnection:]_block_invoke
+ ___91-[ML3MusicLibrary(RemoveSourceOrTracks) _removeLibraryPinsForDeletedTracksUsingConnection:]_block_invoke.172
+ ___94+[ML3Entity incrementRevisionForRevisionTypeContentWithConnection:deletionType:persistentIDs:]_block_invoke
+ ___94-[ML3MusicLibrary performColorAnalysisForArtworkWithConnection:shouldRegenerateColorAnalysis:]_block_invoke.686
+ ___95+[ML3Container deleteFromLibrary:deletionType:persistentIDs:count:preserveUndeletableEntities:]_block_invoke
+ ___95+[ML3Container deleteFromLibrary:deletionType:persistentIDs:count:preserveUndeletableEntities:]_block_invoke_2
+ ___97+[ML3Entity incrementRevisionWithLibrary:persistentID:deletionType:revisionType:usingConnection:]_block_invoke
+ ___98-[ML3MusicLibrary enumerateLibraryPinsPersistentIDsAfterRevision:revisionTrackingCode:usingBlock:]_block_invoke
+ ___98-[ML3MusicLibrary enumerateLibraryPinsPersistentIDsAfterRevision:revisionTrackingCode:usingBlock:]_block_invoke_2
+ ___99-[ML3MusicLibrary enumerateArtworkRelativePathsWithConnection:matchingRelativePathContainer:block:]_block_invoke.673
+ ___Block_byref_object_copy_.10956
+ ___Block_byref_object_copy_.11805
+ ___Block_byref_object_copy_.11910
+ ___Block_byref_object_copy_.12769
+ ___Block_byref_object_copy_.12933
+ ___Block_byref_object_copy_.13334
+ ___Block_byref_object_copy_.13783
+ ___Block_byref_object_copy_.14906
+ ___Block_byref_object_copy_.1572
+ ___Block_byref_object_copy_.17498
+ ___Block_byref_object_copy_.17828
+ ___Block_byref_object_copy_.18361
+ ___Block_byref_object_copy_.18490
+ ___Block_byref_object_copy_.19198
+ ___Block_byref_object_copy_.19620
+ ___Block_byref_object_copy_.19871
+ ___Block_byref_object_copy_.20752
+ ___Block_byref_object_copy_.21110
+ ___Block_byref_object_copy_.22754
+ ___Block_byref_object_copy_.23208
+ ___Block_byref_object_copy_.2414
+ ___Block_byref_object_copy_.2501
+ ___Block_byref_object_copy_.25042
+ ___Block_byref_object_copy_.25120
+ ___Block_byref_object_copy_.25222
+ ___Block_byref_object_copy_.25421
+ ___Block_byref_object_copy_.25732
+ ___Block_byref_object_copy_.26129
+ ___Block_byref_object_copy_.28209
+ ___Block_byref_object_copy_.29027
+ ___Block_byref_object_copy_.3842
+ ___Block_byref_object_copy_.407
+ ___Block_byref_object_copy_.410
+ ___Block_byref_object_copy_.412
+ ___Block_byref_object_copy_.479
+ ___Block_byref_object_copy_.509
+ ___Block_byref_object_copy_.5102
+ ___Block_byref_object_copy_.5289
+ ___Block_byref_object_copy_.530
+ ___Block_byref_object_copy_.594
+ ___Block_byref_object_copy_.6338
+ ___Block_byref_object_copy_.711
+ ___Block_byref_object_copy_.717
+ ___Block_byref_object_copy_.724
+ ___Block_byref_object_copy_.728
+ ___Block_byref_object_copy_.735
+ ___Block_byref_object_copy_.740
+ ___Block_byref_object_copy_.7551
+ ___Block_byref_object_copy_.7641
+ ___Block_byref_object_copy_.8246
+ ___Block_byref_object_copy_.8909
+ ___Block_byref_object_copy_.9385
+ ___Block_byref_object_copy_.9508
+ ___Block_byref_object_copy_.9611
+ ___Block_byref_object_dispose_.10957
+ ___Block_byref_object_dispose_.11806
+ ___Block_byref_object_dispose_.11911
+ ___Block_byref_object_dispose_.12770
+ ___Block_byref_object_dispose_.12934
+ ___Block_byref_object_dispose_.13335
+ ___Block_byref_object_dispose_.13784
+ ___Block_byref_object_dispose_.14907
+ ___Block_byref_object_dispose_.1573
+ ___Block_byref_object_dispose_.17499
+ ___Block_byref_object_dispose_.17829
+ ___Block_byref_object_dispose_.18362
+ ___Block_byref_object_dispose_.18491
+ ___Block_byref_object_dispose_.19199
+ ___Block_byref_object_dispose_.19621
+ ___Block_byref_object_dispose_.19872
+ ___Block_byref_object_dispose_.20753
+ ___Block_byref_object_dispose_.21111
+ ___Block_byref_object_dispose_.22755
+ ___Block_byref_object_dispose_.23209
+ ___Block_byref_object_dispose_.2415
+ ___Block_byref_object_dispose_.2502
+ ___Block_byref_object_dispose_.25043
+ ___Block_byref_object_dispose_.25121
+ ___Block_byref_object_dispose_.25223
+ ___Block_byref_object_dispose_.25422
+ ___Block_byref_object_dispose_.25733
+ ___Block_byref_object_dispose_.26130
+ ___Block_byref_object_dispose_.28210
+ ___Block_byref_object_dispose_.29028
+ ___Block_byref_object_dispose_.3843
+ ___Block_byref_object_dispose_.408
+ ___Block_byref_object_dispose_.411
+ ___Block_byref_object_dispose_.413
+ ___Block_byref_object_dispose_.480
+ ___Block_byref_object_dispose_.510
+ ___Block_byref_object_dispose_.5103
+ ___Block_byref_object_dispose_.5290
+ ___Block_byref_object_dispose_.531
+ ___Block_byref_object_dispose_.595
+ ___Block_byref_object_dispose_.6339
+ ___Block_byref_object_dispose_.712
+ ___Block_byref_object_dispose_.718
+ ___Block_byref_object_dispose_.725
+ ___Block_byref_object_dispose_.729
+ ___Block_byref_object_dispose_.736
+ ___Block_byref_object_dispose_.741
+ ___Block_byref_object_dispose_.7552
+ ___Block_byref_object_dispose_.7642
+ ___Block_byref_object_dispose_.8247
+ ___Block_byref_object_dispose_.8910
+ ___Block_byref_object_dispose_.9386
+ ___Block_byref_object_dispose_.9509
+ ___Block_byref_object_dispose_.9612
+ ____ZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinAction_block_invoke
+ ____ZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinAction_block_invoke.23123
+ ____ZL37ML3LibraryPinDefaultActionDescription19ML3LibraryPinAction_block_invoke.4959
+ ____ZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityType_block_invoke
+ ____ZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityType_block_invoke.23128
+ ____ZL37ML3LibraryPinnedEntityTypeDescription13ML3EntityType_block_invoke.4966
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke.270
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke.277
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke.284
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke.293
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke_2.291
+ ____ZN16ML3ImportSession13_finishImportEv_block_invoke_2.297
+ ____ZN16ML3ImportSession21_reconcileLibraryPinsEv_block_invoke
+ ____ZN16ML3ImportSession21_reconcileLibraryPinsEv_block_invoke.375
+ ____ZN16ML3ImportSession26_updateEntityRevisionTableERNSt3__16vectorINS0_10shared_ptrI13ML3ImportItemEENS0_9allocatorIS4_EEEEx_block_invoke
+ ____ZN16ML3ImportSession34_prepareContainerAuthorImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.738
+ ____ZN16ML3ImportSession38_populateExistingLibraryPinnedEntitiesEv_block_invoke
+ ____ZN16ML3ImportSession38_prepareContainerItemPersonImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.723
+ ____ZN16ML3ImportSession5flushEb_block_invoke.176
+ ___block_descriptor_40_e8_32r_e15_v32?08Q16^B24lr32l8
+ ___block_descriptor_40_e8_v12?0B8l
+ ___block_descriptor_44_e40_v32?0"ML3DatabaseRow"8"NSError"16^B24l
+ ___block_descriptor_48_e8_32r_e31_v16?0"ML3DatabaseConnection"8lr32l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSNumber"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e40_v32?0"ML3DatabaseRow"8"NSError"16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_65_e8_32s40r48r56r_e15_v32?0q8Q16^B24ls32l8r40l8r48l8r56l8
+ ___block_descriptor_76_e8_32s40r_e31_B16?0"ML3DatabaseConnection"8lr40l8s32l8
+ ___block_descriptor_77_e8_32s40r_e31_B16?0"ML3DatabaseConnection"8ls32l8r40l8
+ ___block_descriptor_84_e8_32s40s48s56r64r_e27_v36?0"NSString"8q16B24q28ls32l8r56l8r64l8s40l8s48l8
+ ___block_literal_global.10978
+ ___block_literal_global.11029
+ ___block_literal_global.113.3087
+ ___block_literal_global.11825
+ ___block_literal_global.12256
+ ___block_literal_global.1226
+ ___block_literal_global.13751
+ ___block_literal_global.13927
+ ___block_literal_global.1447
+ ___block_literal_global.14802
+ ___block_literal_global.15679
+ ___block_literal_global.159
+ ___block_literal_global.16504
+ ___block_literal_global.16839
+ ___block_literal_global.17554
+ ___block_literal_global.18678
+ ___block_literal_global.19619
+ ___block_literal_global.19892
+ ___block_literal_global.20060
+ ___block_literal_global.20177
+ ___block_literal_global.20321
+ ___block_literal_global.20863
+ ___block_literal_global.21315
+ ___block_literal_global.21612
+ ___block_literal_global.21739
+ ___block_literal_global.22093
+ ___block_literal_global.22866
+ ___block_literal_global.2433
+ ___block_literal_global.24492
+ ___block_literal_global.25144
+ ___block_literal_global.25274
+ ___block_literal_global.26139
+ ___block_literal_global.26461
+ ___block_literal_global.27410
+ ___block_literal_global.276
+ ___block_literal_global.290
+ ___block_literal_global.3097
+ ___block_literal_global.314
+ ___block_literal_global.4372
+ ___block_literal_global.4535
+ ___block_literal_global.485
+ ___block_literal_global.4949
+ ___block_literal_global.5101
+ ___block_literal_global.5271
+ ___block_literal_global.543
+ ___block_literal_global.557
+ ___block_literal_global.5905
+ ___block_literal_global.6042
+ ___block_literal_global.6304
+ ___block_literal_global.6788
+ ___block_literal_global.688
+ ___block_literal_global.752
+ ___block_literal_global.7528
+ ___block_literal_global.753
+ ___block_literal_global.759
+ ___block_literal_global.790
+ ___block_literal_global.827
+ ___block_literal_global.828
+ ___block_literal_global.83.6102
+ ___block_literal_global.830
+ ___block_literal_global.832
+ ___block_literal_global.834
+ ___block_literal_global.844
+ ___block_literal_global.8476
+ ___block_literal_global.8574
+ ___block_literal_global.882
+ ___block_literal_global.8902
+ ___block_literal_global.896
+ ___block_literal_global.911
+ ___block_literal_global.9139
+ ___block_literal_global.9364
+ ___block_literal_global.9494
+ ___block_literal_global.987
+ ___block_literal_global.9974
+ ___block_literal_global.999
+ ___getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.18136
+ ___getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.18118
+ ___getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.18148
+ ___iTunesCloudLibraryCore_block_invoke.18131
+ _audit_stringiTunesCloud.18134
+ _getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.18135
+ _getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.18117
+ _getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.18147
+ _iTunesCloudLibrary.18119
+ _iTunesCloudLibraryCore.frameworkLibrary.18130
+ _objc_msgSend$_checkoutConnection:ignoreSubPoolClosedState:
+ _objc_msgSend$_deleteRowsFromLibraryPinsTableForPersistentIDs:count:library:usingConnection:
+ _objc_msgSend$_processLibraryPinElement:
+ _objc_msgSend$_processLibraryPinOperation:withImportSession:
+ _objc_msgSend$_processMaxPinCount:
+ _objc_msgSend$_processPinCount:
+ _objc_msgSend$_removeLibraryPinsForDeletedTracksUsingConnection:
+ _objc_msgSend$_setError
+ _objc_msgSend$addContainers:completion:
+ _objc_msgSend$cloudItemID
+ _objc_msgSend$cloudLibraryID
+ _objc_msgSend$currentDeviceFavoritesPlaylistInLibrary:usingConnection:
+ _objc_msgSend$defaultAction
+ _objc_msgSend$deleteFromLibrary:deletionType:persistentIDs:count:preserveUndeletableEntities:
+ _objc_msgSend$entityType
+ _objc_msgSend$enumerateObjectsWithOptions:usingBlock:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasCloudItemID
+ _objc_msgSend$hasCloudLibraryID
+ _objc_msgSend$hasDefaultAction
+ _objc_msgSend$hasEntityType
+ _objc_msgSend$hasError
+ _objc_msgSend$hasPosition
+ _objc_msgSend$hasPositionUUID
+ _objc_msgSend$initWithLibraryPath:trackData:playlistData:albumArtistData:albumData:libraryPinsData:clientIdentity:
+ _objc_msgSend$libraryPin
+ _objc_msgSend$libraryPinImportItemFromDAAPElement:
+ _objc_msgSend$libraryPinsData
+ _objc_msgSend$parentPlaylistPersistentIdsAndNames
+ _objc_msgSend$playlistItem
+ _objc_msgSend$position
+ _objc_msgSend$removeContainers:completion:
+ _objc_msgSend$sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:
+ _objc_msgSend$session:failedToAddContainer:shouldStop:
+ _objc_msgSend$session:failedToRemoveContainer:shouldStop:
+ _objc_msgSend$session:failedToRemoveItem:shouldStop:
+ _objc_msgSend$session:failedToUpdateContainer:shouldStop:
+ _objc_msgSend$session:failedToUpdateItem:shouldStop:
+ _objc_msgSend$setCloudItemID:
+ _objc_msgSend$setCloudLibraryID:
+ _objc_msgSend$setDefaultAction:
+ _objc_msgSend$setEntityType:
+ _objc_msgSend$setLibraryPin:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setSubPoolIsClosed
+ _objc_msgSend$updateContainers:completion:
+ _objc_msgSend$userUndeleteablePlaylistPersistentIDSInLibrary:
+ _propertiesForGroupingKey.onceToken.5904
+ _propertiesForGroupingKey.onceToken.7527
+ _propertiesForGroupingKey.onceToken.9363
+ _propertiesForGroupingKey.onceToken.9493
+ _propertiesForGroupingKey.propertiesForGroupingKey.5906
+ _propertiesForGroupingKey.propertiesForGroupingKey.7529
+ _propertiesForGroupingKey.propertiesForGroupingKey.9365
+ _propertiesForGroupingKey.propertiesForGroupingKey.9495
- -[ML3UpdateSpotlightIndexOperation _checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:]
- GCC_except_table1002
- GCC_except_table1005
- GCC_except_table1006
- GCC_except_table1012
- GCC_except_table1013
- GCC_except_table1014
- GCC_except_table1035
- GCC_except_table105
- GCC_except_table1050
- GCC_except_table1057
- GCC_except_table1059
- GCC_except_table1068
- GCC_except_table111
- GCC_except_table1142
- GCC_except_table1179
- GCC_except_table1199
- GCC_except_table121
- GCC_except_table125
- GCC_except_table1255
- GCC_except_table132
- GCC_except_table136
- GCC_except_table1363
- GCC_except_table1370
- GCC_except_table1377
- GCC_except_table1379
- GCC_except_table1386
- GCC_except_table1399
- GCC_except_table140
- GCC_except_table1412
- GCC_except_table1414
- GCC_except_table1437
- GCC_except_table1444
- GCC_except_table145
- GCC_except_table1453
- GCC_except_table1459
- GCC_except_table1482
- GCC_except_table1486
- GCC_except_table149
- GCC_except_table1493
- GCC_except_table1498
- GCC_except_table150
- GCC_except_table151
- GCC_except_table1519
- GCC_except_table1521
- GCC_except_table1523
- GCC_except_table1533
- GCC_except_table1535
- GCC_except_table1537
- GCC_except_table1539
- GCC_except_table1545
- GCC_except_table1549
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1591
- GCC_except_table1622
- GCC_except_table1626
- GCC_except_table1642
- GCC_except_table1646
- GCC_except_table1649
- GCC_except_table1652
- GCC_except_table1676
- GCC_except_table1681
- GCC_except_table1683
- GCC_except_table1695
- GCC_except_table1702
- GCC_except_table1704
- GCC_except_table1705
- GCC_except_table1706
- GCC_except_table1708
- GCC_except_table1747
- GCC_except_table1760
- GCC_except_table1762
- GCC_except_table1767
- GCC_except_table1776
- GCC_except_table1783
- GCC_except_table1823
- GCC_except_table1830
- GCC_except_table1832
- GCC_except_table1850
- GCC_except_table1854
- GCC_except_table1862
- GCC_except_table1866
- GCC_except_table1876
- GCC_except_table1877
- GCC_except_table1892
- GCC_except_table1903
- GCC_except_table1937
- GCC_except_table1967
- GCC_except_table1973
- GCC_except_table1974
- GCC_except_table1975
- GCC_except_table1990
- GCC_except_table1997
- GCC_except_table2001
- GCC_except_table2002
- GCC_except_table2003
- GCC_except_table2004
- GCC_except_table2005
- GCC_except_table2007
- GCC_except_table2008
- GCC_except_table2009
- GCC_except_table2010
- GCC_except_table2019
- GCC_except_table2020
- GCC_except_table2021
- GCC_except_table2027
- GCC_except_table2030
- GCC_except_table2033
- GCC_except_table2034
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table2053
- GCC_except_table2054
- GCC_except_table2055
- GCC_except_table2056
- GCC_except_table2057
- GCC_except_table2061
- GCC_except_table2065
- GCC_except_table2070
- GCC_except_table2071
- GCC_except_table2088
- GCC_except_table2089
- GCC_except_table2090
- GCC_except_table2091
- GCC_except_table2101
- GCC_except_table2102
- GCC_except_table2103
- GCC_except_table2115
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2123
- GCC_except_table2127
- GCC_except_table2129
- GCC_except_table2131
- GCC_except_table2133
- GCC_except_table2140
- GCC_except_table2141
- GCC_except_table2142
- GCC_except_table2153
- GCC_except_table2154
- GCC_except_table2156
- GCC_except_table2157
- GCC_except_table2158
- GCC_except_table2159
- GCC_except_table2160
- GCC_except_table2161
- GCC_except_table2163
- GCC_except_table2164
- GCC_except_table2166
- GCC_except_table2173
- GCC_except_table2175
- GCC_except_table2177
- GCC_except_table2179
- GCC_except_table2181
- GCC_except_table2183
- GCC_except_table2216
- GCC_except_table2217
- GCC_except_table2218
- GCC_except_table2219
- GCC_except_table2380
- GCC_except_table2384
- GCC_except_table2443
- GCC_except_table2459
- GCC_except_table2472
- GCC_except_table2477
- GCC_except_table2482
- GCC_except_table2489
- GCC_except_table2492
- GCC_except_table2503
- GCC_except_table2505
- GCC_except_table2511
- GCC_except_table2516
- GCC_except_table2520
- GCC_except_table2524
- GCC_except_table2530
- GCC_except_table2536
- GCC_except_table2537
- GCC_except_table2538
- GCC_except_table2759
- GCC_except_table2807
- GCC_except_table2810
- GCC_except_table2815
- GCC_except_table2838
- GCC_except_table2867
- GCC_except_table2878
- GCC_except_table2882
- GCC_except_table2885
- GCC_except_table2899
- GCC_except_table2901
- GCC_except_table2903
- GCC_except_table2906
- GCC_except_table2909
- GCC_except_table2944
- GCC_except_table2947
- GCC_except_table2957
- GCC_except_table2960
- GCC_except_table3015
- GCC_except_table3022
- GCC_except_table3025
- GCC_except_table3042
- GCC_except_table3043
- GCC_except_table3044
- GCC_except_table3045
- GCC_except_table3046
- GCC_except_table3052
- GCC_except_table3053
- GCC_except_table3059
- GCC_except_table3060
- GCC_except_table3061
- GCC_except_table3062
- GCC_except_table3063
- GCC_except_table3064
- GCC_except_table3072
- GCC_except_table3073
- GCC_except_table3074
- GCC_except_table3099
- GCC_except_table3115
- GCC_except_table3118
- GCC_except_table3127
- GCC_except_table3138
- GCC_except_table3139
- GCC_except_table3140
- GCC_except_table3142
- GCC_except_table3149
- GCC_except_table3150
- GCC_except_table3162
- GCC_except_table3165
- GCC_except_table3169
- GCC_except_table3233
- GCC_except_table3254
- GCC_except_table3255
- GCC_except_table3261
- GCC_except_table3266
- GCC_except_table3267
- GCC_except_table3268
- GCC_except_table3269
- GCC_except_table3274
- GCC_except_table3276
- GCC_except_table3279
- GCC_except_table3281
- GCC_except_table3282
- GCC_except_table3283
- GCC_except_table3284
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3289
- GCC_except_table3290
- GCC_except_table3291
- GCC_except_table3292
- GCC_except_table3293
- GCC_except_table3294
- GCC_except_table3295
- GCC_except_table3300
- GCC_except_table3301
- GCC_except_table3302
- GCC_except_table3303
- GCC_except_table3304
- GCC_except_table3305
- GCC_except_table3306
- GCC_except_table3307
- GCC_except_table3308
- GCC_except_table3314
- GCC_except_table3316
- GCC_except_table3317
- GCC_except_table3325
- GCC_except_table3328
- GCC_except_table3338
- GCC_except_table3339
- GCC_except_table3340
- GCC_except_table3341
- GCC_except_table3348
- GCC_except_table3365
- GCC_except_table3390
- GCC_except_table3425
- GCC_except_table3724
- GCC_except_table3734
- GCC_except_table3736
- GCC_except_table374
- GCC_except_table3759
- GCC_except_table376
- GCC_except_table3761
- GCC_except_table377
- GCC_except_table3771
- GCC_except_table378
- GCC_except_table379
- GCC_except_table380
- GCC_except_table383
- GCC_except_table389
- GCC_except_table3930
- GCC_except_table3934
- GCC_except_table3939
- GCC_except_table3942
- GCC_except_table3945
- GCC_except_table3954
- GCC_except_table3957
- GCC_except_table3958
- GCC_except_table3959
- GCC_except_table3964
- GCC_except_table3972
- GCC_except_table3983
- GCC_except_table399
- GCC_except_table4004
- GCC_except_table4014
- GCC_except_table4018
- GCC_except_table4021
- GCC_except_table4024
- GCC_except_table406
- GCC_except_table408
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table417
- GCC_except_table418
- GCC_except_table419
- GCC_except_table420
- GCC_except_table4203
- GCC_except_table421
- GCC_except_table4217
- GCC_except_table4219
- GCC_except_table4221
- GCC_except_table4222
- GCC_except_table4223
- GCC_except_table4226
- GCC_except_table4232
- GCC_except_table4237
- GCC_except_table4241
- GCC_except_table4260
- GCC_except_table4262
- GCC_except_table437
- GCC_except_table439
- GCC_except_table4407
- GCC_except_table4414
- GCC_except_table4421
- GCC_except_table4422
- GCC_except_table4423
- GCC_except_table4429
- GCC_except_table4496
- GCC_except_table4497
- GCC_except_table4498
- GCC_except_table4499
- GCC_except_table4503
- GCC_except_table4511
- GCC_except_table4513
- GCC_except_table452
- GCC_except_table4523
- GCC_except_table4532
- GCC_except_table4546
- GCC_except_table4547
- GCC_except_table4548
- GCC_except_table458
- GCC_except_table4653
- GCC_except_table4656
- GCC_except_table4663
- GCC_except_table4681
- GCC_except_table4682
- GCC_except_table4683
- GCC_except_table4684
- GCC_except_table4799
- GCC_except_table4803
- GCC_except_table4805
- GCC_except_table4807
- GCC_except_table4808
- GCC_except_table4809
- GCC_except_table4896
- GCC_except_table4899
- GCC_except_table4903
- GCC_except_table4906
- GCC_except_table4907
- GCC_except_table492
- GCC_except_table4921
- GCC_except_table4929
- GCC_except_table493
- GCC_except_table4931
- GCC_except_table4934
- GCC_except_table4935
- GCC_except_table4936
- GCC_except_table4937
- GCC_except_table4938
- GCC_except_table4939
- GCC_except_table4941
- GCC_except_table4945
- GCC_except_table4947
- GCC_except_table4950
- GCC_except_table4952
- GCC_except_table4954
- GCC_except_table4955
- GCC_except_table4956
- GCC_except_table4957
- GCC_except_table4958
- GCC_except_table4960
- GCC_except_table4961
- GCC_except_table4962
- GCC_except_table4974
- GCC_except_table4979
- GCC_except_table498
- GCC_except_table5017
- GCC_except_table5021
- GCC_except_table5023
- GCC_except_table5027
- GCC_except_table5030
- GCC_except_table5032
- GCC_except_table5035
- GCC_except_table5037
- GCC_except_table5043
- GCC_except_table5062
- GCC_except_table5083
- GCC_except_table5088
- GCC_except_table5098
- GCC_except_table5099
- GCC_except_table5101
- GCC_except_table5107
- GCC_except_table5170
- GCC_except_table5175
- GCC_except_table5176
- GCC_except_table5178
- GCC_except_table5182
- GCC_except_table5183
- GCC_except_table5263
- GCC_except_table5266
- GCC_except_table5267
- GCC_except_table5271
- GCC_except_table5272
- GCC_except_table5273
- GCC_except_table5287
- GCC_except_table5288
- GCC_except_table5289
- GCC_except_table5300
- GCC_except_table5302
- GCC_except_table5304
- GCC_except_table5307
- GCC_except_table5311
- GCC_except_table5312
- GCC_except_table5326
- GCC_except_table5362
- GCC_except_table5371
- GCC_except_table5376
- GCC_except_table539
- GCC_except_table540
- GCC_except_table541
- GCC_except_table543
- GCC_except_table5469
- GCC_except_table547
- GCC_except_table5475
- GCC_except_table5481
- GCC_except_table5487
- GCC_except_table5493
- GCC_except_table5499
- GCC_except_table5505
- GCC_except_table5507
- GCC_except_table5513
- GCC_except_table5514
- GCC_except_table5520
- GCC_except_table5526
- GCC_except_table5531
- GCC_except_table5532
- GCC_except_table5540
- GCC_except_table5547
- GCC_except_table555
- GCC_except_table5553
- GCC_except_table5556
- GCC_except_table5582
- GCC_except_table560
- GCC_except_table561
- GCC_except_table5610
- GCC_except_table5618
- GCC_except_table5631
- GCC_except_table5639
- GCC_except_table5712
- GCC_except_table5716
- GCC_except_table572
- GCC_except_table5723
- GCC_except_table5726
- GCC_except_table5730
- GCC_except_table5745
- GCC_except_table5748
- GCC_except_table5751
- GCC_except_table5758
- GCC_except_table5759
- GCC_except_table5761
- GCC_except_table5787
- GCC_except_table5788
- GCC_except_table5789
- GCC_except_table5790
- GCC_except_table5795
- GCC_except_table5796
- GCC_except_table580
- GCC_except_table582
- GCC_except_table5825
- GCC_except_table5849
- GCC_except_table5851
- GCC_except_table5853
- GCC_except_table5854
- GCC_except_table5855
- GCC_except_table5856
- GCC_except_table5857
- GCC_except_table586
- GCC_except_table5861
- GCC_except_table5863
- GCC_except_table5868
- GCC_except_table5869
- GCC_except_table5910
- GCC_except_table5955
- GCC_except_table5956
- GCC_except_table5957
- GCC_except_table596
- GCC_except_table5983
- GCC_except_table5986
- GCC_except_table5996
- GCC_except_table6000
- GCC_except_table6001
- GCC_except_table6006
- GCC_except_table6007
- GCC_except_table6008
- GCC_except_table6011
- GCC_except_table6012
- GCC_except_table6013
- GCC_except_table6014
- GCC_except_table6015
- GCC_except_table6017
- GCC_except_table6019
- GCC_except_table6020
- GCC_except_table6021
- GCC_except_table6025
- GCC_except_table6026
- GCC_except_table6027
- GCC_except_table6028
- GCC_except_table603
- GCC_except_table6030
- GCC_except_table6031
- GCC_except_table6033
- GCC_except_table6034
- GCC_except_table6035
- GCC_except_table6036
- GCC_except_table6038
- GCC_except_table6039
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6054
- GCC_except_table6073
- GCC_except_table6074
- GCC_except_table6077
- GCC_except_table6079
- GCC_except_table608
- GCC_except_table6081
- GCC_except_table6082
- GCC_except_table6084
- GCC_except_table609
- GCC_except_table6090
- GCC_except_table6114
- GCC_except_table6117
- GCC_except_table619
- GCC_except_table6193
- GCC_except_table620
- GCC_except_table6200
- GCC_except_table6201
- GCC_except_table6202
- GCC_except_table6203
- GCC_except_table6204
- GCC_except_table6205
- GCC_except_table6206
- GCC_except_table6214
- GCC_except_table6216
- GCC_except_table6218
- GCC_except_table6221
- GCC_except_table6224
- GCC_except_table6226
- GCC_except_table623
- GCC_except_table6232
- GCC_except_table6240
- GCC_except_table6242
- GCC_except_table6245
- GCC_except_table6246
- GCC_except_table6247
- GCC_except_table6248
- GCC_except_table6250
- GCC_except_table6254
- GCC_except_table6260
- GCC_except_table6263
- GCC_except_table6268
- GCC_except_table6269
- GCC_except_table6270
- GCC_except_table6271
- GCC_except_table6272
- GCC_except_table6273
- GCC_except_table6275
- GCC_except_table6276
- GCC_except_table6277
- GCC_except_table6278
- GCC_except_table6285
- GCC_except_table6291
- GCC_except_table6293
- GCC_except_table6294
- GCC_except_table6296
- GCC_except_table6302
- GCC_except_table6303
- GCC_except_table6304
- GCC_except_table6305
- GCC_except_table6306
- GCC_except_table6307
- GCC_except_table6308
- GCC_except_table6309
- GCC_except_table6315
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table6320
- GCC_except_table6321
- GCC_except_table6322
- GCC_except_table6325
- GCC_except_table6326
- GCC_except_table6328
- GCC_except_table633
- GCC_except_table6330
- GCC_except_table6332
- GCC_except_table6333
- GCC_except_table6334
- GCC_except_table6337
- GCC_except_table634
- GCC_except_table6343
- GCC_except_table6344
- GCC_except_table6347
- GCC_except_table635
- GCC_except_table636
- GCC_except_table6376
- GCC_except_table6377
- GCC_except_table6384
- GCC_except_table6385
- GCC_except_table6387
- GCC_except_table6389
- GCC_except_table6391
- GCC_except_table6392
- GCC_except_table6403
- GCC_except_table6406
- GCC_except_table6423
- GCC_except_table6430
- GCC_except_table6438
- GCC_except_table6444
- GCC_except_table6446
- GCC_except_table6448
- GCC_except_table6463
- GCC_except_table6465
- GCC_except_table647
- GCC_except_table6473
- GCC_except_table6485
- GCC_except_table650
- GCC_except_table6609
- GCC_except_table6614
- GCC_except_table6626
- GCC_except_table6630
- GCC_except_table6632
- GCC_except_table6647
- GCC_except_table6648
- GCC_except_table6649
- GCC_except_table6655
- GCC_except_table6660
- GCC_except_table6661
- GCC_except_table6662
- GCC_except_table6698
- GCC_except_table6699
- GCC_except_table6705
- GCC_except_table6707
- GCC_except_table6708
- GCC_except_table6709
- GCC_except_table6710
- GCC_except_table6711
- GCC_except_table6712
- GCC_except_table6713
- GCC_except_table6714
- GCC_except_table6720
- GCC_except_table6721
- GCC_except_table6722
- GCC_except_table6723
- GCC_except_table6724
- GCC_except_table6725
- GCC_except_table6731
- GCC_except_table6732
- GCC_except_table6733
- GCC_except_table6744
- GCC_except_table6745
- GCC_except_table6746
- GCC_except_table6747
- GCC_except_table6748
- GCC_except_table6749
- GCC_except_table6750
- GCC_except_table6751
- GCC_except_table6752
- GCC_except_table6753
- GCC_except_table6758
- GCC_except_table6759
- GCC_except_table6765
- GCC_except_table6766
- GCC_except_table6767
- GCC_except_table6768
- GCC_except_table6770
- GCC_except_table6774
- GCC_except_table6775
- GCC_except_table6777
- GCC_except_table6798
- GCC_except_table6820
- GCC_except_table6842
- GCC_except_table6851
- GCC_except_table6858
- GCC_except_table6905
- GCC_except_table6933
- GCC_except_table6938
- GCC_except_table6941
- GCC_except_table6965
- GCC_except_table6970
- GCC_except_table7050
- GCC_except_table7078
- GCC_except_table7113
- GCC_except_table714
- GCC_except_table715
- GCC_except_table716
- GCC_except_table717
- GCC_except_table718
- GCC_except_table7202
- GCC_except_table722
- GCC_except_table723
- GCC_except_table7303
- GCC_except_table731
- GCC_except_table733
- GCC_except_table7373
- GCC_except_table7379
- GCC_except_table7385
- GCC_except_table7386
- GCC_except_table7387
- GCC_except_table739
- GCC_except_table740
- GCC_except_table7402
- GCC_except_table7406
- GCC_except_table743
- GCC_except_table745
- GCC_except_table7452
- GCC_except_table7458
- GCC_except_table748
- GCC_except_table749
- GCC_except_table760
- GCC_except_table763
- GCC_except_table7765
- GCC_except_table7766
- GCC_except_table7767
- GCC_except_table7773
- GCC_except_table7775
- GCC_except_table7776
- GCC_except_table7779
- GCC_except_table782
- GCC_except_table788
- GCC_except_table794
- GCC_except_table800
- GCC_except_table806
- GCC_except_table812
- GCC_except_table850
- GCC_except_table913
- GCC_except_table915
- GCC_except_table921
- GCC_except_table944
- GCC_except_table948
- GCC_except_table955
- GCC_except_table993
- GCC_except_table997
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _CFAllocatorAllocate
- _MDItemAppEntityInstanceId
- _MDItemBundleID
- _MDItemContentType
- _MSVFastHexStringFromBytes.hexCharacters.27514
- _OBJC_CLASS_$_CSSearchQuery
- _OBJC_CLASS_$_CSSearchQueryContext
- __MSV_XXH_XXH32_update.27506
- __MSV_XXH_XXH64_digest.27511
- __MSV_XXH_XXH64_update.27507
- __ZL22FastAppendPersistentIDP37ML3QueryResultSet_MutableBackingStorexh
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPKNS_10shared_ptrI27ML3DatabaseImportDataSourceEES8_PS6_EENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_10shared_ptrI13ML3ImportItemEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__114default_deleteIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS_10shared_ptrI13ML3ImportItemEEE26_ContainerItemReactionInfoEclB8ne190102EPS5_
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNKSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIx14ML3ArtworkTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIxxEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP11_constraintNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP17_constraint_stateNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNKSt9type_infoeqB8ne190102ERKS_
- __ZNSt11range_errorC1B8ne190102EPKc
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110shared_ptrI10ML3CPPDataEC2B8ne190102IS1_Li0EEEPT_
- __ZNSt3__110shared_ptrI12ML3AlbumDataED1B8ne190102Ev
- __ZNSt3__110shared_ptrI12ML3GenreDataED1B8ne190102Ev
- __ZNSt3__110shared_ptrI13ML3ArtistDataED1B8ne190102Ev
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I25ML3SubscriptionImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I26ML3ContainerItemImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I27ML3ProtoSyncAlbumImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I27ML3ProtoSyncTrackImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ContainerAuthorImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ITunesSyncAlbumImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ITunesSyncTrackImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ProtoSyncArtistImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ProtoSyncDeleteImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I29ML3ITunesSyncArtistImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I31ML3ProtoSyncContainerImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I32ML3ITunesSyncContainerImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I34ML3ContainerItemReactionImportItemLi0EEEPT_
- __ZNSt3__110shared_ptrI15ML3ComposerDataED1B8ne190102Ev
- __ZNSt3__110shared_ptrI27ML3DatabaseImportDataSourceEC2B8ne190102I36ML3ItemStoreDatabaseImportDataSourceLi0EEEPT_
- __ZNSt3__110shared_ptrIN6ML3CPP7ElementEE18__enable_weak_thisB8ne190102IS2_S2_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIx20ML3CollectionInfoSetEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEE5resetB8ne190102EPS6_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEENS_22__tree_node_destructorINS6_ISH_EEEEED1B8ne190102Ev
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20ML3CollectionInfoSetEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__115allocate_sharedB8ne190102I12ML3AlbumDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_RiSB_SB_SB_R12ML3NameOrderSB_S4_S4_SA_SB_RbS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_S9_S9_S4_R12ML3NameOrderSC_S4_SA_RbRiS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_SA_SA_S4_R12ML3NameOrderSC_S4_S9_RbiiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I18ML3AlbumImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI12ML3AlbumDataEERNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERbRU8__strongP6NSDataxRxSJ_SE_ELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I19ML3ArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataxELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I29ML3SetCloudIDArtistImportItemNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102Ev
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEEEEE7destroyB8ne190102INS_4pairIKS8_SE_EEvLi0EEEvRSI_PT_
- __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED0B8ne190102Ev
- __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED1B8ne190102Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrIN6ML3CPP7ElementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_10shared_ptrIN6ML3CPP6Parser15ParserContainerEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIwEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__119__throw_range_errorB8ne190102EPKc
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__120__optional_copy_baseINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELb0EEC2B8ne190102ERKSC_
- __ZNSt3__120__throw_bad_weak_ptrB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj14ML3ImportValueINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEPvEEEEEclB8ne190102EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3AlbumDataEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3GenreDataEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ArtistDataEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI15ML3ComposerDataEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_6vectorINS_4pairIxxEENS1_IS6_EEEEEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPSE_EEED2B8ne190102Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI27ML3DatabaseImportDataSourceEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPKSD_SG_PSD_EET2_RT_T0_T1_SI_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEC1B8ne190102ERKSJ_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEaSB8ne190102ERKSJ_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExNS_4lessIS6_EENS4_INS_4pairIKS6_xEEEEED1B8ne190102Ev
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEED1Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCache9__advanceB8ne190102Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCacheD1B8ne190102Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPKS3_S9_EEvT_T0_l
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne190102IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_13unordered_mapIxyNS_4hashIxEENS_8equal_toIxEENS_9allocatorINS_4pairIKxyEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_13unordered_mapIyxNS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyxEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__init_with_sizeB8ne190102IPSD_SH_EEvT_T0_m
- __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE21__push_back_slow_pathIRKSD_EEPSD_OT_
- __ZNSt3__16vectorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEENS6_ISD_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
- __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B8ne190102Em
- __ZNSt3__18optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEaSB8ne190102IS7_vEERSC_OT_
- __ZNSt3__19allocatorI18DAAPParserDelegateE9constructB8ne190102IS1_JRU8__strongKP22ML3DAAPImportOperationRNS_10shared_ptrIN6ML3CPP6ParserEEER32ML3DAAPImportOperationEntityTypebEEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___103+[ML3Track deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:usingConnection:]_block_invoke.2501
- ___103-[ML3UpdateSpotlightIndexOperation _indexItemsFromLibrarySinceRevision:targetRevision:completionBlock:]_block_invoke.47
- ___104+[ML3Entity deleteFromLibrary:deletionType:canonicalizeCollections:persistentIDs:count:usingConnection:]_block_invoke.221
- ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.106
- ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.114
- ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.122
- ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.124
- ___107-[ML3MusicLibrary(RemoveSourceOrTracks) removeSource:forImportOperation:usingConnection:postNotifications:]_block_invoke.92
- ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke.2529
- ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke.2535
- ___110+[ML3Track unlinkRedownloadableAssetsFromLibrary:persistentIDs:deletionType:disableKeepLocal:deletedFileSize:]_block_invoke_2.2533
- ___136-[ML3MusicLibrary enumeratePersistentIDsAfterRevision:revisionTrackingCode:maximumRevisionType:forMediaTypes:inUsersLibrary:usingBlock:]_block_invoke.620
- ___141-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.671
- ___143-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.682
- ___150-[ML3MusicLibrary(RemoveSourceOrTracks) _removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:]_block_invoke.143
- ___150-[ML3MusicLibrary(RemoveSourceOrTracks) _removeSource:fromPersistentIDS:forImportOperation:canonocalizeCollections:usingConnection:postNotifications:]_block_invoke.148
- ___152-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]_block_invoke.678
- ___43-[ML3RemoveCloudSourcesOperation _execute:]_block_invoke.42
- ___43-[ML3RemoveCloudSourcesOperation _execute:]_block_invoke.60
- ___43-[ML3UpdateSpotlightIndexOperation execute]_block_invoke.23
- ___43-[ML3UpdateSpotlightIndexOperation execute]_block_invoke.24
- ___43-[ML3UpdateSpotlightIndexOperation execute]_block_invoke.25
- ___46-[ML3ClientImportSession _xpcClientConnection]_block_invoke.97
- ___52-[ML3MusicLibrary removeOrphanedTracksOnlyInCaches:]_block_invoke.745
- ___52-[_ML3DatabaseConnectionSubPool checkoutConnection:]_block_invoke
- ___52-[_ML3DatabaseConnectionSubPool checkoutConnection:]_block_invoke_2
- ___52-[_ML3DatabaseConnectionSubPool checkoutConnection:]_block_invoke_3
- ___58-[ML3MusicLibrary _closeAndLockCurrentDatabaseConnections]_block_invoke.976
- ___59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.488
- ___59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.512
- ___63-[ML3MusicLibrary _removeOrphanedArtworkAssetsUsingConnection:]_block_invoke.946
- ___65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.922
- ___65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.935
- ___67+[ML3Container deleteFromLibrary:deletionType:persistentIDs:count:]_block_invoke
- ___67+[ML3Container deleteFromLibrary:deletionType:persistentIDs:count:]_block_invoke_2
- ___71-[ML3DatabaseValidation _validateLibraryDatabaseIfNecessary:withError:]_block_invoke.16
- ___74-[ML3UpdateSpotlightIndexOperation _batchIndexWithObject:completionBlock:]_block_invoke.52
- ___76-[ML3MusicLibrary sanitizeSortMapContentsUsingConnection:didSortMapEntries:]_block_invoke.888
- ___77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.698
- ___83-[ML3UpdateSpotlightIndexOperation _createSearchableItemsForTracksWithQuery:error:]_block_invoke.82
- ___91-[ML3UpdateSpotlightIndexOperation _checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:]_block_invoke
- ___91-[ML3UpdateSpotlightIndexOperation _checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:]_block_invoke_2
- ___94-[ML3MusicLibrary performColorAnalysisForArtworkWithConnection:shouldRegenerateColorAnalysis:]_block_invoke.668
- ___99-[ML3MusicLibrary enumerateArtworkRelativePathsWithConnection:matchingRelativePathContainer:block:]_block_invoke.655
- ___Block_byref_object_copy_.10760
- ___Block_byref_object_copy_.11598
- ___Block_byref_object_copy_.11702
- ___Block_byref_object_copy_.12565
- ___Block_byref_object_copy_.12718
- ___Block_byref_object_copy_.13106
- ___Block_byref_object_copy_.13555
- ___Block_byref_object_copy_.14554
- ___Block_byref_object_copy_.1536
- ___Block_byref_object_copy_.17119
- ___Block_byref_object_copy_.17447
- ___Block_byref_object_copy_.17981
- ___Block_byref_object_copy_.18795
- ___Block_byref_object_copy_.19201
- ___Block_byref_object_copy_.19452
- ___Block_byref_object_copy_.20335
- ___Block_byref_object_copy_.20691
- ___Block_byref_object_copy_.21837
- ___Block_byref_object_copy_.22657
- ___Block_byref_object_copy_.2386
- ___Block_byref_object_copy_.24483
- ___Block_byref_object_copy_.24560
- ___Block_byref_object_copy_.24662
- ___Block_byref_object_copy_.2471
- ___Block_byref_object_copy_.24876
- ___Block_byref_object_copy_.25186
- ___Block_byref_object_copy_.25568
- ___Block_byref_object_copy_.268
- ___Block_byref_object_copy_.27646
- ___Block_byref_object_copy_.281
- ___Block_byref_object_copy_.284
- ___Block_byref_object_copy_.28468
- ___Block_byref_object_copy_.286
- ___Block_byref_object_copy_.347
- ___Block_byref_object_copy_.374
- ___Block_byref_object_copy_.3765
- ___Block_byref_object_copy_.393
- ___Block_byref_object_copy_.457
- ___Block_byref_object_copy_.5019
- ___Block_byref_object_copy_.5211
- ___Block_byref_object_copy_.577
- ___Block_byref_object_copy_.584
- ___Block_byref_object_copy_.586
- ___Block_byref_object_copy_.591
- ___Block_byref_object_copy_.595
- ___Block_byref_object_copy_.6353
- ___Block_byref_object_copy_.7528
- ___Block_byref_object_copy_.7618
- ___Block_byref_object_copy_.8226
- ___Block_byref_object_copy_.8820
- ___Block_byref_object_copy_.9295
- ___Block_byref_object_copy_.9404
- ___Block_byref_object_copy_.9491
- ___Block_byref_object_dispose_.10761
- ___Block_byref_object_dispose_.11599
- ___Block_byref_object_dispose_.11703
- ___Block_byref_object_dispose_.12566
- ___Block_byref_object_dispose_.12719
- ___Block_byref_object_dispose_.13107
- ___Block_byref_object_dispose_.13556
- ___Block_byref_object_dispose_.14555
- ___Block_byref_object_dispose_.1537
- ___Block_byref_object_dispose_.17120
- ___Block_byref_object_dispose_.17448
- ___Block_byref_object_dispose_.17982
- ___Block_byref_object_dispose_.18796
- ___Block_byref_object_dispose_.19202
- ___Block_byref_object_dispose_.19453
- ___Block_byref_object_dispose_.20336
- ___Block_byref_object_dispose_.20692
- ___Block_byref_object_dispose_.21838
- ___Block_byref_object_dispose_.22658
- ___Block_byref_object_dispose_.2387
- ___Block_byref_object_dispose_.24484
- ___Block_byref_object_dispose_.24561
- ___Block_byref_object_dispose_.24663
- ___Block_byref_object_dispose_.2472
- ___Block_byref_object_dispose_.24877
- ___Block_byref_object_dispose_.25187
- ___Block_byref_object_dispose_.25569
- ___Block_byref_object_dispose_.269
- ___Block_byref_object_dispose_.27647
- ___Block_byref_object_dispose_.282
- ___Block_byref_object_dispose_.28469
- ___Block_byref_object_dispose_.285
- ___Block_byref_object_dispose_.287
- ___Block_byref_object_dispose_.348
- ___Block_byref_object_dispose_.375
- ___Block_byref_object_dispose_.3766
- ___Block_byref_object_dispose_.394
- ___Block_byref_object_dispose_.458
- ___Block_byref_object_dispose_.5020
- ___Block_byref_object_dispose_.5212
- ___Block_byref_object_dispose_.578
- ___Block_byref_object_dispose_.585
- ___Block_byref_object_dispose_.587
- ___Block_byref_object_dispose_.592
- ___Block_byref_object_dispose_.596
- ___Block_byref_object_dispose_.6354
- ___Block_byref_object_dispose_.7529
- ___Block_byref_object_dispose_.7619
- ___Block_byref_object_dispose_.8227
- ___Block_byref_object_dispose_.8821
- ___Block_byref_object_dispose_.9296
- ___Block_byref_object_dispose_.9405
- ___Block_byref_object_dispose_.9492
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke.208
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke.215
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke.222
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke.231
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke_2.229
- ____ZN16ML3ImportSession13_finishImportEv_block_invoke_2.235
- ____ZN16ML3ImportSession34_prepareContainerAuthorImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.593
- ____ZN16ML3ImportSession38_prepareContainerItemPersonImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.583
- ____ZN16ML3ImportSession42_populateExistingAlbumIdentifiersForSourceEi_block_invoke.56
- ____ZN16ML3ImportSession43_populateExistingArtistIdentifiersForSourceEi_block_invoke.41
- ____ZN16ML3ImportSession48_populateExistingAlbumArtistIdentifiersForSourceEi_block_invoke.51
- ____ZN16ML3ImportSession5flushEb_block_invoke.114
- ___block_descriptor_48_e40_v32?0"ML3DatabaseRow"8"NSError"16^B24l
- ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_48_e8_32r40r_e15_v32?0q8Q16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32r40w_e17_v16?0"NSArray"8lr32l8w40l8
- ___block_descriptor_48_ea8_32r_e20_v40?0q8r^16Q24^B32lr32l8
- ___block_descriptor_52_ea8_32r_e20_v40?0q8r^16Q24^B32lr32l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_76_e8_32s40r_e31_B16?0"ML3DatabaseConnection"8ls32l8r40l8
- ___block_descriptor_76_e8_32s40s48s56r_e27_v36?0"NSString"8q16B24q28ls32l8r56l8s40l8s48l8
- ___block_descriptor_77_e8_32s40r_e31_B16?0"ML3DatabaseConnection"8lr40l8s32l8
- ___block_literal_global.10781
- ___block_literal_global.10832
- ___block_literal_global.115
- ___block_literal_global.11618
- ___block_literal_global.12048
- ___block_literal_global.1206
- ___block_literal_global.13523
- ___block_literal_global.13696
- ___block_literal_global.1415
- ___block_literal_global.14450
- ___block_literal_global.15327
- ___block_literal_global.16143
- ___block_literal_global.16464
- ___block_literal_global.17175
- ___block_literal_global.18275
- ___block_literal_global.19200
- ___block_literal_global.19472
- ___block_literal_global.19640
- ___block_literal_global.19758
- ___block_literal_global.19902
- ___block_literal_global.20446
- ___block_literal_global.20895
- ___block_literal_global.21192
- ___block_literal_global.21319
- ___block_literal_global.21673
- ___block_literal_global.22425
- ___block_literal_global.23932
- ___block_literal_global.2402
- ___block_literal_global.24584
- ___block_literal_global.24714
- ___block_literal_global.25578
- ___block_literal_global.25897
- ___block_literal_global.26848
- ___block_literal_global.3056
- ___block_literal_global.315
- ___block_literal_global.406
- ___block_literal_global.4301
- ___block_literal_global.4463
- ___block_literal_global.479
- ___block_literal_global.5018
- ___block_literal_global.5192
- ___block_literal_global.544
- ___block_literal_global.5808
- ___block_literal_global.5945
- ___block_literal_global.605
- ___block_literal_global.608
- ___block_literal_global.6317
- ___block_literal_global.670
- ___block_literal_global.6785
- ___block_literal_global.685
- ___block_literal_global.732
- ___block_literal_global.7505
- ___block_literal_global.769
- ___block_literal_global.813
- ___block_literal_global.814
- ___block_literal_global.816
- ___block_literal_global.818
- ___block_literal_global.820
- ___block_literal_global.83.6005
- ___block_literal_global.8397
- ___block_literal_global.8495
- ___block_literal_global.8814
- ___block_literal_global.890
- ___block_literal_global.9051
- ___block_literal_global.9274
- ___block_literal_global.9392
- ___block_literal_global.966
- ___block_literal_global.978
- ___block_literal_global.9842
- ___getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.17756
- ___getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.17738
- ___getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.17768
- ___iTunesCloudLibraryCore_block_invoke.17751
- _audit_stringiTunesCloud.17754
- _getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.17755
- _getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.17737
- _getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.17767
- _iTunesCloudLibrary.17739
- _iTunesCloudLibraryCore.frameworkLibrary.17750
- _objc_msgSend$_checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:
- _objc_msgSend$attributeSet
- _objc_msgSend$contentType
- _objc_msgSend$initWithQueryString:queryContext:
- _objc_msgSend$setCompletionHandler:
- _objc_msgSend$setFetchAttributes:
- _objc_msgSend$setFoundItemsHandler:
- _propertiesForGroupingKey.onceToken.5807
- _propertiesForGroupingKey.onceToken.7504
- _propertiesForGroupingKey.onceToken.9273
- _propertiesForGroupingKey.onceToken.9391
- _propertiesForGroupingKey.propertiesForGroupingKey.5809
- _propertiesForGroupingKey.propertiesForGroupingKey.7506
- _propertiesForGroupingKey.propertiesForGroupingKey.9275
- _propertiesForGroupingKey.propertiesForGroupingKey.9393
CStrings:
+ "    pins: %d adds %d updates %d deletes"
+ " defaultAction="
+ " pinnedPositionUUID="
+ " sagaID="
+ "%{public}@ Not creating connection as the pool is closed"
+ "<ML3MatchLibraryPinImportItem "
+ "<ML3ProtoSyncLibraryPinImportItem "
+ "@\"MIPLibraryPin\""
+ "@28@0:8^B16B24"
+ "@32@0:8@16^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}24"
+ "@36@0:8q16@24B32"
+ "@64@0:8q16@24q32q40q48@56"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "ALTER TABLE item_store ADD COLUMN immersive_deep_link_url TEXT NOT NULL DEFAULT ''"
+ "ALTER TABLE library_pins_new RENAME TO library_pins"
+ "AutomaticDownloadEnabledForLibraryPins"
+ "B32@0:8@16^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}24"
+ "B48@0:8@16i24r^q28Q36B44"
+ "B48@0:8r^q16Q24@32@40"
+ "B80@0:8{shared_ptr<ML3CPP::Element>=^{Element}^{__shared_weak_count}}16{vector<long long, std::allocator<long long>>=^q^q^q}32{vector<std::unordered_set<std::string>, std::allocator<std::unordered_set<std::string>>>=^v^v^v}56"
+ "CREATE INDEX IF NOT EXISTS ItemContentRating ON item_extra (content_rating ASC)"
+ "CREATE TABLE library_pins (pin_pid INTEGER PRIMARY KEY, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL DEFAULT 0, default_action INTEGER NOT NULL DEFAULT 1, position_uuid TEXT, UNIQUE (entity_pid, entity_type))"
+ "CREATE TABLE library_pins_new (pin_pid INTEGER PRIMARY KEY, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL DEFAULT 0, default_action INTEGER NOT NULL DEFAULT 1, position_uuid TEXT, UNIQUE (entity_pid, entity_type))"
+ "Could not delete existing library pins error=%{public}@"
+ "Could not delete library pin with pid=%lld, error=%{public}@"
+ "Could not find album artist to pin"
+ "Could not find album to pin"
+ "Could not find playlist to pin"
+ "Could not find track to pin"
+ "Could not remove cloud_library_id from album artist with persistentID:%lld, error=%{public}@"
+ "Could not set keep local for album artist items, error=%{public}@"
+ "Could not set keep local for album items, error=%{public}@"
+ "Could not set keep local for album, error=%{public}@"
+ "Could not set keep local for container items, error=%{public}@"
+ "Could not set keep local on container, error=%{public}@"
+ "Could not set keep local on track, error=%{public}@"
+ "Could not update entity revision for pinPID=%lld"
+ "Could not update library pin with pid=%lld, error=%{public}@"
+ "Could not update max allowed pin count to %u, error=%{public}@"
+ "DELETE FROM _MLDatabaseProperties WHERE key IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "DELETE FROM library_pins"
+ "DELETE FROM library_pins WHERE (entity_type=0 AND entity_pid)"
+ "DELETE FROM library_pins WHERE entity_pid=?"
+ "DELETE FROM library_pins WHERE entity_pid=? AND entity_type=?"
+ "DELETE FROM library_pins WHERE entity_type=1 AND entity_pid"
+ "DELETE FROM library_pins WHERE pin_pid=?"
+ "DROP TABLE library_pins"
+ "Drillin"
+ "Error inserting pin with pid=%lld, entity_pid=%lld, entity_type=%{public}@, error=%{public}@"
+ "Failed to delete artist from library_pins with error: %{public}@"
+ "Failed to delete from library_pins with error: %{public}@"
+ "Failed to deserialize library pins data with error: %{public}@"
+ "Failed to increment entity revision for container_pid=%lld, error=%{public}@"
+ "Failed to set parent persistent id for container_pid=%lld, error=%{public}@"
+ "INSERT INTO library_pins_new (pin_pid, entity_pid, entity_type, position, default_action, position_uuid) SELECT pin_pid, entity_pid, entity_type, position, default_action, position_uuid FROM library_pins"
+ "INSERT OR REPLACE INTO _MLDatabaseProperties (key, value) VALUES (?,?)"
+ "INSERT OR REPLACE INTO library_pins (pin_pid, entity_pid, entity_type, default_action, position, position_uuid) VALUES (?, ?, ?, ?, ?, ?)"
+ "Import Metrics: Finished importing pins in %2f seconds (fileCount=%d)"
+ "Importing %llu bytes of library pins data from: %{public}@"
+ "IsSubPoolClosed"
+ "LibraryPin"
+ "MIPLibraryPin"
+ "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d, busyConnections=%p, availableConnections=%p, isSubPoolClosed=%d"
+ "ML3LibraryPin"
+ "MLCloudLibraryForcePerformDeltaSync"
+ "MLCloudLibraryMaxPinCount"
+ "PRAGMA user_version = 2240040;"
+ "PRAGMA user_version = 2300000;"
+ "PRAGMA user_version = 2300010;"
+ "PRAGMA user_version = 2300020;"
+ "Play"
+ "PosterSizedTVArtwork"
+ "Removing all local pinned entities addedLibraryPins.size()=%lu, existingLibraryPinsEntityPidMap.size()=%lu"
+ "SELECT 1 FROM album_artist WHERE album_artist.album_artist_pid=? AND liked_state=? LIMIT 1"
+ "SELECT 1 FROM item JOIN album ON (item.album_pid=album.album_pid) WHERE album.album_pid=? AND in_my_library=1 LIMIT 1"
+ "SELECT 1 FROM item JOIN album_artist ON (item.album_artist_pid=album_artist.album_artist_pid) WHERE album_artist.album_artist_pid=? AND in_my_library=1 LIMIT 1"
+ "SELECT 1 FROM item JOIN item_store USING(item_pid) WHERE item_pid=? AND in_my_library=1 LIMIT 1"
+ "SELECT 1 FROM item WHERE in_my_library AND album_pid=? LIMIT 1"
+ "SELECT 1 FROM library_pins LIMIT 1"
+ "SELECT 1 from album_artist LEFT OUTER JOIN item ON (album_artist.album_artist_pid=item.album_artist_pid) WHERE (album_artist.album_artist_pid=? AND (album_artist.liked_state=? OR in_my_library)) LIMIT 1"
+ "SELECT COUNT() FROM library_pins"
+ "SELECT album.album_pid, store_id, sync_id, cloud_library_id, album_order, album_order_section FROM album JOIN item ON (album.representative_item_pid=item.item_pid) WHERE album_pid != 0"
+ "SELECT album.album_pid, store_id, sync_id, cloud_library_id, album_order, album_order_section FROM album JOIN item ON (album.representative_item_pid=item.item_pid) WHERE cloud_library_id != ''"
+ "SELECT album.album_pid, store_id, sync_id, cloud_library_id, album_order, album_order_section FROM album JOIN item ON (album.representative_item_pid=item.item_pid) WHERE store_id != 0"
+ "SELECT album.album_pid, store_id, sync_id, cloud_library_id, album_order, album_order_section FROM album JOIN item ON (album.representative_item_pid=item.item_pid) WHERE sync_id != 0"
+ "SELECT album_artist.album_artist_pid from album_artist LEFT OUTER JOIN item ON (album_artist.album_artist_pid=item.album_artist_pid) WHERE (album_artist.cloud_universal_library_id=? AND (album_artist.liked_state=? OR in_my_library)) LIMIT 1"
+ "SELECT album_artist.album_artist_pid, store_id, sync_id, cloud_universal_library_id, sort_order, album_order_section FROM album_artist JOIN item ON (album_artist.representative_item_pid=item.item_pid) WHERE store_id != 0"
+ "SELECT album_artist.album_artist_pid, store_id, sync_id, cloud_universal_library_id, sort_order, sort_order_section FROM album_artist JOIN item ON (album_artist.representative_item_pid=item.item_pid) WHERE album_pid != 0"
+ "SELECT album_artist.album_artist_pid, store_id, sync_id, cloud_universal_library_id, sort_order, sort_order_section FROM album_artist JOIN item ON (album_artist.representative_item_pid=item.item_pid) WHERE cloud_universal_library_id != ''"
+ "SELECT album_artist.album_artist_pid, store_id, sync_id, cloud_universal_library_id, sort_order, sort_order_section FROM album_artist JOIN item ON (album_artist.representative_item_pid=item.item_pid) WHERE sync_id != 0"
+ "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type, artwork.artwork_variant_type FROM artwork LEFT OUTER JOIN best_artwork_token ON (artwork_token = available_artwork_token) WHERE artwork.artwork_type != ? AND artwork.artwork_variant_type = best_artwork_token.artwork_variant_type AND available_artwork_token IS NULL"
+ "SELECT cloud_library_id FROM album WHERE album_pid=?"
+ "SELECT cloud_universal_library_id FROM album_artist WHERE album_artist_pid=?"
+ "SELECT container_pid FROM container WHERE store_cloud_id=?"
+ "SELECT entity_pid, revision, revision_type, deleted FROM entity_revision WHERE revision > ? AND class = ?;"
+ "SELECT item.album_pid FROM item JOIN album ON (item.album_pid=album.album_pid) WHERE (in_my_library AND album.cloud_library_id=?) LIMIT 1"
+ "SELECT item_artist.item_artist_pid, store_id, sync_id, item_artist_order, item_artist_order_section, series_name_order, series_name_order_section FROM item_artist JOIN item ON (item_artist.representative_item_pid=item.item_pid) WHERE item_artist_pid != 0"
+ "SELECT item_artist.item_artist_pid, store_id, sync_id, item_artist_order, item_artist_order_section, series_name_order, series_name_order_section FROM item_artist JOIN item ON (item_artist.representative_item_pid=item.item_pid) WHERE store_id != 0"
+ "SELECT item_artist.item_artist_pid, store_id, sync_id, item_artist_order, item_artist_order_section, series_name_order, series_name_order_section FROM item_artist JOIN item ON (item_artist.representative_item_pid=item.item_pid) WHERE sync_id != 0"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) WHERE in_my_library AND store_saga_id=?"
+ "SELECT pin_pid FROM library_pins"
+ "SELECT pin_pid FROM library_pins WHERE entity_type=? AND entity_pid=?"
+ "SELECT pin_pid, entity_pid, entity_type from library_pins"
+ "SELECT pin_pid, entity_pid, entity_type, default_action, position, position_uuid FROM library_pins ORDER BY position"
+ "SELECT position from library_pins ORDER BY position ASC"
+ "SELECT smart_criteria FROM container WHERE container_pid=?"
+ "SELECT store_cloud_id FROM container WHERE container_pid=?"
+ "SELECT store_saga_id FROM item_store WHERE item_pid=?"
+ "SELECT value FROM _MLDatabaseProperties WHERE key='MLCloudLibraryMaxPinCount'"
+ "Skipping update for pin_pid=%lld, type=%{public}@, default_action=%{public}@, saga_id=%lld, cloud_library_id=%s"
+ "Starting to import pins from: %{public}@"
+ "T@\"MIPLibraryPin\",&,N,V_libraryPin"
+ "T@\"MIPPlaylist\",R,C,N,V_playlistItem"
+ "T@\"NSData\",R,N,V_libraryPinsData"
+ "T@\"NSString\",&,N,V_cloudLibraryID"
+ "T@\"NSString\",&,N,V_positionUUID"
+ "T^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?},R,N,V_moduleMethods"
+ "Tq,N,V_cloudItemID"
+ "Tq,N,V_defaultAction"
+ "Tq,N,V_entityType"
+ "Tq,N,V_position"
+ "Track"
+ "UPDATE album set keep_local=? WHERE album_pid=?"
+ "UPDATE container SET parent_pid=0 WHERE container_pid=?"
+ "UPDATE container set keep_local=? WHERE container_pid=?"
+ "UPDATE item set keep_local=?, keep_local_constraints=? WHERE (in_my_library AND keep_local < ? AND item.album_pid=?)"
+ "UPDATE item set keep_local=?, keep_local_constraints=? WHERE (in_my_library AND keep_local <= ? AND item.album_artist_pid=? AND media_type & ? != 0)"
+ "UPDATE item set keep_local=?, keep_local_constraints=? WHERE (item_pid=? AND keep_local <= ?)"
+ "UPDATE item set keep_local=?, keep_local_constraints=? WHERE keep_local < ? AND item_pid IN (SELECT item_pid FROM container_item WHERE container_pid=?)"
+ "UPDATE library_pins SET position=?, position_uuid=?, default_action=? WHERE pin_pid=?"
+ "We have holes in pin positions currentPosition=%d, position=%d"
+ "We have more pins(%lld) than the max allowed count(%lld)"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks Removing pinned album with PID=%lld as it no longer has library backed tracks"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks Removing pinned artist with PID=%lld as it no longer has library backed tracks"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks Removing pinned entity with PID=%lld failed with error=%{public}@"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks Removing pinned song with PID=%lld as it's no longer in library"
+ "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks hasSyncSource=%{BOOL}u, trackPID= %lld"
+ "[ML3RemoveCloudSourcesOperation] %{public}@ - Removing all library pins failed with error=%{public}@."
+ "[ML3RemovePlaylistsOperation] failed to remove containers from library pins. err=%{public}@"
+ "[Validation] Failed to create directory '%{public}@'. err=%{public}@"
+ "^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}"
+ "^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8"
+ "_checkoutConnection:ignoreSubPoolClosedState:"
+ "_cloudItemID"
+ "_cloudLibraryID"
+ "_defaultAction"
+ "_deleteRowsFromLibraryPinsTableForPersistentIDs:count:library:usingConnection:"
+ "_entityType"
+ "_isSubPoolClosed"
+ "_libraryPin"
+ "_libraryPinsData"
+ "_maxLibraryPinsCount"
+ "_playlistItem"
+ "_position"
+ "_processLibraryPinElement:"
+ "_processLibraryPinOperation:withImportSession:"
+ "_processMaxPinCount:"
+ "_processPinCount:"
+ "_processedLibraryPinsCount"
+ "_removeLibraryPinsForDeletedTracksUsingConnection:"
+ "_setError"
+ "_totalLibraryPinsCount"
+ "addContainer:persistentID:"
+ "addContainers cannot be called without an active session"
+ "addContainers:completion:"
+ "addContainersReturningResult:"
+ "adding pinnedEntity=%{public}s, _didFlushBeforeProcessingPinsPayload=%{BOOL}u"
+ "cannot add pin for source=%d"
+ "cannot update pin count for source=%d"
+ "clearSagaForcePerformDeltaSync"
+ "clearSagaMaxLibraryPinCount"
+ "cloudItemID"
+ "cloudLibraryID"
+ "collectionWithPersistentID:addedToLibrary:"
+ "com.apple.medialibrary.entity-revision-changed::%zu"
+ "defaultAction"
+ "deleteFromLibrary:deletionType:persistentIDs:count:preserveUndeletableEntities:"
+ "deleted library pin with pid=%lld, entity_pid=%lld, type=%{public}@"
+ "entityType"
+ "enumerateLibraryPinsPersistentIDsAfterRevision:revisionTrackingCode:usingBlock:"
+ "enumerateObjectsWithOptions:usingBlock:"
+ "exportLibraryPinWithCloudItemID:cloudLibraryID:defaultAtion:type:position:positionUUID:"
+ "failed to process library pin sync operation"
+ "failed to reconcile library pins"
+ "getBytes:range:"
+ "hasCloudItemID"
+ "hasCloudLibraryID"
+ "hasDefaultAction"
+ "hasEntityType"
+ "hasLibraryPin"
+ "hasPosition"
+ "hasPositionUUID"
+ "hasUserPinnedLibraryEntity"
+ "immersive_deep_link_url"
+ "initWithLibraryPath:trackData:playlistData:albumArtistData:albumData:libraryPinsData:clientIdentity:"
+ "initWithMultiverseIdentifier:playlistItem:"
+ "isFolder"
+ "item_store.immersive_deep_link_url"
+ "libraryPin"
+ "libraryPinImportItemFromDAAPElement:"
+ "libraryPinsData"
+ "library_pins"
+ "parentPlaylist"
+ "parentPlaylistPersistentIdsAndNames"
+ "playlistItem"
+ "playlist_folders"
+ "removeContainer:persistentID:"
+ "removeContainers cannot be called without an active session"
+ "removeContainers:completion:"
+ "removeContainersReturningResult:"
+ "sagaForcePerformDeltaSync"
+ "sagaIDTreeForPlaylistWithIdentifier:inLibrary:includeUndeletablePlaylists:"
+ "sagaIDTreeForPlaylistWithIdentifier:inLibrary:persistentIDsToIgnore:"
+ "sagaMaximumLibraryPinCount"
+ "saved %lu cloud, %lu store/sync id, %lu order mappings, %lu pidsToRemoveAfterReset for album"
+ "saved %lu cloud, %lu store/sync id, %lu order mappings, %lu pidsToRemoveAfterReset for album artist"
+ "saved %lu store/sync id, %lu order mappings, %lu series mappings for item artist"
+ "session:failedToAddContainer:shouldStop:"
+ "session:failedToRemoveContainer:shouldStop:"
+ "session:failedToUpdateContainer:shouldStop:"
+ "sessionFailedToAddContainer:completion:"
+ "sessionFailedToRemoveContainer:completion:"
+ "sessionFailedToUpdateContainer:completion:"
+ "setCloudItemID:"
+ "setCloudLibraryID:"
+ "setDefaultAction:"
+ "setEntityType:"
+ "setHasCloudItemID:"
+ "setHasDefaultAction:"
+ "setHasEntityType:"
+ "setHasPosition:"
+ "setLibraryPin:"
+ "setPosition:"
+ "setSagaForcePerformDeltaSync:"
+ "setSagaMaximumLibraryPinCount:"
+ "setSubPoolIsClosed"
+ "setting max allowed pins=%d"
+ "skip adding library pin=%s as it's not valid"
+ "skipping invalid library pin %s"
+ "skipping library pin sync operation of type=%d"
+ "starting import session with %lld tracks, %lld artists, %lld albums, %lld containers, %lld pins for update type %d, clientInitiatedReset=%d"
+ "updateContainer called for unknown container"
+ "updateContainer:persistentID:"
+ "updateContainers cannot be called without an active session"
+ "updateContainers:completion:"
+ "updateContainersReturningResult:"
+ "updated position=%lld, default_action=%{public}@, position_uuid=%s for for pin_pid=%lld, type=%{public}@, saga_id_id=%lld, cloud_id=%s"
+ "updating entity counts for import session: sessionStarted=%s, %lld tracks, %lld artists, %lld albums, %lld containers, %lld pins, %lld maxPinCount for update type %d"
+ "userUndeleteablePlaylistPersistentIDSInLibrary:"
+ "{?=\"cloudItemID\"b1\"defaultAction\"b1\"entityType\"b1\"position\"b1}"
+ "{?=\"trackAdds\"i\"trackUpdates\"i\"trackDeletes\"i\"playlistAdds\"i\"playlistDeletes\"i\"playlistUpdates\"i\"artistAdds\"i\"artistUpdates\"i\"albumUpdates\"i\"pinAdds\"i\"catalogPinAdds\"i\"totalSize\"I}"
+ "{map<unsigned int, unsigned long, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned long>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, unsigned long>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, unsigned long>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, unsigned long>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{shared_ptr<ML3DAAPImportItem>=^{ML3DAAPImportItem}^{__shared_weak_count}}80@0:8{shared_ptr<ML3CPP::Element>=^{Element}^{__shared_weak_count}}16{vector<long long, std::allocator<long long>>=^q^q^q}32{vector<std::unordered_set<std::string>, std::allocator<std::unordered_set<std::string>>>=^v^v^v}56"
+ "{unordered_map<long long, std::string, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, std::string>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, std::string>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, std::string>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, std::string>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, std::string>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__table_\"{__hash_table<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<long long, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<long long, std::allocator<long long>>=\"__begin_\"^q\"__end_\"^q\"__cap_\"^q}"
+ "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__cap_\"*}"
- "%@=\"com.apple.Music\" && %@ != \"*cloudID=*\" && %@ != \"*.content\""
- "@32@0:8@16^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}24"
- "B32@0:8@16^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}24"
- "B80@0:8{shared_ptr<ML3CPP::Element>=^{Element}^{__shared_weak_count}}16{vector<long long, std::allocator<long long>>=^q^q{__compressed_pair<long long *, std::allocator<long long>>=^q}}32{vector<std::unordered_set<std::string>, std::allocator<std::unordered_set<std::string>>>=^v^v{__compressed_pair<std::unordered_set<std::string> *, std::allocator<std::unordered_set<std::string>>>=^v}}56"
- "CREATE TABLE library_pins (pin_pid INTEGER PRIMARY KEY, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL DEFAULT 0, default_action INTEGER NOT NULL DEFAULT 0, saga_id INTEGER NOT NULL DEFAULT 0, cloud_library_id TEXT, position_uuid TEXT, UNIQUE (entity_pid, entity_type))"
- "Could not remove cloud_library_id from album_artist with persistentID:%lld, error=%{public}@"
- "DELETE FROM _MLDatabaseProperties WHERE key IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "Import Metrics: Finished Processing Album Artist Import in %2f seconds"
- "Import Metrics: Finished Processing Album Import in %2f seconds"
- "Late Night Mode"
- "LateNightMode"
- "ML3DatabaseConnectionSubPool=%p, maxConcurrentConnections=%lu, useReadOnlyConnections=%d, useDistantConnections=%d, busyConnections=%p, availableConnections=%p"
- "SELECT album_artist_order, album_artist_order_section from item where album_artist_pid=? LIMIT 1"
- "SELECT album_order, album_order_section FROM item where album_pid=? LIMIT 1"
- "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type, artwork.artwork_variant_type FROM artwork LEFT OUTER JOIN best_artwork_token ON (artwork_token = available_artwork_token) WHERE artwork.artwork_type != ? AND available_artwork_token IS NULL"
- "SELECT item_artist_order, item_artist_order_section, series_name_order, series_name_order_section from item where item_artist_pid=? LIMIT 1"
- "T^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?},R,N,V_moduleMethods"
- "UPDATE item_stats SET liked_state=0, liked_state_changed_date=0"
- "[ML3MusicLibrary+RemoveSourceOrTracks] ML3MusicLibrary+RemoveSourceOrTracks Removing source: %d, failed to clear item_stats properties. error: %@"
- "[ML3UpdateSpotlightIndexOperation] Corrupt data found previously donated, wiping the index and re-indexing everything"
- "[ML3UpdateSpotlightIndexOperation] Failed to fetch stale items from CSSearchQuery."
- "[ML3UpdateSpotlightIndexOperation] Making CSSearchQuery to check for stale items with corrupt data."
- "[ML3UpdateSpotlightIndexOperation] No corrupt data found that was previously donated"
- "^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}"
- "^{sqlite3_module=i^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16@0:8"
- "_checkIfPreviouslyDonatedStaleItemsWithCompletionBlock:"
- "attributeSet"
- "contentType"
- "initWithQueryString:queryContext:"
- "parsedStoreArtistItemImportProperties=%{public}@"
- "saved %lu cloud id, %lu store id mappings for existing album artists with %{public}@"
- "saved %lu cloud id, %lu store id mappings for existing album with %{public}@"
- "saved %lu id mappings for existing album artist name/section order"
- "saved %lu id mappings for existing album name/section order"
- "saved %lu name order mappings for existing artist name/section order"
- "saved %lu store id mappings for existing item artists with %{public}@"
- "setFetchAttributes:"
- "setFoundItemsHandler:"
- "starting import session with %lld tracks, %lld artists, %lld albums, %lld containers for update type %d, clientInitiatedReset=%d"
- "updating entity counts for import session: sessionStarted=%s, %lld tracks, %lld artists, %lld albums, %lld containers for update type %d"
- "v16@?0@\"NSArray\"8"
- "{?=\"trackAdds\"i\"trackUpdates\"i\"trackDeletes\"i\"playlistAdds\"i\"playlistDeletes\"i\"playlistUpdates\"i\"artistAdds\"i\"artistUpdates\"i\"albumUpdates\"i\"totalSize\"I}"
- "{map<unsigned int, unsigned long, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned long>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, unsigned long>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, unsigned long>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, unsigned long>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned int, unsigned long>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, unsigned long>, std::less<unsigned int>>>=\"__value_\"Q}}}"
- "{shared_ptr<ML3DAAPImportItem>=^{ML3DAAPImportItem}^{__shared_weak_count}}80@0:8{shared_ptr<ML3CPP::Element>=^{Element}^{__shared_weak_count}}16{vector<long long, std::allocator<long long>>=^q^q{__compressed_pair<long long *, std::allocator<long long>>=^q}}32{vector<std::unordered_set<std::string>, std::allocator<std::unordered_set<std::string>>>=^v^v{__compressed_pair<std::unordered_set<std::string> *, std::allocator<std::unordered_set<std::string>>>=^v}}56"
- "{unordered_map<long long, std::string, std::hash<long long>, std::equal_to<long long>, std::allocator<std::pair<const long long, std::string>>>=\"__table_\"{__hash_table<std::__hash_value_type<long long, std::string>, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, std::string>, std::hash<long long>, std::equal_to<long long>>, std::__unordered_map_equal<long long, std::__hash_value_type<long long, std::string>, std::equal_to<long long>, std::hash<long long>>, std::allocator<std::__hash_value_type<long long, std::string>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<long long, std::string>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long long, std::string>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<long long, std::__hash_value_type<long long, std::string>, std::hash<long long>, std::equal_to<long long>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<long long, std::__hash_value_type<long long, std::string>, std::equal_to<long long>, std::hash<long long>>>=\"__value_\"f}}}"
- "{unordered_set<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__table_\"{__hash_table<long long, std::hash<long long>, std::equal_to<long long>, std::allocator<long long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<long long, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<long long, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<long long, void *> *>, std::allocator<std::__hash_node<long long, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<long long, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::hash<long long>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::equal_to<long long>>=\"__value_\"f}}}"
- "{vector<long long, std::allocator<long long>>=\"__begin_\"^q\"__end_\"^q\"__end_cap_\"{__compressed_pair<long long *, std::allocator<long long>>=\"__value_\"^q}}"
- "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__end_cap_\"{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=\"__value_\"*}}"

```
