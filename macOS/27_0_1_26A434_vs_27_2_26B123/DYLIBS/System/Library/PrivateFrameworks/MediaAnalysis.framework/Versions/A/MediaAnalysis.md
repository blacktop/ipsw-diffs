## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis`

```diff

-435.79.5.4.0
-  __TEXT.__text: 0x476364
-  __TEXT.__objc_methlist: 0x22518
-  __TEXT.__const: 0x16488
-  __TEXT.__gcc_except_tab: 0x60a14
-  __TEXT.__cstring: 0x1fca7
-  __TEXT.__oslogstring: 0x2fc9b
+460.14.5.2.0
+  __TEXT.__text: 0x477dd8
+  __TEXT.__delay_helper: 0x1e0
+  __TEXT.__objc_methlist: 0x22608
+  __TEXT.__const: 0x164b8
+  __TEXT.__gcc_except_tab: 0x60bdc
+  __TEXT.__cstring: 0x20366
+  __TEXT.__oslogstring: 0x2fe3b
   __TEXT.__dlopen_cstrs: 0x3c6
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x960

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift_as_cont: 0xc4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12b38
+  __TEXT.__unwind_info: 0x12b88
   __TEXT.__eh_frame: 0x1828
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3fb8
-  __DATA_CONST.__objc_classlist: 0x1598
+  __DATA_CONST.__const: 0x4060
+  __DATA_CONST.__objc_classlist: 0x15a0
   __DATA_CONST.__objc_catlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xeae0
+  __DATA_CONST.__objc_selrefs: 0xeb60
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xf80
-  __DATA_CONST.__objc_arraydata: 0xe60
-  __DATA_CONST.__got: 0x22b8
-  __AUTH_CONST.__const: 0x9ad8
-  __AUTH_CONST.__cfstring: 0x1c680
-  __AUTH_CONST.__objc_const: 0x408d8
+  __DATA_CONST.__objc_superrefs: 0xf88
+  __DATA_CONST.__objc_arraydata: 0xe88
+  __DATA_CONST.__got: 0x22c0
+  __AUTH_CONST.__const: 0x9a68
+  __AUTH_CONST.__cfstring: 0x1cb20
+  __AUTH_CONST.__objc_const: 0x40ae8
   __AUTH_CONST.__weak_auth_got: 0x70
   __AUTH_CONST.__objc_floatobj: 0x300
-  __AUTH_CONST.__objc_arrayobj: 0xb88
+  __AUTH_CONST.__objc_arrayobj: 0xbb8
   __AUTH_CONST.__objc_doubleobj: 0x240
-  __AUTH_CONST.__objc_intobj: 0x3690
+  __AUTH_CONST.__objc_intobj: 0x36a8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x2270
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x390
-  __AUTH.__data: 0x118
+  __AUTH.__objc_data: 0xf0
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0x10
-  __DATA.__objc_ivar: 0x34b4
-  __DATA.__data: 0x1e18
-  __DATA.__bss: 0x2ea9
+  __DATA.__objc_ivar: 0x34d4
+  __DATA.__data: 0xe9c
+  __DATA.__bss: 0x2e99
   __DATA.__common: 0x3c1
-  __DATA_DIRTY.__objc_data: 0xd9c0
-  __DATA_DIRTY.__data: 0x288
-  __DATA_DIRTY.__bss: 0x728
+  __DATA_DIRTY.__objc_data: 0xdcb0
+  __DATA_DIRTY.__data: 0x1320
+  __DATA_DIRTY.__bss: 0x748
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16247
-  Symbols:   34011
-  CStrings:  8109
+  Functions: 16267
+  Symbols:   34109
+  CStrings:  8160
 
Symbols:
+ +[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]
+ -[MADHKSVClip generativeMetrics]
+ -[MADHKSVClip setGenerativeMetrics:]
+ -[MADHKSVGenerativeMetrics copyWithZone:]
+ -[MADHKSVGenerativeMetrics pccProcessingDurationMilliseconds]
+ -[MADHKSVGenerativeMetrics pccVideoCaptionDurationMilliseconds]
+ -[MADHKSVGenerativeMetrics pccVideoDecodeDurationMilliseconds]
+ -[MADHKSVGenerativeMetrics pccVideoEmbeddingDurationMilliseconds]
+ -[MADHKSVGenerativeMetrics pccVideoGatingDurationMilliseconds]
+ -[MADHKSVGenerativeMetrics setPccProcessingDurationMilliseconds:]
+ -[MADHKSVGenerativeMetrics setPccVideoCaptionDurationMilliseconds:]
+ -[MADHKSVGenerativeMetrics setPccVideoDecodeDurationMilliseconds:]
+ -[MADHKSVGenerativeMetrics setPccVideoEmbeddingDurationMilliseconds:]
+ -[MADHKSVGenerativeMetrics setPccVideoGatingDurationMilliseconds:]
+ -[MADServicePhotosVideoAsset isPhotosAsset]
+ -[MADServiceVideoAsset isPhotosAsset]
+ -[MADServiceVideoSafetyProcessingTask storeSafetyClassificationResults]
+ -[MADSharedTextTokenizer tokenIDsForText:offsets:]
+ -[MADTextTokenizationTask processInput:resource:computeOffsets:tokenIDs:tokenOffsets:error:]
+ -[MADTextureStyleMetaAnalyzer .cxx_destruct]
+ -[MADTextureStyleMetaAnalyzer initWithRequestAnalyses:formatDescription:]
+ -[MADTextureStyleMetaAnalyzer privateResults]
+ -[MADTextureStyleMetaAnalyzer processMetadataGroup:flags:]
+ -[PHAsset(MediaAnalysisTUProcessing) mad_hasContentClassificationPassport]
+ -[VCPFullAnalysisURLProcessingTask dealloc]
+ -[VCPMovieAnalyzer initWithPHAsset:withPausedAnalysis:forAnalysisTypes:downloadedResourceURL:]
+ OBJC_IVAR_$_MADHKSVClip._generativeMetrics
+ OBJC_IVAR_$_MADHKSVGenerativeMetrics._pccProcessingDurationMilliseconds
+ OBJC_IVAR_$_MADHKSVGenerativeMetrics._pccVideoCaptionDurationMilliseconds
+ OBJC_IVAR_$_MADHKSVGenerativeMetrics._pccVideoDecodeDurationMilliseconds
+ OBJC_IVAR_$_MADHKSVGenerativeMetrics._pccVideoEmbeddingDurationMilliseconds
+ OBJC_IVAR_$_MADHKSVGenerativeMetrics._pccVideoGatingDurationMilliseconds
+ OBJC_IVAR_$_MADTextureStyleMetaAnalyzer._results
+ OBJC_IVAR_$_VCPFullAnalysisURLProcessingTask._started
+ _MediaAnalysisMetaTSInfoResultsKey
+ _MediaAnalysisMetaTSResultsKey
+ _OBJC_CLASS_$_MADTextureStyleMetaAnalyzer
+ _OBJC_CLASS_$_PNAssetCurationUtilities$loadHelper_x8
+ _OBJC_CLASS_$_PNPersonClusterManager$loadHelper_x8
+ _OBJC_CLASS_$_PNPersonPromoter$loadHelper_x25
+ _OBJC_CLASS_$_PNPersonPromoter$loadHelper_x8
+ _OBJC_CLASS_$_PNPersonPromoter$loadHelper_x8$for$_MADPersonPromoterHasProcessedForLibrary+4
+ _OBJC_METACLASS_$_MADTextureStyleMetaAnalyzer
+ _PNPersonPromoterVersion$loadHelper_x8
+ _VCPAnalyticsField17246HKSVProcessingConsecutiveIndex
+ _VCPAnalyticsField17246HKSVProcessingCountPreviousRequestsPendingWhenAdmitted
+ _VCPAnalyticsField17246HKSVProcessingDidGlobalLastClipIDMismatchPredecessor
+ _VCPAnalyticsField17246HKSVProcessingDidLapseConsecutiveWindow
+ _VCPAnalyticsField17246HKSVProcessingFragmentTotalDurationMilliseconds
+ _VCPAnalyticsField17246HKSVProcessingPendingPredecessorElapsedMilliseconds
+ _VCPAnalyticsField17246HKSVProcessingPreviousConsecutiveStatus
+ _VCPAnalyticsField17246HKSVProcessingPreviousOSStatus
+ _VCPAnalyticsField17246HKSVProcessingRetryCount
+ _VCPAnalyticsField17246HKSVProcessingRetryDelayBucket
+ _VCPAnalyticsFieldNumberOfAssetsThumbnailSufficient
+ _VCPAnalyticsFieldNumberOfAssetsThumbnailTooSmall
+ _VCPAnalyticsFieldTimeFetchingFullInSeconds
+ _VCPAnalyticsFieldTimeFetchingGatingInSeconds
+ _VCPAnalyticsFieldTimePreparingFullInSeconds
+ _VCPAnalyticsFieldTimePreparingGatingInSeconds
+ _VCPAnalyticsFieldTimePublishingFullInSeconds
+ _VCPAnalyticsFieldTimePublishingGatingInSeconds
+ __OBJC_$_INSTANCE_METHODS_MADTextureStyleMetaAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_MADTextureStyleMetaAnalyzer
+ __OBJC_CLASS_RO_$_MADTextureStyleMetaAnalyzer
+ __OBJC_METACLASS_RO_$_MADTextureStyleMetaAnalyzer
+ __ZL17shapeElementCountP7NSArrayIP8NSNumberE
+ __ZN5Darts15DoubleArrayImplIvvivE10copy_arrayEPKvm
+ __ZNK5Darts15DoubleArrayImplIvvivE8validateEi
+ __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE7__cloneEPNS0_6__baseISH_EE
+ __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE7__cloneEv
+ __ZNKSt3__18functionIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS4_iEENS_9allocatorIS7_EEEEiEEclES4_SB_i
+ __ZNSt3__110__function12__value_funcIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEiEE4swapB9nqe220106ERSE_
+ __ZNSt3__110__function12__value_funcIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEiEED2B9nqe220106Ev
+ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEE7destroyEv
+ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEED0Ev
+ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEED1Ev
+ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEEclEOS8_OSG_Oi
+ __ZTINSt3__110__function6__baseIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEiEEE
+ __ZTINSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEEE
+ __ZTSNSt3__110__function6__baseIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEiEEE
+ __ZTSNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEEE
+ __ZTVNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEiEEE
+ __ZZ58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]E21isInitialAnalysisPass
+ __ZZ58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]E4once
+ ___50-[MADSharedTextTokenizer tokenIDsForText:offsets:]_block_invoke
+ ___58+[PHPhotoLibrary(MediaAnalysis) mad_isInitialAnalysisPass]_block_invoke
+ _dlopenHelper$PhotosIntelligence
+ _dlopenHelperFlag$PhotosIntelligence
+ _objc_msgSend$computeOffsets
+ _objc_msgSend$existingObjectWithID:error:
+ _objc_msgSend$finishDate
+ _objc_msgSend$generativeMetrics
+ _objc_msgSend$getTokenIDsAndOffsetMappingForText:
+ _objc_msgSend$goreFrameCountThreshold
+ _objc_msgSend$initWithPHAsset:withPausedAnalysis:forAnalysisTypes:downloadedResourceURL:
+ _objc_msgSend$initWithTokenIDs:tokenOffsets:error:
+ _objc_msgSend$isPhotosAsset
+ _objc_msgSend$mad_isInitialAnalysisPass
+ _objc_msgSend$offsetMapping
+ _objc_msgSend$pccProcessingDurationMilliseconds
+ _objc_msgSend$pccVideoCaptionDurationMilliseconds
+ _objc_msgSend$pccVideoDecodeDurationMilliseconds
+ _objc_msgSend$pccVideoEmbeddingDurationMilliseconds
+ _objc_msgSend$pccVideoGatingDurationMilliseconds
+ _objc_msgSend$processInput:resource:computeOffsets:tokenIDs:tokenOffsets:error:
+ _objc_msgSend$requestFragmentCount
+ _objc_msgSend$requestFragmentSize
+ _objc_msgSend$requestOverallPayloadSize
+ _objc_msgSend$resultCaptionCount
+ _objc_msgSend$resultEmbeddingCount
+ _objc_msgSend$resultOverallPayloadSize
+ _objc_msgSend$setFinishDate:
+ _objc_msgSend$setGenerativeMetrics:
+ _objc_msgSend$setPccProcessingDurationMilliseconds:
+ _objc_msgSend$setPccVideoCaptionDurationMilliseconds:
+ _objc_msgSend$setPccVideoDecodeDurationMilliseconds:
+ _objc_msgSend$setPccVideoEmbeddingDurationMilliseconds:
+ _objc_msgSend$setPccVideoGatingDurationMilliseconds:
+ _objc_msgSend$setRequestFragmentCount:
+ _objc_msgSend$setRequestFragmentSize:
+ _objc_msgSend$setRequestOverallPayloadSize:
+ _objc_msgSend$setResultCaptionCount:
+ _objc_msgSend$setResultEmbeddingCount:
+ _objc_msgSend$setResultOverallPayloadSize:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$startDate
+ _objc_msgSend$storeSafetyClassificationResults
+ _objc_msgSend$tokenIDsForText:offsets:
+ _objc_msgSend$violentFrameCountThreshold
- +[PHAssetResourceManager(MediaAnalysis) vcp_inMemoryDownload:withTaskID:toData:cancel:]
- +[VCPHomeKitAnalysisSession requestHistogramCalculationForPixelBuffer:normalizedBoundingBox:error:]
- +[VCPHomeKitAnalysisSession sessionWithProperties:andResultsHandler:]
- -[MADServiceVideoSafetyProcessingTask storeSafetyClassificationResultsForSharedAsset]
- -[MADTextTokenizationTask processInput:resource:tokenIDs:error:]
- -[VCPHomeKitAnalysisSession processWithVideoAnalyzerFragmentResult:completionHandler:]
- -[VCPHomeKitAnalysisSession processWithVideoAnalyzerFragmentResults:embeddingOnly:previousAnalysis:completionHandler:]
- -[VCPMADResourceManager reserveBudgetNormalized:]
- __87+[PHAssetResourceManager(MediaAnalysis) vcp_inMemoryDownload:withTaskID:toData:cancel:]_block_invoke
- __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE11target_typeEv
- __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE7__cloneEv
- __ZNKSt3__18functionIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS4_iEENS_9allocatorIS7_EEEEEEclES4_SB_
- __ZNSt3__110__function12__value_funcIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEEE4swapB9nqe220106ERSE_
- __ZNSt3__110__function12__value_funcIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEEED2B9nqe220106Ev
- __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEE7destroyEv
- __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEED0Ev
- __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEED1Ev
- __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEEclEOS8_OSG_
- __ZTINSt3__110__function6__baseIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEEEE
- __ZTINSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEEE
- __ZTSNSt3__110__function6__baseIFvNS_17basic_string_viewIcNS_11char_traitsIcEEEEPNS_6vectorINS_4pairIS5_iEENS_9allocatorIS8_EEEEEEE
- __ZTSNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEEE
- __ZTVNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0FvS8_PNS_6vectorINS_4pairIS8_iEENS_9allocatorISC_EEEEEEE
- ___87+[PHAssetResourceManager(MediaAnalysis) vcp_inMemoryDownload:withTaskID:toData:cancel:]_block_invoke
- ___block_descriptor_40_e8_32s_e16_v16?0"NSData"8l
- ___block_descriptor_40_e8_32s_e8_v16?0d8l
- ___block_descriptor_64_e8_32s40s_e17_v16?0"NSError"8l
- _objc_msgSend$configureProcessTimeIntervalFrom:
- _objc_msgSend$initWithTokenIDs:error:
- _objc_msgSend$processInput:resource:tokenIDs:error:
- _objc_msgSend$reserveBudget:
- _objc_msgSend$storeSafetyClassificationResultsForSharedAsset
CStrings:
+ "!pieces_blob.empty()"
+ "(piece_offsets_[i]) < (pieces_blob.size())"
+ "(pieces_blob.back()) == ('\\0')"
+ "(unk_id_) < (GetPieceSize())"
+ "(unk_id_) >= (0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/src/mmap_model_proto.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1161: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1163: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1177: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1182: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1394: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1730: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1732: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1747: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:798: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:914: exception: failed to build rank index: std::bad_alloc"
+ "/System/Library/PrivateFrameworks/PhotosIntelligence.framework/Versions/A/PhotosIntelligence"
+ "CSUTokenizer_tokenIDsAndOffsetMappingForText"
+ "ConsecutiveIndex"
+ "CountPreviousRequestsPendingWhenAdmitted"
+ "DidGlobalLastClipIDMismatchPredecessor"
+ "DidLapseConsecutiveWindow"
+ "Failed to create the text encoder"
+ "Failed to generate MADImageEmbeddingResult: expected shape %@ (%lu fp16 elements), got %lu elements"
+ "FragmentTotalDurationMilliseconds"
+ "MetaTSInfoResults"
+ "MetaTSResults"
+ "NumberOfAssetsThumbnailSufficient"
+ "NumberOfAssetsThumbnailTooSmall"
+ "Offset output not supported for multi-segment input"
+ "PCC processing duration"
+ "PCC video caption duration"
+ "PCC video decode duration"
+ "PCC video embedding duration"
+ "PCC video gating duration"
+ "PendingPredecessorElapsedMilliseconds"
+ "PreviousConsecutiveStatus"
+ "PreviousOSStatus"
+ "RetryCount"
+ "RetryDelayBucket"
+ "The trie of the pieces is invalid."
+ "The trie of the reserved ids is invalid."
+ "TimeFetchingFullInSeconds"
+ "TimeFetchingGatingInSeconds"
+ "TimePreparingFullInSeconds"
+ "TimePreparingGatingInSeconds"
+ "TimePublishingFullInSeconds"
+ "TimePublishingGatingInSeconds"
+ "Tokenization failed to produce offsets"
+ "Tokenization produced unexpected offset count"
+ "VCPMADImageEmbeddingTask expected shape %@ (%lu fp16 elements) but got %lu elements"
+ "[%@] Analysis was never executed"
+ "[%@] Configuring typeNFrameCountThreshold: %u, typeGFrameCountThreshold: %u,            typeVFrameCountThreshold: %u"
+ "[%@] Failed to obtain analysis result for Photos asset."
+ "[%@] Invalid configuration, goreFrameCountThreshold must be > 0"
+ "[%@] Invalid configuration, violentFrameCountThreshold must be > 0"
+ "[%@][MOCForPath] Failed to create persistent store coordinator for path %@"
+ "[MADCD|Asset] Failed to find asset with object id that matches %@"
+ "[MediaAnalysis] [MADTextureStyleMetaAnalyzer] Read %lu texture style info samples"
+ "[MediaAnalysis] [MADTextureStyleMetaAnalyzer] Texture style item carries no value"
+ "generativeMetrics"
+ "mdta/com.apple.quicktime.texturestyle-info"
+ "pccProcessingDurationMilliseconds"
+ "pccVideoCaptionDurationMilliseconds"
+ "pccVideoDecodeDurationMilliseconds"
+ "pccVideoEmbeddingDurationMilliseconds"
+ "pccVideoGatingDurationMilliseconds"
+ "pieces_.validate(GetPieceSize())"
+ "precompiled_charsmap is invalid."
+ "reserved_id_map_.validate(GetPieceSize())"
- "(num_nodes) < (trie_results.size())"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
- "Attempt to download resource: %@"
- "Cancelling download (ID:%d)"
- "Download resource timed-out (ID:%d)"
- "Failed to generate MADImageEmbeddingResult"
- "[%@] Configuring sensitiveFrameCountThreshold: %u"
- "[%@] Download progress: %.2f"
- "[%@] Failed to obtain analysis result for shared Photos asset."
- "[HomeKitAnalysis] Histogram calculation is not supported on this platform"
```
