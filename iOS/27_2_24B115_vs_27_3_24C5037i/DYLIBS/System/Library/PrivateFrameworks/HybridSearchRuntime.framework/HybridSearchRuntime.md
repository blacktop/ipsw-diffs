## HybridSearchRuntime

> `/System/Library/PrivateFrameworks/HybridSearchRuntime.framework/HybridSearchRuntime`

```diff

-73.3.4.0.0
-  __TEXT.__text: 0x294a98
+73.14.0.2.0
+  __TEXT.__text: 0x2b3b74
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0xe4d8
-  __TEXT.__swift5_typeref: 0x5fe0
-  __TEXT.__swift5_fieldmd: 0x2aac
-  __TEXT.__constg_swiftt: 0x37a0
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x21d7
-  __TEXT.__swift5_assocty: 0xa60
-  __TEXT.__swift5_protos: 0x80
-  __TEXT.__swift5_proto: 0x5bc
-  __TEXT.__swift5_types: 0x414
-  __TEXT.__cstring: 0xf372
-  __TEXT.__swift5_capture: 0x4888
-  __TEXT.__oslogstring: 0x7452
-  __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__swift_as_entry: 0x13cc
-  __TEXT.__swift_as_ret: 0x1c98
-  __TEXT.__swift_as_cont: 0x3804
+  __TEXT.__const: 0xf148
+  __TEXT.__swift5_typeref: 0x621c
+  __TEXT.__swift5_fieldmd: 0x2d20
+  __TEXT.__constg_swiftt: 0x3990
+  __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_reflstr: 0x2347
+  __TEXT.__swift5_assocty: 0xab0
+  __TEXT.__swift5_protos: 0x7c
+  __TEXT.__swift5_proto: 0x600
+  __TEXT.__swift5_types: 0x450
+  __TEXT.__cstring: 0xfd22
+  __TEXT.__swift5_capture: 0x4cdc
+  __TEXT.__oslogstring: 0x7852
+  __TEXT.__swift5_mpenum: 0x80
+  __TEXT.__swift_as_entry: 0x14c0
+  __TEXT.__swift_as_ret: 0x1dcc
+  __TEXT.__swift_as_cont: 0x3d20
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__swift5_acfuncs: 0x2d0
+  __TEXT.__swift5_acfuncs: 0x2f8
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0xdee0
-  __TEXT.__eh_frame: 0x27b10
+  __TEXT.__unwind_info: 0xf290
+  __TEXT.__eh_frame: 0x29e08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1010
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__got: 0x1a18
-  __AUTH_CONST.__const: 0x10030
+  __DATA_CONST.__got: 0x1a58
+  __AUTH_CONST.__const: 0x11120
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x1fa8
+  __AUTH_CONST.__objc_const: 0x1f88
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2c90
+  __AUTH_CONST.__auth_got: 0x2d08
   __AUTH.__objc_data: 0x150
-  __AUTH.__data: 0x1720
-  __DATA.__data: 0x2458
+  __AUTH.__data: 0x18b0
+  __DATA.__data: 0x25c8
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0x3ad0
-  __DATA_DIRTY.__bss: 0x2f80
+  __DATA_DIRTY.__data: 0x3a00
+  __DATA_DIRTY.__bss: 0x2e80
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14583
-  Symbols:   336
-  CStrings:  1040
+  Functions: 15473
+  Symbols:   342
+  CStrings:  1098
 
Symbols:
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get_throwing
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
- _swift_task_future_wait_throwing
CStrings:
+ " (\n    id SERIAL PRIMARY KEY,\n    embedding FLOAT16["
+ " (\n    slot UINT16 PRIMARY KEY,\n    model_name STRING,\n    model_version UINT16\n);"
+ " are both stamped "
+ " as both current and legacy"
+ " has a stamp whose columns cannot be read"
+ " is not the current model "
+ " {\n    slot: 0,\n    model_name: 'appleEmbeddingModel',\n    model_version: 10\n});"
+ " {slot: $slot})\nSET s.model_name = $name,\n    s.model_version = $version;"
+ "%{public}s: checkpoint after dropping slot tables failed; the next open will replay the drops: %{public}@"
+ "%{public}s: legacy generation %{public}s failed for %{public}s; continuing with the current generation only: %{public}@"
+ "%{public}s: skipping vector search for %{public}s — embedding generation timed out"
+ "%{public}s: skipping vector search for %{public}s — embedding model error: %{public}@"
+ "%{public}s: skipping vector search for %{public}s — unexpected error: %{public}@"
+ "',\n    'embedding',\n    metric := '"
+ "',\n    'embedding',\n    metric := 'cosine'\n);"
+ ")\nRETURN s.slot, s.model_name, s.model_version;"
+ ") RETURN count(c);"
+ ", which this build has no storage for"
+ ": it holds the current embedding model"
+ "ALTER INDEX Documents_general_fts ON Documents_general ADD mailAccount_emailAddressText STRING FTS_ONLY;"
+ "ALTER INDEX Documents_general_fts ON Documents_general ADD mailAccount_name STRING FTS_ONLY;"
+ "ALTER TABLE Documents_general ADD mailAccount_accountIdentifier STRING;"
+ "ALTER TABLE Documents_general ADD mailAccount_appEntityIdentifier STRING;"
+ "ALTER TABLE Documents_general ADD mailAccount_emailAddress STRING;"
+ "ALTER TABLE Documents_general ADD mailAccount_sourceBundleIdentifier STRING;"
+ "An embedding slot stamp has a slot column that cannot be read"
+ "Embedding generations name "
+ "Embedding model prewarm completed for %{public}s (including CLIPSafety)"
+ "Embedding slot stamp names slot "
+ "Embedding slots "
+ "Embedding slots resolved: current=%{public}s (%{public}s), legacy=%{public}s, clearing=%{public}s"
+ "HybridIndex creation finished without publishing an index"
+ "Index opened read-only with %{public}ld slot(s) needing a clear; disabling vector search rather than returning results from a generation nothing can correct"
+ "Index opened read-only; nothing to clear, vector search stays enabled"
+ "IngestionManager: dropLegacyEmbeddings called"
+ "MATCH (s:_hybridindex_embedding_slots)\nWHERE s.slot = $slot\nDELETE s;"
+ "Refusing to drop slot "
+ "]->()\nRETURN count(DISTINCT d);"
+ "_hybridindex_embedding_slots"
+ "appleEmbeddingModel"
+ "database still referenced as its HybridIndex deallocates"
+ "dropLegacyEmbeddings"
+ "dropLegacyEmbeddings (slot "
+ "dropLegacyEmbeddings: legacy and current both resolve to slot %{public}s"
+ "dropLegacyEmbeddings: no legacy slot to reclaim; no-op"
+ "dropLegacyEmbeddings: reclaiming slot %{public}s (%{public}s) holding %{public}lld chunk(s)"
+ "dropLegacyEmbeddings: slot %{public}s reclaimed"
+ "dropLegacyEmbeddings: write connection unavailable (%{public}s); failing fast so the caller retries"
+ "embedQueryUsingSafety: starting embedding generation (model=%{public}s, timeout=%{public}s, priority=%{public}hhu, checkSafety=%{bool,public}d, contextLength=%{public}s)"
+ "embedding version "
+ "embeddingCountsByModel"
+ "embeddingSlotResolutionFailed"
+ "global_textContent"
+ "hybridIndexConcurrentInstances: "
+ "hybridIndexCreationNotPublished: "
+ "hybridIndexDatabaseOutlivedIndex: "
+ "hybridIndexEmbeddingSlotResolutionFailed: "
+ "hybridIndexLeakedConnection: "
+ "operation retained its connection"
+ "perform(text:version:checkSafety:safetyThreshold:embeddingModelProperties:contextLength:allowTruncation:sendAnalyticsEvent:)"
+ "performHybridRetrieve"
+ "performHybridRetrieve: no queryable embedding generation for %{public}s - skipping"
+ "performHybridSearch"
+ "performHybridSearch: no queryable embedding generation for %{public}s, skipping"
+ "resolveEmbeddingSlots (cleared "
+ "siriTranscript_chunkIndexContent"
+ "the previous HybridIndex outlived the manager's last reference to it"
+ "tokenCount(for:version:)"
+ "updateEmbeddings: rejecting embedding for entityType=%{public}s provenanceStableIdentifier=%{public}s — tagged version %{public}hu, current model is %{public}s"
- "%{public}s: skipping, not an internal build"
- "Embedding model prewarm completed (including CLIPSafety)"
- "embedQueryUsingSafety: starting embedding generation (timeout=%{public}s, priority=%{public}hhu, checkSafety=%{bool,public}d, contextLength=%{public}s)"
- "perform(text:checkSafety:safetyThreshold:embeddingModelProperties:contextLength:allowTruncation:sendAnalyticsEvent:)"
- "performHybridRetrieve: skipping vector retrieval for %{public}s — embedding generation timed out"
- "performHybridRetrieve: skipping vector retrieval for %{public}s — embedding model error: %{public}@"
- "performHybridRetrieve: skipping vector retrieval for %{public}s — unexpected error: %{public}@"
- "performHybridSearch: skipping vector search for %{public}s — embedding generation timed out"
- "performHybridSearch: skipping vector search for %{public}s — embedding model error: %{public}@"
- "performHybridSearch: skipping vector search for %{public}s — unexpected error: %{public}@"
- "tokenCount(for:)"
```
