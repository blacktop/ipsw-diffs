## MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0xaa04
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x4b0
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x210
-  __TEXT.__cstring: 0x2273
-  __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x194d
-  __TEXT.__objc_methtype: 0x2bd
-  __TEXT.__oslogstring: 0x11ac
-  __TEXT.__unwind_info: 0x208
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_catlist: 0x10
+2624.100.67.0.0
+  __TEXT.__text: 0x12288
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x1ec0
+  __TEXT.__objc_methlist: 0x7e0
+  __TEXT.__const: 0x1a0
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__cstring: 0x3cc1
+  __TEXT.__oslogstring: 0x1ec6
+  __TEXT.__objc_methname: 0x23f7
+  __TEXT.__objc_classname: 0xd8
+  __TEXT.__objc_methtype: 0x3bf
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__cfstring: 0x1060
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5c8
-  __DATA.__objc_selrefs: 0x6f8
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x140
-  __DATA.__bss: 0x48
+  __DATA.__objc_const: 0x908
+  __DATA.__objc_selrefs: 0x9a0
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0x230
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 190
-  Symbols:   146
-  CStrings:  638
+  Functions: 321
+  Symbols:   182
+  CStrings:  989
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _MBMobileUID
+ _MBSQLiteJournalSuffixes
+ _MBStringWithDate
+ _NSFileSystemSize
+ _NSURLCreationDateKey
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSUUID
+ _chown
+ _free
+ _fs_snapshot_create
+ _fs_snapshot_delete
+ _fs_snapshot_list
+ _fs_snapshot_mount
+ _fs_snapshot_rename
+ _fsctl
+ _getfsstat
+ _kCFAbsoluteTimeIntervalSince1970
+ _mkdtemp
+ _mktemp
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_sync_enter
+ _objc_sync_exit
+ _realpath$DARWIN_EXTSN
+ _removefile_state_alloc
+ _removefile_state_free
+ _removefile_state_get
+ _removefile_state_set
+ _removefileat
+ _rename
+ _sleep
+ _snprintf
+ _statfs
+ _strcmp
+ _strdup
+ _unmount
- _MBCreateTemporaryFilePathIn
- _MBRemoveTemporaryDirectory
- _OBJC_CLASS_$_MBFileSystemManager
- _OBJC_CLASS_$_MBTemporaryDirectory
CStrings:
+ "\x02"
+ "\x03"
+ "%s/%s_XXXXXXXXXXXXXXX"
+ "%s/XXXXXXXXXXXXXXX"
+ "*"
+ "+[MBFileSystemManager createAndMountSnapshotForVolume:name:atFirstAvailableMountPoint:error:cancelationHandler:]"
+ "+[MBFileSystemManager deleteAllSnapshotsForVolume:withPrefix:latestCreationDate:error:]"
+ "+[MBFileSystemManager listSnapshotsForVolume:error:]"
+ "+[MBFileSystemManager startFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager stopFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager volumeUUIDWithVolumeMountPoint:error:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:]"
+ "+[MBTemporaryDirectory temporaryDirectoryOnSameVolumeAsPath:identifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
+ ", "
+ "-[MBTemporaryDirectory _initWithExistingFsRepPath:identifier:]"
+ "-[NSFileManager(MobileBackup) _pathsRootedAt:subpaths:]"
+ "-[NSFileManager(MobileBackup) _tryMovingThenRemovingItemAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_migrateIfNeededFromSource:sourceSubPaths:toDestination:destinationSubPaths:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveAsideAndMarkPurgeableDBFilesAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveAsideItemAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveToTmpDirThenRemoveItemAtPath:error:]"
+ "/.b/0"
+ "/.b/1"
+ "/.b/4"
+ "/.b/5"
+ "/.b/6"
+ "/.b/7"
+ "/var/mobile"
+ "/var/mobile/Library/Caches/Backup"
+ "/var/mobile/Library/Caches/Backup/DT"
+ "/var/mobile/tmp/com.apple.backup.testing"
+ "/var/tmp/com.apple.backup"
+ "/var/tmp/com.apple.backup.testing"
+ "<%@: name=\"%@\", uuid=%@, creationDate=\"%@\"(%.3f)>"
+ "<%s: %@, path: %s>"
+ "=mbfm= =purge= Failed to mark %{public}@ as purgeable: %@"
+ "=mbfm= =purge= Marked %{public}@ as purgeable"
+ "=mbfm= Failed to mark DB %@ as purgeable: %@"
+ "=mbfm= Failed to move aside DB file %@: %@"
+ "=mbfm= Moved aside DB file %@ to %@"
+ "=mbfm= Updating plist at %@ to %@"
+ "=mbfm= ma: Moved aside %{public}@ to %{public}@"
+ "=mbfm= ma: Unable to move aside %{public}@ to %{public}@: %@"
+ "=mbfm= mg: Cleaning up un-migrated (%{public}@) from %{public}@, already present in %{public}@"
+ "=mbfm= mg: Migrating (%{public}@) from %{public}@ to %{public}@"
+ "=mbfm= mg: Nothing to migrate from %{public}@ to %{public}@"
+ "=mbfm= mg: Nothing to migrate from %{public}@, already present in %{public}@"
+ "=mbfm= rm: Created move-aside temp dir: %@"
+ "=mbfm= rm: Nothing at %{public}@ to move to temporary cleanup dir %{public}@"
+ "=mbfm= rm: Nothing at %{public}@ to remove"
+ "=mbfm= rm: Removed %{public}@ in place"
+ "=mbfm= rm: Removing temporary cleanup dir %{public}@"
+ "=mbfm= rm: Unable to create temporary cleanup dir, removing %{public}@ in place: %{public}@"
+ "=mbfm= rm: Unable to move %{public}@ to temporary cleanup dir %{public}@: %@"
+ "=mbfm= rm: moved item at %{public}@ to temp cleanup dir %{public}@"
+ "=tmpdir= %@ failed to create new contents directory: %@"
+ "=tmpdir= %@ failed to move contents aside to purge: %@"
+ "=tmpdir= %@ was not disposed before dealloc"
+ "=tmpdir= Failed to create %s directory (mkdtemp error: %d)"
+ "=tmpdir= could not find mount point for %@: %@"
+ "=tmpdir= failed to delete %@: %@"
+ "@\"NSDate\""
+ "@32@0:8*16@24"
+ "@32@0:8@16@?24"
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32^@40@?48"
+ "B16@?0@\"MBFileSystemSnapshot\"8"
+ "B24@?0Q8^@16"
+ "B32@0:8@16@24"
+ "B40@0:8@?16Q24^@32"
+ "B48@0:8@16@24^@32@?40"
+ "B48@0:8@16d24^@32@?40"
+ "B52@0:8i16@20@28@36^@44"
+ "B52@0:8i16@20@28^@36@?44"
+ "B56@0:8@16@24@32@40^@48"
+ "B56@0:8@16d24d32^@40@?48"
+ "Cancelled while trying to unmount %@"
+ "Couldn't get attr list for filesystem path %@"
+ "Created filesystem snapshot %{public}@ at %{public}@ in %.3fs"
+ "Creating filesystem snapshot %{public}@ at %{public}@"
+ "Deleted snapshot %{public}@ at %{public}@"
+ "Deleted snapshot: %{public}@"
+ "Failed to create filesystem snapshot %{public}@ at %{public}@ (%d): %{errno}d"
+ "Failed to create filesystem snapshot %{public}@ at %{public}@ (canceled)"
+ "Failed to create snapshot"
+ "Failed to create snapshot: %d"
+ "Failed to delete snapshot %{public}@ at %{public}@: %{errno}d"
+ "Failed to fetch attributes at %@: %@"
+ "Failed to get NSURLCreationDateKey for %@: %@"
+ "Failed to get NSURLIsDirectoryKey for %@: %@"
+ "Failed to get filesystem capacity at \"%@\": %@"
+ "Failed to list file system snapshots at %{public}@: %{public}@"
+ "Failed to mark item purgeable"
+ "Failed to open %{public}@: %{errno}d"
+ "Failed to open snapshot path"
+ "Failed to read attributes for directory entry: %{errno}d\n"
+ "Failed to read snapshot attributes"
+ "Failed to remove drive backup snapshot directory %@: %@"
+ "Failed to start APFS key rolling"
+ "Failed to stop APFS key rolling"
+ "Failed to unmount %llu/%llu snapshots"
+ "Found file system snapshot: %{public}@"
+ "Ignoring %@ since it was created at %.3f"
+ "Ignoring snapshot: %{public}@"
+ "Listing all snapshots at %{public}@"
+ "MBCreateTemporaryFilePathIn"
+ "MBFileSystemManager"
+ "MBFileSystemManager.m"
+ "MBFileSystemSnapshot"
+ "MBTemporaryDirectory"
+ "MBTemporaryDirectory.m"
+ "MBTemporaryPath"
+ "Mount point %@ is already in use"
+ "NSFileManager+MobileBackup.m"
+ "NSString *_mktemp(const char *)"
+ "No free mount points for APFS snapshot"
+ "No mountpoint specified from which to unmount the current snapshot"
+ "No snapshots to delete for %{public}@"
+ "Nothing to unmount"
+ "Nothing to unmount at %{public}@"
+ "Removed %@ in %.3fs"
+ "Removed drive backup snapshot directory: %@"
+ "Removing %@ created at %.3f"
+ "Retrying unmount for %@ after EBUSY"
+ "Snapshot %{public}@ not found at %{public}@"
+ "Snapshot not found"
+ "Started APFS key rolling for %{public}@"
+ "Stopped APFS key rolling for %{public}@"
+ "T@\"NSDate\",&,N,V_creationDate"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_uuid"
+ "TempDir: Failed to create %s directory (mkdtemp error: %d)"
+ "TempDir: Failed to create directory (mkdtemp error: %d)"
+ "TempDir: Unable to create %s directory (mkpath_np error: %d)"
+ "TempDir: Unable to create temp file path in %s (%d)"
+ "TempDir: Unable to set ownership on %s directory (chown error: %d)"
+ "TempDir: cannot be disposed multiple times %@"
+ "Timed out trying to unmount %@"
+ "UUIDString"
+ "Unable to delete snapshot"
+ "Unable to mount snapshot"
+ "Unable to mount snapshot %@ at mount point %s: %{errno}d"
+ "Unable to move to temporary cleanup dir"
+ "Unable to open %@: %{errno}d"
+ "Unable to open %@: %{errno}d while checking if FS supports snapshot"
+ "Unable to open snapshot path"
+ "Unable to rename snapshot"
+ "Unable to rename snapshot: %@ -> %@: %{errno}d"
+ "Unable to unmount snapshot"
+ "Unmounted %llu mount points"
+ "Unmounted snapshot at %{public}@"
+ "_"
+ "_anyPathExists:"
+ "_createSnapshotForVolumeFd:volumeMountPoint:name:error:cancelationHandler:"
+ "_creationDate"
+ "_deleteFileSystemSnapshots:block:"
+ "_deleteSnapshotForVolume:name:error:"
+ "_disposed"
+ "_fsRepPath"
+ "_identifier"
+ "_initWithExistingFsRepPath:identifier:"
+ "_migratePaths:to:error:"
+ "_mkdtemp"
+ "_mkpath_if_necessary"
+ "_mktemp"
+ "_mountSnapshotForVolumeFd:volumeMountPoint:name:mountPoint:error:"
+ "_moveItemAtPath:toTempDir:"
+ "_name"
+ "_path"
+ "_pathsRootedAt:subpaths:"
+ "_perform:times:error:"
+ "_purgeContentsAt:rPath:error:"
+ "_removeAllPaths:error:"
+ "_tryMovingThenRemovingItemAtPath:error:"
+ "_unmountWithRetry:startTime:timeout:error:cancelationHandler:"
+ "_uuid"
+ "addEntriesFromDictionary:"
+ "apfs"
+ "array"
+ "attributesOfFileSystemForPath:error:"
+ "char * _Nullable _mkdtemp(const char *, NSString *__strong, NSError *__autoreleasing *)"
+ "codeForNSError:"
+ "com.apple.backup"
+ "componentsJoinedByString:"
+ "createAndMountSnapshotForVolume:name:atFirstAvailableMountPoint:error:cancelationHandler:"
+ "createSnapshotForVolume:name:error:cancelationHandler:"
+ "creationDate"
+ "dataWithPropertyList:format:options:error:"
+ "dbPath"
+ "dealloc"
+ "deleteAllSnapshotsAcrossVolumes:withPrefix:error:"
+ "destinationDirectory.isAbsolutePath"
+ "dictionary"
+ "dictionaryWithContentsOfFile:"
+ "disposeWithError:"
+ "disposeWithoutDeleting"
+ "errnoForError:"
+ "errorWithCode:description:"
+ "errorWithErrno:format:"
+ "errorWithErrors:"
+ "fetchAllAPFSVolumeMountPoints"
+ "fgetattrlist failed at %{public}@: %{errno}d"
+ "fileSystemCapacity"
+ "fileURLWithPath:isDirectory:"
+ "fsRepPath"
+ "fs_snapshot_list failed"
+ "fs_snapshot_list failed at %{public}@: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_START) failed: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_STOP) failed: %{errno}d"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "identifier.length"
+ "initWithBytes:length:encoding:"
+ "initWithCapacity:"
+ "initWithName:uuid:creationDate:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "initWithUUIDBytes:"
+ "initWithUUIDString:"
+ "isAbsolutePath"
+ "isError:withCode:"
+ "iso8601String"
+ "latestCreationDate"
+ "listSnapshotsForVolume:error:"
+ "mb_markAsPurgeableItemAtPath:error:"
+ "mb_migrateIfNeededFromSource:sourceSubPaths:toDestination:destinationSubPaths:error:"
+ "mb_moveAsideAndMarkPurgeableDBFilesAtPath:error:"
+ "mb_moveAsideItemAtPath:error:"
+ "mb_savePlistAtPath:addingItems:removing:error:"
+ "mountPoints.count > 0"
+ "move-aside-cleanup"
+ "name"
+ "namePtr[nameLength - 1] == '\\0'"
+ "now"
+ "objectAtIndexedSubscript:"
+ "open error"
+ "open failed at %{public}@: %{errno}d"
+ "p <= attrBuf + sizeof(attrBuf)"
+ "parentDirectory"
+ "parentDirectoryPath"
+ "purgeContentsWithError:"
+ "removeItemAtURL:error:"
+ "removeObjectsForKeys:"
+ "removefileat() error"
+ "renameSnapshotForVolume:name:newName:error:"
+ "root"
+ "setByAddingObject:"
+ "setCreationDate:"
+ "setName:"
+ "setUuid:"
+ "setWithObjects:"
+ "sharedTemporaryDirectoryForTest:"
+ "sharedTemporaryDirectoryIdentifiedBy:"
+ "sourceDirectory.isAbsolutePath"
+ "sourceSubPaths.count == destinationSubPaths.count"
+ "startFilesystemKeyRollingWithPath:error:"
+ "statfs failed"
+ "stopFilesystemKeyRollingWithPath:error:"
+ "stringByAppendingPathExtension:"
+ "stringByAppendingString:"
+ "stringByDeletingLastPathComponent"
+ "subpaths"
+ "testName.length"
+ "timeIntervalSince1970"
+ "timeIntervalSinceReferenceDate"
+ "unmount failed at %{public}@: %{errno}d"
+ "unmount:error:"
+ "unmount:timeout:error:cancelationHandler:"
+ "unmountAndDeleteSnapshotForVolume:name:mountPoint:error:"
+ "unmountAndRenameSnapshotForVolume:name:mountPoint:newName:error:"
+ "userTemporaryDirectoryForPersona:identifiedBy:"
+ "userTemporaryDirectoryForTest:"
+ "uuid"
+ "void _mkpath_if_necessary(const char *)"
+ "volumeMountPointForFile:error:"
+ "volumeSupportsLocalSnapshots:"
+ "volumeUUID"
+ "volumeUUIDWithVolumeMountPoint:error:"
+ "writeToFile:options:error:"

```
