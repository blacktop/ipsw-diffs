## SiriEntityMatcher

> `/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher`

```diff

-3510.3.1.0.0
-  __TEXT.__text: 0x5e470
+3510.5.2.0.0
+  __TEXT.__text: 0x5e4f8
   __TEXT.__auth_stubs: 0x16d0
   __TEXT.__objc_methlist: 0x401c
   __TEXT.__const: 0x13b7c

   __TEXT.__oslogstring: 0x66a0
   __TEXT.__cstring: 0x70ff
   __TEXT.__swift5_typeref: 0x2a
-  __TEXT.__gcc_except_tab: 0x3ae8
+  __TEXT.__gcc_except_tab: 0x3aec
   __TEXT.__ustring: 0x9e78
   __TEXT.__unwind_info: 0x1c38
   __TEXT.__eh_frame: 0xb0
   __TEXT.__objc_classname: 0x9ee
   __TEXT.__objc_methname: 0x846d
-  __TEXT.__objc_methtype: 0x2486
+  __TEXT.__objc_methtype: 0x24aa
   __TEXT.__objc_stubs: 0x6fa0
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0x24998

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 565B265E-F655-3B16-B967-F49ABA2B8E3B
+  UUID: 29FF09B3-9E20-3728-957A-5E0A91E1B0A4
   Functions: 1635
   Symbols:   553
   CStrings:  3594
Functions:
~ sub_267dd5588 -> sub_268028588 : 1788 -> 1796
~ sub_267dd7e54 -> sub_26802ae5c : 328 -> 332
~ sub_267dd8548 -> sub_26802b554 : 76 -> 80
~ sub_267dd8d2c -> sub_26802bd3c : 188 -> 192
~ sub_267ddc588 -> sub_26802f59c : 68 -> 64
~ sub_267ddc7ac -> sub_26802f7bc : 88 -> 80
~ sub_267ddce70 -> sub_26802fe78 : 832 -> 840
~ sub_267ddd43c -> sub_26803044c : 3556 -> 3572
~ sub_267de2128 -> sub_268035148 : 412 -> 420
~ sub_267de2878 -> sub_2680358a0 : 824 -> 836
~ sub_267de2f84 -> sub_268035fb8 : 300 -> 304
~ sub_267de32b8 -> sub_2680362f0 : 548 -> 544
~ sub_267de35f4 -> sub_268036628 : 308 -> 312
~ sub_267de3b4c -> sub_268036b84 : 1368 -> 1380
~ sub_267de5e84 -> sub_268038ec8 : 160 -> 164
~ sub_267de7984 -> sub_26803a9cc : 3396 -> 3400
~ sub_267de99c8 -> sub_26803ca14 : 540 -> 544
~ sub_267de9be4 -> sub_26803cc34 : 676 -> 680
~ sub_267de9f04 -> sub_26803cf58 : 224 -> 228
~ sub_267debb68 -> sub_26803ebc0 : 368 -> 372
~ sub_267e09544 -> sub_26805c5a0 : 1956 -> 1972
~ sub_267e17648 -> sub_26806a6b4 : 1892 -> 1920
~ sub_267e21fa0 -> sub_268075028 : 356 -> 360
~ sub_267e2b8fc -> sub_26807e988 : 320 -> 316
CStrings:
+ "{Indexer=\"context\"{ContextV2=\"pimpl\"{shared_ptr<skit::internal::ContextImpl>=\"__ptr_\"^{ContextImpl}\"__cntrl_\"^{__shared_weak_count}}}\"index_writer\"{IndexWriter=\"pimpl\"{unique_ptr<skit::internal::IndexWriterImpl, std::default_delete<skit::internal::IndexWriterImpl>>=\"\"{?=\"__ptr_\"^{IndexWriterImpl}}}}\"index_locale\"q\"index_locale_id\"{basic_string<char16_t, std::char_traits<char16_t>, std::allocator<char16_t>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[11S]\"__padding_\"{__padding<1UL>=\"__padding_\"[1c]}\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"^S\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"tokenizer\"{shared_ptr<semskitbridge::Tokenizer>=\"__ptr_\"^{Tokenizer}\"__cntrl_\"^{__shared_weak_count}}\"analyzer\"{shared_ptr<semskitbridge::Analyzer>=\"__ptr_\"^{Analyzer}\"__cntrl_\"^{__shared_weak_count}}\"alias\"{Alias=\"pimpl\"{shared_ptr<skit::internal::AliasImpl>=\"__ptr_\"^{AliasImpl}\"__cntrl_\"^{__shared_weak_count}}}\"trial_factors\"{TrialFactors=\"use_contact_aliases\"B\"use_contact_emoji_matches\"B\"use_contact_diacritics_stripping\"B\"use_contact_prefix_matching\"B\"use_contact_phonetic_search\"B\"use_token_lemmatization\"B\"phonetic_search_n_gram_order\"i\"use_media_threshold_filtering\"B\"index_phonetic_vector_db\"B}\"index_features\"S}"
+ "{TokenStream=\"__begin_\"^{Token}\"__end_\"^{Token}\"\"{?=\"__cap_\"^{Token}}}"
+ "{path=\"__pn_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}}"
+ "{unique_ptr<semskitbridge::Indexer, std::default_delete<semskitbridge::Indexer>>=\"\"{?=\"__ptr_\"^{Indexer}}}"
+ "{vector<std::pair<semskitbridge::SearchGroup, std::vector<std::byte>>, std::allocator<std::pair<semskitbridge::SearchGroup, std::vector<std::byte>>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
- "{Indexer=\"context\"{ContextV2=\"pimpl\"{shared_ptr<skit::internal::ContextImpl>=\"__ptr_\"^{ContextImpl}\"__cntrl_\"^{__shared_weak_count}}}\"index_writer\"{IndexWriter=\"pimpl\"{unique_ptr<skit::internal::IndexWriterImpl, std::default_delete<skit::internal::IndexWriterImpl>>=\"__ptr_\"^{IndexWriterImpl}}}\"index_locale\"q\"index_locale_id\"{basic_string<char16_t, std::char_traits<char16_t>, std::allocator<char16_t>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[11S]\"__padding_\"{__padding<1UL>=\"__padding_\"[1c]}\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"^S\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}\"tokenizer\"{shared_ptr<semskitbridge::Tokenizer>=\"__ptr_\"^{Tokenizer}\"__cntrl_\"^{__shared_weak_count}}\"analyzer\"{shared_ptr<semskitbridge::Analyzer>=\"__ptr_\"^{Analyzer}\"__cntrl_\"^{__shared_weak_count}}\"alias\"{Alias=\"pimpl\"{shared_ptr<skit::internal::AliasImpl>=\"__ptr_\"^{AliasImpl}\"__cntrl_\"^{__shared_weak_count}}}\"trial_factors\"{TrialFactors=\"use_contact_aliases\"B\"use_contact_emoji_matches\"B\"use_contact_diacritics_stripping\"B\"use_contact_prefix_matching\"B\"use_contact_phonetic_search\"B\"use_token_lemmatization\"B\"phonetic_search_n_gram_order\"i\"use_media_threshold_filtering\"B\"index_phonetic_vector_db\"B}\"index_features\"S}"
- "{TokenStream=\"__begin_\"^{Token}\"__end_\"^{Token}\"__cap_\"^{Token}}"
- "{path=\"__pn_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{unique_ptr<semskitbridge::Indexer, std::default_delete<semskitbridge::Indexer>>=\"__ptr_\"^{Indexer}}"
- "{vector<std::pair<semskitbridge::SearchGroup, std::vector<std::byte>>, std::allocator<std::pair<semskitbridge::SearchGroup, std::vector<std::byte>>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"

```
