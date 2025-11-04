## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-619.10.0.0.0
-  __TEXT.__text: 0x486ac8
+619.12.0.0.0
+  __TEXT.__text: 0x486ef0
   __TEXT.__auth_stubs: 0x4130
-  __TEXT.__objc_methlist: 0x38c64
+  __TEXT.__objc_methlist: 0x38c74
   __TEXT.__const: 0x427a
-  __TEXT.__cstring: 0x5a3d1
+  __TEXT.__cstring: 0x5a321
   __TEXT.__oslogstring: 0x3ad99
   __TEXT.__gcc_except_tab: 0x10064
   __TEXT.__dlopen_cstrs: 0x1d2

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe428
+  __TEXT.__unwind_info: 0xe430
   __TEXT.__eh_frame: 0x2a34
   __TEXT.__objc_classname: 0x8c15
-  __TEXT.__objc_methname: 0xae2a2
-  __TEXT.__objc_methtype: 0x18004
-  __TEXT.__objc_stubs: 0x4cf40
+  __TEXT.__objc_methname: 0xae2dc
+  __TEXT.__objc_methtype: 0x180ae
+  __TEXT.__objc_stubs: 0x4cf80
   __DATA_CONST.__got: 0x39c0
-  __DATA_CONST.__const: 0xbf48
+  __DATA_CONST.__const: 0xbf98
   __DATA_CONST.__objc_classlist: 0x1f88
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1be08
+  __DATA_CONST.__objc_selrefs: 0x1be10
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1518
-  __DATA_CONST.__objc_arraydata: 0x1378
+  __DATA_CONST.__objc_arraydata: 0x1280
   __AUTH_CONST.__auth_got: 0x20b0
-  __AUTH_CONST.__const: 0x8ae0
-  __AUTH_CONST.__cfstring: 0x3a780
+  __AUTH_CONST.__const: 0x8b00
+  __AUTH_CONST.__cfstring: 0x3a760
   __AUTH_CONST.__objc_const: 0x83b78
-  __AUTH_CONST.__objc_intobj: 0x33c0
-  __AUTH_CONST.__objc_arrayobj: 0x1098
-  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __AUTH_CONST.__objc_intobj: 0x3378
+  __AUTH_CONST.__objc_arrayobj: 0x1050
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x54d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5BB3181B-3EC5-3BCF-BA43-8831C6200C1F
-  Functions: 25561
-  Symbols:   76842
-  CStrings:  42897
+  UUID: C199E044-5004-37FF-9EC6-9B578DCC15EE
+  Functions: 25566
+  Symbols:   76857
+  CStrings:  42898
 
Symbols:
+ -[ATXFaceGalleryLayoutGenerator _localizedNameForPosterWithAppBundleId:extensionBundleId:]
+ ___58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.67
+ ___59-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke
+ ___59-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke.cold.1
+ ___62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.115
+ ___62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.120
+ ___78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke_5
+ ___block_descriptor_40_e8_32bs_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_"ATXPosterDescriptor"16?0"NSString"8ls32l8
+ ___block_literal_global.111
+ ___block_literal_global.126
+ _objc_msgSend$_localizedNameForPosterWithAppBundleId:extensionBundleId:
+ _objc_msgSend$localizedNameForBundle:
- ___58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.64
- ___62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.158
- ___block_literal_global.114
Functions:
~ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 80 -> 84
~ +[ATXActionPredictionsHelpers keepRandomPredictionItems:limit:predictionItemsToKeep:] : 800 -> 804
~ __ZNSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE24__emplace_back_slow_pathIJRKSF_EEEPSF_DpOT_ : 304 -> 308
~ __ZNSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_ : 312 -> 316
~ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 300 -> 296
~ ___79+[ATXActionCacheReader _getExtraPredictionsFromChunk:map:abGroup:assetVersion:]_block_invoke : 480 -> 484
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP9ATXActioniEENS_22__unordered_map_hasherIS4_S5_13ATXActionHash14ATXActionEqualLb1EEENS_21__unordered_map_equalIS4_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JS4_RlEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 648 -> 644
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP8NSStringPK17ATXPredictionItemEENS_22__unordered_map_hasherIS4_S8_15ATXNSStringHash16ATXNSStringEqualLb1EEENS_21__unordered_map_equalIS4_S8_SB_SA_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS4_JNS_4pairIS4_S7_EEEEENSJ_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 636 -> 632
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em : 60 -> 64
~ -[ATXFaceSuggestionAssetParameters unitySectionDescriptors] : 12 -> 92
+ ___59-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke
~ -[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors] : 268 -> 304
~ ___62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke : 416 -> 484
+ ___62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.120
~ -[ATXFaceSuggestionAssetParameters uprankedDateIntervals] : 1552 -> 1480
~ ___53-[ATXFaceGalleryLayoutGenerator _processDescriptors:]_block_invoke : 1512 -> 1532
~ +[ATXFaceGalleryLayoutGenerator _descriptorsByDeduplicatingExtensionsInDescriptors:] : 1100 -> 1348
+ -[ATXFaceGalleryLayoutGenerator _localizedNameForPosterWithAppBundleId:extensionBundleId:]
~ -[ATXFaceGalleryLayoutGenerator _localizedTitleTextWithSemanticType:] : 348 -> 356
~ -[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:] : 2700 -> 2744
+ ___78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke_5
~ -[ATXFaceSuggestionConfiguredWatchFaceSignal valueForDescriptor:] : 1028 -> 1048
+ ___91-[ATXFaceSuggestionAssetParameters extensionBundleIdsEligibleForComplicationsInFaceGallery]_block_invoke.cold.1
CStrings:
+ "-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke"
+ "@\"ATXPosterDescriptor\"16@?0@\"NSString\"8"
+ "UnitySectionDescriptors"
+ "_localizedNameForPosterWithAppBundleId:extensionBundleId:"
+ "com.apple.EmojiPoster"
+ "com.apple.GradientPoster"
+ "com.apple.Posters.KaleidoscopePosterApp"
+ "com.apple.Posters.KaleidoscopePosterApp.KaleidoscopePoster"
+ "com.apple.Posters.UnityPosterApp.ExtragalacticPoster"
+ "com.apple.Posters.UnityPosterApp.RhizomePoster"
+ "com.apple.Posters.UnityPosterApp.Unity2025Poster"
+ "com.apple.Posters.UnityPosterApp.UnityPosterExtension"
+ "com.apple.Posters.WeatherPosterApp.WeatherPoster"
+ "com.apple.PridePoster"
+ "v52@0:8C16@20{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}{?=^{ATXPredictionItem}}}28"
+ "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}\"count\"Q}\"enumerationInProgress\"B}"
+ "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HTGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HTGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{unordered_map<ATXAction *, int, ATXActionHash, ATXActionEqual, std::allocator<std::pair<ATXAction *const, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<ATXAction *, int>, std::__unordered_map_hasher<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionHash, ATXActionEqual>, std::__unordered_map_equal<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionEqual, ATXActionHash>, std::allocator<std::__hash_value_type<ATXAction *, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<ATXAction *, int, ATXActionHash, ATXActionEqual, std::allocator<std::pair<ATXAction *const, int>>>={__hash_table<std::__hash_value_type<ATXAction *, int>, std::__unordered_map_hasher<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionHash, ATXActionEqual>, std::__unordered_map_equal<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionEqual, ATXActionHash>, std::allocator<std::__hash_value_type<ATXAction *, int>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *>=^v}}{?=Q}{?=f}}}16@0:8"
+ "{unordered_map<NSString *, ATXPredictionItem, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, ATXPredictionItem>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, ATXPredictionItem>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, ATXPredictionItem>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<NSString *, ATXPredictionItem, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, ATXPredictionItem>>>={__hash_table<std::__hash_value_type<NSString *, ATXPredictionItem>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, ATXPredictionItem>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *>=^v}}{?=Q}{?=f}}}24@0:8@16"
+ "{unordered_map<NSString *, const ATXPredictionItem *, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, const ATXPredictionItem *>>>={__hash_table<std::__hash_value_type<NSString *, const ATXPredictionItem *>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, const ATXPredictionItem *>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, const ATXPredictionItem *>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, const ATXPredictionItem *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *>=^v}}{?=Q}{?=f}}}24@0:8r^v16"
+ "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=\"__begin_\"^{ATXPredictionItem}\"__end_\"^{ATXPredictionItem}\"\"{?=\"__cap_\"^{ATXPredictionItem}}}"
+ "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}{?=^{ATXPredictionItem}}}24@0:8@16"
+ "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}{?=^{ATXPredictionItem}}}40@0:8@16@24@32"
+ "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}{?=^{ATXPredictionItem}}}48@0:8@16@24@32@40"
+ "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}{?=^{ATXPredictionItem}}}68@0:8@16@24C32@36@44@52@60"
- "com.apple.EmojiPoster.EmojiPosterExtension:nature"
- "com.apple.GradientPoster.GradientPosterExtension:plum.preset3"
- "com.apple.MercuryPoster:space"
- "com.apple.NanoUniverse.AegirProxyApp.AegirPoster:Earth"
- "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:black"
- "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:blue"
- "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:unity"
- "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-1"
- "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-4"
- "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-5"
- "com.apple.WatchFacesWallpaperSupport.Unity2025Poster:unity/com.apple.PridePoster.PridePosterExtension:grid-fill"
- "com.apple.weather.poster:weather-poster-gallery"
- "v52@0:8C16@20{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}^{ATXPredictionItem}}28"
- "{HDGuardedData=\"scores\"{SimdVector<float __attribute__((ext_vector_type(8))), float>=\"chunks\"{vector<float __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<float __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"abs\"{SimdVector<int __attribute__((ext_vector_type(8))), unsigned int>=\"chunks\"{vector<int __attribute__((ext_vector_type(8))), (anonymous namespace)::SimdAlignedAllocator<int __attribute__((ext_vector_type(8)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}\"count\"Q}\"enumerationInProgress\"B}"
- "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HDGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"^v}"
- "{unique_ptr<proactive::pas::SynchronizedObject<(anonymous namespace)::HTGuardedData, proactive::pas::detail::RecursiveMutex>, std::default_delete<proactive::pas::SynchronizedObject<(anonymous namespace)::HTGuardedData, proactive::pas::detail::RecursiveMutex>>>=\"__ptr_\"^v}"
- "{unordered_map<ATXAction *, int, ATXActionHash, ATXActionEqual, std::allocator<std::pair<ATXAction *const, int>>>=\"__table_\"{__hash_table<std::__hash_value_type<ATXAction *, int>, std::__unordered_map_hasher<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionHash, ATXActionEqual>, std::__unordered_map_equal<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionEqual, ATXActionHash>, std::allocator<std::__hash_value_type<ATXAction *, int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<ATXAction *, int, ATXActionHash, ATXActionEqual, std::allocator<std::pair<ATXAction *const, int>>>={__hash_table<std::__hash_value_type<ATXAction *, int>, std::__unordered_map_hasher<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionHash, ATXActionEqual>, std::__unordered_map_equal<ATXAction *, std::__hash_value_type<ATXAction *, int>, ATXActionEqual, ATXActionHash>, std::allocator<std::__hash_value_type<ATXAction *, int>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<ATXAction *, int>, void *> *>=^v}Qf}}16@0:8"
- "{unordered_map<NSString *, ATXPredictionItem, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, ATXPredictionItem>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, ATXPredictionItem>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, ATXPredictionItem>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_map<NSString *, ATXPredictionItem, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, ATXPredictionItem>>>={__hash_table<std::__hash_value_type<NSString *, ATXPredictionItem>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, ATXPredictionItem>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, ATXPredictionItem>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, ATXPredictionItem>, void *> *>=^v}Qf}}24@0:8@16"
- "{unordered_map<NSString *, const ATXPredictionItem *, ATXNSStringHash, ATXNSStringEqual, std::allocator<std::pair<NSString *const, const ATXPredictionItem *>>>={__hash_table<std::__hash_value_type<NSString *, const ATXPredictionItem *>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, const ATXPredictionItem *>, ATXNSStringHash, ATXNSStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, const ATXPredictionItem *>, ATXNSStringEqual, ATXNSStringHash>, std::allocator<std::__hash_value_type<NSString *, const ATXPredictionItem *>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, const ATXPredictionItem *>, void *> *>=^v}Qf}}24@0:8r^v16"
- "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=\"__begin_\"^{ATXPredictionItem}\"__end_\"^{ATXPredictionItem}\"__cap_\"^{ATXPredictionItem}}"
- "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}^{ATXPredictionItem}}24@0:8@16"
- "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}^{ATXPredictionItem}}40@0:8@16@24@32"
- "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}^{ATXPredictionItem}}48@0:8@16@24@32@40"
- "{vector<ATXPredictionItem, std::allocator<ATXPredictionItem>>=^{ATXPredictionItem}^{ATXPredictionItem}^{ATXPredictionItem}}68@0:8@16@24C32@36@44@52@60"

```
