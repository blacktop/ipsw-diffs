## APFoundation

> `/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`

```diff

-557.1.33.0.0
-  __TEXT.__text: 0x1d100c
-  __TEXT.__objc_methlist: 0x46bc
-  __TEXT.__const: 0xf120
-  __TEXT.__cstring: 0x462d
-  __TEXT.__oslogstring: 0x49e6
+557.2.8.0.0
+  __TEXT.__text: 0x1d3e48
+  __TEXT.__objc_methlist: 0x4924
+  __TEXT.__const: 0xf1c0
+  __TEXT.__cstring: 0x47fd
+  __TEXT.__oslogstring: 0x4ba6
   __TEXT.__gcc_except_tab: 0x844
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x2bcc
-  __TEXT.__swift5_typeref: 0x1c74
+  __TEXT.__constg_swiftt: 0x2bb4
+  __TEXT.__swift5_typeref: 0x1c9a
   __TEXT.__swift5_reflstr: 0xe2e
-  __TEXT.__swift5_fieldmd: 0x197c
+  __TEXT.__swift5_fieldmd: 0x1988
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x338
-  __TEXT.__swift5_proto: 0x428
+  __TEXT.__swift5_proto: 0x438
   __TEXT.__swift5_types: 0x23c
   __TEXT.__swift5_protos: 0xa4
   __TEXT.__swift5_capture: 0x714

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x3c
-  __TEXT.__unwind_info: 0x3360
-  __TEXT.__eh_frame: 0x23f8
+  __TEXT.__unwind_info: 0x3470
+  __TEXT.__eh_frame: 0x2440
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1380
-  __DATA_CONST.__objc_classlist: 0x3b8
+  __DATA_CONST.__const: 0x1430
+  __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25b8
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_selrefs: 0x2718
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x9d0
-  __AUTH_CONST.__const: 0x9fa0
-  __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0x99a8
-  __AUTH_CONST.__objc_intobj: 0x198
+  __DATA_CONST.__got: 0xa20
+  __AUTH_CONST.__const: 0xa060
+  __AUTH_CONST.__cfstring: 0x3b80
+  __AUTH_CONST.__objc_const: 0x9fb0
+  __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1620
-  __AUTH.__objc_data: 0x540
+  __AUTH_CONST.__auth_got: 0x1638
+  __AUTH.__objc_data: 0x680
   __AUTH.__data: 0x948
-  __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x2180
+  __DATA.__objc_ivar: 0x3e8
+  __DATA.__data: 0x21e0
   __DATA.__common: 0xcc
   __DATA_DIRTY.__objc_data: 0x1810
-  __DATA_DIRTY.__data: 0x2560
-  __DATA_DIRTY.__bss: 0x1678
+  __DATA_DIRTY.__data: 0x2570
+  __DATA_DIRTY.__bss: 0x1688
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3943
-  Symbols:   774
-  CStrings:  1040
+  Functions: 4027
+  Symbols:   792
+  CStrings:  1074
 
Symbols:
+ _APDatabaseTransactionQueryPrefix
+ _APDiagnosticThrottleDefaultsKey
+ _APSimulateCrashNoKillProcessWithoutABCReport
+ _APSimulateCrashWithoutABCReport
+ _CreateDiagnosticReportSubtypeCrashSynchronously
+ _OBJC_CLASS_$_APDatabaseQueryInfo
+ _OBJC_CLASS_$_APDatabaseTelemetry
+ _OBJC_CLASS_$_APDatabaseTimingLock
+ _OBJC_CLASS_$_APDiagnosticThrottle
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_METACLASS_$_APDatabaseQueryInfo
+ _OBJC_METACLASS_$_APDatabaseTelemetry
+ _OBJC_METACLASS_$_APDatabaseTimingLock
+ _OBJC_METACLASS_$_APDiagnosticThrottle
+ _clock_gettime_nsec_np
+ _kSymptomDiagnosticReplyRateLimitExpiresIn
+ _kSymptomDiagnosticReplySuccess
+ _objc_setProperty_atomic_copy
CStrings:
+ " (DEFERRED)"
+ " (EXCLUSIVE)"
+ "%08x"
+ "%@|%@|%@"
+ "();,"
+ "(transaction)"
+ "(unknown)"
+ "APDiagnosticThrottle.suppressedUntil"
+ "DELETE"
+ "Database lock held for %llu ms"
+ "Database.CoreAnalyticsThresholdMs"
+ "Database.SlowQueryThresholdMs"
+ "DatabaseSlowQuery"
+ "Diagnostic Reporter skipped a report from excluded process %{public}@"
+ "Diagnostic Reporter suppressed a repeated report, subtype:%{public}@, key:%{public}@, description:\"%{public}@\""
+ "FROM"
+ "INSERT"
+ "INTO"
+ "OR"
+ "QueryDuration"
+ "QueryType"
+ "REPLACE"
+ "SELECT"
+ "SearchAdsSettings"
+ "TRANSACTION"
+ "TableName"
+ "ThresholdMs"
+ "UPDATE"
+ "[APDatabaseTelemetry]: Database lock held for %{public}llu ms (threshold %{public}llu ms). Type: %{public}ld, Table: %{public}@, Database: %{public}@, Version: %{public}ld, Query: %{public}@"
+ "[APDatabaseTelemetry]: Skipping Core Analytics for unmapped database: %{public}@"
+ "`\"'[]"
+ "com.apple.ap.database.telemetry"
+ "com.apple.ap.diagnosticreport"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "sqlite_master"
- "!"
```
