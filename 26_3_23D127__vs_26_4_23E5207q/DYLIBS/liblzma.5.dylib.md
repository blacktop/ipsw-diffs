## liblzma.5.dylib

> `/usr/lib/liblzma.5.dylib`

```diff

 21.0.0.0.0
-  __TEXT.__text: 0x1755c
+  __TEXT.__text: 0x171d0
   __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0x64c0
+  __TEXT.__const: 0x64b0
   __TEXT.__cstring: 0x310
   __TEXT.__unwind_info: 0x478
   __DATA_CONST.__got: 0x8

   __AUTH_CONST.__auth_got: 0xe8
   __AUTH_CONST.__const: 0x5a8
   - /usr/lib/libSystem.B.dylib
-  UUID: E453E834-BDC9-3930-8931-75A0C2055043
-  Functions: 343
+  UUID: 13DD6E6D-89CF-3005-88EC-24730BE36179
+  Functions: 344
   Symbols:   634
   CStrings:  34
 
Functions:
+ sub_2a50d36bc
~ _lzma_raw_coder_memusage : 144 -> 148
~ _lzma_index_padding_size : 60 -> 56
~ _lzma_index_cat : 480 -> 500
~ _lzma_index_iter_next : 488 -> 484
~ _iter_set_info : 440 -> 424
~ _lzma_vli_size : 36 -> 32
~ _lzma_filter_encoder_is_supported : 52 -> 48
~ _lzma_filter_decoder_is_supported : 52 -> 48
~ _index_decode : 732 -> 728
~ _stream_decode : 1152 -> 1156
~ _lzma_crc32 : 296 -> 284
~ _lzma_crc64 : 232 -> 228
~ _lz_encoder_prepare : 672 -> 660
~ _lzma_str_to_filters : 1152 -> 1148
~ _lzma_str_from_filters : 968 -> 964
~ _lzma_str_list_filters : 1004 -> 1016
~ _str_append_u32 : 276 -> 272
~ _parse_options : 920 -> 900
~ _lzma_lzma_encode : 2196 -> 2188
~ _length_encoder_reset : 232 -> 204
~ _lzma_lzma_encoder_create : 416 -> 412
~ _lzma_lzma_encoder_memusage : 152 -> 148
~ _match : 960 -> 952
~ _length_update_prices : 416 -> 404
~ _lzma_lzma_optimum_normal : 6972 -> 6176
~ _get_literal_price : 204 -> 200
~ _lzma_decode : 10812 -> 10972
~ _stream_decode_mt : 3000 -> 2876
~ _worker_decoder : 552 -> 544
~ _simple_code : 660 -> 684
~ _x86_code : 388 -> 384
~ _powerpc_code : 180 -> 172
~ _ia64_code : 396 -> 316
~ _stream_encode_mt : 1680 -> 1696
~ _sparc_code : 212 -> 204

```
