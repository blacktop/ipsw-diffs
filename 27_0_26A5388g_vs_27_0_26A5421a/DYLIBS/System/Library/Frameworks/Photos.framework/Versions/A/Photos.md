## Photos

> `/System/Library/Frameworks/Photos.framework/Versions/A/Photos`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0x2f51f4
-  __TEXT.__objc_methlist: 0x25bfc
+911.0.134.0.0
+  __TEXT.__text: 0x2f773c
+  __TEXT.__objc_methlist: 0x25dc4
   __TEXT.__const: 0x1770
   __TEXT.__dlopen_cstrs: 0x280
   __TEXT.__constg_swiftt: 0x544

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x31daa
+  __TEXT.__cstring: 0x31e7c
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x21415
+  __TEXT.__oslogstring: 0x21567
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x915c
+  __TEXT.__gcc_except_tab: 0x9248
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x9518
+  __TEXT.__unwind_info: 0x9598
   __TEXT.__eh_frame: 0x4a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x31d0
-  __DATA_CONST.__objc_classlist: 0xeb8
-  __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x2d0
+  __DATA_CONST.__objc_classlist: 0xec0
+  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13cf0
+  __DATA_CONST.__objc_selrefs: 0x13db0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc20
-  __DATA_CONST.__objc_arraydata: 0x838
-  __DATA_CONST.__got: 0x27c8
-  __AUTH_CONST.__const: 0xb3f8
-  __AUTH_CONST.__cfstring: 0x2c800
-  __AUTH_CONST.__objc_const: 0x401d8
+  __DATA_CONST.__objc_arraydata: 0x858
+  __DATA_CONST.__got: 0x2800
+  __AUTH_CONST.__const: 0xb488
+  __AUTH_CONST.__cfstring: 0x2c880
+  __AUTH_CONST.__objc_const: 0x40428
   __AUTH_CONST.__objc_intobj: 0x2388
   __AUTH_CONST.__objc_arrayobj: 0x7b0
   __AUTH_CONST.__objc_doubleobj: 0x130
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1688
-  __AUTH.__objc_data: 0x5098
+  __AUTH_CONST.__auth_got: 0x1690
+  __AUTH.__objc_data: 0x50e8
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x345c
-  __DATA.__data: 0x2920
+  __DATA.__objc_ivar: 0x3468
+  __DATA.__data: 0x2980
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x17a8
   __DATA.__common: 0x49

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14673
-  Symbols:   33230
-  CStrings:  8598
+  Functions: 14714
+  Symbols:   33321
+  CStrings:  8609
 
Symbols:
+ +[PHAsset predicateForResourcesForOsMigrationForResourceTypes:assetIDs:includeLocalOnly:iCPLEnabled:includeFullSizeRenders:]
+ +[PHAssetResourceUploadJobOptions ph_optionsWithDictionary:]
+ +[PHFindQueryUtilities leoSortDescriptorsFromSortDescriptors:]
+ +[PHSearchQueryManager _fetchVisibleAssetUUIDsForResults:inLibrary:]
+ +[PHSearchQueryManager _filterResults:withValidAssetUUIDs:]
+ +[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:allowedBundleIdentifiers:maximumSearchResults:allowUnattributedQuery:completion:]
+ +[PHSearchUtility bundleIdentifiersAllowedForSiriSearch]
+ +[PHSearchUtility searchIntentsAttributedStringFromWhoValues:whatValues:whereValues:whenValues:]
+ +[PHSearchUtility searchIntentsDataFromWhoValues:whatValues:whereValues:whenValues:error:]
+ -[PHAssetCreationRequest _entitledClientSkipsUUIDValidation]
+ -[PHAssetExtendedMetadata originalFilename]
+ -[PHAssetResource filename]
+ -[PHAssetResourceUploadJobConfiguration options]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest options]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest ph_optionsDictionary]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest ph_setOptionsDictionary:]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest setOptions:]
+ -[PHAssetResourceUploadJobOptions copyWithZone:]
+ -[PHAssetResourceUploadJobOptions description]
+ -[PHAssetResourceUploadJobOptions hash]
+ -[PHAssetResourceUploadJobOptions isEqual:]
+ -[PHAssetResourceUploadJobOptions ph_dictionaryRepresentation]
+ -[PHAssetResourceUploadJobOptions preventsExpensiveNetworkAccess]
+ -[PHAssetResourceUploadJobOptions setPreventsExpensiveNetworkAccess:]
+ -[PHAsynchronousPhotoLibraryExecutionContext dispatchRetryOnQueue:block:]
+ -[PHCollectionShareChangeRequest addAssetsToCollectionShareByCopyingSourceAssets:creationOptionsMappedToSourceAssets:withBatchCommentText:outCreatedSharePostPlaceholder:skipSharePost:]
+ -[PHPerformChangesTransaction _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]
+ -[PHPerformChangesTransaction _sendSingleChangesRequest:onExecutionContext:withInstrumentation:reply:]
+ -[PHPerformChangesTransaction commitTransactionWithChangesRequest:onExecutionContext:withInstrumentation:retryCount:reply:]
+ -[PHPerformChangesTransaction initWithQueue:priority:clientProvider:]
+ -[PHPhotoLibrary _createUploadJobExtensionConfigurationWithOptions:error:]
+ -[PHPhotoLibrary _deleteUploadJobExtensionConfigurationWithError:]
+ -[PHPhotoLibrary _setUploadJobExtensionEnabled:options:error:]
+ -[PHPhotoLibrary disableUploadJobExtensionWithError:]
+ -[PHPhotoLibrary enableUploadJobExtensionWithOptions:error:]
+ -[PHPhotoLibrary setUploadJobExtensionOptions:error:]
+ -[PHPhotoLibrary uploadJobExtensionOptions]
+ -[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:skipSharePost:]
+ -[PHSynchronousPhotoLibraryExecutionContext dispatchRetryOnQueue:block:]
+ -[PLPhotoLibraryBundle(PHPerformChanges) photoKitClientForAccessLevel:]
+ GCC_except_table10036
+ GCC_except_table10050
+ GCC_except_table10051
+ GCC_except_table10058
+ GCC_except_table10103
+ GCC_except_table10178
+ GCC_except_table10179
+ GCC_except_table10180
+ GCC_except_table10181
+ GCC_except_table10182
+ GCC_except_table10183
+ GCC_except_table10184
+ GCC_except_table10185
+ GCC_except_table10186
+ GCC_except_table10187
+ GCC_except_table10188
+ GCC_except_table10189
+ GCC_except_table10190
+ GCC_except_table10191
+ GCC_except_table10192
+ GCC_except_table10193
+ GCC_except_table10194
+ GCC_except_table10195
+ GCC_except_table10196
+ GCC_except_table10197
+ GCC_except_table10198
+ GCC_except_table10199
+ GCC_except_table10200
+ GCC_except_table10201
+ GCC_except_table10312
+ GCC_except_table10321
+ GCC_except_table10322
+ GCC_except_table10323
+ GCC_except_table10324
+ GCC_except_table10325
+ GCC_except_table10326
+ GCC_except_table10327
+ GCC_except_table10338
+ GCC_except_table10356
+ GCC_except_table10389
+ GCC_except_table10390
+ GCC_except_table10391
+ GCC_except_table10392
+ GCC_except_table10393
+ GCC_except_table10421
+ GCC_except_table10422
+ GCC_except_table10423
+ GCC_except_table10424
+ GCC_except_table10425
+ GCC_except_table10426
+ GCC_except_table10427
+ GCC_except_table10428
+ GCC_except_table10429
+ GCC_except_table10430
+ GCC_except_table10467
+ GCC_except_table10472
+ GCC_except_table10492
+ GCC_except_table10499
+ GCC_except_table10581
+ GCC_except_table10674
+ GCC_except_table10841
+ GCC_except_table10861
+ GCC_except_table10864
+ GCC_except_table10865
+ GCC_except_table10891
+ GCC_except_table10893
+ GCC_except_table10983
+ GCC_except_table11001
+ GCC_except_table1119
+ GCC_except_table1137
+ GCC_except_table11520
+ GCC_except_table1164
+ GCC_except_table11680
+ GCC_except_table11687
+ GCC_except_table11695
+ GCC_except_table11699
+ GCC_except_table11701
+ GCC_except_table11705
+ GCC_except_table11711
+ GCC_except_table11817
+ GCC_except_table11836
+ GCC_except_table11838
+ GCC_except_table11840
+ GCC_except_table11842
+ GCC_except_table11877
+ GCC_except_table11926
+ GCC_except_table11933
+ GCC_except_table11935
+ GCC_except_table11937
+ GCC_except_table11943
+ GCC_except_table11980
+ GCC_except_table12111
+ GCC_except_table12137
+ GCC_except_table12149
+ GCC_except_table12191
+ GCC_except_table12205
+ GCC_except_table12291
+ GCC_except_table12295
+ GCC_except_table12336
+ GCC_except_table12340
+ GCC_except_table12349
+ GCC_except_table12350
+ GCC_except_table12357
+ GCC_except_table12395
+ GCC_except_table12402
+ GCC_except_table12412
+ GCC_except_table12417
+ GCC_except_table12467
+ GCC_except_table12559
+ GCC_except_table12562
+ GCC_except_table12568
+ GCC_except_table12570
+ GCC_except_table1258
+ GCC_except_table12610
+ GCC_except_table12629
+ GCC_except_table12640
+ GCC_except_table12702
+ GCC_except_table12705
+ GCC_except_table12713
+ GCC_except_table12719
+ GCC_except_table12721
+ GCC_except_table1277
+ GCC_except_table12786
+ GCC_except_table12864
+ GCC_except_table12868
+ GCC_except_table12909
+ GCC_except_table12933
+ GCC_except_table12940
+ GCC_except_table13070
+ GCC_except_table13082
+ GCC_except_table13177
+ GCC_except_table13244
+ GCC_except_table13450
+ GCC_except_table1352
+ GCC_except_table13529
+ GCC_except_table13571
+ GCC_except_table13620
+ GCC_except_table13630
+ GCC_except_table13650
+ GCC_except_table13665
+ GCC_except_table13693
+ GCC_except_table13695
+ GCC_except_table13708
+ GCC_except_table13710
+ GCC_except_table13712
+ GCC_except_table13731
+ GCC_except_table13877
+ GCC_except_table13888
+ GCC_except_table13915
+ GCC_except_table13921
+ GCC_except_table13937
+ GCC_except_table14007
+ GCC_except_table14009
+ GCC_except_table14055
+ GCC_except_table14057
+ GCC_except_table14081
+ GCC_except_table14084
+ GCC_except_table14238
+ GCC_except_table1446
+ GCC_except_table1471
+ GCC_except_table1517
+ GCC_except_table1592
+ GCC_except_table1692
+ GCC_except_table1794
+ GCC_except_table1798
+ GCC_except_table1824
+ GCC_except_table1829
+ GCC_except_table1833
+ GCC_except_table1843
+ GCC_except_table2030
+ GCC_except_table2034
+ GCC_except_table2038
+ GCC_except_table2040
+ GCC_except_table2042
+ GCC_except_table2044
+ GCC_except_table2054
+ GCC_except_table2056
+ GCC_except_table2058
+ GCC_except_table2070
+ GCC_except_table2102
+ GCC_except_table2104
+ GCC_except_table2106
+ GCC_except_table2108
+ GCC_except_table2110
+ GCC_except_table2112
+ GCC_except_table2114
+ GCC_except_table2116
+ GCC_except_table2118
+ GCC_except_table2120
+ GCC_except_table2122
+ GCC_except_table2139
+ GCC_except_table2141
+ GCC_except_table2143
+ GCC_except_table2146
+ GCC_except_table2148
+ GCC_except_table2151
+ GCC_except_table2153
+ GCC_except_table2155
+ GCC_except_table2183
+ GCC_except_table2185
+ GCC_except_table2188
+ GCC_except_table2191
+ GCC_except_table2295
+ GCC_except_table2300
+ GCC_except_table2310
+ GCC_except_table2322
+ GCC_except_table2362
+ GCC_except_table2535
+ GCC_except_table2548
+ GCC_except_table2576
+ GCC_except_table2593
+ GCC_except_table2612
+ GCC_except_table2622
+ GCC_except_table2659
+ GCC_except_table2664
+ GCC_except_table2726
+ GCC_except_table2842
+ GCC_except_table2844
+ GCC_except_table2850
+ GCC_except_table2858
+ GCC_except_table2890
+ GCC_except_table2976
+ GCC_except_table2981
+ GCC_except_table2984
+ GCC_except_table2994
+ GCC_except_table3007
+ GCC_except_table3009
+ GCC_except_table3016
+ GCC_except_table3146
+ GCC_except_table3150
+ GCC_except_table3153
+ GCC_except_table3220
+ GCC_except_table3228
+ GCC_except_table3263
+ GCC_except_table3267
+ GCC_except_table3272
+ GCC_except_table3396
+ GCC_except_table3429
+ GCC_except_table3435
+ GCC_except_table3438
+ GCC_except_table3448
+ GCC_except_table3463
+ GCC_except_table3466
+ GCC_except_table3475
+ GCC_except_table3479
+ GCC_except_table3493
+ GCC_except_table3511
+ GCC_except_table3512
+ GCC_except_table3528
+ GCC_except_table3537
+ GCC_except_table3634
+ GCC_except_table3641
+ GCC_except_table3662
+ GCC_except_table3664
+ GCC_except_table3666
+ GCC_except_table3713
+ GCC_except_table3741
+ GCC_except_table3772
+ GCC_except_table3774
+ GCC_except_table3792
+ GCC_except_table3794
+ GCC_except_table3797
+ GCC_except_table3957
+ GCC_except_table3991
+ GCC_except_table3999
+ GCC_except_table4001
+ GCC_except_table4016
+ GCC_except_table4019
+ GCC_except_table4021
+ GCC_except_table4054
+ GCC_except_table4059
+ GCC_except_table4060
+ GCC_except_table4314
+ GCC_except_table4321
+ GCC_except_table4352
+ GCC_except_table4373
+ GCC_except_table4376
+ GCC_except_table4382
+ GCC_except_table4387
+ GCC_except_table4398
+ GCC_except_table4402
+ GCC_except_table4420
+ GCC_except_table4486
+ GCC_except_table4811
+ GCC_except_table4821
+ GCC_except_table487
+ GCC_except_table4881
+ GCC_except_table4885
+ GCC_except_table4887
+ GCC_except_table4890
+ GCC_except_table496
+ GCC_except_table4960
+ GCC_except_table4965
+ GCC_except_table498
+ GCC_except_table4998
+ GCC_except_table506
+ GCC_except_table508
+ GCC_except_table5128
+ GCC_except_table5132
+ GCC_except_table5479
+ GCC_except_table5510
+ GCC_except_table5556
+ GCC_except_table5582
+ GCC_except_table5615
+ GCC_except_table5620
+ GCC_except_table5644
+ GCC_except_table5648
+ GCC_except_table5652
+ GCC_except_table5674
+ GCC_except_table5680
+ GCC_except_table5684
+ GCC_except_table5698
+ GCC_except_table5701
+ GCC_except_table5704
+ GCC_except_table5727
+ GCC_except_table5762
+ GCC_except_table5783
+ GCC_except_table5794
+ GCC_except_table580
+ GCC_except_table5833
+ GCC_except_table5845
+ GCC_except_table5879
+ GCC_except_table5882
+ GCC_except_table5888
+ GCC_except_table5892
+ GCC_except_table5904
+ GCC_except_table5937
+ GCC_except_table5966
+ GCC_except_table5993
+ GCC_except_table5995
+ GCC_except_table6008
+ GCC_except_table6077
+ GCC_except_table6154
+ GCC_except_table6159
+ GCC_except_table6164
+ GCC_except_table625
+ GCC_except_table6322
+ GCC_except_table6327
+ GCC_except_table6340
+ GCC_except_table6365
+ GCC_except_table6376
+ GCC_except_table6379
+ GCC_except_table6417
+ GCC_except_table6454
+ GCC_except_table6456
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table6855
+ GCC_except_table6875
+ GCC_except_table6888
+ GCC_except_table6901
+ GCC_except_table6920
+ GCC_except_table6950
+ GCC_except_table6953
+ GCC_except_table6955
+ GCC_except_table6957
+ GCC_except_table6959
+ GCC_except_table6968
+ GCC_except_table698
+ GCC_except_table701
+ GCC_except_table7016
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table7030
+ GCC_except_table704
+ GCC_except_table705
+ GCC_except_table7066
+ GCC_except_table7068
+ GCC_except_table707
+ GCC_except_table7107
+ GCC_except_table7360
+ GCC_except_table7363
+ GCC_except_table7385
+ GCC_except_table7392
+ GCC_except_table7410
+ GCC_except_table7416
+ GCC_except_table7417
+ GCC_except_table7418
+ GCC_except_table7419
+ GCC_except_table7430
+ GCC_except_table7431
+ GCC_except_table7432
+ GCC_except_table7589
+ GCC_except_table7809
+ GCC_except_table785
+ GCC_except_table7854
+ GCC_except_table7872
+ GCC_except_table7873
+ GCC_except_table7932
+ GCC_except_table7957
+ GCC_except_table796
+ GCC_except_table7961
+ GCC_except_table7968
+ GCC_except_table8022
+ GCC_except_table8228
+ GCC_except_table8230
+ GCC_except_table8277
+ GCC_except_table8317
+ GCC_except_table8321
+ GCC_except_table8323
+ GCC_except_table8337
+ GCC_except_table8342
+ GCC_except_table8382
+ GCC_except_table8410
+ GCC_except_table8452
+ GCC_except_table8534
+ GCC_except_table8592
+ GCC_except_table8613
+ GCC_except_table8616
+ GCC_except_table8635
+ GCC_except_table8694
+ GCC_except_table8700
+ GCC_except_table8706
+ GCC_except_table8707
+ GCC_except_table8708
+ GCC_except_table8709
+ GCC_except_table8710
+ GCC_except_table8714
+ GCC_except_table8718
+ GCC_except_table8729
+ GCC_except_table8732
+ GCC_except_table8757
+ GCC_except_table8805
+ GCC_except_table8870
+ GCC_except_table890
+ GCC_except_table9027
+ GCC_except_table9068
+ GCC_except_table9074
+ GCC_except_table9077
+ GCC_except_table9340
+ GCC_except_table9344
+ GCC_except_table9372
+ GCC_except_table9373
+ GCC_except_table942
+ GCC_except_table9471
+ GCC_except_table9481
+ GCC_except_table9514
+ GCC_except_table9566
+ GCC_except_table9611
+ GCC_except_table9631
+ GCC_except_table9659
+ GCC_except_table966
+ GCC_except_table9687
+ GCC_except_table970
+ GCC_except_table9720
+ GCC_except_table9722
+ GCC_except_table981
+ GCC_except_table9813
+ GCC_except_table983
+ GCC_except_table9904
+ OBJC_IVAR_$_PHAssetExtendedMetadata._originalFilename
+ OBJC_IVAR_$_PHAssetResource._filename
+ OBJC_IVAR_$_PHAssetResourceUploadJobConfiguration._options
+ OBJC_IVAR_$_PHAssetResourceUploadJobOptions._preventsExpensiveNetworkAccess
+ OBJC_IVAR_$_PHPerformChangesTransaction._clientProvider
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionKey
+ _OBJC_CLASS_$_PHAssetResourceUploadJobOptions
+ _OBJC_CLASS_$_PLPhotoLibraryBundle
+ _OBJC_METACLASS_$_PHAssetResourceUploadJobOptions
+ _PHFindSuggestionAndPredicateFromParseTokens
+ _PLAssetResourceUploadJobConfigurationOptionsPreventsExpensiveNetworkAccess
+ _PLCameraMessagesBundleId
+ _PLFileProviderBundleIDRemappedToAppBundleID
+ __134-[PHPerformChangesTransaction _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]_block_invoke
+ __211-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:skipSharePost:]_block_invoke
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PLPhotoLibraryBundle_$_PHPerformChanges
+ __OBJC_$_CATEGORY_PLPhotoLibraryBundle_$_PHPerformChanges
+ __OBJC_$_CLASS_METHODS_PHAssetResourceUploadJobOptions
+ __OBJC_$_CLASS_PROP_LIST_PHCreationRequestOptions
+ __OBJC_$_INSTANCE_METHODS_PHAssetResourceUploadJobOptions
+ __OBJC_$_INSTANCE_VARIABLES_PHAssetResourceUploadJobOptions
+ __OBJC_$_PROP_LIST_PHAssetResourceUploadJobOptions
+ __OBJC_$_PROP_LIST_PLPhotoLibraryBundle_$_PHPerformChanges
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PHPerformChangesClientProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PHPerformChangesClientProvider
+ __OBJC_$_PROTOCOL_REFS_PHPerformChangesClientProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_PLPhotoLibraryBundle_$_PHPerformChanges
+ __OBJC_CLASS_PROTOCOLS_$_PHAssetResourceUploadJobOptions
+ __OBJC_CLASS_RO_$_PHAssetResourceUploadJobOptions
+ __OBJC_LABEL_PROTOCOL_$_PHPerformChangesClientProvider
+ __OBJC_METACLASS_RO_$_PHAssetResourceUploadJobOptions
+ __OBJC_PROTOCOL_$_PHPerformChangesClientProvider
+ ___102-[PHPerformChangesTransaction _sendSingleChangesRequest:onExecutionContext:withInstrumentation:reply:]_block_invoke
+ ___134-[PHPerformChangesTransaction _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]_block_invoke
+ ___160+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:allowedBundleIdentifiers:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke
+ ___160+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:allowedBundleIdentifiers:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke_2
+ ___211-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:skipSharePost:]_block_invoke
+ ___53-[PHPhotoLibrary setUploadJobExtensionOptions:error:]_block_invoke
+ ___59+[PHSearchQueryManager _filterResults:withValidAssetUUIDs:]_block_invoke
+ ___62+[PHFindQueryUtilities leoSortDescriptorsFromSortDescriptors:]_block_invoke
+ ___66-[PHPhotoLibrary _deleteUploadJobExtensionConfigurationWithError:]_block_invoke
+ ___68+[PHSearchQueryManager _fetchVisibleAssetUUIDsForResults:inLibrary:]_block_invoke
+ ___74-[PHPhotoLibrary _createUploadJobExtensionConfigurationWithOptions:error:]_block_invoke
+ ___96+[PHSearchUtility searchIntentsAttributedStringFromWhoValues:whatValues:whereValues:whenValues:]_block_invoke
+ ___block_descriptor_40_e8_32s_e24_B16?0"PHSearchResult"8l
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSSortDescriptor"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e43_v24?0"NSArray"8"PHSearchIntentQUToken"16l
+ ___block_descriptor_96_e8_32s40s48r56r64r72r80r_e56_v48?0"NSArray"8"NSArray"16"NSArray"24Q32"NSError"40l
+ _objc_msgSend$_createUploadJobExtensionConfigurationWithOptions:error:
+ _objc_msgSend$_deleteUploadJobExtensionConfigurationWithError:
+ _objc_msgSend$_entitledClientSkipsUUIDValidation
+ _objc_msgSend$_fetchVisibleAssetUUIDsForResults:inLibrary:
+ _objc_msgSend$_filterResults:withValidAssetUUIDs:
+ _objc_msgSend$_performIntentSearchForLibrary:searchText:searchOptions:allowedBundleIdentifiers:maximumSearchResults:allowUnattributedQuery:completion:
+ _objc_msgSend$_sendSingleChangesRequest:onExecutionContext:withInstrumentation:reply:
+ _objc_msgSend$_setUploadJobExtensionEnabled:options:error:
+ _objc_msgSend$addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:skipSharePost:
+ _objc_msgSend$addAssetsToCollectionShareByCopyingSourceAssets:creationOptionsMappedToSourceAssets:withBatchCommentText:outCreatedSharePostPlaceholder:skipSharePost:
+ _objc_msgSend$bundleIdentifiersAllowedForSiriSearch
+ _objc_msgSend$changeRequestForAssetResourceUploadJobConfiguration:
+ _objc_msgSend$commitTransactionWithChangesRequest:onExecutionContext:withInstrumentation:retryCount:reply:
+ _objc_msgSend$disableUploadJobExtensionWithError:
+ _objc_msgSend$dispatchRetryOnQueue:block:
+ _objc_msgSend$initWithQueue:priority:clientProvider:
+ _objc_msgSend$leoSortDescriptorsFromSortDescriptors:
+ _objc_msgSend$osMigrationTransferableResourcePredicate
+ _objc_msgSend$ph_dictionaryRepresentation
+ _objc_msgSend$ph_optionsDictionary
+ _objc_msgSend$ph_optionsWithDictionary:
+ _objc_msgSend$ph_setOptionsDictionary:
+ _objc_msgSend$photoKitClientForAccessLevel:
+ _objc_msgSend$predicateForResourcesForOsMigrationForResourceTypes:assetIDs:includeLocalOnly:iCPLEnabled:includeFullSizeRenders:
+ _objc_msgSend$preventsExpensiveNetworkAccess
+ _objc_msgSend$searchIntentsAttributedStringFromWhoValues:whatValues:whereValues:whenValues:
+ _objc_msgSend$setPreventsExpensiveNetworkAccess:
+ _objc_msgSend$spotlightTextLinesFromDocumentObservation:withTextFound:
+ sharedLazyPhotoLibraryForCMM.pl_once_object_46
+ sharedLazyPhotoLibraryForCMM.pl_once_token_46
- +[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]
- -[PHAssetExtendedMetadata originalFileName]
- -[PHPerformChangesTransaction initWithQueue:priority:]
- -[PHPhotoLibrary _clientForAccessLevel:]
- -[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]
- -[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:reply:]
- -[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:]
- GCC_except_table10002
- GCC_except_table10012
- GCC_except_table10027
- GCC_except_table10034
- GCC_except_table10037
- GCC_except_table10060
- GCC_except_table10062
- GCC_except_table10063
- GCC_except_table10064
- GCC_except_table10065
- GCC_except_table10066
- GCC_except_table10067
- GCC_except_table10070
- GCC_except_table10071
- GCC_except_table10072
- GCC_except_table10073
- GCC_except_table10074
- GCC_except_table10075
- GCC_except_table10076
- GCC_except_table10077
- GCC_except_table10079
- GCC_except_table10080
- GCC_except_table10081
- GCC_except_table10082
- GCC_except_table10083
- GCC_except_table10092
- GCC_except_table10102
- GCC_except_table10117
- GCC_except_table10127
- GCC_except_table10288
- GCC_except_table10297
- GCC_except_table10298
- GCC_except_table10299
- GCC_except_table10300
- GCC_except_table10301
- GCC_except_table10302
- GCC_except_table10303
- GCC_except_table10314
- GCC_except_table10332
- GCC_except_table10365
- GCC_except_table10366
- GCC_except_table10367
- GCC_except_table10368
- GCC_except_table10369
- GCC_except_table10379
- GCC_except_table10397
- GCC_except_table10398
- GCC_except_table10399
- GCC_except_table10400
- GCC_except_table10401
- GCC_except_table10402
- GCC_except_table10404
- GCC_except_table10405
- GCC_except_table10406
- GCC_except_table10443
- GCC_except_table10444
- GCC_except_table10448
- GCC_except_table10475
- GCC_except_table10557
- GCC_except_table10650
- GCC_except_table10816
- GCC_except_table10836
- GCC_except_table10839
- GCC_except_table10840
- GCC_except_table10866
- GCC_except_table10868
- GCC_except_table10958
- GCC_except_table10976
- GCC_except_table1109
- GCC_except_table1127
- GCC_except_table11486
- GCC_except_table1153
- GCC_except_table11643
- GCC_except_table11646
- GCC_except_table11653
- GCC_except_table11661
- GCC_except_table11665
- GCC_except_table11667
- GCC_except_table11671
- GCC_except_table11783
- GCC_except_table11802
- GCC_except_table11804
- GCC_except_table11806
- GCC_except_table11808
- GCC_except_table11843
- GCC_except_table11892
- GCC_except_table11899
- GCC_except_table11901
- GCC_except_table11903
- GCC_except_table11909
- GCC_except_table11946
- GCC_except_table12077
- GCC_except_table12103
- GCC_except_table12115
- GCC_except_table12157
- GCC_except_table12171
- GCC_except_table12257
- GCC_except_table12261
- GCC_except_table12302
- GCC_except_table12306
- GCC_except_table12315
- GCC_except_table12316
- GCC_except_table12323
- GCC_except_table12361
- GCC_except_table12368
- GCC_except_table12378
- GCC_except_table12383
- GCC_except_table12433
- GCC_except_table1247
- GCC_except_table12525
- GCC_except_table12528
- GCC_except_table12534
- GCC_except_table12538
- GCC_except_table12578
- GCC_except_table12597
- GCC_except_table12608
- GCC_except_table1266
- GCC_except_table12666
- GCC_except_table12669
- GCC_except_table12677
- GCC_except_table12683
- GCC_except_table12685
- GCC_except_table12749
- GCC_except_table12827
- GCC_except_table12831
- GCC_except_table12835
- GCC_except_table12896
- GCC_except_table12903
- GCC_except_table13033
- GCC_except_table13045
- GCC_except_table13138
- GCC_except_table13205
- GCC_except_table1341
- GCC_except_table13411
- GCC_except_table13489
- GCC_except_table13531
- GCC_except_table13580
- GCC_except_table13590
- GCC_except_table13610
- GCC_except_table13625
- GCC_except_table13653
- GCC_except_table13655
- GCC_except_table13668
- GCC_except_table13670
- GCC_except_table13672
- GCC_except_table13691
- GCC_except_table13837
- GCC_except_table13848
- GCC_except_table13875
- GCC_except_table13881
- GCC_except_table13897
- GCC_except_table13967
- GCC_except_table13969
- GCC_except_table14015
- GCC_except_table14017
- GCC_except_table14041
- GCC_except_table14044
- GCC_except_table14198
- GCC_except_table1435
- GCC_except_table1460
- GCC_except_table1506
- GCC_except_table1581
- GCC_except_table1681
- GCC_except_table1783
- GCC_except_table1787
- GCC_except_table1813
- GCC_except_table1818
- GCC_except_table1822
- GCC_except_table1832
- GCC_except_table2019
- GCC_except_table2023
- GCC_except_table2025
- GCC_except_table2027
- GCC_except_table2029
- GCC_except_table2031
- GCC_except_table2033
- GCC_except_table2043
- GCC_except_table2045
- GCC_except_table2059
- GCC_except_table2091
- GCC_except_table2093
- GCC_except_table2095
- GCC_except_table2097
- GCC_except_table2099
- GCC_except_table2101
- GCC_except_table2103
- GCC_except_table2105
- GCC_except_table2107
- GCC_except_table2109
- GCC_except_table2111
- GCC_except_table2113
- GCC_except_table2115
- GCC_except_table2117
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2140
- GCC_except_table2142
- GCC_except_table2144
- GCC_except_table2172
- GCC_except_table2174
- GCC_except_table2177
- GCC_except_table2180
- GCC_except_table2284
- GCC_except_table2289
- GCC_except_table2299
- GCC_except_table2311
- GCC_except_table2351
- GCC_except_table2524
- GCC_except_table2537
- GCC_except_table2565
- GCC_except_table2582
- GCC_except_table2601
- GCC_except_table2611
- GCC_except_table2648
- GCC_except_table2653
- GCC_except_table2715
- GCC_except_table2820
- GCC_except_table2833
- GCC_except_table2839
- GCC_except_table2847
- GCC_except_table2879
- GCC_except_table2959
- GCC_except_table2965
- GCC_except_table2973
- GCC_except_table2983
- GCC_except_table2996
- GCC_except_table2998
- GCC_except_table3005
- GCC_except_table3135
- GCC_except_table3139
- GCC_except_table3142
- GCC_except_table3209
- GCC_except_table3217
- GCC_except_table3252
- GCC_except_table3256
- GCC_except_table3261
- GCC_except_table3385
- GCC_except_table3418
- GCC_except_table3424
- GCC_except_table3427
- GCC_except_table3437
- GCC_except_table3441
- GCC_except_table3455
- GCC_except_table3464
- GCC_except_table3468
- GCC_except_table3482
- GCC_except_table3489
- GCC_except_table3501
- GCC_except_table3517
- GCC_except_table3526
- GCC_except_table3623
- GCC_except_table3630
- GCC_except_table3651
- GCC_except_table3653
- GCC_except_table3655
- GCC_except_table3702
- GCC_except_table3730
- GCC_except_table3761
- GCC_except_table3763
- GCC_except_table3781
- GCC_except_table3783
- GCC_except_table3786
- GCC_except_table3946
- GCC_except_table3980
- GCC_except_table3988
- GCC_except_table3990
- GCC_except_table4005
- GCC_except_table4008
- GCC_except_table4010
- GCC_except_table4043
- GCC_except_table4048
- GCC_except_table4049
- GCC_except_table4303
- GCC_except_table4309
- GCC_except_table4340
- GCC_except_table4361
- GCC_except_table4364
- GCC_except_table4370
- GCC_except_table4375
- GCC_except_table4386
- GCC_except_table4390
- GCC_except_table4408
- GCC_except_table4474
- GCC_except_table4799
- GCC_except_table4809
- GCC_except_table483
- GCC_except_table4869
- GCC_except_table4873
- GCC_except_table4875
- GCC_except_table4878
- GCC_except_table492
- GCC_except_table494
- GCC_except_table4948
- GCC_except_table4953
- GCC_except_table4986
- GCC_except_table502
- GCC_except_table504
- GCC_except_table5116
- GCC_except_table5120
- GCC_except_table5466
- GCC_except_table5497
- GCC_except_table5543
- GCC_except_table5569
- GCC_except_table5602
- GCC_except_table5607
- GCC_except_table5631
- GCC_except_table5635
- GCC_except_table5639
- GCC_except_table5661
- GCC_except_table5667
- GCC_except_table5671
- GCC_except_table5685
- GCC_except_table5688
- GCC_except_table5691
- GCC_except_table5714
- GCC_except_table5755
- GCC_except_table576
- GCC_except_table5776
- GCC_except_table5787
- GCC_except_table5826
- GCC_except_table5838
- GCC_except_table5872
- GCC_except_table5875
- GCC_except_table5881
- GCC_except_table5885
- GCC_except_table5897
- GCC_except_table5922
- GCC_except_table5951
- GCC_except_table5978
- GCC_except_table5980
- GCC_except_table5992
- GCC_except_table6061
- GCC_except_table612
- GCC_except_table6138
- GCC_except_table6143
- GCC_except_table6148
- GCC_except_table6306
- GCC_except_table6311
- GCC_except_table6324
- GCC_except_table634
- GCC_except_table6349
- GCC_except_table636
- GCC_except_table6360
- GCC_except_table6363
- GCC_except_table640
- GCC_except_table6401
- GCC_except_table643
- GCC_except_table6438
- GCC_except_table6440
- GCC_except_table6839
- GCC_except_table685
- GCC_except_table6859
- GCC_except_table6872
- GCC_except_table688
- GCC_except_table6885
- GCC_except_table689
- GCC_except_table690
- GCC_except_table6904
- GCC_except_table691
- GCC_except_table692
- GCC_except_table6934
- GCC_except_table6937
- GCC_except_table6939
- GCC_except_table694
- GCC_except_table6941
- GCC_except_table6943
- GCC_except_table6952
- GCC_except_table6999
- GCC_except_table7013
- GCC_except_table7049
- GCC_except_table7051
- GCC_except_table7090
- GCC_except_table7343
- GCC_except_table7346
- GCC_except_table7368
- GCC_except_table7375
- GCC_except_table7393
- GCC_except_table7397
- GCC_except_table7398
- GCC_except_table7399
- GCC_except_table7400
- GCC_except_table7401
- GCC_except_table7402
- GCC_except_table7413
- GCC_except_table7572
- GCC_except_table772
- GCC_except_table7792
- GCC_except_table783
- GCC_except_table7837
- GCC_except_table7855
- GCC_except_table7856
- GCC_except_table7915
- GCC_except_table7940
- GCC_except_table7944
- GCC_except_table7951
- GCC_except_table8005
- GCC_except_table8211
- GCC_except_table8213
- GCC_except_table8260
- GCC_except_table8300
- GCC_except_table8304
- GCC_except_table8306
- GCC_except_table8308
- GCC_except_table8320
- GCC_except_table8365
- GCC_except_table8393
- GCC_except_table8435
- GCC_except_table8517
- GCC_except_table8575
- GCC_except_table8596
- GCC_except_table8599
- GCC_except_table8618
- GCC_except_table8677
- GCC_except_table8683
- GCC_except_table8689
- GCC_except_table8690
- GCC_except_table8691
- GCC_except_table8692
- GCC_except_table8693
- GCC_except_table8695
- GCC_except_table8697
- GCC_except_table8701
- GCC_except_table8715
- GCC_except_table8736
- GCC_except_table877
- GCC_except_table8781
- GCC_except_table8846
- GCC_except_table9003
- GCC_except_table9044
- GCC_except_table9050
- GCC_except_table9053
- GCC_except_table930
- GCC_except_table9316
- GCC_except_table9320
- GCC_except_table9324
- GCC_except_table9349
- GCC_except_table9447
- GCC_except_table9457
- GCC_except_table9490
- GCC_except_table9542
- GCC_except_table956
- GCC_except_table9587
- GCC_except_table960
- GCC_except_table9607
- GCC_except_table9635
- GCC_except_table9663
- GCC_except_table9696
- GCC_except_table9698
- GCC_except_table971
- GCC_except_table973
- GCC_except_table9789
- GCC_except_table9880
- OBJC_IVAR_$_PHAssetExtendedMetadata._originalFileName
- OBJC_IVAR_$_PHAssetResource._originalFilename
- __121-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]_block_invoke
- __197-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:]_block_invoke
- ___121-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]_block_invoke
- ___135+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke
- ___135+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke_2
- ___197-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:]_block_invoke
- ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke
- ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke_2
- ___83-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:reply:]_block_invoke
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e56_v48?0"NSArray"8"NSArray"16"NSArray"24Q32"NSError"40l
- _objc_msgSend$_clientForAccessLevel:
- _objc_msgSend$_performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:
- _objc_msgSend$_sendChangesRequest:onExecutionContext:withInstrumentation:reply:
- _objc_msgSend$addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:
- _objc_msgSend$flattenLivePhotoToStillIfNeeded
- _objc_msgSend$initWithQueue:priority:
- _objc_msgSend$spotlightTextLinesFromDocumentObservation:
- sharedLazyPhotoLibraryForCMM.pl_once_object_44
- sharedLazyPhotoLibraryForCMM.pl_once_token_44
CStrings:
+ "<%@: %p; preventsExpensiveNetworkAccess: %d>"
+ "B16@?0@\"PHSearchResult\"8"
+ "Excluding bundle from intent search: %@"
+ "Failed to archive search intents query, error: %@"
+ "PHPhotosErrorShareTypeRequiresOSUpgrade"
+ "PHPhotosErrorShareTypeUnsupported"
+ "PhotoKit XPC proxy is invalid. Retries left: %zd"
+ "Share %{public}@ skipping PHSharePost creation (skipSharePost); assets will be folded into an existing post"
+ "self.isClientEntitled"
+ "setUploadJobExtensionOptions called without authorization (status: %ld)"
+ "uploadJobExtensionOptions called without authorization (status: %ld)"
+ "v24@?0@\"NSArray\"8@\"PHSearchIntentQUToken\"16"
- "PhotoKit XPC proxy is invalid. Retry attempt: %zd"
```
