## NaturalLanguage

> `/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`

```diff

-174.5.0.0.0
-  __TEXT.__text: 0x57b00
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x36cc
-  __TEXT.__const: 0x4f4
-  __TEXT.__cstring: 0x3740
+174.6.0.0.0
+  __TEXT.__text: 0x58a80
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_methlist: 0x3704
+  __TEXT.__const: 0x4c4
+  __TEXT.__cstring: 0x3951
   __TEXT.__ustring: 0x32
-  __TEXT.__gcc_except_tab: 0x2d38
+  __TEXT.__gcc_except_tab: 0x2e8c
   __TEXT.__oslogstring: 0x128
-  __TEXT.__unwind_info: 0x1750
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__objc_classname: 0x5f5
-  __TEXT.__objc_methname: 0x6de7
-  __TEXT.__objc_methtype: 0x1c8a
-  __TEXT.__objc_stubs: 0x4fe0
+  __TEXT.__objc_methname: 0x6eaf
+  __TEXT.__objc_methtype: 0x1ca8
+  __TEXT.__objc_stubs: 0x5040
   __DATA_CONST.__got: 0x650
-  __DATA_CONST.__const: 0x1368
+  __DATA_CONST.__const: 0x13e0
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a18
+  __DATA_CONST.__objc_selrefs: 0x1a40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__auth_got: 0xb60
   __AUTH_CONST.__const: 0x650
-  __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0x67c8
+  __AUTH_CONST.__cfstring: 0x4a20
+  __AUTH_CONST.__objc_const: 0x67e8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x3c0
+  __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0x4c8
   __DATA.__bss: 0x228
   __DATA_DIRTY.__objc_data: 0x14f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F8AB24F-1AE3-35F0-AE53-F96C4B3EB43B
-  Functions: 1595
-  Symbols:   5870
-  CStrings:  2609
+  UUID: 3789F5AF-EFF2-3601-BB3E-A4EB66DF6196
+  Functions: 1604
+  Symbols:   5898
+  CStrings:  2640
 
Symbols:
+ +[NLE5Embedding compileEmbeddingModelWithModelPath:cachePath:useANE:adapters:]
+ +[NLE5Embedding embeddingModelWithModelPath:cachePath:useANE:adapters:]
+ +[NLE5Embedding embeddingModelWithModelPath:cachePath:useANE:adapters:].cold.1
+ +[NLE5Embedding embeddingModelWithModelPath:cachePath:useANE:adapters:].cold.2
+ +[NLE5Embedding isCompiledEmbeddingModelWithModelPath:cachePath:useANE:adapters:error:]
+ -[NLContextualEmbedding _obtainCompiledModelCachePathIfNeeded]
+ -[NLContextualEmbedding _setCachePathOnce:]
+ -[NLContextualEmbedding cachePath]
+ -[NLContextualEmbedding setCachePath:]
+ -[NLXPCEmbeddingServerClient compiledModelCacheForIdentifier:completionHandler:]
+ -[NLXPCEmbeddingServerClient synchronousCompiledModelCacheForIdentifier:completionHandler:]
+ GCC_except_table107
+ GCC_except_table71
+ GCC_except_table80
+ _OBJC_IVAR_$_NLContextualEmbedding._cachePath
+ __ZL12compileModelRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbP7NSArrayIP8NSStringEPKc
+ __ZL12compileModelRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbP7NSArrayIP8NSStringEPKc.cold.1
+ ___62-[NLContextualEmbedding _obtainCompiledModelCachePathIfNeeded]_block_invoke
+ ___71+[NLE5Embedding embeddingModelWithModelPath:cachePath:useANE:adapters:]_block_invoke
+ ___80-[NLXPCEmbeddingServerClient compiledModelCacheForIdentifier:completionHandler:]_block_invoke
+ ___80-[NLXPCEmbeddingServerClient compiledModelCacheForIdentifier:completionHandler:]_block_invoke_2
+ ___91-[NLXPCEmbeddingServerClient synchronousCompiledModelCacheForIdentifier:completionHandler:]_block_invoke
+ ___91-[NLXPCEmbeddingServerClient synchronousCompiledModelCacheForIdentifier:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e43_v32?0"NSString"8"NSString"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32r40r_e43_v32?0"NSString"8"NSString"16"NSError"24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v32?0"NSString"8"NSString"16"NSError"24ls32l8s40l8
+ ___block_literal_global.229
+ ___block_literal_global.429
+ __isRunningInDaemon
+ _objc_msgSend$_obtainCompiledModelCachePathIfNeeded
+ _objc_msgSend$_setCachePathOnce:
+ _objc_msgSend$_xpc_compiledEmbeddingModelCacheForIdentifier:completionHandler:
+ _objc_msgSend$compileEmbeddingModelWithModelPath:cachePath:useANE:adapters:
+ _objc_msgSend$compiledModelCacheForIdentifier:completionHandler:
+ _objc_msgSend$embeddingModelWithModelPath:cachePath:useANE:adapters:
+ _objc_msgSend$isCompiledEmbeddingModelWithModelPath:cachePath:useANE:adapters:error:
+ _objc_msgSend$synchronousCompiledModelCacheForIdentifier:completionHandler:
+ _objc_sync_enter
+ _objc_sync_exit
- +[NLE5Embedding compileEmbeddingModelWithModelPath:useANE:adapters:]
- +[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:]
- +[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:].cold.1
- +[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:].cold.2
- +[NLE5Embedding isCompiledEmbeddingModelWithModelPath:useANE:adapters:error:]
- -[NLXPCEmbeddingServerClient compileModelWithIdentifier:completionHandler:]
- GCC_except_table63
- GCC_except_table75
- __ZL10kModelPath
- __ZL12compileModelRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbP7NSArrayIP8NSStringE
- __ZL12compileModelRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbP7NSArrayIP8NSStringE.cold.1
- ___61+[NLE5Embedding embeddingModelWithModelPath:useANE:adapters:]_block_invoke
- ___75-[NLXPCEmbeddingServerClient compileModelWithIdentifier:completionHandler:]_block_invoke
- ___75-[NLXPCEmbeddingServerClient compileModelWithIdentifier:completionHandler:]_block_invoke_2
- ___block_literal_global.213
- ___block_literal_global.392
- _objc_msgSend$_xpc_compileEmbeddingForIdentifier:completionHandler:
- _objc_msgSend$compileEmbeddingModelWithModelPath:useANE:adapters:
- _objc_msgSend$compileModelWithIdentifier:completionHandler:
- _objc_msgSend$embeddingModelWithModelPath:useANE:adapters:
- _objc_msgSend$isCompiledEmbeddingModelWithModelPath:useANE:adapters:error:
CStrings:
+ "'%@' %s compilation to '%@'"
+ "'compileModel '%s' to cache path: '%s'"
+ "/private/var/db/com.apple.naturallanguaged"
+ "@44@0:8@16@24B32@36"
+ "B44@0:8@16@24B32@36"
+ "B52@0:8@16@24B32@36^@44"
+ "Cache path already set for '%@' - '%@', ignoring new value"
+ "Compilation path is not set for '%@' - '%@' model"
+ "Embedding model '%@' - '%@' is %@ (error: %@)"
+ "Failed to locate compilation cache for embedding model"
+ "Failed to obtain compiled model cache from daemon: %@"
+ "Failed to obtain model compilation cache"
+ "Obtained cachePath '%@' - '%@': %@"
+ "Requesting cachePath '%@' - '%@'"
+ "_cachePath"
+ "_obtainCompiledModelCachePathIfNeeded"
+ "_setCachePathOnce:"
+ "_xpc_compiledEmbeddingModelCacheForIdentifier:completionHandler:"
+ "cachePath"
+ "compileEmbeddingModelWithModelPath:cachePath:useANE:adapters:"
+ "compiled"
+ "compiledModelCacheForIdentifier:completionHandler:"
+ "embeddingModelWithModelPath:cachePath:useANE:adapters:"
+ "isCompiledEmbeddingModelWithModelPath:cachePath:useANE:adapters:error:"
+ "not compiled"
+ "setCachePath:"
+ "synchronousCompiledModelCacheForIdentifier:completionHandler:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSError\"24"
- "'%@' %s compilation"
- "@36@0:8@16B24@28"
- "B36@0:8@16B24@28"
- "B44@0:8@16B24@28^@36"
- "_xpc_compileEmbeddingForIdentifier:completionHandler:"
- "compileEmbeddingModelWithModelPath:useANE:adapters:"
- "compileModelWithIdentifier:completionHandler:"
- "embeddingModelWithModelPath:useANE:adapters:"
- "isCompiledEmbeddingModelWithModelPath:useANE:adapters:error:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
