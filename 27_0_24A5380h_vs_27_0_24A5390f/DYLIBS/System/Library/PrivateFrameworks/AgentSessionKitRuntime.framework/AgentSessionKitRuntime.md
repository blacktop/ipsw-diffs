## AgentSessionKitRuntime

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/AgentSessionKitRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-287.0.6.0.0
-  __TEXT.__text: 0x1fc0b8
-  __TEXT.__objc_methlist: 0x6cc
-  __TEXT.__const: 0x197ec
-  __TEXT.__cstring: 0x1f7e
-  __TEXT.__swift5_typeref: 0x715d
-  __TEXT.__swift5_capture: 0x2494
-  __TEXT.__oslogstring: 0x79cc
-  __TEXT.__constg_swiftt: 0x37c4
-  __TEXT.__swift5_reflstr: 0x5ce1
-  __TEXT.__swift5_fieldmd: 0x4b24
+291.1.0.5.0
+  __TEXT.__text: 0x205ad4
+  __TEXT.__objc_methlist: 0x6e4
+  __TEXT.__const: 0x19a8c
+  __TEXT.__cstring: 0x200e
+  __TEXT.__swift5_typeref: 0x7215
+  __TEXT.__swift5_capture: 0x270c
+  __TEXT.__oslogstring: 0x801c
+  __TEXT.__constg_swiftt: 0x3900
+  __TEXT.__swift5_reflstr: 0x5d91
+  __TEXT.__swift5_fieldmd: 0x4bdc
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_mpenum: 0x60
   __TEXT.__swift5_assocty: 0x10c0
-  __TEXT.__swift5_proto: 0x920
-  __TEXT.__swift5_types: 0x3f8
-  __TEXT.__swift_as_entry: 0x2bc
-  __TEXT.__swift_as_ret: 0x28c
-  __TEXT.__swift_as_cont: 0x708
-  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x92c
+  __TEXT.__swift5_types: 0x404
+  __TEXT.__swift_as_entry: 0x2e8
+  __TEXT.__swift_as_ret: 0x2b4
+  __TEXT.__swift_as_cont: 0x77c
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_types2: 0x10
-  __TEXT.__unwind_info: 0x8e18
-  __TEXT.__eh_frame: 0x11500
+  __TEXT.__unwind_info: 0x9458
+  __TEXT.__eh_frame: 0x11cf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0x320
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x750
+  __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__got: 0x1390
-  __AUTH_CONST.__const: 0x7cd8
-  __AUTH_CONST.__objc_const: 0xa008
-  __AUTH_CONST.__auth_got: 0x2428
+  __DATA_CONST.__got: 0x13b8
+  __AUTH_CONST.__const: 0x83c0
+  __AUTH_CONST.__objc_const: 0xa2f0
+  __AUTH_CONST.__auth_got: 0x2478
   __AUTH.__objc_data: 0x1700
-  __AUTH.__data: 0x4500
-  __DATA.__data: 0x3730
-  __DATA.__bss: 0x10520
+  __AUTH.__data: 0x47b0
+  __DATA.__data: 0x3760
+  __DATA.__bss: 0x105c0
   __DATA.__common: 0x120
   __DATA_DIRTY.__objc_data: 0x5c8
-  __DATA_DIRTY.__data: 0x3d58
+  __DATA_DIRTY.__data: 0x3d18
   __DATA_DIRTY.__bss: 0x3900
   __DATA_DIRTY.__common: 0x108
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14394
-  Symbols:   299
-  CStrings:  678
+  Functions: 14596
+  Symbols:   303
+  CStrings:  704
 
Symbols:
+ _OBJC_CLASS_$_CKMergeableDeltaMetadata
+ _OBJC_CLASS_$_CKMergeableDeltaVectors
+ _OBJC_CLASS_$_CKReplaceDeltasRequest
+ _OBJC_CLASS_$_CKReplaceMergeableDeltasOperation
CStrings:
+ "%{public}s: expired"
+ "DailyMaintenanceTask: deleted %ld expired sessions"
+ "DailyMaintenanceTask: deleted %ld stale transient sessions"
+ "DailyMaintenanceTask: expired session cleanup failed: %{public}@"
+ "DailyMaintenanceTask: stale transient session cleanup failed: %{public}@"
+ "Reserved cloud identifier (awaiting ingest): %s"
+ "WeeklyMaintenanceTask: delta compaction complete"
+ "WeeklyMaintenanceTask: running delta compaction"
+ "applyToDatabase: promoted transient session to persistable session=%{public}s"
+ "com.apple.GenerativeFunctions.agentstored.WeeklyMaintenance"
+ "compactSession: compacted %{public}ld deltas → 1 session=%{public}s"
+ "compactSession: refusing to compact from empty/degraded state session=%{public}s live=%{public}ld vector=%{public}ld"
+ "compactSession: session=%{public}s failed: %{public}@"
+ "compactSession: skip (%{public}ld < %{public}ld) session=%{public}s"
+ "compactSession: skip (local behind server, not caught up) session=%{public}s"
+ "compactSession: skip (not synced) session=%{public}s"
+ "compactSession: skip (pending local changes) session=%{public}s"
+ "compactSessionDeltas(count: "
+ "delta compaction eligibility query failed: %{public}@"
+ "enhanced siri availability changed"
+ "enqueuing %{public}ld sessions for delta compaction"
+ "fullStateDelta: expected exactly one delta, got %{public}ld"
+ "no eligible sessions found for compaction"
+ "replaceMergeableDeltas(_:sessionId:)"
+ "replaceMergeableDeltas: session=%{public}s operation failed: %{public}@"
+ "replaceMergeableDeltas: session=%{public}s per-replacement failed: %{public}@"
+ "replaceMergeableDeltas: session=%{public}s replace confirmed"
+ "replaceMergeableDeltas: session=%{public}s replacing %{public}ld deltas with %{public}ld"
+ "started enhanced-Siri availability observation"
+ "sync coordinator created (eligible)"
+ "sync coordinator creation skipped, device ineligible"
- "MaintenanceTask: deleted %ld expired sessions"
- "MaintenanceTask: deleted %ld stale transient sessions"
- "MaintenanceTask: expired"
- "MaintenanceTask: expired session cleanup failed: %@"
- "MaintenanceTask: stale transient session cleanup failed: %@"
```
