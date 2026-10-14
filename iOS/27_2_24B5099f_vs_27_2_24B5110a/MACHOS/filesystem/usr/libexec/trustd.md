## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.74.0.0
-  __TEXT.__text: 0x59a08
-  __TEXT.__auth_stubs: 0x23c0
-  __TEXT.__objc_stubs: 0x3400
+62460.40.78.0.0
+  __TEXT.__text: 0x5b130
+  __TEXT.__auth_stubs: 0x2490
+  __TEXT.__objc_stubs: 0x3520
   __TEXT.__objc_methlist: 0xe2c
   __TEXT.__const: 0xde20
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x307d
+  __TEXT.__objc_methname: 0x312e
   __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xae0
-  __TEXT.__cstring: 0x621e
-  __TEXT.__oslogstring: 0x5f18
-  __TEXT.__unwind_info: 0x13e0
-  __DATA_CONST.__const: 0x3e70
-  __DATA_CONST.__cfstring: 0x5ea0
+  __TEXT.__cstring: 0x6650
+  __TEXT.__oslogstring: 0x6120
+  __TEXT.__unwind_info: 0x13e8
+  __DATA_CONST.__const: 0x3f38
+  __DATA_CONST.__cfstring: 0x6740
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11f0
+  __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x908
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1780
-  __DATA.__objc_selrefs: 0xe88
+  __DATA.__objc_selrefs: 0xed0
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x400

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1210
-  Symbols:   884
-  CStrings:  2240
+  Functions: 1214
+  Symbols:   897
+  CStrings:  2335
 
Symbols:
+ ___strlcpy_chk
+ _dirname_r
+ _pread
+ _rename
+ _sqlite3_close_v2
+ _statfs
+ _strcmp
+ _strlcpy
+ _strncmp
+ _strstr
+ _sysctl
+ _time
+ _unlink
CStrings:
+ "%02x"
+ "%s-wal"
+ "%s.%d.tmp"
+ "(%d) %s"
+ "-corruption-log.plist"
+ "-wal"
+ ":memory:"
+ "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}{?=CCCCBBiiiiiCI[4[160c]][128c][256c][192c]}^{sqlite3}i^{__CFArray}}8"
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
+ "SecDbCorruptionLog: unable (%{darwin.errno}d) to set protection class"
+ "SecDbCorruptionLog: unable to serialize log for %{public}@"
+ "SecDbCorruptionLog: write failed (%{darwin.errno}d)"
+ "SecDbHandleCorrupt: Tried to write corruption marker %{public}s but one already exists"
+ "SecDbSecDbProcessCorruptionMarker: found corruption marker %{public}s"
+ "appendFormat:"
+ "bytesRead"
+ "completed"
+ "corruptionError"
+ "couldNotRun"
+ "dataWithContentsOfFile:options:error:"
+ "dbDeleted"
+ "dbMtime"
+ "dbSize"
+ "dbUnlinkFailed"
+ "detectedAt"
+ "entries"
+ "episode"
+ "failingSQL"
+ "file:"
+ "fileChangeCounter"
+ "fileExistsAtPath:"
+ "fileHeader"
+ "fileURLWithPath:"
+ "filesAtDetection"
+ "genp"
+ "hadPriorIOFailure"
+ "headerFirst32Hex"
+ "immutable=1"
+ "inet"
+ "integerValue"
+ "integrityCheck"
+ "integrityCheckRowsTotal"
+ "integrityCheckStatus"
+ "kern.osversion"
+ "keys"
+ "lastWriterSqliteVersion"
+ "magicValid"
+ "markerAgeSeconds"
+ "markerOutcome"
+ "migrationFailure"
+ "noSuccessor"
+ "openErrmsg"
+ "openFailed"
+ "openResultCode"
+ "origin"
+ "osVersion"
+ "pageSize"
+ "postMortem"
+ "preexisted"
+ "priorLogUnreadable"
+ "ranAndFailed"
+ "readErrno"
+ "remediation"
+ "removeObjectsInRange:"
+ "resetOnly"
+ "schemaVersionNew"
+ "schemaVersionOld"
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
+ "stringByAppendingString:"
+ "stringWithCapacity:"
+ "tableRowCounts"
+ "totalEpisodes"
+ "unknown"
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
```
