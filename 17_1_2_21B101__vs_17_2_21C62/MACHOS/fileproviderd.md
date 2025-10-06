## fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

-1703.42.2.0.0
-  __TEXT.__text: 0x84c704
-  __TEXT.__auth_stubs: 0x4cb0
+1703.62.4.0.0
+  __TEXT.__text: 0x86f6d0
+  __TEXT.__auth_stubs: 0x4cd0
   __TEXT.__objc_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0x13b0
-  __TEXT.__const: 0x173ec
-  __TEXT.__cstring: 0x3166e
+  __TEXT.__objc_methlist: 0x13d0
+  __TEXT.__const: 0x175ec
+  __TEXT.__cstring: 0x324be
   __TEXT.__objc_classname: 0x2e3
-  __TEXT.__objc_methname: 0x7c7b
+  __TEXT.__objc_methname: 0x8834
   __TEXT.__objc_methtype: 0x2869
   __TEXT.__oslogstring: 0xdd8
-  __TEXT.__constg_swiftt: 0xd824
-  __TEXT.__swift5_typeref: 0xd173
-  __TEXT.__swift5_fieldmd: 0x726c
+  __TEXT.__constg_swiftt: 0xd8d8
+  __TEXT.__swift5_typeref: 0xd263
+  __TEXT.__swift5_fieldmd: 0x7308
   __TEXT.__swift5_types: 0x784
   __TEXT.__ustring: 0x30
-  __TEXT.__swift5_reflstr: 0x79ce
-  __TEXT.__swift5_capture: 0x10ecc
+  __TEXT.__swift5_reflstr: 0x7c2e
+  __TEXT.__swift5_capture: 0x11208
   __TEXT.__swift5_proto: 0x1110
   __TEXT.__gcc_except_tab: 0x424
   __TEXT.__swift5_builtin: 0x5b4
   __TEXT.__swift5_mpenum: 0xd4
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_assocty: 0x18e0
-  __TEXT.__unwind_info: 0x101f0
-  __TEXT.__eh_frame: 0x1e858
-  __DATA_CONST.__auth_got: 0x2668
+  __TEXT.__unwind_info: 0x105b4
+  __TEXT.__eh_frame: 0x1ee10
+  __DATA_CONST.__auth_got: 0x2678
   __DATA_CONST.__got: 0xd28
-  __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x3b300
+  __DATA_CONST.__auth_ptr: 0x428
+  __DATA_CONST.__const: 0x3bc50
   __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xcd48
-  __DATA.__objc_selrefs: 0x1f30
+  __DATA.__objc_const: 0xcea8
+  __DATA.__objc_selrefs: 0x2158
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x350
+  __DATA.__objc_classrefs: 0x360
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0x118
-  __DATA.__objc_data: 0x26b0
-  __DATA.__data: 0x12790
+  __DATA.__objc_data: 0x2720
+  __DATA.__data: 0x12830
   __DATA.__common: 0x548
   __DATA.__bss: 0x215a0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D62D877-4AD8-3A2B-B5BA-128FB755A7E5
-  Functions: 27201
-  Symbols:   1988
-  CStrings:  5412
+  UUID: 52C1642D-41FE-3E54-8A3E-22EE6617D19C
+  Functions: 27453
+  Symbols:   1992
+  CStrings:  5524
 
Symbols:
+ _FPWriteImportCookieForDomainURL
+ _OBJC_CLASS_$_FPImportItemPendingReconciliation
+ _OBJC_CLASS_$_FPImportItemPendingScanningDisk
+ _OBJC_CLASS_$_FPImportItemPendingScanningProvider
+ _fpfs_num_entries
- _OBJC_CLASS_$_FPImportCookie
CStrings:
+ "\n                                  AND throttle.last_error IS NOT NULL\nWHERE fp_snap.parent_id = "
+ "\n   AND rec.fp_id IS NOT NULL\nORDER BY rec.scheduling_timestamp DESC\nLIMIT 5"
+ "\n   AND throttle.job_type IN ("
+ "\n   GROUP BY rec.fp_id"
+ "\n  AND fs_snap.parent_id != fs_snap.id"
+ "\n AND fp_snap.parent_id != fp_snap.id"
+ "\n ORDER BY rec.scheduling_timestamp DESC\n LIMIT 5"
+ ")\n                                  AND throttle.state = "
+ ")\n   AND throttle.last_error IS NOT NULL"
+ ")\n   AND throttle.last_error IS NOT NULL\n GROUP BY rec.fs_id\n LIMIT 100"
+ ")\n GROUP BY rec.fs_id\n ORDER BY rec.scheduling_timestamp DESC\n LIMIT 5"
+ ")\nGROUP BY fs_disk_import_status"
+ ")\nORDER BY scheduling_timestamp ASC\nLIMIT 1"
+ ",\n                                  "
+ ",\n                                                            "
+ "Attempting to import detached folder at %{public}s into new domain %{public}s"
+ "Attempting to import existing domain at %{public}s into new domain %{public}s"
+ "Error gathering telemetry for scanning provider %@"
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithContentDiffFP"
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithContentDiffFS"
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithoutContentDiffFP"
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithoutContentDiffFS"
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithoutDiff"
+ "FPCKPendingSetInternalErrorCodeNilError"
+ "FPCKPendingSetInternalErrorDomain"
+ "Failed gathering info for item pending scanning disk %@"
+ "SELECT fp_snap.id, rec.fp_deletion_status, rec.fp_updated_fields\n  FROM FP_snapshot as fp_snap\nINNER JOIN reconciliation_table AS rec ON fp_snap.id == rec.fp_id\nWHERE fp_snap.parent_id = "
+ "SELECT fs_disk_import_status, COUNT(DISTINCT fs_id)\n  FROM reconciliation_table\n WHERE fs_disk_import_status IN ("
+ "SELECT fs_id, scheduling_timestamp, fs_disk_import_status,\n       fs_updated_fields, fp_updated_fields, fp_content_status\n  FROM reconciliation_table\n  WHERE fs_disk_import_status IN ("
+ "SELECT fs_snap.id, rec.fs_disk_import_status, rec.fs_deletion_status, rec.fs_updated_fields\n  FROM FS_snapshot as fs_snap\nINNER JOIN reconciliation_table AS rec ON fs_snap.id == rec.fs_id\nWHERE fs_snap.parent_id = "
+ "SELECT rec.fp_id, rec.fp_content_status, rec.fp_updated_fields, rec.fs_id\n  FROM reconciliation_table AS rec\nWHERE rec.fs_disk_import_status == "
+ "SELECT rec.fs_id, rec.fs_content_status, rec.fp_id\n  FROM reconciliation_table AS rec\nWHERE rec.fs_disk_import_status == "
+ "SELECT rec.fs_id, rec.item_is_flocked, throttle.job_type\n  FROM reconciliation_table AS rec\nLEFT JOIN fs_throttle AS throttle ON throttle.item_id == rec.fs_id\nWHERE rec.fs_disk_import_status == "
+ "SELECT rec.fs_id, throttle.last_error\n  FROM FP_snapshot as fp_snap\nINNER JOIN reconciliation_table AS rec ON fp_snap.id == rec.fp_id\nLEFT JOIN fp_throttle AS throttle ON throttle.item_id == rec.fp_id\n                                  AND throttle.job_type IN ("
+ "Update for pending set, db is not a sql db"
+ "attempting create a domain at %{public}s, but that path already exists and is not owned by anyone"
+ "attempting create a domain root at %{public}s, but that path already exists and is owned by a different provider %{public}s, expected %{public}s"
+ "attempting create a domain root at %{public}s, but that path already exists and is owned by existing domain %{public}s, expected %{public}s"
+ "attempting create a domain root at %{public}s, but that path already exists and is owned by missing domain %{public}s, expected %{public}s"
+ "can't create dataless root at %{public}s: file already exists"
+ "creating root at %{public}s"
+ "creating symlink from  %{public}s to detached root %{public}s"
+ "dasContext"
+ "equivalentContentVersions"
+ "equivalentMetadataVersions"
+ "equivalentStructureVersions"
+ "error fetching diagnostic attributes: %@"
+ "failed getting diagnostic attributes, %@"
+ "failed to write import cookie for domain %{public}s: %s"
+ "finished gathering import progress"
+ "gathering import progress"
+ "importProgressForItemsPendingReconciliation(completionHandler:)"
+ "importProgressForItemsPendingReconciliationWithCompletionHandler:"
+ "importProgressForItemsPendingScanningDisk(completionHandler:)"
+ "importProgressForItemsPendingScanningDiskWithCompletionHandler:"
+ "importProgressForItemsPendingScanningProvider(completionHandler:)"
+ "importProgressForItemsPendingScanningProviderWithCompletionHandler:"
+ "isRegistered"
+ "isRunning"
+ "itemPendingScanningDiskNumberOfChildrenNotPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingReconciliation"
+ "itemPendingScanningDiskNumberOfChildrenPendingRejection"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDown"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUp"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion"
+ "itemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent"
+ "itemPendingScanningProviderNumberOfChildren"
+ "itemPendingScanningProviderNumberOfChildrenFailingCreation"
+ "itemPendingScanningProviderNumberOfChildrenPendingCreation"
+ "lastRegistrationDate"
+ "marking folder %{public}s as detached from %{public}s"
+ "numberOfItemsInError"
+ "numberOfItemsInFPSnapshot"
+ "numberOfItemsPendingReconciliation"
+ "numberOfItemsPendingScanningDisk"
+ "numberOfItemsPendingScanningProvider"
+ "setDbCreationTimestamp:"
+ "setErrorDetails:"
+ "setItemIdentifier:"
+ "setItemPendingReconciliationIsLockedInDB:"
+ "setItemPendingReconciliationJobCode:"
+ "setItemPendingReconciliationJobSchedulingState:"
+ "setItemPendingScanningDiskEnumerationStatus:"
+ "setItemPendingScanningDiskHasMultiplePagesEnumeration:"
+ "setItemPendingScanningDiskNumberOfChildrenNotPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingReconciliation:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingRejection:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDown:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncDownReparent:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUp:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpDeletion:"
+ "setItemPendingScanningDiskNumberOfChildrenPendingSyncUpReparent:"
+ "setItemPendingScanningProviderEnumerationStatus:"
+ "setItemPendingScanningProviderHasMultiplePagesEnumeration:"
+ "setItemPendingScanningProviderNumberOfChildren:"
+ "setItemPendingScanningProviderNumberOfChildrenFailingCreation:"
+ "setItemPendingScanningProviderNumberOfChildrenPendingCreation:"
+ "setItemPendingScanningProviderRemovalOfDatalessBitStatus:"
+ "setItemsPendingReconciliation:"
+ "setItemsPendingScanningDisk:"
+ "setItemsPendingScanningProvider:"
+ "setLatestFolderSelectedForImport:"
+ "setLatestFolderSelectedForImportIsMonitored:"
+ "setLatestFolderSelectedForImportState:"
+ "setLatestFolderSelectedForImportTimestamp:"
+ "setLatestFolderSelectedForImportWasModifiedOnDisk:"
+ "setLatestFolderSelectedForImportWasModifiedRemotely:"
+ "setNumberOfItemsInError:"
+ "setNumberOfItemsPendingReconciliation:"
+ "setNumberOfItemsPendingScanningDisk:"
+ "setNumberOfItemsPendingScanningProvider:"
+ "setNumberOfItemsPendingSelection:"
+ "setNumberOfItemsReconciled:"
+ "setStateOfDownloadJobs:"
+ "setStateOfUploadJobs:"
+ "setStatus:"
+ "setXpcActivityDasdContext:"
+ "setXpcActivityIsActive:"
+ "setXpcActivityRegisteredWithDuet:"
+ "setXpcActivityTimeSinceLastActivation:"
+ "setXpcActivityTimeSinceLastRegistration:"
+ "taking over %{public}s"
+ "taking over domain root at %{public}s, the path already exists and is not owned by anyone"
+ "👽  enumerating %{public}s is throttled, unfaulting folder to allow user access"
+ "👽  import of %{public}s within %{public}s is throttled, unfaulting folder to allow user access"
+ "👽  missing continue-disk-import job, adding a new one"
- ")\n   AND rec.fs_id IS NOT NULL\n   AND throttle.last_error IS NOT NULL"
- ")\n   AND rec.fs_id IS NOT NULL\n   AND throttle.last_error IS NOT NULL\n GROUP BY rec.fs_id\n LIMIT 100"
- "Attempting to import detached folder at %s into new domain %s"
- "Attempting to import existing domain at %s into new domain %s"
- "attempting create a domain at %s, but that path already exists and is not owned by anyone"
- "attempting create a domain root at %s, but that path already exists and is owned by a different provider %s, expected %s"
- "attempting create a domain root at %s, but that path already exists and is owned by existing domain %s, expected %s"
- "attempting create a domain root at %s, but that path already exists and is owned by missing domain %s, expected %s"
- "can't create dataless root at %s: file already exists"
- "creating root at %s"
- "creating symlink from  %s to detached root %s"
- "initWithStatus:numberOfItemsReconciled:numberOfItemsInError:errorDetails:"
- "marking folder %s as detached from %s"
- "sessionForProvider:version:"
- "taking over %s"
- "taking over domain root at %s, the path already exists and is not owned by anyone"
- "writeCookieForDomainURL:error:"
- "👽  enumerating %s is throttled, unfaulting folder to allow user access"
- "👽  import of %s within %s is throttled, unfaulting folder to allow user access"

```
