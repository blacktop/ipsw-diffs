## Photos

> `/System/Library/Frameworks/Photos.framework/Photos`

```diff

-802.43.254.0.0
-  __TEXT.__text: 0x28f6e4
-  __TEXT.__auth_stubs: 0x2a90
-  __TEXT.__objc_methlist: 0x2411c
-  __TEXT.__const: 0xf90
+810.40.105.0.0
+  __TEXT.__text: 0x28de54
+  __TEXT.__auth_stubs: 0x2ba0
+  __TEXT.__objc_methlist: 0x241dc
+  __TEXT.__const: 0x11b0
   __TEXT.__dlopen_cstrs: 0x239
-  __TEXT.__constg_swiftt: 0x1dc
-  __TEXT.__swift5_typeref: 0x292
+  __TEXT.__swift5_typeref: 0x35e
   __TEXT.__swift5_reflstr: 0xd1
-  __TEXT.__swift5_fieldmd: 0xb0
-  __TEXT.__swift5_assocty: 0x80
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__cstring: 0x2b7ce
-  __TEXT.__swift5_capture: 0x6c
-  __TEXT.__gcc_except_tab: 0x9cf8
-  __TEXT.__oslogstring: 0x1cceb
+  __TEXT.__swift5_assocty: 0x98
+  __TEXT.__constg_swiftt: 0x38c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_fieldmd: 0xf8
+  __TEXT.__cstring: 0x2bcb9
+  __TEXT.__swift5_capture: 0xac
+  __TEXT.__oslogstring: 0x1c84d
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__gcc_except_tab: 0x98c4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8528
+  __TEXT.__unwind_info: 0x85a0
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x3703
-  __TEXT.__objc_methname: 0x6b7e7
-  __TEXT.__objc_methtype: 0x6d7e
-  __TEXT.__objc_stubs: 0x39be0
-  __DATA_CONST.__got: 0x26e8
-  __DATA_CONST.__const: 0x7f28
-  __DATA_CONST.__objc_classlist: 0xdb8
+  __TEXT.__objc_classname: 0x375b
+  __TEXT.__objc_methname: 0x6b8e6
+  __TEXT.__objc_methtype: 0x6d3b
+  __TEXT.__objc_stubs: 0x39d40
+  __DATA_CONST.__got: 0x2738
+  __DATA_CONST.__const: 0x7f20
+  __DATA_CONST.__objc_classlist: 0xdc0
   __DATA_CONST.__objc_catlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x2e8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f18
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x13008
+  __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xb48
-  __DATA_CONST.__objc_arraydata: 0x950
-  __AUTH_CONST.__auth_got: 0x1558
-  __AUTH_CONST.__const: 0x3bd8
-  __AUTH_CONST.__cfstring: 0x28340
-  __AUTH_CONST.__objc_const: 0x3d3d0
-  __AUTH_CONST.__objc_intobj: 0x2040
-  __AUTH_CONST.__objc_arrayobj: 0x6d8
+  __DATA_CONST.__objc_arraydata: 0x980
+  __AUTH_CONST.__auth_got: 0x15e0
+  __AUTH_CONST.__const: 0x3d78
+  __AUTH_CONST.__cfstring: 0x28500
+  __AUTH_CONST.__objc_const: 0x3d4e8
+  __AUTH_CONST.__objc_intobj: 0x2088
+  __AUTH_CONST.__objc_arrayobj: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x6f10
+  __AUTH.__objc_data: 0x6f60
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x3240
-  __DATA.__data: 0x2898
+  __DATA.__objc_ivar: 0x3250
+  __DATA.__data: 0x29a0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1620
+  __DATA.__bss: 0x18b0
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0x1a38
   __DATA_DIRTY.__data: 0x148

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore
   - /System/Library/Frameworks/ImageIO.framework/ImageIO

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C0628212-6D26-3673-8208-DDE3B011C312
-  Functions: 13488
-  Symbols:   45219
-  CStrings:  28960
+  UUID: 6F085DCD-CB8C-3DDF-B203-FC6AE9BA6025
+  Functions: 13546
+  Symbols:   45295
+  CStrings:  29022
 
Symbols:
+ +[PHAssetResourceUploadJob fetchAssetResourceUploadJobsForConfiguration:options:]
+ +[PHAssetResourceUploadJob fetchAssetResourceUploadJobsWithAction:options:]
+ +[PHAssetResourceUploadJob fetchAssetResourceUploadJobsWithOptions:]
+ +[PHAssetResourceUploadJobChangeRequest _countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:]
+ +[PHAssetResourceUploadJobChangeRequest acknowledgeJob:]
+ +[PHAssetResourceUploadJobChangeRequest cancelJob:]
+ +[PHAssetResourceUploadJobChangeRequest creationRequestForAssetResourceUploadJobWithURLRequest:assetResource:]
+ +[PHAssetResourceUploadJobChangeRequest maximumUnacknowledgedJobCountKey:]
+ +[PHAssetResourceUploadJobChangeRequest retryJob:withURLRequest:]
+ +[PHAssetResourceUploadJobConfiguration configurationStatusWithOptions:]
+ +[PHAssetResourceUploadJobConfigurationChangeRequest creationRequestForAssetResourceUploadJobConfigurationWithState:]
+ +[PHAssetResourceUploadJobConfigurationChangeRequest creationRequestForAssetResourceUploadJobConfiguration]
+ +[PHAssetTextUnderstandingProperties entityName]
+ +[PHAssetTextUnderstandingProperties keyPathFromPrimaryObject]
+ +[PHAssetTextUnderstandingProperties propertiesToFetch]
+ +[PHAssetTextUnderstandingProperties propertySetName]
+ +[PHQuery _queryForAssetResourceUploadJobsWithOptions:configuration:predicate:]
+ +[PHQuery queryForAcknowledgeableAssetResourceUploadJobsWithConfiguration:options:]
+ +[PHQuery queryForAssetResourceUploadJobsWithConfiguration:states:options:]
+ +[PHQuery queryForRetryableAssetResourceUploadJobsWithConfiguration:options:]
+ +[PHSearchResultProcessor searchResultsFromAssetUUIDs:]
+ +[PHSearchSuggestionProcessor _pHSearchSuggestionFromPLSearchSuggestion:rangeOfSuggestionText:]
+ +[PHSearchSuggestionProcessor searchSuggestionsFromPLSearchSuggestions:suggestions:queryId:batchId:rangeOfSuggestionText:]
+ -[PHAsset textUnderstandingProperties]
+ -[PHAssetChangeRequest resetTextUnderstandingAttributes]
+ -[PHAssetChangeRequest setTextUnderstandingData:version:]
+ -[PHAssetResourceUploadJob URLRequest]
+ -[PHAssetResourceUploadJob attemptCount]
+ -[PHAssetResourceUploadJob clientStatus]
+ -[PHAssetResourceUploadJob lastModifiedDate]
+ -[PHAssetResourceUploadJob resource]
+ -[PHAssetResourceUploadJobChangeRequest _commonInitializer]
+ -[PHAssetResourceUploadJobChangeRequest _getAcknowledgement]
+ -[PHAssetResourceUploadJobChangeRequest _getConfigurationFromLibrary:error:]
+ -[PHAssetResourceUploadJobChangeRequest _getState]
+ -[PHAssetResourceUploadJobChangeRequest attemptCount]
+ -[PHAssetResourceUploadJobChangeRequest clientStatus]
+ -[PHAssetResourceUploadJobChangeRequest incrementAttemptCount]
+ -[PHAssetResourceUploadJobChangeRequest initForNewObject]
+ -[PHAssetResourceUploadJobChangeRequest initWithUUID:objectID:]
+ -[PHAssetResourceUploadJobChangeRequest lastModifiedDate]
+ -[PHAssetResourceUploadJobChangeRequest setAttemptCount:]
+ -[PHAssetResourceUploadJobChangeRequest setLastModifiedDate:]
+ -[PHAssetResourceUploadJobChangeRequest setOnlyClientStatus:]
+ -[PHAssetResourceUploadJobChangeRequest setOnlyState:]
+ -[PHAssetResourceUploadJobChangeRequest setState:clientStatus:]
+ -[PHAssetResourceUploadJobChangeRequest updateClientStatus:]
+ -[PHAssetResourceUploadJobChangeRequest updateState:]
+ -[PHAssetResourceUploadJobChangeRequest validateInsertIntoPhotoLibrary:error:]
+ -[PHAssetResourceUploadJobChangeRequest validateMutationsToManagedObject:error:]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest _confirmAppHasValidExtensionWithPhotoLibrary:error:]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest setSkipExtensionValidation:]
+ -[PHAssetResourceUploadJobConfigurationChangeRequest skipExtensionValidation]
+ -[PHAssetTextUnderstandingProperties .cxx_destruct]
+ -[PHAssetTextUnderstandingProperties initWithFetchDictionary:asset:prefetched:]
+ -[PHAssetTextUnderstandingProperties textUnderstandingData]
+ -[PHAssetTextUnderstandingProperties textUnderstandingVersion]
+ -[PHPerformChangesRequest decodeWithService:clientAuthorization:error:]
+ -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:]
+ -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:]
+ GCC_except_table10010
+ GCC_except_table10011
+ GCC_except_table10055
+ GCC_except_table10056
+ GCC_except_table10060
+ GCC_except_table10079
+ GCC_except_table10084
+ GCC_except_table10154
+ GCC_except_table10247
+ GCC_except_table10387
+ GCC_except_table10424
+ GCC_except_table1043
+ GCC_except_table10514
+ GCC_except_table10542
+ GCC_except_table1059
+ GCC_except_table1087
+ GCC_except_table1179
+ GCC_except_table1196
+ GCC_except_table12170
+ GCC_except_table12230
+ GCC_except_table12374
+ GCC_except_table12378
+ GCC_except_table12382
+ GCC_except_table12419
+ GCC_except_table12443
+ GCC_except_table12450
+ GCC_except_table12658
+ GCC_except_table12900
+ GCC_except_table12978
+ GCC_except_table13023
+ GCC_except_table13070
+ GCC_except_table13080
+ GCC_except_table13098
+ GCC_except_table13113
+ GCC_except_table13142
+ GCC_except_table13159
+ GCC_except_table13178
+ GCC_except_table13260
+ GCC_except_table13266
+ GCC_except_table13282
+ GCC_except_table1357
+ GCC_except_table1376
+ GCC_except_table1400
+ GCC_except_table1439
+ GCC_except_table1488
+ GCC_except_table1672
+ GCC_except_table1676
+ GCC_except_table1690
+ GCC_except_table1694
+ GCC_except_table1704
+ GCC_except_table1890
+ GCC_except_table1894
+ GCC_except_table1896
+ GCC_except_table1898
+ GCC_except_table1900
+ GCC_except_table1902
+ GCC_except_table1904
+ GCC_except_table1907
+ GCC_except_table1914
+ GCC_except_table1916
+ GCC_except_table1918
+ GCC_except_table1930
+ GCC_except_table1962
+ GCC_except_table1964
+ GCC_except_table1966
+ GCC_except_table1970
+ GCC_except_table1972
+ GCC_except_table1974
+ GCC_except_table1976
+ GCC_except_table1978
+ GCC_except_table1980
+ GCC_except_table1982
+ GCC_except_table1984
+ GCC_except_table1986
+ GCC_except_table1988
+ GCC_except_table1990
+ GCC_except_table1992
+ GCC_except_table1995
+ GCC_except_table1997
+ GCC_except_table1999
+ GCC_except_table2001
+ GCC_except_table2003
+ GCC_except_table2011
+ GCC_except_table2013
+ GCC_except_table2015
+ GCC_except_table2043
+ GCC_except_table2045
+ GCC_except_table2048
+ GCC_except_table2157
+ GCC_except_table2162
+ GCC_except_table2170
+ GCC_except_table2180
+ GCC_except_table2220
+ GCC_except_table2381
+ GCC_except_table2394
+ GCC_except_table2419
+ GCC_except_table2434
+ GCC_except_table2453
+ GCC_except_table2463
+ GCC_except_table2499
+ GCC_except_table2504
+ GCC_except_table2565
+ GCC_except_table2663
+ GCC_except_table2674
+ GCC_except_table2676
+ GCC_except_table2710
+ GCC_except_table2784
+ GCC_except_table2789
+ GCC_except_table2794
+ GCC_except_table2797
+ GCC_except_table2818
+ GCC_except_table2820
+ GCC_except_table2823
+ GCC_except_table2954
+ GCC_except_table2958
+ GCC_except_table2961
+ GCC_except_table3028
+ GCC_except_table3036
+ GCC_except_table3065
+ GCC_except_table3069
+ GCC_except_table3074
+ GCC_except_table3190
+ GCC_except_table3223
+ GCC_except_table3229
+ GCC_except_table3232
+ GCC_except_table3242
+ GCC_except_table3246
+ GCC_except_table3252
+ GCC_except_table3255
+ GCC_except_table3259
+ GCC_except_table3263
+ GCC_except_table3274
+ GCC_except_table3279
+ GCC_except_table3290
+ GCC_except_table3291
+ GCC_except_table3307
+ GCC_except_table3316
+ GCC_except_table3413
+ GCC_except_table3419
+ GCC_except_table3435
+ GCC_except_table3439
+ GCC_except_table3486
+ GCC_except_table3513
+ GCC_except_table3544
+ GCC_except_table3546
+ GCC_except_table3566
+ GCC_except_table3569
+ GCC_except_table3779
+ GCC_except_table3781
+ GCC_except_table3804
+ GCC_except_table3839
+ GCC_except_table3847
+ GCC_except_table3849
+ GCC_except_table3867
+ GCC_except_table3869
+ GCC_except_table3901
+ GCC_except_table3906
+ GCC_except_table3907
+ GCC_except_table4169
+ GCC_except_table4175
+ GCC_except_table4202
+ GCC_except_table4225
+ GCC_except_table4227
+ GCC_except_table4231
+ GCC_except_table4236
+ GCC_except_table4247
+ GCC_except_table4251
+ GCC_except_table4330
+ GCC_except_table4640
+ GCC_except_table4642
+ GCC_except_table4649
+ GCC_except_table4713
+ GCC_except_table4715
+ GCC_except_table4719
+ GCC_except_table4721
+ GCC_except_table4724
+ GCC_except_table4793
+ GCC_except_table4798
+ GCC_except_table4828
+ GCC_except_table4975
+ GCC_except_table5332
+ GCC_except_table5381
+ GCC_except_table5399
+ GCC_except_table5405
+ GCC_except_table5411
+ GCC_except_table5424
+ GCC_except_table5452
+ GCC_except_table5454
+ GCC_except_table5457
+ GCC_except_table5458
+ GCC_except_table5463
+ GCC_except_table5471
+ GCC_except_table5475
+ GCC_except_table5484
+ GCC_except_table5488
+ GCC_except_table5525
+ GCC_except_table5533
+ GCC_except_table5563
+ GCC_except_table5589
+ GCC_except_table5593
+ GCC_except_table5597
+ GCC_except_table5617
+ GCC_except_table5623
+ GCC_except_table5627
+ GCC_except_table5641
+ GCC_except_table5644
+ GCC_except_table5647
+ GCC_except_table5668
+ GCC_except_table5714
+ GCC_except_table5725
+ GCC_except_table5772
+ GCC_except_table5803
+ GCC_except_table5806
+ GCC_except_table5812
+ GCC_except_table5816
+ GCC_except_table5845
+ GCC_except_table5875
+ GCC_except_table5901
+ GCC_except_table5903
+ GCC_except_table5914
+ GCC_except_table5961
+ GCC_except_table6035
+ GCC_except_table6040
+ GCC_except_table6045
+ GCC_except_table6186
+ GCC_except_table6189
+ GCC_except_table6202
+ GCC_except_table6227
+ GCC_except_table6237
+ GCC_except_table6240
+ GCC_except_table6277
+ GCC_except_table6315
+ GCC_except_table6317
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table6704
+ GCC_except_table6717
+ GCC_except_table6730
+ GCC_except_table6747
+ GCC_except_table6776
+ GCC_except_table6779
+ GCC_except_table6783
+ GCC_except_table6785
+ GCC_except_table6793
+ GCC_except_table6836
+ GCC_except_table6849
+ GCC_except_table6882
+ GCC_except_table6884
+ GCC_except_table6923
+ GCC_except_table696
+ GCC_except_table699
+ GCC_except_table700
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table7183
+ GCC_except_table7184
+ GCC_except_table7194
+ GCC_except_table7201
+ GCC_except_table7217
+ GCC_except_table7219
+ GCC_except_table7220
+ GCC_except_table7221
+ GCC_except_table7223
+ GCC_except_table7235
+ GCC_except_table7236
+ GCC_except_table7237
+ GCC_except_table7394
+ GCC_except_table7612
+ GCC_except_table7638
+ GCC_except_table7657
+ GCC_except_table7659
+ GCC_except_table7660
+ GCC_except_table7721
+ GCC_except_table774
+ GCC_except_table7743
+ GCC_except_table7747
+ GCC_except_table7753
+ GCC_except_table7806
+ GCC_except_table783
+ GCC_except_table7966
+ GCC_except_table7968
+ GCC_except_table8015
+ GCC_except_table8055
+ GCC_except_table8059
+ GCC_except_table8061
+ GCC_except_table8063
+ GCC_except_table8075
+ GCC_except_table8120
+ GCC_except_table8148
+ GCC_except_table8273
+ GCC_except_table8331
+ GCC_except_table8351
+ GCC_except_table8354
+ GCC_except_table8373
+ GCC_except_table8435
+ GCC_except_table8439
+ GCC_except_table8443
+ GCC_except_table8452
+ GCC_except_table8454
+ GCC_except_table8494
+ GCC_except_table8558
+ GCC_except_table871
+ GCC_except_table8715
+ GCC_except_table8756
+ GCC_except_table9006
+ GCC_except_table9010
+ GCC_except_table9014
+ GCC_except_table9034
+ GCC_except_table9035
+ GCC_except_table9127
+ GCC_except_table9137
+ GCC_except_table9169
+ GCC_except_table919
+ GCC_except_table9221
+ GCC_except_table9261
+ GCC_except_table9281
+ GCC_except_table9308
+ GCC_except_table9333
+ GCC_except_table9366
+ GCC_except_table9368
+ GCC_except_table9458
+ GCC_except_table9549
+ GCC_except_table9668
+ GCC_except_table9682
+ GCC_except_table9683
+ GCC_except_table9693
+ GCC_except_table9716
+ GCC_except_table9717
+ GCC_except_table9718
+ GCC_except_table9719
+ GCC_except_table9720
+ GCC_except_table9721
+ GCC_except_table9722
+ GCC_except_table9737
+ GCC_except_table9747
+ GCC_except_table9909
+ GCC_except_table9918
+ GCC_except_table9919
+ GCC_except_table9920
+ GCC_except_table9921
+ GCC_except_table9922
+ GCC_except_table9932
+ GCC_except_table9950
+ GCC_except_table9976
+ GCC_except_table9977
+ GCC_except_table9990
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_PHAssetTextUnderstandingProperties
+ _OBJC_CLASS_$_PHSearchSuggestionProcessor
+ _OBJC_CLASS_$_PLResourceRecipeGenerationOptions
+ _OBJC_CLASS_$__EXExtensionIdentity
+ _OBJC_IVAR_$_PHAssetChangeRequest._didSetTextUnderstandingProperties
+ _OBJC_IVAR_$_PHAssetChangeRequest._resetTextUnderstandingProperties
+ _OBJC_IVAR_$_PHAssetChangeRequest._textUnderstandingData
+ _OBJC_IVAR_$_PHAssetChangeRequest._textUnderstandingVersion
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._URLRequest
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._attemptCount
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._clientStatus
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._lastModifiedDate
+ _OBJC_IVAR_$_PHAssetResourceUploadJob._resource
+ _OBJC_IVAR_$_PHAssetResourceUploadJobChangeRequest._incrementAttemptCount
+ _OBJC_IVAR_$_PHAssetResourceUploadJobChangeRequest._shouldBypassValidateMutations
+ _OBJC_IVAR_$_PHAssetResourceUploadJobConfigurationChangeRequest._bundleIdentifier
+ _OBJC_IVAR_$_PHAssetResourceUploadJobConfigurationChangeRequest._skipExtensionValidation
+ _OBJC_IVAR_$_PHAssetTextUnderstandingProperties._textUnderstandingData
+ _OBJC_IVAR_$_PHAssetTextUnderstandingProperties._textUnderstandingVersion
+ _OBJC_METACLASS_$_PHAssetTextUnderstandingProperties
+ _OBJC_METACLASS_$_PHSearchSuggestionProcessor
+ _PHAssetPropertySetTextUnderstanding
+ _PLResourceBackgroundUploadExtensionPointLabel
+ _PLSpotlightSearchResultContentTypePerson
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19122
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22362
+ _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36467
+ __INSTANCE_METHODS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration
+ __IVARS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration
+ __OBJC_$_CLASS_METHODS_PHAssetTextUnderstandingProperties
+ __OBJC_$_CLASS_METHODS_PHSearchSuggestionProcessor
+ __OBJC_$_CLASS_PROP_LIST_PHAssetPropertySet.2617
+ __OBJC_$_INSTANCE_METHODS_PHAssetTextUnderstandingProperties
+ __OBJC_$_INSTANCE_VARIABLES_PHAssetTextUnderstandingProperties
+ __OBJC_$_PROP_LIST_PHAssetPropertySet.2624
+ __OBJC_$_PROP_LIST_PHAssetTextUnderstandingProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLBackgroundResourceUploadExtensionXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PLBackgroundResourceUploadExtensionXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_PLBackgroundResourceUploadExtensionXPCProtocol
+ __OBJC_CLASS_RO_$_PHAssetTextUnderstandingProperties
+ __OBJC_CLASS_RO_$_PHSearchSuggestionProcessor
+ __OBJC_LABEL_PROTOCOL_$_PLBackgroundResourceUploadExtensionXPCProtocol
+ __OBJC_METACLASS_RO_$_PHAssetTextUnderstandingProperties
+ __OBJC_METACLASS_RO_$_PHSearchSuggestionProcessor
+ __OBJC_PROTOCOL_$_PLBackgroundResourceUploadExtensionXPCProtocol
+ __PROTOCOLS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration
+ __PROTOCOLS__TtC6PhotosP33_418ED0618F5CF054A91C652800E0906849_PHBackgroundResourceUploadExtensionConfiguration.1
+ ___110+[PHAssetResourceUploadJobChangeRequest _countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:]_block_invoke
+ ___122+[PHSearchSuggestionProcessor searchSuggestionsFromPLSearchSuggestions:suggestions:queryId:batchId:rangeOfSuggestionText:]_block_invoke
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke.111
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_2.112
+ ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_3.114
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.157
+ ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.158
+ ___156-[PHServerResourceRequestRunner startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:]_block_invoke.153
+ ___37+[PHAsset propertiesToFetchWithHint:]_block_invoke.596
+ ___39-[PHAsset _createKeywordPropertyObject]_block_invoke.868
+ ___55+[PHAssetTextUnderstandingProperties propertiesToFetch]_block_invoke
+ ___61-[PHSearchQuery _executeSpotlightSearchWithResultsHandlerV2:]_block_invoke.172
+ ___64+[PHQuery queryForAssetCollectionsWithLocalIdentifiers:options:]_block_invoke
+ ___78-[PHAssetResourceUploadJobChangeRequest validateInsertIntoPhotoLibrary:error:]_block_invoke
+ ___81+[PHAssetResourceUploadJob fetchAssetResourceUploadJobsForConfiguration:options:]_block_invoke
+ ___84+[PHSearchUtility insertSpacingIfNeededBetweenAnnotationsAndPlainTextInQueryString:]_block_invoke.130
+ ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.129
+ ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.137
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke.126
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_2.128
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_3.129
+ ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_4.130
+ ___Block_byref_object_copy_.10325
+ ___Block_byref_object_copy_.11071
+ ___Block_byref_object_copy_.11345
+ ___Block_byref_object_copy_.11504
+ ___Block_byref_object_copy_.12348
+ ___Block_byref_object_copy_.12613
+ ___Block_byref_object_copy_.13087
+ ___Block_byref_object_copy_.13561
+ ___Block_byref_object_copy_.1418
+ ___Block_byref_object_copy_.14776
+ ___Block_byref_object_copy_.1490
+ ___Block_byref_object_copy_.15511
+ ___Block_byref_object_copy_.17451
+ ___Block_byref_object_copy_.18428
+ ___Block_byref_object_copy_.1945
+ ___Block_byref_object_copy_.20092
+ ___Block_byref_object_copy_.20258
+ ___Block_byref_object_copy_.20580
+ ___Block_byref_object_copy_.21047
+ ___Block_byref_object_copy_.21653
+ ___Block_byref_object_copy_.22175
+ ___Block_byref_object_copy_.22369
+ ___Block_byref_object_copy_.2345
+ ___Block_byref_object_copy_.24196
+ ___Block_byref_object_copy_.25072
+ ___Block_byref_object_copy_.26755
+ ___Block_byref_object_copy_.27278
+ ___Block_byref_object_copy_.2778
+ ___Block_byref_object_copy_.28005
+ ___Block_byref_object_copy_.28295
+ ___Block_byref_object_copy_.29819
+ ___Block_byref_object_copy_.30791
+ ___Block_byref_object_copy_.31536
+ ___Block_byref_object_copy_.31830
+ ___Block_byref_object_copy_.3308
+ ___Block_byref_object_copy_.33209
+ ___Block_byref_object_copy_.33783
+ ___Block_byref_object_copy_.34346
+ ___Block_byref_object_copy_.34537
+ ___Block_byref_object_copy_.34975
+ ___Block_byref_object_copy_.35554
+ ___Block_byref_object_copy_.35832
+ ___Block_byref_object_copy_.36764
+ ___Block_byref_object_copy_.37244
+ ___Block_byref_object_copy_.38846
+ ___Block_byref_object_copy_.3907
+ ___Block_byref_object_copy_.39403
+ ___Block_byref_object_copy_.43467
+ ___Block_byref_object_copy_.43891
+ ___Block_byref_object_copy_.44102
+ ___Block_byref_object_copy_.44331
+ ___Block_byref_object_copy_.45671
+ ___Block_byref_object_copy_.46079
+ ___Block_byref_object_copy_.46598
+ ___Block_byref_object_copy_.46900
+ ___Block_byref_object_copy_.47276
+ ___Block_byref_object_copy_.47763
+ ___Block_byref_object_copy_.48273
+ ___Block_byref_object_copy_.49151
+ ___Block_byref_object_copy_.49349
+ ___Block_byref_object_copy_.49559
+ ___Block_byref_object_copy_.49596
+ ___Block_byref_object_copy_.51767
+ ___Block_byref_object_copy_.52067
+ ___Block_byref_object_copy_.52800
+ ___Block_byref_object_copy_.53601
+ ___Block_byref_object_copy_.5447
+ ___Block_byref_object_copy_.6498
+ ___Block_byref_object_copy_.6970
+ ___Block_byref_object_copy_.8440
+ ___Block_byref_object_copy_.8765
+ ___Block_byref_object_copy_.900
+ ___Block_byref_object_copy_.9057
+ ___Block_byref_object_copy_.9625
+ ___Block_byref_object_dispose_.10326
+ ___Block_byref_object_dispose_.11072
+ ___Block_byref_object_dispose_.11346
+ ___Block_byref_object_dispose_.11505
+ ___Block_byref_object_dispose_.12349
+ ___Block_byref_object_dispose_.12614
+ ___Block_byref_object_dispose_.13088
+ ___Block_byref_object_dispose_.13562
+ ___Block_byref_object_dispose_.1419
+ ___Block_byref_object_dispose_.14777
+ ___Block_byref_object_dispose_.1491
+ ___Block_byref_object_dispose_.15512
+ ___Block_byref_object_dispose_.17452
+ ___Block_byref_object_dispose_.18429
+ ___Block_byref_object_dispose_.1946
+ ___Block_byref_object_dispose_.20093
+ ___Block_byref_object_dispose_.20259
+ ___Block_byref_object_dispose_.20581
+ ___Block_byref_object_dispose_.21048
+ ___Block_byref_object_dispose_.21654
+ ___Block_byref_object_dispose_.22176
+ ___Block_byref_object_dispose_.22370
+ ___Block_byref_object_dispose_.2346
+ ___Block_byref_object_dispose_.24197
+ ___Block_byref_object_dispose_.25073
+ ___Block_byref_object_dispose_.26756
+ ___Block_byref_object_dispose_.27279
+ ___Block_byref_object_dispose_.2779
+ ___Block_byref_object_dispose_.28006
+ ___Block_byref_object_dispose_.28296
+ ___Block_byref_object_dispose_.29820
+ ___Block_byref_object_dispose_.30792
+ ___Block_byref_object_dispose_.31537
+ ___Block_byref_object_dispose_.31831
+ ___Block_byref_object_dispose_.3309
+ ___Block_byref_object_dispose_.33210
+ ___Block_byref_object_dispose_.33784
+ ___Block_byref_object_dispose_.34347
+ ___Block_byref_object_dispose_.34538
+ ___Block_byref_object_dispose_.34976
+ ___Block_byref_object_dispose_.35555
+ ___Block_byref_object_dispose_.35833
+ ___Block_byref_object_dispose_.36765
+ ___Block_byref_object_dispose_.37245
+ ___Block_byref_object_dispose_.38847
+ ___Block_byref_object_dispose_.3908
+ ___Block_byref_object_dispose_.39404
+ ___Block_byref_object_dispose_.43468
+ ___Block_byref_object_dispose_.43892
+ ___Block_byref_object_dispose_.44103
+ ___Block_byref_object_dispose_.44332
+ ___Block_byref_object_dispose_.45672
+ ___Block_byref_object_dispose_.46080
+ ___Block_byref_object_dispose_.46599
+ ___Block_byref_object_dispose_.46901
+ ___Block_byref_object_dispose_.47277
+ ___Block_byref_object_dispose_.47764
+ ___Block_byref_object_dispose_.48274
+ ___Block_byref_object_dispose_.49152
+ ___Block_byref_object_dispose_.49350
+ ___Block_byref_object_dispose_.49560
+ ___Block_byref_object_dispose_.49597
+ ___Block_byref_object_dispose_.51768
+ ___Block_byref_object_dispose_.52068
+ ___Block_byref_object_dispose_.52801
+ ___Block_byref_object_dispose_.53602
+ ___Block_byref_object_dispose_.5448
+ ___Block_byref_object_dispose_.6499
+ ___Block_byref_object_dispose_.6971
+ ___Block_byref_object_dispose_.8441
+ ___Block_byref_object_dispose_.8766
+ ___Block_byref_object_dispose_.901
+ ___Block_byref_object_dispose_.9058
+ ___Block_byref_object_dispose_.9626
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.19123
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.22363
+ ___SensitiveContentAnalysisLibraryCore_block_invoke.36468
+ ____fetchTypeForAssetCollectionLocalIdentifierCode_block_invoke
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r88r_e40_v32?0"<PHInsertChangeRequest>"8Q16^B24ls32l8s40l8r72l8r80l8s48l8s56l8s64l8r88l8
+ ___block_literal_global.1001
+ ___block_literal_global.1003
+ ___block_literal_global.1009
+ ___block_literal_global.1011
+ ___block_literal_global.1013
+ ___block_literal_global.1015
+ ___block_literal_global.1017
+ ___block_literal_global.1019
+ ___block_literal_global.1021
+ ___block_literal_global.1023
+ ___block_literal_global.1025
+ ___block_literal_global.1027
+ ___block_literal_global.1029
+ ___block_literal_global.1031
+ ___block_literal_global.1033
+ ___block_literal_global.1035
+ ___block_literal_global.1037
+ ___block_literal_global.1039
+ ___block_literal_global.1041
+ ___block_literal_global.1041.36649
+ ___block_literal_global.1043
+ ___block_literal_global.1045
+ ___block_literal_global.10455
+ ___block_literal_global.1047
+ ___block_literal_global.1049
+ ___block_literal_global.1051
+ ___block_literal_global.1053
+ ___block_literal_global.1053.36648
+ ___block_literal_global.1055
+ ___block_literal_global.1057
+ ___block_literal_global.1059
+ ___block_literal_global.1061
+ ___block_literal_global.1063.36645
+ ___block_literal_global.1065
+ ___block_literal_global.1065.36643
+ ___block_literal_global.1067
+ ___block_literal_global.1069
+ ___block_literal_global.1071
+ ___block_literal_global.1073
+ ___block_literal_global.1075
+ ___block_literal_global.1077
+ ___block_literal_global.1079
+ ___block_literal_global.1081
+ ___block_literal_global.1083
+ ___block_literal_global.1085
+ ___block_literal_global.1087
+ ___block_literal_global.1089
+ ___block_literal_global.1093
+ ___block_literal_global.1095
+ ___block_literal_global.1097
+ ___block_literal_global.1099
+ ___block_literal_global.1099.36641
+ ___block_literal_global.1101
+ ___block_literal_global.1103
+ ___block_literal_global.1105
+ ___block_literal_global.1107
+ ___block_literal_global.1109
+ ___block_literal_global.1111
+ ___block_literal_global.1113
+ ___block_literal_global.1115
+ ___block_literal_global.11166
+ ___block_literal_global.1117
+ ___block_literal_global.1119
+ ___block_literal_global.112.41158
+ ___block_literal_global.1121
+ ___block_literal_global.1123
+ ___block_literal_global.1125
+ ___block_literal_global.1127
+ ___block_literal_global.1129
+ ___block_literal_global.1131
+ ___block_literal_global.1133
+ ___block_literal_global.1135
+ ___block_literal_global.11361
+ ___block_literal_global.1137
+ ___block_literal_global.1139
+ ___block_literal_global.1141
+ ___block_literal_global.1143
+ ___block_literal_global.1145
+ ___block_literal_global.1147
+ ___block_literal_global.1149
+ ___block_literal_global.1151
+ ___block_literal_global.1153
+ ___block_literal_global.1155
+ ___block_literal_global.1157
+ ___block_literal_global.1159
+ ___block_literal_global.1161
+ ___block_literal_global.1163
+ ___block_literal_global.1165
+ ___block_literal_global.1167
+ ___block_literal_global.1169
+ ___block_literal_global.1171
+ ___block_literal_global.11738
+ ___block_literal_global.1184
+ ___block_literal_global.1186
+ ___block_literal_global.1188
+ ___block_literal_global.1190
+ ___block_literal_global.1192
+ ___block_literal_global.1194
+ ___block_literal_global.1196
+ ___block_literal_global.1198
+ ___block_literal_global.1200
+ ___block_literal_global.1202
+ ___block_literal_global.1204
+ ___block_literal_global.1206
+ ___block_literal_global.1208
+ ___block_literal_global.1210
+ ___block_literal_global.1212
+ ___block_literal_global.1214
+ ___block_literal_global.1216
+ ___block_literal_global.1218
+ ___block_literal_global.1220
+ ___block_literal_global.1222
+ ___block_literal_global.1224
+ ___block_literal_global.1226
+ ___block_literal_global.1228
+ ___block_literal_global.1230
+ ___block_literal_global.1236
+ ___block_literal_global.12670
+ ___block_literal_global.13381
+ ___block_literal_global.134.47823
+ ___block_literal_global.13563
+ ___block_literal_global.14128
+ ___block_literal_global.1438
+ ___block_literal_global.14451
+ ___block_literal_global.146.38814
+ ___block_literal_global.148
+ ___block_literal_global.14844
+ ___block_literal_global.15496
+ ___block_literal_global.17032
+ ___block_literal_global.1740
+ ___block_literal_global.1744
+ ___block_literal_global.1751
+ ___block_literal_global.17685
+ ___block_literal_global.18457
+ ___block_literal_global.18508
+ ___block_literal_global.1956
+ ___block_literal_global.19692
+ ___block_literal_global.20010
+ ___block_literal_global.20596
+ ___block_literal_global.206.28578
+ ___block_literal_global.206.29485
+ ___block_literal_global.210.29488
+ ___block_literal_global.21022
+ ___block_literal_global.212.29489
+ ___block_literal_global.217.13933
+ ___block_literal_global.21962
+ ___block_literal_global.224.14732
+ ___block_literal_global.22837
+ ___block_literal_global.234.34070
+ ___block_literal_global.2375
+ ___block_literal_global.240
+ ___block_literal_global.24105
+ ___block_literal_global.25431
+ ___block_literal_global.2594
+ ___block_literal_global.26097
+ ___block_literal_global.2662
+ ___block_literal_global.26979
+ ___block_literal_global.2762
+ ___block_literal_global.27708
+ ___block_literal_global.2775
+ ___block_literal_global.27982
+ ___block_literal_global.2833
+ ___block_literal_global.28609
+ ___block_literal_global.2863
+ ___block_literal_global.28880
+ ___block_literal_global.28959
+ ___block_literal_global.2937
+ ___block_literal_global.29474
+ ___block_literal_global.29936
+ ___block_literal_global.3.11366
+ ___block_literal_global.3.2774
+ ___block_literal_global.30321
+ ___block_literal_global.30518
+ ___block_literal_global.30802
+ ___block_literal_global.3116
+ ___block_literal_global.31219
+ ___block_literal_global.3168
+ ___block_literal_global.3186
+ ___block_literal_global.32063
+ ___block_literal_global.3207
+ ___block_literal_global.32207
+ ___block_literal_global.3235
+ ___block_literal_global.3256
+ ___block_literal_global.32680
+ ___block_literal_global.3298
+ ___block_literal_global.33294
+ ___block_literal_global.3349
+ ___block_literal_global.3385
+ ___block_literal_global.34073
+ ___block_literal_global.34360
+ ___block_literal_global.3440
+ ___block_literal_global.34482
+ ___block_literal_global.34634
+ ___block_literal_global.3479
+ ___block_literal_global.348.19584
+ ___block_literal_global.34817
+ ___block_literal_global.3512
+ ___block_literal_global.35292
+ ___block_literal_global.3535
+ ___block_literal_global.35837
+ ___block_literal_global.3597
+ ___block_literal_global.36342
+ ___block_literal_global.37.32109
+ ___block_literal_global.37.47395
+ ___block_literal_global.37110
+ ___block_literal_global.37305
+ ___block_literal_global.37850
+ ___block_literal_global.3814
+ ___block_literal_global.38157
+ ___block_literal_global.3858
+ ___block_literal_global.38889
+ ___block_literal_global.39147
+ ___block_literal_global.39576
+ ___block_literal_global.3971
+ ___block_literal_global.40156
+ ___block_literal_global.40370
+ ___block_literal_global.40856
+ ___block_literal_global.41164
+ ___block_literal_global.4234
+ ___block_literal_global.42474
+ ___block_literal_global.4274
+ ___block_literal_global.4297
+ ___block_literal_global.43057
+ ___block_literal_global.43470
+ ___block_literal_global.4349
+ ___block_literal_global.4380
+ ___block_literal_global.44157
+ ___block_literal_global.4430
+ ___block_literal_global.44348
+ ___block_literal_global.4495
+ ___block_literal_global.44969
+ ___block_literal_global.4537
+ ___block_literal_global.4568
+ ___block_literal_global.45756
+ ___block_literal_global.4585
+ ___block_literal_global.46111
+ ___block_literal_global.4616
+ ___block_literal_global.4622
+ ___block_literal_global.4634
+ ___block_literal_global.4637
+ ___block_literal_global.4639
+ ___block_literal_global.46429
+ ___block_literal_global.46520
+ ___block_literal_global.4660
+ ___block_literal_global.4678
+ ___block_literal_global.4689
+ ___block_literal_global.4704
+ ___block_literal_global.4715
+ ___block_literal_global.47184
+ ___block_literal_global.4729
+ ___block_literal_global.47402
+ ___block_literal_global.47842
+ ___block_literal_global.47990
+ ___block_literal_global.4803
+ ___block_literal_global.4812
+ ___block_literal_global.48764
+ ___block_literal_global.49116
+ ___block_literal_global.49561
+ ___block_literal_global.49609
+ ___block_literal_global.49918
+ ___block_literal_global.50.26065
+ ___block_literal_global.50191
+ ___block_literal_global.51503
+ ___block_literal_global.52887
+ ___block_literal_global.53455
+ ___block_literal_global.5480
+ ___block_literal_global.549
+ ___block_literal_global.554
+ ___block_literal_global.593
+ ___block_literal_global.62.1416
+ ___block_literal_global.648
+ ___block_literal_global.651
+ ___block_literal_global.6585
+ ___block_literal_global.678.36837
+ ___block_literal_global.688
+ ___block_literal_global.6977
+ ___block_literal_global.727
+ ___block_literal_global.7648
+ ___block_literal_global.7871
+ ___block_literal_global.8041
+ ___block_literal_global.85.53433
+ ___block_literal_global.851
+ ___block_literal_global.871
+ ___block_literal_global.8757
+ ___block_literal_global.8844
+ ___block_literal_global.9295
+ ___block_literal_global.975
+ ___block_literal_global.98
+ ___block_literal_global.980.13075
+ ___block_literal_global.991
+ ___block_literal_global.993
+ ___block_literal_global.995
+ ___block_literal_global.997
+ ___block_literal_global.999
+ ___getSCSensitivityAnalysisClass_block_invoke.19121
+ ___getSCSensitivityAnalysisClass_block_invoke.22361
+ ___getSCSensitivityAnalysisClass_block_invoke.36466
+ ___handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier_block_invoke
+ ___swift_instantiateGenericMetadata
+ ___unnamed_5
+ __currentTimestampString.s_formatter.47396
+ __currentTimestampString.s_onceToken.47394
+ __fetchTypeForAssetCollectionLocalIdentifierCode
+ __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_object_34
+ __fetchTypeForAssetCollectionLocalIdentifierCode.pl_once_token_34
+ __swiftImmortalRefCount
+ __swift_stdlib_reportUnimplementedInitializer
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_73
+ _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_73
+ _allowedInfoKeys.allowedKeys.1549
+ _allowedInfoKeys.allowedKeys.18710
+ _allowedInfoKeys.allowedKeys.40661
+ _allowedInfoKeys.onceToken.1548
+ _allowedInfoKeys.onceToken.18709
+ _allowedInfoKeys.onceToken.40660
+ _associated conformance 6Photos42PHBackgroundResourceUploadProcessingResultOSHAASQ
+ _audit_stringSensitiveContentAnalysis.19132
+ _audit_stringSensitiveContentAnalysis.22367
+ _audit_stringSensitiveContentAnalysis.36478
+ _block_copy_helper.7
+ _block_descriptor.9
+ _block_destroy_helper.8
+ _corePropertiesToFetch.array.22840
+ _corePropertiesToFetch.array.28606
+ _corePropertiesToFetch.array.34074
+ _corePropertiesToFetch.onceToken.22839
+ _corePropertiesToFetch.onceToken.28605
+ _corePropertiesToFetch.onceToken.34072
+ _defaultManager.onceToken.51849
+ _entityKeyMap.pl_once_object_15.11147
+ _entityKeyMap.pl_once_object_15.11749
+ _entityKeyMap.pl_once_object_15.1226
+ _entityKeyMap.pl_once_object_15.13372
+ _entityKeyMap.pl_once_object_15.13669
+ _entityKeyMap.pl_once_object_15.1434
+ _entityKeyMap.pl_once_object_15.1850
+ _entityKeyMap.pl_once_object_15.27699
+ _entityKeyMap.pl_once_object_15.28970
+ _entityKeyMap.pl_once_object_15.32671
+ _entityKeyMap.pl_once_object_15.36332
+ _entityKeyMap.pl_once_object_15.40188
+ _entityKeyMap.pl_once_object_15.44371
+ _entityKeyMap.pl_once_object_15.46102
+ _entityKeyMap.pl_once_object_15.4629
+ _entityKeyMap.pl_once_object_15.46512
+ _entityKeyMap.pl_once_object_15.47987
+ _entityKeyMap.pl_once_object_15.50066
+ _entityKeyMap.pl_once_object_15.50985
+ _entityKeyMap.pl_once_object_15.7877
+ _entityKeyMap.pl_once_object_16.34062
+ _entityKeyMap.pl_once_object_16.34472
+ _entityKeyMap.pl_once_object_16.40357
+ _entityKeyMap.pl_once_object_16.4222
+ _entityKeyMap.pl_once_object_16.47172
+ _entityKeyMap.pl_once_object_16.53442
+ _entityKeyMap.pl_once_token_15.11146
+ _entityKeyMap.pl_once_token_15.11748
+ _entityKeyMap.pl_once_token_15.1225
+ _entityKeyMap.pl_once_token_15.13371
+ _entityKeyMap.pl_once_token_15.13668
+ _entityKeyMap.pl_once_token_15.1433
+ _entityKeyMap.pl_once_token_15.1849
+ _entityKeyMap.pl_once_token_15.27698
+ _entityKeyMap.pl_once_token_15.28969
+ _entityKeyMap.pl_once_token_15.32670
+ _entityKeyMap.pl_once_token_15.36331
+ _entityKeyMap.pl_once_token_15.40187
+ _entityKeyMap.pl_once_token_15.44370
+ _entityKeyMap.pl_once_token_15.46101
+ _entityKeyMap.pl_once_token_15.4628
+ _entityKeyMap.pl_once_token_15.46511
+ _entityKeyMap.pl_once_token_15.47986
+ _entityKeyMap.pl_once_token_15.50065
+ _entityKeyMap.pl_once_token_15.50984
+ _entityKeyMap.pl_once_token_15.7876
+ _entityKeyMap.pl_once_token_16.34061
+ _entityKeyMap.pl_once_token_16.34471
+ _entityKeyMap.pl_once_token_16.40356
+ _entityKeyMap.pl_once_token_16.4221
+ _entityKeyMap.pl_once_token_16.47171
+ _entityKeyMap.pl_once_token_16.53441
+ _getSCSensitivityAnalysisClass.19119
+ _getSCSensitivityAnalysisClass.36462
+ _getSCSensitivityAnalysisClass.softClass.19120
+ _getSCSensitivityAnalysisClass.softClass.22360
+ _getSCSensitivityAnalysisClass.softClass.36465
+ _get_witness_table 6Photos35PHBackgroundResourceUploadExtensionRzlAA01_bcdE13Configuration33_418ED0618F5CF054A91C652800E09068LLCyxGAA0bcdeF0HPyHC.2
+ _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_object_47
+ _handleUnsupportedAssetCollectionFetchTypeForLocalIdentifier.pl_once_token_47
+ _identifierPropertiesToFetch.array.35293
+ _identifierPropertiesToFetch.onceToken.35291
+ _objc_allocWithZone
+ _objc_msgSend$_commonInitializer
+ _objc_msgSend$_confirmAppHasValidExtensionWithPhotoLibrary:error:
+ _objc_msgSend$_countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:
+ _objc_msgSend$_getAcknowledgement
+ _objc_msgSend$_getConfigurationFromLibrary:error:
+ _objc_msgSend$_getState
+ _objc_msgSend$_queryForAssetResourceUploadJobsWithOptions:configuration:predicate:
+ _objc_msgSend$applicationExtensionRecords
+ _objc_msgSend$archiveDataForURLRequest:
+ _objc_msgSend$attemptCount
+ _objc_msgSend$changeRequestForUploadJob:
+ _objc_msgSend$clientStatus
+ _objc_msgSend$configurationWithBundleIdentifier:managedObjectContext:error:
+ _objc_msgSend$configurationWithObjectID:managedObjectContext:error:
+ _objc_msgSend$configurationWithUUID:managedObjectContext:error:
+ _objc_msgSend$decodeData:error:
+ _objc_msgSend$extensionPointIdentifier
+ _objc_msgSend$fetchAssetResourceUploadJobConfigurationsWithOptions:
+ _objc_msgSend$fetchAssetResourceUploadJobsForConfiguration:options:
+ _objc_msgSend$generateAndStoreForAsset:options:progress:completion:
+ _objc_msgSend$getCPLConfigurationValueForKey:completionHandler:
+ _objc_msgSend$incrementAttemptCount
+ _objc_msgSend$initWithApplicationExtensionRecord:
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:
+ _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:
+ _objc_msgSend$initWithVersion:taskIdentifier:reason:networkAccessAllowed:clientBundleID:
+ _objc_msgSend$insertIntoManagedObjectContext:uuid:bundleID:
+ _objc_msgSend$isUnitTesting
+ _objc_msgSend$longValue
+ _objc_msgSend$maximumUnacknowledgedJobCountKey:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$predicateForAcknowledgeableJobs
+ _objc_msgSend$processPairingForGroupIDs:inContext:error:
+ _objc_msgSend$queryForAcknowledgeableAssetResourceUploadJobsWithConfiguration:options:
+ _objc_msgSend$queryForAssetResourceUploadJobsWithConfiguration:states:options:
+ _objc_msgSend$queryForRetryableAssetResourceUploadJobsWithConfiguration:options:
+ _objc_msgSend$resetTextUnderstandingAttributes
+ _objc_msgSend$setAttemptCount:
+ _objc_msgSend$setOnlyClientStatus:
+ _objc_msgSend$setOnlyState:
+ _objc_msgSend$setTextUnderstandingData:version:
+ _objc_msgSend$skipExtensionValidation
+ _objc_msgSend$textUnderstandingData
+ _objc_msgSend$textUnderstandingVersion
+ _objc_msgSend$typesMaskForDeferredProcessingNeeded:
+ _objc_msgSend$updateClientStatus:
+ _objc_msgSend$updateState:
+ _propertiesToFetch.pl_once_object_24.33779
+ _propertiesToFetch.pl_once_object_72
+ _propertiesToFetch.pl_once_object_79
+ _propertiesToFetch.pl_once_token_24.33778
+ _propertiesToFetch.pl_once_token_72
+ _propertiesToFetch.pl_once_token_79
+ _propertiesToFetchWithHint:.array.11162
+ _propertiesToFetchWithHint:.array.11756
+ _propertiesToFetchWithHint:.array.13692
+ _propertiesToFetchWithHint:.array.1439
+ _propertiesToFetchWithHint:.array.23334
+ _propertiesToFetchWithHint:.array.27709
+ _propertiesToFetchWithHint:.array.28980
+ _propertiesToFetchWithHint:.array.32681
+ _propertiesToFetchWithHint:.array.36343
+ _propertiesToFetchWithHint:.array.40209
+ _propertiesToFetchWithHint:.array.46112
+ _propertiesToFetchWithHint:.array.47991
+ _propertiesToFetchWithHint:.array.50079
+ _propertiesToFetchWithHint:.array.51013
+ _propertiesToFetchWithHint:.array.7905
+ _propertiesToFetchWithHint:.onceToken.11161
+ _propertiesToFetchWithHint:.onceToken.11755
+ _propertiesToFetchWithHint:.onceToken.1235
+ _propertiesToFetchWithHint:.onceToken.13380
+ _propertiesToFetchWithHint:.onceToken.13691
+ _propertiesToFetchWithHint:.onceToken.1437
+ _propertiesToFetchWithHint:.onceToken.22833
+ _propertiesToFetchWithHint:.onceToken.23333
+ _propertiesToFetchWithHint:.onceToken.27707
+ _propertiesToFetchWithHint:.onceToken.28608
+ _propertiesToFetchWithHint:.onceToken.28979
+ _propertiesToFetchWithHint:.onceToken.32679
+ _propertiesToFetchWithHint:.onceToken.34066
+ _propertiesToFetchWithHint:.onceToken.36341
+ _propertiesToFetchWithHint:.onceToken.40208
+ _propertiesToFetchWithHint:.onceToken.4232
+ _propertiesToFetchWithHint:.onceToken.46110
+ _propertiesToFetchWithHint:.onceToken.47989
+ _propertiesToFetchWithHint:.onceToken.50078
+ _propertiesToFetchWithHint:.onceToken.51012
+ _propertiesToFetchWithHint:.onceToken.7904
+ _propertiesToFetchWithHint:.pl_once_object_15.34483
+ _propertiesToFetchWithHint:.pl_once_object_15.40371
+ _propertiesToFetchWithHint:.pl_once_object_15.47185
+ _propertiesToFetchWithHint:.pl_once_object_15.53456
+ _propertiesToFetchWithHint:.pl_once_token_15.34481
+ _propertiesToFetchWithHint:.pl_once_token_15.40369
+ _propertiesToFetchWithHint:.pl_once_token_15.47183
+ _propertiesToFetchWithHint:.pl_once_token_15.53454
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.13383
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.22835
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.28611
+ _propertiesToFetchWithHint:.propertiesToFetchByHint.34068
+ _propertiesToFetchWithHint:.propertyQueue.13382
+ _propertiesToFetchWithHint:.propertyQueue.22834
+ _propertiesToFetchWithHint:.propertyQueue.28610
+ _propertiesToFetchWithHint:.propertyQueue.34067
+ _propertiesToPrefetch.onceToken.22374
+ _propertiesToPrefetch.onceToken.28274
+ _propertiesToPrefetch.onceToken.33760
+ _propertiesToPrefetch.propertiesToPrefetch.22375
+ _propertiesToPrefetch.propertiesToPrefetch.28275
+ _propertiesToPrefetch.propertiesToPrefetch.33761
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.13071
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.28457
+ _propertySetAccessorsByPropertySet.accessorByPropertySetName.34037
+ _propertySetAccessorsByPropertySet.onceToken.13070
+ _propertySetAccessorsByPropertySet.onceToken.28456
+ _propertySetAccessorsByPropertySet.onceToken.34036
+ _propertySetClassForPropertySet:.onceToken.13074
+ _propertySetClassForPropertySet:.onceToken.28464
+ _propertySetClassForPropertySet:.onceToken.34045
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13076
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28465
+ _propertySetClassForPropertySet:.propertySetClassByPropertySetName.34046
+ _sharedDecoder.s_onceToken.50190
+ _sharedDecoder.s_shared.50192
+ _swift_allocateGenericClassMetadata
+ _swift_checkMetadataState
+ _swift_getGenericMetadata
+ _swift_getObjectType
+ _swift_initClassMetadata2
+ _swift_isaMask
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _symbolic $s6Photos35PHBackgroundResourceUploadExtensionP
+ _symbolic $s6Photos48PHBackgroundResourceUploadExtensionConfigurationP
+ _symbolic G0R0_
+ _symbolic Su
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ 6Photos42PHBackgroundResourceUploadProcessingResultO
+ _symbolic _____ 6Photos49_PHBackgroundResourceUploadExtensionConfiguration33_418ED0618F5CF054A91C652800E09068LLC
+ _symbolic _____ So42PLBackgroundResourceUploadProcessingResultV
+ _symbolic _____IeyBy_ So42PLBackgroundResourceUploadProcessingResultV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yxG 6Photos49_PHBackgroundResourceUploadExtensionConfiguration33_418ED0618F5CF054A91C652800E09068LLC
+ _symbolic qd__
+ _symbolic x
+ _transformValueExpression:forKeyPath:._passThroughSet.11120
+ _transformValueExpression:forKeyPath:._passThroughSet.11745
+ _transformValueExpression:forKeyPath:._passThroughSet.13361
+ _transformValueExpression:forKeyPath:._passThroughSet.13654
+ _transformValueExpression:forKeyPath:._passThroughSet.1431
+ _transformValueExpression:forKeyPath:._passThroughSet.1846
+ _transformValueExpression:forKeyPath:._passThroughSet.22813
+ _transformValueExpression:forKeyPath:._passThroughSet.27675
+ _transformValueExpression:forKeyPath:._passThroughSet.28594
+ _transformValueExpression:forKeyPath:._passThroughSet.28966
+ _transformValueExpression:forKeyPath:._passThroughSet.32662
+ _transformValueExpression:forKeyPath:._passThroughSet.34050
+ _transformValueExpression:forKeyPath:._passThroughSet.36326
+ _transformValueExpression:forKeyPath:._passThroughSet.40177
+ _transformValueExpression:forKeyPath:._passThroughSet.4211
+ _transformValueExpression:forKeyPath:._passThroughSet.44353
+ _transformValueExpression:forKeyPath:._passThroughSet.46090
+ _transformValueExpression:forKeyPath:._passThroughSet.47984
+ _transformValueExpression:forKeyPath:._passThroughSet.50963
+ _transformValueExpression:forKeyPath:._passThroughSet.53404
+ _transformValueExpression:forKeyPath:.onceToken.11119
+ _transformValueExpression:forKeyPath:.onceToken.11744
+ _transformValueExpression:forKeyPath:.onceToken.13360
+ _transformValueExpression:forKeyPath:.onceToken.13653
+ _transformValueExpression:forKeyPath:.onceToken.1430
+ _transformValueExpression:forKeyPath:.onceToken.1845
+ _transformValueExpression:forKeyPath:.onceToken.22812
+ _transformValueExpression:forKeyPath:.onceToken.27674
+ _transformValueExpression:forKeyPath:.onceToken.28593
+ _transformValueExpression:forKeyPath:.onceToken.28965
+ _transformValueExpression:forKeyPath:.onceToken.32661
+ _transformValueExpression:forKeyPath:.onceToken.34049
+ _transformValueExpression:forKeyPath:.onceToken.36325
+ _transformValueExpression:forKeyPath:.onceToken.40176
+ _transformValueExpression:forKeyPath:.onceToken.4210
+ _transformValueExpression:forKeyPath:.onceToken.44352
+ _transformValueExpression:forKeyPath:.onceToken.46089
+ _transformValueExpression:forKeyPath:.onceToken.47983
+ _transformValueExpression:forKeyPath:.onceToken.50962
+ _transformValueExpression:forKeyPath:.onceToken.53403
- +[PHAssetResourceUploadJob fetchAssetResourceUploadJobsWithConfiguration:options:]
- +[PHAssetResourceUploadJobChangeRequest creationRequestForAssetResourceUploadJobWithURLRequest:configuration:assetResource:error:]
- +[PHAssetResourceUploadJobConfigurationChangeRequest creationRequestForAssetResourceUploadJobConfigurationWithBundleIdentifier:]
- +[PHAssetResourceUploadJobConfigurationChangeRequest creationRequestForAssetResourceUploadJobConfigurationWithBundleIdentifier:state:]
- +[PHQuery _fetchTypeForLocalIdentifiers:]
- +[PHSearchProcessor _albumUUIDsFromAssetBasedSearchResults:]
- +[PHSearchProcessor _collectionUUIDsForSpotlightSearchableItem:identifiersKey:countsKey:assetCountByCollectionUUID:]
- +[PHSearchProcessor _embeddingLookupIdentifiersForMatchedEmbeddingIDs:assetEmbeddingIds:]
- +[PHSearchProcessor _filterResultsByMatchType:forQuery:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:]
- +[PHSearchProcessor _highlightUUIDsFromAssetBasedSearchResults:]
- +[PHSearchProcessor _memoryUUIDsFromAssetBasedSearchResults:]
- +[PHSearchProcessor _pHSearchSuggestionFromPLSearchSuggestion:rangeOfSuggestionText:]
- +[PHSearchProcessor _popResultsFromResults:popCount:]
- +[PHSearchProcessor _rankedAssetSearchResultsFromResults:maxResults:queryId:batchId:]
- +[PHSearchProcessor _rankedCollectionSearchResultsFromResults:maxResults:queryId:batchId:]
- +[PHSearchProcessor _removeTransientProcessingStateForSearchResults:]
- +[PHSearchProcessor _searchResultTypeForSpotlightSearchableItem:]
- +[PHSearchProcessor searchResultsFromAssetUUIDs:]
- +[PHSearchProcessor searchSuggestionsFromPLSearchSuggestions:suggestions:queryId:batchId:rangeOfSuggestionText:]
- -[PHAssetResourceUploadJob requestData]
- -[PHAssetResourceUploadJobChangeRequest _commonInitalizer]
- -[PHAssetResourceUploadJobChangeRequest failedAttemptCount]
- -[PHAssetResourceUploadJobChangeRequest initForNewObjectWithRequestData:]
- -[PHAssetResourceUploadJobChangeRequest initWithUUID:objectID:requestData:]
- -[PHAssetResourceUploadJobChangeRequest lastRetryDate]
- -[PHAssetResourceUploadJobChangeRequest setFailedAttemptCount:]
- -[PHAssetResourceUploadJobChangeRequest setLastRetryDate:]
- -[PHAssetResourceUploadJobChangeRequest setState:]
- -[PHAssetResourceUploadJobConfigurationChangeRequest placeholderForCreatedAssetResourceUploadJobConfiguration]
- -[PHPerformChangesRequest decodeWithService:clientAuthorization:]
- -[PHSearchProcessor .cxx_destruct]
- -[PHSearchProcessor _searchResultFromSpotlightSearchableItem:queryOptions:matchedLookupIdentifiers:assetCountByCollectionUUID:]
- -[PHSearchProcessor init]
- -[PHSearchProcessor photosAlbumAssetCountsKey]
- -[PHSearchProcessor photosAlbumIdentifiersKey]
- -[PHSearchProcessor photosHighlightAssetCountsKey]
- -[PHSearchProcessor photosHighlightIdentifiersKey]
- -[PHSearchProcessor photosMemoryAssetCountsKey]
- -[PHSearchProcessor photosMemoryIdentifiersKey]
- -[PHSearchProcessor searchResultsFromSpotlightSearchableItems:query:annotatedQueryString:searchResults:unfilteredAssetSearchResults:rankedAssetSearchResults:rankedCollectionSearchResults:assetUUIDsForSuggestions:collectionUUIDsForSuggestions:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:scopedUUIDs:matchedLookupIdentifiers:]
- -[PHSearchProcessor setPhotosAlbumAssetCountsKey:]
- -[PHSearchProcessor setPhotosAlbumIdentifiersKey:]
- -[PHSearchProcessor setPhotosHighlightAssetCountsKey:]
- -[PHSearchProcessor setPhotosHighlightIdentifiersKey:]
- -[PHSearchProcessor setPhotosMemoryAssetCountsKey:]
- -[PHSearchProcessor setPhotosMemoryIdentifiersKey:]
- -[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]
- -[PHSearchResult assetAlbumUUIDs]
- -[PHSearchResult assetHighlightUUIDs]
- -[PHSearchResult assetMemoryUUIDs]
- -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:]
- -[PHSearchResult initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:matchedThumbnailIdentifier:]
- -[PHSearchResult releaseOwningCollectionUUIDs]
- GCC_except_table10020
- GCC_except_table10021
- GCC_except_table10057
- GCC_except_table10061
- GCC_except_table10080
- GCC_except_table10085
- GCC_except_table10155
- GCC_except_table10248
- GCC_except_table10388
- GCC_except_table10425
- GCC_except_table10515
- GCC_except_table10543
- GCC_except_table1076
- GCC_except_table1092
- GCC_except_table1120
- GCC_except_table1212
- GCC_except_table12166
- GCC_except_table12228
- GCC_except_table1229
- GCC_except_table12372
- GCC_except_table12376
- GCC_except_table12380
- GCC_except_table12417
- GCC_except_table12441
- GCC_except_table12448
- GCC_except_table12656
- GCC_except_table12898
- GCC_except_table12976
- GCC_except_table13021
- GCC_except_table13068
- GCC_except_table13078
- GCC_except_table13096
- GCC_except_table13111
- GCC_except_table13140
- GCC_except_table13153
- GCC_except_table13176
- GCC_except_table13258
- GCC_except_table13264
- GCC_except_table13280
- GCC_except_table1390
- GCC_except_table1409
- GCC_except_table1433
- GCC_except_table1472
- GCC_except_table1521
- GCC_except_table1709
- GCC_except_table1713
- GCC_except_table1727
- GCC_except_table1742
- GCC_except_table1928
- GCC_except_table1932
- GCC_except_table1934
- GCC_except_table1936
- GCC_except_table1938
- GCC_except_table1940
- GCC_except_table1942
- GCC_except_table1945
- GCC_except_table1952
- GCC_except_table1954
- GCC_except_table1956
- GCC_except_table2000
- GCC_except_table2002
- GCC_except_table2004
- GCC_except_table2010
- GCC_except_table2012
- GCC_except_table2014
- GCC_except_table2016
- GCC_except_table2018
- GCC_except_table2020
- GCC_except_table2022
- GCC_except_table2024
- GCC_except_table2026
- GCC_except_table2028
- GCC_except_table2030
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2041
- GCC_except_table2044
- GCC_except_table2046
- GCC_except_table2049
- GCC_except_table2053
- GCC_except_table2081
- GCC_except_table2083
- GCC_except_table2086
- GCC_except_table2089
- GCC_except_table2195
- GCC_except_table2200
- GCC_except_table2208
- GCC_except_table2218
- GCC_except_table2258
- GCC_except_table2437
- GCC_except_table2452
- GCC_except_table2471
- GCC_except_table2481
- GCC_except_table2517
- GCC_except_table2522
- GCC_except_table2583
- GCC_except_table2681
- GCC_except_table2692
- GCC_except_table2694
- GCC_except_table2728
- GCC_except_table2802
- GCC_except_table2812
- GCC_except_table2815
- GCC_except_table2825
- GCC_except_table2836
- GCC_except_table2838
- GCC_except_table2841
- GCC_except_table2972
- GCC_except_table2976
- GCC_except_table2979
- GCC_except_table3046
- GCC_except_table3054
- GCC_except_table3083
- GCC_except_table3087
- GCC_except_table3092
- GCC_except_table3208
- GCC_except_table3241
- GCC_except_table3247
- GCC_except_table3250
- GCC_except_table3260
- GCC_except_table3264
- GCC_except_table3270
- GCC_except_table3273
- GCC_except_table3277
- GCC_except_table3281
- GCC_except_table3292
- GCC_except_table3297
- GCC_except_table3308
- GCC_except_table3309
- GCC_except_table3325
- GCC_except_table3334
- GCC_except_table3431
- GCC_except_table3453
- GCC_except_table3455
- GCC_except_table3457
- GCC_except_table3504
- GCC_except_table3531
- GCC_except_table3562
- GCC_except_table3582
- GCC_except_table3584
- GCC_except_table3587
- GCC_except_table3797
- GCC_except_table3799
- GCC_except_table3821
- GCC_except_table3856
- GCC_except_table3866
- GCC_except_table3881
- GCC_except_table3884
- GCC_except_table3886
- GCC_except_table3918
- GCC_except_table3923
- GCC_except_table3924
- GCC_except_table4186
- GCC_except_table4192
- GCC_except_table4219
- GCC_except_table4242
- GCC_except_table4244
- GCC_except_table4248
- GCC_except_table4253
- GCC_except_table4268
- GCC_except_table4281
- GCC_except_table4347
- GCC_except_table4657
- GCC_except_table4659
- GCC_except_table4666
- GCC_except_table4730
- GCC_except_table4732
- GCC_except_table4736
- GCC_except_table4738
- GCC_except_table4741
- GCC_except_table4810
- GCC_except_table4815
- GCC_except_table4845
- GCC_except_table4992
- GCC_except_table5347
- GCC_except_table5396
- GCC_except_table5414
- GCC_except_table5420
- GCC_except_table5439
- GCC_except_table5441
- GCC_except_table5467
- GCC_except_table5469
- GCC_except_table5472
- GCC_except_table5473
- GCC_except_table5478
- GCC_except_table5486
- GCC_except_table5490
- GCC_except_table5499
- GCC_except_table5503
- GCC_except_table5540
- GCC_except_table5548
- GCC_except_table5578
- GCC_except_table5604
- GCC_except_table5608
- GCC_except_table5612
- GCC_except_table5632
- GCC_except_table5638
- GCC_except_table5642
- GCC_except_table5656
- GCC_except_table5659
- GCC_except_table5662
- GCC_except_table5683
- GCC_except_table5729
- GCC_except_table5740
- GCC_except_table5787
- GCC_except_table5818
- GCC_except_table5821
- GCC_except_table5827
- GCC_except_table5831
- GCC_except_table5860
- GCC_except_table5890
- GCC_except_table5916
- GCC_except_table5918
- GCC_except_table5929
- GCC_except_table5976
- GCC_except_table6050
- GCC_except_table6055
- GCC_except_table6060
- GCC_except_table6192
- GCC_except_table6195
- GCC_except_table6208
- GCC_except_table6233
- GCC_except_table6243
- GCC_except_table6246
- GCC_except_table6283
- GCC_except_table6321
- GCC_except_table6323
- GCC_except_table660
- GCC_except_table6709
- GCC_except_table6722
- GCC_except_table6735
- GCC_except_table674
- GCC_except_table6752
- GCC_except_table676
- GCC_except_table6784
- GCC_except_table6786
- GCC_except_table6788
- GCC_except_table679
- GCC_except_table6790
- GCC_except_table6798
- GCC_except_table682
- GCC_except_table6841
- GCC_except_table6854
- GCC_except_table686
- GCC_except_table6887
- GCC_except_table6889
- GCC_except_table689
- GCC_except_table6928
- GCC_except_table7188
- GCC_except_table7189
- GCC_except_table7199
- GCC_except_table7206
- GCC_except_table7225
- GCC_except_table7226
- GCC_except_table7227
- GCC_except_table7228
- GCC_except_table7229
- GCC_except_table7240
- GCC_except_table7241
- GCC_except_table7242
- GCC_except_table729
- GCC_except_table732
- GCC_except_table733
- GCC_except_table734
- GCC_except_table735
- GCC_except_table736
- GCC_except_table738
- GCC_except_table7399
- GCC_except_table7617
- GCC_except_table7643
- GCC_except_table7662
- GCC_except_table7664
- GCC_except_table7665
- GCC_except_table7726
- GCC_except_table7748
- GCC_except_table7752
- GCC_except_table7758
- GCC_except_table7811
- GCC_except_table7971
- GCC_except_table7973
- GCC_except_table8020
- GCC_except_table8060
- GCC_except_table8064
- GCC_except_table8066
- GCC_except_table8068
- GCC_except_table807
- GCC_except_table8085
- GCC_except_table8125
- GCC_except_table8153
- GCC_except_table816
- GCC_except_table8278
- GCC_except_table8336
- GCC_except_table8356
- GCC_except_table8359
- GCC_except_table8378
- GCC_except_table8440
- GCC_except_table8444
- GCC_except_table8448
- GCC_except_table8457
- GCC_except_table8459
- GCC_except_table8499
- GCC_except_table8563
- GCC_except_table8720
- GCC_except_table8766
- GCC_except_table9011
- GCC_except_table9015
- GCC_except_table9019
- GCC_except_table9021
- GCC_except_table904
- GCC_except_table9047
- GCC_except_table9048
- GCC_except_table9140
- GCC_except_table9150
- GCC_except_table9182
- GCC_except_table9234
- GCC_except_table9268
- GCC_except_table9288
- GCC_except_table9315
- GCC_except_table9340
- GCC_except_table9373
- GCC_except_table9375
- GCC_except_table9465
- GCC_except_table952
- GCC_except_table9556
- GCC_except_table9675
- GCC_except_table9689
- GCC_except_table9697
- GCC_except_table9700
- GCC_except_table9730
- GCC_except_table9740
- GCC_except_table9814
- GCC_except_table9815
- GCC_except_table9816
- GCC_except_table9817
- GCC_except_table9818
- GCC_except_table9819
- GCC_except_table9820
- GCC_except_table9916
- GCC_except_table9925
- GCC_except_table9926
- GCC_except_table9927
- GCC_except_table9928
- GCC_except_table9929
- GCC_except_table9931
- GCC_except_table9936
- GCC_except_table9954
- GCC_except_table9981
- GCC_except_table9982
- GCC_except_table9992
- _OBJC_CLASS_$_PHSearchProcessor
- _OBJC_IVAR_$_PHAssetResourceUploadJob._requestData
- _OBJC_IVAR_$_PHAssetResourceUploadJobConfigurationChangeRequest._placeholderForCreatedAssetResourceUploadJobConfiguration
- _OBJC_IVAR_$_PHSearchProcessor._photosAlbumAssetCountsKey
- _OBJC_IVAR_$_PHSearchProcessor._photosAlbumIdentifiersKey
- _OBJC_IVAR_$_PHSearchProcessor._photosHighlightAssetCountsKey
- _OBJC_IVAR_$_PHSearchProcessor._photosHighlightIdentifiersKey
- _OBJC_IVAR_$_PHSearchProcessor._photosMemoryAssetCountsKey
- _OBJC_IVAR_$_PHSearchProcessor._photosMemoryIdentifiersKey
- _OBJC_IVAR_$_PHSearchResult._assetAlbumUUIDs
- _OBJC_IVAR_$_PHSearchResult._assetHighlightUUIDs
- _OBJC_IVAR_$_PHSearchResult._assetMemoryUUIDs
- _OBJC_METACLASS_$_PHSearchProcessor
- _PHSearchBatchResultProcessingEnabled._batchResultProcessingEnabled
- _PHSearchBatchResultProcessingEnabled.once
- _PLSearchThumbnailMapVerboseLoggingEnabled
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.19317
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.22491
- _SensitiveContentAnalysisLibraryCore.frameworkLibrary.36580
- __OBJC_$_CLASS_METHODS_PHSearchProcessor
- __OBJC_$_CLASS_PROP_LIST_PHAssetPropertySet.2603
- __OBJC_$_INSTANCE_METHODS_PHSearchProcessor
- __OBJC_$_INSTANCE_VARIABLES_PHSearchProcessor
- __OBJC_$_PROP_LIST_PHAssetPropertySet.2610
- __OBJC_$_PROP_LIST_PHSearchProcessor
- __OBJC_CLASS_RO_$_PHSearchProcessor
- __OBJC_METACLASS_RO_$_PHSearchProcessor
- ___112+[PHSearchProcessor searchSuggestionsFromPLSearchSuggestions:suggestions:queryId:batchId:rangeOfSuggestionText:]_block_invoke
- ___116+[PHSearchProcessor _collectionUUIDsForSpotlightSearchableItem:identifiersKey:countsKey:assetCountByCollectionUUID:]_block_invoke
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke.107
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_2.108
- ___126-[PHServerResourceRequestRunner _applyCorrectionsToAssetObjectIDURL:resourceIdentity:errorCodes:clientBundleID:library:reply:]_block_invoke_3.110
- ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.150
- ___152-[PHServerResourceRequestRunner startWalrusTimeRangeDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:partialVideoURL:reply:]_block_invoke.153
- ___156-[PHServerResourceRequestRunner startDownloadForRequest:backingResource:clientBundleID:shouldReturnAdjustmentInfo:needsDownload:shouldApplyTimeRange:reply:]_block_invoke.149
- ___364-[PHSearchProcessor searchResultsFromSpotlightSearchableItems:query:annotatedQueryString:searchResults:unfilteredAssetSearchResults:rankedAssetSearchResults:rankedCollectionSearchResults:assetUUIDsForSuggestions:collectionUUIDsForSuggestions:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:scopedUUIDs:matchedLookupIdentifiers:]_block_invoke
- ___364-[PHSearchProcessor searchResultsFromSpotlightSearchableItems:query:annotatedQueryString:searchResults:unfilteredAssetSearchResults:rankedAssetSearchResults:rankedCollectionSearchResults:assetUUIDsForSuggestions:collectionUUIDsForSuggestions:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:scopedUUIDs:matchedLookupIdentifiers:]_block_invoke.81
- ___37+[PHAsset propertiesToFetchWithHint:]_block_invoke.592
- ___39-[PHAsset _createKeywordPropertyObject]_block_invoke.861
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.172
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke.174
- ___59-[PHSearchQuery _executeSpotlightSearchWithResultsHandler:]_block_invoke_2
- ___61-[PHSearchQuery _executeSpotlightSearchWithResultsHandlerV2:]_block_invoke.177
- ___82+[PHAssetResourceUploadJob fetchAssetResourceUploadJobsWithConfiguration:options:]_block_invoke
- ___84+[PHSearchUtility insertSpacingIfNeededBetweenAnnotationsAndPlainTextInQueryString:]_block_invoke.82
- ___85+[PHSearchProcessor _rankedAssetSearchResultsFromResults:maxResults:queryId:batchId:]_block_invoke
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.121
- ___85-[PHServerResourceRequestRunner chooseVideoWithRequest:library:clientBundleID:reply:]_block_invoke.133
- ___90+[PHSearchProcessor _rankedCollectionSearchResultsFromResults:maxResults:queryId:batchId:]_block_invoke
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke.124
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_2.126
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_3.127
- ___96-[PHPerformChangesRequest executeWithLibraryServicesManager:libraryName:executionContext:reply:]_block_invoke_4.128
- ___Block_byref_object_copy_.10464
- ___Block_byref_object_copy_.11209
- ___Block_byref_object_copy_.11483
- ___Block_byref_object_copy_.11642
- ___Block_byref_object_copy_.12487
- ___Block_byref_object_copy_.12753
- ___Block_byref_object_copy_.13219
- ___Block_byref_object_copy_.13697
- ___Block_byref_object_copy_.1465
- ___Block_byref_object_copy_.14902
- ___Block_byref_object_copy_.15654
- ___Block_byref_object_copy_.1644
- ___Block_byref_object_copy_.17622
- ___Block_byref_object_copy_.18600
- ___Block_byref_object_copy_.20264
- ___Block_byref_object_copy_.20430
- ___Block_byref_object_copy_.20753
- ___Block_byref_object_copy_.2106
- ___Block_byref_object_copy_.21220
- ___Block_byref_object_copy_.21801
- ___Block_byref_object_copy_.22308
- ___Block_byref_object_copy_.22499
- ___Block_byref_object_copy_.24338
- ___Block_byref_object_copy_.2512
- ___Block_byref_object_copy_.25212
- ___Block_byref_object_copy_.26903
- ___Block_byref_object_copy_.27432
- ___Block_byref_object_copy_.28160
- ___Block_byref_object_copy_.28448
- ___Block_byref_object_copy_.2944
- ___Block_byref_object_copy_.29972
- ___Block_byref_object_copy_.30944
- ___Block_byref_object_copy_.31689
- ___Block_byref_object_copy_.31983
- ___Block_byref_object_copy_.33365
- ___Block_byref_object_copy_.33946
- ___Block_byref_object_copy_.34503
- ___Block_byref_object_copy_.34645
- ___Block_byref_object_copy_.3488
- ___Block_byref_object_copy_.35082
- ___Block_byref_object_copy_.35662
- ___Block_byref_object_copy_.35942
- ___Block_byref_object_copy_.36903
- ___Block_byref_object_copy_.37345
- ___Block_byref_object_copy_.38946
- ___Block_byref_object_copy_.39503
- ___Block_byref_object_copy_.4095
- ___Block_byref_object_copy_.43575
- ___Block_byref_object_copy_.43999
- ___Block_byref_object_copy_.44210
- ___Block_byref_object_copy_.44439
- ___Block_byref_object_copy_.45778
- ___Block_byref_object_copy_.46186
- ___Block_byref_object_copy_.46705
- ___Block_byref_object_copy_.47007
- ___Block_byref_object_copy_.47382
- ___Block_byref_object_copy_.47869
- ___Block_byref_object_copy_.48363
- ___Block_byref_object_copy_.49241
- ___Block_byref_object_copy_.49439
- ___Block_byref_object_copy_.49649
- ___Block_byref_object_copy_.49686
- ___Block_byref_object_copy_.51858
- ___Block_byref_object_copy_.52162
- ___Block_byref_object_copy_.52897
- ___Block_byref_object_copy_.53700
- ___Block_byref_object_copy_.5634
- ___Block_byref_object_copy_.6683
- ___Block_byref_object_copy_.7158
- ___Block_byref_object_copy_.8913
- ___Block_byref_object_copy_.901
- ___Block_byref_object_copy_.9203
- ___Block_byref_object_copy_.9766
- ___Block_byref_object_dispose_.10465
- ___Block_byref_object_dispose_.11210
- ___Block_byref_object_dispose_.11484
- ___Block_byref_object_dispose_.11643
- ___Block_byref_object_dispose_.12488
- ___Block_byref_object_dispose_.12754
- ___Block_byref_object_dispose_.13220
- ___Block_byref_object_dispose_.13698
- ___Block_byref_object_dispose_.1466
- ___Block_byref_object_dispose_.14903
- ___Block_byref_object_dispose_.15655
- ___Block_byref_object_dispose_.1645
- ___Block_byref_object_dispose_.17623
- ___Block_byref_object_dispose_.18601
- ___Block_byref_object_dispose_.20265
- ___Block_byref_object_dispose_.20431
- ___Block_byref_object_dispose_.20754
- ___Block_byref_object_dispose_.2107
- ___Block_byref_object_dispose_.21221
- ___Block_byref_object_dispose_.21802
- ___Block_byref_object_dispose_.22309
- ___Block_byref_object_dispose_.22500
- ___Block_byref_object_dispose_.24339
- ___Block_byref_object_dispose_.2513
- ___Block_byref_object_dispose_.25213
- ___Block_byref_object_dispose_.26904
- ___Block_byref_object_dispose_.27433
- ___Block_byref_object_dispose_.28161
- ___Block_byref_object_dispose_.28449
- ___Block_byref_object_dispose_.2945
- ___Block_byref_object_dispose_.29973
- ___Block_byref_object_dispose_.30945
- ___Block_byref_object_dispose_.31690
- ___Block_byref_object_dispose_.31984
- ___Block_byref_object_dispose_.33366
- ___Block_byref_object_dispose_.33947
- ___Block_byref_object_dispose_.34504
- ___Block_byref_object_dispose_.34646
- ___Block_byref_object_dispose_.3489
- ___Block_byref_object_dispose_.35083
- ___Block_byref_object_dispose_.35663
- ___Block_byref_object_dispose_.35943
- ___Block_byref_object_dispose_.36904
- ___Block_byref_object_dispose_.37346
- ___Block_byref_object_dispose_.38947
- ___Block_byref_object_dispose_.39504
- ___Block_byref_object_dispose_.4096
- ___Block_byref_object_dispose_.43576
- ___Block_byref_object_dispose_.44000
- ___Block_byref_object_dispose_.44211
- ___Block_byref_object_dispose_.44440
- ___Block_byref_object_dispose_.45779
- ___Block_byref_object_dispose_.46187
- ___Block_byref_object_dispose_.46706
- ___Block_byref_object_dispose_.47008
- ___Block_byref_object_dispose_.47383
- ___Block_byref_object_dispose_.47870
- ___Block_byref_object_dispose_.48364
- ___Block_byref_object_dispose_.49242
- ___Block_byref_object_dispose_.49440
- ___Block_byref_object_dispose_.49650
- ___Block_byref_object_dispose_.49687
- ___Block_byref_object_dispose_.51859
- ___Block_byref_object_dispose_.52163
- ___Block_byref_object_dispose_.52898
- ___Block_byref_object_dispose_.53701
- ___Block_byref_object_dispose_.5635
- ___Block_byref_object_dispose_.6684
- ___Block_byref_object_dispose_.7159
- ___Block_byref_object_dispose_.8914
- ___Block_byref_object_dispose_.902
- ___Block_byref_object_dispose_.9204
- ___Block_byref_object_dispose_.9767
- ___PHSearchBatchResultProcessingEnabled_block_invoke
- ___SensitiveContentAnalysisLibraryCore_block_invoke.19318
- ___SensitiveContentAnalysisLibraryCore_block_invoke.22492
- ___SensitiveContentAnalysisLibraryCore_block_invoke.36581
- ____fetchTypeForLocalIdentifierCode_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80r88r96r_e40_v32?0"<PHInsertChangeRequest>"8Q16^B24ls32l8s40l8r80l8r88l8s48l8s56l8s64l8s72l8r96l8
- ___block_descriptor_131_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e33_v32?0"CSSearchableItem"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_144_e8_32s40s48s56bs64r72r80r88r96r104r112w120n11_8_8_s0_t8w8_e17_v16?0"NSError"8l
- ___block_descriptor_57_e8_32s40s48s_e30_v24?0"NSString"8"NSArray"16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s_e25_v24?0Q8"NSCountedSet"16ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32r40r48r56r64r72w_e27_v16?0"CSAttributedQuery"8lw72l8r32l8r40l8r48l8r56l8r64l8
- ___block_literal_global.1000
- ___block_literal_global.1002
- ___block_literal_global.1004
- ___block_literal_global.1006
- ___block_literal_global.1008
- ___block_literal_global.1010
- ___block_literal_global.1016
- ___block_literal_global.1018
- ___block_literal_global.1020
- ___block_literal_global.1022
- ___block_literal_global.1024
- ___block_literal_global.1026
- ___block_literal_global.1028
- ___block_literal_global.1030
- ___block_literal_global.1032
- ___block_literal_global.1034
- ___block_literal_global.1034.36760
- ___block_literal_global.1036
- ___block_literal_global.1038
- ___block_literal_global.1040
- ___block_literal_global.1042
- ___block_literal_global.1044
- ___block_literal_global.1046
- ___block_literal_global.1048
- ___block_literal_global.1050
- ___block_literal_global.1052
- ___block_literal_global.1054
- ___block_literal_global.1056
- ___block_literal_global.1056.36758
- ___block_literal_global.1058
- ___block_literal_global.1058.36756
- ___block_literal_global.10593
- ___block_literal_global.1060
- ___block_literal_global.1062
- ___block_literal_global.1064
- ___block_literal_global.1066
- ___block_literal_global.1068
- ___block_literal_global.1072
- ___block_literal_global.1074
- ___block_literal_global.1076
- ___block_literal_global.1078
- ___block_literal_global.108
- ___block_literal_global.1080
- ___block_literal_global.1082
- ___block_literal_global.1084
- ___block_literal_global.1086
- ___block_literal_global.1088
- ___block_literal_global.1090
- ___block_literal_global.1092
- ___block_literal_global.1092.36754
- ___block_literal_global.1094
- ___block_literal_global.1096
- ___block_literal_global.1098
- ___block_literal_global.1100
- ___block_literal_global.1102
- ___block_literal_global.1104
- ___block_literal_global.1106
- ___block_literal_global.1108
- ___block_literal_global.1110
- ___block_literal_global.1112
- ___block_literal_global.1114
- ___block_literal_global.1116
- ___block_literal_global.1118
- ___block_literal_global.112.41266
- ___block_literal_global.1120
- ___block_literal_global.1122
- ___block_literal_global.1124
- ___block_literal_global.1126
- ___block_literal_global.1128
- ___block_literal_global.1130
- ___block_literal_global.11304
- ___block_literal_global.1132
- ___block_literal_global.1134
- ___block_literal_global.1136
- ___block_literal_global.1138
- ___block_literal_global.1140
- ___block_literal_global.1142
- ___block_literal_global.1144
- ___block_literal_global.1146
- ___block_literal_global.1148
- ___block_literal_global.11499
- ___block_literal_global.1150
- ___block_literal_global.1152
- ___block_literal_global.1154
- ___block_literal_global.1156
- ___block_literal_global.1158
- ___block_literal_global.1160
- ___block_literal_global.1162
- ___block_literal_global.1164
- ___block_literal_global.1166
- ___block_literal_global.1168
- ___block_literal_global.1181
- ___block_literal_global.1183
- ___block_literal_global.1185
- ___block_literal_global.1187
- ___block_literal_global.11876
- ___block_literal_global.1189
- ___block_literal_global.1191
- ___block_literal_global.1193
- ___block_literal_global.1195
- ___block_literal_global.1197
- ___block_literal_global.1199
- ___block_literal_global.1201
- ___block_literal_global.1203
- ___block_literal_global.1205
- ___block_literal_global.1207
- ___block_literal_global.1209
- ___block_literal_global.1211
- ___block_literal_global.1213
- ___block_literal_global.1215
- ___block_literal_global.1217
- ___block_literal_global.1219
- ___block_literal_global.1277
- ___block_literal_global.12810
- ___block_literal_global.134.47929
- ___block_literal_global.13516
- ___block_literal_global.13699
- ___block_literal_global.14260
- ___block_literal_global.144
- ___block_literal_global.14579
- ___block_literal_global.146.38914
- ___block_literal_global.1485
- ___block_literal_global.14970
- ___block_literal_global.15649
- ___block_literal_global.1606
- ___block_literal_global.17202
- ___block_literal_global.1726
- ___block_literal_global.17856
- ___block_literal_global.18629
- ___block_literal_global.18680
- ___block_literal_global.1903
- ___block_literal_global.19864
- ___block_literal_global.20181
- ___block_literal_global.206.28731
- ___block_literal_global.206.29639
- ___block_literal_global.20769
- ___block_literal_global.210.29642
- ___block_literal_global.2117
- ___block_literal_global.21195
- ___block_literal_global.212.29643
- ___block_literal_global.217.14065
- ___block_literal_global.22099
- ___block_literal_global.224.14858
- ___block_literal_global.22977
- ___block_literal_global.234.34233
- ___block_literal_global.24246
- ___block_literal_global.2545
- ___block_literal_global.25570
- ___block_literal_global.26239
- ___block_literal_global.2648
- ___block_literal_global.27134
- ___block_literal_global.2734
- ___block_literal_global.2751
- ___block_literal_global.27863
- ___block_literal_global.28137
- ___block_literal_global.2819
- ___block_literal_global.2849
- ___block_literal_global.28762
- ___block_literal_global.29033
- ___block_literal_global.29112
- ___block_literal_global.2941
- ___block_literal_global.29628
- ___block_literal_global.3.11504
- ___block_literal_global.3.2940
- ___block_literal_global.30088
- ___block_literal_global.30473
- ___block_literal_global.30670
- ___block_literal_global.30955
- ___block_literal_global.3102
- ___block_literal_global.3109
- ___block_literal_global.31372
- ___block_literal_global.3154
- ___block_literal_global.3172
- ___block_literal_global.3193
- ___block_literal_global.3221
- ___block_literal_global.32216
- ___block_literal_global.32360
- ___block_literal_global.3242
- ___block_literal_global.32833
- ___block_literal_global.3284
- ___block_literal_global.3335
- ___block_literal_global.33472
- ___block_literal_global.34236
- ___block_literal_global.3426
- ___block_literal_global.344
- ___block_literal_global.34517
- ___block_literal_global.34596
- ___block_literal_global.3465
- ___block_literal_global.34742
- ___block_literal_global.34924
- ___block_literal_global.3498
- ___block_literal_global.35400
- ___block_literal_global.3572
- ___block_literal_global.3583
- ___block_literal_global.35947
- ___block_literal_global.36452
- ___block_literal_global.37.32262
- ___block_literal_global.37.47501
- ___block_literal_global.372
- ___block_literal_global.37215
- ___block_literal_global.3726
- ___block_literal_global.37406
- ___block_literal_global.37952
- ___block_literal_global.3800
- ___block_literal_global.38258
- ___block_literal_global.3844
- ___block_literal_global.38989
- ___block_literal_global.39247
- ___block_literal_global.3957
- ___block_literal_global.39676
- ___block_literal_global.40267
- ___block_literal_global.40478
- ___block_literal_global.40964
- ___block_literal_global.41272
- ___block_literal_global.42582
- ___block_literal_global.4283
- ___block_literal_global.43165
- ___block_literal_global.4335
- ___block_literal_global.43578
- ___block_literal_global.4385
- ___block_literal_global.4388
- ___block_literal_global.44265
- ___block_literal_global.4428
- ___block_literal_global.44456
- ___block_literal_global.4450
- ___block_literal_global.4492
- ___block_literal_global.45077
- ___block_literal_global.4523
- ___block_literal_global.4540
- ___block_literal_global.4571
- ___block_literal_global.4577
- ___block_literal_global.45863
- ___block_literal_global.4589
- ___block_literal_global.4594
- ___block_literal_global.4615
- ___block_literal_global.46218
- ___block_literal_global.4633
- ___block_literal_global.4644
- ___block_literal_global.46536
- ___block_literal_global.4659
- ___block_literal_global.46627
- ___block_literal_global.4670
- ___block_literal_global.47290
- ___block_literal_global.47508
- ___block_literal_global.4767
- ___block_literal_global.47948
- ___block_literal_global.4807
- ___block_literal_global.48096
- ___block_literal_global.48854
- ___block_literal_global.4899
- ___block_literal_global.49206
- ___block_literal_global.49651
- ___block_literal_global.49699
- ___block_literal_global.4973
- ___block_literal_global.50.26207
- ___block_literal_global.50008
- ___block_literal_global.50281
- ___block_literal_global.51594
- ___block_literal_global.52986
- ___block_literal_global.53554
- ___block_literal_global.546
- ___block_literal_global.551
- ___block_literal_global.5668
- ___block_literal_global.589.22972
- ___block_literal_global.62.1463
- ___block_literal_global.644
- ___block_literal_global.647
- ___block_literal_global.677
- ___block_literal_global.6770
- ___block_literal_global.684
- ___block_literal_global.7165
- ___block_literal_global.723
- ___block_literal_global.7837
- ___block_literal_global.80
- ___block_literal_global.8064
- ___block_literal_global.8235
- ___block_literal_global.837
- ___block_literal_global.85.53532
- ___block_literal_global.864
- ___block_literal_global.8905
- ___block_literal_global.8992
- ___block_literal_global.9435
- ___block_literal_global.96
- ___block_literal_global.968
- ___block_literal_global.980.36931
- ___block_literal_global.982.36925
- ___block_literal_global.984
- ___block_literal_global.986
- ___block_literal_global.988
- ___block_literal_global.989
- ___block_literal_global.990
- ___block_literal_global.992
- ___block_literal_global.994
- ___block_literal_global.996
- ___block_literal_global.998
- ___copy_helper_block_e8_120n11_8_8_s0_t8w8
- ___destroy_helper_block_e8_120n4_8_s0
- ___getSCSensitivityAnalysisClass_block_invoke.19316
- ___getSCSensitivityAnalysisClass_block_invoke.22489
- ___getSCSensitivityAnalysisClass_block_invoke.36579
- __currentTimestampString.s_formatter.47502
- __currentTimestampString.s_onceToken.47500
- __fetchTypeForLocalIdentifierCode.pl_once_object_34
- __fetchTypeForLocalIdentifierCode.pl_once_token_34
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_object_72
- _additionalPropertiesToFetchOnPrimaryObject.pl_once_token_72
- _allowedInfoKeys.allowedKeys.1703
- _allowedInfoKeys.allowedKeys.18884
- _allowedInfoKeys.allowedKeys.40769
- _allowedInfoKeys.onceToken.1702
- _allowedInfoKeys.onceToken.18883
- _allowedInfoKeys.onceToken.40768
- _audit_stringSensitiveContentAnalysis.19327
- _audit_stringSensitiveContentAnalysis.22496
- _audit_stringSensitiveContentAnalysis.36586
- _corePropertiesToFetch.array.22980
- _corePropertiesToFetch.array.28759
- _corePropertiesToFetch.array.34237
- _corePropertiesToFetch.onceToken.22979
- _corePropertiesToFetch.onceToken.28758
- _corePropertiesToFetch.onceToken.34235
- _createObjectChangeRequestsFromXPCObject
- _defaultManager.onceToken.51944
- _entityKeyMap.pl_once_object_15.11285
- _entityKeyMap.pl_once_object_15.11887
- _entityKeyMap.pl_once_object_15.1267
- _entityKeyMap.pl_once_object_15.13507
- _entityKeyMap.pl_once_object_15.13804
- _entityKeyMap.pl_once_object_15.1481
- _entityKeyMap.pl_once_object_15.2009
- _entityKeyMap.pl_once_object_15.27854
- _entityKeyMap.pl_once_object_15.29123
- _entityKeyMap.pl_once_object_15.32824
- _entityKeyMap.pl_once_object_15.36442
- _entityKeyMap.pl_once_object_15.40299
- _entityKeyMap.pl_once_object_15.44479
- _entityKeyMap.pl_once_object_15.46209
- _entityKeyMap.pl_once_object_15.46619
- _entityKeyMap.pl_once_object_15.4799
- _entityKeyMap.pl_once_object_15.48093
- _entityKeyMap.pl_once_object_15.50156
- _entityKeyMap.pl_once_object_15.51076
- _entityKeyMap.pl_once_object_15.8070
- _entityKeyMap.pl_once_object_16.34225
- _entityKeyMap.pl_once_object_16.34583
- _entityKeyMap.pl_once_object_16.40465
- _entityKeyMap.pl_once_object_16.4376
- _entityKeyMap.pl_once_object_16.47278
- _entityKeyMap.pl_once_object_16.53541
- _entityKeyMap.pl_once_token_15.11284
- _entityKeyMap.pl_once_token_15.11886
- _entityKeyMap.pl_once_token_15.1266
- _entityKeyMap.pl_once_token_15.13506
- _entityKeyMap.pl_once_token_15.13803
- _entityKeyMap.pl_once_token_15.1480
- _entityKeyMap.pl_once_token_15.2008
- _entityKeyMap.pl_once_token_15.27853
- _entityKeyMap.pl_once_token_15.29122
- _entityKeyMap.pl_once_token_15.32823
- _entityKeyMap.pl_once_token_15.36441
- _entityKeyMap.pl_once_token_15.40298
- _entityKeyMap.pl_once_token_15.44478
- _entityKeyMap.pl_once_token_15.46208
- _entityKeyMap.pl_once_token_15.46618
- _entityKeyMap.pl_once_token_15.4798
- _entityKeyMap.pl_once_token_15.48092
- _entityKeyMap.pl_once_token_15.50155
- _entityKeyMap.pl_once_token_15.51075
- _entityKeyMap.pl_once_token_15.8069
- _entityKeyMap.pl_once_token_16.34224
- _entityKeyMap.pl_once_token_16.34582
- _entityKeyMap.pl_once_token_16.40464
- _entityKeyMap.pl_once_token_16.4375
- _entityKeyMap.pl_once_token_16.47277
- _entityKeyMap.pl_once_token_16.53540
- _getSCSensitivityAnalysisClass.19314
- _getSCSensitivityAnalysisClass.36575
- _getSCSensitivityAnalysisClass.softClass.19315
- _getSCSensitivityAnalysisClass.softClass.22488
- _getSCSensitivityAnalysisClass.softClass.36578
- _identifierPropertiesToFetch.array.35401
- _identifierPropertiesToFetch.onceToken.35399
- _objc_msgSend$_albumUUIDsFromAssetBasedSearchResults:
- _objc_msgSend$_collectionUUIDsForSpotlightSearchableItem:identifiersKey:countsKey:assetCountByCollectionUUID:
- _objc_msgSend$_commonInitalizer
- _objc_msgSend$_executeSpotlightSearchWithResultsHandler:
- _objc_msgSend$_fetchTypeForLocalIdentifiers:
- _objc_msgSend$_filterResultsByMatchType:forQuery:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:
- _objc_msgSend$_highlightUUIDsFromAssetBasedSearchResults:
- _objc_msgSend$_memoryUUIDsFromAssetBasedSearchResults:
- _objc_msgSend$_rankedAssetSearchResultsFromResults:maxResults:queryId:batchId:
- _objc_msgSend$_rankedCollectionSearchResultsFromResults:maxResults:queryId:batchId:
- _objc_msgSend$_removeTransientProcessingStateForSearchResults:
- _objc_msgSend$_searchResultFromSpotlightSearchableItem:queryOptions:matchedLookupIdentifiers:assetCountByCollectionUUID:
- _objc_msgSend$assetAlbumUUIDs
- _objc_msgSend$assetHighlightUUIDs
- _objc_msgSend$assetMemoryUUIDs
- _objc_msgSend$finishEncoding
- _objc_msgSend$generateAndStoreForAsset:networkAccessAllowed:clientBundleID:progress:completion:
- _objc_msgSend$getCPLConfigrationValueForKey:completionHandler:
- _objc_msgSend$initForNewObjectWithRequestData:
- _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:
- _objc_msgSend$initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:matchedThumbnailIdentifier:
- _objc_msgSend$initWithUUID:objectID:requestData:
- _objc_msgSend$processPairingForGroupIDs:inContext:deferredProcessingNeeded:error:
- _objc_msgSend$releaseOwningCollectionUUIDs
- _objc_msgSend$requestData
- _objc_msgSend$searchResultsFromSpotlightSearchableItems:query:annotatedQueryString:searchResults:unfilteredAssetSearchResults:rankedAssetSearchResults:rankedCollectionSearchResults:assetUUIDsForSuggestions:collectionUUIDsForSuggestions:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:scopedUUIDs:matchedLookupIdentifiers:
- _objc_msgSend$setBundleIdentifier:
- _objc_msgSend$setFailedAttemptCount:
- _objc_msgSend$setPhotosAlbumAssetCountsKey:
- _objc_msgSend$setPhotosAlbumIdentifiersKey:
- _objc_msgSend$setPhotosHighlightAssetCountsKey:
- _objc_msgSend$setPhotosHighlightIdentifiersKey:
- _objc_msgSend$setPhotosMemoryAssetCountsKey:
- _objc_msgSend$setPhotosMemoryIdentifiersKey:
- _objc_msgSend$signalBackgroundProcessingNeededOnLibrary:
- _objc_msgSend$sortUsingDescriptors:
- _objc_msgSend$spatialOverCaptureGroupIdentifier
- _propertiesToFetch.pl_once_object_24.33942
- _propertiesToFetch.pl_once_object_73
- _propertiesToFetch.pl_once_token_24.33941
- _propertiesToFetch.pl_once_token_73
- _propertiesToFetchWithHint:.array.11300
- _propertiesToFetchWithHint:.array.11894
- _propertiesToFetchWithHint:.array.13826
- _propertiesToFetchWithHint:.array.1486
- _propertiesToFetchWithHint:.array.23475
- _propertiesToFetchWithHint:.array.27864
- _propertiesToFetchWithHint:.array.29133
- _propertiesToFetchWithHint:.array.32834
- _propertiesToFetchWithHint:.array.36453
- _propertiesToFetchWithHint:.array.40320
- _propertiesToFetchWithHint:.array.46219
- _propertiesToFetchWithHint:.array.48097
- _propertiesToFetchWithHint:.array.50169
- _propertiesToFetchWithHint:.array.51104
- _propertiesToFetchWithHint:.array.8098
- _propertiesToFetchWithHint:.onceToken.11299
- _propertiesToFetchWithHint:.onceToken.11893
- _propertiesToFetchWithHint:.onceToken.1276
- _propertiesToFetchWithHint:.onceToken.13515
- _propertiesToFetchWithHint:.onceToken.13825
- _propertiesToFetchWithHint:.onceToken.1484
- _propertiesToFetchWithHint:.onceToken.22971
- _propertiesToFetchWithHint:.onceToken.23474
- _propertiesToFetchWithHint:.onceToken.27862
- _propertiesToFetchWithHint:.onceToken.28761
- _propertiesToFetchWithHint:.onceToken.29132
- _propertiesToFetchWithHint:.onceToken.32832
- _propertiesToFetchWithHint:.onceToken.34229
- _propertiesToFetchWithHint:.onceToken.36451
- _propertiesToFetchWithHint:.onceToken.40319
- _propertiesToFetchWithHint:.onceToken.4386
- _propertiesToFetchWithHint:.onceToken.46217
- _propertiesToFetchWithHint:.onceToken.48095
- _propertiesToFetchWithHint:.onceToken.50168
- _propertiesToFetchWithHint:.onceToken.51103
- _propertiesToFetchWithHint:.onceToken.8097
- _propertiesToFetchWithHint:.pl_once_object_15.34597
- _propertiesToFetchWithHint:.pl_once_object_15.40479
- _propertiesToFetchWithHint:.pl_once_object_15.47291
- _propertiesToFetchWithHint:.pl_once_object_15.53555
- _propertiesToFetchWithHint:.pl_once_token_15.34595
- _propertiesToFetchWithHint:.pl_once_token_15.40477
- _propertiesToFetchWithHint:.pl_once_token_15.47289
- _propertiesToFetchWithHint:.pl_once_token_15.53553
- _propertiesToFetchWithHint:.propertiesToFetchByHint.13518
- _propertiesToFetchWithHint:.propertiesToFetchByHint.22974
- _propertiesToFetchWithHint:.propertiesToFetchByHint.28764
- _propertiesToFetchWithHint:.propertiesToFetchByHint.34231
- _propertiesToFetchWithHint:.propertyQueue.13517
- _propertiesToFetchWithHint:.propertyQueue.22973
- _propertiesToFetchWithHint:.propertyQueue.28763
- _propertiesToFetchWithHint:.propertyQueue.34230
- _propertiesToPrefetch.onceToken.22506
- _propertiesToPrefetch.onceToken.28425
- _propertiesToPrefetch.onceToken.33932
- _propertiesToPrefetch.propertiesToPrefetch.22507
- _propertiesToPrefetch.propertiesToPrefetch.28426
- _propertiesToPrefetch.propertiesToPrefetch.33933
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.13206
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.28610
- _propertySetAccessorsByPropertySet.accessorByPropertySetName.34200
- _propertySetAccessorsByPropertySet.onceToken.13205
- _propertySetAccessorsByPropertySet.onceToken.28609
- _propertySetAccessorsByPropertySet.onceToken.34199
- _propertySetClassForPropertySet:.onceToken.13208
- _propertySetClassForPropertySet:.onceToken.28617
- _propertySetClassForPropertySet:.onceToken.34208
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.13209
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.28618
- _propertySetClassForPropertySet:.propertySetClassByPropertySetName.34209
- _sharedDecoder.s_onceToken.50280
- _sharedDecoder.s_shared.50282
- _transformValueExpression:forKeyPath:._passThroughSet.11258
- _transformValueExpression:forKeyPath:._passThroughSet.11883
- _transformValueExpression:forKeyPath:._passThroughSet.13496
- _transformValueExpression:forKeyPath:._passThroughSet.13789
- _transformValueExpression:forKeyPath:._passThroughSet.1478
- _transformValueExpression:forKeyPath:._passThroughSet.2005
- _transformValueExpression:forKeyPath:._passThroughSet.22926
- _transformValueExpression:forKeyPath:._passThroughSet.27830
- _transformValueExpression:forKeyPath:._passThroughSet.28747
- _transformValueExpression:forKeyPath:._passThroughSet.29119
- _transformValueExpression:forKeyPath:._passThroughSet.32815
- _transformValueExpression:forKeyPath:._passThroughSet.34213
- _transformValueExpression:forKeyPath:._passThroughSet.36436
- _transformValueExpression:forKeyPath:._passThroughSet.40288
- _transformValueExpression:forKeyPath:._passThroughSet.4365
- _transformValueExpression:forKeyPath:._passThroughSet.44461
- _transformValueExpression:forKeyPath:._passThroughSet.46197
- _transformValueExpression:forKeyPath:._passThroughSet.48090
- _transformValueExpression:forKeyPath:._passThroughSet.51054
- _transformValueExpression:forKeyPath:._passThroughSet.53503
- _transformValueExpression:forKeyPath:.onceToken.11257
- _transformValueExpression:forKeyPath:.onceToken.11882
- _transformValueExpression:forKeyPath:.onceToken.13495
- _transformValueExpression:forKeyPath:.onceToken.13788
- _transformValueExpression:forKeyPath:.onceToken.1477
- _transformValueExpression:forKeyPath:.onceToken.2004
- _transformValueExpression:forKeyPath:.onceToken.22925
- _transformValueExpression:forKeyPath:.onceToken.27829
- _transformValueExpression:forKeyPath:.onceToken.28746
- _transformValueExpression:forKeyPath:.onceToken.29118
- _transformValueExpression:forKeyPath:.onceToken.32814
- _transformValueExpression:forKeyPath:.onceToken.34212
- _transformValueExpression:forKeyPath:.onceToken.36435
- _transformValueExpression:forKeyPath:.onceToken.40287
- _transformValueExpression:forKeyPath:.onceToken.4364
- _transformValueExpression:forKeyPath:.onceToken.44460
- _transformValueExpression:forKeyPath:.onceToken.46196
- _transformValueExpression:forKeyPath:.onceToken.48089
- _transformValueExpression:forKeyPath:.onceToken.51053
- _transformValueExpression:forKeyPath:.onceToken.53502
CStrings:
+ "%@ to fetch asset collection with local identifier (%@) with invalid fetch type: %@"
+ "%@, URLRequest: %@ state: %hu clientStatus: %hu lastModifiedDate: %@ attemptCount: %hu"
+ "%@, state: %hu"
+ "%K != %hu"
+ "%K == %hu"
+ "%td change requests are invalid"
+ "@\"NSURLRequest\""
+ "@104@0:8Q16@24Q32B40B44@48@56@64@72@80@88@96"
+ "@20@0:8s16"
+ "@96@0:8Q16@24Q32B40B44@48@56@64@72@80@88"
+ "A change request should not be resetting OCR data set if it is setting new TU data."
+ "A change request should not have TU data set if it is being reset."
+ "An existing configuration record for the same bundle identifier was found"
+ "B16@?0@\"NSString\"8"
+ "B40@0:8@\"<PLPerformChangesRequestService>\"16@\"<PLClientAuthorization>\"24^@32"
+ "Cannot increment attemptCount more than its current value: %d"
+ "Cannot modify acknowledged job with uuid %@"
+ "Cannot reregister a job when attemptCount is %d"
+ "Change request XPC object is nil"
+ "Connection interrupted for %s"
+ "Connection invalidated for %s"
+ "Current state:%hu and acknowledgement:%hu.\nTarget state:%hu and acknowledgement:%hu.\n"
+ "Error while attempting to pair live photo assets in the library: %@"
+ "Failed to create AssetResourceUploadJobConfiguration - app missing extension"
+ "Failed to create AssetResourceUploadJobConfiguration - missing app record"
+ "Invalid configuration identifier"
+ "Local video key frame on demand repair"
+ "PHAssetPropertySetTextUnderstanding"
+ "PHAssetTextUnderstandingProperties"
+ "PHIncrementAttemptCountKey"
+ "PHResourceUploadShouldBypassValidateMutationsKey"
+ "PHSearchSuggestionProcessor"
+ "PLBackgroundResourceUploadExtensionXPCProtocol"
+ "Photos._PHBackgroundResourceUploadExtensionConfiguration"
+ "Q40@0:8@16@24^@32"
+ "ResourceUploadExtension"
+ "T@\"NSData\",R,N,V_textUnderstandingData"
+ "T@\"NSDate\",R,N,V_lastModifiedDate"
+ "T@\"NSString\",&,N,V_bundleIdentifier"
+ "T@\"NSURLRequest\",R,N,V_URLRequest"
+ "TB,N,V_skipExtensionValidation"
+ "Too many unacknowledged jobs. Please acknowledge jobs, or cancel pending ones"
+ "Tq,R,N,V_textUnderstandingVersion"
+ "Ts,R,N,V_attemptCount"
+ "Ts,R,N,V_clientStatus"
+ "URLRequest"
+ "Unexpected behavior: configuration always has an objectID. Flagging that here, configuration is a uuid: %@"
+ "_URLRequest"
+ "_attemptCount"
+ "_clientStatus"
+ "_commonInitializer"
+ "_confirmAppHasValidExtensionWithPhotoLibrary:error:"
+ "_countOfCancelableAcknowledgeableJobsWithConfiguration:library:error:"
+ "_didSetTextUnderstandingProperties"
+ "_getAcknowledgement"
+ "_getConfigurationFromLibrary:error:"
+ "_getState"
+ "_incrementAttemptCount"
+ "_queryForAssetResourceUploadJobsWithOptions:configuration:predicate:"
+ "_resetTextUnderstandingProperties"
+ "_shouldBypassValidateMutations"
+ "_skipExtensionValidation"
+ "_textUnderstandingData"
+ "_textUnderstandingVersion"
+ "acknowledgeJob:"
+ "appex"
+ "applicationExtensionRecords"
+ "archiveDataForURLRequest:"
+ "attemptCount"
+ "cancelJob:"
+ "characterRecognitionAttributes.textUnderstandingData"
+ "clientStatus"
+ "com.apple.plphotosctl"
+ "configurationStatusWithOptions:"
+ "configurationWithBundleIdentifier:managedObjectContext:error:"
+ "configurationWithObjectID:managedObjectContext:error:"
+ "configurationWithUUID:managedObjectContext:error:"
+ "creationRequestForAssetResourceUploadJobConfiguration"
+ "creationRequestForAssetResourceUploadJobConfigurationWithState:"
+ "creationRequestForAssetResourceUploadJobWithURLRequest:assetResource:"
+ "decodeData:error:"
+ "decodeWithService:clientAuthorization:error:"
+ "extensionPointIdentifier"
+ "fetchAssetResourceUploadJobsForConfiguration:options:"
+ "fetchAssetResourceUploadJobsWithAction:options:"
+ "fetchAssetResourceUploadJobsWithOptions:"
+ "generateAndStoreForAsset:options:progress:completion:"
+ "getCPLConfigurationValueForKey:completionHandler:"
+ "incrementAttemptCount"
+ "init()"
+ "initWithApplicationExtensionRecord:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:"
+ "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:creationDate:addedDate:matchedThumbnailIdentifier:"
+ "initWithVersion:taskIdentifier:reason:networkAccessAllowed:clientBundleID:"
+ "insertIntoManagedObjectContext:uuid:bundleID:"
+ "interfaceWithProtocol:"
+ "isUnitTesting"
+ "logger"
+ "longValue"
+ "maximumUnacknowledgedJobCountKey:"
+ "mediaAnalysisAttributes.characterRecognitionAttributes.textUnderstandingData"
+ "mediaAnalysisAttributes.textUnderstandingVersion"
+ "numberWithLong:"
+ "predicateForAcknowledgeableJobs"
+ "process:"
+ "processPairingForGroupIDs:inContext:error:"
+ "queryForAcknowledgeableAssetResourceUploadJobsWithConfiguration:options:"
+ "queryForAssetResourceUploadJobsWithConfiguration:states:options:"
+ "queryForRetryableAssetResourceUploadJobsWithConfiguration:options:"
+ "resetTextUnderstandingAttributes"
+ "resetTextUnderstandingProperties"
+ "resume"
+ "retryJob:withURLRequest:"
+ "setAttemptCount:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setOnlyClientStatus:"
+ "setOnlyState:"
+ "setSkipExtensionValidation:"
+ "setState:clientStatus:"
+ "setTextUnderstandingData:version:"
+ "skipExtensionValidation"
+ "textUnderstandingAlgorithmVersion = %ld\n"
+ "textUnderstandingData"
+ "textUnderstandingData = %p(.textUnderstandingData.length = %lu)\n"
+ "textUnderstandingProperties"
+ "textUnderstandingVersion"
+ "typesMaskForDeferredProcessingNeeded:"
+ "unknown identifier"
+ "updateClientStatus:"
+ "updateState:"
+ "v24@0:8@?<v@?Q>16"
+ "v24@0:8s16s20"
- "%@ not set. Defaulting to YES."
- "%@, bundleIdentifier: %@ state: %hu"
- "%@, requestData: %@ state: %hu "
- "%{public}@ %tu unexpected domain identifiers returned from Spotlight: %@"
- "%{public}@ Found %tu assets, %tu assets for suggestions, %tu albums, %tu highlights, and %tu memories from Spotlight for query: %@"
- "%{public}@ Found %tu collections below threshold. Collection UUIDs: %@"
- "%{public}@ No results to process for query: \"%@\""
- "%{public}@ Processed %tu asset results, %tu asset results for suggestions, and %tu collection results, %tu collection results for suggestions for query: %@"
- "%{public}@ Processing %tu items from Spotlight with %tu scoped identifiers"
- "%{public}@ Received %tu searchable item(s) with undefined type(s): %@"
- "%{public}@ Scoped search set is empty, no results to process for query \"%@\"."
- "%{public}@ Spotlight QU annotated query: \"%@\""
- "%{public}@ Spotlight Query Embedding: %@"
- "%{public}@ Spotlight returned %{public}tu items."
- "%{public}@ Updated collections with asset based collections: %tu albums, %tu highlights and %tu memories from Spotlight for query: %@"
- "3EP0"
- "@\"PHObjectPlaceholder\""
- "@120@0:8Q16@24Q32B40B44@48@56@64@72@80@88@96@104@112"
- "@128@0:8Q16@24Q32B40B44@48@56@64@72@80@88@96@104@112@120"
- "@40@0:8@16@24f32f36"
- "@40@0:8@16Q24i32i36"
- "Asset Resource cannot be nil."
- "Error while attempting to pair CTM assets in the library: %@"
- "PHSearchBatchResultProcessingEnabled"
- "PHSearchProcessor"
- "PHSearchProcessor.m"
- "PLAssetResourceURLRequestRequestKey"
- "PLAssetResourceUploadVersionKey"
- "PLSearchBackendQuerySearchableItemTranslation"
- "Query: %d, Batch: %d, CSSearchableItems: %tu, PHSearchResults: %tu"
- "Received searchableItem with invalid result type: %@"
- "Selected ThumbnailID: %@, for assetUUID: %@, and lookupIdentifiers: %@"
- "Serialized Data: %{public}s"
- "SharedStreamCollectionShareSupport"
- "T@\"NSArray\",R,N,V_assetAlbumUUIDs"
- "T@\"NSArray\",R,N,V_assetHighlightUUIDs"
- "T@\"NSArray\",R,N,V_assetMemoryUUIDs"
- "T@\"NSData\",R,N,V_requestData"
- "T@\"PHObjectPlaceholder\",R,N,V_placeholderForCreatedAssetResourceUploadJobConfiguration"
- "Unexpected attribute found in photosComputedAttributesHandler. Attribute: %@, values: %@"
- "_albumUUIDsFromAssetBasedSearchResults:"
- "_assetAlbumUUIDs"
- "_assetHighlightUUIDs"
- "_assetMemoryUUIDs"
- "_collectionUUIDsForSpotlightSearchableItem:identifiersKey:countsKey:assetCountByCollectionUUID:"
- "_commonInitalizer"
- "_executeSpotlightSearchWithResultsHandler:"
- "_fetchTypeForLocalIdentifiers:"
- "_filterResultsByMatchType:forQuery:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:"
- "_highlightUUIDsFromAssetBasedSearchResults:"
- "_memoryUUIDsFromAssetBasedSearchResults:"
- "_placeholderForCreatedAssetResourceUploadJobConfiguration"
- "_rankedAssetSearchResultsFromResults:maxResults:queryId:batchId:"
- "_rankedCollectionSearchResultsFromResults:maxResults:queryId:batchId:"
- "_removeTransientProcessingStateForSearchResults:"
- "_requestData"
- "_searchResultFromSpotlightSearchableItem:queryOptions:matchedLookupIdentifiers:assetCountByCollectionUUID:"
- "assetAlbumUUIDs"
- "assetHighlightUUIDs"
- "assetMemoryUUIDs"
- "countsKey"
- "creationRequestForAssetResourceUploadJobConfigurationWithBundleIdentifier:"
- "creationRequestForAssetResourceUploadJobConfigurationWithBundleIdentifier:state:"
- "creationRequestForAssetResourceUploadJobWithURLRequest:configuration:assetResource:error:"
- "decodeWithService:clientAuthorization:"
- "failedAttemptCount"
- "fetchAssetResourceUploadJobsWithConfiguration:options:"
- "finishEncoding"
- "generateAndStoreForAsset:networkAccessAllowed:clientBundleID:progress:completion:"
- "getCPLConfigrationValueForKey:completionHandler:"
- "identifiersKey"
- "initForNewObjectWithRequestData:"
- "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:"
- "initWithSearchResultType:uuid:retrievalType:hasOCRTextMatch:isSensitiveLocation:embeddingDistances:l1Score:l2Score:collectionScore:assetAlbumUUIDs:assetMemoryUUIDs:assetHighlightUUIDs:creationDate:addedDate:matchedThumbnailIdentifier:"
- "initWithUUID:objectID:requestData:"
- "lastRetryDate"
- "outAssetUUIDsForSuggestions"
- "outCollectionUUIDsForSuggestions"
- "outRankedAssetSearchResults"
- "outRankedCollectionSearchResults"
- "outSearchResults"
- "outUnfilteredAssetSearchResults"
- "placeholderForCreatedAssetResourceUploadJobConfiguration"
- "processPairingForGroupIDs:inContext:deferredProcessingNeeded:error:"
- "releaseOwningCollectionUUIDs"
- "searchResultsFromSpotlightSearchableItems:query:annotatedQueryString:searchResults:unfilteredAssetSearchResults:rankedAssetSearchResults:rankedCollectionSearchResults:assetUUIDsForSuggestions:collectionUUIDsForSuggestions:highPrecisionEmbeddingDistanceThreshold:veryHighPrecisionEmbeddingDistanceThreshold:scopedUUIDs:matchedLookupIdentifiers:"
- "setFailedAttemptCount:"
- "setLastRetryDate:"
- "signalBackgroundProcessingNeededOnLibrary:"
- "sortUsingDescriptors:"
- "v112@0:8@16@24@32o^@40o^@48o^@56o^@64o^@72o^@80f88f92@96@104"
- "v24@?0Q8@\"NSCountedSet\"16"
- "v32@0:8@\"<PLPerformChangesRequestService>\"16@\"<PLClientAuthorization>\"24"
- "v32@?0@\"CSSearchableItem\"8Q16^B24"

```
