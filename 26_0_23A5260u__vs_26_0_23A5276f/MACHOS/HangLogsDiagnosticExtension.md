## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-375.0.0.0.0
-  __TEXT.__text: 0x10fb8
-  __TEXT.__auth_stubs: 0x9a0
+378.0.0.0.0
+  __TEXT.__text: 0x11350
+  __TEXT.__auth_stubs: 0x990
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_stubs: 0x1840
-  __TEXT.__objc_methlist: 0xb34
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x2527
-  __TEXT.__oslogstring: 0x17dd
+  __TEXT.__objc_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0xb24
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0x2476
+  __TEXT.__oslogstring: 0x1892
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__objc_methname: 0x3f87
+  __TEXT.__objc_methname: 0x4032
   __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methtype: 0x751
+  __TEXT.__objc_methtype: 0x78e
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__cfstring: 0x2480
+  __TEXT.__unwind_info: 0x3a8
+  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__cfstring: 0x2380
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1eb8
-  __DATA.__objc_selrefs: 0xa98
-  __DATA.__objc_ivar: 0x218
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA.__objc_const: 0x1e58
+  __DATA.__objc_selrefs: 0xb20
+  __DATA.__objc_ivar: 0x210
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0xb4
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D281F789-B761-3592-A147-0CD49CE5EC41
+  UUID: 8069B0D1-6606-304D-A6F2-A3255A8B65A1
   Functions: 414
-  Symbols:   431
-  CStrings:  1413
+  Symbols:   434
+  CStrings:  1414
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _addNewTaskStateToHangEvent
- _ADClientPushValueForDistributionKey
- _HTAggdPushValueForDistributionKey
- _kHTPrefsMemoryLoggingEnabled
- _kHTPrefsMemoryLoggingIntervalSec
CStrings:
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
+ "Hang detected below telemetry threshold: hang duration = %.2fms, telemetry treshold = %.2dms"
+ "One or more of required XPC Keys were not received by hangtracerd"
+ "Received RB Notification for state change of process '%s'. State changed from %d to %d"
+ "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
+ "There is no HTMonitorPidHangEvent for process with pid %d and bundleInfo %{public}@"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
+ "_updateRunningBoardProcessMonitor"
+ "bundle"
+ "descriptor"
+ "identifierWithPid:"
+ "monitorWithConfiguration:"
+ "objectForKey:"
+ "predicateMatchingIdentifiers:"
+ "previousState"
+ "received XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
+ "received an unexpected XPC response from hangtracerd"
+ "removeObject:"
+ "removePidFromProcessMonitoring:"
+ "set"
+ "setPredicates:"
+ "setServiceClass:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "setValues:"
+ "setupRunningBoardProcessMonitorForPid:"
+ "state"
+ "stateInfo"
+ "taskState"
+ "updateConfiguration:"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "\xf0\xf0A!V!"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
- "Hang detected below aggd threshold: hang duration = %.2fms, aggd treshold = %.2dms"
- "HangTracerEnableMemoryLogging"
- "HangTracerMemoryLoggingInterval"
- "One or more of required XPC Keys were not recieved by hangtracerd"
- "Recieved XPC_ERROR_CONNECTION_INVALID connection from HangTracer with reason: %s"
- "Recieved an unexpected XPC response from hangtracerd"
- "TB,R,V_memoryLoggingEnabled"
- "TI,V_memoryLoggingIntervalSec"
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
- "_memoryLoggingEnabled"
- "_memoryLoggingIntervalSec"
- "com.apple.ht_always_on.%s.%s"
- "com.apple.ht_assertion_overlap.%s.%s"
- "com.apple.ht_assertion_stats.hang_overlap_ms"
- "com.apple.ht_assertion_stats.hang_overlap_percent"
- "com.apple.ht_debugger_attached.%s.%s"
- "com.apple.ht_extended_launch_overlap.%s.%s"
- "initPropertyMemoryLoggingIntervalSec:"
- "memoryLoggingEnabled"
- "memoryLoggingIntervalSec"
- "setMemoryLoggingIntervalSec:"
- "v20@0:8I16"
- "\xf0\xf0Q!V!"

```
