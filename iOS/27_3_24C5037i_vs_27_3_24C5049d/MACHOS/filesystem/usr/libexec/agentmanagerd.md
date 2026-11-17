## agentmanagerd

> `/usr/libexec/agentmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_acfuncs`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-5.6.0.0.0
-  __TEXT.__text: 0x105b30
-  __TEXT.__auth_stubs: 0x2ef0
+5.11.0.0.0
+  __TEXT.__text: 0x122904
+  __TEXT.__auth_stubs: 0x3030
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x44c8
-  __TEXT.__swift5_typeref: 0x19b2
-  __TEXT.__cstring: 0x2bc5
-  __TEXT.__swift5_capture: 0x2e78
+  __TEXT.__const: 0x4ac8
+  __TEXT.__swift5_typeref: 0x1cbc
+  __TEXT.__cstring: 0x3a75
+  __TEXT.__swift5_capture: 0x3424
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x14a8
+  __TEXT.__constg_swiftt: 0x16b4
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0xcbf
-  __TEXT.__swift5_fieldmd: 0xf84
-  __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_proto: 0x294
-  __TEXT.__swift5_types: 0x118
+  __TEXT.__swift5_reflstr: 0xe0f
+  __TEXT.__swift5_fieldmd: 0x11e4
+  __TEXT.__swift5_assocty: 0x318
+  __TEXT.__swift5_proto: 0x2d4
+  __TEXT.__swift5_types: 0x138
   __TEXT.__objc_classname: 0x529
-  __TEXT.__objc_methname: 0xed3
+  __TEXT.__objc_methname: 0xf03
   __TEXT.__objc_methtype: 0x1e0
-  __TEXT.__swift_as_entry: 0x394
-  __TEXT.__swift_as_ret: 0x480
-  __TEXT.__swift_as_cont: 0x81c
-  __TEXT.__swift5_protos: 0x38
-  __TEXT.__oslogstring: 0x4475
+  __TEXT.__swift_as_entry: 0x3f8
+  __TEXT.__swift_as_ret: 0x540
+  __TEXT.__swift_as_cont: 0x954
+  __TEXT.__swift5_protos: 0x44
+  __TEXT.__oslogstring: 0x4925
   __TEXT.__swift5_acfuncs: 0x28
-  __TEXT.__unwind_info: 0x3a80
-  __TEXT.__eh_frame: 0xaf48
-  __DATA_CONST.__const: 0x84f8
+  __TEXT.__unwind_info: 0x4630
+  __TEXT.__eh_frame: 0xca88
+  __DATA_CONST.__const: 0x95a0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__auth_got: 0x1780
-  __DATA_CONST.__got: 0xbf8
-  __DATA_CONST.__auth_ptr: 0x930
-  __DATA.__objc_const: 0x1918
+  __DATA_CONST.__auth_got: 0x1820
+  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__auth_ptr: 0x9a8
+  __DATA.__objc_const: 0x1958
   __DATA.__objc_selrefs: 0x330
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x3630
-  __DATA.__common: 0x250
+  __DATA.__data: 0x3bd0
+  __DATA.__common: 0x268
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6417
-  Symbols:   1323
-  CStrings:  646
+  Functions: 7021
+  Symbols:   1355
+  CStrings:  698
 
Symbols:
+ _$s10Foundation4DateV11distantPastACvgZ
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestV12templateNameSSSgvg
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestV13finishedSince10Foundation4DateVvg
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestV2idAA14UUIDIdentifierVyAA0G8MetadataVGvg
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestV8ResponseV5statsAGSayAA0deF0VGSg_tcfC
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestV8ResponseVMn
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestVAA18IPCRequestProtocolAAMc
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestVMa
+ _$s12AgentManager10XPCRequestO21WorkOrderStatsRequestVMn
+ _$s12AgentManager10XPCRequestO21workOrderStatsRequestyA2C04WorkefG0VcACmFWC
+ _$s12AgentManager14WorkOrderStatsV12templateName7pending7running19waitingForHydration9completed6failed9abandoned7dropped25oldestUnfinishedCreatedAt012lastFinishedT0ACSS_S7i10Foundation4DateVSgAQtcfC
+ _$s12AgentManager14WorkOrderStatsVMa
+ _$s12AgentManager14WorkOrderStatsVMn
+ _$s12AgentManager19InferenceDependencyV27requiresEmbeddingCompletionSbvg
+ _$s12AgentManager19InferenceDependencyVMn
+ _$s12GRDBInternal18StatementArgumentsV1poiyA2C_ACtFZ
+ _$s12GRDBInternal18StatementArgumentsVMn
+ _$s12GRDBInternal18StatementArgumentsVyACxcSTRzAA24DatabaseValueConvertible7ElementRpzlufC
+ _$s12GRDBInternal8DatabaseC13makeStatement3sqlAA0D0CSS_tKF
+ _$s12GRDBInternal9StatementC7execute9argumentsyAA0B9ArgumentsVSg_tKF
+ _$sSD6ValuesVMn
+ _$sSD6ValuesVyxq__GSlsMc
+ _$sSDMa
+ _$sShMa
+ _$ss10_HashTableV14occupiedBucket5afterAB0D0VAF_tF
+ _$ss15FlattenSequenceVsSlRzSl7ElementRpzrlE5IndexVMn
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsGenerativeModelSystems
+ _objc_release_x9
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "\nAND protection IN "
+ "\nAND updated_at < ?"
+ " item(s) not embedded ("
+ " since its last run at "
+ " still generating"
+ "%s never received %ld of %s's dependency items: %s"
+ "%s's dependency items%s are embedded; running it."
+ "%{public}s"
+ "%{public}s is %{public}s"
+ "Backfill for %s didn't move past %s; trying it again on the next backfill"
+ "CREATE TABLE work_order (\n    template_name TEXT NOT NULL,\n    work_order_id TEXT NOT NULL,\n    execution_group_id TEXT NOT NULL,\n    protection TEXT NOT NULL,\n    state TEXT NOT NULL,\n    error TEXT,\n    cancelled_run_count INTEGER NOT NULL DEFAULT 0,\n    run_count INTEGER NOT NULL DEFAULT 0,\n    created_at REAL NOT NULL,\n    first_run_at REAL,\n    finished_at REAL,\n    updated_at REAL NOT NULL,\n    PRIMARY KEY (template_name, work_order_id, execution_group_id)) WITHOUT ROWID;\nCREATE INDEX work_order_by_state ON work_order (state, protection);\nCREATE INDEX work_order_by_finished ON work_order (finished_at);"
+ "Could not reconcile recorded work orders: %@"
+ "Could not record work order %s of %{public}s as %{public}s: %@"
+ "DELETE FROM work_order WHERE finished_at < ?"
+ "Execution window for %s changed while checking it, skipping."
+ "Finished workOrderStatsRequest %s"
+ "GLPInsightsEmbedding"
+ "Holding %s for its dependencies' embeddings: %s; next check %s, deadline %s."
+ "INSERT INTO work_order (\n    template_name, work_order_id, execution_group_id, protection, state,\n    error, cancelled_run_count, run_count, created_at, first_run_at,\n    finished_at, updated_at)\nVALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?9)\nON CONFLICT (template_name, work_order_id, execution_group_id) DO UPDATE SET\n    protection = excluded.protection,\n    state = excluded.state,\n    error = excluded.error,\n    cancelled_run_count = MAX(cancelled_run_count, excluded.cancelled_run_count),\n    run_count = run_count + excluded.run_count,\n    first_run_at = COALESCE(first_run_at, excluded.first_run_at),\n    finished_at = excluded.finished_at,\n    updated_at = excluded.updated_at\nWHERE excluded.updated_at >= work_order.updated_at"
+ "Marked %ld work order(s) no longer pending as dropped"
+ "No execution window recorded"
+ "No work order for %s from %s; counting it as backfilled"
+ "Not waiting for %s's dependency embeddings outside a deferred pass."
+ "Not waiting for %s's dependency embeddings: %@"
+ "Not waiting for %s's dependency embeddings: the state store is off."
+ "Not waking for %s's open window: its template isn't registered here."
+ "Not waking for %s's window: its trigger is now %s."
+ "Received workOrderStatsRequest %s"
+ "Running %s at its window deadline %s without its dependencies' embeddings: %s"
+ "SELECT MAX(started) FROM (\n    SELECT MAX(dispatched_at) AS started FROM generation\n    WHERE template_name = ?1\n    UNION ALL\n    SELECT MAX(first_run_at) FROM work_order\n    WHERE template_name = ?1 AND state IN ('completed', 'failed', 'abandoned'))"
+ "SELECT gi.source_item_identifier AS identifier,\n    MIN(g.dispatched_at) AS dispatched_at,\n    (SELECT MAX(r.indexed_at) FROM item_status r\n        WHERE r.source_item_identifier = gi.source_item_identifier\n        AND (gi.set_identifier IS NULL OR r.set_identifier = gi.set_identifier)\n        AND (?3 IS NULL OR r.pipeline = ?3)) AS indexed_at\nFROM generation g\nJOIN generation_item gi ON gi.generation_id = g.id\nWHERE g.template_name = ?1 AND g.completed_at > ?2\nAND NOT EXISTS (\n    SELECT 1 FROM item_status s\n    WHERE s.source_item_identifier = gi.source_item_identifier\n    AND (gi.set_identifier IS NULL OR s.set_identifier = gi.set_identifier)\n    AND (?3 IS NULL OR s.pipeline = ?3)\n    AND (s.embedded_at >= g.dispatched_at\n        OR s.deleted_at >= g.dispatched_at\n        OR (s.failed_at >= g.dispatched_at\n            AND (s.failure_is_transient = 0\n                OR s.failure_count >= ?4))))\nGROUP BY gi.source_item_identifier\nORDER BY dispatched_at, identifier"
+ "SELECT template_name, state, COUNT(*) AS count,\n    MIN(CASE WHEN finished_at IS NULL THEN created_at END) AS oldest_unfinished,\n    MAX(finished_at) AS last_finished\nFROM work_order\nWHERE finished_at IS NULL OR finished_at >= ?\nGROUP BY template_name, state\nORDER BY template_name"
+ "SELECT template_name, work_order_id, execution_group_id FROM work_order\nWHERE state IN "
+ "UPDATE work_order SET state = ?1, finished_at = ?2, updated_at = ?2\nWHERE template_name = ?3 AND work_order_id = ?4 AND execution_group_id = ?5"
+ "WorkOrderStatsRequest"
+ "abandoned"
+ "completed"
+ "dropped"
+ "endDate"
+ "execution_group_id"
+ "failed"
+ "next check, window deadline "
+ "not set, last window "
+ "oldest_unfinished"
+ "pendingEmbeddingQuery"
+ "protectionClass"
+ "set, window open since "
+ "set, window opens "
+ "startDate"
+ "status"
+ "waitingForHydration"
+ "workOrderRecorder"
```
