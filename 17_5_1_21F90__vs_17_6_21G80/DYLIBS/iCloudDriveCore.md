## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-2720.120.29.0.0
-  __TEXT.__text: 0x2c03e0
-  __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0x1595c
+2720.140.11.0.0
+  __TEXT.__text: 0x2c053c
+  __TEXT.__auth_stubs: 0x1b30
+  __TEXT.__objc_methlist: 0x1598c
   __TEXT.__const: 0x358
-  __TEXT.__cstring: 0x74257
-  __TEXT.__oslogstring: 0x37e5d
-  __TEXT.__gcc_except_tab: 0x132d4
+  __TEXT.__cstring: 0x7427d
+  __TEXT.__oslogstring: 0x37ead
+  __TEXT.__gcc_except_tab: 0x132a4
   __TEXT.__ustring: 0x36
   __TEXT.__unwind_info: 0x8214
   __TEXT.__objc_classname: 0x21c2
-  __TEXT.__objc_methname: 0x39ed7
+  __TEXT.__objc_methname: 0x39f45
   __TEXT.__objc_methtype: 0x6ba5
-  __TEXT.__objc_stubs: 0x28080
+  __TEXT.__objc_stubs: 0x28100
   __DATA_CONST.__got: 0xaf8
   __DATA_CONST.__const: 0x81c0
   __DATA_CONST.__objc_classlist: 0x888
-  __DATA_CONST.__objc_catlist: 0xc8
+  __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x30c00
-  __DATA_CONST.__objc_selrefs: 0xc798
+  __DATA_CONST.__objc_const: 0x30c10
+  __DATA_CONST.__objc_selrefs: 0xc7c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xcd8
   __DATA_CONST.__objc_superrefs: 0x7a0
   __DATA_CONST.__objc_arraydata: 0xd98
-  __AUTH_CONST.__cfstring: 0x1fb20
-  __AUTH_CONST.__objc_const: 0x6850
+  __AUTH_CONST.__cfstring: 0x1fba0
+  __AUTH_CONST.__objc_const: 0x6890
   __AUTH_CONST.__const: 0x24e8
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__auth_got: 0xda8
   __AUTH.__objc_data: 0x2850
   __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x1c04

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12907
-  Symbols:   38871
-  CStrings:  20873
+  Functions: 12912
+  Symbols:   38884
+  CStrings:  20888
 
Symbols:
+ -[BRCAccountHandler _shouldResetLocalData:]
+ -[BRCAccountSessionFPFS _handleUnloadedZones:]
+ -[BRCUserDefaults handleUnloadedZones]
+ -[NSMutableIndexSet(BRCZoneRowID) addZoneRowID:]
+ -[NSMutableIndexSet(BRCZoneRowID) removeZoneRowID:]
+ GCC_except_table163
+ GCC_except_table170
+ GCC_except_table187
+ GCC_except_table197
+ _BRCGetAccountDSIDForMobileDocsRoot.cold.1
+ __OBJC_$_CATEGORY_NSMutableIndexSet_$_BRCZoneRowID
+ __OBJC_$_INSTANCE_METHODS_NSMutableIndexSet(BRCZoneRowID)
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.232
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.232.cold.1
+ ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.234
+ ___46-[BRCAccountSessionFPFS _handleUnloadedZones:]_block_invoke
+ ___46-[BRCAccountSessionFPFS _handleUnloadedZones:]_block_invoke_2
+ ___46-[BRCAccountSessionFPFS _handleUnloadedZones:]_block_invoke_2.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.291
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.291.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.291.cold.2
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.291.cold.3
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.291.cold.4
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.298
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.298.cold.1
+ ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.301
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.321
+ ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.321.cold.1
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.235
+ ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.235.cold.1
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.336
+ ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.337
+ ___70-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.352
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.329
+ ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.329.cold.1
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.328
+ ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.328.cold.1
+ ___block_literal_global.15
+ ___block_literal_global.229
+ ___block_literal_global.231
+ ___block_literal_global.300
+ ___block_literal_global.334
+ ___block_literal_global.340
+ ___block_literal_global.778
+ ___block_literal_global.786
+ _objc_msgSend$_handleUnloadedZones:
+ _objc_msgSend$_shouldResetLocalData:
+ _objc_msgSend$addZoneRowID:
+ _objc_msgSend$br_isExcludedFromSyncInFPFSIsFile:
+ _objc_msgSend$br_isFileProviderErrorCode:
+ _objc_msgSend$br_safeFileSystemRepresentation
+ _objc_msgSend$handleUnloadedZones
+ _objc_msgSend$removeIndex:
+ _objc_msgSend$removeZoneRowID:
- -[BRCFSUploader recoverAndReportMissingJobs].cold.3
- -[CKRecord(BRCSerializationAdditions) deserializeFilename:basename:bounceno:extension:userInfo:error:].cold.3
- -[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]
- GCC_except_table153
- GCC_except_table160
- GCC_except_table167
- GCC_except_table171
- GCC_except_table173
- GCC_except_table184
- GCC_except_table190
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.229
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.229.cold.1
- ___116-[BRCAccountHandler setMigrationStatus:forDSID:shouldUpdateAccount:shouldPostAccountChangedNotification:completion:]_block_invoke.231
- ___44-[BRCFSUploader recoverAndReportMissingJobs]_block_invoke.247
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.2
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.3
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.290.cold.4
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.297
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.297.cold.1
- ___49-[BRCAccountSessionFPFS _loadClientZonesFromDisk]_block_invoke.300
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.312
- ___49-[BRCAccountSessionFPFS destroySharedClientZone:]_block_invoke.312.cold.1
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.232
- ___51-[BRCAccountHandler markMigrationCompletedForDSID:]_block_invoke.232.cold.1
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.327
- ___64-[BRCAccountSessionFPFS fetchUserRecordIDWithCompletionHandler:]_block_invoke.328
- ___70-[BRCAccountSessionFPFS setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.343
- ___80-[NSError(BRCAdditions) brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors]_block_invoke
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.320
- ___88-[BRCAccountSessionFPFS _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.320.cold.1
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.319
- ___99-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke.319.cold.1
- ___block_literal_global.226
- ___block_literal_global.228
- ___block_literal_global.249
- ___block_literal_global.299
- ___block_literal_global.325
- ___block_literal_global.336
- ___block_literal_global.768
- ___block_literal_global.776
- _fpfs_path_is_safe_save_temp_file_ext
- _objc_exception_throw
- _objc_msgSend$br_any_of:
- _objc_msgSend$br_badFilenameAlternativeName
- _objc_msgSend$brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors
- _objc_msgSend$brc_isCloudKitRequestRejectedError
- _objc_msgSend$retriableCKInteralErrorCodesForRejectedRequestedError
CStrings:
+ "-[BRCAccountSessionFPFS _handleUnloadedZones:]"
+ "-[BRCAccountSessionFPFS _handleUnloadedZones:]_block_invoke"
+ "-[BRCAccountSessionFPFS _handleUnloadedZones:]_block_invoke_2"
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
+ "br_isExcludedFromSyncInFPFSIsFile:"
+ "br_isFileProviderErrorCode:"
+ "br_safeFileSystemRepresentation"
+ "database ID: %@"
+ "handleUnloadedZones"
+ "removeIndex:"
+ "removeZoneRowID:"
- "UPDATE client_uploads SET throttle_state = 1, next_retry_stamp = 0  WHERE throttle_id IN (SELECT cu.throttle_id from client_uploads AS cu LEFT JOIN client_items AS ci                       ON cu.throttle_id = ci.rowid                        WHERE cu.throttle_state = 33                         AND call_block(%p, ci.version_upload_error))"
- "[DEBUG] Could not convert %@ to fileSystemRepresentation for reason: %@ --> use bad filename alternative name instead%@"
- "[DEBUG] Got unexpected exception %@. rethrow%@"
- "[DEBUG] Uploader: scheduling %lld upload jobs that where in permenant failure state%@"
- "br_any_of:"
- "br_badFilenameAlternativeName"
- "brc_hasAnyRetriableUnderlyingErrorInCKRejectedTopErrors"

```
