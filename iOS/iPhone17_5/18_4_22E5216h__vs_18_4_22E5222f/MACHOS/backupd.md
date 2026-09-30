## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2624.100.98.0.0
-  __TEXT.__text: 0x2c54c8
-  __TEXT.__auth_stubs: 0x37a0
-  __TEXT.__objc_stubs: 0x2cbc0
-  __TEXT.__objc_methlist: 0x1a3ec
-  __TEXT.__const: 0x2440
-  __TEXT.__cstring: 0x77ae1
-  __TEXT.__objc_methname: 0x3bae5
-  __TEXT.__constg_swiftt: 0xaf4
-  __TEXT.__swift5_typeref: 0x10d3
+2624.100.102.0.0
+  __TEXT.__text: 0x2c5bd4
+  __TEXT.__auth_stubs: 0x37e0
+  __TEXT.__objc_stubs: 0x2cc20
+  __TEXT.__objc_methlist: 0x1a42c
+  __TEXT.__const: 0x2420
+  __TEXT.__cstring: 0x77c50
+  __TEXT.__objc_methname: 0x3bb54
+  __TEXT.__constg_swiftt: 0xad4
+  __TEXT.__swift5_typeref: 0x10c7
   __TEXT.__swift5_reflstr: 0x14e5
-  __TEXT.__swift5_fieldmd: 0x1508
-  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_fieldmd: 0x14ec
+  __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x184
-  __TEXT.__swift5_types: 0xfc
+  __TEXT.__swift5_types: 0xf8
   __TEXT.__objc_classname: 0x2288
   __TEXT.__objc_methtype: 0x6afa
   __TEXT.__swift5_capture: 0x404
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__oslogstring: 0x352d1
-  __TEXT.__gcc_except_tab: 0xd3b0
+  __TEXT.__oslogstring: 0x35455
+  __TEXT.__gcc_except_tab: 0xd43c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x78c8
+  __TEXT.__unwind_info: 0x78e0
   __TEXT.__eh_frame: 0x27e0
-  __DATA_CONST.__auth_got: 0x1be0
+  __DATA_CONST.__auth_got: 0x1c00
   __DATA_CONST.__got: 0xeb0
-  __DATA_CONST.__auth_ptr: 0x350
-  __DATA_CONST.__const: 0x96a8
-  __DATA_CONST.__cfstring: 0x20be0
+  __DATA_CONST.__auth_ptr: 0x348
+  __DATA_CONST.__const: 0x9678
+  __DATA_CONST.__cfstring: 0x20c00
   __DATA_CONST.__objc_classlist: 0xb38
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x2a0

   __DATA_CONST.__objc_arraydata: 0xd78
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
-  __DATA.__objc_const: 0x28f50
-  __DATA.__objc_selrefs: 0xce78
+  __DATA.__objc_const: 0x28f60
+  __DATA.__objc_selrefs: 0xce98
   __DATA.__objc_ivar: 0x1e34
   __DATA.__objc_data: 0x7b68
   __DATA.__data: 0x2a48

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10867
-  Symbols:   1456
-  CStrings:  25839
+  Functions: 10870
+  Symbols:   1460
+  CStrings:  25856
 
Symbols:
+ _container_copy_from_path
+ _container_delete_all_container_content
+ _container_free_object
+ _container_get_error_description
CStrings:
+ "\n  SELECT domain, \n         totalZeroByteFiles, \n         totalAssetFiles, \n         totalAssetBytes, \n         totalATCFiles, \n         totalATCBytes\n    FROM Domains\nORDER BY totalAssetBytes;"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  absolutePath IS %@\n  AND   domainID = %llu\n  AND  (restoreState = %u OR restoreState = %u)\n LIMIT 1"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND  (restoreState = %u OR restoreState = %u)\n  AND   type = %u\n ORDER BY restorableID ASC"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND  (restoreState = %u OR restoreState = %u)\n  AND   type = %u\n ORDER BY restorableID DESC"
+ "\n UPDATE Domains\n SET    engineState = %u, \n        rootPath = %@\n WHERE  domainID = %llu"
+ "\nCREATE TABLE IF NOT EXISTS Domains (\ndomainID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \ndomain TEXT NOT NULL UNIQUE, \ntotalAssetRecords INTEGER NOT NULL, \ntotalAssetBytes INTEGER NOT NULL, \ntotalXattrBytes INTEGER NOT NULL, \ntotalRegularAssets INTEGER NOT NULL, \ntotalEmptyAssets INTEGER NOT NULL, \ntotalDBAssets INTEGER NOT NULL, \ntotalEncryptedAssets INTEGER NOT NULL, \ntotalItems INTEGER NOT NULL, \ntotalDirs INTEGER NOT NULL, \ntotalSymlinks INTEGER NOT NULL, \ntotalZeroByteFiles INTEGER NOT NULL, \ntotalAssetFiles INTEGER NOT NULL, \ntotalXattrItems INTEGER NOT NULL, \ntotalHardlinks INTEGER NOT NULL, \ntotalATCItems INTEGER NOT NULL, \ntotalATCFiles INTEGER NOT NULL, \ntotalATCBytes INTEGER NOT NULL, \ntotalDatalessItems INTEGER NOT NULL, \nrootPath TEXT, \nengineState INTEGER NOT NULL, \nverificationStatus INTEGER NOT NULL\n);"
+ "\nINSERT INTO Domains (\ndomain, \nengineState, \ntotalItems, \ntotalDirs, \ntotalSymlinks, \ntotalHardlinks, \ntotalXattrItems, \ntotalZeroByteFiles, \ntotalAssetFiles, \ntotalAssetBytes, \ntotalXattrBytes, \ntotalAssetRecords, \ntotalRegularAssets, \ntotalEmptyAssets, \ntotalDBAssets, \ntotalEncryptedAssets, \ntotalATCItems, \ntotalATCFiles, \ntotalATCBytes, \ntotalDatalessItems, \nrootPath, \nverificationStatus\n) VALUES (%@, %u, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, NULL, %u)\nRETURNING domainID;"
+ "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u\n GROUP BY RestorableAssets.inode;"
+ "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE Restorables.absolutePath IS %@\n   AND RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u LIMIT 1"
+ "=ckrestore-engine= Foreground asset count:%llu size:%llu, background asset count:%llu size:%llu"
+ "=domain-engine= App %@ was uninstalled while a it was being restored, reporting %@ instead of %@ "
+ "=domain-engine= Resetting container for %@ with root %@ after fatal restore error"
+ "B64@?0@\"NSString\"8Q16Q24q32Q40q48^@56"
+ "Failed to reset container at %@: %s"
+ "No container found to reset at path %@"
+ "PendingDirectoryFixUp"
+ "Reset container %s with root path %@"
+ "_isFatalRestoreErrorToRecordInPlan:"
+ "containerIDForPath:error:"
+ "container_copy_from_path failed: %s"
+ "container_delete_all_container_content failed: %s"
+ "resetContainerWithRoot:error:"
+ "stringWithCString:"
- "\n  SELECT domain, \n         restoreType, \n         totalZeroByteFiles, \n         totalAssetFiles, \n         totalAssetBytes, \n         totalATCFiles, \n         totalATCBytes\n    FROM Domains\nORDER BY totalAssetBytes;"
- "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  absolutePath IS %@\n  AND   domainID = %llu\n  AND   restoreState = %u\n LIMIT 1"
- "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID ASC"
- "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID DESC"
- "\n UPDATE Domains\n SET    engineState = %u, \n        restoreType = %u, \n        rootPath = %@\n WHERE  domainID = %llu"
- "\nCREATE TABLE IF NOT EXISTS Domains (\ndomainID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \ndomain TEXT NOT NULL UNIQUE, \ntotalAssetRecords INTEGER NOT NULL, \ntotalAssetBytes INTEGER NOT NULL, \ntotalXattrBytes INTEGER NOT NULL, \ntotalRegularAssets INTEGER NOT NULL, \ntotalEmptyAssets INTEGER NOT NULL, \ntotalDBAssets INTEGER NOT NULL, \ntotalEncryptedAssets INTEGER NOT NULL, \ntotalItems INTEGER NOT NULL, \ntotalDirs INTEGER NOT NULL, \ntotalSymlinks INTEGER NOT NULL, \ntotalZeroByteFiles INTEGER NOT NULL, \ntotalAssetFiles INTEGER NOT NULL, \ntotalXattrItems INTEGER NOT NULL, \ntotalHardlinks INTEGER NOT NULL, \ntotalATCItems INTEGER NOT NULL, \ntotalATCFiles INTEGER NOT NULL, \ntotalATCBytes INTEGER NOT NULL, \ntotalDatalessItems INTEGER NOT NULL, \nrootPath TEXT, \nrestoreType INTEGER NOT NULL, \nengineState INTEGER NOT NULL, \nverificationStatus INTEGER NOT NULL\n);"
- "\nINSERT INTO Domains (\ndomain, \nengineState, \nrestoreType, \ntotalItems, \ntotalDirs, \ntotalSymlinks, \ntotalHardlinks, \ntotalXattrItems, \ntotalZeroByteFiles, \ntotalAssetFiles, \ntotalAssetBytes, \ntotalXattrBytes, \ntotalAssetRecords, \ntotalRegularAssets, \ntotalEmptyAssets, \ntotalDBAssets, \ntotalEncryptedAssets, \ntotalATCItems, \ntotalATCFiles, \ntotalATCBytes, \ntotalDatalessItems, \nrootPath, \nverificationStatus\n) VALUES (%@, %u, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, NULL, %u)\nRETURNING domainID;"
- "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u\n GROUP BY RestorableAssets.inode;"
- "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE Restorables.absolutePath IS %@\n   AND RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u LIMIT 1"
- "B68@?0@\"NSString\"8i16Q20Q28q36Q44q52^@60"
- "Internal Error"
- "Placed"

```
