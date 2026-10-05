## EmbeddingCore

> `/System/Library/PrivateFrameworks/EmbeddingCore.framework/EmbeddingCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-460.8.2.0.0
-  __TEXT.__text: 0x69f08
+460.12.1.0.0
+  __TEXT.__text: 0x69fdc
   __TEXT.__objc_methlist: 0x1954
   __TEXT.__const: 0x1160
-  __TEXT.__gcc_except_tab: 0x7308
+  __TEXT.__gcc_except_tab: 0x7330
   __TEXT.__cstring: 0x5df2
-  __TEXT.__oslogstring: 0x191f
+  __TEXT.__oslogstring: 0x195f
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__constg_swiftt: 0x1b8
   __TEXT.__swift5_builtin: 0x14

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2125
+  Functions: 2127
   Symbols:   3314
-  CStrings:  740
+  CStrings:  741
 
Functions:
~ -[MADCrossEncoder _processNextBatch:] : 1652 -> 1656
~ -[MADCrossEncoder _processQuery:documents:maxNumChunks:chunkOverlap:outputs:] : 1852 -> 1928
~ -[MADCrossEncoder _createBatchedInputIdsWithBatchSize:queryTokens:chunks:realCount:] : 1072 -> 1136
~ _OUTLINED_FUNCTION_7 : 12 -> 20
+ _OUTLINED_FUNCTION_8
~ __ZNKSt3__114default_deleteIN13sentencepiece4util6Status3RepEEclB9fqe220106EPS4_ : 92 -> 88
~ -[MADCrossEncoder _processQuery:documents:maxNumChunks:chunkOverlap:outputs:].cold.2 : 56 -> 64
~ -[MADCrossEncoder _processQuery:documents:maxNumChunks:chunkOverlap:outputs:].cold.3 : 60 -> 56
~ -[MADCrossEncoder _processQuery:documents:maxNumChunks:chunkOverlap:outputs:].cold.7 : 56 -> 60
~ -[MADCrossEncoder _processQuery:documents:maxNumChunks:chunkOverlap:outputs:].cold.8 : 80 -> 56
+ +[MADTextEmbeddingSafety createForEmbeddingVersion:].cold.1
CStrings:
+ "MADCrossEncoder: no room for document tokens (ctx %lu, query %lu)"
+ "cross_encoder_v140_ane_8bit_combined"
- "cross_encoder_v130_ane_8bit_combined"
```
