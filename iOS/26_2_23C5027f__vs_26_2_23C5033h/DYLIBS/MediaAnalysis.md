## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

 380.1.1.0.0
-  __TEXT.__text: 0x460740
+  __TEXT.__text: 0x4605ac
   __TEXT.__auth_stubs: 0x3f80
   __TEXT.__delay_stubs: 0x84
   __TEXT.__delay_helper: 0xa4

   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x113a8
+  __TEXT.__unwind_info: 0x11398
   __TEXT.__eh_frame: 0x940
   __TEXT.__objc_classname: 0x436d
   __TEXT.__objc_methname: 0x3cd9c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1BDCEF9D-AC31-3D23-AF93-72F422D736DE
-  Functions: 16757
+  UUID: 3BA74774-5317-31EB-B881-C9622A93BCDD
+  Functions: 16753
   Symbols:   56789
   CStrings:  22010
 
Symbols:
+ ___101-[VCPMediaAnalyzer findTimeRangesFor:inURLAsset:withOptions:andProgressHandler:andCompletionHandler:]_block_invoke.1041
+ ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.681
+ ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.682
+ ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.938
+ ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.939
+ ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.565
+ ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.567
+ ___48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.578
+ ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.908
+ ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.909
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.707
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.707.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.715
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.715.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.719
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.719.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.727
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.727.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.727.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.731
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.731.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.731.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.734
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.734.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.734.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.735
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.735.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.735.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.737
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.737.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.737.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.748
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.748.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.751
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.751.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.751.cold.2
+ ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.570
+ ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.572
+ ___67-[VCPMediaAnalyzer _getDatabaseSandboxExtensionForPhotoLibraryURL:]_block_invoke.922
+ ___69-[VCPMediaAnalyzer analyzeOndemand:pairedURL:forAnalysisTypes:error:]_block_invoke.947
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.758
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.758.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.758.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.3
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.4
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.5
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.6
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.7
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.8
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.765.cold.9
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.778
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.778.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.778.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.783
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.783.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.783.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.788
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.788.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.788.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.793
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.793.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.793.cold.2
+ ___84-[VCPMediaAnalyzer _getSandboxExtensionForMediaAnalysisDatabaseWithPhotoLibraryURL:]_block_invoke.911
+ ___Block_byref_object_copy_.705
+ ___Block_byref_object_dispose_.706
+ ___block_literal_global.1004
+ ___block_literal_global.1015
+ ___block_literal_global.1032
+ ___block_literal_global.1046
+ ___block_literal_global.508
+ ___block_literal_global.515
+ ___block_literal_global.563
+ ___block_literal_global.633
+ ___block_literal_global.641
+ ___block_literal_global.646
+ ___block_literal_global.649
+ ___block_literal_global.651
+ ___block_literal_global.654
+ ___block_literal_global.656
+ ___block_literal_global.659
+ ___block_literal_global.664
+ ___block_literal_global.675
+ ___block_literal_global.709
+ ___block_literal_global.742
+ ___block_literal_global.774
+ ___block_literal_global.787
+ ___block_literal_global.907
+ ___block_literal_global.946
+ ___block_literal_global.949
+ ___block_literal_global.969
+ ___block_literal_global.982
+ ___block_literal_global.987
+ ___block_literal_global.999
- ___101-[VCPMediaAnalyzer findTimeRangesFor:inURLAsset:withOptions:andProgressHandler:andCompletionHandler:]_block_invoke.1032
- ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.672
- ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.673
- ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.929
- ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.930
- ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.556
- ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.558
- ___48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.569
- ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.899
- ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.900
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.698
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.698.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.701
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.701.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.706
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.706.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.722
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.722.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.722.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.725
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.725.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.725.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.739
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.739.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742.cold.2
- ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.561
- ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.563
- ___67-[VCPMediaAnalyzer _getDatabaseSandboxExtensionForPhotoLibraryURL:]_block_invoke.913
- ___69-[VCPMediaAnalyzer analyzeOndemand:pairedURL:forAnalysisTypes:error:]_block_invoke.938
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.3
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.4
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.5
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.6
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.7
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.8
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.9
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784.cold.2
- ___84-[VCPMediaAnalyzer _getSandboxExtensionForMediaAnalysisDatabaseWithPhotoLibraryURL:]_block_invoke.902
- ___Block_byref_object_copy_.696
- ___Block_byref_object_dispose_.697
- ___block_literal_global.1006
- ___block_literal_global.1023
- ___block_literal_global.499
- ___block_literal_global.506
- ___block_literal_global.554
- ___block_literal_global.629
- ___block_literal_global.632
- ___block_literal_global.637
- ___block_literal_global.640
- ___block_literal_global.642
- ___block_literal_global.647
- ___block_literal_global.650
- ___block_literal_global.655
- ___block_literal_global.666
- ___block_literal_global.674
- ___block_literal_global.700
- ___block_literal_global.733
- ___block_literal_global.765
- ___block_literal_global.778
- ___block_literal_global.898
- ___block_literal_global.937
- ___block_literal_global.940
- ___block_literal_global.960
- ___block_literal_global.973
- ___block_literal_global.978
- ___block_literal_global.990
- ___block_literal_global.995
Functions:
~ -[VCPFaceShapeModel updateBoundaryLandmarkCoordinates:pts2D:lm2D:lm3dPos:] : 584 -> 604
~ -[VCPProtoAssetAnalysis dictionaryRepresentation] : 21112 -> 21132
~ -[VCPProtoAssetAnalysis writeTo:] : 13904 -> 13924
~ -[VCPProtoAssetAnalysis copyWithZone:] : 15192 -> 15212
~ -[VCPProtoAssetAnalysis mergeFrom:] : 13564 -> 13584
~ -[VCPVideoFaceMeshAnalyzer rotateLandmarks:width:height:landmarks:numLandmarks:] : 412 -> 428
~ __ZNK13sentencepiece14ModelInterface18LookupCommonPrefixENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEEPNS1_6vectorIiNS1_9allocatorIiEEEE : 952 -> 956
~ __ZN13sentencepiece9BuildTrieERN5Darts15DoubleArrayImplIvvivEERKNSt3__13mapINS4_17basic_string_viewIcNS4_11char_traitsIcEEEEiNS4_4lessIS9_EENS4_9allocatorINS4_4pairIKS9_iEEEEEEPi : 1224 -> 1232
~ __ZNSt3__15dequeIZNK5Darts15DoubleArrayImplIvvivE16predictiveSearchINS3_16result_pair_typeEEEmPKcPT_mmiE5StateNS_9allocatorISA_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPZNK5Darts15DoubleArrayImplIvvivE16predictiveSearchINS3_16result_pair_typeEEEmPKcPT_mmiE5StateNS_9allocatorISB_EEE13emplace_frontIJSB_EEEvDpOT_ : 268 -> 272
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEhEENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSN_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 640 -> 644
~ __ZNSt3__16vectorINS_4pairINS0_INS1_INS_17basic_string_viewIcNS_11char_traitsIcEEEEiEENS_9allocatorIS6_EEEEfEENS7_ISA_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairINS_17basic_string_viewIcNS_11char_traitsIcEEEEiEENS_9allocatorIS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN5Darts15DoubleArrayImplIvvivE16result_pair_typeENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJNS_17basic_string_viewIcS3_EEEEEPS6_DpOT_ : 408 -> 404
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em : 68 -> 72
~ __ZNKSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEhEENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE4findIS7_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_ : 252 -> 256
- __ZNSt3__16vectorImNS_9allocatorImEEE6resizeEm
~ __ZN13sentencepiece10normalizer13PrefixMatcherC2ERKNSt3__13setINS2_17basic_string_viewIcNS2_11char_traitsIcEEEENS2_4lessIS7_EENS2_9allocatorIS7_EEEE : 716 -> 728
- __ZNSt3__16vectorImNS_9allocatorImEEE8__appendEm
~ __ZN13sentencepiece22SentencePieceProcessor4LoadENSt3__110unique_ptrINS_10ModelProtoENS1_14default_deleteIS3_EEEE : 2576 -> 2584
~ __ZNK13sentencepiece22SentencePieceProcessor11NBestEncodeENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEEiPNS1_6vectorINS6_IiNS1_9allocatorIiEEEENS7_IS9_EEEE : 1108 -> 1112
~ __ZNK13sentencepiece22SentencePieceProcessor20SampleEncodeAndScoreENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEEifbbPNS1_6vectorINS1_4pairINS6_IiNS1_9allocatorIiEEEEfEENS8_ISB_EEEE : 1220 -> 1224
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_17basic_string_viewIcNS_11char_traitsIcEEEENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairINS_17basic_string_viewIcNS_11char_traitsIcEEEES5_EENS_9allocatorIS6_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEENS4_IS8_EEE24__emplace_back_slow_pathIJRS8_EEEPS8_DpOT_ : 316 -> 312
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRS3_EEEPS3_DpOT_ : 304 -> 300
~ __ZNSt3__16vectorINS_4pairINS0_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS5_IS7_EEEEfEENS5_ISA_EEE24__emplace_back_slow_pathIJRS9_fEEEPSA_DpOT_ : 296 -> 292
~ __ZNSt3__16vectorINS_4pairINS0_IiNS_9allocatorIiEEEEfEENS2_IS5_EEE24__emplace_back_slow_pathIJRS4_fEEEPS5_DpOT_ : 284 -> 280
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE13shrink_to_fitEv : 212 -> 208
- __ZNSt3__16vectorIPN13sentencepiece7unigram7Lattice4NodeENS_9allocatorIS5_EEE9push_backB8ne200100ERKS5_
~ __ZN13sentencepiece7unigram7Lattice6SampleEf : 888 -> 892
~ __ZNK13sentencepiece7unigram5Model15EncodeOptimizedENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 1376 -> 1388
~ __ZNK13sentencepiece7unigram5Model11NBestEncodeENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEi : 1192 -> 1196
~ __ZNK13sentencepiece7unigram5Model20SampleEncodeAndScoreENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEfibb : 3164 -> 3184
~ __ZNSt3__16vectorIPN13sentencepiece7unigram7Lattice4NodeENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairINS0_IPN13sentencepiece7unigram7Lattice4NodeENS_9allocatorIS6_EEEEfEENS7_ISA_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairINS0_INS1_INS_17basic_string_viewIcNS_11char_traitsIcEEEEiEENS_9allocatorIS6_EEEEfEENS7_ISA_EEE24__emplace_back_slow_pathIJRS9_RKfEEEPSA_DpOT_ : 296 -> 292
~ __ZNSt3__16vectorINS_4pairINS0_INS1_INS_17basic_string_viewIcNS_11char_traitsIcEEEEiEENS_9allocatorIS6_EEEEfEENS7_ISA_EEE24__emplace_back_slow_pathIJRS9_dEEEPSA_DpOT_ : 300 -> 296
- __ZNSt3__16vectorINS0_IPN13sentencepiece7unigram7Lattice4NodeENS_9allocatorIS5_EEEENS6_IS8_EEE11__vallocateB8ne200100Em
~ __ZNSt3__16vectorINS_4pairINS0_INS1_INS_17basic_string_viewIcNS_11char_traitsIcEEEEiEENS_9allocatorIS6_EEEEfEENS7_ISA_EEE24__emplace_back_slow_pathIJRS9_fEEEPSA_DpOT_ : 296 -> 292
~ __ZNK13sentencepiece9character5Model6EncodeENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 512 -> 520
~ __ZNK13sentencepiece3bpe5Model12SampleEncodeENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEf : 1896 -> 1904
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEENS_4pairIS5_S5_EEEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS5_JRKNS_21piecewise_construct_tENS_5tupleIJRKS5_EEENSO_IJEEEEEENS6_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 624 -> 628
~ __ZNSt3__110__function6__funcIZNK13sentencepiece3bpe5Model12SampleEncodeENS_17basic_string_viewIcNS_11char_traitsIcEEEEfE3$_0NS_9allocatorIS9_EEFvS8_PNS_6vectorINS_4pairIS8_iEENSA_ISE_EEEEEEclEOS8_OSH_ : 440 -> 444
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEENS_4pairIS5_S5_EEEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE4findIS5_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_ : 276 -> 280
~ __ZNKSt3__114default_deleteIN13sentencepiece4util6Status3RepEEclB8ne200100EPS4_ : 108 -> 96
~ __ZN6google8protobuf8internal12ExtensionSetD2Ev.cold.1 : 88 -> 96
~ __ZN6google8protobuf8internal13OnShutdownRunEPFvPKvES3_ : 268 -> 272

```
