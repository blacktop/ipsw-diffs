## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2467.0.23.0.0
-  __TEXT.__text: 0x13681c
-  __TEXT.__auth_stubs: 0x1de0
-  __TEXT.__objc_stubs: 0x15260
-  __TEXT.__objc_methlist: 0xf73c
+2467.0.40.0.0
+  __TEXT.__text: 0x137c04
+  __TEXT.__auth_stubs: 0x1e00
+  __TEXT.__objc_stubs: 0x15300
+  __TEXT.__objc_methlist: 0xf7a4
   __TEXT.__const: 0x1268
-  __TEXT.__objc_methname: 0x24682
-  __TEXT.__cstring: 0xc4b6
-  __TEXT.__oslogstring: 0xfc09
+  __TEXT.__objc_methname: 0x24852
+  __TEXT.__cstring: 0xc516
+  __TEXT.__oslogstring: 0xfeb9
   __TEXT.__objc_classname: 0x1808
   __TEXT.__objc_methtype: 0x30c1
-  __TEXT.__gcc_except_tab: 0x3a38
+  __TEXT.__gcc_except_tab: 0x3aa4
   __TEXT.__dlopen_cstrs: 0x268
   __TEXT.__swift5_typeref: 0x8f8
   __TEXT.__swift5_capture: 0x1e4

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x3f60
+  __TEXT.__unwind_info: 0x3f88
   __TEXT.__eh_frame: 0xbb0
-  __DATA_CONST.__const: 0x4180
-  __DATA_CONST.__cfstring: 0xda60
+  __DATA_CONST.__const: 0x4160
+  __DATA_CONST.__cfstring: 0xdae0
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__auth_got: 0xf00
-  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__auth_got: 0xf10
+  __DATA_CONST.__got: 0xaf8
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x2b1c8
-  __DATA.__objc_selrefs: 0x7c68
-  __DATA.__objc_ivar: 0x1188
+  __DATA.__objc_const: 0x2b270
+  __DATA.__objc_selrefs: 0x7ca0
+  __DATA.__objc_ivar: 0x1190
   __DATA.__objc_data: 0x3ff8
   __DATA.__data: 0x1b18
   __DATA.__bss: 0x11b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6791
-  Symbols:   852
-  CStrings:  9618
+  Functions: 6803
+  Symbols:   855
+  CStrings:  9639
 
Symbols:
+ _IOObjectRelease
+ _NSFileHandleOperationException
+ _objc_exception_rethrow
CStrings:
+ "\t"
+ "%@::DeviceNotIdle"
+ "%@::UserAbsentWithDisplay"
+ "Device Active"
+ "Getting distinct PPSTimeSeries for subsystem: %@ category: %@ with valueFilter: %@ & metrics: %@ & timeFilter:%@"
+ "RequiredMinimumBatteryLevel"
+ "T@\"_DASDataProtectionStateMonitor\",&,N,V_dataProtectionMonitor"
+ "Trial: ConcurrencyBoostingEnabled set to %d"
+ "Trial: PhasedSchedulingEnabled set to %d"
+ "Trigger: %{public}@ is now [%@]"
+ "Unable to create stream for %@: %@"
+ "auxiliaryType"
+ "convertKeybagLockedStream:toKnowledgeStoreStream:"
+ "deviceWarm == %@"
+ "getDistinctPPSTimeSeries: metrics must be non-empty for %@/%@"
+ "getDistinctPPSTimeSeries:category:valueFilter:metrics:timeFilter:filepath:error:"
+ "initWithMetrics:predicate:timeFilter:limitCount:offsetCount:readDirection:returnsDistinctEntities:"
+ "isPrioritizedIdleStackTask"
+ "performWriteExperiments:atFileName:withTask:"
+ "refreshPhaseSchedulingGatesWithTrialManager:"
+ "refreshStaleStringInterning: %lu active StringIDs from %lu successful queries (%lu failed)"
+ "refreshStaleStringInterning: all stale StringIDs confirmed active, skipping remaining categories"
+ "refreshStaleStringInterning: error querying array columns for %{public}@: %{public}@"
+ "refreshStaleStringInterning: error querying scalar columns for %{public}@: %{public}@"
+ "refreshStaleTaskMetadata: %{public}@ returned %lu events, %lu TaskIDs still pending"
+ "refreshStaleTaskMetadata: all stale TaskIDs confirmed active, skipping remaining categories"
+ "setDataProtectionMonitor:"
+ "writeExperiments: file I/O aborted (%{public}@: %{public}@); dropping partial write"
- "Backlight On"
- "Trigger: %@ is now [%@]"
- "Unable create stream for %@: %@"
- "isPrioritizedIdleStackTasks"
- "refreshStaleStringInterning: %lu active StringIDs from %lu categories (%lu failed)"
- "refreshStaleStringInterning: error querying %{public}@: %{public}@"
- "refreshStaleTaskMetadata: %{public}@ returned %lu events"
```
