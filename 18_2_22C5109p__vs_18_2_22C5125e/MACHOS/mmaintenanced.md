## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-158.60.1.0.0
-  __TEXT.__text: 0x15d44
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x1154
-  __TEXT.__oslogstring: 0x1a93
-  __TEXT.__cstring: 0x1178
-  __TEXT.__gcc_except_tab: 0x71c
-  __TEXT.__swift5_typeref: 0x64
+158.60.3.0.0
+  __TEXT.__text: 0x1875c
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__init_offsets: 0x8
+  __TEXT.__const: 0x1184
+  __TEXT.__oslogstring: 0x20c3
+  __TEXT.__cstring: 0x1718
+  __TEXT.__gcc_except_tab: 0x748
   __TEXT.__objc_methname: 0xe9
+  __TEXT.__swift5_typeref: 0x64
   __TEXT.__swift5_capture: 0x78
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x758
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__eh_frame: 0x208
-  __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__const: 0xd80
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
   __DATA.__data: 0xeb0
-  __DATA.__bss: 0x40
-  __DATA.__common: 0x38
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x40
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 448
-  Symbols:   399
-  CStrings:  325
+  Functions: 504
+  Symbols:   406
+  CStrings:  412
 
Symbols:
+ ___cxa_guard_abort
+ __dispatch_source_type_mach_recv
+ __os_assumes_log
+ _bootstrap_check_in
+ _mach_msg_server_once
+ _objc_release_x8
+ _objc_retain_x20
+ _task_get_special_port
- _objc_retain_x27
CStrings:
+ "%!l(MISSING)lx\n"
+ "%!s(MISSING): Cannot open database file %!s(MISSING), errno %!d(MISSING)"
+ "%!s(MISSING): failed to open database %!s(MISSING), rc: %!d(MISSING)"
+ "%!s(MISSING): failed to retrieve vm.vm_ecc_max_db_pages, using fallback limit of %!d(MISSING)"
+ "%!s(MISSING): failed with rc=%!d(MISSING)"
+ "%!s(MISSING): sqlite3_step returned %!d(MISSING)"
+ "%!s(MISSING): sqlite3_step(stmt_ue_preceded_by_ce_count) returned %!d(MISSING)"
+ "Accumulated"
+ "Address"
+ "Bank"
+ "CE"
+ "CEorUE"
+ "CFStringCreateWithCString failed"
+ "CREATE TABLE IF NOT EXISTS ecc_errors_v2 (ID INTEGER PRIMARY KEY,time INT NOT NULL,addr INT NOT NULL,row INT,column INT,bank INT,count INT NOT NULL,correctable INT NOT NULL);"
+ "Column"
+ "CountType"
+ "DELETE FROM ecc_errors_v2 WHERE (addr >> ?) = ?;"
+ "Database directory doesn't exist."
+ "Epoch"
+ "ErrorCount"
+ "Failed to get total count for correctable=%!d(MISSING) epoch=%!d(MISSING) "
+ "Failed to get unique addr count for correctable=%!d(MISSING) epoch=%!d(MISSING) "
+ "Failed to insert error into database for addr %!l(MISSING)lx"
+ "Failed to log error, message not from kernel: audit_pid %!d(MISSING)"
+ "Failed to remove address %!l(MISSING)lx from database"
+ "Failed to set context for inbound notifications on the mach port"
+ "INSERT INTO ecc_errors_v2('time','addr','row','column','bank','count','correctable') VALUES(?, ?, ?, ?, ?, ?, ?);"
+ "IODeviceTree:/chosen"
+ "Incorrect valueRef's length"
+ "Initialiazing EccDatabase..."
+ "Initializing Memory Error MIG server..."
+ "Notified CoreAnalytics of ECC error -> correctable: %!u(MISSING), preceded_by_correctable: %!u(MISSING), epoch: %!u(MISSING), uniqueness: %!u(MISSING), vendor: %!u(MISSING), count: %!u(MISSING)"
+ "Notified CoreAnalytics of MCC error: status(%!x(MISSING)) amcc(%!x(MISSING)) plane(%!x(MISSING)) bank(%!x(MISSING)) way(%!x(MISSING)) index(%!x(MISSING)) bit_off_cl(%!x(MISSING)) bit_off_within_hcl(%!x(MISSING)) single_bit(%!u(MISSING)) multi_bit(%!u(MISSING))"
+ "One of the prepared statement preparations failed, combined rc: %!d(MISSING)"
+ "PRAGMA quick_check"
+ "PrecededByCE"
+ "Received a notification, but EccDatabase is not in a valid state"
+ "Received test event for addr %!l(MISSING)lx, ignoring"
+ "Retired database is corrupt. Regenerating it."
+ "Row"
+ "SELECT (addr >> ?) as Page, MAX(time) as Time FROM ecc_errors_v2 WHERE correctable=0 GROUP BY Page ORDER BY Time DESC LIMIT ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = 0 AND (addr >> ?) = ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = ? AND time >= ?;"
+ "SELECT COUNT(*) FROM ecc_errors_v2 WHERE correctable = ?;"
+ "SELECT COUNT(DISTINCT correctable) FROM ecc_errors_v2 WHERE addr = ?;"
+ "SELECT DISTINCT addr FROM ecc_errors_v2 WHERE correctable = ? AND time >= ?;"
+ "SELECT DISTINCT addr FROM ecc_errors_v2 WHERE correctable = ?;"
+ "TimePeriod"
+ "Total"
+ "UE"
+ "Unable to open iodevicetree to read %!s(MISSING)"
+ "Unknown ECC event version %!u(MISSING)\n"
+ "Vendor"
+ "^v8@?0"
+ "amcc"
+ "bank"
+ "bit_off_cl"
+ "bit_off_within_hcl"
+ "com.apple.ecc_error"
+ "com.apple.mcc.error"
+ "com.apple.memory-maintenance.report-ecc-status"
+ "com.apple.mmaintenanced.server"
+ "database %!s(MISSING) is corrupted"
+ "dram-ecc"
+ "dram-vendor-id"
+ "failed to close connection to %!s(MISSING), rc: %!d(MISSING)"
+ "failed to recreate database file after deletion, rc: %!d(MISSING)"
+ "failed to remove %!s(MISSING), errno: %!d(MISSING)"
+ "get_total_count"
+ "get_unique_addr_count"
+ "index"
+ "initialize"
+ "insert"
+ "is_page_retired"
+ "multi_bit"
+ "ok"
+ "plane"
+ "recreated %!s(MISSING) successfully"
+ "regenerate_retired_pages"
+ "regenerated the retired page list, rc=%!d(MISSING)"
+ "remove_addr"
+ "single_bit"
+ "status"
+ "update_persistent_retirement_limit"
+ "vm.vm_ecc_max_db_pages"
+ "way"
+ "wrote page %!l(MISSING)lu"

```
