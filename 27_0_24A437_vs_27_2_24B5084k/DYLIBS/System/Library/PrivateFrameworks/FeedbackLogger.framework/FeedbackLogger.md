## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3600.56.26.11.2
-  __TEXT.__text: 0x1cb2c
-  __TEXT.__objc_methlist: 0x11fc
+3605.21.1.1.1
+  __TEXT.__text: 0x1d0f0
+  __TEXT.__objc_methlist: 0x124c
   __TEXT.__const: 0x14c0
   __TEXT.__swift5_typeref: 0x4e7
   __TEXT.__swift5_fieldmd: 0x3f4
   __TEXT.__constg_swiftt: 0x288
-  __TEXT.__cstring: 0x2081
+  __TEXT.__cstring: 0x2079
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_reflstr: 0x2fd
   __TEXT.__swift5_capture: 0xec
-  __TEXT.__oslogstring: 0x1dd7
+  __TEXT.__oslogstring: 0x2027
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__gcc_except_tab: 0x2a4
-  __TEXT.__unwind_info: 0xc68
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0xc88
   __TEXT.__eh_frame: 0x538
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__const: 0x478
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc88
+  __DATA_CONST.__objc_selrefs: 0xcc0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x1a60
+  __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x8a8
   __AUTH.__objc_data: 0x168
   __AUTH.__data: 0x3d0
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x558
   __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x450

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 929
-  Symbols:   1329
-  CStrings:  344
+  Functions: 935
+  Symbols:   1352
+  CStrings:  352
 
Symbols:
+ -[FLLogger _cancelTerminationWatcher]
+ -[FLLogger _handleTermination]
+ -[FLLogger _setupTerminationWatcher]
+ -[FLLogger _tryRelinquishForTerminationWithAttemptsRemaining:]
+ -[FLLogger setTerminationWatcher:]
+ -[FLLogger terminationWatcher]
+ -[FLSQLitePersistence(BatchManager) firstPayloadForBatch:]
+ -[FLSQLitePersistence(UploadManager) doUploadHousekeeping:]
+ GCC_except_table109
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table192
+ GCC_except_table261
+ GCC_except_table286
+ GCC_except_table360
+ GCC_except_table49
+ GCC_except_table59
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table87
+ GCC_except_table91
+ GCC_except_table94
+ _OBJC_IVAR_$_FLLogger._terminating
+ _OBJC_IVAR_$_FLLogger._terminationWatcher
+ _OBJC_IVAR_$_FLLogger._terminationWatcherResolved
+ ___36-[FLLogger _setupTerminationWatcher]_block_invoke
+ ___62-[FLLogger _tryRelinquishForTerminationWithAttemptsRemaining:]_block_invoke
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ __dispatch_source_type_signal
+ _objc_msgSend$_cancelTerminationWatcher
+ _objc_msgSend$_handleTermination
+ _objc_msgSend$_setupTerminationWatcher
+ _objc_msgSend$_tryRelinquishForTerminationWithAttemptsRemaining:
+ _objc_msgSend$firstPayloadForBatch:
+ _objc_msgSend$setWriteTransactionTTL:
+ _objc_msgSend$watchdogQueue
+ _os_unfair_lock_trylock
- -[FLSQLitePersistence(UploadManager) doUploadHousekeeping]
- GCC_except_table105
- GCC_except_table122
- GCC_except_table183
- GCC_except_table252
- GCC_except_table277
- GCC_except_table351
- GCC_except_table47
- GCC_except_table57
- GCC_except_table66
- GCC_except_table78
- GCC_except_table83
- GCC_except_table89
- GCC_except_table92
- _MGCopyAnswer
CStrings:
+ "Gave up relinquishing the write transaction after SIGTERM: lock held throughout. Falling back to the TTL."
+ "Got SIGTERM while holding a write transaction; relinquishing it now."
+ "Got SIGTERM with no write transaction held; later writes get the shortened TTL."
+ "Installed SIGTERM watcher (dispatch source only; signal disposition untouched)."
+ "Managed process: not installing a SIGTERM watcher (RBSAssertion path)."
+ "SELECT payload FROM records WHERE batchId=? ORDER BY rowId ASC LIMIT 1;"
+ "SELECT s.batchId, s.timestampRefId, COALESCE(sum(length(r.payload)), 0), s.status, s.processedAttempts, s.dateCreated, s.dateUploaded, s.dateLastProcessed, COUNT(DISTINCT(r.rowId)) FROM batchStatus s LEFT JOIN records r ON s.batchId = r.batchId WHERE s.batchId=? GROUP BY s.batchId;"
+ "SIGTERM watcher fired in a managed process; ignoring."
+ "SQLite first payload read for batch (%s) failed: %d"
+ "Write arrived after SIGTERM; not re-punting the write transaction TTL deadline."
- "RegulatoryModelNumber"
- "SELECT s.batchId, s.timestampRefId, COALESCE(sum(length(r.payload)), 0), s.status, s.processedAttempts, s.dateCreated, s.dateUploaded, s.dateLastProcessed, COUNT(DISTINCT(r.rowId)), first_value(r.payload) OVER (ORDER BY r.rowId) FROM batchStatus s LEFT JOIN records r ON s.batchId = r.batchId WHERE s.batchId=? GROUP BY s.batchId;"
```
