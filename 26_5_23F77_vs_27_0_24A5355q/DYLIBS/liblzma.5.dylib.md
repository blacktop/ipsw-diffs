## liblzma.5.dylib

> `/usr/lib/liblzma.5.dylib`

```diff

 21.0.0.0.0
-  __TEXT.__text: 0x171d0
-  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__text: 0x17508
   __TEXT.__const: 0x64b0
   __TEXT.__cstring: 0x310
   __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__got: 0x8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd8
-  __AUTH_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x5a8
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libSystem.B.dylib
-  UUID: 80DC43E1-B3BC-3BFC-80A0-7BFABF7D2038
+  UUID: D9A6C7BA-17DD-31E2-86B3-1BB77800AE3E
   Functions: 344
   Symbols:   634
   CStrings:  34
Functions:
~ _lzma_validate_chain : 184 -> 192
~ _lzma_index_append : 540 -> 556
~ _lzma_index_iter_next : 484 -> 492
~ _iter_set_info : 424 -> 444
~ _lzma_index_iter_locate : 236 -> 244
~ _lzma_block_header_size : 272 -> 252
~ _lzma_block_header_encode : 356 -> 364
~ _lzma_filter_encoder_is_supported : 48 -> 52
~ _index_encode : 568 -> 600
~ _lzma_vli_encode : 180 -> 188
~ _block_decode : 628 -> 644
~ _lzma_block_header_decode : 500 -> 516
~ _lzma_filter_decoder_is_supported : 48 -> 52
~ _index_decode : 728 -> 772
~ _stream_decode : 1156 -> 1160
~ _lzma_vli_decode : 332 -> 336
~ _lzma_check_update : 220 -> 228
~ _lzma_crc32 : 284 -> 288
~ _lzma_crc64 : 228 -> 236
~ _lzip_decode : 1092 -> 1100
~ _lzma_lz_encoder_init : 540 -> 548
~ _lzma_mf_find : 248 -> 252
~ _lzma_mf_hc3_find : 420 -> 432
~ _hc_find_func : 232 -> 240
~ _lzma_mf_hc3_skip : 192 -> 196
~ _lzma_mf_hc4_find : 572 -> 576
~ _lzma_mf_hc4_skip : 224 -> 232
~ _lzma_mf_bt2_find : 196 -> 200
~ _bt_find_func : 332 -> 340
~ _lzma_mf_bt2_skip : 168 -> 172
~ _bt_skip_func : 260 -> 276
~ _lzma_mf_bt3_find : 436 -> 448
~ _lzma_mf_bt3_skip : 224 -> 228
~ _lzma_mf_bt4_find : 588 -> 592
~ _lzma_mf_bt4_skip : 256 -> 264
~ _normalize : 120 -> 128
~ _lzma_str_to_filters : 1148 -> 1160
~ _lzma_str_from_filters : 964 -> 980
~ _lzma_str_list_filters : 1016 -> 1020
~ _parse_options : 900 -> 912
~ _lzma_lzma_encode : 2188 -> 2216
~ _lzma_lzma_encoder_reset : 520 -> 536
~ _lzma_lzma_encoder_create : 412 -> 416
~ _match : 952 -> 984
~ _length_update_prices : 404 -> 432
~ _lzma_lzma_preset : 244 -> 252
~ _lzma_lzma_optimum_fast : 916 -> 936
~ _lzma_lzma_optimum_normal : 6176 -> 6488
~ _get_literal_price : 200 -> 204
~ _file_info_decode : 1484 -> 1488
~ _lzma_decode : 10972 -> 10884
~ _lzma_decoder_reset : 644 -> 660
~ _lzma_decoder_uncompressed : 16 -> 20
~ _lzma_decoder_init : 224 -> 228
~ _lzma_lzma2_props_encode : 180 -> 184
~ _lzma2_encode : 824 -> 828
~ _arm64_code : 212 -> 220
~ _stream_decode_mt : 2876 -> 2880
~ _threads_end : 220 -> 224
~ _x86_code : 384 -> 388
~ _powerpc_code : 172 -> 176
~ _ia64_code : 316 -> 324
~ _arm_code : 164 -> 168
~ _armthumb_code : 188 -> 192
~ _stream_encode_mt : 1696 -> 1700
~ _threads_end : 212 -> 216
~ _threads_stop : 248 -> 256

```
