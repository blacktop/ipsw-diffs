## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.40.6.0.9
-  __TEXT.__text: 0x28a9e0
+2349.40.37.0.0
+  __TEXT.__text: 0x28c500
   __TEXT.__auth_stubs: 0x3300
-  __TEXT.__objc_stubs: 0x2b7c0
-  __TEXT.__objc_methlist: 0x182dc
-  __TEXT.__cstring: 0x6e22f
-  __TEXT.__objc_methname: 0x38fef
+  __TEXT.__objc_stubs: 0x2bb40
+  __TEXT.__objc_methlist: 0x184bc
+  __TEXT.__cstring: 0x6e9e4
+  __TEXT.__objc_methname: 0x3981d
   __TEXT.__const: 0x15a0
   __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_typeref: 0xbc9

   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0x94
-  __TEXT.__objc_classname: 0x2100
-  __TEXT.__objc_methtype: 0x69db
-  __TEXT.__oslogstring: 0x32540
+  __TEXT.__objc_classname: 0x2157
+  __TEXT.__objc_methtype: 0x6a16
+  __TEXT.__oslogstring: 0x327f1
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x384
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xcc28
+  __TEXT.__gcc_except_tab: 0xcebc
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x7058
+  __TEXT.__unwind_info: 0x7098
   __TEXT.__eh_frame: 0x1c98
   __DATA_CONST.__auth_got: 0x1990
   __DATA_CONST.__got: 0xe68
   __DATA_CONST.__auth_ptr: 0x348
-  __DATA_CONST.__const: 0x8868
-  __DATA_CONST.__cfstring: 0x1f700
-  __DATA_CONST.__objc_classlist: 0xa90
+  __DATA_CONST.__const: 0x88b8
+  __DATA_CONST.__cfstring: 0x1f8c0
+  __DATA_CONST.__objc_classlist: 0xab0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x7f8
+  __DATA_CONST.__objc_superrefs: 0x808
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xd38
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0x4e0
-  __DATA.__objc_const: 0x29530
-  __DATA.__objc_selrefs: 0xc628
-  __DATA.__objc_ivar: 0x1d74
-  __DATA.__objc_data: 0x73b0
+  __DATA.__objc_const: 0x29a10
+  __DATA.__objc_selrefs: 0xc770
+  __DATA.__objc_ivar: 0x1da4
+  __DATA.__objc_data: 0x74f0
   __DATA.__data: 0x20e8
   __DATA.__common: 0x49
   __DATA.__bss: 0x1d68

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10185
+  Functions: 10223
   Symbols:   1399
-  CStrings:  24575
+  CStrings:  24687
 
CStrings:
+ "_findChangesForBundleIDs:error:"
+ "@\"MBBackupTelemetry\""
+ "domainHMACsToRepair.count >= pendingDomainHMACsToRepair.count"
+ "SELECT domainHMAC FROM DomainHMACsToRepair"
+ "initWithSettingsContext:serviceManager:domainManager:"
+ "Could not fetch restore verification summary from plan: %!@(MISSING)"
+ "initWithDomainsNotVerifiedCount:domainsPassingVerificationCount:domainsFailingVerificationCount:"
+ "setPendingRepairedDomainHMACs:"
+ "formatOfLastCommittedSnapshot"
+ "=sizing= Finished scanning for changes - %!@(MISSING)"
+ "UnknownDomainHMACsToRepair"
+ "\"\x11\x14"
+ "_backgroundVerificationEnabled"
+ "Tq,N,V_modifiedBytes"
+ "pendingRepairedDomainHMACs"
+ "MBCKSizingEngine.m"
+ "\n  SELECT verificationStatus, COUNT(*)\n    FROM Domains\nGROUP BY verificationStatus"
+ "_telemetry"
+ "-[MBRestorePlanDB _recordVerificationState:forDomainID:error:]"
+ "T@\"NSMutableSet\",&,N,V_repairedDomainNames"
+ "=cloud-backup= =domain repair= Found domain HMAC to repair %!@(MISSING)"
+ "TB,N,V_backgroundVerificationEnabled"
+ "modifiedBytesByBundleID"
+ "+[MBRestoreCloudFormatPolicy isRestoringFromFileLists:persona:error:]"
+ "MBTapToRadar"
+ "=cloud-backup= =domain repair= Failed to add repair domains to pending snapshot database: %!@(MISSING)"
+ "foregroundDomains"
+ "DELETE FROM ScannedDomains"
+ "shouldRepairDomains"
+ "=cloud-backup-policy= Using server-specified snapshot format: %!@(MISSING)"
+ "TQ,R,N,V_domainsFailingVerificationCount"
+ "=sizing= nil domain manager"
+ "verificationDidRun"
+ "_repairedDomainNames"
+ "-[_RestoreDomainPlanStandard recordVerificationSuccess:]"
+ "domainNamesToForegroundInstall"
+ "recordVerificationSuccess:"
+ "T@\"NSSet\",&,N,V_unknownDomainHMACsToRepair"
+ "INSERT OR REPLACE INTO DomainHMACsToRepair (domainHMAC) VALUES (%!@(MISSING))"
+ "statusToReport"
+ "\nINSERT INTO Domains (\ndomain, \nengineState, \ntotalItems, \ntotalDirs, \ntotalSymlinks, \ntotalHardlinks, \ntotalXattrItems, \ntotalZeroByteFiles, \ntotalAssetFiles, \ntotalAssetBytes, \ntotalXattrBytes, \ntotalAssetRecords, \ntotalRegularAssets, \ntotalEmptyAssets, \ntotalDBAssets, \ntotalEncryptedAssets, \ntotalATCItems, \nrootPath, \nverificationStatus\n) VALUES (%!@(MISSING), %!u(MISSING), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, NULL, %!d(MISSING))\nRETURNING domainID;"
+ "RemoteConfigurationBuildVersion"
+ "-[MBRestorePlanDB fetchRestoreVerificationSummary:]_block_invoke"
+ "=cloud-backup= =domain repair= Failed to open MBPendingSnapshotDB: %!@(MISSING)"
+ "modifiedBytes"
+ "domainsFailingVerificationCount"
+ "@40@0:8Q16Q24Q32"
+ "TB,N,V_isRestoringWithFileLists"
+ "Failed to collect restore errors and file TTR: %!@(MISSING)"
+ "_pendingRepairedDomainHMACs"
+ "setBackgroundRestoreVerificationStatus:"
+ "setModifiedBytes:"
+ "=domain repair= Found domainHMACsToRepair on device record: %!@(MISSING)"
+ "unknownDomainHMACsToRepair"
+ "\nUPDATE Domains\n    SET verificationStatus = %!d(MISSING)\n WHERE domainID = %!l(MISSING)lu"
+ "_recordVerificationState:forDomainID:error:"
+ "domainsPassingVerificationCount"
+ "setRepairedDomainNames:"
+ "\x01%!O(MISSING)\x03\x12"
+ "-[MBCKSizingEngine initWithSettingsContext:serviceManager:]"
+ "+[MBRestoreCloudFormatPolicy shouldRestoreSnapshot:account:persona:useFileLists:error:]"
+ "-[MBPendingSnapshotDB domainHMACsToRepairMatches:outResult:error:]"
+ "-[MBRestorePlanDB recordVerificationSuccessForForegroundDomains:error:]_block_invoke"
+ "Tq,N,V_formatOfLastCommittedSnapshot"
+ "-[MBRestorePlanDB fetchRestoreVerificationSummary:]"
+ "=cloud-backup= =domain repair= Failed to compare pending and new domainHMACsToRepair for equality: %!@(MISSING)"
+ "=sizing= modified:%!l(MISSING)lu total:%!l(MISSING)lu"
+ "=sizing= Failed to scan for changes: %!@(MISSING)"
+ "-[MBCKSizingEngine fileScanner:didFindFile:]"
+ "backgroundVerificationEnabled"
+ "setTotalBytesOnDisk:"
+ "_totalBytesOnDisk"
+ "_findChangesForDomains:error:"
+ "backgroundRestoreVerificationEnabled"
+ "-[MBRestorePlanDB recordVerificationSuccessForForegroundDomains:error:]"
+ "B40@0:8Q16Q24^@32"
+ "setModifiedBytesByBundleID:"
+ "totalBytesOnDisk"
+ "_modifiedBytesByBundleID"
+ "=cloud-backup= Could not remove all file changes from the cache: %!@(MISSING)"
+ "setUnknownDomainHMACsToRepair:"
+ "T@\"NSString\",N,V_backgroundRestoreVerificationStatus"
+ "\nCREATE TABLE IF NOT EXISTS Domains (\ndomainID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \ndomain TEXT NOT NULL UNIQUE, \ntotalAssetRecords INTEGER NOT NULL, \ntotalAssetBytes INTEGER NOT NULL, \ntotalXattrBytes INTEGER NOT NULL, \ntotalRegularAssets INTEGER NOT NULL, \ntotalEmptyAssets INTEGER NOT NULL, \ntotalDBAssets INTEGER NOT NULL, \ntotalEncryptedAssets INTEGER NOT NULL, \ntotalItems INTEGER NOT NULL, \ntotalDirs INTEGER NOT NULL, \ntotalSymlinks INTEGER NOT NULL, \ntotalZeroByteFiles INTEGER NOT NULL, \ntotalAssetFiles INTEGER NOT NULL, \ntotalXattrItems INTEGER NOT NULL, \ntotalHardlinks INTEGER NOT NULL, \ntotalATCItems INTEGER NOT NULL, \nrootPath TEXT, \nengineState INTEGER NOT NULL, \nverificationStatus INTEGER NOT NULL\n);"
+ "T@\"NSSet\",C,N,V_pendingRepairedDomainHMACs"
+ "=scanning= Scanning domain %!{(MISSING)public}@ at %!@(MISSING) with mtpt %!@(MISSING) from snapshot %!@(MISSING) mode:0x%!l(MISSING)x policy:0x%!l(MISSING)x"
+ "=cloud-backup= =domain repair= Not cloning file list for domain pending repair: %!@(MISSING)"
+ "_totalBytesOnDiskByDomainName"
+ "snapshotFormatForCurrentRestore:"
+ "domainHMACsToRepairMatches:outResult:error:"
+ "=domain repair= Pending repair domains %!@(MISSING) != new repair domains %!@(MISSING)"
+ "T@\"NSMutableDictionary\",R,N,V_totalBytesOnDiskByDomainName"
+ "repairedDomainNames"
+ "=cloud-backup= =domain repair= Invalidating pending snapshot"
+ "TQ,R,N,V_domainsPassingVerificationCount"
+ "T@\"NSDictionary\",&,N,V_modifiedBytesByBundleID"
+ "domainHMACsToRepairOnDisk"
+ "=cloud-backup-policy= Fetched snapshot format from behavior options: %!@(MISSING)"
+ "Failed to get non-retyrable error count: %!@(MISSING)"
+ "CREATE TABLE IF NOT EXISTS DomainHMACsToRepair (domainHMAC TEXT NOT NULL PRIMARY KEY )"
+ "-[MBCKSizingEngine setUpWithError:]"
+ "sendStatusRequestForBackgroundRestoreCompletionWithAccount:databaseManager:sourceDeviceID:snapshotUUID:snapshotIndex:plan:duration:error:"
+ "SizingEngine"
+ "isRestoringWithFileLists"
+ "_runWithError:"
+ "trackRepairedDomainName:"
+ "fetchRestoreVerificationSummary:"
+ "=cloud-backup= =domain repair= Forcing a scan on domain pending repair"
+ "file.domain"
+ "(reg-empty) mode 0%!o(MISSING), u/gid %!d(MISSING)/%!d(MISSING), flags 0x%!x(MISSING), b/m/ctime %!l(MISSING)d/%!l(MISSING)d/%!l(MISSING)d, size %!l(MISSING)lu, ino %!l(MISSING)lu, gen %!u(MISSING), pc %!h(MISSING)hu, hasXattrs %!d(MISSING)(%!l(MISSING)lu)"
+ "_findDomainsLimitedTo:error:"
+ "MBRestoreVerificationSummary"
+ "TQ,R,N,V_domainsNotVerifiedCount"
+ "removeAllScannedDomains:"
+ "_modifiedBytes"
+ "-[MBPendingSnapshotDB _domainHMACsToRepair:]"
+ "\x01F"
+ "MBTapToRadar.m"
+ "recordVerificationSuccessForForegroundDomains:error:"
+ "setBackgroundVerificationEnabled:"
+ "addDomainsToBackUpToiCloudWithAppManager:manager:account:"
+ "T@\"NSSet\",R,N,V_domainNamesToForegroundInstall"
+ "\x01!\x11\x14\x13\x15"
+ "=domain repair= Repaired domain HMACs: %!@(MISSING)"
+ "=sizing= Failed to size next backup: %!@(MISSING)"
+ "_domainsFailingVerificationCount"
+ "=cloud-backup= Could not remove deleted file changes from the cache: %!@(MISSING)"
+ "setDomainHMACsToRepairOnDisk:"
+ "Invalid restore verification state: %!l(MISSING)u"
+ "_backgroundRestoreVerificationStatus"
+ "T@\"NSMutableDictionary\",R,N,V_modifiedBytesByDomainName"
+ "_isRestoringWithFileLists"
+ "_domainHMACsToRepair:"
+ "_domainsNotVerifiedCount"
+ "MBRestoreCloudFormatPolicy.m"
+ "=cloud-backup-policy= Force opt-in to %!@(MISSING) format from dry restore options"
+ "=sizing= Format of last committed snapshot: %!@(MISSING)"
+ "RepairedDomainNames"
+ "isEqualToSet:"
+ "recordVerificationFailure:"
+ "=sizing= Failed to fetch placeholder for %!@(MISSING): %!@(MISSING)"
+ "-[MBPendingSnapshotDB addDomainHMACsToRepair:error:]"
+ "reportLightrailRestoreFailed"
+ "domainsNotVerifiedCount"
+ "snapshotFormatForAccount:error:"
+ "=sizing= Failed to notify plugins of startingBackupWithEngine: %!@(MISSING)"
+ "v80@0:8@16@24@32@40Q48@56d64@72"
+ "setFormatOfLastCommittedSnapshot:"
+ "totalBytesOnDiskByDomainName"
+ "_bundleIDForDomainName:"
+ "Tq,N,V_totalBytesOnDisk"
+ "initWithSettingsContext:serviceManager:"
+ "addDomainHMACsToRepair:error:"
+ "Found non retryable errors"
+ "_domainHMACsToRepairOnDisk"
+ "-[MBCKSizingEngine initWithSettingsContext:serviceManager:domainManager:]"
+ "_tearDown"
+ "MBBackupTelemetry"
+ "modifiedBytesByDomainName"
+ "_formatOfLastCommittedSnapshot"
+ "_modifiedBytesByDomainName"
+ "MBCKSizingEngine"
+ "=domain repair= Not copying assets in previous file list for %!@(MISSING)"
+ "dryRestoreInterval"
+ "removeDeletedFileChanges"
+ "_unknownDomainHMACsToRepair"
+ "setIsRestoringWithFileLists:"
+ "+[MBTapToRadar _collectRestoreErrorsAndFileTTR:restoreFailuresPlistPath:error:]"
+ "telemetry"
+ "T@\"MBBackupTelemetry\",R,N,V_telemetry"
+ "Could not determine if restoring using file lists: %!@(MISSING)"
+ "MBRestoreCloudFormatPolicy"
+ "Failed to add repair domain HMAC %!@(MISSING): %!@(MISSING)"
+ "=sizing= Scanning domains: %!@(MISSING)"
+ "-[MBCKManager _startScanWithSettingsContext:error:]_block_invoke"
+ "\x12'\xf06"
+ "T@\"NSSet\",&,N,V_domainHMACsToRepairOnDisk"
+ "backgroundRestoreVerificationStatus"
+ "_domainsPassingVerificationCount"
+ "MBBackupCloudFormatPolicy"
+ "C\x14\x1f\x01"
+ "-[_RestoreDomainPlanStandard recordVerificationFailure:]"
+ "SnapshotFormatEnum"
- "=usage= Excluding disabled domains: %!@(MISSING)"
- "Found domainHMACsToRepair on device record: %!@(MISSING)"
- "TQ,N,V_bytesUsed"
- "_isEnabledForBackup"
- "File doesn't have a domain: %!@(MISSING)"
- "\"\x12\x13"
- "v72@0:8@16@24@32@40Q48d56@64"
- "-[MBCKUsageEngine findDomainsLimitedTo:error:]"
- "TQ,R,N,V_telemetryID"
- "TB,N,V_isEnabledForBackup"
- "-[MBCKUsageEngine initWithSettingsContext:debugContext:serviceManager:]"
- "=snapshot-policy= Found non retryable errors"
- "\x01%!O(MISSING)\x01\x12"
- "=snapshot-policy= Failed to create a TTR: %!@(MISSING)"
- "-[MBCKManager _ckRunScanWithSettingsContext:]"
- "_bytesUsedByDomainName"
- "_cleanupSnapshotsAndRemoveThem:"
- "=cloud-backup= Disabled domains: %!@(MISSING)"
- "(reg-empty) mode 0%!o(MISSING), u/gid %!d(MISSING)/%!d(MISSING), flags 0x%!x(MISSING), b/m/ctime %!l(MISSING)d/%!l(MISSING)d/%!l(MISSING)d, size %!l(MISSING)lu, ino %!l(MISSING)lu, pc %!h(MISSING)hu, hasXattrs %!d(MISSING)(%!l(MISSING)lu)"
- "setBytesUsedByBundleID:"
- "=cloud-backup= Restricted domains: %!@(MISSING)"
- "=usage= Adding %!l(MISSING)lu bytes for %!@(MISSING)"
- "MBCKUsageEngine.m"
- "=usage= Finished scanning for changes - %!@(MISSING)"
- "\x12'\xf04"
- "findChangesForDomains:error:"
- "bytesUsedByBundleID"
- "=cloud-backup= Using server-specified snapshot format: %!@(MISSING)"
- "bytesUsedByDomainName"
- "+[MBRestoreCloudFormatInfoPolicy isRestoringFromFileLists:persona:error:]"
- "=usage= nil domain manager"
- "\nCREATE TABLE IF NOT EXISTS Domains (\ndomainID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \ndomain TEXT NOT NULL UNIQUE, \ntotalAssetRecords INTEGER NOT NULL, \ntotalAssetBytes INTEGER NOT NULL, \ntotalXattrBytes INTEGER NOT NULL, \ntotalRegularAssets INTEGER NOT NULL, \ntotalEmptyAssets INTEGER NOT NULL, \ntotalDBAssets INTEGER NOT NULL, \ntotalEncryptedAssets INTEGER NOT NULL, \ntotalItems INTEGER NOT NULL, \ntotalDirs INTEGER NOT NULL, \ntotalSymlinks INTEGER NOT NULL, \ntotalZeroByteFiles INTEGER NOT NULL, \ntotalAssetFiles INTEGER NOT NULL, \ntotalXattrItems INTEGER NOT NULL, \ntotalHardlinks INTEGER NOT NULL, \ntotalATCItems INTEGER NOT NULL, \nrootPath TEXT, \nengineState INTEGER NOT NULL\n);"
- "=usage= Calculated successfully: %!l(MISSING)lu bytes"
- "setIsEnabledForBackup:"
- "-[MBCKUsageEngine initWithSettingsContext:debugContext:serviceManager:domainManager:]"
- "+[MBRestoreCloudFormatInfoPolicy _collectRestoreErrorsAndFileTTR:restoreFailuresPlistPath:error:]"
- "=usage= Scanning domains: %!@(MISSING)"
- "T@\"NSNumber\",R,N,V_uploadedFileCount"
- "bundleIDForDomainName:"
- "_ckRunScanWithSettingsContext:"
- "purgeAllFileChanges"
- "-[MBCKUsageEngine setUpWithError:]"
- "bytesUsed"
- "findDomainsLimitedTo:error:"
- "T@\"NSMutableDictionary\",R,N,V_bytesUsedByDomainName"
- "=usage= Failed to notify plugins of startingBackupWithEngine: %!@(MISSING)"
- "MBRestoreCloudFormatInfoPolicy"
- "initWithSettingsContext:debugContext:serviceManager:domainManager:"
- "_bytesUsed"
- "\x01%!"(MISSING)
- "=cloud-backup= Placeholder: Failed to archive placeholder for: %!@(MISSING) %!@(MISSING)"
- "MBRestoreCloudFormatInfoPolicy.m"
- "=snapshot-policy= Failed to get non-retyrable error count: %!@(MISSING)"
- "+[MBRestoreCloudFormatInfoPolicy shouldRestoreSnapshot:account:persona:useFileLists:error:]"
- "T@\"NSArray\",R,N,V_throughputs"
- "T@\"NSDictionary\",&,N,V_bytesUsedByBundleID"
- "T@\"NSNumber\",R,N,V_uploadedSize"
- "=usage= Scanning files for changes"
- "findChangesForBundleIDs:error:"
- "initWithSettingsContext:debugContext:serviceManager:"
- "=usage= Scan failed: %!@(MISSING)"
- "MBCKUsageEngine"
- "_bytesUsedByBundleID"
- "purgeDeletedFileChanges"
- "\nINSERT INTO Domains (\ndomain, \nengineState, \ntotalItems, \ntotalDirs, \ntotalSymlinks, \ntotalHardlinks, \ntotalXattrItems, \ntotalZeroByteFiles, \ntotalAssetFiles, \ntotalAssetBytes, \ntotalXattrBytes, \ntotalAssetRecords, \ntotalRegularAssets, \ntotalEmptyAssets, \ntotalDBAssets, \ntotalEncryptedAssets, \ntotalATCItems, \nrootPath\n) VALUES (%!@(MISSING), %!u(MISSING), -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, NULL)\nRETURNING domainID;"
- "setBytesUsed:"
- "sendStatusRequestForBackgroundRestoreCompletionWithAccount:databaseManager:sourceDeviceID:snapshotUUID:snapshotIndex:duration:error:"
- "\x018)\x15D\x13\x18"
- "=snapshot-policy= Failed to collect restore errors and file TTR: %!@(MISSING)"
- "removeDomains:"
- "=usage= Failed to fetch placeholder for %!@(MISSING): %!@(MISSING)"
- "=scanning= Scanning domain %!{(MISSING)public}@ at %!@(MISSING) from snapshot %!@(MISSING) mode:0x%!l(MISSING)x policy:0x%!l(MISSING)x"
- "-[MBCKUsageEngine performRetryablePhase:]"
- "=cloud-backup= Found domain HMAC to repair %!@(MISSING)"
- "=usage= Retrying after error: %!@(MISSING)"
- "=cloud-backup= Could not purge deleted files from the cache: %!@(MISSING)"
- "=usage= Failed to scan for changes: %!@(MISSING)"
- "=usage= Excluding restricted domains: %!@(MISSING)"
- "=cloud-backup= Fetched snapshot format from behaviour options: %!@(MISSING)"

```
