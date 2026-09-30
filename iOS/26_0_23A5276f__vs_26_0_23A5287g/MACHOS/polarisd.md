## polarisd

> `/System/Library/PrivateFrameworks/Polaris.framework/polarisd`

```diff

-220.0.13.0.0
-  __TEXT.__text: 0x15e58
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0x1794
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x13f8
-  __TEXT.__oslogstring: 0x14a6
-  __TEXT.__objc_classname: 0x36b
-  __TEXT.__objc_methname: 0x3114
-  __TEXT.__objc_methtype: 0xcef
-  __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__auth_got: 0x808
+220.0.17.0.0
+  __TEXT.__text: 0x177c4
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x27a0
+  __TEXT.__objc_methlist: 0x190c
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x1590
+  __TEXT.__oslogstring: 0x152a
+  __TEXT.__objc_methname: 0x349d
+  __TEXT.__objc_classname: 0x381
+  __TEXT.__objc_methtype: 0xd9c
+  __TEXT.__gcc_except_tab: 0x608
+  __TEXT.__unwind_info: 0x578
+  __DATA_CONST.__auth_got: 0x828
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x720
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x31f8
-  __DATA.__objc_selrefs: 0xc00
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_const: 0x3468
+  __DATA.__objc_selrefs: 0xc88
+  __DATA.__objc_ivar: 0x258
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x440
   __DATA.__thread_vars: 0x60
   __DATA.__thread_bss: 0x38
-  __DATA.__bss: 0x10b0
-  __DATA.__common: 0x1db8
+  __DATA.__bss: 0x10a0
+  __DATA.__common: 0x1db0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 7AB9613F-1BDF-3D4C-9D1F-AE97C43156CC
-  Functions: 609
-  Symbols:   327
-  CStrings:  1087
+  UUID: 6035BDD4-B929-36A5-8C98-300803A83EE6
+  Functions: 639
+  Symbols:   331
+  CStrings:  1137
 
Symbols:
+ _malloc_type_calloc
+ _objc_retainBlock
+ _xpc_array_append_value
+ _xpc_array_create
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
- _NSLog
- _objc_release_x1
CStrings:
+ "-[PSOrchestrator(Policy) updateGraphTargetState:fromPolicy:]"
+ "-[PSOrchestrator_v2(Policy) updateGraphTargetState:fromPolicy:]"
+ "04:10:57"
+ "@\"PSOrchestratorStatisticsDelegate\""
+ "@32@0:8Q16@?24"
+ "@52@0:8@16@24@32B40@44"
+ "Jun 26 2025"
+ "OrchestratorStatistics: New max duration: %.1f ms, Seconds since boot: %.1f, Orchestration number: %llu"
+ "PSOrchestratorStatisticsDelegate"
+ "Q8@?0"
+ "Strides current:%@ target:%@ requested:%@ Frequency current:%@ target:%@ Bounds lower:%@ upper:%@ domain:%@"
+ "T@\"NSMutableDictionary\",&,N,V_graphToDesiredLowerBoundStride"
+ "T@\"NSNumber\",&,N,V_lowerBoundStride"
+ "T@\"NSNumber\",&,N,V_policyTargetLowerBoundStride"
+ "T@\"NSNumber\",&,N,V_upperBoundStride"
+ "T@\"PSOrchestratorStatisticsDelegate\",&,N,V_statisticsDelegate"
+ "Two policies are trying to set target strides. This is an invalid configuration! Aborting!"
+ "^{historyEntry=QQ}"
+ "_allTimeStatistics"
+ "_getTime"
+ "_graphToDesiredLowerBoundStride"
+ "_lowerBoundStride"
+ "_policyTargetLowerBoundStride"
+ "_recentHistory"
+ "_recentHistoryBufferCapacity"
+ "_startTime"
+ "_statisticsDelegate"
+ "_upperBoundStride"
+ "allTimeStatistics"
+ "applyPolicyConstraints:withDesiredStride:"
+ "desired stride for %@ is %@"
+ "didEndOrchestration"
+ "dumpStateToXPCDictionary:"
+ "duration"
+ "frameIdUpdateWithVirtualStride:frameId:"
+ "graphToDesiredLowerBoundStride"
+ "history"
+ "historyCount"
+ "initWithGSM:shouldUseOrchestratorV2:"
+ "initWithHistoryCapacity:getTime:"
+ "initWithQueue:withBuilder:withGSTManager:isSessionForLocalReplay:withSystemPulseRate:"
+ "inputResourcesForGraph:"
+ "lowerBoundStride"
+ "mutableCopy"
+ "numberOfOrchestrationsRecorded"
+ "orchestrationNumber"
+ "orchestrator_statistics"
+ "policyTargetLowerBoundStride"
+ "setGraphToDesiredLowerBoundStride:"
+ "setLowerBoundStride:"
+ "setPolicyTargetLowerBoundStride:"
+ "setStatisticsDelegate:"
+ "setUpperBoundStride:"
+ "startTimestamp"
+ "statistics"
+ "statisticsDelegate"
+ "total"
+ "upperBoundStride"
+ "willStartOrchestration"
+ "{?=\"max\"{?=\"start\"Q\"duration\"Q\"orchestrationNumber\"Q}\"total\"Q\"numberOfOrchestrations\"Q}"
+ "\x82"
- "00:28:34"
- "Jun 14 2025"
- "PSMSGUtilities"
- "T@\"NSNumber\",&,N,V_policyTargetStride"
- "_policyTargetStride"
- "currentDisplayFrequency"
- "d16@0:8"
- "desired freq for %@ is %@, desired Stride is %@ , requested is %@"
- "policyTargetStride"
- "setPolicyTargetStride:"
- "sharedInstance"

```
