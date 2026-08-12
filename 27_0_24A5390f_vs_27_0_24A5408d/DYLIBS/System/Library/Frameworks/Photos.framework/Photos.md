## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x2d9bd0
-  __TEXT.__objc_methlist: 0x26b3c
+912.0.111.0.0
+  __TEXT.__text: 0x2dbfe0
+  __TEXT.__objc_methlist: 0x26d04
   __TEXT.__const: 0x1778
   __TEXT.__dlopen_cstrs: 0x280
   __TEXT.__constg_swiftt: 0x544

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__cstring: 0x3270e
+  __TEXT.__cstring: 0x327f6
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__oslogstring: 0x23415
+  __TEXT.__oslogstring: 0x23567
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x95bc
+  __TEXT.__gcc_except_tab: 0x96a8
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x9668
+  __TEXT.__unwind_info: 0x96e0
   __TEXT.__eh_frame: 0x4a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8f40
-  __DATA_CONST.__objc_classlist: 0xf28
-  __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x2f8
+  __DATA_CONST.__const: 0x8fb8
+  __DATA_CONST.__objc_classlist: 0xf30
+  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14620
+  __DATA_CONST.__objc_selrefs: 0x146f0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc60
-  __DATA_CONST.__objc_arraydata: 0x900
-  __DATA_CONST.__got: 0x2990
+  __DATA_CONST.__objc_arraydata: 0x920
+  __DATA_CONST.__got: 0x29c8
   __AUTH_CONST.__const: 0x46d8
-  __AUTH_CONST.__cfstring: 0x2d5c0
-  __AUTH_CONST.__objc_const: 0x420c0
+  __AUTH_CONST.__cfstring: 0x2d660
+  __AUTH_CONST.__objc_const: 0x42310
   __AUTH_CONST.__objc_intobj: 0x23e8
   __AUTH_CONST.__objc_arrayobj: 0x798
   __AUTH_CONST.__objc_doubleobj: 0x130
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x18b8
-  __AUTH.__objc_data: 0x7d98
+  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH.__objc_data: 0x7de8
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x35f0
-  __DATA.__data: 0x2b68
+  __DATA.__objc_ivar: 0x35fc
+  __DATA.__data: 0x2bc8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1a68
   __DATA.__common: 0x55

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14868
-  Symbols:   33959
-  CStrings:  8854
+  Functions: 14909
+  Symbols:   34053
+  CStrings:  8866
 
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
+ GCC_except_table10055
+ GCC_except_table10177
+ GCC_except_table10201
+ GCC_except_table10202
+ GCC_except_table10209
+ GCC_except_table10212
+ GCC_except_table10246
+ GCC_except_table10256
+ GCC_except_table10331
+ GCC_except_table10332
+ GCC_except_table10333
+ GCC_except_table10334
+ GCC_except_table10335
+ GCC_except_table10336
+ GCC_except_table10337
+ GCC_except_table10338
+ GCC_except_table10339
+ GCC_except_table10340
+ GCC_except_table10341
+ GCC_except_table10342
+ GCC_except_table10343
+ GCC_except_table10344
+ GCC_except_table10345
+ GCC_except_table10346
+ GCC_except_table10347
+ GCC_except_table10348
+ GCC_except_table10349
+ GCC_except_table10350
+ GCC_except_table10351
+ GCC_except_table10352
+ GCC_except_table1039
+ GCC_except_table10463
+ GCC_except_table10472
+ GCC_except_table10473
+ GCC_except_table10474
+ GCC_except_table10475
+ GCC_except_table10476
+ GCC_except_table10477
+ GCC_except_table10478
+ GCC_except_table10489
+ GCC_except_table10507
+ GCC_except_table10540
+ GCC_except_table10541
+ GCC_except_table10542
+ GCC_except_table10543
+ GCC_except_table10544
+ GCC_except_table10572
+ GCC_except_table10573
+ GCC_except_table10574
+ GCC_except_table10575
+ GCC_except_table10576
+ GCC_except_table10577
+ GCC_except_table10578
+ GCC_except_table10579
+ GCC_except_table10580
+ GCC_except_table10581
+ GCC_except_table1061
+ GCC_except_table10618
+ GCC_except_table10619
+ GCC_except_table10623
+ GCC_except_table10642
+ GCC_except_table10647
+ GCC_except_table1065
+ GCC_except_table10729
+ GCC_except_table1074
+ GCC_except_table1076
+ GCC_except_table10822
+ GCC_except_table11008
+ GCC_except_table11011
+ GCC_except_table11012
+ GCC_except_table11038
+ GCC_except_table11040
+ GCC_except_table11130
+ GCC_except_table11158
+ GCC_except_table11692
+ GCC_except_table11849
+ GCC_except_table11852
+ GCC_except_table11858
+ GCC_except_table11866
+ GCC_except_table11870
+ GCC_except_table11872
+ GCC_except_table11876
+ GCC_except_table11882
+ GCC_except_table11988
+ GCC_except_table12007
+ GCC_except_table12009
+ GCC_except_table12011
+ GCC_except_table12013
+ GCC_except_table12048
+ GCC_except_table12097
+ GCC_except_table1210
+ GCC_except_table12104
+ GCC_except_table12106
+ GCC_except_table12108
+ GCC_except_table12114
+ GCC_except_table12151
+ GCC_except_table1226
+ GCC_except_table12282
+ GCC_except_table12308
+ GCC_except_table12320
+ GCC_except_table12362
+ GCC_except_table12364
+ GCC_except_table12377
+ GCC_except_table12482
+ GCC_except_table12486
+ GCC_except_table12527
+ GCC_except_table1253
+ GCC_except_table12531
+ GCC_except_table12540
+ GCC_except_table12541
+ GCC_except_table12548
+ GCC_except_table12586
+ GCC_except_table12593
+ GCC_except_table12605
+ GCC_except_table12610
+ GCC_except_table12660
+ GCC_except_table12752
+ GCC_except_table12755
+ GCC_except_table12761
+ GCC_except_table12763
+ GCC_except_table12803
+ GCC_except_table12822
+ GCC_except_table12833
+ GCC_except_table12895
+ GCC_except_table12898
+ GCC_except_table12906
+ GCC_except_table12912
+ GCC_except_table12914
+ GCC_except_table12979
+ GCC_except_table13057
+ GCC_except_table13061
+ GCC_except_table13102
+ GCC_except_table13126
+ GCC_except_table13133
+ GCC_except_table13272
+ GCC_except_table13284
+ GCC_except_table13378
+ GCC_except_table13445
+ GCC_except_table1345
+ GCC_except_table1362
+ GCC_except_table13651
+ GCC_except_table13730
+ GCC_except_table13772
+ GCC_except_table13821
+ GCC_except_table13831
+ GCC_except_table13851
+ GCC_except_table13866
+ GCC_except_table13894
+ GCC_except_table13896
+ GCC_except_table13909
+ GCC_except_table13911
+ GCC_except_table13913
+ GCC_except_table13932
+ GCC_except_table14078
+ GCC_except_table14089
+ GCC_except_table14116
+ GCC_except_table14122
+ GCC_except_table14138
+ GCC_except_table14208
+ GCC_except_table14210
+ GCC_except_table14256
+ GCC_except_table14258
+ GCC_except_table14282
+ GCC_except_table14285
+ GCC_except_table14439
+ GCC_except_table1451
+ GCC_except_table1543
+ GCC_except_table1568
+ GCC_except_table1614
+ GCC_except_table1689
+ GCC_except_table1787
+ GCC_except_table1888
+ GCC_except_table1892
+ GCC_except_table1912
+ GCC_except_table1917
+ GCC_except_table1921
+ GCC_except_table1931
+ GCC_except_table2118
+ GCC_except_table2122
+ GCC_except_table2126
+ GCC_except_table2128
+ GCC_except_table2130
+ GCC_except_table2132
+ GCC_except_table2142
+ GCC_except_table2144
+ GCC_except_table2146
+ GCC_except_table2158
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2194
+ GCC_except_table2196
+ GCC_except_table2198
+ GCC_except_table2200
+ GCC_except_table2202
+ GCC_except_table2204
+ GCC_except_table2206
+ GCC_except_table2208
+ GCC_except_table2210
+ GCC_except_table2227
+ GCC_except_table2229
+ GCC_except_table2231
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2239
+ GCC_except_table2241
+ GCC_except_table2243
+ GCC_except_table2271
+ GCC_except_table2273
+ GCC_except_table2276
+ GCC_except_table2279
+ GCC_except_table2383
+ GCC_except_table2388
+ GCC_except_table2396
+ GCC_except_table2406
+ GCC_except_table2444
+ GCC_except_table2615
+ GCC_except_table2628
+ GCC_except_table2656
+ GCC_except_table2671
+ GCC_except_table2690
+ GCC_except_table2700
+ GCC_except_table2737
+ GCC_except_table2742
+ GCC_except_table2804
+ GCC_except_table2918
+ GCC_except_table2920
+ GCC_except_table2926
+ GCC_except_table2934
+ GCC_except_table2966
+ GCC_except_table3042
+ GCC_except_table3047
+ GCC_except_table3052
+ GCC_except_table3055
+ GCC_except_table3076
+ GCC_except_table3078
+ GCC_except_table3085
+ GCC_except_table3212
+ GCC_except_table3216
+ GCC_except_table3219
+ GCC_except_table3286
+ GCC_except_table3294
+ GCC_except_table3329
+ GCC_except_table3333
+ GCC_except_table3338
+ GCC_except_table3468
+ GCC_except_table3501
+ GCC_except_table3507
+ GCC_except_table3510
+ GCC_except_table3520
+ GCC_except_table3524
+ GCC_except_table3533
+ GCC_except_table3537
+ GCC_except_table3552
+ GCC_except_table3568
+ GCC_except_table3569
+ GCC_except_table3585
+ GCC_except_table3594
+ GCC_except_table3691
+ GCC_except_table3697
+ GCC_except_table3718
+ GCC_except_table3720
+ GCC_except_table3722
+ GCC_except_table3769
+ GCC_except_table3797
+ GCC_except_table3828
+ GCC_except_table3830
+ GCC_except_table3848
+ GCC_except_table3850
+ GCC_except_table3853
+ GCC_except_table4016
+ GCC_except_table4050
+ GCC_except_table4058
+ GCC_except_table4060
+ GCC_except_table4075
+ GCC_except_table4078
+ GCC_except_table4080
+ GCC_except_table4113
+ GCC_except_table4118
+ GCC_except_table4119
+ GCC_except_table4373
+ GCC_except_table4380
+ GCC_except_table4408
+ GCC_except_table4433
+ GCC_except_table4438
+ GCC_except_table4443
+ GCC_except_table4454
+ GCC_except_table4458
+ GCC_except_table4476
+ GCC_except_table4543
+ GCC_except_table4868
+ GCC_except_table4878
+ GCC_except_table4937
+ GCC_except_table4939
+ GCC_except_table4943
+ GCC_except_table4945
+ GCC_except_table4948
+ GCC_except_table5018
+ GCC_except_table5023
+ GCC_except_table5053
+ GCC_except_table5183
+ GCC_except_table5187
+ GCC_except_table5535
+ GCC_except_table5566
+ GCC_except_table560
+ GCC_except_table5612
+ GCC_except_table5631
+ GCC_except_table5637
+ GCC_except_table5643
+ GCC_except_table5655
+ GCC_except_table5657
+ GCC_except_table567
+ GCC_except_table5683
+ GCC_except_table5688
+ GCC_except_table569
+ GCC_except_table5691
+ GCC_except_table5693
+ GCC_except_table5699
+ GCC_except_table5720
+ GCC_except_table5724
+ GCC_except_table5763
+ GCC_except_table577
+ GCC_except_table579
+ GCC_except_table5796
+ GCC_except_table5801
+ GCC_except_table5825
+ GCC_except_table5829
+ GCC_except_table5833
+ GCC_except_table5855
+ GCC_except_table5861
+ GCC_except_table5865
+ GCC_except_table5879
+ GCC_except_table5882
+ GCC_except_table5885
+ GCC_except_table5908
+ GCC_except_table5942
+ GCC_except_table5963
+ GCC_except_table5972
+ GCC_except_table6011
+ GCC_except_table6023
+ GCC_except_table6057
+ GCC_except_table6060
+ GCC_except_table6066
+ GCC_except_table6070
+ GCC_except_table6082
+ GCC_except_table6115
+ GCC_except_table6144
+ GCC_except_table6173
+ GCC_except_table6187
+ GCC_except_table6256
+ GCC_except_table6333
+ GCC_except_table6338
+ GCC_except_table6343
+ GCC_except_table6504
+ GCC_except_table6517
+ GCC_except_table652
+ GCC_except_table6542
+ GCC_except_table6552
+ GCC_except_table6555
+ GCC_except_table6593
+ GCC_except_table6630
+ GCC_except_table6632
+ GCC_except_table7031
+ GCC_except_table7051
+ GCC_except_table7064
+ GCC_except_table7077
+ GCC_except_table7096
+ GCC_except_table7126
+ GCC_except_table7129
+ GCC_except_table7131
+ GCC_except_table7133
+ GCC_except_table7135
+ GCC_except_table7144
+ GCC_except_table7192
+ GCC_except_table7206
+ GCC_except_table7242
+ GCC_except_table7244
+ GCC_except_table7283
+ GCC_except_table729
+ GCC_except_table751
+ GCC_except_table753
+ GCC_except_table7536
+ GCC_except_table7539
+ GCC_except_table7561
+ GCC_except_table7568
+ GCC_except_table757
+ GCC_except_table7584
+ GCC_except_table7588
+ GCC_except_table7589
+ GCC_except_table7590
+ GCC_except_table7591
+ GCC_except_table760
+ GCC_except_table7602
+ GCC_except_table7603
+ GCC_except_table7604
+ GCC_except_table7761
+ GCC_except_table7980
+ GCC_except_table802
+ GCC_except_table8025
+ GCC_except_table8043
+ GCC_except_table8044
+ GCC_except_table805
+ GCC_except_table806
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table809
+ GCC_except_table8104
+ GCC_except_table811
+ GCC_except_table8126
+ GCC_except_table8130
+ GCC_except_table8137
+ GCC_except_table8191
+ GCC_except_table8391
+ GCC_except_table8393
+ GCC_except_table8440
+ GCC_except_table8480
+ GCC_except_table8484
+ GCC_except_table8486
+ GCC_except_table8500
+ GCC_except_table8505
+ GCC_except_table8545
+ GCC_except_table8573
+ GCC_except_table8615
+ GCC_except_table8706
+ GCC_except_table8764
+ GCC_except_table8784
+ GCC_except_table8787
+ GCC_except_table8806
+ GCC_except_table8865
+ GCC_except_table8869
+ GCC_except_table8873
+ GCC_except_table8874
+ GCC_except_table8875
+ GCC_except_table8876
+ GCC_except_table8877
+ GCC_except_table8881
+ GCC_except_table8885
+ GCC_except_table889
+ GCC_except_table8896
+ GCC_except_table8920
+ GCC_except_table8964
+ GCC_except_table898
+ GCC_except_table9029
+ GCC_except_table9186
+ GCC_except_table9227
+ GCC_except_table9233
+ GCC_except_table9236
+ GCC_except_table9499
+ GCC_except_table9503
+ GCC_except_table9507
+ GCC_except_table9527
+ GCC_except_table9528
+ GCC_except_table9624
+ GCC_except_table9634
+ GCC_except_table9667
+ GCC_except_table9719
+ GCC_except_table9764
+ GCC_except_table9784
+ GCC_except_table9810
+ GCC_except_table9838
+ GCC_except_table9871
+ GCC_except_table9873
+ GCC_except_table990
+ GCC_except_table9964
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionKey
+ _OBJC_CLASS_$_PHAssetResourceUploadJobOptions
+ _OBJC_CLASS_$_PLPhotoLibraryBundle
+ _OBJC_IVAR_$_PHAssetExtendedMetadata._originalFilename
+ _OBJC_IVAR_$_PHAssetResource._filename
+ _OBJC_IVAR_$_PHAssetResourceUploadJobConfiguration._options
+ _OBJC_IVAR_$_PHAssetResourceUploadJobOptions._preventsExpensiveNetworkAccess
+ _OBJC_IVAR_$_PHPerformChangesTransaction._clientProvider
+ _OBJC_METACLASS_$_PHAssetResourceUploadJobOptions
+ _PHFindSuggestionAndPredicateFromParseTokens
+ _PLAssetResourceUploadJobConfigurationOptionsPreventsExpensiveNetworkAccess
+ _PLCameraMessagesBundleId
+ _PLFileProviderBundleIDRemappedToAppBundleID
+ _TCCAccessCopyBundleIdentifiersDisabledForService
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
+ ___block_descriptor_40_e8_32s_e24_B16?0"PHSearchResult"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSSortDescriptor"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e43_v24?0"NSArray"8"PHSearchIntentQUToken"16ls32l8
+ ___block_descriptor_96_e8_32s40s48r56r64r72r80r_e56_v48?0"NSArray"8"NSArray"16"NSArray"24Q32"NSError"40ls32l8r48l8r56l8r64l8r72l8r80l8s40l8
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
+ _objc_msgSend$hiddenAppBundleIdentifiers
+ _objc_msgSend$initWithQueue:priority:clientProvider:
+ _objc_msgSend$leoSortDescriptorsFromSortDescriptors:
+ _objc_msgSend$lockedAppBundleIdentifiers
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
+ _sharedLazyPhotoLibraryForCMM.pl_once_object_46
+ _sharedLazyPhotoLibraryForCMM.pl_once_token_46
- +[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]
- -[PHAssetExtendedMetadata originalFileName]
- -[PHPerformChangesTransaction initWithQueue:priority:]
- -[PHPhotoLibrary _clientForAccessLevel:]
- -[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]
- -[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:reply:]
- -[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:]
- GCC_except_table10033
- GCC_except_table10155
- GCC_except_table10165
- GCC_except_table10179
- GCC_except_table10180
- GCC_except_table10190
- GCC_except_table10213
- GCC_except_table10214
- GCC_except_table10215
- GCC_except_table10216
- GCC_except_table10217
- GCC_except_table10218
- GCC_except_table10219
- GCC_except_table10220
- GCC_except_table10223
- GCC_except_table10224
- GCC_except_table10225
- GCC_except_table10226
- GCC_except_table10227
- GCC_except_table10228
- GCC_except_table10229
- GCC_except_table10230
- GCC_except_table10232
- GCC_except_table10233
- GCC_except_table10234
- GCC_except_table10243
- GCC_except_table10244
- GCC_except_table10253
- GCC_except_table10268
- GCC_except_table10278
- GCC_except_table1029
- GCC_except_table10441
- GCC_except_table10450
- GCC_except_table10451
- GCC_except_table10452
- GCC_except_table10453
- GCC_except_table10454
- GCC_except_table10455
- GCC_except_table10456
- GCC_except_table10467
- GCC_except_table10485
- GCC_except_table1051
- GCC_except_table10518
- GCC_except_table10519
- GCC_except_table10520
- GCC_except_table10521
- GCC_except_table10522
- GCC_except_table10532
- GCC_except_table1055
- GCC_except_table10550
- GCC_except_table10551
- GCC_except_table10552
- GCC_except_table10553
- GCC_except_table10555
- GCC_except_table10556
- GCC_except_table10557
- GCC_except_table10558
- GCC_except_table10559
- GCC_except_table10596
- GCC_except_table10597
- GCC_except_table10601
- GCC_except_table10620
- GCC_except_table10625
- GCC_except_table1064
- GCC_except_table1066
- GCC_except_table10707
- GCC_except_table10800
- GCC_except_table10966
- GCC_except_table10985
- GCC_except_table10988
- GCC_except_table11015
- GCC_except_table11017
- GCC_except_table11107
- GCC_except_table11135
- GCC_except_table11660
- GCC_except_table11817
- GCC_except_table11820
- GCC_except_table11826
- GCC_except_table11834
- GCC_except_table11838
- GCC_except_table11840
- GCC_except_table11844
- GCC_except_table11850
- GCC_except_table11956
- GCC_except_table11975
- GCC_except_table11977
- GCC_except_table11979
- GCC_except_table11981
- GCC_except_table1200
- GCC_except_table12016
- GCC_except_table12065
- GCC_except_table12072
- GCC_except_table12074
- GCC_except_table12076
- GCC_except_table12082
- GCC_except_table12119
- GCC_except_table1216
- GCC_except_table12250
- GCC_except_table12276
- GCC_except_table12288
- GCC_except_table12330
- GCC_except_table12332
- GCC_except_table12345
- GCC_except_table1242
- GCC_except_table12450
- GCC_except_table12454
- GCC_except_table12495
- GCC_except_table12499
- GCC_except_table12508
- GCC_except_table12509
- GCC_except_table12516
- GCC_except_table12554
- GCC_except_table12561
- GCC_except_table12573
- GCC_except_table12578
- GCC_except_table12628
- GCC_except_table12720
- GCC_except_table12723
- GCC_except_table12729
- GCC_except_table12731
- GCC_except_table12771
- GCC_except_table12790
- GCC_except_table12801
- GCC_except_table12859
- GCC_except_table12862
- GCC_except_table12870
- GCC_except_table12876
- GCC_except_table12878
- GCC_except_table12942
- GCC_except_table13020
- GCC_except_table13024
- GCC_except_table13028
- GCC_except_table13089
- GCC_except_table13096
- GCC_except_table13235
- GCC_except_table13247
- GCC_except_table13339
- GCC_except_table1334
- GCC_except_table13406
- GCC_except_table1351
- GCC_except_table13612
- GCC_except_table13690
- GCC_except_table13732
- GCC_except_table13781
- GCC_except_table13791
- GCC_except_table13811
- GCC_except_table13826
- GCC_except_table13854
- GCC_except_table13856
- GCC_except_table13869
- GCC_except_table13871
- GCC_except_table13873
- GCC_except_table13892
- GCC_except_table14038
- GCC_except_table14049
- GCC_except_table14076
- GCC_except_table14082
- GCC_except_table14098
- GCC_except_table14168
- GCC_except_table14170
- GCC_except_table14216
- GCC_except_table14218
- GCC_except_table14242
- GCC_except_table14245
- GCC_except_table14399
- GCC_except_table1440
- GCC_except_table1532
- GCC_except_table1557
- GCC_except_table1603
- GCC_except_table1678
- GCC_except_table1776
- GCC_except_table1877
- GCC_except_table1881
- GCC_except_table1901
- GCC_except_table1906
- GCC_except_table1910
- GCC_except_table1920
- GCC_except_table2107
- GCC_except_table2111
- GCC_except_table2113
- GCC_except_table2115
- GCC_except_table2117
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2131
- GCC_except_table2133
- GCC_except_table2147
- GCC_except_table2179
- GCC_except_table2181
- GCC_except_table2183
- GCC_except_table2185
- GCC_except_table2187
- GCC_except_table2189
- GCC_except_table2191
- GCC_except_table2193
- GCC_except_table2195
- GCC_except_table2197
- GCC_except_table2199
- GCC_except_table2201
- GCC_except_table2203
- GCC_except_table2205
- GCC_except_table2207
- GCC_except_table2209
- GCC_except_table2228
- GCC_except_table2230
- GCC_except_table2232
- GCC_except_table2260
- GCC_except_table2262
- GCC_except_table2265
- GCC_except_table2268
- GCC_except_table2372
- GCC_except_table2377
- GCC_except_table2385
- GCC_except_table2395
- GCC_except_table2433
- GCC_except_table2604
- GCC_except_table2617
- GCC_except_table2645
- GCC_except_table2660
- GCC_except_table2679
- GCC_except_table2689
- GCC_except_table2726
- GCC_except_table2731
- GCC_except_table2793
- GCC_except_table2896
- GCC_except_table2909
- GCC_except_table2915
- GCC_except_table2923
- GCC_except_table2955
- GCC_except_table3031
- GCC_except_table3036
- GCC_except_table3041
- GCC_except_table3044
- GCC_except_table3054
- GCC_except_table3067
- GCC_except_table3074
- GCC_except_table3201
- GCC_except_table3205
- GCC_except_table3208
- GCC_except_table3275
- GCC_except_table3283
- GCC_except_table3318
- GCC_except_table3322
- GCC_except_table3327
- GCC_except_table3457
- GCC_except_table3490
- GCC_except_table3496
- GCC_except_table3499
- GCC_except_table3509
- GCC_except_table3513
- GCC_except_table3519
- GCC_except_table3522
- GCC_except_table3526
- GCC_except_table3546
- GCC_except_table3558
- GCC_except_table3574
- GCC_except_table3583
- GCC_except_table3680
- GCC_except_table3686
- GCC_except_table3707
- GCC_except_table3709
- GCC_except_table3711
- GCC_except_table3758
- GCC_except_table3786
- GCC_except_table3817
- GCC_except_table3819
- GCC_except_table3837
- GCC_except_table3839
- GCC_except_table3842
- GCC_except_table4005
- GCC_except_table4039
- GCC_except_table4047
- GCC_except_table4049
- GCC_except_table4064
- GCC_except_table4067
- GCC_except_table4069
- GCC_except_table4102
- GCC_except_table4107
- GCC_except_table4108
- GCC_except_table4362
- GCC_except_table4368
- GCC_except_table4396
- GCC_except_table4419
- GCC_except_table4421
- GCC_except_table4426
- GCC_except_table4442
- GCC_except_table4446
- GCC_except_table4464
- GCC_except_table4531
- GCC_except_table4856
- GCC_except_table4866
- GCC_except_table4925
- GCC_except_table4927
- GCC_except_table4931
- GCC_except_table4933
- GCC_except_table4936
- GCC_except_table5006
- GCC_except_table5011
- GCC_except_table5041
- GCC_except_table5171
- GCC_except_table5175
- GCC_except_table5522
- GCC_except_table5553
- GCC_except_table556
- GCC_except_table5599
- GCC_except_table5618
- GCC_except_table5624
- GCC_except_table563
- GCC_except_table5630
- GCC_except_table5642
- GCC_except_table5644
- GCC_except_table565
- GCC_except_table5670
- GCC_except_table5675
- GCC_except_table5678
- GCC_except_table5680
- GCC_except_table5686
- GCC_except_table5694
- GCC_except_table5698
- GCC_except_table573
- GCC_except_table575
- GCC_except_table5750
- GCC_except_table5783
- GCC_except_table5788
- GCC_except_table5812
- GCC_except_table5816
- GCC_except_table5820
- GCC_except_table5842
- GCC_except_table5848
- GCC_except_table5852
- GCC_except_table5866
- GCC_except_table5869
- GCC_except_table5872
- GCC_except_table5895
- GCC_except_table5935
- GCC_except_table5956
- GCC_except_table5965
- GCC_except_table6004
- GCC_except_table6016
- GCC_except_table6050
- GCC_except_table6053
- GCC_except_table6059
- GCC_except_table6063
- GCC_except_table6075
- GCC_except_table6100
- GCC_except_table6129
- GCC_except_table6156
- GCC_except_table6158
- GCC_except_table6240
- GCC_except_table6317
- GCC_except_table6322
- GCC_except_table6327
- GCC_except_table648
- GCC_except_table6485
- GCC_except_table6488
- GCC_except_table6526
- GCC_except_table6536
- GCC_except_table6539
- GCC_except_table6577
- GCC_except_table6614
- GCC_except_table6616
- GCC_except_table7015
- GCC_except_table7035
- GCC_except_table7048
- GCC_except_table7061
- GCC_except_table7080
- GCC_except_table7110
- GCC_except_table7113
- GCC_except_table7115
- GCC_except_table7117
- GCC_except_table7119
- GCC_except_table7128
- GCC_except_table7175
- GCC_except_table7189
- GCC_except_table719
- GCC_except_table7225
- GCC_except_table7227
- GCC_except_table7266
- GCC_except_table741
- GCC_except_table743
- GCC_except_table747
- GCC_except_table750
- GCC_except_table7519
- GCC_except_table7522
- GCC_except_table7544
- GCC_except_table7551
- GCC_except_table7567
- GCC_except_table7569
- GCC_except_table7570
- GCC_except_table7571
- GCC_except_table7572
- GCC_except_table7573
- GCC_except_table7574
- GCC_except_table7585
- GCC_except_table7744
- GCC_except_table792
- GCC_except_table795
- GCC_except_table796
- GCC_except_table7963
- GCC_except_table797
- GCC_except_table798
- GCC_except_table799
- GCC_except_table8008
- GCC_except_table801
- GCC_except_table8026
- GCC_except_table8027
- GCC_except_table8087
- GCC_except_table8109
- GCC_except_table8113
- GCC_except_table8120
- GCC_except_table8174
- GCC_except_table8374
- GCC_except_table8376
- GCC_except_table8423
- GCC_except_table8463
- GCC_except_table8467
- GCC_except_table8469
- GCC_except_table8471
- GCC_except_table8483
- GCC_except_table8528
- GCC_except_table8556
- GCC_except_table8598
- GCC_except_table8689
- GCC_except_table8747
- GCC_except_table8767
- GCC_except_table8770
- GCC_except_table8789
- GCC_except_table879
- GCC_except_table8848
- GCC_except_table8852
- GCC_except_table8856
- GCC_except_table8857
- GCC_except_table8858
- GCC_except_table8859
- GCC_except_table8860
- GCC_except_table8862
- GCC_except_table8864
- GCC_except_table8868
- GCC_except_table888
- GCC_except_table8882
- GCC_except_table8942
- GCC_except_table9007
- GCC_except_table9164
- GCC_except_table9205
- GCC_except_table9211
- GCC_except_table9214
- GCC_except_table9477
- GCC_except_table9481
- GCC_except_table9485
- GCC_except_table9505
- GCC_except_table9506
- GCC_except_table9602
- GCC_except_table9612
- GCC_except_table9645
- GCC_except_table9697
- GCC_except_table9742
- GCC_except_table9762
- GCC_except_table9788
- GCC_except_table980
- GCC_except_table9816
- GCC_except_table9849
- GCC_except_table9851
- GCC_except_table9942
- _OBJC_IVAR_$_PHAssetExtendedMetadata._originalFileName
- _OBJC_IVAR_$_PHAssetResource._originalFilename
- ___121-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:progressContainer:reply:]_block_invoke
- ___135+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke
- ___135+[PHSearchQueryManager _performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:]_block_invoke_2
- ___197-[PHShareAssetChangeRequestHelper addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:]_block_invoke
- ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke
- ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke_2
- ___83-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:reply:]_block_invoke
- ___block_descriptor_80_e8_32s40r48r56r64r72r_e56_v48?0"NSArray"8"NSArray"16"NSArray"24Q32"NSError"40lr40l8r48l8r56l8r64l8r72l8s32l8
- _objc_msgSend$_clientForAccessLevel:
- _objc_msgSend$_performIntentSearchForLibrary:searchText:searchOptions:maximumSearchResults:allowUnattributedQuery:completion:
- _objc_msgSend$_sendChangesRequest:onExecutionContext:withInstrumentation:reply:
- _objc_msgSend$addAssetsToCPLShare:creationOptionsPerAsset:withMomentSharePreview:withBatchCommentText:outKeyAssetIdentifier:outContainsEPPAssets:outCreatedSharePostPlaceholder:
- _objc_msgSend$flattenLivePhotoToStillIfNeeded
- _objc_msgSend$initWithQueue:priority:
- _objc_msgSend$spotlightTextLinesFromDocumentObservation:
- _sharedLazyPhotoLibraryForCMM.pl_once_object_44
- _sharedLazyPhotoLibraryForCMM.pl_once_token_44
CStrings:
+ "<%@: %p; preventsExpensiveNetworkAccess: %d>"
+ "B16@?0@\"PHSearchResult\"8"
+ "Excluding bundle from intent search: %@"
+ "Failed to archive search intents query, error: %@"
+ "PHPhotosErrorShareTypeRequiresOSUpgrade"
+ "PHPhotosErrorShareTypeUnsupported"
+ "PhotoKit XPC proxy is invalid. Retries left: %zd"
+ "Share %{public}@ skipping PHSharePost creation (skipSharePost); assets will be folded into an existing post"
+ "kTCCServiceSiriAccess"
+ "self.isClientEntitled"
+ "setUploadJobExtensionOptions called without authorization (status: %ld)"
+ "uploadJobExtensionOptions called without authorization (status: %ld)"
+ "v24@?0@\"NSArray\"8@\"PHSearchIntentQUToken\"16"
- "PhotoKit XPC proxy is invalid. Retry attempt: %zd"
```
