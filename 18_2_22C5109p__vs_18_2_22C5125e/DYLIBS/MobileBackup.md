## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2349.60.69.0.1
-  __TEXT.__text: 0x3a87c
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x4304
+2349.60.109.0.0
+  __TEXT.__text: 0x3b8ac
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x438c
   __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x9d78
-  __TEXT.__gcc_except_tab: 0x164c
-  __TEXT.__oslogstring: 0x3839
-  __TEXT.__unwind_info: 0x1330
+  __TEXT.__cstring: 0xa1c5
+  __TEXT.__gcc_except_tab: 0x173c
+  __TEXT.__oslogstring: 0x39f3
+  __TEXT.__unwind_info: 0x1348
   __TEXT.__objc_classname: 0x44a
-  __TEXT.__objc_methname: 0xb465
-  __TEXT.__objc_methtype: 0x1504
-  __TEXT.__objc_stubs: 0x56a0
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x760
+  __TEXT.__objc_methname: 0xb6c3
+  __TEXT.__objc_methtype: 0x1547
+  __TEXT.__objc_stubs: 0x57e0
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26a8
+  __DATA_CONST.__objc_selrefs: 0x2738
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x6340
-  __AUTH_CONST.__objc_const: 0x64e0
+  __AUTH_CONST.__cfstring: 0x6540
+  __AUTH_CONST.__objc_const: 0x6540
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1749
-  Symbols:   2197
-  CStrings:  3706
+  Functions: 1762
+  Symbols:   2223
+  CStrings:  3773
 
Symbols:
+ _MBBackupAgentRestoreEndedNotification
+ _MBBackupAgentRestoreStartedNotification
+ _MBDumpLsofOutputToLogDir
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _kMBBackgroundRestoreCellularAccessChangedNotification
+ _posix_spawn
+ _posix_spawn_file_actions_addopen
+ _posix_spawn_file_actions_destroy
+ _posix_spawn_file_actions_init
+ _posix_spawnattr_destroy
+ _posix_spawnattr_init
+ _posix_spawnattr_setflags
+ _unlink
+ _waitpid
CStrings:
+ "%!d(MISSING)"
+ "-p"
+ "/%!@(MISSING):%!l(MISSING)d"
+ "/usr/sbin/lsof"
+ "<%!s(MISSING): %!@(MISSING), path: %!s(MISSING)>"
+ "<%!s(MISSING): %!p(MISSING); accountIdentifier=%!@(MISSING), personaIdentifier=%!@(MISSING), isPrimaryAccount=%!d(MISSING), changeType=%!l(MISSING)d>"
+ "<%!s(MISSING): %!p(MISSING); backupUUID=%!@(MISSING), snapshotUUID=%!@(MISSING), backupUDID=%!@(MISSING), snapshotID=%!l(MISSING)u>"
+ "<%!s(MISSING): %!p(MISSING); deviceUDID=%!@(MISSING), deviceUUID=%!@(MISSING), device=\"%!@(MISSING)/%!@(MISSING)/%!@(MISSING)\", restoreSysFiles=%!d(MISSING), snapshots=%!@(MISSING)>"
+ "<%!s(MISSING): %!p(MISSING); id=%!@(MISSING), user=%!@(MISSING)>"
+ "<%!s(MISSING): %!p(MISSING); isPrimaryUser=%!d(MISSING)>"
+ "<%!s(MISSING): %!p(MISSING); snapshotID=%!l(MISSING)u, snapshotUUID=%!@(MISSING), commitID=%!@(MISSING), format=%!l(MISSING)ld, state=%!d(MISSING), type=%!l(MISSING)d, backupPolicy=%!l(MISSING)d, deviceName=\"%!@(MISSING)\", date=\"%!@(MISSING)\", systemVersion=%!@(MISSING), buildVersion=%!@(MISSING), isCompatible=%!d(MISSING)/%!@(MISSING), quotaReserved=%!l(MISSING)lu, estimatedRestoreSize=%!l(MISSING)ld, accountType=%!l(MISSING)d>"
+ "<%!s(MISSING): %!p(MISSING); state=%!d(MISSING), progress=%!f(MISSING), timeRemaining=%!l(MISSING)u, isCloud=%!d(MISSING), isBackground=%!d(MISSING), date=\"%!@(MISSING)\", error=\"%!@(MISSING)\">"
+ "=mbfm= Updating plist at %!@(MISSING) to %!@(MISSING)"
+ "=peak-memory= %!l(MISSING)lu bytes"
+ "=tmpdir= Failed to create %!s(MISSING) directory (mkdtemp error: %!d(MISSING))"
+ "BackupDomain"
+ "Dumped lsof output to %!@(MISSING)"
+ "Failed to mark item as purgeable at %!@(MISSING)"
+ "IsAutomation"
+ "Spawned /usr/sbin/lsof %!s(MISSING) %!s(MISSING)"
+ "TB,R,N,GisBackupDomain"
+ "TempDir: Failed to create %!s(MISSING) directory (mkdtemp error: %!d(MISSING))"
+ "TempDir: Failed to create directory (mkdtemp error: %!d(MISSING))"
+ "addEntriesFromDictionary:"
+ "arrayWithCapacity:"
+ "backupDomain"
+ "char *_mkdtemp(const char *, NSString *__strong, NSError *__autoreleasing *)"
+ "com.apple.private.restrict-post.MobileBackup.BackupAgent.RestoreEnded"
+ "com.apple.private.restrict-post.MobileBackup.BackupAgent.RestoreStarted"
+ "com.apple.private.restrict-post.MobileBackup.Drive.RestoreEnded"
+ "com.apple.private.restrict-post.MobileBackup.Drive.RestoreStarted"
+ "com.apple.private.restrict-post.MobileBackup.backgroundCellularAccessChanged"
+ "com.apple.private.restrict-post.MobileBackup.backupStateChanged"
+ "com.apple.private.restrict-post.MobileBackup.restoreCompletedAlertStateChanged"
+ "com.apple.private.restrict-post.MobileBackup.restoreStateChanged"
+ "dataWithPropertyList:format:options:error:"
+ "dictionaryRepresentationForError:withMultiErrors:"
+ "dictionaryWithContentsOfFile:"
+ "dryRestore:snapshotUUID:error:"
+ "dryRestoreContentDirectory"
+ "dryRestoreMetadataDirectory"
+ "dry_restore_content"
+ "dry_restore_metadata"
+ "errorWithDictionaryRepresentation:withMultiErrors:"
+ "isAutomation"
+ "isBackupDomain"
+ "isTooManyOpenFilesError:"
+ "kMBMessageDryRestore"
+ "kMBMessageDryRestoreAllowance"
+ "kMBMessageDryRestoreSnapshotUUID"
+ "kMBMessageScheduleActivities"
+ "lsof"
+ "lsof exited"
+ "lsof stopped"
+ "lsof was terminated by signal %!d(MISSING)"
+ "lsof-%!@(MISSING)-%!@(MISSING).log"
+ "manager:didUpdateProgress:estimatedTimeRemaining:bytesRemaining:state:"
+ "mb_savePlistAtPath:addingItems:removing:error:"
+ "posix_spawn() failed: %!{(MISSING)errno}d"
+ "posix_spawn_file_actions_addopen() failed: %!{(MISSING)errno}d"
+ "posix_spawn_file_actions_init() failed: %!{(MISSING)errno}d"
+ "posix_spawnattr_setflags() failed: %!{(MISSING)errno}d"
+ "removeObjectsForKeys:"
+ "scheduleActivities:error:"
+ "signatureForError:"
+ "underlyingErrors"
+ "v52@0:8@\"MBManager\"16f24Q28q36@\"NSString\"44"
+ "v52@0:8@16f24Q28q36@44"
+ "waitpid() failed: %!{(MISSING)errno}d"
+ "writeToFile:options:error:"
- "<%!@(MISSING): %!@(MISSING), path: %!s(MISSING)>"
- "<%!@(MISSING): %!p(MISSING); accountIdentifier=%!@(MISSING), personaIdentifier=%!@(MISSING), isPrimaryAccount=%!d(MISSING), changeType=%!l(MISSING)d>"
- "<%!@(MISSING): %!p(MISSING); backupUUID=%!@(MISSING), snapshotUUID=%!@(MISSING), backupUDID=%!@(MISSING), snapshotID=%!l(MISSING)u>"
- "<%!@(MISSING): %!p(MISSING); deviceUDID=%!@(MISSING), deviceUUID=%!@(MISSING), device=\"%!@(MISSING)/%!@(MISSING)/%!@(MISSING)\", restoreSysFiles=%!d(MISSING), snapshots=%!@(MISSING)>"
- "<%!@(MISSING): %!p(MISSING); id=%!@(MISSING), user=%!@(MISSING)>"
- "<%!@(MISSING): %!p(MISSING); isPrimaryUser=%!d(MISSING)>"
- "<%!@(MISSING): %!p(MISSING); snapshotID=%!l(MISSING)u, snapshotUUID=%!@(MISSING), commitID=%!@(MISSING), format=%!l(MISSING)ld, state=%!d(MISSING), type=%!l(MISSING)d, backupPolicy=%!l(MISSING)d, deviceName=\"%!@(MISSING)\", date=\"%!@(MISSING)\", systemVersion=%!@(MISSING), buildVersion=%!@(MISSING), isCompatible=%!d(MISSING)/%!@(MISSING), quotaReserved=%!l(MISSING)lu, estimatedRestoreSize=%!l(MISSING)ld, accountType=%!l(MISSING)d>"
- "<%!@(MISSING): %!p(MISSING); state=%!d(MISSING), progress=%!f(MISSING), timeRemaining=%!l(MISSING)u, isCloud=%!d(MISSING), isBackground=%!d(MISSING), date=\"%!@(MISSING)\", error=\"%!@(MISSING)\">"
- "Fetched peak memory usage of %!l(MISSING)lu "
- "TempDir: Unable to create %!s(MISSING) directory (mkdtemp error: %!d(MISSING))"
- "char *_mkdtemp(const char *, NSString *__strong)"
- "com.apple.MobileBackup.Drive.RestoreEnded"
- "com.apple.MobileBackup.Drive.RestoreStarted"
- "com.apple.MobileBackup.backupStateChanged"
- "com.apple.MobileBackup.restoreCompletedAlertStateChanged"
- "com.apple.MobileBackup.restoreStateChanged"

```
