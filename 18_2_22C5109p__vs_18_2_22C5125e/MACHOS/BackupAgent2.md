## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2349.60.69.0.1
-  __TEXT.__text: 0x93e50
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0xda20
-  __TEXT.__objc_methlist: 0x690c
-  __TEXT.__const: 0x428
-  __TEXT.__cstring: 0x1b240
-  __TEXT.__oslogstring: 0xcc1b
-  __TEXT.__objc_methname: 0xfe62
+2349.60.109.0.0
+  __TEXT.__text: 0x950c8
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_stubs: 0xdb40
+  __TEXT.__objc_methlist: 0x699c
+  __TEXT.__const: 0x438
+  __TEXT.__cstring: 0x1b616
+  __TEXT.__oslogstring: 0xcef1
+  __TEXT.__objc_methname: 0x10044
   __TEXT.__objc_classname: 0xab5
-  __TEXT.__objc_methtype: 0x2365
-  __TEXT.__gcc_except_tab: 0x2250
-  __TEXT.__unwind_info: 0x1920
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x550
+  __TEXT.__objc_methtype: 0x234a
+  __TEXT.__gcc_except_tab: 0x22c0
+  __TEXT.__unwind_info: 0x1958
+  __DATA_CONST.__auth_got: 0xc40
+  __DATA_CONST.__got: 0x558
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x14f0
-  __DATA_CONST.__cfstring: 0xae00
+  __DATA_CONST.__cfstring: 0xaf00
   __DATA_CONST.__objc_classlist: 0x3b0
-  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10

   __DATA_CONST.__objc_arraydata: 0x98
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xb608
-  __DATA.__objc_selrefs: 0x43c8
+  __DATA.__objc_const: 0xb658
+  __DATA.__objc_selrefs: 0x4430
   __DATA.__objc_ivar: 0x64c
   __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x8d8

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon
+  - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2529
-  Symbols:   574
-  CStrings:  7451
+  Functions: 2540
+  Symbols:   577
+  CStrings:  7497
 
Symbols:
+ _MBBackupAgentRestoreEndedNotification
+ _MBBackupAgentRestoreStartedNotification
+ _MBPeakProcessMemoryUsage
+ _MBWeakLinkClass
+ _MBWeakLinkSymbol
+ _NSUnderlyingErrorKey
- _NSStringFromClass
- _OBJC_CLASS_$_BRCDatabaseBackupManager
- _OBJC_CLASS_$_BRCDatabaseRestoreManager
CStrings:
+ "%!@(MISSING) does not exist on expected volume(s) [%!@(MISSING)]"
+ "%!s(MISSING) database is closed"
+ "%!s(MISSING) is not MBRestorable"
+ "%!s(MISSING)-%!p(MISSING)"
+ "-[MBMountedSnapshotTracker trackSnapshotForVolume:snapshotName:mountPoint:]"
+ "<MBNode %!p(MISSING): mode 0%!o(MISSING), direntCount %!u(MISSING), uid %!d(MISSING), gid %!d(MISSING), birth %!l(MISSING)d, modified %!l(MISSING)d, flags 0x%!x(MISSING), statusChanged %!l(MISSING)d, fileSize %!l(MISSING)lu, inode %!l(MISSING)lu, genCount %!u(MISSING), cloneID %!l(MISSING)lu, pc %!h(MISSING)hu, xattrs %!d(MISSING)>"
+ "=iCloudDrive= Failed to create CloudDocs database backup manager"
+ "=iCloudDrive= Failed to create CloudDocs database restore manager"
+ "=iCloudDrive= Missing userVolumeMountPoint for iCloud Drive Database"
+ "=restore-placeholders= Failed to move EDS placeholders from %!@(MISSING) to %!@(MISSING)"
+ "=restore-placeholders= Moving EDS placeholders from %!@(MISSING) to %!@(MISSING)"
+ "=restore-policy= Restoring BackupDomain for EDS persona in-place at %!@(MISSING)"
+ "=restore-policy= Restoring legacy placeholder for EDS persona in-place at %!@(MISSING)"
+ "=scanning= Found %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), first pass"
+ "=scanning= Found %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), second pass"
+ "=scanning= Found %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), single pass"
+ "=scanning= Found a direntcount of %!u(MISSING) under %!{(MISSING)public}@ (%!{(MISSING)public}@)"
+ "=scanning= Found a total of %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), first pass"
+ "=scanning= Found a total of %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), second pass"
+ "=scanning= Found a total of %!l(MISSING)lu/%!u(MISSING) items under %!{(MISSING)public}@ (%!{(MISSING)public}@), single pass"
+ "@32@0:8#16^@24"
+ "@80@0:8@16@24@32@40i48I52@56@64^{_MBFileScannerDomainStats=qqqQQQQQQ}72"
+ "App not installed: %!@(MISSING)"
+ "B32@0:8^{?=IIIIqqqqQIQSC{?=b1b1b1}}16@24"
+ "B32@?0@\"NSString\"8r^{?=IIIIqqqqQIQSC{?=b1b1b1}}16@\"NSError\"24"
+ "B64@0:8@16@24@32@40q48^@56"
+ "BRCDatabaseBackupManager"
+ "BRCDatabaseRestoreManager"
+ "BRGenerateDatabaseRestoreManager"
+ "CloudDocs.framework"
+ "CloudDocsDaemon.framework"
+ "Failed to load app with identifier %!@(MISSING): %!@(MISSING)"
+ "Failed to move MBBehaviorOptions plist: %!@(MISSING)"
+ "Failed to remove existing MBBehaviorOptions plist: %!@(MISSING)"
+ "Finished batch i:%!u(MISSING), c:%!l(MISSING)u, t:%!f(MISSING), r:%!f(MISSING), o:%!u(MISSING) s:%!l(MISSING)lu"
+ "Loaded container %!@(MISSING) (%!@(MISSING)) at %!@(MISSING) for parent app %!@(MISSING)"
+ "Moving local MBBehaviorOptions plist from %!@(MISSING) -> %!@(MISSING)"
+ "Removing existing MBBehaviorOptions plist in backup %!@(MISSING)"
+ "_addContainer:toArray:visited:"
+ "_backupManagerForSnapshotURL:liveFSURL:"
+ "_performTwoPassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:stats:"
+ "_placeholderFilesForBundleID:"
+ "_restoreManagerForRestoreDirURL:"
+ "_visitContainerDependenciesAndFilterDuplicates:"
+ "com.apple.private.restrict-post.MobileBackup.Drive.RestoreEnded"
+ "com.apple.private.restrict-post.MobileBackup.Drive.RestoreStarted"
+ "fetchAppWithIdentifier:persona:error:"
+ "isAppPlaceholderName:"
+ "isBackupDomain"
+ "isTooManyOpenFilesError:"
+ "openReadOnlyInstance:error:"
+ "peakMemoryUsage"
+ "plistPath"
+ "restoreRootForDomain:"
+ "setUpMobileBackupPreferencesForBackgroundRestoreWithAccount:restoreSession:cloudFormatInfo:performanceStatistics:backupPolicy:error:"
+ "trackSnapshotForVolume:snapshotName:mountPoint:"
+ "uniqueContainers"
+ "v24@0:8^{?=IIIIqqqqQIQSC{?=b1b1b1}}16"
+ "v24@0:8r^{?=IIIIqqqqQIQSC{?=b1b1b1}}16"
+ "{?=\"direntCount\"I\"userID\"I\"groupID\"I\"flags\"I\"birth\"q\"modified\"q\"statusChanged\"q\"fileSize\"q\"inode\"Q\"genCount\"I\"cloneID\"Q\"mode\"S\"protectionClass\"C\"_is\"{?=\"hardlink\"b1\"fullClone\"b1\"hasXattrs\"b1}}"
- "%!@(MISSING) database is closed"
- "%!@(MISSING) is not MBRestorable"
- "%!@(MISSING)-%!p(MISSING)"
- "-[MBMountedSnapshotTracker trackSnapshotForVolume:snapshotName:mountPount:]"
- "<MBNode %!p(MISSING): mode 0%!o(MISSING), direntCount %!h(MISSING)u, uid %!d(MISSING), gid %!d(MISSING), birth %!l(MISSING)d, modified %!l(MISSING)d, flags 0x%!x(MISSING), statusChanged %!l(MISSING)d, fileSize %!l(MISSING)lu, inode %!l(MISSING)lu, genCount %!u(MISSING), cloneID %!l(MISSING)lu, pc %!h(MISSING)hu, xattrs %!d(MISSING)>"
- "=iCloudDrive= Missing userVolumeMountPount for iCloud Drive Database"
- "=scanning= Found %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), first pass"
- "=scanning= Found %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), second pass"
- "=scanning= Found %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), single pass"
- "=scanning= Found a direntcount of %!l(MISSING)lu under %!{(MISSING)public}@ (%!{(MISSING)public}@)"
- "=scanning= Found a total of %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), first pass"
- "=scanning= Found a total of %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), second pass"
- "=scanning= Found a total of %!l(MISSING)lu items under %!{(MISSING)public}@ (%!{(MISSING)public}@), single pass"
- "@76@0:8@16@24@32@40i48@52@60^{_MBFileScannerDomainStats=qqqQQQQQQ}68"
- "@84@0:8@16@24@32@40i48Q52@60@68^{_MBFileScannerDomainStats=qqqQQQQQQ}76"
- "B32@0:8^{?=SSIIIqqqqQIQC{?=b1b1b1}}16@24"
- "B32@?0@\"NSString\"8r^{?=SSIIIqqqqQIQC{?=b1b1b1}}16@\"NSError\"24"
- "Finished batch i:%!u(MISSING), c:%!l(MISSING)u, t:%!f(MISSING), r:%!f(MISSING), o:%!u(MISSING)"
- "_performTwoPassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:directoryPathStack:directoryCountStack:stats:"
- "com.apple.MobileBackup.Drive.RestoreEnded"
- "com.apple.MobileBackup.Drive.RestoreStarted"
- "openReadOnlyInstance:"
- "trackSnapshotForVolume:snapshotName:mountPount:"
- "v24@0:8^{?=SSIIIqqqqQIQC{?=b1b1b1}}16"
- "v24@0:8r^{?=SSIIIqqqqQIQC{?=b1b1b1}}16"
- "{?=\"mode\"S\"direntCount\"S\"userID\"I\"groupID\"I\"flags\"I\"birth\"q\"modified\"q\"statusChanged\"q\"fileSize\"q\"inode\"Q\"genCount\"I\"cloneID\"Q\"protectionClass\"C\"_is\"{?=\"hardlink\"b1\"fullClone\"b1\"hasXattrs\"b1}}"

```
