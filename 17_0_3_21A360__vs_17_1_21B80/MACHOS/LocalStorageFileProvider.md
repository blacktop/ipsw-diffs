## LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

-1681.0.14.0.0
-  __TEXT.__text: 0x8b1b70
-  __TEXT.__auth_stubs: 0x4eb0
-  __TEXT.__objc_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0x1810
+1703.42.2.0.0
+  __TEXT.__text: 0x8b9970
+  __TEXT.__auth_stubs: 0x4ec0
+  __TEXT.__objc_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0x1848
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__const: 0x187dc
-  __TEXT.__cstring: 0x3368e
-  __TEXT.__objc_methname: 0x8d7f
-  __TEXT.__objc_classname: 0x3d9
-  __TEXT.__objc_methtype: 0x2dec
-  __TEXT.__constg_swiftt: 0xdb5c
-  __TEXT.__swift5_typeref: 0xd783
+  __TEXT.__const: 0x18b4c
+  __TEXT.__cstring: 0x33eee
+  __TEXT.__objc_methname: 0x902d
+  __TEXT.__objc_classname: 0x3ef
+  __TEXT.__objc_methtype: 0x2e32
+  __TEXT.__constg_swiftt: 0xde98
+  __TEXT.__swift5_typeref: 0xd863
   __TEXT.__swift5_builtin: 0x5dc
-  __TEXT.__swift5_reflstr: 0x84ae
-  __TEXT.__swift5_fieldmd: 0x7b28
+  __TEXT.__swift5_reflstr: 0x858e
+  __TEXT.__swift5_fieldmd: 0x7bf8
   __TEXT.__swift5_assocty: 0x1a18
   __TEXT.__swift5_proto: 0x12bc
-  __TEXT.__swift5_types: 0x81c
-  __TEXT.__swift5_capture: 0x11364
+  __TEXT.__swift5_types: 0x838
+  __TEXT.__swift5_capture: 0x115c8
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__ustring: 0x30
-  __TEXT.__oslogstring: 0xb84
+  __TEXT.__oslogstring: 0xc6e
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__unwind_info: 0x114d4
-  __TEXT.__eh_frame: 0x1fdb8
-  __DATA_CONST.__auth_got: 0x2768
-  __DATA_CONST.__got: 0xd88
-  __DATA_CONST.__auth_ptr: 0x4b0
-  __DATA_CONST.__const: 0x3d130
-  __DATA_CONST.__cfstring: 0x7a0
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__unwind_info: 0x115e0
+  __TEXT.__eh_frame: 0x1fdc8
+  __DATA_CONST.__auth_got: 0x2770
+  __DATA_CONST.__got: 0xd98
+  __DATA_CONST.__auth_ptr: 0x4b8
+  __DATA_CONST.__const: 0x3da68
+  __DATA_CONST.__cfstring: 0x840
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x11630
-  __DATA.__objc_selrefs: 0x2100
+  __DATA.__objc_const: 0x11800
+  __DATA.__objc_selrefs: 0x21b0
   __DATA.__objc_protorefs: 0xf0
-  __DATA.__objc_classrefs: 0x338
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x120
-  __DATA.__objc_data: 0x2e08
-  __DATA.__data: 0x13c10
+  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_superrefs: 0x50
+  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_data: 0x2e70
+  __DATA.__data: 0x14058
   __DATA.__bss: 0x24920
   __DATA.__common: 0x728
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
   - /System/Library/PrivateFrameworks/Synapse.framework/Synapse
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28356
-  Symbols:   857
-  CStrings:  5770
+  Functions: 28510
+  Symbols:   862
+  CStrings:  5839
 
Symbols:
+ _FPDiagnosticAttributeKeyDBFParentItemID
+ _GSDocumentVersionsNameSpace
+ _NSClassFromString
+ _OBJC_CLASS_$_FPFSTapToRadarManager
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _OBJC_METACLASS_$_FPFSTapToRadarManager
- _OBJC_CLASS_$_NSKeyedUnarchiver
CStrings:
+ "\n   AND rt.conflicting_versions_in_genstore = 1\n   AND rt.rowID > "
+ "\n   AND rt.rowID > "
+ "\n   ORDER BY rt.rowID\n   LIMIT "
+ "\n ORDER BY rt.rowID\n LIMIT "
+ "\nORDER BY rt.rowID ASC\n LIMIT "
+ "%@ ‼️  done executing %{public}s%{public}s [duration %{public}s]"
+ "%@ ✅  done executing %{public}s%{public}s [duration %{public}s]"
+ ",\n       fs_structural_filename = "
+ "@56@0:8@16@24@32Q40B48B52"
+ "All"
+ "FPFSTapToRadarManager"
+ "FileProvider"
+ "FileProvider database corruption detected"
+ "RadarComponent"
+ "RadarDraft"
+ "Reimport for domain: "
+ "SELECT rowID, fs_vfs_fileid, fs_vfs_generationid, fs_id, fs_captured_content_file_id,\n              fp_captured_content_file_id, fs_structural_parent_id\nFROM reconciliation_table\nWHERE fs_id IS NOT NULL\n   OR fs_vfs_fileid IS NOT NULL\n   OR fs_captured_content_file_id IS NOT NULL\n   OR fp_captured_content_file_id IS NOT NULL\nORDER BY rowID"
+ "SELECT rt.rowID, fs.parent_id, fs.filename\n  FROM reconciliation_table AS rt\n INNER JOIN fs_snapshot AS fs ON (rt.fs_id = fs.id)\n WHERE (fs_structural_parent_id != fs.parent_id\n        OR fs_structural_filename != fs.filename)\n   AND fs_updated_fields == 0\n   AND fs_deletion_status == 0\n   AND fs_scheduling_state != "
+ "SELECT rt.rowID, rt.fs_id\n  FROM reconciliation_table AS rt\n WHERE rt.fp_content_status == "
+ "SQLDB: list dataless items with conflicts"
+ "Should not call fixupOutOfSyncFSBaseVersion on non-ItemStateVersion types"
+ "TapToRadarService"
+ "UPDATE reconciliation_table\n   SET fs_structural_parent_id = "
+ "[DEBUG] Creating a radar draft request"
+ "[DEBUG] Not internal build, ignoring tap to radar request"
+ "[DEBUG] Tap to radar returned successfuly"
+ "[WARNING] Tap to radar returned error: (%@)"
+ "_TtC9libfssync23GSRemoteVersionsManager"
+ "__itemAtURL:didResolveConflictVersionWithClientID:name:purposeID:"
+ "_executionQueue"
+ "a database corruption detected"
+ "alwaysFailInGSUpload"
+ "attempting create a domain root at %s, but that path already exists and is owned by a different provider %s, expected %s"
+ "attempting create a domain root at %s, but that path already exists and is owned by existing domain %s, expected %s"
+ "attempting create a domain root at %s, but that path already exists and is owned by missing domain %s, expected %s"
+ "clean-remote-versions"
+ "com.apple.fileprovider.ttr-queue"
+ "crashReporterKey"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
+ "didChange(_:completionHandler:)"
+ "documentURL"
+ "domainForIdentifier:reason:"
+ "enumeratorAtPath:"
+ "failed to remove %s: %@"
+ "fixup-conflicts-in-gs-for-dataless-items"
+ "fixup-out-of-sync-fs-base-version"
+ "fp_isFileProviderError:"
+ "gsManager"
+ "implement FullScanRowIDJob.executeFromRowID in sub-class"
+ "initWithDatabasesBackupsPaths:providerDomainID:domainUserInfo:reason:usingFPFS:iCDPackageDetection:"
+ "initWithName:version:identifier:"
+ "libfssync/Maintenance.swift"
+ "listRemoteVersionsOfItem(at:includeCachedVersions:completionHandler:)"
+ "listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:"
+ "nameSpace"
+ "remove-conflict-stuck-in-the-wharf"
+ "removeStuckConflictsFromTheWharf(conflictsToRemove:completion:)"
+ "removeStuckWharfPropagationItems(completion:)"
+ "requestTapToRadarWithTitle:description:componentName:componentVersion:componentID:keywords:attachments:displayReason:"
+ "requestTapToRadarWithTitle:description:keywords:attachments:displayReason:"
+ "retry(on:result:conflictsToAdd:message:error:completion:)"
+ "rootIsOwnedByDifferentProvider"
+ "root_owned_by_different_provider"
+ "scheduleFPCKRun:domainUserInfo:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:"
+ "setAttachments:"
+ "setAutoDiagnostics:"
+ "setClassification:"
+ "setComponent:"
+ "setDeleteOnAttach:"
+ "setKeywords:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setTitle:"
+ "sharedInstance"
+ "skipping compressed / unreadable object in package"
+ "storage"
+ "v32@0:8@\"FPItemID\"16@?<v@?>24"
+ "v36@0:8@\"NSURL\"16B24@?<v@?@\"FPItem\"@\"NSArray\"@\"NSError\">28"
+ "v56@0:8@16@24@32@40@48"
+ "v80@0:8@16@24@32@40Q48Q56B64B68@?72"
+ "v80@0:8@16@24@32@40q48@56@64@72"
+ "wharf/propagate/"
+ "⚔️  Impossible to fetch URL for Item %s, can not remove all remote versions for this item..."
+ "⚔️  Item %s not found, can not remove all remote versions for this item..."
+ "⚔️  Putting remote version %s into Genstore..."
+ "⚔️  Removing all remote versions for item %s ..."
+ "⚔️  associate thumnail %s for loser %s"
+ "⚔️  enter group for thumbnail fetching"
+ "👽 item content status is %{public}s instead of content:import: %{public}s"
- "%@ ‼️  done executing %{public}s%{public}s [duration %s]"
- "%@ ✅  done executing %{public}s%{public}s [duration %s]"
- "@48@0:8@16@24Q32B40B44"
- "SELECT rowID, fs_vfs_fileid, fs_vfs_generationid, fs_id, fs_captured_content_file_id,\n              fp_captured_content_file_id, fs_structural_parent_id\nFROM reconciliation_table\nWHERE fs_is IS NOT NULL\n   OR fs_vfs_fileid IS NOT NULL\n   OR fs_captured_content_file_id IS NOT NULL\n   OR fp_captured_content_file_id IS NOT NULL\nORDER BY rowID"
- "attempting create a domain at %s, but that path already exists and is owned by existing domain %s, expected %s"
- "attempting create a domain at %s, but that path already exists and is owned by missing domain %s, expected %s"
- "didChange(_:)"
- "didChangeItemID:"
- "domainWithID:"
- "initWithDatabasesBackupsPaths:providerDomainID:reason:usingFPFS:iCDPackageDetection:"
- "listRemoteVersionsOfItem(at:completionHandler:)"
- "listRemoteVersionsOfItemAtURL:completionHandler:"
- "scheduleFPCKRun:databasesBackupsPath:urls:options:reason:fpfs:iCDPackageDetection:completionHandler:"
- "skip item not importing from disk"
- "v24@0:8@\"FPItemID\"16"
- "v32@0:8@\"NSURL\"16@?<v@?@\"FPItem\"@\"NSArray\"@\"NSError\">24"
- "v72@0:8@16@24@32Q40Q48B56B60@?64"
- "⚔️  Impossible to fetch URL for Item %s, can not remove all losers for this item..."
- "⚔️  Item %s not found, can not remove all losers for this item..."
- "⚔️  Removing all conflict losers for item %s ..."
- "⚔️  failed to associate thumbnail to Loser %{public}s: %@"
- "⚔️  fetching thumbnails for losers %s"

```
