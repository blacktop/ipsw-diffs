## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-190.40.2.0.0
-  __TEXT.__text: 0x58f40
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__const: 0x769a1
+193.100.4.0.0
+  __TEXT.__text: 0x5c8c0
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__const: 0x76dd1
   __TEXT.__cstring: 0x2ec
-  __TEXT.__unwind_info: 0x648
+  __TEXT.__unwind_info: 0x690
   __TEXT.__eh_frame: 0x448
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x280
-  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x10a0
-  __DATA.__data: 0x80
+  __DATA.__data: 0x480
   __DATA.__common: 0x1200
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: A3410B9E-48AF-3F60-96DF-418440953C01
-  Functions: 510
-  Symbols:   1140
+  UUID: 2BB7B3E1-B6CE-3C91-9ACE-D819B51BE26D
+  Functions: 531
+  Symbols:   1195
   CStrings:  49
 
Symbols:
+ _MmmDecodeBlock
+ _MmmEncodeBlock
+ _MmmGetOptimal
+ _MmmInitCostTable
+ _MmmInitOptimal
+ _MmmMatchFinderCreateTree
+ _MmmMatchFinderDestroy
+ _MmmMatchFinderSearch
+ _MmmMatchFinderSearchTree
+ _MmmRefreshCostCache
+ _MmmRefreshMatchLengthCache
+ _MmmRefreshRecentLengthCache
+ _MmmSelectParser
+ _OUTLINED_FUNCTION_0
+ __ZL14MmmUpdateStatehh.lut
+ __ZL16MmmCreateParsingP6MmmOptj
+ __ZL18MmmCopyMatchUnsafePhS_j.rep_distance
+ __ZL18MmmCopyMatchUnsafePhS_j.repeat_perm
+ __ZL19MmmGetLitLamContexth.lut
+ __ZL20MmmModelInitCommandsP8MmmModel.lit_state_count
+ __ZL20MmmModelInitCommandsP8MmmModel.mat_state_count
+ __ZL22MmmMatchFinderSkipTreeP20MmmMatchFinderStructj
+ _init_quantization_lut
+ _memcmp
+ _mmm_cost_lut
+ _mmm_decode_buffer
+ _mmm_decode_scratch_size
+ _mmm_encode_buffer
+ _mmm_encode_scratch_size
+ _mmm_stream_identify_algorithm
+ _strlen
- _getDecoderTable
- _quantize_slow

```
