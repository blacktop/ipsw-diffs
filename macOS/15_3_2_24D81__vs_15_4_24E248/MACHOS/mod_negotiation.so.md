## mod_negotiation.so

> `/usr/libexec/apache2/mod_negotiation.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x711c
+880.0.0.0.0
+  __TEXT.__text: 0x62bc
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__cstring: 0x76c
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 2C9BA892-FC19-36C6-BFB5-77B493286F07
+  UUID: E72A9251-747D-39A3-A9FC-E50C2C28E66B
   Functions: 47
   Symbols:   126
   CStrings:  98
Functions:
~ _create_neg_dir_config : 76 -> 72
~ _merge_neg_dir_configs : 224 -> 196
~ _cache_negotiated_docs : 88 -> 76
~ _set_language_priority : 144 -> 132
~ _set_force_priority : 396 -> 344
~ _fix_encoding : 560 -> 476
~ _handle_multi : 916 -> 792
~ _handle_map_file : 1548 -> 1376
~ _do_header_line : 172 -> 152
~ _get_entry : 1332 -> 1184
~ _atoq : 548 -> 484
~ _parse_accept_headers : 584 -> 560
~ _read_types_multi : 2080 -> 1824
~ _do_negotiation : 928 -> 792
~ _read_type_map : 1960 -> 1764
~ _set_mime_fields : 240 -> 224
~ _variantsortf : 156 -> 148
~ _get_header_line : 844 -> 760
~ _lcase_header_name_return_body : 544 -> 500
~ _strip_paren_comments : 336 -> 296
~ _do_languages_line : 272 -> 240
~ _get_body : 428 -> 392
~ _parse_negotiate_header : 612 -> 508
~ _maybe_add_default_accepts : 288 -> 260
~ _best_match : 1004 -> 824
~ _set_neg_headers : 2764 -> 2308
~ _store_variant_list : 164 -> 156
~ _setup_choice_response : 564 -> 500
~ _do_cache_negotiated_docs : 52 -> 48
~ _set_default_lang_quality : 248 -> 212
~ _discard_variant_by_env : 280 -> 248
~ _variant_has_language : 144 -> 120
~ _set_accept_quality : 660 -> 556
~ _set_language_quality : 1764 -> 1452
~ _set_encoding_quality : 672 -> 572
~ _set_charset_quality : 676 -> 556
~ _is_variant_better_rvsa : 304 -> 280
~ _is_variant_better : 1180 -> 1028
~ _is_identity_encoding : 212 -> 180
~ _mime_match : 672 -> 572
~ _find_lang_index : 284 -> 256
~ _level_cmp : 348 -> 300
~ _find_content_length : 260 -> 224
~ _make_variant_list : 992 -> 896
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_negotiation.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/mappers/mod_negotiation.c"

```
