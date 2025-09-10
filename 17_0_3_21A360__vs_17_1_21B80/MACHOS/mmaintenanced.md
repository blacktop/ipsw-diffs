## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-120.0.0.0.0
-  __TEXT.__text: 0x11f04
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__oslogstring: 0x1298
-  __TEXT.__cstring: 0xdc4
-  __TEXT.__const: 0x4e0
-  __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__unwind_info: 0x654
-  __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0xab8
+127.0.0.0.0
+  __TEXT.__text: 0x1317c
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__init_offsets: 0x4
+  __TEXT.__oslogstring: 0x162b
+  __TEXT.__cstring: 0xf69
+  __TEXT.__const: 0x4e8
+  __TEXT.__gcc_except_tab: 0x728
+  __TEXT.__unwind_info: 0x69c
+  __TEXT.__eh_frame: 0x88
+  __DATA_CONST.__auth_got: 0x530
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0xae0
   __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0x188
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x18
+  __DATA.__common: 0x84
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3DBE09EC-45B4-392C-B51E-CFC14D37F293
-  Functions: 391
-  Symbols:   210
-  CStrings:  271
+  UUID: EA5CF97A-6837-3D63-9D01-C78322AF3D9E
+  Functions: 427
+  Symbols:   217
+  CStrings:  311
 
Symbols:
+ ___cxa_atexit
+ _difftime
+ _sqlite3_bind_null
+ _sqlite3_column_int64
+ _sqlite3_exec
+ _sqlite3_reset
+ _vm_page_mask
+ _vm_page_shift
+ _vm_page_size
- _localtime
- _sqlite3_errmsg
CStrings:
+ "%s: Cannot open database file %s, %{errno}d"
+ "%s: failed to open database %s, rc: %d"
+ "%s: failed to retreive vm.vm_ecc_max_db_pages, using fallback limit of %d"
+ "%s: failed with rc=%d"
+ "%s: sqlite3_step returned %d"
+ "%s: sqlite3_step(stmt_ue_preceded_by_ce_count) returned %d"
+ "Accumulated"
+ "Address"
+ "Bank"
+ "CE"
+ "CEorUE"
+ "CREATE TABLE IF NOT EXISTS ecc_errors_v2 (ID INTEGER PRIMARY KEY,time INT NOT NULL,addr INT NOT NULL,row INT,column INT,bank INT,count INT NOT NULL,correctable INT NOT NULL);"
+ "Column"
+ "CountType"
+ "Database directory doesn't exist."
+ "Epoch"
+ "ErrorCount"
+ "Failed to get total count for correctable=%d epoch=%d "
+ "Failed to get unique addr count for correctable=%d epoch=%d "
+ "Failed to insert error into database for addr %llx"
+ "Failed to remove corrupt database."
+ "INSERT INTO ecc_errors_v2('time','addr','row','column','bank','count','correctable') VALUES(?, ?, ?, ?, ?, ?, ?);"
+ "Notified CoreAnalytics of ECC error -> correctable: %u, preceded_by_correctable: %u, epoch: %u, uniqueness: %u, vendor: %u, count: %u"
+ "One of the prepared statement preparations failed, combined rc: %d"
+ "PRAGMA quick_check"
+ "PrecededByCE"
+ "Received a notification, but EccDatabase is not in a valid state"
+ "Retired database is corrupt.  Removing it."
+ "Row"
+ "SELECT (addr >> ?) as Page, MAX(time) as Time FROM ecc_errors_v2 WHERE correctable=0 GROUP BY Page ORDER BY Time DESC LIMIT ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = 0 AND (addr / ?) = ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? AND time >= ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = ?;"
+ "SELECT COUNT(DISTINCT correctable) FROM ecc_errors_v2 WHERE addr = ?;"
+ "SELECT addr, COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? AND time >= ? GROUP BY addr;"
+ "SELECT addr, COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? GROUP BY addr;"
+ "TimePeriod"
+ "Total"
+ "UE"
+ "Vendor"
+ "com.apple.ecc_error"
+ "database %s is corrupted"
+ "failed to close connection to %s, rc: %d"
+ "failed to recreate database file after deletion, rc: %d"
+ "failed to remove %s, errno: %d"
+ "get_total_count"
+ "get_unique_addr_count"
+ "initialize"
+ "insert"
+ "is_page_retired"
+ "ok"
+ "recreated %s successfully"
+ "regenerate_retired_pages"
+ "regenerated the retired page list, rc=%d"
+ "update_persistent_retirement_limit"
+ "vm.vm_ecc_max_db_pages"
+ "wrote page %llu"
- "CREATE TABLE IF NOT EXISTS ECC_ERRORS (ID INTEGER PRIMARY KEY, ADDR HEX NOT NULL, YEAR INT NOT NULL, MONTH INT NOT NULL, DAY INT NOT NULL, HOUR INT NOT NULL, MINUTE INT NOT NULL, IN_PANIC_PATH INT, IS_CPU_REPORTED INT, CORRECTABLE INT, RETIRED INT, CE_COUNT INT, num_occurrences INT NOT NULL, version INT NOT NULL);"
- "Cannot open database file %s, %{errno}d"
- "Database directory doesn't exist"
- "INSERT INTO ECC_ERRORS('ADDR', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'IN_PANIC_PATH', 'IS_CPU_REPORTED', 'CORRECTABLE', 'RETIRED', 'CE_COUNT', 'num_occurrences', 'version') VALUES( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? );"
- "Notified CoreAnalytics error at addr %llx..."
- "SELECT * FROM ECC_ERRORS WHERE ID = ?;"
- "SELECT MAX(ID) FROM ECC_ERRORS WHERE ADDR = ?;"
- "a+"
- "addr"
- "ce_count"
- "com.apple.memory.error"
- "is_correctable"
- "is_cpu_reported"
- "is_panic_path"
- "is_retired"
- "num_occurrences"
- "sqlite err: %s"

```
