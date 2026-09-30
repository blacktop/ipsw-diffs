## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4025.200.18.0.0
-  __TEXT.__text: 0x294b54
+4025.300.10.0.0
+  __TEXT.__text: 0x297260
   __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_methlist: 0x177ec
+  __TEXT.__objc_methlist: 0x178fc
   __TEXT.__const: 0x1503c
   __TEXT.__dlopen_cstrs: 0x4cf
   __TEXT.__gcc_except_tab: 0x34e4
-  __TEXT.__cstring: 0x17158
-  __TEXT.__oslogstring: 0x2007f
+  __TEXT.__cstring: 0x1719d
+  __TEXT.__oslogstring: 0x2047b
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x6538
+  __TEXT.__unwind_info: 0x6590
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x3aca
-  __TEXT.__objc_methname: 0x35307
-  __TEXT.__objc_methtype: 0x7dde
-  __TEXT.__objc_stubs: 0x1b280
+  __TEXT.__objc_methname: 0x35912
+  __TEXT.__objc_methtype: 0x7e29
+  __TEXT.__objc_stubs: 0x1b400
   __DATA_CONST.__got: 0xf90
-  __DATA_CONST.__const: 0x7260
+  __DATA_CONST.__const: 0x7288
   __DATA_CONST.__objc_classlist: 0xd50
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa068
+  __DATA_CONST.__objc_selrefs: 0xa120
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xb80
   __DATA_CONST.__objc_arraydata: 0x468
   __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__const: 0x10820
-  __AUTH_CONST.__cfstring: 0x18380
-  __AUTH_CONST.__objc_const: 0x2f6a8
+  __AUTH_CONST.__cfstring: 0x183a0
+  __AUTH_CONST.__objc_const: 0x2f708
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CA00F082-64F5-3870-8ECB-6AAEE4F0F7FA
-  Functions: 9737
-  Symbols:   30975
-  CStrings:  17651
+  UUID: 8438E8D1-8B77-3ED2-A032-9F41F4527616
+  Functions: 9775
+  Symbols:   31064
+  CStrings:  17691
 
Symbols:
+ -[ICCloudClient deprioritizeCloudAlbumArtworkForPersistentID:]
+ -[ICCloudClient deprioritizePurchaseHistoryAlbumArtworkForPersistentID:]
+ -[ICCloudClient deprioritizeSubscriptionAlbumArtworkForPersistentID:]
+ -[ICCloudClient importCloudAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]
+ -[ICCloudClient importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]
+ -[ICCloudClient importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]
+ -[ICCloudClient importSubscriptionContainerArtworkForPersistentID:artworkVariantType:completionHandler:]
+ -[ICCloudClient loadArtworkInfoForCloudAlbumPersistentID:completionHandler:]
+ -[ICCloudClient loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:]
+ -[ICCloudClient loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:]
+ -[ICCloudClient reconcileAvailabilityForItemSagaIDs:completion:]
+ -[ICDefaults setThermalLevelOverride:]
+ -[ICDefaults thermalLevelOverride]
+ GCC_except_table1288
+ GCC_except_table1487
+ GCC_except_table1500
+ GCC_except_table1753
+ GCC_except_table1936
+ GCC_except_table1965
+ GCC_except_table1980
+ GCC_except_table2020
+ GCC_except_table2132
+ GCC_except_table2147
+ GCC_except_table2196
+ GCC_except_table2198
+ GCC_except_table2204
+ GCC_except_table2211
+ GCC_except_table2239
+ GCC_except_table2254
+ GCC_except_table2259
+ GCC_except_table2261
+ GCC_except_table2266
+ GCC_except_table2269
+ GCC_except_table2282
+ GCC_except_table2359
+ GCC_except_table2368
+ GCC_except_table2371
+ GCC_except_table2374
+ GCC_except_table2377
+ GCC_except_table2379
+ GCC_except_table2381
+ GCC_except_table2383
+ GCC_except_table2390
+ GCC_except_table2392
+ GCC_except_table2409
+ GCC_except_table2448
+ GCC_except_table2479
+ GCC_except_table2481
+ GCC_except_table2483
+ GCC_except_table2485
+ GCC_except_table2835
+ GCC_except_table2880
+ GCC_except_table3026
+ GCC_except_table3043
+ GCC_except_table3053
+ GCC_except_table3076
+ GCC_except_table3086
+ GCC_except_table3184
+ GCC_except_table3452
+ GCC_except_table3456
+ GCC_except_table3459
+ GCC_except_table3474
+ GCC_except_table3485
+ GCC_except_table3504
+ GCC_except_table3544
+ GCC_except_table3558
+ GCC_except_table3671
+ GCC_except_table3831
+ GCC_except_table3996
+ GCC_except_table4038
+ GCC_except_table4136
+ GCC_except_table4144
+ GCC_except_table4148
+ GCC_except_table4150
+ GCC_except_table4152
+ GCC_except_table4156
+ GCC_except_table4163
+ GCC_except_table4167
+ GCC_except_table4182
+ GCC_except_table4185
+ GCC_except_table4364
+ GCC_except_table4416
+ GCC_except_table4420
+ GCC_except_table4423
+ GCC_except_table4428
+ GCC_except_table4492
+ GCC_except_table4534
+ GCC_except_table4538
+ GCC_except_table4540
+ GCC_except_table4607
+ GCC_except_table4684
+ GCC_except_table4772
+ GCC_except_table4855
+ GCC_except_table4923
+ GCC_except_table5004
+ GCC_except_table5165
+ GCC_except_table5422
+ GCC_except_table5518
+ GCC_except_table5566
+ GCC_except_table5590
+ GCC_except_table5631
+ GCC_except_table5632
+ GCC_except_table5705
+ GCC_except_table5723
+ GCC_except_table5990
+ GCC_except_table5998
+ GCC_except_table6009
+ GCC_except_table6011
+ GCC_except_table6012
+ GCC_except_table6013
+ GCC_except_table6014
+ GCC_except_table6024
+ GCC_except_table6029
+ GCC_except_table6040
+ GCC_except_table6055
+ GCC_except_table6057
+ GCC_except_table6063
+ GCC_except_table6072
+ GCC_except_table6081
+ GCC_except_table6115
+ GCC_except_table6146
+ GCC_except_table6159
+ GCC_except_table6166
+ GCC_except_table6167
+ GCC_except_table6227
+ GCC_except_table6230
+ GCC_except_table6244
+ GCC_except_table6267
+ GCC_except_table6278
+ GCC_except_table6281
+ GCC_except_table6284
+ GCC_except_table6287
+ GCC_except_table6290
+ GCC_except_table6293
+ GCC_except_table6296
+ GCC_except_table6299
+ GCC_except_table6302
+ GCC_except_table6305
+ GCC_except_table6308
+ GCC_except_table6409
+ GCC_except_table6623
+ GCC_except_table6630
+ GCC_except_table6804
+ GCC_except_table6808
+ GCC_except_table6810
+ GCC_except_table6837
+ GCC_except_table6883
+ GCC_except_table7065
+ GCC_except_table7198
+ GCC_except_table7342
+ GCC_except_table7355
+ GCC_except_table7378
+ GCC_except_table7389
+ GCC_except_table7434
+ GCC_except_table7435
+ GCC_except_table7436
+ GCC_except_table7437
+ GCC_except_table7438
+ GCC_except_table7479
+ GCC_except_table7497
+ GCC_except_table7549
+ GCC_except_table7552
+ GCC_except_table7561
+ GCC_except_table7568
+ GCC_except_table7615
+ GCC_except_table7634
+ GCC_except_table7667
+ GCC_except_table7725
+ GCC_except_table7726
+ GCC_except_table7739
+ GCC_except_table8157
+ GCC_except_table8161
+ GCC_except_table8165
+ GCC_except_table8187
+ GCC_except_table8193
+ GCC_except_table8204
+ GCC_except_table8244
+ GCC_except_table8247
+ GCC_except_table8314
+ GCC_except_table8359
+ GCC_except_table8408
+ GCC_except_table8436
+ GCC_except_table8441
+ GCC_except_table8443
+ GCC_except_table8445
+ GCC_except_table8477
+ GCC_except_table8620
+ GCC_except_table8628
+ GCC_except_table8633
+ GCC_except_table8648
+ GCC_except_table8656
+ GCC_except_table8700
+ GCC_except_table8733
+ GCC_except_table8848
+ GCC_except_table8852
+ GCC_except_table8854
+ GCC_except_table8891
+ GCC_except_table8894
+ GCC_except_table8901
+ GCC_except_table8904
+ GCC_except_table9113
+ GCC_except_table9117
+ GCC_except_table9157
+ GCC_except_table9254
+ GCC_except_table9259
+ _MSVFastHexStringFromBytes.hexCharacters.41996
+ _MusicLibraryLibraryCore.frameworkLibrary.22286
+ _MusicLibraryLibraryCore.frameworkLibrary.31775
+ __MSV_XXH_XXH32_update.11845
+ __MSV_XXH_XXH32_update.17761
+ __MSV_XXH_XXH32_update.17877
+ __MSV_XXH_XXH32_update.20698
+ __MSV_XXH_XXH32_update.31712
+ __MSV_XXH_XXH32_update.41986
+ __MSV_XXH_XXH64_digest.17884
+ __MSV_XXH_XXH64_digest.31718
+ __MSV_XXH_XXH64_update.11846
+ __MSV_XXH_XXH64_update.17762
+ __MSV_XXH_XXH64_update.17878
+ __MSV_XXH_XXH64_update.20699
+ __MSV_XXH_XXH64_update.31713
+ __MSV_XXH_XXH64_update.41987
+ ___100-[ICCloudClient importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke
+ ___100-[ICCloudClient importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke.123
+ ___103-[ICCloudClient importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke
+ ___103-[ICCloudClient importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke.122
+ ___104-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke
+ ___104-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke.118
+ ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.181
+ ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.176
+ ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.186
+ ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.171
+ ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.156
+ ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.157
+ ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.199
+ ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.200
+ ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.151
+ ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.152
+ ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.132
+ ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.133
+ ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.154
+ ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.161
+ ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.162
+ ___62-[ICCloudClient deprioritizeCloudAlbumArtworkForPersistentID:]_block_invoke
+ ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.163
+ ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.164
+ ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.136
+ ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.137
+ ___64-[ICCloudClient reconcileAvailabilityForItemSagaIDs:completion:]_block_invoke
+ ___64-[ICCloudClient reconcileAvailabilityForItemSagaIDs:completion:]_block_invoke.193
+ ___64-[ICCloudClient reconcileAvailabilityForItemSagaIDs:completion:]_block_invoke.194
+ ___64-[ICCloudClient reconcileAvailabilityForItemSagaIDs:completion:]_block_invoke_2
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.198
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.199
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.200
+ ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.159
+ ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.160
+ ___69-[ICCloudClient deprioritizeSubscriptionAlbumArtworkForPersistentID:]_block_invoke
+ ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.134
+ ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.135
+ ___72-[ICCloudClient deprioritizePurchaseHistoryAlbumArtworkForPersistentID:]_block_invoke
+ ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.127
+ ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.128
+ ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.130
+ ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.131
+ ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.189
+ ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.190
+ ___76-[ICCloudClient loadArtworkInfoForCloudAlbumPersistentID:completionHandler:]_block_invoke
+ ___76-[ICCloudClient loadArtworkInfoForCloudAlbumPersistentID:completionHandler:]_block_invoke.144
+ ___76-[ICCloudClient loadArtworkInfoForCloudAlbumPersistentID:completionHandler:]_block_invoke.145
+ ___76-[ICCloudClient loadArtworkInfoForCloudAlbumPersistentID:completionHandler:]_block_invoke_2
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.191
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.192
+ ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.140
+ ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.141
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:]_block_invoke
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:]_block_invoke.149
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:]_block_invoke.150
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:]_block_invoke_2
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.138
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.139
+ ___86-[ICCloudClient loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:]_block_invoke
+ ___86-[ICCloudClient loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:]_block_invoke.147
+ ___86-[ICCloudClient loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:]_block_invoke.148
+ ___86-[ICCloudClient loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:]_block_invoke_2
+ ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.195
+ ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.196
+ ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.142
+ ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.143
+ ___93-[ICCloudClient importCloudAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke
+ ___93-[ICCloudClient importCloudAlbumArtworkForPersistentID:artworkVariantType:completionHandler:]_block_invoke.121
+ ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.205
+ ___Block_byref_object_copy_.10631
+ ___Block_byref_object_copy_.10827
+ ___Block_byref_object_copy_.10955
+ ___Block_byref_object_copy_.1160
+ ___Block_byref_object_copy_.12434
+ ___Block_byref_object_copy_.13811
+ ___Block_byref_object_copy_.14356
+ ___Block_byref_object_copy_.14580
+ ___Block_byref_object_copy_.14845
+ ___Block_byref_object_copy_.15264
+ ___Block_byref_object_copy_.16410
+ ___Block_byref_object_copy_.16915
+ ___Block_byref_object_copy_.17142
+ ___Block_byref_object_copy_.17492
+ ___Block_byref_object_copy_.18975
+ ___Block_byref_object_copy_.19329
+ ___Block_byref_object_copy_.19546
+ ___Block_byref_object_copy_.20532
+ ___Block_byref_object_copy_.21451
+ ___Block_byref_object_copy_.22249
+ ___Block_byref_object_copy_.22855
+ ___Block_byref_object_copy_.22964
+ ___Block_byref_object_copy_.25377
+ ___Block_byref_object_copy_.25827
+ ___Block_byref_object_copy_.2603
+ ___Block_byref_object_copy_.26425
+ ___Block_byref_object_copy_.26786
+ ___Block_byref_object_copy_.27778
+ ___Block_byref_object_copy_.28736
+ ___Block_byref_object_copy_.29759
+ ___Block_byref_object_copy_.30104
+ ___Block_byref_object_copy_.31137
+ ___Block_byref_object_copy_.32061
+ ___Block_byref_object_copy_.32453
+ ___Block_byref_object_copy_.32639
+ ___Block_byref_object_copy_.32800
+ ___Block_byref_object_copy_.33557
+ ___Block_byref_object_copy_.3520
+ ___Block_byref_object_copy_.35699
+ ___Block_byref_object_copy_.3587
+ ___Block_byref_object_copy_.35926
+ ___Block_byref_object_copy_.36060
+ ___Block_byref_object_copy_.36994
+ ___Block_byref_object_copy_.37156
+ ___Block_byref_object_copy_.37846
+ ___Block_byref_object_copy_.38116
+ ___Block_byref_object_copy_.38741
+ ___Block_byref_object_copy_.38922
+ ___Block_byref_object_copy_.39238
+ ___Block_byref_object_copy_.3931
+ ___Block_byref_object_copy_.40085
+ ___Block_byref_object_copy_.40655
+ ___Block_byref_object_copy_.4276
+ ___Block_byref_object_copy_.4448
+ ___Block_byref_object_copy_.4481
+ ___Block_byref_object_copy_.5373
+ ___Block_byref_object_copy_.5529
+ ___Block_byref_object_copy_.5630
+ ___Block_byref_object_copy_.6378
+ ___Block_byref_object_copy_.6815
+ ___Block_byref_object_copy_.6927
+ ___Block_byref_object_copy_.7422
+ ___Block_byref_object_copy_.9691
+ ___Block_byref_object_copy_.9796
+ ___Block_byref_object_dispose_.10632
+ ___Block_byref_object_dispose_.10828
+ ___Block_byref_object_dispose_.10956
+ ___Block_byref_object_dispose_.1161
+ ___Block_byref_object_dispose_.12435
+ ___Block_byref_object_dispose_.13812
+ ___Block_byref_object_dispose_.14357
+ ___Block_byref_object_dispose_.14581
+ ___Block_byref_object_dispose_.14846
+ ___Block_byref_object_dispose_.15265
+ ___Block_byref_object_dispose_.16411
+ ___Block_byref_object_dispose_.16916
+ ___Block_byref_object_dispose_.17143
+ ___Block_byref_object_dispose_.17493
+ ___Block_byref_object_dispose_.18976
+ ___Block_byref_object_dispose_.19330
+ ___Block_byref_object_dispose_.19547
+ ___Block_byref_object_dispose_.20533
+ ___Block_byref_object_dispose_.21452
+ ___Block_byref_object_dispose_.22250
+ ___Block_byref_object_dispose_.22856
+ ___Block_byref_object_dispose_.22965
+ ___Block_byref_object_dispose_.25378
+ ___Block_byref_object_dispose_.25828
+ ___Block_byref_object_dispose_.2604
+ ___Block_byref_object_dispose_.26426
+ ___Block_byref_object_dispose_.26787
+ ___Block_byref_object_dispose_.27779
+ ___Block_byref_object_dispose_.28737
+ ___Block_byref_object_dispose_.29760
+ ___Block_byref_object_dispose_.30105
+ ___Block_byref_object_dispose_.31138
+ ___Block_byref_object_dispose_.32062
+ ___Block_byref_object_dispose_.32454
+ ___Block_byref_object_dispose_.32640
+ ___Block_byref_object_dispose_.32801
+ ___Block_byref_object_dispose_.33558
+ ___Block_byref_object_dispose_.3521
+ ___Block_byref_object_dispose_.35700
+ ___Block_byref_object_dispose_.3588
+ ___Block_byref_object_dispose_.35927
+ ___Block_byref_object_dispose_.36061
+ ___Block_byref_object_dispose_.36995
+ ___Block_byref_object_dispose_.37157
+ ___Block_byref_object_dispose_.37847
+ ___Block_byref_object_dispose_.38117
+ ___Block_byref_object_dispose_.38742
+ ___Block_byref_object_dispose_.38923
+ ___Block_byref_object_dispose_.39239
+ ___Block_byref_object_dispose_.3932
+ ___Block_byref_object_dispose_.40086
+ ___Block_byref_object_dispose_.40656
+ ___Block_byref_object_dispose_.4277
+ ___Block_byref_object_dispose_.4449
+ ___Block_byref_object_dispose_.4482
+ ___Block_byref_object_dispose_.5374
+ ___Block_byref_object_dispose_.5530
+ ___Block_byref_object_dispose_.5631
+ ___Block_byref_object_dispose_.6379
+ ___Block_byref_object_dispose_.6816
+ ___Block_byref_object_dispose_.6928
+ ___Block_byref_object_dispose_.7423
+ ___Block_byref_object_dispose_.9692
+ ___Block_byref_object_dispose_.9797
+ ___MusicLibraryLibraryCore_block_invoke.22287
+ ___MusicLibraryLibraryCore_block_invoke.31776
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8
+ ___block_literal_global.10.26439
+ ___block_literal_global.10190
+ ___block_literal_global.11582
+ ___block_literal_global.11995
+ ___block_literal_global.12.15301
+ ___block_literal_global.12.25164
+ ___block_literal_global.12.26437
+ ___block_literal_global.12571
+ ___block_literal_global.13.39247
+ ___block_literal_global.13212
+ ___block_literal_global.13254
+ ___block_literal_global.13844
+ ___block_literal_global.15034
+ ___block_literal_global.1507
+ ___block_literal_global.15317
+ ___block_literal_global.16838
+ ___block_literal_global.170.29040
+ ___block_literal_global.17546
+ ___block_literal_global.18.26435
+ ___block_literal_global.18.35761
+ ___block_literal_global.180
+ ___block_literal_global.18004
+ ___block_literal_global.183
+ ___block_literal_global.18401
+ ___block_literal_global.185
+ ___block_literal_global.18798
+ ___block_literal_global.188
+ ___block_literal_global.19027
+ ___block_literal_global.19234
+ ___block_literal_global.198
+ ___block_literal_global.20.26433
+ ___block_literal_global.20419
+ ___block_literal_global.214
+ ___block_literal_global.217.4238
+ ___block_literal_global.219
+ ___block_literal_global.22.26430
+ ___block_literal_global.22086
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.22309
+ ___block_literal_global.225
+ ___block_literal_global.22759
+ ___block_literal_global.22868
+ ___block_literal_global.2347
+ ___block_literal_global.2439
+ ___block_literal_global.24411
+ ___block_literal_global.24535
+ ___block_literal_global.25163
+ ___block_literal_global.25364
+ ___block_literal_global.25935
+ ___block_literal_global.26087
+ ___block_literal_global.26301
+ ___block_literal_global.26445
+ ___block_literal_global.2705
+ ___block_literal_global.27813
+ ___block_literal_global.28320
+ ___block_literal_global.28565
+ ___block_literal_global.2901
+ ___block_literal_global.29136
+ ___block_literal_global.29477
+ ___block_literal_global.29775
+ ___block_literal_global.29925
+ ___block_literal_global.3.18011
+ ___block_literal_global.30921
+ ___block_literal_global.31476
+ ___block_literal_global.31536
+ ___block_literal_global.3194
+ ___block_literal_global.31948
+ ___block_literal_global.32532
+ ___block_literal_global.33153
+ ___block_literal_global.33594
+ ___block_literal_global.34828
+ ___block_literal_global.35336
+ ___block_literal_global.35783
+ ___block_literal_global.36937
+ ___block_literal_global.3745
+ ___block_literal_global.37858
+ ___block_literal_global.38219
+ ___block_literal_global.38317
+ ___block_literal_global.38607
+ ___block_literal_global.39066
+ ___block_literal_global.39257
+ ___block_literal_global.3949
+ ___block_literal_global.40186
+ ___block_literal_global.40326
+ ___block_literal_global.40472
+ ___block_literal_global.40660
+ ___block_literal_global.41236
+ ___block_literal_global.41483
+ ___block_literal_global.41821
+ ___block_literal_global.4249
+ ___block_literal_global.4499
+ ___block_literal_global.4562
+ ___block_literal_global.4683
+ ___block_literal_global.47.31576
+ ___block_literal_global.56.13800
+ ___block_literal_global.5793
+ ___block_literal_global.6.26443
+ ___block_literal_global.6258
+ ___block_literal_global.66.22735
+ ___block_literal_global.68.31433
+ ___block_literal_global.6996
+ ___block_literal_global.7092
+ ___block_literal_global.7309
+ ___block_literal_global.7469
+ ___block_literal_global.7702
+ ___block_literal_global.8.2430
+ ___block_literal_global.8.26441
+ ___block_literal_global.82.31603
+ ___block_literal_global.8419
+ ___block_literal_global.8490
+ ___block_literal_global.9398
+ ___getML3MusicLibraryClass_block_invoke.22285
+ __supportedInterfaceForXPCConnection._supportedInterfaceForXPCConnection.25347
+ __supportedInterfaceForXPCConnection.onceToken.25346
+ _audit_stringMusicLibrary.22302
+ _audit_stringMusicLibrary.31779
+ _getML3MusicLibraryClass.22283
+ _getML3MusicLibraryClass.softClass.22284
+ _objc_msgSend$deprioritizeCloudAlbumArtworkForPersistentID:configuration:
+ _objc_msgSend$deprioritizePurchaseHistoryAlbumArtworkForPersistentID:configuration:
+ _objc_msgSend$deprioritizeSubscriptionAlbumArtworkForPersistentID:configuration:
+ _objc_msgSend$importCloudAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:
+ _objc_msgSend$importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:
+ _objc_msgSend$importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:
+ _objc_msgSend$importSubscriptionContainerArtworkForPersistentID:artworkVariantType:completionHandler:
+ _objc_msgSend$importSubscriptionContainerArtworkForPersistentID:artworkVariantType:configuration:completion:
+ _objc_msgSend$loadArtworkInfoForCloudAlbumPersistentID:configuration:completion:
+ _objc_msgSend$loadArtworkInfoForPurchaseHistoryAlbumPersistentID:configuration:completion:
+ _objc_msgSend$loadArtworkInfoForSubscriptionAlbumPersistentID:configuration:completion:
+ _objc_msgSend$reconcileAvailabilityForItemSagaIDs:configuration:completion:
+ _objc_msgSend$thermalLevelOverride
+ _shared.onceToken.38606
+ _sharedCache.sOnceToken.29924
+ _sharedCache.sSharedCache.29926
+ _sharedController.sOnceToken.35782
+ _sharedController.sOnceToken.39256
+ _sharedController.sSharedController.35784
+ _sharedController.sSharedController.39258
+ _sharedManager.sOnceToken.19233
+ _sharedManager.sOnceToken.28319
+ _sharedManager.sOnceToken.2900
+ _sharedManager.sSharedManager.19235
+ _sharedManager.sSharedManager.28321
+ _sharedManager.sSharedManager.2902
+ _sharedMonitor.sOnceToken.18400
+ _sharedMonitor.sOnceToken.40185
+ _sharedMonitor.sSharedMonitor.18402
+ _sharedMonitor.sSharedMonitor.40187
+ _sharedProvider.sOnceToken.40471
+ _sharedProvider.sSharedProvider.40473
- GCC_except_table1283
- GCC_except_table1451
- GCC_except_table1464
- GCC_except_table1717
- GCC_except_table1900
- GCC_except_table1929
- GCC_except_table1944
- GCC_except_table1984
- GCC_except_table2096
- GCC_except_table2111
- GCC_except_table2160
- GCC_except_table2162
- GCC_except_table2168
- GCC_except_table2175
- GCC_except_table2203
- GCC_except_table2218
- GCC_except_table2223
- GCC_except_table2225
- GCC_except_table2230
- GCC_except_table2233
- GCC_except_table2246
- GCC_except_table2323
- GCC_except_table2332
- GCC_except_table2335
- GCC_except_table2338
- GCC_except_table2341
- GCC_except_table2343
- GCC_except_table2345
- GCC_except_table2347
- GCC_except_table2354
- GCC_except_table2356
- GCC_except_table2373
- GCC_except_table2412
- GCC_except_table2443
- GCC_except_table2445
- GCC_except_table2447
- GCC_except_table2449
- GCC_except_table2799
- GCC_except_table2844
- GCC_except_table2990
- GCC_except_table3007
- GCC_except_table3017
- GCC_except_table3040
- GCC_except_table3050
- GCC_except_table3148
- GCC_except_table3416
- GCC_except_table3420
- GCC_except_table3423
- GCC_except_table3438
- GCC_except_table3449
- GCC_except_table3468
- GCC_except_table3508
- GCC_except_table3522
- GCC_except_table3635
- GCC_except_table3795
- GCC_except_table3960
- GCC_except_table4002
- GCC_except_table4100
- GCC_except_table4108
- GCC_except_table4110
- GCC_except_table4112
- GCC_except_table4114
- GCC_except_table4116
- GCC_except_table4120
- GCC_except_table4127
- GCC_except_table4131
- GCC_except_table4149
- GCC_except_table4328
- GCC_except_table4380
- GCC_except_table4384
- GCC_except_table4387
- GCC_except_table4392
- GCC_except_table4456
- GCC_except_table4498
- GCC_except_table4502
- GCC_except_table4504
- GCC_except_table4571
- GCC_except_table4648
- GCC_except_table4736
- GCC_except_table4819
- GCC_except_table4887
- GCC_except_table4968
- GCC_except_table5129
- GCC_except_table5386
- GCC_except_table5482
- GCC_except_table5530
- GCC_except_table5554
- GCC_except_table5595
- GCC_except_table5596
- GCC_except_table5669
- GCC_except_table5687
- GCC_except_table5947
- GCC_except_table5954
- GCC_except_table5962
- GCC_except_table5973
- GCC_except_table5975
- GCC_except_table5976
- GCC_except_table5977
- GCC_except_table5978
- GCC_except_table5988
- GCC_except_table5993
- GCC_except_table6004
- GCC_except_table6021
- GCC_except_table6027
- GCC_except_table6036
- GCC_except_table6045
- GCC_except_table6079
- GCC_except_table6110
- GCC_except_table6123
- GCC_except_table6130
- GCC_except_table6131
- GCC_except_table6191
- GCC_except_table6194
- GCC_except_table6208
- GCC_except_table6231
- GCC_except_table6236
- GCC_except_table6242
- GCC_except_table6245
- GCC_except_table6248
- GCC_except_table6251
- GCC_except_table6254
- GCC_except_table6257
- GCC_except_table6260
- GCC_except_table6263
- GCC_except_table6266
- GCC_except_table6269
- GCC_except_table6373
- GCC_except_table6585
- GCC_except_table6592
- GCC_except_table6766
- GCC_except_table6770
- GCC_except_table6772
- GCC_except_table6799
- GCC_except_table6845
- GCC_except_table7027
- GCC_except_table7160
- GCC_except_table7304
- GCC_except_table7317
- GCC_except_table7340
- GCC_except_table7351
- GCC_except_table7396
- GCC_except_table7397
- GCC_except_table7398
- GCC_except_table7399
- GCC_except_table7400
- GCC_except_table7441
- GCC_except_table7459
- GCC_except_table7511
- GCC_except_table7514
- GCC_except_table7523
- GCC_except_table7530
- GCC_except_table7577
- GCC_except_table7596
- GCC_except_table7629
- GCC_except_table7687
- GCC_except_table7688
- GCC_except_table7701
- GCC_except_table8119
- GCC_except_table8123
- GCC_except_table8127
- GCC_except_table8149
- GCC_except_table8155
- GCC_except_table8166
- GCC_except_table8171
- GCC_except_table8206
- GCC_except_table8276
- GCC_except_table8321
- GCC_except_table8370
- GCC_except_table8398
- GCC_except_table8403
- GCC_except_table8405
- GCC_except_table8407
- GCC_except_table8439
- GCC_except_table8582
- GCC_except_table8590
- GCC_except_table8595
- GCC_except_table8610
- GCC_except_table8618
- GCC_except_table8662
- GCC_except_table8695
- GCC_except_table8810
- GCC_except_table8814
- GCC_except_table8816
- GCC_except_table8853
- GCC_except_table8856
- GCC_except_table8863
- GCC_except_table8866
- GCC_except_table9075
- GCC_except_table9079
- GCC_except_table9119
- GCC_except_table9216
- GCC_except_table9221
- _MSVFastHexStringFromBytes.hexCharacters.41965
- _MusicLibraryLibraryCore.frameworkLibrary.22260
- _MusicLibraryLibraryCore.frameworkLibrary.31760
- __MSV_XXH_XXH32_update.11827
- __MSV_XXH_XXH32_update.17739
- __MSV_XXH_XXH32_update.17856
- __MSV_XXH_XXH32_update.20680
- __MSV_XXH_XXH32_update.31697
- __MSV_XXH_XXH32_update.41955
- __MSV_XXH_XXH64_digest.17863
- __MSV_XXH_XXH64_digest.31703
- __MSV_XXH_XXH64_update.11828
- __MSV_XXH_XXH64_update.17740
- __MSV_XXH_XXH64_update.17857
- __MSV_XXH_XXH64_update.20681
- __MSV_XXH_XXH64_update.31698
- __MSV_XXH_XXH64_update.41956
- ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.171
- ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.166
- ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.176
- ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.161
- ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.146
- ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.147
- ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.187
- ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.188
- ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.141
- ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.142
- ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.129
- ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.130
- ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.144
- ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.151
- ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.152
- ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.153
- ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.154
- ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.133
- ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.134
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.187
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.188
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.189
- ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.149
- ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.150
- ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.131
- ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.132
- ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.124
- ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.125
- ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.127
- ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.128
- ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.179
- ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.180
- ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.181
- ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.182
- ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.137
- ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.138
- ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.135
- ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.136
- ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke
- ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.118
- ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.183
- ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.184
- ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.139
- ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.140
- ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.193
- ___Block_byref_object_copy_.10613
- ___Block_byref_object_copy_.10809
- ___Block_byref_object_copy_.10937
- ___Block_byref_object_copy_.1145
- ___Block_byref_object_copy_.12417
- ___Block_byref_object_copy_.13785
- ___Block_byref_object_copy_.14331
- ___Block_byref_object_copy_.14555
- ___Block_byref_object_copy_.14820
- ___Block_byref_object_copy_.15239
- ___Block_byref_object_copy_.16388
- ___Block_byref_object_copy_.16893
- ___Block_byref_object_copy_.17120
- ___Block_byref_object_copy_.17470
- ___Block_byref_object_copy_.18954
- ___Block_byref_object_copy_.19308
- ___Block_byref_object_copy_.19525
- ___Block_byref_object_copy_.20514
- ___Block_byref_object_copy_.21425
- ___Block_byref_object_copy_.22223
- ___Block_byref_object_copy_.22829
- ___Block_byref_object_copy_.22938
- ___Block_byref_object_copy_.25353
- ___Block_byref_object_copy_.25804
- ___Block_byref_object_copy_.2587
- ___Block_byref_object_copy_.26402
- ___Block_byref_object_copy_.26763
- ___Block_byref_object_copy_.27761
- ___Block_byref_object_copy_.28719
- ___Block_byref_object_copy_.29743
- ___Block_byref_object_copy_.30088
- ___Block_byref_object_copy_.31121
- ___Block_byref_object_copy_.32046
- ___Block_byref_object_copy_.32438
- ___Block_byref_object_copy_.32624
- ___Block_byref_object_copy_.32785
- ___Block_byref_object_copy_.33539
- ___Block_byref_object_copy_.3512
- ___Block_byref_object_copy_.35676
- ___Block_byref_object_copy_.3579
- ___Block_byref_object_copy_.35903
- ___Block_byref_object_copy_.36037
- ___Block_byref_object_copy_.36971
- ___Block_byref_object_copy_.37133
- ___Block_byref_object_copy_.37823
- ___Block_byref_object_copy_.38093
- ___Block_byref_object_copy_.38718
- ___Block_byref_object_copy_.38899
- ___Block_byref_object_copy_.39215
- ___Block_byref_object_copy_.3925
- ___Block_byref_object_copy_.40061
- ___Block_byref_object_copy_.40631
- ___Block_byref_object_copy_.4265
- ___Block_byref_object_copy_.4431
- ___Block_byref_object_copy_.4464
- ___Block_byref_object_copy_.5355
- ___Block_byref_object_copy_.5511
- ___Block_byref_object_copy_.5609
- ___Block_byref_object_copy_.6356
- ___Block_byref_object_copy_.6793
- ___Block_byref_object_copy_.6906
- ___Block_byref_object_copy_.7401
- ___Block_byref_object_copy_.9670
- ___Block_byref_object_copy_.9775
- ___Block_byref_object_dispose_.10614
- ___Block_byref_object_dispose_.10810
- ___Block_byref_object_dispose_.10938
- ___Block_byref_object_dispose_.1146
- ___Block_byref_object_dispose_.12418
- ___Block_byref_object_dispose_.13786
- ___Block_byref_object_dispose_.14332
- ___Block_byref_object_dispose_.14556
- ___Block_byref_object_dispose_.14821
- ___Block_byref_object_dispose_.15240
- ___Block_byref_object_dispose_.16389
- ___Block_byref_object_dispose_.16894
- ___Block_byref_object_dispose_.17121
- ___Block_byref_object_dispose_.17471
- ___Block_byref_object_dispose_.18955
- ___Block_byref_object_dispose_.19309
- ___Block_byref_object_dispose_.19526
- ___Block_byref_object_dispose_.20515
- ___Block_byref_object_dispose_.21426
- ___Block_byref_object_dispose_.22224
- ___Block_byref_object_dispose_.22830
- ___Block_byref_object_dispose_.22939
- ___Block_byref_object_dispose_.25354
- ___Block_byref_object_dispose_.25805
- ___Block_byref_object_dispose_.2588
- ___Block_byref_object_dispose_.26403
- ___Block_byref_object_dispose_.26764
- ___Block_byref_object_dispose_.27762
- ___Block_byref_object_dispose_.28720
- ___Block_byref_object_dispose_.29744
- ___Block_byref_object_dispose_.30089
- ___Block_byref_object_dispose_.31122
- ___Block_byref_object_dispose_.32047
- ___Block_byref_object_dispose_.32439
- ___Block_byref_object_dispose_.32625
- ___Block_byref_object_dispose_.32786
- ___Block_byref_object_dispose_.33540
- ___Block_byref_object_dispose_.3513
- ___Block_byref_object_dispose_.35677
- ___Block_byref_object_dispose_.3580
- ___Block_byref_object_dispose_.35904
- ___Block_byref_object_dispose_.36038
- ___Block_byref_object_dispose_.36972
- ___Block_byref_object_dispose_.37134
- ___Block_byref_object_dispose_.37824
- ___Block_byref_object_dispose_.38094
- ___Block_byref_object_dispose_.38719
- ___Block_byref_object_dispose_.38900
- ___Block_byref_object_dispose_.39216
- ___Block_byref_object_dispose_.3926
- ___Block_byref_object_dispose_.40062
- ___Block_byref_object_dispose_.40632
- ___Block_byref_object_dispose_.4266
- ___Block_byref_object_dispose_.4432
- ___Block_byref_object_dispose_.4465
- ___Block_byref_object_dispose_.5356
- ___Block_byref_object_dispose_.5512
- ___Block_byref_object_dispose_.5610
- ___Block_byref_object_dispose_.6357
- ___Block_byref_object_dispose_.6794
- ___Block_byref_object_dispose_.6907
- ___Block_byref_object_dispose_.7402
- ___Block_byref_object_dispose_.9671
- ___Block_byref_object_dispose_.9776
- ___MusicLibraryLibraryCore_block_invoke.22261
- ___MusicLibraryLibraryCore_block_invoke.31761
- ___block_literal_global.10.26416
- ___block_literal_global.10171
- ___block_literal_global.11564
- ___block_literal_global.11980
- ___block_literal_global.12.15276
- ___block_literal_global.12.25138
- ___block_literal_global.12.26414
- ___block_literal_global.12547
- ___block_literal_global.13.39224
- ___block_literal_global.13190
- ___block_literal_global.13232
- ___block_literal_global.13818
- ___block_literal_global.1491
- ___block_literal_global.15009
- ___block_literal_global.15292
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.163
- ___block_literal_global.165
- ___block_literal_global.16816
- ___block_literal_global.170.29025
- ___block_literal_global.17524
- ___block_literal_global.17983
- ___block_literal_global.18.26412
- ___block_literal_global.18.35738
- ___block_literal_global.18380
- ___block_literal_global.186
- ___block_literal_global.18777
- ___block_literal_global.19006
- ___block_literal_global.19213
- ___block_literal_global.20.26410
- ___block_literal_global.202.25343
- ___block_literal_global.20402
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.209.25320
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.22.26407
- ___block_literal_global.22060
- ___block_literal_global.22283
- ___block_literal_global.22733
- ___block_literal_global.22842
- ___block_literal_global.2331
- ___block_literal_global.2422
- ___block_literal_global.24385
- ___block_literal_global.24509
- ___block_literal_global.25137
- ___block_literal_global.25339
- ___block_literal_global.25912
- ___block_literal_global.26064
- ___block_literal_global.26278
- ___block_literal_global.26422
- ___block_literal_global.2689
- ___block_literal_global.27796
- ___block_literal_global.28303
- ___block_literal_global.28548
- ___block_literal_global.2890
- ___block_literal_global.29121
- ___block_literal_global.29461
- ___block_literal_global.29759
- ___block_literal_global.29909
- ___block_literal_global.3.17990
- ___block_literal_global.30905
- ___block_literal_global.31461
- ___block_literal_global.31521
- ___block_literal_global.3186
- ___block_literal_global.31933
- ___block_literal_global.32517
- ___block_literal_global.33135
- ___block_literal_global.33576
- ___block_literal_global.34805
- ___block_literal_global.35313
- ___block_literal_global.35760
- ___block_literal_global.36914
- ___block_literal_global.3737
- ___block_literal_global.37835
- ___block_literal_global.38196
- ___block_literal_global.38294
- ___block_literal_global.38584
- ___block_literal_global.39043
- ___block_literal_global.39234
- ___block_literal_global.3943
- ___block_literal_global.40162
- ___block_literal_global.40302
- ___block_literal_global.40448
- ___block_literal_global.40636
- ___block_literal_global.41211
- ___block_literal_global.41452
- ___block_literal_global.41790
- ___block_literal_global.4240
- ___block_literal_global.4482
- ___block_literal_global.4545
- ___block_literal_global.4666
- ___block_literal_global.47.31561
- ___block_literal_global.56.13774
- ___block_literal_global.5772
- ___block_literal_global.6.26420
- ___block_literal_global.6237
- ___block_literal_global.66.22709
- ___block_literal_global.68.31417
- ___block_literal_global.6975
- ___block_literal_global.7071
- ___block_literal_global.7288
- ___block_literal_global.7448
- ___block_literal_global.7682
- ___block_literal_global.8.2413
- ___block_literal_global.8.26418
- ___block_literal_global.82.31588
- ___block_literal_global.8398
- ___block_literal_global.8469
- ___block_literal_global.9377
- ___getML3MusicLibraryClass_block_invoke.22259
- __supportedInterfaceForXPCConnection._supportedInterfaceForXPCConnection.25321
- __supportedInterfaceForXPCConnection.onceToken.25319
- _audit_stringMusicLibrary.22276
- _audit_stringMusicLibrary.31764
- _getML3MusicLibraryClass.22257
- _getML3MusicLibraryClass.softClass.22258
- _objc_msgSend$importSubscriptionContainerArtworkForPersistentID:configuration:completion:
- _shared.onceToken.38583
- _sharedCache.sOnceToken.29908
- _sharedCache.sSharedCache.29910
- _sharedController.sOnceToken.35759
- _sharedController.sOnceToken.39233
- _sharedController.sSharedController.35761
- _sharedController.sSharedController.39235
- _sharedManager.sOnceToken.19212
- _sharedManager.sOnceToken.28302
- _sharedManager.sOnceToken.2889
- _sharedManager.sSharedManager.19214
- _sharedManager.sSharedManager.28304
- _sharedManager.sSharedManager.2891
- _sharedMonitor.sOnceToken.18379
- _sharedMonitor.sOnceToken.40161
- _sharedMonitor.sSharedMonitor.18381
- _sharedMonitor.sSharedMonitor.40163
- _sharedProvider.sOnceToken.40447
- _sharedProvider.sSharedProvider.40449
CStrings:
+ "%{public}@ Found thermal level override value %{public}@"
+ "%{public}@ [SKD] - Ignoring fatal error from stop request: '%{public}@'"
+ "Failed to process availability. err = %{public}@"
+ "ICDefaultsKeyThermalLevelOverride"
+ "Processing availability for tracks with saga IDs %{public}@ ..."
+ "Sending request to deprioritize cloud album artwork import with persistent ID %lld..."
+ "Sending request to deprioritize purchase history album artwork import with persistent ID %lld..."
+ "Sending request to deprioritize subscription album artwork import with persistent ID %lld..."
+ "Sending request to import cloud album image for item persistent ID %lld..."
+ "Sending request to import purchase history album image for item persistent ID %lld..."
+ "Sending request to import subscription album image for item persistent ID %lld..."
+ "Sending request to import subscription artwork for container persistent ID %lld with variant %d..."
+ "Sending request to load cloud album artwork info for persistent ID %lld..."
+ "Sending request to load purchase history album artwork info for persistent ID %lld..."
+ "Sending request to load subscription album artwork info for persistent ID %lld..."
+ "deprioritizeCloudAlbumArtworkForPersistentID:"
+ "deprioritizeCloudAlbumArtworkForPersistentID:configuration:"
+ "deprioritizePurchaseHistoryAlbumArtworkForPersistentID:"
+ "deprioritizePurchaseHistoryAlbumArtworkForPersistentID:configuration:"
+ "deprioritizeSubscriptionAlbumArtworkForPersistentID:"
+ "deprioritizeSubscriptionAlbumArtworkForPersistentID:configuration:"
+ "importCloudAlbumArtworkForPersistentID:artworkVariantType:completionHandler:"
+ "importCloudAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:completionHandler:"
+ "importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:completionHandler:"
+ "importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importSubscriptionContainerArtworkForPersistentID:artworkVariantType:completionHandler:"
+ "importSubscriptionContainerArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "loadArtworkInfoForCloudAlbumPersistentID:completionHandler:"
+ "loadArtworkInfoForCloudAlbumPersistentID:configuration:completion:"
+ "loadArtworkInfoForPurchaseHistoryAlbumPersistentID:completionHandler:"
+ "loadArtworkInfoForPurchaseHistoryAlbumPersistentID:configuration:completion:"
+ "loadArtworkInfoForSubscriptionAlbumPersistentID:completionHandler:"
+ "loadArtworkInfoForSubscriptionAlbumPersistentID:configuration:completion:"
+ "reconcileAvailabilityForItemSagaIDs:completion:"
+ "reconcileAvailabilityForItemSagaIDs:configuration:completion:"
+ "setThermalLevelOverride:"
+ "thermalLevelOverride"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v40@0:8q16@\"ICConnectionConfiguration\"24@?<v@?@\"NSError\"@\"NSDictionary\">32"
- "Sending request to import subscription artwork for container persistent ID %lld..."
- "importSubscriptionContainerArtworkForPersistentID:configuration:completion:"

```
