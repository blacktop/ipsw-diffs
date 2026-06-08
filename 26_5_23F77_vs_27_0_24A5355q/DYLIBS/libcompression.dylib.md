## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-193.120.2.0.0
-  __TEXT.__text: 0x5cb30
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__const: 0x76951
+210.0.0.0.0
+  __TEXT.__text: 0x65380
+  __TEXT.__const: 0x76e91
   __TEXT.__cstring: 0x2ec
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__unwind_info: 0x700
   __TEXT.__eh_frame: 0x448
-  __DATA_CONST.__got: 0x10
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x280
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x10a0
-  __DATA.__data: 0x80
+  __AUTH_CONST.__auth_got: 0x188
+  __DATA.__data: 0x480
   __DATA.__common: 0x1200
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
