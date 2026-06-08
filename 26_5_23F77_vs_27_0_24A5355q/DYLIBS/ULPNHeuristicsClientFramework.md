## ULPNHeuristicsClientFramework

> `/System/Library/PrivateFrameworks/ULPNHeuristicsClientFramework.framework/ULPNHeuristicsClientFramework`

```diff

-142.100.19.0.0
-  __TEXT.__text: 0x156c0
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__const: 0xf40
-  __TEXT.__constg_swiftt: 0x748
-  __TEXT.__swift5_typeref: 0x4db
-  __TEXT.__swift5_reflstr: 0x704
-  __TEXT.__swift5_fieldmd: 0x600
+236.0.0.0.1
+  __TEXT.__text: 0x16558
+  __TEXT.__const: 0xfd0
+  __TEXT.__constg_swiftt: 0x7a0
+  __TEXT.__swift5_typeref: 0x519
+  __TEXT.__swift5_reflstr: 0x754
+  __TEXT.__swift5_fieldmd: 0x64c
   __TEXT.__cstring: 0x520
-  __TEXT.__oslogstring: 0x694
+  __TEXT.__oslogstring: 0x6c4
   __TEXT.__swift5_capture: 0x1c
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x390
-  __TEXT.__eh_frame: 0x298
-  __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x3b3
-  __TEXT.__objc_methtype: 0x47
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x130
+  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__eh_frame: 0x2a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH_CONST.__const: 0x968
-  __AUTH_CONST.__objc_const: 0x570
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x978
+  __AUTH_CONST.__objc_const: 0x590
+  __AUTH_CONST.__auth_got: 0x490
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x858
-  __DATA.__data: 0x2c0
+  __AUTH.__data: 0x898
+  __DATA.__data: 0x2b8
+  __DATA.__common: 0x10
   __DATA.__bss: 0xb80
-  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8737EC54-0C18-39D5-92F5-7815E64317FA
-  Functions: 358
-  Symbols:   300
-  CStrings:  114
+  UUID: BD0C66ED-B593-3638-A3CF-C2E0AA0F4D98
+  Functions: 356
+  Symbols:   331
+  CStrings:  68
 
Symbols:
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_project_boxed_opaque_existential_1
+ _objc_retain_x20
+ _swift_release_x1
+ _swift_release_x10
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _symbolic $s29ULPNHeuristicsClientFramework24ULPNDiagnosticsReportingP
+ _symbolic ______p 29ULPNHeuristicsClientFramework24ULPNDiagnosticsReportingP
- _symbolic _____Sg 7Network7NWErrorO
CStrings:
+ "Pair diagnostic: %s on %s (delta: %lds)"
- "@\"NSDictionary\"8@?0"
- "OffloadStateDisconnectionInfo"
- "WSSParameterSnapshots"
- "_TtC29ULPNHeuristicsClientFramework14PushHeuristics"
- "_TtC29ULPNHeuristicsClientFramework14ULPNHeuristics"
- "_TtC29ULPNHeuristicsClientFramework17RunningAverageEMA"
- "_TtC29ULPNHeuristicsClientFramework20PushTelemetryHandler"
- "_TtC29ULPNHeuristicsClientFramework25ULPNHeuristicsDiagnostics"
- "alpha"
- "code"
- "cosStorage"
- "defaultOffloadState"
- "delegate"
- "diagnosticReporter"
- "ema"
- "emaValues"
- "excessiveFailuresTimestamp"
- "failureEventHistory"
- "init"
- "initWithInt:"
- "initWithInteger:"
- "interface"
- "isDiagnosticsEnabled"
- "lastSnapshotFailureTimestamp"
- "lastSuccessfulReportTimestamp"
- "lastUpdateTime"
- "log"
- "minimumSnapshotFailureRetryInterval"
- "minimumSuccessReportInterval"
- "offloadState"
- "processInfo"
- "processName"
- "pskOffloadingSeenOnce"
- "pushHeuristics"
- "setDateFormat:"
- "setDateStyle:"
- "setTimeStyle:"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "smoothingFactor"
- "snapshotWithSignature:duration:event:payload:reply:"
- "stringFromDate:"
- "telemetryHandlers"
- "timeProvider"
- "timeUnit"
- "useEventRateNormalization"
- "v16@?0@\"NSDictionary\"8"
- "weightScorer"

```
