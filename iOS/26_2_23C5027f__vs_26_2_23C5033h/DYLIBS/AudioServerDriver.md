## AudioServerDriver

> `/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver`

```diff

 1110.2.0.0.0
-  __TEXT.__text: 0x61fac
+  __TEXT.__text: 0x62014
   __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_methlist: 0x376c
   __TEXT.__gcc_except_tab: 0x3310

   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x3da
   __TEXT.__objc_methname: 0x6351
-  __TEXT.__objc_methtype: 0x1b1f
+  __TEXT.__objc_methtype: 0x1b61
   __TEXT.__objc_stubs: 0x40c0
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0xa38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22000714-EFC2-3F58-9C33-268EB2743630
+  UUID: 0653791A-EE0E-33D5-AB8A-9D38843963CC
   Functions: 2180
   Symbols:   6371
   CStrings:  2454
Functions:
~ __ZN18ASDSRCStreamHelperC2ERK24CAStreamBasicDescriptionRKNSt3__16vectorIS0_NS3_9allocatorIS0_EEEERKNS4_INS_38ASDUnderlyingStreamDoIOOperationBlocksENS5_ISA_EEEEbj : 1792 -> 1796
~ __ZNSt3__16vectorI24CAStreamBasicDescriptionNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_IP10RamstadSRCNS_9allocatorIS2_EEEENS3_IS5_EEE24__emplace_back_slow_pathIJRKS5_EEEPS5_DpOT_ : 304 -> 300
~ __ZNSt3__16vectorIP10RamstadSRCNS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN18CASmartPreferences21_RegisterFirstHandlerEPK10__CFStringS2_NSt3__18functionIFbPKvEEE : 240 -> 244
~ __ZNSt3__16vectorIN18CASmartPreferences4PrefENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRPK10__CFStringSA_RNS_8functionIFbPKvEEEEEEPS2_DpOT_ : 332 -> 336
~ __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJ18ASDStreamDirection27AudioStreamBasicDescriptionU8__strongU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvSC_jESF_U8__strongU13block_pointerFiyjSB_EEEEPS2_DpOT_ : 368 -> 372
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIyP17ASDDSPGraphHelperLNS0_33guarded_lookup_hash_table_optionsE2ENS0_30guarded_lookup_default_hash_fnIyEEE6rehashEj : 292 -> 296
~ ___43-[ASDSRCStream _allocateStreamingResources]_block_invoke : 1180 -> 1184
~ __ZNSt3__16vectorIN18ASDSRCStreamHelper38ASDUnderlyingStreamDoIOOperationBlocksENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 324 -> 328
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIjP27ASDDeviceRealTimeOperationsLNS0_33guarded_lookup_hash_table_optionsE2ENS0_30guarded_lookup_default_hash_fnIjEEE6rehashEj : 292 -> 296
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIjP27ASDStreamRealTimeOperationsLNS0_33guarded_lookup_hash_table_optionsE2ENS0_30guarded_lookup_default_hash_fnIjEEE6rehashEj : 292 -> 296
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE16__construct_nodeIJPKcSL_EEENS_10unique_ptrINS_11__hash_nodeIS8_PvEENS_22__hash_node_destructorINS5_ISP_EEEEEEDpOT_ : 156 -> 160
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE20__node_insert_uniqueEPNS_11__hash_nodeIS8_PvEE : 100 -> 104
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJPKcEEEPS6_DpOT_ : 288 -> 284
~ __ZNSt3__16vectorIN8DSPGraph11GraphIODataENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZN20RamstadKernelFactory22ReferenceRamstadKernelEiidb : 396 -> 400
~ __ZN21RamstadKernelFactoryD22ReferenceRamstadKernelEiidb : 396 -> 400
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN5CALog5Scope4initEyPKcPK10__CFStringS5_j : 568 -> 572
~ __ZN18ASDDSPStreamHelperC2ERK24CAStreamBasicDescriptionRKNSt3__16vectorINS_9DSPStreamENS3_9allocatorIS5_EEEERN5caulk10concurrent25guarded_lookup_hash_tableIyP17ASDDSPGraphHelperLNSC_33guarded_lookup_hash_table_optionsE2ENSC_30guarded_lookup_default_hash_fnIyEEEE18ASDStreamDirection : 1756 -> 1764
~ __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE7reserveEm : 220 -> 236
~ __ZN18ASDDSPStreamHelper9addStreamERKNS_9DSPStreamE : 1276 -> 1284
~ __ZNSt3__16vectorIN18ASDDSPStreamHelper9DSPStreamENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 300 -> 304
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBTCugC9ynr0XMXt7LoDs_60ATYe8jarz5c9sAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "{list<ASDDSPGraphHelper, std::allocator<ASDDSPGraphHelper>>=\"__end_\"{__list_node_base<ASDDSPGraphHelper, void *>=\"__prev_\"^v\"__next_\"^v}\"\"{?=\"__size_\"Q}}"
+ "{unique_ptr<ASDBufferList, std::default_delete<ASDBufferList>>=\"\"{?=\"__ptr_\"^{ASDBufferList}}}"
+ "{unique_ptr<ASDDSPStreamHelper, std::default_delete<ASDDSPStreamHelper>>=\"\"{?=\"__ptr_\"^{ASDDSPStreamHelper}}}"
+ "{unique_ptr<ASDSRCStreamHelper, std::default_delete<ASDSRCStreamHelper>>=\"\"{?=\"__ptr_\"^{ASDSRCStreamHelper}}}"
+ "{unique_ptr<AudioRingBuffer, std::default_delete<AudioRingBuffer>>=\"\"{?=\"__ptr_\"^{AudioRingBuffer}}}"
+ "{unique_ptr<DSPGraph::Interpreter, std::default_delete<DSPGraph::Interpreter>>=\"\"{?=\"__ptr_\"^{Interpreter}}}"
+ "{unique_ptr<caulk::concurrent::guarded_lookup_hash_table<unsigned long long, ASDDSPGraphHelper *, caulk::concurrent::guarded_lookup_hash_table_must_count_dereferences>, std::default_delete<caulk::concurrent::guarded_lookup_hash_table<unsigned long long, ASDDSPGraphHelper *, caulk::concurrent::guarded_lookup_hash_table_must_count_dereferences>>>=\"\"{?=\"__ptr_\"^v}}"
+ "{unordered_map<std::string, std::string, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__hash_table<std::__hash_value_type<std::string, std::string>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::string>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::string>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::string>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *>=^v}}{?=Q}{?=f}}}24@0:8@16"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}24@0:8@16"
- "/AppleInternal/Library/BuildRoots/4~CATAugBY3SEDr3xxMzxP8tDmt9b6HuS8qwNyW5w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "{list<ASDDSPGraphHelper, std::allocator<ASDDSPGraphHelper>>=\"__end_\"{__list_node_base<ASDDSPGraphHelper, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
- "{unique_ptr<ASDBufferList, std::default_delete<ASDBufferList>>=\"__ptr_\"^{ASDBufferList}}"
- "{unique_ptr<ASDDSPStreamHelper, std::default_delete<ASDDSPStreamHelper>>=\"__ptr_\"^{ASDDSPStreamHelper}}"
- "{unique_ptr<ASDSRCStreamHelper, std::default_delete<ASDSRCStreamHelper>>=\"__ptr_\"^{ASDSRCStreamHelper}}"
- "{unique_ptr<AudioRingBuffer, std::default_delete<AudioRingBuffer>>=\"__ptr_\"^{AudioRingBuffer}}"
- "{unique_ptr<DSPGraph::Interpreter, std::default_delete<DSPGraph::Interpreter>>=\"__ptr_\"^{Interpreter}}"
- "{unique_ptr<caulk::concurrent::guarded_lookup_hash_table<unsigned long long, ASDDSPGraphHelper *, caulk::concurrent::guarded_lookup_hash_table_must_count_dereferences>, std::default_delete<caulk::concurrent::guarded_lookup_hash_table<unsigned long long, ASDDSPGraphHelper *, caulk::concurrent::guarded_lookup_hash_table_must_count_dereferences>>>=\"__ptr_\"^v}"
- "{unordered_map<std::string, std::string, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__hash_table<std::__hash_value_type<std::string, std::string>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::string>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::string>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::string>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::string>, void *> *>=^v}Qf}}24@0:8@16"
- "{vector<std::string, std::allocator<std::string>>=^v^v^v}24@0:8@16"

```
