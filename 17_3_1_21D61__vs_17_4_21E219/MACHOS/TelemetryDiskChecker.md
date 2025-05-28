## TelemetryDiskChecker

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker`

```diff

-2461.80.8.0.0
-  __TEXT.__text: 0xb5a8
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x590
+2720.100.117.0.0
+  __TEXT.__text: 0x80b0
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__objc_methlist: 0x368
   __TEXT.__const: 0x58
-  __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0x1f8a
-  __TEXT.__objc_methtype: 0x4cc
-  __TEXT.__cstring: 0x183d
-  __TEXT.__oslogstring: 0x1146
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__unwind_info: 0x2f4
-  __DATA_CONST.__auth_got: 0x370
+  __TEXT.__objc_classname: 0x108
+  __TEXT.__objc_methname: 0x17e6
+  __TEXT.__objc_methtype: 0x389
+  __TEXT.__cstring: 0xf58
+  __TEXT.__oslogstring: 0xcfd
+  __TEXT.__gcc_except_tab: 0x388
+  __TEXT.__unwind_info: 0x1f0
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x580
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x11a0
-  __DATA.__objc_selrefs: 0x850
-  __DATA.__objc_classrefs: 0x110
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x98
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x188
-  __DATA.__bss: 0x30
+  __DATA.__objc_const: 0xf90
+  __DATA.__objc_selrefs: 0x5f0
+  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
-  - /System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
+  - /System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 211
-  Symbols:   168
-  CStrings:  630
+  Functions: 128
+  Symbols:   139
+  CStrings:  442
 
Symbols:
+ _OBJC_CLASS_$_BRCPQLConnection
+ _OBJC_CLASS_$_BRCPackageItem
+ _exit
- _OBJC_CLASS_$_BRCSystemResourcesManager
- _OBJC_CLASS_$_BRCUserDefaults
- _OBJC_CLASS_$_BRDocObjectID
- _OBJC_CLASS_$_BRInodeObjectID
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_PQLConnection
- _OBJC_METACLASS_$_PQLConnection
- ___assert_rtn
- _abc_report_assert_with_signature
- _abc_report_panic_with_signature
- _br_pacer_cancel
- _br_pacer_create
- _br_pacer_pretend_event_handler_fired
- _br_pacer_resume
- _br_pacer_set_event_handler
- _br_pacer_signal
- _br_pacer_signal_at_most_after_min_interval
- _brc_append_system_info_to_message
- _dispatch_async
- _dlerror
- _dlopen
- _dlsym
- _objc_release_x1
- _packageItemsOrderedByPathForFileObjectID
- _sqlite3_bind_parameter_count
- _sqlite3_column_count
- _sqlite3_result_int
- _sqlite3_sql
- _sqlite3_stmt_status
- _stat
- _strlen
- _usleep
CStrings:
+ "SELECT COUNT(*) FROM client_unapplied_table WHERE throttle_state IN (1)"
+ "SELECT item_id, zone_rowid FROM client_items WHERE %@ AND item_state IN (0)"
+ "SELECT item_id, zone_rowid FROM client_items WHERE item_file_id = %@ AND item_state IN (0)"
+ "SELECT si.item_id IS NULL, (SELECT sz.zone_owner = %@ FROM server_zones AS sz WHERE sz.rowid = si.zone_rowid), si.quota_used, si.recursive_child_count, si.shared_children_count, si.shared_alias_count, si.child_count FROM client_items AS ci LEFT JOIN server_items AS si ON (si.item_id = ci.item_id AND si.zone_rowid = ci.zone_rowid) WHERE ci.%@ AND ci.item_state IN (0)"
+ "T@\"NSString\",?,R,C"
+ "[DEBUG] Skipping checksumming package at %@%@"
+ "packageItemsForFileObjectID:order:db:"
- "\x01a"
- "    %@\n"
- " (for statement %@)"
- "%@ has been locked for %f seconds: %@"
- "%@ locked for more than 1 minute %@, aborting..."
- "(ignored by caller)"
- "(null)"
- "(on statement %@)"
- "(passed to caller)"
- "-[BRCPQLConnection _setErrorHandlerWithDBCorruptionHandler:]_block_invoke"
- "-[BRCPQLConnection _setLockedHandler]_block_invoke"
- "-[BRCPQLConnection _shouldFlushWithChangeCount:]"
- "-[BRCPQLConnection _validateIsRunningWithCorrectPersona]"
- "-[BRCPQLConnection attachDBAtPath:as:error:]"
- "-[BRCPQLConnection brc_closeWithError:]"
- "-[BRCPQLConnection brc_close]"
- "-[BRCPQLConnection disableProfilingForQueriesInBlock:]"
- "-[BRCPQLConnection executeWithExpectedIndex:sql:]"
- "-[BRCPQLConnection executeWithSlowStatementRadar:sql:]"
- "-[BRCPQLConnection fetchWithSlowStatementRadar:objectOfClass:sql:]"
- "-[BRCPQLConnection fetchWithSlowStatementRadar:objectWithConstructor:sql:]"
- "-[BRCPQLConnection fetchWithSlowStatementRadar:sql:]"
- "-[BRCPQLConnection setProfilingEnabled:]_block_invoke"
- "-[BRCPQLConnection setProfilingHook:]"
- "-[BRDiskCheckerService _setupDatabaseConnectionFromURL:error:]_block_invoke_3"
- "-[BRDiskCheckerValidateTreeConsistencyOperation _fpfsFileObjectIDWithURL:]"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/core/shared/foundation/BRCPQLConnection.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs_plugins/xpc-services/telemetry-disk-checker/BRDiskCheckerValidateTreeConsistencyOperation.m"
- "/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore"
- "@\"NSString\""
- "@\"br_pacer\""
- "@32@0:8#16@24"
- "@32@0:8@16*24"
- "@32@0:8@16@?24"
- "@32@0:8@?16@24"
- "@40@0:8#16:24@32"
- "@40@0:8#16@24*32"
- "@40@0:8@16#24@32"
- "@40@0:8@16@?24@32"
- "@40@0:8@?16@24*32"
- "@48@0:8#16:24@32*40"
- "ATTACH \"%@\" AS %@"
- "B20@0:8i16"
- "B20@?0@\"PQLConnection\"8i16"
- "B24@0:8^@16"
- "B32@0:8@16*24"
- "B32@0:8@?16@24"
- "B32@?0@\"BRCPQLConnection\"8@\"PQLStatement\"16@\"NSError\"24"
- "B36@0:8@16i24^@28"
- "B40@0:8@16@24^@32"
- "BRCPQLConnection"
- "Can't find packageItemsOrderedByPathForFileObjectIDFPFS in iCloudDriveCore framework"
- "Can't open iCloudDriveCore"
- "Q"
- "SELECT COUNT(*) FROM client_unapplied_table WHERE throttle_state IN (1,26)"
- "SELECT item_id, zone_rowid FROM client_items WHERE %@ AND item_state IN (0, -1)"
- "SELECT item_id, zone_rowid FROM client_items WHERE item_file_id = %@ AND item_state IN (0, -1)"
- "SELECT si.item_id IS NULL, (SELECT sz.zone_owner = %@ FROM server_zones AS sz WHERE sz.rowid = si.zone_rowid), si.quota_used, si.recursive_child_count, si.shared_children_count, si.shared_alias_count, si.child_count FROM client_items AS ci LEFT JOIN server_items AS si ON (si.item_id = ci.item_id AND si.zone_rowid = ci.zone_rowid) WHERE ci.%@ AND ci.item_state IN (0, -1)"
- "Significantly too slow SQL statement: "
- "Sqlite database became corrupted, abort..."
- "T@\"NSString\",&,N,V_assertionPersonaIdentifier"
- "T@?,C,D,N"
- "TB,N"
- "TB,R,N,V_isReadonly"
- "TQ,R,N,V_vmStepsExecuted"
- "UTF8String"
- "[CRIT] %@%@"
- "[CRIT] API MISUSE: you need to an index to use%@"
- "[CRIT] API MISUSE: you need to provide a radar%@"
- "[CRIT] Assertion failed: _batchingPacer%@"
- "[CRIT] Assertion failed: block%@"
- "[CRIT] Assertion failed: fileObjectID.type == BRFileObjectIDTypeNonDocument%@"
- "[CRIT] Can't find packageItemsOrderedByPathForFileObjectIDFPFS in iCloudDriveCore framework :%s%@"
- "[CRIT] Significantly too slow SQL statement ( vm steps: %u  max:%lu ): %s%@"
- "[CRIT] UNREACHABLE: Got really unexpected error: %@%@"
- "[CRIT] UNREACHABLE: Running on the connection with the wrong persona%@"
- "[CRIT] error closing connection %@: %@%@"
- "[DEBUG] Checksumming package at %@%@"
- "[ERROR] %@%@"
- "[ERROR] %s: %s error: %@%@"
- "[ERROR] Failed to stat path %@ for metrics%@"
- "[ERROR] Sqlite failed on %@ with error [%@]%@"
- "[ERROR] Sqlite request %@ failed on %@ with error [%@]%@"
- "[WARNING] %@%@"
- "[WARNING] Can't open iCloudDriveCore : %s%@"
- "[WARNING] Possible slow statement on %@:\n  binds:    %d\n  changes:  %lld\n  vm steps: %d (max: %lu)\n  sql:      %s\n  %@%@"
- "[WARNING] Possible slow statement on %@:\n  binds:    %d\n  columns:  %d\n  rows:     %ld\n  vm steps: %d (max: %lu)\n  sql:      %s\n  %@%@"
- "_assertionPersonaIdentifier"
- "_autovacuumInProgress"
- "_batchingPacer"
- "_changeCount"
- "_changesOverride"
- "_flushImmediately"
- "_flushInterval"
- "_fpfsFileObjectIDWithURL:"
- "_isReadonly"
- "_setErrorHandlerWithDBCorruptionHandler:"
- "_setLockedHandler"
- "_shouldFlushWithChangeCount:"
- "_validateIsRunningWithCorrectPersona"
- "_vmStepsExecuted"
- "appendFormat:"
- "assertOnQueue"
- "assertionPersonaIdentifier"
- "autovacuumIfNeeded"
- "autovacuumableSpaceInBytes"
- "br_currentPersonaID"
- "br_makeNextFlushCheckpoint"
- "brc_closeWithError:"
- "changes"
- "close:"
- "code"
- "com.apple.bird.db.batching"
- "connectedToPowerSource"
- "currentOperationDuration"
- "d"
- "dbAutovacuumBatchSize"
- "dbAutovacuumRatio"
- "dbTraced"
- "defaultsForMangledID:"
- "disableProfilingForQueriesInBlock:"
- "error closing connection %@: %@"
- "execute:"
- "execute:args:"
- "executeRaw:"
- "executeWithErrorHandler:sql:"
- "executeWithExpectedIndex:sql:"
- "executeWithSlowStatementRadar:sql:"
- "explain query plan %@"
- "fetch:args:"
- "fetchObject:sql:args:"
- "fetchObjectOfClass:initializer:sql:"
- "fetchObjectOfClass:initializer:sql:args:"
- "fetchObjectOfClass:sql:"
- "fetchObjectOfClass:sql:args:"
- "fetchWithSlowStatementRadar:objectOfClass:sql:"
- "fetchWithSlowStatementRadar:objectWithConstructor:sql:"
- "fetchWithSlowStatementRadar:sql:"
- "flush"
- "flushToMakeEditsVisibleToIPCReaders"
- "forceBatchStart"
- "iCloudDriveCoreLibrary"
- "incrementalVacuum:"
- "initWithDocID:"
- "initWithFileID:"
- "initWithFormat:"
- "initpackageItemsOrderedByPathForFileObjectIDFPFS"
- "integerValue"
- "isDocumentsItemIDWithSQLiteValue:"
- "isInTransaction"
- "isReadonly"
- "isRootItemIDWithSQLiteValue:"
- "item_doc_id = %llu"
- "item_file_id = %llu"
- "item_id_is_documents"
- "item_id_is_root"
- "length"
- "lockedHandler"
- "manager"
- "needsAutovacuum"
- "packageItemsOrderedByPathForFileObjectIDFPFS"
- "performWithFlags:action:whenFlushed:"
- "plan:\n"
- "pragma page_count"
- "pragma page_size"
- "profilingEnabled"
- "profilingHook"
- "q"
- "q16@0:8"
- "registerFunction:nArgs:handler:"
- "scheduleFlushWithCheckpoint:whenFlushed:"
- "setAssertionPersonaIdentifier:"
- "setCrashIfUsedAfterClose:"
- "setLabel:"
- "setLockedHandler:"
- "setProfilingEnabled:"
- "setProfilingHook:"
- "setSqliteErrorHandler:"
- "setTraced:"
- "setting profiling hook is not supported on %@"
- "setupPragmas"
- "sizeInBytes"
- "sqliteErrorHandler"
- "string"
- "stringByAppendingString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "useBatchingOnTargetQueue:withPolicyHandler:"
- "usePacedBatchingOnTargetQueue:withInterval:changeCount:"
- "v16@?0@\"PQLConnection\"8"
- "v28@0:8B16@?20"
- "v28@?0^{sqlite3_context=}8i16^^{sqlite3_value}20"
- "v32@?0@\"PQLConnection\"8@\"PQLStatement\"16@\"NSError\"24"
- "v32@?0@\"PQLConnection\"8^{sqlite3_stmt=}16Q24"
- "v36@0:8@16d24i32"
- "vmStepsExecuted"

```
