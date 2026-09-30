## NaturalLanguage

> `/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`

```diff

-169.0.0.0.0
-  __TEXT.__text: 0x537b0
-  __TEXT.__auth_stubs: 0x1690
+172.0.0.0.0
+  __TEXT.__text: 0x53d44
+  __TEXT.__auth_stubs: 0x1660
   __TEXT.__objc_methlist: 0x366c
   __TEXT.__const: 0x534
-  __TEXT.__cstring: 0x3523
+  __TEXT.__cstring: 0x3569
   __TEXT.__ustring: 0x32
   __TEXT.__gcc_except_tab: 0x2c64
   __TEXT.__oslogstring: 0xdb
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__objc_classname: 0x5f6
-  __TEXT.__objc_methname: 0x6ca1
+  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__objc_classname: 0x5f5
+  __TEXT.__objc_methname: 0x6c88
   __TEXT.__objc_methtype: 0x1c4e
   __TEXT.__objc_stubs: 0x4f00
-  __DATA_CONST.__got: 0x668
-  __DATA_CONST.__const: 0x12d8
+  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__const: 0x12e8
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19f0
+  __DATA_CONST.__objc_selrefs: 0x19e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0xb60
+  __AUTH_CONST.__auth_got: 0xb48
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x6440
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0x6798
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_ivar: 0x3bc
   __DATA.__data: 0x4c8
   __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x14a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D575F87-19CE-3A22-B691-812D1B3ECF8F
-  Functions: 1579
-  Symbols:   5815
-  CStrings:  2553
+  UUID: 17B37320-76EF-38F6-A13D-EEABF0D6C91D
+  Functions: 1580
+  Symbols:   5820
+  CStrings:  2561
 
Symbols:
+ +[NLContextualEmbedding logCategory]
+ GCC_except_table65
+ __OBJC_$_PROP_LIST_NLE5Embedding.265
+ __OBJC_CLASS_PROTOCOLS_$_NLContextualEmbedding
+ ___47-[NLContextualEmbedding loadWithOptions:error:]_block_invoke
+ ___49-[NLTaggerAssetRequest completeWithResult:error:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_literal_global.213
+ ___block_literal_global.306
+ ___block_literal_global.390
+ _kNLEmbeddingTokenizedBatchComponentRanges
+ _kNLEmbeddingTokenizedBatchComponentsCount
- -[NLContextualEmbedding isE5Enabled]
- GCC_except_table62
- GCC_except_table67
- _NLStringEmbeddingCopyDataForTokenizedBatch
- _NLStringEmbeddingCopyTextForTokenIDs
- _NLStringEmbeddingCopyTokenIDsForText
- _OBJC_IVAR_$_NLContextualEmbedding._embedding
- _OBJC_IVAR_$_NLContextualEmbedding._isE5Enabled
- __OBJC_$_PROP_LIST_NLE5Embedding.259
- ___44-[NLContextualEmbedding requiresCompilation]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_literal_global.201
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.343
- _kNLStringEmbeddingMultilingualBERT
- _kNLStringEmbeddingTokenizedBatchComponentRanges
- _kNLStringEmbeddingTokenizedBatchComponentsCount
CStrings:
+ "'%@' %s compilation"
+ "Compilation of '%@' model failed:%@\nCaller bundle id: '%@'"
+ "Compilation of '%@' model succeeded. Caller bundle id: '%@'"
+ "Complation request for embedding model '%@' - '%@' %@ error: %@"
+ "Embedding model requires compilation"
+ "Failed to load embedding model '%@' - '%@'"
+ "Failed to locate assets for '%@' - '%@' embedding model"
+ "Loading embedding model '%@' - '%@'"
+ "doesn't require"
+ "fragmentCountPerSample"
+ "fragmentRangesForTokens"
+ "requires"
+ "succeeded"
- "Compilation of '%@' model with '%@' identifier failed:%@\nCaller bundle id: '%@'"
- "Compilation of '%@' model with '%@' identifier succeeded. Caller bundle id: '%@'"
- "Failed to load embedding model in MIL representation"
- "Failed to load sentence embedding model"
- "Is new compile required: %s"
- "NLContextualEmbedding adapters are not supported in EIR"
- "NLContextualEmbedding requires compilation, falling back to EIR"
- "_isE5Enabled"
- "isE5Enabled"
- "no"
- "yes"

```
