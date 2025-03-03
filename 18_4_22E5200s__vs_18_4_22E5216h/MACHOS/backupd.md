## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2624.100.67.0.0
-  __TEXT.__text: 0x2c3af8
-  __TEXT.__auth_stubs: 0x37b0
+2624.100.98.0.0
+  __TEXT.__text: 0x2c54c8
+  __TEXT.__auth_stubs: 0x37a0
   __TEXT.__objc_stubs: 0x2cbc0
-  __TEXT.__objc_methlist: 0x1a4a4
-  __TEXT.__const: 0x2520
-  __TEXT.__cstring: 0x76be8
-  __TEXT.__objc_methname: 0x3bc28
-  __TEXT.__constg_swiftt: 0xb30
-  __TEXT.__swift5_typeref: 0x10c3
-  __TEXT.__swift5_reflstr: 0x1515
-  __TEXT.__swift5_fieldmd: 0x153c
-  __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0x104
-  __TEXT.__objc_classname: 0x225f
-  __TEXT.__objc_methtype: 0x6af1
+  __TEXT.__objc_methlist: 0x1a3ec
+  __TEXT.__const: 0x2440
+  __TEXT.__cstring: 0x77ae1
+  __TEXT.__objc_methname: 0x3bae5
+  __TEXT.__constg_swiftt: 0xaf4
+  __TEXT.__swift5_typeref: 0x10d3
+  __TEXT.__swift5_reflstr: 0x14e5
+  __TEXT.__swift5_fieldmd: 0x1508
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_proto: 0x184
+  __TEXT.__swift5_types: 0xfc
+  __TEXT.__objc_classname: 0x2288
+  __TEXT.__objc_methtype: 0x6afa
   __TEXT.__swift5_capture: 0x404
-  __TEXT.__oslogstring: 0x34dc1
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__gcc_except_tab: 0xd3f8
+  __TEXT.__oslogstring: 0x352d1
+  __TEXT.__gcc_except_tab: 0xd3b0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x7908
-  __TEXT.__eh_frame: 0x27d0
-  __DATA_CONST.__auth_got: 0x1be8
-  __DATA_CONST.__got: 0xe98
-  __DATA_CONST.__auth_ptr: 0x370
-  __DATA_CONST.__const: 0x9758
-  __DATA_CONST.__cfstring: 0x20ba0
-  __DATA_CONST.__objc_classlist: 0xb30
+  __TEXT.__unwind_info: 0x78c8
+  __TEXT.__eh_frame: 0x27e0
+  __DATA_CONST.__auth_got: 0x1be0
+  __DATA_CONST.__got: 0xeb0
+  __DATA_CONST.__auth_ptr: 0x350
+  __DATA_CONST.__const: 0x96a8
+  __DATA_CONST.__cfstring: 0x20be0
+  __DATA_CONST.__objc_classlist: 0xb38
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x298
+  __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x828
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xd78
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x540
-  __DATA.__objc_const: 0x290b8
-  __DATA.__objc_selrefs: 0xcec0
-  __DATA.__objc_ivar: 0x1e5c
-  __DATA.__objc_data: 0x7b18
+  __DATA.__objc_const: 0x28f50
+  __DATA.__objc_selrefs: 0xce78
+  __DATA.__objc_ivar: 0x1e34
+  __DATA.__objc_data: 0x7b68
   __DATA.__data: 0x2a48
-  __DATA.__bss: 0x3870
+  __DATA.__bss: 0x36f0
   __DATA.__common: 0x49
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10890
+  Functions: 10867
   Symbols:   1456
-  CStrings:  25838
+  CStrings:  25839
 
Symbols:
+ _$ss5Int32VN
+ _$ss5Int32Vs23CustomStringConvertiblesWP
+ _MKBKeyBagKeyStashCommit
+ _OBJC_CLASS_$_MBManagedPolicy
+ _objc_retain_x11
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$s10Foundation4DataVMn
- _$ss4Int8VMn
- _MCFeatureAccountModificationAllowed
- _MCFeatureCloudBackupAllowed
- _objc_retain_x7
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x05\xa76"
+ "\n SELECT Domains.domain, \nRestorables.domainID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, \nxattrs, \nrelativePath, \nrestorableID\n FROM   Restorables\n  JOIN  Domains ON\n       (Restorables.domainID = Domains.domainID)\n WHERE  Restorables.absolutePath = %@;"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u LIMIT 1"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  absolutePath IS %@\n  AND   domainID = %llu\n  AND   restoreState = %u\n LIMIT 1"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID ASC"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID DESC"
+ "\n SELECT Restorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu;"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size != 0 LIMIT 1"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size = 0"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size != 0"
+ "\n SELECT Restorables.restorableID, \nRestorables.inode, Restorables.size, Restorables.birth, Restorables.modified, Restorables.statusChanged, Restorables.userID, Restorables.groupID, Restorables.mode, Restorables.flags, Restorables.protectionClass, Restorables.xattrs, Restorables.relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size = 0"
+ "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u\n GROUP BY RestorableAssets.inode;"
+ "\nSELECT RestorableAssets.inode, \nlinkCount, \nRestorableAssets.recordIDSuffix, RestorableAssets.encryptionKey, RestorableAssets.compressionMethod, RestorableAssets.assetType, RestorableAssets.assetSize, RestorableAssets.assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE Restorables.absolutePath IS %@\n   AND RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u LIMIT 1"
+ " after decompressing"
+ " after performing cross-volume copy"
+ " as Class C, since Cx is unavailable (ignoring "
+ " before decompressing"
+ " before performing cross-volume copy"
+ " was already removed from CK container "
+ "%@-%llu-%@.%@"
+ "+[MBAssetDecrypterFactory assetDecrypterWithTracker:device:error:]"
+ "+[MBAssetRecordFetcher assetFetcherWithTracker:device:error:]"
+ "-[MBAssetRecordFetcher _handleAssetFetchResponseFor:record:withFetchError:]"
+ "-[MBBackupScheduler _initWithServiceManager:]"
+ "-[MBCKBackupEngine _snapshotFormatForAccount:previousSnapshot:error:]"
+ "-[MBCKEngine _refreshSnapshot:operationTracker:refreshState:fileToDomainCache:error:]"
+ "-[MBRestoreDomainEngine fetcher:didReceiveAsset:path:]"
+ "-[MBRestoreDomainEngine initWithRootPath:policy:depot:fetcher:decrypter:plan:progress:verifier:logger:error:]"
+ "-[_AssetDecrypter _initWithTracker:device:]"
+ "-[_AssetDecrypter _keybag:metadata:]"
+ "-[_AssetDecrypter decrypt:restorable:metadata:error:]"
+ "=cloud-backup-policy= Default snapshot format: %@"
+ "=cloud-backup-policy= Previous snapshot format: %@"
+ "=cloud-backup= Account disabled in EDU and RRTS mode"
+ "=cloud-backup= Failed to load domains to back up: %@"
+ "=daemon= Committed stash bag"
+ "=daemon= Doing a Userspace reboot"
+ "=daemon= Doing a full reboot"
+ "=daemon= Idled. Stopping service."
+ "=daemon= MBDaemonIdleTimerInterval=%ld"
+ "=daemon= Not rebooting after restore because %@ %@ preference is set"
+ "=daemon= Over-released work assertion: %s"
+ "=daemon= SIGHUP"
+ "=daemon= SIGQUIT"
+ "=daemon= SIGTERM"
+ "=daemon= SIGUSR2"
+ "=daemon= Unable to commit stash bag: %d"
+ "=daemon= Unhandled signal %d"
+ "=daemon= holdWorkAssertion: %s, %d"
+ "=daemon= reboot3 failed: %d"
+ "=daemon= releaseWorkAssertion: %s, %d"
+ "=diag= %s does not have associated crypto dstreams"
+ "=domain repair= Found domainHMACsToRepair for %@ record: %@"
+ "=restorable= =restorable= Failed to fetch the protection class for %@: %@"
+ "=restorable= =restorable= Failed to set protection class %d at %@: %@"
+ "=restorable= =restorable= Unexpected device lock error for pc:%d"
+ "=restorable= Cannot restore domain root %@ for %@ as symlink"
+ "=restorable= Creating empty file at %@"
+ "=restorable= Creating symbolic link: %@"
+ "=restorable= Directory already exists"
+ "=restorable= Expected failure setting protection class %d -> %d: %@"
+ "=restorable= Failed to clone from %@ to %@: %{errno}d"
+ "=restorable= Failed to get current protection class: %@"
+ "=restorable= Failed to hardlink from %@ to %@: %{errno}d"
+ "=restorable= Failed to move from %@ to %@: %@"
+ "=restorable= Failed to resolve On My iPhone file conflict from %@ to %@(%ld): %@"
+ "=restorable= Failed to restore BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore directory BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore protection class %d instead of %d at %@: %@"
+ "=restorable= Failed to restore regular file BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore symlink BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Fixing ownership at %@"
+ "=restorable= Making directory at %@ (0%3o)"
+ "=restorable= Making directory: 0%3o"
+ "=restorable= Not re-applying the com.apple.decmpfs xattr yet."
+ "=restorable= Not restoring protection class for symlink at %@"
+ "=restorable= Protection class is already %d, not setting for path: %s"
+ "=restorable= Removing existing %@"
+ "=restorable= Removing existing object %@"
+ "=restorable= Restoring BSD flags: 0x%x"
+ "=restorable= Restoring attributes u/gid %d/%d, b/m/c/atime %ld/%ld/%ld/%ld, permissions 0%o to %@"
+ "=restorable= Restoring directory BSD flags: 0x%x"
+ "=restorable= Restoring directory extended attributes (%ld) at path %@"
+ "=restorable= Restoring directory ownership: %d:%d at path %@"
+ "=restorable= Restoring directory permissions: 0%3o"
+ "=restorable= Restoring last modified time (%@) at %@"
+ "=restorable= Restoring last modified time (%@) for %@"
+ "=restorable= Restoring protection class %d at %@"
+ "=restorable= Restoring protection class %d instead of %d for: %@"
+ "=restorable= Restoring protection class: %d -> %d for path: %s"
+ "=restorable= Restoring regular file BSD flags: 0x%x at %@"
+ "=restorable= Restoring regular file extended attributes (%ld) at %@"
+ "=restorable= Restoring regular file ownership: %d:%d at %@"
+ "=restorable= Restoring regular file permissions: 0%3o at %@"
+ "=restorable= Restoring symbolic link extended attributes"
+ "=restorable= Restoring symbolic link ownership: %d:%d"
+ "=restorable= Restoring symbolic link permissions: 0%3o"
+ "=restorable= Restoring symlink BSD flags: 0x%x"
+ "=restorable= Successfully resolved On My iPhone file conflict from %@ to %@(%ld)"
+ "=restorable= The hashes of existing file and restoring file are the same. Skip re-restoring On My iPhone file at %@"
+ "=restorable= Unexpected failure setting protection class %d -> %d: %@"
+ "=restorable= Unexpected nil extended attribute com.apple.decmpfs for dataless file: %@"
+ "=restorable= Unspecified data class for %@ -> defaulting to %d"
+ "=restorable= Using APFSIOC_MAKE_OBJECT_DATALESS to restore the com.apple.decmpfs xattr on %@: %@"
+ "=restorable= fsctl(APFSIOC_MAKE_OBJECT_DATALESS) failed at %@: %{errno}d"
+ "=restorable= fstatat failed at %s (%ld): %{errno}d"
+ "=scanning= No domain root present for %@ found at %@ under %@"
+ "=scheduler= Received notification for account %{public}@: %@"
+ "=transcribing= Reusing asset %@ for %@:%@ (inode: %llu) because of metadata-only change 0x%lx"
+ "=transcribing= Reusing asset %@ for %@:%@ across volume transition (old inode: %llu, new inode: %llu) because of metadata-only change 0x%lx"
+ "@28@0:8C16@20"
+ "@32@0:8^@16@24"
+ "@80@0:8@16@24@32@40@48@56@64^@72"
+ "@96@0:8@16@24@32@40@48@56@64@72@80^@88"
+ "B32@0:8^@16@?<Q@?@\"<MBRestorable>\"B@\"MBAssetMetadata\"^@>24"
+ "B48@0:8@\"NSString\"16@\"<MBRestorable>\"24@\"MBAssetMetadata\"32^@40"
+ "B76@0:8@16@24@32@40B48@52@60^@68"
+ "CREATE TEMPORARY TABLE IF NOT EXISTS HardlinkedInodes (inode INTEGER NOT NULL PRIMARY KEY) "
+ "Compressed asset "
+ "DELETE FROM Assets WHERE inode IN (SELECT inode FROM HardlinkedInodes)"
+ "DELETE FROM FileMetadata WHERE inode IN (SELECT inode FROM HardlinkedInodes)"
+ "DELETE FROM SymlinkTargets WHERE inode IN (SELECT inode FROM HardlinkedInodes)"
+ "DROP TABLE IF EXISTS HardlinkedInodes"
+ "DecrypterAdditions"
+ "Decrypting asset in place at %@ with keybag %@"
+ "Depositing asset (ino: "
+ "Failed to decrypt asset at %@, metadata:%@, on-disk:%@: %@"
+ "Failed to find a keybag to decrypt asset at %@: %@"
+ "Failed to get file info for %@: %@"
+ "Failed to set Cx protection class, leaving as C on %@, error:%@"
+ "Failed to unlock keybag to decrypt asset at %@: %@"
+ "INSERT OR REPLACE INTO HardlinkedInodes (inode) SELECT inode FROM FileMetadata GROUP BY inode HAVING COUNT(*) > 1"
+ "Loaded FSEvent state %@"
+ "MBAssetDecrypter.m"
+ "MBAssetDecrypterFactory"
+ "Metadata mismatch [%@] for %@ %@:\n\tcloud: %@\n\tlocal: %@"
+ "No keybag found for protected asset"
+ "Not changing the \"%{public}@\" state on account %{public}@: %@"
+ "Not sending telemetry: %@"
+ "Q36@?0@\"<MBRestorable>\"8B16@\"MBAssetMetadata\"20^@28"
+ "_MBChangedBackupConditions"
+ "_changedConditions"
+ "_decrypter"
+ "_encodingPath"
+ "_handleAssetFetchResponseFor:record:withFetchError:"
+ "_initWithServiceManager:"
+ "_keybag:metadata:"
+ "_openRawEncryptedWithPathFSR:error:"
+ "_refreshSnapshot:operationTracker:refreshState:fileToDomainCache:error:"
+ "_removeHardLinkedFilesForVolumeTransition:"
+ "_setIsAutoBackupOnCellularAllowed:"
+ "_setIsBackupOnCellularEnabled:"
+ "_setIsEnabled:"
+ "_setIsLocked:"
+ "_setIsOnCellular:"
+ "_setIsOnExpensiveCellular:"
+ "_setIsOnPower:"
+ "_setIsOnWiFi:"
+ "_setLastOnConditionEvents:account:"
+ "_setProtectionClass:withPath:"
+ "_snapshotFormatForAccount:behaviorOptionsFormat:previousSnapshot:"
+ "_snapshotFormatForAccount:previousSnapshot:error:"
+ "assetDecrypterWithTracker:device:error:"
+ "assetFetcherWithTracker:device:error:"
+ "checkIfCloudAccountModificationIsAllowed:"
+ "checkIfCloudBackupIsAllowed:"
+ "checkIfDiagnosticTelemetryIsAllowed:"
+ "checkIfDriveBackupIsAllowed:"
+ "checkIfDriveRestoreIsAllowed:"
+ "decrypt:restorable:metadata:error:"
+ "depositWithAsset:assetPath:error:"
+ "fcntl error setting Cx protection class"
+ "fetcher:didReceiveAsset:path:"
+ "initWithIdentifier:destinationPath:policy:depot:decrypter:progressModel:logger:error:"
+ "initWithRootPath:policy:depot:fetcher:decrypter:plan:progress:verifier:logger:error:"
+ "placeAsset:isHardlink:metadata:error:"
+ "q40@0:8@16q24@32"
+ "restoreWithDomain:rootPath:snapshotUUID:deviceUUID:verified:account:connection:error:"
+ "sharedPolicy"
+ "snapshotFormatForAccount:previousSnapshot:error:"
+ "v40@0:8@\"<MBAssetFetcher>\"16@\"MBFetchedAsset\"24@\"NSString\"32"
+ "\xa1"
- "\x05R"
- "\x05\x97G"
- "\n SELECT Domains.domain, \nRestorables.domainID, \ninode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, \nxattrs, \nrelativePath, \nrestorableID\n FROM   Restorables\n  JOIN  Domains ON\n       (Restorables.domainID = Domains.domainID)\n WHERE  Restorables.absolutePath = %@;"
- "\n SELECT Restorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u LIMIT 1"
- "\n SELECT Restorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableSymlinkTargets.targetPath, \nRestorableSymlinkTargets.linkCount, \nRestorables.restorableID\n  FROM  Restorables\n   JOIN RestorableSymlinkTargets ON\n       (RestorableSymlinkTargets.inode = Restorables.inode\n    AND RestorableSymlinkTargets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.assetSignature, \nRestorableAssets.assetType, \nRestorableAssets.compressionMethod\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size != 0 LIMIT 1"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.assetSignature, \nRestorableAssets.assetType, \nRestorableAssets.compressionMethod\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE absolutePath IS %@\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  restoreState = %u\n   AND  size = 0"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.assetSignature, \nRestorableAssets.assetType, \nRestorableAssets.compressionMethod\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size != 0"
- "\n SELECT Restorables.restorableID, \nRestorables.inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \nRestorableAssets.linkCount, \nRestorableAssets.assetSignature, \nRestorableAssets.assetType, \nRestorableAssets.compressionMethod\n FROM   Restorables\n  JOIN  RestorableAssets ON \n       (RestorableAssets.inode = Restorables.inode\n    AND RestorableAssets.domainID = Restorables.domainID\n       )\n  WHERE restoreState = %u\n   AND  Restorables.domainID = %llu\n   AND  type = %u\n   AND  size = 0"
- "\n SELECT inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  absolutePath IS %@\n  AND   domainID = %llu\n  AND   restoreState = %u\n LIMIT 1"
- "\n SELECT inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID ASC"
- "\n SELECT inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu\n  AND   restoreState = %u\n  AND   type = %u\n ORDER BY restorableID DESC"
- "\n SELECT inode, size, birth, modified, statusChanged, userID, groupID, mode, flags, protectionClass, xattrs, relativePath, \npriority, \nrestorableID\n FROM   Restorables\n WHERE  domainID = %llu;"
- "\nSELECT RestorableAssets.inode, \nlinkCount, \nrecordIDSuffix, encryptionKey, compressionMethod, assetType, assetSize, assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u\n GROUP BY RestorableAssets.inode;"
- "\nSELECT RestorableAssets.inode, \nlinkCount, \nrecordIDSuffix, encryptionKey, compressionMethod, assetType, assetSize, assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE Restorables.absolutePath IS %@\n   AND RestorableAssets.domainID = %llu\n   AND (RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu OR RestorableAssets.assetState = %lu)\n   AND Restorables.restoreState = %u LIMIT 1"
- " as Class B since device is locked"
- "%@-%llu.%@"
- "+[MBAssetRecordFetcher assetFetcherWithOperationTracker:device:error:]"
- "-[MBAssetRecordFetcher _decrypterFor:error:]"
- "-[MBAssetRecordFetcher _handleAssetFetchResponseFor:decrypter:record:withFetchError:]"
- "-[MBBackupScheduler initWithServiceManager:]"
- "-[MBBackupScheduler initWithServiceManager:]_block_invoke"
- "-[MBCKBackupEngine _snapshotFormatForAccount:error:]"
- "-[MBRestoreDomainEngine fetcher:didReceiveAsset:decrypter:path:]"
- "-[MBRestoreDomainEngine initWithRootPath:policy:depot:fetcher:plan:progress:verifier:logger:error:]"
- "-[_AssetDecrypter _initWith:asset:]"
- "-[_AssetDecrypter _keybag:]"
- "-[_AssetDecrypter decrypt:error:]"
- "=asset-fetch= Decrypting file in place at %@ with keybag %@"
- "=asset-fetch= Failed to decrypt file at %@, asset:%@, on-disk:%@: %@"
- "=asset-fetch= Failed to find a keybag to decrypt file at %@: %@"
- "=asset-fetch= Failed to get UUID from encryption key for file %@"
- "=asset-fetch= Failed to get file info for %@: %@"
- "=asset-fetch= Failed to save device record with recovered keybag %{public}@: %@"
- "=asset-fetch= Failed to unlock keybag to decrypt file at %@: %@"
- "=asset-fetch= Missing encryption key for %@"
- "=asset-fetch= No keybag found for %{public}@: %@"
- "=cloud-backup= Account disabled in EDU mode"
- "=cloud-backup= Failed to load domains to back up"
- "=domain repair= Found domainHMACsToRepair on device record: %@"
- "=scheduler= Received \"%{public}@\" notification for account %{public}@: %@"
- "=transcribing= Reusing asset %@ for %@:%@ because of metadata-only change 0x%lx (isTransitioningVolumeUUIDs %d)"
- "@\"MBAssetRecordFetcher\""
- "@\"_TtC7backupd14MBFetchedAsset\""
- "@28@0:8C16r*20"
- "@72@0:8@16@24@32@40@48@56^@64"
- "@88@0:8@16@24@32@40@48@56@64@72^@80"
- "Account disabled in EDU mode"
- "B32@0:8^@16@?<Q@?@\"<MBRestorable>\"Qc@\"NSData\"B^@>24"
- "B56@0:8@16Q24c32@36B44^@48"
- "B72@0:8@16@24@32@40@48@56^@64"
- "Backup disabled for this device"
- "Cannot restore domain root %@ for %@ as symlink"
- "Creating empty file at %@"
- "Creating symbolic link: %@"
- "Deposited asset (ino: "
- "Directory already exists"
- "Doing a Userspace reboot"
- "Doing a full reboot"
- "Failed to clone from %@ to %@: %{errno}d"
- "Failed to decrypt "
- "Failed to hardlink from %@ to %@: %{errno}d"
- "Failed to move encrypted asset into asset processing path "
- "Failed to move from %@ to %@: %@"
- "Failed to resolve On My iPhone file conflict from %@ to %@(%ld): %@"
- "Failed to restore BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore directory BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore protection class %d instead of %d at %@: %@"
- "Failed to restore regular file BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore symlink BSD flags (0x%x) at %@: %{errno}d"
- "Failed to set protection class %d at %@: %@"
- "Fixing ownership at %@"
- "Idled. Stopping service."
- "MBChangedBackupConditions"
- "MBDaemonIdleTimerInterval=%ld"
- "MBEncodingPath"
- "Making directory at %@ (0%3o)"
- "Making directory: 0%3o"
- "Metadata mismatch [%@] for %@ %@:\n\tlocal: %@\n\tcloud: %@"
- "Missing decrypter for "
- "Missing encryption key for %@"
- "Not changing the \"%{public}@\" state on account %{public}@ since the device is in EDU mode"
- "Not re-applying the com.apple.decmpfs xattr yet."
- "Not rebooting after restore because %@ %@ preference is set"
- "Not restoring protection class for symlink at %@"
- "Over-released work assertion: %s"
- "Q48@?0@\"<MBRestorable>\"8Q16c24@\"NSData\"28B36^@40"
- "Removing existing %@"
- "Removing existing object %@"
- "Restoring BSD flags: 0x%x"
- "Restoring attributes u/gid %d/%d, b/m/c/atime %ld/%ld/%ld/%ld, permissions 0%o to %@"
- "Restoring directory BSD flags: 0x%x"
- "Restoring directory extended attributes (%ld) at path %@"
- "Restoring directory ownership: %d:%d at path %@"
- "Restoring directory permissions: 0%3o"
- "Restoring last modified time (%@) at %@"
- "Restoring last modified time (%@) for %@"
- "Restoring protection class %d at %@"
- "Restoring protection class %d instead of %d for: %@"
- "Restoring protection class: %d for path: %s"
- "Restoring regular file BSD flags: 0x%x at %@"
- "Restoring regular file extended attributes (%ld) at %@"
- "Restoring regular file ownership: %d:%d at %@"
- "Restoring regular file permissions: 0%3o at %@"
- "Restoring symbolic link extended attributes"
- "Restoring symbolic link ownership: %d:%d"
- "Restoring symbolic link permissions: 0%3o"
- "Restoring symlink BSD flags: 0x%x"
- "SIGHUP"
- "SIGQUIT"
- "SIGTERM"
- "SIGUSR2"
- "Successfully resolved On My iPhone file conflict from %@ to %@(%ld)"
- "T@\"<NSObject>\",&,N,V_backupObserver"
- "T@\"MBCKOperationTracker\",R,N,V_tracker"
- "Td,N,V_backupPeriod"
- "The hashes of existing file and restoring file are the same. Skip re-restoring On My iPhone file at %@"
- "T{?=BBBBBBBB},R,N"
- "Unexpected device lock error for pc:%d"
- "Unexpected nil extended attribute com.apple.decmpfs for dataless file: %@"
- "Unhandled signal %d"
- "Unspecified data class for %@ -> defaulting to %d"
- "Using APFSIOC_MAKE_OBJECT_DATALESS to restore the com.apple.decmpfs xattr on %@: %@"
- "[account isKindOfClass:MBServiceAccount.class]"
- "[error isKindOfClass:NSError.class]"
- "_asset"
- "_backupObserver"
- "_backupPeriod"
- "_decrypterFor:error:"
- "_handleAssetFetchResponseFor:decrypter:record:withFetchError:"
- "_initWith:asset:"
- "_isAccountModificationDisabledByRestrictions"
- "_isAutoBackupOnCellularAllowedChanged"
- "_isBackupOnCellularEnabledChanged"
- "_isCloudBackupRestricted"
- "_isEnabledChanged"
- "_isLockedChanged"
- "_isOnCellularChanged"
- "_isOnExpensiveCellularChanged"
- "_isOnPowerChanged"
- "_isOnWiFiChanged"
- "_keybag:"
- "_keybagUUIDString"
- "_setProtectionClass:withPathFSR:"
- "_snapshotFormatForAccount:behaviorOptionsFormat:"
- "_snapshotFormatForAccount:error:"
- "assetFetcherWithOperationTracker:device:error:"
- "b1"
- "backupObserver"
- "backupPeriod"
- "com.apple.backup.scheduler.backupFinished"
- "decrypt:error:"
- "decrypted_asset_cas_by_signature"
- "depositWithAsset:decrypter:assetPath:error:"
- "fetcher:didReceiveAsset:decrypter:path:"
- "finfo->dstream_exists"
- "fsctl(APFSIOC_MAKE_OBJECT_DATALESS) failed at %@: %{errno}d"
- "fstatat failed at %s (%ld): %{errno}d"
- "holdWorkAssertion: %s, %d"
- "initWithIdentifier:destinationPath:policy:depot:progressModel:logger:error:"
- "initWithRootPath:policy:depot:fetcher:plan:progress:verifier:logger:error:"
- "initWithServiceManager:"
- "isAutoBackupOnCellularAllowed"
- "isBackupDisabledByMCPolicy"
- "isDiagnosticSubmissionAllowed"
- "isEphemeralMultiUser"
- "isLocked"
- "isOnCellular"
- "isOnExpensiveCellular"
- "isOnPower"
- "object"
- "openRawEncryptedWithPath:error:"
- "openRawEncryptedWithPathFSR:error:"
- "placeAsset:assetType:compressionMethod:assetSignature:isHardlink:error:"
- "q32@0:8@16q24"
- "reboot3 failed: %d"
- "releaseWorkAssertion: %s, %d"
- "restoreWithDomain:rootPath:snapshotUUID:deviceUUID:account:connection:error:"
- "setBackupObserver:"
- "setBackupPeriod:"
- "setIsAutoBackupOnCellularAllowed:"
- "setIsBackupOnCellularEnabled:"
- "setIsEnabled:"
- "setIsLocked:"
- "setIsOnCellular:"
- "setIsOnExpensiveCellular:"
- "setIsOnPower:"
- "setLastOnConditionEvents:account:"
- "snapshotFormatForAccount:error:"
- "v48@0:8@\"<MBAssetFetcher>\"16@\"MBFetchedAsset\"24@\"<MBAssetDecrypter>\"32@\"NSString\"40"
- "\x91"

```
