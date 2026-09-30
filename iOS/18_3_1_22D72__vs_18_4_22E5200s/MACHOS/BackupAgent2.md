## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x9535c
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0xdbc0
-  __TEXT.__objc_methlist: 0x69bc
-  __TEXT.__const: 0x438
-  __TEXT.__cstring: 0x1b6ff
-  __TEXT.__oslogstring: 0xcf73
-  __TEXT.__objc_methname: 0x100d7
-  __TEXT.__objc_classname: 0xab5
-  __TEXT.__objc_methtype: 0x233b
-  __TEXT.__gcc_except_tab: 0x22c4
-  __TEXT.__unwind_info: 0x1960
-  __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0x558
+2624.100.67.0.0
+  __TEXT.__text: 0xa6474
+  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__objc_stubs: 0xe2c0
+  __TEXT.__objc_methlist: 0x7450
+  __TEXT.__const: 0x4b0
+  __TEXT.__cstring: 0x1de2a
+  __TEXT.__oslogstring: 0xe3e7
+  __TEXT.__objc_methname: 0x10cf6
+  __TEXT.__objc_classname: 0xb4e
+  __TEXT.__objc_methtype: 0x2386
+  __TEXT.__gcc_except_tab: 0x28e8
+  __TEXT.__unwind_info: 0x1da0
+  __DATA_CONST.__auth_got: 0xd10
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x14f0
-  __DATA_CONST.__cfstring: 0xafe0
-  __DATA_CONST.__objc_classlist: 0x3b0
-  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__const: 0x16f8
+  __DATA_CONST.__cfstring: 0xb7a0
+  __DATA_CONST.__objc_classlist: 0x3e8
+  __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x278
-  __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xb658
-  __DATA.__objc_selrefs: 0x4450
-  __DATA.__objc_ivar: 0x64c
-  __DATA.__objc_data: 0x24e0
+  __DATA.__objc_const: 0xb248
+  __DATA.__objc_selrefs: 0x4758
+  __DATA.__objc_ivar: 0x68c
+  __DATA.__objc_data: 0x2710
   __DATA.__data: 0x8d8
-  __DATA.__bss: 0x1d8
+  __DATA.__bss: 0x248
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2541
-  Symbols:   577
-  CStrings:  7506
+  Functions: 2943
+  Symbols:   603
+  CStrings:  8005
 
Symbols:
+ _MBGetLogDir
+ _MBIsInternalInstall
+ _NSFileSystemSize
+ _NSSelectorFromString
+ _NSURLCreationDateKey
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_NSUUID
+ __DefaultRuneLocale
+ ___maskrune
+ _chown
+ _fs_snapshot_create
+ _fs_snapshot_delete
+ _fs_snapshot_list
+ _fs_snapshot_mount
+ _fs_snapshot_rename
+ _getfsstat
+ _getpid
+ _kCFAbsoluteTimeIntervalSince1970
+ _memcpy
+ _mkdtemp
+ _mktemp
+ _objc_release_x2
+ _openat_dprotected_np
+ _posix_spawn
+ _posix_spawn_file_actions_addopen
+ _posix_spawn_file_actions_destroy
+ _posix_spawn_file_actions_init
+ _posix_spawnattr_destroy
+ _posix_spawnattr_init
+ _posix_spawnattr_setflags
+ _realpath$DARWIN_EXTSN
+ _removefile_state_alloc
+ _removefile_state_free
+ _removefile_state_get
+ _removefile_state_set
+ _removefileat
+ _setattrlistat
+ _snprintf
+ _statfs
+ _strdup
+ _strtol
+ _unmount
+ _waitpid
- _MBCreateTemporaryFilePathIn
- _MBD2DSnapshotMountPoints
- _MBFinderSnapshotMountPoints
- _MBLivePathFromSnapshotPath
- _MBRemoveTemporaryDirectory
- _MBSnapshotName
- _MBSnapshotPathFromLivePath
- _MBTemporaryPath
- _MGCopyAnswer
- _OBJC_CLASS_$_MBDebugContext
- _OBJC_CLASS_$_MBDomainManager
- _OBJC_CLASS_$_MBFileSystemManager
- _OBJC_CLASS_$_MBSystemDomainsVersions
- _OBJC_CLASS_$_MBTemporaryDirectory
- _OBJC_METACLASS_$_MBDomainManager
- _rmdir
- _setattrlist
CStrings:
+ "\x02\x11"
+ "\a\x13"
+ "!"
+ "!fileHandle || [path isEqualToString:_fileHandlePathForSnapshot]"
+ "!fileHandle || [path isEqualToString:_fileHandlePath]"
+ "!snapshotPath || volumeMountPoint"
+ "%02lx"
+ "%@ value is not a dictionary"
+ "%s books domains \"%{public}@\""
+ "%s domain \"%{public}@\""
+ "%s health domains \"%{public}@\""
+ "%s/%s_XXXXXXXXXXXXXXX"
+ "%s/XXXXXXXXXXXXXXX"
+ "%u%c%u"
+ "%u-%c-%u"
+ "+"
+ "+[MBDomainManager _readDomainsFromPlist:accountType:volumeMountPoint:error:]"
+ "+[MBFileSystemManager createAndMountSnapshotForVolume:name:atFirstAvailableMountPoint:error:cancelationHandler:]"
+ "+[MBFileSystemManager deleteAllSnapshotsForVolume:withPrefix:latestCreationDate:error:]"
+ "+[MBFileSystemManager listSnapshotsForVolume:error:]"
+ "+[MBFileSystemManager startFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager stopFilesystemKeyRollingWithPath:error:]"
+ "+[MBFileSystemManager volumeUUIDWithVolumeMountPoint:error:]"
+ "+[MBRestorableOperation move:fromSource:destination:destinationSize:conflictResolution:error:]"
+ "+[MBTelemetry submitEventName:event:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:]"
+ "+[MBTemporaryDirectory temporaryDirectoryOnSameVolumeAsPath:identifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
+ "-[MBDomainManager _initWithAccountType:volumeMountPoint:plistPath:error:]"
+ "-[MBFileScanner _foundFile:snapshotPath:stats:]"
+ "-[MBTemporaryDirectory _initWithExistingFsRepPath:identifier:]"
+ "-[NSFileManager(MobileBackup) _pathsRootedAt:subpaths:]"
+ "-[NSFileManager(MobileBackup) _tryMovingThenRemovingItemAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_migrateIfNeededFromSource:sourceSubPaths:toDestination:destinationSubPaths:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveAsideAndMarkPurgeableDBFilesAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveAsideItemAtPath:error:]"
+ "-[NSFileManager(MobileBackup) mb_moveToTmpDirThenRemoveItemAtPath:error:]"
+ "-[_CachedFileDescriptors _cachedFDForDomain:withSnapshotPath:error:]"
+ "-[_CachedFileDescriptors _cachedFDForPath:WithError:]"
+ "-p"
+ "/.b/0"
+ "/.b/1"
+ "/.b/4"
+ "/.b/5"
+ "/.b/6"
+ "/.b/7"
+ "/private/var/"
+ "/usr/sbin/lsof"
+ "/var"
+ "/var/"
+ "/var/mobile"
+ "/var/mobile/Library/Caches/Backup"
+ "/var/mobile/Library/Caches/Backup/DT"
+ "/var/mobile/tmp/com.apple.backup.testing"
+ "/var/tmp/backupd-XXXXXXXXXXXXXXX"
+ "/var/tmp/com.apple.backup"
+ "/var/tmp/com.apple.backup.testing"
+ "2"
+ "<%@: name=\"%@\", uuid=%@, creationDate=\"%@\"(%.3f)>"
+ "<%s: %@, path: %s>"
+ "=analytics= CA metrics have both success and failure recordings"
+ "=analytics= Failed to submit \"%{public}@\""
+ "=analytics= Submitting \"%{public}@\": %@"
+ "=analytics= Successfully submitted \"%{public}@\""
+ "=atc-bundles= %@: dataClass:\"%@\", Filtered appleIDs: %@"
+ "=diag=       0x%llx:+%lld (crid %llu)"
+ "=diag=       class:   %#x"
+ "=diag=       exists?  %u"
+ "=diag=       flags:   %#x"
+ "=diag=       len:     %u"
+ "=diag=       os:      %@"
+ "=diag=       payload: %u (trunc? %d)"
+ "=diag=       refcnt:  %u"
+ "=diag=       rev:     %u"
+ "=diag=       version: %u.%u"
+ "=diag=     class:   %#x"
+ "=diag=     exists?  %u"
+ "=diag=     flags:   %#x"
+ "=diag=     len:     %u"
+ "=diag=     os:      %@"
+ "=diag=     payload: %u (trunc? %d)"
+ "=diag=     refcnt:  %u"
+ "=diag=     rev:     %u"
+ "=diag=     version: %u.%u"
+ "=diag=   alloced_size: %llu"
+ "=diag=   default_crid: %llu"
+ "=diag=   num extents:  %u"
+ "=diag=   refcnt:       %u"
+ "=diag=   size:         %llu"
+ "=diag= Dstream id %llu, dstream size %llu bytes"
+ "=diag= Dumped lsof output to %@"
+ "=diag= Dumping crypto file info"
+ "=diag= Extent offset %lld and length %lld"
+ "=diag= Failed to mark item as purgeable at %@"
+ "=diag= Spawned /usr/sbin/lsof %s %s"
+ "=diag= lsof exited"
+ "=diag= lsof stopped"
+ "=diag= lsof was terminated by signal %d"
+ "=diag= posix_spawn() failed: %{errno}d"
+ "=diag= posix_spawn_file_actions_addopen() failed: %{errno}d"
+ "=diag= posix_spawn_file_actions_init() failed: %{errno}d"
+ "=diag= posix_spawnattr_setflags() failed: %{errno}d"
+ "=diag= private_id: %llu"
+ "=diag= prot_class: %llu (explicit? %d)"
+ "=diag= waitpid() failed: %{errno}d"
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
+ "=scanning= open failed at %@: %{errno}d"
+ "=tmpdir= %@ failed to create new contents directory: %@"
+ "=tmpdir= %@ failed to move contents aside to purge: %@"
+ "=tmpdir= %@ was not disposed before dealloc"
+ "=tmpdir= Failed to create %s directory (mkdtemp error: %d)"
+ "=tmpdir= could not find mount point for %@: %@"
+ "=tmpdir= failed to delete %@: %@"
+ "@\"<MBDomainManagerDelegate>\""
+ "@\"MBSystemDomainsVersions\""
+ "@\"NSFileHandle\""
+ "@28@0:8C16r*20"
+ "@32@0:8*16@24"
+ "@36@0:8S16@?20@?28"
+ "@40@0:8@16@24B32B36"
+ "@44@0:8@16@24@32B40"
+ "@48@0:8@16^Q24^Q32@40"
+ "@48@0:8@16q24@32^@40"
+ "@48@0:8q16@24@32^@40"
+ "@56@0:8@16@24@32^@40@?48"
+ "@60@0:8@16@24@32@40i48^{_MBFileScannerDomainStats=qqqQQQQQQ}52"
+ "@64@0:8@16@24@32@40@48^{_MBFileScannerDomainStats=qqqQQQQQQ}56"
+ "@64@0:8@16@24@32Q40q48^@56"
+ "@72@0:8@16@24@32i40@44@52i60^{_MBFileScannerDomainStats=qqqQQQQQQ}64"
+ "Account is marked as managed %@"
+ "AppDomain-com.apple.HealthPrivacyService"
+ "AppDomainPlugin-com.apple.Health.DiagnosticExtension"
+ "AppDomainPlugin-com.apple.Health.HealthShareExtension"
+ "B16@?0@\"MBFileSystemSnapshot\"8"
+ "B24@?0Q8^@16"
+ "B40@0:8@16d24@32"
+ "B40@0:8@?16Q24^@32"
+ "B44@0:8S16^@20@?28@?36"
+ "B48@0:8@16@24^@32@?40"
+ "B48@0:8@16d24^@32@?40"
+ "B52@0:8@16@24C32@36^@44"
+ "B52@0:8i16@20@28@36^@44"
+ "B52@0:8i16@20@28^@36@?44"
+ "B56@0:8@16d24d32^@40@?48"
+ "Cancelled while trying to unmount %@"
+ "Couldn't get attr list for filesystem path %@"
+ "Created filesystem snapshot %{public}@ at %{public}@ in %.3fs"
+ "Creating domain for uninstalled container %@"
+ "Creating filesystem snapshot %{public}@ at %{public}@"
+ "DataSeparatedDomains"
+ "Deleted snapshot %{public}@ at %{public}@"
+ "Deleted snapshot: %{public}@"
+ "Disabled domains: %@"
+ "Disabling"
+ "Domain already exists: %@"
+ "Domain for path \"%@\": domain=\"%@\", relativePath=\"%@\""
+ "Domain not found for redirect: %@"
+ "Domain plist value for key %@ is not a dictionary: %{public}@"
+ "Domains"
+ "Enabling"
+ "Error loading system domains from %@: %@"
+ "Failed creating temporary directory to download file: %@"
+ "Failed creating temporary directory to upload data: %@"
+ "Failed to compile regex: %@"
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
+ "Failed to load system domains from %@: %@"
+ "Failed to load the system domains at %{public}@: %{public}@"
+ "Failed to load the system domains plist at %{public}@: %{public}@"
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
+ "Hexadecimal"
+ "Ignoring %@ since it was created at %.3f"
+ "Ignoring snapshot: %{public}@"
+ "Listing all snapshots at %{public}@"
+ "Loaded system domains from %{public}@ (%.1f,%.1f,%.1f): %{public}@"
+ "Loaded system domains versions from %{public}@: (%.1f,%.1f,%.1f)"
+ "Loading system domains from %{public}@ %ld"
+ "Loading system domains versions from %{public}@"
+ "MBCreateTemporaryFilePathIn"
+ "MBDebugContext"
+ "MBDomainManager"
+ "MBDomainManager.m"
+ "MBFileSystemManager"
+ "MBFileSystemManager.m"
+ "MBFileSystemSnapshot"
+ "MBRestorableOperation"
+ "MBSnapshotPathFromLivePath"
+ "MBSplitPath"
+ "MBSystemDomainsVersions"
+ "MBTelemetry"
+ "MBTelemetry.m"
+ "MBTempPathUtils.m"
+ "MBTemporaryDirectory"
+ "MBTemporaryDirectory.m"
+ "MBTemporaryPath"
+ "MKBFileOpenForBackup"
+ "MaxSupportedVersion"
+ "MinSupportedVersion"
+ "Mount point %@ is already in use"
+ "NSFileManager+MobileBackup.m"
+ "NSString *MBTemporaryPath(void)"
+ "NSString *_mktemp(const char *)"
+ "No free mount points for APFS snapshot"
+ "No mountpoint specified from which to unmount the current snapshot"
+ "No snapshots to delete for %{public}@"
+ "Nothing to unmount"
+ "Nothing to unmount at %{public}@"
+ "Null name"
+ "Placeholder: Failed to archive placeholder for: %@ %@"
+ "Preference %@ %@ not a dictionary"
+ "Redirecting from %@ to %@: %@"
+ "Removed %@ in %.3fs"
+ "Removed drive backup snapshot directory: %@"
+ "Removing %@ created at %.3f"
+ "Removing domain %@ not matching regex (%@)"
+ "Removing domains not matching regex (%@)"
+ "Restricted domains: %@"
+ "Retrying unmount for %@ after EBUSY"
+ "Snapshot %{public}@ not found at %{public}@"
+ "Snapshot not found"
+ "Started APFS key rolling for %{public}@"
+ "Stopped APFS key rolling for %{public}@"
+ "SystemDomains"
+ "SystemDomains value not a dictionary"
+ "T@\"<MBDomainManagerDelegate>\",W,N,V_delegate"
+ "T@\"MBSystemDomainsVersions\",&,N,V_systemDomainsVersions"
+ "T@\"NSDate\",&,N,V_creationDate"
+ "T@\"NSDictionary\",&,N,V_systemDomainsByName"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSMutableDictionary\",&,N,V_domainsByName"
+ "T@\"NSString\",&,N,V_name"
+ "TempDir: Failed to create %s directory (mkdtemp error: %d)"
+ "TempDir: Failed to create directory (mkdtemp error: %d)"
+ "TempDir: Unable to create %s directory (mkpath_np error: %d)"
+ "TempDir: Unable to create temp file path in %s (%d)"
+ "TempDir: Unable to set ownership on %s directory (chown error: %d)"
+ "TempDir: cannot be disposed multiple times %@"
+ "Timed out trying to unmount %@"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
+ "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"
+ "Unable to delete snapshot"
+ "Unable to mount snapshot"
+ "Unable to mount snapshot %@ at mount point %s: %{errno}d"
+ "Unable to move to temporary cleanup dir"
+ "Unable to obtain MBTemporaryPath()"
+ "Unable to open %@: %{errno}d"
+ "Unable to open %@: %{errno}d while checking if FS supports snapshot"
+ "Unable to open snapshot path"
+ "Unable to rename snapshot"
+ "Unable to rename snapshot: %@ -> %@: %{errno}d"
+ "Unable to unmount snapshot"
+ "Unknown domain: %@"
+ "Unmounted %llu mount points"
+ "Unmounted snapshot at %{public}@"
+ "_"
+ "_CachedFileDescriptors"
+ "_anyPathExists:"
+ "_cachedFDForDomain:withSnapshotPath:error:"
+ "_cachedFDForPath:WithError:"
+ "_createSnapshotForVolumeFd:volumeMountPoint:name:error:cancelationHandler:"
+ "_creationDate"
+ "_deleteFileSystemSnapshots:block:"
+ "_deleteSnapshotForVolume:name:error:"
+ "_diagnoseFile"
+ "_dictionary"
+ "_disposed"
+ "_domainsByName"
+ "_fileHandleForSnapshot"
+ "_fileHandlePath"
+ "_fileHandlePathForSnapshot"
+ "_fsRepPath"
+ "_getNumberOfFileExtents"
+ "_identifier"
+ "_initWithAccountType:volumeMountPoint:plistPath:error:"
+ "_initWithExistingFsRepPath:identifier:"
+ "_initWithSystemDomains:versions:"
+ "_isUnencryptedLocal"
+ "_mb_openatWithMode:setupDir:itemAccessor:"
+ "_migratePaths:to:error:"
+ "_mkdtemp"
+ "_mkpath_if_necessary"
+ "_mktemp"
+ "_mountSnapshotForVolumeFd:volumeMountPoint:name:mountPoint:error:"
+ "_moveItemAtPath:toTempDir:"
+ "_name"
+ "_pathsRootedAt:subpaths:"
+ "_perform:times:error:"
+ "_purgeContentsAt:rPath:error:"
+ "_readDomainsFromPlist:accountType:volumeMountPoint:error:"
+ "_removeAllPaths:error:"
+ "_restoreDirectoryAttributes"
+ "_scanDirectory:domain:fds:domainDirFd:snapshotPath:relativePath:depth:stats:"
+ "_scanFilesForDomain:fds:snapshotPath:relativePath:stats:"
+ "_scanFilesUsingGetattrlistbulkForDomain:fds:snapshotPath:relativePath:stats:"
+ "_scanFilesUsingReaddirForDomain:fds:snapshotPath:relativePath:depth:stats:"
+ "_scanTree:forDomain:fds:snapshotPath:relativePath:stats:"
+ "_setEnabled:forDomainNames:persona:"
+ "_setProtectionClass:withPathFSR:"
+ "_systemDomainsByName"
+ "_systemDomainsVersions"
+ "_tryMovingThenRemovingItemAtPath:error:"
+ "_unmountWithRetry:startTime:timeout:error:cancelationHandler:"
+ "_usageOfDirectoryAtPath:count:size:options:"
+ "aa_isManagedAppleID"
+ "accountType != MBAccountTypeUnspecified"
+ "addDomain:forName:"
+ "addDomainsToBackUpToiCloudWithAppManager:manager:account:"
+ "allRestrictedDomainNames:account:"
+ "apfs"
+ "archivePlaceholderDomainWithPersonaIdentifier:intoDirectory:error:"
+ "attributesOfFileSystemForPath:error:"
+ "boolForName:"
+ "cachedFDForDomain:withSnapshotPath:error:"
+ "char * _Nullable _mkdtemp(const char *, NSString *__strong, NSError *__autoreleasing *)"
+ "com.apple.backup"
+ "createSnapshotForVolume:name:error:cancelationHandler:"
+ "dbPath"
+ "deleteAllSnapshotsAcrossVolumes:withPrefix:error:"
+ "deleteAllSnapshotsForVolume:withPrefix:latestCreationDate:error:"
+ "destinationDirectory.isAbsolutePath"
+ "dictionaryWithContentsOfURL:error:"
+ "disposeWithError:"
+ "disposeWithoutDeleting"
+ "domainsByName"
+ "doubleFromStringValueForKey:plist:"
+ "drive-download-data"
+ "drive-upload-data"
+ "eventName && event"
+ "fetchAllAPFSVolumeMountPoints"
+ "fgetattrlist failed at %{public}@: %{errno}d"
+ "fsRepPath"
+ "fs_snapshot_list failed"
+ "fs_snapshot_list failed at %{public}@: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_START) failed: %{errno}d"
+ "fsctl(APFS_KEY_ROLLING_STOP) failed: %{errno}d"
+ "fsetattrlist() failed"
+ "groupInTransaction:transaction:"
+ "i40@0:8@16@24^@32"
+ "identifier.length"
+ "initForTestingWithDomains:"
+ "initForTestingWithPersona:systemDomainsPlistAtPath:"
+ "initWithBytes:length:encoding:"
+ "initWithDictionary:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithName:uuid:creationDate:"
+ "initWithPattern:options:error:"
+ "initWithSystemDomains:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "initWithUUIDBytes:"
+ "initWithUUIDString:"
+ "initWithVersion:minSupportedVersion:maxSupportedVersion:"
+ "iso8601String"
+ "latestCreationDate"
+ "listSnapshotsForVolume:error:"
+ "lsof"
+ "lsof-%@-%@.log"
+ "mb_base64EncodedFileSystemPathString"
+ "mb_hexadecimalString"
+ "mb_markAsPurgeableItemAtPath:error:"
+ "mb_migrateIfNeededFromSource:sourceSubPaths:toDestination:destinationSubPaths:error:"
+ "mb_moveAsideItemAtPath:error:"
+ "mb_openatWithMode:error:setupDir:itemAccessor:"
+ "mb_savePlistAtPath:addingItems:removing:error:"
+ "mb_stringByAppendingSlash"
+ "mktemp failed: %{errno}d"
+ "mountPoints.count > 0"
+ "move-aside-cleanup"
+ "move:fromSource:destination:destinationSize:conflictResolution:error:"
+ "namePtr[nameLength - 1] == '\\0'"
+ "nonContainerizedDomainWithName:plist:accountType:volumeMountPoint:"
+ "open failed"
+ "open failed at %{public}@: %{errno}d"
+ "open_dprotected_np"
+ "openat"
+ "openat() error"
+ "openat_dprotected_np() error"
+ "p <= attrBuf + sizeof(attrBuf)"
+ "parentDirectory"
+ "parentDirectoryPath"
+ "performSelectorForName:"
+ "performWithConnection:accessor:"
+ "pread"
+ "purgeContentsWithError:"
+ "r.location == 0 && 0 < r.length"
+ "range.location == 0"
+ "rangeOfString:"
+ "relativePathDomainRedirects"
+ "removeDeviceTransferDirectoryWithEarliestCreationDate:"
+ "removeDomains:"
+ "removeDomainsNotMatchingRegex:"
+ "removeDriveBackupSnapshotsWithLatestCreationDate:"
+ "removeItemAtURL:error:"
+ "removeValueForName:"
+ "removefileat() error"
+ "renameSnapshotForVolume:name:newName:error:"
+ "replaceSnapshotMountPointPrefix"
+ "restore:attributesToDestination:error:"
+ "restore:directoryAtPath:settingDataProtection:settingOwnershipAndFlags:"
+ "restore:emptyRegularFileAtPath:settingAttributes:"
+ "restore:protectionClassToDestination:unspecifiedDirectoryProtectionClass:logger:error:"
+ "restore:regularFileAtPath:settingAttributes:"
+ "restore:symbolicLinkAtPath:withTarget:settingOwnershipAndFlags:"
+ "root"
+ "setByAddingObject:"
+ "setCreationDate:"
+ "setDelegate:andSelector:forName:"
+ "setDomainsByName:"
+ "setName:"
+ "setSimulatedDate:"
+ "setSystemDomainsByName:"
+ "setSystemDomainsVersions:"
+ "sharedTemporaryDirectoryForTest:"
+ "simulatedDate"
+ "sourceDirectory.isAbsolutePath"
+ "sourceSubPaths.count == destinationSubPaths.count"
+ "standardizedRelativePathFor:"
+ "startFilesystemKeyRollingWithPath:error:"
+ "statfs failed"
+ "stopFilesystemKeyRollingWithPath:error:"
+ "stringByReplacingCharactersInRange:withString:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringWithString:"
+ "submitEngineCompletedEventName:engineStarted:engineError:"
+ "submitEventName:event:"
+ "subpaths"
+ "systemDomainsByName"
+ "systemDomainsVersions"
+ "testName.length"
+ "unmount failed at %{public}@: %{errno}d"
+ "unmount:timeout:error:cancelationHandler:"
+ "unmountAndRenameSnapshotForVolume:name:mountPoint:newName:error:"
+ "userTemporaryDirectoryForTest:"
+ "v32@0:8^i16r^*24"
+ "v40@0:8@16:24@32"
+ "void _mkpath_if_necessary(const char *)"
+ "volumeMountPointForFile:error:"
+ "volumeSupportsLocalSnapshots:"
+ "volumeUUID"
+ "volumeUUIDWithVolumeMountPoint:error:"
+ "\x91\"$\x13!"
- "\a\x14"
- "%s is not MBRestorable"
- "+[MBAnalyticsEvent submitEventName:metrics:]"
- "-[NSObject(MBRestorableMixin) moveFileFromSource:destination:destinationSize:conflictResolution:error:]"
- "=diag= Dstream id %llu, dstream size %llu bytes\n"
- "=diag= Extent offset %lld and length %lld\n"
- "=diag= crypto_id %llu key_class %u, os_vers 0x%x, rev %hu, len %hu"
- "=diag= offset %lld:length %llu, id %lld"
- "=restore-policy= Not restoring because this is an iPod: %@"
- "=scanning= Not backed up (device explicit): %@"
- "@\"MBAnalyticsEvent\""
- "@\"NSError\"20@0:8i16"
- "@\"NSError\"28@0:8@\"NSString\"16B24"
- "@\"NSError\"32@0:8@\"NSString\"16B24B28"
- "@\"NSError\"36@0:8@\"NSString\"16@\"NSString\"24B32"
- "@\"NSString\"56@0:8@\"NSString\"16@\"NSString\"24Q32q40^@48"
- "@24@0:8r*16"
- "@32@0:8@16B24B28"
- "@48@0:8@16@24@32^{_MBFileScannerDomainStats=qqqQQQQQQ}40"
- "@52@0:8@16@24@32i40^{_MBFileScannerDomainStats=qqqQQQQQQ}44"
- "@56@0:8@16@24Q32q40^@48"
- "@64@0:8@16@24i32@36@44i52^{_MBFileScannerDomainStats=qqqQQQQQQ}56"
- "Absolute path doesn't have domain root %@ as prefix: %@"
- "Analytics - Failed to submit \"%@\""
- "Analytics - Setting %@ to %@"
- "Analytics - Setting error: %@"
- "Analytics - Submitting \"%{public}@\": %@"
- "Analytics - Successfully submitted \"%{public}@\""
- "AppleTV"
- "B32@0:8@?16^@24"
- "B40@0:8@\"NSString\"16I24I28^@32"
- "B40@0:8@16I24I28^@32"
- "B44@0:8@\"NSString\"16C24@\"MBRestoreOperationLogger\"28^@36"
- "B44@0:8@\"NSString\"16I24I28S32^@36"
- "B44@0:8@16C24@28^@36"
- "B44@0:8@16I24I28S32^@36"
- "CA metrics have both success and failure recordings"
- "Error removing existing item at %@"
- "InternalBuild"
- "Leaving non-empty staged directory at %@"
- "MBAnalyticsEvent"
- "MBAnalyticsEvent.m"
- "MBAnalyticsEventPlugin"
- "MBBooksPlugin.m"
- "MBDiagnoseFile"
- "MBDiagnoseGetNumberOfFileExtents"
- "MBFileProviderPlugin.m"
- "MBManateePlugin.m"
- "MBRestorableMixin"
- "MBiCloudDrivePlugin.m"
- "Not restoring because this is an iPod: %@"
- "Removing staged item at %@"
- "Restoring ownership at %@"
- "Restoring protection class: %d"
- "T@\"MBAnalyticsEvent\",&,N,V_analyticsEvent"
- "T@\"MBDomain\",R,D,N"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSDictionary\",R,D,N"
- "T@\"NSString\",R,D,N"
- "TQ,R,D,N"
- "TS,R,D,N"
- "_analyticsEvent"
- "_eventName"
- "_isDriveOrMegaBackupPolicy"
- "_metrics"
- "_restoreDirectoryModificationTimes"
- "_scanDirectory:domain:domainDirFd:snapshotPath:relativePath:depth:stats:"
- "_scanFilesForDomain:snapshotPath:relativePath:stats:"
- "_scanFilesUsingGetattrlistbulkForDomain:snapshotPath:relativePath:stats:"
- "_scanFilesUsingReaddirForDomain:snapshotPath:relativePath:depth:stats:"
- "_scanTree:forDomain:snapshotPath:relativePath:stats:"
- "_setProtectionClassWithFD:"
- "_setProtectionClassWithPathFSR:"
- "_standardizePath:fromDomain:"
- "analyticsEvent"
- "backupd"
- "cachedFileDescriptorWithSnapshotPath:error:"
- "decryptToString:withKey:salt:error:"
- "eventName && metrics"
- "groupInTransaction:error:"
- "iPod"
- "initWithEventName:"
- "isIPod"
- "mb_openatWithFlags:error:setupDir:itemAccessor:"
- "moveFileFromSource:destination:destinationSize:conflictResolution:error:"
- "performWithConnection:error:"
- "relativePathsNotToBackupAndRestoreToAppleTVs"
- "relativePathsNotToRestoreToIPods"
- "releaseCachedFileDescriptors"
- "removeFailedAssetFromDestination:withError:"
- "restoreAttributesToDestination:error:"
- "restoreAttributesToDestination:withUserID:groupID:permissions:error:"
- "restoreDirectoryAtPath:settingDataProtection:settingOwnershipAndFlags:"
- "restoreEmptyRegularFileAtPath:settingAttributes:"
- "restoreLastModifiedWithFD:"
- "restoreOwnershipToDestination:withUserID:withGroupID:withError:"
- "restoreProtectionClassToDestination:unspecifiedDirectoryProtectionClass:logger:error:"
- "restoreRegularFileAtPath:settingAttributes:"
- "restoreSymbolicLinkAtPath:withTarget:settingOwnershipAndFlags:"
- "rmdir error"
- "setAnalyticsEvent:"
- "setKey:value:"
- "setMetric:value:"
- "setattrlist() failed"
- "submit"
- "submitEventName:metrics:"

```
