## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.74.0.0
-  __TEXT.__text: 0x3d68
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x520
+62460.40.78.0.0
+  __TEXT.__text: 0x5090
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0xdc
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x42d
+  __TEXT.__objc_methname: 0x529
   __TEXT.__objc_methtype: 0x1a7
-  __TEXT.__cstring: 0xe28
+  __TEXT.__cstring: 0x1597
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0x108
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0xc60
+  __DATA_CONST.__cfstring: 0x1660
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x198
-  __DATA.__objc_selrefs: 0x198
+  __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 34
-  Symbols:   175
-  CStrings:  212
+  Symbols:   184
+  CStrings:  305
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _strncmp
+ _strstr
Functions:
~ sub_100001374 -> sub_1000013c4 : 6368 -> 11272
CStrings:
+ "\n                       "
+ "\n  --- Episode %@ ---\n"
+ "\n  --- Episode %lu: not readable, skipping ---\n"
+ "\n  Database: %@\n"
+ "\n End of Keychain Database Corruption History\n"
+ "\n Keychain Database Corruption History \n"
+ "\nA corruption log exists at %@ but could not be read.\n"
+ "\nNo database corruption has ever been recorded.\n"
+ "                       %@\n"
+ "                       (%@ in the write-ahead log not counted)\n"
+ "                       could not open: (%@) %@\n"
+ "                       genp: %@   inet: %@   keys: %@   cert: %@\n"
+ "  At detection:      db %@, wal %@, volume free %@, read-only %@\n"
+ "  Declared corrupt:  %@\n"
+ "  Detected:          %@ (uptime %@s, OS %@)\n"
+ "  Episodes recorded: %ld (kept: %lu, dropped: %ld)\n"
+ "  Failing statement: %@\n"
+ "  File header:       not a SQLite database (first bytes: %@)\n"
+ "  File header:       page size %@, %@ pages, change counter %@/%@, last writer sqlite %@\n"
+ "  Integrity check:   %@ (%@ of %@ rows kept)\n"
+ "  Marker:            %@\n"
+ "  Note: an earlier log was unreadable and was restarted.\n"
+ "  Origin:            %@\n"
+ "  Post-mortem:       %@\n"
+ "  Prior I/O failure: YES\n"
+ "  Remediation:       %@%@\n"
+ "  SQLite error:      (%@) %@\n"
+ "  SQLite log:\n"
+ "  Schema upgrade:    %@ -> %@\n"
+ "  Stale WAL left:    YES\n"
+ " (marker age %@s)"
+ "%ld.%ld.%ld"
+ "-corruption-log.plist"
+ ":memory:"
+ "?"
+ "NO"
+ "YES"
+ "boolValue"
+ "corruptionError"
+ "dataWithContentsOfFile:options:error:"
+ "dbSize"
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
+ "filesAtDetection"
+ "hadPriorIOFailure"
+ "headerFirst32Hex"
+ "i"
+ "integerValue"
+ "integrityCheck"
+ "integrityCheckRowsTotal"
+ "integrityCheckStatus"
+ "lastWriterSqliteVersion"
+ "longLongValue"
+ "magicValid"
+ "markerAgeSeconds"
+ "markerOutcome"
+ "numberWithUnsignedInteger:"
+ "openErrmsg"
+ "openResultCode"
+ "origin"
+ "osVersion"
+ "pageSize"
+ "postMortem"
+ "priorLogUnreadable"
+ "propertyListWithData:options:format:error:"
+ "remediation"
+ "schemaVersionNew"
+ "schemaVersionOld"
+ "sizeInPages"
+ "sqliteErrmsg"
+ "sqliteExtendedCode"
+ "sqliteLog"
+ "staleWalLeftBehind"
+ "status"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "tableRowCounts"
+ "totalEpisodes"
+ "unknown"
+ "unreadable"
+ "uptimeAtDetection"
+ "versionValidFor"
+ "volumeFreeBytes"
+ "volumeReadOnly"
+ "walBytesNotCounted"
+ "walSize"
```
