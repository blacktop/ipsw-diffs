## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-2720.120.29.0.0
-  __TEXT.__text: 0x329e20
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0x1748c
+2720.140.11.0.0
+  __TEXT.__text: 0x329fd8
+  __TEXT.__auth_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0x174bc
   __TEXT.__const: 0x3e0
-  __TEXT.__cstring: 0x7ca18
-  __TEXT.__oslogstring: 0x438d3
-  __TEXT.__gcc_except_tab: 0x1804c
+  __TEXT.__cstring: 0x7ca32
+  __TEXT.__oslogstring: 0x43923
+  __TEXT.__gcc_except_tab: 0x1801c
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x92a4
+  __TEXT.__unwind_info: 0x929c
   __TEXT.__objc_classname: 0x23ad
-  __TEXT.__objc_methname: 0x3e07b
+  __TEXT.__objc_methname: 0x3e09b
   __TEXT.__objc_methtype: 0x7efb
-  __TEXT.__objc_stubs: 0x2afe0
+  __TEXT.__objc_stubs: 0x2b000
   __DATA_CONST.__got: 0xb88
   __DATA_CONST.__const: 0x8b40
   __DATA_CONST.__objc_classlist: 0x8f0
-  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36048
-  __DATA_CONST.__objc_selrefs: 0xd5c8
+  __DATA_CONST.__objc_const: 0x36058
+  __DATA_CONST.__objc_selrefs: 0xd5e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xd88
   __DATA_CONST.__objc_superrefs: 0x818
   __DATA_CONST.__objc_arraydata: 0xd28
   __AUTH_CONST.__const: 0x2508
-  __AUTH_CONST.__objc_const: 0x6dc8
-  __AUTH_CONST.__cfstring: 0x20460
+  __AUTH_CONST.__objc_const: 0x6e08
+  __AUTH_CONST.__cfstring: 0x204e0
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH_CONST.__auth_got: 0xea0
   __AUTH.__objc_data: 0x24e0
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x1f88

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14406
-  Symbols:   42975
-  CStrings:  23060
+  Functions: 14410
+  Symbols:   42984
+  CStrings:  23072
 
Symbols:
+ -[BRCAccountHandler _shouldResetLocalData:]
+ -[BRCAccountSession _handleUnloadedZones:]
+ -[BRCUserDefaults handleUnloadedZones]
+ -[NSMutableIndexSet(BRCZoneRowID) addZoneRowID:]
+ -[NSMutableIndexSet(BRCZoneRowID) removeZoneRowID:]
+ GCC_except_table163
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table69
+ _BRCGetAccountDSIDForMobileDocsRoot.cold.1
+ __OBJC_$_CATEGORY_NSMutableIndexSet_$_BRCZoneRowID
+ __OBJC_$_INSTANCE_METHODS_NSMutableIndexSet(BRCZoneRowID)
+ ___112-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke.260
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.262
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.262.cold.1
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.264
+ ___42-[BRCAccountSession _handleUnloadedZones:]_block_invoke
+ ___42-[BRCAccountSession _handleUnloadedZones:]_block_invoke_2
+ ___42-[BRCAccountSession _handleUnloadedZones:]_block_invoke_2.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.230
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.230.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.230.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.230.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.230.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.237
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.237.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.240
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.260
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.260.cold.1
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.265
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.265.cold.1
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.276
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.277
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.269
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.269.cold.1
+ ___block_literal_global.15
+ ___block_literal_global.239
+ ___block_literal_global.261
+ ___block_literal_global.295
+ ___block_literal_global.374
+ ___block_literal_global.740
+ ___block_literal_global.748
+ _objc_msgSend$_handleUnloadedZones:
+ _objc_msgSend$_shouldResetLocalData:
+ _objc_msgSend$addZoneRowID:
+ _objc_msgSend$br_safeFileSystemRepresentation
+ _objc_msgSend$handleUnloadedZones
+ _objc_msgSend$removeZoneRowID:
- -[BRCFSUploader recoverAndReportMissingJobs].cold.3
- -[CKRecord(BRCSerializationAdditions) deserializeFilename:basename:bounceno:extension:userInfo:error:].cold.3
- -[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]
- GCC_except_table158
- GCC_except_table160
- GCC_except_table162
- GCC_except_table167
- GCC_except_table173
- GCC_except_table68
- ___112-[BRCAccountSession(DatabaseAdditions) dumpDatabaseToFileHandle:zoneName:includeAllItems:verbose:tracker:error:]_block_invoke.257
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.259
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.259.cold.1
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.261
- ___44-[BRCFSUploader recoverAndReportMissingJobs]_block_invoke.247
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.229.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.236
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.236.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.239
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.251
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.251.cold.1
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.262
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.262.cold.1
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.267
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.268
- ___80-[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]_block_invoke
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.260
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.260.cold.1
- ___block_literal_global.238
- ___block_literal_global.249
- ___block_literal_global.256
- ___block_literal_global.258
- ___block_literal_global.265
- ___block_literal_global.286
- ___block_literal_global.370
- ___block_literal_global.730
- ___block_literal_global.738
- _objc_exception_throw
- _objc_msgSend$br_any_of:
- _objc_msgSend$br_badFilenameAlternativeName
- _objc_msgSend$brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors
- _objc_msgSend$brc_isCloudKitRequestRejectedError
- _objc_msgSend$retriableCKInteralErrorCodesForRejectedRequestedError
CStrings:
+ "-[BRCAccountSession _handleUnloadedZones:]"
+ "-[BRCAccountSession _handleUnloadedZones:]_block_invoke"
+ "-[BRCAccountSession _handleUnloadedZones:]_block_invoke_2"
+ "BRCGetAccountDSIDForMobileDocsRoot"
+ "Reset Local State"
+ "SELECT 1 FROM client_items WHERE zone_rowid = %lu LIMIT 1"
+ "Unloaded zone is referenced by item"
+ "[CRIT] UNREACHABLE: %s xattr value '%@' has the wrong format%@"
+ "[CRIT] UNREACHABLE: Found zoneRowID %lu which was skipped on load but is referenced by an item on DB%@"
+ "[WARNING] Checking if unloaded zone %lu is being referenced by a client item%@"
+ "[WARNING] We found %@ unloaded zones, but handling logic is disabled by user defaults%@"
+ "_handleUnloadedZones:"
+ "_shouldResetLocalData:"
+ "account-session.should.handle.unloaded.zones"
+ "addZoneRowID:"
+ "br_safeFileSystemRepresentation"
+ "database ID: %@"
+ "handleUnloadedZones"
+ "removeZoneRowID:"
- "UPDATE client_uploads SET throttle_state = 1, next_retry_stamp = 0  WHERE throttle_id IN (SELECT cu.throttle_id from client_uploads AS cu LEFT JOIN client_items AS ci                       ON cu.throttle_id = ci.rowid                        WHERE cu.throttle_state = 33                         AND call_block(%p, ci.version_upload_error))"
- "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
- "[DEBUG] Got unexpected exception %@. rethrow%@"
- "[DEBUG] Uploader: scheduling %lld upload jobs that where in permenant failure state%@"
- "br_any_of:"
- "br_badFilenameAlternativeName"
- "brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors"

```
