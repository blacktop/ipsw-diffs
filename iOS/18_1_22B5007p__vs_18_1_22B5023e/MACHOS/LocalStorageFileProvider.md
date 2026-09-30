## LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

-2732.0.44.0.0
-  __TEXT.__text: 0x911c20
-  __TEXT.__auth_stubs: 0x50f0
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x1be8
+2732.0.85.0.0
+  __TEXT.__text: 0x915014
+  __TEXT.__auth_stubs: 0x50e0
+  __TEXT.__objc_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0x1bf0
   __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__const: 0x1b84c
-  __TEXT.__cstring: 0x2d7b6
-  __TEXT.__objc_methname: 0xac75
-  __TEXT.__objc_classname: 0x470
-  __TEXT.__objc_methtype: 0x3550
-  __TEXT.__constg_swiftt: 0xf3d4
-  __TEXT.__swift5_typeref: 0xef15
+  __TEXT.__const: 0x1bc1c
+  __TEXT.__cstring: 0x2e3c6
+  __TEXT.__objc_methname: 0xad74
+  __TEXT.__objc_classname: 0x47e
+  __TEXT.__objc_methtype: 0x3538
+  __TEXT.__constg_swiftt: 0xf7e8
+  __TEXT.__swift5_typeref: 0xeeb5
   __TEXT.__swift5_builtin: 0x6b8
-  __TEXT.__swift5_reflstr: 0x96ee
-  __TEXT.__swift5_fieldmd: 0x8830
+  __TEXT.__swift5_reflstr: 0x985e
+  __TEXT.__swift5_fieldmd: 0x8940
   __TEXT.__swift5_assocty: 0x1c20
-  __TEXT.__swift5_proto: 0x1464
-  __TEXT.__swift5_types: 0x8e8
-  __TEXT.__swift5_capture: 0x13d94
-  __TEXT.__swift5_protos: 0x70
+  __TEXT.__swift5_proto: 0x148c
+  __TEXT.__swift5_types: 0x8f8
+  __TEXT.__swift5_capture: 0x140c0
+  __TEXT.__swift5_protos: 0x74
   __TEXT.__ustring: 0x30
-  __TEXT.__oslogstring: 0xd6fa
+  __TEXT.__oslogstring: 0xd77a
   __TEXT.__swift5_mpenum: 0x100
-  __TEXT.__unwind_info: 0x10658
-  __TEXT.__eh_frame: 0x22c4c
-  __DATA_CONST.__auth_got: 0x2888
-  __DATA_CONST.__got: 0x1148
-  __DATA_CONST.__auth_ptr: 0x2fe8
-  __DATA_CONST.__const: 0x3db08
+  __TEXT.__unwind_info: 0x107d0
+  __TEXT.__eh_frame: 0x230dc
+  __DATA_CONST.__auth_got: 0x2880
+  __DATA_CONST.__got: 0x1168
+  __DATA_CONST.__auth_ptr: 0x2d28
+  __DATA_CONST.__const: 0x3e518
   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x17e88
-  __DATA.__objc_selrefs: 0x26d8
+  __DATA.__objc_const: 0x182d8
+  __DATA.__objc_selrefs: 0x2720
   __DATA.__objc_ivar: 0x134
-  __DATA.__objc_data: 0x3310
-  __DATA.__data: 0x13b68
-  __DATA.__bss: 0x27da0
-  __DATA.__common: 0x890
+  __DATA.__objc_data: 0x32a0
+  __DATA.__data: 0x13ea8
+  __DATA.__bss: 0x280a0
+  __DATA.__common: 0x8b0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24987
-  Symbols:   919
-  CStrings:  6581
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 25127
+  Symbols:   930
+  CStrings:  6646
 
Symbols:
+ _FPDomainStateDirectoryName
+ _FPDomainTemporaryDirectoryName
+ _OBJC_CLASS_$_FPDVolume
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kGSLibraryErrorDomain
- _OBJC_CLASS_$_FPFSItem
CStrings:
+ "\n\n        UNION\n\n        SELECT snap.parent_id\n        FROM parentHierarchy\n        INNER JOIN "
+ "\n        AND rec."
+ "\n  AND +snap.id != snap.parent_id\n  LIMIT 1"
+ "\n  AND other_snap.parent_id = "
+ "\n  AND scheduling_state = "
+ "\n  WHERE scheduling_state = "
+ "  - no requested TTRs"
+ " != 0\n\n        UNION\n\n        SELECT parent_rec."
+ " != 0\n         AND fs_scheduling_state_conditions != 0"
+ " != 0\n   AND rt.fs_scheduling_state_conditions != 0\n   AND parent_rt.fs_deletion_status & "
+ " != 0)\nSELECT parentHierarchy.id\nFROM parentHierarchy\nWHERE parentHierarchy.jobWaitCondition & "
+ " == 0\n        AND parent_rec."
+ " == 0\n ORDER BY rt.rowID"
+ " AS jobs\n  WHERE type = "
+ " AS snap\n        INNER JOIN reconciliation_table as parent_rec ON parent_rec."
+ " AS snap\n        WHERE snap.id = "
+ " AS snap\n  INNER JOIN reconciliation_table AS rt ON (snap.id = rt."
+ " AS snap ON snap.id = parentHierarchy.id\n        INNER JOIN reconciliation_table as parent_rec ON parent_rec."
+ " AS snap ON snap.id = parentHierarchy.id\n        WHERE snap.parent_id != snap.id\n        AND parentHierarchy.id != "
+ ")\nSELECT 1\nFROM parentHierarchy\nWHERE parentHierarchy.id = "
+ "+ previous stuck deletion state:"
+ "+ refresh speculative policy: no"
+ "+ refresh speculative policy: yes"
+ "+ stuck deletion:"
+ "AND scheduling_state_conditions = "
+ "B20@0:8i16"
+ "CREATE INDEX reconciliation_table__stuck_deletion_monitor\n          ON reconciliation_table(fs_id)\n       WHERE fs_deletion_status & "
+ "Error in checkForStuckDeletion: %!@(MISSING)"
+ "FPAdditionsGS"
+ "FileProvider stuck deletion detected"
+ "SELECT rowID, fs_id, fp_id\n  FROM reconciliation_table\n  WHERE "
+ "SELECT rt.fs_id\n  FROM reconciliation_table AS rt\nINDEXED BY reconciliation_table__stuck_deletion_monitor\nINNER JOIN fs_snapshot AS fs ON (fs.id = rt.fs_id)\nINNER JOIN reconciliation_table AS parent_rt ON (fs.parent_id = parent_rt.fs_id)\n WHERE rt.fs_deletion_status & "
+ "SQLDB: list items pending recursive deletion"
+ "SQLDB: lookupPathMatchingItemIDInCreationParentHierarchy"
+ "SQLDB: parentHierarchyContainsAncestorID"
+ "Should not procedd with eviction due to content policy prevention"
+ "Stuck deletion for domain: "
+ "WITH RECURSIVE parentHierarchy(id) AS (\n        SELECT snap.parent_id\n        FROM "
+ "WITH RECURSIVE parentHierarchy(id, jobWaitCondition) AS (\n        SELECT parent_rec."
+ "[GlobalProgress] Publishing %!s(MISSING)"
+ "_id = snap.id\n        WHERE snap.id = "
+ "_id = snap.parent_id\n        INNER JOIN reconciliation_table as rec ON rec."
+ "_id = snap.parent_id\n        WHERE snap.parent_id != snap.id\n        AND parentHierarchy.jobWaitCondition & "
+ "_id)\n  INNER JOIN "
+ "_id)\n  WHERE snap.parent_id = "
+ "_id, parent_rec."
+ "_pendingBackgroundDownloadsCounter"
+ "_scheduling_state_conditions\n        FROM "
+ "_scheduling_state_conditions\n        FROM parentHierarchy\n        INNER JOIN "
+ "_snapshot AS other_snap ON (other_snap.id = rt."
+ "a stuck deletion detected"
+ "com.apple.fileproviderd.content-policy"
+ "com.apple.metadata:kMDLabel_"
+ "databaseLimit"
+ "downloadSchedulerRunning"
+ "evictionBytheUser"
+ "findProviderDomainDirectory:location:error:"
+ "fp_GSInvalidStorageError"
+ "fp_isGSErrorWithCode:"
+ "fp_isGSInvalidStorageError"
+ "fsEventStreamIsStable"
+ "getProviderDomainID:location:foundDomainID:error:"
+ "isEventStreamIdle"
+ "isRefreshingSpeculativePolicy"
+ "itemWasPathMatching"
+ "known folder is a symlink to the logical location, deleting the symlink"
+ "pace-speculativeContentPolicy-updates"
+ "phase"
+ "prettyNameForDomain:"
+ "previousRecursiveDeletionRoots"
+ "removeItemAtPath:error:"
+ "removedURL"
+ "rootURLForLocation:error:"
+ "speculativeRefreshInheritedContentPolicyMaximumJobs"
+ "stuck-deletion-monitor.plist"
+ "stuckDeletionMonitor"
+ "supportPathForDomain:failIfNotExisting:error:"
+ "supportsRemoteVersions"
+ "♻️ forcing bounce of colliding item %!s(MISSING) as cycle with %!s(MISSING) was broken at creation time"
+ "⧗conditionalCpuRuntime"
+ "⧗contentPolicyRefreshRuntime"
+ "💂🏼\u200d♀️  TTR-ing stuck deletion:\n%!s(MISSING)"
+ "💂🏼\u200d♀️  evaluating stuck deletion"
- " AS other_snap ON (other_snap.id = "
- " AS snap\n INNER JOIN reconciliation_table AS rt ON (snap.id = rt."
- ")\n   AND +snap.id != snap.parent_id\n LIMIT 1"
- "Failed to provide stateDirectoryURL because domain is invalidated"
- "Failed to provide temporaryDirectoryURL because domain is invalidated"
- "[GlobalProgress] Publishing %!s(MISSING) for %!{(MISSING)public}s"
- "_id)\n INNER JOIN "
- "couldn't retrieve provider domainID from %!s(MISSING): %!@(MISSING)"
- "couldn't upgrade domain xattr on %!s(MISSING): %!@(MISSING)"
- "fp_isFileProviderInternalError:"
- "no provider for "
- "pendingBackgroundDownloadsCounter"
- "purgatoryURL"
- "stateDirectoryURL(completionHandler:)"
- "stateDirectoryURLWithCompletionHandler:"
- "temporaryDirectoryURL(completionHandler:)"
- "temporaryDirectoryURLWithCompletionHandler:"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"

```
