## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x246b4
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x3a80
+1490.2.0.1.1
+  __TEXT.__text: 0x24734
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_stubs: 0x3aa0
   __TEXT.__objc_methlist: 0x1f9c
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x910
-  __TEXT.__cstring: 0x1bc2
-  __TEXT.__oslogstring: 0x4e9e
-  __TEXT.__objc_methname: 0x3ec8
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x8fc
+  __TEXT.__cstring: 0x1be7
+  __TEXT.__oslogstring: 0x4cd3
+  __TEXT.__objc_methname: 0x3ed3
   __TEXT.__objc_classname: 0x891
   __TEXT.__objc_methtype: 0x63e
   __TEXT.__unwind_info: 0x748
   __DATA_CONST.__const: 0x838
-  __DATA_CONST.__cfstring: 0x2360
+  __DATA_CONST.__cfstring: 0x23a0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__auth_got: 0x4d8
   __DATA_CONST.__got: 0x448
   __DATA.__objc_const: 0x4598
-  __DATA.__objc_selrefs: 0x12f0
+  __DATA.__objc_selrefs: 0x12f8
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x4e0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 628
-  Symbols:   300
-  CStrings:  1601
+  Symbols:   301
+  CStrings:  1598
 
Symbols:
+ _objc_retain_x27
Functions:
~ sub_100019984 : 13764 -> 1556
~ sub_10001cf48 -> sub_100019f98 : 812 -> 13764
~ sub_10001d274 -> sub_10001d55c : 1372 -> 812
~ sub_10001d7d0 -> sub_10001d888 : 240 -> 1372
~ sub_10001d8c0 -> sub_10001dde4 : 556 -> 240
~ sub_10001daec -> sub_10001ded4 : 1832 -> 556
~ sub_10001e214 -> sub_10001e100 : 7804 -> 7452
~ sub_1000228c0 -> sub_10002264c : 5596 -> 6352
CStrings:
+ "/Home.app/Home"
+ "Could not find %s process"
+ "Dumping '%@'"
+ "Dumping objects and history for %lu database(s)"
+ "Found %s process: PID %d, start time: %.0f"
+ "[%{public}@] Could not find %s process"
+ "[%{public}@] Dumping '%@'"
+ "[%{public}@] Dumping objects and history for %lu database(s)"
+ "[%{public}@] Found %s process: PID %d, start time: %.0f"
+ "[%{public}@] [LogArchive] Most recent quarantine: %.0f (homed: %.0f, Home.app: %.0f)"
+ "[%{public}@] [LogArchive] No recent quarantine for either process, skipping log archive collection"
+ "[%{public}@] [LogArchive] Process start times — homed: %.0f, Home.app: %.0f; statistics: %.0f"
+ "[%{public}@] [LogArchive] Quarantine is recent (homed: %d, Home.app: %d), will collect log archive"
+ "[LogArchive] Most recent quarantine: %.0f (homed: %.0f, Home.app: %.0f)"
+ "[LogArchive] No recent quarantine for either process, skipping log archive collection"
+ "[LogArchive] Process start times — homed: %.0f, Home.app: %.0f; statistics: %.0f"
+ "[LogArchive] Quarantine is recent (homed: %d, Home.app: %d), will collect log archive"
+ "hasSuffix:"
+ "sysdiagnose_de_home_quarantine_logarchive"
+ "system_logs.logarchive"
- "Could not find homed process"
- "DE_homed_quarantine_log_archive.logarchive"
- "Found homed process: PID %d, start time: %.0f"
- "[%{public}@] Could not find homed process"
- "[%{public}@] Found homed process: PID %d, start time: %.0f"
- "[%{public}@] [LogArchive] Failed to get homed start time, using statistics-based comparison"
- "[%{public}@] [LogArchive] Most recent quarantine: %.0f"
- "[%{public}@] [LogArchive] Most recent statistics: %.0f"
- "[%{public}@] [LogArchive] No statistics records found, skipping log archive collection"
- "[%{public}@] [LogArchive] Quarantine is older than %.0f hours, skipping log archive collection"
- "[%{public}@] [LogArchive] Quarantine is within %.0f hours, will collect log archive"
- "[%{public}@] [LogArchive] Quarantine occurred after homed started, will collect log archive"
- "[%{public}@] [LogArchive] Quarantine occurred before homed started, skipping log archive collection"
- "[%{public}@] [LogArchive] homed started at: %.0f"
- "[LogArchive] Failed to get homed start time, using statistics-based comparison"
- "[LogArchive] Most recent quarantine: %.0f"
- "[LogArchive] Most recent statistics: %.0f"
- "[LogArchive] No statistics records found, skipping log archive collection"
- "[LogArchive] Quarantine is older than %.0f hours, skipping log archive collection"
- "[LogArchive] Quarantine is within %.0f hours, will collect log archive"
- "[LogArchive] Quarantine occurred after homed started, will collect log archive"
- "[LogArchive] Quarantine occurred before homed started, skipping log archive collection"
- "[LogArchive] homed started at: %.0f"
```
