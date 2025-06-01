## MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

-2008.60.8.0.0
-  __TEXT.__text: 0x5750
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x348
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x12b3
-  __TEXT.__objc_classname: 0x3a
-  __TEXT.__objc_methname: 0xf21
-  __TEXT.__objc_methtype: 0x121
-  __TEXT.__oslogstring: 0x8d0
-  __TEXT.__unwind_info: 0x16c
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__cfstring: 0x540
-  __DATA_CONST.__objc_classlist: 0x10
+2125.102.2.0.0
+  __TEXT.__text: 0x8aa0
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0x1500
+  __TEXT.__objc_methlist: 0x410
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__cstring: 0x1ffb
+  __TEXT.__objc_classname: 0x63
+  __TEXT.__objc_methname: 0x15d1
+  __TEXT.__objc_methtype: 0x1bf
+  __TEXT.__oslogstring: 0xe86
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__cfstring: 0x840
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x470
-  __DATA.__objc_selrefs: 0x4a8
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x518
+  __DATA.__objc_selrefs: 0x668
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0xa0
-  __DATA.__bss: 0x20
+  __DATA.__objc_data: 0xf0
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2274413B-6C17-30E6-90B4-B572BB213511
-  Functions: 100
-  Symbols:   111
-  CStrings:  417
+  UUID: ECDE62C9-A156-3142-BC58-DA606E190D6A
+  Functions: 135
+  Symbols:   135
+  CStrings:  628
 
Symbols:
+ _MBCreateTemporaryFilePathIn
+ _MBIsInternalInstall
+ _NSFileCreationDate
+ _NSFileGroupOwnerAccountName
+ _NSFileOwnerAccountName
+ _NSFileSize
+ _NSStringFromSelector
+ _OBJC_CLASS_$_MBDomain
+ _OBJC_CLASS_$_MBTemporaryDirectory
+ _OBJC_CLASS_$_NSMutableDictionary
+ ___error
+ _close
+ _copyfile
+ _copyfile_state_alloc
+ _copyfile_state_free
+ _fgetattrlist
+ _lstat
+ _mkpath_np
+ _objc_retainAutorelease
+ _open
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _readlink
+ _renamex_np
CStrings:
+ "%@: persona:%@"
+ "+[MBFileOperation createPathInDirectory:fileName:]"
+ "+[MBFileOperation createPathInDirectory:fileName:]_block_invoke"
+ "+[MBFileOperation crossVolumeCopyFrom:toDestination:shouldDeleteSource:error:]"
+ "+[MBFileOperation crossVolumeMoveFrom:intoDir:toFileNamed:error:]"
+ "+[MBFileOperation symbolicLinkTargetWithPathFSR:error:]"
+ "+[MBPersona(RestoreLocationAdditions) _stashFileAtURL:prefetchDirectory:error:]"
+ "-[MBPersona(RestoreLocationAdditions) _fileSystemSupportsSparseFiles:]"
+ "-[MBPersona(RestoreLocationAdditions) _moveRestoreDirectoryFrom:toFinalLocation:error:]"
+ "-[MBPersona(RestoreLocationAdditions) _removeRestorePrefetchCacheAtPath:earliestDate:]"
+ "-[MBPersona(RestoreLocationAdditions) cleanupRestoreDirectoriesWithError:]"
+ "-[MBPersona(RestoreLocationAdditions) createRestoreDirectoriesWithError:]"
+ "-[MBPersona(RestoreLocationAdditions) finalizeRestoreDirectoriesWithError:]"
+ "-[MBPersona(RestoreLocationAdditions) removeRestorePrefetchCachesOlderThanDate:]"
+ "-[MBPersona(RestoreLocationAdditions) shouldRestoreFilesSparse]"
+ "/Library/Caches/com.apple.xbs/Sources/MobileBackup/Versions/2/Source/MBFileOperation.m"
+ "/Library/Caches/com.apple.xbs/Sources/MobileBackup/Versions/2/Source/MBPersona+RestoreLocations.m"
+ "@32@0:8@16@24"
+ "@32@0:8r*16^@24"
+ "@40@0:8@16@24^@32"
+ "B24@0:8@16"
+ "B24@0:8^@16"
+ "B40@0:8@16@24^@32"
+ "B44@0:8r*16r*24B32^@36"
+ "B48@0:8@16@24@32^@40"
+ "Couldn't get attr list for filesystem path %@ while checking if it can support sparse files"
+ "Created the directory at %@"
+ "Creating shared incomplete restore directory: %@"
+ "Creating user incomplete restore directory: %@"
+ "Error creating incomplete shared restore directory"
+ "Error creating incomplete user restore directory"
+ "FAULT"
+ "Failed to convert filesystem representation"
+ "Failed to convert filesystem representation %s"
+ "Failed to create temporary directory %@"
+ "Failed to move %@ to %@: %@"
+ "Failed to move prefetch directory from %{public}@ -> %{public}@: %@"
+ "Failed to move restore sandbox from %{public}@ into place %{public}@: %{public}@"
+ "Failed to move restore sandbox into place"
+ "Failed to remove %@: %@"
+ "Failed to remove %{public}@: %@"
+ "Failed to remove existing restore directory"
+ "Failed to remove existing restore directory at %{public}@: %{public}@"
+ "Found destination file at %@"
+ "Found source file at %@"
+ "MBFileOperation"
+ "MBFileOperation.m"
+ "MBPersona+RestoreLocations.m"
+ "MBPrefetchPath"
+ "Moved prefetch directory from %{public}@ -> %{public}@"
+ "Moving shared restore directory into place: %@ -> %@"
+ "Moving user restore directory into place: %@ -> %@"
+ "NO"
+ "No prefetch directory found at %{public}@"
+ "No restore sandbox at %{public}@"
+ "Q24@0:8@16"
+ "Q32@0:8@16@24"
+ "Removed %@: %llu bytes"
+ "Removed %{public}@ (%llu bytes)"
+ "Removed prefetch directory at %{public}@"
+ "Removing old restore directory"
+ "Removing the prefetch directory at %{public}@"
+ "RestoreFilesSparse"
+ "RestoreLocationAdditions"
+ "Skipping shared creating incomplete restore directory: %@"
+ "Unable to create temporary path in: %@"
+ "Unable to open %@: %{errno}d while checking if FS supports sparse files"
+ "YES"
+ "_CreateRestoreDirectory"
+ "_fileSystemSupportsSparseFiles:"
+ "_moveRestoreDirectoryFrom:toFinalLocation:error:"
+ "_removeRestorePrefetchCacheAtPath:earliestDate:"
+ "_securityd"
+ "_stashFileAtURL:prefetchDirectory:error:"
+ "absolutePath"
+ "attributesOfItemAtPath:error:"
+ "boolValue"
+ "cleanupRestoreDirectoriesWithError:"
+ "compare:"
+ "containerIDWithName:"
+ "copyfile failed"
+ "copyfile(%s, %s) failed (%d): %{errno}d"
+ "could not copy across volumes from %s to %s: %@"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createPathInDirectory:fileName:"
+ "createRestoreDirectoriesWithError:"
+ "crossVolumeCopyFrom:toDestination:shouldDeleteSource:error:"
+ "crossVolumeMoveFrom:intoDir:toFileNamed:error:"
+ "cross_volume_copy"
+ "dispose"
+ "domain"
+ "dst"
+ "errorWithCode:error:path:format:"
+ "errorWithCode:path:format:"
+ "fileExistsAtPath:"
+ "fileExistsAtPath:isDirectory:"
+ "fileName"
+ "fileSystemRepresentation"
+ "finalizeRestoreDirectoriesWithError:"
+ "initFileURLWithPath:"
+ "isSystemContainerDomain"
+ "isSystemSharedContainerDomain"
+ "lstat failed at %@: %{errno}d"
+ "makeTemporaryFilePath"
+ "mb_moveToTmpDirThenRemoveItemAtPath:error:"
+ "mb_stringWithFileSystemRepresentation:"
+ "mkdir failed at %@: %{errno}d"
+ "mobile"
+ "moveItemAtPath:toPath:error:"
+ "moveItemAtURL:toURL:error:"
+ "name"
+ "numberWithInt:"
+ "outError"
+ "parentDir"
+ "personaAttributesForPersonaType:withError:"
+ "posixErrorWithCode:format:"
+ "posixErrorWithCode:path:format:"
+ "posixErrorWithPath:format:"
+ "prefetch-dir-cleanup"
+ "prefetchDirectory"
+ "readlink error"
+ "relativePath"
+ "rename of stashed resource from %s to %s failed"
+ "rename of stashed resource from %{public}@ to %{public}s failed: %{errno}d"
+ "restorePathForRestorable:"
+ "restorePrefetchDirectories"
+ "restorePrefetchDirectoryForDomain:"
+ "setObject:forKeyedSubscript:"
+ "sharedIncompleteRestoreDirectory"
+ "sharedRestoreDirectory"
+ "shouldRestoreFilesSparse"
+ "shouldRestoreFilesSparse=%s"
+ "shouldRestoreToSharedVolume"
+ "src"
+ "srcFilePath"
+ "srcURL"
+ "stashAsset:forDomain:error:"
+ "stringWithFileSystemRepresentation:length:"
+ "symbolicLinkTargetWithPath:error:"
+ "symbolicLinkTargetWithPathFSR:error:"
+ "systemDataContainerRestoreDirectory"
+ "systemSharedDataContainerRestoreDirectory"
+ "temporaryDirectoryOnSameVolumeAsPath:identifiedBy:error:"
+ "unsignedLongLongValue"
+ "userIncompleteRestoreDirectory"
+ "userRestoreDirectory"
+ "var"
+ "var/Keychains"
+ "var/Managed Preferences"
+ "var/Managed Preferences/mobile"
+ "var/MobileDevice"
+ "var/MobileDevice/ProvisioningProfiles"
+ "var/mobile"
+ "wheel"

```
