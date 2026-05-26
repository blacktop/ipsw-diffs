## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-405.3.1.0.0
-  __TEXT.__text: 0x3e53a4
+415.5.1.0.0
+  __TEXT.__text: 0x3eb078
   __TEXT.__auth_stubs: 0x3f60
   __TEXT.__delay_stubs: 0xc0
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x1d258
-  __TEXT.__const: 0x14ca8
-  __TEXT.__gcc_except_tab: 0x56e1c
-  __TEXT.__cstring: 0x1aa64
-  __TEXT.__oslogstring: 0x281bb
+  __TEXT.__objc_methlist: 0x1d660
+  __TEXT.__const: 0x14d28
+  __TEXT.__gcc_except_tab: 0x57494
+  __TEXT.__cstring: 0x1add1
+  __TEXT.__oslogstring: 0x2865b
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x3b8

   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x11730
+  __TEXT.__unwind_info: 0x11800
   __TEXT.__eh_frame: 0x928
-  __TEXT.__objc_classname: 0x4588
-  __TEXT.__objc_methname: 0x3db01
-  __TEXT.__objc_methtype: 0xd02a
-  __TEXT.__objc_stubs: 0x29dc0
-  __DATA_CONST.__got: 0x1d00
-  __DATA_CONST.__const: 0x6828
-  __DATA_CONST.__objc_classlist: 0x12b0
+  __TEXT.__objc_classname: 0x4678
+  __TEXT.__objc_methname: 0x3e5a1
+  __TEXT.__objc_methtype: 0xd0da
+  __TEXT.__objc_stubs: 0x2a320
+  __DATA_CONST.__got: 0x1d18
+  __DATA_CONST.__const: 0x68e0
+  __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xccd8
+  __DATA_CONST.__objc_selrefs: 0xceb0
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xee8
-  __DATA_CONST.__objc_arraydata: 0x11e0
+  __DATA_CONST.__objc_superrefs: 0xef8
+  __DATA_CONST.__objc_arraydata: 0x1238
   __AUTH_CONST.__auth_got: 0x1fe0
-  __AUTH_CONST.__const: 0x47c8
-  __AUTH_CONST.__cfstring: 0x171c0
-  __AUTH_CONST.__objc_const: 0x389e0
+  __AUTH_CONST.__const: 0x4808
+  __AUTH_CONST.__cfstring: 0x17500
+  __AUTH_CONST.__objc_const: 0x39290
   __AUTH_CONST.__objc_floatobj: 0x290
   __AUTH_CONST.__objc_doubleobj: 0x480
-  __AUTH_CONST.__objc_intobj: 0x2f10
-  __AUTH_CONST.__objc_arrayobj: 0xc18
+  __AUTH_CONST.__objc_intobj: 0x2f88
+  __AUTH_CONST.__objc_arrayobj: 0xc60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2070
+  __AUTH.__objc_data: 0x22f0
   __AUTH.__data: 0x1d8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x32b4
-  __DATA.__data: 0x1a94
-  __DATA.__bss: 0xaa9
+  __DATA.__objc_ivar: 0x32fc
+  __DATA.__data: 0x1a9c
+  __DATA.__bss: 0xab9
   __DATA.__common: 0x3c1
   __DATA_DIRTY.__objc_data: 0x9ca0
   __DATA_DIRTY.__data: 0x150

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9D656B76-B0D7-3F50-88CA-45BE5925904D
-  Functions: 13480
-  Symbols:   48732
-  CStrings:  21564
+  UUID: 342275D9-71E5-3DEF-91E5-3861E964F8FF
+  Functions: 13561
+  Symbols:   49029
+  CStrings:  21743
 
Symbols:
+ +[MADEmbedding prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:]
+ +[MADEmbedding searchWithQueryTexts:photoLibraryURL:options:error:]
+ +[MADEmbeddingSearchQueryResult supportsSecureCoding]
+ +[MADEmbeddingStore _madEmbeddingsFromGroupedVSKAssets:]
+ +[MADEmbeddingStore _madEmbeddingsWithThumbnailIdsFromMADBForLibrary:pairedVSKAssets:]
+ +[MADEmbeddingStore preferredImageEmbeddings:versions:forAssetUUID:fromImageEmbeddingResults:error:]
+ +[MADEmbeddingStore preferredVideoEmbeddings:versions:embeddingIndices:thumbnailIdentifiers:forAssetUUID:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:]
+ +[MADEmbeddingStoreService _embeddingSimilarityThresholdForVersion:similarityLevel:]
+ +[MADQuerySafetyResult supportsSecureCoding]
+ +[MADTextEmbeddingMD8DefaultResource sharedResourceWithComputeUnits:]
+ +[MADTextEmbeddingMD8ExtendedResource extendedContextLength]
+ +[MADTextEmbeddingMD8ExtendedResource sharedResourceWithComputeUnits:]
+ +[MADTextEmbeddingMD8Resource revision]
+ +[MADTextEmbeddingSafetyMD8 embeddingLength]
+ +[MADTextEmbeddingSafetyMD8 embeddingVersion]
+ +[MADTextEmbeddingSafetyMD8 modelName]
+ +[MADTextEmbeddingSafetyMD8 threshold]
+ +[MADTextEmbeddingThresholdMD8 embeddingLength]
+ +[MADTextEmbeddingThresholdMD8 embeddingVersion]
+ +[MADTextEmbeddingThresholdMD8 modelName]
+ +[MADTextEmbeddingThresholdMD8 thresholdBase]
+ +[MADTextTokenizerMD8Resource sharedResource]
+ +[MADVectorDatabase _vectorDataTypeForEmbeddingType:]
+ +[MADVectorDatabase _vectorDimensionForEmbeddingType:]
+ +[MADVectorDatabase databaseWithDirectoryURL:readOnly:databaseVersion:embeddingType:]
+ +[MADVectorDatabaseManager _databaseDirectoryURLForPhotoLibrary:embeddingType:]
+ +[MADVectorDatabaseManager _databaseVersionForEmbeddingType:]
+ +[MADVectorDatabaseManager _databaseVersionForVisualEmbedding]
+ +[MADVectorDatabaseManager _historicalFolderNames]
+ +[MADVectorDatabaseManager databaseDirectoryURLForPhotoLibrary:embeddingType:]
+ +[MADVectorDatabaseManager sharedDatabaseWithPhotoLibrary:embeddingType:]
+ +[VCPVideoTransformerBackbone revision].cold.1
+ +[VSKAttribute(MediaAnalysis) mad_embeddingIndexAttributeName]
+ +[VSKAttribute(MediaAnalysis) mad_embeddingIndexAttribute]
+ +[VSKAttribute(MediaAnalysis) mad_thumbnailIdentifierAttributeName]
+ +[VSKAttribute(MediaAnalysis) mad_thumbnailIdentifierAttribute]
+ -[MADEmbeddingFetchOptions description]
+ -[MADEmbeddingFetchOptions forceXPC]
+ -[MADEmbeddingFetchOptions setForceXPC:]
+ -[MADEmbeddingSearchOptions checkSafety]
+ -[MADEmbeddingSearchOptions embeddingSourceTypes]
+ -[MADEmbeddingSearchOptions forceXPC]
+ -[MADEmbeddingSearchOptions searchMode]
+ -[MADEmbeddingSearchOptions setCheckSafety:]
+ -[MADEmbeddingSearchOptions setEmbeddingSourceTypes:]
+ -[MADEmbeddingSearchOptions setForceXPC:]
+ -[MADEmbeddingSearchOptions setSearchMode:]
+ -[MADEmbeddingSearchQueryResult .cxx_destruct]
+ -[MADEmbeddingSearchQueryResult description]
+ -[MADEmbeddingSearchQueryResult encodeWithCoder:]
+ -[MADEmbeddingSearchQueryResult error]
+ -[MADEmbeddingSearchQueryResult initWithCoder:]
+ -[MADEmbeddingSearchQueryResult initWithQueryText:querySafetyResult:queryEmbedding:sortedResults:error:]
+ -[MADEmbeddingSearchQueryResult queryEmbedding]
+ -[MADEmbeddingSearchQueryResult querySafetyResult]
+ -[MADEmbeddingSearchQueryResult queryText]
+ -[MADEmbeddingSearchQueryResult sortedResults]
+ -[MADEmbeddingSearchResult embeddingIndices]
+ -[MADEmbeddingSearchResult embeddingSourceType]
+ -[MADEmbeddingSearchResult initWithAssetUUID:similarity:metric:embeddingSourceType:similarityLevel:embeddingIndices:thumbnailIdentifiers:]
+ -[MADEmbeddingSearchResult setSimilarity:]
+ -[MADEmbeddingSearchResult setSimilarityLevel:]
+ -[MADEmbeddingSearchResult similarityLevel]
+ -[MADEmbeddingSearchResult similarity]
+ -[MADEmbeddingSearchResult thumbnailIdentifiers]
+ -[MADEmbeddingStoreService _isEmbeddingSourceTypeRequested:inOptions:]
+ -[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:]
+ -[MADEmbeddingStoreService searchWithQueryTexts:photoLibraryURL:options:error:]
+ -[MADQuerySafetyResult description]
+ -[MADQuerySafetyResult encodeWithCoder:]
+ -[MADQuerySafetyResult initWithCoder:]
+ -[MADQuerySafetyResult initWithSafetyState:semanticSafetyScore:]
+ -[MADQuerySafetyResult safetyState]
+ -[MADQuerySafetyResult semanticSafetyScore]
+ -[MADTextEmbeddingMD8Resource calibrationVersion]
+ -[MADTextEmbeddingMD8Resource tokenEmbeddingType]
+ -[MADTextEmbeddingMD8Resource version]
+ -[MADTextTokenizerMD8Resource version]
+ -[MADVectorDatabase _openVSKClientsWithTargetVersion:embeddingType:]
+ -[MADVectorDatabase _vectorDatabaseReadOnlyConfig]
+ -[MADVectorDatabase _vectorDatabaseReadWriteConfigWithTargetVersion:]
+ -[MADVectorDatabase initWithDirectoryURL:readyOnly:databaseVersion:embeddingType:]
+ -[MADVectorDatabaseManager _createDatabaseForPhotoLibrary:embeddingType:]
+ -[MADVectorDatabaseManager _purgeHistoricalDataForPhotoLibrary:]
+ -[MADVectorDatabaseManager _sharedDatabaseWithPhotoLibrary:embeddingType:]
+ -[VCPVideoTransformerBackbone patchEmbedding]
+ -[VSKAsset(MediaAnalysis) mad_embeddingIndexArray]
+ -[VSKAsset(MediaAnalysis) mad_thumbnailIdentifierArray]
+ -[VSKAttribute(MediaAnalysis) mad_isEmbeddingIndexAttribute]
+ -[VSKAttribute(MediaAnalysis) mad_isThumbnailIdentifierAttribute]
+ _MADImageEmbeddingIndex
+ _OBJC_CLASS_$_MADEmbeddingSearchQueryResult
+ _OBJC_CLASS_$_MADQuerySafetyResult
+ _OBJC_CLASS_$_MADTextEmbeddingMD8DefaultResource
+ _OBJC_CLASS_$_MADTextEmbeddingMD8ExtendedResource
+ _OBJC_CLASS_$_MADTextEmbeddingMD8Resource
+ _OBJC_CLASS_$_MADTextEmbeddingSafetyMD8
+ _OBJC_CLASS_$_MADTextEmbeddingThresholdMD8
+ _OBJC_CLASS_$_MADTextInput
+ _OBJC_CLASS_$_MADTextTokenizerMD8Resource
+ _OBJC_IVAR_$_MADEmbeddingFetchOptions._forceXPC
+ _OBJC_IVAR_$_MADEmbeddingSearchOptions._checkSafety
+ _OBJC_IVAR_$_MADEmbeddingSearchOptions._embeddingSourceTypes
+ _OBJC_IVAR_$_MADEmbeddingSearchOptions._forceXPC
+ _OBJC_IVAR_$_MADEmbeddingSearchOptions._searchMode
+ _OBJC_IVAR_$_MADEmbeddingSearchQueryResult._error
+ _OBJC_IVAR_$_MADEmbeddingSearchQueryResult._queryEmbedding
+ _OBJC_IVAR_$_MADEmbeddingSearchQueryResult._querySafetyResult
+ _OBJC_IVAR_$_MADEmbeddingSearchQueryResult._queryText
+ _OBJC_IVAR_$_MADEmbeddingSearchQueryResult._sortedResults
+ _OBJC_IVAR_$_MADEmbeddingSearchResult._embeddingIndices
+ _OBJC_IVAR_$_MADEmbeddingSearchResult._embeddingSourceType
+ _OBJC_IVAR_$_MADEmbeddingSearchResult._similarity
+ _OBJC_IVAR_$_MADEmbeddingSearchResult._similarityLevel
+ _OBJC_IVAR_$_MADEmbeddingSearchResult._thumbnailIdentifiers
+ _OBJC_IVAR_$_MADQuerySafetyResult._safetyState
+ _OBJC_IVAR_$_MADQuerySafetyResult._semanticSafetyScore
+ _OBJC_IVAR_$_MADVectorDatabase._embeddingSourceType
+ _OBJC_IVAR_$_VCPVideoTransformerBackbone._patchEmbedding
+ _OBJC_METACLASS_$_MADEmbeddingSearchQueryResult
+ _OBJC_METACLASS_$_MADQuerySafetyResult
+ _OBJC_METACLASS_$_MADTextEmbeddingMD8DefaultResource
+ _OBJC_METACLASS_$_MADTextEmbeddingMD8ExtendedResource
+ _OBJC_METACLASS_$_MADTextEmbeddingMD8Resource
+ _OBJC_METACLASS_$_MADTextEmbeddingSafetyMD8
+ _OBJC_METACLASS_$_MADTextEmbeddingThresholdMD8
+ _OBJC_METACLASS_$_MADTextTokenizerMD8Resource
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_VSKAttribute_$_MediaAnalysis
+ __OBJC_$_CLASS_METHODS_MADEmbeddingSearchQueryResult
+ __OBJC_$_CLASS_METHODS_MADQuerySafetyResult
+ __OBJC_$_CLASS_METHODS_MADTextEmbeddingMD8DefaultResource
+ __OBJC_$_CLASS_METHODS_MADTextEmbeddingMD8ExtendedResource
+ __OBJC_$_CLASS_METHODS_MADTextEmbeddingMD8Resource
+ __OBJC_$_CLASS_METHODS_MADTextEmbeddingSafetyMD8
+ __OBJC_$_CLASS_METHODS_MADTextEmbeddingThresholdMD8
+ __OBJC_$_CLASS_METHODS_MADTextTokenizerMD8Resource
+ __OBJC_$_CLASS_PROP_LIST_MADEmbeddingSearchQueryResult
+ __OBJC_$_CLASS_PROP_LIST_MADQuerySafetyResult
+ __OBJC_$_INSTANCE_METHODS_MADEmbeddingSearchQueryResult
+ __OBJC_$_INSTANCE_METHODS_MADQuerySafetyResult
+ __OBJC_$_INSTANCE_METHODS_MADTextEmbeddingMD8Resource
+ __OBJC_$_INSTANCE_METHODS_MADTextTokenizerMD8Resource
+ __OBJC_$_INSTANCE_VARIABLES_MADEmbeddingFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_MADEmbeddingSearchQueryResult
+ __OBJC_$_INSTANCE_VARIABLES_MADQuerySafetyResult
+ __OBJC_$_PROP_LIST_MADEmbeddingFetchOptions
+ __OBJC_$_PROP_LIST_MADEmbeddingSearchQueryResult
+ __OBJC_$_PROP_LIST_MADQuerySafetyResult
+ __OBJC_CLASS_PROTOCOLS_$_MADEmbeddingSearchQueryResult
+ __OBJC_CLASS_PROTOCOLS_$_MADQuerySafetyResult
+ __OBJC_CLASS_RO_$_MADEmbeddingSearchQueryResult
+ __OBJC_CLASS_RO_$_MADQuerySafetyResult
+ __OBJC_CLASS_RO_$_MADTextEmbeddingMD8DefaultResource
+ __OBJC_CLASS_RO_$_MADTextEmbeddingMD8ExtendedResource
+ __OBJC_CLASS_RO_$_MADTextEmbeddingMD8Resource
+ __OBJC_CLASS_RO_$_MADTextEmbeddingSafetyMD8
+ __OBJC_CLASS_RO_$_MADTextEmbeddingThresholdMD8
+ __OBJC_CLASS_RO_$_MADTextTokenizerMD8Resource
+ __OBJC_METACLASS_RO_$_MADEmbeddingSearchQueryResult
+ __OBJC_METACLASS_RO_$_MADQuerySafetyResult
+ __OBJC_METACLASS_RO_$_MADTextEmbeddingMD8DefaultResource
+ __OBJC_METACLASS_RO_$_MADTextEmbeddingMD8ExtendedResource
+ __OBJC_METACLASS_RO_$_MADTextEmbeddingMD8Resource
+ __OBJC_METACLASS_RO_$_MADTextEmbeddingSafetyMD8
+ __OBJC_METACLASS_RO_$_MADTextEmbeddingThresholdMD8
+ __OBJC_METACLASS_RO_$_MADTextTokenizerMD8Resource
+ __ZZ39+[VCPVideoTransformerBackbone revision]E4once
+ __ZZ39+[VCPVideoTransformerBackbone revision]E8revision
+ __ZZ45+[MADTextEmbeddingThresholdMD8 thresholdBase]E13thresholdBase
+ __ZZ45+[MADTextEmbeddingThresholdMD8 thresholdBase]E4once
+ ___39+[VCPVideoTransformerBackbone revision]_block_invoke
+ ___45+[MADTextEmbeddingThresholdMD8 thresholdBase]_block_invoke
+ ___45+[MADTextTokenizerMD8Resource sharedResource]_block_invoke
+ ___68-[MADVectorDatabase _openVSKClientsWithTargetVersion:embeddingType:]_block_invoke
+ ___69+[MADTextEmbeddingMD8DefaultResource sharedResourceWithComputeUnits:]_block_invoke
+ ___70+[MADTextEmbeddingMD8ExtendedResource sharedResourceWithComputeUnits:]_block_invoke
+ ___74-[MADVectorDatabaseManager _sharedDatabaseWithPhotoLibrary:embeddingType:]_block_invoke
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.760
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.773
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.778
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.783
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.788
+ ___79-[MADEmbeddingStoreService searchWithEmbeddings:photoLibraryURL:options:error:]_block_invoke.265
+ ___79-[MADEmbeddingStoreService searchWithQueryTexts:photoLibraryURL:options:error:]_block_invoke
+ ___86+[MADEmbeddingStore _madEmbeddingsWithThumbnailIdsFromMADBForLibrary:pairedVSKAssets:]_block_invoke
+ ___88-[MADEmbeddingStoreService fetchEmbeddingsWithAssetUUIDs:photoLibraryURL:options:error:]_block_invoke.261
+ ___89-[MADVectorDatabase rebuildWithForce:cancelBlock:extendTimeoutBlock:totalEmbeddingCount:]_block_invoke.414
+ ___92-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:]_block_invoke
+ ___92-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:]_block_invoke.269
+ ___block_descriptor_32_e34_"MADTextTokenizerMD8Resource"8?0l
+ ___block_descriptor_40_e41_"MADTextEmbeddingMD8DefaultResource"8?0l
+ ___block_descriptor_40_e42_"MADTextEmbeddingMD8ExtendedResource"8?0l
+ ___block_descriptor_48_ea8_32r40r_e20_v20?0i8"NSError"12lr32l8r40l8
+ ___block_descriptor_80_ea8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_80_ea8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_96_ea8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_literal_global.220
+ _objc_msgSend$_createDatabaseForPhotoLibrary:embeddingType:
+ _objc_msgSend$_databaseDirectoryURLForPhotoLibrary:embeddingType:
+ _objc_msgSend$_databaseVersionForEmbeddingType:
+ _objc_msgSend$_databaseVersionForVisualEmbedding
+ _objc_msgSend$_embeddingSimilarityThresholdForVersion:similarityLevel:
+ _objc_msgSend$_historicalFolderNames
+ _objc_msgSend$_isEmbeddingSourceTypeRequested:inOptions:
+ _objc_msgSend$_madEmbeddingsFromGroupedVSKAssets:
+ _objc_msgSend$_madEmbeddingsWithThumbnailIdsFromMADBForLibrary:pairedVSKAssets:
+ _objc_msgSend$_openVSKClientsWithTargetVersion:embeddingType:
+ _objc_msgSend$_sharedDatabaseWithPhotoLibrary:embeddingType:
+ _objc_msgSend$_vectorDataTypeForEmbeddingType:
+ _objc_msgSend$_vectorDatabaseReadOnlyConfig
+ _objc_msgSend$_vectorDatabaseReadWriteConfigWithTargetVersion:
+ _objc_msgSend$_vectorDimensionForEmbeddingType:
+ _objc_msgSend$bias
+ _objc_msgSend$checkSafety
+ _objc_msgSend$databaseDirectoryURLForPhotoLibrary:embeddingType:
+ _objc_msgSend$databaseWithDirectoryURL:readOnly:databaseVersion:embeddingType:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$embeddingResults
+ _objc_msgSend$embeddingSourceTypes
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$forceXPC
+ _objc_msgSend$getStringValue
+ _objc_msgSend$initWithAssetUUID:similarity:metric:embeddingSourceType:similarityLevel:embeddingIndices:thumbnailIdentifiers:
+ _objc_msgSend$initWithDirectoryURL:readyOnly:databaseVersion:embeddingType:
+ _objc_msgSend$initWithQueryText:querySafetyResult:queryEmbedding:sortedResults:error:
+ _objc_msgSend$initWithSafetyState:semanticSafetyScore:
+ _objc_msgSend$initWithStringIdentifier:vectors:perVectorAttribute:payload:
+ _objc_msgSend$initWithText:
+ _objc_msgSend$isSafe
+ _objc_msgSend$mad_embeddingIndexAttribute
+ _objc_msgSend$mad_embeddingIndexAttributeName
+ _objc_msgSend$mad_isEmbeddingIndexAttribute
+ _objc_msgSend$mad_isThumbnailIdentifierAttribute
+ _objc_msgSend$mad_thumbnailIdentifierArray
+ _objc_msgSend$mad_thumbnailIdentifierAttribute
+ _objc_msgSend$mad_thumbnailIdentifierAttributeName
+ _objc_msgSend$perVectorAttribute
+ _objc_msgSend$performRequests:textInputs:completionHandler:
+ _objc_msgSend$preferredImageEmbeddings:versions:forAssetUUID:fromImageEmbeddingResults:error:
+ _objc_msgSend$preferredVideoEmbeddings:versions:embeddingIndices:thumbnailIdentifiers:forAssetUUID:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:
+ _objc_msgSend$prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:
+ _objc_msgSend$safetyScore
+ _objc_msgSend$scale
+ _objc_msgSend$searchByBatch:stringIdentifiers:attributeFilters:selectAttributes:limit:fullScan:includePayload:numberOfProbes:batchSize:numConcurrentReaders:error:
+ _objc_msgSend$searchMode
+ _objc_msgSend$searchWithQueryTexts:photoLibraryURL:options:error:
+ _objc_msgSend$setComputeSafety:
+ _objc_msgSend$setComputeThreshold:
+ _objc_msgSend$setSimilarity:
+ _objc_msgSend$setSimilarityLevel:
+ _objc_msgSend$sharedDatabaseWithPhotoLibrary:embeddingType:
+ _objc_msgSend$similarity
+ _objc_msgSend$stringIdentifiedAssetsWithIdentifiers:attributeFilters:pagination:includeVectors:selectAttributes:error:
- +[MADEmbeddingStore preferredImageEmbeddingsForAssetUUID:version:fromImageEmbeddingResults:error:]
- +[MADEmbeddingStore preferredVideoEmbeddingsForAssetUUID:version:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:]
- +[MADVectorDatabase _vectorDatabaseVersion]
- +[MADVectorDatabase databaseDirectoryURLForPhotoLibrary:]
- +[MADVectorDatabase databaseWithPhotoLibrary:readyOnly:]
- +[MADVectorDatabase historicalFolderNames]
- +[MADVectorDatabaseManager sharedDatabaseWithPhotoLibrary:]
- -[MADEmbeddingSearchResult initWithAssetUUID:distance:metric:]
- -[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]
- -[MADVectorDatabase _openVSKClientWithError:]
- -[MADVectorDatabase _purgeHistoricalData]
- -[MADVectorDatabase _vectorDatabaseReadOnlyConfigWithError:]
- -[MADVectorDatabase _vectorDatabaseReadWriteConfigWithError:]
- -[MADVectorDatabase initWithPhotoLibrary:readyOnly:]
- -[MADVectorDatabaseManager sharedDatabaseWithPhotoLibrary:]
- _OBJC_IVAR_$_MADVectorDatabase._photoLibrary
- ___45-[MADVectorDatabase _openVSKClientWithError:]_block_invoke
- ___59-[MADVectorDatabaseManager sharedDatabaseWithPhotoLibrary:]_block_invoke
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.755
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.762
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.775
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.780
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.785
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.790
- ___79-[MADEmbeddingStoreService searchWithEmbeddings:photoLibraryURL:options:error:]_block_invoke.263
- ___81+[MADEmbeddingStore fetchEmbeddingsWithAssetUUIDs:photoLibraryURL:options:error:]_block_invoke
- ___84-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]_block_invoke
- ___84-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]_block_invoke.267
- ___88-[MADEmbeddingStoreService fetchEmbeddingsWithAssetUUIDs:photoLibraryURL:options:error:]_block_invoke.259
- ___89-[MADVectorDatabase rebuildWithForce:cancelBlock:extendTimeoutBlock:totalEmbeddingCount:]_block_invoke.449
- ___block_descriptor_80_ea8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_96_ea8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- _objc_msgSend$_openVSKClientWithError:
- _objc_msgSend$_purgeHistoricalData
- _objc_msgSend$_vectorDatabaseReadOnlyConfigWithError:
- _objc_msgSend$_vectorDatabaseReadWriteConfigWithError:
- _objc_msgSend$_vectorDatabaseVersion
- _objc_msgSend$databaseDirectoryURLForPhotoLibrary:
- _objc_msgSend$databaseWithPhotoLibrary:readyOnly:
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$historicalFolderNames
- _objc_msgSend$initWithAssetUUID:distance:metric:
- _objc_msgSend$initWithPhotoLibrary:readyOnly:
- _objc_msgSend$preferredImageEmbeddingsForAssetUUID:version:fromImageEmbeddingResults:error:
- _objc_msgSend$preferredVideoEmbeddingsForAssetUUID:version:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:
- _objc_msgSend$sharedDatabaseWithPhotoLibrary:
CStrings:
+ " (forceXPC)"
+ "%@ Mismatching image embedding count (%d) and version count (%d)"
+ "%@ Mismatching summarized embedding indices count (%d) and thumbnail IDs count (%d)"
+ "%@ Mismatching video segement embedding count (%d) and version count (%d)"
+ "%@ Mismatching video summarized embedding count (%d) and embedding index count (%d)"
+ "%@ Mismatching video summarized embedding count (%d) and thumbnail identifier count (%d)"
+ "%@ Mismatching video summarized embedding count (%d) and version count (%d)"
+ "%@ No valid video summarized embeddings (total %d, indices %@)"
+ "%@: %f>"
+ "%@: [%@], "
+ "%@[%@] Asset has %d embeddings, %d thumbnail identifiers"
+ "%@[%@] Invalid embedding type for VSKAsset %@"
+ "%@[%@] Mismatching embedding data count %d with thumbnail identifiers count %d, skip setting thumbnail identifiers"
+ "%@[%@] No embedding in VSKAsset %@"
+ "@\"MADEmbeddingResult\""
+ "@\"MADQuerySafetyResult\""
+ "@\"MADTextEmbeddingMD8DefaultResource\"8@?0"
+ "@\"MADTextEmbeddingMD8ExtendedResource\"8@?0"
+ "@\"MADTextTokenizerMD8Resource\"8@?0"
+ "@28@0:8Q16f24"
+ "@44@0:8@16B24@28Q36"
+ "@72@0:8@16@24q32Q40Q48@56@64"
+ "B32@0:8Q16@24"
+ "B56@0:8^@16^@24@32@40^@48"
+ "B88@0:8^@16^@24^@32^@40@48@56@64@72^@80"
+ "CheckSafety"
+ "EmbeddingIndices"
+ "EmbeddingSourceType"
+ "EmbeddingSourceTypes"
+ "Failed to generate text embedding for query: %@"
+ "ForceXPC"
+ "MADEmbeddingSearchQueryResult"
+ "MADQuerySafetyResult"
+ "MADTextEmbeddingMD8DefaultResource"
+ "MADTextEmbeddingMD8ExtendedResource"
+ "MADTextEmbeddingMD8Resource"
+ "MADTextEmbeddingSafetyMD8"
+ "MADTextEmbeddingThresholdMD8"
+ "MADTextTokenizerMD8Resource"
+ "QueryEmbedding"
+ "QuerySafetyResult"
+ "QueryText"
+ "Safety only supported for MD5-MD8"
+ "SafetyState"
+ "SearchMode"
+ "SearchUnifiedEmbeddingMD8"
+ "SemanticSafetyScore"
+ "Similarity"
+ "SimilarityLevel"
+ "SortedResults"
+ "T@\"MADEmbeddingResult\",R,N,V_queryEmbedding"
+ "T@\"MADQuerySafetyResult\",R,N,V_querySafetyResult"
+ "T@\"NSArray\",R,N,V_embeddingIndices"
+ "T@\"NSArray\",R,N,V_sortedResults"
+ "T@\"NSData\",R,V_patchEmbedding"
+ "T@\"NSNumber\",R,N,V_similarity"
+ "T@\"NSSet\",C,N,V_embeddingSourceTypes"
+ "T@\"NSString\",R,N,V_queryText"
+ "TB,N,V_checkSafety"
+ "TB,N,V_forceXPC"
+ "TQ,N,V_searchMode"
+ "TQ,R,N,V_embeddingSourceType"
+ "TQ,R,N,V_safetyState"
+ "TQ,R,N,V_similarityLevel"
+ "Tf,R,N,V_semanticSafetyScore"
+ "Threshold calibration only supported for MD3-MD8"
+ "VCPImageEmbeddingRequest only supports revision 9 (MD7) and revision 10 (MD8)"
+ "[MADEmbeddingStoreService] Performing XPC embedding fetching for %u assets%s"
+ "[MADEmbeddingStoreService] Performing XPC prewarm with concurrencyLimit %u%s"
+ "[MADEmbeddingStoreService] Skipping search due to text embedding generation failure: %@"
+ "[MADEmbeddingStoreService] Visual embedding search failed: %@"
+ "[MADEmbeddingStoreService] XPC search with %llu embeddings%s"
+ "[MADEmbeddingStore|LegacyFetch]"
+ "[MADEmbedding] Invalid input for queryTexts: %@"
+ "[MUBackbone] Backbone revision set to %d"
+ "[VSKAsset+MediaAnalysis] No embeddingIndex attribute found in perVectorAttribute[%d]"
+ "[VSKAsset+MediaAnalysis] No per-vector attribute found"
+ "[VSKAsset+MediaAnalysis] No thumbnailIdentifier attribute found in perVectorAttribute[%d]"
+ "[VSKDBManager] Embedding generation disabled, skip vector database creation"
+ "[VSKDBManager] Failed to open database (embedding type: %d) for photo library %@"
+ "[VSKDBManager] Failed to remove %@: %@"
+ "[VSKDBManager] Failed to retrieve path for Photo Library %@"
+ "[VSKDBManager] Invalid media analysis directory %@"
+ "[VSKDBManager] Releasing shared database for %@"
+ "[VSKDBManager] Removed %@"
+ "[VSKDBManager] Unknown vectorDB folder name for embedding type %d"
+ "[VSKDBManager] Unknown vectorDB version for embedding type %d"
+ "[VSKDBManager][VisualEmbedding] Target version: %@"
+ "[VSKDB] Failed to initialize %@ v%@ database"
+ "[VSKDB] Unable to initialize vector database with abbreviated initializer - %@"
+ "[VSKDB] Unknown data type for embedding type %d"
+ "[VSKDB] Unknown dimension for embedding type %d"
+ "_checkSafety"
+ "_createDatabaseForPhotoLibrary:embeddingType:"
+ "_databaseDirectoryURLForPhotoLibrary:embeddingType:"
+ "_databaseVersionForEmbeddingType:"
+ "_databaseVersionForVisualEmbedding"
+ "_embeddingIndices"
+ "_embeddingSimilarityThresholdForVersion:similarityLevel:"
+ "_embeddingSourceType"
+ "_embeddingSourceTypes"
+ "_forceXPC"
+ "_historicalFolderNames"
+ "_isEmbeddingSourceTypeRequested:inOptions:"
+ "_madEmbeddingsFromGroupedVSKAssets:"
+ "_madEmbeddingsWithThumbnailIdsFromMADBForLibrary:pairedVSKAssets:"
+ "_openVSKClientsWithTargetVersion:embeddingType:"
+ "_patchEmbedding"
+ "_purgeHistoricalDataForPhotoLibrary:"
+ "_queryEmbedding"
+ "_querySafetyResult"
+ "_queryText"
+ "_safetyState"
+ "_searchMode"
+ "_semanticSafetyScore"
+ "_sharedDatabaseWithPhotoLibrary:embeddingType:"
+ "_similarity"
+ "_similarityLevel"
+ "_sortedResults"
+ "_vectorDataTypeForEmbeddingType:"
+ "_vectorDatabaseReadOnlyConfig"
+ "_vectorDatabaseReadWriteConfigWithTargetVersion:"
+ "_vectorDimensionForEmbeddingType:"
+ "checkSafety"
+ "d32@0:8Q16Q24"
+ "databaseDirectoryURLForPhotoLibrary:embeddingType:"
+ "databaseWithDirectoryURL:readOnly:databaseVersion:embeddingType:"
+ "decodeFloatForKey:"
+ "decodeInt32ForKey:"
+ "embeddingIndex"
+ "embeddingIndices"
+ "embeddingResults"
+ "embeddingSourceType"
+ "embeddingSourceTypes"
+ "encodeFloat:forKey:"
+ "encodeInt32:forKey:"
+ "forceXPC"
+ "getStringValue"
+ "i32@0:8@16Q24"
+ "initWithAssetUUID:similarity:metric:embeddingSourceType:similarityLevel:embeddingIndices:thumbnailIdentifiers:"
+ "initWithDirectoryURL:readyOnly:databaseVersion:embeddingType:"
+ "initWithQueryText:querySafetyResult:queryEmbedding:sortedResults:error:"
+ "initWithSafetyState:semanticSafetyScore:"
+ "initWithStringIdentifier:vectors:perVectorAttribute:payload:"
+ "initWithText:"
+ "isSafe"
+ "mad_embeddingIndexArray"
+ "mad_embeddingIndexAttribute"
+ "mad_embeddingIndexAttributeName"
+ "mad_isEmbeddingIndexAttribute"
+ "mad_isThumbnailIdentifierAttribute"
+ "mad_thumbnailIdentifierArray"
+ "mad_thumbnailIdentifierAttribute"
+ "mad_thumbnailIdentifierAttributeName"
+ "mubb_md8"
+ "patchEmbedding"
+ "patch_embed"
+ "perVectorAttribute"
+ "performRequests:textInputs:completionHandler:"
+ "preferredImageEmbeddings:versions:forAssetUUID:fromImageEmbeddingResults:error:"
+ "preferredVideoEmbeddings:versions:embeddingIndices:thumbnailIdentifiers:forAssetUUID:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:"
+ "prewarmSearchWithConcurrencyLimit:photoLibraryURL:options:error:"
+ "queryEmbedding"
+ "querySafetyResult"
+ "queryText"
+ "safetyScore"
+ "safetyState"
+ "searchByBatch:stringIdentifiers:attributeFilters:selectAttributes:limit:fullScan:includePayload:numberOfProbes:batchSize:numConcurrentReaders:error:"
+ "searchMode"
+ "searchWithQueryTexts:photoLibraryURL:options:error:"
+ "semanticSafetyScore"
+ "setCheckSafety:"
+ "setComputeSafety:"
+ "setComputeThreshold:"
+ "setEmbeddingSourceTypes:"
+ "setForceXPC:"
+ "setSearchMode:"
+ "setSimilarity:"
+ "setSimilarityLevel:"
+ "sharedDatabaseWithPhotoLibrary:embeddingType:"
+ "similarity"
+ "similarityLevel"
+ "sortedResults"
+ "stringIdentifiedAssetsWithIdentifiers:attributeFilters:pagination:includeVectors:selectAttributes:error:"
+ "text_safety_md8_v1.espresso.net"
+ "text_threshold_md8_v1.espresso.net"
+ "thumbnailIdentifier"
+ "v20@?0i8@\"NSError\"12"
+ "v48@0:8Q16@24@32^@40"
- "%@ Failed to create vskConfig - %@"
- "%@ No valid summarized video embeddings (total %d, indices %@)"
- "%@[%@] Invalid embedding count"
- "@40@0:8@16@24q32"
- "@48@0:8@16^Q24@32^@40"
- "@64@0:8@16^Q24@32@40@48^@56"
- "Safety only supported for MD5-MD7"
- "SearchUnifiedEmbeddingMD7"
- "Threshold calibration only supported for MD3-MD7"
- "VCPImageEmbeddingRequest only supports revision 5 (MD5), revision 7 (MD6) and revision 8 (MD7)"
- "[MADEmbeddingStoreService] Performing XPC embedding fetching for %u assets"
- "[MADEmbeddingStoreService] XPC search with %llu embeddings"
- "[MADVectorDatabaseManager] Embedding generation disabled, skip vector database creation"
- "[MADVectorDatabaseManager] Failed to open database for %@"
- "[MADVectorDatabaseManager] Releasing shared database for %@"
- "[VSKDB] Failed to initialize %@ database - %@"
- "[VSKDB] Failed to retrieve path for Photo Library %@"
- "[VSKDB] Invalid media analysis directory %@"
- "[VSKDB] Target version: %@"
- "[VSKDB] Unable to initialize vector database with abbreviated initializer: %@"
- "_openVSKClientWithError:"
- "_purgeHistoricalData"
- "_vectorDatabaseReadOnlyConfigWithError:"
- "_vectorDatabaseReadWriteConfigWithError:"
- "_vectorDatabaseVersion"
- "assetUUID: %@, "
- "databaseDirectoryURLForPhotoLibrary:"
- "databaseWithPhotoLibrary:readyOnly:"
- "decodeIntForKey:"
- "distance: %@, "
- "encodeInt:forKey:"
- "historicalFolderNames"
- "initWithAssetUUID:distance:metric:"
- "initWithPhotoLibrary:readyOnly:"
- "metric: %d>"
- "preferredImageEmbeddingsForAssetUUID:version:fromImageEmbeddingResults:error:"
- "preferredVideoEmbeddingsForAssetUUID:version:fromVideoEmbeddingResults:audioFusedVideoEmbeddingResults:summarizedVideoEmbeddingResults:error:"
- "sharedDatabaseWithPhotoLibrary:"

```
