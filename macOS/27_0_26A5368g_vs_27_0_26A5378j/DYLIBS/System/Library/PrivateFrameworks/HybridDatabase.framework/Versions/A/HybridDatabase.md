## HybridDatabase

> `/System/Library/PrivateFrameworks/HybridDatabase.framework/Versions/A/HybridDatabase`

```diff

-  __TEXT.__text: 0x7ec4a4
+  __TEXT.__text: 0x7fd2ac
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__gcc_except_tab: 0x54384
-  __TEXT.__const: 0xe9740
-  __TEXT.__constg_swiftt: 0xa68
-  __TEXT.__swift5_typeref: 0x890
+  __TEXT.__gcc_except_tab: 0x549e4
+  __TEXT.__const: 0xe9b40
+  __TEXT.__constg_swiftt: 0xac8
+  __TEXT.__swift5_typeref: 0x8e0
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x65d
-  __TEXT.__swift5_fieldmd: 0xa30
-  __TEXT.__cstring: 0x22d07
+  __TEXT.__swift5_reflstr: 0x70d
+  __TEXT.__swift5_fieldmd: 0xac8
+  __TEXT.__cstring: 0x23dbb
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0xe4
+  __TEXT.__swift5_types: 0xec
+  __TEXT.__oslogstring: 0x3158
+  __TEXT.__swift5_capture: 0x200
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x160
-  __TEXT.__oslogstring: 0x2ed4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1a638
-  __TEXT.__eh_frame: 0x3b88
+  __TEXT.__unwind_info: 0x1a830
+  __TEXT.__eh_frame: 0x3df8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38a88
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0x38ac8
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
   __DATA_CONST.__objc_selrefs: 0xd8
-  __DATA_CONST.__got: 0x520
-  __AUTH_CONST.__const: 0x39048
+  __DATA_CONST.__got: 0x528
+  __AUTH_CONST.__const: 0x395b8
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0xa98
+  __AUTH_CONST.__objc_const: 0xbd0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0xea0
-  __AUTH.__data: 0x10
+  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH.__data: 0xd0
   __AUTH.__thread_vars: 0x78
   __AUTH.__thread_bss: 0x28
-  __DATA.__data: 0x4e8
+  __DATA.__data: 0x494
   __DATA.__common: 0x18
-  __DATA.__bss: 0x4118
-  __DATA_DIRTY.__data: 0x920
-  __DATA_DIRTY.__bss: 0x4238
+  __DATA.__bss: 0x3e78
+  __DATA_DIRTY.__data: 0x988
+  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__bss: 0x44d8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 21985
-  Symbols:   426
-  CStrings:  5528
+  Functions: 22201
+  Symbols:   436
+  CStrings:  5602
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__thread_vars : content changed
Symbols:
+ ___mac_syscall
+ __dispatch_source_type_vnode
+ _dispatch_get_global_queue
+ _dispatch_release
+ _dispatch_resume
+ _dispatch_set_context
+ _dispatch_source_cancel_and_wait
+ _dispatch_source_create
+ _dispatch_source_get_data
+ _dispatch_source_get_handle
+ _dispatch_source_set_event_handler_f
+ _objc_autoreleaseReturnValue
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc
CStrings:
+ "!databaseHeader || header->databaseID.value == databaseHeader->databaseID.value"
+ "!deletionRecord.pkVectors.empty()"
+ "!insertionRecord.ownedVectors.empty()"
+ "!tables.contains(info.oid)"
+ "'\nSET a.start_term_offset = "
+ "')\n    AND lower(index_name)=lower('"
+ "')\nRETURN COUNT(*);"
+ "') RETURN CAST(max_position AS INT64)"
+ "',\n    start_term_offset: 0,\n    max_term_offset: "
+ "',\n    table_name: '"
+ ") RETURN num_terms_processed, last_cursor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/doc_score_compute.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/doc_term_stats_collection.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/parsed_fts_query.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/query_fts_index.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/json/src/functions/extract_functions/json_extract.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/json/src/utils/json_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/function/query_hnsw_index.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_config.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_graph.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_index.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_index_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_ddl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_extension.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_extension_clause.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_file_scan.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_graph_pattern.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_reading_clause.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_updating_clause.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/copy/bind_copy_from.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bind_expression/bind_subquery_expression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/binder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/bound_statement_visitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/binder/expression/expression_util.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/catalog_entry_type.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/index_catalog_entry.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/rel_group_catalog_entry.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/table_catalog_entry.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_set.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/arrow/arrow_row_batch.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/copier_config/csv_reader_config.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/copier_config/reader_config.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/conflict_action.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/extend_direction_util.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/path_semantic.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/query_rel_type.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/rel_direction.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/table_type.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/enums/transaction_action.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/expression_type.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/file_system.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/local_file_system.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/virtual_file_system.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/index/index_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/task_system/task_scheduler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/type_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/types/interval_t.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/types/types.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/types/value/value.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/common/vector/value_vector.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/expression_evaluator_visitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/path_evaluator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/pattern_evaluator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/extension/extension.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/aggregate/min_max.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/aggregate_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/array/array_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/cast_from_string_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/comparison_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_frontier.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_task.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/gds/output_writer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/internal_id/internal_id_creation_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/list/list_range_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/list/list_sort_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/path/length_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/string/regex_replace_function.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/table/projected_graph_info.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/table/stats_info.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/table/storage_info.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/table/table_info.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/utility/count_if.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/vector_arithmetic_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/vector_cast_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/function/vector_hash_functions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/graph/parsed_graph_entry.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/main/client_context.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/optimizer/acc_hash_join_optimizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/optimizer/correlated_subquery_unnest_solver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/optimizer/projection_push_down_optimizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/expression/parsed_expression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/parsed_statement_visitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_copy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_ddl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_expression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_reading_clause.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_transaction.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/transformer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/parser/visitor/standalone_call_rewriter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/cardinality_estimator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/join_plan_solver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/join_tree.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/extend/base_logical_extend.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/factorization/flatten_resolver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_explain.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_flatten.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_hash_join.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/persistent/logical_delete.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/persistent/logical_set.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/append_simple.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_copy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_join_order.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_read.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_subquery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_update.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/planner.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/planner/query_planner.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_copy_from.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_delete.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_extend.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_insert.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_scan_node_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_semi_masker.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_set.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_simple.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/map/plan_mapper.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/aggregate/simple_aggregate.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/alter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/create_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/drop.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/hash_join/hash_join_probe.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/order_by/order_by_key_encoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/order_by/top_k.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/path_property_probe.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/delete_executor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/index_builder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/reader/copy_from_error.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/reader/parquet/column_reader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/writer/parquet/column_writer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/writer/parquet/parquet_rle_bp_encoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/scan/scan_rel_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/alter_storage_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/buffer_manager/bm_page_lock.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/buffer_manager/buffer_manager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/checkpointer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/compression/compression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/compression/float_compression.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/free_space_manager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/index/hash_index.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/index/hash_index_utils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/local_storage/local_node_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/local_storage/local_storage.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/predicate/constant_predicate.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/storage_manager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/chunked_node_group.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk_scan_cursor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk_stats.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_chunked_node_group.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_column_chunk_checkpoint_cursor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_node_group.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/dictionary_column.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/list_column.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/list_segment.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/node_group.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/node_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/pk_equals.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/rel_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/rel_table_data.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment_metadata.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment_split_streamer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/string_segment.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/table/version_info.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/undo_buffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/wal/wal_record.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/src/storage/wal/wal_replayer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/bitstate.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/compile.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/dfa.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/include/walker-inl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/nfa.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/onepass.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/parse.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/prog.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/re2.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/regexp.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/simplify.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FQVi6k/Sources/HybridDatabase/libhybriddatabase/third_party/re2/tostring.cpp"
+ "46.0.1"
+ "CALL GET_FTS_MAX_POSITION('"
+ "CALL RETOKENIZE_FTS_INDEX('"
+ "CALL show_indexes()\nWHERE lower(table_name)=lower('"
+ "CALL show_tables()\nWHERE lower(name)=lower('"
+ "CREATE NODE TABLE `"
+ "Cannot apply vnode guard to file {}: {}"
+ "Cannot confine file {}: {}"
+ "Cannot convert nil to type UInt64"
+ "Catalog::Get(clientContext)"
+ "DiskArray numElements {} exceeds PIP chain capacity {}"
+ "DiskArrayCollection first header page {} is invalid!"
+ "DiskArrayCollection header page {}'s next header page ({}) is invalid!"
+ "Failed to create _INCREMENTAL_FTS_RETOKENIZE_PROGRESS table."
+ "Failed to create retokenize progress entry for "
+ "Failed to delete retokenize progress entry for "
+ "Failed to extract column of type UInt64: "
+ "Failed to get global dispatch queue for file tamper detector, this should never happen"
+ "Failed to get max FTS position for "
+ "Failed to load retokenize progress."
+ "Failed to populate a new shadow page with the DB file contents."
+ "Failed to run incremental FTS retokenize for "
+ "Failed to update retokenize progress for "
+ "FileTamperDetector: %{public}s"
+ "FileTamperDetector: dispatch handle %{public}d and fd %{public}d don't match for file at path %{public}s"
+ "FileTamperDetector: external modification detected on file %{public}s. Types:"
+ "FileTamperDetector: failed to create tamper detector for file at path %{public}s"
+ "Found used page range (startPage={}, numPages={}) that goes past the end of the DB file (numPages={})"
+ "GET_FTS_MAX_POSITION"
+ "HDBTokenizer: segment: failed to extract UTF-8 bytes (length %llu)"
+ "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %zu bytes)"
+ "HDBTokenizer: segment: token normalization failed"
+ "HDBTokenizer::naturalTermCount: called on invalid tokenizer (moved-from or init failed); returning 0"
+ "HDBTokenizer::tokenizeForIngestion: called on invalid tokenizer (moved-from or init failed); returning 0"
+ "Incremental FTS retokenize: %s [%llu, %llu)/%llu, processed %llu terms, cursor %llu."
+ "Incremental FTS retokenize: %s complete."
+ "Incremental FTS retokenize: %s resuming at offset %llu/%llu"
+ "Incremental FTS retokenize: done in %fs"
+ "Incremental FTS retokenize: no indexes to process"
+ "Incremental FTS retokenize: registered %s/%s (max offset: %lld)"
+ "Incremental FTS retokenize: skipping %s/%s (empty terms table)"
+ "Integrity check failed on in-mem hash index. Overflow slot {} is out of bound. Num overflow slots is {}."
+ "Integrity check failed on persistent hash index. Free overflow slot {} is out of bound. Num overflow slots is {}."
+ "Integrity check failed on persistent hash index. The next overflow slot {} is out of bound. Num overflow slots is {}."
+ "LocalFileInfo: external tampering detected for file at path {}."
+ "PIP {}"
+ "PIP {}'s nextPipPageIdx"
+ "Page at file type {}, index {} evicted while reading, this should never happen."
+ "Page index {} in disk array {} is invalid"
+ "RETOKENIZE_FTS_INDEX"
+ "_INCREMENTAL_FTS_RETOKENIZE_PROGRESS"
+ "` {\n    fts_index_name: '"
+ "`(\n    fts_index_name STRING PRIMARY KEY,\n    table_name STRING,\n    start_term_offset INT64,\n    max_term_offset INT64\n)"
+ "`)\nRETURN a.fts_index_name, a.table_name, a.start_term_offset, a.max_term_offset"
+ "`)\nWHERE a.fts_index_name = '"
+ "anchorState == updateRecord.ownedSrcNodeIDVector->state && anchorState == updateRecord.ownedDstNodeIDVector->state && anchorState == updateRecord.ownedPropertyVector->state"
+ "anchorState->getSelVector().getSelSize() == 1"
+ "array page {}"
+ "delete"
+ "endOffset <= numEntries"
+ "first PIP pageIdx"
+ "index.has_value()"
+ "last_cursor"
+ "libhybriddatabase/src/include/processor/operator/sink.h"
+ "max_position"
+ "num_terms_processed"
+ "openFile: vnguard isn't available on the current system, skipping applying..."
+ "propertyVectors.size() == entry->getNumProperties()"
+ "rename"
+ "resultSet"
+ "revoke"
+ "std::nullopt == DatabaseHeader::readDatabaseHeader(*dataFH->getFileInfo())"
+ "tables.contains(tableID)"
+ "transaction && transaction->isRecovery()"
+ "transaction::Transaction::Get(clientContext) && transaction::Transaction::Get(clientContext)->isRecovery()"
+ "vnguard"
- "') \n    AND lower(index_name)=lower('"
- "') \nRETURN COUNT(*);"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/doc_score_compute.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/doc_term_stats_collection.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/parsed_fts_query.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/fts/src/function/query_fts_index.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/json/src/functions/extract_functions/json_extract.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/json/src/utils/json_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/function/query_hnsw_index.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_config.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_graph.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_index.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/extension/vector/src/index/hnsw_index_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_ddl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_extension.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_extension_clause.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_file_scan.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_graph_pattern.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_reading_clause.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/bind_updating_clause.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind/copy/bind_copy_from.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bind_expression/bind_subquery_expression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/binder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/bound_statement_visitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/binder/expression/expression_util.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/catalog_entry_type.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/index_catalog_entry.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/rel_group_catalog_entry.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_entry/table_catalog_entry.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/catalog/catalog_set.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/arrow/arrow_row_batch.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/copier_config/csv_reader_config.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/copier_config/reader_config.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/conflict_action.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/extend_direction_util.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/path_semantic.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/query_rel_type.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/rel_direction.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/table_type.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/enums/transaction_action.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/expression_type.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/file_system.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/virtual_file_system.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/index/index_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/task_system/task_scheduler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/type_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/types/interval_t.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/types/types.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/types/value/value.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/common/vector/value_vector.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/expression_evaluator_visitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/path_evaluator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/extension/extension.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/aggregate/min_max.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/aggregate_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/array/array_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/cast_from_string_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/comparison_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_frontier.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_task.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/gds/gds_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/gds/output_writer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/internal_id/internal_id_creation_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/list/list_range_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/list/list_sort_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/path/length_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/string/regex_replace_function.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/table/projected_graph_info.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/table/stats_info.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/table/storage_info.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/table/table_info.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/utility/count_if.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/vector_arithmetic_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/vector_cast_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/function/vector_hash_functions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/graph/parsed_graph_entry.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/main/client_context.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/optimizer/acc_hash_join_optimizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/optimizer/projection_push_down_optimizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/expression/parsed_expression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/parsed_statement_visitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_copy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_ddl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_expression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_reading_clause.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transform/transform_transaction.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/transformer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/parser/visitor/standalone_call_rewriter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/cardinality_estimator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/join_plan_solver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/join_order/join_tree.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/extend/base_logical_extend.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/factorization/flatten_resolver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_explain.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_hash_join.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/persistent/logical_delete.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/persistent/logical_set.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/append_simple.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_copy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_join_order.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_read.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_subquery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/plan/plan_update.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/planner.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/planner/query_planner.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_copy_from.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_delete.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_extend.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_insert.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_scan_node_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_semi_masker.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_set.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/map_simple.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/map/plan_mapper.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/aggregate/simple_aggregate.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/alter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/create_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/ddl/drop.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/order_by/order_by_key_encoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/order_by/top_k.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/path_property_probe.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/delete_executor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/index_builder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/reader/copy_from_error.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/reader/parquet/column_reader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/writer/parquet/column_writer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/persistent/writer/parquet/parquet_rle_bp_encoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/scan/scan_rel_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/alter_storage_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/buffer_manager/buffer_manager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/checkpointer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/compression/compression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/compression/float_compression.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/index/hash_index.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/index/hash_index_utils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/local_storage/local_node_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/local_storage/local_storage.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/predicate/constant_predicate.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/storage_manager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/chunked_node_group.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk_scan_cursor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/column_chunk_stats.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_chunked_node_group.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_column_chunk_checkpoint_cursor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/csr_node_group.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/dictionary_column.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/list_column.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/list_segment.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/node_group.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/node_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/pk_equals.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/rel_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/rel_table_data.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment_metadata.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/segment_split_streamer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/string_segment.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/table/version_info.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/undo_buffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/src/storage/wal/wal_record.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/bitstate.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/compile.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/dfa.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/include/walker-inl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/nfa.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/onepass.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/parse.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/prog.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/re2.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/regexp.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/simplify.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.o1Wc1E/Sources/HybridDatabase/libhybriddatabase/third_party/re2/tostring.cpp"
- "44.0.1"
- "CALL show_indexes() \nWHERE lower(table_name)=lower('"
- "CALL show_tables() \nWHERE lower(name)=lower('"
- "Failed to execute CorrelatedSubqueryUnnestSolver. This should not happen."
- "Found used page range (startPage=%{public}u, numPages=%{public}u) that goes past the end of the DB file (numPages=%{public}u)"
- "HDBTokenizer: Latin-ASCII transform failed (%llu UTF-16 code units)"
- "HDBTokenizer: failed to extract UTF-8 bytes for normalized string of length %llu"
- "HDBTokenizer: sanitized input still failed UTF-8 decode (original %zu bytes, sanitized %zu bytes)"
- "HDBTokenizer::naturalTokenCount: called on invalid tokenizer (moved-from or init failed); returning 0"
- "HDBTokenizer::streamIngestionTerms: called on invalid tokenizer (moved-from or init failed); returning 0"
- "HDBTokenizer::tokenizeForIngestion: called on invalid tokenizer (moved-from or init failed); returning empty"
- "Incremental FTS vacuum interrupted."
- "Incremental HNSW creation interrupted."
- "LogicalFlatten::computeFlatSchema() should never be used."
- "Trying to get result table from {} operator which doesn't have one."
- "Unimplemented join type for HashJoinProbe::getJoinResult()"
- "getNextTupleInternal() should not be called on sink operator."
- "{} operator does not implement getNumFlatTuples()."
- "{} operator does not implement getQueryResult()."

```
