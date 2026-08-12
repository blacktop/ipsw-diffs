## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-177.0.8.502.1
-  __TEXT.__text: 0x5aeec
-  __TEXT.__objc_methlist: 0x4634
+177.0.16.0.0
+  __TEXT.__text: 0x5b188
+  __TEXT.__objc_methlist: 0x4644
   __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x6075
+  __TEXT.__cstring: 0x6144
   __TEXT.__gcc_except_tab: 0x10c4
-  __TEXT.__oslogstring: 0xf32a
-  __TEXT.__unwind_info: 0x1088
+  __TEXT.__oslogstring: 0xf3aa
+  __TEXT.__unwind_info: 0x1098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a20
+  __DATA_CONST.__objc_selrefs: 0x2a28
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x2200
+  __DATA_CONST.__objc_arraydata: 0x21e0
   __DATA_CONST.__got: 0x328
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x6300
+  __AUTH_CONST.__cfstring: 0x6340
   __AUTH_CONST.__objc_const: 0x61b0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x550

   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x530
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xd0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0x208

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  Functions: 2065
-  Symbols:   3586
-  CStrings:  1872
+  Functions: 2069
+  Symbols:   3591
+  CStrings:  1876
 
Symbols:
+ -[CSIssueDetector isDriverCoalitionName:]
+ ___41-[CSIssueDetector isDriverCoalitionName:]_block_invoke
+ _isDriverCoalitionName:.driverRegex
+ _isDriverCoalitionName:.onceToken
+ _objc_msgSend$isDriverCoalitionName:
CStrings:
+ "(p.processName = '%@' OR p.processName = '%@' OR %@)"
+ "SELECT m.* FROM (SELECT m.* FROM XPCMetrics_OngoingRestore_14_2 AS m JOIN XPCMetrics_OngoingRestore_14_2_Array_processName AS p ON m.ID = p.FK_ID WHERE %@ AND m.timestamp < %f ORDER BY m.timestamp DESC LIMIT 1) AS m UNION SELECT m.* FROM XPCMetrics_OngoingRestore_14_2 AS m JOIN XPCMetrics_OngoingRestore_14_2_Array_processName AS p ON m.ID = p.FK_ID WHERE %@ AND m.timestamp >= %f AND m.timestamp < %f ORDER BY timestamp"
+ "Skipping coalition '%@' (CID: %@) - kernel driver coalition"
+ "^(com\\.apple\\.)?[Dd]river(Kit)?\\."
+ "isDriverCoalitionName: failed to compile driver coalition regex: %@"
+ "m.fastPassName IN (SELECT DISTINCT Name FROM PLDuetService_EventNone_DASActivityLifecycle WHERE ',' || REPLACE(InvolvedProcesses, ' ', '') || ',' LIKE '%%,%@,%%' OR ',' || REPLACE(InvolvedProcesses, ' ', '') || ',' LIKE '%%,%@,%%')"
- "SELECT m.* FROM (SELECT m.* FROM XPCMetrics_OngoingRestore_14_2 AS m JOIN XPCMetrics_OngoingRestore_14_2_Array_processName AS p ON m.ID = p.FK_ID WHERE (p.processName = '%@' OR p.processName = '%@') AND m.timestamp < %f ORDER BY m.timestamp DESC LIMIT 1) AS m UNION SELECT m.* FROM XPCMetrics_OngoingRestore_14_2 AS m JOIN XPCMetrics_OngoingRestore_14_2_Array_processName AS p ON m.ID = p.FK_ID WHERE (p.processName = '%@' OR p.processName = '%@') AND m.timestamp >= %f AND m.timestamp < %f ORDER BY timestamp"
- "com.apple.hybridsearchd"
```
