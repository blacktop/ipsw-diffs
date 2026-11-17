## CorePersonalizationRuntime

> `/System/Library/PrivateFrameworks/CorePersonalizationRuntime.framework/CorePersonalizationRuntime`

```diff

-5.8.0.2.0
-  __TEXT.__text: 0x53471c
+5.12.0.0.0
+  __TEXT.__text: 0x53ee5c
   __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x36e78
-  __TEXT.__cstring: 0x18ccf
-  __TEXT.__swift5_typeref: 0xc20c
-  __TEXT.__swift5_capture: 0x8ee8
-  __TEXT.__swift5_reflstr: 0xa18a
+  __TEXT.__const: 0x37058
+  __TEXT.__cstring: 0x18eaf
+  __TEXT.__swift5_typeref: 0xc33e
+  __TEXT.__swift5_capture: 0x8bcc
+  __TEXT.__swift5_reflstr: 0xa22a
   __TEXT.__swift5_assocty: 0x2d90
-  __TEXT.__constg_swiftt: 0x8ec0
-  __TEXT.__swift5_fieldmd: 0xea2c
-  __TEXT.__swift5_builtin: 0x190
-  __TEXT.__swift5_proto: 0x3004
-  __TEXT.__swift5_types: 0xd68
-  __TEXT.__oslogstring: 0x88cf
-  __TEXT.__swift5_mpenum: 0x1ac
-  __TEXT.__swift_as_entry: 0x11c8
-  __TEXT.__swift_as_ret: 0x1828
-  __TEXT.__swift_as_cont: 0x2600
+  __TEXT.__constg_swiftt: 0x8f54
+  __TEXT.__swift5_fieldmd: 0xeac4
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_proto: 0x300c
+  __TEXT.__swift5_types: 0xd70
+  __TEXT.__oslogstring: 0x8b8d
+  __TEXT.__swift5_mpenum: 0x1b4
+  __TEXT.__swift_as_entry: 0x1204
+  __TEXT.__swift_as_ret: 0x1880
+  __TEXT.__swift_as_cont: 0x26d0
   __TEXT.__swift5_protos: 0xc4
-  __TEXT.__unwind_info: 0x1b5d8
-  __TEXT.__eh_frame: 0x38238
+  __TEXT.__unwind_info: 0x1af78
+  __TEXT.__eh_frame: 0x389d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1380
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3b348
-  __AUTH_CONST.__objc_const: 0x2050
-  __AUTH_CONST.__auth_got: 0x35f0
+  __AUTH_CONST.__const: 0x3acf8
+  __AUTH_CONST.__objc_const: 0x2168
+  __AUTH_CONST.__auth_got: 0x3650
   __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0xbac8
-  __DATA.__data: 0xaaf0
-  __DATA.__common: 0x4b8
+  __AUTH.__data: 0xbb28
+  __DATA.__data: 0xab90
+  __DATA.__common: 0x4d0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37838
-  Symbols:   334
-  CStrings:  2294
+  Functions: 37944
+  Symbols:   335
+  CStrings:  2308
 
Symbols:
+ _swift_retain_x9
CStrings:
+ "\nDETACH DELETE e;"
+ "\nRETURN count(e);"
+ " = $workflowName\n  AND e."
+ " IN CAST($ids AS STRING[])\n  AND e.status IS NULL"
+ " IS NOT NULL\nRETURN e."
+ " dropped as too old (no evidence event ending within "
+ " have not recorded a status, "
+ " with evidence resolving to no sensed event, which the filter cannot apply to"
+ " with no Cascade evidence and "
+ "' staleness filter — "
+ ")\nWHERE e.status IS NULL\n  AND e."
+ ". They may have been "
+ "Cascade acknowledged %ld of %ld removal(s)"
+ "Failed to get execution statuses: "
+ "Failed to get execution statuses: %@"
+ "InsightStore: Deleted workflow %s: %ld entities from %ld executions, and %ld contexts whose work orders never ran"
+ "InsightWorkflow[%s]: Could not delete expired contexts whose work orders never ran: %@"
+ "InsightWorkflow[%s]: Could not discard %ld contexts saved before work order generation failed: %@"
+ "InsightWorkflow[%s]: Deleted %ld contexts whose work orders never ran, past retention policy: %s"
+ "InsightWorkflow[%s]: Discarded %ld of %ld contexts saved before work order generation failed"
+ "MemoryServer recall named unknown executions: notOnRecord=%{public}ld unfinished=%{public}ld"
+ "MotivatorBarrierResourceWorkflow: '"
+ "MotivatorBarrierResourceWorkflow: input sources truncated at the %{public}ld-character budget — included %{public}ld of %{public}ld entries, stopped in '%{public}s'"
+ "No record of workflow executions "
+ "Workflow executions "
+ "because they are still running or ended without one."
+ "deleted by retention, or along with everything they produced."
+ "input insight(s) attributed to a sensed pattern or event with no endTime"
+ "input insight(s) whose linked endTime (oldest, or newest for evidence-checked types, where an event with none counts as past it) is past their source retention window less "
+ "waitForSignal(executionId:maxWait:)"
+ "withPriority(_:enabled:_:)"
+ "🕸️ MemoryGraph: opened handle in %ldms (migrated: %{bool,public}d)"
+ "🕸️ MemoryGraph: schema already migrated, skipping the migration"
- "\n\n## Environment\nFiled automatically by com.apple.CorePersonalization via TapToRadarKit."
- " = $isDeletion, n."
- " RETURN count(n);"
- "' is on record. It may have been deleted by retention, or belong to a run that has not finished recording its status."
- ": $identifier})\nSET n."
- "AND n.isDeletion = true"
- "CREATE NODE TABLE IF NOT EXISTS CascadeDonationState ("
- "Cascade acknowledged %ld of %ld removal(s); the rest stay owed"
- "Cascade donation: %s no longer exists; dropping its row"
- "CascadeDonationState"
- "Could not record %ld owed Cascade removal(s): %@"
- "Could not settle %ld acknowledged Cascade removal(s): %@"
- "InsightWorkflow[%s]: Could not record %ld owed donation(s): %@"
- "No workflow execution '"
- "input insight(s) whose oldest linked endTime is past their source retention window less "
- "key entityType valid "
- "name valid "
- "withBackgroundPriority(enabled:_:)"
- "🕸️ MemoryGraph: opened handle in %ldms"
```
