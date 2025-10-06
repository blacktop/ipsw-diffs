## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-810.40.105.0.0
-  __TEXT.__text: 0x28de54
-  __TEXT.__auth_stubs: 0x2ba0
-  __TEXT.__objc_methlist: 0x241dc
-  __TEXT.__const: 0x11b0
+810.46.103.0.0
+  __TEXT.__text: 0x28fbc8
+  __TEXT.__auth_stubs: 0x2bb0
+  __TEXT.__objc_methlist: 0x24364
+  __TEXT.__const: 0x1168
   __TEXT.__dlopen_cstrs: 0x239
-  __TEXT.__swift5_typeref: 0x35e
-  __TEXT.__swift5_reflstr: 0xd1
+  __TEXT.__swift5_typeref: 0x31c
+  __TEXT.__swift5_reflstr: 0xf1
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__constg_swiftt: 0x38c
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_fieldmd: 0xf8
-  __TEXT.__cstring: 0x2bcb9
+  __TEXT.__constg_swiftt: 0x360
+  __TEXT.__swift5_fieldmd: 0x11c
+  __TEXT.__cstring: 0x2be3f
   __TEXT.__swift5_capture: 0xac
-  __TEXT.__oslogstring: 0x1c84d
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x40
+  __TEXT.__oslogstring: 0x1c9d1
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x24
-  __TEXT.__gcc_except_tab: 0x98c4
+  __TEXT.__gcc_except_tab: 0x9990
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x85a0
+  __TEXT.__unwind_info: 0x8620
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x375b
-  __TEXT.__objc_methname: 0x6b8e6
-  __TEXT.__objc_methtype: 0x6d3b
-  __TEXT.__objc_stubs: 0x39d40
-  __DATA_CONST.__got: 0x2738
-  __DATA_CONST.__const: 0x7f20
+  __TEXT.__objc_classname: 0x3766
+  __TEXT.__objc_methname: 0x6beb6
+  __TEXT.__objc_methtype: 0x6d56
+  __TEXT.__objc_stubs: 0x39fa0
+  __DATA_CONST.__got: 0x2718
+  __DATA_CONST.__const: 0x7fc8
   __DATA_CONST.__objc_classlist: 0xdc0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13008
+  __DATA_CONST.__objc_selrefs: 0x130b8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xb48
-  __DATA_CONST.__objc_arraydata: 0x980
-  __AUTH_CONST.__auth_got: 0x15e0
-  __AUTH_CONST.__const: 0x3d78
-  __AUTH_CONST.__cfstring: 0x28500
-  __AUTH_CONST.__objc_const: 0x3d4e8
-  __AUTH_CONST.__objc_intobj: 0x2088
-  __AUTH_CONST.__objc_arrayobj: 0x708
+  __DATA_CONST.__objc_arraydata: 0x978
+  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__const: 0x3e68
+  __AUTH_CONST.__cfstring: 0x286c0
+  __AUTH_CONST.__objc_const: 0x3d6f0
+  __AUTH_CONST.__objc_intobj: 0x2070
+  __AUTH_CONST.__objc_arrayobj: 0x6f0
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x6f60
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x3250
+  __DATA.__objc_ivar: 0x3274
   __DATA.__data: 0x29a0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x18b0
+  __DATA.__bss: 0x1830
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0x1a38
   __DATA_DIRTY.__data: 0x148

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F085DCD-CB8C-3DDF-B203-FC6AE9BA6025
-  Functions: 13546
-  Symbols:   45295
-  CStrings:  29022
+  UUID: 08A68BFC-D177-305D-8ECE-5D96F76AF291
+  Functions: 13590
+  Symbols:   45409
+  CStrings:  29092
 
Symbols:
+ +[PHAssetResourceUploadJob fetchJobsWithAction:options:]
+ +[PHAssetResourceUploadJob jobLimit]
+ +[PHAssetResourceUploadJobChangeRequest _countOfCancellableAcknowledgeableJobsWithConfiguration:library:error:]
+ +[PHAssetResourceUploadJobChangeRequest createJobWithDestination:resource:]
+ +[PHAssetResourceUploadJobChangeRequest creationRequestForAssetResourceUploadJobWithDestination:resource:]
+ +[PHAssetResourceUploadJobConfigurationChangeRequest changeRequestForConfiguration:]
+ +[PHQuery queryForInFlightJobCountWithConfiguration:options:]
+ +[PHQueryPersonContext fetchOptionsWithOverriddenChangeDetectionCriteriaIfNecessary:]
+ +[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photoLibrary:]
+ +[PHSearchQueryOptions queryOptionsForSyndicationLibraryWithOptions:]
+ +[PHSearchResult supportsSecureCoding]
+ +[PHSearchUtility isSyndicationLibrary:]
+ +[PHSearchUtility photosBundleIdentifier]
+ +[PHSearchUtility syndicationLibraryBundleIdentifiers]
+ -[PHAssetResourceUploadJob destination]
+ -[PHAssetResourceUploadJobChangeRequest acknowledge]
+ -[PHAssetResourceUploadJobChangeRequest retryWithDestination:]
+ -[PHFeatureAvailabilityReadOptions setValidateSpotlightAvailability:]
+ -[PHFeatureAvailabilityReadOptions validateSpotlightAvailability]
+ -[PHMediaProcessingAlgorithmVersionProvider description]
+ -[PHMediaProcessingAlgorithmVersionProvider initWithSceneAnalysisVersion:faceAnalysisVersion:characterRecognitionAlgorithmVersion:visualSearchAlgorithmVersion:stickerConfidenceAlgorithmVersion:vaAnalysisVersion:vaLocationAnalysisVersion:mediaAnalysisVersion:mediaAnalysisImageVersion:captionGenerationVersion:imageEmbeddingVersion:videoEmbeddingVersion:videoSensitivityAnalysisVersion:textUnderstandingAlgorithmVersion:textUnderstandingGatingVersion:]
+ -[PHMediaProcessingAlgorithmVersionProvider setTextUnderstandingAlgorithmVersion:]
+ -[PHMediaProcessingAlgorithmVersionProvider setTextUnderstandingGatingVersion:]
+ -[PHMediaProcessingAlgorithmVersionProvider textUnderstandingAlgorithmVersion]
+ -[PHMediaProcessingAlgorithmVersionProvider textUnderstandingGatingVersion]
+ -[PHPhotoLibrary _errorCodeForAuthorizationStatus:accessLevel:]
+ -[PHPhotoLibrary isUploadJobExtensionEnabled]
+ -[PHPhotoLibrary setUploadJobExtensionEnabled:error:]
+ -[PHPhotoLibrary(FeatureAvailability) _validateSpotlightAvailabilityInFeatureAvailability:forFeature:completionHandler:]
+ -[PHPhotoLibrary(FeatureAvailability) featureAvailabilityForFeature:readOptions:completionHandler:]
+ -[PHPhotoLibraryFeatureAvailabilityReporter initWithPhotoLibrary:readOptions:]
+ -[PHSearchIndex _spotlightIndexStateForLibraryWithCompletionHandler:]
+ -[PHSearchIndex acquireSpotlightSandboxExtensionIfNeeded]
+ -[PHSearchIndex validateSpotlightIndexForLibraryExistsWithCompletionHandler:]
+ -[PHSearchQueryOptions bundleIdentifiers]
+ -[PHSearchQueryOptions filterQueries]
+ -[PHSearchQueryOptions setBundleIdentifiers:]
+ -[PHSearchQueryOptions setFilterQueries:]
+ -[PHSearchResult bundleIdentifier]
+ -[PHSearchResult encodeWithCoder:]
+ -[PHSearchResult initWithCoder:]
+ -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:bundleIdentifier:]
+ -[PHSearchResult isSyndicationAsset]
+ -[PHSearchResultProcessor _finalizePhotosResultsForQuery:resultHandler:]
+ -[PHSearchResultProcessor _finalizeSyndicationResultsForQuery:resultHandler:]
+ -[PHSearchResultProcessor _isSyndicationLibrary]
+ -[PHSearchResultProcessor _processSearchableItemForPhotosLibrary:]
+ -[PHSearchResultProcessor _processSearchableItemForSyndicationLibrary:]
+ GCC_except_table10006
+ GCC_except_table10007
+ GCC_except_table10008
+ GCC_except_table10009
+ GCC_except_table10020
+ GCC_except_table10040
+ GCC_except_table10041
+ GCC_except_table10042
+ GCC_except_table10043
+ GCC_except_table10044
+ GCC_except_table10045
+ GCC_except_table10046
+ GCC_except_table10047
+ GCC_except_table10048
+ GCC_except_table10049
+ GCC_except_table10085
+ GCC_except_table10086
+ GCC_except_table10090
+ GCC_except_table10109
+ GCC_except_table10114
+ GCC_except_table10184
+ GCC_except_table10277
+ GCC_except_table10420
+ GCC_except_table10457
+ GCC_except_table1052
+ GCC_except_table10547
+ GCC_except_table10575
+ GCC_except_table1068
+ GCC_except_table1096
+ GCC_except_table11073
+ GCC_except_table11228
+ GCC_except_table11231
+ GCC_except_table11237
+ GCC_except_table11243
+ GCC_except_table11247
+ GCC_except_table11253
+ GCC_except_table11359
+ GCC_except_table11378
+ GCC_except_table11380
+ GCC_except_table11384
+ GCC_except_table11419
+ GCC_except_table11466
+ GCC_except_table11473
+ GCC_except_table11475
+ GCC_except_table11477
+ GCC_except_table11520
+ GCC_except_table11666
+ GCC_except_table11678
+ GCC_except_table11720
+ GCC_except_table11722
+ GCC_except_table11735
+ GCC_except_table11834
+ GCC_except_table11838
+ GCC_except_table11877
+ GCC_except_table1188
+ GCC_except_table11881
+ GCC_except_table11890
+ GCC_except_table11891
+ GCC_except_table11935
+ GCC_except_table11942
+ GCC_except_table11986
+ GCC_except_table1205
+ GCC_except_table12070
+ GCC_except_table12073
+ GCC_except_table12079
+ GCC_except_table12081
+ GCC_except_table12121
+ GCC_except_table12140
+ GCC_except_table12149
+ GCC_except_table12205
+ GCC_except_table12207
+ GCC_except_table12267
+ GCC_except_table12411
+ GCC_except_table12415
+ GCC_except_table12456
+ GCC_except_table12480
+ GCC_except_table12487
+ GCC_except_table12695
+ GCC_except_table12937
+ GCC_except_table13015
+ GCC_except_table13060
+ GCC_except_table13107
+ GCC_except_table13117
+ GCC_except_table13135
+ GCC_except_table13150
+ GCC_except_table13179
+ GCC_except_table13192
+ GCC_except_table13194
+ GCC_except_table13196
+ GCC_except_table13215
+ GCC_except_table13297
+ GCC_except_table13303
+ GCC_except_table13319
+ GCC_except_table1366
+ GCC_except_table1385
+ GCC_except_table1409
+ GCC_except_table1448
+ GCC_except_table1497
+ GCC_except_table1685
+ GCC_except_table1689
+ GCC_except_table1703
+ GCC_except_table1707
+ GCC_except_table1717
+ GCC_except_table1903
+ GCC_except_table1909
+ GCC_except_table1911
+ GCC_except_table1913
+ GCC_except_table1915
+ GCC_except_table1917
+ GCC_except_table1920
+ GCC_except_table1927
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1943
+ GCC_except_table1975
+ GCC_except_table1977
+ GCC_except_table1979
+ GCC_except_table1981
+ GCC_except_table1983
+ GCC_except_table1985
+ GCC_except_table1987
+ GCC_except_table1989
+ GCC_except_table1991
+ GCC_except_table1993
+ GCC_except_table2005
+ GCC_except_table2010
+ GCC_except_table2012
+ GCC_except_table2014
+ GCC_except_table2016
+ GCC_except_table2019
+ GCC_except_table2021
+ GCC_except_table2024
+ GCC_except_table2026
+ GCC_except_table2028
+ GCC_except_table2056
+ GCC_except_table2058
+ GCC_except_table2061
+ GCC_except_table2064
+ GCC_except_table2175
+ GCC_except_table2183
+ GCC_except_table2193
+ GCC_except_table2233
+ GCC_except_table2397
+ GCC_except_table2408
+ GCC_except_table2430
+ GCC_except_table2445
+ GCC_except_table2464
+ GCC_except_table2474
+ GCC_except_table2510
+ GCC_except_table2515
+ GCC_except_table2576
+ GCC_except_table2685
+ GCC_except_table2687
+ GCC_except_table2721
+ GCC_except_table2795
+ GCC_except_table2800
+ GCC_except_table2805
+ GCC_except_table2808
+ GCC_except_table2829
+ GCC_except_table2831
+ GCC_except_table2834
+ GCC_except_table2965
+ GCC_except_table2969
+ GCC_except_table2972
+ GCC_except_table3039
+ GCC_except_table3047
+ GCC_except_table3076
+ GCC_except_table3080
+ GCC_except_table3085
+ GCC_except_table3201
+ GCC_except_table3234
+ GCC_except_table3240
+ GCC_except_table3243
+ GCC_except_table3253
+ GCC_except_table3257
+ GCC_except_table3266
+ GCC_except_table3270
+ GCC_except_table3285
+ GCC_except_table3301
+ GCC_except_table3302
+ GCC_except_table3318
+ GCC_except_table3327
+ GCC_except_table3424
+ GCC_except_table3430
+ GCC_except_table3446
+ GCC_except_table3448
+ GCC_except_table3450
+ GCC_except_table3497
+ GCC_except_table3524
+ GCC_except_table3555
+ GCC_except_table3557
+ GCC_except_table3575
+ GCC_except_table3577
+ GCC_except_table3580
+ GCC_except_table3791
+ GCC_except_table3793
+ GCC_except_table3820
+ GCC_except_table3854
+ GCC_except_table3862
+ GCC_except_table3879
+ GCC_except_table3882
+ GCC_except_table3884
+ GCC_except_table3916
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table4184
+ GCC_except_table4190
+ GCC_except_table4217
+ GCC_except_table4240
+ GCC_except_table4242
+ GCC_except_table4246
+ GCC_except_table4262
+ GCC_except_table4266
+ GCC_except_table4279
+ GCC_except_table4345
+ GCC_except_table4662
+ GCC_except_table4664
+ GCC_except_table4671
+ GCC_except_table471
+ GCC_except_table4735
+ GCC_except_table4737
+ GCC_except_table4741
+ GCC_except_table4743
+ GCC_except_table4746
+ GCC_except_table478
+ GCC_except_table480
+ GCC_except_table4815
+ GCC_except_table4820
+ GCC_except_table4850
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table4997
+ GCC_except_table5354
+ GCC_except_table5403
+ GCC_except_table5421
+ GCC_except_table5427
+ GCC_except_table5433
+ GCC_except_table5446
+ GCC_except_table5448
+ GCC_except_table5474
+ GCC_except_table5476
+ GCC_except_table5479
+ GCC_except_table5480
+ GCC_except_table5485
+ GCC_except_table5493
+ GCC_except_table5497
+ GCC_except_table5506
+ GCC_except_table5510
+ GCC_except_table5547
+ GCC_except_table5555
+ GCC_except_table5585
+ GCC_except_table5611
+ GCC_except_table5615
+ GCC_except_table5619
+ GCC_except_table5639
+ GCC_except_table564
+ GCC_except_table5645
+ GCC_except_table5649
+ GCC_except_table5663
+ GCC_except_table5666
+ GCC_except_table5669
+ GCC_except_table5690
+ GCC_except_table5737
+ GCC_except_table5746
+ GCC_except_table5793
+ GCC_except_table5824
+ GCC_except_table5827
+ GCC_except_table5833
+ GCC_except_table5837
+ GCC_except_table5870
+ GCC_except_table5900
+ GCC_except_table5926
+ GCC_except_table5928
+ GCC_except_table5939
+ GCC_except_table5986
+ GCC_except_table6060
+ GCC_except_table6065
+ GCC_except_table6070
+ GCC_except_table6211
+ GCC_except_table6214
+ GCC_except_table6252
+ GCC_except_table6262
+ GCC_except_table6265
+ GCC_except_table628
+ GCC_except_table6302
+ GCC_except_table6340
+ GCC_except_table6342
+ GCC_except_table650
+ GCC_except_table652
+ GCC_except_table659
+ GCC_except_table6729
+ GCC_except_table6742
+ GCC_except_table6755
+ GCC_except_table6772
+ GCC_except_table6801
+ GCC_except_table6804
+ GCC_except_table6806
+ GCC_except_table6808
+ GCC_except_table6810
+ GCC_except_table6818
+ GCC_except_table6861
+ GCC_except_table6874
+ GCC_except_table6907
+ GCC_except_table6909
+ GCC_except_table6948
+ GCC_except_table704
+ GCC_except_table706
+ GCC_except_table708
+ GCC_except_table7208
+ GCC_except_table7212
+ GCC_except_table7213
+ GCC_except_table7227
+ GCC_except_table7234
+ GCC_except_table7250
+ GCC_except_table7252
+ GCC_except_table7253
+ GCC_except_table7254
+ GCC_except_table7255
+ GCC_except_table7256
+ GCC_except_table7257
+ GCC_except_table7266
+ GCC_except_table7267
+ GCC_except_table7268
+ GCC_except_table7425
+ GCC_except_table7643
+ GCC_except_table7669
+ GCC_except_table7688
+ GCC_except_table7690
+ GCC_except_table7691
+ GCC_except_table7752
+ GCC_except_table777
+ GCC_except_table7774
+ GCC_except_table7778
+ GCC_except_table7784
+ GCC_except_table7837
+ GCC_except_table786
+ GCC_except_table7997
+ GCC_except_table7999
+ GCC_except_table8046
+ GCC_except_table8086
+ GCC_except_table8090
+ GCC_except_table8092
+ GCC_except_table8094
+ GCC_except_table8106
+ GCC_except_table8111
+ GCC_except_table8151
+ GCC_except_table8179
+ GCC_except_table8304
+ GCC_except_table8362
+ GCC_except_table8382
+ GCC_except_table8385
+ GCC_except_table8404
+ GCC_except_table8462
+ GCC_except_table8466
+ GCC_except_table8470
+ GCC_except_table8479
+ GCC_except_table8481
+ GCC_except_table8520
+ GCC_except_table8584
+ GCC_except_table874
+ GCC_except_table8741
+ GCC_except_table8782
+ GCC_except_table8787
+ GCC_except_table9032
+ GCC_except_table9036
+ GCC_except_table9040
+ GCC_except_table9060
+ GCC_except_table9061
+ GCC_except_table9155
+ GCC_except_table9165
+ GCC_except_table9197
+ GCC_except_table922
+ GCC_except_table9249
+ GCC_except_table9290
+ GCC_except_table9310
+ GCC_except_table9337
+ GCC_except_table9362
+ GCC_except_table9395
+ GCC_except_table9397
+ GCC_except_table9487
+ GCC_except_table9578
+ GCC_except_table9697
+ GCC_except_table9711
+ GCC_except_table9712
+ GCC_except_table9814
+ GCC_except_table9815
+ GCC_except_table9816
+ GCC_except_table9817
+ GCC_except_table9818
+ GCC_except_table9819
+ GCC_except_table9820
+ GCC_except_table9821
+ GCC_except_table9822
+ GCC_except_table9823
+ GCC_except_table9824
+ GCC_except_table9825
+ GCC_except_table9826
+ GCC_except_table9827
+ GCC_except_table9828
+ GCC_except_table9829
+ GCC_except_table9830
+ GCC_except_table9831
+ GCC_except_table9832
+ GCC_except_table9833
+ GCC_except_table9834
+ GCC_except_table9835
+ GCC_except_table9836
+ GCC_except_table9837
+ GCC_except_table9838
+ GCC_except_table9839
+ GCC_except_table9840
+ GCC_except_table9841
+ GCC_except_table9842
+ GCC_except_table9938
+ GCC_except_table9947
+ GCC_except_table9948
+ GCC_except_table9949
+ GCC_except_table9951
+ GCC_except_table9962
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._destination
+ _OBJC_IVAR_$_PHFeatureAvailabilityReadOptions._validateSpotlightAvailability
+ _OBJC_IVAR_$_PHMediaProcessingAlgorithmVersionProvider._textUnderstandingAlgorithmVersion
+ _OBJC_IVAR_$_PHMediaProcessingAlgorithmVersionProvider._textUnderstandingGatingVersion
+ _OBJC_IVAR_$_PHPhotoLibraryFeatureAvailabilityReporter._readOptions
+ _OBJC_IVAR_$_PHSearchIndex._queryLock
+ _OBJC_IVAR_$_PHSearchIndex._spotlightSandboxExtension
+ _OBJC_IVAR_$_PHSearchQueryOptions._bundleIdentifiers
+ _OBJC_IVAR_$_PHSearchQueryOptions._filterQueries
+ _OBJC_IVAR_$_PHSearchResult._bundleIdentifier
+ _PLNotesBundleID
+ _PLSearchBackendDonationsGetLog
+ _PLSyndicationAllEquivalentFileProviderLocalAndCloudBundleIDs
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19231
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22476
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36593
+ __OBJC_$_CLASS_METHODS_PHSearchQueryOptions
+ __OBJC_$_CLASS_PROP_LIST_PHAssetResourceUploadJob
+ __OBJC_$_CLASS_PROP_LIST_PHSearchResult
+ __OBJC_CLASS_PROTOCOLS_$_PHSearchResult
+ __PROTOCOLS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration.5
+ ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.495
+ ___109-[PHSearchQueryManager suggestionsForSearchQuery:rangeOfSuggestionText:searchQueryResult:suggestionsHandler:]_block_invoke.114
+ ___109-[PHSearchQueryManager suggestionsForSearchQuery:rangeOfSuggestionText:searchQueryResult:suggestionsHandler:]_block_invoke.115
+ ___110+[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photoLibrary:]_block_invoke
+ ___110+[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photoLibrary:]_block_invoke_2
+ ___111+[PHAssetResourceUploadJobChangeRequest _countOfCancellableAcknowledgeableJobsWithConfiguration:library:error:]_block_invoke
+ ___120-[PHPhotoLibrary(FeatureAvailability) _validateSpotlightAvailabilityInFeatureAvailability:forFeature:completionHandler:]_block_invoke
+ ___24-[PHSearchIndex dealloc]_block_invoke
+ ___34-[PHPhotoLibrary postOpenProgress]_block_invoke.428
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke.445
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_2.446
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_3.447
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_4.448
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_5.450
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_6.451
+ ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_7.456
+ ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke
+ ___53-[PHPhotoLibrary setUploadJobExtensionEnabled:error:]_block_invoke_2
+ ___55-[PHPhotoLibrary _processPendingChangesWithDebugEvent:]_block_invoke.699
+ ___55-[PHPhotoLibrary openAndWaitWithUpgrade:options:error:]_block_invoke.414
+ ___55-[PHPhotoLibrary openAndWaitWithUpgrade:options:error:]_block_invoke_2.417
+ ___57-[PHSearchIndex acquireSpotlightSandboxExtensionIfNeeded]_block_invoke
+ ___62-[PHImageManager requestStreamForVideo:options:resultHandler:]_block_invoke.694
+ ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.742
+ ___64-[PHPhotoLibrary _onQueueNotifyAvailabilityObserversWithReason:]_block_invoke.485
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.683
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.690
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.688
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.692
+ ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.689
+ ___66-[PHSearchResultProcessor _processSearchableItemForPhotosLibrary:]_block_invoke
+ ___66-[PHSearchResultProcessor _processSearchableItemForPhotosLibrary:]_block_invoke_2
+ ___66-[PHSearchResultProcessor _processSearchableItemForPhotosLibrary:]_block_invoke_3
+ ___67-[PHSearchQueryManager performSearch:searchOptions:resultsHandler:]_block_invoke.73
+ ___67-[PHSearchQueryManager performSearch:searchOptions:resultsHandler:]_block_invoke.74
+ ___69-[PHSearchIndex _spotlightIndexStateForLibraryWithCompletionHandler:]_block_invoke
+ ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.81
+ ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.86
+ ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.87
+ ___76-[PHSearchQueryManager suggestionsForSearchText:options:suggestionsHandler:]_block_invoke.118
+ ___77-[PHSearchIndex validateSpotlightIndexForLibraryExistsWithCompletionHandler:]_block_invoke
+ ___84+[PHSearchUtility insertSpacingIfNeededBetweenAnnotationsAndPlainTextInQueryString:]_block_invoke.133
+ ___86-[PHPhotoLibraryFeatureAvailabilityReporter availabilityForFeature:completionHandler:]_block_invoke
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.659
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.663
+ ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.668
+ ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.716
+ ___99-[PHPhotoLibrary(FeatureAvailability) featureAvailabilityForFeature:readOptions:completionHandler:]_block_invoke
+ ___99-[PHPhotoLibrary(FeatureAvailability) featureAvailabilityForFeature:readOptions:completionHandler:]_block_invoke.35
+ ___99-[PHPhotoLibrary(FeatureAvailability) featureAvailabilityForFeature:readOptions:completionHandler:]_block_invoke_2
+ ___Block_byref_object_copy_.10396
+ ___Block_byref_object_copy_.11141
+ ___Block_byref_object_copy_.11415
+ ___Block_byref_object_copy_.11574
+ ___Block_byref_object_copy_.12418
+ ___Block_byref_object_copy_.12678
+ ___Block_byref_object_copy_.13141
+ ___Block_byref_object_copy_.13608
+ ___Block_byref_object_copy_.1422
+ ___Block_byref_object_copy_.14820
+ ___Block_byref_object_copy_.1494
+ ___Block_byref_object_copy_.15593
+ ___Block_byref_object_copy_.17558
+ ___Block_byref_object_copy_.18537
+ ___Block_byref_object_copy_.1949
+ ___Block_byref_object_copy_.20173
+ ___Block_byref_object_copy_.20339
+ ___Block_byref_object_copy_.20661
+ ___Block_byref_object_copy_.21130
+ ___Block_byref_object_copy_.21740
+ ___Block_byref_object_copy_.22287
+ ___Block_byref_object_copy_.22483
+ ___Block_byref_object_copy_.2350
+ ___Block_byref_object_copy_.24321
+ ___Block_byref_object_copy_.25197
+ ___Block_byref_object_copy_.26881
+ ___Block_byref_object_copy_.27405
+ ___Block_byref_object_copy_.28132
+ ___Block_byref_object_copy_.28419
+ ___Block_byref_object_copy_.2842
+ ___Block_byref_object_copy_.29938
+ ___Block_byref_object_copy_.30905
+ ___Block_byref_object_copy_.31650
+ ___Block_byref_object_copy_.31944
+ ___Block_byref_object_copy_.33325
+ ___Block_byref_object_copy_.3360
+ ___Block_byref_object_copy_.33903
+ ___Block_byref_object_copy_.34466
+ ___Block_byref_object_copy_.34656
+ ___Block_byref_object_copy_.35095
+ ___Block_byref_object_copy_.35674
+ ___Block_byref_object_copy_.35951
+ ___Block_byref_object_copy_.36884
+ ___Block_byref_object_copy_.37339
+ ___Block_byref_object_copy_.38966
+ ___Block_byref_object_copy_.3951
+ ___Block_byref_object_copy_.39523
+ ___Block_byref_object_copy_.43598
+ ___Block_byref_object_copy_.44022
+ ___Block_byref_object_copy_.44233
+ ___Block_byref_object_copy_.44462
+ ___Block_byref_object_copy_.45806
+ ___Block_byref_object_copy_.46214
+ ___Block_byref_object_copy_.46732
+ ___Block_byref_object_copy_.47034
+ ___Block_byref_object_copy_.47409
+ ___Block_byref_object_copy_.47896
+ ___Block_byref_object_copy_.48400
+ ___Block_byref_object_copy_.49278
+ ___Block_byref_object_copy_.49476
+ ___Block_byref_object_copy_.49686
+ ___Block_byref_object_copy_.49723
+ ___Block_byref_object_copy_.51889
+ ___Block_byref_object_copy_.52188
+ ___Block_byref_object_copy_.52922
+ ___Block_byref_object_copy_.53724
+ ___Block_byref_object_copy_.5518
+ ___Block_byref_object_copy_.6581
+ ___Block_byref_object_copy_.7051
+ ___Block_byref_object_copy_.8518
+ ___Block_byref_object_copy_.8841
+ ___Block_byref_object_copy_.904
+ ___Block_byref_object_copy_.9135
+ ___Block_byref_object_copy_.9698
+ ___Block_byref_object_dispose_.10397
+ ___Block_byref_object_dispose_.11142
+ ___Block_byref_object_dispose_.11416
+ ___Block_byref_object_dispose_.11575
+ ___Block_byref_object_dispose_.12419
+ ___Block_byref_object_dispose_.12679
+ ___Block_byref_object_dispose_.13142
+ ___Block_byref_object_dispose_.13609
+ ___Block_byref_object_dispose_.1423
+ ___Block_byref_object_dispose_.14821
+ ___Block_byref_object_dispose_.1495
+ ___Block_byref_object_dispose_.15594
+ ___Block_byref_object_dispose_.17559
+ ___Block_byref_object_dispose_.18538
+ ___Block_byref_object_dispose_.1950
+ ___Block_byref_object_dispose_.20174
+ ___Block_byref_object_dispose_.20340
+ ___Block_byref_object_dispose_.20662
+ ___Block_byref_object_dispose_.21131
+ ___Block_byref_object_dispose_.21741
+ ___Block_byref_object_dispose_.22288
+ ___Block_byref_object_dispose_.22484
+ ___Block_byref_object_dispose_.2351
+ ___Block_byref_object_dispose_.24322
+ ___Block_byref_object_dispose_.25198
+ ___Block_byref_object_dispose_.26882
+ ___Block_byref_object_dispose_.27406
+ ___Block_byref_object_dispose_.28133
+ ___Block_byref_object_dispose_.28420
+ ___Block_byref_object_dispose_.2843
+ ___Block_byref_object_dispose_.29939
+ ___Block_byref_object_dispose_.30906
+ ___Block_byref_object_dispose_.31651
+ ___Block_byref_object_dispose_.31945
+ ___Block_byref_object_dispose_.33326
+ ___Block_byref_object_dispose_.3361
+ ___Block_byref_object_dispose_.33904
+ ___Block_byref_object_dispose_.34467
+ ___Block_byref_object_dispose_.34657
+ ___Block_byref_object_dispose_.35096
+ ___Block_byref_object_dispose_.35675
+ ___Block_byref_object_dispose_.35952
+ ___Block_byref_object_dispose_.36885
+ ___Block_byref_object_dispose_.37340
+ ___Block_byref_object_dispose_.38967
+ ___Block_byref_object_dispose_.3952
+ ___Block_byref_object_dispose_.39524
+ ___Block_byref_object_dispose_.43599
+ ___Block_byref_object_dispose_.44023
+ ___Block_byref_object_dispose_.44234
+ ___Block_byref_object_dispose_.44463
+ ___Block_byref_object_dispose_.45807
+ ___Block_byref_object_dispose_.46215
+ ___Block_byref_object_dispose_.46733
+ ___Block_byref_object_dispose_.47035
+ ___Block_byref_object_dispose_.47410
+ ___Block_byref_object_dispose_.47897
+ ___Block_byref_object_dispose_.48401
+ ___Block_byref_object_dispose_.49279
+ ___Block_byref_object_dispose_.49477
+ ___Block_byref_object_dispose_.49687
+ ___Block_byref_object_dispose_.49724
+ ___Block_byref_object_dispose_.51890
+ ___Block_byref_object_dispose_.52189
+ ___Block_byref_object_dispose_.52923
+ ___Block_byref_object_dispose_.53725
+ ___Block_byref_object_dispose_.5519
+ ___Block_byref_object_dispose_.6582
+ ___Block_byref_object_dispose_.7052
+ ___Block_byref_object_dispose_.8519
+ ___Block_byref_object_dispose_.8842
+ ___Block_byref_object_dispose_.905
+ ___Block_byref_object_dispose_.9136
+ ___Block_byref_object_dispose_.9699
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.19232
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.22477
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.36594
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e31_v16?0"PLFeatureAvailability"8ls32l8
+ ___block_descriptor_40_e8_32bs_e43_v24?0"PHFeatureAvailability"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e43_v24?0"PLFeatureAvailability"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32bs48n11_8_8_s0_t8w8_e43_v24?0"PLFeatureAvailability"8"NSError"16l
+ ___block_descriptor_64_e8_32s40bs48n11_8_8_s0_t8w8_e20_v20?0B8"NSError"12l
+ ___block_literal_global.1041.36773
+ ___block_literal_global.10527
+ ___block_literal_global.1057.36772
+ ___block_literal_global.1063.36769
+ ___block_literal_global.1065.36767
+ ___block_literal_global.1099.36765
+ ___block_literal_global.112.41269
+ ___block_literal_global.11236
+ ___block_literal_global.11431
+ ___block_literal_global.11808
+ ___block_literal_global.1240
+ ___block_literal_global.12725
+ ___block_literal_global.134.47956
+ ___block_literal_global.13429
+ ___block_literal_global.13610
+ ___block_literal_global.1369
+ ___block_literal_global.1378
+ ___block_literal_global.1393
+ ___block_literal_global.1403
+ ___block_literal_global.14177
+ ___block_literal_global.1422
+ ___block_literal_global.1442
+ ___block_literal_global.14503
+ ___block_literal_global.146.38934
+ ___block_literal_global.14895
+ ___block_literal_global.15578
+ ___block_literal_global.17140
+ ___block_literal_global.1741
+ ___block_literal_global.1748
+ ___block_literal_global.1752
+ ___block_literal_global.17794
+ ___block_literal_global.182
+ ___block_literal_global.18566
+ ___block_literal_global.18617
+ ___block_literal_global.188
+ ___block_literal_global.1960
+ ___block_literal_global.19777
+ ___block_literal_global.200
+ ___block_literal_global.20091
+ ___block_literal_global.206.28702
+ ___block_literal_global.206.29607
+ ___block_literal_global.20677
+ ___block_literal_global.210.29610
+ ___block_literal_global.21105
+ ___block_literal_global.212.29611
+ ___block_literal_global.216
+ ___block_literal_global.217.13981
+ ___block_literal_global.22079
+ ___block_literal_global.221
+ ___block_literal_global.228.40466
+ ___block_literal_global.22944
+ ___block_literal_global.234.34190
+ ___block_literal_global.2383
+ ___block_literal_global.24230
+ ___block_literal_global.25554
+ ___block_literal_global.26224
+ ___block_literal_global.2629
+ ___block_literal_global.27106
+ ___block_literal_global.27835
+ ___block_literal_global.28109
+ ___block_literal_global.2839
+ ___block_literal_global.28729
+ ___block_literal_global.29000
+ ___block_literal_global.29080
+ ___block_literal_global.29596
+ ___block_literal_global.3.11436
+ ___block_literal_global.3.2838
+ ___block_literal_global.3000
+ ___block_literal_global.30055
+ ___block_literal_global.30436
+ ___block_literal_global.30633
+ ___block_literal_global.30916
+ ___block_literal_global.31333
+ ___block_literal_global.32177
+ ___block_literal_global.32321
+ ___block_literal_global.32794
+ ___block_literal_global.33414
+ ___block_literal_global.34193
+ ___block_literal_global.3437
+ ___block_literal_global.34480
+ ___block_literal_global.34601
+ ___block_literal_global.34753
+ ___block_literal_global.348.19674
+ ___block_literal_global.34937
+ ___block_literal_global.35412
+ ___block_literal_global.3587
+ ___block_literal_global.35956
+ ___block_literal_global.36460
+ ___block_literal_global.37.32223
+ ___block_literal_global.37.47528
+ ___block_literal_global.37205
+ ___block_literal_global.37400
+ ___block_literal_global.37946
+ ___block_literal_global.38253
+ ___block_literal_global.387
+ ___block_literal_global.39009
+ ___block_literal_global.39267
+ ___block_literal_global.39696
+ ___block_literal_global.40280
+ ___block_literal_global.40482
+ ___block_literal_global.40967
+ ___block_literal_global.41275
+ ___block_literal_global.426
+ ___block_literal_global.42605
+ ___block_literal_global.4286
+ ___block_literal_global.43188
+ ___block_literal_global.4325
+ ___block_literal_global.43601
+ ___block_literal_global.44288
+ ___block_literal_global.44479
+ ___block_literal_global.45101
+ ___block_literal_global.45891
+ ___block_literal_global.46246
+ ___block_literal_global.46563
+ ___block_literal_global.46654
+ ___block_literal_global.4681
+ ___block_literal_global.470
+ ___block_literal_global.47317
+ ___block_literal_global.474
+ ___block_literal_global.47535
+ ___block_literal_global.4773
+ ___block_literal_global.47975
+ ___block_literal_global.48123
+ ___block_literal_global.4847
+ ___block_literal_global.48891
+ ___block_literal_global.49243
+ ___block_literal_global.49688
+ ___block_literal_global.497
+ ___block_literal_global.49736
+ ___block_literal_global.50.26192
+ ___block_literal_global.50045
+ ___block_literal_global.503
+ ___block_literal_global.50318
+ ___block_literal_global.51631
+ ___block_literal_global.53010
+ ___block_literal_global.53578
+ ___block_literal_global.555
+ ___block_literal_global.5551
+ ___block_literal_global.567
+ ___block_literal_global.596
+ ___block_literal_global.62.1420
+ ___block_literal_global.6664
+ ___block_literal_global.675
+ ___block_literal_global.684
+ ___block_literal_global.687
+ ___block_literal_global.689
+ ___block_literal_global.7058
+ ___block_literal_global.7728
+ ___block_literal_global.7951
+ ___block_literal_global.807
+ ___block_literal_global.8122
+ ___block_literal_global.85.53556
+ ___block_literal_global.8833
+ ___block_literal_global.8920
+ ___block_literal_global.9369
+ ___block_literal_global.987
+ ___block_literal_global.99
+ ___getSCSensitivityAnalysisClass_block_invoke.19230
+ ___getSCSensitivityAnalysisClass_block_invoke.22475
+ ___getSCSensitivityAnalysisClass_block_invoke.36592
+ ___swift_memcpy1_1
+ ___unnamed_6
+ __currentTimestampString.s_formatter.47529
+ __currentTimestampString.s_onceToken.47527
+ _allowedEntities.pl_once_object_77
+ _allowedEntities.pl_once_object_78
+ _allowedEntities.pl_once_token_77
+ _allowedEntities.pl_once_token_78
+ _allowedInfoKeys.allowedKeys.1553
+ _allowedInfoKeys.allowedKeys.18819
+ _allowedInfoKeys.allowedKeys.40772
+ _allowedInfoKeys.onceToken.1552
+ _allowedInfoKeys.onceToken.18818
+ _allowedInfoKeys.onceToken.40771
+ _audit_stringSensitiveContentAnalysis.19241
+ _audit_stringSensitiveContentAnalysis.22481
+ _audit_stringSensitiveContentAnalysis.36598
+ _block_copy_helper.10
+ _block_descriptor.12
+ _block_destroy_helper.11
+ _corePropertiesToFetch.array.22947
+ _corePropertiesToFetch.array.28726
+ _corePropertiesToFetch.array.34194
+ _corePropertiesToFetch.onceToken.22946
+ _corePropertiesToFetch.onceToken.28725
+ _corePropertiesToFetch.onceToken.34192
+ _defaultManager.onceToken.51969
+ _entityKeyMap.pl_once_object_15.11217
+ _entityKeyMap.pl_once_object_15.11819
+ _entityKeyMap.pl_once_object_15.1230
+ _entityKeyMap.pl_once_object_15.13423
+ _entityKeyMap.pl_once_object_15.13718
+ _entityKeyMap.pl_once_object_15.1438
+ _entityKeyMap.pl_once_object_15.1854
+ _entityKeyMap.pl_once_object_15.27827
+ _entityKeyMap.pl_once_object_15.29091
+ _entityKeyMap.pl_once_object_15.32785
+ _entityKeyMap.pl_once_object_15.36450
+ _entityKeyMap.pl_once_object_15.40312
+ _entityKeyMap.pl_once_object_15.44502
+ _entityKeyMap.pl_once_object_15.46237
+ _entityKeyMap.pl_once_object_15.46646
+ _entityKeyMap.pl_once_object_15.4673
+ _entityKeyMap.pl_once_object_15.48120
+ _entityKeyMap.pl_once_object_15.50193
+ _entityKeyMap.pl_once_object_15.51112
+ _entityKeyMap.pl_once_object_15.7957
+ _entityKeyMap.pl_once_object_16.34182
+ _entityKeyMap.pl_once_object_16.34591
+ _entityKeyMap.pl_once_object_16.40469
+ _entityKeyMap.pl_once_object_16.4274
+ _entityKeyMap.pl_once_object_16.47305
+ _entityKeyMap.pl_once_object_16.53565
+ _entityKeyMap.pl_once_token_15.11216
+ _entityKeyMap.pl_once_token_15.11818
+ _entityKeyMap.pl_once_token_15.1229
+ _entityKeyMap.pl_once_token_15.13422
+ _entityKeyMap.pl_once_token_15.13717
+ _entityKeyMap.pl_once_token_15.1437
+ _entityKeyMap.pl_once_token_15.1853
+ _entityKeyMap.pl_once_token_15.27826
+ _entityKeyMap.pl_once_token_15.29090
+ _entityKeyMap.pl_once_token_15.32784
+ _entityKeyMap.pl_once_token_15.36449
+ _entityKeyMap.pl_once_token_15.40311
+ _entityKeyMap.pl_once_token_15.44501
+ _entityKeyMap.pl_once_token_15.46236
+ _entityKeyMap.pl_once_token_15.46645
+ _entityKeyMap.pl_once_token_15.4672
+ _entityKeyMap.pl_once_token_15.48119
+ _entityKeyMap.pl_once_token_15.50192
+ _entityKeyMap.pl_once_token_15.51111
+ _entityKeyMap.pl_once_token_15.7956
+ _entityKeyMap.pl_once_token_16.34181
+ _entityKeyMap.pl_once_token_16.34590
+ _entityKeyMap.pl_once_token_16.40468
+ _entityKeyMap.pl_once_token_16.4273
+ _entityKeyMap.pl_once_token_16.47304
+ _entityKeyMap.pl_once_token_16.53564
+ _getSCSensitivityAnalysisClass.19228
+ _getSCSensitivityAnalysisClass.36588
+ _getSCSensitivityAnalysisClass.softClass.19229
+ _getSCSensitivityAnalysisClass.softClass.22474
+ _getSCSensitivityAnalysisClass.softClass.36591
+ _get_witness_table 6Photos35PHBackgroundResourceUploadExtensionRzlAA01_bcdE13Configuration33_418ED0618F5CF054A91C652800E09068LLCyxG0E10Foundation03AppeF0HPyHC.6
+ _identifierPropertiesToFetch.array.35413
+ _identifierPropertiesToFetch.onceToken.35411
+ _objc_msgSend$_countOfCancellableAcknowledgeableJobsWithConfiguration:library:error:
+ _objc_msgSend$_finalizePhotosResultsForQuery:resultHandler:
+ _objc_msgSend$_finalizeSyndicationResultsForQuery:resultHandler:
+ _objc_msgSend$_isSyndicationLibrary
+ _objc_msgSend$_processSearchableItemForPhotosLibrary:
+ _objc_msgSend$_processSearchableItemForSyndicationLibrary:
+ _objc_msgSend$_spotlightIndexStateForLibraryWithCompletionHandler:
+ _objc_msgSend$_validateSpotlightAvailabilityInFeatureAvailability:forFeature:completionHandler:
+ _objc_msgSend$acquireSpotlightSandboxExtensionIfNeeded
+ _objc_msgSend$addAttributeKeyPath:forEntityName:
+ _objc_msgSend$addRelationshipKeyPath:forEntityName:
+ _objc_msgSend$annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photoLibrary:
+ _objc_msgSend$archiveDataForDestination:
+ _objc_msgSend$availabilityFromInvalidatingSearchIndexInFeatureAvailability:
+ _objc_msgSend$bundleID
+ _objc_msgSend$bundleIdentifiers
+ _objc_msgSend$creationRequestForAssetResourceUploadJobConfiguration
+ _objc_msgSend$creationRequestForAssetResourceUploadJobWithDestination:resource:
+ _objc_msgSend$currentTUAlgorithmVersion
+ _objc_msgSend$currentTUGatingVersion
+ _objc_msgSend$deleteAssetResourceUploadJobConfigurations:
+ _objc_msgSend$featureAvailabilityForFeature:readOptions:completionHandler:
+ _objc_msgSend$fetchOptionsWithOverriddenChangeDetectionCriteriaIfNecessary:
+ _objc_msgSend$filterQueries
+ _objc_msgSend$initWithSceneAnalysisVersion:faceAnalysisVersion:characterRecognitionAlgorithmVersion:visualSearchAlgorithmVersion:stickerConfidenceAlgorithmVersion:vaAnalysisVersion:vaLocationAnalysisVersion:mediaAnalysisVersion:mediaAnalysisImageVersion:captionGenerationVersion:imageEmbeddingVersion:videoEmbeddingVersion:videoSensitivityAnalysisVersion:textUnderstandingAlgorithmVersion:textUnderstandingGatingVersion:
+ _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:bundleIdentifier:
+ _objc_msgSend$isBackgroundResourceUploadExtensionClient
+ _objc_msgSend$isSyndicationLibrary:
+ _objc_msgSend$jobLimit
+ _objc_msgSend$queryOptionsForSyndicationLibraryWithOptions:
+ _objc_msgSend$setBundleIdentifiers:
+ _objc_msgSend$setResultsHandlerQueue:
+ _objc_msgSend$setTextUnderstandingAlgorithmVersion:
+ _objc_msgSend$setTextUnderstandingGatingVersion:
+ _objc_msgSend$setValidateSpotlightAvailability:
+ _objc_msgSend$syndicationLibraryBundleIdentifiers
+ _objc_msgSend$textUnderstandingAlgorithmVersion
+ _objc_msgSend$textUnderstandingGatingVersion
+ _objc_msgSend$validateSpotlightAvailability
+ _objc_msgSend$validateSpotlightIndexForLibraryExistsWithCompletionHandler:
+ _propertiesToFetch.pl_once_object_24.33899
+ _propertiesToFetch.pl_once_token_24.33898
+ _propertiesToFetchWithHint:.array.11232
+ _propertiesToFetchWithHint:.array.11826
+ _propertiesToFetchWithHint:.array.13740
+ _propertiesToFetchWithHint:.array.1443
+ _propertiesToFetchWithHint:.array.23434
+ _propertiesToFetchWithHint:.array.27836
+ _propertiesToFetchWithHint:.array.29101
+ _propertiesToFetchWithHint:.array.32795
+ _propertiesToFetchWithHint:.array.36461
+ _propertiesToFetchWithHint:.array.40333
+ _propertiesToFetchWithHint:.array.46247
+ _propertiesToFetchWithHint:.array.48124
+ _propertiesToFetchWithHint:.array.50206
+ _propertiesToFetchWithHint:.array.51140
+ _propertiesToFetchWithHint:.array.7985
+ _propertiesToFetchWithHint:.onceToken.11231
+ _propertiesToFetchWithHint:.onceToken.11825
+ _propertiesToFetchWithHint:.onceToken.1239
+ _propertiesToFetchWithHint:.onceToken.13428
+ _propertiesToFetchWithHint:.onceToken.13739
+ _propertiesToFetchWithHint:.onceToken.1441
+ _propertiesToFetchWithHint:.onceToken.22940
+ _propertiesToFetchWithHint:.onceToken.23433
+ _propertiesToFetchWithHint:.onceToken.27834
+ _propertiesToFetchWithHint:.onceToken.28728
+ _propertiesToFetchWithHint:.onceToken.29100
+ _propertiesToFetchWithHint:.onceToken.32793
+ _propertiesToFetchWithHint:.onceToken.34186
+ _propertiesToFetchWithHint:.onceToken.36459
+ _propertiesToFetchWithHint:.onceToken.40332
+ _propertiesToFetchWithHint:.onceToken.4284
+ _propertiesToFetchWithHint:.onceToken.46245
+ _propertiesToFetchWithHint:.onceToken.48122
+ _propertiesToFetchWithHint:.onceToken.50205
+ _propertiesToFetchWithHint:.onceToken.51139
+ _propertiesToFetchWithHint:.onceToken.7984
+ _propertiesToFetchWithHint:.pl_once_object_15.34602
+ _propertiesToFetchWithHint:.pl_once_object_15.40483
+ _propertiesToFetchWithHint:.pl_once_object_15.47318
+ _propertiesToFetchWithHint:.pl_once_object_15.53579
+ _propertiesToFetchWithHint:.pl_once_token_15.34600
+ _propertiesToFetchWithHint:.pl_once_token_15.40481
+ _propertiesToFetchWithHint:.pl_once_token_15.47316
+ _propertiesToFetchWithHint:.pl_once_token_15.53577
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.13431
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.22942
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.28731
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.34188
+ _propertiesToFetchWithHint:.propertyQueue.13430
+ _propertiesToFetchWithHint:.propertyQueue.22941
+ _propertiesToFetchWithHint:.propertyQueue.28730
+ _propertiesToFetchWithHint:.propertyQueue.34187
+ _propertiesToPrefetch.onceToken.22489
+ _propertiesToPrefetch.onceToken.28398
+ _propertiesToPrefetch.onceToken.33880
+ _propertiesToPrefetch.propertiesToPrefetch.22490
+ _propertiesToPrefetch.propertiesToPrefetch.28399
+ _propertiesToPrefetch.propertiesToPrefetch.33881
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.13127
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.28581
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.34157
+ _propertySetAccessorsByPropertySet.onceToken.13126
+ _propertySetAccessorsByPropertySet.onceToken.28580
+ _propertySetAccessorsByPropertySet.onceToken.34156
+ _propertySetClassForPropertySet:.onceToken.13129
+ _propertySetClassForPropertySet:.onceToken.28588
+ _propertySetClassForPropertySet:.onceToken.34165
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13130
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28589
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.34166
+ _sharedDecoder.s_onceToken.50317
+ _sharedDecoder.s_shared.50319
+ _transformValueExpression:forKeyPath:._passThroughSet.11190
+ _transformValueExpression:forKeyPath:._passThroughSet.11815
+ _transformValueExpression:forKeyPath:._passThroughSet.13412
+ _transformValueExpression:forKeyPath:._passThroughSet.13703
+ _transformValueExpression:forKeyPath:._passThroughSet.1435
+ _transformValueExpression:forKeyPath:._passThroughSet.1850
+ _transformValueExpression:forKeyPath:._passThroughSet.22919
+ _transformValueExpression:forKeyPath:._passThroughSet.27803
+ _transformValueExpression:forKeyPath:._passThroughSet.28718
+ _transformValueExpression:forKeyPath:._passThroughSet.29087
+ _transformValueExpression:forKeyPath:._passThroughSet.32776
+ _transformValueExpression:forKeyPath:._passThroughSet.34170
+ _transformValueExpression:forKeyPath:._passThroughSet.36444
+ _transformValueExpression:forKeyPath:._passThroughSet.40301
+ _transformValueExpression:forKeyPath:._passThroughSet.4266
+ _transformValueExpression:forKeyPath:._passThroughSet.44484
+ _transformValueExpression:forKeyPath:._passThroughSet.46225
+ _transformValueExpression:forKeyPath:._passThroughSet.48117
+ _transformValueExpression:forKeyPath:._passThroughSet.51090
+ _transformValueExpression:forKeyPath:._passThroughSet.53527
+ _transformValueExpression:forKeyPath:.onceToken.11189
+ _transformValueExpression:forKeyPath:.onceToken.11814
+ _transformValueExpression:forKeyPath:.onceToken.13411
+ _transformValueExpression:forKeyPath:.onceToken.13702
+ _transformValueExpression:forKeyPath:.onceToken.1434
+ _transformValueExpression:forKeyPath:.onceToken.1849
+ _transformValueExpression:forKeyPath:.onceToken.22918
+ _transformValueExpression:forKeyPath:.onceToken.27802
+ _transformValueExpression:forKeyPath:.onceToken.28717
+ _transformValueExpression:forKeyPath:.onceToken.29086
+ _transformValueExpression:forKeyPath:.onceToken.32775
+ _transformValueExpression:forKeyPath:.onceToken.34169
+ _transformValueExpression:forKeyPath:.onceToken.36443
+ _transformValueExpression:forKeyPath:.onceToken.40300
+ _transformValueExpression:forKeyPath:.onceToken.4265
+ _transformValueExpression:forKeyPath:.onceToken.44483
+ _transformValueExpression:forKeyPath:.onceToken.46224
+ _transformValueExpression:forKeyPath:.onceToken.48116
+ _transformValueExpression:forKeyPath:.onceToken.51089
+ _transformValueExpression:forKeyPath:.onceToken.53526
+ _uniqueObjectIDCache.pl_once_object_76
+ _uniqueObjectIDCache.pl_once_token_76
- +[PHAssetResourceUploadJob fetchAssetResourceUploadJobsWithAction:options:]
- +[PHAssetResourceUploadJobChangeRequest _countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:]
- +[PHAssetResourceUploadJobChangeRequest acknowledgeJob:]
- +[PHAssetResourceUploadJobChangeRequest cancelJob:]
- +[PHAssetResourceUploadJobChangeRequest creationRequestForAssetResourceUploadJobWithURLRequest:assetResource:]
- +[PHAssetResourceUploadJobChangeRequest maximumUnacknowledgedJobCountKey:]
- +[PHAssetResourceUploadJobChangeRequest retryJob:withURLRequest:]
- +[PHAssetResourceUploadJobConfiguration configurationStatusWithOptions:]
- +[PHAssetResourceUploadJobConfigurationChangeRequest creationRequestForAssetResourceUploadJobConfigurationWithState:]
- +[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photosEntityStore:photoLibrary:]
- -[PHAssetResourceUploadJob URLRequest]
- -[PHAssetResourceUploadJobChangeRequest placeholderForCreatedAssetResourceUploadJob]
- -[PHChange _shouldCreateChangeDetailsWithCurrentFetchResultForQuery:]
- -[PHSearchQueryManager _acquireSpotlightSandboxExtensionIfNeeded]
- -[PHSearchQueryManager _releaseSpotlightSandboxExtension]
- -[PHSearchQueryManager dealloc]
- -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:]
- -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:]
- GCC_except_table10011
- GCC_except_table10012
- GCC_except_table10013
- GCC_except_table10014
- GCC_except_table10015
- GCC_except_table10016
- GCC_except_table10017
- GCC_except_table10018
- GCC_except_table10019
- GCC_except_table10055
- GCC_except_table10056
- GCC_except_table10060
- GCC_except_table10079
- GCC_except_table10084
- GCC_except_table10154
- GCC_except_table10247
- GCC_except_table10387
- GCC_except_table10424
- GCC_except_table1043
- GCC_except_table10514
- GCC_except_table10542
- GCC_except_table1059
- GCC_except_table1087
- GCC_except_table11036
- GCC_except_table11191
- GCC_except_table11194
- GCC_except_table11200
- GCC_except_table11206
- GCC_except_table11210
- GCC_except_table11216
- GCC_except_table11322
- GCC_except_table11341
- GCC_except_table11343
- GCC_except_table11345
- GCC_except_table11347
- GCC_except_table11429
- GCC_except_table11436
- GCC_except_table11438
- GCC_except_table11440
- GCC_except_table11446
- GCC_except_table11629
- GCC_except_table11641
- GCC_except_table11683
- GCC_except_table11685
- GCC_except_table11698
- GCC_except_table1179
- GCC_except_table11797
- GCC_except_table11801
- GCC_except_table11840
- GCC_except_table11844
- GCC_except_table11853
- GCC_except_table11854
- GCC_except_table11861
- GCC_except_table11905
- GCC_except_table11949
- GCC_except_table1196
- GCC_except_table12033
- GCC_except_table12036
- GCC_except_table12042
- GCC_except_table12044
- GCC_except_table12084
- GCC_except_table12103
- GCC_except_table12112
- GCC_except_table12168
- GCC_except_table12170
- GCC_except_table12230
- GCC_except_table12374
- GCC_except_table12378
- GCC_except_table12382
- GCC_except_table12443
- GCC_except_table12450
- GCC_except_table12658
- GCC_except_table12900
- GCC_except_table12978
- GCC_except_table13023
- GCC_except_table13070
- GCC_except_table13080
- GCC_except_table13098
- GCC_except_table13113
- GCC_except_table13142
- GCC_except_table13155
- GCC_except_table13157
- GCC_except_table13159
- GCC_except_table13178
- GCC_except_table13260
- GCC_except_table13266
- GCC_except_table13282
- GCC_except_table1357
- GCC_except_table1376
- GCC_except_table1400
- GCC_except_table1439
- GCC_except_table1488
- GCC_except_table1672
- GCC_except_table1676
- GCC_except_table1690
- GCC_except_table1694
- GCC_except_table1704
- GCC_except_table1890
- GCC_except_table1894
- GCC_except_table1896
- GCC_except_table1898
- GCC_except_table1900
- GCC_except_table1902
- GCC_except_table1904
- GCC_except_table1914
- GCC_except_table1916
- GCC_except_table1918
- GCC_except_table1930
- GCC_except_table1962
- GCC_except_table1964
- GCC_except_table1966
- GCC_except_table1968
- GCC_except_table1970
- GCC_except_table1972
- GCC_except_table1974
- GCC_except_table1976
- GCC_except_table1978
- GCC_except_table1980
- GCC_except_table1982
- GCC_except_table1984
- GCC_except_table1986
- GCC_except_table1988
- GCC_except_table1990
- GCC_except_table1992
- GCC_except_table2006
- GCC_except_table2011
- GCC_except_table2013
- GCC_except_table2015
- GCC_except_table2043
- GCC_except_table2045
- GCC_except_table2048
- GCC_except_table2051
- GCC_except_table2157
- GCC_except_table2162
- GCC_except_table2180
- GCC_except_table2220
- GCC_except_table2381
- GCC_except_table2394
- GCC_except_table2419
- GCC_except_table2434
- GCC_except_table2453
- GCC_except_table2463
- GCC_except_table2499
- GCC_except_table2504
- GCC_except_table2565
- GCC_except_table2663
- GCC_except_table2676
- GCC_except_table2710
- GCC_except_table2784
- GCC_except_table2789
- GCC_except_table2794
- GCC_except_table2797
- GCC_except_table2807
- GCC_except_table2820
- GCC_except_table2823
- GCC_except_table2954
- GCC_except_table2958
- GCC_except_table2961
- GCC_except_table3028
- GCC_except_table3036
- GCC_except_table3065
- GCC_except_table3069
- GCC_except_table3074
- GCC_except_table3190
- GCC_except_table3223
- GCC_except_table3229
- GCC_except_table3232
- GCC_except_table3242
- GCC_except_table3246
- GCC_except_table3252
- GCC_except_table3255
- GCC_except_table3259
- GCC_except_table3279
- GCC_except_table3291
- GCC_except_table3307
- GCC_except_table3316
- GCC_except_table3413
- GCC_except_table3419
- GCC_except_table3435
- GCC_except_table3437
- GCC_except_table3439
- GCC_except_table3486
- GCC_except_table3513
- GCC_except_table3544
- GCC_except_table3546
- GCC_except_table3564
- GCC_except_table3566
- GCC_except_table3569
- GCC_except_table3779
- GCC_except_table3781
- GCC_except_table3804
- GCC_except_table3839
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table3867
- GCC_except_table3869
- GCC_except_table3901
- GCC_except_table3906
- GCC_except_table3907
- GCC_except_table4169
- GCC_except_table4175
- GCC_except_table4202
- GCC_except_table4225
- GCC_except_table4227
- GCC_except_table4231
- GCC_except_table4236
- GCC_except_table4247
- GCC_except_table4264
- GCC_except_table4330
- GCC_except_table4640
- GCC_except_table4642
- GCC_except_table4649
- GCC_except_table468
- GCC_except_table4713
- GCC_except_table4715
- GCC_except_table4719
- GCC_except_table4721
- GCC_except_table4724
- GCC_except_table475
- GCC_except_table477
- GCC_except_table4793
- GCC_except_table4798
- GCC_except_table4828
- GCC_except_table485
- GCC_except_table487
- GCC_except_table4975
- GCC_except_table5332
- GCC_except_table5381
- GCC_except_table5399
- GCC_except_table5405
- GCC_except_table5411
- GCC_except_table5424
- GCC_except_table5426
- GCC_except_table5452
- GCC_except_table5454
- GCC_except_table5457
- GCC_except_table5458
- GCC_except_table5463
- GCC_except_table5471
- GCC_except_table5475
- GCC_except_table5484
- GCC_except_table5488
- GCC_except_table5525
- GCC_except_table5533
- GCC_except_table5563
- GCC_except_table5589
- GCC_except_table5593
- GCC_except_table5597
- GCC_except_table561
- GCC_except_table5617
- GCC_except_table5623
- GCC_except_table5627
- GCC_except_table5641
- GCC_except_table5644
- GCC_except_table5647
- GCC_except_table5668
- GCC_except_table5714
- GCC_except_table5725
- GCC_except_table5772
- GCC_except_table5803
- GCC_except_table5806
- GCC_except_table5812
- GCC_except_table5816
- GCC_except_table5845
- GCC_except_table5875
- GCC_except_table5901
- GCC_except_table5903
- GCC_except_table5914
- GCC_except_table5961
- GCC_except_table6035
- GCC_except_table6040
- GCC_except_table6045
- GCC_except_table6186
- GCC_except_table6189
- GCC_except_table6202
- GCC_except_table6237
- GCC_except_table6240
- GCC_except_table625
- GCC_except_table6277
- GCC_except_table6315
- GCC_except_table6317
- GCC_except_table647
- GCC_except_table649
- GCC_except_table653
- GCC_except_table6704
- GCC_except_table6717
- GCC_except_table6730
- GCC_except_table6747
- GCC_except_table6776
- GCC_except_table6779
- GCC_except_table6781
- GCC_except_table6783
- GCC_except_table6785
- GCC_except_table6793
- GCC_except_table6836
- GCC_except_table6849
- GCC_except_table6882
- GCC_except_table6884
- GCC_except_table6923
- GCC_except_table696
- GCC_except_table700
- GCC_except_table701
- GCC_except_table7183
- GCC_except_table7184
- GCC_except_table7194
- GCC_except_table7201
- GCC_except_table7219
- GCC_except_table7220
- GCC_except_table7221
- GCC_except_table7222
- GCC_except_table7223
- GCC_except_table7224
- GCC_except_table7235
- GCC_except_table7236
- GCC_except_table7237
- GCC_except_table7394
- GCC_except_table7612
- GCC_except_table7638
- GCC_except_table7657
- GCC_except_table7659
- GCC_except_table7660
- GCC_except_table7721
- GCC_except_table774
- GCC_except_table7743
- GCC_except_table7747
- GCC_except_table7753
- GCC_except_table7806
- GCC_except_table783
- GCC_except_table7966
- GCC_except_table7968
- GCC_except_table8015
- GCC_except_table8055
- GCC_except_table8059
- GCC_except_table8061
- GCC_except_table8063
- GCC_except_table8075
- GCC_except_table8080
- GCC_except_table8120
- GCC_except_table8148
- GCC_except_table8273
- GCC_except_table8331
- GCC_except_table8351
- GCC_except_table8354
- GCC_except_table8373
- GCC_except_table8435
- GCC_except_table8439
- GCC_except_table8443
- GCC_except_table8452
- GCC_except_table8454
- GCC_except_table8494
- GCC_except_table8558
- GCC_except_table871
- GCC_except_table8715
- GCC_except_table8756
- GCC_except_table8761
- GCC_except_table9006
- GCC_except_table9010
- GCC_except_table9014
- GCC_except_table9034
- GCC_except_table9035
- GCC_except_table9127
- GCC_except_table9137
- GCC_except_table9169
- GCC_except_table919
- GCC_except_table9221
- GCC_except_table9261
- GCC_except_table9281
- GCC_except_table9308
- GCC_except_table9333
- GCC_except_table9366
- GCC_except_table9368
- GCC_except_table9458
- GCC_except_table9549
- GCC_except_table9668
- GCC_except_table9682
- GCC_except_table9683
- GCC_except_table9690
- GCC_except_table9693
- GCC_except_table9716
- GCC_except_table9717
- GCC_except_table9718
- GCC_except_table9720
- GCC_except_table9721
- GCC_except_table9723
- GCC_except_table9724
- GCC_except_table9725
- GCC_except_table9726
- GCC_except_table9727
- GCC_except_table9728
- GCC_except_table9729
- GCC_except_table9731
- GCC_except_table9732
- GCC_except_table9733
- GCC_except_table9734
- GCC_except_table9735
- GCC_except_table9736
- GCC_except_table9737
- GCC_except_table9738
- GCC_except_table9739
- GCC_except_table9741
- GCC_except_table9742
- GCC_except_table9743
- GCC_except_table9744
- GCC_except_table9759
- GCC_except_table9769
- GCC_except_table9909
- GCC_except_table9918
- GCC_except_table9919
- GCC_except_table9920
- GCC_except_table9921
- GCC_except_table9922
- GCC_except_table9932
- GCC_except_table9976
- GCC_except_table9977
- GCC_except_table9978
- GCC_except_table9979
- GCC_except_table9990
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_PLFileSystemVolumeManager
- _OBJC_CLASS_$__EXExtensionIdentity
- _OBJC_IVAR_$_PHAssetResourceUploadJob._URLRequest
- _PLResourceBackgroundUploadExtensionPointLabel
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19122
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22362
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36467
- __PROTOCOLS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration.1
- ___103-[PHPhotoLibrary _sendChangesRequest:onExecutionContext:withInstrumentation:remainingRetryCount:reply:]_block_invoke.488
- ___109-[PHSearchQueryManager suggestionsForSearchQuery:rangeOfSuggestionText:searchQueryResult:suggestionsHandler:]_block_invoke.116
- ___109-[PHSearchQueryManager suggestionsForSearchQuery:rangeOfSuggestionText:searchQueryResult:suggestionsHandler:]_block_invoke.117
- ___110+[PHAssetResourceUploadJobChangeRequest _countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:]_block_invoke
- ___128+[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photosEntityStore:photoLibrary:]_block_invoke
- ___128+[PHSearchQueryAnnotation annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photosEntityStore:photoLibrary:]_block_invoke_2
- ___34-[PHPhotoLibrary postOpenProgress]_block_invoke.418
- ___49-[PHSearchResultProcessor _processSpotlightItem:]_block_invoke
- ___49-[PHSearchResultProcessor _processSpotlightItem:]_block_invoke_2
- ___49-[PHSearchResultProcessor _processSpotlightItem:]_block_invoke_3
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke.435
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_2.436
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_3.437
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_4.438
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_5.440
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_6.441
- ___50-[PHPhotoLibrary initWithPhotoLibraryBundle:type:]_block_invoke_7.446
- ___55-[PHPhotoLibrary _processPendingChangesWithDebugEvent:]_block_invoke.693
- ___55-[PHPhotoLibrary openAndWaitWithUpgrade:options:error:]_block_invoke.400
- ___55-[PHPhotoLibrary openAndWaitWithUpgrade:options:error:]_block_invoke_2.403
- ___57-[PHSearchQueryManager _releaseSpotlightSandboxExtension]_block_invoke
- ___62-[PHImageManager requestStreamForVideo:options:resultHandler:]_block_invoke.691
- ___63-[PHImageManager requestAVProxyForAsset:options:resultHandler:]_block_invoke.739
- ___64-[PHPhotoLibrary _onQueueNotifyAvailabilityObserversWithReason:]_block_invoke.478
- ___65-[PHSearchQueryManager _acquireSpotlightSandboxExtensionIfNeeded]_block_invoke
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.680
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke.684
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.685
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_2.689
- ___66-[PHImageManager requestPlayerItemForVideo:options:resultHandler:]_block_invoke_3.686
- ___67-[PHSearchQueryManager performSearch:searchOptions:resultsHandler:]_block_invoke.75
- ___67-[PHSearchQueryManager performSearch:searchOptions:resultsHandler:]_block_invoke.76
- ___69-[PHPhotoLibrary _stopWatchingFileSystemVolumeForLibraryAvailability]_block_invoke
- ___70-[PHPhotoLibrary _startWatchingFileSystemVolumeForLibraryAvailability]_block_invoke
- ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.83
- ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.89
- ___72-[PHSearchQueryManager performBatchSearch:searchOptions:resultsHandler:]_block_invoke.90
- ___76-[PHSearchQueryManager suggestionsForSearchText:options:suggestionsHandler:]_block_invoke.120
- ___84+[PHSearchUtility insertSpacingIfNeededBetweenAnnotationsAndPlainTextInQueryString:]_block_invoke.130
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.656
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.660
- ___88-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.665
- ___89-[PHImageManager requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:]_block_invoke.713
- ___Block_byref_object_copy_.10325
- ___Block_byref_object_copy_.11071
- ___Block_byref_object_copy_.11345
- ___Block_byref_object_copy_.11504
- ___Block_byref_object_copy_.12348
- ___Block_byref_object_copy_.12613
- ___Block_byref_object_copy_.13087
- ___Block_byref_object_copy_.13561
- ___Block_byref_object_copy_.1418
- ___Block_byref_object_copy_.14776
- ___Block_byref_object_copy_.1490
- ___Block_byref_object_copy_.15511
- ___Block_byref_object_copy_.17451
- ___Block_byref_object_copy_.18428
- ___Block_byref_object_copy_.1945
- ___Block_byref_object_copy_.20092
- ___Block_byref_object_copy_.20258
- ___Block_byref_object_copy_.20580
- ___Block_byref_object_copy_.21047
- ___Block_byref_object_copy_.21653
- ___Block_byref_object_copy_.22175
- ___Block_byref_object_copy_.22369
- ___Block_byref_object_copy_.2345
- ___Block_byref_object_copy_.24196
- ___Block_byref_object_copy_.25072
- ___Block_byref_object_copy_.26755
- ___Block_byref_object_copy_.27278
- ___Block_byref_object_copy_.2778
- ___Block_byref_object_copy_.28005
- ___Block_byref_object_copy_.28295
- ___Block_byref_object_copy_.29819
- ___Block_byref_object_copy_.30791
- ___Block_byref_object_copy_.31536
- ___Block_byref_object_copy_.31830
- ___Block_byref_object_copy_.3308
- ___Block_byref_object_copy_.33209
- ___Block_byref_object_copy_.33783
- ___Block_byref_object_copy_.34346
- ___Block_byref_object_copy_.34537
- ___Block_byref_object_copy_.34975
- ___Block_byref_object_copy_.35554
- ___Block_byref_object_copy_.35832
- ___Block_byref_object_copy_.36764
- ___Block_byref_object_copy_.37244
- ___Block_byref_object_copy_.38846
- ___Block_byref_object_copy_.3907
- ___Block_byref_object_copy_.39403
- ___Block_byref_object_copy_.43467
- ___Block_byref_object_copy_.43891
- ___Block_byref_object_copy_.44102
- ___Block_byref_object_copy_.44331
- ___Block_byref_object_copy_.45671
- ___Block_byref_object_copy_.46079
- ___Block_byref_object_copy_.46598
- ___Block_byref_object_copy_.46900
- ___Block_byref_object_copy_.47276
- ___Block_byref_object_copy_.47763
- ___Block_byref_object_copy_.48273
- ___Block_byref_object_copy_.49151
- ___Block_byref_object_copy_.49349
- ___Block_byref_object_copy_.49559
- ___Block_byref_object_copy_.49596
- ___Block_byref_object_copy_.51767
- ___Block_byref_object_copy_.52067
- ___Block_byref_object_copy_.52800
- ___Block_byref_object_copy_.53601
- ___Block_byref_object_copy_.5447
- ___Block_byref_object_copy_.6498
- ___Block_byref_object_copy_.6970
- ___Block_byref_object_copy_.8440
- ___Block_byref_object_copy_.8765
- ___Block_byref_object_copy_.900
- ___Block_byref_object_copy_.9057
- ___Block_byref_object_copy_.9625
- ___Block_byref_object_dispose_.10326
- ___Block_byref_object_dispose_.11072
- ___Block_byref_object_dispose_.11346
- ___Block_byref_object_dispose_.11505
- ___Block_byref_object_dispose_.12349
- ___Block_byref_object_dispose_.12614
- ___Block_byref_object_dispose_.13088
- ___Block_byref_object_dispose_.13562
- ___Block_byref_object_dispose_.1419
- ___Block_byref_object_dispose_.14777
- ___Block_byref_object_dispose_.1491
- ___Block_byref_object_dispose_.15512
- ___Block_byref_object_dispose_.17452
- ___Block_byref_object_dispose_.18429
- ___Block_byref_object_dispose_.1946
- ___Block_byref_object_dispose_.20093
- ___Block_byref_object_dispose_.20259
- ___Block_byref_object_dispose_.20581
- ___Block_byref_object_dispose_.21048
- ___Block_byref_object_dispose_.21654
- ___Block_byref_object_dispose_.22176
- ___Block_byref_object_dispose_.22370
- ___Block_byref_object_dispose_.2346
- ___Block_byref_object_dispose_.24197
- ___Block_byref_object_dispose_.25073
- ___Block_byref_object_dispose_.26756
- ___Block_byref_object_dispose_.27279
- ___Block_byref_object_dispose_.2779
- ___Block_byref_object_dispose_.28006
- ___Block_byref_object_dispose_.28296
- ___Block_byref_object_dispose_.29820
- ___Block_byref_object_dispose_.30792
- ___Block_byref_object_dispose_.31537
- ___Block_byref_object_dispose_.31831
- ___Block_byref_object_dispose_.3309
- ___Block_byref_object_dispose_.33210
- ___Block_byref_object_dispose_.33784
- ___Block_byref_object_dispose_.34347
- ___Block_byref_object_dispose_.34538
- ___Block_byref_object_dispose_.34976
- ___Block_byref_object_dispose_.35555
- ___Block_byref_object_dispose_.35833
- ___Block_byref_object_dispose_.36765
- ___Block_byref_object_dispose_.37245
- ___Block_byref_object_dispose_.38847
- ___Block_byref_object_dispose_.3908
- ___Block_byref_object_dispose_.39404
- ___Block_byref_object_dispose_.43468
- ___Block_byref_object_dispose_.43892
- ___Block_byref_object_dispose_.44103
- ___Block_byref_object_dispose_.44332
- ___Block_byref_object_dispose_.45672
- ___Block_byref_object_dispose_.46080
- ___Block_byref_object_dispose_.46599
- ___Block_byref_object_dispose_.46901
- ___Block_byref_object_dispose_.47277
- ___Block_byref_object_dispose_.47764
- ___Block_byref_object_dispose_.48274
- ___Block_byref_object_dispose_.49152
- ___Block_byref_object_dispose_.49350
- ___Block_byref_object_dispose_.49560
- ___Block_byref_object_dispose_.49597
- ___Block_byref_object_dispose_.51768
- ___Block_byref_object_dispose_.52068
- ___Block_byref_object_dispose_.52801
- ___Block_byref_object_dispose_.53602
- ___Block_byref_object_dispose_.5448
- ___Block_byref_object_dispose_.6499
- ___Block_byref_object_dispose_.6971
- ___Block_byref_object_dispose_.8441
- ___Block_byref_object_dispose_.8766
- ___Block_byref_object_dispose_.901
- ___Block_byref_object_dispose_.9058
- ___Block_byref_object_dispose_.9626
- ___SensitiveContentAnalysisLibraryCore_block_invoke.19123
- ___SensitiveContentAnalysisLibraryCore_block_invoke.22363
- ___SensitiveContentAnalysisLibraryCore_block_invoke.36468
- ___block_literal_global.1041.36649
- ___block_literal_global.10455
- ___block_literal_global.1053.36648
- ___block_literal_global.1063.36645
- ___block_literal_global.1065.36643
- ___block_literal_global.1099.36641
- ___block_literal_global.11166
- ___block_literal_global.112.41158
- ___block_literal_global.11361
- ___block_literal_global.11738
- ___block_literal_global.1236
- ___block_literal_global.12670
- ___block_literal_global.13381
- ___block_literal_global.134.47823
- ___block_literal_global.13563
- ___block_literal_global.1358
- ___block_literal_global.1367
- ___block_literal_global.1382
- ___block_literal_global.1392
- ___block_literal_global.1411
- ___block_literal_global.14128
- ___block_literal_global.1438
- ___block_literal_global.14451
- ___block_literal_global.146.38814
- ___block_literal_global.14844
- ___block_literal_global.15496
- ___block_literal_global.17032
- ___block_literal_global.1740
- ___block_literal_global.1744
- ___block_literal_global.1751
- ___block_literal_global.17685
- ___block_literal_global.18457
- ___block_literal_global.185
- ___block_literal_global.18508
- ___block_literal_global.191
- ___block_literal_global.1956
- ___block_literal_global.19692
- ___block_literal_global.20010
- ___block_literal_global.203
- ___block_literal_global.20596
- ___block_literal_global.206.28578
- ___block_literal_global.206.29485
- ___block_literal_global.210.29488
- ___block_literal_global.21022
- ___block_literal_global.212.29489
- ___block_literal_global.217.13933
- ___block_literal_global.219
- ___block_literal_global.21962
- ___block_literal_global.224.14732
- ___block_literal_global.22837
- ___block_literal_global.234.34070
- ___block_literal_global.2375
- ___block_literal_global.240
- ___block_literal_global.24105
- ___block_literal_global.25431
- ___block_literal_global.2594
- ___block_literal_global.26097
- ___block_literal_global.26979
- ___block_literal_global.27708
- ___block_literal_global.2775
- ___block_literal_global.27982
- ___block_literal_global.28609
- ___block_literal_global.28880
- ___block_literal_global.28959
- ___block_literal_global.2937
- ___block_literal_global.29474
- ___block_literal_global.29936
- ___block_literal_global.3.11366
- ___block_literal_global.3.2774
- ___block_literal_global.30321
- ___block_literal_global.30518
- ___block_literal_global.30802
- ___block_literal_global.31219
- ___block_literal_global.32063
- ___block_literal_global.32207
- ___block_literal_global.32680
- ___block_literal_global.33294
- ___block_literal_global.3385
- ___block_literal_global.34073
- ___block_literal_global.34360
- ___block_literal_global.34482
- ___block_literal_global.34634
- ___block_literal_global.348.19584
- ___block_literal_global.34817
- ___block_literal_global.35292
- ___block_literal_global.3535
- ___block_literal_global.35837
- ___block_literal_global.36342
- ___block_literal_global.37.32109
- ___block_literal_global.37.47395
- ___block_literal_global.37110
- ___block_literal_global.37305
- ___block_literal_global.37850
- ___block_literal_global.38157
- ___block_literal_global.38889
- ___block_literal_global.39147
- ___block_literal_global.39576
- ___block_literal_global.40156
- ___block_literal_global.402
- ___block_literal_global.40370
- ___block_literal_global.40856
- ___block_literal_global.41164
- ___block_literal_global.4234
- ___block_literal_global.42474
- ___block_literal_global.4274
- ___block_literal_global.43057
- ___block_literal_global.43470
- ___block_literal_global.44157
- ___block_literal_global.44348
- ___block_literal_global.44969
- ___block_literal_global.45756
- ___block_literal_global.460
- ___block_literal_global.46111
- ___block_literal_global.4637
- ___block_literal_global.464
- ___block_literal_global.46429
- ___block_literal_global.46520
- ___block_literal_global.47184
- ___block_literal_global.4729
- ___block_literal_global.47402
- ___block_literal_global.47842
- ___block_literal_global.47990
- ___block_literal_global.4803
- ___block_literal_global.48764
- ___block_literal_global.490
- ___block_literal_global.49116
- ___block_literal_global.49561
- ___block_literal_global.496
- ___block_literal_global.49609
- ___block_literal_global.49918
- ___block_literal_global.50.26065
- ___block_literal_global.50191
- ___block_literal_global.51503
- ___block_literal_global.52887
- ___block_literal_global.53455
- ___block_literal_global.548
- ___block_literal_global.5480
- ___block_literal_global.560
- ___block_literal_global.589
- ___block_literal_global.62.1416
- ___block_literal_global.6585
- ___block_literal_global.669
- ___block_literal_global.678.36837
- ___block_literal_global.681
- ___block_literal_global.683
- ___block_literal_global.6977
- ___block_literal_global.7648
- ___block_literal_global.7871
- ___block_literal_global.804
- ___block_literal_global.8041
- ___block_literal_global.85.53433
- ___block_literal_global.8757
- ___block_literal_global.8844
- ___block_literal_global.9295
- ___block_literal_global.98
- ___block_literal_global.980.13075
- ___getSCSensitivityAnalysisClass_block_invoke.19121
- ___getSCSensitivityAnalysisClass_block_invoke.22361
- ___getSCSensitivityAnalysisClass_block_invoke.36466
- ___unnamed_5
- __currentTimestampString.s_formatter.47396
- __currentTimestampString.s_onceToken.47394
- _allowedEntities.pl_once_object_82
- _allowedEntities.pl_once_object_83
- _allowedEntities.pl_once_token_82
- _allowedEntities.pl_once_token_83
- _allowedInfoKeys.allowedKeys.1549
- _allowedInfoKeys.allowedKeys.18710
- _allowedInfoKeys.allowedKeys.40661
- _allowedInfoKeys.onceToken.1548
- _allowedInfoKeys.onceToken.18709
- _allowedInfoKeys.onceToken.40660
- _audit_stringSensitiveContentAnalysis.19132
- _audit_stringSensitiveContentAnalysis.22367
- _audit_stringSensitiveContentAnalysis.36478
- _block_copy_helper.7
- _block_descriptor.9
- _block_destroy_helper.8
- _corePropertiesToFetch.array.22840
- _corePropertiesToFetch.array.28606
- _corePropertiesToFetch.array.34074
- _corePropertiesToFetch.onceToken.22839
- _corePropertiesToFetch.onceToken.28605
- _corePropertiesToFetch.onceToken.34072
- _defaultManager.onceToken.51849
- _entityKeyMap.pl_once_object_15.11147
- _entityKeyMap.pl_once_object_15.11749
- _entityKeyMap.pl_once_object_15.1226
- _entityKeyMap.pl_once_object_15.13372
- _entityKeyMap.pl_once_object_15.13669
- _entityKeyMap.pl_once_object_15.1434
- _entityKeyMap.pl_once_object_15.1850
- _entityKeyMap.pl_once_object_15.27699
- _entityKeyMap.pl_once_object_15.28970
- _entityKeyMap.pl_once_object_15.32671
- _entityKeyMap.pl_once_object_15.36332
- _entityKeyMap.pl_once_object_15.40188
- _entityKeyMap.pl_once_object_15.44371
- _entityKeyMap.pl_once_object_15.46102
- _entityKeyMap.pl_once_object_15.4629
- _entityKeyMap.pl_once_object_15.46512
- _entityKeyMap.pl_once_object_15.47987
- _entityKeyMap.pl_once_object_15.50066
- _entityKeyMap.pl_once_object_15.50985
- _entityKeyMap.pl_once_object_15.7877
- _entityKeyMap.pl_once_object_16.34062
- _entityKeyMap.pl_once_object_16.34472
- _entityKeyMap.pl_once_object_16.40357
- _entityKeyMap.pl_once_object_16.4222
- _entityKeyMap.pl_once_object_16.47172
- _entityKeyMap.pl_once_object_16.53442
- _entityKeyMap.pl_once_token_15.11146
- _entityKeyMap.pl_once_token_15.11748
- _entityKeyMap.pl_once_token_15.1225
- _entityKeyMap.pl_once_token_15.13371
- _entityKeyMap.pl_once_token_15.13668
- _entityKeyMap.pl_once_token_15.1433
- _entityKeyMap.pl_once_token_15.1849
- _entityKeyMap.pl_once_token_15.27698
- _entityKeyMap.pl_once_token_15.28969
- _entityKeyMap.pl_once_token_15.32670
- _entityKeyMap.pl_once_token_15.36331
- _entityKeyMap.pl_once_token_15.40187
- _entityKeyMap.pl_once_token_15.44370
- _entityKeyMap.pl_once_token_15.46101
- _entityKeyMap.pl_once_token_15.4628
- _entityKeyMap.pl_once_token_15.46511
- _entityKeyMap.pl_once_token_15.47986
- _entityKeyMap.pl_once_token_15.50065
- _entityKeyMap.pl_once_token_15.50984
- _entityKeyMap.pl_once_token_15.7876
- _entityKeyMap.pl_once_token_16.34061
- _entityKeyMap.pl_once_token_16.34471
- _entityKeyMap.pl_once_token_16.40356
- _entityKeyMap.pl_once_token_16.4221
- _entityKeyMap.pl_once_token_16.47171
- _entityKeyMap.pl_once_token_16.53441
- _getSCSensitivityAnalysisClass.19119
- _getSCSensitivityAnalysisClass.36462
- _getSCSensitivityAnalysisClass.softClass.19120
- _getSCSensitivityAnalysisClass.softClass.22360
- _getSCSensitivityAnalysisClass.softClass.36465
- _get_witness_table 6Photos35PHBackgroundResourceUploadExtensionRzlAA01_bcdE13Configuration33_418ED0618F5CF054A91C652800E09068LLCyxGAA0bcdeF0HPyHC.2
- _identifierPropertiesToFetch.array.35293
- _identifierPropertiesToFetch.onceToken.35291
- _objc_msgSend$_acquireSpotlightSandboxExtensionIfNeeded
- _objc_msgSend$_countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:
- _objc_msgSend$_releaseSpotlightSandboxExtension
- _objc_msgSend$_shouldCreateChangeDetailsWithCurrentFetchResultForQuery:
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photosEntityStore:photoLibrary:
- _objc_msgSend$applicationExtensionRecords
- _objc_msgSend$archiveDataForURLRequest:
- _objc_msgSend$changeRequestForUploadJob:
- _objc_msgSend$extensionPointIdentifier
- _objc_msgSend$initWithApplicationExtensionRecord:
- _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
- _objc_msgSend$initWithSceneAnalysisVersion:faceAnalysisVersion:characterRecognitionAlgorithmVersion:visualSearchAlgorithmVersion:stickerConfidenceAlgorithmVersion:vaAnalysisVersion:vaLocationAnalysisVersion:mediaAnalysisVersion:mediaAnalysisImageVersion:captionGenerationVersion:imageEmbeddingVersion:videoEmbeddingVersion:videoSensitivityAnalysisVersion:
- _objc_msgSend$initWithSceneAnalysisVersion:imageEmbeddingVersion:faceAnalysisVersion:characterRecognitionAlgorithmVersion:visualSearchAlgorithmVersion:stickerConfidenceAlgorithmVersion:vaAnalysisVersion:vaLocationAnalysisVersion:mediaAnalysisVersion:mediaAnalysisImageVersion:captionGenerationVersion:
- _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:
- _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:
- _objc_msgSend$maximumUnacknowledgedJobCountKey:
- _objc_msgSend$queryForAssetResourceUploadJobsWithConfiguration:states:options:
- _objc_msgSend$removeObserver:forKeyPath:context:
- _objc_msgSend$sharedFileSystemVolumeManager
- _objc_msgSend$unregisterWithVolumeManager
- _propertiesToFetch.pl_once_object_24.33779
- _propertiesToFetch.pl_once_token_24.33778
- _propertiesToFetchWithHint:.array.11162
- _propertiesToFetchWithHint:.array.11756
- _propertiesToFetchWithHint:.array.13692
- _propertiesToFetchWithHint:.array.1439
- _propertiesToFetchWithHint:.array.23334
- _propertiesToFetchWithHint:.array.27709
- _propertiesToFetchWithHint:.array.28980
- _propertiesToFetchWithHint:.array.32681
- _propertiesToFetchWithHint:.array.36343
- _propertiesToFetchWithHint:.array.40209
- _propertiesToFetchWithHint:.array.46112
- _propertiesToFetchWithHint:.array.47991
- _propertiesToFetchWithHint:.array.50079
- _propertiesToFetchWithHint:.array.51013
- _propertiesToFetchWithHint:.array.7905
- _propertiesToFetchWithHint:.onceToken.11161
- _propertiesToFetchWithHint:.onceToken.11755
- _propertiesToFetchWithHint:.onceToken.1235
- _propertiesToFetchWithHint:.onceToken.13380
- _propertiesToFetchWithHint:.onceToken.13691
- _propertiesToFetchWithHint:.onceToken.1437
- _propertiesToFetchWithHint:.onceToken.22833
- _propertiesToFetchWithHint:.onceToken.23333
- _propertiesToFetchWithHint:.onceToken.27707
- _propertiesToFetchWithHint:.onceToken.28608
- _propertiesToFetchWithHint:.onceToken.28979
- _propertiesToFetchWithHint:.onceToken.32679
- _propertiesToFetchWithHint:.onceToken.34066
- _propertiesToFetchWithHint:.onceToken.36341
- _propertiesToFetchWithHint:.onceToken.40208
- _propertiesToFetchWithHint:.onceToken.4232
- _propertiesToFetchWithHint:.onceToken.46110
- _propertiesToFetchWithHint:.onceToken.47989
- _propertiesToFetchWithHint:.onceToken.50078
- _propertiesToFetchWithHint:.onceToken.51012
- _propertiesToFetchWithHint:.onceToken.7904
- _propertiesToFetchWithHint:.pl_once_object_15.34483
- _propertiesToFetchWithHint:.pl_once_object_15.40371
- _propertiesToFetchWithHint:.pl_once_object_15.47185
- _propertiesToFetchWithHint:.pl_once_object_15.53456
- _propertiesToFetchWithHint:.pl_once_token_15.34481
- _propertiesToFetchWithHint:.pl_once_token_15.40369
- _propertiesToFetchWithHint:.pl_once_token_15.47183
- _propertiesToFetchWithHint:.pl_once_token_15.53454
- _propertiesToFetchWithHint:.propertiesToFetchByHint.13383
- _propertiesToFetchWithHint:.propertiesToFetchByHint.22835
- _propertiesToFetchWithHint:.propertiesToFetchByHint.28611
- _propertiesToFetchWithHint:.propertiesToFetchByHint.34068
- _propertiesToFetchWithHint:.propertyQueue.13382
- _propertiesToFetchWithHint:.propertyQueue.22834
- _propertiesToFetchWithHint:.propertyQueue.28610
- _propertiesToFetchWithHint:.propertyQueue.34067
- _propertiesToPrefetch.onceToken.22374
- _propertiesToPrefetch.onceToken.28274
- _propertiesToPrefetch.onceToken.33760
- _propertiesToPrefetch.propertiesToPrefetch.22375
- _propertiesToPrefetch.propertiesToPrefetch.28275
- _propertiesToPrefetch.propertiesToPrefetch.33761
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.13071
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.28457
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.34037
- _propertySetAccessorsByPropertySet.onceToken.13070
- _propertySetAccessorsByPropertySet.onceToken.28456
- _propertySetAccessorsByPropertySet.onceToken.34036
- _propertySetClassForPropertySet:.onceToken.13074
- _propertySetClassForPropertySet:.onceToken.28464
- _propertySetClassForPropertySet:.onceToken.34045
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13076
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28465
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.34046
- _sharedDecoder.s_onceToken.50190
- _sharedDecoder.s_shared.50192
- _symbolic $s6Photos48PHBackgroundResourceUploadExtensionConfigurationP
- _symbolic Su
- _transformValueExpression:forKeyPath:._passThroughSet.11120
- _transformValueExpression:forKeyPath:._passThroughSet.11745
- _transformValueExpression:forKeyPath:._passThroughSet.13361
- _transformValueExpression:forKeyPath:._passThroughSet.13654
- _transformValueExpression:forKeyPath:._passThroughSet.1431
- _transformValueExpression:forKeyPath:._passThroughSet.1846
- _transformValueExpression:forKeyPath:._passThroughSet.22813
- _transformValueExpression:forKeyPath:._passThroughSet.27675
- _transformValueExpression:forKeyPath:._passThroughSet.28594
- _transformValueExpression:forKeyPath:._passThroughSet.28966
- _transformValueExpression:forKeyPath:._passThroughSet.32662
- _transformValueExpression:forKeyPath:._passThroughSet.34050
- _transformValueExpression:forKeyPath:._passThroughSet.36326
- _transformValueExpression:forKeyPath:._passThroughSet.40177
- _transformValueExpression:forKeyPath:._passThroughSet.4211
- _transformValueExpression:forKeyPath:._passThroughSet.44353
- _transformValueExpression:forKeyPath:._passThroughSet.46090
- _transformValueExpression:forKeyPath:._passThroughSet.47984
- _transformValueExpression:forKeyPath:._passThroughSet.50963
- _transformValueExpression:forKeyPath:._passThroughSet.53404
- _transformValueExpression:forKeyPath:.onceToken.11119
- _transformValueExpression:forKeyPath:.onceToken.11744
- _transformValueExpression:forKeyPath:.onceToken.13360
- _transformValueExpression:forKeyPath:.onceToken.13653
- _transformValueExpression:forKeyPath:.onceToken.1430
- _transformValueExpression:forKeyPath:.onceToken.1845
- _transformValueExpression:forKeyPath:.onceToken.22812
- _transformValueExpression:forKeyPath:.onceToken.27674
- _transformValueExpression:forKeyPath:.onceToken.28593
- _transformValueExpression:forKeyPath:.onceToken.28965
- _transformValueExpression:forKeyPath:.onceToken.32661
- _transformValueExpression:forKeyPath:.onceToken.34049
- _transformValueExpression:forKeyPath:.onceToken.36325
- _transformValueExpression:forKeyPath:.onceToken.40176
- _transformValueExpression:forKeyPath:.onceToken.4210
- _transformValueExpression:forKeyPath:.onceToken.44352
- _transformValueExpression:forKeyPath:.onceToken.46089
- _transformValueExpression:forKeyPath:.onceToken.47983
- _transformValueExpression:forKeyPath:.onceToken.50962
- _transformValueExpression:forKeyPath:.onceToken.53403
- _uniqueObjectIDCache.pl_once_object_81
- _uniqueObjectIDCache.pl_once_token_81
CStrings:
+ " - %@: %@"
+ "%@, destination: %@ state: %ld clientStatus: %ld lastModifiedDate: %@ attemptCount: %hu"
+ "0 0"
+ "<%@ %p>"
+ "@\"PHFeatureAvailabilityReadOptions\""
+ "@112@0:8Q16@24Q32B40B44@48@56@64@72@80@88@96@104"
+ "@80@0:8s16s20s24s28s32s36s40Q44s52s56s60s64s68s72s76"
+ "Current state:%ld and acknowledgement:%ldcurrentAcknowledgement"
+ "Error initializing SCSensitivityAnalysis for asset: %{public}@ error: %@ value: %lld"
+ "Error initializing SCSensitivityAnalysis for assetID: %{public}@ error: %@ value: %lld"
+ "FeatureAvailability - encountered error validating spotlight index: %@"
+ "FeatureAvailability - graph updated availability was nil"
+ "FeatureAvailability - just-in-time invalidating spotlight index availability during availability fetch"
+ "FeatureAvailability - updated availability was nil, initing new. Encountered error: %@"
+ "Invalid syndication bundle identifier (%@) for SearchableItem: %@"
+ "Missing syndication bundle identifier for SearchableItem: %@, skipping"
+ "PHFeatureAvailability - validateSpotlightAvailabilityInFeatureAvailability"
+ "PHPhotosErrorSearchIntentsUnarchiveError"
+ "PHSearchResultPropertyBundleIdentifier"
+ "PHSearchResultPropertyUUID"
+ "PHSearchResultResultType"
+ "Preparing query options for SPL query with bundleIDs: %@"
+ "Preparing query options for syndication library query with bundleIDs: %@"
+ "Retrieving Spotlight Private Index at path: %@"
+ "Should only have 1 configuration"
+ "T@\"NSArray\",R,N,V_bundleIdentifiers"
+ "T@\"NSArray\",R,N,V_filterQueries"
+ "T@\"NSURLRequest\",R,V_destination"
+ "T@\"PHAssetResource\",R,V_resource"
+ "TB,N,V_validateSpotlightAvailability"
+ "TB,R,GisUploadJobExtensionEnabled"
+ "TUAnalysis"
+ "TUGating"
+ "Too many configurations"
+ "Tq,R,N,V_clientStatus"
+ "Tq,R,V_state"
+ "Ts,V_textUnderstandingAlgorithmVersion"
+ "Ts,V_textUnderstandingGatingVersion"
+ "Unable to open Spotlight Index"
+ "_bundleIdentifiers"
+ "_countOfCancellableAcknowledgeableJobsWithConfiguration:library:error:"
+ "_errorCodeForAuthorizationStatus:accessLevel:"
+ "_filterQueries"
+ "_finalizePhotosResultsForQuery:resultHandler:"
+ "_finalizeSyndicationResultsForQuery:resultHandler:"
+ "_isSyndicationLibrary"
+ "_processSearchableItemForPhotosLibrary:"
+ "_processSearchableItemForSyndicationLibrary:"
+ "_readOptions"
+ "_spotlightIndexStateForLibraryWithCompletionHandler:"
+ "_textUnderstandingAlgorithmVersion"
+ "_textUnderstandingGatingVersion"
+ "_validateSpotlightAvailability"
+ "_validateSpotlightAvailabilityInFeatureAvailability:forFeature:completionHandler:"
+ "acknowledge"
+ "acquireSpotlightSandboxExtensionIfNeeded"
+ "addAttributeKeyPath:forEntityName:"
+ "addRelationshipKeyPath:forEntityName:"
+ "annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photoLibrary:"
+ "archiveDataForDestination:"
+ "availabilityFromInvalidatingSearchIndexInFeatureAvailability:"
+ "background-upload"
+ "bundleID"
+ "bundleIdentifier: %@\n"
+ "bundleIdentifiers"
+ "changeRequestForConfiguration:"
+ "createJobWithDestination:resource:"
+ "creationRequestForAssetResourceUploadJobWithDestination:resource:"
+ "currentTUAlgorithmVersion"
+ "currentTUGatingVersion"
+ "featureAvailabilityForFeature:readOptions:completionHandler:"
+ "fetchJobsWithAction:options:"
+ "fetchOptionsWithOverriddenChangeDetectionCriteriaIfNecessary:"
+ "filterQueries"
+ "initWithPhotoLibrary:readOptions:"
+ "initWithSceneAnalysisVersion:faceAnalysisVersion:characterRecognitionAlgorithmVersion:visualSearchAlgorithmVersion:stickerConfidenceAlgorithmVersion:vaAnalysisVersion:vaLocationAnalysisVersion:mediaAnalysisVersion:mediaAnalysisImageVersion:captionGenerationVersion:imageEmbeddingVersion:videoEmbeddingVersion:videoSensitivityAnalysisVersion:textUnderstandingAlgorithmVersion:textUnderstandingGatingVersion:"
+ "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:bundleIdentifier:"
+ "isBackgroundResourceUploadExtensionClient"
+ "isSyndicationAsset"
+ "isSyndicationLibrary:"
+ "isUploadJobExtensionEnabled"
+ "jobLimit"
+ "kMDItemPhotosDonationState > 0"
+ "q40@0:8@16@24^@32"
+ "queryForInFlightJobCountWithConfiguration:options:"
+ "queryOptionsForSyndicationLibraryWithOptions:"
+ "retryWithDestination:"
+ "setBundleIdentifiers:"
+ "setTextUnderstandingAlgorithmVersion:"
+ "setTextUnderstandingGatingVersion:"
+ "setUploadJobExtensionEnabled:error:"
+ "setValidateSpotlightAvailability:"
+ "syndicationLibraryBundleIdentifiers"
+ "textUnderstandingAlgorithmVersion"
+ "textUnderstandingGatingVersion"
+ "tu"
+ "uploadJobExtensionEnabled"
+ "v16@?0@\"PLFeatureAvailability\"8"
+ "v24@?0@\"PHFeatureAvailability\"8@\"NSError\"16"
+ "v24@?0@\"PLFeatureAvailability\"8@\"NSError\"16"
+ "validateSpotlightAvailability"
+ "validateSpotlightIndexForLibraryExistsWithCompletionHandler:"
- "%@, URLRequest: %@ state: %hu clientStatus: %hu lastModifiedDate: %@ attemptCount: %hu"
- "@104@0:8Q16@24Q32B40B44@48@56@64@72@80@88@96"
- "@20@0:8s16"
- "@96@0:8Q16@24Q32B40B44@48@56@64@72@80@88"
- "Current state:%hu and acknowledgement:%hu.\nTarget state:%hu and acknowledgement:%hu.\n"
- "EXAppExtensionAttributes"
- "Error intializing SCSensitivityAnalysis for asset: %{public}@ error: %@ value: %lld"
- "Error intializing SCSensitivityAnalysis for assetID: %{public}@ error: %@ value: %lld"
- "Failed to create AssetResourceUploadJobConfiguration - missing app record"
- "FeatureAvailability - updated availability was nil, initing new"
- "MOC for the watched file system volume is available"
- "No MOC for the watched file system volume"
- "No file system volume for URL %@"
- "No managed object context for %@"
- "Q40@0:8@16@24^@32"
- "T@\"NSURLRequest\",R,N,V_URLRequest"
- "Ts,R,N,V_clientStatus"
- "URLRequest"
- "Watched filesystem volume's MOC is nil."
- "_URLRequest"
- "_acquireSpotlightSandboxExtensionIfNeeded"
- "_countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:"
- "_releaseSpotlightSandboxExtension"
- "_shouldCreateChangeDetailsWithCurrentFetchResultForQuery:"
- "acknowledgeJob:"
- "addObserver:forKeyPath:options:context:"
- "annotatedQueryStringFromSpotlightAttributedQueryString:forSearchQuery:photosEntityStore:photoLibrary:"
- "applicationExtensionRecords"
- "archiveDataForURLRequest:"
- "cancelJob:"
- "configurationStatusWithOptions:"
- "creationRequestForAssetResourceUploadJobConfigurationWithState:"
- "creationRequestForAssetResourceUploadJobWithURLRequest:assetResource:"
- "extensionPointIdentifier"
- "fetchAssetResourceUploadJobsWithAction:options:"
- "initWithApplicationExtensionRecord:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:"
- "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:"
- "maximumUnacknowledgedJobCountKey:"
- "placeholderForCreatedAssetResourceUploadJob"
- "removeObserver:forKeyPath:context:"
- "retryJob:withURLRequest:"
- "sharedFileSystemVolumeManager"
- "unregisterWithVolumeManager"
- "v24@0:8s16s20"

```
