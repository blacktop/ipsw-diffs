## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-193.120.2.0.0
-  __TEXT.__text: 0x5cb30 sha256:5277406c7b70eb52b8bbfe11dee3aad04e11001a008f566258f862b17a5fc49a
-  __TEXT.__auth_stubs: 0x300 sha256:dc53a1600396cd2c2d72049ff879da063af5c778e02d1da0eaaf1219aee7bf2f
-  __TEXT.__const: 0x76951 sha256:2297f644160cc6d51c7f5660698d573e9fe5da6652e18d238e2915bd54bf4027
+210.0.0.0.0
+  __TEXT.__text: 0x65380 sha256:37a9097c8e759518507dcdeaabc21e7a5e765c07d6777e9edd5f5768658e0731
+  __TEXT.__const: 0x76e91 sha256:ebfe3deaf663523a8e00f8773c8d7849bd085fa3a706a35a9afb2c1339bea303
   __TEXT.__cstring: 0x2ec sha256:08991badba67456ea6615a2b7996b3990d16ca63fca2befaad33e5cc26615e84
-  __TEXT.__unwind_info: 0x678 sha256:e329b96e4cf45e2c4b62f80ed20d38bc0488549371b1bffb02f4e677ef9d47e8
-  __TEXT.__eh_frame: 0x448 sha256:b02a1883b6b685e07a01e0f0d72982854f40b8cabe616b11cefa606437f289e6
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x280 sha256:998e92375d48b6999096b34bcd3ba8e4a565bd15777ab4f17c0eeefbf2de246d
-  __AUTH_CONST.__auth_got: 0x180 sha256:a1a4f5721c1c4610af7f71078f3a68c330536d679803b0e0507ee8dc10c5dfca
-  __AUTH_CONST.__const: 0x10a0 sha256:f767577552ab522aa1e9c25288d89a788fad25d686575975e6678ec08b79cc4d
-  __DATA.__data: 0x80 sha256:d209f1be46f8e11e9dd52ab45d0e3c9e22d5816baf1f8e31a1f480f04b08e448
+  __TEXT.__unwind_info: 0x700 sha256:7b85e671fb81c4e6e7bb3d3e279ad2fdfd957ce2bbe23de4b59776c9ab81daff
+  __TEXT.__eh_frame: 0x448 sha256:8e33801d343baa3a891c815f9975b99c29030b4c32e0dec936c28d7a7c0c5c6d
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x280 sha256:d933944db530cd97f14814497bc9860b3f7a387c54ab82f01694e1ac3dac1590
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x10a0 sha256:16d6f99fb67d0f972bd30e708e621c3553d9f416c3787f553166a50c79775c6f
+  __AUTH_CONST.__auth_got: 0x188 sha256:3eefc4790b52024832ea4c03c6e7a781f3ef9416866a959b2777fce101ad9d61
+  __DATA.__data: 0x480 sha256:dd3f25da8c6a644686d063ab8738c84ca9e68fe69e4e961b576865d4ace8dbe8
   __DATA.__common: 0x1200 sha256:606f558e014930f9c1669f03c71c28945c4631568e39cd308c6c7f4077c7bfb9
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: EBC43580-EB14-3833-9757-701CD16872EF
-  Functions: 527
-  Symbols:   1171
+  UUID: E825FC1F-5BAD-3E75-8EDD-A444376FDD28
+  Functions: 546
+  Symbols:   1229
   CStrings:  49
 
Symbols:
+ _MshDecoderFetchStream
+ _MshEncoderAppendStream
+ _MshEncoderFlush
+ _OUTLINED_FUNCTION_1
+ _RavDecodeBlock
+ _RavEncodeBlock
+ _RavGetOptimal
+ _RavInitCostTable
+ _RavInitOptimal
+ _RavMatchFinderCreateTree
+ _RavMatchFinderDestroy
+ _RavMatchFinderSearch
+ _RavMatchFinderSearchTree
+ _RavRefreshCostCache
+ _RavRefreshMatchLengthCache
+ _RavRefreshRecentLengthCache
+ _RavSelectParser
+ __ZL14MshCopyFirst16Phj.rep_distance
+ __ZL14MshCopyFirst16Phj.rep_distance4
+ __ZL14MshCopyFirst16Phj.rep_distance8
+ __ZL14MshFilterMatchjj.maxDistance
+ __ZL14RavUpdateStatehh.lut
+ __ZL16RavCreateParsingP6RavOptj
+ __ZL18RavCopyMatchUnsafePhS_j.rep_distance
+ __ZL18RavCopyMatchUnsafePhS_j.repeat_perm
+ __ZL19RavGetLitLamContexth.lut
+ __ZL20RavModelInitCommandsP8RavModel.lit_state_count
+ __ZL20RavModelInitCommandsP8RavModel.mat_state_count
+ __ZL22RavMatchFinderSkipTreeP20RavMatchFinderStructj
+ _memcmp
+ _msh_decode_buffer
+ _msh_decode_scratch_size
+ _msh_encode_buffer
+ _msh_encode_scratch_size
+ _rav_cost_lut
+ _rav_decode_buffer
+ _rav_decode_scratch_size
+ _rav_encode_buffer
+ _rav_encode_scratch_size
+ _rav_stream_identify_algorithm
- _PalDecoderFetchStream
- _PalEncoderAppendStream
- _PalEncoderFlush
- __ZL14PalCopyFirst16Phj.rep_distance
- __ZL14PalCopyFirst16Phj.rep_distance4
- __ZL14PalCopyFirst16Phj.rep_distance8
- __ZL14PalFilterMatchjj.maxDistance
- _pal_decode_buffer
- _pal_decode_scratch_size
- _pal_encode_buffer
- _pal_encode_scratch_size

```
