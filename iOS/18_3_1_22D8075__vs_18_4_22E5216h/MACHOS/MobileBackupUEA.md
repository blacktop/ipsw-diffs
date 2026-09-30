## MobileBackupUEA

> `/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x4438
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0xd8
-  __TEXT.__oslogstring: 0x6bc
-  __TEXT.__cstring: 0x9d7
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0xf50
-  __TEXT.__objc_methtype: 0x4a5
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x158
-  __DATA.__auth_got: 0x250
-  __DATA.__got: 0xb0
-  __DATA.__const: 0x1b8
-  __DATA.__cfstring: 0x2a0
-  __DATA.__objc_classlist: 0x8
+2624.100.98.0.0
+  __TEXT.__text: 0x92cc
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x12c0
+  __TEXT.__objc_methlist: 0x6b4
+  __TEXT.__const: 0x160
+  __TEXT.__oslogstring: 0xe5b
+  __TEXT.__cstring: 0x191a
+  __TEXT.__objc_classname: 0x85
+  __TEXT.__objc_methname: 0x18ac
+  __TEXT.__objc_methtype: 0x587
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__unwind_info: 0x220
+  __DATA.__auth_got: 0x368
+  __DATA.__got: 0x118
+  __DATA.__const: 0x2f0
+  __DATA.__cfstring: 0x7e0
+  __DATA.__objc_classlist: 0x18
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x18
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb48
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_const: 0x848
+  __DATA.__objc_selrefs: 0x6e0
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
-  __DATA.__bss: 0x8
+  __DATA.__objc_arraydata: 0x30
+  __DATA.__objc_arrayobj: 0x48
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 76
-  Symbols:   126
-  CStrings:  360
+  Functions: 143
+  Symbols:   189
+  CStrings:  618
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _MBD2DSnapshotMountPoints
+ _MBFinderSnapshotMountPoints
+ _MBLivePathFromSnapshotPath
+ _MBSnapshotName
+ _MBSnapshotNameWithCurrentDate
+ _MBSnapshotPathFromLivePath
+ _MBStringWithDate
+ _MBTemporaryPath
+ _MBiCloudUserSessionSnapshotMountPoints
+ _NSFileCreationDate
+ _NSFileSystemSize
+ _NSURLCreationDateKey
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_MBException
+ _OBJC_CLASS_$_MBFileSystemSnapshot
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_MBFileSystemManager
+ _OBJC_METACLASS_$_MBFileSystemSnapshot
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ ___error
+ _close
+ _dispatch_once
+ _dispatch_sync
+ _fgetattrlist
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
+ _objc_alloc_init
+ _objc_exception_throw
+ _objc_opt_class
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_retain_x4
+ _open
+ _realpath$DARWIN_EXTSN
+ _sleep
+ _snprintf
+ _statfs
+ _strcmp
+ _strdup
+ _unmount
CStrings:
+ "\x03"
+ "!snapshotPath || volumeMountPoint"
+ "%@-%@"
+ "%s/XXXXXXXXXXXXXXX"
+ "+[MBFileSystemManager createAndMountSnapshotForVolume:name:atFirstAvailableMountPoint:error:cancelationHandler:]"
+ "+[MBFileSystemManager deleteAllSnapshotsForVolume:withPrefix:latestCreationDate:error:]"
+ "+[MBFileSystemManager listSnapshotsForVolume:error:]"
+ "+[MBFileSystemManager startFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager stopFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager volumeUUIDWithVolumeMountPoint:error:]"
+ "/.b/0"
+ "/.b/1"
+ "/.b/4"
+ "/.b/5"
+ "/.b/6"
+ "/.b/7"
+ "/private"
+ "/private/var/"
+ "/var"
+ "/var/"
+ "/var/mobile"
+ "/var/mobile/Library/Caches/Backup"
+ "/var/mobile/Library/Caches/Backup/DT"
+ "/var/tmp/backupd-XXXXXXXXXXXXXXX"
+ "<%@: name=\"%@\", uuid=%@, creationDate=\"%@\"(%.3f)>"
+ "@\"NSDate\""
+ "@\"NSString\""
+ "@32@0:8@16@?24"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32^@40@?48"
+ "B16@?0@\"MBFileSystemSnapshot\"8"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "B48@0:8@16@24@32^@40"
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
+ "Failed to open %{public}@: %{errno}d"
+ "Failed to open snapshot path"
+ "Failed to read attributes for directory entry: %{errno}d\n"
+ "Failed to read snapshot attributes"
+ "Failed to remove %@: %@"
+ "Failed to remove drive backup snapshot directory %@: %@"
+ "Failed to start APFS key rolling"
+ "Failed to stop APFS key rolling"
+ "Failed to unmount %llu/%llu snapshots"
+ "Found file system snapshot: %{public}@"
+ "Ignoring %@ since it was created at %.3f"
+ "Ignoring snapshot: %{public}@"
+ "Listing all snapshots at %{public}@"
+ "MBFileSystemManager"
+ "MBFileSystemManager.m"
+ "MBFileSystemSnapshot"
+ "MBSnapshotPathFromLivePath"
+ "MBTempPathUtils.m"
+ "MBTemporaryPath"
+ "Mount point %@ is already in use"
+ "NSString *MBTemporaryPath(void)"
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
+ "Timed out trying to unmount %@"
+ "UUIDString"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"
+ "Unable to delete snapshot"
+ "Unable to mount snapshot"
+ "Unable to mount snapshot %@ at mount point %s: %{errno}d"
+ "Unable to obtain MBTemporaryPath()"
+ "Unable to open %@: %{errno}d"
+ "Unable to open %@: %{errno}d while checking if FS supports snapshot"
+ "Unable to open snapshot path"
+ "Unable to rename snapshot"
+ "Unable to rename snapshot: %@ -> %@: %{errno}d"
+ "Unable to unmount snapshot"
+ "Unmounted %llu mount points"
+ "Unmounted snapshot at %{public}@"
+ "_createSnapshotForVolumeFd:volumeMountPoint:name:error:cancelationHandler:"
+ "_creationDate"
+ "_deleteFileSystemSnapshots:block:"
+ "_deleteSnapshotForVolume:name:error:"
+ "_mountSnapshotForVolumeFd:volumeMountPoint:name:mountPoint:error:"
+ "_name"
+ "_unmountWithRetry:startTime:timeout:error:cancelationHandler:"
+ "_uuid"
+ "apfs"
+ "arrayWithObjects:count:"
+ "attributesOfFileSystemForPath:error:"
+ "attributesOfItemAtPath:error:"
+ "characterAtIndex:"
+ "compare:"
+ "createAndMountSnapshotForVolume:name:atFirstAvailableMountPoint:error:cancelationHandler:"
+ "createSnapshotForVolume:name:error:cancelationHandler:"
+ "creationDate"
+ "currentHandler"
+ "deleteAllSnapshotsAcrossVolumes:withPrefix:error:"
+ "deleteAllSnapshotsForVolume:withPrefix:latestCreationDate:error:"
+ "en_US_POSIX"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "error"
+ "errorWithCode:description:"
+ "errorWithCode:path:format:"
+ "errorWithErrno:format:"
+ "errorWithErrno:path:format:"
+ "errorWithErrors:"
+ "fetchAllAPFSVolumeMountPoints"
+ "fgetattrlist failed at %{public}@: %{errno}d"
+ "fileExistsAtPath:"
+ "fileSystemCapacity"
+ "fileSystemRepresentation"
+ "fileURLWithPath:isDirectory:"
+ "fs_snapshot_list failed"
+ "fs_snapshot_list failed at %{public}@: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_START) failed: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_STOP) failed: %{errno}d"
+ "getResourceValue:forKey:error:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "initWithBytes:length:encoding:"
+ "initWithCapacity:"
+ "initWithCode:format:"
+ "initWithFormat:"
+ "initWithName:uuid:creationDate:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "initWithUTF8String:"
+ "initWithUUIDBytes:"
+ "initWithUUIDString:"
+ "isEqualToString:"
+ "lastPathComponent"
+ "latestCreationDate"
+ "length"
+ "listSnapshotsForVolume:error:"
+ "localTimeZone"
+ "localeWithLocaleIdentifier:"
+ "mb_moveToTmpDirThenRemoveItemAtPath:error:"
+ "mb_stringWithFileSystemRepresentation:"
+ "mktemp failed: %{errno}d"
+ "mountPoints.count > 0"
+ "name"
+ "namePtr[nameLength - 1] == '\\0'"
+ "open error"
+ "open failed at %{public}@: %{errno}d"
+ "p <= attrBuf + sizeof(attrBuf)"
+ "r.location == 0 && 0 < r.length"
+ "range.location == 0"
+ "rangeOfString:"
+ "removeDeviceTransferDirectoryWithEarliestCreationDate:"
+ "removeDriveBackupSnapshotsWithLatestCreationDate:"
+ "removeItemAtURL:error:"
+ "renameSnapshotForVolume:name:newName:error:"
+ "replaceSnapshotMountPointPrefix"
+ "setCreationDate:"
+ "setDateFormat:"
+ "setLocale:"
+ "setName:"
+ "setTimeZone:"
+ "setUuid:"
+ "setWithObjects:"
+ "startFilesystemKeyRollingWithPath:error:"
+ "statfs failed"
+ "stopFilesystemKeyRollingWithPath:error:"
+ "stringByReplacingCharactersInRange:withString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "substringFromIndex:"
+ "timeIntervalSince1970"
+ "timeIntervalSinceReferenceDate"
+ "unmount failed at %{public}@: %{errno}d"
+ "unmount:error:"
+ "unmount:timeout:error:cancelationHandler:"
+ "unmountAndDeleteSnapshotForVolume:name:mountPoint:error:"
+ "unmountAndRenameSnapshotForVolume:name:mountPoint:newName:error:"
+ "unsignedLongLongValue"
+ "uuid"
+ "volumeMountPointForFile:error:"
+ "volumeSupportsLocalSnapshots:"
+ "volumeUUID"
+ "volumeUUIDWithVolumeMountPoint:error:"
+ "yyyy-MM-dd.HH:mm:ss"
- "manager:didFinishDeviceTransferPreflight:error:"
- "v40@0:8@\"MBManager\"16@\"MBDeviceTransferPreflight\"24@\"NSError\"32"

```
