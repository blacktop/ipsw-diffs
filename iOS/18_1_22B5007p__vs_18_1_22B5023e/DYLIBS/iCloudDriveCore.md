## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3097.0.216.0.1
-  __TEXT.__text: 0x2d3278
+3097.0.245.0.0
+  __TEXT.__text: 0x2d55e8
   __TEXT.__auth_stubs: 0x1b70
-  __TEXT.__objc_methlist: 0x165c0
+  __TEXT.__objc_methlist: 0x16688
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x77d23
-  __TEXT.__oslogstring: 0x3963b
-  __TEXT.__gcc_except_tab: 0x17ec0
+  __TEXT.__cstring: 0x78092
+  __TEXT.__oslogstring: 0x39823
+  __TEXT.__gcc_except_tab: 0x1800c
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x8560
+  __TEXT.__unwind_info: 0x85e8
   __TEXT.__objc_classname: 0x2388
-  __TEXT.__objc_methname: 0x3d076
-  __TEXT.__objc_methtype: 0x760f
-  __TEXT.__objc_stubs: 0x29d80
+  __TEXT.__objc_methname: 0x3d2ef
+  __TEXT.__objc_methtype: 0x762d
+  __TEXT.__objc_stubs: 0x29f80
   __DATA_CONST.__got: 0x1650
-  __DATA_CONST.__const: 0x8630
+  __DATA_CONST.__const: 0x86a8
   __DATA_CONST.__objc_classlist: 0x8e0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd010
+  __DATA_CONST.__objc_selrefs: 0xd088
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7e8
   __DATA_CONST.__objc_arraydata: 0xe00
   __AUTH_CONST.__auth_got: 0xdc8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2678
-  __AUTH_CONST.__cfstring: 0x21180
-  __AUTH_CONST.__objc_const: 0x39988
-  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__const: 0x26a8
+  __AUTH_CONST.__cfstring: 0x212e0
+  __AUTH_CONST.__objc_const: 0x399e8
+  __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x2a80
+  __AUTH.__objc_data: 0x2850
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1d34
+  __DATA.__objc_ivar: 0x1d3c
   __DATA.__data: 0x2168
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0x2e40
+  __DATA.__bss: 0x228
+  __DATA_DIRTY.__objc_data: 0x3070
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x2d0
+  __DATA_DIRTY.__bss: 0x328
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12315
-  Symbols:   15048
-  CStrings:  21677
+  Functions: 12351
+  Symbols:   15090
+  CStrings:  21721
 
Symbols:
+ OBJC_IVAR_$_BRCAppLibrary._forceIngestionGroup
CStrings:
+ "\b\x11\"\x11\x1c\x13\x14\x1e\x12$"
+ " last-error: %!@(MISSING)"
+ "%!@(MISSING):%!l(MISSING)d"
+ "-[BRCAccountSessionFPFS _saltPartiallySaltedItemsWithActivity:]_block_invoke"
+ "-[BRCAccountSessionFPFS _saltPartiallySaltedItemsWithActivity:]_block_invoke_2"
+ "-[BRCAppLibrary flushAndForceIngestRootAndDocumentsFolder]_block_invoke"
+ "-[BRCAppLibrary waitForRootIngestion]"
+ "-[BRCClientZone addOutOfBandOperation:]_block_invoke_2"
+ "-[BRCClientZone removeOutOfBandOperation:]_block_invoke"
+ "-[BRCXPCClient _waitForContainerToBeForcedIngestWithContainerID:containerURL:sandboxExtension:bundleVersion:error:reply:]"
+ "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:outOfBandUpload:error:]"
+ "5\"H\x12"
+ "AGGRESSIVE_SALTING"
+ "Aggressive salting (partially salted)"
+ "AppLibrary is nil"
+ "B60@0:8^@16^@24^@32@40B48^@52"
+ "CA_NIL_APP_LIBRARY"
+ "CREATE INDEX \"server_items/partially_salted_folders\" ON server_items (zone_rowid, item_id) WHERE item_type IN (0, 9, 10) AND salting_state = 2"
+ "SELECT item_id FROM server_items WHERE salting_state = 2 AND item_type IN (0, 9, 10) AND zone_rowid = %!@(MISSING) LIMIT 1"
+ "[CRIT] UNREACHABLE: Container %!@(MISSING) should really exist!%!@(MISSING)"
+ "[DEBUG] Checking for items that need salting%!@(MISSING)"
+ "[DEBUG] Failed to defer the salting state%!@(MISSING)"
+ "[DEBUG] Finished waiting for force ingestion of %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] Item %!@(MISSING) is waiting for re-apply from the server truth%!@(MISSING)"
+ "[DEBUG] Waiting for %!@(MISSING) to be forced ingest%!@(MISSING)"
+ "[DEBUG] We asked FP to reingest item %!@(MISSING), but we still don't have the fileID to upload%!@(MISSING)"
+ "[DEBUG] added %!@(MISSING) as out of band sync operation%!@(MISSING)"
+ "[DEBUG] removed %!@(MISSING) out of band sync operation%!@(MISSING)"
+ "[ERROR] failed to continue the salting state%!@(MISSING)"
+ "_appLibrariesState"
+ "_cancelOutOfBandOperations"
+ "_forceIngestionGroup"
+ "_getAndUpdateDaysSinceLastMigrationProgress:itemsNotMigrated:reconciledItems:"
+ "_getPartiallySaltedItemWithAppLibrary:"
+ "_outOfBandSyncOperations"
+ "_saltPartiallySaltedItemsWithActivity:"
+ "_waitForContainerToBeForcedIngestWithContainerID:containerURL:sandboxExtension:bundleVersion:error:reply:"
+ "addOutOfBandOperation:"
+ "br_partialSaltingCompletion"
+ "brc_isSaltingError"
+ "com.apple.bird.finish-salting-partially-salted-directories"
+ "deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:outOfBandUpload:error:"
+ "edp.aggressive-salting"
+ "finishSaltingPartiallySaltedDirectories"
+ "finishSaltingPartiallySaltedDirectoriesActivity"
+ "flushAndForceIngestRootAndDocumentsFolder"
+ "isBusy"
+ "lastErrorDescription"
+ "removeOutOfBandOperation:"
+ "salt-partially-salted"
+ "waitForRootIngestion"
+ "\x812"
- "\b\x11\"\x11\x1c\x13\x14\x1d\x12$"
- "-[BRCAccountSessionFPFS __getOrCreateAppLibrary:rowID:alreadyExists:withClientZone:createCZMMoved:]_block_invoke"
- "-[CKRecord(BRCSerializationAdditions) deserializeVersion:fakeStatInfo:contentBoundaryKey:clientZone:error:]"
- "4\"H\x12"
- "[CRIT] UNREACHABLE: Can't compute padded file size%!@(MISSING)"
- "_daysSinceLastMigrationProgress:itemsNotMigrated:reconciledItems:"
- "paddedFileSize"
- "q2"

```
