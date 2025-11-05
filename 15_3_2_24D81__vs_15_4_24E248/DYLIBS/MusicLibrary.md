## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Versions/A/MusicLibrary`

```diff

-4024.300.23.0.0
-  __TEXT.__text: 0x1f7774
+4024.500.35.0.0
+  __TEXT.__text: 0x1f92c8
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0xd554
-  __TEXT.__const: 0x6302
-  __TEXT.__gcc_except_tab: 0x1312c
-  __TEXT.__cstring: 0x63df8
-  __TEXT.__oslogstring: 0x187d7
-  __TEXT.__ustring: 0xc
+  __TEXT.__objc_methlist: 0xdccc
+  __TEXT.__const: 0x6342
   __TEXT.__dlopen_cstrs: 0xec
-  __TEXT.__unwind_info: 0x68f8
-  __TEXT.__objc_classname: 0x18e0
-  __TEXT.__objc_methname: 0x1d09a
-  __TEXT.__objc_methtype: 0x50b9
-  __TEXT.__objc_stubs: 0x13980
-  __DATA_CONST.__got: 0xa20
-  __DATA_CONST.__const: 0x5658
-  __DATA_CONST.__objc_classlist: 0x6d0
+  __TEXT.__gcc_except_tab: 0x132d0
+  __TEXT.__cstring: 0x65a58
+  __TEXT.__oslogstring: 0x18c79
+  __TEXT.__ustring: 0xc
+  __TEXT.__unwind_info: 0x6888
+  __TEXT.__objc_classname: 0x1929
+  __TEXT.__objc_methname: 0x1da78
+  __TEXT.__objc_methtype: 0x5248
+  __TEXT.__objc_stubs: 0x13b80
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x5670
+  __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6718
+  __DATA_CONST.__objc_selrefs: 0x68a0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x500
-  __DATA_CONST.__objc_arraydata: 0x1098
+  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_arraydata: 0x10b8
   __AUTH_CONST.__auth_got: 0xd68
-  __AUTH_CONST.__const: 0xb9b0
-  __AUTH_CONST.__cfstring: 0x21740
-  __AUTH_CONST.__objc_const: 0x15438
+  __AUTH_CONST.__const: 0xba90
+  __AUTH_CONST.__cfstring: 0x21e60
+  __AUTH_CONST.__objc_const: 0x14e28
   __AUTH_CONST.__objc_arrayobj: 0x20b8
-  __AUTH_CONST.__objc_intobj: 0x1a88
+  __AUTH_CONST.__objc_intobj: 0x1b30
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4420
+  __AUTH.__objc_data: 0x44c0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xe34
+  __DATA.__objc_ivar: 0xe78
   __DATA.__data: 0xac0
-  __DATA.__bss: 0xd90
+  __DATA.__bss: 0xda0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CB364CE4-3D90-33FC-AD5A-065A52C6ED73
-  Functions: 7769
-  Symbols:   16501
-  CStrings:  15962
+  UUID: CA830152-4FE0-3A62-BFBE-BA46B62C736E
+  Functions: 7748
+  Symbols:   16613
+  CStrings:  16160
 
Symbols:
+ +[ML3MusicLibrary(Artwork) artworkRelativePathFromToken:variantType:]
+ -[ML3Artwork initWithToken:artworkType:variantType:musicLibrary:]
+ -[ML3Artwork initWithToken:relativePath:artworkType:variantType:musicLibrary:]
+ -[ML3Artwork variantType]
+ -[ML3ArtworkConfiguration _supportedSizeKeysForMediaType:artworkType:artworkVariantType:]
+ -[ML3ArtworkConfiguration sizesToAutogenerateForMediaType:artworkType:artworkVariantType:]
+ -[ML3ArtworkConfiguration supportedSizesForMediaType:artworkType:artworkVariantType:]
+ -[ML3ArtworkTokenSet initWithEntity:artworkType:artworkVariantType:]
+ -[ML3AsyncDatabaseOperation .cxx_destruct]
+ -[ML3AsyncDatabaseOperation _execute]
+ -[ML3AsyncDatabaseOperation _verifyLibraryAndAttributesProperties:]
+ -[ML3AsyncDatabaseOperation cancel]
+ -[ML3AsyncDatabaseOperation error]
+ -[ML3AsyncDatabaseOperation execute]
+ -[ML3AsyncDatabaseOperation finishWithError:]
+ -[ML3AsyncDatabaseOperation finish]
+ -[ML3AsyncDatabaseOperation initWithLibrary:writer:]
+ -[ML3AsyncDatabaseOperation isAsynchronous]
+ -[ML3AsyncDatabaseOperation isCancelled]
+ -[ML3AsyncDatabaseOperation isConcurrent]
+ -[ML3AsyncDatabaseOperation isExecuting]
+ -[ML3AsyncDatabaseOperation isFinished]
+ -[ML3AsyncDatabaseOperation start]
+ -[ML3AsyncDatabaseOperation success]
+ -[ML3MediaLibraryWriter cancelDatabaseOperationsForClient:completion:]
+ -[ML3MusicLibrary _autogenerateArtworkForRelativePath:artworkType:mediaType:variantType:completionHandler:]
+ -[ML3MusicLibrary _determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:variantType:usingConnection:]
+ -[ML3MusicLibrary _insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:]
+ -[ML3MusicLibrary _insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:usingConnection:]
+ -[ML3MusicLibrary _updateBestArtworkTokensForArtworkToken:artworkType:sourceType:variantType:preserveExistingAvailableToken:usingConnection:]
+ -[ML3MusicLibrary enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:usingBlock:]
+ -[ML3MusicLibrary importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:]
+ -[ML3MusicLibrary importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:usingConnection:]
+ -[ML3MusicLibrary importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:variantType:]
+ -[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]
+ -[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]
+ -[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]
+ -[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]
+ -[ML3MusicLibrary isArtworkTokenAvailable:forVariantType:]
+ -[ML3MusicLibrary retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:completionHandler:]
+ -[ML3MusicLibrary updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:preserveExistingAvailableToken:usingConnection:]
+ -[ML3MusicLibrary(Maintenance) performMainentanceTasksUsingActivity:]
+ -[ML3SpotlightBatchDonationObject .cxx_destruct]
+ -[ML3SpotlightBatchDonationObject currentRevision]
+ -[ML3SpotlightBatchDonationObject entityStringsToDelete]
+ -[ML3SpotlightBatchDonationObject initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:]
+ -[ML3SpotlightBatchDonationObject playlistsPersistentIDsToUpdate]
+ -[ML3SpotlightBatchDonationObject targetRevision]
+ -[ML3SpotlightBatchDonationObject trackPersistentIDsToUpdate]
+ -[MLMediaLibraryService performMaintenanceTasksForDatabaseAtPath:]
+ GCC_except_table1008
+ GCC_except_table1012
+ GCC_except_table1017
+ GCC_except_table1021
+ GCC_except_table103
+ GCC_except_table1030
+ GCC_except_table104
+ GCC_except_table1046
+ GCC_except_table105
+ GCC_except_table1050
+ GCC_except_table1054
+ GCC_except_table1065
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table1391
+ GCC_except_table14
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table1435
+ GCC_except_table1437
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table1464
+ GCC_except_table1471
+ GCC_except_table1480
+ GCC_except_table1486
+ GCC_except_table150
+ GCC_except_table1507
+ GCC_except_table151
+ GCC_except_table1511
+ GCC_except_table1520
+ GCC_except_table1525
+ GCC_except_table1546
+ GCC_except_table1548
+ GCC_except_table1550
+ GCC_except_table156
+ GCC_except_table1560
+ GCC_except_table1562
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1572
+ GCC_except_table1576
+ GCC_except_table159
+ GCC_except_table1593
+ GCC_except_table1602
+ GCC_except_table1605
+ GCC_except_table1618
+ GCC_except_table1628
+ GCC_except_table1641
+ GCC_except_table1659
+ GCC_except_table1661
+ GCC_except_table1677
+ GCC_except_table1681
+ GCC_except_table1687
+ GCC_except_table1690
+ GCC_except_table1711
+ GCC_except_table1716
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1726
+ GCC_except_table1728
+ GCC_except_table1730
+ GCC_except_table1737
+ GCC_except_table1740
+ GCC_except_table1741
+ GCC_except_table1742
+ GCC_except_table1744
+ GCC_except_table1751
+ GCC_except_table1783
+ GCC_except_table1788
+ GCC_except_table1796
+ GCC_except_table1798
+ GCC_except_table1803
+ GCC_except_table1812
+ GCC_except_table1819
+ GCC_except_table1866
+ GCC_except_table1868
+ GCC_except_table1890
+ GCC_except_table1898
+ GCC_except_table1902
+ GCC_except_table1913
+ GCC_except_table1928
+ GCC_except_table1937
+ GCC_except_table1939
+ GCC_except_table1973
+ GCC_except_table20
+ GCC_except_table2009
+ GCC_except_table2010
+ GCC_except_table2013
+ GCC_except_table2014
+ GCC_except_table2030
+ GCC_except_table2039
+ GCC_except_table2043
+ GCC_except_table2046
+ GCC_except_table2047
+ GCC_except_table2061
+ GCC_except_table2063
+ GCC_except_table2077
+ GCC_except_table2078
+ GCC_except_table2079
+ GCC_except_table2089
+ GCC_except_table2095
+ GCC_except_table2096
+ GCC_except_table2097
+ GCC_except_table2098
+ GCC_except_table2099
+ GCC_except_table2100
+ GCC_except_table2101
+ GCC_except_table2102
+ GCC_except_table2108
+ GCC_except_table2130
+ GCC_except_table2131
+ GCC_except_table2132
+ GCC_except_table2133
+ GCC_except_table2138
+ GCC_except_table2139
+ GCC_except_table2140
+ GCC_except_table2147
+ GCC_except_table2149
+ GCC_except_table2151
+ GCC_except_table2161
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2171
+ GCC_except_table2175
+ GCC_except_table2183
+ GCC_except_table2195
+ GCC_except_table2199
+ GCC_except_table2200
+ GCC_except_table2212
+ GCC_except_table2213
+ GCC_except_table2214
+ GCC_except_table2218
+ GCC_except_table2219
+ GCC_except_table2220
+ GCC_except_table2221
+ GCC_except_table2228
+ GCC_except_table2229
+ GCC_except_table2230
+ GCC_except_table2231
+ GCC_except_table2232
+ GCC_except_table2234
+ GCC_except_table2235
+ GCC_except_table2236
+ GCC_except_table2237
+ GCC_except_table2238
+ GCC_except_table2242
+ GCC_except_table2243
+ GCC_except_table2260
+ GCC_except_table2268
+ GCC_except_table2271
+ GCC_except_table2272
+ GCC_except_table2273
+ GCC_except_table2274
+ GCC_except_table2275
+ GCC_except_table2277
+ GCC_except_table2278
+ GCC_except_table2284
+ GCC_except_table2285
+ GCC_except_table2435
+ GCC_except_table2439
+ GCC_except_table2498
+ GCC_except_table2514
+ GCC_except_table2527
+ GCC_except_table2532
+ GCC_except_table2547
+ GCC_except_table2558
+ GCC_except_table2564
+ GCC_except_table2571
+ GCC_except_table2577
+ GCC_except_table2581
+ GCC_except_table2587
+ GCC_except_table2593
+ GCC_except_table2594
+ GCC_except_table2595
+ GCC_except_table2818
+ GCC_except_table2866
+ GCC_except_table2869
+ GCC_except_table2874
+ GCC_except_table2897
+ GCC_except_table2926
+ GCC_except_table2943
+ GCC_except_table2946
+ GCC_except_table2957
+ GCC_except_table2959
+ GCC_except_table2961
+ GCC_except_table2964
+ GCC_except_table2967
+ GCC_except_table3000
+ GCC_except_table3003
+ GCC_except_table3013
+ GCC_except_table3015
+ GCC_except_table3016
+ GCC_except_table3061
+ GCC_except_table3081
+ GCC_except_table3082
+ GCC_except_table3083
+ GCC_except_table3091
+ GCC_except_table3092
+ GCC_except_table3098
+ GCC_except_table3099
+ GCC_except_table3100
+ GCC_except_table3101
+ GCC_except_table3102
+ GCC_except_table3103
+ GCC_except_table3111
+ GCC_except_table3112
+ GCC_except_table3115
+ GCC_except_table3151
+ GCC_except_table3157
+ GCC_except_table3161
+ GCC_except_table3164
+ GCC_except_table3167
+ GCC_except_table3171
+ GCC_except_table3173
+ GCC_except_table3184
+ GCC_except_table3186
+ GCC_except_table3188
+ GCC_except_table3195
+ GCC_except_table3196
+ GCC_except_table3206
+ GCC_except_table3208
+ GCC_except_table3211
+ GCC_except_table3215
+ GCC_except_table3257
+ GCC_except_table3279
+ GCC_except_table3300
+ GCC_except_table3307
+ GCC_except_table3330
+ GCC_except_table3331
+ GCC_except_table3332
+ GCC_except_table3336
+ GCC_except_table3339
+ GCC_except_table3340
+ GCC_except_table3341
+ GCC_except_table3342
+ GCC_except_table3343
+ GCC_except_table3347
+ GCC_except_table3348
+ GCC_except_table3351
+ GCC_except_table3352
+ GCC_except_table3353
+ GCC_except_table3354
+ GCC_except_table3364
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3381
+ GCC_except_table3384
+ GCC_except_table3385
+ GCC_except_table3387
+ GCC_except_table3388
+ GCC_except_table3389
+ GCC_except_table3394
+ GCC_except_table3395
+ GCC_except_table3396
+ GCC_except_table3397
+ GCC_except_table3398
+ GCC_except_table3412
+ GCC_except_table3437
+ GCC_except_table3472
+ GCC_except_table3771
+ GCC_except_table3781
+ GCC_except_table3783
+ GCC_except_table3806
+ GCC_except_table3808
+ GCC_except_table3818
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table3977
+ GCC_except_table3986
+ GCC_except_table3989
+ GCC_except_table3992
+ GCC_except_table4001
+ GCC_except_table4004
+ GCC_except_table4005
+ GCC_except_table4006
+ GCC_except_table4011
+ GCC_except_table402
+ GCC_except_table4021
+ GCC_except_table4032
+ GCC_except_table405
+ GCC_except_table4053
+ GCC_except_table4059
+ GCC_except_table4063
+ GCC_except_table4067
+ GCC_except_table4070
+ GCC_except_table4073
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table42
+ GCC_except_table4242
+ GCC_except_table4256
+ GCC_except_table4259
+ GCC_except_table4261
+ GCC_except_table4262
+ GCC_except_table4264
+ GCC_except_table4268
+ GCC_except_table427
+ GCC_except_table4279
+ GCC_except_table428
+ GCC_except_table4283
+ GCC_except_table4302
+ GCC_except_table4304
+ GCC_except_table433
+ GCC_except_table4449
+ GCC_except_table445
+ GCC_except_table4460
+ GCC_except_table4467
+ GCC_except_table4468
+ GCC_except_table4469
+ GCC_except_table4475
+ GCC_except_table4542
+ GCC_except_table4543
+ GCC_except_table4544
+ GCC_except_table4549
+ GCC_except_table4557
+ GCC_except_table4571
+ GCC_except_table4576
+ GCC_except_table458
+ GCC_except_table4590
+ GCC_except_table4591
+ GCC_except_table4592
+ GCC_except_table464
+ GCC_except_table4700
+ GCC_except_table4704
+ GCC_except_table4707
+ GCC_except_table4725
+ GCC_except_table4726
+ GCC_except_table4727
+ GCC_except_table4728
+ GCC_except_table4841
+ GCC_except_table4843
+ GCC_except_table4847
+ GCC_except_table4849
+ GCC_except_table4851
+ GCC_except_table4852
+ GCC_except_table4853
+ GCC_except_table4925
+ GCC_except_table4928
+ GCC_except_table4937
+ GCC_except_table4938
+ GCC_except_table4953
+ GCC_except_table4954
+ GCC_except_table4970
+ GCC_except_table4971
+ GCC_except_table4972
+ GCC_except_table4973
+ GCC_except_table4974
+ GCC_except_table4975
+ GCC_except_table4977
+ GCC_except_table498
+ GCC_except_table4981
+ GCC_except_table4983
+ GCC_except_table4986
+ GCC_except_table4988
+ GCC_except_table499
+ GCC_except_table4990
+ GCC_except_table4991
+ GCC_except_table4992
+ GCC_except_table4993
+ GCC_except_table4994
+ GCC_except_table4996
+ GCC_except_table4997
+ GCC_except_table4998
+ GCC_except_table5010
+ GCC_except_table5015
+ GCC_except_table5053
+ GCC_except_table5057
+ GCC_except_table5059
+ GCC_except_table506
+ GCC_except_table5061
+ GCC_except_table5063
+ GCC_except_table5066
+ GCC_except_table5068
+ GCC_except_table507
+ GCC_except_table5071
+ GCC_except_table5073
+ GCC_except_table5077
+ GCC_except_table5079
+ GCC_except_table5086
+ GCC_except_table5091
+ GCC_except_table5098
+ GCC_except_table5114
+ GCC_except_table5119
+ GCC_except_table5124
+ GCC_except_table5133
+ GCC_except_table5134
+ GCC_except_table5135
+ GCC_except_table5137
+ GCC_except_table5143
+ GCC_except_table5206
+ GCC_except_table5209
+ GCC_except_table5211
+ GCC_except_table5212
+ GCC_except_table5214
+ GCC_except_table5216
+ GCC_except_table5218
+ GCC_except_table5219
+ GCC_except_table5298
+ GCC_except_table5302
+ GCC_except_table5306
+ GCC_except_table5307
+ GCC_except_table5309
+ GCC_except_table5324
+ GCC_except_table5325
+ GCC_except_table5327
+ GCC_except_table5331
+ GCC_except_table5338
+ GCC_except_table5340
+ GCC_except_table5342
+ GCC_except_table5343
+ GCC_except_table5344
+ GCC_except_table5345
+ GCC_except_table5349
+ GCC_except_table5350
+ GCC_except_table5364
+ GCC_except_table5400
+ GCC_except_table5409
+ GCC_except_table5416
+ GCC_except_table546
+ GCC_except_table549
+ GCC_except_table5522
+ GCC_except_table5528
+ GCC_except_table5534
+ GCC_except_table554
+ GCC_except_table5540
+ GCC_except_table5546
+ GCC_except_table5547
+ GCC_except_table5548
+ GCC_except_table555
+ GCC_except_table5554
+ GCC_except_table5555
+ GCC_except_table5561
+ GCC_except_table5567
+ GCC_except_table5572
+ GCC_except_table5573
+ GCC_except_table5581
+ GCC_except_table5590
+ GCC_except_table5596
+ GCC_except_table5599
+ GCC_except_table561
+ GCC_except_table5625
+ GCC_except_table5653
+ GCC_except_table566
+ GCC_except_table5661
+ GCC_except_table567
+ GCC_except_table5674
+ GCC_except_table5682
+ GCC_except_table570
+ GCC_except_table5710
+ GCC_except_table5755
+ GCC_except_table5759
+ GCC_except_table5766
+ GCC_except_table5771
+ GCC_except_table5772
+ GCC_except_table5778
+ GCC_except_table578
+ GCC_except_table5781
+ GCC_except_table5783
+ GCC_except_table5784
+ GCC_except_table5810
+ GCC_except_table5811
+ GCC_except_table5812
+ GCC_except_table5813
+ GCC_except_table586
+ GCC_except_table5868
+ GCC_except_table5869
+ GCC_except_table5871
+ GCC_except_table5872
+ GCC_except_table5873
+ GCC_except_table5874
+ GCC_except_table5875
+ GCC_except_table5876
+ GCC_except_table5877
+ GCC_except_table5879
+ GCC_except_table588
+ GCC_except_table5881
+ GCC_except_table5883
+ GCC_except_table5886
+ GCC_except_table5888
+ GCC_except_table5889
+ GCC_except_table592
+ GCC_except_table5930
+ GCC_except_table5975
+ GCC_except_table5976
+ GCC_except_table6004
+ GCC_except_table6009
+ GCC_except_table6012
+ GCC_except_table6017
+ GCC_except_table6019
+ GCC_except_table602
+ GCC_except_table6020
+ GCC_except_table6021
+ GCC_except_table6022
+ GCC_except_table6025
+ GCC_except_table6026
+ GCC_except_table6027
+ GCC_except_table6028
+ GCC_except_table6031
+ GCC_except_table6032
+ GCC_except_table6033
+ GCC_except_table6034
+ GCC_except_table6037
+ GCC_except_table6040
+ GCC_except_table6045
+ GCC_except_table6047
+ GCC_except_table6048
+ GCC_except_table6050
+ GCC_except_table6051
+ GCC_except_table6053
+ GCC_except_table6054
+ GCC_except_table6055
+ GCC_except_table6056
+ GCC_except_table6058
+ GCC_except_table6059
+ GCC_except_table6060
+ GCC_except_table6061
+ GCC_except_table6072
+ GCC_except_table6073
+ GCC_except_table6074
+ GCC_except_table609
+ GCC_except_table6093
+ GCC_except_table6094
+ GCC_except_table6097
+ GCC_except_table6099
+ GCC_except_table6101
+ GCC_except_table6104
+ GCC_except_table611
+ GCC_except_table6110
+ GCC_except_table6134
+ GCC_except_table6137
+ GCC_except_table615
+ GCC_except_table6160
+ GCC_except_table618
+ GCC_except_table6210
+ GCC_except_table6212
+ GCC_except_table6219
+ GCC_except_table6220
+ GCC_except_table6221
+ GCC_except_table6222
+ GCC_except_table6225
+ GCC_except_table6233
+ GCC_except_table6235
+ GCC_except_table6236
+ GCC_except_table6237
+ GCC_except_table6245
+ GCC_except_table6251
+ GCC_except_table6259
+ GCC_except_table626
+ GCC_except_table6261
+ GCC_except_table6263
+ GCC_except_table6266
+ GCC_except_table6269
+ GCC_except_table6281
+ GCC_except_table6282
+ GCC_except_table6284
+ GCC_except_table6285
+ GCC_except_table629
+ GCC_except_table6294
+ GCC_except_table6298
+ GCC_except_table6306
+ GCC_except_table6312
+ GCC_except_table6317
+ GCC_except_table6323
+ GCC_except_table6324
+ GCC_except_table6325
+ GCC_except_table6326
+ GCC_except_table6327
+ GCC_except_table6328
+ GCC_except_table6329
+ GCC_except_table6330
+ GCC_except_table6336
+ GCC_except_table6339
+ GCC_except_table634
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6342
+ GCC_except_table6343
+ GCC_except_table6346
+ GCC_except_table6349
+ GCC_except_table6351
+ GCC_except_table6353
+ GCC_except_table6354
+ GCC_except_table6365
+ GCC_except_table6368
+ GCC_except_table6369
+ GCC_except_table6387
+ GCC_except_table6406
+ GCC_except_table6408
+ GCC_except_table6409
+ GCC_except_table6410
+ GCC_except_table6411
+ GCC_except_table6412
+ GCC_except_table6414
+ GCC_except_table6424
+ GCC_except_table6427
+ GCC_except_table643
+ GCC_except_table6431
+ GCC_except_table6432
+ GCC_except_table6433
+ GCC_except_table6443
+ GCC_except_table6445
+ GCC_except_table6447
+ GCC_except_table6451
+ GCC_except_table6455
+ GCC_except_table6463
+ GCC_except_table6467
+ GCC_except_table6469
+ GCC_except_table6471
+ GCC_except_table6473
+ GCC_except_table6488
+ GCC_except_table6489
+ GCC_except_table6490
+ GCC_except_table6492
+ GCC_except_table6494
+ GCC_except_table6496
+ GCC_except_table6498
+ GCC_except_table6500
+ GCC_except_table6502
+ GCC_except_table6504
+ GCC_except_table6506
+ GCC_except_table6508
+ GCC_except_table6510
+ GCC_except_table6511
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table659
+ GCC_except_table662
+ GCC_except_table6632
+ GCC_except_table6637
+ GCC_except_table6653
+ GCC_except_table6655
+ GCC_except_table6670
+ GCC_except_table668
+ GCC_except_table6683
+ GCC_except_table6684
+ GCC_except_table6685
+ GCC_except_table6721
+ GCC_except_table6722
+ GCC_except_table6728
+ GCC_except_table6729
+ GCC_except_table6735
+ GCC_except_table6737
+ GCC_except_table6744
+ GCC_except_table6745
+ GCC_except_table6746
+ GCC_except_table6747
+ GCC_except_table6748
+ GCC_except_table6754
+ GCC_except_table6755
+ GCC_except_table6756
+ GCC_except_table6767
+ GCC_except_table6768
+ GCC_except_table6769
+ GCC_except_table6770
+ GCC_except_table6771
+ GCC_except_table6772
+ GCC_except_table6773
+ GCC_except_table6774
+ GCC_except_table6775
+ GCC_except_table6776
+ GCC_except_table6781
+ GCC_except_table6782
+ GCC_except_table6788
+ GCC_except_table6789
+ GCC_except_table6790
+ GCC_except_table6791
+ GCC_except_table6793
+ GCC_except_table6798
+ GCC_except_table6800
+ GCC_except_table6821
+ GCC_except_table6843
+ GCC_except_table6865
+ GCC_except_table6881
+ GCC_except_table6905
+ GCC_except_table6928
+ GCC_except_table6929
+ GCC_except_table6930
+ GCC_except_table6993
+ GCC_except_table7021
+ GCC_except_table7141
+ GCC_except_table7227
+ GCC_except_table726
+ GCC_except_table7297
+ GCC_except_table7303
+ GCC_except_table7309
+ GCC_except_table7310
+ GCC_except_table7311
+ GCC_except_table733
+ GCC_except_table7376
+ GCC_except_table7382
+ GCC_except_table7386
+ GCC_except_table739
+ GCC_except_table741
+ GCC_except_table748
+ GCC_except_table753
+ GCC_except_table757
+ GCC_except_table760
+ GCC_except_table768
+ GCC_except_table7689
+ GCC_except_table7690
+ GCC_except_table7691
+ GCC_except_table7697
+ GCC_except_table7699
+ GCC_except_table7700
+ GCC_except_table7703
+ GCC_except_table771
+ GCC_except_table781
+ GCC_except_table784
+ GCC_except_table790
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table808
+ GCC_except_table814
+ GCC_except_table820
+ GCC_except_table83
+ GCC_except_table855
+ GCC_except_table91
+ GCC_except_table920
+ GCC_except_table924
+ GCC_except_table932
+ GCC_except_table958
+ GCC_except_table96
+ GCC_except_table962
+ GCC_except_table969
+ GCC_except_table973
+ MSVFastHexStringFromBytes.hexCharacters.25562
+ OBJC_IVAR_$_ML3Artwork._variantType
+ OBJC_IVAR_$_ML3ArtworkTokenSet._artworkVariantType
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._cancelled
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._error
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._executing
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._finished
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._lock
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._startTime
+ OBJC_IVAR_$_ML3AsyncDatabaseOperation._success
+ OBJC_IVAR_$_ML3MediaLibraryWriter._activeSiriIndexOperation
+ OBJC_IVAR_$_ML3MediaLibraryWriter._activeSpotlightIndexOperation
+ OBJC_IVAR_$_ML3MediaLibraryWriter._lock
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._currentRevision
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._entityStringsToDelete
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._playlistsPersistentIDsToUpdate
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._targetRevision
+ OBJC_IVAR_$_ML3SpotlightBatchDonationObject._trackPersistentIDsToUpdate
+ _ML3ArtworkConfigurationArtworkVariantTypeForString
+ _ML3ArtworkConfigurationStringForArtworkVariantType
+ _ML3ContainerPropertyEditSessionID
+ _ML3MigrationFunction2220020to2240000
+ _ML3MigrationFunction2240000to2240010
+ _ML3MigrationFunction2240010to2240020
+ _ML3MigrationFunction2240020to2240030
+ _ML3MigrationFunction2240030to2240031
+ _ML3MigrationFunction2240031to2240032
+ _MSV_XXH_XXH32_update.25554
+ _MSV_XXH_XXH64_digest.25559
+ _MSV_XXH_XXH64_update.25555
+ _OBJC_CLASS_$_ML3AsyncDatabaseOperation
+ _OBJC_CLASS_$_ML3SpotlightBatchDonationObject
+ _OBJC_METACLASS_$_ML3AsyncDatabaseOperation
+ _OBJC_METACLASS_$_ML3SpotlightBatchDonationObject
+ __136-[ML3MusicLibrary enumeratePersistentIDsAfterRevision:revisionTrackingCode:maximumRevisionType:forMediaTypes:inUsersLibrary:usingBlock:]_block_invoke.663
+ __141-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.729
+ __143-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke.745
+ __152-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]_block_invoke.737
+ __43-[MLMediaLibraryService _serviceConnection]_block_invoke.321
+ __47-[ML3MusicLibrary _tearDownNotificationManager]_block_invoke.1074
+ __47-[ML3MusicLibrary removeArtworkAssetWithToken:]_block_invoke.755
+ __52-[ML3MusicLibrary removeOrphanedTracksOnlyInCaches:]_block_invoke.832
+ __59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.520
+ __59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.546
+ __59-[ML3ProtoSyncImportOperation _unlinkUnavailableMediaItems]_block_invoke.44
+ __62+[ML3Container populateMediaTypesOfStaticContainersInLibrary:]_block_invoke.550
+ __63-[ML3MusicLibrary _removeOrphanedArtworkAssetsUsingConnection:]_block_invoke.1043
+ __65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.1012
+ __65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.1023
+ __65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.1030
+ __66-[ML3Container setValues:forProperties:async:withCompletionBlock:]_block_invoke.462
+ __76-[ML3MusicLibrary sanitizeSortMapContentsUsingConnection:didSortMapEntries:]_block_invoke.972
+ __77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.768
+ __77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.769
+ __79-[MLMediaLibraryService mediaLibraryResourcesServiceListenerEndpointWithError:]_block_invoke.277
+ __79-[MLMediaLibraryService mediaLibraryResourcesServiceListenerEndpointWithError:]_block_invoke.296
+ __85-[ML3ArtworkConfiguration supportedSizesForMediaType:artworkType:artworkVariantType:]_block_invoke.35
+ __93-[ML3Container setItemReactionText:onEntryAtPosition:forUserIdentifier:previousReactionText:]_block_invoke.628
+ __99-[ML3MusicLibrary autogenerateSupportedSizesForAllOriginalArtworkWithConnection:completionHandler:]_block_invoke.698
+ __99-[ML3MusicLibrary enumerateArtworkRelativePathsWithConnection:matchingRelativePathContainer:block:]_block_invoke.716
+ __Block_byref_object_copy_.10805
+ __Block_byref_object_copy_.10914
+ __Block_byref_object_copy_.11771
+ __Block_byref_object_copy_.11933
+ __Block_byref_object_copy_.12755
+ __Block_byref_object_copy_.13764
+ __Block_byref_object_copy_.1521
+ __Block_byref_object_copy_.16207
+ __Block_byref_object_copy_.16540
+ __Block_byref_object_copy_.17056
+ __Block_byref_object_copy_.17885
+ __Block_byref_object_copy_.18282
+ __Block_byref_object_copy_.18538
+ __Block_byref_object_copy_.19415
+ __Block_byref_object_copy_.19772
+ __Block_byref_object_copy_.20863
+ __Block_byref_object_copy_.21628
+ __Block_byref_object_copy_.23423
+ __Block_byref_object_copy_.23506
+ __Block_byref_object_copy_.2360
+ __Block_byref_object_copy_.23613
+ __Block_byref_object_copy_.23894
+ __Block_byref_object_copy_.24260
+ __Block_byref_object_copy_.2458
+ __Block_byref_object_copy_.25692
+ __Block_byref_object_copy_.26531
+ __Block_byref_object_copy_.282
+ __Block_byref_object_copy_.295
+ __Block_byref_object_copy_.298
+ __Block_byref_object_copy_.361
+ __Block_byref_object_copy_.3757
+ __Block_byref_object_copy_.388
+ __Block_byref_object_copy_.407
+ __Block_byref_object_copy_.4636
+ __Block_byref_object_copy_.473
+ __Block_byref_object_copy_.4829
+ __Block_byref_object_copy_.5950
+ __Block_byref_object_copy_.597
+ __Block_byref_object_copy_.604
+ __Block_byref_object_copy_.611
+ __Block_byref_object_copy_.615
+ __Block_byref_object_copy_.7166
+ __Block_byref_object_copy_.7256
+ __Block_byref_object_copy_.7844
+ __Block_byref_object_copy_.8434
+ __Block_byref_object_copy_.8915
+ __Block_byref_object_copy_.9024
+ __Block_byref_object_copy_.9108
+ __Block_byref_object_copy_.9980
+ __Block_byref_object_dispose_.10806
+ __Block_byref_object_dispose_.10915
+ __Block_byref_object_dispose_.11772
+ __Block_byref_object_dispose_.11934
+ __Block_byref_object_dispose_.12756
+ __Block_byref_object_dispose_.13765
+ __Block_byref_object_dispose_.1522
+ __Block_byref_object_dispose_.16208
+ __Block_byref_object_dispose_.16541
+ __Block_byref_object_dispose_.17057
+ __Block_byref_object_dispose_.17886
+ __Block_byref_object_dispose_.18283
+ __Block_byref_object_dispose_.18539
+ __Block_byref_object_dispose_.19416
+ __Block_byref_object_dispose_.19773
+ __Block_byref_object_dispose_.20864
+ __Block_byref_object_dispose_.21629
+ __Block_byref_object_dispose_.23424
+ __Block_byref_object_dispose_.23507
+ __Block_byref_object_dispose_.2361
+ __Block_byref_object_dispose_.23614
+ __Block_byref_object_dispose_.23895
+ __Block_byref_object_dispose_.24261
+ __Block_byref_object_dispose_.2459
+ __Block_byref_object_dispose_.25693
+ __Block_byref_object_dispose_.26532
+ __Block_byref_object_dispose_.283
+ __Block_byref_object_dispose_.296
+ __Block_byref_object_dispose_.299
+ __Block_byref_object_dispose_.362
+ __Block_byref_object_dispose_.3758
+ __Block_byref_object_dispose_.389
+ __Block_byref_object_dispose_.408
+ __Block_byref_object_dispose_.4637
+ __Block_byref_object_dispose_.474
+ __Block_byref_object_dispose_.4830
+ __Block_byref_object_dispose_.5951
+ __Block_byref_object_dispose_.598
+ __Block_byref_object_dispose_.605
+ __Block_byref_object_dispose_.612
+ __Block_byref_object_dispose_.616
+ __Block_byref_object_dispose_.7167
+ __Block_byref_object_dispose_.7257
+ __Block_byref_object_dispose_.7845
+ __Block_byref_object_dispose_.8435
+ __Block_byref_object_dispose_.8916
+ __Block_byref_object_dispose_.9025
+ __Block_byref_object_dispose_.9109
+ __Block_byref_object_dispose_.9981
+ __ML3LogCategorySortMap
+ __ML3MigrationFunction2100050to2100060_block_invoke.3276
+ __ML3MigrationFunction2200070to2220000_block_invoke.3512
+ __ML3MigrationFunction2240000to2240010_block_invoke.3551
+ __ML3MigrationFunction2240000to2240010_block_invoke.3573
+ __OBJC_$_CLASS_METHODS_ML3MusicLibrary(ML3ArtistAdditions|ML3AlbumAdditions|Validation|SortMap|ML3GenreAdditions|ML3ComposerAdditions|ML3AlbumArtistAdditions|ProcessingAdditions|CacheManagement|Artwork|Schema|UbiquitousDatabase|ML3Resources|RemoveSourceOrTracks|Saga|MLProtocol|MLUnitTestingAdditions|Maintenance|Jalisco)
+ __OBJC_$_INSTANCE_METHODS_ML3AsyncDatabaseOperation
+ __OBJC_$_INSTANCE_METHODS_ML3MusicLibrary(ML3ArtistAdditions|ML3AlbumAdditions|Validation|SortMap|ML3GenreAdditions|ML3ComposerAdditions|ML3AlbumArtistAdditions|ProcessingAdditions|CacheManagement|Artwork|Schema|UbiquitousDatabase|ML3Resources|RemoveSourceOrTracks|Saga|MLProtocol|MLUnitTestingAdditions|Maintenance|Jalisco)
+ __OBJC_$_INSTANCE_METHODS_ML3SpotlightBatchDonationObject
+ __OBJC_$_INSTANCE_VARIABLES_ML3AsyncDatabaseOperation
+ __OBJC_$_INSTANCE_VARIABLES_ML3SpotlightBatchDonationObject
+ __OBJC_CLASS_RO_$_ML3AsyncDatabaseOperation
+ __OBJC_CLASS_RO_$_ML3SpotlightBatchDonationObject
+ __OBJC_METACLASS_RO_$_ML3AsyncDatabaseOperation
+ __OBJC_METACLASS_RO_$_ML3SpotlightBatchDonationObject
+ __ZN16ML3ImportSession24_flushBookletImportItemsERNSt3__16vectorINS0_10shared_ptrI13ML3ImportItemEENS0_9allocatorIS4_EEEE
+ __ZN16ML3ImportSession26_removeBookletsFromLibraryERNSt3__16vectorIxNS0_9allocatorIxEEEE
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPKNS_10shared_ptrI27ML3DatabaseImportDataSourceEES8_PS6_EENS_4pairIT_T1_EESB_T0_SC_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_10shared_ptrI13ML3ImportItemEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__114default_deleteIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS_10shared_ptrI13ML3ImportItemEEE26_ContainerItemReactionInfoEclB8ne190102EPS5_
+ __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNKSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIx14ML3ArtworkTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIxxEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP11_constraintNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP17_constraint_stateNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt11range_errorC1B8ne190102EPKc
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110shared_ptrI10ML3CPPDataEC2B8ne190102IS1_Li0EEEPT_
+ __ZNSt3__110shared_ptrI12ML3AlbumDataED1B8ne190102Ev
+ __ZNSt3__110shared_ptrI12ML3GenreDataED1B8ne190102Ev
+ __ZNSt3__110shared_ptrI13ML3ArtistDataED1B8ne190102Ev
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I25ML3SubscriptionImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I26ML3ContainerItemImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I27ML3ProtoSyncAlbumImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I27ML3ProtoSyncTrackImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ContainerAuthorImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ITunesSyncAlbumImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ITunesSyncTrackImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ProtoSyncArtistImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I28ML3ProtoSyncDeleteImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I29ML3ITunesSyncArtistImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I31ML3ProtoSyncContainerImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I32ML3ITunesSyncContainerImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne190102I34ML3ContainerItemReactionImportItemLi0EEEPT_
+ __ZNSt3__110shared_ptrI15ML3ComposerDataED1B8ne190102Ev
+ __ZNSt3__110shared_ptrI27ML3DatabaseImportDataSourceEC2B8ne190102I36ML3ItemStoreDatabaseImportDataSourceLi0EEEPT_
+ __ZNSt3__110shared_ptrIN6ML3CPP7ElementEE18__enable_weak_thisB8ne190102IS2_S2_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIx20ML3CollectionInfoSetEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEE5resetB8ne190102EPS6_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEENS_22__tree_node_destructorINS6_ISH_EEEEED1B8ne190102Ev
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20ML3CollectionInfoSetEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__115allocate_sharedB8ne190102I12ML3AlbumDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_RiSB_SB_SB_R12ML3NameOrderSB_S4_S4_SA_SB_RbS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_S9_S9_S4_R12ML3NameOrderSC_S4_SA_RbRiS4_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_SA_SA_S4_R12ML3NameOrderSC_S4_S9_RbiiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I18ML3AlbumImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI12ML3AlbumDataEERNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERbRU8__strongP6NSDataxRxSJ_SE_ELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I19ML3ArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataxELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I29ML3SetCloudIDArtistImportItemNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSP_E_JONS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSO_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlSR_E_JRKNS0_6__baseILSL_1EJxfbSD_SG_EEEEEEDcSQ_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne190102Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEEEEE7destroyB8ne190102INS_4pairIKS8_SE_EEvLi0EEEvRSI_PT_
+ __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED0B8ne190102Ev
+ __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED1B8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrIN6ML3CPP7ElementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_10shared_ptrIN6ML3CPP6Parser15ParserContainerEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIwEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__119__throw_range_errorB8ne190102EPKc
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
+ __ZNSt3__120__optional_copy_baseINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELb0EEC2B8ne190102ERKSC_
+ __ZNSt3__120__throw_bad_weak_ptrB8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj14ML3ImportValueINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEPvEEEEEclB8ne190102EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3AlbumDataEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3GenreDataEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ArtistDataEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI15ML3ComposerDataEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_6vectorINS_4pairIxxEENS1_IS6_EEEEEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne190102EPS9_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne190102Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPSE_EEED2B8ne190102Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI27ML3DatabaseImportDataSourceEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPKSD_SG_PSD_EET2_RT_T0_T1_SI_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEC1B8ne190102ERKSJ_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEaSB8ne190102ERKSJ_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExNS_4lessIS6_EENS4_INS_4pairIKS6_xEEEEED1B8ne190102Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCache9__advanceB8ne190102Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCacheD1B8ne190102Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne190102Ev
+ __ZNSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPKS3_S9_EEvT_T0_l
+ __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne190102IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_13unordered_mapIxyNS_4hashIxEENS_8equal_toIxEENS_9allocatorINS_4pairIKxyEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_13unordered_mapIyxNS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyxEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__init_with_sizeB8ne190102IPSD_SH_EEvT_T0_m
+ __ZNSt3__16vectorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEENS6_ISD_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
+ __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B8ne190102Em
+ __ZNSt3__18optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEaSB8ne190102IS7_vEERSC_OT_
+ __ZNSt3__19allocatorI18DAAPParserDelegateE9constructB8ne190102IS1_JRU8__strongKP22ML3DAAPImportOperationRNS_10shared_ptrIN6ML3CPP6ParserEEER32ML3DAAPImportOperationEntityTypebEEEvPT_DpOT0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZL31ML3TrackSourceStringDescriptioniE24__trackSourceDescription
+ __ZZL31ML3TrackSourceStringDescriptioniE9onceToken
+ ___101-[ML3MusicLibrary _insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:]_block_invoke
+ ___109-[ML3MusicLibrary enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:usingBlock:]_block_invoke
+ ___109-[ML3MusicLibrary enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:usingBlock:]_block_invoke_2
+ ___110-[ML3MusicLibrary importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:variantType:]_block_invoke
+ ___118-[ML3MusicLibrary importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:]_block_invoke
+ ___133-[ML3MusicLibrary retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:completionHandler:]_block_invoke
+ ___133-[ML3MusicLibrary retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:completionHandler:]_block_invoke_2
+ ___141-[ML3MusicLibrary _updateBestArtworkTokensForArtworkToken:artworkType:sourceType:variantType:preserveExistingAvailableToken:usingConnection:]_block_invoke
+ ___141-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke
+ ___143-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:]_block_invoke
+ ___152-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]_block_invoke
+ ___154-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:]_block_invoke
+ ___173-[ML3MusicLibrary _determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:variantType:usingConnection:]_block_invoke
+ ___58-[ML3MusicLibrary isArtworkTokenAvailable:forVariantType:]_block_invoke
+ ___58-[ML3MusicLibrary isArtworkTokenAvailable:forVariantType:]_block_invoke_2
+ ___66-[MLMediaLibraryService performMaintenanceTasksForDatabaseAtPath:]_block_invoke
+ ___69-[ML3MusicLibrary(Maintenance) performMainentanceTasksUsingActivity:]_block_invoke
+ ___70-[ML3MediaLibraryWriter cancelDatabaseOperationsForClient:completion:]_block_invoke
+ ___85-[ML3ArtworkConfiguration supportedSizesForMediaType:artworkType:artworkVariantType:]_block_invoke
+ ___89-[ML3ArtworkConfiguration _supportedSizeKeysForMediaType:artworkType:artworkVariantType:]_block_invoke
+ ___ML3MigrationFunction2240000to2240010_block_invoke
+ ___ML3MigrationFunction2240000to2240010_block_invoke_2
+ ___ZN16ML3ImportSession13_finishImportEv_block_invoke.214
+ ___ZN16ML3ImportSession13_finishImportEv_block_invoke.221
+ ___ZN16ML3ImportSession13_finishImportEv_block_invoke.228
+ ___ZN16ML3ImportSession13_finishImportEv_block_invoke.237
+ ___ZN16ML3ImportSession13_finishImportEv_block_invoke_2.243
+ ___ZN16ML3ImportSession34_prepareContainerAuthorImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.613
+ ___ZN16ML3ImportSession38_prepareContainerItemPersonImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.603
+ ___ZN16ML3ImportSession42_populateExistingAlbumIdentifiersForSourceEi_block_invoke.58
+ ___ZN16ML3ImportSession43_populateExistingArtistIdentifiersForSourceEi_block_invoke.41
+ ___ZN16ML3ImportSession48_populateExistingAlbumArtistIdentifiersForSourceEi_block_invoke.53
+ ___ZN16ML3ImportSession5flushEb_block_invoke.122
+ ____ZL31ML3TrackSourceStringDescriptioni_block_invoke
+ ___block_descriptor_104_e8_32r40r48r56r64r72r80r88r96r_e40_v32?0"ML3DatabaseRow"8"NSError"16^B24l
+ ___block_descriptor_48_e8_32s40s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24l
+ ___block_descriptor_56_e8_32s40r48r_e22_v24?0"NSNumber"8^B16l
+ ___block_descriptor_60_e8_32s40s_e39_B32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_64_e8_32s40s48r56r_e40_v32?0"ML3DatabaseRow"8"NSError"16^B24l
+ ___block_descriptor_72_e8_32bs_e31_v16?0"ML3DatabaseConnection"8l
+ ___block_descriptor_88_e8_32r40r48r_e31_v16?0"ML3DatabaseConnection"8l
+ ___block_descriptor_88_e8_32s40s48s56r_e31_B16?0"ML3DatabaseConnection"8l
+ ___block_descriptor_88_e8_32s40s_e31_v16?0"ML3DatabaseConnection"8l
+ ___block_descriptor_93_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32r40r48r56r64r72r80r88r96r
+ ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r96r
+ __block_literal_global.10052
+ __block_literal_global.1057
+ __block_literal_global.1070
+ __block_literal_global.10827
+ __block_literal_global.111
+ __block_literal_global.11255
+ __block_literal_global.1211
+ __block_literal_global.12714
+ __block_literal_global.12902
+ __block_literal_global.13661
+ __block_literal_global.1404
+ __block_literal_global.14526
+ __block_literal_global.15336
+ __block_literal_global.15656
+ __block_literal_global.161
+ __block_literal_global.16266
+ __block_literal_global.17349
+ __block_literal_global.18281
+ __block_literal_global.18557
+ __block_literal_global.18724
+ __block_literal_global.18848
+ __block_literal_global.18992
+ __block_literal_global.19532
+ __block_literal_global.20247
+ __block_literal_global.20352
+ __block_literal_global.20702
+ __block_literal_global.21397
+ __block_literal_global.23531
+ __block_literal_global.23666
+ __block_literal_global.2390
+ __block_literal_global.24271
+ __block_literal_global.24595
+ __block_literal_global.3006
+ __block_literal_global.320
+ __block_literal_global.3930
+ __block_literal_global.4093
+ __block_literal_global.422
+ __block_literal_global.4635
+ __block_literal_global.479
+ __block_literal_global.4810
+ __block_literal_global.5423
+ __block_literal_global.5560
+ __block_literal_global.587
+ __block_literal_global.5933
+ __block_literal_global.625
+ __block_literal_global.628
+ __block_literal_global.6411
+ __block_literal_global.706
+ __block_literal_global.7143
+ __block_literal_global.726
+ __block_literal_global.8098
+ __block_literal_global.819
+ __block_literal_global.820
+ __block_literal_global.83.5620
+ __block_literal_global.8425
+ __block_literal_global.853
+ __block_literal_global.8671
+ __block_literal_global.8893
+ __block_literal_global.9012
+ __block_literal_global.9512
+ __block_literal_global.974
+ __block_literal_global.9999
+ __getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.16849
+ __getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.16835
+ __getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.16861
+ __iTunesCloudLibraryCore_block_invoke.16844
+ _objc_msgSend$_autogenerateArtworkForRelativePath:artworkType:mediaType:variantType:completionHandler:
+ _objc_msgSend$_determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:variantType:usingConnection:
+ _objc_msgSend$_execute
+ _objc_msgSend$_insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:
+ _objc_msgSend$_insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:usingConnection:
+ _objc_msgSend$_supportedSizeKeysForMediaType:artworkType:artworkVariantType:
+ _objc_msgSend$_updateBestArtworkTokensForArtworkToken:artworkType:sourceType:variantType:preserveExistingAvailableToken:usingConnection:
+ _objc_msgSend$_verifyLibraryAndAttributesProperties:
+ _objc_msgSend$artworkRelativePathFromToken:variantType:
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:usingBlock:
+ _objc_msgSend$importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:usingConnection:
+ _objc_msgSend$importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:variantType:
+ _objc_msgSend$importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:
+ _objc_msgSend$importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:
+ _objc_msgSend$importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:
+ _objc_msgSend$importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:
+ _objc_msgSend$initWithEntity:artworkType:artworkVariantType:
+ _objc_msgSend$initWithToken:artworkType:variantType:musicLibrary:
+ _objc_msgSend$initWithToken:relativePath:artworkType:variantType:musicLibrary:
+ _objc_msgSend$instanceMethodForSelector:
+ _objc_msgSend$isArtworkTokenAvailable:forVariantType:
+ _objc_msgSend$performMainentanceTasksUsingActivity:
+ _objc_msgSend$performMaintenanceTasksForDatabaseAtPath:
+ _objc_msgSend$retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:completionHandler:
+ _objc_msgSend$sizesToAutogenerateForMediaType:artworkType:artworkVariantType:
+ _objc_msgSend$supportedSizesForMediaType:artworkType:artworkVariantType:
+ _objc_msgSend$updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:preserveExistingAvailableToken:usingConnection:
+ _objc_msgSend$willChangeValueForKey:
+ audit_stringiTunesCloud.16847
+ getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.16848
+ getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.16834
+ getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.16860
+ iTunesCloudLibrary.16836
+ iTunesCloudLibraryCore.frameworkLibrary.16843
+ propertiesForGroupingKey.onceToken.5422
+ propertiesForGroupingKey.onceToken.7142
+ propertiesForGroupingKey.onceToken.8892
+ propertiesForGroupingKey.onceToken.9011
+ propertiesForGroupingKey.propertiesForGroupingKey.5424
+ propertiesForGroupingKey.propertiesForGroupingKey.7144
+ propertiesForGroupingKey.propertiesForGroupingKey.8894
+ propertiesForGroupingKey.propertiesForGroupingKey.9013
- -[ML3ArtworkConfiguration _supportedSizeKeysForMediaType:artworkType:]
- -[ML3MediaLibraryWriter cancelActiveTransationAndDatabaseOperationsForClient:]
- -[ML3MusicLibrary _autogenerateArtworkForRelativePath:artworkType:mediaType:completionHandler:]
- -[ML3MusicLibrary _insertArtworkRowWithArtworkToken:artworkType:sourceType:relativePath:usingConnection:]
- -[ML3MusicLibrary _updateBestArtworkTokensForArtworkToken:artworkType:sourceType:preserveExistingAvailableToken:usingConnection:]
- GCC_except_table1007
- GCC_except_table1011
- GCC_except_table1016
- GCC_except_table1019
- GCC_except_table1026
- GCC_except_table1045
- GCC_except_table1049
- GCC_except_table1053
- GCC_except_table106
- GCC_except_table1064
- GCC_except_table1071
- GCC_except_table1073
- GCC_except_table113
- GCC_except_table115
- GCC_except_table124
- GCC_except_table125
- GCC_except_table128
- GCC_except_table129
- GCC_except_table13
- GCC_except_table132
- GCC_except_table133
- GCC_except_table139
- GCC_except_table140
- GCC_except_table143
- GCC_except_table144
- GCC_except_table1450
- GCC_except_table1457
- GCC_except_table1466
- GCC_except_table1472
- GCC_except_table148
- GCC_except_table149
- GCC_except_table1494
- GCC_except_table1498
- GCC_except_table1506
- GCC_except_table1510
- GCC_except_table153
- GCC_except_table1531
- GCC_except_table1533
- GCC_except_table1535
- GCC_except_table154
- GCC_except_table1545
- GCC_except_table1547
- GCC_except_table1549
- GCC_except_table1551
- GCC_except_table1556
- GCC_except_table1559
- GCC_except_table1571
- GCC_except_table1580
- GCC_except_table1583
- GCC_except_table1595
- GCC_except_table1603
- GCC_except_table1614
- GCC_except_table1630
- GCC_except_table1632
- GCC_except_table1634
- GCC_except_table1650
- GCC_except_table1654
- GCC_except_table1660
- GCC_except_table1663
- GCC_except_table1686
- GCC_except_table1689
- GCC_except_table1691
- GCC_except_table1693
- GCC_except_table1699
- GCC_except_table1701
- GCC_except_table1703
- GCC_except_table1710
- GCC_except_table1714
- GCC_except_table1715
- GCC_except_table1717
- GCC_except_table1724
- GCC_except_table1756
- GCC_except_table1761
- GCC_except_table1769
- GCC_except_table1771
- GCC_except_table1776
- GCC_except_table1785
- GCC_except_table1792
- GCC_except_table1832
- GCC_except_table1839
- GCC_except_table1841
- GCC_except_table1863
- GCC_except_table1871
- GCC_except_table1875
- GCC_except_table1885
- GCC_except_table19
- GCC_except_table1901
- GCC_except_table1910
- GCC_except_table1946
- GCC_except_table1976
- GCC_except_table1982
- GCC_except_table1983
- GCC_except_table1986
- GCC_except_table1987
- GCC_except_table2012
- GCC_except_table2016
- GCC_except_table2017
- GCC_except_table2018
- GCC_except_table2019
- GCC_except_table2020
- GCC_except_table2021
- GCC_except_table2022
- GCC_except_table2023
- GCC_except_table2024
- GCC_except_table2025
- GCC_except_table2034
- GCC_except_table2035
- GCC_except_table2036
- GCC_except_table2042
- GCC_except_table2058
- GCC_except_table2059
- GCC_except_table2060
- GCC_except_table2068
- GCC_except_table2070
- GCC_except_table2073
- GCC_except_table2074
- GCC_except_table2080
- GCC_except_table2081
- GCC_except_table2088
- GCC_except_table2104
- GCC_except_table2105
- GCC_except_table2106
- GCC_except_table2111
- GCC_except_table2120
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2123
- GCC_except_table2124
- GCC_except_table2137
- GCC_except_table2143
- GCC_except_table2144
- GCC_except_table2154
- GCC_except_table2156
- GCC_except_table2158
- GCC_except_table2160
- GCC_except_table2163
- GCC_except_table2167
- GCC_except_table2172
- GCC_except_table2173
- GCC_except_table2182
- GCC_except_table2184
- GCC_except_table2186
- GCC_except_table2188
- GCC_except_table2189
- GCC_except_table2192
- GCC_except_table2193
- GCC_except_table2201
- GCC_except_table2202
- GCC_except_table2203
- GCC_except_table2205
- GCC_except_table2206
- GCC_except_table2207
- GCC_except_table2210
- GCC_except_table2241
- GCC_except_table2245
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2248
- GCC_except_table2250
- GCC_except_table2251
- GCC_except_table2257
- GCC_except_table2258
- GCC_except_table2408
- GCC_except_table2412
- GCC_except_table2471
- GCC_except_table2487
- GCC_except_table2500
- GCC_except_table2505
- GCC_except_table2510
- GCC_except_table2517
- GCC_except_table2520
- GCC_except_table2531
- GCC_except_table2533
- GCC_except_table2539
- GCC_except_table2550
- GCC_except_table2554
- GCC_except_table2567
- GCC_except_table2568
- GCC_except_table2791
- GCC_except_table2839
- GCC_except_table2842
- GCC_except_table2847
- GCC_except_table2870
- GCC_except_table2899
- GCC_except_table2910
- GCC_except_table2916
- GCC_except_table2919
- GCC_except_table2930
- GCC_except_table2932
- GCC_except_table2934
- GCC_except_table2940
- GCC_except_table2973
- GCC_except_table2976
- GCC_except_table2986
- GCC_except_table2988
- GCC_except_table2989
- GCC_except_table3027
- GCC_except_table3034
- GCC_except_table3037
- GCC_except_table3055
- GCC_except_table3056
- GCC_except_table3057
- GCC_except_table3058
- GCC_except_table3065
- GCC_except_table3071
- GCC_except_table3072
- GCC_except_table3073
- GCC_except_table3074
- GCC_except_table3075
- GCC_except_table3076
- GCC_except_table3088
- GCC_except_table3113
- GCC_except_table3124
- GCC_except_table3130
- GCC_except_table3134
- GCC_except_table3137
- GCC_except_table3144
- GCC_except_table3146
- GCC_except_table3158
- GCC_except_table3159
- GCC_except_table3160
- GCC_except_table3162
- GCC_except_table3169
- GCC_except_table3170
- GCC_except_table3180
- GCC_except_table3182
- GCC_except_table3189
- GCC_except_table3231
- GCC_except_table3253
- GCC_except_table3274
- GCC_except_table3275
- GCC_except_table3281
- GCC_except_table3286
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3289
- GCC_except_table3296
- GCC_except_table3298
- GCC_except_table3299
- GCC_except_table3303
- GCC_except_table3304
- GCC_except_table3305
- GCC_except_table3306
- GCC_except_table3309
- GCC_except_table3310
- GCC_except_table3311
- GCC_except_table3316
- GCC_except_table3317
- GCC_except_table3321
- GCC_except_table3323
- GCC_except_table3326
- GCC_except_table3328
- GCC_except_table3346
- GCC_except_table3358
- GCC_except_table3359
- GCC_except_table3360
- GCC_except_table3362
- GCC_except_table3368
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3371
- GCC_except_table3411
- GCC_except_table3445
- GCC_except_table3741
- GCC_except_table3751
- GCC_except_table3753
- GCC_except_table3776
- GCC_except_table3778
- GCC_except_table378
- GCC_except_table3788
- GCC_except_table381
- GCC_except_table387
- GCC_except_table388
- GCC_except_table3947
- GCC_except_table3951
- GCC_except_table3956
- GCC_except_table3959
- GCC_except_table3962
- GCC_except_table3971
- GCC_except_table3974
- GCC_except_table3975
- GCC_except_table3976
- GCC_except_table399
- GCC_except_table3991
- GCC_except_table400
- GCC_except_table4002
- GCC_except_table4023
- GCC_except_table4029
- GCC_except_table4033
- GCC_except_table4037
- GCC_except_table4040
- GCC_except_table4043
- GCC_except_table408
- GCC_except_table409
- GCC_except_table41
- GCC_except_table418
- GCC_except_table419
- GCC_except_table4212
- GCC_except_table4226
- GCC_except_table4229
- GCC_except_table4231
- GCC_except_table4232
- GCC_except_table4234
- GCC_except_table4238
- GCC_except_table4244
- GCC_except_table4249
- GCC_except_table4253
- GCC_except_table4272
- GCC_except_table431
- GCC_except_table441
- GCC_except_table4418
- GCC_except_table4429
- GCC_except_table4436
- GCC_except_table4437
- GCC_except_table4438
- GCC_except_table4444
- GCC_except_table4511
- GCC_except_table4512
- GCC_except_table4513
- GCC_except_table4514
- GCC_except_table4518
- GCC_except_table4526
- GCC_except_table4528
- GCC_except_table4540
- GCC_except_table456
- GCC_except_table4560
- GCC_except_table4561
- GCC_except_table462
- GCC_except_table4666
- GCC_except_table4669
- GCC_except_table4673
- GCC_except_table4676
- GCC_except_table4694
- GCC_except_table4695
- GCC_except_table4696
- GCC_except_table4810
- GCC_except_table4812
- GCC_except_table4816
- GCC_except_table4818
- GCC_except_table4820
- GCC_except_table4821
- GCC_except_table4822
- GCC_except_table4894
- GCC_except_table4897
- GCC_except_table4903
- GCC_except_table4906
- GCC_except_table4907
- GCC_except_table4922
- GCC_except_table4923
- GCC_except_table4931
- GCC_except_table4936
- GCC_except_table4939
- GCC_except_table4940
- GCC_except_table4941
- GCC_except_table4942
- GCC_except_table4943
- GCC_except_table4944
- GCC_except_table4946
- GCC_except_table4950
- GCC_except_table4952
- GCC_except_table4955
- GCC_except_table4957
- GCC_except_table4959
- GCC_except_table496
- GCC_except_table4960
- GCC_except_table4961
- GCC_except_table4963
- GCC_except_table4966
- GCC_except_table497
- GCC_except_table4979
- GCC_except_table4984
- GCC_except_table502
- GCC_except_table5022
- GCC_except_table5026
- GCC_except_table5028
- GCC_except_table5030
- GCC_except_table5032
- GCC_except_table5035
- GCC_except_table5037
- GCC_except_table5040
- GCC_except_table5042
- GCC_except_table5046
- GCC_except_table5048
- GCC_except_table505
- GCC_except_table5055
- GCC_except_table5060
- GCC_except_table5067
- GCC_except_table5083
- GCC_except_table5088
- GCC_except_table5093
- GCC_except_table5102
- GCC_except_table5103
- GCC_except_table5104
- GCC_except_table5106
- GCC_except_table5112
- GCC_except_table5175
- GCC_except_table5178
- GCC_except_table5181
- GCC_except_table5182
- GCC_except_table5184
- GCC_except_table5186
- GCC_except_table5188
- GCC_except_table5189
- GCC_except_table5268
- GCC_except_table5271
- GCC_except_table5272
- GCC_except_table5276
- GCC_except_table5277
- GCC_except_table5279
- GCC_except_table5294
- GCC_except_table5295
- GCC_except_table5297
- GCC_except_table5308
- GCC_except_table5310
- GCC_except_table5312
- GCC_except_table5313
- GCC_except_table5314
- GCC_except_table5315
- GCC_except_table5319
- GCC_except_table5320
- GCC_except_table5334
- GCC_except_table5370
- GCC_except_table5379
- GCC_except_table5386
- GCC_except_table543
- GCC_except_table544
- GCC_except_table5480
- GCC_except_table5486
- GCC_except_table5492
- GCC_except_table5498
- GCC_except_table5504
- GCC_except_table551
- GCC_except_table5517
- GCC_except_table5518
- GCC_except_table552
- GCC_except_table5524
- GCC_except_table5525
- GCC_except_table5531
- GCC_except_table5537
- GCC_except_table5542
- GCC_except_table5543
- GCC_except_table5551
- GCC_except_table5560
- GCC_except_table5566
- GCC_except_table5569
- GCC_except_table559
- GCC_except_table5593
- GCC_except_table5621
- GCC_except_table5629
- GCC_except_table564
- GCC_except_table5642
- GCC_except_table565
- GCC_except_table5650
- GCC_except_table5678
- GCC_except_table568
- GCC_except_table5723
- GCC_except_table5727
- GCC_except_table5734
- GCC_except_table5739
- GCC_except_table5740
- GCC_except_table5746
- GCC_except_table5749
- GCC_except_table5751
- GCC_except_table5752
- GCC_except_table576
- GCC_except_table5762
- GCC_except_table5763
- GCC_except_table5764
- GCC_except_table5765
- GCC_except_table5821
- GCC_except_table5822
- GCC_except_table5823
- GCC_except_table5824
- GCC_except_table5825
- GCC_except_table5826
- GCC_except_table5827
- GCC_except_table5829
- GCC_except_table5831
- GCC_except_table5833
- GCC_except_table5836
- GCC_except_table5838
- GCC_except_table5839
- GCC_except_table585
- GCC_except_table587
- GCC_except_table5880
- GCC_except_table591
- GCC_except_table5925
- GCC_except_table5926
- GCC_except_table5927
- GCC_except_table5953
- GCC_except_table5954
- GCC_except_table5956
- GCC_except_table5957
- GCC_except_table5959
- GCC_except_table5961
- GCC_except_table5962
- GCC_except_table5966
- GCC_except_table5967
- GCC_except_table5968
- GCC_except_table5970
- GCC_except_table5971
- GCC_except_table5972
- GCC_except_table5973
- GCC_except_table5974
- GCC_except_table5978
- GCC_except_table5979
- GCC_except_table5980
- GCC_except_table5981
- GCC_except_table5984
- GCC_except_table5985
- GCC_except_table5986
- GCC_except_table5987
- GCC_except_table5988
- GCC_except_table5990
- GCC_except_table5992
- GCC_except_table5993
- GCC_except_table5994
- GCC_except_table5997
- GCC_except_table5998
- GCC_except_table5999
- GCC_except_table600
- GCC_except_table6000
- GCC_except_table6002
- GCC_except_table6005
- GCC_except_table6008
- GCC_except_table6010
- GCC_except_table6014
- GCC_except_table6015
- GCC_except_table6036
- GCC_except_table6043
- GCC_except_table6044
- GCC_except_table6052
- GCC_except_table6076
- GCC_except_table6079
- GCC_except_table608
- GCC_except_table610
- GCC_except_table6103
- GCC_except_table613
- GCC_except_table6152
- GCC_except_table6154
- GCC_except_table6162
- GCC_except_table6163
- GCC_except_table6164
- GCC_except_table6165
- GCC_except_table6166
- GCC_except_table6167
- GCC_except_table617
- GCC_except_table6175
- GCC_except_table6177
- GCC_except_table6178
- GCC_except_table6179
- GCC_except_table6181
- GCC_except_table6182
- GCC_except_table6184
- GCC_except_table6185
- GCC_except_table6187
- GCC_except_table6188
- GCC_except_table6193
- GCC_except_table6201
- GCC_except_table6203
- GCC_except_table6205
- GCC_except_table6206
- GCC_except_table6207
- GCC_except_table6208
- GCC_except_table6209
- GCC_except_table6211
- GCC_except_table6217
- GCC_except_table6226
- GCC_except_table6227
- GCC_except_table624
- GCC_except_table6241
- GCC_except_table6244
- GCC_except_table6247
- GCC_except_table6248
- GCC_except_table6249
- GCC_except_table6256
- GCC_except_table6262
- GCC_except_table6273
- GCC_except_table6274
- GCC_except_table6276
- GCC_except_table6277
- GCC_except_table6278
- GCC_except_table6279
- GCC_except_table628
- GCC_except_table6280
- GCC_except_table6286
- GCC_except_table6301
- GCC_except_table6303
- GCC_except_table6304
- GCC_except_table6305
- GCC_except_table6308
- GCC_except_table6309
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table633
- GCC_except_table6337
- GCC_except_table6348
- GCC_except_table6356
- GCC_except_table6360
- GCC_except_table6361
- GCC_except_table6362
- GCC_except_table6363
- GCC_except_table6374
- GCC_except_table6377
- GCC_except_table638
- GCC_except_table6381
- GCC_except_table6382
- GCC_except_table6383
- GCC_except_table6392
- GCC_except_table6393
- GCC_except_table6395
- GCC_except_table6396
- GCC_except_table6400
- GCC_except_table6401
- GCC_except_table6402
- GCC_except_table6404
- GCC_except_table6417
- GCC_except_table6419
- GCC_except_table6421
- GCC_except_table6423
- GCC_except_table6438
- GCC_except_table6439
- GCC_except_table6440
- GCC_except_table6444
- GCC_except_table6456
- GCC_except_table6458
- GCC_except_table6460
- GCC_except_table6461
- GCC_except_table647
- GCC_except_table655
- GCC_except_table6575
- GCC_except_table658
- GCC_except_table6580
- GCC_except_table6596
- GCC_except_table6598
- GCC_except_table661
- GCC_except_table6613
- GCC_except_table6614
- GCC_except_table6615
- GCC_except_table6621
- GCC_except_table6626
- GCC_except_table6627
- GCC_except_table6628
- GCC_except_table6664
- GCC_except_table6665
- GCC_except_table667
- GCC_except_table6675
- GCC_except_table6676
- GCC_except_table6677
- GCC_except_table6679
- GCC_except_table6680
- GCC_except_table6686
- GCC_except_table6687
- GCC_except_table6688
- GCC_except_table6689
- GCC_except_table6690
- GCC_except_table6691
- GCC_except_table6697
- GCC_except_table6698
- GCC_except_table6699
- GCC_except_table6710
- GCC_except_table6711
- GCC_except_table6712
- GCC_except_table6713
- GCC_except_table6714
- GCC_except_table6715
- GCC_except_table6716
- GCC_except_table6717
- GCC_except_table6718
- GCC_except_table6719
- GCC_except_table6724
- GCC_except_table6725
- GCC_except_table6731
- GCC_except_table6740
- GCC_except_table6741
- GCC_except_table6764
- GCC_except_table6786
- GCC_except_table6809
- GCC_except_table6818
- GCC_except_table6825
- GCC_except_table6849
- GCC_except_table6872
- GCC_except_table6873
- GCC_except_table6937
- GCC_except_table6965
- GCC_except_table7085
- GCC_except_table7171
- GCC_except_table721
- GCC_except_table7241
- GCC_except_table7247
- GCC_except_table7253
- GCC_except_table7254
- GCC_except_table7255
- GCC_except_table7270
- GCC_except_table7274
- GCC_except_table729
- GCC_except_table7320
- GCC_except_table738
- GCC_except_table740
- GCC_except_table746
- GCC_except_table750
- GCC_except_table755
- GCC_except_table759
- GCC_except_table7633
- GCC_except_table7634
- GCC_except_table7635
- GCC_except_table7641
- GCC_except_table7643
- GCC_except_table7644
- GCC_except_table7647
- GCC_except_table767
- GCC_except_table770
- GCC_except_table780
- GCC_except_table783
- GCC_except_table789
- GCC_except_table795
- GCC_except_table801
- GCC_except_table807
- GCC_except_table81
- GCC_except_table813
- GCC_except_table819
- GCC_except_table854
- GCC_except_table89
- GCC_except_table90
- GCC_except_table919
- GCC_except_table923
- GCC_except_table931
- GCC_except_table95
- GCC_except_table957
- GCC_except_table961
- GCC_except_table968
- GCC_except_table97
- GCC_except_table972
- GCC_except_table99
- MSVFastHexStringFromBytes.hexCharacters.25361
- _MSV_XXH_XXH32_update.25353
- _MSV_XXH_XXH64_digest.25358
- _MSV_XXH_XXH64_update.25354
- __129-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:]_block_invoke.731
- __131-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:]_block_invoke.747
- __136-[ML3MusicLibrary enumeratePersistentIDsAfterRevision:revisionTrackingCode:maximumRevisionType:forMediaTypes:inUsersLibrary:usingBlock:]_block_invoke.665
- __140-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:]_block_invoke.739
- __43-[MLMediaLibraryService _serviceConnection]_block_invoke.316
- __47-[ML3MusicLibrary _tearDownNotificationManager]_block_invoke.1062
- __47-[ML3MusicLibrary removeArtworkAssetWithToken:]_block_invoke.757
- __52-[ML3MusicLibrary removeOrphanedTracksOnlyInCaches:]_block_invoke.830
- __59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.522
- __59-[ML3MusicLibrary savePlaylistsSinceRevision:withGrappaID:]_block_invoke.548
- __59-[ML3ProtoSyncImportOperation _unlinkUnavailableMediaItems]_block_invoke.46
- __62+[ML3Container populateMediaTypesOfStaticContainersInLibrary:]_block_invoke.547
- __63-[ML3MusicLibrary _removeOrphanedArtworkAssetsUsingConnection:]_block_invoke.1034
- __65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.1010
- __65-[ML3MusicLibrary _removeOrphanedArtworkMetadataUsingConnection:]_block_invoke.1021
- __66-[ML3ArtworkConfiguration supportedSizesForMediaType:artworkType:]_block_invoke.32
- __66-[ML3Container setValues:forProperties:async:withCompletionBlock:]_block_invoke.459
- __76-[ML3MusicLibrary sanitizeSortMapContentsUsingConnection:didSortMapEntries:]_block_invoke.970
- __77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.770
- __77-[ML3MusicLibrary migrateExistingArtworkToken:newArtworkToken:newSourceType:]_block_invoke.771
- __79-[MLMediaLibraryService mediaLibraryResourcesServiceListenerEndpointWithError:]_block_invoke.274
- __79-[MLMediaLibraryService mediaLibraryResourcesServiceListenerEndpointWithError:]_block_invoke.293
- __93-[ML3Container setItemReactionText:onEntryAtPosition:forUserIdentifier:previousReactionText:]_block_invoke.625
- __99-[ML3MusicLibrary autogenerateSupportedSizesForAllOriginalArtworkWithConnection:completionHandler:]_block_invoke.700
- __99-[ML3MusicLibrary enumerateArtworkRelativePathsWithConnection:matchingRelativePathContainer:block:]_block_invoke.718
- __Block_byref_object_copy_.10751
- __Block_byref_object_copy_.10860
- __Block_byref_object_copy_.11716
- __Block_byref_object_copy_.11878
- __Block_byref_object_copy_.12697
- __Block_byref_object_copy_.13690
- __Block_byref_object_copy_.1526
- __Block_byref_object_copy_.16136
- __Block_byref_object_copy_.16472
- __Block_byref_object_copy_.16988
- __Block_byref_object_copy_.17820
- __Block_byref_object_copy_.18217
- __Block_byref_object_copy_.18474
- __Block_byref_object_copy_.19347
- __Block_byref_object_copy_.19707
- __Block_byref_object_copy_.20657
- __Block_byref_object_copy_.21398
- __Block_byref_object_copy_.23225
- __Block_byref_object_copy_.23308
- __Block_byref_object_copy_.23415
- __Block_byref_object_copy_.2364
- __Block_byref_object_copy_.23696
- __Block_byref_object_copy_.24063
- __Block_byref_object_copy_.2466
- __Block_byref_object_copy_.25491
- __Block_byref_object_copy_.26316
- __Block_byref_object_copy_.284
- __Block_byref_object_copy_.297
- __Block_byref_object_copy_.302
- __Block_byref_object_copy_.363
- __Block_byref_object_copy_.3751
- __Block_byref_object_copy_.390
- __Block_byref_object_copy_.409
- __Block_byref_object_copy_.4643
- __Block_byref_object_copy_.475
- __Block_byref_object_copy_.4835
- __Block_byref_object_copy_.5878
- __Block_byref_object_copy_.599
- __Block_byref_object_copy_.608
- __Block_byref_object_copy_.613
- __Block_byref_object_copy_.617
- __Block_byref_object_copy_.7106
- __Block_byref_object_copy_.7196
- __Block_byref_object_copy_.7781
- __Block_byref_object_copy_.8376
- __Block_byref_object_copy_.8856
- __Block_byref_object_copy_.8965
- __Block_byref_object_copy_.9050
- __Block_byref_object_copy_.9935
- __Block_byref_object_dispose_.10752
- __Block_byref_object_dispose_.10861
- __Block_byref_object_dispose_.11717
- __Block_byref_object_dispose_.11879
- __Block_byref_object_dispose_.12698
- __Block_byref_object_dispose_.13691
- __Block_byref_object_dispose_.1527
- __Block_byref_object_dispose_.16137
- __Block_byref_object_dispose_.16473
- __Block_byref_object_dispose_.16989
- __Block_byref_object_dispose_.17821
- __Block_byref_object_dispose_.18218
- __Block_byref_object_dispose_.18475
- __Block_byref_object_dispose_.19348
- __Block_byref_object_dispose_.19708
- __Block_byref_object_dispose_.20658
- __Block_byref_object_dispose_.21399
- __Block_byref_object_dispose_.23226
- __Block_byref_object_dispose_.23309
- __Block_byref_object_dispose_.23416
- __Block_byref_object_dispose_.2365
- __Block_byref_object_dispose_.23697
- __Block_byref_object_dispose_.24064
- __Block_byref_object_dispose_.2467
- __Block_byref_object_dispose_.25492
- __Block_byref_object_dispose_.26317
- __Block_byref_object_dispose_.285
- __Block_byref_object_dispose_.298
- __Block_byref_object_dispose_.303
- __Block_byref_object_dispose_.364
- __Block_byref_object_dispose_.3752
- __Block_byref_object_dispose_.391
- __Block_byref_object_dispose_.410
- __Block_byref_object_dispose_.4644
- __Block_byref_object_dispose_.476
- __Block_byref_object_dispose_.4836
- __Block_byref_object_dispose_.5879
- __Block_byref_object_dispose_.600
- __Block_byref_object_dispose_.609
- __Block_byref_object_dispose_.614
- __Block_byref_object_dispose_.618
- __Block_byref_object_dispose_.7107
- __Block_byref_object_dispose_.7197
- __Block_byref_object_dispose_.7782
- __Block_byref_object_dispose_.8377
- __Block_byref_object_dispose_.8857
- __Block_byref_object_dispose_.8966
- __Block_byref_object_dispose_.9051
- __Block_byref_object_dispose_.9936
- __ML3MigrationFunction2200070to2220000_block_invoke.3509
- __OBJC_$_CLASS_METHODS_ML3MusicLibrary(ML3ArtistAdditions|ML3AlbumAdditions|Validation|SortMap|ML3GenreAdditions|ML3ComposerAdditions|ML3AlbumArtistAdditions|ProcessingAdditions|CacheManagement|Artwork|Schema|UbiquitousDatabase|ML3Resources|RemoveSourceOrTracks|Saga|MLProtocol|MLUnitTestingAdditions|Jalisco)
- __OBJC_$_INSTANCE_METHODS_ML3MusicLibrary(ML3ArtistAdditions|ML3AlbumAdditions|Validation|SortMap|ML3GenreAdditions|ML3ComposerAdditions|ML3AlbumArtistAdditions|ProcessingAdditions|CacheManagement|Artwork|Schema|UbiquitousDatabase|ML3Resources|RemoveSourceOrTracks|Saga|MLProtocol|MLUnitTestingAdditions|Jalisco)
- __ZN10ML3CPPDataD2Ev
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPKNS_10shared_ptrI27ML3DatabaseImportDataSourceEES8_PS6_EENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_10shared_ptrI13ML3ImportItemEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne180100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__114default_deleteIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS_10shared_ptrI13ML3ImportItemEEE26_ContainerItemReactionInfoEclB8ne180100EPS5_
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNKSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIx14ML3ArtworkTypeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIxxEENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP11_constraintNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP17_constraint_stateNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt11range_errorC1B8ne180100EPKc
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110shared_ptrI10ML3CPPDataEC2B8ne180100IS1_vEEPT_
- __ZNSt3__110shared_ptrI12ML3AlbumDataED1B8ne180100Ev
- __ZNSt3__110shared_ptrI12ML3GenreDataED1B8ne180100Ev
- __ZNSt3__110shared_ptrI13ML3ArtistDataED1B8ne180100Ev
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I25ML3SubscriptionImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I26ML3ContainerItemImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I27ML3ProtoSyncAlbumImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I27ML3ProtoSyncTrackImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I28ML3ContainerAuthorImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I28ML3ITunesSyncAlbumImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I28ML3ITunesSyncTrackImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I28ML3ProtoSyncArtistImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I28ML3ProtoSyncDeleteImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I29ML3ITunesSyncArtistImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I31ML3ProtoSyncContainerImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I32ML3ITunesSyncContainerImportItemvEEPT_
- __ZNSt3__110shared_ptrI13ML3ImportItemEC2B8ne180100I34ML3ContainerItemReactionImportItemvEEPT_
- __ZNSt3__110shared_ptrI15ML3ComposerDataED1B8ne180100Ev
- __ZNSt3__110shared_ptrI27ML3DatabaseImportDataSourceEC2B8ne180100I36ML3ItemStoreDatabaseImportDataSourcevEEPT_
- __ZNSt3__110shared_ptrIN6ML3CPP7ElementEE18__enable_weak_thisB8ne180100IS2_S2_vEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIx20ML3CollectionInfoSetEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEE5resetB8ne180100EPS6_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEENS_22__tree_node_destructorINS6_ISH_EEEEED1B8ne180100Ev
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3AlbumDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI12ML3GenreDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI13ML3ArtistDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI15ML3ComposerDataEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20ML3CollectionInfoSetEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__115allocate_sharedB8ne180100I12ML3AlbumDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_RiSB_SB_SB_R12ML3NameOrderSB_S4_S4_SA_SB_RbS4_EvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_S9_S9_S4_R12ML3NameOrderSC_S4_SA_RbRiS4_EvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I13ML3ArtistDataNS_9allocatorIS1_EEJRxRNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEESA_SA_SA_S4_R12ML3NameOrderSC_S4_S9_RbiiEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I18ML3AlbumImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI12ML3AlbumDataEERNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERbRU8__strongP6NSDataxRxSJ_SE_EvEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I19ML3ArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxEvEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataRxEvEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I24ML3AlbumArtistImportItemNS_9allocatorIS1_EEJRNS_10shared_ptrI13ML3ArtistDataEERU8__strongP6NSDataxEvEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I29ML3SetCloudIDArtistImportItemNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne180100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne180100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0ELm0EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSO_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEEOSW_EEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0ELm0EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSQ_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEERKSY_EEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne180100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne180100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1ELm1EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSO_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEEOSW_EEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1ELm1EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSQ_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEERKSY_EEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne180100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne180100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2ELm2EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSO_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEEOSW_EEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2ELm2EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSQ_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEERKSY_EEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne180100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne180100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3ELm3EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSO_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEEOSW_EEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3ELm3EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSQ_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEERKSY_EEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR26ML3StatementBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne180100IONS1_9__variant15__value_visitorIR29ML3VirtualTableBindingVisitorEEJRKNS0_6__baseILNS0_6_TraitE1EJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEDcT_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4EEE10__dispatchB8ne180100IOZNS0_6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EE9__destroyB8ne180100EvEUlRT_E_JRNS0_6__baseILSI_1EJxfbSD_SG_EEEEEEDcSK_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4ELm4EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100INS0_18__move_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSO_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEEOSW_EEEDcSO_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm4ELm4EEE10__dispatchB8ne180100IOZNS0_6__ctorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEE19__generic_constructB8ne180100IRKNS0_18__copy_constructorISH_LNS0_6_TraitE1EEEEEvRSI_OT_EUlRSQ_OT0_E_JRNS0_6__baseILSL_1EJxfbSD_SG_EEERKSY_EEEDcSQ_DpT0_
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELNS0_6_TraitE1EED2Ev
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS9_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEEPvEEEEE7destroyB8ne180100INS_4pairIKS8_SE_EEvvEEvRSI_PT_
- __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED0B8ne180100Ev
- __ZNSt3__118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EED1B8ne180100Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10shared_ptrIN6ML3CPP7ElementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPNS_10shared_ptrIN6ML3CPP6Parser15ParserContainerEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIwEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__119__throw_range_errorB8ne180100EPKc
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100Ev
- __ZNSt3__120__optional_copy_baseINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEELb0EEC2B8ne180100ERKSC_
- __ZNSt3__120__throw_bad_weak_ptrB8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIj14ML3ImportValueINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEPvEEEEEclB8ne180100EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3AlbumDataEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI12ML3GenreDataEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ArtistDataEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_10shared_ptrI15ML3ComposerDataEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxNS_6vectorINS_4pairIxxEENS1_IS6_EEEEEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyNS_10shared_ptrI13ML3ImportItemEEEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEExEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__126__throw_bad_variant_accessB8ne180100Ev
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPSE_EEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_10shared_ptrI13ML3ImportItemEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_10shared_ptrI27ML3DatabaseImportDataSourceEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEEEEPKSD_SG_PSD_EET2_RT_T0_T1_SI_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEC1B8ne180100ERKSJ_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS7_I13ML3ImportItemEEE26_ContainerItemReactionInfoEENS_4lessIS6_EENS4_INS_4pairIKS6_SC_EEEEEaSB8ne180100ERKSJ_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExNS_4lessIS6_EENS4_INS_4pairIKS6_xEEEEED1B8ne180100Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCache9__advanceB8ne180100Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIZN16ML3ImportSession40_prepareContainerItemReactionImportItemsENS8_I13ML3ImportItemEEE26_ContainerItemReactionInfoEEEENS_19__map_value_compareIS7_SE_NS_4lessIS7_EELb1EEENS5_ISE_EEE18_DetachedTreeCacheD1B8ne180100Ev
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne180100Ev
- __ZNSt3__16vectorI21ML3VirtualTableColumnNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorINS_10shared_ptrI13ML3ImportItemEENS_9allocatorIS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne180100IPKS3_S9_EEvT_T0_l
- __ZNSt3__16vectorINS_10shared_ptrI27ML3DatabaseImportDataSourceEENS_9allocatorIS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrIN6ML3CPP7ElementEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne180100IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_13unordered_mapIxyNS_4hashIxEENS_8equal_toIxEENS_9allocatorINS_4pairIKxyEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_13unordered_mapIyxNS_4hashIyEENS_8equal_toIyEENS_9allocatorINS_4pairIKyxEEEEEENS6_ISB_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_13unordered_setINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4hashIS7_EENS_8equal_toIS7_EENS5_IS7_EEEENS5_ISD_EEE16__init_with_sizeB8ne180100IPSD_SH_EEvT_T0_m
- __ZNSt3__16vectorINS_8optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEENS6_ISD_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne180100IPxS5_EEvT_T0_m
- __ZNSt3__16vectorIxNS_9allocatorIxEEEC2Em
- __ZNSt3__17variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEaSB8ne180100IxLi0ExLm0ELi0EEERSA_OT_
- __ZNSt3__18optionalINS_7variantIJxfbNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI10ML3CPPDataEEEEEEaSB8ne180100IS7_vEERSC_OT_
- __ZNSt3__19allocatorI18DAAPParserDelegateE9constructB8ne180100IS1_JRU8__strongKP22ML3DAAPImportOperationRNS_10shared_ptrIN6ML3CPP6ParserEEER32ML3DAAPImportOperationEntityTypebEEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___121-[ML3MusicLibrary retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:completionHandler:]_block_invoke
- ___121-[ML3MusicLibrary retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:completionHandler:]_block_invoke_2
- ___129-[ML3MusicLibrary _updateBestArtworkTokensForArtworkToken:artworkType:sourceType:preserveExistingAvailableToken:usingConnection:]_block_invoke
- ___129-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:]_block_invoke
- ___131-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:]_block_invoke
- ___140-[ML3MusicLibrary importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:]_block_invoke
- ___142-[ML3MusicLibrary importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:]_block_invoke
- ___161-[ML3MusicLibrary _determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:usingConnection:]_block_invoke
- ___36-[ML3MaintenanceTasksOperation main]_block_invoke
- ___43-[ML3MusicLibrary isArtworkTokenAvailable:]_block_invoke
- ___43-[ML3MusicLibrary isArtworkTokenAvailable:]_block_invoke_2
- ___66-[ML3ArtworkConfiguration supportedSizesForMediaType:artworkType:]_block_invoke
- ___70-[ML3ArtworkConfiguration _supportedSizeKeysForMediaType:artworkType:]_block_invoke
- ___78-[ML3MediaLibraryWriter cancelActiveTransationAndDatabaseOperationsForClient:]_block_invoke
- ___89-[ML3MusicLibrary _insertArtworkRowWithArtworkToken:artworkType:sourceType:relativePath:]_block_invoke
- ___97-[ML3MusicLibrary enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:usingBlock:]_block_invoke
- ___97-[ML3MusicLibrary enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:usingBlock:]_block_invoke_2
- ___98-[ML3MusicLibrary importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:]_block_invoke
- ___ML3MigrationFunction2100050to2100060_block_invoke_2
- ___ZN16ML3ImportSession13_finishImportEv_block_invoke.216
- ___ZN16ML3ImportSession13_finishImportEv_block_invoke.223
- ___ZN16ML3ImportSession13_finishImportEv_block_invoke.230
- ___ZN16ML3ImportSession13_finishImportEv_block_invoke.241
- ___ZN16ML3ImportSession13_finishImportEv_block_invoke_2.245
- ___ZN16ML3ImportSession34_prepareContainerAuthorImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.615
- ___ZN16ML3ImportSession38_prepareContainerItemPersonImportItemsENSt3__110shared_ptrI13ML3ImportItemEE_block_invoke.605
- ___ZN16ML3ImportSession42_populateExistingAlbumIdentifiersForSourceEi_block_invoke.57
- ___ZN16ML3ImportSession43_populateExistingArtistIdentifiersForSourceEi_block_invoke.37
- ___ZN16ML3ImportSession48_populateExistingAlbumArtistIdentifiersForSourceEi_block_invoke.52
- ___ZN16ML3ImportSession5flushEb_block_invoke.125
- ____ZN16ML3ImportSession42_populateExistingAlbumIdentifiersForSourceEi_block_invoke_2
- ____ZN16ML3ImportSession43_populateExistingArtistIdentifiersForSourceEi_block_invoke_2
- ____ZN16ML3ImportSession48_populateExistingAlbumArtistIdentifiersForSourceEi_block_invoke_2
- ___block_descriptor_44_e8_32s_e39_B32?0"NSString"8"NSDictionary"16^B24l
- ___block_descriptor_48_e31_v16?0"ML3DatabaseConnection"8l
- ___block_descriptor_48_e8_32bs40w_e5_v8?0l
- ___block_descriptor_64_e8_32bs_e31_v16?0"ML3DatabaseConnection"8l
- ___block_descriptor_80_e8_32r40r48r_e31_v16?0"ML3DatabaseConnection"8l
- ___block_descriptor_80_e8_32s40s48s56r_e31_B16?0"ML3DatabaseConnection"8l
- ___block_descriptor_85_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- ___copy_helper_block_e8_32b40w
- __block_literal_global.10007
- __block_literal_global.1045
- __block_literal_global.1058
- __block_literal_global.10773
- __block_literal_global.108.13450
- __block_literal_global.11201
- __block_literal_global.1210
- __block_literal_global.12656
- __block_literal_global.12838
- __block_literal_global.13590
- __block_literal_global.1410
- __block_literal_global.14455
- __block_literal_global.15265
- __block_literal_global.15585
- __block_literal_global.159
- __block_literal_global.16195
- __block_literal_global.17286
- __block_literal_global.18216
- __block_literal_global.18493
- __block_literal_global.18657
- __block_literal_global.18781
- __block_literal_global.18925
- __block_literal_global.19464
- __block_literal_global.20042
- __block_literal_global.20147
- __block_literal_global.20497
- __block_literal_global.21178
- __block_literal_global.23333
- __block_literal_global.23468
- __block_literal_global.2398
- __block_literal_global.24074
- __block_literal_global.24395
- __block_literal_global.3035
- __block_literal_global.321
- __block_literal_global.3941
- __block_literal_global.4104
- __block_literal_global.424
- __block_literal_global.461
- __block_literal_global.4642
- __block_literal_global.4816
- __block_literal_global.5429
- __block_literal_global.5568
- __block_literal_global.5862
- __block_literal_global.589
- __block_literal_global.627
- __block_literal_global.630
- __block_literal_global.6342
- __block_literal_global.7083
- __block_literal_global.728
- __block_literal_global.8040
- __block_literal_global.817
- __block_literal_global.818
- __block_literal_global.83.5628
- __block_literal_global.8368
- __block_literal_global.851
- __block_literal_global.8612
- __block_literal_global.8834
- __block_literal_global.8953
- __block_literal_global.9468
- __block_literal_global.972
- __block_literal_global.9954
- __getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc_block_invoke.16781
- __getICStoreArtworkInfoImageFormatJPEGSymbolLoc_block_invoke.16768
- __getICStorePlatformMetadataKindPlaylistSymbolLoc_block_invoke.16793
- __iTunesCloudLibraryCore_block_invoke.16776
- _objc_msgSend$_autogenerateArtworkForRelativePath:artworkType:mediaType:completionHandler:
- _objc_msgSend$_determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:usingConnection:
- _objc_msgSend$_importDAAPPayloadFromFile:
- _objc_msgSend$_insertArtworkRowWithArtworkToken:artworkType:sourceType:relativePath:usingConnection:
- _objc_msgSend$_processTrackElement:
- _objc_msgSend$_supportedSizeKeysForMediaType:artworkType:
- _objc_msgSend$_updateBestArtworkTokensForArtworkToken:artworkType:sourceType:preserveExistingAvailableToken:usingConnection:
- _objc_msgSend$cancelActiveTransactionForClient:
- _objc_msgSend$enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:usingBlock:
- _objc_msgSend$getObjects:andKeys:count:
- _objc_msgSend$importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:shouldPerformColorAnalysis:completion:
- _objc_msgSend$initWithToken:relativePath:artworkType:musicLibrary:
- _objc_msgSend$retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:completionHandler:
- audit_stringiTunesCloud.16779
- getICStoreArtworkInfoCropStyleSquareCenterCropSymbolLoc.ptr.16780
- getICStoreArtworkInfoImageFormatJPEGSymbolLoc.ptr.16767
- getICStorePlatformMetadataKindPlaylistSymbolLoc.ptr.16792
- iTunesCloudLibrary.16769
- iTunesCloudLibraryCore.frameworkLibrary.16775
- propertiesForGroupingKey.onceToken.5428
- propertiesForGroupingKey.onceToken.7082
- propertiesForGroupingKey.onceToken.8833
- propertiesForGroupingKey.onceToken.8952
- propertiesForGroupingKey.propertiesForGroupingKey.5430
- propertiesForGroupingKey.propertiesForGroupingKey.7084
- propertiesForGroupingKey.propertiesForGroupingKey.8835
- propertiesForGroupingKey.propertiesForGroupingKey.8954
CStrings:
+ "%{public}@ Failed to remove cached asset %{public}@ error %{public}@"
+ "%{public}@ Maintenance operation completed. success = %{BOOL}u"
+ "%{public}@ Skipping maintenance because no file exists at path '%{public}@'"
+ "%{public}@ Starting maintenance operation..."
+ "-%d"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MusicLibrary/MusicLibrary/Sorting/iPhoneSortKey/iPhoneSortKey.c"
+ "@36@0:8I16q20q28"
+ "@48@0:8@16q24q32@40"
+ "@56@0:8@16@24q32q40@48"
+ "@56@0:8q16q24@32@40@48"
+ "ALTER TABLE artwork_new RENAME TO artwork"
+ "ALTER TABLE best_artwork_token_new RENAME TO best_artwork_token"
+ "ALTER TABLE container ADD COLUMN edit_session_id TEXT NOT NULL DEFAULT ''"
+ "B32@0:8@16q24"
+ "B52@0:8@16q24q32I40q44"
+ "B56@0:8@16q24q32q40@48"
+ "B60@0:8@16q24q32q40B48@52"
+ "B64@0:8@16@24q32q40I48q52B60"
+ "B64@0:8@16q24q32q40@48@56"
+ "B68@0:8q16q24q32d40B48q52@60"
+ "BOOL UpdateBestArtworkToken(ML3DatabaseConnection *__strong, int64_t, ML3EntityType, ML3ArtworkType, ML3ArtworkVariantType, NSString *__strong, NSString *__strong, ML3ArtworkSourceType, BOOL)"
+ "CREATE INDEX IF NOT EXISTS ArtworkArtworkTokenAttributes ON artwork (artwork_token ASC, artwork_variant_type ASC)"
+ "CREATE INDEX IF NOT EXISTS ArtworkRelativePath ON artwork (relative_path ASC)"
+ "CREATE INDEX IF NOT EXISTS ArtworkTokenEntityPIDEntityType ON artwork_token (entity_pid ASC, entity_type, artwork_variant_type ASC)"
+ "CREATE INDEX IF NOT EXISTS BestArtworkTokenArtworkVariantType ON best_artwork_token (artwork_variant_type ASC)"
+ "CREATE INDEX IF NOT EXISTS BestArtworkTokenEntityPIDEntityType ON best_artwork_token (entity_pid ASC, entity_type, artwork_variant_type ASC)"
+ "CREATE INDEX IF NOT EXISTS ContainerAuthorPersonPID ON container_author (person_pid ASC)"
+ "CREATE INDEX IF NOT EXISTS ItemStatsLikedStateChangedDate ON item_stats (liked_state_changed_date DESC)"
+ "CREATE TABLE artwork (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, relative_path TEXT NOT NULL DEFAULT '', artwork_type INTEGER NOT NULL DEFAULT 0, interest_data BLOB, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (artwork_token, artwork_source_type, artwork_variant_type))"
+ "CREATE TABLE artwork_new (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, relative_path TEXT NOT NULL DEFAULT '', artwork_type INTEGER NOT NULL DEFAULT 0, interest_data BLOB, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (artwork_token, artwork_source_type, artwork_variant_type))"
+ "CREATE TABLE artwork_token (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, artwork_type INTEGER NOT NULL DEFAULT 0, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (artwork_source_type, artwork_type, entity_pid, entity_type, artwork_variant_type))"
+ "CREATE TABLE artwork_token_new (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, artwork_type INTEGER NOT NULL DEFAULT 0, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (artwork_source_type, artwork_type, entity_pid, entity_type, artwork_variant_type))"
+ "CREATE TABLE best_artwork_token (entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, artwork_type INTEGER NOT NULL DEFAULT 0, available_artwork_token TEXT NOT NULL DEFAULT '', fetchable_artwork_token TEXT NOT NULL DEFAULT '', fetchable_artwork_source_type INTEGER NOT NULL DEFAULT 0, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (entity_pid, entity_type, artwork_type, artwork_variant_type))"
+ "CREATE TABLE best_artwork_token_new (entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, artwork_type INTEGER NOT NULL DEFAULT 0, available_artwork_token TEXT NOT NULL DEFAULT '', fetchable_artwork_token TEXT NOT NULL DEFAULT '', fetchable_artwork_source_type INTEGER NOT NULL DEFAULT 0, artwork_variant_type INTEGER NOT NULL DEFAULT 0, UNIQUE (entity_pid, entity_type, artwork_type, artwork_variant_type))"
+ "CREATE TABLE container (container_pid INTEGER PRIMARY KEY, distinguished_kind INTEGER NOT NULL DEFAULT 0, date_created INTEGER NOT NULL DEFAULT 0, date_modified INTEGER NOT NULL DEFAULT 0, date_played INTEGER NOT NULL DEFAULT 0, name TEXT NOT NULL DEFAULT '', name_order INTEGER NOT NULL DEFAULT 0, is_owner INTEGER NOT NULL DEFAULT 1, is_editable INTEGER NOT NULL DEFAULT 0, parent_pid INTEGER NOT NULL DEFAULT 0, contained_media_type INTEGER NOT NULL DEFAULT 0, workout_template_id INTEGER NOT NULL DEFAULT 0, is_hidden INTEGER NOT NULL DEFAULT 0, is_ignorable_itunes_playlist INTEGER NOT NULL DEFAULT 0, description TEXT, play_count_user INTEGER NOT NULL DEFAULT 0, play_count_recent INTEGER NOT NULL DEFAULT 0, liked_state INTEGER NOT NULL DEFAULT 0, smart_evaluation_order INTEGER NOT NULL DEFAULT 0, smart_is_folder INTEGER NOT NULL DEFAULT 0, smart_is_dynamic INTEGER NOT NULL DEFAULT 0, smart_is_filtered INTEGER NOT NULL DEFAULT 0, smart_is_genius INTEGER NOT NULL DEFAULT 0, smart_enabled_only INTEGER NOT NULL DEFAULT 0, smart_is_limited INTEGER NOT NULL DEFAULT 0, smart_limit_kind INTEGER NOT NULL DEFAULT 0, smart_limit_order INTEGER NOT NULL DEFAULT 0, smart_limit_value INTEGER NOT NULL DEFAULT 0, smart_reverse_limit_order INTEGER NOT NULL DEFAULT 0, smart_criteria BLOB, play_order INTEGER NOT NULL DEFAULT 0, is_reversed INTEGER NOT NULL DEFAULT 0, album_field_order INTEGER NOT NULL DEFAULT 0, repeat_mode INTEGER NOT NULL DEFAULT 0, shuffle_items INTEGER NOT NULL DEFAULT 0, has_been_shuffled INTEGER NOT NULL DEFAULT 0, filepath TEXT NOT NULL DEFAULT '', is_saveable INTEGER NOT NULL DEFAULT 0, is_src_remote INTEGER NOT NULL DEFAULT 0, is_ignored_syncing INTEGER NOT NULL DEFAULT 0, container_type INTEGER NOT NULL DEFAULT 0, is_container_type_active_target INTEGER NOT NULL DEFAULT 0, orig_date_modified INTEGER NOT NULL DEFAULT 0, store_cloud_id INTEGER NOT NULL DEFAULT 0, has_cloud_play_order INTEGER NOT NULL DEFAULT 0, cloud_global_id TEXT NOT NULL DEFAULT '', cloud_share_url TEXT NOT NULL DEFAULT '', cloud_is_public INTEGER NOT NULL DEFAULT 0, cloud_is_visible INTEGER NOT NULL DEFAULT 0, cloud_is_subscribed INTEGER NOT NULL DEFAULT 0, cloud_is_curator_playlist INTEGER NOT NULL DEFAULT 0, cloud_author_store_id INTEGER NOT NULL DEFAULT 0, cloud_author_display_name TEXT NOT NULL DEFAULT '', cloud_author_store_url TEXT NOT NULL DEFAULT '', cloud_min_refresh_interval INTEGER NOT NULL DEFAULT 0, cloud_last_update_time INTEGER NOT NULL DEFAULT 0, cloud_user_count INTEGER NOT NULL DEFAULT 0, cloud_global_play_count INTEGER NOT NULL DEFAULT 0, cloud_global_like_count INTEGER NOT NULL DEFAULT 0, keep_local INTEGER NOT NULL DEFAULT 0, keep_local_status INTEGER NOT NULL DEFAULT 0, keep_local_status_reason INTEGER NOT NULL DEFAULT 0, keep_local_constraints INTEGER NOT NULL DEFAULT 0, external_vendor_identifier TEXT NOT NULL DEFAULT '', external_vendor_display_name TEXT NOT NULL DEFAULT '', external_vendor_container_tag TEXT NOT NULL DEFAULT '', is_external_vendor_playlist INTEGER NOT NULL DEFAULT 0, sync_id INTEGER NOT NULL DEFAULT 0, cloud_is_sharing_disabled INTEGER NOT NULL DEFAULT 0, cloud_version_hash TEXT NOT NULL DEFAULT '', date_played_local INTEGER NOT NULL DEFAULT 0, cloud_author_handle TEXT NOT NULL DEFAULT '', cloud_universal_library_id TEXT NOT NULL DEFAULT '', should_display_index INTEGER NOT NULL DEFAULT 0, date_downloaded INTEGER NOT NULL DEFAULT 0, category_type_mask INTEGER NOT NULL DEFAULT 0, grouping_sort_key TEXT NOT NULL DEFAULT '', traits INTEGER NOT NULL DEFAULT 0, liked_state_changed_date INTEGER NOT NULL DEFAULT 0, is_collaborative INTEGER NOT NULL DEFAULT 0, collaborator_invite_options INTEGER NOT NULL DEFAULT 0, collaborator_permissions INTEGER NOT NULL DEFAULT 0, collaboration_invitation_link TEXT NOT NULL DEFAULT '', cover_artwork_recipe TEXT NOT NULL DEFAULT '', collaboration_invitation_url_expiration_date INTEGER NOT NULL DEFAULT 0 ,collaboration_join_request_pending INTEGER NOT NULL DEFAULT 0 ,collaborator_status INTEGER NOT NULL DEFAULT 0, edit_session_id TEXT NOT NULL DEFAULT '') "
+ "CREATE TABLE library_pins (pin_pid INTEGER PRIMARY KEY, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, default_action INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL DEFAULT 0, saga_id INTEGER NOT NULL DEFAULT 0, cloud_library_id TEXT NOT NULL DEFAULT '', position_uuid TEXT NOT NULL DEFAULT '', UNIQUE (entity_pid, entity_type))"
+ "CREATE TABLE library_pins (pin_pid INTEGER PRIMARY KEY, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL DEFAULT 0, default_action INTEGER NOT NULL DEFAULT 0, saga_id INTEGER NOT NULL DEFAULT 0, cloud_library_id TEXT, position_uuid TEXT, UNIQUE (entity_pid, entity_type))"
+ "Clearing cached collection data cloudIDCacheCount=%lld, album=%zu, albumArtist=%zu"
+ "Clearing cached collection data groupingKeyCacheCount=%lld, artist=%zu, album=%zu, albumArtist=%zu, composer=%zu, genre=%zu"
+ "Clearing cached collection data sourceIDCacheCount=%lld, artist=%zu, album=%zu, albumArtist=%zu, composer=%zu, genre=%zu"
+ "Could not run maintenance task for library at %@. error=%@"
+ "DELETE FROM artwork WHERE artwork_token = ? AND artwork_variant_type = ?"
+ "DELETE FROM artwork WHERE artwork_variant_type = %@ AND artwork_token"
+ "DROP TABLE artwork"
+ "DROP TABLE best_artwork_token"
+ "Deleting %ld artwork assets from orphaned metadata with variantType = %{public}@."
+ "Deleting %ld chapter artwork assets from orphaned metadata."
+ "Failed to create library pins table"
+ "Failed to remove orphaned artwork entries"
+ "Failed to remove orphaned chapter artwork entries"
+ "Found %d possible downloaded tracks to remove"
+ "INSERT INTO artwork_new (artwork_token, artwork_source_type, relative_path, artwork_type, interest_data) SELECT artwork_token, artwork_source_type, relative_path, artwork_type, interest_data FROM artwork"
+ "INSERT INTO artwork_token_new (artwork_token, artwork_source_type, artwork_type, entity_pid, entity_type) SELECT artwork_token, artwork_source_type, artwork_type, entity_pid, entity_type FROM artwork_token"
+ "INSERT INTO best_artwork_token_new (entity_pid, entity_type, artwork_type, available_artwork_token, fetchable_artwork_token, fetchable_artwork_source_type) SELECT entity_pid, entity_type, artwork_type, available_artwork_token, fetchable_artwork_token, fetchable_artwork_source_type FROM best_artwork_token"
+ "INSERT OR REPLACE INTO artwork (artwork_token, artwork_type, artwork_source_type, relative_path, artwork_variant_type) VALUES (?, ?, ?, ?, ?)"
+ "INSERT OR REPLACE INTO artwork_token (artwork_token, artwork_source_type, artwork_type, entity_pid, entity_type, artwork_variant_type) VALUES (?, ?, ?, ?, ?, ?)"
+ "INSERT OR REPLACE INTO artwork_token (artwork_token,artwork_source_type,artwork_type,entity_pid,entity_type,artwork_variant_type)"
+ "INSERT OR REPLACE INTO best_artwork_token (entity_pid, entity_type, artwork_type, available_artwork_token, fetchable_artwork_token, fetchable_artwork_source_type, artwork_variant_type) VALUES (?, ?, ?, ?, ?, ?, ?)"
+ "ML3ArtworkVariantTypeDefault"
+ "ML3ArtworkVariantTypeMotion"
+ "ML3ArtworkVariantTypeMotionPreviewFrame"
+ "ML3ArtworkVariantTypePortrait"
+ "ML3ArtworkVariantTypePortraitMotion"
+ "ML3AsyncDatabaseOperation"
+ "ML3AsyncDatabaseOperation.m"
+ "ML3SpotlightBatchDonationObject"
+ "Maintenance"
+ "Match"
+ "PRAGMA user_version = 2240000;"
+ "PRAGMA user_version = 2240010;"
+ "PRAGMA user_version = 2240020;"
+ "PRAGMA user_version = 2240030;"
+ "PRAGMA user_version = 2240031;"
+ "PRAGMA user_version = 2240032;"
+ "PairedDevice"
+ "PurchaseHistory"
+ "SELECT 1 FROM artwork WHERE artwork_token=? AND artwork_variant_type = ?"
+ "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) JOIN album ON (item.album_pid=album.album_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 AND album.liked_state != 2 LIMIT 1"
+ "SELECT artwork_source_type, artwork_type, interest_data FROM artwork WHERE artwork_token = ? AND artwork_variant_type = ?"
+ "SELECT artwork_token, artwork_source_type FROM artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ? AND artwork_variant_type = ?"
+ "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type, artwork.artwork_variant_type FROM artwork LEFT OUTER JOIN best_artwork_token ON (artwork_token = available_artwork_token) WHERE artwork.artwork_type != ? AND available_artwork_token IS NULL"
+ "SELECT artwork_token, artwork_variant_type FROM artwork WHERE relative_path = ?"
+ "SELECT artwork_token.artwork_token, artwork_token.artwork_source_type, (artwork.relative_path != '') AS has_artwork_on_disk FROM artwork_token LEFT OUTER JOIN artwork USING (artwork_token) WHERE artwork_token.entity_pid = ? AND artwork_token.entity_type = ? AND artwork_token.artwork_type = ? AND artwork_token.artwork_variant_type = ? ORDER BY artwork_token.artwork_source_type ASC"
+ "SELECT available_artwork_token FROM best_artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ? AND artwork_variant_type = ?"
+ "SELECT available_artwork_token, fetchable_artwork_token, fetchable_artwork_source_type FROM best_artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ? AND artwork_variant_type = ?"
+ "SELECT entity_pid, entity_type FROM artwork_token WHERE artwork_token = ? AND artwork_type = ? AND artwork_source_type = ? AND artwork_variant_type = ?"
+ "SELECT entity_pid, entity_type, artwork_type FROM best_artwork_token WHERE available_artwork_token = ? AND artwork_variant_type = ?"
+ "SELECT entity_pid, entity_type, best_artwork_token.artwork_type, available_artwork_token, best_artwork_token.artwork_variant_type FROM best_artwork_token LEFT OUTER JOIN artwork ON (available_artwork_token = artwork_token AND best_artwork_token.artwork_variant_type = artwork.artwork_variant_type) WHERE available_artwork_token != '' AND artwork_token IS NULL"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=? AND base_location_id > 0) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=? AND store_item_id=? AND base_location_id > 0) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=? AND store_item_id=?) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=? AND subscription_store_item_id=? AND base_location_id > 0) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=? AND subscription_store_item_id=?) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) JOIN item_extra USING(item_pid) WHERE (item_pid != ? AND title=? AND album_pid=? AND album_artist_pid=? AND item_artist_pid=? AND media_type=?) LIMIT 1;"
+ "SELECT item_pid FROM item JOIN item_store using(item_pid) WHERE sync_id=0 AND store_saga_id=0 AND purchase_history_id=0 AND (is_ota_purchased OR base_location_id >= 250);"
+ "SELECT title, album_pid, album_artist_pid, item_artist_pid, media_type, store_item_id, subscription_store_item_id, is_ota_purchased, base_location_id FROM item JOIN item_extra USING(item_pid) JOIN item_store USING(item_pid) WHERE item_pid=?"
+ "StorePurchase"
+ "Subclass %@ must implement -%@ defined in %@."
+ "Subscription"
+ "Sync"
+ "SyncLocationRollback: could not set path %@ for item with base_location %llu"
+ "System"
+ "Tq,R,N,V_variantType"
+ "Updating best tokens for entity_pid = %lld entity_type = %d artwork_type = %d artwork_variant_type = %d with invalid available token %{public}@"
+ "We have an active operation of type %d"
+ "Will remove track with pid=%lld as it matched to downloaded track with pid=%lld"
+ "[ML3AsyncDatabaseOperation class]"
+ "[ML3AsyncDatabaseOperation] Async operation %p failed in %.3f seconds"
+ "[ML3AsyncDatabaseOperation] Async operation %p finished successfully in %.3f seconds"
+ "[Maintenance] %{pubic}@ All maintenance completed."
+ "[Maintenance] %{pubic}@ Cleaning up artwork for maintenance activity."
+ "[Maintenance] %{pubic}@ Cleaning up missing foreign keys"
+ "[Maintenance] %{pubic}@ Cleaning up old Cache"
+ "[Maintenance] %{pubic}@ Clearing sanitizeClientBuildVersion as it's invalid"
+ "[Maintenance] %{pubic}@ Failed to set state of maintenance activity to DONE."
+ "[Maintenance] %{pubic}@ Item tables are not in sync - will perform a client initiated reset lastClientInitiatedResetClientBuildVersion=%{public}@, currentDeviceBuildVersion=%{public}@"
+ "[Maintenance] %{pubic}@ Marking Purgeable Artwork"
+ "[Maintenance] %{pubic}@ Rebuilding collections (itemAlbumCount=%lld, totalAlbumCount=%lld, itemAlbumArtistCount=%lld, totalAlbumArtistCount=%lld, itemItemArtistCount=%lld, totalItemArtistCount=%lld)"
+ "[Maintenance] %{pubic}@ Rebuilding sort map (usedSortMapEntryCount=%lld, totalSortMapEntryCount=%lld)"
+ "[Maintenance] %{pubic}@ Reconciling HLS Asset Size"
+ "[Maintenance] %{pubic}@ Removing cached playlists not played since %{public}@"
+ "[Maintenance] %{pubic}@ Removing orphaned assets"
+ "[Maintenance] %{pubic}@ Removing orphaned tracks before %{public}@"
+ "[Maintenance] %{pubic}@ Start maintenance activity to convert existing artwork to ASTC."
+ "[Maintenance] %{pubic}@ Start maintenance activity to prune unused metadata"
+ "[Maintenance] %{public}@ Skipping maintenance because database is not validated, currentDatabaseVersion=%d, latestDatabaseVersion=%d "
+ "_activeSiriIndexOperation"
+ "_activeSpotlightIndexOperation"
+ "_artworkVariantType"
+ "_autogenerateArtworkForRelativePath:artworkType:mediaType:variantType:completionHandler:"
+ "_cancelled"
+ "_currentRevision"
+ "_determineAndUpdateBestArtworkTokensForEntityPersistentID:entityType:artworkType:retrievalTime:preserveExistingAvailableToken:variantType:usingConnection:"
+ "_entityStringsToDelete"
+ "_execute"
+ "_executing"
+ "_finished"
+ "_insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:"
+ "_insertArtworkRowWithArtworkToken:artworkType:sourceType:variantType:relativePath:usingConnection:"
+ "_playlistsPersistentIDsToUpdate"
+ "_supportedSizeKeysForMediaType:artworkType:artworkVariantType:"
+ "_targetRevision"
+ "_trackPersistentIDsToUpdate"
+ "_updateBestArtworkTokensForArtworkToken:artworkType:sourceType:variantType:preserveExistingAvailableToken:usingConnection:"
+ "_variantType"
+ "_verifyLibraryAndAttributesProperties:"
+ "artworkRelativePathFromToken:variantType:"
+ "cancelDatabaseOperationsForClient:completion:"
+ "didChangeValueForKey:"
+ "edit_session_id"
+ "entityStringsToDelete"
+ "enumerateArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:usingBlock:"
+ "importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:"
+ "importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:usingConnection:"
+ "importExistingOriginalArtworkWithArtworkToken:artworkType:sourceType:mediaType:variantType:"
+ "importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:"
+ "importOriginalArtworkFromFileURL:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:"
+ "importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:"
+ "importOriginalArtworkFromImageData:withArtworkToken:artworkType:sourceType:mediaType:variantType:shouldPerformColorAnalysis:completion:"
+ "initWithCurrentRevision:targetRevision:trackPersistentIDsToUpdate:playlistsPersistentIDsToUpdate:entityStringsToDelete:"
+ "initWithEntity:artworkType:artworkVariantType:"
+ "initWithToken:artworkType:variantType:musicLibrary:"
+ "initWithToken:relativePath:artworkType:variantType:musicLibrary:"
+ "instanceMethodForSelector:"
+ "isArtworkTokenAvailable:forVariantType:"
+ "isAsynchronous"
+ "isConcurrent"
+ "isFinished"
+ "performMainentanceTasksUsingActivity:"
+ "performMaintenanceTasksForDatabaseAtPath:"
+ "playlistsPersistentIDsToUpdate"
+ "retrieveBestArtworkTokensForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:completionHandler:"
+ "sizesToAutogenerateForMediaType:artworkType:artworkVariantType:"
+ "starting import session %p. source=%s, itemCount=%d, isReset=%d, clientInitiatedReset=%d"
+ "starting to flush (all=%{BOOL}u, cachedCollectionsOverThreshold=%{BOOL}u)"
+ "supportedArtworkVariantTypes"
+ "supportedSizesForMediaType:artworkType:artworkVariantType:"
+ "targetRevision"
+ "trackPersistentIDsToUpdate"
+ "unknown"
+ "updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:preserveExistingAvailableToken:usingConnection:"
+ "v24@0:8@\"NSString\"16"
+ "v24@?0@\"NSNumber\"8^B16"
+ "v52@0:8@16q24I32q36@?44"
+ "v56@0:8q16q24q32q40@?48"
+ "v64@0:8q16q24@32q40q48q56"
+ "v64@0:8q16q24q32q40d48@?56"
+ "v68@0:8q16q24q32q40d48B56@60"
+ "v72@0:8@16@24q32q40I48q52B60@?64"
+ "v72@0:8q16q24@32q40q48q56@64"
+ "variantType"
+ "willChangeValueForKey:"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MusicLibrary/MusicLibrary/Sorting/iPhoneSortKey/iPhoneSortKey.c"
- "B52@0:8@16q24q32B40@44"
- "B56@0:8@16q24q32@40@48"
- "BOOL UpdateBestArtworkToken(ML3DatabaseConnection *__strong, int64_t, ML3EntityType, ML3ArtworkType, NSString *__strong, NSString *__strong, ML3ArtworkSourceType, BOOL)"
- "CREATE INDEX IF NOT EXISTS ArtworkTokenEntityPIDEntityType ON artwork_token (entity_pid ASC, entity_type ASC)"
- "CREATE INDEX IF NOT EXISTS BestArtworkTokenEntityPIDEntityType ON best_artwork_token (entity_pid ASC, entity_type ASC)"
- "CREATE TABLE artwork (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, relative_path TEXT NOT NULL DEFAULT '', artwork_type INTEGER NOT NULL DEFAULT 0, interest_data BLOB, UNIQUE (artwork_token, artwork_source_type))"
- "CREATE TABLE artwork_token (artwork_token TEXT NOT NULL DEFAULT '', artwork_source_type INTEGER NOT NULL DEFAULT 0, artwork_type INTEGER NOT NULL DEFAULT 0, entity_pid INTEGER NOT NULL DEFAULT 0, entity_type INTEGER NOT NULL DEFAULT 0, UNIQUE (artwork_source_type, artwork_type, entity_pid, entity_type))"
- "CREATE TABLE container (container_pid INTEGER PRIMARY KEY, distinguished_kind INTEGER NOT NULL DEFAULT 0, date_created INTEGER NOT NULL DEFAULT 0, date_modified INTEGER NOT NULL DEFAULT 0, date_played INTEGER NOT NULL DEFAULT 0, name TEXT NOT NULL DEFAULT '', name_order INTEGER NOT NULL DEFAULT 0, is_owner INTEGER NOT NULL DEFAULT 1, is_editable INTEGER NOT NULL DEFAULT 0, parent_pid INTEGER NOT NULL DEFAULT 0, contained_media_type INTEGER NOT NULL DEFAULT 0, workout_template_id INTEGER NOT NULL DEFAULT 0, is_hidden INTEGER NOT NULL DEFAULT 0, is_ignorable_itunes_playlist INTEGER NOT NULL DEFAULT 0, description TEXT, play_count_user INTEGER NOT NULL DEFAULT 0, play_count_recent INTEGER NOT NULL DEFAULT 0, liked_state INTEGER NOT NULL DEFAULT 0, smart_evaluation_order INTEGER NOT NULL DEFAULT 0, smart_is_folder INTEGER NOT NULL DEFAULT 0, smart_is_dynamic INTEGER NOT NULL DEFAULT 0, smart_is_filtered INTEGER NOT NULL DEFAULT 0, smart_is_genius INTEGER NOT NULL DEFAULT 0, smart_enabled_only INTEGER NOT NULL DEFAULT 0, smart_is_limited INTEGER NOT NULL DEFAULT 0, smart_limit_kind INTEGER NOT NULL DEFAULT 0, smart_limit_order INTEGER NOT NULL DEFAULT 0, smart_limit_value INTEGER NOT NULL DEFAULT 0, smart_reverse_limit_order INTEGER NOT NULL DEFAULT 0, smart_criteria BLOB, play_order INTEGER NOT NULL DEFAULT 0, is_reversed INTEGER NOT NULL DEFAULT 0, album_field_order INTEGER NOT NULL DEFAULT 0, repeat_mode INTEGER NOT NULL DEFAULT 0, shuffle_items INTEGER NOT NULL DEFAULT 0, has_been_shuffled INTEGER NOT NULL DEFAULT 0, filepath TEXT NOT NULL DEFAULT '', is_saveable INTEGER NOT NULL DEFAULT 0, is_src_remote INTEGER NOT NULL DEFAULT 0, is_ignored_syncing INTEGER NOT NULL DEFAULT 0, container_type INTEGER NOT NULL DEFAULT 0, is_container_type_active_target INTEGER NOT NULL DEFAULT 0, orig_date_modified INTEGER NOT NULL DEFAULT 0, store_cloud_id INTEGER NOT NULL DEFAULT 0, has_cloud_play_order INTEGER NOT NULL DEFAULT 0, cloud_global_id TEXT NOT NULL DEFAULT '', cloud_share_url TEXT NOT NULL DEFAULT '', cloud_is_public INTEGER NOT NULL DEFAULT 0, cloud_is_visible INTEGER NOT NULL DEFAULT 0, cloud_is_subscribed INTEGER NOT NULL DEFAULT 0, cloud_is_curator_playlist INTEGER NOT NULL DEFAULT 0, cloud_author_store_id INTEGER NOT NULL DEFAULT 0, cloud_author_display_name TEXT NOT NULL DEFAULT '', cloud_author_store_url TEXT NOT NULL DEFAULT '', cloud_min_refresh_interval INTEGER NOT NULL DEFAULT 0, cloud_last_update_time INTEGER NOT NULL DEFAULT 0, cloud_user_count INTEGER NOT NULL DEFAULT 0, cloud_global_play_count INTEGER NOT NULL DEFAULT 0, cloud_global_like_count INTEGER NOT NULL DEFAULT 0, keep_local INTEGER NOT NULL DEFAULT 0, keep_local_status INTEGER NOT NULL DEFAULT 0, keep_local_status_reason INTEGER NOT NULL DEFAULT 0, keep_local_constraints INTEGER NOT NULL DEFAULT 0, external_vendor_identifier TEXT NOT NULL DEFAULT '', external_vendor_display_name TEXT NOT NULL DEFAULT '', external_vendor_container_tag TEXT NOT NULL DEFAULT '', is_external_vendor_playlist INTEGER NOT NULL DEFAULT 0, sync_id INTEGER NOT NULL DEFAULT 0, cloud_is_sharing_disabled INTEGER NOT NULL DEFAULT 0, cloud_version_hash TEXT NOT NULL DEFAULT '', date_played_local INTEGER NOT NULL DEFAULT 0, cloud_author_handle TEXT NOT NULL DEFAULT '', cloud_universal_library_id TEXT NOT NULL DEFAULT '', should_display_index INTEGER NOT NULL DEFAULT 0, date_downloaded INTEGER NOT NULL DEFAULT 0, category_type_mask INTEGER NOT NULL DEFAULT 0, grouping_sort_key TEXT NOT NULL DEFAULT '', traits INTEGER NOT NULL DEFAULT 0, liked_state_changed_date INTEGER NOT NULL DEFAULT 0, is_collaborative INTEGER NOT NULL DEFAULT 0, collaborator_invite_options INTEGER NOT NULL DEFAULT 0, collaborator_permissions INTEGER NOT NULL DEFAULT 0, collaboration_invitation_link TEXT NOT NULL DEFAULT '', cover_artwork_recipe TEXT NOT NULL DEFAULT '', collaboration_invitation_url_expiration_date INTEGER NOT NULL DEFAULT 0 ,collaboration_join_request_pending INTEGER NOT NULL DEFAULT 0 ,collaborator_status INTEGER NOT NULL DEFAULT 0)"
- "Deleting %ld artwork assets from orphaned metadata."
- "Favoriting"
- "INSERT OR REPLACE INTO artwork (artwork_token, artwork_type, artwork_source_type, relative_path) VALUES (?, ?, ?, ?)"
- "INSERT OR REPLACE INTO artwork_token (artwork_token, artwork_source_type, artwork_type, entity_pid, entity_type) VALUES (?, ?, ?, ?, ?)"
- "INSERT OR REPLACE INTO artwork_token (artwork_token,artwork_source_type,artwork_type,entity_pid,entity_type)"
- "SELECT 1 FROM artwork WHERE artwork_token=?"
- "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 LIMIT 1"
- "SELECT album_artist_pid FROM album_artist WHERE album_artist_pid NOT IN (SELECT album_artist_pid FROM item) AND album_artist_pid NOT IN (SELECT album_artist_pid FROM album)"
- "SELECT artwork_source_type, artwork_type, interest_data FROM artwork WHERE artwork_token = ?"
- "SELECT artwork_token FROM artwork WHERE relative_path = ?"
- "SELECT artwork_token, artwork_source_type FROM artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ?"
- "SELECT artwork_token, artwork_source_type, relative_path, artwork.artwork_type FROM artwork LEFT OUTER JOIN best_artwork_token ON artwork_token = available_artwork_token WHERE artwork.artwork_type != ? AND available_artwork_token IS NULL"
- "SELECT artwork_token.artwork_token, artwork_token.artwork_source_type, (artwork.relative_path != '') AS has_artwork_on_disk FROM artwork_token LEFT OUTER JOIN artwork USING (artwork_token) WHERE artwork_token.entity_pid = ? AND artwork_token.entity_type = ? AND artwork_token.artwork_type = ? ORDER BY artwork_token.artwork_source_type ASC"
- "SELECT available_artwork_token FROM best_artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ?"
- "SELECT available_artwork_token, fetchable_artwork_token, fetchable_artwork_source_type FROM best_artwork_token WHERE entity_pid = ? AND entity_type = ? AND artwork_type = ?"
- "SELECT entity_pid, entity_type FROM artwork_token WHERE artwork_token = ? AND artwork_type = ? AND artwork_source_type = ?"
- "SELECT entity_pid, entity_type, artwork_type FROM best_artwork_token WHERE available_artwork_token = ?"
- "SELECT entity_pid, entity_type, best_artwork_token.artwork_type, available_artwork_token FROM best_artwork_token LEFT OUTER JOIN artwork ON available_artwork_token = artwork_token WHERE available_artwork_token != '' AND artwork_token IS NULL"
- "Updating best tokens for entity_pid = %lld entity_type = %d artwork_type = %d with invalid available token %{public}@"
- "[ML3StoreImportOperation] failed to import track data"
- "[MaintenanceTasksOperation] All maintenance completed."
- "[MaintenanceTasksOperation] Cleaning up artwork for maintenance activity."
- "[MaintenanceTasksOperation] Cleaning up missing foreign keys"
- "[MaintenanceTasksOperation] Cleaning up old Cache"
- "[MaintenanceTasksOperation] Clearing sanitizeClientBuildVersion as it's invalid"
- "[MaintenanceTasksOperation] Failed to set state of maintenance activity to DONE."
- "[MaintenanceTasksOperation] Item tables are not in sync - will perform a client initiated reset lastClientInitiatedResetClientBuildVersion=%{public}@, currentDeviceBuildVersion=%{public}@"
- "[MaintenanceTasksOperation] Marking Purgeable Artwork"
- "[MaintenanceTasksOperation] Rebuilding collections (itemAlbumCount=%lld, totalAlbumCount=%lld, itemAlbumArtistCount=%lld, totalAlbumArtistCount=%lld, itemItemArtistCount=%lld, totalItemArtistCount=%lld)"
- "[MaintenanceTasksOperation] Rebuilding sort map (usedSortMapEntryCount=%lld, totalSortMapEntryCount=%lld)"
- "[MaintenanceTasksOperation] Reconciling HLS Asset Size"
- "[MaintenanceTasksOperation] Removing cached playlists not played since %{public}@"
- "[MaintenanceTasksOperation] Removing orphaned assets"
- "[MaintenanceTasksOperation] Removing orphaned tracks before %{public}@"
- "[MaintenanceTasksOperation] Skipping maintenance because no file exists at path '%{public}@'"
- "[MaintenanceTasksOperation] Start maintenance activity to convert existing artwork to ASTC."
- "[MaintenanceTasksOperation] Start maintenance activity to prune unused metadata"
- "_autogenerateArtworkForRelativePath:artworkType:mediaType:completionHandler:"
- "_insertArtworkRowWithArtworkToken:artworkType:sourceType:relativePath:usingConnection:"
- "_supportedSizeKeysForMediaType:artworkType:"
- "_updateBestArtworkTokensForArtworkToken:artworkType:sourceType:preserveExistingAvailableToken:usingConnection:"
- "cancelActiveTransationAndDatabaseOperationsForClient:"
- "getObjects:andKeys:count:"
- "starting import session %p. source=%d, itemCount=%d, isReset=%d, clientInitiatedReset=%d"
- "starting to flush (all=%{BOOL}u)"
- "v44@0:8@16q24I32@?36"

```
