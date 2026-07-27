## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/iCloudDriveCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-4479.160.7.0.1
-  __TEXT.__text: 0x362cec
+4479.160.12.0.0
+  __TEXT.__text: 0x362d9c
   __TEXT.__auth_stubs: 0x19c0
   __TEXT.__objc_methlist: 0x1add0
   __TEXT.__const: 0x508
-  __TEXT.__cstring: 0x7f8fc
-  __TEXT.__oslogstring: 0x3cae9
-  __TEXT.__gcc_except_tab: 0x1a720
+  __TEXT.__cstring: 0x7fb72
+  __TEXT.__oslogstring: 0x3cadc
+  __TEXT.__gcc_except_tab: 0x1a710
   __TEXT.__ustring: 0x36
   __TEXT.__unwind_info: 0xa9d0
   __TEXT.__objc_classname: 0x2b1f

   __TEXT.__objc_methtype: 0x96ad
   __TEXT.__objc_stubs: 0x30420
   __DATA_CONST.__got: 0x1790
-  __DATA_CONST.__const: 0x1eb0
+  __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x288

   __DATA_CONST.__objc_arraydata: 0xfc0
   __AUTH_CONST.__auth_got: 0xcf0
   __AUTH_CONST.__const: 0xb390
-  __AUTH_CONST.__cfstring: 0x234a0
+  __AUTH_CONST.__cfstring: 0x234c0
   __AUTH_CONST.__objc_const: 0x3e080
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__objc_arrayobj: 0x300

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14107
+  Functions: 14108
   Symbols:   24694
-  CStrings:  23309
+  CStrings:  23316
 
Functions:
~ -[BRCClientDatabaseFacade getSyncStatusBitMask] : 860 -> 1160
~ -[BRCXPCRegularIPCsClient updateContainerMetadataForID:] : 1368 -> 1364
~ -[BRCXPCRegularIPCsClient simulateHealthIssueWithContainer:status:reply:] : 3264 -> 3100
~ -[BRCXPCRegularIPCsClient updateContainerMetadataForID:].cold.1 : 76 -> 68
~ -[BRCXPCRegularIPCsClient _t_createFileAtURL:reply:].cold.1 : 80 -> 68
~ -[BRCXPCRegularIPCsClient _t_canReadFileAtURL:reply:].cold.2 : 80 -> 68
+ -[BRCXPCRegularIPCsClient waitUntilIdle:timeout:reply:].cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HcvPtz/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
+ "SELECT COUNT(*), COALESCE(SUM(si.recursive_child_count), 0) FROM client_items AS ci INNER JOIN server_items AS si ON ci.item_id = si.item_id AND ci.zone_rowid = si.zone_rowid WHERE ci.item_localsyncupstate = 4   AND ci.item_min_supported_os_rowid IS NULL   AND ci.item_state = 1   AND ci.item_trash_put_back_parent_id IS NOT NULL   AND si.item_trash_put_back_parent_id IS NOT NULL"
+ "SELECT COUNT(*), SUM(item_type IN (0, 9, 10)) FROM client_items WHERE item_localsyncupstate = 4   AND item_min_supported_os_rowid IS NULL   AND item_state = 1"
+ "[ERROR] nonexistent container%@"
+ "tombstoneNeedsSyncUpInTrash"
+ "tombstoneNeedsSyncUpInTrashMoreThan25Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan50Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan75Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan90Percent"
+ "tombstoneNeedsSyncUpInTrashMoreThan95Percent"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/account/BRCAccountSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/account/BRCAccountsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/backup/BRCBackupSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/containers/BRCClientZone.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/containers/BRCServerZone.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/daemon/BRCDaemon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/database/BRCClientDatabaseFacade.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/database/BRCClientState.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/database/BRCDatabaseSchema.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/database/BRCServerPersistedState.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/foundation/BRCFairScheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/foundation/BRCPQLConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/items/BRCItemID.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/notifs/BRCAccountHandler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/sync/records/CKRecord+BRCItemAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vcuQ2O/Sources/CloudDocs_executables/core/shared/sync/transfers/BRCTransferStream.m"
- "SELECT COUNT(*) FROM client_items WHERE item_localsyncupstate != 0 AND item_localsyncupstate == 4 AND item_state = 1 AND NOT item_id_is_documents(item_id) LIMIT 1"
- "[NOTICE] simulating health issue on %@: %@%@"
```
