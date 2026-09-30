## logd

> `/usr/libexec/logd`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0x241bc
-  __TEXT.__auth_stubs: 0x1900
+1815.0.0.0.0
+  __TEXT.__text: 0x27450
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__delay_helper: 0x110
   __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x3c6b
+  __TEXT.__objc_methlist: 0x44
+  __TEXT.__const: 0x2d0
+  __TEXT.__cstring: 0x4d56
   __TEXT.__objc_methname: 0x4ee
-  __TEXT.__objc_classname: 0x14
+  __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__auth_got: 0xd88
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1f48
-  __DATA_CONST.__cfstring: 0x580
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_nlclslist: 0x8
+  __DATA_CONST.__const: 0x2160
+  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x90
+  __DATA.__objc_const: 0x120
   __DATA.__objc_selrefs: 0x1f0
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1ccd
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x1d24
   __DATA.__os_assumes_log: 0x8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xca90
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0xdf18
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0A7D40F9-0C37-3ED1-8510-9A53362A3E42
-  Functions: 484
-  Symbols:   456
-  CStrings:  593
+  UUID: EC487E7E-3EFB-3BDC-9928-513EF97FA899
+  Functions: 512
+  Symbols:   490
+  CStrings:  676
 
Symbols:
+ _RTLogBufferCheckStatus
+ _RTLogBufferGetResource
+ _RTLogRingBufferIterateFrom
+ _RTLogRingBufferJoinManaged
+ __os_feature_enabled_impl
+ __os_object_alloc
+ __os_trace_calloc_typed
+ __os_trace_malloc_typed
+ __os_trace_realloc_typed
+ __os_trace_zalloc_typed
+ __sqlite3_db_truncate
+ __sqlite3_maintain_load_factor
+ __xpc_error_connection_invalid
+ __xpc_type_int64
+ _cc_clear
+ _ccdigest
+ _ccsha256_di
+ _dlopen
+ _mach_error_string
+ _os_variant_has_factory_content
+ _proc_name
+ _sqlite3_bind_blob
+ _sqlite3_bind_int
+ _sqlite3_bind_int64
+ _sqlite3_close_v2
+ _sqlite3_column_int
+ _sqlite3_column_int64
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_extended_errcode
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_last_insert_rowid
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_step
+ _xpc_copy_description
+ _xpc_dictionary_copy_mach_send
+ _xpc_int64_get_value
- __Znwm
- __os_trace_calloc
- __os_trace_malloc
- __os_trace_realloc
- __os_trace_zalloc
CStrings:
+ "%s/logdata.statistics.0.db"
+ "%s[%d] dropped %u %s events"
+ "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "All logs erased (peer:%s) (mask:%llx)"
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]{?=(?=@@)b1}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
+ "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]{?=(?=^{logd_realtime_client_s}^{firehose_client_s})b1}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BsS{os_unfair_lock_s=I}CB[0c]}8"
+ "BEGIN TRANSACTION;"
+ "BUG IN LIBTRACE: Failed to create sql table"
+ "Could not fetch os osenvironment sysctl: %d"
+ "DefaultProcessQuarantineLimit"
+ "END TRANSACTION;"
+ "ERROR: No file records found."
+ "ERROR: No rows found."
+ "Failed to close sql database with %d : %s"
+ "Failed to create dispatch source."
+ "Failed to create sql table with %d: %s"
+ "Failed to create/open sql database with %d : %s"
+ "Failed to deallocate shared memory: %s"
+ "Failed to find disconnected client with pid %d in the list of realtime clients"
+ "Failed to get page count: %s\n"
+ "INSERT INTO file_info(book,time_stamp,file_id,time_covered,overall_total) VALUES (?, ?, ?, ?, ?);"
+ "INSERT INTO process_info(book,process_name_hash,file_id,client_total) VALUES (?, ?, ?, ?);"
+ "Libtrace"
+ "MaxProcessQuarantineLimit"
+ "OSLogDarwin_C.c"
+ "OS_logd_realtime_client"
+ "PRAGMA page_count;"
+ "PRAGMA user_version = 1;PRAGMA locking_mode = NORMAL;PRAGMA auto_vacuum  = FULL;PRAGMA foreign_keys = ON;PRAGMA journal_mode = WAL;PRAGMA page_size = 4096;PRAGMA cache_spill = 1;CREATE TABLE IF NOT EXISTS file_info(id INTEGER PRIMARY KEY AUTOINCREMENT,file_id INTEGER NOT NULL,book INTEGER NOT NULL,time_stamp INTEGER NOT NULL,time_covered INTEGER NOT NULL DEFAULT 0,overall_total INTEGER NOT NULL DEFAULT 0);CREATE TABLE IF NOT EXISTS process_info(id INTEGER PRIMARY KEY AUTOINCREMENT,file_id INTEGER NOT NULL,book INTEGER NOT NULL,process_name_hash BLOB NOT NULL,client_total INTEGER NOT NULL DEFAULT 0,FOREIGN KEY(file_id) REFERENCES file_info(id) ON DELETE CASCADE);CREATE INDEX IF NOT EXISTS book_idx ON file_info(book);CREATE INDEX IF NOT EXISTS book_idx ON process_info(book);CREATE INDEX IF NOT EXISTS process_name_hash_idx ON process_info(process_name_hash);"
+ "Quarantined: %s"
+ "ROLLBACK;"
+ "ROLLING BACK %d, %s"
+ "SELECT SUM(client_total) FROM (SELECT client_total FROM process_info WHERE process_name_hash = ? AND book = ? ORDER BY file_id DESC LIMIT ?) AS last_n_rows;"
+ "SELECT SUM(time_covered), SUM(overall_total) FROM (SELECT overall_total, time_covered FROM file_info WHERE book = ? ORDER BY id DESC LIMIT ?) AS last_n_rows;"
+ "Shared memory cleanup failed for client %d"
+ "Shared memory size is invalid"
+ "Successfully wrote preferences plist: %s"
+ "Timer canceled. Cleaning up...\n"
+ "Unable to create realtime ring resource is null"
+ "Unable to create realtime ring size is null"
+ "Unable to write new preferences plist: %s Error: %s (%d)"
+ "_client_lookup_subsystem metadata is null"
+ "_client_queue == NULL"
+ "cannot map shared memory for realtime client"
+ "client %s:%d is deallocating"
+ "com.apple.logd.realtime"
+ "com.apple.logd.realtime.queue"
+ "debug"
+ "default"
+ "error and fault"
+ "hw.osenvironment"
+ "info"
+ "logd_multiple_file_quarantines"
+ "logd_realtime.c"
+ "logd_realtime_start_listener"
+ "logd_sql_stats_database"
+ "metadata"
+ "realtime client [%s:%d] was added"
+ "realtime client buffer is not valid"
+ "realtime client buffer size is not valid"
+ "realtime client ring buffer join failed"
+ "realtime listener: started"
+ "realtime: connection interrupted"
+ "realtime: connection invalid"
+ "realtime: failed to create service"
+ "realtime: unknown error"
+ "realtime: unknown error '%s'"
+ "rt_message_type"
+ "rt_shmem_descriptor"
+ "rt_shmem_size"
+ "signpost"
+ "simulated"
+ "simulated    : 1\n"
+ "sqlite3_bind_blob failed: %d"
+ "sqlite3_bind_int failed: %d"
+ "sqlite3_bind_int64 failed: %d"
+ "sqlite3_bind_int64 for file_total=%llu failed: %d"
+ "sqlite3_bind_int64 for row_id=%lld failed: %d"
+ "sqlite3_bind_int64 for time=%lu failed: %d"
+ "sqlite3_bind_int64 for time_covered=%lu failed: %d"
+ "sqlite3_bind_text for book=%d failed: %d"
+ "sqlite3_bind_text for fileid=%llu failed: %d"
+ "sqlite3_prepare(insert) for %s failed: %d, %s"
+ "sqlite3_prepare(select) for %s failed: %d, %s"
+ "sqlite3_step failed for %s with %d, %s"
+ "starting realtime listener"
+ "time covered : %zu\n"
+ "v16@?0^{logd_book_s=^?*C@QQqqAqiiQQBi[4q]QQc}8"
- "All logs erased (mask:%llx)"
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]@^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BS{os_unfair_lock_s=I}CB[0c]}8"
- "B16@?0^{firehose_client_context_s={?=^{firehose_client_context_s}^^{firehose_client_context_s}}{?=^{firehose_subsystem_entry_s}^^{firehose_subsystem_entry_s}}[16C][16C]^{firehose_client_s}^{tracev3_buffer_uuidinfo_s}^{os_trace_uuid_set_s}[5{logd_stats_s=Q}]BS{os_unfair_lock_s=I}CB[0c]}8"
- "time covered : %llu\n"
- "v16@?0^{logd_book_s=^?*@QQqqAqiiQQBi[4q]QQ}8"

```
