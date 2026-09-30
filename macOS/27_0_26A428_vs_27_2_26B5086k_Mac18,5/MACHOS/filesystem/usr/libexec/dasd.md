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

-2467.0.40.0.0
-  __TEXT.__text: 0x132874
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_stubs: 0x15300
-  __TEXT.__objc_methlist: 0xf7a4
+2467.40.37.0.0
+  __TEXT.__text: 0x133bc4
+  __TEXT.__auth_stubs: 0x1e40
+  __TEXT.__objc_stubs: 0x15480
+  __TEXT.__objc_methlist: 0xf84c
   __TEXT.__const: 0x1268
-  __TEXT.__objc_methname: 0x24852
-  __TEXT.__cstring: 0xc516
-  __TEXT.__oslogstring: 0xfeb9
+  __TEXT.__objc_methname: 0x24b0b
+  __TEXT.__cstring: 0xc566
+  __TEXT.__oslogstring: 0x10209
   __TEXT.__objc_classname: 0x1808
-  __TEXT.__objc_methtype: 0x30c1
-  __TEXT.__gcc_except_tab: 0x3aa4
+  __TEXT.__objc_methtype: 0x3121
+  __TEXT.__gcc_except_tab: 0x3ad8
   __TEXT.__dlopen_cstrs: 0x268
   __TEXT.__swift5_typeref: 0x8f8
   __TEXT.__swift5_capture: 0x1e4

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5080
+  __TEXT.__unwind_info: 0x50d0
   __TEXT.__eh_frame: 0xbb0
-  __DATA_CONST.__const: 0x4160
-  __DATA_CONST.__cfstring: 0xdae0
+  __DATA_CONST.__const: 0x4170
+  __DATA_CONST.__cfstring: 0xdb60
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__auth_got: 0xf10
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__auth_got: 0xf30
+  __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x2b270
-  __DATA.__objc_selrefs: 0x7ca0
-  __DATA.__objc_ivar: 0x1190
+  __DATA.__objc_const: 0x2b300
+  __DATA.__objc_selrefs: 0x7d30
+  __DATA.__objc_ivar: 0x119c
   __DATA.__objc_data: 0x3ff8
   __DATA.__data: 0x1b18
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6805
-  Symbols:   855
-  CStrings:  9639
+  Functions: 6829
+  Symbols:   858
+  CStrings:  9685
 
Symbols:
+ _dispatch_assert_queue_not$V2
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _NSFileProtectionCompleteUntilFirstUserAuthentication
CStrings:
+ "%@|v"
+ "%@|v%ld"
+ "@\"RBSProcessMonitor\""
+ "@32@0:8@16q24"
+ "Activity %s has no launch reason, skipping"
+ "Convert stream: %@ : Failed to save %lu events: %@"
+ "Convert stream: %@ : Failed to save %lu final events: %@"
+ "Convert stream: %@ : Timed out waiting for conversion to complete"
+ "ERROR Submitting Activity: %@ due to configuration limits. Please contact us to prevent this activity from getting rejected. Configuration: %@"
+ "FastPass %{public}@ v%d consumed %.1fs this run, %.1fs cumulative"
+ "FastPass %{public}@ v%d has consumed %.1fs of its %.1fs budget, %.1fs remaining"
+ "FastPassConsumedRuntime"
+ "Override status: %@"
+ "T@\"NSMutableSet\",&,N,V_suspendedBundleIDs"
+ "T@\"RBSProcessMonitor\",&,N,V_suspensionMonitor"
+ "TB,N,V_suspensionSendPending"
+ "_suspendedBundleIDs"
+ "_suspensionMonitor"
+ "_suspensionSendPending"
+ "accrueFastPassRuntimeForActivity:"
+ "addConsumedRuntime:forFastPass:semanticVersion:"
+ "clearConsumedRuntimeForFastPass:resetAll:"
+ "consumedRuntimeForFastPass:semanticVersion:"
+ "consumedRuntimeKeyForFastPass:semanticVersion:"
+ "d32@0:8@16q24"
+ "d40@0:8@16q24d32"
+ "defaultPathIsInexpensive"
+ "defaultPathIsUnconstrained"
+ "directBiomeWriterStreamNames"
+ "initWithDKStreamIdentifier:"
+ "isConstrained"
+ "isExpensive"
+ "isMindPalaceAmbientActivity"
+ "isMindPalaceUserInitiatedActivity"
+ "mindPalaceAmbient == 1"
+ "remainingRuntimeForFastPass:semanticVersion:budget:"
+ "setSuspendedBundleIDs:"
+ "setSuspensionMonitor:"
+ "setSuspensionSendPending:"
+ "suspendedBundleIDs"
+ "suspensionMonitor"
+ "suspensionSendPending"
+ "v16@?0@\"_DKEvent\"8"
+ "v40@0:8d16@24q32"
+ "writeDirectStreamName: %@ : Processed events are not valid JSON objects, skipping with error %@"
+ "writeDirectStreamName: %@ : Timed out waiting for write to complete, numberOfWrittenEvents may be an undercount"
+ "writeDirectStreamName: %@ : written %lu events, total written so far: %lu"
+ "writeDirectStreamName:toFileHandle:withEventPredicate:withEventProvider:"
+ "writeExperiment: %@ : stream %@ is in directBiomeWriterStreamNames but has no direct writer wired up"
+ "writeStream: %@ : Timed out waiting for read to complete, numberOfWrittenEvents may be an undercount"
- "ERROR Submitting Activity: %@ due to configuration limits. Please contact das-core@group.apple.com to prevent this activity from getting rejected. Configuration: %@"
- "convertKeybagLockedStream:toKnowledgeStoreStream:"
- "inexpensivePathAvailable"
- "initWithDKStreamIdentifier:contentProtection:"
```
