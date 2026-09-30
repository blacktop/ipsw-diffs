## HybridDatabase

> `/System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase`

```diff

-49.0.1.0.0
-  __TEXT.__text: 0x803554
+54.0.0.0.0
+  __TEXT.__text: 0x806780
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__gcc_except_tab: 0x5552c
-  __TEXT.__const: 0xe9b40
-  __TEXT.__constg_swiftt: 0xac8
-  __TEXT.__swift5_typeref: 0x8f6
+  __TEXT.__gcc_except_tab: 0x558dc
+  __TEXT.__const: 0xe9cc0
+  __TEXT.__swift5_typeref: 0x90a
+  __TEXT.__swift5_reflstr: 0x70d
+  __TEXT.__swift5_assocty: 0xb0
+  __TEXT.__constg_swiftt: 0xb00
+  __TEXT.__swift5_fieldmd: 0xb30
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x6ad
-  __TEXT.__swift5_fieldmd: 0xa98
-  __TEXT.__cstring: 0x22915
-  __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0xec
-  __TEXT.__oslogstring: 0x31e3
+  __TEXT.__cstring: 0x22e16
+  __TEXT.__swift5_proto: 0x1e8
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__oslogstring: 0x31d6
   __TEXT.__swift5_capture: 0x1e0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1aa90
-  __TEXT.__eh_frame: 0x3f08
+  __TEXT.__unwind_info: 0x1b0e0
+  __TEXT.__eh_frame: 0x4010
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__weak_got: 0x20
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__got: 0x540
-  __AUTH_CONST.__const: 0x39610
+  __AUTH_CONST.__const: 0x39738
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xb70
   __AUTH_CONST.__weak_auth_got: 0x28

   __AUTH.__data: 0xc8
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__data: 0x4ac
+  __DATA.__data: 0x4b4
+  __DATA.__bss: 0x4018
   __DATA.__common: 0x30
-  __DATA.__bss: 0x3e68
   __DATA_DIRTY.__data: 0x978
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x4690
+  __DATA_DIRTY.__bss: 0x4670
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 22234
+  Functions: 22278
   Symbols:   475
-  CStrings:  5623
+  CStrings:  5659
 
CStrings:
+ "54"
+ "Assertion failed in \"#%{public}s:#%{public}d\": #%{public}s"
+ "Assertion failed in \"{}:{}\": {}"
+ "ChunkedCSRHeader::integrityCheck: CSR offset {} at index {} is less than offset {} at index {}"
+ "ChunkedCSRHeader::integrityCheck: Largest CSR offset {} is larger than the number of rows in the CSR {}."
+ "Found CHECKPOINT record in WAL but no shadow file"
+ "HybridSearch.IntegrityCheckCorruptionErrorSilenced"
+ "InMemChunkedCSRHeader::populateCSRLengthFromOffsets: CSR offset {} at index {} is less than offset {} at index {}"
+ "IntegrityCheck: Mismatch between existence of null column of column '{}' ({}) and null segment ({})."
+ "Predicate contains {} conjunctive expressions, which exceeds the maximum of {}."
+ "WAL file size {} is larger than the corruptWALSizeLimit {}."
+ "catalogSizeMB"
+ "com.apple.HybridSearch.index.errors"
+ "com.apple.hybriddatabase.retokenize.status"
+ "com.apple.hybriddatabase.storage.deletions"
+ "connectionConfigError"
+ "connectionInitializationFailed"
+ "currentLength >= numDeletedRows"
+ "dataFileSizeMB"
+ "databaseInitializationFailed"
+ "deletionPercent"
+ "entry"
+ "errorCode"
+ "errorDescription"
+ "errorDomain"
+ "errorMsg"
+ "fsmFreeSizeMB"
+ "getFlatTupleFailed"
+ "getNextQueryResultFailed"
+ "hnswIndexNotReady"
+ "i == 0 || csrOffsets[i] >= csrOffsets[i - 1]"
+ "metadataSizeMB"
+ "operation"
+ "pagesToVacuum"
+ "prepareStatmentFailed"
+ "queryExecutionFailed"
+ "shadowSizeMB"
+ "topKInputCount"
+ "totalPages"
+ "transactionManager"
+ "valueConversionFailed"
- "49.0.1"
- "Assertion failed in file \"#%{public}s\" on line #%{public}d: #%{public}s"
- "Assertion failed in file \"{}\" on line {}: {}"
- "Mismatch between null segment and null column existance."
- "encountered"
```
