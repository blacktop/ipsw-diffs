## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

-1388.4.13.0.0
-  __TEXT.__text: 0x1e27c
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x3ba0
-  __TEXT.__objc_methlist: 0x1f5c
+1418.5.4.0.0
+  __TEXT.__text: 0x23624
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x3be0
+  __TEXT.__objc_methlist: 0x1f6c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x878
-  __TEXT.__cstring: 0x1be4
-  __TEXT.__oslogstring: 0x1bc4
-  __TEXT.__objc_methname: 0x3f53
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x8c0
+  __TEXT.__cstring: 0x1c38
+  __TEXT.__oslogstring: 0x2bb7
+  __TEXT.__objc_methname: 0x3f86
   __TEXT.__objc_classname: 0x8a6
   __TEXT.__objc_methtype: 0x61f
-  __TEXT.__unwind_info: 0x778
-  __DATA_CONST.__auth_got: 0x4e0
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__const: 0x988
-  __DATA_CONST.__cfstring: 0x23e0
+  __DATA_CONST.__cfstring: 0x2460
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x4540
-  __DATA.__objc_selrefs: 0x1318
+  __DATA.__objc_const: 0x4550
+  __DATA.__objc_selrefs: 0x1330
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9879026B-79F9-325E-BA44-31A8C47B9F02
-  Functions: 632
-  Symbols:   305
-  CStrings:  1678
+  UUID: D9128952-BC56-3AFA-8711-BE9875417F44
+  Functions: 635
+  Symbols:   302
+  CStrings:  1755
 
Symbols:
+ _malloc_type_malloc
+ _strcmp
+ _sysctl
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%{public}@"
+ "%{public}@  → Collected %lu database file(s)"
+ "%{public}@  → Collected %lu network diagnostic file(s)"
+ "%{public}@  → Creating HMHomeManager with appropriate options"
+ "%{public}@  → Device does not meet criteria, skipping"
+ "%{public}@  → Found %lu memgraph(s)"
+ "%{public}@  → Homes: %lu, Current Accessory: %@"
+ "%{public}@  → Network diagnostic collector completed in %.2f seconds"
+ "%{public}@  → Network diagnostics report:\n%@"
+ "%{public}@  → No quarantine detected, skipping log archive"
+ "%{public}@  → No video analysis logs found"
+ "%{public}@  → Requesting homed to prepare for diagnostic extension"
+ "%{public}@  → Session UUID: %@"
+ "%{public}@  → Skipped (not applicable)"
+ "%{public}@  → Starting network diagnostics collection (timeout: %.0f seconds)"
+ "%{public}@  → Stopped W5Client with UUID: %@"
+ "%{public}@  → This triggers memgraph generation via ReportMemoryException"
+ "%{public}@  → Waiting for home data sync (60 second timeout)"
+ "%{public}@  → tcpdump setup completed in %.2f seconds, starting network diagnostic collector"
+ "%{public}@  ✓ Adding pcap file: %@ (%.2f MB)"
+ "%{public}@  ✓ Cascade donations collected"
+ "%{public}@  ✓ Dispatch queue info collected"
+ "%{public}@  ✓ Event counters collected (last 7 days)"
+ "%{public}@  ✓ Full log archive collected"
+ "%{public}@  ✓ Home Manager delegate callback received - homes synchronized"
+ "%{public}@  ✓ Home data synchronized successfully"
+ "%{public}@  ✓ HomeUtil dump collected (privacy level: Private)"
+ "%{public}@  ✓ HomeUtil dump collected (privacy level: Restricted)"
+ "%{public}@  ✓ Network diagnostics completed successfully in %.2f seconds"
+ "%{public}@  ✓ Preparation successful"
+ "%{public}@  ✓ Spotlight donations collected"
+ "%{public}@  ✓ Video analysis logs collected"
+ "%{public}@  ✓ Wrote network diagnostics report to: %@"
+ "%{public}@  ✗ Error enumerating network diagnostic files: %@"
+ "%{public}@  ✗ Failed to collect Cascade donations"
+ "%{public}@  ✗ Failed to collect HomeUtil dump"
+ "%{public}@  ✗ Failed to collect Spotlight donations"
+ "%{public}@  ✗ Failed to collect dispatch queue info"
+ "%{public}@  ✗ Failed to collect event counters"
+ "%{public}@  ✗ Failed to prepare: %@"
+ "%{public}@  ✗ Failed to retrieve home data within timeout, continuing anyway"
+ "%{public}@  ✗ Failed to write network diagnostics report: %@"
+ "%{public}@  ✗ Network diagnostics completed with error after %.2f seconds: %@"
+ "%{public}@  ✗ Network diagnostics timed out after %.2f seconds"
+ "%{public}@  ✗ No pcap files were generated"
+ "%{public}@  ✗ Preparation timed out after 2 minutes"
+ "%{public}@Could not find homed process"
+ "%{public}@Failed to allocate memory for process list"
+ "%{public}@Failed to get process list size: %d"
+ "%{public}@Failed to get process list: %d"
+ "%{public}@Found homed process: PID %d, start time: %.0f"
+ "%{public}@STEP %lu/%lu: Collecting Dispatch Queue Information"
+ "%{public}@STEP %lu/%lu: Collecting Endpoint Assignments"
+ "%{public}@STEP %lu/%lu: Collecting Event Counters"
+ "%{public}@STEP %lu/%lu: Collecting HomeUtil Dump (Restricted)"
+ "%{public}@STEP %lu/%lu: Collecting Memgraphs"
+ "%{public}@STEP %lu/13: Collecting Cascade Donations"
+ "%{public}@STEP %lu/13: Collecting Database Files"
+ "%{public}@STEP %lu/13: Collecting Full Log Archive"
+ "%{public}@STEP %lu/13: Collecting HomeUtil Dump (Sensitive)"
+ "%{public}@STEP %lu/13: Collecting Network Diagnostics"
+ "%{public}@STEP %lu/13: Collecting Spotlight Donations"
+ "%{public}@STEP %lu/13: Collecting Video Analysis Session Logs"
+ "%{public}@STEP 1/%lu: Initializing Home Manager"
+ "%{public}@STEP 2/%lu: Preparing homed for Diagnostic Collection"
+ "%{public}@Sensitive Information Collection: DISABLED"
+ "%{public}@Sensitive Information Collection: ENABLED"
+ "%{public}@[LogArchive] *** QUARANTINE DETECTED *** Client: %@, Size: %@ bytes (total: %@ bytes), File: %@, Time: %@"
+ "%{public}@[LogArchive] Creating log archive (Persist: 30min, HighVolume: 1hr)"
+ "%{public}@[LogArchive] Device does not meet criteria for log archive collection"
+ "%{public}@[LogArchive] Device status - Primary: %@, iPhone: %@, iPad: %@, Watch: %@"
+ "%{public}@[LogArchive] Diagnostics directory does not exist or is not accessible: %@"
+ "%{public}@[LogArchive] Failed to construct log archive: %d"
+ "%{public}@[LogArchive] Failed to create archive directory: %@"
+ "%{public}@[LogArchive] Failed to create directory %s: %@"
+ "%{public}@[LogArchive] Failed to create file: %s (errno: %d)"
+ "%{public}@[LogArchive] Failed to create parent directory: %@"
+ "%{public}@[LogArchive] Failed to decode %@ as UTF-8"
+ "%{public}@[LogArchive] Failed to fstat source: %s (errno: %d)"
+ "%{public}@[LogArchive] Failed to get file system representation for: %s"
+ "%{public}@[LogArchive] Failed to get homed start time, using statistics-based comparison"
+ "%{public}@[LogArchive] Failed to open %@: %@"
+ "%{public}@[LogArchive] Log archive created successfully"
+ "%{public}@[LogArchive] Log archive creation timed out after 2 minutes"
+ "%{public}@[LogArchive] Log archive warning: %s"
+ "%{public}@[LogArchive] Most recent quarantine: %.0f"
+ "%{public}@[LogArchive] Most recent statistics: %.0f"
+ "%{public}@[LogArchive] No statistics records found, skipping log archive collection"
+ "%{public}@[LogArchive] Quarantine detected, creating log archive"
+ "%{public}@[LogArchive] Quarantine is older than %.0f hours, skipping log archive collection"
+ "%{public}@[LogArchive] Quarantine is within %.0f hours, will collect log archive"
+ "%{public}@[LogArchive] Quarantine occurred after homed started, will collect log archive"
+ "%{public}@[LogArchive] Quarantine occurred before homed started, skipping log archive collection"
+ "%{public}@[LogArchive] homed started at: %.0f"
+ "%{public}@━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
+ "%{public}@║ HomeKit Diagnostic Extension Collection Complete"
+ "%{public}@║ HomeKit Diagnostic Extension Collection Started"
+ "%{public}@║ PHASE COMPLETED: %@, Duration: %.2f seconds"
+ "%{public}@║ PHASE STARTED: %@"
+ "%{public}@║ Sensitive Information: %@"
+ "%{public}@║ Total Attachments: %lu"
+ "%{public}@╔════════════════════════════════════════════════════════════════"
+ "%{public}@╚════════════════════════════════════════════════════════════════"
+ "HomeUtil counters read -d 7"
+ "None"
+ "attributesOfItemAtPath:error:"
+ "fileSize"
+ "homeutil counters read"
+ "homeutil-counters-read.json"
+ "version13_2"
- "%{public}@Adding pcap file: %@"
- "%{public}@Completed network diagnostics with result/error: %@/%@. Report:\n%@"
- "%{public}@Done with diagnostic attachments %@. Error: %@"
- "%{public}@Failed to prepare for diagnostic extension, error: %@"
- "%{public}@Failed to retrieve home data, but continuing anyway."
- "%{public}@Failed to write network diagnostics report to file with error: %@"
- "%{public}@Finished collection"
- "%{public}@Phase Finished: %@, elapsed: %fs"
- "%{public}@Phase Started: %@"
- "%{public}@Preparing homed for the diagnostic extension."
- "%{public}@Starting collection (allowSensitive = %@)"
- "%{public}@Starting network diagnostics session: %@"
- "%{public}@Stopped W5Client with UUID: %@"
- "%{public}@Timed out preparing."
- "%{public}@[FullLogArchive] *** QUARANTINE DETECTED *** Client: %@, Size: %@ bytes (total: %@ bytes), File: %@, Time: %@"
- "%{public}@[FullLogArchive] Creating log archive (Persist: 30min, HighVolume: 1hr)"
- "%{public}@[FullLogArchive] Device does not meet criteria for log archive collection"
- "%{public}@[FullLogArchive] Device status - Primary: %@, iPhone: %@, iPad: %@, Watch: %@"
- "%{public}@[FullLogArchive] Diagnostics directory does not exist or is not accessible: %@"
- "%{public}@[FullLogArchive] Failed to construct log archive: %d"
- "%{public}@[FullLogArchive] Failed to create archive directory: %@"
- "%{public}@[FullLogArchive] Failed to create directory %s: %@"
- "%{public}@[FullLogArchive] Failed to create file: %s (errno: %d)"
- "%{public}@[FullLogArchive] Failed to create parent directory: %@"
- "%{public}@[FullLogArchive] Failed to decode %@ as UTF-8"
- "%{public}@[FullLogArchive] Failed to fstat source: %s (errno: %d)"
- "%{public}@[FullLogArchive] Failed to get file system representation for: %s"
- "%{public}@[FullLogArchive] Failed to open %@: %@"
- "%{public}@[FullLogArchive] Log archive created successfully"
- "%{public}@[FullLogArchive] Log archive creation timed out after 2 minutes"
- "%{public}@[FullLogArchive] Log archive warning: %s"
- "%{public}@[FullLogArchive] Most recent quarantine: %.0f, Most recent statistics: %.0f"
- "%{public}@[FullLogArchive] Quarantine detected, creating log archive"
- "%{public}@[FullLogArchive] Quarantine is older than %.0f hours, skipping log archive collection"
- "%{public}@[FullLogArchive] Quarantine is recent (%.0f hours old), will collect log archive"
- "%{public}@[FullLogArchive] Time difference: %.0f seconds"
- "%{public}@homeManagerDidUpdateHomes called, home data is populated"

```
