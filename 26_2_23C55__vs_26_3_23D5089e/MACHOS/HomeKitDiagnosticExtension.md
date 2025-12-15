## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

-1388.3.6.0.0
-  __TEXT.__text: 0x1c844
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x3a80
+1388.4.6.0.0
+  __TEXT.__text: 0x1e27c
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x3ba0
   __TEXT.__objc_methlist: 0x1f5c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x708
-  __TEXT.__cstring: 0x1b0c
-  __TEXT.__oslogstring: 0x1576
-  __TEXT.__objc_methname: 0x3eb2
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x878
+  __TEXT.__cstring: 0x1be4
+  __TEXT.__oslogstring: 0x1bc4
+  __TEXT.__objc_methname: 0x3f53
   __TEXT.__objc_classname: 0x8a6
   __TEXT.__objc_methtype: 0x61f
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x950
-  __DATA_CONST.__cfstring: 0x22a0
+  __TEXT.__unwind_info: 0x778
+  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__const: 0x988
+  __DATA_CONST.__cfstring: 0x23e0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x4540
-  __DATA.__objc_selrefs: 0x12d0
+  __DATA.__objc_selrefs: 0x1318
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CE329520-D2E2-35BC-8F9A-B6A3D28EFED1
-  Functions: 630
-  Symbols:   287
-  CStrings:  1626
+  UUID: 05437EB3-EFE8-3FFC-8885-69F11FE8AFEB
+  Functions: 632
+  Symbols:   305
+  CStrings:  1678
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OSLogConstructArchive
+ _OSLogConstructHighVolumeAgeLimit
+ _OSLogConstructHighVolumeSizeLimit
+ _OSLogConstructPersistAgeLimit
+ _OSLogConstructPersistSizeLimit
+ _OSLogConstructSignpostAgeLimit
+ _OSLogConstructSignpostSizeLimit
+ _OSLogConstructSpecialAgeLimit
+ _OSLogConstructSpecialSizeLimit
+ ___error
+ _close
+ _dispatch_get_global_queue
+ _fstat
+ _open
+ _read
+ _write
CStrings:
+ "%{public}@[FullLogArchive] *** QUARANTINE DETECTED *** Client: %@, Size: %@ bytes (total: %@ bytes), File: %@, Time: %@"
+ "%{public}@[FullLogArchive] Creating log archive (Persist: 30min, HighVolume: 1hr)"
+ "%{public}@[FullLogArchive] Device does not meet criteria for log archive collection"
+ "%{public}@[FullLogArchive] Device status - Primary: %@, iPhone: %@, iPad: %@, Watch: %@"
+ "%{public}@[FullLogArchive] Diagnostics directory does not exist or is not accessible: %@"
+ "%{public}@[FullLogArchive] Failed to construct log archive: %d"
+ "%{public}@[FullLogArchive] Failed to create archive directory: %@"
+ "%{public}@[FullLogArchive] Failed to create directory %s: %@"
+ "%{public}@[FullLogArchive] Failed to create file: %s (errno: %d)"
+ "%{public}@[FullLogArchive] Failed to create parent directory: %@"
+ "%{public}@[FullLogArchive] Failed to decode %@ as UTF-8"
+ "%{public}@[FullLogArchive] Failed to fstat source: %s (errno: %d)"
+ "%{public}@[FullLogArchive] Failed to get file system representation for: %s"
+ "%{public}@[FullLogArchive] Failed to open %@: %@"
+ "%{public}@[FullLogArchive] Log archive created successfully"
+ "%{public}@[FullLogArchive] Log archive creation timed out after 2 minutes"
+ "%{public}@[FullLogArchive] Log archive warning: %s"
+ "%{public}@[FullLogArchive] Most recent quarantine: %.0f, Most recent statistics: %.0f"
+ "%{public}@[FullLogArchive] Quarantine detected, creating log archive"
+ "%{public}@[FullLogArchive] Quarantine is older than %.0f hours, skipping log archive collection"
+ "%{public}@[FullLogArchive] Quarantine is recent (%.0f hours old), will collect log archive"
+ "%{public}@[FullLogArchive] Time difference: %.0f seconds"
+ "/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed"
+ "/private/var/db/diagnostics"
+ "DE_homed_quarantine_log_archive.logarchive"
+ "Full Log Archive"
+ "JSONObjectWithData:options:error:"
+ "URLByDeletingLastPathComponent"
+ "client"
+ "closeFile"
+ "doubleValue"
+ "file"
+ "fileHandleForReadingFromURL:error:"
+ "fileSystemRepresentation"
+ "homes"
+ "i20@?0i8r*12"
+ "isCurrentDevice"
+ "logd quarantine"
+ "logd statistics"
+ "logdata.statistics.0.jsonl"
+ "logdata.statistics.1.jsonl"
+ "readDataToEndOfFile"
+ "record"
+ "residentDevices"
+ "sizeBytes"
+ "status"
+ "stringByAppendingPathComponent:"
+ "totalBytes"
+ "unixTime"
+ "v16@?0r*8"
- "/var/mobile/Library/Logs/CrashReporter"
- "DiagnosticLogs"
- "HomeKit Logs"
- "HomeKit.(.)*.log(.gz)?"
- "filesInDir:matchingPattern:excludingPattern:"
- "modificationDate"
- "q24@?0@8@16"
- "sortUsingComparator:"

```
