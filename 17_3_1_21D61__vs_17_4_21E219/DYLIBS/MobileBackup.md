## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2008.60.8.0.0
-  __TEXT.__text: 0x43b1c
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x4864
-  __TEXT.__const: 0x5a8
-  __TEXT.__cstring: 0xc699
-  __TEXT.__oslogstring: 0x3fc0
-  __TEXT.__gcc_except_tab: 0x1500
-  __TEXT.__unwind_info: 0x1524
-  __TEXT.__objc_classname: 0x4bd
-  __TEXT.__objc_methname: 0xbaea
-  __TEXT.__objc_methtype: 0x14f3
-  __TEXT.__objc_stubs: 0x62c0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x7c0
+2125.102.2.0.0
+  __TEXT.__text: 0x42538
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x4894
+  __TEXT.__const: 0x590
+  __TEXT.__cstring: 0xc381
+  __TEXT.__oslogstring: 0x3c86
+  __TEXT.__gcc_except_tab: 0x1580
+  __TEXT.__unwind_info: 0x14e8
+  __TEXT.__objc_classname: 0x4a6
+  __TEXT.__objc_methname: 0xbc50
+  __TEXT.__objc_methtype: 0x151d
+  __TEXT.__objc_stubs: 0x6120
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x848
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f28
-  __DATA_CONST.__objc_selrefs: 0x2938
+  __DATA_CONST.__objc_const: 0x50b8
+  __DATA_CONST.__objc_selrefs: 0x2940
+  __DATA_CONST.__objc_classrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0x6700
+  __AUTH_CONST.__cfstring: 0x6900
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7a8
-  __DATA.__objc_classrefs: 0x2f0
-  __DATA.__objc_superrefs: 0x170
-  __DATA.__objc_ivar: 0x3e8
+  __AUTH_CONST.__auth_got: 0x7b0
+  __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x200
-  __DATA_DIRTY.__const: 0x600
+  __DATA.__bss: 0x1f8
+  __DATA_DIRTY.__const: 0x520
   __DATA_DIRTY.__objc_const: 0x1b00
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D7D1CA2-14E6-39F9-9F08-DD326BE8F0CE
-  Functions: 1878
-  Symbols:   5918
-  CStrings:  4861
+  UUID: 17566EA6-B803-3065-8A10-F905813D0FCD
+  Functions: 1891
+  Symbols:   5933
+  CStrings:  4874
 
Symbols:
+ +[MBDomain isAppName:]
+ +[MBDomain isContainerizedName:]
+ +[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]
+ +[MBTemporaryDirectory sharedTemporaryDirectoryForTest:].cold.1
+ +[MBTemporaryDirectory userTemporaryDirectoryForTest:]
+ +[MBTemporaryDirectory userTemporaryDirectoryForTest:].cold.1
+ -[MBBackgroundRestoreInfo airTrafficDidFinishRestore]
+ -[MBBackgroundRestoreInfo appDataDidFinishRestore]
+ -[MBBackgroundRestoreInfo perClassItemsRemaining]
+ -[MBBackgroundRestoreInfo recentATCErrors]
+ -[MBBackgroundRestoreInfo setAirTrafficDidFinishRestore:]
+ -[MBBackgroundRestoreInfo setAppDataDidFinishRestore:]
+ -[MBBackgroundRestoreInfo setPerClassItemsRemaining:]
+ -[MBBackgroundRestoreInfo setRecentATCErrors:]
+ -[MBBehaviorOptions _behaviorOptionForTopLevelKey:]
+ -[MBBehaviorOptions _getNumberOptionForKey:]
+ -[MBBehaviorOptions engineStateToCancelRestoreAfter]
+ -[MBBehaviorOptions shouldRestoreFromLegacySnapshotFormat]
+ -[MBBehaviorOptions snapshotFormatString]
+ -[MBBehaviorOptions syntheticATCPathPrefix]
+ -[MBBehaviorOptions useSandboxCKContainer]
+ -[MBBehaviorOptions verifySnapshotAfterCommit]
+ -[MBDomain isContainerizedDomain]
+ -[MBDomainManager removeDomains:]
+ -[MBManagerClient pendingSnapshotForCurrentDeviceWithError:]
+ -[MBPersona restoreSnapshotsDatabaseDirectory]
+ -[MBPersona snapshotDatabaseDirectory]
+ -[MBSnapshot commitID]
+ -[MBSnapshot format]
+ -[MBSnapshot initWithSnapshotID:backupUUID:snapshotUUID:commitID:format:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:type:backupPolicy:accountType:]
+ -[MBSnapshot setCommitID:]
+ -[MBSnapshot setFormat:]
+ -[MBSnapshot setType:]
+ -[MBSnapshot type]
+ -[MBStateInfo backupAttemptCount]
+ -[MBStateInfo initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:backupAttemptCount:]
+ -[MBStateInfo setBackupAttemptCount:]
+ -[MBTemporaryDirectory disposeWithoutDeleting]
+ -[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:]
+ -[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:].cold.1
+ -[NSString(MBSplitPath) _mb_openatWithFlags:setupDir:itemAccessor:]
+ -[NSString(MBSplitPath) mb_openatWithFlags:error:setupDir:itemAccessor:]
+ GCC_except_table1
+ GCC_except_table130
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table154
+ GCC_except_table176
+ GCC_except_table36
+ GCC_except_table55
+ _MBCKStringForBackupState
+ _MBPeakProcessMemoryUsage
+ _MBSnapshotFormatContainsFileLists
+ _MBSnapshotFormatForString
+ _MBSnapshotTypeIsFull
+ _MBStringForBackupPolicy
+ _MBStringForSnapshotFormat
+ _MBStringForSnapshotType
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._airTrafficDidFinishRestore
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._appDataDidFinishRestore
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._perClassItemsRemaining
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._recentATCErrors
+ _OBJC_IVAR_$_MBSnapshot._commitID
+ _OBJC_IVAR_$_MBSnapshot._format
+ _OBJC_IVAR_$_MBSnapshot._type
+ _OBJC_IVAR_$_MBStateInfo._backupAttemptCount
+ __OBJC_$_CLASS_METHODS_MBPersona
+ __OBJC_$_INSTANCE_METHODS_MBPersona
+ __OBJC_$_PROP_LIST_MBPersona
+ ___37-[MBManagerClient setSupportsiTunes:]_block_invoke.39
+ ___44-[MBBehaviorOptions _getNumberOptionForKey:]_block_invoke
+ ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.106
+ ____sharedVolumeTmpDirRoot_block_invoke
+ ____testingOnlySharedVolumeTmpDirRoot_block_invoke
+ ____testingOnlyUserVolumeTmpDirRoot_block_invoke
+ ___block_literal_global.200
+ ___block_literal_global.211
+ ___block_literal_global.225
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.252
+ ___block_literal_global.75
+ ___block_literal_global.78
+ __mkpath_if_necessary
+ __mkpath_if_necessary.cold.1
+ __sharedVolumeTmpDirRoot._path
+ __sharedVolumeTmpDirRoot.onceToken
+ __testingOnlySharedVolumeTmpDirRoot._path
+ __testingOnlySharedVolumeTmpDirRoot.onceToken
+ __testingOnlyUserVolumeTmpDirRoot._path
+ __testingOnlyUserVolumeTmpDirRoot.onceToken
+ _kCFPreferencesCurrentHost
+ _mkpath_np
+ _objc_msgSend$_behaviorOptionForTopLevelKey:
+ _objc_msgSend$_getNumberOptionForKey:
+ _objc_msgSend$_mb_openatWithFlags:setupDir:itemAccessor:
+ _objc_msgSend$initWithSnapshotID:backupUUID:snapshotUUID:commitID:format:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:type:backupPolicy:accountType:
+ _objc_msgSend$initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:backupAttemptCount:
+ _objc_msgSend$isAppName:
+ _objc_msgSend$isContainerizedName:
+ _objc_msgSend$isDataSeparatedAccount
+ _objc_msgSend$mb_splitIntoBase:andRelativePath:
+ _openat
+ _proc_pid_rusage
- +[MBDomain isContainerName:]
- +[MBTemporaryDirectory sharedTemporaryDirectoryForTesting]
- +[MBTemporaryDirectory userTemporaryDirectoryForTesting]
- -[MBBehaviorOptions _behaviorContainerOptionForKey:]
- -[MBBehaviorOptions backupFromLocalSnapshot]
- -[MBBehaviorOptions conn]
- -[MBBehaviorOptions enableSQLiteArchivingWithDefaultValue:]
- -[MBBehaviorOptions fixOwnershipOnFileScanWithDefaultValue:]
- -[MBBehaviorOptions setBackupFromLocalSnapshot:]
- -[MBBehaviorOptions setCloudKitContainerName:]
- -[MBBehaviorOptions setConn:]
- -[MBBehaviorOptions setManifestPageSize:]
- -[MBBehaviorOptions setMaxBatchCount:]
- -[MBBehaviorOptions setMaxBatchFetchAssetSize:]
- -[MBBehaviorOptions setMaxBatchSaveAssetSize:]
- -[MBBehaviorOptions setMaxBatchSize:]
- -[MBBehaviorOptions setRecordSaveAttempts:]
- -[MBBehaviorOptions setSQLTrace:]
- -[MBBehaviorOptions setShouldKeepFileSystemSnapshotAfterBackupFailure:]
- -[MBBehaviorOptions setSqlBatchCount:]
- -[MBBehaviorOptions setSqlBatchTime:]
- -[MBBehaviorOptions setUsePowerLog:]
- -[MBPersona(RestoreLocationAdditions) _fileSystemSupportsSparseFiles:]
- -[MBPersona(RestoreLocationAdditions) _moveRestoreDirectoryFrom:toFinalLocation:error:]
- -[MBPersona(RestoreLocationAdditions) _moveRestoreDirectoryFrom:toFinalLocation:error:].cold.1
- -[MBPersona(RestoreLocationAdditions) _removeRestorePrefetchCacheAtPath:earliestDate:]
- -[MBPersona(RestoreLocationAdditions) cleanupRestoreDirectoriesWithError:]
- -[MBPersona(RestoreLocationAdditions) createRestoreDirectoriesWithError:]
- -[MBPersona(RestoreLocationAdditions) finalizeRestoreDirectoriesWithError:]
- -[MBPersona(RestoreLocationAdditions) finalizeRestoreDirectoriesWithError:].cold.1
- -[MBPersona(RestoreLocationAdditions) removeRestorePrefetchCachesOlderThanDate:]
- -[MBPersona(RestoreLocationAdditions) shouldRestoreFilesSparse]
- -[MBSnapshot backupType]
- -[MBSnapshot initWithSnapshotID:backupUUID:snapshotUUID:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:backupType:backupPolicy:accountType:]
- -[MBSnapshot setBackupType:]
- -[MBStateInfo initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:]
- -[_MBUser setIsPrimaryUser:]
- GCC_except_table134
- GCC_except_table143
- GCC_except_table145
- GCC_except_table147
- GCC_except_table149
- GCC_except_table151
- GCC_except_table158
- GCC_except_table54
- _MBBackupTypeIsFull
- _MBStringForBackupType
- _NSFileSize
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_IVAR_$_MBBehaviorOptions._conn
- _OBJC_IVAR_$_MBSnapshot._backupType
- __CreateRestoreDirectory
- __OBJC_$_CLASS_METHODS_MBPersona(RestoreLocationAdditions)
- __OBJC_$_INSTANCE_METHODS_MBPersona(RestoreLocationAdditions)
- ___37-[MBManagerClient setSupportsiTunes:]_block_invoke.33
- ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.103
- ___63-[MBPersona(RestoreLocationAdditions) shouldRestoreFilesSparse]_block_invoke
- ____sharedTmpDirRoot_block_invoke
- ____testingOnlyUserTmpDirRoot_block_invoke
- ___block_literal_global.197
- ___block_literal_global.208
- ___block_literal_global.222
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.80
- ___kCFBooleanFalse
- __sharedTmpDirRoot.onceToken
- __sharedTmpDirRoot.sharedTmpPath
- __testingOnlyUserTmpDirRoot.onceToken
- __testingOnlyUserTmpDirRoot.usrTmpPath
- _objc_msgSend$_behaviorContainerOptionForKey:
- _objc_msgSend$_fileSystemSupportsSparseFiles:
- _objc_msgSend$_moveRestoreDirectoryFrom:toFinalLocation:error:
- _objc_msgSend$_removeRestorePrefetchCacheAtPath:earliestDate:
- _objc_msgSend$conn
- _objc_msgSend$defaultCenter
- _objc_msgSend$enumeratorAtPath:
- _objc_msgSend$errorWithCode:error:path:format:
- _objc_msgSend$fileExistsAtPath:isDirectory:
- _objc_msgSend$initWithServiceName:
- _objc_msgSend$initWithSnapshotID:backupUUID:snapshotUUID:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:backupType:backupPolicy:accountType:
- _objc_msgSend$initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:
- _objc_msgSend$isContainerName:
- _objc_msgSend$makeTemporaryFilePath
- _objc_msgSend$mb_moveToTmpDirThenRemoveItemAtPath:error:
- _objc_msgSend$messageWithName:arguments:
- _objc_msgSend$postNotificationName:object:userInfo:
- _objc_msgSend$restorePrefetchDirectories
- _objc_msgSend$setIsPrimaryUser:
- _objc_msgSend$sharedIncompleteRestoreDirectory
- _objc_msgSend$sharedRestoreDirectory
- _objc_msgSend$userRestoreDirectory
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _shouldRestoreFilesSparse.lock
- _shouldRestoreFilesSparse.onceToken
- _shouldRestoreFilesSparse.supportsSparseFilesByVolume
CStrings:
+ "\x13"
+ "%s/%s_XXXXXXXXXXXXXXX"
+ ")A"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
+ "-[MBBehaviorOptions _getNumberOptionForKey:]_block_invoke"
+ "-[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:]"
+ "/var/mobile/tmp/com.apple.backup.testing"
+ "/var/tmp/com.apple.backup"
+ "/var/tmp/com.apple.backup.testing"
+ "3\x11"
+ "<%@: %p; snapshotID=%lu, snapshotUUID=%@, commitID=%@, format=%lld, state=%d, type=%ld, backupPolicy=%ld, deviceName=\"%@\", date=\"%@\", systemVersion=%@, buildVersion=%@, isCompatible=%d/%@, quotaReserved=%llu, estimatedRestoreSize=%lld, accountType=%ld>"
+ "=tmpdir= %@ failed to create new contents directory: %@"
+ "=tmpdir= %@ failed to move contents aside to purge: %@"
+ "=tmpdir= %@ was not disposed before being dealloc'd"
+ "=tmpdir= could not find mount point for %@: %@"
+ "=tmpdir= failed to delete %@: %@"
+ "@144@0:8Q16@24@32@40q48@56@64@72@80i88B92@96@104Q112q120q128q136"
+ "@36@0:8i16@?20@?28"
+ "@64@0:8i16f20Q24B32B36@40@48Q56"
+ "ACAccount not eligible for backup"
+ "B44@0:8i16^@20@?28@?36"
+ "BOOL MBSnapshotFormatContainsFileLists(MBSnapshotFormat)"
+ "CancelRestoreAfterEngineState"
+ "Commit"
+ "Complete"
+ "CreateVolumeSnapshots"
+ "DomainsAssets"
+ "Failed to fetch rusage info: %{errno}d"
+ "Failed to mark item purgeable"
+ "Fetched peak memory usage of %llu "
+ "FindChanges"
+ "For key %@, found value %@ which was not a NSNumber.  Ignoring."
+ "Informing client connection was interrupted: %@"
+ "Library/Caches/NeverRestore"
+ "MBPeakProcessMemoryUsage"
+ "ManifestsFiles"
+ "ManifestsFilesAndDomains"
+ "ManifestsFilesAndDomainsAssets"
+ "NSString *MBStringForSnapshotFormat(MBSnapshotFormat)"
+ "Nil persona identifier for Data Separated account"
+ "Nil persona identifier for Primary account"
+ "NotStarted"
+ "PrepareToUploadFiles"
+ "RefreshCache"
+ "ReserveQuota"
+ "Setup"
+ "ShouldRestoreLegacySnapshotFormat"
+ "SnapshotFormat"
+ "SynchronizeFileLists"
+ "SyntheticATCPathPrefix"
+ "T@\"NSMutableDictionary\",&,V_perClassItemsRemaining"
+ "T@\"NSMutableDictionary\",&,V_recentATCErrors"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",&,N,V_commitID"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_airTrafficDidFinishRestore"
+ "TB,N,V_appDataDidFinishRestore"
+ "TB,R,D,N"
+ "TB,R,N,GisContainerizedDomain"
+ "TB,R,N,V_isPrimaryUser"
+ "TQ,N,V_backupAttemptCount"
+ "Td,R,N"
+ "TempDir: Unable to create %s directory (mkpath_np error: %d)"
+ "TempDir: Unable to create temp file path in %s (%d)"
+ "TempDir: Unable to set ownership on %s directory (chown error: %d)"
+ "TempDir: cannot be disposed multiple times %@"
+ "Tq,N,V_format"
+ "Tq,N,V_type"
+ "Unknown snapshot format %llu"
+ "Unknown snapshot format reason %llu"
+ "Unspecified"
+ "UploadDomainRecords"
+ "UploadFiles"
+ "UseSandboxCKContainer"
+ "VerifySnapshotAfterCommit"
+ "_airTrafficDidFinishRestore"
+ "_appDataDidFinishRestore"
+ "_backupAttemptCount"
+ "_behaviorOptionForTopLevelKey:"
+ "_commitID"
+ "_format"
+ "_getNumberOptionForKey:"
+ "_mb_openatWithFlags:setupDir:itemAccessor:"
+ "_mkpath_if_necessary"
+ "_perClassItemsRemaining"
+ "_recentATCErrors"
+ "_type"
+ "airTrafficDidFinishRestore"
+ "appDataDidFinishRestore"
+ "backupAttemptCount"
+ "com.apple.backup"
+ "commitID"
+ "containerizedDomain"
+ "disposeWithoutDeleting"
+ "engineStateToCancelRestoreAfter"
+ "format"
+ "full-seed"
+ "identifier.length"
+ "initWithSnapshotID:backupUUID:snapshotUUID:commitID:format:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:type:backupPolicy:accountType:"
+ "initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:backupAttemptCount:"
+ "isAppName:"
+ "isContainerizedDomain"
+ "isContainerizedName:"
+ "isDataSeparatedAccount"
+ "kMBMessagePendingSnapshotForCurrentDevice"
+ "kMBNotifyDaemonNextTimeKeyBagIsUnlocked %d (%@)"
+ "mb_markItemPurgeableAtPath:error:"
+ "mb_openatWithFlags:error:setupDir:itemAccessor:"
+ "mega"
+ "openat error"
+ "pendingSnapshotForCurrentDeviceWithError"
+ "pendingSnapshotForCurrentDeviceWithError:"
+ "perClassItemsRemaining"
+ "recentATCErrors"
+ "removeDomains:"
+ "restoreSnapshotsDatabaseDirectory"
+ "restore_snapshots"
+ "setAirTrafficDidFinishRestore:"
+ "setAppDataDidFinishRestore:"
+ "setBackupAttemptCount:"
+ "setCommitID:"
+ "setFormat:"
+ "setPerClassItemsRemaining:"
+ "setRecentATCErrors:"
+ "setType:"
+ "sharedTemporaryDirectoryForTest:"
+ "shouldRestoreFromLegacySnapshotFormat"
+ "snapshotDatabaseDirectory"
+ "snapshotFormatString"
+ "syntheticATCPathPrefix"
+ "testName.length"
+ "type"
+ "useSandboxCKContainer"
+ "userTemporaryDirectoryForTest:"
+ "verifySnapshotAfterCommit"
+ "void _mkpath_if_necessary(const char *)"
- "\x14"
- "%@: persona:%@"
- "%s/%s-XXXXXXXXXXXXXXX"
- ")"
- "-[MBPersona(RestoreLocationAdditions) _fileSystemSupportsSparseFiles:]"
- "-[MBPersona(RestoreLocationAdditions) _moveRestoreDirectoryFrom:toFinalLocation:error:]"
- "-[MBPersona(RestoreLocationAdditions) _removeRestorePrefetchCacheAtPath:earliestDate:]"
- "-[MBPersona(RestoreLocationAdditions) cleanupRestoreDirectoriesWithError:]"
- "-[MBPersona(RestoreLocationAdditions) createRestoreDirectoriesWithError:]"
- "-[MBPersona(RestoreLocationAdditions) finalizeRestoreDirectoriesWithError:]"
- "-[MBPersona(RestoreLocationAdditions) removeRestorePrefetchCachesOlderThanDate:]"
- "-[MBPersona(RestoreLocationAdditions) shouldRestoreFilesSparse]"
- "/Library/Caches/com.apple.xbs/Sources/MobileBackupFramework/Versions/2/Source/MBPersona+RestoreLocations.m"
- "/var/mobile/tmp"
- "/var/tmp"
- "4"
- "<%@: %p; snapshotID=%lu, snapshotUUID=%@, state=%d, backupType=%ld, backupPolicy=%ld, deviceName=\"%@\", date=\"%@\", systemVersion=%@, buildVersion=%@, isCompatible=%d/%@, quotaReserved=%llu, estimatedRestoreSize=%lld, accountType=%ld>"
- "@128@0:8Q16@24@32@40@48@56@64i72B76@80@88Q96q104q112q120"
- "@56@0:8i16f20Q24B32B36@40@48"
- "BackupFromLocalSnapshotKey"
- "Couldn't get attr list for filesystem path %@ while checking if it can support sparse files"
- "Creating shared incomplete restore directory: %@"
- "Creating user incomplete restore directory: %@"
- "EnableSQLiteArchiving"
- "Error creating incomplete shared restore directory"
- "Error creating incomplete user restore directory"
- "Failed to create temporary directory %@"
- "Failed to move prefetch directory from %{public}@ -> %{public}@: %@"
- "Failed to move restore sandbox from %{public}@ into place %{public}@: %{public}@"
- "Failed to move restore sandbox into place"
- "Failed to remove %{public}@: %@"
- "Failed to remove existing restore directory"
- "Failed to remove existing restore directory at %{public}@: %{public}@"
- "FixOwnershipOnFileScan"
- "MBBehaviorOptionsChangedKeys"
- "MBBehaviorOptionsKeysChanged"
- "MBPersona+RestoreLocations.m"
- "Moved prefetch directory from %{public}@ -> %{public}@"
- "Moving shared restore directory into place: %@ -> %@"
- "Moving user restore directory into place: %@ -> %@"
- "Nil persona identifier"
- "No prefetch directory found at %{public}@"
- "No restore sandbox at %{public}@"
- "Q24@0:8@16"
- "Removed %@: %llu bytes"
- "Removed %{public}@ (%llu bytes)"
- "Removed prefetch directory at %{public}@"
- "Removing old restore directory"
- "Removing the prefetch directory at %{public}@"
- "RestoreFilesSparse"
- "RestoreLocationAdditions"
- "Skipping shared creating incomplete restore directory: %@"
- "T@\"MBConnection\",&,N,V_conn"
- "TB,D,N"
- "TB,N,V_isPrimaryUser"
- "TempDir: %@ failed to create new contents directory: %@"
- "TempDir: %@ failed to move contents aside to purge: %@"
- "TempDir: %@ was not disposed before being dealloc'd"
- "TempDir: Unable to create temp file path in %s (%{errno}d)"
- "TempDir: cannot be double-disposed %@"
- "TempDir: could not find mount point for %@: %@"
- "TempDir: could not find tmp dir at %@: %@"
- "TempDir: failed to delete %@: %@"
- "Temporary directory does not exist."
- "Ti,N"
- "Tq,N"
- "Tq,N,V_backupType"
- "Unable to open %@: %{errno}d while checking if FS supports sparse files"
- "_CreateRestoreDirectory"
- "_backupType"
- "_behaviorContainerOptionForKey:"
- "_conn"
- "_fileSystemSupportsSparseFiles:"
- "_moveRestoreDirectoryFrom:toFinalLocation:error:"
- "_removeRestorePrefetchCacheAtPath:earliestDate:"
- "_securityd"
- "backupFromLocalSnapshot"
- "cleanupRestoreDirectoriesWithError:"
- "conn"
- "createRestoreDirectoriesWithError:"
- "defaultCenter"
- "enableSQLiteArchivingWithDefaultValue:"
- "enumeratorAtPath:"
- "fileExistsAtPath:isDirectory:"
- "finalizeRestoreDirectoriesWithError:"
- "fixOwnershipOnFileScanWithDefaultValue:"
- "initWithSnapshotID:backupUUID:snapshotUUID:deviceName:date:created:modified:state:isCompatible:systemVersion:buildVersion:quotaReserved:backupType:backupPolicy:accountType:"
- "initWithState:progress:estimatedTimeRemaining:isCloud:isBackground:error:errors:"
- "isContainerName:"
- "kMBMessageGetBehaviorOption"
- "kMBMessageSetBehaviorOption"
- "outError"
- "postNotificationName:object:userInfo:"
- "prefetch-dir-cleanup"
- "removeRestorePrefetchCachesOlderThanDate:"
- "setBackupFromLocalSnapshot:"
- "setBackupType:"
- "setCloudKitContainerName:"
- "setConn:"
- "setIsPrimaryUser:"
- "setManifestPageSize:"
- "setMaxBatchCount:"
- "setMaxBatchFetchAssetSize:"
- "setMaxBatchSaveAssetSize:"
- "setMaxBatchSize:"
- "setRecordSaveAttempts:"
- "setSQLTrace:"
- "setShouldKeepFileSystemSnapshotAfterBackupFailure:"
- "setSqlBatchCount:"
- "setSqlBatchTime:"
- "setUsePowerLog:"
- "sharedTemporaryDirectoryForTesting"
- "shouldRestoreFilesSparse"
- "shouldRestoreFilesSparse=%s"
- "testing"
- "userTemporaryDirectoryForTesting"
- "var"
- "var/Keychains"
- "var/Managed Preferences"
- "var/Managed Preferences/mobile"
- "var/MobileDevice"
- "var/MobileDevice/ProvisioningProfiles"
- "var/mobile"
- "wheel"

```
