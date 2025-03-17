## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2624.100.102.0.0
-  __TEXT.__text: 0x2c5bd4
+2624.102.1.0.0
+  __TEXT.__text: 0x2c5f88
   __TEXT.__auth_stubs: 0x37e0
-  __TEXT.__objc_stubs: 0x2cc20
+  __TEXT.__objc_stubs: 0x2cc40
   __TEXT.__objc_methlist: 0x1a42c
   __TEXT.__const: 0x2420
-  __TEXT.__cstring: 0x77c50
-  __TEXT.__objc_methname: 0x3bb54
+  __TEXT.__cstring: 0x77e56
+  __TEXT.__objc_methname: 0x3bb7a
   __TEXT.__constg_swiftt: 0xad4
   __TEXT.__swift5_typeref: 0x10c7
   __TEXT.__swift5_reflstr: 0x14e5

   __TEXT.__swift5_capture: 0x404
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__oslogstring: 0x35455
-  __TEXT.__gcc_except_tab: 0xd43c
+  __TEXT.__oslogstring: 0x35555
+  __TEXT.__gcc_except_tab: 0xd460
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x78e0
   __TEXT.__eh_frame: 0x27e0
   __DATA_CONST.__auth_got: 0x1c00
   __DATA_CONST.__got: 0xeb0
-  __DATA_CONST.__auth_ptr: 0x348
+  __DATA_CONST.__auth_ptr: 0x350
   __DATA_CONST.__const: 0x9678
   __DATA_CONST.__cfstring: 0x20c00
   __DATA_CONST.__objc_classlist: 0xb38

   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
   __DATA.__objc_const: 0x28f60
-  __DATA.__objc_selrefs: 0xce98
+  __DATA.__objc_selrefs: 0xcea8
   __DATA.__objc_ivar: 0x1e34
   __DATA.__objc_data: 0x7b68
   __DATA.__data: 0x2a48

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 10870
   Symbols:   1460
-  CStrings:  25856
+  CStrings:  25868
 
CStrings:
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE (restoreState = %u OR restoreState = %u )\n   AND  Restorables.domainID = %llu\n   AND  type = %u"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  (restoreState = %u OR restoreState = %u )\n   AND  Restorables.domainID = %llu\n   AND  type = %u LIMIT 1"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE (restoreState = %u OR restoreState = %u )\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size != 0"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE (restoreState = %u OR restoreState = %u )\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size = 0"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  (restoreState = %u OR restoreState = %u )\n   AND  size != 0 LIMIT 1"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  (restoreState = %u OR restoreState = %u )\n   AND  size = 0"
+ "\n SELECT relativePath, \nmode, \npriority, \nabsolutePath\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   (restoreState = %u OR restoreState = %u OR restoreState = %u OR restoreState = %u)\n ORDER BY Restorables.type, Restorables.restorableID ASC\n LIMIT %lu OFFSET %lu;"
+ " does not contain assetID prefix"
+ "=cloud-backup-policy= Invalid snapshot format for backup (%lld) %@"
+ "=cloud-backup= Failed to stash missed encryption keys DB: %@"
+ "=cloud-backup= Invalidating pending snapshot - behaviour option"
+ "=restore-policy= Not restoring mobile gestalt cache: %{public}@"
+ "Device record for snapshot "
+ "forceInvalidatePendingSnapshot"
+ "format"
+ "systemgroup.com.apple.mobilegestaltcache"
- "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u LIMIT 1"
- "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size != 0 LIMIT 1"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size = 0"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size != 0"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size = 0"
- "\n SELECT relativePath, \nmode, \npriority, \nabsolutePath\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   (restoreState = %u OR restoreState = %u)\n ORDER BY Restorables.type, Restorables.restorableID ASC\n LIMIT %lu OFFSET %lu;"
- "Invalid snapshot format for backup (%lld) %@"

```
