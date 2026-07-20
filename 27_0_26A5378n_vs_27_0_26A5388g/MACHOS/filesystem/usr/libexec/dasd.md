## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2467.0.14.0.0
-  __TEXT.__text: 0x134234
+2467.0.23.0.0
+  __TEXT.__text: 0x13681c
   __TEXT.__auth_stubs: 0x1de0
-  __TEXT.__objc_stubs: 0x14fe0
-  __TEXT.__objc_methlist: 0xf674
-  __TEXT.__const: 0x1258
-  __TEXT.__objc_methname: 0x242f2
-  __TEXT.__cstring: 0xc316
-  __TEXT.__oslogstring: 0xf959
+  __TEXT.__objc_stubs: 0x15260
+  __TEXT.__objc_methlist: 0xf73c
+  __TEXT.__const: 0x1268
+  __TEXT.__objc_methname: 0x24682
+  __TEXT.__cstring: 0xc4b6
+  __TEXT.__oslogstring: 0xfc09
   __TEXT.__objc_classname: 0x1808
   __TEXT.__objc_methtype: 0x30c1
-  __TEXT.__gcc_except_tab: 0x398c
+  __TEXT.__gcc_except_tab: 0x3a38
   __TEXT.__dlopen_cstrs: 0x268
   __TEXT.__swift5_typeref: 0x8f8
   __TEXT.__swift5_capture: 0x1e4

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x3f20
+  __TEXT.__unwind_info: 0x3f60
   __TEXT.__eh_frame: 0xbb0
-  __DATA_CONST.__const: 0x4140
-  __DATA_CONST.__cfstring: 0xd900
+  __DATA_CONST.__const: 0x4180
+  __DATA_CONST.__cfstring: 0xda60
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_intobj: 0x1368
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __DATA_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_arraydata: 0x1e0
+  __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__auth_got: 0xf00
   __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x2b198
-  __DATA.__objc_selrefs: 0x7bb0
-  __DATA.__objc_ivar: 0x1184
+  __DATA.__objc_const: 0x2b1c8
+  __DATA.__objc_selrefs: 0x7c68
+  __DATA.__objc_ivar: 0x1188
   __DATA.__objc_data: 0x3ff8
   __DATA.__data: 0x1b18
-  __DATA.__bss: 0x11a0
+  __DATA.__bss: 0x11b0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6766
+  Functions: 6791
   Symbols:   852
-  CStrings:  9573
+  CStrings:  9618
 
CStrings:
+ "Activity has primaryDomain=Default; phased scheduling must declare a real domain"
+ "Activity not BPC-allowlisted with PhasedScheduling=true"
+ "Bulk-path phased gate failed for %{public}@ (allowlisted=%d, hasRealDomain=%d) — degrading to non-phased. BGSystemTask clients should submit via the single-submit path for proper rejection."
+ "ConcurrencyBoostingEnabled"
+ "Deferring phased %{public}@ phase=%d, recency frontier=%d"
+ "EnablementPhase0"
+ "EnablementPhase1"
+ "EnablementPhase2"
+ "Not running %{public}@ immediately on submission: phase=%d is above the recency frontier; deferring to gated scheduling"
+ "Phase"
+ "Phase-preempting %{public}@ (phase=%d) to unblock frontier-phase %{public}@ (phase=%d)"
+ "Phased activity %{public}@ phase=%ld domainPriority=%ld"
+ "PhasedSchedulingEnabled"
+ "Rejecting phased submission of %{public}@: %{public}@"
+ "T@\"NSMutableDictionary\",&,N,V_intensivePreemptionReservations"
+ "_enqueueStringInterningCachePrepopulation"
+ "_enqueueTaskMetadataCachePrepopulation"
+ "_intensivePreemptionReservations"
+ "_snapshotTaskMetadataForActivity:"
+ "appstored"
+ "com.apple.appstored.ArcadePostPO"
+ "com.apple.appstored.ArcadePostSummary"
+ "domainPriority"
+ "eligiblePendingPhasedActivitiesExcluding:atDate:"
+ "holderHasLiveIntensivePreemptionReservation:atDate:"
+ "intensivePreemptionReservations"
+ "isConcurrencyBoostingEnabled"
+ "isPhaseSchedulingEnabled"
+ "isPhasedProcessingEnabled"
+ "isPhasedSchedulingActivity:"
+ "liveIntensivePreemptionReservationCountExcludingHolder:atDate:"
+ "phase"
+ "phaseFrontierForCandidateActivities:"
+ "phaseFrontierForCandidateActivities:includeRunningAndPrerunning:"
+ "phaseFrontierForGroupScopeWithRequester:runningActivities:"
+ "phaseOrderingForActivity:vs:"
+ "phasedPreemptionVictimInGroup:forFrontierRequester:"
+ "phasedSubmissionShouldDeferImmediateRun:"
+ "priorityForDomain:"
+ "refreshStaleTaskMetadata: excluded %lu stale rows from known high-frequency appstored activities from re-donation (rdar://181067888)"
+ "reserveIntensivePreemptedSlotForHolder:atDate:"
+ "setDomainPriority:"
+ "setIntensivePreemptionReservations:"
+ "setPhase:"
+ "support_concurrency_boosting"
+ "support_phased_processing"
+ "sweepExpiredIntensivePreemptionReservationsLocked:"
- "_prepopulateStringInterningCache"
- "_prepopulateTaskMetadataCache"
```
