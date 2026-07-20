## HybridDatabase

> `/System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__thread_vars`

```diff

-46.0.1.0.0
-  __TEXT.__text: 0x7fc0d8
+49.0.1.0.0
+  __TEXT.__text: 0x803554
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__gcc_except_tab: 0x54a70
-  __TEXT.__const: 0xe9980
+  __TEXT.__gcc_except_tab: 0x5552c
+  __TEXT.__const: 0xe9b40
   __TEXT.__constg_swiftt: 0xac8
-  __TEXT.__swift5_typeref: 0x8e0
+  __TEXT.__swift5_typeref: 0x8f6
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x70d
-  __TEXT.__swift5_fieldmd: 0xac8
-  __TEXT.__cstring: 0x222eb
+  __TEXT.__swift5_reflstr: 0x6ad
+  __TEXT.__swift5_fieldmd: 0xa98
+  __TEXT.__cstring: 0x22915
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_proto: 0x1dc
   __TEXT.__swift5_types: 0xec
-  __TEXT.__oslogstring: 0x3158
-  __TEXT.__swift5_capture: 0x200
+  __TEXT.__oslogstring: 0x31e3
+  __TEXT.__swift5_capture: 0x1e0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1a900
-  __TEXT.__eh_frame: 0x3e50
+  __TEXT.__unwind_info: 0x1aa90
+  __TEXT.__eh_frame: 0x3f08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38ac0
+  __DATA_CONST.__const: 0x38ab0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0xd8
-  __DATA_CONST.__got: 0x528
-  __AUTH_CONST.__const: 0x395b8
+  __DATA_CONST.__objc_selrefs: 0xc8
+  __DATA_CONST.__got: 0x540
+  __AUTH_CONST.__const: 0x39610
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0xbd0
+  __AUTH_CONST.__objc_const: 0xb70
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x1008
-  __AUTH.__data: 0xd0
+  __AUTH_CONST.__auth_got: 0x1040
+  __AUTH.__data: 0xc8
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__data: 0x494
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x3e78
-  __DATA_DIRTY.__data: 0x988
+  __DATA.__data: 0x4ac
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x3e68
+  __DATA_DIRTY.__data: 0x978
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x4630
+  __DATA_DIRTY.__bss: 0x4690
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 22193
-  Symbols:   470
-  CStrings:  5599
+  Functions: 22234
+  Symbols:   475
+  CStrings:  5623
 
Symbols:
+ _CFRelease
+ _CFStringCreateMutableCopy
+ _CFStringNormalize
+ _CFStringTransform
+ _objc_retain
+ _objc_retain_x19
- _objc_release_x28
CStrings:
+ " ..."
+ " RETURN COUNT(*);"
+ " is out of the representable range for a Kuzu timestamp."
+ ") RETURN num_terms_processed, num_new_terms, last_cursor"
+ "49.0.1"
+ "ANALYZE_FTS_INDEX"
+ "BufferReader: attempted to read {} bytes from buffer with only {} bytes remaining (buffer size {})."
+ "COPY `{}` FROM (MATCH (b:`{}`) WITH b.term as term, {}, CAST(count(*) as UINT32) as tf, {} as dense_positions_lists RETURN term, {}, tf, list_transform(list_filter(dense_positions_lists, x -> x.lst IS NOT NULL), x -> list_sort(x.lst)), list_transform(list_filter(dense_positions_lists, x -> x.lst IS NOT NULL), x -> x.idx));"
+ "CREATE (:`{}` {fts_index_name: '{}', table_name: '{}', start_term_offset: 0, max_term_offset: {}});"
+ "CREATE NODE TABLE IF NOT EXISTS `{}` (id INT64 PRIMARY KEY, state INT64);"
+ "CREATE NODE TABLE `{}` (fts_index_name STRING PRIMARY KEY, table_name STRING, start_term_offset INT64, max_term_offset INT64);"
+ "DATABASE_UUID"
+ "Deserialized std::vector length {} exceeds remaining input bytes {}."
+ "Deserialized string length {} exceeds remaining input bytes {}."
+ "Failed to count vacuum hard failures."
+ "Failed to count vacuum interruption failures."
+ "Failed to create _VACUUM_FAILURE_LOG table."
+ "Failed to record vacuum failure for type "
+ "HDB:checkpoint_on_close"
+ "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %llu bytes)"
+ "HDBTokenizer::splitFusedTerm: called on invalid tokenizer (moved-from or init failed); returning empty"
+ "Incremental FTS retokenize: %s [%llu, %llu)/%llu, processed %llu terms, added %llu new terms, cursor %llu."
+ "Integrity check failed on FTS index {}. Position values in sublist {} are not sorted ascendingly: positions[{}]={} <= positions[{}]={} for term offset {} and doc offset {}."
+ "MATCH (:`{}`)-[:`{}`]->(:`{}`) RETURN count(*)"
+ "MATCH (a:`_VACUUM_FAILURE_LOG`) WHERE a.type = "
+ "MATCH (a:`{}`) RETURN a.state;"
+ "MATCH (n:`{}`) RETURN count(*)"
+ "Mismatch between null segment and null column existance."
+ "Rare case: FSST-compressed string data was larger than the uncompressed data. %{public}lu/%{public}llu strings with total size %{public}llu were compressed into a %{public}llu byte buffer"
+ "Retokenize progress table was not initialized. The database may need to be re-opened."
+ "Segment page range [{}, {}) is beyond the end of the DB file (numPages={})."
+ "String index {} at position {} is out of bounds (max {})! "
+ "String offsets for lookup are invalid or fall outside the bounds of the data! String: [{}, {}), max offset in segment: {}"
+ "String offsets to be scanned ({}/{}) are invalid or fall outside the bounds of the data! String: [{}, {}), max offset in segment: {}"
+ "String offsets {}, {} are decreasing instead of increasing. Length of compressed string was {}"
+ "String segment has no null segment!"
+ "Term alternatives shouldn't be generated for a stopword only query fragment."
+ "_VACUUM_FAILURE_LOG"
+ "_VACUUM_STATE"
+ "`(\n    id SERIAL,\n    type INT64,\n    progress DOUBLE,\n    PRIMARY KEY(id)\n)"
+ "checkpoint_on_close failed: %s"
+ "checkpoint_on_close: time_ms=%{public}llu"
+ "columnID < dataTypes.size()"
+ "com.apple.hybriddatabase.retokenize"
+ "createInternalRetokenizeTable: failed with unknown error"
+ "createInternalRetokenizeTable: failed: %{public}s"
+ "interruptionCount"
+ "numTermsProcessed"
+ "num_new_terms"
+ "uuid"
- "',\n    start_term_offset: 0,\n    max_term_offset: "
- "',\n    table_name: '"
- ") RETURN num_terms_processed, last_cursor"
- "46.0.1"
- "COPY `{}` FROM (MATCH (b:`{}`) WITH b.term as term, {}, CAST(count(*) as UINT32) as tf, {} as dense_positions_lists RETURN term, {}, tf, list_transform(list_filter(dense_positions_lists, x -> x.lst IS NOT NULL), x -> x.lst), list_transform(list_filter(dense_positions_lists, x -> x.lst IS NOT NULL), x -> x.idx));"
- "CREATE NODE TABLE IF NOT EXISTS `_VACUUM_STATE`(id INT64 PRIMARY KEY, state INT64);"
- "CREATE NODE TABLE `"
- "Checkpoint during database destruction failed with error %{public}s "
- "Checkpoint during database destruction failed with unknown error"
- "Failed to create _INCREMENTAL_FTS_RETOKENIZE_PROGRESS table."
- "Failed to create retokenize progress entry for "
- "HDB:deinit_db"
- "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %zu bytes)"
- "Incremental FTS retokenize: %s [%llu, %llu)/%llu, processed %llu terms, cursor %llu."
- "Incremental FTS retokenize: registered %s/%s (max offset: %lld)"
- "Incremental FTS retokenize: skipping %s/%s (empty terms table)"
- "Ingested failure."
- "MATCH (a:`_VACUUM_STATE`) RETURN a.state;"
- "No vacuum is in progress."
- "No vacuum to resume."
- "Vacuum was interrupted."
- "` {\n    fts_index_name: '"
- "`(\n    fts_index_name STRING PRIMARY KEY,\n    table_name STRING,\n    start_term_offset INT64,\n    max_term_offset INT64\n)"
- "checkpoint_on_close: finished"
- "deinit_db: starting"
- "deinit_db: time_ms=%{public}llu"
```
