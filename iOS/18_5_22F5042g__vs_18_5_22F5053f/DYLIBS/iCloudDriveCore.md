## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3437.120.2.0.0
-  __TEXT.__text: 0x2f0c0c
+3437.120.13.0.1
+  __TEXT.__text: 0x2f0ce0
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x18fbc
+  __TEXT.__objc_methlist: 0x18fec
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x7a2c7
-  __TEXT.__oslogstring: 0x3aea7
+  __TEXT.__cstring: 0x7a38a
+  __TEXT.__oslogstring: 0x3ae00
   __TEXT.__gcc_except_tab: 0x19a68
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9978
+  __TEXT.__unwind_info: 0x9988
   __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x40f8b
+  __TEXT.__objc_methname: 0x4101a
   __TEXT.__objc_methtype: 0x8807
-  __TEXT.__objc_stubs: 0x2c8c0
+  __TEXT.__objc_stubs: 0x2c940
   __DATA_CONST.__got: 0x16f8
   __DATA_CONST.__const: 0x8e08
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc08
+  __DATA_CONST.__objc_selrefs: 0xdc30
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x878
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2958
-  __AUTH_CONST.__cfstring: 0x21f20
+  __AUTH_CONST.__cfstring: 0x21f40
   __AUTH_CONST.__objc_const: 0x3b1c8
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13103
-  Symbols:   15995
-  CStrings:  22594
+  Functions: 13104
+  Symbols:   15996
+  CStrings:  22597
 
CStrings:
+ "-[BRCFSDownloader _cancelJobs:state:cancelError:]"
+ "SELECT throttle_id, download_kind, download_etag, transfer_operation, transfer_stage, app_library_rowid, zone_rowid, throttle_state, transfer_size FROM client_downloads WHERE throttle_id = %lld    AND throttle_state != 0"
+ "SELECT throttle_id, download_kind, download_etag, transfer_operation, transfer_stage, app_library_rowid, zone_rowid, throttle_state, transfer_size FROM client_downloads WHERE throttle_id = %lld AND download_etag = %@   AND throttle_state != 0"
+ "_buildDownloadActiveJobsResultSetForThrottleID:etag:kind:"
+ "_cancelJobs:state:cancelError:"
+ "beforeFirstSyncComponent"
+ "br_isValidContentVersion"
+ "br_isValidStructureVersion"
+ "brc_genericDownloadErrorWithUnderlyingError:"
- "-[BRCFSDownloader _cancelJobs:state:]"
- "-[BRCPendingChangesStream _dbBecameCorrupted:withDescription:]"
- "SELECT throttle_id, download_kind, download_etag, transfer_operation, transfer_stage, app_library_rowid, zone_rowid, throttle_state, transfer_size FROM client_downloads WHERE throttle_id = %lld AND throttle_state != 0"
- "[CRIT] error closing BRCPendingChangesStream DB connection: %@%@"
- "[ERROR] We are in an error scenario, trying to close the DB, but it's busy - let's avoid dealloc it%@"
- "setEnabledTopics:ignoredTopics:opportunisticTopics:nonWakingTopics:"

```
