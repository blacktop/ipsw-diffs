## securityd_system

> `/usr/libexec/securityd_system`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x3fd8c
-  __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_stubs: 0x1a80
+62460.40.78.0.0
+  __TEXT.__text: 0x42954
+  __TEXT.__auth_stubs: 0x1b90
+  __TEXT.__objc_stubs: 0x1ce0
   __TEXT.__objc_methlist: 0xf44
   __TEXT.__const: 0x270
   __TEXT.__objc_classname: 0x2f6
   __TEXT.__objc_methtype: 0xcb2
-  __TEXT.__cstring: 0x868d
-  __TEXT.__objc_methname: 0x207f
-  __TEXT.__oslogstring: 0x4330
+  __TEXT.__cstring: 0x8e13
+  __TEXT.__objc_methname: 0x2241
+  __TEXT.__oslogstring: 0x4568
   __TEXT.__gcc_except_tab: 0x304
-  __TEXT.__unwind_info: 0x1080
-  __DATA_CONST.__const: 0xb558
-  __DATA_CONST.__cfstring: 0x7fc0
+  __TEXT.__unwind_info: 0x10c8
+  __DATA_CONST.__const: 0xb6c0
+  __DATA_CONST.__cfstring: 0x89c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0xd60
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__auth_got: 0xdd8
+  __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1ba8
-  __DATA.__objc_selrefs: 0x948
+  __DATA.__objc_selrefs: 0x9e0
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x690
-  __DATA.__data: 0x1580
+  __DATA.__data: 0x1588
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x10
-  __DATA.__bss: 0x6ec
+  __DATA.__bss: 0xdfc
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1130
-  Symbols:   728
-  CStrings:  2113
+  Functions: 1147
+  Symbols:   751
+  CStrings:  2233
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSURL
+ _bzero
+ _dirname_r
+ _kSecItemCountNonSyncableLive
+ _kSecItemCountNonSyncableTombstone
+ _kSecItemCountSyncableLive
+ _kSecItemCountSyncableTombstone
+ _open
+ _pread
+ _rename
+ _sqlite3_close_v2
+ _statfs
+ _strcmp
+ _strlcpy
+ _strncmp
+ _strstr
+ _sysctl
+ _sysctlbyname
+ _time
+ _unlink
CStrings:
+ " AND agrp IN (?"
+ " GROUP BY agrp"
+ " WHERE agrp IN (?"
+ " WHERE musr = ?"
+ "%02x"
+ "%s-wal"
+ "%s.%d.tmp"
+ "(%d) %s"
+ "-corruption-log.plist"
+ "-wal"
+ ":memory:"
+ "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}{?=CCCCBBiiiiiCI[4[160c]][128c][256c][192c]}^{sqlite3}i^{__CFArray}}8"
+ "B32@0:8^@16q24"
+ "CREATE INDEX IF NOT EXISTS cert_agrp_musr_sync_tomb ON cert(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS genp_agrp_musr_sync_tomb ON genp(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS inet_agrp_musr_sync_tomb ON inet(agrp, musr, sync, tomb);"
+ "CREATE INDEX IF NOT EXISTS keys_agrp_musr_sync_tomb ON keys(agrp, musr, sync, tomb);"
+ "SELECT agrp, SUM(CASE WHEN sync=0 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=0 AND tomb=1 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=0 THEN 1 ELSE 0 END), SUM(CASE WHEN sync=1 AND tomb=1 THEN 1 ELSE 0 END) FROM %@"
+ "SELECT count(*) FROM cert"
+ "SELECT count(*) FROM genp"
+ "SELECT count(*) FROM inet"
+ "SELECT count(*) FROM keys"
+ "SecDBCheckCorrupted integrity_check returned %{public}s"
+ "SecDbCorruptionLog: close failed (%{darwin.errno}d)"
+ "SecDbCorruptionLog: log at %{public}@ was unusable, starting over"
+ "SecDbCorruptionLog: path too long: %{public}@"
+ "SecDbCorruptionLog: unable (%{darwin.errno}d) to create %s"
+ "SecDbCorruptionLog: unable (%{darwin.errno}d) to rename into place"
+ "SecDbCorruptionLog: unable to serialize log for %{public}@"
+ "SecDbCorruptionLog: write failed (%{darwin.errno}d)"
+ "SecDbHandleCorrupt: Tried to write corruption marker %{public}s but one already exists"
+ "SecDbSecDbProcessCorruptionMarker: found corruption marker %{public}s"
+ "SecServerItemCountAllWithAccessGroups query template: %@"
+ "absoluteString"
+ "accessGroups must be a non-empty CFArray, got %@"
+ "applicationID"
+ "bytesRead"
+ "com.apple.security.ckks"
+ "com.apple.security.egoIdentities"
+ "com.apple.security.octagon"
+ "com.apple.security.sos-usercredential"
+ "completed"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "corruptionError"
+ "couldNotRun"
+ "dataWithContentsOfFile:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "dateWithTimeIntervalSince1970:"
+ "dbDeleted"
+ "dbMtime"
+ "dbSize"
+ "dbUnlinkFailed"
+ "defaultManager"
+ "detectedAt"
+ "entries"
+ "episode"
+ "failingSQL"
+ "file:"
+ "fileChangeCounter"
+ "fileExistsAtPath:"
+ "fileHeader"
+ "fileSystemRepresentation"
+ "fileURLWithPath:"
+ "filesAtDetection"
+ "found sharing items, treating as sys_bound item: %{private}@"
+ "hadPriorIOFailure"
+ "headerFirst32Hex"
+ "immutable=1"
+ "initWithBytes:length:encoding:"
+ "integerValue"
+ "integrityCheck"
+ "integrityCheckRowsTotal"
+ "integrityCheckStatus"
+ "item-counts"
+ "kern.osversion"
+ "lastObject"
+ "lastWriterSqliteVersion"
+ "magicValid"
+ "markerAgeSeconds"
+ "markerOutcome"
+ "migrationFailure"
+ "noSuccessor"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "numberWithLongLong:"
+ "openErrmsg"
+ "openFailed"
+ "openResultCode"
+ "origin"
+ "osVersion"
+ "pageSize"
+ "postMortem"
+ "preexisted"
+ "priorLogUnreadable"
+ "propertyListWithData:options:format:error:"
+ "ranAndFailed"
+ "readErrno"
+ "remediation"
+ "removeObjectsInRange:"
+ "resetOnly"
+ "schemaVersionNew"
+ "schemaVersionOld"
+ "sec_count_all_with_access_groups_id"
+ "setQuery:"
+ "sizeInPages"
+ "sqlite3: (%d) %{public}s"
+ "sqliteCorrupt"
+ "sqliteErrmsg"
+ "sqliteExtendedCode"
+ "sqliteLog"
+ "sqliteNotADb"
+ "sqliteSystemErrno"
+ "staleWalLeftBehind"
+ "stringWithCapacity:"
+ "sync = 0"
+ "tableRowCounts"
+ "totalEpisodes"
+ "uptimeAtDetection"
+ "versionValidFor"
+ "volumeFreeBytes"
+ "volumeReadOnly"
+ "walBytesNotCounted"
+ "walSize"
+ "writeFailed"
+ "written"
- "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}^{sqlite3}i^{__CFArray}}8"
- "SecDBCheckCorrupted integrity_check returned %s"
- "SecDbHandleCorrupt: Tried to write corruption marker %s but one already exists"
- "SecDbSecDbProcessCorruptionMarker: found corruption marker %s"
- "v32@0:8^@16q24"
```
