## NaturalLanguage

> `/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`

```diff

-172.0.0.0.0
-  __TEXT.__text: 0x53d44
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x366c
-  __TEXT.__const: 0x534
-  __TEXT.__cstring: 0x3569
+172.2.0.0.0
+  __TEXT.__text: 0x53e68
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_methlist: 0x3684
+  __TEXT.__const: 0x53c
+  __TEXT.__cstring: 0x354d
   __TEXT.__ustring: 0x32
   __TEXT.__gcc_except_tab: 0x2c64
-  __TEXT.__oslogstring: 0xdb
-  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__oslogstring: 0x128
+  __TEXT.__unwind_info: 0x1720
   __TEXT.__objc_classname: 0x5f5
-  __TEXT.__objc_methname: 0x6c88
+  __TEXT.__objc_methname: 0x6cda
   __TEXT.__objc_methtype: 0x1c4e
-  __TEXT.__objc_stubs: 0x4f00
+  __TEXT.__objc_stubs: 0x4f20
   __DATA_CONST.__got: 0x650
-  __DATA_CONST.__const: 0x12e8
+  __DATA_CONST.__const: 0x1368
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e8
+  __DATA_CONST.__objc_selrefs: 0x19f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__auth_got: 0xb70
+  __AUTH_CONST.__const: 0x650
+  __AUTH_CONST.__cfstring: 0x4740
   __AUTH_CONST.__objc_const: 0x6798
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xd8

   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x3bc
   __DATA.__data: 0x4c8
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x228
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91E259A1-851B-347C-A854-DFA712F337A2
-  Functions: 1580
-  Symbols:   5820
-  CStrings:  2561
+  UUID: E502766A-C6C4-386C-AE5D-24C7D9623435
+  Functions: 1588
+  Symbols:   5852
+  CStrings:  2580
 
Symbols:
+ +[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:].cold.2
+ -[NLContextualEmbedding _sentenceEmbeddingVectorDataForString:error:]
+ -[NLContextualEmbedding _sentenceEmbeddingVectorForString:error:]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table111
+ GCC_except_table25
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table62
+ GCC_except_table75
+ GCC_except_table88
+ _NLContextualEmbeddingSignpostHandle
+ _NLContextualEmbeddingSignpostHandle.cold.1
+ _NLContextualEmbeddingSignpostHandle.log_handle
+ _NLContextualEmbeddingSignpostHandle.onceToken
+ __OBJC_$_PROP_LIST_NLE5Embedding.256
+ __ZZL30getSentencePieceModelLoadQueuevE5queue
+ __ZZL30getSentencePieceModelLoadQueuevE9onceToken
+ ___61+[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:]_block_invoke
+ ___NLContextualEmbeddingSignpostHandle_block_invoke
+ ____ZL30getSentencePieceModelLoadQueuev_block_invoke
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.265
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.392
+ __os_signpost_emit_with_name_impl
+ _objc_exception_rethrow
+ _objc_msgSend$_sentenceEmbeddingVectorDataForString:error:
+ _objc_msgSend$_sentenceEmbeddingVectorForString:error:
+ _objc_terminate
+ _os_signpost_enabled
+ _os_signpost_id_generate
- GCC_except_table100
- GCC_except_table103
- GCC_except_table108
- GCC_except_table22
- GCC_except_table34
- GCC_except_table41
- GCC_except_table53
- GCC_except_table86
- __OBJC_$_PROP_LIST_NLE5Embedding.265
- ___block_literal_global.232
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.244
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.250
- ___block_literal_global.390
- _objc_msgSend$now
CStrings:
+ "_sentenceEmbeddingVectorDataForString:error:"
+ "_sentenceEmbeddingVectorForString:error:"
+ "bn-Latn"
+ "com.apple.NaturalLanguage"
+ "com.apple.NaturalLanguage.SentencePieceModelLoadQueue"
+ "compileE5"
+ "gu-Latn"
+ "hi-Latn"
+ "inferenceE5"
+ "kn-Latn"
+ "loadAdapterE5"
+ "loadBackboneE5"
+ "loadE5"
+ "ml-Latn"
+ "mr-Latn"
+ "pa-Latn"
+ "sentenceEmbedding"
+ "ta-Latn"
+ "te-Latn"
+ "ur-Latn"
- "%.2f ms spent creating Execution Stream and allocating buffers"
- "%.2f ms spent loading head"
- "%.2f ms spent on compilation"
- "%.2f ms spent running head inference"
- "%.2f ms spent running inference"
- "now"

```
