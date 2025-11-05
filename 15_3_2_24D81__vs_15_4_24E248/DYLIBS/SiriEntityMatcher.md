## SiriEntityMatcher

> `/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/Versions/A/SiriEntityMatcher`

```diff

-3403.4.1.14.1
-  __TEXT.__text: 0x5bccc
+3404.45.3.0.0
+  __TEXT.__text: 0x5b9ac
   __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_methlist: 0x321c
-  __TEXT.__const: 0x1381c
-  __TEXT.__gcc_except_tab: 0x38a8
-  __TEXT.__cstring: 0x635c
-  __TEXT.__oslogstring: 0x5cad
-  __TEXT.__ustring: 0x98ee
+  __TEXT.__objc_methlist: 0x374c
+  __TEXT.__const: 0x13864
   __TEXT.__dlopen_cstrs: 0x78
-  __TEXT.__unwind_info: 0x1aa0
+  __TEXT.__gcc_except_tab: 0x38c4
+  __TEXT.__cstring: 0x6361
+  __TEXT.__oslogstring: 0x5ca0
+  __TEXT.__ustring: 0x98ee
+  __TEXT.__unwind_info: 0x1a48
   __TEXT.__objc_classname: 0x802
-  __TEXT.__objc_methname: 0x758a
-  __TEXT.__objc_methtype: 0x2470
+  __TEXT.__objc_methname: 0x75a0
+  __TEXT.__objc_methtype: 0x2430
   __TEXT.__objc_stubs: 0x6560
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0x22f08

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d10
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x930
   __AUTH_CONST.__const: 0x2330
   __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0x6b98
+  __AUTH_CONST.__objc_const: 0x6280
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x1900
   __DATA.__objc_ivar: 0x3d4

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libskit.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8F7F5C54-74D7-3613-A65F-E52886530078
-  Functions: 1529
+  UUID: 3EB7852E-6B96-3154-9923-5A916979A0A7
+  Functions: 1505
   Symbols:   472
-  CStrings:  3245
+  CStrings:  3246
 
CStrings:
+ " itemType: %@, %@%@content: %@, allMetaContentCount: %d"
+ "%s Accepted %u / %u candidate(s) in group: %@"
+ "prettyPrintedResults:"
+ "{Indexer=\"context\"{ContextV2=\"pimpl\"{shared_ptr<skit::internal::ContextImpl>=\"__ptr_\"^{ContextImpl}\"__cntrl_\"^{__shared_weak_count}}}\"index_writer\"{IndexWriter=\"pimpl\"{unique_ptr<skit::internal::IndexWriterImpl, std::default_delete<skit::internal::IndexWriterImpl>>=\"__ptr_\"{__compressed_pair<skit::internal::IndexWriterImpl *, std::default_delete<skit::internal::IndexWriterImpl>>=\"__value_\"^{IndexWriterImpl}}}}\"index_locale\"q\"index_locale_id\"{basic_string<char16_t, std::char_traits<char16_t>, std::allocator<char16_t>>=\"__r_\"{__compressed_pair<std::basic_string<char16_t>::__rep, std::allocator<char16_t>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[11S]\"__padding_\"[1C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"^S\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"tokenizer\"{shared_ptr<semskitbridge::Tokenizer>=\"__ptr_\"^{Tokenizer}\"__cntrl_\"^{__shared_weak_count}}\"analyzer\"{shared_ptr<semskitbridge::Analyzer>=\"__ptr_\"^{Analyzer}\"__cntrl_\"^{__shared_weak_count}}\"alias\"{Alias=\"pimpl\"{shared_ptr<skit::internal::AliasImpl>=\"__ptr_\"^{AliasImpl}\"__cntrl_\"^{__shared_weak_count}}}\"trial_factors\"{TrialFactors=\"use_contact_aliases\"B\"use_contact_emoji_matches\"B\"use_contact_diacritics_stripping\"B\"use_contact_prefix_matching\"B\"use_contact_phonetic_search\"B\"use_token_lemmatization\"B\"phonetic_search_n_gram_order\"i\"use_media_threshold_filtering\"B}\"index_features\"S}"
+ "{path=\"__pn_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}}"
- " itemType: %@, %@%@content: %@, allMetaContent: %@"
- "%s Accepted %u / %u candidate(s) in group: %@%{sensitive}@"
- "{Indexer=\"context\"{ContextV2=\"pimpl\"{shared_ptr<skit::internal::ContextImpl>=\"__ptr_\"^{ContextImpl}\"__cntrl_\"^{__shared_weak_count}}}\"index_writer\"{IndexWriter=\"pimpl\"{unique_ptr<skit::internal::IndexWriterImpl, std::default_delete<skit::internal::IndexWriterImpl>>=\"__ptr_\"{__compressed_pair<skit::internal::IndexWriterImpl *, std::default_delete<skit::internal::IndexWriterImpl>>=\"__value_\"^{IndexWriterImpl}}}}\"index_locale\"q\"index_locale_id\"{basic_string<char16_t, std::char_traits<char16_t>, std::allocator<char16_t>>=\"__r_\"{__compressed_pair<std::basic_string<char16_t>::__rep, std::allocator<char16_t>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[11S]\"__padding_\"[1C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"^S\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}\"tokenizer\"{shared_ptr<semskitbridge::Tokenizer>=\"__ptr_\"^{Tokenizer}\"__cntrl_\"^{__shared_weak_count}}\"analyzer\"{shared_ptr<semskitbridge::Analyzer>=\"__ptr_\"^{Analyzer}\"__cntrl_\"^{__shared_weak_count}}\"alias\"{Alias=\"pimpl\"{shared_ptr<skit::internal::AliasImpl>=\"__ptr_\"^{AliasImpl}\"__cntrl_\"^{__shared_weak_count}}}\"trial_factors\"{TrialFactors=\"use_contact_aliases\"B\"use_contact_emoji_matches\"B\"use_contact_diacritics_stripping\"B\"use_contact_prefix_matching\"B\"use_contact_phonetic_search\"B\"use_token_lemmatization\"B\"phonetic_search_n_gram_order\"i\"use_media_threshold_filtering\"B}\"index_features\"S}"
- "{path=\"__pn_\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}}"

```
