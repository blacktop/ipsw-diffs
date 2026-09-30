## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.0.20.0.2
-  __TEXT.__text: 0x30e32c
+4257.2.1.0.0
+  __TEXT.__text: 0x30e5fc
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x1a02c
+  __TEXT.__objc_methlist: 0x1a034
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d152
+  __TEXT.__cstring: 0x7d217
   __TEXT.__oslogstring: 0x3bf5b
   __TEXT.__gcc_except_tab: 0x1a3ac
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9f00
+  __TEXT.__unwind_info: 0x9f08
   __TEXT.__objc_classname: 0x2a9d
-  __TEXT.__objc_methname: 0x441aa
+  __TEXT.__objc_methname: 0x441c0
   __TEXT.__objc_methtype: 0x8fc6
-  __TEXT.__objc_stubs: 0x2ee40
+  __TEXT.__objc_stubs: 0x2ee60
   __DATA_CONST.__got: 0x16f8
   __DATA_CONST.__const: 0x95c8
   __DATA_CONST.__objc_classlist: 0xa50
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe5f8
+  __DATA_CONST.__objc_selrefs: 0xe600
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x910
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x2b78
-  __AUTH_CONST.__cfstring: 0x22860
+  __AUTH_CONST.__const: 0x2b80
+  __AUTH_CONST.__cfstring: 0x228c0
   __AUTH_CONST.__objc_const: 0x3cfa0
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 17557ABD-3C90-3D12-ADD7-85FB1008D3D7
-  Functions: 13544
-  Symbols:   44086
-  CStrings:  27629
+  UUID: 0D585642-3C46-37C6-A6F2-5BB3E18593E4
+  Functions: 13546
+  Symbols:   44091
+  CStrings:  27637
 
Symbols:
+ -[BRCAppLibrary didUpdatePristineness]
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table275
+ GCC_except_table294
+ ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.142
+ ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke.148
+ ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.177
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.175
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.175.cold.1
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.176
+ ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.176.cold.1
+ ___block_literal_global.179
+ _br_db_fixup_9
+ _objc_msgSend$didUpdatePristineness
- GCC_except_table269
- GCC_except_table293
- ___234-[BRCAppLibrary itemsEnumeratorWithRankMin:rankMax:namePrefix:withDeadItems:shouldIncludeFolders:shouldIncludeOnlyFolders:shouldIncludeDocumentsScope:shouldIncludeDataScope:shouldIncludeExternalScope:shouldIncludeTrashScope:count:db:]_block_invoke.136
- ___48-[BRCAppLibrary resumeQueryBasedSyncIfNecessary]_block_invoke.142
- ___52-[BRCAppLibrary waitForRootIngestionWithCompletion:]_block_invoke.171
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.169
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.169.cold.1
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.170
- ___58-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke.170.cold.1
- ___block_literal_global.173
Functions:
~ -[BRCAppLibrary _activateState:origState:] : 1696 -> 1708
+ -[BRCAppLibrary didUpdatePristineness]
+ _br_db_fixup_9
~ -[BRCClientDatabaseFacade itemByParentID:andLogicalName:excludingItemID:zoneRowID:itemBuilder:] : 704 -> 708
CStrings:
+ "-[BRCAppLibrary didUpdatePristineness]"
+ "SELECT rowid, zone_rowid, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_parent_zone_rowid, item_localsyncupstate, item_local_diffs, item_notifs_rank, app_library_rowid, item_min_supported_os_rowid, item_user_visible, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, item_processing_stamp, item_bouncedname, item_scope, item_local_change_count, item_old_version_identifier, fp_creation_item_identifier, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, version_uploaded_assets, version_upload_error, version_old_zone_item_id, version_old_zone_rowid, version_local_change_count, version_old_version_identifier, item_live_conflict_loser_etags, item_file_id, item_generation FROM client_items WHERE ((item_parent_id = %@ AND item_parent_zone_rowid = %@ AND item_filename = %@ AND item_bouncedname IS NULL) OR (item_parent_id = %@ AND item_parent_zone_rowid = %@ AND item_bouncedname = %@)) %@"
+ "UPDATE client_items SET item_notifs_rank = bump_notifs_rank() WHERE item_id = %@"
+ "didUpdatePristineness"
+ "non-pristine"
+ "pristine"
- "SELECT rowid, zone_rowid, item_id, item_creator_id, item_sharing_options, item_side_car_ckinfo, item_parent_zone_rowid, item_localsyncupstate, item_local_diffs, item_notifs_rank, app_library_rowid, item_min_supported_os_rowid, item_user_visible, item_stat_ckinfo, item_state, item_type, item_mode, item_birthtime, item_lastusedtime, item_favoriterank,item_parent_id, item_filename, item_hidden_ext, item_finder_tags, item_xattr_signature, item_trash_put_back_path, item_trash_put_back_parent_id, item_alias_target, item_creator, item_processing_stamp, item_bouncedname, item_scope, item_local_change_count, item_old_version_identifier, fp_creation_item_identifier, version_name, version_ckinfo, version_mtime, version_size, version_thumb_size, version_thumb_signature, version_content_signature, version_xattr_signature, version_edited_since_shared, version_device, version_conflict_loser_etags, version_quarantine_info, version_uploaded_assets, version_upload_error, version_old_zone_item_id, version_old_zone_rowid, version_local_change_count, version_old_version_identifier, item_live_conflict_loser_etags, item_file_id, item_generation FROM client_items WHERE item_parent_id = %@ AND item_parent_zone_rowid = %@ AND  ((item_filename = %@ AND item_bouncedname IS NULL) OR (item_bouncedname = %@)) %@"

```
