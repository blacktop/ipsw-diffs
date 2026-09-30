## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.40.41.0.0
-  __TEXT.__text: 0x28c85c
+2349.40.54.0.1
+  __TEXT.__text: 0x28e360
   __TEXT.__auth_stubs: 0x3300
-  __TEXT.__objc_stubs: 0x2bb40
-  __TEXT.__objc_methlist: 0x184bc
-  __TEXT.__cstring: 0x6eb38
-  __TEXT.__objc_methname: 0x3981d
+  __TEXT.__objc_stubs: 0x2bca0
+  __TEXT.__objc_methlist: 0x185a4
+  __TEXT.__cstring: 0x6f5d6
+  __TEXT.__objc_methname: 0x39b40
   __TEXT.__const: 0x15a0
   __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_typeref: 0xbc9

   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0x94
   __TEXT.__objc_classname: 0x2157
-  __TEXT.__objc_methtype: 0x6a16
-  __TEXT.__oslogstring: 0x328ff
+  __TEXT.__objc_methtype: 0x6a52
+  __TEXT.__oslogstring: 0x32b9e
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x384
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xceb4
+  __TEXT.__gcc_except_tab: 0xceb8
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x7098
+  __TEXT.__unwind_info: 0x70b0
   __TEXT.__eh_frame: 0x1c98
   __DATA_CONST.__auth_got: 0x1990
   __DATA_CONST.__got: 0xe68
   __DATA_CONST.__auth_ptr: 0x348
   __DATA_CONST.__const: 0x88b8
-  __DATA_CONST.__cfstring: 0x1f900
+  __DATA_CONST.__cfstring: 0x1fa60
   __DATA_CONST.__objc_classlist: 0xab0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x808
-  __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0xd38
-  __DATA_CONST.__objc_dictobj: 0x258
+  __DATA_CONST.__objc_intobj: 0x3c0
+  __DATA_CONST.__objc_arraydata: 0xd28
+  __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x4e0
-  __DATA.__objc_const: 0x29a10
-  __DATA.__objc_selrefs: 0xc770
-  __DATA.__objc_ivar: 0x1da4
+  __DATA.__objc_const: 0x29be0
+  __DATA.__objc_selrefs: 0xc7d0
+  __DATA.__objc_ivar: 0x1dc0
   __DATA.__objc_data: 0x74f0
   __DATA.__data: 0x20e8
   __DATA.__common: 0x49

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10223
+  Functions: 10248
   Symbols:   1399
-  CStrings:  24697
+  CStrings:  24767
 
CStrings:
+ "T@\"NSNumber\",&,N,V_modifiedRegularFileCount"
+ "T@\"NSNumber\",&,N,V_uploadedAssetSize"
+ "=encryption key= Failed to update key fetched from the missed encryption key DB (inode:%!l(MISSING)lu size:%!l(MISSING)lu): %!@(MISSING)"
+ "transactionError"
+ "\n SELECT \n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    SUM(IIF(restoreState == %!u(MISSING), 1, 0)),\n    COUNT(*)\n FROM Restorables\n JOIN  Domains ON\n       Domains.domainID = Restorables.domainID\n WHERE Domains.rootPath IS NOT NULL"
+ "\n UPDATE Domains\n    SET engineState = %!u(MISSING)\n  WHERE domainID = %!u(MISSING);"
+ "-[MBRestorePlanDB _domainIDForDomainName:inDB:error:]"
+ "skipDomains:error:"
+ "T@\"NSNumber\",&,N,V_unmodifiedRegularFileCount"
+ "-[MBRestorePlanDB skipDomains:error:]"
+ "-[MBRestorePlanDB _verificationStateForDomainID:error:]"
+ "setTestCommitRepairChecksumOnLightrailChecksumMismatch:"
+ "\nSELECT \n  SUM (assetSize)\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %!u(MISSING)\n   AND Restorables.restoreState != %!u(MISSING)\n   AND Restorables.restoreState != %!u(MISSING)\n GROUP BY RestorableAssets.inode;"
+ "-[MBRestorePlanDB _skipDomainID:into:error:]"
+ "\n SELECT verificationStatus\n   FROM Domains\n  WHERE domainID = %!u(MISSING);"
+ "-[MBRestorePlanDB _addRemainingProgress:forDomainID:domainName:readOnlyDB:error:]_block_invoke"
+ "=cloud-backup= Saved mutated device record"
+ "initWithDomainsNotVerifiedCount:domainsPassingVerificationCount:domainsFailingVerificationCount:domainsSkippedVerificationCount:"
+ "\n SELECT \n    IFNULL(SUM(IIF(type == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING) AND restoreState == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING) AND restoreState == %!u(MISSING), 1, 0)), 0)\n FROM   Restorables\n WHERE (restoreState = %!u(MISSING)\n     OR restoreState = %!u(MISSING)\n       )\n    AND domainID = %!u(MISSING);"
+ "_skipDomainID:into:error:"
+ "=encryption key= Failed to set updated encryption key in the missed encryption key DB (inode:%!l(MISSING)lu size:%!l(MISSING)lu): %!@(MISSING)"
+ "=encryption key= Updated key fetched from the missed encryption key DB (inode:%!l(MISSING)lu size:%!l(MISSING)lu)"
+ "@48@0:8Q16Q24Q32Q40"
+ "_domainsSkippedVerificationCount"
+ "\n UPDATE Restorables\n    SET restoreState = %!u(MISSING)\n  WHERE domainID = %!u(MISSING);"
+ "shouldTriggerDeviceRecordOpLockFailureInBackupCommit"
+ "addRepairDomainToMBCKDevice"
+ "\nSELECT RestorableAssets.inode, \nlinkCount, \nrecordIDSuffix, encryptionKey, compressionMethod, assetType, assetSize, assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %!u(MISSING)\n   AND RestorableAssets.assetState != %!l(MISSING)u\n   AND Restorables.restoreState != %!u(MISSING)\n   AND Restorables.restoreState != %!u(MISSING)\n   AND Restorables.absolutePath IS %!@(MISSING)\n GROUP BY RestorableAssets.inode;"
+ "\nSELECT \n  SUM (assetSize),\n  COUNT(*)\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %!u(MISSING)\n   AND Restorables.restoreState != %!u(MISSING)\n   AND Restorables.restoreState != %!u(MISSING)\n   AND RestorableAssets.domainID = %!u(MISSING)\n GROUP BY RestorableAssets.inode;"
+ "testCommitRepairChecksumOnLightrailChecksumMismatch"
+ "Q28@0:8I16^@20"
+ "enumerateDomainNamesByTotalAssetSize:enumerator:"
+ "setTotalSize:"
+ "-[MBRestorePlanDB restoreVerificationSummary:]"
+ "\"$\x13A\x1f\x14)\x19"
+ "_testCommitRepairChecksumOnLightrailChecksumMismatch"
+ "TQ,R,N,V_domainsSkippedVerificationCount"
+ "-[MBRestorePlanDB _addRemainingProgress:forDomainID:domainName:readOnlyDB:error:]_block_invoke_2"
+ "=cloud-backup= Failed to save mutated device record: %!@(MISSING)"
+ "outPendingRestoreSize"
+ "-[MBRestorePlanDB fetchPendingRestoreSize:remainingFileCount:totalFileCount:error:]_block_invoke_3"
+ "-[MBRestorePlanDB enumerateDomainNamesByTotalAssetSize:enumerator:]_block_invoke_2"
+ "-[MBRestorePlanDB enumerateDomainNamesByTotalAssetSize:enumerator:]_block_invoke"
+ "-[MBRestorePlanDB enumerateDomainNamesByTotalAssetSize:enumerator:]"
+ "=domain-engine= %!{(MISSING)public}@: Failed requesting asset %!@(MISSING): %!@(MISSING)"
+ "domainsSkippedVerificationCount"
+ "wasSkipped"
+ "Invalid restorable state (%!@(MISSING)) for %!@(MISSING) when returning atc restorable by absolute path"
+ "=cloud-backup= Could not find device record in account"
+ "-[MBRestorePlanDB fetchPendingRestoreSize:remainingFileCount:totalFileCount:error:]_block_invoke_2"
+ "_addRemainingProgress:forDomainID:domainName:readOnlyDB:error:"
+ "\n SELECT relativePath, \nmode, \npriority, \nabsolutePath\n FROM   Restorables\n WHERE  domainID = %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n ORDER BY Restorables.type, Restorables.relativePath ASC\n LIMIT %!l(MISSING)u OFFSET %!l(MISSING)u;"
+ "restoreVerificationSummary:"
+ "=cloud-backup= Failed to fetch devices: %!@(MISSING)"
+ "outTotalFileCount"
+ "=plan= Failed to get verification state for %!@(MISSING): %!@(MISSING)"
+ "-[MBRestorePlanDB fetchPendingRestoreSize:remainingFileCount:totalFileCount:error:]_block_invoke"
+ "verifierWasRun"
+ "-[MBRestorePlanDB restoreVerificationSummary:]_block_invoke"
+ "TB,N,V_testCommitRepairChecksumOnLightrailChecksumMismatch"
+ "B36@0:8I16@20^@28"
+ "_verificationStateForDomainID:error:"
+ "-[MBRestorePlanDB _addRemainingProgress:forDomainID:domainName:readOnlyDB:error:]"
+ "TQ,N,V_totalSize"
+ "outFileCount"
+ "Legacy"
+ "\n  SELECT domain, totalAssetBytes\n    FROM Domains\nORDER BY totalAssetBytes;"
+ "=cloud-backup= Failed to fetch account record: %!@(MISSING)"
+ "addRepairDomainHMAC:"
+ "-[MBRestoreDomainEngine _downloadAssets:withFetcher:]_block_invoke"
+ "=domain-engine= %!{(MISSING)public}@: Requesting asset %!@(MISSING)"
+ "-[MBRestorePlanDB fetchPendingRestoreSize:remainingFileCount:totalFileCount:error:]"
+ "T@\"NSNumber\",&,N,V_uploadedAssetCount"
+ "_domainIDForDomainName:inDB:error:"
+ "B52@0:8@16I24@28@36^@44"
+ "snapshotFormatRestored"
- "_domainIDForDomainName:error:"
- "-[MBRestorePlanDB _addRemainingProgress:forDomainName:readOnlyDB:error:]_block_invoke"
- "-[MBRestorePlanDB fetchRestoreVerificationSummary:]_block_invoke"
- "\n SELECT relativePath, \nmode, \npriority, \nabsolutePath\n FROM   Restorables\n WHERE  domainID = %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n  AND   restoreState != %!u(MISSING)\n ORDER BY Restorables.type, Restorables.relativePath ASC\n LIMIT %!l(MISSING)u OFFSET %!l(MISSING)u;"
- "_addRemainingProgress:forDomainName:readOnlyDB:error:"
- "-[MBRestorePlanDB _domainIDForDomainName:error:]"
- "\n SELECT \n SUM(IIF(restoreState == %!d(MISSING), 1, 0)), \n COUNT(*) \n FROM Restorables"
- "\n SELECT \n    IFNULL(SUM(IIF(type == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING) AND restoreState == %!u(MISSING), 1, 0)), 0),\n    IFNULL(SUM(IIF(type == %!u(MISSING) AND restoreState == %!u(MISSING), 1, 0)), 0)\n FROM   Restorables\n  JOIN  Domains ON \n       (Restorables.domainID = Domains.domainID)\n WHERE (restoreState = %!u(MISSING) OR restoreState = %!u(MISSING))\n    AND domain = %!@(MISSING);"
- "Invalid restorable state (%!@(MISSING)) for %!@(MISSING) when returning atc restoreable by absolute path"
- "=domain-engine= %!{(MISSING)public}@: Requested asset %!@(MISSING)"
- "@40@0:8Q16Q24Q32"
- "-[MBRestorePlanDB _addRemainingProgress:forDomainName:readOnlyDB:error:]_block_invoke_2"
- "\n SELECT \n SUM (assetSize) \n FROM RestorableAssets\n WHERE assetState = %!l(MISSING)lu"
- "fetchRestoreVerificationSummary:"
- "\"$\x13A\x1f\x14%!\(MISSING)x19"
- "-[MBRestorePlanDB fetchRestoreVerificationSummary:]"
- "\nSELECT RestorableAssets.inode, \nlinkCount, \nrecordIDSuffix, encryptionKey, compressionMethod, assetType, assetSize, assetSignature, \nRestorables.size, \nRestorables.protectionClass, \nRestorables.relativePath\n FROM  RestorableAssets\n JOIN  Restorables ON \n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.domainID = %!u(MISSING)\n   AND assetState != %!l(MISSING)u\n   AND absolutePath IS %!@(MISSING)\n GROUP BY RestorableAssets.inode;"
- "\n SELECT \n   SUM (assetSize), COUNT(*) \n FROM   RestorableAssets\n  JOIN  Domains ON \n       (RestorableAssets.domainID = Domains.domainID)\n WHERE  assetState = %!u(MISSING)\n    AND domain = %!@(MISSING)"
- "verificationDidRun"
- "-[MBRestorePlanDB _addRemainingProgress:forDomainName:readOnlyDB:error:]"
- "initWithDomainsNotVerifiedCount:domainsPassingVerificationCount:domainsFailingVerificationCount:"

```
