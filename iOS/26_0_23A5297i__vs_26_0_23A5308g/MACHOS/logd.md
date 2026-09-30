## logd

> `/usr/libexec/logd`

```diff

-1815.0.12.0.0
-  __TEXT.__text: 0x27740
-  __TEXT.__auth_stubs: 0x1b20
+1815.0.16.0.0
+  __TEXT.__text: 0x268e0
+  __TEXT.__auth_stubs: 0x19d0
   __TEXT.__delay_helper: 0x110
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x4d1b
+  __TEXT.__cstring: 0x4622
   __TEXT.__objc_methname: 0x4ee
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methtype: 0x10
-  __TEXT.__unwind_info: 0x6c8
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0xd98
+  __DATA_CONST.__auth_got: 0xcf0
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2138
+  __DATA_CONST.__const: 0x2078
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_nlclslist: 0x10

   __DATA.__data: 0x1d24
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xef18
+  __DATA.__bss: 0xeae8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6001077F-9546-3B7F-B798-0C49D52ACF72
-  Functions: 514
-  Symbols:   492
-  CStrings:  669
+  UUID: 28591BCC-F44E-3E42-9F1B-6307439B80CE
+  Functions: 506
+  Symbols:   471
+  CStrings:  645
 
Symbols:
- __os_feature_enabled_impl
- __sqlite3_db_truncate
- __sqlite3_maintain_load_factor
- _cc_clear
- _ccdigest
- _ccsha256_di
- _sqlite3_bind_blob
- _sqlite3_bind_int
- _sqlite3_bind_int64
- _sqlite3_close_v2
- _sqlite3_column_int
- _sqlite3_column_int64
- _sqlite3_errmsg
- _sqlite3_exec
- _sqlite3_extended_errcode
- _sqlite3_finalize
- _sqlite3_free
- _sqlite3_last_insert_rowid
- _sqlite3_open_v2
- _sqlite3_prepare_v2
- _sqlite3_step
CStrings:
+ "TTL Compaction: Private IOV Length %lu is less than range length %hu"
+ "TTL Compaction: Private IOV Length was bad: %lu"
+ "TTL Compaction: Private data range would have read OOB: %p + %hu - %lu > %p + %lu"
+ "TTL Compaction: Public data would overwrite chunk: %hu + %hu"
+ "TTL Compaction: Range length %hu overflew private offset: %hu"
+ "TTL Compaction: privacy offset overflow: %lu"
+ "TTL Compaction: range requested %hu greater than max chunk size"
+ "TTL Compaction: tracepoint hit overflow adding %hu to %hu"
- "%s/logdata.statistics.0.db"
- "BEGIN TRANSACTION;"
- "END TRANSACTION;"
- "ERROR: No file records found."
- "ERROR: No rows found."
- "Failed to close sql database with %d : %s"
- "Failed to create sql table with %d: %s. Closing database..."
- "Failed to create/open sql database with %d : %s"
- "Failed to get page count: %s\n"
- "INSERT INTO file_info(book,time_stamp,file_id,time_covered,overall_total) VALUES (?, ?, ?, ?, ?);"
- "INSERT INTO process_info(book,process_name_hash,file_id,client_total) VALUES (?, ?, ?, ?);"
- "Libtrace"
- "PRAGMA page_count;"
- "PRAGMA user_version = 1;PRAGMA locking_mode = NORMAL;PRAGMA auto_vacuum  = FULL;PRAGMA foreign_keys = ON;PRAGMA journal_mode = WAL;PRAGMA page_size = 4096;PRAGMA cache_spill = 1;CREATE TABLE IF NOT EXISTS file_info(id INTEGER PRIMARY KEY AUTOINCREMENT,file_id INTEGER NOT NULL,book INTEGER NOT NULL,time_stamp INTEGER NOT NULL,time_covered INTEGER NOT NULL DEFAULT 0,overall_total INTEGER NOT NULL DEFAULT 0);CREATE TABLE IF NOT EXISTS process_info(id INTEGER PRIMARY KEY AUTOINCREMENT,file_id INTEGER NOT NULL,book INTEGER NOT NULL,process_name_hash BLOB NOT NULL,client_total INTEGER NOT NULL DEFAULT 0,FOREIGN KEY(file_id) REFERENCES file_info(id) ON DELETE CASCADE);CREATE INDEX IF NOT EXISTS book_idx ON file_info(book);CREATE INDEX IF NOT EXISTS book_idx ON process_info(book);CREATE INDEX IF NOT EXISTS process_name_hash_idx ON process_info(process_name_hash);"
- "ROLLBACK;"
- "ROLLING BACK %d, %s"
- "SELECT SUM(client_total) FROM (SELECT client_total FROM process_info WHERE process_name_hash = ? AND book = ? ORDER BY file_id DESC LIMIT ?) AS last_n_rows;"
- "SELECT SUM(time_covered), SUM(overall_total) FROM (SELECT overall_total, time_covered FROM file_info WHERE book = ? ORDER BY id DESC LIMIT ?) AS last_n_rows;"
- "logd_multiple_file_quarantines"
- "logd_sql_stats_database"
- "sqlite3_bind_blob failed: %d"
- "sqlite3_bind_int failed: %d"
- "sqlite3_bind_int64 failed: %d"
- "sqlite3_bind_int64 for file_total=%llu failed: %d"
- "sqlite3_bind_int64 for row_id=%lld failed: %d"
- "sqlite3_bind_int64 for time=%lu failed: %d"
- "sqlite3_bind_int64 for time_covered=%lu failed: %d"
- "sqlite3_bind_text for book=%d failed: %d"
- "sqlite3_bind_text for fileid=%llu failed: %d"
- "sqlite3_prepare(insert) for %s failed: %d, %s"
- "sqlite3_prepare(select) for %s failed: %d, %s"
- "sqlite3_step failed for %s with %d, %s"

```
