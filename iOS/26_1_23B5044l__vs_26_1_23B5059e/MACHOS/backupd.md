## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2899.40.32.0.0
-  __TEXT.__text: 0x271900
-  __TEXT.__auth_stubs: 0x3370
-  __TEXT.__objc_stubs: 0x29220
+2899.40.40.0.0
+  __TEXT.__text: 0x271b54
+  __TEXT.__auth_stubs: 0x3360
+  __TEXT.__objc_stubs: 0x29200
   __TEXT.__objc_methlist: 0x17784
-  __TEXT.__const: 0x1580
-  __TEXT.__cstring: 0x6f218
-  __TEXT.__objc_methname: 0x37d5e
+  __TEXT.__const: 0x1570
+  __TEXT.__cstring: 0x6f1e1
+  __TEXT.__objc_methname: 0x37d5c
   __TEXT.__constg_swiftt: 0x7cc
   __TEXT.__swift5_typeref: 0xd08
   __TEXT.__swift5_reflstr: 0xe12

   __TEXT.__objc_classname: 0x1fab
   __TEXT.__objc_methtype: 0x64f8
   __TEXT.__swift5_capture: 0x3ec
-  __TEXT.__oslogstring: 0x32b7a
+  __TEXT.__oslogstring: 0x32b48
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc09c
+  __TEXT.__gcc_except_tab: 0xc08c
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x6910
   __TEXT.__eh_frame: 0x1c88
-  __DATA_CONST.__auth_got: 0x19c8
+  __DATA_CONST.__auth_got: 0x19c0
   __DATA_CONST.__got: 0xda0
   __DATA_CONST.__auth_ptr: 0x298
-  __DATA_CONST.__const: 0x83a8
-  __DATA_CONST.__cfstring: 0x1c960
+  __DATA_CONST.__const: 0x83e8
+  __DATA_CONST.__cfstring: 0x1c940
   __DATA_CONST.__objc_classlist: 0xa10
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA.__objc_const: 0x25418
-  __DATA.__objc_selrefs: 0xbf98
+  __DATA.__objc_selrefs: 0xbf90
   __DATA.__objc_ivar: 0x1b34
   __DATA.__objc_data: 0x7000
   __DATA.__data: 0x24d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CA20E31-7582-33D8-9CE2-BC74B80C095F
-  Functions: 9494
-  Symbols:   1344
-  CStrings:  23753
+  UUID: F8CAD71F-B1C7-3166-9CE2-8A4A8889F3E3
+  Functions: 9495
+  Symbols:   1343
+  CStrings:  23754
 
Symbols:
- _random
CStrings:
+ "=quota-calculation= Failed to synchronize file lists when sizing domain %@: %@"
+ "=scheduler= [Off condition after %.1fs] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, passcodeChanged:%d, managerStates:%@, changes:%{public}@"
+ "=scheduler= [Off condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, passcodeChanged:%d, managerStates:%@, changes:%{public}@"
+ "=sync= =domain repair= Failed to add repair domains to pending snapshot database: %@"
+ "=sync= =domain repair= Found domain HMAC to repair %@"
+ "=sync= Added domain %@(%d) with reference %@ into pending snapshot database"
+ "=sync= Consolidated baseRecordID %@ with domain on disk %@"
+ "=sync= Deleting file list for %@ that isn't present in snapshot"
+ "=sync= Encountered fetch errors during file list synchronization: %@"
+ "=sync= Failed to add domains into pending snapshot database: %@"
+ "=sync= Failed to close pending snapshot DB: %@"
+ "=sync= Failed to create pending snapshot database: %@"
+ "=sync= Failed to decompress domain record %@: %@"
+ "=sync= Failed to delete file list database for domain %@: %@"
+ "=sync= Failed to fetch recordID %@: %@"
+ "=sync= Failed to finish batch fetch of domain records: %@"
+ "=sync= Failed to insert domain name into pending snapshot DB: %@"
+ "=sync= Failed to synchronize file lists: %@"
+ "=sync= Fetched domain record %@ for domain %@"
+ "=sync= Fetching domain record ID %@ from reference %@"
+ "=sync= Finished file list synchronization in %.2fs - consolidated:%llu fetched:%llu deleted:%llu"
+ "Enqueued batches (%lld) of total files (%lld), hard links (%llu), total download (%lld). Expected duration: %0.3f s"
+ "MBDriveScript had (%ld) operations, and performed (%ld)"
+ "Restored batches (%lld) of total files (%lld), hard links (%llu) of total %lld bytes"
+ "_operations[%lld] = %@"
+ "mb_enumerateFirstAndLastNObjects:fromIndex:block:"
+ "v24@?0@8Q16"
- "=domain record op= =domain repair= Failed to add repair domains to pending snapshot database: %@"
- "=domain record op= =domain repair= Found domain HMAC to repair %@"
- "=domain record op= Added domain %@(%d) with reference %@ into pending snapshot database"
- "=domain record op= Consolidated baseRecordID %@ with domain on disk %@"
- "=domain record op= Deleting file list for %@ that isn't present in snapshot"
- "=domain record op= Encountered fetch errors during file list synchronization: %@"
- "=domain record op= Failed to add domains into pending snapshot database: %@"
- "=domain record op= Failed to close pending snapshot DB: %@"
- "=domain record op= Failed to create pending snapshot database: %@"
- "=domain record op= Failed to decompress domain record %@: %@"
- "=domain record op= Failed to delete file list database for domain %@: %@"
- "=domain record op= Failed to fetch recordID %@: %@"
- "=domain record op= Failed to finish batch fetch of domain records: %@"
- "=domain record op= Failed to insert domain name into pending snapshot DB: %@"
- "=domain record op= Failed to synchronize file lists: %@"
- "=domain record op= Fetched domain record %@ for domain %@"
- "=domain record op= Fetching domain record ID %@ from reference %@"
- "=domain record op= Finished file list synchronization in %.2fs - consolidated:%llu fetched:%llu deleted:%llu"
- "=scheduler= [Off condition after %.1fs] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, managerStates:%@, changes:%{public}@"
- "=scheduler= [Off condition] state changed, enabled:%d, locked:%d, onPower:%d, onWiFi:%d, onCellular:%d(%d), autoBackupOnCellularEnabled:%d, autoBackupOnCellularAllowedByProvider:%d, managerStates:%@, changes:%{public}@"
- "CacheRefreshTest"
- "Enqueued batches (%lld) of total files (%lld) total download (%lld)"
- "MBDriveScript had (%ld) operations, and performed (%ld):\n%@"
- "Resetting the cache - CacheRefreshTest"
- "Restored batches (%lld) of total files (%lld) of total %lld bytes"
- "exchangeObjectAtIndex:withObjectAtIndex:"
- "mb_shuffle"

```
