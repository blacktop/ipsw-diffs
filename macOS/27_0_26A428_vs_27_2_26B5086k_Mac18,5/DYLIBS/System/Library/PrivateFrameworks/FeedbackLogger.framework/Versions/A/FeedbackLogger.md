## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/Versions/A/FeedbackLogger`

```diff

-3600.56.26.14.1
-  __TEXT.__text: 0x1b8c8
-  __TEXT.__objc_methlist: 0x11fc
+3605.21.1.4.1
+  __TEXT.__text: 0x1beb8
+  __TEXT.__objc_methlist: 0x124c
   __TEXT.__const: 0x1420
   __TEXT.__swift5_typeref: 0x449
   __TEXT.__swift5_fieldmd: 0x3f4
   __TEXT.__constg_swiftt: 0x288
-  __TEXT.__cstring: 0x2081
+  __TEXT.__cstring: 0x2079
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_reflstr: 0x2fd
   __TEXT.__swift5_capture: 0x84
-  __TEXT.__oslogstring: 0x1c34
+  __TEXT.__oslogstring: 0x1e84
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__unwind_info: 0xc00
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__unwind_info: 0xc20
   __TEXT.__eh_frame: 0x538
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc50
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__const: 0xa68
+  __DATA_CONST.__got: 0x208
+  __AUTH_CONST.__const: 0xa98
   __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x1a60
+  __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x670
   __AUTH.__objc_data: 0x168
   __AUTH.__data: 0x3d0
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x508
   __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x450

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 911
-  Symbols:   1281
-  CStrings:  338
+  Functions: 917
+  Symbols:   1304
+  CStrings:  346
 
Symbols:
+ -[FLLogger _cancelTerminationWatcher]
+ -[FLLogger _handleTermination]
+ -[FLLogger _setupTerminationWatcher]
+ -[FLLogger _tryRelinquishForTerminationWithAttemptsRemaining:]
+ -[FLLogger setTerminationWatcher:]
+ -[FLLogger terminationWatcher]
+ -[FLSQLitePersistence(BatchManager) firstPayloadForBatch:]
+ -[FLSQLitePersistence(UploadManager) doUploadHousekeeping:]
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table115
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table223
+ GCC_except_table292
+ GCC_except_table317
+ GCC_except_table391
+ GCC_except_table49
+ GCC_except_table65
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table88
+ GCC_except_table94
+ OBJC_IVAR_$_FLLogger._terminating
+ OBJC_IVAR_$_FLLogger._terminationWatcher
+ OBJC_IVAR_$_FLLogger._terminationWatcherResolved
+ ___36-[FLLogger _setupTerminationWatcher]_block_invoke
+ ___62-[FLLogger _tryRelinquishForTerminationWithAttemptsRemaining:]_block_invoke
+ ___block_descriptor_48_e8_32w_e5_v8?0l
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
- GCC_except_table113
- GCC_except_table130
- GCC_except_table134
- GCC_except_table153
- GCC_except_table214
- GCC_except_table283
- GCC_except_table308
- GCC_except_table382
- GCC_except_table47
- GCC_except_table63
- GCC_except_table76
- GCC_except_table82
- GCC_except_table86
- GCC_except_table92
- GCC_except_table99
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
