## EmojiFoundation

> `/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation`

```diff

-261.2.0.0.0
-  __TEXT.__text: 0x57e80
+261.3.0.0.0
+  __TEXT.__text: 0x57ea4
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_methlist: 0x2534
   __TEXT.__const: 0x9082

   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_classname: 0x65f
   __TEXT.__objc_methname: 0x5777
-  __TEXT.__objc_methtype: 0xff2
+  __TEXT.__objc_methtype: 0x1004
   __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x24558

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EE9016D5-276D-3E24-8ADE-89041813A2BF
+  UUID: 8FB4FCED-26F2-32D0-89BE-A27C01F29FC5
   Functions: 1881
   Symbols:   11026
   CStrings:  4125
Functions:
~ __ZNSt3__16vectorINS_7variantIJNS_9monostateEjdNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IhNS6_IhEEEEEEENS6_ISB_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEmEENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE4findIS7_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_ : 252 -> 256
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN3CEM18AdaptationDatabaseEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JNS_4pairIKS7_SB_EEEEENSO_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_ : 604 -> 608
~ __ZNSt3__120back_insert_iteratorINS_6vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS5_IS7_EEEEEaSB8ne200100EOS7_ : 328 -> 332
~ __ZNSt3__16vectorINS_3mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_7variantIJNS_9monostateEjdS7_NS0_IhNS5_IhEEEEEEENS_4lessIS7_EENS5_INS_4pairIKS7_SC_EEEEEENS5_ISJ_EEE24__emplace_back_slow_pathIJRKSJ_EEEPSJ_DpOT_ : 304 -> 308
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEmEENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRS7_RlEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 616 -> 620
~ ___47-[TESTriggerPhraseCollection _buildAndLoadTrie]_block_invoke : 1752 -> 1756
~ __ZNSt3__16vectorINS_12basic_stringIDsNS_11char_traitsIDsEENS_9allocatorIDsEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZN4trie4TrieItDsN8internal6marisa6CursorEE5buildEmPPKcPKmPKx : 588 -> 596
~ __ZNSt3__16vectorINS_12basic_stringIDsNS_11char_traitsIDsEENS_9allocatorIDsEEEENS4_IS6_EEE24__emplace_back_slow_pathIJPKDsmEEEPS6_DpOT_ : 300 -> 312
CStrings:
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{unique_ptr<CEM::AdaptationDatabaseController, std::default_delete<CEM::AdaptationDatabaseController>>=\"\"{?=\"__ptr_\"^{AdaptationDatabaseController}}}"
+ "{unique_ptr<trie::MarisaTrie<unsigned short, char16_t>, std::default_delete<trie::MarisaTrie<unsigned short, char16_t>>>=\"\"{?=\"__ptr_\"^v}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- "{unique_ptr<CEM::AdaptationDatabaseController, std::default_delete<CEM::AdaptationDatabaseController>>=\"__ptr_\"^{AdaptationDatabaseController}}"
- "{unique_ptr<trie::MarisaTrie<unsigned short, char16_t>, std::default_delete<trie::MarisaTrie<unsigned short, char16_t>>>=\"__ptr_\"^v}"

```
