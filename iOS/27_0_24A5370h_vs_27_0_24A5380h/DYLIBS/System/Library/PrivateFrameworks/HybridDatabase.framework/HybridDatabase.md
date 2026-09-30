## HybridDatabase

> `/System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase`

```diff

-  __TEXT.__text: 0x83d550
+  __TEXT.__text: 0x7fc0d8
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__gcc_except_tab: 0x54508
-  __TEXT.__const: 0xe9540
-  __TEXT.__constg_swiftt: 0xa68
-  __TEXT.__swift5_typeref: 0x890
+  __TEXT.__gcc_except_tab: 0x54a70
+  __TEXT.__const: 0xe9980
+  __TEXT.__constg_swiftt: 0xac8
+  __TEXT.__swift5_typeref: 0x8e0
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x65d
-  __TEXT.__swift5_fieldmd: 0xa30
-  __TEXT.__cstring: 0x26673
+  __TEXT.__swift5_reflstr: 0x70d
+  __TEXT.__swift5_fieldmd: 0xac8
+  __TEXT.__cstring: 0x222eb
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
-  __TEXT.__unwind_info: 0x1a818
-  __TEXT.__eh_frame: 0x3be0
+  __TEXT.__unwind_info: 0x1a900
+  __TEXT.__eh_frame: 0x3e50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38a80
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0x38ac0
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
-  __AUTH_CONST.__auth_got: 0xfd8
-  __AUTH.__data: 0x10
+  __AUTH_CONST.__auth_got: 0x1008
+  __AUTH.__data: 0xd0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__data: 0x4e8
+  __DATA.__data: 0x494
   __DATA.__common: 0x18
-  __DATA.__bss: 0x4118
-  __DATA_DIRTY.__data: 0x920
-  __DATA_DIRTY.__bss: 0x4340
+  __DATA.__bss: 0x3e78
+  __DATA_DIRTY.__data: 0x988
+  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__bss: 0x4630
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 22044
-  Symbols:   464
-  CStrings:  5593
+  Functions: 22193
+  Symbols:   470
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
- __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x8
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
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/common/file_system/local_file_system.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/expression_evaluator/pattern_evaluator.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/optimizer/correlated_subquery_unnest_solver.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/planner/operator/logical_flatten.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/processor/operator/hash_join/hash_join_probe.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/storage/buffer_manager/bm_page_lock.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/storage/free_space_manager.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/HybridDatabase/libhybriddatabase/src/storage/wal/wal_replayer.cpp"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:233: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:246: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:260: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:438: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:297: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:302: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:317: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:279: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:284: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/bitset:686: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/bitset:696: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1577: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2213: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:830: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1148: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/regex:4741: libc++ Hardening assertion ready() failed: match_results::format() called when not ready\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:465: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:508: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:522: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:526: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:537: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:550: libc++ Hardening assertion !empty() failed: span<T>::front() on empty span\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:555: libc++ Hardening assertion !empty() failed: span<T>::back() on empty span\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1362: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1492: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1497: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1502: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1507: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3384: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3393: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:331: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:417: libc++ Hardening assertion __pos < size() failed: string_view[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:425: libc++ Hardening assertion !empty() failed: string_view::front(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:429: libc++ Hardening assertion !empty() failed: string_view::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:436: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
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
